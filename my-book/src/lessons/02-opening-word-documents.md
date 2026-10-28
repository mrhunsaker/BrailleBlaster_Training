# Lesson 2: Opening and Converting Word Documents

> **Lesson at a glance**
>
> - **Unit:** Unit 1: Universal Lessons
> - **Suggested time:** about 3 hours
> - **Prerequisites:** [Lesson 1](01-navigating-the-interface.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Explain why opening a `.docx` file is an import, not a finished transcription.
- Tell a structurally well-built Word document from one that only looks well built.
- Inspect an imported document in the Print View and Style View and correct styles instead of adding spaces.
- Decide when converting a file outside BrailleBlaster is worth the extra layer of interpretation.

## Why this matters

In production transcription work, print material rarely arrives as a NIMAS file — it just as often arrives as a Word document (.docx) or, less commonly today, an OpenDocument Text file (.odt) from a publisher, a teacher, or a parent. BrailleBlaster can open both directly, using the structure already present in the file — headings, lists, bold and italic runs, tables — to jump-start the transcription instead of starting from a blank page. How well that jump-start works, though, depends entirely on how well-structured the source file is, which makes this lesson as much about *diagnosing* a Word document as it is about opening one.

---

## How to use this lesson

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

## Step by step in BrailleBlaster

### Opening a Well-Formatted Word Document

1. Go to **File > Open** (`Ctrl+O`).
2. Select the .docx or .odt file. BrailleBlaster recognizes both extensions directly, alongside NIMAS XML, EPUB, HTML, Markdown, LaTeX, plain text, and several others.
3. Review the incoming document with Breadcrumbs turned on (**View > Toggle Views > Breadcrumbs**), scanning headings, lists, and emphasized text to see how much came in correctly mapped.
4. Correct anything that mapped imperfectly — this is normal even with a well-built source file, and is not a sign of an error on your part.

### Troubleshooting Poorly Formatted Word or ODT Documents

When a document arrives with structure that was faked visually rather than built properly (manually-indented "headings," tab-and-space "lists," font-size changes standing in for real heading levels), expect BrailleBlaster to bring it in largely as undifferentiated Body Text. Work through it methodically rather than reformatting reactively line by line:

1. **Read before you fix.** Skim the whole incoming document first — in the original Word/ODT file if possible, side by side with BrailleBlaster — to understand what the author actually intended structurally (where the real headings, real lists, and real emphasis are meant to be), before applying any styles.
2. **Fix structure before emphasis.** Apply correct heading and list styles first. Fixing emphasis on text that's about to be restyled anyway wastes effort, since restyling a container can affect how emphasis displays within it.
3. **Use Find and Replace with Formatting** (covered in full in [Lesson 12](12-find-and-replace.md)) to locate every instance of a particular visual pattern — for example, every paragraph that's merely bolded and slightly larger, standing in for a heading — and correct them as a batch rather than one at a time.
4. **Watch for inconsistency, not just absence.** A poorly-formatted document is often *inconsistently* fake-structured: some "headings" are done with bold-and-larger-font, others with all-caps, others with manual centering. Don't assume the same fix pattern applies throughout; verify each section.
5. **When in doubt, treat it as prose and add structure deliberately**, the same way you would if you were transcribing directly from a printed page rather than an electronic file. BrailleBlaster's ability to read Word's internal structure is a shortcut when that structure is real — it isn't a substitute for reading the document.

> **Note:** If a .docx file behaves unpredictably on open — content missing, structure garbled beyond what fake-formatting alone would explain — it's sometimes faster to convert it to a plainer intermediate format (HTML, for instance, using Word's own "Save As") and reopen that, since a simpler format leaves less room for BrailleBlaster to misinterpret. This is the same idea used for stubborn LaTeX files (see [Lesson 8](08-ascii-math-hub.md)'s math workflow, and [Lesson 17](17-what-pandoc-does.md) on Pandoc).

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

---

## Key takeaways

- BrailleBlaster reads the actual internal structure of .docx and .odt files, not just their visual appearance.
- A well-built source document (real headings, real lists, real character styles) transfers into BrailleBlaster with much of its layout already correct.
- A visually-formatted-but-structurally-flat document transfers in as largely undifferentiated Body Text, regardless of how correct it looks in Word.
- Diagnose before fixing: read the whole document, correct structure before emphasis, and use Find and Replace with Formatting to batch-correct repeated patterns.
- When a file behaves unpredictably, converting to a simpler intermediate format and reopening it can be faster than fighting the original.
