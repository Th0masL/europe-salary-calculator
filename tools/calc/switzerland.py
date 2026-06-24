"""Switzerland salary calculation — computed from published tax rates.

Rates are 2026 (single). Currency CHF (FX path). ANCHORED ON ZÜRICH CITY: Swiss
income tax is federal + cantonal + communal, and the cantonal/communal part varies
2–3× by location (Zug low, Geneva/Vaud high), so net is canton-specific — this is a
representative Zürich estimate, not a single nationwide truth.
 - Employee social: AHV/IV/EO 5.3% (no cap) + ALV 1.1% (to CHF 148,200, then +0.5%
   to CHF 315,000) + BVG/LPP pillar-2 pension on the coordinated salary (age-banded;
   ~5% employee representative) + non-occupational accident ~1%.
 - Income tax: progressive federal (max 11.5%) + Zürich cantonal + communal,
   effective on taxable income (gross − employee social − standard deductions).
 - Employer: mirrors AHV + ALV + BVG, plus occupational accident & family-allowance
   fund (~1.5% representative).

Tax table and BVG share are calibrated against the EOR cross-refs.

Sources: PwC/ESTV 2026 (federal tariff, AHV/ALV rates); BVG 2026 coordinated-salary
limits (entry CHF 22,680, coordination CHF 25,725, upper CHF 88,200).
"""
from engine import progressive

NAME = "Switzerland"
CURRENCY = "CHF"
YEAR = 2026
EMPLOYER_BREAKDOWN = "AHV/IV/EO 5.3% + ALV 1.1% + BVG pension (age-banded) + accident & family-allowance funds"
INF = float("inf")

AHV = 0.053
ALV1, ALV2 = 0.011, 0.005
ALV_CAP1, ALV_CAP2 = 148200, 315000
NBU = 0.01                       # non-occupational accident (employee)
ER_EXTRA = 0.045                 # employer occupational accident + family-allowance
                                 # fund + pension premium (calibrated to eBook/Deel)

BVG_ENTRY = 22680
BVG_COORD_DED = 25725
BVG_UPPER = 88200
BVG_MIN_COORD = 3675
BVG_RATE = 0.05                  # representative employee/employer share (age ~35-44)

DEDUCTIONS = 6000                # standard professional/insurance deductions
TAX = [(15000, 0.0), (30000, 0.08), (50000, 0.12), (80000, 0.17),
       (120000, 0.22), (180000, 0.27), (INF, 0.30)]


def _alv(salary):
    return ALV1 * min(salary, ALV_CAP1) + ALV2 * max(0.0, min(salary, ALV_CAP2) - ALV_CAP1)


def _bvg_coord(gross):
    if gross < BVG_ENTRY:
        return 0.0
    return max(BVG_MIN_COORD, min(gross, BVG_UPPER) - BVG_COORD_DED)


def compute(gross):
    """Return (employer_cost, net) in CHF; build_formula converts to EUR."""
    coord = _bvg_coord(gross)
    ee_social = AHV * gross + _alv(gross) + NBU * gross + BVG_RATE * coord
    taxable = max(0.0, gross - ee_social - DEDUCTIONS)
    income_tax = progressive(taxable, TAX)

    net = gross - ee_social - income_tax
    er_social = AHV * gross + _alv(gross) + BVG_RATE * coord + ER_EXTRA * gross
    employer_cost = gross + er_social
    return employer_cost, net
