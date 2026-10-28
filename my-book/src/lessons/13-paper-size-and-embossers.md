# Lesson 13: Paper Size and Connecting an Embosser

> **Lesson at a glance**
>
> - **Unit:** Unit 1: Universal Lessons
> - **Suggested time:** about 3 hours
> - **Prerequisites:** [Lesson 1](01-navigating-the-interface.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Match the braille page geometry to the physical paper before transcribing.
- Set interpoint correctly and explain what it changes.
- Create and select an embosser profile, and tell **File > Print** from **File > Emboss**.
- Troubleshoot a bad emboss in a sensible order.

## Why this matters

Every other skill in this course produces a file on screen. This lesson is about turning that file into physical braille — or at least setting up the document so that it *can* be, correctly, the first time it reaches a real embosser. Getting page setup right before transcription begins saves enormous rework later, because page size, margins, and lines-per-page directly determine where BrailleBlaster places every page break in the finished document.

This lesson covers the basics every transcriber needs on day one: setting page properties and connecting a single embosser. [Lesson 13](13-paper-size-and-embossers.md) returns to embossing in more depth — multiple embosser profiles, advanced byte-level options, and troubleshooting a misbehaving device — once learners have more context for why those advanced options exist.

---

## How to use this lesson

The first half explains how page geometry and embosser configuration interact. The second half is a practice document — work through the scenarios and decide which setting belongs in BrailleBlaster before embossing. The goal is to avoid treating an embosser as a simple "Print" button.

---

## The Concept

### Braille page geometry must agree with the physical paper

BrailleBlaster's Page Properties control the document's page size, lines per page, cells per line, and margins. These values describe the geometry BrailleBlaster uses when laying out the braille.

The physical paper loaded in the embosser must be compatible with those assumptions.

A mismatch can cause:

- text to run beyond the physical page;
- unexpected page breaks;
- an embosser warning that the document is larger than the paper;
- wasted paper;
- a document that appears correct on screen but embosses incorrectly.

### Interpoint is a page-production setting

Interpoint embosses on both sides of the sheet. Single-sided embossing uses one side only. The document's page geometry and the embosser's physical capabilities must both support the selected mode.

### Connecting the embosser is separate from formatting the document

BrailleBlaster supports embossers from manufacturers including Index, Enabling Technology, Braillo, APH (PixBlaster and PageBlaster), IRIE, and ViewPlus. A generic manufacturer option is available when a model is not listed.

A teacher should understand the distinction:

- **Document settings** determine what BrailleBlaster intends to emboss.
- **Embosser settings** determine how that intended braille is sent to the physical device.
- **Paper settings** determine whether the physical sheet can accommodate the document geometry.

---

## Step by step in BrailleBlaster

### Basic Page Setup

1. Go to **Settings > Page Properties**.
2. Set **Page Size** to match your braille paper.
3. Set **Lines Per Page** and **Cells Per Line** — these, together with page size and margins, determine how much braille text fits on each page.
4. Set the four margins, choosing inches, cells, or lines as the unit.
5. Set **Interpoint** to Yes or No depending on your embosser and paper.
6. Click **OK** to apply to the current document, or **Make Default** to apply these settings to every future document as well.

### Connecting a First Embosser

1. Go to **Settings > Embosser Settings**.
2. Choose to add a new embosser profile.
3. In the Edit Embosser window, give the profile a **Name** you'll recognize later (useful once an agency has more than one embosser).
4. Choose the **Embosser Device** — the physical device as your computer sees it, from the dropdown of connected printers/embossers.
5. Choose the **Embosser Manufacturer**. If you don't know the manufacturer or the exact model isn't listed, choose **Generic**, and then the option that best matches the device: *Text only* (BrailleBlaster assumes the embosser itself already knows its page size, margins, and interpoint setting), *Text with margins* (BrailleBlaster adds the margin spacing itself, as extra characters in the braille stream), or *Graphics Embosser* (for embossers that support tactile graphics — currently the ViewPlus family, and still in beta).
6. Click **OK** to save the profile.

### Embossing a Document

1. Go to **File > Emboss** (`Ctrl+E`).
2. Choose the embosser profile, the number of copies, and the page range (All, or a specific range).
3. Click **OK** to send the job to the embosser, or **Cancel** to back out without embossing.

> **Note:** BrailleBlaster prints the *Print View* when you use **File > Print**, and embosses the *Braille View* when you use **File > Emboss** — these are two different output paths for two different audiences (a sighted proofreader vs. a braille reader), and it's easy for a new transcriber to reach for the wrong one when they mean "get this out of the computer."

---

## Worked Demonstration (small, fully correct)

Suppose a document is intended for standard 11.5-inch by 11-inch braille paper.

A sound setup sequence is:

1. Open **Settings > Page Properties**.
2. Confirm the page size and margins.
3. Confirm cells per line and lines per page.
4. Decide whether the job is single-sided or interpoint.
5. Open **Settings > Embosser Settings**.
6. Select the correct manufacturer and model when available.
7. Confirm that the embosser is connected and available to the computer.
    a. This is a good time to go to **File > Export > Save BRF/PEF**
    b. Verify this file has the correct number of characters per line and lines per page
8. Before producing a large job, emboss a short test.
9. Check the physical page against the expected margins and page numbering.
10. Only then run the full job.

The key verification is physical: **a correct Braille View is not a substitute for a test emboss.**

---

## Practice Document

### Scenario 1 — paper mismatch

```text
BrailleBlaster:
Page Size = 11.5 x 11 inches
Cells Per Line = 40
Lines Per Page = 25

Loaded paper:
8.5 x 11 inches
```

### Scenario 2 — correct paper, wrong interpoint assumption

```text
Document:
Interpoint = Yes

Embosser:
Configured for single-sided production
```

### Scenario 3 — unknown embosser

```text
Embosser:
Manufacturer = not listed
Model = not listed

BrailleBlaster:
Generic manufacturer is available.
```

### Scenario 4 — production job

```text
A 180-page textbook is ready to emboss.
The document has never been physically test-embossed.
```

---

## Answer Key

### Scenario 1

The page geometry is incompatible with the loaded paper. Change the document page settings or load the correct paper before embossing. Do not solve a physical paper problem by reducing text arbitrarily.

### Scenario 2

The document and embosser assumptions disagree. Confirm the desired production mode and configure the document and embosser consistently before starting the job.

### Scenario 3

Use the Generic manufacturer configuration when appropriate, with the available text-only or text-with-margins options. Test the output because a generic configuration is a compatibility fallback, not proof that every embosser-specific feature is supported.

### Scenario 4

Do not immediately emboss all 180 pages. Produce a short test, inspect the physical braille, verify page geometry, and then proceed.

### Production rule

**Paper → Page Properties → Embosser → Test → Full production.**

---

---

## Going further: managing embosser profiles

Once you can emboss a single job, the next skill is keeping several embossers and several paper setups under control without surprises.

### Profiles, Manufacturers, and Models

Every embosser BrailleBlaster can send a job to needs its own **profile**, managed under **Settings > Embosser Settings**. A profile bundles together: a **Name** you assign, the **Embosser Device** as your computer's operating system sees it, and the **Embosser Manufacturer** and **Model**, which together tell BrailleBlaster exactly how to format the outgoing braille stream for that specific hardware.

BrailleBlaster ships with built-in support for a substantial list of manufacturers and models, including APH's own PixBlaster and PageBlaster, ViewPlus Technologies' full line (EmBraille, Columbia, Delta, Premier, Elite, Emprint, SpotDot, Max, Cub, and Cub JR), IRIE devices, Index Braille's Basic-D, Everest-D, BrailleBox, and Fanfold lines, the extensive Enabling Technologies catalog (Phoenix, Cyclone, Trident, BookMaker, the Romeo and Juliet families, and more), and Braillo's 200/400/600/270 series. If your exact model isn't listed, or you're not sure which manufacturer entry matches your device, **Generic** is the recommended fallback, with three sub-options:

- **Text only** — for devices not covered by a specific driver; BrailleBlaster assumes page size, margins, and interpoint have already been configured on the embosser itself.
- **Text with margins** — the same idea, except BrailleBlaster adds the margin spacing itself as extra characters within the braille stream, rather than relying on the embosser's own settings.
- **Graphics Embosser** — for devices that support embossing tactile graphics alongside braille text; currently in beta, and currently supported specifically by the ViewPlus embosser family.

### Advanced Embosser Options

For the Generic **Text only** and **Text with margins** profiles specifically, an **Advanced** tab exposes low-level options that exist to work around quirks in how a particular device expects to receive data. These normally stay at their defaults, and are the kind of setting you'd typically only touch at the direction of technical support once a specific embosser problem has been diagnosed:

| Option                 | What It Controls                                                       |
| ---------------------- | ---------------------------------------------------------------------- |
| Add margins            | Whether margin spacing is added by BrailleBlaster (true/false)         |
| Pad page               | Whether the page is padded out (true/false)                            |
| Form feed on full page | Whether a form-feed character is sent when a page is full (true/false) |
| End of line            | The exact byte sequence sent at the end of each line                   |
| End of page            | The exact byte sequence sent at the end of each page                   |
| Header                 | A byte sequence sent before the document                               |
| Footer                 | A byte sequence sent after the document                                |

The byte-string fields (End of line, End of page, Header, Footer) accept most ASCII characters typed directly, plus a small set of escape sequences for characters that are awkward to type directly: `\\` for a literal backslash, `\r` for carriage return, `\n` for new line, `\t` for tab, `\f` for form feed, and `\x` followed by two hexadecimal digits for any arbitrary byte (`\x1b`, for instance, sends the byte commonly known as Escape).

### Managing Multiple Embosser Profiles

1. Go to **Settings > Embosser Settings** to see every profile currently configured.
2. To add a new profile, follow the same steps as [Lesson 13](13-paper-size-and-embossers.md): Name, Embosser Device, Manufacturer, and Model.
3. To switch which embosser a document goes to, choose the appropriate profile at emboss time — **File > Emboss** (`Ctrl+E`) presents a profile selector alongside copy count and page range, and profiles can also be managed on the fly from within that dialog via its **Manage Embossers** button.
4. Keep profile **Names** specific enough that a busy production floor with several embossers won't confuse them — including the physical location or purpose of the device in the name (for example, "Room 2 — Index Everest — Drafts") avoids a wrong-profile emboss.

### Troubleshooting Embosser Issues

When embossed output doesn't match expectations, work through the problem in this order, rather than guessing at random settings:

1. **Confirm the embosser configuration is actually correct.** Re-check the Manufacturer and Model selected in the profile against the physical device — it's a common mistake to select a visually similar but incorrect model from a long dropdown list.
2. **Try Generic Text Only support** as a diagnostic step. If a model-specific driver is producing bad output, temporarily switching the profile to Generic Text Only (with the embosser's own onboard settings governing page size, margins, and interpoint) isolates whether the problem is in BrailleBlaster's model-specific driver or somewhere else in the chain (cabling, the embosser's own settings, or the document itself).
3. **Tweak the Advanced embosser options** only after the first two steps haven't resolved the issue, and ideally with guidance from support or from documented values for your specific model — certain embosser families (Enabling Technologies devices and Index Braille devices among them) have documented recommended Advanced-option values for known compatibility quirks.

---

## Key takeaways

- Page setup lives in three related dialogs under **Settings**: Translation Settings, Page Numbers, and Page Properties.
- BrailleBlaster's page defaults (11.5" × 11" paper, 0.5"/0.5"/1.25"/0.48" margins) are a starting point, not a universal standard — confirm your agency's specifications.
- Interpoint controls single- vs. double-sided embossing.
- An embosser profile (Settings → Embosser Settings) is required before embossing; when the exact model isn't listed, Generic with Text only or Text with margins is the fallback.
- File → Print sends the Print View to a regular printer; File → Emboss (`Ctrl+E`) sends the Braille View to an embosser — these are not interchangeable.
- Each embosser needs its own profile under **Settings > Embosser Settings**, specifying Name, Device, Manufacturer, and Model.
- Generic (Text only, Text with margins, or Graphics Embosser) is the correct fallback when a specific model isn't listed or isn't known.
- Advanced embosser options (available for Generic profiles) control low-level byte-string behavior and should be treated as a last-resort troubleshooting tool, not a routine setting.
- When embossed output looks wrong, check the Manufacturer/Model selection first, try Generic Text Only as a diagnostic isolation step second, and only then consider Advanced options.
