# Belgium employee salary/payroll — income year 2026

**Independent research dossier — accessed 2026-10-04.** This note was reconstructed from Belgian public authorities, the National Labour Council and legislation-facing administrative instructions. It deliberately does not rely on the repository's existing Belgian calculator, generated data, earlier Belgian notes, or any prior audit.

## Scope and conclusion

The target person is a Belgian-resident, individually assessed, single employee with no children or other dependants, working under an ordinary private-profit-sector white-collar contract for the full year. There are no benefits in kind, pension deductions, actual professional expenses, overtime, bonuses, stock compensation or foreign income.

Belgium does not have one fully determined “2026 salary formula” from annual gross alone. Three facts prevent that:

1. municipal surcharge depends on the employee's municipality and is set by assessment year;
2. the employee work bonus and the special social-security contribution are payroll-period calculations, so payment timing and full-time-equivalent wage matter; and
3. sector/company facts determine salary indexation, year-end pay, several special employer levies, and the new 2026 wage-moderation charge.

The worked cases therefore use a disclosed benchmark package: annual cash gross includes twelve normal monthly salaries plus statutory double holiday pay of 92% of one monthly salary (`G = 12.92 × M`), with no sectoral thirteenth month. A **7.00% municipal surcharge is only a scenario assumption**, not a national rate. Results are annual assessment estimates, not monthly withholding tables.

## 1. Universal federal personal-income-tax rules

### 1.1 Income year 2026 / assessment year 2027 brackets

FPS Finance, **“Tax rates”**, currently publishes both the income-year 2025 and 2026 columns. For income year 2026 (assessment year 2027), the exact federal brackets are:

| Portion of net taxable income | Rate |
|---:|---:|
| EUR 0–16,720 | 25% |
| EUR 16,720–29,510 | 40% |
| EUR 29,510–51,070 | 45% |
| Above EUR 51,070 | 50% |

The same page gives a basic personal tax allowance of **EUR 11,180** for income year 2026. For this dossier's facts it produces a tax reduction of `11,180 × 25% = EUR 2,795`. The page itself illustrates the method: calculate bracket tax, calculate tax on the allowance, then subtract it.

