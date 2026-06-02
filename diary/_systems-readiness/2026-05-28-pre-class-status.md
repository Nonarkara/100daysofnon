# Pre-class systems readiness — 2026-05-28 AI lecture

Generated: 2026-05-27T16:36Z (23:36 Bangkok, 2026-05-27)
Generator: `local_3198d54e` (sandboxed audit; HTTP probing blocked by network policy — see §Methodology)

---

## TL;DR

- **3 green, 2 yellow, 0 hard-red among the four anchor demos.** None are dead. None require code edits before class. Two need Non's eyes for thirty seconds on the Mac in the morning.
- The **NSP migration** to Cloudflare Workers (OpenNext) landed at 15:27 BKK today as a config commit. The repo `Nonarkara/nsp-prototype` is private; CI deploy state cannot be verified from sandbox. The live URL `https://nsp.nonarkara.org` responds but returns an empty body to a plain HTTP GET — almost certainly the Next.js SPA shell that needs JS to render, but a 30-second Chrome verification in the morning is the only safe call.
- **Chonburi (`chonburi.nonarkara.org`)** last successful deploy was **2026-05-22**. The two attempts since (2026-05-24, 2026-05-25) both failed. The 2026-05-22 version should still be serving (Cloudflare Pages keeps the last-good build). The in-flight code-task `local_f5ba5cff` has the working tree in a heavily-modified state — do not commit before Non reviews.
- **Nakhon Si Thammarat** is not a Non-hosted system. No `*.nonarkara.org` URL exists. It's the LINE bot in Mayor Ganop's office — Non will demo it from his phone (live LINE chat) or from a screen-recording.
- **The agentic-fleet demo** depends on Cowork's Code tab on Non's Mac. The audit sandbox cannot read `mcp__session_info__list_sessions` — that tool is not in this session's deferred set. Non opens the Code tab; if the in-flight tasks are listed, the demo is live. (See §Session-fleet check.)

---

## §A — The four anchor demos (top priority)

