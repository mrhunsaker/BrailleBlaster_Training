# Lesson 23: The TOC Tool and Distributing a TOC Among Volumes

> **Lesson at a glance**
>
> - **Unit:** Unit 3: Transcriber-Focused Lessons
> - **Suggested time:** about 2 hours
> - **Prerequisites:** [Lesson 5](05-heading-levels.md), [Lesson 13](13-paper-size-and-embossers.md), [Lesson 21](21-running-heads-and-page-numbers.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Insert volume breaks with the **Volume Manager** before building the TOC, or plan the same breaks by hand if the tool is unavailable.
- Build and update a Table of Contents and disperse it to volumes.
- Plan volume breaks at natural boundaries and not at an arbitrary sheet count.
- Verify volume and page numbers before proofreading.

> [!TIP]
> **More practice:** the [Volume Plan job aid](../reference/job-aids.md).

---

## How to use this lesson

This document teaches a multi-volume workflow. **Insert the End of Volume markers in the body text first.** Then build/update the TOC and use its volume-distribution function. For this training set, use **approximately 35–50 braille paper sheets per volume as an initial planning estimate**. This is an exercise estimate, not a universal production requirement; agency specifications and the actual page density of the book take precedence.

---

## The Concept

### Volume boundaries come before TOC distribution

The TOC should reflect the actual volume structure. Therefore the production sequence is:

```text
Estimate volume boundaries
        ↓
Insert End of Volume markers in the body text
        ↓
Build/update the TOC
        ↓
Disperse TOC entries to volumes
        ↓
Verify volume/page numbers
        ↓
Proofread
```

BrailleBlaster's User Guide specifically includes **Building the Table of Contents (TOC)**, **Formatting a Table of Contents Entry**, and **Disperse to Volumes** as TOC functions.  BrailleBlaster also supports volume-aware navigation. 

### How this works in BrailleBlaster: the Volume Manager and the TOC Builder

> [!IMPORTANT]
> **Where these tools live depends on your BrailleBlaster version.** The older 2.x User Guide describes the Volume Manager and the TOC Builder as an ordinary tool. In the current 3.x source code, however, it sits in a **Debug** menu that stays hidden until you press `Ctrl+Shift+` ` (the backtick key) in the Print View. The 3.x User Guide does not document it, so it may be unfinished. To find out what your version does, press `Ctrl+Shift+` ` and look for a **Debug** item in the menu bar. If there is one, use it and **proofread everything it produces**. If it is missing or does not work, use the manual method described below.

In the practice documents below, a line such as `[END OF VOLUME]` is a plain-text stand-in that shows you *where* a break belongs. In BrailleBlaster you do not type that marker. You insert a real **volume break** with the Volume Manager, and BrailleBlaster adds the End of Volume statement and records which text belongs to which volume. Defining volumes this way is what lets the T-Page Generator, the TOC Builder, and BRF saving work correctly, so do it first.

**Insert a volume break**

1. Place the cursor where the break should fall. The break is inserted directly *before* the cursor, so everything before the cursor becomes one volume and everything after it becomes the next.
2. Open **Volume Manager > Insert** and choose the type: **Normal** (End of Volume), **Preliminary** (End of Preliminary Volume), or **Supplementary** (End of Supplementary Volume). Your agency's guidelines decide which types to use.
3. The best cursor position is on a print page indicator, which puts the break before that indicator. If the print page starts at the top of a braille page and has no indicator, put the cursor at the start of the first element on that braille page, and the break lands on the previous braille page.

To fix a mistake, use **Change Volume Type** or **Delete Current Volume**. Deleting works only when a break already exists.

**Build the TOC**

Before you open the TOC Builder, finish the preparation the official guide recommends: remove emphasis where it should not carry into the TOC, delete bullets, format non-TOC elements such as sidebars, and insert the volume breaks. Then:

1. Open the **TOC Builder**. A TOC toolbar appears.
2. Select the text of an entry and click **TOC Entry** or press `F4`. BrailleBlaster applies the margins, blank lines, and guide dots. A multi-level list becomes a multi-level TOC, and headings become their TOC equivalents.
3. For custom levels, check **Override Margin** and enter the indent and runover cells.
4. For TOC headings, which repeat when they are referenced in another volume, use the **Headings** menu: Centered, Centered NB (no blank lines), Cell 5, or Cell 7.
5. To convert numbers into page numbers with guide dots, check **Find Page** and enter any **Page Prefix**. Page numbers that include letters, such as C13 or G5, are not found automatically, so use the **Page Number** tool on the highlighted text.
6. At each place where the TOC should divide, click **Volume Split**. This inserts the text "TOC Volume Split Placeholder."
7. Click **Disperse to Volumes**. The placeholders become volume numbers, and each volume keeps only the entries and headings that occur in it. If you click Disperse before any volumes exist, you get a warning to create volumes first.

### If the tools are hidden or unavailable: building by hand

The same result is possible with documented tools, at the cost of more care and more proofreading.

- **Volumes.** Decide the break points with the Volume Plan job aid. **File > Export > Save BRF/PEF** then produces the BRF for the volume or volumes your document defines. If your version does not define volumes, produce one BRF per volume by saving separate documents, each holding one volume's text.
- **Table of contents.** Type the entries as a list, using the list styles from [Lesson 6](06-list-formatting.md), and add the braille page numbers yourself. Confirm each page number in the Braille Preview with **Navigate > Go To Page**, because they must match the final pagination. Re-check them after *any* change that moves text.
- **Volume numbers in the TOC.** Add the volume number next to each entry by hand, and re-check it when a break moves.

A hand-built TOC is easy to get wrong after a late edit. Build it **last**, and treat it as the most error-prone part of the job.

### Planning with 35–50 sheets

For this exercise, begin with 35–50 sheets per volume. Do not treat 40 as a mandatory break point.

Prefer a natural structural boundary when possible:

- end of a chapter;
- end of a major section;
- end of a complete table/exercise unit;
- another logical production boundary.

If a chapter ends at sheet 48, for example, it may be better to end the volume there than to split it at sheet 40 merely to hit an estimate.

### Why the marker must be inserted first

The volume marker establishes which material belongs to which volume. If the TOC is distributed before those boundaries exist, the TOC does not yet have the final volume structure to reflect.

---

## Worked Demonstration

Suppose a book is approximately 160 braille sheets and has natural boundaries near Chapters 3, 6, and 9.

Plan:

```text
Volume 1: Chapters 1–3
[END OF VOLUME]

Volume 2: Chapters 4–6
[END OF VOLUME]

Volume 3: Chapters 7–9
[END OF VOLUME]

Volume 4: Chapter 10 onward
```

### Step 1

Place the End of Volume marker in the body text at each selected boundary.

### Step 2

Build/update the TOC after the volume structure exists.

### Step 3

Use the TOC tool's **Disperse to Volumes** function.

### Step 4

Check every distributed TOC entry against the actual volume and braille page.

---

## Practice Document

### Scenario 1 — 120 sheets

```text
Candidate boundaries:
Chapter 4
Chapter 8
Chapter 12
```

Use the 35–50-sheet estimate to identify likely volume boundaries, then favor logical chapter endings.

### Scenario 2 — 190 sheets

```text
Candidate boundaries:
Chapter 2
Chapter 5
Chapter 8
Chapter 11
Chapter 14
```

Choose reasonable boundaries without assuming every volume must contain exactly the same number of sheets.

### Scenario 3 — TOC first

```text
The TOC has already been generated.
No End of Volume markers have been inserted.
The transcriber now wants to disperse the TOC among volumes.
```

What should happen first?

### Scenario 4 — chapter crosses the estimate

```text
Estimated break: sheet 42
Chapter 7 ends: sheet 48
Chapter 8 begins: sheet 49
```

Should Chapter 7 automatically be split at sheet 42?

### Scenario 5 — incorrect TOC location

```text
TOC:
Chapter 9 .......... Volume 1, page 37

Actual Chapter 9:
Volume 2, page 2
```

What should be checked?

---

## Answer Key

### 1. 120 sheets

Begin with roughly three volumes of about 40 sheets each, then adjust to chapter boundaries and production requirements.

### 2. 190 sheets

Use the 35–50-sheet range as a planning aid. Natural boundaries are preferable to arbitrary page counts.

### 3. TOC first

**Insert the End of Volume markers first.** Then build/update and disperse the TOC.

### 4. Chapter crosses the estimate

No. The estimate is not an automatic cutting rule. A chapter ending at sheet 48 may be a better volume boundary than breaking it at 42.

### 5. Incorrect TOC location

Check the volume markers, page numbering, and whether the TOC was generated before the final volume structure was established. Rebuild/update and redistribute after corrections.

---

## Production Checklist

- [ ] Candidate volume boundaries identified.
- [ ] End of Volume markers inserted in the body text.
- [ ] Volume sizes reviewed against the 35–50-sheet training estimate.
- [ ] Logical structural boundaries considered.
- [ ] TOC built/updated after volume boundaries were established.
- [ ] TOC dispersed to volumes.
- [ ] Volume numbers verified.
- [ ] Braille page numbers verified.
- [ ] TOC proofread in Braille View.

## Core Principle

**Put the volume boundaries in the text first. Then let the TOC reflect those boundaries.**

---

## Source Citations

- BrailleBlaster User Guide — Building the Table of Contents, Formatting a TOC Entry, and Disperse to Volumes. 
- BrailleBlaster documentation — volume-aware navigation and volume breaks. 
- BrailleBlaster official site — volume splitting functionality. 
- **Training-set planning estimate:** 35–50 braille paper sheets per volume, as specified for this exercise; not presented as a universal Braille Formats requirement.
