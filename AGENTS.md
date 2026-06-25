# AGENTS.md

Instructions for AI agents and coding assistants working in this repository.

## Site URL

The production site is deployed at:

```
https://knowledgebase.superhostem.cz
```

## URL structure

All HTML pages are served under the `/knowledge-base/html/` path prefix. Always use this base when constructing absolute URLs (e.g. in `og:url` meta tags, sitemaps, redirects, or any other references):

```
https://knowledgebase.superhostem.cz/knowledge-base/html/<filename>.html
```

### Language subfolders

| Language | Path prefix |
|----------|-------------|
| Czech (default) | `/knowledge-base/html/` |
| English | `/knowledge-base/html/en/` |
| Vietnamese | `/knowledge-base/html/vn/` |

### Examples

```
https://knowledgebase.superhostem.cz/knowledge-base/html/index.html
https://knowledgebase.superhostem.cz/knowledge-base/html/en/index.html
https://knowledgebase.superhostem.cz/knowledge-base/html/vn/index.html
https://knowledgebase.superhostem.cz/knowledge-base/html/jak-funguje-napojeni-pres-ical.html
```

## What NOT to do

- **Do not** use `/html/` as the path prefix — this will result in broken links.
- **Do not** use relative paths in `og:url` or other absolute URL fields.

## Build output

The deploy workflow (`/.github/workflows/deploy-pages.yml`) copies all HTML files into `_site/knowledge-base/html/`. The source files live in `knowledge base/html/` (with a space) in this repo.