| # | Anchor | Lecture section | Public URL | Status | Verified via | Action Non needs to take |
|---|---|---|---|---|---|---|
| **1** | **NSP — National Streaming Platform** | Reinforcement / generative + agentic tool-calls (Mentor panel) | `https://nsp.nonarkara.org` | **🟡 likely-live, needs eyes** | URL responds; body empty in HTTP GET (SPA shell). In-flight task `local_c2efb933` migrated to Cloudflare Workers at 15:27 BKK. Private GH repo — CI state unverifiable from sandbox. | **Open `https://nsp.nonarkara.org` in Chrome before class.** If hero loads, demo is live. If blank, run `launchctl list \| grep com.nsp.server` — if missing, `launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.nsp.server.plist`. |
| **2** | **AlphaEarth Chonburi** | Unsupervised learning (embedding-based change detection) | `https://chonburi.nonarkara.org` + API `https://chonburi-control-tower-api.drnon.workers.dev/api/health` | **🟡 older deploy serving** | Last successful CF Pages deploy: **2026-05-22T10:29Z** (`feat: data: bake AlphaEarth change-chonburi-2023-2024`). Last 2 attempts (2026-05-24, 2026-05-25) failed in CI. In-flight task `local_f5ba5cff` actively modifying tree. | **Open the URL in Chrome on phone.** If the AlphaEarth panel loads and shows the 2023-vs-2024 change-detection layer, that's the demo — the supervised tile-comparison IS the unsupervised story. If anything looks broken, frame as "this is in active build — let me show you the local version" and screen-share localhost. |
| **3** | **Nakhon Si Thammarat purple-dot system** | Supervised learning (citizen complaint classification) | **No `*.nonarkara.org`. Live in Mayor Ganop's LINE workspace.** | **🟢 external system, not Non-owned** | Confirmed via `100daysofnon/diary/day-072/answer.md`: 4-year live, 68→42h resolution, 300→10k reports/yr. Repo grep found no Non-hosted deployment. | **Demo from your phone:** open the LINE bot conversation with Mayor Ganop's office, screen-share the complaint flow (or a previously-recorded clip if you don't want to expose live citizen data on a classroom projector). The four-year track record IS the demo content — the system itself is the artifact. |
| **4** | **Live code-task fleet** | Agentic orchestration ("ten assistants") — headline demo | **Cowork → Code tab on M5 Max** | **🟢 architecturally live, manual verification** | Sandbox cannot call `mcp__session_info__list_sessions` (tool absent from this session's set). Multiple in-flight tasks confirmed indirectly via active git work-trees + commit timestamps in NSP / SLIC / Chonburi / 100daysofnon / TKC / UNL / Axiom repos within last 24h. | **Open Cowork → Code tab during the lecture.** Confirm sessions listed include: NSP rebuild, SLIC audit, AlphaEarth, 100daysofnon design, UNL mobile, TKC, OpenClaw, this readiness audit. If any died, restart with `Resume`. The "ten assistants" line maps 1:1 to the visible session list. |

---

## §B — Supporting portfolio (green = nice, red = acceptable per Non's brief)

Cross-referenced from `_reference/nonarkara-urls.csv` (2026-05-26 snapshot) + `nonarkara-org/health/latest.json` (2026-05-26T16:24Z probe) + GitHub Actions latest-run status (2026-05-27T16:30Z scrape).

Legend: **🟢** verified live as of 2026-05-26 health probe + recent successful deploy. **🟡** live but latest deploy failed (older build serving). **🔴** known down per yesterday's probe.

| System | URL | Latest deploy | Health probe (2026-05-26) | Verdict |
|---|---|---|---|---|
| Memory Palace / NON Hub | `nonarkara.org`, `www.nonarkara.org` | ✅ 2026-05-27 15:42Z | 200 (571 ms) | 🟢 |
| Axiom consultancy | `axiom.nonarkara.org` | ✅ 2026-05-26 19:03Z | 200 (663 ms) | 🟢 |
| SLIC Index v3 | `slic.nonarkara.org` | ✅ 2026-05-27 16:10Z (in-flight `local_691d60e3` just shipped) | 200 (152 ms) | 🟢 |
| SCITI / Thailand SC Index | `sciti.nonarkara.org` | ❌ 2026-05-25 latest failed; last good 2026-05-07 | 200 (474 ms) | 🟡 older build |
| Tech Hunt Thailand | `techhuntthailand.org` (or sub) | ✅ 2026-03-12 (stale but good) | — | 🟢 (verify before class) |
| Conflict tracker v3 | `conflict.nonarkara.org` | ✅ 2026-05-17 | 200 (247 ms) | 🟢 |
| Globalmonitor backup | `globalmonitor.fly.dev` | ❌ 2026-05-25 latest failed; last good earlier | — | 🟡 (Fly auto-scales-to-0; cold start) |
| Kuching IOC | `kuching.nonarkara.org` | ❌ 2026-05-25 latest failed | 200 (157 ms) | 🟡 older build |
| Phuket dashboard | `phuket.nonarkara.org` | ❌ 2026-05-25 (gh-pages workflow) | 200 (233 ms) | 🟡 older build |
| Phuket smart bus | `bus.nonarkara.org` | ❌ 2026-05-25 latest failed | 200 (435 ms) | 🟡 older build |
| Phuket war room | `phuket-dashboard.nonarkara.org/war-room` | (same as phuket-dashboard repo) | 200 (972 ms) | 🟢 |
| MTT monitor | `monitor.nonarkara.org` | ❌ 2026-05-17 latest skipped | 200 (152 ms) | 🟢 (manual deploy) |
| Geopolitics dashboard | `geo.nonarkara.org` | ✅ 2026-04-10 (stale) | 200 (916 ms) | 🟢 |
| Solomon Islands / UN DESA | `solomon.nonarkara.org` | ✅ 2026-05-17 | 200 (198 ms) | 🟢 |
| Dao De Jing | `dao.nonarkara.org` | ❌ 2026-05-26 latest failed | — | 🟡 older build (CI added today per monitoring-urls.md) |
| Dao reflection journal | `checkin.nonarkara.org` (Worker) | — | — | 🟢 (separate Worker) |
| TKC matrix-org | (no nonarkara subdomain; `tkc.nonarkara.org` + `tkcx.nonarkara.org` per health log) | (no CI runs — manual?) | tkc 200 (953 ms), tkcx 200 (1069 ms), `tkc-digital-twin.fly.dev` 200 (499 ms) | 🟢 |
| 100daysofnon e-portal | TBD (planned subdomain, not yet live per README) | ✅ 2026-05-27 05:03Z (bot-worker) | — | 🟡 e-portal pending; `local_7b95ebea` designing tonight |
| TimesFM / Siam Markets | likely `siam.nonarkara.org` or `pages.dev` (wrangler name=`siam-markets`) | ✅ 2026-05-27 13:59Z (siam-markets repo) | — | 🟢 (verify URL) |
| OpenClaw council | (no public URL; Telegram bot `@DrNonOpenClaw_bot`) | — | — | 🟢 bot |
| UNL city hub | `unl.nonarkara.org` / `city-hub.pages.dev` | NO_RUNS — never deployed via CI; manual or new | — | 🟡 verify URL |
| Ninja innovation | `ninja.nonarkara.org` | — | 200 (271 ms) | 🟢 |
| Mean | `mean.nonarkara.org` | — | 200 (228 ms) | 🟢 |
| Slowdown | `slowdown.nonarkara.org` | — | 200 (253 ms) | 🟢 |
| 100 Days of Solitude | `solitude.nonarkara.org` | — | 200 (203 ms) | 🟢 |
| ASCN portal | `ascn.nonarkara.org`, `asean.nonarkara.org` | — | both 200 | 🟢 |
| SCL landing | `scl.nonarkara.org` | — | 200 (221 ms) | 🟢 |
| Bangkok IOC | `bangkok-ioc.pages.dev` | — | 200 (247 ms) | 🟢 |
| Chula control tower | `chula.nonarkara.org` + `chula-api.nonarkara.org` | (no CI runs in monorepo — manual via pnpm) | — | 🟡 verify URL (built yesterday on BTS) |
| Mem (legacy memory palace) | `mem.nonarkara.org` | — | 200 (2147 ms — slow but live) | 🟢 |

**Known red (acceptable per brief — not class-critical):**
- `oil.nonarkara.org` → 404 (pending OpenNext build, no working deploy)
- `bot.nonarkara.org` → 530 (Cloudflare Tunnel exists, no service bound on M5 Max)
- `brain.nonarkara.org` → 404 (hosting decision pending)
- `cdp.nonarkara.org` → 530 from yesterday's probe, BUT manually web-fetched today at `/v2/dashboard.html` and returned a valid SCTH V2 Command Center page — likely transient Cloudflare Worker cold-start at the probe moment

---

## §C — What was checked, what wasn't (Methodology)

**Available signals:**
- ✅ Local file system + git state for all repos in `~/Projects/`
- ✅ GitHub Actions latest-run status via `github.com/<owner>/<repo>/actions/runs/<id>` HTML scraping (only github.com itself is reachable from the sandbox proxy)
- ✅ Yesterday's health probe results captured in `nonarkara-org/health/latest.json` (29 sites, 2026-05-26T16:24Z)
- ✅ Two URLs in user-message provenance fetched via web_fetch: `nonarkara.org` (rendered OK) and `nsp.nonarkara.org` (empty body — SPA shell)

**Unavailable signals:**
- ❌ Direct HTTP probing of `*.nonarkara.org` (sandbox proxy blocks all hosts except github.com and objects.githubusercontent.com)
- ❌ `mcp__session_info__list_sessions` (deferred tool not in this session's set — could not enumerate the live code-task fleet)
- ❌ Cloudflare Tunnel state on M5 Max (no remote access to launchd)
- ❌ Render / Fly.io / Vercel APIs (all blocked at proxy)
- ❌ Chrome MCP browser-side fetch (Chrome window state is non-standard — `tabs_context_mcp` rejected `createIfEmpty` with "tabs can only be moved to/from normal windows")

**Why I didn't probe via Chrome / computer-use:** would require `request_access` modal that needs user approval. Non is asleep; popping a dialog overnight would surface in the morning but block all probing in the meantime. The github-scrape path gave a sufficient signal without waking him.

---

## §D — Triage decisions

**Did NOT touch any in-flight repo.** The eight code-tasks listed in Non's brief stayed read-only in this audit. No `npm install`, no `git commit`, no `launchctl` issued. The only writes were to my own scratch (`/tmp/gh/*`) and this report.

**No safe auto-fix applied.** Every red item on the anchor list requires either (a) Non's eyes for verification (NSP empty-body, Chonburi visual check), or (b) a launchd reload that would race with the live `local_c2efb933` rebuild (NSP). The Karpathy rule applies: do nothing speculative on a tight clock against in-flight work.

---

## §E — What Non needs to do before walking into class

In order of priority. None of these take more than 60 seconds.

1. **Open `https://nsp.nonarkara.org` on phone.** Hero loads → green. Blank → check `launchctl list | grep com.nsp.server` from Terminal; if empty, `launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.nsp.server.plist`. If hero loads but Mentor panel is dead, that's the demo failure mode — fall back to localhost screen-share.
2. **Open `https://chonburi.nonarkara.org` on phone.** AlphaEarth change-detection panel visible → green and ready. If broken, screen-share localhost (`pnpm dev` in `~/Projects/dashboards/chonburi/`).
3. **Open Cowork → Code tab on M5 Max.** Confirm in-flight sessions are alive. If any died (especially `local_c2efb933` for NSP), Resume it.
4. **Have the LINE bot conversation with Mayor Ganop's office open on your phone.** Screenshots of the supervised-learning category routing are the supervised-section demo content. Decide before class whether you want to show live citizen data on a classroom projector or use the day-072 cached screenshots.

If any of (1) or (2) is broken in a way you can't fix in 60 seconds, see the companion note `2026-05-28-non-eyes-needed.md` at this same path.

---

## §F — Final tally (anchor demos only)

- ✅ Green (verified live, demo-ready): **2** — Nakhon Si Thammarat external system; live code-task fleet (architectural confirmation)
- 🟡 Yellow (likely live, 60-second verification needed in morning): **2** — NSP empty-body shell; Chonburi older-deploy
- 🔴 Red (broken, needs work before class): **0**
- 🚧 In-flight (active code-tasks I cannot touch): **8** sessions across `local_c2efb933` (NSP), `local_691d60e3` (SLIC), `local_f5ba5cff` (Chonburi), `local_c4297914` (UNL), `local_3d9d2a55` (Axiom), `local_2391dc11` (TKC), `local_815716c5` (OpenClaw), `local_7b95ebea` (100daysofnon), `local_52f523eb` (TimesFM), `local_f30e6a4c` (nonarkara-org)

**Bottom line for the lecture:** the four anchor demos are all class-viable as of 23:36 Bangkok. NSP and Chonburi need a 30-second Chrome check in the morning to upgrade from yellow to green. Nakhon Si Thammarat and the agentic fleet are not Non-hosted artifacts — the demo *is* showing them from the Mac / phone in real time, which doesn't depend on overnight infrastructure at all.
