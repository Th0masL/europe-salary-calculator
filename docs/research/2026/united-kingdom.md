# United Kingdom — employee payroll, tax year 2026/27

**Clean-room research dossier.** Accessed **2026-10-04**. This was reconstructed solely from GOV.UK/HMRC, the Scottish Government and DWP. It does not use repository calculator code, generated data, existing UK documentation, prior audits, or other country dossiers.

## Scope and conventions

Profile: UK-resident employee, age 30, single, no children, one ordinary private-sector employment for the full tax year, Category A National Insurance, regular annual cash salary, no taxable benefits, bonus, pension contributions, student/postgraduate loan, Gift Aid, salary sacrifice, other income or deductions. “2026/27” means **6 April 2026 to 5 April 2027**.

Income tax is shown separately for:

- **England, Wales and Northern Ireland (rUK)** — the 2026/27 non-savings employment-income rates are the same; and
- **Scotland** — Scottish rates and bands apply to non-savings employment income where HMRC identifies the employee as a Scottish taxpayer.

The standard code is `1257L` outside Scotland and `S1257L` in Scotland while the full £12,570 allowance is due. The calculations are **final annual liabilities**, including the statutory withdrawal of Personal Allowance above £100,000. At high income, HMRC would normally alter the employee's code to collect that withdrawal; a literal unchanged `1257L`/`S1257L` all year can under-withhold and require reconciliation.

For a reproducible NIC result, salary is paid monthly. The first 11 payments are annual salary divided by 12 and rounded to the nearest penny; the twelfth is the exact penny residual. Employee and employer NIC are calculated separately for every month using HMRC's exact-percentage method and each is rounded to the nearest penny. Income tax is shown as the exact annual liability, not an attempt to reproduce every cumulative PAYE rounding step.

## Results

### Employee result by income-tax regime

All amounts are pounds per tax year.

| Gross | Personal Allowance | Taxable income | Employee NIC | rUK income tax | rUK net cash | Scottish income tax | Scottish net cash |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000.00 | 12,570.00 | 7,430.00 | 593.88 | 1,486.00 | 17,920.12 | 1,446.33 | 17,959.79 |
| 60,000.00 | 12,570.00 | 47,430.00 | 3,210.00 | 11,432.00 | 45,358.00 | 13,182.05 | 43,607.95 |
| 100,000.00 | 12,570.00 | 87,430.00 | 4,010.04 | 27,432.00 | 68,557.96 | 30,732.05 | 65,257.91 |
| 200,000.00 | 0.00 | 200,000.00 | 6,009.96 | 76,203.00 | 117,787.04 | 83,634.35 | 110,355.69 |
| 600,000.00 | 0.00 | 600,000.00 | 14,010.00 | 256,203.00 | 329,787.00 | 275,634.35 | 310,355.65 |

`Net cash = gross − income tax − employee NIC`. There is no pension or student-loan deduction in the requested profile.

### Employer-side result

The income-tax regime does not affect employer NIC.

| Gross | Employer NIC before relief | Gross + employer NIC | If one eligible employer can allocate full Employment Allowance here | Maximum marginal levy addition if £15,000 levy allowance already exhausted |
|---:|---:|---:|---:|---:|
| 20,000.00 | 2,249.39 | 22,249.39 | 20,000.00 | 100.00 |
| 60,000.00 | 8,249.40 | 68,249.40 | 60,000.00 | 300.00 |
| 100,000.00 | 14,249.41 | 114,249.41 | 103,749.41 | 500.00 |
| 200,000.00 | 29,249.39 | 229,249.39 | 218,749.39 | 1,000.00 |
| 600,000.00 | 89,249.40 | 689,249.40 | 678,749.40 | 3,000.00 |

The third column is the reproducible statutory employee-level employer cost used as the base result. The Employment Allowance and Apprenticeship Levy columns are **not additive universal amounts**: both depend on the whole employer or connected group. The levy column is `0.5% × this salary` only as a marginal allocation where the employer is already levy-paying and its allowance has been exhausted.

## 1. Income tax

### 1.1 Personal Allowance and taper

HMRC's **“Income Tax rates and allowances for current and previous tax years”**, updated 2026-04-06, gives a £12,570 Personal Allowance and £100,000 income limit for 2026/27, then states that the allowance falls by £1 for every £2 above that limit and may reach zero. GOV.UK's current-rates page confirms it is zero at £125,140.

With no pension, Gift Aid or other adjustment in this profile, adjusted net income is gross salary `G`:

```text
PA = max(0, 12,570 − 0.5 × max(G − 100,000, 0))
taxable income X = G − PA
```

