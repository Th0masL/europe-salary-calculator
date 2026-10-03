# Finland employee salary and payroll calculation, tax year 2026

**Independent research dossier — accessed 2026-10-04.** This reconstruction uses only primary Finnish public-sector sources: Finlex, the Finnish Tax Administration (Vero), the Finnish Centre for Pensions / Työeläke.fi, the Employment Fund, Statistics Finland, the Workers’ Compensation Center, and the City of Helsinki. It was prepared without consulting the repository's Finland calculator, generated datasets, Finland calculation documentation, or any prior audit.

## Scope and modelling assumptions

The worked cases are for a Finnish-resident employee who is:

- 30 years old throughout 2026 (therefore inside every relevant insurance age range);
- single, with no children, no church membership and no capital or other earned income;
- in ordinary private-sector TyEL employment, not a part-owner, seafarer or posted worker;
- paid regular cash salary evenly over 12 months and covered by Finnish social insurance;
- resident in **Helsinki**, whose enacted 2026 municipal income-tax rate is **5.30%**;
- claiming no itemised expenses, commuting deduction, unemployment-fund dues or other personal deductions, so only automatic deductions apply.

Helsinki is a deliberate, reproducible municipality assumption—not a national average. The City Council fixed 5.30% on 5 November 2025; the decision was published 12 November 2025. Vero separately publishes 7.60% as the statutory *average municipal rate used for non-residents*, but that is not a resident's municipality rate and is not used here.

All figures below are annual mathematical results rounded to cents at presentation. Exact tax-assessment and tax-card rounding conventions were not established from a sufficiently clear primary source; production results may therefore differ by a small rounding amount.

## Employee calculation rules

Let annual gross cash salary be `G`.

### 1. Contributions withheld from salary

| Item | 2026 rule | Base / condition |
|---|---:|---|
| Employee TyEL | 7.30% | Gross TyEL earnings. Same employee rate for all ages in 2026. TyEL begins from the month after age 17, applies at monthly earnings of at least €71.72, and ends at 69 for persons born 1958–1961 or 70 for persons born in/after 1962. No annual earnings cap was found. |
| Employee unemployment insurance | 0.89% | Gross covered pay. Applies from age 18 through age 64 (person has turned 18 and is under 65). No individual earnings cap was found. |
| Health-insurance daily-allowance contribution | 0.88% | If annual wage and entrepreneurial income is at least €17,255, 0.88% applies to the **entire** base, including the part below the threshold; otherwise zero. Applies to ages 16–67. |

For every worked salary (`G >= €20,000`):

```text
TyEL_employee = 0.0730 × G
UI_employee   = 0.0089 × G
Daily_allowance = 0.0088 × G
```

The Finnish Tax Administration's detailed guidance states that statutory employee pension, unemployment-insurance and health-insurance daily-allowance contributions are deductions from net earned income (Income Tax Act section 96). They are nevertheless actual employee cash charges as shown above.

### 2. Income-acquisition deduction and taxable earned income

The automatic deduction for the production/acquisition of wage income is €750, but never more than wage income. It is a “natural deduction” and is applied in both state and municipal assessment.

```text
Income_acquisition = min(G, 750)
Pure_earned_income P = G - Income_acquisition

Pre_basic_base A = max(0,
    P - TyEL_employee - UI_employee - Daily_allowance)
```

The 2026 basic allowance is made in both state and municipal taxation after the other income deductions:

```text
if A <= 4,265: Basic = A
else:          Basic = max(0, 4,265 - 0.18 × (A - 4,265))

Taxable_earned_income T = A - Basic
```

Vero says no partial basic allowance remains above approximately €27,959. The algebraic formula reaches zero at €27,959.44; the stated €27,959 cut-off should govern an assessment implementation rather than inferring extra precision.

### 3. State income tax before credits

Finlex Act 1140/2025, section 1, enacted 5 December 2025, published 11 December 2025 and effective 1 January 2026, provides:

| Taxable earned income `T` | Tax at lower limit | Rate on excess |
|---:|---:|---:|
| €0–€22,000 | €0.00 | 12.64% |
| €22,000–€32,600 | €2,780.80 | 19.00% |
| €32,600–€40,100 | €4,794.80 | 30.25% |
| €40,100–€52,100 | €7,063.55 | 33.25% |
| over €52,100 | €11,053.55 | 37.50% |

