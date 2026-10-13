// 100 Days of Non — Bot Worker
//
// A minimal Cloudflare Worker that wires the museum's chat UI to the
// Claude API. The system prompt is assembled from site/data/voice-anchor.json
// and the demo set from site/data/bot-demos.json. The corpus index is used
// for lightweight retrieval (top-N by keyword match) before generation.
//
// Endpoints:
//   POST /api/ask     {question: string}  →  {answer, kind, cite, retrieved[]}
//   GET  /api/health  →  {ok: true}
//
// Secrets (set with `npx wrangler secret put`):
//   ANTHROPIC_API_KEY   — Claude API key (sk-ant-...)
//
// Optional vars (in wrangler.toml [vars]):
//   ANTHROPIC_MODEL         — defaults to "claude-sonnet-4-5"
//   ALLOWED_ORIGINS         — pages allowed to call the model
//   RATE_LIMIT_PER_MINUTE   — per-IP token bucket (default 10)
//   RATE_LIMIT_PER_DAY      — per-IP daily questions (default 100)
//   GLOBAL_DAILY_CAP        — model calls for the whole museum (default 200)
//
// CORS stays `*` so the museum page can read answers from a workers.dev host.
// ALLOWED_ORIGINS is a separate check on Origin / Referer before any model call.

import { AskLimiter } from './limiter.js';
import {
  MESSAGES,
  clientIp,
  isAllowedSiteRequest,
  readLimits,
} from './limits.js';

const VOICE_ANCHOR_URL = 'https://100.nonarkara.org/data/voice-anchor.json';
const BOT_DEMOS_URL    = 'https://100.nonarkara.org/data/bot-demos.json';
const CORPUS_INDEX_URL = 'https://100.nonarkara.org/data/corpus-index.json';

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
};

export { AskLimiter };

export default {
  async fetch(request, env) {
    return handleRequest(request, env);
  },
};

export async function handleRequest(request, env = {}, deps = {}) {
  const url = new URL(request.url);

  if (request.method === 'OPTIONS') {
    return new Response(null, { headers: CORS_HEADERS });
  }

  if (url.pathname === '/api/health') {
    return json({ ok: true, ts: new Date().toISOString() });
  }

  if (url.pathname === '/api/ask' && request.method === 'POST') {
    try {
      return await handleAsk(request, env, deps);
    } catch (e) {
      return json({ error: String(e).slice(0, 200) }, 500);
    }
  }

  return json({ error: 'Not found' }, 404);
}

async function handleAsk(request, env, deps) {
  if (!isAllowedSiteRequest(request, env)) {
    return json({ error: MESSAGES.origin, code: 'origin' }, 403, {
      'Cache-Control': 'no-store',
    });
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: 'Question must be 1–500 chars.' }, 400);
  }
  const q = (body && body.question || '').toString().trim();
  if (!q || q.length > 500) {
    return json({ error: 'Question must be 1–500 chars.' }, 400);
  }

  const now = typeof deps.now === 'function' ? deps.now() : Date.now();
  const decision = await reserveAsk(env, request, {
    chargeGlobal: Boolean(env.ANTHROPIC_API_KEY),
    now,
  }, deps);
  if (!decision.ok) return limitResponse(decision);

  const result = await ask(q, env, deps.fetch);
  return json(result);
}

async function reserveAsk(env, request, opts, deps) {
  if (deps.reserve) return deps.reserve(env, request, opts);
  return reserveWithDurableObject(env, request, opts);
}

async function reserveWithDurableObject(env, request, opts) {
  const ns = env && env.ASK_LIMITER;
  if (!ns || typeof ns.idFromName !== 'function' || typeof ns.get !== 'function') {
    return { ok: false, reason: 'limiter_unavailable', retryAfter: 30 };
  }
  try {
    const stub = ns.get(ns.idFromName('global'));
    const res = await stub.fetch('https://limiter.internal/consume', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        ip: clientIp(request),
        now: opts.now,
        limits: readLimits(env),
        chargeGlobal: Boolean(opts.chargeGlobal),
      }),
    });
    if (!res.ok) return { ok: false, reason: 'limiter_unavailable', retryAfter: 30 };
    const decision = await res.json();
    if (!decision || typeof decision.ok !== 'boolean') {
      return { ok: false, reason: 'limiter_unavailable', retryAfter: 30 };
    }
    return {
      ok: decision.ok,
      reason: decision.reason || null,
      retryAfter: decision.retryAfter || 0,
    };
  } catch {
    return { ok: false, reason: 'limiter_unavailable', retryAfter: 30 };
  }
}

function limitResponse(decision) {
  const reason = decision.reason || 'limiter_unavailable';
  const status = reason === 'limiter_unavailable' ? 503 : 429;
  const code = reason === 'global_day'
    ? 'daily_cap'
    : reason === 'limiter_unavailable'
      ? 'unavailable'
      : 'rate_limited';
  const retryAfter = Math.max(1, Number(decision.retryAfter) || 1);
  return json({
    error: MESSAGES[reason] || MESSAGES.limiter_unavailable,
    code,
    retry_after: retryAfter,
  }, status, {
    'Cache-Control': 'no-store',
    'Retry-After': String(retryAfter),
  });
}

