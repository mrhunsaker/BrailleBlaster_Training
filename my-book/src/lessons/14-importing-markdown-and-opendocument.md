# Lesson 14: Importing Source Formats I: Markdown and OpenDocument

> **Lesson at a glance**
>
> - **Unit:** Unit 2: Advanced Lessons
> - **Suggested time:** about 2 hours
> - **Prerequisites:** [Lesson 2](02-opening-word-documents.md), [Lesson 4](04-layout-styles.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- State what structure Markdown and OpenDocument Text carry into BrailleBlaster.
- Open each format and know what to verify afterward.
- Spot the Markdown list problem that needs checking after import.

## Why this matters

[Lesson 2](02-opening-word-documents.md) covered Word and OpenDocument files, and [Lesson 20](20-nimas-production-files.md) covered NIMAS XML — but BrailleBlaster's list of supported open formats is longer than either chapter suggests on its own: Markdown (.md), LaTeX (.tex), plain XHTML, EPUB, plain text, and BRF/BRL round out the list. Each of these arrives in a transcriber's inbox for a different reason, and each brings its own trade-offs worth understanding up front, rather than learning by surprise the first time a file behaves unexpectedly.

---

## How to use this lesson

This is the first of three lessons about opening source files that are not Word documents. Here you learn how BrailleBlaster treats **Markdown** and **OpenDocument Text**. [Lesson 15](15-importing-latex-xml-nimas-epub.md) covers LaTeX, general XML, NIMAS, and EPUB, and [Lesson 16](16-choosing-an-import-workflow.md) brings all six formats together so you can practice choosing the right workflow.

Read each part, work through the practice items, and check yourself against the answer key. The goal in every case is the same: to learn what BrailleBlaster can preserve, and what you must verify after import.

---
## The Concept

### Different source formats carry different kinds of structure

BrailleBlaster can open several formats, including Markdown, OpenDocument Text (`.odt`), LaTeX, XML/NIMAS, DOCX, HTML, EPUB, and text files.

These formats are not interchangeable.

* **Markdown** expresses structure through lightweight markup such as `#`, `-`, `*`, and other Markdown conventions.
* **OpenDocument Text** can contain rich word-processing structure similar to Microsoft's DOCX format.
* **LaTeX** represents document structure and mathematical notation through commands.
* **General XML** can carry explicit semantic and publishing structure, but the meaning of its tags depends on the XML vocabulary being used.
* **NIMAS XML** is a specific XML-based format intended for accessible instructional materials and has a more standardized structure that BrailleBlaster can use for specialized processing.
* **EPUB** is a packaged electronic publication that can contain multiple structured content files, navigation information, images, styles, and other resources.

#### The most important rule

> **The file extension tells you how the source is encoded; the source structure tells you what BrailleBlaster can preserve.**

Opening a source file is only the beginning of the transcription process. After importing, the transcriber must inspect the structure and verify that the resulting braille is correct.

---

## Importing Markdown

### What Markdown is

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

### Opening a Markdown file

1. Open BrailleBlaster.
2. Select **File > Open**.
3. Select the `.md` file.
4. Allow BrailleBlaster to import the document.
5. Review the resulting Print View.
6. Check the corresponding Braille View.
7. Correct imported styles where necessary.

### What to check

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

#### Important point about lists

A Markdown list such as:

```markdown
- warm
- cool
- cold
```

communicates that the material is a list.

It does **not** mean that the final braille margins should be accepted without review.

---

### Worked Demonstration — Markdown

Source:

```markdown
# Weather

## Temperature

Temperature tells us how hot or cold something is.

- warm
- cool
- cold
```

#### Expected workflow

1. Open the `.md` file.
2. Inspect the imported heading structure.
3. Verify that `# Weather` is the intended heading level.
4. Verify that `## Temperature` is the intended subordinate heading.
5. Verify that the three items are actually structured as a list.
6. Check the list margins and continuation lines in Braille View.
7. Apply or correct BrailleBlaster styles as necessary.

---

## Importing OpenOffice / OpenDocument Text

### What format is meant here?

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

### Opening an ODT file

1. Select **File > Open**.
2. Select the `.odt` file.
3. Review the imported structure.
4. Compare important formatting with the original document.
5. Correct styles that did not import as intended.
6. Check Braille View.

### What to check

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

### Worked Demonstration — OpenDocument

```text
File: weather.odt

Contains:
- Heading 1
- Heading 2
- bulleted list
- one table
```

#### Expected workflow

Open the `.odt` file and inspect each imported structure.

Verify:

* the Heading 1 became the appropriate BrailleBlaster heading;
* the Heading 2 became the appropriate subordinate heading;
* the bulleted list is structurally a list;
* the table remains a table or has been converted into the appropriate structure;
* the table's braille presentation is correct.

---

### Practice

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

#### Answer Key

At minimum:

1. Unit heading structure.
2. Heading hierarchy.
3. Numbered-list structure.
4. Table structure.
5. Caption treatment.
6. Page breaks/page information where applicable.
7. Braille View and resulting margins.

---

---

## Source Citations

* **BrailleBlaster current documentation** — supported opening formats and file-import behavior, including Markdown, OpenDocument, LaTeX, XML, EPUB, and other supported formats.
* **BrailleBlaster FAQ** — supported Markdown, ODT, DOCX, HTML, EPUB3, XML, and TXT files.
* **BrailleBlaster User Manual** — LaTeX, Pandoc-supported document types, and mathematical import/conversion.
* **BrailleBlaster User Manual** — NIMAS-specific operations, Book Tree, and Production Note Manager.
* **BrailleBlaster release information** — EPUB importer and NIMAS/XML improvements.