Thus, for example, above €52,100: `State_raw = 11,053.55 + 0.375 × (T - 52,100)`.

### 4. Municipal tax and health-care contribution before credits

```text
Municipal_raw = 0.0530 × T          # Helsinki 2026
Health_care_raw = 0.0110 × T
```

The insured person's health-care contribution is 1.10% of income taxable in municipal taxation. Government Decree 1026/2025 was published 25 November 2025 and is effective for calendar year 2026. It also fixes the daily-allowance and employer health-insurance rates used in this dossier.

### 5. Employment-income credit (työtulovähennys)

For an under-65 employee with no qualifying children, Vero's detailed guidance issued 15 January 2026 gives:

```text
Credit_before_taper = min(0.18 × G, 3,430)
Taper = 0.02 × min(max(P - 35,000, 0), 50,550 - 35,000)
Employment_credit = max(0, Credit_before_taper - Taper)
```

The credit is first deducted from state earned-income tax. Any excess is deducted proportionally from municipal tax, the health-care contribution and church tax. Church tax is zero under the assumptions.

Important evidence conflict: Vero's shorter English “automatic deductions” page displayed older-looking 2%/3.44% taper text involving €42,550 when accessed. The later, tax-year-specific Finnish detailed guidance (record VH/271/00.01.00/2026, issued and effective 15 January 2026) unambiguously says the 2026 reduction is **2% of pure earned income from €35,000 through €50,550 and stops increasing thereafter**, and gives worked examples. This dossier follows that stronger source. A production implementation should not import the English summary's stale taper.

### 6. Public broadcasting tax

For a mainland resident aged at least 18 with no capital/YEL/MYEL income:

```text
YLE_tax = min(160, 0.025 × max(P - 15,150, 0))
```

The base is *pure earned income*: wage income after natural deductions such as the €750 income-acquisition deduction. Vero expressly says employee pension contributions are **not** natural deductions for this purpose. Employment-income credit does not reduce YLE tax. The €160 maximum is reached at roughly €22,300 of gross wage under these assumptions.

### 7. Net cash formula

```text
Income_tax_and_health = State_after_credit
                      + Municipal_after_credit
                      + Health_care_after_credit
                      + Daily_allowance
                      + YLE_tax

Net_cash = G - TyEL_employee - UI_employee - Income_tax_and_health
```

## Employer contributions

The legal obligation must be separated from the rate assumption:

| Employer item | 2026 value used | Status |
|---|---:|---|
| TyEL | 17.10% | **Average**, not a universal statutory employer rate. The average total TyEL charge is 24.40%, of which the employee pays 7.30%. Actual employer cost varies with insurer, client bonuses/administration, employer size and disability experience. |
| Employer health insurance | 1.91% | Fixed statutory rate on covered wages; for employees aged 16–67 and insured under the Finnish system. |
| Employer unemployment insurance | 0.31% | Statutory rate up to employer-wide annual payroll of €2,509,500; 1.23% on payroll above that threshold. The worked cases assume the employer's **total** payroll remains at or below the threshold. Employer payment liability begins when total calendar-year wages exceed €1,500; covered employee age is 18–64. |
| Occupational accident/disease insurance | 0.51% | **Statistics Finland 2026 average**, not a fixed tariff. Actual rate varies by work risk and insurer. Insurance is obligatory when employer-wide annual wages exceed €1,500; TVK says there is no employee-age or individual minimum/maximum earnings limit. |
| Group life insurance | 0.06% | **Statistics Finland 2026 average**, not a fixed tariff. Required where the applicable collective agreement requires it; varies by insurer/sector. |

The illustrative employer load is therefore `17.10% + 1.91% + 0.31% + 0.51% + 0.06% = 19.89%`, and illustrative total employer cost is `1.1989 × G`. Only the 1.91% health rate and the applicable unemployment rate are fixed in that combined number; the TyEL, accident and group-life entries are averages.

There is no defensible single “statutory employer percentage” for Finland because several mandatory coverages are experience-, insurer-, risk-, sector- or payroll-dependent.

