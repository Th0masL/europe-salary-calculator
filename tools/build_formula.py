#!/usr/bin/env python3
"""
Build the "formula" dataset from the per-country calculators in tools/calc/ and
write data/formula.json + data/formula.js.

Each tools/calc/<country>.py module is a self-contained calculation from that
country's published tax rates (no third-party API). This dataset is an
independent ground truth: use it to validate the API sources
(tools/compare_sources.py) or, where it's solid, to replace them in the consensus.

Add a country by dropping a new file in tools/calc/ — it's picked up automatically.

Usage:
    python3 tools/build_formula.py
"""
import datetime
import importlib
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CALC_DIR = ROOT / "tools" / "calc"
FX_URL = "https://open.er-api.com/v6/latest/EUR"
SALARY_POINTS = [30000, 60000, 100000, 150000]  # annual EUR


def load_country_modules():
    sys.path.insert(0, str(CALC_DIR))
    mods = []
    for f in sorted(CALC_DIR.glob("*.py")):
        if f.stem in ("engine", "__init__"):
            continue
        mods.append(importlib.import_module(f.stem))
    return mods


def fx_rates():
    with urllib.request.urlopen(FX_URL, timeout=30) as r:
        return json.load(r)  # full response: "rates" (EUR -> currency) + update times


def fx_as_of(fx):
    """Clean date the FX rates were last published, e.g. '2026-06-24'."""
    raw = fx.get("time_last_update_utc")
    if not raw:
        return None
    try:
        return datetime.datetime.strptime(raw, "%a, %d %b %Y %H:%M:%S %z").date().isoformat()
    except ValueError:
        return None


def main():
    mods = load_country_modules()
    need_fx = any(getattr(m, "CURRENCY", "EUR") != "EUR" for m in mods)
    fx = fx_rates() if need_fx else None
    rates = fx["rates"] if fx else {}

    countries = []
    for m in mods:
        cur = getattr(m, "CURRENCY", "EUR")
        # work in the local currency (so caps/brackets are right), then to EUR
        rate = 1.0 if cur == "EUR" else rates[cur]  # EUR -> local
        points = []
        for gross_eur in SALARY_POINTS:
            cost_loc, net_loc = m.compute(gross_eur * rate)
            points.append({"gross": gross_eur,
                           "cost": round(cost_loc / rate),
                           "net": round(net_loc / rate)})
        entry = {"name": m.NAME, "year": getattr(m, "YEAR", None), "points": points}
        breakdown = getattr(m, "EMPLOYER_BREAKDOWN", None)
        if breakdown:
            entry["costNote"] = breakdown
        countries.append(entry)
        p60 = next(p for p in points if p["gross"] == 60000)
        print(f"  {m.NAME} ({cur}, {getattr(m, 'YEAR', '?')}): "
              f"cost@60k EUR {p60['cost']}, net@60k EUR {p60['net']}")

    # The US cities (tools/calc_us.py -> data/us.json) are also a from-published-rates
    # calc, so they belong in this dataset too. They share one employer-cost shape.
    us_cost_note = ("Employer FICA 7.65% (6.2% Social Security capped, 1.45% Medicare) + "
                    "FUTA (federal unemployment) + SUTA (state unemployment)")
    us_path = ROOT / "data" / "us.json"
    if us_path.exists():
        us_cities = json.loads(us_path.read_text(encoding="utf-8"))["countries"]
        for c in us_cities:
            entry = {k: c[k] for k in ("name", "us", "flag", "costOfLiving", "points") if k in c}
            entry["costNote"] = us_cost_note
            countries.append(entry)
        print(f"  + {len(us_cities)} US cities from calc_us.py")

    doc = {
        "meta": {
            "title": "Formula salary calc (per-country, no vendor)",
            "source": "Computed from each country's published tax rates (tools/calc/*.py)",
            "currency": "EUR",
            "fetched": datetime.date.today().isoformat(),
            "fxAsOf": fx_as_of(fx) if fx else None,
            "provides": ["gross", "cost", "net"],
            "salaryPoints": SALARY_POINTS,
            "note": ("Independent ground truth from published rates. Single filer, no "
                     "personal deductions beyond the mandatory ones. Estimates for comparison."),
        },
        "countries": countries,
    }
    (ROOT / "data").mkdir(exist_ok=True)
    with open(ROOT / "data" / "formula.json", "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    with open(ROOT / "data" / "formula.js", "w", encoding="utf-8") as f:
        f.write("// AUTO-GENERATED from data/formula.json by tools/build_formula.py - do not edit.\n")
        f.write("window.SALARY_DATA_FORMULA = " + json.dumps(doc, ensure_ascii=False) + ";\n")
    print(f"\nWrote data/formula.json + .js with {len(countries)} country(ies).")


if __name__ == "__main__":
    main()
