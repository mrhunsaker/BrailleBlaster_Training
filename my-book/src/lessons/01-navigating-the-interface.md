# Lesson 1: Navigating the BrailleBlaster Interface

> **Lesson at a glance**
>
> - **Unit:** Unit 1: Universal Lessons
> - **Suggested time:** about 60 minutes
> - **Prerequisites:** None
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Name the three BrailleBlaster views (Print, Braille, and Style) and say which one you edit text in.
- Show, hide, and rearrange views with **View > Toggle Views**.
- Switch the Braille View between simulated braille and ASCII.
- Open the Braille Preview and move through it by print page number or by ordinal page number.
- Move through a document by structure with Previous Element and Next Element, and by page with Go to Page.
- Find the menu where each major tool in this course lives.

## Why this matters

Every other lesson in this course assumes you can find your way around the BrailleBlaster window. When you apply a style, check a translation, or preview a page, you are moving between the same few views and menus again and again. Ten minutes spent learning how those views work saves hours of confusion later.

This lesson is deliberately short and hands-on. You will not transcribe anything yet. You will build the habits that every later lesson depends on: edit in one place, check in another, and always look at the braille.

---

## How to use this lesson

Read **The Concept** first. Then work through the **Orientation Exercise**, which uses a short practice passage you paste into a new document. Check your results against the **Answer Key**.

> [!NOTE]
> BrailleBlaster changes between releases. This course follows the BrailleBlaster 3.x documentation. If a menu item has moved in your version, use **Help > Search** to find it. The idea behind each step stays the same even when a label changes.

---

## The Concept

### One document, three views

BrailleBlaster shows the same document in three views at once:

- **Print View** shows the print text. This is where you type, paste, select, and edit. In the current documentation, changes to the text of the document are made only in the Print View.
- **Braille View** shows the braille translation of that text, so you can see what your choices produce.
- **Style View** shows which style is applied to each block of text, such as Body Text, a heading, or a list level.

Think of the three views as three windows onto one document. When you change something in the Print View, the other two update. That is why the course keeps telling you to "check the Braille View": the Print View shows what you meant, and the Braille View shows what the reader will get.

### Show, hide, and rearrange views

You choose which views are visible and in what order.

1. Go to **View > Toggle Views**. A check mark appears beside each view that is open.
2. Uncheck a view to hide it. Check it to show it again. (`Alt+P` toggles the Print View.)
3. A view that you hide and then show again comes back on the **right-hand side** of the window.
4. To put the views in the order you prefer, go to **View > Toggle Views > Rearrange Views** and use **Move Up** and **Move Down**. The views appear from left to right in the order of the list.

The same **Toggle Views** menu also turns on the **Breadcrumbs** bar, which you will use heavily in [Lesson 4](04-layout-styles.md). Breadcrumbs show every style that wraps the text at the cursor.

### Simulated braille or ASCII

By default the Braille View shows braille cells. If you turn off **View Braille** in the View menu, the Braille View and the Braille Preview show the braille as ASCII characters instead. Neither choice changes the document. It only changes how you look at it. Use whichever is easier to read and check with your own setup.

### The Braille Preview

The **Braille Preview** (`Alt+Home`) shows the document the way it would appear as an embossed BRF, laid out on whole braille pages. Pages appear in **2 Page View**, like an open bound book, with even-numbered pages on the left and odd-numbered pages on the right. If you are producing single-sided material, you can turn 2 Page View off under **View > 2 Page View**.

In the Braille Preview you can move through the document in two ways:

- by **print page number**, which is the number normally shown in the top right corner of a braille page, or
- by **ordinal page number**, which is the page's position out of the total number of pages, whatever the print and braille page numbers say.

> [!TIP]
> If you open a BRF file in BrailleBlaster, it opens in the Braille Preview and cannot be edited. A BRF is a finished product. To change it, you need the original source file.

### Moving through a document

You can move line by line with the arrow keys, but BrailleBlaster offers faster ways:

- **Previous Element** and **Next Element** jump from one text element to the next, where an element is a block shown in the Style View. This is much quicker than line-by-line movement in a long document.
- `Ctrl+Home` and `Ctrl+End` jump to the beginning and end of the file.
- `Ctrl+G` goes to a specific page.
- For a NIMAS textbook, the **Book Tree** lets you jump by section and heading. See [Lesson 20](20-nimas-production-files.md).

### Making the screen comfortable

You can increase or decrease the font size (`Ctrl` plus the plus key, or `Ctrl` plus the minus key). Be aware that a larger font or larger toolbar icons change how much text fits on screen in the Print and Braille Views. Adjust until you can work comfortably.

### What happens when you paste

When you copy text from another document and paste it into BrailleBlaster, all of it arrives in the **Body Text** style, with 3-1 margins: the first line starts in cell 3, and runover lines start in cell 1. Special symbols that are not on the keyboard are preserved. Every practice document in this course starts life this way, which is why you will spend so much time in the Style View.

### Files you will meet

- `Ctrl+N` creates a new document and `Ctrl+O` opens a file.
- BrailleBlaster's default save format is **BBZ**, a zipped file set that keeps images and other resources alongside the document.
- A **BRF** is the finished, embosser-ready braille file. You create one with **File > Export > Save BRF/PEF**. See [Lesson 13](13-paper-size-and-embossers.md).
- BrailleBlaster can open Word, OpenDocument, Markdown, LaTeX, HTML, EPUB, XML and NIMAS, and plain text files. [Lesson 2](02-opening-word-documents.md) and [Lessons 14](14-importing-markdown-and-opendocument.md) through [16](16-choosing-an-import-workflow.md) cover them.

