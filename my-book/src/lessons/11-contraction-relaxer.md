# Lesson 11: Using the Contraction Relaxer

> **Lesson at a glance**
>
> - **Unit:** Unit 1: Universal Lessons
> - **Suggested time:** about 2 hours
> - **Prerequisites:** [Lesson 1](01-navigating-the-interface.md), [Lesson 3](03-typeface-emphasis.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Explain why contracted braille is not an all-or-nothing instructional decision.
- Relax or uncontract selected text with **Tools > Contraction Relaxer** and `Ctrl+Shift+T`.
- Use Direct translation (`Ctrl+D`) and the No Translate text attribute where they fit.
- Apply a teacher decision rule and document why a contraction was relaxed.

## Why this matters

Standard literary braille (Unified English Braille, Grade 2) uses contractions extensively — single cells or short cell combinations standing in for common letter groups and whole words, which is what makes contracted braille meaningfully more compact than an uncontracted, letter-for-letter transcription. Most of the time, an agency's translation table setting handles this globally and correctly, with no per-document intervention needed. But contractions can occasionally cause real problems for a specific reader or a specific kind of material — an emerging reader still learning contractions, unfamiliar technical vocabulary where contraction boundaries could be confusing, or specific words where the contracted form happens to be more ambiguous than useful. The **Contraction Relaxer** exists for exactly this situation: finer control than an all-or-nothing switch between contracted and uncontracted braille.

---

## How to use this lesson

The first half explains the concept from a teacher's perspective. The second half is a practice document — copy the "Practice Story" block into BrailleBlaster, translate it in contracted UEB, and use the **Contraction Relaxer** to selectively suppress contractions that may not yet be appropriate for a particular learner. The point is not to produce a universally "better" braille file: it is to practice making a deliberate instructional choice about which contractions a student should encounter. The story supplied for this exercise is intentionally rich in contraction opportunities.

---

## The Concept

### Contracted UEB is not an all-or-nothing instructional decision

The NFB's 2015 *Instruction Manual for Braille Transcribing, UEB Edition* teaches contractions as a systematic part of UEB rather than as arbitrary shortcuts. For teachers for students with visual impairments (TVI) or a school-based braille transcriber, however, the practical question is often different from the transcriber's question: **Which contractions should this particular student be reading right now?**

BrailleBlaster's Contraction Relaxer provides a way to make that instructional adjustment without converting the entire document to uncontracted UEB. BrailleBlaster's current documentation explicitly describes the tool as a way to suppress selected contractions while retaining more control than changing the entire document to an uncontracted translation profile.

This tool is similar to the "Learning Tables" function in Duxbury DBT. For no, the developers of BrailleBlaster have made the explicit decision to focus on a single source for the sequence of learning braille contractions. 

### The teacher's task is to match the code to the learner

A useful instructional progression is:

- Start with the student's current contraction knowledge rather than the full list of UEB contractions.
- Keep contractions the student has been explicitly taught and is expected to recognize.
- Relax contractions that have not yet been introduced when their presence would turn a reading exercise into an unnecessary decoding task.
- Recheck the resulting braille after changing the contraction settings; the goal is a readable instructional text, not merely a visually simpler Print View.
- Preserve the same instructional decision across a lesson or passage unless there is a reason to change it.

The contraction relaxer therefore belongs in the teacher's toolkit as an **access and instructional differentiation tool**, not merely as a transcription shortcut.

### What "relaxing" means

Relaxing a contraction means telling the translation process not to use a selected contraction in places where that contraction would otherwise be valid. The print word does not change. The student's reading task changes because the braille spells out more of the word instead of representing part of it with a contraction.

For example, a teacher may want a passage to remain fully UEB while temporarily reducing the number of contraction types a beginning reader must decode. The exact set should be based on the student's instructional sequence.

### A note about the 2015 NFB materials and current BrailleBlaster

The NFB 2015 manual is a UEB training resource; the Contraction Relaxer is a later BrailleBlaster feature. This exercise therefore combines two layers deliberately:

1. **UEB knowledge from the 2015 training:** recognize what contractions are doing in the words.
2. **Current BrailleBlaster workflow:** use the Contraction Relaxer to suppress selected contraction categories for an instructional purpose.

Do not treat the current tool's interface as if it were part of the 2015 manual.

---
## The Old, Hard Manual way

For this example, I am going to manually apply the contraction for "day" into the following block of text. 

``` 
Today is the greatest day I've ever known.
```

For the sake of simplicity and argument, I am going to go into the **Tools > Contraction Relaxer** Menu and selecting "Uncontracted (Grade 1)".

To manually swap out the letter d, a, and y with a dot 5 followed by the letter "d", I do the following. 
- Press `CTRL+F` or go to **Edit > Find and Replace** to open the find and replace dialog. 
- In **Find** I will type "day" without the quotation marks. 
- In **Replace With** I will type ASCII braille for dot5 followed by the letter "d". This is `"d`
- I will then click the **Formatting** button next to **Replace With**
- In the **Replace Formatting** menu that pops up, I will click the dropdown menu next to **Text Attributes** and select **No Translate**
- Press the **Add** button next to the dropdown Menu 
- When I press **Replace All**, every incidence of "day" is replaced with the initial letter contraction for day. 

In essence, this manual process does the same thing as selecting every incidence of "day" in the print view and hitting `CTRL+D` or **Tools > Change Translation > Direct**, which returns the now highlighted text as ASCII braille equivalent rather than the UEB Translation.

This is a laborious process, but it is the way a lot of us have had to relax contractions in the past. The Contraction Relaxer dialog provides us a more user friendly tool to accomplish this. But it is important to know the old way, as it gives the finest level of granularity for any students learning contractions in a nonstandard order. 

### CHALLENGE

Paste the following into the print view. Then go to **Tools > Change Translation > Uncontracted**, select the entire text and press `CTRL+SHIFT+T`, or go to **Tools > Contraction Relaxer > Uncontracted (Grade 1)**. 
```
today forever forefather here knows landlord motherlode namely honest party questions bright wholesome primetime underground workout younger therefore characteristic throughout whereafter bought
```
Practice using the find and replace menu to translate the dot 5 initial letter contractions embedded in the pasted words. It feels odd at first, but with practice the process comes to feel more natural. 

## Step by step

1. Go to **Tools > Contraction Relaxer**.
2. Review the available contractions and select which ones should be suppressed (relaxed) for this document, based on the specific need driving the request — a reader's current contraction curriculum, a term whose contracted form is causing confusion, or a similar targeted reason.
3. Apply the changes and review the affected text in the Braille View to confirm the intended contractions are now suppressed while the rest of the document's contracted braille is unaffected.

> **Note:** Because the Contraction Relaxer changes translation behavior at a fairly fundamental level, treat any relaxer configuration as a deliberate, documented decision for a specific document or reader — not a setting to reach for casually. If your agency serves multiple readers with different contraction-learning stages, a documented, per-reader relaxer profile (what's relaxed, and why) is worth maintaining alongside the file itself, so a future transcriber picking up the same reader's material later understands the reasoning rather than just inheriting an unexplained configuration.

---

## Worked Demonstration using Contraction Relaxer (small, fully correct)

```
The teacher will help the child read the book before the class begins.
```

Suppose the student's current instructional target includes ordinary alphabetic words but not the contraction patterns represented by every possible UEB contraction.

A teacher-facing workflow is:

- Translate the passage in contracted UEB.
- Open **Tools > Contraction Relaxer**.
- Review the available contraction choices rather than guessing which contractions occur.
- Select only the contraction unit(s) the student has not yet been taught.
- Apply the change.
- Inspect the Braille View and read the passage as the student will encounter it.
- If the passage still contains a contraction that is outside the student's taught set, return to the relaxer and adjust the selected unit(s).
- Save the differentiated instructional version separately from the master document when the materials need to be reused at different instructional levels.

The important distinction is between **"uncontracted"** and **"selectively relaxed."** The latter preserves more of the normal UEB reading environment while reducing the specific contraction burden.

---

## Practice Document: "Herbert and the Magic Eggs"

### Practice instructions

Copy the passage below into BrailleBlaster.

For each round, use the Contraction Relaxer to create a different instructional version:

- **Round 1 — Full contracted UEB:** make no contraction-relaxation changes.
- **Round 2 — Beginning-reader differentiation:** relax the contraction units that your student has not yet been taught. Record the units you selected.
- **Round 3 — Targeted review:** choose one contraction unit that appears repeatedly in the passage and relax it so the student can read the surrounding vocabulary without that contraction.
- **Round 4 — Restore and compare:** restore the original contracted translation and compare the Braille View with Round 3.

Do not manually retype words to remove contractions. The exercise is specifically about using the translation control.

### Practice Story

```text
Herbert and the Magic Eggs
a UEB braille story by Erin Jepsen
Moscow, Idaho

Once upon a time, there was a young mouse whose name was Herbert. One day, Herbert, who always thought about wanting to go off by himself for the afternoon, declared that today would be different. According to Herbert, he needed to be quick to get across the road to his favorite hiding spot. Rather than risking all the people driving along the highway, he had a brilliant idea. He decided to tunnel beneath the road in order to reach the place where his friend would meet him. She called herself Spirit Stella, and she was Herbert’s best friend.

When they played together, as children do, they imagined all sorts of strange sounds, deceiving themselves into believing that beyond the distant mountains, a voice said, “Lord Herbert, you are just a little bit behind your part in receiving quite enough questions. Your knowledge is not already so great that you cannot arrive between the hills to the magic castle!”

Herbert immediately sat down beside Stella, but before he could begin to cry, she said, “You know, Herbert, you are still a child. Your mother will work with you every day so you receive everything you need to reach the castle: science, either geography or geometry; also, although they should teach beyond the letters that seem useless, they do know as much as myself about so many other things! Don’t deceive yourself, Herbert, you’re already almost through those subjects that you need for your quest.”

Herbert (against his conscience) replied to Stella, “It’s useless. My father was even declaring, ‘my son can do no good unless he reaches the castle, collects the magic eggs, and does the rejoicing dance tomorrow.’ So, I will have to go out tonight into the world. This is the only right way that the magic will renew itself. Perhaps you would come with me?”

“I’d like that, Herbert,” said Stella, after some thought. We should do whatever is necessary, and afterward, we’ll come altogether again from the wonderful castle to your house, although by the time we arrive under the cover of darkness, neither of us will be able to see; we’ll be so blind we must find our way by braille!

“Shall we depart, then?” asked Herbert, and Stella nodded. This is the way their path led: first, below the forest, under tall trees, then above these crazy large boulders such as did not even have a name. Stella herself, because she had more words than Herbert, could conceive of a compliment to be paid to the boulders, but Herbert, was only perceiving the rumble in his tummy.

“We need a ration given to us,” he complained. “One which we ourselves can affect to eat as we walk. That would at least accomplish its purpose here.”

Stella replied to him, “It’s a pity your character is so weak that you’re thinking more about your stomach than conceiving a name for these rocks! One should tell oneself, or maybe thyself that it’s no illusion we were here—wait!”

“What?” asked a bewildered Herbert.

“I perceive that these enormous rocks, which you would have passed, are really our castle! We have arrived!”

“Oh, let’s rejoice!” bubbled Herbert. “You get the magic eggs, and I’ll get some eggs for eating.”

So they did and ran joyfully back home to Herbert’s dad with the magic eggs.

The end.
```

---

## Answer Key

### Round 1

**Full contracted UEB** — no contraction units are deliberately relaxed. The purpose is to establish the baseline against which the instructional versions can be compared.

### Round 2

**Fully uncontracted UEB** — all contraction units are deliberately relaxed. The purpose is to establish the no-contraction baseline against which the instructional versions can be compared.

### Round 3

There is no single correct list of relaxed units without knowing the student's instructional history. A defensible teacher record should identify:

- the contraction unit(s) selected;
- why those units are outside the student's current taught set;
- whether the choice applies to the whole passage or only to a lesson;
- whether the resulting text was checked in Braille View.

### Round 4

Choose a contraction unit that is visibly frequent in the passage. A strong practice choice is one whose relaxation changes many words, because the teacher can then compare the instructional effect quickly. The answer is correct when the selected contraction unit is the only intended variable and the surrounding text remains unchanged.

### Round 5

Restoring contracted UEB should return the document to the baseline translation. If it does not, inspect the Contraction Relaxer selections and confirm that the document's translation profile has not also been changed.

### Teacher decision rule

The best answer is not "use fewer contractions." The best answer is **"use the contractions that match the learner's current instructional target."** The NFB training materials establish the UEB contraction system; the current BrailleBlaster feature provides a practical way to differentiate a text without abandoning contracted UEB altogether.

---

## Key takeaways

- The Contraction Relaxer (**Tools > Contraction Relaxer**) allows selective suppression of individual contractions, distinct from both a document-wide uncontracted translation profile and a selection-level Uncontracted Translation toggle.
- It exists for targeted situations — a reader's current contraction-learning stage, or a specific term where contraction is causing confusion — not as a general-purpose formatting choice.
- Relaxing contractions increases the braille length of the affected text; that trade-off should be a conscious decision, not an incidental side effect.
- Document why a relaxer configuration was used, especially in agencies serving readers at different contraction-learning stages, so the reasoning survives being handed off to another transcriber later.

---

## Source Citations

- National Federation of the Blind, *Instruction Manual for Braille Transcribing — UEB Edition, 2015*, available from the NFB Braille Transcribing resources page.
