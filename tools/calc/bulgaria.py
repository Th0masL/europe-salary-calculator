"""Bulgaria salary calculation — computed from published tax rates.

Rates are 2026 (single private-sector employee). Bulgaria adopted the euro on
1 Jan 2026.

Key features:
 - Social-security + health contributions are CAPPED at a low maximum insurable
   income: €2,111.64/month = €25,339.68/yr. Above ~€25k all contributions stop
   growing, so employer cost and the employee deduction are flat in cash terms —
   that's why Bulgaria's employer-cost % falls sharply as salary rises.
 - Flat 10% income tax (no brackets, no personal allowance).
 - Tax base = gross − employee contributions; then 10%.

Rates (PwC 2026):
 - Employee: 10.58% social security + 3.20% health = 13.78% (capped).
 - Employer: 13.72% social security + 4.80% health + accident 0.4–1.1% (capped).
   We use a representative office accident rate of 0.5% → 19.02% employer.

Sources: PwC Bulgaria 2026 (rates + €2,111.64 max insurable income); NRA / NSSI.
"""

NAME = "Bulgaria"
CURRENCY = "EUR"
YEAR = 2026

CONTRIB_CAP = 2111.64 * 12          # €25,339.68 / yr — maximum insurable income
EMPLOYEE_RATE = 0.1058 + 0.0320     # 13.78%
EMPLOYER_RATE = 0.1372 + 0.0480 + 0.005   # 19.02% (incl. representative 0.5% accident)
INCOME_TAX = 0.10


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    base = min(gross, CONTRIB_CAP)
    employee_contrib = base * EMPLOYEE_RATE
    taxable = gross - employee_contrib
    income_tax = taxable * INCOME_TAX

    net = gross - employee_contrib - income_tax
    employer_cost = gross + base * EMPLOYER_RATE
    return employer_cost, net
