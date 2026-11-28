# Lesson 35: Word: Building Structure with Styles

> \*\*Lesson at a glance\*\*
>
> - \*\*Unit:\*\* Unit 5: Handbook (Supplemental)
> - \*\*Suggested time:\*\* about 2 hr 30 min
> - \*\*Prerequisites:\*\* [Lesson 33](33-what-makes-a-good-source.md)
> - \*\*You will need:\*\* A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Apply real heading, list, and other styles in Word using the keyboard.
- Inspect any Word file to find out whether its structure is real or only looks real.
- Prepare a Word file for BrailleBlaster, using the rules that prevent loss.
- Use the special style names BrailleBlaster recognizes: margin styles, empty paragraphs, and list styles.
- Export a clean `.docx`.

> [!TIP]
> \*\*Practice files:\*\* `word-01-well-structured.docx`, `word-02-flat-structure.docx`, and `word-05-braille-aware-styles.docx` in the [sample files](../samples/index.md).

> [!CAUTION]
> Do not make text look like a heading by changing its font size or boldness alone. Apply the actual semantic heading style; visual formatting is not reliable structure for navigation, conversion, or braille heading assignment.

## Why this matters

Word is the most common source BrailleBlaster sees, and the one with the widest gap between *looking* right and *being* right. Two Word files can print identically while one carries real structure and the other carries none. The keyboard commands and checks in this lesson let you build structure in one pass, and see through a file that only pretends to have it. They are also what you would teach a teacher or author who sends you files.

{HB}

---

## How to use this lesson

Read **The Concept**, then keep the **shortcut tables** and the **inspection checklist** at hand. The practice uses the three sample files.

> [!NOTE]
> Shortcuts are for \*\*Word on Windows\*\*. The Mac versions differ in several places, and Word's menus change between releases. Where a Mac key is well established it is listed, and otherwise check Word's own keyboard shortcut list.

---

## The Concept

### Styles are the structure

In Word, a **paragraph style** says what a paragraph *is*: Heading 1, List Bullet, Quote, Normal. A **direct format** says only what it *looks like*: bold, 16 point, indented. BrailleBlaster, through Pandoc, can see styles. It can see direct bold and italic. It cannot guess that a bold 16-point line is a heading.

So the single most useful habit is **apply a style and never fake one**. A chapter title is Heading 1 whatever it looks like, and a bullet is a list item, not a typed character.

### What BrailleBlaster does with Word styles

BrailleBlaster reads `.docx` files with Pandoc's *styles* option turned on. That means the **style names** reach BrailleBlaster's conversion script. These results come from running the script on test files:

| Word style or feature | Result in BrailleBlaster |
| --------------------- | ------------------------ |
| Heading 1 | **Centered Heading** |
| Heading 2 | **Cell 5 Heading** |
| Heading 3 to Heading 6 | **Cell 7 Heading** (all the same) |
| **Title** | **Not a heading.** Ordinary body text |
| Normal and most others | Body Text |
| **Quote** | Displayed Blocked Text |
| List Bullet, List Number | A list, with the bullet or number typed in as text |
| **List Paragraph**, **List**, **List 2** to **List 9**, **List Continue** to **List Continue 9** | A list item |
| A style named like **`3-1`**, **`1-3`**, **`5-7`**, or **`7-5`** | The braille **margins** you named |
| **BB Empty Paragraph** | A blank line |
| A real **Ctrl+Enter page break** | A page break |
| A paragraph with no text | An empty paragraph, kept |
| Bold, italic, underline (direct or by character style) | Bold, italics, underline |
| A **Word equation** | Math |
| **Tracked changes** | Insertions are accepted and deletions removed |
| A real **footnote** | A superscript number and a "Footnotes" section at the end |
| A **picture alone in its paragraph**, with a caption | **Dropped, with the caption** |
| A **picture inside a line of text** | Kept, with its alt text |

> [!IMPORTANT]
> The last two rows are the dangerous ones. Set every picture to \*\*In Line with Text\*\*, put it in a paragraph with some text, and check the figure count after import.

### Margin style names

