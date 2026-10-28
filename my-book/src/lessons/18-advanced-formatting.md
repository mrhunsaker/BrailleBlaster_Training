# Lesson 18: Advanced Formatting: Boxes, Plays, Poems, and Deep Lists

> **Lesson at a glance**
>
> - **Unit:** Unit 2: Advanced Lessons
> - **Suggested time:** about 3 hours
> - **Prerequisites:** [Lesson 4](04-layout-styles.md), [Lesson 5](05-heading-levels.md), [Lesson 6](06-list-formatting.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Treat boxed material as a structural decision and not a drawing task.
- Format plays so speaker and stage direction stay distinct.
- Format poems by line and stanza, using line numbers where needed.
- Format deep lists with the correct list style and margins.

## Why this matters

Most transcription work lives comfortably in body text, headings, and simple lists — the styles covered in [Lesson 4](04-layout-styles.md). But sooner or later, every transcriber meets print material that doesn't fit those shapes: a sidebar set off in a box, a script with character names and stage directions, a poem where line breaks are meaningful, or an outline nested more deeply than a simple bulleted list. BrailleBlaster has dedicated styles for exactly these cases, each following its own section of *Braille Formats 2016*, and this lesson is a tour of the ones a transcriber meets often enough to need working familiarity with, beyond the basics.

---

## How to use this lesson

The first half explains several structures that require more than ordinary paragraph styles. The second half is a practice document — identify the appropriate structural treatment before applying BrailleBlaster styles. The objective is to preserve the **function** of the print structure, not its visual appearance.

---

## The Concept

### Boxed material is a structural problem

A box in print may contain a definition, warning, example, sidebar, or other material. The transcriber must determine what the box means before choosing a braille treatment.

Do not reproduce a decorative border merely because it is visible in print. The reader needs the information and, when relevant, the fact that the material is set apart.

### Plays depend on speaker and stage structure

A play commonly contains:

- character names;
- dialogue;
- stage directions;
- scenes or acts.

The braille format must preserve who is speaking and which text is a stage direction. Speaker changes cannot depend on indentation that is merely visual.

### Poems depend on line and stanza structure

Poetry is not ordinary prose broken into short lines. The line structure can carry meaning. Stanzas, indentation, and line numbers may need special treatment.

BrailleBlaster includes poetry styles and line-number tools that should be used instead of manually inserting spaces.

### Deep lists are structural, not visual

A nested list can be many levels deep. The correct list style depends on the deepest level used by the list section and the applicable margin system.

Do not use a separate, improvised indentation scheme for every branch of a list.

---

## Step by step: Applying a Specialized Style

The mechanical steps are the same as any other style application ([Lesson 4](04-layout-styles.md)), so there is no new workflow to learn even if you expect boxed material, plays, and poetry to require a fundamentally different one:

1. Highlight the text (a full box's contents, a script's lines, a poem's stanza).
2. Go to **Styles** and select the appropriate style — Box/Full Box, the relevant Play style, or Poetic Stanza — or use the corresponding toolbar button.
3. Check Breadcrumbs to confirm the CONTAINER wrapping applied correctly around the full intended extent of the material — a box or stanza that only wraps part of its intended contents is a common and easy-to-miss error.
4. Consult the Style Appendix (**Help**) for the specific margin and spacing specification of the style in question if the result doesn't look right, rather than guessing at manual adjustments.

---

## Worked Demonstration (small, fully correct)

### Box

```text
IMPORTANT:
Always wear safety goggles during the experiment.
```

If the print box communicates an instructional warning, preserve the warning's function and distinguish it appropriately. Do not create a decorative rectangle simply because the source has a border.

### Play

```text
MAYA: We should leave now.

JORDAN: Why?

MAYA: Because the storm is coming.

[Thunder.]

JORDAN: I understand.
```

The speaker identity and stage direction must remain clear in braille.

### Poem

```text
The river moves
beneath the bridge

and carries leaves
toward the sea.
```

Preserve the line and stanza relationships rather than converting the poem into one prose paragraph.

### Deep list

```text
- Science
  - Biology
    - Cells
      - Nucleus
```

Apply the appropriate nested-list structure rather than typing spaces.

---

## Practice Document

### 1. Boxed material

```text
[BOX]
Key Idea:
Evaporation changes liquid water into water vapor.
[/BOX]
```

### 2. Play

```text
ACT I

LENA: Are you ready?

SAM: Almost.

[LENA picks up the book.]

LENA: Now I am ready.
```

### 3. Poem

```text
Winter Morning

Snow rests
on every branch.

The quiet road
waits for footsteps.
```

### 4. Poem with line numbers

```text
1 The first light appears.
2 The houses wake.
3 The street becomes bright.
4 The day begins.
```

### 5. Deep list

```text
- Animals
  - Vertebrates
    - Mammals
      - Primates
        - Great Apes
```

### 6. Mixed sidebar

```text
Vocabulary
adaptation — a trait that helps an organism survive
habitat — the place where an organism lives
```

---

## Answer Key

### 1. Boxed material

Identify the box's function first. If it is a key idea or warning, the reader should receive that information as distinguished material. Do not reproduce the print border as decoration.

### 2. Play

Use play-oriented structure so speaker names and stage directions remain distinguishable. "LENA picks up the book." is a stage direction, not dialogue.

### 3. Poem

Preserve the two stanzas and their line boundaries. Do not reflow the poem as ordinary prose.

### 4. Poem with line numbers

Use the Line Number Tools and the appropriate poetic structure rather than typing the numbers as ordinary text.

### 5. Deep list

Treat the entire section as one nested list. The deepest branch determines the list-level margin scheme for the section.

### 6. Mixed sidebar

Preserve the distinction between the vocabulary heading and its definitions. The sidebar's print appearance does not automatically determine its braille style.

### Core principle

**Ask what the print structure means before deciding how to encode it.**

---

## Key takeaways

- Box and Full Box set visually-distinct print material (sidebars, call-outs) apart in braille as their own container style.
- Play styles handle the specific repeating structure of scripts — character names, dialogue, and stage directions — as their own distinct elements.
- Poetic Stanza preserves meaningful line breaks in poetry, and is the correct container to use (instead of Prose) when applying Line Numbers to poetry.
- BrailleBlaster's List styles extend well beyond the handful of levels shown by default, supporting genuinely deep outline structures — but deep visual indentation in a source document doesn't automatically mean deep logical nesting is warranted in the braille.
- Applying any specialized style follows the same basic workflow as [Lesson 4](04-layout-styles.md)'s styles; consult the built-in Style Appendix for the specific margin rules of a style you're using for the first time.

---

## Source Citations

- BrailleBlaster current documentation — formatting styles, poetry styles, line numbering, and nested lists.
- *Braille Formats 2016* — provisions for lists, poetry, plays, and special material.
- BrailleBlaster User Manual — line numbering and formatting styles.
