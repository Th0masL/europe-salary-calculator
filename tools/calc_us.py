#!/usr/bin/env python3
"""
Compute US employment cost + net pay directly from published 2025
rates — NO reliance on EOR/payroll vendors. Writes data/us.json + data/us.js.

Covers the 5 cities we track (state-level): Seattle/WA, San Francisco/CA,
New York/NY (incl. NYC local tax), Austin/TX, Atlanta/GA.

Assumptions (the same simplifications every paycheck calculator makes):
  * single filer, standard deduction, no dependents/credits/itemizing
  * employer cost = mandatory payroll taxes only (employer FICA + FUTA + SUTA);
    workers' comp / benefits are excluded (they're insurance, not a tax, and
    vary by occupation) — this is the pure "direct employer" tax burden
  * SUTA uses representative new-employer rates (varies by employer in reality)

Salaries are entered in EUR (to match the rest of the tool); we convert to USD
via the live ECB rate, compute in USD, and convert results back to EUR.

Usage:
    python3 tools/calc_us.py
"""
import datetime
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FX_URL = "https://api.frankfurter.app/latest?from=EUR&to=USD"
UA = "Mozilla/5.0 (salary-calculator)"
SALARY_POINTS = list(range(20000, 400001, 10000))  # 20k..400k EUR, 10k step (39 points)

# ---- 2025 federal -----------------------------------------------------------
FED_STD_DEDUCTION = 15000
FED_BRACKETS = [  # (upper bound of taxable income, marginal rate)
    (11925, 0.10), (48475, 0.12), (103350, 0.22), (197300, 0.24),
    (250525, 0.32), (626350, 0.35), (float("inf"), 0.37),
]
SS_RATE = 0.062
SS_WAGE_BASE = 176100        # 2025 Social Security wage cap
MEDICARE_RATE = 0.0145
ADD_MEDICARE_RATE = 0.009    # employee only, wages over $200k (single)
ADD_MEDICARE_THRESHOLD = 200000
FUTA = 0.006 * 7000          # 0.6% effective on first $7,000 => $42 max

# ---- per-state --------------------------------------------------------------
# state income tax: None | flat | brackets. Plus SUTA (rate, wage base) and any
# extra employee levies (CA SDI, NYC local).
STATES = {
    "Washington": {
        "income": None,                       # no state income tax
        "suta": (0.0125, 72800),              # WA 2025 wage base $72,800
    },
    "Texas": {
        "income": None,
        "suta": (0.027, 9000),                # new-employer 2.7%, base $9,000
    },
    "Georgia": {
        "income": ("flat", 0.0539, 12000),    # 5.39% flat (2025), $12,000 std ded
        "suta": (0.027, 9500),
    },
    "California": {
        "income": ("brackets", 5540, [        # 2025 single brackets, $5,540 std ded
            (10756, 0.01), (25499, 0.02), (40245, 0.04), (55866, 0.06),
            (70606, 0.08), (360659, 0.093), (432787, 0.103), (721314, 0.113),
            (float("inf"), 0.123)]),
        "sdi": 0.012,                         # CA SDI 1.2% (2025), uncapped, employee
        "suta": (0.034, 7000),                # new-employer 3.4%, base $7,000
    },
    "New York": {
        "income": ("brackets", 8000, [        # NY state 2025 single, $8,000 std ded
            (8500, 0.04), (11700, 0.045), (13900, 0.0525), (80650, 0.055),
            (215400, 0.06), (1077550, 0.0685), (5000000, 0.0965),
            (25000000, 0.103), (float("inf"), 0.109)]),
        "local": ("brackets", 0, [            # NYC resident tax, single
            (12000, 0.03078), (25000, 0.03762), (50000, 0.03819),
            (float("inf"), 0.03876)]),
        "suta": (0.041, 12800),               # NY new-employer ~4.1%, base $12,800
    },
    "Florida": {
        "income": None,                       # no state income tax
        "suta": (0.027, 7000),                # new-employer 2.7%, base $7,000
    },
    "Illinois": {
        "income": ("flat", 0.0495, 2775),     # 4.95% flat; IL personal exemption (no std ded)
        "suta": (0.0395, 13916),              # new-employer ~3.95%, 2025 base $13,916
        # Chicago: no city income tax
    },
    "Massachusetts": {
        "income": ("flat", 0.05, 4400),       # 5% flat earned income; $4,400 personal exemption
        "sdi": 0.0046, "sdi_capped": True,    # MA PFML employee share ~0.46% (2025), SS-capped
        "suta": (0.0187, 15000),              # new-employer ~1.87%, base $15,000
        # Boston: no local income tax; 4% surtax >$1.083M not reached in our range
    },
    "Colorado": {
        "income": ("flat", 0.044, 15000),     # 4.40% flat on federal taxable income (fed $15k std)
        "sdi": 0.0045, "sdi_capped": True,    # CO FAMLI employee share 0.45% (2025), SS-capped
        "head_tax": (69.0, 48.0),             # Denver OPT: employee $5.75/mo, employer $4/mo
        "suta": (0.0305, 27200),              # new-employer ~3.05%, 2025 base $27,200
    },
    "District of Columbia": {
        "income": ("brackets", 15000, [       # DC 2025 single, $15,000 standard deduction
            (10000, 0.04), (40000, 0.06), (60000, 0.065), (250000, 0.085),
            (500000, 0.0925), (1000000, 0.0975), (float("inf"), 0.1075)]),
        "suta": (0.027, 9000),                # new-employer 2.7%, base $9,000
        # DC Paid Family Leave is employer-paid (0.75%) — excluded like WA's (see note)
    },
}

