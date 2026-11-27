# Lesson 49: File Management, Backups, Version Control, and Student Privacy

> **Lesson at a glance**
>
> - **Unit:** Unit 5: Handbook (Supplemental)
> - **Suggested time:** about 2 hours
> - **Prerequisites:** [Lesson 13](13-paper-size-and-embossers.md), [Lesson 28](28-editing-the-translation.md), [Lesson 48](48-job-intake-and-the-agency-style-sheet.md)
> - **You will need:** A computer, and the sample files from the [Sample Files](../samples/index.md) page where a lesson uses them.

## Learning objectives

By the end of this lesson you will be able to:

- Organize a job into folders, name its files so that versions are never confused, and recover from a crash.
- Back up work so that no single failure loses it, and check that a copy is intact.
- Use version control for text sources, and know where it must not be used.
- Protect student information in file names, titles, logs, error reports, and shared files.

> [!WARNING]
> Do not put student names, disability details, school identifiers, or other protected information in filenames, public repositories, issue reports, screenshots, or unapproved cloud services. Use the organization's approved storage and sharing procedures.

## Why this matters

Braille production produces a lot of files for one job: the source, a working copy, the BBX, one or more BRFs, notes, and images. Within a month, nobody can tell which is current. A crash takes the afternoon's work. Worse, a file name carries a student's full name into an email, or a log is sent to a support service with a school's folder paths in it.

Good file habits prevent the first two problems, and good privacy habits prevent the third. Both are cheap to build and expensive to skip.

> [!NOTE]
> **About the tests in this lesson.** Where this lesson says what BrailleBlaster does with a file, the statement comes from reading BrailleBlaster's conversion script and from running that script on the sample files with Pandoc 3.12.1, the version the program bundles. It has **not** been confirmed by opening the files in the application. Treat each as an expectation, check it in your own copy, and report differences.

---

## How to use this lesson

Read **The Concept**, adopt the **folder and naming pattern** or adapt it to your agency's, and use the **privacy checklist** on every job. The practice asks you to audit a folder.

> [!IMPORTANT]
> **This lesson is not legal advice.** Student privacy is governed by law and by the policies of your school, district, and agency. Where they differ from anything here, **follow them**, and ask your administrator when in doubt.

---

## The Concept

### A folder for every stage

Keep the stages of a job apart, so that a source is never overwritten by your edits.

```text
2026-11-12_S4471_Energy-and-Motion/
  01_source/        the files exactly as received. Never edited
  02_working/       your BBX and any converted copies
  03_output/        the BRF or PEF for each volume, ready to emboss
  04_notes/         the ticket, the production log, the error log, questions
  05_archive/       older versions, kept until the job is closed
```

This matches the course's own pattern ([Setup](../start/setup.md)): a `sources` folder you do not edit, a `working` folder, and an `output` folder.

### Names that never collide

A good name says **when**, **for whom** (by ID), **what**, and **which version**. Put the date first in the form `YYYY-MM-DD` so that files sort in order.

| Pattern | Example |
| ------- | ------- |
| `YYYY-MM-DD_StudentID_Title_vN.ext` | `2026-11-12_S4471_Energy-and-Motion_v3.bbx` |
| BRF per volume | `2026-11-12_S4471_Energy-and-Motion_vol1.brf` |

- **Increase the version number** when you make a significant change. Do not name anything *final*, *final2*, or *newest*.
- **Avoid spaces and special characters** in file names. Use hyphens or underscores.
- **Never put a student's name in a file name.** Use an ID that only your agency can map to a name.

### Backups

A backup that sits beside the original is not a backup. The widely used **3-2-1 rule**:

- keep **three** copies of important work;
- on **two** different kinds of storage (for example a computer and an external drive); and
- **one** copy kept somewhere else (offsite, or in storage your agency approves).

A backup you have **never restored** is a hope. Once a term, open a backup file and confirm that it works.

**Check that a copy is intact** with a checksum, a short fingerprint of the file's contents:

