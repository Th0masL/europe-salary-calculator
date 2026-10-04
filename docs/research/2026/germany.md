# Germany employee payroll, wage tax, and employer cost, 2026 — independent research dossier

**All sources accessed:** 2026-10-04
**Currency:** euro (EUR)
**Result type:** annualized payroll withholding and contribution liability for regular salary; not individualized tax-return advice.

## 1. Reproducible employee and employer

The employee is age 30, resident throughout 2026, single, tax class I, childless, not a church member, and has no other income, benefits, allowances entered in ELStAM, deductible expenses above the statutory lump sums, or special payment. The job is ordinary private employment covered by statutory pension and unemployment insurance.

The employee lives and works in **Berlin**, not Saxony. This fixes the childless employee's long-term-care contribution at 2.4% and the employer share at 1.8%. The Saxony exception is shown separately.

The employee remains in statutory health insurance even when annual salary exceeds the 2026 compulsory-insurance threshold. Because no sickness fund is named, the model uses the officially announced **average additional contribution rate of 2.9%**, exactly as the final BMF 2026 payroll algorithm's general test table does. An actual fund's rate can differ.

`G` is annual regular taxable gross cash salary, paid evenly through the year. There are no one-off payments. Annual direct calculations can differ by cents from twelve rounded monthly contribution calculations.

## 2. Primary official sources

### Wage and income tax

1. Bundesministerium der Finanzen (BMF), **“Programmablaufpläne zur Lohnsteuer für/ab 2026”**, final corrected version dated **12 November 2025**: <https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026.html>. The downloadable **Anlage 1** is the official machine payroll algorithm and **Anlage 2** is the manual table algorithm. Pinpoints on Anlage 2 page 1: EUR 12,348 basic allowance; EUR 20,350 solidarity-surcharge exemption; health/care ceiling EUR 69,750; average health additional rate 2.9%; pension/unemployment ceiling EUR 101,400; unemployment 2.6%; pension 18.6%. Page 21 says the general annual check table uses `KVZ = 2.90` and full social-insurance coverage.

2. BMF, **“LStH 2026 — § 32a Einkommensteuertarif”**, official 2026 Income Tax Handbook: <https://ksth.bundesfinanzministerium.de/lsth/2026/A-Einkommensteuergesetz/IV-Tarif-31-34b/Paragraf-32a/inhalt.html>. Pinpoint: the five exact 2026 formulas and the instruction to round taxable income down to whole euros, reproduced in section 4 below. This page is the 2026 handbook; no separate page publication date is displayed.

3. BMF official external test interface documentation, **“Lohn- und Einkommensteuerrechner: Externe Programmierschnittstelle”**: <https://www.bmf-steuerrechner.de/interface/einganginterface.xhtml>, and its 2026 calculator input documentation: <https://www.bmf-steuerrechner.de/bl/bl2026/eingabeformbl2026.xhtml>. Pinpoints: the official Programmablaufplan is the basis for wage tax and solidarity surcharge; `RE4` is taxable gross cents, and the inputs distinguish pension, unemployment, health, additional health rate, care, Saxony, and childless status. The five worked wage-tax results were independently checked against `2026Version1` with `LZZ=1`, `STKL=1`, `KVZ=2.90`, `PVZ=1`, `PVS=0`, statutory insurance, and no allowances.

4. BMF, **“LStH 2026 — Solidaritätszuschlaggesetz 1995,” §§ 3–4**, official 2026 handbook text: <https://lsth.bundesfinanzministerium.de/lsth/2026/B-Anhaenge/Anhang-27/I/inhalt.html>. The governing amendment is Article 4 of the Tax Development Act of **23 December 2024**, effective **1 January 2026**. Pinpoints: single-person exemption **EUR 20,350** of the tax base; standard rate **5.5%**; mitigation-zone maximum **11.9%** of the excess over the exemption; fractions of a cent are discarded.

### 2026 social insurance

5. Bundesministerium für Arbeit und Soziales (BMAS), **“Sozialversicherungsrechengrößen-Verordnung 2026”**: <https://www.bmas.de/DE/Service/Gesetze-und-Gesetzesvorhaben/sozialversicherungs-rechengroessenverordnung-2026.html>. The Cabinet approved it **8 October 2025**, the Bundesrat approved it **21 November 2025**, and the values apply from **1 January 2026**. Pinpoints: health/care contribution ceiling EUR 5,812.50 monthly / **EUR 69,750 annually**; general pension/unemployment ceiling EUR 8,450 monthly / **EUR 101,400 annually**; statutory-health compulsory-insurance threshold EUR 6,450 monthly / **EUR 77,400 annually**.

