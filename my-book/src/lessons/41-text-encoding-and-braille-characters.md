# Lesson 41: Text Encoding, Clean Text, and Braille Characters

> **Lesson at a glance**
>
> - **Unit:** Unit 5: Handbook (Supplemental)
> - **Suggested time:** about 2 hr 30 min
> - **Prerequisites:** [Lesson 33](33-what-makes-a-good-source.md)
> - **You will need:** A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Explain bytes, characters, and encodings, and check a file for the right one.
- Find and fix the invisible characters that damage a source: smart quotes, non-breaking spaces, soft hyphens, ligatures, form feeds, and byte-order marks.
- Reflow hard-wrapped text into paragraphs, and report what a file contains with a short script.
- Convert between dot numbers, Unicode braille, and Braille ASCII, and read a BRF file as text.

> [!TIP]
> **Practice file:** make your own test with the script in this lesson, or use any text you have copied from a PDF or a web page.

> [!WARNING]
> Do not change a file's encoding or normalize characters in place without keeping an untouched copy. A conversion can silently replace characters or alter byte interpretation; inspect the result and confirm that braille cells, punctuation, and non-English text remain intact.

## Why this matters

Text looks simple, but a copied paragraph can carry dozens of invisible differences: a curly quote where the code expects a straight one, a non-breaking space that no search finds, a soft hyphen in the middle of a word, a ligature that is one character and not two. Each can change what a translator does, and none is visible on screen. The Braille View may be the first place you notice.

The second half of this lesson turns to **braille as text**. A BRF is a text file. Unicode has a block for braille patterns. Being able to move between dots, cells, and characters lets you read a BRF in any editor, and understand what BrailleBlaster's "Direct" translation and View Braille option are showing you.

{HB}

---

## How to use this lesson

Read **The Concept**, then try the scripts on a messy text of your own. The braille table is a reference: skim it once and come back to it.

---

## The Concept

### Characters, bytes, and encodings

A computer stores a file as **bytes**. An **encoding** is the rule for turning bytes into **characters**. The same bytes can be different characters in a different encoding.

| Encoding | What it covers | Notes |
| -------- | -------------- | ----- |
| **ASCII** | 128 characters: English letters, digits, basic punctuation, control codes | The common core of everything else |
| **Latin-1** and **Windows-1252** | ASCII plus accented Western European letters and, in Windows-1252, curly quotes and dashes | Older Windows files. Often *unlabeled* |
| **UTF-8** | Every character in Unicode, stored in one to four bytes | The standard choice. ASCII text is also valid UTF-8 |

**Use UTF-8.** BrailleBlaster reads its text and XML in UTF-8. A file saved in Windows-1252 shows `é` as a nonsense pair of characters when read as UTF-8.

> [!NOTE]
> A **byte-order mark** (BOM) is the three bytes `EF BB BF` at the start of some UTF-8 files, written by some Windows programs. It is the character U+FEFF. It is harmless in many programs and a nuisance in others. Remove it if it appears as a stray character at the top of your text.

### The invisible troublemakers

| Character | Code point | Problem | Fix |
| --------- | ---------- | ------- | --- |
| `“ ”` curly double quotes | U+201C, U+201D | Not the straight `"` that a search or script expects | Search for both |
| `‘ ’` curly single quotes and apostrophes | U+2018, U+2019 | The same | Search for both |
| `–` en dash and `—` em dash | U+2013, U+2014 | May be a range, a break, or a minus | Decide what each is |
| `…` ellipsis | U+2026 | One character, not three periods | Know which your rules want |
| **No-break space** | U+00A0 | Looks like a space, but is not one | Replace with a normal space, or keep deliberately |
| **Soft hyphen** | U+00AD | Invisible, splits a word | Delete |
| **Zero-width space** | U+200B | Invisible, splits a word for a search | Delete |
| **Byte-order mark** | U+FEFF | Invisible, at the start of a file | Delete |
| **Ligatures** `ﬁ` `ﬂ` | U+FB01, U+FB02 | One character instead of two letters. Common in text copied from PDF | Replace with `fi` and `fl` |
| **Minus sign** `−` | U+2212 | Not the ordinary hyphen `-` | Keep it if it is mathematics |
| `×` and `÷` | U+00D7, U+00F7 | Real math symbols, not the letters `x` and a slash | Keep them as math |
| `°` degree | U+00B0 | A symbol with its own braille rule | Keep it |
| `•` bullet | U+2022 | A *typed* bullet means the list is fake | Remove it and apply a list style |
| **Form feed** | U+000C | A page-break control character | BrailleBlaster's text loader splits lines at it |