# our city labels -> (state, annual cost of living EUR for a single person =
# Numbeo "single person monthly costs excl. rent" + "1-bed apartment city centre"
# rent, x12). The first five match the eBook (Boundless/Numbeo); Miami is from
# Numbeo directly (numbeo.com/cost-of-living/in/Miami): $1,455 + $2,821/mo.
CITIES = [
    ("Seattle, WA", "Washington", 40522),
    ("San Francisco, CA", "California", 50802),
    ("New York, NY", "New York", 60046),
    ("Austin, TX", "Texas", 35197),
    ("Atlanta, GA", "Georgia", 33187),
    ("Miami, FL", "Florida", 44800),
    # These five from fetch_numbeo.py (single + avg city-centre/outside rent). The
    # live cost_of_living.json map is what the app actually displays; these are the
    # baked fallback.
    ("Chicago, IL", "Illinois", 34980),
    ("Los Angeles, CA", "California", 40615),
    ("Boston, MA", "Massachusetts", 47256),
    ("Washington, DC", "District of Columbia", 41708),
    ("Denver, CO", "Colorado", 33410),
]


def progressive(taxable, brackets):
    """Marginal-bracket tax on `taxable`. brackets = [(upper, rate), ...]."""
    tax, lower = 0.0, 0.0
    for upper, rate in brackets:
        if taxable > lower:
            tax += (min(taxable, upper) - lower) * rate
            lower = upper
        else:
            break
    return tax


def state_income_tax(gross, cfg):
    inc = cfg.get("income")
    if not inc:
        return 0.0
    if inc[0] == "flat":
        _, rate, std = inc
        return max(0.0, gross - std) * rate
    if inc[0] == "brackets":
        _, std, brackets = inc
        return progressive(max(0.0, gross - std), brackets)
    return 0.0


def local_tax(gross, cfg):
    loc = cfg.get("local")
    if not loc:
        return 0.0
    _, std, brackets = loc
    return progressive(max(0.0, gross - std), brackets)


def employee_fica(gross):
    ss = min(gross, SS_WAGE_BASE) * SS_RATE
    medicare = gross * MEDICARE_RATE
    add = max(0.0, gross - ADD_MEDICARE_THRESHOLD) * ADD_MEDICARE_RATE
    return ss + medicare + add


def employer_payroll(gross, cfg):
    ss = min(gross, SS_WAGE_BASE) * SS_RATE
    medicare = gross * MEDICARE_RATE
    suta_rate, suta_base = cfg["suta"]
    suta = min(gross, suta_base) * suta_rate
    return ss + medicare + FUTA + suta


