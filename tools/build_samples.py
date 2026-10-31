#!/usr/bin/env python3
"""Generate the practice sample files for the BrailleBlaster curriculum.

Run from the repository root:   python3 tools/build_samples.py
Requires: python-docx, pypandoc_binary   (pip install python-docx pypandoc_binary)

Writes to my-book/src/samples/. Every file is generated, so edit this script and
re-run it instead of editing the output files by hand.
"""
import os, zipfile, textwrap
import docx
from docx.shared import Pt
import pypandoc

OUT = os.path.join(os.path.dirname(__file__), '..', 'my-book', 'src', 'samples')
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)
W = lambda name, text: open(os.path.join(OUT, name), 'w', encoding='utf-8').write(textwrap.dedent(text).lstrip('\n'))

# ------------------------------------------------------------------ Word files
def well_structured():
    d = docx.Document()
    d.add_heading('Chapter 1: Introduction to Chemistry', level=1)
    d.add_heading('The Atomic Theory', level=2)
    d.add_paragraph('All matter is composed of atoms, which are the basic building blocks of chemistry.')
    d.add_heading('Key Concepts', level=3)
    for t in ['Atoms are the smallest unit of an element',
              'Atoms combine to form molecules',
              'Chemical reactions involve the rearrangement of atoms']:
        d.add_paragraph(t, style='List Bullet')
    p = d.add_paragraph('The modern atomic theory was developed by John Dalton in the early 19th century. The textbook ')
    r = p.add_run('Foundations of Matter'); r.style = 'Emphasis'     # a real Word character style
    p.add_run(' covers it in depth, and the term ')
    r = p.add_run('atom'); r.style = 'Strong'                        # a real Word character style
    p.add_run(' is defined on the first page.')
    d.add_heading('The Periodic Table', level=2)
    d.add_paragraph('The periodic table organizes all known elements based on their atomic number and properties.')
    d.save(os.path.join(OUT, 'word-01-well-structured.docx'))

def flat():
    """Same content, but formatted by hand: nothing uses a built-in style except Normal."""
    d = docx.Document()
    def fake_heading(text, size):
        p = d.add_paragraph(); r = p.add_run(text); r.bold = True; r.font.size = Pt(size)
    fake_heading('Chapter 1: Introduction to Chemistry', 18)
    fake_heading('The Atomic Theory', 14)
    d.add_paragraph('All matter is composed of atoms, which are the basic building blocks of chemistry.')
    fake_heading('Key Concepts', 12)
    for t in ['Atoms are the smallest unit of an element',
              'Atoms combine to form molecules',
              'Chemical reactions involve the rearrangement of atoms']:
        d.add_paragraph('    \u2022\t' + t)
    p = d.add_paragraph('The modern atomic theory was developed by John Dalton in the early 19th century. The textbook ')
    r = p.add_run('Foundations of Matter'); r.italic = True
    p.add_run(' covers it in depth, and the term ')
    r = p.add_run('atom'); r.bold = True
    p.add_run(' is defined on the first page.')
    fake_heading('The Periodic Table', 14)
    d.add_paragraph('The periodic table organizes all known elements based on their atomic number and properties.')
    d.save(os.path.join(OUT, 'word-02-flat-structure.docx'))

def geometry():
    d = docx.Document()
    def fh(text, size):
        p = d.add_paragraph(); r = p.add_run(text); r.bold = True; r.font.size = Pt(size)
    fh('Introduction to Geometry', 18)
    d.add_paragraph('This chapter covers the fundamentals of geometric shapes and their properties.')
    fh('Shapes and Their Properties', 14)
    d.add_paragraph('All two-dimensional shapes have specific properties that define them:')
    for t in ['Triangles have three sides', 'Squares have four equal sides', 'Circles have no sides']:
        d.add_paragraph('\t* ' + t)
    d.add_paragraph('The area of a triangle is given by the formula: base \u00d7 height \u00f7 2.')
    fh('Types of Triangles', 12)
    for t in ['Equilateral triangles have three equal sides', 'Isosceles triangles have two equal sides',
              'Scalene triangles have no equal sides']:
        d.add_paragraph('\t* ' + t)
    p = d.add_paragraph(); r = p.add_run('Important: '); r.italic = True
    p.add_run('The sum of the angles in any triangle is always 180 degrees.')
    d.save(os.path.join(OUT, 'word-03-geometry-three-pass.docx'))

