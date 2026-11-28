# Lesson 40: LaTeX for Transcribers

> \*\*Lesson at a glance\*\*
>
> - \*\*Unit:\*\* Unit 5: Handbook (Supplemental)
> - \*\*Suggested time:\*\* about 2 hr 30 min
> - \*\*Prerequisites:\*\* [Lesson 7](07-math-translation-toggle.md), [Lesson 37](37-reading-xml.md)
> - \*\*You will need:\*\* A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Read the structure of a LaTeX document: preamble, body, commands, environments, comments, and special characters.
- Say how BrailleBlaster treats LaTeX headings, emphasis, lists, tables, quotations, notes, and math.
- Read common LaTeX math commands in plain English, and predict the MathML structure.
- Spot the constructs that are silently lost, and request a better LaTeX file.

> [!TIP]
> \*\*Practice files:\*\* `sample.tex` and `math-foundations.tex` in the [sample files](../samples/index.md).

> [!CAUTION]
> Do not treat a LaTeX command as proof that the visible output is correct or complete. Macros, packages, custom commands, and included files can change meaning; request the compiled source or a complete project when the supplied `.tex` file is incomplete.

## Why this matters

LaTeX is the standard way mathematicians, scientists, and many teachers write documents with equations. When a professor or a textbook author sends a `.tex` file, you receive the math **as the author typed it**, which is the best case for math. BrailleBlaster opens `.tex` files directly, and the equations become math without anyone retyping them.

But LaTeX is a programming-style language. A transcriber who cannot read it cannot tell whether the conversion went right. This lesson teaches you to read LaTeX, and shows what BrailleBlaster keeps and what it quietly drops.

{HB}

---

## How to use this lesson

Read **The Concept**, then study the **math reading table**. The practice asks you to read equations aloud and check your reading against the structure BrailleBlaster receives. [Lesson 38](38-dtbook-nimas-and-mathml.md) explains MathML, which this lesson uses.

> [!NOTE]
> You do \*\*not\*\* need LaTeX software installed. BrailleBlaster's converter, Pandoc, reads the `.tex` file itself. A LaTeX program is only needed to \*typeset\* a document, which is not part of your job.

---

## The Concept

### The anatomy of a LaTeX file

```latex
\documentclass{article}           % the preamble: settings and packages
\usepackage{amsmath}

\title{Sample LaTeX Document}     % metadata
\author{Test Author}

\begin{document}                  % the body begins here
\maketitle

\section{Introduction}            % a heading
The quadratic formula is:
\begin{equation}                  % an environment: begin ... end
  x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation}
\end{document}
```

| Part | Example | Meaning |
| ---- | ------- | ------- |
| **Command** | `\section{Title}`, `\textbf{word}` | A backslash, a name, and arguments in braces |
| **Environment** | `\begin{itemize} … \end{itemize}` | A block with a start and an end |
| **Preamble** | everything before `\begin{document}` | Settings, packages, and macros. Not the content |
| **Comment** | `% a note` | Everything after a `%` on a line is ignored |
| **Math** | `$x^2$`, `\[ … \]`, `equation`, `align` | Inline math in dollar signs. Display math in an environment |
| **Special characters** | `\% \& \$ \# \_ \{ \}` | A backslash makes a reserved character literal |

### What BrailleBlaster does with LaTeX

These results come from running BrailleBlaster's own conversion script on test `.tex` files with the Pandoc version the program bundles.

