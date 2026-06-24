"""Moldova salary calculation — computed from published tax rates.

Rates are 2026 (single). Currency MDL (FX path). Confirmed vs PwC / CNAS:
 - Employee: social security (CAS) 6% + health (CNAM) 9%, both deductible from the
   PIT base.
 - Income tax: flat 12% on (gross − employee contributions − personal allowance).
   The personal allowance (MDL 29,700) applies ONLY if annual income ≤ MDL 360,000
   (~€18k), so it is €0 across this app's salary range.
 - Employer: social security (CNAS) 24%; NO employer health.

The EOR calculators are wrong here: Deel/Skuad show +32% employer (a
special-conditions rate, not the standard one) and a higher net (omitting the 6%
employee CAS). PwC confirms the 6%+9% / 24% split above; net is ~74.8% of gross.

Sources: PwC Moldova 2026 (6% CAS / 9% CNAM / 24% employer; 12% PIT; MDL 29,700
allowance, capped at MDL 360,000 income).
"""

NAME = "Moldova"
CURRENCY = "MDL"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social security (CNAS) 24%"

EE_SSC = 0.06
EE_HEALTH = 0.09
ER_SSC = 0.24
ALLOWANCE = 29700          # personal exemption (annual)
ALLOWANCE_CAP = 360000     # allowance applies only if income <= this
PIT = 0.12


def compute(gross):
    """Return (employer_cost, net) in MDL; build_formula converts to EUR."""
    employee = gross * (EE_SSC + EE_HEALTH)
    allowance = ALLOWANCE if gross <= ALLOWANCE_CAP else 0.0
    taxable = max(0.0, gross - employee - allowance)
    pit = taxable * PIT

    net = gross - employee - pit
    employer_cost = gross * (1 + ER_SSC)
    return employer_cost, net
