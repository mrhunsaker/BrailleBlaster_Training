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
- Use **Tools > Contraction Relaxer** to set how far through a contraction sequence a document goes, by choosing a unit.
- Tell the Relaxer (a document-level, instructional tool) apart from **Tools > Change Translation** (a selection-level tool): Uncontracted with `Ctrl+Shift+T`, and Direct with `Ctrl+D`.
- Use Direct translation and the No Translate text attribute where they fit.
- Apply a teacher decision rule and document which unit you chose and why.

> [!TIP]
> **More practice:** [Lab 7: Choosing the Right Translation Control](../labs/lab-7-relaxation-plan.md) and the [Translation Control Plan job aid](../reference/job-aids.md).

## Why this matters

Standard literary braille (Unified English Braille, Grade 2) uses contractions extensively — single cells or short cell combinations standing in for common letter groups and whole words, which is what makes contracted braille meaningfully more compact than an uncontracted, letter-for-letter transcription. Most of the time, an agency's translation table setting handles this globally and correctly, with no per-document intervention needed. But contractions can occasionally cause real problems for a specific reader or a specific kind of material — an emerging reader still learning contractions, unfamiliar technical vocabulary where contraction boundaries could be confusing, or specific words where the contracted form happens to be more ambiguous than useful. The **Contraction Relaxer** exists for exactly this situation: finer control than an all-or-nothing switch between contracted and uncontracted braille.

---

## How to use this lesson

The first half explains the concept from a teacher's perspective. The second half is a practice document: copy the "Practice Story" block into BrailleBlaster and produce several instructional versions of it by choosing different units in the **Contraction Relaxer**. The point is not to produce a universally "better" braille file. It is to practice matching a text to what a particular learner has been taught.

---

## The Concept

### Contracted UEB is not an all-or-nothing instructional decision

The NFB's 2015 *Instruction Manual for Braille Transcribing, UEB Edition* teaches contractions as a systematic part of UEB rather than as arbitrary shortcuts. For teachers for students with visual impairments (TVI) or a school-based braille transcriber, however, the practical question is often different from the transcriber's question: **Which contractions should this particular student be reading right now?**

BrailleBlaster's **Contraction Relaxer** provides a way to make that instructional adjustment without hand-editing the braille. You choose a *unit* of a contraction-teaching sequence, and BrailleBlaster translates the document with the contractions taught up to and including that unit, and no others. The choices run from **Fully Uncontracted (Grade 1 UEB)** at one end to **Fully Contracted (Grade 2 UEB)** at the other.

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

In BrailleBlaster, a document starts fully contracted. *Relaxing* means choosing a lower unit so that contractions the learner has not yet been taught are written out letter by letter instead. The print word does not change. The learner's reading task changes, because the braille spells out more of each word.

The dialog says it plainly: "Select a unit to toggle specific translation rules. This will allow you to specify words and contractions up to and including the selected unit." So the unit you choose is the **last unit your learner has been taught**, and every earlier unit is included too. The tool is **cumulative**, which is why you do not pick the units to switch off. You pick the unit to stop at.

### Relaxer, Change Translation, and Translation Settings

Three controls look alike but work at different levels. Mixing them up is the most common mistake with this lesson.

| Control | Works on | How you use it | Shortcut |
| ------- | -------- | -------------- | -------- |
| **Settings > Translation Settings** | The whole document's code and grade | Choose a braille code such as UEB, or UEB Uncontracted | None |
| **Tools > Contraction Relaxer** | The whole document, by teaching unit | Choose a unit from the drop-down and click OK | None |
| **Tools > Change Translation** | The text you have selected | Choose **Uncontracted** or **Direct** | `Ctrl+Shift+T` (Uncontracted), `Ctrl+D` (Direct) |

Use the Relaxer when a *learner's contraction sequence* decides the answer. Use Change Translation when a *passage* needs special handling, such as computer code or a string that must appear exactly as typed. [Lab 7](../labs/lab-7-relaxation-plan.md) practices both.

### A note about the 2015 NFB materials and current BrailleBlaster

The NFB 2015 manual is a UEB training resource; the Contraction Relaxer is a later BrailleBlaster feature. This exercise therefore combines two layers deliberately:

1. **UEB knowledge from the 2015 training:** recognize what contractions are doing in the words.
2. **Current BrailleBlaster workflow:** use the Contraction Relaxer to choose how much of the contraction sequence a document uses, for an instructional purpose.

Do not treat the current tool's interface as if it were part of the 2015 manual.

---
## The Old, Hard Manual way

For this example, I am going to manually apply the contraction for "day" into the following block of text. 

``` 
Today is the greatest day I've ever known.
```

For the sake of simplicity and argument, I am going to go into the **Tools > Contraction Relaxer** Menu and selecting "Fully Uncontracted (Grade 1 UEB)".

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

Paste the following into the print view. Then go to **Tools > Change Translation > Uncontracted**, select the entire text and press `CTRL+SHIFT+T`, or go to **Tools > Contraction Relaxer** and choose **Fully Uncontracted (Grade 1 UEB)**. 
```
today forever forefather here knows landlord motherlode namely honest party questions bright wholesome primetime underground workout younger therefore characteristic throughout whereafter bought
```
Practice using the find and replace menu to translate the dot 5 initial letter contractions embedded in the pasted words. It feels odd at first, but with practice the process comes to feel more natural. 

## Step by step

### Using the Contraction Relaxer

1. Go to **Tools > Contraction Relaxer**. A dialog opens.
2. Read the instruction at the top: it lets you specify words and contractions *up to and including* the unit you select.
3. Open the drop-down list. It offers, in order:
   - **Fully Uncontracted (Grade 1 UEB)**
   - **Unit 2:** Alphabetic wordsigns
   - **Unit 3:** Strong contractions *and, for, of, the, with*
   - **Unit 5:** Shortform words *ab, ac, af, ag, al, bl, ei, fr, ll*
   - **Unit 6:** Strong groupsigns, wordsigns, and shortforms *ch, sh, th, wh, ou, st*
   - **Unit 7:** Strong groupsigns and shortforms *ar, ed, er, gh, ow, ing*
   - **Unit 9:** Dot 5 initial-letter contractions
   - **Unit 11:** Two-cell punctuation and shortform words
   - **Unit 12:** Initial-letter contractions for dots 4-5 and 4-5-6
   - **Unit 14:** Lower wordsigns *his, was, were, be, in, enough*
   - **Unit 15:** Lower groupsigns *be, con, dis, ea, bb, cc, ff, gg, in, en*
   - **Unit 17:** Final-letter groupsigns
   - **Fully Contracted (Grade 2 UEB)**
4. Choose the **last unit your learner has been taught**.
5. Click **View Contractions** if you want to see the list of contractions the choice allows.
6. Click **OK** to apply it, or **Cancel** to leave without changing anything.
7. BrailleBlaster records your choice in the document's translation-corrections file, sets the translation to UEB Uncontracted (or to UEB Grade 2 if you chose Fully Contracted), and refreshes the document. Check the Braille View.

The Relaxer has no keyboard shortcut. It remembers your last choice, so the drop-down opens on the unit you used before.

> [!NOTE]
> The dialog's unit numbers follow a published contraction-teaching sequence. Units 4, 8, 10, 13, and 16 are not offered. Units that deal with math signs, modes, and typeform indicators are handled differently from text contractions. Match your learner's actual program to the units listed and record which unit you chose.

### Using Change Translation for a selection

1. Select the text.
2. Go to **Tools > Change Translation**, use the Change Translation toolbar button, or right-click and choose **Change Translation**.
3. Choose **Uncontracted** (`Ctrl+Shift+T`) for grade 1 braille without contractions. The selection is highlighted in green in the Braille View.
4. Or choose **Direct** (`Ctrl+D`) for the literal ASCII translation. The selection is highlighted in purple in the Print View. Use Direct when you must force a particular result that BrailleBlaster would not otherwise allow.

> [!IMPORTANT]
> Because the Relaxer changes the document's translation setting and writes to its translation-corrections file, treat every Relaxer choice as a deliberate, documented decision for a specific document or reader. Keep a record of the unit and the reason beside the file, so a later transcriber understands why the braille looks the way it does.