### What BrailleBlaster does with a text file

BrailleBlaster's text loader, confirmed from its source:

- Each **non-blank line** becomes one **Body Text** paragraph.
- **Blank lines are skipped.** They do not mark paragraphs.
- A **form feed** character splits a line.
- **Characters that XML 1.0 does not allow are removed**, and the removal is only recorded in the log.
- The file is read as **UTF-8**.

So a text file with one paragraph per line imports cleanly, and a **hard-wrapped** file (every line broken at 60 or 70 characters) becomes a stack of tiny paragraphs.

---

## Tools

### Find the non-ASCII characters

```bash
grep -nP '[^\x00-\x7F]' file.txt        # show every line that has a non-ASCII character
```

### Report exactly what is in a file

Save this as `char_report.py`:

```python
import sys, unicodedata, collections
text = open(sys.argv[1], encoding="utf-8", errors="replace").read()
counts = collections.Counter(c for c in text if ord(c) > 126 or (ord(c) < 32 and c not in "\n\t"))
for ch, n in sorted(counts.items(), key=lambda x: -x[1]):
    print(f"U+{ord(ch):04X}  {n:4d}  {unicodedata.name(ch, 'CONTROL CHARACTER')}")
```

Run it with `python3 char_report.py file.txt`. On a test paragraph containing curly quotes, an em dash, an ellipsis, two no-break spaces, a `ﬁ` ligature, a soft hyphen, and a form feed, it printed one line for each of those eight characters.

### Reflow hard-wrapped text

Save this as `unwrap.py`. It joins the lines of each paragraph and separates paragraphs by a blank line:

```python
import re, sys
text = open(sys.argv[1], encoding="utf-8").read().replace("\r\n", "\n")
out = []
for p in re.split(r"\n\s*\n", text):
    out.append(" ".join(l.strip() for l in p.split("\n") if l.strip()))
print("\n".join(out))
```

Run `python3 unwrap.py file.txt > fixed.txt`. It produces **one paragraph per line**, which is what BrailleBlaster's text loader wants.

> [!WARNING]
> Reflowing joins lines at the break, so a word hyphenated at the end of a line stays hyphenated (`hy- phen`). Search the result for `- ` and fix by hand.

### Check and change the encoding

```bash
file -i file.txt                                   # a guess at the encoding
iconv -f WINDOWS-1252 -t UTF-8 file.txt > utf8.txt # convert a Windows-1252 file
head -c 3 file.txt | od -An -tx1                   # shows "ef bb bf" if there is a BOM
```

`file -i` can only guess, and may say `unknown-8bit`. If accented letters look wrong, try `WINDOWS-1252` first.

---

## Braille as text

### Three ways to write the same cell

A six-dot braille cell has 64 possible patterns. A computer can represent a cell in three ways.

1. **Dot numbers.** The raised dots, from 1 to 6: dots *1-4* is the cell for *c*.
2. **Unicode braille.** The Unicode block *Braille Patterns* holds every cell as one character, from **U+2800** (blank) up to U+28FF. It holds 256 patterns, because it also covers the eight-dot cells.
3. **Braille ASCII.** The character set used in **BRF files**, which maps each of the 64 six-dot patterns to a printable ASCII character, so that braille can travel as ordinary text.

### The formula

For the six-dot cells, **the Unicode character is U+2800 plus the sum of 2 raised to (dot number − 1) for each raised dot.** So dot 1 adds 1, dot 2 adds 2, dot 3 adds 4, dot 4 adds 8, dot 5 adds 16, and dot 6 adds 32.

**Worked example: the letter *c* (dots 1 and 4).** 1 + 8 = 9, so the character is U+2800 + 9 = **U+2809**, which is `⠉`. In Braille ASCII, a value of 9 is the character `C`.

**Worked example: *hello*.** The letters are dots 125, 15, 123, 123, 135. Their values are 19, 17, 7, 7, and 21. In Unicode that is `⠓⠑⠇⠇⠕`, and in Braille ASCII it is `HELLO`. For the letters *a* to *z*, Braille ASCII is the same letter in capitals.

> [!NOTE]
> The letters match, but the punctuation and the digits do not. In Braille ASCII, the character `1` is **dot 2**, not the numeral one. The numeral one is the cell for *a* with a numeric indicator before it. The capital sign (dot 6) is the comma `,`, and the numeric indicator (dots 3456) is the number sign `#`.

