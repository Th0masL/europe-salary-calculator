# 🇪🇺 Europe Salary Calculator

A simple static web page to compare **take-home pay** and the **real cost of
employment** for a salary across **36 European countries** and **11 US cities**.

👉 **Live:** https://th0masl.github.io/europe-salary-calculator/

It answers questions like:

- **“My employer will spend €100,000 total on me — where do I take home the most?”**
  Pick *Employer budget*, type `100,000`, and the table ranks every country by
  net pay (Bulgaria, Albania and Switzerland come out on top; France, Italy and
  Slovenia at the bottom).
- **“What does a €100,000 gross salary mean net, and what does it cost the employer?”**
  Pick *Gross salary*, type `100,000`, and each row shows the net take-home and
  the total employer cost.
- **“I want €50,000 net — which country is cheapest for my employer?”**
  Pick *Net pay* and sort by employer cost.

## Run locally

It's a dependency-free static site — just open it:

```bash
# simplest: double-click index.html, or
xdg-open index.html
```

Or serve it (also how to deploy to GitHub Pages):

```bash
python3 -m http.server 8000   # then visit http://localhost:8000
```

Views are shareable: the URL captures the mode and amount, e.g.
`index.html?mode=cost&amount=100000`.

“Display results monthly” changes the presentation only; the entered amount and
shareable URL remain annual so switching the display cannot change the calculation.

## How it works

Each location has **total employer cost** and **employee net pay** at a few
gross-salary points. Those become `{gross, cost, net}` data points, which all
increase together. The calculator:

1. **Interpolates** linearly between the points to estimate any salary, and
2. **Inverts** the relationship, so you can fix the employer cost, the gross, or
   the target net and solve for the other two.

Amounts outside the generated range are not extrapolated; the affected row shows
`—`. Formula data covers €20,000–€600,000 gross in €5,000 increments.

### Formula model — computed from published rates

The live calculator uses Formula exclusively. It computes employer cost and net
pay **from published tax rates**, with no EOR vendor in the runtime calculation —
one self-contained Python module per country under `tools/calc/`, sharing
`tools/calc/engine.py`. European modules use 2026 rules; the US city calculator
currently uses 2025 federal and state rules.

Each module was assembled from named official or secondary sources (national tax
authorities and tax-provider summaries), with vendor outputs used as sanity checks
during the original research. The resulting reasoning, comparisons, and caveats
remain in the module notes and Git history, but most original source URLs were not
retained. The per-module docstrings record the rates and which figures were treated
as confirmed versus representative; the audit below is the first systematic check
against retained primary-source links. Coverage: **all 36 European
entries (27 EU + Montenegro + Albania, Moldova, Norway, Serbia, Switzerland, Turkey,
Ukraine, UK) + 11 US cities** = 47 total (the US from `tools/calc_us.py`).

The generated [calculation reference](docs/calculations/README.md) makes those
details easier to audit. It includes an index of tax years and currencies, a page
per European country, a shared US methodology, and a page for each US city. Pages
show assumptions, exact parameters or location configuration, executable logic,
representative outputs, and a verification checklist. The dated
[primary-source audit](docs/calculations/audits/2026-10-04-primary-source-audit.md)
records what has actually been independently checked and the discrepancies still
to investigate. CI checks that the generated reference is regenerated whenever an
implementation changes.

A recurring subtlety the formulas get right (and several vendor calculators get
wrong) is **whether employee social contributions are deductible from the
income-tax base** — it varies by country (e.g. Lithuania / Czechia *no*, Latvia /
Greece / Slovenia *yes*), so neighbours can't be assumed to match.

The comparison table's input and output contract is always EUR. Non-euro formulas
with currency-denominated thresholds or caps (such as Poland, Denmark, Sweden and
Czechia) convert the EUR input to local currency for the calculation, then convert
the result back using FX rates fetched at build time (the FX date is shown in the
app). Currency-invariant percentage-only formulas may calculate directly in EUR;
eurozone countries also compute directly in EUR. Build with
`python3 tools/build_formula.py` → `data/formula.json` + `.js`; drop a new
`tools/calc/<country>.py` and it's picked up automatically.

The **“After living costs”** column subtracts Numbeo's estimated annual cost of
living for a single person (capital city for countries, the city itself for US
entries) — a rough proxy for purchasing power.

### US cities (🇺🇸)

