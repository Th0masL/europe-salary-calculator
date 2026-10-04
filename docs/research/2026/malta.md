# Malta employee payroll, tax year 2026 — clean-room research dossier

**Access/research date:** 2026-10-04  
**Scope:** Malta-resident single employee, age 30, no children, ordinary full-time private employment, one main employment, equal regular basic salary over 52 contribution weeks, no benefits in kind or special tax regime. This dossier was reconstructed independently from Malta Tax and Customs Administration (MTCA), Department of Social Security, Department of Industrial and Employment Relations (DIER), and legislation sources.

## Executive result and gross-pay convention

The 2026 single-person income-tax schedule is 0% to EUR 12,000, 15% to EUR 16,000, 25% to EUR 60,000, and 35% thereafter. Tax is calculated on gross taxable employment emoluments; employee Class 1 Social Security Contributions (SSC) are a separate payroll deduction, not a deduction from the income-tax base.

For an employee born after 1961, Class 1 SSC is normally 10% of basic weekly wage, rounded weekly to cents, capped at **EUR 55.93 per week**. The employer matches it. The private employer also pays an employer-only Maternity and Adoption Leave Trust contribution of 0.3% of basic weekly wage, capped at **EUR 1.68 per week**.

Malta additionally requires four fixed cash payments for a full-year employee:

- statutory bonus: EUR 135.10 at end-June and EUR 135.10 in December;
- weekly allowance: EUR 121.16 at end-March and EUR 121.16 at end-September; and
- annual total: **EUR 512.52**.

Because the request specifies annual **gross cash compensation**, each worked gross `G` is defined to include the EUR 512.52. Thus `annual basic salary = G − 512.52`. This avoids adding cash after calling `G` “gross.” If a payroll input instead means a contractual annual **basic** salary exclusive of statutory payments, total taxable gross and employer cash cost must first be increased by EUR 512.52; see the bridge in section 6.

## 1. Income tax: 2026 single rates

MTCA's official **“Tax Rates for Individuals — 2026”** table gives:

| Chargeable income | Calculation shown by MTCA | Equivalent marginal bands |
|---:|---:|---:|
| EUR 0–12,000 | 0% | 0% |
| EUR 12,001–16,000 | `15% × income − 1,800` | 15% over EUR 12,000 |
| EUR 16,001–60,000 | `25% × income − 3,400` | 25% over EUR 16,000, after EUR 600 tax in prior band |
| EUR 60,001+ | `35% × income − 9,400` | 35% over EUR 60,000, after EUR 11,600 cumulative tax |

The dated MTCA PDF **“2026 Tax Rates 13-04-26 (amendment)”**, section 2.1, states that the standard single rates continue to apply to resident individuals who do not qualify for another rate. The child-enhanced married/parent schedules therefore do not apply to this single, childless employee.

For this case:

`chargeable employment income = total gross cash emoluments G`

`PIT = applicable 2026 rate × G − MTCA subtraction amount`

`net cash = G − PIT − employee Class 1 SSC`

MTCA describes the Final Settlement System (FSS) as deducting tax from **gross emoluments** as received. It separately requires employers to deduct employee SSC and remit both tax and SSC monthly. Nothing in the ordinary employee sources reviewed provides a deduction of employee Class 1 SSC from chargeable employment income, so it is not subtracted before applying the bands.

The FSS performs in-year withholding and the employer completes the FS3/FS7 annual reconciliation by 15 February of the following year. The annual examples below calculate final tax directly from the published annual bands rather than reproduce each periodic FSS withholding.

## 2. Class 1 Social Security Contributions

MTCA's **“Class 1 — Social Security Contribution Rates: 2026”** table, for a person born from 1 January 1962 onwards, gives:

| Category | Basic weekly wage | Employee weekly SSC | Employer weekly SSC | Maternity weekly |
|---|---:|---:|---:|---:|
| B (age 18+) | EUR 0.10–229.44 | EUR 22.94, or employee may elect 10% pro rata | EUR 22.94 | EUR 0.69 |
| C | EUR 229.45–559.30 | 10% | 10% | 0.30% |
| D | EUR 559.31+ | EUR 55.93 | EUR 55.93 | EUR 1.68 |