### The full table

This table was generated by computing the formula for all 64 patterns, and the letters and digits were checked against their known cells. A blank cell is the space character.

| Dots | Cell | Unicode | Braille ASCII |
| ---- | ---- | ------- | ------------- |
| none | ⠀ | U+2800 | (space) |
| 1 | ⠁ | U+2801 | `A` |
| 2 | ⠂ | U+2802 | `1` |
| 12 | ⠃ | U+2803 | `B` |
| 3 | ⠄ | U+2804 | `'` |
| 13 | ⠅ | U+2805 | `K` |
| 23 | ⠆ | U+2806 | `2` |
| 123 | ⠇ | U+2807 | `L` |
| 4 | ⠈ | U+2808 | `@` |
| 14 | ⠉ | U+2809 | `C` |
| 24 | ⠊ | U+280A | `I` |
| 124 | ⠋ | U+280B | `F` |
| 34 | ⠌ | U+280C | `/` |
| 134 | ⠍ | U+280D | `M` |
| 234 | ⠎ | U+280E | `S` |
| 1234 | ⠏ | U+280F | `P` |
| 5 | ⠐ | U+2810 | `"` |
| 15 | ⠑ | U+2811 | `E` |
| 25 | ⠒ | U+2812 | `3` |
| 125 | ⠓ | U+2813 | `H` |
| 35 | ⠔ | U+2814 | `9` |
| 135 | ⠕ | U+2815 | `O` |
| 235 | ⠖ | U+2816 | `6` |
| 1235 | ⠗ | U+2817 | `R` |
| 45 | ⠘ | U+2818 | `^` |
| 145 | ⠙ | U+2819 | `D` |
| 245 | ⠚ | U+281A | `J` |
| 1245 | ⠛ | U+281B | `G` |
| 345 | ⠜ | U+281C | `>` |
| 1345 | ⠝ | U+281D | `N` |
| 2345 | ⠞ | U+281E | `T` |
| 12345 | ⠟ | U+281F | `Q` |
| 6 | ⠠ | U+2820 | `,` |
| 16 | ⠡ | U+2821 | `*` |
| 26 | ⠢ | U+2822 | `5` |
| 126 | ⠣ | U+2823 | `<` |
| 36 | ⠤ | U+2824 | `-` |
| 136 | ⠥ | U+2825 | `U` |
| 236 | ⠦ | U+2826 | `8` |
| 1236 | ⠧ | U+2827 | `V` |
| 46 | ⠨ | U+2828 | `.` |
| 146 | ⠩ | U+2829 | `%` |
| 246 | ⠪ | U+282A | `[` |
| 1246 | ⠫ | U+282B | `$` |
| 346 | ⠬ | U+282C | `+` |
| 1346 | ⠭ | U+282D | `X` |
| 2346 | ⠮ | U+282E | `!` |
| 12346 | ⠯ | U+282F | `&` |
| 56 | ⠰ | U+2830 | `;` |
| 156 | ⠱ | U+2831 | `:` |
| 256 | ⠲ | U+2832 | `4` |
| 1256 | ⠳ | U+2833 | `\` |
| 356 | ⠴ | U+2834 | `0` |
| 1356 | ⠵ | U+2835 | `Z` |
| 2356 | ⠶ | U+2836 | `7` |
| 12356 | ⠷ | U+2837 | `(` |
| 456 | ⠸ | U+2838 | `_` |
| 1456 | ⠹ | U+2839 | `?` |
| 2456 | ⠺ | U+283A | `W` |
| 12456 | ⠻ | U+283B | `]` |
| 3456 | ⠼ | U+283C | `#` |
| 13456 | ⠽ | U+283D | `Y` |
| 23456 | ⠾ | U+283E | `)` |
| 123456 | ⠿ | U+283F | `=` |

### Reading a BRF

A BRF is a plain text file in Braille ASCII, usually with a **fixed line length** (such as 40 characters) and a **form feed** (U+000C) between pages. You can open one in any text editor and read it, if you know the table. Two cautions:

- Some BRFs use **uppercase** Braille ASCII and some use **lowercase**. BrailleBlaster's Braille Preview has an *Uppercase* option for this reason ([Lesson 1](01-navigating-the-interface.md)).
- Line endings and form feeds vary. A BRF made for one embosser may not suit another.

