# Lab 2: Import Comparison Lab

**Time:** about 90 minutes. **Needs:** [Lessons 14](../lessons/14-importing-markdown-and-opendocument.md), [15](../lessons/15-importing-latex-xml-nimas-epub.md), and [16](../lessons/16-choosing-an-import-workflow.md). **Files:** `word-01-well-structured.docx`, `sample.odt`, `markdown-samples.zip` (unzip it first), `sample.tex`, and `sample.epub`. **Job aid:** the Import Log in [Job Aids](../reference/job-aids.md).

## Scenario

The same kind of content, a short document with headings, a list, and a little math or emphasis, arrives in five different formats. Your supervisor asks: *"Which of these is the best source to transcribe from, and what should I check on each?"*

You will answer with evidence, not opinion.

## Before you start

**BrailleBlaster can open all of these file types.** **File > Open** lists the recognized types, including `.docx`, `.odt`, `.md`, `.tex`, and `.epub`. The question is not *whether* they open. It is **what survives**.

Make a prediction table before you open anything. For each format, guess whether headings, lists, emphasis, and math will survive.

| Format | Headings | Lists | Emphasis | Math |
| ------ | -------- | ----- | -------- | ---- |
| Word (`.docx`) | | | | |
| OpenDocument (`.odt`) | | | | |
| Markdown (`.md`) | | | | |
| LaTeX (`.tex`) | | | | |
| EPUB (`.epub`) | | | | |

## Steps

For each file:

1. Open it with **File > Open** (`Ctrl+O`).
2. Look at the **Style View** and **Breadcrumbs** to see what BrailleBlaster recognized.
3. Check the **Braille View** for headings, lists, emphasis, and any math.
4. Fill in an Import Log.
5. Note what you would have to fix by hand.

### Format-specific checks

- **Word:** compare with Lab 1. This file has real styles, so most of the structure should arrive.
- **ODT:** check the same things as Word, and note whether the style names differ.
- **Markdown:** look closely at the **nested list**. List handling is the most common Markdown surprise, and the markup around the list is easy to misread. Check the inline math (`$E = mc^2$`) and the displayed fraction, and note what happened to the **code block**.
- **LaTeX:** the official documentation says LaTeX mathematics is converted to **ASCII Math** when the file opens. Check each equation in the Braille View. Do not assume that LaTeX commands you saw in the source remain visible after import.
- **EPUB:** note how the two chapters arrive, and whether you can navigate between them.

## Expected observations

You should find that:

- Structure survives best where the source *declares* structure (real Word styles, Markdown headings, EPUB chapters).
- Math survives best where it was written as math (LaTeX), and still needs verifying.
- Every format needs at least one human check, and the checks differ from format to format.

Write down any place where your results differ from this list.

## Debrief questions

1. Which format was the best source for this content, and what made it best?
2. Which format needed the most checking, and why?
3. If the same content arrived only as a scanned PDF, what would you ask the sender for instead?
4. Use the **six core principles of importing** from [Lesson 16](../lessons/16-choosing-an-import-workflow.md). Which one did this lab illustrate most clearly?

## Report

Write a half-page recommendation for your supervisor that ranks the formats from best to worst *for this content*, and gives the first three checks for each.
