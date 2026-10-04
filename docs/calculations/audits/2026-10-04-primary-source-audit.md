# Calculation primary-source audit — 2026-10-04

This is a first-pass provenance and discrepancy audit of the formulas currently
used by the website. It is **not** a payroll certification. The review compared
the implementation with primary government, tax-authority, and social-security
sources where a sufficiently specific source could be found. No formula was
changed as part of this audit: discrepancies are recorded here for a separate,
country-by-country correction and regression-test pass.

## Status meanings

- **Core match** — the official material checked supports the principal income-tax
  and/or contribution constants, and the checked subset contains no contradiction.
- **Partial** — at least one important rule is supported, but the complete employee
  and employer calculation was not independently established.
- **Investigate** — an official source contradicts the implementation, or the
  implementation explicitly uses a material approximation or omission.
- **Insufficient evidence** — this pass did not locate sufficiently specific
  primary material to make a useful comparison.

These labels apply only to the evidence inspected below. “Core match” does not
mean that every credit, deduction, local charge, employer levy, or edge case has
been validated.

## Confirmed discrepancies and material gaps

1. **Belgium — wrong 2026 personal allowance.** The implementation uses €10,910,
   which is the allowance for income year 2025. FPS Finance publishes €11,180 for
   income year 2026. With the model's 25% allowance reduction and 7% communal
   surcharge, this understates annual net pay by about **€72** once the allowance
   is fully usable. The 2026 bracket boundaries themselves match.
2. **Denmark — stale employment deduction and missing job allowance.** The code
   uses 10.65%, capped at DKK 45,100. SKAT publishes **12.75%, capped at DKK
   63,300** for 2026. It also publishes a separate job allowance of 4.5% of income
   above DKK 235,200, capped at DKK 3,100; the model omits it. At salaries high
   enough to receive both maxima, the omitted deductions reduce the modeled net
   by roughly **DKK 7,894 per year** at the modeled combined basic/municipal rate.
3. **Finland — first state-tax boundary is stale.** Vero publishes €22,000 for
   2026; the code uses €21,200. For tax bases above €22,000 this alone overstates
   state tax by about **€51 per year**. The larger issue remains the module's
   explicitly simplified earned-income credit and omitted municipal deductions.
4. **Latvia — solidarity tax is omitted above €105,300.** The model caps employee
   and employer social contributions at €105,300. VID says remuneration above
   that maximum remains subject to solidarity tax, paid during the year using the
   normal 34.09% split (23.59% employer / 10.50% employee) and reconciled to a
   25% solidarity-tax liability. This can materially overstate net pay and
   understate employer cost at the high end of the website's range.
5. **Spain — high-salary solidarity contribution is omitted.** Spanish Social
   Security confirms that remuneration above the maximum contribution base is
   subject to an additional, tiered solidarity contribution. The module explicitly
   omits it, so high-salary net and employer-cost results need correction.
6. **California (San Francisco and Los Angeles) — 2024 state values are labelled
   2025.** The model uses a $5,540 single standard deduction and bracket boundaries
   beginning at $10,756. California FTB publishes a **$5,706** deduction and a
   first 2025 boundary of **$11,079** (with the remaining boundaries indexed too).
7. **United Kingdom — scope label is too broad.** The implemented bands match
   England, Wales, and Northern Ireland, but not Scotland's separate income-tax
   bands. The row should either be labelled accordingly or gain a documented
   location assumption.

Smaller issue: Sweden's official 2026 state-tax threshold is SEK 643,000 while
the code uses SEK 643,100. The SEK 100 difference is immaterial by itself, but the
module's simplified basic and earned-income deductions are not immaterial and
still require validation.

## European country matrix

