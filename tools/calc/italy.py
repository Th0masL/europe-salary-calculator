"""Italy salary calculation — computed from published tax rates.

Rates are 2026 (single, no children). Italy is high-contribution + progressive.
 - Employee: INPS ~9.19% (capped at the €122,295 pensionable ceiling) + an extra
   1% above the first pensionable band (~€56k).
 - IRPEF: 23% to €28k, 33% to €50k, 43% above, on (gross − INPS). Plus regional
   (~1.7%) and municipal (~0.5%) surtaxes (both vary by location — averages used).
   The employment tax credit (detrazione) and "cuneo fiscale" relief phase out by
   ~€50k, so they're €0 in this app's salary range.
 - Employer: INPS ~29.72% (capped) + TFR severance accrual ~6.91% + INAIL ~1% +
   a ~5% bucket for the near-universal 13th month / CCNL & sectoral variation
   ≈ 42.6%, which lands near the credible cross-refs (Rippling +43%, eBook/Skuad
   +47%; Deel +71% is an outlier).

*** Italy is the most variable / approximate module. The regional + municipal
surtaxes (we use ~3%) range from ~1% to >4% by location, and the employer cost
swings with the CCNL and whether the 13th/14th month is on top of the entered
gross. Treat both as representative, not exact. ***

Sources: Agenzia delle Entrate 2026 IRPEF; INPS 2026 (rates, €122,295 ceiling).
"""
from engine import progressive

NAME = "Italy"
CURRENCY = "EUR"
YEAR = 2026
INF = float("inf")

INPS_CAP = 122295
FIRST_BAND = 56000          # approx first pensionable band for the +1%
EE_INPS = 0.0919
EE_ADDITIONAL = 0.01
ER_INPS = 0.2972
ER_TFR = 0.0691
ER_INAIL = 0.01
ER_EXTRAS = 0.05            # near-universal 13th month + CCNL/sectoral variation (representative)
IRPEF = [(28000, 0.23), (50000, 0.33), (INF, 0.43)]
REGIONAL = 0.022
MUNICIPAL = 0.008


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    capped = min(gross, INPS_CAP)
    ee_inps = capped * EE_INPS + max(0.0, capped - FIRST_BAND) * EE_ADDITIONAL

    taxable = max(0.0, gross - ee_inps)
    irpef = progressive(taxable, IRPEF)
    surtax = (REGIONAL + MUNICIPAL) * taxable

    net = gross - ee_inps - irpef - surtax
    employer_cost = gross + capped * ER_INPS + gross * (ER_TFR + ER_INAIL + ER_EXTRAS)
    return employer_cost, net
