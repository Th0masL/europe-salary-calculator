# Cyprus employee payroll, tax year 2026 — clean-room research dossier

**Access/research date:** 2026-10-04  
**Scope:** Cyprus-resident, single employee aged 30, no children, ordinary private employment, equal cash salary in 12 monthly payrolls, no first-employment exemption, pension/provident contribution, life insurance, housing/green deduction, benefit in kind, or other income. All calculations were independently reconstructed from Cyprus government, Tax Department, and Social Insurance Services material.

## Headline result

For 2026 the employee pays **8.8% social insurance** on monthly earnings up to **EUR 5,742**, plus **2.65% General Health System (GHS/GeSY)** on earnings up to **EUR 180,000 annually**. The employer pays **8.8% social insurance**, **1.2% Redundancy Fund**, and **0.5% Human Resource Development levy** on the monthly-capped base, **2% Social Cohesion Fund without a ceiling**, and **2.9% GHS up to EUR 180,000**.

The Central Holiday Fund is employer-specific. The primary calculation below assumes an employer has obtained an exemption and pays normal salary during annual leave. A second scenario shows a non-exempt five-day-week employer at the statutory minimum **8%** Holiday Fund rate. This distinction materially changes both employer cost and, in some cases, employee contribution deductions.

The 2026 PIT bands apply to taxable income after permitted deductions. Mandatory employee social insurance and GHS are deductible, subject to the common one-fifth limit; under every worked example those two deductions alone remain within that limit.

## 1. Personal income tax

The Tax Department's **“Individual Income Tax Return”** page labels the following table **“From Tax Year 2026 onwards (Tax Reform)”**:

| Taxable income | Marginal rate | Tax through top of band |
|---:|---:|---:|
| EUR 0–22,000 | 0% | 0 |
| EUR 22,001–32,000 | 20% | 2,000 |
| EUR 32,001–42,000 | 25% | 4,500 cumulative |
| EUR 42,001–72,000 | 30% | 13,500 cumulative |
| Above EUR 72,000 | 35% | `13,500 + 35% × (income − 72,000)` |

The EUR 22,000 amount is a zero-rate band, not a refundable credit.

### Deductions and allowances

Form **T.D.59A 2026, “Declaration for Claiming Tax Deductions for the Tax Year 2026 – Income Tax”**, instructions 10 and 19–21, establishes the payroll order. Contributions to approved life/medical, GHS, pension/provident and Social Insurance arrangements share a ceiling of **one fifth of the intermediate taxable-income calculation**. In this dossier there are no voluntary contributions; actual employee Social Insurance and GHS contributions are both deductible and their total never reaches 20% of gross/intermediate income.

The 2026 reform also introduced personal deductions subject to facts and income criteria, including deductions connected with dependent children/students, qualifying main-home rent or mortgage interest, qualifying green expenditure/electric vehicles, and home insurance against specified risks. None is automatic. They are zero here because the facts provide no child or qualifying expenditure. First-employment exemptions (including 20%, capped at EUR 8,550, and qualifying 50% regimes) are also excluded because eligibility was not specified.

For the stated case:

`taxable_income = gross_cash_salary − employee_social_insurance − employee_GHS`

`PIT = progressive_2026_rates(taxable_income)`

`net_cash = gross_cash_salary − employee_social_insurance − employee_GHS − PIT`

The employer withholds through PAYE. T.D.59A instructs the employer to estimate annual income/deductions and calculate the tax; bonuses and other non-ad-hoc income are taxed in the month paid. From tax year 2026, the Tax Department states that individual returns are submitted through Tax For All; a resident aged 25–70 is within the filing rule irrespective of income.

## 2. Social Insurance Fund

The Social Insurance statutory schedule gives, for contribution years beginning 2024 through 2028:

- employee: **8.8%**;
- employer: **8.8%**; and
- state: **5.2%** (not an employer payroll cost).

