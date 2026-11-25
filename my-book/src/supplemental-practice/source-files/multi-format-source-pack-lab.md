# Multi-Format Source-Pack Lab: Energy in Our Community

## Purpose

Compare how one short fictional science chapter is represented in different source formats. Identify what each format preserves, what it makes explicit, and what may be lost during import. This is an import and structure exercise, not a braille transcription standard.

## Package manifest

| File | Format / role | Intended use |
|---|---|---|
| energy-field-guide.md | Canonical Markdown wording | Content comparison baseline |
| energy-field-guide.html | Semantic HTML | Inspect heading, table, figure, and list structure |
| energy-field-guide-flawed.html | Deliberately weak HTML | Diagnose visual-only headings, missing table semantics, missing image alternative, and flattened lists |
| energy-field-guide.xml | Custom structured XML | Map elements to semantic structures; identify missing schema governance |
| energy-field-guide-nimas.xml | Simplified DTBook/NIMAS-style XML | Inspect hierarchy, metadata, table markup, and figure representation |
| energy-field-guide.tex | LaTeX | Inspect chapter/section, equation, table, figure, and list conversion |
| energy-field-guide-data.csv | Tabular data | Import or reconstruct a data table |
| energy-field-guide.epub | EPUB 3 package | Inspect metadata, navigation, XHTML, MathML, table, and SVG asset |
| structured-field-guide.docx | Separate Word structure specimen | Practice Word style and table import; it is not a byte-for-byte copy of this chapter |

## Lab A — Establish a baseline

1. Open the canonical Markdown chapter.
2. Identify all headings, paragraphs, equation content, table data, figure information, ordered steps, and review questions.
3. Record the content inventory before importing any other file.
4. Keep an untouched copy of every source file.

**Deliverable:** a source-content inventory and a list of expected structures.

## Lab B — Compare the clean imports

Import or inspect the semantic HTML, XML, LaTeX, and EPUB sources using the workflows available in the course. For each, record:

- Whether heading levels and reading order survive.
- Whether the equation remains distinguishable from surrounding prose.
- Whether table headers retain their relationship to data cells.
- Whether the figure and its explanatory text remain associated.
- Whether ordered steps remain a real list.
- Whether metadata and navigation are retained or need reconstruction.
- Any unsupported content, conversion warnings, or manual remediation.

Do not infer that a visually correct page has a correct semantic structure.

## Lab C — Repair the flawed HTML

The flawed HTML is intentionally defective. Find and document at least these categories:

- The chapter and section headings are styled with generic div and paragraph elements rather than heading elements.
- The table has no caption or explicit header structure.
- The figure references a missing image and has no alternative text or caption association.
- The ordered steps are flattened into one paragraph.
- The equation is plain text rather than structured mathematical content.
- The document language and character encoding are not declared.

Repair a copy. Preserve the wording and data. Use semantic elements where appropriate, and document each change.

## Lab D — Audit the NIMAS/DTBook specimen

Treat the NIMAS file as a teaching specimen only. Identify at least four issues or verification needs, including:

- Whether the supplied metadata is sufficient for the intended production context.
- Whether the table markup expresses header/data relationships clearly.
- Whether the figure has an accessible representation and associated description.
- Whether list and heading structure is complete and consistent.
- Whether the file validates against the actual applicable DTBook/NIMAS DTD and production requirements.

Do not certify conformance based on this exercise. A production NIMAS file requires the authoritative specification and validation process.

## Lab E — Reconcile data and math

Use the CSV file to reconstruct Table 3.1. Calculate energy use using E = P × t:

| Device | Calculation | Daily energy |
|---|---:|---:|
| LED lamp | 8 × 5 | 40 Wh |
| Laptop | 45 × 4 | 180 Wh |
| Projector | 220 × 2 | 440 Wh |

Explain why the device with the greatest power also has the greatest daily energy use in this particular data set, and why that relationship is not guaranteed in general.

## Lab F — Final verification

Compare your repaired/imported result with the canonical Markdown source. Verify:

- [ ] No source paragraphs are missing or duplicated.
- [ ] Heading hierarchy is meaningful.
- [ ] Equation symbols and variable definitions are preserved.
- [ ] All table values and units match the source.
- [ ] Figure content is represented and its instructional purpose is clear.
- [ ] Ordered steps remain ordered.
- [ ] Review questions are complete and in sequence.
- [ ] Import decisions and unresolved limitations are documented.

## Submission

Submit the untouched source inventory, at least two import comparison records, the repaired HTML, the NIMAS audit, the reconstructed table, and a final QA note. Include screenshots only as supplementary evidence; they do not replace the editable project or structural inspection.

## Instructor note

Expected findings are documented at a category level, not as a single required braille rendering. Evaluate whether learners identify semantic and access risks, preserve source meaning, and verify the resulting project. For NIMAS and EPUB production, require current authoritative validation rather than accepting this synthetic teaching set as a standards test.
