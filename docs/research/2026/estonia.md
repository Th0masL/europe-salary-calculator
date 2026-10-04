# Estonia employee payroll — tax year 2026

Clean-room research dossier. Access date for every online source: **2026-10-04**.

## Scope and modelled employee

This dossier reconstructs the payroll of an Estonian-resident employee from Estonian primary sources only. It does not rely on calculator code, generated data, an earlier country dossier, or an audit.

The worked examples assume:

- a resident natural person who is **below pensionable age throughout 2026**;
- one ordinary private-sector employment contract, continuously active for all 12 months;
- regular cash salary paid in 12 monthly instalments during 2026;
- no children and no other income or deductions;
- a written application asking the sole employer to apply the full basic exemption of €700 each month;
- active membership of the mandatory funded pension (second pillar), at the statutory/default **2% employee rate**; and
- no sickness, injury, quarantine, unpaid leave, fringe benefits, or cross-border social-security facts.

Age and second-pillar membership are material variables. The prompt supplies neither age nor birth year, so the examples deliberately choose a working-age second-pillar member. A person who has left or has not joined the second pillar has no 2%/4%/6% withholding; a member who elected 4% or 6% has a different net salary. Pensionable-age employees also have a different basic exemption and cease paying employee unemployment insurance in the month specified below.

All examples are annual economic calculations. Actual payroll is calculated per payment and statutory amounts are rounded to cents, so monthly payment splits can create cent-level differences. The annual income-tax return reconciles the basic exemption and deductible employee social-security contributions.

## 1. Rules in force for 2026

### 1.1 Income tax

The general personal income-tax rate is **22%**. The consolidated Income Tax Act §4(1) says that, apart from listed exceptions, “the rate of income tax is 22%”; §3(1) makes the natural-person tax period the calendar year. The official consolidation identifies the wording as in force **2026-01-01 through 2026-12-31**, with the English translation published **2025-12-30**.[^ita]

For a resident below pensionable age, Income Tax Act §23(1) gives a fixed **€8,400 annual basic exemption** from 2026. It does not taper with income. EMTA’s 2026 “Tax rates” panel states the payroll equivalent: **€700 per month / €8,400 per year**, and explicitly says it no longer decreases as income rises.[^rates]

The tax base for the assumptions here is therefore:

```text
employee unemployment premium U = gross cash salary G × 1.6%
employee funded-pension contribution P = G × 2%
annual taxable income T = max(0, G − U − P − 8,400)
annual income tax I = T × 22%
```

The deduction order is statutory, not an inference from a net-pay calculator:

- Income Tax Act §28¹(1) deducts mandatory funded-pension contributions from a resident natural person’s annual income, and §28¹(2) deducts withheld unemployment-insurance premiums.[^ita-deductions]
- For payroll withholding, Income Tax Act §42(5) says to deduct the employee unemployment premium before calculating withholding; §42(6) says the same for the mandatory funded-pension contribution.[^ita-withholding]
- Section 42(1) permits up to one-twelfth of the annual basic exemption each month on the taxpayer’s written application.[^ita-withholding]

There is no progressive salary bracket in this model: after the deductions and fixed exemption, the remaining employment income is taxed at 22%.

### 1.2 Basic-exemption election and annual reconciliation

The annual exemption is an entitlement; applying it during payroll is an election:

- EMTA, “Calculation of basic exemption,” last updated **2026-06-26**, says the employee must give the employer a written application. Only one employer/payer may apply it at a time. Without an application, the employer withholds income tax from the first euro.[^basic]
- The employee can request any monthly amount from €0 through €700. If pay is too low, payroll applies only the usable amount.[^basic]
- Unused exemption cannot be carried to another payroll month, advanced, or accumulated. On the annual return, however, the full annual amount up to €8,400 can be applied.[^basic]
- If too much was applied by payers, the annual return produces additional tax; if none or too little was used, the annual return produces a refund. EMTA states the refund/additional-payment deadline as no later than 1 October of the following year.[^basic]

