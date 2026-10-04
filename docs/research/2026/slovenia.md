# Slovenia — employee payroll research for income year 2026

**Research status:** clean-room reconstruction from Slovenian primary sources only.
**Access date for every linked source:** 2026-10-04.
**Currency:** euro (EUR). Amounts are annual unless stated otherwise.

## Scope and result definition

The worked case is a Slovenian tax resident, single, age 30 throughout 2026, no children or other dependants, one main employer, full-time ordinary private-sector employment for the full calendar year, and regular cash salary paid in 12 equal monthly instalments. There are no benefits in kind, bonuses, union dues, voluntary pension payments, disability status, cross-border facts or special reliefs. “Gross salary” in the examples is the contractual cash salary only; statutory vacation and winter regress and expense reimbursements are shown separately because they are not regular salary.

The reproducible outputs are:

* **salary net cash** = gross salary − employee percentage contributions − employee mandatory health contribution − annual PIT;
* **salary employer cost** = gross salary + employer percentage contributions; and
* a separate **minimum full-year statutory cash package** adds the minimum vacation regress and winter regress, but not meals or commuting reimbursement because those cannot be calculated without facts not supplied.

All five examples are above the monthly minimum contribution base and the low-income additional-general-allowance threshold. No contribution ceiling is applied.

## 1. Personal income tax (dohodnina)

### 1.1 2026 allowances

