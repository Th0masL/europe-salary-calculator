# Greece — employee payroll and income tax, income year 2026

**Clean-room research dossier.** Accessed **2026-10-04**. This document was reconstructed only from Greek government, AADE, Ministry of Labour, Labour Inspectorate, e-EFKA and TEKA material. It does not use the repository's implementation, generated data, prior audits, or other country dossiers.

## Scope and reproducible profile

The model is for a Greek tax resident, single, age **30**, no children, employed for the full calendar year under an ordinary private-sector salaried contract, with no benefits in kind, other income, deductions, disability, foreign-work relief, special occupation, heavy/unhealthy work, or occupational pension fund. The employee is assumed to be covered by the ordinary mixed IKA-TEAM social-insurance package **KPK 101**, including ordinary supplementary pension insurance. The employer is assumed not to be in an occupation subject to the 1% occupational-risk contribution.

“Annual gross” `G` includes all statutory regular cash pay: twelve monthly salaries, one Christmas bonus, one-half monthly salary as Easter bonus, and one-half monthly salary as holiday allowance. Thus, for monthly salary `M`:

```text
G = 12M + 1M + 0.5M + 0.5M = 14M
M = G / 14
```

This is sometimes described as “14 salaries”, but the two half payments are not full monthly salaries. The calculations assume full-year entitlement and a constant salary. The Labour Inspectorate's **“Αμοιβή”** page says a full-year salaried employee receives one monthly salary at Christmas and one-half monthly salary at Easter; the Ministry of Labour's **“Απόσπαση Εργαζομένων”** page says the holiday allowance may not exceed one-half monthly salary. The 2026 Labour Inspectorate Easter notice, published 2026-04-03, independently states the Easter amount and 2026 payment date.

## Results at a glance

Amounts are euros, rounded to cents only for display. They are annual analytic liabilities, not a reconstruction of each payslip's cent rounding.

| Gross `G` | Monthly `M` | Insurable base `B` | Employee SI | Taxable salary `X` | PIT before reduction | Art. 16 reduction | Final PIT | Net cash | Employer SI | Employer cost incl. assumed €20 ELPC |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000.00 | 1,428.57 | 20,000.00 | 2,674.00 | 17,326.00 | 1,559.34 | 670.48 | 888.86 | 16,437.14 | 4,358.00 | 24,378.00 |
| 60,000.00 | 4,285.71 | 60,000.00 | 8,022.00 | 51,978.00 | 12,471.42 | 0.00 | 12,471.42 | 39,506.58 | 13,074.00 | 73,094.00 |
| 100,000.00 | 7,142.86 | 100,000.00 | 13,370.00 | 86,630.00 | 27,317.20 | 0.00 | 27,317.20 | 59,312.80 | 21,790.00 | 121,810.00 |
| 200,000.00 | 14,285.71 | 115,190.93 | 15,401.03 | 184,598.97 | 70,423.55 | 0.00 | 70,423.55 | 114,175.42 | 25,100.10 | 225,120.10 |
| 600,000.00 | 42,857.14 | 116,429.10 | 15,566.57 | 584,433.43 | 246,350.71 | 0.00 | 246,350.71 | 338,082.72 | 25,369.90 | 625,389.90 |

The employer-cost column includes the conditional annual €20 Special Account for Children's Camps contribution described below. If the employer's coverage package does not contain OEE coverage, subtract €20. Accident insurance purchased privately, collective-agreement benefits, payroll-provider fees and other employer-specific costs are not included.

## 1. Personal income tax

### 1.1 Scale effective for 2026 income

AADE Circular **O.3068/18-11-2025**, communicating Law 5246/2025 (Government Gazette A 198/11.11.2025), reproduces amended Income Tax Code article 15. Circular page 3, lines 165–176 in the searchable PDF gives the general scale; page 4, lines 197–201 gives the youth rates; page 21–22, lines 1029–1041 makes article 3 applicable to income acquired from tax year 2026.

| Taxable employment income slice | General rate | Rate used for this age-30 profile |
|---:|---:|---:|
| €0–€10,000 | 9% | 9% |
| €10,000.01–€20,000 | 20% | **9%** |
| €20,000.01–€30,000 | 26% | 26% |
| €30,000.01–€40,000 | 34% | 34% |
| €40,000.01–€60,000 | 39% | 39% |
| over €60,000 | 44% | 44% |

