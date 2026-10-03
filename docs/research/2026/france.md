# France: employee payroll and income tax, income year 2026

**Clean-room research dossier — law and official guidance available on 2026-10-04.** This note was reconstructed from French official sources only. It does not use calculator code, generated data, another country model, an earlier France dossier, or an audit.

## 1. Scope and result status

The worked case is a French tax resident, single, one tax share, no children, employed for the full calendar year under the general social-security regime, in metropolitan France outside Bas-Rhin, Haut-Rhin and Moselle, as an ordinary private-sector **cadre**, with no overtime, bonus, benefit in kind, employee savings, expense reimbursement, impatriate regime, disability, church or other special status. Gross is regular cash salary, paid in 12 equal monthly instalments, and already includes normal paid-leave remuneration. The employer is assumed to have **50–249 employees**, to be subject to unemployment insurance and apprenticeship tax, and not to be a temporary-work business, a paid-leave-fund industry, an agricultural employer, a VAT-exempt employer subject to payroll tax, or the beneficiary of a special geographic/sector exemption. There is no employee-specific withholding-rate calculation here: “income tax” means final annual liability.

These assumptions matter. In particular, the employer's municipality, activity/AT-MP code, collective agreement and health-insurance contract have deliberately not been invented. Exact employer cost and exact take-home therefore require inputs not supplied in the question; §8 keeps them algebraic.

**Tax-law status.** The 2026 Finance Act enacted the scale for **2025 income** and made the amended CGI article 197 applicable to 2025 “and subsequent years.” Thus, on the access date, that is the enacted scale applicable to 2026 income. Parliament normally changes it in the Finance Act for 2027 before 2026 income is assessed. The income-tax figures below are consequently a reproducible **law-as-enacted-at-2026-10-04 scenario**, not a prediction of the final 2027 assessment scale. No future indexation is guessed.

## 2. Primary-source register

All sources were accessed 2026-10-04.

