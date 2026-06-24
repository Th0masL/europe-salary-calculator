"""Greece salary calculation — computed from published tax rates.

Rates are 2026 (single, no children).
 - Employee: EFKA 13.37%, capped at €7,761.94/mo (€93,143/yr).
 - Income tax: progressive 9/20/26/34/39/44% on (gross − EFKA). The employment
   tax credit (~€777) phases out by ~€51k, so it's €0 in this app's salary range.
 - Employer: EFKA 21.79%, capped at €93,143/yr.

Sources: PwC Greece 2026 (EFKA rates + €7,761.94/mo cap; PIT brackets).
"""
from engine import progressive

NAME = "Greece"
CURRENCY = "EUR"
YEAR = 2026
INF = float("inf")

EFKA_CAP = 7761.94 * 12         # €93,143.28/yr
EE_EFKA = 0.1337
ER_EFKA = 0.2179
BRACKETS = [(10000, 0.09), (20000, 0.20), (30000, 0.26), (40000, 0.34), (60000, 0.39), (INF, 0.44)]


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    ee_efka = min(gross, EFKA_CAP) * EE_EFKA
    taxable = max(0.0, gross - ee_efka)
    income_tax = progressive(taxable, BRACKETS)

    net = gross - ee_efka - income_tax
    employer_cost = gross + min(gross, EFKA_CAP) * ER_EFKA
    return employer_cost, net
