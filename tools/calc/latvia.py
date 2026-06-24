"""Latvia salary calculation — computed from published tax rates.

Rates are 2026 (single, no children).
 - Employee: NSIC (VSAOI) 10.50%, capped at €105,300/yr.
 - Income tax (IIN): 25.5% up to €105,300, 33% above, +3% over €200,000, on
   (gross − employee NSIC). NSIC IS deductible from the PIT base here (unlike
   Lithuania). The non-taxable minimum tapers to €0 above €3,600/mo, so it's €0 in
   this app's salary range.
 - Employer: NSIC 23.59%, capped at €105,300/yr.
 - Above the €105,300 cap a solidarity-tax mechanism replaces NSIC (only bites
   above the cap — i.e. €150k slightly).

Sources: VID 2026 (PIT rates); PwC/KPMG Latvia 2026 (NSIC split, €105,300 cap).
"""
from engine import progressive

NAME = "Latvia"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Social insurance (NSIC) 23.59% (capped €105,300)"
INF = float("inf")

NSIC_CAP = 105300
EE_NSIC = 0.105
ER_NSIC = 0.2359
PIT_BRACKETS = [(105300, 0.255), (200000, 0.33), (INF, 0.36)]   # 33% + extra 3% over 200k


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    ee_nsic = min(gross, NSIC_CAP) * EE_NSIC
    taxable = max(0.0, gross - ee_nsic)        # NPM is €0 in range
    pit = progressive(taxable, PIT_BRACKETS)

    net = gross - ee_nsic - pit
    employer_cost = gross + min(gross, NSIC_CAP) * ER_NSIC
    return employer_cost, net
