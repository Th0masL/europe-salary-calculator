#!/usr/bin/env python3
"""
Compute US employment cost + net pay directly from published 2026
rates — NO reliance on EOR/payroll vendors. Writes data/us.json + data/us.js.

Covers the 11 cities tracked by the website. Most are state-level calculations;
New York includes NYC resident tax and Denver includes its local occupational tax.

Assumptions (the same simplifications every paycheck calculator makes):
  * single filer, standard deduction, no dependents/credits/itemizing
  * employer cost = mandatory payroll taxes only (employer FICA + FUTA + SUTA
    and configured state paid-leave premiums for a representative larger employer);
    workers' comp / benefits are excluded (they're insurance, not a tax, and
    vary by occupation) — this is the pure "direct employer" tax burden
  * SUTA uses representative new-employer rates (varies by employer in reality)

Salaries are entered in EUR (to match the rest of the tool); we convert to USD
via the live ECB rate, compute in USD, and convert results back to EUR.

Usage:
    python3 tools/calc_us.py
"""
import datetime
import argparse
import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FX_URL = "https://api.frankfurter.app/latest?from=EUR&to=USD"
UA = "Mozilla/5.0 (salary-calculator)"
SALARY_POINTS = list(range(20000, 600001, 5000))  # 20k..600k EUR, 5k step (117 points)
YEAR = 2026
RESEARCHED = "2026-10-04"
INDEPENDENT_REVIEW = "Pending"
SOURCES = [
    "https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill",
    "https://www.ssa.gov/oact/COLA/cbb.html",
    "https://edd.ca.gov/en/payroll_taxes/rates_and_withholding/",
    "https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.html",
    "https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf",
    "https://www.tax.ny.gov/bus/wt/rate.htm",
    "https://www.tax.ny.gov/pdf/publications/withholding/nys50_t_nys.pdf",
    "https://dor.georgia.gov/taxes/important-tax-updates",
    "https://tax.illinois.gov/questionsandanswers/answer.851.html",
    "https://www.mass.gov/info-details/tax-rates",
    "https://tax.colorado.gov/sites/tax/files/documents/DR_0104EP_2026.pdf",
    "https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026_D40ES_Book_wLinks04012026.pdf",
    "https://paidleave.wa.gov/estimate-your-paid-leave-payments/",
    "https://wacaresfund.wa.gov/how-it-works",
    "https://esd.wa.gov/employer-requirements/unemployment-taxes/how-we-determine-tax-rates",
    "https://efte.twc.texas.gov/estimate_cbs_and_tax_rates.html",
    "https://dol.georgia.gov/faqs-employers/employers-faqs-unemployment-insurance",
    "https://floridarevenue.com/taxes/taxesfees/Pages/rt_rate.aspx",
    "https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/EA-50_2026.pdf",
    "https://dol.ny.gov/node/131",
    "https://www.mass.gov/info-details/employer-contributions-to-unemployment",
    "https://www.mass.gov/info-details/paid-family-and-medical-leave-employer-contribution-rates-and-calculator",
    "https://famli.colorado.gov/employers/premiums-and-finances",
    "https://dcpaidfamilyleave.dc.gov/employer-information/",
    "https://essp.does.dc.gov/DOES%20ESSP%20Employer%20Landing%20Page.html",
]

