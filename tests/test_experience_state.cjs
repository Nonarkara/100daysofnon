const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const {test} = require('node:test');

const source = fs.readFileSync(path.join(__dirname, '../site/experience/experience.js'), 'utf8');

function harness(saved, storageBlocked = false) {
  const elements = new Map();
  const element = id => {
    if (!elements.has(id)) elements.set(id, {
      hidden: false, disabled: false, textContent: '', value: 0,
      classList: {add() {}, remove() {}, toggle() {}},
      setAttribute(name, value) { this[name] = value; },
      querySelectorAll() { return []; },
      addEventListener() {}, replaceChildren() {}, focus() {},
    });
    return elements.get(id);
  };
  const frames = [];
  const listeners = new Map();
  let now = 0;
  const context = vm.createContext({
    document: {
      body: element('body'), hidden: false,
      getElementById: element, querySelectorAll: () => [],
      addEventListener(name, fn) {
        if (!listeners.has(name)) listeners.set(name, []);
        listeners.get(name).push(fn);
      },
    },
    window: {addEventListener() {}, scrollTo() {}},
    localStorage: {
      getItem() {
        if (storageBlocked) throw new Error('Storage blocked');
        return saved;
      },
      setItem() { if (storageBlocked) throw new Error('Storage blocked'); },
    },
    performance: {now: () => now},
    setInterval() {},
    requestAnimationFrame: fn => frames.push(fn),
  });
  vm.runInContext(source, context);
  return {
    element, frames, run: code => vm.runInContext(code, context),
    visibility(hidden, time) {
      now = time;
      context.document.hidden = hidden;
      for (const fn of listeners.get('visibilitychange') || []) fn();
    },
  };
}

test('malformed and unavailable browser storage still allow the story to start', () => {
  for (const h of [harness('{'), harness(null, true)]) {
    h.run('start(true)');
    assert.equal(h.element('experience').hidden, false);
    assert.equal(h.run('state.scene'), 0);
  }
});

test('a fresh route preserves earned notebook entries', () => {
  const h = harness(JSON.stringify({scene: 5, notes: [{key: 'kept', text: 'A receipt', scene: 2}], responses: {5: 1}}));
  h.run('start(true)');
  assert.equal(h.run('state.notes.length'), 1);
  assert.equal(h.run('Object.keys(state.responses).length'), 0);
  assert.equal(h.element('note-count').textContent, '01');
});

test('stored notebook text is escaped, invalid scenes and choices are discarded', () => {
  const h = harness(JSON.stringify({scene: 2, notes: [{key: 'safe', text: '<script>x</script>', scene: 2}, {key: 'bad', text: 'outside', scene: 100}], responses: {2: 9, 1: 0}}));
  assert.equal(h.run('state.notes.length'), 1);
  assert.equal(h.run('state.responses[2]'), undefined);
  assert.equal(h.run('state.responses[1]'), 0);
  assert.equal(h.run("escapeHTML(state.notes[0].text)"), '&lt;script&gt;x&lt;/script&gt;');
});

test('notes are not duplicated on revisit', () => {
  const h = harness(null);
  h.run("addNote('window', 'First try'); addNote('window', 'First try')");
  assert.equal(h.run('state.notes.length'), 1);
});

test('contact from the archive restores Bangkok and takes four foreground seconds', () => {
  const h = harness(null);
  h.run('started = true; state.scene = 9; inArchive = true; beginContact()');
  assert.equal(h.element('scene-kicker').textContent, '10 / THE CONTACT');
  assert.equal(h.run('state.completed'), false);
  h.frames.shift()(1000);
  h.run('document.hidden = true');
  h.frames.shift()(5000);
  assert.equal(h.run('state.completed'), false);
  h.run('document.hidden = false');
  h.frames.shift()(6000);
  h.frames.shift()(7000);
  assert.equal(h.run('state.completed'), false);
  h.frames.shift()(8000);
  assert.equal(h.run('state.completed'), true);
  assert.equal(h.element('ending').hidden, false);
  assert.equal(h.run('state.notes[0].key'), 'contact');
});

test('a suspended animation frame does not count time in a hidden tab', () => {
  const h = harness(null);
  h.run('started = true; state.scene = 9; beginContact()');
  h.frames.shift()(1000);
  h.visibility(true, 1000);
  // Browsers suspend animation frames while the tab is hidden.
  h.visibility(false, 61000);
  h.frames.shift()(62000);
  assert.equal(h.run('state.completed'), false);
  h.frames.shift()(63000);
  assert.equal(h.run('state.completed'), false);
  h.frames.shift()(64000);
  assert.equal(h.run('state.completed'), true);
});
