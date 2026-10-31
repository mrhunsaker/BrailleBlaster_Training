#!/usr/bin/env python3
"""Quality checks for the BrailleBlaster curriculum manuscript.

Run from the repository root:   python3 tools/check_book.py
Exits with status 1 if any ERROR is found. Warnings do not fail the run.

Checks
  * every Markdown file is listed in SUMMARY.md (no orphan pages)
  * every file has exactly one top-level heading
  * every relative link, and every #anchor, resolves
  * every lesson has a "Lesson at a glance" block and "Learning objectives"
  * every file linked from the Sample Files page exists
  * known-bad statements from earlier drafts do not creep back in
"""
import glob, os, re, sys

SRC = os.path.join(os.path.dirname(__file__), '..', 'my-book', 'src')
SRC = os.path.abspath(SRC)
errors, warnings = [], []

def read(p): return open(p, encoding='utf-8').read()

def slug(h):
    """Approximates mdBook's heading id generation."""
    h = re.sub(r'`', '', h).strip().lower()
    h = re.sub(r'[^\w\- ]', '', h, flags=re.UNICODE)
    return h.replace(' ', '-')

def headings(text):
    out, fence = [], None
    for line in text.split('\n'):
        m = re.match(r'^\s*(`{3,}|~{3,})', line)
        if m:
            fence = None if fence and m.group(1)[0] == fence[0] else (fence or m.group(1)); continue
        if fence is None:
            m = re.match(r'^(#{1,6}) (.*)', line)
            if m: out.append((len(m.group(1)), m.group(2).strip()))
    return out

files = sorted(os.path.relpath(p, SRC) for p in glob.glob(SRC + '/**/*.md', recursive=True))
summary = read(os.path.join(SRC, 'SUMMARY.md'))
listed = {os.path.normpath(m) for m in re.findall(r'\]\(([^)#]+\.md)', summary)}

anchors = {}
for f in files:
    t = read(os.path.join(SRC, f))
    hs = headings(t)
    anchors[f] = {slug(h) for _, h in hs}
    if f != 'SUMMARY.md':
        if f not in listed: errors.append(f'{f}: not listed in SUMMARY.md')
        h1 = [h for lvl, h in hs if lvl == 1]
        if len(h1) != 1: errors.append(f'{f}: expected 1 top-level heading, found {len(h1)}')

BAD = [r'OpenSCAD', r'3DMake', r'Relaxer[^\n]{0,40}Ctrl\+Shift\+G', r'File → ', r"BBZ\*\* is BrailleBlaster's default",
       r'Tools > Volume Manager', r'Tools > TOC Builder', r'Tools > T-Page',          # these three live in the Debug menu in 3.x
       r'Contraction Relaxer\*\* and `Ctrl\+Shift\+T`', r'Relaxer, Ctrl\+Shift\+T',
       r'Help > Search', r'Style Appendix']  # neither exists in the 3.x Help menu  # Ctrl+Shift+T is Change Translation, not the Relaxer
for f in files:
    t = read(os.path.join(SRC, f))
    for pat in BAD:
        if re.search(pat, t): errors.append(f'{f}: contains known-bad text /{pat}/')
    # links
    for m in re.finditer(r'\]\(([^)\s]*)\)', t):
        target = m.group(1)
        if not target or re.match(r'^[a-z]+:', target): continue
        path, _, anchor = target.partition('#')
        dest = os.path.normpath(os.path.join(os.path.dirname(f), path)) if path else f
        full = os.path.join(SRC, dest)
        if not os.path.exists(full): errors.append(f'{f}: broken link {target}'); continue
        if anchor and dest.endswith('.md') and anchor not in anchors.get(dest, set()):
            errors.append(f'{f}: broken anchor {target}')

for f in files:
    if f.startswith('lessons/'):
        t = read(os.path.join(SRC, f))
        if '**Lesson at a glance**' not in t: errors.append(f'{f}: missing "Lesson at a glance"')
        if '## Learning objectives' not in t: errors.append(f'{f}: missing "Learning objectives"')
        if '## Source Citations' not in t and '## Source citations' not in t:
            warnings.append(f'{f}: no Source Citations section')

if os.path.exists(os.path.join(SRC, 'samples', 'index.md')):
    t = read(os.path.join(SRC, 'samples', 'index.md'))
    for m in re.finditer(r'\]\(([^)#\s]+\.(?:docx|odt|epub|tex|html|xml|opf|zip|txt))\)', t):
        if not os.path.exists(os.path.join(SRC, 'samples', m.group(1))):
            errors.append(f'samples/index.md: missing file {m.group(1)}')

print(f'Checked {len(files)} Markdown files.')
for w in warnings: print('WARNING:', w)
for e in errors: print('ERROR:  ', e)
print(f'{len(errors)} error(s), {len(warnings)} warning(s).')
sys.exit(1 if errors else 0)
