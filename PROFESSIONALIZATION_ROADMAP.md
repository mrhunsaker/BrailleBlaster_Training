# Professionalization Roadmap

What this curriculum needs, beyond its current content, to be used confidently by agencies, districts, and training programs. Items are grouped by priority and sized small (S, about a day), medium (M, about a week), or large (L, a month or more of part-time work).

## Where the curriculum stands

**Strong now:**

- 24 lessons with objectives, practice documents, answer keys, and citations to *Braille Formats 2016*
- Nine labs and a drill bank that use real sample files
- An Instructor Guide with strategy, pitfalls, practice tiers, and session plans
- A capstone with a rubric, printable job aids, and automated link and structure checks

**Not yet professional-grade:**

- **No in-application verification.** Menu paths come from documentation and drafts. Two errors found this session (the default save format, and the volume workflow) show this risk is real.
- **No learner testing.** Time estimates, difficulty, and answer keys have never met real learners.
- **No subject-matter expert review** by a certified transcriber, which is the single most credible quality signal.
- **Large feature areas are missing** (Tables, glossaries and indexes, tactile graphics, page-control options). See Priority B.
- **No formal assessment beyond one capstone.**
- **Accessibility of the book itself is unverified.** For a braille curriculum this matters more than for most.

## Priority table

| # | Item | Priority | Size |
| - | ---- | -------- | ---- |
| A1 | In-application verification pass, with a version stamp on every lesson | Must | M |
| A2 | Subject-matter expert review (BANA, UEB, Nemeth) | Must | M |
| A3 | Pilot with real learners and revise | Must | L |
| A4 | Accessibility audit and screen reader testing of the site | Must | M |
| B1 | Lesson: Tables | **Done (Lesson 25)** | M |
| B2 | Lesson: Page control and style options | **Done (Lesson 26)** | M |
| B3 | Lesson: Glossaries, indexes, and guide words | **Done, except the experimental guide-word tools (Lesson 31)** | M |
| B4 | Lesson: Tactile graphics and image placeholders | **Done (Lesson 27).** The Image Describer is not documented in 3.x | M |
| B5 | Lesson: Editing the translation | **Done (Lesson 28)** | S |
| B6 | Lesson: Proofreading and quality assurance | **Done (Lesson 32)** | M |
| B7 | Lesson: UEB technical, numeric passages, and other codes | **Done (Lesson 29)** | M |
| B8 | Lesson: Multi-transcriber workflows | **Withdrawn.** Dividing a NIMAS file is not in the 3.x guide | S |
| C1 | Pre-assessment and post-assessment | High | M |
| C2 | Per-unit performance tasks with rubrics | High | M |
| C3 | Quiz item bank with answer rationales | Medium | M |
| C4 | Competency map to external standards | Medium | M |
| C5 | Completion criteria and a certificate | Medium | S |
| D1 | Screenshots with alt text, or captioned and described video | High | L |
| D2 | Instructor slide decks and facilitator scripts | Medium | L |
| D3 | Learner workbook (printable) | Medium | M |
| D4 | Learner prerequisites diagnostic | Medium | S |
| E1 | A braille edition of the curriculum itself | High | M |
| E2 | Accessible PDF and EPUB editions | Medium | M |
| F1 | Choose and apply a content license; third-party permissions | Must | S |
| G1 | Verification log, changelog, and a release process | High | S |
| G2 | Contribution and review workflow | Medium | S |
| G3 | Automated watch for new BrailleBlaster releases | Medium | S |
| H1 | LMS packaging | Low | M |
| I1 | Evaluation plan and evidence collection | Medium | M |

---

## A. Accuracy and trust (do these first)

### A1. In-application verification pass (M)

Sit down with the version of BrailleBlaster your learners will use and work through **every lesson and lab exactly as written**. For each, record:

- the BrailleBlaster version and operating system;
- each menu path and shortcut that was correct, wrong, or different;
- each expected observation that did not occur.

Then add a one-line stamp at the top of each lesson, for example *Verified with BrailleBlaster 3.2.1 on Windows 11, 2026-11-15.* The lessons then tell users how current they are, and a release-watching process (G3) tells you when a stamp has gone stale.

**Known items to check first:**

