# Portugal — employee salary and employer-cost research for income year 2026

**Clean-room scope.** This dossier was reconstructed from Portuguese primary sources only. It does not rely on calculator code, generated datasets, prior audits, or other country dossiers. All web sources were accessed **2026-10-04**.

## 1. Reproducible profile and result boundary

The calculations assume:

- an individual resident in mainland Portugal for all of 2026;
- single, no spouse, no dependants, no disability, no other income or losses;
- ordinary private-sector employment under the general Social Security regime;
- no union dues, professional-order dues, voluntary pension contribution, benefit in kind, overtime, termination payment, or special exemption;
- no eligibility/election for *IRS Jovem* or another age-, career-, expatriate-, or activity-specific regime;
- gross cash salary `G` includes the statutory holiday and Christmas subsidies and is paid as **14 equal gross amounts**, `M = G / 14`: 12 ordinary monthly salaries, one holiday subsidy, and one Christmas subsidy;
- employment lasts the full calendar year, so both subsidies are earned in full;
- no meal allowance is included in `G` or added to employer cost;
- the employee has at least EUR 714.29 of eligible, NIF-linked general household invoices, and therefore receives the full EUR 250 general-family-expense credit. Because that is factual rather than automatic, a zero-credit sensitivity is stated below;
- annual amounts are computed to full precision and displayed to cents. Illustrative payroll withholding is rounded to the nearest cent for each of the 14 separately assessed payments. The official sources found do not state a universal payroll software rounding convention, so this cents convention is an explicit modelling assumption.

The municipality was not specified in the task. Municipal participation can reduce the resident's IRS by between 0% and 5% of the relevant net collection. Accordingly, final IRS and net pay are shown as a **range**: no municipal give-back through the maximum 5% give-back. This is more reproducible than silently selecting a municipality whose decision may concern a different income year.

## 2. National annual IRS liability

### 2.1 Category A income and specific deduction

All salary, including fixed or variable accessory remuneration, is Category A employment income. The annual specific deduction per employee is the greater of:

```text
8.54 × IAS
mandatory employee social-protection contributions, if those contributions exceed 8.54 × IAS
```

The 2026 IAS is EUR 537.13. Thus:

```text
8.54 × 537.13 = EUR 4,587.0902  (EUR 4,587.09 displayed)
employee Social Security = 11% × G
D = max(EUR 4,587.0902, 11% × G), limited to employment income
taxable income X = G − D
```

For the five requested salaries, the EUR 4,587.09 floor applies only at EUR 20,000; actual 11% contributions are the larger deduction at all other test points.

### 2.2 2026 general rates

Article 68 CIRS, as amended by the 2026 State Budget, provides:

| Taxable income (EUR) | Normal/marginal rate | Average rate at upper bound |
|---:|---:|---:|
| up to 8,342 | 12.50% | 12.500% |
| 8,342–12,587 | 15.70% | 13.579% |
| 12,587–17,838 | 21.20% | 15.823% |
| 17,838–23,089 | 24.10% | 17.705% |
| 23,089–29,397 | 31.10% | 20.579% |
| 29,397–43,090 | 34.90% | 25.130% |
| 43,090–46,566 | 43.10% | 26.472% |
| 46,566–86,634 | 44.60% | 34.856% |
| over 86,634 | 48.00% | — |

The statutory calculation is not merely `X × the top marginal rate`. Article 68(2) splits `X`: the completed lower bracket is charged using the table's average rate, and the excess using the next bracket's normal rate. For example, when `46,566 < X ≤ 86,634`:

```text
general collection B = 46,566 × 26.472% + (X − 46,566) × 44.60%
```

The examples below follow this prescribed average-rate method. Because published average rates have three decimals, mechanically summing marginal slices can differ by cents; the Article 68(2) method controls here.

### 2.3 Additional solidarity rate

Article 68-A adds:

```text
S = 0                                           if X ≤ 80,000
S = 2.5% × (X − 80,000)                        if 80,000 < X ≤ 250,000
S = 2.5% × 170,000 + 5% × (X − 250,000)        if X > 250,000
```

This is a national high-income addition, not a municipal surcharge.

### 2.4 Minimum-existence adjustment

The 2026 reference is the greater of EUR 12,880 and `1.5 × 14 × IAS`; EUR 12,880 is greater. Article 70(4)(a) disapplies the adjustment where gross income exceeds `2.2 × 14 × IAS`. In 2026 that cutoff is:

```text
2.2 × 14 × 537.13 = EUR 16,543.60
```

