"""Shared helpers for the per-country formula-based salary calculators.

Each country lives in its own module (tools/calc/<country>.py) and exposes:

    NAME      = "Estonia"          # display name (matches the rest of the app)
    CURRENCY  = "EUR"              # local currency; the runner converts to EUR
    YEAR      = 2025               # tax year the rates are for
    def compute(gross) -> (employer_cost, net)   # all in the local currency

Keeping one file per country makes each set of rates easy to find, verify and
update in isolation. This module only holds maths that several countries share.
"""


def progressive(taxable, brackets):
    """Progressive (marginal-bracket) tax on `taxable`.

    brackets = [(upper_bound, marginal_rate), ...] ascending, last bound = inf.
    e.g. [(11000, 0.0), (25000, 0.10), (inf, 0.20)]
    """
    tax, lower = 0.0, 0.0
    for upper, rate in brackets:
        if taxable <= lower:
            break
        tax += (min(taxable, upper) - lower) * rate
        lower = upper
    return tax
