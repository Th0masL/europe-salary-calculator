# Bulgaria employee payroll, tax year 2026 — clean-room research dossier

**Research cut-off/access date:** 2026-10-04.
**Scope:** resident, single employee aged 30, no children or other reliefs, one ordinary private-sector labour contract, third category of labour, equal regular cash salary in all 12 months. This is an independent reconstruction from Bulgarian primary official sources only. It does not rely on calculator code, generated data, prior audits, or another country dossier.

## Executive result

Bulgaria changed its social-insurance ceiling during 2026. It also adopted the euro on 1 January 2026. The legal payroll currency is therefore EUR, even though the requested examples are denominated in BGN. This dossier converts at the irrevocable official rate **EUR 1 = BGN 1.95583** and presents BGN-equivalent results for comparability.

For the chosen office scenario (NACE/KID 82, occupation group 4, clerical support), an employee born after 1959 bears **13.78%** social and health contributions on monthly insurable pay, and the employer bears **18.52% plus occupational-accident risk**. The selected risk rate is **0.4% through July and 0.5% from August**. PIT is **10% of gross taxable employment income less employee mandatory social and health contributions**. There is no assumed personal allowance or tax relief.

The maximum monthly insurance base is **EUR 2,111.64 for January–July** and **EUR 2,300 for August–December**. Thus, for a salary above both ceilings throughout the year, the unrounded annual maximum base is EUR 26,281.48, or BGN 51,402.1070284 at the fixed conversion rate.

## Currency and modelling convention

The Ministry of Finance announcement **“Bulgaria successfully joined the euro area”**, dated 2026-01-07, states that the euro became Bulgaria's official currency on 2026-01-01. A Ministry written answer dated 2025-09-15 states that lev amounts convert automatically at the official rate **EUR 1 = BGN 1.95583**.

The examples therefore use:

`annual EUR gross = requested annual BGN gross / 1.95583`

and translate the resulting unrounded annual components back to BGN at the same rate. A production payroll must calculate each month in EUR and apply the statutory cent-rounding rules. The annual illustrations intentionally retain full precision before the final two-decimal display; small cent-level differences from summing twelve rounded payslips are therefore possible.

## Statutory calculation

### 1. Monthly insurable income

For workers and employees, NSSI's page **“Осигуряване на работници и служители”** says contributions are based on gross monthly remuneration, not below the minimum by economic activity and occupational group, and not above the maximum monthly insurable income.

For month `m`:

`insurance_base_m = min(max(gross_m, applicable_minimum_m), maximum_m)`

The 2026 State Social Security Budget Act, promulgated in **State Gazette No. 68 of 2026-07-28**, provides the following two periods:

| Period | Maximum monthly base | General self-employed minimum (not the employee floor) |
|---|---:|---:|
| 1 Jan–31 Jul | EUR 2,111.64 | EUR 550.66 |
| 1 Aug–31 Dec | EUR 2,300.00 | EUR 620.20 |

Pinpoint: 2026 SSS Budget Act §9 (official PDF pp. 3–4); NSSI's 2026-08-06 explanatory table, lines headed **“Осигурителен доход”**.

The employee minimum is not one universal minimum wage figure; it varies by main economic activity and occupational group. To make the scenario reproducible, this dossier chooses **KID 82 (office administrative and support activities), occupation group 4 (“Помощен административен персонал” / clerical support)**:

| Period | Scenario minimum | Pinpoint |
|---|---:|---|
| Jan–Jul | BGN 1,077 = EUR 550.66 monthly | official 2025 Appendix 1A, K/M/N/O block including code 82, group-4 column; carried into the first 2026 period by 2026 Act §9 |
| Aug–Dec | EUR 716 monthly | 2026 Act Appendix 1A, K/M/N/O block including code 82, group-4 column |

All five examples exceed those floors in every month, so the selected occupation group does not change their numerical results.

### 2. Employee and employer contribution rates

