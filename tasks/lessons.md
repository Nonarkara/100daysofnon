# Lessons — 100daysofnon

The same mistake never happens twice. Read at the start of every session.

## 2026-05-24 · Cloudflare Pages shadow-claim on custom domain

- **What went wrong:** Set up GitHub Pages + DNS CNAME `100days.nonarkara.org → nonarkara.github.io`. Site appeared "deployed" — workflow green, gh-pages branch correct, GitHub Pages built. But the live URL served entirely different content (an old "100 Days of Solitude" Cloudflare Pages project) for every path.
- **Root cause:** A pre-existing Cloudflare Pages project (`100-days-of-solitude`) had registered `100days.nonarkara.org` as a custom domain. When two services claim the same domain in Cloudflare, **Cloudflare Pages wins over an external CNAME**, regardless of DNS settings. The DNS proxy showed Cloudflare IPs as expected; the catch was that Cloudflare was routing internally to its own Pages project, never to GitHub Pages.
- **Correct behaviour:** Before setting up any new custom domain in Cloudflare, run `npx wrangler pages project list 2>&1 | grep <domain>` to check if the domain is already claimed by another Pages project. If it is, decide whether to (a) reassign it, (b) delete the old project, or (c) pick a different subdomain.
- **How to recognise:** Symptoms — `cf-cache-status: DYNAMIC` returning unexpected content for all paths, gh-pages branch verifiably correct, GitHub Pages API reports "built", but live URL serves wholly different site. The "all paths return same content" tell rules out CDN propagation (which would 404 on new paths). Means: domain hijacked by another Cloudflare service.

## 2026-05-25 · PDF-to-corpus extraction must preserve structure

- **What went wrong:** Initial read of the nonharvard PDF used the Read tool's `pages` parameter which only reads 20 pages at a time. Tempting to read the first 20 and assume the rest follows the same pattern. Mostly works but loses post boundaries on long entries.
- **Correct behaviour:** For corpus extraction, use `pdftotext` (which is installed at `/opt/homebrew/bin/pdftotext`) to convert the entire PDF to plain text in one pass, then parse the text into structured posts using consistent delimiters (date headers, post titles).
- **How to recognise:** When a task says "extract all N items from a document," reach for `pdftotext` / `pandoc` / `unzip` first; reach for the Read tool only when you need visual structure or pagination cues.
