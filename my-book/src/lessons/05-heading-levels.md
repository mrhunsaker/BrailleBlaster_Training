# Lesson 5: Applying Heading Levels

> **Lesson at a glance**
>
> - **Unit:** Unit 1: Universal Lessons
> - **Suggested time:** about 90 minutes
> - **Prerequisites:** [Lesson 4](04-layout-styles.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Name the three block heading formats defined by *Braille Formats 2016* and their order of importance.
- Compress a print hierarchy of more than three levels into braille headings using the rule in section 4.2.1.
- Recognize when a deep print level becomes a paragraph (run-in) heading.
- Apply Centered, Cell-5, Cell-7, and paragraph headings consistently and justify the choices.

---

## How to use this lesson

The first half explains the concept. The second half is a practice document — copy the fenced "Practice Document" block into a new BrailleBlaster file and apply the correct heading style to every heading line. Nothing in the practice block uses Markdown `#` syntax to mark headings, and heading lines look exactly like body text once pasted in — that's deliberate. In real transcription work, plain text carries no heading information either; you identify a heading from context (or, as here, from a legend showing the source document's structure) and apply the style yourself. Everything in the practice block *other than* heading assignment is already correct — you are only fixing heading levels.

---

## The Concept

### UEB/Braille Formats only defines three block-style heading formats

Print documents can have as many heading levels as a designer wants — HTML alone gives you six (`<h1>` through `<h6>`). Braille does not attempt to match that one-for-one. *Braille Formats 2016* §4 defines exactly **three** indented/blocked heading formats, used in a fixed order of importance:

| Braille Format | Placement            | Blank Lines                                                                      |
| -------------- | -------------------- | -------------------------------------------------------------------------------- |
| **Centered**   | Centered on the line | Preceded *and* followed by a blank line (§4.4.1)                                 |
| **Cell-5**     | Blocked in cell 5    | Preceded by a blank line; usually not followed by one (§4.5.1–§4.5.3)            |
| **Cell-7**     | Blocked in cell 7    | Preceded by a blank line (none if it directly follows a cell-5 heading) (§4.6.2) |

The hierarchy always runs in that order — centered, then cell-5, then cell-7 (§4.2.2) — and a cell-7 heading can never be followed by *any* other heading type (§4.6.6) to indicate an item lower in the hierarchy. It is always the bottom of the hierarchy.

### What happens when print has more than three levels?

*Braille Formats 2016* §4.2.1 addresses this directly: *"When there are more than three distinct heading levels in print, cell-7 headings are applied only to the lowest hierarchy level; the use of centered headings is extended to one or more subsection levels as necessary."* In practice, this means:

- The **shallowest** print levels (title, part, unit, chapter) compress upward into **Centered**, even if that means two or three different print levels all become centered headings.
- The **one level just above the smallest heading** becomes **Cell-5**.
- The **lowest surviving block-style level** becomes **Cell-7**.
- Anything *deeper* than that is usually no longer a true "own-line" heading in the original print at all — it's a **Paragraph (run-in) Heading**.

### Paragraph (run-in) headings — the fourth tool

§4.8 covers the case that matters most for deep hierarchies. A paragraph heading is an emphasized word or short phrase that introduces a paragraph *without* being set on its own line — think of a bolded term at the start of a paragraph in a textbook ("**Photosynthesis.** Plants convert..."). Rules:

- Follow print for emphasis, capitalization, and punctuation; use full capitalization only if print does (§4.8.1).
- No *additional* emphasis is added beyond what print already shows.
- A paragraph heading may be promoted to a cell-5 or cell-7 heading if doing so would help the reader navigate better (§4.8.2) — this is a judgment call, not a rule.
- A heading level may be changed (promoted or demoted) if more than one style of paragraph heading is used in print, or if a single heading's effect spans multiple paragraphs (§4.8.3).

### Why this matters for a reader

