# Lab 7: Choosing the Right Translation Control

**Time:** about 60 minutes. **Needs:** [Lessons 7](../lessons/07-math-translation-toggle.md), [11](../lessons/11-contraction-relaxer.md), and [22](../lessons/22-transcribers-notes.md). **File:** `relaxer-code-and-math.txt` from the [sample files](../samples/index.md). **Job aid:** the Translation Control Plan in [Job Aids](../reference/job-aids.md).

## Scenario

A computer science teacher gives you a handout with short code samples and some algorithm math inside ordinary sentences. It is for a learner who has been taught contractions only through the early units. You have three different problems, and BrailleBlaster has three different controls:

| Problem | Right control | Level |
| ------- | ------------- | ----- |
| How many contractions should this learner see in the *prose*? | **Tools > Contraction Relaxer** | The whole document, by teaching unit |
| Must this *code* appear exactly as typed? | **Tools > Change Translation** (Uncontracted `Ctrl+Shift+T`, or Direct `Ctrl+D`) | The selected text |
| Is this *mathematics*? | The math toggle, `Ctrl+M` | The selected text |

The skill is choosing the right control for each passage and recording why. A common mistake is to reach for the Relaxer to fix a line of code. The Relaxer works on the whole document and cannot help one passage.

## The passes

Work in passes, like the Three-Pass Method in [Lab 1](lab-1-rescue-word-document.md):

1. **Transcribe** with the document fully contracted.
2. **Identify** each passage that needs a decision, and list it in the plan.
3. **Apply** the right control to each.
4. **Verify** every change in the Braille View.
5. **Document** every use in a Transcriber's Note.

## Steps

### Pass 1: Transcribe

Paste `relaxer-code-and-math.txt` into a new document. Read the Braille View. Find words that BrailleBlaster has contracted inside the code. Write a **prediction** of which words will contract, then check. Words such as *function* or *return* can contain contractions, so look and do not assume.

### Pass 2: Identify

Complete the Translation Control Plan. Include at least:

- the two-line code sample in Part A;
- the identifier `add_one` where it appears in prose;
- the expression `O(log n)`;
- the formula `mid = (low + high) / 2`;
- the *prose* of the whole handout, for the learner.

For each, decide which control applies and why.

### Pass 3: Apply

1. **For the learner.** Open **Tools > Contraction Relaxer** and choose the last unit this learner has been taught. Pick **Unit 3** for this lab. Remember that earlier units are included too. Click **OK**.
2. **For the code.** Select the code and use **Tools > Change Translation** with **Uncontracted** (`Ctrl+Shift+T`). If a string must appear *exactly* as typed, use **Direct** (`Ctrl+D`) instead. Note how the two are highlighted: Uncontracted in green in the Braille View, and Direct in purple in the Print View.
3. **For the mathematics.** Flag true math with `Ctrl+M` and choose Inline or Block, using the rule from [Lesson 7](../lessons/07-math-translation-toggle.md).

> [!NOTE]
> The Relaxer changes the **whole document**, so run it once, first, and then apply the selection-level controls. If you reverse the order, check that the Relaxer has not changed your selections.

### Pass 4: Verify

Read the Braille View from top to bottom. Confirm that:

- the prose follows the chosen unit, so contractions from later units are written out;
- the code is uncontracted (or exactly as typed, if you used Direct);
- the math is flagged and translated as math.

### Pass 5: Document

Write a short Transcriber's Note ([Lesson 22](../lessons/22-transcribers-notes.md)) that tells the reader what is unusual, and a separate line in your plan that records the **unit** and the **reason** for the teacher. A model note:

> *Computer code is shown uncontracted so that every character can be read exactly.*

## A decision rule to apply

Ask two questions in this order:

1. **"Is this a matter of what the learner has been taught?"** If yes, use the Relaxer, and set it once for the document.
2. **"Would contractions change the meaning, or make this impossible to read exactly?"** If yes, use Change Translation on that passage. If the answer is only "it would be shorter," leave it alone.

## Expected observations

- The Relaxer changes the prose throughout the document, and not only the passages you were thinking about.
- Code is the clearest case for selection-level Uncontracted or Direct translation.
- Mathematics belongs under the math toggle, not under either translation control.
- A reader who sees uncontracted code with no explanation will wonder if it is an error. The note answers that.

## Debrief questions

1. Why is the Relaxer the wrong tool for one line of code?
2. What is the difference between *Uncontracted* and *Direct* for a selection?
3. The Relaxer is cumulative. What would go wrong if you chose Unit 3 thinking it switched Unit 3 *off*?
4. How would the plan change for a learner who has been taught through Unit 9?