This creates the familiar 60% effective rUK income-tax marginal rate between £100,000 and £125,140 (and higher Scottish effective marginal rates in the affected Scottish bands), because £1 of allowance is lost for each £2 of additional income.

### 1.2 England, Wales and Northern Ireland

HMRC's 2026/27 table, lines 129–144, applies these bands to **income after allowances**:

| Taxable-income slice | Rate |
|---:|---:|
| first £37,700 | 20% |
| £37,700 to £125,140 | 40% |
| over £125,140 | 45% |

```text
T_rUK(X) = 20% × min(X, 37,700)
          + 40% × min(max(X − 37,700, 0), 87,440)
          + 45% × max(X − 125,140, 0)
```

HMRC's employer thresholds page explicitly lists the same bands for England/Northern Ireland and Wales. The starting rate for savings is irrelevant because the profile contains only employment income.

### 1.3 Scotland

The Scottish Government's **“Scottish Income Tax 2026 to 2027: technical factsheet”**, published 2026-01-13, Table 1, gives the headline thresholds assuming the standard allowance. HMRC's income-tax rates table supplies the corresponding taxable-income band limits:

| Taxable-income slice | Width | Rate |
|---:|---:|---:|
| £0–£3,967 | 3,967 | 19% starter |
| £3,967–£16,956 | 12,989 | 20% basic |
| £16,956–£31,092 | 14,136 | 21% intermediate |
| £31,092–£62,430 | 31,338 | 42% higher |
| £62,430–£125,140 | 62,710 | 45% advanced |
| over £125,140 | — | 48% top |

```text
T_S(X) = 19% × min(X, 3,967)
       + 20% × min(max(X − 3,967, 0), 12,989)
       + 21% × min(max(X − 16,956, 0), 14,136)
       + 42% × min(max(X − 31,092, 0), 31,338)
       + 45% × min(max(X − 62,430, 0), 62,710)
       + 48% × max(X − 125,140, 0)
```

The Scottish factsheet footnote at lines 99–100 explains that its presentation adds the standard £12,570 allowance to the taxable band limits (for example, £31,092 + £12,570 = the £43,662 higher-rate threshold). This distinction matters when the allowance tapers: the calculation must use taxable income and the taxable band limits above, not mechanically subtract headline gross thresholds.

As a reasonableness check, Scottish Table 2 says a £20,000 taxpayer pays about £40 less than rUK, while £60,000 and £100,000 taxpayers pay about £1,750 and £3,300 more. The independent differences here are £39.67, £1,750.05 and £3,300.05.

### 1.4 PAYE code and reconciliation

HMRC P9X **“Tax codes to use from 6 April 2026”**, updated 2026-02-19, confirms the £12,570 UK-wide allowance, £242 weekly/£1,048 monthly PAYE threshold and emergency code 1257L. GOV.UK **“Income Tax in Scotland — Who pays”** says Scottish codes begin `S` and the standard full-allowance code is `S1257L`.

PAYE is withholding, not a separate tax. A cumulative standard code spreads free pay and bands through the year; HMRC checks total tax after the year. At salaries over £100,000, correct final tax requires the Personal Allowance taper even if a payroll initially operated 1257L. This dossier reports final liability and does not treat under-withholding as a tax saving.

## 2. National Insurance contributions

### 2.1 2026/27 thresholds and rates

HMRC **“Rates and thresholds for employers 2026 to 2027”**, published 2026-01-30 and effective 2026-04-06 through 2027-04-05, gives:

| Threshold | Weekly | Monthly | Annual reference |
|---|---:|---:|---:|
| Lower earnings limit | £129 | £559 | £6,708 |
| Primary threshold | £242 | £1,048 | £12,570 |
| Secondary threshold | £96 | £417 | £5,000 |
| Upper earnings limit | £967 | £4,189 | £50,270 |

For ordinary Category A:

- employee: 0% through the primary threshold, 8% above it through the upper earnings limit, and 2% above the upper earnings limit;
- employer: 15% above the secondary threshold, with no upper cap.

For monthly gross `m`:

```text
employee_NIC_month = round_penny(
    8% × max(min(m, 4,189) − 1,048, 0)
  + 2% × max(m − 4,189, 0))

employer_NIC_month = round_penny(15% × max(m − 417, 0))
annual NIC = sum of the 12 monthly amounts
```

The lower earnings limit preserves benefit entitlement but does not itself create a positive Category A employee charge. NIC is not deductible from income subject to PAYE income tax.

### 2.2 Period basis and rounding

