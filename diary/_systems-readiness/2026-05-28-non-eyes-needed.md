# Things that need Non's eyes overnight or first thing in the morning

Generated: 2026-05-27T16:36Z (23:36 Bangkok) by `local_3198d54e` readiness audit.

If the four anchor demos are all you care about, this note is enough — skip the full readiness report unless you want the supporting-portfolio table.

---

## 1. NSP — verify the migration actually shipped

**Status:** Migration commit landed at **15:27 BKK today** (`feat: migrate to Cloudflare Workers via OpenNext, GitHub-driven deploys`). The repo `Nonarkara/nsp-prototype` is private; CI deploy state cannot be confirmed from this sandbox. The live URL `https://nsp.nonarkara.org` responds to HTTP GET with an empty body — which is the expected behaviour of a Next.js SPA shell rendering client-side, **but is also the failure mode of a half-shipped OpenNext deploy**. I cannot tell the difference without rendering JS.

**What to check (60 seconds):**
1. Open `https://nsp.nonarkara.org` in Chrome (not curl) on your phone.
2. If the hero + Mentor panel + Portal Effect funnel render → **green, demo is live, ignore the rest of this section**.
3. If blank: open Terminal and run `launchctl list | grep com.nsp.server`.
4. If the launchd job is missing (no output): `launchctl bootstrap gui/$UID ~/Library/LaunchAgents/com.nsp.server.plist` — that restarts the local Next.js server. Verify with `curl -sIL --max-time 5 https://nsp.nonarkara.org` returning 200 + a non-empty body.
5. If launchd IS running but the page is still blank: the OpenNext migration probably broke the build. Fall back: `cd ~/Projects/consulting/nsp-prototype && pnpm dev` and demo from `localhost:3000`. Don't try to fix the production build before class.

**Why this is yellow, not red:** the migration commit committed cleanly and the in-flight code-task `local_c2efb933` is responsible for completing it. If the task is still running when you wake up, give it ten minutes and recheck. If the task crashed mid-migration, that's the most likely cause of the empty body.

---

## 2. Chonburi — confirm AlphaEarth panel is in the deployed build

**Status:** Last successful Cloudflare Pages deploy was **2026-05-22**, before the AlphaEarth panel landed. Two subsequent deploys (2026-05-24, 2026-05-25) both failed in CI. The site is serving the 2026-05-22 version, which **may not include the AlphaEarth change-detection layer** — that landed in the commit `feat: data: bake AlphaEarth change-chonburi-2023-2024` on the same day, so it might or might not be in the last good build.

**What to check (60 seconds):**
1. Open `https://chonburi.nonarkara.org` in Chrome on your phone.
2. If the LayerPalette includes "AlphaEarth" / "Change 2023→2024" and the layer renders satellite-tile diffs → **green, this is the unsupervised-learning demo, ignore the rest**.
3. If the panel is missing or the layer is empty: fall back to localhost. `cd ~/Projects/dashboards/chonburi && pnpm dev` — the working tree has all the AlphaEarth work uncommitted, so localhost will be the most complete version. Demo from there.

**Do not commit the working tree.** The in-flight task `local_f5ba5cff` has 19+ modified files and a separate branch `claude/heuristic-herschel-081441`. Let the task finish or let it merge first.

---

## 3. Live code-task fleet — visual confirmation in Cowork

**Status:** The audit sandbox cannot enumerate live sessions (`mcp__session_info__list_sessions` tool not available in this session). However, recent git activity in NSP, SLIC, Chonburi, UNL, TKC, Axiom, 100daysofnon, and nonarkara-org all show commits within the last 24 hours — strong indirect evidence the fleet is alive.

**What to check (10 seconds):**
1. Open Cowork on Mac.
2. Switch to the Code tab.
3. Confirm the visible session list includes: NSP rebuild, SLIC audit, AlphaEarth Chonburi, 100daysofnon design, UNL mobile, TKC manual, OpenClaw council, TimesFM, nonarkara.org Memory Palace, this readiness audit.
4. If any are missing or shown as "crashed" / "errored", click Resume.

This is the headline demo — opening the Code tab live in the lecture is *literally* showing the "ten assistants" mental model running in real time.

---

## 4. Nakhon Si Thammarat — pick your demo mode

**Status:** Not Non-hosted. Lives in Mayor Ganop's office (LINE bot + purple-dot map system, 4-year live track record).

**What to decide (one decision, before class):**
- **Option A — live LINE bot demo:** open the actual chat on your phone, show a real complaint flow + the purple-dot map rendering. Highest impact, but exposes live citizen data on a classroom projector. Decide whether your audience is appropriate for that.
- **Option B — cached demo:** use the screenshots and stats already captured in `100daysofnon/diary/day-072/answer.md` and the chonburi lecture summary. Lower impact but safer.

Either way, this anchor is **not technical-readiness dependent** — no overnight check needed.

---

## 5. One housekeeping item Non may want to fix later (not before class)

The repeated CI failures across kuching-ioc, phuket-dashboard, phuket-smart-bus, smart-city-thailand-index, smart-city-thailand-monitor, globalmonitor, chonburi-control-tower, and dao **all on 2026-05-25** suggest a common cause — most likely the `CLOUDFLARE_API_TOKEN` rotation flagged in `_reference/monitoring-urls.md` ("⚠ CI token expired (code 9109)"). The older successful deploys keep the sites serving, so this is a CI-health issue, not a live-site issue. Fix at leisure — not class-critical.

---

## Bottom line for tonight

Sleep. None of these items break the class. NSP and Chonburi each need one Chrome tab open in the morning and a possible 30-second fallback to localhost. The Nakhon Si Thammarat demo decision can be made in the taxi.
