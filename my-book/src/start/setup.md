# Setup and Prerequisites

## What you need

- A computer that can run BrailleBlaster. At the time of writing, APH lists Windows, macOS, and Linux support. Check the [system requirements](https://brailleblaster.org/docs/systemRequirements.php) for current details.
- BrailleBlaster, installed and opened at least once.
- Working knowledge of literary braille (UEB).
- For [Lesson 13](../lessons/13-paper-size-and-embossers.md): access to an embosser and braille paper is helpful, but you can complete the lesson without one.
- For [Lesson 17](../lessons/17-what-pandoc-does.md): nothing extra. Pandoc works behind the scenes, and you do not need to install it to follow the lesson.

## Installing BrailleBlaster

1. Download BrailleBlaster from [brailleblaster.org/download.php](https://brailleblaster.org/download.php).
2. Choose an **installer** if you want automatic updates. Zip and tar packages are available too, but they must be updated by hand.
3. If you have BrailleBlaster 2.1 installed, **uninstall it before installing 3.x**. APH's 3.0 release notes call this out.
4. Open BrailleBlaster and confirm it starts with an empty Print View and Braille View.

BrailleBlaster has been open source under the GNU Public License since version 3.0.0 (March 2025). A community-maintained fork, BrailleBlaster-NG, also exists. This course follows the APH 3.x documentation. If you use BrailleBlaster-NG, check any menu path that does not match.

> [!NOTE]
> Version 3.2 added a Bookmark Window (**Navigate** menu) and an Insert Link window. Those tools are not part of the core lessons, but you may notice them in your menus.

## Prepare your workspace

1. Create a folder for the course, for example `BrailleBlaster-Training`.
2. Inside it, create subfolders: `sources`, `working`, and `output`.
3. Keep every original source file in `sources` and never edit it. Work on copies in `working`.
4. Save finished BRF files to `output`.

## Check your translation settings

Before the lessons that use math or special codes, look at the translation settings for your document. This course assumes **Unified English Braille (UEB)** for literary text, with Nemeth Code available for math ([Lesson 7](../lessons/07-math-translation-toggle.md)). BrailleBlaster also supports other codes. See the official documentation if your agency uses a different one.

## A quick readiness check

You are ready to start when you can say yes to all of these:

- [ ] BrailleBlaster opens and I can see a Print View.
- [ ] I can paste text into the Print View.
- [ ] I have a course folder with `sources`, `working`, and `output`.
- [ ] I know which braille code my agency or school uses.
