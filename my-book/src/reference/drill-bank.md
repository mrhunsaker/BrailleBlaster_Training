# Practice Drill Bank

Short, focused items for quick practice, warm-ups, and review. They come from the earlier Hands-On Practice Guide, with answer keys and several new judgment traps added. Each drill takes two to five minutes.

## How to use the drills

1. Copy one item into a new BrailleBlaster document.
2. Make your decisions **before** you read the key.
3. Check the Braille View.
4. Compare your reasoning with the key. Many items have more than one defensible answer, so the *reasoning* is what you are checking.

> [!NOTE]
> Emphasis drills use the markup key from [Lesson 3](../lessons/03-typeface-emphasis.md): `**bold**`, `*italic*`, `++underline++`, `[SCRIPT]…[/SCRIPT]`, `~~strikethrough~~`, `[HIGHLIGHT:color]…[/HIGHLIGHT]`. The markup is a stand-in so the print is unambiguous. It is **not** real formatting, and the symbols should not appear in your braille.

> [!IMPORTANT]
> The keys give principles and expected outcomes. Braille-code details such as which indicator a particular passage takes depend on your code, your agency, and your version, so **confirm in the Braille View** and your agency's rules.

---

## A. Emphasis (Lesson 3)

**A1.** The term **mitosis** appears frequently in biology textbooks.

**A2.** The novel *To Kill a Mockingbird* is required reading for all freshmen.

**A3.** The ++warning label++ on the equipment must not be removed.

**A4.** The teacher wrote [SCRIPT]Please review Chapter 3[/SCRIPT] in the margin of the textbook.

**A5.** The ++**key formula**++ in *The Chemistry Handbook* is H₂O.

**A6.** [HIGHLIGHT:pink]This sentence was highlighted in pink in the original and contains important information.[/HIGHLIGHT]

**A7.** The word **IMPORTANT** appears in capitals and bold in the print, and serves no purpose beyond visual emphasis.

**A8.** The *book title* contains a **key term** that should be ++underlined++ for the exam.

**Key**

- **A1.** Keep. A bolded key term is meaningful. One word takes a word-level indicator, so check that BrailleBlaster supplied one and not a passage indicator.
- **A2.** Keep. A title is classic italic. It is four words, so check whether your Braille View shows passage-level indicators, and recall the two-word versus three-word threshold from Lesson 3.
- **A3.** Keep if the print underlines it for meaning. Two words means two word-level indicators, one before each word.
- **A4.** Keep the script, because the typeform tells the reader this text is *handwritten*, a different voice. Consider a Transcriber's Note if the context is unclear.
- **A5.** Two typeforms combine on "key formula" (bold and underline), the title is italic, and H₂O has a subscript, which is mathematics. Decide each separately: emphasis, then the math toggle for the formula.
- **A6.** A judgment call. If the teacher refers to the highlighting, it carries meaning: use a **transcriber-defined typeform** and explain it on the Special Symbols page. If the highlighting was only the previous reader's study marks, disregard it. Either way, write down the decision.
- **A7.** Disregard the bold. It is decoration. Keep the capitals as printed, because capitalization is part of the word, not a typeform.
- **A8.** Three different typeforms on three different pieces of text. Treat each on its own terms and verify in the Braille View that none leaks into its neighbor.

---

## B. Styles, headings, and lists (Lessons 4 to 6)

**B1.** Apply styles to these two lines. You have no legend.

```text
Introduction to Cellular Biology
The Structure and Function of Cells
```

**B2.** Apply styles to this text.

```text
All living organisms are composed of cells. The cell is the basic unit of life. Cells can be prokaryotic or eukaryotic.
Another characteristic of cells is that they can reproduce.
```

**B3.** Apply styles to this text.

```text
- The three states of matter are solid
- liquid
- and gas
```

**B4.** Apply list styles to this two-level list.

```text
- Mammals
    - Dogs
    - Cats
    - Humans
- Reptiles
    - Snakes
    - Lizards
```

**B5.** Format this quotation.

```text
As the poet wrote of the tide:
The water slips away at noon
and leaves the shore a quiet floor,
a scatter of shells and a bent spoon
```

**Key**

- **B1.** There is no legend, so you must state an assumption. If these are two headings at different levels, use two heading levels. If the second is a subtitle of the first, treat them as one heading unit. The skill is saying which you assumed, and asking for the print source when you can.
- **B2.** Two Body Text paragraphs. First check whether the line break between them is a real paragraph break or only a wrapped line in the source. If it is wrapped, join them.
- **B3.** This is a trap. It is **not a list**. It is one sentence split across lines, with bullets added by a previous editor. Join it into a single Body Text paragraph: *The three states of matter are solid, liquid, and gas.* Do the structural test from Lesson 4: is this really a structured enumeration?
- **B4.** A two-level list: Mammals and Reptiles at level 1, and their children at level 2. Check Breadcrumbs for the CONTAINER, and confirm the runover margins in the Braille View.
- **B5.** The line breaks matter here, because it is verse, so a poetry style is the right choice, not a block quotation. A prose quotation would take a quotation or block style listed in the style specification tables in the User Guide instead. See Lesson 18.

---

## C. Math (Lessons 7 and 8)

**C1.** The area of a circle is πr² where r is the radius.

**C2.** The Pythagorean theorem states that a² + b² = c².

