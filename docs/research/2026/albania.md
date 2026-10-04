# Albania employee payroll, income year 2026 — clean-room research dossier

**Scope and access date.** Independently reconstructed from the Albanian Tax Administration (DPT/Tatime), Social Insurance Institute (ISSH), and Official Publications Centre (QBZ), accessed **2026-10-04**. The model is an Albanian-resident employee, age 30, single, no children, with one ordinary private employer, twelve equal monthly payments of regular gross cash salary, and a signed personal-status declaration with that employer. No voluntary-pension deduction, benefits, special occupation, second job, or employer subsidy is assumed.

All amounts are Albanian lek (ALL). Calculations retain sub-lek precision to expose the statutory arithmetic.

## 1. Primary official sources and pinpoints

1. **QBZ, Official Gazette no. 70/2023, Law no. 29/2023 “Për tatimin mbi të ardhurat”, enacted 30 March 2023.** <https://qbz.gov.al/alfresco/webdav/FZ/2023/70/FZ-2023-70.pdf>. Key pinpoints:

   - art. 22(1), Gazette p. 8230: annual/monthly personal deductions are ALL 600,000/50,000 where annual/monthly income is up to ALL 600,000/50,000; ALL 420,000/35,000 for annual income over 600,000 through 720,000 or monthly income over 50,000 through 60,000; and ALL 360,000/30,000 above those limits; child compensation is ALL 48,000 per dependent child;
   - art. 23(2)–(3), pp. 8230–8231: the employee may claim 1/12 of the personal deduction monthly through a personal-status declaration, only once per month; other deductions are annual-return items;
   - art. 24(1), p. 8231: annual taxable employment income is taxed at **13% through ALL 2,040,000** and **23% above ALL 2,040,000**;
   - art. 65, p. 8247: the employer withholds monthly payroll tax, takes 1/12 of art. 22(a)–(c) deductions for the employee who signed the status declaration, files/pays by the 20th of the following month, and another concurrent employer may not duplicate the deductions;
   - arts. 66–67, pp. 8247–8248: the status declaration may be signed with only one payroll agent per month; an individual must file an annual return when annual income from all sources exceeds **ALL 1,200,000**, when concurrently employed by multiple employers, or when specified other income exceeds ALL 50,000.

2. **Tax Administration, “Ndryshime në deklaratën e statusit personal dhe listëpagesën e re”, implementation notice for Law 29/2023.** It confirms that the personal-status declaration drives payroll calculation under the new law and explains the new payroll fields, including the separate social- and health-contribution bases. <https://www.tatime.gov.al/d/8/45/45/1833/ndryshime-ne-deklaraten-e-statusit-personal-dhe-listepagesen-e-re>.

3. **Tax Administration, “Nga 1 janari 2026, rritet paga minimale dhe maksimale”, effective 1 January 2026.** It states: monthly minimum wage/contribution floor **ALL 50,000**; monthly maximum base for social-insurance contributions **ALL 186,416**; and health contributions for employees apply from the ALL 50,000 floor **up to the full gross wage**, i.e. no upper ceiling. <https://www.tatime.gov.al/d/8/45/45/1914/nga-1-janari-2026-rritet-paga-minimale-dhe-maksimale>.

4. **Tax Administration legislation index, “Kontributet e sigurimeve shoqërore dhe shëndetësore”.** The current index identifies **Council of Ministers Decision (VKM) no. 776 of 19 December 2025, “Për përcaktimin e pagës minimale në shkallë vendi”**, plus Law no. 7703, Law no. 10383, Law no. 9136, and VKM no. 77 as the controlling contribution instruments. <https://www.tatime.gov.al/c/6/73/kontributet-e-sigurimeve-shoqerore-dhe-shendetesore>.

5. **ISSH/QBZ consolidated Law no. 7703 of 11 May 1993, “Për sigurimet shoqërore në Republikën e Shqipërisë”, updated through Law no. 64/2023, arts. 9–10.** Article 9 says employees and employers pay on gross wages and places workplace-accident/occupational-disease and unemployment contributions on the employer. Article 10 states **13.8% employer** for sickness, maternity and pensions and **9.5% employee** social insurance, and confirms the statutory monthly minimum/maximum mechanism. <https://qbz.gov.al/alfresco/webdav/Aktet/ligj/kuvendi-i-shqiperise/1993/05/11/7703/cons-2023-08-07/LIGJ%20Nr.%207703%2C%20dat%C3%AB%2011.05.1993.pdf>.

6. **Tax Administration, employer/contribution guidance, “Punëdhënësi, sigurimet shoqërore dhe shëndetësore”.** It distinguishes the capped social-insurance base from the health base, which has only a minimum; it also identifies the E-SIG payroll as the individual contribution record. The amounts embedded in this older general page are historical, so only its enduring base rule is used; the exact 2026 limits come from source 3. <https://www.tatime.gov.al/c/5/78/89/punedhenesi-sigurimet-shoqerore-dhe-shendetesore>.

