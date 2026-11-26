# Lesson 39: Inside the Packages: DOCX, ODT, EPUB, eBraille, NIMAS, and BBX

> **Lesson at a glance**
>
> - **Unit:** Unit 5: Handbook (Supplemental)
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 37](37-reading-xml.md)
> - **You will need:** A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Open a `.docx`, `.odt`, `.epub`, or `.ebrl` file as the zip package it is, and name its main parts.
- Use a few commands to diagnose a Word file: its styles, floating pictures, text boxes, tracked changes, equations, and page breaks.
- Explain how BrailleBlaster stores a document, and what a BBX and a BBZ contain.
- Decide when looking inside a file is the fastest way to solve an import problem.

> [!TIP]
> **Practice files:** `word-01-well-structured.docx`, `word-02-flat-structure.docx`, `word-05-braille-aware-styles.docx`, `sample.odt`, `sample.epub`, and `nimas-style-sample.zip` in the [sample files](../samples/index.md).

## Why this matters

When an import goes wrong, the menu will not tell you why. But the file will. A `.docx` that "has headings" but imports flat is usually a file whose headings are not headings. An EPUB that loses its chapters often has them in the wrong order in its package. A figure that vanished may be a floating picture. Each of these questions can be answered in a minute by looking *inside* the file.

Almost every format in this course is a **zip file** that holds XML. This lesson shows what is inside, and gives you commands to ask the file direct questions.

{HB}

---

## How to use this lesson

Read **The Concept**, then run the commands in **Step by step** on the sample files. You need only a zip tool and a terminal, or a text editor.

> [!NOTE]
> On Windows, you can copy the file, change its extension to `.zip`, and open it in File Explorer. In a terminal, `unzip` works on Linux and macOS, and `python3 -m zipfile -l file.docx` works anywhere Python is installed. Always work on a **copy**.

---

## The Concept

### A package is a zip file with a map

A package is a zip archive that holds many small files and a **manifest** that says what they are. The file extension (`.docx`, `.epub`, and so on) is only a label. The first few entries usually give it away: `[Content_Types].xml` for Word, `mimetype` for OpenDocument and EPUB.

### DOCX: Word

A real listing for `word-01-well-structured.docx`:

```text
[Content_Types].xml
_rels/.rels
docProps/core.xml
word/document.xml          <- the paragraphs
word/styles.xml            <- the definitions of the styles
word/numbering.xml         <- the definitions of the lists
word/_rels/document.xml.rels
word/settings.xml
word/theme/theme1.xml
```

Other parts appear when needed: `word/footnotes.xml`, `word/comments.xml`, and `word/media/` for pictures.

**`word/document.xml`** holds the text. A paragraph is a `<w:p>`. Here is a real heading and a real list item from the sample:

```xml
<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr>
     <w:r><w:t>Chapter 1: Introduction to Chemistry</w:t></w:r></w:p>

<w:p><w:pPr><w:pStyle w:val="ListBullet"/></w:pPr>
     <w:r><w:t>Atoms combine to form molecules</w:t></w:r></w:p>
```

Compare a **fake heading** from the flat file. There is no `pStyle`. It has only direct formatting:

```xml
<w:p><w:r><w:rPr><w:b/><w:sz w:val="36"/></w:rPr>
     <w:t>Chapter 1: Introduction to Chemistry</w:t></w:r></w:p>
```

`<w:b/>` means bold, and `w:sz` is the size in half-points (36 is 18 points). This is the clearest possible picture of the difference between structure and appearance.

A character style, such as *Emphasis* or *Strong*, appears as `<w:rStyle w:val="Emphasis"/>` inside a run, not as direct formatting.

> [!IMPORTANT]
> `document.xml` records a style by its **ID**, which has no spaces: `BBEmptyParagraph`. The **name** you see in Word, `BB Empty Paragraph`, is stored in `styles.xml`. BrailleBlaster, through Pandoc, matches on the **name**.

### ODT: OpenDocument Text

```text
mimetype
content.xml            <- the text
styles.xml             <- the styles
meta.xml
META-INF/manifest.xml
```

In `content.xml` a heading is explicit about its level:

```xml
<text:h text:style-name="Heading_20_1" text:outline-level="1">Chapter 1</text:h>
<text:p text:style-name="P1">Item 1</text:p>
```

`text:h` is a heading, and `text:outline-level` is its level. `text:p` is an ordinary paragraph. In the style name, `_20_` stands for a space.