The Social Insurance Services notice **“Notice to employers regarding the maximum earnings … 2026,”** dated 2026-01-15 (notice text dated December 2025), sets the ceiling at **EUR 1,325 weekly from 2026-01-05** and **EUR 5,742 monthly from 2026-01-01**. It expressly applies the ceiling to Social Insurance, Annual Paid Leave, Redundancy, and Human Resource Development contributions.

For an evenly paid monthly employee:

`annual_SI_base = 12 × min(monthly_contributory_earnings, 5,742)`

The maximum annual base is therefore **EUR 68,904**. This annual number is only a consequence of 12 equal monthly periods: the legal ceiling is monthly and unused capacity does not freely move between months.

## 3. GHS (GeSY)

The Tax Department's official **“Guidance for GHS 2023”**, dated 2023-04-12, gives the continuing rates from 2020-07-01: **2.65% employee** and **2.90% employer**, and states that the maximum income subject to GHS is **EUR 180,000**. The Social Insurance Services employer-contributions page confirms the same rates and annual ceiling.

For the stated single employment:

`GHS_base = min(GHS_contributory_earnings, 180,000)`

The ceiling is annual, unlike the monthly Social Insurance ceiling. If excess GHS has been withheld across income sources, the official guidance points to the Health Insurance Organisation refund procedure.

## 4. Employer-only funds

| Fund | Rate | Ceiling/base | Status for ordinary private employer |
|---|---:|---|---|
| Redundancy Fund | 1.2% | Monthly SI ceiling | Employer-only |
| Human Resource Development levy | 0.5% | Monthly SI ceiling | Employer-only |
| Social Cohesion Fund | 2.0% | Total earnings, **no ceiling** | Employer-only |
| Central Holiday Fund | 8%–16% according to leave entitlement | Monthly SI ceiling | Employer-only unless approved exemption |

These rates and bases are set out on the Ministry of Labour/Social Insurance Services **“Employer Registration — Contributions”** page. Its wording is particularly useful: capped earnings apply to Social Insurance, Holiday, Redundancy and HRD; total earnings without a maximum apply to Social Cohesion; GHS has its separate EUR 180,000 annual ceiling.

### Central Holiday Fund choice

The official **“Annual Leave — Obligations of the Employer”** table (last update 2021-04-14) gives, for a five-day week, **8% for 20 leave days**, increasing by entitlement to 16% for 40 days. For a six-day week, 24 days begins at 8%. An employer that gives paid leave on terms more favourable than the statutory minimum may apply for an exemption using form Y.K.A. 1-005; an exemption is not automatic.

Social Insurance Services' official worked examples show the interaction:

- non-exempt employer: EUR 1,000 earnings + EUR 80 Holiday Fund contribution = EUR 1,080 contribution earnings, on which SI, Redundancy, HRD, Social Cohesion and GHS are calculated; and
- exempt employer paying leave directly: those contributions are calculated on EUR 1,000.

Accordingly, this dossier presents:

1. **Primary scenario — approved exemption:** Holiday Fund contribution zero; employee receives normal salary while on leave.
2. **Alternative — non-exempt, five-day week, 20 days:** employer contributes 8% on earnings up to the monthly ceiling; that contribution enters the other contribution bases, subject to each fund's own ceiling.

The zero contribution in scenario 1 is an employer-status assumption, not a universal Cyprus exemption.

## 5. Thirteenth salary and calculation timing

The official Social Insurance employer guide includes basic salary, overtime, commissions and **13th/14th salary** in insurable earnings. It says earnings payable for periods exceeding a week/month (13th salary, 54th week, commissions, etc.) are included up to the amount which, when added to earnings for that period, does not exceed the applicable maximum. T.D.59A likewise includes wages, bonuses and other remuneration in taxable employment income and directs withholding in the payment month.

Therefore:

