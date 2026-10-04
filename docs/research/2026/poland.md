# Poland employee salary and payroll rules — tax year 2026

Research status: **independent clean-room reconstruction from Polish primary official sources**.  
Access date for every source: **2026-10-04**.

## Scope and assumptions

The employee is Polish tax resident for all of 2026, single, age 30, has no children or other income/deductions, and works under one ordinary employment contract (`umowa o pracę`). Pay is regular taxable cash salary. The standard local employment expense is used: PLN 250 monthly, maximum PLN 3,000 annually. No commuting uplift, copyright expense, youth exemption, PPK, special-work pension contribution, benefit or relief is included.

The worked employer case is a private entrepreneur subject to FGŚP, with pay above the monthly minimum and a **1.67% accident contribution** (the official small-payer case for no more than nine insured persons). That rate is a scenario, not a universal average.

Amounts are in Polish złoty (PLN). `G` denotes annual gross cash salary.

## 1. Personal income tax (`PIT`)

### 1.1 Tax base and scale

For salary only:

`annual PIT base before whole-złoty rounding = G − employee social contributions − employment expenses`.

The 2026 standard expenses for one employment relationship are **PLN 250 monthly / PLN 3,000 annually**. Ministry of Finance (`podatki.gov.pl`), [“Ile wynoszą koszty uzyskania przychodów w rozliczeniu PIT za 2026 rok?”](https://www.podatki.gov.pl/twoj-e-pit-rozlicz-roczny-pit-online/pytania-i-odpowiedzi/koszty-uzyskania-przychodow/71-ile-wynosza-koszty-uzyskania-przychodow-w-rozliczeniu-pit-za-2026-rok), published **2025-12-15**, updated **2026-09-28**, bullet 1, gives PLN 3,000 (PLN 250 monthly) for one employment relationship.

The annual taxable base is rounded to whole złoty. The 2026 scale is:

| Rounded annual base `T` | PIT before other credits |
|---|---|
| `T ≤ 120,000` | `max(0, 12% × T − 3,600)` |
| `T > 120,000` | `10,800 + 32% × (T − 120,000)` |

The PLN 3,600 reduction is the 12% value of the **PLN 30,000 tax-free amount**. Ministry of Finance, [“Dochody z pracy”](https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/dochody-z-pracy), published **2025-12-15**, updated **2026-09-30**, headings “Jak ustalić koszty uzyskania przychodów” and “Jak obliczyć podatek,” gives the expense and scale. Its [PIT-2 guidance](https://podatki.gov.pl/poradniki-i-informatory/pit-2-pit-2a-pit-3-zasady-skladania-oswiadczen-o-stosowaniu-pomniejszenia-zaliczki-o-kwote-zmniejszajaca-podatek-112-124-lub-136), published **2026-02-18**, updated **2026-06-24**, lines under the opening heading, states PLN 30,000, PLN 3,600 and the PLN 300 monthly reduction.

Employee-funded pension, disability and sickness contributions are deductible from PIT income. Ministry of Finance, [“Odliczenie składek na ubezpieczenie społeczne PIT”](https://podatki.gov.pl/ulgi-i-odliczenia/odliczenie-skladek-na-ubezpieczenie-spoleczne-pit), published **2025-12-15**, updated **2026-06-24**, heading “Kiedy przysługuje odliczenie,” expressly lists employee pension, disability and sickness contributions withheld by the payer.

### 1.2 Health contribution is not deductible

An employment health contribution cannot reduce PIT income or tax. Ministry of Finance, [“Odliczenie składek na ubezpieczenie zdrowotne PIT”](https://podatki.gov.pl/ulgi-i-odliczenia/odliczenie-skladek-na-ubezpieczenie-zdrowotne-pit), published **2025-12-15**, updated **2026-06-24**, heading “Kiedy przysługuje odliczenie” and employee FAQ, says a contribution paid from an employment contract cannot be deducted and specifically answers that employer-withheld employee contributions are not deductible.

## 2. Employee social and health contributions

### 2.1 Employee social insurance

| Contribution | Employee rate | Annual cap? |
|---|---:|---|
| Old-age pension (`emerytalne`) | 9.76% | yes |
| Disability (`rentowe`) | 1.50% | yes |
| Sickness (`chorobowe`) | 2.45% | no |
| **Total below pension/disability cap** | **13.71%** | mixed |

The shared 2026 pension/disability assessment ceiling is **PLN 282,600** (30 times the forecast monthly salary). Consequently:

`employee social = 11.26% × min(G, 282,600) + 2.45% × G`, subject to payroll-period grosz rounding.

After cumulative pension/disability assessment reaches PLN 282,600, the 9.76% and 1.50% deductions stop for the remainder of the year; 2.45% sickness continues.

Primary evidence:

- ZUS, [“Jesteś pracownikiem? Poznaj swoje ubezpieczenia”](https://www.zus.pl/documents/10182/167561/Jestes_pracownikiem.pdf/a049dc44-6680-4a0e-b07a-60adc7dc01eb?download=true&version=1.3), current edition available in 2026 (no issue date visible in the PDF), PDF pp. 4–5, “Jaka jest wysokość składek”: 19.52% pension split 9.76%/9.76%, disability 1.50% employee and 6.50% employer, sickness 2.45% employee, variable employer accident, and health 9% employee.
- ZUS, [“Nowe wysokości składek na ubezpieczenia społeczne w 2026 r.”](https://www.zus.pl/en/o-zus/aktualnosci/-/asset_publisher/aktualnosci/content/id/13663769), published **2025-12-30**, citing the Minister's **2025-11-19** announcement (M.P. 2025 item 1206), numbered point 2: PLN 282,600.

### 2.2 Health

The employee health base each month is:

`gross liable pay − employee pension − employee disability − employee sickness`.

Health is **9%**, wholly employee-funded, and its base has **no 30-times ceiling**. ZUS, [“Podstawa wymiaru składek na ubezpieczenie zdrowotne”](https://www.zus.pl/pracujacy/ubezpieczenie-zdrowotne-w-polsce/podstawa-wymiaru-skladek-na-ubezpieczenie-zdrowotne), dated **2022-01-01** and current for this rule, section “Podstawa wymiaru składek … pracowników,” states both the employee-social subtraction and no 30-times limit. The ZUS employee brochure above, PDF p. 4, gives the 9% rate.

Thus annual health is approximately `9% × (G − employee social)`, but actual payroll is the sum of monthly bases and contributions rounded to grosze.

## 3. Employer social contributions and funds

| Employer item | Rate in worked scenario | Base/cap |
|---|---:|---|
| Old-age pension | 9.76% | capped at cumulative PLN 282,600 |
| Disability | 6.50% | capped at cumulative PLN 282,600 |
| Accident | 1.67% | all liable gross; employer-specific rate |
| Labour Fund + Solidarity Fund (`FP + FS`) | 2.45% | all gross here; no 30-times cap |
| Guaranteed Employee Benefits Fund (`FGŚP`) | 0.10% | all gross here; no 30-times cap |

For the selected 1.67% accident case:

`employer contributions = 16.26% × min(G, 282,600) + 4.22% × G`, subject to monthly grosz rounding.

ZUS's employee brochure, PDF pp. 4–5, says FP/FS and FGŚP use employment revenue without the annual pension/disability cap, with age and minimum-pay exceptions. This employee is age 30 and every worked monthly salary exceeds the 2026 minimum, so those exceptions do not apply. The government business portal, [“Jakie składki na ubezpieczenia społeczne płaci przedsiębiorca do ZUS”](https://biznes.gov.pl/pl/portal/00274), current 2026 table, gives the complete split: employer pension 9.76%, disability 6.50%, accident 0.67%–3.33%, FP 2.45%, and FGŚP 0.10%.

### Accident rate is an employer variable

ZUS, [“Contributions”](https://lang.zus.pl/finances/contributions), dated **2026-06-23**, table and footnotes (a)–(b), gives accident rates **0.67%–3.33%**, with **1.67%** for payers reporting on average no more than nine insured persons or not registered in REGON. Larger payers use an activity-group rate and, where ZUS determines it, a 0.5–1.5 correction factor. ZUS's [2026/27 accident notice](https://www.zus.pl/en/o-zus/komunikaty/-/asset_publisher/MjyWa4JLZeZ8/content/id/13932557), dated **2026-03-27**, confirms new payer-specific rates apply from **2026-04-01**. The worked scenario assumes the small-payer 1.67% rate throughout; another employer must substitute its January–March 2026 and April–December 2026 rates.

FEP (Bridging Pensions Fund) at 1.5% can apply to listed work in special conditions/special character; the assumed ordinary job is not such work. Employer-level PFRON obligations can also arise from workforce size and disability-employment ratios, but are not an individual percentage of this employee's salary and cannot be calculated from the facts supplied.

## 4. High-income solidarity levy (`danina solidarnościowa`)

The levy is **4%** of the excess over **PLN 1,000,000** of the statutory sum of qualifying income after permitted employee social-contribution deductions. For salary only under these assumptions:

`solidarity base = max(0, G − PLN 3,000 employment expenses − employee social − PLN 1,000,000)`,

rounded to whole złoty under the declaration instructions, and:

`solidarity levy = 4% × solidarity base`, rounded to whole złoty.

It is additional to ordinary PIT and is reported/paid separately by **30 April of the following calendar year**; the employer does not withhold it through ordinary payroll.

Primary legal pinpoint: consolidated [Personal Income Tax Act](https://isap.sejm.gov.pl/isap.nsf/download.xsp/WDU20240000226/U/D20240226Lj.pdf), Act of **1991-07-26**, consolidated text shown as at 2025-01-17, Chapter 6a, Article 30h(1)–(4), PDF pp. 314–315: 4%, PLN 1,000,000 excess, allowed social contributions, and 30 April declaration/payment. The calculation is also laid out field-by-field in the Ministry of Finance [DSF-1 form](https://www.podatki.gov.pl/media/5577/dsf-1-01_2019.pdf), section C, fields 18–25. Later amendments located during this research did not change Article 30h's rate or threshold for 2026.

## 5. PPK: default enrolment but excluded baseline

At age 30 the employee is within automatic enrolment (ages 18–55) unless a valid opt-out declaration is filed. Official PPK portal, [“Na czym polega autozapis do PPK?”](https://www.mojeppk.pl/aktualnosci/autozapis_ppk_0124.html), published **2024-01-23**, says employees 18–55 with mandatory pension/disability insurance are automatically enrolled; opt-outs are revisited on the four-year re-enrolment cycle (next in 2027, not 2026).

The problem expressly requests no PPK unless separately modelled, so the worked baseline assumes an effective opt-out. If enrolled at standard basic rates:

- employee pays **2% of PPK remuneration** from net pay;
- employer adds **1.5%**;
- the PPK remuneration base continues beyond the social-insurance 30-times cap;
- the employer payment is taxable employment income at 12%/32% (and can affect the solidarity base) but is exempt from social, health and fund contributions; and
- optional additional rates and a reduced employee rate down to 0.5% for qualifying low monthly pay are plan/person variables.

Official PPK pinpoints:

- [“Czy wysokość wpłaty podstawowej pracodawcy zależy od wysokości wpłaty pracownika?”](https://www.mojeppk.pl/faq/pracownik/wplaty-do-ppk_czy-wysokosc-wplaty-podstawowej-pracodawcy-zalezy-od-wysokosci-wplaty-pracownika.html): employer 1.5%, employee 2%, possible reduced employee rate.
- [“Czy w zakresie wpłat do PPK obowiązuje limit 30-krotności?”](https://www.mojeppk.pl/faq/pracodawca/wplaty-do-ppk_czy-w-zakresie-wplat-do-ppk-obowiazuje-limit-30-krotnosci-kwoty-prognozowanego.html): no; contributions continue after that ceiling.
- [“Czy od wpłaty sfinansowanej przez pracodawcę uczestnik PPK zapłaci ZUS?”](https://www.mojeppk.pl/faq/pracownik/podatki-i-skladki-zus_czy-od-wplaty-sfinansowanej-przez-pracodawce-uczestnik-ppk-zaplaci-zus.html): no social, health or extra-fund base.
- [PPK FAQ](https://www.mojeppk.pl/faq.html), headings “Czy wpłaty … stanowią przychód pracownika?” and “Jaki podatek …?”: employer contributions are taxable employment income and attract the employee's 12%/32% scale rate.

An exact alternative annual net is not shown because the employer contribution becomes income when transferred to the financial institution; December-pay timing and any pre-2026 contribution can move taxable PPK income between calendar years. For a same-year simplified estimate, add `2% × G` employee saving and `1.5% × G` employer cost, then recalculate PIT/solidarity with the employer 1.5% added to taxable employment income.

## 6. Monthly payroll versus annual reconciliation

For each payroll month the normal order is:

1. determine gross liable remuneration;
2. calculate employee pension and disability on the remaining part of the cumulative PLN 282,600 ceiling, plus uncapped sickness;
3. calculate 9% health on gross less those employee social contributions;
4. calculate PIT income as gross less employee social less the PLN 250 monthly employment expense (plus taxable employer PPK if participating);
5. apply payroll advance rules, including the 12%/32% threshold and, if the employee submitted the relevant PIT-2 statement to this sole payer, up to PLN 300 monthly tax reduction; and
6. deduct social, health, PIT advance and any employee PPK from cash pay.

At year end, PIT-37 recomputes the scale on annual rounded taxable income, applies the annual PLN 3,000 expense and PLN 3,600 reduction, and settles against advances. The solidarity levy is a separate self-assessment. Ministry of Finance's PIT-2 page cited above explains that PLN 300 is merely 1/12 of the annual reduction and can be allocated among up to three payers; its use changes cash timing, not the annual liability.

The worked calculations split regular annual salary into 11 equal cent-rounded monthly payments and a twelfth balancing payment. Each contribution is rounded to grosze monthly. The annual PIT and solidarity bases and liabilities are rounded to full złoty: fractions below PLN 0.50 are dropped and PLN 0.50 or more rounds upward. Small differences from a payroll engine can arise if the contractual pay-date pattern differs.

## 7. Independent worked calculations

### 7.1 Employee deductions, PIT and net

| Gross `G` | Pension base (capped) | Employee pension 9.76% | Disability 1.50% | Sickness 2.45% | Employee social total | Health 9% | PIT base | PIT | Solidarity | Net cash |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 100,000 | 100,000 | 9,759.97 | 1,500.00 | 2,450.04 | **13,710.01** | 7,766.05 | 83,290 | 6,395 | 0 | **72,128.94** |
| 300,000 | 282,600 | 27,581.76 | 4,239.00 | 7,350.00 | **39,170.76** | 23,474.69 | 257,829 | 54,905 | 0 | **182,449.55** |
| 500,000 | 282,600 | 27,581.78 | 4,239.00 | 12,249.96 | **44,070.74** | 41,033.68 | 452,929 | 117,337 | 0 | **297,558.58** |
| 1,000,000 | 282,600 | 27,581.75 | 4,239.00 | 24,500.04 | **56,320.79** | 84,931.13 | 940,679 | 273,417 | 0 | **585,331.08** |
| 3,000,000 | 282,600 | 27,581.76 | 4,239.00 | 73,500.00 | **105,320.76** | 260,521.13 | 2,891,679 | 897,737 | 75,667 | **1,660,754.11** |

Notes and checks:

- PIT base is whole-złoty rounding of `G − social − 3,000`. At PLN 100,000: `100,000 − 13,710.01 − 3,000 = 83,289.99`, rounded to 83,290; PIT is `12% × 83,290 − 3,600 = 6,394.80`, rounded to 6,395.
- At PLN 300,000: `10,800 + 32% × (257,829 − 120,000) = 54,905.28`, rounded to 54,905.
- Health at PLN 1,000,000 is the monthly-rounded sum of 9% of gross less that month's employee social contributions: PLN 84,931.13. It remains uncapped after pension/disability stop.
- PLN 1,000,000 gross does **not** itself trigger solidarity levy because deductible social contributions and the PLN 3,000 employment expense reduce statutory income below the levy threshold.
- At PLN 3,000,000, the solidarity excess is whole-złoty rounding of `3,000,000 − 105,320.76 − 3,000 − 1,000,000 = 1,891,679.24`, or PLN 1,891,679; 4% is PLN 75,667.16, rounded to PLN 75,667.

### 7.2 Employer-cost scenario: 1.67% accident rate, no PPK

| Gross `G` | Employer pension 9.76% | Disability 6.50% | Accident 1.67% | FP+FS 2.45% | FGŚP 0.10% | Employer contributions | Employer cost |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 100,000 | 9,759.97 | 6,500.04 | 1,670.04 | 2,450.04 | 99.96 | **20,480.05** | **120,480.05** |
| 300,000 | 27,581.76 | 18,369.00 | 5,010.00 | 7,350.00 | 300.00 | **58,610.76** | **358,610.76** |
| 500,000 | 27,581.78 | 18,368.98 | 8,349.96 | 12,249.96 | 500.04 | **67,050.72** | **567,050.72** |
| 1,000,000 | 27,581.75 | 18,369.01 | 16,700.04 | 24,500.04 | 999.96 | **88,150.80** | **1,088,150.80** |
| 3,000,000 | 27,581.76 | 18,369.00 | 50,100.00 | 73,500.00 | 3,000.00 | **172,550.76** | **3,172,550.76** |

The few-grosz variation in capped pension components comes from rounding each regular monthly payroll contribution, including the partial cap-crossing month. Substituting accident rate `a` changes employer contributions by `(a − 1.67%) × G`, with payroll-period rounding. Employer cost excludes PPK, FEP, PFRON and employer-specific benefits.

## 8. Universal rules versus variables

Universal for the stated employee profile:

- PIT scale 12%/32%, PLN 120,000 threshold and PLN 3,600 reduction;
- PLN 3,000 standard single-employment expense;
- employee rates 9.76%, 1.50%, 2.45% and health 9%;
- PLN 282,600 pension/disability base ceiling;
- employer pension 9.76% and disability 6.50%;
- uncapped contribution treatment described above; and
- 4% solidarity levy above the PLN 1,000,000 statutory income threshold.

Variables:

- accident rate and possible change between contribution years;
- employer status/exemptions for FP/FS and FGŚP;
- PPK participation, rates and transfer dates;
- special-condition work/FEP;
- employer-level PFRON liability;
- commuting or actual-ticket costs, copyright income, other income/reliefs, benefits and multiple payers; and
- exact payroll/pay-date and rounding sequence.

## 9. Evidence quality and unresolved facts

### Strongest evidence

The Ministry of Finance's dated 2026 employment-income and deduction pages directly state the live PIT scale, expenses and health non-deductibility. ZUS directly supplies the employee/employer split and the PLN 282,600 official 2026 ceiling, with the underlying 2025-11-19 ministerial announcement identified. Article 30h is direct statutory evidence for the solidarity levy. The official PPK portal gives unusually precise answers on rates, cap treatment and taxation.

### Weakest evidence / deliberately unresolved

- No universal accident premium exists. The dossier uses ZUS's exact 1.67% small-payer case and identifies the full 0.67%–3.33% range; a real employer's ZUS notice can differ and can change on 1 April.
- Employer PFRON, FEP and other sector/benefit costs need workforce and job facts and are excluded rather than guessed.
- An exact PPK alternative needs actual participation, additional-rate choices and transfer timing. Only statutory mechanics and a safe recalculation method are given.
- The current ZUS employee brochure exposes no issue date inside the PDF. Its rate split is corroborated by ZUS's dated 2026 contribution page and current government business table.
- Worked values use a disclosed equal-month pay and rounding convention. Different lawful payment timing may move a few grosze, and employer PPK transfers can move taxable income between years.
