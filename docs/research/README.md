# Independent formula research

This directory contains clean-room research dossiers used to verify the salary
calculator. Researchers reconstruct a jurisdiction from primary official sources
without reading the existing formula implementation or its generated outputs.

The dossiers are evidence, not executable logic. A separate integration pass must:

1. compare the dossier with the existing implementation;
2. resolve every open question and location/sector choice;
3. add source metadata and authoritative regression examples;
4. update the formula, generated data, and calculation reference together; and
5. obtain an independent review for material or ambiguous changes.

## Required profile

Unless a dossier records a necessary jurisdiction-specific exception, research uses:

- resident employee;
- single, no spouse or dependants;
- ordinary private-sector employment;
- standard/default deductions and credits only;
- regular annual gross cash compensation;
- no optional pension, benefits, equity, bonus, or special expatriate regime; and
- the tax year shown in the dossier.

Researchers must distinguish universal statutory rules from regional, municipal,
sectoral, risk-class, insurer, age, employer-history, or employee-choice inputs.
Variable inputs must not be presented as universally accurate constants.

## Evidence standard

Use primary sources: tax and social-security authorities, legislation, official
calculators, official rate tables, and official worked examples. Secondary sources
may help locate material but do not establish a value. Every implemented constant
should ultimately have:

- a direct source URL and page/table title;
- publication date, effective date, and access date;
- a pinpoint showing exactly what the source supports;
- any translation or interpretation caveat; and
- at least one independently reproducible threshold or worked-example test.

Unknowns stay unknown. Never fill an evidence gap with a plausible rate.

The [2026 European coverage ledger](2026/README.md) links every completed dossier.

## Workflow states

- **Researching** — clean-room primary-source reconstruction is in progress.
- **Dossier complete** — research exists, but has not been compared to the code.
- **Compared** — discrepancies and matches are recorded without modifying logic.
- **Integrated** — approved changes and regression tests are implemented.
- **Reviewed** — a second independent pass validates the integrated result.

The clean-room research phase is complete for all 36 European jurisdictions. Code
comparison, integration, and independent review remain separate follow-up phases.
