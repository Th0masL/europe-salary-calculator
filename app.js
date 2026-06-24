/* Europe Salary Calculator — vanilla JS, no dependencies.
 *
 * Each country exposes 4 data points {gross, cost, net}, all monotonically
 * increasing together. Given any one of the three values we interpolate the
 * other two: find the bracketing segment on the chosen axis, compute the
 * fraction t, and linearly interpolate every field. Outside the known range we
 * extrapolate from the nearest segment (and flag it).
 */
(function () {
  "use strict";

  var SOURCES = {
    consensus: { label: "Consensus", data: window.SALARY_DATA_CONSENSUS },
    ebook: { label: "2025 eBook", data: window.SALARY_DATA_EBOOK },
    skuad: { label: "Skuad (live)", data: window.SALARY_DATA_SKUAD },
    deel: { label: "Deel (live)", data: window.SALARY_DATA_DEEL },
    formula: { label: "Formula", data: window.SALARY_DATA_FORMULA },
  };
  var DEFAULT_SOURCE = ["consensus", "ebook", "skuad", "deel", "formula"]
    .find(function (s) { return SOURCES[s].data; });
  if (!DEFAULT_SOURCE) {
    document.getElementById("resultsBody").innerHTML =
      '<tr><td colspan="8" class="empty">Could not load any data files (data/*.js)</td></tr>';
    return;
  }

  function currentData() {
    return (SOURCES[state.source] && SOURCES[state.source].data) || SOURCES[DEFAULT_SOURCE].data;
  }

  // Cost-of-living override (current Numbeo data, refreshed by tools/fetch_numbeo.py).
  // Takes precedence over the values embedded in the salary datasets.
  var COL = window.COST_OF_LIVING || {};

  // Metadata (flag, EU/US, cost of living) by country name, from the richest
  // source. Lean fetchers (Deel) only carry {name, points}, so we backfill.
  var META = {};
  ["ebook", "consensus", "skuad"].forEach(function (s) {
    if (!SOURCES[s].data) return;
    SOURCES[s].data.countries.forEach(function (c) {
      if (!META[c.name]) META[c.name] = c;
    });
  });

  // Canonical, ordered list of every location across all sources. The table
  // always shows this full list; a source that lacks a location renders it with
  // "—" (so e.g. the Formula source shows only Estonia + US filled in).
  var MASTER = [];
  (function () {
    var seen = {};
    ["consensus", "ebook", "skuad", "deel", "formula"].forEach(function (s) {
      if (!SOURCES[s].data) return;
      SOURCES[s].data.countries.forEach(function (c) {
        if (!seen[c.name]) { seen[c.name] = 1; MASTER.push(c.name); }
      });
    });
  })();

  var MODES = {
    cost: { label: "Total employer budget (per year)", noun: "employer budget", best: "highest take-home" },
    gross: { label: "Gross salary (per year)", noun: "gross salary", best: "highest take-home" },
    net: { label: "Target net take-home (per year)", noun: "net pay", best: "cheapest for the employer" },
  };
  var PRESETS = [50000, 75000, 100000, 150000, 200000];

  var state = {
    source: DEFAULT_SOURCE,
    mode: "cost",
    amount: 100000,
    euOnly: false,
    monthly: false,
    search: "",
    sortKey: "net",
    sortDir: -1, // -1 desc, 1 asc
  };

  // Hydrate from the URL query so views are shareable/bookmarkable.
  (function readURL() {
    var q = new URLSearchParams(location.search);
    if (SOURCES[q.get("source")] && SOURCES[q.get("source")].data) state.source = q.get("source");
    if (MODES[q.get("mode")]) state.mode = q.get("mode");
    var amt = parseFloat(q.get("amount"));
    if (!isNaN(amt) && amt > 0) state.amount = amt;
    if (q.get("eu") === "1") state.euOnly = true;
    if (q.get("monthly") === "1") state.monthly = true;
  })();

  function writeURL() {
    var q = new URLSearchParams();
    q.set("source", state.source);
    q.set("mode", state.mode);
    q.set("amount", String(Math.round(state.amount)));
    if (state.euOnly) q.set("eu", "1");
    if (state.monthly) q.set("monthly", "1");
    history.replaceState(null, "", "?" + q.toString());
  }

  // ---- interpolation ------------------------------------------------------

  function lerp(a, b, t) { return a + (b - a) * t; }

  // Solve a country for a given axis value. axis is "cost" | "gross" | "net".
  // Some sources (Deel) may lack a metric for a few countries, so we only use
  // points that carry the axis we're solving on, and only interpolate the other
  // metrics where both endpoints provide them. Returns null if not solvable.
  function solve(country, axis, value) {
    var pts = country.points.filter(function (p) { return p[axis] != null; });
    var n = pts.length;
    if (n < 2) return null;
    var lo = pts[0][axis], hi = pts[n - 1][axis];
    var i, t, extrapolated = false;

    if (value <= lo) {
      i = 0; extrapolated = value < lo;
    } else if (value >= hi) {
      i = n - 2; extrapolated = value > hi;
    } else {
      for (i = 0; i < n - 1; i++) {
        if (value >= pts[i][axis] && value <= pts[i + 1][axis]) break;
      }
    }
    var a = pts[i], b = pts[i + 1];
    var span = b[axis] - a[axis];
    t = span === 0 ? 0 : (value - a[axis]) / span;

    function lerpKey(key) {
      return (a[key] != null && b[key] != null) ? lerp(a[key], b[key], t) : null;
    }
    var res = {
      gross: lerpKey("gross"),
      cost: lerpKey("cost"),
      net: lerpKey("net"),
      extrapolated: extrapolated,
    };
    res[axis] = value; // keep the input exact
    if (res.net != null && res.net < 0) res.net = 0;
    return res;
  }

  // ---- formatting ---------------------------------------------------------

  var eur0 = new Intl.NumberFormat("en-IE", { style: "currency", currency: "EUR", maximumFractionDigits: 0 });

  function money(v) {
    if (v == null) return "—";
    var n = state.monthly ? v / 12 : v;
    return eur0.format(Math.round(n));
  }
  function plainNum(v) { return new Intl.NumberFormat("en-US").format(Math.round(v)); }

  // ---- computation for the whole table ------------------------------------

  function compute() {
    var byName = {};
    currentData().countries.forEach(function (c) { byName[c.name] = c; });

    var rows = MASTER
      .filter(function (name) {
        var eu = (META[name] || {}).eu;
        return !state.euOnly || eu;
      })
      .filter(function (name) {
        return !state.search || name.toLowerCase().indexOf(state.search.toLowerCase()) !== -1;
      })
      .map(function (name) {
        var c = byName[name] || {};
        var m = META[name] || {};
        var col = COL[name] != null ? COL[name]
          : (c.costOfLiving != null ? c.costOfLiving : m.costOfLiving);
        var base = {
          name: name,
          flag: c.flag || m.flag || "🏳️",
          eu: c.eu != null ? c.eu : m.eu,
          us: !!(c.us || m.us), approx: !!c.approx,
          costOfLiving: col,
          costNote: c.costNote || null,   // employer-cost breakdown (Formula source only)
        };
        var s = byName[name] ? solve(c, state.mode, state.amount) : null;
        if (!s) {
          // this source has no data for this location → a "—" row
          base.cost = base.gross = base.net = null;
          base.netRatio = base.costPerNet = base.surplus = null;
          base.extrapolated = false;
          return base;
        }
        base.cost = s.cost; base.gross = s.gross; base.net = s.net;
        base.netRatio = (s.cost > 0 && s.net != null) ? s.net / s.cost : null;
        base.costPerNet = (s.net > 0 && s.cost != null) ? s.cost / s.net : null;
        base.surplus = (s.net != null && col != null) ? s.net - col : null;
        base.extrapolated = s.extrapolated;
        return base;
      });

    var key = state.sortKey, dir = state.sortDir;
    rows.sort(function (a, b) {
      if (key === "name") return a.name.localeCompare(b.name) * dir;
      var av = a[key], bv = b[key];
      if (av == null && bv == null) return 0;
      if (av == null) return 1;   // missing values sort last
      if (bv == null) return -1;
      return (av - bv) * dir;
    });
    return rows;
  }

  // ---- rendering ----------------------------------------------------------

  function render() {
    var rows = compute();
    var body = document.getElementById("resultsBody");

    if (!rows.length) {
      body.innerHTML = '<tr><td colspan="8" class="empty">No countries match your filter.</td></tr>';
    } else {
      body.innerHTML = rows.map(function (r, idx) {
        var hasSurplus = r.surplus != null;
        var surplusCls = !hasSurplus ? "" : r.surplus >= 0 ? "surplus-pos" : "surplus-neg";
        var topCls = idx === 0 && (state.sortKey === "net" || state.sortKey === "surplus") && state.sortDir === -1 ? "top-row" : "";
        var warn = r.extrapolated
          ? ' <span class="extrap" title="Outside the benchmark range — extrapolated, less reliable">*</span>' : "";
        var approx = r.approx
          ? '<span class="approx" title="Single-benchmark estimate: one US data point, converted from USD (1 EUR = 1.13 USD) and modelled at a flat rate. Least precise away from ~€100k.">≈</span> ' : "";
        var tag = r.eu ? '<span class="eu-tag">EU</span>'
          : r.us ? '<span class="us-tag">US</span>' : "";
        // Employer-cost cell: if this source carries a breakdown (Formula), show it
        // on hover so the number is auditable line-by-line.
        var costCell = money(r.cost);
        if (r.costNote && r.cost != null) {
          var t = r.costNote.replace(/&/g, "&amp;").replace(/"/g, "&quot;")
            .replace(/</g, "&lt;").replace(/>/g, "&gt;")
            .replace(/ \+ /g, "&#10;");   // each " + " component on its own line (&#10; = newline)
          costCell = '<span class="has-note" title="Employer cost:&#10;' + t + '">' + costCell + "</span>";
        }
        return (
          '<tr class="' + topCls + '">' +
            '<td class="rank">' + (idx + 1) + "</td>" +
            '<td class="country"><span class="country-cell"><span class="flag">' + r.flag +
              '</span><span class="cname">' + r.name + "</span>" + tag + "</span></td>" +
            '<td class="val-strong">' + approx + costCell + warn + "</td>" +
            "<td>" + money(r.gross) + "</td>" +
            '<td class="val-net">' + money(r.net) + "</td>" +
            "<td>" + (r.netRatio != null ? Math.round(r.netRatio * 100) + "%" : "—") + "</td>" +
            "<td>" + (r.costPerNet != null ? "€" + r.costPerNet.toFixed(2) : "—") + "</td>" +
            '<td class="' + surplusCls + '">' +
              (hasSurplus ? (r.surplus >= 0 ? "+" : "−") + money(Math.abs(r.surplus)) : "—") + "</td>" +
          "</tr>"
        );
      }).join("");
    }

    renderSummary(rows);
    syncSortIndicators();
    writeURL();
  }

  function renderSummary(rows) {
    var el = document.getElementById("summary");
    if (!rows.length) { el.innerHTML = ""; return; }
    var mode = MODES[state.mode];
    // best = best for the user given the mode (ignoring rows missing that metric)
    var best;
    if (state.mode === "net") {
      var withCost = rows.filter(function (r) { return r.cost != null; });
      best = withCost.reduce(function (a, b) { return b.cost < a.cost ? b : a; }, withCost[0]);
    } else {
      var withNet = rows.filter(function (r) { return r.net != null; });
      best = withNet.reduce(function (a, b) { return b.net > a.net ? b : a; }, withNet[0]);
    }
    if (!best) { el.innerHTML = ""; return; }
    var per = state.monthly ? " / month" : " / year";
    var html;
    if (state.mode === "cost") {
      html = "With an employer budget of <b>" + money(state.amount) + "</b>" + per +
        ", <strong>" + best.flag + " " + best.name + "</strong> gives the highest take-home: " +
        "<b>" + money(best.net) + "</b>" + per + " net" +
        ' <span class="muted">(gross ' + money(best.gross) + ").</span>";
    } else if (state.mode === "gross") {
      html = "For a gross salary of <b>" + money(state.amount) + "</b>" + per +
        ", the best net take-home is in <strong>" + best.flag + " " + best.name + "</strong>: " +
        "<b>" + money(best.net) + "</b>" + per +
        ' <span class="muted">(costs the employer ' + money(best.cost) + ").</span>";
    } else {
      html = "To deliver a net take-home of <b>" + money(state.amount) + "</b>" + per +
        ", <strong>" + best.flag + " " + best.name + "</strong> is cheapest for the employer: " +
        "<b>" + money(best.cost) + "</b>" + per +
        ' <span class="muted">(gross ' + money(best.gross) + ").</span>";
    }
    el.innerHTML = '<div class="card"><span class="lead">' + html + "</span>" +
      '<span class="src-note">' + sourceNote() + "</span></div>";
  }

  function sourceNote() {
    var meta = currentData().meta || {};
    var when = meta.fetched ? " · fetched " + meta.fetched : "";
    if (state.source === "consensus") {
      return "Source: Consensus — Europe: median of eBook + Skuad + Deel (outliers dropped); " +
        "US: direct 2025 calc from published rates (no EOR)" + when + ".";
    }
    if (state.source === "skuad") {
      return "Source: Skuad live calculator" + when +
        " · 35 European countries (Slovenia n/a) + 5 US cities (blog-based).";
    }
    if (state.source === "deel") {
      return "Source: Deel live calculators" + when +
        " · cost from employee-cost tool (EOR fee removed), net from take-home tool.";
    }
    if (state.source === "formula") {
      var fx = meta.fxAsOf ? " · non-euro rows (PL/DK/SE/CZ) converted at FX rates from " + meta.fxAsOf : "";
      return "Source: Formula — computed from each country's published tax rates (no vendor)" +
        when + fx + ". Countries not yet implemented show blank (—).";
    }
    return "Source: Boundless 2025 eBook · 36 European countries + 5 US cities.";
  }

  function syncSortIndicators() {
    document.querySelectorAll("thead th").forEach(function (th) {
      th.classList.remove("sorted-asc", "sorted-desc");
      if (th.dataset.sort === state.sortKey) {
        th.classList.add(state.sortDir === -1 ? "sorted-desc" : "sorted-asc");
      }
    });
  }

  // ---- input parsing ------------------------------------------------------

  function parseAmount(str) {
    var n = parseFloat(String(str).replace(/[^0-9.]/g, ""));
    return isNaN(n) ? 0 : n;
  }

  // ---- wiring -------------------------------------------------------------

  var amountInput = document.getElementById("amount");
  var amountLabel = document.getElementById("amountLabel");

  function setMode(mode) {
    state.mode = mode;
    document.querySelectorAll(".seg").forEach(function (b) {
      b.setAttribute("aria-checked", b.dataset.mode === mode ? "true" : "false");
    });
    amountLabel.textContent = MODES[mode].label;
    // sensible default sort per mode
    state.sortKey = mode === "net" ? "cost" : "net";
    state.sortDir = -1;
    if (mode === "net") state.sortDir = 1; // cheapest employer cost first
    render();
  }

  document.querySelectorAll(".seg").forEach(function (btn) {
    btn.addEventListener("click", function () { setMode(btn.dataset.mode); });
  });

  function setSource(source) {
    if (!SOURCES[source] || !SOURCES[source].data) return;
    state.source = source;
    document.querySelectorAll(".src").forEach(function (b) {
      b.setAttribute("aria-checked", b.dataset.source === source ? "true" : "false");
    });
    render();
  }

  document.querySelectorAll(".src").forEach(function (btn) {
    btn.addEventListener("click", function () { setSource(btn.dataset.source); });
  });

  amountInput.addEventListener("input", function () {
    state.amount = parseAmount(amountInput.value);
    render();
  });
  amountInput.addEventListener("blur", function () {
    if (state.amount > 0) amountInput.value = plainNum(state.amount);
  });

  document.getElementById("euOnly").addEventListener("change", function (e) {
    state.euOnly = e.target.checked; render();
  });
  document.getElementById("showMonthly").addEventListener("change", function (e) {
    state.monthly = e.target.checked; render();
  });
  document.getElementById("search").addEventListener("input", function (e) {
    state.search = e.target.value; render();
  });

  document.querySelectorAll("thead th").forEach(function (th) {
    th.addEventListener("click", function () {
      var key = th.dataset.sort;
      if (!key || key === "rank") return;
      if (state.sortKey === key) { state.sortDir *= -1; }
      else { state.sortKey = key; state.sortDir = key === "name" ? 1 : -1; }
      render();
    });
  });

  // presets
  var chips = document.getElementById("presets");
  chips.innerHTML = PRESETS.map(function (v) {
    return '<button class="chip" data-v="' + v + '">' + eur0.format(v) + "</button>";
  }).join("");
  chips.addEventListener("click", function (e) {
    var b = e.target.closest(".chip");
    if (!b) return;
    state.amount = parseFloat(b.dataset.v);
    amountInput.value = plainNum(state.amount);
    render();
  });

  // init — reflect hydrated state into the DOM, then render
  amountInput.value = plainNum(state.amount);
  document.getElementById("euOnly").checked = state.euOnly;
  document.getElementById("showMonthly").checked = state.monthly;
  // disable a source button if its data file failed to load
  document.querySelectorAll(".src").forEach(function (b) {
    if (!SOURCES[b.dataset.source].data) b.setAttribute("disabled", "");
    b.setAttribute("aria-checked", b.dataset.source === state.source ? "true" : "false");
  });
  setMode(state.mode);
})();