7. **QBZ/Ministry of Finance, Instruction no. 4 of 4 February 2025 amending General Instruction no. 26 of 8 September 2023, payroll field 24.** It says the employee health-contribution wage cannot be below the national minimum and **has no upper limit (tavan)**. Field 25 applies the percentage in force. <https://qbz.gov.al/alfresco/webdav/Aktet/udhezim/ministria-e-financave/2025/02/04/4/base/udhezim-2025-02-04-4.pdf>.

8. **Tax Administration, “Të ardhurat bruto”.** The employment-income list expressly includes performance rewards, special-fund payments and **13th salary** as gross employment income. <https://www.tatime.gov.al/c/3/11/18/te-ardhurat-bruto>.

9. **Tax Administration tax calendar, “Afatet e deklarimit dhe pagesës së detyrimeve tatimore”.** The annual individual income declaration and payment are due **31 March of the following year**. <https://www.tatime.gov.al/c/3/20/kalendari-tatimor>.

10. **Tax Administration, “Pyetje-përgjigje për Listëpagesat”, current payroll FAQ.** It confirms that, for an individual with employment income only and one employer, annual filing ordinarily produces no additional tax because the employer already declared and paid it; the DIVA employment/payroll-tax fields are pre-populated from payrolls. <https://www.tatime.gov.al/d/8/45/45/1860/pyetje-pergjigje-per-listepagesat>.

## 2. Ordinary monthly payroll rules for 2026

### Personal income tax

Let monthly gross employment income be `g`. With a signed status declaration, the monthly personal deduction `d(g)` is:

```text
g ≤ 50,000              d = 50,000
50,000 < g ≤ 60,000     d = 35,000
g > 60,000              d = 30,000
```

Monthly taxable employment income is `t = max(0, g − d)`. The annual band of ALL 2,040,000 is one-twelfth, or **ALL 170,000**, for payroll:

```text
if t ≤ 170,000:  monthly PIT = 13% × t
if t > 170,000:  monthly PIT = 22,100 + 23% × (t − 170,000)
```

No employee social or health contribution deduction appears in arts. 21–24 before the employment rates: the statutory base is gross employment income reduced by the art. 22 personal deduction (and any separately permitted item, none assumed here). Contributions are therefore not subtracted again when computing PIT.

Every requested monthly salary exceeds ALL 60,000, so each receives the ALL 30,000 monthly deduction, annualised to **ALL 360,000**.

### Social and health contributions

For a full month:

```text
social base s = min(max(g, 50,000), 186,416)
health base h = max(g, 50,000)       # no upper ceiling
```

| Contribution | Employee | Employer | Base/cap |
|---|---:|---:|---|
| Social insurance | 9.5% | 15.0% | `s`, capped at ALL 186,416/month |
| Health insurance | 1.7% | 1.7% | `h`, no upper cap |
| **Total nominal rate below social cap** | **11.2%** | **16.7%** | Different bases above cap |

The employer 15% social total includes the 13.8% sickness/maternity/pension amount in Law 7703 art. 10 plus the employer-only workplace-accident/occupational-disease and unemployment components required by art. 9 and VKM no. 77. There is no separate variable experience-rated accident premium in this ordinary case. No other universal employer payroll charge was identified.

```text
cash net = gross − employee social − employee health − PIT
employer cost = gross + employer social + employer health
```

## 3. Worked calculations — twelve equal monthly salaries

| Annual gross `G` | Monthly gross `g` | Annual social base | Annual health base | Annual personal deduction | Annual PIT base |
|---:|---:|---:|---:|---:|---:|
| 2,000,000 | 166,666.67 | 2,000,000 | 2,000,000 | 360,000 | 1,640,000 |
| 6,000,000 | 500,000.00 | 2,236,992 (capped) | 6,000,000 | 360,000 | 5,640,000 |
| 10,000,000 | 833,333.33 | 2,236,992 (capped) | 10,000,000 | 360,000 | 9,640,000 |
| 20,000,000 | 1,666,666.67 | 2,236,992 (capped) | 20,000,000 | 360,000 | 19,640,000 |
| 60,000,000 | 5,000,000.00 | 2,236,992 (capped) | 60,000,000 | 360,000 | 59,640,000 |

Employee side:

| Annual gross | Employee social 9.5% | Employee health 1.7% | PIT calculation | PIT | **Annual cash net** |
|---:|---:|---:|---|---:|---:|
| 2,000,000 | 190,000.00 | 34,000.00 | 13% × 1,640,000 | 213,200.00 | **1,562,800.00** |
| 6,000,000 | 212,514.24 | 102,000.00 | 265,200 + 23% × (5,640,000−2,040,000) | 1,093,200.00 | **4,592,285.76** |
| 10,000,000 | 212,514.24 | 170,000.00 | 265,200 + 23% × (9,640,000−2,040,000) | 2,013,200.00 | **7,604,285.76** |
| 20,000,000 | 212,514.24 | 340,000.00 | 265,200 + 23% × (19,640,000−2,040,000) | 4,313,200.00 | **15,134,285.76** |
| 60,000,000 | 212,514.24 | 1,020,000.00 | 265,200 + 23% × (59,640,000−2,040,000) | 13,513,200.00 | **45,254,285.76** |

