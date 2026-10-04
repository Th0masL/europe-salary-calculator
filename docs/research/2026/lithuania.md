# Lithuania employee payroll, income year 2026 — clean-room research dossier

**Research/access date:** 2026-10-04
**Scope:** a Lithuanian-resident, single employee with no children, below pension age, in ordinary indefinite private employment; regular cash salary only; no benefits, deductible expenses, disability NPD, or second-pillar contribution unless shown separately. Amounts are euro. This is an independent reconstruction from Lithuanian primary sources; it does not rely on calculator code or another country model.

## Reproducible scenario and important boundaries

The employer is assumed to be an ordinary newly registered/private employer in **occupational-accident risk group I**. Sodra says employers not assigned to groups II–IV, including newly registered employers, are group I. The contract is indefinite, so the 1.31% unemployment rate applies rather than the fixed-term 2.03% rate. The employee is not voluntarily accumulating in the second pillar in the base results.

The annual gross is paid in 12 nearly equal monthly instalments. For cent-reproducibility, months 1–11 are annual gross / 12 rounded half-up to cents and December is the residual. Every monthly payroll component is rounded half-up to cents, then summed. The annual PIT return is separately computed from full-year amounts. This convention is explicit because the official pages establish monthly withholding and annual reconciliation but do not fully specify every software rounding step on the cited pages; compliant payroll software can consequently differ by a few cents.

## Primary sources

All links were accessed 2026-10-04.

