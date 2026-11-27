# Lesson 33: What Makes a Good Source

> **Lesson at a glance**
>
> - **Unit:** Unit 5: Handbook (Supplemental)
> - **Suggested time:** about 90 minutes
> - **Prerequisites:** [Lesson 2](02-opening-word-documents.md), [Lesson 14](14-importing-markdown-and-opendocument.md), [Lesson 16](16-choosing-an-import-workflow.md)
> - **You will need:** A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Rank the common source types by how much structure each carries into BrailleBlaster.
- Name the file types BrailleBlaster opens, and say how each is read.
- Apply the ten import-safety rules that protect a document from silent loss.
- Write a clear source request that a teacher, author, or publisher can act on.

> [!IMPORTANT]
> The source ladder is a triage aid, not a guarantee that a higher-ranked format is accurate or complete. Even a well-structured DOCX or NIMAS package can contain wrong content, missing images, inaccessible math, or stale revisions; compare it with the authoritative source.

## Why this matters

The quality of a braille transcription is limited by the quality of its source. A well-built source gives BrailleBlaster real headings, real lists, real math, and real page numbers, and the transcriber spends the time on judgment. A flat or damaged source gives BrailleBlaster only text, and the transcriber spends the time rebuilding structure by hand, with every chance to introduce an error.

Most transcribers cannot choose their sources, but they can **ask for better ones**, and they can **recognize damage early**. This unit of the course, the Handbook, teaches the skills that happen *before* BrailleBlaster opens a file: how sources are built, how to read them, how to repair them, and how to request them. This first lesson is the map.

{HB}

---

## How to use this lesson

Read the **source ladder** and the **ten rules**, then do the ranking exercise. Keep this page open as you work through the rest of the Handbook, because every later lesson refers back to it.

---

## The Concept

### The source ladder

From richest structure to poorest. Each step down means more work and more risk for you.

| Rank | Source | What it carries | What to expect |
| ---- | ------ | --------------- | -------------- |
| 1 | **NIMAS file set** (DTBook XML with a package file) from a publisher | Headings, lists, tables, page numbers, math as MathML, notes, image groups with descriptions | The best case. BrailleBlaster has a dedicated importer for it. Still proofread ([Lesson 20](20-nimas-production-files.md)) |
| 2 | **Word or LibreOffice file built with real styles** | Heading levels, list structure, emphasis, page breaks | Very good. See [Lesson 35](35-word-structure-with-styles.md) and [Lesson 36](36-libreoffice-openoffice-and-google-docs.md) |
| 3 | **EPUB** | Chapters, headings, lists, links, images | Good if it was built with structure. Check the order of content |
| 4 | **Markdown, LaTeX, or HTML** written with structure in mind | Whatever the author marked up | Excellent for math (LaTeX) and for plain structure (Markdown). See [Lessons 34](34-markdown-syntax-guide.md) and [40](40-latex-for-transcribers.md) |
| 5 | **Flat Word file** that only *looks* formatted | Words, direct bold and italic, typed bullets | Most of the structure must be rebuilt ([Lab 1](../labs/lab-1-rescue-word-document.md)) |
| 6 | **Plain text** | Words only, one paragraph per line | No structure at all, but at least no damage |
| 7 | **Text-based PDF** | Words, in an order that may be wrong | Copy-paste damage is likely ([Lesson 42](42-pdfs-scans-and-ocr.md)) |
| 8 | **Scanned PDF or photograph** | Pixels | Must be OCR'd, and every word proofread against the print |
| 9 | **Print only** | Paper | Scan, OCR, and proofread, or retype |

### What BrailleBlaster opens, and how

The **File > Open** dialog recognizes these types. Most are read by the bundled converter **Pandoc** (version 3.12.1 at the time of writing), then passed through BrailleBlaster's own conversion script, `bbx.lua`.

