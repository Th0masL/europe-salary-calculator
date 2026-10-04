# 2026 formula-to-research comparison summary

## Methodology and caveats

This summary consolidates the 36 country comparison files in this directory. It does not re-audit the source dossiers or calculator modules. Counts come only from Markdown rows matching the findings-table schema:

```text
| Critical|High|Medium|Low | Confirmed mismatch|Unsupported assumption|Scenario difference|Product decision|Match | ... |
```

Descriptive bullets in each file's **Matches** section are deliberately excluded. Consequently, “Match” below counts only Montenegro's one findings-table row, not every rule that a comparison narrative says agrees. A country's matrix severity is its highest findings-table severity; it is not an average and does not imply every part of that module is wrong.

The comparisons test the dossiers' stated resident/profile/location/payment scenarios. A scenario difference is not necessarily a code defect. Exact employer cost is particularly sensitive to sector, location, insurer, fund, collective agreement, employer size and employee elections. Where no universal amount exists, the sound output is a labeled statutory floor, range, or parameterized scenario—not a fabricated all-in percentage.

## Verified findings totals

There are **129 findings-table rows** across exactly **36 country files**.

### By severity

| Severity | Count |
|---|---:|
| Critical | 23 |
| High | 53 |
| Medium | 28 |
| Low | 25 |
| **Total** | **129** |

Country-level maximum severity is Critical for 18 countries, High for 15, and Medium for 3; no country tops out at Low.

### By classification

| Classification | Count |
|---|---:|
| Confirmed mismatch | 82 |
| Unsupported assumption | 16 |
| Scenario difference | 20 |
| Product decision | 10 |
| Match | 1 |
| **Total** | **129** |

### Severity × classification reconciliation

| Severity | Confirmed mismatch | Unsupported assumption | Scenario difference | Product decision | Match | Total |
|---|---:|---:|---:|---:|---:|---:|
| Critical | 20 | 3 | 0 | 0 | 0 | 23 |
| High | 40 | 9 | 4 | 0 | 0 | 53 |
| Medium | 14 | 1 | 8 | 5 | 0 | 28 |
| Low | 8 | 3 | 8 | 5 | 1 | 25 |
| **Total** | **82** | **16** | **20** | **10** | **1** | **129** |

## Country matrix

