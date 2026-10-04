# Luxembourg employee payroll, tax year 2026 — clean-room research dossier

Access date for every source: **2026-10-04**. This dossier was reconstructed only from Luxembourg government, Administration des contributions directes (ACD), Centre commun de la sécurité sociale (CCSS), and Guichet sources. It does not rely on calculator code, generated data, prior audits, or another country dossier.

## Scope and reproducible assumptions

- Luxembourg-resident individual, age 30, unmarried, no children, **tax class 1**.
- One ordinary private-sector employment, personally affiliated to Luxembourg social security for all of 2026.
- Gross cash compensation is the stated annual total. There are no benefits in kind, exempt overtime, impatriate relief, participatory bonus exemption, travel deduction, actual employment expenses above the forfait, private pension deduction, or other income/deduction.
- Except for the €20,000 example explained below, salary is paid regularly over 12 months. There is no separate 13th-month payment in the worked examples.
- Employer scenario: ordinary private employer using the multisectoral occupational-health service (STM), accident bonus-malus factor **1.00**, and Mutualité des employeurs class **1**. Those three choices are not universal; alternatives are shown below.
- Figures are annual statutory-liability estimates rounded to cents for display. Actual payroll calculates and rounds contributions monthly, and wage-tax withholding is an advance. Cent-level differences can therefore arise from payroll-system rounding.

### The €20,000 boundary case

The indexed 2026 unqualified full-time minimum is €2,703.74 per month for January–May and €2,771.33 for June–December, or **€32,918.01** for the year. Thus €20,000 cannot represent a full-time, full-year ordinary job for an employee aged 30. It is modelled as a lawful **60.7570% part-time job paid at the prorated minimum** (about 105.11 of 173 hours monthly). The contribution minimum and dependency-insurance abatement are prorated by that same fraction. This is an explicit scenario, not an assertion that €20,000 is a lawful full-time salary.

## 1. Income tax

### 1.1 Taxable income

For these facts, before the statutory €50 rounding:

```text
taxable income before rounding
  = gross cash salary
  - employee health insurance (2.80% + 0.25% on the capped base)
  - employee pension insurance (8.50% on the capped base)
  - €540 employment-expense forfait
  - €480 special-expense forfait
```

The **1.40% dependency contribution is not one of the deductible mandatory health/pension contributions**. ACD, “Détermination du revenu net provenant d'une occupation salariée,” last updated 2022-05-23, lines/items on the €540 forfait and deductible mandatory health and pension contributions plus €480 special-expense forfait: <https://impotsdirects.public.lu/fr/az/d/deter_salar.html>.

Under article 126 L.I.R., adjusted taxable income `x` is the result rounded **down to the next lower multiple of €50**. ACD, “Barèmes,” effective from tax year 2025, references the official tariff and automated formulas: <https://impotsdirects.public.lu/fr/baremes.html>; coordinated L.I.R. (text in force 2026): <https://impotsdirects.public.lu/fr/legislation/LIR.html>.

### 1.2 Class-1 tariff (still applicable in 2026)

ACD states that the following base tariff applies from tax year 2025 and that class 1 uses the base tariff. No later 2026 tariff replacement is shown in the ACD tariff collection; the ACD collection says the latest tariff adaptation remains the one effective 2025-01-01.

| Slice of adjusted taxable income `x` | Marginal rate |
|---:|---:|
| below €13,230 | 0% |
| €13,230–€15,435 | 8% |
| €15,435–€17,640 | 9% |
| €17,640–€19,845 | 10% |
| €19,845–€22,050 | 11% |
| €22,050–€24,255 | 12% |
| €24,255–€26,550 | 14% |
| €26,550–€28,845 | 16% |
| €28,845–€31,140 | 18% |
| €31,140–€33,435 | 20% |
| €33,435–€35,730 | 22% |
| €35,730–€38,025 | 24% |
| €38,025–€40,320 | 26% |
| €40,320–€42,615 | 28% |
| €42,615–€44,910 | 30% |
| €44,910–€47,205 | 32% |
| €47,205–€49,500 | 34% |
| €49,500–€51,795 | 36% |
| €51,795–€54,090 | 38% |
| €54,090–€117,450 | 39% |
| €117,450–€176,160 | 40% |
| €176,160–€234,870 | 41% |
| above €234,870 | 42% |

