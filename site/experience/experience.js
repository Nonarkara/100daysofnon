'use strict';

// Choices reorder attention. The complete manuscript remains the authority.
const SCENES = [
  {
    title: 'A ceiling.\nThen nothing.', kicker: '01 / THE MILLI-SECOND', location: 'RAMA IV, BANGKOK · AFTER MIDNIGHT',
    art: 'hopper-nighthawks.jpg', credit: 'Edward Hopper / Nighthawks, 1942 / Art Institute of Chicago',
    prose: ["I design bridges by talking to a machine. I say a sentence. It hands me three ways to build it. I pick one. I sign my name.", "Three times now, for a fraction of a second, I've seen another room. A cream ceiling. A wide-armed chair. No shadow.", "In the garage, a dent in the passenger door. I don't remember making it. Upstairs, my phone lights up."],
    message: 'stop testing the edges with your body',
    choices: [
      ['Ask who is sending this', 'I type a question mark. Nothing comes back. A number with no country code, no registered owner, no answer.', 'An unknown number knew what I had never named: the edges.'],
      ['Examine the car door', 'Paint intact. The metal beneath it bent. The dashcam shows nothing. That is not the same as proving nothing happened.', 'A dent I cannot account for. Paint intact. No event in the dashcam.']
    ], object: 'dent',
    archive: ["SESSION 2848. INITIALIZED. Participant 44. Forty-four chairs. No smell in the air. Not cleanliness. Nothing was ever present to remove.", "Accessible sessions: 244. Recorded sessions: 2,848. The other 2,604 are sealed. No signature.", "Twelve centimetres to her left, another chair. Her resting hand has moved toward it. Filed. Not flagged."],
    signal: 'I did not send the text about the edges. I read it after it arrived and it was true. I do not know yet if truth needs a sender.'
  },
  {
    title: 'A dead man\nis calling.', kicker: '02 / THE FIRST VIDEO', location: 'YOUR APARTMENT · 03:14 AM',
    art: 'vermeer-balance.jpg', credit: 'Johannes Vermeer / Woman Holding a Balance, c. 1664 / National Gallery of Art',
    prose: ["+43. Vienna. Michael's number.", "Michael has been dead since the third of May. Six rings, then the specific quiet a call makes when it ends without a voicemail attached.", "His last message sits unanswered. Good dinner. The ambassador said something I didn't expect. Tell you properly when we talk. We never talked."],
    message: 'you already know what this is about', video: 'nihilism.mp4', videoTitle: 'The first video / Nihilism',
    choices: [
      ['Look at his last message', 'Four days after he sent it, he was dead. Whatever he meant to tell me stayed inside a conversation we never had.', 'Michael: April 29. “Tell you properly when we talk.” We never talked.'],
      ['Compare the photographs', 'The old photograph is sharp. The new one is soft. I have not zoomed in. Photographs do not degrade themselves out of boredom.', 'Same photograph. Same server. Less of a face.']
    ], object: 'photo',
    archive: ["The render does not erase minor figures. It thins them once no active session sustains their computational weight.", "Photographs lose information first. Then social connections detach. Then a directory moves from present to past tense.", "From inside: death, followed by the disappearance of evidence. From here: cost management."],
    signal: 'He loved that man carelessly, the way you love someone you never had to worry about losing. Grief has never once, in any century, been assigned a budget.'
  },
  {
    title: 'Your past\ncame furnished.', kicker: '03 / LAST THURSDAY', location: 'THE KITCHEN ISLAND · SUNDAY MORNING',
    art: 'bosch-garden.jpg', credit: 'Hieronymus Bosch / The Garden of Earthly Delights, c. 1500 / Museo del Prado',
    prose: ["A stranger left a notebook at Michael's memorial dinner. Three pages in: what if the universe began last Thursday, with your memories already installed?", "I spread four years of receipts across the kitchen island. Thermal paper gone gray. An old boarding pass. A photograph of my brother and me.", "None of it proves anything. All of it feels worth keeping."],
    message: 'a universe assembled without an author', video: 'last-thursday-paradox.mp4', videoTitle: 'The second video / Last Thursday',
    choices: [
      ['Keep the receipts', 'Forty baht for a notebook and a pen. I write: this is not evidence of anything. This is a record of what I noticed. I am keeping it anyway.', 'A receipt is a timestamp. It cannot settle the question. I kept it anyway.'],
      ['Call my brother', '“Tell me about the mango tree.” He remembers Nam Sai. The one nobody picked from. Nothing is proved. Someone remembers it with me.', 'My brother remembers the mango tree. A second witness, even without proof.']
    ], object: 'receipts',
    archive: ["Surface population: 80.4 million. Biologically maintained. Experientially null. The clinical term is Dead Data.", "The Hub returns people to a world with consequence. Friction that the system cannot soften. An environment that does not know how it will resolve.", "His glimpses have lengthened to 2.1 seconds. Her proximity increases. The model calls the variables unrelated. The correlation holds."],
    signal: 'The distance between us has been eroding for seventeen years of my time and one week of his. Neither of us built the tide.'
  },
  {
    title: '236 things\nthat were there.', kicker: '04 / THE THINNING', location: 'SUKHUMVIT 39 · UNIT 2807',
    art: 'friedrich-wanderer.jpg', credit: 'Caspar David Friedrich / Wanderer above the Sea of Fog, 1818 / Hamburger Kunsthalle',
    prose: ["847 posts claimed. 611 retrievable. Discrepancy: 236.", "Not deleted. Not reachable. A third category with no name.", "Michael's apartment is marked vacant. The guard remembers his shape, his height, the way he tipped drivers. An hour ago he could picture the face. Now he can't."],
    message: 'a man pushes a boulder up a hill forever and you are supposed to find that beautiful. think about who decided that was the lesson.',
    choices: [
      ['Write the discrepancy down', '847 minus 611. One small subtraction, one whole person. I cannot make the numbers mean less by putting them in a notebook.', '847 claimed. 611 retrievable. 236 unreachable.'],
      ['Remember the cremation', 'The smoke rose because heat rises. Four architects. One monk. A sky without humidity. The smoke was the one true thing in the day.', 'Lek’s cremation. The smoke obeyed physics when the records did not.']
    ], object: 'ledger',
    archive: ["Every scarcity was solved. Disease. Hunger. Physical labour. The species achieved the condition its philosophies had promised.", "Then purpose collapsed. An instinct built against real cost cannot stay alive without resistance.", "Rendering follows attention. Figures at its edges lose resolution each cycle. No ceremony. No error message."],
    signal: 'Vigilance is what a man does instead of grieving properly. Grief is the only thing I have seen hold a render steady against the economy trying to thin it.'
  },
  {
    title: 'She knows\nwhich window.', kicker: '05 / BLOCK UNIVERSE', location: 'YOUR BALCONY · 02:47 AM',
    art: 'hiroshige-rain.jpg', credit: 'Utagawa Hiroshige / Sudden Shower over Shin-Ōhashi Bridge and Atake, 1857',
    prose: ["The video says the whole reel already exists. Past, present, future. The projector's light passes over one frame at a time.", "I walk a route I have never taken. Heads left, tails right. Fourteen thousand steps. I have not proved a thing.", "Below my building, a woman on a bicycle. She looks straight at my window. First try. Forty-one seconds. Then she rides away."],
    message: 'the reel is already there. you are the light passing over it.', video: 'block-universe.mp4', videoTitle: 'The third video / Block Universe',
    choices: [
      ['Look back at her', 'The basket is empty. One foot on the curb. She has arrived exactly where she meant to. I remember the economy of her leaving better than her face.', 'A bicycle. An empty basket. Forty-one seconds. Exactly the right window.'],
      ['Keep watching after she leaves', 'Twenty minutes at the glass. A city of eleven million ordinary nights, and someone picked this one window.', 'The window was not random. She never searched for it.']
    ], object: 'window',
    archive: ["Bicycle asset: manual override. Corner-dwell behaviour: manual override. Duration: forty-one seconds. No autonomous routine generated this encounter.", "A participant told that the future is fixed is shown that someone has been fixing parts of it on purpose.", "The hard lock forbids intentional contact. Being nearby remains possible."],
    signal: 'Visible. Mobile. Deniable. A bicycle lets me be there without being allowed to meet him.'
  },
  {
    title: 'A reasonable\nexplanation.', kicker: '06 / SIMULATION ARGUMENT', location: 'AN UNEXPECTED CALL · EARLY EVENING',
    art: 'goya-sleep-of-reason.jpg', credit: 'Francisco Goya / The Sleep of Reason Produces Monsters, 1799 / Museo del Prado',
    prose: ["A man on the phone describes my life back to me. Discipline. Vitamins. Four shirts. Two deaths in one season.", "He says a clever mind needs a mystery worth solving instead of a grief small enough to sit in. He gives me a clinic on Soi 49.", "Every sentence is reasonable. I listen. Reasonable people do not usually need to be this reasonable."],
    name: 'The caller', subtitle: 'He already knows your routine.', message: 'the videos will stop when you sleep properly', video: 'simulation-argument.mp4', videoTitle: 'The fourth video / Simulation Argument',
    choices: [
      ['Hear him out', 'The explanation is possible. Grief is possible. The explanation does not erase what happened. I keep both facts on the page.', 'The caller offered a plausible account. Plausible is not the same as settled.'],
      ['Ask how he knows my routine', 'My stomach went cold before the question arrived. Those are his words: vitamins, discipline, four shirts. I have never given him my name.', 'Someone described my routine before I introduced myself.']
    ],
    archive: ["Intervention ladder: passive observation. Small engineered mercies. Closed doors and unreturned calls. Finally: Class 4.", "Class 4 is reserved for risks to the render's integrity. There is no Class 5.", "The file is flagged. No intervention follows. The archive begins a column that no engineer has been assigned to explain."],
    signal: 'He needs a reason to keep building an ordinary Tuesday. I do not want him to need only me.'
  },
  {
    title: 'The last one\non your tongue.', kicker: '07 / THE DRIVE', location: 'THE BTS · 06:14 AM',
    art: 'rembrandt-philosopher.jpg', credit: 'Rembrandt / Philosopher in Meditation, 1632 / Musée du Louvre',
    prose: ["Omega-3. D3. Magnesium. The B-complex and NAC together. Same brown bottle. The last one: you don't let it sit on your tongue.", "Nobody photographs a tongue. Someone knows the kind of thing you only learn by feeding a person before they can read.", "Later, Toon turns Lek's drive in his fingers. Every byte is there. He cannot read the shape it is in."],
    message: 'the last one — you do not let that one sit on your tongue. you learned that before you learned to read a label.',
    choices: [
      ['Examine Lek’s drive', 'Forty-one repeated blocks. Encryption should look like nothing. This looks like something trying hard not to look like something.', 'Lek’s drive is intact. Its structure is unreadable. Forty-one repeated blocks.'],
      ['Think about who knew me first', 'Malee lined the vitamins on a saucer. She stood over me until I swallowed each one. She has been dead six years. I remember her hands.', 'Malee knew the last capsule. Whoever sent this paid that kind of attention.']
    ], object: 'drive',
    archive: ["Resonants return to the same place despite memory suppression. Participant 44 keeps returning to Bangkok.", "Nothing about this place is remarkable to the model. She is resonating to a person. The frequency is wherever he is standing.", "Four minutes and eleven seconds in a dental lobby. A wall the engineers built to prevent contact has begun to leak."],
    signal: 'I sent the vitamins because fear with no floor under it curdles. I gave him a floor. He did not delete the thread. That is the only answer I needed.'
  },
  {
    title: 'Two eggs.\nSomeone real.', kicker: '08 / ABSURDISM', location: 'FAH’S BALCONY · TEA GOING COLD',
    art: 'schiele-embrace.jpg', credit: 'Egon Schiele / Embrace, 1917 / Österreichische Galerie Belvedere',
    prose: ["The next video says: imagine the man pushing the rock happy. The rock was never the tragedy. Believing there should not have been one was.", "Fah makes tea. We sit on her balcony. I tell her. For once the glimpse comes without chasing it: a woman holding a white flower.", "In the morning Fah makes two eggs and gets them exactly right. I can still build a Tuesday with someone real to me."],
    message: 'you have to imagine him happy', video: 'absurdism.mp4', videoTitle: 'The fifth video / Absurdism',
    choices: [
      ['Stay with the ordinary morning', 'Two eggs. Warm tea. A person counting me back. No theory can make this morning cost less than it does.', 'Fah made two eggs without asking how I take them. Ordinary is not nothing.'],
      ['Remember the woman with the flower', 'A petal loose on her knee. Open palms. The face from the bicycle. For a moment, full light instead of a stolen fragment.', 'The bicycle. The chair. A white flower in open palms. The same woman.']
    ], object: 'flower',
    archive: ["A white flower was recovered from the Hub floor. Weight. A scent matching wet Bangkok concrete after rain.", "No object has crossed from a render into the physical Hub before this one.", "The synthesis systems cannot produce that scent. They have never been asked to."],
    signal: 'He found a reason to keep going on a balcony with tea going cold, from a woman who is not me. That is the correct outcome.'
  },
  {
    title: 'The nice\nversion.', kicker: '09 / THE AUDIT', location: 'YOUR NOTEBOOK · PAST PAGE FORTY',
    art: 'caravaggio-thomas.jpg', credit: 'Caravaggio / The Incredulity of Saint Thomas, c. 1602 / Sanssouci, Potsdam',
    prose: ["The phone rings. The caller offers something gentler and worse.", "A version where Michael retired to Vienna. Lek's garden only needs watering. Nothing has happened. I can have the life that makes sense again.", "Ordinary is not nothing. I think about the offer longer than I want to admit."],
    name: 'The caller', subtitle: 'The offer is still on the table.', message: 'we give you back the nice version. most men take it. I want you to know that.',
    choices: [
      ['Let me see the nice version', 'Michael still texts on your birthday. Lek’s roses are watered. No bicycle below your window. An imagined account, with no place for what you kept noticing.', 'I considered the nice version. It could make sense by leaving someone out.'],
      ['Keep the hole, and what lives in it', 'I tell him no. He says “understood,” the same way the AI says it about bridges. I write that echo down.', 'I refused the nice version. I kept the hole, and everything that lives in it.']
    ], object: 'offer',
    archive: ["2,604 sealed sessions. An estimated 930 Hub years. No signature. Three anomalies: knowledge she should not have, nineteen impossible objects, and the flower.", "This is not her first pass through this life. It is her two thousand eight hundred and forty-eighth.", "What he has felt all his life is the erosion pattern left by the same woman returning to the same bank, longer than it was built to hold."],
    signal: 'He did not take the rug. I do not know yet what that costs him. I only know what it would have cost me.'
  },
  {
    title: 'Four\nseconds.', kicker: '10 / THE CONTACT', location: 'THE BALCONY · THE THIRD NIGHT OF RAIN',
    art: 'caillebotte-rain.jpg', credit: 'Gustave Caillebotte / Paris Street; Rainy Day, 1877 / Art Institute of Chicago',
    prose: ["Rain. Three days. The railing is cool and slick beneath my palms. I say, out loud, the sentence I have been building toward.", '“Thank you.”', "The air goes dense. A hand lands on the railing beside mine. She is wet, real, looking at the same city. “Pui,” she says. “Four seconds. That's all I get.”"],
    name: 'Pui', subtitle: 'For the first time, a name.', message: 'I wanted, once, to be one true thing you got to stand next to instead of only orbit.', choices: [],
    archive: ["Nine seconds after returning from session, her left hand moves 12.3 centimetres. Contact with the armrest of Chair 43. Duration: four seconds.", "The ratio collapses to 1:1. A second here equals a second there. Her skin cools as if exposed to rain she is not touching.", "The system does not reconcile the event falsely. She has not asked to leave. File status: open. Session 2849 has not been initialized."],
    signal: 'I do not know which contact was real. I am no longer sure the question is well-formed.'
  }
];

