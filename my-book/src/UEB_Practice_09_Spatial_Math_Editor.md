# UEB Practice: The Spatial Math Editor

## How to use this document:

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

## Source Citations

- BrailleBlaster current documentation — Making Spatial Math, Spatial Math Editor, and container types.
- BrailleBlaster User Manual — math translation and spatial math.
- BrailleBlaster FAQ — support for spatial math, number lines, matrices, and tables with math.
