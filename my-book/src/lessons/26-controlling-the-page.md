# Lesson 26: Controlling the Page with Style Options

> **Lesson at a glance**
>
> - **Unit:** Unit 4: Specialized Content
> - **Suggested time:** about 2 hours
> - **Prerequisites:** [Lesson 4](04-layout-styles.md), [Lesson 5](05-heading-levels.md), [Lesson 13](13-paper-size-and-embossers.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Explain why Style Options exist and when a style alone is not enough.
- Set an exact starting cell with **Set Cell Position**, and keep text together with a **Line Break**.
- Keep elements on one braille page with **Don't Split**, and with the next element using **Keep With Next**.
- Control spacing with **Lines Before**, **Lines After**, and **Double Spaced**.
- Keep text off the top or bottom line with **Skip Number Lines**.
- Place material on facing pages with **Page Side**, and add blank pages with **New Pages Before** and **New Pages After**.

> [!TIP]
> **More practice:** use `reflow-paragraph.txt` from the [sample files](../samples/index.md) to fill several braille pages, so that page-break options have something to act on.

## Why this matters

A style gives an element the right margins and spacing for *its kind*. But real documents contain oddities that no preset style anticipates: a line that must start in a particular cell, a heading that must not be stranded at the bottom of a page, a table that must sit on facing pages in an interpoint volume, or a blank page that has to stay blank. **Style Options** are the tools for those cases.

The guide puts it plainly: there are many oddities in braille formatting, and they cannot all be covered by a predetermined style.

> [!IMPORTANT]
> Use a Style Option to solve a *specific* problem, after the right style is applied. Do not use options to rebuild a style by hand. If you find yourself applying the same options to every element of one kind, you probably need a different style.

---

## How to use this lesson

Read **The Concept** and **Step by step**, then work through the exercises in order. They build on one another, so keep the same practice document open throughout.

---

## The Concept

### Options adjust; styles define

A **style** defines an element: its margins, its spacing, whether it starts a new line. A **Style Option** adjusts one aspect of an element *without changing what it is*. The element stays a Body Text paragraph or a list item, with one rule added.

### Options and the page

Almost every option answers a question about the **braille page**, not the print page:

| Question | Option |
| -------- | ------ |
| Where does this line start? | Set Cell Position |
| Where does this line break, without starting a new element? | Line Break |
| Must these elements stay on one braille page? | Don't Split |
| Must this element stay with the next one? | Keep With Next |
| How many blank lines go before or after? | Lines Before, Lines After |
| Should this be double spaced? | Double Spaced |
| May this element use the top or bottom line, which carries page numbers? | Skip Number Lines |
| Must this appear on a left (even) or right (odd) page? | Page Side |
| Must a blank page come before or after? | New Pages Before, New Pages After |

### Why facing pages matter

In an **interpoint** volume, braille is on both sides of each sheet. A left page is an **even** page and a right page is an **odd** page. When a table, graphic, or set of answer choices must be seen across a spread, both pages have to face each other. A formatting change earlier in the document can shift text onto the wrong kind of page, so the instruction has to be attached to the element and not to a page number.

---

## Step by step

### Set your own starting cell

1. Place the cursor before the element you want to indent.
2. Go to **Edit > Set Cell Position**. A box opens.
3. Type the cell number where the text should start, and click **OK**.

If you type a number lower than the cell the text is on, the text drops to the next line and starts there. The command does not work if the cursor is at the end of a line, and it applies to **one line at a time**.

### Keep text on the same line, in the same element

Pressing Enter starts a **new element**, like a new paragraph. To drop text down without starting a new element:

1. Place the cursor where you want the break.
2. Go to **Edit > Line Break**, or press `Shift+Enter`.

The text moves to the next braille line and starts at the *runover* cell for the element's style. For Body Text, with 3-1 margins, the new line starts in cell 1.

### Keep elements together

- **Don't Split.** Highlight the elements to keep together, then go to **Styles > Options > Don't Split**. It is the only option that works across elements of *different* styles. If the selection is longer than one braille page, the extra text continues onto the next page.
- **Keep With Next.** Select the element, then go to **Styles > Options > Keep With Next**. If the next element moves to a new page because of later changes, this one moves with it. This is the usual fix for a heading stranded at the bottom of a page.

### Add blank lines and double spacing

- **Lines Before** and **Lines After.** Select the element, go to **Styles > Options**, choose the option, and enter a value. Every style that begins on a new line starts with a value of **1** for both. To get a blank line, use **2**. A Centered Heading already uses **2** before and **2** after, so for one extra blank line before it, enter **3**.
- **Double Spaced.** Highlight the elements and go to **Styles > Options > Double Spaced**.

### Keep text off the page-number lines

Go to **Styles > Options > Skip Number Lines** and choose:

- **Top:** the element may not appear on the top line of the braille page.
- **Bottom:** it may not appear on the bottom line.
- **Both:** it skips both.
- **None:** removes the other settings.

The choice applies immediately. A running head and guide words are always skipped automatically, even when **None** is chosen.

### Create facing pages

1. Select the element.
2. Go to **Styles > Options > Page Side**.
3. Choose **Left** (an even page) or **Right** (an odd page).

If the text is already on that kind of page, it stays. If not, it moves to the next page of the chosen kind. The setting travels with the element, so it keeps working after later changes.

### Add blank pages

If the side of the page does not matter and you only need a blank page:

1. Select the element and go to **Styles > Options**.
2. Choose **New Pages Before** or **New Pages After**.
3. The element, or the text after it, moves to a new page. Then press `Ctrl+Enter` before or after the element to add the blank page.

If the blank page exists so that material *faces* other material, use **Page Side** instead, because it keeps them facing.

---

## Worked Demonstration

1. Paste `reflow-paragraph.txt` into a new document and apply a heading style to a short title line you type above it.
2. Open the **Braille Preview** (`Alt+Home`) and note where the page breaks fall.
3. Put the cursor before the first word of the paragraph and use **Edit > Set Cell Position**, entering **9**. Look at the Braille View. Then try typing **2**, and notice the drop to the next line.
4. Add a **Line Break** (`Shift+Enter`) in the middle of the paragraph. Note the cell where the new line starts.
5. Add enough copies of the paragraph that the heading falls near the bottom of a page, then apply **Keep With Next** to the heading and see what moves.
6. Select the heading and set **Lines Before** to **3**. Compare the blank lines in the Braille View.

---

## Practice Document

Use a fresh document. Paste three copies of the paragraph from `reflow-paragraph.txt`, separated by short headings you type: *Part One*, *Part Two*, *Part Three*. Apply a heading style to each. Add four short lines at the end that you will style as a list.

### Tasks

1. Place the cursor at the start of the second paragraph and set its first line to start in cell **7** with **Set Cell Position**. What happens to the runover lines?
2. Insert a **Line Break** in the middle of the first paragraph. Where does the second part start, and why?
3. Select the four list lines and apply **Don't Split**. How can you test that the option works?
4. Apply **Keep With Next** to *Part Two*. Add or remove text above it until that heading would fall at the bottom of a page. What do you observe in the Braille Preview?
5. Set **Lines Before** to **3** on *Part Three*. Compare it with *Part One*. How many blank lines separate each heading from the text above?
6. Apply **Skip Number Lines: Top** to the first line of the second paragraph. Describe what could change.
7. In an interpoint document, set **Page Side: Right** on *Part Three*. Confirm in the Braille Preview that it begins on an odd (right) page.
8. Apply **New Pages After** to the list. Add `Ctrl+Enter` after it. What is the result?

### Answer Key

1. Only the **first line** is moved to cell 7. Set Cell Position applies to a single line, so the runover lines return to the style's runover margin (cell 1 for Body Text). Do not use this to indent a whole paragraph.
2. The second part begins on the next braille line **in the runover cell of the style**, which is cell 1 for Body Text. A Line Break does not start a new element, so the style's runover margin applies and the element stays one paragraph.
3. Make the list long enough or place it near the bottom of a page, so that without the option it would split across two pages. With **Don't Split**, the whole selection moves to the next page together, unless it is longer than a page.
4. When *Part Two* would otherwise be the last line on a page, **Keep With Next** carries it to the next page with the element that follows it, so the heading is never stranded.
5. A **Lines Before** value of 1 means no blank line, and a value of 2 means one blank line, so the number of blank lines is the value minus one. A Centered Heading already has a value of 2 before it, which is one blank line, so *Part One* and *Part Two* have one blank line above them. *Part Three* with a value of 3 has **two** blank lines above it.
6. The first line of that paragraph will not be placed on the top line of a braille page. If it would have landed there, it moves down, so the paragraph may shift to a different line. It is meant for lines that must not collide with page-number text.
7. Page Side Right means an **odd** page. If the heading was already on an odd page, it stays. If not, it moves to the next odd page, and an even page may be left blank. Interpoint matters because only then do left and right pages face.
8. **New Pages After** moves the text after the list onto a new page, and `Ctrl+Enter` after the list adds a blank page. If the blank page is only there to make something face something else, **Page Side** would have been the better tool.

---

## Key takeaways

- A **style** defines an element. A **Style Option** adjusts one aspect of it for the braille page. Apply the right style first.
- **Set Cell Position** moves one line. **Line Break** drops text to the next line without starting a new element.
- **Don't Split** keeps a group together. **Keep With Next** keeps an element with the one after it.
- **Lines Before** and **Lines After** start at 1. Use 2 for a blank line.
- **Page Side** is for facing pages in interpoint work. **New Pages Before** and **After** are for blank pages when the side does not matter.
- Check every option in the **Braille Preview**, because only the preview shows the real page breaks.

---

## Source Citations

- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/) and the source repository [github.com/aphtech/brailleblaster-docs](https://github.com/aphtech/brailleblaster-docs): "Using Style Options" (setting your own margin, keeping text on the same line and page, Keep With Next, blank lines, double lines, Skip Number Lines, facing pages, and blank pages).
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html).