- a contractual 13th salary is not exempt from PIT, GHS, SI, or the employer funds merely because of its label;
- PIT is ultimately annual, so dividing the same annual cash salary into 12 or 13 payments does not change final annual PIT absent rounding;
- the monthly EUR 5,742 ceiling can make SI/Redundancy/HRD/Holiday results depend on the actual payroll allocation; and
- GHS remains subject to its annual EUR 180,000 ceiling and Social Cohesion remains uncapped.

The examples use 12 equal monthly payments, not a 13th salary. A 13-payment contract must be modelled by actual pay period rather than by reusing the annual figures mechanically.

## 6. Worked calculations — primary Holiday Fund-exempt scenario

Shared formulas for annual gross `G`, paid `G/12` monthly:

`S = min(G, 12 × 5,742) = min(G, 68,904)`

`H = min(G, 180,000)`

`employee deductions = 8.8% × S + 2.65% × H`

`employer charges = (8.8% + 1.2% + 0.5%) × S + 2% × G + 2.9% × H`

### Detailed intermediates

| Annual gross | SI base `S` | GHS base `H` | Employee SI 8.8% | Employee GHS 2.65% | Taxable income | PIT | Net cash |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 20,000 | 20,000 | 1,760.00 | 530.00 | 17,710.00 | 0.00 | **17,710.00** |
| 60,000 | 60,000 | 60,000 | 5,280.00 | 1,590.00 | 53,130.00 | 7,839.00 | **45,291.00** |
| 100,000 | 68,904 | 100,000 | 6,063.55 | 2,650.00 | 91,286.45 | 20,250.26 | **71,036.19** |
| 200,000 | 68,904 | 180,000 | 6,063.55 | 4,770.00 | 189,166.45 | 54,508.26 | **134,658.19** |
| 600,000 | 68,904 | 180,000 | 6,063.55 | 4,770.00 | 589,166.45 | 194,508.26 | **394,658.19** |

PIT checks:

- EUR 60,000: `2,000 + 2,500 + 30% × (53,130 − 42,000) = 7,839`.
- EUR 100,000: `13,500 + 35% × (91,286.448 − 72,000) = 20,250.2568`.
- EUR 200,000: `13,500 + 35% × (189,166.448 − 72,000) = 54,508.2568`.

### Employer intermediates and cost

| Gross | Employer SI 8.8% | Redundancy 1.2% | HRD 0.5% | Social cohesion 2% | Employer GHS 2.9% | Total employer charges | Total employer cost |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 1,760.00 | 240.00 | 100.00 | 400.00 | 580.00 | 3,080.00 | **23,080.00** |
| 60,000 | 5,280.00 | 720.00 | 300.00 | 1,200.00 | 1,740.00 | 9,240.00 | **69,240.00** |
| 100,000 | 6,063.55 | 826.85 | 344.52 | 2,000.00 | 2,900.00 | 12,134.92 | **112,134.92** |
| 200,000 | 6,063.55 | 826.85 | 344.52 | 4,000.00 | 5,220.00 | 16,454.92 | **216,454.92** |
| 600,000 | 6,063.55 | 826.85 | 344.52 | 12,000.00 | 5,220.00 | 24,454.92 | **624,454.92** |

## 7. Alternative employer scenario — non-exempt, 8% Holiday Fund

For equal monthly gross, first calculate the Holiday Fund on the monthly-capped salary:

`CHF = 8% × min(G, 68,904)`

`X = G + CHF` (augmented contribution earnings)

`S2 = 12 × min((G/12) + 8% × min(G/12, 5,742), 5,742)`

`H2 = min(X, 180,000)`

Employee SI/GHS and tax use the actual employee contributions generated from `S2` and `H2`. Employer cost includes CHF itself plus SI, Redundancy, HRD, Social Cohesion and GHS on their respective bases.