1. ~~Where **Save BRF/PEF** lives.~~ *Confirmed in the source: **File > Export > Save BRF/PEF**.*
2. Whether the Braille View is editable in 3.x.
3. The names of the Box and Block styles, and what Breadcrumbs entries look like.
4. ~~Whether any eBraille export exists.~~ *It exists, in debug mode. Check that it works in your build.*
5. How BrailleBlaster handles Word character styles versus direct formatting (the Sample Files page sets up this comparison).
6. How the `sample-dtbook.xml` NIMAS-style set imports, because it was never opened in the application.
7. Every number in the setup and Lesson 13 sections (page defaults, paper sizes).

### A2. Subject-matter expert review (M)

Ask one or two certified literary and Nemeth transcribers, and a TVI who is not the author, to review the **content**, not the formatting. Give them the answer keys and ask: "Would you sign your name to this?" Pay them, and credit them in the acknowledgements with their permission. Keep a record of their comments and your responses.

### A3. Pilot with real learners (L)

Run Unit 1 with five to ten learners from your target audience. Collect: time on each lesson, errors on each practice, questions asked, and where they stopped following. Revise the lessons that took far longer than their estimate or that produced the same wrong answer repeatedly. Do the same for the capstone, using a second scorer to check the rubric.

### A4. Accessibility audit of the book (M)

See Priority E. This item is listed under "trust" because a braille curriculum that is hard to use with a screen reader or braille display will lose credibility immediately.

---

## B. Content gaps against what BrailleBlaster actually does

> **Status (version 2.2.0):** most of the gaps below are now written as Unit 4 (Lessons 25 to 32). The table is kept so you can see where each lesson came from. Two items remain open: the experimental guide-word tools and multi-transcriber workflows.

The official User Guide documents these feature areas. None has a lesson yet. They are listed in the order we recommend writing them.

