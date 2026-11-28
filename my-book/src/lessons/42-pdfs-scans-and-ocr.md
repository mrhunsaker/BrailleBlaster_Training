# Lesson 42: PDFs, Scans, and OCR

> \*\*Lesson at a glance\*\*
>
> - \*\*Unit:\*\* Unit 5: Handbook (Supplemental)
> - \*\*Suggested time:\*\* about 2 hours
> - \*\*Prerequisites:\*\* [Lesson 33](33-what-makes-a-good-source.md), [Lesson 41](41-text-encoding-and-braille-characters.md)
> - \*\*You will need:\*\* A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Tell a text-based PDF from a scanned one using free tools, and say whether a PDF is tagged.
- Extract text from a PDF in the right order, and know when the order will be wrong.
- Run OCR on a scan, and proofread the result for the errors OCR makes.
- Decide when a PDF is not good enough, and ask for a better source.

> [!CAUTION]
> OCR output is a hypothesis, not an authoritative transcription. Always compare it visually with the scan, especially minus signs, decimal points, superscripts, subscripts, columns, table cells, and similar-looking characters in math.

## Why this matters

A PDF is a picture of a page that happens to contain some text. It was built to *look* the same everywhere, not to say what its contents *are*. There is no heading, no list, and often no reading order inside a typical PDF. That makes it one of the poorest sources for braille, and also one of the most common, because teachers and publishers send what they have.

Sometimes a PDF is all you can get. This lesson shows how to get the most out of one, how to tell how bad it is before you start, and how to ask for something better.

> [!NOTE]
> \*\*About the tests in this lesson.\*\* Where this lesson says what BrailleBlaster does with a file, the statement comes from reading BrailleBlaster's conversion script and from running that script on the sample files with Pandoc 3.12.1, the version the program bundles. It has \*\*not\*\* been confirmed by opening the files in the application. Treat each as an expectation, check it in your own copy, and report differences.

---

## How to use this lesson

Read **The Concept** and the **tool table**. If you have a PDF handy, run the commands on it. The OCR exercise at the end asks you to find the errors in a deliberately damaged passage.

> [!NOTE]
> The commands in this lesson use \*\*poppler\*\* (`pdfinfo`, `pdffonts`, `pdfimages`, `pdftotext`, `pdftoppm`) and \*\*Tesseract\*\*, all free. They were run on test files made for this lesson. `ocrmypdf` is also free, and its options are taken from its documentation but were not run here.

---

## The Concept

### Three kinds of PDF

| Kind | What it holds | Where it ranks | What to do |
| ---- | ------------- | -------------- | ---------- |
| **Tagged PDF** | Text, plus a hidden structure of headings, lists, tables, and reading order | Best, but rare | Extract it, and expect a decent structure. Check it anyway |
| **Untagged text PDF** | Text, with no structure | Poor | Extract the text. You rebuild the structure |
| **Scanned (image) PDF** | A picture of each page, and no text | Poorest | **OCR** it first. Every word needs proofreading |

A PDF exported from Word is often untagged and has lost its styles, even though the Word original had real structure. **Always ask for the original file.**

### What goes wrong when you extract text

- **Reading order.** In two columns, text may be extracted line by line across both columns, or one column at a time.
- **Running heads and page numbers** land in the middle of paragraphs.
- **Hyphenation.** A word broken at the end of a line (*me-ters*) may stay broken.
- **Ligatures.** `ﬁ` and `ﬂ` become single characters ([Lesson 41](41-text-encoding-and-braille-characters.md)).
- **Tables** flatten into rows of words, and **math** turns to nonsense, because it was drawn with special glyphs.
- **Images and their captions** may be lost or detached.
- **Footnotes** appear wherever they fell on the page.

### What OCR is

**OCR** (optical character recognition) turns a picture of text into text. It makes characteristic mistakes. Look for these:

| What is on the page | What OCR may read |
| ------------------- | ----------------- |
| `e` | `c` |
| `m` | `rn` |
| `1` (one) | `l` (lowercase L) or `I` |
| `0` (zero) | `O` (capital letter) |
| `lt`, `li` | `h`, `b` |
| `w` | `vv` |
| An apostrophe or a comma | Missing |
| A diacritic (`é`) | A plain letter |

It reads **clean, modern, single-column print** well, and **old, skewed, noisy, or multi-column pages** badly.

---

## Tools

| Tool | What it does | Example |
| ---- | ------------ | ------- |
| `pdfinfo` | Tells you the page count and whether the file is **tagged** | `pdfinfo file.pdf` |
| `pdffonts` | Lists the fonts. **No fonts means no text layer**, so it is a scan | `pdffonts file.pdf` |
| `pdfimages -list` | Lists the images. A scan shows one big image per page | `pdfimages -list file.pdf` |
| `pdftotext` | Extracts the text | `pdftotext file.pdf out.txt` |
| `pdftoppm` | Turns each page into an image, ready for OCR | `pdftoppm -r 300 -png file.pdf page` |
| `tesseract` | OCR on an image | `tesseract page-1.png out -l eng` |
| `ocrmypdf` | OCR on a whole PDF, with cleanup options | `ocrmypdf --deskew --rotate-pages in.pdf out.pdf` |

### What the tests showed

On a test PDF made with a running head, two columns, a page number, and a hyphenated word:

- `pdfinfo` reported **`Tagged: no`**. `pdffonts` listed a font.
- `pdftotext file.pdf` read the **left column, then the right column**, kept the running head and the page number on separate lines, rejoined the hyphenated word (*me-ters* became *meters*), and ended the page with a form-feed character.
- `pdftotext -layout file.pdf` put the **two columns side by side** on each line and left *me-* and *ters* apart. That is faithful to the look of the page and **useless for braille**.

On an image-only PDF, `pdffonts` listed **no fonts**, and `pdfimages -list` showed one image. After `pdftoppm` turned it into a PNG, `tesseract` recognized the text of a clean test image almost perfectly. Real scans will not.

> [!IMPORTANT]
> Use the default `pdftotext` mode for braille, not `-layout`. And a clean synthetic test is not a real scan. Expect real OCR to need real proofreading.

### Other ways in

- **Word can open a PDF** and convert it to an editable document (**File > Open**). The result is sometimes good for simple pages and messy for everything else. Check the headings and lists.
- **Pandoc cannot read PDFs.** It can write them, but BrailleBlaster has no PDF import. You must extract the text first.
- **BrailleBlaster does not read PDFs.** Convert the PDF to text or Word first, or ask for a better source.

---

## Step by step

### Triage a PDF

1. **Run `pdfinfo`** and note `Tagged` and the page count.
2. **Run `pdffonts`**. If it lists fonts, the PDF has a text layer. If it lists none, it is a scan.
3. **Open the PDF** and try to select a few words. Search for a word you can see.
4. **Decide:** tagged or clean text, extract it; a scan, OCR it; anything damaged or math-heavy, ask for the original.
5. **Record** the decision on your Import Log ([Job Aids](../reference/job-aids.md)).

### Extract text from a text PDF

```bash
pdftotext file.pdf out.txt
```

Open `out.txt`, then:

1. **Delete the running heads and page numbers** that fell inside paragraphs. Keep the page numbers in your notes if the braille needs them.
2. **Unwrap** hard-wrapped lines and **clean** invisible characters ([Lesson 41](41-text-encoding-and-braille-characters.md)).
3. **Rebuild the structure**: headings, lists, tables.
4. **Compare with the PDF** page by page.

### OCR a scan

```bash
pdftoppm -r 300 -png scan.pdf page        # one PNG per page, at 300 dots per inch
tesseract page-1.png out -l eng           # writes out.txt
```

For a whole PDF at once, `ocrmypdf` can straighten and rotate pages, and write the recognized text to a separate file with `--sidecar`:

```bash
ocrmypdf --deskew --rotate-pages --sidecar text.txt scan.pdf scan-ocr.pdf
```