The age concession is statutory for taxpayers aged 26 through 30. This dossier assumes the stated age 30 is accepted for the 2026 classification. The source does not, in the cited passage, resolve the relevant birthday/reference-date rule; that is an edge case for a person turning 31 during the year.

For this profile the pre-credit tax function is:

```text
T0(X) = 9% × min(X, 20,000)
      + 26% × min(max(X - 20,000, 0), 10,000)
      + 34% × min(max(X - 30,000, 0), 10,000)
      + 39% × min(max(X - 40,000, 0), 20,000)
      + 44% × max(X - 60,000, 0)
```

### 1.2 Taxable salary and employee social insurance

The worked scenario uses `X = G − employee mandatory social contributions`. AADE's 2026 E1 FAQ/instructions place employee-paid insurance contributions in E1 codes 351–352 and expressly state, for salary-like remuneration where employee and employer portions are paid through APD, that only the employee contribution is subtracted to find taxable income. That is consistent with the salary certificate reporting net taxable remuneration. No general employment-expense lump sum is added: the statutory relief for an ordinary employee is the article 16 tax reduction, not a separate standard expense deduction.

### 1.3 Article 16 tax reduction

The Ministry of Finance **“Φορολογία Εισοδήματος”** guide, section 1.1, lines 500–502, states:

- €777 for a taxpayer with no dependent children, limited to the scale tax; and
- above €12,000 taxable salary/pension income, the reduction falls by €20 per €1,000.

The annual formula used here is the proportional algebraic reading:

```text
R(X) = max(0, min(T0(X), 777 − 0.02 × max(X − 12,000, 0)))
PIT = T0(X) − R(X)
```

For `X = €17,326`, `R = 777 − 0.02 × 5,326 = €670.48`. For all four higher examples the taper has already reduced the credit to zero. The primary wording does not expressly state how a fraction of a €1,000 is rounded. This dossier uses proportional calculation and rounds only the final displayed amount; payroll-software cent/step treatment remains unresolved and can create a small difference.

### 1.4 Electronic-payment condition and targeted 2026 deduction

The same Ministry guide, section 1.4, lines 655–660, requires qualifying electronic expenditure equal to 30% of actual salary/pension/business income, capped at €20,000. A shortfall increases scale tax by 22% of the shortfall. It also says that for 2022–2026, 30% of specified electronically paid service expenses can be deducted from taxable income, capped at €5,000.

The examples assume the taxpayer satisfies the ordinary electronic-spend condition and claim **no** targeted service-expense deduction because no spending facts were supplied. On the E1-reported real salary amounts `X` used here, required qualifying expenditure for the five examples is respectively €5,197.80, €15,593.40, €20,000, €20,000 and €20,000. A non-compliant employee needs an additional tax line `22% × max(required − qualifying spend, 0)`.

### 1.5 Solidarity and other levies

No special solidarity contribution is charged. AADE's **“Φόρος Εισοδήματος Φυσικών Προσώπων”** page, lines 37–40, states that article 43A's special solidarity contribution was abolished for all income acquired from **2023 onward** by article 177 of Law 4972/2022. No municipal income-tax surcharge applies to ordinary Greek salary in the sourced rules. Property taxes, imputed-living-expense adjustments and tax on other income are outside the profile.

### 1.6 Withholding versus final annual tax

AADE O.3068, page 5, lines 241–248, reproduces article 60(1): monthly employment income, including benefits in kind, daily wages and lump-sum benefits, is first annualised and then subjected to articles 15 and 16 for withholding. Final income tax is annual; monthly withholding is a prepayment reconciled on the return. With constant full-year pay, aggregate withholding should broadly follow the annual calculation, but payment-by-payment rounding and payroll implementation can differ. No primary 2026 source located in this research specified a universal cent-rounding order, so the table does not claim payslip-exact withholding.

## 2. Social insurance

### 2.1 Ordinary contribution package

e-EFKA Circular **38/2024**, titled **“Μείωση ασφαλιστικών εισφορών κλάδου υγειονομικής περίθαλψης … από 01.01.2025”**, applies the Law 5162/2024 health-contribution reduction from 2025. Its active coverage-package table, page 5, lines 315–324, gives:

| e-EFKA KPK | Coverage | Employee | Employer | Total | Used here |
|---:|---|---:|---:|---:|---|
| 101 | Mixed, IKA-TEAM | **13.37%** | **21.79%** | **35.16%** | Yes |
| 102 | Mixed, IKA-TEAM plus occupational risk | 13.37% | 22.79% | 36.16% | No |
| 103 | Mixed, without supplementary pension | 10.37% | 18.79% | 29.16% | Sensitivity only |
| 104 | Mixed, no supplementary pension, plus risk | 10.37% | 19.79% | 30.16% | No |

The Ministry of Labour's **“Ασφαλιστικές Εισφορές”** page identifies the main-pension component as 20%, split 6.67% employee and 13.33% employer (lines 125–131). Circular 38 gives the 2025-and-later health component as 2.05% employee and 4.05% employer (page 1, lines 51–66). TEKA's **“Νέοι Ασφαλισμένοι Μισθωτοί”** page, lines 85–96, gives ordinary supplementary pension at 6%, split 3%/3%. The KPK total, rather than a hand-built sum of individual branches, is the controlling rate used in the examples.

The ordinary 13.37%/21.79% KPK 101 rates remained the current official package found for 2026; no later 2026 primary instrument changing KPK 101 was located. This is strong evidence for the selected scenario, but not a universal rate for every employee.

### 2.2 Supplementary-insurance institution and variability

TEKA lines 49–60 say an employee who first worked in Greece from 2022 (or was born from 2004) is generally in TEKA; a person who started by 2021 generally remains in e-EFKA's supplementary branch, subject to listed exceptions. Lines 87–96 say the contribution is the same 3% employee and 3% employer for the majority either way. Age 30 alone does not reveal first-insurance date, so the institution is unresolved; the amount in KPK 101 is not affected.

Supplementary coverage itself is occupation/history dependent. If this employee is not covered by IKA-TEAM supplementary insurance, KPK 103 would reduce both employee and employer rates by 3 percentage points. Salaried lawyers, engineers, health professionals, bank/media employees and persons in mandatory occupational funds can have category-based rules and are excluded from this ordinary profile.

### 2.3 2026 ceiling and bonus treatment

e-EFKA **“Γενικές ερωτήσεις”**, updated 2026-05-13, lines 43–49, gives the maximum monthly insurable earnings from **2026-01-01** as **€7,761.94**, under decision Δ.15/Δ΄/1865/23-01-2026 (Government Gazette B 318/29-01-2026) and e-EFKA Circular 4/2026. The Ministry contribution page states that contributions apply to earnings of every kind (apart from listed exceptional social benefits) up to that amount.

Crucially, the Ministry page says Christmas bonus, Easter bonus and holiday allowance are contribution-bearing and the maximum is applied **independently** to them. Therefore, with `C = €7,761.94` and `M = G/14`:

```text
B = 12 × min(M, C)        regular months
  +     min(M, C)         Christmas bonus
  +     min(0.5M, C)      Easter bonus
  +     min(0.5M, C)      holiday allowance

employee SI = 13.37% × B
employer SI = 21.79% × B
```

At sufficiently high pay, the absolute maximum under this constant-pay pattern is `15C = €116,429.10`, not `14C`, because each of the two half-month extras receives its own full independent ceiling. At €200,000 gross, each half-payment (€7,142.86) is still below `C`, producing `B = 13C + 2 × €7,142.86 = €115,190.93`. At €600,000, every component is capped, producing `B = 15C`.

The e-EFKA FAQ also gives the full-time minimum contribution base as €920 monthly from 2026-04-01. All example monthly salaries exceed it; a low-pay or partial-year case needs month-specific minimum-wage treatment.

### 2.4 Occupational risk, heavy work and employer-only fixed charge

The Ministry contribution page, lines 165–176, says a 1% occupational-risk contribution, employer only, applies to enterprises listed in article 1(1) of Royal Decree 473/1961 where work conditions endanger life or health. KPK 102 confirms the one-percentage-point employer difference. It is **not universal** and is zero in the ordinary office scenario. If applicable, add `1% × B` to employer cost (€200, €600, €1,000, €1,151.91 and €1,164.29 in the five examples). Heavy/unhealthy categories carry other employee and employer increments and are excluded.

e-EFKA's employer FAQ, lines 119–122, states an annual **€20 per employee** contribution for the Special Account for Children's Camps (ELPC) where the employer's APD coverage package contains OEE coverage. The table assumes that ordinary KPK 101 employer condition and adds €20. Because the official FAQ phrases this by coverage package, it is not treated as unconditional for every employer.

## 3. Worked calculations

