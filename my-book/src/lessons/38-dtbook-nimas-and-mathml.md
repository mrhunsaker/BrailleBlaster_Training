# Lesson 38: DTBook, NIMAS, and MathML

> \*\*Lesson at a glance\*\*
>
> - \*\*Unit:\*\* Unit 5: Handbook (Supplemental)
> - \*\*Suggested time:\*\* about 2 hr 30 min
> - \*\*Prerequisites:\*\* [Lesson 37](37-reading-xml.md)
> - \*\*You will need:\*\* A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Describe the parts of a NIMAS file set and the structure of a DTBook document.
- Read the DTBook element map and say what BrailleBlaster does with each element.
- Read presentation MathML, including fractions, roots, scripts, and matrices.
- Inspect a NIMAS file for missing page numbers, images, notes, and math before you transcribe.
- Recognize the special classes BrailleBlaster adds to DTBook for plays, verse, and typeforms.

> [!TIP]
> \*\*Practice file:\*\* `nimas-style-sample.zip` (or `sample-dtbook.xml` and `sample-package.opf`) in the [sample files](../samples/index.md).

> [!WARNING]
> Do not infer that a MathML expression is correct merely because its XML is valid. Confirm the mathematical meaning—especially scripts, fractions, roots, matrices, and operators—against the source image or authoritative source before transcription.

## Why this matters

When a textbook arrives as a NIMAS file, you are not looking at a document so much as a *database of a book*: every heading, list, page number, sidebar, image, and equation is labeled by what it is. That is why NIMAS is the best source on the ladder in [Lesson 33](33-what-makes-a-good-source.md). It is also why you must be able to read its labels. A missing `pagenum`, an image without alt text, or an equation stored as a picture will not announce itself.

> [!NOTE]
> \*\*About the tests in this lesson.\*\* Where this lesson says what BrailleBlaster does with a file, the statement comes from reading BrailleBlaster's conversion script and from running that script on the sample files with Pandoc 3.12.1, the version the program bundles. It has \*\*not\*\* been confirmed by opening the files in the application. Treat each as an expectation, check it in your own copy, and report differences.

---

## How to use this lesson

[Lesson 20](20-nimas-production-files.md) teaches the BrailleBlaster side of NIMAS: opening, the Book Tree, and production notes. This lesson teaches the **file side**: what is inside. Read it with [Lesson 37](37-reading-xml.md) and the sample file open.

---

## The Concept

### What a NIMAS file set contains

NIMAS, the National Instructional Materials Accessibility Standard, specifies a **file set** for a book. Its main parts are:

- one or more **content files** in **DTBook** XML, which hold the book;
- a **package file** (`.opf`) that lists the pieces and describes the book;
- the **images**, as separate files; and
- a **PDF** of the title and copyright pages.

> [!NOTE]
> Check the current NIMAS technical specification for the exact required contents, because the details have been revised over time. The parts above are enough for the transcriber's purposes.

BrailleBlaster opens a NIMAS file in two ways, and both were confirmed in its source:

- A single **DTBook `.xml`** file.
- A **`.zip`** that holds a package file. BrailleBlaster looks for `.opf` files inside the zip, reads each one's *manifest*, and loads the files it lists. If the manifest names a file that is not in the zip, it reports "Unable to find file … in zip." So the package file and the content file must agree.

### The shape of a DTBook document

```xml
<dtbook version="2005-3">
  <head>  <meta name="dc:Title" content="…"/> … </head>
  <book>
    <frontmatter>  <doctitle>…</doctitle>  <docauthor>…</docauthor> … </frontmatter>
    <bodymatter>
      <level1> <h1>…</h1> <p>…</p> <level2> <h2>…</h2> … </level2> </level1>
    </bodymatter>
    <rearmatter> … </rearmatter>
  </book>
</dtbook>
```

- `head` holds **metadata**: title, creator, identifier, and language.
- `frontmatter`, `bodymatter`, and `rearmatter` divide the book. Front matter holds the title page material, and rear matter holds glossaries and indexes.
- `level1` to `level6` are **nested sections**. Each is introduced by a heading `h1` to `h6`.

---

## The element map

This table comes from BrailleBlaster's own mapping file, `nimas.parserMap.xml`. It lists what the importer **does with each DTBook element**. Elements that are not listed fall through to a general fallback.

### Structure and headings

| DTBook | BrailleBlaster |
| ------ | -------------- |
| `book` | The root of the document |
| `level1` to `level5`, `frontmatter`, `bodymatter`, `rearmatter` | Sections |
| `doctitle`, `docauthor` | **Moved to the document head. Not in the body.** Build the title page yourself ([Lesson 24](24-t-page-generator.md)) |
| `h1`, `bridgehead` | **Centered Heading** |
| `h2`, `hd` | **Cell 5 Heading** |
| `h3` to `h8` | **Cell 7 Heading** |
| `byline` | Attribution style |
| `p` | Body Text |