def inconsistent():
    d = docx.Document()
    def fh(text, size, bold=True, italic=False):
        p = d.add_paragraph(); r = p.add_run(text); r.bold = bold; r.italic = italic; r.font.size = Pt(size)
    fh('Chapter One: The Basics', 18)
    d.add_paragraph('This is the first chapter of the book.')
    fh('Main Concepts', 14)                      # bold 14
    for t, lvl in [('Concept A is important', 0), ('Concept B is also important', 0),
                   ('Concept B1 is a sub-concept', 1), ('Concept C should be noted', 0)]:
        d.add_paragraph(('    ' * lvl) + '- ' + t)  # hyphen bullets, spaces for nesting
    d.add_heading('Key Terms', level=2)           # a REAL heading style among the fake ones
    for label, kind in [('Term 1', 'b'), ('Term 2', 'i'), ('Term 3', 'u')]:
        p = d.add_paragraph(); r = p.add_run(label)
        r.bold = kind == 'b'; r.italic = kind == 'i'; r.underline = kind == 'u'
        p.add_run({'b': ' is defined as the first idea.', 'i': ' means the second idea.', 'u': ' refers to the third idea.'}[kind])
    fh('Another Section', 13, bold=True, italic=True)   # bold italic fake heading at a different size
    d.add_paragraph('This section has different formatting:')
    for t, lvl in [('Item 1', 0), ('Item 2', 0), ('Sub-item 1', 1)]:
        d.add_paragraph(('\t' * (lvl + 1)) + '\u2022 ' + t)  # different bullet character and tabs
    d.save(os.path.join(OUT, 'word-04-inconsistent-formatting.docx'))

# ------------------------------------------------------------------ Markdown / LaTeX / ODT / EPUB / HTML
MD_SAMPLE = r'''# Sample Markdown Document

## Introduction

This document demonstrates Markdown formatting.

### Key Features

- Headings at multiple levels
- **Bold text** for emphasis
- *Italic text* for light emphasis
- `Code formatting` for code snippets

### Lists

1. First ordered item
2. Second ordered item
   - Nested unordered item
   - Another nested item
3. Third ordered item

### Mathematics

Inline math: $E = mc^2$

Displayed math:

$$\frac{a + b}{c - d}$$

### Code Block

```python
def hello_world():
    print("Hello, World!")
```
'''
MD_MATH = r'''# Pandoc Math Test

## Inline Math

The area of a circle is $A = \pi r^2$.

The circumference is $C = 2\pi r$.

## Displayed Math

The quadratic formula:

$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

The Pythagorean theorem:

$$a^2 + b^2 = c^2$$

## Code with Math

In Python, you can calculate the area of a circle:

```python
import math

def circle_area(radius):
    return math.pi * radius ** 2

area = circle_area(5)
print(f"Area: {area}")
```

The formula used is $A = \pi r^2$.
'''
TEX_SAMPLE = r'''\documentclass{article}
\usepackage{amsmath}

\title{Sample LaTeX Document}
\author{Test Author}
\date{\today}

\begin{document}

\maketitle

\section{Introduction}

This document demonstrates LaTeX formatting. The quadratic formula is:

\begin{equation}
  x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation}

\section{Mathematics}

The Pythagorean theorem states that:

\begin{equation*}
  a^2 + b^2 = c^2
\end{equation*}

\begin{itemize}
  \item First item
  \item Second item
  \begin{itemize}
    \item Nested item
  \end{itemize}
\end{itemize}

\end{document}
'''
TEX_MATH = r'''\documentclass{article}
\usepackage{amsmath}
\usepackage{amssymb}

\title{Mathematical Foundations}
\author{Jane Doe}
\date{\today}

\begin{document}

\maketitle

\section{Introduction}

In this document, we explore some fundamental mathematical concepts. The most famous equation in physics is:

\begin{equation}
  E = mc^2
\end{equation}

where $E$ is energy, $m$ is mass, and $c$ is the speed of light.

\section{Algebra}

The quadratic formula is essential for solving quadratic equations:

\begin{equation*}
  x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\end{equation*}

\begin{itemize}
  \item This formula gives the roots of any quadratic equation
  \item It requires the equation to be in standard form: $ax^2 + bx + c = 0$
  \item The discriminant ($b^2 - 4ac$) determines the nature of the roots
\end{itemize}

\section{Geometry}

The Pythagorean theorem states that in a right triangle:

\begin{equation}
  a^2 + b^2 = c^2
\end{equation}

\end{document}
'''
ODT_SOURCE = '''---
title: Sample ODT Document
---

# Chapter 1

This is a paragraph with some text. It contains an **important** idea and a *note* to remember.

## Section 1.1

- Item 1
- Item 2
- Item 3
'''
EPUB_SOURCE = '''---
title: Sample EPUB Reader
author: Test Author
lang: en-US
---

# Chapter 1: Beginnings

This short EPUB has two chapters, so you can see how BrailleBlaster handles a packaged publication.

## A first section

A paragraph with a **key term** and an *italic title*.

- A list item
- Another list item

# Chapter 2: Continuations

The second chapter begins on its own page in print.

1. First step
2. Second step
'''