### Where this shows up in BrailleBlaster

- **View Braille** switches the Braille View between Unicode cells and ASCII ([Lesson 1](01-navigating-the-interface.md)).
- **Change Translation: Direct** ([Lesson 28](28-editing-the-translation.md)) uses the ASCII translation literally.
- **Six Key Mode** types cells directly. What you type there is *not* translated, and is stored as braille characters.

---

## Step by step

### Clean a text before importing

1. Run `char_report.py` and read the list.
2. For each problem character, decide: **keep** (real math symbols, a degree sign), **replace** (ligatures, curly quotes if your rules need it), or **delete** (soft hyphens, zero-width spaces, a BOM).
3. Unwrap hard-wrapped text with `unwrap.py`.
4. Search for typed bullets and numbers that should be list structure.
5. Save as UTF-8 with a `.txt` extension, and open it in BrailleBlaster.

### Convert a word to dots, Unicode, and Braille ASCII

1. Write each letter's dots.
2. Add 2 raised to (dot − 1) for each, to get the value.
3. Add that to U+2800 for the Unicode cell.
4. Use the table (or the letter, in capitals) for the Braille ASCII.

---

## Practice

### Tasks

1. What is the Unicode character for dots 1, 2, and 4 (the letter *f*)? Show the sum.
2. Write the word *bad* in dot numbers, in Unicode braille, and in Braille ASCII.
3. Decode this Braille ASCII text, which has no capital or number signs: `DAD`.
4. What do `,` and `#` mean in Braille ASCII?
5. Why does the Braille ASCII character `5` not mean the numeral five?
6. A text file imports as hundreds of one-line paragraphs. What is the cause, and how do you fix it?
7. A search for the word *fine* fails, although you can see it in the text. Name two likely causes.
8. A file shows `cafÃ©` instead of `café`. What is wrong, and what do you try first?

### Answer Key

1. Dots 1, 2, and 4: 1 + 2 + 8 = 11. U+2800 + 11 = U+280B, which is `⠋`.
2. *b* is dots 12, *a* is dot 1, *d* is dots 145. In Unicode: `⠃⠁⠙`. In Braille ASCII: `BAD`.
3. *dad*, because for letters the Braille ASCII character is the capital letter.
4. `,` is **dot 6**, which is the **capital sign**. `#` is **dots 3456**, which is the **numeric indicator**.
5. In Braille ASCII, `5` is the cell for **dots 2 and 6**. It is just a character that stands for that pattern. A numeral five in braille is the cell for *e* after a numeric indicator.
6. The text is **hard-wrapped**, so each line became a paragraph. Reflow it with `unwrap.py`, or ask for the text with one paragraph per line.
7. The word contains an invisible character, such as a **soft hyphen** (`ﬁ-ne`), a **zero-width space**, or a **ligature** (the `ﬁ` in *fine* is one character). A no-break space between words would also defeat a search for a phrase.
8. The file is in **Windows-1252** (or Latin-1) but is being read as UTF-8, or the reverse. Try `iconv -f WINDOWS-1252 -t UTF-8`.

---

## Key takeaways

- **Use UTF-8.** A file saved in another encoding turns accented letters into nonsense.
- The troublemakers are invisible: curly quotes, no-break spaces, soft hyphens, zero-width spaces, ligatures, byte-order marks, and form feeds. A short script finds them.
- BrailleBlaster reads **each non-blank line of a text file as one paragraph**, skips blank lines, and silently removes characters XML cannot hold. Reflow hard-wrapped text first.
- A braille cell can be **dots**, a **Unicode character** (U+2800 plus the sum of 2 to the power dot-minus-1), or a **Braille ASCII** character. For letters, Braille ASCII is the capital letter.
- A BRF is a text file in Braille ASCII with fixed lines and form feeds.

---

## Source Citations

- The BrailleBlaster program source (the conversion script `bbx.lua` and the Pandoc loader), read at commit `369176b`, with the conversion tests run using Pandoc 3.12.1, the version BrailleBlaster bundles, including the text loader, which treats each non-blank line as a paragraph and removes characters that XML 1.0 forbids.
- The Unicode Consortium, *The Unicode Standard*, the *Braille Patterns* block (U+2800 to U+28FF), at [unicode.org](https://www.unicode.org/charts/PDF/U2800.pdf).
- The Braille ASCII table and the letter and digit patterns were checked by computation. See also [Lesson 44](44-quick-reference-cards.md).
