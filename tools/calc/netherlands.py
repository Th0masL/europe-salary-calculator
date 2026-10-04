"""Netherlands salary calculation — computed from published tax rates.

Rates are 2026 for the age-40, single, no-child profile, no 30% ruling and no
occupational pension. The Dutch system is distinctive: the EMPLOYEE pays no
separate social contributions — "national
insurance" is baked into the first Box-1 bracket — so net = gross − wage tax + tax
credits. The EMPLOYER pays the employee-insurance premiums (WW/WIA/AOF) and the
income-related health contribution (Zvw), capped at the maximum premium wage.

 - Box 1 brackets 2026: 35.75% to €38,883, 37.56% to €78,426, 49.50% above.
 - Tax credits (reduce the tax, both phase out with income): general (algemene
   heffingskorting) and labour (arbeidskorting).
 - Employer scenario: specified small business-services employer, written
   indefinite non-on-call contract, low AWf/Aof, sector-43 Whk and Zvw: 16.77%
   capped at €79,409. Occupational pension/CAO costs are excluded.

Net is computed PRE-pension on the employee side too (no occupational-pension
deduction), which matches eBook; deducting the employee pension share would lower
net ~€4–6k. Holiday allowance 8% is treated as part of the entered gross.

The 2026 tax credits are the official Belastingdienst figures (general €3,115
tapering from €29,736; labour builds up, peaks €5,685, tapers to €0 at €132,920) —
net is validated at €20k→€19,453 and €30k→€27,754. The employer rate is the named
small business-services scenario documented in the research dossier.

Sources: Belastingdienst 2026 (brackets); Deloitte Belastingplan 2026 (credits);
UWV/Belastingdienst (employer premiums, max premium wage).
"""
import math

from engine import progressive

NAME = "Netherlands"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Named small business-services scenario: low AWf/Aof + Wko + sector-43 Whk + Zvw = 16.77% to €79,409; pension excluded"
INF = float("inf")

BRACKETS = [(38883, 0.3575), (78426, 0.3756), (INF, 0.495)]

MAX_PREMIUM_WAGE = 79409
ER_STATUTORY = 0.1677


def _general_credit(income):
    """Algemene heffingskorting 2026 (under AOW age): €3,115, tapering to €0 by €78,426."""
    return max(0.0, 3115 - 0.06398 * max(0.0, income - 29736))


def _labour_credit(income):
    """Arbeidskorting 2026 (under AOW age): builds up, peaks €5,685, then tapers to €0."""
    if income <= 11965:
        return 0.08324 * income
    if income <= 25845:
        return 996 + 0.31009 * (income - 11965)
    if income <= 45592:
        return 5300 + 0.01950 * (income - 25845)
    return max(0.0, 5685 - 0.06510 * (income - 45592))   # €0 at €132,920


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    tax = progressive(gross, BRACKETS)
    tax = math.floor(max(0.0, tax - _general_credit(gross) - _labour_credit(gross)) + .5)

    net = gross - tax
    employer_cost = gross + min(gross, MAX_PREMIUM_WAGE) * ER_STATUTORY
    return employer_cost, net
