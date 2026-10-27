# UEB Practice: Opening and Converting Word Documents

## How to use this document:

The first half explains what happens when a Microsoft Word document enters BrailleBlaster. The second half is a practice document — use the supplied Word-style source descriptions to decide what should be preserved automatically, what should be checked, and what should be reformatted inside BrailleBlaster. The goal is to learn the difference between **opening a file** and **finishing a braille transcription**.

---

## The Concept

### Opening a DOCX is an import operation, not a finished transcription

BrailleBlaster can open Microsoft Word `.docx` files. When a file is opened, its structural information is interpreted and brought into BrailleBlaster. That can include headings, lists, emphasis, tables, and other document structure.

The important teacher/transcriber habit is: **do not assume that successful opening means successful formatting.**

A Word document may contain:

- visual spacing created with tabs or empty paragraphs;
- headings represented only by font size or bold;
- nested lists with inconsistent Word indentation;
- page breaks that do not correspond to braille page breaks;
- tables whose visual layout does not map directly to braille;
- math objects that need verification;
- headers and footers that need to be interpreted rather than copied literally.

### BrailleBlaster uses document structure, but braille has its own structure

Print and braille are not equivalent page-layout systems. A Word document may use a large heading, a 24-point font, and a large top margin to communicate hierarchy. BrailleBlaster instead applies styles, margins, blank lines, page numbers, and other braille conventions.

Therefore the workflow is:

1. Open the `.docx`.
2. Inspect the Print View and Style View.
3. Verify the imported hierarchy.
4. Correct styles rather than inserting spaces manually.
5. Check page numbers, lists, emphasis, math, and tables.
6. Inspect Braille View.
7. Save the BrailleBlaster document in the working format.

### Converting a Word document outside BrailleBlaster

If a source cannot be opened directly or requires preprocessing, conversion can be useful. But conversion creates another layer of interpretation. A teacher or transcriber should know which program performed the conversion and which structural information may have changed.

The safest rule is: **preserve the original DOCX, work from a copy, and verify the imported structure in BrailleBlaster.**

---

## Worked Demonstration (small, fully correct)

Print source:

```text
SCIENCE REVIEW

Chapter 2: Matter

Matter is anything that has mass and takes up space.

1. Solids
   a. Have a definite shape
   b. Have a definite volume

2. Liquids
   a. Have a definite volume
   b. Take the shape of their container
```

Suppose the Word file uses Heading 1 for "SCIENCE REVIEW," Heading 2 for "Chapter 2: Matter," and Word's numbered-list tools for the two levels.

Correct workflow:

- Open the `.docx` with **File > Open** or `Ctrl+O`.
- Verify that the headings imported as meaningful styles rather than merely bold text.
- Verify that the two-level list is actually represented by BrailleBlaster list styles.
- Check the Braille View for the resulting margins and runovers.
- Do not repair list indentation by adding spaces.
- If the Word source used visual blank paragraphs for spacing, replace the visual trick with the appropriate BrailleBlaster style or style option.

The import is successful only when the **structure** is correct, not merely when all the words appear.

---

## Practice Document

### Scenario 1 — straightforward DOCX

```text
The Word file contains:
- Title: "Weather and Climate"
- Heading 1: "Weather"
- Heading 2: "Temperature"
- A three-item bulleted list
- One paragraph in italics for emphasis
- No tables or equations
```

### Scenario 2 — visually formatted but structurally weak DOCX

```text
The Word file contains:
- A 24-point bold line used as the title
- A 16-point bold line used as a section heading
- Five spaces before every list item (tab button is never pressed so the default list formatting in word is never triggered)
- Blank paragraphs inserted between every paragraph
- A footer containing the page number
- A two-column table
```

### Scenario 3 — mixed instructional content

```text
The Word file contains:
- Three heading levels
- A nested list
- A fraction written as a Word equation object
- A photograph with a caption
- A running header
- Print page numbers in the footer
```

For each scenario, decide which parts should be accepted provisionally and which parts require deliberate checking after import.

---

## Answer Key

### Scenario 1

Mostly straightforward. Verify the heading styles, list style, and italic emphasis in BrailleBlaster. The absence of complex structures does not eliminate the need to check Braille View.

### Scenario 2

Requires substantial cleanup. Font size and bold can help identify headings, but they are not themselves the braille heading styles. Spaces and blank paragraphs should not be treated as the final braille formatting. The table and footer require separate verification.

### Scenario 3

Requires the most checking. Headings and lists should be verified as structural elements. The equation should be checked as math rather than assumed correct because it arrived from Word. The photograph needs appropriate image handling, and the running header/page-number information must be distinguished from ordinary body text.

### Core principle

**Open first; inspect second; format third.** Do not use the apparent success of the import as proof that the braille structure is correct.

---
