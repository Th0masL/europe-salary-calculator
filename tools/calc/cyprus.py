"""Cyprus salary calculation — computed from published tax rates.

Rates are 2026 (single private-sector employee, no special regime).

Two things shape the numbers:
 - Social Insurance (plus the Redundancy + Human Resource Development funds) is
   capped at the insurable-earnings ceiling — €68,904/yr in 2026 — so above that
   it stops growing. GESY is capped much higher (€180,000). The Social Cohesion
   Fund (2%) is the one with NO cap: it's charged on total earnings.
 - Income tax is on chargeable income = gross − employee SI − employee GESY (both
   are deductible). The €22,000 tax-free amount is the 0% band of the brackets,
   not a separate allowance on top.

Employer side (confirmed vs KPMG / PwC / tsielepis 2026 tax alerts):
SI 8.8% + Redundancy 1.2% + HRDF 0.5% + Social Cohesion 2.0% + GESY 2.9% = 15.4%.
The initial research had Redundancy at 2.0% and omitted the HRDF; verification
corrected both. SI/Redundancy/HRDF are capped at €68,904, Social Cohesion is
uncapped, GESY is capped at €180,000.

Sources: Cyprus Ministry of Finance Tax Tools (2026 brackets); KPMG / PwC /
tsielepis 2026 tax alerts (rates, €68,904 insurable-earnings ceiling, GESY caps).
"""
from engine import progressive

NAME = "Cyprus"
CURRENCY = "EUR"
YEAR = 2026
INF = float("inf")

# Ceilings: insurable earnings (SI / Redundancy / HRDF) and the higher GESY cap.
SI_CEILING = 68904
GESY_CAP = 180000

# Employee, deducted from gross.
EMPLOYEE_SI = 0.088          # Social Insurance      — capped at SI_CEILING
EMPLOYEE_GESY = 0.0265       # GESY (health)         — capped at GESY_CAP

# Employer, on top of gross.
EMPLOYER_CAPPED = 0.088 + 0.012 + 0.005   # SI 8.8 + Redundancy 1.2 + HRDF 0.5, capped at SI_CEILING
EMPLOYER_COHESION = 0.020                 # Social Cohesion Fund — NO cap (total earnings)
EMPLOYER_GESY = 0.029                     # GESY (health) — capped at GESY_CAP

# Income tax on chargeable income (progressive); €22,000 is the 0% band.
TAX_BRACKETS = [(22000, 0.0), (32000, 0.20), (42000, 0.25), (72000, 0.30), (INF, 0.35)]


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    employee_si = min(gross, SI_CEILING) * EMPLOYEE_SI
    employee_gesy = min(gross, GESY_CAP) * EMPLOYEE_GESY

    taxable = max(0.0, gross - employee_si - employee_gesy)
    income_tax = progressive(taxable, TAX_BRACKETS)
    net = gross - employee_si - employee_gesy - income_tax

    employer_cost = (
        gross
        + min(gross, SI_CEILING) * EMPLOYER_CAPPED
        + gross * EMPLOYER_COHESION
        + min(gross, GESY_CAP) * EMPLOYER_GESY
    )
    return employer_cost, net
