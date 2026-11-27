# Lesson 37: Reading and Working with XML

> **Lesson at a glance**
>
> - **Unit:** Unit 5: Handbook (Supplemental)
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 33](33-what-makes-a-good-source.md)
> - **You will need:** A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Read an XML file: elements, attributes, text, comments, entities, namespaces, and encoding.
- Say whether a file is well-formed, and read the error when it is not.
- Open, pretty-print, and check an XML file with free tools.
- Write simple XPath queries to find headings, page numbers, notes, and images.
- Recognize where XML hides inside the formats you already use.

> [!TIP]
> **Practice file:** `sample-dtbook.xml` in the [sample files](../samples/index.md).

> [!CAUTION]
> Well-formed XML is not necessarily valid against its schema or useful for transcription. Check both syntax and the expected vocabulary/namespace; a file can parse successfully while omitting required structure or using elements incorrectly.

## Why this matters

XML is the language underneath most of the structured formats this course touches. A **NIMAS** file is XML. An **EPUB** and an **eBraille** publication are zip files full of XML and XHTML. A **Word** file is a zip file whose `document.xml` holds the paragraphs. **MathML** is XML. BrailleBlaster's own **BBX** file is XML.

You do not need to write XML to be a good transcriber. But being able to *read* it lets you answer questions no menu can: Does this file really contain the page numbers I was promised? Is that note a production note or part of the text? Why did a heading not come through? This lesson teaches you to read XML calmly.

> [!NOTE]
> **About the tests in this lesson.** Where this lesson says what BrailleBlaster does with a file, the statement comes from reading BrailleBlaster's conversion script and from running that script on the sample files with Pandoc 3.12.1, the version the program bundles. It has **not** been confirmed by opening the files in the application. Treat each as an expectation, check it in your own copy, and report differences.

---

## How to use this lesson

Read **The Concept**, then open `sample-dtbook.xml` in a plain text editor and in a web browser, and work along with the queries. The next two lessons use what you learn here: [Lesson 38](38-dtbook-nimas-and-mathml.md) maps the NIMAS vocabulary, and [Lesson 39](39-inside-the-packages.md) opens the zip packages.

---

## The Concept

### XML is text with a tree inside it

An XML file is plain text. The tags describe a **tree**: one root element that holds other elements, which hold others, down to the text. Here is a fragment of the sample file:

```xml
<level1 id="ch1">
  <pagenum id="p1" page="normal">1</pagenum>
  <h1>Chapter 1: Energy and Motion</h1>
  <p>Energy is the ability to do work.</p>
</level1>
```

| Part | Example | What it is |
| ---- | ------- | ---------- |
| **Element** | `<h1>…</h1>` | A start tag, content, and an end tag |
| **Attribute** | `id="ch1"` | A name and a value, inside the start tag. The value is always quoted |
| **Text** | `Chapter 1: Energy and Motion` | The content between tags |
| **Empty element** | `<img src="a.png"/>` | An element with no content, closed by `/>` |
| **Comment** | `<!-- a note -->` | Ignored by programs |
| **Prolog** | `<?xml version="1.0" encoding="UTF-8"?>` | The first line. It names the encoding |
| **DOCTYPE** | `<!DOCTYPE dtbook PUBLIC …>` | Names the rules (the DTD) the file claims to follow |

An element's **parent** is the one that contains it, its **children** are the ones inside it, and its **siblings** are the ones beside it. In the fragment, `h1` is a child of `level1` and a sibling of `p`.

### Well-formed: the seven rules

A file is **well-formed** if it obeys every one of these. A program must refuse a file that does not.

1. There is **exactly one root element**.
2. Every start tag has an **end tag**, or is self-closed.
3. Elements are **properly nested**: the last one opened is the first one closed.
4. **Attribute values are quoted.**
5. Names are **case-sensitive**: `<P>` is not `<p>`.
6. The characters `<` and `&` in text are **escaped**: write `&lt;` and `&amp;`.
7. Only the **five built-in entities** (`&lt; &gt; &amp; &quot; &apos;`) and numeric ones (such as `&#8226;`) are allowed, unless the file declares others.

