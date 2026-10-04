"""Slovakia salary calculation — computed from published tax rates.

Rates are 2026 (single, no children). The 2026 consolidation package made it more
progressive and pricier: PIT went to four brackets (19/25/30/35%), employee health
rose to 5%, and the social-insurance cap is €16,764/month (€201,168/yr).

 - Employee: social insurance 9.4% (capped at €201,168/yr) + health 5% (uncapped).
 - Income tax: progressive on (gross − contributions − the income-dependent
   taxpayer allowance). The allowance is €5,966.73 at lower bases and phases to
   zero at a pre-allowance base of about €43,983.33.
 - Employer: social 24.4% (capped €201,168) + health 11% + accident 0.8% (the last
   two uncapped) ≈ 36.2%.

Sources: PwC Slovakia 2026; Forvis Mazars 2026 CEE tax guide (brackets, rates, cap).
"""
import math

from engine import progressive

NAME = "Slovakia"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social insurance 24.4% (capped €201,168) + health 11% + accident 0.8%"
INF = float("inf")

SOCIAL_CAP = 16764 * 12             # €201,168/yr max assessment base
EE_SOCIAL_RATES = (0.014, 0.04, 0.03, 0.01)
EE_HEALTH = 0.05                    # uncapped
ER_SOCIAL_RATES = (0.014, 0.14, 0.03, 0.01, 0.0025, 0.0475)
ER_HEALTH = 0.11
ER_ACCIDENT = 0.008

BRACKETS = [(43983.32, 0.19), (60349.21, 0.25), (75010.32, 0.30), (INF, 0.35)]
FULL_ALLOWANCE = 5966.73
ALLOWANCE_FULL_TO = 26083.13
ALLOWANCE_PHASEOUT_CONSTANT = 14661.11


def floor_cent(amount):
    return math.floor((amount + 1e-9) * 100) / 100


def compute(gross):
    """Return annual reconciled amounts for 12 equal monthly pays, in EUR."""
    monthly_gross = gross / 12
    monthly_social_base = min(monthly_gross, SOCIAL_CAP / 12)
    social = 12 * sum(floor_cent(monthly_social_base * rate)
                      for rate in EE_SOCIAL_RATES)
    health = 12 * floor_cent(monthly_gross * EE_HEALTH)
    base_before_allowance = max(0.0, gross - social - health)
    if base_before_allowance <= ALLOWANCE_FULL_TO:
        allowance = FULL_ALLOWANCE
    else:
        allowance = max(0.0, ALLOWANCE_PHASEOUT_CONSTANT - base_before_allowance / 3)
    taxable = max(0.0, base_before_allowance - allowance)
    income_tax = floor_cent(progressive(taxable, BRACKETS))

    net = gross - social - health - income_tax
    employer_social = 12 * sum(floor_cent(monthly_social_base * rate)
                               for rate in ER_SOCIAL_RATES)
    employer_health = 12 * floor_cent(monthly_gross * ER_HEALTH)
    employer_accident = 12 * floor_cent(monthly_gross * ER_ACCIDENT)
    employer_cost = gross + employer_social + employer_health + employer_accident
    return employer_cost, net