6. Deutsche Rentenversicherung, **“Maßgebliche Rechengrößen und Werte ab 1.1.2026”**, official 2026 table: <https://www.deutsche-rentenversicherung.de/SharedDocs/Downloads/DE/Traeger/BayernSued/Zahlen_und_Tabellen/ZuT_2026_1.pdf?__blob=publicationFile&v=4>. Pinpoints: pension 18.6%, split 9.3%/9.3%; health 14.6%, split 7.3%/7.3%; official average additional health contribution 2.9%, split 1.45%/1.45%; unemployment 2.6%, split 1.3%/1.3%; care 3.6%, normally split 1.8%/1.8%; childless supplement 0.6% employee-only.

7. Bundesministerium für Gesundheit (BMG), **“Beiträge der gesetzlichen Krankenversicherung (GKV)”**, 2026 table: <https://www.bundesgesundheitsministerium.de/beitraege>. Pinpoints: general health rate 14.6%; official 2026 average additional rate 2.9%; fund-specific rates may differ; health ceiling EUR 69,750; compulsory-insurance threshold EUR 77,400; employers share the fund-specific additional contribution equally.

8. BMG, **“Finanzierung der sozialen Pflegeversicherung”**, current 2026 official guidance: <https://www.bundesgesundheitsministerium.de/themen/pflege/online-ratgeber-pflege/die-pflegeversicherung/finanzierung>. Pinpoints: total care rate 3.6%, childless total 4.2%, ordinary states employee 2.4%/employer 1.8%, and Saxony employee 2.9%/employer 1.3%. The childless surcharge begins after age 23; the selected employee is 30.

9. Deutsche Rentenversicherung, **“Werte der Rentenversicherung,” stand 1 July 2026**: <https://www.deutsche-rentenversicherung.de/DRV/DE/Experten/Zahlen-und-Fakten/Werte-der-Rentenversicherung/werte-der-rentenversicherung>. Pinpoints: 2026 pension 18.6%, unemployment 2.6%, health 14.6%, care 3.6%/childless 4.2%, and pension ceiling EUR 8,450 monthly.

### Employer-only charges

10. BMAS, **“Das ändert sich im neuen Jahr”**, published **22 December 2025**, effective **1 January 2026**: <https://www.bmas.de/DE/Service/Presse/Pressemitteilungen/2025/das-aendert-sich-im-neuen-jahr.html>. Pinpoints: 2026 insolvency-money levy **0.15%** and unemployment rate 2.6%. Deutsche Rentenversicherung's **“Insolvenzgeldumlage”** confirms that insolvent-capable employers pay it alone on pension-insurable remuneration, including one-off payments, up to the pension ceiling: <https://www.deutsche-rentenversicherung.de/DRV/DE/Experten/Arbeitgeber-und-Steuerberater/summa-summarum/Lexikon/I/insolvenzgeldumlage>.

11. Deutsche Gesetzliche Unfallversicherung (DGUV), **“Beitragsberechnung”**, current guidance: <https://www.dguv.de/de/ihr_partner/unternehmen/beitragsberechnung/index.jsp>. Pinpoint: occupational-accident insurance is retrospectively assessed as `remuneration × contribution factor × risk class / 1,000`, then potentially adjusted for the employer's claims record. There is no national universal employee percentage.

12. Deutsche Rentenversicherung, **“Ausgleichsverfahren U1”** and **“Ausgleichsverfahren U2”**, current official guidance: <https://www.deutsche-rentenversicherung.de/DRV/DE/Experten/Arbeitgeber-und-Steuerberater/summa-summarum/Lexikon/A/ausgleichsverfahren_u1> and <https://www.deutsche-rentenversicherung.de/DRV/DE/Experten/Arbeitgeber-und-Steuerberater/summa-summarum/Lexikon/A/ausgleichsverfahren_u2>. Pinpoints: U1 applies to employers generally having no more than 30 employees; U2 applies regardless of employer size, including where only men are employed; both are employer-only and sickness-fund-specific. Therefore no universal U1/U2 rate can be put into the numeric employer total.

## 3. Contribution formulas

Let:

```text
R = min(G, 101,400)    pension, unemployment, insolvency-levy base
H = min(G, 69,750)     health and long-term-care base
```

### Employee, Berlin/non-Saxony, childless

| Component | Formula |
|---|---:|
| Pension | 9.30% × `R` |
| Unemployment | 1.30% × `R` |
| Health, using official average additional rate | (7.30% + 1.45%) × `H` = 8.75% × `H` |
| Long-term care | (1.80% + 0.60% childless) × `H` = 2.40% × `H` |