---

## Worked Demonstration using Contraction Relaxer (small, fully correct)

```text
The teacher will help the child read the book before the class begins.
```

Suppose a learner has been taught through Unit 3 (the strong contractions *and, for, of, the, with*) but has not yet met the later units.

1. Paste the sentence and translate it fully contracted. Read the Braille View as the baseline.
2. Open **Tools > Contraction Relaxer** and choose **Unit 3: Strong contractions and, for, of, the, with**. Click **OK**.
3. Read the Braille View again. Contractions from Units 2 and 3 should still appear, so *the* is still written as a single contraction. Contractions from later units, which the learner has not met, should now be written out letter by letter.
4. Choose **Fully Uncontracted (Grade 1 UEB)** and compare. Even *the* is now spelled out.
5. Choose **Fully Contracted (Grade 2 UEB)** to restore the baseline, and check that the braille matches step 1.
6. Record the unit, the date, and the reason.

The important distinction is between **"uncontracted"** and **"partly contracted to a unit."** The second keeps more of the normal UEB reading environment while limiting the contraction burden to what the learner has been taught.

---

## Practice Document: "Herbert and the Magic Eggs"

### Practice instructions

Copy the passage below into BrailleBlaster.

For each round, use the Contraction Relaxer to create a different instructional version:

- **Round 1: Fully Contracted.** Choose **Fully Contracted (Grade 2 UEB)** and make no other change. This is your baseline.
- **Round 2: Fully Uncontracted.** Choose **Fully Uncontracted (Grade 1 UEB)**. This is the no-contraction extreme.
- **Round 3: A beginning-reader version.** Choose a unit for a learner who has been taught only the earliest contractions (for example Unit 3). Record the unit you chose and why.
- **Round 4: A later-stage version.** Choose a unit for a learner who has been taught more (for example Unit 9). Compare it with Round 3 and note which words changed.
- **Round 5: Restore and compare.** Choose **Fully Contracted** again and confirm the Braille View matches Round 1.

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

**Fully Contracted (Grade 2 UEB).** No contraction units are held back. The purpose is to establish the baseline against which the instructional versions can be compared.

### Round 2

**Fully Uncontracted (Grade 1 UEB).** Every contraction is written out. The purpose is to establish the no-contraction extreme.

### Round 3

There is no single correct unit without knowing the learner's instructional history. A defensible record identifies:

- the unit chosen (remember that earlier units are included automatically);
- why the learner's program has reached that unit and no further;
- whether the choice applies to the whole passage or only to this lesson;
- whether the result was checked in the Braille View.

### Round 4

A higher unit should allow more contractions than the unit in Round 3, so more words should look like ordinary contracted UEB. The comparison is correct when the *unit* is the only variable and the surrounding text is unchanged.

### Round 5

Choosing Fully Contracted again should return the document to the baseline. If it does not, open **Settings > Translation Settings** and confirm that the document's translation has not been changed some other way, for example by an earlier Uncontracted setting.

### Teacher decision rule

The best answer is not "use fewer contractions." The best answer is **"use the contractions that match the learner's current instructional target."** The NFB training materials establish the UEB contraction system; the current BrailleBlaster feature provides a practical way to differentiate a text without abandoning contracted UEB altogether.

---

## Key takeaways

- The Contraction Relaxer (**Tools > Contraction Relaxer**) is a **document-level instructional tool**. You choose a teaching unit, and the document uses the contractions taught up to and including that unit.
- It is **cumulative**. Choose the *last unit the learner has been taught*, not the units to switch off. It has no keyboard shortcut.
- **Tools > Change Translation** is the selection-level tool: Uncontracted (`Ctrl+Shift+T`, green in the Braille View) and Direct (`Ctrl+D`, purple in the Print View).
- Relaxing contractions makes the affected text longer in braille. Make that trade-off on purpose.
- Document the unit and the reason, so the reasoning survives a hand-off to another transcriber.

---

## Source Citations

- National Federation of the Blind, *Instruction Manual for Braille Transcribing — UEB Edition, 2015*, available from the NFB Braille Transcribing resources page.