```bash
sha256sum file.bbx                 # Linux
shasum -a 256 file.bbx             # macOS
Get-FileHash file.bbx -Algorithm SHA256   # Windows PowerShell
```

Two copies with the same checksum are identical.

### Recovery in BrailleBlaster

BrailleBlaster keeps automatic saves. If it closes unexpectedly, look under **File > Recent Auto Saves** for the document. This is a safety net, not a plan. **Save often with Ctrl+S**, and keep your own versions.

### Version control for text sources

**Git** records every change to a set of files, lets you compare versions, and lets you go back. It suits **text sources**: Markdown, LaTeX, plain text, and XML. A short routine:

```bash
git init                           # once, in the job folder
git add 01_source 04_notes         # choose what to track
git commit -m "Received source"    # a saved version, with a note
git log --oneline                  # the history
git diff                           # what changed since the last commit
```

> [!WARNING]
> Git is **not** a place for student data. Use a **private** repository only, and only if your agency allows it. **Never** put a student's name or records in a public repository, and be careful of hosted services whose servers are outside your agency's control. Git is also poor at binary files such as a `.bbz` or a `.docx`, because it cannot show what changed inside them.

### Retention and disposal

How long you keep a job's files, and how you destroy them afterward, is **your agency's policy**. In general:

- Keep the **source** and the **output** until delivery is confirmed.
- Keep **final BRFs** for as long as reprints may be needed, as policy allows.
- **Delete** drafts and temporary files that hold student information when the job closes.
- **Delete securely**: moving a file to the trash does not erase it.

---

## Student privacy

### What is at stake

In the United States, the **Family Educational Rights and Privacy Act** (FERPA) protects **education records**: information directly related to a student and kept by a school or by a party acting for it. A student's name tied to a disability, a school, or a grade is the kind of information that matters. Special education records also have confidentiality rules under the **Individuals with Disabilities Education Act** (IDEA), in 34 CFR Part 300, Subpart F. Many states and districts add their own rules.

A transcriber often works for a school or district as a **contractor**, and typically has access to student information only so far as the work requires. The safe habit is to **handle everything about a student as if it were confidential**, and to **use as little of it as the job needs**.

### The privacy checklist

| Where it can leak | What to do |
| ----------------- | ---------- |
| **File names and folder names** | Use a student **ID**, not a name |
| **The text of the document** | A worksheet may carry a name at the top. Ask whether to transcribe it, and whether to replace it with an ID |
| **The title page** | Include a student's name only if your agency requires it |
| **Email** | Send student documents only through **approved, secure channels**. Do not put a name in a subject line |
| **Cloud storage and shared drives** | Use only what your agency approves |
| **Logs and screenshots** | They show paths, file names, and text. Check them before sharing |
| **Error reports** | See below |
| **Translation corrections** | A word saved **globally** is sent to APH ([Lesson 28](28-editing-the-translation.md)) |
| **Secure test materials** | Follow the testing agency's rules. Do not keep copies outside the approved process |
| **Old files** | Delete them at the end of the job, securely |

### What BrailleBlaster shares, and when

BrailleBlaster has a **Privacy settings** tab, on the **Help** menu. It offers two choices:

- **Usage reporting**, a checkbox: *I want to help make BrailleBlaster better by sharing usage data with APH.* It is a choice you make.
- **Updates**: *Automatically check for updates.*

APH's privacy policy, which ships with the program, says that if you press the **Report Error** button, APH **collects the error's stack trace, the version number, a generated unique ID saved in your settings, and your IP address**, and uses them to process your report and provide support. A **stack trace** is the program's own record of what failed. It does not normally include your document. **Help > View log** shows a record of what the program has written, and it can include **file paths**, which may contain folder names. Read a log before you send it.

> [!NOTE]
> Read the current **APH Privacy Policy** for yourself. A copy is installed with the program, and it is published on APH's website. It may change between versions, and your agency may have its own requirements about usage reporting. Ask your administrator before you turn it on.

---

## Step by step

### Start a job safely

