# Lesson 54: A Model Job: Capstone Walkthrough

> **Lesson at a glance**
>
> - **Unit:** Unit 5: Handbook (Supplemental)
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 48](48-job-intake-and-the-agency-style-sheet.md), [Lesson 32](32-proofreading-and-quality-assurance.md)
> - **You will need:** A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Follow one complete job from intake to delivery, with every decision explained.
- Compare your own capstone work with a model, and tell a defensible difference from a mistake.
- Read a completed production log and error log, and write your own to the same standard.
- Use the model as a pattern for real jobs.

> [!IMPORTANT]
> **Try the [Capstone](../capstone/capstone.md) first.** This walkthrough is a *model*, and not the only right answer. If you read it before you try the job, you will learn much less.

> [!IMPORTANT]
> The model demonstrates one defensible workflow, not a universal template. Do not copy its page dimensions, code choice, volume assumptions, or formatting decisions into a real job without checking that job's source, reader requirements, agency rules, and equipment.

## Why this matters

Rubrics tell you what a good job looks like. A model shows you one. This lesson walks through the capstone chapter from the first email to the final log, saying at each step **what was decided, why, which tool did it, and which lesson explains it.** Because the standards leave room for judgment, your answers may differ. What should not differ is that **every decision is made on purpose, applied consistently, and written down**.

{HB}

---

## How to use this lesson

Work through the capstone yourself. Then read each step here and compare. Where you differ, ask the questions at the end: is yours defensible, consistent, and recorded?

> [!NOTE]
> The agency, the student ID, the dates, and the time and size figures here are **made up** for the walkthrough. The tool names and menu paths are the documented ones. The Debug-menu tools are described as in [Lessons 23](23-toc-and-volumes.md) and [24](24-t-page-generator.md), with the manual method as a fallback. Nothing here has been run in the application.

---

## 1. The job

> *"Hi, could you braille Chapter 3 of the science book, "Energy and Motion," for my student? She reads UEB, and Nemeth for math. Thanks."*

### The intake ticket (filled in)

| Field | Entry |
| ----- | ----- |
| Ticket and date | 2026-0412, received 2026-11-12 |
| Requester | Science teacher, Lakeside Middle School |
| Due | 2026-11-24 |
| Student | **S0001**, grade 7 |
| Source | The chapter as plain text, with a legend, from the teacher's email. No Word or NIMAS file supplied |
| Source quality | Rank 6, plain text. The legend supplies the structure |
| Permission | The school's own material, for this student |
| Code | Contracted UEB, with **Nemeth within UEB** for math |
| Format | 11.5 by 11 inches, 40 cells by 25 lines, **interpoint** |
| Features | Headings, a three-level list, a box, a figure, equations, a key term in bold, a book title in italics, yellow highlighting |
| Special requests | The teacher refers to the yellow text aloud |
| Open questions | Is the "5-2 minutes" a range or an arithmetic expression? A better source? |

### The estimate

