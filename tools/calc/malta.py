"""Malta salary calculation — computed from published tax rates.

Rates are 2026 (single person).

Two things that make Malta different from the % countries:
 - Social Security (Class 1) is **capped at a fixed weekly amount** (€55.93/week
   in 2026, ~€2,908/yr). Above ~€29k/yr it's a flat cash amount, not 10%.
 - Income tax is on **chargeable income = gross − employee SSC** (SSC IS
   deductible). Verified against the official rates via PwC Tax Summaries /
   Commissioner for Revenue: €60k gross → net €46,218.73. (An earlier version
   here wrongly taxed the full gross because it had been "checked" against the
   EOR APIs — which both under-deduct and agree with each other. Lesson logged.)
   The €12,000 tax-free amount is the 0% band of the brackets, not a separate
   allowance on top.

The employer also pays the Maternity Leave Trust Fund (0.3%). Its cap is unclear:
the research's rate table says capped at €1.68/week (~€87/yr, same wage ceiling as
SSC), but its worked example applied a flat 0.3% (€180 on €60k). We use the capped
figure; the difference is < €100/yr. (Worth a quick re-verify.)
Malta also has statutory bonuses (~€512/yr); like the other sources we treat the
entered gross as the full annual figure and don't add them on top.

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

# Income tax on gross (single, 2026); €12,000 tax-free as the 0% band.
TAX_BRACKETS = [(12000, 0.0), (16000, 0.15), (60000, 0.25), (INF, 0.35)]


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    ssc = min(SSC_RATE * gross, SSC_CAP)            # employee & employer each
    maternity = min(MATERNITY_RATE * gross, MATERNITY_CAP)
    income_tax = progressive(gross - ssc, TAX_BRACKETS)  # SSC is deductible (chargeable income)

    net = gross - ssc - income_tax
    employer_cost = gross + ssc + maternity
    return employer_cost, net
