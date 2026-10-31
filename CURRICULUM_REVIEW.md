# Curriculum Review Notes

Editorial notes from the restructuring of this repository into a finished mdBook curriculum. Read this before publishing.

## 1. What the repository was

The repository was an mdBook scaffold copied from the OpenSCAD/3DMake course. The root README, `book.toml` (preprocessors), the book introduction, the Contributors page, `.gitmodules`, and `.gitignore` still described 3D printing. The book itself had 19 practice lessons, three **empty** section pages (Universal, Advanced, Transcriber-Focused), an empty GUI lesson, an empty eBraille lesson, an empty Backmatter, and a blank index. The four files in `AddlFiles/` held trainer material that was not in the book.

## 2. What was done

- **Replaced** the introduction, Contributors page, root README, `book.toml`, and `SUMMARY.md`.
- **Wrote new:** Lesson 1 (Interface), Lesson 4 (Layout Styles), Lesson 19 (eBraille), the capstone, three unit pages with checkpoints, setup, how-to-use, syllabus and pacing plans, the Instructor Guide (index, three teaching-note pages, assessment), shortcuts, glossary, troubleshooting, and resources.
- **Standardized every lesson:** "Lesson at a glance" (unit, time, prerequisites), learning objectives, "Why this matters," "Step by step" (from the Manual), "Key takeaways," and one H1 per file.
- **Split the 1,115-line import lesson** into Lessons 14, 15, and 16, and demoted its multiple H1s.
- **Fixed Lesson 24** (multiple H1s; leftover "requested 3a, 3b, 3c" wording).
- **Reordered** lessons into a teaching sequence and renumbered (see the map below).
- **Fixed** the `BASHSOURCE` typo in `mdbook_generate.sh` (it should be `BASH_SOURCE`), a few typos in the lessons, and two stale cross-references ("companion chapter").
- **Removed** `.gitmodules` and the OpenSCAD `.gitignore` entries.

## 3. Lesson map (old to new)

| New | Title | Source |
| --- | ----- | ------ |
| 1 | Interface | New (user guide) |
| 2 | Word documents | Practice 07 + Manual ch. 5 |
| 3 | Typeface emphasis | Practice 03 + Manual ch. 1 |
| 4 | Layout styles | New, from Manual ch. 2 |
| 5 | Heading levels | Practice 01 |
| 6 | Lists | Practice 02 |
| 7 | Math toggle | Practice 04 + Manual ch. 3 |
| 8 | ASCII Math Hub | Practice 05 + Manual ch. 4 |
| 9 | Spatial Math Editor | Practice 09 + Manual ch. 7 |
| 10 | Number lines | Practice 10 + Manual ch. 8 |
| 11 | Contraction Relaxer | Practice 06 + Manual ch. 16 |
| 12 | Find and Replace | Practice 11 + Manual ch. 9 |
| 13 | Paper size and embossers | Practice 08 + Manual ch. 6 and 14 |
| 14 to 16 | Importing formats | Practice 13, split in three, + Manual ch. 12 |
| 17 | Pandoc | Practice 16 + Manual ch. 17 |
| 18 | Advanced formatting | Practice 15 + Manual ch. 15 |
| 19 | eBraille | New, from Manual ch. 10 and the DAISY spec |
| 20 | NIMAS | Practice 12 + Manual ch. 11 |
| 21 | Running heads and page numbers | Practice 14 + Manual ch. 13 |
| 22 | Transcriber's Notes | Practice 17 |
| 23 | TOC and volumes | Practice 18 |
| 24 | T-Page Generator | Practice 19 |

## 4. Factual problems found in the drafts

**These matter most.** The `AddlFiles/BrailleBlaster_Comprehensive_Training_Guide.md` contradicts the Manual, the practice lessons, and published sources in several places. I used only its teaching approach.

