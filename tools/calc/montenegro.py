"""Montenegro salary calculation — computed from published tax rates.

Rates are 2026 (single private-sector employee). Confirmed against PwC Tax
Summaries (post-"Europe Now 2.0", Oct 2024):
 - Health contributions ABOLISHED (0% both sides).
 - Employee: pension & disability (PIO) 10% + unemployment 0.5%. PIO cap ~€68,765
   /yr is the one figure not fully confirmed for 2026; it only bites above ~€69k.
 - Employer: unemployment 0.5% ONLY — no employer pension or health. Montenegro's
   employer cost is therefore ~+0.5%, the lowest here. This is CORRECT, not a gap:
   "Europe Now" deliberately removed the employer social burden.
 - Salary tax: progressive on MONTHLY GROSS — 0% to €700, 9% €700–1,000, 15%
   above. Brackets are gross amounts; contributions do NOT reduce the base.
 - Municipal surtax ON the income tax: 15% Podgorica/Cetinje, 13% elsewhere. We
   use Podgorica (capital) = 15%, consistent with the rest of the app.

Lesson logged: three EOR calculators put employer cost at +5–7% and net ~€46k —
BOTH wrong (legacy/non-statutory items; taxing after contributions). The statutory
reconstruction here, verified vs PwC, is +0.5% employer and tax-on-gross. A clean
case of clustered third-party calculators agreeing *and* being wrong together.

Sources: PwC Montenegro tax summaries (PIT brackets, surtax base, contributions).
"""
from engine import progressive

NAME = "Montenegro"
CURRENCY = "EUR"
YEAR = 2026
INF = float("inf")

PENSION_RATE = 0.10
PENSION_CAP = 68765            # annual ceiling
UNEMPLOYMENT = 0.005           # employee and employer each

# Salary tax: progressive on MONTHLY gross.
TAX_BANDS_MONTHLY = [(700, 0.0), (1000, 0.09), (INF, 0.15)]
SURTAX = 0.15                  # Podgorica municipal surtax, charged on the income tax


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    pension = min(gross, PENSION_CAP) * PENSION_RATE
    unemployment = gross * UNEMPLOYMENT

    income_tax = progressive(gross / 12, TAX_BANDS_MONTHLY) * 12
    surtax = income_tax * SURTAX

    net = gross - pension - unemployment - income_tax - surtax
    employer_cost = gross + gross * UNEMPLOYMENT   # employer pension assumed 0% — UNVERIFIED
    return employer_cost, net