| Guide section | Why it matters | Proposed lesson | Unit |
| ------------- | -------------- | --------------- | ---- |
| **Working with Tables** (Insert > Table, Convert Text to Table, the Table Editor, Auto, Simple, Listed, Stairstep, and Linear table types, Reformat Table) | Tables are everywhere in textbooks and are among the hardest transcription tasks. This is the largest gap | **Tables** | 2 |
| **Style Options** (Set Cell Position, Line Break, Don't Split, Keep With Next, Lines Before and After, Double Spaced, Skip Number Lines, Page Side, New Pages Before and After) | These control page breaks, facing pages in interpoint work, and blank pages | **Controlling the Page** | 2 |
| **Alphabetic References** (glossary and index selection, guide words, alphabetic divisions, term and definition spacing, glossaries with pronunciation) | Required for most textbooks | **Glossaries and Indexes** | 3 |
| **Tactile Graphics** and the **Image Describer** (Image Placeholder, attaching images, ViewPlus support) | Images are inevitable, and so are decisions about them | **Images and Tactile Graphics** | 3 |
| **Modifying the Braille Translation** (spell check, entering braille directly, Change Translation, Correct Braille Translation) | The escape hatch when the translator gets it wrong | **Editing the Translation** | 2 |
| **Smart Volumes** in depth (types, Change Volume Type, Delete, saving individual volumes) | Partly covered in Lesson 23 now | Expand Lesson 23 | 3 |
| **Line Numbering** (Wrap Prose, increment, Edit Line Number) | Prose and poetry for literature courses | Add to Lesson 18 | 2 |
| **Making Math**: numeric passages, numeric series, UEB technical material, and Math Help | Lesson 7 centers on Nemeth in UEB contexts | **UEB Technical Math** | 2 |
| **Translation Settings** (UEB, Nemeth, EBAE, US Spanish, Cherokee) | Needed for any non-default code | Add to Lesson 13 or a new setup lesson | 1 |
| **Style Loadouts** (Styles > Configure > Loadouts, Alt plus number) | A real speed gain, now only mentioned | Add to Lesson 4 | 1 |
| **Dividing a NIMAS file** among transcribers and rejoining | Production-team work | **Multi-Transcriber Workflows** | 3 |
| **Help and reporting issues** | Learners need to know how to get help and report bugs | Add to Lesson 1 and Resources | 1 |

Beyond BrailleBlaster itself, a professional curriculum also needs:

- **B6. Proofreading and quality assurance.** How to proofread braille from a BRF and from the Braille View, how to read for errors rather than meaning, what a second-reader pass looks like, and how to keep an errata log. BrailleZephyr (the free BRF editor the guide mentions) fits here.
- **Source preparation.** How to ask a publisher or teacher for a better source file, and how to request NIMAS files.
- **Working with a braille reader.** Getting feedback from the student who will use the product, which no software lesson can replace.

---

### New items found in the source (added in 2.2.0)

Reading the BrailleBlaster source and the 3.x guide turned up items that the earlier roadmap could not have known:

- **Ask APH about the Debug-menu tools.** The TOC Builder, T-Page Generator, Volume Manager, Alphabetic Reference tools, and eBraille exporter are in a hidden Debug menu in the current 3.x source, and the 3.x guide does not document them. Ask APH whether these are meant for general use, whether they will be documented, and how they should be taught. The answer decides whether Lessons 23, 24, and 31 stay as they are or are rewritten. This is the most important open question in the curriculum.
- **A command-line lesson (S).** `brailleblaster export brf|pef|ebraille <input> <output>` converts files without opening the program, with `--braille-profile` to choose settings. It could anchor a short lesson on batch production. Verify the program name for each operating system.
- **Documentation gaps to report to APH.** The 3.x guide still calls the Insert menu item "Image Placeholder" where the program says "Image Manager," and refers to a "Configuring Style Loadouts" section that does not appear.
- **Translation profiles.** The command line mentions a braille profile option, and the translation settings offer several codes. A short lesson on choosing and documenting profiles for an agency would help.

## C. Assessment and credentialing

**C1. Pre- and post-assessment (M).** A short, scored task set (about 45 minutes) that you give before and after the course. It is the cheapest way to show the course works, and it tells learners where to start. Include both knowledge items and a small performance task.

**C2. Per-unit performance tasks (M).** The unit checkpoints are descriptive now. Turn each into a scored task with a rubric, like the capstone's, and calibrate the rubrics by having two people score the same samples.

**C3. Quiz item bank (M).** Write 8 to 10 selected-response items per lesson, each with a rationale for the right answer and for each wrong one. Tag every item with its objective. This enables auto-scored practice in an LMS, and shows which objectives are weakly assessed.

**C4. Competency map (M).** Build a table that maps each course outcome to external frameworks, so a district or agency can see what the course covers. Candidates include state TVI competencies, the content outlines for transcriber certification exams, and the BANA documents. **Verify each framework's current name and content with its owner before publishing the map.**

**C5. Completion criteria and a certificate (S).** State exactly what earns a certificate of completion (for example: all unit checkpoints at "Meets," and a capstone score of at least 28 out of 40 with no row below 2). A certificate of *completion* says what a learner did. Do not call it a *certification* unless an independent body awards it.

**If you plan to offer continuing education credit**, ask the relevant state agency or professional body what a provider must document. Typical requirements include learning objectives, contact hours, an instructor biography, attendance records, a learner evaluation, and a certificate. The course already has objectives and time estimates, so most of the remaining work is administrative.

---

## D. Instructional design

- **D1. Visuals (L).** The lessons describe screens in words. Add either annotated screenshots **with alt text**, or short captioned and audio-described screen recordings. Screenshots of BrailleBlaster are the highest-value addition for learners who see. Descriptions are the highest-value addition for learners who do not. Provide both.
- **D2. Instructor materials (L).** Slide decks, facilitator scripts, a printable answer key set, and a short "first day" checklist. Slides must have accessible structure and speaker notes.
- **D3. Learner workbook (M).** A printable or braille-ready workbook with the practice documents, the job aids, and blank logs, so learners do not have to copy from a web page.
- **D4. Prerequisite diagnostic (S).** Ten items that check UEB fluency and basic computer skills. Tell learners honestly when they should take a UEB course first.
- **D5. Spaced review.** Add a short "retrieval practice" box to later lessons that revisits earlier ones (for example, Lesson 21 asks one question from Lesson 5). Cheap, and well supported by research on learning.
- **D6. Learner paths.** Publish three explicit paths (classroom TVI, production transcriber, instructor) with the lessons, labs, and time for each, instead of leaving the choice to the reader.

---

## E. Accessibility and formats of the book

**E1. A braille edition of the curriculum (M).** Transcribe the curriculum itself with BrailleBlaster. It proves the workflow works, gives braille-reading learners a native copy, and makes a powerful capstone-quality example for the course. It will also find formatting problems in the manuscript, such as tables that do not transcribe well.

**E2. Accessibility audit (M).** Audit the generated site against **WCAG 2.1 AA** (or 2.2). Check:

- color contrast in the **Rust** and **Navy** themes and in code blocks and callouts;
- keyboard navigation, focus order, and a skip-to-content link;
- heading structure on every page, which the checker already enforces;
- table headers, because many tables here are used for layout of reference data;
- language attributes, and that no meaning depends on color alone;
- the search box and the copy-to-clipboard buttons with a screen reader.

Test with at least two screen readers (for example NVDA with a browser, and VoiceOver) **and a refreshable braille display**, and have blind testers do it, not only sighted people with screen-reader emulation. Publish an **accessibility statement** with a feedback address.

**E3. Alternate formats (M).** Produce accessible PDF and EPUB editions per unit. Make sure every file in the Sample Files pack has a plain-text equivalent where possible.

---

## F. Legal and licensing

- **F1. License (S).** The repository is under the Apache License 2.0, which is designed for software. Curricula more often use a Creative Commons license (CC BY or CC BY-SA 4.0 are common) so that others may adapt and share with attribution. Decide, perhaps with advice from your institution, and say so in the README. Keep the generator scripts under Apache 2.0 if you like. A split license is common.
- **Third-party material.** Confirm permissions for any quotations from or close paraphrases of *Braille Formats 2016* and the BrailleBlaster documentation, or reduce them to citations and links. Credit APH and BANA, and keep the "not an official APH publication" notice. If you add screenshots of BrailleBlaster, check APH's terms for documentation and branding.
- **Sample content.** Every sample file is original or generated. Keep it that way, or record the source and license of anything you add.
- **Privacy.** If you add analytics, a feedback form, or an LMS, write a short privacy notice. The static site collects nothing now.

---

## G. Maintenance and governance

- **G1. Verification log, changelog, release process (S).** `CHANGELOG.md` is started. Add a `VERIFICATION.md` table (lesson, BrailleBlaster version, date, verifier). Tag each release and archive it (for example with Zenodo, for a citable DOI). `CITATION.cff` is started.
- **G2. Contribution workflow (S).** `CONTRIBUTING.md`, an issue template for content errors, and a pull-request template are started. Add a rule that any change to a menu path or shortcut needs a stated version and verifier.
- **G3. Release watching (S).** A scheduled GitHub Action that checks the BrailleBlaster releases page and opens an issue when a new version appears, titled "Re-verify the curriculum against BrailleBlaster X.Y.Z."
- **External link checking (S).** Add a scheduled link checker for outside URLs. The current checker covers only internal links.
- **Ownership.** Name a maintainer and a back-up, a response time for error reports, and where the community asks questions.

---

## H. Delivery

- **H1. LMS packaging (M).** If districts or universities will adopt this, provide a Common Cartridge or SCORM-ready export, or a Moodle or Canvas course shell that links to the book and holds the quizzes and rubrics from C. Check accessibility again afterward, since LMS wrappers often add barriers.
- **Answer-key security.** The answer keys are public in the book. That is right for self-learners. For a graded course, publish a second, instructor-only edition without answers, or move the keys to a protected area.

---

## I. Evaluation and evidence

Plan how you will know the course works.

1. **Reaction.** A short end-of-session survey: clarity, pace, relevance, and what to change.
2. **Learning.** Pre- and post-assessment scores (C1) and capstone rubric scores.
3. **Behavior.** A follow-up three months later: "What have you transcribed since the course, and what went wrong?"
4. **Results.** For an agency, error rates or turnaround time on real jobs, if they are tracked.

Even a small pilot with a clean write-up gives you something to cite when you seek adoption or funding.

---

## Suggested sequence

**First 30 days:** A1 (verification pass), F1 (license decision), G1 and G2 (finish the scaffolding), A2 (recruit an expert reviewer).
**Days 30 to 60:** A3 (pilot Unit 1), B1 (Tables), B2 (Page control), C1 (pre- and post-assessment).
**Days 60 to 90:** E2 (accessibility audit), B3 to B6, C2 (unit tasks), E1 (braille edition).
**Later:** D1 (visuals), D2 and D3, C3 to C5, H1, and the evaluation plan.

## What was already corrected while building this roadmap

`VERIFICATION.md` records what was checked against the BrailleBlaster source and what still needs the application.

Writing this roadmap involved checking the earlier drafts against the official User Guide. Corrections already made in the book are listed in `CURRICULUM_REVIEW.md`. They include the default save format (BBX, not BBZ), the Volume Manager workflow in Lesson 23, the T-Page Generator cautions in Lesson 24, and the Braille Preview's three navigation modes.
