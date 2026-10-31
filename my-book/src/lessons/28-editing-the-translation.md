# Lesson 28: Editing the Translation

> **Lesson at a glance**
>
> - **Unit:** Unit 4: Specialized Content
> - **Suggested time:** about 90 minutes
> - **Prerequisites:** [Lesson 3](03-typeface-emphasis.md), [Lesson 7](07-math-translation-toggle.md), [Lesson 11](11-contraction-relaxer.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Enter braille directly with **Six Key Mode**, and explain why that text is not translated.
- Change the translation of a selection to **Uncontracted** or **Direct**, and recognize the colors that mark each.
- Use **Correct Braille Translation** to define a new character, correct a character, or correct a word.
- Choose between saving a correction **locally** and **globally**, and explain the privacy difference.
- View, edit, and delete earlier corrections.

## Why this matters

BrailleBlaster relies on the open-source translator **Liblouis** to turn print into braille, and Liblouis is very good, but it cannot know every proper noun, foreign word, or unusual symbol. Sooner or later it gets one wrong, or meets a character it has no braille for. A professional transcriber needs a safe, repeatable way to fix those cases, and to know *which* tool to reach for.

This lesson pulls together the translation-editing tools into one decision guide. You met two of them in [Lesson 11](11-contraction-relaxer.md). Here you add the other two.

---

## How to use this lesson

Read **The Concept**, then use the **decision table** in the practice. Work with a short, private practice document, never a real student's file.

> [!WARNING]
> The tools in this lesson can **send information outside your computer**. Saving a correction **globally** submits it to APH. Do not use real student names, addresses, or other private information in anything you save globally. Use **Save Translation Locally** unless you are sure.

---

## The Concept

### Four tools, four jobs

| Tool | Acts on | Use it when | Shortcut |
| ---- | ------- | ----------- | -------- |
| **Six Key Mode** | What you type next | You want to type braille directly, with no translation | `Alt+X` (on and off) |
| **Change Translation: Uncontracted** | The selected text | A passage must be in grade 1 braille, with no contractions | `Ctrl+Shift+T` |
| **Change Translation: Direct** | The selected text | You must force the literal ASCII translation, when BrailleBlaster would not otherwise allow it | `Ctrl+D` |
| **Correct Braille Translation** | A character or a word, for this and future documents | A character, proper noun, or foreign word is translating wrongly or not at all | `Ctrl+T` |

The first three change **this document only**. The last one changes **how BrailleBlaster translates in the future**, which is far more powerful and needs more care.

### Six Key Mode

In Six Key Mode, six keys on the left and right of the home row stand for the six dots of a braille cell:

| Key | Dot |
| --- | --- |
| F | 1 |
| D | 2 |
| S | 3 |
| J | 4 |
| K | 5 |
| L | 6 |

You press the keys for a cell at the same time. BrailleBlaster does **not** translate what you type this way, so what shows in the Print View also shows in the Braille View. That is the point: you are typing braille, not print.

> [!NOTE]
> If Six Key Mode does not work, the cause is most likely your keyboard. Not all keyboards register several letters pressed at once.

### Undefined characters

When BrailleBlaster meets a Unicode character it has no braille for, such as the black right-pointing triangle (U+25B6), it shows the character itself in the **Print View**, and shows the character's **Unicode name** enclosed in Transcriber's Notes in the **Braille View**. That is a safe default, because the reader is told something is there. A **correction** lets you replace the name with an agency-approved symbol.

### Saving a correction

- **Save Translation Locally** writes the correction to a file **on your computer**. It is for personal or agency preferences.
- **Save Translation Globally** saves it locally **and submits it to APH**, who review it for future releases and to share with other Liblouis users. This helps braille readers everywhere, and it also means the word leaves your computer.

---

## Step by step

### Type braille directly

1. Go to **Tools > Six Key Mode**, or press `Alt+X`.
2. Press the keys for each cell together. For example, F alone is dot 1, and F with D is dots 1-2.
3. Press `Alt+X` again to return to normal typing.

### Change a selection's translation

1. Select the text, from a single word to several pages.
2. Go to **Tools > Change Translation**, use the toolbar button, or right-click and choose **Change Translation**.
3. Choose **Uncontracted** (green in the Braille View) or **Direct** (purple in the Print View).

### Correct a translation

1. Highlight the character or word in the Print View.
2. Go to **Tools > Correct Braille Translation**, or press `Ctrl+T`. The highlighted print appears in the **Print** box, and the **Braille** box waits for the correct braille.
3. Choose what kind of correction it is:
   - **Define New Character** creates a character BrailleBlaster did not have.
   - **Correct Character** fixes a character that is translating wrongly.
   - **Correct Word** fixes a proper noun or foreign word.
4. Choose your **entry method**: **Six Key** or **ASCII**.
5. Type the correct braille in the Braille box.
6. Choose **Save Translation Locally** or **Save Translation Globally**, or **Cancel**.

### Review and undo corrections

1. In the Correct Translation window, click **View Corrections**.
2. To change an entry, click **Edit Translation**. To remove one, select it and click **Delete Entry**.
3. Click **Cancel** to return without changes.

> [!TIP]
> BrailleBlaster 3.x also has **Tools > Spell Check**. Spell-check the print text before you transcribe, and fix print typos in the source or the Print View, so that you do not "correct" a translation that was only a typing mistake.

---

## Worked Demonstration

```text
Ms. Siobhan Nguyen read the label. The ▶ symbol starts the video.
```

1. Paste the text. Read the Braille View. Find the triangle. The Print View should show the symbol, and the Braille View should show its Unicode name inside Transcriber's Notes.
2. Highlight **Siobhan**, press `Ctrl+T`, and choose **Correct Word**. Type the braille your agency prefers, and choose **Save Translation Locally**.
3. Reread the Braille View. Then add *Siobhan* again in a second sentence and see whether the correction applies to it.
4. Open **View Corrections** and find your entry. Delete it with **Delete Entry**, and confirm the second sentence returns to the original translation.

---

## Practice Document

```text
Private practice text, not a real student's.

Ms. Siobhan Nguyen read the label. The ▶ symbol starts the video.
The code is a1b2c3. The Spanish word is ñandú.
```

### Tasks

1. Turn on **Six Key Mode** and type the three cells for the letters **c**, **a**, and **b**. Which keys did you press for each? Turn Six Key Mode off. Look in the Braille View.
2. Select `a1b2c3`. Apply **Direct** translation. What color is the text in the Print View? Undo it, and apply **Uncontracted** instead. What color does the Braille View show?
3. Use **Correct Braille Translation** on *Siobhan* and choose **Correct Word**, and save it **locally**. Check that the correction applies to a second occurrence of the word.
4. Highlight the `▶` and open **Correct Braille Translation**. Which of the three options fits, and why?
5. Open **View Corrections**. Edit one entry, then delete both entries.
6. For each case, say which tool you would use: (a) a computer code string that must appear exactly; (b) a surname your agency spells in a particular way; (c) a short passage in grade 1 braille for a beginning reader; (d) a brand-new symbol the text uses everywhere.

### Answer Key

1. **c** is dots 1-4, so press **F and J** together. **a** is dot 1, so press **F**. **b** is dots 1-2, so press **F and D** together. In the Braille View, the cells you typed should appear exactly as typed, because Six Key text is not translated.
2. Direct text is highlighted in **purple in the Print View**. Uncontracted text is highlighted in **green in the Braille View**. Both are selection-level changes, and neither affects the rest of the document.
3. After saving locally, the corrected braille should appear for *Siobhan* in the second sentence too, because the correction is stored and used by later translations. If it does not, check that the second occurrence is spelled identically, including capitalization.
4. **Define New Character**, because the triangle has no braille definition. (Use **Correct Character** only for a character that already translates but wrongly.)
5. Choose a corrections entry, click **Edit Translation**, change it, and save. Selecting an entry and clicking **Delete Entry** removes it. After deleting, the word and the symbol return to the earlier translation.
6. (a) **Direct**. (b) **Correct Word**, saved locally unless you have decided to share it. (c) **Uncontracted** on that selection, or the **Contraction Relaxer** if it is a whole document tied to a learner's sequence ([Lesson 11](11-contraction-relaxer.md)). (d) **Define New Character**.

> [!NOTE]
> Never use a student's real name when you practice saving corrections, and never save such a name globally.

---

## Key takeaways

- **Six Key Mode** (`Alt+X`) types untranslated braille. **Change Translation** acts on a selection (Uncontracted `Ctrl+Shift+T`, Direct `Ctrl+D`). **Correct Braille Translation** (`Ctrl+T`) changes how BrailleBlaster translates in the future.
- An undefined Unicode character shows as its **Unicode name in Transcriber's Notes** in the Braille View, until you define it.
- **Save Translation Globally submits the correction to APH.** Use **Locally** for anything private.
- **View Corrections** lets you edit or delete earlier entries.
- Fix print typos first with **Spell Check**, so that you do not "correct" a typing mistake.

---

## Source Citations

- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/) and the source repository [github.com/aphtech/brailleblaster-docs](https://github.com/aphtech/brailleblaster-docs): "Modifying the Braille Translation" (Entering Braille Directly, Changing the Text Translation, Correcting the Braille Translation, Viewing Past Corrections).
- The Liblouis project, [liblouis.io](https://liblouis.io/).
