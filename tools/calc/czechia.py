"""Czech Republic salary calculation — computed from published tax rates.

Rates are 2026 (single, no children). Currency CZK (FX path).
 - Employee: social security 7.1% (capped at CZK 2,350,416/yr) + health 4.5%
   (uncapped) = 11.6%.
 - Income tax: 15% up to CZK 1,762,812, 23% above — on GROSS. The "super-gross"
   base was abolished in 2021, so employee contributions are NOT deductible from
   the PIT base. Minus the basic taxpayer credit (sleva na poplatníka, ~CZK
   30,840/yr).
 - Employer: social security 24.8% (capped) + health 9.0% (uncapped) = 33.8%.

Sources: PwC/KPMG Czech 2026 (rates, CZK 2,350,416 cap, CZK 1,762,812 23% threshold).
"""
import math

from engine import progressive

NAME = "Czech Republic"
CURRENCY = "CZK"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Statutory floor: social 24.8% (capped) + health 9%; mandatory activity-rated accident premium excluded"
INF = float("inf")

SOCIAL_CAP = 2350416
EE_SOCIAL = 0.071           # capped
EE_HEALTH = 0.045           # uncapped
ER_SOCIAL = 0.248           # capped
ER_HEALTH = 0.09            # uncapped
BASIC_CREDIT = 30840        # sleva na poplatníka
PIT_BRACKETS = [(1762812, 0.15), (INF, 0.23)]


def compute(gross):
    """Return the final annual cash and employer floor for 12 regular pays."""
    regular = math.floor(gross / 12)
    payments = [regular] * 11 + [gross - 11 * regular]
    remaining_social_base = SOCIAL_CAP
    ee_social = er_social = ee_health = 0.0
    for payment in payments:
        social_base = min(payment, remaining_social_base)
        remaining_social_base -= social_base
        ee_social += math.ceil(EE_SOCIAL * social_base)
        er_social += math.ceil(ER_SOCIAL * social_base)
        ee_health += math.ceil(EE_HEALTH * payment)

    pit = max(0.0, math.ceil(progressive(gross, PIT_BRACKETS)) - BASIC_CREDIT)
    net = gross - ee_social - ee_health - pit
    employer_cost = gross + er_social + gross * ER_HEALTH
    return employer_cost, net
