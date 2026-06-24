"""Lithuania salary calculation — computed from published tax rates.

Rates are 2026 (single, no children). Like Romania, the 2019 reform shifted almost
all contributions onto the EMPLOYEE, leaving a very low employer cost.
 - Employee: Sodra social insurance 12.52% + compulsory health (PSD) 6.98% = 19.5%.
 - Income tax: progressive 20% to €82,962, 25% to €138,270, 32% above, on GROSS —
   Sodra/PSD are NOT deductible from the PIT base. (The research's stated order was
   wrong; net = gross − 19.5% − GPM, which is confirmed by eBook/Deel/Skuad all
   landing on €36,300 at €60k.) The non-taxable amount (NPD) tapers to €0 in range.
 - Employer: Sodra 1.77% (permanent) + Guarantee Fund 0.16% + Long-term Employment
   Benefit Fund 0.16% + office accident ~0.4% ≈ 2.49% (cross-refs run a bit higher
   on the accident class).

Note: the Sodra ceiling (~60 average wages) caps the social portion above ~€126k,
so the €150k point slightly overstates employee contributions — flagged.

Sources: Rödl/Forvis Mazars Lithuania 2026 (brackets); Sodra 2026 (rates).
"""
from engine import progressive

NAME = "Lithuania"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Sodra 1.77% + Guarantee Fund 0.16% + Long-term Employment Fund 0.16% + accident ~0.4%"
INF = float("inf")

EE_RATE = 0.1252 + 0.0698                    # Sodra + health = 19.5%
ER_RATE = 0.0177 + 0.0016 + 0.0016 + 0.004   # Sodra + guarantee + long-term + accident ≈ 2.49%
BRACKETS = [(82962, 0.20), (138270, 0.25), (INF, 0.32)]


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    employee = gross * EE_RATE
    income_tax = progressive(gross, BRACKETS)   # PIT on GROSS; contributions not deductible

    net = gross - employee - income_tax
    employer_cost = gross * (1 + ER_RATE)
    return employer_cost, net