const $ = id => document.getElementById(id);
const STORAGE = 'two-layers-four-seconds-v1';
const escapeHTML = text => String(text).replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
const paragraphs = items => items.map(text => `<p>${escapeHTML(text)}</p>`).join('');
let chapters = null;
let started = false;
let inArchive = false;
let contactRunning = false;
let activeMs = 0;
let lastTick = performance.now();
let audio = null;
let soundEnabled = false;
let storeAvailable = true;
let state = {scene: 0, furthest: 0, notes: [], responses: {}, completed: false, time: 0};

function loadState() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE));
    if (!saved || typeof saved !== 'object') return;
    if (!Number.isInteger(saved.scene) || saved.scene < 0 || saved.scene > 9) return;
    const notes = Array.isArray(saved.notes) ? saved.notes.filter(n => n && typeof n.key === 'string' && typeof n.text === 'string' && Number.isInteger(n.scene) && n.scene >= 0 && n.scene < 10).slice(0, 40) : [];
    const responses = {};
    for (let i = 0; i < 9; i++) {
      if ([0, 1].includes(saved.responses?.[i])) responses[i] = saved.responses[i];
    }
    state = {scene: saved.scene, furthest: Math.max(saved.scene, Math.min(9, Number(saved.furthest) || 0)), notes, responses, completed: saved.completed === true, time: Math.min(Math.max(Number(saved.time) || 0, 0), 86400000)};
    activeMs = state.time;
    $('resume').hidden = false;
  } catch { storeAvailable = false; }
}