Source: FPS Finance, [Tax rates](https://fin.belgium.be/en/private-individuals/tax-return/tax-rates-income/tax-rates), table “Income tax year 2026 (assessment year 2027)” and section “Personal tax allowance”; values visible by 2026-10-04. No separate publication date is shown on the page.

Federal tax before other credits is therefore:

```text
B(T) = 25% × min(T, 16,720)
     + 40% × min(max(T - 16,720, 0), 12,790)
     + 45% × min(max(T - 29,510, 0), 21,560)
     + 50% × max(T - 51,070, 0)

federal PIT before other credits = max(0, B(T) - 2,795)
```

### 1.2 Taxable employment income and professional expenses

The federal overview says professional income is taxed net: gross salary less social contributions and actual or fixed-rate professional costs; if no actual expenses are claimed, the legal fixed-rate allowance is automatic. Source: Belgium.be, [Income tax](https://www.belgium.be/en/taxes/income_tax), sections “Social contributions” and “Professional expenses” (accessed 2026-10-04; no date displayed).

For 2025 income, the latest filed-return instructions prove the employee formula is **30% of taxable gross remuneration after personal social contributions**, capped at EUR 5,930. Source: FPS Finance, [Toelichting aangifte 2026 — Deel 1 — Vlaams Gewest](https://fin.belgium.be/sites/default/files/media/documents/toelichting-deel-1-vg-2026.pdf), assessment year 2026 (income 2025), p. 36, heading “19. Andere beroepskosten”; published in 2026.

For 2026 payroll withholding, FPS Finance's official page links **“Sleutelformule vanaf 1 januari 2026”** and “Regels 1 januari 2026,” effective 2026-01-01. The 2026 key formula fixes the employee maximum at **EUR 6,070**. Direct official document link: [FPS Finance MyMinfin — 2026 key formula](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/compare/da14799a-a9fa-420e-9b75-2004a59d4ce3/821b117c-eebc-497a-8297-ed2bb1e99d75/821b117c-eebc-497a-8297-ed2bb1e99d75); index page: [Bedrijfsvoorheffing berekenen](https://financien.belgium.be/nl/ondernemingen/personeel_en_loon/bedrijfsvoorheffing/berekening). The linked MyMinfin document is script-rendered and did not expose searchable text during this research. Thus **EUR 6,070 is strong payroll-formula evidence but not yet corroborated by the assessment-year-2027 return instructions**, which will only be filed in 2027. This is the dossier's main income-tax evidence limitation.

Benchmark formula:

```text
taxable remuneration before expenses = G - deductible employee social contributions
professional-expense allowance E = min(30% × that amount, EUR 6,070)
T = taxable remuneration before expenses - E
```

### 1.3 Fiscal work-bonus credit

FPS Finance's latest return instructions distinguish social work-bonus amounts qualifying for tax credits of **33.14%** and **52.54%**, reported respectively under salary-sheet codes 284 and 360. Source: FPS Finance, [Explications déclaration 2026 — Partie 1 — Région de Bruxelles-Capitale](https://fin.belgium.be/sites/default/files/media/documents/explications-partie-1-bxl-2026.pdf), p. 44, heading “K. Bonus à l'emploi”; assessment year 2026 / income 2025, published 2026.

The split continues in the 2026 social work-bonus scheme (component A and component B; section 2.2 below). However, the assessment-year-2027 filing instructions were not available on 2026-10-04. The worked EUR 20,000 case therefore displays the mechanically inferred credit but does not silently treat it as fully verified assessment law.

### 1.4 Municipal surcharge

Municipal surcharge is not a federal flat rate. FPS Finance publishes a municipality-by-municipality table. For example, the **assessment-year 2026** table lists Brussels at 4.9%, Antwerp at 7.0%, and many municipalities at different rates. Source: FPS Finance, [Municipal tax rate — assessment year 2026](https://fin.belgium.be/sites/default/files/media/documents/municipal-tax-rate-2026.pdf), table “CITY OR MUNICIPALITY / Rate (%)”, published 2026.

No official assessment-year-2027 municipality table was located by the access date. Accordingly:

- universal rule: apply the taxpayer's municipality's surcharge percentage to the relevant federal personal-tax base;
- benchmark assumption: **7.00%** purely for comparability;
- implementation requirement: municipality must be an input or the output must be labelled an estimate.

## 2. Employee social-security rules

### 2.1 Ordinary employee contribution and holiday-pay withholding

The ordinary private-sector employee contribution is **13.07% of gross pay**, with a work-bonus reduction for low earners. Source: Belgian Social Security, [Welke soorten bijdragen bestaan er?](https://www.socialsecurity.be/site_nl/employer/infos/employers_nsso/which-contributions.htm), heading “Gewone socialezekerheidsbijdragen” (accessed 2026-10-04; continuously updated).

For white-collar staff, statutory double holiday pay is not subject to ordinary contributions. It is nevertheless subject to a special employee withholding of **13.07%**, except the portion corresponding from the third day of the fourth vacation week. The administrative instructions implement this as a contribution base equal to **85/92** of statutory double holiday pay. Source: ONSS/RSZ Administrative Instructions 2026/3, [Le double pécule de vacances](https://www.socialsecurity.be/employer/instructions/dmfa/fr/latest/instructions/salary/particularcases/holidaypay.html), heading “Le double pécule de vacances” and example stating `85/92`; current version published 2026-08-27 and effective for 2026 Q3. See also [Retenue sur le double pécule](https://www.socialsecurity.be/employer/instructions/dmfa/fr/latest/instructions/special_contributions/other_specialcontributions/doubleholiday_privatesector.html), heading “Montant de la retenue.”

For the benchmark (`G = 12.92M`):

```text
ordinary social base = 12M
double holiday pay = 0.92M
holiday special-withholding base = (85/92) × 0.92M = 0.85M
employee social charge before work bonus = 13.07% × (12M + 0.85M)
```

### 2.2 Social work bonus

The work bonus reduces the normal 13.07% employee charge; it cannot exceed the contribution due. It is monthly and depends on a reference monthly full-time-equivalent wage, not annual gross alone. Source: ONSS/RSZ Administrative Instructions 2026/3, [Werkbonus](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/workers_reductions/workbonus.html), headings “Praktische toepassing,” “Vaststelling van het refertemaandloon,” and “Vaststelling van het verminderingsbedrag.”

For a full-time white-collar employee with full monthly performance, `S = W` and `P = R`. Official 2026 parameters are time-varying:

| Period | Component A | Component B |
|---|---|---|
| 2026 H1 | EUR 125.04 up to S=2,880.32, then `125.04 - .2738(S-2,880.32)` to S=3,336.98 | EUR 168.62 up to S=2,255.50, then `168.62 - .2699(S-2,255.50)` to S=2,880.32 |
| Jul–Aug 2026 | EUR 127.54 up to S=2,937.93, then `127.54 - .3196(S-2,937.93)` to S=3,336.98 | EUR 171.99 up to S=2,300.62, then `171.99 - .2699(S-2,300.62)` to S=2,937.93 |
| From Sep 2026 | EUR 127.54 up to S=2,937.93, then `127.54 - .2739(S-2,937.93)` to S=3,403.62 | same component B as Jul–Aug |

H1 source: ONSS/RSZ Administrative Instructions 2026/2, same [work-bonus page](https://www.socialsecurity.be/employer/instructions/dmfa/de/latest/instructions/deductions/workers_reductions/workbonus.html), table for white-collar employees. H2 source: 2026/3 page above, lines/tables headed “juli en augustus 2026” and “vanaf 1 september 2026.” The 2026/3 instructions state an annual work-bonus ceiling of **EUR 3,594.36 from 1 July 2026**.

### 2.3 Special social-security contribution (CSSS/BBSZ)

This is a separate employee charge. The annual liability is ultimately based on annual taxable **household** income and reconciled by direct-tax administration; employer withholdings are merely advances. Source: ONSS/RSZ Administrative Instructions 2026/3, [La cotisation spéciale pour la sécurité sociale](https://www.socialsecurity.be/employer/instructions/dmfa/fr/latest/instructions/special_contributions/other_specialcontributions/specialsocialsecuritycontribution.html), opening paragraphs under the page title.

For an individually assessed person, the official 2026 payroll advance per quarter is:

| Quarterly/related monthly pay condition | Quarterly advance |
|---|---:|
| monthly pay EUR 1,945.38–2,190.18 and quarterly pay EUR 5,836.14–6,570.54 | 4.22% of monthly portion above EUR 1,945.38 |
| monthly EUR 2,190.18–3,737 and quarterly EUR 6,570.54–11,211 | EUR 30.99 + 1.10% of monthly portion above EUR 2,190.18 |
| monthly EUR 3,737–4,100 and quarterly EUR 11,211–12,300 | EUR 82.05 + 3.38% of monthly portion above EUR 3,737 |
| monthly EUR 4,100–6,038.82 and quarterly EUR 12,300–18,116.46 | EUR 118.83 + 1.10% of monthly portion above EUR 4,100 |
| quarterly pay above EUR 18,116.46 | EUR 182.82 |

Same official source, heading “Montant de la retenue,” subsection “imposition individuelle”; 2026/3 version, published 2026-08-27. Maximum annual payroll advance is `4 × 182.82 = EUR 731.28`.

**Unresolved:** the official page does not state the final annual assessment formula or its 2026 annual-income thresholds. Consequently, the calculations below show the official payroll advance, not a claimed final household reconciliation.

## 3. Employer rules

### 3.1 Base contribution and structural reduction

The public ONSS summary says the private-profit employer rate is **25%** and that the profit-sector structural reduction is largely built into that fixed rate. Source: Belgian Social Security, [Welke soorten bijdragen bestaan er?](https://www.socialsecurity.be/site_nl/employer/infos/employers_nsso/which-contributions.htm), headings “Gewone socialezekerheidsbijdragen” and “Vermindering van de bijdragen.” The detailed 2026/3 instructions show a globalised base percentage of 24.92%; the public-facing 25% is the intended rounded rate for an ordinary salary estimate. Source: [De bijdragen](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html), heading “Het geglobaliseerde bijdragepercentage.”

The structural reduction is universal for workers subject to all branches. For category 1 in 2026 Q3:

```text
R = 0.1400 × max(11,687.74 - S, 0)
  + 0.1600 × max(9,738.14 - S, 0)
```

where S is reference quarterly wage; the final reduction is `Ps = R × μ × βs`. Source: ONSS/RSZ Administrative Instructions 2026/3, [De structurele vermindering](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/structuralreduction_targetgroupreductions/structuralreduction.html), headings “Bedrag van de vermindering” and the category-1 formula effective Q3 2026. For the EUR 20,000 mechanical case, this formula exceeds the raw 25% quarterly contribution, so the benchmark floors employer base contribution at zero; real entitlement still depends on DmfA performance factors and legal working time.

Employer-target-group reductions (first hire, age, region, etc.) require employer/employee facts and are excluded.

### 3.2 High-salary employer cap

From 2025 Q3 employer base contributions are not due on ordinary quarterly wage above a ceiling. In 2026 the ceiling is **EUR 86,700 per quarter from January through June** and **EUR 88,434 from 1 July**. The reduction is `(LC1 + LC61 - ceiling) × employer rate`. Source: ONSS/RSZ Administrative Instructions 2026/3, [Vrijstelling werkgeversbijdrage boven loonplafond](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/otheremployersreductions/partial_exemption_very_high_salaries.html), headings “Betrokken werknemers” and “Eerder grensbedrag”; effective dates stated on page.

This cap materially affects the EUR 600,000 case.

### 3.3 Holiday pay and employer contribution base

For white-collar employees, the employer pays holiday pay directly; no annual-holiday-fund employer contribution is included in ordinary ONSS contributions. Source: ONSS/RSZ Administrative Instructions 2026/3, [Les vacances annuelles](https://www.socialsecurity.be/employer/instructions/dmfa/fr/latest/instructions/obligations/obligations_branches/anualholidays.html), heading “Travailleurs intellectuels et apprentis intellectuels.”

Statutory double holiday pay is **92% of normal monthly gross** for a full qualifying year; single holiday pay is ordinary salary during leave. Source: FPS Social Security, [Annual vacation](https://socialsecurity.belgium.be/sites/default/files/alwa-en.pdf), white-collar section stating “12/12ths of 92% of gross salary”; publication date shown by the public document index as 2016. The modern ONSS instructions independently restate 92% in the `85/92` explanation cited above.

Therefore the benchmark includes double holiday cash in `G`, but applies no ordinary employer contribution to the `0.92M` element.

### 3.4 2026 wage moderation: not universal as a simple percentage

From **1 June 2026**, index adjustment is temporarily moderated over two periods. Once a sector/company index event occurs, a special employer wage-moderation contribution can arise on monthly reference salaries above EUR 4,000. Its formula uses the applicable sector/company index percentage, work fraction and the global employer rate; the official example with a 1.6% July index and 25% employer rate produces EUR 55 for that month. Source: ONSS/RSZ Administrative Instructions 2026/3, [Cotisation spéciale de modération salariale (index centime)](https://www.socialsecurity.be/employer/instructions/dmfa/fr/latest/instructions/special_contributions/pennyindex_wagemoderationcontribution.html), effective 2026-06-01, headings “Limitation temporaire,” “Formule,” and “Exemple 1.”

Annual gross alone cannot establish the sector's index mechanism, index dates, reference salary or work fraction. This contribution is therefore **excluded from worked employer totals and must be exposed as unresolved/sector-specific**, not approximated.

### 3.5 Other employer charges

The following must not be represented by a universal Belgian percentage:

- sectoral funds, closure-fund and risk-group charges;
- the 1.60% unemployment contribution where employer-size rules apply;
- insurance premiums (work accident, occupational cover), external-service costs and payroll administration;
- employer-specific target-group reductions;
- first-worker and regional reductions;
- sectoral thirteenth month/end-of-year premium;
- the annual redistribution of social charges, which can be a credit for some SMEs and a debit for larger employers.

The ONSS describes the last item as a redistribution benefiting certain SMEs and charging larger employers; it is employer-wide rather than a simple per-employee cost. Source: [La redistribution des charges sociales](https://www.socialsecurity.be/employer/instructions/dmfa/fr/latest/instructions/socialsecuritycontributions/socialchargesredistribution.html), heading “Employeurs concernés,” 2026/3.

## 4. Worked calculations

### 4.1 Benchmark formulas and caveats

All figures are euros, rounded to cents only for display. Internally calculations retain full precision.

```text
M = G / 12.92
normal salary = 12M
double holiday pay = 0.92M

ordinary employee SS = 13.07% × 12M - social work bonus
holiday withholding = 13.07% × 0.85M
employee social total = ordinary employee SS + holiday withholding

pre-expense taxable pay = G - employee social total
E = min(30% × pre-expense taxable pay, 6,070)
T = pre-expense taxable pay - E

federal PIT = bracket tax B(T) - 2,795 - fiscal work-bonus credit
illustrative municipal surcharge = 7% × positive federal PIT before refundable work-bonus credit
net = G - employee social total - federal PIT - municipal surcharge
      - official CSSS payroll advances

employer base SS = 25% × normal salary, less structural reduction,
                   and after the high-salary quarterly cap
illustrative employer cost = G + employer base SS
```

The EUR 20,000 case is **not a lawful full-year full-time adult benchmark**. The interprofessional guaranteed average minimum monthly income is EUR 2,189.81 from 2026-04-01 and EUR 2,233.61 from 2026-07-01, while sector minima can be higher. Sources: National Labour Council, [Salaire minimum](https://cnt-nar.be/fr/dossiers-thematiques/salaire-minimum), heading “Depuis le 1er avril 2026”; and FPS Employment, [Remuneration](https://employment.belgium.be/en/themes/international/posting/working-conditions-be-respected-case-posting-belgium/remuneration?id=38256), amount from 2026-07-01. The EUR 20,000 row is retained only as the requested mechanical stress test. A genuine part-time case needs hours/FTE data, which changes the work-bonus calculation.

### 4.2 Intermediate amounts

| Annual gross G | Monthly base M | 12M ordinary salary | 0.92M double holiday | Work bonus | Ordinary employee SS | Holiday withholding | Total employee social |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 1,547.99 | 18,575.85 | 1,424.15 | 2,427.86 | 0.00 | 171.97 | 171.97 |
| 60,000 | 4,643.96 | 55,727.55 | 4,272.45 | 0.00 | 7,283.59 | 515.92 | 7,799.51 |
| 100,000 | 7,739.94 | 92,879.26 | 7,120.74 | 0.00 | 12,139.32 | 859.87 | 12,999.19 |
| 200,000 | 15,479.88 | 185,758.51 | 14,241.49 | 0.00 | 24,278.64 | 1,719.74 | 25,998.37 |
| 600,000 | 46,439.63 | 557,275.54 | 42,724.46 | 0.00 | 72,835.91 | 5,159.21 | 77,995.12 |

For EUR 20,000, normal monthly contributions are `13.07% × 1,547.99 = 202.32`; the work bonus is capped at the contribution due, so it removes the full ordinary contribution each month. The double-holiday special withholding remains. This assumes full monthly performance; a realistic part-time worker requires an FTE calculation.

| G | Pay after employee social | Expense allowance | Net taxable T | Bracket tax B(T) | Personal-allowance reduction | Federal PIT before work-bonus credit |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 19,828.03 | 5,948.41 | 13,879.62 | 3,469.90 | 2,795.00 | 674.90 |
| 60,000 | 52,200.49 | 6,070.00 | 46,130.49 | 16,775.22 | 2,795.00 | 13,980.22 |
| 100,000 | 87,000.81 | 6,070.00 | 80,930.81 | 33,928.41 | 2,795.00 | 31,133.41 |
| 200,000 | 174,001.63 | 6,070.00 | 167,931.63 | 77,428.81 | 2,795.00 | 74,633.81 |
| 600,000 | 522,004.88 | 6,070.00 | 515,934.88 | 251,430.44 | 2,795.00 | 248,635.44 |

For the mechanical EUR 20,000 case, the inferred 2026 fiscal work-bonus credit is about **EUR 981.60**:

```text
H1 component A = 6 × 125.04
H1 component B after contribution cap = 6 × (202.32 - 125.04)
H2 component A = 6 × 127.54
H2 component B after contribution cap = 6 × (202.32 - 127.54)
credit ≈ 33.14% × total A + 52.54% × total B = EUR 981.60
```

That exceeds pre-credit federal PIT by EUR 306.69. Because the 2027 return instructions and exact refundable/municipal ordering were not available, the final table reports both the conservative “no inferred credit” result and the mechanical-credit result for this row.

### 4.3 Employee result and employer cost

| G | Federal PIT used | 7% municipal scenario | CSSS payroll advances | Estimated employee net | Employer base SS | Employer cost before excluded charges |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 conservative | 674.90 | 47.24 | 0.00 | 19,105.88 | 0.00* | 20,000.00* |
| 20,000 with inferred refundable work-bonus credit | -306.69 | 47.24** | 0.00 | 20,087.48 | 0.00* | 20,000.00* |
| 60,000 | 13,980.22 | 978.62 | 499.25 | 36,742.40 | 13,931.89 | 73,931.89 |
| 100,000 | 31,133.41 | 2,179.34 | 731.28 | 52,956.79 | 23,219.81 | 123,219.81 |
| 200,000 | 74,633.81 | 5,224.37 | 731.28 | 93,412.17 | 46,439.63 | 246,439.63 |
| 600,000 | 248,635.44 | 17,404.48 | 731.28 | 255,233.68 | 87,567.00 | 687,567.00 |

\* Mechanical structural-reduction floor. The salary is below the adult full-time income floor, and a real part-time calculation needs DmfA hours/performance factors.

\** The municipal scenario is deliberately calculated on the positive federal amount before the potentially refundable work-bonus credit. Exact assessment ordering remains unresolved; it should not be inferred from annual gross alone.

Employer details:

- Through EUR 200,000, `employer SS = 25% × 12M` (except the low-wage structural-reduction stress case).
- At EUR 600,000, every quarter's ordinary salary exceeds the cap. The base is `2 × 86,700 + 2 × 88,434 = 350,268`; `25% = EUR 87,567`.
- All employer totals exclude sector/company wage moderation, sectoral funds, the employer-wide annual redistribution, insurance and targeted reductions.

## 5. Effective dates and material edge cases

- **2026 tax parameters:** income-year 2026 / assessment-year 2027 brackets and EUR 11,180 allowance are expressly published by FPS Finance.
- **Work bonus changes during the year:** H1, Jul–Aug and Sep–Dec parameters differ. Annualising a single month is wrong near the thresholds.
- **Minimum income:** EUR 20,000 is not a valid full-time/full-year adult case. Part-time hours must be supplied.
- **Holiday history:** full 92% double holiday pay assumes full qualifying work in the preceding vacation-service year. New starters, returners, leavers and reduced-hours employees use different rules.
- **Thirteenth month:** not universal. Include only when the joint committee, company CBA or contract grants it.
- **Municipality:** replace 7% with the assessment-year-2027 rate for the employee's municipality when published.
- **CSSS:** payroll advances are not the final household liability. Multiple jobs, partner income and annual assessment can create a balance due/refund.
- **Work bonus:** part-time and incomplete-performance formulas gross up to reference pay; annual gross alone is insufficient.
- **Employer high-pay cap:** applies to specified ordinary-wage codes and per employer/per quarter, not indiscriminately to every cash element.
- **Wage moderation from 2026-06-01:** requires sector/company index facts and may add employer cost above the dossier totals.
- **Regions/sectors/employer facts:** targeted contribution reductions, Social Maribel, special funds, first-hire relief and older-worker rules are not universal.
- **Nonresidents:** the full personal allowance has a 75%-Belgian-professional-income condition; outside this dossier's resident scope.

## 6. Evidence assessment and unresolved facts

### Strongest evidence

1. FPS Finance's live table expressly labels and states the 2026 tax brackets and EUR 11,180 allowance.
2. ONSS/RSZ 2026/3 instructions give effective-period formulas and exact values for ordinary rates, work bonus, CSSS payroll advances, structural reduction, high-pay cap and wage moderation.
3. Official holiday-pay sources agree on 92% double holiday pay, its exclusion from ordinary contributions, and the special 13.07% employee withholding mechanics.

### Weakest evidence / do not hard-code without follow-up

1. **EUR 6,070 professional-expense cap:** present in the official 2026 withholding key formula, but assessment-year-2027 filing instructions were not yet published and the MyMinfin document is script-rendered. Reconfirm against the 2027 return instructions.
2. **Final annual CSSS liability:** only the official payroll-advance schedule was located; final annual household thresholds/formula remain unresolved.
3. **Fiscal work-bonus settlement and municipal ordering for income year 2026:** rates are evidenced, but assessment-year-2027 instructions were unavailable. The EUR 20,000 refundable result is explicitly an inference.
4. **Municipal surcharge for assessment year 2027:** unavailable. The 7% worked assumption is a scenario, not Belgian law.
5. **Employer total cost:** cannot be exact without joint committee, company size, region, index history, targeted reductions and employer-wide levies.

## 7. Implementation guidance

An implementation should separate:

- annual assessment tax from payroll withholding;
- universal federal inputs from municipality/sector/employer inputs;
- ordinary salary, double holiday pay, year-end premium and exceptional pay;
- employee ordinary social contribution, work bonus, holiday withholding and CSSS;
- employer base rate, structural reduction, high-pay cap, wage-moderation contribution and other special charges.

At minimum, request or expose assumptions for municipality, joint committee/sector, normal monthly salary, payment periods, FTE/work fraction, entitlement to holiday pay, employer category/size, region and any target-group reduction. A single annual gross input can only produce the benchmark estimate documented here.