def compute(gross_usd, cfg):
    """Return (employer_cost_usd, net_usd) for a single filer."""
    fed = progressive(max(0.0, gross_usd - FED_STD_DEDUCTION), FED_BRACKETS)
    state = state_income_tax(gross_usd, cfg)
    local = local_tax(gross_usd, cfg)
    sdi_base = min(gross_usd, SS_WAGE_BASE) if cfg.get("sdi_capped") else gross_usd
    sdi = sdi_base * cfg.get("sdi", 0.0)             # CA SDI (uncapped) / MA PFML, CO FAMLI (SS-capped)
    head_ee, head_er = cfg.get("head_tax", (0.0, 0.0))  # fixed local head tax (Denver OPT)
    emp_fica = employee_fica(gross_usd)
    net = gross_usd - fed - state - local - sdi - emp_fica - head_ee
    cost = gross_usd + employer_payroll(gross_usd, cfg) + head_er
    return round(cost), round(net)


def get_fx():
    req = urllib.request.Request(FX_URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["rates"]["USD"]  # USD per 1 EUR


def main():
    try:
        fx = get_fx()
    except Exception as e:  # noqa: BLE001
        fx = 1.15
        print(f"  ! FX fetch failed ({e}); using EUR->USD = {fx}", file=sys.stderr)
    print(f"  EUR->USD = {fx:.4f}")

    out = []
    for label, state, col in CITIES:
        cfg = STATES[state]
        points = []
        for gross_eur in SALARY_POINTS:
            cost_usd, net_usd = compute(gross_eur * fx, cfg)
            points.append({"gross": gross_eur,
                           "cost": round(cost_usd / fx),
                           "net": round(net_usd / fx)})
        out.append({"name": label, "us": True, "flag": "\U0001F1FA\U0001F1F8",
                    "costOfLiving": col, "points": points})
        p60 = next(p for p in points if p["gross"] == 60000)
        print(f"  {label}: cost@60k €{p60['cost']}, net@60k €{p60['net']}")

    # self-check against Deel's independent per-state numbers, if present
    deel_path = ROOT / "data" / "deel.json"
    if deel_path.exists():
        deel = {c["name"]: c["points"] for c in
                json.loads(deel_path.read_text(encoding="utf-8"))["countries"]}
        print("\n  validation vs Deel (net @ €60k / €150k):")
        for c in out:
            dp = {p["gross"]: p for p in deel.get(c["name"], [])}
            mp = {p["gross"]: p for p in c["points"]}
            diffs = []
            for g in (60000, 150000):
                if g in dp and g in mp and dp[g].get("net"):
                    diffs.append(f"{(mp[g]['net'] - dp[g]['net']) / dp[g]['net'] * 100:+.1f}%")
            print(f"    {c['name']:<20} {' / '.join(diffs) or 'n/a'}")

    doc = {
        "meta": {
            "title": "US employment cost + net (direct calc from published rates)",
            "source": "Computed from published 2025 US federal + state rates (no EOR vendor)",
            "currency": "EUR",
            "fetched": datetime.date.today().isoformat(),
            "fxEurUsd": round(fx, 4),
            "provides": ["gross", "cost", "net"],
            "salaryPoints": SALARY_POINTS,
            "note": ("Single filer, standard deduction, no credits. Employer cost = "
                     "mandatory payroll taxes only (employer FICA + FUTA + SUTA + Denver "
                     "OPT); workers' comp/benefits and employer paid-leave premiums (DC/WA) "
                     "excluded. NYC local tax included for New York. Employee disability/"
                     "paid-leave levies included where they exist (CA SDI, MA PFML, CO "
                     "FAMLI). SUTA uses representative new-employer rates. Estimates "
                     "for comparison only."),
        },
        "countries": out,
    }
    (ROOT / "data").mkdir(exist_ok=True)
    with open(ROOT / "data" / "us.json", "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    with open(ROOT / "data" / "us.js", "w", encoding="utf-8") as f:
        f.write("// AUTO-GENERATED from data/us.json by tools/calc_us.py - do not edit.\n")
        f.write("window.SALARY_DATA_US = " + json.dumps(doc, ensure_ascii=False) + ";\n")
    print(f"\nWrote data/us.json + data/us.js with {len(out)} US cities.")


if __name__ == "__main__":
    main()
