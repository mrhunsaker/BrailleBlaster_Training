# Lesson 19: The eBraille Format

> **Lesson at a glance**
>
> - **Unit:** Unit 2: Advanced Lessons
> - **Suggested time:** about 60 minutes
> - **Prerequisites:** [Lesson 13](13-paper-size-and-embossers.md)
> - **You will need:** BrailleBlaster open and ready, and a way to copy text from this page.

## Learning objectives

By the end of this lesson you will be able to:

- Explain what eBraille is, who maintains it, and what problem it solves.
- Contrast a BRF with an eBraille publication.
- Describe how eBraille relates to the tag-based thinking behind NIMAS.
- Say why eBraille supplements and does not replace embossed braille.

## Why this matters

For decades the end product of braille transcription has been the **BRF** (Braille Ready File). A BRF is built around a fixed page: a set number of cells per line and lines per page, hard-coded for one paper size. That is exactly right for embossing a physical book. It is a poor fit for a refreshable braille display, especially the newer multiline displays, where the "page" is whatever the device can show, and that changes from device to device.

**eBraille** is the field's answer to that mismatch. It is worth understanding now, because it is arriving in production tools, and because its origin story runs directly through BrailleBlaster itself.

---

## How to use this lesson

This is a **concept lesson**. There is no click path to memorize, because export support depends on the version of BrailleBlaster you have installed. Read the sections, work through the three exercises at the end, and check your answers against the key.

> [!NOTE]
> eBraille is new and still being adopted. Check the Help menu and the release notes for your BrailleBlaster version to see which eBraille tools are available. The concepts below do not depend on any one menu.

---

## The Concept

### What eBraille is

eBraille is a digital braille reading format. It is standardized and maintained by the **DAISY Consortium**, and version 1.0 was released in August 2025. It was developed by the American Printing House for the Blind (APH) in partnership with DAISY and more than forty international partners.

Structurally, eBraille is built on an **EPUB 3-compatible file set**. It uses XHTML documents, CSS, and the same general web technologies that power e-books, instead of a flat, page-fixed stream of text. A packaged eBraille publication uses the file extension **`.ebrl`**, not `.epub`.

### Reflow is the key idea

Because eBraille content is marked up with semantic tags (this is a heading, this is a list, this is a footnote) and is not hard-coded into fixed lines and pages, a publication **reflows** to fit whatever display it is opened on. A 20-cell display, a 40-cell display, a single-line display, and a multiline display can all read the same file.

Unlike a BRF, an eBraille publication is not transformed on the fly by the reading device. It arrives already formatted according to the braille code rules of the region where it was produced, while keeping the flexibility to reflow.

### Where it came from

When BrailleBlaster opens a tagged NIMAS file ([Lesson 20](20-nimas-production-files.md)), it reads the publisher's print tags and maps them onto braille formatting. eBraille runs the same idea in the opposite direction: it applies tags to braille formatting itself, so the finished file stays meaningfully structured instead of being a flat grid of cells. Both formats rest on the same tag-based thinking, at opposite ends of the production pipeline.

### Distribution

An eBraille publication can be packaged as a single `.ebrl` file, unzipped onto a local file system, or deployed to the web. Because it shares its technology with the web, it can in principle be read in a standard web browser with the right screen reader or braille display support.

### Who supports it

Production tools including BrailleBlaster, Duxbury, and others have committed to supporting eBraille, and device support is developing for displays such as APH's Monarch and several single-line displays. A BRF-to-eBraille converter is part of the surrounding tooling, so existing BRF files do not have to be re-transcribed from scratch.

### What it does not do

eBraille does **not** replace BRF or embossed braille. It solves a different problem: reflowable digital reading on refreshable displays. Embossed, physical braille remains essential, and production workflows still depend on both.

### A comparison

| Question                      | BRF                                     | eBraille                                         |
| ----------------------------- | --------------------------------------- | ------------------------------------------------ |
| Built around                  | A fixed page for one paper size         | Structure that reflows to any display            |
| Underlying technology         | Plain braille text stream               | EPUB 3-compatible files (XHTML, CSS)             |
| File extension                | `.brf`                                  | `.ebrl` (packaged)                               |
| Best for                      | Embossing physical pages                | Reading on refreshable braille displays          |
| Keeps structure such as headings | Only through layout                  | Through tags                                     |
| Maintained by                 | A long-standing convention              | The DAISY Consortium                             |

---

## Practice

### Exercise 1: Explain it to a colleague

In one paragraph and in your own words, explain the practical difference between a BRF and an eBraille file to a colleague who has never heard of either. Avoid jargon. Then read your paragraph aloud and ask whether it would make sense to someone outside the field.

### Exercise 2: Choose the format

For each situation, say whether a BRF, an eBraille publication, or both are the better fit, and why.

1. A school needs a printed braille copy of a science textbook for a student who reads on paper.
2. A reader uses a multiline refreshable display and wants one file that fits any screen.
3. An agency wants to keep a long-term, structured copy of a title that it embosses on request.
4. A student switches between a 20-cell and a 40-cell display.

### Exercise 3: Look inside an eBraille file (optional)

If you can obtain a sample `.ebrl` file (see the DAISY eBraille page in the sources below), make a **copy** and give the copy a `.zip` extension. A packaged eBraille file is a zip container, like an EPUB. Extract it and open one of the XHTML files in a plain text editor.

1. Can you find a heading in the markup? What tag marks it?
2. Do you see hard line breaks at a fixed width, as you would in a BRF? Why or why not?
3. How does this differ from opening a BRF in a text editor?

### Answer Key

**Exercise 1.** A good answer says that a BRF is a finished set of fixed pages made for one paper size, ideal for embossing, while an eBraille file carries structure and reflows to fit whatever display the reader uses. Check that it does not say eBraille replaces BRF.

**Exercise 2.**
1. **BRF.** Embossing physical pages is exactly what the fixed-page format is for.
2. **eBraille.** Reflow to the device is its core purpose.
3. **Both.** Many agencies keep the structured file and produce a BRF for embossing when needed.
4. **eBraille.** The content reflows to whichever display is in use.

**Exercise 3.**
1. Headings appear as XHTML heading elements, such as `h1` or `h2`, because the format is built on EPUB 3-compatible web technology.
2. No fixed-width line breaks, because the content is not hard-wrapped to one paper size. Reflow happens at the reader.
3. A BRF is a stream of text arranged on fixed pages with no tags, so structure is visible only through its layout.

---

## Key takeaways

- eBraille is a DAISY Consortium standard (version 1.0, August 2025) for digital, reflowable braille reading, built on an EPUB 3-compatible file set and packaged as `.ebrl`.
- A BRF assumes one fixed page size. eBraille content reflows to fit whatever braille display it is opened on.
- Its core idea, applying structural tags to braille content, mirrors how BrailleBlaster already reads structural tags from NIMAS files, just in the opposite direction.
- eBraille supplements BRF and physical embossing. It does not replace them.

---

## Source Citations

- The DAISY Consortium, *eBraille 1.0* specification, at [daisy.github.io/ebraille/published/1.0/](https://daisy.github.io/ebraille/published/1.0/). It is the source for the EPUB 3 compatibility, the `.ebrl` extension, and the packaging rules.
- The DAISY Consortium, [eBraille standard overview](https://daisy.org/activities/standards/ebraille/). It is the source for release timing and the reflow description.
- American Printing House for the Blind, [Meet eBraille](https://www.aph.org/meet-ebraille/). It is the source for the development partnership.
