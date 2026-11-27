#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
ADMONITIONS_FILTER="$SCRIPT_DIR/../src/admonitions.lua"

if [[ ! -f "$ADMONITIONS_FILTER" ]]; then
    echo "Admonitions Lua filter not found: $ADMONITIONS_FILTER" >&2
    exit 1
fi

exec pandoc --lua-filter="$ADMONITIONS_FILTER" "$@"
