# Codex Notes

## Project

This repo is `superhostem-KB`, a static knowledge base for Superhostem.

- Main content lives in `knowledge base/`.
- Public-compatible alias `knowledge-base` points to `knowledge base`.
- HTML output lives in `knowledge base/html/`.
- Shared CSS: `knowledge base/assets/superhostem.css`.
- Shared JS: `knowledge base/assets/kb-navigation.js`.
- Remote: `https://github.com/yun0de/superhostem-KB`.

## Local Preview

Serve from `knowledge base/`, not from `knowledge base/html/`.

```sh
cd "/Users/phnguyen/Documents/Projects/superhostem-KB/knowledge base"
python3 -m http.server 8080
```

Main URL:

```text
http://localhost:8080/html/index.html
```

## Recent Work Summary

- Added missing index links for city fee articles.
- Added root redirect `knowledge base/index.html`.
- Expanded article `co-vsechno-najdu-v-detailu-rezervace` in CZ/EN/VN.
- Added CTA to message automation in that reservation detail article.
- Styled article CTA link lists (`.kb-article-link-list`) as cards.
- Styled rich article CTA component (`.kb-article-next-cta`).
- Added homepage live search suggestions with keyboard support.
- Fixed homepage anchor navigation around `Začínáme`, `Knihovna`, `Nejčtenější`.
- Changed language switcher to globe dropdown, like main `superhostem.cz`.
- Changed light/dark switcher to compact dropdown.
- Rolled header menu CSS/JS cache-bust across all 66 HTML files.
- Fixed `jak-pridat-novou-nemovitost` tip blocks by adding `.kb-article-tip` CSS.

## Important Checks

Useful checks before commit/push:

```sh
git diff --check
node --check "knowledge base/assets/kb-navigation.js"
bash scripts/check-kb-publish-safety.sh
```

Known issue:

- `scripts/check-kb-index-consistency.sh` may still fail because EN/VN articles are not all linked from public indexes.

## Git Notes

Git remote push can succeed while local `origin/main` ref update fails with:

```text
cannot lock ref 'refs/remotes/origin/main'
```

When that happens, verify remote with:

```sh
git ls-remote origin refs/heads/main
git rev-parse HEAD
```

If SHA matches, push is OK even if `git status` says `ahead`.

## Untracked Files

Do not accidentally commit:

- `.DS_Store`
- `knowledge base/articles/.DS_Store`
- AIDesigner/Codex setup files unless explicitly wanted:
  - `.agents/`
  - `.aidesigner/`
  - `.claude/`
  - `.codex/`
  - `.mcp.json`

## AIDesigner State

AIDesigner init was attempted.

- Project config files were created locally.
- MCP login succeeded once.
- Current session did not hot-load AIDesigner tools.
- Fresh Codex session may be needed for AIDesigner MCP.

## Latest Published Commit

Latest pushed fix:

```text
c4409e9 fix: style add-property article tips
```
