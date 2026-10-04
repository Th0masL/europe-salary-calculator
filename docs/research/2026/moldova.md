# Moldova employee payroll — income year 2026

**Research cut-off / access date:** 2026-10-04
**Currency:** Moldovan leu (MDL)
**Scope:** resident individual, age 30, single, no children, ordinary private-sector employment, regular cash salary, no special regime or employer incentive. This is a clean-room reconstruction from Moldovan government, SFS, CNAS and CNAM material. It is an annual model of twelve equal monthly salaries unless stated otherwise.

## Result in one page

For an ordinary private-sector employee in the stated facts:

- employee compulsory health-insurance premium (AOAM): **9%** of gross salary and other remuneration;
- income tax: **12%** of taxable employment income after the employee health premium and any permitted exemption/deduction;
- ordinary personal exemption: **MDL 29,700 per year**, but only where annual taxable income is **less than MDL 360,000**. There is no taper: the full exemption is lost at the threshold;
- employer state social-insurance contribution (BASS): **24%** of salary and other remuneration for the ordinary private-sector category;
- no employee BASS contribution, no separate employer health premium, and no separately stated accident-insurance payroll percentage apply to the ordinary case in the official 2026 schedules reviewed.

All five requested salaries fail the personal-exemption income test. Consequently, for these examples:

```text
H = 9% × G
pre-exemption taxable income T0 = G − H = 91% × G
personal exemption E = 0, because T0 ≥ 360,000
PIT = 12% × (T0 − E) = 10.92% × G
employee net = G − H − PIT = 80.08% × G
employer BASS = 24% × G
employer cost = G + employer BASS = 124% × G
```

The **360,000 test is on taxable income, not gross cash salary**. With only salary and the compulsory 9% medical premium, the gross salary at which `T0` reaches 360,000 is approximately MDL 395,604.40. Thus the MDL 400,000 example is just above the cut-off (`400,000 × 91% = 364,000`).

## Statutory rules and primary evidence

### 1. Income tax and personal exemption