### A map of the menus

This is where the tools in this course live. Use it as a table of contents for the program.

- **File**: open, new, print, emboss, export. See [Lesson 2](02-opening-word-documents.md) and [Lesson 13](13-paper-size-and-embossers.md).
- **Edit**: Find and Replace (`Ctrl+F`), Page Break (`Ctrl+Enter`), Edit Page Number. See [Lesson 12](12-find-and-replace.md) and [Lesson 21](21-running-heads-and-page-numbers.md).
- **View**: Toggle Views, Rearrange Views, View Braille, 2 Page View, toolbars. This lesson.
- **Styles**: applying styles, Repeat Last Style (`Ctrl+R`), Configure. See [Lessons 4](04-layout-styles.md), [5](05-heading-levels.md), and [6](06-list-formatting.md).
- **Emphasis**: bold, italics, underline, script, and the other typeforms. See [Lesson 3](03-typeface-emphasis.md).
- **Tools**: Contraction Relaxer, Change Translation, Unwrap Element. See [Lesson 4](04-layout-styles.md) and [Lesson 11](11-contraction-relaxer.md).
- **Math**: Toggle Math Translation, Nemeth Block and Inline, ASCII Math Hub, Spatial Math Editor. See [Lessons 7](07-math-translation-toggle.md) through [10](10-spatial-number-lines.md).
- **Insert**: Running Head and related tools. See [Lesson 21](21-running-heads-and-page-numbers.md).
- **Settings**: Page Properties, Embosser Settings, Page Numbers. See [Lesson 13](13-paper-size-and-embossers.md) and [Lesson 21](21-running-heads-and-page-numbers.md).
- **Help**: Search, Math Help, and the Style Appendix, which lists the margins and spacing for each style.

---

## Orientation Exercise

### Practice Document

Create a new document with `Ctrl+N`, then copy the block below and paste it into the Print View.

```text
My First Braille Document

This paragraph is plain body text. BrailleBlaster places it in the Body Text style when it is pasted.

This is a second paragraph. It is longer than the first, so that the Braille View has more than one line to show. A braille page holds far fewer characters per line than a typical print page, so a paragraph like this wraps onto several lines.

A third and final paragraph completes the passage.
```

### Tasks

1. Look at the **Style View**. What style does each of the four blocks have?
2. Hide the Style View with **View > Toggle Views**. Then show it again. Where on screen does it come back?
3. Open **View > Toggle Views > Rearrange Views** and move the Braille View so it is the first of the three views. Then restore your preferred order.
4. Turn **View Braille** off, look at the Braille View, then turn it back on. What changed, and what did not?
5. Open the **Braille Preview** with `Alt+Home`. On what kind of page layout is the text shown?
6. In the Braille Preview, move to a page using the print page number option, then using the ordinal page number option. Do the two ever differ in this short document?
7. Return to the Print View. Press `Ctrl+End`, then `Ctrl+Home`. Then use **Next Element** to step through the blocks one at a time.
8. Change the font size, then change it back.
9. Try to type a new word directly into the Braille View. What do you find?

### Answer Key

1. All four blocks, including the title line, are in **Body Text**. Pasting always produces Body Text. You will change the title's style in later lessons.
2. It returns on the **right-hand side** of the window.
3. Use **Move Up** or **Move Down** in the Rearrange Views window. The views appear left to right in list order.
4. The Braille View switches between braille cells and ASCII characters. The document itself, the translation, and the Print View do not change. This is purely a display choice.
5. In **2 Page View**, like an open book, with even pages on the left and odd pages on the right.
6. In a short document with no print page numbers added, there is usually nothing to distinguish them. They start to differ in real work, when print page numbers and braille page numbers advance at different rates.
7. `Ctrl+End` goes to the end and `Ctrl+Home` returns to the beginning. Next Element moves one block at a time, which matches what the Style View shows.
8. Any size you find comfortable is correct. Larger text shows less on screen at once.
9. In the current documentation, text changes belong in the **Print View**. If your version behaves differently, note it. It is exactly the sort of difference between releases that this course tells you to verify.

> [!TIP]
> Keep this document. You will reuse it as a safe sandbox for trying out menus while you work through later lessons.

---

## Key takeaways

- The Print View is where you edit. The Braille View and Style View are where you check.
- Views can be hidden, shown, and rearranged under **View > Toggle Views**. Breadcrumbs are turned on from the same menu.
- The Braille Preview shows real braille pages, in 2 Page View, and can be navigated by print page or by ordinal page.
- Previous Element and Next Element move through a document by structure, which is faster than line-by-line movement.
- Pasted text always arrives as Body Text, so the Style View is your starting point for almost every task.

---

## Source Citations

- BrailleBlaster User Guide (current online edition) and BrailleBlaster User Manual, Version 2.1 (February 2023), "Getting Started" and "Modifying the View," at [brailleblaster.org/docs](https://brailleblaster.org/docs). The View, Toggle Views, Rearrange Views, View Braille, Braille Preview, Print Page and Ordinal Page navigation, Previous Element and Next Element, and paste-to-Body-Text behaviors described here come from this documentation.
- BrailleBlaster 3.x release notes at [github.com/aphtech/brailleblaster/releases](https://github.com/aphtech/brailleblaster/releases), for the version of the program this course follows.
