---
title: "BrailleBlaster: From Print to Braille"
subtitle: "A Trainer's Manual for Teaching Print-to-Braille Transcription"
author: "Michael Ryan Hunsaker, M.Ed., Ph.D."
date: "August 6, 2026"
---

# About This Manual

This manual is the companion script for a tutorial series on **BrailleBlaster**, the free, open-source braille transcription program developed by the American Printing House for the Blind (APH). It is written for the person delivering the training as much as for the person receiving it: each chapter can be read on its own, taught as a stand-alone lesson, or stitched together into a full course that takes a new transcriber from a blank screen to a properly formatted, embossable braille file.

The chapters follow the same arc a new transcriber actually walks: first the everyday mechanics of formatting text and applying styles, then the tools that make math and tables manageable, then the file-format and workflow knowledge that separates a hobbyist from a production transcriber. Topics are grouped into five parts, moving from **Foundations** through **Intermediate Tools**, **Files You'll Meet on the Job**, **Advanced Practice**, and finally a closing look at **Pandoc**, the engine quietly running underneath much of BrailleBlaster's file handling.

Every chapter follows the same shape, so trainees know what to expect:

- **Why It Matters** — the real-world transcription problem the feature solves.
- **The Concept** — what is actually happening to the text or the document.
- **Step by Step** — the click path, using the menu names and shortcuts in the current BrailleBlaster release.
- **Worked Example** — a concrete example you can reproduce on screen.
- **Trainer Tips and Pitfalls** — what to watch for when this is being taught live.
- **Key Takeaways** — a short recap.
- **Practice Exercise** — something to hand the trainee before moving on.

> **Note:** BrailleBlaster is under active development. Menu wording, icon placement, and dialog layout can shift slightly between releases. The instructions here reflect the BrailleBlaster 3.x / BrailleBlaster-NG generation of the software (the open-source, GPL3 release). If a menu item has moved in your installed version, the underlying concept and workflow described here will still apply — use Help > Search or the built-in Math Help / Style Appendix to locate the renamed item.

## A Note on Formatting Conventions in This Document

Because this manual is written in Markdown and is meant to convert cleanly to Word, PDF, and other formats, it uses a small, consistent set of conventions throughout:

- **Menu paths** are written in bold with an arrow, like this: **File → Open**.
- Keyboard shortcuts are written in a fixed-width code style, like this: `Ctrl+M`.
- *Italics* are used for the first mention of a new term, for on-screen labels, and for light emphasis.
- <u>Underline</u> is used sparingly, generally to mirror an example of underlined print text that a trainee is being asked to transcribe.
- Blockquotes are used for callouts:

> **Trainer Tip:** Callouts like this one flag something worth saying out loud during a live session — a common point of confusion, a shortcut worth drilling, or a place where trainees typically make the same mistake.

- Numbered lists are reserved for procedures performed in order. Bulleted lists are used for options, settings, or reference information that isn't sequential.
- Tables are used for reference material — keyboard shortcuts, margin specifications, and settings — that a trainee will want to scan rather than read top to bottom.

## Contents

**Part I — Foundations**
1. Applying Text Formatting and Transcriber's Formats  
2. Applying Layout Styles  
3. The Math Translation Toggle and Nemeth Indicators  
4. The ASCII Math Hub  
5. Opening and Converting Word Documents  
6. Paper Size and Connecting to an Embosser  

**Part II — Intermediate Tools**  
7. The Spatial Math Editor  
8. Spatial Number Lines  
9. Global Find and Replace with Formatting Options  

**Part III — Files You'll Meet on the Job**  
10. The eBraille Format  
11. Importing and Working with NIMAS/XML Files  

**Part IV — Advanced Practice**  
12. Importing from Markdown, OpenOffice, LaTeX, and XML  
13. Transcriber Tasks: Running Heads and Page Numbering  
14. Setting Up and Managing Embossers  
15. Advanced Formatting: Boxed Material, Plays, Poems, and Deep Lists  
16. The Contraction Relaxer  

**Part V — Expert Level Information**  
17. What Pandoc Does for BrailleBlaster  

---

# Part I — Foundations: Getting Comfortable in BrailleBlaster

Part I covers the formatting moves a transcriber makes dozens of times a day: applying character-level emphasis, choosing the right layout style for a paragraph or list, and turning ordinary text into math when the print material calls for it. Everything in this part assumes only that BrailleBlaster is installed and a document — even a short pasted paragraph — is open on screen.

## Chapter 1: Applying Text Formatting and Transcriber's Formats

### Why It Matters

Print documents lean on bold, italics, underlining, and color to carry meaning — a bolded key term, an italicized book title, a highlighted warning. None of that survives a straight copy-and-paste into braille. A braille reader can't see that a word was yellow. Braille has its own, much more limited vocabulary for "this text is different," and the transcriber's first and most repeated job is deciding which print emphasis actually matters to the reader and then applying the correct braille equivalent — not the print one.

This is also usually the first hands-on skill a new transcriber practices, because it's low-risk (it's easy to undo), high-frequency (it happens in nearly every document), and it forces trainees to start thinking like a braille reader instead of a sighted proofreader.

### The Concept

BrailleBlaster calls this family of tools **Emphasis**. Emphasis can only be applied to text that already exists on the page — highlight it first, then apply the emphasis. BrailleBlaster supports emphasis at three "grains": a single **character**, a **word**, or a **passage** (a run of text spanning multiple words, sentences, or even paragraphs). The grain isn't something you pick from a menu — it's simply how much text you highlight before applying the emphasis. Highlight one letter and bold it, and only that letter is bolded in braille (this matters for things like a bolded single variable in a math expression); highlight three paragraphs and bold them, and the whole passage carries the emphasis.

The standard emphasis types, with their default shortcuts, are:

| Emphasis  | Shortcut      | Typical Use                                            |
| --------- | ------------- | ------------------------------------------------------ |
| Bold      | `Ctrl+B`      | Bolded print terms, headings inside body text          |
| Italics   | `Ctrl+I`      | Book/publication titles, foreign words, light emphasis |
| Underline | `Ctrl+U`      | Underlined print text                                  |
| Script    | `Alt+Shift+S` | Text meant to mimic handwriting in print               |

Beyond these four "print typeform" options, BrailleBlaster provides two categories that don't correspond to anything in print at all:

- **Transcriber's Note (TN) indicators** mark text the *transcriber* is adding to explain something to the braille reader — not part of the original print. A TN indicator opens before the note and closes after it; applied across several elements, the opening indicator appears once at the very start and the closing indicator once at the very end, rather than being repeated on every paragraph.
- **Transcriber-Defined Typeforms** solve the opposite problem: print formatting that has no standard braille equivalent at all, such as highlighting, colored font, or double-underlining. BrailleBlaster lets you assign up to five of these (`Shift+Alt+1` through `Shift+Alt+5`), and the meaning of each one is defined in writing on the document's Transcriber's Notes page, so the reader knows that, for example, "Transcriber-Defined 1" means "this text was highlighted in yellow in the original."

This last point is worth dwelling on with trainees: **braille doesn't invent new symbols to represent print formatting** — every transcriber-defined typeform must be explicitly defined for the reader up front. Making that call (does this highlighting matter enough to preserve, or is it decorative and safe to drop?) is a judgment skill, not a button-press skill, and it's one worth discussing early.

### Step by Step

1. In the **Print View**, highlight the character, word, or passage you want to emphasize.
2. Apply the emphasis using any of the three equivalent methods:
   - the keyboard shortcut (fastest once memorized),
   - the corresponding button on the Emphasis toolbar, or
   - the **Emphasis** menu.
3. Confirm the change by glancing at the **Braille View** — the emphasized text now carries the correct braille typeform indicators around it.

To remove emphasis, highlight the same text and apply the same emphasis command again — it toggles off. For a large passage with mixed emphasis, use **Emphasis → Remove Emphasis from Section** (`Ctrl+Shift+R`) to strip everything from the selection in one step, rather than hunting for each individually-forma tted run.

> **Note:** Two cleanup tools are worth teaching alongside the basics, because braille conventions actually call for removing certain print emphasis rather than preserving it: **Emphasis → Remove All Emphasis from Headings** and **Emphasis → Remove All Emphasis from List Prefixes**. Braille headings and list markers are not usually bolded even when their print counterparts are — these tools sweep the whole document in one pass instead of requiring a manual check of every heading and list item.

### Worked Example

Give trainees this short passage to transcribe by hand as a first exercise:

> The captain's log read, *"We are three days from port,"* and beneath it, in the margin, someone had written **do not open until instructed**.

Walk through the decisions out loud:
- The italicized quotation is a genuine print distinction (a direct quote) — apply *Italics*.
- The bolded margin note is print emphasis that should transfer — apply **Bold**.
- If the margin note was also handwritten in the original (a common textbook device for "student annotations"), that's a candidate for *Script* instead of Bold, since Script specifically signals handwriting-like text rather than typographic boldness. This is a good moment to point out that BrailleBlaster gives you the *tool*, but deciding *which* tool matches the print intent is the actual transcription skill.

### Trainer Tips and Pitfalls

> **Trainer Tip:** New transcribers often try to apply emphasis and then type — that is, they turn on Bold and expect everything they type next to be bold, the way a word processor works. BrailleBlaster's Emphasis tools work the opposite way: select existing text first, then apply the emphasis. This single habit change is worth drilling before moving on.

> **Trainer Tip:** Ask trainees to open the **Braille View** side-by-side with the **Print View** for this entire chapter. Seeing the emphasis indicators actually appear and disappear in braille as they toggle bold/italics/underline on and off does more to build intuition than any amount of explanation.

A common early mistake is treating every instance of print bold as worth preserving. Encourage trainees to ask "would a braille reader lose meaning without this?" — chapter titles restated in bold within running text, decorative bolding, and inconsistent publisher styling are all candidates for being dropped rather than dutifully reproduced.

### Key Takeaways

- Emphasis is applied to existing text, at the character, word, or passage level — never typed "into."
- Bold, Italics, Underline, and Script map to the four standard print typeforms; Transcriber's Notes and Transcriber-Defined Typeforms cover everything print formatting can throw at you that doesn't have a direct braille equivalent.
- Not every instance of print emphasis should be preserved — braille formatting is governed by *Braille Formats 2016* and by reader usefulness, not by strict visual fidelity to the print page.
- Use the bulk-removal tools (Remove Emphasis from Section, Remove All Emphasis from Headings/List Prefixes) instead of manually un-formatting text one instance at a time.

### Practice Exercise

Hand trainees a one-page excerpt from any print textbook containing at least: one bolded key term, one italicized title, one underlined phrase, and one instance of highlighting or colored text. Ask them to transcribe the formatting decisions onto a worksheet before touching BrailleBlaster — for each instance, they should note whether they'd preserve it, and if so, with which tool. Then have them apply their decisions in BrailleBlaster and compare the Braille View output against their worksheet.

## Chapter 2: Applying Layout Styles

### Why It Matters

Emphasis (Chapter 1) changes how individual words look. **Styles** change how whole elements — paragraphs, list items, headings, block quotations — are laid out on the braille page: their margins, their spacing, whether they start a new line, and how they behave when they cross a page break. If emphasis is the "font" of braille, styles are the "paragraph formatting," and they matter more, because braille margins are a reader's primary navigation cue. A misapplied style doesn't just look wrong — it can make a document genuinely hard to read by finger.

### The Concept

Every block of text in a BrailleBlaster document has exactly one style applied to it at a time. BrailleBlaster's styles are **contextual**: the same style name can behave differently depending on where it sits in the document structure, because the underlying rules come from *Braille Formats 2016*, the formatting standard published by the Braille Authority of North America (BANA). You don't set margins by typing numbers (in the normal case) — you choose a style, and BrailleBlaster applies the correct BANA-compliant margins for you.

The core style families a new transcriber meets immediately are:

- **Body Text** — the default style, indented paragraphs with 3-1 margins (first line begins in cell 3, runover lines begin in cell 1). This is what plain pasted text becomes automatically.
- **Headings** — multiple heading levels (centered headings, cell-5 headings, and so on), each with its own BANA-defined spacing before and after.
- **List** — for enumerated or bulleted print lists; list styles carry their own margin pairs and can be nested.
- **Block/Box styles** — for material that's visually set off in print (sidebars, call-out boxes) and needs to be visually set off in braille as well.

Some styles act as **containers** — List, Poetry, and Box styles among them. In the **Breadcrumbs** view, a container-level style is prefixed with the word "CONTAINER," and clicking it selects every element that belongs to that container at once. This distinction matters because it's the basis for one of the most useful cleanup tools in the program, **Unwrap Element** (see below).

### Step by Step

**Applying a style:**

1. Place the cursor inside the element (or highlight a run of elements) you want to restyle.
2. Go to **Styles** and choose the style, or click its button on the Styles toolbar.
3. The style is applied immediately — check the **Style View** (usually docked at the left of the window) or the **Breadcrumbs** bar to confirm.

**Repeating the last style**, useful when formatting a long run of similarly-structured material (a glossary, a list of practice problems):

1. Place the cursor in the next element.
2. Go to **Styles → Repeat Last Style** or use `Ctrl+R`.

**Viewing what's applied:** Turn on **Breadcrumbs** (**View → Toggle Views → Breadcrumbs**) to see, at a glance, every style wrapping the text at the cursor's position — outermost container first, most specific style last, like a trail leading back to exactly where you are in the document's structure.

**Removing a style** without replacing it with another one:

1. With Breadcrumbs visible, click on the element you want to affect.
2. Click the container button for that element in Breadcrumbs to select it.
3. Go to **Tools → Unwrap Element**.

