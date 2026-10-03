# Switzerland — employee payroll and income tax, tax year 2026

**Research status:** clean-room reconstruction from Swiss public authorities and legislation. **Access date for every web source: 2026-10-04.** This dossier does not use calculator code, generated data, another country model, or an earlier dossier.

## 1. Scope and reproducible fact pattern

The model is an individual who throughout 2026:

- is resident in **the City of Zürich, Canton Zürich** and subject to ordinary assessment;
- is single, has no children or dependants, and belongs to no recognised church;
- has no income or wealth other than regular annual cash employment salary `G`;
- works for an ordinary private-sector Swiss employer, is below AHV reference age, and works at least eight hours per week;
- is age **35–44** for the worked occupational-pension illustration (age cannot be inferred from salary);
- claims no pillar 3a contribution, commuting, meal, training, debt-interest, donation, or other fact-dependent deduction; and
- has enough actual Swiss health/accident/life-insurance premiums to use the applicable capped insurance deduction.

Income tax is annual. For an ordinarily assessed employee it is not generally a payroll deduction, so “cash after payroll deductions” and “cash after annual income tax” are intentionally separate.

## 2. What is universal and what is not

### Statutory fixed components

| Item | 2026 employee | 2026 employer | Base / limit |
|---|---:|---:|---|
| AHV | 4.35% | 4.35% | uncapped AHV salary |
| IV | 0.70% | 0.70% | uncapped AHV salary |
| EO | 0.25% | 0.25% | uncapped AHV salary |
| **AHV/IV/EO total** | **5.30%** | **5.30%** | uncapped |
| ALV | 1.10% | 1.10% | only to CHF 148,200/year (CHF 12,350/month) |

Thus each side's fixed social contribution is

```text
S(G) = 0.053 G + 0.011 min(G, 148,200).
```

