# 2026 European research coverage

This ledger tracks clean-room primary-source dossiers. “Dossier complete” means
the research has been written; it does not mean the calculator has been corrected
or certified.

All **36 country dossiers and code comparisons are complete** as of 2026-10-04.
Each dossier was reconstructed without reading that country's existing
implementation or generated outputs. The comparison pass found 128 review items;
see the [consolidated comparison summary](comparisons/SUMMARY.md). Calculator
logic has not yet been changed from these findings.

| Country | Research | Code comparison | Integration | Independent review |
|---|---|---|---|---|
| Albania | [Dossier complete](albania.md) | [Compared](comparisons/albania.md) | Core fixes implemented | Pending |
| Austria | [Dossier complete](austria.md) | [Compared](comparisons/austria.md) | Pending | Pending |
| Belgium | [Dossier complete](belgium.md) | [Compared](comparisons/belgium.md) | Pending | Pending |
| Bulgaria | [Dossier complete](bulgaria.md) | [Compared](comparisons/bulgaria.md) | Core fixes implemented | Pending |
| Croatia | [Dossier complete](croatia.md) | [Compared](comparisons/croatia.md) | Pending | Pending |
| Cyprus | [Dossier complete](cyprus.md) | [Compared](comparisons/cyprus.md) | Pending | Pending |
| Czech Republic | [Dossier complete](czech-republic.md) | [Compared](comparisons/czech-republic.md) | Pending | Pending |
| Denmark | [Dossier complete](denmark.md) | [Compared](comparisons/denmark.md) | Pending | Pending |
| Estonia | [Dossier complete](estonia.md) | [Compared](comparisons/estonia.md) | Pending | Pending |
| Finland | [Dossier complete](finland.md) | [Compared](comparisons/finland.md) | Pending | Pending |
| France | [Dossier complete](france.md) | [Compared](comparisons/france.md) | Pending | Pending |
| Germany | [Dossier complete](germany.md) | [Compared](comparisons/germany.md) | Pending | Pending |
| Greece | [Dossier complete](greece.md) | [Compared](comparisons/greece.md) | Pending | Pending |
| Hungary | [Dossier complete](hungary.md) | [Compared](comparisons/hungary.md) | Pending | Pending |
| Ireland | [Dossier complete](ireland.md) | [Compared](comparisons/ireland.md) | Pending | Pending |
| Italy | [Dossier complete](italy.md) | [Compared](comparisons/italy.md) | Pending | Pending |
| Latvia | [Dossier complete](latvia.md) | [Compared](comparisons/latvia.md) | Pending | Pending |
| Lithuania | [Dossier complete](lithuania.md) | [Compared](comparisons/lithuania.md) | Core fixes implemented | Pending |
| Luxembourg | [Dossier complete](luxembourg.md) | [Compared](comparisons/luxembourg.md) | Pending | Pending |
| Malta | [Dossier complete](malta.md) | [Compared](comparisons/malta.md) | Core fixes implemented | Pending |
| Moldova | [Dossier complete](moldova.md) | [Compared](comparisons/moldova.md) | Core fixes implemented | Pending |
| Montenegro | [Dossier complete](montenegro.md) | [Compared](comparisons/montenegro.md) | Core fixes implemented | Pending |
| Netherlands | [Dossier complete](netherlands.md) | [Compared](comparisons/netherlands.md) | Pending | Pending |
| Norway | [Dossier complete](norway.md) | [Compared](comparisons/norway.md) | Pending | Pending |
| Poland | [Dossier complete](poland.md) | [Compared](comparisons/poland.md) | Core fixes implemented | Pending |
| Portugal | [Dossier complete](portugal.md) | [Compared](comparisons/portugal.md) | Core fixes implemented | Pending |
| Romania | [Dossier complete](romania.md) | [Compared](comparisons/romania.md) | Pending | Pending |
| Serbia | [Dossier complete](serbia.md) | [Compared](comparisons/serbia.md) | Pending | Pending |
| Slovakia | [Dossier complete](slovakia.md) | [Compared](comparisons/slovakia.md) | Core fixes implemented | Pending |
| Slovenia | [Dossier complete](slovenia.md) | [Compared](comparisons/slovenia.md) | Core fixes implemented | Pending |
| Spain | [Dossier complete](spain.md) | [Compared](comparisons/spain.md) | Pending | Pending |
| Sweden | [Dossier complete](sweden.md) | [Compared](comparisons/sweden.md) | Pending | Pending |
| Switzerland | [Dossier complete](switzerland.md) | [Compared](comparisons/switzerland.md) | Pending | Pending |
| Turkey | [Dossier complete](turkey.md) | [Compared](comparisons/turkey.md) | Core fixes implemented | Pending |
| United Kingdom | [Dossier complete](united-kingdom.md) | [Compared](comparisons/uk.md) | Pending | Pending |
| Ukraine | [Dossier complete](ukraine.md) | [Compared](comparisons/ukraine.md) | Core fixes implemented | Pending |

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

## Comparison method

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

That comparison is now recorded in the linked country files. The next phase is
reviewed implementation, beginning with isolated confirmed corrections and adding
regression vectors before broader formula rebuilds.
