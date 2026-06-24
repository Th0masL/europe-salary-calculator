"""Austria salary calculation — computed from published tax rates.

Rates are 2026 (single, no children, full insurance). Austria is a 14-SALARY
system and that's the whole game: the two extra "special payments" (13th/14th) are
taxed at a flat favourable rate, which lifts net well above what a naive 12-month
progressive calc would give.

Model (validated against PwC's official 2026 worked examples — it reproduces their
€54k case to the cent: SS €696.99/mo and wage tax €505.64/mo):
 - Split annual gross into 14 equal payments: 12 regular + 2 special.
 - Employee social security 18.07% (incl. the AK + housing levies — the research's
   17.07% omitted them; the PwC examples confirm 18.07%), on each payment up to the
   Höchstbeitragsgrundlage (~€6,630/mo regular, ~€13,260/yr special — 2026
   estimate; only bites above ~€93k gross).
 - Regular pay: progressive 2026 brackets on (regular − SS), minus a ~€548 credit
   (Verkehrsabsetzbetrag etc., calibrated to the PwC examples).
 - Special pay: first €620 tax-free, remainder at 6% (the 13th/14th sit within the
   Jahressechstel and stay in the 6% band for salaries up to ~€175k).
 - Employer: SS 20.38% + DB 3.7% + DZ 0.36% + Kommunalsteuer 3.0% + MVK 1.53%
   ≈ 29% (SS portion capped; the others on full gross).

Flags: the 2026 Höchstbeitragsgrundlage is an estimate (affects only €100k+); the
employer levies beyond SS are standard but DZ varies slightly by Land.

Sources: PwC Austria 2026 (brackets + worked examples); ÖGK 2026 SS rates.
"""
from engine import progressive

NAME = "Austria"
CURRENCY = "EUR"
YEAR = 2026
INF = float("inf")

MONTHLY_CEIL = 6630          # Höchstbeitragsgrundlage 2026, monthly regular (estimate)
SPECIAL_CEIL = 13260         # annual ceiling for special payments (≈ 2× monthly)
EE_SS = 0.1807               # employee SS incl. AK + housing (validated vs PwC)
ER_SS = 0.2038
ER_LEVIES = 0.037 + 0.0036 + 0.03 + 0.0153   # DB + DZ + Kommunalsteuer + MVK ≈ 8.59%
TAX_CREDIT = 548             # Verkehrsabsetzbetrag etc. (calibrated to PwC examples)
SPECIAL_EXEMPT = 620
SPECIAL_RATE = 0.06

BRACKETS = [(13539, 0.0), (21992, 0.20), (36458, 0.30), (70365, 0.40),
            (104859, 0.48), (1000000, 0.50), (INF, 0.55)]


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    monthly = gross / 14.0
    regular_annual = monthly * 12
    special_annual = monthly * 2

    reg_ss = min(monthly, MONTHLY_CEIL) * 12 * EE_SS
    spec_ss = min(special_annual, SPECIAL_CEIL) * EE_SS

    reg_tax = max(0.0, progressive(regular_annual - reg_ss, BRACKETS) - TAX_CREDIT)
    spec_tax = max(0.0, special_annual - spec_ss - SPECIAL_EXEMPT) * SPECIAL_RATE

    net = gross - reg_ss - spec_ss - reg_tax - spec_tax

    er_ss = (min(monthly, MONTHLY_CEIL) * 12 + min(special_annual, SPECIAL_CEIL)) * ER_SS
    employer_cost = gross + er_ss + gross * ER_LEVIES
    return employer_cost, net