Every requested gross salary starts at EUR 20,000, so the minimum-existence adjustment is inapplicable to all five cases.

### 2.5 Credits and the meaning of “standard”

There is no unconditional flat personal allowance or personal tax credit for this profile. Article 78-B instead permits **35% of eligible general household invoices, capped at EUR 250 per taxpayer**. The invoice must be communicated to AT and associated with the taxpayer's NIF. The worked calculation assumes the cap is reached:

```text
C = min(35% × eligible general household invoices, EUR 250) = EUR 250
collection after modelled credit K = max(0, B − C)
```

The Article 78(7) overall cap covers the deductions in Article 78(1)(c)–(h), (k), and (m), not the general-family-expense deduction in (b). Other expense credits—health, education, rent/mortgage items where applicable, nursing homes, VAT invoice incentive, domestic work, charitable/fiscal benefits—depend on facts absent from this profile and are set to zero.

**Sensitivity:** if the taxpayer has no qualifying NIF-linked invoices, add EUR 250 to the pre-municipal IRS shown below; the municipal give-back base correspondingly rises by up to EUR 12.50.

### 2.6 Municipality-specific participation

Under Article 26 of the Local Finance Law, a municipality is entitled to up to 5% of IRS calculated on collection net of Article 78(1) deductions. If it chooses less than 5%, the difference multiplied by that net collection becomes a taxpayer deduction. AT's official liquidation layout puts the additional solidarity amount in “total collection”, then subtracts Article 78 deductions and the municipal benefit. Therefore, for this profile:

```text
pre-municipal collection Q = K + S
municipal benefit MB = (5% − municipality's chosen percentage) × Q
0 ≤ MB ≤ 5% × Q
final IRS T = Q − MB
```

This is location- and annual-decision-specific. As an illustration of why the year must not be inferred, Lisbon's 2026 municipal budget says its 2026 receipts/give-back relate to **2025 income**, calculated after Article 78 deductions. A decision labelled “2026” is therefore not automatically the rate applicable to 2026 income assessed in 2027. No municipality was supplied and the complete final set of municipal decisions applicable to 2026 income was not established from the primary sources by the access date. The results consequently retain the lawful 0%–5% benefit range.

## 3. Withholding is a prepayment, not final tax

Despacho 233-A/2026 applies from 1 January 2026 to mainland residents. For Table I (*não casado sem dependentes*), monthly withholding is:

```text
W(R) = max(0, R × table marginal rate − table fixed deduction)
```

The relevant Table I rows are:

| Monthly remuneration R (EUR) | Rate | Deduction |
|---:|---:|---:|
| up to 920 | 0% | 0 |
| up to 1,042 | 12.50% | `12.50% × 2.60 × (1,273.85 − R)` |
| up to 1,108 | 15.70% | `15.70% × 1.35 × (1,554.83 − R)` |
| up to 1,154 | 15.70% | 94.71 |
| up to 1,212 | 21.20% | 158.18 |
| up to 1,819 | 24.10% | 193.33 |
| up to 2,119 | 31.10% | 320.66 |
| up to 2,499 | 34.90% | 401.19 |
| up to 3,305 | 38.36% | 487.66 |
| up to 5,547 | 39.69% | 531.62 |
| up to 20,221 | 44.95% | 823.40 |
| over 20,221 | 47.17% | 1,272.31 |

Article 99-C(5) requires holiday and Christmas subsidies to be withheld **autonomously**, not added to the ordinary salary in the payment month. Because this dossier models 14 equal payments, illustrative annual withholding is `14 × W(G/14)`, after cents rounding on each payment.

Withholding is credited in the annual assessment under Article 78(2). It does not replace the Article 68 annual computation, credits, solidarity addition, or municipal benefit. Refunds in the worked table are therefore expected and do not imply a lower legal rate at payroll.

## 4. Social Security and statutory pay structure

### 4.1 Ordinary employee and employer rates

For an ordinary employee under the general regime:

```text
employee contribution = 11.00% × contributory remuneration
employer contribution = 23.75% × contributory remuneration
total = 34.75%
```

The Social Security guide identifies those rates for ordinary employees/teleworkers. The contributory code defines the base as gross remuneration due for professional activity and expressly includes base salary plus holiday, Christmas, Easter, and analogous subsidies. No ordinary upper earnings ceiling is specified for this real-remuneration case, so all `G` is used in the five calculations.

### 4.2 Holiday and Christmas subsidies

