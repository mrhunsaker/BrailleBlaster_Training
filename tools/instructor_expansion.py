#!/usr/bin/env python3
"""One-time expansion of the Instructor Guide teaching notes.

Inserts a "Teaching strategy, pitfalls, and practice" block into each lesson's
section of my-book/src/instructor/unit-*.md. Idempotent: it skips a lesson that
already has the block. Content is vetted against the official BrailleBlaster
User Guide; where the earlier drafts disagreed with it, the guide won.
"""
import re, os
ROOT = os.path.join(os.path.dirname(__file__), '..', 'my-book', 'src', 'instructor')
MARK = '### Teaching strategy and practice design'

D = {
1: dict(strategy="Let learners explore a sandbox document before you explain anything. Ask them to change something in the Print View and predict what changes in the other two views.",
  pit=["Expecting to type in the Braille View → remind them the Print View is where text is edited.",
       "Hiding every view → at least one view must always stay displayed.",
       "Forgetting Breadcrumbs → turn them on at the start and leave them on."],
  adv="Customize the layout (rearrange views, icon size, toolbar groups) and compare setups with a partner.",
  tiers=("Open a document and name the three views.", "Rearrange the views and preview by print, braille, and ordinal page.", "Find five tools from the course in the menus without a map.")),
2: dict(strategy="Show the Word styles pane next to BrailleBlaster's Style View for the same file. The gap between what *looks* structured and what *is* structured is the lesson.",
  pit=["Assuming a document that looks right is built right → compare Sample files 01 and 02.",
       "Fixing problems one by one as they scroll past → insist on the Three-Pass Method (Lab 1).",
       "Fixing emphasis before structure → structure first, emphasis last."],
  adv="Triage: when a document is too far gone, copy the raw text into a new document and style it from scratch. Build a style map and write a note to the author.",
  tiers=("Open a well-structured file and verify the styles.", "Diagnose a flat file and write a style map.", "Triage an inconsistent file and decide between repair and rebuild.")),
3: dict(strategy="Start from meaning, not appearance: ask what the emphasis tells the *reader*. Then teach the mechanics, which are always select first and apply second.",
  pit=["Applying emphasis to everything that is bold in print → ask whether it carries meaning (Drill A7).",
       "Pressing the shortcut with nothing selected and expecting existing text to change → select first.",
       "Leaving print-only emphasis on headings → the heading style already says it."],
  adv="Combined typeforms, transcriber-defined typeforms (and their documentation on the Special Symbols page), and removing emphasis from a section.",
  tiers=("Apply bold and italic to selected text.", "Choose between symbol, word, and passage level.", "Decide about highlighting and document it.")),
4: dict(strategy="Teach the idea first: you choose what the text *is*, and BrailleBlaster chooses the margins. Then spend most of the time with Breadcrumbs visible.",
  pit=["Typing spaces to indent → apply a style.",
       "Not reading Breadcrumbs → they show containers that the Print View hides.",
       "Unwrap Element greyed out → the selection is not a container style; apply another style directly."],
  adv="Style levels (default five, up to eight), style loadouts with the Alt-number shortcuts, and the Style Appendix under Help.",
  tiers=("Apply a heading, a list, and a box.", "Read and explain a Breadcrumbs trail.", "Reformat a document using Repeat Last Style and Unwrap Element.")),
5: dict(strategy="Give learners a heading map worksheet. The skill is a *consistent* mapping from print levels to braille headings, with a reason.",
  pit=["Changing the mapping partway through a document → fix the map first, then apply it.",
       "Using more braille levels than the print has → compress per the section cited in the lesson.",
       "Faking a heading with spaces or blank lines → use the heading style."],
  adv="Paragraph headings, and the point at which a Transcriber's Note should explain a compressed hierarchy.",
  tiers=("Apply three heading levels.", "Compress a four-level hierarchy.", "Defend a mapping in writing.")),
6: dict(strategy="Start with the structural test: is this a real list? Then do nested lists and the margin formula.",
  pit=["Treating a sentence broken across bulleted lines as a list → Drill B3.",
       "Wrong runover → check the Braille View, not only the Print View.",
       "Running out of levels → Styles > Configure > Style Levels."],
  adv="Eight-level lists, and lists inside other containers.",
  tiers=("Format a simple list.", "Format a three-level list.", "Format the eight-level challenge list and explain the runover.")),
7: dict(strategy="Begin with the problem: braille uses the same symbols for letters and for math. Then let learners discover what goes wrong without the toggle.",
  pit=["Flagging every hyphen, number, or letter x → apply the sentence test and the context test.",
       "Flagging nothing → read the Braille View for obvious math in prose.",
       "Forgetting to check the pink highlight → math is highlighted bright pink in the Print View."],
  adv="UEB technical material and numeric passages, and Nemeth within UEB contexts. Agency conventions differ, so document the rule you follow.",
  tiers=("Flag a simple equation.", "Separate math from prose in a mixed paragraph.", "Choose Block versus Inline and justify it.")),
8: dict(strategy="Teach it as a tool for the unfamiliar. Learners who can already type an expression do not need the Hub. Learners who cannot, do.",
  pit=["Forgetting to click Insert → build, preview, insert, verify.",
       "Not checking that the result is flagged as math → look for the pink highlight.",
       "Reaching for the Hub for something trivial → know when typing is faster."],
  adv="Replace Current Math, Previous and Next Math for review, the Examples and Search tabs, and full-screen mode.",
  tiers=("Insert a fraction.", "Build a complex fraction and a nested exponent.", "Build a system, a matrix, and a piecewise function.")),
9: dict(strategy="Ask first whether position carries meaning. If it does, the answer is a spatial container, not spaces.",
  pit=["Faking alignment with spaces → use the Spatial Math Editor.",
       "Choosing the wrong container type → Matrix, Math Templates, Number Line Editor, or Regular Text.",
       "Trying to edit spatial math in the Print View → you cannot. Place the cursor in it and reopen the Spatial Math Editor."],
  adv="Matrix settings (grouping device, ellipsis in blank cells, wide-overflow style), math template types (simple, fraction, division), and grid alignment.",
  tiers=("Build a small matrix.", "Build aligned equations with a template.", "Build a long-division layout and a wide matrix.")),
10: dict(strategy="Start with a number line the learner has to *describe* to a partner, then build it. The settings are the lesson.",
  pit=["Overcrowding labels → a common rule of thumb is that a reader should be able to read the line within a comfortable span of one or two fingers; confirm your agency's guidance.",
       "Forgetting a text description or instruction to go with the line.",
       "Mixing up open and closed endpoints → empty circle versus full circle."],
  adv="Reduce Fraction, Beveled Fraction, Add Arrows, Stretch Across Page, Remove Leading Zeros, Math Entry versus User Text (with up to 10 markers), and Points versus Interval.",
  tiers=("Build a basic number line.", "Show an interval with mixed endpoints.", "Build a fraction number line with custom settings.")),
11: dict(strategy="Frame it as meaning versus speed. Contractions make reading faster, and sometimes exactness matters more.",
  pit=["Relaxing large passages out of habit → only with a reason.",
       "Not relaxing code → apply the meaning test.",
       "Not documenting → write the Transcriber's Note (Lab 7)."],
  adv="Work in passes: transcribe, identify, relax, verify, document. Compare with Direct translation and No Translate.",
  tiers=("Relax a code snippet.", "Handle mixed prose, code, and math.", "Write and defend a relaxation plan.")),
12: dict(strategy="Start with the danger, not the power. Show a Replace All that wrecks a document and recover from it.",
  pit=["Searching for a common word with no options → Whole Word and Match Case.",
       "Replace All without testing → Find first, then Replace one at a time for the first few.",
       "Ignoring scope → check whether the search covers the selection or the whole document.",
       "Assuming a search reveals what a line *is* → Lab 8, Task 3."],
  adv="Finding and replacing by formatting, style, or attribute through the Formatting window, resetting a search, and repeating the last search.",
  tiers=("Replace a word safely.", "Find and replace by formatting.", "Plan a multi-step cleanup and test each step.")),
13: dict(strategy="Bring real braille paper. Teach \"Print is for eyes. Emboss is for fingers.\" Make a test emboss non-negotiable.",
  pit=["Changing page properties after transcribing → set them first.",
       "Clicking Make Default too soon → use OK until the values are confirmed.",
       "Sending a job with Print instead of Emboss.",
       "Unclear profile names → use a naming pattern.",
       "Ignoring interpoint → it uses both sides of the sheet."],
  adv="Generic profiles (Text only, Text with margins, Graphics), multi-embosser management, profile maintenance, and a test-page protocol.",
  tiers=("Set page properties and preview.", "Create and test an embosser profile.", "Build a profile set for several devices and paper types.")),
14: dict(strategy="Use the same short document in every format and ask what survived.",
  pit=["Assuming every format imports equally well → test each one.",
       "Not checking math → always read the Braille View.",
       "Misreading Markdown lists → check nesting after import."],
  adv="Markdown variants and OpenDocument styles.",
  tiers=("Open each format.", "Record what survived.", "Recommend the best source format.")),
15: dict(strategy="Teach LaTeX through the math. Remind learners that BrailleBlaster converts LaTeX math to ASCII Math, and that unsupported notation is the exception to plan for.",
  pit=["Judging by the source instead of the result → read the Braille View.",
       "Treating general XML as NIMAS → they are different workflows.",
       "Fighting a stubborn LaTeX file → convert to HTML another way (Lab 3)."],
  adv="Macros, packages, and custom commands that BrailleBlaster does not support.",
  tiers=("Open a simple LaTeX file.", "Verify every equation.", "Use the HTML fallback.")),
16: dict(strategy="Make this a decision-making session: give learners descriptions of six sources and have them choose and defend a workflow.",
  pit=["Using one workflow for everything.", "Skipping the log.", "Not keeping the original."],
  adv="Documenting a repeatable workflow for an agency.",
  tiers=("Identify the format.", "Choose a workflow.", "Write the workflow as a procedure for others.")),
17: dict(strategy="Start with the problem, then reveal the tool. Make clear that Pandoc is a structure converter, and that BrailleBlaster opens LaTeX directly.",
  pit=["Fear of the command line → begin with one command and the cookbook.",
       "Wrong file paths → check the current folder.",
       "Converting without checking → treat the output as a new import."],
  adv="Options such as standalone output, table of contents, and math output.",
  tiers=("Explain what Pandoc does.", "Run a conversion.", "Document a fallback workflow.")),
18: dict(strategy="Recognition first: look at print examples and ask what each *does*. Then apply styles.",
  pit=["Using a box style for anything slightly set off → \"Is it really in a box in the print?\"",
       "Confusing a poetry line with a stanza container.",
       "Using inconsistent play formatting → write a one-page play guide.",
       "Not checking the Braille View."],
  adv="Nested boxes, concrete poems, line numbering with Tools > Line Number Tools (Wrap Prose, increment), and custom styles.",
  tiers=("Format a simple box, poem, and play.", "Format each with edge cases.", "Plan a document that mixes all three.")),
19: dict(strategy="Compare, do not drill. Show a BRF and an eBraille publication side by side if you can, and discuss what each is for.",
  pit=["Believing eBraille replaces BRF → it supplements it.",
       "Overstating tool support → check the installed version.",
       "Editing an eBraille package by hand → inspect, do not edit."],
  adv="Packaging, and the relationship to NIMAS tags.",
  tiers=("Explain eBraille.", "Choose the right format for a scenario.", "Inspect an `.ebrl` package.")),
20: dict(strategy="Frame NIMAS as the publisher's source: structure and meaning without visual design. Then make clear that it still needs a human.",
  pit=["Assuming it is perfect → review every element.",
       "Skipping image descriptions → use the Image Describer, and enhance descriptions where needed.",
       "Ignoring production notes → decide on each one.",
       "Not checking completeness → compare against the print."],
  adv="Dividing a NIMAS file among several transcribers, Alphabetic Reference tools, and the legal context (Policy and Standards Background).",
  tiers=("Open and navigate a NIMAS file.", "Decide on notes, sidebars, and images.", "Plan a multi-transcriber production.")),
21: dict(strategy="Print comparison: show a print book and the braille equivalent and point out what braille adds. In braille nothing is automatic.",
  pit=["Forgetting to set up → make it part of the start-of-job checklist.",
       "Running head too long for the longest page number.",
       "Confusing braille and print numbers → use the Braille Preview's three navigation modes.",
       "Not reviewing the Page Change List."],
  adv="Special page numbering, T-pages, and agency-specific standards.",
  tiers=("Add a running head and page numbers.", "Edit and delete numbers deliberately.", "Plan numbering for a multi-volume work.")),
22: dict(strategy="Teach the decision before the mechanics: is a note needed, and where does it belong?",
  pit=["Writing too many notes → a note is for the reader's need, not the transcriber's comfort.",
       "Mixing a print caption with a description → keep them apart.",
       "Putting a note in the wrong place → inline versus its own paragraph."],
  adv="Standard wording, and keeping the Transcriber's Notes page consistent with the notes in the text.",
  tiers=("Add an inline note.", "Add a paragraph note.", "Write a set of notes and make them consistent.")),
23: dict(strategy="Teach the sequence: plan, insert volume breaks, build the TOC, disperse, verify.",
  pit=["Building the TOC before volumes exist → Disperse to Volumes will warn you.",
       "Breaking volumes at an arbitrary sheet count → use natural boundaries.",
       "Page numbers with letters (such as C13) are not found automatically → use the Page Number tool.",
       "Forgetting to prepare the document → remove emphasis, delete bullets, format sidebars."],
  adv="TOC headings (Centered, Centered NB, Cell 5, Cell 7), Override Margin for multi-level TOCs, and Volume types.",
  tiers=("Insert volume breaks.", "Build and disperse a TOC.", "Plan and verify a four-volume set.")),
24: dict(strategy="Teach the production order: generate T-pages last, inside the generator, and then proofread.",
  pit=["Generating too early → volumes are not yet set.",
       "Editing T-pages in the Print View → those edits are lost when the generator reopens.",
       "Forgetting that special symbols are arranged by volume.",
       "Trusting Auto Fill blindly → check every symbol it finds."],
  adv="Auto Fill Options and rules for special symbols, Copy Current Volume, and the secondary title page.",
  tiers=("Generate a title page.", "Generate all pages for one volume.", "Generate pages for a multi-volume set and verify each.")),
}
LABS = {1:"Drill D; Lab 1",2:"Lab 1",3:"Drill A",4:"Drill B",5:"Drill B; Lab 9",6:"Drill B; Lab 9",7:"Drill C; Lab 7",8:"Drill C; Lab 3",9:"Lab 9",10:"Drill C",11:"Drill F; Lab 7",12:"Lab 8",13:"Drill E; Lab 5",14:"Lab 2",15:"Lab 2; Lab 3",16:"Lab 2",17:"Lab 3; Pandoc Cookbook",18:"Lab 9",19:"Policy background",20:"Lab 4",21:"Lab 6",22:"Lab 7",23:"Job Aid 6",24:"Job Aids 7 and 8"}

