# Netherlands employee salary and payroll rules — tax year 2026

Research status: **independent clean-room reconstruction from Dutch primary official sources**.  
Access date for every source: **2026-10-04**.

## Scope and modelling boundary

The employee is resident in the Netherlands for all of 2026, single, age 30, has no children, no other income, deductions or tax partner, works in an ordinary private-sector employment, and receives regular cash compensation. The expat/30% facility does not apply. The worked employee cases assume no occupational-pension deduction and no employer recovery of WGA premium. Those are not assertions that the costs are universally zero: both depend on the employer, plan or choice and are shown as unresolved variables.

`G` below means **total annual taxable gross cash pay, including holiday allowance**. This avoids adding holiday allowance twice. The calculation is an annual income-tax and national-insurance reconciliation, not a replication of periodic payroll-table withholding. All displayed results are rounded to the nearest euro only after calculating with the published percentages; unrounded intermediate amounts are given where useful.

## 1. Box 1 income tax and national insurance

For a person below AOW age throughout 2026, salary-only taxable Box 1 income `T` equals `G` under the assumptions. The combined 2026 schedule is:

| Slice of taxable Box 1 income | Combined rate | Composition |
|---|---:|---|
| `0–38,883` | 35.75% | 8.10% income tax + 17.90% AOW + 0.10% Anw + 9.65% Wlz |
| `38,883–78,426` | 37.56% | income tax |
| over `78,426` | 49.50% | income tax |

Thus:

`gross Box 1 levy = 0.3575 × min(T, 38,883) + 0.3756 × min(max(T − 38,883, 0), 39,543) + 0.495 × max(T − 78,426, 0)`.

The national-insurance component is already inside the first bracket; it is not added again. Its 2026 component rates total 27.65% and stop at income of EUR 38,883 (maximum approximately EUR 10,751).

Primary pinpoints:

- Belastingdienst, [“Tarieven, bedragen en percentages loonheffingen vanaf 1 januari 2026 — Bijlage bij de Nieuwsbrief Loonheffingen 2026”](https://odb.belastingdienst.nl/wp-content/uploads/2025/12/Cijferbijlage-2026-bij-Nieuwsbrief-LH-LH-209-1B61FD_TG.pdf), dated **2025-12-16**, effective **2026-01-01**, Table 1, PDF pp. 2–3: thresholds, combined rates and the AOW/Anw/Wlz/income-tax composition.
- Belastingdienst, [“Hoeveel moet u betalen?”](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/sociale_verzekeringen/premies_volks_en_werknemersverzekeringen/volksverzekeringen/hoeveel_moet_u_betalen), current 2026 page (no revision date displayed), table “tarieven en maximumbedragen premie volksverzekeringen”: 17.90%, 0.10%, 9.65%, maximum base EUR 38,883 and stated maximum EUR 10,751.

## 2. Tax credits (`heffingskortingen`)

### 2.1 General tax credit (`algemene heffingskorting`)

The credit depends on aggregate income (`verzamelinkomen`), equal to `G` here:

| 2026 aggregate income `V` | General credit `AHK` |
|---|---|
| `V ≤ 29,736` | EUR 3,115 |
| `29,736 < V < 78,426` | `3,115 − 6.398% × (V − 29,736)` |
| `V ≥ 78,426` | zero |

The taper is capped at the credit, so it cannot become negative.

### 2.2 Labour tax credit (`arbeidskorting`)

Employment income `A` equals `G` here:

| 2026 employment income `A` | Labour credit `AK` |
|---|---|
| `A ≤ 11,965` | `8.324% × A` |
| `11,965 < A ≤ 25,845` | `996 + 31.009% × (A − 11,965)` |
| `25,845 < A ≤ 45,592` | `5,300 + 1.950% × (A − 25,845)` |
| `45,592 < A < 132,920` | `max(0, 5,685 − 6.510% × (A − 45,592))` |
| `A ≥ 132,920` | zero |

Primary pinpoint for both credits: Belastingdienst, [“Voorlopige aanslag 2026: gebruikte tarieven en heffingskortingen”](https://www.belastingdienst.nl/wps/wcm/connect/nl/voorlopige-aanslag/content/voorlopige-aanslag-tarieven-en-heffingskortingen), current 2026 page (no revision date displayed), headings “Algemene heffingskorting” and “Arbeidskorting.” The dated 2025-12-16 payroll appendix above independently gives the amounts and percentages in Table 2a/2b, PDF p. 3. Its printed line says maximum labour-credit taper is reached at “132.290”; this is internally inconsistent with its own EUR 5,685 and 6.510% figures. The current Belastingdienst formula table gives **EUR 132,920**, and `45,592 + 5,685 / 0.06510 = 132,919.19`, so EUR 132,920 is used. This discrepancy is disclosed rather than silently guessed.

No income-dependent combination credit is available because the assumed employee has no child.

## 3. Employee-side social insurance and health treatment

- **National insurance:** AOW, Anw and Wlz are employee liabilities embedded in the first Box 1 rate as shown in section 1.
- **Employee insurance:** the employer normally bears WW, WAO/WIA and ZW premiums. Belastingdienst's [“Wat zijn loonheffingen?”](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/internationaal/personeel/u_bent_niet_in_nederland_gevestigd_loonheffingen_inhouden/wat_zijn_loonheffingen) (current page, no revision date displayed), heading “Premies werknemersverzekeringen,” says the employer bears them fully, with one exception: up to 50% of the WGA part of Whk may be recovered from the employee.
- **Optional WGA recovery:** [Wet financiering sociale verzekeringen](https://wetten.overheid.nl/BWBR0017745/2026-01-01), effective text at **2026-01-01**, Article 34(2), permits—not requires—the employer to recover at most half of the qualifying differentiated Whk premium. Belastingdienst's dated legal position [“KG:204:2026:10 Aanvulling WGA-hiaatverzekering”](https://kennisgroepen.belastingdienst.nl/publicaties/kg204202610-aanvulling-wga-hiaatverzekering-7-juli-2026/), published **2026-07-09**, updated **2026-07-20**, statutory discussion and conclusion, confirms the 50% ceiling and that recovery of the statutory differentiated Whk premium does not reduce taxable wage. The ZW-flex component cannot be recovered. The examples assume no recovery. In employer Scenario A below, the sector-43 WGA component is 0.80%, so an electing employer could reduce employee net by at most `0.40% × min(G, 79,409)`.
- **Zvw:** for an ordinary employee insured for employee insurance, the employer pays the 2026 **6.10% employers' Zvw levy** and the employee does not pay the 4.85% personal contribution. Belastingdienst, [“Werkgeversheffing Zvw of bijdrage Zvw?”](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/zorgverzekeringswet/bijdrage_zorgverzekeringswet/tabel_werkgeversheffing_zvw_of_bijdrage_zvw/), current 2026 table, row “Loon uit tegenwoordige dienstbetrekking … verzekerd voor de werknemersverzekeringen,” gives 6.10%, employer levy “Ja,” own contribution “Nee.”
- **Nominal health-insurance premium:** the employee separately pays a policy premium to a health insurer. It is neither a statutory percentage of salary nor an employer payroll withholding in this baseline, so no amount is invented or subtracted from salary net.

## 4. Statutory employer payroll premiums

The common 2026 maximum premium wage for employee insurance and maximum contribution wage for Zvw is **EUR 79,409 per employee per year**. On regular annual pay, define `M = min(G, 79,409)`.

| Employer item | 2026 rate/rule |
|---|---:|
| AWf low (WW) | 2.74% |
| AWf high | 7.74% |
| Aof low | 6.27% |
| Aof high | 7.63% |
| Wko supplement | 0.50% |
| Whk | employer/sector-specific |
| Employer Zvw levy | 6.10% |

The **low AWf** applies where the employment contract is written, indefinite and not on-call; otherwise the high rate generally applies, subject to listed exceptions and possible retrospective revision. Source: Belastingdienst, [“Lage en hoge AWf-premie: hoe werkt de premiedifferentiatie WW?”](https://www.belastingdienst.nl/wps/wcm/connect/nl/personeel-en-loon/content/premiedifferentiatie-ww-lage-en-hoge-ww-premie), current 2026 page, headings “Wanneer betaalt u de lage en wanneer de hoge AWf-premie?” and the displayed 2.74%/7.74% rates.

Aof uses the low rate for small employers and high rate for medium/large employers. Employer size for 2026 uses the employer's 2024 premium wage: small through EUR 1,082,500, medium through EUR 4,330,000, large above EUR 4,330,000. Whk is sectoral for small employers, individual for large employers, and blended for medium employers.

Primary numeric pinpoint: the dated Belastingdienst payroll appendix, Table 9 (PDF p. 9), gives AWf, Aof, Wko and size thresholds; Table 10 (pp. 10–11) gives small-employer sector Whk rates; Table 11 (pp. 11–12) gives the EUR 79,409 cap; Table 12 (p. 12) gives Zvw 6.10%. UWV, [“Januarinota 2026”](https://www.uwv.nl/assets-kai/files/3f0c1774-1ea5-478d-8c40-64f649f90a58/uwv-januarinota-2026.pdf), published **January 2026**, Table 1.5, PDF p. 9, corroborates the cap and shows the 2026 national-average Whk of 1.52% (WGA 0.96% + ZW-flex 0.56%).

There is no single universal employer percentage. Two reproducible illustrations are therefore kept separate:

### Scenario A — specified small business-services employer, stable contract

- written indefinite non-on-call contract: AWf low 2.74%;
- small employer: Aof low 6.27%;
- Wko 0.50%;
- small-employer sector 43, “Zakelijke Dienstverlening I”: Whk 1.16% (WGA 0.80% + ZW-flex 0.36%); and
- Zvw 6.10%.

Total: **16.77% × M**. Sector 43 is a modelling choice, not a national rule; the exact figures are in the dated appendix, Table 10, row 43.

### Scenario B — high-rate/national-average benchmark

- flexible or otherwise high-AWf contract: 7.74%;
- medium/large Aof rate: 7.63%;
- Wko 0.50%;
- UWV national-average Whk benchmark: 1.52%; and
- Zvw 6.10%.

Total: **23.49% × M**. This is an analytical benchmark, not an employer-specific statutory rate: a real medium/large employer must use its Whk decision/notification. UWV's [“Premienota 2026 — Gedifferentieerde premies WGA en Ziektewet”](https://www.uwv.nl/assets-kai/files/4b2acadd-fba9-4b73-bf3c-311773371617/gedifferentieerde-premies-wga-en-ziektewet-2026.pdf), 2026 publication (no exact issue date visible in the PDF), section 1.1, Table 1.1, explains the individual/sector differentiation and gives average, minimum and maximum WGA and ZW parameters.

Ufo 0.68% is an employer-government premium and is not included for the stipulated ordinary private employer.

## 5. Holiday allowance

The statutory starting point is at least **8%** holiday allowance on covered earned pay. [Wet minimumloon en minimumvakantiebijslag](https://wetten.overheid.nl/BWBR0002638/2026-01-01), effective text at **2026-01-01**, Articles 15–16, states the 8% right and the collective/contractual exceptions subject to minimum-pay protection. Rijksoverheid, [“Hoe hoog is mijn vakantiegeld?”](https://www.rijksoverheid.nl/vraag-en-antwoord/vakantiedagen-en-vakantiegeld/hoe-hoog-is-mijn-vakantiegeld) (current page, no revision date displayed), states that it is ordinarily calculated on prior-year gross salary, paid at least annually, and that an employee earning more than three times minimum wage may agree in writing to a lower or zero allowance.

Holiday allowance is taxable wage and is subject to the same employee and employer levies; Rijksoverheid's [“Wat moet ik als werkgever afdragen over het loon van werknemers?”](https://www.rijksoverheid.nl/vraag-en-antwoord/inkomstenbelasting/loonheffing-premies-werkgever) (current page, no revision date displayed), heading “Loonheffing over alle beloningen,” expressly lists salary and holiday pay.

Because `G` is inclusive, a conventional package consisting only of base salary plus 8% allowance decomposes as:

`base = G / 1.08`; `holiday allowance = G − base`.

This decomposition does not change tax or contributions. A contract quoting salary **exclusive** of holiday allowance would require adding it before applying this dossier.

## 6. Occupational pension and other non-universal costs

There is no universal second-pillar rate. Rijksoverheid, [“Waar heb ik recht op als ik met pensioen ga?”](https://www.rijksoverheid.nl/vraag-en-antwoord/pensioen/waar-heb-ik-recht-op-als-ik-met-pensioen-ga) (current page, no revision date displayed), heading “Pensioen via uw werkgever,” says not every employer offers a plan; a mandatory industry fund obliges an employer in that industry. Plan contribution rate, pensionable salary, franchise and employer/employee split are therefore unresolved without a sector and plan.

Where an employee pension contribution is withheld under a qualifying employer plan, it normally reduces fiscal wage. Belastingdienst, [“U betaalt vrijwillig pensioenpremie”](https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/prive/werk_en_inkomen/pensioen_en_andere_uitkeringen/u-betaalt-vrijwillig-pensioenpremie/) (current page, no revision date displayed), final note, confirms employer-withheld pension premiums have already reduced fiscal wage. The examples deliberately model a no-plan statutory baseline; a pension scenario cannot be calculated responsibly from the supplied facts.

Other CAO or sector funds, disability supplements, training funds and risk insurances are likewise variable and excluded.

## 7. Calculation method

For each total annual gross `G`:

1. `T = A = V = G` because there are no deductions or other income.
2. Calculate gross Box 1 levy by section 1.
3. Calculate `AHK` and `AK` by section 2.
4. `annual employee levy = max(0, gross Box 1 levy − AHK − AK)`.
5. `cash net before the separately purchased nominal health-policy premium = G − annual employee levy`.
6. Employer Scenario A contribution is `16.77% × min(G, 79,409)`; Scenario B is `23.49% × min(G, 79,409)`.
7. Employer cost shown is gross plus that scenario's statutory contribution. Pension/CAO costs are not included.

Periodic payroll withholding, especially the special-remuneration table used when holiday allowance is paid as a lump, can differ during the year. Income-tax assessment reconciles the annual liability calculated from actual annual income.

## 8. Independent worked calculations

### 8.1 Employee tax and net cash

| Gross `G` | First-bracket levy | Second-bracket levy | Third-bracket levy | Gross Box 1 levy | AHK | AK | Final levy | Net cash |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 7,150.00 | 0 | 0 | 7,150.00 | −3,115.00 | −3,487.57 | **547** | **19,453** |
| 60,000 | 13,900.67 | 7,931.55 | 0 | 21,832.22 | −1,178.71 | −4,747.04 | **15,906** | **44,094** |
| 100,000 | 13,900.67 | 14,852.35 | 10,679.13 | 39,432.15 | 0 | −2,143.04 | **37,289** | **62,711** |
| 200,000 | 13,900.67 | 14,852.35 | 60,179.13 | 88,932.15 | 0 | 0 | **88,932** | **111,068** |
| 600,000 | 13,900.67 | 14,852.35 | 258,179.13 | 286,932.15 | 0 | 0 | **286,932** | **313,068** |

Checks:

- EUR 20,000 labour credit: `996 + 31.009% × (20,000 − 11,965) = 3,487.57315`; levy `7,150 − 3,115 − 3,487.57315 = 547.42685`.
- EUR 60,000 general credit: `3,115 − 6.398% × (60,000 − 29,736) = 1,178.70928`; labour credit `5,685 − 6.510% × (60,000 − 45,592) = 4,747.03920`.
- EUR 100,000 labour credit: `5,685 − 6.510% × 54,408 = 2,143.03920`; both credits are zero from their respective endpoints thereafter.
- At EUR 600,000 the top slice is `(600,000 − 78,426) × 49.50% = 258,179.13`.

No employee-insurance or employee Zvw percentage is subtracted. An employer-elected WGA recovery and the employee's nominal health-policy premium would reduce spendable cash but are not determinable from the stated facts.

### 8.2 Holiday-allowance decomposition (illustrative 8%-inclusive package)

| Total gross `G` | Base `G / 1.08` | 8% allowance |
|---:|---:|---:|
| 20,000 | 18,518.52 | 1,481.48 |
| 60,000 | 55,555.56 | 4,444.44 |
| 100,000 | 92,592.59 | 7,407.41 |
| 200,000 | 185,185.19 | 14,814.81 |
| 600,000 | 555,555.56 | 44,444.44 |

### 8.3 Employer scenarios

| Gross `G` | Premium base `M` | Scenario A contribution 16.77% | Scenario A cost | Scenario B contribution 23.49% | Scenario B cost |
|---:|---:|---:|---:|---:|---:|
| 20,000 | 20,000 | 3,354.00 | **23,354.00** | 4,698.00 | **24,698.00** |
| 60,000 | 60,000 | 10,062.00 | **70,062.00** | 14,094.00 | **74,094.00** |
| 100,000 | 79,409 | 13,316.89 | **113,316.89** | 18,653.17 | **118,653.17** |
| 200,000 | 79,409 | 13,316.89 | **213,316.89** | 18,653.17 | **218,653.17** |
| 600,000 | 79,409 | 13,316.89 | **613,316.89** | 18,653.17 | **618,653.17** |

Both schedules stop growing once the common EUR 79,409 premium ceiling is reached. They exclude pension and CAO funds. Scenario A is a fully specified statutory case; Scenario B deliberately uses UWV's national-average Whk and must not be represented as an actual employer quote.

## 9. Universal rules versus variables

Universal within the stated assumptions:

- the three 2026 Box 1 brackets and embedded national-insurance treatment;
- the published general and labour-credit formulas;
- ordinary employee Zvw treatment;
- the EUR 79,409 annual employee-insurance/Zvw wage ceiling;
- the 8% holiday-allowance statutory starting point and taxation of holiday pay; and
- employer responsibility for employee-insurance premiums, subject to the limited optional WGA recovery.

Employer/employee-specific variables:

- written indefinite/non-on-call versus flexible contract (AWf);
- employer size (Aof) and sector/claims history or own-risk status (Whk);
- optional recovery of up to half the WGA component;
- occupational-pension and CAO-fund coverage, rates, franchise and split;
- whether quoted annual salary includes holiday allowance and whether a lawful exception applies;
- nominal health-policy premium; and
- taxable benefits, reimbursements, deductions, other income, multiple employments and cross-border insurance.

## 10. Evidence assessment and unresolved points

### Strongest evidence

The strongest source is Belastingdienst's **2025-12-16** numerical appendix for payroll levies effective 2026-01-01: it places brackets, component rates, credits, AWf/Aof/Wko, all sector Whk values, the common ceiling and Zvw in one dated official document. The current Belastingdienst assessment page independently provides the annual credit formulas. UWV's January 2026 note corroborates the ceiling and average Whk components. Legislation supplies the vacation-allowance and WGA-recovery authority.

### Weakest evidence / deliberately unresolved

- The occupational-pension and CAO-fund amounts cannot be derived without a sector and plan; no average is substituted.
- A real Whk rate requires the employer's sector or individual decision. Scenario A fixes sector 43; Scenario B is explicitly a national-average benchmark.
- The dated payroll appendix contains the apparent “132.290” labour-credit endpoint transposition described in section 2.2. The current official formula and arithmetic support EUR 132,920, which is disclosed transparently.
- Several current Belastingdienst/Rijksoverheid explanatory pages display the 2026 values but no visible publication or revision date; they are identified as undated current pages and paired with dated official evidence wherever possible.
- Annual computations here retain percentages through the formula and round only presentation totals. Periodic payroll tables and the final assessment may differ by small rounding amounts; no unsupported statutory rounding rule is invented.