1. Create the **folder structure** with the student's **ID** in the name.
2. Put the received files in `01_source` and **do not edit them**.
3. Work on a **copy** in `02_working`, and save with a **new version number** at each milestone.
4. **Back up** at the end of each session, and verify with a checksum.
5. Keep **no names** in file names, logs, or notes.

### Close a job safely

1. Confirm **delivery**.
2. Archive or delete according to **policy**.
3. **Securely delete** drafts and temporary files.
4. Record **where the final files are** on the ticket.

---

## Practice

### The folder audit

A transcriber's desktop contains these items. Find the problems.

```text
Desktop/
  Maria Gonzalez IEP notes.docx
  science chapter FINAL.docx
  science chapter FINAL2.docx
  science chapter FINAL2 (copy).bbx
  chapter4.brf
  email to Mrs Chen about Jason.txt
  BB log sent to support.txt
  backup-folder-on-same-disk/
```

### Tasks

1. List at least **eight** problems.
2. Rename the three science files and the BRF using the pattern in this lesson, for student ID S4471, a chapter titled "Energy and Motion", dated 2026-11-12.
3. What is wrong with a backup folder on the same disk?
4. The transcriber is asked to send the log to support. What should be checked first?
5. A teacher emails the file `Maria-math-test.docx`. What do you do?
6. Why is Git not suited to a `.bbz` file?

### Answer Key

1. The problems:
   1. A **student's full name** in a file name (*Maria Gonzalez IEP notes*), and **IEP notes**, which are sensitive records, on a desktop.
   2. **`FINAL`, `FINAL2`, and `(copy)`**: nothing says which is current.
   3. **A `.docx` and a `.bbx` mixed together** with no folder structure.
   4. A **BRF with no date, student ID, or version** (`chapter4.brf`).
   5. **A text file named for a teacher and a student** (*Mrs Chen about Jason*), which looks like student information in a loose file.
   6. **A log "sent to support"** that may carry file paths and names.
   7. **A backup on the same disk**, which is not a backup.
   8. **Everything on the desktop**, with no stages, no archive, and no retention plan.
2. Example names: `2026-11-12_S4471_Energy-and-Motion_v1.docx` (the source, in `01_source`), `2026-11-12_S4471_Energy-and-Motion_v2.bbx` (the working file), and `2026-11-12_S4471_Energy-and-Motion_vol1.brf` (the output). Any consistent version scheme is acceptable.
3. If the disk fails or is stolen, the original and the backup are **lost together**. A backup needs a **different** storage device, and one copy elsewhere.
4. **Read it first.** Look for **file paths, names, and text** that identify a student or a school, and remove or redact them, or ask the administrator. Send only what support needs.
5. **Ask the teacher** whether the student's name needs to appear, and **replace it with an ID** in the file name for your own files. Reply on the approved channel, and keep the original only as policy allows.
6. A `.bbz` is a **zip file**. Git stores it as one opaque blob, so it cannot show **what changed** inside it, and every version takes the full space.

---

## Key takeaways

- Separate the stages: **source, working, output, notes, archive**. Never edit the source.
- Name files `YYYY-MM-DD_StudentID_Title_vN.ext`. **No student names**, and no *final2*.
- Follow **3-2-1**, verify with a **checksum**, and **test a restore**. Use **File > Recent Auto Saves** after a crash.
- **Git** suits text sources in a **private** repository, and never public student data.
- **Handle everything about a student as confidential.** Check logs and error reports first, and use **Help > Privacy settings** with your administrator's agreement.
- This lesson is **not legal advice**. Follow your school, district, and agency policy.

---

## Source Citations

- The BrailleBlaster program source (the **File > Recent Auto Saves** menu item and the **Privacy settings** tab) and the *APH Privacy Policy* that ships with the program.
- U.S. Department of Education, *Family Educational Rights and Privacy Act (FERPA)*, at [studentprivacy.ed.gov](https://studentprivacy.ed.gov/), and 34 CFR Part 300, Subpart F (confidentiality of information), under IDEA.
- [Lesson 28](28-editing-the-translation.md) for global translation corrections, and [Policy and Standards Background](../reference/policy-background.md).
