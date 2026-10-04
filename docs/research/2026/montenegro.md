# Montenegro employee payroll — income year 2026

**Research cut-off / access date:** 2026-10-04  
**Currency:** euro (EUR)  
**Location:** Podgorica (Glavni grad)  
**Case:** resident, age 30, single, no children, ordinary private-sector office employee, twelve equal monthly cash salaries, no benefits, reliefs or employer incentive. For a reproducible employer-cost result, the employer is an ordinary company and Chamber member, and the employee is assumed **not** to be a union member.

This is a clean-room reconstruction from Montenegro government, Tax Administration, Ministry, Official Gazette, Podgorica and statutory-fund sources. It distinguishes payroll withheld during 2026 from a possible later refund of pension contributions above the annual maximum, whose 2026 amount had not yet been promulgated at the research cut-off.

## Executive result

For an equal monthly gross salary `m`:

```text
monthly PIT = 0% × min(m, 700)
            + 9% × min(max(m − 700, 0), 300)
            + 15% × max(m − 1,000, 0)

employee PIO pension contribution = 10% × m
employee unemployment contribution = 0.5% × m
payroll net = m − employee PIO − employee unemployment − PIT

Podgorica surtax = 15% × PIT                   [employer-side payroll cost]
employer unemployment = 0.5% × m
Labour Fund = 0.2% × m
Chamber contribution = 0.27% × m
employer cost = m + those four employer-side amounts
```

There is no standard employee or employer compulsory health contribution after the Europe Now reforms, and employer PIO is **0%**. The statutory employee deductions are therefore 10% PIO, 0.5% unemployment and PIT. Podgorica surtax does not reduce the net salary in the official payroll presentation; it is added to employer funds required.

## Primary-source rules

### 1. Wage income tax: monthly 0% / 9% / 15%

