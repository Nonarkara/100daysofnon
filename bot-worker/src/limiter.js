// One SQLite Durable Object holds every per-IP bucket and the daily model cap.
// Requests are serialized so two callers cannot both take the last slot.
// The worker maps the decision onto HTTP; this object always returns JSON.

import { consumeLimit, normalizeIp } from './limits.js';

export class AskLimiter {
  constructor(ctx) {
    this.ctx = ctx;
    this.storage = ctx.storage;
  }

  async fetch(request) {
    let body = null;
    try {
      body = await request.json();
    } catch {
      body = null;
    }
    if (!body || typeof body !== 'object') {
      return Response.json({ ok: false, reason: 'limiter_unavailable', retryAfter: 30 });
    }

    const consume = () => this.consume(body);
    const decision = this.ctx.blockConcurrencyWhile
      ? await this.ctx.blockConcurrencyWhile(consume)
      : await consume();

    return Response.json({
      ok: Boolean(decision.ok),
      reason: decision.reason || null,
      retryAfter: decision.retryAfter || 0,
    });
  }

  async consume(body) {
    const ip = normalizeIp(body.ip);
    const now = Number.isFinite(body.now) ? body.now : Date.now();
    const [storedGlobal, storedMeta, storedIp] = await Promise.all([
      this.storage.get('global'),
      this.storage.get('meta'),
      this.storage.get(`ip:${ip}`),
    ]);

    const state = {
      globalDay: (storedGlobal && storedGlobal.day) || '',
      globalCount: Number(storedGlobal && storedGlobal.count) || 0,
      trackedDay: (storedMeta && storedMeta.day) || '',
      tracked: Number(storedMeta && storedMeta.tracked) || 0,
      ips: storedIp ? { [ip]: storedIp } : {},
    };

    const result = consumeLimit(state, {
      ip,
      now,
      limits: body.limits,
      chargeGlobal: body.chargeGlobal,
    });

    if (result.writes) {
      const jobs = [this.storage.put(`ip:${ip}`, result.writes.ip)];
      if (result.writes.global) jobs.push(this.storage.put('global', result.writes.global));
      if (result.writes.meta) jobs.push(this.storage.put('meta', result.writes.meta));
      await Promise.all(jobs);
    }

    return result;
  }
}