The table's footnotes define the measure as basic weekly wage (or weekly equivalent of basic monthly salary) and require percentage rates to be calculated to the nearest cent **weekly**.

The Department of Social Security page **“Social Security Contributions”** is explicit that basic weekly wage excludes allowances, bonuses, and overtime. Accordingly, the statutory EUR 512.52 is taxable cash but not part of the Class 1 basic-weekly-wage base.

Contributions attach to each Monday. The Department's 2025 explainer states there are 52 or 53 contributions depending on the number of Mondays in the year. Calendar year 2026 has **52 Mondays** (5 January through 28 December), so this dossier uses 52 contributions.

For the stated equal-pay case:

`annual_basic = G − 512.52`

`basic_weekly_wage = annual_basic / 52`

`weekly SSC = round_to_cent(10% × weekly wage)` in category C, or the fixed category-D amount EUR 55.93

`annual employee SSC = annual employer SSC = 52 × weekly SSC`

The maximum annual employee or employer SSC in this 52-contribution year is therefore `52 × 55.93 = EUR 2,908.36`. This is a weekly cap, not a general annual cap: uneven pay or a partial year must be calculated week by week.

The state also contributes under the tripartite system, but that state contribution is neither withheld from the employee nor paid as an additional employer payroll charge and is excluded from employer cost.

## 3. Maternity and Adoption Leave Trust contribution

The Department of Social Security's **“Maternity / Adoption Leave Trust Claim”** states:

- it applies to private-sector employers for their employees;
- the rate is 0.3% of basic weekly wage;
- it is entirely employer-paid and must not be deducted from wages; and
- the Public Service, public-sector entities, authorities, agencies and public corporations are exempt.

This ordinary private employer is not exempt. The 2026 Class 1 table supplies the category-C 0.30% and category-D fixed maximum EUR 1.68 per week. At 52 contributions, maximum annual Maternity Fund cost is **EUR 87.36**.

The contribution is a financing charge. Maternity leave itself can produce cash-flow and reimbursement timing, but it is not an additional fixed percentage included in these regular-pay examples.

## 4. Statutory bonus and weekly allowance

DIER's official **“Bonus and Weekly Allowances”** page lists the four payments exactly:

| Due | Type | Full amount |
|---|---|---:|
| End of March | Weekly allowance | EUR 121.16 |
| End of June | Statutory bonus | EUR 135.10 |
| End of September | Weekly allowance | EUR 121.16 |
| 15–23 December | Statutory bonus | EUR 135.10 |

For a partial entitlement, DIER states EUR 0.74 per calendar day for the bonus and EUR 4.66 per working week (or proportion) for the weekly allowance. DIER's 2026 minimum-wage page says every employee is entitled to the statutory bonus and weekly allowance. Its standard employment-contract material states these payments are **in addition to** the basic weekly wage.

They are employment cash emoluments and therefore included in taxable gross. The Social Security definition excludes bonuses and allowances from basic weekly wage, so no Class 1 or Maternity contribution is calculated on them.

This creates two legitimate data conventions:

1. **Total-gross convention used below:** `G = basic salary + 512.52`.
2. **Quoted-basic convention:** `taxable gross = quoted basic + 512.52`; SSC/Maternity are calculated on quoted basic alone.

A calculator must label which convention its input uses. Silently adding EUR 512.52 to a number already described as total annual gross would double count the statutory payments.

## 5. Employer charges and calculation order

For the ordinary private employment assumed here, the fixed payroll additions identified in the official sources are:

- employer Class 1 SSC, equal to the employee weekly amount; and
- employer-only Maternity Fund contribution.

The statutory bonuses and allowances are not a levy: they are employee cash remuneration. Under the total-gross convention they are already inside `G`. No separate universal payroll tax, unemployment levy, or health levy was found in the reviewed official Class 1/FSS tables, and none is added.

Calculation sequence:

1. Split total annual gross into EUR 512.52 statutory payments and remaining basic salary.
2. Divide basic salary by 52 to get basic weekly wage.
3. Choose the age-specific Class 1 category and calculate/round the weekly employee, employer and maternity amounts.
4. Multiply each weekly contribution by 52.
5. Apply PIT to total taxable gross `G` without deducting SSC.
6. Employee net is gross less PIT and employee SSC; employer cost is gross plus employer SSC and Maternity Fund.