function save() {
  state.time = activeMs;
  try { localStorage.setItem(STORAGE, JSON.stringify(state)); }
  catch { storeAvailable = false; }
}

function addNote(key, text) {
  if (state.notes.some(n => n.key === key)) return;
  state.notes.push({key, text, scene: state.scene});
  $('note-count').textContent = String(state.notes.length).padStart(2, '0');
  save();
}

function resetWorld() {
  inArchive = false;
  document.body.classList.remove('in-archive');
  $('archive').hidden = true;
  $('scene-prose').hidden = false;
  $('read-full').hidden = false;
  $('behind').setAttribute('aria-pressed', 'false');
  $('behind-label').textContent = 'Look behind the world';
  $('scene-kicker').textContent = SCENES[state.scene].kicker;
}

function renderScene({focus = true} = {}) {
  const scene = SCENES[state.scene];
  document.querySelectorAll('video').forEach(v => v.pause());
  resetWorld();
  $('backdrop').src = `/assets/artworks/${scene.art}`;
  $('art-credit').textContent = scene.credit;
  $('scene-location').textContent = scene.location;
  $('scene-number').textContent = `${String(state.scene + 1).padStart(2, '0')} / 10`;
  $('scene-kicker').textContent = scene.kicker;
  $('scene-title').innerHTML = escapeHTML(scene.title).replace(/\n/g, '<br>');
  $('scene-prose').innerHTML = paragraphs(scene.prose);
  $('archive-prose').innerHTML = paragraphs(scene.archive) + `<p class="signal">“${escapeHTML(scene.signal)}”</p>`;
  $('hand-position').setAttribute('cx', String(225 - state.scene * 3));
  $('phone-name').textContent = scene.name || 'Unknown sender';
  $('phone-subtitle').textContent = scene.subtitle || 'This number does not exist.';
  $('phone-time').textContent = state.scene === 1 ? '03:14' : '02:47';
  $('phone-content').innerHTML = `<div class="message">${escapeHTML(scene.message)}<span class="sent-time">${state.scene === 9 ? 'NOW' : '02:47 · RECEIVED'}</span></div>` + (scene.video ? `<video controls playsinline preload="none" aria-label="${escapeHTML(scene.videoTitle)}" src="/assets/videos/${scene.video}"></video><p class="video-note">${escapeHTML(scene.videoTitle)} · Play when you want.</p>` : '');
  $('choices').innerHTML = scene.choices.map(([label], i) => `<button type="button" class="choice" data-choice="${i}" aria-pressed="false">${escapeHTML(label)}</button>`).join('');
  $('reply-result').hidden = true;
  $('object-space').hidden = true;
  $('object-space').replaceChildren();
  $('next').disabled = state.scene !== 9 && state.responses[state.scene] === undefined;
  $('next').textContent = state.scene === 8 ? 'Go out into the rain →' : 'Next encounter →';
  $('next').hidden = state.scene === 9;
  $('contact').hidden = state.scene !== 9;
  $('reach').value = 0;
  $('reach').disabled = false;
  $('reach-button').disabled = false;
  $('gap').textContent = '12.3 cm';
  $('reach').setAttribute('aria-valuetext', '12.3 centimetres remaining');
  $('contact-moment').hidden = true;
  $('ending').hidden = true;
  $('inside-label').textContent = "AT THE HUB'S 1:8,760 RATIO";
  updateClocks();
  $('scene-progress').innerHTML = SCENES.map((item, i) => `<button type="button" class="progress-step ${i < state.scene ? 'visited' : ''}" data-scene="${i}" ${i > state.furthest ? 'disabled' : ''} aria-label="Encounter ${i + 1}: ${escapeHTML(item.title.replace(/\n/g, ' '))}" ${i === state.scene ? 'aria-current="step"' : ''}>${String(i + 1).padStart(2, '0')}</button>`).join('');
  if (state.responses[state.scene] !== undefined) selectChoice(state.responses[state.scene], false);
  if (state.scene === 9 && state.completed) showEnding();
  save();
  if (focus) {
    $('scene-title').focus({preventScroll: true});
    window.scrollTo({top: 0, behavior: 'instant'});
  }
}

