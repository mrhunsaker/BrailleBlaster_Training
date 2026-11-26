# Lesson 36: LibreOffice, OpenOffice, and Google Docs

> **Lesson at a glance**
>
> - **Unit:** Unit 5: Handbook (Supplemental)
> - **Suggested time:** about 2 hours
> - **Prerequisites:** [Lesson 33](33-what-makes-a-good-source.md), [Lesson 35](35-word-structure-with-styles.md)
> - **You will need:** A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Apply real styles in LibreOffice Writer, Apache OpenOffice Writer, and Google Docs using the keyboard.
- Explain which BrailleBlaster features work for `.odt` files and which need `.docx`.
- Inspect a file from any of these programs for fake structure.
- Export each program's file in the form BrailleBlaster reads best.

> [!TIP]
> **Practice file:** `sample.odt` in the [sample files](../samples/index.md), and any document you have in these programs.

## Why this matters

Many schools and agencies use free office software, and many teachers write in Google Docs. All of these can produce well-structured files, and all of them can produce flat ones. The commands differ from Word, but the principle from [Lesson 35](35-word-structure-with-styles.md) is the same: **apply a style, and never fake one**.

They also differ in one way that matters for braille: the OpenDocument format (`.odt`) that LibreOffice and OpenOffice save loses some of what a `.docx` can carry into BrailleBlaster.

{HB}

---

## How to use this lesson

Read the section for the program you use, and the section on **ODT versus DOCX** whatever you use. Keep the shortcut tables nearby.

---

## The Concept

### ODT versus DOCX in BrailleBlaster

BrailleBlaster reads the two formats differently. It reads `.docx` with Pandoc's *styles* option, so style **names** reach its script. It reads `.odt` **without** it, and Pandoc does not support that option for ODT at all. Tested results:

| Feature | `.docx` | `.odt` |
| ------- | ------- | ------ |
| Heading 1, 2, 3 | Centered, Cell 5, Cell 7 | The same |
| Lists | Kept | Kept |
| Bold, italic, underline | Kept | Kept |
| Margin styles named `3-1`, `1-3`, and so on | **Recognized** | **Ignored** |
| `BB Empty Paragraph`, the List style family | **Recognized** | **Ignored** |
| Word page breaks (`Ctrl+Enter`) | **Kept**, by a dedicated filter | Not handled by that filter |
| Empty paragraphs | Kept | Not kept by that filter |

So: **if you only need headings, lists, and emphasis, ODT is fine. If you need margin styles, empty paragraphs, or page breaks, save as DOCX.** Every program in this lesson can.

### Three programs, one idea

- **LibreOffice Writer** is the most actively developed. Its styles are in a *Styles sidebar* (`F11`).
- **Apache OpenOffice Writer** is the older sibling. Most commands are the same, with an older interface. Check each shortcut in your version.
- **Google Docs** works in a browser, with its own style menu and a different set of keys.

---

## LibreOffice Writer

### Shortcuts

| Action | Shortcut |
| ------ | -------- |
| Heading 1, 2, 3 | `Ctrl+1`, `Ctrl+2`, `Ctrl+3` |
| Body Text | `Ctrl+0` |
| Open the Styles sidebar | `F11` |
| Focus the paragraph style box (type a style name) | `Ctrl+F11` |
| Create a style from the selection | `Shift+F11` |
| Update the style from the selection | `Ctrl+Shift+F11` |
| Numbered list on or off | `F12` |
| Bullet list on or off | `Shift+F12` |
| Clear direct formatting | `Ctrl+M` |
| Show formatting marks | `Ctrl+F10` |
| Navigator (the heading outline) | `F5` |
| Find and Replace | `Ctrl+H` |
| Page break | `Ctrl+Enter` |
| Line break inside a paragraph | `Shift+Enter` |
| Non-breaking space | `Ctrl+Shift+Space` |
| Footnote | `Ctrl+Alt+F` |
| Endnote | `Ctrl+Alt+D` |
| Bold, italic, underline | `Ctrl+B`, `Ctrl+I`, `Ctrl+U` |

### Inspecting a file

1. Open the **Navigator** (`F5`) and expand **Headings**. Real headings are listed.
2. Open the **Styles sidebar** (`F11`) and click through paragraphs to see their paragraph style.
3. Turn on **formatting marks** (`Ctrl+F10`) to find typed bullets, spaces, and tabs.
4. In **Find and Replace**, tick **Other options > Paragraph Styles** to search by style name.
5. Use **Tools > Accessibility Check** to catch missing alt text and untagged structure.

### Saving

- **File > Save As**, and choose **Word 2007-365 (.docx)** for the most features in BrailleBlaster.
- Choose **ODF Text Document (.odt)** only if headings, lists, and emphasis are all you need.
- **File > Export As > Export directly as EPUB** makes an EPUB.

### Math

Use **Insert > Object > Formula** to open the formula editor, which writes a math object. Always check how an equation arrives in BrailleBlaster, because converting it is less certain than converting a Word equation or LaTeX.

---

## Apache OpenOffice Writer

OpenOffice uses most of the same keys, with these cautions.