Labour Code Article 263 gives a worker a Christmas subsidy equal to one month's remuneration, payable by 15 December, with proportionality for entry, exit, or worker-related contract suspension. Article 264 grants holiday-period remuneration plus a holiday subsidy and says it is normally paid before leave unless agreed otherwise.

For a full-year employee this dossier therefore defines:

```text
base monthly salary = G / 14
12 base salaries + 1 holiday subsidy + 1 Christmas subsidy = G
```

Both subsidies are taxable employment income, in the Social Security base, and subject to autonomous IRS withholding. A contract quoting “annual gross” but excluding the two subsidies would describe a different `G` and cannot be compared directly with these examples.

### 4.3 Fundo de Garantia Salarial (FGS)

FGS is not added as a second payroll percentage. Article 14(2) of the FGS regime says employer financing comes from the employer-paid share of the **active-employment-policy component of the global contributory rate**. It is therefore funded within the 23.75% employer Social Security amount for this ordinary profile. Adding a separate FGS percentage would double count it.

### 4.4 Mandatory occupational-accident insurance

Law 98/2009 Article 79 requires the employer to transfer workplace-accident liability to an authorised insurer. Article 81 requires premiums to be graduated by accident risk, taking account of the activity and prevention conditions. The ASF likewise describes fixed- and variable-premium policies and remuneration-based reporting.

Consequently no universal statutory premium rate exists. Let `P_AT` be the employer's actual annual premium, including applicable insurance levies/taxes. Then:

```text
known statutory payroll cost = G + 23.75% × G = 1.2375 × G
exact total employer cost = 1.2375 × G + P_AT
```

The ASF lists insurer-level charges relevant to pricing (including 0.15% of insured salaries for the Workplace Accident Fund and 5% stamp duty on accident-insurance premiums), but those do **not** establish the employer's commercial premium. No invented 1% or other proxy is used.

## 5. Meal allowance boundary (excluded from the examples)

A private employer is not universally required by the Labour Code to pay a meal allowance; it may arise from contract, established practice, or collective agreement. CIRS Article 2(3)(b)(2) taxes only the portion above the public-sector legal reference, or above that reference by 70% where paid through meal vouchers/cards. Article 2(14) ties the limits to the public-sector amount.

The official AT guidance identifies the reference as EUR 6.00 per workday in cash. With the current 70% voucher uplift, the corresponding voucher/card limit is EUR 10.20 per workday. The contributory code subjects meal allowance on the same incidence terms as IRS. Thus, under the facts used here:

- modelled meal allowance: EUR 0;
- no addition to gross, employee deductions, or employer cost;
- if one is introduced, days actually eligible, payment medium, and any excess must be supplied before calculating tax and contributions.

## 6. Worked calculations

### 6.1 Annual liability and employee net

Definitions: `B` is Article 68 general collection; `S` is the additional solidarity charge; `K = B − EUR 250`; pre-municipal collection is `Q = K + S`; municipal benefit ranges from zero to `5% × Q`; final net is `G − 11%G − final IRS`. Values are EUR.

| G | G/14 | Employee SS 11% | Specific deduction D | Taxable X | General B | Solidarity S | K after EUR250 credit | Municipal benefit 0…5%Q | Final IRS range (max…min) | Employee net range (min…max) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 20,000.00 | 1,428.57 | 2,200.00 | 4,587.09 | 15,412.91 | 2,308.28 | 0.00 | 2,058.28 | 0.00…102.91 | 2,058.28…1,955.37 | 15,741.72…15,844.63 |
| 60,000.00 | 4,285.71 | 6,600.00 | 6,600.00 | 53,400.00 | 15,374.92 | 0.00 | 15,124.92 | 0.00…756.25 | 15,124.92…14,368.67 | 38,275.08…39,031.33 |
| 100,000.00 | 7,142.86 | 11,000.00 | 11,000.00 | 89,000.00 | 31,332.83 | 225.00 | 31,082.83 | 0.00…1,565.39 | 31,307.83…29,742.44 | 57,692.17…59,257.56 |
| 200,000.00 | 14,285.71 | 22,000.00 | 22,000.00 | 178,000.00 | 74,052.83 | 2,450.00 | 73,802.83 | 0.00…3,812.64 | 76,252.83…72,440.19 | 101,747.17…105,559.81 |
| 600,000.00 | 42,857.14 | 66,000.00 | 66,000.00 | 534,000.00 | 244,932.83 | 18,450.00 | 244,682.83 | 0.00…13,156.64 | 263,132.83…249,976.19 | 270,867.17…284,023.81 |