A resolution of **300 dpi** is the usual choice for OCR. Then proofread every word against the page ([Lesson 32](32-proofreading-and-quality-assurance.md)).

### Math in a PDF

Do not trust any extraction of mathematics. Look at the page, and **retype each equation** in the ASCII Math Hub ([Lesson 8](08-ascii-math-hub.md)), or ask for the source in LaTeX or Word.

---

## Practice

### The OCR exercise

Below is the passage as printed, and the same passage as OCR returned it. The OCR text has **eight** errors. Find and classify them.

**As printed**

```text
Rivers carry water, mud, and sand from the hills to the sea. The Nile is about 6,650 kilometers long. In 1998, the town built a new bridge. The river's speed is measured in meters per second.
```

**As OCR returned it**

```text
Rivcrs carry water, rnud, and sand from the hills to the sea. The Nile
CHAPTER 2 - RIVERS 41
is about 6,65O kilometers long. In l998, the town buih a new bridge. The rivers speed is measured in meters per sec- ond.
```

### Tasks

1. List the eight errors, and say what OCR mistake each is.
2. Which ones would a spell checker catch?
3. Which would it miss?
4. A teacher sends a PDF. `pdffonts` prints a table with no rows. What is it, and what do you do?
5. `pdftotext -layout` puts two columns side by side. Should you use that output for braille?
6. A PDF of a science chapter has twelve equations. How do you handle them?

### Answer Key

1. The eight errors:
   1. **Rivcrs** for *Rivers*: `e` read as `c`.
   2. **rnud** for *mud*: `m` read as `rn`.
   3. **A line of running head and page number** (`CHAPTER 2 - RIVERS 41`) in the middle of a sentence.
   4. **6,65O** for *6,650*: the digit zero read as the letter `O`.
   5. **l998** for *1998*: the digit one read as a lowercase `l`.
   6. **buih** for *built*: `lt` read as `h`.
   7. **rivers** for *river's*: the apostrophe was lost.
   8. **sec- ond** for *second*: a hyphenated line break was left in the middle of the word.
2. A spell checker catches **Rivcrs**, **rnud**, **buih**, and **sec- ond**.
3. It usually misses **6,65O** and **l998**, because spell checkers tend to skip tokens that contain digits; the **running head**, because those are real words; and **rivers** for *river's*, because that is a real word too.
4. It is a **scan**, because there is no text layer. OCR it, and proofread every word, or ask for the original file.
5. **No.** It keeps the page's *look*, so the columns are interleaved. Use the default extraction, which read the columns in order.
6. Do **not** trust any extraction. Retype each equation in the ASCII Math Hub from the page, or ask for the LaTeX or Word source.

---

## Key takeaways

- A PDF is a picture of a page. Always ask for the **original file**, and ask for a NIMAS file if the title qualifies.
- Triage with `pdfinfo` (tagged?), `pdffonts` (a text layer?), and `pdfimages -list` (a scan?).
- Use the default `pdftotext` for braille. **`-layout` interleaves columns.**
- OCR confuses `e`/`c`, `m`/`rn`, `1`/`l`, `0`/`O`, and `lt`/`h`. A spell checker misses the digit mistakes and the lost apostrophes.
- **Never trust extracted math.** Retype it.
- BrailleBlaster and Pandoc do not read PDFs. Convert the PDF to text or Word first.

---

## Source Citations

- Poppler, *poppler-utils* (`pdfinfo`, `pdffonts`, `pdfimages`, `pdftotext`, `pdftoppm`), at [poppler.freedesktop.org](https://poppler.freedesktop.org/).
- The Tesseract OCR project, at [github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract), and OCRmyPDF, at [ocrmypdf.readthedocs.io](https://ocrmypdf.readthedocs.io/).
- The tests were run on a generated test PDF and a generated scan with poppler and Tesseract 5.3.4.
- [Policy and Standards Background](../reference/policy-background.md), for questions about copying and accessible formats.
