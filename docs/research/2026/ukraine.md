# Ukraine — employee payroll, calendar year 2026

**Independent clean-room dossier. Accessed 2026-10-04.** This reconstruction uses only official Ukrainian sources: the State Tax Service (DPS), Pension Fund of Ukraine (PFU), and legislation published by the Verkhovna Rada. It does not use repository calculator code, generated data, an existing Ukraine document, a prior audit, or another country dossier.

## Scope and reproducible assumptions

The employee is Ukrainian tax resident, age 30, single, without children or disability, employed under an ordinary private-sector labour contract for all of 2026. Compensation is cash salary only: no benefits in kind, pension contributions, reimbursed expenses, gifts, loans, tax discount, special industry status, Diia City regime, military service, or other income.

The stated annual gross is earned evenly over 12 calendar months. Formulae use the exact fraction `annual gross / 12`; displayed annual results are exact mathematical totals rounded to two decimals. Actual payroll must denominate each monthly payment in kopiykas. Where annual gross is not divisible by 12 kopiykas, allocation of the residual and payroll software's item-level rounding can move the sum of monthly deductions by a few kopiykas. The official sources found prescribe two-decimal reporting and general rounding for USC, but did not provide one universal item-level PIT/military-levy rounding algorithm. No false precision is inferred from that gap.

All five examples are far above the 2026 monthly minimum wage and the tax-social-privilege ceiling. They assume a complete month at the principal employment, so no minimum-USC exception or part-month issue arises.

## Headline results

Amounts are UAH per calendar year. The employee has no USC deduction.

| Annual gross | PIT, 18% | Military levy, 5% | Employee net | Employer USC | Base employer cost |
|---:|---:|---:|---:|---:|---:|
| 1,000,000.00 | 180,000.00 | 50,000.00 | 770,000.00 | 220,000.00 | 1,220,000.00 |
| 3,000,000.00 | 540,000.00 | 150,000.00 | 2,310,000.00 | 456,561.60 | 3,456,561.60 |
| 5,000,000.00 | 900,000.00 | 250,000.00 | 3,850,000.00 | 456,561.60 | 5,456,561.60 |
| 10,000,000.00 | 1,800,000.00 | 500,000.00 | 7,700,000.00 | 456,561.60 | 10,456,561.60 |
| 30,000,000.00 | 5,400,000.00 | 1,500,000.00 | 23,100,000.00 | 456,561.60 | 30,456,561.60 |

`Employee net = gross − PIT − military levy`.

`Base employer cost = gross + employer USC`.

The employer-cost column excludes event-dependent sick pay, occupational-accident sick pay, paid leave already contained in annual salary, contractual benefits, and payroll administration. There is no separate employee-level statutory payroll percentage supported by the researched sources beyond employer USC.

## 1. Personal income tax (PIT / ПДФО)

DPS's official reproduction of Tax Code section IV states in article 167.1 that the rate is **18%** for salary and other incentive, compensation, and employment-related payments. The 2026 DPS payroll notice independently states that an employer withholds 18% PIT from accrued salary.

For monthly cash salary `S`:

```text
PIT base = S − applicable tax social privilege
PIT = 18% × PIT base
```

For this profile the privilege is zero, so annual PIT is simply `18% × annual gross`. Employer USC is an employer charge and is not deducted in computing the employee's PIT base.

The employer is the tax agent. Tax Code article 168.1.1 requires withholding from the employee's income; article 168.1.2 requires remittance when taxable income is paid. This is monthly payroll withholding, not a progressive annual band calculation.

### Tax social privilege (ПСП)

DPS's 2026 Knowledge Base answer gives:

- ordinary monthly privilege: **UAH 1,664** (50% of the UAH 3,328 working-age subsistence minimum at 1 January); and
- maximum monthly salary eligible for it: **UAH 4,660** (`3,328 × 1.4`, rounded to the nearest UAH 10).

It applies to salary from one employer for a reporting month, normally after an employee application. Even the lowest example pays about UAH 83,333.33 monthly, so none receives the privilege. It is not a general personal allowance and cannot be extrapolated annually.

