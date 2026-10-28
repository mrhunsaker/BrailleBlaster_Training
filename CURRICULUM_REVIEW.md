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
