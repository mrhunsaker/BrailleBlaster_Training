# Lesson 6: Applying List Formatting

> **Lesson at a glance**
>
> - **Unit:** Unit 1: Universal Lessons
> - **Suggested time:** about 90 minutes
> - **Prerequisites:** [Lesson 4](04-layout-styles.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Format simple lists with BrailleBlaster list styles.
- Apply the margin formula for nested lists.
- Explain why runover lines sit two cells past the deepest level in use.
- Format a list that is eight levels deep and check it against the answer key.

---

## How to use this lesson

The first half explains the concept and gives you the margin formula for nested lists at any depth. The second half is a practice document — six separate lists, each preceded by a line telling you **how many levels deep** it should be, but not which specific lines belong at which level. That's the part you determine from the wording and structure of the content itself, exactly as you would from a Word document where indentation is inconsistent or missing. Nothing in the practice lists uses Markdown bullets, dashes, or indentation — every list item is a plain line of text. Everything else in this document is already correct; you are only fixing list depth and margins.

---

## The Concept

### Simple lists

A list with no subentries is a **simple list**. Per §8.3.1, use **1-3 margins**: the first line of each item begins in cell 1, and any runover (a long item that wraps to a second braille line) begins in cell 3. A simple list is normally preceded and followed by a blank line (§8.3.2a) — except when it directly follows a cell-5 or cell-7 heading, in which case no blank line is inserted before it (§8.3.3a).

### Nested lists — the margin formula

A **nested list** is a list within a list: it has main entries and at least one level of subentries (§8.5.1). The margin rule, stated in §8.5.1(b), is simple and completely regular:

> The main entry begins in cell 1. Each subentry level begins two cells to the right of the previous level. **All runovers begin two cells to the right of the farthest indented subentry** — the same runover cell is shared by every level in that list.

This gives a clean formula. For a list nested **n** levels deep:

- Level *k*'s first line begins in cell **(2k − 1)**
- **Every** level's runover begins in cell **(2n + 1)**

| Depth    | Margins (first line–runover, cell by cell)        |
| -------- | ------------------------------------------------- |
| 1 level  | 1-3                                               |
| 2 levels | 1-5, 3-5                                          |
| 3 levels | 1-7, 3-7, 5-7                                     |
| 4 levels | 1-9, 3-9, 5-9, 7-9                                |
| 5 levels | 1-11, 3-11, 5-11, 7-11, 9-11                      |
| 6 levels | 1-13, 3-13, 5-13, 7-13, 9-13, 11-13               |
| 7 levels | 1-15, 3-15, 5-15, 7-15, 9-15, 11-15, 13-15        |
| 8 levels | 1-17, 3-17, 5-17, 7-17, 9-17, 11-17, 13-17, 15-17 |

Notice that the runover cell for a shallow-level item **changes** depending on how deep the list eventually goes — a level-1 item's runover sits in cell 5 in a two-level list, but cell 17 in an eight-level list. This is why §8.5.1(c) requires that **all items within a section that contains subentries be treated as one nested list, even if some items at that level have no subentries of their own** — you can't mix margin systems partway through a single list.

### Why the runover is always two cells past the deepest level

Per the Braille Reader's Perspective note in §8.1.5, keeping the runover margin constant across every level (rather than giving each level its own separate runover position) means a reader can identify **how many levels deep the whole list goes** the moment they hit the *first* runover line — before they've read the whole list. That consistency is the entire point of the formula; it's worth more to the reader than saving a cell or two of margin on shallow items.

### Other list-level rules worth knowing

- Follow print for capitalization and punctuation of every item (§8.1.4).
- Nested lists are always transcribed in a **single column**, even if print showed them in side-by-side columns (§8.5.1d).
- Bulleted subentries are transcribed as a nested list, using the same margin formula (§8.6.2c).
- Outlines (Roman numeral / letter / number outlines) use the identical nested-list formula (§8.8.1) — an outline is not a different structure, just a nested list with a particular labeling convention.

### Worked demonstration (small, fully correct)

Print source:

```
Mammals
  Dogs
  Cats
Reptiles
  Snakes
  Lizards
```

This is a two-level nested list. Per the formula: Level 1 ("Mammals", "Reptiles") = margin 1-5; Level 2 ("Dogs", "Cats", "Snakes", "Lizards") = margin 3-5. In BrailleBlaster, this means applying the **List** container style with **List Level 2a** to "Mammals" and "Reptiles," and **List Level 2b** to the four animal names nested beneath them — not typing manual spaces to fake the indentation. If you accidentally apply **List Level 1** instead of **List Level 2a**, as soon as you apply **List Level 2b** later on to an adjacent line, the program will correct the list so it is all on **List Level 2**.

---

## Practice Document

Each list below is preceded by its **target depth**. Read the item wording carefully — the nesting is implied by the content, not shown visually. Apply BrailleBlaster's List style at the correct level for every line, using the margin formula above to double-check yourself once styles are applied (check the Braille View, not just the Print View).

### List 1

**Target structure:** simple list — no nesting (1 level)

```
Types of Rocks

- Igneous
- Sedimentary
- Metamorphic
```

### List 2

**Target structure:** 2-level nested list. Only some main entries have subentries — treat the whole section as one nested list per §8.5.1(c).

```
Kitchen Equipment Needed for This Recipe

- Mixing bowls
  - Large bowl for dry ingredients
  - Small bowl for wet ingredients
- Measuring cups
- Oven
  - Baking sheet
```

### List 3

**Target structure:** 3-level nested list (a basic biological classification)

```
Animal Groups Covered in This Unit
- Mammals
  - Carnivores
    - Lions
    - Wolves
  - Herbivores
    - Deer
    - Rabbits
- Reptiles
  - Snakes
  - Lizards
```

### List 4

**Target structure:** 4-level nested list (library classification scheme)

```
Fiction Section Organization

- Mystery
  - Cozy Mystery
  - Traditional
  - Culinary
  - Hardboiled
    - Noir
      - Neo-Noir
- Science Fiction
  - Space Opera
  - Military SF
  - Cyberpunk
    - Classic Cyberpunk
    - Post-Cyberpunk
```

### List 5

**Target structure:** 5-level nested list (school district organization)

```
Riverside School District Structure

- Elementary Schools
  - Oak Street Elementary
    - Kindergarten
      - Morning Session
      - Afternoon Session
    - Grade 1
- Middle Schools
  - Riverside Middle
    - Grade 6
    - Grade 7
      - Team A
        - Group 1
        - Group 2
      - Team B
```

### List 6 — Challenge: 8 levels deep

**Target structure:** 8-level nested list (full biological taxonomy for a single species — every rank present, in order)

```
Taxonomic Classification of selected Apes

- Domain: Eukarya
  - Kingdom: Animalia
    - Phylum: Chordata
      - Class: Mammalia
        - Order: Primates
          - Family: Hominidae
            - Genus: Pan
              - Species: *Pan troglodytes* 
              - Species: *Pan paniscus*
            - Genus: Gorilla
              - Species: *Gorilla gorilla*
            - Genus: Pongo
              - Species: *Pongo pygmaeus*
```

---

## Answer Key

**List 1** — simple list, 1-3 margin for all three items (no nesting).

**List 2** — 2-level list, margins 1-5 / 3-5.
- Level 1: "Mixing bowls," "Measuring cups," "Oven"
- Level 2: "Large bowl for dry ingredients," "Small bowl for wet ingredients," "Baking sheet"
- Note: "Measuring cups" and "Oven" have no subentries of their own, but per §8.5.1(c) they still take Level 1 formatting because they're part of a section that contains nested items.

**List 3** — 3-level list, margins 1-7 / 3-7 / 5-7.
- Level 1: "Mammals," "Reptiles"
- Level 2: "Carnivores," "Herbivores" (under Mammals), "Snakes," "Lizards" (under Reptiles)
- Level 3: "Lions," "Wolves" (under Carnivores), "Deer," "Rabbits" (under Herbivores)

**List 4** — 4-level list, margins 1-9 / 3-9 / 5-9 / 7-9.
- Level 1: "Mystery," "Science Fiction"
- Level 2: "Cozy Mystery," "Hardboiled," "Space Opera," "Cyberpunk"
- Level 3: "Traditional," "Culinary," "Noir,"  "Military SF," "Classic Cyberpunk," "Post-Cyberpunk"
- Level 4: "Neo-Noir," *(This is a reminder that a list's stated maximum depth is the deepest branch reached anywhere in it — not every branch has to reach that depth, per §8.5.1(c)'s "even if some items do not have a subentry.")*

**List 5** — 5-level list, margins 1-11 / 3-11 / 5-11 / 7-11 / 9-11.
- Level 1: "Elementary Schools," "Middle Schools"
- Level 2: "Oak Street Elementary," "Riverside Middle"
- Level 3: "Kindergarten," "Grade 1," "Grade 6," "Grade 7"
- Level 4: "Morning Session," "Afternoon Session," "Team A," "Team B"
- Level 5: none reached under Grade 1/6 in this particular list — same principle as List 4.

**List 6 (challenge)** — 8-level list, margins 1-17 / 3-17 / 5-17 / 7-17 / 9-17 / 11-17 / 13-17 / 15-17. Because every rank in a taxonomy is a single, unbranching chain down to the species, this list has exactly one item at each of the eight levels: 
- Level 1: Domain (1-17)
- Level 2: Kingdom (3-17)
- Level 3: Phylum (5-17)
- Level 4: Class (7-17)
- Level 5: Order (9-17)
- Level 6: Family (11-17)
- Level 7: Genus (13-17)
- Level 8: Species (15-17), all sharing runover cell 17.

---

## Source Citations

- *Braille Formats 2016*, §8 Lists — §8.1 (Fundamentals, including §8.1.4–§8.1.5), §8.3 (Simple Vertical Lists), §8.5 (Nested Lists, especially §8.5.1's margin formula and its sub-rules), §8.6 (Bulleted Lists), §8.8 (Outlines).
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, available at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html).

*Margin figures for one through four levels are quoted directly from §8.5.1(b); figures for five through eight levels are this document's extension of that same explicitly stated formula, verified against the BANA online edition at brailleauthority.org.*