Unwrap Element removes List, Poetic Stanza, Box, Full Box, and Prose styles, and returns the text to Body Text — 3-1 margins, indented paragraph. (If Unwrap Element is greyed out, it means the current selection isn't one of those unwrappable container styles; apply a different style directly instead.)

**Adjusting how many style levels you see:** Some styles — headings and lists especially — have multiple numbered levels (Heading 1, Heading 2, and so on). BrailleBlaster shows five by default but supports up to eight. Go to **Styles → Configure → Style Levels** and choose the number that fits the document's structure — a heavily-nested textbook chapter may need more than the default five.

### Worked Example

Take a short print excerpt with a heading, two paragraphs of body text, and a three-item bulleted list:

1. Paste the raw text — it lands entirely in Body Text.
2. Select the heading line, apply the appropriate heading level.
3. Leave the two paragraphs as Body Text (the default is usually already correct).
4. Select the three list lines and apply the List style. Notice, in Breadcrumbs, the CONTAINER label wrapping all three lines as one unit.
5. Use `Ctrl+R` on the second and third list items after applying it to the first, to demonstrate how much faster Repeat Last Style is for uniform material.

### Trainer Tips and Pitfalls

> **Trainer Tip:** Trainees coming from word processors expect "formatting" to mean fonts and colors. Spend a minute up front reframing styles as *structural* — you're telling BrailleBlaster what kind of thing this text *is* (a heading, a list, a quotation), not how it should merely look. The visual result follows from that identity, per BANA rules, rather than being something you dial in by hand.

> **Trainer Tip:** The CONTAINER concept in Breadcrumbs is one of the more confusing ideas for new transcribers, because it isn't visible in the Print View at all — it only shows up in Breadcrumbs. Make a habit of keeping Breadcrumbs on during the entire styles unit.

A frequent pitfall: applying a list style to text that isn't actually a structured list in the source (for example, a run of short sentences that merely *look* list-like because they're short). Encourage trainees to ask whether the print material is doing something structural (enumeration, sequence, parallel items) before reaching for the List style.

### Key Takeaways

- Styles control paragraph-level layout (margins, spacing, page-break behavior); Emphasis controls character-level typeform.
- Styles are contextual and BANA-compliant — you choose *what the text is*, and BrailleBlaster computes the correct margins.
- Breadcrumbs shows every style wrapping the current text, with CONTAINER-level styles (List, Poetry, Box) called out explicitly.
- Unwrap Element is the fast path back to plain Body Text from any container style.
- Repeat Last Style (`Ctrl+R`) is the efficient way to format long runs of parallel material.

### Practice Exercise

Give trainees a one-page excerpt containing at least two heading levels, a short numbered list, and a block quotation. Have them apply styles from scratch, then use Breadcrumbs to narrate, out loud or in writing, the full style "trail" at three different points in the document.

## Chapter 3: The Math Translation Toggle and Nemeth Indicators

### Why It Matters

Ordinary prose translates directly from print letters to braille letters. Mathematical and scientific notation does not — braille math uses its own linear notation (Nemeth Code, or UEB Technical Material) that doesn't correspond one-to-one with how the expression looks in print. Before BrailleBlaster can translate a stretch of text as math instead of as prose, you have to tell it, explicitly, that the selected text *is* math. That single flag — on or off — is the Math Translation Toggle, and it's the gateway to everything else math-related in the program.

### The Concept

Selecting text and pressing `Ctrl+M` (or using **Math → Toggle Math Translation**, or right-clicking and choosing Math from the context menu) marks that selection for math translation instead of literary translation. In the Print View, text marked this way is highlighted bright pink, which makes it easy to spot — both for the transcriber proofreading their own work and for a trainer scanning a trainee's screen from across the room.

Under the hood, BrailleBlaster represents math using **ASCII Math**, a compact linear notation for writing equations with a standard keyboard (Chapter 4 covers this in depth). Once text is flagged as math and written in ASCII Math, BrailleBlaster translates it into whichever braille math code the document's translation settings specify — UEB Technical Material, or UEB with Nemeth in mathematical contexts.

**Nemeth indicators** are the easiest, most visible example of what math translation actually produces, which is why they're a good first demonstration for new trainees. When Nemeth material appears inside a document that's otherwise translated in UEB, BANA formatting rules require the Nemeth passage to be clearly bracketed off from the surrounding literary text so the reader's fingers know exactly where the code switches. BrailleBlaster automates this with two options:

- **Nemeth Block** — places the opening indicator on the line *before* the Nemeth material and the closing indicator on the line *after* it. Use this for anything longer than a short inline expression: a displayed equation, a multi-line derivation, a boxed formula.
- **Nemeth Inline** — places the indicators immediately before and after the material, separated only by a space, keeping it within the flow of a sentence. Use this for a short expression embedded in running prose, like referring to *x* + 2 in the middle of a paragraph.

### Step by Step

1. Select the text containing the mathematical expression.
2. Toggle math translation on: `Ctrl+M`, or **Math → Toggle Math Translation**. The selection turns bright pink in the Print View.
3. If the document's translation is UEB with Nemeth math, and the expression should be transcribed in Nemeth code, select the (now math-flagged) text again and choose **Math → Nemeth Block** or **Math → Nemeth Inline**, depending on whether the material is a displayed equation or an inline reference.
4. Check the **Braille View** to confirm the indicators appear correctly on either side of the passage.

> **Note:** Turn on the Math toolbar before teaching this chapter — **View → Toolbar → Math** — so the Nemeth Block/Inline and related buttons are visible on screen rather than buried in menus. Math tools are one of the few toolbar groups *not* shown by default.

### Worked Example

Take a short paragraph of prose that contains one inline reference to a variable and one displayed equation on its own line:

> Solve for *x* in the equation below.
>
> x + 5 = 12

1. Select "x" in the first line, toggle Math Translation (`Ctrl+M`), then apply **Nemeth Inline** if the document uses Nemeth for math.
2. Select the displayed equation on its own line, toggle Math Translation, then apply **Nemeth Block**, since it's a self-contained displayed equation rather than a word inside a sentence.
3. Compare the two results in the Braille View — trainees should be able to see and describe the difference between the inline indicators (tight to the material, space-separated) and the block indicators (their own line before and after).

### Trainer Tips and Pitfalls

> **Trainer Tip:** This is a good moment to explicitly separate two different decisions trainees are making at once: (1) *is this math?* (the `Ctrl+M` toggle) and (2) *how should the boundary be marked?* (Block vs. Inline). Trainees sometimes reach for Nemeth Block/Inline before flagging the math translation at all — walk through the two-step order every time until it's automatic.

A common pitfall: forgetting that Nemeth Block/Inline only matters when Nemeth material appears *within* a UEB document. If the whole document's translation setting is a Nemeth-based table already, these indicators generally aren't needed, because there's no code-switch for the reader to navigate. This is worth flagging so trainees don't apply indicators reflexively regardless of context.

### Key Takeaways

- `Ctrl+M` (or **Math → Toggle Math Translation**) is the single switch that tells BrailleBlaster to treat selected text as math rather than prose. Math-flagged text is shown in bright pink in the Print View.
- Nemeth Block and Nemeth Inline bracket Nemeth material within a UEB document so the reader knows exactly where the braille code changes and changes back.
- Use Block for displayed/standalone equations; use Inline for short expressions embedded in a sentence.
- These indicators are a UEB-with-Nemeth-context concept — a document translated entirely in a Nemeth-based table generally won't need them.

### Practice Exercise

Give trainees a short worksheet passage containing three inline variable references and one displayed, multi-term equation. Have them flag each as math, choose Block or Inline appropriately for each instance, and then explain — in their own words — why they made each choice.

## Chapter 4: The ASCII Math Hub

### Why It Matters

Once text is flagged as math (Chapter 3), someone still has to *write* the expression in a form BrailleBlaster can translate — and typing raw ASCII Math from memory is a real skill that takes time to build, especially for symbols that don't have an obvious keyboard equivalent (a square root, a Greek letter, a set-union symbol). The **ASCII Math Hub** exists to close that gap: it's a browsable, searchable palette of every common mathematical symbol and structure, each shown as both its ASCII Math code and an image of how it prints, so a transcriber can build an unfamiliar equation without having to already know the syntax by heart.

### The Concept

BrailleBlaster uses **ASCII Math**, a compact linear notation, to represent mathematical equations before they're translated into braille math code. If you already know ASCII Math syntax, you can simply type it directly into the Print View once math translation is toggled on. The ASCII Math Hub is the assisted alternative — and, in practice, the tool most transcribers reach for whenever a print equation contains anything beyond the simplest arithmetic.

The Hub organizes symbols and structures into tabs, which can be shown or hidden individually from the Hub's own **Settings → Show Tabs** menu:

- **Operation Symbols** — division, multiplication, union, and similar operators.
- **Miscellaneous Symbols** — absolute value, angle, plus-minus, and other frequently-used marks.
- **Relation Symbols** — equals, greater-than, proportional-to, and other relational operators.
- **Greek Symbols** — the full Greek alphabet, upper and lower case.
- **Logical Symbols** — true, there-exists, if-and-only-if, and similar logic notation.
- **Grouping Symbols** — the various sizes and styles of brackets, braces, and parentheses.
- **Arrows** — the full family of directional and double arrows.
- **Accents** — circumflexes, dots, and other diacritical marks used over variables.
- **Functions** — abbreviations for cosine, cotangent, cosecant, and other named functions.
- **Special** — column vectors, complex subscripts, matrices, and script-order templates.
- **Examples** — a reference tab showing common composite structures (a complex fraction, an exponent, an overbar) in both ASCII Math and image form side by side, so you can match what's in front of you on the printed page to the code that produces it.
- **Search** — type any symbol name into the search box and click OK to jump straight to it, rather than browsing tab by tab.

### Step by Step

1. Select the location in your document where the equation belongs (or select existing math-flagged text you want to edit).
2. Go to **Math → ASCII Math Hub**.
3. Browse the tabs, or use **Search**, to find each symbol or structure the equation needs. The **Examples** tab is the fastest starting point for a composite structure like a fraction, since it shows the whole pattern at once rather than requiring you to assemble it symbol by symbol.
4. Build the equation in the Hub's entry area.
5. Click **Insert** to place the finished equation into your document at the cursor position.
   - If you're revising a previously entered equation, choose **Replace Current Math** instead, and use the **Previous Math** / **Next Math** buttons to step through every math element already in the document.
6. Back in the Print View, confirm the inserted equation is highlighted bright pink — the same visual cue used for any math-flagged text.

> **Trainer Tip:** The Hub can be expanded to fill the whole screen (**Settings → Full Screen** inside the Hub window), and its font size can be increased or decreased with the Plus/Minus buttons next to the Font Size control. For a training room with a projector, maximizing the Hub before demonstrating a complex symbol search makes it far easier for trainees at the back of the room to follow along.

### Worked Example

A classic first Hub exercise, and a good one to use explicitly with trainees, is **a complex fraction** — a fraction whose numerator or denominator is itself a fraction, which is awkward to type from memory but sits right in the Hub's Examples tab:

1. Place the cursor where the fraction belongs and toggle math translation on if it isn't already.
2. Open **Math → ASCII Math Hub**.
3. Go to the **Examples** tab and locate the complex fraction entry — note both its ASCII Math code and its printed appearance shown side by side.
4. Either insert the example directly and edit the placeholder numbers, or use it as a template to type the equivalent structure with your own values, using the **Search** tab if you need to look up any additional symbol (a variable with a subscript, for instance).
5. Click **Insert**, then check the Braille View to see the resulting Nemeth or UEB Technical rendering of the complex fraction.

This example is worth using precisely because it's the kind of structure a transcriber can't reliably improvise from memory — it's exactly the case the Hub was built for.

### Trainer Tips and Pitfalls

> **Trainer Tip:** Some trainees try to type ASCII Math directly into the Print View from the very first lesson, skipping the Hub entirely, because they've read about ASCII Math syntax online. That's a legitimate long-term goal — experienced transcribers often do work faster typing directly — but for anyone still building fluency, starting with the Hub (especially the Examples tab) builds correct habits and avoids silent syntax errors that only show up as garbled braille.

A common early mistake is not noticing that entered math is highlighted pink and mistaking a plain, un-flagged equation for a completed one. Make it routine to check the Print View highlighting immediately after every Hub insertion.

### Key Takeaways

- The ASCII Math Hub is an assisted equation builder for ASCII Math, BrailleBlaster's underlying linear math notation.
- Its tabs mirror the categories of mathematical notation a transcriber is likely to need — operators, relations, Greek letters, grouping symbols, functions, and more.
- The Examples tab shows common composite structures (like a complex fraction) as both code and image, making it the fastest way to build something you recognize by sight but wouldn't know how to type from memory.
- Insert places new math; Replace Current Math, together with Previous Math/Next Math, is how you revise math that's already in the document.

### Practice Exercise

Give trainees three print expressions of increasing complexity: a simple fraction, a complex (nested) fraction, and an expression involving a Greek letter and an exponent. Have them build all three using the ASCII Math Hub, insert them, and then locate each one again afterward using Previous Math/Next Math to practice navigating math elements in a longer document.

## Chapter 5: Opening and Converting Word Documents

### Why It Matters

In production transcription work, print material rarely arrives as a NIMAS file — it just as often arrives as a Word document (.docx) or, less commonly today, an OpenDocument Text file (.odt) from a publisher, a teacher, or a parent. BrailleBlaster can open both directly, using the structure already present in the file — headings, lists, bold and italic runs, tables — to jump-start the transcription instead of starting from a blank page. How well that jump-start works, though, depends entirely on how well-structured the source file is, which makes this chapter as much about *diagnosing* a Word document as it is about opening one.

