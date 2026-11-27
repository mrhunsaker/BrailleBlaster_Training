# Lesson 50: Embosser Operation and Maintenance

> **Lesson at a glance**
>
> - **Unit:** Unit 5: Handbook (Supplemental)
> - **Suggested time:** about 90 minutes
> - **Prerequisites:** [Lesson 13](13-paper-size-and-embossers.md), [Lesson 45](45-page-geometry-and-volume-sizing.md)
> - **You will need:** A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Run a pre-flight check before every emboss, and a short routine after.
- Choose, store, and load braille paper sensibly.
- Work through a bad emboss in a sensible order, from the profile to the hardware.
- Keep a maintenance log, and know when to stop and call the manufacturer or a technician.

> [!TIP]
> **Template:** the **Embosser Maintenance Log** and **Pre-Flight Checklist** are in the [Job Aids](../reference/job-aids.md) as Aid 12.

> [!CAUTION]
> Never reach into a powered embosser, bypass an interlock, or attempt an internal repair while the machine is energized. Follow the manufacturer's safety and maintenance instructions, and stop work when a fault requires a qualified technician.

## Why this matters

All the careful work in the earlier lessons ends at the embosser. A tired machine, damp paper, or a profile that does not match the paper produces braille that cannot be read, after hours of good formatting. The student's books are only as good as the last step.

This lesson gives a short, careful routine for the **transcriber** who operates an embosser. It is deliberately general.

> [!IMPORTANT]
> **The manufacturer's manual is the authority** for your model: how to load paper, what paper it takes, how to clean it, how often it needs service, and what its settings mean. Where this lesson and the manual disagree, **follow the manual**. This lesson does not replace training from your agency or the manufacturer.

{HB}

---

## How to use this lesson

Read **The Concept**, then adapt the **pre-flight checklist** to your machine and keep it by the embosser. The practice asks you to diagnose six faults in a sensible order.

---

## The Concept

### Three layers, checked in this order

When braille comes out wrong, the cause is in one of three layers. Check them **in this order**, because the cheapest to change comes first.

1. **The document.** Page properties, styles, and the Braille Preview ([Lessons 13](13-paper-size-and-embossers.md) and [45](45-page-geometry-and-volume-sizing.md)).
2. **The profile and the settings.** The embosser profile in BrailleBlaster, and the embosser's own paper size, margins, and interpoint settings.
3. **The hardware.** Paper, the embossing head, and the mechanism.

If the **Braille Preview** looks wrong, the problem is the document. If the preview looks right and the paper is wrong, the problem is the profile, the settings, or the machine.

### Paper

Braille paper is **heavier than ordinary paper** so that the dots stay raised. Things to know:

- **Use the paper the manufacturer approves.** Paper that is too thin tears or holds the dots poorly. Paper that is too thick jams.
- **Interpoint** needs paper that is suitable for dots on both sides.
- **Single sheets** and **continuous (fan-fold) paper** use different feeding paths. Many embossers take only one kind.
- **Store paper flat**, in a cool, dry place, away from damp and direct sun. Paper that has absorbed moisture jams and embosses poorly.
- **Let paper reach the room's temperature** before loading it, if it was stored somewhere very different.
- **Do not reuse** a sheet that has been embossed unless it is a test.

### The pre-flight check

Before every job:

1. **Right paper** loaded, **right way up**, and square.
2. **Profile selected** in BrailleBlaster, for this embosser and this paper.
3. **Interpoint setting** matches the document, on the embosser and in the page properties.
4. **Page properties** match the paper ([Lesson 13](13-paper-size-and-embossers.md)).
5. **The first page** goes out as a test, and you check the margins and the first line.
6. **Then** the full job.

### Safety

- **Embossers are loud.** Use the manufacturer's sound cover, if there is one, and consider hearing protection for long jobs.
- **Keep fingers, hair, and clothing away** from moving parts and the embossing head while the machine is on.
- **Unplug it before opening or cleaning** it, unless the manual says otherwise.
- **Do not use liquids or sprays** on the machine unless the manual allows them.

---

## Care and maintenance

Do **only what the manual tells you to do**. Routine care is usually:

| When | What |
| ---- | ---- |
| **Each use** | Check the paper path is clear. Look for torn scraps of paper |
| **Regularly** | Remove dust from the outside and the paper path, as the manual describes |
| **After a jam** | Clear it as the manual describes, and run a test page before the real job |
| **When the manual says** | Replace parts, lubricate, or calibrate. Some embossers need this, and many do not |
| **After a driver or firmware update, or a physical change** | Recheck every profile ([Lab 5](../labs/lab-5-test-page-and-embosser.md)) |
| **Once a term** | Run a standard test page and keep it as a record |

**Never open the machine** beyond what the manual allows, and **never touch the embossing head** with your fingers.

