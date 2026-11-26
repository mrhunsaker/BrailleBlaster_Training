# Glossary

**ASCII Math** is a compact linear text notation for equations. BrailleBlaster uses it as the intermediate form for math before translating into a braille math code. See [Lesson 8](../lessons/08-ascii-math-hub.md).

**BANA** is the Braille Authority of North America, publisher of *Braille Formats 2016*, the standard that BrailleBlaster's styles follow.

**BBX** is BrailleBlaster's default save format, a BrailleBlaster XML file.

**BBZ** is a zipped NIMAS file set. Saving a NIMAS ZIP produces a BBZ, which keeps the images with the document.

**Body Text** is the default style: an indented paragraph with 3-1 margins. Pasted text arrives as Body Text.

**Braille ASCII** is the character set used in BRF files. It maps each of the 64 six-dot braille patterns to a printable ASCII character, so braille can travel as text. For the letters *a* to *z* it is the capital letter. See [Lesson 41](../lessons/41-text-encoding-and-braille-characters.md).

**Braille Formats 2016** is the BANA reference standard for braille layout: margins, headings, lists, typeforms, tables, and more.

**Braille Preview** shows the document as it would appear when embossed, in 2 Page View. See [Lesson 1](../lessons/01-navigating-the-interface.md).

**Braille View** shows the braille translation of the document as you work.

**Breadcrumbs** is a bar that lists every style wrapping the text at the cursor, outermost container first.

**BRF (Braille Ready File)** is a fixed-page, embosser-ready braille file. It is the traditional end product of a transcription.

**Byte-order mark (BOM)** is the invisible character U+FEFF, written as the bytes `EF BB BF` at the start of some UTF-8 files. See [Lesson 41](../lessons/41-text-encoding-and-braille-characters.md).

**Cell-5 heading** and **Cell-7 heading** are block headings that start in cell 5 or cell 7. See [Lesson 5](../lessons/05-heading-levels.md).

**Centered heading** is the highest-level block heading format, centered on the line.

**Checksum** is a short fingerprint of a file's contents, used to confirm that two copies are identical. See [Lesson 49](../lessons/49-file-management-and-student-privacy.md).

**Container style** is a style that holds several elements as one unit, such as a List, Poetry, or Box. Breadcrumbs mark it with the word CONTAINER.

**Contraction Relaxer** is a tool for selectively reducing contractions, usually for instruction. See [Lesson 11](../lessons/11-contraction-relaxer.md).

**Debug menu** is a menu in BrailleBlaster 3.x that is hidden until you press `Ctrl+Shift+` ` . In the source examined it holds the TOC Builder, T-Page Generator, Volume Manager, and Alphabetic Reference tools.

**Direct translation** passes selected text through as ASCII braille instead of applying the UEB translation.

**DTBook** is the XML vocabulary used for the content files of a NIMAS file set. See [Lesson 38](../lessons/38-dtbook-nimas-and-mathml.md).

**eBraille** is a reflowable, EPUB 3-compatible digital braille format maintained by the DAISY Consortium. See [Lesson 19](../lessons/19-ebraille.md).

**Embosser profile** is a saved configuration that tells BrailleBlaster which device to send braille to and how to handle margins.

**Intake ticket** is a short form that travels with a job from request to delivery, recording the reader, source, code, format, and estimate. See [Lesson 48](../lessons/48-job-intake-and-the-agency-style-sheet.md).

**Interpoint** is double-sided embossing, producing braille on both sides of the page.

**Liblouis** is the open-source translation engine BrailleBlaster uses to turn text into braille.

**Lua writer (`bbx.lua`)** is BrailleBlaster's own script that turns the structure Pandoc reads into BrailleBlaster's XML. What it does not recognize is dropped. See [Lesson 33](../lessons/33-what-makes-a-good-source.md).

**Math Translation Toggle** (`Ctrl+M`) marks selected text for math translation instead of literary translation.

**MathML** is an XML vocabulary for mathematics. *Presentation MathML* describes how an equation is laid out. See [Lesson 38](../lessons/38-dtbook-nimas-and-mathml.md).

**Namespace** is an address that says which vocabulary an XML element belongs to. See [Lesson 37](../lessons/37-reading-xml.md).

**Nemeth Code** is a braille code for math and science notation. It can be the primary math code or be embedded in UEB with Nemeth Block and Inline indicators.

**NIMAS** is the National Instructional Materials Accessibility Standard, an XML-based source format for accessible instructional materials. See [Lesson 20](../lessons/20-nimas-production-files.md).

**No Translate** is a text attribute that tells BrailleBlaster not to translate the marked text.

**OCR (optical character recognition)** turns a picture of text into text, with characteristic errors. See [Lesson 42](../lessons/42-pdfs-scans-and-ocr.md).

**Package** is a zip file with a map. DOCX, ODT, EPUB, eBraille, BBZ, and NIMAS zips are all packages. See [Lesson 39](../lessons/39-inside-the-packages.md).

**Pandoc** is an open-source document converter that underlies part of BrailleBlaster's support for formats such as LaTeX. See [Lesson 17](../lessons/17-what-pandoc-does.md).

**P-page** and **T-page** are page-number types for preliminary pages and transcriber-generated pages, distinct from Normal numbering.

**Print View** is the view where you type, paste, and edit the text.

**Production note** is a publisher note in a NIMAS file, intended to help with physical production, which you may keep, hide, or remove.

**Running head** is text repeated at the top of braille pages to orient the reader. See [Lesson 21](../lessons/21-running-heads-and-page-numbers.md).

**Runover** is a second or later line of a wrapped paragraph or list item.

**Spine** is the list in an EPUB or eBraille package file that gives the reading order. See [Lesson 39](../lessons/39-inside-the-packages.md).

**Style ID and style name** are the two labels a Word style has. The ID has no spaces and appears in `document.xml`. The name is shown in Word and is what BrailleBlaster matches. See [Lesson 39](../lessons/39-inside-the-packages.md).

**Style View** shows which style is applied to each block of text.

**Tagged PDF** is a PDF that carries a hidden structure of headings, lists, and reading order. Most PDFs are not tagged. See [Lesson 42](../lessons/42-pdfs-scans-and-ocr.md).

**Transcriber-defined typeform** is one of five slots (1 to 5) for print formatting that has no standard braille symbol, such as highlighting or color. Each one must be defined for the reader on the Special Symbols page.

**Transcriber's Note (TN)** is text added by the transcriber, not the author, to explain something to the braille reader. See [Lesson 22](../lessons/22-transcribers-notes.md).

**TVI** is a teacher of students with visual impairments.

**UEB (Unified English Braille)** is BrailleBlaster's default literary braille code.

**Uncontracted (Grade 1)** translation turns contractions off for the selected text.

**Unicode braille** is the Unicode block *Braille Patterns* (U+2800 to U+28FF), which holds every braille cell as one character. See [Lesson 41](../lessons/41-text-encoding-and-braille-characters.md).

**Well-formed** describes an XML file that obeys the seven syntax rules. *Valid* is stronger: the file also follows its DTD or schema. See [Lesson 37](../lessons/37-reading-xml.md).

**XPath** is a small query language for asking questions of an XML file. See [Lesson 37](../lessons/37-reading-xml.md).
