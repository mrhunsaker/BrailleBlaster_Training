# Lesson 52: Decision Trees

> \*\*Lesson at a glance\*\*
>
> - \*\*Unit:\*\* Unit 5: Handbook (Supplemental)
> - \*\*Suggested time:\*\* about 90 minutes
> - \*\*Prerequisites:\*\* [Lesson 33](33-what-makes-a-good-source.md), [Lesson 47](47-subject-area-decision-guide.md)
> - \*\*You will need:\*\* A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Use a text decision tree to settle a recurring question quickly and consistently.
- Choose a translation control, a table type, an import path, an image treatment, and a deliverable format.
- Decide whether to flag text as math, keep or ignore emphasis, use a list or box, and write a Transcriber's Note.
- Recognize when a tree does not answer the question and a human decision, written down, is needed.

> [!NOTE]
> A decision tree is a consistency aid, not an authority or substitute for professional judgment. If the facts do not fit a branch, stop, consult the relevant standard or student's team, and document the exception instead of forcing the case into the nearest answer.

## Why this matters

A transcriber makes the same dozen decisions on every job: Is this math? Does this table fit? Should this image be described? Written as prose, the answers are scattered through the lessons. As a **tree**, each is a short sequence of questions that ends in an action, and the same inputs always give the same result. That is what consistency means, and it is what an agency style sheet ([Lesson 48](48-job-intake-and-the-agency-style-sheet.md)) tries to protect.

{HB}

---

## How to use this lesson

Each tree is a numbered list of **questions**. Answer the first one, and follow the instruction to the next. Each tree ends with an **action** and the lesson that explains it. The trees are written as text so that a screen reader or a braille display reads them in order.

> [!IMPORTANT]
> A tree \*\*summarizes decisions the earlier lessons teach.\*\* It does not replace them, the standards, or your agency's style sheet. When a tree does not fit your case, \*\*stop, decide on judgment, and write the decision down\*\* ([Lesson 43](43-braille-formats-crosswalk.md)).

---

## Tree 1: Which translation control?

1. Is the question about **what this learner has been taught** (their contraction sequence), for the **whole document**? **Yes:** use the **Contraction Relaxer** and choose the last unit taught ([Lesson 11](11-contraction-relaxer.md)). **No:** go to 2.
2. Is it about **which braille code or grade** the whole document uses? **Yes:** **Settings > Translation Settings** ([Lesson 29](29-ueb-technical-and-numeric-material.md)). **No:** go to 3.
3. Is the text **mathematics**? **Yes:** the **math toggle**, `Ctrl+M` ([Lesson 7](07-math-translation-toggle.md)). **No:** go to 4.
4. Must the passage be **exact** (code, a file name, a code string), with no contractions? **Yes:** go to 5. **No:** go to 6.
5. Do you need the **literal ASCII translation** that BrailleBlaster would not otherwise allow? **Yes:** **Change Translation: Direct** (`Ctrl+D`). **No:** **Change Translation: Uncontracted** (`Ctrl+Shift+T`) ([Lesson 28](28-editing-the-translation.md)).
6. Is a **word or character** translating **wrongly or not at all**? **Yes:** **Correct Braille Translation** (`Ctrl+T`), saved **locally** unless you are sure ([Lesson 28](28-editing-the-translation.md)). **No:** go to 7.
7. Do you need to **type braille directly**? **Yes:** **Six Key Mode** (`Alt+X`). **No:** leave the translation alone.

## Tree 2: Which table type?

1. Is the table **really tabular data** (rows and columns that a reader compares)? **No:** it is probably a list or a layout. Use a list style ([Lesson 6](06-list-formatting.md)). **Yes:** go to 2.
2. Build it in the **Table Editor** and set **Simple**. Open **Simple Table Options** and read **Total Width**. Is it **no wider than the cells per line**? **Yes:** use **Simple** ([Lesson 25](25-tables.md)). **No:** go to 3.
3. Can you make it fit by **one cell between columns** or **custom widths**? **Yes:** do that and check again. **No:** go to 4.
4. Is each **row a labeled thing with several attributes**? **Yes:** **Listed**, with its Transcriber's Note. **No:** go to 5.
5. Do the **columns form levels** that step across the page? **Yes:** **Stairstep**. **No:** go to 6.
6. Use **Linear**, with the column headings in the Transcriber's Note.
7. Always: **check the Braille View**, and **write the note** for any change of format.

