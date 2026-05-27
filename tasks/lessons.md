# Lessons — 100daysofnon

The same mistake never happens twice. Read at the start of every session.

## 2026-05-27 · Day-pages can become stale relative to diary content

- **What went wrong:** Day 3's `site/day/003/index.html` was rendering an entirely different topic (TKC ninja workshop / Phase II) than what was in `diary/day-003/answer.md` (the father arc, 10 messages, 16 artifacts). The site was hand-coded from a prior Day-3 question that was later sharpened to a different prompt. Day 2 had the same drift on a smaller scale (the page rendered Msgs 1–4 but the diary had Msgs 1–9). The hand-coded approach drifts silently — there's no compiler error when the source-of-truth (`diary/day-XXX/answer.md`) is ahead of the derived artifact (`site/day/XXX/index.html`).
- **Correct behaviour:** day pages must be generated from `diary/day-XXX/`, not hand-coded. The `build.py` generator does this — every day page is now `build.py N` → `site/day/0NN/index.html`. The mood is a small JSON override in `site/data/day-moods.json`; the body is read fresh from the diary every build. Run the generator after any diary edit, and the page reflects the latest source.
- **How to recognise:** if `site/day/XXX/index.html` was last edited days before `diary/day-XXX/answer.md` was last edited, the page is stale. `git log -1 --format=%ci -- site/day/XXX/index.html` vs `git log -1 --format=%ci -- diary/day-XXX/answer.md` will tell you. Also: if the page renders content that contradicts the diary (subject mismatch, message count mismatch, missing artifacts), assume the page is stale rather than assuming the diary is.

## 2026-05-27 · `shutil.copy2` poisons re-runs by preserving restricted perms

- **What went wrong:** `shutil.copy2(src, dst)` preserves source metadata including permission bits. The diary artifacts had `-r--------` perms; after the first copy the site copies were also read-only, so the second `build.py` run threw `PermissionError` trying to overwrite them.
- **Correct behaviour:** for build outputs you intend to re-write, use `shutil.copyfile` (data only, no metadata) and `dst.chmod(0o644)` to normalise. Idempotency of a generator depends on it.
- **How to recognise:** the second run of an idempotent build fails with `PermissionError: [Errno 13]` on the destination path of a file the FIRST run created. The destination's mode bits match the source's restrictive ones.

## 2026-05-24 · Cloudflare Pages shadow-claim on custom domain

- **What went wrong:** Set up GitHub Pages + DNS CNAME `100days.nonarkara.org → nonarkara.github.io`. Site appeared "deployed" — workflow green, gh-pages branch correct, GitHub Pages built. But the live URL served entirely different content (an old "100 Days of Solitude" Cloudflare Pages project) for every path.
- **Root cause:** A pre-existing Cloudflare Pages project (`100-days-of-solitude`) had registered `100days.nonarkara.org` as a custom domain. When two services claim the same domain in Cloudflare, **Cloudflare Pages wins over an external CNAME**, regardless of DNS settings. The DNS proxy showed Cloudflare IPs as expected; the catch was that Cloudflare was routing internally to its own Pages project, never to GitHub Pages.
- **Correct behaviour:** Before setting up any new custom domain in Cloudflare, run `npx wrangler pages project list 2>&1 | grep <domain>` to check if the domain is already claimed by another Pages project. If it is, decide whether to (a) reassign it, (b) delete the old project, or (c) pick a different subdomain.
- **How to recognise:** Symptoms — `cf-cache-status: DYNAMIC` returning unexpected content for all paths, gh-pages branch verifiably correct, GitHub Pages API reports "built", but live URL serves wholly different site. The "all paths return same content" tell rules out CDN propagation (which would 404 on new paths). Means: domain hijacked by another Cloudflare service.

## 2026-05-25 · PDF-to-corpus extraction must preserve structure

- **What went wrong:** Initial read of the nonharvard PDF used the Read tool's `pages` parameter which only reads 20 pages at a time. Tempting to read the first 20 and assume the rest follows the same pattern. Mostly works but loses post boundaries on long entries.
- **Correct behaviour:** For corpus extraction, use `pdftotext` (which is installed at `/opt/homebrew/bin/pdftotext`) to convert the entire PDF to plain text in one pass, then parse the text into structured posts using consistent delimiters (date headers, post titles).
- **How to recognise:** When a task says "extract all N items from a document," reach for `pdftotext` / `pandoc` / `unzip` first; reach for the Read tool only when you need visual structure or pagination cues.
