"""Slovenia salary calculation — computed from published tax rates.

Rates are 2026 (single, no children).
 - Employee: social security 22.10% + long-term care 1.00% = 23.10%, plus a flat
   compulsory health contribution (OZP) €39.36/mo.
 - Income tax: progressive 16/26/33/39/50% on (gross − 22.10% SS − general relief
   €5,551.93) → e.g. €41,188 base at €60k. Confirmed vs PwC/FURS that the SS IS
   deductible from the PIT base; the 1% long-term-care and the flat OZP come off
   net but not the PIT base. (Two EOR calculators land ~€30k net by NOT deducting
   SS from the PIT base — that over-taxes; the correct net is ~€35k.)
 - Employer: social security 16.10% + long-term care 1.00% = 17.10%.

Sources: PwC/FURS Slovenia 2026 (PIT base + brackets); taxravens/lano (SS, LTC, OZP).
"""
from engine import progressive

NAME = "Slovenia"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social security 16.10% + long-term care 1.0%"
INF = float("inf")

EE_SS = 0.2210                 # social security — deductible from the PIT base
EE_LTC = 0.01                  # long-term care — off net, not the PIT base
OZP = 39.36 * 12               # flat compulsory health contribution, €472.32/yr
ER_SS = 0.1610 + 0.01          # social security + long-term care = 17.10%
GENERAL_RELIEF = 5551.93
BRACKETS = [(9721.43, 0.16), (28592.44, 0.26), (57184.88, 0.33), (82346.23, 0.39), (INF, 0.50)]


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    ss = gross * EE_SS
    ltc = gross * EE_LTC
    tax_base = max(0.0, gross - ss - GENERAL_RELIEF)
    pit = progressive(tax_base, BRACKETS)

    net = gross - ss - ltc - OZP - pit
    employer_cost = gross * (1 + ER_SS)
    return employer_cost, net
