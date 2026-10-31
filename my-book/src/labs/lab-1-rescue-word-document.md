# Lab 1: Rescue a Poorly Formatted Word Document

**Time:** about 90 minutes. **Needs:** [Lessons 2](../lessons/02-opening-word-documents.md), [4](../lessons/04-layout-styles.md), [5](../lessons/05-heading-levels.md), [6](../lessons/06-list-formatting.md), and [12](../lessons/12-find-and-replace.md). **Files:** `word-02-flat-structure.docx`, `word-03-geometry-three-pass.docx`, and `word-04-inconsistent-formatting.docx` from the [sample files](../samples/index.md). **Job aids:** the Style Map and the Import Log in [Job Aids](../reference/job-aids.md).

## Scenario

Most Word documents you receive will not be built with real heading and list styles. The author made them *look* right. You are the detective: the author left clues about the intended structure, and your job is to read them correctly.

The lab uses the **Three-Pass Method**, which keeps you from fixing problems randomly as you scroll.

1. **Pass 1, Reconnaissance.** Read the whole document. Do not fix anything yet. Record the visual patterns in a style map.
2. **Pass 2, Structural correction.** Apply headings and lists, in batches where you can, and check with Breadcrumbs.
3. **Pass 3, Emphasis correction.** Only now decide which emphasis to keep, and apply or remove it.

The order matters because structure decisions change what the emphasis means. A bold heading needs no braille emphasis, because the heading style already says "this is a heading."

## Before you start

- Work on a **copy** of each file.
- Turn on **View > Toggle Views > Breadcrumbs**, and keep the Style View visible.
- **Predict first.** Before opening the flat file, write down what you think BrailleBlaster will do with the bold text and the bullet characters.

## Part A: Warm-up with the flat chemistry file

1. Open `word-02-flat-structure.docx` in BrailleBlaster and look at the Style View.
2. Record which styles you see. How many different styles are there?
3. Now open `word-01-well-structured.docx` in a second tab or window and compare.

**Expected observations.** The two files contain the same words. The well-structured file should arrive with heading and list styles already applied, because Word told BrailleBlaster what each paragraph *is*. The flat file should arrive almost entirely as Body Text, because Word only told BrailleBlaster what the paragraphs *look like*. Write down anything that differs from this.

## Part B: The geometry file, in three passes

Open `word-03-geometry-three-pass.docx`.

### Pass 1: Reconnaissance

Read the document top to bottom and complete a style map like this one. Count the instances yourself.

| Visual pattern | Count | Likely structure | BrailleBlaster style you will apply |
| -------------- | ----- | ---------------- | ----------------------------------- |
|                |       |                  |                                     |

Look for these clues: text that is bold and larger than its neighbors, lines that begin with a tab and an asterisk, an italic lead-in word, and any symbols that are really mathematics.

### Pass 2: Structural correction

1. Decide the heading levels from the sizes: the largest bold line is the chapter title, the next is a section, and the smallest is a subsection. Apply heading styles with the mapping you learned in [Lesson 5](../lessons/05-heading-levels.md).
2. Remove the typed asterisks and tabs from the list lines. You can do that safely with Find and Replace (**Edit > Find and Replace**, `Ctrl+F`), as long as you test with **Find** first.
3. Apply list styles to the two groups of list lines ([Lesson 6](../lessons/06-list-formatting.md)).
4. Check every change in Breadcrumbs.

### Pass 3: Emphasis correction

1. The word "Important:" is italic in the source. Decide whether the italic carries meaning for the reader or is only a visual lead-in, and apply emphasis only if it carries meaning.
2. Look at the sentence "The area of a triangle is given by the formula: base × height ÷ 2." Decide what is mathematics and flag it using the rules from [Lesson 7](../lessons/07-math-translation-toggle.md).
3. Check the Braille View from top to bottom.

### Expected observations for Part B

| Question | A defensible answer |
| -------- | ------------------- |
| How many fake headings are there? | Three: a chapter title, a section heading, and a subsection heading, at three different sizes |
| How many list lines, and how many lists? | Six list lines in two separate lists of three |
| Is the italic "Important:" worth carrying? | Often yes, if "Important" is signaling a key statement. It is a judgment call. Explain your choice |
| What needs the math toggle? | The expression with the multiplication and division signs |

## Part C: The inconsistent file

Open `word-04-inconsistent-formatting.docx`. This file formats **similar things differently**, so a single find-and-replace will not fix it.

1. Create a style map for it. Include the real Heading 2 and the fake headings, and the two different bullet patterns.
2. Look at the three "Term" paragraphs. One is bold, one is italic, and one is underlined. Decide whether they are really three different kinds of thing or one kind of thing (a defined term) formatted three ways.
3. Decide on one consistent treatment, apply it, and explain it in one sentence for the reader's notes.
4. Apply consistent styles throughout and verify with Breadcrumbs.

**Expected observations.** You should find four heading patterns (three bold sizes, one bold italic) plus one real Heading 2. You should find two list patterns (hyphen with space indents, and bullet with tabs), one of which nests. There is no single right answer for the terms, but whatever you choose must be applied to all three.

## When a document is too far gone

Sometimes it is faster to **start over from the text**. Select all the text in the Print View, copy it into a new BrailleBlaster document, and apply every style from scratch with the style map in front of you. Decide this during Pass 1, not halfway through Pass 2.

## Record your work

Complete an **Import Log** from the Job Aids page for each file: what the file looked like, what BrailleBlaster did, and what you changed.

## Debrief questions

1. Why is "fix structure before emphasis" a better order than the reverse?
2. What does it cost to fix each instance one at a time, compared with a batch fix? When is one at a time safer?
3. If you could send one note back to the author of `word-02-flat-structure.docx`, what would it say? (Hint: three words, starting with "Use the".)
4. How would the work have changed if the source arrived as `word-01-well-structured.docx`?

## Checklist

- [ ] I worked on copies.
- [ ] I completed the style map before changing anything.
- [ ] Every heading and list uses a style, and no spaces or typed bullets remain.
- [ ] I decided about emphasis only after the structure was finished.
- [ ] I checked the Braille View from the first line to the last.
