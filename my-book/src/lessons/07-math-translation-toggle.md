# Lesson 7: The Math Translation Toggle

> **Lesson at a glance**
>
> - **Unit:** Unit 1: Universal Lessons
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 1](01-navigating-the-interface.md), [Lesson 3](03-typeface-emphasis.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Explain why braille needs an explicit switch between literary and mathematical symbols.
- Tell a hyphen from a minus sign, and the letter x from a multiplication sign, in context.
- Flag only the true math in a mixed passage with `Ctrl+M`.
- Choose between Nemeth Block and Nemeth Inline indicators.

## Why this matters

Ordinary prose translates directly from print letters to braille letters. Mathematical and scientific notation does not — braille math uses its own linear notation (Nemeth Code, or UEB Technical Material) that doesn't correspond one-to-one with how the expression looks in print. Before BrailleBlaster can translate a stretch of text as math instead of as prose, you have to tell it, explicitly, that the selected text *is* math. That single flag — on or off — is the Math Translation Toggle, and it's the gateway to everything else math-related in the program.

---

## How to use this lesson

The first half explains why toggling matters. The second half is a practice passage where hyphens/dashes and the letter "x" appear in both ordinary prose and genuine math, mixed together on purpose. Decide, instance by instance, which occurrences need `Ctrl+M` and a Nemeth indicator, and which are correctly left as plain literary text. Everything else in this document is already formatted correctly — you are only deciding where math flagging belongs.

---

## The Concept

### Braille has far fewer symbols than print does

Print can distinguish a hyphen (‑) from an en dash (–) from an em dash (—) from a minus sign (−) using four visually distinct glyphs, and it can distinguish the letter *x* from a multiplication sign (×) using two distinct glyphs, one of which is a dedicated mathematical operator. Braille's entire alphabet is built from only 64 possible dot patterns in a single cell. There simply aren't enough distinct symbols for every print character and every print symbol to get its own permanent, context-free braille equivalent — many braille symbols have to do more than one job, and which job they're doing depends entirely on **which braille code is active** when that symbol is produced. Often, this defines when a given print symbol is represented by a single cell, as in the case of a hyphen (dots 36), as opposed to multiple cells in the case of a visually identical minus sign (dot 5, dots 36).

### The same keystroke means different things in different codes

This is the whole reason the toggle exists. In everyday literary UEB:

- A hyphen (as in "well-known") and a dash both translate using **literary punctuation symbols** — braille's hyphen sign.
- The letter **x** translates as, simply, **the letter x**.

But inside Nemeth (or UEB Technical) math notation:

- A **minus sign** is its own distinct mathematical symbol — not the same braille pattern as a literary hyphen, because a math reader needs to be able to tell, unambiguously and instantly, "this is an operation being performed on numbers," not "this is a compound word."
- A **multiplication sign** (×, or a raised dot ⋅) is its own distinct mathematical symbol — not the same braille pattern as the letter x, because in the middle of an equation like `5 x 3`, a braille reader has no way to guess from context alone whether "x" means "multiply" or is actually the variable *x* sitting next to a number with a typo-like space. Print readers resolve this instantly because × and x simply *look* different, or at least different enough. A braille reader can't fall back on that visual cue — the symbol itself has to carry the distinction, which means the transcription has to get it right the first time.

If BrailleBlaster's translator always treated every hyphen as literary and every "x" as the letter x, every minus sign and every multiplication sign in every equation in the document would come out **wrong** — not just stylistically imperfect, but mathematically unreadable, indistinguishable from ordinary prose punctuation and an ordinary letter.

### Why this can't be automatic

BrailleBlaster cannot reliably guess, from the text alone, whether "-" means a hyphen or a minus sign, or whether "x" means the letter or the operator — both readings are grammatically valid English *and* valid math depending on context that only a human reader (or genuine natural-language understanding) can resolve. "5-2 = 3" is unambiguous to a person; "well-known" is unambiguous to a person; but a translation engine applying one fixed rule to every hyphen in the document has no way to tell them apart reliably at scale. That is exactly the gap the **Math Translation Toggle** (`Ctrl+M`) closes: it's the transcriber telling BrailleBlaster, explicitly, "for this specific span of text, use math symbol rules, not literary symbol rules" — and Nemeth Block/Inline indicators (see the Step by Step section below) then mark that boundary for the braille reader too, exactly the way the toggle marks it for the software.

### It isn't only minus signs and multiplication

The same logic extends to other symbols that mean different things in the two contexts —  e.g., parentheses used for a parenthetical remark versus parentheses grouping a mathematical expression. The minus-sign/hyphen and multiplication-sign/letter-x cases are simply the two a transcriber runs into constantly, in nearly every document that mixes prose and math — which is why they're the two this document focuses on.

---

## Step by step

1. Select the text containing the mathematical expression.
2. Toggle math translation on: `Ctrl+M`, or **Math > Toggle Math Translation**. The selection turns bright pink in the Print View.
3. If the document's translation is UEB with Nemeth math, and the expression should be transcribed in Nemeth code, select the (now math-flagged) text again and choose **Math > Nemeth Block** or **Math > Nemeth Inline**, depending on whether the material is a displayed equation or an inline reference.
4. Check the **Braille View** to confirm the indicators appear correctly on either side of the passage.

> **Note:** Turn on the Math toolbar before teaching this lesson — **View > Toolbar > Math** — so the Nemeth Block/Inline and related buttons are visible on screen rather than buried in menus. Math tools are one of the few toolbar groups *not* shown by default.

---

## Worked Demonstration (small, fully correct)

> The team scored 5-2 in the first half, and the well-known coach called for a time-out. Solve for x: 5x-3 = 12. The x-axis on the graph runs from 0 to 10.

- `5-2` → this is a subtraction operation on two numbers → **flag as math**, Nemeth minus sign.
- `well-known` and `time-out` → ordinary compound-word hyphens in prose → **leave as literary text**, no toggle.
- `Solve for x` → "x" here is a word in an ordinary English sentence (referring to the variable, but not itself inside an equation) → **leave as literary text** — the letter x, not a multiplication sign, and there's no operation to flag.
- `5x-3 = 12` → a full equation → **flag as math**; note that "x" *inside* the equation is being used as a variable, not a multiplication sign, so BrailleBlaster's Nemeth translation handles it as a variable automatically once the span is flagged — you don't need to do anything extra to distinguish it from a multiplication x here, because Nemeth notation for variables and for multiplication are already visually distinct symbols once you're in math mode.
- `x-axis` → a hyphenated compound term, ordinary prose usage → **leave as literary text**.

---

## Practice Passage

Decide, for every instance of a hyphen/dash or the letter "x," whether it needs `Ctrl+M` and Nemeth flagging, or should stay as plain literary text.

1. Maria's after-school job pays $12-$2 in taxes, leaving her $10 an hour.
2. If a full box of pencils holds 24 and Maria has 24-9 left, how many has she used?
3. The well-established rule states that 15-8 = 7.
4. Mark an x in the box next to your favorite answer.
5. Solve for x in the equation 3x+5 = 20.
6. The x-ray showed no fractures, and the technician noted the reading as 3x4 centimeters.
7. To find the area, multiply length x width, or write it as 6x4 = 24.
8. The e-mail from the teacher explained that x, in this context, always represents an unknown number.
9. Compute 100-x when x = 37.
10. The bake sale made a profit of $45-$12 in supply costs, for a net gain the treasurer wrote as $33.
11. Her T-shirt read "10x10 = 100" across the front in bold print.
12. The zig-zag pattern on the rug repeats every 6-2 centimeters, according to the design notes — though the designer meant simply "every four centimeters," using an odd print convention.

---

## Answer Key

1. "after-school" → **leave as literary text** (hyphenated compound word). `$12-$2` → **flag as math**; this is subtraction, not a hyphenated word.
2. `24 - 9` → **flag as math**.
3. "well-established" → **leave as literary text** (compound-word hyphen). `15-8 = 7` → **flag as math**.
4. "Mark an x in the box" → **leave as literary text** — this "x" is an instruction to write the letter x, not an operator; there's no equation here at all.
5. `3x+5 = 20` → **flag as math** (the whole equation, including the "x" used as a variable within it).
6. "x-ray" → **leave as literary text** (a hyphenated compound word, not math). `3x4 centimeters` → **flag as math** — this "x" is functioning as a multiplication sign describing dimensions, not as the letter x or a variable.
7. "length x width" → **flag as math** — even though it reads almost like prose, the "x" here is standing in for a multiplication operation between two named quantities. `6x4 = 24` → **flag as math**.
8. "e-mail" → **leave as literary text** (hyphenated compound word). The later "x" ("x, in this context, always represents an unknown number") is a *reference to* the variable in running prose, not an equation — **leave as literary text**; the sentence is talking about x, not performing an operation with it.
9. `100-x` → **flag as math** (subtraction with a variable). The later "x = 37" is part of the same mathematical statement and should be flagged along with it, not treated as a separate case.
10. `$45-$12` → **flag as math**. "$33" standing alone as the stated result is just a number in prose, not itself requiring a fresh math flag beyond the equation it summarizes — but the equation `$45-$12` = the amount does need flagging.
11. "T-shirt" → **leave as literary text** (hyphenated compound word). `10x10 = 100` → **flag as math**, even though it's printed inside quotation marks on the shirt — the content is still a multiplication equation regardless of where it physically appears in the source.
12. "zig-zag" → **leave as literary text** (hyphenated compound word). `6-2 centimeters` → **flag as math** — this is genuinely a subtraction expression in the design notes, even though the sentence goes on to explain, in prose, that the designer really just meant "four centimeters." The equation itself is still math and should be flagged as such; only the surrounding explanatory prose stays literary.

---

## Key takeaways

- `Ctrl+M` (or **Math > Toggle Math Translation**) is the single switch that tells BrailleBlaster to treat selected text as math rather than prose. Math-flagged text is shown in bright pink in the Print View.
- Nemeth Block and Nemeth Inline bracket Nemeth material within a UEB document so the reader knows exactly where the braille code changes and changes back.
- Use Block for displayed/standalone equations; use Inline for short expressions embedded in a sentence.
- These indicators are a UEB-with-Nemeth-context concept — a document translated entirely in a Nemeth-based table generally won't need them.

---

## Source Citations

- *The Rules of Unified English Braille*, §14.6 (Nemeth Code within UEB Text) — defines the code-switching mechanism that requires an explicit boundary between literary and math symbol sets, which is what the Math Translation Toggle implements in BrailleBlaster.
- Braille Authority of North America,  *Guidance for Transcription Using the Nemeth Code within UEB Contexts* — practical guidance on identifying where a math/literary boundary belongs.
- *The Nemeth Braille Code for Mathematics and Science Notation, 1972 Revision*, with 2007–2015 updates — defines the distinct minus-sign and multiplication-sign symbols referenced throughout this document.
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, §1.2.6 (Mathematics and Science) and §1.3 (Partially Technical Works) — governs when a document's occasional math content requires disclosure on the Transcriber's Notes page.