| Country | Status | Result of this pass |
|---|---|---|
| Albania | Partial | Official 2026 contribution bases (ALL 50,000 monthly minimum; ALL 186,416 maximum) and the 0/13/23% salary-tax structure support important constants. Contribution rates still need a primary-source check. |
| Austria | Partial | BMF's 2026 income-tax brackets match the code. Social-insurance ceilings, special payments, credits, and employer levies remain only partly evidenced. |
| Belgium | **Investigate** | Brackets and the 13.07% employee social-security rate are supported, but the personal allowance is €11,180, not €10,910. Employer sectoral assumptions and the claimed employer cap also need review. |
| Bulgaria | Partial | NRA provides a current 2026 insurable-income reference, but this pass did not establish every employee/employer percentage or the representative accident rate from a primary source. |
| Croatia | Insufficient evidence | No sufficiently specific current official payroll table was located in this pass. Do not treat the module's rates as independently reviewed. |
| Cyprus | Partial | The Ministry of Finance exposes a 2026 tax calculator, but the complete bands, contribution caps, and employer charges were not extracted into reproducible evidence. |
| Czech Republic | Partial | Financial Administration confirms the 2026 average wage and CZK 1,762,812 threshold for the 23% rate. Contributions and caps still need full primary validation. |
| Denmark | **Investigate** | Income-tax thresholds are supported, but the employment deduction is stale and the job allowance is missing. Municipal tax and employer funds remain representative averages. |
| Estonia | **Core match** | EMTA supports 22% income tax, the €8,400 annual basic exemption without taper, and the modeled default 2% funded-pension contribution. |
| Finland | **Investigate** | The first state-tax boundary should be €22,000, not €21,200. Exact earned-income and municipal deductions still need implementation-quality validation. |
| France | **Investigate** | URSSAF publishes the relevant rates and ceilings, but the module describes itself as reconstructed and the most approximate model. Its full employee/employer stack needs a dedicated worked-example review. |
| Germany | Partial | BMF confirms the €12,348 basic allowance. Health add-on, ceilings, care insurance, accident insurance, and exact tax-polynomial behavior require a complete check. |
| Greece | Partial | Law 5246/2025 supports the new 2026 income-tax reform reflected by the module, including the 20/26/34/39% middle rates. Credits and social contributions still need a complete independent check. |
| Hungary | Partial | NAV supports the 18.5% employee social contribution. PIT, employer social tax, allowances, and special cases still need a complete primary-source comparison. |
| Ireland | Partial | Revenue supports the €44,000 standard-rate band, €2,000 personal and employee credits, and the 2026 USC bands. The module deliberately applies the pre-October PRSI rate for the whole year and omits auto-enrolment, so it is not an exact full-year payroll result. |
| Italy | **Investigate** | INPS supports the €122,295 contribution ceiling, but regional/municipal surtaxes and several employer costs are representative. A location/sector assumption and official worked example are needed. |
| Latvia | **Investigate** | PIT rates, 10.5%/23.59% contributions, and the €105,300 maximum are supported. The required solidarity-tax treatment above the maximum is missing. |
| Lithuania | **Core match** | VMI supports the 20/25/32% 2026 bands and thresholds. The model intentionally omits the NPD at the low end, so results around €20k–€30k remain conservative rather than complete. |
| Luxembourg | Partial | ACD's official scale supports the income-tax band structure. Several employer components are reconstructed/tuned and need primary-source validation. |
| Malta | Insufficient evidence | The official rates portal was located, but a sufficiently clear 2026 Class 1 table was not. The maternity contribution cap is already marked for re-verification in code. |
| Moldova | Insufficient evidence | SFS publishes 2026 tax-law changes and annual income-tax data, but this pass did not recover a complete official employee payroll formula suitable for comparison. |
| Montenegro | **Investigate** | No complete primary payroll schedule was established. The module itself flags the pension cap and employer assumption as not fully verified. |
| Netherlands | Partial | Belastingdienst's 2026 income-tax brackets support the employee core. Occupational pension and the employer bundle remain representative rather than universal. |
| Norway | **Investigate** | Skatteetaten supports the 22% ordinary-income tax and bracket-tax framework, but the module's personal allowance and minimum-standard deduction are explicitly estimated. |
| Poland | Partial | ZUS confirms the PLN 282,600 annual contribution cap and the tax authority confirms the PLN 3,000 employment expense. The complete employee/employer stack still needs one coherent official worked-example check. |
| Portugal | Partial | The official income-tax code and 2026 withholding circular were located. Annual liability, social-security treatment, FGS, and work-accident assumptions still need a reproducible comparison. |
| Romania | Insufficient evidence | ANAF material found in this pass did not provide a complete current employee payroll formula. The code values therefore remain unverified here. |
| Serbia | **Investigate** | The tax law supports the structure, but the code's 2026 monthly allowance and estimated contribution ceiling were not confirmed from the official 2026 adjustments; supplementary annual tax is omitted. |
| Slovakia | Partial | Financial Administration provides current employee-tax guidance, but this pass did not establish every 2026 bracket, allowance, and contribution value in one reproducible official source set. |
| Slovenia | Partial | FURS publishes 2026 allowance and social-contribution material. The exact annual employment calculation and the module's full bracket/contribution combination still need a worked-example check. |
| Spain | **Investigate** | The module uses representative regional IRPF and accident rates and omits the official solidarity contribution above the maximum base. |
| Sweden | **Investigate** | Skatteverket supports 31.42% employer contributions and a SEK 643,000 state-tax threshold. The code uses 643,100 and materially simplifies the basic and earned-income deductions. |
| Switzerland | **Investigate** | The model is a representative Zürich estimate with a calibrated tax table, not a direct implementation of an official federal/cantonal/municipal schedule. |
| Turkey | Partial | GİB's 2026 wage-income brackets match the code. SGK ceilings and employee/employer rates still need an official 2026 source. |
| United Kingdom | **Core match with scope issue** | GOV.UK supports the 2026/27 allowance, taper, England/NI bands, and NI rates. Scotland is not represented, so the generic country label is misleading. |
| Ukraine | Partial | The tax authority supports the 18% PIT structure. The 2026 military levy, unified social contribution base, and employer treatment still need full primary confirmation. |

