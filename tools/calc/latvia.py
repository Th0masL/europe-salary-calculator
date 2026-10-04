"""Latvia salary calculation — computed from published tax rates.

Rates are 2026 (single, no children). Cash VSAOI continues above the €105,300
social maximum; the excess is reallocated through solidarity-tax reconciliation.
The universal annual non-taxable minimum is €6,600. Final employer cost reflects
the statutory 9.09%-of-excess refund and the €4.32 business-risk fee.

Sources: VID 2026 (PIT rates); PwC/KPMG Latvia 2026 (NSIC split, €105,300 cap).
"""
from engine import progressive

NAME = "Latvia"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "VSAOI/solidarity 23.59% cash rate with 9.09%-of-excess refund + €4.32 risk fee"
INF = float("inf")

NSIC_CAP = 105300
EE_NSIC = 0.105
ER_NSIC = 0.2359
NON_TAXABLE_MINIMUM = 6600
RISK_FEE = 4.32


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    employee_cash = gross * EE_NSIC
    excess = max(0.0, gross - NSIC_CAP)
    solidarity_pit_advance = 0.10 * excess
    deductible_social = employee_cash - solidarity_pit_advance
    deductions = deductible_social + NON_TAXABLE_MINIMUM
    lower_gross = min(gross, NSIC_CAP)
    lower_base = max(0.0, lower_gross - deductions)
    remaining_deductions = max(0.0, deductions - lower_gross)
    upper_base = max(0.0, excess - remaining_deductions)
    ordinary_pit = 0.255 * lower_base + 0.33 * upper_base
    additional_tax = 0.03 * max(0.0, gross - 200000)

    net = gross - employee_cash - ordinary_pit - additional_tax + solidarity_pit_advance
    employer_refund = 0.0909 * excess
    employer_cost = gross + gross * ER_NSIC - employer_refund + RISK_FEE
    return employer_cost, net
