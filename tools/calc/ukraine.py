"""Ukraine salary calculation — computed from published tax rates.

Rates are 2026 (single). Currency UAH (FX path — needed for the USC cap).
 - Employee: 18% PIT + 5% military tax on gross, no general allowance and no cap —
   so net is a flat 77% of gross.
 - Employer: 22% unified social contribution (USC/ЄСВ) on gross, capped at 15× the
   minimum wage per month (UAH 8,647 → UAH 129,705/mo). The cap sits at ~€34k/yr, so
   above that the employer USC is a flat cash amount and its % of gross falls.

Sources: PwC Ukraine 2026 (18% PIT, 5% military tax, 22% USC, 15× min-wage cap with
the 20× increase postponed for 2026).
"""

NAME = "Ukraine"
CURRENCY = "UAH"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Unified social contribution (USC) 22% (capped at 15× min wage)"

MIN_WAGE = 8647
USC_CAP = MIN_WAGE * 15 * 12       # 15× min wage/month, annualized
PIT = 0.18
MILITARY = 0.05
USC = 0.22


def compute(gross):
    """Return (employer_cost, net) in UAH; build_formula converts to EUR."""
    net = gross * (1 - PIT - MILITARY)
    employer_cost = gross + USC * min(gross, USC_CAP)
    return employer_cost, net