The following expands the summary table. Each equation retains full precision until the displayed result.

### Gross €20,000

```text
M = 20,000 / 14 = 1,428.571429
B = G = 20,000.00                     (all components below ceiling)
employee SI = 20,000 × 13.37% = 2,674.00
employer SI = 20,000 × 21.79% = 4,358.00
X = 20,000 − 2,674 = 17,326.00
T0 = 17,326 × 9% = 1,559.34
R = 777 − 2% × (17,326 − 12,000) = 670.48
PIT = 1,559.34 − 670.48 = 888.86
net = 20,000 − 2,674 − 888.86 = 16,437.14
employer cost = 20,000 + 4,358 + 20 = 24,378.00
```

### Gross €60,000

```text
M = 4,285.714286; B = 60,000.00
employee SI = 8,022.00; employer SI = 13,074.00
X = 51,978.00
T0 = 1,800 + 2,600 + 3,400 + 39% × 11,978 = 12,471.42
R = 0; PIT = 12,471.42
net = 60,000 − 8,022 − 12,471.42 = 39,506.58
employer cost = 60,000 + 13,074 + 20 = 73,094.00
```

### Gross €100,000

```text
M = 7,142.857143; B = 100,000.00
employee SI = 13,370.00; employer SI = 21,790.00
X = 86,630.00
T0 = 1,800 + 2,600 + 3,400 + 7,800 + 44% × 26,630 = 27,317.20
R = 0; PIT = 27,317.20
net = 100,000 − 13,370 − 27,317.20 = 59,312.80
employer cost = 100,000 + 21,790 + 20 = 121,810.00
```

### Gross €200,000

```text
M = 14,285.714286
B = 13 × 7,761.94 + 2 × 7,142.857143 = 115,190.934286
employee SI = B × 13.37% = 15,401.03
employer SI = B × 21.79% = 25,100.10
X = 184,598.97
T0 = 15,600 + 44% × (184,598.972086 − 60,000) = 70,423.55
R = 0; PIT = 70,423.55
net = 200,000 − 15,401.03 − 70,423.55 = 114,175.42
employer cost = 200,000 + 25,100.10 + 20 = 225,120.10
```

### Gross €600,000

```text
M = 42,857.142857
B = 15 × 7,761.94 = 116,429.10
employee SI = B × 13.37% = 15,566.57
employer SI = B × 21.79% = 25,369.90
X = 584,433.43
T0 = 15,600 + 44% × (584,433.42933 − 60,000) = 246,350.71
R = 0; PIT = 246,350.71
net = 600,000 − 15,566.57 − 246,350.71 = 338,082.72
employer cost = 600,000 + 25,369.90 + 20 = 625,389.90
```

Here €15,600 is the cumulative age-30 tax through €60,000: `€20,000×9% + €10,000×26% + €10,000×34% + €20,000×39%`.

## 4. Calculation order for implementation

1. Validate the profile: tax residence, age band, children, full-year service, KPK, supplementary coverage, hazardous/heavy category and OEE/ELPC condition.
2. Convert inclusive annual gross to `M = G/14`; construct 12 regular payments plus Christmas `M`, Easter `0.5M`, and leave allowance `0.5M`.
3. Apply the €7,761.94 ceiling separately to each regular month and separately to each of the three extras; sum to annual `B`.
4. Compute employee and employer contributions from the applicable KPK. In the base case these are 13.37% and 21.79% of `B`.
5. Subtract employee mandatory contributions from gross to obtain annual taxable salary `X`.
6. Apply the age-30 article 15 scale, then the article 16 reduction/taper.
7. Add any electronic-payment shortfall charge; none is assumed here. Do not invent the targeted service-expense deduction without expense data.
8. Net cash is `G − employee SI − final PIT`. Base employer cost is `G + employer SI`, plus the conditional €20 ELPC and any employer-specific risk or other cost.

For live payroll, article 60 annualisation should be applied payment by payment and final tax reconciled annually. The precise official cent-rounding sequence was not established from the located primary sources; an implementation should not claim payslip-cent identity without an AADE/e-EFKA technical specification.

## 5. Universal rules versus assumptions and unresolved inputs

### Statutory or broadly universal for this profile

