# Lesson 25: Tables

> **Lesson at a glance**
>
> - **Unit:** Unit 4: Specialized Content
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 4](04-layout-styles.md), [Lesson 6](06-list-formatting.md), [Lesson 12](12-find-and-replace.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Create a table with **Insert > Table** and fill in the Table Editor.
- Explain what the Auto, Simple, Listed, Stairstep, and Linear table types do.
- Use Simple Table Options to control the cells between columns, guide dots, row headings, and column widths.
- Write the Transcriber's Note that explains a changed table format.
- Edit a table only through the Table Editor, and reformat or delete a table.
- Decide whether a print table can stay a table in braille or must be restructured.

> [!TIP]
> **More practice:** the Print Source Legend and tasks below use only plain text, so you can paste them straight into the Table Editor.

## Why this matters

Tables are everywhere in textbooks, and they are among the hardest things to transcribe. A print table uses the whole width of a page and the reader's eye to compare across rows and down columns. A braille page is usually about 40 cells wide, and a refreshable display shows even less. Some print tables fit. Many do not.

*Braille Formats 2016* gives several ways to present a table in braille so that the reader can still find what they need. BrailleBlaster's Table Editor builds each of those formats for you, but **you decide which format fits** and you explain any change to the reader.

---

## How to use this lesson

Read **The Concept**, then follow **Step by step**. Work through the practice tables in order, keeping the Table Editor open and the Braille View visible, and check yourself against the **Answer Key**.

> [!NOTE]
> This lesson follows the BrailleBlaster 3.x User Guide. Menu names can change between releases. If **Insert > Table** is not where you expect it, use the **BrailleBlaster User Guide** (**Help > BrailleBlaster User Guide**, or `F1`).

---

## The Concept

### A table has a structure and a presentation

A table is **data** (rows and columns of entries, with headings) shown in a **presentation** (a layout on the page). In print, one presentation is used for everything. In braille, the best presentation depends on how much the table has to say and how wide it is. The data stays the same. The presentation changes.

BrailleBlaster separates the two. You type the data once, in the **Table Editor**, and then choose a **table type**, which is the presentation.

### The table types

- **Auto.** BrailleBlaster picks the type it thinks best fits the amount and length of the information. This is the default.
- **Simple.** A standard braille table with columns and rows, and a line separator beneath each column heading. Use it when the table fits the braille page.
- **Listed.** The row headings become **Cell 5 headings**. The column headings become the first part of each listed item, followed by a colon that BrailleBlaster inserts. The entries follow the colon. Use it when the table is too wide, and each row is a labeled thing with several attributes.
- **Stairstep.** Each row becomes a group of lines, and each column starts at a **different margin**, so the columns step across the page.
- **Linear.** The column headings go into a Transcriber's Note before the table, and each row becomes one line in a list, separated by colons and semicolons.

> [!IMPORTANT]
> Listed, Stairstep, and Linear **change the print format**, so the reader must be told. BrailleBlaster adds a Transcriber's Note field for each of them, with default wording you can edit. Never leave out the explanation.

### Choose the format by fit and by meaning

There is no single rule, and *Braille Formats 2016* is the authority. These questions help:

1. **Does it fit?** Add up the column widths and the spaces between columns and compare with the cells on your braille line. If it fits and reads clearly, Simple is the first choice.
2. **What does the reader do with it?** If the reader compares down a column, keep the columns together. If the reader looks up one row at a time, a Listed or Linear format may be easier.
3. **Is the table nested or hierarchical?** A Stairstep format can show levels.
4. **Can it be shortened without losing meaning?** Sometimes a wide table has an empty or decorative column. Do not drop content without a note.

### Edits happen in the Table Editor

Text inside a table **cannot be edited in the Print View**, even to fix a typo. To change it, place the cursor inside the table and reopen the Table Editor. If the cursor is not on a table, BrailleBlaster shows the message "Cursor is not on table."

---

## Step by step

### Create a table

1. Place the cursor where the table should begin.
2. Go to **Insert > Table**. The Table Editor opens.
3. In the lower right corner, set the **Rows** and **Columns**. The default is 3 rows and 3 columns.
4. Type the text for each entry.
5. (Optional) Add emphasis or change the translation with the drop-down menus on the toolbar.
6. Check that the **Table type** in the lower left corner is set to **Auto**, and select **Save**. BrailleBlaster formats the table in the style it judges best.

The shortcuts for emphasis and for changing the translation are the same in the Table Editor as in the Print View.

### Emphasis and translation inside a table

- **Emphasis.** Select text in the table and choose a typeform. To apply a typeform to every entry, use **Tools > Add Emphasis to All**. To remove it all, use **Tools > Remove All Emphasis**.
- **Translation.** Select text and choose **Direct**, **Uncontracted**, or **Math**. **Direct** is for pre-translated ASCII braille. **Uncontracted** removes contractions while keeping your translation table. **Math** creates linear math with ASCII Math. If the whole table is mathematics, use **Tools > Add Math Translation to All**.
- **Swap.** **Tools > Swap Columns and Rows** can improve fit.

### Choose a type

Use the **Table type** menu in the lower left of the editor. When you choose a type, a button for that type's options appears beside the menu.

**Simple Table Options** opens a window with:

- **Cells between columns:** 2 (the default) or 1.
- **Guide dots:** Enabled (the default) or Disabled. These dots follow the material in the columns.
- **Row headings:** when Enabled (the default), material in column 2 and beyond starts on the same line as any *runover* of the heading in column 1. When Disabled, it starts on the line where the heading starts.
- **Column widths:** Default or Custom. With Custom, a field appears for each column showing the number of braille cells it uses. Between the fields, a number in parentheses (1 or 2) shows the cells between columns. **Total Width: X** shows the total cells the table takes. Watch it so the table does not exceed the width of the braille page.

**Create Transcriber's Note Heading** (Listed, Stairstep, and Linear) adds a text field at the top of the editor:

- **Listed.** A 7-5 field with the default text: "Print format is changed. Row headings are blocked in cell 5; column headings begin in cell 1. All headings are repeated for clarity. A colon separates headings from table entries."
- **Stairstep.** A 7-5 field that defaults to "Table changes as follows:", followed by fields at the margins 1-1, 3-3, 5-5, and so on.
- **Linear.** A 7-5 field for the note, and a 1-3 field that lists the column headings in order, with a colon after the first heading and a semicolon after each other.

Edit the default wording if your document needs it, then click **OK**.

### Reformat or delete

- **Actions > Reformat Table** converts the table into plain text. A warning says so, and asks you to confirm. Then a list of styles appears, and the style you choose is applied to all the table's text.
- **Advanced Reformat** works the same way, except that each field can get a *different* style, which you choose cell by cell.
- **Actions > Delete Table** removes the table and its text from the Print View completely.

---

## Worked Demonstration

1. You do not need to paste anything. Go to **Insert > Table** and set 4 rows and 3 columns.
2. Type this data. The first row is the column headings.

   | Fruit  | Color  | Season |
   | ------ | ------ | ------ |
   | Apple  | Red    | Autumn |
   | Cherry | Red    | Summer |
   | Lemon  | Yellow | Winter |

3. Leave **Table type** on **Auto** and click **Save**. Look at the Braille View. Which type did BrailleBlaster choose, and does the table fit?
4. Place the cursor in the table, reopen the Table Editor, and switch the type to **Listed**. Click **Create Transcriber's Note Heading** and read the default text.
5. Save, and read the Braille View again. How does each row read now?
6. Switch to **Simple**, open **Simple Table Options**, and change **Cells between columns** from 2 to 1. Watch **Total Width** change.
7. Save. Try to type a word in the table from the Print View. The text should not accept edits there, because table text can only be changed in the Table Editor.

---

## Practice Document

Work through these four tables. Each starts in the Table Editor.

### Print Source Legend

| Table | Print appearance |
| ----- | ---------------- |
| **A** | A small table: three columns (*Month*, *Rainfall in millimeters*, *Sunny days*) and four rows of data |
| **B** | A wide table: six columns (*Planet*, *Diameter in kilometers*, *Distance from the Sun in millions of kilometers*, *Orbital period in days*, *Moons*, *Main gases in the atmosphere*) and four rows of data |
| **C** | A table whose entries are all arithmetic expressions |
| **D** | A table with a column of empty cells and one decorative column that holds only a small picture |

### Data

```text
Table A
Month | Rainfall in millimeters | Sunny days
January | 78 | 11
February | 64 | 13
March | 71 | 16
April | 55 | 19

Table B
Planet | Diameter in kilometers | Distance from the Sun in millions of kilometers | Orbital period in days | Moons | Main gases in the atmosphere
Mercury | 4879 | 58 | 88 | 0 | almost none
Venus | 12104 | 108 | 225 | 0 | carbon dioxide, nitrogen
Earth | 12742 | 150 | 365 | 1 | nitrogen, oxygen
Mars | 6779 | 228 | 687 | 2 | carbon dioxide, nitrogen

Table C
Expression | Value
3 + 4 | 7
9 - 2 | 7
6 x 2 | 12
8 / 4 | 2
```

### Tasks

1. **Table A.** Build it in the Table Editor with Auto. Open the Simple Table Options. Record the Total Width, and compare it with the **cells per line** shown in **Settings > Page Properties**. Does it fit?
2. **Table B.** Build it and set **Simple**. Open Simple Table Options, switch to **Custom** column widths, and record the Total Width. Does it fit the page? Then switch to **Listed**, add the Transcriber's Note heading, and read the Braille View. Finally try **Linear**.
3. **Table C.** Build it. Decide whether every entry is mathematics, and if so use **Tools > Add Math Translation to All**. Check the Braille View.
4. **Table D.** Describe in one sentence what you would do about the empty column and the decorative picture column, and what you would put in a Transcriber's Note.
5. Put the cursor *outside* any table and try to open the Table Editor for editing. Record the message.
6. Use **Actions > Reformat Table** on Table A. What does the result look like, and what warning came first?

### Answer Key

1. Table A has short entries, so it should fit comfortably within the cells per line. The check is the comparison, not the guess. Whether it fits is decided by **Total Width** against the page width. If the Total Width is less than or equal to the cells per line, Simple works.
2. Table B is much wider. With the long headings and the long final column, the **Total Width** should be larger than the cells per line, so a Simple table cannot be used as it stands. **Listed** turns each planet into a Cell 5 heading and writes each attribute as "column heading: value". **Linear** puts the six column headings in a Transcriber's Note and lists each planet's values on a line. Either can be correct. Your choice should be justified by how a reader will use the data, and the Transcriber's Note should be present.
3. If every entry in the table is an expression, **Add Math Translation to All** is the efficient choice. Check the Braille View so that the minus sign, the multiplication sign `x`, and the division sign are all translated as math.
4. A defensible answer says: do not leave an empty column unexplained. Either keep the column and the empty cells, or drop the column and say so in a note. Describe the picture's content if it is informative, or omit it with a note if it is purely decorative. A Transcriber's Note should record any change from the print.
5. BrailleBlaster shows the message **"Cursor is not on table."**
6. A warning appears first, saying that reformatting converts the table formatting to plain text and asking whether you are sure. The result is ordinary text in the style you chose. The table structure is gone, so use this only when you have decided against a table.

> [!TIP]
> Whenever you change a table's format, ask: "Would the reader know the print was a table, and how to read this?" If not, expand the Transcriber's Note.

---

## Key takeaways

- A table has data and a presentation. You type the data once and choose the presentation.
- Table types are **Auto, Simple, Listed, Stairstep, and Linear**. Listed, Stairstep, and Linear change the print format and need a Transcriber's Note.
- **Total Width** in the Simple Table Options tells you whether a Simple table fits the page.
- Text in a table can only be edited in the Table Editor. The Print View will not let you.
- **Reformat Table** turns a table into plain text. **Delete Table** removes it.

---

## Source Citations

- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/) and the source repository [github.com/aphtech/brailleblaster-docs](https://github.com/aphtech/brailleblaster-docs): "Working with Tables" (inserting, formatting, editing, and reformatting tables).
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html). The table formats BrailleBlaster builds are those described there.