Because every worked salary exceeds €700 after employee contributions in every regular month, the examples use all €8,400 during payroll as well as in the annual final calculation.

For completeness, EMTA gives a separate pensionable-age exemption of **€776 per month / €9,312 per year**. That case is outside the chosen assumptions.[^rates]

### 1.3 Employee unemployment insurance

Government Regulation No. 78, “Rates of unemployment insurance premium for insured persons and employers in 2026–2029,” adopted **2025-09-25**, published **2025-09-30**, effective **2026-01-01**, §1 fixes:

- insured employee: **1.6%**; and
- employer: **0.8%**

of the remuneration within Unemployment Insurance Act §40.[^ui-reg]

Unemployment Insurance Act §40(1)(1) includes wages, salaries, and other remuneration paid to insured persons. Section 42 requires the employer to withhold the insured-person share and pay the employer share; calculated premiums are rounded to one cent.[^uia]

For an ordinary working-age employee there is no employee salary cap in those provisions: both percentages apply to all covered salary. This “no cap” conclusion is a reading of the assessment base in §40 together with the rate regulation; the sources do not use a separate sentence labelled “no ceiling.”

The employee withholding ends on the last day of the month in which the employee reaches pensionable age or is granted early/flexible old-age pension. The employer’s 0.8% continues. EMTA states that distinction in its 2026 table.[^rates]

### 1.4 Mandatory funded pension (second pillar)

For a participating employee, Funded Pensions Act §9 provides a **2% default** rate and permits the person to choose **4% or 6%**. The selected higher rate remains valid for at least a calendar year.[^fpa]

The model uses 2%. This is reproducible because:

- EMTA says 2%, 4%, or 6% applies according to the person’s choice, and 2% is the default if no higher-rate application was made;[^rates]
- Pensionikeskus, “Changing the contribution rate to 2%, 4% or 6%,” says the higher rate is voluntary and 2% remains the default; an application received by 30 November applies from the following 1 January, while a December application applies from January of the year after that.[^pk]

The employer withholds the member’s selected percentage from gross remuneration. EMTA’s “Contributions to mandatory funded pension,” last updated **2025-01-06**, explains that the Tax and Customs Board adds another **4% of gross salary out of the 33% social tax**. That 4% does **not** increase employer cost: it is an allocation from social tax, and remains 4% regardless of whether the employee elects 2%, 4%, or 6%.[^pension]

Membership itself is not universal. EMTA instructs employers to check obligation changes on 1 January, 1 May, and 1 September. The examples assume continuous membership for all of 2026.[^pension]

No salary cap applies to an employee’s funded-pension withholding under Funded Pensions Act §§7–9. EMTA separately describes a cap for a **self-employed person**, confirming that cap is a different regime and is not imported into employee payroll.[^fpa][^pension-self]

### 1.5 Employer social tax and its monthly minimum

Social Tax Act §7(1) sets the ordinary rate at **33%** of the taxable amount. Section 8 makes the taxable period a calendar month.[^sta]

For an employment contract, §2(2) generally requires social tax on the month’s remuneration but on no less than the statutory monthly base. EMTA’s “Social tax,” last updated **2026-07-20**, fixes the 2026 minimum base at **€886**, hence a minimum monthly employer liability of **€292.38** (`886 × 33%`).[^social]

Thus, for a full month under the model assumptions:

```text
employer social tax S = 33% × max(monthly gross salary, €886)
```

The statute contains exceptions and proportional rules—for example certain pensioners, persons with reduced work ability, students, short employment periods, and multiple-employer cases. These are not modelled. The ordinary minimum also applies during some months with no cash wage, such as unpaid leave, unless an exception applies.[^social-min]

Each requested salary is above the floor even if paid evenly monthly:

| Annual gross | Regular monthly gross | Above €886? |
|---:|---:|:---:|
| €20,000 | €1,666.67 | yes |
| €60,000 | €5,000.00 | yes |
| €100,000 | €8,333.33 | yes |
| €200,000 | €16,666.67 | yes |
| €600,000 | €50,000.00 | yes |

