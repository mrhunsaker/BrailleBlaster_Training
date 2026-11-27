# Lesson 34: Markdown Syntax Guide for Braille Sources

> **Lesson at a glance**
>
> - **Unit:** Unit 5: Handbook (Supplemental)
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 33](33-what-makes-a-good-source.md)
> - **You will need:** A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Write every common Markdown construct correctly: headings, emphasis, lists, quotes, code, tables, links, images, footnotes, math, and metadata.
- Predict what BrailleBlaster does with each construct, using the conversion table.
- Avoid the constructs that lose or break content during import.
- Use `custom-style` blocks to set braille margins, empty paragraphs, and page breaks from Markdown.
- Prepare and check a Markdown file for import.

> [!TIP]
> **Practice file:** `markdown-syntax-tour.md`, inside [markdown-samples.zip](../samples/index.md). It uses every construct in this lesson.

> [!WARNING]
> Do not assume that valid Markdown is necessarily safe to import into BrailleBlaster. This lesson documents observed behavior for a particular conversion pipeline; test the constructs used in your file and check for dropped or flattened content after import.

## Why this matters

Markdown is the simplest way to write a structured document. It is plain text, so it opens in any editor, works well with screen readers and braille displays, survives copying between systems, and is easy to keep under version control. Many authors and teachers already write in it, and **BrailleBlaster opens `.md` files directly**.

Its simplicity is also its trap. Markdown has no single definition, different tools handle the same file differently, and BrailleBlaster ignores or alters several constructs. This lesson is a full syntax guide *and* a map of what happens to each construct on import.

{HB}

---

## How to use this lesson

This is a **reference lesson**. Read the first two sections once, and then use the conversion table whenever you prepare a file. The practice at the end asks you to predict, then check.

---

## The Concept

### Which Markdown?

There are several flavors. **CommonMark** is a careful standard definition of the core. **GitHub Flavored Markdown** adds tables, task lists, and strikethrough. **Pandoc's Markdown** adds footnotes, definition lists, math, line blocks, fenced divs, and more.

BrailleBlaster reads `.md` files with **Pandoc's Markdown reader and its default extensions**. So this lesson follows Pandoc's Markdown. A construct that works on GitHub may behave differently here, and the reverse.

### From text to braille in three steps

1. **Pandoc** reads the Markdown and builds a neutral document structure.
2. BrailleBlaster's script **`bbx.lua`** turns that structure into BrailleBlaster's XML.
3. BrailleBlaster applies **styles** and translates to braille.

Everything in the conversion table below happens in step 2. A construct the script does not know is dropped, and you will not be told.

---

## Syntax reference

### Headings

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4

Heading 1 in the older style
============================

Heading 2 in the older style
----------------------------
```

Leave a blank line before a heading. A space after the `#` signs is required in Pandoc's Markdown.

### Paragraphs and line breaks

A blank line separates paragraphs. A single line break inside a paragraph is a **soft break**, and is treated as a space. For a **hard break**, end the line with a backslash, or with two spaces:

```markdown
First line\
Second line, in the same paragraph.
```

### Emphasis and inline marks

```markdown
*italic* or _italic_
**bold** or __bold__
***bold and italic***
~~strikethrough~~
H~2~O   (subscript)
x^2^    (superscript)
[small caps]{.smallcaps}
[underlined text]{.underline}
`inline code`
```

### Lists

```markdown
- Bullet one
- Bullet two
    - Nested bullet, indented four spaces
- Bullet three

1. First
2. Second
    1. Nested numbered item
3. Third

(a) A lettered list
(b) Another item

- [ ] A task, not yet done
- [x] A task that is done

Term
:   Its definition.
```

Indent nested items by **four spaces** for the most reliable result. Start numbers are respected: a list that begins `5.` begins at five. A list needs a blank line before it.

### Quotations, rules, and code

````markdown
> A block quotation, which may
> run over several lines.

---

    An indented block of four spaces is code.

```python
def greet(name):
    return "Hello, " + name
```
````

### Links and images

```markdown
[link text](https://example.org "Optional title")
![alt text](picture.png "Optional title")
```

**Always write real alt text.** It is the only description of the picture that travels with the file.

### Tables

```markdown
| Month    | Rainfall (mm) | Sunny days |
|:---------|--------------:|-----------:|
| January  |            78 |         11 |
| February |            64 |         13 |
```

