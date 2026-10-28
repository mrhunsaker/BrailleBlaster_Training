# Lesson 17: What Pandoc Does for BrailleBlaster

> **Lesson at a glance**
>
> - **Unit:** Unit 2: Advanced Lessons
> - **Suggested time:** about 60 minutes
> - **Prerequisites:** [Lesson 14](14-importing-markdown-and-opendocument.md), [Lesson 15](15-importing-latex-xml-nimas-epub.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Explain that Pandoc converts document structure and does not apply braille formatting rules.
- Predict what is likely to survive a conversion and what must be checked.
- Use "convert to HTML first" as a deliberate troubleshooting step.

## Why this matters

Throughout this course — Word and OpenDocument import ([Lesson 2](02-opening-word-documents.md)), LaTeX handling ([Lesson 16](16-choosing-an-import-workflow.md)), even the general idea of a broad, forgiving range of supported file formats — one piece of infrastructure keeps showing up without being named directly: **Pandoc**, a widely-used, open-source document-conversion tool. BrailleBlaster leans on Pandoc-supported formats for a meaningful share of its import capability, and understanding roughly what Pandoc is and does — without needing to become a command-line expert — gives a transcriber a genuinely useful mental model for *why* some files import cleanly and others don't, and *what's actually possible* when a file doesn't open the way you'd expect.

This lesson is intentionally the last lesson in the course, and intentionally light on hands-on exercises. It's meant as a capstone: a look under the hood, for learners who are ready for it, rather than a tool a transcriber needs to operate directly on day one.

---

## How to use this lesson

The first half explains Pandoc as a conversion layer used by BrailleBlaster for supported source formats. The second half is a practice document — predict what information is likely to survive conversion and what must be checked inside BrailleBlaster. The central idea is that Pandoc converts **document structures**, not braille formatting rules.

---

## The Concept

### Pandoc is a document converter, not a braille translator

Pandoc describes itself as a universal document converter. It reads a source format, constructs an internal representation of the document, and writes another format.

That makes Pandoc useful to BrailleBlaster because many modern documents contain structures that are easier to interpret through a general document-conversion pipeline than by writing a separate parser for every source format.

### The basic model

Conceptually:

```text
Source document
      |
      v
   Pandoc reader
      |
      v
Intermediate document structure
      |
      v
Pandoc writer / BrailleBlaster importer
      |
      v
BrailleBlaster document
      |
      v
BrailleBlaster styles + translation + page layout
```

The important point is that **Pandoc is not deciding the final braille margins or page numbering rules**. BrailleBlaster still has to apply its own document structure and braille-production logic.

### Conversion can be lossy

Pandoc's own documentation warns that its intermediate representation is less expressive than some source formats. Consequently, not every formatting detail can survive every conversion.

Examples of information that may require verification include:

- exact margin sizes;
- unusual Word formatting;
- complex tables;
- specialized source-specific layout;
- unsupported LaTeX packages or notation.

This is why the BrailleBlaster manual recommends checking imported documents and, in some difficult LaTeX cases, converting to HTML first.

### Why this matters for teachers

A teacher may receive a DOCX, ODT, Markdown, HTML, EPUB, or LaTeX source and reasonably expect the instructional content to arrive intact. The conversion layer can make that practical, but the teacher still needs to verify:

- headings;
- lists;
- emphasis;
- math;
- images;
- tables;
- page information;
- reading order.

The conversion process is a starting point for braille preparation, not a substitute for instructional review.

---

## What this means for you

You will likely never run Pandoc directly as a transcriber using BrailleBlaster day to day — it operates behind the scenes as part of how certain file types open. But knowing it's there reframes a few recurring troubleshooting situations usefully:

- When an unusual or unsupported file format doesn't import well, converting it to a more universally well-supported intermediate format (HTML being the most reliable) before opening it in BrailleBlaster isn't a hacky workaround — it's working *with* the same architecture BrailleBlaster itself relies on, just doing one extra conversion step by hand that BrailleBlaster would otherwise have attempted automatically.
- The consistent advice throughout this course to prioritize genuinely well-structured source documents — real heading styles, real list structures, real semantic markup, rather than merely visually-formatted text — isn't just good practice for BrailleBlaster specifically. It's good practice for the entire class of tools BrailleBlaster is built on top of, and it will keep paying off as BrailleBlaster's own supported-format list continues to grow.

---

## Worked Demonstration (small, fully correct)

Source Markdown:

```markdown
# Fractions

A fraction has a numerator and a denominator.

1. Read the numerator.
2. Read the denominator.

The example is $1/2$.
```

Conceptual conversion:

```text
Markdown
  ↓
Pandoc parses heading, paragraph, list, and math
  ↓
BrailleBlaster receives structured content
  ↓
BrailleBlaster applies braille styles and math translation
  ↓
Teacher/transcriber verifies Braille View
```

What Pandoc does **not** decide:

- whether a heading should be centered, cell 5, or cell 7;
- what braille page number belongs on a page;
- whether a list's margins meet Braille Formats;
- whether a running head is required;
- whether a particular contraction should be relaxed for a student.

Those are BrailleBlaster/transcription decisions.

---

## Practice Document

### Scenario 1 — DOCX

```text
A Word document contains:
- Heading styles
- A numbered list
- Bold vocabulary
- A complex table
```

### Scenario 2 — Markdown

```text
A Markdown document contains:
- headings
- nested lists
- links
- footnotes
- simple math
```

### Scenario 3 — LaTeX

```text
A LaTeX document contains:
- sections
- equations
- a package-specific command
- a custom page layout
```

### Scenario 4 — conversion loss

```text
The imported document has the correct words,
but its original 2-inch print margins are gone.
```

### Scenario 5 — Braille-specific decision

```text
The imported text contains a paragraph that a teacher wants
to be uncontracted because the student has not yet learned
the relevant contractions.
```

---

## Answer Key

### Scenario 1

Pandoc/BrailleBlaster can preserve much of the structural content, but the complex table requires direct verification. The final braille table structure is not determined by Word's visual appearance alone.

### Scenario 2

Headings and lists are structural information that can be imported. Links and footnotes may also be represented, but they must be checked in BrailleBlaster. Simple math needs verification in the math workflow.

### Scenario 3

Sections and supported math can be imported. A package-specific command or unusual page-layout feature may not survive as intended. If BrailleBlaster cannot interpret the source correctly, the manual recommends considering conversion to HTML as an intermediate route for difficult LaTeX.

### Scenario 4

This is expected behavior for a general document converter. Pandoc's internal representation does not preserve every source-format detail, and exact margin size is not the same thing as semantic document structure.

### Scenario 5

This is **not a Pandoc decision**. It is an instructional BrailleBlaster decision. Use the Contraction Relaxer or an appropriate translation setting to implement the teacher's instructional goal.

### Core principle

**Pandoc moves structure across formats. BrailleBlaster turns that structure into a braille document. The teacher/transcriber remains responsible for the final instructional and braille decisions.**

---

## Key takeaways

- Pandoc is a general-purpose, open-source document converter that BrailleBlaster relies on for part of its support for formats like LaTeX and other Pandoc-supported document types.
- This shared architecture is why converting an unsupported or poorly-behaving file to HTML — a reliably well-supported format — is a recurring, sensible troubleshooting step throughout this course, not a one-off trick specific to any single format.
- Broad format *support* and reliable per-file *conversion quality* are different things; a well-structured source file, in nearly any supported format, will outperform a poorly-structured one.
- The emphasis throughout this course on genuine document structure over visual-only formatting reflects how the whole underlying conversion pipeline actually works, not just a BrailleBlaster-specific preference.

---

## Source Citations

- Pandoc official documentation — Pandoc as a universal document converter and its reader/AST/writer architecture.
- Pandoc User's Guide — conversion is structural and can be lossy when the source is more expressive than Pandoc's intermediate model.
- BrailleBlaster User Manual — Pandoc-supported document types and LaTeX import.
- BrailleBlaster current release information — Pandoc importer fixes and version reporting.
