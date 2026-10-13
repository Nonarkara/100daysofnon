# 100 Days of Non — Bot Worker

A Cloudflare Worker that wires the museum's chat UI to the Claude API.

## What it does

- Receives `POST /api/ask { question }` from the chat frontend
- Retrieves the 3 most-relevant blog posts from `corpus-index.json` (keyword overlap)
- Builds a system prompt from `voice-anchor.json` + the 49 demo Q&As + the retrieved excerpts
- Calls Claude (default: `claude-sonnet-4-5`) and returns `{ kind, answer, cite, retrieved[] }`
- Refuses that call when the page is off-site, the connection is over its limit, or the museum has hit its daily cap
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

Add a DNS CNAME `api.100 → 100days-bot.<your-handle>.workers.dev` in Cloudflare and uncomment the `[[routes]]` block in `wrangler.toml`. Then the worker answers at `https://api.100.nonarkara.org/api/ask`.

## Cost notes

- Claude Sonnet 4.5 input ~$3/MTok, output ~$15/MTok.
- Each bot call sends ~3,500 tokens of system prompt (voice + 12 demos + 3 retrieved excerpts) + the user question, and receives ~200–500 tokens.
- Order of magnitude: $0.015 per chat exchange.
- Cloudflare Workers Free tier: 100,000 requests/day. The museum will not hit that.
- Cloudflare does not enforce a hard spend cap on the model this route calls. The guards below are that cap.

## Cost and abuse guards

`POST /api/ask` checks three things before it calls the model. A normal visit is unchanged: same JSON, same CORS headers, and a person asking a handful of questions never sees a 429.

1. **Site check.** `Origin`, or `Referer` when Origin is missing, must be the museum (`https://100.nonarkara.org` by default). A client can set the header, so this only cuts casual use from other pages. `GET /api/health` stays open.
2. **Per connection.** Token bucket of **10 questions a minute** and **100 a day**, keyed by `CF-Connecting-IP` (not `X-Forwarded-For`). The day resets at midnight in Asia/Bangkok.
3. **Whole museum.** **200 model calls a day.** Past that the worker returns HTTP 429 and does not call the model. At the estimate above, a day that hits the cap is about $3.

Tune them in `wrangler.toml` under `[vars]`: `RATE_LIMIT_PER_MINUTE`, `RATE_LIMIT_PER_DAY`, `GLOBAL_DAILY_CAP`, `ALLOWED_ORIGINS` (comma-separated). Set `GLOBAL_DAILY_CAP` to `0` to stop model calls without deleting the key.

Counts live in one SQLite Durable Object, `AskLimiter`. The first `npx wrangler deploy` creates it. If that binding is missing or the object cannot be reached, `/api/ask` returns 503 and does not call the model.

The site does not use Cloudflare Turnstile, so this worker does not add it.

To try the route from a shell, send the museum origin:

```bash
curl -s https://100.nonarkara.org/api/ask \
  -H 'origin: https://100.nonarkara.org' \
  -H 'content-type: application/json' \
  -d '{"question":"Where is Bangkok?"}'
```

Run the tests from this directory:

```bash
node --test
```

## What's NOT in this worker (by design)

- No conversation memory. Each `ask` is stateless. (Add a `messages[]` parameter if you want threading.)
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
