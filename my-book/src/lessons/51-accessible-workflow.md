# Lesson 51: An Accessible Workflow: Screen Readers, Braille Displays, and the Keyboard

> **Lesson at a glance**
>
> - **Unit:** Unit 5: Handbook (Supplemental)
> - **Suggested time:** about 2 hours
> - **Prerequisites:** [Lesson 1](01-navigating-the-interface.md), [Lesson 4](04-layout-styles.md)
> - **You will need:** A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Work through BrailleBlaster by keyboard alone, using the menu mnemonics and the shortcut list.
- Use the features the official guide identifies as screen-reader aware, and adjust Breadcrumbs when they are disruptive.
- Test your own assistive-technology setup against a standard set of tasks, and record the results.
- Plan a proofreading workflow that uses touch, speech, or sight as the transcriber needs.
- Report an accessibility barrier so that it can be fixed.

> [!TIP]
> **Template:** the **Accessibility Test Log** is in the [Job Aids](../reference/job-aids.md) as Aid 13.

## Why this matters

Braille transcription is work that blind and sighted people do side by side, and many of the best braille transcribers read braille themselves. A tool for making braille should be one that blind transcribers can use. How well a given screen reader and braille display work with a given release of BrailleBlaster, on a given operating system, varies, and it changes with each version.

This lesson does not claim to settle that. It does three things: it collects what the official sources **say** about keyboard and screen-reader support; it gives a **protocol** for testing your own setup; and it describes **working habits** that help everyone.

> [!NOTE]
> **An invitation.** This lesson would be stronger with tested guidance from blind transcribers and from teachers of students with visual impairments who use screen readers and braille displays daily. If that is you, please add what you know, as described under "Report a barrier."

{HB}

---

## How to use this lesson

Read **What the sources say**, then run the **test protocol** with your own equipment and record the results. The habits section is a set of suggestions, not tested instructions.

---

## What the sources say

These are the statements about keyboard use and accessibility that were found in the official user guide and in the program's source code. **Nothing else in this lesson is claimed about a particular screen reader.**

### Keyboard access

- **The menus have Alt-key mnemonics.** In the program's text, the underlined letter of each top-level menu is marked, which gives these keys:

| Menu | Key | Menu | Key |
| ---- | --- | ---- | --- |
| File | `Alt+F` | Settings | `Alt+S` |
| Edit | `Alt+E` | Emphasis | `Alt+A` |
| Navigate | `Alt+N` | Styles | `Alt+L` |
| Tools | `Alt+T` | Insert | `Alt+I` |
| View | `Alt+V` | Math | `Alt+M` |
| Help | `Alt+H` | | |

- **A full shortcut list** is on the [Shortcuts page](../reference/shortcuts.md), taken from Appendix B of the guide. It includes the context menu (`Shift+F10`), moving between elements (`Ctrl+Up` and `Ctrl+Down`), going to a page (`Ctrl+G`), the Braille Preview (`Alt+Home`), and the User Guide (`F1`).
- **BrailleBlaster is built with the SWT toolkit**, as the program source shows. This toolkit draws the operating system's own windows and controls. What that means for any particular screen reader should be **tested**, not assumed.

### Screen reader support named in the guide

1. **The Braille Preview's status line** shows the page number, line number, and cell number of the cursor, and the guide says it is **accessible to screen readers**. It is the way to know where you are in the braille.
2. **Breadcrumbs are announced.** The guide says that when a screen reader is in use and Breadcrumbs are on, **every change to the Breadcrumbs is read**. It adds that you can turn them off at **View > Toggle Views > Breadcrumbs**.

> [!IMPORTANT]
> Earlier lessons tell you to keep Breadcrumbs on. **If you use a screen reader and find the announcements disruptive, turn them off,** and use the **Style View** and **Previous and Next Element** (`Ctrl+Up` and `Ctrl+Down`) to learn the style of what you are on. Turn Breadcrumbs back on when you want to check a container.

### What this means for the course's own habits

