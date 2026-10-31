# Lesson 29: UEB Technical Material, Numeric Passages, and Other Codes

> **Lesson at a glance**
>
> - **Unit:** Unit 4: Specialized Content
> - **Suggested time:** about 2 hours
> - **Prerequisites:** [Lesson 7](07-math-translation-toggle.md), [Lesson 8](08-ascii-math-hub.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Name the braille codes BrailleBlaster can translate with, and find them under **Settings > Translation Settings**.
- Explain the difference between **UEB Technical Material** and **Nemeth within UEB contexts**, and who decides which to use.
- Choose the right indicator tools for each: Nemeth Block and Inline, or Numeric Passage Block and Inline.
- Apply **Numeric Series** to insert dot 5 spaces in a series of numbers.
- Use **Math Help** to look up a tool or button.

## Why this matters

[Lesson 7](07-math-translation-toggle.md) and [Lesson 8](08-ascii-math-hub.md) used Nemeth indicators for math. That is one of **two** ways BrailleBlaster supports math inside a UEB document. The other is **UEB Technical Material**, which writes math with UEB symbols and its own indicators. Which one a student uses is a decision for their team, their teacher, and their curriculum, not for the transcriber. A transcriber's job is to know that both exist, to set up the document for the one required, and to use the right tools for it.

Likewise, UEB is BrailleBlaster's default, but it is not the only code the program translates. If your agency serves learners who use another code, you need to know where to look.

---

## How to use this lesson

This lesson is more about **choosing and setting up** than about braille-code rules. It tells you where the controls are and how the tools behave. For the braille code itself, rely on *The Rules of Unified English Braille* and the *Nemeth Code* book, and always confirm the result in the Braille View.

> [!IMPORTANT]
> Do not guess which math code a student reads. Ask. The wrong code makes the whole transcription wrong, however carefully it was formatted.

---

## The Concept

### Codes BrailleBlaster can translate with

Go to **Settings > Translation Settings**. The default is **UEB**. The other options listed in the guide are:

- **UEB Uncontracted**
- **UEB with Nemeth** (contracted and uncontracted)
- **EBAE** (English Braille, American Edition; contracted and uncontracted)
- **Spanish US**
- **Cherokee Plus Nemeth**

The same tab lets you choose your **default math translation table**.

> [!NOTE]
> Choosing a code sets the *default*. You can still change the translation of individual selections ([Lesson 28](28-editing-the-translation.md)), but changing the whole document's code is a decision to make once, at the start. Click **OK** to apply it to this document, or **Make Default** to apply it to future documents too.

### Two ways to write math inside UEB

| | **UEB Technical Material** | **Nemeth within UEB contexts** |
| - | -------------------------- | ------------------------------ |
| What it is | Math and science written with UEB symbols and UEB's technical indicators | Math written in the Nemeth Code, set off inside a UEB document by Nemeth indicators |
| Tools you use | **Math > Numeric Passage Block** or **Numeric Passage Inline** when needed | **Math > Nemeth Block** or **Nemeth Inline** |
| Where you set the default | **Settings > Translation Settings**, the default math table | The same place |

Both rely on the same first step, **Toggle Math Translation** (`Ctrl+M`), which marks the text as math and highlights it **bright pink** in the Print View. Both can be built with the **ASCII Math Hub** and the **Spatial Math Editor**.

> [!WARNING]
> **Block** and **Inline** work the same way in each family: *Block* puts the indicators on the line before and after the material, and *Inline* puts them directly before and after it, separated only by a space. But the indicators are **different**. Do not mix a Nemeth indicator into a UEB Technical document or the other way around.

### Numeric passages and series

For UEB Technical Material, the guide describes two related tools:

- **Numeric Passage Block** and **Numeric Passage Inline** wrap the selected material in a numeric passage, either on the lines before and after it (Block), or directly around it (Inline).
- **Numeric Series** places **dot 5** where spaces used to be in a series of numbers. If there were two spaces, there are two dot 5 cells.

### Math Help

**Math > Math Help** opens a quick list of definitions for the math tools and their button icons. Use it whenever you meet an unfamiliar button, especially after turning on **View > Toolbar > Math**.

---

## Step by step

### Choose the code and the math table

1. Go to **Settings > Translation Settings**.
2. Choose the code (UEB, UEB with Nemeth, and so on) and, if offered, the default math translation table.
3. Click **OK** for this document, or **Make Default** for future documents. **Cancel** leaves everything unchanged.

### Mark and wrap math

1. Select the text that is mathematics.
2. Press `Ctrl+M` (**Math > Toggle Math Translation**). The text turns pink.
3. For **Nemeth within UEB**, choose **Math > Nemeth Block** or **Nemeth Inline**.
4. For **UEB Technical Material**, choose **Math > Numeric Passage Block** or **Numeric Passage Inline** *where a numeric passage is needed*.

### Add numeric spaces to a series

1. Highlight the series of numbers.
2. Go to **Math > Numeric Series**.

Each space is replaced by a dot 5. Two spaces become two dot 5 cells.

---

## Worked Demonstration

```text
The scores were 12 15 18 21 and the total was 66.
```

1. Paste the text into a document set to **UEB with Nemeth**. Highlight *12 15 18 21* and press `Ctrl+M`. It should turn pink.
2. With the text still selected, choose **Math > Numeric Series**. Look at the Braille View. Each space in the series should now be a dot 5 cell.
3. Undo, and then choose **Math > Nemeth Inline** and look at the indicators around the numbers. Undo again.
4. Change **Settings > Translation Settings** to the UEB Technical math table. Repeat the step with **Math > Numeric Passage Inline**.
5. Note which indicators appear in each case.

---

## Practice Document

```text
Use a document set to your agency's math code.

1. The sum 3 + 4 = 7 is true.
2. The expression x squared minus 5x plus 6 equals 0 is written x^2 - 5x + 6 = 0.
3. The first four prime numbers are 2 3 5 7.
4. Half plus a third is 1/2 + 1/3.
```

### Tasks

1. Mark the math in sentences 1, 2 and 4 with `Ctrl+M`. Choose **Nemeth Inline** for each. Read the Braille View and record the indicators.
2. Mark the same sentences again after switching the default math table to **UEB Technical Material**. Use **Numeric Passage Inline** where you think a numeric passage is needed. Compare the Braille View with Task 1.
3. Apply **Numeric Series** to the numbers in sentence 3. How many dot 5 cells appear between the numbers?
4. Open **Math > Math Help** and find the definition of one button you had not used before. Write it down.
5. Your agency says the student reads Nemeth. Which of Tasks 1 and 2 matches, and what do you do about the other?
6. List the code options that appear under **Settings > Translation Settings**.

### Answer Key

1. Nemeth Inline puts Nemeth indicators directly before and after each marked expression, separated only by a space. The exact cells depend on your code table, so confirm them in your Nemeth reference.
2. The braille differs from Task 1, because UEB Technical Material and Nemeth are different codes with different indicators. A transcriber does not choose between them for style. The student's code decides.
3. There is **one** dot 5 cell for each single space, so the series of four numbers has **three** dot 5 cells between the numbers.
4. Any button's definition from Math Help is correct, as long as you read it from the list.
5. **Task 1**, because the student reads Nemeth. Delete the UEB Technical version, reset the default math table to the Nemeth context, and never leave both in a document.
6. UEB (the default), UEB Uncontracted, UEB with Nemeth (contracted and uncontracted), EBAE (contracted and uncontracted), Spanish US, and Cherokee Plus Nemeth.

> [!TIP]
> Write the required math code at the top of your job notes before you start. It is the single fact that decides everything in this lesson.

---

## Key takeaways

- **Settings > Translation Settings** controls the braille code and the default math table. UEB is the default.
- BrailleBlaster supports both **UEB Technical Material** and **Nemeth within UEB contexts**. The student's code decides which to use.
- `Ctrl+M` marks math in either case. **Nemeth Block and Inline** belong to Nemeth. **Numeric Passage Block and Inline** belong to UEB Technical Material.
- **Numeric Series** replaces spaces in a series of numbers with dot 5.
- **Math Help** explains every math tool and button.

---

## Source Citations

- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/) and the source repository [github.com/aphtech/brailleblaster-docs](https://github.com/aphtech/brailleblaster-docs): "Setting Braille Translation" and "Making Math" (Editing Math, Add Nemeth Indicators, Add Numeric Passages, Add Numeric Spaces to a Series of Numbers, Get Math Help).
- *The Rules of Unified English Braille* and *The Nemeth Braille Code for Mathematics and Science Notation*, for the rules behind the indicators.
