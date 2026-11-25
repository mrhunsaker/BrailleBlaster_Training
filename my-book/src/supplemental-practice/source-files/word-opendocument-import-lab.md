# Word and OpenDocument Import Comparison Lab

## Purpose
Compare two structured office-document sources and one intentionally degraded Word source. All contain the same fictional Grade 7 science chapter with headings, an equation, a data table, figure information, and numbered tasks.

## Source files
- [Structured Word source](energy-field-guide.docx)
- [Structured OpenDocument source](energy-field-guide.odt)
- [Intentionally flawed Word source](energy-field-guide-flawed.docx)
- [Canonical wording reference](energy-field-guide.md)

Work from copies. Preserve each original unchanged.

## Part A — Establish a baseline
For each file, record the application/version, import route, warnings, whether it opens without repair, and differences from the Markdown master. Do not assume a file extension guarantees particular feature support or import fidelity.

## Part B — Inspect semantic structure
Compare title/chapter heading, section hierarchy, equation and definition, table rows/columns/header, figure description/caption, numbered task sequence, and paragraph order. Distinguish source semantics from visual appearance: bold text is not necessarily a heading, and aligned values are not necessarily a table.

## Part C — Repair the flawed source
On a working copy:
1. Apply title, Heading 1, and Heading 2 styles.
2. Restore the equation as a distinct expression and retain its explanatory sentence.
3. Rebuild the device data as a three-column table; identify the header row where supported.
4. Separate figure description from caption. Enter and verify alternative text if the application supports it; otherwise retain an explicit adjacent description.
5. Restore the pathway prompts and review questions as distinct numbered items.
6. Check punctuation, symbols, units, and wording against the Markdown master.

Record each repair, rationale, and verification.

## Part D — Import and compare in BrailleBlaster
Import each clean office-document source separately, then import the repaired flawed copy. Inspect heading levels, table dimensions and cell order, equation boundaries, figure description/caption, list numbering, and all device values/units. Review translated output against the applicable code, settings, and production requirements. Do not assume Word and OpenDocument use identical converters.

## Part E — Data check
Calculate daily energy using E = P × t:
- LED lamp: 8 W × 5 h = 40 Wh
- Laptop: 45 W × 4 h = 180 Wh
- Projector: 220 W × 2 h = 440 Wh

Explain why power alone is insufficient to compare energy use.

## Submission
1. Completed feature comparison.
2. Repaired working copy of the flawed Word file.
3. Import issue log with at least five observations.
4. Evidence-based recommendation identifying the source/import path requiring least remediation.
5. Final QA note confirming originals were preserved and imported content checked against the master.

## Evaluation criteria
Structural inspection; accurate repairs; correct calculations and units; evidence-based import comparison; reproducible issue and QA notes.

**Standards note:** These are synthetic teaching files, not exhaustive OOXML/ODF implementations or accessibility-conformance test documents. Validate actual production sources against relevant application behavior and specifications.
