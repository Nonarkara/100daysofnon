# Input 46 — SynapTechAI: 7 Open-Source AI Tools (650k+ combined stars)

**Source:** Thai-language post by **SynapTechAI** (same source as Input 19's codebase-memory-mcp post earlier today). Hashtags: `#SynapTechAI #OpenSource #AIAgent #DevTools #LLM`.

**The 7 tools listed:**

| # | Tool | Claimed stars | Pitch |
|---|---|---|---|
| 1 | **Ollama** | 174k | *"Docker of AI Inference"* — local runtime + new Cloud tier ($20/mo Pro), scale without changing stack |
| 2 | **Open WebUI** | 142k | Self-hosted ChatGPT — RAG, function calling, multi-user, voice, image gen. *Saves $15k/yr for a 50-person team replacing ChatGPT Team* |
| 3 | **Browser Use** | ~99.5k | *"Rising star"* — AI browser automation for sites with no API. Growing faster than LangChain |
| 4 | **vLLM** | 83.3k | *"NGINX of LLM Serving"* — PagedAttention → 10-24x throughput. Ollama for dev, vLLM for production |
| 5 | **Unsloth** | 66.8k | Fine-tuning on consumer GPUs. 2x training speed, 80% less VRAM. Fine-tune 7B on RTX 4090 (24GB) |
| 6 | **CrewAI** | 53.9k | Multi-agent without a PhD. Agents have role, goal, backstory, toolset |
| 7 | **Continue** | 34.1k | Open-source Copilot. VS Code / JetBrains. Zero data leaves your network |

## The post's argument

> *"If 2023's question was 'is OSS AI good enough?', 2026's question is 'why are we still using closed APIs?'"*
>
> *"The gap between open weights and closed APIs has narrowed from embarrassing → barely-there."*

## Why this matters for Horizon

This is the **third specialized OSS list today** (openapps.pro Input 30 = general, RAGHub Input 38 = RAG, this = top-7 OSS-AI). **Convergence:** 6 of the 7 tools are already in today's brief through other inputs (Ollama in Inputs 30, 33; Open WebUI in 30; vLLM adjacent; CrewAI in 18, 29, 42; Continue in 30, 42). The 7th — **Browser Use** — is the genuinely new addition.

**Browser Use** is the *browser-automation* counterpart to **WebMCP** (Input 33). WebMCP exposes site-side tools to agents; Browser Use lets agents *drive* sites that haven't exposed WebMCP tools yet. **Together they describe the complete agent-browser interaction substrate for 2026** — sites with WebMCP cooperation, and sites without it.

## EGO-VOID note on the star counts

Unlike Input 39's SYNTAIX carousel (where Markitdown was inflated 19×), these star counts are **more plausibly accurate** because:
- Ollama at 174k is consistent with widely-reported numbers
- vLLM at 83.3k is consistent with widely-reported numbers
- The order-of-magnitude differences between tools track real-world adoption signals

Still: any Horizon publication using these numbers should verify against GitHub at publication time. SynapTechAI's curation register is *more credible* than the SYNTAIX carousel's based on the prior input's verifiability — but not infallible.

## Two Horizon placements

**M6 lesson addition** — *"The complete 2026 OSS AI dev-stack at a glance."* Pair with Input 42's 12-repo list as the more developer-focused complement (Input 42 is broader; Input 46 is OSS-AI-specific). Add **Browser Use** explicitly as the browser-automation layer alongside Persona/WebMCP (Input 33).

**Pinterest card** — *"650k+ combined stars: the 7 OSS AI tools that explain why 2026 looks different from 2024."*

Source: SynapTechAI Thai-language post.