These are the errors you meet in practice. The messages are from the standard XML library; other tools word them differently.

| Mistake | Example | Typical message |
| ------- | ------- | --------------- |
| Mismatched nesting | `<a><b>text</a></b>` | Opening and ending tag mismatch |
| Unclosed element | `<a><b>text</b>` | Premature end of data |
| Two roots | `<a/><b/>` | Extra content at the end of the document |
| Unescaped `<` | `<a>5 < 6</a>` | invalid element name |
| Unquoted attribute | `<a id=1/>` | AttValue: " or ' expected |
| HTML entity | `<a>&nbsp;</a>` | Entity 'nbsp' not defined |

> [!NOTE]
> The last one is common. `&nbsp;` is an **HTML** entity, not an XML one. In XML, write the non-breaking space as `&#160;`.

### Well-formed is not valid

**Well-formed** means the syntax is right. **Valid** means the file also follows its **DTD** or **schema**: only the allowed elements, in the allowed order. A file can be well-formed and still invalid, for example a `<p>` placed directly inside `<book>` where the rules forbid it. BrailleBlaster does not require validity, but a publisher's NIMAS file *should* be valid.

### Namespaces

A **namespace** says which vocabulary an element belongs to, so two vocabularies can share a file. The sample file declares DTBook as the default namespace:

```xml
<dtbook xmlns="http://www.daisy.org/z3986/2005/dtbook/" version="2005-3">
```

and uses a **prefix** for MathML:

```xml
<m:math xmlns:m="http://www.w3.org/1998/Math/MathML"><m:mi>s</m:mi>…
```

Every element inside `<dtbook>` is in the DTBook namespace without a prefix. The prefix `m:` is only a local nickname. What matters is the address after `xmlns`. This is why a query for `//h1` finds nothing in a file with a default namespace: you must say which namespace you mean.

### Encoding

The prolog's `encoding="UTF-8"` says how characters are stored. **UTF-8** is the right choice. If the declaration and the real encoding disagree, accented letters and symbols turn to nonsense. See [Lesson 41](41-text-encoding-and-braille-characters.md).

---

## Tools for reading XML

### In a web browser

Drag the file onto a browser window. Firefox and Chrome show an indented, collapsible tree, and report a well-formedness error. This is the fastest check, and it needs no installation.

### In a text editor

Any plain text editor works. A programmer's editor such as **Visual Studio Code** (with an XML extension) or **Notepad++** adds colors, folding, and checking. Always keep **line wrapping on** while you read.

### On the command line

`xmllint` ships with the libxml2 library on Linux and macOS. It is also available for Windows.

```bash
xmllint --noout sample-dtbook.xml          # silent if well-formed
xmllint --format sample-dtbook.xml         # pretty-print to the screen
xmllint --noout --nonet sample-dtbook.xml  # never fetch the DTD from the internet
```

If the file names an external DTD that cannot be loaded, `xmllint` may warn about it. That is not a well-formedness error.

`xmlstarlet` can run queries from the command line:

```bash
xmlstarlet sel -N d=http://www.daisy.org/z3986/2005/dtbook/ -t -v "//d:h1" -n sample-dtbook.xml
```

### With a few lines of Python

```python
from lxml import etree
tree = etree.parse("sample-dtbook.xml", etree.XMLParser(load_dtd=False, no_network=True))
ns = {"d": "http://www.daisy.org/z3986/2005/dtbook/"}
print(tree.xpath("//d:h1/text()", namespaces=ns))
```

---

## XPath: asking questions of a file

**XPath** is a small query language for XML. You describe a path through the tree.

| Expression | Meaning |
| ---------- | ------- |
| `/book` | A `book` element at the very top |
| `//p` | Every `p` anywhere in the file |
| `//level2/p` | Every `p` that is a *direct child* of a `level2` |
| `//level1[@id='ch2']` | The `level1` whose `id` attribute is `ch2` |
| `//img/@alt` | The `alt` attribute of every `img` |
| `//h1/text()` | The text inside every `h1` |
| `count(//p)` | How many `p` elements there are |
| `//li//list` | A `list` nested somewhere inside an `li` |
| `//*[local-name()='h1']` | Any `h1`, whatever its namespace |

