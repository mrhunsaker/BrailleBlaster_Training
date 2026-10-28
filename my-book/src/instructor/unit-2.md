# Teaching Notes: Unit 2: Advanced Lessons

These notes support Lessons 14 to 19. Unit 2 relies on learners seeing what survives each import. Bring real files, including a messy one.

## Lesson 14: Importing Source Formats I: Markdown and OpenDocument

**Read the lesson:** [Importing Source Formats I: Markdown and OpenDocument](../lessons/14-importing-markdown-and-opendocument.md). **Suggested time:** 120 minutes.

### Check for understanding

- States what Markdown and ODT preserve.
- Notices list problems after a Markdown import.
- Names the first things to check after each import.

---

## Lesson 15: Importing Source Formats II: LaTeX, XML, NIMAS, and EPUB

**Read the lesson:** [Importing Source Formats II: LaTeX, XML, NIMAS, and EPUB](../lessons/15-importing-latex-xml-nimas-epub.md). **Suggested time:** 150 minutes.

### Check for understanding

- Explains the math consequence of LaTeX.
- Separates general XML from NIMAS.
- Treats EPUB as its own workflow.

---

## Lesson 16: Choosing an Import Workflow

**Read the lesson:** [Choosing an Import Workflow](../lessons/16-choosing-an-import-workflow.md). **Suggested time:** 90 minutes.

### Demonstration idea

If you have access to source material in more than one format — for instance, a short document available as both a `.docx` export and an original `.md` file — open both in BrailleBlaster and compare the results side by side. This is a genuinely instructive exercise: learners can see directly how Markdown's explicit structural syntax tends to produce a cleaner, more predictable import than a word-processor file of uncertain internal construction, even when the two files look identical when read as plain text or viewed in a browser.

### Tips and pitfalls

**Tip:** If your agency has any influence over how source material is authored — commissioning custom worksheets from in-house staff, for instance — this lesson is worth revisiting from the *opposite* direction: which formats would make transcription faster and more reliable downstream? Markdown and well-structured LaTeX are often better authoring targets than a word processor document, precisely because their structure can't drift into "looks right but isn't" the way visual word-processor formatting can.

A common pitfall specific to LaTeX: assuming that because *some* LaTeX opened perfectly last time, *all* LaTeX will. LaTeX's flexibility (custom packages, macros, unusual notation) means import fidelity varies file to file far more than it does for the other formats in this lesson. Build the TeX4HT fallback into the standard workflow rather than treating it as a rare exception.

### Check for understanding

- Chooses the right workflow for each of the six scenarios.
- Recites the six core principles in their own words.
- Completes the production checklist on a real file.

### Extension activity

Have learners take one short document and produce it in two different source formats they have access to (for example, saved as both .docx and exported/copied as Markdown). Have them open both in BrailleBlaster, compare the resulting structure using Breadcrumbs, and write a short note on which format required more manual correction and why.

---

## Lesson 17: What Pandoc Does for BrailleBlaster

**Read the lesson:** [What Pandoc Does for BrailleBlaster](../lessons/17-what-pandoc-does.md). **Suggested time:** 60 minutes.

### Tips and pitfalls

**Tip:** For a class of newer transcribers, this lesson works best as a short closing discussion rather than a technical deep dive — the goal is a working mental model ("there's a shared conversion engine under a lot of this, and that's why 'convert to HTML first' keeps coming up as advice"), not command-line fluency. Save deeper Pandoc mechanics for transcribers who go on to take a more technical, IT-adjacent role within your agency.

### Check for understanding

- Explains Pandoc as a structure converter, not a braille translator.
- Predicts what is lost in conversion.
- Uses convert-to-HTML as a deliberate fallback.

### Extension activity

As a closing exercise for the full course, have learners write a short memo (a paragraph or two) to a hypothetical colleague explaining, in plain language, why they should ask source-material authors for well-structured documents (real headings, real lists) whenever possible — drawing on at least three specific examples from earlier chapters in this course ([Lesson 2](../lessons/02-opening-word-documents.md)'s Word documents, [Lesson 20](../lessons/20-nimas-production-files.md)'s NIMAS files, and this lesson's Pandoc-supported formats are all fair game) to make the case concrete rather than abstract.

---

## Lesson 18: Advanced Formatting: Boxes, Plays, Poems, and Deep Lists

**Read the lesson:** [Advanced Formatting: Boxes, Plays, Poems, and Deep Lists](../lessons/18-advanced-formatting.md). **Suggested time:** 180 minutes.

### Demonstration idea

Take a one-page excerpt containing a short boxed "fun fact" sidebar, four lines of a two-character script exchange, and a four-line poem stanza. Apply Box (or Full Box, depending on the sidebar's exact print treatment), the appropriate Play styles for the character names and dialogue lines, and Poetic Stanza for the poem, in that order. After each one, check Breadcrumbs to confirm the container wraps exactly the intended text — no more, no less — before moving to the next element.

### Tips and pitfalls

**Tip:** Deep lists are a good moment to revisit the "Reduce Fraction"-style lesson from [Lesson 10](../lessons/10-spatial-number-lines.md): just because BrailleBlaster *can* represent eleven levels of nesting doesn't mean every source document's apparent nesting is meaningful at that depth. Encourage learners to sanity-check unusually deep outline structure against the actual print original before reproducing every visual indent level as a distinct braille list level — a print document's visual indentation sometimes reflects word-processor formatting habits rather than a genuinely eleven-deep logical structure.

### Check for understanding

- Decides whether a box is structural or decorative.
- Keeps speaker and stage directions distinct in a play.
- Formats a poem by line and stanza, with line numbers where needed.

### Extension activity

Provide learners a one-page excerpt combining a boxed sidebar, a short two-character script exchange, and a short poem. Have them apply the correct style to each, verify each container's extent using Breadcrumbs, and look up the specific margin specification for one of the three styles in the built-in Style Appendix, reporting back what they found.

---

## Lesson 19: The eBraille Format

**Read the lesson:** [The eBraille Format](../lessons/19-ebraille.md). **Suggested time:** 60 minutes.

### Tips and pitfalls

**Tip:** This is a good chapter for a short discussion rather than a hands-on exercise, especially for a class of brand-new transcribers. Frame it as "here's where the field is heading and why," not "here's a tool you need to master today." Save the hands-on eBraille workflow for a later, dedicated session once BrailleBlaster's eBraille export tools are part of your agency's regular production process.

A pitfall worth naming explicitly: don't let learners walk away thinking eBraille *replaces* BRF or embossed braille. It solves a different problem — reflowable digital reading on refreshable displays — and exists alongside, not instead of, page-fixed embossed output.

### Check for understanding

- Explains eBraille to a non-specialist in plain words.
- Chooses BRF, eBraille, or both for each scenario.
- States that eBraille does not replace BRF.

### Extension activity

Have learners write a short (one-paragraph) explanation, in their own words, of the practical difference between a BRF file and an eBraille file, aimed at a colleague who has never heard of either. Discuss a few answers as a group and compare which explanations would actually make sense to someone outside the field.

