# Croatia — employee payroll research for income year 2026

**Method:** independent clean-room reconstruction from Croatian primary official sources only.
**Source access date:** 2026-10-04 for every link.
**Currency:** euro (EUR).

## Scope and reproducible assumptions

The employee is resident in the **City of Zagreb**, single, without children or other dependants, ordinarily employed full-time by one private employer for all of 2026, and paid regular cash salary in **12 equal monthly instalments**. There are no benefits in kind, deductible donations, disability, special-area relief, expatriate/returnee relief, first-employment relief, accelerated pension service, or voluntary third-pillar payment.

“Age 30” is not enough by itself to determine Croatia's young-person annual PIT reduction because the statute uses the whole tax year in which a person reaches the specified age. For the principal calculation this dossier makes the explicit reproducible assumption that the employee was **born in 1996 and turns 30 during 2026**. A person born in 1995 who is still 30 on part of 2026 turns 31 during that tax year and does not receive this relief; the table therefore also shows PIT before the youth reduction.

The employee is assumed to be mandatorily insured in pension pillars I and II. “Gross salary” excludes any optional Christmas/vacation award or contractual thirteenth salary.

## 1. Income tax in Zagreb

### 1.1 National base, allowance and bands

The **Zakon o izmjenama i dopunama Zakona o porezu na dohodak**, NN 152/2024, enacted 2024-12-13, published 2024-12-24 and effective 2025-01-01, amended:

* Article 14(1): basic personal allowance from €560 to **€600 monthly**;
* Article 19: annual boundary between the lower and higher rates to **€60,000**; and
* Article 24(3): payroll's corresponding monthly boundary to **€5,000**.

