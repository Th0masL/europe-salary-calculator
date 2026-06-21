#!/usr/bin/env python3
"""
Fetch employer-cost data from Rippling's employee-cost calculator API and write
data/rippling.json + data/rippling.js.

Rippling gives **gross + total employer cost** (no net). Its figures look
accurate where they work — notably correct for Estonia (€80,604 = social tax 33%
+ unemployment 0.8%), where Skuad and Deel overstate. But its backend errors for
some countries (France, UK), which are skipped.

Endpoint (reverse-engineered from the calculator's JS; no PII required despite
the lead-gen form):
  POST https://app.rippling.com/api/global_expansion/api/get_employer_cost_breakdown/
  body: {"locale_country":"en-US",
         "role_data":{"country_code":"EE","currency":"EUR","state":"","yearly_salary":60000}}
  -> {total_cost:{yearly_value}, costs:[...], ...}

Usage:
    python3 tools/fetch_rippling.py
"""
import datetime
import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL = "https://app.rippling.com/api/global_expansion/api/get_employer_cost_breakdown/"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36"
SALARY_POINTS = [30000, 60000, 100000, 150000]  # annual EUR

# our 36 country names -> ISO2 codes
ISO2 = {
    "Albania": "AL", "Austria": "AT", "Belgium": "BE", "Bulgaria": "BG",
    "Croatia": "HR", "Cyprus": "CY", "Czech Republic": "CZ", "Denmark": "DK",
    "Estonia": "EE", "Finland": "FI", "France": "FR", "Germany": "DE",
    "Greece": "GR", "Hungary": "HU", "Ireland": "IE", "Italy": "IT",
    "Latvia": "LV", "Lithuania": "LT", "Luxembourg": "LU", "Malta": "MT",
    "Moldova": "MD", "Montenegro": "ME", "Netherlands": "NL", "Norway": "NO",
    "Poland": "PL", "Portugal": "PT", "Romania": "RO", "Serbia": "RS",
    "Slovakia": "SK", "Slovenia": "SI", "Spain": "ES", "Sweden": "SE",
    "Switzerland": "CH", "Turkey": "TR", "Ukraine": "UA", "United Kingdom": "GB",
}


def get_cost(code, salary):
    body = json.dumps({
        "locale_country": "en-US",
        "role_data": {"country_code": code, "currency": "EUR",
                      "state": "", "yearly_salary": salary},
    }).encode()
    req = urllib.request.Request(URL, data=body, method="POST",
                                 headers={"User-Agent": UA, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        res = json.load(r)
    if res.get("error") or "total_cost" not in res:
        return None
    return round(float(res["total_cost"]["yearly_value"]))


def main():
    out, skipped = [], []
    for name, code in ISO2.items():
        points = []
        for salary in SALARY_POINTS:
            try:
                cost = get_cost(code, salary)
            except Exception as e:  # noqa: BLE001
                print(f"  ! {name} {salary}: {e}", file=sys.stderr)
                cost = None
            if cost:
                points.append({"gross": salary, "cost": cost})
            time.sleep(0.3)
        if len(points) < 2:
            skipped.append(name)
            continue
        out.append({"name": name, "points": points})
        print(f"  {name}: cost@60k €"
              f"{next((p['cost'] for p in points if p['gross'] == 60000), '-')}")

    if skipped:
        print("  skipped (Rippling errored): " + ", ".join(skipped), file=sys.stderr)

    doc = {
        "meta": {
            "title": "Employer cost (Rippling calculator)",
            "source": "Rippling employee-cost calculator API",
            "endpoint": URL,
            "currency": "EUR",
            "fetched": datetime.date.today().isoformat(),
            "provides": ["gross", "cost"],
            "salaryPoints": SALARY_POINTS,
            "note": ("Gross + total employer cost only (no net). Accurate where available "
                     "(e.g. Estonia); Rippling's backend errors for some countries (France, "
                     "UK) which are omitted. Estimates for comparison only."),
        },
        "countries": out,
    }
    (ROOT / "data").mkdir(exist_ok=True)
    with open(ROOT / "data" / "rippling.json", "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    with open(ROOT / "data" / "rippling.js", "w", encoding="utf-8") as f:
        f.write("// AUTO-GENERATED from data/rippling.json by tools/fetch_rippling.py - do not edit.\n")
        f.write("window.SALARY_DATA_RIPPLING = " + json.dumps(doc, ensure_ascii=False) + ";\n")
    print(f"\nWrote data/rippling.json + .js with {len(out)} countries "
          f"({len(skipped)} skipped).")


if __name__ == "__main__":
    main()