### The Concept

When BrailleBlaster opens a .docx or .odt file, it reads the document's underlying structure — not just what the text looks like, but what Word or the word processor recorded it *as*: a Heading 1, a bulleted list, a table, a bolded run. BrailleBlaster maps that structure onto its own styles wherever it can, which means a well-built Word document can arrive in BrailleBlaster already carrying most of its layout styles and much of its emphasis correctly applied.

The key phrase is *well-built*. Word and OpenOffice both allow a document to *look* structured — indented to look like a list, larger and bold to look like a heading — without actually *being* structured that way underneath. A paragraph that's merely indented with the Tab key and bolded by hand looks like a heading on screen, but Word has no idea it's a heading; it's still, structurally, an ordinary paragraph. BrailleBlaster inherits that ambiguity. This is the single biggest source of "why didn't this come in formatted correctly?" questions from new transcribers, and it's worth naming explicitly during training rather than letting trainees discover it by trial and error.

### Step by Step: Opening a Well-Formatted Word Document

1. Go to **File → Open** (`Ctrl+O`).
2. Select the .docx or .odt file. BrailleBlaster recognizes both extensions directly, alongside NIMAS XML, EPUB, HTML, Markdown, LaTeX, plain text, and several others.
3. Review the incoming document with Breadcrumbs turned on (**View → Toggle Views → Breadcrumbs**), scanning headings, lists, and emphasized text to see how much came in correctly mapped.
4. Correct anything that mapped imperfectly — this is normal even with a well-built source file, and is not a sign of an error on your part.

### Troubleshooting Poorly Formatted Word or ODT Documents

When a document arrives with structure that was faked visually rather than built properly (manually-indented "headings," tab-and-space "lists," font-size changes standing in for real heading levels), expect BrailleBlaster to bring it in largely as undifferentiated Body Text. Work through it methodically rather than reformatting reactively line by line:

1. **Read before you fix.** Skim the whole incoming document first — in the original Word/ODT file if possible, side by side with BrailleBlaster — to understand what the author actually intended structurally (where the real headings, real lists, and real emphasis are meant to be), before applying any styles.
2. **Fix structure before emphasis.** Apply correct heading and list styles first. Fixing emphasis on text that's about to be restyled anyway wastes effort, since restyling a container can affect how emphasis displays within it.
3. **Use Find and Replace with Formatting** (covered in full in Chapter 9) to locate every instance of a particular visual pattern — for example, every paragraph that's merely bolded and slightly larger, standing in for a heading — and correct them as a batch rather than one at a time.
4. **Watch for inconsistency, not just absence.** A poorly-formatted document is often *inconsistently* fake-structured: some "headings" are done with bold-and-larger-font, others with all-caps, others with manual centering. Don't assume the same fix pattern applies throughout; verify each section.
5. **When in doubt, treat it as prose and add structure deliberately**, the same way you would if you were transcribing directly from a printed page rather than an electronic file. BrailleBlaster's ability to read Word's internal structure is a shortcut when that structure is real — it isn't a substitute for reading the document.