Employer side:

| Annual gross | Employer social 15% | Employer health 1.7% | Total employer contributions | **Employer cost** |
|---:|---:|---:|---:|---:|
| 2,000,000 | 300,000.00 | 34,000.00 | 334,000.00 | **2,334,000.00** |
| 6,000,000 | 335,548.80 | 102,000.00 | 437,548.80 | **6,437,548.80** |
| 10,000,000 | 335,548.80 | 170,000.00 | 505,548.80 | **10,505,548.80** |
| 20,000,000 | 335,548.80 | 340,000.00 | 675,548.80 | **20,675,548.80** |
| 60,000,000 | 335,548.80 | 1,020,000.00 | 1,355,548.80 | **61,355,548.80** |

### End-to-end check: ALL 6,000,000

```text
monthly gross                                              500,000
monthly social base (capped)                               186,416
annual social base                                       2,236,992
annual health base                                       6,000,000

employee social = 9.5% × 2,236,992                         212,514.24
employee health = 1.7% × 6,000,000                         102,000.00
PIT base = 6,000,000 − 12 × 30,000                       5,640,000.00
PIT = 13% × 2,040,000 + 23% × 3,600,000                 1,093,200.00
cash net                                                 4,592,285.76

employer social = 15% × 2,236,992                          335,548.80
employer health = 1.7% × 6,000,000                         102,000.00
employer cost                                            6,437,548.80
```

## 4. Monthly calculation, annual return, bonus, and rounding

- **Monthly operation.** The employer applies the monthly personal deduction and one-twelfth tax band in each payroll and submits/pays by the 20th of the following month. Social and health floors/caps also apply monthly. Twelve equal payments make the annual arithmetic above reconcile exactly before rounding.

- **Annual filing.** Every requested gross salary exceeds Law 29/2023 art. 67’s ALL 1.2 million threshold, so the employee must file DIVA and pay any balance by **31 March 2027**. With one employer, no other income/deductions, a valid status declaration and twelve equal payrolls, annual tax is the same as aggregate withholding; Tatime’s payroll FAQ confirms that this fact pattern ordinarily has no further tax to pay.

- **Bonus/13th salary.** Tatime expressly classifies a 13th salary and performance reward as gross employment income, so it enters that month’s PIT and can move the payment through the monthly 13%/23% schedule. It is not a tax-free benefit. The official contribution summary clearly puts gross wage and permanent salary additions into contribution bases, and Law 7703 uses total gross pay, but the reviewed official pages do not state with equal specificity how a discretionary one-off 13th salary interacts with the monthly social ceiling. This dossier therefore does **not** guess a lump-bonus contribution result. A real bonus payroll should be verified against the current E-SIG instruction; the regular-pay examples are unaffected.

- **Rounding.** E-SIG is a monthly lek-denominated individual payroll declaration. No authoritative rule in the reviewed primary materials specified whether every component is rounded to whole lek, to two decimals, or only at a total-field stage. The tables intentionally show exact arithmetic to two decimals; production software should reproduce the current e-filing validation/rounding convention. This unresolved presentation issue can change annual totals by only small rounding differences, not the statutory bases or rates.

## 5. Universal rules versus variable cases

The PIT rates/deductions, 2026 floors and social ceiling, ordinary contribution percentages, and filing threshold above are universal for the stated employee. The following are outside the model: mining/special-category additional contributions, self-employed bases, unpaid family workers, part-month proration, multiple employers, voluntary pension deductions, dependent-child compensation, education expenses, disability or treaty relief, and benefits in kind. These require facts not supplied and must not be inferred from annual gross.

## 6. Evidence assessment

**Strongest evidence.** Law 29/2023 directly states the deductions, rates, monthly payroll operation, personal-status declaration, and annual filing threshold. Tatime’s dedicated 2026 notice directly states both 2026 contribution limits and—critically—the absence of a health ceiling. Law 7703 directly fixes the employee and core employer social rates and employer responsibility for accident and unemployment branches.

**Weakest evidence / unresolved.** The consolidated official material makes the aggregate ordinary rates clear, but the current public summaries do not present the employer-only 1.2 percentage points in one convenient 2026 component table. The exact e-filing rounding convention was not located. Finally, PIT treatment of a 13th salary is explicit, while its precise one-off contribution-ceiling treatment is less explicit in the reviewed primary guidance. Those points are flagged rather than guessed.

