import assert from 'node:assert/strict';
import { test } from 'node:test';
import {
  DEFAULT_ALLOWED_ORIGINS,
  DEFAULT_LIMITS,
  allowedOrigins,
  bangkokDay,
  clientIp,
  consumeLimit,
  emptyLimitState,
  isAllowedSiteRequest,
  readLimits,
  secondsUntilBangkokMidnight,
} from '../src/limits.js';

const LIMITS = { ...DEFAULT_LIMITS };
const NOON = Date.parse('2026-10-13T05:00:00.000Z'); // 12:00 in Bangkok
const JUST_BEFORE_MIDNIGHT = Date.parse('2026-10-13T16:59:59.000Z');
const MIDNIGHT = Date.parse('2026-10-13T17:00:00.000Z'); // 2026-10-14 00:00 +07

function take(state, ip, now, limits = LIMITS, chargeGlobal = true, maxTrackedIps) {
  return consumeLimit(state, { ip, now, limits, chargeGlobal, maxTrackedIps });
}

test('defaults are 10/min, 100/day, and 200 model calls', () => {
  assert.deepEqual(DEFAULT_LIMITS, {
    perIpPerMinute: 10,
    perIpPerDay: 100,
    globalPerDay: 200,
  });
  assert.deepEqual(readLimits({}), DEFAULT_LIMITS);
  assert.deepEqual(readLimits({
    RATE_LIMIT_PER_MINUTE: '4',
    RATE_LIMIT_PER_DAY: '9',
    GLOBAL_DAILY_CAP: '0',
  }), { perIpPerMinute: 4, perIpPerDay: 9, globalPerDay: 0 });
  assert.equal(readLimits({ GLOBAL_DAILY_CAP: '-5' }).globalPerDay, 200);
  assert.equal(readLimits({ GLOBAL_DAILY_CAP: 'nope' }).globalPerDay, 200);
});

test('the museum day follows Asia/Bangkok', () => {
  assert.equal(bangkokDay(JUST_BEFORE_MIDNIGHT), '2026-10-13');
  assert.equal(bangkokDay(MIDNIGHT), '2026-10-14');
  assert.equal(secondsUntilBangkokMidnight(NOON), 12 * 60 * 60);
  assert.equal(secondsUntilBangkokMidnight(MIDNIGHT), 24 * 60 * 60);
});

test('a star origin does not open the guard', () => {
  assert.deepEqual(allowedOrigins({}), DEFAULT_ALLOWED_ORIGINS);
  assert.deepEqual(allowedOrigins({ ALLOWED_ORIGIN: '*' }), DEFAULT_ALLOWED_ORIGINS);
  assert.deepEqual(
    allowedOrigins({ ALLOWED_ORIGINS: 'https://100.nonarkara.org/, https://preview.example' }),
    ['https://100.nonarkara.org', 'https://preview.example'],
  );
});

test('origin is required, and a bad origin is not saved by Referer', () => {
  const site = (headers) => new Request('https://100.nonarkara.org/api/ask', { headers });
  assert.equal(isAllowedSiteRequest(site({ Origin: 'https://100.nonarkara.org' }), {}), true);
  assert.equal(isAllowedSiteRequest(site({ Referer: 'https://100.nonarkara.org/bot/' }), {}), true);
  assert.equal(isAllowedSiteRequest(site({}), {}), false);
  assert.equal(isAllowedSiteRequest(site({ Origin: 'null' }), {}), false);
  assert.equal(isAllowedSiteRequest(site({
    Origin: 'https://evil.example',
    Referer: 'https://100.nonarkara.org/',
  }), {}), false);
  assert.equal(isAllowedSiteRequest(site({
    Origin: 'https://100.nonarkara.org.evil.example',
  }), {}), false);
});

test('CF-Connecting-IP wins over a spoofed forwarded header', () => {
  const request = new Request('https://100.nonarkara.org/api/ask', {
    headers: {
      'CF-Connecting-IP': '203.0.113.8',
      'X-Forwarded-For': '198.51.100.9, 10.0.0.1',
    },
  });
  assert.equal(clientIp(request), '203.0.113.8');
  const forwarded = new Request('https://100.nonarkara.org/api/ask', {
    headers: { 'X-Forwarded-For': '198.51.100.9, 10.0.0.1' },
  });
  assert.equal(clientIp(forwarded), '198.51.100.9');
  assert.equal(clientIp(new Request('https://100.nonarkara.org/api/ask')), 'unknown');
});

