# Instructor Guide — Applied Import and Conversion Assessment

## Before administering

1. Confirm that the six source files referenced in the assessment packet are present in the course source-file directory.
2. Test the intended import paths with the same BrailleBlaster and converter versions available to learners.
3. Record known environment limitations; do not pre-label a behavior as a defect unless it has been reproduced.
4. Provide learners with the assessment packet and scoring rubric. Keep this guide and the instructor answer keys separate where assessment security matters.
5. Require original-source preservation and a named working directory.

## Assessment flow

| Phase | Suggested time | Instructor checkpoint |
|---|---:|---|
| Environment and source inventory | 15 min | Version record and untouched originals |
| Scenarios 1–2: office documents | 45 min | Heading/table/list inspection |
| Scenarios 3–4: HTML and LaTeX | 45 min | Markup and math boundaries |
| Scenario 5: XML/NIMAS-style | 35 min | Vocabulary and package caution |
| Scenario 6: EPUB and CSV | 35 min | Navigation and data reconciliation |
| Final QA and recommendation | 25 min | Evidence-backed release decision |

Timing is a planning estimate. Adjust for learner accommodations, software availability, and course pacing.

## Evaluation protocol

For each scenario, evaluate four distinct layers:

1. **Source correctness:** Is the structure/content present and valid in the supplied specimen?
2. **Conversion behavior:** What changed during conversion, and is there evidence?
3. **BrailleBlaster editing:** Were repairs minimal, traceable, and made in a working copy?
4. **Output verification:** Was the resulting structure and translated output checked against the source and applicable production requirements?

Ask learners to identify the layer where each defect originated. Do not accept an unexplained statement such as “the import broke it.”

## Expected evidence by scenario

### Scenario 1 — Word
The flawed specimen is deliberately presentational: visual-only heading cues, flattened equation/data, missing image/alt text, and prompts run together. A sound repair restores semantic styles, a three-column data table, distinct equation and explanation, and separate task items. Verify values: LED lamp 8 W/5 h; laptop 45 W/4 h; projector 220 W/2 h.

### Scenario 2 — OpenDocument
The ODT specimen includes outline-level headings, a native table, and list structures. Learners should report observed import behavior, not claim parity with Word by assumption. Verify device order and table cell boundaries.

### Scenario 3 — HTML
The semantic specimen uses meaningful headings, list/table structures, MathML, language/encoding declarations, and figure context. The flawed specimen removes or degrades several of these. Learners should identify the markup defect separately from any importer-specific behavior.

### Scenario 4 — LaTeX
Look for preservation of section boundaries, math delimiters, list structure, table content, and prose context. Score the learner's comparison against the source, not a guessed universal converter result.

### Scenario 5 — XML/NIMAS-style
The generic XML is a custom teaching vocabulary. The NIMAS-style file is explicitly simplified and is not a certified production package. Strong learners distinguish a well-formed XML document from a valid, complete, appropriately packaged production source.

### Scenario 6 — EPUB
Expected inspection includes package metadata, navigation document, spine/reading order, XHTML chapter, MathML, semantic table, and SVG figure. The CSV reconciliation should preserve:
- LED lamp: 8 W, 5 h, 40 Wh/day.
- Laptop: 45 W, 4 h, 180 Wh/day.
- Projector: 220 W, 2 h, 440 Wh/day.

## Interview prompts for borderline submissions

- Show the exact source and imported location for one reported defect.
- What evidence distinguishes a source defect from a conversion defect?
- Which semantic relationship would be lost if the table were linearized?
- How did you verify that the equation remained separate from explanatory prose?
- What would prevent you from releasing this file to production?
- Which assumptions did you make, and how did you label them?

## Scoring and remediation

Use the companion [100-point scoring rubric](applied-import-assessment-rubric.md). Apply the critical-defect override even if the numeric score is passing. Give the learner a precise defect location, expected evidence, and a retest condition. Re-score only the affected criteria unless the correction changes other parts of the workflow.

## Records to retain

Retain the completed rubric, learner issue log, environment/version record, final QA statement, and evidence of critical-defect closure according to the training program's record-retention policy. Do not retain unnecessary personal information in sample artifacts.