## Tree 3: Which import path?

1. What is the **source**? A **NIMAS file or zip**: open it with the NIMAS importer ([Lessons 20](20-nimas-production-files.md), [38](38-dtbook-nimas-and-mathml.md)). **A Word file:** go to 2. **Markdown, LaTeX, or HTML:** go to 4. **A PDF or a scan:** go to 6. **Plain text:** go to 7.
2. Does `w:pStyle` appear in the file? (`unzip -p file.docx word/document.xml | grep -o 'w:pStyle'`, [Lesson 39](39-inside-the-packages.md)) **No:** the structure is fake. Ask for a better file, or rebuild ([Lab 1](../labs/lab-1-rescue-word-document.md)). **Yes:** go to 3.
3. Check for **floating pictures, text boxes, and Title-style headings**, then import ([Lesson 35](35-word-structure-with-styles.md)).
4. Does the file contain a **Markdown line block**, a **stand-alone image**, or a **LaTeX figure or TikZ picture**? **Yes:** fix them first ([Lesson 33](33-what-makes-a-good-source.md)). **No:** go to 5.
5. Open it ([Lessons 34](34-markdown-syntax-guide.md), [40](40-latex-for-transcribers.md)), and **check the title, the headings, and every equation**.
6. Run `pdfinfo` and `pdffonts` ([Lesson 42](42-pdfs-scans-and-ocr.md)). **Text layer:** extract with `pdftotext`. **No text layer:** OCR it. **Always:** proofread against the page, and retype math. **Better:** ask for the original.
7. **One paragraph per line?** **Yes:** open it. **No:** unwrap it first, and clean the characters ([Lesson 41](41-text-encoding-and-braille-characters.md)).

## Tree 4: Describe, make a graphic, do both, or omit?

1. Is the image **decoration** (a border, a logo)? **Yes:** **omit**, with a note if your agency requires one. **No:** go to 2.
2. Can its **key information be said in words**? **Yes:** go to 3. **No:** go to 4.
3. Is it merely an **illustration** of what the text says? **Yes:** a **short description**. **No:** a **full description** with values and labels ([Lesson 46](46-image-description-and-tactile-graphics-resources.md)).
4. Does the reader need to know **where things are or how they connect**? **Yes:** a **tactile graphic, with a description** for the labels. **No:** a **full description**.
5. Will the student **produce or analyze** a similar figure? **Yes:** a **tactile graphic** is likely required. Plan the page with **Page Side** ([Lessons 26](26-controlling-the-page.md), [27](27-images-and-tactile-graphics.md)).

## Tree 5: Do I flag this as math?

1. Is it a **number, letter, or sign** that stands for a **quantity or operation**? **No:** it is **text**. Leave it. **Yes:** go to 2.
2. Is the hyphen or letter part of a **compound word** or a **name** (*well-known*, *x-ray*)? **Yes:** **text**. **No:** go to 3.
3. Is it an **expression with more than one part** (`a + b`, `x^2`)? **Yes:** **flag it** with `Ctrl+M`, then choose **Inline** if it sits in a sentence, or **Block** if it stands alone ([Lesson 7](07-math-translation-toggle.md)). **No:** go to 4.
4. Is it a **single variable** referring to math (*where r is the radius*)? **Follow your agency style sheet**, and be consistent.
5. Is the structure **complex** (nested fractions, roots, matrices)? **Yes:** build it in the **ASCII Math Hub** or **Spatial Math Editor** ([Lessons 8](08-ascii-math-hub.md), [9](09-spatial-math-editor.md)).

## Tree 6: Keep or ignore this emphasis?

