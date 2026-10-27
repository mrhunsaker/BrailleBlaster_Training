# UEB Practice: Global Find and Replace with Formatting Options

## How to use this document:

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
