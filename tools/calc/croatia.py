"""Croatia salary calculation — computed from published tax rates.

Rates are 2026.

IMPORTANT correction vs the raw research: the employer burden is NOT ~33.7%.
In Croatia the pension contributions (20%) are employee-side, and the old
unemployment + work-injury contributions were merged into the health
contribution in 2019. So the employer pays only **16.5% health** on top of gross
— confirmed by the live calculators (Deel @60k = €69,900 = exactly 16.5%).

Income tax is municipality-set (lower bracket 15–23%, upper 25–33%). We use
Zagreb's rates (23% / 33%) for consistency with the rest of the app, which uses
the capital city. Most other municipalities use the default 20% / 30%.

Verified vs Porezna uprava / PwC: the €60k threshold is on the TAXABLE BASE
(gross − contributions − allowance), the €143,496/yr ceiling covers both pension
pillars, and the 23% rate matches the eBook at €60k. NOTE: the official "worked
example" we were given misapplied the contribution ceiling (charged 20% on the
cap, not on a below-cap salary) and produced an impossible net — so we implement
the rules, not that example.

Sources: Porezna uprava (Tax Administration); PwC Croatia sample calculation;
Official Gazette Order 2237/2025.
"""
from engine import progressive

NAME = "Croatia"
CURRENCY = "EUR"
YEAR = 2026
INF = float("inf")

# Employer, on top of gross: health insurance only (incl. unemployment +
# work-injury merged in since 2019). No cap.
EMPLOYER_HEALTH = 0.165

# Employee, deducted from gross: pension pillar I (15%) + pillar II (5%) = 20%,
# capped at the highest contribution base (€143,496/yr).
EMPLOYEE_PENSION = 0.20
PENSION_CAP = 143496

# Income tax on (gross − pension − personal allowance); Zagreb rates (max range).
PERSONAL_ALLOWANCE = 7200                      # €600/mo, no phase-out
TAX_BRACKETS = [(60000, 0.23), (INF, 0.33)]    # Zagreb; national default is 20% / 30%


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    employer_cost = gross * (1 + EMPLOYER_HEALTH)

    pension = min(gross, PENSION_CAP) * EMPLOYEE_PENSION
    taxable = max(0.0, gross - pension - PERSONAL_ALLOWANCE)
    income_tax = progressive(taxable, TAX_BRACKETS)

    net = gross - pension - income_tax
    return employer_cost, net