# ---- 2026 federal -----------------------------------------------------------
FED_STD_DEDUCTION = 16100
FED_BRACKETS = [  # (upper bound of taxable income, marginal rate)
    (12400, 0.10), (50400, 0.12), (105700, 0.22), (201775, 0.24),
    (256225, 0.32), (640600, 0.35), (float("inf"), 0.37),
]
SS_RATE = 0.062
SS_WAGE_BASE = 184500        # 2026 Social Security wage cap
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
        "suta": (0.0125, 78200),              # representative rate; 2026 wage base
        # 2026 Paid Leave: 1.13%, split 71.43% employee / 28.57% employer.
        # WA Cares: employee-only 0.58%, uncapped. Employer share assumes 50+ staff.
        "employee_levies": [(0.0113 * 0.7143, SS_WAGE_BASE), (0.0058, None)],
        "employer_levies": [(0.0113 * 0.2857, SS_WAGE_BASE)],
    },
    "Texas": {
        "income": None,
        "suta": (0.027, 9000),                # new-employer 2.7%, base $9,000
    },
    "Georgia": {
        "income": ("flat", 0.0499, 15000),    # 2026 flat rate and single deduction
        "suta": (0.027, 9500),
    },
    "California": {
        # FTB's 2026 estimate instructions specify the $5,706 deduction and the
        # latest published (2025) tax table while the final 2026 return is pending.
        "income": ("brackets", 5706, [
            (11079, 0.01), (26264, 0.02), (41452, 0.04), (57542, 0.06),
            (72724, 0.08), (371479, 0.093), (445771, 0.103), (742953, 0.113),
            (float("inf"), 0.123)]),
        "employee_levies": [(0.013, None)],    # 2026 CA SDI, uncapped
        "employer_levies": [(0.001, 7000)],   # Employment Training Tax
        "suta": (0.034, 7000),
    },
    "New York": {
        "income": ("brackets", 8000, [        # enacted first step of 2026 rate cut
            (8500, 0.039), (11700, 0.044), (13900, 0.0515), (80650, 0.054),
            (215400, 0.059), (1077550, 0.0685), (5000000, 0.0965),
            (25000000, 0.103), (float("inf"), 0.109)]),
        "local": ("brackets", 0, [            # NYC resident tax, single
            (12000, 0.03078), (25000, 0.03762), (50000, 0.03819),
            (float("inf"), 0.03876)]),
        "suta": (0.041, 13000),               # 2026 new-employer total, wage base
    },
    "Florida": {
        "income": None,                       # no state income tax
        "suta": (0.027, 7000),                # new-employer 2.7%, base $7,000
    },
    "Illinois": {
        "income": ("flat", 0.0495, 2925),     # exemption unavailable above $250k AGI
        "deduction_income_limit": 250000,
        "suta": (0.0335, 14250),              # 2026 standard entry rate and wage base
        # Chicago: no city income tax
    },
    "Massachusetts": {
        "income": ("flat", 0.05, 4400),       # 5% flat earned income; $4,400 personal exemption
        "surtax": (1107750, 0.04),             # 2026 millionaire surtax threshold
        "employee_levies": [(0.0046, SS_WAGE_BASE)],
        "employer_levies": [(0.0042, SS_WAGE_BASE)],  # 25+ employee PFML scenario
        "suta": (0.0242, 15000),              # 2026 new-employer rate
        # Boston has no local income tax.
    },
    "Colorado": {
        "income": ("flat", 0.044, FED_STD_DEDUCTION),
        "employee_levies": [(0.0044, SS_WAGE_BASE)],
        "employer_levies": [(0.0044, SS_WAGE_BASE)],  # half of 2026 FAMLI premium
        "head_tax": (69.0, 48.0),             # Denver OPT: employee $5.75/mo, employer $4/mo
        "suta": (0.0305, 30600),              # representative rate; 2026 wage base
    },
    "District of Columbia": {
        "income": ("brackets", FED_STD_DEDUCTION, [
            (10000, 0.04), (40000, 0.06), (60000, 0.065), (250000, 0.085),
            (500000, 0.0925), (1000000, 0.0975), (float("inf"), 0.1075)]),
        "suta": (0.029, 9000),                # new employer 2.7% + 0.2% assessment
        "employer_levies": [(0.0075, None)],  # DC Paid Family Leave
    },
}