The military-levy base is not reduced by the privilege: DPS explicitly says military levy applies to the full salary without subtracting PIT, funded-pension contributions, or the tax social privilege.

No child, disability, education, mortgage, donation, or other documented tax discount is assumed. Such relief is fact-specific and is not a standard deduction for the selected employee.

## 2. Military levy (військовий збір)

For an ordinary employee the rate is **5% of gross taxable salary**. DPS confirms both that employees are payers and that the 2026 rate for individuals, including employees, is 5% of the taxable object.

```text
military levy = 5% × gross salary
```

The 5% rate took effect for ordinary individual income accrued from **1 December 2024** under Law 4015-IX; the old 1.5% rate survives for specified military/service remuneration, which is outside this profile. The accrual period, rather than a delayed payment date, controls the transition.

This is still a temporary-code levy, but its end is no longer simultaneous with the end of martial law. DPS states that Law 4835-IX of 7 April 2026, effective **15 April 2026**, extended collection for three calendar years following the year in which martial law is ended or cancelled. Thus 5% applies throughout 2026 even if martial law later ends during 2026. Independently, Presidential Decree 596/2026, approved by Law 4928-IX, extended martial law from **05:30 on 2 August 2026 for 90 days**, so it was in force on the dossier's access date.

## 3. Unified social contribution (USC / ЄСВ)

### 3.1 Ordinary employer rate and bases

For the selected non-disabled ordinary employee, the employer rate is **22%**. DPS and PFU both describe it as an employer accrual; there is no employee USC withholding in the stated profile. The reduced 8.41% employer rate for qualifying employees with disabilities is outside scope.

The 2026 State Budget Act set:

- monthly minimum wage: **UAH 8,647** from 1 January 2026;
- minimum monthly USC for a complete qualifying principal-employment month: **UAH 1,902.34** (`8,647 × 22%`);
- ordinary maximum monthly USC base: **UAH 172,940**, equal to 20 minimum wages; and
- maximum monthly USC: **UAH 38,046.80** (`172,940 × 22%`).

The 2026 maximum is a special budget-year rule: State Budget Act article 32 suspends the otherwise applicable definition in Law 2464-VI for 2026. The separate 15-minimum-wage cap for military/police remuneration does not apply.

For each complete month here:

```text
USC base = min(max(monthly accrued salary, 8,647), 172,940)
employer USC = 22% × USC base
```

All examples exceed the minimum. DPS states that the base reporting period is the **calendar month** and that USC is charged on aggregate income for that month, subject to the maximum. The annual maximum for 12 capped months is therefore:

```text
12 × 38,046.80 = UAH 456,561.60
```

There is no annual true-up that lets unused cap in one month shelter income in another.

### 3.2 Included remuneration and bonuses

Law 2464-VI article 7, as quoted by DPS, includes basic and additional salary plus other incentive and compensation payments in the USC base. DPS's bonus guidance says employment-related supplements, allowances, and bonuses are salary and are taxed in the month **in which accrued**, even where they relate to an earlier period.

Consequently a cash bonus is subject to 18% PIT and 5% military levy like salary and enters that accrual month's aggregate USC base. The UAH 172,940 USC cap applies to the month's aggregate. A calculator cannot derive annual USC from annual compensation alone if bonus timing is unknown. The worked examples avoid that ambiguity by using 12 even accrual months.

For sickness, maternity, and annual-leave amounts covering more than one month, DPS says the maximum USC base is applied separately to the month to which each amount relates. That is a different allocation rule from an ordinary current-month bonus.

### 3.3 Rounding

DPS's official reporting guidance says monetary fields are completed in hryvnias with kopiykas and rounded to two decimal places under generally established rules. USC is formed employee-by-employee for each month. The table uses exact annual mathematical results because it is a tax-model comparison; an operational payroll should calculate and round each monthly reporting item and preserve the final salary residual. At UAH 1 million, for example, 11 payments of UAH 83,333.33 and a final UAH 83,333.37 can make the rounded annual USC UAH 219,999.97 rather than the exact-rate UAH 220,000.00. This is a rounding presentation difference, not a different rate.

## 4. Statutory sickness costs