The controlling annual amounts are in the Ministry of Finance regulation **“Pravilnik o določitvi usklajenih zneskov olajšav, enačbe za določitev olajšave in lestvice za odmero dohodnine za leto 2026”**, document 2025-01-3538, signed 2025-12-03 and published in *Uradni list RS* 104/2025 on 2025-12-12; it applies for 2026. [PISRS text](https://pisrs.si/pregledNpb?idPredpisa=PRAV15981&idPredpisaChng=PRAV15981); [official-gazette issue index](https://www.uradni-list.si/glasilo-uradni-list-rs/celotno-kazalo/2025104).

Its exact 2026 figures are:

* basic general allowance: **€5,551.93**;
* if total income does not exceed **€17,766.18**, an additional general allowance of **€20,832.39 − 1.17259 × total income** is added to the basic allowance;
* special allowance for employment income for a person “up to completion of age 29”: **€1,443.50**.

The assumed employee is age 30, so the young-worker allowance is not used. Every sample salary exceeds €17,766.18, so each receives only the €5,551.93 basic general allowance. FURS also publishes a **“Pripomoček za izračun splošne olajšave v letu 2026 pri izračunu akontacije dohodnine od mesečnega dohodka iz delovnega razmerja”**, updated 2025-12-19, for monthly withholding. [FURS calculator page](https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/dohodnina/dohodnina_dohodek_iz_zaposlitve/pripomocek_za_izracun_splosne_olajsave_v_letu_2026_pri_izracunu_akontacije_dohodnine_od_mesecnega_dohodka_iz_delovnega_razmerja).

### 1.2 Taxable base and 2026 scale

Article 41(1) of **Zakon o dohodnini (ZDoh-2)** says the employment-income tax base is employment income reduced by mandatory social-security contributions payable by the employee. [PISRS consolidated ZDoh-2, Article 41](https://pisrs.si/Pis.web/pregledPredpisa?print=1&sop=2006-01-5013&tab=osnovni). Accordingly, this dossier deducts both the percentage employee contributions and the fixed mandatory health contribution before the general allowance.

The same 2026 regulation gives this exact annual scale:

| Annual taxable base | Annual PIT |
|---:|---:|
| €0–€9,721.43 | 16% of base |
| €9,721.43–€28,592.44 | €1,555.43 + 26% of excess over €9,721.43 |
| €28,592.44–€57,184.88 | €6,461.89 + 33% of excess over €28,592.44 |
| €57,184.88–€82,346.23 | €15,897.40 + 39% of excess over €57,184.88 |
| over €82,346.23 | €25,710.33 + 50% of excess over €82,346.23 |

Here, `annual taxable base = max(0, gross salary − employee mandatory contributions − applicable allowances)`.

### 1.3 Withholding versus final annual assessment

For a main employer, the official SPOT payroll guidance says the monthly advance uses one twelfth of the annual scale and one twelfth of the allowances; a non-main employer instead withholds at 25% without allowances. [SPOT, “Prispevki za socialno varnost”, section on employment-income advance](https://spot.gov.si/sl/teme/prispevki-za-socialno-varnost). FURS explains in **“Letna odmera dohodnine”** that annual income is assessed and advances already withheld are credited against the final annual liability. [FURS annual-assessment page](https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/dohodnina/letna_odmera_dohodnine).

Thus the examples calculate the final annual PIT directly. Exact payslip withholding can differ by cents because payroll is monthly and rounded. The reviewed official sources did not provide a single universal cents-rounding algorithm covering every payroll component, so no unverified rounding convention is invented here.

## 2. Mandatory social contributions

### 2.1 Ordinary percentage contributions

The government’s SPOT page **“Socialna varnost in zavarovanja”** gives the following employer and employee rates on gross salary. The page does not display a publication date; it was current on the access date. [Official SPOT table](https://spot.gov.si/sl/poslovanje/zaposlovanje-in-delovno-razmerje/socialna-varnost-in-zavarovanja/).

| Insurance | Employee | Employer |
|---|---:|---:|
| Pension and disability | 15.50% | 8.85% |
| Compulsory health | 6.36% | 6.56% |
| Parental protection | 0.10% | 0.10% |
| Unemployment | 0.14% | 0.06% |
| Injury at work / occupational disease | — | 0.53% |
| **Ordinary subtotal** | **22.10%** | **16.10%** |

ZPIZ’s **“Delavci v delovnem razmerju”** confirms the employer calculates, withholds and pays the worker’s contributions as well as its own contributions. [ZPIZ employee-insurance page](https://www.zpiz.si/content2019/delavci-v-delovnem-razmerju). FURS lists the governing social-security statutes on **“Prispevki za socialno varnost”**. [FURS overview](https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/prispevki_za_socialno_varnost).

### 2.2 Long-term-care contribution

ZZZS’s official implementation page **“Aktivnosti uvedbe dolgotrajne oskrbe”** states that collection began on **2025-07-01**, that an employee pays **1%**, the employer pays **1%**, and the combined rate is **2%**; the contribution base is the same base used for compulsory health insurance for sickness and injury outside work. [ZZZS, contribution section](https://www.zzzs.si/dolgotrajna-oskrba/aktivnosti-uvedbe-dolgotrajne-oskrbe/). It applies for all of 2026 in this scenario.

Therefore the total variable rates used are:

* employee: **22.10% + 1.00% = 23.10%** of gross salary;
* employer: **16.10% + 1.00% = 17.10%** of gross salary.

### 2.3 Fixed mandatory health contribution (OZP)

ZZZS’s **“Obvezni zdravstveni prispevek”** identifies OZP as a compulsory social-security contribution and states that the main employer withholds it from gross income. It is a fixed nominal amount and is not prorated. The official page specifies **€39.36 per month from March 2026 through February 2027**. [ZZZS OZP page, sections “Višina obveznega zdravstvenega prispevka” and employee withholding](https://zavezanec.zzzs.si/prispevki-za-obvezno-zdravstveno-zavarovanje/obvezni-zdravstveni-prispevek/). ZZZS’s official **2025 annual report** records the preceding amount as **€37.17 from March 2025**, which consequently applies in January and February 2026. [ZZZS, *Letno poročilo ZZZS 2025*, published 2026-03-23](https://www.zzzs.si/fileadmin/user_upload/slike/o_zzzs/letno_porocilo_zzzs_2025_23.3.2026.pdf).

For a continuously insured employee in 2026:

`annual OZP = 2 × €37.17 + 10 × €39.36 = €467.94`.

OZP is employee-borne; it is not added to employer cost. Because it is a mandatory employee social contribution, it is deducted in the Article 41 PIT base calculation.

### 2.4 Minimum and maximum contribution bases

FURS’s notice **“Najnižja osnova za obračun prispevkov za socialno varnost za osebe v delovnem razmerju”**, published 2026-02-26 at 13:32, pinpoints Article 144(4) ZPIZ-2: the monthly minimum is 60% of the last known annual average wage, converted monthly. It states **€1,521.62 from 2026-03-01 through 2027-02-28**, based on the 2025 average monthly wage of €2,536.03. [FURS notice](https://www.fu.gov.si/novica/najnizja_osnova_za_obracun_prispevkov_za_socialno_varnost_za_osebe_v_delovnem_razmerju_1-16145). For January–February, the rule uses 60% of the 2024 average; SURS’s **“Plače zaposlenih pri pravnih osebah, december 2024”**, published 2025-02-17, gives the 2024 average as €2,394.92, hence **€1,436.95** after rounding. [SURS release](https://www.stat.si/StatWeb/news/Index/13457).

Article 144(1) ZPIZ-2 bases ordinary employee contributions on salary and other employment remuneration, while Article 144(4) supplies the floor. The same consolidated text sets a 3.5-times-average maximum in Article 145(5) for self-employed persons, company members and farmers—not employees under Article 144. No maximum for an ordinary employee was found in the reviewed primary provisions, so contributions are applied to full salary at every example level. [PISRS consolidated ZPIZ-2, Articles 144–145, pp. 76–78](https://pisrs.si/api/datoteke/integracije/356019101).

The lowest sample is €20,000 / 12 = €1,666.67 monthly, above both 2026 monthly floors. Thus no top-up calculation is required. If monthly salary fell below the floor, contribution cost would no longer be a simple percentage of cash salary and the statutory allocation of the difference would have to be implemented.

## 3. Meals, commuting and regress payments

These items must not be silently folded into a universal salary formula.

### 3.1 Meal and commuting reimbursements

Article 130(1) of **Zakon o delovnih razmerjih (ZDR-1)** requires the employer to reimburse the employee's meal-at-work and home-to-work transport costs; Article 130(2) says the amount is set by an industry collective agreement, or by secondary legislation if no such collective amount exists. [PISRS consolidated ZDR-1, Article 130](https://pisrs.si/Pis.web/pregledPredpisa?d-49685-p=1&id=ZAKO5944). The entitlement is therefore universal, but its cash amount is not. Separately, the official **“Uredba o davčni obravnavi povračil stroškov in drugih dohodkov iz delovnega razmerja”** provides tax-base exclusion ceilings:

* meals: up to **€7.96 per day** present at work for at least four hours; if present at least ten hours, up to an additional **€0.76 per completed hour after eight hours**;
* home-to-work commuting: up to **€0.21 per full kilometre** for each attendance day, subject to the regulation’s distance and other conditions.

[PISRS consolidated reimbursement regulation, Articles 2–3](https://pisrs.si/pregledPredpisa?d-49687-s=2&id=URED4359). The actual amount depends on the applicable collective agreement or secondary rule, attendance days, residence, worksite, distance and transport facts. Amounts above the regulatory exclusion are not automatically exempt. Therefore neither item appears in the worked numbers.

### 3.2 Vacation regress

The Ministry of Labour’s **“Pravico do regresa za letni dopust ima vsak delavec, ki ima sklenjeno pogodbo o zaposlitvi”**, published 2026-04-17 and updated 2026-04-20, states that every employee has the right under Article 131 ZDR-1 to at least the 2026 minimum wage, **€1,481.88**, for a full year/full entitlement; proportional rules apply for shorter employment or ordinary part-time work. Payment is generally due by July 1, exceptionally by November 1 under an industry collective agreement for employer illiquidity. [GOV.SI notice, especially paragraphs 1–6](https://www.gov.si/novice/2026-04-17-pravico-do-regresa-za-letni-dopust-ima-vsak-delavec-ki-ima-sklenjeno-pogodbo-o-zaposlitvi/).

ZDoh-2 Article 44(1)(13) excludes vacation regress from the PIT base up to 100% of the Slovenian average monthly wage, subject to its annual test. [PISRS consolidated ZDoh-2, Article 44](https://pisrs.si/Pis.web/pregledPredpisa?print=1&sop=2006-01-5013&tab=osnovni). ZPIZ-2 Article 144(3) similarly includes only the portion exceeding 100% of the last known Slovenian average monthly wage in the contribution base. [PISRS consolidated ZPIZ-2, Article 144(3), pp. 76–77](https://pisrs.si/api/datoteke/integracije/356019101). The statutory minimum €1,481.88 is below those ceilings, so this dossier treats that minimum as PIT- and contribution-free. A higher collective or contractual regress requires testing at payment and annual reconciliation.

### 3.3 Winter regress

The **Zakon o pravici do zimskega regresa … (ZPZR)**, Official Gazette RS 91/2025, effective 2025-11-20, created an ongoing employee right. Article 2 sets it at **half the minimum wage** in cash; Articles 2–3 contain proportional-employment rules and the ordinary payment deadline (18 days after the November salary period). Article 4 excludes the statutory amount from the employment-income PIT base, subject to the combined business-performance-payment ceiling; Article 5 excludes it from the social-contribution base. [Official PISRS act PDF, pp. 1–2](https://pisrs.si/api/datoteke/integracije/400056166).

For a full-year, full-time employee in 2026, the statutory winter regress is `€1,481.88 / 2 = €740.94`. The examples assume no business-performance payment that would consume the linked tax ceiling.

## 4. Calculation formulas and worked examples

For gross salary `G` in the stated scenario:

```text
employee percentage contributions E = 23.10% × G
fixed employee OZP H               = €467.94
PIT base before allowance B        = G − E − H
annual taxable base T              = max(0, B − €5,551.93)
PIT P                              = 2026 progressive-scale tax(T)
salary net                         = G − E − H − P

employer percentage contributions R = 17.10% × G
salary employer cost                = G + R
minimum regresses                   = €1,481.88 + €740.94 = €2,222.82
employer cash cost incl. regresses  = G + R + €2,222.82
```

Intermediate and final amounts, rounded to cents only after annual calculation:

| Gross salary G | Employee % contrib. E | OZP H | Base before allowance B | Allowance | Taxable base T | PIT P | Salary net | Employer contrib. R | Salary employer cost | Cost incl. minimum regresses |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| €20,000.00 | €4,620.00 | €467.94 | €14,912.06 | €5,551.93 | €9,360.13 | €1,497.62 | **€13,414.44** | €3,420.00 | **€23,420.00** | **€25,642.82** |
| €60,000.00 | €13,860.00 | €467.94 | €45,672.06 | €5,551.93 | €40,120.13 | €10,266.03 | **€35,406.03** | €10,260.00 | **€70,260.00** | **€72,482.82** |
| €100,000.00 | €23,100.00 | €467.94 | €76,432.06 | €5,551.93 | €70,880.13 | €21,238.55 | **€55,193.51** | €17,100.00 | **€117,100.00** | **€119,322.82** |
| €200,000.00 | €46,200.00 | €467.94 | €153,332.06 | €5,551.93 | €147,780.13 | €58,427.28 | **€94,904.78** | €34,200.00 | **€234,200.00** | **€236,422.82** |
| €600,000.00 | €138,600.00 | €467.94 | €460,932.06 | €5,551.93 | €455,380.13 | €212,227.28 | **€248,704.78** | €102,600.00 | **€702,600.00** | **€704,822.82** |

Bracket checks:

* €20,000: `P = 16% × €9,360.13 = €1,497.62`.
* €60,000: `P = €6,461.89 + 33% × (€40,120.13 − €28,592.44) = €10,266.03`.
* €100,000: `P = €15,897.40 + 39% × (€70,880.13 − €57,184.88) = €21,238.55`.
* €200,000: `P = €25,710.33 + 50% × (€147,780.13 − €82,346.23) = €58,427.28`.
* €600,000: `P = €25,710.33 + 50% × (€455,380.13 − €82,346.23) = €212,227.28`.

The employee additionally receives €2,222.82 of minimum regresses under the full-year assumptions, so minimum total employee cash is salary net plus €2,222.82. Those payments are deliberately not labelled salary net because their entitlement, payment dates and ceiling tests are legally distinct.

## 5. Universal rules versus variable or unresolved items

### Included as universal for the stated employee

* the 2026 PIT scale and €5,551.93 basic allowance;
* 23.10% employee and 17.10% employer aggregate percentage contributions, including 1% each for long-term care;
* annual OZP of €467.94 for continuous insurance in 2026;
* no employee contribution ceiling and the statutory monthly contribution floor (irrelevant at the sample salaries);
* minimum full-year vacation regress of €1,481.88 and winter regress of €740.94.

### Variable, conditional, or deliberately unresolved

* Meal and commuting reimbursement is mandatory under ZDR-1 Article 130, but the amount depends on the applicable collective agreement or fallback rule and actual attendance, distance and transport facts; the tax regulation's exemption ceilings alone are not enough to calculate cash.
* Higher vacation regress, business-performance pay, and any winter-regress excess require the statutory combined annual ceiling tests.
* Industry collective agreements can prescribe additional payments or higher rights. None is selected because “ordinary private employment” does not identify an industry.
* Employers subject to special disability-quota, hazardous-work/occupational-pension, apprenticeship or other status-based rules can have further costs. They are not universal to an ordinary office employee and are excluded.
* The employer’s administrative payroll costs, voluntary benefits and insurance premiums are not statutory payroll levies and are excluded.
* Exact monthly withholding may differ by cents from the annual results. Final PIT is the annual-assessment amount; a production payslip engine needs the current official monthly rounding and reporting rules.

## 6. Evidence assessment

**Strongest evidence.** The 2026 allowance and bracket figures come from the dedicated 2026 Ministry of Finance regulation in the Official Gazette. The long-term-care rates and OZP amounts come directly from ZZZS. The contribution floor comes from a dated 2026 FURS notice citing the exact ZPIZ-2 paragraph. The winter-regress amount and exemptions are stated directly in Articles 2, 4 and 5 of ZPZR.

**Weakest evidence / implementation caution.** The ordinary contribution-rate table is an undated but current government SPOT page rather than a 2026-dated rate decree. The January–February minimum base is derived mechanically as 60% of the official 2024 SURS average because the 2026 FURS notice explicitly states which year applies, rather than being printed as a separate FURS euro figure. Finally, the annual examples intentionally do not simulate monthly component rounding; the official sources establish annual assessment and monthly withholding, but the reviewed pages did not expose one complete, universal cents-level payroll algorithm.
