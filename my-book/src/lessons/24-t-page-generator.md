# Lesson 24: The T-Page Generator

> **Lesson at a glance**
>
> - **Unit:** Unit 3: Transcriber-Focused Lessons
> - **Suggested time:** about 2 hours
> - **Prerequisites:** [Lesson 21](21-running-heads-and-page-numbers.md), [Lesson 22](22-transcribers-notes.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Distinguish Normal, T-page, and P-page numbering.
- Create a title page, a Special Symbols page, and a Transcriber's Notes page with the T-Page Generator.
- Verify what the generator produced instead of trusting it blindly.

> [!TIP]
> **More practice:** the [Production Checklist and Production Log](../reference/job-aids.md).

---

## How to use this lesson

The **T-Page Generator** is an automated BrailleBlaster tool for creating transcriber-generated pages. The User Guide lists functions for creating a Title Page, Secondary Title Page, Transcriber's Notes Page, and Special Symbols Page. 

This lesson covers three generated pages, in the order you will usually make them:

- **Part 1: Title Page**
- **Part 2: Special Symbols Page**
- **Part 3: Transcriber's Notes Page**

The goal is to learn the production sequence and then verify what the generator produced.

---

## The Concept

### T-pages are transcriber-generated pages

BrailleBlaster distinguishes **Normal**, **T-page**, and **P-page** numbering. T-pages are used for transcriber-generated pages. 

Current release information recommends using the T-Page Generator to create T-pages rather than manually applying T-page numbering. 

The generator automates structure; it does not remove the need for proofreading.

### Where to find the generator

> [!IMPORTANT]
> **Where these tools live depends on your BrailleBlaster version.** The older 2.x User Guide describes the T-Page Generator as an ordinary tool. In the current 3.x source code, however, it sits in a **Debug** menu that stays hidden until you press `Ctrl+Shift+` ` (the backtick key) in the Print View. The 3.x User Guide does not document it, so it may be unfinished. To find out what your version does, press `Ctrl+Shift+` ` and look for a **Debug** item in the menu bar. If there is one, use it and **proofread everything it produces**. If it is missing or does not work, use the manual method described below.

### Before you open the generator

> [!IMPORTANT]
> Generate the T-pages **last**. The official guide recommends using the T-Page Generator after you have finished the whole transcription, including any volume breaks ([Lesson 23](23-toc-and-volumes.md)), because BrailleBlaster uses the volume breaks to place the T-pages in the right volumes. Special symbols are also arranged by volume, so check your volume breaks before you start on that tab.

> [!WARNING]
> Make every edit to a T-page **inside the generator window**. If you edit a generated T-page directly in the Print View and then reopen the generator, those edits are lost.

Open the **T-Page Generator**. The window has four tabs: **Title Page 1**, **Title Page 2** (a secondary title page, when your format or agency requires one), **Special Symbols**, and **Transcriber's Notes**. The buttons at the bottom stay the same on every tab:

- **Previous Volume** and **Next Volume** move between volumes, so you can make changes for one volume at a time.
- **Copy Current Volume** copies everything you have entered for the current volume to all the volumes.
- **OK** saves your changes, and **Cancel** closes the window without saving.

On the title page tabs, the **Emphasis**, **Translation** (Uncontracted or Direct), **Margin**, and **Settings** (for centering) menus adjust the text. The default title page margin is 1-3.

---

## Part 1: The Title Page

### The Concept

A title page is not ordinary body text. Use the T-Page Generator rather than creating vertical placement with blank paragraphs.

BrailleBlaster's release history notes that title-page styles can be applied in the T-Page Generator, with a default 1-3 style and other numeric styles available. 

### Worked Demonstration

Create a title page for:

```text
INTRODUCTION TO BIOLOGY

Third Edition

Mary Smith

Prepared for classroom use
```

Use the T-Page Generator's Title Page function. Then verify:

- title wording;
- author/editor information;
- edition information;
- required production information;
- title-page styles;
- T-page numbering;
- Braille View.

### Practice Document

Create a title page for:

```text
EARTH SCIENCE

An Introduction to Geology

Fourth Edition

Jordan Lee

Braille edition prepared for instructional use
```

### Answer Key

Use the Title Page generator. Apply the appropriate title-page styles and verify the result in Braille View. Do not use blank lines to imitate the print page's vertical layout.

---

## Part 2: The Special Symbols Page

### The Concept

The Special Symbols Page identifies special symbols used in the transcription that the reader needs to understand. The official screenshots identify the T-Pages dialog as being able to search the document for special symbols. Current release information also records that the T-Page Generator can generate a Special Symbols page. 

The generator is an aid. The transcriber must review the resulting list and decide which symbols belong on the final page.

### Worked Demonstration

A textbook contains:

```text
25°C
H₂O
$5.00
© 2026
→
±
```

Use the Special Symbols Page Generator to identify the symbols, then review:

1. whether each symbol actually occurs in the book;
2. whether an entry is needed for the reader;
3. the wording of the symbol description;
4. the corresponding braille representation;
5. whether the symbol is already explained elsewhere.

### Practice Document

A science book contains:

```text
25°C
NaCl
H₂O
±5
→
© 2026
```

#### Questions

1. Which symbols should be reviewed by the generator?
2. Should every generated entry automatically be retained?
3. What must be checked after the page is generated?

### Answer Key

1. Review the symbols detected in the document and determine which ones require a reader-facing entry.
2. No. The generated page requires editorial review.
3. Check meaning, terminology, braille representation, and whether an entry is actually useful to the reader.

---

## Part 3: The Transcriber's Notes Page

### The Concept

The Transcriber's Notes Page is a T-page for book-wide transcription information. It is different from a TN inserted into the body at the point of need.

#### Body TN

```text
[TN: The following diagram is not to scale.]
```

This explains something where it occurs.

#### Transcriber's Notes Page

```text
TRANSCRIBER'S NOTES

Color references are identified by their names in braille.
```

This establishes a convention that applies throughout the book.

#### Transcriber-defined typeforms

BrailleBlaster documentation notes that print features such as highlighting, colored font, or double underlining may have no direct braille equivalent. Transcriber-Defined Typeforms can represent such emphasis, with the meaning defined on the Transcriber's Notes Page. 

The relationship is:

```text
Print feature
    ↓
Braille representation
    ↓
Definition of the convention
    ↓
Transcriber's Notes Page
```

### Worked Demonstration

Suppose yellow highlighting identifies vocabulary in print. The transcription uses a defined braille typeform for that highlighting.

Workflow:

1. Apply the chosen transcriber-defined typeform to the affected text.
2. Explain the convention on the Transcriber's Notes Page.
3. Generate the page with the T-Page Generator.
4. Verify the first occurrence and the corresponding explanation.

### Practice Document

#### Scenario 1 — color

Red print identifies vocabulary and is represented by a defined braille typeform.

#### Scenario 2 — highlighting

Print highlighting identifies answer choices and is represented by a defined braille typeform.

#### Scenario 3 — figure descriptions

Several figures have transcriber-generated descriptions.

#### Scenario 4 — recurring convention

One transcription convention applies throughout the entire book.

For each scenario, decide whether the information belongs on the Transcriber's Notes Page, in a body TN, or both.

### Answer Key

#### 1. Color

If it is a recurring defined typeform, explain it on the Transcriber's Notes Page. A local body TN may be added when a particular occurrence needs additional explanation.

#### 2. Highlighting

A recurring convention belongs on the Transcriber's Notes Page. Do not repeat the same explanation at every occurrence unless context requires it.

#### 3. Figure descriptions

The descriptions belong with the figures as transcriber-generated descriptions/TNs. A general book-wide statement about the treatment of figures may also belong on the Transcriber's Notes Page.

#### 4. Recurring convention

Use the Transcriber's Notes Page rather than repeating the same explanation throughout the text.

---

## If the generator is hidden or unavailable: building the pages by hand

The documented tools are enough to build transcriber-generated pages yourself.

1. **Type each page.** Place the cursor where the page belongs and type its text. Use the styles the lesson describes for each page: centered text for title lines, Body Text for ordinary lines, and the **Transcriber's Note** style (**Styles > Miscellaneous > Transcriber's Note**) for the notes page. For a Miscellaneous style, select the whole set of text first, because the program adds the note indicators around the selection.
2. **End the page.** Press `Ctrl+Enter` (**Edit > Page Break**) after each page so that the next one starts on a new braille page.
3. **Number the pages as T-pages.** Open **Edit > Page Number Dialog**, go to the **Edit Page Number** tab, then the **Page Number Type** tab, and choose **T-page**. Once you change the type, the braille page numbers keep that type until you choose another, so switch back to **Normal** for the body.
4. **Check the result.** Use the Braille Preview and **Navigate > Go To Page** to confirm that the T-pages are numbered t1, t2, and so on, and that the body begins on page 1.

