# Capstone: Transcribe a Textbook Chapter

The capstone brings the whole course together. You will transcribe a short chapter as if it were a real production job, make and defend your decisions, and hand in a finished, volume-ready package.

**Suggested time:** about 4 hours, over one or two sittings.
**Prerequisites:** Units 1 and 3. Unit 2 is helpful but optional.

## The job

A middle school science teacher has asked for a braille copy of "Chapter 3: Energy and Motion" for a student who reads UEB with Nemeth Code for math. The student uses embossed braille and needs the material in more than one volume.

You will be given the print source as a plain-text document with a legend (below), because plain text carries no formatting and the real skill is deciding structure from context.

## Deliverables

1. The BrailleBlaster document (`.bbz`).
2. A BRF export of each volume.
3. A **production log** of no more than one page that records:
   - the page setup and embosser or paper you assumed;
   - how you mapped the print headings to braille headings and why;
   - every Transcriber's Note you wrote and why it was needed;
   - which print emphasis you kept, which you dropped, and what you did with the highlighting;
   - where you chose the volume breaks;
   - anything you would flag to the teacher.
4. A **proofreading checklist** with each item marked.

## The source

### Print source legend

| Element in the source | How it looked in print |
| --------------------- | ---------------------- |
| "CHAPTER 3: ENERGY AND MOTION" | Chapter title, the highest heading level |
| "3.1 What Is Energy?", "3.2 Motion and Speed" | Section headings |
| "Kinds of Energy", "Calculating Speed" | Subsection headings |
| `**word**` | Bold key term |
| `*Title*` | Italic book title |
| `[HIGHLIGHT:yellow]text[/HIGHLIGHT]` | Yellow highlighting that the teacher refers to aloud |
| `[BOX] ... [/BOX]` | A shaded box titled "Did You Know?" |
| `[FIGURE]` | A diagram of a roller coaster, with a printed caption |
| `[PAGE 41]` | A print page break |
| The list under "Kinds of Energy" | A three-level list. "Kinetic energy," "Potential energy," and "Thermal energy" are level 1. "Energy of motion," "Stored energy," and "Energy of heat" are level 2. The examples ("A moving cart," "A stretched spring," "A book on a high shelf") are level 3 |

None of the markup above is real formatting. It is a stand-in so the print source is unambiguous.

### Practice Document

```text
[PAGE 41]
CHAPTER 3: ENERGY AND MOTION

3.1 What Is Energy?

Energy is the ability to do work. A roller coaster at the top of a hill has a lot of stored energy. As it rolls down, that energy changes into motion. The book *Forces Around Us* describes this idea in more detail.

Kinds of Energy

There are many kinds of energy. The three you will study first are:

Kinetic energy
Energy of motion
A moving cart
Potential energy
Stored energy
A stretched spring
A book on a high shelf
Thermal energy
Energy of heat

[BOX]
Did You Know?
Energy cannot be created or destroyed. It can only change from one form to another.
[/BOX]

[PAGE 42]
The key term to remember is **conservation**. [HIGHLIGHT:yellow]Everything in yellow will be on the quiz.[/HIGHLIGHT]

[FIGURE]
Caption: Figure 3.1 A roller coaster at the top of a hill and at the bottom.
[/FIGURE]

3.2 Motion and Speed

Speed tells us how fast something moves. A car that travels 120 miles in 2 hours has an average speed of 60 miles per hour.

Calculating Speed

To find speed, divide the distance by the time:

speed = distance / time

For example, if d = 120 and t = 2, then

s = d/t = 120/2 = 60

A cyclist rides 3x - 5 miles on Monday, where x = 10. Solve for the distance: 3x - 5 = 25.

The well-known "zig-zag" test track is 2 miles long, and the test cars rated x-ray safe pass in about 5-2 minutes of setup.
```

> [!NOTE]
> The last sentence is a trap on purpose. Look back at [Lesson 7](../lessons/07-math-translation-toggle.md) before you decide what is math.

## Required tasks

Work in roughly this order. The lessons that apply to each task are listed.