## 6. Worked calculations

All values are EUR. Percentage weekly contributions are rounded to the nearest cent before multiplying by 52, as MTCA requires.

### EUR 20,000 annual total gross

`annual basic = 20,000 − 512.52 = 19,487.48`

`weekly basic = 19,487.48 / 52 = 374.7592308` → category C

`weekly SSC = round(10% × 374.7592308) = 37.48`

`weekly maternity = round(0.30% × 374.7592308) = 1.12`

| Item | Calculation | EUR |
|---|---|---:|
| PIT | 25% × 20,000 − 3,400 | 1,600.00 |
| Employee SSC | 37.48 × 52 | 1,948.96 |
| **Employee net** | 20,000 − 1,600 − 1,948.96 | **16,451.04** |
| Employer SSC | 37.48 × 52 | 1,948.96 |
| Employer maternity | 1.12 × 52 | 58.24 |
| **Employer cost** | 20,000 + 1,948.96 + 58.24 | **22,007.20** |

### Higher salaries (category D)

For every remaining example, `(G − 512.52) / 52` exceeds EUR 559.31. Each therefore uses fixed weekly employee SSC EUR 55.93, employer SSC EUR 55.93, and maternity EUR 1.68:

- annual employee SSC = annual employer SSC = `55.93 × 52 = EUR 2,908.36`;
- annual maternity = `1.68 × 52 = EUR 87.36`; and
- employer charges above gross = EUR 2,995.72.

| Total annual gross | Annual basic | Weekly basic | PIT formula | PIT | Employee SSC | Net cash | Employer SSC | Maternity | Employer cost |
|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|
| 60,000 | 59,487.48 | 1,143.9900 | 25% × 60,000 − 3,400 | 11,600.00 | 2,908.36 | **45,491.64** | 2,908.36 | 87.36 | **62,995.72** |
| 100,000 | 99,487.48 | 1,913.2208 | 35% × 100,000 − 9,400 | 25,600.00 | 2,908.36 | **71,491.64** | 2,908.36 | 87.36 | **102,995.72** |
| 200,000 | 199,487.48 | 3,836.2977 | 35% × 200,000 − 9,400 | 60,600.00 | 2,908.36 | **136,491.64** | 2,908.36 | 87.36 | **202,995.72** |
| 600,000 | 599,487.48 | 11,528.6054 | 35% × 600,000 − 9,400 | 200,600.00 | 2,908.36 | **396,491.64** | 2,908.36 | 87.36 | **602,995.72** |

### Bridge if an input is annual basic salary instead

For quoted annual basic `Q`:

`total taxable cash gross = Q + 512.52`

`weekly contribution wage = Q / 52`

`employer cost = Q + 512.52 + employer SSC + maternity contribution`

For example, a quoted EUR 20,000 basic salary is not the first row above: it produces total cash gross EUR 20,512.52. A system should not choose between these conventions without an explicit product definition.

## 7. Universal rules versus variables

| Universal for this scenario | Variable / must be supplied |
|---|---|
| 2026 single PIT bands | Tax status, special regime or tax credits |
| Basic weekly wage excludes bonuses/allowances/overtime | Number of contribution Mondays in a partial employment period |
| Age-30 category-C/D thresholds and caps | Uneven weekly/monthly basic salary |
| Employer matches employee Class 1 rate | Whether input gross includes statutory EUR 512.52 |
| Private-employer maternity contribution | Public-sector/exempt employer status |
| Full-year statutory cash payments total EUR 512.52 | Partial-year pro-rating and other contractual bonuses |

## 8. Primary-source register

All sources accessed 2026-10-04.