HMRC CWG2 says the ordinary NIC earnings period is the regular payment interval; for a monthly-paid employee, NIC is worked out with the monthly thresholds. It is not an annual reconciliation like income tax. HMRC National Insurance Manual **NIM11002**, updated 2026-07-22, lines 72–81, requires employee and employer NIC to be calculated separately and rounded to the nearest penny, disregarding amounts below half a penny.

That is why these results differ slightly from applying the annual reference thresholds directly. The explicit monthly pay schedules are:

| Annual salary | Months 1–11 | Month 12 |
|---:|---:|---:|
| £20,000 | £1,666.67 | £1,666.63 |
| £60,000 | £5,000.00 | £5,000.00 |
| £100,000 | £8,333.33 | £8,333.37 |
| £200,000 | £16,666.67 | £16,666.63 |
| £600,000 | £50,000.00 | £50,000.00 |

A weekly, four-weekly, irregularly paid or director case can yield a different annual NIC amount and is outside this scenario.

## 3. Employer-wide items and pension boundary

### 3.1 Employment Allowance

HMRC's Employment Allowance page says an eligible employer may reduce annual employer Class 1 NIC by up to **£10,500**, consuming the relief through payroll until it is exhausted or the tax year ends. Eligibility guidance says ordinary businesses doing less than half their work in the public sector may claim; the pre-April-2025 £100,000 prior-year NIC cap no longer excludes large-NIC employers. Exclusions include a company whose sole director is its only employee liable to employer NIC, specified domestic employees, and off-payroll workers; connected companies/charities have only one claim, and an employer with several payrolls claims against only one.

Therefore Employment Allowance cannot be allocated universally to this employee. The table's illustration assumes this is the only relevant employee and an otherwise eligible employer, so the relief is `min(employer NIC, £10,500)`. A general salary calculator should show employer NIC before allowance or request employer-wide facts.

### 3.2 Apprenticeship Levy

HMRC **“Pay Apprenticeship Levy”**, updated 2026-04-06, lines 113–138, states:

- levy rate: **0.5%** of the employer's annual pay bill;
- liability/reporting where annual pay bill, including connected companies/charities, exceeds **£3 million**;
- pay bill includes employee payments subject to secondary Class 1 NIC, including pay below the secondary threshold; and
- the annual levy allowance is **£15,000**, shared across connected entities.

The employer-level formula is:

```text
levy = max(0, 0.5% × employer/group levy pay bill − allocated £15,000 allowance)
```

It is impossible to derive the levy attributable to one worker from that worker's salary alone. No levy is included in base employer cost. If the employer is already above £3 million and has fully used its allowance, the marginal cost of this salary is 0.5% of salary, as shown in the table.

### 3.3 Automatic enrolment and the requested “no pension” case

DWP's **“Review of the Automatic Enrolment Earnings Trigger and Qualifying Earnings Band for 2026/27”**, published 2025-12-18, Table 1, retains:

- annual earnings trigger: **£10,000**;
- lower qualifying-earnings limit: **£6,240**;
- upper qualifying-earnings limit: **£50,270**.

GOV.UK's workplace-pension employer guidance says an employer must enrol and contribute for staff aged 22 to State Pension age earning at least £10,000 and normally working in the UK. GOV.UK's contribution page gives a minimum 8% total contribution, at least 3% employer, generally on earnings from £6,240 to £50,270.

Every example employee crosses the trigger. “No pension” therefore requires a valid employee opt-out (or another fact taking the worker outside the duty); an employer cannot simply elect not to enrol. On the common qualifying-earnings basis, the minimum employer amount before opt-out would be:

```text
3% × min(max(G − 6,240, 0), 44,030)
```

That is £412.80 at £20,000 and £1,320.90 at each higher salary. It is excluded from base employer cost because the requested profile says no pension. Scheme certification and pensionable-pay definitions can produce different amounts.

## 4. Worked calculations

### Gross £20,000

```text
PA = 12,570; X = 7,430
rUK tax = 20% × 7,430 = 1,486.00
Scottish tax = 19% × 3,967 + 20% × 3,463
             = 753.73 + 692.60 = 1,446.33
employee NIC = 12 × £49.49 = 593.88
employer NIC = 11 × £187.45 + £187.44 = 2,249.39
rUK net = 20,000 − 1,486 − 593.88 = 17,920.12
Scottish net = 20,000 − 1,446.33 − 593.88 = 17,959.79
base employer cost = 20,000 + 2,249.39 = 22,249.39
```

### Gross £60,000

