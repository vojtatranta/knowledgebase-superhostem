#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
KB_DIR="$ROOT_DIR/knowledge base/html"
INDEX_FILE="$KB_DIR/index.html"

if [[ ! -f "$INDEX_FILE" ]]; then
  echo "Missing knowledge base index: $INDEX_FILE" >&2
  exit 1
fi

python3 - "$KB_DIR" "$INDEX_FILE" <<'PY'
from pathlib import Path
import re
import sys

kb_dir = Path(sys.argv[1])
index_file = Path(sys.argv[2])

html_files = sorted(p for p in kb_dir.glob("*.html"))
index_text = index_file.read_text(encoding="utf-8")

index_links = set(re.findall(r'href="\./([^"]+\.html)"', index_text))
index_links.add("index.html")

missing_from_index = []
broken_targets = []

for file in html_files:
    if file.name != "index.html" and file.name not in index_links:
        missing_from_index.append(file.name)

    text = file.read_text(encoding="utf-8")
    local_links = re.findall(r'href="\./([^"]+\.html)"', text)
    for target in local_links:
        target_path = kb_dir / target
        if not target_path.exists():
            broken_targets.append((file.name, target, "missing file"))
        elif target not in index_links:
            broken_targets.append((file.name, target, "not linked from index"))

if missing_from_index or broken_targets:
    if missing_from_index:
        print("Published KB files missing from index.html:", file=sys.stderr)
        for name in missing_from_index:
            print(f"  - {name}", file=sys.stderr)
        print(file=sys.stderr)

    if broken_targets:
        print("Article links pointing outside the public index:", file=sys.stderr)
        for source, target, reason in broken_targets:
            print(f"  - {source} -> {target} ({reason})", file=sys.stderr)

    sys.exit(1)

print("Knowledge base index consistency check passed.")
PY
