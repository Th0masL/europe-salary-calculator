# Country payroll-data research prompt

Reusable prompt for Perplexity (or any web-searching assistant) to gather the
current statutory figures needed to write a `tools/calc/<country>.py` module.
Replace `{{COUNTRY}}` and paste.

---

I'm building a salary / employment-cost calculator and need the **current
statutory payroll figures for {{COUNTRY}}** for a standard full-time
private-sector employee (single, no dependents, no special regime).

Search official sources and give me each figure **with the tax year it applies
to and a link to the authoritative source** (the national tax authority and/or
social-security institution). If a 2026 figure isn't published yet, give the
latest in force and say which year it is. Flag anything scheduled to change.

Please provide:

1. **Currency** used for salaries.

2. **Employer contributions** — everything the employer pays *on top of* gross
   salary. For each: name, rate (%), the base it applies to (usually gross
   salary), and any monthly/annual **ceiling or cap**. Cover social security,
   pension, health, unemployment, work-accident, and any payroll taxes.

3. **Employee contributions** — everything **deducted from** the employee's
   gross. Same format: name, rate, base, cap. Cover pension, social security,
   unemployment, health, etc.

4. **Personal income tax**:
   - Flat or progressive?
   - If progressive, the **full bracket table**: each income threshold and its
     marginal rate.
   - Any surtax, solidarity tax, or **municipal/local income tax** (with rates).
   - The **tax-free allowance / personal exemption** (amount), and any
     **phase-out / taper** rules (the income range over which it reduces to 0).

5. **Order of calculation** — this matters a lot:
   - Are the employee's social contributions **deductible from taxable income
     before** income tax is applied?
   - Any other standard deductions applied before tax?

6. **Mandatory extra pay** — any legally required 13th/14th-month salary or
   mandatory bonuses (these raise the real employer cost).

7. **Official worked examples (for validation)** — using the **official tax
   authority's own calculator or a published worked example** (not a payroll
   vendor / EOR site), give the full breakdown for **one or two specific annual
   gross salaries (e.g. €60,000 and €100,000)**: each employer contribution, each
   employee deduction, the income tax, the resulting **net pay**, and the **total
   employer cost**. Cite the official calculator/source URL. This is what I'll
   check the code against, so accuracy here matters most.

Format the answer as a clear, structured list or table I can transcribe into
code — exact numbers, not ranges, with the source and year next to each.
