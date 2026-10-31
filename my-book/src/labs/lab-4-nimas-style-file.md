# Lab 4: A NIMAS-Style File, Start to Finish

**Time:** about 90 minutes. **Needs:** [Lesson 20](../lessons/20-nimas-production-files.md). **Files:** `nimas-style-sample.zip` from the [sample files](../samples/index.md). **Job aids:** the Import Log and the Production Checklist in [Job Aids](../reference/job-aids.md).

## Scenario

A publisher's NIMAS file has just arrived for a short science reader. NIMAS carries the *structure* of the book: headings, lists, page numbers, sidebars, captions, and math. It does not carry the printed page design. BrailleBlaster reads that structure and applies braille formatting to it, but you remain responsible for checking every decision.

> [!NOTE]
> The sample is a small **NIMAS-style** teaching file, not a validated NIMAC file set. See the note on the [Sample Files](../samples/index.md#nimas-style-set-lesson-20-lab-4) page. Real NIMAS files are best for authentic practice if your agency can supply one.

## What is inside the file

The sample contains:

- two chapters, with level-2 sections in the first;
- a three-item list, one item of which has a nested two-item list;
- three print page numbers;
- a sidebar titled "Did You Know?";
- a publisher production note;
- a MathML fraction inside a sentence;
- a figure with a caption.

Read this list first and **predict** how you expect each element to arrive in BrailleBlaster.

## Steps

1. **Open the file.** Use **File > Open** and choose the zip, or the XML file. NIMAS XML and NIMAS ZIP are both recognized file types.
2. **Navigate with the Book Tree.** Use it to jump between the two chapters, as [Lesson 20](../lessons/20-nimas-production-files.md) shows.
3. **Inspect the structure.** For each of the elements in the list above, find it in the Print View, then look at the Style View and Breadcrumbs. Does it have the style you predicted?
4. **Check the page numbers.** Find the print page indicators. Do they appear in the right places?
5. **Decide about the production note.** The official User Guide gives you tools for **publisher's production notes**. Decide whether this note is meant for the transcriber, the student, or neither, and whether to keep it, hide it, or remove it. Write down your reason.
6. **Check the math.** The guide says MathML in a NIMAS file is converted to ASCII Math and translated into your chosen math code. Read the Braille View for the fraction and confirm it is flagged as math.
7. **Handle the figure.** Find the image group and its caption. The caption is the *publisher's* text. Any description of the picture for the braille reader is *your* addition, and belongs in a Transcriber's Note ([Lesson 22](../lessons/22-transcribers-notes.md)). If the image file is present, think about how the Image Describer would help. (The sample references an image file that is not included, so you can practice the decision without the tool.)
8. **Check the sidebar.** Decide whether it is structurally a box and how it should look in braille ([Lesson 18](../lessons/18-advanced-formatting.md)).
9. **Remove print-only formatting.** The official guide notes that headings may be bold in the print file, but bold is not needed in braille. Check whether any heading carries emphasis that you should remove.
10. **Proofread.** Read the whole Braille View from start to finish.

## Record what you found

| Element | Predicted | Actual | What I changed |
| ------- | --------- | ------ | -------------- |
| Chapter titles | | | |
| Section headings | | | |
| Nested list | | | |
| Print page numbers | | | |
| Production note | | | |
| Sidebar | | | |
| MathML fraction | | | |
| Figure and caption | | | |

## Expected observations

A structured source should give you headings, a list, page indicators, and flagged math with far less manual work than a flat document, which is what [Lesson 20](../lessons/20-nimas-production-files.md) teaches. It should not give you a finished transcription. Expect to make decisions about the production note, the sidebar, the figure description, and heading emphasis.

## Going further: working in parallel

The official guide describes **dividing a NIMAS file into multiple files** so several transcribers can work on different chapters at once and then rejoin them. Ask your instructor whether your agency does this, and what rule it uses to keep styles consistent across transcribers.

## Debrief questions

1. What did BrailleBlaster decide *for* you, and what did it leave to you?
2. Which of the decisions would you want written into your agency's standards so every transcriber makes the same choice?
3. The production note was written by the publisher for someone else. What does that tell you about reading any note in a source file?
4. Who benefits when the publisher's NIMAS file is well built, and who pays when it is not?
