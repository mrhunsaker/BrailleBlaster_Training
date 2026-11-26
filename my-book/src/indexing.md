# Indexing Workflow Reference

This page is a practical companion to [Lesson 31: Glossaries and Indexes](lessons/31-glossaries-and-indexes.md). Use that lesson for the full concept explanation, style examples, worked demonstration, and answer key. This reference consolidates the production sequence and verification points.

## 1. Inspect the source

Before applying styles:

1. Identify the index or glossary boundaries.
2. Determine the number of hierarchy levels.
3. Distinguish main entries, subentries, definitions, cross-references, and locators.
4. Check whether the source provides semantic tags or only visual formatting.
5. Record project-specific requirements for entry wording, locator treatment, and pagination.

Do not infer hierarchy from indentation or boldface alone when the source structure is ambiguous. Resolve uncertainty against the source and project specification.

## 2. Apply the matching styles

Use the Glossary or Index style family that matches the total number of levels. Apply the correct level style to every entry and subentry, then inspect first-line and runover positions in Braille View.

The style names encode the number of levels and the level letter (for example, Index 2a and Index 2b). The exact style specification in the installed BrailleBlaster User Guide is authoritative; do not substitute a calculated margin pattern for the version-specific style table.

## 3. Handle emphasis deliberately

In alphabetic-reference sections, do not carry over print emphasis automatically. Follow the applicable edition of Braille Formats and the project specification. If using BrailleBlaster's Remove Emphasis from Alphabetic Reference Entry Words tool:

1. Save a working copy first.
2. Confirm the section has the appropriate Glossary or Index styles.
3. Run the tool.
4. Review the result and restore any emphasis that is required to distinguish a foreign word, title, or other special case.

Treat tools marked experimental in the installed release as requiring additional verification.

## 4. Add guide words after pagination is stable

Guide words depend on the first and last entries appearing on each braille page. Finalize styles, spacing, running heads, page numbering, and other layout decisions before generating or editing guide words. Any later pagination change can invalidate them.

## 5. Quality-control checklist

- [ ] All entries and subentries are present and in the correct order.
- [ ] Hierarchy is represented consistently.
- [ ] Each entry has the correct level style.
- [ ] First-line and runover positions match the installed style specification.
- [ ] Locators and cross-references match the source.
- [ ] Emphasis has been reviewed against the applicable standard.
- [ ] Guide words match the final page contents.
- [ ] Braille Preview has been checked page by page.
- [ ] Corrections and unresolved questions are recorded.
- [ ] A second qualified reviewer has completed the required review.

## Evidence to retain

Keep the source reference, style decisions, exception notes, final page review, correction log, and reviewer sign-off with the production record. For learner assessment, use the practice passage and answer guide in Lesson 31 and record observed performance rather than relying only on a completed worksheet.

## Authority and version control

BrailleBlaster's available styles and tools vary by release. Consult the User Guide for the installed build and the current applicable braille code and transcription standards. This workflow is a training aid, not a substitute for the governing standard or the contract for a specific production.
