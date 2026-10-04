"""Austria salary calculation — computed from published tax rates.

Rates are 2026 (single, no children, full insurance). Austria is a 14-SALARY
system and that's the whole game: the two extra "special payments" (13th/14th) are
taxed at a flat favourable rate, which lifts net well above what a naive 12-month
progressive calc would give.

Representative Vienna scenario with 14 equal payments. Employee unemployment
rates vary with each payment; regular and special contributions use their final
2026 rates and ceilings. Tax includes the statutory transport credit/surcharge,
negative-tax treatment and special-payment overflow into ordinary income.

Sources: PwC Austria 2026 (brackets + worked examples); ÖGK 2026 SS rates.
"""
from engine import progressive

NAME = "Austria"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social security 20.38% (capped) + DB 3.7% + Kommunalsteuer 3.0% + DZ 0.36% + MVK 1.53%"
INF = float("inf")

MONTHLY_CEIL = 6930
SPECIAL_CEIL = 13860
EE_REGULAR_BASE = 0.1537
EE_SPECIAL_BASE = 0.1412
ER_REGULAR = 0.2123
ER_SPECIAL = 0.2048
ER_LEVIES = 0.037 + 0.0036 + 0.03 + 0.0153   # DB + DZ + Kommunalsteuer + MVK ≈ 8.59%
SPECIAL_EXEMPT = 620
SPECIAL_BANDS = [(620, 0.0), (25000, 0.06), (50000, 0.27), (83333, 0.3575), (INF, 0.0)]
VIENNA_DGA = 106

BRACKETS = [(13539, 0.0), (21992, 0.20), (36458, 0.30), (70365, 0.40),
            (104859, 0.48), (1000000, 0.50), (INF, 0.55)]


def employee_unemployment_rate(payment):
    if payment <= 2225:
        return 0.0
    if payment <= 2427:
        return 0.01
    if payment <= 2630:
        return 0.02
    return 0.0295


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    monthly = gross / 14.0
    regular_annual = monthly * 12
    special_annual = monthly * 2

    av = employee_unemployment_rate(monthly)
    reg_ss = min(monthly, MONTHLY_CEIL) * 12 * (EE_REGULAR_BASE + av)
    spec_ss = min(special_annual, SPECIAL_CEIL) * (EE_SPECIAL_BASE + av)

    net_special = special_annual - spec_ss
    overflow = max(0.0, net_special - 83333)
    ordinary_base = max(0.0, regular_annual - reg_ss - 132 + overflow)
    total_taxable_income = ordinary_base - overflow + net_special
    surcharge = (804 if total_taxable_income <= 19761 else
                 804 * max(0.0, (30259 - total_taxable_income) / (30259 - 19761)))
    reg_tax = progressive(ordinary_base, BRACKETS) - 496 - surcharge
    spec_tax = 0.0 if special_annual <= 2615 else progressive(net_special, SPECIAL_BANDS)

    net = gross - reg_ss - spec_ss - reg_tax - spec_tax

    er_ss = (min(monthly, MONTHLY_CEIL) * 12 * ER_REGULAR
             + min(special_annual, SPECIAL_CEIL) * ER_SPECIAL)
    employer_cost = gross + er_ss + gross * ER_LEVIES + VIENNA_DGA
    return employer_cost, net
