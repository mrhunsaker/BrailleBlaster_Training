# Lesson 9: The Spatial Math Editor

> **Lesson at a glance**
>
> - **Unit:** Unit 1: Universal Lessons
> - **Suggested time:** about 3 hours
> - **Prerequisites:** [Lesson 7](07-math-translation-toggle.md), [Lesson 8](08-ascii-math-hub.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Decide when meaning depends on position and therefore needs spatial math.
- Choose the right container type: Matrix, Math Templates, Number Line Editor, or Regular Text.
- Build a matrix, aligned equations, a fractional comparison, and a short worked computation.
- Verify spatial alignment and translation in both views.

## Why this matters

Not all mathematics is linear. A long-division problem, a number line, a matrix, or a worked equation template all depend on *position* — numbers stacked, aligned, or arranged in two dimensions — in ways that ASCII Math's left-to-right notation can't represent on its own. Print math and braille math handle this differently, but both still need to preserve the spatial relationships the reader depends on to actually follow the working, not just the final answer. The **Spatial Math Editor** is BrailleBlaster's purpose-built tool for this category of material, and it's significant enough that its underlying approach is the subject of a U.S. patent held by APH (Patent No. US 11,410,575 B2, "Interface and Tools for Accessible Textbook Generation").

---

## How to use this lesson

The first half explains when spatial math should be built with BrailleBlaster's Spatial Math Editor rather than typed as ordinary linear text. The second half is a practice document — create each expression with the appropriate spatial container, then check the Braille View.

---

## The Concept

### Spatial math represents relationships by position

Linear text places symbols one after another. Spatial math uses rows, columns, alignment, fractions, matrices, systems, and other positional relationships.

BrailleBlaster provides a **Spatial Math Editor** for creating and editing these structures. Spatial math cannot be edited as ordinary Print View text in the same way as a paragraph; the cursor must be placed in the spatial math and the editor opened to modify the structure.

### Container type matters

Current BrailleBlaster documentation identifies spatial containers including:

- Number Line Editor
- Matrix
- Math Templates
- Regular Text

The editor also provides row and column controls for structures that require explicit spatial organization.

### Do not fake spatial structure with spaces

A matrix created with spaces and line breaks may look aligned in print but does not necessarily carry the mathematical structure needed for braille. The same is true of a system of equations.

Use the spatial editor when the **relationship among elements depends on position**.

---

## Step by step

1. Place the cursor where the spatial math belongs (or inside existing spatial math you want to edit).
2. Go to **Math > Spatial Math Editor**.
3. Choose the **Container Type** that matches the print structure: Number Line Editor, Matrix, Math Templates, or Regular Text.
4. Use the container-specific settings to configure the structure. For a Matrix, for example: choose the **Translation** (Uncontracted, Direct, ASCII Math, or Literary), decide whether to **Add Ellipsis to Blank Cells**, choose a **Grouping Device** (bracket, parentheses, brace, or vertical bar — each also available in a "big" variant for larger structures), and set the **Wide Overflow Style** (Block and Blank Line, or Indent Columns) for matrices too large to fit on one braille page.
5. Use **Row**/**Column** Previous, Next, and Delete to build the structure to the correct dimensions.
6. Click **Insert** to place the finished spatial math into the document, or **Cancel** to discard the changes.

---

## Worked Demonstration (small, fully correct)

Create:

```text
  3  -1
  2   5
```

as a two-by-two matrix.

Correct workflow:

- Go to **Math > Spatial Math Editor**.
- Select **Matrix** as the container type.
- Set two rows and two columns.
- Enter the four matrix elements.
- Insert the matrix.
- Check the Print View for the intended structure.
- Check the Braille View for correct spatial alignment and math translation.

Do not type four separate lines with spaces and call the result a matrix.

---

## Practice Document

### 1. Matrix

```text
[ 3  -1 ]
[ 2   5 ]
```

### 2. Aligned equations

```text
2x + 3 = 11
x + 1  =  5
```

### 3. Fractional comparison

```text
  3       5
  -   <   -
  4       6
```

### 4. Short spatial computation

```text
   24
-   7
-----
   17
```

### 5. Mixed structure

```text
x + y = 10
x - y =  2
```

Create the structure in the editor rather than simulating alignment with spaces.

---

## Answer Key

### 1. Matrix

Use the **Matrix** container with two rows and two columns.

### 2. Aligned equations

Use a spatial structure that preserves the intended alignment of the equals signs and equation rows. Do not make the alignment dependent on ordinary spaces.

### 3. Fractional comparison

Use a math template that preserves the numerator/denominator relationship. If the intended structure is a fraction, use the fraction structure rather than a slash typed into a paragraph.

### 4. Short spatial computation

Use a spatial math structure when the vertical subtraction layout is instructional or mathematically meaningful. The horizontal line is part of the structure, not a decorative run of hyphens.

### 5. Mixed structure

The two equations form a system. Preserve the row relationship as a mathematical structure.

### Verification rule

The final test is not whether the Print View "looks aligned." The test is whether the Braille View expresses the intended mathematical structure.

---

## Key takeaways

- Spatial math (number lines, matrices, templates, and aligned grids) is built and edited in the separate Spatial Math Editor window, never directly in the Print View.
- Four Container Types cover the common cases: Number Line Editor, Matrix, Math Templates, and Regular Text.
- Matrices support up to 9×9 cells, a choice of grouping device, and two strategies for handling overflow onto multiple braille pages.
- Math Templates (Simple, Fraction, Division) are well suited to worksheet-style problems, including the option to show or hide a worked solution.

---

## Source Citations

- BrailleBlaster current documentation — Making Spatial Math, Spatial Math Editor, and container types.
- BrailleBlaster User Manual — math translation and spatial math.
- BrailleBlaster FAQ — support for spatial math, number lines, matrices, and tables with math.