> [!IMPORTANT]
> BrailleBlaster picks the heading style from the **`h` number**, not from how deeply the `level` is nested. A `level3` that begins with an `h2` is a Cell 5 heading. Compare the two when a heading looks wrong.

### Lists, definitions, and tables

| DTBook | BrailleBlaster |
| ------ | -------------- |
| `list`, `li` | A list and its items |
| `li class="bai-toc"`, `"bai-ind"`, `"bai-exe"` | A table-of-contents, index, or exercise margin style |
| `dl`, `dt`, `dd` | A definition list: the term, then its definition |
| `table`, `thead`, `tbody`, `tfoot`, `tr`, `td`, `th` | A table, with header, body, and footer rows |
| `bai-tabletn` with `format` = `simple`, `listed`, `stairs`, or `linear` | A table's Transcriber's Note, for each table format ([Lesson 25](25-tables.md)) |

### Notes, boxes, images, and page numbers

| DTBook | BrailleBlaster |
| ------ | -------------- |
| `sidebar` | A **Box** |
| `note` and `noteref` | A note, and a reference to it |
| `blockquote` | A block quotation |
| `prodnote` | A **production note** container, which the **Production Note Manager** lets you keep, hide, or remove |
| `imggroup` | An **image** container |
| `img` | An image, with its alt text |
| `caption` | A **Caption** |
| `pagenum` | A **print page number** |
| `div` | A generic container |
| `a`, `dfn`, `span` | An inline span with no special style |
| `br` | A line break |

### Poetry, plays, and line numbers

| DTBook | BrailleBlaster |
| ------ | -------------- |
| `poem`, `linegroup`, `line` | A real **poem** with stanzas and lines, so the poetry styles apply |
| `linenum` | A **poem line number** |
| `span class="linenum"` | A **prose line number** |
| `bai-play`, `bai-verse`, `bai-stage` with `level` 0 or 1 | Play, verse-play, and stage-direction styles with fixed margins ([Lesson 18](18-advanced-formatting.md)) |

### Emphasis, math, and the rest

| DTBook | BrailleBlaster |
| ------ | -------------- |
| `strong` | Bold |
| `em` | Italics |
| `span class="underline"` | Underline |
| `bai-script` | Script |
| `bai-trans1` to `bai-trans5` | Transcriber-defined typeforms 1 to 5 |
| `sup` | Superscript |
| `math` | **Math**, read by a MathML importer |
| anything not listed (for example `sub`, `cite`, `q`, `abbr`, `code`) | **The fallback importer** |

> [!NOTE]
> The `bai-` names are extra elements and classes that BrailleBlaster recognizes on top of standard DTBook. A publisher's NIMAS file will normally not use them. They matter if a file was prepared for braille production, and they show what BrailleBlaster is able to receive.
>
> What the fallback importer does with an unlisted element (such as `sub` for subscripts) has not been tested. Search a file for the elements you need, and check them.

---

## Reading MathML

NIMAS stores math as **presentation MathML**: XML that describes how an equation is *laid out*. It is also what BrailleBlaster receives when it converts LaTeX or a Word equation. Once you recognize about a dozen elements, you can read any of it.

### The elements

| Element | Meaning | Example |
| ------- | ------- | ------- |
| `mi` | An identifier (a variable or name) | `<mi>x</mi>` |
| `mn` | A number | `<mn>120</mn>` |
| `mo` | An operator or symbol | `<mo>+</mo>` |
| `mtext` | Plain text inside math | `<mtext>speed</mtext>` |
| `mrow` | A group read as one unit | `a + b` |
| `mfrac` | A fraction: numerator, then denominator | |
| `msup`, `msub`, `msubsup` | Superscript, subscript, or both: base, then the script(s) | |
| `msqrt` | A square root | |
| `mroot` | A root with an index: radicand, then index | |
| `mtable`, `mtr`, `mtd` | A table or matrix: rows of cells | |
| `mspace` | A space | |

The key idea is **nesting**: an element's children are its parts, in order.

### Worked readings

These structures were produced from LaTeX by the same Pandoc version BrailleBlaster uses. Each shows how the nesting mirrors the equation.

| Equation | Structure (read inside out) |
| -------- | --------------------------- |
| *E = mc²* | row( mi E, mo =, mi m, **msup**( mi c, mn 2 ) ) |
| (a + b) / (c − d) | **mfrac**( row( a + b ), row( c − d ) ) |
| √(x² + y²) | **msqrt**( row( **msup**( x, 2 ), +, **msup**( y, 2 ) ) ) |
| ³√x | **mroot**( mi x, mn 3 ) |
| xᵢ² | **msubsup**( mi x, mi i, mn 2 ) |
| xⁿ⁺¹ | **msup**( mi x, row( n + 1 ) ) |
| speed = d/t | row( mtext speed, mo =, **mfrac**( d, t ) ) |
| a 2 × 2 matrix | **mtable**( **mtr**( **mtd** 1, **mtd** 2 ), **mtr**( **mtd** 3, **mtd** 4 ) ) |

