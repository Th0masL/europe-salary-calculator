"""Germany salary calculation — computed from published tax rates.

Rates are 2026 for the age-40, single, childless, tax-class-I profile in Berlin,
with statutory health insurance using the official average add-on.

Social contributions (clear): four branches, each split ~50/50, with TWO ceilings:
 - Pension 9.3% + unemployment 1.3%, capped at €101,400/yr.
 - Health 8.75% (7.3% + half the 2.9% average add-on), capped at €69,750/yr.
 - Care: employer 1.8%; employee 1.8% + 0.6% childless surcharge = 2.4%; €69,750 cap.
(The research's care split looked wrong; these are the standard rates.)

Income tax: Germany uses the continuous §32a polynomial tariff, not flat brackets.
The BMF annual wage-tax sequence floors taxable income and wage tax to whole euros.
Employer cost is the determinable statutory floor; fund-specific U1/U2 and
activity-specific accident insurance are excluded rather than guessed.

Sources: BMF §32a 2026 (verified coefficients + continuity); PwC Germany 2026
deductions; DRV/BMG 2026 rates + ceilings (€101,400 / €69,750); GFB €12,348.
"""
import math

NAME = "Germany"
CURRENCY = "EUR"
YEAR = 2026
EMPLOYER_BREAKDOWN = "Statutory floor: pension/unemployment + health/care (capped) + 0.15% insolvency; variable U1/U2 and accident insurance excluded"

PENSION_CAP = 101400          # pension + unemployment ceiling
HEALTH_CAP = 69750            # health + care ceiling

EMPLOYEE_PENS_UNEMP = 0.093 + 0.013      # 10.6%
EMPLOYEE_HEALTH_CARE = 0.0875 + 0.024    # 11.15% (health 8.75 + childless care 2.4)
EMPLOYER_PENS_UNEMP = 0.093 + 0.013      # 10.6%
EMPLOYER_HEALTH_CARE = 0.0875 + 0.018    # 10.55% (health 8.75 + care 1.8)
EMPLOYER_INSOLVENCY = 0.0015
DEDUCTIBLE_HEALTH_CARE = 0.0845 + 0.024  # payroll precautionary health + care
LUMP_SUMS = 1230 + 36        # Werbungskostenpauschale + Sonderausgabenpauschbetrag


def _est(zve):
    """2026 §32a income tax (reconstructed coefficients)."""
    if zve <= 12348:
        return 0.0
    if zve <= 17799:
        y = (zve - 12348) / 10000.0
        return (914.51 * y + 1400) * y
    if zve <= 69878:
        z = (zve - 17799) / 10000.0
        return (173.10 * z + 2397) * z + 1034.87
    if zve <= 277825:
        return 0.42 * zve - 11135.63
    return 0.45 * zve - 19470.38


SOLI_FREIGRENZE = 20350       # 2026 single; below this assessed income tax, no Soli
SOLI_RATE = 0.055
SOLI_PHASEIN = 0.119          # Milderungszone slope above the Freigrenze


def _soli(income_tax):
    """Solidaritätszuschlag: 5.5% of income tax, above a Freigrenze with a phase-in."""
    amount = min(SOLI_RATE * income_tax,
                 max(0.0, SOLI_PHASEIN * (income_tax - SOLI_FREIGRENZE)))
    return math.floor(amount * 100) / 100


def compute(gross):
    """Return (employer_cost, net) for an annual gross salary, in EUR."""
    pu_base = min(gross, PENSION_CAP)
    hc_base = min(gross, HEALTH_CAP)

    employee = pu_base * EMPLOYEE_PENS_UNEMP + hc_base * EMPLOYEE_HEALTH_CARE

    vorsorge = pu_base * 0.093 + hc_base * DEDUCTIBLE_HEALTH_CARE
    zve = int(max(0.0, gross - vorsorge - LUMP_SUMS))
    income_tax = int(_est(zve))

    net = gross - employee - income_tax - _soli(income_tax)
    employer_cost = (gross + pu_base * EMPLOYER_PENS_UNEMP
                     + hc_base * EMPLOYER_HEALTH_CARE
                     + pu_base * EMPLOYER_INSOLVENCY)
    return employer_cost, net
