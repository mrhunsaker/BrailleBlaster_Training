# Lesson 3: Typeface Emphasis

> **Lesson at a glance**
>
> - **Unit:** Unit 1: Universal Lessons
> - **Suggested time:** about 2 hours
> - **Prerequisites:** [Lesson 1](01-navigating-the-interface.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Name the four standard UEB typeforms and the five transcriber-defined typeforms.
- Choose between the symbol, word, and passage indicator for a stretch of emphasized text.
- Apply the two-word versus three-word threshold correctly.
- Recognize when print emphasis should be disregarded rather than carried into braille.
- Apply emphasis in BrailleBlaster by selecting existing text first.

## Why this matters

Print documents lean on bold, italics, underlining, and color to carry meaning — a bolded key term, an italicized book title, a highlighted warning. None of that survives a straight copy-and-paste into braille. A braille reader can't see that a word was yellow. Braille has its own, much more limited vocabulary for "this text is different," and the transcriber's first and most repeated job is deciding which print emphasis actually matters to the reader and then applying the correct braille equivalent — not the print one.

This is also usually the first hands-on skill a new transcriber practices, because it's low-risk (it's easy to undo), high-frequency (it happens in nearly every document), and it forces learners to start thinking like a braille reader instead of a sighted proofreader.

---

## How to use this lesson

Unlike the heading and list documents in this series, the print emphasis itself (bold, italic, underline, strikethrough, color, highlighting) *is* the information you need — so it's shown using the markup key below rather than stripped out. Your job is to decide, for each instance, (1) which UEB indicator tier applies — symbol, word, or passage — and (2) whether the emphasis should be applied at all, or disregarded per §5.3. Everything else in this document is already correctly formatted.