test('token bucket allows a burst of 10 and refills one token per 6 seconds', () => {
  let state = emptyLimitState();
  for (let i = 0; i < 10; i += 1) {
    const step = take(state, '203.0.113.1', NOON);
    assert.equal(step.ok, true, `request ${i + 1}`);
    state = step.state;
  }
  const blocked = take(state, '203.0.113.1', NOON);
  assert.equal(blocked.ok, false);
  assert.equal(blocked.reason, 'per_minute');
  assert.equal(blocked.retryAfter, 6);
  assert.equal(blocked.writes, null);
  assert.equal(blocked.state.globalCount, 10);

  const early = take(state, '203.0.113.1', NOON + 5999);
  assert.equal(early.ok, false);
  assert.equal(early.reason, 'per_minute');

  const refilled = take(state, '203.0.113.1', NOON + 6000);
  assert.equal(refilled.ok, true);
  assert.equal(refilled.state.ips['203.0.113.1'].tokens, 0);

  const other = take(state, '203.0.113.2', NOON);
  assert.equal(other.ok, true);
});

test('per-IP day cap is 100 and resets at Bangkok midnight', () => {
  const limits = { perIpPerMinute: 1000, perIpPerDay: 100, globalPerDay: 1000 };
  let state = emptyLimitState();
  for (let i = 0; i < 100; i += 1) {
    const step = take(state, '203.0.113.1', NOON, limits);
    assert.equal(step.ok, true);
    state = step.state;
  }
  const blocked = take(state, '203.0.113.1', NOON, limits);
  assert.equal(blocked.reason, 'per_day');
  assert.equal(blocked.state.globalCount, 100);

  const nextDay = take(state, '203.0.113.1', MIDNIGHT, limits);
  assert.equal(nextDay.ok, true);
  assert.equal(nextDay.state.globalCount, 1);
  assert.equal(nextDay.state.ips['203.0.113.1'].dayCount, 1);
});

test('global cap counts model calls only and stops at 200', () => {
  const limits = { perIpPerMinute: 1000, perIpPerDay: 1000, globalPerDay: 200 };
  let state = emptyLimitState();
  const unpaid = take(state, '203.0.113.1', NOON, limits, false);
  assert.equal(unpaid.ok, true);
  assert.equal(unpaid.writes.global, undefined);
  assert.equal(unpaid.state.globalCount, 0);
  state = unpaid.state;

  for (let i = 0; i < 200; i += 1) {
    const step = take(state, `203.0.113.${i}`, NOON, limits, true, 5000);
    assert.equal(step.ok, true, `call ${i + 1}`);
    state = step.state;
  }
  assert.equal(state.globalCount, 200);
  const blocked = take(state, '203.0.113.250', NOON, limits, true, 5000);
  assert.equal(blocked.ok, false);
  assert.equal(blocked.reason, 'global_day');
  assert.equal(blocked.state.globalCount, 200);
  assert.equal(blocked.state.ips['203.0.113.250'], undefined);
});

test('a full global cap does not consume the caller bucket', () => {
  const limits = { perIpPerMinute: 10, perIpPerDay: 100, globalPerDay: 0 };
  const blocked = take(emptyLimitState(), '203.0.113.1', NOON, limits, true);
  assert.equal(blocked.reason, 'global_day');
  assert.equal(blocked.writes, null);
  const personal = take(blocked.state, '203.0.113.1', NOON, limits, false);
  assert.equal(personal.ok, true);
});

test('new addresses are refused once the tracked-IP cap is full', () => {
  const limits = { perIpPerMinute: 10, perIpPerDay: 100, globalPerDay: 50 };
  let state = emptyLimitState();
  state = take(state, '203.0.113.1', NOON, limits, true, 1).state;
  const crowded = take(state, '203.0.113.2', NOON, limits, true, 1);
  assert.equal(crowded.reason, 'crowded');
  const again = take(state, '203.0.113.1', NOON, limits, true, 1);
  assert.equal(again.ok, true);
});
