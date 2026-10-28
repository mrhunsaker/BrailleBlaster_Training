# Lesson 16: Choosing an Import Workflow

> **Lesson at a glance**
>
> - **Unit:** Unit 2: Advanced Lessons
> - **Suggested time:** about 90 minutes
> - **Prerequisites:** [Lesson 14](14-importing-markdown-and-opendocument.md), [Lesson 15](15-importing-latex-xml-nimas-epub.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Identify the right import workflow from a description or sample of a source file.
- Compare all six source types side by side.
- Apply the six core principles of importing and a production checklist.

---

## How to use this lesson

This lesson is review and practice. You have now met six source formats in [Lesson 14](14-importing-markdown-and-opendocument.md) and [Lesson 15](15-importing-latex-xml-nimas-epub.md). Here you compare them side by side, work through scenarios that mix them, and finish with the production checklist and core principles you should apply after any import.

If you are teaching this course, this lesson also works well as a short unit assessment.

---
## Step by step: Choosing an Import Path

1. Identify the source file's actual format — not just its extension, but how it was produced. A `.docx` built in Google Docs, a `.docx` built in Microsoft Word, and a `.docx` built by exporting from a LaTeX tool can all behave differently on import even though they share an extension.
2. If the file is Markdown, LaTeX, or a well-structured .docx/.odt, open it directly (**File > Open**, `Ctrl+O`) and expect a reasonably faithful structural transfer, subject to the review habits from [Lesson 2](02-opening-word-documents.md).
3. If the file is LaTeX and contains packages or notation BrailleBlaster doesn't support cleanly, convert to HTML with a tool like TeX4HT, rename any resulting `.xht` file to `.xhtml`, and open that instead.
4. If the file is a non-NIMAS XML format BrailleBlaster doesn't recognize, convert it to HTML or another supported format using an external tool before opening it in BrailleBlaster.
5. Regardless of source format, review the imported document's structure with Breadcrumbs before beginning detailed editing — the review discipline from [Lesson 2](02-opening-word-documents.md) applies across every import path in this lesson, not just Word.

---

## Worked Demonstration — Comparing All Six Source Types

### Markdown

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

### OpenDocument

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

### LaTeX

```latex
\section{Energy}

The formula is $E=mc^2$.
```

**Expected workflow:** Open the `.tex`, verify the section structure, and inspect the imported mathematics.

---

### General XML

```xml
<section>
  <h1>Energy</h1>
  <p>Energy can change from one form to another.</p>
</section>
```

**Expected workflow:** Determine what XML vocabulary is being used and how the tags are mapped before assuming that the file will behave like NIMAS.

---

### NIMAS XML

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

### EPUB

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

## Practice Document

### Scenario 1 — Markdown

```text
Filename: lesson.md

Contents:
# Fractions
## Equivalent Fractions
- 1/2
- 2/4
- 3/6
```

#### Questions

1. What source format is this?
2. What should be checked first?
3. Does the Markdown indentation automatically determine final braille margins?

---

### Scenario 2 — OpenDocument

```text
Filename: lesson.odt

Contents:
A styled heading, a numbered list,
a table, and italic vocabulary terms.
```

#### Questions

1. What source format is this?
2. Which imported structures should be inspected?
3. What should be checked in Braille View?

---

### Scenario 3 — LaTeX

```text
Filename: lesson.tex

Contents:
\section{Motion}

\[
v = \frac{d}{t}
\]
```

#### Questions

1. What source format is this?
2. What happens to the mathematical source during the relevant import workflow?
3. What should be checked after import?

---

### Scenario 4 — General XML

```text
Filename: lesson.xml

Contents:
Publisher-created XML with section and paragraph tags.
No NIMAS documentation is supplied.
```

#### Questions

1. Can this automatically be called NIMAS?
2. What should the transcriber determine first?
3. What should be verified after import?

---

### Scenario 5 — NIMAS XML

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

#### Questions

1. What makes this different from arbitrary XML?
2. Which BrailleBlaster tools should be considered?
3. What still needs to be verified manually?

---

### Scenario 6 — EPUB

```text
Filename: science.epub

Contents:
- three chapters
- images
- captions
- footnotes
- navigation
```

#### Questions

1. What source format is this?
2. What should be checked first?
3. What structural information may need special attention?

---

## Answer Key

### Scenario 1 — Markdown

Markdown should import its structural markup.

Verify:

* heading levels;
* list formatting;
* list indentation;
* continuation lines;
* other Markdown structures.

**No.** Markdown indentation does not automatically mean that the resulting braille margins should be accepted without review.

---

### Scenario 2 — OpenDocument

Open the ODT and inspect:

* imported heading styles;
* numbered-list structure;
* table structure;
* italic/emphasis;
* page structure.

Then inspect the result in Braille View.

---

### Scenario 3 — LaTeX

LaTeX mathematics enters BrailleBlaster's mathematical workflow rather than simply remaining as ordinary source-code text.

Verify:

* section structure;
* equation structure;
* fraction;
* mathematical operators;
* mathematical translation;
* resulting braille.

---

### Scenario 4 — General XML

**No.**

Do not call it NIMAS simply because it is XML.

Determine:

* what XML vocabulary is being used;
* what the elements mean;
* how BrailleBlaster maps those elements;
* whether the source contains the structural information needed for the intended transcription.

Then verify the imported headings, paragraphs, lists, tables, and other structures.

---

### Scenario 5 — NIMAS XML

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

### Scenario 6 — EPUB

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

## Comparison Exercise

| Source                | Extension        | What the source primarily provides                       | Main concern after import                             |
| --------------------- | ---------------- | -------------------------------------------------------- | ----------------------------------------------------- |
| **Markdown**          | `.md`            | Lightweight markup                                       | Verify markup-to-structure conversion                 |
| **OpenDocument Text** | `.odt`           | Rich word-processing structure                           | Verify styles, lists, tables, and page structure      |
| **LaTeX**             | `.tex`           | Document markup and mathematical notation                | Verify math and formatting; inspect math conversion   |
| **General XML**       | `.xml`           | Custom semantic/publishing structure                     | Determine what the XML tags actually mean             |
| **NIMAS XML**         | `.xml` / package | Standardized accessible instructional-material structure | Use NIMAS-specific tools and verify automation        |
| **EPUB**              | `.epub`          | Packaged electronic publication                          | Verify chapters, navigation, resources, and structure |

---

## Final Practice — Identify the Import Workflow

For each source, identify the format and state the **first three things** you would inspect after opening it.

#### A. Markdown

```text
# Chapter 1
## Animals
- Dogs
- Cats
```

#### B. ODT

A document with:

```text
- Heading 1
- Heading 2
- numbered list
- table
- italic vocabulary
```

#### C. LaTeX

A mathematics chapter containing:

```text
- fractions
- superscripts
- displayed equations
```

#### D. General XML

```xml
<chapter>
  <title>Energy</title>
  <p>Energy can change form.</p>
</chapter>
```

#### E. NIMAS XML

A textbook file containing:

```text
- headings
- page numbers
- tables
- MathML
- images
- production notes
```

#### F. EPUB

A three-chapter EPUB containing:

```text
- images
- captions
- footnotes
- navigation
```

---

## Final Answer Key

#### A. Markdown

1. Heading structure.
2. List structure.
3. Whether Markdown markup has been converted into appropriate BrailleBlaster styles.

#### B. ODT

1. Heading styles.
2. Table structure.
3. Numbered-list structure.

#### C. LaTeX

1. Mathematical structure.
2. Math conversion/import.
3. Resulting mathematical braille.

#### D. General XML

1. What XML vocabulary is being used.
2. How `<title>` maps.
3. How `<p>` maps.

#### E. NIMAS XML

1. Book Tree/headings.
2. Production Notes.
3. Page numbers, tables, lists, and mathematics.

#### F. EPUB

1. Chapter/navigation order.
2. Headings and structural hierarchy.
3. Images, captions, footnotes, and other embedded resources.

---

## Production Checklist

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

## Core Principles

#### 1. Import first; validate second.

An imported file is a starting point, not a finished transcription.

#### 2. The extension does not tell the whole story.

A `.xml` file is not automatically NIMAS.

#### 3. Structure must be verified.

A heading that looks correct in Print View may still have the wrong BrailleBlaster style.

#### 4. Mathematics requires special attention.

LaTeX mathematical notation enters BrailleBlaster's math workflow and must be checked in the resulting braille.

#### 5. EPUB deserves its own workflow.

An EPUB is a packaged electronic publication, not simply another form of XML or a Word document.

#### 6. Automation does not replace proofreading.

Whether the source is Markdown, ODT, LaTeX, XML, NIMAS, or EPUB, the transcriber remains responsible for verifying the final braille.

> **The extension tells you how the source is encoded; the source structure tells you what BrailleBlaster can preserve.**

---

---

## Key takeaways

BrailleBlaster opens Markdown, OpenDocument, LaTeX, plain text, HTML/XHTML, EPUB, and NIMAS XML directly, in addition to Word — each format arrives via a different real-world workflow.
- Markdown's explicit structural syntax tends to import more predictably than word-processor formatting, for the same reason a well-built Word document outperforms a fake-structured one ([Lesson 2](02-opening-word-documents.md)).
- LaTeX files retain their formatting and math on import without requiring LaTeX to be installed, but unsupported packages or notation may require converting to HTML (via TeX4HT or similar) first — and renaming the resulting `.xht` file to `.xhtml`.
- Non-NIMAS XML generally needs conversion to a more general format before it opens cleanly, since BrailleBlaster's XML support centers on the NIMAS schema.

---

## Source Citations

* **BrailleBlaster current documentation** — supported opening formats and file-import behavior, including Markdown, OpenDocument, LaTeX, XML, EPUB, and other supported formats.
* **BrailleBlaster FAQ** — supported Markdown, ODT, DOCX, HTML, EPUB3, XML, and TXT files.
* **BrailleBlaster User Manual** — LaTeX, Pandoc-supported document types, and mathematical import/conversion.
* **BrailleBlaster User Manual** — NIMAS-specific operations, Book Tree, and Production Note Manager.
* **BrailleBlaster release information** — EPUB importer and NIMAS/XML improvements.