| Country | Highest severity | Headline | Recommended disposition |
|---|---|---|---|
| Albania | High | PIT uses the wrong base and annualized bands. | Replace PIT with the statutory personal deduction and taxable-income bands; retain the regular-pay contribution path. |
| Austria | Critical | Blended SV and calibrated credits do not reproduce payment-specific contributions, negative tax or special-pay overflow. | Rebuild regular/special SV and tax; update ceilings; make Vienna-specific DGA/DZ explicit. |
| Belgium | Critical | Work bonuses/CSSS are missing or flattened, and employer cost embeds an unsupported sector proxy. | Model monthly payment structure and reductions; use a statutory employer subtotal plus explicit municipality/sector inputs. |
| Bulgaria | High | The August 2026 contribution-ceiling increase is absent. | Implement split-year monthly ceilings and expose occupational-risk class. |
| Croatia | High | The age-30 youth PIT reduction is omitted. | Add birth-year eligibility or explicitly scope the product to no youth relief. |
| Cyprus | High | Correct Holiday Fund-exempt arithmetic is presented as though the exemption were universal. | Label the exempt path and add a non-exempt 8% Holiday Fund scenario. |
| Czech Republic | High | Mandatory employer accident insurance is absent from a value labeled total cost. | Return a statutory floor, parameterize the activity rate, and add payroll rounding if exactness is required. |
| Denmark | Critical | Bottom and municipal tax bases are conflated; employment/job deductions are stale or missing. | Separate tax bases, implement final deductions/ATP base, and itemize conditional employer funds. |
| Estonia | Medium | Baseline arithmetic matches, but pillar-II and exemption elections are hard-coded. | Keep the current scenario; expose elections and add the monthly social-tax floor for broader coverage. |
| Finland | Critical | Simplified allowances, credit taper and health-tax ordering materially understate net. | Rebuild the ordered state/municipal/health calculation, update YLE, and expose municipality. |
| France | Critical | CSG base and 2026 RGDU are wrong; employer cost includes invented extras. | Implement official bases/reduction/tax details and return deterministic employer subtotal plus explicit variable inputs. |
| Germany | High | Employee differences are bounded, but employer accident/U2 rates are unsupported universal assumptions. | Transcribe final BMF rounding/PAP and separate the fixed employer floor from fund/BG variables. |
| Greece | Critical | Age-sensitive PIT, Article 16 relief and 14-payment EFKA ceilings are wrong or absent. | Rebuild PIT/relief and compute EFKA by payment; expose age, KPK and payment pattern. |
| Hungary | Critical | Currency metadata says EUR for a HUF statutory calculation. | Change the module contract to HUF; retain the simple ordinary baseline and disclose employer-wide rehabilitation rules. |
| Ireland | High | MyFutureFund is omitted and October PRSI rate changes are not modeled. | Add enrolment and pay-calendar-aware PRSI; label any annual approximation. |
| Italy | Critical | Low-income relief is omitted and employer INPS/TFR/extras use incorrect blended bases. | Rebuild statutory credits and component-level employer calculation for an explicit region/sector scenario. |
| Latvia | Critical | Non-taxable minimum and solidarity cash/reconciliation mechanics are fundamentally wrong. | Model ordinary withholding, solidarity allocation/refund, NPM and separate 3% assessment explicitly. |
| Lithuania | High | Annual NPD is omitted and employer rates/caps are misallocated. | Implement NPD and separate employer components with their correct caps and accident class. |
| Luxembourg | Critical | Social charges are uncapped and the tariff omits deductions, rounding, fund addition and credits. | Implement contribution-specific caps and the exact ACD annual tariff sequence. |
| Malta | Critical | Employee SSC is incorrectly deducted from the PIT base. | Tax total gross; calculate SSC/MLTF from basic weekly wage and make gross semantics explicit. |
| Moldova | Critical | A nonexistent 6% employee BASS charge is withheld and deducted for PIT. | Remove employee BASS and correct the AOAM-based exemption test. |
| Montenegro | Critical | An unsupported PIO maximum is used during payroll. | Remove the in-year cap, correct municipal surtax placement, and add Labour Fund/Chamber levies. |
| Netherlands | High | Employer pension and premium aggregates are unsupported and internally inconsistent with the scenario. | Preserve employee logic, but replace employer blending with named selectable statutory and pension scenarios. |
| Norway | High | Income deductions and OTP base/G are stale; AGA on OTP is omitted. | Update official values, implement NI taper, and calculate minimum OTP plus AGA correctly. |
| Poland | Critical | The 4% solidarity levy above PLN1 million is absent. | Add the annual solidarity assessment and statutory monthly/annual rounding. |
| Portugal | High | Specific deduction is stale and FGS is double-counted outside the global rate. | Update the deduction, remove separate FGS, and parameterize municipality/credit/accident premium. |
| Romania | Medium | Current EUR/high-income linear scope cannot represent authoritative RON low-income rules. | Keep a clearly labeled high-income scenario; change currency and add low-income coverage before claiming generality. |
| Serbia | Critical | Supplementary annual tax is omitted and the contribution ceiling is estimated. | Fix known floor/ceiling now; version the annual-tax statistic or label output before annual tax. |
| Slovakia | High | The income-dependent NČZD allowance is omitted. | Implement NČZD and payroll rounding; leave DFT as an employer-level variable. |
| Slovenia | High | LTC/OZP are missing from the PIT deduction base and statutory regresses are absent from employer cost. | Fix deductibility/OZP and expose salary-only versus all-mandatory employer cash cost. |
| Spain | High | Autonomous-region architecture, low-income relief and solidarity contributions are missing. | Parameterize region, separate state/regional scales and minima, and add both solidarity shares. |
| Sweden | Critical | Approximate basic/job deductions and invented phase-out produce very large net errors. | Replace estimates with official SKV formulas; expose municipality and separate optional pension. |
| Switzerland | Critical | Synthetic income tax is not federal plus Zürich tax; ALV2 is obsolete and employer extras are bundled. | Implement official Zürich/federal tax, remove ALV2, update BVG and parameterize insurance/pension/FAK inputs. |
| Turkey | High | Unincentivized employer SGK is one percentage point too low. | Change it to 21.75% and keep discounts as explicit optional scenarios. |
| United Kingdom | Medium | rUK arithmetic is close, but Scotland is unsupported and NIC timing is annualized. | Add pay-period NIC rounding and a Scotland region option, or label scope as rUK. |
| Ukraine | Critical | The temporary 2026 USC maximum is 20, not 15, minimum wages per month. | Update the monthly cap and retain separate disability/special-regime paths. |

## Prioritized implementation sequence

The groups below are work streams, not a claim that every country belongs to only one conceptual category. Within each group, earlier items combine clearer authority with larger impact or smaller implementation risk.

### 1. Obvious isolated corrections

These should land first because they are tightly bounded and have authoritative expected values.