Accordingly, the minimum does not alter any worked example and annual social tax is simply 33% of annual gross. The employee does not separately pay a health-insurance contribution: state health insurance is financed within employer social tax; EMTA describes the 33% social tax as financing pension and state health insurance.[^social]

No employee salary ceiling applies to ordinary employer social tax. The separate statutory cap EMTA describes for self-employed business income is not an employee cap.[^pension-self]

### 1.6 Employer sickness and other non-percentage costs

Occupational Health and Safety Act §12²(1) requires the employer to pay **70% of the employee’s average wage for calendar days 4–8** of sickness, injury, or quarantine. The cited English consolidation was in force from **2026-04-01 to 2026-07-12**, translation published **2026-03-19**; the operative day-4-to-8 wording has applied since **2023-07-01**.[^ohsa]

Tervisekassa’s “Comparison of benefits for incapacity for work,” last updated **2026-07-10**, independently confirms employer payment on days 4–8 and Tervisekassa payment from day 9 at 70% for ordinary illness/domestic injury.[^sick]

This is a statutory but contingent employer cost. It cannot be converted into a universal annual payroll percentage without employee-specific absence data. It is therefore shown as **€0 in the no-sickness worked scenario**, not asserted to be generally zero.

The qualifying sickness benefit is exempt from social tax under Social Tax Act §3(3). Voluntary top-ups are possible under Occupational Health and Safety Act §12³ but are not a universal mandatory charge.[^sta][^ohsa]

Ordinary paid annual leave is not added as a percentage to the requested regular annual cash salary: paid leave changes when salary is paid, not the agreed annual salary amount in this model. Occupational-health/safety compliance and equipment can create employer costs, but they are workplace-specific rather than a fixed payroll levy. No separate universal employer accident-insurance premium was identified in the cited payroll statutes.

## 2. Calculation order

For each cash salary payment to the modelled employee:

1. Determine gross taxable remuneration.
2. Withhold employee unemployment insurance at 1.6%.
3. Withhold the employee’s default funded-pension contribution at 2%.
4. Deduct both withholdings and the elected basic exemption (up to €700 for that calendar month) before calculating income-tax withholding.
5. Withhold 22% income tax on the non-negative remainder.
6. Net cash pay equals gross less the two employee contributions and income tax.
7. Separately, the employer pays 33% social tax, subject to the €886 monthly minimum base, plus employer unemployment insurance at 0.8%.
8. Declare/pay the relevant monthly amounts on the TSD cycle. EMTA notes taxation is **cash-based**: the rates depend on when remuneration is paid, not the work period.[^rates]
9. Reconcile the calendar year on the resident individual’s income-tax return. Full-year deductible contributions and the annual €8,400 exemption determine final tax.

Under the no-sickness, full-year, above-minimum assumptions, let annual gross be `G`:

```text
U = 0.016G
P = 0.020G
B = 8,400
T = max(0, G − U − P − B)
I = 0.22T
Net = G − U − P − I

Employer social tax = 0.33G
Employer unemployment insurance = 0.008G
Regular employer cost = G + 0.33G + 0.008G = 1.338G

Second-pillar state allocation (informational, already inside social tax) = 0.04G
```

There is no double counting of the 4% state allocation in employer cost.

## 3. Independent worked calculations

### €20,000 annual gross

```text
Gross salary                                      €20,000.00
Employee unemployment insurance: 20,000 × 1.6%      −320.00
Employee funded pension: 20,000 × 2%                 −400.00
Annual basic exemption                              −8,400.00
Income-tax base                                     10,880.00
Income tax: 10,880 × 22%                            −2,393.60
Net employee cash                                  €16,886.40

Employer social tax: 20,000 × 33%                   €6,600.00
Employer unemployment: 20,000 × 0.8%                  160.00
Regular employer cost                              €26,760.00
State 4% pension allocation (inside social tax)       €800.00
```

