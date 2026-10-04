"""Moldova salary calculation — computed from published tax rates.

Rates are 2026 (single). Currency MDL (FX path). Confirmed from Moldovan primary
sources:
 - Employee: mandatory health insurance (AOAM) 9%, deductible from the PIT base.
   Ordinary employees do not pay a separate BASS contribution.
 - Income tax: flat 12% on (gross − AOAM − personal exemption). The MDL 29,700
   exemption is lost when pre-exemption taxable income is at least MDL 360,000.
 - Employer: social security (CNAS) 24%; NO employer health.

Sources: Moldova Ministry of Finance, CNAM, CNAS, and 2026 tax legislation.
"""

NAME = "Moldova"
CURRENCY = "MDL"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social security (CNAS) 24%"

EE_HEALTH = 0.09
ER_SSC = 0.24
ALLOWANCE = 29700          # personal exemption (annual)
ALLOWANCE_CAP = 360000     # lost when pre-exemption taxable income reaches this
PIT = 0.12


def compute(gross):
    """Return (employer_cost, net) in MDL; build_formula converts to EUR."""
    health = gross * EE_HEALTH
    pre_exemption_taxable = gross - health
    allowance = ALLOWANCE if pre_exemption_taxable < ALLOWANCE_CAP else 0.0
    taxable = max(0.0, pre_exemption_taxable - allowance)
    pit = taxable * PIT

    net = gross - health - pit
    employer_cost = gross * (1 + ER_SSC)
    return employer_cost, net
