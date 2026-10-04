"""Switzerland salary calculation — computed from published tax rates.

Rates are 2026 for a single age-35–44 employee in Zürich City. The benchmark uses
the equal-split minimum BVG old-age credit and zero variable accident/pension-risk
premiums. Income tax is official federal plus Zürich simple tax × 2.14 and CHF24.

Sources: PwC/ESTV 2026 (federal tariff, AHV/ALV rates); BVG 2026 coordinated-salary
limits (entry CHF 22,680, coordination CHF 25,725, upper CHF 88,200).
"""
from engine import progressive

NAME = "Switzerland"
CURRENCY = "CHF"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Zürich identifiable core: AHV 5.3% + capped ALV 1.1% + SVA FAK 1.025% + illustrative BVG 5%"
INF = float("inf")

AHV = 0.053
ALV = 0.011
ALV_CAP = 148200
FAK = 0.01025

BVG_ENTRY = 22680
BVG_COORD_DED = 26460
BVG_UPPER = 90720
BVG_MIN_COORD = 3780
BVG_RATE = 0.05                  # representative employee/employer share (age ~35-44)
ZH_BANDS = [(7000, 0.0), (12000, 0.02), (16800, 0.03), (24800, 0.04),
            (34500, 0.05), (45700, 0.06), (58800, 0.07), (76400, 0.08),
            (110400, 0.09), (144100, 0.10), (197400, 0.11),
            (266700, 0.12), (INF, 0.13)]


def _federal_tax(taxable):
    bands = [
        (15200, 33200, 0.0, 0.77), (33200, 43500, 138.60, 0.88),
        (43500, 58000, 229.20, 2.64), (58000, 76200, 612.00, 2.97),
        (76200, 82100, 1152.50, 5.94), (82100, 108900, 1502.95, 6.60),
        (108900, 141500, 3271.75, 8.80), (141500, 185100, 6140.55, 11.00),
        (185100, 793900, 10936.55, 13.20), (793900, INF, 91298.15, 11.50),
    ]
    if taxable <= 15200:
        return 0.0
    for lower, upper, anchor, per_hundred in bands:
        if taxable <= upper:
            tax = anchor + ((taxable - lower) / 100) * per_hundred
            tax = int(tax * 20 + 1e-9) / 20
            return 0.0 if tax < 25 else tax


def _bvg_coord(gross):
    if gross < BVG_ENTRY:
        return 0.0
    return max(BVG_MIN_COORD, min(gross, BVG_UPPER) - BVG_COORD_DED)


def compute(gross):
    """Return (employer_cost, net) in CHF; build_formula converts to EUR."""
    coord = _bvg_coord(gross)
    ee_social = AHV * gross + ALV * min(gross, ALV_CAP) + BVG_RATE * coord
    wage_certificate = gross - ee_social
    professional = min(4000, max(2000, 0.03 * wage_certificate))
    has_bvg = coord > 0
    zh_insurance = 2900 if has_bvg else 4350
    federal_insurance = 1800 if has_bvg else 2700
    zh_taxable = int(max(0.0, wage_certificate - professional - zh_insurance) // 100) * 100
    federal_taxable = int(max(0.0, wage_certificate - professional - federal_insurance) // 100) * 100
    zh_tax = progressive(zh_taxable, ZH_BANDS) * 2.14 + 24
    federal_tax = _federal_tax(federal_taxable)
    income_tax = zh_tax + federal_tax

    net = gross - ee_social - income_tax
    er_social = (AHV * gross + ALV * min(gross, ALV_CAP)
                 + FAK * gross + BVG_RATE * coord)
    employer_cost = gross + er_social
    return employer_cost, net
