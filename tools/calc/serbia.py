"""Serbia salary calculation — computed from published tax rates.

Rates are 2026 (single). Currency RSD (FX path).
 - Employee social contributions: 14% pension (PIO) + 5.15% health + 0.75%
   unemployment = 19.9%, on a base capped at the monthly maximum.
 - Salary tax (PIT): flat 10% on (gross − non-taxable allowance RSD 34,221/month).
   Contributions are NOT deducted from the PIT base.
 - Employer social contributions: 10% pension (PIO) + 5.15% health = 15.15% (the
   employer PIO rate was cut to 10% in 2023; the 16.65% figure uses the old 11.5%),
   same capped base.

The high-earner annual supplementary tax (10% above 3× the average annual wage) is
a separate annual filing, excluded here (as the EOR calcs also do).

Sources: PwC Serbia 2026 (10% PIT, RSD 34,221 allowance); relocationserbia 2026
payroll (19.9% employee / 10%+5.15% employer split).
"""

NAME = "Serbia"
CURRENCY = "RSD"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Pension (PIO) 10% + health 5.15% (capped at the monthly max base)"

EE_RATE = 0.199
ER_RATE = 0.1515
PIT_RATE = 0.10
ALLOWANCE = 34221 * 12          # non-taxable salary amount (annual)
MAX_BASE = 700000 * 12          # monthly max contribution base ~RSD 700k (2026 est)


def compute(gross):
    """Return (employer_cost, net) in RSD; build_formula converts to EUR."""
    base = min(gross, MAX_BASE)
    employee = EE_RATE * base
    pit = PIT_RATE * max(0.0, gross - ALLOWANCE)

    net = gross - employee - pit
    employer_cost = gross + ER_RATE * base
    return employer_cost, net
