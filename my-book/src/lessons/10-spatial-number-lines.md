# Lesson 10: Spatial Number Lines

> **Lesson at a glance**
>
> - **Unit:** Unit 1: Universal Lessons
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 9](09-spatial-math-editor.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Choose between Math Entry and User Text for number-line labels.
- Show single points, open intervals, closed intervals, and mixed endpoints correctly.
- Build a number line with the Number Line Editor.
- Check the translation of the finished number line.

## Why this matters

Number lines look simple and are anything but, once you start transcribing them. A print number line encodes information in position (where a point sits between labeled marks), in symbol (open vs. filled circles, arrows), and often in fraction form that print textbooks show in a "nice," pre-reduced way for pedagogical reasons. All of that has to survive translation into a linear braille format that a reader explores with their fingertip rather than their eye, moving left to right one cell at a time. This lesson builds directly on [Lesson 9](09-spatial-math-editor.md) — the Number Line Editor is one of the four container types inside the Spatial Math Editor — and deserves its own dedicated lesson because number lines show up constantly in early-grades math materials and have enough of their own settings to warrant close attention.

---

## How to use this lesson

The first half explains the Number Line Editor as a specialized spatial-math structure. The second half is a practice document — create each number line in BrailleBlaster and select the appropriate view, points or interval, endpoint symbols, and labels.

---

## The Concept

### A number line is more than a sequence of numbers

A number line communicates two kinds of information simultaneously:

1. **Values and labels**
2. **Position and relationship along a line**

BrailleBlaster's Spatial Math Editor includes a **Number Line Editor** specifically for this purpose.

### Math Entry and User Text are different choices

Current BrailleBlaster documentation describes two number-line views:

- **Math Entry** — for sequential number-line information entered as math.
- **User Text** — for labels that are not entered as mathematical expressions.

User Text also provides a Line Marker option for placing multiple labeled markers along the line.

### Points and intervals communicate different mathematics

The editor distinguishes:

- **Points** — discrete locations.
- **Interval** — a line segment.
- **None** — no points or interval.

An interval can also have an endpoint type:

- Empty Circle
- Full Circle
- None

These choices should reflect the mathematical meaning of the source, not the teacher's preference for how the graphic looks.

---

## Step by step

1. Place the cursor where the number line belongs; open **Math > Spatial Math Editor**.
2. Choose **Number Line Editor** as the Container Type.
3. Review and set the settings above — Reduce Fraction, Beveled Fraction, Add Arrows to Line, Stretch Across Page, Remove Leading Zeros, and Number Line View — to match the print original *before* entering values, since several of these change how the values you're about to enter will be interpreted and displayed.
4. If you chose *Interval* under Interval/Points, also set Start Interval Type and End Interval Type to match the print circles.
5. Fill in the core values: **Count By** (the increment between labeled numbers), **Line Start**, **Line End**, and — if using an Interval — **Interval Start** and **Interval End**. BrailleBlaster calculates the full number line automatically once these are filled in with mathematically consistent values.
6. Click **Insert** to place the completed number line into the document.

---

## Worked Demonstration (small, fully correct)

Create the number line for:

```text
0    1    2    3    4    5
          ●
```

The marked point is at 2.

Correct setup:

- Open **Math > Spatial Math Editor**.
- Choose **Number Line Editor**.
- Use Math Entry if the labels are mathematical values.
- Set the appropriate range.
- Choose **Points**.
- Place the point at 2.
- Insert the number line.
- Check the Braille View.

If the exercise instead represents the interval `2 ≤ x ≤ 4`, the structure is different: use an interval with the appropriate endpoint symbols rather than a single point.

---

## Practice Document

### 1. Single point

```text
0  1  2  3  4  5
      ●
```

### 2. Open interval

```text
0  1  2  3  4  5
      ○────────○
```

Interpret the endpoints as open.

### 3. Closed interval

```text
0  1  2  3  4  5
      ●────────●
```

Interpret the endpoints as closed.

### 4. Mixed endpoints

```text
0  1  2  3  4  5
      ○────────●
```

### 5. User-text labels

```text
cold       comfortable       hot
 |-------------|--------------|
```

Use labels that are not merely numerical math expressions. (Note, this one has an error and I leave it to your discretion to fix it)

---

## Answer Key

### 1. Single point

Use **Points** and place one point at the designated value.

### 2. Open interval

Use **Interval**, with **Empty Circle** at both ends.

### 3. Closed interval

Use **Interval**, with **Full Circle** at both ends.

### 4. Mixed endpoints

Use **Interval**, with an Empty Circle at the open endpoint and Full Circle at the closed endpoint.

### 5. User-text labels

Use **User Text** because the labels are words rather than mathematical values. The Line Marker option may be used when multiple labeled locations are needed. 

The trick here was using the word comfortable makes the numberline too long. I personally replaced it with "comfy" and it worked great. 

### Translation check

The documentation notes that decimal values can require attention to translation. For example, `0.5` appears as `.5` in braille. Always verify number-line labels in Braille View rather than assuming the Print View gives the final code.

---

---

## Key takeaways

- Number lines are one of the four container types inside the Spatial Math Editor, with settings specific to fractions, arrows, page width, interval markers, and endpoint symbols.
- Set the descriptive options (Reduce Fraction, Beveled Fraction, Number Line View, and so on) before entering the numeric values, since they affect how those values are interpreted.
- BrailleBlaster calculates the full sequence of labeled points automatically from Count By, Line Start, and Line End — you don't type each label individually.
- Match Start/End Interval Type to the print original's open vs. filled circles to preserve the mathematical meaning of the interval, not just its visual appearance.