The childless employee total is therefore `10.60% × R + 11.15% × H`. Contributions stop increasing above their respective ceilings; there is no uncapped high-income social contribution in this model.

### Employer fixed statutory components

| Component | Formula |
|---|---:|
| Pension | 9.30% × `R` |
| Unemployment | 1.30% × `R` |
| Health | 8.75% × `H` |
| Long-term care | 1.80% × `H` |
| Insolvency-money levy | 0.15% × `R` |

The quantified employer floor is `G` plus those five items. Add U2, U1 if the employer is in scope, and occupational-accident insurance at their actual rates. Other collectively agreed benefits or occupational pension are not universal statutory percentages.

In Saxony only, for this childless employee, move 0.50 percentage point of `H` from employer to employee: employee care becomes 2.90% and employer care 1.30%. Total combined care funding does not change.

## 4. Exact 2026 tax algorithm

The wage-tax algorithm does not apply the income-tax polynomial to gross pay. For this exact profile, BMF's `Vorsorgepauschale` is:

```text
pension subamount     = 9.30% × R
basic health/care     = (8.45% + 2.40%) × H = 10.85% × H
VSP                   = pension subamount + basic health/care
taxable annual amount = floor(G - 1,230 - 36 - VSP) whole euros
```

EUR 1,230 is the employee-expense lump sum (`Arbeitnehmer-Pauschbetrag`) and EUR 36 is the special-expense lump sum. The payroll precautionary allowance's health component uses the reduced 14.0% base health rate plus half the 2.9% additional rate: `14.0% / 2 + 2.9% / 2 = 8.45%`. That tax deduction is deliberately not identical to the 8.75% actual employee health contribution. Unemployment insurance does not add a further payroll precautionary deduction for this profile.

For whole-euro taxable income `x`, § 32a EStG gives:

```text
tax = 0                                             x <= 12,348

y = (x - 12,348) / 10,000
tax = (914.51*y + 1,400)*y                         12,349 <= x <= 17,799

z = (x - 17,799) / 10,000
tax = (173.10*z + 2,397)*z + 1,034.87              17,800 <= x <= 69,878

tax = 0.42*x - 11,135.63                           69,879 <= x <= 277,825
tax = 0.45*x - 19,470.38                           x >= 277,826
```

The resulting annual wage tax is rounded down to whole euros under the BMF annual algorithm.

For this childless tax-class-I case, solidarity surcharge on annual wage tax `T` is:

```text
Soli = 0                                             T <= 20,350
Soli = floor-cent(min(5.5%*T, 11.9%*(T-20,350)))    T > 20,350
```

No church tax is charged.

## 5. Worked annual calculations

### Employee contributions

| `G` | `R` | `H` | Pension | Unemployment | Health | Care | Total employee social |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 20,000 | 20,000 | 1,860.00 | 260.00 | 1,750.00 | 480.00 | 4,350.00 |
| 60,000 | 60,000 | 60,000 | 5,580.00 | 780.00 | 5,250.00 | 1,440.00 | 13,050.00 |
| 100,000 | 100,000 | 69,750 | 9,300.00 | 1,300.00 | 6,103.13 | 1,674.00 | 18,377.13 |
| 200,000 | 101,400 | 69,750 | 9,430.20 | 1,318.20 | 6,103.13 | 1,674.00 | 18,525.53 |
| 600,000 | 101,400 | 69,750 | 9,430.20 | 1,318.20 | 6,103.13 | 1,674.00 | 18,525.53 |

### Tax intermediates and official BMF results

| `G` | Pension VSP | Health/care VSP | Total VSP | Taxable `x` | Tariff zone | Wage tax | Soli |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 1,860.00 | 2,170.00 | 4,030.00 | 14,704 | 2 | 380.00 | 0.00 |
| 60,000 | 5,580.00 | 6,510.00 | 12,090.00 | 46,644 | 3 | 9,389.00 | 0.00 |
| 100,000 | 9,300.00 | 7,567.88 | 16,867.88 | 81,866 | 4 | 23,248.00 | 344.86 |
| 200,000 | 9,430.20 | 7,567.88 | 16,998.08 | 181,735 | 4 | 65,193.00 | 3,585.61 |
| 600,000 | 9,430.20 | 7,567.88 | 16,998.08 | 581,735 | 5 | 242,310.00 | 13,327.05 |

For example:

