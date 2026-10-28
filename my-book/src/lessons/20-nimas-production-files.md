# Lesson 20: Importing and Working with NIMAS Files

> **Lesson at a glance**
>
> - **Unit:** Unit 3: Transcriber-Focused Lessons
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 4](04-layout-styles.md), [Lesson 15](15-importing-latex-xml-nimas-epub.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Explain what structure NIMAS carries and what BrailleBlaster can infer from it.
- Navigate a long textbook with the Book Tree.
- Decide whether each publisher production note should be kept, hidden, or removed.
- Proofread an imported NIMAS file for missing headings and nested lists.

## Why this matters

**NIMAS** (the National Instructional Materials Accessibility Standard) is, for many production transcribers, the single most common source format they'll open — it's the XML-based format publishers submit to the National Instructional Materials Access Center (NIMAC) so that accessible formats, including braille, can be produced for K-12 students with qualifying print disabilities under IDEA 2004. BrailleBlaster was built from the start around taking advantage of NIMAS's rich markup, which is why NIMAS files typically arrive in BrailleBlaster far more pre-formatted than an average Word document ([Lesson 2](02-opening-word-documents.md)) — but "more pre-formatted" is not the same as "finished," and this lesson covers both the shortcuts NIMAS gives you and the manual review it still requires.

---

## How to use this lesson

The first half explains what makes NIMAS different from a flat text source. The second half is a practice document — inspect the supplied XML-style scenarios and decide what BrailleBlaster may infer automatically and what still requires human review.

---

## The Concept

### NIMAS is structural XML

NIMAS (National Instructional Materials Accessibility Standard) is an XML-based format used for accessible instructional materials. Unlike a plain text file, NIMAS can carry structural information about the source document.

That structure may help BrailleBlaster identify:

- headings;
- sections;
- lists;
- tables;
- print page information;
- other source structure.

### Importing NIMAS can save work, but it does not remove proofreading

BrailleBlaster's NIMAS workflow can automatically apply some formatting from the source. The current documentation specifically notes that NIMAS files may arrive with print and braille page information, heading designations, tables, lists, and other structure.

The transcriber/teacher still needs to inspect the result because source markup may be incomplete, inconsistent, or based on a publisher's production choices.

### Production notes are not ordinary body text

NIMAS files may contain publisher production notes intended to help with physical production. BrailleBlaster includes tools for viewing and deciding whether production notes should be kept, hidden, or removed.

The key question is: **Does the note help produce the braille material, or is it irrelevant to the student's reading document?**

### Book Tree is a navigation aid

NIMAS files can be navigated with the Book Tree, which reflects section and heading structure. This is especially useful for long textbook files.

---

## Step by step: Opening and Reviewing a NIMAS File

1. Go to **File > Open** (`Ctrl+O`) and select the NIMAS XML file, or the zipped NIMAS package.
2. Once open, use the **Book Tree** to get an overview of the book's structure before diving into detailed editing.
3. Check for and read any **Publisher's Production Notes** included in the file.
4. Review headings, lists, tables, and emphasis with Breadcrumbs turned on, watching specifically for print-only formatting (like bold headings) that came through technically correctly mapped but doesn't belong in the final braille.
5. If the file contains MathML, spot-check a few converted math elements in the Braille View to confirm the automatic ASCII Math conversion translated as expected, especially for anything mathematically unusual.
6. For a large textbook being split across multiple transcribers, use the file-dividing tools to break the book along its publisher-designated sections before assigning work.

---

## Worked Demonstration (small, fully correct)

Suppose a NIMAS source contains:

```xml
<section>
  <h1>Chapter 4: Energy</h1>
  <p>Energy is the ability to do work.</p>
  <ol>
    <li>Potential energy</li>
    <li>Kinetic energy</li>
  </ol>
</section>
```

After opening the NIMAS file:

- Inspect the Book Tree.
- Confirm that "Chapter 4: Energy" is recognized as a heading.
- Confirm that the two items are a list rather than two ordinary paragraphs.
- Check the style hierarchy.
- Check print-page information.
- Inspect Braille View.
- Do not manually reproduce the XML tags inside the braille document.

The XML is the source structure; BrailleBlaster's styles are the working transcription structure.

---

## Practice Document

### Scenario 1 — clean NIMAS structure

```xml
<section>
  <h1>Plants</h1>
  <h2>Roots</h2>
  <p>Roots anchor a plant and absorb water.</p>
</section>
```

### Scenario 2 — missing heading tag

```xml
<p>Chapter 6: Weather</p>
<p>Weather describes short-term atmospheric conditions.</p>
```

### Scenario 3 — production note

```text
Publisher production note:
"Place the color plate after page 42 in the final print edition."
```

### Scenario 4 — nested list

```xml
<ol>
  <li>Mammals
    <ol>
      <li>Dogs</li>
      <li>Cats</li>
    </ol>
  </li>
</ol>
```

### Scenario 5 — long textbook

```text
A 700-page NIMAS file has imported successfully.
The Book Tree contains hundreds of sections.
```

---

## Answer Key

### Scenario 1

The heading hierarchy and paragraph should be recognized from the XML structure. Verify the imported styles and resulting braille.

### Scenario 2

The text may look like a heading in Print View, but the XML structure does not identify it as one. Human review is required.

### Scenario 3

Treat it as a production note, not as ordinary body text. Decide whether it should be kept, hidden, or removed based on its usefulness to the production workflow.

### Scenario 4

The nested list structure is meaningful and should be preserved as a nested list in BrailleBlaster.

### Scenario 5

Use the Book Tree and other navigation tools rather than scrolling linearly. A successful import still requires systematic inspection of headings, lists, tables, page numbers, and production notes.

### Core principle

**NIMAS gives BrailleBlaster structure to work with; it does not give the transcriber permission to stop checking the work.**

---

---

## Key takeaways

- NIMAS is an XML-based format publishers use to submit accessible-format-ready textbooks to NIMAC under IDEA 2004; it's the source format BrailleBlaster was originally built around.
- Rich NIMAS tagging lets BrailleBlaster automatically map most structural elements (headings, lists, tables, page numbers) onto the correct styles — but print-only formatting (like bold headings) can still come through attached to a correctly-identified element and needs manual review.
- MathML embedded in a NIMAS file is automatically converted to ASCII Math and translated into the document's braille math code.
- The Book Tree is the fastest way to get a structural overview of a NIMAS book; Publisher's Production Notes are a valuable, easily-overlooked source of context.
- Large NIMAS textbooks can be divided along publisher-designated sections for parallel work by multiple transcribers, then rejoined into one final file.
