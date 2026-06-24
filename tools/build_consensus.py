#!/usr/bin/env python3
"""
Build a consensus dataset by combining the aligned sources, and write
data/consensus.json + data/consensus.js.

For every location and a fixed set of gross-salary points we interpolate each
source, drop any value that sits >10% from the median of the others (an
outlier), and take the median of what's left — separately for cost and net.
Metadata (flag, EU/US, cost of living, dev salary) comes from the eBook entry.

Sources: ebook, skuad, deel for European rows; US cities use our own 'us' direct
calc, and rippling contributes employer cost only. Run the per-source fetchers first.

Usage:
    python3 tools/build_consensus.py
"""
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# 'us' = direct calc from published rates (US only); 'rippling' = employer cost only (no net)
SOURCES = ["ebook", "skuad", "deel", "us", "rippling"]
GROSS_POINTS = [30000, 45000, 60000, 80000, 100000, 125000, 150000]
OUTLIER_PCT = 0.10  # a source >10% from the median of the others is dropped


def load(src):
    p = ROOT / "data" / f"{src}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def interp(points, key, gross):
    pts = sorted((p for p in points if key in p), key=lambda p: p["gross"])
    if len(pts) < 2:
        return None
    if gross <= pts[0]["gross"]:
        a, b = pts[0], pts[1]
    elif gross >= pts[-1]["gross"]:
        a, b = pts[-2], pts[-1]
    else:
        a, b = next((pts[i], pts[i + 1]) for i in range(len(pts) - 1)
                    if pts[i]["gross"] <= gross <= pts[i + 1]["gross"])
    span = b["gross"] - a["gross"]
    t = 0 if span == 0 else (gross - a["gross"]) / span
    return a[key] + (b[key] - a[key]) * t


def median(xs):
    xs = sorted(xs)
    n = len(xs)
    return xs[n // 2] if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2


def consensus_value(values):
    """values: list of numbers. Drop outliers vs median-of-others, return median."""
    vals = [v for v in values if v is not None]
    if not vals:
        return None, []
    # Dedupe near-identical values: some sources aren't independent (e.g. the US
    # blog estimate appears verbatim in both eBook and Skuad), and counting it
    # twice would let it outvote a real source like Deel's per-state figures.
    uniq = []
    for v in vals:
        if not any(abs(v - u) <= 1 for u in uniq):
            uniq.append(v)
    vals = uniq
    if len(vals) >= 3:
        kept = []
        for i, v in enumerate(vals):
            others = vals[:i] + vals[i + 1:]
            med = median(others)
            if not med or abs(v - med) / med <= OUTLIER_PCT:
                kept.append(v)
        vals = kept or vals
    return round(median(vals)), vals


def main():
    docs = {s: load(s) for s in SOURCES if load(s)}
    idx = {s: {c["name"]: c["points"] for c in docs[s]["countries"]} for s in docs}
    ebook = docs["ebook"]

    # Metadata (flag, cost of living, …) per name: prefer eBook, then the direct
    # US calc, then Deel. The 'us' source carries metadata for US-only cities like
    # Miami that the eBook doesn't have.
    meta_by_name = {}
    for s in ("ebook", "us", "deel", "skuad"):
        for c in docs.get(s, {"countries": []})["countries"]:
            meta_by_name.setdefault(c["name"], c)

    # Iterate every location: eBook order first, then any extras (e.g. Miami).
    names = [c["name"] for c in ebook["countries"]]
    seen = set(names)
    for s in ("us", "deel", "skuad"):
        for c in docs.get(s, {"countries": []})["countries"]:
            if c["name"] not in seen:
                names.append(c["name"])
                seen.add(c["name"])

    out = []
    for name in names:
        base = meta_by_name[name]
        # US is state-level. We use our own direct calc from published rates ('us' source —
        # non-EOR, validated against Deel to <1% and more complete for NYC). Fall
        # back to Deel, then to the rest. European countries use all sources; the
        # US-only 'us' source never appears for them.
        is_us = bool(base.get("us"))
        if is_us and name in idx.get("us", {}):
            srcs = ["us"]
        elif is_us and name in idx.get("deel", {}):
            srcs = ["deel"]
        else:
            srcs = [s for s in idx if s != "us"]
        points = []
        for g in GROSS_POINTS:
            costs = [interp(idx[s][name], "cost", g) for s in srcs if name in idx[s]]
            nets = [interp(idx[s][name], "net", g) for s in srcs if name in idx[s]]
            cost, _ = consensus_value(costs)
            net, _ = consensus_value(nets)
            p = {"gross": g}
            if cost:
                p["cost"] = cost
            if net:
                p["net"] = net
            if "cost" in p or "net" in p:
                points.append(p)
        # how many sources contributed (at €60k) — for transparency
        n_sources = len([s for s in srcs if name in idx[s]])
        entry = {k: base[k] for k in ("name", "flag", "eu") if k in base}
        # note: 'approx' is intentionally NOT carried over — the consensus US comes
        # straight from Deel's real per-state data, not the flat blog estimate.
        for k in ("us", "devSalary", "costOfLiving"):
            if k in base:
                entry[k] = base[k]
        entry["sources"] = n_sources
        entry["points"] = points
        out.append(entry)

    doc = {
        "meta": {
            "title": "Consensus (median of aligned sources)",
            "source": "Consensus of Boundless eBook + Skuad + Deel",
            "currency": "EUR",
            "fetched": datetime.date.today().isoformat(),
            "combines": list(idx.keys()),
            "grossPoints": GROSS_POINTS,
            "note": ("Per location and salary, the median of the available sources "
                     "for cost and net, after dropping any value >10% from the median "
                     "of the others. Europe: eBook/Skuad/Deel; US cities: our own direct "
                     "calc; Rippling contributes employer cost only. "
                     "Estimates for comparison only."),
        },
        "countries": out,
    }
    (ROOT / "data").mkdir(exist_ok=True)
    with open(ROOT / "data" / "consensus.json", "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    with open(ROOT / "data" / "consensus.js", "w", encoding="utf-8") as f:
        f.write("// AUTO-GENERATED from data/consensus.json by tools/build_consensus.py - do not edit.\n")
        f.write("window.SALARY_DATA_CONSENSUS = " + json.dumps(doc, ensure_ascii=False) + ";\n")
    print(f"Wrote data/consensus.json + data/consensus.js with {len(out)} entries "
          f"(combining {', '.join(idx.keys())}).")


if __name__ == "__main__":
    main()
