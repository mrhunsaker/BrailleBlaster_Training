# Lab 3: When LaTeX Misbehaves

**Time:** about 60 minutes. **Needs:** [Lessons 7](../lessons/07-math-translation-toggle.md), [8](../lessons/08-ascii-math-hub.md), [15](../lessons/15-importing-latex-xml-nimas-epub.md), and [17](../lessons/17-what-pandoc-does.md). **Files:** `math-foundations.tex` and `math-foundations-from-tex.html` from the [sample files](../samples/index.md). **Reference:** the [Pandoc Cookbook](../reference/pandoc-cookbook.md).

## Scenario

A professor sends a LaTeX file of a math handout. BrailleBlaster opens `.tex` files directly and converts the LaTeX to ASCII Math, so most files just work. Sooner or later one does not, because it uses a package or a notation BrailleBlaster does not support.

The official guidance for that moment is to **convert the document to HTML with another tool, and open the HTML instead**. This lab walks through finding a problem, then using the fallback.

## Part A: Open the LaTeX directly

1. Open `math-foundations.tex` with **File > Open**.
2. Check the Style View and Breadcrumbs. Do the three sections arrive as headings, and the three list items as a list?
3. Find each of the five expressions in the table below in the Print View. Are they highlighted pink (flagged as math)? The first section also contains three single-letter inline variables, *E*, *m*, and *c*. Check those too.
4. Read the Braille View for each expression.

| Expression | In the Print View as math? | Braille looks right? | Notes |
| ---------- | -------------------------- | -------------------- | ----- |
| `E = mc^2` (displayed) | | | |
| `x = (-b ± √(b² − 4ac)) / 2a` (displayed, in an `equation*` environment) | | | |
| `ax^2 + bx + c = 0` (inline, inside a list item) | | | |
| `b^2 − 4ac` (inline, inside parentheses) | | | |
| `a^2 + b^2 = c^2` (displayed) | | | |

**What to watch for.** The `equation*` environment is the kind of notation that some converters struggle with, and it is the one equation Pandoc could not convert when it produced the sample HTML file. If BrailleBlaster handles it, good. If it does not, you have just found the situation this lab is about.

## Part B: The HTML fallback

1. Open `math-foundations-from-tex.html` with **File > Open**.
2. Check the same five expressions.
3. Find the equation that Pandoc left as raw TeX. What does BrailleBlaster do with it?
4. Decide what you would do about it in a real job.

## Part C: Fixing a single expression

Wherever an expression is wrong or missing, you have two sound options:

- **Replace it with the ASCII Math Hub.** Select the expression, open **Math > ASCII Math Hub**, build the correct expression, and use **Replace Current Math**. See [Lesson 8](../lessons/08-ascii-math-hub.md).
- **Retype it and flag it** with `Ctrl+M`, then choose Nemeth Block or Inline as in [Lesson 7](../lessons/07-math-translation-toggle.md).

Whichever you choose, finish by checking the Braille View.

## Part D: Write the procedure

Write a five-line procedure that a colleague could follow the next time a LaTeX file misbehaves. Include when to give up on the conversion and fix the math by hand.

## Expected observations

The directly opened `.tex` file and the HTML file are two routes to the same content. Neither is guaranteed to be perfect, and the important skill is **noticing**. You should find that the headings and list arrive in both, and that the math needs line-by-line verification in both.

## Debrief questions

1. Which route was faster, and which was more reliable for this file?
2. Why does "I can see the LaTeX source" tell you nothing about what BrailleBlaster produced?
3. When is it better to rebuild three equations in the Hub than to troubleshoot the conversion?
4. If you were the professor's assistant, what could you ask the professor to do to make the next file easier to convert?
