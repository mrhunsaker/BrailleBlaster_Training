# Applied Import and Conversion Assessment Pack

## Assessment purpose

This assessment evaluates whether a learner can inspect source structure, select and execute an import workflow, diagnose conversion defects, preserve content, and verify the resulting braille-production project. It is a practical assessment, not a test of memorized menu paths.

**Recommended time:** 3–4 hours  
**Level:** Intermediate to advanced  
**Total:** 100 points  
**Required evidence:** saved working project(s), source-to-output comparison, issue log, and final QA statement.

Use the supplied fictional practice files. Preserve every original and work from copies. Record the BrailleBlaster version and any external converter/application versions used.

## Candidate instructions

For each scenario:

1. Inventory the source and identify its structural features.
2. State the intended import route and why it is appropriate.
3. Import or convert using the available course workflow.
4. Compare the result with the source; do not rely on appearance alone.
5. Correct defects in a working copy and document consequential decisions.
6. Verify the corrected project and submit the requested evidence.

If a named feature is unsupported in the installed environment, record the limitation and propose a safe alternative. Do not claim a test passed when it could not be performed.

---

## Scenario 1 — Word source with visual-only structure

**Source:** `energy-field-guide-flawed.docx`  
**Task:** Repair the document before import. Restore heading hierarchy, equation boundaries, tabular data, figure information, and numbered tasks. Import the repaired copy and compare it with the canonical Markdown source.

**Required evidence**
- Source defect inventory with at least five findings.
- Repaired Word working copy.
- Import comparison identifying at least three observed changes or preserved features.
- QA confirmation of all three device records and units.

**Critical risks:** lost data row, incorrect equation, missing task, false assumption that bold text is a semantic heading.

## Scenario 2 — OpenDocument import and structural fidelity

**Source:** `energy-field-guide.odt`  
**Task:** Import the ODT source. Inspect outline levels, paragraph order, table geometry, equation text, and numbered lists. Compare the result with the Word source import; report differences only when observed.

**Required evidence**
- Import log with application and version details.
- Feature-by-feature comparison.
- Corrected project or documented reason no correction was required.
- Verification of the table's three records and column order.

**Critical risks:** assuming ODT and DOCX import are identical; silently rebuilding a table with reordered values.

## Scenario 3 — HTML conversion: semantic versus presentational markup

**Source:** `energy-field-guide.html` and `energy-field-guide-flawed.html`  
**Task:** Compare the semantic and flawed HTML. Identify encoding/language, heading, list, table, equation, and image-description differences. Import or convert both using the course workflow and document what survives.

**Required evidence**
- HTML defect inventory.
- Repaired flawed HTML or a documented remediation map.
- Before/after structure comparison.
- Evidence that equation and table values remain correct.

**Critical risks:** treating visual heading appearance as hierarchy; losing table header relationships; dropping figure context.

## Scenario 4 — LaTeX mathematical content

**Source:** `energy-field-guide.tex`  
**Task:** Inspect the source structure and math delimiters. Convert/import using the available workflow. Verify the equation and surrounding prose, section hierarchy, list items, and table content. Identify any conversion artifact rather than manually correcting it without a record.

**Required evidence**
- Source structure map.
- Conversion/import log.
- Equation verification against the source.
- At least two documented conversion observations.

**Critical risks:** equation merged with prose; symbols or units changed; list boundaries lost.

## Scenario 5 — XML/NIMAS-style structured source

**Source:** `energy-field-guide.xml` and `energy-field-guide-nimas.xml`  
**Task:** Compare the custom teaching XML with the simplified DTBook/NIMAS-style specimen. Identify the vocabulary and structural differences. Evaluate the source before attempting import; do not assume the simplified specimen is a certified NIMAS package.

**Required evidence**
- Element/structure mapping table.
- Import feasibility decision and rationale.
- At least three source or package limitations.
- Corrected or normalized working copy if the workflow requires one.

**Critical risks:** representing the teaching specimen as production-conformant; flattening semantic relationships; importing without checking package expectations.

## Scenario 6 — EPUB package and cross-format reconciliation

**Source:** `energy-field-guide.epub`  
**Task:** Inspect package navigation, metadata, reading order, chapter content, MathML, table, and SVG figure. Import or convert using the available workflow. Compare the resulting content with the Markdown master and CSV data.

**Required evidence**
- Package inventory.
- Navigation/reading-order check.
- Math/table/figure verification.
- Reconciliation of device values with the CSV source.

**Critical risks:** missing chapter from reading order; math or SVG lost; CSV values changed or interpreted as different units.

---

## Final production decision

Write a concise recommendation addressing:

- Which source format and import route produced the most reliable starting structure in your tested environment?
- Which format required the most remediation?
- Which defects were present in the source versus introduced during conversion/import?
- What additional review is required before production release?

Your recommendation must cite evidence from your logs. Do not generalize beyond the versions and specimens tested.

## Submission manifest

- [ ] Environment/version record.
- [ ] Six scenario logs, including scenarios marked not tested and why.
- [ ] Source-to-output comparison evidence.
- [ ] Repaired working copies where required.
- [ ] Defect/decision log with severity and verification.
- [ ] Final recommendation and QA statement.
- [ ] Original source files preserved unchanged.