This is slower and easier to get wrong than the generator, especially the Special Symbols page, which must list every symbol and typeform the volume uses. Keep a list as you work.

## Complete T-Page Workflow

Use this sequence:

```text
Finish enough of the transcription to identify T-page content
                    ↓
Review recurring transcription conventions
                    ↓
Identify special symbols
                    ↓
Identify transcriber-defined typeforms
                    ↓
Open T-Page Generator
                    ↓
Create Title Page
                    ↓
Generate Special Symbols Page
                    ↓
Create Transcriber's Notes Page
                    ↓
Review and edit generated material
                    ↓
Verify T-page numbering and Braille View
```

### Final Practice Checklist

#### Title Page

- [ ] Correct title
- [ ] Correct author/editor
- [ ] Correct edition
- [ ] Required production information
- [ ] Appropriate title-page styles
- [ ] Correct T-page numbering

#### Special Symbols Page

- [ ] Symbols actually occur in the document
- [ ] Descriptions are understandable
- [ ] Braille representations are correct
- [ ] Unnecessary entries removed
- [ ] Page proofread

#### Transcriber's Notes Page

- [ ] Book-wide conventions identified
- [ ] Transcriber-defined typeforms explained
- [ ] Recurring conventions explained once rather than repeatedly
- [ ] Body TNs remain at their points of need
- [ ] Page proofread

### Core Principle

**The T-Page Generator makes standard transcriber-generated pages faster to create. The transcriber remains responsible for deciding what belongs on those pages and for proofreading the generated result.**

---

## Source Citations

- *Braille Formats 2016* — transcriber-generated pages and Transcriber's Notes.