A style whose **name** is two odd numbers joined by a hyphen sets the braille margins directly: the first number is the **first-line cell** and the second is the **runover cell**. The script accepts the name only if both numbers are odd, both are 11 or less, and the runover is not more than two cells before the first line. So `3-1`, `1-3`, `5-7`, `7-5`, and `1-1` work, but `2-4` and `13-1` do not.

You create the style in Word like any other, and name it exactly. This is rarely needed. Use it for something unusual, such as a block with margins no ordinary style gives.

---

## Keyboard shortcuts for structure

### Applying styles

| Action | Windows | Mac |
| ------ | ------- | --- |
| Heading 1, 2, 3 | `Ctrl+Alt+1`, `Ctrl+Alt+2`, `Ctrl+Alt+3` | `Cmd+Option+1`, `2`, `3` |
| Normal | `Ctrl+Shift+N` | `Cmd+Shift+N` |
| Apply Styles box (type a style name) | `Ctrl+Shift+S` | |
| Open the Styles pane | `Alt+Ctrl+Shift+S` | |
| List Bullet style | `Ctrl+Shift+L` | |
| Reset paragraph formatting | `Ctrl+Q` | |
| Reset character formatting | `Ctrl+Space` | |

### Emphasis, breaks, and special characters

| Action | Windows |
| ------ | ------- |
| Bold, italic, underline | `Ctrl+B`, `Ctrl+I`, `Ctrl+U` |
| Page break | `Ctrl+Enter` |
| Line break inside a paragraph | `Shift+Enter` |
| Non-breaking space | `Ctrl+Shift+Space` |
| Non-breaking hyphen | `Ctrl+Shift+Hyphen` |

### Notes and math

| Action | Windows | Mac |
| ------ | ------- | --- |
| Footnote | `Ctrl+Alt+F` | `Cmd+Option+F` |
| Endnote | `Ctrl+Alt+D` | |
| Insert an equation | `Alt+=` | |

### Seeing and checking

| Action | Windows | Mac |
| ------ | ------- | --- |
| Show formatting marks | `Ctrl+Shift+8` | `Cmd+8` |
| Reveal Formatting (what style, what direct format) | `Shift+F1` | |
| Navigation Pane (the heading outline) | `Ctrl+F` | |
| Find and Replace | `Ctrl+H` | |
| Turn tracked changes on or off | `Ctrl+Shift+E` | |

---

## Inspecting a file you were sent

A file is **well built** if the structure can be *seen* by Word's own tools. Use these checks, in order.

1. **Navigation Pane.** Press `Ctrl+F` and choose the **Headings** tab. If the headings you expect are listed, they are real. If it is empty, none are.
2. **Styles pane.** Click in several paragraphs and watch the style name. Bold text that says "Normal" is a fake heading.
3. **Formatting marks.** Press `Ctrl+Shift+8`. Look for **typed bullets**, **runs of spaces**, **empty paragraphs used as spacing**, and **tabs used to indent**. These are all signs of direct formatting.
4. **Reveal Formatting.** Press `Shift+F1` and click a paragraph to see exactly what is applied.
5. **Find by style.** In **Find and Replace**, open **More > Format > Style** to find every paragraph in one style. This also reveals a style used inconsistently.
6. **Selection Pane.** On the **Home** tab, choose **Select > Selection Pane** to list floating objects. **Text boxes**, shapes, and floating pictures are the ones most likely to be missed or scrambled.
7. **Check Accessibility.** On the **Review** tab, choose **Check Accessibility**. It reports missing alt text, empty headings, and tables without headers.
8. **Inspect Document.** Under **File > Info > Check for Issues**, choose **Inspect Document** to find hidden text, comments, and tracked changes.

---

## Step by step

### Prepare a Word file for BrailleBlaster

