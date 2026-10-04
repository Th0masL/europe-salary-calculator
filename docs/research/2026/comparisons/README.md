# Formula-to-research comparisons

These files compare the existing calculator modules with the independent 2026
research dossiers. They are review artifacts, not implementation changes.

See the [consolidated comparison summary](SUMMARY.md) for verified totals, the
country matrix, implementation priorities, and the proposed regression strategy.

Every difference is classified as:

- **Confirmed mismatch** — primary evidence directly contradicts the current code.
- **Unsupported assumption** — the code uses a value or simplification without
  sufficient primary evidence.
- **Scenario difference** — both calculations can be valid, but they model a
  different location, employee, employer, payment schedule, or optional regime.
- **Product decision** — no universal value exists; the product must expose or
  clearly label an assumption.
- **Match** — the implemented rule agrees with the researched rule for the same
  scenario.

Severity is assessed against the website's €20,000–€600,000 gross range:

- **Critical:** materially reverses comparisons or invalidates high-salary output.
- **High:** material recurring difference in employee net or employer cost.
- **Medium:** meaningful but bounded difference, or affects a limited range.
- **Low:** labelling, minor threshold, rounding, or small fixed-amount difference.

The product's comparison table is intentionally denominated in EUR. A non-euro
module may calculate directly in EUR when every applicable rule is homogeneous
and currency-invariant. It only needs a local-currency round trip when a statutory
amount, threshold, cap, rounding rule, or other nominal value affects the result.

No formula should be changed from these notes until its scenario choice and test
vectors have been reviewed.