The colons in the second row set alignment. The first row is the header row. Cells may contain emphasis, but not block elements such as lists.

### Footnotes

```markdown
A sentence with a note.[^1]

[^1]: The text of the note.
```

### Mathematics

```markdown
Inline math: $E = mc^2$.

Displayed math:

$$\frac{a + b}{c - d}$$
```

The math is **LaTeX math** between dollar signs. See [Lesson 40](40-latex-for-transcribers.md) for how to read it.

### Metadata, raw HTML, and escapes

```markdown
---
title: A Document Title
author: A. Writer
---

A literal asterisk: \*not italic\*.

<div class="note">Raw HTML is passed through.</div>
```

A backslash before a punctuation mark makes it a literal character.

---

## What BrailleBlaster does with each construct

This table is from running `bbx.lua` on `markdown-syntax-tour.md`, with Pandoc 3.12.1. "Verified by test" means the script's output showed it.

| Construct | Result in BrailleBlaster | Advice |
| --------- | ------------------------ | ------ |
| `# Heading 1` | **Centered Heading** | Use for the title or chapter |
| `## Heading 2` | **Cell 5 Heading** | Section |
| `###` to `######` | **Cell 7 Heading**, all the same | Plan the mapping if you use four or more levels |
| Setext headings | Same as `#` and `##` | |
| Paragraph | Body Text | |
| Soft line break | A space | |
| Hard line break | A real line break inside the paragraph | The safe way to keep lines apart |
| `*italic*` | Italics | |
| `**bold**` | Bold | |
| `***both***` | Bold italics | |
| `~~struck~~` | **Plain text. The strikethrough is lost** | Do not rely on it |
| `H~2~O` | The literal text `H_2O` | Use math instead |
| `x^2^` | The literal text `x^2` | Use math instead |
| `[x]{.smallcaps}` | **Bold** | |
| `[x]{.underline}` | Underline | |
| `` `inline code` `` | **Its own displayed block, breaking the sentence** | Avoid inline code in running text |
| Code block | Displayed Blocked Text | |
| `> quotation` | Displayed Blocked Text | |
| `---` rule | A line of hyphens | |
| Bullet list | A list with a typed bullet prefix. Nested lists are kept as nested lists | Check levels after import |
| Numbered, lettered, roman lists | A list with the number or letter typed in, and the start number kept | |
| Task list | A bullet followed by a box character | |
| Definition list | A definition list: the term, then the definition | |
| **Line block (`\|` lines)** | **The conversion fails with an error** | **Never use. Use backslash line breaks** |
| Pipe table | A simple table. The header row is separated by a line. Alignment is ignored. Emphasis in cells is kept | Check the table type ([Lesson 25](25-tables.md)) |
| Link | The link text only. The address is stored but not shown | Spell out any address the reader needs |
| Image inside a sentence | An image, with its alt text | |
| **Image alone in a paragraph** | **Dropped, with its caption** | **Put it inside a sentence** |
| Footnote | A superscript number, as the literal text `^1`, and a "Footnotes" heading with the notes at the end | Decide whether to move notes |
| `$...$` and `$$...$$` | Math, as an inline math element in its own block | Verify in the Braille View |
| YAML metadata | **Ignored** | Build the title page yourself |
| Raw HTML `<div>` | The text inside is kept, the tag is ignored | |
| Backslash escapes | The literal character | |

---

## Braille-aware Markdown

Pandoc's Markdown lets you wrap a paragraph in a **fenced div** with a `custom-style` attribute. BrailleBlaster's script reads that attribute, and recognizes three special names. All three were verified by test:

````markdown
::: {custom-style="3-1"}
This paragraph starts in cell 3, and its runover lines start in cell 1.
:::

::: {custom-style="BB Empty Paragraph"}
:::

::: {custom-style="BB Page Break"}
:::
````

- A style named with **two odd numbers separated by a hyphen**, such as `3-1`, `1-3`, `5-7`, or `7-5`, sets the braille margins directly: the *first-line cell*, then the *runover cell*. The script accepts it only when both numbers are odd, both are 11 or less, and the runover is not more than two cells before the first line.
- **`BB Empty Paragraph`** makes a blank line.
- **`BB Page Break`** makes a page break.

