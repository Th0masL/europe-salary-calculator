# France — 2026 implementation comparison

## Compared artifacts

- Dossier: `docs/research/2026/france.md` (official URSSAF/Agirc-Arrco/legislation sources, accessed 2026-10-04).
- Implementation: `tools/calc/france.py`.

## Implementation update — 2026-10-04

The employee path now uses the official CSG base, 2026 expense cap, décote and
CEHR flow. Employer output is the dossier's deterministic statutory subtotal with
2026 RGDU; invented AT-MP/health/mobility/extras were removed and remain excluded.

## Current implementation scenario

Resident single cadre, 12 regular payments and nominally a large metropolitan employer. The module describes itself as approximate and adds an 8% Île-de-France “extras” layer without employer/location inputs.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| Critical | Confirmed mismatch | CSG/CRDS base | The module applies the 1.75% allowance to all gross and excludes employer-funded mandatory cadre providence. Officially the allowance is limited to four PASS and employer health/providence funding enters at 100%. Dossier CSG bases are EUR19,950/59,670.90/98,970.90/197,356.70/597,356.70, not `98.25% × G`. | Dossier §§2 S11-S13, 3, 5; `france.py:65,71-73`. |
| High | Confirmed mismatch | Income tax | The scale breaks match, but the module uses the old EUR14,171 expense cap, omits the décote and uses an approximate RFR/CEHR flow. The law-as-enacted dossier uses the EUR14,555 cap; omission of the décote drives the low-income error. | Dossier §§1, 4-5; `france.py:51-53,93-108`. |
| Critical | Confirmed mismatch | Employer reductions | Employer sickness/family thresholds and the statement that no general reduction applies use the superseded pre-2026 model. The dossier applies the 2026 RGDU up to 3 SMIC, including EUR1,308 at EUR60k. | Dossier §2 S4-S7 and §6; `france.py:23-25,49,81-89`. |
| Critical | Unsupported assumption | Employer extras | The module adds 2% AT-MP and 8% of gross for mutuelle/providence/mobility/CSE, although those inputs are location, contract, activity and employer specific. It also cannot represent mandatory health-plan euro premiums. | Dossier §§1, 6, 8; `france.py:25,29-35,55-58,86-89,109`. |
| High | Confirmed mismatch | Employer components | Several rates/bases differ from final 2026 rules (including old-age uncapped and apprenticeship structure), and minimum cadre providence/forfait social are not represented in the official-base order. | Dossier §§2-3, 6; `france.py:77-90`. |

## Matches

- PASS EUR48,060, T1/T2/P8 structure, employee old-age and Agirc-Arrco core rates, and general deduction of eligible contributions before the 10% professional expense deduction broadly match.
- The code correctly recognizes that exact French employer cost is variable, but then quantifies invented rates instead of keeping them algebraic.

## Output impact

Employer dossier numbers are deterministic subtotals excluding AT-MP, mobility, health premium and sector/company charges, so employer deltas are not like-for-like totals.

| Gross EUR | Module net | Dossier cash after tax* | Net delta | Module cost | Dossier subtotal | Difference |
|---:|---:|---:|---:|---:|---:|---:|
| 20,000 | 15,479.85 | 15,798.05 | -318.20 | 28,772.40 | 20,622.40† | +8,150.00 |
| 60,000 | 41,138.29 | 41,081.60 | +56.69 | 89,984.69 | 84,618.97 | +5,365.72 |
| 100,000 | 64,244.81 | 64,188.12 | +56.69 | 151,617.49 | 142,695.77 | +8,921.72 |
| 200,000 | 113,954.96 | 114,054.28 | -99.32 | 302,665.81 | 284,285.17 | +18,380.64 |
| 600,000 | 290,303.63 | 290,195.27 | +108.36 | 859,592.55 | 802,975.32 | +56,617.23 |

`*` Before unresolved employee health premium. `†` EUR20k is an invalid full-time cadre fact and only a mechanical stress row.

## Recommended disposition

Implement the official CSG base, final scale/expense cap/décote, and 2026 RGDU. Remove representative employer extras from the deterministic total; require AT-MP, municipality/mobility and health-contract inputs or return an algebraic subtotal plus unknowns.

## Regression vectors

Use the dossier's five employee rows and deterministic employer subtotals. EUR20k tests décote but must remain marked as a part-time/incomplete-year stress case; EUR60k tests RGDU; EUR600k tests the four-PASS CSG allowance limit, P8 and CEHR.
