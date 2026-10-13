import assert from 'node:assert/strict';
import { test } from 'node:test';
import worker, { handleRequest } from '../src/index.js';
import { AskLimiter } from '../src/limiter.js';
import { MESSAGES } from '../src/limits.js';

const NOON = Date.parse('2026-10-13T05:00:00.000Z');

function memoryStorage() {
  const data = new Map();
  return {
    data,
    async get(key) {
      await Promise.resolve();
      return data.has(key) ? structuredClone(data.get(key)) : undefined;
    },
    async put(key, value) {
      await Promise.resolve();
      data.set(key, structuredClone(value));
    },
  };
}

function limiterContext(storage) {
  let tail = Promise.resolve();
  return {
    storage,
    blockConcurrencyWhile(fn) {
      const run = tail.then(() => fn());
      tail = run.then(() => {}, () => {});
      return run;
    },
  };
}

function bindingFor(limiter) {
  return {
    idFromName(name) {
      assert.equal(name, 'global');
      return 'global';
    },
    get(id) {
      assert.equal(id, 'global');
      return {
        fetch(url, init) {
          return limiter.fetch(new Request(url, init));
        },
      };
    },
  };
}

function envWith(limiter, extra = {}) {
  return {
    ANTHROPIC_API_KEY: 'test-key',
    ANTHROPIC_MODEL: 'claude-sonnet-4-5',
    ASK_LIMITER: bindingFor(limiter),
    ...extra,
  };
}

function freshLimiter() {
  return new AskLimiter(limiterContext(memoryStorage()));
}

function ask(question, { ip = '203.0.113.10', origin, referer, extraHeaders = {} } = {}) {
  const headers = {
    'Content-Type': 'application/json',
    'CF-Connecting-IP': ip,
    ...extraHeaders,
  };
  if (origin) headers.Origin = origin;
  if (referer) headers.Referer = referer;
  return new Request('https://100.nonarkara.org/api/ask', {
    method: 'POST',
    headers,
    body: JSON.stringify({ question }),
  });
}

function siteFetch(pages) {
  const calls = [];
  const fetcher = async (url, init) => {
    const href = String(url);
    calls.push({ url: href, init });
    if (href.includes('voice-anchor')) {
      return Response.json({
        identity: 'Non.',
        voice_rules: ['Be brief.'],
        forbidden_phrases: ['as an AI'],
        answer_logic: { DIRECT: 'From the record.' },
        the_chain: 'chain',
        central_tension: 'tension',
      });
    }
    if (href.includes('bot-demos')) {
      return Response.json({ qa: [{ q: 'Demo?', a: 'Yes.', kind: 'DIRECT', cite: 'Day 01' }] });
    }
    if (href.includes('corpus-index')) {
      return Response.json([{
        id: 'day-001',
        n: 1,
        date: '2020-01-01',
        title: 'Bangkok rain',
        excerpt: 'The soi was flooded.',
        themes: ['rain'],
        locations: ['Bangkok'],
      }]);
    }
    if (href.includes('api.anthropic.com')) {
      return Response.json({
        content: [{ text: '{"kind":"DIRECT","answer":"From the record.","cite":"Day 01, blog · Bangkok rain"}' }],
      });
    }
    throw new Error(`unexpected fetch ${href}`);
  };
  return { fetcher, calls, pages };
}

function modelCalls(calls) {
  return calls.filter((call) => call.url.includes('api.anthropic.com'));
}

test('health, preflight, and unknown routes stay open', async () => {
  const health = await worker.fetch(new Request('https://100.nonarkara.org/api/health'));
  assert.equal(health.status, 200);
  const healthBody = await health.json();
  assert.equal(healthBody.ok, true);
  assert.equal(typeof healthBody.ts, 'string');
  assert.equal(health.headers.get('Access-Control-Allow-Origin'), '*');

  const preflight = await worker.fetch(new Request('https://evil.example/api/ask', { method: 'OPTIONS' }));
  assert.equal(preflight.status, 200);
  assert.equal(preflight.headers.get('Access-Control-Allow-Methods'), 'POST, GET, OPTIONS');

  const missing = await worker.fetch(new Request('https://100.nonarkara.org/nope'));
  assert.equal(missing.status, 404);
  assert.deepEqual(await missing.json(), { error: 'Not found' });
});

test('the default export rejects an off-site caller before any model call', async () => {
  let fetched = false;
  const previous = globalThis.fetch;
  globalThis.fetch = async () => {
    fetched = true;
    throw new Error('network');
  };
  try {
    const res = await worker.fetch(ask('Where is Bangkok?', { origin: 'https://evil.example' }), {
      ANTHROPIC_API_KEY: 'test-key',
      ASK_LIMITER: bindingFor(freshLimiter()),
    });
    assert.equal(res.status, 403);
    assert.deepEqual(await res.json(), { error: MESSAGES.origin, code: 'origin' });
    assert.equal(fetched, false);
  } finally {
    globalThis.fetch = previous;
  }
});