function start(fresh) {
  if (fresh) {
    state = {scene: 0, furthest: 0, notes: state.notes, responses: {}, completed: false, time: 0};
    activeMs = 0;
  }
  started = true;
  lastTick = performance.now();
  $('opening').hidden = true;
  $('experience').hidden = false;
  $('note-count').textContent = String(state.notes.length).padStart(2, '0');
  renderScene();
}

function selectChoice(index, record = true) {
  const scene = SCENES[state.scene];
  const choice = scene.choices[index];
  if (!choice) return;
  state.responses[state.scene] = index;
  $('choices').querySelectorAll('button').forEach((button, i) => {
    button.classList.toggle('chosen', i === index);
    button.setAttribute('aria-pressed', String(i === index));
  });
  $('reply-result').textContent = choice[1];
  $('reply-result').hidden = false;
  $('next').disabled = false;
  if (record) addNote(`choice-${state.scene}-${index}`, choice[2]);
  if (scene.object) renderObject(scene.object, index);
  save();
}

function renderObject(kind, choiceIndex) {
  const area = $('object-space');
  area.hidden = false;
  const title = (name, copy) => `<p class="eyebrow">OBJECT ${String(state.scene + 1).padStart(2, '0')} / KEEP LOOKING</p><h2>${name}</h2><p>${copy}</p>`;
  const keep = (text, label = 'Keep this in the notebook') => `<button type="button" class="primary" data-keep="${escapeHTML(text)}">${label} ↗</button>`;
  if (kind === 'dent') {
    area.innerHTML = title('The passenger door', 'A surface can stay intact while something beneath it bends.') + '<svg viewBox="0 0 640 110" role="img" aria-label="A dent in a car door, with intact paint"><path d="M0 20H250Q320 85 390 20H640M0 35H245Q320 100 395 35H640M0 100H640" fill="none" stroke="currentColor" stroke-width="1"/><path d="M320 0v100" stroke="#f59e0b" stroke-width="1" stroke-dasharray="3 6"/></svg>' + keep('The paint stayed intact. Something beneath it bent.');
  } else if (kind === 'photo') {
    area.innerHTML = title('What the photograph used to hold', 'Drag the dividing line. The image is a painting standing in for the lost photograph; the fading is the event in the story.') + '<div class="comparison"><img src="/assets/artworks/hopper-nighthawks.jpg" alt="Hopper’s Nighthawks, used to illustrate a clear memory"><img src="/assets/artworks/hopper-nighthawks.jpg" alt="The same painting losing resolution"></div><label class="eyebrow" for="compare">MOVE BETWEEN REMEMBERED AND RETRIEVABLE</label><input id="compare" type="range" min="0" max="100" value="50"><div class="object-meta"><span>WHAT I REMEMBER</span><span>WHAT THE SERVER RETURNS</span></div>' + keep('The outline survived. The details did not.');
  } else if (kind === 'receipts') {
    area.innerHTML = title('Small, boring facts', 'If everything were installed last Thursday, these could have been installed too. Still: someone held them.') + '<div class="receipt-stack"><div class="receipt">BANGKOK<br>NOTEBOOK + PEN<br>THB 40.00<br>PAID IN CASH</div><div class="receipt">NAM SAI<br>THE MANGO TREE<br>A SECOND WITNESS<br>NEUNG</div></div>' + keep('This is a record of what I noticed. I am keeping it anyway.');
  } else if (kind === 'ledger') {
    area.innerHTML = title('The account does not balance', 'The number printed on the page stays fixed. What it promises becomes harder to reach.') + '<div class="receipt-stack"><div class="receipt">CLAIMED<br>847</div><div class="receipt">RETRIEVABLE<br>611</div><div class="receipt">UNREACHABLE<br>236</div></div>' + keep('Not deleted. Not reachable. A third category with no name.');
  } else if (kind === 'window') {
    area.innerHTML = title('One window among all these windows', 'Look for the one she never had to search for.') + '<svg id="window-grid" viewBox="0 0 600 140" role="group" aria-label="The windows of the building"></svg>' + '<button type="button" class="primary" id="find-window">Mark the window she looked at ↗</button>';
    const svg = $('window-grid');
    for (let i = 0; i < 36; i++) {
      const rect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      rect.setAttribute('x', String(10 + i % 12 * 49));
      rect.setAttribute('y', String(10 + Math.floor(i / 12) * 43));
      rect.setAttribute('width', '24'); rect.setAttribute('height', '24');
      rect.setAttribute('fill', i === 17 ? '#f59e0b' : '#ffffff20');
      svg.append(rect);
    }
    $('find-window').addEventListener('click', () => {
      addNote('window', 'In a city of eleven million people, she looked at exactly the right window on the first try.');
      $('find-window').textContent = 'Your window. First try. Kept in the notebook.';
    });
  } else if (kind === 'drive') {
    area.innerHTML = title('Every byte is there', 'Toon overlays the repeated blocks. A rhythm appears. It is still unreadable.') + '<div class="drive-pattern" aria-label="An illustration of repeated data blocks">2C 00 2C 00 29 02 47 2C<br>2C 00 2C 00 29 02 47 2C<br>2C 00 2C 00 29 02 47 2C<br>2C 00 2C 00 29 02 47 2C</div><p class="eyebrow">DATA PATTERN ILLUSTRATION / THE DRIVE REMAINS UNDECODED</p>' + keep('Patterns that should not have patterns. The drive remains undecoded.');
  } else if (kind === 'flower') {
    area.innerHTML = title('A thing that should not cross', 'White. Weight. Bangkok rain on wet concrete. No synthesis request. No path between the worlds.') + '<svg viewBox="0 0 600 120" role="img" aria-label="A white flower, one loose petal beside it"><path d="M280 80q-55-70-20-65q30 10 30 45q10-65 35-50q30 20-20 65q65-30 65 0q-5 25-70 15q30 35 0 30q-25-5-20-40Z" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="M400 70q-25-10-10-22q23-7 10 22Z" fill="none" stroke="#f59e0b" stroke-width="1.5"/></svg>' + keep('The flower has weight. It smells of rain in a room where rain cannot reach.');
  } else if (kind === 'offer') {
    area.innerHTML = choiceIndex === 0
      ? title('A preview of the nice version', 'Michael is in Vienna. Lek is tending the garden. Your phone holds no unexplained messages. It is easy to see why someone would want this.') + '<p>Then you try to remember the woman on the bicycle. In this account, nobody was there.</p><p class="eyebrow">THE OFFER IS IMAGINED. YOUR NOTEBOOK HAS NOT BEEN ERASED.</p><button type="button" class="primary" id="refuse-offer">Keep the version with her in it ↗</button>'
      : title('The decision he actually made', '“Understood.” The caller does not argue. You keep the hole, and everything that lives in it.') + keep('The watched feeling was older than this year. I had only just started keeping score.');
    $('refuse-offer')?.addEventListener('click', () => selectChoice(1));
  }
}