The NRA's official **“Table of the rates of insurance contributions for 2026”**, issued with instruction ВК-30-10237/2026-08-12, row 1.2 (labour-contract worker born after 31 December 1959), supplies the controlling 2026 totals and allocation. The health split is separately confirmed by NRA's 2026 health-contribution page.

| Component | Employee | Employer | Total | Treatment |
|---|---:|---:|---:|---|
| State pension fund | 6.58% | 8.22% | 14.80% | insurance base, capped monthly |
| General sickness and maternity | 1.40% | 2.10% | 3.50% | insurance base, capped monthly |
| Unemployment | 0.40% | 0.60% | 1.00% | insurance base, capped monthly |
| Universal pension fund (born after 1959) | 2.20% | 2.80% | 5.00% | insurance base, capped monthly |
| Health insurance | 3.20% | 4.80% | 8.00% | insurance base, capped monthly |
| Occupational accident/disease (ТЗПБ) | 0% | variable | variable | employer only; risk-class rate |
| **Subtotal excluding ТЗПБ** | **13.78%** | **18.52%** | **32.30%** | |

The current 2026 NRA table explicitly shows employee DОО + universal-pension-fund **10.58%** (8.38% DОО + 2.20% universal fund), employer **13.72% + ТЗПБ** (10.92% DОО + 2.80% universal fund), and health **3.20% employee / 4.80% employer**. The fund-level DОО split above is the ordinary 60:40 allocation reflected in the Social Security Code and is cross-checked by NSSI's official contribution-history table; the current table is authoritative for the 2026 aggregates.

### 3. Occupational-accident risk scenario

ТЗПБ is entirely employer-paid and varies by the employer's principal economic activity. NSSI's **“НОИ разяснява: какво се променя във вноските за фонд ‘Трудова злополука и професионална болест’ от 1 август 2026 г.”**, dated 2026-08-05, gives a statutory range of **0.4%–1.1%** and specifically identifies KID 82 as changing from **0.4% for January–July to 0.5% for August–December**. These match Appendix 2 and Appendix 2A of the 2026 Budget Act.

This is a selected risk-class scenario, not a universal employer rate:

`risk = 0.004 × sum(Jan–Jul insurance bases) + 0.005 × sum(Aug–Dec insurance bases)`

### 4. PIT and calculation order

The consolidated 2026 Personal Income Taxes Act (ЗДДФЛ) provides:

- Article 25(1): annual employment tax base equals taxable employment income under Article 24 less mandatory employee social-security and health-insurance contributions withheld by the employer.
- Article 42(2)–(4): the employer determines the monthly tax base after those employee mandatory contributions and withholds advance tax.
- Article 48(1): tax on the general annual tax base is **10%**.
- Article 49: the main employer performs the annual employment-income tax reconciliation; NRA's **“Трудов договор”** page says a taxpayer with only employment income need not file if the employer has determined the annual tax at 31 December and withheld/remitted it in full by 31 January of the following year.

For the assumptions here (no reliefs):

`employee contributions = 13.78% × insurance base`

`PIT base = gross cash salary − employee contributions`

`PIT = 10% × PIT base`

`employee net = gross − employee contributions − PIT`

The insurance cap limits contributions, not taxable salary. PIT therefore continues to grow above the cap.

### 5. Employer-only charges and contingent costs

- **Guaranteed claims fund (ГВРС): 0% in 2026.** Section 15(1) of the 2026 State Social Security Budget Act says no contributions are due to the fund for 2026; NRA's current fund-rate page says the same. This is not added to employer cost.
- **Sick leave:** NSSI's official employer procedure, citing Social Security Code Article 40(5), says that for incapacity beginning after 2023 the employer pays the **first two working days at 70%** of the relevant average daily gross remuneration (subject to the stated floor and six-month coverage condition). This is event-contingent, not a fixed payroll percentage, so the worked examples assume no sick leave and add zero.
- Severance, overtime premiums, benefits in kind, labour-law leave timing, voluntary benefits, and collective-agreement costs are not universal fixed employer levies and are outside the regular-cash-salary examples.

