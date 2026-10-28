# Lesson 4: Applying Layout Styles

> **Lesson at a glance**
>
> - **Unit:** Unit 1: Universal Lessons
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 1](01-navigating-the-interface.md), [Lesson 3](03-typeface-emphasis.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Explain the difference between emphasis (character level) and styles (block level).
- Apply the core style families: Body Text, headings, lists, and block or box styles.
- Read the Breadcrumbs bar to see every style wrapping the text at the cursor.
- Use Repeat Last Style and Unwrap Element to work faster and recover from mistakes.
- Say why you choose what a block of text *is* instead of typing margins by hand.

## Why this matters

[Lesson 3](03-typeface-emphasis.md) was about how individual words look. **Styles** are about how whole blocks of text are laid out on the braille page: their margins, their spacing, whether they start a new line, and how they behave when they cross a page break. If emphasis is the "font" of braille, styles are the "paragraph formatting," and they matter more, because braille margins are a reader's main navigation cue. A misapplied style does not just look wrong. It can make a document genuinely hard to read by finger.

This lesson teaches the idea behind every style you will apply for the rest of the course. [Lesson 5](05-heading-levels.md) and [Lesson 6](06-list-formatting.md) then go deep on headings and lists.

---

## How to use this lesson

Read **The Concept** and **Step by Step**, then work through the practice at the end. Keep the **Breadcrumbs** bar visible the whole time. It is the single best tool for understanding what BrailleBlaster thinks your text *is*.

---

## The Concept

### You choose what the text is; BrailleBlaster chooses the margins

Every block of text in a BrailleBlaster document has exactly one style at a time. Styles in BrailleBlaster are **contextual**: the same style name can behave a little differently depending on where it sits in the document, because the underlying rules come from *Braille Formats 2016*, the formatting standard published by the Braille Authority of North America (BANA).

You do not set margins by typing numbers. In the normal case you choose a style, and BrailleBlaster applies the correct BANA-compliant margins for you. A word-processor habit to unlearn: you are not deciding how text *looks*, you are telling BrailleBlaster what kind of thing the text *is* (a heading, a list, a quotation), and the correct look follows from that.

### Emphasis versus styles

- **Emphasis** works at the character level: bold, italics, underline, and the other typeforms in [Lesson 3](03-typeface-emphasis.md).
- **Styles** work at the paragraph or block level: margins, spacing, and page-break behavior.

### The core style families

- **Body Text** is the default. Indented paragraphs with 3-1 margins: the first line begins in cell 3 and runover lines begin in cell 1. Plain pasted text becomes Body Text automatically.
- **Headings** come in several levels, such as centered headings and cell-5 headings, each with its own BANA-defined spacing before and after. See [Lesson 5](05-heading-levels.md).
- **Lists** are for enumerated or bulleted print lists. List styles carry their own margin pairs and can be nested. See [Lesson 6](06-list-formatting.md).
- **Block and Box styles** are for material that is set off in print, such as sidebars and call-out boxes, and needs to be set off in braille too. See [Lesson 18](18-advanced-formatting.md).

### Containers and Breadcrumbs

Some styles act as **containers**. List, Poetry, and Box styles are examples. A container holds several elements together as one unit.

Containers are invisible in the Print View. They only show up in the **Breadcrumbs** bar, which lists every style wrapping the text at your cursor, outermost container first and most specific style last, like a trail leading back to exactly where you are in the document's structure. A container-level style is prefixed with the word **CONTAINER**, and selecting it selects every element in that container at once.

---

## Step by step

**Turn on Breadcrumbs.** Go to **View > Toggle Views > Breadcrumbs**. Leave them on for the whole lesson.

**Apply a style:**

1. Place the cursor inside the element, or highlight a run of elements, that you want to restyle.
2. Go to **Styles** and choose the style, or click its button on the Styles toolbar.
3. The style is applied immediately. Check the **Style View** (usually docked at the left of the window) or the **Breadcrumbs** bar to confirm.

**Repeat the last style.** This is the fast way to format a long run of similarly structured material, such as a glossary or a list of practice problems:

1. Place the cursor in the next element.
2. Go to **Styles > Repeat Last Style** or press `Ctrl+R`.

**Remove a container style** without replacing it with another one:

1. With Breadcrumbs visible, click on the element you want to affect.
2. Click the container button for that element in Breadcrumbs to select it.
3. Go to **Tools > Unwrap Element**.

Unwrap Element removes List, Poetic Stanza, Box, Full Box, and Prose styles and returns the text to Body Text with 3-1 margins. If Unwrap Element is greyed out, the current selection is not one of those container styles. Apply a different style directly instead.

**Change how many style levels you see.** Some styles, such as headings and lists, have numbered levels. BrailleBlaster shows five by default but supports up to eight. Go to **Styles > Configure > Style Levels** and choose the number that fits the document. A heavily nested textbook chapter may need more than the default five.

> [!NOTE]
> If a style does not seem to give the margins you expect, do not fix it by typing spaces or numbers. Look it up in the **Style Appendix** under **Help**, which gives the margins and spacing for each style, and check Breadcrumbs to confirm which style is really applied.

---

## Worked Demonstration

Take a short print excerpt with a heading, two paragraphs of body text, and a three-item bulleted list.

1. Paste the raw text. It lands entirely in Body Text.
2. Select the heading line and apply the appropriate heading style.
3. Leave the two paragraphs as Body Text. That is already correct.
4. Select the three list lines and apply a List style. In Breadcrumbs, notice the **CONTAINER** label wrapping all three lines as one unit.
5. Apply the list style to the first item, then use `Ctrl+R` on the second and third items to see how much faster Repeat Last Style is for uniform material.

---

## Practice Document

Copy the block below into a new BrailleBlaster document. Every line pastes in as Body Text. The **Print Source Legend** below tells you what each part looked like in print. Do not look for formatting in the block itself. Plain text carries none, which is the point.

```text
The Water Cycle

Water moves continuously between the oceans, the air, and the land. This movement is called the water cycle.

Three Main Stages

The cycle has three main stages. Each one is described below.

Evaporation
Condensation
Precipitation

Key idea: The sun supplies the energy that drives every stage of the cycle.
```

### Print Source Legend

| Text                                                    | Appearance in print                                     |
| ------------------------------------------------------- | ------------------------------------------------------- |
| "The Water Cycle"                                       | Chapter title, the highest-level heading                |
| "Three Main Stages"                                     | Section heading, one level below the chapter title      |
| The two sentences under the title and the section title | Ordinary paragraphs                                     |
| "Evaporation", "Condensation", "Precipitation"          | A bulleted list of three short items                    |
| "Key idea: ..."                                         | A sentence inside a shaded box, set off from the text   |

### Tasks

1. Apply a heading style to each of the two headings. For this lesson, give the chapter title the top heading level and the section title the next level down. [Lesson 5](05-heading-levels.md) explains exactly how print levels map to braille heading styles.
2. Leave the two ordinary paragraphs as Body Text.
3. Apply a List style to the three list items. Apply it to the first, then use Repeat Last Style on the other two.
4. Apply a Box style to the "Key idea" sentence.
5. With Breadcrumbs on, place the cursor at three points and write down the full trail you see at each: (a) in the chapter title, (b) in "Condensation," (c) in the "Key idea" sentence.
6. Select the list container in Breadcrumbs and use **Tools > Unwrap Element**. Describe what happens to the three items. Then undo it.

### Answer Key

1. Chapter title: the top heading level. Section title: the next level down. BrailleBlaster applies the BANA spacing for you, so no spaces or blank lines should be typed.
2. The two paragraphs are already Body Text, with 3-1 margins, so no action is needed. Leaving them alone is a correct answer.
3. All three items sit in one **List** container. After you style the first, Repeat Last Style (`Ctrl+R`) styles the next two in one keystroke each.
4. The "Key idea" sentence takes a Box style and sits inside a **Box** container.
5. Expect (a) a heading style with no container, (b) the **CONTAINER** list entry first, then the specific list item style, and (c) the **CONTAINER** box entry first, then the box's content style. The exact wording of each entry depends on your version. What matters is that the container appears first, which shows structure that the Print View never displays.
6. After **Unwrap Element**, the three items return to Body Text with 3-1 margins. They are no longer a list. This confirms that Unwrap Element is the quick way back to plain text from any container style.

**A note on judgment.** The box in this passage is a plain sentence. A transcriber would first ask whether the print really sets the text off, and whether the reader needs to know that. If the box were purely decorative, plain Body Text could be the better choice. Styles describe structure, not decoration. See [Lesson 18](18-advanced-formatting.md).

---

## Key takeaways

- Styles control paragraph-level layout (margins, spacing, page-break behavior). Emphasis controls character-level typeform.
- Styles are contextual and BANA-compliant. You choose *what the text is*, and BrailleBlaster works out the correct margins.
- Breadcrumbs show every style wrapping the current text, with container-level styles (List, Poetry, Box) called out explicitly.
- **Tools > Unwrap Element** is the fast path back to plain Body Text from any container style.
- Repeat Last Style (`Ctrl+R`) is the efficient way to format long runs of parallel material.
- Ask whether the print is doing something structural before reaching for a List or Box style. A run of short sentences that merely *look* list-like is not a list.

---

## Source Citations

- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, available at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html). It is the standard behind BrailleBlaster's styles.
- BrailleBlaster User Guide, sections on Styles, the Style View, and Breadcrumbs, at [brailleblaster.org/docs](https://brailleblaster.org/docs).