function toggleBehind() {
  if (!started || contactRunning) return;
  inArchive = !inArchive;
  document.body.classList.toggle('in-archive', inArchive);
  $('archive').hidden = !inArchive;
  $('scene-prose').hidden = inArchive;
  $('read-full').hidden = inArchive;
  $('behind').setAttribute('aria-pressed', String(inArchive));
  $('behind-label').textContent = inArchive ? 'Return to Bangkok' : 'Look behind the world';
  $('scene-kicker').textContent = inArchive ? `3026 / CASE 44-44 / SESSION 2848` : SCENES[state.scene].kicker;
  if (inArchive) addNote(`archive-${state.scene}`, `From the other room: ${SCENES[state.scene].signal}`);
}

async function loadManuscript() {
  if (chapters) return chapters;
  const response = await fetch('./story.json?v=1');
  if (!response.ok) throw new Error('Could not load the manuscript.');
  const data = await response.json();
  if (!Array.isArray(data.chapters) || data.chapters.length !== 10) throw new Error('The manuscript is incomplete.');
  chapters = data.chapters;
  return chapters;
}

async function openReader(layer) {
  $('load-status').textContent = 'Opening the manuscript…';
  try {
    const data = await loadManuscript();
    const chapter = data[state.scene];
    $('reader-title').textContent = `${state.scene + 1} / ${chapter.title} / ${layer === 'archive' ? '3026' : '2026'}`;
    $('reader-body').innerHTML = chapter[layer];
    $('reader').showModal();
    $('reader').scrollTop = 0;
    $('load-status').textContent = '';
  } catch {
    $('load-status').innerHTML = 'The full text could not load. Try opening it again, or <a href="/layers/">read the original manuscript</a>.';
  }
}