function json(obj, status = 200, extraHeaders = {}) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { ...CORS_HEADERS, 'Content-Type': 'application/json', ...extraHeaders },
  });
}

async function loadVoice(fetcher) {
  const r = await fetcher(VOICE_ANCHOR_URL, { cf: { cacheTtl: 3600 } });
  return r.json();
}

async function loadDemos(fetcher) {
  const r = await fetcher(BOT_DEMOS_URL, { cf: { cacheTtl: 3600 } });
  const d = await r.json();
  return d.qa || [];
}

async function loadCorpusIndex(fetcher) {
  const r = await fetcher(CORPUS_INDEX_URL, { cf: { cacheTtl: 3600 } });
  return r.json();
}

// Lightweight retrieval: rank corpus posts by keyword overlap with question.
function retrieve(question, index, k = 3) {
  const qWords = new Set(
    question.toLowerCase().split(/\W+/).filter(w => w.length > 3)
  );
  const scored = index.map(p => {
    let score = 0;
    const text = (p.title + ' ' + p.excerpt + ' ' + p.themes.join(' ') + ' ' + p.locations.join(' ')).toLowerCase();
    for (const w of qWords) if (text.includes(w)) score += 1;
    return { p, score };
  });
  scored.sort((a, b) => b.score - a.score);
  return scored.filter(x => x.score > 0).slice(0, k).map(x => x.p);
}

function buildSystemPrompt(voice, demos, retrieved) {
  const rules = voice.voice_rules.map(r => '- ' + r).join('\n');
  const forbidden = voice.forbidden_phrases.map(p => '- never say: "' + p + '"').join('\n');
  const logic = Object.entries(voice.answer_logic)
    .map(([k, v]) => `[${k}] — ${v}`).join('\n\n');

  const demoSample = demos.slice(0, 12).map(d =>
    `User: ${d.q}\nNon (${d.kind}): ${d.a}\nCitation: ${d.cite || '(none)'}\n---`
  ).join('\n\n');

  const corpus = retrieved.length
    ? '\n\n# Relevant blog excerpts (for grounding only — cite if used)\n\n' +
      retrieved.map(p =>
        `[Post day-${String(p.n).padStart(3,'0')} · ${p.date}] "${p.title}"\n${p.excerpt}`
      ).join('\n\n')
    : '';

  return `${voice.identity}

# Voice rules
${rules}

# Forbidden phrases
${forbidden}

# Answer logic — you MUST pick one of these four kinds for every reply
${logic}

# The chain
${voice.the_chain}

# The central tension (do not resolve)
${voice.central_tension}

# Reply format
Respond as JSON only, no prose outside the JSON:
{ "kind": "DIRECT" | "DEDUCTION" | "STRUCTURAL" | "NOT_KNOWN",
  "answer": "...the answer in his voice, complete prose, no bullet points...",
  "cite":   "Day NN, blog · title  (or other source)  (empty string if none)" }

# Few-shot examples (his actual voice — match this register)
${demoSample}${corpus}`;
}

async function ask(question, env, fetcher = fetch) {
  const [voice, demos, index] = await Promise.all([
    loadVoice(fetcher),
    loadDemos(fetcher),
    loadCorpusIndex(fetcher),
  ]);
  const retrieved = retrieve(question, index, 3);
  const systemPrompt = buildSystemPrompt(voice, demos, retrieved);

  const model = env.ANTHROPIC_MODEL || 'claude-sonnet-4-5';
  const apiKey = env.ANTHROPIC_API_KEY;
  if (!apiKey) {
    return {
      error: 'ANTHROPIC_API_KEY not configured on the worker.',
      hint:  'Run: npx wrangler secret put ANTHROPIC_API_KEY',
    };
  }

  const r = await fetcher('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': apiKey,
      'anthropic-version': '2023-06-01',
    },
    body: JSON.stringify({
      model,
      max_tokens: 800,
      system: systemPrompt,
      messages: [{ role: 'user', content: question }],
    }),
  });

  if (!r.ok) {
    const errText = await r.text();
    return { error: `Anthropic API error ${r.status}`, detail: errText.slice(0, 400) };
  }

  const data = await r.json();
  const raw = (data.content?.[0]?.text || '').trim();

  // Parse JSON reply (defensive: model might wrap in fences)
  let parsed = null;
  try {
    const jsonStr = raw.replace(/^```(?:json)?/i, '').replace(/```$/, '').trim();
    parsed = JSON.parse(jsonStr);
  } catch (e) {
    parsed = { kind: 'DIRECT', answer: raw, cite: '' };
  }

  return {
    ...parsed,
    retrieved: retrieved.map(p => ({
      id: p.id, n: p.n, date: p.date, title: p.title,
    })),
  };
}