The 11 US cities are state-level: Seattle→WA, San Francisco→CA, New York→NY,
Austin→TX, Atlanta→GA, Miami→FL, Chicago→IL, Los Angeles→CA, Boston→MA,
Washington→DC, Denver→CO. (Miami/Florida, like Texas and Washington, has no state
income tax — a strong high-take-home example.) Their Formula figures are calculated
directly by `tools/calc_us.py`: 2025 federal brackets plus the standard deduction,
FICA (with the Social Security cap), and state income tax, including NYC local tax
for New York. Employer cost includes mandatory payroll taxes only (employer FICA +
FUTA + SUTA; workers' compensation and benefits excluded). The model assumes a
single filer taking the standard deduction.

US employer cost is small — **~8–10% on top of gross** (mostly the 7.65% employer
FICA, tapering above the Social Security cap) — versus 50%+ across much of Europe.
Cost of living stays city-specific.

## Project layout

```
index.html                   # markup
styles.css                   # styling
app.js                       # interpolation + table rendering (vanilla JS)
data/
  us.json    / .js           # US: direct calc from published rates (11 cities, no EOR)
  formula.json   / .js       # per-country calc from published rates (build_formula.py)
  cost_of_living.json / .js  # current per-location living-cost estimates
docs/calculations/            # generated, auditable location calculation reference
tools/
  calc/                      # Formula source: one module per country + engine.py
    engine.py                #   shared maths (progressive brackets, caps)
    <country>.py             #   36 European modules — compute(gross) -> (cost, net)
    country-data-prompt.md   #   reusable research prompt for gathering a country's rates
  build_formula.py           # build data/formula.json/.js from tools/calc/* (+ FX, + US)
  generate_calculation_docs.py # build/check the location calculation reference
  calc_us.py                 # US cost + net from published 2025 federal/state rates
  fetch_numbeo.py            # refresh cost-of-living from current Numbeo
```

The deployed `.js` files wrap the canonical JSON in browser globals so the page
works directly from `file://` without a server.

### Regenerating the data

```bash
# 1. US direct calculation from published rates
python3 tools/calc_us.py          # → data/us.json + .js

# 2. Formula data — per-country modules plus the US data from step 1
python3 tools/build_formula.py    # → data/formula.json + .js  (fetches FX for non-euro)

# 3. Optional: refresh cost-of-living from current Numbeo (slow; rate-limited)
python3 tools/fetch_numbeo.py     # → data/cost_of_living.json + .js

# 4. Validate the generated data
python3 tools/generate_calculation_docs.py
python3 tools/generate_calculation_docs.py --check
python3 tools/validate_data.py
python3 -m unittest discover -s tests -v
```

GitHub Actions runs the Python compilation, structural regression suite, dataset
validation, and JavaScript syntax check on every push and pull request. These
checks catch broken calculations and generated data, but they do not replace an
annual review of each jurisdiction's source rates.

### Data shape

```jsonc
{
  "name": "Austria",
  "flag": "🇦🇹",
  "eu": true,
  "year": 2026,
  "costNote": "Social security 20.38% (capped) + …",
  "points": [
    { "gross": 20000, "cost": 25794, "net": 16283 },
    { "gross": 25000, "cost": 32243, "net": 19619 },
    // …one point every €5,000 gross…
    { "gross": 600000, "cost": 670457, "net": 330160 }
  ]
}
```

US cities carry `"us": true` and use the same €20,000–€600,000 grid, calculated
directly from federal, state, and city rules rather than a flat effective rate:

```jsonc
{
  "name": "Austin, TX",
  "flag": "🇺🇸",
  "us": true,
  "year": 2025,
  "costOfLiving": 35197,
  "points": [
    { "gross": 20000, "cost": 21781, "net": 17859 },
    // …one point every €5,000 gross…
    { "gross": 600000, "cost": 618579, "net": 398899 }
  ]
}
```

## ⚠️ Disclaimer

These figures are **estimates for comparison only**. They simplify personal
circumstances, marital status, children, regional taxes, optional benefits,
bonuses, and currency fluctuations, and the browser interpolates between generated
€5,000 gross-salary points. **Do not use them as precise payroll or budgeting
figures.**

Country modules contain research notes and named sources, but most do not yet
contain a complete set of direct citations. See the primary-source audit above for
the current evidence status. Cost-of-living estimates are from Numbeo.
