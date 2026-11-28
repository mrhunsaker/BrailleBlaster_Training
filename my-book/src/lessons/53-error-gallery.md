# Lesson 53: Error Gallery

> \*\*Lesson at a glance\*\*
>
> - \*\*Unit:\*\* Unit 5: Handbook (Supplemental)
> - \*\*Suggested time:\*\* about 2 hours
> - \*\*Prerequisites:\*\* [Lesson 33](33-what-makes-a-good-source.md), [Lesson 35](35-word-structure-with-styles.md), [Lesson 32](32-proofreading-and-quality-assurance.md)
> - \*\*You will need:\*\* A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Recognize the most common errors in braille production by their symptoms.
- Say what caused each error, what to check, and how to fix it.
- Use a before-and-after view of an error to find the same mistake in your own work.
- Sort an error by category, so that you know which proofreading pass catches it.

> [!WARNING]
> A symptom can have more than one cause. Diagnose the source, structure, translation settings, and output before changing anything; applying a familiar fix without confirming the cause can introduce a second error.

## Why this matters

Experienced transcribers do not make fewer mistakes because they are careful. They make fewer because they have **seen each mistake before**. They know what a dropped image looks like when the Braille View looks tidy, and what a Replace All does to a surname. This lesson is a gallery of those mistakes, sorted by category, with the cause and the fix for each.

> [!NOTE]
> \*\*About the tests in this lesson.\*\* Where this lesson says what BrailleBlaster does with a file, the statement comes from reading BrailleBlaster's conversion script and from running that script on the sample files with Pandoc 3.12.1, the version the program bundles. It has \*\*not\*\* been confirmed by opening the files in the application. Treat each as an expectation, check it in your own copy, and report differences.

---

## How to use this lesson

Read the gallery once, to learn the shapes of the errors. Then use it as a **diagnostic**: when something looks wrong, find the symptom here. The practice asks you to name ten errors from short descriptions.

Each case gives **what you see**, **why it happens**, **the fix**, and **where to read more**. Every case about an import was reproduced with BrailleBlaster's own conversion script.

---

## A. Import errors

These lose or alter content **silently**. The Braille View looks fine.

| # | What you see | Why it happens | The fix | Lesson |
| - | ------------ | -------------- | ------- | ------ |
| A1 | A **picture and its caption are gone** after import | A picture alone in its paragraph is a Pandoc *figure*, which the conversion script does not handle. The same is true of a LaTeX `figure` and an HTML `<figure>` | Put the picture **inside a sentence**, or in the same paragraph as its caption text. Count figures before and after | [33](33-what-makes-a-good-source.md) |
| A2 | A **Markdown file will not import**, with an error | A **line block** (lines that start with `|`) makes the conversion script fail | Write poems with a **backslash at the end of each line** | [34](34-markdown-syntax-guide.md) |
| A3 | The **title, author, and date are missing** from a LaTeX or Markdown import | `\title`, `\author`, `\maketitle`, and a YAML header produce no output | Build the **title page** yourself | [24](24-t-page-generator.md), [40](40-latex-for-transcribers.md) |
| A4 | A **document title is body text**, not a heading | The Word **Title** style is not a heading to BrailleBlaster | Use **Heading 1**, or apply the heading in BrailleBlaster | [35](35-word-structure-with-styles.md) |
| A5 | A **text file is hundreds of one-line paragraphs** | The text loader makes one paragraph per non-blank line, so hard-wrapped text is split | **Unwrap** the text first | [41](41-text-encoding-and-braille-characters.md) |
| A6 | A **struck-out word** is not struck out | Strikethrough is dropped, and the text stays | Mark it another way, with a **note** | [34](34-markdown-syntax-guide.md) |
| A7 | `H~2~O` appears as the **literal** `H_2O` | Subscript and superscript become literal characters outside math | Use a **math expression** | [34](34-markdown-syntax-guide.md) |
| A8 | A **sentence is broken** around a code word | Inline code becomes its own displayed block | Remove the code style, or fix after import | [34](34-markdown-syntax-guide.md) |
| A9 | A **style named `3-1` has no effect** | `.odt` files are read without style names. Only `.docx` carries them | Save as **`.docx`** | [36](36-libreoffice-openoffice-and-google-docs.md) |
| A10 | **Four levels of headings** all look the same below level two | Levels 3 to 6 all become **Cell 7 Headings** | Decide the mapping, then apply it ([Lesson 5](05-heading-levels.md)) | [33](33-what-makes-a-good-source.md) |
| A11 | A **TikZ drawing has vanished** | TikZ pictures are silently dropped | Ask for a **description**, and write a note | [40](40-latex-for-transcribers.md) |
| A12 | A **book's chapters come in the wrong order** (EPUB) | The reading order is the package file's **spine** | Read the spine, and fix the source | [39](39-inside-the-packages.md) |

### A closer look: the poem

**Before** (it fails to import):

```markdown
| The water slips away at noon
| and leaves the shore a quiet floor,
```