Notice that in *xⁿ⁺¹* the exponent is **one `mrow`**. That grouping is exactly what the parentheses do in the ASCII Math of [Lesson 8](08-ascii-math-hub.md).

### Warning signs in NIMAS math

- An **`img` where an equation should be.** The equation is a picture, and BrailleBlaster cannot read a picture. You must retype it, or ask for MathML.
- A **very flat `mrow`** with no `mfrac` or `msup` for what is obviously a fraction. The structure is wrong, and the braille may be too.
- **Invisible operators and spaces.** Equations can contain empty or space elements. They are normal.

---

## Step by step

### Inspect a NIMAS file set before you start

1. **Unzip a copy** of the file set.
2. **Open the `.opf`** in a text editor. Find the `manifest` and check that every `item` it lists exists in the folder.
3. **Open the DTBook `.xml`** in a browser to confirm it is well-formed ([Lesson 37](37-reading-xml.md)).
4. **Count the things you can compare with the print**:
   - `//pagenum`: do the print page numbers run in order and without gaps?
   - `//imggroup` and `//img`: is the number right, and does each `img` have an `alt`?
   - `//prodnote`: what kinds are there, and who are they for?
   - `//math` and any `img` inside a math sentence.
   - `//table`: how many, and how wide?
5. **Open it in BrailleBlaster**, use the Book Tree, and compare the outline with the print table of contents.

---

## Practice

Use `sample-dtbook.xml` and `sample-package.opf`.

### Tasks

1. Open `sample-package.opf`. What file does its manifest list? Does it exist in the sample?
2. For each of these DTBook elements in the sample file, say what BrailleBlaster is expected to make of it: `h1`, `h2`, `sidebar`, `prodnote`, `pagenum`, `imggroup`, `caption`, `strong`, and the nested `list`.
3. Where does the `doctitle` go? What does that mean for you?
4. Read this MathML in words: `msqrt( row( msup( x, 2 ), +, msup( y, 2 ) ) )`.
5. Write the structure for *a/b + c/d*.
6. A NIMAS file has an `img` where the print has a long equation. What do you do?
7. A `level3` begins with an `h2`. What heading style is expected?
8. List three checks you make on a NIMAS file before transcribing.

### Answer Key

1. It lists `sample-dtbook.xml`, which is in the sample. (If it were missing, BrailleBlaster would report that it cannot find the file in the zip.)
2. `h1` becomes a **Centered Heading**; `h2` a **Cell 5 Heading**; `sidebar` a **Box**; `prodnote` a **production note** you can keep, hide, or remove; `pagenum` a **print page number**; `imggroup` an **image container**; `caption` a **Caption**; `strong` **bold**; the nested list a list with a second level.
3. It is moved to the **document head**, so it does not appear in the body. You must build the title page yourself.
4. *The square root of x squared plus y squared.* The radicand is one group.
5. `row( mfrac( a, b ), mo +, mfrac( c, d ) )`.
6. Do not transcribe the picture. Retype the equation in the ASCII Math Hub ([Lesson 8](08-ascii-math-hub.md)), and ask the publisher for a file with the math in MathML.
7. A **Cell 5 Heading**, because the style follows the `h` number and not the nesting.
8. Any three of: the manifest matches the folder; the XML is well-formed; the page numbers are in order; every image has alt text; the math is MathML and not pictures; the production notes have been reviewed; the outline matches the print.

---

## Key takeaways

- A NIMAS file set is DTBook XML plus a package file, images, and a PDF. BrailleBlaster needs the package file's manifest to agree with the folder.
- BrailleBlaster picks the heading style from the **`h` number**: `h1` Centered, `h2` Cell 5, `h3` to `h8` Cell 7.
- **`doctitle` and `docauthor` go to the head**, so the title page is yours to make.
- `prodnote`, `sidebar`, `imggroup`, and `pagenum` each map to a distinct BrailleBlaster element. `poem` markup gives real poetry containers.
- Read MathML by nesting: `mfrac`, `msup`, `msqrt`, and `mtable` hold their parts in order. A picture of an equation is a warning sign.

---

## Source Citations

- The BrailleBlaster program source: the NIMAS mapping file `nimas.parserMap.xml` and the NIMAS zip loader, read at commit `369176b`. MathML structures were produced with Pandoc 3.12.1.
- DAISY Consortium, *ANSI/NISO Z39.86 (DTBook)*, at [daisy.org](https://daisy.org/).
- *National Instructional Materials Accessibility Standard (NIMAS)*, the Center for Accessible Technology in Education (CAST) and the NIMAC, at [nimac.us](https://www.nimac.us/).
- World Wide Web Consortium, *Mathematical Markup Language (MathML)*, at [w3.org/TR/MathML3](https://www.w3.org/TR/MathML3/).
- [Policy and Standards Background](../reference/policy-background.md).