| Gross | CHF | SI-family base `S2` | GHS base `H2` | Employee deductions | PIT | Net cash | Employer charges incl. CHF | Employer cost |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 1,600.00 | 21,600.00 | 21,600.00 | 2,473.20 | 0.00 | **17,526.80** | 4,926.40 | **24,926.40** |
| 60,000 | 4,800.00 | 64,800.00 | 64,800.00 | 7,419.60 | 7,674.12 | **44,906.28** | 14,779.20 | **74,779.20** |
| 100,000 | 5,512.32 | 68,904.00 | 105,512.32 | 8,859.63 | 20,199.13 | **70,941.24** | 17,917.34 | **117,917.34** |
| 200,000 | 5,512.32 | 68,904.00 | 180,000.00 | 10,833.55 | 54,508.26 | **134,658.19** | 22,077.49 | **222,077.49** |
| 600,000 | 5,512.32 | 68,904.00 | 180,000.00 | 10,833.55 | 194,508.26 | **394,658.19** | 30,077.49 | **630,077.49** |

At EUR 100,000, for example, employer charges are CHF 5,512.32 + SI 6,063.55 + Redundancy 826.85 + HRD 344.52 + Social Cohesion 2,110.25 + employer GHS 3,059.86 = EUR 17,917.34.

All figures retain full precision until final display. Live payroll may differ by cents because deductions and PAYE are calculated and rounded by pay period.

## 8. Universal rules and variables

| Fixed for the stated employee | Requires employer/employee facts |
|---|---|
| 2026 PIT bands | New personal deductions and income tests |
| SI rate 8.8% each side | Actual month-by-month pay/bonus allocation |
| Monthly SI-family ceiling EUR 5,742 | Approved Holiday Fund exemption and leave entitlement |
| GHS 2.65% employee / 2.9% employer, EUR 180,000 annual ceiling | First-employment and other special tax exemptions |
| Redundancy 1.2%; HRD 0.5%; Social Cohesion 2% | Provident/pension plan and collective-agreement costs |
| Social Cohesion has no maximum | Benefits in kind and other taxable remuneration |

## 9. Primary-source register

All links accessed 2026-10-04.

