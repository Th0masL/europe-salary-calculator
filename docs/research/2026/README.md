# 2026 European research coverage

This ledger tracks clean-room primary-source dossiers. “Dossier complete” means
the research has been written; it does not mean the calculator has been corrected
or certified.

All **36 country dossiers are complete** as of 2026-10-04. Each was reconstructed
without reading that country's existing implementation or generated outputs. A
separate comparison pass is still required before changing calculator logic.

| Country | Research | Code comparison | Integration | Independent review |
|---|---|---|---|---|
| Albania | [Dossier complete](albania.md) | Pending | Pending | Pending |
| Austria | [Dossier complete](austria.md) | Pending | Pending | Pending |
| Belgium | [Dossier complete](belgium.md) | Pending | Pending | Pending |
| Bulgaria | [Dossier complete](bulgaria.md) | Pending | Pending | Pending |
| Croatia | [Dossier complete](croatia.md) | Pending | Pending | Pending |
| Cyprus | [Dossier complete](cyprus.md) | Pending | Pending | Pending |
| Czech Republic | [Dossier complete](czech-republic.md) | Pending | Pending | Pending |
| Denmark | [Dossier complete](denmark.md) | Pending | Pending | Pending |
| Estonia | [Dossier complete](estonia.md) | Pending | Pending | Pending |
| Finland | [Dossier complete](finland.md) | Pending | Pending | Pending |
| France | [Dossier complete](france.md) | Pending | Pending | Pending |
| Germany | [Dossier complete](germany.md) | Pending | Pending | Pending |
| Greece | [Dossier complete](greece.md) | Pending | Pending | Pending |
| Hungary | [Dossier complete](hungary.md) | Pending | Pending | Pending |
| Ireland | [Dossier complete](ireland.md) | Pending | Pending | Pending |
| Italy | [Dossier complete](italy.md) | Pending | Pending | Pending |
| Latvia | [Dossier complete](latvia.md) | Pending | Pending | Pending |
| Lithuania | [Dossier complete](lithuania.md) | Pending | Pending | Pending |
| Luxembourg | [Dossier complete](luxembourg.md) | Pending | Pending | Pending |
| Malta | [Dossier complete](malta.md) | Pending | Pending | Pending |
| Moldova | [Dossier complete](moldova.md) | Pending | Pending | Pending |
| Montenegro | [Dossier complete](montenegro.md) | Pending | Pending | Pending |
| Netherlands | [Dossier complete](netherlands.md) | Pending | Pending | Pending |
| Norway | [Dossier complete](norway.md) | Pending | Pending | Pending |
| Poland | [Dossier complete](poland.md) | Pending | Pending | Pending |
| Portugal | [Dossier complete](portugal.md) | Pending | Pending | Pending |
| Romania | [Dossier complete](romania.md) | Pending | Pending | Pending |
| Serbia | [Dossier complete](serbia.md) | Pending | Pending | Pending |
| Slovakia | [Dossier complete](slovakia.md) | Pending | Pending | Pending |
| Slovenia | [Dossier complete](slovenia.md) | Pending | Pending | Pending |
| Spain | [Dossier complete](spain.md) | Pending | Pending | Pending |
| Sweden | [Dossier complete](sweden.md) | Pending | Pending | Pending |
| Switzerland | [Dossier complete](switzerland.md) | Pending | Pending | Pending |
| Turkey | [Dossier complete](turkey.md) | Pending | Pending | Pending |
| United Kingdom | [Dossier complete](united-kingdom.md) | Pending | Pending | Pending |
| Ukraine | [Dossier complete](ukraine.md) | Pending | Pending | Pending |

## Material cautions carried into comparison

- **Belgium:** annual gross alone cannot determine work-bonus, municipal, sector,
  holiday-pay, wage-moderation, and final special-contribution treatment.
- **Denmark:** exact employer cost needs sector, AES/AUB, maternity-scheme, and
  commercial accident-insurance facts.
- **Finland and Italy:** the employer totals use explicitly labelled official
  averages or fixed classification scenarios rather than universal rates.
- **France:** the income-tax result uses law in force on 2026-10-04; the Finance
  Act for 2027 may still alter final taxation of 2026 income. Employer cost also
  needs location, accident-risk, health-plan, and collective-agreement inputs.
- **Ireland:** PRSI changes during October 2026 and MyFutureFund depends on pay
  dates and enrolment status; the dossier therefore fixes a weekly-pay convention.
- **Montenegro:** the 2026 annual pension-contribution maximum had not yet been
  promulgated. High-earner results are in-year withholding before any later refund.
- **Netherlands:** an official appendix contains an internally inconsistent labour-
  credit endpoint; the dossier records the conflict and follows the current formula.
- **Portugal:** the general-expense credit and municipal benefit depend on facts
  not inferable from salary; workplace-accident insurance remains variable.
- **Serbia:** final supplementary annual tax depends on the official 2026 average
  salary, which will only be published after the year.
- **Spain:** IRPF is regional and occupational-accident rates are activity-specific;
  the dossier fixes Madrid and an office-only occupation.
- **Switzerland:** occupational pension and accident-insurance premiums require a
  plan, age, and risk class; the numeric result is a Zürich fixed-core benchmark.
- **United Kingdom:** Scotland requires a separate income-tax calculation. Employer
  cost also depends on employer-wide allowance, levy, and pension facts.

Other dossiers carry narrower rounding, payment-timing, employer-classification,
or source-publication caveats in their evidence sections. These must remain visible
during comparison rather than being collapsed into unsupported universal rates.

## Next phase

For each country, a separate integrator should compare the dossier with the current
module and record:

1. exact matches;
2. confirmed mismatches;
3. unsupported current assumptions;
4. product choices needed for variable regional, sectoral, or employer inputs; and
5. authoritative regression vectors to add before implementation.

No formula should be changed merely because a scenario differs: first determine
whether the product intentionally models the same employee, location, pay timing,
and employer classification as the dossier.
