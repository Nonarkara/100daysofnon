# Input 65 — WanGP (deepbeepmeep/Wan2GP): open-source video/image/audio generation for the "GPU Poor"

**Source:** GitHub — `github.com/deepbeepmeep/Wan2GP`. **I actually fetched the repo README** for this input, so verification is direct-source rather than second-hand.

**Author:** DeepBeepMeep · **Latest release at fetch:** v11.77 (May 21, 2026) · **Repo status:** fork of `Wan-Video/Wan2.1` (Alibaba's official Wan video model), heavily extended. Active Discord, active X presence (@deepbeepmeep).

## What WanGP actually is — one paragraph

A **single Web UI + CLI + headless-batch platform** that wraps ~20+ open-source generative models — video, image, audio, TTS, voice-cloning — with **aggressive VRAM optimization** so consumer/older GPUs can run models that normally need datacenter hardware. Named tagline: *"The best Open Source Video Generative Models Accessible to the GPU Poor."*

## Models supported (verified from README)

**Video:** Wan 2.1 / 2.2, Hunyuan Video, LTX-2 / LTX-2.3 (heavily developed), Flux, Z-Image, LongCat, Kandinsky, Vista 4D (video reshooting from novel camera angles), Magi Human (talking head)

**Image:** Qwen Image, HiDreamO1 (edit + text preservation), Flux

**Audio / TTS / Voice cloning:** Qwen3 TTS, Chatterbox, HearMula, Omnivoice (100 languages), ScenemeAI, DramaBox, SeedVC (voice cloning with background/music/singing), Ace Step 1.5 Turbo XL (song generation)

**Post-processing:** FlashVSR (x2/x4 spatial upsampling; 6GB VRAM for x2, 10GB for x4 — impressive), Prompt Enhancer, Motion Designer, Pose/Depth/Flow extraction, Video Browser, CivitAI browser+downloader, model manager

**Bundled agent:** Deepy — a WanGP-native agent built on Qwen3VL Abliterated, runs offline at 8GB VRAM, can chain video-gen + image-gen + audio-gen + transcription + trimming into full workflows. Free — no OpenAI/Anthropic subscription required.

## VRAM and hardware coverage — this is the differentiator

- **6 GB VRAM** sufficient for many models
- **10 GB VRAM** for x4 spatial upsampling
- **16 GB VRAM** for Magi Human at 1080p with 101 frames
- Full NVIDIA range: **GTX 10XX → RTX 50XX**
- **AMD RDNA 2/3/3.5/4** supported (installation docs provided)
- **MPS / Apple Silicon** early support (May 2026 — not fast, not all models yet)

**Quantized-format support:** int8, fp8, gguf, NV FP4, Nunchaku — the range that makes low-VRAM inference actually work.

## Verification pass — three green, two amber

- ✅ **Repo real + active**: v11.77 shipped May 21, 2026; earlier releases through May 2026 show *weekly-cadence* development
- ✅ **Legitimate downstream of Wan-Video/Wan2.1** (Alibaba's official open-source video model — Apache-licensed upstream)
- ✅ **Multi-format install path** (BAT/SH scripts, Pinokio community scripts, manual conda, Docker for Debian) — matches serious project posture
- 🟡 **License not stated in README text** — needs direct check of the LICENSE file (upstream Wan is Apache 2.0, so likely inherits; verify before Coolify deployment)
- 🟡 **Single-maintainer signature** — the update log is written entirely in DeepBeepMeep's voice; the project is impressive but has real single-point-of-failure risk. Discord community exists but bus-factor is worth acknowledging.

## Why this matters for Horizon — the open-source counterpart to the MarketryPro paid-tools grid

Today's [[Input 60 Ultraboost Integration Map]] catalogued 20 paid-vs-free tool comparisons from the MarketryPro cards. The paid side included: **Higgsfield ($49/mo)** for video, **Midjourney ($60/mo)** for image, **Suno ($10/mo)** + **Udio (free)** for music, **Eleven Labs ($17/mo)** for voice. **WanGP is the open-source, self-hosted, no-subscription substrate for essentially all of those categories.**

For Horizon curriculum:

### M6 lesson: *"Self-hosted generative media in 2026 — when the free tier is actually better than the subscription"*

Direct teaching using WanGP as the anchor. Same shape as the Local-Inference lesson proposed in [[Input 63 turbo-fieldfare]] — teach both the capability + the tradeoffs. Concrete tradeoffs Horizon must name:

| Aspect | WanGP self-hosted | Cloud subscriptions |
|---|---|---|
| Cost after setup | ~$0 (electricity + your time) | $10-60/month per service |
| Privacy | Full — content never leaves your machine | Vendor-defined |
| Model choice | 20+ models, weekly-updated | Vendor-locked |
| Speed on 8GB VRAM | Slow (measured in minutes per generation) | Fast (seconds) |
| Speed on RTX 5090 / M5 Pro | Approaches cloud speed | Fast |
| Reliability | You debug when it breaks | Vendor uptime |
| Skills needed | Non-trivial install + config | Sign-up + credit card |

**Horizon's honest teaching:** for occasional personal/experimental use, cloud subscriptions are fine. **For production workflows with confidential content, self-hosted WanGP on decent hardware is the correct answer.** For the Thai SMB segment Horizon targets, this maps to: real estate/legal/consulting = self-hosted; social-media hobby = cloud.

### The Honesty Layer angle — deepfake and voice-clone ethics

WanGP includes: **SeedVC voice cloning** (works with singing and background music), **Magi Human talking heads** (1080p from a single reference), **LongCat 1.5 Avatar** (unlimited-length talking heads via sliding windows), **Vista 4D** (reshooting existing videos from novel angles). **These capabilities have legitimate creative uses AND direct deepfake-misuse potential.**

**Horizon must teach both the technical capability AND the ethical bounds.** Same discipline as [[Input 26 Skill Preservation]] and [[Input 58 Manabu]]. A Horizon lesson on WanGP that omits the deepfake ethics is a curriculum-incomplete lesson. Concrete Thai-context bounds:

- Voice cloning a real person without informed consent likely violates Thailand's PDPA (Personal Data Protection Act, 2019) — biometric voice data is PDPA-scoped
- Non-consensual intimate imagery generation is criminalized under Thai Computer Crime Act B.E. 2560 amendments
- The 2024 Thai Cabinet resolution on AI-generated political content creates additional bounds for election-adjacent use

**These bounds should be first-class Horizon curriculum content, not appended footnotes.**

## Direct implications for Non's live projects

### FloodDash — no direct fit right now

FloodDash is a real-time flood-alert system. Generative video is not the current bottleneck. **Possible future use:** brief AI-generated explainer videos of what different flood severity levels look like in Thai neighborhoods, for the sub-district-specific alert pages proposed in [[FloodDash WO-01]]. Low priority.

### Phuket SMART Bus — marginal fit

Possible: Thai-language voice announcements for airport queue passengers via Omnivoice / ScenemeAI. Would replace or supplement current LINE-based notifications. **Waits for the mobile-responsive rewrite (WO-01) to ship first.**

### SLIC v3 — a real fit for the *"video summary of the axis"* format

Each SLIC v3 axis could ship with a short (~30-60 second) AI-generated video explainer showing the axis in plain language, Bangkok examples, and one datapoint. WanGP + Omnivoice (Thai) + Wan 2.2 for the visuals. **Real proposal.** Low priority relative to the axis 10 build itself.

### Horizon curriculum content production — the strongest fit

Horizon needs lesson thumbnails, short intro videos, TTS-generated Thai voiceovers for accessibility, potentially AI-generated case-study illustrations. **WanGP self-hosted on a decent GPU (or on your M-series Mac via early MPS support) is the correct answer for Horizon's own content-production stack.** Recommendation: install on the strongest workstation you have; use for asset generation; do not host as a public service (WanGP is single-user by design).

### 100daysofnon Pinterest library — real fit

The Pinterest library concept named in earlier inputs could source concept images + short video clips from WanGP. Would allow content-production velocity that manual sourcing cannot match. **Real fit.**

## Practical placement in [[Input 60 Ultraboost Integration Map]]

**Tier B candidate** — install after Tier A settles. Same tier as n8n / Trigger.dev / Hoppscotch / GeoLibre / turbo-fieldfare. Install requires: decent NVIDIA GPU on a Linux/Windows machine (Mac support is early), ~50GB disk space for model checkpoints, one afternoon of setup work per the one-click installer.

**Recommendation:** if you have a workstation with a used RTX 3090 / 4090 or better, WanGP is worth the install. If your only options are the M-series Mac (which the MPS support is early on) or a laptop GPU, treat as Tier C — the workflows will be too slow to be useful, and cloud subscriptions win on ROI-per-hour.

## What NOT to do

- ⚠️ **Don't install on production Coolify VPS** — WanGP wants a GPU workstation, not a headless server. Local install only.
- ⚠️ **Don't teach WanGP capabilities without teaching the deepfake ethical bounds** — see the Honesty Layer angle above.
- ⚠️ **Don't rely on WanGP for production-critical workflows without a fallback** — single-maintainer signature means bus-factor risk. Cloud vendors' uptime is worse than they claim, but WanGP's uptime is *your* problem.
- ⚠️ **Don't cite the "6GB VRAM sufficient" claim as universal** — some models require more; check per-model requirements before committing to a hardware purchase.

## Also — I should offer the outstanding turbo-fieldfare verification pass

I did the WebFetch here on Wan2GP directly. **I could do the same pass on `github.com/drumih/turbo-fieldfare` right now to upgrade [[Input 63]]'s verification status from "confirmed exists" to "confirmed license + activity + maintainer + build health."** Say the word.

## Cross-references

- [[Input 60 Ultraboost Integration Map]] — the tier-map WanGP joins as Tier B candidate
- [[Input 63 turbo-fieldfare]] — sibling local-inference tool for LLM domain; WanGP is the media-generation analog
- [[Input 26 Skill Preservation]] / [[Input 58 Manabu]] — the Honesty Layer discipline this input inherits
- [[Input 61 LINE OA MCP]] — the Solo-Empire framing; WanGP is *the media stack* the Solo Empire uses when it cares about privacy or cost
- [[FloodDash WO-01]] / [[Phuket Bus WO-01]] — the live projects marginally-adjacent to this tool
- [[SLIC brief.md]] — the v3 project that has real use for WanGP for axis-explainer videos
- [[feedback_teach_dont_silently_fix]] — the discipline requiring the ethical-bounds section
- Thailand PDPA (Personal Data Protection Act, 2019); Thai Computer Crime Act B.E. 2560; 2024 Thai Cabinet resolution on AI-generated political content — the legal bounds any Horizon lesson using WanGP must name
- Upstream: `github.com/Wan-Video/Wan2.1` (Alibaba's official Wan 2.1 model, Apache 2.0)
