"""Bulgaria salary calculation — computed from published tax rates.

Rates are 2026 (single private-sector employee). Bulgaria adopted the euro on
1 Jan 2026.

Key features:
 - Social-security + health contributions are CAPPED at a low maximum insurable
   income: €2,111.64/month from January through July and €2,300/month from August.
   Above the ceiling, contributions stop growing, so employer cost and the employee
   deduction are flat in cash terms.
 - Flat 10% income tax (no brackets, no personal allowance).
 - Tax base = gross − employee contributions; then 10%.

Rates (PwC 2026):
 - Employee: 10.58% social security + 3.20% health = 13.78% (capped).
 - Employer: 13.72% social security + 4.80% health + accident 0.4–1.1% (capped).
   We use a representative office accident rate of 0.5% → 19.02% employer.

Sources: NRA / NSSI and Bulgaria's 2026 State Social Security Budget Act.
"""

NAME = "Bulgaria"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social security 13.72% + health 4.8% + office accident 0.5%, with split 2026 monthly caps"

MONTHLY_CAP_JAN_JUL = 2111.64
MONTHLY_CAP_AUG_DEC = 2300.00
EMPLOYEE_RATE = 0.1058 + 0.0320     # 13.78%
EMPLOYER_RATE = 0.1372 + 0.0480 + 0.005   # 19.02% (incl. representative 0.5% accident)
INCOME_TAX = 0.10


def compute(gross):
    """Return (employer_cost, net) in EUR, assuming 12 equal monthly pays."""
    monthly_gross = gross / 12
    base = (7 * min(monthly_gross, MONTHLY_CAP_JAN_JUL)
            + 5 * min(monthly_gross, MONTHLY_CAP_AUG_DEC))
    employee_contrib = base * EMPLOYEE_RATE
    taxable = gross - employee_contrib
    income_tax = taxable * INCOME_TAX

    net = gross - employee_contrib - income_tax
    employer_cost = gross + base * EMPLOYER_RATE
    return employer_cost, net
