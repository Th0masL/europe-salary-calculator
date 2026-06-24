"""Slovakia salary calculation — computed from published tax rates.

Rates are 2026 (single, no children). The 2026 consolidation package made it more
progressive and pricier: PIT went to four brackets (19/25/30/35%), employee health
rose to 5%, and the social-insurance cap is €16,764/month (€201,168/yr).

 - Employee: social insurance 9.4% (capped at €201,168/yr) + health 5% (uncapped).
 - Income tax: progressive on (gross − contributions). The personal allowance
   phases out with income and is €0 well below this app's salary range, so it's
   omitted here.
 - Employer: social 24.4% (capped €201,168) + health 11% + accident 0.8% (the last
   two uncapped) ≈ 36.2%.

Sources: PwC Slovakia 2026; Forvis Mazars 2026 CEE tax guide (brackets, rates, cap).
"""
from engine import progressive

NAME = "Slovakia"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social insurance 24.4% (capped €201,168) + health 11% + accident 0.8%"
INF = float("inf")

SOCIAL_CAP = 16764 * 12             # €201,168/yr max assessment base
EE_SOCIAL = 0.094                   # capped
EE_HEALTH = 0.05                    # uncapped
ER_SOCIAL = 0.244                   # capped
ER_HEALTH_ACCIDENT = 0.11 + 0.008   # health + accident, uncapped

BRACKETS = [(43983.32, 0.19), (60349.21, 0.25), (75010.32, 0.30), (INF, 0.35)]


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    social = min(gross, SOCIAL_CAP) * EE_SOCIAL
    health = gross * EE_HEALTH
    taxable = max(0.0, gross - social - health)    # personal allowance is €0 in range
    income_tax = progressive(taxable, BRACKETS)

    net = gross - social - health - income_tax
    employer_cost = gross + min(gross, SOCIAL_CAP) * ER_SOCIAL + gross * ER_HEALTH_ACCIDENT
    return employer_cost, net
