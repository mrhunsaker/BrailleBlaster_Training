#!/usr/bin/env bash
# Build the mdBook, normalize LaTeX admonitions, and compile the PDF source.
# Run from the repository root: bash build_script.sh

set -Eeuo pipefail

ROOT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
BOOK_DIR="$ROOT_DIR/my-book"
CLEANUP_SCRIPT="$ROOT_DIR/cleanup_admonition.sh"
TEX_FILE="$BOOK_DIR/docs/pandoc/tex/BrailleBlaster_Training.tex"

log() { printf '\n==> %s\n' "$*"; }
die() { printf 'Error: %s\n' "$*" >&2; exit 1; }

for command in mdbook mdbook-pandoc pandoc python3 perl lualatex; do
    command -v "$command" >/dev/null 2>&1 || die "Required command not found: $command"
done

[[ -f "$BOOK_DIR/book.toml" ]] || die "Cannot find mdBook config: $BOOK_DIR/book.toml"
[[ -f "$CLEANUP_SCRIPT" ]] || die "Missing cleanup script: $CLEANUP_SCRIPT"

# These preprocessors are referenced by my-book/book.toml. They are ignored by
# the repository's current .gitignore, so verify that they exist in this checkout.
for required_file in "$BOOK_DIR/scripts/admonitions_pre.py" "$BOOK_DIR/scripts/pandoc-admonitions.sh"; do
    [[ -f "$required_file" ]] || die "Required mdBook helper is missing: $required_file"
done

log "Building mdBook and Pandoc LaTeX output"
mdbook build "$BOOK_DIR"

[[ -f "$TEX_FILE" ]] || die "Pandoc LaTeX output not found. Expected: $TEX_FILE"

log "Normalizing admonition environments in $TEX_FILE"
bash "$CLEANUP_SCRIPT" "$TEX_FILE"

TEX_DIR="$(cd -- "$(dirname -- "$TEX_FILE")" && pwd)"
TEX_BASENAME="$(basename -- "$TEX_FILE")"
TEX_JOB="${TEX_BASENAME%.tex}"

cd "$TEX_DIR"

run_lualatex() {
    local pass="$1"
    log "LuaLaTeX pass $pass of 3"
    lualatex -interaction=nonstopmode -halt-on-error "$TEX_BASENAME"
}

# First LaTeX pass: generate auxiliary files, including the Biber control file.
lualatex -interaction=nonstopmode -halt-on-error "$TEX_FILE"

# Run Biber only when references are present.
BCF_FILE="${TEX_FILE%.tex}.bcf"
BIB_FILE="${TEX_FILE%.tex}.bbl"

if [[ -s "$BCF_FILE" ]]; then
    echo "Bibliography references detected. Running Biber..."
    biber "${TEX_FILE%.tex}"

    if [[ ! -f "$BIB_FILE" ]]; then
        echo "ERROR: Biber did not generate the expected bibliography file: $BIB_FILE" >&2
        exit 1
    fi
else
    echo "No bibliography control file found. Skipping Biber."
fi

# Additional LaTeX passes: resolve citations, cross-references, and layout.
lualatex -interaction=nonstopmode -halt-on-error "$TEX_FILE"
lualatex -interaction=nonstopmode -halt-on-error "$TEX_FILE"

# Generate the index only if an index file exists and contains entries.
IDX_FILE="${TEX_FILE%.tex}.idx"

if [[ -s "$IDX_FILE" ]]; then
    echo "Index entries detected. Running makeindex..."
    makeindex "$IDX_FILE"
else
    echo "No index entries found. Skipping makeindex."
fi

# Final LaTeX pass to incorporate the generated index.
if [[ -s "$IDX_FILE" ]]; then
    lualatex -interaction=nonstopmode -halt-on-error "$TEX_FILE"
fi

# Copy the final PDF to the repository root with the build date appended.
PDF_FILE="${TEX_FILE%.tex}.pdf"
BUILD_DATE=$(date +%Y%m%d)
ROOT_PDF="$ROOT_DIR/BrailleBlaster_Training_${BUILD_DATE}.pdf"

if [[ ! -f "$PDF_FILE" ]]; then
    echo "ERROR: Expected PDF was not generated: $PDF_FILE" >&2
    exit 1
fi

cp "$PDF_FILE" "$ROOT_PDF"

echo "Dated PDF copied to: $ROOT_PDF"