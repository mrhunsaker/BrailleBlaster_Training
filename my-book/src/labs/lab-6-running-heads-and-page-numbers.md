# Lab 6: Running Heads and Page Numbers

**Time:** about 60 minutes. **Needs:** [Lesson 21](../lessons/21-running-heads-and-page-numbers.md). **File:** `running-heads-multichapter.txt` from the [sample files](../samples/index.md). **Job aid:** the Page Numbering and Running Head Plan in [Job Aids](../reference/job-aids.md).

## Scenario

In print, running heads and page numbers are usually automatic. In braille, nothing is automatic: you decide what appears, where, and on which pages. You are preparing a short three-chapter guide for a student who will refer to the print edition in class, so the **print page numbers** matter as much as the braille ones.

## Before you start: make a plan

Fill in the Page Numbering and Running Head Plan from the Job Aids page *before* you open BrailleBlaster. Decide:

- the running head text, and whether it fits at the top of the page with the longest page number;
- whether the document is **single-sided** or **interpoint**;
- where braille page numbers and print page numbers should appear, according to your agency;
- which print page each chapter starts on. For this lab, assume Chapter 1 starts on print page 1, Chapter 2 on print page 4, and Chapter 3 on print page 9.

## Steps

### 1. Set up the document

1. Paste `running-heads-multichapter.txt` into a new document.
2. Apply heading styles to the title and the three chapter titles ([Lesson 5](../lessons/05-heading-levels.md)).

### 2. Set the page number options

1. Go to **Settings > Page Numbers**.
2. Choose **Interpoint** or **Single-Sided**.
3. Choose the placement of the **braille** page numbers and the **print** page numbers, and your **continuation indicators**.
4. Click **OK** (not **Make Default**) while you are practicing.

### 3. Add the running head

1. Go to **Insert > Running Head**. The default is **No Running Head**.
2. Choose **Enter Title** and type your running head.
3. Click **OK**.

The Running Head tool adds the same running head to your braille pages, **except for t1 and braille page 1**. It is a single title for the document. If the print book's running heads change by chapter, do not try to force that here. Decide with your agency's standards how the braille edition should handle it, and note your decision in the plan.

Before you accept the running head, check that its length fits at the top of the page and still works for **all** print page numbers, as *Braille Formats 2016* requires. Test the longest print page number you will use.

### 4. Add print page numbers

1. In the Print View, type the print page number where each print page break occurs. For this lab, put `1`, `4`, and `9` at the start of the three chapters.
2. Highlight each number and apply **Styles > Miscellaneous > Page**, or use the Page button on the Styles toolbar.
3. If a print page begins in the middle of a braille page, BrailleBlaster shows a print page change indicator across the page. Look for these in the Braille View.

### 5. Review

1. Open **File > Braille Preview** and navigate by **print page**, then by **braille page**, then by **ordinal page**. Confirm that they give you different numbers where they should.
2. Open the **Page Change List** in the Page Number dialog and view the changes you made.
3. Make one deliberate edit: change one print page number, then check the Page Change List again. Then delete that number and check again.

## Expected observations

- There is no running head on t1 or braille page 1, and there is one on the other braille pages.
- Print page numbers and braille page numbers advance independently.
- The Page Change List shows every edit to the page numbers, which is how you find a number you changed by accident.

## Debrief questions

1. What would a student lose if the print page numbers were missing?
2. Why does a running head need to be tested against the *longest* page number, not the first?
3. What is the risk of adding a page number by typing it and forgetting to apply the Page style?
4. Where in your plan did you have to make a decision that no tool made for you?
