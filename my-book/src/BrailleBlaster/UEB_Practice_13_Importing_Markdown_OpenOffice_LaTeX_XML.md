# UEB Practice: Importing from Markdown, OpenOffice, LaTeX, XML, and EPUB

## How to use this document

The first half explains how these source formats differ when they enter BrailleBlaster. The second half is a practice document. Identify which source format is being represented, what BrailleBlaster can preserve, and what must be verified after import.

The formats covered separately are:

1. **Markdown (`.md`)**
2. **OpenOffice / OpenDocument Text (`.odt`)**
3. **LaTeX (`.tex`)**
4. **General XML (`.xml`)**
5. **NIMAS XML**
6. **EPUB (`.epub`)**

This document intentionally treats **general XML separately from NIMAS XML**. An XML file is not automatically a NIMAS file.

---

# The Concept

## Different source formats carry different kinds of structure

BrailleBlaster can open several formats, including Markdown, OpenDocument Text (`.odt`), LaTeX, XML/NIMAS, DOCX, HTML, EPUB, and text files.

These formats are not interchangeable.

* **Markdown** expresses structure through lightweight markup such as `#`, `-`, `*`, and other Markdown conventions.
* **OpenDocument Text** can contain rich word-processing structure similar to Microsoft's DOCX format.
* **LaTeX** represents document structure and mathematical notation through commands.
* **General XML** can carry explicit semantic and publishing structure, but the meaning of its tags depends on the XML vocabulary being used.
* **NIMAS XML** is a specific XML-based format intended for accessible instructional materials and has a more standardized structure that BrailleBlaster can use for specialized processing.
* **EPUB** is a packaged electronic publication that can contain multiple structured content files, navigation information, images, styles, and other resources.

### The most important rule

> **The file extension tells you how the source is encoded; the source structure tells you what BrailleBlaster can preserve.**

Opening a source file is only the beginning of the transcription process. After importing, the transcriber must inspect the structure and verify that the resulting braille is correct.

---

# Part 1 — Importing Markdown

## What Markdown is

Markdown is a lightweight markup language. A Markdown source may use symbols such as:

```markdown
# Heading 1

## Heading 2

**bold**

*emphasis*

- list item
```

BrailleBlaster can open Markdown (`.md`) files.

Markdown is useful because its markup communicates basic document structure. However, the Markdown syntax itself should not simply be treated as finished braille formatting.

## Opening a Markdown file

1. Open BrailleBlaster.
2. Select **File > Open**.
3. Select the `.md` file.
4. Allow BrailleBlaster to import the document.
5. Review the resulting Print View.
6. Check the corresponding Braille View.
7. Correct imported styles where necessary.

## What to check

After opening Markdown, inspect:

* heading levels;
* lists;
* emphasis;
* links;
* tables;
* block quotations;
* code or preformatted material;
* images;
* image descriptions;
* mathematics;
* special symbols;
* page information where applicable.

### Important point about lists

A Markdown list such as:

```markdown
- warm
- cool
- cold
```

communicates that the material is a list.

It does **not** mean that the final braille margins should be accepted without review.

---

## Worked Demonstration — Markdown

Source:

```markdown
# Weather

## Temperature

Temperature tells us how hot or cold something is.

- warm
- cool
- cold
```

### Expected workflow

1. Open the `.md` file.
2. Inspect the imported heading structure.
3. Verify that `# Weather` is the intended heading level.
4. Verify that `## Temperature` is the intended subordinate heading.
5. Verify that the three items are actually structured as a list.
6. Check the list margins and continuation lines in Braille View.
7. Apply or correct BrailleBlaster styles as necessary.

---

# Part 2 — Importing OpenOffice / OpenDocument Text

## What format is meant here?

For this lesson, **OpenOffice** means an OpenDocument Text file, normally using the `.odt` extension.

An ODT file can contain considerably more formatting information than a plain-text document.

It may contain:

* paragraph styles;
* headings;
* numbered lists;
* bulleted lists;
* tables;
* emphasis;
* page breaks;
* images;
* captions;
* hyperlinks;
* footnotes;
* mathematical material.

## Opening an ODT file

1. Select **File > Open**.
2. Select the `.odt` file.
3. Review the imported structure.
4. Compare important formatting with the original document.
5. Correct styles that did not import as intended.
6. Check Braille View.

## What to check

Do not assume that because the ODT looks correct in the original application, every structure will automatically be correct in BrailleBlaster.

Check:

* heading hierarchy;
* list structure;
* table structure;
* emphasis;
* captions;
* page breaks;
* images;
* footnotes/endnotes;
* mathematical content;
* Braille View margins and indentation.

---

## Worked Demonstration — OpenDocument

```text
File: weather.odt

Contains:
- Heading 1
- Heading 2
- bulleted list
- one table
```

### Expected workflow

Open the `.odt` file and inspect each imported structure.

Verify:

* the Heading 1 became the appropriate BrailleBlaster heading;
* the Heading 2 became the appropriate subordinate heading;
* the bulleted list is structurally a list;
* the table remains a table or has been converted into the appropriate structure;
* the table's braille presentation is correct.

---

## Practice

An ODT document contains:

```text
Unit 3

Weather

1. Clouds
2. Rain
3. Snow

Table 1: Types of precipitation
```

Identify at least five things that should be checked after import.

### Answer Key

At minimum:

1. Unit heading structure.
2. Heading hierarchy.
3. Numbered-list structure.
4. Table structure.
5. Caption treatment.
6. Page breaks/page information where applicable.
7. Braille View and resulting margins.

---

# Part 3 — Importing LaTeX

## What LaTeX is

LaTeX is a markup system commonly used for technical and mathematical documents.

For example:

```latex
\section{Energy}

The formula is $E=mc^2$.
```

LaTeX communicates both document structure and mathematical notation through commands.

## LaTeX has a special math consequence

When LaTeX is opened in BrailleBlaster, LaTeX mathematics is converted into **ASCII Math** in the relevant workflow.

The current BrailleBlaster documentation notes an important exception involving NIMAS XML, TXT, BRL, and ZIP file types.

Therefore:

> **Do not assume that seeing LaTeX source commands in the original file means those commands will remain visible after import.**

The mathematics enters BrailleBlaster's math workflow and must be checked there.

## What to check

After opening a LaTeX document:

* section and heading structure;
* equations;
* fractions;
* superscripts and subscripts;
* mathematical symbols;
* displayed mathematics;
* math translation;
* Print View;
* Braille View.

---

## Worked Demonstration — LaTeX

Source:

```latex
\section{Motion}

\[
v = \frac{d}{t}
\]
```

### Expected workflow

1. Open the `.tex` file.
2. Verify that `Motion` became the intended heading.
3. Inspect the imported equation.
4. Verify the fraction structure.
5. Check the mathematical representation.
6. Check the resulting braille.

Do not assume that a visually correct Print View guarantees a correct mathematical braille representation.

---

## Practice

Import:

```latex
\section{Fractions}

\[
\frac{3}{4} + \frac{1}{2} = \frac{5}{4}
\]
```

### Answer Key

Check:

1. The heading.
2. The three fractions.
3. The mathematical operators.
4. The imported math structure.
5. The resulting braille.

---

# Part 4 — Importing General XML

## XML is not automatically NIMAS

XML stands for **eXtensible Markup Language**.

XML is a framework for representing structured information. An XML file may use a publisher's own vocabulary and tags.

For example:

```xml
<section>
  <h1>Energy</h1>
  <p>Energy can change from one form to another.</p>
</section>
```

The fact that the file ends in `.xml` does **not** tell the transcriber that it is NIMAS.

An XML file might instead be:

* publisher-created XML;
* a custom educational XML vocabulary;
* an XML export from another application;
* NIMAS XML;
* another specialized XML format.

## Why general XML needs separate treatment

A custom XML file may contain tags such as:

```xml
<chapter>
  <title>Plants</title>
  <paragraph>Plants need light.</paragraph>
</chapter>
```

The transcriber must determine what those tags mean.

For example:

* Does `<title>` represent a heading?
* Does `<paragraph>` represent ordinary body text?
* Does `<item>` represent a list item?
* Is a `<table>` actually structured as a table?
* Are page numbers represented?
* Is mathematical information present?
* Are images and captions represented?

The XML tags themselves do not automatically determine the final braille formatting.

---

## Worked Demonstration — General XML

Source:

```xml
<chapter>
  <title>Birds</title>
  <paragraph>Birds have feathers.</paragraph>
  <paragraph>Many birds can fly.</paragraph>
</chapter>
```

The intended structure might be:

```text
Birds

Birds have feathers.

Many birds can fly.
```

### Expected workflow

1. Determine what XML vocabulary is being used.
2. Identify the semantic meaning of the tags.
3. Open the XML in BrailleBlaster.
4. Inspect how the tags were mapped.
5. Verify the heading structure.
6. Verify the paragraph structure.
7. Check Braille View.
8. Manually correct anything that did not map as intended.