The regular monthly gross is about €1,666.67, so the €886 social-tax minimum base does not apply.

### €60,000 annual gross

```text
Gross salary                                      €60,000.00
Employee unemployment insurance: 60,000 × 1.6%      −960.00
Employee funded pension: 60,000 × 2%               −1,200.00
Annual basic exemption                              −8,400.00
Income-tax base                                     49,440.00
Income tax: 49,440 × 22%                           −10,876.80
Net employee cash                                  €46,963.20

Employer social tax: 60,000 × 33%                  €19,800.00
Employer unemployment: 60,000 × 0.8%                  480.00
Regular employer cost                              €80,280.00
State 4% pension allocation (inside social tax)     €2,400.00
```

### €100,000 annual gross

```text
Gross salary                                     €100,000.00
Employee unemployment insurance: 100,000 × 1.6%   −1,600.00
Employee funded pension: 100,000 × 2%              −2,000.00
Annual basic exemption                              −8,400.00
Income-tax base                                     88,000.00
Income tax: 88,000 × 22%                           −19,360.00
Net employee cash                                  €77,040.00

Employer social tax: 100,000 × 33%                 €33,000.00
Employer unemployment: 100,000 × 0.8%                 800.00
Regular employer cost                             €133,800.00
State 4% pension allocation (inside social tax)     €4,000.00
```

### €200,000 annual gross

```text
Gross salary                                     €200,000.00
Employee unemployment insurance: 200,000 × 1.6%   −3,200.00
Employee funded pension: 200,000 × 2%              −4,000.00
Annual basic exemption                              −8,400.00
Income-tax base                                    184,400.00
Income tax: 184,400 × 22%                          −40,568.00
Net employee cash                                 €152,232.00

Employer social tax: 200,000 × 33%                 €66,000.00
Employer unemployment: 200,000 × 0.8%               1,600.00
Regular employer cost                             €267,600.00
State 4% pension allocation (inside social tax)     €8,000.00
```

### €600,000 annual gross

```text
Gross salary                                     €600,000.00
Employee unemployment insurance: 600,000 × 1.6%   −9,600.00
Employee funded pension: 600,000 × 2%             −12,000.00
Annual basic exemption                              −8,400.00
Income-tax base                                    570,000.00
Income tax: 570,000 × 22%                         −125,400.00
Net employee cash                                 €453,000.00

Employer social tax: 600,000 × 33%                €198,000.00
Employer unemployment: 600,000 × 0.8%               4,800.00
Regular employer cost                             €802,800.00
State 4% pension allocation (inside social tax)    €24,000.00
```

### Cross-check table

| Annual gross | Employee UI | Employee II pillar | Tax base after €8,400 | Income tax | Net cash | Employer social tax | Employer UI | Regular employer cost |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| €20,000.00 | €320.00 | €400.00 | €10,880.00 | €2,393.60 | €16,886.40 | €6,600.00 | €160.00 | €26,760.00 |
| €60,000.00 | €960.00 | €1,200.00 | €49,440.00 | €10,876.80 | €46,963.20 | €19,800.00 | €480.00 | €80,280.00 |
| €100,000.00 | €1,600.00 | €2,000.00 | €88,000.00 | €19,360.00 | €77,040.00 | €33,000.00 | €800.00 | €133,800.00 |
| €200,000.00 | €3,200.00 | €4,000.00 | €184,400.00 | €40,568.00 | €152,232.00 | €66,000.00 | €1,600.00 | €267,600.00 |
| €600,000.00 | €9,600.00 | €12,000.00 | €570,000.00 | €125,400.00 | €453,000.00 | €198,000.00 | €4,800.00 | €802,800.00 |

## 4. Variables and exclusions a calculator must expose

These are not universal constants and should not be silently hard-coded as if they were:

- second-pillar participation status and effective start/end date;
- employee-selected second-pillar rate (2%, 4%, or 6%);
- pensionable-age status, which changes the basic exemption and employee unemployment premium;
- amount of monthly basic exemption requested from the employer (0–€700) and whether another payer applies it;
- pay timing, because Estonia uses a cash basis;
- months below the social-tax minimum, multiple-employer allocation, shortened months, and statutory exceptions;
- sickness/injury/quarantine days and average-wage base;
- cross-border A1/social-security coverage;
- voluntary benefits, occupational-health expenditure, fringe benefits, and employer-specific costs.

No fixed collective-agreement contribution, sector levy, employer pension premium in addition to the 33% social tax, or general salary contribution cap was identified for the ordinary employee described here.

## 5. Evidence assessment and unresolved points

**Strongest evidence.** The 22% rate, €8,400 exemption, and deduction order are stated directly in the consolidated Income Tax Act (§§3, 4, 23, 28¹, 42) and mirrored in EMTA’s 2026 material. The unemployment rates have a year-specific Government regulation. The funded-pension rates have both Funded Pensions Act §9 and matching EMTA/Pensionikeskus guidance. The 33% social tax and monthly minimum have both the Social Tax Act and a current 2026 EMTA page.

**Weakest evidence / limits.** The official provisions apply contributions to covered remuneration without naming an employee “maximum”; therefore the absence of an employee cap is a legal reading of the assessment provisions, not an explicit no-cap sentence. Exact cent results can vary with the actual monthly pay split and payroll rounding. The prompt does not give age/birth year or second-pillar history, so working age and continuous membership at the default 2% rate are explicit scenario choices rather than universal facts. A single annual sickness-cost amount is inherently unresolved without an absence event and average-wage facts.

## Primary sources

[^rates]: Estonian Tax and Customs Board (EMTA), [“Tax rates”](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates), section “Tax rates — 2026”: 22%; €700/€8,400; 33%; €886/€292.38; 1.6%/0.8%; 2%/4%/6% and default 2%; cash basis. Last updated **2026-03-26**. Effective values: **2026**. Accessed **2026-10-04**.

