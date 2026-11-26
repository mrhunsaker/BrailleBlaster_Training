# Findings to Report to the BrailleBlaster Project

While building the Handbook (Lessons 33 to 54), BrailleBlaster's own Markdown, Word, LaTeX, HTML, and EPUB conversion script was run on test files. Several behaviors lose content silently or fail. They are listed here with a reproducible test set and, for the two most serious, a tested fix, so that they can be reported to APH and fixed for everyone.

## Read this first

- **What was tested.** The conversion script `bbx.lua` from the BrailleBlaster source (commit `369176b9402d331be2674c8d4c707c4240ef396b`, 2026-10-19) was run with **Pandoc 3.12.1**, the version the project's `pom.xml` bundles, using the same options as `PandocArchiverLoader.kt` (`--from=docx+styles+empty_paragraphs`, `markdown`, `latex`, and so on, plus the two Word filters).
- **What was not tested.** None of this was confirmed **inside the application**. BrailleBlaster also runs Kotlin fixers after the conversion. It is possible that something in the application handles a case before or after the script. **Please reproduce each item in the application before filing it.**
- **Test files.** `my-book/src/samples/upstream-test-cases.zip` holds one small file for each case below. `tools/build_samples.py` regenerates it.

## Summary

| # | Issue | Effect | Severity | Fix tested? |
| - | ----- | ------ | -------- | ----------- |
| 1 | Markdown **line block** makes the conversion fail | The file cannot be opened | High | **Yes** |
| 2 | A **figure** (an image alone in its paragraph, a LaTeX `figure`, an HTML `<figure>`) is dropped, with its caption | Silent loss of content | High | **Yes** |
| 3 | Title, author, and date from LaTeX and Markdown are dropped | Silent loss of metadata | Medium | No (a design question) |
| 4 | Unsupported LaTeX environments such as TikZ are dropped without a warning | Silent loss of content | Medium | No |
| 5 | A plain LaTeX `tabular` gains an empty first row | A blank header row | Low | No |
| 6 | The converter calls Pandoc with the deprecated `--mathml` option | A warning now, and a possible failure in a future Pandoc | Low | No |
| 7 | The 3.x User Guide does not document several features, and names one menu item differently from the program | Confusion | Documentation | n/a |
| 8 | The Word *Title* style is not treated as a heading | A title arrives as body text | Question | n/a |

---

## Issue 1: Markdown line blocks make the import fail

**Reproduce.** Open `case1-markdown-line-block.md`:

```markdown
# Line block

| The water slips away at noon
| and leaves the shore a quiet floor
```

**Observed.** The conversion stops with:

```text
Error running Lua:
bbx.lua:453: attempt to concatenate a table value (local 's')
```

**Expected.** The two lines arrive as lines of verse, or as a blocked text with a line break between them.

**Cause.** In the classic custom-writer API, `LineBlock(ls)` receives a **list** of strings. `bbx.lua` passes that list straight to `BlockQuote`, which concatenates it as if it were a string:

```lua
function LineBlock(ls)
  return BlockQuote(ls)      -- ls is a table
end
```

**Proposed fix (tested).** Join the lines with the script's own line-break helper:

```lua
function LineBlock(ls)
  return BlockQuote(table.concat(ls, LineBreak(1)))
end
```

With the fix, the file imports as a *Displayed Blocked Text* block with a line break between the lines. A comparison of the output for an unrelated test file, with and without the fix, was **byte-identical**.

**Note.** Markdown line blocks are the standard Pandoc way to write poetry, so this affects exactly the kind of text a transcriber is likely to meet.

---

## Issue 2: Figures are dropped, with their captions

**Reproduce.** Open each of these:

- `case2-markdown-image-alone.md`: `![A bar chart of rainfall](chart.png "Rainfall")` alone in its paragraph.
- `case3-word-image-alone.docx`: a Word picture alone in its paragraph, followed by a paragraph in the *Caption* style.
- `case4-latex-figure.tex`: a `figure` environment with `\includegraphics` and `\caption`.
- `case5-html-figure.html`: an HTML `<figure>` with `<img>` and `<figcaption>`.

**Observed.** Pandoc prints `WARNING: Undefined function 'Figure'`, and the output contains **neither the image nor its caption**. The text before and after survives. An image **inside a sentence** is kept, so the loss depends on how the author laid out the page.

**Expected.** The image (with its alt text) and the caption arrive.

**Cause.** Since Pandoc 3.0, a stand-alone image and these environments are read as a `Figure` block. `bbx.lua` defines no `Figure` handler, so Pandoc drops the block.

**Proposed fix (tested).** In the classic writer API the arguments are `(caption, contents, attr)`:

```lua
function Figure(caption, contents, attr)
  return contents .. caption
end
```

With the fix, all four cases import with the **image first and the caption after it**, as separate blocks. The caption could instead be given a Caption style.

**Why it matters.** The loss is silent: the Braille View looks tidy, and nothing says that a figure is missing. A student could miss a diagram.

**Workaround for authors.** Keep the image inside a sentence, or in the same paragraph as its caption ([Lesson 33](my-book/src/lessons/33-what-makes-a-good-source.md)).

---

## Issue 3: Document metadata is dropped

**Reproduce.** `case6-latex-title-block.tex` has `\title`, `\author`, and `\maketitle`. A Markdown file with a YAML header behaves the same way.

**Observed.** Nothing from the title block appears.

**Question.** Should the title and author be kept? One option is to import them into the document's head, as the NIMAS importer does for `doctitle` and `docauthor`, so that the T-Page Generator can use them.

---

## Issue 4: Unsupported LaTeX is dropped without a warning

A TikZ picture, and other environments Pandoc cannot read, are removed. A transcriber has no way to know that content was there. A log message, or a visible placeholder, would help.

## Issue 5: An empty header row for `tabular`

A LaTeX `tabular` with no header imports with an **empty first table row**. This may show as a blank row at the top of the table.

## Issue 6: The deprecated `--mathml` option

`bbx.lua` calls Pandoc with `--from=latex --to=html --mathml` (lines 344 and 354). Pandoc 3.12.1 reports that `--mathml` is **deprecated** and should be `--math-method=mathml`. It works now, and may stop working in a later Pandoc.

---

## Issue 7: Documentation

- The **3.x User Guide** does not describe the **TOC Builder**, **T-Page Generator**, **Volume Manager**, **Alphabetic Reference** tools, or the **eBraille export**. In the program they are in the **Debug** menu, which is hidden until `Ctrl+Shift+` ` is pressed. The older 2.x guide documented them as normal tools. It would help to say whether they are meant for general use.
- The guide says **Insert > Image Placeholder**. The program's menu item is **Insert > Image Manager**.
- The guide refers to a section on **Configuring Style Loadouts** that does not appear in the document.

## Issue 8: The Word *Title* style

Word's **Title** style arrives as **body text**, and **Heading 1** arrives as a Centered Heading. Authors often use *Title* for the top of a document. This may be intended, but it surprises people, and a note in the guide would help.

---

## How to report

Open an issue on the BrailleBlaster project's GitHub page, `github.com/aphtech/brailleblaster`. For each issue, include:

1. the **BrailleBlaster version** and operating system;
2. the **test file** from `upstream-test-cases.zip`;
3. what **happened** and what you **expected**; and
4. for Issues 1 and 2, the **proposed fix** above.

If you reproduce an issue in the application, or find that the application already handles it, please record that in `VERIFICATION.md`.