- 2026 article 15 brackets and the 26–30 age concession.
- Article 16 €777 no-child reduction and its taper above €12,000.
- Abolition of the special solidarity contribution from 2023.
- Contribution-bearing Christmas, Easter and leave payments, with the ceiling applied independently.
- 2026 monthly ceiling €7,761.94.
- Christmas `1M`, Easter `0.5M`, and leave allowance no more than `0.5M` for a full-year monthly-paid private employee.

### Explicit scenario assumptions, not universal

- KPK 101 with supplementary pension: 13.37% employee and 21.79% employer.
- No occupational-risk or heavy/unhealthy contribution.
- ELPC applies because the assumed ordinary coverage package contains OEE; otherwise employer cost is €20 lower.
- Full-year continuous employment and constant salary; no absences that prorate bonuses.
- Electronic-spend condition fully met; no qualifying targeted-service deduction claimed.
- Employee has no taxable benefits, other income, deemed-income adjustment or individual tax credit.

### Unresolved / do not hard-code without more facts

- Whether this particular employee belongs to TEKA or legacy e-EFKA supplementary insurance (same 3%/3% amount in this scenario).
- Whether a real occupation is covered by supplementary insurance at all, a mandatory occupational fund, heavy/unhealthy rules, or the 1% risk surcharge.
- The exact legal birthday/reference-date test for the 26–30 youth bracket when the employee turns 31 during 2026.
- Payroll-period cent rounding and whether the €20-per-€1,000 credit taper is rounded by whole €1,000 steps or pro-rated for a partial €1,000. The worked table uses pro-rating.
- Any collective-agreement cost, private insurance, meal vouchers, fringe benefits, severance accrual, payroll administration or other employer-specific expense.

## 6. Primary sources and exact support

All links were accessed 2026-10-04.

