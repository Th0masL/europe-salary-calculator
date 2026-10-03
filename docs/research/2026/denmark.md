# Denmark employee payroll and salary calculation — income year 2026

**Independent research dossier. Access date for every web source: 2026-10-04.**

## Scope, independence, and result status

This dossier reconstructs the 2026 rules from Danish public authorities and legislation only. It was prepared without consulting the repository's Denmark calculator, generated datasets, earlier Denmark calculation documentation, or a prior audit.

The worked model is for an adult resident employee who is single, has no children, is not a member of the Danish National Church, has no capital income or other income/deductions, receives no employer pension beyond statutory ATP, and works full-time throughout 2026 for an ordinary private employer. `G` is total regular taxable gross cash pay actually paid during 2026. Thus, if a quoted annual salary excludes the statutory holiday supplement, that supplement must first be added to `G`; see “Holiday pay” below.

The calculations use the official weighted-average 2026 municipal income-tax rate, 25.049%. An actual employee must use the rate of the employee's tax municipality. The results are annual liability illustrations, not monthly withholding-card simulations; payroll-period rounding can cause small differences.

## 1. Employee-side rules

### 1.1 ATP (Arbejdsmarkedets Tillægspension)

For an employee paid monthly who works at least 117 hours/month, the A-rate is:

- employee: DKK 99/month = **DKK 1,188/year**;
- employer: DKK 198/month = **DKK 2,376/year**;
- total remitted: DKK 297/month = **DKK 3,564/year**.

These are hour-band amounts, not percentages of salary. The worked cases assume known full-time hours even at the low illustrative salary. The official table also gives reduced bands for 78–116 and 39–77 hours and zero below 39 hours.