```text
PA = 12,570; X = 47,430
rUK tax = 20% × 37,700 + 40% × 9,730 = 11,432.00
Scottish tax = 753.73 + 2,597.80 + 2,968.56 + 42% × 16,338
             = 13,182.05
employee NIC = 12 × £267.50 = 3,210.00
employer NIC = 12 × £687.45 = 8,249.40
rUK net = 45,358.00; Scottish net = 43,607.95
base employer cost = 68,249.40
```

### Gross £100,000

```text
PA = 12,570; X = 87,430
rUK tax = 7,540 + 40% × 49,730 = 27,432.00
Scottish tax = 753.73 + 2,597.80 + 2,968.56 + 13,161.96
             + 45% × 25,000 = 30,732.05
employee NIC = 12 × £334.17 = 4,010.04
employer NIC = 11 × £1,187.45 + £1,187.46 = 14,249.41
rUK net = 68,557.96; Scottish net = 65,257.91
base employer cost = 114,249.41
```

### Gross £200,000

```text
PA = 0; X = 200,000
rUK tax = 7,540 + 40% × 87,440 + 45% × 74,860
         = 76,203.00
Scottish tax = 753.73 + 2,597.80 + 2,968.56 + 13,161.96
             + 45% × 62,710 + 48% × 74,860
             = 83,634.35
employee NIC = 12 × £500.83 = 6,009.96
employer NIC = 11 × £2,437.45 + £2,437.44 = 29,249.39
rUK net = 117,787.04; Scottish net = 110,355.69
base employer cost = 229,249.39
```

### Gross £600,000

```text
PA = 0; X = 600,000
rUK tax = 7,540 + 34,976 + 45% × 474,860 = 256,203.00
Scottish tax through £125,140 taxable = 47,701.55
Scottish top-rate tax = 48% × 474,860 = 227,932.80
Scottish tax = 275,634.35
employee NIC = 12 × £1,167.50 = 14,010.00
employer NIC = 12 × £7,437.45 = 89,249.40
rUK net = 329,787.00; Scottish net = 310,355.65
base employer cost = 689,249.40
```

## 5. Calculation order

1. Determine Scottish-taxpayer status. Use Scottish rates only for non-savings/non-dividend income of a Scottish taxpayer; otherwise use rUK employment rates.
2. Establish adjusted net income. Here it equals gross salary because there are no pension/Gift Aid/other adjustments.
3. Calculate the £12,570 Personal Allowance and taper it £1 per £2 above £100,000, to zero at £125,140.
4. Subtract the allowance from gross, then apply the appropriate taxable-income bands. This produces final annual income tax.
5. Independently, for each monthly payment, apply Category A NIC thresholds/rates. Calculate primary and secondary NIC separately and round each to the nearest penny each period; sum 12 periods.
6. Employee net is gross less annual income tax and primary NIC. Pension and loans are zero under the stated facts.
7. Base employer cost is gross plus secondary NIC. Only then consider employer-wide Employment Allowance, Apprenticeship Levy and, if the employee has not opted out, pension contributions.

## 6. Boundaries, variability and unresolved items

### Universal within the selected employee facts

- The Personal Allowance, taper, rUK and Scottish 2026/27 employment-income bands.
- Category A monthly NIC thresholds and 8%/2% employee, 15% employer rates.
- Monthly NIC earnings-period calculation and penny rounding.
- Auto-enrolment trigger and qualifying-earnings limits.

### Employer- or employee-specific

- Employment Allowance eligibility and allocation across the employer's NIC bill.
- Apprenticeship Levy depends on the whole connected pay bill and allocated allowance.
- Pension scheme basis; “no pension” implies a valid opt-out in this profile.
- Other NIC categories, Freeport/Investment Zone status, under-21, apprentice and veteran employer reliefs.
- Benefits, salary sacrifice, bonus timing, irregular pay, directors, multiple employments, student loans and Scottish residence.

### Unresolved / intentionally not guessed

- Exact month-by-month cumulative PAYE deductions for a high earner before HMRC changes the tax code. Final liability is shown, but actual withholding timing depends on HMRC coding notices and payroll dates.
- Any allocation of Employment Allowance or Apprenticeship Levy to an individual in a multi-employee employer.
- Pension opt-out timing/refund mechanics and scheme-specific pensionable pay.
- Employer's Liability insurance, payroll administration and contractual benefits; these are real employer costs but not determinable statutory percentages of this salary.

## 7. Primary sources

All sources accessed 2026-10-04.