---

## Practice

Given:

```xml
<section>
  <heading>Weather</heading>
  <item>Rain</item>
  <item>Snow</item>
</section>
```

Determine:

1. Which element is probably a heading?
2. Which elements are probably list items?
3. What must be verified after import?

### Answer Key

1. `<heading>` is probably a heading.
2. `<item>` elements are probably list items.
3. Verify that BrailleBlaster actually imported them as the intended styles and list structure. Check indentation, continuation lines, and Braille View.

---

# Part 5 — Importing NIMAS XML

## NIMAS is a specific XML workflow

NIMAS is an XML-based standard used for accessible instructional materials.

It is important to distinguish:

> **General XML is not automatically NIMAS.**

NIMAS has a particular structure and intended use, and BrailleBlaster provides specialized tools for NIMAS files.

## NIMAS-specific features

Depending on the source and workflow, NIMAS can provide structured information for:

* headings;
* lists;
* tables;
* page information;
* images;
* mathematical material;
* production notes;
* document navigation.

BrailleBlaster has operations specifically associated with NIMAS files.

These include:

* Book Tree navigation;
* Production Note Manager;
* NIMAS-specific formatting;
* handling of structured source information;
* MathML-related processing.

## Production Notes

NIMAS files may contain publisher production notes.

The transcriber should review these notes and determine how they should be handled rather than automatically assuming that every production note belongs in the final braille.

BrailleBlaster's Production Note Manager provides options for handling production notes.

## NIMAS practice

After opening a NIMAS file:

1. Inspect the Book Tree.
2. Review production notes.
3. Check automatically imported headings.
4. Check page numbers.
5. Check lists.
6. Check tables.
7. Check mathematical material.
8. Review images and descriptions.
9. Proofread the resulting braille.

### Key distinction

**General XML**

> Determine what the XML structure means.

**NIMAS XML**

> Use the standardized structure and NIMAS-specific BrailleBlaster tools, then verify the automated formatting.

---

# Part 6 — Importing EPUB Specifically

## EPUB is its own import workflow

BrailleBlaster supports **EPUB e-books (`.epub`)** as an input format.

EPUB should be treated separately from both general XML and NIMAS.

An EPUB is a packaged electronic publication. It can contain multiple structured content files along with navigation, styles, images, metadata, and other resources.

## Opening an EPUB

1. Select **File > Open**.
2. Select the `.epub` file.
3. Allow BrailleBlaster to import the publication.
4. Inspect the imported structure.
5. Check chapter boundaries.
6. Check headings.
7. Check lists and tables.
8. Check images and captions.
9. Check links and footnotes.
10. Check mathematics if present.
11. Proofread the resulting braille.

## Why EPUB needs careful review

An EPUB may contain:

* multiple XHTML/HTML content documents;
* navigation information;
* stylesheets;
* images;
* metadata;
* embedded resources;
* mathematical content;
* footnotes;
* hyperlinks.

The EPUB importer therefore has to reconstruct a usable document from a packaged electronic publication.

---

## Worked Demonstration — EPUB

Imagine an EPUB containing:

```text
Chapter 1
Chapter 2
Chapter 3

Each chapter contains:
- headings
- paragraphs
- lists
- one image
- a caption
```

### Check 1 — Navigation

Do the chapters appear in the correct order?

### Check 2 — Headings

Do the chapter titles have appropriate heading levels?

### Check 3 — Lists

Are list items actually structured as lists?

### Check 4 — Figures

Is the image present or represented appropriately?

Is the caption separated from any transcriber-generated description?

### Check 5 — Page Structure

Does the imported document need print-page information or other production formatting added?

---

# Worked Demonstration — Comparing All Five Source Types

## Markdown

```markdown
# Weather

## Temperature

Temperature tells us how hot or cold something is.

- warm
- cool
- cold
```

**Expected workflow:** Open the `.md`, inspect the imported heading and list structure, then apply or correct BrailleBlaster styles.

---

## OpenDocument

```text
File: weather.odt

Contains:
- Heading 1
- Heading 2
- bulleted list
- one table
```

**Expected workflow:** Open the `.odt`, verify each imported structure, and correct the braille formatting where needed.

---

## LaTeX

```latex
\section{Energy}

The formula is $E=mc^2$.
```

**Expected workflow:** Open the `.tex`, verify the section structure, and inspect the imported mathematics.

---

## General XML

```xml
<section>
  <h1>Energy</h1>
  <p>Energy can change from one form to another.</p>
</section>
```

