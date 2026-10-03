# Sweden employee salary and payroll rules — income year 2026

Research status: **independent clean-room reconstruction from Swedish primary official sources**.  
Access date for every source: **2026-10-04**.

## Scope and explicit assumptions

The employee is a Swedish tax resident, single, under age 66 at the start of 2026, with no children, no other income or deductions, no membership in the Church of Sweden or another registered religious community, and ordinary private employment paid as regular cash salary throughout the year. The examples also assume no voluntary trade-union or unemployment-fund membership fees; those membership-dependent credits are described separately below.

The worked employer-cost examples additionally assume the employee was born **1960–2002**. “Under 66” alone is not enough to choose the employer rate in 2026 because a temporary youth reduction applies to persons born 2003–2007 from April onward.

The examples calculate **final annual tax**, rather than reproducing the banded monthly withholding table. For regular main employment, the employer withholds preliminary tax using the employee's tax table and column 1. Final tax reconciles through the income assessment. Amounts are in Swedish kronor (SEK).

## 1. Municipality choice and local rates

### 1.1 Reproducible assumption: Stockholm municipality

Stockholm is used because Skatteverket's official 2026 municipality file provides all three relevant non-church rates on a single reproducible row:

| Component | 2026 rate |
|---|---:|
| Stockholm municipal tax | 18.22% |
| Stockholm regional tax | 12.33% |
| **Municipal income tax used in credits (`KI`)** | **30.55%** |
| Stockholm burial fee | 0.070% |
| Total excluding church fee | 30.620% |

