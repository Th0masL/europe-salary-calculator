# Romania employee payroll, income year 2026 — clean-room research dossier

**Scope and access date.** This dossier was reconstructed independently from Romanian primary official sources and legislation, accessed **2026-10-04**. It models a Romanian-resident employee, age 30, single, no children or dependants, working an ordinary full-time private-sector main job under normal working conditions, with regular cash salary paid in 12 monthly instalments. It excludes benefits in kind, vouchers, pension/disability exemptions, special/arduous working conditions, and secondments. The five requested salaries are all high enough that the ordinary personal deduction and the special minimum-wage exemption are zero.

## Reproducible result

For the stated employee and the requested salaries, let annual gross cash salary be \(G\):

```text
employee CAS       = 25% × G
employee CASS      = 10% × G
personal deduction = 0
PIT base           = G − CAS − CASS = 65% × G
PIT                = 10% × PIT base = 6.5% × G
employee deductions= 41.5% × G
net cash salary    = 58.5% × G
employer CAM       = 2.25% × G
employer cost      = 102.25% × G
```

Employment salary has no general upper contribution ceiling: CAS, CASS and CAM continue on the full salary. Consequently the same marginal percentages apply to every requested case. This is distinct from annual thresholds/caps found elsewhere in the Fiscal Code for some non-employment income.

## Statutory rules

### Salary income and calculation order

The official consolidated **Law no. 227/2015 on the Fiscal Code** defines salary income broadly in Article 76(1): cash or in-kind income obtained by a resident or non-resident carrying out activity under an individual employment contract, regardless of the income's name or the form in which it is granted. The law was originally published in *Monitorul Oficial* no. 688 of 10 September 2015; the official consolidated text records amendments through 2026. [Official consolidated Fiscal Code, Article 76](https://legislatie.just.ro/Public/FormaPrintabila/00000G0ULE201QFJAE81YU76CHBAI7U1); [official legislation record and consolidation history](https://legislatie.just.ro/Public/DetaliiDocumentAfis/234680).

For an employee's **main job**, Article 78(2)(a) makes monthly payroll tax final and specifies the order: gross salary minus mandatory social contributions attributable to the month, minus the Article 77 personal deduction and any other expressly permitted deductions, then 10% income tax. [Fiscal Code, Article 78, official printable text](https://legislatie.just.ro/Public/FormaPrintabila/00000G0M0J2BGUHO14B1RISKWLGR65WN) (pinpoint: paragraph (2)(a), 10% applied to the monthly calculation base).

Thus, absent a personal deduction or other deductions:

\[
\text{PIT}=10\%\times(\text{gross}-\text{CAS}-\text{CASS}).
\]

### Personal income tax and personal deduction

- **PIT rate:** 10% of the Article 78 monthly taxable base.
- **Basic personal deduction:** Article 77 allows it only at the declared main job and only where monthly gross income is no more than the applicable national minimum gross salary plus RON 2,000. It is a deduction from the PIT base, not a cash credit and not a reduction of CAS/CASS.
- For **zero dependants**, the deduction is 20% of the minimum wage where monthly gross is no more than the minimum wage. Above the minimum, its percentage falls by 0.5 percentage point for every commenced RON 50 band; it reaches zero in the `minimum + 1,951…2,000` band and is unavailable above `minimum + 2,000`.
- A compact reproduction of the statutory zero-dependant table is, with monthly gross \(m\) and minimum wage \(s\):

\[
D(m,s)=
\begin{cases}
0.20s,&m\le s\\
s\,[0.20-0.005\lceil(m-s)/50\rceil],&s<m\le s+2{,}000\\
0,&m>s+2{,}000.
\end{cases}
\]

