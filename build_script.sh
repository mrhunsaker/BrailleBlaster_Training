#!/usr/bin/env bash
# Build the mdBook, normalize LaTeX admonitions, and compile the PDF source.
# Run from any directory: ./build_script.sh

set -Eeuo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
BOOK_DIR="$ROOT_DIR/my-book"
CLEANUP_SCRIPT="$ROOT_DIR/cleanup_admonition.sh"
TEX_FILE="$BOOK_DIR/docs/pandoc/tex/BrailleBlaster_Training.tex"

log() { printf '\n==> %s\n' "$*"; }
die() { printf 'Error: %s\n' "$*" >&2; exit 1; }

for command in mdbook perl lualatex; do
    command -v "$command" >/dev/null 2>&1 || die "Required command not found: $command"
done

[[ -f "$BOOK_DIR/book.toml" ]] || die "Cannot find mdBook config: $BOOK_DIR/book.toml"
[[ -x "$CLEANUP_SCRIPT" ]] || die "Missing or non-executable cleanup script: $CLEANUP_SCRIPT"

log "Building mdBook and Pandoc LaTeX output"
mdbook build "$BOOK_DIR"

[[ -f "$TEX_FILE" ]] || die "Pandoc LaTeX output not found. Expected: $TEX_FILE"

log "Normalizing admonition environments in $TEX_FILE"
"$CLEANUP_SCRIPT" "$TEX_FILE"

TEX_DIR="$(cd -- "$(dirname -- "$TEX_FILE")" && pwd)"
TEX_BASENAME="$(basename -- "$TEX_FILE")"
TEX_JOB="${TEX_BASENAME%.tex}"

cd "$TEX_DIR"

run_lualatex() {
    local pass="$1"
    log "LuaLaTeX pass $pass of 3"
    lualatex -interaction=nonstopmode -halt-on-error "$TEX_BASENAME"
}

# First pass writes the .toc/.lot files and, if configured, the .idx file.
run_lualatex 1

# Only run makeindex when LaTeX actually emitted index entries.
if [[ -s "$TEX_JOB.idx" ]]; then
    command -v makeindex >/dev/null 2>&1 || die "Index entries were generated ($TEX_JOB.idx), but makeindex is not installed."
    log "Generating the index"
    makeindex "$TEX_JOB.idx"
fi

# Second and third passes resolve the TOC, list of tables, page references,
# and any generated index references.
run_lualatex 2
run_lualatex 3

log "Build complete"
printf 'PDF: %s/%s.pdf\n' "$TEX_DIR" "$TEX_JOB"
