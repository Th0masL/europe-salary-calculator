#!/usr/bin/env python3
"""
Fetch employer-cost data from Remote.com's public cost-calculator API and write
data/remote.json + data/remote.js.

Remote gives **gross salary and total employer cost** (employer contributions),
but NOT employee net pay. So each point here is {gross, cost} only.

Endpoints (reverse-engineered from the calculator's JS):
  GET  https://api.remote.com/api/v1/cost-calculator/countries
  POST https://api.remote.com/api/v1/cost-calculator/estimation
       body: {
         "employer_currency_slug": "<currency-uuid>",
         "employments": [{
           "annual_gross_salary_in_employer_currency": <int>,
           "region_slug": "<region-uuid>",
           "employment_term": "indefinite"
         }]
       }

Heads-up on data quality: Remote's figures look anomalous for some countries
(e.g. France carries a spurious ~EUR 106k fixed employer cost). Capture it, then
let tools/compare_sources.py flag the outliers.

Usage:
    python3 tools/fetch_remote.py
"""
import datetime
import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://api.remote.com/api/v1/cost-calculator"
UA = "Mozilla/5.0 (salary-calculator data fetch)"
SALARY_POINTS = [30000, 60000, 100000, 150000]

# Our 36 European country names. Remote's country labels mostly match; overrides
# handle the exceptions.
EU_NAMES = [
    "Albania", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus",
    "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany",
    "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania",
    "Luxembourg", "Malta", "Moldova", "Montenegro", "Netherlands", "Norway",
    "Poland", "Portugal", "Romania", "Serbia", "Slovakia", "Slovenia",
    "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom",
]
NAME_OVERRIDES = {"Czech Republic": "Czechia", "Turkey": "Türkiye",
                  "United Kingdom": "United Kingdom (UK)"}
# Montenegro is not offered by Remote, so it is skipped automatically.


def http_json(url, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    headers = {"User-Agent": UA}
    if data:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers,
                                 method="POST" if data else "GET")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def get_countries():
    return http_json(f"{BASE}/countries")["data"]


def find_eur_slug(countries):
    for c in countries:
        if c["currency"]["code"] == "EUR":
            return c["currency"]["slug"]
    raise SystemExit("No EUR currency slug found in Remote country list")


def estimate(eur_slug, region_slug, salary):
    body = {
        "employer_currency_slug": eur_slug,
        "employments": [{
            "annual_gross_salary_in_employer_currency": salary,
            "region_slug": region_slug,
            "employment_term": "indefinite",
        }],
    }
    res = http_json(f"{BASE}/estimation", body)
    if res.get("message"):
        return None
    costs = res["data"]["employments"][0]["employer_currency_costs"]
    return round(costs["annual_total"])


def main():
    countries = get_countries()
    eur_slug = find_eur_slug(countries)
    by_name = {c["name"]: c for c in countries}

    out = []
    for name in EU_NAMES:
        c = by_name.get(NAME_OVERRIDES.get(name, name)) or by_name.get(name)
        if not c:
            print(f"  ! {name}: not in Remote list, skipping", file=sys.stderr)
            continue
        points = []
        for salary in SALARY_POINTS:
            try:
                cost = estimate(eur_slug, c["region_slug"], salary)
            except Exception as e:  # noqa: BLE001
                print(f"  ! {name} {salary}: {e}", file=sys.stderr)
                cost = None
            if cost:
                points.append({"gross": salary, "cost": cost})
            time.sleep(0.25)
        if len(points) < 2:
            print(f"  ! {name}: too few points, skipping", file=sys.stderr)
            continue
        out.append({"name": name, "points": points})
        print(f"  {name}: {len(points)} points (cost@60k "
              f"EUR {next((p['cost'] for p in points if p['gross'] == 60000), '-')})")

    doc = {
        "meta": {
            "title": "Employer cost (Remote.com calculator)",
            "source": "Remote.com cost-calculator API",
            "endpoint": f"{BASE}/estimation",
            "currency": "EUR",
            "fetched": datetime.date.today().isoformat(),
            "provides": ["gross", "cost"],
            "salaryPoints": SALARY_POINTS,
            "note": ("Gross + total employer cost only (no net). Some countries look "
                     "anomalous (e.g. France has a spurious fixed employer cost). "
                     "Estimates for comparison only."),
        },
        "countries": out,
    }
    (ROOT / "data").mkdir(exist_ok=True)
    with open(ROOT / "data" / "remote.json", "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    with open(ROOT / "data" / "remote.js", "w", encoding="utf-8") as f:
        f.write("// AUTO-GENERATED from data/remote.json by tools/fetch_remote.py - do not edit.\n")
        f.write("window.SALARY_DATA_REMOTE = " + json.dumps(doc, ensure_ascii=False) + ";\n")
    print(f"\nWrote data/remote.json + data/remote.js with {len(out)} countries.")


if __name__ == "__main__":
    main()