Source: [Virk, “ATP for employees” / table “A-sats”](https://virk.dk/guidance/atp/atp-arbejdsgiver/atp-medarbejdere/) (current page; no publication date displayed; table current when accessed 2026-10-04). Exact row: “Min. 117 timer/md. | 99,00 kr. | 198,00 kr. | 297,00 kr.” Virk's Samlet Betaling page independently states DKK 891 per full-time employee per quarter (3 × DKK 297) for 2026: [“Arbejdsgiver — Samlet Betaling”](https://virk.dk/vejledning/samlet-betaling/sb-arbejdsgiver/).

ATP tax treatment is not simply an ordinary deduction. Both employee and employer ATP contributions are disregarded in taxable income. The legal guide states: “Bidrag til ATP skal ikke medregnes ved opgørelsen af lønmodtagerens skattepligtige indkomst” and confirms the employee/employer split of 1/3 and 2/3: [Skattestyrelsen, Den juridiske vejledning 2026-1, C.A.10.2.1.1.2.4](https://info.skat.dk/data.aspx?oid=2048235) (2026-1 edition; accessed 2026-10-04).

### 1.2 Labour-market contribution (AM-bidrag)

The rate is **8%**. SKAT says the employer deducts AM-bidrag after ATP and the employee's own pension contribution, but before other tax. From 2026, the rate is 0% through the end of the income year in which a person turns 17; the worked model is an adult.

For this dossier, with no employee pension other than ATP:

```text
employee_ATP = 1,188
AM_base      = G - employee_ATP
AM           = 8% × AM_base
```

Source: [SKAT, “Am-bidrag (arbejdsmarkedsbidrag)”](https://skat.dk/borger/am-bidrag) (current guidance; 2026 age change effective from income year 2026; accessed 2026-10-04): “8 %” and “efter at ATP og eget pensionsbidrag er fratrukket.” The statutory basis is AMBL §1; [Den juridiske vejledning 2026-1, C.A.12.2](https://info.skat.dk/data.aspx?oid=1976912) states 8% and dates the minor exemption to Law no. 96 of 4 February 2025, effective 1 January 2026.

AM-bidrag itself is deducted in computing taxable personal income under PSL §3(2)(6). Source: [Den juridiske vejledning 2026-1, C.A.4.1.11](https://info.skat.dk/data.aspx?oid=2061784) (2026-1 edition; accessed 2026-10-04).

Accordingly, in the stated no-other-items case:

```text
personal_income P = G - employee_ATP - AM
```

### 1.3 Employment deduction (beskæftigelsesfradrag)

For 2026 the deduction is **12.75%**, capped at **DKK 63,300**. It is a deduction in taxable income, not personal income and not a cash credit.

The exact statutory base starts from the AM contribution base and also includes employer-reported ATP. With gross cash pay `G`, no non-ATP pension, and full-rate ATP, the base in these examples is therefore:

```text
employment_base E = (G - employee_ATP) + total_ATP
                  = G + employer_ATP
                  = G + 2,376

employment_deduction = min(12.75% × E, 63,300)
```

This treatment follows [Den juridiske vejledning 2026-1, C.A.4.3.7, “Beregningsgrundlag mv.”](https://info.skat.dk/data.aspx?oid=2273718), which says the base starts from the AM base and that ATP payments reported by the employer enter the base. The rate/cap are on the same page. The official public summary gives the same 12.75%, DKK 63,300, and a full-deduction income of DKK 496,471: [SKAT, “Beskæftigelses- og jobfradrag”](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag) (2026 table; accessed 2026-10-04).

The controlling wording is LL §9J in the consolidated Ligningsloven, no. 1500 of **24 November 2025**: [Lovtidende PDF](https://www.lovtidende.dk/api/pdf/250970), page 27. It expressly includes employer-reported ATP. Effective for income year 2026, the 12.75% rule was enacted by Law no. 482 of **22 May 2024**, §2(1) and §10(4): [Retsinformation](https://www.retsinformation.dk/eli/lta/2024/482).

The extra senior employment deduction (1.4%, maximum DKK 6,100 in 2026) is **not universal** and is excluded because the employee's age was not specified. It applies only in the last two income years before statutory pension age under the rule in force. The extra single-parent deduction is also excluded because the model has no children.

### 1.4 Job allowance (jobfradrag)

For 2026 the job allowance is **4.5% of the employment base above DKK 235,200**, capped at **DKK 3,100**:

```text
job_allowance = min(4.5% × max(E - 235,200, 0), 3,100)
```

It uses the same base and conditions as the ordinary employment deduction and reduces taxable income. Source: [Den juridiske vejledning 2026-1, C.A.4.3.8](https://info.skat.dk/data.aspx?oid=2273725) (2026-1 edition; accessed 2026-10-04), with the exact 2026 threshold and cap; see also the [SKAT public 2026 table](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag).

### 1.5 Personal allowance (personfradrag)

The 2026 personal allowance is **DKK 54,100**. Source: [Den juridiske vejledning 2026-1, C.A.9.1](https://info.skat.dk/data.aspx?oid=1976905) (2026-1 edition; accessed 2026-10-04): “Personfradraget er i 2026 54.100 kr.”

Technically it is a tax-value credit, not an income-base deduction. Under PSL §12 its value is calculated at the municipal/church rate and the state bottom-tax rate. For every worked case both personal income and taxable income exceed DKK 54,100, so the following algebraically equivalent presentation is valid:

```text
bottom-tax base    = P  - 54,100
municipal-tax base = TI - 54,100
```

The statutory credit mechanism is in [Personskatteloven §12, consolidated-act PDF](https://www.retsinformation.dk/api/pdf/223942) (official consolidated text; §12 under “Skatteværdi”; accessed 2026-10-04). The tax-reform bill's explanatory notes expressly say the allowance technically reduces calculated bottom and municipal taxes rather than their bases: [Bill L138, 2023-24](https://www.retsinformation.dk/eli/ft/202312L00138) (introduced 2024; explanatory notes to PSL §12).

### 1.6 State taxes in 2026

For an employee with no capital income:

| Component | 2026 rate and threshold | Calculation in this dossier |
|---|---:|---|
| Bottom tax (bundskat) | 12.01% | `12.01% × max(P - 54,100, 0)` |
| Middle tax (mellemskat) | 7.5% above DKK 641,200 after AM | `7.5% × max(P - 641,200, 0)` |
| Top tax (topskat) | 7.5% above DKK 777,900 after AM | `7.5% × max(P - 777,900, 0)` |
| Additional top tax (toptopskat) | 5% above DKK 2,592,700 after AM | `5% × max(P - 2,592,700, 0)` |

Primary source: [SKAT, “Bundskat, mellemskat, topskat og toptopskat”](https://skat.dk/hjaelp/bundskat-mellemskat-topskat-og-toptopskat) (2026 rates page; accessed 2026-10-04). The page states each exact percentage and threshold and that the three higher thresholds use personal income after AM-bidrag. The reform creating the 2026 middle/top/additional-top structure is Law no. 482 of 22 May 2024: [Retsinformation](https://www.retsinformation.dk/eli/lta/2024/482), effective from income year 2026 under §10(4).

### 1.7 Municipal tax, church tax, and the tax ceiling

Municipal income tax is imposed on taxable income. In this no-other-deductions model:

```text
taxable_income TI = P - employment_deduction - job_allowance
municipal_tax      = municipal_rate × max(TI - 54,100, 0)
```

The employee's actual rate depends on tax municipality. For a location-neutral example, this dossier uses the official **weighted national average 25.049%** (rounded official headline: 25.0%). The official table was published **27 October 2025** and gives 25.068% for 2025 and 25.049% for 2026: [Ministry of Taxation, “Kommuneskatter — gennemsnitsprocenten i 2026”](https://svmn.dk/tal-og-metode/satser/statistik-i-kommunerne/kommuneskatter-gennemsnitsprocenten-i-2026). Individual 2026 municipal rates are published in the Ministry's spreadsheet collection, dated **31 October 2025**: [“Kommuneskatteprocenter 1977-2026 i regneark”](https://skm.dk/tal-og-metode/satser/statistik-i-kommunerne/kommuneskatteprocenter-1977-2025).

Church tax is **zero** under the stated non-member assumption. It is membership- and municipality-specific. The same 27 October 2025 official table reports an average 0.867% among church-tax payers in 2026, but that is not used here.

The 2026 sloping ceiling for personal income caps the sum of bottom tax + middle tax + municipal rate at **44.57%** by reducing middle tax. It does not separately cap the new top and additional-top taxes. At the official average municipal rate:

```text
12.01% + 7.5% + 25.049% = 44.559% < 44.57%
```

Therefore no ceiling reduction is needed in the examples. In a municipality above 25.06%, the middle-tax rate on the relevant base is reduced by the excess over 44.57%. Source: [Den juridiske vejledning 2026-1, C.C.5.2.15.2 “Skatteloft”](https://info.skat.dk/data.aspx?oid=1948928) (2026-1 edition; accessed 2026-10-04). The legislative rule is PSL §19 as substituted by Law no. 482 of 22 May 2024. The separate 42% ceiling concerns positive net capital income, absent here.

## 2. Employer-side statutory charges

Denmark has no general employer social-security percentage comparable to many EU systems. Instead, ordinary employers face flat contributions plus variable insurance/sector obligations. “Mandatory” does not mean one universal number: several charges depend on hours, employer size, sector, maternity scheme, holiday arrangement, training record, or insurer.

### 2.1 ATP and Samlet Betaling items

The official 2026 Samlet Betaling table is per full-time employee **per quarter**, except where the row itself says per month:

| Item | Official 2026 rate | Annualized full-time amount | Universality / qualification |
|---|---:|---:|---|
| ATP total remittance | DKK 891/quarter | DKK 3,564 | Includes DKK 1,188 withheld from employee; employer economic cost is **DKK 2,376**. |
| AUB | DKK 705.25/quarter | **DKK 2,821** | Employers paying ATP generally contribute, but a deduction applies for the first employee and every 50th employee; apprentices/trainees registered in AUB are exempt. Not safely universal per individual worker. |
| AES + occupational-injury levy | Sector table | **DKK 284–2,911** across the ordinary private-sector groups shown | Employer-paid and sector-specific; the full table also contains public-sector group 84 at DKK 10,892; see below. |
| AFU | DKK 0/quarter | **DKK 0** | Statutory scheme, but zero rate in 2026. |
| Barsel.dk | DKK 550/quarter | **DKK 2,200** | Private employers unless covered by another approved maternity scheme. |
| FerieKonto administration | DKK 4/month | **DKK 48** | Only for months/employees for whom the employer must report to FerieKonto. |
| Financing contribution (FIB) | DKK 82/quarter | **DKK 328** | Private employer per full-rate ATP-equivalent employee; limited exemptions exist. |
| Lønmodtagernes Feriemidler administration | DKK 5/quarter | **DKK 20** | Listed rate; applicability depends on the employer's remaining frozen-holiday-fund administration, so it is not assumed for every current employee. |
| Læreplads-AUB | annual statement | unresolved per employee | Company-specific result, not a flat payroll rate. |

Primary rate source: [Virk, “Satser for Samlet Betaling 2017-2026,” section “Bidragssatser 2026”](https://virk.dk/vejledning/samlet-betaling/sb-arbejdsgiver/sb-tidligere-satser/) (2026 rates; accessed 2026-10-04). The live [Samlet Betaling employer page](https://virk.dk/vejledning/samlet-betaling/sb-arbejdsgiver/) repeats AUB DKK 705.25, ATP DKK 891, Barsel.dk DKK 550, and FIB DKK 82 per quarter and FerieKonto DKK 4/month.

AUB detail: [Virk, “Arbejdsgivernes Uddannelsesbidrag (AUB)”](https://virk.dk/vejledning/aub/aub-arbejdsgiver/) states **DKK 2,821 for each full-time employee in 2026**, with a deduction for the first and every 50th employee. Its table splits each quarter into AUB DKK 596.75 + VEU DKK 108.50 = DKK 705.25.

Barsel.dk detail: the 2026 full-time monthly equivalent is DKK 183.33 at at least 117 hours, effective **1 January 2026**: [Virk, “Barsel.dk — Delvist omfattet,” rate table](https://virk.dk/vejledning/barsel-dk/bdk-privat-arbejdsgiver/delvist-omfattet/). Virk states elsewhere on the Samlet Betaling page that no Barsel.dk contribution is due when the employer is covered by another approved maternity scheme.

FIB detail: [Virk, “Finansieringsbidrag”](https://virk.dk/vejledning/finansieringsbidrag/fib-finansieringsbidrag/) gives **DKK 82/quarter in 2026** and itemizes it as unemployment/VEU DKK 13.25, sickness DKK 19.75, maternity DKK −5.00, job-clarification benefit DKK −1.00, and Wage Earners' Guarantee Fund DKK 55.00.

Læreplads-AUB is mandatory only for employers that in the previous year paid more than one full ATP contribution for vocationally trained employees. The 2026 deficit contribution is **DKK 27,000 per missing trainee point**, so it cannot be allocated correctly from one employee's salary alone. Source: [Virk/Business in Denmark, “Arbejdsgivernes Uddannelsesbidrag (AUB),” updated 19 May 2026](https://businessindenmark.virk.dk/guidance/aub-bid-arbejdsgivernes-uddannelsesbidrag/aub-bid-employer/); see also [Virk, “Læreplads-AUB”](https://virk.dk/vejledning/aub/aub-arbejdsgiver/laereplads-aub/).

### 2.2 AES and compulsory occupational-accident insurance

AES finances occupational-disease cover and includes an occupational-injury levy. The official **“AES-Satser 2026”** table gives annual total collection per full-time employee by industry group, inclusive of DKK 2 collection cost:

- lowest listed: group 31, energy/water, **DKK 284**;
- group 71, finance/business services, **DKK 457** (AES DKK 268 + levy DKK 189);
- industry: **DKK 1,558**;
- construction, other: **DKK 2,323**;
- highest ordinary private-sector-type group shown: group 83, social institutions/associations/culture/waste, **DKK 2,911**;
- the full table's highest row is public-sector group 84, defence/police/courts/foreign affairs, **DKK 10,892**, which is not the ordinary private-employer assumption.

Source: [Virk/AES, “AES-Satser 2026” PDF](https://virk.dk/assets/6feKOXUjVtAaPklFxxBz9C/aes_bidragssatser_2026.pdf) (title expressly 2026; accessed 2026-10-04). The correct value requires the employer's industry classification; no universal average should be inserted.

Separately, every in-scope employer must transfer occupational-accident risk to an authorized insurer. The premium is mandatory but market- and risk-specific, and no official universal 2026 amount exists. Source: [Arbejdsskadesikringsloven, consolidated act no. 667 of 2026, §50](https://www.retsinformation.dk/eli/lta/2026/667) (published 2026): employers subject to security obligations “skal overføre deres risiko for ulykker til et forsikringsselskab.” **Unresolved amount: insurer quote required.**

### 2.3 Holiday pay is compensation, not a payroll-fund percentage in every case

Under Ferieloven §16:

- a monthly employee entitled to pay on public holidays and sick days receives normal salary during holiday plus a **1% holiday supplement**;
- other employees accrue **12.5% holiday allowance**;
- an eligible employee may elect 12% holiday allowance instead of salary plus supplement before the holiday year.

Sources: [Ferieloven, consolidated act no. 230 of 12 February 2021, §§16–19](https://retsinformation.dk/eli/lta/2021/230) (current statutory provisions; accessed 2026-10-04) and [Life in Denmark, “Holiday allowance”](https://lifeindenmark.borger.dk/working/holiday-allowance-ny/holiday-allowance) (official public guidance; accessed 2026-10-04).

The worked examples define `G` as total gross cash compensation actually paid, so no second holiday amount is added to employee taxable income. If instead `G` is stated base salary excluding the statutory 1% supplement for a monthly salaried worker, the supplement must be separately budgeted and taxed when paid. For hourly/holiday-allowance employees, 12.5% is generally a deferred wage entitlement, not safely an extra amount on top of a salary already quoted as total compensation.

### 2.4 Employer-cost illustration, not a universal output

For comparability only, suppose a full-time monthly employee works in AES group 71 at a private employer that:

- is not entitled to the AUB first/50th-employee exemption;
- is in Barsel.dk, not an alternative approved scheme;
- has no current FerieKonto or frozen-fund administration fee for this salaried employee;
- has no Læreplads-AUB deficit; and
- quotes `G` inclusive of any holiday supplement.

Then known employer charges are:

```text
employer ATP                    2,376
AUB                             2,821
AES group 71                      457
Barsel.dk                       2,200
FIB                               328
AFU                                 0
                                -----
known annual charges            8,182 DKK

illustrative employer cost = G + 8,182
                           + occupational-accident insurance premium (unresolved)
```

That illustrative known cost is DKK 158,182 / 458,182 / 758,182 / 1,508,182 / 4,508,182 at the five salary points, before the unresolved insurance premium and any conditional items. It must not be presented as a universal Danish employer rate.

Occupational pension beyond ATP is not universally fixed by statute: it depends on collective agreement or contract and is therefore excluded. The same is true of agreement-specific benefits, extra holiday days, higher holiday supplements, and private health/pension insurance.

## 3. Worked annual calculations

### 3.1 Formula set used

All amounts below are DKK. Intermediate results retain øre; displayed totals are rounded to 0.01.

```text
A  = 1,188                                      employee ATP
ER = 2,376                                      employer ATP
AM_base = G - A
AM = 0.08 × AM_base
P  = AM_base - AM                               personal income
E  = AM_base + (A + ER) = G + ER                employment/job base
BF = min(0.1275 × E, 63,300)                    employment deduction
JF = min(0.045 × max(E - 235,200, 0), 3,100)   job allowance
TI = P - BF - JF                                taxable income

municipal = 0.25049 × max(TI - 54,100, 0)
bottom    = 0.1201  × max(P  - 54,100, 0)
middle    = 0.075   × max(P  - 641,200, 0)
top       = 0.075   × max(P  - 777,900, 0)
top-top   = 0.05    × max(P  - 2,592,700, 0)

cash deductions = A + AM + municipal + bottom + middle + top + top-top
net cash         = G - cash deductions
```

The employment and job deductions reduce municipal taxable income but not the personal-income bases for bottom/middle/top/additional-top tax. The personal allowance reduces bottom and municipal tax only. No church tax applies. At the 25.049% average municipality, the 44.57% ceiling does not reduce middle tax.

### 3.2 DKK 150,000 gross

| Step | Calculation | Amount |
|---|---:|---:|
| Employee ATP | fixed | 1,188.00 |
| AM base | 150,000 − 1,188 | 148,812.00 |
| AM-bidrag | 8% × 148,812 | 11,904.96 |
| Personal income `P` | 148,812 − 11,904.96 | 136,907.04 |
| Employment/job base `E` | 150,000 + 2,376 | 152,376.00 |
| Employment deduction | 12.75% × 152,376 | 19,427.94 |
| Job allowance | below DKK 235,200 | 0.00 |
| Taxable income `TI` | 136,907.04 − 19,427.94 | 117,479.10 |
| Municipal tax | 25.049% × (117,479.10 − 54,100) | 15,875.83 |
| Bottom tax | 12.01% × (136,907.04 − 54,100) | 9,945.13 |
| Middle / top / top-top | below thresholds | 0.00 |
| **Total cash deductions** | ATP + AM + taxes | **38,913.92** |
| **Net cash** | 150,000 − 38,913.92 | **111,086.08** |

### 3.3 DKK 450,000 gross

| Step | Calculation | Amount |
|---|---:|---:|
| Employee ATP | fixed | 1,188.00 |
| AM base | 450,000 − 1,188 | 448,812.00 |
| AM-bidrag | 8% × 448,812 | 35,904.96 |
| Personal income `P` | 448,812 − 35,904.96 | 412,907.04 |
| Employment/job base `E` | 450,000 + 2,376 | 452,376.00 |
| Employment deduction | 12.75% × 452,376 | 57,677.94 |
| Job allowance | capped | 3,100.00 |
| Taxable income `TI` | 412,907.04 − 57,677.94 − 3,100 | 352,129.10 |
| Municipal tax | 25.049% × (352,129.10 − 54,100) | 74,653.31 |
| Bottom tax | 12.01% × (412,907.04 − 54,100) | 43,092.73 |
| Middle / top / top-top | below thresholds | 0.00 |
| **Total cash deductions** | ATP + AM + taxes | **154,838.99** |
| **Net cash** | 450,000 − 154,838.99 | **295,161.01** |

### 3.4 DKK 750,000 gross

| Step | Calculation | Amount |
|---|---:|---:|
| Employee ATP | fixed | 1,188.00 |
| AM base | 750,000 − 1,188 | 748,812.00 |
| AM-bidrag | 8% × 748,812 | 59,904.96 |
| Personal income `P` | 748,812 − 59,904.96 | 688,907.04 |
| Employment/job base `E` | 750,000 + 2,376 | 752,376.00 |
| Employment deduction | capped | 63,300.00 |
| Job allowance | capped | 3,100.00 |
| Taxable income `TI` | 688,907.04 − 63,300 − 3,100 | 622,507.04 |
| Municipal tax | 25.049% × (622,507.04 − 54,100) | 142,380.28 |
| Bottom tax | 12.01% × (688,907.04 − 54,100) | 76,240.33 |
| Middle tax | 7.5% × (688,907.04 − 641,200) | 3,578.03 |
| Top / top-top | below thresholds | 0.00 |
| **Total cash deductions** | ATP + AM + taxes | **283,291.59** |
| **Net cash** | 750,000 − 283,291.59 | **466,708.41** |

### 3.5 DKK 1,500,000 gross

| Step | Calculation | Amount |
|---|---:|---:|
| Employee ATP | fixed | 1,188.00 |
| AM base | 1,500,000 − 1,188 | 1,498,812.00 |
| AM-bidrag | 8% × 1,498,812 | 119,904.96 |
| Personal income `P` | 1,498,812 − 119,904.96 | 1,378,907.04 |
| Employment/job base `E` | 1,500,000 + 2,376 | 1,502,376.00 |
| Employment deduction | capped | 63,300.00 |
| Job allowance | capped | 3,100.00 |
| Taxable income `TI` | 1,378,907.04 − 63,300 − 3,100 | 1,312,507.04 |
| Municipal tax | 25.049% × (1,312,507.04 − 54,100) | 315,218.38 |
| Bottom tax | 12.01% × (1,378,907.04 − 54,100) | 159,109.33 |
| Middle tax | 7.5% × (1,378,907.04 − 641,200) | 55,328.03 |
| Top tax | 7.5% × (1,378,907.04 − 777,900) | 45,075.53 |
| Top-top | below threshold | 0.00 |
| **Total cash deductions** | ATP + AM + taxes | **695,824.22** |
| **Net cash** | 1,500,000 − 695,824.22 | **804,175.78** |

### 3.6 DKK 4,500,000 gross

| Step | Calculation | Amount |
|---|---:|---:|
| Employee ATP | fixed | 1,188.00 |
| AM base | 4,500,000 − 1,188 | 4,498,812.00 |
| AM-bidrag | 8% × 4,498,812 | 359,904.96 |
| Personal income `P` | 4,498,812 − 359,904.96 | 4,138,907.04 |
| Employment/job base `E` | 4,500,000 + 2,376 | 4,502,376.00 |
| Employment deduction | capped | 63,300.00 |
| Job allowance | capped | 3,100.00 |
| Taxable income `TI` | 4,138,907.04 − 63,300 − 3,100 | 4,072,507.04 |
| Municipal tax | 25.049% × (4,072,507.04 − 54,100) | 1,006,570.78 |
| Bottom tax | 12.01% × (4,138,907.04 − 54,100) | 490,585.33 |
| Middle tax | 7.5% × (4,138,907.04 − 641,200) | 262,328.03 |
| Top tax | 7.5% × (4,138,907.04 − 777,900) | 252,075.53 |
| Top-top tax | 5% × (4,138,907.04 − 2,592,700) | 77,310.35 |
| **Total cash deductions** | ATP + AM + taxes | **2,449,962.97** |
| **Net cash** | 4,500,000 − 2,449,962.97 | **2,050,037.03** |

### 3.7 Comparison summary

| Gross `G` | Employee ATP | AM | Income taxes | Total deductions | Net cash | Effective deduction rate |
|---:|---:|---:|---:|---:|---:|---:|
| 150,000 | 1,188.00 | 11,904.96 | 25,820.96 | 38,913.92 | 111,086.08 | 25.94% |
| 450,000 | 1,188.00 | 35,904.96 | 117,746.03 | 154,838.99 | 295,161.01 | 34.41% |
| 750,000 | 1,188.00 | 59,904.96 | 222,198.63 | 283,291.59 | 466,708.41 | 37.77% |
| 1,500,000 | 1,188.00 | 119,904.96 | 574,731.26 | 695,824.22 | 804,175.78 | 46.39% |
| 4,500,000 | 1,188.00 | 359,904.96 | 2,088,870.01 | 2,449,962.97 | 2,050,037.03 | 54.44% |

## 4. Universal rules versus inputs that must remain configurable

### Universal within the stated employee profile

- 8% AM-bidrag, after employee ATP/own pension deductions.
- DKK 54,100 personal allowance.
- 12.75% employment deduction, maximum DKK 63,300.
- 4.5% job allowance above DKK 235,200, maximum DKK 3,100.
- 12.01% bottom tax.
- 7.5% middle tax above DKK 641,200; 7.5% top tax above DKK 777,900; 5% additional-top tax above DKK 2,592,700, all on relevant personal income after AM.
- Full-time monthly ATP A-rate: employee DKK 99 and employer DKK 198 per month.
- No church tax for a non-member.

### Municipality-, employee-, sector-, or employer-specific

- Municipal tax rate (25.049% here is an official national weighted average, not an individual's rate).
- Church tax if the employee is a member.
- ATP band if hours/pay frequency differ.
- Extra senior or single-parent employment deductions.
- Employer pension and collectively agreed employee pension.
- AES industry group and compulsory accident-insurance premium.
- AUB headcount exemptions, Barsel.dk versus an approved alternative, FerieKonto use, frozen-fund administration, and Læreplads-AUB result.
- Holiday-pay treatment and whether a quoted salary includes the 1% supplement or represents a 12.5%-allowance arrangement.

## 5. Unresolved facts and implementation cautions

1. **Compulsory occupational-accident insurance premium:** mandatory by statute, but no official universal rate; it requires employer risk/industry data and an insurer quote.
2. **Læreplads-AUB per employee:** no determinate flat charge. It depends on company training targets and trainee points; the only fixed 2026 parameter located is DKK 27,000 per missing point.
3. **Conditional administration fees:** the official 2026 amounts are clear, but whether FerieKonto DKK 4/month and Lønmodtagernes Feriemidler DKK 5/quarter apply requires employer/employee status not in the prompt.
4. **Monthly withholding versus final annual tax:** exact pay slips use the tax card, pay-period withholding and rounding. The annual model above is suitable for a salary calculator estimate but should not claim to reproduce SKAT's assessment to the krone.
5. **Salary convention:** a calculator must say whether gross pay includes the statutory holiday supplement and any employee/employer pension. Without that definition, both taxable pay and employer cost can be misstated.

## 6. Evidence assessment

**Strongest evidence:** the 2026 SKAT rate pages; the 2026-1 Den juridiske vejledning; consolidated Ligningsloven no. 1500 of 24 November 2025; Law no. 482 of 22 May 2024; the Ministry's municipal-rate table published 27 October 2025; and Virk's explicit 2026 ATP/Samlet Betaling/AES tables. These sources state exact values and, for the tax reform, effective dates.

**Weakest evidence / remaining uncertainty:** there is deliberately no single employer-cost total. Accident-insurance premiums are commercially priced; AES is sector-specific; AUB and Læreplads-AUB depend on employer facts; holiday administration depends on the pay arrangement. Any calculator that emits one universal Danish employer percentage would be making an unsupported assumption.