| LaTeX | Result in BrailleBlaster |
| ----- | ------------------------ |
| `\section` in an `article` | **Centered Heading** |
| `\subsection` in an `article` | **Cell 5 Heading** |
| `\subsubsection` and deeper | **Cell 7 Heading** |
| `\chapter` in a `book` | **Centered Heading**, with `\section` as **Cell 5** |
| `\textbf` | Bold |
| `\textit`, `\emph` | Italics |
| `\underline` | Underline |
| `\textsc` | **Bold** |
| `itemize`, `enumerate`, nested lists | Lists, with nesting kept |
| `quote` | Displayed Blocked Text |
| `verse` | Displayed Blocked Text, with the line breaks kept |
| `center` | **Plain body text. The centering is lost** |
| `tabular` | A simple table. It may gain an **empty first row**, so check it |
| `\footnote` | A superscript number and a "Footnotes" section |
| `$…$`, `equation`, `align`, `\[ … \]` | Math |
| A simple `\newcommand` macro used in math | Expanded, so the math still works |
| `\title`, `\author`, `\date`, `\maketitle` | **Nothing. The title block is lost** |
| `\includegraphics` inside `figure` | **Dropped, with its caption** |
| **TikZ** pictures | **Silently dropped** |

> [!IMPORTANT]
> \*\*The document class changes the heading levels.\*\* In an `article`, `\section` is the top level. In a `book` or `report`, `\chapter` is. So the same `\section` is a Centered Heading in one file and a Cell 5 Heading in the other. Read the first line of the file, `\documentclass{...}`, before you judge the headings.

---

## Reading math

LaTeX math is a compact way to write what [Lesson 38](38-dtbook-nimas-and-mathml.md) shows as nested elements. The skill is to **read it aloud**.

### Structures

| LaTeX | Read as |
| ----- | ------- |
| `\frac{a}{b}` | *a over b* (the first group is the numerator) |
| `\sqrt{x}` | *the square root of x* |
| `\sqrt[3]{x}` | *the cube root of x* |
| `x^{2}` or `x^2` | *x squared*, or *x to the power 2* |
| `x_{i}` | *x sub i* |
| `x_{i}^{2}` | *x sub i, squared* |
| `\sum_{i=1}^{n} i` | *the sum of i, from i equals 1 to n* |
| `\int_0^1 x\,dx` | *the integral from 0 to 1 of x dx* |
| `\lim_{x \to 0} f(x)` | *the limit as x approaches 0 of f of x* |
| `\begin{matrix}1&2\\3&4\end{matrix}` | *a matrix with rows 1, 2 and 3, 4* |
| `\text{speed}` | the words *speed*, inside math |

Groups are written in **braces**. `x^{n+1}` is *x to the n plus 1*, but `x^n+1` is *x to the n, plus 1*. Those are different equations, and the braces make the difference.

### Symbols

| LaTeX | Meaning | LaTeX | Meaning |
| ----- | ------- | ----- | ------- |
| `\pm` | plus or minus | `\leq`, `\geq` | less than or equal, greater than or equal |
| `\times` | multiplication cross | `\neq` | not equal |
| `\cdot` | multiplication dot | `\approx` | approximately equal |
| `\div` | division sign | `\to` | arrow, *approaches* |
| `\infty` | infinity | `\alpha`, `\beta`, `\theta`, `\pi` | Greek letters |
| `\left( … \right)` | parentheses that grow to fit | `\Delta` | capital delta |

### Reading a structure, not just a string

Ask three questions of any equation:

1. **What is the outermost operation?** (An equals sign, a fraction, a sum.)
2. **What are its parts, in order?** (Numerator and denominator, base and exponent.)
3. **Are any parts themselves structures?** (A fraction whose top is a square root.)

For `\frac{-b \pm \sqrt{b^2-4ac}}{2a}`: the outermost operation is a **fraction**. Its top is *minus b, plus or minus, a square root*. Inside the root is *b squared minus 4ac*. Its bottom is *2a*. That is exactly the nesting BrailleBlaster receives.

---

## Step by step

### Check a LaTeX file before importing

1. **Read the first line.** Note the `\documentclass`, because it sets the heading mapping.
2. **Search for the lost constructs.** Look for `\maketitle`, `\includegraphics`, `tikzpicture`, and `figure`. Plan for each.
3. **Search for `\newcommand` and `\def`.** Simple macros are expanded, but complicated ones may not be.
4. **Scan the packages** in the preamble. A package that changes how text is *typeset* is harmless. One that creates *content* (such as TikZ) is lost.
5. **Open it in BrailleBlaster** and check every equation against the source ([Lab 3](../labs/lab-3-when-latex-misbehaves.md)).

