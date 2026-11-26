# Verification Record

This file records what the curriculum has been checked against, and what has **not** yet been checked. Update it whenever you re-verify a lesson. See `PROFESSIONALIZATION_ROADMAP.md`, item A1.

## What "verified" means here

Two kinds of checking are recorded separately, because they are not the same:

- **Source-verified.** A menu path, label, shortcut, or behavior was confirmed by reading the BrailleBlaster program source code or the official user guide source. This proves the feature *exists and is labeled that way*. It does not prove it behaves as a lesson expects when you click it.
- **Application-verified.** Someone ran BrailleBlaster and followed the lesson. **No lesson has been application-verified yet.**

## Sources used

| Source | Identifier | Date |
| ------ | ---------- | ---- |
| BrailleBlaster program source, `aphtech/brailleblaster` | commit `369176b9402d331be2674c8d4c707c4240ef396b` | 2026-10-19 |
| BrailleBlaster 3.x User Guide source, `aphtech/brailleblaster-docs` | commit `81c1742885a317636bfe2ffef0fda5d491e131b8` | 2026-09-30 |
| BrailleBlaster 2.x User Guide (older web manual) | `brailleblaster.org/docs/manual/manual.php`, read in the first review pass | Not dated |
| eBraille 1.0 specification (DAISY Consortium) | `daisy.github.io/ebraille/published/1.0/` | 2025 |

## Corrections made by checking the source (version 2.2.0)