1. **Set up** the page for 40 cells by 25 lines, single-sided or interpoint as you choose, and record the choice. (Lesson 13)
2. **Structure.** Map the print headings to braille headings. There are four print levels. (Lessons 4 and 5)
3. **Lists.** Format the nested list correctly. (Lesson 6)
4. **Emphasis.** Decide what to keep. Treat the highlighting as meaningful, because the teacher refers to it aloud. (Lesson 3)
5. **Math.** Flag the real math and build the displayed expressions. Leave prose hyphens and the letter x alone. (Lessons 7 and 8)
6. **Box and figure.** Treat the box by its function. Write a short transcriber-generated description for the figure, apart from the print caption. (Lessons 18 and 22)
7. **Page numbers and running head.** Add print page numbers 41 and 42 at the right points, and a running head that fits. (Lesson 21)
8. **Notes.** Write at least one inline and one separate Transcriber's Note. (Lesson 22)
9. **Volumes and TOC.** For this short chapter, divide it into two pretend volumes at a natural boundary, insert End of Volume markers, build the TOC, and disperse it. (Lesson 23)
10. **T-pages.** Generate a title page, a Special Symbols page for the highlighting typeform, and a Transcriber's Notes page. (Lesson 24)
11. **Output.** Export a BRF for each volume. (Lesson 13)
12. **Proof and log.** Complete the proofreading checklist and the production log.

## Proofreading checklist

- [ ] Every heading has the intended style, and the same print level always gets the same braille style.
- [ ] Lists have the correct levels, and runovers are correct.
- [ ] Only meaningful emphasis is carried, and the highlighting has a transcriber-defined typeform documented on the Special Symbols page.
- [ ] Only true math is flagged. Hyphens in "well-known," "zig-zag," and "x-ray" are literary.
- [ ] Print and braille page numbers are distinct and correct.
- [ ] The running head fits with the longest page number.
- [ ] Notes are placed correctly, and the Transcriber's Notes page matches the notes in the text.
- [ ] The TOC and the volume breaks agree.
- [ ] I looked at the Braille View after every major change.

## Scoring rubric

Score each row from 1 (not yet) to 4 (exemplary). Total: 40 points.

| Criterion | 4: Exemplary | 3: Proficient | 2: Developing | 1: Not yet |
| --------- | ------------ | ------------- | ------------- | ----------- |
| **Structure and headings** | All levels mapped consistently, with a clear rationale | Consistent, with minor issues | Some inconsistency | Levels confused or faked with spaces |
| **Lists and layout styles** | Correct levels, margins, and containers | One minor error | Several errors | Lists built with spaces |
| **Emphasis decisions** | Meaningful emphasis kept, decorative dropped, highlight documented | Mostly correct | Over- or under-preserved | Emphasis ignored or typed in |
| **Mathematics** | All math flagged and built correctly, with no false positives | One error | Several errors | Math missing or mis-flagged throughout |
| **Special structures** | Box and figure handled by function, with a distinct description | Minor errors | Box decorative, or figure unclear | Not addressed |
| **Page numbers and running head** | Correct and verified | Minor error | Print and braille numbers confused | Absent or wrong |
| **Notes and T-pages** | Accurate, matching, and well placed | Minor mismatch | Incomplete | Absent |
| **Volumes and TOC** | Natural breaks, TOC matches volumes | Minor mismatch | Breaks arbitrary | Not completed |
| **Output and proofreading** | BRFs correct and checklist complete | Minor gaps | Checklist partial | No verification |
| **Production log** | Clear, specific, and honest about doubts | Mostly clear | Vague | Missing |

**Interpreting the total.** 36 to 40 is production-ready. 28 to 35 is proficient and needs a revision pass. 20 to 27 needs targeted review of the lessons named above. Below 20, repeat the relevant lessons and try again.

## After the capstone

Compare your log with a classmate's or with your instructor's. Where you made different choices, ask what each choice assumed about the reader. *Braille Formats 2016* is a set of guidelines for making structural decisions, not a rulebook that covers every case. Two defensible answers that are applied consistently and explained are both correct.
