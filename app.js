/* Europe Salary Calculator — vanilla JS, no dependencies.
 *
 * Each country exposes data points {gross, cost, net}, all monotonically
 * increasing together. Given any one of the three values we interpolate the
 * other two: find the bracketing segment on the chosen axis, compute the
 * fraction t, and linearly interpolate every field. Outside the generated
 * generated range we return null (the row shows "—") rather than extrapolating.
 */
(function () {
  "use strict";

  var root = document.documentElement;
  var themeMeta = document.querySelector('meta[name="theme-color"]');
  var themeButtons = document.querySelectorAll('button[data-theme-choice]');
  var media = window.matchMedia('(prefers-color-scheme: dark)');
  var storageKey = 'europe-salary-theme';

  function savedTheme() {
    try {
      var saved = localStorage.getItem(storageKey);
      return saved === 'light' || saved === 'dark' ? saved : 'system';
    } catch (error) {
      return 'system';
    }
  }

  function persistTheme(choice) {
    try {
      if (choice === 'system') localStorage.removeItem(storageKey);
      else localStorage.setItem(storageKey, choice);
    } catch (error) {}
  }

  function applyTheme(choice, persist) {
    if (choice !== 'light' && choice !== 'dark') choice = 'system';

    if (choice === 'system') root.removeAttribute('data-theme');
    else root.setAttribute('data-theme', choice);
    root.setAttribute('data-theme-choice', choice);

    var resolved = choice === 'system' ? (media.matches ? 'dark' : 'light') : choice;
    root.style.colorScheme = resolved;
    var background = getComputedStyle(root).getPropertyValue('--color-bg').trim();
    if (background) themeMeta.setAttribute('content', background);

    Array.prototype.forEach.call(themeButtons, function (button) {
      button.setAttribute('aria-pressed', String(button.getAttribute('data-theme-choice') === choice));
    });

    if (persist) persistTheme(choice);
  }

  Array.prototype.forEach.call(themeButtons, function (button) {
    button.addEventListener('click', function () {
      applyTheme(button.getAttribute('data-theme-choice'), true);
    });
  });

  function systemThemeChanged() {
    if (root.getAttribute('data-theme-choice') === 'system') applyTheme('system', false);
  }
  if (media.addEventListener) media.addEventListener('change', systemThemeChanged);
  else if (media.addListener) media.addListener(systemThemeChanged);

  applyTheme(root.getAttribute('data-theme-choice') || savedTheme(), false);
}());

