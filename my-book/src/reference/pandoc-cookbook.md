# Pandoc Cookbook

BrailleBlaster opens many formats directly, including `.tex` (LaTeX), `.md`, `.odt`, `.docx`, `.epub`, and `.html`. LaTeX is converted to ASCII Math when the file opens, and BrailleBlaster does not need LaTeX software installed to do it. This is what [Lesson 17](../lessons/17-what-pandoc-does.md) teaches.

You will only need Pandoc yourself when you want a **fallback**: a file BrailleBlaster does not open cleanly, converted to something it does. This page is a short cookbook for that situation.

> [!NOTE]
> Pandoc converts *document structure* between formats. It does not apply braille formatting rules, and it does not convert anything *to* BrailleBlaster. You always finish in BrailleBlaster.

## When to reach for Pandoc

Use a conversion only after the direct route has not worked:

1. Try opening the original with **File > Open**.
2. Check the result: structure, math, and emphasis.
3. If something is wrong and cannot be fixed more quickly by hand, convert to **HTML** and open that instead.

The official User Guide gives the same advice for LaTeX that uses packages or notation BrailleBlaster does not support: convert it to HTML with another application, and open the HTML.

## Install Pandoc

Check first whether it is already installed:

```bash
pandoc --version
```

| System | How |
| ------ | --- |
| Windows | Download the installer from [pandoc.org](https://pandoc.org/installing.html), run it, and then open a new command window and check the version |
| macOS | `brew install pandoc` (needs Homebrew) |
| Linux (Debian or Ubuntu) | `sudo apt install pandoc` |

## Recipes

Run these in a terminal or command window, in the folder that holds your file.

**Markdown to HTML**

```bash
pandoc input.md -o output.html
```

**LaTeX to HTML (standalone page)**

```bash
pandoc input.tex -s -o output.html
```

**LaTeX to Word**

```bash
pandoc input.tex -o output.docx
```

**EPUB to HTML**

```bash
pandoc input.epub -o output.html
```

**Say the formats explicitly** when the file extension is ambiguous:

```bash
pandoc input.txt -f markdown -t html -o output.html
```

**Add a table of contents** to a standalone page:

```bash
pandoc input.tex -s --toc -o output.html
```

**Write math as MathML** (an experiment: verify how BrailleBlaster handles it before relying on it):

```bash
pandoc input.tex -s --mathml -o output.html
```

You can try the first recipes on the [sample files](../samples/index.md). `sample.tex` and `math-foundations.tex` are good practice sources.

## Other LaTeX-to-HTML route

The official guide names **TeX4HT** as an example of a LaTeX-to-HTML converter that works with the standard LaTeX compiler and has very good LaTeX support. It writes XHTML files with the extension `.xht`. **Change the extension to `.xhtml`** so BrailleBlaster recognizes the file.

## Troubleshooting

| Symptom | Likely cause | What to do |
| ------- | ------------ | ---------- |
| "command not found" or "pandoc is not recognized" | Pandoc is not installed, or is not on the path | Reinstall and open a **new** terminal window |
| "File not found" or "cannot open" | You are in the wrong folder, or the name has a typo | Check the folder with `ls` (macOS, Linux) or `dir` (Windows). Put the file in the current folder, or type the full path |
| A warning that math could not be converted | A notation or environment Pandoc does not handle | Read the warning. The affected expression may remain as raw TeX. Rebuild it in the ASCII Math Hub ([Lab 3](../labs/lab-3-when-latex-misbehaves.md)) |
| The converted file looks fine but BrailleBlaster shows flat text | The conversion kept the look and not the structure | Open the converted file in a browser or word processor and check for real headings |
| Garbled characters | A text encoding problem | Re-save the source as UTF-8 and convert again |

## After any conversion

Treat the converted file as a **new import**. Complete an Import Log ([Job Aids](job-aids.md)), check headings, lists, emphasis, and every equation in the Braille View, and keep the original source untouched.