[Official Narodne novine text, Articles 2–5](https://narodne-novine.nn.hr/clanci/sluzbeni/2024_12_152_2505.html). For a full year, the assumed employee's personal allowance is therefore **€7,200**.

Under Articles 23–24 of the **Zakon o porezu na dohodak**, employment income is reduced first by mandatory employee contributions and then by the personal allowance; the employer calculates and withholds the advance at each payment. [Official original act, especially Articles 23–24](https://narodne-novine.nn.hr/clanci/sluzbeni/2016_12_115_2525.html), read with the later euro and 2025 amendments above.

Thus:

```text
employment income = gross salary − employee pension contributions
annual PIT base    = max(0, employment income − €7,200)
```

Croatia no longer has a separate municipal surcharge (*prirez*). National law fixes the bands and permits each local unit to elect rates within statutory ranges; the employee's residence determines the applicable local rates.

### 1.2 Zagreb rates verified for 2026

Zagreb's **“Odluka o visini poreznih stopa godišnjeg poreza na dohodak”**, adopted 2025-02-18, published in NN 28/2025 on 2025-02-19 and applicable from 2025-03-01, sets:

* lower rate: **23%**;
* higher rate: **33%**.

[Official Gazette PDF, Article 2 at page 1 lines 54–61](https://narodne-novine.nn.hr/eli/sluzbeni/2025/28/292/pdf). Zagreb's official finance page still lists that decision as **Službeni glasnik Grada Zagreba 7/25** among the city's current rules in 2026. [City of Zagreb finance office page](https://www.zagreb.hr/en/gradski-ured-za-financije/101506). No later superseding 2026 rate decision was identified.

For the assumed Zagreb resident, annual tax before age relief is:

```text
23% × min(PIT base, €60,000)
+ 33% × max(0, PIT base − €60,000)
```

### 1.3 Young-person annual reduction

Article 46 was amended by **Zakon o izmjenama i dopunama Zakona o porezu na dohodak**, NN 121/2019, published 2019-12-11 and applicable from 2020. It reduces annual PIT on employment salary:

* by 100% of the proportionate lower-rate liability for persons up to age 25; and
* by **50% of the proportionate lower-rate liability for persons aged 26–30**.

Article 46 also says the reduction applies for the entire tax period in which the person reaches the relevant age. [Official NN text, Article 13 inserting Article 46(2)–(4), lines 133–144](https://narodne-novine.nn.hr/clanci/sluzbeni/full/2019_12_121_2385.html). The government's **“Porezna reforma 2025”** confirms that the 26–30 reduction remains 50%. [Official government presentation, December 2024, youth-relief slide](https://vlada.gov.hr/UserDocsImages/2016/Sjednice/2024/Prosinac/47_sjednica_VRH/Porezna_reforma_2025.pdf).

For the born-1996 assumption:

```text
youth reduction = 50% × tax charged at Zagreb's lower rate
                = 50% × 23% × min(PIT base, €60,000)
final annual PIT = tax before relief − youth reduction
```

It does **not** halve the 33% slice. The reduction is an annual-liability rule and is normally realized through the annual special assessment/refund; it should not be confused with ordinary monthly withholding. A born-1995 employee gets no youth reduction in 2026, so “tax before relief” is their final PIT on these facts.

## 2. Employee pension contributions

### 2.1 Pillar allocation

The official government page **“Sustav mirovinskog osiguranja”** states that pillars I and II are mandatory, contributions are withheld from gross salary, and a member of both pays **15% to pillar I** (intergenerational solidarity) and **5% to pillar II** (individual capitalised savings). [gov.hr pension-system page, “Drugi stup”](https://gov.hr/hr/sustav-mirovinskog-osiguranja/846). The Ministry's **“Kapitalizirana štednja (II. i III. stup)”** also distinguishes a person insured only in pillar I (20%) from a pillar-I-and-II member (15% + 5%) and confirms pillar III is voluntary. [Ministry/REGOS page](https://mss.gov.hr/print.aspx?id=116&url=print).

At age 30 the assumed worker belongs to both mandatory pillars. The employee can select or change the compulsory pension fund, but that does not change the 5% payroll rate. A choice between an all-pillar-I pension and combined pillar-I/pillar-II benefits arises on retirement; it is not a payroll-rate election. REGOS's official new-employee notice gives a one-month period to select a compulsory fund. [REGOS, “Obavijest novozaposlenima”](https://mss.gov.hr/kapitalizirana-stednja-ii-i-iii-stup/obavijest-novozaposlenima-157/157).

### 2.2 2026 floors and ceilings

The Ministry of Finance **“Naredba o iznosima osnovica za obračun doprinosa za obvezna osiguranja za 2026. godinu”**, NN 150/2025, signed 2025-12-03, published 2025-12-12, effective the day after publication and applicable to January–December 2026, gives:

* minimum monthly base, Article 3: **€757.34**;
* maximum monthly base, Article 4: **€11,958.00**;
* maximum annual base, Article 5: **€143,496.00**.

[Official 2026 order, Articles 2–5 and 20–21](https://narodne-novine.nn.hr/clanci/sluzbeni/2025_12_150_2237.html).

The contribution act is important to applying these figures correctly:

* Articles 204–205 say the **monthly maximum applies to both pillar-I and pillar-II pension contributions on salary**;
* Articles 206–208 say the annual maximum applies to pillar-I solidarity contributions and explain when an employer or the Tax Administration may apply it.

[Official **Zakon o doprinosima**, Articles 204–208](https://narodne-novine.nn.hr/clanci/sluzbeni/2008_07_84_2716.html). Because the scenario pays equal monthly salary, the effective base for each pillar is:

`pension base = min(annual gross salary, 12 × €11,958 = €143,496)`.

Employee pension contributions therefore equal:

`15% × capped base + 5% × capped base = 20% × capped base`.

This equal-pay result must not be generalized to irregular bonuses without applying the monthly and annual rules separately. Every sample monthly salary exceeds the €757.34 minimum; no minimum-base top-up arises.

## 3. Employer health contribution and cost

The **Zakon o izmjenama i dopunama Zakona o doprinosima**, NN 106/2018, enacted 2018-11-21, published 2018-11-30 and effective 2019-01-01, changed Article 14's health rate from 15% to **16.5%** and removed the separate employment and work-injury contribution structure. [Official NN text, amendment to Article 14](https://narodne-novine.nn.hr/clanci/sluzbeni/full/2018_11_106_2063.html). The current government Invest Croatia payroll page likewise identifies pension deductions of 15% + 5% and employer health of 16.5%. [Government investment portal, “Plaće”](https://investcroatia.gov.hr/zaposljavanje/place/).

For ordinary employment, employer health is calculated on full gross salary and is not subject to the pension maximum:

`employer health = 16.5% × gross salary`.

No separate universal employer unemployment, work-injury, payroll, or solidarity percentage is added under the current contribution structure. Accordingly:

`ordinary employer cost = gross salary + employer health`.

There are two material but non-assumed exceptions:

* From 2025, a qualifying person entering their first indefinite employment can produce a one-year employer health exemption. The official government payroll page describes the condition and one-year duration. The worker's history is not supplied, so the examples conservatively use the ordinary 16.5%.
* **Zakon o izmjenama Zakona o doprinosima**, NN 152/2024, effective 2025-01-01, ended new general young-person exemptions but Article 5 preserves an exemption already begun before the amendment. [Official act, Articles 2–5 and 9](https://narodne-novine.nn.hr/clanci/sluzbeni/full/2024_12_152_2506.html). No transitional exemption is assumed.

## 4. Thirteenth salary, holiday pay and occasional awards

Croatian labour law does not establish a universal private-sector thirteenth salary or cash holiday/Christmas award. Article 90a of the **Zakon o radu**, inserted by NN 151/2022 (published 2022-12-22, effective 2023-01-01), describes *regres*, Christmas awards and similar material rights as payments made where provided by legislation, collective agreement, work rules, employer act, or employment contract, and says they are not salary for Labour Act classification. [Official amendment, Article 35 inserting Articles 90a–90b](https://narodne-novine.nn.hr/clanci/sluzbeni/2022_12_151_2343.html).

The tax treatment is distinct from entitlement. The **Pravilnik o izmjenama i dopunama Pravilnika o porezu na dohodak**, NN 143/2023, published 2023-12-01 and effective 2023-12-02, sets a combined exemption of up to **€700 annually** for occasional awards such as Christmas bonus and vacation allowance. [Official regulation, table item 5 and JOPPD item 22](https://narodne-novine.nn.hr/clanci/sluzbeni/2023_12_143_1956.html). This is a ceiling, not a mandatory payment.

Any contractual “13th salary” paid as remuneration for work, or an award exceeding/without satisfying an exemption, is taxable salary and generally subject to contributions. Because no such right or amount is specified, the worked examples include none. An irregular payment also requires separate testing of the pension monthly/annual ceilings rather than simply using the equal-month formula below.

## 5. Worked annual calculations

Let `G` be regular annual gross salary and `C = min(G, €143,496)` under the equal-12-month assumption:

```text
pillar I contribution       = 15% × C
pillar II contribution      =  5% × C
employee pension total E    = 20% × C
employment income D         = G − E
personal allowance          = €7,200
annual PIT base T           = max(0, D − €7,200)
ordinary Zagreb PIT P0      = 23% × min(T, €60,000)
                            + 33% × max(0, T − €60,000)
youth reduction Y           = 50% × 23% × min(T, €60,000)
final PIT P                  = P0 − Y
annual net                   = G − E − P
employer health H           = 16.5% × G
employer cost               = G + H
```

Amounts are rounded to cents at the annual presentation level:

| Gross G | Pension base C | Pillar I 15% | Pillar II 5% | Employee pension E | Income D | Allowance | PIT base T | PIT before youth relief P0 | Youth reduction Y | Final PIT P | Annual net | Employer health | Employer cost |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| €20,000.00 | €20,000.00 | €3,000.00 | €1,000.00 | €4,000.00 | €16,000.00 | €7,200.00 | €8,800.00 | €2,024.00 | €1,012.00 | **€1,012.00** | **€14,988.00** | €3,300.00 | **€23,300.00** |
| €60,000.00 | €60,000.00 | €9,000.00 | €3,000.00 | €12,000.00 | €48,000.00 | €7,200.00 | €40,800.00 | €9,384.00 | €4,692.00 | **€4,692.00** | **€43,308.00** | €9,900.00 | **€69,900.00** |
| €100,000.00 | €100,000.00 | €15,000.00 | €5,000.00 | €20,000.00 | €80,000.00 | €7,200.00 | €72,800.00 | €18,024.00 | €6,900.00 | **€11,124.00** | **€68,876.00** | €16,500.00 | **€116,500.00** |
| €200,000.00 | €143,496.00 | €21,524.40 | €7,174.80 | €28,699.20 | €171,300.80 | €7,200.00 | €164,100.80 | €48,153.26 | €6,900.00 | **€41,253.26** | **€130,047.54** | €33,000.00 | **€233,000.00** |
| €600,000.00 | €143,496.00 | €21,524.40 | €7,174.80 | €28,699.20 | €571,300.80 | €7,200.00 | €564,100.80 | €180,153.26 | €6,900.00 | **€173,253.26** | **€398,047.54** | €99,000.00 | **€699,000.00** |

Bracket checks:

* €20,000: `P0 = 23% × €8,800 = €2,024`; half lower-rate reduction €1,012.
* €60,000: `P0 = 23% × €40,800 = €9,384`; half reduction €4,692.
* €100,000: `P0 = 23% × €60,000 + 33% × €12,800 = €18,024`; reduction is half of €13,800, or €6,900.
* €200,000: `P0 = €13,800 + 33% × €104,100.80 = €48,153.264`; final €41,253.264.
* €600,000: `P0 = €13,800 + 33% × €504,100.80 = €180,153.264`; final €173,253.264.

For the age-ambiguous alternative (born in 1995 and turning 31 during 2026), final PIT equals column `P0`, and annual net equals respectively **€13,976.00, €38,616.00, €61,976.00, €123,147.54, and €391,147.54**.

## 6. Calculation order, payroll timing and rounding

For each regular monthly payment the employer:

1. caps the pension salary base at €11,958 and withholds pillar I and II contributions;
2. subtracts contributions and the €600 monthly personal allowance shown on the employee's tax card;
3. applies Zagreb's 23% rate through €5,000 monthly taxable base and 33% above it;
4. pays net salary and reports/settles the liabilities; and
5. separately pays 16.5% employer health on gross salary.

Annual assessment reconciles annual taxable income and reliefs. The age-30 reduction is shown as an annual reduction/refund, so in-year payslip cash can be lower than the final annual net displayed here. Monthly component rounding can also create cents differences from annual multiplication. The reviewed primary sources establish the order and limits but were not used to invent a single unsupported cents-rounding convention.

## 7. Universal versus conditional rules

### Included for the stated case

* Zagreb location-specific rates of 23% and 33%, annual boundary €60,000;
* €600 monthly / €7,200 annual personal allowance;
* 15% pillar I plus 5% pillar II withheld from salary;
* €11,958 monthly pension ceiling for each pillar under equal monthly salary;
* 16.5% employer health on full gross;
* 50% annual reduction of the lower-rate PIT component for a person born in 1996 who reaches age 30 in 2026.

### Conditional or unresolved without more facts

* A birth year of 1995 removes the young-person PIT reduction even if the employee is age 30 for part of 2026.
* First-indefinite-employment or preserved pre-2025 employer-health exemptions depend on employment history and commencement date.
* A person insured only in pillar I pays 20% there instead of the assumed 15% + 5% split; that is not the ordinary age-30 case.
* A fund choice changes where pillar-II assets are invested, not take-home pay.
* Thirteenth salary, vacation/Christmas awards and other material rights depend on the applicable agreement or employer act. The €700 rule is only a tax exemption ceiling.
* Irregular bonuses, multiple employers, partial months, unpaid leave, and salary relating to another period can change how the monthly and annual contribution ceilings operate.

## 8. Evidence assessment

**Strongest evidence.** The exact 2026 contribution bases are in the dedicated Ministry of Finance 2026 order. Zagreb's 23%/33% rates are in its operative decision and corroborated by the city's current legislation page. The €600 allowance and €60,000 band are explicit amendments in NN 152/2024. The contribution law expressly distinguishes the monthly two-pillar ceiling from the annual pillar-I ceiling.

**Weakest evidence / implementation caution.** Croatia publishes a base act plus many amending acts rather than one conveniently consolidated 2026 payroll table; the 16.5% health rate therefore relies on the exact NN 106/2018 amendment plus a current government payroll page. “Age 30” is inherently under-specified without birth year, which is why both born-1996 and born-1995 outcomes are disclosed. Finally, monthly statutory rounding was not independently reduced to a cents-perfect annual simulation; the examples are annual-liability calculations under equal monthly pay.
