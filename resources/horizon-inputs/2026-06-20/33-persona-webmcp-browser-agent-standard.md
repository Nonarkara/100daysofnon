# Input 33 — Persona + WebMCP: browser-side standard for agent-tool exposure

**Source:** Thai-language post explaining the Persona library + the WebMCP standard. Hashtags: `#WebMCP #vibecodingthailand`. URLs cited: **persona-chat.dev** (the library), **Runtype** (the company behind it).

## What it is — verified during research

**WebMCP** is a **standard** (not just one library) for exposing webpage functions to AI agents as callable tools. Browser-native API: **`document.modelContext`** (with `navigator.modelContext` deprecated in Chrome 150). Documented in:
- [W3C / Web Machine Learning incubator spec](https://webmachinelearning.github.io/webmcp/)
- [Chrome developer docs](https://developer.chrome.com/docs/ai/webmcp/imperative-api)
- Reference site: [webmcp.dev](https://webmcp.dev/)
- Directory: [webmcp.com](https://webmcp.com/) — sites with tools for AI agents

**Persona** ([persona-chat.dev](https://persona-chat.dev/)) is an open-source themeable chat widget by **Runtype** that implements the WebMCP standard. **42 tools** available out of the box per the WebMCP directory listing.

This is a real W3C-track standard, not vendor handwaving. Browser-side adoption is happening in Chrome now.

## The architecture in plain terms

Webpage exposes its existing functions to a shared registration point on the page (`document.modelContext`). An agent in a chat widget on the page can then **discover and invoke those functions** as tools — same MCP pattern Anthropic uses for server-side tools, now for browser-side ones. Example tool exposure:

```js
document.modelContext.registerTool({
  name: "search_products",
  description: "Search the product catalog for items matching a query",
  inputSchema: { ... },
  handler: async (input) => { /* existing site function */ }
});
```

When a user types *"find me running shoes size 42"* in the chat, the agent:
1. Discovers `search_products` is registered
2. Invokes it with the parsed input
3. **Pauses to ask the user for approval** (human-in-the-loop popup is non-optional in Persona's implementation)
4. On approval, executes; returns results in the chat

## Why this is structurally significant for Horizon

**Three architectural points the post makes that matter:**

1. **No backend rewrites required.** Existing site functions get *wrapped* as tools. The chat is just another channel for invoking what the page already does. No new endpoints, no API redesign.
2. **Human-in-the-loop is non-optional.** Every tool invocation pauses for a user approval popup with a plain-language summary. Direct echo of the Safety-First Sequencing discipline in Non's own multi-agent-orchestration skill (Input 18) — irreversible actions gate at the human layer.
3. **Backend-agnostic.** Persona ships adapters for Vercel AI SDK, OpenAI Agents SDK, LangGraph.js. The widget is the *front* layer; you keep whatever LLM stack you already use.

**Plus two practical reliability points:**

- **Shadow DOM + prefixed CSS** prevents widget styles from leaking into the host page (the classic *"installed a chat widget, my CSS broke"* failure mode).
- **`customFetch` + `parseSSEEvent`** hooks let you adapt non-standard SSE backends without modifying the backend itself.

## Why this matters for Horizon — three structural impacts

### 1. It's the *consumer-side* counterpart to OKF (Input 27)

OKF standardizes how knowledge is stored (vendor-neutral Markdown directory). WebMCP standardizes how *agent-callable tools* are exposed (vendor-neutral `document.modelContext` registration). **Together they describe the 2026 vendor-neutral substrate for agentic AI:** knowledge layer (OKF) + tool layer (WebMCP). Horizon's curriculum should teach both as complementary halves of the same standardization wave.

Same strategic note as OKF: **Horizon's own platform should ship WebMCP-native.** Pinterest library card actions, use-case grid navigation, Personal Path Generator commands — all exposed as WebMCP tools so any agent (the user's own ChatGPT, Claude, Gemini browser extension) can invoke them. **The platform talks to the learner's preferred agent, not just its own.**

### 2. It changes what M4 (real working systems) teaches

M4's current syllabus assumes you build the *interface* to your system (Supabase backend per Input 20 + frontend per Input 28's prototype-first or plan-first patterns). WebMCP adds a *third* surface: **the agent-callable interface.** A complete M4 lesson now teaches three faces of a real system:
- Human-readable web pages (the traditional UI)
- Machine-readable APIs (the developer interface)
- **Agent-callable tools (the WebMCP interface)** ← new

Adding the third face means the same Supabase-backed system Non builds for the Mayor's dashboard can be *operated by the Mayor's own AI agent* without building a separate API surface. Direct value to Horizon's depa/SEIC audience.

### 3. It's a Tips & Techniques walkthrough waiting to happen

Per Input 22's Tips & Techniques surface spec: a 5-minute walkthrough of *"add a Persona chat widget to your existing website and expose 3 tools."* Worked example for any Thai-language developer reading.

## Cross-references to today's other inputs

- **Pairs with [[Input 18 — Non's multi-agent-orchestration skill]]** — WebMCP's human-in-the-loop approval IS the same Safety-First Sequencing discipline at the browser-tool layer. Non's skill spec covers the AGENT_NOTES.md layer for inter-agent coordination; WebMCP covers the per-tool-call user-approval layer.
- **Pairs with [[Input 20 — Supabase]]** — Supabase functions become WebMCP tools trivially. Each Supabase RPC function or Edge Function gets wrapped in a `document.modelContext.registerTool` call. **The agentic surface for a Supabase app is essentially free with WebMCP.**
- **Pairs with [[Input 27 — OKF]]** — knowledge layer + tool layer, same vendor-neutral standardization wave.
- **Pairs with [[Input 29 — BigSet]]** — BigSet's generated datasets could expose their refresh/query operations as WebMCP tools, letting agents *interrogate* the live dataset on a page rather than re-fetching the whole table.
- **Pairs with [[Input 32 — Anthropic Fable prompting guide]]** — the "set the boundaries" pattern (*"if I'm describing a problem, give your assessment. Don't fix until I ask."*) is exactly the prompting-side counterpart to WebMCP's human-in-the-loop approval at the tool-call side. Boundaries-in-prompt + approval-on-tool-call = the same safety stance at two layers.

## Three Horizon placements

### 1. M4 expansion — *"The three faces of a real system"*

Add to M4 (real working systems) as a lesson: human-readable UI + machine-readable API + **agent-callable WebMCP tools**. Worked example uses the Persona library on a Supabase-backed project to add agent operability to a system the learner has already built.

### 2. Tips & Techniques card — *"Add Persona to your website in 5 minutes and expose 3 tools"*

Standard Tips & Techniques walkthrough (per Input 22 spec). Sub-5-minute, immediately repeatable.

### 3. Horizon Research paper #11

***"WebMCP and the Vendor-Neutral Substrate for Browser-Side Agents: Why 2026 Is the Year Your Website Talks to Anyone's AI."*** Cross-references to OKF (Input 27) as the knowledge-layer counterpart. Particularly relevant for Thai government / SEIC / depa stakeholders deciding which agentic-platform standards to commit to in next-cycle procurements.

## Verification status (EGO-VOID applied)

- ✅ WebMCP is a real W3C-track standard, documented in the Web Machine Learning incubator + Chrome developer docs
- ✅ `document.modelContext` is the correct current API name; `navigator.modelContext` deprecated in Chrome 150
- ✅ persona-chat.dev exists and is listed in webmcp.com's directory with 42 tools
- ✅ Runtype as the platform company is verified — *"AI product platform for building and deploying AI experiences — agents, flows, and chatbots — across web chat, Slack, email, and API"*
- ⚠️ MIT license claim from the Thai post — likely accurate for the Persona widget specifically but worth confirming in the actual repo before Horizon publishes a recommendation
- ⚠️ The Thai post mentions adapters for *"Vercel AI SDK · OpenAI Agents SDK · LangGraph.js"* — verified plausible from the search results context but not directly confirmed for each adapter

## Add to the brief

This input contributes (a) M4 *"three faces of a real system"* lesson, (b) Tips & Techniques walkthrough, (c) Horizon Research paper #11 seed, (d) significant cross-references to Inputs 18, 20, 27, 29, 32 — WebMCP is genuinely a connective tissue across multiple Horizon themes.

Sources verified:
- [persona-chat.dev](https://persona-chat.dev/)
- [webmcp.dev](https://webmcp.dev/)
- [W3C / WebML incubator WebMCP spec](https://webmachinelearning.github.io/webmcp/)
- [Chrome developer docs — WebMCP](https://developer.chrome.com/docs/ai/webmcp)
- [WebMCP directory](https://webmcp.com/)