Source: Skatteverket, [“Kommunala skattesatser 2026”](https://www.skatteverket.se/download/18.1522bf3f19aea8075ba428/1765291540367/skattesatser-kommuner-2026.txt) (official 2026 text dataset), header and Stockholm rows: columns `Kommunal-skatt 18.22`, `Landstings-skatt 12.33`, `Begravnings-avgift 0.07`, and `Summa, exkl. kyrkoavgift 30.62`. No publication timestamp is exposed in the text file; its URL and placement under Skatteverket's 2026 tables identify the tax year.

The choice is more reproducible than using the 2026 national average of 34% reported in the technical payroll publication: that rounded table rate incorporates a standardized burial/religious-community component and is not appropriate for the stipulated non-member.

The 30.620% total rounds to **tax table 31**. Under Skatteverket's [“Skattetabeller”](https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/skattetabeller.4.96cca41179bad4b1aa8a46.html) (“Tax tables”), 2026 section “Så beräknas skatten,” the table number is the whole-number rounding of municipal + regional + burial fee (+ church fee only for members), and column 1 is salary for a person under 66 whose income qualifies for the earned-income credit. Tax-table withholding is preliminary; the formulas below calculate annual final tax at the exact Stockholm rates.

### 1.2 Burial fee is not church tax

Non-members still pay the burial fee. Skatteverket, [“Begravningsavgift”](https://www.skatteverket.se/privat/skatter/arbeteochinkomst/askattsedelochskattetabeller/begravningsavgift.4.1ee2ea81054cf37b1c800030.html) (“Burial fee”), current 2026 table, gives Stockholm **0.070%** and says liability depends on the municipality of registration on 1 November of the preceding year. It is charged on municipally taxable earned income. No church/community fee is included here.

## 2. Tax base and basic allowance (`grundavdrag`)

For salary-only cases, fixed earned income (`fastställd förvärvsinkomst`, `FFI`) is annual gross salary after any general deductions; under the assumptions there are none, so `FFI = gross salary G`. Taxable earned income (`BFI`) is:

`BFI = FFI − grundavdrag`.

The 2026 price base amount (`PBB`) is **SEK 59,200**. For a person under 66, calculate the unrounded basic allowance as follows:

| FFI interval | Unrounded allowance |
|---|---|
| `FFI ≤ 0.99 PBB` (≤ 58,608) | `0.423 PBB` |
| `0.99 PBB < FFI ≤ 2.72 PBB` (58,608–161,024) | `0.423 PBB + 20% × (FFI − 0.99 PBB)` |
| `2.72 PBB < FFI ≤ 3.11 PBB` (161,024–184,112) | `0.77 PBB` |
| `3.11 PBB < FFI ≤ 7.88 PBB` (184,112–466,496) | `0.77 PBB − 10% × (FFI − 3.11 PBB)` |
| `FFI > 7.88 PBB` (> 466,496) | `0.293 PBB` |

The allowance cannot exceed FFI and is rounded **up to the next whole SEK 100**. Thus the high-income allowance is `ceil100(0.293 × 59,200) = SEK 17,400`.

Primary pinpoint: Skatteverket, [“Teknisk beskrivning för skattetabeller 2026 (SKV 433), edition 36”](https://www.skatteverket.se/download/18.1522bf3f19aea8075ba55c/1766385913260/teknisk-beskrivning-skv-433-2026-utgava-36.pdf) (“Technical description for tax tables 2026”), dated **2025-12-10**, pp. 8–9, section 6 “Grundavdrag.” The document says the tax tables form part of SKVFS 2025:20, effective **2026-01-01**. The underlying [Income Tax Act (1999:1229)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/inkomstskattelag-19991229_sfs-1999-1229/), issued **1999-12-16**, consolidated through 2026, contains the basic-allowance rules in Chapter 63.

## 3. Municipal and state income tax

### 3.1 Municipal and regional tax

Stockholm municipal/regional income tax is:

`Municipal tax = floor(BFI × 30.55%)`.

The burial fee is separately:

`Burial fee = floor(BFI × 0.070%)`.

SKV 433, pp. 13–14, section 7.3, says the municipal income tax consists of municipal and regional tax and uses the same taxable earned-income base as state tax; fractions of a krona are dropped after calculation. The burial fee is not reducible by the tax credits discussed below.

### 3.2 State income tax

The 2026 state-tax threshold (`skiktgräns`) is **SEK 643,000 of taxable earned income**, after basic allowance. State tax is:

`State tax = 20% × max(BFI − 643,000, 0)`.

For a person under 66, Skatteverket gives the approximate pre-allowance breakpoint as **SEK 660,400** (`643,000 + 17,400`). Sources:

- Skatteverket, [“När ska man betala statlig inkomstskatt och hur hög är den?”](https://www.skatteverket.se/privat/etjansterochblanketter/svarpavanligafragor/inkomstavtjanst/privattjansteinkomsterfaq/narskamanbetalastatliginkomstskattochhurhogarden.5.10010ec103545f243e8000166.html), current 2026 section: 20%, SEK 643,000 taxable threshold, SEK 660,400 breakpoint for a person under 66.
- SKV 433, dated 2025-12-10, pp. 13–14, section 7.2: 20% on taxable earned income above SEK 643,000 (with no state tax unless the base exceeds the threshold by at least SEK 200).

## 4. Employee pension charge and offsetting credit

The general pension charge (`allmän pensionsavgift`) is a statutory employee charge, but a tax credit normally offsets it 100%:

- charge: **7%** of FFI;
- 2026 contribution-base ceiling: **SEK 673,038** (`8.07 × SEK 83,400` income base amount);
- maximum charge: **SEK 47,100**;
- charge is rounded to the nearest SEK 100, with an exact SEK 50 tie rounded down;
- no charge where pensionable income is below SEK 25,042; and
- the tax credit is 100% of the charge, but cannot exceed municipal plus state income tax.

All five worked cases have sufficient municipal/state tax for the full credit. Therefore the charge and its credit are shown separately but cancel in final net tax. This is not an additional employee social withholding left after reconciliation.

Primary pinpoint: SKV 433, pp. 14–16, sections 7.4 and 7.5.1. Skatteverket's [“Belopp och procent – inkomstår 2026”](https://www.skatteverket.se/privat/skatter/beloppochprocent/2026.4.1522bf3f19aea8075ba21.html), current 2026 page, heading “Allmän pensionsavgift,” also states 7%, maximum SEK 47,100, and 100% tax credit.

No separate employee unemployment, health, or general social-insurance percentage is deducted from ordinary salary under these assumptions. Union dues, unemployment-fund membership, and contractual insurance are not universal statutory employee charges.

Two optional 2026 tax reductions must not be mistaken for compulsory payroll contributions. Skatteverket's legal guidance, [“Skattereduktion för avgift till arbetslöshetskassa”](https://www4.skatteverket.se/rattsligvagledning/edition/2026.12/411854.html) (2026 edition, section “Skattereduktionens storlek”), says the reduction is **25% of the unemployment-fund fee paid during the calendar year**. Its guidance [“Skattereduktion för fackföreningsavgift”](https://www4.skatteverket.se/rattsligvagledning/edition/2026.9/370077.html) (2026 edition, sections “Vilka avgifter omfattas?” and “Skattereduktionens storlek”) likewise gives **25% of qualifying union membership fees**, while excluding fees for supplementary insurance. Both depend on actual voluntary membership and paid fees. With neither specified, the examples use zero for the fees and credits rather than inventing an amount.

## 5. Earned-income tax credits

### 5.1 Employment credit (`jobbskatteavdrag`)

For an employee under 66, let:

- `AI` = work income, rounded down to whole SEK 100 (equal to gross salary here);
- `GA` = rounded basic allowance; and
- `KI = 30.55%`, Stockholm municipal + regional income-tax rate, excluding burial and church fees.

The 2026 employment credit is computed with decimals and then rounded down to whole kronor:

| AI interval | Amount before whole-krona truncation |
|---|---|
| `AI ≤ 0.91 PBB` (≤ 53,872) | `(AI − GA) × KI` |
| `0.91 PBB < AI ≤ 3.24 PBB` (53,872–191,808) | `[0.91 PBB + 0.3874 × (AI − 0.91 PBB) − GA] × KI` |
| `3.24 PBB < AI ≤ 8.08 PBB` (191,808–478,336) | `[1.813 PBB + 0.251 × (AI − 3.24 PBB) − GA] × KI` |
| `AI > 8.08 PBB` (> 478,336) | `(3.027 PBB − GA) × KI` |

It can offset municipal income tax only—not state tax, burial fee, public-service fee, or the pension charge. For Stockholm and income above SEK 478,336, it saturates at:

`floor[(3.027 × 59,200 − 17,400) × 30.55%] = SEK 49,429`.

Primary pinpoint: SKV 433, pp. 16–19, section 7.5.2, especially the under-66 formula table and rounding instruction. Skatteverket, [“Jobbskatteavdrag”](https://www.skatteverket.se/jobbskatteavdrag), current 2026 guidance, confirms that the credit depends on work income and whether the person was under 66 at year start and can offset only municipal income tax. Statutory basis: Income Tax Act Chapter 67, sections 5–9.

### 5.2 General earned-income reduction (`skattereduktion för förvärvsinkomst`)

This separate credit is required for a complete annual result even though it is not the jobbskatteavdrag:

- `BFI ≤ 40,000`: zero;
- `40,000 < BFI ≤ 240,000`: `floor[0.75% × (BFI − 40,000)]`; and
- `BFI > 240,000`: SEK 1,500.

It offsets municipal income tax only and is applied after the pension and employment credits. Primary pinpoint: SKV 433, pp. 23–24, section 7.5.4.

## 6. Public-service fee

For an unlimited Swedish tax resident aged at least 18 at the start of the year:

`Public-service fee = floor[min(1% × BFI, SEK 1,184)]`.

The 2026 cap follows from `1.42 × income base amount SEK 83,400 = SEK 118,428`; 1% is SEK 1,184 after dropping fractions. Tax reductions do not offset this fee.

Primary sources:

- [Public Service Act (2025:986)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-2025986-om-public-service_sfs-2025-986/), effective for 2026, Chapter 5 sections 3–5: liable resident aged 18, taxable earned-income base capped at 1.42 income base amounts, rate 1%.
- SKV 433, dated 2025-12-10, pp. 24–25, section 7.6: SEK 118,428 base cap, SEK 1,184 maximum, and whole-krona truncation.

## 7. Statutory employer contributions

For an ordinary employee born 1960–2002, full employer contributions plus the general payroll levy total **31.42% of gross remuneration**, with no annual earnings cap:

| Component | 2026 rate |
|---|---:|
| Sickness insurance | 3.55% |
| Parental insurance | 2.00% |
| Old-age pension | 10.21% |
| Survivors' pension | 0.30% |
| Labour-market charge | 2.64% |
| Occupational-injury charge | 0.10% |
| General payroll levy | 12.62% |
| **Total** | **31.42%** |

Employer contribution is therefore `31.42% × gross`, and statutory employer cost is `gross × 1.3142`.

Skatteverket, [“Arbetsgivaravgifter”](https://www.skatteverket.se/foretag/arbetsgivare/arbetsgivaravgifterochskatteavdrag/arbetsgivaravgifter.4.233f91f71260075abe8800020817.html), current page updated for the **2026-03-30** youth-law change, says the full rate is 31.42% of gross salary and taxable benefits and provides the component table. The [Social Contributions Act (2000:980)](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/socialavgiftslag-2000980_sfs-2000-980/), issued **2000-11-23**, consolidated through 2026, Chapter 2, makes salary and other remuneration for work contribution-liable and contains the component rates; the general payroll levy is legislated separately.

### Age and other employer-rate variables

- Person who had reached age 67 at the start of 2026 (Skatteverket's birth years 1938–1958): only 10.21% old-age pension charge.
- Born 1937 or earlier: zero employer contribution.
- Born 2003–2007: for remuneration paid **2026-04-01 through 2027-09-30**, 20.81% on the first SEK 25,000 per calendar month and 31.42% above it; January–March 2026 remains at the full rate. This temporary rule means an age/birth-year input is mandatory.
- Research/R&D relief, regional support, and the employer-growth (`växa`) refund are employer/activity-specific and are not applied.

There is no general annual ceiling on the 31.42% employer charge. The worked examples therefore apply it to all gross salary.

### Collective-agreement insurance and pensions

Occupational pension, agreement insurance, and related special payroll tax can add material employer cost, but are not a universal percentage. The official business portal [verksamt.se, “Försäkringskostnader för arbetsgivare”](https://verksamt.se/personal-rekrytering/vad-kostar-det/forsakringskostnader-for-arbetsgivare) (“Insurance costs for employers”), current page with no visible revision date, states that an employer not bound by a collective or adhesion agreement is not obliged to take agreement insurance and may insure voluntarily. Rates depend on agreement, sector, pension plan, age, and compensation. They are therefore **unresolved variables and excluded**, not assumed to be zero universally.

## 8. Calculation formula and rounding used

For each gross salary `G`:

1. `FFI = floor_to_100(G)`; all requested salaries are already multiples of SEK 100.
2. Calculate `GA` from section 2 and round it upward to SEK 100.
3. `BFI = FFI − GA`.
4. `K = floor(BFI × 30.55%)` municipal/regional tax.
5. `B = floor(BFI × 0.070%)` burial fee.
6. `S = floor[20% × max(BFI − 643,000, 0)]` state income tax.
7. Calculate the pension charge `AP` at 7% subject to its ceiling and SEK-100 rounding; `AP_credit = AP` in all examples.
8. Calculate and floor the jobbskatteavdrag `J` using section 5.1.
9. Calculate the general earned-income reduction `F` using section 5.2.
10. `PS = floor[min(1% × BFI, 1,184)]`.
11. `Final tax = K + B + S + AP + PS − AP_credit − J − F`.
12. `Employee net = G − final tax`.

Credits cannot reduce the burial or public-service fees. All examples have sufficient municipal income tax to use `J` and `F`, and sufficient municipal + state income tax to use the full pension credit.

## 9. Independent worked calculations

### 9.1 Employee annual tax and net salary

| Gross G | Basic allowance GA | Taxable income BFI | Municipal tax K | State tax S | Burial B | Pension charge / credit | Job credit J | Other earned credit F | Public service PS | Final tax | Net salary |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 200,000 | 44,000 | 156,000 | 47,658 | 0 | 109 | 14,000 / −14,000 | −19,975 | −870 | 1,184 | **28,106** | **171,894** |
| 600,000 | 17,400 | 582,600 | 177,984 | 0 | 407 | 42,000 / −42,000 | −49,429 | −1,500 | 1,184 | **128,646** | **471,354** |
| 1,000,000 | 17,400 | 982,600 | 300,184 | 67,920 | 687 | 47,100 / −47,100 | −49,429 | −1,500 | 1,184 | **319,046** | **680,954** |
| 2,000,000 | 17,400 | 1,982,600 | 605,684 | 267,920 | 1,387 | 47,100 / −47,100 | −49,429 | −1,500 | 1,184 | **825,246** | **1,174,754** |
| 6,000,000 | 17,400 | 5,982,600 | 1,827,684 | 1,067,920 | 4,187 | 47,100 / −47,100 | −49,429 | −1,500 | 1,184 | **2,850,046** | **3,149,954** |

Intermediate checks:

- At SEK 200,000, raw GA is `45,584 − 10% × (200,000 − 184,112) = 43,995.20`, rounded up to 44,000. Job-credit quantity is `107,329.60 + 25.1% × (200,000 − 191,808) − 44,000 = 65,385.792`; multiplying by 30.55% and dropping fractions gives 19,975.
- At SEK 600,000 and above, GA is `ceil100(0.293 × 59,200) = 17,400`; the saturated job-credit quantity is `3.027 × 59,200 − 17,400 = 161,798.40`, giving `floor(161,798.40 × 30.55%) = 49,429`.
- At SEK 1,000,000, state tax is `20% × (982,600 − 643,000) = 67,920`.
- At SEK 6,000,000, municipal tax is `floor(5,982,600 × 30.55%) = 1,827,684`, state tax is 1,067,920, burial fee is 4,187, and public service remains capped at 1,184.

### 9.2 Statutory employer cost (born 1960–2002)

| Gross salary | Employer charge 31.42% | Statutory employer cost |
|---:|---:|---:|
| 200,000 | 62,840 | **262,840** |
| 600,000 | 188,520 | **788,520** |
| 1,000,000 | 314,200 | **1,314,200** |
| 2,000,000 | 628,400 | **2,628,400** |
| 6,000,000 | 1,885,200 | **7,885,200** |

Collective pension/insurance, holiday-pay timing, employer-specific reliefs, and benefits are excluded.

## 10. Universal rules versus variables

Universal within the stated employee profile:

- 2026 PBB SEK 59,200 and ordinary under-66 basic-allowance formula;
- 20% state tax above SEK 643,000 taxable earned income;
- 7% general pension charge, SEK 673,038 base ceiling/SEK 47,100 charge ceiling, and matching credit where tax capacity permits;
- under-66 jobbskatteavdrag formula and separate earned-income reduction;
- public-service formula and SEK 1,184 cap; and
- 31.42% employer rate for the selected 1960–2002 birth cohort without employer-specific relief.

Variables:

- municipality/region and burial fee (Stockholm was selected here);
- church or other registered-community membership;
- voluntary trade-union and unemployment-fund membership and the actual fees paid;
- exact birth year, including the 2026 youth reduction and older-worker rate;
- non-salary income, deductions, benefits, multiple payers, and residence duration;
- tax-credit limitation where income tax is insufficient;
- collective-agreement pension and insurance; and
- R&D, regional, `växa`, and international social-security exceptions.

## 11. Evidence quality and unresolved points

### Strongest evidence

The strongest source is Skatteverket's dated SKV 433 edition 36. It gives the complete 2026 basic-allowance, jobbskatteavdrag, pension-charge, state-tax, other-credit, public-service, and rounding rules in one official technical specification. SKVFS 2025:20 makes the corresponding tables effective for 2026. The exact Stockholm rates come directly from Skatteverket's machine-readable 2026 municipality dataset. The Riksdag's consolidated Income Tax, Public Service, and Social Contributions Acts corroborate the legal structure.

### Weakest evidence / deliberately unresolved

- Final annual tax is calculated from the exact Stockholm rates and published annual formulas. Actual monthly table-31 withholding can differ temporarily because tables use pay intervals, annualization, and preliminary-tax rounding; the annual assessment reconciles it.
- The official municipality text dataset exposes no publication/revision timestamp. Its tax-year label and download placement are authoritative, but a more precise publication date is unavailable in the file.
- Collective pension and agreement-insurance cost cannot be stated without employer sector, agreement, plan, and employee age. No value is guessed.
- “Under 66” does not by itself select one employer-contribution rate because of the temporary youth reduction. The worked cost explicitly adds the birth-year assumption 1960–2002.
- Component-level whole-krona truncation follows SKV 433's stated method. A production annual assessment can differ by a few kronor if Skatteverket applies a different aggregation order to facts outside these simplified assumptions.