## Worked calculations

### Shared intermediates

For equal monthly salary `M = G / 12` (shown in requested BGN-equivalent units):

- January–July ceiling: `EUR 2,111.64 × 1.95583 = BGN 4,130.0088612`.
- August–December ceiling: `EUR 2,300 × 1.95583 = BGN 4,498.409`.
- Fully capped annual base: `7 × EUR 2,111.64 + 5 × EUR 2,300 = EUR 26,281.48 = BGN 51,402.1070284`.
- Employee contribution components are `6.58%, 1.40%, 0.40%, 2.20%, 3.20%` of the annual insurance base.
- Employer components before risk are `8.22%, 2.10%, 0.60%, 2.80%, 4.80%` of that base.

Values below are rounded to BGN 0.01 only for display.

### BGN 40,000 annual gross

Monthly gross is BGN 3,333.33, below both ceilings and above both scenario floors. Annual insurance base is therefore BGN 40,000.00.

| Item | Formula | BGN |
|---|---|---:|
| Employee pension | 40,000 × 6.58% | 2,632.00 |
| Employee sickness/maternity | 40,000 × 1.40% | 560.00 |
| Employee unemployment | 40,000 × 0.40% | 160.00 |
| Employee universal pension | 40,000 × 2.20% | 880.00 |
| Employee health | 40,000 × 3.20% | 1,280.00 |
| **Employee contributions** | 40,000 × 13.78% | **5,512.00** |
| PIT base | 40,000 − 5,512 | 34,488.00 |
| PIT | 34,488 × 10% | 3,448.80 |
| **Net salary** | 40,000 − 5,512 − 3,448.80 | **31,039.20** |
| Employer pension | 40,000 × 8.22% | 3,288.00 |
| Employer sickness/maternity | 40,000 × 2.10% | 840.00 |
| Employer unemployment | 40,000 × 0.60% | 240.00 |
| Employer universal pension | 40,000 × 2.80% | 1,120.00 |
| Employer health | 40,000 × 4.80% | 1,920.00 |
| Employer ТЗПБ | 7 × (40,000/12) × 0.4% + 5 × (40,000/12) × 0.5% | 176.67 |
| **Employer contributions** | 40,000 × 18.52% + 176.67 | **7,584.67** |
| **Employer cost** | 40,000 + 7,584.67 | **47,584.67** |

### Above-cap salaries

Each remaining monthly gross exceeds both monthly ceilings. Consequently, each uses the same annual insurance base, employee contributions, employer contributions, and risk charge:

| Capped-base component | Formula | BGN |
|---|---|---:|
| Employee pension | 51,402.1070284 × 6.58% | 3,382.26 |
| Employee sickness/maternity | base × 1.40% | 719.63 |
| Employee unemployment | base × 0.40% | 205.61 |
| Employee universal pension | base × 2.20% | 1,130.85 |
| Employee health | base × 3.20% | 1,644.87 |
| **Employee contributions** | base × 13.78% | **7,083.21** |
| Employer pension | base × 8.22% | 4,225.25 |
| Employer sickness/maternity | base × 2.10% | 1,079.44 |
| Employer unemployment | base × 0.60% | 308.41 |
| Employer universal pension | base × 2.80% | 1,439.26 |
| Employer health | base × 4.80% | 2,467.30 |
| Employer ТЗПБ | 7 × 4,130.0088612 × 0.4% + 5 × 4,498.409 × 0.5% | 228.10 |
| **Employer contributions** | base × 18.52% + 228.10 | **9,747.77** |

