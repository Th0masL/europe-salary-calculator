"""Portugal salary calculation — computed from published tax rates.

Rates are 2026 (single private-sector employee, no dependents, mainland).

Notes:
 - Employee Social Security is 11% of gross, no cap.
 - IRS taxable income = gross − the "specific deduction" for employment income,
   which is max(8.54 × IAS = €4,587.0902, the employee SS paid). Above ~€41.7k
   gross the SS exceeds the floor, so in practice taxable = gross − SS. (A
   single person gets no extra personal credit. The EOR APIs cluster ~€3–5k lower
   on net because they skip this deduction and over-tax — our figure is realistic.)
 - IRS is progressive (2026 brackets), plus a "solidarity" surcharge: 2.5% on
   taxable income from €80,000 to €250,000 and 5% above €250,000.
 - Portugal pays 14 months (holiday + Christmas allowances are mandatory), but
   that's payment TIMING — the annual gross total is unchanged, so the annual
   gross-to-net here is unaffected. We treat the entered figure as annual total.

Employer side: the global 23.75% employer Social Security rate already finances
the Wage Guarantee Fund (FGS); adding another 1% would double count it. Mandatory
work-accident insurance is retained as an explicit 1% office-risk estimate because
the actual commercial premium depends on occupation and insurer.

Sources: Portuguese Social Security, CIRS as amended by the 2026 State Budget,
and the 2026 IAS ordinance.
"""
from engine import progressive

NAME = "Portugal"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social Security 23.75% (includes FGS financing) + estimated office work-accident insurance 1.0%"
INF = float("inf")

EMPLOYEE_SS = 0.11
EMPLOYER_SS = 0.2375                      # global rate; includes FGS financing
EMPLOYER_WORK_ACCIDENT = 0.01            # mandatory insurance, ~office rate (configurable)

SPECIFIC_DEDUCTION = 8.54 * 537.13        # 2026 floor; or SS paid if larger

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
    employer_cost = gross * (1 + EMPLOYER_SS + EMPLOYER_WORK_ACCIDENT)
    return employer_cost, net