> [!NOTE]
> This is a power-user feature. Use it for the rare element that no ordinary Markdown construct can express, and not as a replacement for headings and lists. The same names work in Word ([Lesson 35](35-word-structure-with-styles.md)).

---

## Step by step

### Prepare a Markdown file for import

1. **Check the structure.** Every chapter and section should start with a `#` heading, with no skipped levels.
2. **Search for the dangerous constructs.** Look for lines that start with `|` but are not table rows (line blocks), for images alone on a line, and for `~~`.
3. **Rewrite poems** with backslash line breaks.
4. **Move images** into a sentence, or add the caption text to the same paragraph.
5. **Replace** `H~2~O`-style marks and `x^2^` with math.
6. **Plan for what the importer drops**: the title block and strikethrough.
7. **Convert it yourself first** if you want to preview the structure. Pandoc can turn the file into HTML, which any browser shows ([Pandoc Cookbook](../reference/pandoc-cookbook.md)).

### Write a poem safely

```markdown
The water slips away at noon\
and leaves the shore a quiet floor,\
a scatter of shells and a bent spoon
```

The lines will arrive as separate lines in one paragraph. They do **not** get the poetry style, so apply it after import ([Lesson 18](18-advanced-formatting.md)).

### Keep a picture and its caption

```markdown
![A bar chart of rainfall by month](chart.png) Figure 2.1 Rainfall by month.
```

The picture and the caption are in one paragraph, so both are kept. Move the caption to its own Caption-style block after import ([Lesson 27](27-images-and-tactile-graphics.md)).

---

## Practice

Use `markdown-syntax-tour.md` and `line-block-test.md` from [markdown-samples.zip](../samples/index.md).

### Tasks

1. Before you open anything, predict what each of the following becomes: `####` heading, `~~struck~~`, `H~2~O`, an inline `` `code` ``, a footnote, and a pipe table. Write the predictions down.
2. Open `markdown-syntax-tour.md` in BrailleBlaster and compare.
3. Open `line-block-test.md`. What happens? Rewrite the poem so that it imports.
4. Write one Markdown fragment that produces: a Cell 5 heading, an empty paragraph, and a paragraph with the margins 1-3.
5. Someone sends a Markdown file in which every figure is on its own line. How do you fix it with the fewest edits?
6. A teacher wants a word to be crossed out in braille. Is Markdown strikethrough a good way to carry that? What should you do?

### Answer Key

1. A `####` heading becomes a **Cell 7 Heading** (same as `###`). `~~struck~~` becomes **plain text**. `H~2~O` becomes the **literal text** `H_2O`. Inline code becomes **its own displayed block**. A footnote becomes `^1` plus a **Footnotes** section. A pipe table becomes a **simple table**.
2. If your results differ, record the difference. Your copy of BrailleBlaster may use a different filter version, or the behavior may have changed.
3. The tested conversion **fails with an error**. Replace each `|` line with a line ending in a backslash, as in the poem example above.
4. This is one correct answer:

   ````markdown
   ## A Cell 5 heading

   ::: {custom-style="BB Empty Paragraph"}
   :::

   ::: {custom-style="1-3"}
   This paragraph has the margins 1-3.
   :::
   ````
5. Add the caption text, or a few words, to the same paragraph as each image. A picture that shares its paragraph with text is not a figure, so it is kept.
6. **No.** Strikethrough is dropped, so the line would be lost. Mark the word in a way that survives, such as a Transcriber's Note, and agree the treatment with the teacher.

---

## Key takeaways

- BrailleBlaster reads Markdown with **Pandoc's Markdown** and its own script. Learn that dialect, not just GitHub's.
- Headings: `#` is Centered, `##` is Cell 5, and `###` to `######` are all Cell 7.
- **Line blocks fail. Stand-alone images vanish. Metadata is ignored.** Write around them.
- Strikethrough is dropped, subscript and superscript become literal characters, and inline code breaks the paragraph.
- `custom-style` blocks can set margins (`3-1`), empty paragraphs, and page breaks.

---

## Source Citations

- The BrailleBlaster program source (the conversion script `bbx.lua` and the Pandoc loader), read at commit `369176b`, with the conversion tests run using Pandoc 3.12.1, the version BrailleBlaster bundles.
- Pandoc, *Pandoc's Markdown*, in the Pandoc User's Guide, at [pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html).
- CommonMark, at [commonmark.org](https://commonmark.org/).
