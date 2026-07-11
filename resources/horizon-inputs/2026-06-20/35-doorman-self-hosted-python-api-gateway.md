# Input 35 — Doorman: self-hosted Python API gateway for REST, SOAP, GraphQL, gRPC, and AI APIs

**Source:** Thai-language micro-post. Hashtags: `#Github #Chai_AI #Doorman`. Bilingual headline: *"Doorman คือ Self-hosted Python API gateway รองรับ REST, SOAP, GraphQL, gRPC และ AI APIs พร้อมความยืดหยุ่นในการปรับใช้งาน / A self-hosted Python API gateway supporting REST, SOAP, GraphQL, gRPC, and AI APIs with multi-protocol flexibility."*

## What it is (distilled)

A **self-hosted API gateway** written in Python, supporting **5 protocols in one stack**: REST + SOAP + GraphQL + gRPC + AI APIs. The pitch is multi-protocol unification under one gateway you control yourself, with the *AI APIs* line being the 2026-distinctive feature (most API gateways from the pre-LLM era treat AI calls as just another HTTP endpoint; Doorman positions LLM/agent traffic as a first-class protocol).

I haven't independently fetched the repo for this short post — the hashtag credits suggest the source is **Chai_AI** on GitHub. **Verification status:** unverified at filing time. The Horizon Research version of any paper that uses Doorman should fetch the repo, confirm license, confirm the protocol-support claims, and confirm the AI-APIs handling is meaningful (e.g., LLM-aware rate limiting / token-counting / streaming SSE pass-through) and not just labeling.

## Why this matters for Horizon — the gateway layer of the modern stack

Today's prior inputs covered: knowledge layer (OKF, Input 27), tool layer (WebMCP, Input 33), backend layer (Supabase, Input 20; Convex via BigSet, Input 29), agent orchestration layer (Mastra via BigSet, Input 29), context layer (codebase-memory-mcp, Input 19), discovery directory (openapps.pro, Input 30). **Doorman fills the gateway/edge layer.**

A complete 2026 self-hosted agentic stack now has named candidates at every layer:

| Layer | Today's candidate |
|---|---|
| Edge / Gateway | **Doorman** (this input) or Caddy / Traefik (from openapps.pro Input 30) |
| Backend / BaaS | Supabase (Input 20), Convex |
| Agent orchestration | Mastra (Input 29), the patterns in Non's skill (Input 18) |
| Tool exposure | WebMCP (Input 33) |
| Knowledge | OKF (Input 27) |
| Context for code agents | codebase-memory-mcp (Input 19) |
| Skills install | Codex Desktop Skills (Input 22), Caveman (Input 24) |
| Discovery | openapps.pro (Input 30) |

This makes the stack legible. **Horizon's M6 syllabus can now teach the *complete substrate* a learner needs to ship a production agentic system,** with named OSS candidates at every layer and the discipline to pick between them.

## Horizon placement — single Tips card + M6 layer-named mention

This input is small (a short Thai post, no full carousel). The right Horizon placement is correspondingly small:

1. **Tips & Techniques card** — *"Doorman: when you need one gateway for REST + GraphQL + gRPC + AI APIs."* 90-second card, link to the GitHub repo, brief on when to reach for it vs. simpler reverse proxies like Caddy.
2. **M6 layer-named mention** — in the lesson on the modern OSS stack (which gets its anchor from Input 30's openapps.pro directory + Input 29's BigSet reference architecture), Doorman is named as the gateway-layer candidate when multi-protocol unification matters.

Not big enough on its own to warrant a Horizon Research paper. Lives best as connective tissue in the broader stack lesson.

## Verification flags

- ⚠️ Repo URL not provided in the Thai post; *Chai_AI* on GitHub is the implied source. Confirm before publishing.
- ⚠️ The "AI APIs" first-class-protocol claim needs verification — is it just routing HTTP-to-LLM, or does it have LLM-specific features (token counting, streaming-SSE pass-through, rate-limit-by-tokens)? The Horizon write-up should answer this concretely.
- ⚠️ License claim implicit ("self-hosted, open-source") — verify what license before recommending.

Source: GitHub via Chai_AI per hashtags.
