#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="$ROOT_DIR/knowledge base/html"

if [[ ! -d "$TARGET_DIR" ]]; then
  echo "Missing published knowledge base directory: $TARGET_DIR" >&2
  exit 1
fi

tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

run_check() {
  local name="$1"
  local pattern="$2"
  local output_file="$tmp_dir/$name.txt"

  if rg -n -i -P "$pattern" "$TARGET_DIR" >"$output_file"; then
    echo "Found blocked $name leak(s):" >&2
    cat "$output_file" >&2
    echo >&2
    return 1
  fi

  return 0
}

status=0

# Competitor/source-analysis leakage.
run_check "competition" '\b(konkurenc|konkurenč|konkurenčn|konkurent|competitor|competitive analysis|konkurenční výhod)\w*|\bvzorov(ý|eho|ém)\s+článk\w*' || status=1

# AI provenance leakage.
run_check "ai" '\b(chatgpt|openai|gpt-?[0-9.]*|llm|large language model|prompt(?:y|ing)?|uměl(?:á|e)\s+inteligenc\w*|generovan[ýáé]\s+(pomocí\s+)?ai)\b' || status=1

# Internal author/developer instructions that should not ship.
run_check "internal-notes" '\b(todo|fixme|placeholder|lorem ipsum|poznámka pro autora|poznámka pro developera|developer note|author note|interní poznámka|redakční poznámka|draft)\b' || status=1

if [[ "$status" -ne 0 ]]; then
  echo "Knowledge base publish safety check failed." >&2
  exit 1
fi

echo "Knowledge base publish safety check passed."