Article 77 also provides a supplementary deduction of 15% of the minimum wage for employees up to age 26. It does **not** apply to this age-30 employee. [Fiscal Code Article 77 as replaced by Government Ordinance no. 16/2022, official text](https://legislatie.just.ro/Public/FormaPrintabila/00000G121RF28BQKOIT1ZQLBGKGIN00V) (published 15 July 2022; effective for income beginning January 2023; pinpoint: paragraphs (1), (2), table, and (10)(a)).

The relevant 2026 monthly minimum wages and therefore zero-dependant deduction bounds are:

| Period | National minimum gross wage | Maximum zero-dependant deduction | Deduction unavailable above |
|---|---:|---:|---:|
| 1 Jan–30 Jun 2026 | RON 4,050 | RON 810 | RON 6,050 monthly gross |
| 1 Jul–31 Dec 2026 | RON 4,325 | RON 865 | RON 6,325 monthly gross |

The second-half amount is set by **Government Decision no. 146/2026 establishing the guaranteed minimum gross basic salary**, adopted 12 March 2026, published in *Monitorul Oficial* no. 196 of 13 March 2026, effective 1 July 2026: RON 4,325 per month for 166.667 hours, or RON 25.949/hour. It repeals Government Decision no. 1506/2024 from that date. [HG 146/2026, Articles 1–2, official text](https://legislatie.just.ro/Public/FormaPrintabila/00000G08T1O29AS01P33TVD30CAHKX4U). The RON 4,050 first-half amount and the July increase are also reflected in **Emergency Ordinance no. 89/2025**, adopted 23 December and published 24 December 2025. [OUG 89/2025, official record](https://legislatie.just.ro/Public/DetaliiDocumentAfis/307679).

### Employee social insurance

For ordinary salary under normal working conditions:

- **CAS (pension/social insurance): 25%** of gross salary, borne by the employee. Fiscal Code Article 138(a) specifies 25%; the official Constitutional Court record reproduces the operative rates. [Decision no. 650/2020, official text, pinpoint quoting Article 138(a)](https://legislatie.just.ro/Public/DetaliiDocument/235512).
- **CASS (health insurance): 10%** of gross salary, borne by the employee. [Fiscal Code Article 156, official amended text, pinpoint paragraph setting 10%](https://legislatie.just.ro/public/DetaliiDocument/272286).
- The salary contribution bases in the Fiscal Code do not impose a general maximum on ordinary employment salary. The sample calculations therefore apply both contributions to all gross cash salary.

The employer withholds the employee amounts. Extra employer CAS of 4% or 8% can arise for legally classified special or other working conditions; it is not universal and is excluded by the ordinary-office/normal-conditions assumption.

### Employer work-insurance contribution (CAM)

Fiscal Code Article 220^3 sets the **contribuția asiguratorie pentru muncă** at **2.25%**. The employer bears it on salary remuneration within the statutory base. [Emergency Ordinance no. 79/2017, Article I introducing Article 220^3, official text](https://legislatie.just.ro/Public/DetaliiDocumentAfis/194621) (adopted 8 November 2017, published in *Monitorul Oficial* no. 885 of 10 November 2017; effective 2018).

For an ordinary private employer, CAM is the universal payroll charge identified here. Employer cost in this model is therefore salary plus 2.25% CAM. Additional employer CAS for special working conditions and non-payroll obligations are employer/category specific and are not included.

### Minimum-wage exemption and minimum contribution bases

This is a separate rule from the Article 77 personal deduction. According to ANAF's **“Informaţii referitoare la suma minimă neimpozabilă în anul 2026”**, document no. GLR_CRP-83 of 21 January 2026:

- January–June: RON **300/month** is outside PIT and mandatory social-contribution bases where the employee has a full-time main job, the contractual basic salary is exactly the RON 4,050 minimum, and monthly gross income (with the source's stated exclusions for meal/vacation vouchers and food allowance) does not exceed RON **4,300**.
- July–December: the corresponding amount is RON **200/month**, for a basic salary at the RON 4,325 minimum and monthly gross not exceeding RON **4,600**.

[ANAF, “Informaţii referitoare la suma minimă neimpozabilă în anul 2026,” 21 January 2026](https://static.anaf.ro/static/3/Galati/20260123122801_suma%20neimpozabila%20in%202026.pdf) (pinpoint: the two period-specific bullet lists and eligibility conditions). The legal basis is [OUG 89/2025](https://legislatie.just.ro/Public/DetaliiDocumentAfis/307679), adopted 23 December 2025 and published in *Monitorul Oficial* no. 1203 of 24 December 2025.

Related minimum-contribution-base rules can require employer-paid differences for some low-paid employees, subject to statutory exceptions. They have no effect here: every requested monthly salary is well above both the minimum wage and the personal-deduction cutoff.

### Sector relief is not a universal 2026 rule

The former salary PIT/contribution facilities for software creation, construction, agriculture and food production must not be applied to an ordinary 2026 payroll. **Emergency Ordinance no. 156/2024**, adopted 30 December 2024 and published in *Monitorul Oficial* no. 1334 of 31 December 2024, repealed Fiscal Code Article 60 points 2, 5 and 7 and the connected Article 60^1 rules from January 2025. [OUG 156/2024, official text, pinpoint Article LXIV](https://legislatie.just.ro/Public/FormaPrintabila/00000G1RV53IFEZ9IE01ECQP7T67MUBZ).

Person-specific exemptions (for example, qualifying severe disability), special working-condition contributions, and any later targeted schemes remain outside this ordinary employee profile.

## Cash bonuses, meal benefits and holiday benefits

These items must not be conflated:

1. **Cash salary, annual bonus, 13th salary, cash holiday/vacation bonus.** Article 76(1)'s broad salary definition applies regardless of name, while the official methodological norms expressly include bonuses/rewards, annual awards and vacation pay in gross salary income. They ordinarily bear PIT, CAS, CASS and CAM like salary. [Fiscal Code Article 76(1)](https://legislatie.just.ro/Public/FormaPrintabila/00000G0ULE201QFJAE81YU76CHBAI7U1); [official Fiscal Code methodological norms, Article 76 examples](https://legislatie.just.ro/Public/DetaliiDocument/200819).
2. **Meal tickets.** Under the statutory benefit treatment they are salary-taxable and CASS-able, but excluded from CAS and CAM. ANAF's official contribution matrix records `TICHETE DE MASĂ: Impozit DA; CAS NU; CASS DA; CAM NU`. [ANAF, “Servicii ocazionale / tratament fiscal” table, pinpoint row “TICHETE DE MASĂ”](https://static.anaf.ro/static/10/Ploiesti/servicii_ocazionale.pdf). Law no. 296/2023 made meal and vacation vouchers exceptions to the general CASS exclusion for Article 76(4) benefits. [Law no. 296/2023, official text, Article III amendments to Article 157(2)](https://legislatie.just.ro/Public/DetaliiDocument/276245) (published 27 October 2023; relevant provisions effective 2024).
3. **Vacation vouchers.** In the ordinary statutory treatment they are PIT- and CASS-able but not CAS- or CAM-able; their legal availability and value are benefit/employer specific. They are not modeled as cash salary.
4. **Qualifying holiday gifts.** Cash or in-kind gifts offered on the narrowly specified occasions and to qualifying persons are non-taxable up to RON **300 per person per occasion** under Article 76(4)(a); the excess or a general cash bonus follows ordinary salary treatment. The RON 300 threshold was enacted by **OUG no. 130/2021**, adopted 17 December 2021, effective from 2022. [OUG 130/2021, official text, amendments to Article 76(4)(a)](https://legislatie.just.ro/public/detaliidocument/249349).

None of these vouchers or special gifts is included in the requested regular-gross-cash calculations.

## Worked calculations

All examples use 12 equal monthly payroll periods. At the lowest salary, monthly gross is RON 8,333.33, already above both the first-half RON 6,050 and second-half RON 6,325 personal-deduction limits. Therefore personal deduction is zero for every month and every case. The special RON 300/RON 200 minimum-wage exclusion is also unavailable.

| Annual gross \(G\) | Monthly gross \(G/12\) | CAS 25% | CASS 10% | Personal deduction | PIT base \(G-CAS-CASS\) | PIT 10% | Total employee deductions | Annual net | Employer CAM 2.25% | Total employer cost |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 100,000 | 8,333.33 | 25,000 | 10,000 | 0 | 65,000 | 6,500 | 41,500 | **58,500** | 2,250 | **102,250** |
| 300,000 | 25,000.00 | 75,000 | 30,000 | 0 | 195,000 | 19,500 | 124,500 | **175,500** | 6,750 | **306,750** |
| 500,000 | 41,666.67 | 125,000 | 50,000 | 0 | 325,000 | 32,500 | 207,500 | **292,500** | 11,250 | **511,250** |
| 1,000,000 | 83,333.33 | 250,000 | 100,000 | 0 | 650,000 | 65,000 | 415,000 | **585,000** | 22,500 | **1,022,500** |
| 3,000,000 | 250,000.00 | 750,000 | 300,000 | 0 | 1,950,000 | 195,000 | 1,245,000 | **1,755,000** | 67,500 | **3,067,500** |

Example at RON 100,000:

```text
CAS       = 100,000 × 0.25 = 25,000
CASS      = 100,000 × 0.10 = 10,000
PIT base  = 100,000 − 25,000 − 10,000 − 0 = 65,000
PIT       = 65,000 × 0.10 = 6,500
net       = 100,000 − 25,000 − 10,000 − 6,500 = 58,500
CAM       = 100,000 × 0.0225 = 2,250
cost      = 100,000 + 2,250 = 102,250
```

The remaining rows scale identically because there is neither a contribution cap nor a progressive salary PIT band in this fact pattern.

## Timing, annualisation and unresolved points

- Romanian employee PIT is calculated and withheld monthly and is final under Article 78. The table is an annual analytical reconstruction, not a claim that payroll is legally assessed only once a year.
- Equal monthly salary was assumed. Actual payroll software reports through Form 112 and rounds monthly declared amounts; allocating gross that is not exactly divisible by 12 can create small whole-leu differences from a pure annual multiplication. The official sources reviewed did not yield a single universal payroll-software rounding algorithm, so no unsupported rounding rule is imposed here.
- The exact CAM/CAS treatment of a non-cash benefit depends on the benefit's legal form and statutory limits. A label such as “holiday bonus” is insufficient: a cash bonus is salary, while qualifying gifts or vouchers can have the special treatments above.
- Accident/work-risk funding for an ordinary employer is embedded in CAM rather than modeled here as a separate universal employer percentage. Special/other working-condition CAS, collective-agreement benefits and sector-specific non-payroll costs require employer facts.

## Evidence assessment

**Strongest evidence.** The operative rates and calculation order are stated directly in the official consolidated Fiscal Code and official amending legislation: Article 78 (10% monthly final PIT and base), Article 138 (25% CAS), Article 156 (10% CASS), Article 220^3 (2.25% CAM), and Article 77's complete personal-deduction table. HG 146/2026 directly fixes the July 2026 minimum wage, while ANAF's dated January 2026 notice directly sets out the two 2026 minimum-wage exemption regimes.

**Weakest evidence / limits.** The ANAF benefit matrix is authoritative administrative guidance but is less durable than the Code and does not state a prominent publication date in its title; benefit treatment was therefore cross-checked against Law no. 296/2023 and Article 76. The dossier does not resolve employer-specific special-working-condition rates, non-statutory benefits, or a universal monthly software-rounding convention because those cannot be fixed from the stated facts without guessing.
