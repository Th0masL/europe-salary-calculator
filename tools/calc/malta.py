"""Malta salary calculation — computed from published tax rates.

Rates are 2026 (single person).

Two things that make Malta different from the % countries:
 - Social Security (Class 1) is **capped at a fixed weekly amount** (€55.93/week
   in 2026, ~€2,908/yr). Above ~€29k/yr it's a flat cash amount, not 10%.
 - Income tax is charged on total gross taxable emoluments. Employee SSC is a
   separate payroll deduction and is not deducted from the PIT base.
   The €12,000 tax-free amount is the 0% band of the brackets, not a separate
   allowance on top.

The employer also pays the Maternity and Adoption Leave Trust contribution,
0.3% of basic weekly wage capped at €1.68/week. Malta's €512.52 statutory bonuses
are included in entered total annual gross, but excluded from the weekly SSC and
Maternity contribution bases.

Sources: Commissioner for Revenue (CfR) 2026 SSC + tax rates; PwC Tax Summaries.
"""
from engine import progressive

NAME = "Malta"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Class 1 social security (capped ~€55.93/wk) + Maternity Fund 0.3%"
INF = float("inf")
WEEKS = 52

# Social Security Class 1: 10% of wage, capped at €55.93/week. Both employer
# and employee pay it (same cap).
SSC_RATE = 0.10
SSC_CAP = 55.93 * WEEKS          # €2,908.36 / yr
# Employer-only Maternity Leave Trust Fund: 0.3%, capped €1.68/week.
MATERNITY_RATE = 0.003
MATERNITY_CAP = 1.68 * WEEKS     # €87.36 / yr
STATUTORY_PAYMENTS = 512.52      # taxable bonuses/allowances excluded from SSC base

# Income tax on gross (single, 2026); €12,000 tax-free as the 0% band.
TAX_BRACKETS = [(12000, 0.0), (16000, 0.15), (60000, 0.25), (INF, 0.35)]


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    annual_basic = max(0.0, gross - STATUTORY_PAYMENTS)
    weekly_basic = annual_basic / WEEKS
    weekly_ssc = min(round(SSC_RATE * weekly_basic, 2), SSC_CAP / WEEKS)
    weekly_maternity = min(round(MATERNITY_RATE * weekly_basic, 2), MATERNITY_CAP / WEEKS)
    ssc = weekly_ssc * WEEKS
    maternity = weekly_maternity * WEEKS
    income_tax = progressive(gross, TAX_BRACKETS)

    net = gross - ssc - income_tax
    employer_cost = gross + ssc + maternity
    return employer_cost, net