1. Does the emphasis **carry meaning** (a defined term, a title, a foreign word, a stressed word)? **Yes:** **keep it**, and let BrailleBlaster choose the symbol, word, or passage level ([Lesson 3](03-typeface-emphasis.md)). **No:** go to 2.
2. Is it **decoration** (bold for looks, a heading's own bold)? **Yes:** **ignore it.** The heading style already says it. **No:** go to 3.
3. Is it in an **alphabetic reference entry word** (glossary or index)? **Yes:** **ignore it**, unless needed for distinction ([Lesson 31](31-glossaries-and-indexes.md)). **No:** go to 4.
4. Is it **highlighting or color** the teacher refers to? **Yes:** a **transcriber-defined typeform**, listed on the Special Symbols page. **No:** **decide, and record it.**

## Tree 7: List, box, or plain text?

1. Is it a **real enumeration** (items that are separate and parallel)? **No:** it may be **one sentence broken across lines**. Join it ([Drill B3](../reference/drill-bank.md)). **Yes:** a **list style** at the right level ([Lesson 6](06-list-formatting.md)).
2. Is the text **set off in print** (a box, a shaded call-out) **and does the reader need to know**? **Yes:** a **Box**. **No:** plain Body Text ([Lessons 4](04-layout-styles.md), [18](18-advanced-formatting.md)).
3. Are the **line breaks** the content (verse)? **Yes:** a **poetry style**. **No:** a block quotation or Body Text.

## Tree 8: Should this be a Transcriber's Note?

1. Is it **the author's** words? **Yes:** it is **not** a note. Transcribe it. **No:** go to 2.
2. Does the **reader need it** to understand a change from the print? **Yes:** go to 3. **No:** **no note.**
3. Is it **short and tied to one place**? **Yes:** an **inline note**. **No:** a note in **its own paragraph**, or on the **Transcriber's Notes page** ([Lessons 22](22-transcribers-notes.md), [24](24-t-page-generator.md)).
4. Is it a **description of an image**? Use the **Description style**, which adds the indicators ([Lesson 27](27-images-and-tactile-graphics.md)).

## Tree 9: Which deliverable?

1. Is the reader **using embossed paper**? **Yes:** a **BRF** (or **PEF**, if your embosser takes it) for each volume, from **File > Export > Save BRF/PEF**. **No:** go to 2.
2. Is the reader using a **refreshable display** that reads **eBraille**? **Yes:** consider **eBraille**, remembering that BrailleBlaster's exporter is experimental ([Lesson 19](19-ebraille.md)). Otherwise a **BRF**.
3. Keep the **BBX** (or BBZ) in all cases: it is the source for any change ([Lesson 32](32-proofreading-and-quality-assurance.md)).

---

## Practice

### Tasks

Use the trees to answer. Say which tree and which step.

1. A line of Python code in a paragraph must appear exactly.
2. A table's Total Width is 52 and the page is 40 cells. Each row is a country with five facts. A one-cell gap does not help.
3. A teacher sends a Word file in which no paragraph has a style.
4. A bold word *photosynthesis* is a defined term in a glossary entry.
5. A photograph in the text only illustrates a sentence the text already says.
6. The lines "- liquid" and "- and gas" continue a sentence that begins "The three states of matter are solid".
7. A student reads on a refreshable display, and has no embosser.

### Answer Key

1. **Tree 1**, steps 4 and 5: not math, must be exact, so **Uncontracted** (`Ctrl+Shift+T`), or **Direct** (`Ctrl+D`) if the literal ASCII is needed.
2. **Tree 2**, step 2 fails (52 is wider than 40) and step 3 fails, then step 4: each row is a labeled thing with attributes, so **Listed**, with its Transcriber's Note.
3. **Tree 3**, step 2: no `w:pStyle`, so the structure is fake. **Ask for a better file, or rebuild.**
4. **Tree 6**, step 3: it is an entry word in an alphabetic reference, so **ignore the bold**, unless it is needed for distinction.
5. **Tree 4**, steps 1 to 3: not decoration, key information can be said in words, and it only illustrates, so a **short description**.
6. **Tree 7**, step 1: it is **one sentence broken across lines**, not an enumeration. **Join it.**
7. **Tree 9**, step 2: consider **eBraille**, and note that BrailleBlaster's exporter is experimental. Otherwise supply a **BRF** that the display can read, and keep the BBX.

---

## Key takeaways

- A decision tree turns a recurring question into **a short sequence of questions that ends in an action.**
- The trees here cover **translation controls, tables, imports, images, math, emphasis, structure, notes, and deliverables.**
- A tree **summarizes** the lessons. It does not replace the standards or your **style sheet**.
- When a tree does not fit, **decide on judgment and write it down.**

---

## Source Citations

- Each tree summarizes the lesson or lessons it links to, whose sources are listed there.
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html).