| Annual gross (BGN) | Insurance base | Employee contributions | PIT base | PIT (10%) | Net salary | Employer contributions | Employer cost |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 120,000.00 | 51,402.11 | 7,083.21 | 112,916.79 | 11,291.68 | **101,625.11** | 9,747.77 | **129,747.77** |
| 200,000.00 | 51,402.11 | 7,083.21 | 192,916.79 | 19,291.68 | **173,625.11** | 9,747.77 | **209,747.77** |
| 400,000.00 | 51,402.11 | 7,083.21 | 392,916.79 | 39,291.68 | **353,625.11** | 9,747.77 | **409,747.77** |
| 1,200,000.00 | 51,402.11 | 7,083.21 | 1,192,916.79 | 119,291.68 | **1,073,625.11** | 9,747.77 | **1,209,747.77** |

Example at BGN 120,000: `PIT base = 120,000 − 7,083.2103485 = 112,916.7896515`; `PIT = 11,291.6789651`; `net = 101,625.1106863`.

## Universal rules versus selected variables

| Universal for this employee type | Employer/employee-specific variable |
|---|---|
| 10% PIT rate and deduction of mandatory employee contributions | Tax reliefs and non-cash taxable benefits |
| 13.78% employee aggregate contribution rate | Economic-activity code and occupational group determining the minimum base |
| 18.52% employer aggregate before ТЗПБ | ТЗПБ risk rate (0.4%–1.1%); KID 82 selected here |
| Monthly maximum bases and mid-year change | Actual monthly remuneration pattern; a bonus month cannot borrow unused cap from another month |
| Zero ГВРС contribution for 2026 | Sick-leave events and other contingent labour costs |

## Evidence register

All sources were accessed 2026-10-04.