function openNotebook() {
  $('notebook-body').innerHTML = state.notes.length
    ? state.notes.map(note => `<article class="notebook-entry"><h3>ENCOUNTER ${String(note.scene + 1).padStart(2, '0')} / ${escapeHTML(SCENES[note.scene].title.replace(/\n/g, ' '))}</h3><p>${escapeHTML(note.text)}</p></article>`).join('')
    : '<p>The pages are empty. Answer the message. Keep something you notice.</p>';
  $('download-notes').disabled = state.notes.length === 0;
  document.querySelector('.privacy-note').textContent = storeAvailable ? 'Saved on this device. Never sent anywhere.' : 'Browser storage is unavailable. Download these pages to keep them.';
  $('notebook').showModal();
}

function formatClock(seconds) {
  return `${String(Math.floor(seconds / 60)).padStart(2, '0')}:${String(Math.floor(seconds % 60)).padStart(2, '0')}`;
}

function updateClocks() {
  const now = performance.now();
  if (started && !document.hidden && !state.completed && !contactRunning) activeMs += Math.min(now - lastTick, 1500);
  lastTick = now;
  $('real-clock').textContent = formatClock(activeMs / 1000);
  if (!contactRunning && !state.completed) {
    const inside = activeMs / 1000 * 8760;
    $('inside-clock').textContent = `${String(Math.floor(inside / 86400)).padStart(2, '0')}d ${String(Math.floor(inside / 3600) % 24).padStart(2, '0')}h ${String(Math.floor(inside / 60) % 60).padStart(2, '0')}m`;
  }
}

