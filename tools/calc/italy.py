"""Italy 2026 estimate for the documented Milan/Lombardy scenario."""
from engine import progressive

NAME, CURRENCY, YEAR = "Italy", "EUR", 2026
EMPLOYER_BREAKDOWN = "Small Milan industrial employer: capped FPLD 23.81% + uncapped INPS 5.503333% + INAIL 0.4% + TFR"
INF = float("inf")
CAP, EXTRA_START = 122_295, 56_224
IRPEF = [(28_000, .23), (50_000, .33), (INF, .43)]
LOMBARDY = [(15_000, .0123), (28_000, .0158), (50_000, .0172), (INF, .0173)]


def _employment_credit(income):
    if income <= 15_000:
        return 1_955.0
    if income <= 28_000:
        credit = 1_910 + 1_190 * (28_000 - income) / 13_000
    elif income <= 50_000:
        credit = 1_910 * (50_000 - income) / 22_000
    else:
        return 0.0
    return credit + (65 if 25_000 < income <= 35_000 else 0)


def _wedge_relief(income):
    if income <= 8_500:
        return .071 * income, 0.0
    if income <= 15_000:
        return .053 * income, 0.0
    if income <= 20_000:
        return .048 * income, 0.0
    if income <= 32_000:
        return 0.0, 1_000.0
    if income <= 40_000:
        return 0.0, 1_000 * (40_000 - income) / 8_000
    return 0.0, 0.0


def compute(gross):
    pension_base = min(gross, CAP)
    employee_ss = (.0919 * pension_base + gross * (.005 / 3)
                   + .01 * max(pension_base - EXTRA_START, 0))
    taxable = max(0.0, gross - employee_ss)
    cash_sum, extra_credit = _wedge_relief(taxable)
    national = max(0.0, progressive(taxable, IRPEF) - _employment_credit(taxable) - extra_credit)
    regional = progressive(taxable, LOMBARDY)
    municipal = 0.0 if taxable <= 23_000 else .008 * taxable
    net = gross - employee_ss - national - regional - municipal + cash_sum

    employer_inps = .2381 * pension_base + .05503333 * gross
    tfr = gross / 13.5 - .005 * pension_base
    return gross + employer_inps + .004 * gross + tfr, net