1. **Hungary:** change currency metadata from EUR to HUF.
2. **Turkey:** change unincentivized employer SGK from 20.75% to 21.75%.
3. **Ukraine:** change the 2026 USC cap to 20 minimum wages and apply it monthly.
4. **Bulgaria:** implement the August ceiling step.
5. **Portugal:** update the specific deduction and remove the separately double-counted FGS.
6. **Moldova:** remove the 6% employee BASS and correct the exemption boundary/base.
7. **Malta:** stop deducting employee SSC from PIT; separate basic wage from statutory bonuses.
8. **Croatia:** add the age-30 youth reduction behind an explicit eligibility input.
9. **Slovakia and Lithuania:** add the sourced NČZD/NPD formulas.
10. **Ireland:** add MyFutureFund and the October PRSI rate step under an explicit pay calendar.
11. **Slovenia:** correct split-year OZP and PIT deductibility before adding employer regresses.
12. **Germany, Czech Republic, Poland and UK:** implement authoritative rounding/period sequencing after substantive formulas are fixed.

### 2. Material employee-net formula rebuilds

These require component-level rewrites and should not be patched with another blended rate.

1. **Latvia:** rebuild withholding versus solidarity reconciliation and the separate annual 3% tax.
2. **Sweden:** replace the approximate allowance/job-credit model with official SKV formulas.
3. **Switzerland:** replace synthetic tax with federal and Zürich tariff/multiplier calculations.
4. **Austria:** calculate regular and special payments separately, including income-sensitive SV, credits and negative tax.
5. **Finland:** implement separate state, municipal and health bases, deductions and credit ordering.
6. **Denmark:** split bottom/municipal bases and implement employment/job deductions on their correct base.
7. **France:** correct CSG/CRDS base, taxable-net construction, décote and related annual assessment logic.
8. **Greece:** add age-sensitive PIT, Article 16 and payment-event EFKA.
9. **Belgium:** make the 12-month/holiday-pay structure explicit and calculate work bonuses/CSSS monthly.
10. **Italy:** implement employment relief and official regional/municipal bases for a named location.
11. **Luxembourg:** implement contribution caps and the exact tariff, deductions, credits and rounding.
12. **Spain:** introduce separate state/autonomous scales, minima and low-income relief.
13. **Albania:** replace gross-based withholding bands with the statutory personal-deduction/taxable-base schedule.

### 3. High-income rules and ceilings

These need dedicated threshold vectors even where the lower-income formula is otherwise serviceable.

1. **Poland:** 4% solidarity levy over PLN1 million.
2. **Serbia:** supplementary annual tax; until its final statistic is available, label output before this tax.
3. **Latvia:** social maximum does not cap in-year withholding; reconcile solidarity separately.
4. **Austria:** move net special payments above EUR83,333 into ordinary taxation.
5. **France:** four-PASS CSG allowance limit, P8 retirement ceiling and CEHR.
6. **Spain:** employee and employer solidarity tiers above the ordinary ceiling.
7. **Luxembourg:** contribution ceiling and 9% fund addition at high tax.
8. **Greece:** per-payment EFKA ceiling across 14 payments.
9. **Switzerland:** remove obsolete ALV2 above CHF148,200.
10. **Norway:** OTP through 12G using the official average G.
11. **Italy:** extra employee INPS threshold and employer bases.
12. **Montenegro:** distinguish uncapped payroll withholding from any later maximum-contribution refund.

### 4. Employer-cost scenario and product decisions

Adopt a common product contract: return deterministic statutory cost, list excluded mandatory variables, and allow named scenario inputs. Do not bury variability in a generic “extras” percentage.

1. **Remove unsupported blended extras:** France, Belgium, Denmark, Netherlands, Switzerland, Sweden and Italy.
2. **Expose accident/risk inputs:** Bulgaria, Czech Republic, Finland, Germany, Italy, Lithuania, Netherlands, Norway, Portugal, Spain and Switzerland.
3. **Expose location:** Belgium municipality, Croatia municipality, Denmark municipality, Finland municipality, France establishment/mobility zone, Italy region/municipality, Norway AGA zone, Spain autonomous community, Sweden municipality, Switzerland canton/municipality.
4. **Expose plan/election/status:** Cyprus Holiday Fund exemption, Estonia pillar II/basic-exemption election, Ireland MyFutureFund, Netherlands occupational pension, Switzerland BVG/NBU plan, and UK Scotland/rUK.
5. **Separate salary from mandatory non-salary cash:** Slovenia regresses, Italy TFR, and conditional sickness/leave costs rather than treating them as universal percentages.
6. **Use subtotal/range semantics:** Czech, Denmark, France, Germany and Switzerland cannot produce exact employer cost from gross salary alone.

### 5. Cases that should remain research-blocked

