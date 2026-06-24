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
from engine import progressive

NAME = "Czech Republic"
CURRENCY = "CZK"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social security 24.8% (capped) + health insurance 9.0%"
INF = float("inf")

SOCIAL_CAP = 2350416
EE_SOCIAL = 0.071           # capped
EE_HEALTH = 0.045           # uncapped
ER_SOCIAL = 0.248           # capped
ER_HEALTH = 0.09            # uncapped
BASIC_CREDIT = 30840        # sleva na poplatníka
PIT_BRACKETS = [(1762812, 0.15), (INF, 0.23)]


def compute(gross):
    """Return (employer_cost, net) in CZK; build_formula converts to EUR."""
    ee_social = min(gross, SOCIAL_CAP) * EE_SOCIAL
    ee_health = gross * EE_HEALTH

    pit = max(0.0, progressive(gross, PIT_BRACKETS) - BASIC_CREDIT)   # PIT on gross

    net = gross - ee_social - ee_health - pit
    employer_cost = gross + min(gross, SOCIAL_CAP) * ER_SOCIAL + gross * ER_HEALTH
    return employer_cost, net
