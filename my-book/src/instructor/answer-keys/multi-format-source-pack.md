# Instructor Key: Multi-Format Source-Pack Lab

## Scope

This key supports the synthetic Energy in Our Community source pack. It is not a substitute for a current NIMAS/DTBook or EPUB validation tool, braille code authority, or production specification.

## Canonical content checks

The Markdown master establishes the key content inventory:

- Chapter 3 title and introductory paragraph.
- Two energy-generation paragraphs.
- Investigation paragraph and equation E = P × t.
- Variable definitions: E is energy in watt-hours, P is power in watts, and t is time in hours.
- Table 3.1 with three devices and two numeric fields per device.
- Figure 3.1 energy pathway.
- Three ordered investigation steps.
- Three review questions in the canonical Markdown master.

The HTML, XML, LaTeX, and EPUB are format specimens. The compact EPUB intentionally contains the core instructional content but does not reproduce every review question in the Markdown master. Learners should record this as a content-scope difference rather than assuming all files are byte-identical.

## Flawed HTML: expected findings

1. No html language attribute.
2. No character encoding declaration.
3. Chapter title is a styled div and bold text, not a semantic heading.
4. Section titles are bold paragraphs, not headings.
5. Equation is plain text and uses an asterisk rather than a structured multiplication operator.
6. Table has no caption, thead, or scoped header cells.
7. Figure references missing-figure.png.
8. Figure has no alt text or associated caption element.
9. Ordered steps are flattened into a paragraph, obscuring sequence.
10. Heading/section relationships cannot be reliably inferred from visual styling.

A strong repair uses a valid document language and encoding, h1/h2 hierarchy, MathML or another supported structured equation representation, caption and scoped table headers, meaningful figure alternative text/caption, and ol/li for ordered steps. Do not add content not supported by the source; query the content owner if the missing diagram itself is required.

## Generic XML: expected findings

- It uses a custom namespace and teaching vocabulary, not a published standard.
- No DTD or schema is supplied; well-formedness alone does not establish semantic validity.
- The equation is represented as an empty element with a notation attribute; learners should decide whether the chosen import path can preserve it.
- Table header/data roles are represented with custom element names and need a documented mapping.
- Figure is referenced by filename and caption, but the file itself is not in this generic XML specimen's directory.

Expected student action: propose a mapping table, identify unsupported elements, and avoid labeling the file as NIMAS or standards-conformant.

## NIMAS/DTBook teaching specimen: expected findings

The specimen is intentionally simplified. Reviewers should notice at least:

- Metadata is minimal and does not represent a complete production metadata package.
- Table markup uses a generic th row but does not demonstrate a fully robust, scoped header structure.
- Figure information is supplied as a text paragraph; the source does not contain a linked tactile graphic or complete alternative representation.
- Ordered list structure is present but should be checked against the applicable DTBook vocabulary and importer.
- The DTD declaration and namespace should be validated using the correct current DTD/catalog and production environment.
- This file should not be treated as a certified NIMAS source or validated delivery package.

Do not require students to invent missing metadata or declare compliance. The correct outcome is to document what is missing and what authority or source owner must resolve it.

## LaTeX: expected findings

- Chapter and section commands provide a useful hierarchy.
- The displayed equation is structurally represented in math mode.
- Table and figure environments carry captions, but their placement and conversion may differ after import.
- The figure references energy-flow.pdf, while the EPUB has an SVG illustration; the referenced PDF is not supplied in the LaTeX folder.
- Students should verify table column order and all row values after conversion.

## EPUB: expected findings

The package includes a mimetype entry, container.xml, OPF metadata, navigation document, XHTML content, CSS, MathML equation, semantic table, and SVG image. Students should inspect:

- Whether all manifest hrefs resolve.
- Whether the spine order is appropriate.
- Whether navigation links reach the chapter.
- Whether XHTML and MathML survive the target import workflow.
- Whether image alternative text and figure caption communicate the same information.
- Whether the compact EPUB's content scope differs from the Markdown master.

The package is a teaching sample, not an accessibility certification. Learners should use an EPUBCheck version appropriate to the target EPUB specification and separately assess accessibility.

## CSV and calculations

| Device | Calculation | Daily energy |
|---|---:|---:|
| LED lamp | 8 W × 5 h | 40 Wh |
| Laptop | 45 W × 4 h | 180 Wh |
| Projector | 220 W × 2 h | 440 Wh |

The formula uses power multiplied by time. A high-power device can use less total energy than a lower-power device if it operates for sufficiently fewer hours. In this data set, the projector has both the highest power and the highest calculated daily energy.

## Suggested scoring (20 points)

| Criterion | Points |
|---|---:|
| Accurate source inventory and content comparison | 4 |
| Identifies semantic defects in flawed HTML | 4 |
| XML/NIMAS limitations correctly qualified | 4 |
| Import comparison covers math, table, figure, and navigation | 4 |
| Repaired copy and QA evidence are complete | 4 |

**Critical gate:** Do not award a passing result if the learner claims the simplified NIMAS specimen is production-certified, omits source content without disclosure, or treats visual formatting as proof of semantic structure.