## Independent worked calculations

### Employee-side intermediate values

| Gross `G` | Pure earned `P` (`G−750`) | TyEL 7.30% | UI 0.89% | Daily 0.88% | Before basic `A` | Basic allowance | Taxable `T` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| €20,000.00 | €19,250.00 | €1,460.00 | €178.00 | €176.00 | €17,436.00 | €1,894.22 | €15,541.78 |
| €60,000.00 | €59,250.00 | €4,380.00 | €534.00 | €528.00 | €53,808.00 | €0.00 | €53,808.00 |
| €100,000.00 | €99,250.00 | €7,300.00 | €890.00 | €880.00 | €90,180.00 | €0.00 | €90,180.00 |
| €200,000.00 | €199,250.00 | €14,600.00 | €1,780.00 | €1,760.00 | €181,110.00 | €0.00 | €181,110.00 |
| €600,000.00 | €599,250.00 | €43,800.00 | €5,340.00 | €5,280.00 | €544,830.00 | €0.00 | €544,830.00 |

At €20,000, for example, `A = 20,000 − 750 − 1,460 − 178 − 176 = 17,436`; `Basic = 4,265 − 18% × (17,436 − 4,265) = 1,894.22`; hence `T = 15,541.78`.

### Taxes, credits and employee net cash

| Gross | State raw | Helsinki raw | Health raw | Employment credit | State after credit | Helsinki after credit | Health after credit | YLE | Daily | Total tax/health | Net cash |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| €20,000.00 | €1,964.48 | €823.71 | €170.96 | €3,430.00 | €0.00 | €0.00 | €0.00 | €102.50 | €176.00 | €278.50 | **€18,083.50** |
| €60,000.00 | €11,694.05 | €2,851.82 | €591.89 | €3,119.00 | €8,575.05 | €2,851.82 | €591.89 | €160.00 | €528.00 | €12,706.76 | **€42,379.24** |
| €100,000.00 | €25,333.55 | €4,779.54 | €991.98 | €3,119.00 | €22,214.55 | €4,779.54 | €991.98 | €160.00 | €880.00 | €29,026.07 | **€62,783.93** |
| €200,000.00 | €59,432.30 | €9,598.83 | €1,992.21 | €3,119.00 | €56,313.30 | €9,598.83 | €1,992.21 | €160.00 | €1,760.00 | €69,824.34 | **€113,795.66** |
| €600,000.00 | €195,827.30 | €28,875.99 | €5,993.13 | €3,119.00 | €192,708.30 | €28,875.99 | €5,993.13 | €160.00 | €5,280.00 | €233,017.42 | **€317,842.58** |

At €20,000, the credit first eliminates €1,964.48 of state tax. The remaining €1,465.52 is larger than Helsinki tax plus health care (€994.67), so both are fully eliminated; €102.50 YLE tax and €176 daily-allowance contribution remain. Net cash is `20,000 − 1,460 − 178 − 278.50 = 18,083.50`.

At €60,000 and above, `P` exceeds €50,550, so the credit is `€3,430 − 2% × (€50,550 − €35,000) = €3,119`; state tax is sufficient to absorb it, leaving municipal and health charges unreduced.

### Illustrative employer cost (using explicitly labelled averages)

| Gross | TyEL avg 17.10% | Health 1.91% | UI 0.31% | Accident avg 0.51% | Group life avg 0.06% | Employer add-ons | Total employer cost |
|---:|---:|---:|---:|---:|---:|---:|---:|
| €20,000.00 | €3,420.00 | €382.00 | €62.00 | €102.00 | €12.00 | €3,978.00 | **€23,978.00** |
| €60,000.00 | €10,260.00 | €1,146.00 | €186.00 | €306.00 | €36.00 | €11,934.00 | **€71,934.00** |
| €100,000.00 | €17,100.00 | €1,910.00 | €310.00 | €510.00 | €60.00 | €19,890.00 | **€119,890.00** |
| €200,000.00 | €34,200.00 | €3,820.00 | €620.00 | €1,020.00 | €120.00 | €39,780.00 | **€239,780.00** |
| €600,000.00 | €102,600.00 | €11,460.00 | €1,860.00 | €3,060.00 | €360.00 | €119,340.00 | **€719,340.00** |

