#!/usr/bin/env python3
"""
Fetch an alternative dataset from the live Skuad cost-calculator API (the engine
behind boundlesshq.com/cost-calculator) and write data/skuad.json + data/skuad.js.

Usage:
    python3 tools/fetch_skuad.py

This is a stored *snapshot* of a live, third-party API that may change or vanish,
so we fetch once and commit the result. Re-run to refresh.

What it does
------------
- European countries: query the API at several gross salaries (in EUR) and build
  {gross, cost, net} points. This is a genuine per-country calculation from published rates.
- US cities: the API's US *employee* income tax is unreliable (it falls back to a
  flat ~10% "state tax" for states it hasn't configured — wrong for no-income-tax
  states like WA and TX). So we DO NOT use the API for the US; we reuse the
  trustworthy blog-based US figures already in data/ebook.json instead.
- Cost of living: the API doesn't provide it, so we reuse the eBook's figures.

Endpoint:
  GET https://cost-calculator.skuad.io/cost-calculator/cost
      ?client=website&countryCode=XXX&currencyCode=EUR&salary=NNNN
"""
import datetime
import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://cost-calculator.skuad.io/cost-calculator/cost"
UA = "Mozilla/5.0 (salary-calculator data fetch)"

# Gross salary points (EUR) to sample per country. More points than the eBook's
# three benchmarks => smoother interpolation.
SALARY_POINTS = list(range(20000, 150001, 10000))  # 20k..150k EUR, 10k step (14 points)

# Our 36 European country names -> Skuad 3-letter country codes.
# Slovenia is intentionally absent: the API does not list it.
COUNTRY_CODES = {
    "Albania": "ALB", "Austria": "AUT", "Belgium": "BEL", "Bulgaria": "BGR",
    "Croatia": "HRV", "Cyprus": "CYP", "Czech Republic": "CZE", "Denmark": "DNK",
    "Estonia": "EST", "Finland": "FIN", "France": "FRA", "Germany": "DEU",
    "Greece": "GRC", "Hungary": "HUN", "Ireland": "IRL", "Italy": "ITA",
    "Latvia": "LVA", "Lithuania": "LTU", "Luxembourg": "LUX", "Malta": "MLT",
    "Moldova": "MDA", "Montenegro": "MNE", "Netherlands": "NLD", "Norway": "NOR",
    "Poland": "POL", "Portugal": "PRT", "Romania": "ROU", "Serbia": "SRB",
    "Slovakia": "SVK", "Spain": "ESP", "Sweden": "SWE", "Switzerland": "CHE",
    "Turkey": "TUR", "Ukraine": "UKR", "United Kingdom": "GBR",
}


def fetch_point(code, salary):
    """Return (cost, net) in EUR for one country/salary, or None on failure."""
    url = (f"{API}?client=website&countryCode={code}"
           f"&currencyCode=EUR&salary={salary}")
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.load(r)
    if not body.get("success"):
        return None
    y = body["data"]["yearly"]
    return round(y["totalEmploymentCost"]), round(y["totalEmployeeSalary"])


def main():
    ebook_path = ROOT / "data" / "ebook.json"
    if not ebook_path.exists():
        sys.exit("data/ebook.json not found — run tools/extract_data.py first.")
    ebook = json.loads(ebook_path.read_text(encoding="utf-8"))
    # index eBook entries by name for flags / EU flag / cost of living / US reuse
    by_name = {c["name"]: c for c in ebook["countries"]}

    countries = []
    for name, code in COUNTRY_CODES.items():
        base = by_name[name]
        points = []
        for salary in SALARY_POINTS:
            try:
                res = fetch_point(code, salary)
            except Exception as e:  # noqa: BLE001 - keep going, log it
                print(f"  ! {name} {salary}: {e}", file=sys.stderr)
                res = None
            if res:
                cost, net = res
                points.append({"gross": salary, "cost": cost, "net": net})
            time.sleep(0.2)  # be polite to the API
        # keep only strictly-increasing points (guards against odd API responses)
        clean = []
        for p in points:
            if not clean or (p["cost"] > clean[-1]["cost"] and p["net"] > clean[-1]["net"]):
                clean.append(p)
        if len(clean) < 2:
            print(f"  ! {name}: only {len(clean)} usable points, skipping", file=sys.stderr)
            continue
        countries.append({
            "name": name, "flag": base["flag"], "eu": base["eu"],
            "devSalary": base["devSalary"], "costOfLiving": base["costOfLiving"],
            "points": clean,
        })
        print(f"  {name}: {len(clean)} points")

    # US cities: reuse the reliable blog figures from the eBook dataset as-is.
    us = [dict(c) for c in ebook["countries"] if c.get("us")]
    for c in us:
        c["note"] = "blog-based (API US income tax unreliable)"
    countries += us
    print(f"  + {len(us)} US cities reused from blog data")

    doc = {
        "meta": {
            "title": "Employment costs & net pay (Skuad live calculator)",
            "source": "Skuad cost-calculator API (engine behind boundlesshq.com/cost-calculator)",
            "endpoint": API,
            "currency": "EUR",
            "fetched": datetime.date.today().isoformat(),
            "salaryPoints": SALARY_POINTS,
            "note": ("European countries fetched live from the Skuad API at several gross-salary "
                     "points (genuine per-country calculation; may differ from the eBook study). "
                     "Slovenia is unavailable in the API. US cities reuse the blog figures because "
                     "the API's US state income tax is unreliable. Cost of living reuses the eBook. "
                     "Figures are estimates for comparison only."),
        },
        "countries": countries,
    }

    (ROOT / "data").mkdir(exist_ok=True)
    with open(ROOT / "data" / "skuad.json", "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    with open(ROOT / "data" / "skuad.js", "w", encoding="utf-8") as f:
        f.write("// AUTO-GENERATED from data/skuad.json by tools/fetch_skuad.py - do not edit by hand.\n")
        f.write("window.SALARY_DATA_SKUAD = " + json.dumps(doc, ensure_ascii=False) + ";\n")
    print(f"\nWrote data/skuad.json and data/skuad.js with {len(countries)} entries "
          f"({len(countries) - len(us)} European + {len(us)} US).")


if __name__ == "__main__":
    main()