The AHV/IV Information Centre's **“2.01 Lohnbeiträge an die AHV, die IV und die EO”**, version/effective 1 January 2026, §6, gives 8.7% AHV, 1.4% IV and 0.5% EO (10.6% total), half deducted from the employee and half borne by the employer: [official leaflet](https://www.ahv-iv.ch/p/2.01.d). Its **“2.08 Beiträge an die Arbeitslosenversicherung”**, version/effective 1 January 2026, §§3–5, gives 2.2% through CHF 148,200, shared equally, and confirms that the former solidarity percentage above the ceiling ceased on 1 January 2023: [official leaflet](https://www.ahv-iv.ch/p/2.08.d). SVA Zürich's **“AHV-Beitragspflicht”**, 2026 table “Wer bezahlt welche Beiträge?”, independently pinpoints 5.3% each and ALV 1.1% each to CHF 12,350/month or CHF 148,200/year: [SVA Zürich](https://svazurich.ch/beitragspflicht).

Regular salary, premiums and overtime are part of AHV “massgebender Lohn” (same SVA page, section “Massgebender Lohn”). The CHF 2,500 de-minimis rule on that page is immaterial at the five salaries here.

### Components that salary alone cannot determine

1. **Occupational pension (BVG/LPP).** Mandatory insurance begins at annual pay CHF 22,680; the compulsory insured range ends at CHF 90,720; the coordination deduction is CHF 26,460 and the minimum coordinated salary is CHF 3,780. Retirement saving starts from 1 January after age 24; ages 18–24 have risk cover only. The official 2025/2026 thresholds are in **“Sozialversicherungen 2025/2026”**, table “Berufliche Vorsorge”: [AHV/IV Information Centre](https://www.ahv-iv.ch/p/1.2025.d). The Federal Social Insurance Office (BSV), **“Die Altersvorsorge in der beruflichen Vorsorge”**, updated/published 5 January 2026, says the employer's total contributions must be at least the employees' total but the pension fund rules determine financing: [BSV](https://www.bsv.admin.ch/de/altersvorsorge-beruflichen-vorsorge). Statutory retirement credits on coordinated salary are 7% (25–34), 10% (35–44), 15% (45–54), and 18% (55–65). These are old-age credits, **not** a complete payroll premium: disability/death risk and administration, extra-mandatory coverage, actual age, and the plan split remain unknown.
2. **Accident insurance.** The employer bears occupational-accident insurance (BU). If an employee works at least eight hours weekly, non-occupational accident insurance (NBU) is compulsory and normally borne by the employee, although the employer may pay it. Both are limited to CHF 148,200 insured pay. Rates depend on insurer, industry and risk class. See BSV, **“Ratgeber Sozialversicherung für KMU”**, 2025 edition, chapter 8 “Unfallversicherung”: [official PDF](https://www.bsv.admin.ch/dam/bsv/de/dokumente/themenuebergreifend/broschueren/kmu-ratgeber.pdf.download.pdf/d_kmu_2025.pdf), and Suva, **“Prämienbemessung Berufsunfall und Nichtberufsunfall”** (2026 tariff methodology): [Suva](https://www.suva.ch/de-ch/versicherung/loehne-und-praemien/praemienbemessung-berufsunfall-nicht-berufsunfall).
3. **Family-compensation fund (FAK).** It is employer-only in Zürich but varies by the fund. SVA Zürich's own 2026 rate is 1.025% (SVA page above, table rows “Familienzulagen”); that is a reproducible scenario, not a canton-wide universal rate.
4. **AHV administration charge.** Employer-only and compensation-fund/employer-size dependent. The SVA Zürich **“Verwaltungskostenbeiträge ab 2026”** tariff sets rates as a percentage of employer-wide AHV/IV/EO contributions, declining with the annual contribution total, so one employee's salary cannot select a rate: [official tariff PDF](https://svazurich.ch/content/dam/sva-dokumente/2000_ak/2800_vb/2800_vb1_verwaltungskostenbeitraege_ab_2026.pdf).
5. **Zürich vocational-training fund.** The current levy is 0.1% of declared Zürich payroll, but exemptions include employers training apprentices, employers subject to an industry fund and payrolls below CHF 250,000. This depends on the whole employer, not this employee: Canton Zürich, **“Berufsbildungsfonds”**, section “Beitragspflicht und Befreiung”: [official page](https://www.zh.ch/de/bildung/berufslehre/berufsbildungsfonds.html).
6. **Daily sickness allowance and employer health benefits.** These are contractual/voluntary, not a universal statutory percentage. Mandatory personal health insurance is paid by the resident outside payroll.

BSV itself warns that it cannot state generally applicable current rates for occupational pension, FAK, BU or NBU: **“Beiträge im Überblick”**, table notes: [BSV](https://www.bsv.admin.ch/de/beitraege-im-ueberblick). Accordingly, an “exact Swiss employer cost” derived only from gross salary is not a defensible output.

## 3. Occupational-pension illustration used below

This is a transparent **minimum-retirement-credit illustration**, not a prediction of a payslip. For the assumed age 35–44:

```text
C(G) = 0,                                             if G < 22,680
     = max(3,780, min(G, 90,720) - 26,460),           otherwise

total statutory old-age credit = 10% C(G)
illustrative employee share P_e = 5% C(G)
illustrative employer share P_r = 5% C(G).
```

The equal split is an explicit scenario. The legal constraint is only that the employer's aggregate contribution is at least the aggregate employee contribution. Add unknown employee pension risk/administration/extra-mandatory premium `R_e` and employer counterpart `R_r` for an actual plan.

## 4. Ordinary income tax

### 4.1 Deductions and tax bases

Let employee NBU premium be `N = n × min(G, 148,200)` and employee additional pension premium be `R_e`. Wage-certificate net salary is modelled as:

```text
W = G - S(G) - P_e - R_e - N.
```

For both Zürich and federal tax, the flat “other professional costs” deduction is 3% of net salary, minimum CHF 2,000 and maximum CHF 4,000. The 2026 Zürich guide, **“Wegleitung zur Steuererklärung 2026 – unterjährig”**, section “Übrige Berufskosten”, gives exactly 3% / CHF 2,000 / CHF 4,000; the same guide gives commuting caps (Zürich CHF 5,200, federal CHF 3,300) and meal deductions, all assumed zero here: [official 2026 guide](https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/steuern-finanzen/steuern/natuerlichepersonen/2026/est-wegleitungen-uj/305%20Wegleitung%20ZH%202026%20UJ%20bf.pdf).

The guide's section “Versicherungsprämien, Zinsen von Sparkapitalien” gives, for a single person with pillar-2/3a contributions, maxima CHF 2,900 Zürich and CHF 1,800 federal. If neither taxpayer nor employer contributes to pillar 2/3a, each rises by half: CHF 4,350 and CHF 2,700. Therefore the CHF 20,000 case (below mandatory BVG and no voluntary plan assumed) uses the larger figures; all others use CHF 2,900/1,800.

With zero fact-dependent expenses:

```text
Dprof = min(4,000, max(2,000, 0.03 W))
T_ZH  = floor_to_CHF100(max(0, W - Dprof - I_ZH))
T_CH  = floor_to_CHF100(max(0, W - Dprof - I_CH)).
```

No child, dependant, or spouse social deduction applies. The official **“Steuererklärung 2026”**, lines/boxes 220–398, shows this calculation sequence and the available social deductions: [Canton Zürich form](https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/steuern-finanzen/steuern/natuerlichepersonen/2026/est-formulare-uj/300%20STE%20ZH%202026.pdf).

### 4.2 Federal direct tax, single-person tariff

Apply `T_CH` after discarding fractions below CHF 100. Federal Act on Direct Federal Tax (DBG), **Art. 36(1), version in force 1 January 2026**, gives the following anchor tax and amount for each further CHF 100: 0 through 15,200; then CHF 0.77 to 33,200 (tax 138.60); 0.88 to 43,500 (229.20); 2.64 to 58,000 (612.00); 2.97 to 76,200 (1,152.50); 5.94 to 82,100 (1,502.95); 6.60 to 108,900 (3,271.75); 8.80 to 141,500 (6,140.55); 11.00 to 185,100 (10,936.55); 13.20 to 793,900 (91,298.15); at 794,000 tax is 91,310.00 and each further CHF 100 costs 11.50. Art. 36(3) says amounts below CHF 25 are not collected: [Fedlex DBG Art. 36](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de?version=20261231). The matching ESTV **Form 58c—2026**, dated January 2026, footnotes that sub-CHF-100 income is ignored and annual tax is rounded down to the next CHF 0.05: [ESTV official table](https://www.estv.admin.ch/dam/de/sd-web/gnde9CmEsalK/dbst-tairfe-58c-2026-dfi.pdf).

### 4.3 Zürich state and City tax

The Canton Zürich **“Verordnung über den Ausgleich der kalten Progression ab 1. Januar 2026”**, issued 24 October 2025 and effective 1 January 2026, §35(1), gives the single/basic simple-tax bands:

| Taxable slice (CHF) | Rate |
|---:|---:|
| 0–7,000 | 0% |
| next 5,000 | 2% |
| next 4,800 | 3% |
| next 8,000 | 4% |
| next 9,700 | 5% |
| next 11,200 | 6% |
| next 13,100 | 7% |
| next 17,600 | 8% |
| next 34,000 | 9% |
| next 33,700 | 10% |
| next 53,300 | 11% |
| next 69,300 | 12% |
| above 266,700 | 13% |

Source: [official regulation PDF](https://www.notes.zh.ch/appl/zhlex_r.nsf/WebView/46D70B70E90D0F52C1258D110033A244/%24File/631.1.pdf). Canton Zürich's **ZStB 34.1, “Weisung … Sozialabzüge und Steuertarife (ab Steuerperiode 2026)”**, issued 17 March 2026, valid for tax period 2026, para. 56 confirms that a single person without children uses the basic tariff: [official guidance](https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-34-1.html).

For City of Zürich in 2026, state multiplier is 95% and municipal multiplier 119%; no-church means no church multiplier. City Zürich, **“Steuerberechnung und Steuerfuss”**, table “Steuerfuss Steuerperiode 2026”: [official city page](https://www.stadt-zuerich.ch/de/lebenslagen/steuern/natuerliche-personen/steuerberechnung.html). Hence:

```text
ZH state + city income tax = simple_tax(T_ZH) × (0.95 + 1.19)
                           = simple_tax(T_ZH) × 2.14.
```

Add the Canton Zürich personal tax of CHF 24 for every adult liable for state tax: Zürich Tax Book **ZStB 173.1, “Personalsteuer”**, §200: [official guidance](https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-173-1.html). Assessment-level rounding can differ by cents; the worked figures retain mathematical cents.

## 5. Worked calculations

### 5.1 Critical limitation and benchmark convention

An actual result requires `n`, `R_e`, the actual pension plan and its split. The following is an auditable **fixed-core / zero-variable-premium benchmark**:

- age 35–44 and the equal-split minimum old-age credit in §3;
- `N = 0` and `R_e = 0` only to isolate the known statutory core.

Because the stated employee works at least eight hours weekly, `N=0` is **not an asserted real payslip**. The displayed taxable income and income tax are upper benchmarks; the displayed employee cash is also an upper benchmark. For an actual contract, subtract `N + R_e` from `W`, recalculate `Dprof` and both tax bases, then apply the tariffs.

### 5.2 Employee and tax calculation

| Gross `G` | AHV/IV/EO 5.3% | ALV 1.1% capped | Coordinated `C` | Illustrative employee BVG 5% `C` | `W` before income tax | Professional flat | Zürich taxable | Simple ZH tax | ZH ×2.14 + CHF24 | Federal taxable | Federal tax | Cash after benchmark tax |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 1,060.00 | 220.00 | 0 | 0.00 | 18,720.00 | 2,000.00 | 12,300 | 109.00 | 257.26 | 14,000 | 0.00 | 18,462.74 |
| 60,000 | 3,180.00 | 660.00 | 33,540 | 1,677.00 | 54,483.00 | 2,000.00 | 49,500 | 1,987.00 | 4,276.18 | 50,600 | 416.64 | 49,790.18 |
| 100,000 | 5,300.00 | 1,100.00 | 64,260 | 3,213.00 | 90,387.00 | 2,711.61 | 84,700 | 4,793.00 | 10,281.02 | 85,800 | 1,747.15 | 78,358.83 |
| 200,000 | 10,600.00 | 1,630.20 | 64,260 | 3,213.00 | 184,556.80 | 4,000.00 | 177,600 | 14,161.00 | 30,328.54 | 178,700 | 10,232.55 | 143,995.71 |
| 600,000 | 31,800.00 | 1,630.20 | 64,260 | 3,213.00 | 563,356.80 | 4,000.00 | 556,400 | 62,316.00 | 133,380.24 | 557,500 | 60,093.35 | 369,883.21 |

Checks on representative rows:

```text
G=100,000:
S = 5,300 + 1,100 = 6,400
C = 90,720 - 26,460 = 64,260; P_e = 3,213
W = 100,000 - 6,400 - 3,213 = 90,387
Dprof = 3% × 90,387 = 2,711.61
T_ZH = floor100(90,387 - 2,711.61 - 2,900) = 84,700
T_CH = floor100(90,387 - 2,711.61 - 1,800) = 85,800
Federal = 1,502.95 + 37 × 6.60 = 1,747.15

G=600,000:
ALV stops at 148,200; BVG compulsory coordinated salary stops at 64,260
T_ZH = floor100(563,356.80 - 4,000 - 2,900) = 556,400
simple ZH tax = 62,316; actual state+city+personal = 62,316×2.14+24
Federal = 10,936.55 + 3,724 × 13.20 = 60,093.35.
```

At CHF 20,000 the insurance deductions are CHF 4,350 Zürich / CHF 2,700 federal because no pillar-2 or 3a contribution exists. At the other four salaries they are CHF 2,900 / CHF 1,800.

### 5.3 Employer-cost calculation

For a concrete but limited scenario, assume the employer belongs to **SVA Zürich's** FAK (1.025%) and uses the equal-split BVG old-age credit. The identifiable subtotal is:

```text
Employer core = G + 0.053G + 0.011min(G,148,200) + 0.01025G + P_r.

Actual employer cost = Employer core
                     + BU premium b×min(G,148,200)
                     + pension risk/admin/extra-mandatory R_r
                     + AHV administration charge A
                     + vocational-fund levy V (if not exempt)
                     + any voluntary sickness/benefit costs.
```

| Gross | Employer AHV/IV/EO | Employer ALV | SVA-ZH FAK scenario | Employer BVG old-age illustration | Identifiable employer core | Unresolved additions |
|---:|---:|---:|---:|---:|---:|---|
| 20,000 | 1,060.00 | 220.00 | 205.00 | 0.00 | 21,485.00 | `BU + A + V`; any voluntary benefits |
| 60,000 | 3,180.00 | 660.00 | 615.00 | 1,677.00 | 66,132.00 | `BU + R_r + A + V`; voluntary benefits |
| 100,000 | 5,300.00 | 1,100.00 | 1,025.00 | 3,213.00 | 110,638.00 | same variables |
| 200,000 | 10,600.00 | 1,630.20 | 2,050.00 | 3,213.00 | 217,493.20 | same variables |
| 600,000 | 31,800.00 | 1,630.20 | 6,150.00 | 3,213.00 | 642,793.20 | same variables |

This is not a purported lower bound for every legal arrangement: a different FAK rate or plan structure can move an item downward as well as upward. It is a reproducible subtotal under the stated SVA-Zürich and BVG illustration.

## 6. Source tax versus ordinary assessment

Nationality/permit status was not specified, so the worked tax intentionally assumes ordinary assessment. Canton Zürich's **“Quellensteuerpflichtige Personen”** states:

- a Zürich-resident employee without Swiss citizenship or permit C is normally taxed at source by the employer (page lines 93–123);
- a Swiss citizen or permit-C resident is ordinarily assessed;
- a source-taxed resident with at least CHF 120,000 annual gross employment income undergoes mandatory subsequent ordinary assessment; other triggers include at least CHF 3,000 non-source-taxed income or specified wealth (lines 156–168);
- a resident below the threshold may request subsequent ordinary assessment by 31 March of the following year to claim deductions, and once requested it continues annually (lines 169–176); and
- source tax already paid is credited without interest against final federal/cantonal/municipal/church taxes (lines 156–160).

Source: [Canton Zürich official page](https://www.zh.ch/de/steuern-finanzen/steuern/quellensteuer/Quellensteuerpflichtige-Personen.html), including its 2026 information sheet effective for payments from 1 January 2026. Source withholding uses monthly tariff tables and cannot be substituted by simply dividing this annual ordinary-assessment result by twelve.

## 7. Calculation order and rounding

1. Determine each pay-period AHV salary and contribution bases; payroll systems normally round contribution lines per period. An annual gross alone cannot reproduce cent-perfect monthly payroll if pay varies.
2. Deduct 5.3% AHV/IV/EO and 1.1% ALV through the annual/monthly ceiling.
3. Deduct the actual pension-plan employee premium and actual NBU premium. Do not replace either with the illustrative figures without showing the assumption.
4. For an ordinary annual tax return, start from wage-certificate net salary, claim the professional and insurance deductions, and round each taxable income down to CHF 100 as the tariff instructs.
5. Calculate Zürich simple tax, multiply by 95% state plus 119% city, add CHF 24 personal tax, and add federal tax. ESTV Form 58c specifies federal rounding down to CHF 0.05 and no tax below CHF 25.

The authorities do not publish one national rule that guarantees identical intermediate payroll rounding by every pension/accident provider. A production implementation needs explicit per-period rounding tests against the selected payroll/provider specifications.

## 8. Material edge cases and exclusions

- **Age:** under 25 has no statutory retirement saving; other age bands change the credit from the 10% illustration. Reference-age employees have different ALV/AHV rules.
- **Multiple jobs / short employment:** BVG entry threshold, coordination and ALV ceiling application can differ; annual gross cannot resolve them.
- **Weekly hours:** at no more than eight hours for one employer, NBU coverage does not arise through that employer; occupational accident still does.
- **Pension plan:** plans commonly insure salary above the BVG minimum and may use another coordination method or contribution split.
- **Other income/wealth, home ownership and assets:** Zürich also has wealth tax; none is modelled. Personal health-insurance premiums affect the capped deduction but are not salary withholding.
- **Benefits, bonus timing and expenses:** taxable salary and contribution bases may differ from simple cash gross; reimbursed genuine business expenses require documentation.
- **Minimum wages:** Switzerland has no universal federal salary minimum; sectoral collective agreements or cantonal rules may make a fact pattern employment-specific.
- **Family allowance:** no benefit is included because the worker has no child, but the employer FAK contribution still applies.
- **Church:** membership would add the church multiplier. Another municipality changes the 119% multiplier.

## 9. Source-date ledger

All links were accessed 2026-10-04. Where a live authority page displays no publication date, that absence is recorded rather than inferred.

| Authority and title | Publication/status date | Effective/relevant period | Exact support used |
|---|---|---|---|
| AHV/IV Information Centre, [“2.01 Lohnbeiträge an die AHV, die IV und die EO”](https://www.ahv-iv.ch/p/2.01.d) | version “Stand 1. Januar 2026” | 2026 | §6 contribution rates and equal split; salary elements |
| AHV/IV Information Centre, [“2.08 Beiträge an die Arbeitslosenversicherung”](https://www.ahv-iv.ch/p/2.08.d) | version “Stand 1. Januar 2026” | 2026 | §§3–5, 2.2%, CHF 148,200 and equal split |
| SVA Zürich, [“AHV-Beitragspflicht”](https://svazurich.ch/beitragspflicht) | live page; publication date not displayed | table current in 2026 | 5.3%, 1.1%, CHF 12,350/148,200, FAK 1.025%, administration variability |
| AHV/IV Information Centre, [“Sozialversicherungen 2025/2026”](https://www.ahv-iv.ch/p/1.2025.d) | official 2025/2026 edition | 2025–2026 | BVG 22,680 / 26,460 / 3,780 / 90,720 and age credits |
| BSV, [“Die Altersvorsorge in der beruflichen Vorsorge”](https://www.bsv.admin.ch/de/altersvorsorge-beruflichen-vorsorge) | published/updated 2026-01-05 | current 2026 | entry/age rules and employer aggregate at least employee aggregate |
| BSV, [“Ratgeber Sozialversicherung für KMU”](https://www.bsv.admin.ch/dam/bsv/de/dokumente/themenuebergreifend/broschueren/kmu-ratgeber.pdf.download.pdf/d_kmu_2025.pdf) | 2025 edition | current background for 2026 | chapter 8 BU/NBU payer, eight-hour rule and insured-pay ceiling |
| Suva, [“Prämienbemessung Berufsunfall und Nichtberufsunfall”](https://www.suva.ch/de-ch/versicherung/loehne-und-praemien/praemienbemessung-berufsunfall-nicht-berufsunfall) | live page; publication date not displayed | 2026 tariff method | risk-class rather than universal accident rate |
| SVA Zürich, [“Verwaltungskostenbeiträge ab 2026”](https://svazurich.ch/content/dam/sva-dokumente/2000_ak/2800_vb/2800_vb1_verwaltungskostenbeitraege_ab_2026.pdf) | 2026 tariff | from 2026 | employer-wide contribution bands |
| Canton Zürich, [“Berufsbildungsfonds”](https://www.zh.ch/de/bildung/berufslehre/berufsbildungsfonds.html) | live page; publication date not displayed | current 2026 | 0.1% and listed exemptions |
| BSV, [“Beiträge im Überblick”](https://www.bsv.admin.ch/de/beitraege-im-ueberblick) | live page; publication date not displayed | current 2026 | no generally valid BVG/FAK/BU/NBU rates |
| Canton Zürich, [“Wegleitung zur Steuererklärung 2026 – unterjährig”](https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/steuern-finanzen/steuern/natuerlichepersonen/2026/est-wegleitungen-uj/305%20Wegleitung%20ZH%202026%20UJ%20bf.pdf) and [“Steuererklärung 2026”](https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/steuern-finanzen/steuern/natuerlichepersonen/2026/est-formulare-uj/300%20STE%20ZH%202026.pdf) | 2026 editions | tax period 2026 | professional/insurance deductions and return calculation sequence |
| Fedlex, [DBG Art. 36](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de?version=20261231) | consolidated status 2026-09-02; tariff amendment AS 2025 579/621 | tariff from 2026-01-01 | every federal anchor/rate and CHF 25 collection floor |
| ESTV, [“Form. 58c – 2026”](https://www.estv.admin.ch/dam/de/sd-web/gnde9CmEsalK/dbst-tairfe-58c-2026-dfi.pdf) | 2026-01 | tax period 2026 | tariff table; CHF 100 and CHF 0.05 rounding |
| Canton Zürich, [cold-progression regulation](https://www.notes.zh.ch/appl/zhlex_r.nsf/WebView/46D70B70E90D0F52C1258D110033A244/%24File/631.1.pdf) | issued 2025-10-24 | from 2026-01-01 | §35 basic tariff bands |
| Canton Zürich, [ZStB 34.1](https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-34-1.html) | issued 2026-03-17 | tax period 2026 | para. 56 basic tariff for single/no-child taxpayer |
| City Zürich, [“Steuerberechnung und Steuerfuss”](https://www.stadt-zuerich.ch/de/lebenslagen/steuern/natuerliche-personen/steuerberechnung.html) | live page; publication date not displayed | tax period 2026 | 95% state and 119% city multipliers; church multipliers |
| Canton Zürich, [ZStB 173.1 “Personalsteuer”](https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-173-1.html) | live tax-book entry; publication date not displayed | current 2026 | §200, CHF 24 personal tax |
| Canton Zürich, [“Quellensteuerpflichtige Personen”](https://www.zh.ch/de/steuern-finanzen/steuern/quellensteuer/Quellensteuerpflichtige-Personen.html) | live page; linked sheet valid for payments from 2026-01-01 | 2026 | permit test, CHF 120,000 NOV threshold, other triggers and deadline |

## 10. Evidence assessment and unresolved facts

**Strongest evidence:** the effective-2026 Fedlex Art. 36 federal tariff; ESTV Form 58c; Zürich's effective-2026 cold-progression regulation and official 95%/119% multipliers; and the AHV/IV Information Centre/SVA tables for the 5.3% and capped 1.1% contributions. These directly state the values used.

**Weakest evidence / deliberately unresolved:** no official source can infer a private employer's pension risk and extra-mandatory premium, NBU/BU risk-class rates, compensation-fund administration rate, or vocational-fund exemption from salary alone. The old-age-credit split is an openly labelled scenario, not a statutory employee rate. Consequently the five “cash after tax” figures are zero-variable-premium benchmarks and the employer figures are identifiable core subtotals, not exact quotes. An exact result requires the pension regulations, accident-insurance policy/risk class, compensation-fund affiliation and employer-wide payroll/contribution totals.
