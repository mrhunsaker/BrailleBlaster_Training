# Lab 9: Special Structures Studio

**Time:** about 75 minutes. **Needs:** [Lessons 6](../lessons/06-list-formatting.md) and [18](../lessons/18-advanced-formatting.md). **Files:** `play-excerpt.txt`, `original-poem.txt`, and `deep-list.txt` from the [sample files](../samples/index.md).

## Scenario

Plays, poems, and deep outlines look different in print because their *structure* carries meaning: who is speaking, where a line ends, which item sits under which. In braille the appearance changes, but the structure must not. You will format all three and then explain each choice.

## Part 1: The play

Open `play-excerpt.txt`.

1. Decide what each kind of line *is*: the title and act heading, stage directions, speaker names, speaker directions in parentheses, and dialogue.
2. Check the play styles in the style specification tables (Appendix A of the User Guide), and choose the styles. Apply them.
3. Look at the two stage directions. Are they the same kind of thing as the speaker directions in parentheses?
4. Check the Braille View. Can a reader tell who is speaking at each point, and can they tell a stage direction from dialogue?

**Expected observations.** Each dialogue block should be recognizable as a unit, with the speaker's name distinct from the speech. A spoken line should not be confused with a stage direction.

## Part 2: The poem

Open `original-poem.txt`.

1. Poems depend on **line breaks** and **stanzas**. Find the Poetry styles in the style specification tables.
2. Apply a poetry line style to each line, and wrap each stanza in a stanza container.
3. Check Breadcrumbs. You should see the **CONTAINER** entry for each stanza.
4. Format the title and the author line.
5. Check that every line starts on its own braille line, and that the blank line between stanzas survived.

> [!TIP]
> If a line is too long for the braille page, it must wrap. A poem's runover lines are formatted differently from a paragraph's. Look at how BrailleBlaster treats a wrapped poem line, and check your agency's rule.

## Part 3: The deep outline

Open `deep-list.txt`.

1. Count the nesting levels. The outline has four.
2. The numbers (1., 1.1, 1.1.1) are **typed text** in this file. Decide whether to keep them, as the print has them, or to rely on list markers. Explain your choice.
3. Apply list styles level by level, using the **Lists loadout** (`Ctrl+Shift+L`, then `Alt+1` to `Alt+8` for each level) or Repeat Last Style.
4. If you need more or fewer levels in the style menu, adjust **Styles > Configure > Style Levels**. The default is five and the maximum is eight.
5. Check the Braille View for a consistent runover at each level.

## Part 4: Explain your choices

For each structure, write one sentence for a hypothetical transcriber who will proofread your work:

- "I treated ______ as ______ because ______."

## Debrief questions

1. In which structure was it hardest to decide what each line *was*?
2. What would a student lose if the poem were formatted as ordinary paragraphs?
3. Where did the style specification tables save you from guessing?
4. How do you know when a "box" is a real box in print and not merely a bordered table or a shaded note?
