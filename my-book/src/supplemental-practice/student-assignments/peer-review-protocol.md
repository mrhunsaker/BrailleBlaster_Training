# Capstone Peer-Review Protocol

Use this protocol for a structured review of another learner's capstone package. The purpose is to test the clarity and verifiability of the work, not to impose identical formatting choices where more than one approach is defensible.

## Review rules

1. Review the source, project, exported output, production log, and handoff as a connected package.
2. Separate observable defects from preferences. Cite a source location or output location for every defect.
3. Do not silently repair the author's work. Record the finding and let the author respond.
4. Treat meaning, omission, access, and safety-critical production defects as priority issues.
5. If a decision depends on an agency or client specification that is not supplied, record the missing authority instead of inventing a rule.

## Review sequence

### 1. Package completeness

- Can each deliverable be identified from the manifest?
- Is the original source preserved?
- Are the working project and exported volumes clearly named?
- Are the stated software version and production assumptions recorded?

### 2. Source fidelity and structure

- Compare representative passages against the source.
- Check heading hierarchy, list nesting, emphasis, notes, tables, and figures.
- Look for missing, duplicated, reordered, or unintentionally altered content.
- Confirm that visual appearance has not been mistaken for semantic structure.

### 3. Translation and access

- Ask the author to explain two non-obvious math, technical, or translation decisions.
- Check that local corrections are scoped narrowly and verified in context.
- Confirm that figure treatment communicates information needed by the learning task.
- Check that table reading order preserves meaningful relationships.

### 4. Production and pagination

- Compare the volume plan with actual output.
- Check that contents, page references, running heads, volume breaks, and preliminary pages agree.
- Verify that exported files correspond to the final project version.
- Record any physical embossing checks that remain to be performed.

### 5. Quality assurance and handoff

- Confirm that logged defects have dispositions and rechecks.
- Confirm that unresolved questions are visible to the recipient.
- Check that the handoff does not claim checks that are not evidenced.

## Findings register

Use one row per finding. Include enough information for the author to reproduce it.

| ID | Severity | File / location | Expected | Observed | Recommended action | Recheck |
|---|---|---|---|---|---|---|
| | Critical / Major / Minor / Note | | | | | |

**Severity guide**

- **Critical:** meaning is materially changed, content is missing, or a major access defect prevents the intended use. Do not approve until resolved.
- **Major:** structural, translation, navigation, or production defect with substantial reader or workflow impact.
- **Minor:** localized defect with limited impact that should be corrected before final release where practical.
- **Note:** question, improvement opportunity, or documentation gap that is not itself a confirmed defect.

## Reviewer summary

**Strengths supported by evidence:**

**Highest-priority findings:**

**Questions for the author:**

**Checks that could not be completed:**

**Recommendation:** Approve / Approve after minor corrections / Revise and resubmit / Hold pending specification

## Author response and closure

For each finding, record the response, correction, and verification evidence. A finding is closed only after the correction is rechecked in the relevant context and affected downstream outputs are regenerated or revalidated.

| Finding ID | Author response | Change made | Verification evidence | Closed by / date |
|---|---|---|---|---|

## Reflection

After the review, each learner answers:

1. Which finding most improved the reliability or accessibility of the package?
2. Which reviewer comment required clarification before action?
3. What downstream checks were necessary after a correction?
4. What will you change in your own production workflow?
