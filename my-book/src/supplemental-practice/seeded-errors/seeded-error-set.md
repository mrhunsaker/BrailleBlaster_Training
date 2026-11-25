# Seeded-Error Set: Proofreading and Production QA

Compare the supplied working copy to the source. The instructor may seed these defects in a project/export. Do not assume every visible difference is an error; verify against source and specification.

| ID | Intended defect | Category | Suggested severity |
|---|---|---|---|
| E01 | Level-two heading formatted as body text | Structure | Major |
| E02 | Nested list item promoted to outer level | Structure | Major |
| E03 | Emphasis applied to a whole sentence instead of marked term | Emphasis | Moderate |
| E04 | Find/replace changes part of an unrelated word | Content | Major |
| E05 | Math context ends one expression too early | Translation | Critical |
| E06 | Table header omitted from reconstructed table | Data integrity | Critical |
| E07 | Figure description omits the relationship central to the lesson | Accessibility | Major |
| E08 | Running head differs between two pages in one section | Pagination | Moderate |
| E09 | Volume boundary splits a section heading from its first paragraph | Production | Major |
| E10 | Stale production note remains in student-facing output | Cleanup | Moderate |
| E11 | Glossary cross-reference points to a nonexistent entry | Navigation | Major |
| E12 | Final proofread correction introduces a punctuation error | QA | Moderate |

For every defect, record location, source evidence, category/severity, proposed correction, and post-correction verification. A defect is not closed merely because its visible symptom disappeared.