### EPUB

```text
mimetype
META-INF/container.xml     <- points to the package file
EPUB/content.opf           <- manifest and reading order (spine)
EPUB/nav.xhtml             <- the table of contents
EPUB/toc.ncx               <- an older table of contents
EPUB/text/ch001.xhtml      <- the chapters
EPUB/styles/stylesheet1.css
```

The **`container.xml`** names the package file:

```xml
<rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/>
```

The package file's **`<manifest>`** lists every file, and its **`<spine>`** lists them in **reading order**. If chapters seem out of order after import, read the spine.

### eBraille

BrailleBlaster's eBraille exporter ([Lesson 19](19-ebraille.md)) writes a zip with this layout, taken from its source:

```text
mimetype
META-INF/container.xml
package.opf                <- the package document
index.html                 <- the navigation document
ebraille/document0.html    <- the content
ebraille/css/default.css
```

It is deliberately close to an EPUB. The extension is `.ebrl`.

### NIMAS

A NIMAS zip holds a package file and one or more DTBook files, plus images:

```text
sample-package.opf         <- the manifest
sample-dtbook.xml          <- the content
roller-coaster.png         <- an image, if the manifest lists it
```

See [Lesson 38](38-dtbook-nimas-and-mathml.md).

### BBX and BBZ: BrailleBlaster's own formats

A **BBX** is a single XML file. This is the start of a real one, made from a Markdown file by BrailleBlaster's conversion script:

```xml
<bbdoc xmlns="http://brailleblaster.org/ns/bb"
       xmlns:bb="http://brailleblaster.org/ns/bb"
       xmlns:utd="http://brailleblaster.org/ns/utd">
  <head><bb:version>6</bb:version> … </head>
  <SECTION bb:type="ROOT"><SECTION bb:type="OTHER">
    <BLOCK utd:overrideStyle="Centered Heading" bb:type="STYLE">Title One</BLOCK>
    <BLOCK utd:overrideStyle="Cell 5 Heading" bb:type="STYLE">Section Two</BLOCK>
    <BLOCK bb:type="DEFAULT">Plain paragraph with
      <INLINE bb:type="EMPHASIS" bb:emphasis="BOLD">bold</INLINE> …</BLOCK>
```

You can read the document's whole structure here: `SECTION` and `CONTAINER` hold things together, `BLOCK` is a paragraph or heading, `INLINE` is emphasis, `IMAGE` is a picture, and `bb:type` says what each is. The style name in `utd:overrideStyle` is the style you see in the Style View.

A **BBZ** is a zip. In BrailleBlaster's code, it holds:

- `document.bbx`, the document;
- `bbx_location`, a small pointer file; and
- the original files and images, and any `document.brf` or `document.pef` saved from it.

A file you imported from Word or Markdown is saved as a BBZ.

> [!WARNING]
> Do not edit a BBX or BBZ by hand unless you have a backup and a reason. A small mistake can make the document unreadable. These formats are for **reading**, to understand what BrailleBlaster did.

---

## Step by step

### List and open a package

```bash
unzip -l word-01-well-structured.docx            # list the parts
unzip -p word-01-well-structured.docx word/document.xml | head -c 1500
python3 -m zipfile -l sample.epub                # works without unzip
```

### Diagnose a Word file

Each command below prints counts. Replace the file name.

**Which paragraph styles are used?**

```bash
unzip -p file.docx word/document.xml | grep -o 'w:pStyle w:val="[^"]*"' | sort | uniq -c
```

For `word-01-well-structured.docx` this gives one `Heading1`, two `Heading2`, one `Heading3`, and three `ListBullet`. For `word-02-flat-structure.docx` it gives **nothing**. No paragraph has a style, so the structure is entirely fake. That single result tells you to rebuild or to ask for a better file.

**Are there floating pictures or text boxes?**

```bash
unzip -p file.docx word/document.xml | grep -o '<wp:anchor' | wc -l      # floating pictures
unzip -p file.docx word/document.xml | grep -o '<wp:inline' | wc -l      # pictures in line with text
unzip -p file.docx word/document.xml | grep -o 'w:txbxContent' | wc -l   # text boxes
```

Floating pictures (`wp:anchor`) and text boxes are the ones most likely to be mishandled ([Lesson 33](33-what-makes-a-good-source.md)).

**Are there tracked changes, equations, and hard page breaks?**

