# Lab 8: A Safe Find-and-Replace Cleanup

**Time:** about 45 minutes. **Needs:** [Lesson 12](../lessons/12-find-and-replace.md). **File:** `find-replace-cleanup.txt` from the [sample files](../samples/index.md).

## Scenario

Find and Replace is one of the fastest ways to clean a document and one of the fastest ways to damage one. Your job is to make four changes to a short story handout without breaking anything, and to prove it.

This file contains a **deliberate trap**. The name *John* appears alone, in *John Smith*, and inside the surname *Johnson*.

## Before you start

**Save a dated copy of the document before any Replace All.** Name it so you can find it, for example `cleanup-before-replace-all`.

## Steps

### Task 1: The trap

The editor wants the character *John* renamed *Jon* everywhere.

1. Open **Edit > Find and Replace** (`Ctrl+F`).
2. Type `John` in Find, `Jon` in Replace, and leave **Whole Word** and **Match Case** unchecked.
3. Click **Find** and step through the matches. How many are there, and what are they?
4. **Do not click Replace All yet.** Which matches would be wrong?
5. Now check **Whole Word** and **Match Case**, and find again. Which matches remain?
6. Apply the replacement with **Replace All** only after you are satisfied that every remaining match is correct.

**Expected observations.** Without Whole Word, the search finds *Johnson* as well, and a Replace All would turn it into *Jonson*. With Whole Word and Match Case, only the standalone *John* matches remain. You should never discover this by reading the result afterward. Discover it by stepping through the matches first.

### Task 2: Remove the typed bullets

The text has typed bullet characters at the start of list lines. They should be removed and replaced with a list style.

1. Find the bullet character on its own. How many are there?
2. Replace the bullet character with nothing.
3. Apply a list style to each group of list lines, using Repeat Last Style for the second and third lines ([Lesson 4](../lessons/04-layout-styles.md)).

### Task 3: A pattern that matches the wrong thing

A colleague suggests: "Find every line that starts with *Chapter* and a number, and make it a heading."

1. Search for `Chapter` with **Whole Word** checked. How many matches are there?
2. Read each match in context. Are any of them real chapter headings?
3. Decide what the right action is.

**Expected observations.** All three matches sit inside the *Key Events* list. They are list items that happen to contain the word "Chapter," so turning them into headings would damage the structure. The right action here is **no change**. A search tells you where a *word* is. It cannot tell you what a line *is*. You still have to read.

### Task 4: Undo the damage on purpose

Make one deliberately unsafe replacement: replace `the` with `a` with no options checked. Look at what happened. Then open your saved copy and recover.

This is the cheapest way to learn why you save first and use Find before Replace.

## Record your work

| Change | Find | Replace | Options | Matches | Safe? |
| ------ | ---- | ------- | ------- | ------- | ----- |
| Rename John to Jon | | | | | |
| Remove bullets | | | | | |
| Unsafe test | | | | | |

## Debrief questions

1. What three habits would have prevented the *Jonson* problem?
2. When is Replace (one at a time) better than Replace All?
3. Why is "Find first" a better habit than "Replace first and look afterward"?
4. What kind of change would you never run as a Replace All, no matter how careful the search?
