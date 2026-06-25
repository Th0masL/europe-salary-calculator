"""Lithuania salary calculation — computed from published tax rates.

Rates are 2026 (single, no children). Like Romania, the 2019 reform shifted almost
all contributions onto the EMPLOYEE, leaving a very low employer cost.
 - Employee: Sodra/VSD 12.52% (capped at 60 VDU = €138,729/yr) + compulsory health
   (PSD) 6.98% (uncapped) = 19.5% below the ceiling.
 - Income tax (GPM): progressive 20% to 36 VDU (€83,237), 25% to 60 VDU (€138,729),
   32% above, on GROSS — Sodra/PSD are NOT deductible from the PIT base. (Confirmed
   by eBook/Deel/Skuad all landing on €36,300 at €60k.) The non-taxable amount (NPD)
   is ~€0 above ~€34k but ~€2.9k at €20k — not modelled, so net at €20–30k is
   slightly understated (~€0.6k).
 - Employer: Sodra 1.77% (permanent) + Guarantee Fund 0.16% + Long-term Employment
   Benefit Fund 0.16% + office accident ~0.4% ≈ 2.49% (cross-refs run a bit higher
   on the accident class).

The VSD ceiling (60 VDU = €138,729/yr, 2026: 60 × €2,312.15) is now modelled: above
it VSD stops but PSD continues, so high salaries keep more — the €300k+ employee
marginal is PSD 6.98% + 32% GPM, not the full 19.5%.

Sources: Rödl/Forvis Mazars Lithuania 2026 (brackets); Sodra 2026 (rates).
"""
from engine import progressive

NAME = "Lithuania"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Sodra 1.77% + Guarantee Fund 0.16% + Long-term Employment Fund 0.16% + accident ~0.4%"
INF = float("inf")

VSD = 0.1252                                 # Sodra social insurance — capped at 60 VDU
PSD = 0.0698                                 # compulsory health — uncapped
VSD_CAP = 138729                             # 60 VDU (2026: 60 × €2,312.15/mo)
ER_RATE = 0.0177 + 0.0016 + 0.0016 + 0.004   # Sodra + guarantee + long-term + accident ≈ 2.49%
BRACKETS = [(83237, 0.20), (138729, 0.25), (INF, 0.32)]   # 36 VDU / 60 VDU switch points


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    employee = VSD * min(gross, VSD_CAP) + PSD * gross   # VSD capped, PSD uncapped
    income_tax = progressive(gross, BRACKETS)            # GPM on GROSS; not deductible

    net = gross - employee - income_tax
    employer_cost = gross * (1 + ER_RATE)
    return employer_cost, net