Example detail at `G = EUR 100,000`:

```text
employee SS = 100,000 × 11% = 11,000
D = max(4,587.0902, 11,000) = 11,000
X = 100,000 − 11,000 = 89,000
B = 86,634 × 34.856% + (89,000 − 86,634) × 48%
  = 31,332.82704
S = (89,000 − 80,000) × 2.5% = 225
K = 31,332.82704 − 250 = 31,082.82704
Q = 31,082.82704 + 225 = 31,307.82704
MB = 0 … 5% × 31,307.82704 = 0 … 1,565.391352
final IRS = Q − MB
          = 31,307.83 … 29,742.44
net = 100,000 − 11,000 − final IRS
    = 57,692.17 … 59,257.56
```

### 6.2 Illustrative 2026 withholding and annual reconciliation

| G | Equal payment R=G/14 | Withholding per payment | 14-payment withholding | Expected annual refund range* |
|---:|---:|---:|---:|---:|
| 20,000 | 1,428.57 | 150.96 | 2,113.44 | 55.16…158.07 |
| 60,000 | 4,285.71 | 1,169.38 | 16,371.32 | 1,246.40…2,002.65 |
| 100,000 | 7,142.86 | 2,387.31 | 33,422.34 | 2,114.51…3,679.90 |
| 200,000 | 14,285.71 | 5,598.03 | 78,372.42 | 2,119.59…5,932.23 |
| 600,000 | 42,857.14 | 18,943.40 | 265,207.60 | 2,074.77…15,231.41 |

\* `withholding − final IRS`, assuming the full EUR 250 invoice credit and no other payments on account. The low end has no municipal benefit; the high end has the full 5% benefit. Actual assessment can differ with payroll timing, cents rules, expenses, municipality, and facts outside the profile.

At EUR 60,000, for example, `R = 4,285.714...`, so the Table I row up to EUR 5,547 gives:

```text
W = R × 39.69% − 531.62
  = EUR 1,169.38 per separately assessed payment (cents assumption)
annual withholding = 14 × 1,169.38 = EUR 16,371.32
```

### 6.3 Employer fixed statutory cost and unresolved insurance

| G | Employer Social Security 23.75% | Known salary + employer SS | Exact employer cost |
|---:|---:|---:|---:|
| 20,000 | 4,750.00 | 24,750.00 | `24,750.00 + P_AT` |
| 60,000 | 14,250.00 | 74,250.00 | `74,250.00 + P_AT` |
| 100,000 | 23,750.00 | 123,750.00 | `123,750.00 + P_AT` |
| 200,000 | 47,500.00 | 247,500.00 | `247,500.00 + P_AT` |
| 600,000 | 142,500.00 | 742,500.00 | `742,500.00 + P_AT` |

FGS funding is already inside the 23.75%. `P_AT` cannot be bounded from salary alone because activity risk, claims/prevention conditions, policy terms, insurer, and insured remuneration details are missing. The “known” column is therefore a fixed statutory subtotal, not a claim that accident insurance costs zero.

## 7. Universal rules versus variable assumptions

### Nationally fixed for this profile

- 2026 Article 68 thresholds/rates and Article 68-A solidarity rates;
- 2026 IAS of EUR 537.13 and the `8.54 × IAS` specific-deduction rule;
- ordinary employee 11% and employer 23.75% Social Security rates on contributory remuneration;
- inclusion of holiday and Christmas subsidies in the contributory base;
- statutory right to holiday and Christmas subsidies for a full-year employee;
- autonomous withholding of those subsidies;
- mandatory workplace-accident insurance;
- FGS financing within the employer share of the global contribution rate.

### Municipality-, expense-, sector-, employer-, or contract-specific

- municipal IRS percentage and hence the municipal benefit;
- eligible household, health, education, housing, VAT-invoice, and other credits;
- *IRS Jovem* and other personal regimes;
- collective-agreement additions and meal allowance;
- whether compensation is quoted as 12 monthly amounts plus statutory subsidies, paid in duodecimos, or described under another convention;
- occupational-accident premium;
- contributory incentives/exemptions for particular hires or employers;
- payroll cents implementation.

## 8. Primary-source register

All sources below were accessed 2026-10-04.

1. **Autoridade Tributária e Aduaneira, CIRS Article 68, “Taxas gerais”**, current text amended by Lei 73-A/2025 of 30 December 2025. Pinpoint: paragraph 1 table gives all nine 2026 bands/rates; paragraph 2 gives the average-rate-plus-excess method.
   <https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68.aspx>

