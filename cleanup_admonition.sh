#!/usr/bin/env bash
# Convert mdBook/Pandoc's escaped admonition markers into LaTeX environments.
# Usage: cleanup_admonition.sh [--dry-run] file.tex [file2.tex ...]

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

command -v perl >/dev/null 2>&1 || {
    echo "Error: Perl is required but was not found in PATH." >&2
    exit 1
}

status=0
for file in "$@"; do
    if [[ ! -f "$file" ]]; then
        echo "Skipping missing file: $file" >&2
        status=1
        continue
    fi

    tmp=$(mktemp "${TMPDIR:-/tmp}/cleanup-admonition.XXXXXX")
    trap 'rm -f "$tmp"' EXIT

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
            "\\begin{" . $1 . "}\n" . $2 . "\\end{" . $1 . "}\n"
        }gsex;
    ' "$file" > "$tmp"

    if cmp -s "$file" "$tmp"; then
        echo "No matching admonitions found: $file"
        rm -f "$tmp"
        trap - EXIT
        continue
    fi

    if [[ $dry_run -eq 1 ]]; then
        echo "Would update: $file"
        diff -u -- "$file" "$tmp" || true
        rm -f "$tmp"
        trap - EXIT
        continue
    fi

    backup="${file}.bak"
    if [[ -e "$backup" ]]; then
        backup="${file}.$(date '+%Y%m%d-%H%M%S').bak"
        suffix=1
        while [[ -e "$backup" ]]; do
            backup="${file}.$(date '+%Y%m%d-%H%M%S').${suffix}.bak"
            suffix=$((suffix + 1))
        done
    fi

    cp -p -- "$file" "$backup"
    cat "$tmp" > "$file"
    rm -f "$tmp"
    trap - EXIT
    echo "Updated: $file (backup: $backup)"
done

exit "$status"
