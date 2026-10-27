# UEB Practice: Transcriber Tasks — Running Heads and Page Numbering

## How to use this document:

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

## Source Citations

- BrailleBlaster current documentation — Setting a Running Head.
- BrailleBlaster current documentation — Setting, adding, editing, and changing page numbers.
- *Braille Formats 2016*, especially the provisions governing running heads and print/braille page numbering.