1. **Malta Tax and Customs Administration, “Tax Rates for Individuals — 2026.”** Current 2026 page; no separate publication date displayed. [Official page](https://mtca.gov.mt/personal-tax/tax-rates/tax-ratesindividuals/2026). Pinpoint: lines/table “Single Rates”: 0–12,000 at 0%; 12,001–16,000 at 15% less 1,800; 16,001–60,000 at 25% less 3,400; 60,001+ at 35% less 9,400.
2. **MTCA, “2026 Tax Rates 13-04-26 (amendment).”** Dated 2026-04-13. [Official PDF](https://mtca.gov.mt/docs/default-source/documents/2026-tax-rates.pdf?sfvrsn=37563fb2_5). Pinpoint: section 2.1, Standard Single Rates.
3. **MTCA, “Class 1 — Social Security Contribution Rates: 2026.”** Current 2026 table; linked government service last updated 2026-04-28. [Official page](https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates). Pinpoints: rows C/D for persons born from 1962; footnotes defining basic weekly wage and weekly cent rounding.
4. **Department of Social Security, “Social Security Contributions.”** Current page; no displayed publication date. [Official page](https://socialsecurity.gov.mt/en/information-and-applications-for-benefits-and-services/social-security-contributions/social-security-contributions/). Pinpoints: employed persons; employee/employer matching; basic weekly wage excludes allowances, bonuses and overtime; employer monthly remittance.
5. **Department of Social Security, “Social Security Contributions in Malta: What You Need to Know.”** Published 2025-05-01. [Official page](https://socialsecurity.gov.mt/en/social-security-contributions-in-malta-what-you-need-to-know/). Pinpoint: contributions attach to Mondays, 52 or 53 according to the year; Class 1 based on gross basic weekly wage.
6. **DIER, “Bonus and Weekly Allowances.”** Current 2026 page; no publication date displayed. [Official page](https://dier.gov.mt/en/services/employment-conditions/wages/bonus-and-weekly-allowances/). Pinpoints: EUR 135.10 twice and EUR 121.16 twice; partial-entitlement rates.
7. **DIER, “National Minimum Wage.”** Current 2026 page; no publication date displayed. [Official page](https://dier.gov.mt/en/services/employment-conditions/wages/national-minimum-wage/). Pinpoint: 2026 EUR 229.44 minimum and statement that every employee is entitled to statutory bonus and weekly allowance.
8. **Department of Social Security, “Maternity / Adoption Leave Trust Claim.”** Current service page; no publication date displayed. [Official page](https://socialsecurity.gov.mt/en/benefits-and-services/maternity-adoption-leave-trust-claim-dss/). Pinpoints: private-sector scope, public-sector exemptions, employer-only 0.3%, no wage deduction.
9. **MTCA, “FSS System — Employers FSS registration.”** Current page; no publication date displayed. [Official page](https://mtca.gov.mt/business-tax/fss-system). Pinpoints: tax from gross emoluments, separate tax and SSC deductions, FS3/FS7 reconciliation by 15 February.
10. **Legislation Malta, Social Security Act (Cap. 318).** Consolidated official PDF published/current as of 2026. [Official PDF](https://legislation.mt/getpdf/69d6033d6fe5fd3994d1710c). Pinpoint: Tenth Schedule basis for Class 1 and Maternity contribution tables; current consolidation includes 2026 amendments.
11. **Legislation Malta, Income Tax Act (Cap. 123).** Consolidated official PDF published/current as of 2026. [Official PDF](https://legislation.mt/getpdf/69d5fc0c6fe5fd3994d170f8). Pinpoints: Article 4(1)(b) employment gains and Article 56 rates, as operationalised in MTCA's 2026 table.

## 9. Evidence assessment and unresolved details

**Strongest evidence:** MTCA's 2026-specific tax and Class 1 tables directly provide every rate, threshold, cap and weekly-rounding instruction used in the calculations. DIER directly gives the four statutory cash amounts, and Social Security explicitly excludes bonuses/allowances from basic weekly wage.

**Weakest evidence:** MTCA's HTML tables do not display their own publication dates, although they are labelled 2026 and the associated government service is dated 2026-04-28. The FSS page establishes tax on gross emoluments but does not provide a worked 2026 annual single-person example; the arithmetic is therefore independently reproduced from MTCA's published annual formula.

**Unresolved / implementation caution:** official pages reviewed do not consolidate every periodic FSS withholding rounding rule into the annual rate page. The dossier computes final annual liability and statutory weekly SSC rounding, not a month-by-month payslip simulation. A product must also decide whether its “annual gross” field means total cash including the EUR 512.52 or contractual basic salary excluding it; both cannot be true simultaneously.