For a file with namespaces, either **bind a prefix** (as in the tools above, writing `d:h1`) or use `local-name()`, which ignores the namespace.

---

## Step by step

### Check a file you were sent

1. **Open it in a browser.** If it shows a tree, it is well-formed. If it shows an error, note the line and column.
2. **Read the prolog.** Check the encoding and the DOCTYPE.
3. **Find the root.** For NIMAS it is `dtbook`.
4. **Count what you expect.** Count `h1`, `pagenum`, `img`, and `prodnote` and compare with the print.
5. **Look at the odd elements.** Search for `prodnote`, `sidebar`, `note`, and `math`. Decide how each should be treated.

---

## Practice

Use `sample-dtbook.xml`. Bind `d` to `http://www.daisy.org/z3986/2005/dtbook/` and `m` to `http://www.w3.org/1998/Math/MathML` in your tool.

### Tasks

1. Is the file well-formed? How can you tell?
2. List the text of every `h1` and `h2`.
3. How many `p` elements are there?
4. List the print page numbers, and the `page` attribute of each.
5. What is the text and the `render` attribute of the production note?
6. How many list items are there altogether? How many are at the top level of a list that is directly inside a `level2`?
7. What is the alt text of the image, and what is the caption?
8. Which MathML elements make up the equation?
9. Fix each of these so it is well-formed: `<p>Fish & chips</p>`, `<p>Use <em>care</p></em>`, `<img src=a.png/>`.
10. Write the XPath for "the text of every element that has the attribute `page`".

### Answer Key

1. **Yes.** It opens as a tree in a browser, and a parser such as `xmllint --noout` reports nothing. (A warning about loading the DTD would not matter.)
2. `h1`: *Chapter 1: Energy and Motion* and *Chapter 2: Forces*. `h2`: *Kinds of Energy* and *Calculating Speed*.
3. **5.** Query: `count(//d:p)`.
4. Three page numbers: **1, 2, and 3**, each with `page="normal"`. Query: `//d:pagenum`.
5. Text: *Publisher production note: this chapter is printed in two columns.* The `render` attribute is **`optional`**.
6. **5** list items in all (`count(//d:li)`). **3** are at the top level of the list directly inside the `level2`: `count(//d:level2/d:list/d:li)`. The other two belong to the nested list inside *Potential energy*.
7. Alt text: *A roller coaster at the top of a hill and at the bottom.* Caption: *Figure 1.1 A roller coaster at the top of a hill and at the bottom.* They are the same words in this file.
8. `mi`, `mo`, `mfrac`, `mn`, `mn`, `mo`, `mn`: the fraction 120 over 2, inside an equation that reads *s = 120/2 = 60*.
9. `<p>Fish &amp; chips</p>`; `<p>Use <em>care</em></p>`; `<img src="a.png"/>`.
10. `//*[@page]/text()`.

---

## Key takeaways

- XML is text with a tree inside it. Learn the parts: element, attribute, text, comment, prolog.
- **Well-formed** has seven rules. **Valid** means the file also follows its DTD or schema.
- A **namespace** is an address, not a prefix. Bind it, or use `local-name()`.
- A browser is the quickest well-formedness check, and `xmllint`, `xmlstarlet`, or a few lines of Python do the rest.
- **XPath** lets you count and list what a file really contains.

---

## Source Citations

- World Wide Web Consortium, *Extensible Markup Language (XML) 1.0*, at [w3.org/TR/xml](https://www.w3.org/TR/xml/), and *XML Path Language (XPath)*, at [w3.org/TR/xpath](https://www.w3.org/TR/xpath/).
- The libxml2 project, *xmllint*, at [gitlab.gnome.org/GNOME/libxml2](https://gitlab.gnome.org/GNOME/libxml2).
- The queries and answers were run against `sample-dtbook.xml` with the `lxml` library.
