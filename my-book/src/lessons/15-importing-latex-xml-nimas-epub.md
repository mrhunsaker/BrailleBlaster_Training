# Lesson 15: Importing Source Formats II: LaTeX, XML, NIMAS, and EPUB

> **Lesson at a glance**
>
> - **Unit:** Unit 2: Advanced Lessons
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 14](14-importing-markdown-and-opendocument.md), [Lesson 7](07-math-translation-toggle.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Explain the special math consequence of importing LaTeX.
- Distinguish general XML from NIMAS XML.
- Treat EPUB as its own packaged-publication workflow.
- Write a post-import checklist for each format.

---

## How to use this lesson

This lesson continues from [Lesson 14](14-importing-markdown-and-opendocument.md) with the four formats that need the most care: **LaTeX**, **general XML**, **NIMAS XML**, and **EPUB**. Keep the key rule from Lesson 14 in mind throughout: the file extension tells you how the source is encoded, and the source structure tells you what BrailleBlaster can preserve.

NIMAS also has its own full lesson in the transcriber track ([Lesson 20](20-nimas-production-files.md)). Here you only need to be able to recognize NIMAS and keep it separate from general XML.

---
## Importing LaTeX

### What LaTeX is

LaTeX is a markup system commonly used for technical and mathematical documents.

For example:

```latex
\section{Energy}

The formula is $E=mc^2$.
```

LaTeX communicates both document structure and mathematical notation through commands.

### LaTeX has a special math consequence

When LaTeX is opened in BrailleBlaster, LaTeX mathematics is converted into **ASCII Math** in the relevant workflow.

The current BrailleBlaster documentation notes an important exception involving NIMAS XML, TXT, BRL, and ZIP file types.

Therefore:

> **Do not assume that seeing LaTeX source commands in the original file means those commands will remain visible after import.**

The mathematics enters BrailleBlaster's math workflow and must be checked there.

### What to check

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

### Worked Demonstration — LaTeX

Source:

```latex
\section{Motion}

\[
v = \frac{d}{t}
\]
```

#### Expected workflow

1. Open the `.tex` file.
2. Verify that `Motion` became the intended heading.
3. Inspect the imported equation.
4. Verify the fraction structure.
5. Check the mathematical representation.
6. Check the resulting braille.

Do not assume that a visually correct Print View guarantees a correct mathematical braille representation.

---

### Practice

Import:

```latex
\section{Fractions}

\[
\frac{3}{4} + \frac{1}{2} = \frac{5}{4}
\]
```

#### Answer Key

Check:

1. The heading.
2. The three fractions.
3. The mathematical operators.
4. The imported math structure.
5. The resulting braille.

---

## Importing General XML

### XML is not automatically NIMAS

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

### Why general XML needs separate treatment

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

### Worked Demonstration — General XML

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

#### Expected workflow

1. Determine what XML vocabulary is being used.
2. Identify the semantic meaning of the tags.
3. Open the XML in BrailleBlaster.
4. Inspect how the tags were mapped.
5. Verify the heading structure.
6. Verify the paragraph structure.
7. Check Braille View.
8. Manually correct anything that did not map as intended.

---

### Practice

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

#### Answer Key

1. `<heading>` is probably a heading.
2. `<item>` elements are probably list items.
3. Verify that BrailleBlaster actually imported them as the intended styles and list structure. Check indentation, continuation lines, and Braille View.

---

## Importing NIMAS XML

### NIMAS is a specific XML workflow

NIMAS is an XML-based standard used for accessible instructional materials.

It is important to distinguish:

> **General XML is not automatically NIMAS.**

NIMAS has a particular structure and intended use, and BrailleBlaster provides specialized tools for NIMAS files.

### NIMAS-specific features

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

### Production Notes

NIMAS files may contain publisher production notes.

The transcriber should review these notes and determine how they should be handled rather than automatically assuming that every production note belongs in the final braille.

BrailleBlaster's Production Note Manager provides options for handling production notes.

### NIMAS practice

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

#### Key distinction

**General XML**

> Determine what the XML structure means.

**NIMAS XML**

> Use the standardized structure and NIMAS-specific BrailleBlaster tools, then verify the automated formatting.

---

## Importing EPUB Specifically

### EPUB is its own import workflow

BrailleBlaster supports **EPUB e-books (`.epub`)** as an input format.

EPUB should be treated separately from both general XML and NIMAS.

An EPUB is a packaged electronic publication. It can contain multiple structured content files along with navigation, styles, images, metadata, and other resources.

### Opening an EPUB

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

### Why EPUB needs careful review

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

### Worked Demonstration — EPUB

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

#### Check 1 — Navigation

Do the chapters appear in the correct order?

#### Check 2 — Headings

Do the chapter titles have appropriate heading levels?

#### Check 3 — Lists

Are list items actually structured as lists?

#### Check 4 — Figures

Is the image present or represented appropriately?

Is the caption separated from any transcriber-generated description?

#### Check 5 — Page Structure

Does the imported document need print-page information or other production formatting added?

---

---

## Source Citations

* **BrailleBlaster current documentation** — supported opening formats and file-import behavior, including Markdown, OpenDocument, LaTeX, XML, EPUB, and other supported formats.
* **BrailleBlaster FAQ** — supported Markdown, ODT, DOCX, HTML, EPUB3, XML, and TXT files.
* **BrailleBlaster User Manual** — LaTeX, Pandoc-supported document types, and mathematical import/conversion.
* **BrailleBlaster User Manual** — NIMAS-specific operations, Book Tree, and Production Note Manager.
* **BrailleBlaster release information** — EPUB importer and NIMAS/XML improvements.