2. **Lei n.º 73-A/2025, Orçamento do Estado para 2026**, published 30 December 2025. Pinpoint: amendments to CIRS Article 68 and 2026 income-tax rules.
   <https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Lei-73-A-2025.pdf>

3. **AT, CIRS Article 25, “Rendimentos do trabalho dependente: deduções”**, current text (Article 25(1)(a), 25(2)). Pinpoint: `8.54 × IAS`; mandatory social-protection contributions replace that amount when larger.
   <https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs25.aspx>

4. **Portaria n.º 480-A/2025/1**, published 30 December 2025, annual IAS update; corroborated in **Segurança Social, Guia Prático — Inscrição, Alteração e Cessação do Serviço Doméstico**, 2026 edition, p.17. Pinpoint: “O valor do IAS em 2026 é igual a 537,13€.”
   <https://diariodarepublica.pt/dr/detalhe/portaria/480-a-2025-993056222>
   <https://www.seg-social.pt/ptss/pssd/documento/cmc1xnoen00dakl2y9vd3tedj>

5. **AT, CIRS Article 68-A, “Taxa adicional de solidariedade”**, current text. Pinpoint: paragraphs 1–2, 2.5% over EUR 80,000 through EUR 250,000 and 5% above EUR 250,000.
   <https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs68a.aspx>

6. **AT, CIRS Article 70, “Mínimo de existência”**, current text amended by Lei 73-A/2025. Pinpoint: paragraph 1 EUR 12,880/IAS reference; paragraph 4(a) gross-income exclusion at `2.2 × 14 × IAS`.
   <https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs70.aspx>

7. **AT, CIRS Article 78, “Deduções à coleta”**, current page dated 18 May 2026. Pinpoint: paragraph 1 deduction categories; paragraph 2 withholding as credit; paragraph 7 capped deduction categories (which omit Article 78(1)(b)).
   <https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78.aspx>

8. **AT, CIRS Article 78-B, “Dedução das despesas gerais familiares”**, current text amended by Decreto-Lei 49/2025 effective 1 July 2025. Pinpoint: paragraph 1, 35% and EUR 250 per-taxpayer cap; paragraphs 3 and 5, NIF/invoice communication requirements.
   <https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs78b.aspx>

9. **Despacho n.º 233-A/2026, Tabelas de retenção na fonte para o continente — 2026**, published Diário da República no. 3/2026, supplement, Series II, 6 January 2026; effective from 1 January 2026. Pinpoint: paragraphs 3(b), 10, 12, 15 and Table I on PDF pp.4–5 (document pagination), including every threshold, rate, and deduction used above.
   <https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Despacho-233-A-2026.pdf>

10. **AT, CIRS Article 99-C, “Aplicação da retenção na fonte à categoria A”**, current text. Pinpoint: paragraph 5 autonomous holiday/Christmas withholding; paragraph 6 proportional withholding if subsidies are fractionated.
    <https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs99c.aspx>

11. **Segurança Social, Guia Prático — Inscrição, Vinculação e Cessação de Atividade Trabalhador/Estagiário por Conta de Outrem**, 2026-current guide. Pinpoint: p.15 table, ordinary employee/global rates 23.75% employer, 11% employee, 34.75% total.
    <https://www.seg-social.pt/ptss/pssd/documento/cmc1xlxpq00d9kl2y0p3inyft>

12. **Lei n.º 110/2009, Código dos Regimes Contributivos do Sistema Previdencial**, published 16 September 2009, consolidated current text supplied by DGSS. Pinpoint: Article 44 gross-remuneration base; Article 46(1) remuneration concept; Article 46(2)(a) base salary and (h) holiday/Christmas subsidies; Article 46(3) IRS-aligned incidence for meal allowances; Articles 49–51 composition of the global rate.
    <https://sisscontent.seg-social.pt/documents/10152/113014/C%C3%B3digo%2Bcontributivo%2B-%2Breda%C3%A7%C3%A3o%2Bem%2Bvigor/1e56fad5-0e2a-42c2-b94c-194c4aa64f74>

13. **Código do Trabalho, Lei n.º 7/2009, consolidated official text**. Pinpoint: Article 263(1), Christmas subsidy equals one month and is due by 15 December; Article 264(1)–(3), holiday remuneration/subsidy and normal payment timing.
    <https://guiadoinvestidor.dre.pt/DRE_Investidores/PDF.aspx?DecretoLeiId=38&Idioma=1>

