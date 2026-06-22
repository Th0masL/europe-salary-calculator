"""France salary calculation — computed from published tax rates.

Rates are 2026 (single private-sector CADRE employee, 1 part, mainland, large
employer). *** Most complex / most approximate module. ***
The research data was incomplete (it omitted the AGIRC-ARRCO complementary
pension, the CSG/CRDS rates, and the employer health/family thresholds), so this
is RECONSTRUCTED from standard French payroll rates — a representative case to be
sanity-checked against the cross-refs and confirmed by verification, not a precise
transcription.

Structure:
 - Many contributions split by the PASS ceiling (€48,060 in 2026): a capped slice
   (≤PASS), an uncapped slice (all gross), and a "tranche 2" slice (PASS→8×PASS)
   for the complementary pension.
 - CSG/CRDS are charged on 98.25% of gross; 6.8% (CSG) is income-tax-deductible,
   the rest (2.4% CSG + 0.5% CRDS) is not.
 - Income tax: revenu net imposable = gross − deductible contributions, then a 10%
   work-expense abattement (capped), then the progressive barème (1 part).
 - Employer health (7%→13%) and family allowances (3.45%→5.25%) step up with
   salary (SMIC-based thresholds). No "réduction générale" at these salaries (it
   phases out by ~1.6×SMIC). Work-accident (AT) is at a representative 2%.

Confirmed vs Cleiss / PwC (2026): the core employer rates, the ~20.8% employee
total, the PASS (€48,060), and the income-tax base above. The statutory core is
~42% of gross — but the REALISTIC total employer cost for a cadre is higher once
mandatory-in-practice extras are added (employer mutuelle + cadre prévoyance,
versement mobilité, CSE / médecine du travail). We add a representative ~8% layer
for a large Île-de-France employer (EMPLOYER_EXTRAS), landing ~€90k at €60k gross
— in line with the verified planning range (€91–98k) and the cross-refs. That
extras layer is the main remaining variability: a smaller or non-IdF employer pays
less, so treat the France employer cost as representative, not exact.

Sources: Cleiss / Urssaf 2026 rates; service-public 2026 barème; PASS €48,060;
PwC France (employee share).
"""
from engine import progressive

NAME = "France"
CURRENCY = "EUR"
YEAR = 2026
INF = float("inf")

PASS = 48060                  # plafond annuel de la sécurité sociale, 2026
SMIC = 21840                  # approx annual gross SMIC, for employer thresholds

# Income tax barème (1 part), 2026.
BAREME = [(11600, 0.0), (29579, 0.11), (84577, 0.30), (181917, 0.41), (INF, 0.45)]
ABATTEMENT_CAP = 14171        # 10% frais-pro deduction is capped

# Representative mandatory-extras layer, large Île-de-France employer: mutuelle
# (~1.5%) + cadre prévoyance (~2%) + versement mobilité (~3.2%) + CSE / médecine
# du travail (~1.3%) ≈ 8% of gross. Highly variable — smaller / non-IdF is less.
EMPLOYER_EXTRAS = 0.08


def _employee(gross):
    """Return (total employee contributions, non-deductible part)."""
    capped = min(gross, PASS)
    t2 = max(0.0, min(gross, 8 * PASS) - PASS)
    csg_base = 0.9825 * gross
    above_pass = 0.0014 if gross > PASS else 0.0   # CET only above the PASS
    total = (
        capped * (0.069 + 0.0315 + 0.0086)         # vieillesse plaf + AGIRC-ARRCO T1 + CEG T1
        + gross * (0.004 + 0.00024 + above_pass)   # vieillesse déplaf + APEC + CET
        + t2 * (0.0864 + 0.0108)                   # AGIRC-ARRCO T2 + CEG T2
        + csg_base * 0.097                          # CSG 9.2% + CRDS 0.5%
    )
    non_deductible = csg_base * 0.029               # CSG 2.4% (non-ded) + CRDS 0.5%
    return total, non_deductible


def _employer(gross):
    capped = min(gross, PASS)
    t2 = max(0.0, min(gross, 8 * PASS) - PASS)
    chomage_base = min(gross, 4 * PASS)
    maladie = 0.13 if gross > 2.5 * SMIC else 0.07
    famille = 0.0525 if gross > 3.5 * SMIC else 0.0345
    above_pass = 0.0021 if gross > PASS else 0.0    # CET (employer) only above PASS
    return (
        capped * (0.0855 + 0.0472 + 0.0129 + 0.005)             # vieillesse plaf + AGIRC T1 + CEG T1 + FNAL
        + gross * (maladie + famille + 0.0202 + 0.003 + 0.02    # +vieillesse déplaf +CSA +AT(repr.)
                   + 0.00016 + 0.01 + 0.0068 + 0.00036 + above_pass)  # +dialogue +formation +apprentissage +APEC +CET
        + t2 * (0.1295 + 0.0162)                                 # AGIRC T2 + CEG T2
        + chomage_base * (0.0405 + 0.0025)                       # chômage + AGS
    )


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    contributions, non_deductible = _employee(gross)
    deductible = contributions - non_deductible
    net_imposable = gross - deductible
    abattement = min(0.10 * net_imposable, ABATTEMENT_CAP)
    income_tax = progressive(max(0.0, net_imposable - abattement), BAREME)

    net = gross - contributions - income_tax
    employer_cost = gross + _employer(gross) + gross * EMPLOYER_EXTRAS
    return employer_cost, net