# our city labels -> (state, annual cost of living EUR for a single person =
# Numbeo "single person monthly costs excl. rent" + "1-bed apartment city centre"
# rent, x12). These are baked fallbacks; the live cost_of_living.json map is what
# the app actually displays.
CITIES = [
    ("Seattle, WA", "Washington", 40522),
    ("San Francisco, CA", "California", 50802),
    ("New York, NY", "New York", 60046),
    ("Austin, TX", "Texas", 35197),
    ("Atlanta, GA", "Georgia", 33187),
    ("Miami, FL", "Florida", 44800),
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
        if gross > cfg.get("deduction_income_limit", float("inf")):
            std = 0
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


def configured_levies(gross, cfg, side):
    """Employee/employer state program charges as (rate, optional wage cap)."""
    return sum(rate * (gross if cap is None else min(gross, cap))
               for rate, cap in cfg.get(f"{side}_levies", ()))


def employer_cost_note(cfg):
    parts = ["Employer FICA", "FUTA", "representative new-employer SUTA"]
    if cfg.get("employer_levies"):
        parts.append("applicable state paid-leave/training premiums")
    if cfg.get("head_tax"):
        parts.append("Denver employer OPT")
    return " + ".join(parts)


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
    return ss + medicare + FUTA + suta + configured_levies(gross, cfg, "employer")


def compute(gross_usd, cfg):
    """Return (employer_cost_usd, net_usd) for a single filer."""
    fed = progressive(max(0.0, gross_usd - FED_STD_DEDUCTION), FED_BRACKETS)
    state = state_income_tax(gross_usd, cfg)
    if cfg.get("surtax"):
        threshold, rate = cfg["surtax"]
        state += max(0.0, gross_usd - threshold) * rate
    local = local_tax(gross_usd, cfg)
    employee_levies = configured_levies(gross_usd, cfg, "employee")
    head_ee, head_er = cfg.get("head_tax", (0.0, 0.0))  # fixed local head tax (Denver OPT)
    emp_fica = employee_fica(gross_usd)
    net = gross_usd - fed - state - local - employee_levies - emp_fica - head_ee
    cost = gross_usd + employer_payroll(gross_usd, cfg) + head_er
    return round(cost), round(net)


def get_fx():
    req = urllib.request.Request(FX_URL, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["rates"]["USD"]  # USD per 1 EUR


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fx", type=float,
                        help="fixed EUR->USD rate (useful for reproducible rebuilds)")
    args = parser.parse_args()
    if args.fx:
        fx = args.fx
    else:
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
        native_points = []
        for gross_eur in SALARY_POINTS:
            gross_usd = gross_eur * fx
            cost_usd, net_usd = compute(gross_usd, cfg)
            points.append({"gross": gross_eur,
                           "cost": round(cost_usd / fx),
                           "net": round(net_usd / fx)})
            native_points.append({"gross": round(gross_usd, 2),
                                  "cost": cost_usd,
                                  "net": net_usd})
        out.append({"name": label, "us": True, "flag": "\U0001F1FA\U0001F1F8", "currency": "USD",
                    "costOfLiving": col, "costNote": employer_cost_note(cfg),
                    "points": points, "nativeCurrency": "USD",
                    "nativePoints": native_points})
        p60 = next(p for p in points if p["gross"] == 60000)
        print(f"  {label}: cost@60k €{p60['cost']}, net@60k €{p60['net']}")

    doc = {
        "meta": {
            "title": "US employment cost + net (direct calc from published rates)",
            "source": "Computed from published 2026 US federal + state rates (no EOR vendor)",
            "sourceUrls": SOURCES,
            "currency": "EUR",
            "year": YEAR,
            "researched": RESEARCHED,
            "independentReview": INDEPENDENT_REVIEW,
            "fetched": datetime.date.today().isoformat(),
            "fxEurUsd": round(fx, 4),
            "provides": ["gross", "cost", "net"],
            "salaryPoints": SALARY_POINTS,
            "note": ("Single filer, standard deduction, no credits. Employer cost = "
                     "mandatory payroll taxes only (employer FICA + FUTA + SUTA, applicable "
                     "paid-leave premiums, and Denver OPT); workers' comp/benefits excluded. "
                     "NYC local tax included for New York. Employee disability/paid-leave "
                     "levies included where they exist. WA/MA paid-leave employer shares use "
                     "the larger-employer tier. SUTA uses representative new-employer rates. Estimates "
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
