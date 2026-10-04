"""Lithuania salary calculation — computed from published tax rates.

Rates are 2026 (single, no children). Like Romania, the 2019 reform shifted almost
all contributions onto the EMPLOYEE, leaving a very low employer cost.
 - Employee: Sodra/VSD 12.52% (capped at 60 VDU = €138,729/yr) + compulsory health
   (PSD) 6.98% (uncapped) = 19.5% below the ceiling.
 - Income tax (GPM): progressive 20% to 36 VDU (€83,237), 25% to 60 VDU (€138,729),
   32% above, on GROSS — Sodra/PSD are NOT deductible from the PIT base. (Confirmed
   by eBook/Deel/Skuad all landing on €36,300 at €60k.) The annual non-taxable
   amount (NPD) is reconciled from annual employment income and reaches zero near
   €32.1k.
 - Employer: indefinite-contract unemployment 1.31% + accident class I 0.14%,
   both capped at 60 VDU, plus uncapped Guarantee Fund 0.16% and Long-term
   Employment Benefit Fund 0.16%.

The VSD ceiling (60 VDU = €138,729/yr, 2026: 60 × €2,312.15) is now modelled: above
it VSD stops but PSD continues, so high salaries keep more — the €300k+ employee
marginal is PSD 6.98% + 32% GPM, not the full 19.5%.

Sources: Rödl/Forvis Mazars Lithuania 2026 (brackets); Sodra 2026 (rates).
"""
from engine import progressive

NAME = "Lithuania"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Unemployment 1.31% + accident class I 0.14% (capped) + Guarantee and Long-term funds 0.16% each"
INF = float("inf")

VSD = 0.1252                                 # Sodra social insurance — capped at 60 VDU
PSD = 0.0698                                 # compulsory health — uncapped
VSD_CAP = 138729                             # 60 VDU (2026: 60 × €2,312.15/mo)
ER_CAPPED_RATE = 0.0131 + 0.0014              # indefinite unemployment + class-I accident
ER_UNCAPPED_RATE = 0.0016 + 0.0016            # guarantee + long-term employment funds
BRACKETS = [(83237, 0.20), (138729, 0.25), (INF, 0.32)]   # 36 VDU / 60 VDU switch points
NPD_MAX = 8964
NPD_THRESHOLD = 13836
NPD_PHASEOUT = 0.49


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    employee = VSD * min(gross, VSD_CAP) + PSD * gross   # VSD capped, PSD uncapped
    if gross <= NPD_THRESHOLD:
        npd = min(gross, NPD_MAX)
    else:
        npd = max(0.0, NPD_MAX - NPD_PHASEOUT * (gross - NPD_THRESHOLD))
    income_tax = progressive(max(0.0, gross - npd), BRACKETS)

    net = gross - employee - income_tax
    employer_cost = (gross + min(gross, VSD_CAP) * ER_CAPPED_RATE
                     + gross * ER_UNCAPPED_RATE)
    return employer_cost, net