- **Serbia supplementary annual tax:** the exact 2026 threshold depends on the official 2026 average salary. Implement the formula and label results “before annual tax,” or inject the statistic only when officially published.
- **Montenegro final PIO refund:** no supported 2026 annual maximum was found. Remove the unsupported payroll cap now, but do not invent a final refund amount.
- **France final 2026-income assessment parameters:** the dossier's law-as-enacted scale is a valid versioned scenario, but a later Finance Act can change the ultimate assessment. Keep the version/date visible and refresh when enacted.
- **Belgium EUR20k final assessment ordering:** the exact refundable fiscal-work-bonus/municipal interaction and a lawful part-time work-bonus calculation need later return instructions plus hours/FTE facts. Do not make this stress row an authoritative universal vector.

Employer-specific premiums, fund rates and sector charges are **input-blocked**, not research-blocked. Their absence should produce a subtotal or unresolved line, not delay deterministic employee and statutory-employer corrections.

## Proposed regression-test strategy

1. **Golden country/scenario fixtures.** Encode each dossier's five local-currency worked salaries as versioned fixtures with gross, employee components, final net, deterministic employer components and cost/subtotal. Store scenario metadata beside values: tax year, location, age/birth year, payment count, employer size, fund/plan elections and whether the figure is payroll cash or final assessment.
2. **Test components, not only final net.** Assert contribution bases, caps, taxable income, allowances/credits, each high-income levy and employer subtotal. Equal final net can conceal offsetting base errors.
3. **Boundary triplets.** For every allowance, cap, taper and bracket, test one minor unit below, exactly at, and one minor unit above. Priority boundaries include Latvia's social maximum and EUR200k tax, Poland's PLN1m levy, Austria's EUR83,333 special-pay limit, France's PASS/P4/P8 and 3-SMIC RGDU exit, Greece's per-payment cap, Spain's solidarity bands and Switzerland's ALV/BVG thresholds.
4. **Payment-period fixtures.** Add monthly/weekly sequences for split-year or period-rounded systems: Bulgaria, Ireland, Malta, Ukraine, UK, Belgium, Austria, Greece, Czech Republic, Germany and Poland. Include a regular-pay year and a concentrated-bonus case; annual `min(G, 12C)` must not substitute for monthly caps unless proven equivalent.
5. **Rounding contracts.** Assert the legally required unit and stage—cent, whole currency unit, taxable-base floor or final-tax floor. Use exact decimal arithmetic in tests and zero tolerance where the dossier supplies exact results; use an explicitly documented one-minor-unit tolerance only where the dossier itself flags unresolved payroll sequencing.
6. **Scenario matrix tests.** For configurable rules, include at least two materially different named scenarios: Scotland/rUK, CHF exempt/non-exempt, Estonia pillar 0/2/4/6%, two municipalities where supported, low/high employer premium scenarios, and statutory floor versus supplied accident/pension rates.
7. **Employer-output contract tests.** Assert that variable charges are excluded from a field named `statutory_floor` or supplied as inputs. Prevent regression to invented bundled percentages by requiring component provenance and rejecting an unlabeled “total” when unresolved mandatory inputs remain.
8. **Currency and unit tests.** Call every module in its declared local currency before any FX conversion. Add metadata tests that catch Hungary-style wrong currency labels and ensure converted presentation never feeds back into tax computation.
9. **Research-blocked markers.** Fixtures for Serbia annual tax, Montenegro refund and provisional France assessment parameters should carry an `as_of` date and unresolved flag. Tests should fail visibly when a placeholder is treated as final, rather than freezing guessed amounts.
10. **Rollout gates.** Land isolated corrections first; then enable rebuilt countries only when all five golden vectors, boundary tests and scenario labels pass. Track employee-net and employer-cost changes separately so product review can approve scenario semantics independently of arithmetic.

## Batch-summary reconciliation

The counts above are authoritative because they were regenerated from the 129 findings-table rows. All three reported batch summaries reconcile to their current files:

| Batch | Findings | Critical | High | Medium | Low | Confirmed mismatch | Unsupported assumption | Scenario difference | Product decision | Match |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 46 | 9 | 19 | 11 | 7 | 23 | 9 | 10 | 4 | 0 |
| B | 46 | 9 | 18 | 8 | 11 | 34 | 3 | 6 | 2 | 1 |
| C | 37 | 5 | 16 | 9 | 7 | 25 | 4 | 4 | 4 | 0 |
| **Total** | **129** | **23** | **53** | **28** | **25** | **82** | **16** | **20** | **10** | **1** |

There is **no count inconsistency** between the reported batches and the actual findings tables. The lone table-classified Match is Montenegro's “Europe Now rates” row; descriptive Match bullets elsewhere were not counted.
