# Slovakia employee payroll, income year 2026 — clean-room dossier

**Scope.** Independent reconstruction from Slovak primary official sources, accessed **2026-10-04**. The model is a Slovak-resident employee, age 30, single, no children, not disabled or retired, in ordinary private employment, with regular annual cash salary and the standard taxpayer non-taxable allowance. There are no other deductions, credits, benefits or income. Results are after 2026 annual income-tax reconciliation.

## Result in one view

For each month, with gross cash pay \(g\) and social ceiling \(C=€16,764\):

```text
employee social = 1.4% sickness + 4% old age + 3% disability + 1% unemployment
                = 9.4% × min(g, C), calculated fund by fund
employee health = 5% × g, uncapped
§5 tax base     = gross − employee social − employee health
taxable base    = §5 tax base − taxpayer allowance
PIT             = progressive 19% / 25% / 30% / 35%

employer capped social = 24.4% × min(g, C), calculated fund by fund
employer accident       = 0.8% × g, uncapped
employer health         = 11% × g, uncapped
```

The 24.4% employer capped total comprises 1.4% sickness, 14% old-age, 3% disability, a combined 1% unemployment/support-financing allocation, 0.25% guarantee insurance, and 4.75% solidarity reserve. Below the ceiling, total employer payroll contributions are therefore 36.2% of gross (24.4% capped social + 0.8% accident + 11% health).

## 1. Income tax

### Tax base and 2026 rates

Income Tax Act no. **595/2003 Z. z.**, §5(8), defines an employee's partial tax base as taxable employment income reduced by mandatory insurance borne by the employee. The official time version is effective 1 January–30 December 2026. [Slov-Lex, “595/2003 Z. z. Zákon o dani z príjmov,” §5(8), §11, §15, §35 and §47](https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/2003/595/) (Act approved 4 December 2003, promulgated 31 December 2003; select the time version effective 01.01.2026).

For 2026 employment income after the non-taxable allowance, Financial Administration states these annual bands:

| Part of annual taxable base | Rate | Monthly payroll-prepayment boundary |
|---|---:|---:|
| up to €43,983.32 | 19% | up to €3,665.28 |
| above €43,983.32 through €60,349.21 | 25% | above €3,665.28 through €5,029.10 |
| above €60,349.21 through €75,010.32 | 30% | above €5,029.10 through €6,250.86 |
| above €75,010.32 | 35% | above €6,250.86 |

