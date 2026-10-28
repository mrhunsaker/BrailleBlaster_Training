# Lesson 12: Global Find and Replace with Formatting

> **Lesson at a glance**
>
> - **Unit:** Unit 1: Universal Lessons
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 4](04-layout-styles.md), [Lesson 5](05-heading-levels.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Use Match Case and Whole Word to make a text replacement safe.
- Find and replace by style, container, or text attribute through the Formatting window.
- Choose Replace or Replace All on purpose.
- Spot a Replace All that would damage a document before you run it.

## Why this matters

A single-page worksheet can be corrected by eye. A three-hundred-page textbook cannot. Production transcription depends on being able to find — and, when appropriate, fix — every instance of a pattern across an entire document reliably, whether that pattern is a misspelled term, a formatting inconsistency inherited from a poorly-structured source file ([Lesson 2](02-opening-word-documents.md)), or a style that needs to change document-wide for consistency. BrailleBlaster's Find and Replace tool does this for both plain text *and* formatting, which is what makes it a genuinely global tool rather than a simple word-search box.

---

## How to use this lesson

The first half explains ordinary text replacement and formatting-aware Find and Replace. The second half is a practice document — identify the safest Find and Replace operation for each scenario. The goal is to distinguish **changing words** from **changing styles or text attributes**.

---

## The Concept

### Find and Replace is also a formatting tool

BrailleBlaster's Find and Replace pane can search for text and can also work with formatting. The Formatting window lets the user specify styles, containers, and text attributes for finding or replacing formatted material.

This is particularly useful when a long document contains a repeated formatting error.

### Text replacement and formatting replacement are separate decisions

For text:

- Enter the target in **Find**.
- Enter the replacement in **Replace With**.
- Use Match Case when capitalization matters.
- Use Whole Word when a substring should not match inside a longer word.
- Use Replace for controlled, one-at-a-time changes.
- Use Replace All only when the scope is known and safe.

For formatting:

- Open **Edit > Find and Replace**.
- Select **Formatting**.
- Add the desired style, container, or text attribute.
- Configure the replacement formatting as needed.
- Apply the change deliberately.

### Global does not mean careless

Replace All is powerful because it acts everywhere the search matches. A teacher or transcriber should therefore ask:

- Could this string occur inside another word?
- Does capitalization matter?
- Is the formatting pattern actually wrong everywhere?
- Could the search include headings, page information, or notes?
- Should one exception remain untouched?

---

## Step by step in BrailleBlaster

### Basic Find and Replace

1. Go to **Edit > Find and Replace** (`Ctrl+F`).
2. Type the search text into **Find Text**.
3. Optionally check **Match Case** and/or **Whole Word** to narrow the search.
4. Type the replacement into **Replace With**.
5. Click **Find** to locate the next instance, then **Replace** to change that instance and advance to the next — or click **Replace All** to change every instance in the document at once, without stepping through them individually.
6. Click **Close** when finished.

### Finding and Replacing by Formatting

1. Open **Edit > Find and Replace** (`Ctrl+F`).
2. Click **Formatting** to expand the Find/Replace formatting panel.
3. Choose a category — Styles, Containers, or Text Attributes — and select the specific formatting you want.
4. Click **Add** to attach that formatting condition to the Find box (or, for Replace, the Replace box). Use **Reset** to clear a formatting condition you no longer want.
5. Click **Close Formatting** to return to the main Find and Replace window; the formatting condition now appears as text under the Find (and/or Replace) field.
6. Run **Find**, **Replace**, or **Replace All** as with a plain text search — the results are now filtered by the formatting condition as well as by any text entered.

> **Note:** Click **Reset** to clear all selected formatting conditions and checkboxes at once. The most recently searched text itself is preserved in the Find Text and Replace With fields even after a Reset, so you can re-scope a search without retyping the search term.

---

## Worked Demonstration (small, fully correct)

Suppose a document contains:

```text
The term Braille is used throughout the lesson.
braille is also used in the answer key.
braille is used in the teacher notes.
```

If the instruction is to replace the standalone lowercase word `braille` with `Braille`, use:

- Find: `braille`
- Replace With: `Braille`
- Whole Word: checked
- Match Case: checked if only lowercase instances should change

Do not search for `braille` without Whole Word if words such as `brailleable` could occur.

For formatting, suppose every occurrence of a body paragraph was accidentally assigned **Heading 2**. Use Formatting to find the Heading 2 style and replace it with the intended body style rather than changing the text itself.

---

## Practice Document

### Scenario 1 — whole-word text replacement

```text
Find: "cat"
Replace: "dog"

Text:
The cat slept.
The catalog was on the desk.
A cat climbed the tree.
```

### Scenario 2 — capitalization correction

```text
Find: "ueB"
Replace: "UEB"

Text:
UEB is used here.
ueB appears here.
UEB appears again.
```

### Scenario 3 — repeated style error

```text
Ten ordinary paragraphs have accidentally been assigned Heading 3.
One legitimate Heading 3 also exists.
```

### Scenario 4 — emphasis error

```text
Every occurrence of the word "important" has bold emphasis,
but only the instances in the vocabulary section should be bold.
```

### Scenario 5 — dangerous Replace All

```text
Find: "the"
Replace: "a"
Whole Word: unchecked
```

---

## Answer Key

### Scenario 1

Check **Whole Word**. Otherwise `cat` can match inside `catalog`.

### Scenario 2

Use **Match Case** when the intent is to target the specific capitalization pattern rather than every case variation.

### Scenario 3

Do not globally replace Heading 3 unless the legitimate Heading 3 can be excluded. Use contextual selection or a more specific workflow. Formatting-aware Find and Replace is powerful, but it does not understand semantic exceptions automatically.

### Scenario 4

If the formatting pattern itself is reliable, use Formatting. If only a specific section should retain bold, scope the selection rather than replacing every occurrence globally.

### Scenario 5

This is unsafe. Without Whole Word, `the` can occur inside longer words. Replace All should not be used until the match scope has been verified.

### Core principle

**Search broadly; replace narrowly.** Formatting-aware search is most valuable when it eliminates repetitive manual correction without erasing intentional exceptions.

---

---

## Key takeaways

- Find and Replace (`Ctrl+F`) handles plain text search with optional Match Case and Whole Word narrowing.
- The Formatting panel extends search to Styles, Containers, and Text Attributes, with an Add/Not toggle on the Find side for precise, structure-aware corrections.
- Replace All is powerful and should be used only after confirming, via a plain Find pass, that every match really should be changed.
- Only one formatting condition can be active per Find or Replace box at a time; multi-condition corrections require sequential passes.