| Ref. | Official source, title and date | Exact support / pinpoint |
|---|---|---|
| S1 | [URSSAF, “Plafonds de la Sécurité sociale”](https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/plafonds-securite-sociale.html), updated 2026-01-01 | 2026 PASS €48,060; quarter €12,015; month €4,005; fortnight €2,003; week €924; day €220; hour €30. |
| S2 | [Arrêté du 22 décembre 2025 portant fixation du plafond de la sécurité sociale pour 2026](https://www.legifrance.gouv.fr/eli/arrete/2025/12/22/CPPS2536168A/jo/texte), JORF 2025-12-23, art. 1, effective periods from 2026-01-01 | PMSS €4,005 and daily ceiling €220; primary legal confirmation of S1. |
| S3 | [URSSAF, “Taux de cotisations - Secteur privé”](https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/taux-cotisations-secteur-prive.html), 2026 table, page publication/update 2026-01-01 | Employee old age 6.90% capped + 0.40% all salary; employer old age 8.55% capped + 2.11% all salary; employer sickness 13%, autonomy 0.30%, family 5.25%, dialogue 0.016%, unemployment 4% and AGS 0.25% to €192,240; FNAL >=50 employees 0.50% all salary; training >=11 employees 1%; apprenticeship 0.59% principal + 0.09% balance; AT-MP notified by Carsat; mobility rate is location-specific. It also prints CSG 6.80% deductible, CSG 2.40% taxable and CRDS 0.50% on 98.25% within €192,240. |
| S4 | [URSSAF, “Ce qu’il faut savoir au 1er janvier 2026”](https://www.urssaf.fr/accueil/actualites/informations-nouvelle-annee.html), published for 2026 | From 2026 the former reduced sickness/family rates merge into the RGDU; ordinary eligible employment uses the full rates and the new reduction. It gives `Tmin=.0200`, `Tdelta=.3821`, maximum `.4021` for 50+ employees, exponent 1.75, and eligibility below 3 SMIC. |
| S5 | [CSS art. D241-7](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054252241/), version effective 2026-06-15, Decree 2026-509 of 2026-06-12 | Legal RGDU formula; 2026 threshold is three times SMIC applicable on 2026-01-01; exponent 1.75; coefficient rounded to four decimals. |
| S6 | [URSSAF, “La réduction générale dégressive unique”](https://www.urssaf.fr/accueil/employeur/beneficier-exonerations/reduction-generale-cotisation.html), updated 2026-07-06 | Formula/application and, for 50+ employers, allocation of reduction: URSSAF share `0.3420/0.4021`, Agirc-Arrco share `0.0601/0.4021`; annual or progressive regularisation. |
| S7 | [URSSAF, “Montant du Smic”](https://www.urssaf.fr/accueil/outils-documentation/taux-baremes/montant-smic.html), updated 2026-06-01 | 2026-01-01 through 2026-05-31: €12.02/hour, €1,823.03/month; from 2026-06-01: €12.31/hour, €1,867.02/month. RGDU nevertheless uses the 2026-01-01 value under S5. |
| S8 | [Agirc-Arrco, “Cotisations au régime Agirc-Arrco en 2026”](https://reglementation.agirc-arrco.fr/home/baremes/listes-area/baremes-1/cotisations-au-regime-agirc-arrco-en-2026.html), effective 2026-01-01; source circular 2025-16 SG-DRJ of 2025-10-30 | T1 employee/employer 3.15%/4.72%; T2 8.64%/12.95%; CEG T1 .86%/1.29%, T2 1.08%/1.62%; CET .14%/.21% on T1+T2 when pay exceeds T1. T1 ends at one PASS and T2 at eight PASS. |
| S9 | [Agirc-Arrco circular 2025-16 SG-DRJ, “Paramètres 2026”](https://www.agirc-arrco.fr/storage/CirculaireAgircArrco2025-16sg-drj.pdf), 2025-10-30, APEC table and footnote 1 | Cadre APEC: employee .024%, employer .036%, through four PSS, explicitly €192,240/year and €16,020/month. (The HTML page contains “€192,400”; the circular's arithmetic and S1 establish that this is a typo.) |
| S10 | [ANI of 2017-11-17 on cadre provident insurance](https://www.legifrance.gouv.fr/affichIDCC.do?categorieLien=cid&cidTexte=KALITEXT000036732007), extended by [order of 2018-07-27](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000037311608), JORF 2018-08-14 | Art. 1 maintains an employer-exclusive contribution of 1.50% of pay up to one PSS for covered cadres, allocated primarily to death cover. This is included as the minimum cadre provident cost. |
| S11 | [URSSAF, “La CSG-CRDS”](https://www.urssaf.fr/accueil/employeur/cotisations/liste-cotisations/csg-crds.html), published/updated 2026 | CSG 9.20% and CRDS .50%; ordinary salary base is 98.25%; 1.75% allowance stops at four PASS; employer health contribution is included without allowance. |
| S12 | [URSSAF, “Mettre en place une prévoyance complémentaire”](https://www.urssaf.fr/accueil/employeur/embaucher-gerer-salaries/embaucher/prevoyance-complementaire.html), current 2026 page | Employer provident contributions are subject to CSG/CRDS; exempt contribution limit is 6% PASS + 1.5% pay, capped at 12% PASS; forfait social is 8% at employers with 11+ employees. |
| S13 | [Service-Public, “Complémentaire santé d'entreprise”](https://www.service-public.fr/particuliers/vosdroits/F20739), verified 2024-05-15 | All employees must be offered coverage (dispensations exist); contract price varies; employer must pay at least 50%. This proves why no exact euro premium can be inferred. URSSAF's [health-plan page](https://www.urssaf.fr/accueil/employeur/embaucher-gerer-salaries/embaucher/complementaire-frais-sante.html), current 2026, additionally confirms 8% forfait social (11+ employees) and CSG/CRDS without allowance. |
| S14 | [URSSAF, “Comment sont calculées les cotisations…”](https://www.urssaf.fr/accueil/employeur/cotisations/comprendre-cotisations/calcul-cotisations-employeur.html), updated 2026-06-03 | `contribution = base × rate`; payroll and DSN are monthly; capped bases are progressively regularised year to date; AT rate depends on activity and employer size and is notified by Carsat; part-time ceilings can be reduced. |
| S15 | [DGFiP 2026 income-tax brochure, “Traitements et salaires” and “Calcul de l’impôt”](https://www.impots.gouv.fr/www2/fichiers/documentation/brochure/ir_2026/pdf_integral/Brochure-IR-2026.pdf), published spring 2026 for 2025 income | Salary social contributions and mandatory complementary retirement/providence are deductible; 6.8 points of CSG are deductible, 2.4 CSG and .5 CRDS are not; employer health contribution is taxable. The scale is 0% to €11,600; 11% to €29,579; 30% to €84,577; 41% to €181,917; 45% thereafter. Ten-percent expense allowance min €509/max €14,555. Single-person décote: `max(0, €897 − 45.25% × gross tax)` when gross tax is below €1,982. |
| S16 | [BOFiP, “Détermination de l'impôt brut”](https://bofip.impots.gouv.fr/bofip/2491-PGP.html/identifiant%3DBOI-IR-LIQ-20-10-20260407) and [“Décote…”](https://bofip.impots.gouv.fr/bofip/2495-PGP.html/identifiant%3DBOI-IR-LIQ-20-20-30-20260407), both updated 2026-04-07 | Primary tax-administration confirmation of S15's brackets and rates, and €897/45.25% décote. Both explicitly say these are for 2025 income under Finance Act 2026. |
| S17 | [Finance Act 2026-103, art. 4](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053511609/2026-07-12), promulgated 2026-02-19, JORF 2026-02-20 | Amendments to the scale/décote apply to tax due for 2025 “and subsequent years”; basis for the as-enacted 2026-income scenario, subject to a later Finance Act. |
| S18 | [Service-Public, “Qui doit payer la contribution exceptionnelle sur les hauts revenus?”](https://www.service-public.fr/particuliers/vosdroits/F31130), verified 2026-04-15 | Single-person CEHR starts above €250,000 RFR: 3% through €500,000 and 4% above. It also confirms CDHR applies to 2025 and 2026, begins at €250,000 for a single person, and targets a 20% minimum effective levy, with a 95% estimated instalment in December 2026. |
| S19 | [Service-Public, “Comment est calculée l'indemnité de congés payés?”](https://www.service-public.fr/particuliers/vosdroits/F33359), verified 2026-02-06; and [URSSAF, “Comprendre les cotisations… bulletin de paie”](https://www.urssaf.fr/accueil/salarie/cotisations-urssaf-bulletin-paie.html), published 2025-06-03 | Paid leave is the more favourable of one tenth of reference gross pay and salary maintenance; leave indemnity is remuneration subject to contributions. There is no separate universal “double holiday pay” uplift to add to stated annual gross. |
| S20 | [URSSAF 2026 DSN declaration/regularisation guide](https://www.urssaf.fr/files/live/sites/urssaffr/files/outils-documentation/guides/Guide-declaration-regularisation-cotisations-sociales-Urssaf-DSN.pdf), published 2026 | §1.6: aggregate DSN bases/contributions round to nearest euro under CSS L130-1, but nominative DSN values are transmitted as calculated; also documents 2026 removal of ordinary reduced sickness/family rates. |

## 3. Ceilings, bases and rate formulas

Let annual gross cash salary be `G`, `P = €48,060`, `P4 = €192,240`, `P8 = €384,480`:

```text
T1 = min(G, P)
T2 = max(0, min(G, P8) - P)
CadrePrev = 1.50% × T1                 # employer-only minimum
CSGbase = 98.25% × min(G, P4)
          + max(G - P4, 0)
          + CadrePrev                  # no 1.75% allowance on employer providence
```

No health-plan premium is put into the numeric base. If `H` is the employer health contribution, add `H` to `CSGbase` without allowance.

### Employee deductions

| Item | Annual formula |
|---|---:|
| Basic old age, capped | `6.90% × T1` |
| Basic old age, uncapped | `.40% × G` |
| Agirc-Arrco | `3.15% × T1 + 8.64% × T2` |
| CEG | `.86% × T1 + 1.08% × T2` |
| CET | if `G>P`, `.14% × min(G,P8)`; otherwise zero |
| APEC (cadre) | `.024% × min(G,P4)` |
| Deductible CSG | `6.80% × CSGbase` |
| Non-deductible CSG | `2.40% × CSGbase` |
| CRDS | `.50% × CSGbase` |

There is no ordinary employee unemployment contribution. “Net cash before income tax” is gross less every row above. The tax-return salary before professional expenses subtracts the first six rows and deductible CSG, but not the 2.4% CSG or CRDS.

### Employer deterministic components

The numeric scenario includes: sickness 13% of `G`; autonomy .30%; basic old age 2.11% of `G` plus 8.55% of T1; family 5.25%; dialogue .016%; unemployment 4% through P4; AGS .25% through P4; FNAL .50%; training 1%; apprenticeship .68%; Agirc-Arrco 4.72% T1 + 12.95% T2; CEG 1.29% T1 + 1.62% T2; CET .21% through P8 when `G>P`; APEC .036% through P4; `CadrePrev`; and 8% forfait social on `CadrePrev`.

For this 50+ employer, full-time RGDU is:

```text
annual SMIC for RGDU = €12.02 × 35 × 52 = €21,876.40
x = 0.5 × (3 × 21,876.40 / G - 1)
C = min(.4021, round4(.0200 + .3821 × x^1.75))  if G < €65,629.20
C = 0                                                otherwise
RGDU = C × G
```

The coefficient, not just the final amount, is rounded to four decimals (S5). The June SMIC rise does not replace the January value for the 2026 annual RGDU (S5/S6). Hours, absences and part time alter its SMIC numerator.

## 4. Income-tax model (law as enacted on the access date)

```text
netFiscal0 = G
  - employee old-age contributions
  - Agirc-Arrco - CEG - CET - APEC
  - deductible CSG

professionalExpense = max(€509, min(10% × netFiscal0, €14,555))
R = netFiscal0 - professionalExpense       # one share
```

Apply marginal rates 0%/11%/30%/41%/45% at €11,600/€29,579/€84,577/€181,917. Apply the single décote `max(0,897 − .4525 × grossScaleTax)` (limited so tax cannot go below zero). No credit or reduction is universal for this profile. The employee's personal tax credits, donations, domestic employment, etc. are outside scope.

For health coverage, if employee premium is `S` and employer premium is `H`, cash net falls by `S + 9.7%H`; subject to the statutory tax-deduction limits, `netFiscal0` changes by approximately `+.932H − S` because employer health funding is taxable, the mandatory employee contribution is deductible, and 6.8% CSG on `H` is deductible. Exact health amounts cannot be known from gross salary.

For this salary-only profile, RFR is taken as `R` (no separately added exempt/flat-tax income). CEHR is `3% × (min(RFR,500,000)−250,000)+ + 4% × (RFR−500,000)+`. CDHR is tested at RFR over €250,000. In the only worked case crossing that threshold, ordinary income tax plus CEHR already exceeds 20% of adjusted RFR, so CDHR is zero; this is not a general CDHR calculator.

## 5. Worked employee calculations

Amounts are mathematical annualisations rounded here to cents only for display. A real payroll calculates monthly and progressively regularises capped bases, so cents can differ. `CSGbase` includes the known 1.5%-of-T1 employer cadre providence contribution, but no unknown health premium.

| Gross `G` | T1 | T2 | CSG base |
|---:|---:|---:|---:|
| €20,000 | €20,000.00 | €0.00 | €19,950.00 |
| €60,000 | €48,060.00 | €11,940.00 | €59,670.90 |
| €100,000 | €48,060.00 | €51,940.00 | €98,970.90 |
| €200,000 | €48,060.00 | €151,940.00 | €197,356.70 |
| €600,000 | €48,060.00 | €336,420.00 | €597,356.70 |

| Gross | Old age capped | Old age all | Agirc | CEG | CET | APEC | CSG ded. | CSG non-ded. | CRDS |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| €20,000 | €1,380.00 | €80.00 | €630.00 | €172.00 | €0.00 | €4.80 | €1,356.60 | €478.80 | €99.75 |
| €60,000 | €3,316.14 | €240.00 | €2,545.51 | €542.27 | €84.00 | €14.40 | €4,057.62 | €1,432.10 | €298.35 |
| €100,000 | €3,316.14 | €400.00 | €6,001.51 | €974.27 | €140.00 | €24.00 | €6,730.02 | €2,375.30 | €494.85 |
| €200,000 | €3,316.14 | €800.00 | €14,641.51 | €2,054.27 | €280.00 | €46.14 | €13,420.26 | €4,736.56 | €986.78 |
| €600,000 | €3,316.14 | €2,400.00 | €30,580.58 | €4,046.65 | €538.27 | €46.14 | €40,620.26 | €14,336.56 | €2,986.78 |

| Gross | Total employee social deductions | Cash net before income tax | Salary before 10% | 10% expense | Taxable `R` | Scale tax after décote | CEHR | Cash after final tax* |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| €20,000 | €4,201.95 | €15,798.05 | €16,376.60 | €1,637.66 | €14,738.94 | €0.00 | €0.00 | €15,798.05 |
| €60,000 | €12,530.39 | €47,469.61 | €49,200.06 | €4,920.01 | €44,280.06 | €6,388.01 | €0.00 | €41,081.60 |
| €100,000 | €20,456.09 | €79,543.91 | €82,414.06 | €8,241.41 | €74,172.66 | €15,355.79 | €0.00 | €64,188.12 |
| €200,000 | €40,281.65 | €159,718.35 | €165,441.69 | €14,555.00 | €150,886.69 | €45,664.06 | €0.00 | €114,054.28 |
| €600,000 | €98,871.38 | €501,128.62 | €518,451.96 | €14,555.00 | €503,896.96 | €203,277.47 | €7,655.88 | €290,195.27 |

\* Before unknown employee health premium and its tax consequences; final assessment values are normally rounded in euros. At €20,000, gross scale tax is €345.28, while the computed décote exceeds it, hence zero. At €600,000, CEHR is `3%×€250,000 + 4%×€3,896.96 = €7,655.88`; IR+CEHR is above 20% of RFR, hence modeled CDHR zero.

### The €20,000 edge case

€20,000 is below full-year full-time statutory SMIC even before considering the June increase (five months × €1,823.03 plus seven × €1,867.02 is about €22,184.29). It is also unlikely to satisfy a cadre collective-agreement minimum. The €20,000 row is therefore only a requested mathematical stress test. A lawful case would need part-time hours or an incomplete year. Then the social-security ceiling and RGDU SMIC numerator may be prorated; without hours/dates there is no unique employee or employer result. Its employer RGDU shown below is the mechanically capped full-time formula, not a valid real payroll conclusion.

## 6. Worked deterministic employer-cost scenario

This table contains every rate that is determinable from the stated assumptions, including the mandatory minimum cadre providence contribution and forfait social. It excludes—rather than assumes zero for—AT-MP, mobility payment, health-plan premium and sector/company charges. Accordingly “subtotal cost” is not total employer cost.

| Gross | Determinable charges before RGDU | RGDU coefficient | RGDU | Determinable charges net | Gross + deterministic net charges |
|---:|---:|---:|---:|---:|---:|
| €20,000 | €8,664.40 | .4021† | €8,042.00† | €622.40† | €20,622.40† |
| €60,000 | €25,926.97 | .0218 | €1,308.00 | €24,618.97 | €84,618.97 |
| €100,000 | €42,695.77 | 0 | €0.00 | €42,695.77 | €142,695.77 |
| €200,000 | €84,285.17 | 0 | €0.00 | €84,285.17 | €284,285.17 |
| €600,000 | €202,975.32 | 0 | €0.00 | €202,975.32 | €802,975.32 |

† Invalid as a full-time employment fact for the reason in §5; shown only to complete the requested grid.

For a real employee, let `a` be the notified AT-MP rate, `v` the applicable mobility rate, `H` the annual employer health premium, and `K` all convention/company-specific employer charges. Under the assumed ordinary exemption treatment:

```text
actual employer cost
  = table's last column + a×G + v×G + 1.08×H + K
```

The `1.08×H` is premium plus 8% forfait social. If the health/providence exemption conditions or limits fail, ordinary employer contributions can also apply, so this expression must then be expanded. The AT-MP rate cannot be bounded from salary alone; the mobility payment can be absent or location-specific; the mandatory health contract has no statutory euro premium. Thus an official-source numeric upper/lower total would be false precision.

## 7. Calculation order and paid leave

1. Establish each month's gross and employment time; determine monthly PSS and any permitted proration.
2. Progressively regularise T1/T2/capped Social Security bases year to date (S14).
3. Add employer provident/health funding to the CSG/CRDS base without the salary allowance; apply the 1.75% allowance only to salary up to four PASS (S11/S12).
4. Calculate each employee and employer line as base × rate. Apply CET only once annualised remuneration exceeds T1, then to T1+T2.
5. Calculate RGDU from annual or progressive annual values, round its coefficient to four decimals, cap it, and allocate it between URSSAF and Agirc-Arrco (S5/S6).
6. Derive cash net and taxable net separately; add employer health funding to taxable salary, deduct eligible mandatory contributions and only 6.8% CSG; then apply professional expenses and annual tax.
7. Payroll is monthly and DSN nominative amounts are transmitted as calculated; aggregate DSN amounts round to the nearest euro (S20). The annual tables intentionally do not simulate twelve cent-rounding cycles.

For an ordinary monthly-paid employee, paid leave does not create a universal extra annual salary payment. During leave the employee receives the more favourable salary-maintenance or one-tenth indemnity (S19), and it remains salary subject to contributions. Because `G` is stated annual regular cash compensation, no separate holiday multiplier is added. Paid-leave funds in BTP, transport and dock work are expressly outside the scenario.

## 8. Universal rules versus variable inputs

**Universal within the stated general-regime/cadre scope:** PASS and tranche arithmetic; employee old-age, CSG/CRDS, Agirc-Arrco/CEG/CET, APEC; full ordinary employer sickness/family/old-age rates; unemployment/AGS caps; 50+ FNAL; national training/apprenticeship rates; minimum cadre provident funding; RGDU formula; progressive regularisation; tax residence/share assumptions; statutory scale currently in force; 10% professional-expense deduction; CEHR/CDHR thresholds.

**Employer, sector, place or employee specific:**

- AT-MP rate (Carsat notification based on risk and size) and mobility-payment rate/address;
- mandatory health-contract premium, employee/employer split above the 50% minimum, dispensations, and any taxable/excess funding;
- collective-agreement provident rates above the 1.5% cadre minimum, pension contribution splits more favourable than the default 60/40, conventional training/dialogue levies, occupational-health fees;
- apprenticeship surcharge for 250+ employers (excluded by assuming 50–249), OETH liability, payroll tax for VAT-exempt employers, bonus/profit-sharing/overtime/benefits and expense reimbursements;
- part-time/absence ceiling and SMIC prorations, actual monthly timing, and the personal withholding rate;
- Alsace-Moselle's additional employee health contribution and apprenticeship treatment (explicitly excluded).

## 9. Evidence assessment and unresolved facts

**Strongest evidence.** The 2026 ceiling is fixed both by the 2025-12-22 ministerial order and URSSAF; Agirc-Arrco's dated 2026 circular gives all complementary-pension/APEC values; the RGDU is supported by the current text of CSS D241-7 plus URSSAF's worked formula; URSSAF's 2026 private-sector table provides the core contribution rates. These are direct primary/legal sources and internally reconcile (including 4×PASS = €192,240).

**Weakest evidence / unresolved at the access date.** The ultimate 2026-income tax scale and 10% limits may be changed by the not-yet-enacted 2027 Finance Act; figures therefore use the law currently extended to subsequent years. Exact employer cost is not recoverable without establishment address, Carsat notification, collective agreement and insurance invoices. Exact net pay also needs the mandatory health premium/split. The requested €20,000 full-year cadre case is not legally compatible with full-time SMIC and lacks the hours needed for a lawful part-time reconstruction. Finally, CDHR can depend on adjusted RFR, tax credits and prior/family facts absent here; only the salary-only zero result at the worked high income is established.
