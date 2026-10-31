# Lesson 30: Line Numbers for Prose and Poetry

> **Lesson at a glance**
>
> - **Unit:** Unit 4: Specialized Content
> - **Suggested time:** about 60 minutes
> - **Prerequisites:** [Lesson 4](04-layout-styles.md), [Lesson 18](18-advanced-formatting.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Explain when line numbers are needed, and why they are only added to Prose and Poetic Stanza elements.
- Wrap text with **Wrap Prose**, and set the starting number and the increment.
- Insert, edit, and remove line numbers with the Line Number Tools.
- Recognize when BrailleBlaster has already numbered lines in a NIMAS file.

## Why this matters

Literature textbooks and editions of plays and poems often number their lines, so that a teacher can say "look at line 25" and every student can find it. When the same book is transcribed into braille, those numbers must survive, in a form a braille reader can use. BrailleBlaster's **Line Number Tools** put them in the right place and keep them consistent.

---

## How to use this lesson

Read **The Concept**, then follow **Step by step** with the practice passage open. The lesson is short, so work every task.

---

## The Concept

### Numbers belong to wrapped text

BrailleBlaster only shows line numbers for text that has first been wrapped in the right **container tag**:

- **Prose** for numbered lines of prose. The tool for this is **Wrap Prose**.
- **Poetic Stanza** for numbered lines of poetry. Use the Poetic Stanza style instead of Wrap Prose.

**Wrap Prose** changes nothing about the text itself. It only allows the text to *display* line numbers.

### The numbers are yours to set

You decide the **starting number** and the **increment**:

- **Line Number** sets the first number. It cannot have more than 10 digits. The default is 1.
- **Increment by** sets how much each following number rises. The default is 1.

For a text numbered every fifth line, an increment of 5 is the usual choice.

### NIMAS may already have them

If you open a NIMAS file in which the line numbers are present, BrailleBlaster may have **numbered the lines automatically**. If it did not, the line numbers are not formatted as line numbers in the original file, and you must add them yourself.

---

## Step by step

### Insert line numbers into prose

1. Go to **Tools > Line Number Tools**. A set of line-number buttons is added to the toolbar.
2. Select the text, either in the **Style View** or **Breadcrumbs**, or by highlighting it in the Print View.
3. Click **Wrap Prose** on the toolbar, or press `Ctrl+F2`. (For poetry, apply the **Poetic Stanza** style instead.)
4. Set **Line Number** (the starting number) and **Increment by** (the step).
5. Place the cursor where a line number belongs, and click **Insert** or press `F2`.
6. Repeat for each numbered line. Each new number rises by the increment.

### Edit or remove a line number

1. Click in the text that holds the number you want to change.
2. Choose **Edit Line Number** on the toolbar, or press `Ctrl+Shift+F2`. A window opens.
3. Type the new number. To remove the number completely, delete it.
4. Click **Apply**. Click **Previous** or **Next** to move through the other line numbers in the wrapped text. Each click also applies your changes.
5. Click **Done** to close the window. If BrailleBlaster cannot find any more line numbers, the window closes by itself.

---

## Worked Demonstration

```text
The tide goes out and leaves a line of weed
along the sand. The gulls come down to feed
on what the water left. A small boat waits,
its rope gone slack, beside the rusted gates
of the old pier. Behind it, lamps come on.
```

1. Paste the passage. Apply the **Poetic Stanza** style, because these are lines of verse. (For ordinary prose, you would use **Wrap Prose** instead.)
2. Open **Tools > Line Number Tools**, set **Line Number** to **5** and **Increment by** to **5**.
3. Place the cursor at the start of the fifth line and press `F2`.
4. Read the Braille View and see where the number appears.
5. Press `Ctrl+Shift+F2`, change the number to **6**, and click **Apply**, then **Done**.

---

## Practice Document

```text
The old mill stood beside the river for two hundred years.
Its great wheel turned in spring and stopped in winter.
Children came to watch the water spill over the boards.
They counted the buckets as each one rose and emptied.
At night the stones kept humming, long after the miller slept.
In summer the windows were opened to let the flour dust out.
It drifted over the yard and settled on the cats.
When the mill closed, the wheel was left to rust.
Now only the sound of the water remains.
```

### Print Source Legend

This is **prose**, printed in a textbook with a line number beside every fifth printed line (5, 10, and so on). The text is exactly nine lines long in print.

### Tasks

1. Wrap the passage with **Wrap Prose** (`Ctrl+F2`).
2. Set **Line Number** to **5** and **Increment by** to **5**. Insert a number at the fifth line. Then try to insert a second number at the ninth line, and record each number that appears.
3. Try to insert a number in text that has **not** been wrapped. What happens?
4. Use **Edit Line Number** to change one number, then use **Previous** and **Next** to look at the others. Remove one number completely.
5. Say what you would do for the same passage if it were **poetry**.
6. A NIMAS file arrives with line numbers in the margin, but BrailleBlaster did not number the lines. What is the likely cause?

### Answer Key

1. After wrapping, the text looks unchanged, because Wrap Prose only lets the text *display* line numbers.
2. Each number you insert after the first should rise by the increment. The guide's own example uses an increment of 5 with numbers 5, 10, 15, and so on, so check your results against that, and write down what *Line Number* was set to if your first number is different. In this nine-line passage the print numbers only the fifth line, so only that line should carry a number. A second number would be an error. The exercise shows what the tool does when you add one anyway, and that you, not the tool, decide where numbers belong.
3. The line number does not appear in the Print View or the Braille View, because the text must be wrapped in Prose first (or Poetic Stanza for poetry).
4. Edit Line Number opens a window. Typing a new number and clicking **Apply** changes it. Deleting the number and applying removes it. **Previous** and **Next** apply your changes while moving between numbers, and **Done** closes the window.
5. Apply the **Poetic Stanza** style to the lines instead of Wrap Prose, and then continue with the same Line Number Tools.
6. The line numbers are probably not formatted as line numbers in the original file, so BrailleBlaster could not recognize them. Add them with the Line Number Tools, or ask the publisher for a corrected file.

---

## Key takeaways

- Line numbers display only in **Prose** (`Ctrl+F2`, Wrap Prose) or **Poetic Stanza** text.
- **Line Number** sets the first number (up to 10 digits), and **Increment by** sets the step.
- Insert with `F2`. Edit or remove with `Ctrl+Shift+F2`, and click **Apply**, then **Done**.
- BrailleBlaster may number lines automatically in a NIMAS file, but only if the source formats them as line numbers.

---

## Source Citations

- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/) and the source repository [github.com/aphtech/brailleblaster-docs](https://github.com/aphtech/brailleblaster-docs): "Line Numbering" (Inserting Line Numbers, Editing Line Numbers).
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html).
