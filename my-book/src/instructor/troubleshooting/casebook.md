# BrailleBlaster Training Troubleshooting Casebook

| Symptom | Possible cause | Diagnostic approach | Safe next step |
|---|---|---|---|
| Imported headings absent from navigation | Source headings are visual-only or mapped incorrectly | Inspect source styles/markup and imported structure | Correct semantic styles/mapping, then reimport/test |
| List numbering inconsistent | Mixed manual numbering and real list structure | Inspect source paragraphs and list levels | Normalize list structure in a working copy |
| Math passage translates inconsistently | Context boundary or mode selection is wrong | Compare source expression and context scope | Correct scope and verify adjacent prose |
| Table data detached from headers | Header relationships were lost | Compare each row/column to source | Rebuild or linearize with explicit relationships |
| Running head changes unexpectedly | Section/page setup or inherited formatting differs | Inspect section boundaries and settings | Correct responsible section and inspect neighbors |
| TOC references stale | Pagination or volume boundaries changed after generation | Compare TOC with current output | Regenerate and verify references |
| Figure description too long | Description includes irrelevant visual detail | Revisit instructional purpose and reader task | Prioritize essential relationships and data |
| Find/replace damages unrelated text | Search scope or match options too broad | Review change history and search terms | Undo, narrow scope, repeat, verify |
| Output differs after embossing | Page setup, embosser configuration, or device behavior | Compare electronic layout and test output | Validate settings and run controlled sample |
| eBraille navigation incomplete | Metadata/landmarks or source semantics insufficient | Test in target reading environment | Repair structure and retest compatibility |

For every case, require a record of symptom, evidence, hypothesis, test, correction, and post-fix verification. Avoid destructive troubleshooting on the only copy of a project.