These are contingent costs, not a salary percentage, and are excluded from the worked employer cost:

- ordinary illness: PFU guidance says the employer funds the **first five days**; PFU finances the benefit from day six;
- workplace accident or occupational disease at the employer where the insured event occurred: PFU's 6 July 2026 guidance says the employer pays **100% of average taxable salary for the first 17 days**, and PFU finances from day 18; and
- sickness payments themselves can enter the USC base and, when spanning months, are allocated to their respective months for the cap.

The amount cannot be calculated without an event, days absent, average-pay history, and insurance history. No actuarial reserve or invented percentage is added.

## 5. Worked calculations

The monthly amount shown is the exact annual fraction used for the model. `C = min(monthly gross, 172,940)`.

### Annual gross UAH 1,000,000

```text
monthly gross = 1,000,000 / 12 = 83,333.333333...
tax-social privilege = 0 because monthly gross > 4,660
PIT = 1,000,000 × 18% = 180,000.00
military levy = 1,000,000 × 5% = 50,000.00
employee net = 1,000,000 − 180,000 − 50,000 = 770,000.00

C = 83,333.333333...
employer USC = 12 × C × 22% = 220,000.00
base employer cost = 1,000,000 + 220,000 = 1,220,000.00
```

### Annual gross UAH 3,000,000

```text
monthly gross = 250,000.00; privilege = 0
PIT = 3,000,000 × 18% = 540,000.00
military levy = 3,000,000 × 5% = 150,000.00
employee net = 2,310,000.00

C = min(250,000, 172,940) = 172,940
monthly USC = 172,940 × 22% = 38,046.80
annual USC = 38,046.80 × 12 = 456,561.60
base employer cost = 3,456,561.60
```

### Annual gross UAH 5,000,000

```text
monthly gross = 416,666.666667; privilege = 0
PIT = 5,000,000 × 18% = 900,000.00
military levy = 5,000,000 × 5% = 250,000.00
employee net = 3,850,000.00

C = 172,940; annual USC = 12 × 38,046.80 = 456,561.60
base employer cost = 5,456,561.60
```

### Annual gross UAH 10,000,000

```text
monthly gross = 833,333.333333; privilege = 0
PIT = 10,000,000 × 18% = 1,800,000.00
military levy = 10,000,000 × 5% = 500,000.00
employee net = 7,700,000.00

C = 172,940; annual USC = 456,561.60
base employer cost = 10,456,561.60
```

### Annual gross UAH 30,000,000

```text
monthly gross = 2,500,000.00; privilege = 0
PIT = 30,000,000 × 18% = 5,400,000.00
military levy = 30,000,000 × 5% = 1,500,000.00
employee net = 23,100,000.00

C = 172,940; annual USC = 456,561.60
base employer cost = 30,456,561.60
```

## 6. Calculation order

1. Identify each calendar month's accrued salary and employment-related bonus. Allocate multi-month leave/sickness amounts to their respective months where required.
2. Test that month's salary for the tax social privilege. If salary exceeds UAH 4,660, privilege is zero. All examples fail the test.
3. Withhold PIT at 18% from salary less any applicable privilege.
4. Independently withhold military levy at 5% from the full taxable salary; do not subtract PIT or the privilege.
5. Employee net is gross less PIT and military levy. There is no employee USC deduction for this profile.
6. Aggregate that employee's USC-base remuneration for the calendar month, apply the minimum-base rule if relevant and the UAH 172,940 maximum, then charge employer USC at 22%.
7. Employer cost is gross plus USC, plus any contingent employer-funded sick pay or other contractual cost actually arising.

## 7. Universal rules versus variable or unresolved items

### Universal for the stated facts

- PIT 18%; ordinary-employee military levy 5%.
- No employee USC deduction; employer USC 22%.
- 2026 monthly minimum wage UAH 8,647, ordinary USC cap UAH 172,940, maximum USC UAH 38,046.80.
- Calendar-month USC base and cap.
- PIT privilege UAH 1,664 only if monthly salary does not exceed UAH 4,660; not available in any example.
- Ordinary employment bonuses are salary in the accrual month.