LABFILES = {1:'lab-1-rescue-word-document',2:'lab-2-import-comparison',3:'lab-3-when-latex-misbehaves',4:'lab-4-nimas-style-file',5:'lab-5-test-page-and-embosser',6:'lab-6-running-heads-and-page-numbers',7:'lab-7-relaxation-plan',8:'lab-8-find-and-replace-cleanup',9:'lab-9-special-structures'}
def linkify(txt):
    txt = re.sub(r'Lab (\d)', lambda m: f"[Lab {m.group(1)}](../labs/{LABFILES[int(m.group(1))]}.md)", txt)
    txt = re.sub(r'Drill ([A-F])', lambda m: f"[Drill {m.group(1)}](../reference/drill-bank.md)", txt)
    txt = txt.replace('Pandoc Cookbook', '[Pandoc Cookbook](../reference/pandoc-cookbook.md)').replace('Policy background', '[Policy and Standards Background](../reference/policy-background.md)')
    txt = re.sub(r'Job Aids? ([\d]+)( and (\d+))?', lambda m: m.group(0).replace('Job Aid', '[Job Aid').replace(m.group(0).split()[-1] if False else '', '') , txt) if False else txt
    return txt
def block(n):
    d = D[n]
    lines = [MARK, '', '**Strategy.** ' + d['strategy'], '', '**Common pitfalls and fixes**', ''] + ['- ' + p for p in d['pit']]
    lines += ['', '**Going further.** ' + d['adv'], '', '**Practice tiers**', '',
              '- *Beginner:* ' + d['tiers'][0], '- *Intermediate:* ' + d['tiers'][1], '- *Advanced:* ' + d['tiers'][2], '',
              '**Companion practice:** ' + linkify(LABS[n]) + '.', '']
    return '\n'.join(lines)

for u in (1, 2, 3):
    p = os.path.join(ROOT, f'unit-{u}.md')
    t = open(p, encoding='utf-8').read()
    parts = re.split(r'(?m)^(?=## Lesson \d+:)', t)
    out = [parts[0]]
    for part in parts[1:]:
        n = int(re.match(r'## Lesson (\d+):', part).group(1))
        if MARK in part: out.append(part); continue
        # insert after the first paragraph (the "Read the lesson" line)
        head, sep, rest = part.partition('\n\n')
        head2, sep2, rest2 = rest.partition('\n\n')
        out.append(head + '\n\n' + head2 + '\n\n' + block(n) + '\n' + rest2)
    open(p, 'w', encoding='utf-8').write(''.join(out))
print('expanded')
