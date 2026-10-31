# Sample Files

The lessons give you practice text to copy and paste. Several topics also need **real files**, such as a Word document with genuine heading styles, a LaTeX file, an EPUB, or a NIMAS-style XML set. This page provides them, and the [labs](../labs/index.md) use them.

## Download

- **[all-samples.zip](all-samples.zip)** contains every file below in one download.
- Or choose individual files from the tables on this page.

> [!IMPORTANT]
> These files were generated for this course by `tools/build_samples.py` in the repository. They are **practice files**, not production files. We confirmed their structure with other software (for example, that the well-structured Word file really contains Heading 1, 2, and 3 styles), but we have not opened every file in every BrailleBlaster release. When BrailleBlaster does something different from what a lab expects, **record what you see** and treat it as a finding. That is exactly the habit [Lesson 16](../lessons/16-choosing-an-import-workflow.md) teaches.

## Word documents (Lessons 2 and 12, Lab 1)

| File | What it is | Structure inside |
| ---- | ---------- | ---------------- |
| [word-01-well-structured.docx](word-01-well-structured.docx) | A chemistry chapter built with Word's own styles | 1 Heading 1, 2 Heading 2, 1 Heading 3, 3 List Bullet paragraphs. The italic title and the bold term use the Word character styles *Emphasis* and *Strong* |
| [word-02-flat-structure.docx](word-02-flat-structure.docx) | The same chapter formatted by hand | Every paragraph is Normal. Headings are bold text in larger sizes, and the bullets are a typed bullet character and a tab. The italic and bold are direct formatting |
| [word-03-geometry-three-pass.docx](word-03-geometry-three-pass.docx) | A geometry chapter for the Three-Pass Method | All Normal. Bold headings at three sizes, six tab-and-asterisk list lines, and an italic lead-in |
| [word-04-inconsistent-formatting.docx](word-04-inconsistent-formatting.docx) | A document that formats similar things differently | Three different fake-heading patterns plus one real Heading 2, two list styles, and three different treatments of defined terms |

Open files 01 and 02 side by side. They hold the same words and look nearly identical in Word, yet they carry very different structure. That contrast is the point of [Lesson 2](../lessons/02-opening-word-documents.md).

## Other import formats (Lessons 14 to 17, Labs 2 and 3)

| File | Format | Notes |
| ---- | ------ | ----- |
| [markdown-samples.zip](markdown-samples.zip) | Markdown | Contains `sample.md` (headings, nested list, bold and italic, inline and displayed math, a code block) and `math-demo.md`. They are zipped because they must keep the `.md` extension |
| [sample.odt](sample.odt) | OpenDocument | A title, Heading 1 and 2, a three-item list, bold and italic |
| [sample.epub](sample.epub) | EPUB 3 | Two short chapters, with a list in each |
| [sample.tex](sample.tex) | LaTeX | Sections, two equations, and a nested list |
| [math-foundations.tex](math-foundations.tex) | LaTeX | More mathematics, including inline math in a list and an `equation*` environment |
| [math-foundations-from-tex.html](math-foundations-from-tex.html) | HTML | The result of converting `math-foundations.tex` with Pandoc. This is the "convert to HTML first" fallback from [Lesson 17](../lessons/17-what-pandoc-does.md). Pandoc could not convert one `equation*` block and left it as raw TeX, so compare this file with what BrailleBlaster does when it opens the `.tex` directly |

## NIMAS-style set (Lesson 20, Lab 4)

| File | What it is |
| ---- | ---------- |
| [nimas-style-sample.zip](nimas-style-sample.zip) | A small DTBook XML file and a package file, zipped together |
| [sample-dtbook.xml](sample-dtbook.xml) and [sample-package.opf](sample-package.opf) | The same two files, unzipped |

The content has two chapters, level-2 sections, a nested list, print page numbers, a sidebar, a publisher production note, a figure with a caption, and one MathML fraction.

> [!NOTE]
> This is a **NIMAS-style** teaching file. It has not been validated as a NIMAC file set. Real NIMAS files come to your agency through the NIMAC or your state. When you have access to one, repeat Lab 4 with it. See [Policy and Standards Background](../reference/policy-background.md).

## Plain-text practice sources (Labs 5 to 9)

| File | Used for |
| ---- | -------- |
| [test-page-for-embosser.txt](test-page-for-embosser.txt) | A test page for checking margins and styles on a test emboss (Lab 5) |
| [reflow-paragraph.txt](reflow-paragraph.txt) | One long paragraph for watching text reflow when page properties change (Lab 5) |
| [running-heads-multichapter.txt](running-heads-multichapter.txt) | A three-chapter document for running heads and page numbers (Lab 6) |
| [relaxer-code-and-math.txt](relaxer-code-and-math.txt) | Code and math inside prose, for a relaxation plan (Lab 7) |
| [find-replace-cleanup.txt](find-replace-cleanup.txt) | A document with a deliberate "Johnson" trap for Find and Replace (Lab 8) |
| [play-excerpt.txt](play-excerpt.txt), [original-poem.txt](original-poem.txt), [deep-list.txt](deep-list.txt) | A short original play, an original poem, and a four-level outline (Lab 9) |

The play and the poem were written for this course, so you can reuse them freely.

## Rebuilding the files

Everything on this page is produced by one script, so you can change the content and regenerate it:

```bash
pip install python-docx pypandoc_binary
python3 tools/build_samples.py
```

## Keep your originals

Follow the habit from [Setup](../start/setup.md): keep the downloaded originals in your `sources` folder, and work on copies in `working`.