1. **Cyprus Tax Department, “Individual Income Tax Return.”** Published 2026-07-06 according to the Department's index. [Official page](https://www.gov.cy/mof-tax/en/documents/forologiki-dilosi-eisodimatos-atomoy/). Pinpoints: “From Tax Year 2026 onwards (Tax Reform)” band table; post-reform filing obligation.
2. **Cyprus Tax Department, “Tax Reform 2026.”** Posted 2026-05-29; linked guides/forms revised 2026-05-11. [Official page](https://www.gov.cy/mof-tax/en/documents/forologiki-metarrythmisi-2026/). Pinpoint: Natural Persons section linking T.D.59A, explanatory guide, FAQs, examples and withholding tool.
3. **Cyprus Tax Department, “T.D.59A 2026 — Declaration for Claiming Tax Deductions for the Tax Year 2026 – Income Tax.”** Published 2026-01. [Official PDF](https://www.gov.cy/media/sites/29/2026/01/IR59_2026_English__.pdf). Pinpoints: employee note 10 (one-fifth deduction limit), employer notes 15–22 (income, known contributions, calculation and GHS ceiling), tax table.
4. **Cyprus Tax Department, “Tax Reform 2026 — natural persons.”** Revised 2026-05-11. [Official PDF](https://www.gov.cy/media/sites/29/2026/05/%CE%A6%CE%BF%CF%81%CE%BF%CE%BB%CE%BF%CE%B3%CE%B9%CE%BA%CE%AE-%CE%9C%CE%B5%CF%84%CE%B1%CF%81%CF%81%CF%8D%CE%B8%CE%BC%CE%B9%CF%83%CE%B7-2026-%CF%86%CF%85%CF%83%CE%B9%CE%BA%CE%AC-%CF%80%CF%81%CF%8C%CF%83%CF%89%CF%80%CE%B1-11.05.2026.pdf). Pinpoint: new personal deductions and Cyprus-residence/income conditions.
5. **Social Insurance Services, “Notice to Employers Regarding the Maximum Earnings … 2026.”** Posted 2026-01-15; notice dated December 2025; effective 2026-01-01 monthly / 2026-01-05 weekly. [Official notice](https://sisweb.mlsi.gov.cy/anotato2025/). Pinpoints: EUR 1,325 weekly and EUR 5,742 monthly; named capped funds.
6. **Social Insurance Services, “Employer's Guide.”** Official guide, publication date not displayed in the document; official site metadata/search index dates the web copy to 2014. [Official PDF](https://www.mlsi.gov.cy/mlsi/sid/sidv2.nsf/All/551C82BEE69E2FC9C2257A170034B0EC/%24file/Employer%27s%20Guide.pdf). Pinpoints: statutory contribution schedule (8.8% each employee/employer from 2024 through 2028); 13th/14th salary; Holiday Fund addition to contribution earnings; employer-only fund rates.
7. **Social Insurance Services / Ministry of Labour, “Employer Registration — Contributions.”** Last update 2021-03-23. [Official page](https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/EA4F396F80C4BAA8C22586A10042659F). Pinpoints: capped versus uncapped bases, fund rates, EUR 180,000 GHS ceiling, exempt/non-exempt Holiday Fund examples. The displayed SI example is historical (8.3%); the 2026 SI rate comes from source 6.
8. **Social Insurance Services, “Examples for payment of Contributions …”** Page last modified 2026-09-25; example itself concerns June 2020. [Official page](https://www.mlsi.gov.cy/mlsi/sid/sidv2.nsf/0/1822b48cf5e6a3cec225859d0021bc52?Click=&OpenDocument=). Pinpoints: lines/examples for EUR 1,000 + EUR 80 CHF = EUR 1,080 bases, and exempt-employer EUR 1,000 bases. Used for calculation mechanics, not the historical SI percentage.
9. **Department of Labour Relations, “Annual Leave — Obligations of the Employer.”** Last update 2021-04-14. [Official page](https://www.mlsi.gov.cy/mlsi/sdg/sdg.nsf/All/00DDEF169CC27CAEC22586B7003F35FE). Pinpoints: five-/six-day rate tables; exemption conditions and form Y.K.A. 1-005.
10. **Cyprus Tax Department, “Guidance for GHS 2023.”** Dated 2023-04-12. [Official PDF](https://www.mof.gov.cy/mof/TAX/taxdep.nsf/All/C858F987BBC522B1C2258997003F3864/%24file/Guidance%20for%20GHS%202023.pdf). Pinpoints: rate table (2.65% employee, 2.90% employer from 2020-07-01), EUR 180,000 maximum, excess-withholding refund.
11. **Human Resource Development Authority, “The HRDA and Its Mission.”** Current official page; no publication date displayed. [Official page](https://www.anad.org.cy/wps/portal/hrda/hrdaExternal/anad/mission%20Page/). Pinpoint: every employer levy of 0.5% of employee emoluments; the payroll ceiling is supplied by source 5.

## 10. Evidence assessment and unresolved items

**Strongest evidence:** the Tax Department's 2026-specific return page and T.D.59A directly establish the new bands and deduction order; the Social Insurance Services' dated 2026 ceiling notice gives the exact current ceiling and affected funds. The statutory contribution schedule fixes 8.8% for 2024–2028, covering 2026 without extrapolation.

**Weakest evidence:** the clearest official consolidated employer-fund mechanics page retains a 2020 numerical SI example, although its base rules and the 1.2%/0.5%/2% rates are current and the 2026 SI rate/ceiling are independently supplied by newer official sources. The official Employer's Guide lacks a visible publication date. Neither weakness changes the calculations because historical example rates were not reused.

**Unresolved / implementation caution:** official public guidance reviewed does not state every pay-period cent-rounding convention in one place. Results are therefore annual full-precision illustrations. Holiday Fund exemption must be verified for the actual employer, and a 13th-salary contract must be calculated using its actual pay-period attribution. No undocumented exemption from Redundancy, HRD, Social Cohesion, SI, or GHS is assumed.
