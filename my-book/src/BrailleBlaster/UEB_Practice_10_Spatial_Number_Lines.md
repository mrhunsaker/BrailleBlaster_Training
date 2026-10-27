# UEB Practice: Spatial Number Lines

## How to use this document:

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

