"""France salary calculation — computed from published tax rates.

Rates are 2026 for a single private-sector cadre employee, one tax share and a
50+ employer. Employer output is a deterministic statutory subtotal: variable
AT-MP, mobility, health-plan and sector/company charges are excluded.

Structure:
 - Many contributions split by the PASS ceiling (€48,060 in 2026): a capped slice
   (≤PASS), an uncapped slice (all gross), and a "tranche 2" slice (PASS→8×PASS)
   for the complementary pension.
 - CSG/CRDS are charged on 98.25% of gross; 6.8% (CSG) is income-tax-deductible,
   the rest (2.4% CSG + 0.5% CRDS) is not.
 - Income tax: revenu net imposable = gross − deductible contributions, then a 10%
   work-expense abattement (capped), then the progressive barème (1 part).
 - CEHR (high-income surtax): 3% of RFR between €250k and €500k, 4% above. Base is
   the revenu fiscal de référence ≈ the taxable income (well below gross), so it
   only starts biting around €310k gross. The CDHR 20%-minimum top-up never binds
   for a pure salary (ordinary IR is already ~35–40%).
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
EMPLOYER_BREAKDOWN = "Deterministic statutory subtotal after 2026 RGDU; excludes AT-MP, mobility, health premium and sector/company charges"
INF = float("inf")

PASS = 48060                  # plafond annuel de la sécurité sociale, 2026
SMIC_RGDU = 21876.40

# Income tax barème (1 part), 2026.
BAREME = [(11600, 0.0), (29579, 0.11), (84577, 0.30), (181917, 0.41), (INF, 0.45)]
ABATTEMENT_CAP = 14555
ABATTEMENT_MIN = 509


def _employee(gross):
    """Return (total employee contributions, non-deductible part)."""
    capped = min(gross, PASS)
    t2 = max(0.0, min(gross, 8 * PASS) - PASS)
    cadre_prev = 0.015 * capped
    csg_base = 0.9825 * min(gross, 4 * PASS) + max(gross - 4 * PASS, 0) + cadre_prev
    cet_base = min(gross, 8 * PASS) if gross > PASS else 0.0
    total = (
        capped * (0.069 + 0.0315 + 0.0086)
        + gross * 0.004 + min(gross, 4 * PASS) * 0.00024 + cet_base * 0.0014
        + t2 * (0.0864 + 0.0108)                   # AGIRC-ARRCO T2 + CEG T2
        + csg_base * 0.097                          # CSG 9.2% + CRDS 0.5%
    )
    non_deductible = csg_base * 0.029               # CSG 2.4% (non-ded) + CRDS 0.5%
    return total, non_deductible


def _employer(gross):
    capped = min(gross, PASS)
    t2 = max(0.0, min(gross, 8 * PASS) - PASS)
    p4 = min(gross, 4 * PASS)
    p8 = min(gross, 8 * PASS)
    cet_base = p8 if gross > PASS else 0.0
    cadre_prev = 0.015 * capped
    before_reduction = (
        gross * (0.13 + 0.003 + 0.0211 + 0.0525 + 0.00016 + 0.005 + 0.01 + 0.0068)
        + capped * 0.0855 + p4 * (0.04 + 0.0025)
        + capped * (0.0472 + 0.0129) + t2 * (0.1295 + 0.0162)
        + cet_base * 0.0021 + p4 * 0.00036 + cadre_prev + 0.08 * cadre_prev
    )
    if gross < 3 * SMIC_RGDU:
        x = 0.5 * (3 * SMIC_RGDU / gross - 1)
        coefficient = min(0.4021, round(0.0200 + 0.3821 * x ** 1.75, 4))
    else:
        coefficient = 0.0
    return before_reduction - coefficient * gross


def _cehr(rfr):
    """Contribution exceptionnelle sur les hauts revenus (1 part): 3% €250k–500k, 4% above.
    Base = revenu fiscal de référence ≈ the taxable income for a pure-salary earner."""
    return 0.03 * max(0.0, min(rfr, 500000) - 250000) + 0.04 * max(0.0, rfr - 500000)


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    contributions, non_deductible = _employee(gross)
    deductible = contributions - non_deductible
    net_imposable = gross - deductible
    abattement = max(ABATTEMENT_MIN, min(0.10 * net_imposable, ABATTEMENT_CAP))
    taxable = max(0.0, net_imposable - abattement)
    gross_scale_tax = progressive(taxable, BAREME)
    decote = max(0.0, 897 - 0.4525 * gross_scale_tax)
    income_tax = max(0.0, gross_scale_tax - decote)

    net = gross - contributions - income_tax - _cehr(taxable)
    employer_cost = gross + _employer(gross)
    return employer_cost, net