Source: ACD, “Tarif de base applicable aux personnes physiques (impôt sur le revenu),” last updated 2025-01-17, effective from tax year 2025, tariff bullets and class-1 statement: <https://impotsdirects.public.lu/fr/az/t/tarif_pers.html>. Statutory origin: Law of 2024-12-20, article 3 replacing article 118 L.I.R., Mémorial A No. 589: <https://legilux.public.lu/eli/etat/leg/loi/2024/12/20/a589/jo>.

Let `R(x)` be the sum of each slice width multiplied by its marginal rate. The official annual class-1 automated formula then requires:

```text
I = floor(R(x))                              # un-surcharged tax, whole euros

if x <= €150,000:
    employment-fund addition = floor(0.07 × I)
else:
    employment-fund addition = floor(0.09 × I - €931.80)

tax before credits = I + employment-fund addition
```

The `−€931.80` continuity adjustment is material. It means “9% above €150,000” must not be implemented as `1.09 × I` on the whole tax. The exact formula and “round down to the euro” instruction appear in ACD’s official workbook, sheet “Classe 1,” note to “Formules de l'impôt sur le revenu,” document updated 2025-04-17 and effective from 2025: <https://impotsdirects.public.lu/dam-assets/fr/baremes/bareme-2025-format-excel.xlsx>. The summary rule (7%; 9% beyond €150,000 adjusted taxable income for classes 1/1a) is in ACD, “Fonds pour l'emploi,” last updated 2024-02-13: <https://impotsdirects.public.lu/fr/az/f/fond_empl.html>.

### 1.3 Refundable employee tax credits for 2026

For annual gross salary `G`:

```text
CIS = 0                                      if G < €936 or G >= €80,000
      €300 + 2.9% × (G - €936)              if €936 <= G <= €11,265
      €600                                   if €11,266 <= G <= €40,000
      €600 - 1.5% × (G - €40,000)           if €40,001 <= G <= €79,999

CI-CO2 = 0                                   if G < €936 or G >= €80,000
         €216                                if €936 <= G <= €40,000
         €216 - 0.54% × (G - €40,000)       if €40,001 <= G <= €79,999
```

The credits are available once across all salary, require personal compulsory social-insurance affiliation, and are **creditable and refundable**. Therefore the worked example permits tax net of credits to be negative. Source: ACD, “CIS et CI-CO2 salarié à partir de l'année d'imposition 2026,” last updated 2026-01-05, formulas and conditions: <https://impotsdirects.public.lu/fr/az/c/credit-impot-salaries/cis2026.html>.

## 2. Employee social contributions

The CCSS notice dated **2026-01-16**, “Avis aux employeurs — Taux de cotisation au 01.01.2026 pour salariés,” gives these exact employee rates: health benefits in kind **2.80%**, cash-benefit addition **0.25%**, pension **8.50%**, and dependency **1.40%**. The notice also says the cash-benefit addition applies only to insured persons entitled to cash sickness benefit; that is assumed for this ordinary employee. PDF, page 1, rate table and footnotes 1–2: <https://ccss.public.lu/dam-assets/publications/2026/ccss-20260116-avis-80-99-fr-de.pdf>.

### 2.1 Capped base

Health and pension use a monthly minimum and maximum. The 2026 index change gives:

| Period | Monthly minimum / SSM | Monthly maximum (5 × SSM) |
|---|---:|---:|
| January–May 2026 | €2,703.74 | €13,518.68 |
| June–December 2026 | €2,771.33 | €13,856.63 |

For regular pay at or above the full-time minimum, the annual maximum is:

```text
Cmax = 5 × €13,518.68 + 7 × €13,856.63 = €164,589.81
```

CCSS, “Paramètres sociaux,” 2026 rate table and index rows effective 2026-01-01 and 2026-06-01 (web page displays no separate publication date): <https://ccss.public.lu/fr/parametres-sociaux.html>. CCSS, “Assiettes de cotisation,” last modified 2022-12-28, says the full-time minimum is the SSM, part-time minimum is proportional to hours/173, and the annual base for one employer cannot exceed five times 12 monthly SSMs: <https://ccss.public.lu/fr/assiettes-cotisation.html>. CCSS, “Plafond cotisable,” last modified 2022-09-22, says the cap applies to health, pension, accident, mutuality, family benefits and occupational health and is regularised cumulatively during the year: <https://ccss.public.lu/fr/plafond-cotisable.html>.

For the target regular salaries, define `C = min(G, €164,589.81)`, except that the €20,000 part-time base is its actual €20,000. Then:

```text
employee deductible health + pension = C × (2.80% + 0.25% + 8.50%)
                                     = C × 11.55%
```

### 2.2 Dependency insurance

The dependency base is neither raised to the contribution minimum nor reduced to the contribution maximum. It is reduced by one quarter of the monthly SSM. CCSS publishes €675.93 for January 2026 and €692.83 from June 2026. Thus the full-time annual abatement, using the monthly published cent amounts, is:

```text
A = 5 × €675.93 + 7 × €692.83 = €8,229.46
dependency contribution = 1.40% × (G - A)
```

When monthly hours are under 150, the abatement is prorated by declared hours/173. For the €20,000 minimum-wage part-time scenario, that makes the abatement 25% of gross and the contribution `1.40% × 75% × €20,000 = €210.00`. Source: CCSS employer notice dated 2026-01-16, footnote 2 (January abatement), and CCSS “Assiettes de cotisation,” dependency section and June 2026 example (June abatement and hours rule), URLs above.

CCSS, “Charge des cotisations,” last modified 2025-02-19, confirms health and pension are shared equally, while dependency is borne by the insured employee: <https://ccss.public.lu/fr/charge-cotisations.html>.

## 3. Employer contributions and variable costs

### 3.1 Statutory allocation and chosen scenario

On the same capped base `C`:

| Component | Employer rate in chosen scenario | Universal or variable? |
|---|---:|---|
| Health, benefits in kind | 2.80% | statutory ordinary employee |
| Health, cash-benefit addition | 0.25% | applies where employee has cash-benefit entitlement |
| Pension | 8.50% | statutory for 2026 |
| Accident | 0.6500% | **scenario**: base 0.65% × factor 1.00 |
| Mutualité des employeurs | 0.23% | **scenario**: class 1, financial absenteeism under 0.65% |
| Occupational health | 0.14% | **scenario**: private employer using STM |
| Family benefits | 0% here | 1.70% table item applies only to public-sector employers |
| **Total selected employer rate** | **12.57%** | scenario total |

Accordingly, selected employer contributions are `12.57% × C`, and employer cost is `G + 12.57% × C`.

The accident rate is company-specific: CCSS publishes 2026 factors/rates **0.85/0.5525%, 1.00/0.6500%, 1.10/0.7150%, 1.30/0.8450%, 1.50/0.9750%**. Mutuality is also company-specific: class 1 **0.23%**, class 2 **0.95%**, class 3 **1.56%**, class 4 **2.66%**. The 2026 rates and private/public footnotes are in the CCSS notice dated 2026-01-16, page 1. Accident, mutuality and occupational health are employer-borne under CCSS “Charge des cotisations.”

Occupational health is mandatory, but its organization and cost vary. Guichet, “Affiliation à un service de santé au travail,” last modified 2025-08-22, says every employer must affiliate with or organize a service, lists STM/STI/ASTF, and says the employer rate varies by sector: <https://guichet.public.lu/fr/entreprises/ressources-humaines/securite-sociale/affiliation-service-sante.html>. Hence 0.14% is a reproducible STM scenario, not a universal all-employer rate.