## US city models

The US models use tax year 2025. The IRS federal brackets and $15,750 standard
deduction, and SSA's $176,100 Social Security wage base, match the implementation.
The state/local first pass found one definite error: California uses 2024 values
under a 2025 label, affecting both San Francisco and Los Angeles. Other state and
local configurations remain **partial** until each revenue and labor agency's
2025 income-tax, paid-leave, unemployment, and local-tax rules have been checked
together. Seattle, Austin, and Miami correctly model no general state individual
income tax, but their employer-side assumptions still require that fuller review.

## Primary evidence used

### Definite findings

- Belgium FPS Finance: [2025 and 2026 tax rates and personal allowances](https://fin.belgium.be/en/private-individuals/tax-return/tax-rates-income/tax-rates)
- Denmark SKAT: [2026 employment and job allowances](https://skat.dk/borger/fradrag/arbejdsrelaterede-fradrag/beskaeftigelses-og-jobfradrag)
- Finland Vero: [2026 state earned-income tax scale](https://vero.fi/henkiloasiakkaat/verokortti-ja-veroilmoitus/tulot/ansiotulot/)
- Latvia VID: [social contributions and the €105,300 maximum](https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligatas-iemaksas), [solidarity tax](https://www.vid.gov.lv/en/solidarity-tax), and [personal income-tax rates](https://www.vid.gov.lv/en/personal-income-tax-rates)
- Spain Social Security: [additional solidarity contribution](https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/CotizacionRecaudacionTrabajadores/36537/practicas%2Bformativas?changeLanguage=es)
- Sweden Skatteverket: [2026 state-tax threshold](https://www.skatteverket.se/privat/etjansterochblanketter/svarpavanligafragor/inkomstavtjanst/privattjansteinkomsterfaq/narskamanbetalastatliginkomstskattochhurhogarden.5.10010ec103545f243e8000166.html) and [employer contributions](https://www.skatteverket.se/servicelankar/otherlanguages/englishengelska/businessesandemployers/startingandrunningaswedishbusiness/declaringtaxesbusinesses/filingapayereturn/employercontributions.4.2fb39afe18dabf1e4d24a3d.html)
- California FTB: [2025 tax-rate schedule](https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf) and [2025 standard deduction](https://www.ftb.ca.gov/file/personal/deductions/index.html)

### Other official sources inspected

- Albania Tax Administration: [2026 contribution bases](https://www.tatime.gov.al/d/8/45/45/1914/nga-1-janari-2026-rritet-paga-minimale-dhe-maksimale) and [salary PIT](https://www.tatime.gov.al/eng/c/4/96/108/tax-on-personal-income)
- Austria BMF: [2026 tax brackets and credits](https://www.bmf.gv.at/themen/steuern/arbeitnehmerveranlagung/steuertarif-steuerabsetzbetraege/steuertarif-steuerabsetzbetraege.html)
- Cyprus Ministry of Finance: [2026 tax calculator](https://taxtools.mof.gov.cy/)
- Czech Financial Administration: [employee and employer information](https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/zamestnanci-zamestnavatele/obecne-informace)
- Estonia EMTA: [tax rates](https://www.emta.ee/en/business-client/taxes-and-payment/income-and-social-taxes/tax-rates) and [basic exemption](https://www.emta.ee/en/private-client/taxes-and-payment/tax-incentives/calculation-basic-exemption)
- France URSSAF: [rates and ceilings](https://www.urssaf.fr/accueil/outils-documentation/taux-baremes.html)
- Germany BMF: [2026 tax changes](https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/das-aendert-sich-2026.html)
- Greece AADE: [Law 5246/2025 and 2026 income-tax reform](https://www.aade.gr/sites/default/files/2025-11/%CE%91%CE%A0%CE%9F%CE%A3%CE%A0%CE%91%CE%A3%CE%9C%CE%91%20%CE%A6%CE%95%CE%9A%20%CE%91%20198_2025%20%CE%9D%205246_2025.pdf)
- Hungary NAV: [social-security contribution guidance](https://nav.gov.hu/pfile/file?path=%2Fen%2Ftaxation%2Ftaxinfo%2Fsocial-security-contribution-and-social-contribution-tax-foreign-companies)
- Ireland Revenue: [USC thresholds](https://www.revenue.ie/en/jobs-and-pensions/usc/standard-rates-thresholds.aspx), [credits and bands](https://www.revenue.ie/en/personal-tax-credits-reliefs-and-exemptions/tax-relief-charts/index.aspx), and [income-tax calculation](https://www.revenue.ie/en/jobs-and-pensions/calculating-your-income-tax/how-income-tax-is-calculated.aspx)
- Italy INPS: [2026 employee contribution ceiling](https://www.inps.it/it/it/inps-comunica/notizie/dettaglio-news-page.news.2026.02.lavoratori-dipendenti-limite-minimo-di-retribuzione-giornaliera-2026.html)
- Lithuania VMI: [2026 employment-income bands](https://www.vmi.lt/evmi/5725)
- Luxembourg ACD: [individual income-tax scale](https://impotsdirects.public.lu/fr/az/t/tarif_pers.html)
- Netherlands Belastingdienst: [2026 income-tax brackets](https://www.belastingdienst.nl/wps/wcm/connect/nl/werk-en-inkomen/content/hoeveel-inkomstenbelasting-betalen) and [2026 payroll figures](https://odb.belastingdienst.nl/wp-content/uploads/2025/12/Cijferbijlage-2026-bij-Nieuwsbrief-LH-LH-209-1B61FD_TG.pdf)
- Norway Skatteetaten: [bracket tax](https://www.skatteetaten.no/satser/trinnskatt/?pageid=1932) and [ordinary income-tax overview](https://www.skatteetaten.no/en/person/foreign/are-you-intending-to-work-in-norway/the-tax-return/what-are-you-liable-to-pay-tax-on-in-norway/)
- Poland ZUS: [2026 annual contribution cap](https://www.zus.pl/en/o-zus/aktualnosci/-/asset_publisher/aktualnosci/content/id/13663769) and Ministry of Finance: [employment expenses](https://www.podatki.gov.pl/podatki-osobiste/pit/informacje-podstawowe/co-jest-opodatkowane/dochody-z-pracy)
- Portugal Tax Authority: [Personal Income Tax Code](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/irs/Pages/codigo-do-irs-indice.aspx) and [2026 withholding circular](https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/instrucoes_administrativas/Documents/Circular_1_2026.pdf)
- Serbia Tax Administration: [Personal Income Tax Law](https://www.purs.gov.rs/upload/media/2025/11/24/760462/Law_on_personal_income_tax.pdf)
- Slovenia FURS: [2026 general-allowance calculator](https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/dohodnina/dohodnina_dohodek_iz_zaposlitve/pripomocek_za_izracun_splosne_olajsave_v_letu_2026_pri_izracunu_akontacije_dohodnine_od_mesecnega_dohodka_iz_delovnega_razmerja) and [social-contribution bases](https://www.fu.gov.si/davki_in_druge_dajatve/podrocja/prispevki_za_socialno_varnost/osnove_za_placilo_ter_zneski_prispevkov_za_socialno_varnost)
- Turkey GİB: [2026 income-tax tariff](https://cdn.gib.gov.tr/api/gibportal-file/file/getFileResources?objectKey=arsiv%2Fyardim-kaynaklar%2Fyararli-bilgiler%2Fgelir-vergisi-tarifeleri%2Fgelir-vergisi-tarifesi-2026.pdf)
- United Kingdom GOV.UK: [2026/27 income-tax rates](https://www.gov.uk/government/publications/rates-and-allowances-income-tax/income-tax-rates-and-allowances-current-and-past) and [National Insurance rates](https://www.gov.uk/national-insurance-rates-letters/contribution-rates)
- Ukraine State Tax Service: [PIT rate guidance](https://www.tax.gov.ua/deklaratsiyna-kampaniya-2026/stavki-podatku-na-dohodi-fizichnih-osib-ta-viyskovogo-zboru)
- United States IRS: [2025 federal brackets](https://www.irs.gov/filing/federal-income-tax-rates-and-brackets) and [standard deduction](https://www.irs.gov/publications/p501); SSA: [2025 wage base](https://www.ssa.gov/oact/cola/autoAdj.html); California EDD: [2025 payroll rates](https://edd.ca.gov/en/payroll_taxes/rates_and_withholding/)

## Recommended correction order

1. Fix Belgium, Denmark, Finland, and California, with threshold-focused tests.
2. Implement Latvia and Spain high-income solidarity contributions before relying
   on their results above the ordinary contribution ceilings.
3. Decide and document the UK location scope.
4. Replace the explicitly calibrated/estimated France, Italy, Norway, Sweden,
   Switzerland, Serbia, and Montenegro logic with official worked examples.
5. Complete primary-source packs for every **Partial** and **Insufficient evidence**
   row. Each pack should record URL, publication/effective date, access date,
   exact constants derived from it, and at least one reproducible worked example.