1. **HMRC, “Rates and thresholds for employers 2026 to 2027”**; published 2026-01-30, updated 2026-09-01; effective 2026-04-06 to 2027-04-05. [Source](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2026-to-2027). Pinpoints: lines 115–136, tax year and rUK bands; Scotland/Wales tables in “Tax thresholds, rates and codes”; lines 174–203, NIC thresholds; lines 204–248, Category A employee/employer rates; lines 484–488, £10,500 Employment Allowance.
2. **HMRC, “Income Tax rates and allowances for current and previous tax years”**; updated 2026-04-06. [Source](https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past). Pinpoints: lines 90–99, Personal Allowance and taper; lines 129–144, rUK taxable bands; lines 145–164, Scottish taxable bands.
3. **Scottish Government, “Scottish Income Tax 2026 to 2027: technical factsheet”**; published 2026-01-13. [Source](https://www.gov.scot/publications/scottish-income-tax-technical-factsheet/). Pinpoints: Table 1 lines 40–53, rates/headline bands and taper note; Table 2 lines 72–91, rUK comparison checks; footnote 1 lines 99–100, conversion to taxable-income band limits.
4. **HMRC, P9X “Tax codes to use from 6 April 2026”**; updated 2026-02-19. [Source](https://www.gov.uk/government/publications/p9x-tax-codes/p9x-tax-codes-to-use-from-6-april-2026). Pinpoint: £12,570 allowance, £242 weekly/£1,048 monthly threshold and 1257L emergency code.
5. **GOV.UK, “Income Tax in Scotland — Who pays”**; living guidance, no displayed publication date. [Source](https://www.gov.uk/scottish-income-tax/who-pays). Pinpoint: Scottish residence scope, `S` prefix and `S1257L` standard-allowance code.
6. **HMRC, CWG2 “2026 to 2027: Employer further guide to PAYE and National Insurance contributions”**; 2026 edition added 2026-02-18, parent page updated 2026-09-21. [Source](https://www.gov.uk/government/publications/cwg2-further-guide-to-paye-and-national-insurance-contributions). Pinpoint: section 3.1.1, regular weekly/monthly interval is the NIC earnings period.
7. **HMRC National Insurance Manual NIM11002, “exact percentage method”**; published 2016-04-11, updated 2026-07-22. [Source](https://www.gov.uk/hmrc-internal-manuals/national-insurance-manual/nim11002). Pinpoint: lines 72–81, separate primary/secondary calculation and nearest-penny rounding under SSCR 2001 regulation 12(1).
8. **HMRC, “Employment Allowance — What you'll get / Check if you're eligible”**; living guidance, current on access. [Amount](https://www.gov.uk/claim-employment-allowance), [eligibility](https://www.gov.uk/claim-employment-allowance/eligibility). Pinpoints: amount lines 63–69; eligibility lines 63–90, including April 2025 removal of the £100,000 restriction and employer/group exclusions.
9. **HMRC, “Pay Apprenticeship Levy”**; published 2016-12-12, updated 2026-04-06. [Source](https://www.gov.uk/guidance/pay-apprenticeship-levy). Pinpoints: lines 113–138, 0.5%, £3 million test and pay-bill definition; “Using your Apprenticeship Levy allowance”, annual £15,000 allowance and connected-group allocation.
10. **DWP, “Review of the Automatic Enrolment Earnings Trigger and Qualifying Earnings Band for 2026/27”**; published 2025-12-18. [Source](https://www.gov.uk/government/publications/review-of-the-automatic-enrolment-earnings-trigger-and-qualifying-earnings-band-for-202627/review-of-the-automatic-enrolment-earnings-trigger-and-qualifying-earnings-band-for-202627). Pinpoints: Table 1 lines 97–105, £10,000/£6,240/£50,270; preceding sections give the decision to retain each threshold.
11. **GOV.UK, “Set up and manage a workplace pension scheme — Employers and eligible staff”**; living guidance. [Source](https://www.gov.uk/workplace-pensions-employers). Pinpoint: lines 60–73, age, earnings and UK-work enrolment criteria.
12. **GOV.UK, “Workplace pensions — What you, your employer and the government pay”**; living guidance. [Source](https://www.gov.uk/workplace-pensions/what-you-your-employer-and-the-government-pay). Pinpoints: lines 90–110, qualifying earnings and 3% employer/5% employee/8% total minima.

## Evidence assessment

**Strongest evidence:** HMRC's current 2026/27 rates page and taxable-band tables directly state every PAYE and Category A NIC threshold/rate; the Scottish Government technical factsheet supplies the Scottish rates plus cross-check examples; NIM11002 fixes the otherwise easy-to-miss per-period penny rounding.

**Weakest evidence / principal limitation:** exact employer cost cannot be a single universal number once Employment Allowance, Apprenticeship Levy and workplace pension are considered, because they depend on employer/group facts and opt-out status not supplied. High-earner PAYE withholding timing is also code-dependent even though final annual tax is determinate.