| Topic | Comprehensive Guide says | Verified / used instead |
| ----- | ------------------------ | ----------------------- |
| **eBraille** | An "XML schema" with `.brf` or `.xml` files; BrailleBlaster is "proprietary"; tools "Braille2000" | A DAISY Consortium standard (1.0, August 2025), EPUB 3-compatible, packaged as **`.ebrl`**. BrailleBlaster is GPL3 open source since 3.0.0 |
| Contraction Relaxer shortcut | `Ctrl+Shift+G` | `Ctrl+Shift+T` (Manual and Lesson 11) |
| Running head menu | **Tools > Running Heads** | **Insert > Running Head** (Manual and Lesson 21) |
| Spatial Math Editor | A "canvas, grid, properties panel" WYSIWYG tool | Containers: Number Line Editor, Matrix, Math Templates, Regular Text (Lesson 9) |
| Find and Replace | Regular expressions, `^p` and `^t` codes | Not mentioned in the lessons or the Manual. The codes look like Word syntax. Not used |
| NIMAS "time savings (50-80%)" and similar statistics | Stated as fact | Unsupported by any source. Not used |

The **Demonstration Materials** and **Hands-On Supplement** use Markdown markers such as `**bold**` and `~~~` as "paste into BrailleBlaster" text. Pasted, those characters would appear literally. They were not used. Its eBraille demo also assumes an XML structure (`<bold>`, `<list>`) that the real format does not use.

## 5. Please verify in the application

I could not run BrailleBlaster, so these items come from documentation and your drafts rather than from testing. Please confirm each in your installed version:

1. **Lesson 1:** `Alt+Home` for Braille Preview and `Alt+P` for Print View; the **View > Toggle Views > Breadcrumbs** path; whether text can be typed into the Braille View in 3.x; the menu list under "A map of the menus."
2. **Lesson 13:** **File > Export > Save BRF/PEF**.
3. **Lesson 19:** whether your version has an eBraille export, and where. The lesson deliberately makes no click-path claim.
4. **Lesson 4:** that Box styles are named as I described, and what the Breadcrumbs entries look like.
5. **Shortcuts page:** the full table was taken from the Manual's appendix.
6. **Setup page:** the Windows, macOS, and Linux support statement, and the claim that installed versions update automatically while zip/tar do not (from the 3.2.1 announcement).
7. **Time estimates:** most come from the Guide's teaching times, trimmed. Lessons 1, 5, 6, 22, 23, and 24 are my estimates. Adjust after piloting.

## 6. Decisions you may want to reverse

- **The index preprocessor was removed.** `book.toml` listed `[preprocessor.index]` and `[preprocessor.indexing]`, and the lessons contain no index markers. The old CI installed `mdbook-indexing`, but `[preprocessor.index]` is a different tool, so the build would likely have failed. To restore an index, add the preprocessor back, mark terms with `{{hi:term}}`, and restore the `cargo install mdbook-indexing` line in both workflows.
- **`AddlFiles/` was kept**, with a README explaining each file's status. You could remove it, or move it to a separate branch, once you are happy with the book.
- **`create-missing` is now false**, so a missing file in `SUMMARY.md` fails the build instead of silently creating an empty page. That is how the three empty section pages went unnoticed.
- **Lesson 15 still contains a NIMAS section** that overlaps Lesson 20. I kept it so the six-format comparison stays complete, and cross-linked it.
- **Capstone source text** is original and uses the same plain-text markup key as Lesson 3. Review it for your students' reading level.

## 7. Suggested next steps

1. Add screen reader and braille display notes to the how-to-use page and Lesson 1. This is your area of expertise, and I deliberately made no claims about specific assistive technology.
2. Pilot Unit 1 with a few learners and adjust the time estimates.
3. Add an answer-key walkthrough for the capstone for instructors.
4. Consider adding screenshots with alt text for the menu-heavy lessons (1, 4, 13, 21, 24), or short descriptions of each dialog.
5. Re-check every menu path when a new BrailleBlaster release ships.


---

# Second pass (version 2.1.0): using the AddlFiles and checking against the official guide

## What the four AddlFiles contributed

