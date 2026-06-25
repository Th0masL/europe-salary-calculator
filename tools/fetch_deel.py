#!/usr/bin/env python3
"""
Fetch BOTH net pay and employer cost from Deel's two public calculators and
write data/deel.json + data/deel.js.

Deel exposes two complementary tools, and we take the strength of each:

  NET  <- take-home calculator
    POST https://api-prod.letsdeel.com/guest/take_home_calculator/calculate
    body: {country:<ISO2>, salary:<annual>, currency:"EUR", period:"annual"}
    -> netAnnualSalaryExchanged   (net, in the requested currency = EUR)

  COST <- employee-cost calculator
    POST https://api-prod.letsdeel.com/employment_cost
    body: {country:<NAME>, salary:<monthly>, currency:"EUR"}
    -> (totalCosts - managementFee) * 12

Two gotchas handled here:
  * employment_cost expects a MONTHLY salary and the full country NAME (not ISO2).
  * Deel's `totalCosts` bakes in Deel's own EOR management fee (a flat ~EUR 522/mo);
    we subtract it so `cost` is the mandatory employer cost, comparable to the
    other sources. (We do NOT use employment_cost's own net field — it's
    inconsistent with the dedicated take-home calculator.)

Usage:
    python3 tools/fetch_deel.py
"""
import datetime
import json
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GUEST = "https://api-prod.letsdeel.com/guest/take_home_calculator"
EMPCOST = "https://api-prod.letsdeel.com/employment_cost"
UA = "Mozilla/5.0 (salary-calculator data fetch)"
SALARY_POINTS = list(range(20000, 150001, 10000))  # 20k..150k EUR, 10k step (14 points)

EU_NAMES = [
    "Albania", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus",
    "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany",
    "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania",
    "Luxembourg", "Malta", "Moldova", "Montenegro", "Netherlands", "Norway",
    "Poland", "Portugal", "Romania", "Serbia", "Slovakia", "Slovenia",
    "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom",
]
# take-home /data label overrides (used to look up ISO2)
LABEL_OVERRIDES = {"Turkey": "Türkiye", "Czech Republic": "Czechia",
                   "Moldova": "Moldova, Republic of"}
# country NAME the employment_cost endpoint expects (defaults to our name)
COST_NAME_OVERRIDES = {"Moldova": "Moldova, Republic of"}

# US locations — Deel does real per-state tax (no flat-rate fallback), so these
# replace the blog single-benchmark estimates. (label, take-home state code,
# employment_cost state name). Labels match the eBook US cities so the app's
# flag / cost-of-living metadata backfills by name.
US_LOCATIONS = [
    ("Seattle, WA", "WA", "Washington"),
    ("San Francisco, CA", "CA", "California"),
    ("New York, NY", "NY", "New York"),
    ("Austin, TX", "TX", "Texas"),
    ("Atlanta, GA", "GA", "Georgia"),
    ("Miami, FL", "FL", "Florida"),
]


def http_json(url, payload):
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, method="POST",
                                 headers={"User-Agent": UA, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def get_net(iso2, annual, state=None):
    body = {"country": iso2, "salary": annual, "currency": "EUR", "period": "annual"}
    if state:
        body["state"] = state
    res = http_json(f"{GUEST}/calculate", body)
    if res.get("errors") or "netAnnualSalary" not in res:
        return None
    return round(float(res.get("netAnnualSalaryExchanged") or res["netAnnualSalary"]))


def get_cost(name, annual, state=None):
    body = {"country": name, "salary": annual / 12, "currency": "EUR"}
    if state:
        body["state"] = state
    res = http_json(EMPCOST, body)
    if "totalCosts" not in res:
        return None
    fee = float(res.get("totalCostsData", {}).get("managementFee") or 0)
    return round((float(res["totalCosts"]) - fee) * 12)


def build_points(net_call, cost_call, label):
    """Query both endpoints across SALARY_POINTS; return [{gross, cost?, net?}]."""
    points = []
    for salary in SALARY_POINTS:
        net = cost = None
        try:
            net = net_call(salary)
        except Exception as e:  # noqa: BLE001
            print(f"  ! {label} net {salary}: {e}", file=sys.stderr)
        try:
            cost = cost_call(salary)
        except Exception as e:  # noqa: BLE001
            print(f"  ! {label} cost {salary}: {e}", file=sys.stderr)
        p = {"gross": salary}
        if cost:
            p["cost"] = cost
        if net:
            p["net"] = net
        if len(p) > 1:
            points.append(p)
        time.sleep(0.2)
    return points


def main():
    # fetch the take-home country list (label -> ISO2)
    req = urllib.request.Request(f"{GUEST}/data", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        clist = json.load(r)
    by_label = {c["label"]: c for c in clist}

    out = []
    for name in EU_NAMES:
        entry = by_label.get(LABEL_OVERRIDES.get(name, name)) or by_label.get(name)
        if not entry:
            print(f"  ! {name}: not in Deel list, skipping", file=sys.stderr)
            continue
        iso2 = entry["value"]
        cost_name = COST_NAME_OVERRIDES.get(name, name)
        points = build_points(lambda s, i=iso2: get_net(i, s),
                              lambda s, n=cost_name: get_cost(n, s), name)
        if len(points) < 2:
            print(f"  ! {name}: too few points, skipping", file=sys.stderr)
            continue
        out.append({"name": name, "points": points})
        c60 = next((p.get("cost") for p in points if p["gross"] == 60000), None)
        n60 = next((p.get("net") for p in points if p["gross"] == 60000), None)
        print(f"  {name}: {len(points)} pts (cost@60k {c60}, net@60k {n60})")

    # US states (real per-state Deel calculation)
    for label, st_code, st_name in US_LOCATIONS:
        points = build_points(lambda s, c=st_code: get_net("US", s, c),
                              lambda s, n=st_name: get_cost("United States", s, n), label)
        if len(points) < 2:
            print(f"  ! {label}: too few points, skipping", file=sys.stderr)
            continue
        out.append({"name": label, "us": True, "points": points})
        c60 = next((p.get("cost") for p in points if p["gross"] == 60000), None)
        n60 = next((p.get("net") for p in points if p["gross"] == 60000), None)
        print(f"  {label}: {len(points)} pts (cost@60k {c60}, net@60k {n60})")

    doc = {
        "meta": {
            "title": "Employer cost + net pay (Deel calculators)",
            "source": "Deel employee-cost + take-home calculators",
            "endpoints": {"net": f"{GUEST}/calculate", "cost": EMPCOST},
            "currency": "EUR",
            "fetched": datetime.date.today().isoformat(),
            "provides": ["gross", "cost", "net"],
            "salaryPoints": SALARY_POINTS,
            "note": ("Cost from the employee-cost calculator (Deel's EOR management fee "
                     "removed); net from the dedicated take-home calculator. Includes 5 US "
                     "states with real per-state tax (Deel handles no-income-tax states "
                     "correctly). Single filer; estimates for comparison only."),
        },
        "countries": out,
    }
    (ROOT / "data").mkdir(exist_ok=True)
    with open(ROOT / "data" / "deel.json", "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    with open(ROOT / "data" / "deel.js", "w", encoding="utf-8") as f:
        f.write("// AUTO-GENERATED from data/deel.json by tools/fetch_deel.py - do not edit.\n")
        f.write("window.SALARY_DATA_DEEL = " + json.dumps(doc, ensure_ascii=False) + ";\n")
    print(f"\nWrote data/deel.json + data/deel.js with {len(out)} countries.")


if __name__ == "__main__":
    main()