test('a normal question still returns the same answer shape', async () => {
  const net = siteFetch();
  const res = await handleRequest(
    ask('Tell me about the Bangkok rain', { origin: 'https://100.nonarkara.org' }),
    envWith(freshLimiter()),
    { fetch: net.fetcher, now: () => NOON },
  );
  assert.equal(res.status, 200);
  assert.equal(res.headers.get('Retry-After'), null);
  assert.equal(res.headers.get('Access-Control-Allow-Origin'), '*');
  assert.deepEqual(await res.json(), {
    kind: 'DIRECT',
    answer: 'From the record.',
    cite: 'Day 01, blog · Bangkok rain',
    retrieved: [{ id: 'day-001', n: 1, date: '2020-01-01', title: 'Bangkok rain' }],
  });
  const models = modelCalls(net.calls);
  assert.equal(models.length, 1);
  const sent = JSON.parse(models[0].init.body);
  assert.equal(sent.model, 'claude-sonnet-4-5');
  assert.equal(sent.messages[0].content, 'Tell me about the Bangkok rain');
  assert.match(sent.system, /Bangkok rain/);
  assert.match(sent.system, /Demo\?/);
});

test('Referer from the museum is enough when Origin is absent', async () => {
  const net = siteFetch();
  const res = await handleRequest(
    ask('Hello from the record', { referer: 'https://100.nonarkara.org/bot/' }),
    envWith(freshLimiter()),
    { fetch: net.fetcher, now: () => NOON },
  );
  assert.equal(res.status, 200);
  assert.equal(modelCalls(net.calls).length, 1);
});

test('bad questions are rejected before the limiter or the model', async () => {
  const limiter = freshLimiter();
  let reservations = 0;
  const wrapped = bindingFor(limiter);
  const realGet = wrapped.get;
  wrapped.get = (id) => {
    reservations += 1;
    return realGet(id);
  };
  const env = envWith(limiter);
  env.ASK_LIMITER = wrapped;
  const net = siteFetch();

  const empty = await handleRequest(ask('   ', { origin: 'https://100.nonarkara.org' }), env, { fetch: net.fetcher });
  assert.equal(empty.status, 400);
  assert.deepEqual(await empty.json(), { error: 'Question must be 1–500 chars.' });

  const broken = await handleRequest(new Request('https://100.nonarkara.org/api/ask', {
    method: 'POST',
    headers: { Origin: 'https://100.nonarkara.org', 'Content-Type': 'application/json' },
    body: '{',
  }), env, { fetch: net.fetcher });
  assert.equal(broken.status, 400);

  const long = await handleRequest(
    ask('x'.repeat(501), { origin: 'https://100.nonarkara.org' }),
    env,
    { fetch: net.fetcher },
  );
  assert.equal(long.status, 400);
  assert.equal(reservations, 0);
  assert.equal(modelCalls(net.calls).length, 0);
});

test('the 11th question in a minute is a 429 and does not call the model', async () => {
  const net = siteFetch();
  const env = envWith(freshLimiter());
  let now = NOON;
  for (let i = 0; i < 10; i += 1) {
    const res = await handleRequest(
      ask(`Question ${i} about Bangkok`, { origin: 'https://100.nonarkara.org' }),
      env,
      { fetch: net.fetcher, now: () => now },
    );
    assert.equal(res.status, 200, `question ${i + 1}`);
  }
  const blocked = await handleRequest(
    ask('One more about Bangkok', { origin: 'https://100.nonarkara.org' }),
    env,
    { fetch: net.fetcher, now: () => now },
  );
  assert.equal(blocked.status, 429);
  assert.equal(blocked.headers.get('Retry-After'), '6');
  const body = await blocked.json();
  assert.equal(body.error, MESSAGES.per_minute);
  assert.equal(body.code, 'rate_limited');
  assert.equal(modelCalls(net.calls).length, 10);

  const spoofed = await handleRequest(
    ask('Spoofed forwarded address', {
      origin: 'https://100.nonarkara.org',
      extraHeaders: { 'X-Forwarded-For': '198.51.100.77' },
    }),
    env,
    { fetch: net.fetcher, now: () => now },
  );
  assert.equal(spoofed.status, 429);

  const other = await handleRequest(
    ask('A different connection', { ip: '203.0.113.77', origin: 'https://100.nonarkara.org' }),
    env,
    { fetch: net.fetcher, now: () => now },
  );
  assert.equal(other.status, 200);

  now += 5999;
  const early = await handleRequest(
    ask('Still early', { origin: 'https://100.nonarkara.org' }),
    env,
    { fetch: net.fetcher, now: () => now },
  );
  assert.equal(early.status, 429);

  now += 1;
  const later = await handleRequest(
    ask('A minute has passed', { origin: 'https://100.nonarkara.org' }),
    env,
    { fetch: net.fetcher, now: () => now },
  );
  assert.equal(later.status, 200);
});