| File | Used for | Not used, and why |
| ---- | -------- | ----------------- |
| **Demonstration Materials** | The *content* of the demos became real files: four Word documents, an ODT, an EPUB, LaTeX, Markdown, HTML, a NIMAS-style set, and plain-text sources (see `tools/build_samples.py`). Their scenarios became Labs 1 to 9 | The trainer scripts. Several contain menu paths and numbers that are wrong (below) |
| **Hands-On Practice Guide** | The 29 snippets became the **Drill Bank** with answer keys. Its four-session flow became Sessions 1 to 4 | The snippets had no answers, and two (a Shakespeare block quote, and a list that was really a sentence) needed redesign. I replaced the quotation with original text |
| **Comprehensive Training Guide** | Per-topic teaching strategy, pitfalls, advanced points, three-tier practice design, and assessment ideas, vetted and rewritten into the Instructor Guide. The Three-Pass Method, the "Print is for eyes, Emboss is for fingers" line, profile naming and maintenance, and the relaxation-plan passes | Its UI claims and its eBraille section |
| **Training Manual** | Already used in version 2.0 | |

## New errors found in the drafts

The official User Guide (brailleblaster.org/docs/manual/manual.php) was read in full and used as the arbiter.

| Draft statement | What the official guide says |
| --------------- | ---------------------------- |
| Demonstration Materials: BrailleBlaster "cannot open `.tex` files" and needs Pandoc first | `.tex` is a supported file type. LaTeX is converted to ASCII Math on open. The fallback is converting to HTML with another tool, and renaming `.xht` to `.xhtml` |
| Demonstration Materials: a "sample NIMAS XML" made of an OPF file and XHTML | That is EPUB-style. NIMAS is DTBook XML with an OPF package file. The new `sample-dtbook.xml` follows DTBook |
| Demonstration Materials: a 1.25 inch margin is "approximately 10 cells" | A braille cell is about a quarter of an inch, so that margin is about five cells. The new test page makes no such claim |
| Demonstration Materials and Comprehensive Guide: different running heads for different chapters or page types | The Running Head tool sets **one** title for the document, shown on every braille page except t1 and braille page 1 |
| Comprehensive Guide: Find and Replace regular expressions, `^p` and `^t` | Not in the official guide |
| Comprehensive Guide: Spatial Number Lines as "Line Template, Arrow Tools, Labeling" | The guide describes the Number Line Editor with settings such as Reduce Fraction, Beveled Fraction, Add Arrows to Line, Stretch Across Page, Remove Leading Zeros, Math Entry versus User Text, and Points versus Interval. The Instructor Guide now teaches those |
| Comprehensive Guide: "increase style levels from 5 to 8 for deep lists" | The default is five and the maximum is eight, so a four-level list needs no change |
| Comprehensive Guide: BrailleBlaster is "proprietary" | It is GPL-licensed open source |

## Errors in version 2.0 of *this* book, now corrected

