# Converting LaTeX to HTML

This standalone guide explains how to turn a LaTeX source project into usable HTML for review, web delivery, or downstream import workflows. It covers the two common routes: **Pandoc** for straightforward documents and **make4ht/TeX4ht** for documents that depend heavily on LaTeX packages and TeX-specific layout.

## 1. Understand the source project

Before converting, identify:

- The main `.tex` file (often `main.tex`, `book.tex`, or `thesis.tex`).
- All included files referenced by `\\input{}` or `\\include{}`.
- Bibliography files (`.bib`), image files, custom class files (`.cls`), and style files (`.sty`).
- The compiler expected by the source: pdfLaTeX, XeLaTeX, or LuaLaTeX.
- Whether the document relies on complex mathematics, custom macros, TikZ, tables, footnotes, or cross-references.

Keep the original source tree unchanged. Make a working copy and place generated HTML and support files in a separate output directory.

## 2. Choose a conversion route

| Situation | Recommended route |
|---|---|
| Mostly standard LaTeX, basic sections, lists, tables, and math | Pandoc |
| Complex LaTeX package use or TeX-specific structures | make4ht (TeX4ht) |
| Need to preserve the appearance of a PDF exactly | HTML conversion is not a page-faithful substitute; publish the PDF alongside accessible HTML |
| Need semantic, reflowable HTML | Either route, followed by manual inspection and cleanup |

No converter reproduces every TeX macro or print-layout decision. Expect to review the HTML and repair unsupported constructs.

## 3. Route A — Pandoc

Install Pandoc using the official installation method for your operating system. From a terminal, change to the project directory and convert the main file:

```bash
pandoc main.tex --from=latex --to=html5 --standalone --mathml -o output.html
```

Useful options:

- `--standalone` creates a complete HTML document with a head and body.
- `--mathml` emits mathematical expressions as MathML where supported by the conversion path.
- `--toc` adds a table of contents.
- `--number-sections` numbers section headings.
- `--css=styles.css` links a stylesheet.
- `--extract-media=media` extracts media assets into a directory.
- `--bibliography=references.bib` supplies bibliography data when supported by the source and citation workflow.

Example with a table of contents, extracted media, and a stylesheet:

```bash
pandoc main.tex \
  --from=latex \
  --to=html5 \
  --standalone \
  --toc \
  --number-sections \
  --extract-media=media \
  --css=styles.css \
  -o site/index.html
```

Create the output directory first (for example, `mkdir -p site`). Check Pandoc's conversion messages for unsupported commands or dropped content. If the document uses a custom LaTeX class or extensive macros, Pandoc may not interpret those definitions as TeX would.

## 4. Route B — make4ht / TeX4ht

TeX4ht converts TeX/LaTeX to HTML by processing the document through a TeX engine and translating the resulting structures. The `make4ht` command is the usual build interface.

Install a TeX distribution that includes TeX4ht and make4ht (for example, a current TeX Live installation). Then run:

```bash
make4ht -u -f html5 main.tex
```

Common options and patterns:

- `-u` selects Unicode output.
- `-f html5` selects HTML5 output.
- `-d site/` directs generated files to an output directory (create it first).
- `-l` can be used to request LuaLaTeX in installations where the corresponding engine is configured.

For example:

```bash
mkdir -p site
make4ht -u -f html5 -d site/ main.tex
```

If the project requires XeLaTeX or LuaLaTeX, consult the installed make4ht help and TeX4ht configuration for the appropriate engine invocation. Do not assume a command-line engine switch works identically across TeX distributions.

TeX4ht can handle many constructs that a source-level converter cannot, but specialized packages may still require configuration files or manual correction. Inspect the build log and generated assets.

## 5. Handle mathematics

Math requires deliberate testing because a visually correct expression can still be inaccessible or structurally poor.

