"""Greece salary calculation — computed from published tax rates.

Rates are 2026 for the representative age-30, single, no-child employee paid as
12 salaries plus Christmas, Easter and holiday amounts. Each payment receives its
own EFKA ceiling. The age-30 PIT scale uses 9% through €20,000 and the Article 16
reduction. Employer cost includes the selected KPK 101 €20 ELPC charge.

Sources: PwC Greece 2026 (EFKA rates + €7,761.94/mo cap; PIT brackets).
"""
from engine import progressive

NAME = "Greece"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "EFKA 21.79% with 14-payment ceilings + €20 ELPC (KPK 101 scenario)"
INF = float("inf")

MONTHLY_EFKA_CAP = 7761.94
EE_EFKA = 0.1337
ER_EFKA = 0.2179
BRACKETS = [(20000, 0.09), (30000, 0.26), (40000, 0.34), (60000, 0.39), (INF, 0.44)]
ELPC = 20


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    monthly_unit = gross / 14
    efka_base = (13 * min(monthly_unit, MONTHLY_EFKA_CAP)
                 + 2 * min(0.5 * monthly_unit, MONTHLY_EFKA_CAP))
    ee_efka = efka_base * EE_EFKA
    taxable = max(0.0, gross - ee_efka)
    tax_before_credit = progressive(taxable, BRACKETS)
    credit = max(0.0, min(tax_before_credit, 777 - 0.02 * max(taxable - 12000, 0)))
    income_tax = tax_before_credit - credit

    net = gross - ee_efka - income_tax
    employer_cost = gross + efka_base * ER_EFKA + ELPC
    return employer_cost, net
