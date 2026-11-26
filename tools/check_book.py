#!/usr/bin/env python3
"""Quality checks for the BrailleBlaster curriculum manuscript.

Run from the repository root: python3 tools/check_book.py
Exits with status 1 if any ERROR is found. Warnings do not fail the run.

Checks
  * every Markdown page is reachable from SUMMARY.md through linked index pages
  * every file has exactly one top-level heading
  * every relative link, and every #anchor, resolves
  * every lesson has a "Lesson at a glance" block and "Learning objectives"
  * every file linked from the Sample Files page exists
  * known-bad statements from earlier drafts do not creep back in
  * blank pages, heading-only pages, and explicit unfinished-content markers fail
"""
import glob
import os
import re
import sys

SRC = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "my-book", "src"))
errors, warnings = [], []


def read(path):
    with open(path, encoding="utf-8") as stream:
        return stream.read()


def slug(heading):
    """Approximates mdBook's heading ID generation."""
    heading = re.sub(r"\x60", "", heading).strip().lower()
    heading = re.sub(r"[^\w\- ]", "", heading, flags=re.UNICODE)
    return heading.replace(" ", "-")


def headings(text):
    found, fence = [], None
    for line in text.split("\n"):
        match = re.match(r"^\s*(\x60{3,}|~{3,})", line)
        if match:
            fence = None if fence and match.group(1)[0] == fence[0] else (fence or match.group(1))
            continue
        if fence is None:
            match = re.match(r"^(#{1,6}) (.*)", line)
            if match:
                found.append((len(match.group(1)), match.group(2).strip()))
    return found


def markdown_scan(text):
    """Remove fenced code blocks and inline code before scanning Markdown links."""
    text = re.sub(r"(?ms)^(\s*)(\x60{3,}|~{3,}).*?^\1\2[ \t]*$", "", text)
    return re.sub(r"\x60[^\x60\n]*\x60", "", text)


files = sorted(os.path.relpath(path, SRC) for path in glob.glob(SRC + "/**/*.md", recursive=True))
anchors = {}
for file_path in files:
    text = read(os.path.join(SRC, file_path))
    found = headings(text)
    anchors[file_path] = {slug(heading) for _, heading in found}
    if file_path != "SUMMARY.md":
        h1 = [heading for level, heading in found if level == 1]
        if len(h1) != 1:
            errors.append(f"{file_path}: expected 1 top-level heading, found {len(h1)}")


def linked_markdown_pages(file_path):
    """Yield local Markdown destinations linked from a Markdown page."""
    scan = markdown_scan(read(os.path.join(SRC, file_path)))
    for match in re.finditer(r"\]\(([^)\s]*)\)", scan):
        target = match.group(1)
        if not target or re.match(r"^[a-z]+:", target):
            continue
        link_path = target.partition("#")[0]
        if not link_path:
            continue
        destination = os.path.normpath(os.path.join(os.path.dirname(file_path), link_path))
        if destination.endswith(".md") and destination in anchors:
            yield destination


# SUMMARY.md is the navigation root. Supporting pages may be nested under unit,
# lab, sample, supplemental-practice, instructor, and reference indexes.
reachable, pending = set(), ["SUMMARY.md"]
while pending:
    current = pending.pop()
    for destination in linked_markdown_pages(current):
        if destination not in reachable:
            reachable.add(destination)
            pending.append(destination)

for file_path in files:
    if file_path != "SUMMARY.md" and file_path not in reachable:
        errors.append(f"{file_path}: not reachable from SUMMARY.md through linked index pages")


BAD = [
    r"OpenSCAD", r"3DMake", r"Relaxer[^\n]{0,40}Ctrl\+Shift\+G", r"File → ",
    r"BBZ\*\* is BrailleBlaster's default", r"Tools > Volume Manager",
    r"Tools > TOC Builder", r"Tools > T-Page",
    r"Contraction Relaxer\*\* and \x60Ctrl\+Shift\+T\x60", r"Relaxer, Ctrl\+Shift\+T",
    r"Help > Search", r"Style Appendix",
]
for file_path in files:
    text = read(os.path.join(SRC, file_path))
    for pattern in BAD:
        if re.search(pattern, text):
            errors.append(f"{file_path}: contains known-bad text /{pattern}/")

    scan = markdown_scan(text)
    for match in re.finditer(r"\]\(([^)\s]*)\)", scan):
        target = match.group(1)
        if not target or re.match(r"^[a-z]+:", target):
            continue
        link_path, _, anchor = target.partition("#")
        destination = os.path.normpath(os.path.join(os.path.dirname(file_path), link_path)) if link_path else file_path
        full_path = os.path.join(SRC, destination)
        if not os.path.exists(full_path):
            errors.append(f"{file_path}: broken link {target}")
            continue
        if anchor and destination.endswith(".md") and anchor not in anchors.get(destination, set()):
            errors.append(f"{file_path}: broken anchor {target}")


for file_path in files:
    if file_path.startswith("lessons/"):
        text = read(os.path.join(SRC, file_path))
        if "**Lesson at a glance**" not in text:
            errors.append(f'{file_path}: missing "Lesson at a glance"')
        if "## Learning objectives" not in text:
            errors.append(f'{file_path}: missing "Learning objectives"')
        if "## Source Citations" not in text and "## Source citations" not in text:
            warnings.append(f"{file_path}: no Source Citations section")


sample_index = os.path.join(SRC, "samples", "index.md")
if os.path.exists(sample_index):
    text = read(sample_index)
    for match in re.finditer(r"\]\(([^)#\s]+\.(?:docx|odt|epub|tex|html|xml|opf|zip|txt))\)", text):
        if not os.path.exists(os.path.join(SRC, "samples", match.group(1))):
            errors.append(f"samples/index.md: missing file {match.group(1)}")


STUB_PATTERNS = [
    r"(?im)^\s*TODO(?:[:\s]|$)",
    r"(?im)^\s*TBD(?:[:\s]|$)",
    r"(?i)content to be added",
    r"(?i)coming soon",
    r"(?i)this (?:page|file) is a placeholder",
    r"(?i)placeholder is retained",
    r"(?i)not yet implemented",
    r"(?i)to be completed later",
]
for file_path in files:
    text = read(os.path.join(SRC, file_path))
    visible = re.sub(r"(?s)<!--.*?-->", "", text).strip()
    found = headings(visible)
    if file_path != "SUMMARY.md" and (not visible or (len(found) == 1 and len(visible.splitlines()) <= 2)):
        errors.append(f"{file_path}: empty or heading-only manuscript page")
    for pattern in STUB_PATTERNS:
        if re.search(pattern, visible):
            errors.append(f"{file_path}: unfinished/stub content /{pattern}/")
    if re.search(r"(?m)^\s*#{2,6}\s*$", visible):
        errors.append(f"{file_path}: blank section heading")


print(f"Checked {len(files)} Markdown files.")
for warning in warnings:
    print("WARNING:", warning)
for error in errors:
    print("ERROR:  ", error)
print(f"{len(errors)} error(s), {len(warnings)} warning(s).")
sys.exit(1 if errors else 0)