| Extension | How it is read |
| --------- | -------------- |
| `.docx` | Pandoc, as `docx` with the *styles* and *empty paragraphs* options, plus two extra filters that keep Word page breaks and empty paragraphs |
| `.odt` | Pandoc, as `odt` (no style names, no page breaks) |
| `.md` | Pandoc, as `markdown` (Pandoc's own flavor, with its default extensions) |
| `.tex` | Pandoc, as `latex` |
| `.epub` | Pandoc, as `epub` |
| `.html`, `.htm`, `.xhtml`, `.xhtm`, `.xht` | Pandoc, as `html` with empty paragraphs kept |
| `.xml`, and a `.zip` holding an `.opf` | BrailleBlaster's **NIMAS** importer (not Pandoc) |
| `.txt` | BrailleBlaster directly: each **non-blank line** becomes one Body Text paragraph |
| `.bbx`, `.bbz` | BrailleBlaster's own formats |
| `.brf`, `.brl` | Braille files. A BRF opens only in the Braille Preview |

Pandoc is a *document converter*: it turns the source into a neutral structure, and then `bbx.lua` turns that structure into BrailleBlaster's XML. **What `bbx.lua` does not recognize, it ignores.** That is why the next section matters.

### Ten import-safety rules

These came from running BrailleBlaster's own conversion script, with the bundled Pandoc version, on test files. They describe what the script does. Confirm them in your copy of the program.

1. **Do not leave an image alone in its paragraph.** An image that is the only thing in its paragraph, and a LaTeX `figure` or HTML `<figure>`, is turned by Pandoc into a *figure*, which the script does not handle. In testing, both the image **and its caption** disappeared. An image *inside a sentence* was kept. Count your figures before and after every import.
2. **Do not write poetry as a Markdown line block** (lines that start with `|`). In testing, it made the conversion fail with an error. Use hard line breaks (a backslash at the end of each line) instead.
3. **Do not rely on document metadata.** A Markdown YAML header, and a LaTeX `\title`, `\author`, and `\maketitle`, produced no output in testing. The title page is yours to build ([Lesson 24](24-t-page-generator.md)).
4. **Use real heading styles, and remember the collapse.** Heading level 1 becomes a **Centered Heading**, level 2 a **Cell 5 Heading**, and levels 3 to 6 all a **Cell 7 Heading**. If your print has four levels, you must decide the mapping ([Lesson 5](05-heading-levels.md)).
5. **The Word *Title* style is not a heading.** It arrives as ordinary body text.
6. **Strikethrough is dropped.** The text stays, and the line through it does not.
7. **Subscript and superscript become literal characters** (`H_2O`, `x^2`) outside math. Put real math in a math tool.
8. **Inline code breaks the paragraph.** It becomes its own displayed block in the middle of the sentence.
9. **Hard-wrapped plain text becomes one paragraph per line.** Write one line per paragraph, with a blank line between paragraphs only if you want them to look separate in your editor.
10. **Characters that are not allowed in XML 1.0 are deleted** from a plain text file, with only a log entry to show for it. Clean control characters first ([Lesson 41](41-text-encoding-and-braille-characters.md)).

> [!IMPORTANT]
> Rules 1 to 3 lose content **silently**. No error appears, and the Braille View looks tidy. The only defense is a deliberate comparison with the source after every import. Make "count the figures, read the first and last paragraph of every chapter" part of your routine ([Lesson 32](32-proofreading-and-quality-assurance.md)).

### What good source looks like: a short requirements list

When you can ask for a source, ask for these things:

- **Real styles** for headings, lists, quotations, captions, and notes. Not bold text in a bigger font.
- **No text boxes, columns, or tables used for layout.** They scramble the reading order.
- **Images inline with their text, with alt text.** And a separate caption paragraph when there is one.
- **Mathematics as equations** (Word equations, LaTeX, or MathML), not as pictures.
- **Tables as real tables**, with a header row.
- **Print page numbers** marked in the text, if the braille must refer to the print.
- **A NIMAS file set**, if the title is a textbook and the student qualifies ([Policy and Standards Background](../reference/policy-background.md)).
- **One source per volume or chapter**, if the book is large and several people will work on it.

---

## Step by step

### Triage a new source

1. **Identify the format** from the extension, then open the file in its own program as well as BrailleBlaster.
2. **Place it on the ladder.** Decide whether to repair it, rebuild it, or ask for a better one.
3. **Check the safety rules.** Look for stand-alone images, line blocks, metadata, and Title styles.
4. **Make a copy** and work on the copy.
5. **Record the decision** on your Import Log ([Job Aids](../reference/job-aids.md)).

### Write a source request

Keep it short, polite, and specific. A model:

> **Subject:** Source file for *Energy and Motion*, Chapter 3
>
> Thank you for sending the chapter. To make an accurate braille copy, could you send the original **Word file** (not a PDF)? If the chapter was written in Word, it would help if:
>
> - headings use Word's Heading styles and lists use list styles;
> - pictures sit inside a line of text, with alt text;
> - equations were typed with Word's equation tool and not pasted as pictures.
>
> If the publisher supplied a **NIMAS file** for this title, that would be even better. I can open either one directly. If neither exists, a clean scan is fine, and I will proofread it against the book.
>
> Thank you,

---

## Practice

### Exercise 1: Rank the sources

Place each source on the ladder, and say what you would ask for.

1. A teacher emails a PDF of a worksheet exported from Word.
2. A district sends a ZIP with an `.opf` file and an `.xml` file for a science textbook.
3. A professor sends a `.tex` file with fifty equations.
4. A colleague sends a Word file in which the headings are bold 16-point text and the bullets are typed `-` characters.
5. A parent scans a worksheet with a phone and sends a photograph.
6. A teacher sends a text file in which every line was broken at 70 characters.

### Exercise 2: Spot the loss

A Markdown file has: a YAML title block, a poem written with `|` line blocks, a picture alone on a line with a caption, and a footnote. List what you would expect to lose or break, and what you would do before importing.

### Answer Key

**Exercise 1.**

1. **Rank 7 (text-based PDF), or better if the Word original exists.** Ask for the Word file. A PDF exported from Word has lost its styles.
2. **Rank 1 (NIMAS).** Open it with the NIMAS importer, and proofread it.
3. **Rank 4 (LaTeX).** Good for math. Check every equation, and remember that the title block will not import.
4. **Rank 5 (flat Word).** Rebuild the headings and lists, or ask the author to use styles.
5. **Rank 8 (scan).** Ask for the original file. If none exists, OCR it and proofread every word.
6. **Rank 6 (plain text), with a problem.** The hard wraps will make every line a paragraph. Ask for the text with one paragraph per line, or reflow it first ([Lesson 41](41-text-encoding-and-braille-characters.md)).

**Exercise 2.** The **title** will not import (rule 3), so plan a title page. The **poem** will make the conversion fail (rule 2), so rewrite it with backslash line breaks. The **picture and caption** will both vanish (rule 1), so put the image inside a sentence or follow it with text in the same paragraph. The **footnote** will survive, as a `^1` marker and a "Footnotes" section at the end, so decide whether to keep that arrangement.

---

## Key takeaways

- Transcription quality is capped by source quality. Rank the source, and ask for a better one when you can.
- BrailleBlaster reads most formats through Pandoc and then its own script, which **ignores what it does not recognize**.
- Three rules lose content silently: stand-alone images and figures, Markdown line blocks, and document metadata. Compare the result with the source every time.
- Heading level 1, 2, and 3 to 6 become Centered, Cell 5, and Cell 7 headings. Word's Title style is not a heading.
- Plain text is one paragraph per non-blank line.

---

## Source Citations

- The BrailleBlaster program source (the conversion script `bbx.lua` and the Pandoc loader), read at commit `369176b`, with the conversion tests run using Pandoc 3.12.1, the version BrailleBlaster bundles.
- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/): "Opening Files."
- [Policy and Standards Background](../reference/policy-background.md), for NIMAS.