> **Note:** If a .docx file behaves unpredictably on open — content missing, structure garbled beyond what fake-formatting alone would explain — it's sometimes faster to convert it to a plainer intermediate format (HTML, for instance, using Word's own "Save As") and reopen that, since a simpler format leaves less room for BrailleBlaster to misinterpret. This is the same idea used for stubborn LaTeX files (see Chapter 4's math workflow, and Chapter 17 on Pandoc).

### Worked Example

Bring two versions of the same short document into a training session: one built with genuine Word heading styles and list formatting, and a second, visually identical copy where every "heading" is just bolded, larger, centered text, and every "list" is manually indented with tabs and hyphens. Open both in BrailleBlaster and compare:

- In the first, headings and lists should map to the correct BrailleBlaster styles automatically, and Breadcrumbs will show real heading/list containers.
- In the second, everything should land as Body Text, with the bolding and indentation preserved as visual artifacts rather than structure — a vivid, hands-on demonstration of exactly the gap this chapter is about.

### Trainer Tips and Pitfalls

> **Trainer Tip:** This exercise — the same document, built two ways — is one of the most effective demonstrations in the entire curriculum, because it's the one place where "invisible structure" becomes visible through its consequences. Trainees who see it once rarely forget it.

A common pitfall for trainees moving fast: correcting the *visible* symptom (making a paragraph bold again after it lost its bolding) instead of the *structural* cause (applying the correct heading style, which then handles emphasis appropriately as part of that style). Keep steering trainees back to "what is this, structurally?" rather than "how do I make it look right again?"

### Key Takeaways

- BrailleBlaster reads the actual internal structure of .docx and .odt files, not just their visual appearance.
- A well-built source document (real headings, real lists, real character styles) transfers into BrailleBlaster with much of its layout already correct.
- A visually-formatted-but-structurally-flat document transfers in as largely undifferentiated Body Text, regardless of how correct it looks in Word.
- Diagnose before fixing: read the whole document, correct structure before emphasis, and use Find and Replace with Formatting to batch-correct repeated patterns.
- When a file behaves unpredictably, converting to a simpler intermediate format and reopening it can be faster than fighting the original.

### Practice Exercise

Ask trainees to take any short Word document they have on hand (or provide one deliberately built with fake structure) and produce a short written diagnosis before opening BrailleBlaster: which elements are they confident are real structure, which look suspicious, and what they'll check for once the file is open. Then have them open it, compare their prediction to what actually happened, and correct any mis-mapped elements.

## Chapter 6: Paper Size and Connecting to an Embosser

### Why It Matters

Every other skill in this manual produces a file on screen. This chapter is about turning that file into physical braille — or at least setting up the document so that it *can* be, correctly, the first time it reaches a real embosser. Getting page setup right before transcription begins saves enormous rework later, because page size, margins, and lines-per-page directly determine where BrailleBlaster places every page break in the finished document.

This chapter covers the basics every transcriber needs on day one: setting page properties and connecting a single embosser. Chapter 14 returns to embossing in more depth — multiple embosser profiles, advanced byte-level options, and troubleshooting a misbehaving device — once trainees have more context for why those advanced options exist.

### The Concept

BrailleBlaster separates page setup into a few related settings, all reached through the **Settings** menu:

- **Translation Settings** — which braille code the document uses (UEB, UEB with Nemeth, EBAE, and so on). Covered in earlier chapters as it relates to math; it's mentioned again here because it's set in the same dialog session as page setup, and agencies typically standardize all of these settings together.
- **Page Numbers** — where braille and print page numbers are placed, and how continuation is indicated. Covered fully in Chapter 13.
- **Page Properties** — physical page size, lines per page, cells per line, and margins. This is the heart of this chapter.

Under **Page Properties**, BrailleBlaster's defaults are a page size of 11.5" × 11", with margins of 0.5" top, 0.5" bottom, 1.25" left, and 0.48" right — sized for standard braille paper on a standard embosser. Margins can be expressed in inches, cells, or lines, whichever your agency's specifications use. The **Interpoint** setting determines whether the document embosses on both sides of the page (Yes) or one side only (No) — interpoint roughly doubles a document's page-for-page braille density but requires an embosser that supports double-sided embossing.

Once Translation Settings, Page Numbers, and Page Properties are set the way you want them, you can apply them just to the current document (**OK**) or save them as the default for every new document going forward (**Make Default**) — worth doing once an agency's house settings are established, so every new transcriber doesn't have to re-enter them by hand.

An **embosser** is the physical device that actually produces braille pages; BrailleBlaster needs a profile for whichever embosser it's connected to before it can send a file to be embossed, in much the same way a computer needs a printer driver.

### Step by Step: Basic Page Setup

1. Go to **Settings → Page Properties**.
2. Set **Page Size** to match your braille paper.
3. Set **Lines Per Page** and **Cells Per Line** — these, together with page size and margins, determine how much braille text fits on each page.
4. Set the four margins, choosing inches, cells, or lines as the unit.
5. Set **Interpoint** to Yes or No depending on your embosser and paper.
6. Click **OK** to apply to the current document, or **Make Default** to apply these settings to every future document as well.

### Step by Step: Connecting a First Embosser

1. Go to **Settings → Embosser Settings**.
2. Choose to add a new embosser profile.
3. In the Edit Embosser window, give the profile a **Name** you'll recognize later (useful once an agency has more than one embosser).
4. Choose the **Embosser Device** — the physical device as your computer sees it, from the dropdown of connected printers/embossers.
5. Choose the **Embosser Manufacturer**. If you don't know the manufacturer or the exact model isn't listed, choose **Generic**, and then the option that best matches the device: *Text only* (BrailleBlaster assumes the embosser itself already knows its page size, margins, and interpoint setting), *Text with margins* (BrailleBlaster adds the margin spacing itself, as extra characters in the braille stream), or *Graphics Embosser* (for embossers that support tactile graphics — currently the ViewPlus family, and still in beta).
6. Click **OK** to save the profile.

### Step by Step: Embossing a Document

1. Go to **File → Emboss** (`Ctrl+E`).
2. Choose the embosser profile, the number of copies, and the page range (All, or a specific range).
3. Click **OK** to send the job to the embosser, or **Cancel** to back out without embossing.

> **Note:** BrailleBlaster prints the *Print View* when you use **File → Print**, and embosses the *Braille View* when you use **File → Emboss** — these are two different output paths for two different audiences (a sighted proofreader vs. a braille reader), and it's easy for a new transcriber to reach for the wrong one when they mean "get this out of the computer."

### Worked Example

Before a trainee embosses anything for the first time, have them walk through the full chain deliberately: set Page Properties for the classroom's actual braille paper stock, create an embosser profile for the room's actual embosser (using Generic/Text with margins if the exact make and model isn't in the list), and then emboss a single short practice page — checking, physically, that the margins on the embossed sheet match what was set on screen.

### Trainer Tips and Pitfalls

> **Trainer Tip:** The distinction between Text only and Text with margins trips up more new transcribers than almost anything else in this chapter, because the visible symptom of getting it wrong — margins that are doubled, or missing entirely — looks like a translation problem rather than an embosser-profile problem. If margins look wrong on a physical embossed page but look correct in the Braille Preview, the embosser profile setting is the first thing to check, not the document's styles.

A frequent early mistake is reflexively clicking **Make Default** the first time page properties are set, before an agency's actual house standard has been confirmed — which then silently applies non-standard settings to every future document until someone notices. Encourage trainees to use **OK** (current document only) until settings are deliberately finalized.

### Key Takeaways

- Page setup lives in three related dialogs under **Settings**: Translation Settings, Page Numbers, and Page Properties.
- BrailleBlaster's page defaults (11.5" × 11" paper, 0.5"/0.5"/1.25"/0.48" margins) are a starting point, not a universal standard — confirm your agency's specifications.
- Interpoint controls single- vs. double-sided embossing.
- An embosser profile (Settings → Embosser Settings) is required before embossing; when the exact model isn't listed, Generic with Text only or Text with margins is the fallback.
- File → Print sends the Print View to a regular printer; File → Emboss (`Ctrl+E`) sends the Braille View to an embosser — these are not interchangeable.

### Practice Exercise

Have each trainee set up Page Properties for a specific, real braille paper stock provided in class, create an embosser profile for the training room's device, and emboss a one-paragraph test page. Ask them to physically measure the margins on the output with a ruler and compare against the settings they entered.

---

# Part II — Intermediate Tools: Math, Numbers, and Working Faster

Part II moves from "can I produce correct braille" to "can I produce it efficiently and handle material more complex than straightforward prose." The Spatial Math Editor and its number-line tools address the reality that a great deal of school mathematics is inherently two-dimensional on the page — long division, number lines, matrices — in a way that linear ASCII Math alone can't capture. Global Find and Replace addresses the reality that production transcription is rarely a single small document; it's often hundreds of pages where the same correction needs to happen consistently, every time.

## Chapter 7: The Spatial Math Editor

### Why It Matters

Not all mathematics is linear. A long-division problem, a number line, a matrix, or a worked equation template all depend on *position* — numbers stacked, aligned, or arranged in two dimensions — in ways that ASCII Math's left-to-right notation can't represent on its own. Print math and braille math handle this differently, but both still need to preserve the spatial relationships the reader depends on to actually follow the working, not just the final answer. The **Spatial Math Editor** is BrailleBlaster's purpose-built tool for this category of material, and it's significant enough that its underlying approach is the subject of a U.S. patent held by APH (Patent No. US 11,410,575 B2, "Interface and Tools for Accessible Textbook Generation").

### The Concept

The Spatial Math Editor is a separate editing window from the main Print View — spatial math cannot be edited directly in the Print View at all. Instead, you place the cursor at (or inside) the spatial math you want to create or change, open the Editor, make your changes there, and let BrailleBlaster re-insert the updated result back into the document.

The Editor organizes spatial math into four **Container Types**, each suited to a different kind of two-dimensional print structure:

- **Number Line Editor** — for number lines with labeled points, tick marks, and intervals. Covered in full in Chapter 8.
- **Matrix** — for grids of values enclosed in brackets, parentheses, or braces, up to 9 rows and 9 columns.
- **Math Templates** — for structured equation layouts (simple, fraction, and division templates) built from identifiers, operators, and operands, useful for things like long-division worksheets and worked-example templates with a visible solution.
- **Regular Text** — for building a general-purpose aligned grid out of any text, not necessarily mathematical, with configurable vertical and horizontal alignment.

Whichever container type you choose, a shared set of controls governs the shape of the structure: **Row** and **Column** controls (Previous/Next/Delete) let you add, remove, or navigate between rows and columns, and general **Settings** — which change based on container type and translation — let you apply Nemeth Passage Indicators, a Grade 1 Passage, or Numeric Passage Indicators inline, matching the surrounding document's translation.

### Step by Step

1. Place the cursor where the spatial math belongs (or inside existing spatial math you want to edit).
2. Go to **Math → Spatial Math Editor**.
3. Choose the **Container Type** that matches the print structure: Number Line Editor, Matrix, Math Templates, or Regular Text.
4. Use the container-specific settings to configure the structure. For a Matrix, for example: choose the **Translation** (Uncontracted, Direct, ASCII Math, or Literary), decide whether to **Add Ellipsis to Blank Cells**, choose a **Grouping Device** (bracket, parentheses, brace, or vertical bar — each also available in a "big" variant for larger structures), and set the **Wide Overflow Style** (Block and Blank Line, or Indent Columns) for matrices too large to fit on one braille page.
5. Use **Row**/**Column** Previous, Next, and Delete to build the structure to the correct dimensions.
6. Click **Insert** to place the finished spatial math into the document, or **Cancel** to discard the changes.

### Worked Example: A Math Template for Long Division

Long division is a natural first Spatial Math Editor exercise because it's instantly recognizable and makes the value of a spatial layout tool obvious even to trainees skeptical that "regular" ASCII Math wouldn't be enough:

1. Place the cursor where the problem belongs; open **Math → Spatial Math Editor**.
2. Choose **Math Templates** as the Container Type, then **Division Template** as the Template Type.
3. Set the number of **Operands** the problem requires.
4. If the exercise should show a worked solution rather than just the blank problem, set **Solution** to **True** and enter it; otherwise leave it **False** to produce a blank practice problem for the student to complete.
5. Click **Insert**, then compare the Braille View rendering against a Nemeth long-division reference to confirm the spatial layout translated as expected.

### Trainer Tips and Pitfalls

> **Trainer Tip:** Because the Spatial Math Editor is a separate window, trainees sometimes go looking for spatial math edits inside the ordinary Print View and conclude the tool is broken when nothing happens. Reinforce, early and often: place the cursor near the spatial math *first*, then open the Editor — the Editor reads what's under the cursor and lets you revise it there, not in the main document view.

A common pitfall with matrices specifically: not anticipating page-width overflow until the document is nearly finished. For matrices with many columns or long cell contents, check the **Wide Overflow Style** setting early, rather than discovering a matrix doesn't fit the braille page only at final proofing.

### Key Takeaways

- Spatial math (number lines, matrices, templates, and aligned grids) is built and edited in the separate Spatial Math Editor window, never directly in the Print View.
- Four Container Types cover the common cases: Number Line Editor, Matrix, Math Templates, and Regular Text.
- Matrices support up to 9×9 cells, a choice of grouping device, and two strategies for handling overflow onto multiple braille pages.
- Math Templates (Simple, Fraction, Division) are well suited to worksheet-style problems, including the option to show or hide a worked solution.

### Practice Exercise

Provide trainees with a printed page containing a 3×3 matrix and a two-operand long-division problem. Have them reproduce both using the Spatial Math Editor, then swap completed files with a partner to proofread each other's Braille View output against the original print page.

## Chapter 8: Spatial Number Lines

### Why It Matters

Number lines look simple and are anything but, once you start transcribing them. A print number line encodes information in position (where a point sits between labeled marks), in symbol (open vs. filled circles, arrows), and often in fraction form that print textbooks show in a "nice," pre-reduced way for pedagogical reasons. All of that has to survive translation into a linear braille format that a reader explores with their fingertip rather than their eye, moving left to right one cell at a time. This chapter builds directly on Chapter 7 — the Number Line Editor is one of the four container types inside the Spatial Math Editor — and deserves its own dedicated lesson because number lines show up constantly in early-grades math materials and have enough of their own settings to warrant close attention.

### The Concept

Inside the Spatial Math Editor, choosing **Number Line Editor** as the Container Type exposes a set of number-line-specific settings, all worth reviewing *before* entering the actual line-start, line-end, and interval values:

- **Reduce Fraction** — automatically reduces fractions along the line (so a line from 0 to 1 counted by quarters reads 0, ¼, ½, ¾, 1). Leave this off if the print original deliberately shows an unreduced, consistent denominator throughout (0, ¼, 2/4, ¾, 4/4) — some textbooks do this on purpose to reinforce equivalent fractions, and "fixing" it by reducing would misrepresent the lesson.
- **Beveled Fraction** — sets fraction lines to a beveled (diagonal) style; UEB uses the general fraction line, while Nemeth uses the diagonal line, so this setting should track the document's math translation table.
- **Add Arrows to Line** — places arrows at both ends of the line, matching a print number line that visually extends beyond its labeled range.
- **Stretch Across Page** — stretches the line to use the full width of the braille page; by default, BrailleBlaster instead uses the minimum number of cells needed to fit the line.
- **Remove Leading Zeros** — for number lines involving decimals, drops the leading zero (0.5 becomes .5), matching standard braille math convention.
- **Number Line View** — *Math Entry* builds a standard sequential number line from numeric values; *User Text* instead lets you type text labels for each tick mark (adding a **Line Marker** option, supporting up to 10 markers), useful for number lines labeled with words or non-numeric categories rather than pure numbers.
- **Interval/Points** — choose *Points* to mark individual points along the line, *Interval* to shade or mark a continuous segment of the line, or *None* to remove markup entirely, leaving a plain labeled line.
- **Start Interval Type** and **End Interval Type** — each independently set to *Empty Circle*, *Full Circle*, or *None*, matching the open/closed circle convention print math uses to show whether an endpoint is included in a range.

### Step by Step

1. Place the cursor where the number line belongs; open **Math → Spatial Math Editor**.
2. Choose **Number Line Editor** as the Container Type.
3. Review and set the settings above — Reduce Fraction, Beveled Fraction, Add Arrows to Line, Stretch Across Page, Remove Leading Zeros, and Number Line View — to match the print original *before* entering values, since several of these change how the values you're about to enter will be interpreted and displayed.
4. If you chose *Interval* under Interval/Points, also set Start Interval Type and End Interval Type to match the print circles.
5. Fill in the core values: **Count By** (the increment between labeled numbers), **Line Start**, **Line End**, and — if using an Interval — **Interval Start** and **Interval End**. BrailleBlaster calculates the full number line automatically once these are filled in with mathematically consistent values.
6. Click **Insert** to place the completed number line into the document.

### Worked Example

Reproduce a simple print number line: a line from 0 to 1, counted by quarters, with a shaded interval (filled circle) from ¼ to ¾:

1. Open the Spatial Math Editor, choose Number Line Editor.
2. Leave **Reduce Fraction** on (this line is meant to show reduced quarters, not an unreduced running denominator).
3. Set **Number Line View** to *Math Entry*.
4. Set **Interval/Points** to *Interval*; set both **Start Interval Type** and **End Interval Type** to *Full Circle*, matching a print line where both endpoints of the shaded segment are solid dots.
5. Set **Count By** to ¼, **Line Start** to 0, **Line End** to 1, **Interval Start** to ¼, and **Interval End** to ¾.
6. Click **Insert**, then compare the Braille View output against the print original, checking specifically that the fraction values, the arrows (if the print original has them), and the interval endpoints all match.

### Trainer Tips and Pitfalls

> **Trainer Tip:** Reduce Fraction is the setting most likely to produce a *technically working but pedagogically wrong* result — the braille will translate cleanly either way, but if the print lesson's entire point was showing unreduced equivalent fractions, silently reducing them changes what the material teaches. This is a good moment to remind trainees that transcription decisions can affect meaning even when nothing is "broken" in a technical sense.

A frequent early mistake is entering Line Start/Line End/Count By values that aren't mathematically consistent with each other (an increment that doesn't evenly divide the range), which can produce an unexpected or malformed line. If the number line doesn't come out as expected, re-check that the numbers entered actually describe a sensible sequence before assuming a tool problem.

### Key Takeaways

- Number lines are one of the four container types inside the Spatial Math Editor, with settings specific to fractions, arrows, page width, interval markers, and endpoint symbols.
- Set the descriptive options (Reduce Fraction, Beveled Fraction, Number Line View, and so on) before entering the numeric values, since they affect how those values are interpreted.
- BrailleBlaster calculates the full sequence of labeled points automatically from Count By, Line Start, and Line End — you don't type each label individually.
- Match Start/End Interval Type to the print original's open vs. filled circles to preserve the mathematical meaning of the interval, not just its visual appearance.

### Practice Exercise

Give trainees two print number lines to reproduce: one showing a deliberately unreduced sequence of fractions (to practice recognizing when Reduce Fraction should be turned off), and one using open circles at both ends of a shaded interval (to practice Start/End Interval Type). Have them explain, for each, which settings they chose and why.

## Chapter 9: Global Find and Replace with Formatting Options

### Why It Matters

A single-page worksheet can be corrected by eye. A three-hundred-page textbook cannot. Production transcription depends on being able to find — and, when appropriate, fix — every instance of a pattern across an entire document reliably, whether that pattern is a misspelled term, a formatting inconsistency inherited from a poorly-structured source file (Chapter 5), or a style that needs to change document-wide for consistency. BrailleBlaster's Find and Replace tool does this for both plain text *and* formatting, which is what makes it a genuinely global tool rather than a simple word-search box.

### The Concept

Find and Replace (**Edit → Find and Replace**, or `Ctrl+F`) starts as familiar text search-and-replace, with two refinements available on any search:

- **Match Case** — restricts results to the exact capitalization typed (searching "THE" with Match Case on finds only "THE," not "The" or "the"). Match Case works reliably with all-lowercase, all-uppercase, and initial-capital text, but not with camel-capped or irregularly-capitalized words.
- **Whole Word** — restricts results to the search text standing alone as a full word, so searching "the" with Whole Word on won't also match "theater," "them," or "bathe."

What makes the tool genuinely powerful for production work is the **Formatting** option, which extends both Find and Replace beyond plain text into three categories:

- **Styles** — the layout style applied to text (Heading 1, List, Body Text, and so on).
- **Containers** — enclosing structures like boxes or full-color boxes.
- **Text Attributes** — emphasis and translation settings (bold, italics, Direct translation, and so on).

On the Find side, each formatting category can be set to **Add** (only match text that *has* the selected formatting) or its inverse, the **Not** option (match text *unless* it has the selected formatting). For example, adding "Heading 1" under Add finds a search term only when it appears inside a Heading 1 — useful for correcting a term only where it functions as a heading, leaving the same word alone everywhere else in the body text. On the Replace side, Styles and Text Attributes can likewise be **Add**ed to matched text; a style can't be directly removed through Replace, but it can be replaced with a different one by specifying the target style you're searching for and the style you want it changed to.

Only one style (or one text attribute) can be added to the Find or Replace box at a time — building a search across multiple formatting conditions means running the tool in multiple targeted passes rather than one combined query.

### Step by Step: Basic Find and Replace

1. Go to **Edit → Find and Replace** (`Ctrl+F`).
2. Type the search text into **Find Text**.
3. Optionally check **Match Case** and/or **Whole Word** to narrow the search.
4. Type the replacement into **Replace With**.
5. Click **Find** to locate the next instance, then **Replace** to change that instance and advance to the next — or click **Replace All** to change every instance in the document at once, without stepping through them individually.
6. Click **Close** when finished.

### Step by Step: Finding and Replacing by Formatting

1. Open **Edit → Find and Replace** (`Ctrl+F`).
2. Click **Formatting** to expand the Find/Replace formatting panel.
3. Choose a category — Styles, Containers, or Text Attributes — and select the specific formatting you want.
4. Click **Add** to attach that formatting condition to the Find box (or, for Replace, the Replace box). Use **Reset** to clear a formatting condition you no longer want.
5. Click **Close Formatting** to return to the main Find and Replace window; the formatting condition now appears as text under the Find (and/or Replace) field.
6. Run **Find**, **Replace**, or **Replace All** as with a plain text search — the results are now filtered by the formatting condition as well as by any text entered.

> **Note:** Click **Reset** to clear all selected formatting conditions and checkboxes at once. The most recently searched text itself is preserved in the Find Text and Replace With fields even after a Reset, so you can re-scope a search without retyping the search term.

### Worked Example

Return to the poorly-formatted Word document scenario from Chapter 5, where every fake "heading" was built as bolded, centered, larger-font text rather than a real Heading style, and — after correction — those paragraphs are now properly styled as Heading 1, but many of them are still, individually, also carrying leftover Bold emphasis from the original file:

1. Open **Edit → Find and Replace**, click **Formatting**.
2. Under Styles, select **Heading 1** and click **Add** to the Find condition — leave Find Text blank, so this matches any text within a Heading 1, regardless of content.
3. Under Replace, add **Bold** removed... since Bold can't be directly removed through Replace, instead use the dedicated **Emphasis → Remove All Emphasis from Headings** tool covered in Chapter 1 for this specific case, and reserve Find and Replace with Formatting for cases where you're changing *which* style or attribute applies, not stripping one outright.
4. As a genuinely global-replace example instead: search for a term that was spelled two different ways throughout an inconsistent source document (for example, both "co-operate" and "cooperate"), with Match Case off, and use Replace All to standardize the spelling throughout — narrating out loud, for trainees, why Replace All is safe here (a real, unambiguous spelling correction) versus a case where individually reviewing each Replace would be safer (a term that has different correct meanings in different contexts).

### Trainer Tips and Pitfalls

> **Trainer Tip:** **Replace All** is fast and, used carelessly, is exactly how a document ends up with a batch error repeated fifty times instead of corrected once. Teach trainees to run **Find** first, scroll through a few results to confirm the pattern really is what they think it is, and only then use Replace or Replace All.

A common pitfall with formatting-based searches: forgetting that only one style or attribute can be added to a condition at a time, and expecting a combined "Heading 1 AND Bold" search to work as one query. Plan formatting corrections as a short sequence of single-condition passes instead.

### Key Takeaways

- Find and Replace (`Ctrl+F`) handles plain text search with optional Match Case and Whole Word narrowing.
- The Formatting panel extends search to Styles, Containers, and Text Attributes, with an Add/Not toggle on the Find side for precise, structure-aware corrections.
- Replace All is powerful and should be used only after confirming, via a plain Find pass, that every match really should be changed.
- Only one formatting condition can be active per Find or Replace box at a time; multi-condition corrections require sequential passes.

### Practice Exercise

Give trainees a document with a spelling inconsistency repeated at least five times, and a formatting inconsistency (for example, some but not all list-prefix numbers carrying leftover bold emphasis) affecting at least three elements. Have them correct the spelling with a plain Replace All, and the formatting inconsistency using Find and Replace with Formatting, documenting the exact search conditions they used for each.

---

# Part III — Files You'll Meet on the Job

Part III steps back from moment-to-moment editing to look at the file formats that structure a transcriber's whole workflow: the NIMAS files that arrive from textbook publishers, and the emerging eBraille format that is starting to change what "finished braille" even means. Understanding these formats — not just how to open them, but what they *are* and why they're built the way they are — is what separates someone who can operate BrailleBlaster from someone who understands the production pipeline it sits inside.

## Chapter 10: The eBraille Format

### Why It Matters

For decades, the end product of braille transcription has effectively been the **BRF** (Braille Ready File) — a format built around a fixed page: a specific number of cells per line, a specific number of lines per page, hard-coded for one particular embosser paper size. That's exactly what you want for embossing a physical book. It's a poor fit for a refreshable braille display, especially the new generation of multi-line displays, where the "page" isn't fixed at all — it's whatever the physical display happens to be able to show, which varies device to device and can even be resized by the reader. **eBraille** is the industry's answer to that mismatch, and it's worth understanding both because it's arriving in production tools like BrailleBlaster now, and because its origin story runs directly through BrailleBlaster itself.

### The Concept

eBraille is a digital braille reading format, standardized and maintained by the **DAISY Consortium**, with version 1.0 released in 2025. Structurally, it's built on an **EPUB 3-compatible file set** — meaning it uses XHTML documents, CSS, and the same general web technologies that power EPUB e-books — rather than being a flat, page-fixed text stream the way a BRF is. That single architectural choice is what gives eBraille its key advantage: **reflow**. Because the braille content is marked up with semantic tags rather than hard-coded into fixed lines and pages, an eBraille publication can adapt to whatever braille display it's opened on, rather than assuming one specific paper size and cell count.

The origin of eBraille traces directly back to BrailleBlaster's own approach to NIMAS files (see Chapter 11): when BrailleBlaster opens a tagged NIMAS XML file, it reads the publisher's tags and maps them onto the correct braille formatting. According to APH's own account of the project, eBraille essentially runs that same idea in reverse — instead of reading print tags and producing braille formatting, eBraille applies tags *to* braille formatting itself, so the resulting file remains meaningfully structured (this is a heading, this is a list, this is a footnote) rather than being a flat grid of cells. APH partnered with the DAISY Consortium to turn that idea into a full, vendor-neutral standard, and the working group has since grown to include more than forty organizations internationally.

A few practical points worth knowing:

- eBraille publications can be distributed as a packaged file, unzipped onto a local file system, or deployed to the web, and — because they share EPUB/web technology — can even be read directly in a standard web browser with appropriate screen reader or braille display support.
- Unlike a BRF, an eBraille publication is *not* transformed on the fly by the reading device; it comes already formatted according to the braille code rules of the region where it was produced, while still retaining the flexibility to reflow across different display widths.
- Major braille production and reading tools — Duxbury, BrailleBlaster, and Sao Mai Braille among them — have committed to supporting eBraille, alongside device support developing for displays such as APH's Monarch and several single-line refreshable displays.
- A BRF-to-eBRL converter is part of the surrounding tooling ecosystem, meaning existing BRF files don't have to be re-transcribed from scratch to gain some of eBraille's benefits — they can be converted forward.

### What This Means for a Transcriber Today

eBraille is genuinely new — version 1.0 only arrived in 2025 — so most working transcribers today are still primarily thinking in terms of BRF output and physical embossing. That's not going to stop being true any time soon; embossed, physical braille remains essential. But it's worth introducing this chapter conceptually even to trainees who won't touch an eBraille export in their first weeks, for two reasons: first, because the file formats a transcriber works with will keep evolving, and understanding *why* a format exists (what problem it was built to solve) makes the next one easier to learn than it would otherwise be; second, because the tag-based thinking behind eBraille is the same tag-based thinking behind NIMAS import (Chapter 11) — the two reinforce each other conceptually even though they sit at opposite ends of the production pipeline.

### Trainer Tips and Pitfalls

> **Trainer Tip:** This is a good chapter for a short discussion rather than a hands-on exercise, especially for a class of brand-new transcribers. Frame it as "here's where the field is heading and why," not "here's a tool you need to master today." Save the hands-on eBraille workflow for a later, dedicated session once BrailleBlaster's eBraille export tools are part of your agency's regular production process.

A pitfall worth naming explicitly: don't let trainees walk away thinking eBraille *replaces* BRF or embossed braille. It solves a different problem — reflowable digital reading on refreshable displays — and exists alongside, not instead of, page-fixed embossed output.

### Key Takeaways

- eBraille is a DAISY Consortium standard (version 1.0, 2025) for digital, reflowable braille reading, built on an EPUB 3-compatible, XHTML/CSS file set.
- Unlike a BRF, which assumes one fixed page size, eBraille content reflows to fit whatever braille display it's opened on.
- The format's core idea — applying structural tags to braille content — mirrors how BrailleBlaster already reads structural tags from NIMAS files, just running in the opposite direction.
- eBraille supplements, rather than replaces, BRF and physical embossing; production transcription workflows still depend heavily on both.

### Practice Exercise

Have trainees write a short (one-paragraph) explanation, in their own words, of the practical difference between a BRF file and an eBraille file, aimed at a colleague who has never heard of either. Discuss a few answers as a group and compare which explanations would actually make sense to someone outside the field.

## Chapter 11: Importing and Working with NIMAS/XML Files

### Why It Matters

**NIMAS** (the National Instructional Materials Accessibility Standard) is, for many production transcribers, the single most common source format they'll open — it's the XML-based format publishers submit to the National Instructional Materials Access Center (NIMAC) so that accessible formats, including braille, can be produced for K-12 students with qualifying print disabilities under IDEA 2004. BrailleBlaster was built from the start around taking advantage of NIMAS's rich markup, which is why NIMAS files typically arrive in BrailleBlaster far more pre-formatted than an average Word document (Chapter 5) — but "more pre-formatted" is not the same as "finished," and this chapter covers both the shortcuts NIMAS gives you and the manual review it still requires.

### The Concept

A NIMAS file tags its content richly: headings are marked as headings, lists as lists, tables as tables, and so on, at the markup level rather than just visually. When BrailleBlaster opens a NIMAS XML file (or a zipped NIMAS package), it reads those tags and automatically maps most of them onto the correct BrailleBlaster styles — print and braille page numbering, heading levels, list structures, and table identification chief among them. This is the payoff for NIMAS's structural rigor, and it's a major reason NIMAS import can be so much faster than starting from an unstructured file.

That automation is not, however, a substitute for review, for a specific and important reason: **NIMAS tags describe print structure, not braille formatting rules.** A heading tagged as bold throughout a print file, for instance, may come into BrailleBlaster still carrying that bold emphasis — technically correctly mapped as a heading, but with print-only formatting attached that braille conventions don't call for. Reviewing and correcting these mismatches between "correctly identified" and "correctly formatted for braille" is a core, expected part of working with NIMAS material, not a sign that the import failed.

If a NIMAS file contains **MathML** (the standard markup for mathematical content on the web), BrailleBlaster automatically converts it to ASCII Math and translates it into whichever braille math code the document's translation settings specify — the same math pipeline covered in Chapters 3 and 4, just triggered automatically by the source file's own markup instead of by a transcriber manually flagging text with `Ctrl+M`.

Two tools are specific to NIMAS files and worth knowing from the start:

- **Publisher's Production Notes** — many NIMAS files include notes from the publisher about how the material was originally intended to be produced; these are a useful reference while making braille-specific formatting decisions, and shouldn't be discarded without reading them.
- **The Book Tree** — the most useful navigation tool specifically for NIMAS files, giving a structural, outline-style view of the whole book (chapters, sections, and so on) rather than requiring page-by-page scrolling. For a long textbook, the Book Tree is usually faster than any other navigation method covered in earlier chapters.

For very large NIMAS textbooks, BrailleBlaster also supports **dividing a file into multiple pieces** along publisher-designated sections, so that several transcribers can work on different parts of the same book simultaneously; once each piece is finished, the separate files can be rejoined into one complete document ready to emboss. This only works for files with real publisher-designated sections (as NIMAS files typically have) — it isn't a general-purpose way to split any arbitrary document.

### Step by Step: Opening and Reviewing a NIMAS File

1. Go to **File → Open** (`Ctrl+O`) and select the NIMAS XML file, or the zipped NIMAS package.
2. Once open, use the **Book Tree** to get an overview of the book's structure before diving into detailed editing.
3. Check for and read any **Publisher's Production Notes** included in the file.
4. Review headings, lists, tables, and emphasis with Breadcrumbs turned on, watching specifically for print-only formatting (like bold headings) that came through technically correctly mapped but doesn't belong in the final braille.
5. If the file contains MathML, spot-check a few converted math elements in the Braille View to confirm the automatic ASCII Math conversion translated as expected, especially for anything mathematically unusual.
6. For a large textbook being split across multiple transcribers, use the file-dividing tools to break the book along its publisher-designated sections before assigning work.

### Worked Example

Open a sample NIMAS textbook chapter and, before making any changes, use the Book Tree to answer three questions out loud: How many major sections does this chapter have? Where are the practice problems relative to the main instructional text? Is there a glossary or notes section at the chapter's end? Only after mapping the chapter's shape this way should trainees begin detailed style review — this mirrors the "read before you fix" principle from Chapter 5, applied to a file type that offers a purpose-built tool (the Book Tree) for doing exactly that reading efficiently.

### Trainer Tips and Pitfalls

> **Trainer Tip:** New transcribers sometimes treat a NIMAS file's automatic formatting as fully trustworthy simply because it's structured markup rather than a "messy" Word document. Correct that assumption early: NIMAS gives you a much better *starting point* than an unstructured file, not a finished product. The review habits from Chapter 5 still apply — they're just applied to a smaller set of remaining issues.

A common pitfall: skipping the Publisher's Production Notes because they seem like optional reading. They frequently contain exactly the kind of context (how a particular recurring feature was intended to be handled) that prevents a transcriber from re-deriving a formatting decision from scratch, or getting it wrong.

### Key Takeaways

- NIMAS is an XML-based format publishers use to submit accessible-format-ready textbooks to NIMAC under IDEA 2004; it's the source format BrailleBlaster was originally built around.
- Rich NIMAS tagging lets BrailleBlaster automatically map most structural elements (headings, lists, tables, page numbers) onto the correct styles — but print-only formatting (like bold headings) can still come through attached to a correctly-identified element and needs manual review.
- MathML embedded in a NIMAS file is automatically converted to ASCII Math and translated into the document's braille math code.
- The Book Tree is the fastest way to get a structural overview of a NIMAS book; Publisher's Production Notes are a valuable, easily-overlooked source of context.
- Large NIMAS textbooks can be divided along publisher-designated sections for parallel work by multiple transcribers, then rejoined into one final file.

### Practice Exercise

Provide trainees with a short sample NIMAS chapter. Have them use the Book Tree to produce a written outline of its structure before opening the detailed Print View, then review the chapter for at least one instance of print-only formatting (such as bold carried over on a heading) that needs to be removed despite the heading itself being correctly identified.

---

# Part IV — Advanced Practice

Part IV is where a competent BrailleBlaster user becomes a production-ready transcriber. These chapters cover the file-format range a working transcriber actually meets (not just Word and NIMAS, but Markdown, OpenOffice, and LaTeX), the transcriber-specific bookkeeping tasks every finished document needs (running heads, page numbering), the full depth of embosser management, the less-common but essential formatting styles (boxed material, plays, poetry, deeply nested lists), and the Contraction Relaxer, a tool that gives fine control over exactly how contracted a document's braille is.

## Chapter 12: Importing from Markdown, OpenOffice, LaTeX, and XML

### Why It Matters

Chapter 5 covered Word and OpenDocument files, and Chapter 11 covered NIMAS XML — but BrailleBlaster's list of supported open formats is longer than either chapter suggests on its own: Markdown (.md), LaTeX (.tex), plain XHTML, EPUB, plain text, and BRF/BRL round out the list. Each of these arrives in a transcriber's inbox for a different reason, and each brings its own trade-offs worth understanding up front, rather than learning by surprise the first time a file behaves unexpectedly.

### The Concept: Why So Many Formats?

BrailleBlaster's broad import support exists because source material for transcription genuinely comes from everywhere: a classroom teacher's typed worksheet, a university's LaTeX-authored physics problem set, a self-published book exported from a word processor as OpenDocument, a born-digital document already written in Markdown. Rather than asking every source to be converted to one canonical format before it reaches BrailleBlaster, the program (using Pandoc under the hood for much of this — see Chapter 17) accepts a wide range directly and normalizes it internally.

**Markdown (.md)** files open directly in BrailleBlaster. Markdown's own structure — headings marked with `#`, lists marked with `-` or numbers, **bold** and *italic* marked with simple symbols — maps onto BrailleBlaster styles similarly to how a well-built Word document does (Chapter 5), generally with less ambiguity, because Markdown syntax is inherently structural rather than merely visual: a line starting with `#` cannot accidentally be "fake" the way a manually-bolded, larger-font paragraph in Word can. This is one of the reasons Markdown is a genuinely good source format for a transcriber to request, when the option exists, from an author who's willing to write in it.

**OpenDocument Text (.odt)** files, produced by OpenOffice, LibreOffice, and other open-source office suites, open the same way .docx files do (Chapter 5) and carry the same structural caveat: a well-built .odt file with real heading and list styles transfers cleanly; one with only visual formatting does not.

**LaTeX (.tex)** files receive special handling because LaTeX is fundamentally a typesetting language, not a word processor format — it describes *how to produce* a document rather than being the document's final structure in the way a NIMAS file is. When BrailleBlaster opens a LaTeX file, it maintains the original formatting and math without requiring LaTeX itself to be installed on the system. LaTeX math specifically converts directly into ASCII Math on import (with one notable exception: LaTeX embedded *inside* a NIMAS XML, plain text, BRL, or ZIP file is not auto-converted this way, since those formats have their own math-handling paths). Not every LaTeX package or notation is supported, though — some specialized packages or unusual commands may not translate correctly. When that happens, the recommended workaround is to convert the LaTeX file to HTML first using a dedicated tool such as **TeX4HT** (which integrates with a standard LaTeX compiler and produces strong LaTeX support as a result), and then open the resulting HTML file in BrailleBlaster instead of the original .tex file. One detail worth flagging explicitly to trainees: TeX4HT produces files with a **.xht** extension, which BrailleBlaster does not recognize directly — rename the extension to **.xhtml** before opening it.

**XML**, outside of the NIMAS-specific workflow covered in Chapter 11, generally refers to other XML-based markup a source document might use; BrailleBlaster's XML handling is built primarily around the NIMAS schema, so a non-NIMAS XML file may need to be converted to a more general format (HTML, for instance) before it opens cleanly.

### Step by Step: Choosing an Import Path

1. Identify the source file's actual format — not just its extension, but how it was produced. A `.docx` built in Google Docs, a `.docx` built in Microsoft Word, and a `.docx` built by exporting from a LaTeX tool can all behave differently on import even though they share an extension.
2. If the file is Markdown, LaTeX, or a well-structured .docx/.odt, open it directly (**File → Open**, `Ctrl+O`) and expect a reasonably faithful structural transfer, subject to the review habits from Chapter 5.
3. If the file is LaTeX and contains packages or notation BrailleBlaster doesn't support cleanly, convert to HTML with a tool like TeX4HT, rename any resulting `.xht` file to `.xhtml`, and open that instead.
4. If the file is a non-NIMAS XML format BrailleBlaster doesn't recognize, convert it to HTML or another supported format using an external tool before opening it in BrailleBlaster.
5. Regardless of source format, review the imported document's structure with Breadcrumbs before beginning detailed editing — the review discipline from Chapter 5 applies across every import path in this chapter, not just Word.

### Worked Example

If you have access to source material in more than one format — for instance, a short document available as both a `.docx` export and an original `.md` file — open both in BrailleBlaster and compare the results side by side. This is a genuinely instructive exercise: trainees can see directly how Markdown's explicit structural syntax tends to produce a cleaner, more predictable import than a word-processor file of uncertain internal construction, even when the two files look identical when read as plain text or viewed in a browser.

### Trainer Tips and Pitfalls

> **Trainer Tip:** If your agency has any influence over how source material is authored — commissioning custom worksheets from in-house staff, for instance — this chapter is worth revisiting from the *opposite* direction: which formats would make transcription faster and more reliable downstream? Markdown and well-structured LaTeX are often better authoring targets than a word processor document, precisely because their structure can't drift into "looks right but isn't" the way visual word-processor formatting can.

A common pitfall specific to LaTeX: assuming that because *some* LaTeX opened perfectly last time, *all* LaTeX will. LaTeX's flexibility (custom packages, macros, unusual notation) means import fidelity varies file to file far more than it does for the other formats in this chapter. Build the TeX4HT fallback into the standard workflow rather than treating it as a rare exception.

### Key Takeaways

- BrailleBlaster opens Markdown, OpenDocument, LaTeX, plain text, HTML/XHTML, EPUB, and NIMAS XML directly, in addition to Word — each format arrives via a different real-world workflow.
- Markdown's explicit structural syntax tends to import more predictably than word-processor formatting, for the same reason a well-built Word document outperforms a fake-structured one (Chapter 5).
- LaTeX files retain their formatting and math on import without requiring LaTeX to be installed, but unsupported packages or notation may require converting to HTML (via TeX4HT or similar) first — and renaming the resulting `.xht` file to `.xhtml`.
- Non-NIMAS XML generally needs conversion to a more general format before it opens cleanly, since BrailleBlaster's XML support centers on the NIMAS schema.

### Practice Exercise

Have trainees take one short document and produce it in two different source formats they have access to (for example, saved as both .docx and exported/copied as Markdown). Have them open both in BrailleBlaster, compare the resulting structure using Breadcrumbs, and write a short note on which format required more manual correction and why.

## Chapter 13: Transcriber Tasks — Running Heads and Page Numbering

### Why It Matters

Every finished braille volume needs to tell its reader where they are — which print page this braille page corresponds to, which braille page they're on, and, for a multi-volume or sectioned work, enough context to navigate confidently without sight. Page numbering is not a cosmetic finishing touch; it's core to how a braille reader locates material, matches a braille page back to a print page a sighted teacher or parent is looking at, and cites specific pages in discussion or homework. Because print and braille pagination essentially never line up one-to-one (braille takes more physical space per unit of text), BrailleBlaster tracks print and braille page numbers as two related but independent systems, and this chapter is about managing both correctly — along with the running head that helps orient a reader at the top of every page.

Given how much of a finished, professional transcription's quality shows up specifically in correct, consistent pagination, this chapter runs longer and deeper than most others in this manual — deliberately so.

### The Concept: Two Kinds of Page Number

BrailleBlaster tracks two numbering systems simultaneously:

- **Print page numbers** track where a given point in the braille document falls relative to the *original print source's* pagination — essential for a reader or teacher cross-referencing between a braille copy and a print copy of the same book.
- **Braille page numbers** track the actual sequence of physical braille pages in the finished volume — the numbers the reader uses to navigate the braille document itself.

Both are configured, at the document-default level, under **Settings → Page Numbers**, where you set the placement of each (top-left, top-right, bottom-left, bottom-right, or none), independently for even and odd pages, matching whatever your agency's house specification requires — the defaults are top-right for both even and odd print page numbers, and bottom-right for both even and odd braille page numbers.

**Braille page number types.** A braille page number isn't always a plain sequential number. BrailleBlaster supports three types, switchable at any point in the document via the Page Number Dialog:

- **Normal** — an ordinary sequential braille page number.
- **T-page** — braille page numbers beginning with the letter "t," used for transcriber-generated front matter (a title page, a transcriber's notes page) that precedes the volume's actual page-1 content.
- **P-page** — braille page numbers beginning with the letter "p," used for other preliminary material.

Once a page number type is set, every subsequent braille page continues using that type until you explicitly change it again — so a document typically starts in T-pages for transcriber front matter, switches to Normal at the point where the actual content (braille page 1) begins, and only returns to another type if the material calls for it (P-pages for a preface, for instance).

**Print page runovers.** Because a single print page's worth of text often spans more than one braille page, BrailleBlaster needs a way to mark the continuation. It uses a **continuation letter** system — "5," then "b5" for the next braille page still covering print page 5's content, then "c5," and so on — and this letter can be edited directly if your agency has specific requirements (for instance, for numbering blank pages a particular way).

### Step by Step: Adding a Running Head

The **Running Head** is text that appears at the top of every braille page in the document except the very first transcriber page (t1) and braille page 1 — it doesn't need to introduce itself on the page a reader lands on first, but it helps orient them on every page after that.

1. Go to **Insert → Running Head**.
2. In the small window that opens, **No Running Head** is selected by default (many short transcriptions don't need one at all). Select **Enter Title** instead, and type the running head text.
3. Click **OK** to save.

> **Note:** Before finalizing a running head, confirm its length actually fits at the top of the braille page alongside the print page number for *every* print page number the document will use — including the longest ones — as required by *Braille Formats 2016*. A running head that fits comfortably next to "5" may not fit next to "247" or a hyphenated combined page number; check the longest cases, not just the first one.

### Step by Step: Adding Page Numbers

**Adding a print page number:**

1. Type the print page number into the document at the point where the print page break occurs.
2. Highlight that number and go to **Styles → Miscellaneous → Page**, or use the corresponding Styles toolbar button.
3. If the number falls in the middle of a braille page (as it usually will, since braille and print pagination rarely align), a page-change indicator appears across the page automatically, with the print page number placed at the right margin.

**Adding a page-change indicator with no print page number** (for material with no visible print page numbers, where the page break itself is still worth marking):

1. Place the cursor before the point where the page changed.
2. Go to **Insert → Blank Print Page Indicator**.

**Adding braille page numbers:** Braille page numbers are generated automatically as you work — you generally don't add them by hand. To force an additional braille page break where BrailleBlaster wouldn't otherwise put one (to keep material together, or to match a required layout), place the cursor and use **Edit → Page Break** (`Ctrl+Enter`); the break is inserted after the cursor, pushing everything following it onto the next braille page. Note that there must be text after the cursor for Page Break to work.

### Step by Step: Editing Page Numbers

All page-number editing happens through one central dialog: place the cursor anywhere on the page you want to change, then go to **Edit → Edit Page Number** (or right-click and choose it from the context menu) to open the **Page Number Dialog**. From there:

- **Print Page Indicator tab** — change a previously-entered print page number. If you enter a hyphen to represent a combined range (for a print page numbered as a span, for instance), the **Runover Page Numbers** options become available: **Combined** displays runovers as a hyphenated combination of both numbers, while **Implied** displays only the second number.
- **Print Page Number tab** — change either the **Continuation Letter** (all following runovers of that print page automatically update to match) or the specific **Page Number** for just that one instance, without affecting the surrounding sequence. Numbers here are entered in ASCII.
- **Braille Page Number tab** — set the braille page number directly for the current page, and choose whether that page carries the document's Running Head (Yes/No).
- **Page Number Type tab** — switch between Normal, T-page, and P-page for the current page onward, as described above.

### Step by Step: Deleting Page Numbers

**Deleting a print page indicator** removes the print page number and all its continuation indicators, while leaving the affected pages in the document (they simply carry no print page number afterward; all other print page numbers in the document are unaffected): in the Page Number Dialog's Print Page Indicator tab, click **Delete Indicator**, then **OK**.

**Deleting a specific print page** removes just that one print page number and continuation letter — the following braille page absorbs it. For example, deleting print page "c5" removes it, and the next braille page, previously "d5," becomes the new "c5." Use the Print Page Number tab's **Delete Page** button, then **OK**.

**Deleting a braille page number** isn't a direct dialog action — delete the text (or blank space) occupying that page instead. To change *where* braille page numbers appear on the page (or to remove them from the document layout entirely), use **Settings → Page Numbers**, the same document-default dialog covered above.

### Reviewing Your Work: The Page Change List

Every manual page-number change you make is logged in the Page Number Dialog's **Page Change List** tab — a running audit trail of every edit, each with a **Go To** button that jumps straight to that page. Before finalizing a document, review this list as a matter of course: it's the fastest way to confirm every manual page-number intervention was intentional, and to catch a stray change that doesn't belong. Unwanted entries can be checked and removed with the **Delete** button at the bottom of the list.

### Worked Example

Set up a short practice document end to end:

1. Add a **Running Head** reading the (short) title of the practice document.
2. Type a two-page print excerpt where the print page break falls mid-way through a braille page — mark the print page number using **Styles → Miscellaneous → Page**, and confirm the page-change indicator appears correctly.
3. Insert a title page and a one-paragraph transcriber's note *before* the main content, and set their braille page number type to **T-page** via the Page Number Dialog; confirm the main content itself begins as **Normal**, braille page 1.
4. Open the **Page Change List** and confirm every manual change made during the exercise is accounted for and intentional.

### Trainer Tips and Pitfalls

> **Trainer Tip:** Page numbering is one of the few areas where getting the *concept* right (print vs. braille pagination as two independent tracks) matters more than memorizing every dialog tab. Spend real time up front making sure trainees can explain, in their own words, why a print page 5 might correspond to braille pages "5," "b5," and "c5" — once that clicks, the individual dialog tabs are mostly just "where do I make this specific change," which is easy to look up.

A frequent pitfall: setting a running head without checking it against the longest print page number the document will actually use, only to find it doesn't fit once a three-digit page number appears later in the book. Check the extremes, not just the first page, before finalizing.

Another common mistake: forgetting to switch the page number type back to **Normal** at the actual start of content after using T-pages or P-pages for front matter — leaving the whole document numbered as transcriber pages.

### Key Takeaways

- BrailleBlaster tracks print page numbers and braille page numbers as two independent, related systems; a single print page routinely spans multiple braille pages via a lettered continuation sequence (5, b5, c5...).
- Running Head placement, and default print/braille page number placement, are both set under **Settings → Page Numbers**; the Running Head itself is added via **Insert → Running Head**.
- Braille pages can be typed as Normal, T-page (transcriber front matter), or P-page (other preliminary material) via the Page Number Dialog's Page Number Type tab, and a type persists until explicitly changed again.
- All page-number edits — print or braille — flow through **Edit → Edit Page Number**, and every manual change is logged in the Page Change List for later review.
- Check a running head's fit against the longest page number the document will use, not just the first one.

### Practice Exercise

Have trainees build a short practice volume containing: a T-page title page, a T-page transcriber's note, a Normal-numbered main body spanning at least two print pages (with at least one print page runover), and a running head. Ask them to review the finished document's Page Change List and write a one-sentence justification for each entry.

## Chapter 14: Setting Up and Managing Embossers

### Why It Matters

Chapter 6 covered the basics of connecting a single embosser well enough to emboss a test page. Production environments are rarely that simple: an agency may run several embossers side by side (a fast text-only model for drafts, a higher-quality interpoint model for finished volumes, a graphics-capable model for tactile diagrams), and any embosser, well-configured or not, can occasionally behave unpredictably in ways that have nothing to do with the document itself. This chapter goes deeper into embosser profiles, the advanced options that exist specifically to work around device quirks, and a structured approach to troubleshooting when embossed output doesn't match what the screen shows.

### The Concept: Profiles, Manufacturers, and Models

Every embosser BrailleBlaster can send a job to needs its own **profile**, managed under **Settings → Embosser Settings**. A profile bundles together: a **Name** you assign, the **Embosser Device** as your computer's operating system sees it, and the **Embosser Manufacturer** and **Model**, which together tell BrailleBlaster exactly how to format the outgoing braille stream for that specific hardware.

BrailleBlaster ships with built-in support for a substantial list of manufacturers and models, including APH's own PixBlaster and PageBlaster, ViewPlus Technologies' full line (EmBraille, Columbia, Delta, Premier, Elite, Emprint, SpotDot, Max, Cub, and Cub JR), IRIE devices, Index Braille's Basic-D, Everest-D, BrailleBox, and Fanfold lines, the extensive Enabling Technologies catalog (Phoenix, Cyclone, Trident, BookMaker, the Romeo and Juliet families, and more), and Braillo's 200/400/600/270 series. If your exact model isn't listed, or you're not sure which manufacturer entry matches your device, **Generic** is the recommended fallback, with three sub-options:

- **Text only** — for devices not covered by a specific driver; BrailleBlaster assumes page size, margins, and interpoint have already been configured on the embosser itself.
- **Text with margins** — the same idea, except BrailleBlaster adds the margin spacing itself as extra characters within the braille stream, rather than relying on the embosser's own settings.
- **Graphics Embosser** — for devices that support embossing tactile graphics alongside braille text; currently in beta, and currently supported specifically by the ViewPlus embosser family.

### Advanced Embosser Options

For the Generic **Text only** and **Text with margins** profiles specifically, an **Advanced** tab exposes low-level options that exist to work around quirks in how a particular device expects to receive data. These normally stay at their defaults, and are the kind of setting you'd typically only touch at the direction of technical support once a specific embosser problem has been diagnosed:

| Option                 | What It Controls                                                       |
| ---------------------- | ---------------------------------------------------------------------- |
| Add margins            | Whether margin spacing is added by BrailleBlaster (true/false)         |
| Pad page               | Whether the page is padded out (true/false)                            |
| Form feed on full page | Whether a form-feed character is sent when a page is full (true/false) |
| End of line            | The exact byte sequence sent at the end of each line                   |
| End of page            | The exact byte sequence sent at the end of each page                   |
| Header                 | A byte sequence sent before the document                               |
| Footer                 | A byte sequence sent after the document                                |

The byte-string fields (End of line, End of page, Header, Footer) accept most ASCII characters typed directly, plus a small set of escape sequences for characters that are awkward to type directly: `\\` for a literal backslash, `\r` for carriage return, `\n` for new line, `\t` for tab, `\f` for form feed, and `\x` followed by two hexadecimal digits for any arbitrary byte (`\x1b`, for instance, sends the byte commonly known as Escape).

### Step by Step: Managing Multiple Embosser Profiles

1. Go to **Settings → Embosser Settings** to see every profile currently configured.
2. To add a new profile, follow the same steps as Chapter 6: Name, Embosser Device, Manufacturer, and Model.
3. To switch which embosser a document goes to, choose the appropriate profile at emboss time — **File → Emboss** (`Ctrl+E`) presents a profile selector alongside copy count and page range, and profiles can also be managed on the fly from within that dialog via its **Manage Embossers** button.
4. Keep profile **Names** specific enough that a busy production floor with several embossers won't confuse them — including the physical location or purpose of the device in the name (for example, "Room 2 — Index Everest — Drafts") avoids a wrong-profile emboss.

### Troubleshooting Embosser Issues

When embossed output doesn't match expectations, work through the problem in this order, rather than guessing at random settings:

1. **Confirm the embosser configuration is actually correct.** Re-check the Manufacturer and Model selected in the profile against the physical device — it's a common mistake to select a visually similar but incorrect model from a long dropdown list.
2. **Try Generic Text Only support** as a diagnostic step. If a model-specific driver is producing bad output, temporarily switching the profile to Generic Text Only (with the embosser's own onboard settings governing page size, margins, and interpoint) isolates whether the problem is in BrailleBlaster's model-specific driver or somewhere else in the chain (cabling, the embosser's own settings, or the document itself).
3. **Tweak the Advanced embosser options** only after the first two steps haven't resolved the issue, and ideally with guidance from support or from documented values for your specific model — certain embosser families (Enabling Technologies devices and Index Braille devices among them) have documented recommended Advanced-option values for known compatibility quirks.

> **Trainer Tip:** Frame Advanced embosser options explicitly as a *last resort*, not a first stop. New transcribers troubleshooting a bad emboss sometimes head straight for Advanced options because they look like "the technical settings," when the actual problem is far more often a wrong Manufacturer/Model selection or a physical connection issue. Teach the diagnostic order above as a habit, not just a reference list.

### Worked Example

As a training-room exercise, deliberately misconfigure a profile (select an incorrect but similar-sounding model for the room's actual embosser) and have trainees emboss a short test page. Ask them to describe what went wrong on the physical page, then walk them through the troubleshooting order above to correctly diagnose and fix the profile — reinforcing that a bad emboss is data to be interpreted, not just a problem to route to someone else.

### Key Takeaways

- Each embosser needs its own profile under **Settings → Embosser Settings**, specifying Name, Device, Manufacturer, and Model.
- Generic (Text only, Text with margins, or Graphics Embosser) is the correct fallback when a specific model isn't listed or isn't known.
- Advanced embosser options (available for Generic profiles) control low-level byte-string behavior and should be treated as a last-resort troubleshooting tool, not a routine setting.
- When embossed output looks wrong, check the Manufacturer/Model selection first, try Generic Text Only as a diagnostic isolation step second, and only then consider Advanced options.

### Practice Exercise

Have trainees configure profiles for two different (real or simulated) embosser models, name them clearly enough to avoid confusion, and then walk a partner through the full troubleshooting sequence using a deliberately misconfigured third profile, narrating each diagnostic step out loud.

## Chapter 15: Advanced Formatting — Boxed Material, Plays, Poems, and Deep Lists

### Why It Matters

Most transcription work lives comfortably in body text, headings, and simple lists — the styles covered in Chapter 2. But sooner or later, every transcriber meets print material that doesn't fit those shapes: a sidebar set off in a box, a script with character names and stage directions, a poem where line breaks are meaningful, or an outline nested more deeply than a simple bulleted list. BrailleBlaster has dedicated styles for exactly these cases, each following its own section of *Braille Formats 2016*, and this chapter is a tour of the ones a transcriber meets often enough to need working familiarity with, beyond the basics.

### Boxed Material

Print material set apart visually — a sidebar, a highlighted definition, a "did you know" call-out — needs to be set apart in braille too, so the reader knows it's a digression from the main flow rather than a continuation of it. BrailleBlaster's **Box** and **Full Box** styles serve this purpose; like List and Poetry, they behave as *containers* (Chapter 2), meaning Breadcrumbs marks them with the CONTAINER label and **Unwrap Element** can remove the box styling in one step, returning the contents to Body Text if the box treatment turns out not to be needed. Boxed material has its own options table (covered in the Style Appendix in BrailleBlaster's built-in Help) governing exactly how the box border and internal spacing render in braille — worth reviewing directly in Help the first time you apply it to unfamiliar material, since exact box conventions vary by what the box actually contains.

### Plays

Scripted material — a play, a scripted dialogue exercise — has its own **Play** styles, built to handle the specific, repeating structure of a script: character names, spoken lines, and stage directions, each of which needs to be visually and structurally distinct in the finished braille so a reader can follow who's speaking and when action (rather than speech) is being described. As with other specialized style families, the exact margin and spacing specification for Play styles is detailed in the Style Appendix, and is worth a direct look before transcribing a script for the first time — the specific margin pairs matter for readability in a way that's hard to intuit from general principles alone.

### Poetry

Poetry is transcribed using the **Poetic Stanza** style, one of BrailleBlaster's container styles. Unlike prose, where a line break is just where the text happened to wrap, a line break in a poem is meaningful — it's part of the author's craft — and Poetic Stanza preserves that meaningful line structure rather than letting BrailleBlaster's normal line-wrapping behavior take over. This is also the style to use, instead of Prose, when adding **Line Numbers** to poetry (Chapter 2's tools apply here directly: wrap the material in Poetic Stanza rather than Prose before running the Line Number tools, exactly as flagged back in the introduction to that feature).

### List Levels Beyond the Basics

Chapter 2 introduced the List style as a container and covered the everyday case: a simple bulleted or numbered list at one or two levels of nesting. Real outline-heavy material — a deeply nested table of contents, a legal or technical document with many sub-levels — can go well beyond that. BrailleBlaster's List style palette actually extends much further than the handful of levels visible by default: transcribers working with genuinely deep outlines will find list levels well beyond the basic five, with BrailleBlaster's built-in list styles reaching up into double-digit levels (agencies doing heavy outline work will encounter list-level margin pairs as high as, for example, level 11 pairings) for exactly this kind of deeply structured material. As with Style Levels generally (Chapter 2's **Styles → Configure → Style Levels**, adjustable up to eight visible at once), it's worth deliberately increasing the visible level count *before* starting a deeply-nested document, rather than discovering partway through that the level you need isn't showing in the toolbar yet.

> **Trainer Tip:** Deep lists are a good moment to revisit the "Reduce Fraction"-style lesson from Chapter 8: just because BrailleBlaster *can* represent eleven levels of nesting doesn't mean every source document's apparent nesting is meaningful at that depth. Encourage trainees to sanity-check unusually deep outline structure against the actual print original before reproducing every visual indent level as a distinct braille list level — a print document's visual indentation sometimes reflects word-processor formatting habits rather than a genuinely eleven-deep logical structure.

### Step by Step: Applying a Specialized Style

The mechanical steps are the same as any other style application (Chapter 2), which is worth pointing out explicitly to trainees who might expect boxed material, plays, and poetry to require a fundamentally different workflow:

1. Highlight the text (a full box's contents, a script's lines, a poem's stanza).
2. Go to **Styles** and select the appropriate style — Box/Full Box, the relevant Play style, or Poetic Stanza — or use the corresponding toolbar button.
3. Check Breadcrumbs to confirm the CONTAINER wrapping applied correctly around the full intended extent of the material — a box or stanza that only wraps part of its intended contents is a common and easy-to-miss error.
4. Consult the Style Appendix (**Help**) for the specific margin and spacing specification of the style in question if the result doesn't look right, rather than guessing at manual adjustments.

### Worked Example

Take a one-page excerpt containing a short boxed "fun fact" sidebar, four lines of a two-character script exchange, and a four-line poem stanza. Apply Box (or Full Box, depending on the sidebar's exact print treatment), the appropriate Play styles for the character names and dialogue lines, and Poetic Stanza for the poem, in that order. After each one, check Breadcrumbs to confirm the container wraps exactly the intended text — no more, no less — before moving to the next element.

### Key Takeaways

- Box and Full Box set visually-distinct print material (sidebars, call-outs) apart in braille as their own container style.
- Play styles handle the specific repeating structure of scripts — character names, dialogue, and stage directions — as their own distinct elements.
- Poetic Stanza preserves meaningful line breaks in poetry, and is the correct container to use (instead of Prose) when applying Line Numbers to poetry.
- BrailleBlaster's List styles extend well beyond the handful of levels shown by default, supporting genuinely deep outline structures — but deep visual indentation in a source document doesn't automatically mean deep logical nesting is warranted in the braille.
- Applying any specialized style follows the same basic workflow as Chapter 2's styles; consult the built-in Style Appendix for the specific margin rules of a style you're using for the first time.

### Practice Exercise

Provide trainees a one-page excerpt combining a boxed sidebar, a short two-character script exchange, and a short poem. Have them apply the correct style to each, verify each container's extent using Breadcrumbs, and look up the specific margin specification for one of the three styles in the built-in Style Appendix, reporting back what they found.

## Chapter 16: The Contraction Relaxer

### Why It Matters

Standard literary braille (Unified English Braille, Grade 2) uses contractions extensively — single cells or short cell combinations standing in for common letter groups and whole words, which is what makes contracted braille meaningfully more compact than an uncontracted, letter-for-letter transcription. Most of the time, an agency's translation table setting handles this globally and correctly, with no per-document intervention needed. But contractions can occasionally cause real problems for a specific reader or a specific kind of material — an emerging reader still learning contractions, unfamiliar technical vocabulary where contraction boundaries could be confusing, or specific words where the contracted form happens to be more ambiguous than useful. The **Contraction Relaxer** exists for exactly this situation: finer control than an all-or-nothing switch between contracted and uncontracted braille.

### The Concept

BrailleBlaster already offers two blunter tools that touch on this same territory, and it's worth being clear about how the Contraction Relaxer differs from both:

- **Uncontracted translation profiles** (Chapter 3's translation settings, and the Uncontracted option covered in Chapter 1's translation tools) turn *all* contractions off, document-wide, producing Grade 1 braille throughout.
- **Uncontracted Translation** applied to a specific selection (`Ctrl+Shift+T`, covered under Modifying the Braille Translation) turns contractions off for just that selection, but still treats it as all-or-nothing within that selection — every contraction that would normally apply there is suppressed.

The **Contraction Relaxer**, found under **Tools**, sits between these two: rather than a binary contracted/uncontracted choice, it gives you control over *which specific contractions* are permitted, so a document can remain contracted braille overall while selectively suppressing individual contractions that are causing a specific problem — for a specific reader, a specific vocabulary, or a specific pedagogical moment (a beginning reader who has learned some contractions but not others, for instance, benefits from braille that uses only the contractions they've already been taught, while remaining otherwise standard contracted braille rather than dropping to full Grade 1).

### Step by Step

1. Go to **Tools → Contraction Relaxer**.
2. Review the available contractions and select which ones should be suppressed (relaxed) for this document, based on the specific need driving the request — a reader's current contraction curriculum, a term whose contracted form is causing confusion, or a similar targeted reason.
3. Apply the changes and review the affected text in the Braille View to confirm the intended contractions are now suppressed while the rest of the document's contracted braille is unaffected.

> **Note:** Because the Contraction Relaxer changes translation behavior at a fairly fundamental level, treat any relaxer configuration as a deliberate, documented decision for a specific document or reader — not a setting to reach for casually. If your agency serves multiple readers with different contraction-learning stages, a documented, per-reader relaxer profile (what's relaxed, and why) is worth maintaining alongside the file itself, so a future transcriber picking up the same reader's material later understands the reasoning rather than just inheriting an unexplained configuration.

### Worked Example

A useful, low-stakes way to introduce this tool: take a short passage of standard contracted braille and deliberately relax a single, common contraction (one used often enough in the passage that its effect is obvious). Compare the Braille View before and after, and count how many individual cells the passage now uses compared to fully-contracted output — this makes the trade-off tangible: relaxing even one contraction has a real, measurable cost in braille length, which is worth weighing consciously against the specific benefit for the specific reader.

### Trainer Tips and Pitfalls

> **Trainer Tip:** This is a good moment to connect back to Chapter 1's closing point about judgment: the Contraction Relaxer is a tool for making a considered accommodation, not a way to sidestep learning standard contracted braille conventions. Frame it explicitly in terms of *who* the relaxed contractions are serving and *why*, every time it's used.

A common misunderstanding is treating the Contraction Relaxer as equivalent to switching a document to an uncontracted translation profile. They produce different results and serve different purposes — reach for a full uncontracted profile when the entire document should be Grade 1 throughout, and reach for the Contraction Relaxer when only specific contractions, for a specific reason, need to be suppressed while the rest of the document remains fully contracted.

### Key Takeaways

- The Contraction Relaxer (**Tools → Contraction Relaxer**) allows selective suppression of individual contractions, distinct from both a document-wide uncontracted translation profile and a selection-level Uncontracted Translation toggle.
- It exists for targeted situations — a reader's current contraction-learning stage, or a specific term where contraction is causing confusion — not as a general-purpose formatting choice.
- Relaxing contractions increases the braille length of the affected text; that trade-off should be a conscious decision, not an incidental side effect.
- Document why a relaxer configuration was used, especially in agencies serving readers at different contraction-learning stages, so the reasoning survives being handed off to another transcriber later.

### Practice Exercise

Give trainees a paragraph of standard contracted braille output and ask them to identify, in the Braille View, every instance of one specific common contraction. Have them relax that single contraction using the Contraction Relaxer, compare the before-and-after cell counts, and write one sentence describing a realistic scenario where that specific trade-off would be worth making.

---

# Part V — Finally

## Chapter 17: What Pandoc Does for BrailleBlaster

### Why It Matters

Throughout this manual — Word and OpenDocument import (Chapter 5), LaTeX handling (Chapter 12), even the general idea of a broad, forgiving range of supported file formats — one piece of infrastructure keeps showing up without being named directly: **Pandoc**, a widely-used, open-source document-conversion tool. BrailleBlaster leans on Pandoc-supported formats for a meaningful share of its import capability, and understanding roughly what Pandoc is and does — without needing to become a command-line expert — gives a transcriber a genuinely useful mental model for *why* some files import cleanly and others don't, and *what's actually possible* when a file doesn't open the way you'd expect.

This chapter is intentionally the last in the manual, and intentionally light on hands-on exercises. It's meant as a capstone: a look under the hood, for trainees who are ready for it, rather than a tool a transcriber needs to operate directly on day one.

### The Concept

Pandoc describes itself as a universal document converter — it can read a long list of markup and document formats and convert between almost any of them: Word, OpenDocument, Markdown, LaTeX, HTML, EPUB, and many more, all through one shared internal representation of "what a document is structurally" (headings, lists, emphasis, tables, and so on), rather than needing a separate, bespoke converter for every possible pair of formats.

BrailleBlaster's own documentation makes the connection explicit for at least one major case: LaTeX and other document types that Pandoc supports are described as supported by BrailleBlaster specifically *because* of this relationship. In practice, this means that when BrailleBlaster opens a LaTeX file, a Markdown file, or certain other formats and preserves their structure well, a meaningful part of that capability is Pandoc doing the underlying conversion work, with BrailleBlaster then mapping the resulting structure onto its own styles — the same styles covered throughout this manual, regardless of which source format the document originally came from.

This matters practically in two ways:

1. **It explains the "convert to HTML first" workaround** that appears more than once elsewhere in this manual (Chapters 4 and 12, for unsupported LaTeX packages and notation). HTML is one of the most reliably well-supported formats across the whole Pandoc-adjacent ecosystem, which is exactly why it's the recommended fallback target when a more exotic source format isn't translating cleanly — you're routing around a specific format's edge cases by converting to a format with broader, more predictable support.
2. **It explains why file-format breadth and file-format depth are different things.** BrailleBlaster can *open* an unusually wide range of formats precisely because it doesn't have to implement bespoke support for every one individually — but how *well* a given file converts still depends on how cleanly that file's own internal structure maps onto Pandoc's shared internal document model in the first place, which circles directly back to the "well-built vs. visually-faked structure" distinction from Chapter 5. A format being supported doesn't guarantee a specific file within that format will convert perfectly; a genuinely well-structured source file of nearly any supported format will generally outperform a poorly-structured file in a supposedly "safer" format.

### What This Means for a Transcriber, Practically

You will likely never run Pandoc directly as a transcriber using BrailleBlaster day to day — it operates behind the scenes as part of how certain file types open. But knowing it's there reframes a few recurring troubleshooting situations usefully:

- When an unusual or unsupported file format doesn't import well, converting it to a more universally well-supported intermediate format (HTML being the most reliable) before opening it in BrailleBlaster isn't a hacky workaround — it's working *with* the same architecture BrailleBlaster itself relies on, just doing one extra conversion step by hand that BrailleBlaster would otherwise have attempted automatically.
- The consistent advice throughout this manual to prioritize genuinely well-structured source documents — real heading styles, real list structures, real semantic markup, rather than merely visually-formatted text — isn't just good practice for BrailleBlaster specifically. It's good practice for the entire class of tools BrailleBlaster is built on top of, and it will keep paying off as BrailleBlaster's own supported-format list continues to grow.

### Trainer Tips and Pitfalls

> **Trainer Tip:** For a class of newer transcribers, this chapter works best as a short closing discussion rather than a technical deep dive — the goal is a working mental model ("there's a shared conversion engine under a lot of this, and that's why 'convert to HTML first' keeps coming up as advice"), not command-line fluency. Save deeper Pandoc mechanics for transcribers who go on to take a more technical, IT-adjacent role within your agency.

### Key Takeaways

- Pandoc is a general-purpose, open-source document converter that BrailleBlaster relies on for part of its support for formats like LaTeX and other Pandoc-supported document types.
- This shared architecture is why converting an unsupported or poorly-behaving file to HTML — a reliably well-supported format — is a recurring, sensible troubleshooting step throughout this manual, not a one-off trick specific to any single format.
- Broad format *support* and reliable per-file *conversion quality* are different things; a well-structured source file, in nearly any supported format, will outperform a poorly-structured one.
- The emphasis throughout this manual on genuine document structure over visual-only formatting reflects how the whole underlying conversion pipeline actually works, not just a BrailleBlaster-specific preference.

### Practice Exercise

As a closing exercise for the full course, have trainees write a short memo (a paragraph or two) to a hypothetical colleague explaining, in plain language, why they should ask source-material authors for well-structured documents (real headings, real lists) whenever possible — drawing on at least three specific examples from earlier chapters in this manual (Chapter 5's Word documents, Chapter 11's NIMAS files, and this chapter's Pandoc-supported formats are all fair game) to make the case concrete rather than abstract.

---

# Appendix A: Quick-Reference Keyboard Shortcuts

| Shortcut                       | Action                                      |
| ------------------------------ | ------------------------------------------- |
| `Ctrl+N`                       | New document                                |
| `Ctrl+O`                       | Open file                                   |
| `Ctrl+P`                       | Print (Print View)                          |
| `Ctrl+E`                       | Emboss (Braille View)                       |
| `Ctrl+Home` / `Ctrl+End`       | Navigate to beginning / end of file         |
| `Ctrl+G`                       | Go to a specific page                       |
| `Alt+Home`                     | Open Braille Preview                        |
| `Ctrl+B` / `Ctrl+I` / `Ctrl+U` | Bold / Italics / Underline emphasis         |
| `Alt+Shift+S`                  | Script emphasis                             |
| `Shift+Alt+1` – `Shift+Alt+5`  | Transcriber-Defined Typeforms 1–5           |
| `Ctrl+Shift+R`                 | Remove Emphasis from Section                |
| `Ctrl+R`                       | Repeat Last Style                           |
| `Ctrl+M`                       | Toggle Math Translation                     |
| `Ctrl+Shift+T`                 | Uncontracted Translation (selection)        |
| `Ctrl+D`                       | Direct Translation (selection)              |
| `Ctrl+T`                       | Correct Braille Translation                 |
| `Alt+X`                        | Toggle Six Key Mode                         |
| `Ctrl+F`                       | Find and Replace                            |
| `Shift+Enter`                  | Line Break (keep text on same braille line) |
| `Ctrl+Enter`                   | Page Break (force new braille page)         |
| `F2`                           | Insert line number                          |
| `Ctrl+F2`                      | Wrap Prose (for line numbering)             |
| `Ctrl+Shift+F2`                | Edit line number                            |
| `Ctrl+"+"` / `Ctrl+"-"`        | Increase / decrease font size               |

# Appendix B: Glossary

**ASCII Math** — A compact linear text notation for writing mathematical equations, used by BrailleBlaster as the intermediate form for math before translation into braille math code.

**BANA** — The Braille Authority of North America, publisher of *Braille Formats 2016*, the formatting standard BrailleBlaster's styles are built to follow.

**BBZ** — BrailleBlaster's default save format: a zipped NIMAS-style file set that preserves images and other resources alongside the document.

**Braille Formats 2016** — The BANA reference standard governing braille layout conventions (margins, headings, lists, typeforms, tables, and more) that BrailleBlaster's styles implement.

**BRF (Braille Ready File)** — A fixed-page, embosser-ready braille file format; the traditional end product of a transcription, and the format most physical embossers consume directly.

**eBraille** — A reflowable, EPUB-3-based digital braille reading format standardized by the DAISY Consortium, designed for refreshable braille displays rather than fixed physical pages.

**Interpoint** — Double-sided embossing, producing braille on both sides of the page.

**LibLouis** — The open-source braille translation engine BrailleBlaster relies on to convert text into braille.

**Nemeth Code** — A braille code for mathematical and scientific notation, usable either as a document's primary math code or embedded within a UEB document using Nemeth Block/Inline indicators.

**NIMAS** — The National Instructional Materials Accessibility Standard, an XML-based format publishers use to submit K–12 textbook content to NIMAC for production of accessible formats, including braille.

**Pandoc** — A general-purpose, open-source document converter that underlies part of BrailleBlaster's support for formats such as LaTeX.

**T-page / P-page** — Braille page number types used for transcriber-generated front matter (T-page) and other preliminary material (P-page), distinct from the Normal sequential numbering used for main content.

**UEB (Unified English Braille)** — BrailleBlaster's default literary braille code.

# Closing Note for Trainers

This manual is designed to be taught in the order presented, but every chapter is also written to stand alone, so sessions can be reordered or split to match your own course length and your trainees' prior experience. A cohort with prior Word-processing or DTP experience may move through Part I quickly and benefit from spending more time in Part II and Part IV; a cohort coming from a pure teaching background with no document-production experience may need the reverse.

Wherever possible, teach each chapter with BrailleBlaster open and a real (or realistically messy) source document on screen rather than a clean, pre-built example — the judgment calls this field actually requires (what to preserve, what to drop, what's really structure versus what only looks like structure) only become vivid through practice with material that has genuine ambiguity in it, and that's the skill this manual is ultimately trying to build.