**After** (it imports, one line per line):

```markdown
The water slips away at noon\
and leaves the shore a quiet floor,
```

### A closer look: the picture

**Before** (picture and caption are lost):

```markdown
![A bar chart of rainfall](chart.png)
```

**After** (both are kept):

```markdown
![A bar chart of rainfall](chart.png) Figure 2.1 Rainfall by month.
```

---

## B. Structure errors

| # | What you see | Why it happens | The fix | Lesson |
| - | ------------ | -------------- | ------- | ------ |
| B1 | **Indents and spacing** made with spaces | Typed spaces instead of a style | Apply the style, and delete the spaces | [4](04-layout-styles.md) |
| B2 | A **"list"** that is really **one sentence** across lines | A previous editor added bullets | Join it into a paragraph | [6](06-list-formatting.md) |
| B3 | A list **item at the wrong level** | The wrong list level was applied | Apply the right level, and check the margins | [6](06-list-formatting.md) |
| B4 | A **Box style on decoration** | "Set off in print" was taken to mean "a box" | Use a box only for a real, meaningful box | [18](18-advanced-formatting.md) |
| B5 | A **Simple table wider than the page** | The Total Width was not checked | Use Listed, Stairstep, or Linear, with a note | [25](25-tables.md) |
| B6 | A **heading in the wrong style** | The print level was mapped inconsistently | Fix the **heading map** and apply it throughout | [5](05-heading-levels.md) |
| B7 | A **poem as prose** | Line breaks were treated as wrapping | Apply a poetry style | [18](18-advanced-formatting.md) |
| B8 | A heading **stranded** at the bottom of a page | No option ties it to the next element | **Keep With Next** | [26](26-controlling-the-page.md) |

---

## C. Emphasis errors

| # | What you see | Why it happens | The fix | Lesson |
| - | ------------ | -------------- | ------- | ------ |
| C1 | **Bold on every heading** | Print bold was copied into braille | Remove it, because the heading style already says it | [3](03-typeface-emphasis.md) |
| C2 | **Bold on glossary entry words** | The print bold was kept | **Remove Emphasis from Alphabetic Reference Entry Words**, then restore what is needed | [31](31-glossaries-and-indexes.md) |
| C3 | A **defined term lost its bold** | Emphasis that carries meaning was removed | Restore it | [3](03-typeface-emphasis.md) |
| C4 | **Highlighting dropped** though the teacher refers to it | It was treated as decoration | A **transcriber-defined typeform**, listed on the Special Symbols page | [24](24-t-page-generator.md) |
| C5 | **Emphasis leaks** into the next word | The selection was one character too long | Select exactly the emphasized text | [3](03-typeface-emphasis.md) |

---

## D. Math errors

| # | What you see | Why it happens | The fix | Lesson |
| - | ------------ | -------------- | ------- | ------ |
| D1 | An **equation reads as prose** | It was not flagged | Select it and press `Ctrl+M` | [7](07-math-translation-toggle.md) |
| D2 | A **compound-word hyphen is a minus sign** | Too much text was flagged | Remove the toggle from prose | [7](07-math-translation-toggle.md) |
| D3 | **Two math codes** in one document | Nemeth and UEB Technical indicators were mixed | One family of tools, set by the student's code | [29](29-ueb-technical-and-numeric-material.md) |
| D4 | A **matrix is misaligned** | Spaces were used | The Spatial Math Editor | [9](09-spatial-math-editor.md) |
| D5 | An **equation is a picture** | The source stored math as an image | **Retype** it, and ask for MathML or LaTeX | [38](38-dtbook-nimas-and-mathml.md) |
| D6 | **LaTeX braces misread**: `x^n+1` for `x^{n+1}` | The exponent's grouping was misread | Read the braces | [40](40-latex-for-transcribers.md) |

---

## E. Notes, images, and translation

| # | What you see | Why it happens | The fix | Lesson |
| - | ------------ | -------------- | ------- | ------ |
| E1 | The **print caption and your description look the same** | Both used the Caption style | Caption for the print, **Description** for yours | [27](27-images-and-tactile-graphics.md) |
| E2 | **Transcriber's note indicators typed by hand** inside a Description | The style already adds them | Delete the typed indicators | [27](27-images-and-tactile-graphics.md) |
| E3 | The **Description style covers only part** of the text | The whole item was not selected first | Select the entire item, then apply | [27](27-images-and-tactile-graphics.md) |
| E4 | A **student's name saved globally** in a translation correction | **Save Translation Globally** sends it to APH | Save **locally**, and delete the entry | [28](28-editing-the-translation.md) |
| E5 | **Code has contractions** | The Relaxer was used, which works on the document | Use **Change Translation** on the passage | [11](11-contraction-relaxer.md) |
| E6 | **A symbol shows as a name** in notes | No braille was defined for the character | **Define New Character** | [28](28-editing-the-translation.md) |

---

## F. Pages, volumes, and front matter

