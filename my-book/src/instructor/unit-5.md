# Teaching Notes: Unit 5: Handbook

These notes support Lessons 33 to 54. The Handbook is **supplemental and independent**, so teach a lesson when its topic arises, using the placement table on the [unit page](../units/unit-5-handbook.md). Much of it works best as a **workshop on real files**: bring a few messy sources of different kinds, and inspect them together.

## Two teaching habits for the whole unit

1. **Predict, then check.** Before opening a file in BrailleBlaster, have learners write down what they expect to happen to its headings, images, math, and title. The gap between prediction and result is where the learning is.
2. **Compare with the source.** Make counting figures and checking the title a routine after every import. The most serious problems in this unit lose content silently.

> [!NOTE]
> Most statements about what BrailleBlaster does with a file come from running its conversion script, not from the application. If a result differs in your copy, record it in `VERIFICATION.md` and consider reporting it ([`UPSTREAM_ISSUES.md`](https://github.com/mrhunsaker/BrailleBlaster_Training/blob/main/UPSTREAM_ISSUES.md)).

---

## Lesson 33: What Makes a Good Source

**Read the lesson:** [What Makes a Good Source](../lessons/33-what-makes-a-good-source.md).

### Teaching strategy and practice design

**Strategy.** Bring five real sources of different quality and have learners rank them *before* you teach the ladder. Then reveal what each loses on import.

**Common pitfalls and fixes**

- Treating a file that opens as a file that imported well → compare figure counts and the title every time.
- Skipping the request → show that a good request is the cheapest fix.

### Check for understanding

- Ranks six sources correctly.
- Names at least three of the ten rules and the loss each prevents.
- Writes a specific, polite source request.

---

## Lesson 34: Markdown Syntax Guide

**Read the lesson:** [Markdown Syntax Guide](../lessons/34-markdown-syntax-guide.md).

### Teaching strategy and practice design

**Strategy.** Have learners write a short document in Markdown, convert it, and *predict* each result from the table before checking.

**Common pitfalls and fixes**

- Using a line block for a poem → backslash line breaks.
- An image alone on a line → put it in a sentence.
- Expecting strikethrough to survive.

### Check for understanding

- Writes every common construct.
- Predicts the BrailleBlaster result for each.
- Uses a custom-style block correctly.

---

## Lesson 35: Word: Building Structure with Styles

**Read the lesson:** [Word: Building Structure with Styles](../lessons/35-word-structure-with-styles.md).

### Teaching strategy and practice design

**Strategy.** Teach with two files that look identical and are not (the structured and the flat). Let learners find the difference with the Navigation Pane.

**Common pitfalls and fixes**

- Fake headings → apply a style.
- Floating pictures and text boxes → in line with text.
- Assuming Title is a heading.

### Check for understanding

- Inspects a file by the eight checks.
- Repairs a flat file.
- Names the styles BrailleBlaster recognizes.

---

## Lesson 36: LibreOffice, OpenOffice, and Google Docs

**Read the lesson:** [LibreOffice, OpenOffice, and Google Docs](../lessons/36-libreoffice-openoffice-and-google-docs.md).

### Teaching strategy and practice design

**Strategy.** Run the same task in the program your learners use. Have them save as ODT and DOCX and compare what BrailleBlaster does.

**Common pitfalls and fixes**

- Saving as ODT and expecting margin styles to work.
- Sending a PDF from Google Docs when the original exists.

### Check for understanding

- Applies styles by keyboard in their program.
- Explains the ODT and DOCX difference.
- Exports for BrailleBlaster correctly.

---

## Lesson 37: Reading and Working with XML

**Read the lesson:** [Reading and Working with XML](../lessons/37-reading-xml.md).

### Teaching strategy and practice design

**Strategy.** Start in a web browser, which shows a tree and needs no installation. Break a file on purpose and read the error.

**Common pitfalls and fixes**

- Forgetting the namespace in a query → bind a prefix or use local-name().
- Treating well-formed as valid.

### Check for understanding

- Says whether a file is well-formed and why.
- Writes five XPath queries.
- Fixes three malformed snippets.

---

## Lesson 38: DTBook, NIMAS, and MathML

**Read the lesson:** [DTBook, NIMAS, and MathML](../lessons/38-dtbook-nimas-and-mathml.md).

### Teaching strategy and practice design

**Strategy.** Give learners a NIMAS file and ask what they would check before transcribing. Then teach the element map.

**Common pitfalls and fixes**

- Assuming the level nesting sets the heading style → the h number does.
- Trusting a NIMAS file because it is NIMAS.
- An image where an equation should be.

### Check for understanding

- Names the parts of a NIMAS file set.
- Reads a MathML structure aloud.
- Inspects a file set with the checklist.

---

## Lesson 39: Inside the Packages

**Read the lesson:** [Inside the Packages](../lessons/39-inside-the-packages.md).

### Teaching strategy and practice design

**Strategy.** Open a DOCX, an EPUB, and a BBZ as zip files in front of the class. The surprise that they are all zip files is the lesson.

**Common pitfalls and fixes**

- Editing a BBX or BBZ by hand.
- Confusing style IDs with style names.

### Check for understanding

- Counts pStyle in a Word file and reads the result.
- Finds the spine of an EPUB.
- Describes a BBX and a BBZ.

---

## Lesson 40: LaTeX for Transcribers

**Read the lesson:** [LaTeX for Transcribers](../lessons/40-latex-for-transcribers.md).

### Teaching strategy and practice design

**Strategy.** Teach reading before anything else: have learners say five equations aloud. Check their readings against the structure.

**Common pitfalls and fixes**

- Misreading braces: x^{n+1} and x^n+1.
- Missing the document class.
- Not noticing a dropped TikZ picture.

### Check for understanding

- Reads common LaTeX math in English.
- Predicts the headings for a given document class.
- Lists what will not import.

---

## Lesson 41: Text Encoding, Clean Text, and Braille Characters

**Read the lesson:** [Text Encoding, Clean Text, and Braille Characters](../lessons/41-text-encoding-and-braille-characters.md).

### Teaching strategy and practice design

**Strategy.** Run the character report on a paragraph pasted from a PDF. The list of invisible characters is always a surprise.

**Common pitfalls and fixes**

- Hard-wrapped text → unwrap it.
- Not checking the encoding.
- Confusing the Braille ASCII digit with the numeral.

### Check for understanding

- Finds and fixes invisible characters.
- Converts a word to dots, Unicode, and Braille ASCII.
- Reads a short BRF as text.

---

## Lesson 42: PDFs, Scans, and OCR

**Read the lesson:** [PDFs, Scans, and OCR](../lessons/42-pdfs-scans-and-ocr.md).

### Teaching strategy and practice design

**Strategy.** Give learners a text PDF and a scanned one and ask which is which, using only commands.

**Common pitfalls and fixes**

- Using -layout for braille.
- Trusting extracted math.
- Skipping the proofreading of OCR.

### Check for understanding

- Triages a PDF with three commands.
- Finds the OCR errors in a passage.
- Asks for a better source.

---

## Lesson 43: Braille Formats Crosswalk

**Read the lesson:** [Braille Formats Crosswalk](../lessons/43-braille-formats-crosswalk.md).

### Teaching strategy and practice design

**Strategy.** Hand out the standard and ask learners to find the rule for five decisions. Time them. Speed comes with practice.

**Common pitfalls and fixes**

- Stopping at the first sentence of a rule.
- Confusing *shall* and *may*.
- Treating the agency style sheet as the standard.

### Check for understanding

- Names the authority for each kind of question.
- Finds a rule and its sub-rules.
- Records a judgment decision.

---

## Lesson 44: Quick-Reference Cards

**Read the lesson:** [Quick-Reference Cards](../lessons/44-quick-reference-cards.md).

### Teaching strategy and practice design

**Strategy.** Have learners build a personal card for the five indicators they forget most. Making the card is the learning.

**Common pitfalls and fixes**

- Using a card instead of the code book.
- Copying a card that was never checked.

### Check for understanding

- Encodes and decodes indicators from dots.
- Names the prefix and suffix of any typeform.
- Corrects a card from the code book.

---

## Lesson 45: Page Geometry and Sizing Volumes

**Read the lesson:** [Page Geometry and Sizing Volumes](../lessons/45-page-geometry-and-volume-sizing.md).

### Teaching strategy and practice design

**Strategy.** Give each learner a different book and have them estimate volumes from a measured sample. Compare the estimates.

**Common pitfalls and fixes**

- Estimating from the easiest pages.
- Forgetting front matter.
- Ignoring interpoint.

### Check for understanding

- Calculates pages, sheets, and volumes.
- Explains a profile and settings mismatch.
- Tells the requester the volume count first.

---

## Lesson 46: Image Description and Tactile Graphics

**Read the lesson:** [Image Description and Tactile Graphics](../lessons/46-image-description-and-tactile-graphics-resources.md).

### Teaching strategy and practice design

**Strategy.** Describe a chart aloud to a partner who cannot see it, and have them draw it. The drawing exposes what was missing.

**Common pitfalls and fixes**

- Interpreting instead of describing.
- Leaving out numbers.
- Making a tactile graphic by copying the print image.

### Check for understanding

- Describes a chart, map, and diagram in order.
- Chooses description, graphic, both, or neither.
- Names three published guidelines.

---

## Lesson 47: Subject-Area Decision Guide

**Read the lesson:** [Subject-Area Decision Guide](../lessons/47-subject-area-decision-guide.md).

### Teaching strategy and practice design

**Strategy.** Present six jobs from different subjects and have learners list their questions before any tool. Questions are the skill.

**Common pitfalls and fixes**

- Assuming the code.
- Transcribing music notation.
- Treating a secured test as ordinary work.

### Check for understanding

- Asks the four questions for every subject.
- Matches features to lessons.
- Refers music on.

---

## Lesson 48: Job Intake and the Agency Style Sheet

**Read the lesson:** [Job Intake and the Agency Style Sheet](../lessons/48-job-intake-and-the-agency-style-sheet.md).

### Teaching strategy and practice design

**Strategy.** Give learners a vague email and have them write the reply. Then compare replies.

**Common pitfalls and fixes**

- Asking questions one at a time.
- Starting before the code is confirmed.
- A style sheet nobody updates.

### Check for understanding

- Fills in a complete ticket.
- Gives a range estimate.
- Writes a style sheet entry and a log entry.

---

## Lesson 49: File Management, Backups, Version Control, and Student Privacy

**Read the lesson:** [File Management, Backups, Version Control, and Student Privacy](../lessons/49-file-management-and-student-privacy.md).

### Teaching strategy and practice design

**Strategy.** Run the folder audit as a game: how many privacy problems can learners find in two minutes?

**Common pitfalls and fixes**

- Student names in file names.
- Backups on the same disk.
- Git for student data.

### Check for understanding

- Builds the folder structure.
- Names files correctly.
- Applies the privacy checklist.

---

## Lesson 50: Embosser Operation and Maintenance

**Read the lesson:** [Embosser Operation and Maintenance](../lessons/50-embosser-operation-and-maintenance.md).

### Teaching strategy and practice design

**Strategy.** Teach with the real machine and the manufacturer's manual open. Have every learner emboss a test page and check it.

**Common pitfalls and fixes**

- Skipping the first-page test.
- Opening the machine beyond the manual.
- Not logging faults.

### Check for understanding

- Runs the pre-flight check.
- Diagnoses six faults in order.
- Keeps a log.

---

## Lesson 51: An Accessible Workflow

**Read the lesson:** [An Accessible Workflow](../lessons/51-accessible-workflow.md).

### Teaching strategy and practice design

**Strategy.** Let learners run the test protocol on their own equipment and share the logs. Their results are the content.

**Common pitfalls and fixes**

- Assuming support instead of testing it.
- Leaving Breadcrumbs on when they are disruptive.

### Check for understanding

- Works by keyboard.
- Completes the test log.
- Writes a precise barrier report.

---

## Lesson 52: Decision Trees

**Read the lesson:** [Decision Trees](../lessons/52-decision-trees.md).

### Teaching strategy and practice design

**Strategy.** Have learners use the trees on real jobs, then write their own tree for a question the course does not cover.

**Common pitfalls and fixes**

- Following a tree where it does not fit.
- Not writing the decision down.

### Check for understanding

- Reaches the right action in each tree.
- Says when a tree does not apply.
- Writes a tree of their own.

---

## Lesson 53: Error Gallery

**Read the lesson:** [Error Gallery](../lessons/53-error-gallery.md).

### Teaching strategy and practice design

**Strategy.** Show before-and-after pairs and have learners name the cause before the fix. Then they find their own errors.

**Common pitfalls and fixes**

- Fixing the output and not the source.
- Treating import errors as visible ones.

### Check for understanding

- Names the case for each symptom.
- Sorts errors by category.
- Keeps an error log.

---

## Lesson 54: A Model Job: Capstone Walkthrough

**Read the lesson:** [A Model Job: Capstone Walkthrough](../lessons/54-a-model-job-capstone-walkthrough.md).

### Teaching strategy and practice design

**Strategy.** Assign the capstone first. Hold the walkthrough back until learners have submitted their own.

**Common pitfalls and fixes**

- Reading the model before trying the job.
- Treating the model as the only answer.

### Check for understanding

- Compares a difference using the four questions.
- Writes a production log to the model standard.
- Explains each decision and its lesson.

---