1. **Save a copy** with a new name.
2. **Accept or reject tracked changes** you do not want. (BrailleBlaster accepts insertions and removes deletions, but make the decision yourself.)
3. **Apply real styles.** Select each fake heading and apply a Heading style. Select each list and apply a list style, and delete typed bullets.
4. **Remove layout tricks.** Delete runs of spaces, tabs used to indent, and empty paragraphs used as spacing. Change the paragraph's style instead.
5. **Set every picture In Line with Text**, in a paragraph with text. Add **alt text**: right-click the picture and choose **View Alt Text**.
6. **Type equations** with `Alt+=`, and not as pictures.
7. **Replace a text box** with an ordinary paragraph. Move its text to where it belongs in the reading order.
8. **Run Check Accessibility** and fix what it finds.
9. **Save as `.docx`**. Avoid the old `.doc` format.

### Use a margin style on purpose

1. Open the Styles pane (`Alt+Ctrl+Shift+S`) and choose **New Style**.
2. Name it exactly, for example `3-1`. Choose *Paragraph* as the type and *Normal* as the base.
3. Apply it to the paragraph. Its look in Word does not matter.

### Add a blank line or a page break

- Use a paragraph in the style **BB Empty Paragraph** for a blank line. A truly empty paragraph also works.
- Press `Ctrl+Enter` for a page break. Do **not** use a style for it.

---

## Practice

Use the three Word files from the [sample files](../samples/index.md).

### Tasks

1. Open `word-02-flat-structure.docx` in Word. Run the **Navigation Pane** check. What does it show? Then inspect with formatting marks and **Reveal Formatting**. List three signs that the structure is fake.
2. Repair the file: apply Heading 1, 2, and 3, apply a list style, and remove the typed bullets. Then run the Navigation Pane check again.
3. Open `word-05-braille-aware-styles.docx`. Find the styles named `3-1`, `1-3`, `List Paragraph`, and `BB Empty Paragraph` in the Styles pane.
4. Predict the BrailleBlaster result for each paragraph in file 05, then open it in BrailleBlaster and compare.
5. Add a picture to a file. Where should it sit, and what should you add to it?
6. A colleague asks which Word style to use for the title of a worksheet. What do you tell them, and why?

### Answer Key

1. The Navigation Pane shows **no headings**. Signs of fake structure: the headings are *Normal* style with direct bold and a larger size; the list lines begin with a **typed bullet and a tab**; Reveal Formatting shows direct formatting and no style.
2. After applying Heading 1, 2, and 3, the Navigation Pane lists the headings. Bullets come from the list style, not from typed characters.
3. They should all appear. The `3-1` and `1-3` styles look like ordinary paragraphs in Word. Their power is only in their names.
4. Expected from the test: Heading 1 is a Centered Heading, Heading 2 a Cell 5 Heading, Heading 3 a Cell 7 Heading; the `3-1` and `1-3` paragraphs carry those margins; the empty paragraph is a blank line; the three List Paragraph lines are list items; the **Title**-style paragraph is plain body text; and the text after the page break starts a new page. Differences are worth reporting.
5. **In Line with Text**, in a paragraph that also contains text, with **alt text** added. A picture alone in its paragraph, or floating, may be lost.
6. Use a **Heading 1** if it should be a centered heading in braille, because the **Title** style arrives as plain body text. Agree the treatment with the transcriber.

---

## Key takeaways

- **Apply a style. Never fake one.** BrailleBlaster sees styles and not appearance.
- Heading 1, 2, and 3 to 6 become Centered, Cell 5, and Cell 7 headings. The Word Title style is not a heading.
- Style names such as `3-1`, `BB Empty Paragraph`, and the List family are recognized. They work in **`.docx` only**.
- A picture alone in its paragraph, and its caption, can be lost. Keep pictures **in line with text**, with alt text.
- Inspect with the Navigation Pane, the Styles pane, formatting marks, Reveal Formatting, and Check Accessibility.

---

## Source Citations

- The BrailleBlaster program source (the conversion script `bbx.lua` and the Pandoc loader), read at commit `369176b`, with the conversion tests run using Pandoc 3.12.1, the version BrailleBlaster bundles, including `bbx.lua`, the two Word filters, and the Word page-break handling.
- Microsoft Support, *Keyboard shortcuts in Word*, at [support.microsoft.com](https://support.microsoft.com/).
- Pandoc, *Pandoc User's Guide*, the *styles* extension and the `--track-changes` option, at [pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html).
