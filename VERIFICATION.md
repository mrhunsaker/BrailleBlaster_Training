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
