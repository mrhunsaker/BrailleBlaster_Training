# Lesson 45: Page Geometry and Sizing Volumes

> **Lesson at a glance**
>
> - **Unit:** Unit 5: Handbook (Supplemental)
> - **Suggested time:** about 90 minutes
> - **Prerequisites:** [Lesson 13](13-paper-size-and-embossers.md), [Lesson 23](23-toc-and-volumes.md)
> - **You will need:** A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Explain page size, margins, cells per line, lines per page, and interpoint, and how they relate.
- Say how BrailleBlaster and the embosser each hold part of the page setup, and what goes wrong when they disagree.
- Estimate braille pages, sheets, and volumes from a measured sample.
- Plan volume breaks and front matter so that the count is realistic.

## Why this matters

A transcription is not finished when the last page is formatted. It has to be **embossed**, **bound or boxed**, and **handed to a student**. A volume that is too thick is hard to handle, a title that needs forty volumes was not planned, and a document whose margins do not match its embosser comes out with broken lines. All of this is arithmetic that you can do before you start.

[Lesson 13](13-paper-size-and-embossers.md) taught you to set the page up. [Lesson 23](23-toc-and-volumes.md) taught you to divide a book into volumes. This lesson gives you the numbers behind both.

{HB}

---

## How to use this lesson

Read **The Concept**, then work the estimator on a real or imagined book. The practice has three jobs to size.

> [!NOTE]
> Physical measurements here are **approximations**. A braille cell is about a quarter of an inch wide and a line is about four-tenths of an inch tall, but the exact figures depend on the embosser. **Always read the real numbers from BrailleBlaster's Page Properties** and from your embosser's manual. Planning figures such as sheets per volume are **agency decisions**, not rules.

---

## The Concept

### The vocabulary

| Term | Meaning |
| ---- | ------- |
| **Page size** | The size of the paper, for example 11.5 by 11 inches |
| **Margins** | The unused space at the top, bottom, left, and right |
| **Cells per line** | How many braille cells fit across the page |
| **Lines per page** | How many lines fit down the page |
| **Single-sided** | Braille on one side of each sheet. One sheet is one page |
| **Interpoint** | Braille on both sides of each sheet. One sheet is **two** pages |
| **Sheet** | One piece of paper |
| **Volume** | A group of sheets bound or held together as one physical book |

In an interpoint volume, the **front** of each sheet is an **odd** page and the **back** is an **even** page. Pages that must face each other, such as a table across a spread, sit on the left (even) and right (odd) of an open book ([Lesson 26](26-controlling-the-page.md)).

### How the page setup is held

BrailleBlaster's **Settings > Page Properties** holds the **page size**, **lines per page**, **cells per line**, the **margins**, and **interpoint**. The guide gives the defaults as a page of **11.5 by 11 inches**, with margins of **0.5 inch** at the top and bottom, **1.25 inches** on the left, and **0.48 inch** on the right. You can show the margins in inches, in cells, or in lines.

The **embosser** holds its own settings as well. When BrailleBlaster is told the embosser's make and model, it knows what to send. When you choose **Generic, Text only**, BrailleBlaster sends plain text and **you must set the embosser's own paper size and margins** to match the document, using the manufacturer's software or the buttons on the machine. Three advanced options (from the guide) matter when a generic embosser misbehaves:

- **Add margins.** BrailleBlaster adds spaces and blank lines to imitate margins. The guide recommends **false**, and setting the margins on the embosser instead.
- **Pad page.** BrailleBlaster adds blank lines to fill the last page. It is for embossers that count lines and ignore form feeds. For most embossers it should be **false**.
- **Form feed on full page.** Whether a form feed is added at the end of a full page.

When the two sides **disagree**, the symptoms are familiar: lines that wrap in the wrong place, a page that breaks too early or too late, a first line pushed down, or text embossed off the paper. The fix is always to make the two agree, and then to run a **test emboss** ([Lab 5](../labs/lab-5-test-page-and-embosser.md)).

### Cells per line and lines per page, by arithmetic

You can get close to the numbers by hand. Take the paper size, subtract the margins, and divide by the size of a cell and a line.

| | Calculation | Result |
| - | ----------- | ------ |
| Printable width | 11.5 − 1.25 − 0.48 | **9.77 inches** |
| Printable height | 11 − 0.5 − 0.5 | **10 inches** |
| Cells per line | 9.77 ÷ 0.25 (about a quarter inch per cell) | **about 39** |
| Lines per page | 10 ÷ 0.4 (about four-tenths of an inch per line) | **about 25** |

The result lands close to the familiar **40 cells by 25 lines**. The exact values come from the embosser's real cell spacing, so use the numbers BrailleBlaster shows, and use this arithmetic only to check that they are reasonable.

---

## Sizing a transcription

### Never guess the ratio. Measure it.

How many braille pages one print page becomes depends on the book: a text-heavy novel behaves one way, a math textbook with tables and graphics another, a picture book another. So do not rely on a rule of thumb. **Measure a sample:**

1. Set up the page properties and embosser **exactly as the final job will be**.
2. Transcribe **five typical print pages**, not the easiest five.
3. Count the braille pages they used. Divide braille pages by print pages. That is your **ratio**.

If five print pages produced 14 braille pages, the ratio is 14 ÷ 5 = **2.8**.

### The arithmetic

1. **Braille pages** = print pages × ratio, rounded up, plus extra pages for front matter.
2. **Sheets** = braille pages for single-sided, or braille pages ÷ 2 (rounded up) for interpoint.
3. **Volumes** = sheets ÷ sheets per volume, rounded up.