A blind reader scans for **blank lines** and **left-margin position** the way a sighted reader scans for font size — a blank line is "like a stop sign" (§4.1.2). Centered headings show up as an uneven gap near mid-line; cell-5 and cell-7 headings show up as a consistent left-margin jump readers learn to recognize without counting cells. Collapsing extra print levels into fewer braille levels isn't a loss of information — it's what keeps that scanning system usable. A braille document with six indented heading depths would defeat the entire mechanism.

### Worked demonstration (small, fully correct)

Print source (three heading levels only):

```
UNIT 2: ECOSYSTEMS                    <- H1
Chapter 4: Food Webs                  <- H2
Producers and Consumers               <- H3
Every food web begins with producers...
```

Correct BrailleBlaster styles:

- "UNIT 2: ECOSYSTEMS" → **Centered Heading** (top print level)
- "Chapter 4: Food Webs" → **Cell-5 Heading** (subsection of the unit)
- "Producers and Consumers" → **Cell-7 Heading** (lowest level; must be followed by text on the same braille page per §4.3.9)

That's the baseline three-level mapping. The practice document below pushes past it to six print levels, so you'll need the compression logic above.

---

## Practice Document: "The Circulatory System"

This is a six-level print hierarchy (`<h1>` through `<h6>`), sourced from a biology textbook chapter. The **Heading Map** below tells you which line came from which HTML level in the original — use it the way you'd use a table of contents sitting next to your monitor. Then apply BrailleBlaster styles to the flat text in the Practice Document block, using the concept rules above (not a 1-to-1 guess) to decide how six print levels become three block headings plus paragraph headings.

### Heading Map (from the original HTML source)

| Original Tag  | Heading Text                      |
| ------------- | --------------------------------- |
| `<h1>`        | UNIT 3: THE HUMAN BODY SYSTEMS    |
| `<h2>`        | Chapter 7: The Circulatory System |
| `<h3>`        | 7.1 The Heart                     |
| `<h4>`        | The Four Chambers                 |
| `<h5>`        | The Right Side of the Heart       |
| `<h6>`        | Right Atrium                      |
| `<h6>`        | Right Ventricle                   |
| `<h5>`        | The Left Side of the Heart        |
| `<h6>`        | Left Atrium                       |
| `<h6>`        | Left Ventricle                    |
| `<h4>`        | The Heart's Electrical System     |
| `<h3>`        | 7.2 Blood Vessels                 |
| `<h4>`        | Arteries                          |
| `<h4>`        | Veins                             |
| `<h4>`        | Capillaries                       |
| `<h3>`        | 7.3 Blood and Circulation         |
| `<h4>`        | Components of Blood               |
| `<h5>`        | Red Blood Cells                   |
| `<h5>`        | White Blood Cells                 |
| `<h5>`        | Platelets and Plasma              |
| `<h4>`        | Pulmonary and Systemic Circulation|

### Practice Document (copy this block into BrailleBlaster)

