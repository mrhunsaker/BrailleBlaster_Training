# Lesson 31: Glossaries and Indexes

> **Lesson at a glance**
>
> - **Unit:** Unit 4: Specialized Content
> - **Suggested time:** about 90 minutes
> - **Prerequisites:** [Lesson 3](03-typeface-emphasis.md), [Lesson 4](04-layout-styles.md), [Lesson 13](13-paper-size-and-embossers.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Apply the Glossary and Index styles for the correct number of levels.
- Work out the margins for each level, and check them in the Braille View.
- Remove emphasis from alphabetic-reference entry words, and explain why *Braille Formats 2016* asks for that.
- Describe what guide words are and why they must be handled last.
- Recognize which Alphabetic Reference tools are experimental in 3.x.

## Why this matters

Glossaries and indexes are **alphabetic references**: readers look things up in them. A braille reader finds an entry by feel, so the format must be absolutely consistent: where each entry begins, how the definition wraps, how sub-entries sit under their parents. In print, the entry words are often bold or italic, but *Braille Formats 2016* tells transcribers to **ignore such font attributes** in these sections unless they are needed for distinction, such as a foreign word or a book title.

BrailleBlaster supplies styles for the layout, and a tool for removing the emphasis.

---

## How to use this lesson

Read **The Concept**, then work the practice. The tools for guide words are experimental in the 3.x releases, so this lesson shows you the idea and the safe path, and keeps the hands-on work to the documented styles.

---

## The Concept

### Styles by number of levels

BrailleBlaster's **Glossary** and **Index** styles are in submenus based on how many **levels** the reference has. Each style name starts with *Glossary* or *Index*, then the number of levels, then a **letter** for the level within it.

| Style | What it is | Margins |
| ----- | ---------- | ------- |
| Glossary 1 | A glossary with 1 level | 1-3 |
| Glossary 2a | First level in a glossary with 2 levels | 1-5 |
| Glossary 2b | Second level in a glossary with 2 levels | 3-5 |
| Glossary 5d | Fourth level in a glossary with 5 levels | 7-11 |
| Glossary 5e | Fifth level in a glossary with 5 levels | 9-11 |

The **Index** styles have the same names and the same margins (Index 1, Index 2a, 2b, and so on).

### Reading the margins

Margins are written *first line* **-** *runover*. Glossary 1 is **1-3**: the entry's first line starts in cell 1, and any runover lines start in cell 3.

The rows in the table follow a pattern. In a reference with **N levels**:

- the *first line* of level **k** (where *a* is 1) starts in cell **2(k − 1) + 1**;
- the *runover* of every level is cell **2N + 1**.

Check it against the table: for 2 levels, 2a is 1-5 and 2b is 3-5, and for 5 levels, 5d is 7-11 and 5e is 9-11. The pattern is a way to check your result. Treat the style specification tables in Appendix A of the User Guide as the authority for any style you have not seen.

### Where the term and definition are

Typically the **publisher** has already identified the term and the definition in the source file, so the term can be used as a **guide word** automatically. A reference built by hand from a flat Word document has no such information, so you provide it.

### Guide words

In a long alphabetic reference, braille pages often carry **guide words** at the top: the first and last entries on the page, so a reader can find the right page quickly. Because guide words depend on where the page breaks fall, they must be added **last**, after every formatting decision that could move text. A running head and guide words are skipped automatically by **Skip Number Lines** ([Lesson 26](26-controlling-the-page.md)).

> [!NOTE]
> In current 3.x builds, the **Alphabetic Reference** tools (such as **Identify Guide Word**, **Edit Guide Word**, and **Add/Remove Uncontracted Glossary Items**) are in the hidden **Debug** menu, which you show with `Ctrl+Shift+` `. The 3.x User Guide does not document them, so treat them as experimental and proofread every page they affect. The styles and the emphasis tool below are documented and safe to use.

---

## Step by step

### Apply a glossary or index style

1. Select the entries.
2. Open the **Styles** menu and choose **Glossary Styles** or **Index Styles**.
3. Choose the submenu for the number of levels, then the style for the level.
4. Check the margins in the Braille View.

### Remove emphasis from entry words

1. **Save your work first.** The guide advises it before this tool.
2. Make sure the glossary or index section already has its Glossary or Index style, because the tool works on sections designated that way.
3. Go to **Emphasis > Remove Emphasis from Alphabetic Reference Entry Words**.
4. Re-add emphasis by hand to any entry word that needs it, such as a foreign word or a book title.

The same menu has two related tools: **Remove All Emphasis from Headings** and **Remove All Emphasis from List Prefixes**. Save first for each.

---

## Worked Demonstration

```text
adjective: a word that describes a noun
adverb: a word that describes a verb, an adjective, or another adverb
clause: a group of words with a subject and a verb, which may or may not stand alone as a sentence
```

1. Paste the three entries and apply **Glossary 1** to all of them.
2. In the Braille View, check that each entry begins in cell 1 and that the runover of *clause* begins in cell 3.
3. Select the word *adjective*, press `Ctrl+B` for bold, and do the same for *adverb* and *clause*.
4. Save, then choose **Emphasis > Remove Emphasis from Alphabetic Reference Entry Words**. The bold on the entry words should be gone.

---

## Practice Document

### Print Source Legend

| Part | In print |
| ---- | -------- |
| Part A | A single-level glossary of five terms, with each entry word in bold |
| Part B | A two-level index, in which main entries have indented sub-entries |

```text
Part A
frond: the leaf of a fern or palm
habitat: the place where a plant or animal normally lives
larva: the early stage of an insect, after the egg and before the adult
nectar: the sweet liquid that flowers make to attract insects
spore: a tiny cell that some plants and fungi use to reproduce

Part B
birds, 12
    nests, 14
    migration, 22
fish, 30
    freshwater, 31
    saltwater, 33
```

### Tasks

1. Apply the single-level glossary style to Part A. State the margins that the table gives, and check them in the Braille View for *larva*, whose definition wraps.
2. Make the five entry words bold with `Ctrl+B`. Save. Remove the emphasis with the alphabetic-reference tool. Check the Braille View.
3. Decide the correct styles for Part B, and apply them. Which two styles do you use?
4. Use the pattern to say what margins the **Index 3b** style has.
5. A foreign word in a glossary has a bold, italic entry. What do you do after running the emphasis tool?
6. Why should guide words be added last?

### Answer Key

1. **Glossary 1**, with margins **1-3**: the first line of each entry in cell 1 and its runover in cell 3.
2. The bold on the entry words is removed. The guide's reason is that *Braille Formats 2016* says to ignore font attributes in these sections unless they are needed for distinction.
3. Part B has **two levels**, so use **Index 2a** for the main entries (birds, fish) with margins **1-5**, and **Index 2b** for the sub-entries with margins **3-5**.
4. With N = 3, level b is k = 2, so the first line is at 2(2 − 1) + 1 = **3**, and the runover is 2×3 + 1 = **7**. So Index 3b is **3-7**. Confirm against the style specification tables in Appendix A of the User Guide.
5. Re-apply emphasis by hand to that entry word if the foreign-word distinction is needed. The tool removes emphasis from *all* entry words in the section, so you must restore any that need it.
6. Guide words come from the first and last entries on each *braille page*. Any change to margins, headings, or page breaks can move entries to a different page, and the guide words would then be wrong.

---

## Key takeaways

- **Glossary** and **Index** styles are named by the number of levels (1 to 5 in the guide) and a letter for each level. Check margins in the Braille View.
- For N levels, each level's first line starts in cell 2(k − 1) + 1, and every runover is in cell 2N + 1.
- *Braille Formats 2016* says to ignore font attributes on entry words unless they are needed. **Emphasis > Remove Emphasis from Alphabetic Reference Entry Words** does it in one action. Save first, and restore the emphasis you need.
- Guide words depend on pagination, so add them last. The Alphabetic Reference tools are experimental in 3.x.

---

## Source Citations

- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/) and the source repository [github.com/aphtech/brailleblaster-docs](https://github.com/aphtech/brailleblaster-docs): "Glossary Styles," "Index Styles," and "Removing All Emphasis from Alphabetic Reference Entry Words."
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html).