The [Tax Code, Code No. 1163-XIII of 24 April 1997, consolidated text](https://www.legis.md/cautare/downloadpdf/149766) provides:

- **Article 15(a):** the individual income-tax rate is **12% of annual taxable income**.
- **Article 33(1), Chapter 4 “Scutiri şi alte deduceri”:** a resident individual whose annual taxable income is **less than 360,000 lei** is entitled to a personal exemption of **29,700 lei per year**. The consolidated text records the 29,700 amendment as Law No. 214 of 31 July 2024, effective 1 January 2025; it remains the operative amount for 2026.
- **Article 33(1¹):** effective for 2026, the threshold computation also takes account of income under the special regimes named there. Those regimes are outside this dossier’s facts.
- **Article 88(1):** every employer paying salary, including premiums/bonuses and benefits, must calculate and withhold the tax after requested exemptions and deductions.

The consolidated Code is the strongest source for the rate, entitlement and cut-off. As a contemporaneous cross-check, the Ministry of Finance’s [“Politica fiscală și vamală pentru anul 2027, aprobată de Guvern”](https://www.mf.gov.md/ro/content/politica-fiscal%C4%83-%C8%99i-vamal%C4%83-pentru-anul-2027-aprobat%C4%83-de-guvern) (8 September 2026) describes the proposed 2027 increase as being **from 29,700 to 40,020**, confirming that 29,700 is the current 2026 amount.

There is **no phase-out formula**. SFS’s [“Prezentarea Declarației cu privire la impozitul pe venit (CET18)”](https://www.sfs.md/ro/pagina/cet18) (2026 filing page; lines 106–113 in the web text) says that below 360,000 the exemption is available, while income of **360,000 or more** removes it. Although that page discusses returns for 2025, this mechanism and threshold are the same provisions retained in the 2026 consolidated Code.

### 2. Employee medical insurance and calculation order

CNAM’s [“Prima de asigurare”](https://cnam.md/beneficiari/prima-de-asigurare/) (current 2026 page) states at lines 21–24 that the percentage contribution is charged on salary and other remuneration and is **9.0% for 2026**. The fixed MDL 12,636 premium on that page concerns specified non-payroll categories and is not substituted for the percentage premium of an employee.

The Ministry of Finance’s [“Reforma salarială din sectorul bugetar nu modifică regulile actuale de impozitare a salariilor”](https://mf.gov.md/ru/node/134822) (26 June 2026), lines 129–144, gives the official order in a numerical payroll example: gross 10,000; medical premium 9% = 900; taxable income after medical = 9,100; PIT 12% = 1,092; net = 8,008. The article’s employer-social percentage is for a budget-sector employer and is **not** used here; its employee-side calculation order is general.

Neither the CNAM 2026 page nor the salary calculation identifies an upper cap on percentage AOAM. The model therefore applies 9% to all cash salary. This is an inference from the statutory description “salary and other remuneration” without a maximum, not a separately worded “no cap” statement.

### 3. Employer social insurance

CNAS published [“Particularitățile calculării şi achitării contribuțiilor de asigurări sociale de stat obligatorii în anul 2026”](https://cnas.gov.md/ro/node/609) on **25 February 2026**. CNAS says it was prepared under Law No. 489/1999 and the 2026 social-insurance budget Law No. 320/2025 and is binding on CNAS, its territorial structures, and contribution payers. In the linked [full 14-page CNAS instruction](https://cnas.gov.md/sites/default/files/Edit%20%3Cem%20class%3D%22placeholder%22%3EDispozi%C5%A3ii%3C/em%3E-2026-02/Particularitati%20%202026%20-%20RO%20.pdf):

- point 9, page 2, says the contribution base is salary and rewards calculated monthly for all employees;
- point 9.1, pages 2–3, gives **29%** for budget/public authorities and institutions, subject to stated exceptions;
- point 9.2, page 3, gives **24%** for private-sector employers, including state/municipal enterprises, commercial organisations, and public/private higher-education and medical institutions;
- points 10–10.2, page 3, give **39% public / 32% private** for listed civil-aviation staff working in special conditions; other aviation staff revert to point 1.1;
- points 13–13.1, page 4, calculate qualifying agricultural employers at 24%, of which 6 percentage points are compensated by the state and 18% is paid from the employer’s own funds;
- point 40, page 11, sets the ordinary remittance deadline at the **25th of the following month**.

The ordinary office/private-employer scenario therefore uses **24%**, wholly employer-paid. The instruction assesses it on all monthly salary/rewards and states no upper earnings ceiling for this category. Accordingly, this model has no maximum BASS base. That no-cap conclusion is the direct operational reading of the specified uncapped base, rather than an express sentence labelled “no maximum.”

There is, however, a **minimum base**. CNAS’s [“Aprobarea cuantumului salariului mediu lunar pe economie, prognozat pentru anul 2026 şi a salariul minim pe țară pentru anul 2026”](https://cnas.gov.md/ro/node/568) (18 December 2025), lines 102–103, reports Government Decision No. 771 of 17 December 2025: minimum salary **MDL 6,300 per month from 1 January 2026**. Under Law No. 489/1999 article 22(1), the monthly contribution base per employee cannot be below that amount, proportionate to time worked. All modeled monthly salaries exceed it.

### 4. Workplace accident and occupational disease

The official 2026 rate table does not add a separate risk-class or experience-rated workplace-accident contribution to the ordinary private employer’s 24%. Accident and occupational-disease protection sits within the social-insurance framework. The CNAS 2026 instruction, point 8.3 on page 2, separately tells employers how to report employer-paid incapacity caused by a workplace accident/occupational disease under insured-person category **15321**; it does not prescribe another payroll percentage.

This does **not** mean an accident has no direct employer cost. CNAS’s [“Indemnizaţie pentru incapacitate temporară de muncă”](https://cnas.gov.md/ro/servicii/servicii/prestatii-cazul-accidentului-de-munca-sau-bolii-profesionale/indemnizatie-pentru) (official service page, current in 2026) states that temporary-incapacity benefit is 100% of insured average monthly salary and that the employer pays working days falling in the first 20 calendar days from its own funds; BASS pays from day 21. That contingent benefit is not a fixed payroll levy and is excluded from the worked annual employer-cost amounts.

### 5. Bonuses, “13th salary,” monthly withholding and annual filing

There is no separate 13th-salary concession in the sources reviewed. Tax Code article 88 expressly includes `primele` (bonuses/premiums) in salary withholding. SFS’s database section [“Reținerea impozitului pe venit din salariu, servicii prestate și lucrări efectuate (art. 88 CF)”](https://www.sfs.md/ro/intrebare-baza-de-date-generalizare/88), particularly the answer under 29.1.7.1.1 (SFS Order No. 388, 15 August 2024), repeats that salary includes bonuses and benefits. CNAM charges 9% on “salary and other remuneration,” and CNAS point 9.2 charges 24% on “salary and rewards calculated monthly.” A normal bonus is therefore included in all three bases in the month calculated/paid under the respective rule.

Employers report income tax, withheld medical premium and calculated social contribution monthly on **IPC21**. SFS’s [generalised-practice page on IPC21](https://www.sfs.md/ro/intrebare-baza-de-date-generalizare/94) cites Tax Code article 92 and Law No. 489/1999 and sets filing/payment by the **25th of the following month**. Because statutory payroll operates monthly, an actual payslip can differ by minor rounding from this exact annual model or if pay is uneven.

For a correctly withheld salary-only employee, high salary alone does not create a separate CET18 liability in the SFS list of filing triggers. A resident who **used** the personal exemption but finishes over the threshold must file CET18, relinquish it, and pay the resulting balance. SFS’s CET18 page identifies this trigger and the 30 April deadline; SFS’s 2026 guidance [“Referitor la utilizarea scutirii personale...”](https://www.sfs.md/ru/novosti/referitor-la-utilizarea-scutirii-personale-pentru-anul-2025-de-catre-persoanele-fizice-cetateni) (30 March 2026) explains the same correction. For 2026 income, the ordinary statutory deadline is **30 April 2027**, corroborated directly for the 2026 period in SFS’s [2026 deduction guidance](https://www.sfs.md/ro/ordinele-de-baze-de-date-de-generalizare/1363). Other income, tax due, refunds or elective deductions can independently require or motivate a return.

## Worked calculations

### Annual formula used

Let `G` be annual gross regular cash salary.

1. Employee AOAM: `H = 0.09G`.
2. Income before personal exemption: `T0 = G − H`.
3. Personal exemption: `E = 29,700` only if `T0 < 360,000`; otherwise `E = 0`.
4. PIT base: `B = max(0, T0 − E)`.
5. PIT: `I = 0.12B`.
6. Net cash: `N = G − H − I`.
7. Employer BASS: `S = 0.24G`.
8. Total employer cost: `C = G + S`.

All figures below are exact to the leu under the annual formulas; no monthly rounding adjustment is introduced.

| Annual gross `G` | AOAM `H` (9%) | `T0 = G−H` | Exemption `E` | PIT base `B` | PIT `I` (12%) | Net cash `N` | Employer BASS (24%) | Employer cost `C` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 400,000 | 36,000 | 364,000 | 0 | 364,000 | 43,680 | 320,320 | 96,000 | 496,000 |
| 1,200,000 | 108,000 | 1,092,000 | 0 | 1,092,000 | 131,040 | 960,960 | 288,000 | 1,488,000 |
| 2,000,000 | 180,000 | 1,820,000 | 0 | 1,820,000 | 218,400 | 1,601,600 | 480,000 | 2,480,000 |
| 4,000,000 | 360,000 | 3,640,000 | 0 | 3,640,000 | 436,800 | 3,203,200 | 960,000 | 4,960,000 |
| 12,000,000 | 1,080,000 | 10,920,000 | 0 | 10,920,000 | 1,310,400 | 9,609,600 | 2,880,000 | 14,880,000 |

For transparency, the first row expands to:

```text
Gross                                  400,000
employee medical: 400,000 × 9%         36,000
pre-exemption taxable income           364,000
personal exemption (364,000 ≥ 360,000)       0
PIT: 364,000 × 12%                     43,680
net: 400,000 − 36,000 − 43,680        320,320
employer BASS: 400,000 × 24%           96,000
total employer cost                    496,000
```

The other rows use the same steps. The annual effective employee deduction is 19.92% and net is 80.08% because the exemption is unavailable; employer cost is 124% of salary.

## Universal rules versus scoped or variable items

| Item | Treatment in this dossier | Scope / reason |
|---|---|---|
| 12% PIT | Included | Standard resident-individual rate under Tax Code article 15(a). |
| MDL 29,700 exemption, lost at `T0 ≥ 360,000` | Included as a rule; zero in every requested row | Ordinary resident personal exemption. Other personal/family exemptions are outside the stated facts. |
| Employee AOAM 9% | Included | Percentage-paid employee category; fixed-premium categories are excluded. |
| Employer BASS 24% | Included | Ordinary private-sector employer, point 9.2. |
| Budget/public 29%, special aviation 32%/39%, qualifying agriculture state compensation, IT-park unified tax | Excluded | Employer/sector-specific categories, not universal private office employment. |
| MDL 6,300 monthly minimum BASS base | Checked, but no adjustment needed | Applies to a full-time month; every modeled monthly salary is higher. |
| Separate accident levy | Zero fixed percentage in model | No separate rate appears for the ordinary category; contingent first-20-day incapacity cost remains employer-specific. |
| Bonus/13th salary | Same ordinary bases and rates | No general preferential treatment; timing is monthly. |
| Employer incentives/subsidies and non-cash benefits | Excluded | Facts expressly assume no incentive and regular cash compensation only. |

## Evidence assessment and unresolved points

**Strongest evidence:** (1) the consolidated Tax Code’s articles 15, 33 and 88; (2) CNAM’s explicit 2026 9% page; and (3) CNAS’s dated, binding 2026 instruction, especially points 9–10 and 40. The Ministry’s June 2026 numerical example independently confirms the health-before-PIT calculation order.

**Weakest evidence / bounded inferences:**

- The official sources describe AOAM and ordinary private BASS as percentages of salary/rewards without stating a maximum. Treating both as uncapped is therefore a strong operational inference, but not supported by a sentence literally saying “there is no cap.”
- No separate ordinary-employer accident premium appears in the 2026 contribution schedule. The model sets no such percentage, while explicitly excluding the contingent statutory cost of an actual accident.
- Exact payslip rounding and the allocation of a non-even annual salary across months can cause small differences. The official rules are monthly; the requested examples are exact annual equivalents of twelve equal payments.
- The SFS annual-return pages list obligation triggers rather than giving a single sentence that salary-only employees are exempt from filing. The conclusion that correctly fully withheld salary alone needs no CET18 follows from the exhaustive triggers; a person who used an exemption and crosses the limit must file.

No unresolved fact changes any of the five numerical results under the stated assumptions.