### Variable or outside the profile

- Disability can change employer USC to 8.41%; Diia City and military/service remuneration have special rules.
- Part months, unpaid leave, multiple jobs, non-principal employment, maternity, sick pay, benefits in kind, and civil contracts can change the base or minimum-USC treatment.
- Bonus timing changes USC whenever monthly remuneration crosses the cap.
- Tax discounts require qualifying documented expenditure and an annual claim.
- Sick-pay employer cost depends on whether an insured event occurs and on pay/insurance history.

### Intentionally unresolved, not guessed

- A single mandated item-level rounding sequence for PIT and military levy was not located in the primary material. The official reporting form uses hryvnias and kopiykas; implementations should retain their documented monthly rounding convention.
- No universal employer occupational-risk premium separate from the 22% USC was found for ordinary private employment. The research therefore does not invent one.
- Salary indexation, paid-leave scheduling, severance, occupational health, and wartime labour-law operational costs are not percentages of annual regular gross and cannot be calculated from the supplied facts.

## 8. Primary sources

All sources were accessed **2026-10-04**.

1. **State Tax Service, “У ГУ ДПС у Закарпатській області обговорили питання виплати заробітної плати та сплати податків”** (discussion of wage payment and payroll taxes), published **2026-04-30**. <https://zak.tax.gov.ua/media-ark/news-ark/1006220.html>. Pinpoint: lines 65–69: 2026 minimum wage UAH 8,647; employer withholds PIT 18% and military levy 5%, and accrues USC 22% (8.41% for persons with disabilities).
2. **State Tax Service, “Розділ IV. Податок на доходи фізичних осіб”** (official Tax Code section IV reproduction), living text current on access. <https://tax.gov.ua/nk/rozdil-iv--podatok-na-dohodi-fizichnih-o/>. Pinpoints: article 167.1, 18% rate for salary and employment rewards; articles 168.1.1–168.1.2, employer withholding and remittance when income is paid; article 169.4.1, monthly privilege-income test.
3. **DPS Knowledge Base, question “На яку ПСП та при якому граничному доході…”**, current 2026 answer, no displayed publication date. <https://zir.tax.gov.ua/main/bz/view/?id=43882&src=ques>. Pinpoints: answer lines 40–48: 2026 privilege UAH 1,664; UAH 4,660 monthly salary limit; Tax Code articles 169.1.1 and 169.4.1.
4. **State Tax Service, “Військовий збір у випадку застосування ПСП сплачується з усієї суми нарахованого доходу”**, published **2026-08-03**. <https://cv.tax.gov.ua/media-ark/news-ark/1036232.html>. Pinpoint: levy applies to employment salary without subtracting PIT, funded-pension contributions, or the tax social privilege.
5. **State Tax Service, “Закон України №4015-ІХ: військовий збір”**, published **2024-12-13**. <https://kh.tax.gov.ua/media-ark/news-ark/850615.html>. Pinpoints: lines 7–14: Law 4015-IX effective 2024-12-01; ordinary rate rose to 5%; accrual-period transition; specified military remuneration remains 1.5%.
6. **State Tax Service, “Чи потрібно буде сплачувати військовий збір після завершення воєнного стану?”**, published **2026-07-21**. <https://kyivobl.tax.gov.ua/media-ark/news-ark/1032107.html>. Pinpoints: lines 66–78: Law 4835-IX effective 2026-04-15; levy continues for three calendar years following the end year; employees' rate 5%.
7. **President of Ukraine, Decree 596/2026, “Про продовження строку дії воєнного стану в Україні”**, dated **2026-07-13**, approved by Law 4928-IX effective **2026-07-25**. <https://zakon.rada.gov.ua/laws/show/596/2026>. Pinpoint: extension from 05:30 on 2026-08-02 for 90 days. Approval: <https://zakon.rada.gov.ua/laws/show/4928-20>.
8. **Law of Ukraine 4695-IX, “Про Державний бюджет України на 2026 рік”**, adopted **2025-12-03**. <https://zakon.rada.gov.ua/laws/show/4695-20>. Pinpoints: article 7, working-age subsistence minimum UAH 3,328; article 8, minimum wage UAH 8,647 monthly; article 32, ordinary maximum USC base 20 minimum wages during 2026 and suspension of the usual Law 2464 definition.
9. **Pension Fund of Ukraine, “Інформація про основні показники для добровільної участі…”**, published **2026-01-08**. <https://www.pfu.gov.ua/2176593-informatsiya-pro-osnovni-pokaznyky-dlya-dobrovilnoyi-uchasti-u-systemi-zagalnoobov-yazkovogo-derzhavnogo-pensijnogo-strahuvannya-3/>. Pinpoints: lines 321–327: UAH 8,647 minimum wage, 22% USC, UAH 1,902.34 minimum, UAH 172,940 maximum base, and 2026 suspension note.
10. **State Tax Service, “Ключові показники єдиного внеску у 2026 році”**, published **2026-04-16**. <https://lv.tax.gov.ua/media-ark/news-ark/1001497.html>. Pinpoints: lines 9–16: same bases plus maximum monthly USC UAH 38,046.80.
11. **Law of Ukraine 2464-VI, “Про збір та облік єдиного внеску…”**, adopted **2010-07-08**, 2026 consolidated edition. <https://zakon.rada.gov.ua/laws/show/2464-17/ed20260126>. Pinpoints: article 7, wage/remuneration base; article 8(5), 22% employer rate; article 9, employer computation from accounting records.
12. **State Tax Service, “Порядок застосування максимальної величини бази нарахування єдиного внеску”**, published **2025-12-04**. <https://zak.tax.gov.ua/media-ark/news-ark/959560.html>. Pinpoints: lines 66–82: 22% rate; wage and incentive base; calendar month as reporting period; aggregate monthly income; cap; leave/sickness amounts assigned separately to relevant months.
13. **State Tax Service, “Як оподатковуються ПДФО надбавки, премії…”**, published **2023-07-13**. <https://kyiv.tax.gov.ua/media-ark/news-ark/691162.html>. Pinpoints: lines 6–13: employment premiums are salary, taxable in the month accrued, including premiums concerning earlier periods.
14. **State Tax Service, “Округлення єдиного внеску у звітності…”**, published **2025-04-15**. <https://od.tax.gov.ua/media-ark/news-ark/887134.html>. Pinpoints: lines 79–86: monetary fields in hryvnias with kopiykas, two-decimal general rounding, monthly employee detail, and reconciliation to reported USC.
15. **Pension Fund of Ukraine, “Алгоритм здійснення виплати за лікарняним”**, published **2024-06-17**, living guidance current on access. <https://www.pfu.gov.ua/2165537-algorytm-zdijsnennya-vyplaty-za-likarnyanym-2/>. Pinpoints: lines 335–343: first five ordinary-illness days employer-funded, PFU from day six; first 17 occupational-event days employer-funded, PFU from day 18.
16. **Pension Fund of Ukraine, “Ким виплачується допомога… внаслідок нещасного випадку на виробництві?”**, published **2026-07-06**. <https://www.pfu.gov.ua/zp/385939-kym-vyplachuyetsya-dopomoga-po-tymchasovij-nepratsezdatnosti-vnaslidok-neshhasnogo-vypadku-na-vyrobnytstvi/>. Pinpoints: lines 101–107: 100% average taxable salary, employer funds days 1–17, PFU from day 18.

## Evidence assessment

**Strongest evidence.** The April 2026 DPS payroll notice states all three core rates together for 2026; the enacted State Budget Act, PFU January table, and DPS April USC table triangulate the exact UAH 8,647 minimum, UAH 172,940 cap, and UAH 38,046.80 maximum contribution. The July 2026 DPS military-levy notice captures the important post-April statutory extension that older wartime summaries omit.

**Weakest evidence and implementation caution.** The primary material located does not prescribe one universal item-level rounding sequence for PIT and military levy. Exact monthly payroll totals can therefore differ by a few kopiykas from the annual rate multiplication shown here. Employer sickness cost is inherently event- and history-dependent, while bonus timing changes capped USC; neither can be inferred from annual gross alone.