1. **National Social Security Institute (NSSI), “Закон за бюджета на държавното обществено осигуряване за 2026 г.”** Official PDF, State Gazette No. 68, 2026-07-28; relevant provisions effective 2026-08-01 where stated. [Official PDF](https://www.noi.bg/wp-content/uploads/zbdoo-2026.pdf). Pinpoints: §9 (two periods, minimum/maximum bases), §14 and Appendices 2/2A (ТЗПБ), §15(1) (zero ГВРС), Appendix 1A K/M/N/O–82 row and occupation-group headings.
2. **NSSI, “НОИ РАЗЯСНЯВА: От 1 август 2026 г.: нови размери на осигурителния доход; осигурителни вноски за нова група осигурени лица,”** published 2026-08-06. [Page](https://www.noi.bg/dohod01082026/). Pinpoint: table under “2. Осигурителен доход,” EUR 2,111.64 / 2,300 maximum.
3. **NSSI, “НОИ разяснява: какво се променя във вноските за фонд ‘Трудова злополука и професионална болест’ от 1 август 2026 г.,”** published 2026-08-05. [Page](https://www.noi.bg/tzpb01082026/). Pinpoint: employer-only range 0.4%–1.1%; KID 82 row, 0.4% then 0.5%.
4. **NRA, “Таблица за размера на осигурителните вноски за 2026 г.”** Attachment 1 to instruction ВК-30-10237 of 2026-08-12. [Official PDF](https://nra.bg/wps/wcm/connect/nra.bg25863/6f117462-1836-48f8-9e27-a4b02a1e55fb/%D0%9F%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_1_%D0%92%D0%9A-30-10237_12.08.2026.pdf?MOD=AJPERES). Pinpoint: row 1.2 for labour-contract persons born after 1959: DОО + universal fund totals/allocation, health 8%, and two maximum bases.
5. **NRA, “Размер на осигурителни вноски за здравно осигуряване,”** current 2026 page; no page publication date displayed. [Page](https://nra.bg/wps/wcm/connect/agency/site/osiguryavane/zdravno-osiguryavane/razmer-osiguritelni-vnoski). Pinpoint: 2026 rate 8%, split 4.8% employer / 3.2% employee.
6. **NSSI, “Осигуряване на работници и служители,”** current page; no page publication date displayed. [Page](https://www.noi.bg/osiguriteli/osiguryavane_osiguriteli/osiguriavane-na-rabotnici-i-slujiteli-osiguriteli/). Pinpoint: gross remuneration, activity/occupation minimum, and monthly maximum-base rule.
7. **NRA, 2025 Budget Act Appendix 1A**, official table, published with the 2025 social-security budget materials. [Official PDF](https://nra.bg/wps/wcm/connect/nra.bg25863/30148150-99c4-4a68-8e5b-2d9df3ec6598/%D0%9F%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%2B%E2%84%961%D0%90%2B%D0%BA%D1%8A%D0%BC%2B%D1%87%D0%BB.%2B9%2C%2B%D1%82.%2B2%2B%D0%BE%D1%82%2B%D0%97%D0%91%D0%94%D0%9E%D0%9E%2B2025%2B%D0%B3..pdf). Pinpoint: K/M/N/O block including KID 82, occupation group 4 = BGN 1,077; carried into Jan–Jul 2026 under the 2026 Act.
8. **NRA, “Закон за данъците върху доходите на физическите лица” (consolidated 2026 PDF).** [Official PDF](https://nra.bg/wps/wcm/connect/nra.bg25863/e0daae38-32b9-40b7-8c21-ff7feed98935/%D0%97%D0%94%D0%94%D0%A4%D0%9B%2B2026.pdf?MOD=AJPERES). Original act effective 2007-01-01; the file is NRA's 2026 consolidated text, but the page exposes no precise consolidation timestamp. Pinpoints: Articles 25(1), 42, 48(1), 49.
9. **NRA, “Трудов договор,”** current page; no publication date displayed. [Page](https://nra.bg/wps/wcm/connect/agency/site/taxes/danak-vurhu-dohodite-na-fizicheski-lica/trudov-dogovor). Pinpoint: year-end employer reconciliation and no-filing condition for employment-only income.
10. **NSSI, “Изпълнение на законови задължения – краткосрочни обезщетения и помощи от ДОО,”** current page; no publication date displayed. [Page](https://www.noi.bg/osiguriteli/protseduri-za-izpylnenie-na-zakonovi-zadyljeniya/izpylnenie-zakonovi-zadyljenie-okp/). Pinpoint: first two working days at 70%, citing Social Security Code Article 40(5).
11. **Ministry of Finance, “Bulgaria successfully joined the euro area,”** published 2026-01-07. [Page](https://www.minfin.bg/bg/news/2026-01-07). Pinpoint: euro official currency from 2026-01-01.
12. **Ministry of Finance, written answer**, published 2025-09-15. [Page](https://www.minfin.bg/bg/wreply/13150). Pinpoint: automatic conversion and official rate EUR 1 = BGN 1.95583.

## Evidence assessment and unresolved points

**Strongest evidence:** the enacted 2026 State Social Security Budget Act and its appendices directly establish the split-year ceilings, minimum tables, risk schedules, and zero Guarantee Fund rate. The NRA's dated 2026 contribution table independently consolidates the contribution totals and allocation for precisely this worker category.

**Weakest evidence:** the exact fund-by-fund breakdown inside the DОО aggregate is less conveniently exposed in a single current 2026 HTML table; it is reconstructed from the statutory allocation and cross-checked against NSSI's official historical contribution table, while the current NRA table directly confirms the 8.38%/10.92% DОО aggregates. Also, several evergreen NRA/NSSI pages do not display publication/update dates. These limitations do not affect the aggregate employee deduction, PIT, net, or total employer-cost calculations.

**Unresolved:** the official web materials reviewed do not expose a simple machine-readable statement of every intermediate monthly cent-rounding rule. Accordingly, the examples are mathematically exact annual illustrations before final display rounding, not payslip reproductions. Employer-specific KID classification must be verified from the employer's actual principal activity; KID 82 is an explicit scenario, not a claim about every office employer.