def pandoc_outputs():
    p = lambda name: os.path.join(OUT, name)
    pypandoc.convert_text(ODT_SOURCE, 'odt', format='markdown', outputfile=p('sample.odt'))
    pypandoc.convert_text(EPUB_SOURCE, 'epub3', format='markdown', outputfile=p('sample.epub'))
    # "convert to HTML first" fallback demonstration, produced exactly as Lesson 17 describes
    pypandoc.convert_text(TEX_MATH, 'html', format='latex', outputfile=p('math-foundations-from-tex.html'),
                          extra_args=['-s', '--metadata', 'title=Mathematical Foundations'])

# ------------------------------------------------------------------ NIMAS-style set (DTBook + OPF)
DTBOOK = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE dtbook PUBLIC "-//NISO//DTD dtbook 2005-3//EN" "http://www.daisy.org/z3986/2005/dtbook-2005-3.dtd">
<dtbook xmlns="http://www.daisy.org/z3986/2005/dtbook/" version="2005-3" xml:lang="en-US">
  <head>
    <meta name="dc:Title" content="Sample NIMAS-Style Science Reader"/>
    <meta name="dc:Creator" content="Test Publisher"/>
    <meta name="dc:Language" content="en-US"/>
    <meta name="dc:Identifier" content="sample-nimas-style-0001"/>
    <meta name="dtb:uid" content="sample-nimas-style-0001"/>
  </head>
  <book>
    <frontmatter>
      <doctitle>Sample NIMAS-Style Science Reader</doctitle>
      <docauthor>Test Publisher</docauthor>
    </frontmatter>
    <bodymatter>
      <level1 id="ch1">
        <pagenum id="p1" page="normal">1</pagenum>
        <h1>Chapter 1: Energy and Motion</h1>
        <prodnote id="pn1" render="optional">Publisher production note: this chapter is printed in two columns.</prodnote>
        <p>Energy is the ability to do work. A <strong>roller coaster</strong> at the top of a hill has stored energy.</p>
        <level2 id="ch1s1">
          <h2>Kinds of Energy</h2>
          <p>The three kinds you will study first are:</p>
          <list type="ul">
            <li>Kinetic energy</li>
            <li>Potential energy
              <list type="ul">
                <li>A stretched spring</li>
                <li>A book on a high shelf</li>
              </list>
            </li>
            <li>Thermal energy</li>
          </list>
          <pagenum id="p2" page="normal">2</pagenum>
          <sidebar id="sb1">
            <hd>Did You Know?</hd>
            <p>Energy cannot be created or destroyed. It can only change from one form to another.</p>
          </sidebar>
        </level2>
        <level2 id="ch1s2">
          <h2>Calculating Speed</h2>
          <p>Speed is distance divided by time. For example, if the distance is 120 miles and the time is 2 hours, then
            <m:math xmlns:m="http://www.w3.org/1998/Math/MathML"><m:mi>s</m:mi><m:mo>=</m:mo><m:mfrac><m:mn>120</m:mn><m:mn>2</m:mn></m:mfrac><m:mo>=</m:mo><m:mn>60</m:mn></m:math>
            miles per hour.</p>
          <imggroup id="ig1">
            <img id="img1" src="roller-coaster.png" alt="A roller coaster at the top of a hill and at the bottom."/>
            <caption>Figure 1.1 A roller coaster at the top of a hill and at the bottom.</caption>
          </imggroup>
        </level2>
      </level1>
      <level1 id="ch2">
        <pagenum id="p3" page="normal">3</pagenum>
        <h1>Chapter 2: Forces</h1>
        <p>A force is a push or a pull. Forces can change the speed or the direction of an object.</p>
      </level1>
    </bodymatter>
  </book>