1. **Default save format.** Lesson 1, the Glossary, and the Capstone said BBZ. The official guide says **BBX** is the default, and BBZ is a zipped NIMAS file set. (The error came from the Training Manual's glossary, so it should be fixed there as well.)
2. **BRF/PEF save path.** The official guide says **File > Save BRF/PEF**, while the lessons said **File > Export > Save BRF/PEF**. The book now gives both, with a note that releases differ. Verify in your version (see the roadmap, item A1).
3. **Volumes.** Lesson 23 treated "End of Volume markers" as typed text. The real mechanism is **Tools > Volume Manager**, which also feeds the TOC Builder and T-Page Generator. The lesson now explains it and keeps the plain-text markers as stand-ins.
4. **T-Page Generator.** Lesson 24 lacked two cautions from the official guide: generate T-pages last, and edit them only inside the generator, because edits made in the Print View are lost when the generator reopens.
5. **Braille Preview.** Lesson 1 mentioned two navigation modes. There are three (print, braille, and ordinal page).
6. **Navigate menu.** Lesson 1's menu map left out the Navigate menu (Home, End, Go To Page, Previous Element, Next Element).
7. **A formatting defect.** Lesson 13 still had an unconverted `File →` arrow. The new checker found it.

## Structural problems the checker now prevents

Orphan pages that are not in `SUMMARY.md`, missing or duplicate top-level headings, broken links and anchors, lessons without a glance block or objectives, missing sample files, and known-bad statements from the older drafts.

## Things still to verify in the application

Everything in the roadmap's item A1, plus:

- How the four Word files import. Do the Word character styles *Emphasis* and *Strong* behave differently from direct bold and italic in the flat file?
- Whether `sample-dtbook.xml` opens, how the `sidebar`, `prodnote`, and MathML elements arrive, and whether the missing image reference causes a warning.
- What Lab 3's Pandoc-generated HTML does with the raw `equation*` block.
- Whether a `File > Open` of the zip files works as the labs assume.

Please send any differences back as issues, using the content-error template.


---

# Third pass (version 2.2.0): the rest of the lessons, and the source code

## What was done

The remaining lessons from the roadmap were written as **Unit 4: Specialized Content** (Lessons 25 to 32). To do this reliably, the BrailleBlaster 3.x **program source** and the **3.x User Guide source** were read directly, instead of relying on the older web manual or on the earlier drafts. That turned up errors in this book that earlier passes had missed. `VERIFICATION.md` records what was checked.

## Errors found in this book by reading the source

| What I had written | What the source shows | Where fixed |
| ------------------ | --------------------- | ----------- |
| The Contraction Relaxer works on a selection and uses `Ctrl+Shift+T` | It is a document-level dialog. You pick a teaching unit, and contractions up to and including that unit are allowed. It has no shortcut. `Ctrl+Shift+T` belongs to Change Translation | Lesson 11, Lab 7, Drill F, Job Aid 5, instructor notes, shortcuts |
| The TOC Builder, Volume Manager, and T-Page Generator are on the Tools menu | In the 3.x source they are in the hidden Debug menu, and the guide does not document them | Lessons 23 and 24, capstone, Unit 3 page, shortcuts, Lesson 1 |
| "Use Help > Search" and "the Style Appendix under Help" | Neither exists. The Help menu has Check For Updates, View log, Website, User Guide (`F1`), About, Privacy, and Reset BB | Eight places |
| Loadouts use `Alt+1` to `Alt+9` | `Ctrl+Shift` plus a letter chooses a loadout, then `Alt+1` to `Alt+8` | Shortcuts, Lesson 4 |
| `File > Save BRF/PEF` (changed in version 2.1) | The source has `File > Export > Save BRF/PEF`. The original wording was right | Lessons 1 and 13, shortcuts |
| Lesson 19 had no click path | `File > Export > Export to eBraille` exists in debug mode, and a command line route exists | Lesson 19 |

Note that **three of these were caused by me trusting the older 2.x web manual** over the lessons the author had written. The lessons were often closer to the truth.

## New material

- Lessons 25 to 32, a Unit 4 page with a placement table, Unit 4 teaching notes, and a Proofreading Error Log.
- A manual fallback for T-pages and TOCs, in case the Debug tools are unavailable.
- A shortcuts page rebuilt from Appendix B of the 3.x guide.
- A quality checker that now rejects the mistakes above.

## Decisions you may want to reverse

- **Lessons 23 and 24 were kept**, with prominent notices, and not removed. The concepts are essential to professional braille production, and the 2.x guide documents the tools as normal. If APH confirms the Debug tools are not meant for general use, rewrite these two lessons around the manual method.
- **Unit 4 uses numbers 25 to 32** so existing lesson numbers and links did not change. If you would rather fold the lessons into the earlier units, the placement table on the Unit 4 page shows where each belongs, but every lesson number after the insertion point would change.
- **Lesson 29 stays at the level of settings and tools.** It does not teach UEB Technical or Nemeth rules, which belong to their own manuals.
- **No lesson on multi-transcriber workflows.** The 3.x guide does not document dividing a NIMAS file, so there was nothing reliable to teach.

## Still to verify in the application

See the list in `VERIFICATION.md`. The most important item is that **no lesson has been run in BrailleBlaster**. The source tells us a feature exists and what it is called. Only running it tells us what it does.
