#!/usr/bin/env python3
"""Generate sitemap.xml at the repo root for the Superhostem knowledge base."""
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KB_DIR = REPO_ROOT / "knowledge base"
SITE = "https://knowledgebase.superhostem.cz"
SITEMAP_PATH = REPO_ROOT / "sitemap.xml"

LANG_ALTERNATES = {
    "cs": "",
    "en": "en/",
    "vn": "vn/",
}


def url_path_from_file(rel_path: str) -> str:
    """Return the public URL path for a file relative to KB_DIR."""
    # e.g. "html/index.html" -> "/knowledge-base/html/index.html"
    return f"/knowledge-base/{rel_path}"


def collect_html_files():
    """Collect all HTML files under the knowledge base directory."""
    files = []
    files.extend(sorted(KB_DIR.glob("*.html")))
    files.extend(sorted(KB_DIR.glob("html/*.html")))
    files.extend(sorted(KB_DIR.glob("html/en/*.html")))
    files.extend(sorted(KB_DIR.glob("html/vn/*.html")))
    files.extend(sorted(KB_DIR.glob("articles/*.html")))
    return files


def get_lastmod(file_path: Path) -> str:
    """Return ISO 8601 last modified date from file mtime."""
    mtime = file_path.stat().st_mtime
    dt = datetime.fromtimestamp(mtime, tz=timezone.utc)
    return dt.strftime("%Y-%m-%d")


def lang_from_rel_path(rel_path: str) -> str:
    if rel_path.startswith("html/en/"):
        return "en"
    if rel_path.startswith("html/vn/"):
        return "vn"
    return "cs"


def canonical_rel_path(rel_path: str) -> str:
    """Return a canonical key for grouping translations.

    Root files keep their full path, while html/articles use a folder+basename
    key so that cs/en/vn versions are grouped together.
    """
    import os
    parts = rel_path.split("/")
    if parts[0] in ("html", "articles"):
        return parts[0] + "/" + os.path.basename(rel_path)
    return rel_path


def main() -> None:
    files = collect_html_files()

    # Group translations by canonical name
    by_canonical = {}
    for file_path in files:
        rel_path = file_path.relative_to(KB_DIR).as_posix()
        lang = lang_from_rel_path(rel_path)
        canonical = canonical_rel_path(rel_path)
        by_canonical.setdefault(canonical, {})[lang] = file_path

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">',
    ]

    for canonical, lang_files in sorted(by_canonical.items()):
        primary_file = lang_files.get("cs") or next(iter(lang_files.values()))
        primary_rel = primary_file.relative_to(KB_DIR).as_posix()
        loc = f"{SITE}{url_path_from_file(primary_rel)}"
        lastmod = get_lastmod(primary_file)

        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{lastmod}</lastmod>")
        lines.append("    <changefreq>weekly</changefreq>")

        for lang in ["cs", "en", "vn"]:
            if lang not in lang_files:
                continue
            lang_rel = lang_files[lang].relative_to(KB_DIR).as_posix()
            href = f"{SITE}{url_path_from_file(lang_rel)}"
            lines.append(
                f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{href}" />'
            )

        lines.append("  </url>")

    lines.append("</urlset>")

    SITEMAP_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Generated {SITEMAP_PATH} with {len(by_canonical)} URLs.")


if __name__ == "__main__":
    main()
