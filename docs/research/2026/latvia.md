# Latvia employee salary and payroll rules — tax year 2026

Research status: **independent clean-room reconstruction from Latvian official sources**.  
Access date for every web source: **2026-10-04**.

## Scope and calculation assumptions

This dossier models a Latvian tax resident who is:

- single, with no dependants and no other personal allowances;
- below Latvian pension age and insured for all standard social-insurance risks;
- employed continuously for all 12 months by one ordinary private-sector employer;
- paid an even monthly salary consisting only of regular cash employment income;
- in possession of a payroll tax booklet submitted to that employer; and
- not receiving pension, self-employment, foreign, exempt, capital, or other income.

The examples therefore apply the standard employee/employer social-insurance rates, the full fixed non-taxable minimum at payroll, no church-like or local tax, and the entrepreneurship-risk state fee. Latvia has no municipal payroll income tax comparable to systems in which the municipality chooses the employee's rate.

Amounts are calculated annually and shown to cents. Actual payroll systems calculate and round monthly, so a production result can differ by cents. The dossier distinguishes (a) cash collected during the year from (b) the final allocation and employer refund after solidarity-tax reconciliation.

## 1. Personal income tax (PIT)

### 1.1 Rates and annual reconciliation

For 2026, the ordinary progressive rates on annual taxable income are:

| Annual taxable income | Rate |
|---|---:|
| Up to and including €105,300 | 25.5% |
| Amount over €105,300 | 33% |

The employer withholds **25.5% monthly** from salary income after payroll deductions. The 33% band is settled through the annual income declaration rather than through a second monthly payroll band.

A separate **additional 3% tax** applies to the part of the statutory aggregate annual income base exceeding **€200,000**. Under the salary-only assumptions here, that base is gross salary, so the additional tax is `3% × max(gross salary − €200,000, 0)`. It is an annual-return item and is zero at exactly €200,000.

Official support:

