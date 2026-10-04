# Portugal — implementation comparison

## Compared artifacts

- Independent dossier: `docs/research/2026/portugal.md`
- Current implementation: `tools/calc/portugal.py`
- Comparison date: 2026-10-04

## Implementation update — 2026-10-04

The 8.54×IAS specific-deduction floor was implemented and the separately added
FGS charge removed. The zero-invoice-credit/zero-municipal-benefit scenario and
estimated 1% office accident premium remain explicitly documented assumptions.

## Current implementation scenario

Single mainland employee; annual gross includes 14 payments. The module assumes no municipal give-back, no invoice credit, a separate 1% FGS charge, and a flat 1% accident premium.

## Findings

| Severity | Classification | Area | Finding | Evidence / code |
|---|---|---|---|---|
| High | Confirmed mismatch | Specific deduction | `SPECIFIC_DEDUCTION=4104` is stale. For 2026 the floor is 8.54×IAS = EUR 4,587.09. It affects the EUR 20k vector. | Dossier §2.1. |
| Medium | Scenario difference | Invoice credit | The dossier baseline assumes EUR 250 of eligible NIF-linked household invoices; the module assumes zero. Both are possible, but the module's statement that there is no credit is incomplete. | Dossier §2.5. |
| Medium | Product decision | Municipality | The module silently chooses zero municipal benefit; the dossier establishes a 0%–5% range because municipality/year is unspecified. | Dossier §2.6. |
| High | Confirmed mismatch | FGS | The module adds `EMPLOYER_FGS=1%`; FGS is financed inside the 23.75% global employer rate. This double counts EUR 200/600/1,000/2,000/6,000 at the vectors. | Dossier §4.3. |
| Medium | Unsupported assumption | Accident insurance | A fixed 1% commercial premium is not authoritative; statute makes the premium risk/insurer-specific. | Dossier §4.4; `EMPLOYER_WORK_ACCIDENT=0.01`. |

## Matches

The 11%/23.75% social rates, 2026 IRS brackets, solidarity addition, uncapped base, and annual-gross treatment of holiday/Christmas subsidies agree.

## Output impact

The dossier net range includes a EUR 250 invoice credit and 0%–5% municipal benefit. Module net is compared first with that published range; its fixed employer cost is compared with the dossier's known cost excluding unknown `P_AT`.

| Gross EUR | Module net | Dossier net range | Module employer cost | Dossier known cost | Excess before real accident premium |
|---:|---:|---:|---:|---:|---:|
| 20,000 | 15,389.28 | 15,741.72–15,844.63 | 25,150 | 24,750 | +400 |
| 60,000 | 38,025.32 | 38,275.08–39,031.33 | 75,450 | 74,250 | +1,200 |
| 100,000 | 57,442.27 | 57,692.17–59,257.56 | 125,750 | 123,750 | +2,000 |
| 200,000 | 101,497.27 | 101,747.17–105,559.81 | 251,500 | 247,500 | +4,000 |
| 600,000 | 270,617.27 | 270,867.17–284,023.81 | 754,500 | 742,500 | +12,000 |

With no invoice credit and no municipal benefit, the module is within EUR 0.32 of the dossier at EUR 60k+; at EUR 20k it is EUR 102.44 low because of the stale deduction.

## Recommended disposition

Fix the deduction and remove separate FGS. Parameterize municipality, invoice credit, and actual accident premium; otherwise relabel outputs as the current zero-credit/zero-give-back/1%-premium scenario.

## Regression vectors

Use the five dossier rows under (a) EUR 250 credit/no municipal benefit and (b) zero credit/no municipal benefit. Add `G=4,587.09/11%` deduction crossover and solidarity taxable-income edges EUR 80k/250k.