```text
G = 20,000:
  x = floor(20,000 - 1,230 - 36 - 4,030) = 14,704
  y = (14,704 - 12,348) / 10,000 = 0.2356
  raw tax = (914.51 × 0.2356 + 1,400) × 0.2356 = 380.6020357936
  wage tax = 380

G = 100,000:
  x = floor(100,000 - 1,230 - 36 - 16,867.875) = 81,866
  wage tax = floor(0.42 × 81,866 - 11,135.63) = 23,248
  Soli = floor-cent(11.9% × (23,248 - 20,350)) = 344.86

G = 600,000:
  wage tax = floor(0.45 × 581,735 - 19,470.38) = 242,310
  Soli = 5.5% × 242,310 = 13,327.05
```

### Take-home cash

| `G` | Employee social | Wage tax | Soli | Church tax | Take-home cash |
|---:|---:|---:|---:|---:|---:|
| 20,000 | 4,350.00 | 380.00 | 0.00 | 0.00 | 15,270.00 |
| 60,000 | 13,050.00 | 9,389.00 | 0.00 | 0.00 | 37,561.00 |
| 100,000 | 18,377.13 | 23,248.00 | 344.86 | 0.00 | 58,030.02 |
| 200,000 | 18,525.53 | 65,193.00 | 3,585.61 | 0.00 | 112,695.87 |
| 600,000 | 18,525.53 | 242,310.00 | 13,327.05 | 0.00 | 325,837.43 |

Take-home is `G - employee social - wage tax - Soli`. Values use unrounded annual social contributions before the final displayed-cent rounding.

## 6. Employer cost

| `G` | Employer pension | Unemployment | Health | Care | Insolvency levy | Quantified employer charges | Cost floor |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 1,860.00 | 260.00 | 1,750.00 | 360.00 | 30.00 | 4,260.00 | 24,260.00 + variable charges |
| 60,000 | 5,580.00 | 780.00 | 5,250.00 | 1,080.00 | 90.00 | 12,780.00 | 72,780.00 + variable charges |
| 100,000 | 9,300.00 | 1,300.00 | 6,103.13 | 1,255.50 | 150.00 | 18,108.63 | 118,108.63 + variable charges |
| 200,000 | 9,430.20 | 1,318.20 | 6,103.13 | 1,255.50 | 152.10 | 18,259.13 | 218,259.13 + variable charges |
| 600,000 | 9,430.20 | 1,318.20 | 6,103.13 | 1,255.50 | 152.10 | 18,259.13 | 618,259.13 + variable charges |

“Variable charges” means mandatory U2, U1 if the employer has no more than 30 employees, and statutory accident insurance. U1/U2 depend on the sickness fund and chosen reimbursement tariff; accident insurance depends on the Berufsgenossenschaft, risk class, annual contribution factor, and employer claims experience. Gross salary alone cannot determine them.

## 7. Universal rules, exceptions, and limits

- The income-tax polynomial, basic allowance, solidarity rules, pension/unemployment rates, and contribution ceilings are national.
- The health additional rate is **fund-specific**. The 2.9% used here is the BMG's official reference average, not a promise that an employee's fund charges 2.9%.
- Employees above EUR 77,400 are no longer compulsorily insured in statutory health insurance merely by salary. The examples retain statutory insurance by explicit assumption, so contributions remain due up to EUR 69,750.
- The Saxony care split changes employee/employer net amounts by `0.5% × H` but not their combined cost. At salaries of EUR 100,000 or more, that shift is EUR 348.75 annually.
- Accident insurance and U1/U2 are employer-only; no amount is deducted from employee cash.
- The annual wage-tax algorithm is withholding law. A later income-tax assessment can differ through actual deductible expenses, exact insurance contributions, other income, or deductions; none can be inferred from gross salary.

## 8. Evidence assessment and unresolved values

**Strongest evidence.** The exact tax formula comes directly from the official 2026 BMF handbook and final corrected Programmablaufplan. All five wage-tax and solidarity results were cross-checked cent-for-cent with the official BMF 2026 test interface. BMAS's final 2026 regulation and Deutsche Rentenversicherung's effective-1-January table independently agree on the ceilings and contribution splits.

**Weakest evidence / deliberate non-quantification.** A specific sickness fund was not supplied, so 2.9% is the official BMG average-reference assumption; a production payroll must substitute the employee's actual fund rate. U1, U2, and accident-insurance charges are legally required in the circumstances described but have no universal rate. Employer size, fund tariff, industry, risk class, annual assessment factor, and claims experience are unresolved, so adding an invented percentage would be misleading.

The figures also exclude optional/collectively agreed occupational pensions, capital-forming benefits, company benefits, and payroll administration. Regular monthly salary is assumed; one-off payments can change ceiling allocation and require the separate BMF `sonstige Bezüge` calculation.
