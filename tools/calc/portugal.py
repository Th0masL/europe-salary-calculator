"""Portugal salary calculation — computed from published tax rates.

Rates are 2026 (single private-sector employee, no dependents, mainland).

Notes:
 - Employee Social Security is 11% of gross, no cap.
 - IRS taxable income = gross − the "specific deduction" for employment income,
   which is max(€4,104, the employee SS paid). Above ~€37k gross the SS exceeds
   €4,104, so in practice taxable = gross − SS. (Confirmed vs PwC / gov.pt; a
   single person gets no extra personal credit. The EOR APIs cluster ~€3–5k lower
   on net because they skip this deduction and over-tax — our figure is realistic.)
 - IRS is progressive (2026 brackets), plus a "solidarity" surcharge: 2.5% on
   taxable income from €80,000 to €250,000 and 5% above €250,000.
 - Portugal pays 14 months (holiday + Christmas allowances are mandatory), but
   that's payment TIMING — the annual gross total is unchanged, so the annual
   gross-to-net here is unaffected. We treat the entered figure as annual total.

Employer side (verified): TSU 23.75% + Wage Guarantee Fund (FGS) 1.00% +
work-accident insurance ~1.00% (occupation-dependent, configurable) = 25.75%.
Verification confirmed the FGS is a SEPARATE charge, not folded into the TSU; the
total matches the eBook/Rippling cluster (~25.5%).

Sources: PwC Portugal 2026 budget (IRS brackets, solidarity); TSU 23.75%/11%; FGS
1.00% (separate).
"""
from engine import progressive

NAME = "Portugal"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social Security (TSU) 23.75% + Wage Guarantee Fund 1.0% + work-accident ~1.0%"
INF = float("inf")

EMPLOYEE_SS = 0.11
EMPLOYER_SS = 0.2375                      # TSU (excludes FGS — that's separate below)
EMPLOYER_FGS = 0.01                       # Wage Guarantee Fund, separate charge
EMPLOYER_WORK_ACCIDENT = 0.01            # mandatory insurance, ~office rate (configurable)

SPECIFIC_DEDUCTION = 4104                 # or the SS paid, whichever is larger

# IRS 2026 progressive brackets (annual taxable income).
TAX_BRACKETS = [
    (8342, 0.125), (12587, 0.157), (17838, 0.212), (23089, 0.241),
    (29397, 0.311), (43090, 0.349), (46566, 0.431), (86634, 0.446), (INF, 0.48),
]


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    ss = gross * EMPLOYEE_SS
    taxable = max(0.0, gross - max(SPECIFIC_DEDUCTION, ss))
    irs = progressive(taxable, TAX_BRACKETS)
    solidarity = 0.025 * max(0.0, min(taxable, 250000) - 80000) \
               + 0.05 * max(0.0, taxable - 250000)

    net = gross - ss - irs - solidarity
    employer_cost = gross * (1 + EMPLOYER_SS + EMPLOYER_FGS + EMPLOYER_WORK_ACCIDENT)
    return employer_cost, net
