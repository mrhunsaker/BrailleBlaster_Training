# BrailleBlaster Comprehensive Trainer Guide

> **Purpose**: This guide provides 2-3 pages of detailed trainer material for **each** topic listed in BrailleBlaster\_Topics.md.

## Table of Contents

### Intro/Basic

1. [Applying Text Formatting](#1)
2. [Applying Layout Styles](#2)
3. [Math Translation Toggle](#3)
4. [ASCII Math Hub](#4)
5. [Opening/Converting Word Documents](#5)
6. [Troubleshooting Poorly Formatted Word/ODT](#6)
7. [Paper Size and Embossers](#7)

### Intermediate

8. [Spatial Math Editor](#8)
9. [Spatial Number Lines](#9)
10. [Global Find and Replace](#10)

### Alluded to/Advanced

11. [eBraille Format](#11)
12. [NIMAS/XML Import](#12)

### Unmentioned/Advanced

13. [Markdown/OpenOffice/LaTeX/XML Import](#13)
14. [Transcriber Tasks](#14)
15. [Embosser Setup](#15)
16. [Advanced Formatting](#16)
17. [Contraction Relaxer](#17)

### Finally

18. [What Pandoc Does](#18)

---

# 1. Applying Text Formatting

## Why This Matters

Text formatting is the **first hands-on skill** new transcribers practice. The judgment call of **when to preserve** formatting and **when to drop it** is critical. Braille has a **limited vocabulary** for text emphasis (Bold, Italics, Underline, Script) compared to print's infinite possibilities.

## Core Concepts

- **Bold** (`Ctrl+B`): Key terms, headings within body text
- **Italics** (`Ctrl+I`): Publication titles, foreign words, light emphasis
- **Underline** (`Ctrl+U`): Underlined print text
- **Script** (`Alt+Shift+S`): Text that mimics handwriting
- **Transcriber's Notes (TN)**: Text the transcriber adds; requires opening/closing indicators
- **Transcriber-Defined Typeforms** (`Shift+Alt+1` to `Shift+Alt+5`): For non-standard formatting (highlighting, colored text); must be defined in Transcriber's Notes

## Teaching Strategy

Start with discussion: "What does bold mean to a braille reader vs. italics?" **Selection-First Rule**: Select text first, then apply emphasis (not word processor style).

## Common Pitfalls &amp; Solutions

- **Over-Preservation**: Applying bold to decorative formatting → Use "Would a braille reader lose meaning without this?" test
- **Inconsistent Application**: First book title italicized, second not → Use **Emphasis → Find All Emphasis** to audit
- **Forgetting Braille View**: Not verifying → "Apply formatting, check Braille View" as paired action
- **Transcriber-Defined Overuse**: Assigning slots to every colored text → Discuss cost: documentation required, cognitive load for reader

## Advanced Points

**Emphasis Hierarchy**: Multiple typeforms on same text appear in sequence in braille.  
**Bulk Removal Tools**: Remove Emphasis from Section (`Ctrl+Shift+R`), Remove All Emphasis from Headings/List Prefixes.

## Practice Design

- **Beginner**: Paragraphs with 3-4 clear semantic emphasis instances
- **Intermediate**: Mixed semantic and decorative formatting; decide what to preserve
- **Advanced**: Inconsistent formatting; standardize per BANA

## Assessment

- Apply all four standard typeforms
- Identify Transcriber-Defined candidates
- Explain TN vs. Transcriber-Defined
- Use bulk removal tools
- Justify decisions using "reader meaning" test

## Teaching Time: 130 minutes (2+ pages)

---

# 2. Applying Layout Styles

## Why This Matters

If text formatting is "what words look like," layout styles are "how the document is structured." Braille formatting is **rule-based** (BANA) not **visual**.

## Core Concepts

- **Emphasis**: Character-level (bold, italics)
- **Styles**: Paragraph/block-level (headings, lists, blocks)
- **Style Families**: Body Text (3-1 margins), Headings (BANA-defined spacing), List (nesting capability), Block/Box (visually set off)
- **Container Styles**: List, Poetry, Box act as containers; in Breadcrumbs: prefixed with "CONTAINER"

## Teaching Strategy

**Side-by-Side Comparison**: Show print vs. braille versions. **Breadcrumbs Revelation**: Makes invisible structure visible. Always keep Breadcrumbs visible when working with styles.

## Common Pitfalls &amp; Solutions

- **Applying List to Non-List**: Using List style for short paragraphs → "Structural test": Is this a structured enumeration?
- **Manual Margin Adjustment**: Trying to set margins by typing numbers → BANA rules handle margins automatically
- **Style Override Confusion**: Style doesn't look right → Use Breadcrumbs to diagnose hierarchy
- **Ignoring Containers**: Not understanding container styles → Demonstrate container behavior; use Unwrap Element

## Advanced Points

**Style Configuration**: Adjust number of style levels (**Styles → Configure → Style Levels**). Default 5, complex docs may need up to 8.  
**Style Customization**: Create custom styles (**Styles → Configure → Edit Styles**). Only for specific agency requirements.

## Practice Design

- **Beginner**: Document with clear structural elements
- **Intermediate**: Nested structures; use Breadcrumbs
- **Advanced**: Poorly formatted document; diagnose and apply styles

## Assessment

- Distinguish emphasis vs. layout styles
- Apply all core style families
- Use Breadcrumbs effectively
- Apply/remove container styles
- Use Repeat Last Style
- Explain contextual BANA-compliant styles

## Teaching Time: 170 minutes (2.5+ pages)

---

# 3. Math Translation Toggle

## Why This Matters

Mathematical notation is where many new transcribers hit their first major conceptual wall. In print, math is **visual and two-dimensional**. In braille, math is **linear and one-dimensional** (Nemeth Code or UEB Technical). The Math Translation Toggle (`Ctrl+M`) is the gateway.

## Core Concepts

- **Literary text**: Translated character-by-character
- **Mathematical text**: Translated according to Nemeth or UEB Technical rules
- **Two-Step Process**: 1. Flag text as math (`Ctrl+M`), 2. Apply Nemeth indicators if needed
- **Visual Feedback**: Math-flagged text appears **bright pink** in Print View
- **Nemeth Indicators**: Block (lines before/after) for displayed equations; Inline (immediately before/after) for short expressions in sentences

## Teaching Strategy

**Language Analogy**: "Imagine reading English, then suddenly French. `Ctrl+M` tells BrailleBlaster 'this is math.' Nemeth indicators tell reader 'this is Nemeth code.'"  
**Two Decisions**: 1. *Is this math?* (Toggle), 2. *How mark boundary?* (Block vs. Inline)

## Common Pitfalls &amp; Solutions

- **Forgetting to Toggle**: Formatting visually but forgetting `Ctrl+M` → "See math, press `Ctrl+M`." Pink = confirmation
- **Overuse of Indicators**: Applying to every expression in Nemeth-only doc → Indicators for **code-switching** within UEB only
- **Incorrect Block vs. Inline**: Block for inline or vice versa → "Sentence test": Readable as part of sentence? Yes → Inline. Stands alone? → Block
- **Partial Flagging**: Flagging only part of expression → Entire expression must be flagged

## Advanced Points

**Math in Different Contexts**: Inline in prose (Nemeth Inline), displayed (Nemeth Block), in lists (usually Inline), in headings (rare, treat as Inline)  
**Math and Emphasis**: Apply emphasis *within* math-flagged text  
**Translation Tables**: Works with document's translation table (Nemeth, UEB Technical). Check/change at **Settings → Translation Settings**

## Practice Design

- **Beginner**: 2-3 clear mathematical expressions (1 inline, 1 displayed)
- **Intermediate**: Mixed prose and math; identify and flag appropriately
- **Advanced**: Complex math in various contexts; apply formatting throughout

## Assessment

- Identify mathematical expressions
- Apply Math Translation Toggle
- Choose Block vs. Inline appropriately
- Explain when indicators are/aren't needed
- Verify in Braille View
- Handle math within other formatting

## Teaching Time: 170 minutes (2.5+ pages)

---

# 4. ASCII Math Hub

## Why This Matters

The ASCII Math Hub is the bridge between print mathematics and BrailleBlaster's internal representation. Essential for building complex structures and looking up symbols.

## Core Concepts

- **ASCII Math**: Compact linear notation representing equations before translation to braille math codes
- **Hub Organization**: Symbols organized into tabs: Operation, Miscellaneous, Relation, Greek, Logical, Grouping, Arrows, Accents, Functions, Special, Examples, Search
- **The Examples Tab**: Shows common composite structures (complex fractions) in both code and visual form

## Teaching Strategy

**Start with Recognition**: Show print equations, ask: "What structure do you see? Fraction? Root? Exponent?"  
**Hub as Training Wheels**: Frame as tool for building fluency, not a crutch. Goal: eventually type directly.

## Common Pitfalls &amp; Solutions

- **Skipping the Hub**: Trying to type directly, leading to syntax errors → Require Hub usage for first 2-3 weeks
- **Not Verifying Flagging**: Not noticing inserted text isn't pink → "Hub → Insert → Check for pink"
- **Overcomplicating**: Building unnecessarily complex ASCII Math → "Simplest correct form" principle
- **Ignoring Examples Tab**: Building complex fractions symbol by symbol → Explicitly demonstrate Examples tab first

## Advanced Points

- **Hub Customization**: Full screen, font size, show/hide tabs
- **Replacing Math**: Use **Replace Current Math** with **Previous/Next Math** buttons
- **ASCII Math Syntax**: Parentheses `(a+b)`, carets `x^2`, underscores `x_2`, slashes `a/b`, functions `sin(x)`, Greek `alpha`
- **Common Structures**: Simple fraction `a/b`, complex `(a+b)/(c-d)`, square root `sqrt(x)`, nth root `root(n)(x)`, summation `sum_(i=1)^n i^2`

## Practice Design

- **Beginner**: Simple equations (basic fractions, exponents)
- **Intermediate**: Complex fractions and roots
- **Advanced**: Multi-line derivations

## Assessment

- Navigate Hub efficiently
- Find symbols using browsing and search
- Build simple and complex equations
- Verify math flagging
- Replace existing math
- Explain ASCII Math syntax

## Teaching Time: 230 minutes (3+ pages)

---

# 5. Opening/Converting Word Documents

## Why This Matters

In production, most source material arrives as Word documents. BrailleBlaster's ability to read Word's internal structure can save **hours**—but only if the Word document is **well-structured**.

## Core Concepts

- **Structure vs. Appearance**: Well-structured (uses Word's built-in styles) vs. Visually formatted (manual formatting to *look* structured)
- **What BrailleBlaster Reads**: Paragraph styles, character styles, list structures, table structures, image captions
- **Mapping Process**: Word Heading 1 → BrailleBlaster Heading 1, Word List Paragraph → BrailleBlaster List, Word Normal → Body Text
- **80/20 Rule**: Well-structured imports with 80-90% formatting correct; remaining 10-20% needs adjustment

## Teaching Strategy

**The Revealing Demonstration**: Create two Word versions of same document (Version A: proper styles, Version B: manual formatting). Open both in BrailleBlaster side by side.  
**The Diagnostic Workflow**: 1. Inspect in Word (Style Pane), 2. Predict import, 3. Open and verify, 4. Correct and document

## Common Pitfalls &amp; Solutions

- **Trusting Visual Appearance**: Assuming document is well-structured because it looks good → "Style Pane test": In Word, open Style Pane. If "Normal" for everything, not well-structured
- **Not Checking Import**: Starting work without verifying → "Open → Verify → Then Work"
- **Manual Reformatting**: Manually reapplies formatting to every element → Identify pattern, use Find and Replace with Formatting for batch fixes
- **Ignoring Tables**: Not realizing tables imported but lost structure → Verify table import; often need manual adjustment

## Advanced Points

- **Word Document Preparation**: Apply proper heading styles, use built-in lists, apply character styles, add alt text, use Style Pane to verify
- **ODT vs. DOCX**: ODT generally has better structure; may use different style names; always verify import
- **Conversion as Troubleshooting**: If .docx behaves unpredictably: In Word, **Save As → Web Page (.html)**, open HTML in BrailleBlaster

## Practice Design

- **Beginner**: Well-structured Word; open, verify, minor adjustments
- **Intermediate**: Visually-formatted but structurally-flat; diagnose, predict, open, verify
- **Advanced**: Complex Word with tables, images, nested lists; import, diagnose, create correction plan

## Assessment

- Identify well-structured vs. poorly-structured documents
- Use Word's Style Pane
- Predict import quality
- Verify import using Breadcrumbs
- Diagnose and fix common import issues
- Use HTML as intermediate format
- Prepare Word documents for optimal import

## Teaching Time: 230 minutes (3+ pages)

---

# 6. Troubleshooting Poorly Formatted Word/ODT

## Why This Matters

While well-formatted documents are ideal, **most received will be poorly formatted**. This teaches how to **diagnose, triage, and systematically fix** documents with visual formatting rather than structural formatting.

## Core Concepts

- **The Diagnostic Mindset**: What is author trying to communicate? What visual cues indicate structure? How to map cues to proper braille formatting?
- **The Fix Order Principle**: 1. Read entire document first, 2. Fix structure before emphasis, 3. Fix emphasis last
- **Pattern Recognition**: Most poorly formatted documents have consistent patterns of fake structure; identify pattern, fix in batch

## Teaching Strategy

**Frame as Investigation**: "You're a detective. The author left clues about intended structure. Your job is to find and interpret them correctly."  
**The Three-Pass Method**:

1. **Reconnaissance**: Skim, identify structural elements, note visual patterns, create "style map"
2. **Structural Correction**: Apply proper styles, use Find and Replace with Formatting, verify with Breadcrumbs
3. **Emphasis Correction**: Apply proper emphasis, remove decorative formatting, final verification

## Common Pitfalls &amp; Solutions

- **Reactive Fixing**: Fixing as they scroll → Insist on three-pass method
- **Overlooking Inconsistencies**: Assuming all headings use same pattern → Explicitly check for inconsistency
- **Ignoring Big Picture**: Fixing individual issues without understanding structure → Always start with Pass 1
- **Manual One-by-One**: Fixing each instance individually → Use Find and Replace with Formatting for batch fixes

## Advanced Points

- **Creating Style Maps**: Document visual patterns, counts, likely structures, BrailleBlaster styles
- **Using Find and Replace**: Find all text with specific formatting, replace with style, verify
- **Handling Edge Cases**: Mixed formatting, nested structures, inconsistent nesting
- **Document Triage**: For very poor documents, sometimes faster to copy raw text, paste into new document, apply all formatting from scratch
- **Quality Assurance Checklist**: After fixing, verify all headings, lists, emphasis, math, Breadcrumbs, Braille View

## Practice Design

- **Beginner**: Document with 2-3 consistent patterns; create style map, apply fixes
- **Intermediate**: Document with inconsistent patterns; identify, create correction plan
- **Advanced**: Complex document with nested structures and mixed formatting; triage, diagnose, fix completely

## Assessment

- Perform complete reconnaissance
- Create accurate style map
- Apply three-pass correction method
- Use Find and Replace with Formatting
- Handle inconsistent formatting
- Verify document quality
- Decide when to reformat from scratch

## Teaching Time: 260 minutes (3+ pages)

---

# 7. Paper Size and Embossers

## Why This Matters

This is where digital meets physical. All formatting work is useless if the document doesn't emboss correctly. Page setup affects everything—margins determine page breaks, interpoint affects density, embosser profiles ensure output goes to right device.

## Core Concepts

- **Page Properties**: Page Size (11.5" × 11" or 11" × 11.5"), Margins (0.5" top/bottom, 1.25" left, 0.48" right), Lines Per Page (25-30), Cells Per Line (40-42), Interpoint (Yes/No)
- **The Reflow Principle**: Changing page properties reflows entire document; set **before** transcription begins
- **Translation Settings**: Braille Code (UEB, UEB with Nemeth, EBAE), Math Code, Grade (2 or 1)
- **Embosser Profiles**: Tells BrailleBlaster device, margin handling, graphics support
- **Critical Distinction**: **File → Print** (Print View to printer) vs. **File → Emboss** (`Ctrl+E`) (Braille View to embosser)

## Teaching Strategy

**Start with the Paper**: Bring actual braille paper. Show physical dimensions, margin requirements, interpoint differences.  
**The Setup Workflow**: 1. Check agency standards, 2. Set Page Properties before starting, 3. Create/Select Embosser Profile, 4. Test with short document

## Common Pitfalls &amp; Solutions

- **Setting After Transcription**: Changing properties after completing document → "Set before you start"
- **Clicking Make Default Too Soon**: Setting non-standard as default → Use **OK** until confirmed; only **Make Default** after confirming standards
- **Confusing Print and Emboss**: Sending to embosser using Print → "Print = Eyes, Emboss = Fingers"
- **Incorrect Profile**: Selecting wrong embosser profile → Verify profile before sending; use descriptive names
- **Ignoring Interpoint**: Not setting correctly → Explain physical difference: interpoint uses both sides, doubling density

## Advanced Points

- **Custom Page Sizes**: Measure paper, enter custom dimensions, test with short document
- **Margin Units**: Inches, cells, or lines; teach conversion between them
- **Embosser Profile Types**: Specific Model, Generic Text Only, Generic Text with Margins, Generic Graphics Embosser
- **Troubleshooting**: No output (power/connection), wrong margins (profile/document), garbled text (translation), paper jams (loading/size)
- **Multiple Embosser Management**: Create profile directory, set default profiles, create profile groups, implement testing protocol

## Practice Design

- **Beginner**: Page property specifications; set up document, emboss test page
- **Intermediate**: Document with default settings; change to agency standards, observe reflow
- **Advanced**: Complex document; set up page properties, create embosser profile, emboss complete document

## Assessment

- Set page properties per agency standards
- Explain impact of page properties
- Create embosser profile
- Distinguish Print vs. Emboss
- Set interpoint correctly
- Troubleshoot profile issues
- Verify embossed output

## Teaching Time: 175 minutes (2.5+ pages)

---

# 8. Spatial Math Editor

## Why This Matters

The Spatial Math Editor is BrailleBlaster's **visual equation builder**—WYSIWYG interface for creating mathematical expressions. While ASCII Math Hub is for building through code, Spatial Math Editor lets users **draw** equations visually.

## Core Concepts

- **The Spatial Paradigm**: Unlike linear ASCII Math, allows **two-dimensional layout**; can place symbols anywhere on a grid, build fractions vertically, create matrices
- **The Editor Interface**: Toolbar (symbols/structures), Canvas (grid), Properties Panel, Preview
- **Symbol Palette**: Basic Operations, Grouping, Fractions, Roots, Superscripts/Subscripts, Greek, Functions, Special
- **The Conversion Process**: Build visually → converts to ASCII Math internally → translates to braille math code → appears in Braille View

## Teaching Strategy

**Start with Simple Equations**: Begin with basic equations with clear spatial relationships.  
**The Grid Concept**: Each symbol occupies cells, can be aligned horizontally/vertically, grid maintains spacing/alignment.

## Common Pitfalls &amp; Solutions

- **Overlapping Symbols**: Placing too close → "Personal space" for symbols; use grid lines
- **Incorrect Fraction Alignment**: Not properly aligned → Use fraction templates
- **Forgetting to Insert**: Building but forgetting to click Insert → "Build → Preview → Insert → Verify"
- **Not Verifying Flagging**: Not checking pink highlighting → After inserting, always check Print View for pink
- **Complex Without Templates**: Trying to build complex structures without templates → Always look for templates first

## Advanced Points

- **Customizing Editor**: Grid size, show/hide grid, zoom, symbol sizes
- **Advanced Structures**: Matrices (using template, add rows/columns), nested fractions (using template recursively), summations/integrals (large operator templates), multi-line equations (proper alignment)
- **Spatial Editor vs. ASCII Math Hub**: Visual/WYSIWYG vs. code-based, easier for visual learners vs. steeper learning curve, intuitive for 2D vs. requires linear understanding
- **Combining Approaches**: Use Spatial for complex 2D, Hub for symbols/simple structures, manual typing for familiar expressions
- **Keyboard Shortcuts**: Arrow keys (move), Delete (remove), Ctrl+C/V (copy/paste), Ctrl+Z/Y (undo/redo)
- **Properties Panel**: Adjust symbol size, type, superscripts/subscripts, alignment/spacing

## Practice Design

- **Beginner**: Simple equations (basic fractions, exponents)
- **Intermediate**: Complex fractions and roots
- **Advanced**: Multi-line equations and matrices

## Assessment

- Navigate interface
- Use symbol palettes/templates
- Build simple/complex equations
- Insert correctly
- Verify math flagging
- Combine with other math tools
- Use keyboard shortcuts

## Teaching Time: 230 minutes (3+ pages)

---

# 9. Spatial Number Lines

## Why This Matters

Number lines are a **critical accessibility feature** for blind students learning mathematics. They provide a tactile way to understand numerical relationships, comparisons, and operations.

## Core Concepts

- **Purpose**: Numerical relationships, operations visualization, comparisons, fractions/decimals understanding
- **The Number Line Interface**: Line Template, Number Placement, Arrow Tools, Labeling
- **Types**: Basic (simple line with numbers), Empty (no numbers, for student filling), Fraction (divided into parts), Decimal (with markings), Operation (showing +, -)
- **The Workflow**: Open editor → choose template/start blank → add tick marks → add numbers/labels → add arrows → preview → insert

## Teaching Strategy

**Start with Print Number Lines**: Show print examples, discuss conveyed information, then show tactile representation.  
**The Accessibility Perspective**: Have trainees close eyes, imagine feeling a number line. Discuss what can be conveyed through touch, what's different from visual, what additional tactile cues might help.

## Common Pitfalls &amp; Solutions

- **Overcrowding**: Too many numbers/labels → "Finger span" rule: readable with one or two finger spans; typically 5-10 numbers max
- **Inconsistent Spacing**: Uneven spacing → Use grid and snap-to-grid; distance proportional to numerical difference
- **Missing Context**: No context/instructions → Always include text description (e.g., "Number line from 0 to 10. Find 7.")
- **Not Considering Reader**: Too complex for level → Match complexity to reader's grade level
- **Forgetting to Verify**: Not checking embossed output → Always preview tactile output; some embossers have graphic limitations

## Advanced Points

- **Custom Templates**: For specific grade levels, mathematical concepts, textbooks
- **Advanced Types**: Negative (extending left of zero), Fraction (halves, thirds), Decimal (0.1, 0.2), Inequality (x &gt; 3), Operation (addition as repeated addition)
- **Combining with Other Math**: Number line above/below equation, with text, multiple number lines showing different operations
- **Embosser Considerations**: Graphics embossers (ViewPlus) vs. text embossers (simple drawings), resolution limitations, size limitations
- **Accessibility Standards**: BRAille Formats 2016, WCAG, Local Education Agency Standards

## Practice Design

- **Beginner**: Simple specifications (0-5, 0-10); create basic lines
- **Intermediate**: Mathematical problems; create lines that solve/illustrate
- **Advanced**: Complex concepts; create multi-part diagrams with labels, arrows, explanations

## Assessment

- Create basic number lines with proper spacing
- Add numbers/labels
- Create lines for operations
- Create fraction/decimal lines
- Consider intended reader needs
- Provide appropriate text descriptions
- Verify tactile output
- Create/use custom templates

## Teaching Time: 230 minutes (3+ pages)

---

# 10. Global Find and Replace with Formatting Options

## Why This Matters

Find and Replace is one of the most **powerful productivity tools** in BrailleBlaster. Allows batch operations that would otherwise take hours manually.

## Core Concepts

- **The Power of Batch Operations**: What would take hours manually can take minutes
- **The Three Modes**: Find, Replace, Find and Replace
- **What Can Be Searched**: Text, formatting (bold, italics, fonts, sizes), styles, combinations
- **The Formatting Options Dialog**: Character formatting (bold, italics, font, size, color), paragraph formatting (style, indentation, alignment, spacing), special characters (tabs, line breaks, page breaks)

## Teaching Strategy

**Start with Simple Text Replacement**: Find/replace specific word, phrase, with case sensitivity.  
**Introduce Formatting**: Find all bold text, all Heading 1 styles, replace all italicized with bold.  
**Combine Text and Formatting**: Find all "Important" in bold, replace all Heading 2 with Heading 3, find all underlined and remove underlining.

## Common Pitfalls &amp; Solutions

- **Overly Broad Searches**: Searching for "the" and replacing everywhere → Use **Find** first, **Whole Words Only** and **Match Case**
- **Not Using Formatting Options**: Only searching for text → Real power is in formatting
- **Replacing Without Verification**: Using Replace All without checking → Always use **Find** first, then **Replace** one at a time for first few
- **Complex Patterns Without Testing**: Creating complex patterns without testing → Build incrementally; test after each addition
- **Ignoring Scope**: Not realizing search limited to current selection → Check scope (Current Selection vs. Entire Document) before searching

## Advanced Points

- **Regular Expressions**: `.` (any), `*` (zero+), `+` (one+), `[abc]` (any in set), `^` (start), `$` (end)
- **Wildcards**: `?` (any single), `*` (any string)
- **Special Characters**: `^l` (line break), `^t` (tab), `^p` (paragraph)
- **Formatting Combinations**: Bold AND italic, Heading 1 WITH specific text, Underlined text of specific font size
- **Preserving Formatting**: Replace text while preserving formatting using **Preserve Formatting** option
- **Style-Based Replacement**: Replace one style with another using Formatting Options
- **Multi-Step Workflows**: 1. Convert fake headings to proper styles, 2. Standardize emphasis, 3. Fix list formatting, 4. Verify/clean up
- **Saving Searches**: Search history preserved within session; document for permanent saves

## Practice Design

- **Beginner**: Documents with simple, consistent formatting issues
- **Intermediate**: Documents with complex formatting patterns
- **Advanced**: Poorly formatted documents; create multi-step workflow

## Assessment

- Basic Find/Replace for text
- Formatting Options for formatting patterns
- Complex search patterns (text + formatting)
- Replace vs. Replace All appropriately
- Whole Words Only and Match Case
- Search for special characters
- Replace one style with another
- Create multi-step workflows
- Save/reuse search patterns

## Teaching Time: 230 minutes (3+ pages)

---

# 11. eBraille Format

## Why This Matters

eBraille is a **standard XML-based format** for representing braille documents. Designed to be human-readable, machine-readable, and interoperable.

## Core Concepts

- **What is eBraille?** XML schema defining document structure, braille formatting, mathematical notation, page layout
- **The eBraille File**: `.brf` or `.xml` extension containing XML structure with braille, head, body, styles
- **BrailleBlaster and eBraille**: Can import/export, preserving structure, formatting, math
- **Advantages**: Standardization, interoperability, longevity, metadata, validation

## Teaching Strategy

**Start with Comparison**: Show same document in Word, BrailleBlaster, eBraille. Discuss what each preserves.  
**The XML Concept**: For unfamiliar trainees, explain XML is markup language using tags and attributes.

## Common Pitfalls &amp; Solutions

- **Assuming All Features Preserved**: Expecting all BrailleBlaster features in eBraille → Test with complex documents
- **Editing Manually**: Trying to edit without XML knowledge → Warn against unless comfortable
- **Not Validating**: Exporting without validation → Always validate; BrailleBlaster validates on import
- **Ignoring Metadata**: Not including/updating metadata → Show how to include/edit metadata

## Advanced Points

- **eBraille Schema**: Required elements (braille, head, body), optional elements (metadata, styles)
- **Validation**: BrailleBlaster on import, external XML validators, schema-aware editors
- **eBraille vs. Other Formats**: eBraille (standard, interoperable, verbose), BRF (simple, compact, limited formatting), BrailleBlaster (full features, proprietary), PEF (international standard, complex)
- **eBraille Workflows**: Agency (Create → Export → Share), Archiving (Create → Export → Store), Collaboration (Create → Export → Proofreader → Import edits)
- **eBraille Tools**: Liblouis, Braille2000, Duxbury

## Practice Design

- **Beginner**: Simple documents; export, verify structure
- **Intermediate**: eBraille files; import, verify formatting
- **Advanced**: Workflow requiring export/import; complete workflow, verify integrity

## Assessment

- Export/import eBraille
- Understand XML structure
- Explain advantages
- Verify import quality
- Make adjustments
- Validate files
- Explain legal context
- Use in workflows
- Troubleshoot issues

## Teaching Time: 175 minutes (2.5+ pages)

---

# 12. NIMAS/XML Import Benefits

## Why This Matters

NIMAS (National Instructional Materials Accessibility Standard) is a **U.S. Department of Education standard** for source files used in accessible instructional materials production, including braille.

## Core Concepts

- **What is NIMAS?** Technical standard for source files, requirement for K-12 materials under IDEA, XML-based format preserving structure, content, some formatting
- **NIMAS File Structure**: XML file, images, package document (OPF file)
- **NIMAS vs. Print**: Contains full text, structure, semantic information, image descriptions, MathML; may NOT contain exact visual layout, publisher styling, decorative elements
- **BrailleBlaster and NIMAS**: Can import NIMAS XML directly; maps structure to BrailleBlaster styles; converts MathML to ASCII Math; preserves images/descriptions
- **Benefits**: Structure preservation, MathML support, image descriptions, semantic information, standardization, time savings (50-80%), accuracy

## Teaching Strategy

**Start with Big Picture**: Explain NIMAS files are like "publisher's source code" containing structure and meaning without visual design.  
**The Workflow Advantage**: Traditional (100% manual) vs. NIMAS (20-50% manual for fine-tuning).

## Common Pitfalls &amp; Solutions

- **Assuming NIMAS is Perfect**: Expecting no manual adjustment → Emphasize still needs human review
- **Not Understanding MathML**: Confused by MathML → Provide overview; show conversion to ASCII Math
- **Ignoring Image Descriptions**: Not verifying/improving alt text → Teach that descriptions are included but may need enhancement
- **Not Checking Completeness**: Assuming file contains all content → Verify includes all text, images/descriptions, math, structural elements
- **Version Incompatibility**: Trying to import unsupported version → BrailleBlaster supports NIMAS 1.1; request compatible version

## Advanced Points

- **NIMAS File Structure Deep Dive**: Show package document, manifest, spine
- **MathML in NIMAS**: Show examples, compare to ASCII Math
- **NIMAS Tools**: NIMAS Center, APH, DAISY Consortium, MathML Tools
- **NIMAS Validation**: NIMAS Validator, DAISY Pipeline, BrailleBlaster import validation
- **NIMAS and Accessibility Laws**: IDEA, NIMAS Regulations (34 CFR Part 300), State Requirements
- **NIMAS Workflows**: Publisher → Agency, State Repository, NIMAC
- **Custom Processing**: Pre-process before import, create custom XSLT stylesheets, automate workflows

## Practice Design

- **Beginner**: Simple NIMAS files; import, verify structure
- **Intermediate**: NIMAS with math; import, verify conversion
- **Advanced**: Workflow requiring import/processing; complete workflow, verify output

## Assessment

- Import NIMAS files
- Understand structure
- Explain benefits
- Verify import quality
- Make adjustments
- Validate files
- Explain legal context
- Use in workflows
- Troubleshoot issues

## Teaching Time: 245 minutes (3+ pages)

---

# 13. Markdown/OpenOffice/LaTeX/XML Import

## Why This Matters

BrailleBlaster's ability to import from multiple formats makes it **versatile for different workflows and source materials**. Each format has strengths, weaknesses, typical use cases.

## Core Concepts

**Format Comparison**:


| Format     | Source      | Strengths        | Weaknesses                | Support       |
| ---------- | ----------- | ---------------- | ------------------------- | ------------- |
| Markdown   | Web/docs    | Simple, readable | Limited formatting        | Good          |
| OpenOffice | LibreOffice | Open standard    | Less common               | Good          |
| LaTeX      | Academia    | Precise math     | Steep learning curve      | Good (Pandoc) |
| XML        | Various     | Flexible         | Requires schema knowledge | Good          |


**Import Workflows**: Direct Import (Markdown, ODT, supported XML), Pandoc Conversion (LaTeX, some XML), Intermediate Formats (convert to HTML/DOCX first if direct fails)

## Teaching Strategy

**Start with Format Showcase**: Show same document in all formats. Discuss readability, structure preservation, compactness, best use cases.  
**The Decision Tree**: 1. What format is source? 2. What's document complexity? 3. What's import quality?

## Common Pitfalls &amp; Solutions

- **Assuming All Import Equally**: Expecting same quality from all formats → Test each; create reference document
- **Not Checking Math**: Importing with math but not verifying → Always check math in Braille View
- **Ignoring Encoding**: Garbled text from encoding issues → Teach encodings; show how to check/convert
- **Not Using Intermediate Formats**: Struggling with stubborn LaTeX → Use HTML/plain text first
- **Overlooking Format-Specific Features**: Not realizing some features are format-specific → Create reference chart

## Advanced Points

- **Markdown Extensions**: CommonMark, GitHub Flavored, math extensions, footnotes, definition lists
- **ODT Advanced Features**: Styles mapping, master documents, change tracking, forms/fields
- **LaTeX Deep Dive**: Math environments, macros, packages, custom commands
- **XML Schema Handling**: Identify schema, check support, create custom mappings
- **Pandoc Conversion**: Basic commands, options, filters, templates
- **Format-Specific Troubleshooting**: Markdown (math, tables, links), ODT (styles, math, merged cells), LaTeX (macros, packages), XML (schemas, namespaces, validation)
- **Best Practices**: Keep original, test with small section, verify structure/math/special content, document process

## Practice Design

- **Beginner**: Simple documents; import, verify basic structure
- **Intermediate**: Complex documents with math; import, verify all elements
- **Advanced**: Workflow requiring multiple conversions; determine best path, complete workflow

## Assessment

- Import all formats
- Convert LaTeX using Pandoc
- Explain format strengths/weaknesses
- Choose appropriate import path
- Troubleshoot import issues
- Use intermediate formats
- Verify import quality
- Document workflows

## Teaching Time: 245 minutes (3+ pages)

---

# 14. Transcriber Tasks: Running Heads and Page Numbering

## Why This Matters

Running heads and page numbering are **production-level features** separating hobbyist from professional. Crucial for navigation, consistency, compliance.

Unlike print (often automatic), in braille they require **explicit setup and management** by the transcriber.

## Core Concepts

- **Running Heads**: Headers at top of each page, typically document title, chapter title, or section title; provide context and navigation
- **Page Numbering**: Braille Page Numbers (⠼⠁, ⠼⠃), Print Page Numbers (original), Placement (bottom or in running head)
- **BANA Requirements**: Running heads centered, use Heading style; page numbers right-aligned, use Page Number style; first page different; consistency throughout section
- **The Transcriber's Responsibility**: BrailleBlaster doesn't automatically insert running heads or number pages; must **explicitly define** these elements

## Teaching Strategy

**Start with Print Comparison**: Show print book and braille equivalent. Point out running heads, page number formats, included information.  
**The Manual vs. Automatic Distinction**: In braille, **nothing is automatic**. Every element on every page must be explicitly defined.

## Common Pitfalls &amp; Solutions

- **Forgetting to Set Up**: Completing document, realizing no running heads → Make setup part of initial checklist; set before starting
- **Inconsistent Running Heads**: Different running heads without clear pattern → Create **running head map** for document
- **Running Heads on First Page**: Including full running head on first page → First page often has special running head (just title, without "continued" indicator)
- **Page Number Placement**: Left-aligned instead of right-aligned → BANA: right-aligned, Page Number style
- **Not Updating After Changes**: Changing structure but not updating running heads → After structural changes, always review/update running heads
- **Confusing Braille and Print**: Mixing up the two types → Teach distinction: Braille = sequential for braille doc (⠼⠁), Print = original print numbers

## Advanced Points

- **Running Head Types**: Static (same on every page), Dynamic (changes based on section), Combined (static + dynamic), Special (first page, title page)
- **Running Head Setup**: **Tools → Running Heads** → define content for different page types (First Page, Left Pages, Right Pages, Other Pages) → specify style (usually Heading) → specify placement (usually centered)
- **Page Numbering Setup**: **Settings → Page Numbers** → choose style (Braille, Print, Both) → placement (Top/Bottom) → alignment (Left/Center/Right) → style (usually Page Number)
- **Special Page Numbering**: Roman numerals (front matter), restart numbering (sections/volumes), skip numbering (title pages), custom formats
- **Running Heads and Styles**: Typically use Heading style but can use custom; appear **outside** main document flow; don't affect page break calculations
- **Multi-Volume Documents**: Each volume should have own running head setup; page numbering may continue or restart; volume numbers may be included
- **Automation with Macros**: Create macros to update all running heads after title change, apply consistent patterns, verify consistency
- **BANA Guidelines Deep Dive**: Placement (line 1), content (meaningful, consistent), formatting (Heading for heads, Page Number for numbers), special pages
- **Agency-Specific Standards**: Different requirements for running heads on every page, different types for different document types, specific page number formats

## Practice Design

- **Beginner**: Short document; set up simple running heads and page numbering
- **Intermediate**: Multi-chapter document; different running heads for sections
- **Advanced**: Complex document with front matter, chapters, special pages; complete system

## Assessment

- Set up basic running heads
- Set up page numbering per BANA
- Create different running heads for sections
- Handle special pages correctly
- Update running heads after changes
- Distinguish braille vs. print page numbers
- Apply agency-specific requirements
- Verify in embossed output
- Troubleshoot issues

## Teaching Time: 230 minutes (3+ pages)

---

# 15. Explicit Embosser Setup and Selection

## Why This Matters

While Chapter 6 covers basics, **explicit embosser setup and selection** is about **managing multiple embossers, advanced configurations, troubleshooting** in production. Crucial for agencies with multiple embossers, transcribers working with different types, production environments.

## Core Concepts

- **Embosser Profiles**: Saved configuration including device, manufacturer/model, settings, descriptive name
- **Profile Types**: Specific Model, Generic Text Only, Generic Text with Margins, Generic Graphics Embosser
- **The Profile Management Workflow**: Create → Test → Save → Select → Maintain
- **Embosser Types**: Single-Sided (Index Basic-D, Juliet), Double-Sided (Index Everest-D, ViewPlus), Graphics (ViewPlus Emprint SpotDot), High-Speed (Index V5, Braillo), Portable (Index Basic-S, BrailleNote)
- **Embosser Settings**: Page size, margins, interpoint, lines per page, cells per line, character set

## Teaching Strategy

**Start with a Tour**: Show different embosser models or pictures. Discuss how each works, best suited for, output looks like.  
**The Profile Creation Workshop**: Have trainees create profiles for different scenarios (classroom, production, graphics).

## Common Pitfalls &amp; Solutions

- **Using Generic When Specific Available**: Using Generic when model is listed → Always check if specific model available first
- **Incorrect Margin Handling**: Wrong setting (Text only vs. Text with margins) → "Margin test": Emboss test page, measure margins, adjust setting
- **Not Testing Profiles**: Creating profile without testing → Make testing **required step**
- **Confusing Profile with Document Settings**: Changing profile but not document settings → **Both** must be set correctly: Document Settings (page size, margins, interpoint) and Embosser Profile (device, margin handling)
- **Not Updating Profiles**: Using old profiles after changes → Create **profile maintenance schedule** (after driver updates, firmware updates, physical changes, quarterly)
- **Profile Name Confusion**: Unclear names → Descriptive naming ("Classroom - Index Basic-D - 11.5x11 - Interpoint")

## Advanced Points

- **Embosser Drivers**: Check installed, install new, update existing, remove old
- **Connection Types**: USB, Parallel Port, Serial Port, Network, Bluetooth
- **Multiple Embosser Management**: Create profile directory, set default profiles, create profile groups, implement testing protocol
- **Embosser-Specific Settings**: Index (Basic-D, Everest-D, V5), ViewPlus (Emprint SpotDot, color, resolution), Others (Juliet, Braillo)
- **Troubleshooting**: No output (power/connection/profile/default printer), wrong margins (profile/document), garbled text (translation/character set), paper jams (loading/size/debris), error codes (refer to manual)
- **Embosser Maintenance**: Cleaning pins, lubrication, paper handling, environment, manual consultation
- **Production Workflows**: Document Preparation → Profile Selection → Test Embossing → Production Embossing → Quality Check → Archive
- **Profile Sharing**: Share between computers/transcribers/agencies; backup/restore
- **Automation**: Macros to switch profiles, scripts to select based on document type, batch processing

## Practice Design

- **Beginner**: Embosser specifications; create basic profiles, test with simple documents
- **Intermediate**: Multiple embosser scenarios; create/test profiles for each
- **Advanced**: Production scenario with multiple embossers/document types; create complete profile management system

## Assessment

- Create profiles for different types
- Test profiles with test pages
- Troubleshoot profile issues
- Manage multiple profiles
- Update profiles as needed
- Use descriptive naming
- Perform basic maintenance
- Troubleshoot hardware issues
- Integrate into workflows
- Share profiles

## Teaching Time: 245 minutes (3+ pages)

---

# 16. Advanced Formatting: Boxed Material, Plays, Poems, and Deep Lists

## Why This Matters

Advanced formatting covers **special cases** that don't fit standard paragraph/list structures. Crucial for literary works, educational materials, technical documents. Mastering these separates **basic transcribers** from **advanced professionals**.

## Core Concepts

- **Boxed Material**: Text visually set off in box/border in print; purpose: draw attention to important information (theorems, definitions, warnings); braille equivalent: **Box style** or **Full Box style**; BANA: clearly set off with blank lines before/after
- **Types**: Simple Box, Full Box, Nested Boxes, Boxed Lists
- **Plays**: Structure (character names, dialogue, stage directions); Formatting: Character names (centered/specific margins), Dialogue (indented), Stage Directions (brackets/specific margins); BANA: *Dramatic Works in Braille* provides specific rules
- **Poems**: Structure (lines, stanzas); Formatting: Lines (**Poetry Line** style), Stanzas (**Poetic Stanza** style - container), Titles (centered/specific margins); BANA: *Poetry in Braille* provides specific rules
- **Deep Lists**: Lists with many nesting levels; BrailleBlaster supports up to **11-9 and 11-11 lists** (referring to braille cell positions)

## Teaching Strategy

**Start with Recognition**: Show print examples of each format. Discuss what makes it "special", purpose in print, how to achieve in braille.  
**The Container Concept**: Many advanced formats use **container styles** (Poetic Stanza, Full Box). Teach to identify in Breadcrumbs (prefixed with "CONTAINER"), understand that formatting container affects all within, use **Unwrap Element** to break containers.

## Common Pitfalls &amp; Solutions

- **Overusing Box Styles**: Applying to any slightly set-off text → "Box test": In print, is this actually in a box? If not, use different style
- **Inconsistent Play Formatting**: Different plays formatted differently → Create **play formatting guide** based on BANA's *Dramatic Works in Braille*
- **Poetry Line vs. Poetic Stanza Confusion**: Using wrong style → Poetry Line = individual lines; Poetic Stanza = container for multiple lines
- **Deep List Margin Errors**: Margins not working → Check **Style Levels** setting; may need to increase from default 5 to 8+
- **Not Verifying Braille View**: Not checking how it looks → Always check Braille View for advanced formatting

## Advanced Points

- **Box Style Variations**: Simple Box, Full Box, Nested Boxes, Boxed Lists
- **Play Formatting Deep Dive**: Character names (centered, specific margins), dialogue (indented 3-5 cells), stage directions (brackets, specific margins), scene/act headings (centered, special indicators), cast lists, dramatis personae
- **BANA Guidelines for Plays**: Character names (centered, specific style), dialogue (indented), stage directions (brackets, specific margins), scene/act headings (centered, special indicators)
- **Poetry Formatting Deep Dive**: Simple poems, stanza poems, indented poems, concrete poems, haikus/sonnets
- **BANA Guidelines for Poetry**: Lines (each gets own line), stanzas (separated by blank lines), indentation (preserved as much as possible), titles (centered), author names (end, sometimes special formatting)
- **Deep List Management**: Style Levels (increase from 5 to 8+), Margin Management (careful to avoid running out of space), List Markers (different levels use different braille markers), Nested Containers (lists within other containers)
- **Custom Styles**: Create custom styles (**Styles → Configure → Edit Styles**) for special formatting needs
- **Style Templates**: Create/save for specific publishers, document types, agency standards
- **Advanced Formatting and Embossing**: Boxed material (special margin handling), plays (special page break handling), poems (special line spacing), deep lists (page break placement); always test embossed output

## Practice Design

- **Beginner**: Simple examples of each format; apply basic styles
- **Intermediate**: Complex examples; apply appropriate styles, handle edge cases
- **Advanced**: Document with multiple advanced formatting elements; create complete formatting plan, apply it

## Assessment

- Apply Box/Full Box appropriately
- Format plays per BANA
- Format poems per BANA
- Create/manage deep lists
- Use container styles effectively
- Distinguish advanced formatting types
- Verify in Braille View
- Handle edge cases
- Create custom styles
- Troubleshoot issues

## Teaching Time: 275 minutes (3.5+ pages)

---

# 17. Contraction Relaxer

## Why This Matters

The **Contraction Relaxer** allows transcribers to **temporarily disable braille contractions** for specific passages. Crucial for computer code, mathematical notation, foreign languages, special requirements. Understanding when/how to use it marks an **advanced transcriber**.

## Core Concepts

- **Braille Contractions**: Shortened forms of common combinations (e.g., "ch" = ⠡, "sh" = ⠩); **Grade 2**: Uses contractions (standard); **Grade 1**: No contractions
- **The Relaxer Concept**: Temporarily relaxes contraction rules for specific passages, allowing Grade 1 where needed, switching back to Grade 2 afterward, maintaining both in same document
- **When to Use**: Computer Code (contractions would change meaning), Mathematical Notation (some agencies prefer uncontracted), Foreign Languages (non-English text), Special Requirements, Reader Requests
- **How It Works**: 1. Select text to relax, 2. Apply Relaxer (**Tools → Contraction Relaxer** or `Ctrl+Shift+G`), 3. Selected text switches to Grade 1, 4. Rest of document remains Grade 2
- **Visual Feedback**: Relaxed text may be highlighted/marked differently; always verify in Braille View

## Teaching Strategy

**Start with Contrast**: Show same passage in Grade 2 and Grade 1. Discuss differences in length, reading speed, clarity.  
**The "Meaning vs. Speed" Discussion**: Contractions exist to make reading faster, but sometimes **clarity** is more important.

## Common Pitfalls &amp; Solutions

- **Overusing**: Applying to large sections unnecessarily → Contractions are generally beneficial; only relax when specific reason
- **Underusing**: Not using when clearly needed → "Meaning test": Would contractions change meaning/cause confusion? If yes, use Relaxer
- **Not Verifying**: Not checking braille output → Always check Braille View
- **Inconsistent Application**: Applying to some code but not others → Create **relaxation plan** for document
- **Not Documenting**: Not documenting in Transcriber's Notes → **All** uses should be documented with explanation

## Advanced Points

- **Relaxer Granularity**: Character, word, passage, document levels
- **Relaxer and Other Formatting**: Can be applied to emphasized text, math-flagged text, any style
- **Relaxer Indicators**: Opening/closing indicators signal start/end; some agencies prefer no indicators (document in Notes)
- **BANA Guidelines for Grade 1**: Computer Code (should be Grade 1), Math (Grade 1 or Grade 2 with Nemeth), Foreign Languages (should be Grade 1), Special Symbols (may require Grade 1)
- **Agency-Specific Standards**: Different standards for Grade 1 vs. 2, indicators, documentation
- **Relaxer Workflows**: Initial Pass (transcribe Grade 2) → Identification Pass (identify passages) → Relaxation Pass (apply) → Verification Pass (verify) → Documentation Pass (document in Notes)
- **Relaxer and Math**: Some agencies prefer **all math in Grade 1**, others **math in Nemeth with Grade 2 context**; always document approach
- **Relaxer and Foreign Languages**: Apply to entire foreign passage, use **Script** emphasis, document language in Notes, consider adding pronunciation guide
- **Relaxer Shortcuts**: `Ctrl+Shift+G`
- **Relaxer and Find/Replace**: Use to identify passages needing relaxation (find all code blocks, foreign language passages, math), then apply Relaxer
- **Relaxer Testing**: Apply to test passage, check Braille View, emboss test page, verify with braille reader

## Practice Design

- **Beginner**: Documents with simple code snippets; apply Relaxer to code
- **Intermediate**: Documents with mixed content; identify/relax appropriately
- **Advanced**: Complex document with multiple passages; create relaxation plan, apply, document

## Assessment

- Identify passages needing relaxation
- Apply at different granularity levels
- Verify in Braille View
- Document in Transcriber's Notes
- Explain when/why to use
- Handle edge cases
- Use keyboard shortcut
- Integrate into workflows
- Troubleshoot issues

## Teaching Time: 175 minutes (2.5+ pages)

---

# 18. What Pandoc Does for BrailleBlaster

## Why This Matters

**Pandoc** is a **universal document converter**—command-line tool converting between virtually any document format. For BrailleBlaster, Pandoc is the **secret sauce** enabling import from unsupported formats (LaTeX, some XML).

## Core Concepts

- **What is Pandoc?** Command-line tool, universal document converter (40+ formats), open-source, powerful preprocessing tool for BrailleBlaster
- **Pandoc's Role**: Preprocessor for BrailleBlaster: Input (unsupported format) → Pandoc Conversion (intermediate format) → BrailleBlaster Import (intermediate format)
- **Supported Formats**: Input (Markdown, LaTeX, HTML, DOCX, ODT, EPUB, etc.), Output (HTML, DOCX, ODT, PDF, EPUB, Markdown, plain text, etc.)
- **The Conversion Chain**: LaTeX → (Pandoc) → HTML → (BrailleBlaster) → Braille
- **Pandoc's Strengths**: Format flexibility, structure preservation, math support, customization, automation
- **Pandoc's Limitations**: No GUI (command-line only), learning curve, not perfect (some formatting lost/changed), dependencies

## Teaching Strategy

**Start with the Problem**: "You receive a LaTeX document. BrailleBlaster can't open it directly. What do you do?" Then reveal Pandoc.  
**The Command-Line Concept**: For unfamiliar trainees, explain command line is text-based interface, commands are text instructions, options modify commands, arguments are inputs.

## Common Pitfalls &amp; Solutions

- **Fear of Command Line**: Intimidated by interface → Start with simple commands; use GUI wrappers if available
- **Not Installing**: Trying to use without installing → Provide clear installation instructions
- **Wrong File Paths**: "File not found" errors → Teach absolute paths, relative paths, drag-and-drop, directory navigation
- **Not Checking Quality**: Converting without verifying → Always check converted document before importing
- **Not Using Intermediate Formats**: Trying to convert directly to BrailleBlaster format → Pandoc converts **between document formats**, not to BrailleBlaster; use intermediate formats (HTML, DOCX) that BrailleBlaster can import

## Advanced Points

**Pandoc Installation**:

- **Windows**: Download installer from pandoc.org, run, check "Add to PATH", verify `pandoc --version`
- **Mac**: Install Homebrew, then `brew install pandoc`, verify `pandoc --version`
- **Linux**: Use package manager (Ubuntu: `sudo apt install pandoc`), verify `pandoc --version`

**Basic Commands**:

```
# Markdown to HTML
pandoc input.md -o output.html

# LaTeX to DOCX
pandoc input.tex -o output.docx

# EPUB to HTML
pandoc input.epub -o output.html

# Explicit formats
pandoc input.tex -f latex -t html -o output.html
```

**Pandoc Options**: Standalone (`-s`), Table of Contents (`--toc`), Math Support (`--mathjax`), Custom Templates (`--template=my-template.html`), Filters (`--lua-filter=my-filter.lua`)

**Pandoc and Math**: LaTeX math environments ($...$, \[...\]), macros (simple expanded, complex may need manual), packages (some not supported), custom commands (may need definition)

**Pandoc for Markdown**: Extensions (CommonMark, GitHub Flavored, math), math in Markdown ($...$ or $$...$$), YAML metadata

**Pandoc GUI Wrappers**: Pandoc GUI, Pandoc Editor, Markdown editors with built-in support

**Pandoc Documentation**: Manual (pandoc.org), cheat sheet, templates repository, filters repository

**Custom Workflows**: Identify input format → Determine best intermediate format → Create conversion command → Add post-processing → Document workflow

**Advanced Conversion**: Multi-stage conversion, custom filters, metadata processing, conditional conversion

## Practice Design

- **Beginner**: Simple documents in various formats; use basic commands, convert, import
- **Intermediate**: Complex documents; create custom commands with options, verify conversion
- **Advanced**: Workflow requiring multiple steps; create complete Pandoc workflow, document it

## Assessment

- Install Pandoc
- Run basic conversion commands
- Convert between various formats
- Use Pandoc options
- Integrate into BrailleBlaster workflows
- Troubleshoot conversion issues
- Create custom workflows
- Use for batch processing
- Document workflows

## Teaching Time: 245 minutes (3+ pages)

---

*Last updated: August 2026 | Comprehensive coverage of all BrailleBlaster\_Topics.md entries*