**Expected workflow:** Determine what XML vocabulary is being used and how the tags are mapped before assuming that the file will behave like NIMAS.

---

## NIMAS XML

A NIMAS source might contain:

```text
- structured headings
- print-page information
- lists
- tables
- MathML
- images
- production notes
```

**Expected workflow:** Use the NIMAS-specific BrailleBlaster tools, then verify the automated structure and formatting.

---

## EPUB

An EPUB might contain:

```text
- Chapter 1
- Chapter 2
- Chapter 3
- navigation
- images
- captions
- footnotes
- stylesheets
```

**Expected workflow:** Open the `.epub`, verify navigation and chapter order, inspect the imported structure and embedded material, and then correct the braille formatting as necessary.

---

# Practice Document

## Scenario 1 — Markdown

```text
Filename: lesson.md

Contents:
# Fractions
## Equivalent Fractions
- 1/2
- 2/4
- 3/6
```

### Questions

1. What source format is this?
2. What should be checked first?
3. Does the Markdown indentation automatically determine final braille margins?

---

## Scenario 2 — OpenDocument

```text
Filename: lesson.odt

Contents:
A styled heading, a numbered list,
a table, and italic vocabulary terms.
```

### Questions

1. What source format is this?
2. Which imported structures should be inspected?
3. What should be checked in Braille View?

---

## Scenario 3 — LaTeX

```text
Filename: lesson.tex

Contents:
\section{Motion}

\[
v = \frac{d}{t}
\]
```

### Questions

1. What source format is this?
2. What happens to the mathematical source during the relevant import workflow?
3. What should be checked after import?

---

## Scenario 4 — General XML

```text
Filename: lesson.xml

Contents:
Publisher-created XML with section and paragraph tags.
No NIMAS documentation is supplied.
```

### Questions

1. Can this automatically be called NIMAS?
2. What should the transcriber determine first?
3. What should be verified after import?

---

## Scenario 5 — NIMAS XML

```text
Filename: textbook.xml

Contents:
A NIMAS source containing:
- headings
- page numbers
- tables
- MathML
- images
- production notes
```

### Questions

1. What makes this different from arbitrary XML?
2. Which BrailleBlaster tools should be considered?
3. What still needs to be verified manually?

---

## Scenario 6 — EPUB

```text
Filename: science.epub

Contents:
- three chapters
- images
- captions
- footnotes
- navigation
```

### Questions

1. What source format is this?
2. What should be checked first?
3. What structural information may need special attention?

---

# Answer Key

## Scenario 1 — Markdown

Markdown should import its structural markup.

Verify:

* heading levels;
* list formatting;
* list indentation;
* continuation lines;
* other Markdown structures.

**No.** Markdown indentation does not automatically mean that the resulting braille margins should be accepted without review.

---

## Scenario 2 — OpenDocument

Open the ODT and inspect:

* imported heading styles;
* numbered-list structure;
* table structure;
* italic/emphasis;
* page structure.

Then inspect the result in Braille View.

---

## Scenario 3 — LaTeX

LaTeX mathematics enters BrailleBlaster's mathematical workflow rather than simply remaining as ordinary source-code text.

Verify:

* section structure;
* equation structure;
* fraction;
* mathematical operators;
* mathematical translation;
* resulting braille.

---

## Scenario 4 — General XML

**No.**

Do not call it NIMAS simply because it is XML.

Determine:

* what XML vocabulary is being used;
* what the elements mean;
* how BrailleBlaster maps those elements;
* whether the source contains the structural information needed for the intended transcription.

Then verify the imported headings, paragraphs, lists, tables, and other structures.

---

## Scenario 5 — NIMAS XML

NIMAS is different because it uses a specific standardized XML structure for accessible instructional materials.

Consider:

* Book Tree;
* Production Note Manager;
* heading structure;
* page information;
* tables;
* lists;
* MathML;
* images and descriptions.

Automation does not eliminate proofreading. The resulting braille must still be checked.

---

## Scenario 6 — EPUB

This is an EPUB source.

Check:

* navigation;
* chapter order;
* heading hierarchy;
* images;
* captions;
* footnotes;
* lists;
* tables;
* mathematics;
* hyperlinks;
* page information where applicable.

The EPUB's packaged structure must be correctly reconstructed in BrailleBlaster before detailed transcription work proceeds.

---

# Comparison Exercise