(function () {
  "use strict";

  var DATA = window.SALARY_DATA_FORMULA;
  if (!DATA) {
    document.getElementById("resultsBody").innerHTML =
      '<tr><td colspan="9" class="empty">Could not load the salary calculation data.</td></tr>';
    return;
  }

  // Cost-of-living override (current Numbeo data, refreshed by tools/fetch_numbeo.py).
  // Takes precedence over the values embedded in the salary datasets.
  var COL = window.COST_OF_LIVING || {};

  // Escape data-derived strings before they go into innerHTML / a title attribute.
  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/"/g, "&quot;")
      .replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  // Metadata (flag, EU/US, cost of living) by country name.
  var META = {};
  DATA.countries.forEach(function (c) {
    META[c.name] = c;
  });

  var MASTER = DATA.countries.map(function (c) { return c.name; });

  var MODES = {
    cost: { label: "Total employer budget (per year)", noun: "employer budget", best: "highest take-home" },
    gross: { label: "Gross salary (per year)", noun: "gross salary", best: "highest take-home" },
    net: { label: "Target net take-home (per year)", noun: "net pay", best: "cheapest for the employer" },
  };
  var PRESETS = [50000, 75000, 100000, 150000, 200000];
  var ECB_FX_URL = "https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?lastNObservations=1&format=csvdata";
  var FX_OVERRIDE_KEY = "europe-salary-eur-usd-override";
  var FX_CACHE_KEY = "europe-salary-eur-usd-cache";
  var FX_REFRESH_MS = 24 * 60 * 60 * 1000;
  var bundledEurUsd = Number((DATA.meta || {}).usFxEurUsd) || 1.134;

  function readStoredFx(key) {
    try {
      var value = JSON.parse(localStorage.getItem(key));
      if (value && Number(value.rate) > 0) return value;
    } catch (error) {}
    return null;
  }

  var storedOverride = readStoredFx(FX_OVERRIDE_KEY);
  var cachedFx = readStoredFx(FX_CACHE_KEY);
  var initialFx = storedOverride || cachedFx;

  var state = {
    mode: "cost",
    amount: 100000, // canonical annual EUR; converted only at the UI boundary
    euOnly: false,
    euroOnly: false,
    monthly: false,
    showLivingCosts: false,
    displayCurrency: "EUR",
    eurUsd: initialFx ? Number(initialFx.rate) : bundledEurUsd,
    fxSource: storedOverride ? "manual" : cachedFx ? "cached" : "bundled",
    fxDate: initialFx ? initialFx.date || null : null,
    search: "",
    sortKey: "net",
    sortDir: -1, // -1 desc, 1 asc
  };

  // Hydrate from the URL query so views are shareable/bookmarkable.
  (function readURL() {
    var q = new URLSearchParams(location.search);
    if (MODES[q.get("mode")]) state.mode = q.get("mode");
    var amt = parseFloat(q.get("amount"));
    if (!isNaN(amt) && amt > 0) state.amount = amt;
    if (q.get("eu") === "1") state.euOnly = true;
    if (q.get("euro") === "1") state.euroOnly = true;
    if (q.get("monthly") === "1") state.monthly = true;
    if (q.get("living") === "1") state.showLivingCosts = true;
    if (q.get("currency") === "USD") state.displayCurrency = "USD";
    var fx = parseFloat(q.get("fx"));
    if (!isNaN(fx) && fx > 0) {
      state.eurUsd = fx;
      state.fxSource = "manual";
      state.fxDate = null;
    }
  })();

  function writeURL() {
    var q = new URLSearchParams();
    q.set("mode", state.mode);
    q.set("amount", String(Math.round(state.amount)));
    if (state.euOnly) q.set("eu", "1");
    if (state.euroOnly) q.set("euro", "1");
    if (state.monthly) q.set("monthly", "1");
    if (state.showLivingCosts) q.set("living", "1");
    if (state.displayCurrency === "USD") q.set("currency", "USD");
    if (state.fxSource === "manual") q.set("fx", String(state.eurUsd));
    history.replaceState(null, "", "?" + q.toString());
  }

  // ---- interpolation ------------------------------------------------------

  function lerp(a, b, t) { return a + (b - a) * t; }

  function pointsInEur(country) {
    if (country.nativeCurrency === "USD" && country.nativePoints && state.eurUsd > 0) {
      return country.nativePoints.map(function (point) {
        return {
          gross: point.gross / state.eurUsd,
          cost: point.cost / state.eurUsd,
          net: point.net / state.eurUsd,
        };
      });
    }
    return country.points;
  }

  // Solve a country for a given axis value. axis is "cost" | "gross" | "net".
  // Only use points that carry the axis we're solving on, and interpolate the
  // other metrics where both endpoints provide them. Returns null if not solvable.
  function solve(country, axis, value) {
    var pts = pointsInEur(country).filter(function (p) { return p[axis] != null; });
    var n = pts.length;
    if (n < 2) return null;
    var lo = pts[0][axis], hi = pts[n - 1][axis];
    // Don't extrapolate beyond the generated range; return null so the
    // row shows "—".
    if (value < lo || value > hi) return null;
    var i, t;

    if (value <= lo) {
      i = 0;
    } else if (value >= hi) {
      i = n - 2;
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
    };
    res[axis] = value; // keep the input exact
    if (res.net != null && res.net < 0) res.net = 0;
    return res;
  }

  // ---- formatting ---------------------------------------------------------

  var formatters = {
    EUR: new Intl.NumberFormat("en-IE", { style: "currency", currency: "EUR", maximumFractionDigits: 0 }),
    USD: new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 }),
  };

  function toDisplayCurrency(value) {
    return state.displayCurrency === "USD" ? value * state.eurUsd : value;
  }

  function fromDisplayCurrency(value) {
    return state.displayCurrency === "USD" ? value / state.eurUsd : value;
  }

  function money(v) {
    if (v == null) return "—";
    var n = state.monthly ? toDisplayCurrency(v) / 12 : toDisplayCurrency(v);
    return formatters[state.displayCurrency].format(Math.round(n));
  }
  function plainNum(v) { return new Intl.NumberFormat("en-US").format(Math.round(v)); }

  // ---- computation for the whole table ------------------------------------

  function compute() {
    var byName = {};
    DATA.countries.forEach(function (c) { byName[c.name] = c; });

    var rows = MASTER
      .filter(function (name) {
        var eu = (META[name] || {}).eu;
        return !state.euOnly || eu;
      })
      .filter(function (name) {
        var currency = (META[name] || {}).currency;
        return !state.euroOnly || currency === "EUR";
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
          costNote: c.costNote || null,
        };
        var s = byName[name] ? solve(c, state.mode, state.amount) : null;
        if (!s) {
          // This amount falls outside the generated range → a "—" row.
          base.cost = base.gross = base.net = null;
          base.netRatio = base.costPerNet = base.surplus = null;
          return base;
        }
        base.cost = s.cost; base.gross = s.gross; base.net = s.net;
        base.netRatio = (s.cost > 0 && s.net != null) ? s.net / s.cost : null;
        base.costPerNet = (s.net > 0 && s.cost != null) ? s.cost / s.net : null;
        base.surplus = (s.net != null && col != null) ? s.net - col : null;
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
    document.getElementById("resultsTable").classList.toggle("show-living-costs", state.showLivingCosts);

    if (!rows.length) {
      body.innerHTML = '<tr><td colspan="9" class="empty">No countries match your filter.</td></tr>';
    } else {
      body.innerHTML = rows.map(function (r, idx) {
        var hasSurplus = r.surplus != null;
        var surplusCls = !hasSurplus ? "" : r.surplus >= 0 ? "surplus-pos" : "surplus-neg";
        var approx = r.approx
          ? '<span class="approx" title="Single-benchmark estimate: one US data point, converted from USD (1 EUR = 1.13 USD) and modelled at a flat rate. Least precise away from ~€100k.">≈</span> ' : "";
        var tag = r.eu ? '<span class="eu-tag">EU</span>'
          : r.us ? '<span class="us-tag">US</span>' : "";
        // Show the employer-cost breakdown on hover so the number is
        // auditable line-by-line.
        var costCell = money(r.cost);
        if (r.costNote && r.cost != null) {
          // each " + " component on its own line (&#10; = newline)
          var t = esc(r.costNote).replace(/ \+ /g, "&#10;");
          costCell = '<span class="has-note" title="Employer cost:&#10;' + t + '">' + costCell + "</span>";
        }
        return (
          "<tr>" +
            '<td class="rank">' + (idx + 1) + "</td>" +
            '<td class="country"><span class="country-cell"><span class="flag">' + esc(r.flag) +
              '</span><span class="cname">' + esc(r.name) + "</span>" + tag + "</span></td>" +
            '<td class="val-strong" data-label="Employer cost">' + approx + costCell + "</td>" +
            '<td data-label="Gross">' + money(r.gross) + "</td>" +
            '<td class="val-net" data-label="Net take-home">' + money(r.net) + "</td>" +
            '<td data-label="You keep">' + (r.netRatio != null ? Math.round(r.netRatio * 100) + "%" : "—") + "</td>" +
            '<td class="cost-per-net" data-label="Cost per ' + (state.displayCurrency === "USD" ? "$" : "€") + '1 net">' +
              (r.costPerNet != null ? (state.displayCurrency === "USD" ? "$" : "€") + r.costPerNet.toFixed(2) : "—") + "</td>" +
            '<td class="living-col" data-label="Cost of living">' + money(r.costOfLiving) + "</td>" +
            '<td class="living-col ' + surplusCls + '" data-label="After living costs">' +
              (hasSurplus ? (r.surplus >= 0 ? "+" : "−") + money(Math.abs(r.surplus)) : "—") + "</td>" +
          "</tr>"
        );
      }).join("");
    }

    renderRangeNotice();
    syncSortIndicators();
    writeURL();
  }

  // Largest value of the current generated axis (annual).
  function generatedRangeMax() {
    var m = 0;
    DATA.countries.forEach(function (c) {
      pointsInEur(c).forEach(function (p) {
        if (p[state.mode] != null && p[state.mode] > m) m = p[state.mode];
      });
    });
    return m;
  }

  function renderRangeNotice() {
    var el = document.getElementById("rangeNotice");
    var max = generatedRangeMax();
    if (max && state.amount > max) {
      var per0 = state.monthly ? " / month" : " / year";
      el.innerHTML = '<div class="card">Calculations cover values up to <b>' +
        money(max) + "</b>" + per0 + ", so there's no data at <b>" +
        money(state.amount) + "</b>.</div>";
      return;
    }
    el.innerHTML = "";
  }

  function syncSortIndicators() {
    document.querySelectorAll("thead th").forEach(function (th) {
      th.classList.remove("sorted-asc", "sorted-desc");
      if (th.dataset.sort) th.setAttribute("aria-sort", "none");
      if (th.dataset.sort === state.sortKey) {
        th.classList.add(state.sortDir === -1 ? "sorted-desc" : "sorted-asc");
        th.setAttribute("aria-sort", state.sortDir === -1 ? "descending" : "ascending");
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
  var currencyButtons = document.querySelectorAll(".currency-option");
  var currencySymbol = document.getElementById("currencySymbol");
  var fxInput = document.getElementById("eurUsdRate");
  var fxStatus = document.getElementById("fxStatus");
  var latestFxButton = document.getElementById("useLatestFx");
  var costPerNetHeader = document.getElementById("costPerNetHeader");
  var chips = document.getElementById("presets");

  function formatDate(date) {
    if (!date) return "";
    var parsed = new Date(date + "T00:00:00Z");
    return isNaN(parsed.getTime()) ? date : parsed.toLocaleDateString(undefined, {
      year: "numeric", month: "short", day: "numeric", timeZone: "UTC",
    });
  }

  function renderFxStatus() {
    fxInput.value = state.eurUsd.toFixed(4);
    fxStatus.removeAttribute("data-state");
    if (state.fxSource === "manual") fxStatus.textContent = "Manual override";
    else if (state.fxSource === "ecb") fxStatus.textContent = "ECB · " + formatDate(state.fxDate);
    else if (state.fxSource === "cached") fxStatus.textContent = "Cached ECB rate" + (state.fxDate ? " · " + formatDate(state.fxDate) : "");
    else fxStatus.textContent = "Bundled fallback";
  }

  function showFxFeedback(message, stateName) {
    fxStatus.textContent = message;
    fxStatus.setAttribute("data-state", stateName);
  }

  function renderPresets() {
    chips.innerHTML = PRESETS.map(function (v) {
      return '<button class="chip" data-v="' + v + '">' +
        formatters[state.displayCurrency].format(v) + "</button>";
    }).join("");
  }

  function applyCurrencyUI() {
    currencyButtons.forEach(function (button) {
      var selected = button.dataset.currency === state.displayCurrency;
      button.setAttribute("aria-checked", selected ? "true" : "false");
      button.tabIndex = selected ? 0 : -1;
    });
    currencySymbol.textContent = state.displayCurrency === "USD" ? "$" : "€";
    amountInput.value = plainNum(toDisplayCurrency(state.amount));
    var symbol = state.displayCurrency === "USD" ? "$" : "€";
    costPerNetHeader.innerHTML = "Cost per<br>" + symbol + "1 net";
    costPerNetHeader.title = "Total the employer pays for every " + symbol + "1 the employee takes home";
    renderPresets();
    renderFxStatus();
  }

  function setDisplayCurrency(currency) {
    state.displayCurrency = currency === "USD" ? "USD" : "EUR";
    applyCurrencyUI();
    render();
  }

  function storeFx(key, rate, date, fetchedAt) {
    try {
      localStorage.setItem(key, JSON.stringify({
        rate: rate,
        date: date || null,
        fetchedAt: fetchedAt || null,
      }));
    } catch (error) {}
  }

  function setFx(rate, source, date, preserveDisplayedAmount) {
    if (!(rate > 0)) return;
    var displayedAmount = toDisplayCurrency(state.amount);
    state.eurUsd = rate;
    if (preserveDisplayedAmount && state.displayCurrency === "USD") {
      state.amount = displayedAmount / rate;
    }
    state.fxSource = source;
    state.fxDate = date || null;
    if (source === "manual") storeFx(FX_OVERRIDE_KEY, rate, null, null);
    if (source === "ecb") storeFx(FX_CACHE_KEY, rate, date, Date.now());
    applyCurrencyUI();
    render();
  }

  function parseEcbCsv(csv) {
    var lines = csv.trim().split(/\r?\n/);
    if (lines.length < 2) throw new Error("ECB response did not contain an observation");
    var headers = lines[0].split(",");
    var values = lines[lines.length - 1].split(",");
    var date = values[headers.indexOf("TIME_PERIOD")];
    var rate = parseFloat(values[headers.indexOf("OBS_VALUE")]);
    if (!(rate > 0) || !date) throw new Error("ECB response was incomplete");
    return {rate: rate, date: date};
  }

  function fetchLatestFx(preserveDisplayedAmount, userInitiated) {
    latestFxButton.disabled = true;
    latestFxButton.textContent = "Checking…";
    showFxFeedback("Contacting ECB…", "loading");
    return fetch(ECB_FX_URL, {headers: {Accept: "text/csv"}})
      .then(function (response) {
        if (!response.ok) throw new Error("ECB request failed: " + response.status);
        return response.text();
      })
      .then(function (csv) {
        var latest = parseEcbCsv(csv);
        try { localStorage.removeItem(FX_OVERRIDE_KEY); } catch (error) {}
        setFx(latest.rate, "ecb", latest.date, preserveDisplayedAmount);
        if (userInitiated) {
          showFxFeedback("Updated from ECB · " + formatDate(latest.date), "success");
        }
      })
      .catch(function () {
        showFxFeedback("ECB refresh failed · keeping current rate", "error");
      })
      .then(function () {
        latestFxButton.disabled = false;
        latestFxButton.textContent = "Use latest ECB rate";
      });
  }

  function cachedFxIsFresh() {
    return cachedFx && Number(cachedFx.fetchedAt) > 0 &&
      Date.now() - Number(cachedFx.fetchedAt) < FX_REFRESH_MS;
  }

  function setMode(mode) {
    state.mode = mode;
    document.querySelectorAll(".seg").forEach(function (b) {
      var selected = b.dataset.mode === mode;
      b.setAttribute("aria-checked", selected ? "true" : "false");
      b.tabIndex = selected ? 0 : -1;
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

  function wireRadioKeys(selector, dataKey, activate) {
    document.querySelectorAll(selector).forEach(function (button) {
      button.addEventListener("keydown", function (e) {
        var keys = ["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown", "Home", "End"];
        if (keys.indexOf(e.key) === -1) return;
        e.preventDefault();
        var buttons = Array.from(document.querySelectorAll(selector)).filter(function (b) {
          return !b.disabled;
        });
        var index = buttons.indexOf(button);
        if (e.key === "Home") index = 0;
        else if (e.key === "End") index = buttons.length - 1;
        else {
          var delta = (e.key === "ArrowRight" || e.key === "ArrowDown") ? 1 : -1;
          index = (index + delta + buttons.length) % buttons.length;
        }
        var next = buttons[index];
        activate(next.dataset[dataKey]);
        next.focus();
      });
    });
  }
  wireRadioKeys(".seg", "mode", setMode);
  wireRadioKeys(".currency-option", "currency", setDisplayCurrency);

  amountInput.addEventListener("input", function () {
    state.amount = fromDisplayCurrency(parseAmount(amountInput.value));
    render();
  });
  amountInput.addEventListener("blur", function () {
    if (state.amount > 0) amountInput.value = plainNum(toDisplayCurrency(state.amount));
  });

  currencyButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      setDisplayCurrency(button.dataset.currency);
    });
  });
  fxInput.addEventListener("change", function () {
    var rate = parseFloat(fxInput.value);
    if (rate > 0) setFx(rate, "manual", null, true);
    else renderFxStatus();
  });
  latestFxButton.addEventListener("click", function () { fetchLatestFx(true, true); });

  document.getElementById("euOnly").addEventListener("change", function (e) {
    state.euOnly = e.target.checked; render();
  });
  document.getElementById("euroOnly").addEventListener("change", function (e) {
    state.euroOnly = e.target.checked; render();
  });
  document.getElementById("showMonthly").addEventListener("change", function (e) {
    state.monthly = e.target.checked; render();
  });
  document.getElementById("showLivingCosts").addEventListener("change", function (e) {
    state.showLivingCosts = e.target.checked;
    if (!state.showLivingCosts && (state.sortKey === "costOfLiving" || state.sortKey === "surplus")) {
      state.sortKey = state.mode === "net" ? "cost" : "net";
      state.sortDir = state.mode === "net" ? 1 : -1;
    }
    render();
  });
  document.getElementById("search").addEventListener("input", function (e) {
    state.search = e.target.value; render();
  });

  function sortByHeader(th) {
      var key = th.dataset.sort;
      if (!key) return;
      if (state.sortKey === key) { state.sortDir *= -1; }
      else { state.sortKey = key; state.sortDir = key === "name" ? 1 : -1; }
      render();
  }
  document.querySelectorAll("thead th[data-sort]").forEach(function (th) {
    th.tabIndex = 0;
    th.addEventListener("click", function () { sortByHeader(th); });
    th.addEventListener("keydown", function (e) {
      if (e.key !== "Enter" && e.key !== " ") return;
      e.preventDefault();
      sortByHeader(th);
    });
  });

  // presets use round numbers in the selected display currency.
  chips.addEventListener("click", function (e) {
    var b = e.target.closest(".chip");
    if (!b) return;
    var displayAmount = parseFloat(b.dataset.v);
    state.amount = fromDisplayCurrency(displayAmount);
    amountInput.value = plainNum(displayAmount);
    render();
  });

  // init — reflect hydrated state into the DOM, then render
  document.getElementById("euOnly").checked = state.euOnly;
  document.getElementById("euroOnly").checked = state.euroOnly;
  document.getElementById("showMonthly").checked = state.monthly;
  document.getElementById("showLivingCosts").checked = state.showLivingCosts;
  applyCurrencyUI();
  setMode(state.mode);
  if (state.fxSource !== "manual" && !cachedFxIsFresh()) fetchLatestFx(false, false);
})();
