# Word and OpenDocument Import Comparison — Instructor Key

## Intended outcomes
Learners should recognize that import fidelity depends on source semantics, file features, converter behavior, and BrailleBlaster version. They should distinguish semantic structure from visual formatting.

## Expected source observations

### Structured Word source
- Uses paragraph styles for title, chapter heading, and section headings.
- Presents the equation separately from its definition.
- Contains a three-column device table with a first-row heading.
- Includes a figure description and separate caption.
- Presents pathway prompts and review questions as separate numbered items.

### Structured OpenDocument source
- Uses outline-level headings and a native table.
- Preserves the equation and definition as separate paragraphs.
- Uses list structures for task and review sequences.
- Places an explicit figure description adjacent to figure/caption content.
- Is intentionally compact, not a comprehensive ODF interoperability specimen.

### Flawed Word source
- Headings are bold paragraphs rather than semantic heading styles.
- Equation is flattened into ordinary text and uses x rather than the multiplication symbol.
- Device data is pipe-delimited prose, not a table.
- Figure is represented by a text arrow sequence; no image or alternative text is present.
- Task prompts are run together rather than represented as numbered list items.
- Section boundaries rely on capitalization/bold rather than styles.

Accept additional findings when students demonstrate them from the actual file and import result.

## Repair expectations
Restore heading styles, separate equation and explanatory prose, rebuild the data table, distinguish figure description from caption, and make each task a separate numbered item. Do not invent missing content or silently change master wording.

If the application supports a header-row designation or image alternative text, learners should use and verify it. If a semantic property is unsupported, an explicit adjacent description is preferable to claiming metadata exists.

## Data calculations

| Device | Calculation | Daily estimate |
|---|---:|---:|
| LED lamp | 8 × 5 | 40 Wh |
| Laptop | 45 × 4 | 180 Wh |
| Projector | 220 × 2 | 440 Wh |

Energy is the product of power and time. A lower-power device can use more energy if it operates longer.

## Suggested 20-point rubric
- Source inspection and accurate feature comparison: 5
- Repair of headings, equation, table, figure information, and lists: 6
- Import verification and issue log: 4
- Correct calculations and units: 2
- Evidence-based workflow recommendation and final QA: 3

## Critical-defect gate
Require correction before acceptance if a learner loses a device row, changes a numeric value/unit, drops a question, or treats an unverified visual feature as semantic structure. Successful import alone is not proof of production readiness.

## Instructor facilitation
Compare each element across original source, imported BrailleBlaster document, and translated output. Identify whether a defect originated in source authoring, conversion, import mapping, or subsequent editing. Do not prescribe a universal winner between Word and OpenDocument; base recommendations on tested versions and observed results.