**C3.** In the equation y = mx + b, the variable m is the slope and b is the y-intercept.

**C4.** The formula for compound interest is A = P(1 + r/n)^(nt).

**C5.** The sum of the angles in a triangle is 180°. The circumference of a circle is 2πr.

Build these with the ASCII Math Hub (Lesson 8):

**C6.** (x + 1)/(x − 1)

**C7.** (a/b + c/d)/(e/f − g/h)

**C8.** xⁿ⁺¹

**C9.** H₂O and CO₂

**C10.** √(x² + y²)

**C11.** The formula uses π and θ.

**C12.** (a + b)² = a² + 2ab + b²

**Key**

- **C1.** Flag *πr²* as math with `Ctrl+M`. Apply the **sentence test**: it reads as part of the sentence, so use Nemeth **Inline** if your document uses Nemeth indicators. The lone variable *r* is a judgment call, so follow your agency's convention and be consistent.
- **C2.** The expression is part of the sentence, so Inline.
- **C3.** Flag *y = mx + b* as Inline math. The hyphen in "y-intercept" is a literary hyphen, not a minus sign, so do not flag it as subtraction. Whether to flag the lone *y* is again an agency convention.
- **C4.** Flag it, but build it in the **Hub**: the nested exponent is a structure, so linear typing invites errors.
- **C5.** Two separate sentences, so decide each one. *2πr* is math. For *180°*, check how your code treats a number with a degree sign, and apply that consistently.
- **C6.** In ASCII Math: `(x+1)/(x-1)`. The Hub's Examples tab shows the structure and its image.
- **C7.** A complex fraction: `((a/b)+(c/d))/((e/f)-(g/h))`. Use the Examples tab and build the numerator and denominator separately.
- **C8.** `x^(n+1)`. The parentheses group the whole exponent.
- **C9.** Subscripts: `H_2O` and `CO_2`. Chemical formulas are mathematics-style notation, so flag them.
- **C10.** `sqrt(x^2+y^2)`.
- **C11.** Greek letters appear in the Greek tab, or as `pi` and `theta`.
- **C12.** `(a+b)^2 = a^2 + 2ab + b^2`.

The ASCII Math forms above follow the common AsciiMath style. Use the Hub to confirm the exact form BrailleBlaster expects, and verify each result in the Braille View.

---

## D. Reading a Word document's structure (Lesson 2)

**D1.** A Word document contains these paragraphs, built with Word's Heading 1, Heading 2, and List Bullet styles. What will arrive in BrailleBlaster?

```text
The Water Cycle            (Heading 1)
Evaporation                (Heading 2)
Water turns into vapor and rises into the atmosphere.
Condensation               (Heading 2)
Water vapor cools and forms clouds.
Precipitation              (Heading 2)
Rain, Snow, Sleet, Hail    (four List Bullet paragraphs)
```

**D2.** The same words, but every paragraph is Normal, the three section names are just bold, and the four weather types begin with a typed hyphen. What will arrive, and what must you correct?

**Key**

- **D1.** The headings and list should arrive with matching styles. Verify in Breadcrumbs, then check the Braille View. Little correction should be needed.
- **D2.** Expect Body Text for nearly everything. You must apply the heading styles, remove the typed hyphens, and apply the list style. Fix structure first, then decide about emphasis. This is the situation in [Lab 1](../labs/lab-1-rescue-word-document.md).

---

## E. Page properties (Lesson 13)

**E1.** Paste `reflow-paragraph.txt` from the [sample files](../samples/index.md). Record the number of braille pages at your default page properties.

**E2.** Change the Cells Per Line, then the Lines Per Page, and record the page count each time.

**E3.** Paste the paragraph five times under each of two headings and note how the pages break.

**Key**

- **E1 to E3.** These are observation drills. Fewer cells per line or fewer lines per page should give more pages for the same text. Use them to convince yourself that page properties must be set **before** transcription, and that **OK** applies changes to the current document while **Make Default** changes future documents.

---

## F. Translation controls (Lesson 11)

**F1.** Say which control you would use for each item, and why. Your choices are the **Contraction Relaxer**, **Change Translation: Uncontracted**, **Change Translation: Direct**, and the **math toggle**.

- a learner who has been taught only the earliest contraction units reads the whole handout;
- a line of computer code in the middle of a paragraph;
- a string of pre-translated ASCII braille that must appear exactly as typed;
- the expression O(log n);
- the phrase "binary search" in the prose.

**F2.** A teacher says, "Use the Contraction Relaxer to uncontract this one function name." What do you say?

**Key**

- **F1.** The **learner**: the Relaxer, choosing the last unit the learner has been taught, because that is a whole-document, instructional decision. The **code line**: Change Translation, Uncontracted (`Ctrl+Shift+T`), because every character must be exact and the decision applies to one passage. The **pre-translated ASCII string**: Change Translation, Direct (`Ctrl+D`), which gives the literal ASCII translation. **O(log n)**: the math toggle, because it is mathematics. **"Binary search"**: no special control. It stays as the Relaxer's unit and the document's translation setting dictate.
- **F2.** The Relaxer works on the whole document by teaching unit. For a single function name, select it and use **Tools > Change Translation**: Uncontracted, or Direct if it must be exact.

The deciding questions are: *is this about what the learner has been taught, or about one passage?* and *would contractions change the meaning or make it impossible to read exactly?*