The [consolidated Law on Personal Income Tax](https://wapi.gov.me/download/d93f2f4f-b97b-44fc-9409-7bf26be031c1?version=1.0) (`Zakon o porezu na dohodak fizičkih lica`) gives the operative rules:

- article 10(1), PDF page 3: **0%** on taxable personal income up to **EUR 700**, **9%** from **EUR 700.01 to EUR 1,000**, and **15%** above **EUR 1,000**;
- article 14(1), PDF page 4: personal income includes salary, salary compensation and other income under labour rules;
- article 15, PDF page 4: taxable employment income is the **gross** personal receipt;
- article 46(1)–(4), PDF pages 13–14: the employer calculates, withholds and pays tax **at each payment**, using the gross personal receipt in that calculation period and the article 10 rates.

The PDF notes that this article 10 text applies from 1 January 2025. The later amendment in Official Gazette No. 160/2025, effective 1 January 2026, added/revised gambling-income rules but did not change these wage bands; the Government’s 2026 [“Jasna pravila oporezivanja dobitaka od igara na sreću”](https://www.gov.me/clanak/jasna-pravila-oporezivanja-dobitaka-od-igara-na-srecu-zakon-se-primjenjuje-jednako-na-sve) (5 January 2026) identifies that amendment and effective date.

These are **monthly marginal bands**, not annual brackets. For twelve equal payments, their annual equivalent is:

```text
annual PIT = 9% × min(max(G − 8,400, 0), 3,600)
           + 15% × max(G − 12,000, 0)
```

There is no separate personal allowance to deduct: the zero-rate band performs that function.

### 2. Podgorica surtax

The Ministry of Finance’s [“Uputstvo o načinu obračunavanja plaćanja poreza i doprinosa iz i na lična primanja po osnovu zaposlenja”](https://www.gov.me/dokumenta/f73befc2-975e-42d9-af00-4d5de0a3172d), published **1 April 2026**, states in article 6 that municipal surtax is calculated at the local-government rate and its base is the **calculated employee income tax**. Its worked layout places net salary at gross less employee tax/contributions and adds surtax to total funds needed by the employer.

Podgorica’s official [half-year budget execution report](https://podgorica.me/wp-content/uploads/2024/08/Polugodisnji-izvjestaj-o-ukupno-ostvarenim-primicima-i-izvrsenim-izdacima-iskazanim-u-skladu-sa-organizacionom-funkcionalnom-i-ekonomskom-klasifikacijom-01.01.-30.06.2024.g.pdf), revenue note “Prirez porezu na dohodak fizičkih lica,” states that taxpayers carrying on activity in the Capital City pay surtax at **15%**. The legal authorization is article 7 of the Law on Local Self-Government Financing: up to 13% generally and up to 15% for the Capital City and Old Royal Capital. The applicable Podgorica decision remains listed as **in force** in the official gazette system: [“Odluka o prirezu porezu na dohodak fizičkih lica”](https://www.sluzbenilist.me/propisi/360031), Official Gazette—Municipal Regulations No. 17/2023, published 12 April 2023.

Podgorica is selected because the surtax is municipal rather than nationally uniform and because its 15% rate is expressly documented by the Capital City. A different municipality can change employer cost, but not employee net in the official calculation layout.

### 3. Social-insurance contributions after Europe Now 1 and 2

The Tax Administration’s [current consolidated Law on Contributions for Compulsory Social Insurance](https://www.gov.me/dokumenta/ebe29cb5-e065-48b2-8703-733f7bab27d9), posted **12 January 2026**, and the Ministry’s April 2026 payroll instruction establish:

| Contribution | Employee | Employer | Pinpoint |
|---|---:|---:|---|
| Pension/disability (PIO) | 10.0% | 0% | Contributions Law article 15(1); payroll instruction articles 4–5 |
| Health | 0% | 0% | Contributions Law article 17 is deleted; no health line remains in instruction articles 4–5 |
| Unemployment | 0.5% | 0.5% | Contributions Law article 18(1); instruction articles 4–5 |

Tax Administration’s [“Rast budžetskih prihoda, pojačane aktivnosti PU u sezoni”](https://www.gov.me/clanak/rast-budzetskih-prihoda-pojacane-aktivnosti-pu-u-sezoni) (7 May 2025) independently records the Europe Now 2 change effective from 1 October 2024: insured-person PIO fell from 15% to **10%** and employer PIO from 5.5% to **0%**. The Government’s [15 August 2024 session release](https://www.gov.me/clanak/saopstenje-o-odlukama-vlade-crne-gore-donijetim-na-telefonskoj-sjednici-odrzanoj-15-avgusta-2024-godine) describes the same 20.5%-to-10% reform. Compulsory health payroll contributions had already been abolished under Europe Now 1 from 1 January 2022; the current law/instruction confirms zero by deletion and omission rather than by printing a new 0% rate.

The base is gross remuneration. Contributions Law article 3a defines gross salary to include pay for work/time worked, increased pay, salary compensation and other personal income under law, collective agreement or employment contract that is subject to PIT. Articles 9(1) and 11(1) use gross salary for ordinary employee PIO and unemployment.

### 4. Minimum and maximum contribution bases

**Minimum.** Contributions Law article 4(21) defines the lowest monthly contribution base as the gross basic salary prescribed by the General Collective Agreement for the relevant skill category; articles 9 and 11 say the ordinary employee base cannot be below it. Separately, the Government’s official [Europe Now 2 Q&A](https://www.gov.me/clanak/pitanja-i-odgovori-za-evropu-sad-2) (31 October 2024; attachment published 6 November 2024) states the minimum **net** wage is EUR 600 for jobs through qualification level V and EUR 800 for jobs at level VI or higher. The exact minimum applicable to an employee therefore depends on the job’s required qualification and contractual/collective-agreement classification. Every requested gross salary is safely above either minimum, so that unresolved job classification does not affect the examples.

**Maximum.** Contributions Law article 14 is narrower and procedurally important:

- PIO is calculated and paid across the insured person’s bases during the year;
- the Ministry establishes the highest annual PIO base annually from prior-year average-wage movement;
- excess PIO is dealt with by a **refund** procedure.

As at 4 October 2026, an official 2026 amount could not be found because it had not yet been issued. The Ministry’s official [2026 work programme](https://wapi.gov.me/download/cb435340-6d57-4f41-95d2-716c15e6da20?version=1.0), item 30, schedules the `Pravilnik o usklađivanju iznosa najviše godišnje osnovice ... za 2026. godinu` for **Q4 2026** and says that instrument will prescribe the amount. It would be guessing to substitute the 2025 maximum or derive a value without the prescribed act.

Accordingly, the worked table shows **in-year payroll withholding** of PIO on full gross. Once the 2026 maximum `M` is officially set, a worker with `G > M` may have a refund of `10% × (G − M)` (subject to the statutory procedure), increasing final after-refund cash by that amount. Article 14 applies the maximum only to PIO, not unemployment, PIT or other levies.

### 5. Labour Fund, Chamber and other employer amounts

- **Labour Fund:** the Fund’s official [“O Fondu”](https://www.gov.me/clanak/o-fondu) page, section “Finansiranje Fonda rada,” states **0.20%** at employer expense on the unemployment-contribution base. The April 2026 payroll instruction article 5(3) says the same.
- **Chamber:** the official-gazette record [“Odluka o visini, načinu i rokovima plaćanja članskog doprinosa za Privrednu komoru Crne Gore za 2026. godinu”](https://www.sluzbenilist.me/propisi/389055), Official Gazette No. 151/2025, published 19 December 2025, in force 20 December and applicable **1 January 2026**, sets the 2026 member contribution. Decision items 1–3 specify **0.27%** of gross employee salaries reported on IOPPD and payment when IOPPD is filed. The Chamber’s enabling [Law on the Chamber of Economy, articles 30–31](https://komora.me/wp-content/uploads/2022/01/zakon_pkcg.pdf) requires members to fund the Chamber and authorizes the Assembly to set the base/rate annually. The modeled ordinary company is a member, so 0.27% is included.
- **Union fund:** article 30 of the [General Collective Agreement](https://amrrs.gov.me/sites/default/files/documents/library/Op%C5%A1ti%20kolektivni%20ugovor.pdf) requires an employer to pay **0.2% of salary only for an employee who is a member** of the relevant representative union (and contains a branch-agreement exception). Union membership was not specified, so the reproducible table assumes non-membership and excludes it. If applicable, add `0.2% × G` to employer cost.
- **Increased-duration pension service:** Contributions Law article 16 imposes additional employer PIO rates of 6%, 9%, 12%, 18% or 28% for designated jobs whose 12 months count as 14, 15, 16, 18 or 24 months. Ordinary office employment is not such a job, so no additional rate is modeled.

No separate universal accident-insurance payroll rate was found in the current contributions law or April 2026 payroll instruction. It would be improper to invent one.

### 6. Bonus / 13th salary and reporting

There is no universal preferential “13th salary” regime in the official sources reviewed. A cash bonus arising under the employment relationship falls within gross personal income under Income Tax Law articles 14–15 and the broad gross-salary contribution base in Contributions Law article 3a. Article 46 applies PIT at **each payment**, so paying a bonus in one month applies the monthly brackets to that enlarged month; it is not equivalent to spreading it over twelve months. The worked examples assume regular equal monthly salary and no bonus.

Under the Ministry’s April 2026 instruction:

- article 7: the employer withholds/remits tax, employee and employer contributions, and surtax simultaneously with salary payment;
- article 8: employer reporting is on the unified **IOPPD** report;
- article 9: IOPPD is due to the tax authority by the **15th of the month for all payments made in the previous month**.

The Ministry’s [IOPPD form regulation](https://www.gov.me/dokumenta/43f4a881-c098-4e64-8f0e-312d68de6c58), published **2 April 2026**, is the current form authority.

## Worked calculations

### Formulas for twelve equal salary payments

Let `G` be annual gross salary and `g = G/12` monthly gross.

```text
annual PIT I = 0.09 × min(max(G − 8,400, 0), 3,600)
             + 0.15 × max(G − 12,000, 0)

employee PIO payroll deduction P = 0.10G
employee unemployment Ue = 0.005G
payroll net N = G − P − Ue − I

Podgorica surtax S = 0.15I
employer unemployment Ua = 0.005G
Labour Fund F = 0.002G
Chamber K = 0.0027G
employer cost C = G + S + Ua + F + K
```

The table is an exact annual equivalent before cent rounding in each monthly payroll and **before any later PIO refund above the unresolved 2026 annual maximum**.

| Gross `G` | Monthly gross | Employee PIO 10% | Employee unemployment 0.5% | PIT | Payroll net | Podgorica surtax 15% of PIT | Employer unemployment 0.5% | Labour Fund 0.2% | Chamber 0.27% | Employer cost |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000.00 | 1,666.67 | 2,000.00 | 100.00 | 1,524.00 | 16,376.00 | 228.60 | 100.00 | 40.00 | 54.00 | 20,422.60 |
| 60,000.00 | 5,000.00 | 6,000.00 | 300.00 | 7,524.00 | 46,176.00 | 1,128.60 | 300.00 | 120.00 | 162.00 | 61,710.60 |
| 100,000.00 | 8,333.33 | 10,000.00 | 500.00 | 13,524.00 | 75,976.00 | 2,028.60 | 500.00 | 200.00 | 270.00 | 102,998.60 |
| 200,000.00 | 16,666.67 | 20,000.00 | 1,000.00 | 28,524.00 | 150,476.00 | 4,278.60 | 1,000.00 | 400.00 | 540.00 | 206,218.60 |
| 600,000.00 | 50,000.00 | 60,000.00 | 3,000.00 | 88,524.00 | 448,476.00 | 13,278.60 | 3,000.00 | 1,200.00 | 1,620.00 | 619,098.60 |

The EUR 20,000 row, expanded:

```text
monthly gross                         20,000 / 12 = 1,666.6667
monthly PIT                           27 + 15% × 666.6667 = 127.00
annual PIT                            127 × 12 = 1,524.00
employee PIO                          20,000 × 10% = 2,000.00
employee unemployment                 20,000 × 0.5% = 100.00
payroll net                           20,000 − 2,000 − 100 − 1,524 = 16,376.00
Podgorica surtax                      1,524 × 15% = 228.60
employer unemployment                 20,000 × 0.5% = 100.00
Labour Fund                           20,000 × 0.2% = 40.00
Chamber                               20,000 × 0.27% = 54.00
employer cost                         20,000 + 228.60 + 100 + 40 + 54 = 20,422.60
```

If the employee is a qualifying union member, employer cost instead increases by EUR 40 / 120 / 200 / 400 / 1,200 respectively across the five rows.

## Universal versus location/sector/employer-specific items

| Item | Status in model |
|---|---|
| Monthly wage PIT 0% / 9% / 15% | National, included |
| Employee PIO 10%; unemployment 0.5% | National ordinary employee, included |
| Employer PIO 0%; unemployment 0.5%; health 0% | National ordinary employer, included |
| Labour Fund 0.2% | Statutory employer levy, included |
| Podgorica surtax 15% of PIT | Location-specific, included only because Podgorica was selected |
| Chamber contribution 0.27% | 2026 member levy on gross IOPPD salaries; modeled ordinary company is a member |
| Union fund 0.2% | Employee-membership/branch-agreement dependent, excluded and separately quantified |
| Increased-duration PIO 6%–28% | Hazardous/designated-job specific, excluded for ordinary office work |
| 2026 annual PIO maximum/refund | Statutory mechanism, but amount unresolved as of access date; table shows payroll withholding before refund |

## Evidence assessment and unresolved facts

**Strongest evidence:** the current consolidated tax and contribution laws; the Ministry of Finance’s April 2026 payroll instruction (which supplies the calculation order and sides of payroll); the Tax Administration’s official confirmation of the post-Europe Now 2 PIO rates; and the official 2026 Chamber decision record.

**Weakest / unresolved:**

1. The **2026 highest annual PIO base was not yet promulgated by 4 October 2026**; the Ministry itself scheduled it for Q4. Final after-refund PIO/net for high earners therefore cannot be stated without guessing. The table deliberately reports actual payroll withholding before that refund.
2. The contribution minimum depends on the position’s qualification and collective-agreement classification. The requested salaries are far above any relevant minimum, so this cannot affect the results.
3. Union-fund cost depends on membership and branch rules. It is excluded under the explicit non-member scenario and shown separately.
4. Monthly cent rounding can move annual figures by cents where `G/12` is recurring. The formulas and table retain exact annual equivalents.

No other unresolved point changes the stated payroll-withholding results under the explicit assumptions.
