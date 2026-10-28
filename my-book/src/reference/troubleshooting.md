# Troubleshooting

Work from the symptom to the most likely cause, and always confirm in the Braille View.

## Formatting

| Symptom | Likely cause | What to do | Lesson |
| ------- | ------------ | ---------- | ------ |
| Pasted text has no formatting | Pasted text always arrives as Body Text | Apply styles and emphasis deliberately | [1](../lessons/01-navigating-the-interface.md), [4](../lessons/04-layout-styles.md) |
| A style gives odd margins | Wrong style or level applied | Check Breadcrumbs, then the Style Appendix under **Help**. Do not type spaces | [4](../lessons/04-layout-styles.md) |
| A list or box covers too little or too much | Container did not wrap the full extent | Select the container in Breadcrumbs, or **Tools > Unwrap Element** and reapply | [4](../lessons/04-layout-styles.md) |
| **Unwrap Element** is greyed out | The selection is not a container style | Apply a different style directly | [4](../lessons/04-layout-styles.md) |
| Deeply nested list runs out of levels | Style levels set to the default five | **Styles > Configure > Style Levels** | [6](../lessons/06-list-formatting.md) |
| Headings look wrong after a Word import | Source used bold or large text instead of heading styles | Correct the styles in BrailleBlaster, or fix the source | [2](../lessons/02-opening-word-documents.md) |

## Math

| Symptom | Likely cause | What to do | Lesson |
| ------- | ------------ | ---------- | ------ |
| Equation looks like ordinary prose in braille | Math was not flagged | Select it and press `Ctrl+M`. Flagged text turns pink | [7](../lessons/07-math-translation-toggle.md) |
| Hyphens in compound words came out as minus signs | Too much text flagged as math | Remove the toggle from prose | [7](../lessons/07-math-translation-toggle.md) |
| Inserted equation is not pink | Math was not flagged after insertion | Check the Print View and flag it | [8](../lessons/08-ascii-math-hub.md) |
| Matrix or system is misaligned | Spaces were used instead of the spatial editor | Rebuild it in the Spatial Math Editor | [9](../lessons/09-spatial-math-editor.md) |
| LaTeX math is wrong | A package or command was not understood | Convert to HTML first, then re-check | [15](../lessons/15-importing-latex-xml-nimas-epub.md), [17](../lessons/17-what-pandoc-does.md) |

## Importing

| Symptom | Likely cause | What to do | Lesson |
| ------- | ------- | ---------- | ------ |
| A file opens but the structure is flat | The source has no real structure | Fix styles in BrailleBlaster, or ask for a better source | [2](../lessons/02-opening-word-documents.md) |
| An XML file does not behave like NIMAS | General XML is not NIMAS | Identify the vocabulary the XML uses | [15](../lessons/15-importing-latex-xml-nimas-epub.md) |
| Unfamiliar format will not import cleanly | Limited converter support | Convert to HTML, then open | [17](../lessons/17-what-pandoc-does.md) |
| Publisher note appears in the body | A NIMAS production note | Review notes with the production note tools | [20](../lessons/20-nimas-production-files.md) |

## Output

| Symptom | Likely cause | What to do | Lesson |
| ------- | ------------ | ---------- | ------ |
| Braille emerges on the wrong paper layout | Page properties do not match the paper | Set **Settings > Page Properties** before transcribing | [13](../lessons/13-paper-size-and-embossers.md) |
| Nothing embosses | Power, connection, wrong profile, or wrong default device | Check the device, then the profile | [13](../lessons/13-paper-size-and-embossers.md) |
| Output is wrong on an embosser with a listed model | Wrong manufacturer or model selected | Recheck the profile. Try Generic Text Only as a diagnostic, then Advanced options last | [13](../lessons/13-paper-size-and-embossers.md) |
| Sent the wrong thing to the embosser | **File > Print** sends the Print View to a printer | Use **File > Emboss** (`Ctrl+E`) | [13](../lessons/13-paper-size-and-embossers.md) |
| Running head collides with the page number | Running head too long for the longest page number | Shorten it | [21](../lessons/21-running-heads-and-page-numbers.md) |
| TOC does not match the volumes | TOC built before End of Volume markers | Insert markers first, then update and disperse | [23](../lessons/23-toc-and-volumes.md) |

## Safe habits that prevent most problems

- Work from a copy of the source.
- Save a dated copy before any large Replace All.
- Look at the Braille View after each change.
- Test emboss one page before a long job.