These employer totals are scenarios, not employee-specific legal liabilities. If the employer's aggregate payroll crosses €2,509,500, the excess attracts 1.23% unemployment insurance. Actual TyEL, accident and group-life invoices must replace the averages.

## Primary sources and evidence register

All were accessed **2026-10-04**.

1. **Finlex, “Laki vuoden 2026 tuloveroasteikosta” (Act 1140/2025), section 1.** Enacted 2025-12-05; published 2025-12-11; effective 2026-01-01. Exact five state brackets and rates. <https://www.finlex.fi/fi/lainsaadanto/2025/1140>
2. **Finnish Tax Administration, “Verotettavan tulon laskeminen henkilöverotuksessa” (Calculation of taxable income in individual taxation), VH/271/00.01.00/2026.** Issued/effective 2026-01-15. Pinpoints: paragraphs/lines corresponding to sections 2.2–2.3 (automatic €750 natural deduction and pure earned income), 3.1.2 (employee pension, unemployment and daily-allowance contributions deductible under Income Tax Act section 96), 3.9 (€4,265 basic allowance and 18% withdrawal), and 5.2 (€3,430 employment credit, 18% accrual, 2% taper from €35,000 to €50,550, ordering/allocation). <https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/49038/verotettavan-tulon-laskeminen-henkiloverotuksessa9/>
3. **Finnish Tax Administration, “Tax bases 2026.”** Updated 2025-11-22. Pinpoints 1.10% health care; 0.88% daily allowance at/above €17,255 (zero below); YLE 2.50%, €15,150 threshold and €160 maximum. <https://www.vero.fi/en/individuals/tax-cards-and-tax-returns/tax_card/tax-rate-and-income-ceiling/tax-bases/>
4. **Finlex, Government Decree 1026/2025, “Valtioneuvoston asetus sairausvakuutusmaksujen maksuprosenteista vuonna 2026.”** Published 2025-11-25; effective 2026-01-01 through 2026-12-31. Sections 1–3: employee health 1.10%, daily allowance 0.88% with €17,255 all-or-nothing threshold, employer health 1.91%. <https://www.finlex.fi/api/media/statute/893094/mainPdf/main.pdf?timestamp=2025-11-25T08%3A00%3A00.000Z>
5. **Finnish Tax Administration, “Vakuutetun sairausvakuutusmaksu” (Insured person's health-insurance contribution), VH/7273/00.01.00/2025.** Issued 2025-12-18; effective 2026-01-01. Confirms 2026 rates, municipal-taxable-income health base, credit allocation, and that no health-care contribution remains if municipal taxable earned income is zero after deductions. <https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/338472/vakuutetun-sairausvakuutusmaksu2/>
6. **Finnish Tax Administration, “Yleisradiovero” (Public broadcasting tax), VH/6321/00.01.00/2024.** Issued 2024-12-13; effective 2025-01-01 until further notice. Sections 2.1–2.2: adult/mainland scope, 2.5% of pure income exceeding €15,150, €160 maximum, and explicit classification of the €750 wage deduction—but not employee pension contributions—as a natural deduction. <https://www.vero.fi/syventavat-vero-ohjeet/ohje-hakusivu/48391/yleisradiovero5/>
7. **City of Helsinki, “Tuloveroprosentti 2026,” City Council item 5/§261.** Decision 2025-11-05; published 2025-11-12. Exact 2026 municipal rate: 5.30%. <https://paatokset.hel.fi/fi/asia/hel-2025-016033>
8. **Finnish Tax Administration, “Kuntien ja seurakuntien tuloveroprosentit vuonna 2026,” VH/6585/00.01.00/2025.** Issued/updated 2025-11-18; effective 2026-01-01. Confirms official municipal/parish rate list and 7.60% average rate for the statutory non-resident rule. <https://www.vero.fi/syventavat-vero-ohjeet/paatokset/47465/kuntien-ja-seurakuntien-tuloveroprosentit-vuonna-2026/>
9. **Finnish Centre for Pensions, “Pension Contributions.”** Current 2026 table: private-sector TyEL total average 24.40%, employee share 7.30%. The page also cautions that exact collected rates depend on the pension act and become known after realised reporting. <https://www.etk.fi/en/finnish-pension-system/financing-and-investments/pension-contributions/>
10. **Työeläke.fi / Finnish Centre for Pensions, “Employers arrange pension insurance.”** Updated 2026-09-18. Exact €71.72 monthly threshold, start after age 17, birth-year-specific upper ages, and private-sector TyEL scope. <https://www.tyoelake.fi/en/employers-obligations/employers-arrange-pension-insurance/>
11. **Finnish Centre for Pensions, “Private sector.”** Current 2026 detail: 24.85% basic contract-employer contribution before provider-specific administration/client-bonus effects; employee share 7.30 points; employer outcome varies, and employer-contract threshold is €10,272 over six months. This supports treating 17.10% as an average rather than a universal tariff. <https://www.etk.fi/en/finnish-pension-system/financing-and-investments/pension-contributions/private-sector/>
12. **Employment Fund, “Payment of the unemployment insurance contribution.”** Current 2026 table/section: employee 0.89%; employer 0.31% through €2,509,500 aggregate payroll and 1.23% above; special part-owner/state/university rates separately stated. <https://www.tyollisyysrahasto.fi/en/Unemploymentinsurancecontribution/paying-unemployment-insurance-contributions/>
13. **Employment Fund, “Unemployment insurance contribution.”** Current page: employer liability above €1,500 annual total wages and employee age condition (turned 18, under 65). <https://www.tyollisyysrahasto.fi/en/Unemploymentinsurancecontribution/>
14. **Finnish Tax Administration, “Social insurance contributions.”** Updated 2025-12-08. Consolidated 2026 employer/employee table and conditions: employer health 1.91%; average employer TyEL 17.10%; unemployment rates/thresholds; accident and group-life variability; relevant age conditions. <https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/being-an-employer/social-insurance-contributions/>
15. **Statistics Finland, “Quarterly statistics on labour costs — Instructions for responding: Social insurance contribution percentages for 2026.”** 2026 publication. Page 2: employer pension average 17.10%, health 1.91%, unemployment tiers, accident average 0.51%; page 3: group-life average 0.06%; page 4 expressly directs enterprises to use their own percentages instead of averages when known. <https://media.stat.fi/A7H6ohk0S8qafyCM4bfDaz/cmnrl2zjz1iop07vy2x5yju1t>
16. **Workers’ Compensation Center (TVK), “Taking out Workers’ Comp insurance policy.”** Current page. Confirms compulsory coverage, employer-wide wage threshold, risk information used to price the premium, no employee-age or individual earnings bounds, and group life where a collective agreement requires it. <https://www.tvk.fi/en/insurance/taking-out-an-insurance-policy/>

## Unresolved or implementation-sensitive points

- **Assessment rounding:** the sources above establish formulas and rates, but not a complete machine-level sequence for rounding every annual intermediate. The worked figures retain precision and round only for display.
- **TyEL employer rate:** 17.10% is an official 2026 average, not a rate that can be guaranteed for any employer. An insurer quote or employer-specific percentage is required for exact payroll cost.
- **Accident and group-life rates:** 0.51% and 0.06% are official Statistics Finland averages. Actual insurance/collective-agreement facts are required. Group life is not universally mandatory absent an applicable agreement.
- **Employer unemployment tier:** it depends on whole-employer payroll, not this employee's salary. The examples assume the low tier; an individual gross salary cannot establish the employer's tier.
- **Age and partial-year cases:** the model fixes age 30. Turning an insurance boundary age, starting/ending work mid-month, or pay falling below TyEL's monthly threshold requires period-level logic not represented by an annual scalar.

## Evidence assessment

The strongest evidence is the enacted Finlex state scale; Government Decree 1026/2025; Vero's tax-year-specific detailed calculation guidance; the City of Helsinki decision; and the 2026 rate pages of ETK and the Employment Fund. These directly establish the formulas and effective dates.

The weakest inputs are necessarily the employer accident and group-life percentages and the employer TyEL percentage, because the primary sources themselves identify them as averages or variable rates. They are appropriate only for an illustrative employer-cost estimate. The remaining minor uncertainty is exact administrative rounding, explicitly excluded from the mathematical reconstruction.
