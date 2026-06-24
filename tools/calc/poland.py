"""Poland salary calculation — computed from published tax rates.

Rates are 2026 (single, no children, standard employment contract). Currency PLN
— this is the FIRST module to use the FX path: build_formula.py converts the EUR
salary point to PLN, computes here, then converts the result back, so the
PLN-denominated caps and thresholds apply correctly.

Structure:
 - Employee ZUS 13.71%: pension 9.76% + disability 1.5% (capped at PLN 282,600/yr)
   + sickness 2.45% (uncapped).
 - Health 9% on (gross − ZUS social). Since the 2022 "Polski Ład" reform this is
   NOT deductible from PIT — a real hit to net.
 - PIT progressive 12% / 32% over PLN 120,000, on (gross − ZUS social − KUP). The
   PLN 30,000 tax-free amount is delivered as a PLN 3,600 annual tax reduction;
   KUP (koszty uzyskania) = PLN 3,000/yr standard.
 - Employer ~20.48%: pension 9.76% + disability 6.5% (capped) + accident 1.67% +
   Labour Fund 2.45% + FGŚP 0.1% (uncapped). Accident rate is sector-dependent.

Note: €60k is a high salary in Poland (well into the 32% band), so the take-home %
is lower than the flat-tax neighbours.

Sources: PwC Poland 2026; ZUS (rates + PLN 282,600 cap); Ministry of Finance (PIT).
"""

NAME = "Poland"
CURRENCY = "PLN"
YEAR = 2026

ZUS_CAP = 282600             # pension + disability annual ceiling
PIT_THRESHOLD = 120000
TAX_REDUCTION = 3600         # = 12% × 30,000 tax-free amount
KUP = 3000                   # koszty uzyskania przychodu (standard)

# employee
EE_PENS_DIS = 0.0976 + 0.015        # capped at ZUS_CAP
EE_SICKNESS = 0.0245                # uncapped
HEALTH = 0.09                       # on (gross − ZUS social); NOT PIT-deductible

# employer
ER_PENS_DIS = 0.0976 + 0.065        # capped at ZUS_CAP
ER_OTHER = 0.0167 + 0.0245 + 0.001  # accident + Labour Fund + FGŚP, uncapped


def compute(gross):
    """Return (employer_cost, net) in PLN; build_formula converts to EUR."""
    capped = min(gross, ZUS_CAP)
    zus_social = capped * EE_PENS_DIS + gross * EE_SICKNESS
    health = (gross - zus_social) * HEALTH

    taxable = max(0.0, gross - zus_social - KUP)
    if taxable <= PIT_THRESHOLD:
        pit = max(0.0, taxable * 0.12 - TAX_REDUCTION)
    else:
        pit = (PIT_THRESHOLD * 0.12 - TAX_REDUCTION) + (taxable - PIT_THRESHOLD) * 0.32

    net = gross - zus_social - health - pit
    employer_cost = gross + capped * ER_PENS_DIS + gross * ER_OTHER
    return employer_cost, net