| Source                | Extension        | What the source primarily provides                       | Main concern after import                             |
| --------------------- | ---------------- | -------------------------------------------------------- | ----------------------------------------------------- |
| **Markdown**          | `.md`            | Lightweight markup                                       | Verify markup-to-structure conversion                 |
| **OpenDocument Text** | `.odt`           | Rich word-processing structure                           | Verify styles, lists, tables, and page structure      |
| **LaTeX**             | `.tex`           | Document markup and mathematical notation                | Verify math and formatting; inspect math conversion   |
| **General XML**       | `.xml`           | Custom semantic/publishing structure                     | Determine what the XML tags actually mean             |
| **NIMAS XML**         | `.xml` / package | Standardized accessible instructional-material structure | Use NIMAS-specific tools and verify automation        |
| **EPUB**              | `.epub`          | Packaged electronic publication                          | Verify chapters, navigation, resources, and structure |

---

# Final Practice — Identify the Import Workflow

For each source, identify the format and state the **first three things** you would inspect after opening it.

### A. Markdown

```text
# Chapter 1
## Animals
- Dogs
- Cats
```

### B. ODT

A document with:

```text
- Heading 1
- Heading 2
- numbered list
- table
- italic vocabulary
```

### C. LaTeX

A mathematics chapter containing:

```text
- fractions
- superscripts
- displayed equations
```

### D. General XML

```xml
<chapter>
  <title>Energy</title>
  <p>Energy can change form.</p>
</chapter>
```

### E. NIMAS XML

A textbook file containing:

```text
- headings
- page numbers
- tables
- MathML
- images
- production notes
```

### F. EPUB

A three-chapter EPUB containing:

```text
- images
- captions
- footnotes
- navigation
```

---

# Final Answer Key

### A. Markdown

1. Heading structure.
2. List structure.
3. Whether Markdown markup has been converted into appropriate BrailleBlaster styles.

### B. ODT

1. Heading styles.
2. Table structure.
3. Numbered-list structure.

### C. LaTeX

1. Mathematical structure.
2. Math conversion/import.
3. Resulting mathematical braille.

### D. General XML

1. What XML vocabulary is being used.
2. How `<title>` maps.
3. How `<p>` maps.

### E. NIMAS XML

1. Book Tree/headings.
2. Production Notes.
3. Page numbers, tables, lists, and mathematics.

### F. EPUB

1. Chapter/navigation order.
2. Headings and structural hierarchy.
3. Images, captions, footnotes, and other embedded resources.

---

# Production Checklist

Before beginning detailed transcription work after any import:

* [ ] Correct file opened.
* [ ] Correct source format identified.
* [ ] If XML, determined whether it is general XML (or HTML) or NIMAS.
* [ ] Imported document structure reviewed.
* [ ] Headings checked.
* [ ] Lists checked.
* [ ] Tables checked.
* [ ] Images/captions checked.
* [ ] Mathematics checked.
* [ ] Page information checked.
* [ ] Special symbols checked.
* [ ] Footnotes/endnotes checked where applicable.
* [ ] EPUB navigation checked where applicable.
* [ ] Braille View inspected.
* [ ] Print View compared with the source.
* [ ] Import errors corrected manually.
* [ ] Source-specific BrailleBlaster tools used where appropriate.

---

# Core Principles

### 1. Import first; validate second.

An imported file is a starting point, not a finished transcription.

### 2. The extension does not tell the whole story.

A `.xml` file is not automatically NIMAS.

### 3. Structure must be verified.

A heading that looks correct in Print View may still have the wrong BrailleBlaster style.

### 4. Mathematics requires special attention.

LaTeX mathematical notation enters BrailleBlaster's math workflow and must be checked in the resulting braille.

### 5. EPUB deserves its own workflow.

An EPUB is a packaged electronic publication, not simply another form of XML or a Word document.

### 6. Automation does not replace proofreading.

Whether the source is Markdown, ODT, LaTeX, XML, NIMAS, or EPUB, the transcriber remains responsible for verifying the final braille.

> **The extension tells you how the source is encoded; the source structure tells you what BrailleBlaster can preserve.**

---

# Source Citations

* **BrailleBlaster current documentation** — supported opening formats and file-import behavior, including Markdown, OpenDocument, LaTeX, XML, EPUB, and other supported formats.
* **BrailleBlaster FAQ** — supported Markdown, ODT, DOCX, HTML, EPUB3, XML, and TXT files.
* **BrailleBlaster User Manual** — LaTeX, Pandoc-supported document types, and mathematical import/conversion.
* **BrailleBlaster User Manual** — NIMAS-specific operations, Book Tree, and Production Note Manager.
* **BrailleBlaster release information** — EPUB importer and NIMAS/XML improvements.
