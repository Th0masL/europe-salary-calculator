"""Serbia salary calculation — computed from published tax rates.

Rates are 2026 for the age-40, single, no-child profile. Currency RSD (FX path).
 - Employee social contributions: 14% pension (PIO) + 5.15% health + 0.75%
   unemployment = 19.9%, on a base capped at the monthly maximum.
 - Salary tax (PIT): flat 10% on (gross − non-taxable allowance RSD 34,221/month).
   Contributions are NOT deducted from the PIT base.
 - Employer social contributions: 10% pension (PIO) + 5.15% health = 15.15% (the
   employer PIO rate was cut to 10% in 2023; the 16.65% figure uses the old 11.5%),
   same capped base.

The high-earner supplementary annual tax is excluded until the official full-year
2026 average salary is published. Results are explicitly ordinary payroll before
that later assessment; age 40 receives no under-40 additional deduction.

Sources: PwC Serbia 2026 (10% PIT, RSD 34,221 allowance); relocationserbia 2026
payroll (19.9% employee / 10%+5.15% employer split).
"""

NAME = "Serbia"
CURRENCY = "RSD"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Ordinary payroll before annual tax: PIO 10% + health 5.15%, capped at official 2026 monthly maximum"

EE_RATE = 0.199
ER_RATE = 0.1515
PIT_RATE = 0.10
ALLOWANCE = 34221 * 12          # non-taxable salary amount (annual)
MIN_BASE = 51297 * 12
MAX_BASE = 732820 * 12


def compute(gross):
    """Return (employer_cost, net) in RSD; build_formula converts to EUR."""
    base = min(max(gross, MIN_BASE), MAX_BASE)
    employee = EE_RATE * base
    pit = PIT_RATE * max(0.0, gross - ALLOWANCE)

    net = gross - employee - pit
    employer_cost = gross + ER_RATE * base
    return employer_cost, net