| Action | Shortcut |
| ------ | -------- |
| Heading 1, 2, 3 | `Ctrl+1`, `Ctrl+2`, `Ctrl+3` |
| Text Body | `Ctrl+0` |
| Styles and Formatting window | `F11` |
| Numbered list on or off | `F12` |
| Bullet list on or off | `Shift+F12` |
| Non-breaking space | `Ctrl+Shift+Space` |
| Page break | `Ctrl+Enter` |
| Find and Replace | `Ctrl+H` |

- The names of the default styles differ in older versions (for example *Default* and *Text body*). Check what your version calls them.
- Save as **Word (.docx)** with the same reasoning as LibreOffice.
- If you maintain files in both programs, remember that the formats are compatible, but style names and formatting details can change in the round trip. Compare the heading outline after any conversion.

---

## Google Docs

### Shortcuts (Windows and ChromeOS)

| Action | Shortcut |
| ------ | -------- |
| Heading 1 to 6 | `Ctrl+Alt+1` to `Ctrl+Alt+6` |
| Normal text | `Ctrl+Alt+0` |
| Numbered list | `Ctrl+Shift+7` |
| Bullet list | `Ctrl+Shift+8` |
| Page break | `Ctrl+Enter` |
| Footnote | `Ctrl+Alt+F` |
| Paste without formatting | `Ctrl+Shift+V` |

Mac users replace `Ctrl` with `Cmd` and `Alt` with `Option`.

### Inspecting a file

1. Turn on **View > Show document outline**. Real headings are listed on the left.
2. Click in a paragraph and read the style in the toolbar's style box. "Normal text" on a large bold line is a fake heading.
3. Check images for **alt text**: right-click an image and choose **Alt text**.

### Exporting

- **File > Download > Microsoft Word (.docx)** is the best choice for BrailleBlaster.
- **File > Download > OpenDocument Format (.odt)** and **EPUB Publication (.epub)** are also available. The EPUB is useful for long documents with a clear chapter structure.
- Do **not** send a PDF made from a Google Doc if the original is available. See [Lesson 42](42-pdfs-scans-and-ocr.md).

> [!NOTE]
> Google Docs has no setting for the BrailleBlaster margin style names, so it cannot carry them. If you need them, open the downloaded `.docx` in Word or LibreOffice and set the style names there.

---

## Step by step

### Make any file ready for BrailleBlaster

1. Apply real heading and list styles, and remove typed bullets and layout spaces.
2. Put pictures in line with text, and add alt text.
3. Save as `.docx` (or `.odt` if you need only the basics).
4. Open the result in BrailleBlaster and compare the heading structure with the original outline.

---

## Practice

### Tasks

1. Open `sample.odt` in LibreOffice Writer. Open the Navigator and list the headings. Open the Styles sidebar and name the paragraph style of the list.
2. Add a paragraph style named `3-1` to the file and apply it to a paragraph. Save as `.odt`, then open it in BrailleBlaster. Does the style apply?
3. Save the same file as `.docx` and open it in BrailleBlaster. Does it apply now?
4. In Google Docs, write a heading, a bullet list, and a numbered list using only the keyboard, and download the `.docx`.
5. A teacher saves in `.odt` and asks why the blank lines between her poem's stanzas disappeared. What do you tell her?

### Answer Key

1. The Navigator should list *Chapter 1* and *Section 1.1*. The list items use a list paragraph style.
2. From the test: **it does not apply**. BrailleBlaster reads `.odt` without style names, so the paragraph arrives as ordinary body text.
3. From the test: it **should apply**, because `.docx` is read with style names. Confirm in your copy, and report a difference.
4. The keys are `Ctrl+Alt+1`, `Ctrl+Shift+8`, and `Ctrl+Shift+7`. Check the outline, then download from **File > Download**.
5. Empty paragraphs are not kept by the filter that handles them for `.docx`, and that filter does not run for `.odt`. Ask her to save as `.docx`, or to mark the stanza breaks another way.

---

## Key takeaways

- The principle is the same in every program: **apply a style, never fake one**.
- **`.docx` carries more into BrailleBlaster than `.odt`**: margin styles, empty paragraphs, the List family, and page breaks. Save as DOCX when you need them.
- LibreOffice: `Ctrl+1/2/3`, `F11`, `F5`, `Ctrl+F10`. Google Docs: `Ctrl+Alt+1` to `6`, the document outline.
- Inspect with the outline view and the style box, not by eye.

---

## Source Citations

- The BrailleBlaster program source (the conversion script `bbx.lua` and the Pandoc loader), read at commit `369176b`, with the conversion tests run using Pandoc 3.12.1, the version BrailleBlaster bundles, including the Pandoc loader, which reads `docx` with the *styles* option and `odt` without it.
- The Document Foundation, *LibreOffice Writer Guide*, at [documentation.libreoffice.org](https://documentation.libreoffice.org/).
- Apache OpenOffice, *Writer Guide*, at [openoffice.org](https://www.openoffice.org/).
- Google, *Keyboard shortcuts for Google Docs*, at [support.google.com/docs](https://support.google.com/docs/).