The model does not add a supplementary pension, collective-agreement benefit, or a separately costed in-house/STI/ASTF health service because no universal amount exists on the stated facts. It also does not attempt to value the employer's cash-flow risk from salary continuation during illness; the compulsory Mutualité rate is included.

## 4. Bonus / 13th month and assessment order

A 13th month is not assumed automatically. Guichet’s “Contrat à durée indéterminée (CDI),” last modified 2026-06-04, identifies a gratification, 13th month and bonus as **possible** salary supplements that must be stated in the contract when applicable: <https://guichet.public.lu/fr/citoyens/travail/conditions-travail/types-contrat-travail/contrat-duree-indeterminee.html> (section “Mentions obligatoires,” remuneration item). Sector collective agreements can require one, so it is a contract/sector variable.

If paid, an ordinary cash bonus or 13th month is remuneration:

- it is included in annual gross income; ACD's official gratification example subjects the lump sum to employee health benefits-in-kind, pension and dependency contributions, but not the 0.25% cash-benefit addition (the 2025 example's pension rate must be replaced by the sourced 2026 rate); capped risks remain subject to the cumulative cap;
- dependency insurance uses the uncapped monthly gross plus gratification, less the one monthly abatement;
- for withholding, ACD treats a lump-sum gratification as non-periodic remuneration and applies the non-periodic withholding table after deducting the social contributions attributable to it; ordinary-period deductions are not repeated against the bonus;
- spreading the same amount over 12 regular payments can produce different in-year withholding, but annual tax is regularised against annual taxable salary.

ACD, “Calcul de la charge fiscale grevant une gratification,” last updated 2025-02-13, lines/table for a gratification (health/pension deductions, non-periodic withholding, and dependency base): <https://impotsdirects.public.lu/fr/salpens/charg_grat.html>. CCSS’s cumulative cap treatment is in “Plafond cotisable,” cited above.

ACD describes wage withholding as an advance potentially too high or low. A resident can request the annual salary-tax reconciliation (model 163); it compares all periodic/non-periodic withholding with annual tax and refunds excess withholding/credits. ACD, “Décompte annuel,” last updated 2026-02-24, principle and comparison rules: <https://impotsdirects.public.lu/fr/az/d/decompte.html>. The worked calculations below therefore show **annual liability**, not a simulation of 12 monthly tax cards.

## 5. Worked annual calculations

Common values:

```text
annual capped base maximum Cmax = €164,589.81
full-time dependency abatement A = €8,229.46
deductible employee rate on C     = 11.55%
selected employer rate on C       = 12.57%
```

`Net tax` below means income tax including the employment-fund addition, less refundable CIS and CI-CO2. A negative amount is a refundable credit. `Net cash` is `gross − all employee social contributions − net tax`.

| Annual gross | Capped base `C` | Deductible health + pension (11.55% × C) | Dependency | Employee social total | Taxable before €50 rounding | Adjusted taxable `x` | Base tariff `R(x)` | `I=floor(R)` | Fund addition | CIS + CI-CO2 | Net tax | Net cash | Employer contrib. (12.57% × C) | Employer cost |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| €20,000 | €20,000.00 | €2,310.00 | €210.00 | €2,520.00 | €16,670.00 | €16,650 | €285.75 | €285 | €19 | €816 | **−€512.00** | **€17,992.00** | €2,514.00 | **€22,514.00** |
| €60,000 | €60,000.00 | €6,930.00 | €724.79 | €7,654.79 | €52,050.00 | €52,050 | €8,084.40 | €8,084 | €565 | €408 | **€8,241.00** | **€44,104.21** | €7,542.00 | **€67,542.00** |
| €100,000 | €100,000.00 | €11,550.00 | €1,284.79 | €12,834.79 | €87,430.00 | €87,400 | €21,850.50 | €21,850 | €1,529 | €0 | **€23,379.00** | **€63,786.21** | €12,570.00 | **€112,570.00** |
| €200,000 | €164,589.81 | €19,010.12 | €2,684.79 | €21,694.91 | €179,969.88 | €179,950 | €58,607.90 | €58,607 | €4,342 | €0 | **€62,949.00** | **€115,356.09** | €20,688.94 | **€220,688.94** |
| €600,000 | €164,589.81 | €19,010.12 | €8,284.79 | €27,294.91 | €579,969.88 | €579,950 | €226,058.70 | €226,058 | €19,413 | €0 | **€245,471.00** | **€327,234.09** | €20,688.94 | **€620,688.94** |