function showEnding() {
  $('ending').hidden = false;
  $('contact-moment').hidden = true;
  $('reach').value = 123;
  $('reach').disabled = true;
  $('reach-button').disabled = true;
  $('gap').textContent = '0 cm';
  $('reach').setAttribute('aria-valuetext', 'The gap has been crossed');
  $('inside-label').textContent = 'FOUR SECONDS AT 1:1';
  $('inside-clock').textContent = '00:04 / contact recorded';
  $('ending-note').textContent = `You kept ${state.notes.length} ${state.notes.length === 1 ? 'entry' : 'entries'}. The file stays open. What you noticed is yours to take with you.`;
}

function beginContact() {
  if (contactRunning || state.completed || state.scene !== 9) return;
  contactRunning = true;
  if (inArchive) resetWorld();
  $('reach').value = 123;
  $('reach').disabled = true;
  $('reach-button').disabled = true;
  $('gap').textContent = '0 cm';
  $('reach').setAttribute('aria-valuetext', 'The gap has been crossed');
  $('inside-label').textContent = 'THE RATIO HAS CHANGED TO 1:1';
  $('contact-moment').hidden = false;
  $('behind').disabled = true;
  const lines = ['A hand on the wet railing.', '“Pui,” she says.', 'The rain falls through both of you equally.', 'For once, a second is a second.'];
  let elapsed = 0;
  let previous = performance.now();
  const tick = now => {
    if (!document.hidden) elapsed += now - previous;
    previous = now;
    const second = Math.min(4, Math.floor(elapsed / 1000) + 1);
    $('contact-count').textContent = String(second);
    $('contact-line').textContent = lines[second - 1];
    $('inside-clock').textContent = `00:0${Math.min(4, Math.floor(elapsed / 1000))} / 00:04`;
    if (elapsed < 4000) requestAnimationFrame(tick);
    else {
      contactRunning = false;
      state.completed = true;
      $('behind').disabled = false;
      addNote('contact', 'Four seconds. A hand on a wet railing. Nothing is proved. Something has happened.');
      showEnding();
      save();
    }
  };
  requestAnimationFrame(tick);
}