The **extra pages** are the title page, the special symbols page, the Transcriber's Notes page, the table of contents, and blank pages for facing-page needs. They are small, but they must be counted.

### An estimator

Save this as `estimate.py`:

```python
import math, sys
def estimate(print_pages, ratio, interpoint=True, sheets_per_volume=40, extra_pages=0):
    braille_pages = math.ceil(print_pages * ratio) + extra_pages
    sheets = math.ceil(braille_pages / 2) if interpoint else braille_pages
    volumes = math.ceil(sheets / sheets_per_volume)
    return braille_pages, sheets, volumes
pp, ratio = int(sys.argv[1]), float(sys.argv[2])
ip = sys.argv[3].lower() == "interpoint"
spv = int(sys.argv[4]); extra = int(sys.argv[5]) if len(sys.argv) > 5 else 0
bp, sh, vol = estimate(pp, ratio, ip, spv, extra)
print(f"braille pages: {bp}   sheets: {sh}   volumes: {vol}")
```

Run it as `python3 estimate.py PRINT_PAGES RATIO interpoint|single SHEETS_PER_VOLUME [EXTRA_PAGES]`.

**Worked example.** A 320-page textbook with a measured ratio of 2.8, interpoint, at 40 sheets per volume: `python3 estimate.py 320 2.8 interpoint 40` gives **896 braille pages, 448 sheets, and 12 volumes**. The same book single-sided gives 896 sheets and **23 volumes**. Interpoint halves the paper and the shelf space.

### Choosing sheets per volume

[Lesson 23](23-toc-and-volumes.md) mentions **35 to 50 sheets per volume** as a planning figure. It is **not a rule**. Your agency, the student's age and strength, the binding method, and the book's content all affect it. A volume that is too thick is awkward to hold, and a student who reads with two hands needs a volume that lies flat.

Place volume breaks at **natural boundaries**, such as the end of a chapter, even if that makes the volumes uneven ([Lesson 23](23-toc-and-volumes.md)).

---

## Step by step

### Plan a job's size

1. Ask the requester for the **print page count** and the **braille format** the student needs (paper size, interpoint or not).
2. Set **Settings > Page Properties** and the embosser to the final values.
3. Transcribe a **five-page sample** and compute the **ratio**.
4. Run the **estimator** with your agency's sheets per volume and an allowance for front matter.
5. Compare the estimated **volumes** with the volume plan ([Job Aids](../reference/job-aids.md)).
6. **Tell the requester** the number of volumes, the time, and any concern, before you start the long work.

---

## Practice

### Tasks

1. A page is 8.5 inches by 11 inches, with margins of 0.5 inch on all four sides. Calculate the printable width and height. Using about 0.25 inch per cell and 0.4 inch per line, estimate the cells per line and the lines per page.
2. A 320-page textbook has a ratio of 2.8. How many braille pages, sheets, and volumes at 40 sheets per volume, interpoint? And single-sided?
3. A 120-page unit has a measured ratio of 3.1, plus 12 pages of front matter. Interpoint, at 35 sheets per volume. How many volumes?
4. A 48-page workbook with a ratio of 3.4, single-sided, at 40 sheets per volume. How many pages, sheets, and volumes?
5. Your sample of five print pages produced 17 braille pages. What is the ratio?
6. An embosser is set to Generic, Text only. The braille comes out with lines wrapping early. What do you check?
7. Why is it risky to estimate with the ratio from the easiest five print pages?

### Answer Key

1. Printable width is 8.5 − 1.0 = **7.5 inches** and height is 11 − 1.0 = **10 inches**. That gives about 7.5 ÷ 0.25 = **30 cells per line** and 10 ÷ 0.4 = **25 lines per page**. Confirm in **Settings > Page Properties**.
2. 320 × 2.8 = **896 braille pages**. Interpoint: **448 sheets** and 448 ÷ 40 = 11.2, so **12 volumes**. Single-sided: **896 sheets**, and 896 ÷ 40 = 22.4, so **23 volumes**.
3. 120 × 3.1 = 372, plus 12 = **384 braille pages**. Interpoint gives **192 sheets**, and 192 ÷ 35 = 5.49, so **6 volumes**.
4. 48 × 3.4 = 163.2, rounded up to 164, so **164 braille pages**. Single-sided is **164 sheets**, and 164 ÷ 40 = 4.1, so **5 volumes**.
5. 17 ÷ 5 = **3.4**.
6. The **embosser's own settings** for paper size and margins, because Generic Text only relies on them. Check them in the manufacturer's software or on the machine. Then check the document's **Page Properties** and the **Add margins** option, and run a test emboss.
7. The easy pages understate the average, so the estimate of braille pages, sheets, and volumes is too low, and the job takes more volumes than you promised. Sample **typical** pages, and include a hard one.

---

## Key takeaways

- **Page Properties** holds the page size, margins, cells per line, lines per page, and interpoint. The **embosser** holds its own settings. They must agree, and a test emboss proves it.
- Interpoint puts **two pages on each sheet**, odd on the front and even on the back.
- **Measure the ratio** from a typical five-page sample. Then: pages, then sheets, then volumes.
- **Sheets per volume** is an agency decision, not a rule. Break volumes at natural boundaries.
- Tell the requester the volume count **before** you start.

---

## Source Citations

- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/): "Adjusting Page Properties, Margins, and Interpoint," and the sections on setting up an embosser (Generic Text only, and the advanced options Add margins, Pad page, and Form feed on full page).
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html), for volumes and page layout.
- The estimator was written for this course and its examples were run.
