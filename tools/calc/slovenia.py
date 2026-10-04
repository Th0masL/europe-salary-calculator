"""Slovenia salary calculation — computed from published tax rates.

Rates are 2026 (single, no children).
 - Employee: social security 22.10% + long-term care 1.00% = 23.10%, plus the flat
   compulsory health contribution (OZP): €37.17 in Jan–Feb and €39.36 Mar–Dec.
 - Income tax: progressive 16/26/33/39/50% after all mandatory employee
   contributions, including LTC and OZP, and the €5,551.93 general relief.
 - Employer: social security 16.10% + long-term care 1.00% = 17.10%.
 - Full-year mandatory vacation and winter regresses add €2,222.82 to employer
   cash cost outside regular gross salary.

Sources: PwC/FURS Slovenia 2026 (PIT base + brackets); taxravens/lano (SS, LTC, OZP).
"""
from engine import progressive

NAME = "Slovenia"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social security 16.10% + long-term care 1.0% + minimum vacation/winter regresses €2,222.82"
INF = float("inf")

EE_SS = 0.2210
EE_LTC = 0.01
OZP = 2 * 37.17 + 10 * 39.36   # €467.94 in 2026
ER_SS = 0.1610 + 0.01          # social security + long-term care = 17.10%
MANDATORY_REGRESSES = 1481.88 + 740.94
GENERAL_RELIEF = 5551.93
BRACKETS = [(9721.43, 0.16), (28592.44, 0.26), (57184.88, 0.33), (82346.23, 0.39), (INF, 0.50)]


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    ss = gross * EE_SS
    ltc = gross * EE_LTC
    tax_base = max(0.0, gross - ss - ltc - OZP - GENERAL_RELIEF)
    pit = progressive(tax_base, BRACKETS)

    net = gross - ss - ltc - OZP - pit
    employer_cost = gross * (1 + ER_SS) + MANDATORY_REGRESSES
    return employer_cost, net