The chapter is **two print pages**. A sample at the final settings used about 3 braille pages per print page, so **6 braille pages**. The front matter (a title page, a Special Symbols page, and a Transcriber's Notes page) adds **3**, which makes **9**. Interpoint puts two on a sheet, so **5 sheets**. For the capstone, the job is divided into **two pretend volumes**. The estimate is hours, not days.

---

## 2. Triage the source

1. The source is plain text, **rank 6**. It carries no structure, but **the legend does**, and the legend is the real source of structure.
2. Ask the teacher for the **Word file** if one exists. Record the answer.
3. The text is **one paragraph per line**, so it will import as it is, and no unwrapping is needed ([Lesson 41](41-text-encoding-and-braille-characters.md)).
4. The markup (`**word**`, `[HIGHLIGHT:yellow]`, `[BOX]`, `[PAGE 41]`) is a stand-in. **It must not appear in the braille.** It tells you what to do, and you do it with real styles.

---

## 3. The decisions, task by task

### Task 1: Set up the page ([Lesson 13](13-paper-size-and-embossers.md))

- **Settings > Page Properties:** 40 cells by 25 lines, **interpoint on**. Click **OK**, not Make Default, until the values are confirmed.
- **Settings > Translation Settings:** UEB with Nemeth, contracted.
- **Why:** the format and code come from the ticket. Setting them first avoids reflow later.
- **Recorded:** *40 x 25, interpoint, UEB with Nemeth, contracted.*

### Task 2: Structure ([Lessons 4](04-layout-styles.md), [5](05-heading-levels.md))

There are **three print levels**, and braille has three block heading formats, so the map is direct:

| Print | Braille style |
| ----- | ------------- |
| Chapter title, **CHAPTER 3: ENERGY AND MOTION** | **Centered Heading** |
| Section headings, **3.1** and **3.2** | **Cell 5 Heading** |
| Subsection headings, **Kinds of Energy** and **Calculating Speed** | **Cell 7 Heading** |

All other paragraphs are **Body Text**. No spaces or blank lines are typed. The **Breadcrumbs** confirm each style.

### Task 3: The list ([Lesson 6](06-list-formatting.md))

The legend says three levels:

- **Level 1:** Kinetic energy, Potential energy, Thermal energy.
- **Level 2:** Energy of motion, Stored energy, Energy of heat.
- **Level 3:** A moving cart, A stretched spring, A book on a high shelf.

The sentence *The three you will study first are:* is a **Body Text** paragraph that introduces the list. Apply the list styles level by level, and check the **runover** in the Braille View.

### Task 4: Emphasis ([Lesson 3](03-typeface-emphasis.md))

| Print | Decision | Why |
| ----- | -------- | --- |
| *Forces Around Us* (italic) | **Keep italics** | A book title |
| **conservation** (bold) | **Keep bold** | A key term, and the sentence calls it one |
| Yellow highlighting | **Transcriber-defined typeform 1** (`Shift+Alt+1`) | The teacher refers to it aloud, so it carries meaning |
| Bold in the headings | **None** | The heading style says it |

The highlighting needs an explanation: it goes on the **Special Symbols page** (Task 10).

### Task 5: Mathematics ([Lessons 7](07-math-translation-toggle.md), [8](08-ascii-math-hub.md))

Each instance, and its decision:

| Text | Decision | Why |
| ---- | -------- | --- |
| *speed = distance / time* | **Flag as math**, displayed | An equation, standing alone. Words as variables follow the agency's convention, so record it |
| *s = d/t = 120/2 = 60* | **Flag as math**, build the fractions in the **ASCII Math Hub** | A displayed equation with fractions |
| *d = 120* and *t = 2* | **Flag each**, inline | Equations in a sentence |
| *3x - 5* | **Flag**, inline | An expression. The hyphen is a minus sign, and *x* is a variable |
| *x = 10* | **Flag**, inline | An equation |
| *3x - 5 = 25* | **Flag**, inline | An equation |
| *120 miles in 2 hours* | **Leave alone** | Numbers in a sentence. Not an operation |
| *well-known*, *zig-zag*, *x-ray* | **Leave alone** | Compound words. The hyphen is literary |
| *5-2 minutes* | **Flag as math**, following Lesson 7, and **ask the teacher** | Two numbers joined by a hyphen read as a subtraction in Lesson 7. In a time context it may be a range, so the question goes on the ticket |

In each case, **look at the Braille View**, and look for the pink highlighting in the Print View.

### Task 6: The box and the figure ([Lessons 18](18-advanced-formatting.md), [27](27-images-and-tactile-graphics.md), [46](46-image-description-and-tactile-graphics-resources.md))

- **The box.** It is a real sidebar, set off in print, with a title: **Did You Know?** Use a **Box** style, and keep the title as the first line. *By function*: it is a call-out that the reader should know is set apart.
- **The figure.** Reserve space with **Insert > Image Manager** (a modest number of lines, fewer than a page), and decide on a tactile graphic only if the teacher asks.
- **The print caption** *Figure 3.1 A roller coaster at the top of a hill and at the bottom.* takes the **Caption** style.
- **The description** is yours, in the **Description** style, with the **whole item selected first**:

> *A diagram of a roller coaster track. At the left, the track climbs to a high peak, where a car waits. The track then drops steeply to a low point at the right, where the car is shown again.*

It is objective, in a fixed order, and it adds nothing the picture does not show.

### Task 7: Page numbers and the running head ([Lesson 21](21-running-heads-and-page-numbers.md))

- Type the print page numbers **41** and **42** where the print pages begin, and apply the **Page** style.
- **Insert > Running Head**: *Energy and Motion*. Check that it fits above the longest page number.
- Check with the **Braille Preview** by print page, braille page, and ordinal page, and read the **Page Change List**.

### Task 8: Notes ([Lesson 22](22-transcribers-notes.md))

- **An inline note**, short and tied to one place, such as the figure description, which the Description style adds for you.
- **A separate paragraph note**, near the top of the chapter:

> *Transcriber's Note: Words highlighted in yellow in the print are shown with transcriber-defined typeform 1. See the Special Symbols page.*

Both go on the Transcriber's Notes page as well.

### Task 9: Volumes and the table of contents ([Lesson 23](23-toc-and-volumes.md))

- **The break.** Divide the chapter into two pretend volumes **before 3.2 Motion and Speed**, a section boundary. Use the **Volume Manager**, or mark the break by hand if it is unavailable.
- **The TOC.** Five entries: the chapter, 3.1, *Kinds of Energy*, 3.2, and *Calculating Speed*. Use the **TOC Builder**, or build it by hand from the Braille Preview's page numbers, **last**. Check that the entries and the volumes agree.

### Task 10: The T-pages ([Lesson 24](24-t-page-generator.md))

Make these **last**, inside the generator, or by hand:

| Page | Content |
| ---- | ------- |
| **Title page** | The title, the agency, the volume, and the date. **No student name.** The ID if your agency requires it |
| **Special Symbols page** | Transcriber-defined typeform 1: *yellow highlighting in print* |
| **Transcriber's Notes page** | The highlighting note, and the figure description note |

### Task 11: Output ([Lesson 13](13-paper-size-and-embossers.md))

- **File > Export > Save BRF/PEF**, one for each volume.
- **Emboss the first page** as a test, and check the margins.
- Keep the **BBX**.

### Task 12: Proofread and log ([Lesson 32](32-proofreading-and-quality-assurance.md))

Work the six passes, and keep the error log. The completed logs follow.

---

## 4. The production log (completed)

| Item | Entry |
| ---- | ----- |
| Job | Energy and Motion, Chapter 3, ticket 2026-0412, 2026-11-12 |
| Code and grade | Contracted UEB, with Nemeth within UEB |
| Page setup | 11.5 x 11, 40 x 25, interpoint. Generic embosser, Text only |
| Heading map | Chapter: Centered. Sections: Cell 5. Subsections: Cell 7. Three print levels |
| Lists and special structures | One three-level list. One Box (*Did You Know?*). One figure with a Caption and a Description |
| Emphasis | Kept: italic title, bold key term. Dropped: bold in headings. Highlighting: transcriber-defined typeform 1 |
| Math | Flagged all true math, and built the fractions in the Hub. Left compound hyphens and *120 miles in 2 hours* alone. *5-2* flagged per Lesson 7 |
| Notes | Highlighting (paragraph), figure description (Description style) |
| Volumes | Two pretend volumes, break before 3.2 |
| Open questions | Is *5-2 minutes* a range? Is a Word or NIMAS source available? |

## 5. The error log (completed)

These errors were found in proofreading. They are typical.

| # | Where | Error | Type | Pass | Fixed? |
| - | ----- | ----- | ---- | ---- | ------ |
| 1 | p. 2, line 4 | Heading 3.2 was a Cell 7 Heading, and should be Cell 5 | Structure | 2 | Yes |
| 2 | List | *A stretched spring* at level 2, and should be level 3 | Structure | 2 | Yes |
| 3 | Figure | The description was in the **Caption** style | Notes | 3 | Yes |
| 4 | *x-ray* | Flagged as math | Math | 4 | Yes |
| 5 | Running head | Too long with page number 42 | Pages | 5 | Yes, shortened |
| 6 | TOC | Page number for *Calculating Speed* was off by one after an edit | Pages | 5 | Yes, rechecked |

**What the log shows:** this transcriber's errors were mostly **structure and pages**, so the next job needs more time on Breadcrumbs and the Braille Preview.

---

## Compare your work

Read your own capstone against this one, and ask for each difference:

1. **Is mine a defensible alternative, or a mistake?**
2. **Is it applied consistently** across the whole job?
3. **Did I write down why?**
4. **Would the student's reading be harmed?**

A difference that passes all four is a choice. A difference that fails any is a mistake.

---

## Key takeaways

- A model job is a **pattern**: intake, triage, estimate, decisions, output, proofreading, log.
- Every decision is **made on purpose, applied consistently, and recorded**.
- **Compound-word hyphens stay literary, numbers in a sentence are not math, and a number joined by a hyphen is flagged, with the question recorded.**
- The title page, Special Symbols page, TOC, and volume breaks come **last**.
- A completed **error log** tells you where to look hardest next time.

---

## Source Citations

- [The Capstone](../capstone/capstone.md), and the lessons linked in each step.
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html).
- The agency, student ID, and figures in this walkthrough are fictional.
