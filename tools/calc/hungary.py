"""Hungary salary calculation — computed from published tax rates.

Rates are 2026 (single, no children — the family / under-25 / mother allowances
don't apply). Hungary's flat system is the simplest here:
 - Employee: 18.5% social security (single combined rate, uncapped).
 - Personal income tax: flat 15%, charged on GROSS — employee contributions are
   NOT deductible from the PIT base — so net is a flat 66.5% of gross.
 - Employer: 13% social contribution tax (szocho), uncapped.

Currency note: Hungary uses the forint (HUF), but every figure here is a flat
percentage with no HUF-denominated threshold, so the calculation is
currency-invariant — we compute directly in EUR and skip an unnecessary FX
round-trip. (Switch CURRENCY to "HUF" if a forint-denominated cap is ever added.)

Sources: PwC Hungary 2026; NAV (13% szocho + 18.5% contribution + 15% flat PIT).
"""

NAME = "Hungary"
CURRENCY = "EUR"            # real currency is HUF — see the currency note above
YEAR = 2026

EMPLOYEE_SS = 0.185
INCOME_TAX = 0.15          # flat, charged on gross
EMPLOYER_SZOCHO = 0.13


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    employee = gross * EMPLOYEE_SS
    income_tax = gross * INCOME_TAX        # PIT base is gross, not gross − SS
    net = gross - employee - income_tax    # = gross * 0.665
    employer_cost = gross * (1 + EMPLOYER_SZOCHO)
    return employer_cost, net