### Ask for a better file

If you can reach the author, ask for:

- standard structure commands (`\section`, not hand-sized bold text);
- math in standard LaTeX math, with `amsmath` where needed;
- **no pictures of equations** and no TikZ for things that must be read, or else a text description;
- pictures placed in a sentence, with a caption written in the text; and
- a plain note of the title and author, since they will not import.

---

## Practice

Use `math-foundations.tex`.

### Tasks

1. Read these aloud in plain English: (a) `\frac{a+b}{c-d}`, (b) `\sqrt{x^2+y^2}`, (c) `x_{i}^{2}`, (d) `x^{n+1}`, (e) `\sum_{i=1}^{n} i`.
2. For each of (a) to (d), name the outermost MathML element.
3. What is the difference between `x^{n+1}` and `x^n+1`?
4. A file starts with `\documentclass{report}` and contains `\chapter`, `\section`, and `\subsection`. What heading style does each get?
5. List everything in `math-foundations.tex` that will not appear in BrailleBlaster, and say why.
6. A `.tex` file contains a TikZ diagram of a triangle. What happens, and what do you do?
7. Write the LaTeX for *the square root of (b squared minus 4ac), all over 2a*.

### Answer Key

1. (a) *a plus b, over c minus d.* (b) *The square root of x squared plus y squared.* (c) *x sub i, squared.* (d) *x to the power n plus 1.* (e) *The sum of i, from i equals 1 to n.*
2. (a) **`mfrac`**. (b) **`msqrt`**. (c) **`msubsup`**. (d) **`msup`**. The structures are in [Lesson 38](38-dtbook-nimas-and-mathml.md).
3. In `x^{n+1}` the whole *n + 1* is the exponent, so it is *x to the n plus 1*. In `x^n+1` only *n* is the exponent, and *+ 1* follows, so it is *x to the n, plus 1*.
4. In a `report`, `\chapter` is the top level: **Centered Heading**. `\section` is **Cell 5 Heading**. `\subsection` is **Cell 7 Heading**.
5. The **title, author, and date** (the `\title`, `\author`, `\date`, and `\maketitle` produce nothing). The **preamble**, which holds settings, not content. Build the title page yourself ([Lesson 24](24-t-page-generator.md)).
6. The picture is **silently dropped**, with no warning. Ask for a text description of the triangle, or write one, and add it as a Transcriber's Note ([Lesson 22](22-transcribers-notes.md)). Consider a tactile graphic ([Lesson 27](27-images-and-tactile-graphics.md)).
7. `\frac{\sqrt{b^2-4ac}}{2a}`.

---

## Key takeaways

- BrailleBlaster reads `.tex` files directly, with no LaTeX software needed, and equations arrive as math.
- **The document class decides the headings.** `\section` is Centered in an `article`, and Cell 5 in a `book`.
- The **title block, TikZ pictures, and figures with their captions are lost**, and `center` loses its centering. Plan for each.
- Read math by structure: outermost operation, then parts in order. **Braces make the groups.**
- Ask authors for standard commands, plain-text descriptions of pictures, and a separate note of the title and author.

---

## Source Citations

- The BrailleBlaster program source (the conversion script `bbx.lua` and the Pandoc loader), read at commit `369176b`, with the conversion tests run using Pandoc 3.12.1, the version BrailleBlaster bundles, with `.tex` test files run through `bbx.lua`.
- Pandoc, *Pandoc User's Guide*, the LaTeX reader and its handling of `\documentclass`, at [pandoc.org/MANUAL.html](https://pandoc.org/MANUAL.html).
- The LaTeX Project, *LaTeX documentation*, at [latex-project.org](https://www.latex-project.org/).
- The MathML structures were generated from LaTeX with Pandoc 3.12.1.
- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/): "Making Math" (opening LaTeX files).