1. Inspect inline and display mathematics in the generated HTML.
2. Confirm that fractions, roots, matrices, aligned equations, subscripts, superscripts, and equation numbers survived.
3. Prefer semantic MathML when the toolchain produces reliable MathML.
4. If the HTML uses images or scripts to display equations, verify that equivalent accessible content is available.
5. Test with keyboard navigation and a screen reader where possible.
6. Compare representative expressions against the source and the compiled PDF.

Do not treat a screenshot of an equation as a substitute for machine-readable mathematical structure.

## 6. Handle images, tables, and references

- **Images:** confirm every referenced image was copied to the output and that relative paths resolve. Add meaningful alternative text; do not use filenames as alt text.
- **Tables:** check header associations, reading order, captions, and whether complex merged cells remain understandable.
- **Cross-references:** confirm links to sections, figures, tables, notes, and bibliography entries work.
- **Bibliographies:** verify citations and reference lists are present, correctly linked, and consistently formatted.
- **Fonts and symbols:** verify special characters display correctly and are encoded as Unicode.

Keep related assets in a predictable folder and use relative URLs so the HTML remains portable.

## 7. Validate the HTML

Open the output in at least two browsers and complete these checks:

- The page loads without missing images, stylesheets, scripts, or fonts.
- Heading levels reflect the document hierarchy (do not choose heading levels only for visual size).
- Lists are real HTML lists, not manually typed bullets.
- Tables have meaningful headers and captions where appropriate.
- Links have descriptive text and point to valid destinations.
- Images have useful alternative text or are marked decorative when appropriate.
- The reading order is logical when CSS is disabled.
- Text can be resized and reflowed without loss.
- Mathematics is exposed in an accessible form.
- There are no unexplained omissions compared with the source.

Run an HTML validator (such as the Nu HTML Checker) and address errors that affect semantics, accessibility, or rendering. Validation does not replace human review.

## 8. Common problems and remedies

| Symptom | Likely cause | Response |
|---|---|---|
| Unknown command or missing section | Custom macro or unsupported package | Define or simplify the macro; try make4ht; inspect the source manually |
| Images are missing | Assets were not copied or paths are wrong | Re-run with media extraction or correct relative paths |
| Math is malformed | Unsupported math macro or conversion mode | Isolate the expression, simplify macros, and test MathML output |
| Bibliography is empty | Bibliography toolchain not run or unsupported citation setup | Run the source bibliography workflow; verify the generated references |
| Layout differs from PDF | HTML reflow differs from print pagination | Repair semantic structure and CSS; do not force print-page layout into HTML |
| Build stops on a package error | Missing TeX package or incompatible engine | Install the required package and use the engine specified by the project |

## 9. Suggested production workflow

1. Preserve the original LaTeX project and record its compiler and dependencies.
2. Compile the source to PDF once to establish a baseline and reveal source errors.
3. Convert a working copy using Pandoc or make4ht.
4. Review the build log and list all warnings, unsupported commands, and missing assets.
5. Inspect headings, lists, tables, mathematics, images, notes, and references.
6. Repair the source or conversion configuration; avoid editing generated HTML as the only correction if the conversion will be repeated.
7. Validate the HTML and test keyboard and screen-reader access.
8. Compare the final HTML with the source and PDF; record known differences.
9. Archive the source, conversion command, tool versions, configuration, generated HTML, and review record together.

## 10. Practice exercise

Convert a short LaTeX document containing a title, two section levels, a numbered list, one table, one image, an inline equation, and a displayed equation.

Submit:

- The original `.tex` source and any assets.
- The exact conversion command and converter version.
- The generated HTML and its supporting files.
- A short comparison report listing preserved structures, conversion defects, and corrections.
- Evidence that the HTML was checked for heading hierarchy, reading order, image alternatives, table structure, and mathematical accessibility.

**Key principle:** LaTeX-to-HTML conversion is a transformation of document structure, not simply a change of file extension. Choose the converter based on the source, preserve the source project, and validate the resulting HTML before using it downstream.