[Financial Administration, “Sadzba dane pre závislú činnosť,” 2026 section, lines/points headed “za rok 2026”](https://podpora.financnasprava.sk/939516-Sadzba-dane-pre-z%C3%A1visl%C3%BA-%C4%8Dinnos%C5%A5). The authority's worked example confirms that annual reconciliation applies the annual bands even where monthly withholding used the monthly bands.

These high-income bands are a **2026 change** enacted by **Act no. 261/2025 Z. z., amending certain laws in connection with consolidation of public finances**, adopted 24 September 2025 and promulgated 9 October 2025. Article VIII changes Income Tax Act §15 and §35 to 19%, 25%, 30% and 35%; transitional §52zzzj applies them first to tax year 2026 and January 2026 payroll. [Official promulgated Act 261/2025, pp. 13–15, especially lines 564–575, 599–607 and 632–642](https://static.slov-lex.sk/pdf/SK/ZZ/2025/261/ZZ_2025_261.pdf).

### Standard taxpayer allowance (NČZD)

Let \(B\) be the annual §5 employee tax base **before** this allowance:

\[
N(B)=
\begin{cases}
€5{,}966.73,&B\le €26{,}083.13\\
\max(0,€14{,}661.11-B/3),&B>€26{,}083.13.
\end{cases}
\]

Financial Administration identifies the values as 21, 91.8 and 51.6 times the applicable subsistence minimum. The allowance reaches zero at a base of about €43,983.33. It is available against active employment income; the assumed employee is not a pensioner. [Financial Administration, “Nezdaniteľná časť základu dane na daňovníka za rok 2026,” points before FAQ and examples 1–2](https://podpora.financnasprava.sk/260857-Nezdanite%C4%BEn%C3%A1-%C4%8Das%C5%A5-z%C3%A1kladu-dane-na-da%C5%88ovn%C3%ADka-za-rok-2026). [Financial Directorate information 31/DZPaU/2025/I, “Prehľad súm potrebných pre výpočet daňovej povinnosti fyzických osôb na rok 2026,” October 2025, p. 2 lines 18–26](https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Novinky_leg/Priame_dane_uct/2025/2025.10.17_031_DZPaU_2025_I.pdf).

An employee who signs the declaration may receive €497.23 per month in payroll, but the correct full-year amount is recomputed from annual \(B\). A phaseout or loss of the allowance therefore produces a reconciliation adjustment. Financial Administration says the full annual amount is settled by employer annual reconciliation or the employee's return. [Same NČZD page, questions 5–6](https://podpora.financnasprava.sk/260857-Nezdanite%C4%BEn%C3%A1-%C4%8Das%C5%A5-z%C3%A1kladu-dane-na-da%C5%88ovn%C3%ADka-za-rok-2026).

## 2. Employee social insurance

The Social Insurance Agency's **“Tabuľky platenia poistného od 1. januára 2026”** gives the ordinary employee rates and €16,764 monthly maximum assessment base:

| Fund | Employee rate | 2026 monthly maximum base | Maximum monthly contribution |
|---|---:|---:|---:|
| sickness | 1.40% | €16,764 | €234.69 |
| old-age pension | 4% | €16,764 | €670.56 |
| disability pension | 3% | €16,764 | €502.92 |
| unemployment | 1% | €16,764 | €167.64 |
| **Total** | **9.4%** | | **€1,575.81** |

[Social Insurance Agency, “Tabuľky platenia poistného od 1. januára 2026,” employee table and explanations 2 and 7](https://socpoist.sk/socialne-poistenie/platenie-poistneho/tabulky-platenia-poistneho/tabulky-platenia-poistneho-od-1-6) (effective date is in the title; the live table displays no separate publication date). Its 9 January 2026 notice confirms the employee/employer ceiling, that an employee has no social-insurance minimum base, and that actual remuneration is used subject to the monthly maximum. [Social Insurance Agency, “Nové vymeriavacie základy pre platenie poistného od 1. januára 2026,” dated 9 January 2026, section “Nový maximálny vymeriavací základ”](https://www.socpoist.sk/news/nove-vymeriavacie-zaklady-pre-platenie-poistneho-od-1-januara-2026).

The ceiling is monthly, not a freely transferable annual cap. For 12 regular pays it corresponds to €201,168, but a bonus concentrated in one month could produce a different annual contribution. This dossier assumes regular monthly salary.

## 3. Employer social insurance

For the ordinary employee, the same official 2026 table specifies:

| Fund | Employer rate | Ceiling |
|---|---:|---:|
| sickness | 1.40% | €16,764/month |
| old-age pension | 14% | €16,764/month |
| disability pension | 3% | €16,764/month |
| unemployment / support financing | 1% total | €16,764/month |
| guarantee insurance | 0.25% | €16,764/month |
| solidarity reserve fund | 4.75% | €16,764/month |
| accident insurance | 0.8% | **no maximum** |

The unemployment component is either 1%, or 0.5% plus 0.5% support-financing, depending on whether the employer pays the latter; the combined employer cost remains 1%. The Agency's explanatory note says accident insurance must be added on the employee's actual assessment base because it is uncapped. [Social Insurance Agency 2026 table, employer rows and explanations 2, 5 and `***`](https://socpoist.sk/socialne-poistenie/platenie-poistneho/tabulky-platenia-poistneho/tabulky-platenia-poistneho-od-1-6).

At the capped base, the employer's capped-fund maximum is €4,090.41/month. Accident insurance remains additional. Guarantee and reserve contributions are therefore included in the worked employer cost rather than omitted as generic overhead.

## 4. Public health insurance

For a non-disabled employee from 1 January 2026:

- employee: **5%** of monthly income;
- employer: **11%** of monthly income;
- neither employee nor employer has a maximum assessment base.

[State insurer VšZP, “Zamestnávateľ,” sections “Vymeriavací základ” and “Sadzba poistného,” 2026 rows](https://www.vszp.sk/platitelia/platenie-poistneho/zamestnavatel/) (pinpoints: no minimum/maximum base at lines 404–411; rates at lines 437–448). [VšZP, “Preddavky na poistné,” table “Minimálne a maximálne vymeriavacie základy a preddavky v roku 2026”](https://www.vszp.sk/platitelia/platenie-poistneho/preddavky-poistne.html). These live VšZP pages state applicability from 1 January 2026 but display no separate publication date; they were current on the access date.

Act 261/2025 raised the employee rate from 4% to 5% and establishes, for 1 January 2026 through 31 December 2027, the combined 16% regime including 11% employer health insurance. [Official Act 261/2025, Article XIII, p. 21, lines 963–1008](https://static.slov-lex.sk/pdf/SK/ZZ/2025/261/ZZ_2025_261.pdf).

### Minimum health contribution

For a full calendar month in 2026, minimum combined employee/employer health advance is **€45.45**, 16% of the €284.13 subsistence minimum: employee portion €14.20 (5%) plus notional employer portion €31.25 (11%). If ordinary calculated contributions are less, the employee bears the top-up; it does not increase the employer's 11% burden. Exceptions include a concurrent state-insured status and disability. [VšZP employer page, lines 404–448](https://www.vszp.sk/platitelia/platenie-poistneho/zamestnavatel/). Every requested salary produces health contributions above this minimum, so no top-up appears below.

Health contributions are paid monthly as advances and are subject to health-insurer annual reconciliation. [VšZP, “Preddavky na poistné,” explanation of annual premium versus monthly advances](https://www.vszp.sk/platitelia/platenie-poistneho/preddavky-poistne.html).

## 5. Financial-transaction tax: separate, variable employer cost

From 2026, a Slovak legal person remains a taxpayer for financial-transaction tax (DFT), while the 2026 change removed natural-person entrepreneurs from its taxpayer population. An outbound debit generally bears **0.4%, capped at €40 per transaction**; incoming employee salary is not taxed to the employee merely because it is credited. Financial Administration also confirms that employer-originated employee-related debits can fall within DFT. [Financial Administration, “Daň z finančných transakcií — FAQ,” sections “Predmet dane, základ dane a sadzba dane” and employee-related examples](https://www.financnasprava.sk/sk/aktualne-dan-clo/faq/dan-financne-transakcie/_).

DFT is **not** a wage-base contribution and cannot be stated as a universal percentage of one employee's gross salary: it depends on employer legal form, bank/payment route, whether payments are batched, number of transactions and exemptions. It is consequently excluded from the worked statutory payroll cost. For a legal-person employer paying each employee by a separate bank debit, it may be an additional payment cost; this needs transaction facts rather than a payroll assumption.

## 6. Calculation and rounding method

The worked cases use this reproducible schedule:

1. Annual gross is allocated to 12 regular cent-denominated pays: annual/12 rounded to cents for January–November, with December as the exact residual.
2. Each social-insurance fund is computed separately from `min(monthly gross, €16,764)` and rounded down to the cent. The Social Insurance Agency expressly requires the base and each fund contribution to be rounded down separately. [Agency 2026 table, final explanatory note](https://socpoist.sk/socialne-poistenie/platenie-poistneho/tabulky-platenia-poistneho/tabulky-platenia-poistneho-od-1-6).
3. Each health advance is rounded down to the cent under Health Insurance Act no. 580/2004 Z. z. [Slov-Lex, official Act 580/2004 time version effective 1 January 2026](https://static.slov-lex.sk/pdf/SK/ZZ/2004/580/ZZ_2004_580_20260101.pdf) (pinpoint: §16 rounding and §19 annual reconciliation).
4. Annual §5 base equals gross less the actual rounded employee contributions. Annual NČZD is recomputed. Annual PIT uses annual bands; §47 rounds tax bases and tax down to cents and NČZD up to cents. [Income Tax Act 595/2003, §47](https://www.slov-lex.sk/ezbierky/pravne-predpisy/SK/ZZ/2003/595/).

Monthly withholding can differ from final annual PIT because payroll uses monthly band boundaries and the monthly €497.23 allowance, while annual reconciliation uses exact annual thresholds and the income-dependent annual allowance. Financial Administration says an employee with only employment income may request 2026 reconciliation by 15 February 2027; the employer completes it by 31 March 2027. [Financial Administration employee guidance](https://www.financnasprava.sk/sk/obcania/dane/dan-z-prijmov/zamestnanci); [deadline guidance](https://podpora.financnasprava.sk/536191-Lehota-na-vykonanie-ro%C4%8Dn%C3%A9ho-z%C3%BA%C4%8Dtovania).

## 7. Worked annual calculations

### Intermediate employee calculation

All figures are euros and follow the cent-rounding schedule above.

| Annual gross | Employee social | Employee health | §5 base before NČZD | NČZD | Taxable base | PIT after annual reconciliation | Net cash |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000.00 | 1,879.79 | 999.96 | 17,120.25 | 5,966.73 | 11,153.52 | 2,119.16 | **15,001.09** |
| 60,000.00 | 5,640.00 | 3,000.00 | 51,360.00 | 0.00 | 51,360.00 | 10,201.00 | **41,159.00** |
| 100,000.00 | 9,399.73 | 4,999.92 | 85,600.35 | 0.00 | 85,600.35 | 20,553.14 | **65,047.21** |
| 200,000.00 | 18,799.79 | 9,999.96 | 171,200.25 | 0.00 | 171,200.25 | 50,513.11 | **120,687.14** |
| 600,000.00 | 18,909.72 | 30,000.00 | 551,090.28 | 0.00 | 551,090.28 | 183,474.62 | **367,615.66** |

At €20,000:

```text
§5 base       = 20,000.00 − 1,879.79 − 999.96 = 17,120.25
NČZD           = 5,966.73 (base ≤ 26,083.13)
taxable base   = 17,120.25 − 5,966.73 = 11,153.52
PIT            = floor-cent(11,153.52 × 19%) = 2,119.16
net            = 20,000.00 − 1,879.79 − 999.96 − 2,119.16 = 15,001.09
```

At €100,000, NČZD has fully phased out and the tax crosses all four bands:

```text
§5/taxable base = 100,000.00 − 9,399.73 − 4,999.92 = 85,600.35
PIT = 19% × 43,983.32
    + 25% × (60,349.21 − 43,983.32)
    + 30% × (75,010.32 − 60,349.21)
    + 35% × (85,600.35 − 75,010.32)
    = 20,553.14 after final statutory downward-cent rounding
```

At €600,000, each €50,000 monthly pay exceeds the social ceiling. Employee social is therefore the official maximum €1,575.81 × 12 = €18,909.72, but health remains 5% of the full €600,000.

### Employer contributions and cost

| Annual gross | Capped employer social funds | Uncapped accident 0.8% | Employer health 11% | Total employer contributions | Employer cost excluding DFT |
|---:|---:|---:|---:|---:|---:|
| 20,000.00 | 4,879.66 | 159.96 | 2,199.95 | 7,239.57 | **27,239.57** |
| 60,000.00 | 14,640.00 | 480.00 | 6,600.00 | 21,720.00 | **81,720.00** |
| 100,000.00 | 24,399.62 | 799.92 | 10,999.93 | 36,199.47 | **136,199.47** |
| 200,000.00 | 48,799.66 | 1,599.96 | 21,999.95 | 72,399.57 | **272,399.57** |
| 600,000.00 | 49,084.92 | 4,800.00 | 66,000.00 | 119,884.92 | **719,884.92** |

At €600,000 the capped employer funds equal the official €4,090.41 monthly maximum × 12 = €49,084.92. Accident and health remain uncapped.

## 8. Boundaries and unresolved facts

- This is ordinary employment. Pensioners, disability status, public office, municipal police, trainers, agreements outside employment, multiple simultaneous employers and second-pillar allocation details can change individual fund rows or eligibility. They are not silently assumed.
- The 0.5% unemployment plus 0.5% support-financing split versus 1% unemployment depends on the statutory financing status, but the total ordinary employer rate and every worked employer cost are unchanged.
- Social insurance has a monthly ceiling. Irregular bonuses require month-by-month facts and cannot safely be annualised using €201,168.
- Health insurance is uncapped and annually reconciled. The minimum top-up is employee-borne and irrelevant at every requested salary.
- DFT may add an employer banking cost but is transaction-specific, not a universal payroll contribution; it is shown separately rather than guessed into employer cost.

## Evidence assessment

**Strongest evidence.** Act 261/2025 is the legally binding promulgated source for the new four-band PIT and 2026 health-rate change. Financial Administration's October 2025 numerical schedule supplies exact 2026 thresholds and allowance values. The Social Insurance Agency's dedicated 2026 table supplies every employee/employer fund rate, the €16,764 ceiling, maximum contributions, uncapped accident treatment and rounding instruction.

**Weakest evidence / model sensitivity.** The live Social Insurance Agency and VšZP tables clearly label their 2026 effective rules but do not display separate publication dates; the rates are nevertheless independently anchored in legislation and the Agency's dated notice. DFT cannot be converted into a universal per-employee employer cost without employer legal-form and payment-transaction facts. Cent-level results also depend on the explicitly stated regular-pay allocation; a different real payment schedule—especially a concentrated bonus—changes capped social insurance and monthly withholding, although annual PIT reconciliation still applies the annual bands.
