"""Sweden salary calculation — computed from published tax rates.

Rates are 2026 (single). Currency SEK (FX path). Sweden is distinctive: NO employee
social contributions — just income tax — plus a single flat employer rate.
 - Employee: municipal tax ~32.38% (national average) + state tax 20% above the
   SEK 643,100 threshold, on (gross − grundavdrag); minus the jobbskatteavdrag
   (work tax credit).
 - Employer: arbetsgivaravgifter 31.42% (flat, no cap) + near-universal
   occupational pension (tjänstepension) ~4.5% ≈ 36% (the pension is
   collective-agreement based, like the Dutch one).

*** APPROXIMATE: the grundavdrag and jobbskatteavdrag tapers are simplified
estimates (the research gave rates, not the formulas); the municipal rate and
occupational-pension share vary. Verify against Skatteverket. ***

Sources: Verksamt 2026 (employer 31.42%); SCB (municipal avg 32.38%); Skatteverket
(state-tax threshold).
"""

NAME = "Sweden"
CURRENCY = "SEK"
YEAR = 2026

MUNICIPAL = 0.3238
GRUNDAVDRAG = 16800              # basic allowance floor for higher incomes
STATE_RATE = 0.20
STATE_THRESHOLD = 643100         # skiktgräns (on taxable income)
JOBB_MAX = 30000                 # jobbskatteavdrag near its max (estimate)
JOBB_PHASE_START = 782400        # ~SEK 65,200/mo
JOBB_PHASE_RATE = 0.03
ER_RATE = 0.3142 + 0.045         # arbetsgivaravgifter + occupational pension ≈ 36%


def compute(gross):
    """Return (employer_cost, net) in SEK; build_formula converts to EUR."""
    taxable = max(0.0, gross - GRUNDAVDRAG)
    municipal = MUNICIPAL * taxable
    state = STATE_RATE * max(0.0, taxable - STATE_THRESHOLD)
    jobb = max(0.0, JOBB_MAX - JOBB_PHASE_RATE * max(0.0, gross - JOBB_PHASE_START))
    income_tax = max(0.0, municipal + state - jobb)

    net = gross - income_tax
    employer_cost = gross * (1 + ER_RATE)
    return employer_cost, net
