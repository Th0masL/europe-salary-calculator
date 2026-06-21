#!/usr/bin/env python3
"""
Extract per-country employment-cost data from the Boundless 2025 eBook PDF
and write data/ebook.json + data/ebook.js.

Usage:
    python3 tools/extract_data.py [path/to/ebook.pdf]

Requires `pdftotext` (poppler-utils) on PATH. The PDF itself is gitignored;
this script documents exactly how data/ebook.json was produced.

For each of the 36 countries the eBook shows a bar chart with four data points
(the local developer-average salary plus the €32k / €60k / €150k benchmarks)
for three metrics: total employment cost, net pay, and cost-to-net ratio.
The bars are drawn in ascending order, so we recover the gross<->cost<->net
mapping by sorting: the smallest gross has the smallest cost and smallest net.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PDF = ROOT / "boundless_ebook_employment_costs_2025.pdf"

COUNTRIES = [
    "Albania", "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus",
    "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany",
    "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania",
    "Luxembourg", "Malta", "Moldova", "Montenegro", "Netherlands", "Norway",
    "Poland", "Portugal", "Romania", "Serbia", "Slovakia", "Slovenia",
    "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom",
]

FLAGS = {
    "Albania": "\U0001F1E6\U0001F1F1", "Austria": "\U0001F1E6\U0001F1F9",
    "Belgium": "\U0001F1E7\U0001F1EA", "Bulgaria": "\U0001F1E7\U0001F1EC",
    "Croatia": "\U0001F1ED\U0001F1F7", "Cyprus": "\U0001F1E8\U0001F1FE",
    "Czech Republic": "\U0001F1E8\U0001F1FF", "Denmark": "\U0001F1E9\U0001F1F0",
    "Estonia": "\U0001F1EA\U0001F1EA", "Finland": "\U0001F1EB\U0001F1EE",
    "France": "\U0001F1EB\U0001F1F7", "Germany": "\U0001F1E9\U0001F1EA",
    "Greece": "\U0001F1EC\U0001F1F7", "Hungary": "\U0001F1ED\U0001F1FA",
    "Ireland": "\U0001F1EE\U0001F1EA", "Italy": "\U0001F1EE\U0001F1F9",
    "Latvia": "\U0001F1F1\U0001F1FB", "Lithuania": "\U0001F1F1\U0001F1F9",
    "Luxembourg": "\U0001F1F1\U0001F1FA", "Malta": "\U0001F1F2\U0001F1F9",
    "Moldova": "\U0001F1F2\U0001F1E9", "Montenegro": "\U0001F1F2\U0001F1EA",
    "Netherlands": "\U0001F1F3\U0001F1F1", "Norway": "\U0001F1F3\U0001F1F4",
    "Poland": "\U0001F1F5\U0001F1F1", "Portugal": "\U0001F1F5\U0001F1F9",
    "Romania": "\U0001F1F7\U0001F1F4", "Serbia": "\U0001F1F7\U0001F1F8",
    "Slovakia": "\U0001F1F8\U0001F1F0", "Slovenia": "\U0001F1F8\U0001F1EE",
    "Spain": "\U0001F1EA\U0001F1F8", "Sweden": "\U0001F1F8\U0001F1EA",
    "Switzerland": "\U0001F1E8\U0001F1ED", "Turkey": "\U0001F1F9\U0001F1F7",
    "Ukraine": "\U0001F1FA\U0001F1E6", "United Kingdom": "\U0001F1EC\U0001F1E7",
}

EU = {
    "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic",
    "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
    "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta",
    "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia",
    "Spain", "Sweden",
}

BENCHMARKS = [32000, 60000, 150000]

# US cities come from a separate Boundless 2025 study (US vs Europe), quoted in
# USD at a single benchmark: the local market rate for a mid-level software
# developer. Spot-checks show it shares the eBook's methodology (e.g. its Berlin
# and Paris figures match our Germany/France numbers), so we convert to EUR and
# add the cities to the same table. Figures (USD/yr) from:
# https://boundlesshq.com/blog/us-vs-europe-employment-costs-salaries-net-pay-compared-2025-study/
FX_USD_PER_EUR = 1.13  # 1 EUR = 1.13 USD (May 2025, the rate the study used)

US_CITIES = [
    # name,            gross,   cost,    net,     cost_of_living  (all USD/yr)
    ("Seattle, WA",     133707,  154338,  101262,  45790),
    ("San Francisco, CA", 119203, 143503,  82973,  57406),
    ("New York, NY",    110138,  128630,  79746,   67852),
    ("Austin, TX",      113650,  125470,  88339,   39773),
    ("Atlanta, GA",     114104,  125389,  83155,   37501),
]


def n(s):
    return int(s.replace(",", ""))


def usd_to_eur(usd):
    return round(usd / FX_USD_PER_EUR)


def build_us_cities():
    """US cities as single-benchmark, flat-rate estimates (USD converted to EUR).

    Only one real data point exists per city, so we anchor a straight line at the
    origin and the market-rate point. This means a constant effective rate at all
    salaries (no progressivity or Social Security caps) — a deliberate
    simplification, valid near the benchmark and flagged as approximate.
    """
    cities = []
    for name, gross, cost, net, col in US_CITIES:
        g, c, nt = usd_to_eur(gross), usd_to_eur(cost), usd_to_eur(net)
        cities.append({
            "name": name, "flag": "\U0001F1FA\U0001F1F8", "eu": False, "us": True,
            "approx": True, "devSalary": g, "costOfLiving": usd_to_eur(col),
            "points": [
                {"gross": 0, "cost": 0, "net": 0},
                {"gross": g, "cost": c, "net": nt},
            ],
        })
    return cities


def parse(text):
    lines = text.split("\n")
    marker = "Avg Yearly Gross Salary for Mid-Level"
    idxs = [i for i, l in enumerate(lines) if marker in l] + [len(lines)]

    parsed = {}
    for k in range(len(idxs) - 1):
        block = lines[idxs[k]:idxs[k + 1]]
        btext = "\n".join(block)
        dev = re.search(r"Software Developer:\s*€([\d,]+)", btext)
        col = re.search(r"Avg Yearly Cost of Living:\s*€([\d,]+)", btext)
        country = next((l.strip() for l in block if l.strip() in COUNTRIES), None)
        if not country:
            continue
        # Chart rows: a total-cost euro amount, a net euro amount, and a ratio,
        # all on one line. Euro amounts in the axis labels are suffixed with K,
        # so we exclude those. The four real rows come before the prose.
        rows = []
        for l in block:
            euros = re.findall(r"€([\d,]+)(?!K)", l)
            ratios = re.findall(r"(?<![\d.])(\d\.\d{2})(?![\d])", l)
            if len(euros) == 2 and len(ratios) == 1:
                rows.append((n(euros[0]), n(euros[1])))
        parsed[country] = {
            "dev": n(dev.group(1)) if dev else None,
            "col": n(col.group(1)) if col else None,
            "rows": rows[:4],
        }
    return parsed


def build(parsed):
    countries = []
    for country in COUNTRIES:
        d = parsed[country]
        grosses = sorted(BENCHMARKS + [d["dev"]])
        costs = sorted(r[0] for r in d["rows"])
        nets = sorted(r[1] for r in d["rows"])
        points = [{"gross": g, "cost": c, "net": net}
                  for g, c, net in zip(grosses, costs, nets)]
        # sanity checks
        assert len(points) == 4, f"{country}: expected 4 points"
        for i in range(1, 4):
            assert points[i]["cost"] > points[i - 1]["cost"], f"{country}: cost not monotonic"
            assert points[i]["net"] > points[i - 1]["net"], f"{country}: net not monotonic"
        countries.append({
            "name": country, "flag": FLAGS[country], "eu": country in EU,
            "devSalary": d["dev"], "costOfLiving": d["col"], "points": points,
        })
    return countries


def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PDF
    if not pdf.exists():
        sys.exit(f"PDF not found: {pdf}")
    text = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"],
        check=True, capture_output=True, encoding="utf-8",
    ).stdout

    countries = build(parse(text)) + build_us_cities()
    doc = {
        "meta": {
            "title": "Employment costs & net pay across Europe (2025)",
            "source": "Boundless - 'Understanding Employment Costs in Europe in 2025' (eBook)",
            "usSource": ("Boundless 'US vs Europe' 2025 study - "
                         "https://boundlesshq.com/blog/us-vs-europe-employment-costs-salaries-net-pay-compared-2025-study/"),
            "currency": "EUR",
            "fxUsdPerEur": FX_USD_PER_EUR,
            "year": 2025,
            "developerRole": "Mid-level Software Developer",
            "benchmarks": BENCHMARKS,
            "fields": {
                "gross": "Annual gross salary (EUR)",
                "cost": "Total employer cost = gross + mandatory employer contributions (EUR/yr)",
                "net": "Employee net take-home pay after taxes & employee contributions (EUR/yr)",
                "devSalary": "Average gross salary for a mid-level Software Developer (EUR/yr)",
                "costOfLiving": "Estimated annual cost of living, single person, capital city (EUR/yr)",
            },
            "note": ("European countries have data points at the three gross benchmarks plus the "
                     "local developer average. US cities (marked approximate) come from a separate "
                     "Boundless study with a single USD benchmark, converted to EUR at "
                     f"1 EUR = {FX_USD_PER_EUR} USD, and modelled at a flat effective rate. The "
                     "calculator interpolates linearly between points. Figures are estimates for "
                     "comparison only."),
        },
        "countries": countries,
    }

    (ROOT / "data").mkdir(exist_ok=True)
    with open(ROOT / "data" / "ebook.json", "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    with open(ROOT / "data" / "ebook.js", "w", encoding="utf-8") as f:
        f.write("// AUTO-GENERATED from data/ebook.json by tools/extract_data.py - do not edit by hand.\n")
        f.write("window.SALARY_DATA_EBOOK = " + json.dumps(doc, ensure_ascii=False) + ";\n")
    print(f"Wrote data/ebook.json and data/ebook.js with {len(countries)} entries")


if __name__ == "__main__":
    main()