**Markup key used in the practice passages below** (none of this is native Markdown formatting — it's a plain-text stand-in so the source emphasis is unambiguous when pasted into BrailleBlaster):

| Markup | Represents |
| --- | --- |
| `**text**` | Bold |
| `*text*` | Italic |
| `++text++` | Underline |
| `[SCRIPT]text[/SCRIPT]` | Script / handwriting font |
| `~~text~~` | Strikethrough |
| `[COLOR:red]text[/COLOR]` | Colored text (color named) |
| `[HIGHLIGHT:yellow]text[/HIGHLIGHT]` | Highlighted text (color named) |

---

## The Concept

### Four standard typeforms, five transcriber-defined

*Braille Formats 2016* §5.1.4 states it plainly: UEB defines symbols for italics, bold, underlining, and script. Every other print font attribute — color, highlighting, double underlining, small caps used distinctively, words in a shape, etc. — has no dedicated UEB symbol and instead uses one of five transcriber-defined typeform indicators, assigned in order of first appearance and documented on the Special Symbols page or in a transcriber's note (§5.5.2–§5.5.3).

### Three indicator tiers: symbol, word, passage

Here is the part that trips up most new transcribers: **bold** (or italic, underline, script, or any transcriber-defined typeform) is not one indicator — it's a *family* of three, and which one you use depends on how much text is emphasized (§5.1.4; UEB §9.2–§9.4):

- **Symbol indicator** — covers a single emphasized character (one letter, one digit).
- **Word indicator** — covers a single emphasized word, *or* more than one emphasized character within a word that doesn't extend to the word's end (§5.7.1c: "Use the typeform word indicator when the emphasis applies to more than one symbol").
- **Passage indicator** — covers a run of text spanning **three or more consecutive** emphasized words; it has an explicit opening indicator and a required closing **terminator** (§5.6.1–§5.6.2; UEB §9.4).

The two-versus-three threshold matters: when exactly **two** consecutive words are emphasized, UEB training material (e.g., the NFB's certification Lesson 15 on Typeform Indicators) is explicit that you place the **word indicator before each of the two words separately** — you do *not* jump to a passage indicator until a *third* consecutive word joins them. Passage indicators exist to avoid repeating a word indicator over and over across a long run of emphasized text; for just two words, repeating it twice is actually shorter.

### "Symbols-sequences" — words is a wider category than you'd think

UEB's word-indicator rule doesn't only apply to dictionary words. The technical term used throughout the UEB Rulebook's Section 9 is **word or symbols-sequence** — a "symbols-sequence" is any string of braille symbols bounded by spaces that functions like a word for spacing purposes, even if it isn't one: an abbreviation, a set of initials, a license-plate-style string, a lone number. If print italicizes `IMG_2024`, that's a single symbols-sequence, and the *word* indicator applies to it exactly as it would to an ordinary word — you don't need three separate symbol indicators just because it isn't found in a dictionary.

### When emphasis needs to be disregarded

This is the half of the rule new transcribers most often skip. §5.3 lists specific, recurring situations where print emphasis is **not** carried into braille, because it adds no information for a reader who can't see the visual effect:

- Emphasis used purely for **decorative/layout** purposes with no informational value (§5.3.1, §5.3.6).
- Italics or other emphasis on **single letters standing alone as letters** (§5.3.2), or on **word parts** like isolated prefixes/suffixes (§5.3.3).
- Emphasis on an **entire vocabulary or spelling list** (§5.3.7) — if every item is emphasized identically, the emphasis distinguishes nothing.
- Emphasis on a **title that is a complete heading** (§5.3.5) — the heading format itself is already the reader's cue; adding a typeform on top is redundant. (Note: if that same title is later *mentioned in running text*, the emphasis is restored — §5.3.5's note.)
- Emphasis used only to set off **quoted material** already marked by quotation marks (§5.3.10) — the quotation marks are doing that job already, though the transcriber may judge otherwise case by case.
- Emphasis in **centered, cell-5, or cell-7 headings** in general, unless only *part* of the heading is emphasized, in which case it must be retained for distinction (§5.3.1, §4.3.7).

Conversely, §5.4 is just as clear that emphasis **must** be kept whenever it's meaningful — most commonly when a teacher might reference it directly ("everything in blue will be on the test," §5.4.1) or when it consistently marks glossary terms throughout a book (§5.4.3). The test is always the same question: *does this emphasis carry information the reader needs, or is it decoration?*

### Multiple emphasis in the same passage

When double emphasis occurs (bold italics, bold highlighting), §5.1.5 notes it's often *not* necessary to show both — the transcriber decides whether the primary attribute alone is sufficient, based on whether the secondary attribute adds real distinction.

---

## Step by step

1. In the **Print View**, highlight the character, word, or passage you want to emphasize.
2. Apply the emphasis using any of the three equivalent methods:
   - the keyboard shortcut (fastest once memorized),
   - the corresponding button on the Emphasis toolbar, or
   - the **Emphasis** menu.
3. Confirm the change by glancing at the **Braille View** — the emphasized text now carries the correct braille typeform indicators around it.

To remove emphasis, highlight the same text and apply the same emphasis command again — it toggles off. For a large passage with mixed emphasis, use **Emphasis > Remove Emphasis from Section** (`Ctrl+Shift+R`) to strip everything from the selection in one step, rather than hunting for each individually formatted run.

> **Note:** Two cleanup tools are worth learning alongside the basics, because braille conventions actually call for removing certain print emphasis rather than preserving it: **Emphasis > Remove All Emphasis from Headings** and **Emphasis > Remove All Emphasis from List Prefixes**. Braille headings and list markers are not usually bolded even when their print counterparts are — these tools sweep the whole document in one pass instead of requiring a manual check of every heading and list item.

---

## Worked Demonstration (small, fully correct)

> The **photosynthesis** process in *The Chemistry of Life* requires ++caution when handling open flames++. A student wrote in the margin: [SCRIPT]Remember safety goggles![/SCRIPT]

- `**photosynthesis**` → one word, bold → **bold word indicator**.
- `*The Chemistry of Life*` → four consecutive words (a book title) → **italic passage indicator**, opening before "The" and terminating after "Life."
- `++caution when handling open flames++` → five consecutive words → **underline passage indicator**, terminator at the end.
- The margin note → **script passage indicator** around the whole handwritten sentence (more than two words).

Importantly, with BrailleBlaster the way we apply emphasis or change the typeform is by highlighting the text we want to apply the typeform to, then selecting the emphasis. The software will place the correct character, word, or passage indicators, including terminators as appropriate. One *cannot* type `CTRL+B` and start typing to create bold text in braille. It must be typed, selected, then the bold emphasis must be added. 

---

## Practice Sentences

For each sentence, decide: which typeform, which tier (symbol / word / passage), and whether it should actually be applied per §5.3 — some of these are deliberate "ignore" cases.

1. The abbreviation *CD* should not be misread as the contraction "could" — mark it accordingly.
2. Her license plate read *8X4 22Q* on the report.
3. The term **mitosis** appears on page 42.
4. The book ++Charlotte's Web++ is assigned reading this month, and the ++class discussion++ ++will cover chapters one through three++.
5. In the word **misSpelled**, notice the ++Sp++ that breaks the usual pattern.
6. All twelve words on this week's spelling list — *cat*, *dog*, *run*, *sun*, *fun*, *bun*, *hat*, *bat*, *mat*, *sat*, *rat*, *pat* — are shown in italics in the workbook.
7. On the answer key, correct responses are shown in [COLOR:green]green text[/COLOR] and incorrect responses in [COLOR:red]red text[/COLOR], and the teacher's guide instructs teachers to reference these colors aloud when reviewing with students.
8. The chapter title on its own line reads: *The Age of Exploration*
9. Later in the same chapter, the text mentions that *The Age of Exploration* began in the fifteenth century.
10. A single word, [HIGHLIGHT:yellow]important[/HIGHLIGHT], is highlighted in the middle of an otherwise plain paragraph, and the teacher's edition confirms students should circle this word during the lesson.
11. The entire third paragraph of the essay is shown in [HIGHLIGHT:pink]highlighted pink text[/HIGHLIGHT] in the student's copy, apparently just to make it stand out on the page, with no explanation given anywhere in the material.
12. The prefix ~~dis~~- and suffix -~~ible~~ are shown in a strikethrough font in this word-building exercise, indicating letters that were removed.
13. "I can't believe it," she said, the word *can't* italicized in the original for emphasis.
14. The dedication page reads, in italics: *For my grandmother, who taught me to read.*

---

## Answer Key

1. **Grade 1 territory, not a typeform question** — *(included as a contrast case)* `CD` isn't print-emphasized here at all; it's flagged with a **UEB grade 1 symbol indicator**, not a typeform indicator, because the risk is misreading the *braille contraction*, not representing print italics/bold. Good instinct-check: not every "mark this so it reads correctly" situation is a typeform.
2. Bold/italic not shown, but if it *were* italicized: `8X4 22Q` is a **symbols-sequence**, not a dictionary word — still takes the **word indicator** (once for the whole sequence, since it's bounded by spaces like any word), not letter-by-letter symbol indicators.
3. **Bold, word indicator** — one word.
4. Three separate spans: `Charlotte's Web` (2 words) → **underline word indicator before each of the two words**; `class discussion` (2 words) → same, **word indicator twice**; `will cover chapters one through three` (6 words) → **underline passage indicator** with terminator. This sentence is designed to show the 2-vs-3+ threshold happening twice in one sentence.
5. Only "Sp" is underlined within the word "misSpelled" — that's underline applied to **more than one symbol within a word**, so per §5.7.1c it takes the **underline word indicator**, with a **terminator** immediately after "Sp" since regular type resumes before the end of the word.
6. **Disregard the emphasis entirely** — an entire spelling list uniformly italicized carries no distinguishing information (§5.3.7).
7. **Retain both colors as transcriber-defined typeforms** (e.g., TDT 1 for green, TDT 2 for red) — the teacher explicitly references the colors aloud, so this is meaningful, not decorative (§5.4.1).
8. **Disregard** — italics on a title that is a complete heading (its own line, functioning as a chapter heading) is covered by §5.3.5; the heading format alone is the reader's cue.
9. **Retain** — same title, but now mentioned within running text rather than standing as its own heading; §5.3.5's note explicitly restores the emphasis here. Since it's three words, this is an **italic passage indicator**.
10. **Retain as a transcriber-defined typeform (highlight)**, word indicator — the teacher's edition confirms it's functionally meaningful (students act on it), not decorative.
11. **Disregard** — a full paragraph highlighted with no stated purpose is the textbook case of decorative-only emphasis (§5.3.1, §5.3.6); there's nothing here for a braille reader to act on differently.
12. **Retain as a transcriber-defined typeform (strikethrough)** — this is a word-building exercise where the struck-through letters are pedagogically the entire point (contrast with #6, where the emphasis added nothing); use symbol or word indicators as appropriate to "dis" and "ible" individually.
13. **Retain — italic word indicator.** A single emphasized word inside quotation marks, and the emphasis is doing something the quotation marks alone don't (marking the specific word under discussion), so §5.3.10's general "quoted matter" exception doesn't apply here — this isn't a case of the quotation marks already doing the job on their own.
14. **Disregard** — italics used purely as a stylistic/decorative treatment for a dedication line, per §5.3.6's own example ("italics used for a dedication").

---

## Key takeaways

- Emphasis is applied to existing text, at the character, word, or passage level — never typed "into."
- Bold, Italics, Underline, and Script map to the four standard print typeforms; Transcriber's Notes and Transcriber-Defined Typeforms cover everything print formatting can throw at you that doesn't have a direct braille equivalent.
- Not every instance of print emphasis should be preserved — braille formatting is governed by *Braille Formats 2016* and by reader usefulness, not by strict visual fidelity to the print page.
- Use the bulk-removal tools (Remove Emphasis from Section, Remove All Emphasis from Headings/List Prefixes) instead of manually un-formatting text one instance at a time.

---

## Source Citations

- *Braille Formats 2016*, §5 Typeforms — §5.1 (Fundamentals, especially §5.1.4–§5.1.6), §5.2 (Distinctive Typefaces and Font Attributes), §5.3 (When Print Font Attributes May Be Ignored, §5.3.1–§5.3.11), §5.4 (Retaining Font Attributes), §5.5 (Color, Highlighting, and Other Print Fonts, §5.5.1–§5.5.3), §5.6 (Font Emphasis for One or More Paragraphs), §5.7 (Emphasized Letters within a Word, §5.7.1).
- *The Rules of Unified English Braille*, Section 9: Typeforms — §9.1 (Deciding When to Use Typeform Indicators), §9.2 (Typeform Symbol Indicators), §9.3 (Typeform Word Indicators), §9.4 (Typeform Passage Indicators and Terminators), §9.5 (Transcriber-Defined Typeform Indicators).
- National Federation of the Blind, *Braille Certification Training Manual*, Lesson 15: Typeform Indicators, Small Capital Letters — practical training reference for the two-word-versus-three-word word/passage threshold and the "symbols-sequence" terminology. Available via nfb.org. This is a secondary training resource, not a primary BANA/ICEB publication — confirm against the UEB Rulebook itself for production work.
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, available at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html).

*Section numbers and subsection text verified directly against the BANA online edition at brailleauthority.org.*
