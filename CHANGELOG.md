# Changelog

All notable changes to this curriculum are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/), and versions follow [Semantic Versioning](https://semver.org/) with this meaning: **major** for a change in structure or lesson numbering, **minor** for new lessons, labs, or reference pages, and **patch** for corrections.

## [2.3.0]

### Added
- **Unit 5: Handbook (supplemental)**, with 22 lessons (33 to 54): what makes a good source; Markdown, Word, LibreOffice and Google Docs; XML, DTBook, NIMAS, and MathML; the inside of DOCX, ODT, EPUB, eBraille, and BBX packages; LaTeX; text encoding and braille characters; PDFs, scans, and OCR; a Braille Formats crosswalk; quick-reference cards; page geometry and volume sizing; image description; a subject-area guide; job intake and the agency style sheet; file management and student privacy; embosser care; an accessible workflow; decision trees; an error gallery; and a model capstone job.
- A Unit 5 page with a placement table, and Unit 5 teaching notes.
- **`UPSTREAM_ISSUES.md`**, eight findings to report to the BrailleBlaster project, with a reproducible test set (`upstream-test-cases.zip`) and tested fixes for the two most serious.
- New sample files: `markdown-syntax-tour.md`, `line-block-test.md`, `word-05-braille-aware-styles.docx`, and `upstream-test-cases.zip`.
- Job Aids 10 to 13: the intake ticket, the agency style sheet, the embosser maintenance log, and the accessibility test log.
- Glossary terms, resources, and a section in the Pandoc Cookbook on previewing BrailleBlaster's own conversion.
- A "Handbook" note at the top of the lessons it supports.

### Changed
- `VERIFICATION.md` now separates what was run, read, computed, and cited, and lists what is not yet verified.
- The quality checker ignores Markdown examples inside code blocks when it checks links.
- **Capstone:** corrected "four print levels" to three, removed a duplicated heading, and linked the model walkthrough.
- **Lessons 1 and 4:** noted that a screen reader announces every Breadcrumbs change, and how to turn them off.
- The Pandoc Cookbook now uses `--math-method=mathml` and says that BrailleBlaster bundles its own Pandoc.

### Removed
- Orphaned files from the earlier structure (`BrailleBlaster/`, `Backmatter/`, `Contributors.md`, `indexing.md`), which had returned.

## [2.2.0]

### Added
- **Unit 4: Specialized Content**, with eight new lessons: 25 Tables, 26 Controlling the Page with Style Options, 27 Images and Tactile Graphics, 28 Editing the Translation, 29 UEB Technical Material and Other Codes, 30 Line Numbers, 31 Glossaries and Indexes, and 32 Proofreading and Quality Assurance (with a seeded-error exercise).
- Unit 4 page with a checkpoint and a table of where to teach each lesson, Unit 4 teaching notes, and a Proofreading Error Log job aid.
- `VERIFICATION.md`, recording what was checked against the BrailleBlaster source and what is still unverified.
- A manual fallback method for transcriber-generated pages and the table of contents (Lessons 23 and 24).
- Lesson 19: how to reach the eBraille exporter, the command-line `export` command, and the package layout.

### Changed
- **Lesson 11, Lab 7, Drill F, Job Aid 5, and instructor notes:** the Contraction Relaxer is a document-level, cumulative, unit-based tool with no shortcut. `Ctrl+Shift+T` and `Ctrl+D` belong to Change Translation.
- **Lessons 23 and 24, capstone, Unit 3 page:** the TOC Builder, Volume Manager, and T-Page Generator are in the hidden Debug menu in the current 3.x source. Each lesson now says how to find them.
- **Shortcuts page:** rebuilt from Appendix B of the 3.x User Guide, including style loadouts.
- **Lesson 1:** menu map rebuilt from the source, with the Debug menu and the correct Help menu items.
- **Lesson 20:** added the Production Note Manager and Book Tree paths.
- **Lesson 7:** points to Lesson 29 for UEB Technical Material.
- `File > Export > Save BRF/PEF` restored as the correct path.
- The quality checker now also rejects the corrected mistakes listed above.

### Fixed
- Removed references to a **Help > Search** menu item and a **Style Appendix** in the Help menu, which do not exist in 3.x.

## [2.1.0]

### Added
- **Labs 1 to 9** that use real files, with a Labs overview page.
- **Sample Files** page and a generator (`tools/build_samples.py`) that builds Word, ODT, EPUB, LaTeX, Markdown, HTML, NIMAS-style, and plain-text practice files.
- **Practice Drill Bank** with answer keys.
- **Job Aids**: style map, import log, embosser profile log, page numbering plan, relaxation plan, volume plan, production checklist, and production log.
- **Pandoc Cookbook** and **Policy and Standards Background**.
- Instructor Guide: strategy, pitfalls, practice tiers, and companion practice for all 24 lessons, plus twelve **Session Plans**.
- `tools/check_book.py` and a CI workflow that runs it.
- `PROFESSIONALIZATION_ROADMAP.md`, `CONTRIBUTING.md`, `CITATION.cff`, and issue and pull-request templates.
- Practice callouts in lessons that link to labs, drills, and samples.
- Source Citations for Lessons 2, 10, 12, 13, and 20.

### Changed
- **Lesson 1:** the default save format is BBX (BBZ is a zipped NIMAS file set); added the Navigate menu, the three Braille Preview navigation modes, toolbar and icon options, and the list of supported file types.
- **Lesson 23:** added the Volume Manager (Smart Volumes) and TOC Builder workflow from the official guide.
- **Lesson 24:** added the guidance to generate T-pages last and to edit them only inside the generator, and described the four tabs.
- **Capstone:** the deliverable is a `.bbx` file, and volume breaks use the Volume Manager.
- **Shortcuts, Glossary, Lesson 13:** the BRF/PEF save path is **File > Save BRF/PEF** (under **File > Export** in some releases).

### Removed
- Orphaned files from the earlier structure (`BrailleBlaster/`, `Backmatter/`, `Contributors.md`, `indexing.md`).

## [2.0.0]

### Changed
- Restructured the repository from an OpenSCAD course scaffold into a BrailleBlaster curriculum with 24 lessons in three units, a capstone, an Instructor Guide, and a reference section. See `CURRICULUM_REVIEW.md`.