| Course advice | If you cannot use it |
| ------------- | -------------------- |
| "Look at the Breadcrumbs" | Use the Style View and the element commands, or read the style from the Style View entry |
| "Check the pink highlighting" | Check the Braille View, where math has its own indicators, and use **Previous and Next Math** in the ASCII Math Hub |
| "Check the Braille View" | Check it with your braille display or screen reader, or save a BRF and read it ([Lesson 41](41-text-encoding-and-braille-characters.md)) |
| "Look at the colors" for Uncontracted and Direct text | Use the Braille View and the Print View's text, and the Correct Translation window's list ([Lesson 28](28-editing-the-translation.md)) |

---

## The test protocol

Run these tasks on **your** setup: your operating system, your screen reader or braille display, and your BrailleBlaster version. Use the **Accessibility Test Log**. For each task, note the method, whether it **worked**, and any **workaround**.

| # | Task | What to note |
| - | ---- | ------------ |
| 1 | Start the program, and open the **File** menu by keyboard | Are the menu items announced? |
| 2 | Open a document (`Ctrl+O`) and choose a file | Does the file dialog work with your technology? |
| 3 | Move between the **views**, and read the text of the Print View | Which views can you read? |
| 4 | Move element by element with `Ctrl+Down` | Is each element announced, and does the style come with it? |
| 5 | Apply a **heading style** by menu and by a loadout shortcut | Can you tell which style is now applied? |
| 6 | Turn **Breadcrumbs** on and off | Are the announcements helpful or disruptive? |
| 7 | Apply **bold** to selected text with `Ctrl+B` | Is the change announced? |
| 8 | Open the **Braille Preview** (`Alt+Home`) and read the **status line** | Is the page, line, and cell announced? |
| 9 | Go to a page with `Ctrl+G` | Can you complete the dialog? |
| 10 | Use **Find and Replace** (`Ctrl+F`) | Are results announced? |
| 11 | Insert a **table** and use the Table Editor | Is it usable? |
| 12 | Open the **ASCII Math Hub** and build a fraction | Can you complete it? |
| 13 | Open **Settings > Page Properties** and read the values | Are the fields labeled? |
| 14 | **Save a BRF** and read it on your display or in a reader | Does the file read correctly? |
| 15 | **Emboss** a test page, with `Ctrl+E` | Can you complete the dialog? |

If a task **fails**, try a second route (menu instead of shortcut, or the reverse), and record that too. The most useful report says **exactly what you did, what you expected, and what happened.**

---

## Working habits that help

These are suggestions, and not tested instructions. Adapt them to your own setup and your own preferences.

### Navigate by structure, not by lines

- Use **element navigation** (`Ctrl+Up` and `Ctrl+Down`) and **Go to Page** (`Ctrl+G`) instead of scrolling line by line.
- Use **Bookmarks** (the **Navigate** menu in version 3.2 and later) to mark places in a long job.
- Use the **Book Tree** (`Alt+End`) in a NIMAS file to jump by section.

### Learn the keyboard map

- Learn the **Alt letters** for the menus above, then the shortcuts you use most: save, undo, find, the emphasis keys, `Ctrl+R` to repeat a style, and the **style loadouts** (`Ctrl+Shift` plus a letter, then `Alt+1` to `Alt+8`).
- Make a **one-page list** of your own, in a form you can read, and keep it by you. [Lesson 44](44-quick-reference-cards.md) has cards.

### Proofread in more than one way

[Lesson 32](32-proofreading-and-quality-assurance.md) lists six proofreading passes. Choose, for each pass, **the medium that suits you**:

| Pass | By sight | By speech | By touch |
| ---- | -------- | --------- | -------- |
| Accuracy against the source | The Print View beside the source | The screen reader on the Print View | |
| Structure | Style View, Breadcrumbs | Element-by-element reading | |
| The braille itself | The Braille View | | A braille display reading the **saved BRF**, or the embossed page |
| Page and volume | The Braille Preview | The status line | The embossed pages |

A **second reader who uses a different medium** from yours catches different errors.

### Choose sources that suit you

A well-structured source ([Lesson 33](33-what-makes-a-good-source.md)) is more than a convenience for a blind transcriber. A flat file requires you to inspect structure by sight, which is harder without it. Ask for NIMAS, DOCX with real styles, or LaTeX where you can, and use the inspection commands in [Lesson 39](39-inside-the-packages.md), which work in a terminal and are readable by a screen reader.

