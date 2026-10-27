# UEB Practice: Paper Size and Connecting to an Embosser

## How to use this document:

The first half explains how page geometry and embosser configuration interact. The second half is a practice document — work through the scenarios and decide which setting belongs in BrailleBlaster before embossing. The goal is to avoid treating an embosser as a simple "Print" button.

---

## The Concept

### Braille page geometry must agree with the physical paper

BrailleBlaster's Page Properties control the document's page size, lines per page, cells per line, and margins. These values describe the geometry BrailleBlaster uses when laying out the braille.

The physical paper loaded in the embosser must be compatible with those assumptions.

A mismatch can cause:

- text to run beyond the physical page;
- unexpected page breaks;
- an embosser warning that the document is larger than the paper;
- wasted paper;
- a document that appears correct on screen but embosses incorrectly.

### Interpoint is a page-production setting

Interpoint embosses on both sides of the sheet. Single-sided embossing uses one side only. The document's page geometry and the embosser's physical capabilities must both support the selected mode.

### Connecting the embosser is separate from formatting the document

BrailleBlaster supports embossers from manufacturers including Index, Enabling Technology, Braillo, APH (PixBlaster and PageBlaster), IRIE, and ViewPlus. A generic manufacturer option is available when a model is not listed.

A teacher should understand the distinction:

- **Document settings** determine what BrailleBlaster intends to emboss.
- **Embosser settings** determine how that intended braille is sent to the physical device.
- **Paper settings** determine whether the physical sheet can accommodate the document geometry.

---

## Worked Demonstration (small, fully correct)

Suppose a document is intended for standard 11.5-inch by 11-inch braille paper.

A sound setup sequence is:

1. Open **Settings > Page Properties**.
2. Confirm the page size and margins.
3. Confirm cells per line and lines per page.
4. Decide whether the job is single-sided or interpoint.
5. Open **Settings > Embosser Settings**.
6. Select the correct manufacturer and model when available.
7. Confirm that the embosser is connected and available to the computer.
    a. This is a good time to go to **File > Export > Save BRF/PEF**
    b. Verify this file has the correct number of characters per line and lines per page
8. Before producing a large job, emboss a short test.
9. Check the physical page against the expected margins and page numbering.
10. Only then run the full job.

The key verification is physical: **a correct Braille View is not a substitute for a test emboss.**

---

## Practice Document

### Scenario 1 — paper mismatch

```text
BrailleBlaster:
Page Size = 11.5 x 11 inches
Cells Per Line = 40
Lines Per Page = 25

Loaded paper:
8.5 x 11 inches
```

### Scenario 2 — correct paper, wrong interpoint assumption

```text
Document:
Interpoint = Yes

Embosser:
Configured for single-sided production
```

### Scenario 3 — unknown embosser

```text
Embosser:
Manufacturer = not listed
Model = not listed

BrailleBlaster:
Generic manufacturer is available.
```

### Scenario 4 — production job

```text
A 180-page textbook is ready to emboss.
The document has never been physically test-embossed.
```

---

## Answer Key

### Scenario 1

The page geometry is incompatible with the loaded paper. Change the document page settings or load the correct paper before embossing. Do not solve a physical paper problem by reducing text arbitrarily.

### Scenario 2

The document and embosser assumptions disagree. Confirm the desired production mode and configure the document and embosser consistently before starting the job.

### Scenario 3

Use the Generic manufacturer configuration when appropriate, with the available text-only or text-with-margins options. Test the output because a generic configuration is a compatibility fallback, not proof that every embosser-specific feature is supported.

### Scenario 4

Do not immediately emboss all 180 pages. Produce a short test, inspect the physical braille, verify page geometry, and then proceed.

### Production rule

**Paper → Page Properties → Embosser → Test → Full production.**

---
