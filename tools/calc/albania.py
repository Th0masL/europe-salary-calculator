"""Albania salary calculation — computed from published tax rates.

Rates are 2026 (single). Currency ALL (FX path).
 - Employee: social security 9.5% (wage base capped at ALL 186,416/mo) + health
   1.7% (on full gross, no cap).
 - Income tax: the signed personal-status declaration provides an income-dependent
   monthly personal deduction (ALL 30,000 in the website's range). Taxable monthly
   employment income is taxed at 13% through ALL 170,000 and 23% above.
 - Employer: social security 15.0% (same capped base) + health 1.7%.

Our salary range sits well above the SS cap, so the social part is a flat cash
amount and the employer cost % is low.

Sources: PwC Albania 2026; Albanian tax authority salary table; 2026 fiscal package
(contribution base ALL 50,000–186,416/mo).
"""
from engine import progressive

NAME = "Albania"
CURRENCY = "ALL"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social security 15.0% (capped at ALL 186,416/mo) + health 1.7%"
INF = float("inf")

SS_CAP = 186416 * 12          # ALL 2,236,992/yr maximum base
SS_FLOOR = 50000 * 12         # ALL 600,000/yr minimum base (below this app's range)
EE_SS = 0.095
EE_HEALTH = 0.017
ER_SS = 0.15
ER_HEALTH = 0.017
MONTHLY_PIT_THRESHOLD = 170000


def monthly_personal_deduction(monthly_gross):
    if monthly_gross <= 50000:
        return 50000
    if monthly_gross <= 60000:
        return 35000
    return 30000


def compute(gross):
    """Return annual amounts in ALL for 12 equal monthly payments."""
    monthly_gross = gross / 12
    monthly_ss_base = min(max(monthly_gross, SS_FLOOR / 12), SS_CAP / 12)
    ss_base = monthly_ss_base * 12
    health_base = max(monthly_gross, SS_FLOOR / 12) * 12
    employee = ss_base * EE_SS + health_base * EE_HEALTH

    monthly_taxable = max(0.0, monthly_gross - monthly_personal_deduction(monthly_gross))
    pit = progressive(
        monthly_taxable,
        [(MONTHLY_PIT_THRESHOLD, 0.13), (INF, 0.23)],
    ) * 12

    net = gross - employee - pit
    employer_cost = gross + ss_base * ER_SS + health_base * ER_HEALTH
    return employer_cost, net