- State Revenue Service (VID), [“Personal Income Tax Rates”](https://www.vid.gov.lv/en/personal-income-tax-rates), published 2022-10-19, updated 2025-12-30: table rows “Annual taxable income up to EUR 105 300 — 25.5%” and “part ... exceeding EUR 105 300 — 33%”; the same page states that 25.5% is applied monthly and identifies the additional 3% rate above €200,000.
- [Law “On Personal Income Tax”](https://likumi.lv/ta/id/56880-iedzivotaju-ienakuma-nodokla-likums) (*Par iedzīvotāju ienākuma nodokli*), consolidated text applicable in 2026: Section 15 contains the 25.5% and 33% annual rates; Section 15.1, effective 2026-01-01 in the displayed consolidation, imposes the additional 3% on the specified annual income aggregate over €200,000. Section 1 describes salary/advance payments followed by annual assessment and treats the solidarity-tax amount allocated to PIT as PIT paid.
- VID, [“Obligāti iesniedzamā gada ienākumu deklarācija”](https://www.vid.gov.lv/lv/obligati-iesniedzama-gada-ienakumu-deklaracija) (“Mandatory annual income declaration”), updated 2026-02-11: the 2026 section repeats the 25.5%/33% threshold and fixed minimum, identifies the 3% tax, and says persons whose annual income exceeds €105,300 submit between 1 April and 1 July of the following year.

The annual return reconciles final PIT against salary tax withheld and the PIT share of solidarity tax. Consequently, an employee above €105,300 can have either tax payable or a refund even though payroll correctly withheld 25.5% each month.

### 1.2 Fixed non-taxable minimum

The 2026 non-taxable minimum is:

- **€550 per month**; and
- **€6,600 per year**.

It is no longer income-tested. An employer applies it only when the employee has submitted the payroll tax booklet to that employer. If it was not used in payroll, a resident can claim the unused amount in the annual declaration.

Official support:

- VID, [“Personal Income Tax”](https://www.vid.gov.lv/en/personal-income-tax), updated 2026-05-06, heading “Non-taxable minimum”: €550 per month and €6,600 per year for 2026 and the payroll-tax-booklet condition.
- VID, [“Neapliekamais minimums”](https://www.vid.gov.lv/lv/neapliekamais-minimums) (“Non-taxable minimum”), current 2026 page: the 2026 table gives €550 monthly/€6,600 annually and explains recovery of an unused minimum by annual declaration.

### 1.3 Deduction order

For the assumed employee, the ordinary annual PIT base starts with gross employment income and subtracts:

1. the employee's deductible compulsory social contributions, adjusted for the solidarity-tax PIT allocation; then
2. the €6,600 annual non-taxable minimum.

The PIT law's Section 3 defines taxable income as gross income reduced by eligible expenses, the annual/monthly non-taxable minimum, and allowances. Section 10 lists compulsory social contributions among eligible expenses. Section 10(1.10) requires the reported social-contribution deduction to be reduced by the part of solidarity tax transferred to the PIT distribution account.

The operational annual-declaration instructions confirm both sides of this treatment: employee VSAOI on the employment schedule is reduced by the solidarity amount allocated to PIT, while that allocated amount is also reported as PIT paid in advance. See Cabinet Regulation No. 662, [“Noteikumi par iedzīvotāju ienākuma nodokļa deklarācijām un to aizpildīšanas kārtību”](https://likumi.lv/ta/id/302688-noteikumi-par-iedzivotaju-ienakuma-nodokla-deklaracijam-un-to-aizpildisanas-kartibu) (“Rules on personal income tax declarations and completion”), adopted 2018-10-30, effective 2018-11-03, current consolidation effective 2025-10-24 and applicable to 2026; points 39.6–39.7 and form D lines 6, 7, and 23 subtract the solidarity PIT allocation from the VSAOI deduction and add the same amount to PIT paid in advance.

This adjustment is essential above €105,300. Deducting the full 10.5% employee cash withholding *and* crediting the 10% solidarity allocation as PIT would double-count the same excess-income amount.

The deductions are allocated to the lower-rate income first, rather than shifting the progressive threshold downward. Section 3(2.4) of the PIT law directs deductions to income up to the social maximum and only carries them into excess income if the lower portion is insufficient. A particularly strong computational cross-check is Cabinet Regulation No. 790, [“Grozījumi Ministru kabineta 2010. gada 21. septembra noteikumos Nr. 899 ‘Likuma ‘Par iedzīvotāju ienākuma nodokli’ normu piemērošanas kārtība’”](https://likumi.lv/ta/id/365322) (“Amendments to Cabinet Regulation No. 899”), adopted 2025-12-16, published 2025-12-22, effective 2025-12-23. Annex 4.5's €120,000 example assigns the entire €14,700 gross excess to the 33% band and obtains the €88,050 lower-band base after employee VSAOI, the solidarity adjustment, and the annual minimum. Its displayed parenthetical sign is typographically ambiguous, but the stated €88,050 result unambiguously equals `€105,300 − (€12,600 − €1,470) − €6,120`.

## 2. Mandatory state social insurance contributions (VSAOI)

### 2.1 Standard employee and employer rates

For an ordinary employee insured for all risks in 2026:

| Payer | Rate |
|---|---:|
| Employee (withheld from gross salary) | 10.50% |
| Employer | 23.59% |
| Combined cash collection rate | 34.09% |

The contribution object is employment income subject to PIT, before application of the non-taxable minimum, allowances, or other PIT deductions.

Official support:

- State Social Insurance Agency (VSAA), [“Par iemaksām”](https://www.vsaa.gov.lv/lv/par-iemaksam) (“About contributions”), published 2020-11-20, updated 2025-12-23: “34,09%”, split “23,59%” employer and “10,50%” employee; it also defines the contribution object as all calculated employment income from which PIT must be withheld, without deducting the non-taxable minimum, reliefs, or eligible expenses.
- VID, [“Valsts sociālās apdrošināšanas obligāto iemaksu likmes”](https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligato-iemaksu-likmes) (“Mandatory state social-insurance contribution rates”), updated 2026-09-02: the 2026 ordinary all-risks row repeats 34.09%, 23.59%, and 10.50%.
- VID, [“Mandatory State Social Insurance Contributions”](https://www.vid.gov.lv/en/mandatory-state-social-insurance-contributions), current 2026 English overview: standard-rate split and contribution-base explanation.

VSAA's same page states that employees are socially insured from age 15. The standard all-risks row used here is for an employee who has not reached the age giving entitlement to the state old-age pension (including early retirement). Rates are lower/differently composed for a pension-age employee and certain other insured statuses; those variants are outside the assumptions and must not be treated as universal. The exact pension-age determination is therefore an input/status test, not a universal hard-coded age in this dossier.

### 2.2 Maximum contribution object and collection above it

The annual maximum mandatory social-insurance contribution object is **€105,300 for 2026**. Importantly, this is **not a payroll cash-withholding stop**. Contributions continue to be calculated at 10.50% employee and 23.59% employer on pay above €105,300; the excess-income collection is then treated and reconciled as solidarity tax.

VSAA, [“Par iemaksām”](https://www.vsaa.gov.lv/lv/par-iemaksam), updated 2025-12-23, heading concerning the maximum object, gives €105,300 for 2026 and states that contributions calculated above the maximum become solidarity tax.

There is also a minimum contribution object of **€780 per month / €2,340 per quarter** in 2026, with employer top-up procedures in relevant low-income cases. All five examples exceed it in every month, so it has no numerical effect here. This is documented by VID, [“Mandatory State Social Insurance Contributions”](https://www.vid.gov.lv/en/mandatory-state-social-insurance-contributions), current 2026 overview, section on minimum mandatory contributions.

## 3. Solidarity tax above €105,300

### 3.1 Collection, final rate, refund, and allocation

Let `E = max(gross − €105,300, 0)`.

During the year, the normal combined VSAOI rate of **34.09%** is collected on `E`. The final solidarity-tax rate for 2026 is **25%**, allocated as:

| Final allocation | Rate on E |
|---|---:|
| Health-care financing | 1% |
| State pension special budget | 14% |
| Personal income tax revenue | 10% |
| **Total final solidarity tax** | **25%** |

The collection excess is `34.09% − 25% = 9.09% of E`. VSAA calculates the overpayment by 1 June of the following year and VID refunds it by 1 September. Where ordinary contributions are split between employee and employer, the governing law directs this refund **only to the employer**. Thus:

- the employee's cash withholding remains 10.50% of all gross salary;
- the employer initially pays 23.59% of all gross salary;
- the employer later receives 9.09% of `E`;
- the employer's final burden above the cap is therefore 14.50% of `E`;
- together with the employee's 10.50%, final solidarity tax is 25% of `E`; and
- 10% of `E` is credited to the employee as PIT paid in advance and removed from the employee-social-contribution deduction on the annual return.

Official support:

- VID, [“Solidaritātes nodoklis”](https://www.vid.gov.lv/lv/solidaritates-nodoklis) (“Solidarity tax”), published 2022-09-23, updated 2026-07-11: €105,300 maximum for 2025–2027; 25% solidarity rate; collection at the VSAOI rate; next-year 1 June calculation and 1 September refund; and allocation of 1%, 14%, and 10%.
- [Solidarity Tax Law](https://likumi.lv/ta/id/278636-solidaritates-nodokla-likums) (*Solidaritātes nodokļa likums*), consolidated text applicable in 2026: Sections 3–5 define taxpayers, object, and calendar-year period; Section 6.1 gives 25%; Section 6.2 governs collection and overpayment, with subsection (3) directing the refund only to the employer where the statutory contribution rate is divided between employer and employee.
- VID, [“Valsts sociālās apdrošināšanas obligātās iemaksas”](https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligatas-iemaksas) (“Mandatory state social-insurance contributions”), current 2026 overview: states that 10% of the amount over the maximum is transferred as a PIT advance.
- [Law “On Personal Income Tax”](https://likumi.lv/ta/id/56880-iedzivotaju-ienakuma-nodokla-likums), Section 1 and Section 10(1.10): the 10% solidarity allocation is PIT paid, and the social-contribution deduction is correspondingly reduced.

### 3.2 Why employee net pay and employer cost use different solidarity presentations

The employee does not receive the 9.09% reconciliation refund. Employee cash social withholding remains 10.5% of gross, while the 10% allocation is a PIT prepayment used in the annual assessment. Employer cost can therefore be shown two ways:

- **cash-year cost:** gross + 23.59% of gross + risk fee; and
- **final post-reconciliation cost:** cash-year cost − 9.09% of salary above €105,300.

## 4. Employer-only entrepreneurship-risk state fee

For an ordinary employer covered by the employee-claim guarantee/insolvency regime, the 2026 entrepreneurship-risk state fee is **€0.36 per employee per month**, or **€4.32 for 12 continuous months**. It is employer-only and is not withheld from salary.

Official support:

- VID, [“Uzņēmējdarbības riska valsts nodeva”](https://www.vid.gov.lv/lv/uznemejdarbibas-riska-valsts-nodeva) (“Entrepreneurship-risk state fee”), published 2022-09-28, updated 2026-03-09: scope and employer payment rules.
- VID, [official information material on the 2026 risk fee](https://www.vid.gov.lv/lv/media/32399/download?attachment=), published 2025-11-06: identifies Cabinet Regulation No. 651, adopted 2025-11-04, published 2025-11-05, effective 2026-01-01, and specifies €0.36 per employee per month.

Applicability can depend on the employer's legal status and insolvency-law coverage. The worked examples assume an ordinary covered Latvian private company.

## 5. Formula used for the worked examples

Let:

- `G` = annual gross salary;
- `C` = €105,300 social maximum/PIT band threshold;
- `E = max(G − C, 0)`;
- `S_cash = 10.5% × G` = employee social amount withheld in cash;
- `SP = 10% × E` = solidarity-tax amount allocated as PIT advance;
- `D = S_cash − SP` = employee social deduction allowed in the annual PIT calculation;
- `M = €6,600` = annual non-taxable minimum;
- `Q = D + M` = deductions allocated first to the gross-income portion at or below `C`;
- `L = max(min(G, C) − Q, 0)` = 25.5% PIT base;
- `R = max(Q − min(G, C), 0)` = any deductions left after exhausting the lower portion;
- `H = max(E − R, 0)` = 33% PIT base;
- `T = L + H` = total ordinary PIT taxable base;
- `P = 25.5% × L + 33% × H` = ordinary annual PIT;
- `X = 3% × max(G − €200,000, 0)` = additional annual tax;
- `W = 25.5% × max(G − S_cash − M, 0)` = twelve months of regular payroll PIT withholding under the stated assumptions; and
- `B = P + X − W − SP` = annual return balance, positive if payable and negative if refundable.

Employee net cash after annual reconciliation is:

`Net = G − S_cash − W − B = G − S_cash − (P + X) + SP`.

Employer amounts are:

- initial employer VSAOI/solidarity cash payment `23.59% × G`;
- next-year employer refund `9.09% × E`;
- final employer social/solidarity burden `23.59% × G − 9.09% × E`; and
- final employer cost `G + final employer burden + €4.32`.

No separate employer payroll tax was found for an ordinary private-sector employer beyond employer VSAOI/solidarity collection and the entrepreneurship-risk fee under these assumptions.

## 6. Independent worked calculations

### 6.1 Employee annual calculation

| Gross G | Employee social cash 10.5% | Excess E | Solidarity PIT advance SP (10% E) | Deductible social D | PIT bases L / H | Ordinary PIT P | Extra 3% X | Payroll PIT W | Annual balance B | Final employee net |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| €20,000.00 | €2,100.00 | €0.00 | €0.00 | €2,100.00 | €11,300.00 / €0.00 | €2,881.50 | €0.00 | €2,881.50 | €0.00 | €15,018.50 |
| €60,000.00 | €6,300.00 | €0.00 | €0.00 | €6,300.00 | €47,100.00 / €0.00 | €12,010.50 | €0.00 | €12,010.50 | €0.00 | €41,689.50 |
| €100,000.00 | €10,500.00 | €0.00 | €0.00 | €10,500.00 | €82,900.00 / €0.00 | €21,139.50 | €0.00 | €21,139.50 | €0.00 | €68,360.50 |
| €200,000.00 | €21,000.00 | €94,700.00 | €9,470.00 | €11,530.00 | €87,170.00 / €94,700.00 | €53,479.35 | €0.00 | €43,962.00 | **€47.35 payable** | €134,990.65 |
| €600,000.00 | €63,000.00 | €494,700.00 | €49,470.00 | €13,530.00 | €85,170.00 / €494,700.00 | €184,969.35 | €12,000.00 | €135,252.00 | **€12,247.35 payable** | €389,500.65 |

Checks on the two high-income rows:

- At €200,000: `D = €21,000 − €9,470 = €11,530`; lower-band base `L = €105,300 − €11,530 − €6,600 = €87,170`; upper-band base `H = €94,700`; `P = 25.5% × €87,170 + 33% × €94,700 = €53,479.35`; advances are `€43,962 + €9,470`, leaving €47.35 payable.
- At €600,000: `D = €63,000 − €49,470 = €13,530`; `L = €105,300 − €13,530 − €6,600 = €85,170`; `H = €494,700`; `P = 25.5% × €85,170 + 33% × €494,700 = €184,969.35`; `X = 3% × €400,000 = €12,000`; advances are `€135,252 + €49,470`, leaving €12,247.35 payable.

### 6.2 Employer cash collection, reconciliation, and total cost

| Gross G | Initial employer 23.59% | Excess E | Employer refund 9.09% E | Final employer social/solidarity | Risk fee | Cash-year employer cost | Final post-reconciliation cost |
|---:|---:|---:|---:|---:|---:|---:|---:|
| €20,000.00 | €4,718.00 | €0.00 | €0.00 | €4,718.00 | €4.32 | €24,722.32 | €24,722.32 |
| €60,000.00 | €14,154.00 | €0.00 | €0.00 | €14,154.00 | €4.32 | €74,158.32 | €74,158.32 |
| €100,000.00 | €23,590.00 | €0.00 | €0.00 | €23,590.00 | €4.32 | €123,594.32 | €123,594.32 |
| €200,000.00 | €47,180.00 | €94,700.00 | €8,608.23 | €38,571.77 | €4.32 | €247,184.32 | €238,576.09 |
| €600,000.00 | €141,540.00 | €494,700.00 | €44,968.23 | €96,571.77 | €4.32 | €741,544.32 | €696,576.09 |

For example, at €200,000, the combined amount initially collected on excess salary is `34.09% × €94,700 = €32,283.23`; final solidarity tax is `25% × €94,700 = €23,675.00`; the difference/refund is €8,608.23, paid to the employer. At €600,000 those figures are respectively €168,643.23, €123,675.00, and €44,968.23.

## 7. Universal rules versus variables

Universal for the modeled 2026 ordinary employment case:

- PIT rates 25.5%/33%, €105,300 band threshold, and additional 3% above €200,000;
- fixed €550 monthly/€6,600 annual non-taxable minimum;
- standard 10.50% employee and 23.59% employer VSAOI cash rates;
- €105,300 social maximum and solidarity treatment above it;
- 25% final solidarity rate, 9.09% employer refund, and 10% PIT allocation; and
- €0.36 monthly risk fee for a covered employer.

Variables requiring different treatment in real payroll:

- whether the payroll tax booklet is assigned to this employer;
- pension age and other insured-status categories, which change VSAOI rates;
- dependants, disability/political-repression relief, pensioner minimum, and other personal deductions;
- incomplete-year Latvian residence or employment, uneven pay, benefits in kind, multiple employers, and other income;
- the minimum-contribution regime for low pay;
- the employer's legal form/coverage for the risk fee; and
- monthly and annual statutory rounding performed by payroll and EDS.

## 8. Evidence quality and unresolved implementation details

### Strongest evidence

The strongest evidence is the consolidated primary legislation: the PIT law for annual tax, deduction order, and the solidarity PIT credit; the Solidarity Tax Law for the 25% rate and employer-only refund; and the annual-declaration regulation for the exact reporting interaction between the employee contribution deduction and solidarity PIT prepayment. The current 2026 VID and VSAA pages independently repeat all principal rates, thresholds, allocations, and deadlines.

### Weakest evidence / deliberately unresolved

- The examples use annual arithmetic. The exact statutory cent-rounding sequence across 12 monthly payrolls and EDS annual assessment was not established from a sufficiently explicit 2026 official worked example; therefore cent-level production parity is unresolved.
- The €4.32 annual risk fee assumes 12 chargeable months and a covered ordinary private company. Different employer legal status or a partial month/year can change applicability or the number of monthly charges.
- The additional 3% base can include categories beyond salary under Section 15.1. The salary-only examples use gross salary because no other income exists; this dossier does not generalize that shortcut to mixed-income taxpayers.
- The presentation of the employer's 9.09% as a “final cost” assumes the statutory refund is received. Timing, offsets against other liabilities, or administration of an actual refund is outside the calculation.

No unresolved fact above was filled by analogy or estimation.
