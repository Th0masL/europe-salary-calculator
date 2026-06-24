"""United Kingdom salary calculation — computed from published tax rates.

Rates are 2026/27 (single, England/NI, standard tax code). Currency GBP (FX path).
 - Income tax (PAYE): personal allowance £12,570, tapered away £1 per £2 above
   £100,000 (gone by £125,140 — the ~60% marginal band), then 20% to £50,270,
   40% to £125,140, 45% above.
 - Employee NIC (Class 1 primary): 8% between £12,570 and £50,270, 2% above.
 - Employer NIC (Class 1 secondary): 15% on earnings above the £5,000 secondary
   threshold. (Apprenticeship Levy only bites above a £3M pay bill; Employment
   Allowance is a small-employer offset — neither applies to a standard employee.)
 - PAYE tax and NIC are both on gross — NIC is NOT deductible from the tax base.

Net is validated against UK gross-to-net calculators (~78% at €60k, 70% at €100k,
62% at €150k where the allowance is fully tapered). The near-universal
auto-enrolment workplace pension (min 5% employee + 3% employer on qualifying
earnings £6,240–£50,270) is OPT-OUT, so it's excluded — Deel/Skuad include it,
which lowers their net ~€2.5k and lifts employer cost ~3%. (eBook still uses 2025
rates, so its employer cost predates the 2026 reform to 15% / £5,000.)

Sources: HMRC 2026/27 rates and thresholds; PwC UK.
"""

NAME = "United Kingdom"
CURRENCY = "GBP"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Employer NIC (Class 1) 15% above £5,000"


def _income_tax(gross):
    pa = max(0.0, 12570 - max(0.0, gross - 100000) / 2)
    t = max(0.0, gross - pa)
    add_thresh = 125140 - pa             # additional-rate threshold in taxable terms
    return (0.20 * min(t, 37700)
            + 0.40 * max(0.0, min(t, add_thresh) - 37700)
            + 0.45 * max(0.0, t - add_thresh))


def _employee_nic(gross):
    return 0.08 * max(0.0, min(gross, 50270) - 12570) + 0.02 * max(0.0, gross - 50270)


def compute(gross):
    """Return (employer_cost, net) in GBP; build_formula converts to EUR."""
    net = gross - _income_tax(gross) - _employee_nic(gross)
    employer_cost = gross + 0.15 * max(0.0, gross - 5000)
    return employer_cost, net