[^ita]: Riigi Teataja, [Income Tax Act](https://www.riigiteataja.ee/en/eli/ee/530012014003/consolide/current), §§3(1), 4(1), 23(1). Consolidated wording in force **2026-01-01–2026-12-31**; translation published **2025-12-30**. Section 23(1)’s €8,400 amendment entered into force **2026-01-01**. Accessed **2026-10-04**.

[^ita-deductions]: Riigi Teataja, [Income Tax Act, official English PDF](https://www.riigiteataja.ee/en/tolge/pdf/508052026001), §28¹(1)–(2), “Mandatory social security contributions”: deduction of mandatory funded-pension contributions and withheld unemployment premiums from resident annual income. Consolidation in force from **2026-05-09**; the relevant provisions predate 2026. Accessed **2026-10-04**.

[^ita-withholding]: Riigi Teataja, [Income Tax Act](https://www.riigiteataja.ee/en/eli/ee/530012014003/consolide/current), §42(1), (5), and (6), “Deductions to be made upon withholding of income tax.” Consolidated wording in force **2026-01-01–2026-12-31**; translation published **2025-12-30**. Accessed **2026-10-04**.

[^basic]: EMTA, [“Calculation of basic exemption”](https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/calculation-basic-exemption), sections “Application for basic exemption,” “Submission of income tax return and calculation of basic exemption per year,” and Q&A “Basic exemption cannot be summed up.” Last updated **2026-06-26**; 2026 rules effective **2026-01-01**. Accessed **2026-10-04**.

[^ui-reg]: Government of the Republic, Riigi Teataja, [Regulation No. 78, “Rates of unemployment insurance premium for insured persons and employers in 2026–2029” (official text/PDF)](https://www.riigiteataja.ee/akt/130092025003.pdf), §1(1)–(2). Adopted **2025-09-25**, publication RT I, 30.09.2025, 3, effective **2026-01-01** (2026 wording remains applicable through 2026). Accessed **2026-10-04**.

[^uia]: Riigi Teataja, [Unemployment Insurance Act](https://www.riigiteataja.ee/en/eli/ee/504102022001/consolide), §§40–42, especially §40(1)(1) (wages/salaries/other remuneration), §42(1) (employer withholding/payment), and §42(3) (one-cent rounding). Current consolidated act; relevant assessment provisions in force for 2026. Accessed **2026-10-04**.

[^fpa]: Riigi Teataja, [Funded Pensions Act](https://www.riigiteataja.ee/en/eli/ee/502012024002/consolide), §§7–9, particularly §9(1)–(3): 2% unless another rate is chosen; 4%/6% options. The rate-choice amendment entered into force **2024-01-01**. Accessed **2026-10-04**.

[^pk]: Pensionikeskus, [“Makse määra muutmine 2%, 4% või 6%” (“Changing the contribution rate to 2%, 4% or 6%”)](https://www.pensionikeskus.ee/ii-sammas/sissemaksed/makse-maara-muutmine/), paragraphs under the title and “Maksemäära muutmise avaldus”: rates available from 2025, voluntary increase, default 2%, unchanged 4% social-tax allocation, annual deadlines. Page displays no publication/update date; rule effective from **2025-01-01**. Accessed **2026-10-04**.

[^pension]: EMTA, [“Contributions to mandatory funded pension”](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/contributions-mandatory-funded-pension), bullets under the title and sections “Starting and ending dates for withholding of payment,” “Withholding of payment,” and “Amendment … as of 1 January 2025”: 2%/4%/6%, employer withholding, 4% added from social tax, default 2%, and change timing. Last updated **2025-01-06**; still-current rules applicable in 2026. Accessed **2026-10-04**.

[^pension-self]: EMTA, [“Contribution to mandatory funded pension”](https://www.emta.ee/en/admin/content/handbook_article/89), section on the **self-employed person’s** 2026 maximum. Last updated **2026-07-19**. This source is used only to distinguish the FIE cap from employee payroll. Accessed **2026-10-04**.

[^sta]: Riigi Teataja, [Social Tax Act](https://www.riigiteataja.ee/en/eli/ee/530122024006/consolide/current), §§2(2), 2¹, 3(3), 7(1), and 8(1): employment minimum base, setting of monthly rate, sickness-benefit exemption, ordinary 33% rate, monthly tax period. The §7(1) 33% provision is in force for 2026. Accessed **2026-10-04**.

[^social]: EMTA, [“Social tax”](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax), opening paragraph and “Monthly rate on which the minimum social tax liability is based”: 33%, purpose, €886 base and €292.38 monthly liability. Last updated **2026-07-20**. Accessed **2026-10-04**.

[^social-min]: EMTA, [“Social tax”](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/social-tax), employee minimum-liability examples and exceptions under Social Tax Act §2(4), including the 2026 €886 floor; last updated **2026-07-20**. Also EMTA, [TSD example 3: salary below the social-tax monthly rate](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/submission-declaration-form-tsd/naide-3-tootasu-alla-sotsiaalmaksu-kuumaara), worked €600 salary / €886 base example, last updated **2026-01-06**. Accessed **2026-10-04**.

[^ohsa]: Riigi Teataja, [Occupational Health and Safety Act, official English consolidated text](https://www.riigiteataja.ee/public-api/api/v1/en/akt/519032026001/blob-html), §12²(1) and §12³. Cited consolidation in force **2026-04-01–2026-07-12**, translation published **2026-03-19**; §12²(1) wording effective **2023-07-01**. Accessed **2026-10-04**.

[^sick]: Estonian Health Insurance Fund (Tervisekassa), [“Comparison of benefits for incapacity for work”](https://tervisekassa.ee/en/comparison-benefits-incapacity-work), table rows “Illness or domestic injury” and “Quarantine.” Last updated **2026-07-10**. Accessed **2026-10-04**.