1. **VMI, “NPD ir PNPD taikymas (20 str.)”** (undated live page; 2026 row effective **2026-01-01**), [direct page](https://www.vmi.lt/evmi/npd-pnpd-taikymas-20-str.-1). Pinpoint: row “Nuo 2026-01-01” gives monthly maximum NPD **747**, MMA **1,153**, coefficient **0.49**, zero-NPD point **2,677.49**, and annual values **8,964**, **13,836** and coefficient **0.49**. It also says annual NPD is recalculated from annual taxable income and excess monthly NPD must be repaid.
2. **VMI, “Tarifai (6 str.)”** (undated live statutory-rate table; 2026 row effective **2026-01-01**), [direct page](https://www.vmi.lt/evmi/tarifai-6-str.-1). Pinpoint: 2026 employment-income row: **20% to 36 VDU, 25% from 36 to 60 VDU, 32% above 60 VDU**.
3. **VMI, “Apie gyventojų pajamų mokesčio tarifus”** (undated 2026 explanatory page; effective **2026-01-01**), [direct page](https://www.vmi.lt/evmi/5725?lang=en). Pinpoint: 2026 amounts **36 VDU = 83,237.40** and **60 VDU = 138,729.00**.
4. **VMI, “Gyventojų pajamų mokesčio pakeitimai nuo 2026 m.”** (undated amendments page; effective **2026-01-01**), [direct page](https://www.vmi.lt/evmi/lt/gyventoju-pajamu-mokescio-pakeitimai-nuo-2026-m.). Pinpoint: changes apply from 2026; 2026 MMA is **1,153** under Government Resolution No. 700.
5. **VMI, “Nuolatinių Lietuvos gyventojų pajamų deklaravimas”**, published/updated **2026-02-10**, [direct page](https://www.vmi.lt/evmi/nuolatini%C5%B3-lietuvos-gyventoj%C5%B3-pajam%C5%B3-deklaravimas). Pinpoint: monthly NPD is based on monthly employment income, while annual NPD depends on total annual taxable income; a shortfall is settled in the annual declaration.
6. **Republic of Lithuania Law on Personal Income Tax**, current consolidated edition **2026-06-11–2026-12-31**, [e-Seimas consolidated text](https://e-seimas.lrs.lt/rs/actualedition/TAIS.171369/QTlvfEvkKY/). Relevant provisions: Articles 6 (rates), 20 (NPD) and 23 (withholding).
7. **Sodra, “Nuo 2026 m. sausio 1 d. taikomi ‘Sodros’ įmokų tarifai turintiems samdomų darbuotojų”**, updated **2026-01-05**, [direct page](https://sodra.lt/nuo-2026-m-sausio-1-d-taikomi-sodros-imoku-tarifai-turintiems-samdomu-darbuotoju?lang=en) and [official 2026 PDF](https://sodra.lt/wp-content/uploads/2025/12/Aktuali-informacija-draudejams-2026-metais.pdf). Pinpoint: 2026 social-insurance VDU **2,312.15**, 60-VDU ceiling **138,729**; employee pension 8.72%, sickness 1.99%, maternity 1.81%, health 6.98%; additional pension accumulation 3%; indefinite-contract unemployment 1.31%; accident rates 0.14/0.49/0.70/1.40%; Guarantee Fund 0.16%; Long-term Employment Fund 0.16%.
8. **Sodra, “Įdarbinimas, pranešimai, įmokos ir tarifai”** (undated live page; 2026 employer rules effective **2026-01-01**), [direct page](https://sodra.lt/imokos/idarbinimas-pranesimai-imokos-ir-tarifai). Pinpoint: a new/unlisted employer is risk group I; the group-I accident rate is 0.14%; Guarantee and Long-term Employment Fund rates are each 0.16% of gross; the employee-rate table confirms 19.5% without additional accumulation.
9. **Sodra, “Gaunu pajamų iš sporto ar atlikėjo veiklos”** (undated live contribution-base explanation; 2026 values), [direct page](https://sodra.lt/imokos/gaunu-pajamu-is-sporto-ar-atlikejo-veiklos). Pinpoint: the VSD ceiling is **138,729** in 2026 and **PSD has no ceiling**. Although the page addresses performers, the quoted point states the general VSD/PSD ceiling distinction; the Social Insurance Act remains the controlling authority.
10. **Republic of Lithuania Law on State Social Insurance**, [e-Seimas consolidated text](https://e-seimas.lrs.lt/portal/legalActPrint/lt?actualEditionId=aimSbAxAvw&category=TAD&csrt=9548748728089424378&documentId=TAIS.1327&jfwid=-15mved1lkp). Relevant provisions: contribution bases, rates and annual ceiling.
11. **Sodra, “Pagrindinė informacija” (second-pillar pension accumulation)** (undated live page; 2026 example), [direct page](https://sodra.lt/pensijos/papildomai-kaupiama-pensija/pagrindine-informacija?lang=en). Pinpoint: participant contribution **3% of gross** plus state contribution **1.5%** of the designated national average wage; the 2026 example states average wage **2,232.80** and state payment **33.49/month**.
12. **Law on Pension Accumulation**, [e-Seimas consolidated text](https://e-seimas.lrs.lt/rs/actualedition/TAIS.215829/DwCiHLqMJu/). Pinpoint: Article 8 bases the 3% participant contribution on income on which state social-insurance contributions are calculated.

## 1. Personal income tax (GPM / PIT)

### Rates and thresholds

For 2026 employment income, the annual progressive schedule is:

| Annual band | Rate |
|---|---:|
| Up to 36 VDU = €83,237.40 | 20% |
| €83,237.40–€138,729.00 (36–60 VDU) | 25% |
| Above €138,729.00 (60 VDU) | 32% |

For this salary-only case, let `T = max(0, gross − annual NPD)`. Annual PIT is modelled as:

`0.20 × min(T, 83,237.40) + 0.25 × min(max(T − 83,237.40, 0), 55,491.60) + 0.32 × max(T − 138,729, 0)`.

### NPD (tax-free amount)

Ordinary monthly NPD in 2026 is:

* if monthly gross `M ≤ 1,153`: `min(M, 747)`;
* if `1,153 < M < 2,677.49`: `max(0, 747 − 0.49 × (M − 1,153))`;
* if `M ≥ 2,677.49`: zero.

Annual NPD is:

* if annual taxable income `GMP ≤ 13,836`: `min(GMP, 8,964)`;
* if `GMP > 13,836`: `max(0, 8,964 − 0.49 × (GMP − 13,836))`.

Solving the second formula gives an annual zero point of **€32,129.88** after cent rounding (`13,836 + 8,964 / 0.49`). Disability NPD is outside the scenario.

### Withholding versus final liability

The employer applies NPD and withholds against each payment; the resident then reconciles annual NPD and the annual progressive rates. In this regular monthly-pay scenario every individual payment is below the 36-VDU amount, so the worked payroll cash-flow column uses 20% withholding on that month’s gross less monthly NPD. The annual-return column applies the annual bands. Thus the high-income examples have a genuine annual balance payable even though each monthly payslip was withheld at 20%. This distinction is important: annual tax must not simply be reported as twelve times an ordinary monthly withholding.

## 2. Employee social and health contributions

The 2026 annual VSD ceiling is `60 × 2,312.15 = €138,729.00`.

| Employee component | Rate | 2026 ceiling treatment |
|---|---:|---|
| Pension social insurance | 8.72% | capped at €138,729 |
| Sickness | 1.99% | capped at €138,729 |
| Maternity | 1.81% | capped at €138,729 |
| **VSD subtotal** | **12.52%** | capped at €138,729 |
| Compulsory health insurance (PSD) | **6.98%** | no ceiling |
| **Total below ceiling** | **19.50%** | — |

Therefore, ignoring cent timing, employee contributions are `12.52% × min(gross, 138,729) + 6.98% × gross`. Above the ceiling only PSD continues. The ceiling is cumulative by insured person, so multiple-employer administration requires Sodra coordination and is outside this one-employer scenario.

## 3. Employer contributions

For the chosen indefinite contract and accident group I:

| Employer component | Rate | Ceiling treatment used |
|---|---:|---|
| Unemployment insurance | 1.31% | 60-VDU VSD ceiling |
| Occupational accident/disease, class I | 0.14% | 60-VDU VSD ceiling |
| Guarantee Fund | 0.16% | full gross |
| Long-term Employment Fund | 0.16% | full gross |
| **Total below VSD ceiling** | **1.77%** | — |
| **Continuing above VSD ceiling** | **0.32%** | Guarantee + Long-term funds |

Thus employer cost is gross plus `1.45% × min(gross, 138,729) + 0.32% × gross`, subject to monthly cents. The treatment of the two 0.16% funds as uncapped follows Sodra’s separate “of gross” statements and their exclusion from the VSD-insurance ceiling; the cited summary does not give an equally explicit sentence saying “no ceiling.” This is one of the dossier’s weaker interpretive points and should be rechecked against reporting-system specifications before production use.

Risk group is employer-specific. Keeping all else equal, total below-ceiling employer rates would be **2.12%** in group II, **2.33%** in group III, or **3.03%** in group IV. A fixed-term contract changes unemployment insurance to 2.03%. Neither is universal and neither is used below.

## 4. Optional second-pillar pension accumulation

The base case assumes no additional accumulation. A participant contributes an additional **3%** of the social-insurance contribution base, hence `3% × min(gross, 138,729)` in this one-employer case. Sodra’s 2026 example also gives a state contribution of **€33.49/month** (1.5% of the designated €2,232.80 wage), or €401.88 across 12 displayed monthly amounts. The state amount is not deducted from salary and is not an employer cost. Participation choices and withdrawal/suspension rules are personal, so this charge must not be imposed on every employee.

## 5. Calculation order used

For each month:

1. establish gross cash pay;
2. apply the remaining cumulative 60-VDU ceiling to VSD components;
3. calculate employee VSD and uncapped PSD, plus optional 3% accumulation if elected;
4. calculate monthly NPD and 20% payment withholding for the stated regular-pay pattern;
5. net payroll cash = gross − employee contributions − optional accumulation − PIT withheld;
6. calculate employer contributions and employer cost.

At year end, recompute annual NPD from total annual taxable income, apply the annual 20/25/32% bands, and compare final PIT with amounts withheld. The examples have no benefits or other income; those would change GMP and potentially annual NPD.

## 6. Worked 2026 calculations

### Annual PIT calculation

| Gross | Annual NPD | PIT at 20% | PIT at 25% | PIT at 32% | Final annual PIT |
|---:|---:|---:|---:|---:|---:|
| 20,000 | 5,943.64 | 2,811.27 | 0.00 | 0.00 | **2,811.27** |
| 60,000 | 0.00 | 12,000.00 | 0.00 | 0.00 | **12,000.00** |
| 100,000 | 0.00 | 16,647.48 | 4,190.65 | 0.00 | **20,838.13** |
| 200,000 | 0.00 | 16,647.48 | 13,872.90 | 19,606.72 | **50,127.10** |
| 600,000 | 0.00 | 16,647.48 | 13,872.90 | 147,606.72 | **178,127.10** |

For example, at €20,000: annual NPD is `8,964 − 0.49 × (20,000 − 13,836) = 5,943.64`; taxable income is €14,056.36; PIT is €2,811.272, rounded to €2,811.27. At €200,000: `83,237.40×20% + 55,491.60×25% + 61,271×32% = 50,127.10`.

### Contributions, reconciliation, net and employer cost

These are sums of the monthly cent-rounded components under the pay schedule stated above.

| Gross | Employee VSD 12.52% (capped) | Employee PSD 6.98% | Employee total | PIT withheld in-year | Final PIT | Balance due/(refund) | Final net after annual PIT | Employer contributions | Employer cost |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 2,504.03 | 1,395.96 | **3,899.99** | 2,811.23 | 2,811.27 | **0.04 due** | **13,288.74** | 354.00 | **20,354.00** |
| 60,000 | 7,512.00 | 4,188.00 | **11,700.00** | 12,000.00 | 12,000.00 | 0.00 | **36,300.00** | 1,062.00 | **61,062.00** |
| 100,000 | 12,519.97 | 6,980.04 | **19,500.01** | 20,000.04 | 20,838.13 | **838.09 due** | **59,661.86** | 1,770.00 | **101,770.00** |
| 200,000 | 17,368.89 | 13,959.96 | **31,328.85** | 39,999.96 | 50,127.10 | **10,127.14 due** | **118,544.05** | 2,651.59 | **202,651.59** |
| 600,000 | 17,368.87 | 41,880.00 | **59,248.87** | 120,000.00 | 178,127.10 | **58,127.10 due** | **362,624.03** | 3,931.57 | **603,931.57** |

Employer-component detail:

| Gross | Unemployment 1.31% capped | Accident 0.14% capped | Guarantee 0.16% | Long-term 0.16% | Total |
|---:|---:|---:|---:|---:|---:|
| 20,000 | 261.96 | 27.96 | 32.04 | 32.04 | **354.00** |
| 60,000 | 786.00 | 84.00 | 96.00 | 96.00 | **1,062.00** |
| 100,000 | 1,310.04 | 140.04 | 159.96 | 159.96 | **1,770.00** |
| 200,000 | 1,817.32 | 194.19 | 320.04 | 320.04 | **2,651.59** |
| 600,000 | 1,817.35 | 194.22 | 960.00 | 960.00 | **3,931.57** |

The €200,000 and €600,000 capped component sums differ by cents even though the same annual ceiling applies. That is a deliberate consequence of the stated monthly sequencing and component rounding; the unrounded annual formula would produce identical capped subtotals.

If second-pillar accumulation applies, the additional employee amounts are respectively **€600.00, €1,800.00, €3,000.00, €4,161.87, and €4,161.87**. Subtracting them gives final cash nets of **€12,688.74, €34,500.00, €56,661.86, €114,382.18, and €358,462.16**; employer cost is unchanged.

## 7. Universal rules versus variable facts

**Universal for the stated ordinary 2026 employee:** the 20/25/32 PIT schedule and national thresholds; ordinary NPD formula; employee 12.52% VSD components and 6.98% PSD; €138,729 VSD ceiling; 0.16% Guarantee and 0.16% Long-term Employment Fund rates.

**Employer/person-specific:** accident risk class; unemployment rate for fixed versus indefinite contracts; second-pillar participation; disability NPD; multiple employers; non-cash benefits, other annual income and deductible expenses. These require input rather than a national default.

## 8. Evidence assessment and unresolved points

**Strongest evidence:** VMI’s 2026 NPD and rate tables and Sodra’s 2026 employer-rate bulletin/PDF state the numerical rates, VDU amounts and ceilings directly, and are cross-checked against the consolidated statutes.

**Weakest evidence / matters not guessed:**

* The cited public summaries do not spell out every cent-rounding and cumulative-ceiling sequencing rule used by payroll software. The dossier therefore declares a reproducible convention and exposes the cent differences.
* The uncapped treatment of the two employer funds is a reasoned reading of Sodra’s separate gross-base wording and the statutory VSD ceiling. Production implementation should confirm it against the current SAM reporting specification or obtain written Sodra confirmation.
* The Sodra sentence explicitly stating that PSD has no ceiling appears on an official page written for performer income rather than the main employer summary. The statutory scheme and rate table support the same distinction, but this citation is less direct for an employee than ideal.
* Monthly withholding can depend on the exact payment timing and any multiple payments in one month. The annual PIT figures are authoritative for the salary-only facts; the “withheld in-year” figures are the declared regular-pay scenario, not a universal prediction.
