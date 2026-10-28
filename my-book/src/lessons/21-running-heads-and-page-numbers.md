# Lesson 21: Running Heads and Page Numbering

> **Lesson at a glance**
>
> - **Unit:** Unit 3: Transcriber-Focused Lessons
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 5](05-heading-levels.md), [Lesson 13](13-paper-size-and-embossers.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Tell print page numbers from braille page numbers.
- Add a running head with **Insert > Running Head** and check that it fits.
- Configure page numbers under **Settings > Page Numbers**.
- Edit and delete page numbers deliberately and review them in the Page Change List.

## Why this matters

Every finished braille volume needs to tell its reader where they are — which print page this braille page corresponds to, which braille page they're on, and, for a multi-volume or sectioned work, enough context to navigate confidently without sight. Page numbering is not a cosmetic finishing touch; it's core to how a braille reader locates material, matches a braille page back to a print page a sighted teacher or parent is looking at, and cites specific pages in discussion or homework. Because print and braille pagination essentially never line up one-to-one (braille takes more physical space per unit of text), BrailleBlaster tracks print and braille page numbers as two related but independent systems, and this lesson is about managing both correctly — along with the running head that helps orient a reader at the top of every page.

Given how much of a finished, professional transcription's quality shows up specifically in correct, consistent pagination, this lesson runs longer and deeper than most others in this course — deliberately so.

---

## How to use this lesson

The first half explains running heads and print/braille page numbering as separate production systems. The second half is a practice document — determine what should happen on each page and which BrailleBlaster control should be used.

---

## The Concept

### Running heads and page numbers serve different purposes

A **running head** identifies the work or section at the top of braille pages. Page numbers identify page location.

BrailleBlaster's Running Head tool can place a running head on braille pages, with exceptions for the title/preliminary page behavior defined by the software.

Page-number settings control:

- print page numbers;
- braille page numbers;
- continuation indicators;
- placement of even and odd page numbers;
- page-number types such as ordinary, T-pages, and P-pages.

### Print page numbers are not braille page numbers

A print page number tells the reader where the content appeared in the print source. A braille page number identifies the braille page.

BrailleBlaster can automatically add braille page numbers, while print page indicators are inserted where print-page changes occur.

### Running heads must fit

Before adding a running head, confirm that its length works with the page geometry and with the print-page-number arrangement required for the job. A running head is not simply a copied Word header.

### Editing page numbers is a controlled operation

BrailleBlaster's Page Number Dialog can edit print page indicators, print page numbers, braille page numbers, and page-number types. The Page Change List can also show changes made to page numbering.

---

## Step by step in BrailleBlaster

### Adding a Running Head

The **Running Head** is text that appears at the top of every braille page in the document except the very first transcriber page (t1) and braille page 1 — it doesn't need to introduce itself on the page a reader lands on first, but it helps orient them on every page after that.

1. Go to **Insert > Running Head**.
2. In the small window that opens, **No Running Head** is selected by default (many short transcriptions don't need one at all). Select **Enter Title** instead, and type the running head text.
3. Click **OK** to save.

> **Note:** Before finalizing a running head, confirm its length actually fits at the top of the braille page alongside the print page number for *every* print page number the document will use — including the longest ones — as required by *Braille Formats 2016*. A running head that fits comfortably next to "5" may not fit next to "247" or a hyphenated combined page number; check the longest cases, not just the first one.

### Adding Page Numbers

**Adding a print page number:**

1. Type the print page number into the document at the point where the print page break occurs.
2. Highlight that number and go to **Styles > Miscellaneous > Page**, or use the corresponding Styles toolbar button.
3. If the number falls in the middle of a braille page (as it usually will, since braille and print pagination rarely align), a page-change indicator appears across the page automatically, with the print page number placed at the right margin.

**Adding a page-change indicator with no print page number** (for material with no visible print page numbers, where the page break itself is still worth marking):

1. Place the cursor before the point where the page changed.
2. Go to **Insert > Blank Print Page Indicator**.

**Adding braille page numbers:** Braille page numbers are generated automatically as you work — you generally don't add them by hand. To force an additional braille page break where BrailleBlaster wouldn't otherwise put one (to keep material together, or to match a required layout), place the cursor and use **Edit > Page Break** (`Ctrl+Enter`); the break is inserted after the cursor, pushing everything following it onto the next braille page. Note that there must be text after the cursor for Page Break to work.

### Editing Page Numbers

All page-number editing happens through one central dialog: place the cursor anywhere on the page you want to change, then go to **Edit > Edit Page Number** (or right-click and choose it from the context menu) to open the **Page Number Dialog**. From there:

- **Print Page Indicator tab** — change a previously-entered print page number. If you enter a hyphen to represent a combined range (for a print page numbered as a span, for instance), the **Runover Page Numbers** options become available: **Combined** displays runovers as a hyphenated combination of both numbers, while **Implied** displays only the second number.
- **Print Page Number tab** — change either the **Continuation Letter** (all following runovers of that print page automatically update to match) or the specific **Page Number** for just that one instance, without affecting the surrounding sequence. Numbers here are entered in ASCII.
- **Braille Page Number tab** — set the braille page number directly for the current page, and choose whether that page carries the document's Running Head (Yes/No).
- **Page Number Type tab** — switch between Normal, T-page, and P-page for the current page onward, as described above.

### Deleting Page Numbers

**Deleting a print page indicator** removes the print page number and all its continuation indicators, while leaving the affected pages in the document (they simply carry no print page number afterward; all other print page numbers in the document are unaffected): in the Page Number Dialog's Print Page Indicator tab, click **Delete Indicator**, then **OK**.

**Deleting a specific print page** removes just that one print page number and continuation letter — the following braille page absorbs it. For example, deleting print page "c5" removes it, and the next braille page, previously "d5," becomes the new "c5." Use the Print Page Number tab's **Delete Page** button, then **OK**.

**Deleting a braille page number** isn't a direct dialog action — delete the text (or blank space) occupying that page instead. To change *where* braille page numbers appear on the page (or to remove them from the document layout entirely), use **Settings > Page Numbers**, the same document-default dialog covered above.

### Reviewing Your Work: The Page Change List

Every manual page-number change you make is logged in the Page Number Dialog's **Page Change List** tab — a running audit trail of every edit, each with a **Go To** button that jumps straight to that page. Before finalizing a document, review this list as a matter of course: it's the fastest way to confirm every manual page-number intervention was intentional, and to catch a stray change that doesn't belong. Unwanted entries can be checked and removed with the **Delete** button at the bottom of the list.

---

## Worked Demonstration (small, fully correct)

Suppose a textbook begins:

```text
Print page 42:
Chapter 3 — Weather

Print page 43:
Cloud Formation
```

Desired braille production:

- A running head is required by the production specification.
- Print page 42 must be represented at the correct print-page location.
- The next print page must generate the appropriate continuation behavior.
- Braille page numbers should remain distinct from print-page numbers.

Workflow:

1. Set the running head with **Insert > Running Head**.
2. Set the page-number configuration under **Settings > Page Numbers**.
3. Add or verify print page numbers.
4. Inspect the first occurrence of a page change.
5. Inspect a continuation page.
6. Check Braille View.

---

## Practice Document

### Scenario 1 — running head

```text
Running head requested:
"INTRODUCTION TO BIOLOGY"

The document is 120 braille pages long.
```

### Scenario 2 — print page break

```text
The source changes from print page 57 to print page 58
in the middle of a braille page.
```

### Scenario 3 — preliminary pages

```text
A preliminary section should use P-page numbering.
The main body should later return to ordinary braille page numbering.
```

### Scenario 4 — transcriber-generated pages

```text
A transcriber-created section is inserted before the main text.
The agency requires T-page numbering.
```

### Scenario 5 — page number correction

```text
The current print page number is 84b,
but it should be 84c because an additional continuation page was inserted.
```

---

## Answer Key

### Scenario 1

Use **Insert > Running Head** and verify its length and interaction with page-number lines.

### Scenario 2

Insert or verify the print-page indicator at the correct source boundary. Do not manually type a page number into ordinary body text and assume it will behave as a page indicator.

### Scenario 3

Use the Page Number Dialog to select **P-page** behavior for the preliminary section and return to the normal type when the main text begins.

### Scenario 4

Use **T-page** numbering for the transcriber-generated material when required by the production specification.

### Scenario 5

Use the Page Number Dialog to edit the continuation letter rather than manually changing the visible text. Verify that following continuation pages update appropriately.

### Core principle

**Running heads identify; print-page indicators locate the source; braille page numbers locate the braille volume.**

---

## Key takeaways

- BrailleBlaster tracks print page numbers and braille page numbers as two independent, related systems; a single print page routinely spans multiple braille pages via a lettered continuation sequence (5, b5, c5...).
- Running Head placement, and default print/braille page number placement, are both set under **Settings > Page Numbers**; the Running Head itself is added via **Insert > Running Head**.
- Braille pages can be typed as Normal, T-page (transcriber front matter), or P-page (other preliminary material) via the Page Number Dialog's Page Number Type tab, and a type persists until explicitly changed again.
- All page-number edits — print or braille — flow through **Edit > Edit Page Number**, and every manual change is logged in the Page Change List for later review.
- Check a running head's fit against the longest page number the document will use, not just the first one.

---

## Source Citations

- BrailleBlaster current documentation — Setting a Running Head.
- BrailleBlaster current documentation — Setting, adding, editing, and changing page numbers.
- *Braille Formats 2016*, especially the provisions governing running heads and print/braille page numbering.