```bash
unzip -p file.docx word/document.xml | grep -o '<w:ins ' | wc -l          # tracked insertions
unzip -p file.docx word/document.xml | grep -o '<w:del ' | wc -l          # tracked deletions
unzip -p file.docx word/document.xml | grep -o '<m:oMath>' | wc -l        # equations
unzip -p file.docx word/document.xml | grep -o 'w:br w:type="page"' | wc -l   # page breaks
```

In the test files these returned the expected counts: one insertion, one deletion, and one equation in the tracked-changes test file, and one page break in `word-05-braille-aware-styles.docx`.

**Which custom styles exist?**

```bash
unzip -p file.docx word/styles.xml | grep -o 'w:name w:val="[^"]*"'
```

This lists the style *names*, which is what BrailleBlaster reads.

### Diagnose an EPUB

1. Open `META-INF/container.xml` to find the package file.
2. In the package file, read the `<spine>` to see the reading order.
3. Open each chapter's XHTML in a browser.

---

## Practice

### Tasks

1. List the parts of `word-01-well-structured.docx`. Which part holds the paragraph text, and which holds the definitions of the styles?
2. Run the paragraph-style command on all three Word samples. What does each result say?
3. In `word-05-braille-aware-styles.docx`, the command shows `BBEmptyParagraph`, but Word shows `BB Empty Paragraph`. Explain.
4. Open `sample.epub`'s `container.xml`. What is the package file's path? Then read its spine. How many chapters are in reading order?
5. A teacher says her Word headings "disappear" in BrailleBlaster. You run the style command and it prints nothing. What do you tell her?
6. A figure vanished after import. Which command tells you if the picture was floating?
7. What is the difference between `document.bbx` and a `.bbz`?

### Answer Key

1. The parts are as listed above. **`word/document.xml`** holds the text. **`word/styles.xml`** holds the style definitions, and `word/numbering.xml` the list definitions.
2. File 01: one Heading 1, two Heading 2, one Heading 3, and three List Bullet, so the structure is real. File 02: **nothing**, so the structure is fake. File 05: the margin styles `1-3` and `3-1`, `BBEmptyParagraph`, three `ListParagraph`, the three heading levels, and a `Title`.
3. `document.xml` stores the style **ID**, which has no spaces. The **name**, with spaces, is stored in `styles.xml`. BrailleBlaster matches on the name.
4. The package file is `EPUB/content.opf`. The spine lists the chapter files in reading order. In the sample, two chapters follow the title page.
5. Her headings are not real headings. No paragraph carries a style, so the headings are bold text. She should apply Heading 1, 2, and 3 styles ([Lesson 35](35-word-structure-with-styles.md)).
6. Count `<wp:anchor`. A non-zero count means a floating picture. Also check whether the picture sat alone in its paragraph, which is the other way to lose it.
7. A `.bbx` is the document alone, as XML. A `.bbz` is a zip that holds `document.bbx` along with the original files and images, and any saved BRF or PEF.

---

## Key takeaways

- DOCX, ODT, EPUB, eBraille, NIMAS, and BBZ are **zip files**. Open a copy to see what is inside.
- In a `.docx`, **`w:pStyle`** means a real style, and `w:b` with `w:sz` means direct formatting. Counting `pStyle` tells you at once whether a file's structure is real.
- Style **IDs** are in `document.xml`. Style **names**, which BrailleBlaster reads, are in `styles.xml`.
- `wp:anchor` (floating picture) and `w:txbxContent` (text box) are the warning signs. The tracked-change, equation, and page-break counts explain surprises.
- A BBX is XML with `SECTION`, `BLOCK`, `INLINE`, and `IMAGE`. A BBZ is a zip that holds it. Read them, but do not edit them by hand.

---

## Source Citations

- The BrailleBlaster program source (the conversion script `bbx.lua` and the Pandoc loader), read at commit `369176b`, with the conversion tests run using Pandoc 3.12.1, the version BrailleBlaster bundles, the BBX output of `bbx.lua`, the BBZ archiver, and the eBraille packager.
- ECMA International, *ECMA-376: Office Open XML File Formats*, at [ecma-international.org](https://ecma-international.org/publications-and-standards/standards/ecma-376/).
- OASIS, *Open Document Format for Office Applications (OpenDocument)*, at [oasis-open.org](https://www.oasis-open.org/).
- W3C, *EPUB 3*, at [w3.org/TR/epub-33](https://www.w3.org/TR/epub-33/).
- [Lesson 19](19-ebraille.md) for the eBraille specification.
