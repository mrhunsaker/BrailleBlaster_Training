# Lesson 27: Images and Tactile Graphics

> **Lesson at a glance**
>
> - **Unit:** Unit 4: Specialized Content
> - **Suggested time:** about 90 minutes
> - **Prerequisites:** [Lesson 4](04-layout-styles.md), [Lesson 22](22-transcribers-notes.md), [Lesson 26](26-controlling-the-page.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Reserve space for a tactile graphic with the Image Placeholder (**Insert > Image Manager**).
- Attach an image file and alt text to a placeholder, and update it later.
- Apply the **Caption** and **Description** styles correctly, and explain why the whole item must be selected first.
- Decide which images need a description, a tactile graphic, or neither.
- Plan the facing-page and blank-page needs of a tactile graphic in an interpoint volume.

## Why this matters

Almost every textbook has images, and braille readers are entitled to the information they carry. An image can become a **description** (words), a **tactile graphic** (raised lines and shapes), or both. BrailleBlaster does not decide this for you. What it does is leave the right amount of space, tie an image file to that space, and apply the styles that keep the print caption separate from your description.

This lesson teaches the tools and, more importantly, the decisions behind them.

---

## How to use this lesson

Read **The Concept**, then **Step by step**. The practice uses a figure described in words, because the point is the workflow. If you have a small image file on your computer, you can also practice attaching it.

---

## The Concept

### What is the image for?

Before choosing a tool, ask what job the image does:

- **It carries information the text does not.** A map, a graph, a diagram with labels. The reader needs this, so give a description, a tactile graphic, or both.
- **It illustrates what the text already says.** A photograph of a thing the paragraph describes. A short description may be enough, or the agency's rules may allow omitting it.
- **It is decoration.** A border, a logo, a stock photo. Check your agency's rules, but decoration generally does not need a graphic.

> [!NOTE]
> Describe what the image **shows**, not what you think it means. Keep descriptions objective, and leave interpretation to the reader and the teacher.

### Caption and description are different things

- The **caption** is the **print author's** text under or beside the image. BrailleBlaster has a **Caption** style for it (7-5 margins). The Caption style does *not* add Transcriber's Note indicators. Add them if your rules call for them.
- A **description** is the **transcriber's** text. BrailleBlaster has a **Description** style (7-5 margins) that **automatically** wraps the description in Transcriber's Note indicators. Because the style adds the indicators, you must **highlight the entire item first**, so the indicators fall in the right places.

The distinction matters. A reader must always know whether words came from the author or from the transcriber ([Lesson 22](22-transcribers-notes.md)).

### What BrailleBlaster does with images

- The **Image Placeholder** inserts **blank lines** at the cursor, so that a graphic can be added later. The number of lines must be less than the number of lines on a braille page.
- You can also **attach an image file** to the placeholder and give it **alt text**. When you attach an image, the braille and the graphic can be embossed together on a supported embosser. At present, the guide says that only **ViewPlus graphics embossers** are supported, with more planned.
- When a **NIMAS** file contains an image group with alt text, BrailleBlaster turns that alt text into a **Transcriber's Note** when it imports the file. The test files for BrailleBlaster describe this as a block with 7-5 margins. You still need to check that it reads well.

---

## Step by step

### Reserve space for a graphic

1. Place the cursor where the graphic belongs. The blank lines are inserted *before* the cursor.
2. Go to **Insert > Image Manager**. The window is titled "Insert Image Placeholder".
3. In the **Number of lines** box, type the number of lines you need. It must be **less than the number of lines on a braille page**. In the default setup that means fewer than 25.
4. (Optional) Click **Select Image**, choose a file, and the path appears. Type **Alt Text** for the image.
5. Click **Insert**, or **Cancel** to leave without changing anything.

### Edit an existing placeholder

Place the cursor in the placeholder and open **Insert > Image Manager** again. The window shows the saved number of lines, path, and alt text, and the button now reads **Update**.

### Apply caption and description styles

1. **Highlight the entire item**: the whole caption, or the whole description.
2. Open the **Styles** menu and find **Caption Styles**.
3. Choose **Caption** for the print caption, or **Description** for yours.

### Plan the page

A tactile graphic usually needs its own space on the page. In an interpoint volume, it often needs to face its text, or sit on a page with nothing on the back. Use the tools from [Lesson 26](26-controlling-the-page.md): **Page Side** to keep it on a given side, and **New Pages Before** and **New Pages After** for blank pages.

---

## Worked Demonstration

```text
Figure 3.1 A roller coaster at the top of a hill and at the bottom.
```

1. Paste the line. This is the **print caption**. Highlight the whole line and apply the **Caption** style.
2. Place the cursor at the start of the caption and go to **Insert > Image Manager**. Enter **12** lines and click **Insert**. Look at the Braille View: twelve blank lines should appear before the caption.
3. Below the caption, type your description:

   *A diagram of a roller coaster track. At the left, the track climbs to a high peak. It then drops steeply to a low point at the right. A small car is shown at the top of the first hill.*

4. Highlight the **whole** description and apply the **Description** style. Check the Braille View. Notice that transcriber's note indicators appear around it.
5. Reopen **Insert > Image Manager** with the cursor in the placeholder, change the number of lines to **14**, and click **Update**.

---

## Practice Document

### Print Source Legend

| Item | In print |
| ---- | -------- |
| Figure 1 | A bar chart of rainfall by month, with a printed caption, and a number on each bar |
| Figure 2 | A photograph of a pond, with a caption |
| Figure 3 | A decorative leaf border at the top of each page |
| Figure 4 | A labeled diagram of a plant cell with eight labeled parts |

```text
Figure 1 Rainfall by month, January to April.
Figure 2 A pond in early spring.
Figure 4 The parts of a plant cell.
```

### Tasks

1. For each figure, decide: **description only**, **tactile graphic and description**, or **omit**. Give one reason each.
2. Paste the three caption lines. Apply the **Caption** style to each.
3. For Figure 1, reserve **16** lines. For Figure 4, reserve **20**. Check each in the Braille View.
4. Write a Description for Figure 1 that reports the four values and the trend without interpreting them. Apply the **Description** style to the entire item.
5. Try to reserve **60** lines, more than a page. What does BrailleBlaster do or say?
6. Plan Figure 4 for an interpoint volume: which options from [Lesson 26](26-controlling-the-page.md) would you consider, and why?

### Answer Key

1. **Figure 1** (the chart): a description with the values, plus a tactile graphic if your service provides them, because the reader needs the data. **Figure 2** (the photograph): a short description, or omission if your agency's rules allow, depending on whether the photograph carries information the text lacks. **Figure 3** (the border): **omit**, because it is decoration, and a Transcriber's Note is not necessary unless your rules require one. **Figure 4** (the diagram): a **tactile graphic with a description** is the strongest answer, because the labeled parts are the content.
2. Each caption line, selected in full, takes the **Caption** style (7-5 margins), and no transcriber's note indicators are added by the style.
3. Sixteen and twenty blank lines should appear before the captions. Both are under the number of lines per page.
4. A good description names what the figure is and reports the four values in order and any visible trend (for example "rainfall is highest in the second month"), but does not add causes or opinions. The Description style wraps it in transcriber's note indicators, so you should **not** type the indicators yourself.
5. The number of lines must be fewer than the lines on a braille page, so a value that large is not accepted. Use a smaller number, and plan the graphic on its own page with **New Pages Before** and **New Pages After** if it is taller than one page's worth of space.
6. Consider **Page Side** to put the graphic on a chosen side so that it faces its text, and **New Pages Before** or **After** if it needs a page to itself. Check the Braille Preview after each change.

---

## Key takeaways

- Decide what the image is *for* before choosing a tool.
- **Insert > Image Manager** reserves blank lines (fewer than a page), can attach an image file, and stores alt text.
- A **caption** is the author's, and a **description** is the transcriber's. The **Description** style adds Transcriber's Note indicators for you, so highlight the whole item first.
- A NIMAS image group's alt text becomes a Transcriber's Note on import. Check that it is a good description.
- At present, only ViewPlus graphics embossers are supported for embossing graphics and braille together.

---

## Source Citations

- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/) and the source repository [github.com/aphtech/brailleblaster-docs](https://github.com/aphtech/brailleblaster-docs): "Working with Tactile Graphics" and "Caption Styles."
- The BrailleBlaster source code, `ImagePlaceholder.kt` (the Insert Image Placeholder window) and the `ImageGroupImportFixer` test (alt text becoming a Transcriber's Note).
- Braille Authority of North America, *Braille Formats: Principles of Print-to-Braille Transcription, 2016*, at [brailleauthority.org/formats/formats2016.html](https://www.brailleauthority.org/formats/formats2016.html).