</dtbook>
'''
OPF = '''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://openebook.org/namespaces/oeb-package/1.0/" unique-identifier="sample-nimas-style-0001">
  <metadata>
    <dc-metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
      <dc:Title>Sample NIMAS-Style Science Reader</dc:Title>
      <dc:Creator>Test Publisher</dc:Creator>
      <dc:Language>en-US</dc:Language>
      <dc:Identifier id="sample-nimas-style-0001">sample-nimas-style-0001</dc:Identifier>
    </dc-metadata>
  </metadata>
  <manifest>
    <item id="dtbook" href="sample-dtbook.xml" media-type="application/x-dtbook+xml"/>
  </manifest>
  <spine>
    <itemref idref="dtbook"/>
  </spine>
</package>
'''

# ------------------------------------------------------------------ Plain-text practice sources
def text_files():
    W('test-page-for-embosser.txt', '''
    Embosser Test Page

    This page checks an embosser profile and the page properties of a document.

    Body text test. This paragraph is long enough to wrap onto several braille lines so that you can check where the first line starts and where each runover line starts. Count the cells on a test emboss and compare them with the Body Text style, which uses 3-1 margins.

    A list test, entered as three plain lines:

    First item
    Second item
    Third item

    A math test: x + 5 = 12

    A long-line test: the quick brown fox jumps over the lazy dog, and then the quick brown fox jumps over the lazy dog again, so that a line keeps running past the right margin and has to wrap.
    ''')
    W('reflow-paragraph.txt', ' '.join(
        ['The quick brown fox jumps over the lazy dog. This classic pangram contains every letter of the English alphabet at least once.']*14) + '\n')
    W('running-heads-multichapter.txt', '''
    A Short Guide to Gardening

    Chapter 1: Getting Started

    This is the first chapter of the guide. It introduces the main topics that will be covered, from soil to seeds.

    The first topic is very important and will be discussed in detail. The second topic is also significant and deserves attention.

    Chapter 2: Planting

    This chapter contains the main content of the guide. It builds on the introduction from Chapter 1.

    The first subtopic, choosing a site, is explored here. The second subtopic, preparing the soil, is also covered in this chapter.

    Chapter 3: Care and Harvest

    This final chapter wraps up the guide and summarizes the key points.

    The conclusion ties everything together and offers final thoughts on the seasons of a garden.
    ''')
    W('relaxer-code-and-math.txt', '''
    Part A: A short code sample inside prose.

    In Python, you can define a function like this. The def keyword tells Python that what follows is a function.

    def add_one(number):
        return number + 1

    The return keyword sends a value back to the caller. Notice that the name add_one uses an underscore.

    Part B: Mixed content.

    In computer science, we often use algorithms with mathematical foundations. For example, the binary search algorithm has a time complexity of O(log n).

    The formula for the midpoint is mid = (low + high) / 2, rounded down.

    This algorithm is efficient because it halves the search space with each step.
    ''')
    W('play-excerpt.txt', '''
    The Lighthouse Keeper
    A one-scene play

    ACT I, SCENE 1

    (Stage direction: The top of a lighthouse at dusk. A lamp glows. Enter ANNA from the stairs.)

    ANNA
    (out of breath)
    Ninety-two steps. Every night, ninety-two steps.

    TOMAS
    (entering from the balcony)
    And every night you say the same thing.

    ANNA
    Because every night it is true.

    (Stage direction: They look out over the water. The light turns.)

    END OF SCENE 1
    ''')
    W('original-poem.txt', '''
    Low Tide

    by A. Writer

    The water slips away at noon
    and leaves the shore a quiet floor,
    a scatter of shells and a bent spoon
    that someone's picnic lost before.

    A gull walks out where the waves have been
    and studies the sand for a sign.
    The sun is a coin that is going thin;
    the day is a thread, and it is mine.
    ''')
    W('deep-list.txt', '''
    Outline of a Report

    1. Introduction
       1.1 Background
          1.1.1 Historical Context
          1.1.2 Modern Applications
       1.2 Purpose
    2. Main Content
       2.1 First Topic
          2.1.1 Subtopic A
             2.1.1.1 Detail 1
             2.1.1.2 Detail 2
          2.1.2 Subtopic B
       2.2 Second Topic
    3. Conclusion
       3.1 Summary
       3.2 Future Work
    ''')
    W('find-replace-cleanup.txt', '''
    The Mill Town Stories

    The main character of the story is named John Smith. He lives in a small town called Springfield. John is cheerful, and John works at the mill.

    Character List:
      \u2022 John Smith - protagonist
      \u2022 Mary Johnson - love interest
      \u2022 Mr. Wilson - antagonist

    Important locations:

    The story takes place in Springfield, which has a population of 5,000 people. The mill sits at the edge of the town.

    Key Events:
      \u2022 Chapter 1: John arrives in town
      \u2022 Chapter 2: John meets Mary
      \u2022 Chapter 3: Conflict with Mr. Wilson
    ''')

def zips():
    with zipfile.ZipFile(os.path.join(OUT, 'markdown-samples.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('sample.md', MD_SAMPLE); z.writestr('math-demo.md', MD_MATH)
    with zipfile.ZipFile(os.path.join(OUT, 'nimas-style-sample.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('sample-dtbook.xml', DTBOOK); z.writestr('sample-package.opf', OPF)

def main():
    well_structured(); flat(); geometry(); inconsistent()
    W('sample.tex', TEX_SAMPLE); W('math-foundations.tex', TEX_MATH)
    pandoc_outputs(); text_files(); zips()
    # a copy of the bare XML so it can be opened directly as well
    open(os.path.join(OUT, 'sample-dtbook.xml'), 'w', encoding='utf-8').write(DTBOOK)
    open(os.path.join(OUT, 'sample-package.opf'), 'w', encoding='utf-8').write(OPF)
    # one download for everything
    with zipfile.ZipFile(os.path.join(OUT, 'all-samples.zip'), 'w', zipfile.ZIP_DEFLATED) as z:
        for f in sorted(os.listdir(OUT)):
            if f != 'all-samples.zip' and not f.endswith('.md'):
                z.write(os.path.join(OUT, f), f)
        z.writestr('sample.md', MD_SAMPLE); z.writestr('math-demo.md', MD_MATH)
    print('wrote', sorted(os.listdir(OUT)))

if __name__ == '__main__':
    main()