test('the daily model cap stops further Claude calls', async () => {
  const net = siteFetch();
  const env = envWith(freshLimiter(), {
    GLOBAL_DAILY_CAP: '2',
    RATE_LIMIT_PER_MINUTE: '10',
    RATE_LIMIT_PER_DAY: '100',
  });
  const deps = { fetch: net.fetcher, now: () => NOON };
  const first = await handleRequest(ask('One', { ip: '203.0.113.1', origin: 'https://100.nonarkara.org' }), env, deps);
  const second = await handleRequest(ask('Two', { ip: '203.0.113.2', origin: 'https://100.nonarkara.org' }), env, deps);
  const third = await handleRequest(ask('Three', { ip: '203.0.113.3', origin: 'https://100.nonarkara.org' }), env, deps);
  assert.equal(first.status, 200);
  assert.equal(second.status, 200);
  assert.equal(third.status, 429);
  assert.equal((await third.json()).code, 'daily_cap');
  assert.equal(modelCalls(net.calls).length, 2);
});

test('a missing API key does not call the model or spend the global cap', async () => {
  const net = siteFetch();
  const limiter = freshLimiter();
  const env = envWith(limiter, { GLOBAL_DAILY_CAP: '1', ANTHROPIC_API_KEY: '' });
  const deps = { fetch: net.fetcher, now: () => NOON };
  const blocked = await handleRequest(
    ask('Is the key missing?', { origin: 'https://100.nonarkara.org' }),
    env,
    deps,
  );
  assert.equal(blocked.status, 200);
  assert.deepEqual(await blocked.json(), {
    error: 'ANTHROPIC_API_KEY not configured on the worker.',
    hint: 'Run: npx wrangler secret put ANTHROPIC_API_KEY',
  });
  assert.equal(modelCalls(net.calls).length, 0);

  env.ANTHROPIC_API_KEY = 'test-key';
  const allowed = await handleRequest(
    ask('Now with a key', { ip: '203.0.113.44', origin: 'https://100.nonarkara.org' }),
    env,
    deps,
  );
  assert.equal(allowed.status, 200);
  assert.equal(modelCalls(net.calls).length, 1);
});

test('per-day env limit is enforced', async () => {
  const net = siteFetch();
  const env = envWith(freshLimiter(), {
    RATE_LIMIT_PER_MINUTE: '10',
    RATE_LIMIT_PER_DAY: '2',
    GLOBAL_DAILY_CAP: '50',
  });
  const deps = { fetch: net.fetcher, now: () => NOON };
  assert.equal((await handleRequest(ask('A', { origin: 'https://100.nonarkara.org' }), env, deps)).status, 200);
  assert.equal((await handleRequest(ask('B', { origin: 'https://100.nonarkara.org' }), env, deps)).status, 200);
  const third = await handleRequest(ask('C', { origin: 'https://100.nonarkara.org' }), env, deps);
  assert.equal(third.status, 429);
  assert.equal((await third.json()).error, MESSAGES.per_day);
  assert.equal(modelCalls(net.calls).length, 2);
});

test('a missing or broken limiter fails closed', async () => {
  const net = siteFetch();
  const deps = { fetch: net.fetcher, now: () => NOON };
  const missing = await handleRequest(
    ask('Hello', { origin: 'https://100.nonarkara.org' }),
    { ANTHROPIC_API_KEY: 'test-key' },
    deps,
  );
  assert.equal(missing.status, 503);
  assert.equal((await missing.json()).error, MESSAGES.limiter_unavailable);

  const broken = await handleRequest(ask('Hello again', { origin: 'https://100.nonarkara.org' }), {
    ANTHROPIC_API_KEY: 'test-key',
    ASK_LIMITER: {
      idFromName() { return 'global'; },
      get() { return { fetch() { throw new Error('storage down'); } }; },
    },
  }, deps);
  assert.equal(broken.status, 503);
  assert.equal(modelCalls(net.calls).length, 0);
});

test('the durable object does not hand the last global slot to two callers', async () => {
  const limiter = freshLimiter();
  const limits = { perIpPerMinute: 10, perIpPerDay: 100, globalPerDay: 1 };
  const call = (ip) => limiter.fetch(new Request('https://limiter.internal/consume', {
    method: 'POST',
    body: JSON.stringify({ ip, now: NOON, limits, chargeGlobal: true }),
  }));
  const [a, b] = await Promise.all([call('203.0.113.1'), call('203.0.113.2')]);
  const bodyA = await a.json();
  const bodyB = await b.json();
  assert.equal([bodyA.ok, bodyB.ok].filter(Boolean).length, 1);
  assert.equal(bodyA.state, undefined);
  assert.equal(bodyA.ips, undefined);
  assert.equal(limiter.storage.data.get('global').count, 1);
});

test('a 500-character question is still accepted', async () => {
  const net = siteFetch();
  const question = `Bangkok ${'x'.repeat(492)}`;
  assert.equal(question.length, 500);
  const res = await handleRequest(
    ask(question, { origin: 'https://100.nonarkara.org' }),
    envWith(freshLimiter()),
    { fetch: net.fetcher, now: () => NOON },
  );
  assert.equal(res.status, 200);
  assert.equal(modelCalls(net.calls).length, 1);
});
