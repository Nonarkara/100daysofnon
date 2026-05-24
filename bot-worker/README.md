# 100 Days of Non — Bot Worker

A Cloudflare Worker that wires the museum's chat UI to the Claude API.

## What it does

- Receives `POST /api/ask { question }` from the chat frontend
- Retrieves the 3 most-relevant blog posts from `corpus-index.json` (keyword overlap)
- Builds a system prompt from `voice-anchor.json` + the 49 demo Q&As + the retrieved excerpts
- Calls Claude (default: `claude-sonnet-4-5`) and returns `{ kind, answer, cite, retrieved[] }`
- The frontend renders the answer in Dr Non's voice with the four-kind tag

## Wire it up in 3 minutes

```bash
cd bot-worker/
npx wrangler login                                  # if not already authed
npx wrangler secret put ANTHROPIC_API_KEY           # paste sk-ant-...
npx wrangler deploy
```

Wrangler will return a URL like `https://100days-bot.<your-handle>.workers.dev`. Copy that.

Then in `site/bot/index.html`, find the JS `ask()` function and replace the local best-match logic with a fetch:

```js
async function ask(question) {
  if (initial) { stream.innerHTML = ''; initial = false; }
  appendUser(question);
  appendThinking();
  const r = await fetch('https://100days-bot.<your-handle>.workers.dev/api/ask', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ question }),
  });
  const data = await r.json();
  removeThinking();
  if (data.error) { appendBot('Bot error: ' + data.error, '', 'NOT_KNOWN'); return; }
  appendBot(data.answer, data.cite, data.kind);
  stream.scrollTop = stream.scrollHeight;
}
```

Then commit and push. The bot is live.

## Optional: own subdomain

Add a DNS CNAME `api.100days → 100days-bot.<your-handle>.workers.dev` in Cloudflare and uncomment the `[[routes]]` block in `wrangler.toml`. Then the worker answers at `https://api.100days.nonarkara.org/api/ask`.

## Cost notes

- Claude Sonnet 4.5 input ~$3/MTok, output ~$15/MTok.
- Each bot call sends ~3,500 tokens of system prompt (voice + 12 demos + 3 retrieved excerpts) + the user question, and receives ~200–500 tokens.
- Order of magnitude: $0.015 per chat exchange.
- Cloudflare Workers Free tier: 100,000 requests/day. The museum will not hit that.

## What's NOT in this worker (by design)

- No conversation memory. Each `ask` is stateless. (Add a `messages[]` parameter if you want threading.)
- No rate limiting beyond Cloudflare's defaults. If the museum gets popular, add a KV-based throttle.
- No moderation step. Add an Anthropic Claude classifier or an OpenAI moderation pass if needed.
- No analytics. The Worker logs nothing about questions. Add a KV write if you want a research record.

## Quality control

The system prompt forces the model to reply as JSON with one of four `kind` values:

- `DIRECT` — From the record. Citation required.
- `DEDUCTION` — Deduced from the record. Hedged. Citation suggested.
- `STRUCTURAL` — The signature. Refuses the literal question, answers the shape.
- `NOT_KNOWN` — Out of scope. Suggests a related question.

If the model deviates from the voice (uses forbidden phrases, gives motivational fluff, claims facts not in the record), iterate on `site/data/voice-anchor.json` — that file is the single source of truth for the bot's persona.

## Data dependencies

The worker fetches three JSON files from the live site at request time (with `cf: { cacheTtl: 3600 }` for 1-hour edge cache):

- `/data/voice-anchor.json`
- `/data/bot-demos.json`
- `/data/corpus-index.json`

If you redesign those files, the worker picks up the change after the cache expires (or after a manual purge).
