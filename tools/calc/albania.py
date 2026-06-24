"""Albania salary calculation — computed from published tax rates.

Rates are 2026 (single). Currency ALL (FX path).
 - Employee: social security 9.5% (wage base capped at ALL 186,416/mo) + health
   1.7% (on full gross, no cap).
 - Income tax: progressive monthly withholding table — 0 up to ALL 30,000/mo, 13%
   to ALL 150,000/mo, 23% above — applied to GROSS (contributions not deductible).
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
# Monthly PIT table -> annual brackets (×12): 0 to 360k, 13% to 1.8M, 23% above.
PIT = [(360000, 0.0), (1800000, 0.13), (INF, 0.23)]


def compute(gross):
    """Return (employer_cost, net) in ALL; build_formula converts to EUR."""
    ss_base = min(max(gross, SS_FLOOR), SS_CAP)
    employee = ss_base * EE_SS + gross * EE_HEALTH
    pit = progressive(gross, PIT)        # withholding table is on gross

    net = gross - employee - pit
    employer_cost = gross + ss_base * ER_SS + gross * ER_HEALTH
    return employer_cost, net