### Keep a log

A maintenance log answers the question a technician always asks: *what happened, and when?* Record every service, every jam, every change of paper type, and every update. The template is in the Job Aids.

---

## Troubleshooting

Work down the list for the symptom, and **stop and call for service** if the cause is in the hardware.

| Symptom | Check, in this order |
| ------- | -------------------- |
| **Nothing embosses** | Power and cable; the right profile and port; that the job reached the embosser; the embosser's online or ready state |
| **Lines wrap in the wrong place** | The Braille Preview; the cells per line; the embosser's margins and paper size; **Add margins** ([Lesson 45](45-page-geometry-and-volume-sizing.md)) |
| **The first line is too low, or a page breaks early** | Lines per page; the embosser's top margin; **Pad page** and **Form feed on full page** |
| **Braille on only one side of an interpoint job** | The interpoint setting on the embosser and in Page Properties |
| **Dots are faint** | The paper (too thin or damp); any dot height or embossing pressure setting your model has; then service |
| **Dots tear the paper** | The paper (too thin); the same setting; then service |
| **Paper jams** | The paper (damp, curled, or wrong kind); the loading; the paper path. Clear it by the manual |
| **Odd characters, or garbled braille** | The **manufacturer and model** in the profile; try **Generic, Text only** as a test ([Lesson 13](13-paper-size-and-embossers.md)) |
| **Everything is right in the preview but wrong on paper** | The profile and the embosser's own settings, then the hardware |

> [!NOTE]
> **Missing dots, uneven dots, or a noise that was not there before** point to a worn or damaged embossing head or mechanism. Stop embossing, record it, and call the manufacturer or an authorized technician. Do not try to repair it.

---

## Step by step

### Emboss a job

1. Run the **pre-flight check**.
2. In BrailleBlaster, choose **File > Emboss** (`Ctrl+E`), select the profile, the number of copies, and the page range.
3. **Emboss the first page only.** Check the margins and the first line against the Braille Preview.
4. If it is right, emboss the rest. Stay nearby for the first minutes.
5. When done, **remove the pages promptly** and handle them by the edges, and check **the first page, a middle page, and the last page** for quality.
6. **Log** anything unusual.

### After a bad emboss

1. **Stop** the job.
2. **Look** at the paper, and describe the fault in one sentence.
3. **Find the symptom** in the troubleshooting table, and work down it.
4. Run a **test page** after every change.
5. **Log** the fault and what fixed it.

---

## Practice

### Tasks

For each fault, say which layer you check first, and the first three checks.

1. The braille on every page starts two lines lower than in the Braille Preview.
2. Dots are faint on a new ream of paper.
3. The first page is right, and every page after it is shifted one cell to the right.
4. An interpoint job comes out single-sided.
5. The machine jams at the same point on every sheet.
6. After a firmware update, every profile embosses with the wrong margins.

### Answer Key

1. **The profile and the embosser's settings.** Check the top margin on the embosser, **Lines per page** and the paper size in Page Properties, and the **Pad page** and **Add margins** options.
2. **The paper first**, then the settings. Check that the paper is the kind the manufacturer approves and that it is not damp. Check any dot-height or pressure setting your model has. If both are right, call for service.
3. **The document and the profile.** Check the Braille Preview for the same shift. Then check the left margin on the embosser and in Page Properties, and whether **Add margins** is on. A shift that begins after the first page may be a **form feed** or **Pad page** setting.
4. **The profile and the embosser.** Check the **interpoint** setting on the embosser and in **Settings > Page Properties** and in the page numbers setting.
5. **The hardware.** Check the paper path for scraps and the paper for curl or damp. Clear it as the manual says. If it repeats at the same point, there may be damage, so stop and call for service.
6. **Every profile.** A firmware update can reset the embosser's settings, so recheck each profile against a test page ([Lab 5](../labs/lab-5-test-page-and-embosser.md)), and log the update.

---

## Key takeaways

- **The manufacturer's manual is the authority.** This lesson does not replace it.
- Check **three layers in order**: the document, the profile and settings, then the hardware.
- Use **approved paper**, store it **flat and dry**, and always run a **first-page test**.
- Safety: **loud machine, moving parts, unplug before opening**.
- Keep a **log**, recheck profiles after updates, and **stop and call for service** when the cause is mechanical.

---

## Source Citations

- BrailleBlaster User Guide (the 3.x documentation), at [aphtech.github.io/brailleblaster-docs](https://aphtech.github.io/brailleblaster-docs/): "Setting up an Embosser" and "Printing and Embossing."
- Embosser manufacturers' manuals, which are the authority for each model.
- [Lessons 13](13-paper-size-and-embossers.md), [45](45-page-geometry-and-volume-sizing.md), and [Lab 5](../labs/lab-5-test-page-and-embosser.md).
