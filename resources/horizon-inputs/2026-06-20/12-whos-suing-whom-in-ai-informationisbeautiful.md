# Input 12 — "Who's Suing Whom in AI?" by David McCandless / Information is Beautiful

**Source:** Hub-and-spoke network visualization titled *"Who's Suing Whom in AI?"*, subtitle *"notable copyright infringement cases from over 100 lawsuits"*, by **David McCandless** (Information is Beautiful). Dated **v 10 / June 2026** — current as of this filing. Cited sources: ChatGPTIsEatingTheWorld.com, Wired, news reports. Image filed as `12-whos-suing-whom-in-ai-informationisbeautiful.png`.

## What it shows

Central nodes (defendants — the AI companies): **Google, OpenAI, Meta, Anthropic, NVIDIA, Databricks, Stability**, and others. Surrounding spokes (plaintiffs — content owners): **Disney, Universal Music Group, Reddit, Conde Nast, Getty Images, BBC, Encyclopaedia Britannica, Elsevier, CNN, ZIFF Davis, Penguin / publishers, the Center for Investigative Reporting, the New York Times**, and dozens more. Plaintiff categories color-coded across the bottom: **authors / writers, media, musicians, platform, artists**. Node size encodes organization size.

This is the *current single-image map* of AI copyright litigation as of June 2026.

## Why this matters for Horizon — M5 anchor + recruiting hook

**Module fit:** Horizon **M5 (Frontier ethics & data sovereignty)**. Where Input 3 (Neurable BCI) anchors the *brain-data sovereignty* end of M5, this input anchors the *content-IP sovereignty* end. Together they bracket the module — *who owns what your AI uses, and who owns what your AI produces.*

**Pedagogical use:** the visualization is dense enough that learners can spend 10 minutes just reading it and reach M5's core questions on their own:

- *Why are these specific companies on the defendant side?* (training-data ingestion at scale)
- *Why these specific plaintiffs?* (their work is provably in the training set)
- *What is the legal theory in each cluster?* (fair use vs reproduction vs derivative works vs database rights)
- *Which side am I on as a creator? As a builder?* (probably both — that's the live tension M5 teaches)

**Recruiting use:** the visualization complements Input 11 (the 5-at-risk-Thai-jobs frame). Input 11 names the *anxiety* (your job might go). Input 12 names the *complexity* (and even the people building the AI are being sued by the people whose work made the AI possible). Together they tell prospective learners: *"the field is a contested frontier, not a settled tool. Learn to navigate the contest, not just use the tool."*

## A note on attribution

David McCandless is one of the most-cited data-visualization practitioners working today (TED talks, the *Knowledge is Beautiful* book, the long-running Information is Beautiful site/blog). His work is published under Creative Commons in most cases but Horizon should check the specific license on this graphic before embedding (his site usually permits embedding with attribution; remixing or republishing as Horizon's own may require permission). The clean path is: link to the original on informationisbeautiful.net + thumbnail preview with full attribution.

---

## Non's tab idea — the Pinterest-style artifact showcase for Horizon

Verbatim ask from Non:

> *"I guess I sent you lots of artifacts, like all these cartoons and infographics. Maybe we should have a Pinterest-style tab on Horizon 45 where we can showcase all of these and explain a little bit of what they are."*

This is a strong product feature, not just an aesthetic flourish. Specification follows.

### Feature: `/library` or `/visuals` — the Horizon Artifact Library

**Layout:** Pinterest-style masonry grid (variable-height cards, gap-aligned, infinite scroll or paginated). Mobile-first (Thai audience is overwhelmingly mobile). One artifact per card.

**Each card carries:**
- The image (thumbnail, lazy-loaded; click expands)
- A one-line title (Thai + English toggle)
- A 2–3 sentence explanation: *what it teaches, why it matters, which Horizon module it belongs to*
- Direct link into the module that uses it
- Source attribution + link to original
- Optional learner-facing prompt: *"once you've taken M5, come back and tell us — which AI company are you most aligned with as a builder, and which plaintiff are you most aligned with as a creator?"*

**Filters across the top:** *By Module (M1 / M2 / M3 / M4 / M5 / M6)* — *By Category (cartoon / infographic / chart / diagram / photo)* — *By Source (Thai-language / English-language / global)* — *By Mood (anxiety / inspiration / diagnostic / fun)*.

**Why this is a product win, not just a tab:**

1. **It's the lowest-friction entrance into the curriculum.** Most prospective learners won't read a curriculum doc. They will scroll a beautiful visual grid. Every card is a recruiting tool that links inward.
2. **It's intrinsically shareable.** Each card has its own URL. Sharing one card on LINE / Facebook / TikTok is sharing a piece of Horizon. Free distribution.
3. **It's a content-marketing engine on autopilot.** Every new infographic Non sends (he is clearly going to keep sending them) becomes a new card. The Pinterest tab grows over time, and the surface area for SEO + social grows with it.
4. **It teaches by example.** Horizon learners are *consuming* infographics today. The curriculum will teach them to *make* infographics tomorrow. A "made by Horizon students" sub-tab on the same surface — student-created visuals once the platform is mature — closes the loop.
5. **It's Non-distinctive.** No competitor in the Thai AI-education space (AIS, Samsung SIC, FutureSkill, the course-seller community) has this. The Pinterest tab becomes the front-page feature Horizon is known for.

### Implementation seed

The 12 inputs already filed in this folder become **the seed dataset for the Pinterest tab**. Each input file is structured enough (source / framing / why-it-matters / module-mapping) to be machine-converted into a card record. A small script could read this folder and emit a JSON manifest the front-end consumes.

Sample card record (JSON):

```json
{
  "id": "12-whos-suing-whom-in-ai",
  "title_th": "ใครฟ้องใครในวงการ AI?",
  "title_en": "Who's Suing Whom in AI?",
  "image": "/library/12-whos-suing-whom-in-ai.png",
  "explanation_th": "...",
  "explanation_en": "Network map of 100+ AI copyright lawsuits as of June 2026. Defendants like Google, OpenAI, Meta, Anthropic in the middle; plaintiffs like Disney, Universal Music, Reddit, Conde Nast around the edge.",
  "module": "M5",
  "category": "infographic",
  "source": "David McCandless / Information is Beautiful",
  "source_url": "https://informationisbeautiful.net/...",
  "mood": "diagnostic"
}
```

The Horizon code-task should add this Pinterest tab spec to its integration work alongside the curriculum modules.