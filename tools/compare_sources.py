#!/usr/bin/env python3
"""
Compare every data source at a given gross salary and report where they agree
and where they disagree — the basis for building a "consensus" dataset.

Sources (whichever data/*.json exist):
  ebook   -> cost + net   (Boundless 2025 eBook)
  skuad   -> cost + net   (Skuad live calculator)
  remote  -> cost         (Remote.com)
  deel    -> net          (Deel)

For each country we interpolate each source at the target gross, then:
  * COST is compared across {ebook, skuad, remote}
  * NET  is compared across {ebook, skuad, deel}
We report the spread and flag sources that sit far from the median of the others
(an "outlier"), and emit a consensus (median of the non-outlier sources).

Usage:
    python3 tools/compare_sources.py [gross]      # default gross = 60000
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ["ebook", "skuad", "deel"]  # remote excluded (employer cost unreliable)
OUTLIER_PCT = 0.10  # >10% from the median of the others => flagged


def load():
    data = {}
    for s in SOURCES:
        p = ROOT / "data" / f"{s}.json"
        if p.exists():
            doc = json.loads(p.read_text(encoding="utf-8"))
            data[s] = {c["name"]: c["points"] for c in doc["countries"]}
    return data


def interp(points, key, gross):
    """Linear interpolation of `key` (cost|net) at `gross`; None if unavailable."""
    pts = [p for p in points if key in p]
    if len(pts) < 2:
        return None
    pts = sorted(pts, key=lambda p: p["gross"])
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


def analyse(values):
    """values: {source: number}. Return (consensus, spread_pct, outliers[])."""
    if len(values) < 2:
        only = next(iter(values.values())) if values else None
        return only, 0.0, []
    outliers = []
    for s, v in values.items():
        others = [x for k, x in values.items() if k != s]
        med = median(others)
        if med and abs(v - med) / med > OUTLIER_PCT:
            outliers.append(s)
    kept = {s: v for s, v in values.items() if s not in outliers} or values
    cons = median(list(kept.values()))
    lo, hi = min(values.values()), max(values.values())
    spread = (hi - lo) / med_or(cons) if cons else 0.0
    return cons, spread, outliers


def med_or(x):
    return x or 1


def fmt(v):
    return f"€{round(v):>7,}" if v is not None else "    —  "


def main():
    gross = int(sys.argv[1]) if len(sys.argv) > 1 else 60000
    data = load()
    print(f"Source comparison at gross = €{gross:,}   (outlier = >{int(OUTLIER_PCT*100)}% "
          f"from median of the others)\n")
    print(f"Loaded sources: {', '.join(data.keys())}\n")

    names = list(data.get("ebook", data[next(iter(data))]).keys())
    cost_srcs = [s for s in ["ebook", "skuad", "deel"] if s in data]
    net_srcs = [s for s in ["ebook", "skuad", "deel"] if s in data]

    hdr = f"{'Country':<16}" + "".join(f"{('cost:'+s):>12}" for s in cost_srcs) + \
        f"{'sprd':>6} {'outlier':>9}  |" + \
        "".join(f"{('net:'+s):>12}" for s in net_srcs) + f"{'sprd':>6} {'outlier':>9}"
    print(hdr)
    print("-" * len(hdr))

    consensus = []
    for name in names:
        cost_vals, net_vals = {}, {}
        for s in cost_srcs:
            if name in data[s]:
                v = interp(data[s][name], "cost", gross)
                if v:
                    cost_vals[s] = v
        for s in net_srcs:
            if name in data[s]:
                v = interp(data[s][name], "net", gross)
                if v:
                    net_vals[s] = v
        c_cons, c_spread, c_out = analyse(cost_vals)
        n_cons, n_spread, n_out = analyse(net_vals)

        row = f"{name:<16}"
        row += "".join(fmt(cost_vals.get(s)) for s in cost_srcs)
        row += f"{c_spread*100:>5.0f}% {','.join(c_out) or '-':>9}  |"
        row += "".join(fmt(net_vals.get(s)) for s in net_srcs)
        row += f"{n_spread*100:>5.0f}% {','.join(n_out) or '-':>9}"
        print(row)

        consensus.append({
            "name": name, "gross": gross,
            "cost": round(c_cons) if c_cons else None,
            "net": round(n_cons) if n_cons else None,
            "cost_sources": cost_vals and {k: round(v) for k, v in cost_vals.items()},
            "net_sources": net_vals and {k: round(v) for k, v in net_vals.items()},
            "cost_outliers": c_out, "net_outliers": n_out,
        })

    # summary: how often each source is the outlier
    print("\nOutlier tally (times a source was flagged):")
    for metric, srcs in [("cost", cost_srcs), ("net", net_srcs)]:
        tally = {s: 0 for s in srcs}
        for r in consensus:
            for s in r[f"{metric}_outliers"]:
                tally[s] += 1
        print(f"  {metric}: " + ", ".join(f"{s}={n}" for s, n in tally.items()))

    out = ROOT / "data" / f"comparison_{gross}.json"
    out.write_text(json.dumps({"gross": gross, "countries": consensus},
                              indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {out.relative_to(ROOT)} (per-source values + median, for inspection).")


if __name__ == "__main__":
    main()
