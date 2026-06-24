"""Romania salary calculation — computed from published tax rates.

Rates are 2026 (single, no dependents, normal working conditions). Romania's
structure is unusual: a very HIGH employee burden but a very LOW employer cost,
because the 2018 reform moved almost all social contributions onto the employee
side (gross salaries were grossed up to compensate).
 - Employee: CAS (pension) 25% + CASS (health) 10% = 35% of gross (no salary cap).
 - Income tax: flat 10%, on (gross − employee contributions) → 6.5% of gross.
 - Employer: CAM (work insurance) 2.25% only; no employer pension/health/
   unemployment in normal conditions. So net is a flat 58.5% and employer cost
   just +2.25%.

The personal deduction and the 2026 minimum-wage relief apply only to LOW incomes
(around the minimum wage) and phase out well below this app's salary range, so they
are 0 here. Currency is RON, but with no RON-denominated threshold biting in range,
the calc is currency-invariant — computed directly in EUR. (Use "RON" if a
low-income point that triggers the personal deduction is ever added.)

Sources: PwC Romania 2026 (CAS 25% / CASS 10% / CAM 2.25% / flat 10% PIT).
"""

NAME = "Romania"
CURRENCY = "EUR"           # real currency RON — see note (calc is currency-invariant in range)
YEAR = 2026

EMPLOYEE_SS = 0.25 + 0.10   # CAS + CASS = 35%
INCOME_TAX = 0.10           # flat, on gross − contributions
EMPLOYER_CAM = 0.0225


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    employee = gross * EMPLOYEE_SS
    income_tax = (gross - employee) * INCOME_TAX   # base = gross − contributions
    net = gross - employee - income_tax            # = gross * 0.585
    employer_cost = gross * (1 + EMPLOYER_CAM)
    return employer_cost, net