1. **AADE, Circular O.3068/18-11-2025, “Κοινοποίηση διατάξεων των άρθρων 1 έως 16 … και 47 του ν. 5246/2025”**; published 2025-11-18; underlying Law 5246/2025, Government Gazette A 198/2025 published 2025-11-11. [PDF](https://www.aade.gr/sites/default/files/2025-11/O3068_2025.pdf), [landing page](https://www.aade.gr/egkyklioi-kai-apofaseis/o-3068-18-11-2025). Pinpoints: PDF pp. 3–4 (lines 160–201), brackets and age rates; p. 5 (lines 241–248), withholding after annualisation; pp. 21–22 (lines 1029–1041), effective for 2026 income; pp. 5–6 (lines 250–292), extension of electronic-payment incentives through 2026.
2. **Ministry of National Economy and Finance, “Φορολογία Εισοδήματος” (Income Taxation)**; living guidance page, no displayed publication date. [Source](https://minfin.gov.gr/forologiki-politiki/forologikos-odigos/forologia-eisodimatos/). Pinpoints: section 1.1, lines 486–502, 2026 scale, age rates, €777 reduction and taper; section 1.4, lines 655–660, 30% electronic-spend requirement, €20,000 cap, 22% shortfall charge and special 2022–2026 service-expense deduction.
3. **AADE, “Φόρος Εισοδήματος Φυσικών Προσώπων”**; living guidance page, no displayed publication date. [Source](https://www.aade.gr/exypiretisi-enimerosi/hristikoi-odigoi/hristikos-odigos-gia-ta-basika-forologika-dikaiomata-ton-amea/foros-eisodimatos-fysikon). Pinpoint: lines 37–40, solidarity contribution abolished for all income from 2023 under Law 4972/2022 art. 177.
4. **AADE, “Συχνές ερωτήσεις – απαντήσεις για Δήλωση Φορολογίας Εισοδήματος ΦΠ (Ε1)”**; published 2026-03, instructions for the 2025 return. [PDF](https://www.aade.gr/sites/default/files/2026-03/FAQs_E1_2026_0.pdf). Pinpoint: discussion of E1 codes 351–352 and employee-paid mandatory insurance contributions. It supports the tax-base method but is not itself a 2026 liability table.
5. **e-EFKA, Circular 38/2024, “Μείωση ασφαλιστικών εισφορών κλάδου υγειονομικής περίθαλψης … από 01.01.2025”**; issued December 2024; effective 2025-01-01 under Law 5162/2024. [PDF](https://www.e-efka.gov.gr/sites/default/files/2024-12/%CE%95%CE%93%CE%9A.%2038_2024_%CE%9C%CE%95%CE%99%CE%A9%CE%A3%CE%97%20%CE%91%CE%A3%CE%A6.%20%CE%95%CE%99%CE%A3%CE%A6%CE%9F%CE%A1%CE%A9%CE%9D%20%CE%99%CE%94%CE%99%CE%A9%CE%A4.%20%CE%94%CE%99%CE%9A%CE%91%CE%99%CE%9F%CE%A5%202025%20%28971%CE%A546%CE%9C%CE%91%CE%A0%CE%A3-348%29.pdf). Pinpoints: pp. 0–1, lines 27–66, effective date and 2.05%/4.05% health split; p. 5, lines 315–324, KPK 101–104 exact totals and occupational-risk variants.
6. **Ministry of Labour and Social Security, “Ασφαλιστικές Εισφορές”**; living guidance page, current in 2026. [Source](https://ypergasias.gov.gr/koinoniki-asfalisi/asfalismenoi-eisfores-kai-paroches/asfalistikes-eisfores/). Pinpoints: lines 125–131, main pension 6.67%/13.33%; line 131, all-pay base and €7,761.94 ceiling; page text immediately following that passage, bonuses/leave contribution-bearing and ceiling applied independently; lines 165–176, 1% occupational risk and its limited business scope; lines 236–238, heavy-work/risk exceptions.
7. **e-EFKA, “Γενικές ερωτήσεις” for salaried insurance contributions**; updated 2026-05-13 for the maximum and 2026-06-03 for the minimum. [Source](https://www.e-efka.gov.gr/el/sychnes-eroteseis/asphalisi-eisphores/asphalismenoi/misthotoi-0/genikes-eroteseis). Pinpoints: lines 43–52, €7,761.94 from 2026-01-01, decision and Circular 4/2026; lines 53–61, €920 minimum from 2026-04-01.
8. **TEKA, “Νέοι Ασφαλισμένοι Μισθωτοί”**; living official fund page, no displayed publication date. [Source](https://teka.gov.gr/neoi-asfalismenoi-misthotoi/). Pinpoints: lines 49–60, coverage based on first work from 2022 and exceptions; lines 85–96, 6% supplementary contribution split 3% employee/3% employer; lines 159–162, covered cohorts.
9. **Hellenic Labour Inspectorate, “Αμοιβή”**; living official guidance page. [Source](https://www.hli.gov.gr/ergasiakes-scheseis/ergazomenoi-ergasiakes-sxeseis/dikaiomata-ergazomenoi-ergasiakes-sxeseis/amoivi-2/). Pinpoint: “Δώρο Πάσχα” and “Δώρο Χριστουγέννων” bullets: half a monthly salary and one monthly salary for full qualifying periods. See also **“Μέχρι και τη Μεγάλη Τετάρτη …”**, published 2026-04-03, [source](https://www.hli.gov.gr/dimosiefseis/mechri-kai-ti-megali-tetarti-i-katavoli-dorou-pascha-ston-idiotiko-tomea-2/), confirming the 2026 Easter rule.
10. **Ministry of Labour and Social Security, “Απόσπαση Εργαζομένων”**; living official guidance page. [Source](https://ypergasias.gov.gr/ergasiakes-scheseis/atomikes-ergasiakes-sxeseis/apospasi-ergazomenon/). Pinpoint: holiday-allowance paragraph, cap of half a monthly salary for monthly-paid workers.
11. **e-EFKA, “Κοινών επιχειρήσεων & Οικοδομοτεχνικών Έργων” employer FAQ**; ELPC item last updated 2024-10-21. [Source](https://www.e-efka.gov.gr/el/sychnes-eroteseis/asphalisi-eisphores/ergodotes/apd/koinon-epicheireseon-oikodomotechnikon-ergon). Pinpoint: lines 119–122, conditional €20 annual employer contribution per private-law employee where the APD package includes OEE.

## Evidence assessment

**Strongest evidence:** AADE O.3068 reproduces the enacted 2026 scale, age concession, withholding rule and effective date verbatim; e-EFKA's active KPK table gives the exact 13.37%/21.79% package; the Ministry/e-EFKA 2026 pages give the exact ceiling and expressly say the three extra payments are independently capped.

**Weakest evidence / largest model risk:** the profile does not specify first-insurance date or actual occupation, so KPK 101 and the supplementary-insurance branch are scenario choices rather than universal facts. The official sources located do not settle payroll cent-rounding or fractional-€1,000 taper handling. Employer cost outside statutory KPK contributions is inherently incomplete without the employer's activity, collective agreement and benefits.
