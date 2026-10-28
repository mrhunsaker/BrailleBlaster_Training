# Lesson 22: Transcriber's Notes in the Text

> **Lesson at a glance**
>
> - **Unit:** Unit 3: Transcriber-Focused Lessons
> - **Suggested time:** about 90 minutes
> - **Prerequisites:** [Lesson 3](03-typeface-emphasis.md), [Lesson 4](04-layout-styles.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Decide whether a note is needed and whether it belongs inline or in its own paragraph.
- Apply TN indicators as emphasis and use the Transcriber's Note style for whole paragraphs.
- Separate a print caption from a transcriber-generated description.

---

## How to use this lesson

The first half explains Transcriber's Notes (TN) in three common production situations: **inline**, **as their own paragraph**, and **with figures/captions/descriptions**. The second half is practice. For each scenario, decide whether a TN is needed, where it belongs, and whether it should be inline or separate.

---

## The Concept

### A Transcriber's Note is communication from the transcriber

A TN tells the braille reader something that the transcriber has added because the print source does not communicate a feature adequately in braille, or because the reader needs to understand a transcription decision.

Ask:

- Is this information from the author or from the transcriber?
- Does the reader actually need the explanation?
- Can the information be understood from the braille itself?
- Should the note occur exactly where the issue appears, or apply to a larger section?

### Inline Transcriber's Notes

An inline TN belongs within the current text flow when the explanation is local to a word, phrase, symbol, or sentence.

Example:

```text
The word “lead” [TN: In this sentence, the word is pronounced /led/.] appears here.
```

BrailleBlaster supports Transcriber Note Symbols as emphasis; the current user guide explains that TN indicators are added at the beginning and end of selected text. 

Do not put TN indicators around ordinary parenthetical material supplied by the author merely because it looks like a note.

### TN as its own paragraph

Use a separate TN paragraph when the explanation applies to a passage, section, table, figure, or transcription decision rather than to one exact word.

BrailleBlaster's **Transcriber's Note** style encloses each selected paragraph in TN indicators and uses 7-5 margins. The entire applicable selection should be made before applying the style so BrailleBlaster knows where the indicators belong. 

Example:

```text
[TN: The print source uses color to distinguish the three categories. The categories are identified by name in braille because color itself is not available to the reader.]
```

### Figures: caption versus description

BrailleBlaster distinguishes between a **Caption** and a **Description**. A Caption is print-provided; a Description is transcriber-generated. The current documentation notes that caption styles do not automatically include TN indicators, while transcriber-generated descriptions receive TN treatment. 

Example:

```text
Figure 4.2. The water cycle

[TN: The diagram shows evaporation, condensation, precipitation, and collection in the body of water.]
```

The first line is source text. The second is transcriber-generated information.

### Tables and changed formats

When a print table is substantially reformatted, a TN may be needed to explain the new organization. BrailleBlaster's Table Editor includes **Create Transcriber Note Heading** for listed tables. 

---

## Worked Demonstration

### Example 1 — Inline

A print feature changes meaning at one location only. Add a brief inline TN at that location rather than repeating the explanation throughout the section.

### Example 2 — Own paragraph

```text
[TN: The following section uses a visual shading convention in print. Shaded items are identified by the word “Vocabulary” in braille.]
```

This note applies to the section, so a separate paragraph is appropriate.

### Example 3 — Figure

```text
Figure 6. A map of the United States

[TN: The map shows the Atlantic Ocean on the east and the Pacific Ocean on the west. State boundaries are represented by lines and major cities by dots.]
```

---

## Practice Document

### Scenario 1 — inline

```text
The print source uses red text to identify vocabulary.
```

The color carries instructional meaning. Decide where the reader needs the explanation.

### Scenario 2 — separate paragraph

```text
The next three pages use shaded boxes to identify key ideas.
```

Decide whether one TN before the section is better than repeated inline notes.

### Scenario 3 — print caption

```text
Figure 3.1. Parts of a flower
```

Is this automatically a TN?

### Scenario 4 — transcriber description

A photograph has no descriptive text in print. A transcriber creates a description for the braille reader. What kind of material is this?

### Scenario 5 — listed table

A five-column print table is reformatted as a listed table. Does the reader need an explanation of the changed structure?

### Scenario 6 — unnecessary TN

The author writes:

```text
Note: Remember that plants need water.
```

Should the transcriber automatically put TN indicators around it?

---

## Answer Key

### 1. Inline

If the color distinction matters at a particular point, explain it locally with an inline TN. Avoid repeating the same explanation unnecessarily.

### 2. Separate paragraph

A separate TN is preferable when one explanation applies to an entire section.

### 3. Print caption

No. It is source text. Use the Caption style when appropriate; do not add TN indicators merely because the text identifies a figure. 

### 4. Transcriber description

It is transcriber-generated information and should be treated as a description/TN.

### 5. Listed table

Yes, when the structural change is significant enough that the reader needs an explanation. BrailleBlaster provides a TN-heading function for listed tables. 

### 6. Unnecessary TN

No. It is author-supplied text. It is not a TN merely because it begins with “Note.”

---

## Core Principle

**Ask who is communicating the information and where the reader needs it.** Use an inline TN for a local issue, a separate TN for a larger explanation, and distinguish print captions from transcriber-generated descriptions.

---

## Source Citations

- *Braille Formats 2016* — Transcriber's Notes and special material.