| # | What you see | Why it happens | The fix | Lesson |
| - | ------------ | -------------- | ------- | ------ |
| F1 | **Edits to a T-page are lost** | They were made in the Print View, and the generator was reopened | Edit **inside the generator** | [24](24-t-page-generator.md) |
| F2 | **The TOC disagrees with the volumes** | The TOC was built before the volume breaks | Break the volumes first, then rebuild the TOC | [23](23-toc-and-volumes.md) |
| F3 | **Running head collides** with the page number | It was too long for the longest number | Shorten it | [21](21-running-heads-and-page-numbers.md) |
| F4 | **Print and braille page numbers confused** | The two were not kept apart | Check with the Braille Preview's three modes | [21](21-running-heads-and-page-numbers.md) |
| F5 | **A page number with letters** is not found in the TOC | The tool does not find numbers like C13 | Use the **Page Number** tool by hand | [23](23-toc-and-volumes.md) |
| F6 | **Too many volumes** | The size was not estimated | **Measure the ratio** from a sample | [45](45-page-geometry-and-volume-sizing.md) |

---

## G. Output and workflow

| # | What you see | Why it happens | The fix | Lesson |
| - | ------------ | -------------- | ------- | ------ |
| G1 | **Lines wrap wrongly** on paper | The embosser's settings do not match Page Properties | Match them, then run a **test emboss** | [13](13-paper-size-and-embossers.md), [50](50-embosser-operation-and-maintenance.md) |
| G2 | **Fix lost** on the next export | A BRF was edited by hand | Fix the **BBX** and export again | [32](32-proofreading-and-quality-assurance.md) |
| G3 | **Replace All damaged the text**: *Johnson* became *Jonson* | **Whole Word** was not checked | Test with **Find** first, and use Whole Word and Match Case | [12](12-find-and-replace.md), [Lab 8](../labs/lab-8-find-and-replace-cleanup.md) |
| G4 | **The wrong file is current** | `FINAL`, `FINAL2`, and `(copy)` | Version numbers and folders | [49](49-file-management-and-student-privacy.md) |
| G5 | **A student's name** in a file name or an emailed log | Convenience | Use an **ID**, and read logs before sending | [49](49-file-management-and-student-privacy.md) |
| G6 | **The job is bigger than promised** | No estimate was made | Estimate before starting | [48](48-job-intake-and-the-agency-style-sheet.md) |

---

## Step by step

### Use the gallery as a diagnostic

1. **Describe the symptom** in one sentence.
2. **Find the category.** Is it import, structure, emphasis, math, notes, pages, or output?
3. **Read the cause**, and decide whether it fits your case.
4. **Apply the fix** in the **source**.
5. **Log it** in your error log, so that you see your own pattern ([Lesson 32](32-proofreading-and-quality-assurance.md)).

---

## Practice

### Tasks

Name the case (for example, A1) and the fix for each.

1. After importing a Markdown chapter, a figure and its caption are missing.
2. A poem written with `|` at the start of each line will not import.
3. A glossary's entry words are all bold in the braille.
4. An embossed page has lines that wrap two cells early, though the Braille Preview is right.
5. A name you replaced throughout a document has also changed inside a longer name.
6. The title page content from a LaTeX file is missing.
7. A table is too wide for the page.
8. After you reopened the T-Page Generator, your edits to the title page had gone.
9. A style you named `3-1` in LibreOffice has no effect in BrailleBlaster.
10. A transcriber saved a student's surname as a global translation correction.

### Answer Key

1. **A1.** Put the image inside a sentence, or add the caption text to the same paragraph.
2. **A2.** Rewrite the poem with a backslash at the end of each line.
3. **C2.** Use **Remove Emphasis from Alphabetic Reference Entry Words**, then restore what is needed.
4. **G1.** Match the embosser's settings to Page Properties, and run a test emboss.
5. **G3.** The replacement did not use Whole Word. Recover from your saved copy, then use Whole Word and Match Case.
6. **A3.** The title block does not import. Build the title page yourself.
7. **B5.** Use Listed, Stairstep, or Linear, with a Transcriber's Note.
8. **F1.** Edits made outside the generator are lost. Make them inside it.
9. **A9.** `.odt` is read without style names. Save as `.docx`.
10. **E4.** Delete the entry in **View Corrections**, and save such corrections locally.

---

## Key takeaways

- Most errors have a **shape you can learn**. Import errors lose content silently, structure errors come from shortcuts, and output errors come from mismatched settings.
- The most damaging import errors are **dropped images, failed line blocks, and missing titles**.
- **Fix at the source**, never in the output.
- Keep an **error log**. It is a personal gallery.

---

## Source Citations

- The import cases (A1 to A12) were reproduced with BrailleBlaster's own conversion script, run with Pandoc 3.12.1. See [Lessons 33 to 40](33-what-makes-a-good-source.md).
- The remaining cases summarize the lessons they link to, whose sources are listed there.