```
UNIT 3: THE HUMAN BODY SYSTEMS

Chapter 7: The Circulatory System

The circulatory system moves blood, oxygen, and nutrients throughout the body using the heart, blood vessels, and blood itself. This chapter examines each of these three components in turn.

7.1 The Heart

The heart is a muscular organ roughly the size of a closed fist, located slightly left of center in the chest. It functions as two side-by-side pumps working in a coordinated rhythm.

The Four Chambers

The heart contains four hollow chambers: two atria on top and two ventricles below. Blood always flows from atrium to ventricle on each side before leaving the heart.

The Right Side of the Heart

The right side of the heart receives oxygen-poor blood from the body and sends it to the lungs to be reoxygenated.

Right Atrium

The right atrium receives deoxygenated blood returning from the body through the superior and inferior vena cavae.

Right Ventricle

The right ventricle pumps this blood onward into the pulmonary artery, which carries it to the lungs.

The Left Side of the Heart

The left side of the heart receives newly oxygenated blood from the lungs and sends it out to the rest of the body.

Left Atrium

The left atrium receives oxygen-rich blood returning from the lungs through the pulmonary veins.

Left Ventricle

The left ventricle, the thickest and most muscular chamber, pumps this blood out through the aorta to the entire body.

The Heart's Electrical System

A small cluster of specialized cells called the sinoatrial node generates the electrical signal that triggers each heartbeat, coordinating the contraction of all four chambers in sequence.

7.2 Blood Vessels

Blood travels through three distinct types of vessels, each suited to a different part of the circuit.

Arteries

Arteries carry blood away from the heart under high pressure and have thick, elastic, muscular walls to withstand that pressure.

Veins

Veins carry blood back toward the heart under much lower pressure and rely on one-way valves to prevent backflow.

Capillaries

Capillaries are the smallest vessels, often only a single cell thick, and are the site where oxygen, nutrients, and waste actually cross between blood and body tissue.

7.3 Blood and Circulation

Blood itself is a mixture of cells and fluid, and it follows two connected circuits through the body.

Components of Blood

Blood is composed of several distinct components suspended together, each with a very different job.

Red Blood Cells

Red blood cells contain hemoglobin, the protein responsible for carrying oxygen from the lungs to the rest of the body.

White Blood Cells

White blood cells are part of the immune system and defend the body against infection.

Platelets and Plasma

Platelets assist in clotting to stop bleeding, while plasma, the liquid portion of blood, carries all of these components along with dissolved nutrients and waste.

Pulmonary and Systemic Circulation

Blood follows two loops: the pulmonary circuit, which carries blood between the heart and lungs, and the systemic circuit, which carries blood between the heart and the rest of the body.
```

---

## Answer Key

The reasoning below follows §4.2.1 (compress excess levels; extend centered upward, restrict cell-7 to the lowest surviving block level) and §4.8 (deeper levels become run-in Paragraph Headings).

| Original Level                            | BrailleBlaster Style  | Why |
| ----------------------------------------- | --------------------- | --- |
| H1 (Unit title)                           | **Centered Heading**  | Top of the hierarchy — always centered. |
| H2 (Chapter title)                        | **Centered Heading**  | Still a major division of the book, not a subsection of the unit in any meaningful sense to the reader — centered is "extended" to cover it, per §4.2.1. |
| H3 (Section, e.g. "7.1 The Heart")        | **Cell-5 Heading**    | First true subsection level. |
| H4 (Subsection, e.g. "The Four Chambers") | **Cell-7 Heading**    | Lowest block-style level per §4.2.1 — cell-7 is reserved for the lowest hierarchy tier once levels are compressed. |
| H5 (e.g. "The Right Side of the Heart")   | **Paragraph Heading** | Deeper than the lowest block level; treated as a run-in heading per §4.8. |
| H6 (e.g. "Right Atrium")                  | **Paragraph Heading** | Same as H5 — in a six-level hierarchy, both of the two deepest print levels collapse to run-in headings, since braille has no fourth or fifth indented format to give them. |

**A note on judgment:** This is one defensible resolution, but by no means the only valid one. A transcriber who felt the H5 level ("The Right Side of the Heart" / "The Left Side of the Heart") deserved more visual weight than a run-in phrase could reasonably argue for demoting H4 to cell-7 and leaving H5 as the *last* block format, pushing only H6 to paragraph-heading status — as long as it's applied consistently throughout the whole volume (§4.1.1) and, in a production setting, explained on the Transcriber's Notes page. *Braille Formats 2016* describes itself as a set of guidelines for structuring decisions, not a rulebook covering every case (§1, Basic Principles) — this is exactly the kind of decision it means.

---

## Source Citations

- *Braille Formats 2016*, §4 Headings — §4.1 (Fundamentals), §4.2 (Heading Hierarchy, including §4.2.1's compression rule), §4.3 (General Provisions), §4.4 (Centered Headings), §4.5 (Cell-5 Headings), §4.6 (Cell-7 Headings), §4.8 (Paragraph Headings, §4.8.1–§4.8.3).
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, available at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html), including the March 2024 updates.

*Section numbers verified directly against the BANA online edition at brailleauthority.org.*