14. **Decreto-Lei n.º 59/2015, Novo regime do Fundo de Garantia Salarial**, published 21 April 2015, effective first working day of the following month. Pinpoint: annex Article 14(2), employer funding through the active-employment-policy portion of the employer's share of the global contribution rate.
    <https://files.dre.pt/gratuitos/1s/2015/04/07700.pdf>

15. **Lei n.º 98/2009, Regime de reparação de acidentes de trabalho**, published 4 September 2009, effective 1 January 2010. Pinpoint: Article 79(1), compulsory transfer to authorised insurer; Article 81(2)–(3), premium graduation by activity risk and prevention conditions.
    <https://files.dre.pt/1s/2009/09/17200/0589405920.pdf>

16. **ASF, “Seguro de Acidentes de Trabalho”**, current consumer guidance; and **“Taxas cobradas através do portal da ASF”**, updated 11 February 2026. Pinpoint: mandatory insurance and remuneration-sensitive benefits; FAT charge of 0.15% of insured salaries. ASF's separate **“Taxas e impostos sem intervenção da ASF”**, also updated 11 February 2026, identifies 5% stamp duty on accident-insurance premiums.
    <https://www.fat.asf.com.pt/pt/web/site-pc/seguros/seguro-de-acidentes-de-trabalho>
    <https://www.asf.com.pt/taxas-cobradas-atraves-do-portal-asf>
    <https://www.asf.com.pt/taxas-e-impostos-sem-intervencao-da-asf>

17. **AT, CIRS Article 2, “Rendimentos da categoria A”**, current text amended by Lei 45-A/2024 of 31 December 2024. Pinpoint: paragraph 2 broad remuneration; paragraph 3(b)(2) meal allowance excess and 70% voucher uplift; paragraph 14 public-sector reference.
    <https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs2.aspx>

18. **AT binding information, Processo 27870**, issued/published 2025. Pinpoint: point 8 confirms EUR 6.00 cash and EUR 10.20 card/voucher daily references; point 10 explains private-sector treatment.
    <https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/informacoes_vinculativas/rendimento/cirs/Documents/PIV_27870.pdf>

19. **Lei n.º 73/2013, Regime financeiro das autarquias locais**, published 3 September 2013, as amended; official AT-hosted **Lei n.º 51/2018**, published 16 August 2018. Pinpoint: Article 26(1), up to 5% participation on collection net of Article 78(1) deductions; Article 26(4), difference from 5% is a taxpayer deduction.
    <https://files.dre.pt/gratuitos/1s/2013/09/16900.pdf>
    <https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Lei_51_2018.pdf>

20. **Câmara Municipal de Lisboa, Orçamento 2026 da Cidade de Lisboa**, approved December 2025. Pinpoint: p.21 explains 5% give-back in the 2026 budget relates to 2025 income and is calculated on collection after Article 78 deductions. This source supports the timing warning, not a rate assumed in the calculations.
    <https://www.lisboa.pt/fileadmin/info_administrativa/orcamento/2026/op/Orcamento_2026_2030.pdf>

21. **AT, “Taxa Efetiva de Tributação (TET) em IRS para o ano de 2023”**, official liquidation-order explainer published for the 2023 assessment campaign. Pinpoint: liquidation lines 15 and 18 put the additional tax in total collection; lines 19–22 then subtract collection deductions and municipal benefit. The document is used only to resolve statutory calculation order, not for any 2026 rate or threshold.
    <https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/IRS/IRS_2023/Documents/Formula_Taxa_Tributacao_Efetiva_IRS2023.pdf>

## 9. Evidence assessment and unresolved items

**Strongest evidence.** The annual brackets and exact withholding parameters come directly from the current CIRS and the in-force 2026 withholding order. The employee/employer Social Security split is directly stated in the 2026-current Segurança Social guide, while the contributory code expressly places both statutory subsidies in the base. FGS treatment is unusually clear in Article 14(2) of its own regime.

**Weakest / unresolved evidence.** Exact total employer cost cannot be produced without an insurer quote and workplace risk facts; the law deliberately makes the premium risk-sensitive. The municipal benefit applicable to 2026 income cannot be selected without a municipality and its decision for that income year. The EUR 250 credit depends on actual NIF-linked invoices. Finally, the primary material located specifies formulas and autonomous payment treatment but not a single universal payroll cents-rounding algorithm. These items are exposed as variables or sensitivities rather than guessed.
