# Austria — employee payroll and employer cost, 2026

**Clean-room research dossier.** Only Austrian primary/public-authority material was used (BMF/Findok, RIS legislation, ÖGK, USP, City of Vienna, and the statutory chamber for the regional DZ). Every URL was accessed **2026-10-04**.

## 1. Reproducible scope

The worked case is a resident, single employee with no children, no church-relevant item, one ordinary private white-collar employment, below pension age, working throughout 2026 at a **Vienna workplace**. There are no benefits in kind, expenses beyond the automatic lump sum, commuting allowance, remote-work allowance, union fee, other income, or tax deductions.

### What “annual gross” means here

Austria does not give every employee a universal statutory 13th and 14th salary. The official USP page **“Entgelt”**, updated 20 January 2026, says special payments are due principally when the applicable collective agreement provides them, while most agreements provide holiday and Christmas remuneration: [USP](https://www.usp.gv.at/themen/mitarbeiter-und-gesundheit/entgelt.html). The USP lexicon **“Sonderzahlungen”**, updated 23 June 2026, says amount and payment date are governed by collective agreement, works agreement or individual contract: [USP](https://www.usp.gv.at/services/suchen-und-finden/lexikon/sonderzahlungen.html).

For reproducibility, each annual gross `G` **includes** 14 equal instalments:

```text
M = G / 14
12 regular monthly salaries = 12M
holiday bonus = M, paid separately
Christmas bonus = M, paid separately
total special payments = 2M
```

The employee was employed before 2026, so the first-month exemption from the BV contribution does not apply. The employer's aggregate monthly payroll exceeds EUR 1,460, so small-employer DB/DZ/Kommunalsteuer reductions do not apply.

## 2. Social insurance and payroll contributions

### 2.1 2026 ceilings

ÖGK's **“Arbeitsbehelf 2026 für Dienstgeberinnen und Dienstgeber sowie Lohnverrechnerinnen und Lohnverrechner”**, published 2026, section 2.6 (PDF p. 29), gives EUR 231/day, **EUR 6,930/month**, and **EUR 13,860/year for special payments**. It also says BV is not capped and that special payments bear no AK or housing-fund (WF) contribution: [ÖGK official 2026 guide](https://www.gesundheitskasse.at/cdscontent/load?contentid=10008.802672&version=1770720250).

Define:

```text
R = 12 × min(M, 6,930)       # annual regular SV base
S = min(2M, 13,860)          # annual special-payment SV base
```

### 2.2 Contribution rates for an ordinary employee

ÖGK guide section 3.1.1.2, table “Beschäftigtengruppen und Basisprozentsätze” (PDF p. 41), gives for workers and employees: KV 7.65% (employee 3.87%, employer 3.78%), UV 1.10% employer, PV 22.80% (employee 10.25%, employer 12.55%), AV 5.90% (2.95% each), AK 0.50% employee, WF normally 0.50% each, and insolvency insurance (IE) 0.10% employer. The ordinary national totals shown are 18.07% employee and 20.98% employer.

Vienna changes WF for 2026. City Vienna's **“Wohnbauförderungsbeitrag”**, current for 2026, section “Höhe der Abgabe”, states that from 1 January 2026 each side pays **0.75%** (1.5% total): [City Vienna](https://www.wien.gv.at/wohnen/wohnbaufoerderungsbeitrag). Therefore the Vienna regular-pay totals used here are:

| Component | Employee | Employer |
|---|---:|---:|
| Health (KV) | 3.87% | 3.78% |
| Pension (PV) | 10.25% | 12.55% |
| Unemployment (AV), normal | 2.95% | 2.95% |
| Accident (UV) | — | 1.10% |
| Chamber levy (AK) | 0.50% | — |
| Vienna housing (WF) | 0.75% | 0.75% |
| Insolvency (IE) | — | 0.10% |
| **Regular-pay total** | **18.32%** | **21.23%** |
| **Special-payment total** (no AK/WF) | **17.07%** | **20.48%** |

The employer bears UV; it is not an employee deduction.

### 2.3 Reduced employee unemployment contribution

ÖGK guide section 3.5, effective 1 January 2026, gives the employee AV rate by gross contribution-period pay:

| Gross in the contribution period | Employee AV |
|---:|---:|
| through EUR 2,225 | 0% |
| EUR 2,225.01–2,427 | 1% |
| EUR 2,427.01–2,630 | 2% |
| above EUR 2,630 | 2.95% |

The employer stays at 2.95%. Section 3.5.2 says regular pay and each special payment are tested separately, without adding them. Under the assumed two separate equal bonuses, `AV(M)` applies to regular pay and to each bonus. Thus:

```text
employee regular SV = R × (15.37% + AV(M))
employee special SV = S × (14.12% + AV(M))
employer regular SV = R × 21.23%
employer special SV = S × 20.48%.
```

### 2.4 Betriebliche Vorsorge (Abfertigung neu)

ÖGK guide section 3.6.4 (PDF p. 49) gives **1.53% employer-only** on monthly remuneration including special payments, without the SV ceiling. It also states in section 3.6.2 that the first month with a new employer is generally contribution-free; the continuous-employment assumption removes that variable here.

## 3. Income tax

### 3.1 Ordinary tariff and automatic deductions

EStG 1988 **§33(1), effective 1 January 2026**, states:

| 2026 taxable income slice | Rate |
|---:|---:|
| first EUR 13,539 | 0% |
| 13,539–21,992 | 20% |
| 21,992–36,458 | 30% |
| 36,458–70,365 | 40% |
| 70,365–104,859 | 48% |
| 104,859–1,000,000 | 50% |
| above 1,000,000 (through 2029) | 55% |

Source: [RIS, EStG §33](https://ris.bka.gv.at/Dokumente/Bundesnormen/NOR40274868/NOR40274868.html), consolidated provision effective 2026-01-01 (last amended BGBl. I 97/2025).

EStG **§16(3)** gives the automatic employee expense lump sum of **EUR 132/year**: [RIS §16](https://ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Anlage=&Artikel=&FassungVom=2026-02-24&Gesetzesnummer=10004570&Paragraf=16&ShowPrintPreview=True&Uebergangsrecht=). BMF's **“Werbungskosten Überblick”**, updated 1 January 2026, confirms mandatory insurance, chamber and housing contributions are automatically considered and the EUR 132 lump sum is already in payroll tables: [BMF](https://www.bmf.gv.at/themen/steuern/arbeitnehmerveranlagung/was-kann-ich-geltend-machen/werbungskosten/werbungskosten-ueberblick.html).

EStG §33(5) gives the **EUR 496 Verkehrsabsetzbetrag**. In assessment, it increases by EUR 804 when income is at most EUR 19,761 and phases linearly to zero between EUR 19,761 and EUR 30,259. No Pendlerpauschale or Pendlereuro is assumed. BMF's **“Steuerabsetzbeträge”**, current for 2026, states the same values and that the surcharge is assessment-only: [BMF](https://www.bmf.gv.at/themen/steuern/arbeitnehmerveranlagung/steuertarif-steuerabsetzbetraege/uebersicht-steuerabsetzbetraege.html).

If ordinary tariff tax after credits is negative, §33(8) refunds 55% of qualifying employee contributions, at most EUR 496, increased by up to EUR 804 when the surcharge applies, and never beyond the negative calculated tax. No child-related or single-earner credit applies: “Alleinverdiener” itself requires at least one child.

### 3.2 13th/14th salary taxation

EStG **§67(1)–(2), effective 1 January 2026**, treats 13th/14th salary as “sonstige Bezüge”. Inside the Jahressechstel, after the employee SV attributable to those payments:

| Net special-payment slice | Rate |
|---:|---:|
| first EUR 620 | 0% |
| next EUR 24,380 | 6% |
| next EUR 25,000 | 27% |
| next EUR 33,333 | 35.75% |

Fixed-rate taxation is omitted only when the **gross Jahressechstel** is at most EUR 2,615. Net special payments above EUR 83,333 are taxed under the ordinary rule. The statutory text also defines the Jahressechstel as one-sixth of annualised current regular pay: [RIS, EStG §67](https://ris.bka.gv.at/eli/bgbl/1988/400/P67/NOR40274896). BMF's **Lohnsteuerrichtlinien 2002, maintenance decree 2025**, paras. 1055a and 1063, expressly confirms the 2026 EUR 2,615 limit and the order “special payment minus SV minus EUR 620, then 6%”: [BMF Findok](https://findok.bmf.gv.at/volltext?dokumentId=36d45f2b-2e3b-4e1c-a632-c067dd76817c).

For fourteen equal instalments, `Jahressechstel = 2M`, so both bonuses fit exactly. Define:

```text
B = 2M - employee special SV
special tax = 0 if 2M <= 2,615;
otherwise progressive fixed rates above on B.
Any max(B - 83,333, 0) is moved to ordinary-rate income.

ordinary tariff base E = 12M - employee regular SV - 132 + overflow.
ordinary tax = tariff(E) - 496 - applicable VAB surcharge,
subject to the statutory negative-tax refund limitation.
total annual tax = ordinary tax + special-payment tax.
```

For deciding the VAB-surcharge income threshold, total taxable employment income includes special payments; this distinction does not change any of the five examples (EUR 20,000 remains below the lower threshold; all others are above the upper threshold).

## 4. Employer-only payroll taxes and Vienna assumption

| Item | Rate/base | Authority and pinpoint |
|---|---|---|
| DB to FLAF | 3.70% of payroll | FLAG §41(5), rate from calendar 2025: [RIS](https://ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Anlage=&Artikel=&FassungVom=2025-05-16&Gesetzesnummer=10008220&Paragraf=41&Uebergangsrecht=) |
| DZ, Vienna | 0.36% of DB base | WKO statutory chamber, **“Zuschlag zum Dienstgeberbeitrag”**, status 1 January 2026, 2026 state table: [WKO](https://www.wko.at/lohnverrechnung/zuschlag-dienstgeberbeitrag) |
| Kommunalsteuer | 3.00% | USP **“Kommunalsteuer”**, updated January 2026: [USP](https://www.usp.gv.at/themen/steuern-finanzen/kommunalsteuer/) |
| BV | 1.53%, uncapped | ÖGK guide §§2.6 and 3.6.4 |
| Vienna Dienstgeberabgabe | EUR 2 per employee per started week | City Vienna **“Dienstgeberabgabe”** and Wiener DGA law §5: [city procedure](https://www.wien.gv.at/amtswege/dienstgeberabgabe), [law](https://www.wien.gv.at/recht/landesrecht-wien/rechtsvorschriften/pdf/f3000000.pdf) |

The annual employer examples use 53 calendar weeks touched by a 1 January–31 December 2026 employment, hence EUR 106 Vienna DGA. The law exempts, among others, employment of at most ten weekly hours and employees over 55; this case assumes neither exemption.

DB, DZ and Kommunalsteuer each have employer-level small-payroll relief when monthly aggregate payroll is no more than EUR 1,460 (EUR 1,095 deduction). Gross salary alone cannot establish it, so the stated employer-wide assumption is necessary. The USP **“Fristen und Fälligkeiten”** table, current 2026, independently lists DB 3.7%, DZ 0.31%–0.40%, and Kommunalsteuer 3% of their bases: [USP](https://www.usp.gv.at/themen/steuern-finanzen/steuerliche-rechte-und-pflichten/weitere-informationen-zu-steuerlichen-rechten-und-pflichten-als-unternehmen/fristen-und-faelligkeiten.html).

## 5. Worked annual calculations

Amounts are mathematical annual results rounded to cents for display. Actual payroll calculates and rounds each pay period, so annual summation can differ by cents.

### 5.1 Employee calculation

| Annual gross `G` | `M=G/14` | Employee regular SV | Employee special SV | Ordinary base `E` | Ordinary tax after credits/refund | Net special base `B` | Special tax | **Total tax** | **Annual cash net** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 1,428.57 | 2,634.86 | 403.43 | 14,376.00 | **−1,132.60** | 2,453.71 | 110.02 | **−1,022.58** | **17,984.29** |
| 60,000 | 4,285.71 | 9,421.71 | 1,463.14 | 41,874.86 | 7,701.14 | 7,108.29 | 389.30 | **8,090.44** | **41,024.70** |
| 100,000 | 7,142.86 | 15,234.91 | 2,365.90 | 70,347.37 | 19,090.15 | 11,919.81 | 677.99 | **19,768.14** | **62,631.05** |
| 200,000 | 14,285.71 | 15,234.91 | 2,365.90 | 156,061.66 | 61,255.65 | 26,205.53 | 1,788.29 | **63,043.94** | **119,355.24** |
| 600,000 | 42,857.14 | 15,234.91 | 2,365.90 | 498,934.19* | 232,691.91 | 83,348.38 | 20,129.35 | **252,821.26** | **329,577.93** |

`Annual cash net = G − employee regular SV − employee special SV − total tax`. Negative total tax at EUR 20,000 is an assessment refund; monthly take-home before assessment is lower. The ordinary negative amount is limited to the calculated negative tax (EUR 1,132.60), even though the potential 2026 SV-refund ceiling is EUR 1,300. The special-payment tax remains payable.

`*` At EUR 600,000, net special payments exceed EUR 83,333 by EUR 15.38; that overflow is included in ordinary base `E`. Fixed special tax exhausts the four statutory bands.

Representative checks:

```text
G=20,000:
M = 1,428.5714; employee AV = 0%
regular SV = 17,142.8571 × 15.37% = 2,634.86
special SV = 2,857.1429 × 14.12% = 403.43
E = 17,142.8571 - 2,634.8571 - 132 = 14,376.00
tariff(E) = (14,376 - 13,539)×20% = 167.40
ordinary result = 167.40 - 496 - 804 = -1,132.60
special tax = (2,453.7143 - 620)×6% = 110.02

G=100,000:
regular SV base = 12×6,930 = 83,160
special SV base = 13,860
regular SV = 83,160×18.32% = 15,234.91
special SV = 13,860×17.07% = 2,365.90
E = 85,714.2857 - 15,234.912 - 132 = 70,347.37
ordinary tax before credit = 19,586.15; less VAB 496 = 19,090.15
special tax = (11,919.8123 - 620)×6% = 677.99.
```

### 5.2 Employer cost

```text
Employer cost = G
 + 21.23%×R + 20.48%×S
 + 1.53%×G (BV)
 + 3.70%×G (DB)
 + 0.36%×G (Vienna DZ)
 + 3.00%×G (Kommunalsteuer)
 + EUR 106 Vienna DGA.
```

| Gross | Employer regular SV | Employer special SV | BV 1.53% | DB 3.70% | DZ 0.36% | Kommunal 3% | Vienna DGA | **Employer cost** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 3,639.43 | 585.14 | 306.00 | 740.00 | 72.00 | 600.00 | 106 | **26,048.57** |
| 60,000 | 10,918.29 | 1,755.43 | 918.00 | 2,220.00 | 216.00 | 1,800.00 | 106 | **77,933.71** |
| 100,000 | 17,655.87 | 2,837.53 | 1,530.00 | 3,700.00 | 360.00 | 3,000.00 | 106 | **129,189.40** |
| 200,000 | 17,655.87 | 2,837.53 | 3,060.00 | 7,400.00 | 720.00 | 6,000.00 | 106 | **237,779.40** |
| 600,000 | 17,655.87 | 2,837.53 | 9,180.00 | 22,200.00 | 2,160.00 | 18,000.00 | 106 | **672,139.40** |

## 6. Calculation order and rounding

1. Divide contractual annual gross into the actual regular and special pay events. A 12-pay contract would produce materially different tax even at the same annual gross.
2. Per month/payment, select the employee AV rate from the **uncapped** gross for that contribution period; regular pay and a special payment are tested separately.
3. Apply regular and special SV ceilings separately. Do not cap BV.
4. Deduct employee SV from its corresponding regular or special pay. Apply EUR 132 to regular annual income.
5. Apply §33 tariff and credits to ordinary income. Apply §67 separately inside the Jahressechstel; move only the statutory overflow to ordinary taxation.
6. Payroll systems round individual contribution and tax lines to euro cents at each pay event. The annual tables above deliberately avoid inventing a single rounding path where bonus payment months and payroll-software sequencing are unspecified; expect cent-level reconciliation differences.

## 7. Material edge cases and boundaries

- The collective agreement can change the number, size and payment date of special payments; annual gross alone is insufficient without the 14-pay convention.
- If holiday and Christmas payments are combined in one contribution period, low-income AV testing can differ. Here they are paid separately.
- A new employment makes the first BV month generally contribution-free; an old “Abfertigung” employment can fall outside BMSVG. This case is a continuing post-2002/private employment.
- Place of work changes WF and DZ. Outside Vienna, WF is generally 0.50% each; every state has its own 2026 DZ. Vienna was selected explicitly.
- Employers/persons qualifying for DB/DZ/Kommunal small-payroll relief, new-business relief, age exemptions, or Vienna DGA exemptions need different employer cost.
- Multiple employments, partial year, unpaid leave, benefits, overtime, termination payments and expenses require pay-period recomputation and often annual assessment.
- Employee assessment is necessary to realise the 2026 VAB surcharge/SV refund in the low-income example.
- No family-related credit is available under the stated no-child facts.

## 8. Evidence assessment

**Strongest evidence:** effective-2026 RIS §§33 and 67; ÖGK's 156-page 2026 employer/payroll guide, which directly states the rates, ceilings, separate special-payment base and low-income AV mechanics; and City Vienna's explicit 2026 0.75% WF page.

**Weakest / assumption-sensitive evidence:** the contractually determined 13th/14th entitlement and timing, employer-level small-payroll relief, first-month BV status, and whether a Vienna DGA exemption applies cannot be derived from annual gross. The dossier resolves them with explicit reproducible assumptions. Cent-perfect payroll withholding remains unresolved without exact payment dates and payroll rounding configuration; the annual statutory liability and employer-cost arithmetic are shown before that implementation-level variance.
