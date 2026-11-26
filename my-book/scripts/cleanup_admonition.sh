#!/usr/bin/env bash
#
# Convert escaped admonition markers such as:
#   \textbackslash begin\{adm-tip\}
#   ...content...
#   \textbackslash end\{adm-tip\}
#
# into real LaTeX environments:
#   \begin{adm-tip}
#   ...content...
#   \end{adm-tip}
#
# Usage:
#   ./cleanup_admonition.sh [--dry-run] file.tex [file2.tex ...]
#
# Perl is required. Changed files are backed up as file.tex.bak.
#

set -euo pipefail

dry_run=0
if [[ "${1-}" == "--dry-run" ]]; then
    dry_run=1
    shift
fi

if [[ $# -eq 0 ]]; then
    echo "Usage: $0 [--dry-run] file.tex [file2.tex ...]" >&2
    exit 2
fi

if ! command -v perl >/dev/null 2>&1; then
    echo "Error: Perl is required but was not found in PATH." >&2
    exit 1
fi

status=0

for file in "$@"; do
    if [[ ! -f "$file" ]]; then
        echo "Skipping: not a regular file: $file" >&2
        status=1
        continue
    fi

    tmp=$(mktemp "${TMPDIR:-/tmp}/cleanup-admonition.XXXXXX")

    # Read the whole file so admonition content may span multiple lines.
    perl -0777 -pe '
        s{
            \\textbackslash\ begin\\\{
            (adm-(?:note|caution|tip|important|warning))
            \\\}
            (.*?)
            \\textbackslash\ end\\\{
            \1
            \\\}
        }{
            "\\begin{" . $1 . "}\n" . $2 . "\n\\end{" . $1 . "}\n"
        }gsex;
    ' "$file" > "$tmp"

    if cmp -s "$file" "$tmp"; then
        echo "No matching admonitions found: $file"
        rm -f "$tmp"
        continue
    fi

    if [[ $dry_run -eq 1 ]]; then
        echo "Would update: $file"
        diff -u -- "$file" "$tmp" || true
        rm -f "$tmp"
        continue
    fi

    backup="${file}.bak"
    if [[ -e "$backup" ]]; then
        echo "Error: backup already exists; refusing to overwrite: $backup" >&2
        rm -f "$tmp"
        status=1
        continue
    fi

    cp -p -- "$file" "$backup"
    cat "$tmp" > "$file"
    rm -f "$tmp"
    echo "Updated: $file (backup: $backup)"
done

exit "$status"
