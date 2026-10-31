# Lesson 32: Proofreading and Quality Assurance

> **Lesson at a glance**
>
> - **Unit:** Unit 4: Specialized Content
> - **Suggested time:** about 2 hours
> - **Prerequisites:** [Lesson 4](04-layout-styles.md), [Lesson 5](05-heading-levels.md), [Lesson 13](13-paper-size-and-embossers.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Plan a proofreading pass for each kind of error: accuracy, structure, emphasis, page numbers, notes, and math.
- Proofread from the Print View, the Braille View, the Braille Preview, and a saved BRF.
- Find and classify errors in a seeded draft, using an error log.
- Fix errors at the source and not in the output file.
- Use the Help menu to check your version, view the log, and report an error to APH.

> [!TIP]
> **More practice:** the **Proofreading Error Log** in the [Job Aids](../reference/job-aids.md), and the [Production Checklist](../reference/job-aids.md).

## Why this matters

A transcription that is 99 percent right is not 99 percent usable. A braille reader cannot skim past a wrong page number, a missing sentence, or a heading at the wrong level, and a student cannot ask whether "6,560" is a typo. Every error you leave in is paid for by the reader.

Proofreading is also the part of production that is easiest to skip. The software looks finished, the Braille View looks right, and the deadline is near. This lesson turns proofreading from a vague intention into a method with passes, tools, and a log.

---

## How to use this lesson

Read **The Concept** and **Step by step**, then do the **seeded-error exercise**. Do the exercise before you read the answer key, using the Error Log from the Job Aids page. The goal is not a perfect score. It is learning which kinds of error you tend to miss.

---

## The Concept

### Check one thing at a time

You cannot reliably check everything in one read. Eyes and fingers tire, and attention goes to whatever is most interesting. A better approach is a **separate pass for each kind of error**:

| Pass | Question | Where to look |
| ---- | -------- | ------------- |
| 1. **Accuracy** | Is every word, number, and name the same as in the print, with nothing added or missing? | The Print View, beside the print source |
| 2. **Structure** | Does every heading, list level, box, and table have the right style? | The **Style View** and **Breadcrumbs** |
| 3. **Emphasis and notes** | Is the emphasis that should be there present, and the emphasis that should not be there absent? Does every Transcriber's Note read correctly? | The Print View, then the Braille View |
| 4. **Math** | Is every expression flagged and translated as math, and is nothing else flagged? | The pink highlighting in the Print View, then the Braille View |
| 5. **Page and volume** | Are print and braille page numbers right, is the running head right, and do the volumes and TOC agree? | The **Braille Preview**, **Navigate > Go To Page**, and the **Page Change List** |
| 6. **The braille itself** | Does the translation read correctly? | The Braille View, and a **saved BRF** opened in the Braille Preview |

### Fix at the source

When you find an error, correct it in the **source document** (the file you can edit in the Print View), and then produce the output again. A **BRF cannot be edited in BrailleBlaster**: opening one gives you a read-only Braille Preview. If you correct a BRF in another program, your fix will be lost the next time the BBX is exported, and the two files will disagree.

### Use the tools that find errors for you

- **Tools > Spell Check** finds typing mistakes in the print text. Run it **before** the accuracy pass.
- The **Braille Preview** (`Alt+Home`) has a **Find** box, and a status line that shows the **page, line, and cell** of the cursor. Screen readers can read it.
- **Navigate > Go To Page** jumps to a print, braille, or ordinal page, so you can check a page number against the print.
- The **Page Change List** in the Page Number Dialog lists every page-number change you have made.
- **Help > View Log** and the **Exception Reporting** window collect software errors. See below.

### Habits that make proofreading work

These are common professional practices and not rules from a braille authority, so adapt them to your agency.

- **Rest, then read.** Proofread after a break, or on another day, not right after transcribing.
- **Change the medium.** If you wrote on screen, read the braille by finger. If you read on a display, also read aloud.
- **Use a second reader** whenever the work matters. A second reader catches what you are blind to.
- **Keep a log.** Write each error down with its type. Over time the log tells you which kind of error *you* make, which is where to look hardest.
- **Proofread the output, not only the source.** The BRF is what the reader gets.
- **Do not trust a generator.** T-pages, TOCs, and page numbers all need a human check.

---

## Step by step

### Proofread a document

1. **Save your work**, and keep a copy before you start changing things.
2. Run **Tools > Spell Check** on the print text.
3. Work the passes in the table above, one at a time, and write each error in your log.
4. **Fix** errors in the source. After each batch of fixes, check the Braille View again.
5. Go to **File > Export > Save BRF/PEF** and save the finished output.
6. Open the saved BRF with **File > Open**. It opens in the **Braille Preview**, where you cannot change it. Read it from the first page to the last as a final check.

### Check your version and the log

- **Help > About BrailleBlaster** tells you which BrailleBlaster you are using. Include it in any report.
- **Help > View Log** lets you view or save the software error log for APH's technical support.

### Report an error

If a program error (an exception) appears, **revert to your most recent save** and try again. Then use the button **Tell APH About This Error So They Can Fix It** in the pop-up, instead of dismissing it, so that the problem can be fixed for everyone.

> [!CAUTION]
> **Help > Reset BB** deletes *all* user data, including your translation changes, page settings, and font size. Use it only when an APH employee tells you to.

---

## Seeded-Error Exercise

Below are a **print source** and a **draft transcription**. The draft has **twelve** deliberate errors. Find them, classify each, and write them in your Error Log.

### Print Source Legend

| Print element | How it should be styled |
| ------------- | ----------------------- |
| "Chapter 2: Rivers" | Centered Heading |
| "Three Things Rivers Carry" | Cell 5 Heading |
| The three list items | One list, all at level 1 |
| "tributary" | Bold, because it is a key term |
| "Figure 2.1" line | Print **caption**, Caption style |
| The map description | **Transcriber's** description, Description style |
| "Speed = distance / time." | Mathematics |
| The page number | The print page is **14** |

### Print Source

```text
[PRINT PAGE 14]
Chapter 2: Rivers

A river begins as a small stream in the hills. Rain and melting snow feed it, and it grows as other streams join it.

Three Things Rivers Carry
- Water
- Mud and sand
- Fallen leaves

The Amazon is about 6,400 kilometers long. The Nile is about 6,650 kilometers long.

Key term: tributary, a stream that flows into a larger river.

Figure 2.1 A river and its tributaries.
Description (by the transcriber): A map showing a main river with three smaller streams joining it.

Speed = distance / time. A boat that travels 12 kilometers in 3 hours has a speed of 4 kilometers per hour.
```

### Draft Transcription

The bracketed notes in the draft show the style or emphasis that was applied. They are not part of the text.

```text
[PRINT PAGE 15]
[Centered Heading] Chapter 2: Rivers

[Body Text] A river begins as a small stream in the hills. Rain and melting snow feed it.

[Cell 7 Heading] Three Things Rivers Carry
[List level 1] Water
[List level 1]    Mud and sand
[List level 2] Fallen leaves

[Body Text] The Amazon is about 6,400 kilometres long. The Nile is about 6,560 kilometers long.

[Body Text, no emphasis] Key term: tributary, a stream that flows into a larger river.

[Caption style] A map showing a main river with three smaller streams joining it.

[Body Text, not flagged as math] Speed = distance / time. A boat that travels 12 kilometers in 3 hours has a speed of 4 kilometers per hour.
[Body Text] A boat that travels 12 kilometers in 3 hours has a speed of 4 kilometers per hour.
```

### Tasks

1. Compare the draft with the print source and the legend. List every difference you find. There are **twelve**.
2. Classify each one as **accuracy**, **structure**, **emphasis**, **page number**, **notes and captions**, **math**, or **formatting**.
3. Say which **pass** from the table would have caught each error.
4. Write the **fix** for each, in the source.
5. Which errors would a spell checker miss?

### Answer Key

| # | Error | Type | Pass that finds it | Fix |
| - | ----- | ---- | ------------------ | --- |
| 1 | The page number is 15, and the print page is **14** | Page number | 5 | Correct the page number to 14 |
| 2 | The clause "**and it grows as other streams join it**" is missing from the first paragraph | Accuracy (omission) | 1 | Restore the missing words |
| 3 | "Three Things Rivers Carry" is a **Cell 7** heading, and the legend says **Cell 5** | Structure | 2 | Apply the Cell 5 Heading style |
| 4 | "Mud and sand" has **extra spaces** typed before it to indent it | Formatting | 2 | Delete the spaces. Use the list style instead |
| 5 | "Fallen leaves" is at **list level 2**, and it should be level 1 | Structure | 2 | Apply list level 1 |
| 6 | **"kilometres"** instead of "kilometers" | Accuracy (spelling inconsistent with the source) | 1 | Change it to "kilometers" |
| 7 | **"6,560"** where the print has **6,650** (transposed digits) | Accuracy (number) | 1 | Correct the number |
| 8 | "tributary" has **no bold**, and the source marks it as a key term | Emphasis | 3 | Apply the bold typeform |
| 9 | The print **caption** "Figure 2.1 A river and its tributaries." is **missing** | Notes and captions (omission) | 1 and 3 | Restore it with the Caption style |
| 10 | The description is in the **Caption** style, so it has no Transcriber's Note indicators, and it should be in the **Description** style | Notes and captions | 3 | Apply the Description style to the whole item |
| 11 | "Speed = distance / time." is **not flagged as math** | Math | 4 | Select it and press `Ctrl+M` |
| 12 | The last sentence appears **twice** | Accuracy (duplication) | 1 | Delete the duplicate |

**Task 5.** A spell checker would miss errors 1, 3, 4, 5, 7, 8, 9, 10, 11, and 12, which involve numbers, structure, styles, or whole missing or repeated passages. It might flag "kilometres" if the dictionary is American, but it does not know whether the print used that spelling. This is why proofreading needs the source and a method.

**How did you do?** Look at the *types* you missed, not only the count. Missing the structure errors (3 to 5) means you should spend more time with Breadcrumbs. Missing accuracy errors (2, 6, 7, 12) means a slower line-by-line comparison with the source. Missing notes and captions (9, 10) means checking each figure against the print.

---

## Key takeaways

- Proofread in **separate passes**: accuracy, structure, emphasis and notes, math, page and volume, and the braille itself.
- **Fix at the source.** A BRF opens read-only in the Braille Preview, so correct the BBX and export again.
- Use the tools that find errors: Spell Check, the Braille Preview's Find box and status line, Go To Page, and the Page Change List.
- Keep an **error log**. It shows which errors *you* tend to make.
- If a program error appears, revert to your last save and report it with the **Tell APH About This Error** button. Do not use **Reset BB** unless APH asks you to.

---

## Source Citations

- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/) and the source repository [github.com/aphtech/brailleblaster-docs](https://github.com/aphtech/brailleblaster-docs): "Using the Help Menu," "Reporting BrailleBlaster Issues," and the Braille Preview and page-number sections.
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html).