### Formula trace for each row

**€20,000 (part-time minimum-wage scenario)**

```text
C = €20,000
health + pension = 11.55% × 20,000 = €2,310.00
dependency = 1.40% × (20,000 - 25% × 20,000) = €210.00
taxable = 20,000 - 2,310 - 540 - 480 = €16,670; x = €16,650
R(x) = 8% × 2,205 + 9% × (16,650 - 15,435) = €285.75
I = €285; fund = floor(7% × 285) = €19
CIS = €600; CI-CO2 = €216; net tax = 285 + 19 - 816 = −€512
```

**€60,000**

```text
C = €60,000; health + pension = €6,930.00
dependency = 1.40% × (60,000 - 8,229.46) = €724.79
taxable = €52,050.00; x = €52,050
R(x) = €8,084.40; I = €8,084; fund = floor(7% × 8,084) = €565
CIS = 600 - 1.5% × 20,000 = €300
CI-CO2 = 216 - 0.54% × 20,000 = €108
net tax = 8,084 + 565 - 408 = €8,241
```

**€100,000**

```text
C = €100,000; health + pension = €11,550.00
dependency = 1.40% × (100,000 - 8,229.46) = €1,284.79
taxable = €87,430.00; x = €87,400
R(x) = €21,850.50; I = €21,850; fund = floor(7% × 21,850) = €1,529
credits = €0; net tax = €23,379
```

**€200,000**

```text
C = Cmax = €164,589.81; health + pension = €19,010.12
dependency = 1.40% × (200,000 - 8,229.46) = €2,684.79
taxable = €179,969.88; x = €179,950
R(x) = €58,607.90; I = €58,607
fund = floor(9% × 58,607 - 931.80) = €4,342
credits = €0; net tax = €62,949
```

**€600,000**

```text
C = Cmax = €164,589.81; health + pension = €19,010.12
dependency = 1.40% × (600,000 - 8,229.46) = €8,284.79
taxable = €579,969.88; x = €579,950
R(x) = €226,058.70; I = €226,058
fund = floor(9% × 226,058 - 931.80) = €19,413
credits = €0; net tax = €245,471
```

## 6. Evidence assessment and unresolved variables

**Strongest evidence.** The dated CCSS 2026 employer notice is unusually complete: it gives both employee/employer rates, pension’s 2026 increase to 8.50% per side, accident factors, all four mutuality rates, January bases and dependency rules. The live CCSS parameter table supplies the June index change. For income tax, article 118/ACD’s tariff page supplies every bracket, while the official ACD automated workbook supplies the otherwise easy-to-miss whole-euro rounding and class-1 high-income surcharge adjustment. The dedicated ACD 2026 credit page supplies exact formulas and refundability.

**Weakest evidence / genuinely variable items.** There is no universal occupational-health cash rate across all employers: 0.14% is specifically STM. Accident bonus-malus and mutuality class depend on the employer. A 13th month depends on contract or sector collective agreement. These are intentionally scenario-labelled, not guessed. The worked annual contribution arithmetic abstracts from each payroll engine’s monthly cent-rounding convention, so cents can differ even though rates, indexed bases and annual cap are sourced. No amount is assigned to supplemental pensions, collective-agreement benefits, or an internally organized/non-STM occupational-health service.