| Lesson or page | What was wrong | What the source shows |
| -------------- | -------------- | --------------------- |
| 1, glossary, capstone | BBZ named as the default save format | BBX is the default. BBZ is a zipped NIMAS file set |
| 11, 7, Lab 7, Drill F, Job Aid 5, instructor notes | The Contraction Relaxer was described as a per-selection tool using `Ctrl+Shift+T` | The Relaxer is a **document-level**, **cumulative**, **unit-based** dialog with no shortcut. `Ctrl+Shift+T` is Change Translation: Uncontracted |
| 23, 24, capstone, Unit 3 page, shortcuts | TOC Builder, Volume Manager, and T-Page Generator were shown under the Tools menu | In the 3.x source they are in the hidden **Debug** menu (`Ctrl+Shift+` ` toggles it), and the 3.x guide does not document them |
| 19 | No click path for eBraille export | **File > Export > Export to eBraille** exists but only in debug mode. `brailleblaster export ebraille <in> <out>` also works. The package layout was read from the exporter |
| 13, 1, shortcuts | `File > Export > Save BRF/PEF` was changed to `File > Save BRF/PEF` after reading the older guide | The 3.x source has **File > Export > Save BRF/PEF**. The original path was right |
| 1, 4, 18, 26, 31, troubleshooting, README, how-to-use | "Help > Search" and "the Style Appendix under Help" | Neither exists in the 3.x Help menu. The style tables are Appendix A of the User Guide, reached with `F1` |
| Shortcuts | `Alt+1` to `Alt+9` for loadouts, and `Ctrl+Shift+G` called a Relaxer shortcut | Loadouts use `Ctrl+Shift` plus a letter, then `Alt+1` to `Alt+8`. `Ctrl+Shift+G` is the Glossary loadout |
| 1 | Braille Preview had two navigation modes | There are three: print, braille, and ordinal |
| 1 | Menu map omitted Navigate, and listed non-existent items | Rebuilt from the source menu definitions |

## Source-verified items, by lesson

| Lesson | Items confirmed in source or the 3.x guide |
| ------ | ------------------------------------------ |
| 1 | Menu names and shortcuts; BBX and BBZ; three Braille Preview modes; Navigate menu; Debug-menu toggle |
| 4 | Loadout shortcuts; Unwrap Element; Breadcrumbs |
| 11 | Relaxer dialog text, the 13 drop-down choices, and the absence of a shortcut |
| 13 | **File > Export > Save BRF/PEF**; Page Properties defaults; embosser profile fields |
| 19 | eBraille exporter menu, command line, and package layout |
| 20 | **Tools > Production Note Manager**; **Navigate > Book Tree** (`Alt+End`) |
| 23, 24 | Debug-menu placement; Page Number Type (Normal, T-page, P-page) for the manual fallback |
| 25 to 32 | Every procedure was taken from the 3.x User Guide. Menu labels (Insert > Table, Insert > Image Manager, Edit > Set Cell Position, Tools > Line Number Tools, Tools > Spell Check, Help > View Log, Help > About BrailleBlaster) were confirmed in the source |

## Not yet verified (needs the application)

1. **Everything behavioral.** No expected observation in any lab, drill, or answer key has been confirmed by running BrailleBlaster.
2. **Lesson 25:** which type Auto chooses for the sample tables, and the Total Width values.
3. **Lesson 26:** the exact blank-line counts and page-break behavior of each option.
4. **Lesson 27:** the label shown in the dialog title ("Insert Image Placeholder"), and the limit on lines (the guide says fewer than 25; the source ties it to lines per page).
5. **Lesson 31:** how many glossary and index levels the Styles menu offers. The guide documents 1 to 5; the source has more, including definition styles.
6. **Lessons 23 and 24:** whether the Debug-menu tools work in a released build, and how they differ from the 2.x behavior the lessons were written from.
7. **Sample files:** how each imports (see `CURRICULUM_REVIEW.md`).
8. **Released versus development source.** The source checked is the development branch. A released build such as 3.2.1 may differ.

## How to update this file

When you verify a lesson in the application, add a row below with the lesson, the BrailleBlaster version and operating system, the date, and your name or initials, and list anything that differed.

| Lesson | BrailleBlaster version and OS | Date | Verified by | Differences found |
| ------ | ----------------------------- | ---- | ----------- | ----------------- |
|        |                               |      |             |                   |

---

# Handbook verification (version 2.3.0, Lessons 33 to 54)

## Sources and tools used

| Source or tool | Identifier |
| -------------- | ---------- |
| BrailleBlaster conversion script `bbx.lua`, and the Word filters `docx-empty-paragraph.lua` and `docx-page-break.lua` | `aphtech/brailleblaster` commit `369176b9402d331be2674c8d4c707c4240ef396b` |
| Pandoc loader (`PandocArchiverLoader.kt`) and its reader options | the same commit |
| NIMAS mapping file `nimas.parserMap.xml`, the NIMAS zip loader, the BBZ archiver, the text loader, and the eBraille packager | the same commit |
| Pandoc | **3.12.1**, the version the project's `pom.xml` bundles. Downloaded from the Pandoc releases and used for every conversion test |
| poppler-utils, Tesseract 5.3.4, `lxml`, `python-docx`, `reportlab` | Used to generate and test the PDF, XML, and Word examples |

## How "verified" is used for the Handbook

- **Run.** The behavior was produced by running BrailleBlaster's own conversion script on a test file, with Pandoc 3.12.1. These are the strongest results short of the application.
- **Read.** The behavior was read from the source code or a mapping file, and not run.
- **Computed.** A table was generated by a program from stated rules, and its checkable parts were checked.
- **Cited.** The statement comes from a published source named in the lesson.

## Run: conversion behavior (Lessons 33 to 40, 53)

| Behavior | Result |
| -------- | ------ |
| Markdown H1, H2, H3 to H6 | Centered, Cell 5, Cell 7 (all four deeper levels the same) |
| Word Heading 1, 2, 3 and deeper | The same mapping |
| Word **Title** style | Not a heading. Body text |
| Styles named `3-1`, `1-3`, `5-7`, `7-5` (Word and Markdown `custom-style`) | The braille margins named |
| `BB Empty Paragraph` | An empty paragraph |
| **A Markdown line block** | **The conversion fails** with a Lua error |
| **An image alone in its paragraph** (Markdown, Word), a LaTeX `figure`, an HTML `<figure>` | **Dropped with its caption.** An image inside a sentence is kept |
| Strikethrough, subscript, superscript, small caps, inline code | Dropped, literal `_` and `^`, bold, and a split paragraph |
| Footnotes | A `^1` marker and a "Footnotes" section at the end |
| Hard line break, HTML `<br>` | A real line break |
| Word tracked changes, Word equations | Insertions accepted and deletions removed. Math |
| LaTeX `\title`, `\author`, `\maketitle`, YAML metadata | Dropped |
| LaTeX document class | Changes the heading levels. TikZ is silently dropped. `tabular` gains an empty first row |
| `.odt` with a style named `3-1` | Ignored. Pandoc does not support the `styles` option for ODT |
| A proposed fix for the line block and the figure | Tested on all failing cases, and a regression test showed unrelated output **byte-identical** |

## Read: structure (Lessons 38, 39)

The DTBook element map (`nimas.parserMap.xml`), the NIMAS zip loader (`.opf` required, manifest checked), the BBZ layout (`document.bbx` and `bbx_location`), the plain text loader (one paragraph per non-blank line, illegal XML characters removed, form feed splits lines), the eBraille package layout, BrailleBlaster's menu mnemonics, and the Privacy settings tab.

## Computed (Lessons 41, 44, 45)

The 64-cell braille table (the formula, and the letter and digit patterns, were checked), the indicator cards (generated from dot numbers), and the volume estimator (examples run).

## Not yet verified

1. **Everything in the application.** None of the Handbook was run in BrailleBlaster itself. The conversion script is followed by Kotlin fixers, and the application may handle some cases differently from the script alone.
2. **Word, LibreOffice, OpenOffice, and Google Docs shortcuts** (Lessons 35, 36, 44) are standard shortcuts from the vendors' documentation and were **not run** in those programs. Verify them in your version.
3. **The indicator cards** (Lesson 44) give dot numbers for UEB and Nemeth indicators that were **not checked against the code books** here, and have not been reviewed by a certified transcriber. This is the single most important item to have an expert check.
4. **The Braille Formats crosswalk** (Lesson 43) cites only section numbers already used in Lessons 3, 5, 6, 7, and 8. The "where to look" rows have no numbers.
5. **OCRmyPDF options** (Lesson 42) are from its documentation and were not run.
6. **Accessibility** (Lesson 51): only two screen-reader statements come from the guide. The test protocol has not been run by any blind transcriber.
7. **Privacy and legal statements** (Lesson 49 and the policy page) are a summary, not legal advice, and should be reviewed by someone qualified.
8. **Estimator figures and the example agency** in Lessons 45 and 48 are illustrative.
