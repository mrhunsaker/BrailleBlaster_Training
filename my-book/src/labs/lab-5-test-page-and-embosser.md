# Lab 5: Page Properties and the Test Emboss

**Time:** about 60 minutes. **Needs:** [Lesson 13](../lessons/13-paper-size-and-embossers.md). **Files:** `reflow-paragraph.txt` and `test-page-for-embosser.txt` from the [sample files](../samples/index.md). **Job aids:** the Embosser Profile Log in [Job Aids](../reference/job-aids.md). **Hardware:** an embosser is helpful for Part C, but Parts A and B work without one.

## Scenario

All your formatting work is wasted if the pages come out wrong. You are setting up a workstation for a new embosser and a new paper size, and your supervisor wants it tested, documented, and repeatable.

## Part A: Watch the text reflow

Page properties control where lines and pages break, so **set them before you transcribe**. Prove it to yourself.

1. Open a new document and paste in `reflow-paragraph.txt`.
2. Open **Settings > Page Properties** and note the current Page Size, Lines Per Page, Cells Per Line, and margins. Record them.
3. Open **File > Braille Preview** (`Alt+Home`). Note how many braille pages the paragraph occupies.
4. Return to **Settings > Page Properties**. Change the Cells Per Line (for example from 40 to 32) and click **OK**. Do not click **Make Default** yet.
5. Open the Braille Preview again and count the pages.
6. Repeat with a change to Lines Per Page, then with a different margin.

| Change | Pages before | Pages after |
| ------ | ------------ | ----------- |
| Cells per line | | |
| Lines per page | | |
| A margin | | |

> [!IMPORTANT]
> **OK** applies the changes to this document. **Make Default** applies them to *future* documents. Click **OK** while you are experimenting, and click **Make Default** only after you have confirmed that the values match your agency's standard.

**Expected observations.** Fewer cells per line or fewer lines per page should mean more pages for the same text, and the reverse should mean fewer. If your result is different, record what you see.

## Part B: Create and name an embosser profile

1. Go to **Settings > Embosser Settings** and add an embosser.
2. Fill in the **Name**, **Embosser Device**, **Manufacturer**, **Model**, and **Paper Size**.
3. Use the manufacturer-specific model if yours is listed. If you do not know the manufacturer, choose **Generic**.
4. The Generic choices differ: **Text only** assumes you set the page size, margins, and interpoint on the embosser itself. **Text with margins** adds spaces in the braille to create margins. **Graphics Embosser** is for models that support graphics, and the official guide describes it as beta.
5. Give the profile a **descriptive name** that says where it is, what it is, the paper, and the sides. For example: `Resource Room - Index Basic-D - 11.5x11 - Interpoint`.
6. Record the profile in the Embosser Profile Log.

## Part C: The test emboss (hardware needed)

1. Open a new document, paste in `test-page-for-embosser.txt`, and set the page properties to match the paper in the embosser.
2. Apply a heading style to the first line, and a list style to the three list lines.
3. Choose **File > Emboss** (`Ctrl+E`). Select your profile, one copy, and the page range.
4. Measure the left and right margins with a ruler or by counting cells. Check that the first line of the body paragraph and its runover lines start in the cells the Body Text style specifies (3-1).
5. Compare with the Braille View. If they differ, work through the troubleshooting order: the profile (manufacturer and model), then **Generic Text only** as a diagnostic, then advanced options.

> [!NOTE]
> Without an embosser, do Parts A and B, then use the Braille Preview to check the heading, list, body paragraph, and math line. Remember that a correct preview shows what BrailleBlaster *intends* to send. Only a real emboss shows what the device *does*.

## Part D: Print versus emboss

1. Open **File > Print** and look at the window. What does it print?
2. Open **File > Emboss**. What is different?

Say it in four words: **Print is for eyes. Emboss is for fingers.** **File > Print** sends the Print View to an ordinary printer. **File > Emboss** sends the braille to an embosser.

## Part E: A maintenance note

Add a line to the Embosser Profile Log saying when each profile should be rechecked. A sensible schedule is after a driver or firmware update, after any physical change to the embosser, and on a regular schedule such as once a term.

## Expected observations

- Changing page properties reflows the document.
- A profile needs a descriptive name, or nobody will pick the right one.
- A correct preview does not prove a correct emboss.

## Debrief questions

1. Why does "set page properties before you start" prevent so many headaches?
2. What can you tell from a test page that you cannot tell from a long document?
3. If a profile for a listed model gives odd output, why try Generic Text only?
4. Who should be allowed to change a shared profile, and how will everyone find out?
