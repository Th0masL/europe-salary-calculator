"""Luxembourg salary calculation — computed from published tax rates.

Rates are 2026 (single, tax class 1, no children).

The income-tax scale below is the official PwC/ACD 2026 class-1 scale — a granular
23-band progression rising 8%→39% in ~1% steps, then 40/41/42%. (The first research
pass gave a broken 12%→42% table; this is the verified one. A scaled reconstruction
of the 2024 bands had landed within ~0.1% of these boundaries.)

Social contributions (cap 5×SSM = €162,224/yr — doesn't bite below €150k):
 - Employee: pension 8.5% + health 3.05% (both income-tax deductible) + dependency
   1.40% on (gross − ~€8,112 abatement) (NOT tax-deductible). No employee
   unemployment contribution. (Pension is 8.5%, not 8% — confirmed by the sources;
   an earlier draft here wrongly "corrected" it to 8%.)
 - Employer: pension 8.5% + health 3.05% + mutualité (MDE) + accident ≈ 13%
   (MDE/accident are class/insurer-dependent; tuned to the eBook/Rippling cluster).

Income tax: scale on (gross − pension − health − €540 frais); 7% employment-fund
surcharge on the tax; then the crédit d'impôt salarié (CIS) credited — €600 up to
€40k gross, tapering to €0 by €80k (so €300 at €60k, €0 at €100k+).

Sources: PwC Luxembourg 2026 (class-1 scale); ACD CIS 2026; FEDIL/PwC 2026 social
parameters (rates, €162,224 cap).
"""
from engine import progressive

NAME = "Luxembourg"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Pension 8.5% + health 3.05% + mutualite/accident ~1.5%"
INF = float("inf")

EE_PENS_HEALTH = 0.085 + 0.0305     # deductible
EE_DEPENDENCY = 0.014               # on (gross − abatement), not deductible
DEPENDENCY_ABATEMENT = 8112         # ≈ 1/4 of SSM × 12
ER_RATE = 0.085 + 0.0305 + 0.015    # pension + health + MDE/accident ≈ 13%
FRAIS = 540                         # frais d'obtention (min)
SOLIDARITY = 0.07                   # employment-fund surcharge on the tax

# Official 2026 class-1 scale (upper bound, marginal rate).
SCALE = [
    (13230, 0.0), (15435, 0.08), (17640, 0.09), (19845, 0.10), (22050, 0.11),
    (24255, 0.12), (26550, 0.14), (28845, 0.16), (31140, 0.18), (33435, 0.20),
    (35730, 0.22), (38025, 0.24), (40320, 0.26), (42615, 0.28), (44910, 0.30),
    (47205, 0.32), (49500, 0.34), (51795, 0.36), (54090, 0.38), (117450, 0.39),
    (176160, 0.40), (234870, 0.41), (INF, 0.42),
]


def _cis(gross):
    """Crédit d'impôt salarié, 2026 (function of gross salary)."""
    if gross < 936:
        return 0.0
    if gross <= 11265:
        return 300 + (gross - 936) * 0.029
    if gross <= 40000:
        return 600.0
    if gross < 80000:
        return 600 - (gross - 40000) * 0.015
    return 0.0


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    pens_health = gross * EE_PENS_HEALTH
    dependency = max(0.0, gross - DEPENDENCY_ABATEMENT) * EE_DEPENDENCY

    taxable = max(0.0, gross - pens_health - FRAIS)
    income_tax = progressive(taxable, SCALE)
    total_tax = max(0.0, income_tax * (1 + SOLIDARITY) - _cis(gross))

    net = gross - pens_health - dependency - total_tax
    employer_cost = gross * (1 + ER_RATE)
    return employer_cost, net