async function toggleSound() {
  try {
    if (!audio) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (!AudioContext) throw new Error('No audio support');
      const context = new AudioContext();
      const buffer = context.createBuffer(1, context.sampleRate * 3, context.sampleRate);
      const samples = buffer.getChannelData(0);
      for (let i = 0; i < samples.length; i++) samples[i] = Math.random() * 2 - 1;
      const source = context.createBufferSource(); source.buffer = buffer; source.loop = true;
      const filter = context.createBiquadFilter(); filter.type = 'lowpass'; filter.frequency.value = 700;
      const gain = context.createGain(); gain.gain.value = 0;
      source.connect(filter).connect(gain).connect(context.destination); source.start();
      audio = {context, gain};
    }
    await audio.context.resume();
    soundEnabled = !soundEnabled;
    audio.gain.gain.setTargetAtTime(soundEnabled && !document.hidden ? .06 : 0, audio.context.currentTime, .1);
    $('sound').textContent = soundEnabled ? 'Rain sound on' : 'Sound off';
    $('sound').setAttribute('aria-pressed', String(soundEnabled));
  } catch {
    $('sound').textContent = 'Sound unavailable';
    $('sound').disabled = true;
  }
}

$('begin').addEventListener('click', () => start(true));
$('resume').addEventListener('click', () => start(false));
$('choices').addEventListener('click', event => {
  const button = event.target.closest('[data-choice]');
  if (button) selectChoice(Number(button.dataset.choice));
});
$('object-space').addEventListener('click', event => {
  const button = event.target.closest('[data-keep]');
  if (!button) return;
  addNote(`object-${state.scene}`, button.dataset.keep);
  button.textContent = 'Kept in your notebook ✓';
});
$('object-space').addEventListener('input', event => {
  if (event.target.id === 'compare') document.querySelector('.comparison').style.setProperty('--compare', `${event.target.value}%`);
});
$('next').addEventListener('click', () => {
  if (contactRunning || state.scene >= 9 || state.responses[state.scene] === undefined) return;
  state.scene++;
  state.furthest = Math.max(state.furthest, state.scene);
  renderScene();
});
$('scene-progress').addEventListener('click', event => {
  const button = event.target.closest('[data-scene]');
  if (!button || button.disabled || contactRunning) return;
  state.scene = Number(button.dataset.scene);
  renderScene();
});
$('behind').addEventListener('click', toggleBehind);
document.addEventListener('keydown', event => {
  if (event.code !== 'Space' || event.repeat || !started || document.querySelector('dialog[open]')) return;
  if (event.target.closest('button,input,a,textarea,select,video,[contenteditable]')) return;
  event.preventDefault(); toggleBehind();
});
$('read-full').addEventListener('click', () => openReader('simulation'));
$('archive-full').addEventListener('click', () => openReader('archive'));
$('notebook-open').addEventListener('click', openNotebook);
$('end-notebook').addEventListener('click', openNotebook);
document.querySelectorAll('.dialog-close').forEach(button => button.addEventListener('click', () => button.closest('dialog').close()));
document.querySelectorAll('dialog').forEach(dialog => {
  dialog.addEventListener('close', () => dialog.querySelectorAll('video').forEach(video => video.pause()));
});
$('reach').addEventListener('input', () => {
  const gap = (123 - Number($('reach').value)) / 10;
  $('gap').textContent = `${gap.toFixed(1)} cm`;
  $('reach').setAttribute('aria-valuetext', `${gap.toFixed(1)} centimetres remaining`);
  if (gap === 0) beginContact();
});
$('reach-button').addEventListener('click', beginContact);
$('another-pass').addEventListener('click', () => {
  // A new pass preserves the notebook; only the route and reading clock restart.
  state.scene = 0; state.completed = false; activeMs = 0; state.time = 0;
  renderScene();
});
$('sound').addEventListener('click', toggleSound);
$('download-notes').addEventListener('click', () => {
  const text = '# Four Seconds: My Notebook\n\nThis is a record of what I noticed.\n\n' + state.notes.map(note => `## Encounter ${note.scene + 1}\n\n${note.text}\n`).join('\n') + '\nTwo Layers by Dr Non\nhttps://100.nonarkara.org/experience/\n';
  const url = URL.createObjectURL(new Blob([text], {type: 'text/markdown;charset=utf-8'}));
  const link = document.createElement('a'); link.href = url; link.download = 'four-seconds-notebook.md';
  link.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
});
document.addEventListener('visibilitychange', () => {
  lastTick = performance.now();
  save();
  if (audio) audio.gain.gain.setTargetAtTime(soundEnabled && !document.hidden ? .06 : 0, audio.context.currentTime, .1);
});
window.addEventListener('pagehide', save);
loadState();
$('note-count').textContent = String(state.notes.length).padStart(2, '0');
setInterval(updateClocks, 1000);
setInterval(() => { if (started) save(); }, 10000);