---

## Accessibility of this course

The course is written as plain text with headings, lists, and tables, and its practice documents are plain text blocks. That helps, but **the website has not been audited** with screen readers or braille displays. Known cautions:

- Some pages are **long**. Use the heading navigation of your screen reader, and the site's search.
- **Tables** are used for reference. Ask your screen reader to read table headers, and report any table that is hard to follow.
- **Code blocks** hold the practice text. Each has a copy button.
- **Callouts** (notes, tips, warnings) are quoted blocks that begin with a label.

If you find a barrier, please report it.

---

## Report a barrier

1. **Say exactly what you did,** in numbered steps.
2. **Say what you expected,** and **what happened.**
3. **Give your setup:** the operating system, the screen reader or braille display and its version, and the BrailleBlaster version (**Help > About BrailleBlaster**).
4. **Report it** to the BrailleBlaster project through the **Help** menu's website link, and to this course through its issue tracker, using the accessibility template.

---

## Step by step

### Test your setup

1. Open the **Accessibility Test Log** from the Job Aids.
2. Work through tasks 1 to 15 once, recording the result for each.
3. Retry any failures by a second route.
4. **Write down your workarounds** where they work.
5. Share the log with your instructor, your agency, and the project.

### Set up a proofreading plan

1. List the **six passes** from Lesson 32.
2. Beside each, choose the **medium** you will use.
3. Arrange a **second reader who uses a different medium**, where you can.
4. Add the plan to the **agency style sheet** ([Lesson 48](48-job-intake-and-the-agency-style-sheet.md)).

---

## Practice

### Tasks

1. Run the first eight tasks of the test protocol on your setup and fill in the log.
2. Name the Alt-key for the **Styles** menu and the **Emphasis** menu. Why are they not the first letters of the menu names?
3. Breadcrumbs are announcing every change and you cannot work. What do you do?
4. Which tool tells you your position in the Braille Preview, and in what form?
5. Write a proofreading plan for a student's worksheet, for a transcriber who uses a screen reader and a braille display.
6. You find that a dialog cannot be completed with your screen reader. Write the report.

### Answer Key

1. Answers depend on your setup. A good log has a result and a method for **every** task, including the ones that failed.
2. **`Alt+L`** for Styles and **`Alt+A`** for Emphasis. The first letters, S and E, were already taken by **Settings** and **Edit**, so the program underlines a different letter in each: Sty**l**es and Emph**a**sis.
3. Turn Breadcrumbs off at **View > Toggle Views > Breadcrumbs**. Use the **Style View** and `Ctrl+Up` and `Ctrl+Down` to learn each element's style. Turn them on again when you need to check a container.
4. The **status line** at the lower left of the Braille Preview. It shows the **page number, line number, and cell number** of the cursor, according to your navigation selection, and it is accessible to screen readers.
5. A good plan, for example: *accuracy* by speech on the Print View against the source; *structure* by element navigation with the Style View; *the braille itself* by braille display on the saved BRF; *page and volume* by the status line. A second reader who reads the embossed pages by touch or sight.
6. A good report numbers the steps, states what you expected and what happened, and gives your operating system, assistive technology and version, and BrailleBlaster version.

---

## Key takeaways

- The guide names **two** screen-reader features: the **Braille Preview status line**, and the fact that **Breadcrumbs changes are announced**. Everything else should be **tested on your setup**.
- The menus have **Alt mnemonics**: File F, Edit E, Navigate N, Tools T, View V, Settings S, Emphasis A, Styles L, Insert I, Help H, Math M.
- If Breadcrumbs are disruptive, **turn them off** and use the Style View and element navigation.
- Run the **15-task test protocol**, keep a **log**, and report barriers precisely.
- Choose a **proofreading medium** for each pass, and use a **second reader** who uses a different one.

---

## Source Citations

- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/): the Braille Preview status line, the note on Breadcrumbs and screen readers, and Appendix B (keyboard shortcuts).
- The BrailleBlaster program source: the menu mnemonics in the program's text file, and the use of the SWT toolkit.
- [Lessons 32](32-proofreading-and-quality-assurance.md), [39](39-inside-the-packages.md), and [44](44-quick-reference-cards.md).
