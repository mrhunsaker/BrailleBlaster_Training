#!/usr/bin/env python3
import json
import re
import sys

MAP = {
    "NOTE": "adm-note",
    "TIP": "adm-tip",
    "IMPORTANT": "adm-important",
    "WARNING": "adm-warning",
    "CAUTION": "adm-caution",
}

def transform_markdown(md: str) -> str:
    lines = md.splitlines(keepends=True)
    out = []
    i = 0
    pattern = re.compile(r"^>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*$", re.IGNORECASE)

    while i < len(lines):
        m = pattern.match(lines[i].strip())
        if m:
            kind = m.group(1).upper()
            env = MAP[kind]
            i += 1
            body_lines = []
            while i < len(lines) and lines[i].lstrip().startswith(">"):
                stripped = re.sub(r"^\s*>\s?", "", lines[i], count=1)
                body_lines.append(stripped)
                i += 1
            body_text = "".join(body_lines).strip()
            out.append(
                f"\n\n\\begin{{{env}}}\n{body_text}\n\\end{{{env}}}\n\n"
            )
        else:
            out.append(lines[i])
            i += 1

    return "".join(out)

def walk_chapters(items):
    for item in items:
        if "Chapter" in item:
            ch = item["Chapter"]
            ch["content"] = transform_markdown(ch["content"])
            if ch.get("sub_items"):
                walk_chapters(ch["sub_items"])

def main():
    _context, book = json.load(sys.stdin)
    walk_chapters(book.get("items", []))
    json.dump(book, sys.stdout)

if __name__ == "__main__":
    main()