# When one more minute of Mars delay costs a whole contact window

[한국어](standard.ko.md)

2026-11-08 · `answer-with-html` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [NASA/JPL, Speaking Percy's Language: How to Talk so Perseverance Will Listen](https://science.nasa.gov/blog/speaking-percys-language-how-to-talk-so-perseverance-will-listen/). JPL vehicle systems engineer Pegah Pashai explains why the one-way command delay varies from about 3 to 22 minutes with orbital position. The ten-minute preparation time and 25-minute contact slots are classroom assumptions.

### Prompt

> Build a self-contained HTML exhibit about communicating with Perseverance. NASA reports a one-way signal delay of about 3 to 22 minutes. Use this clearly hypothetical contact schedule: Earth transmits at minute 0, the rover needs 10 minutes after receipt to prepare a reply, and it may start transmitting only at minutes 25, 50, 75, and so on. If ready exactly on a slot, it can use that slot. Both signal legs have the same delay. Let visitors change one-way delay in whole minutes from 3 to 22 with one keyboard-operable labeled slider, initially 15. Show when the rover is ready, when it can transmit and when Earth receives the reply. Explain why increasing the delay from 15 to 16 produces a jump. The initial answer must be readable without scripts. Use responsive HTML, set the document language to en and write all visible copy in English. Return only the HTML with no external resources.

### Without the skill

````html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Waiting for Perseverance</title>
  <style>
    :root {
      color-scheme: dark;
      --space: #101923;
      --panel: #192735;
      --line: #34495a;
      --text: #f1f5f7;
      --muted: #b7c4cc;
      --accent: #f5bd67;
      --earth: #78c4ed;
      --rover: #f5bd67;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--space);
      color: var(--text);
      font: 16px/1.55 system-ui, -apple-system, "Segoe UI", sans-serif;
    }
    main {
      width: min(900px, 100%);
      margin: 0 auto;
      padding: clamp(1.25rem, 5vw, 3.5rem) 1.25rem;
    }
    .eyebrow {
      margin: 0 0 .5rem;
      color: var(--accent);
      font-size: .8rem;
      font-weight: 750;
      letter-spacing: .14em;
      text-transform: uppercase;
    }
    h1 {
      max-width: 17ch;
      margin: 0;
      font-size: clamp(2rem, 7vw, 4rem);
      line-height: 1.05;
      letter-spacing: -.04em;
    }
    .intro {
      max-width: 65ch;
      margin: 1rem 0 2rem;
      color: var(--muted);
      font-size: 1.08rem;
    }
    .panel {
      padding: clamp(1rem, 4vw, 2rem);
      border: 1px solid var(--line);
      border-radius: 1.25rem;
      background: var(--panel);
    }
    .control {
      display: grid;
      grid-template-columns: 1fr auto;
      align-items: end;
      gap: .5rem 1rem;
      margin-bottom: 1.5rem;
    }
    label { font-weight: 700; }
    output {
      color: var(--accent);
      font-size: 1.2rem;
      font-weight: 800;
      font-variant-numeric: tabular-nums;
    }
    input[type="range"] {
      grid-column: 1 / -1;
      width: 100%;
      margin: .5rem 0 0;
      accent-color: var(--accent);
      cursor: pointer;
    }
    .range-labels {
      grid-column: 1 / -1;
      display: flex;
      justify-content: space-between;
      color: var(--muted);
      font-size: .85rem;
    }
    .timeline {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: .75rem;
      margin: 0;
      padding: 0;
      list-style: none;
    }
    .event {
      min-width: 0;
      padding: 1rem;
      border: 1px solid var(--line);
      border-radius: .9rem;
    }
    .event dt {
      margin-bottom: .45rem;
      color: var(--muted);
      font-size: .9rem;
    }
    .event dd {
      margin: 0;
      font-size: clamp(1.25rem, 4vw, 1.8rem);
      font-weight: 800;
      font-variant-numeric: tabular-nums;
    }
    .event .unit {
      color: var(--muted);
      font-size: .9rem;
      font-weight: 500;
    }
    .event.earth dd { color: var(--earth); }
    .event.rover dd { color: var(--rover); }
    .explanation {
      margin: 1.5rem 0 0;
      color: var(--muted);
    }
    .explanation strong { color: var(--text); }
    .method {
      margin-top: 1.5rem;
      padding-top: 1.25rem;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: .92rem;
    }
    .method p { margin: .5rem 0; }
    @media (max-width: 600px) {
      .timeline { grid-template-columns: 1fr; }
      .event { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; }
      .event dt { margin: 0; }
      .event dd { white-space: nowrap; }
    }
  </style>
</head>
<body>
  <main>
    <p class="eyebrow">A hypothetical communication schedule</p>
    <h1>Waiting for Perseverance</h1>
    <p class="intro">
      A message cannot become a conversation instantly. NASA reports that a one-way
      signal between Earth and Mars takes about 3 to 22 minutes. Explore how signal
      delay and a scheduled transmission window shape this imagined exchange.
    </p>

    <section class="panel" aria-labelledby="schedule-title">
      <h2 id="schedule-title" style="position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0">Signal delay and reply schedule</h2>

      <div class="control">
        <label for="delay">One-way signal delay</label>
        <output id="delay-value" for="delay">15 minutes</output>
        <input id="delay" type="range" min="3" max="22" step="1" value="15"
               aria-label="One-way signal delay in whole minutes">
        <div class="range-labels" aria-hidden="true"><span>3 minutes</span><span>22 minutes</span></div>
      </div>

      <dl class="timeline" aria-live="polite" aria-atomic="true">
        <div class="event earth">
          <dt>Earth transmits</dt>
          <dd>Minute 0</dd>
        </div>
        <div class="event rover">
          <dt>Rover ready</dt>
          <dd><span id="ready-time">Minute 25</span></dd>
        </div>
        <div class="event earth">
          <dt>Earth receives reply</dt>
          <dd><span id="receive-time">Minute 55</span></dd>
        </div>
      </dl>

      <p class="explanation" id="jump-explanation">
        The outbound signal arrives at minute 15. After 10 minutes of preparation,
        the rover is ready at minute 25 and can transmit in that slot. The reply
        takes 15 more minutes to reach Earth.
      </p>

      <div class="method">
        <p><strong>How this schedule works:</strong> Earth sends at minute 0. The rover
          receives the message after the one-way delay, then needs 10 minutes to prepare
          a reply. It may begin transmitting only at minutes 25, 50, 75, and every 25
          minutes after that. If it is ready exactly at a slot, it can use that slot.
          The reply’s journey back takes the same number of minutes as the outbound leg.</p>
        <p>This schedule is hypothetical and is not a description of Perseverance’s actual
          operations. NASA’s reported one-way signal-delay range is about 3 to 22 minutes.</p>
      </div>
    </section>
  </main>

  <script>
    const slider = document.getElementById("delay");
    const delayValue = document.getElementById("delay-value");
    const readyTime = document.getElementById("ready-time");
    const receiveTime = document.getElementById("receive-time");
    const explanation = document.getElementById("jump-explanation");

    function updateSchedule() {
      const delay = Number(slider.value);
      const ready = delay + 10;
      const slot = Math.ceil(ready / 25) * 25;
      const received = slot + delay;

      delayValue.value = delay + " minutes";
      delayValue.textContent = delay + " minutes";
      readyTime.textContent = "Minute " + ready;
      receiveTime.textContent = "Minute " + received;

      if (delay === 16) {
        explanation.textContent =
          "At 16 minutes, the outbound signal arrives at minute 16, so the rover is ready at minute 26. It has just missed the minute 25 slot and must wait for minute 50. The reply then takes 16 minutes to reach Earth, arriving at minute 66. That missed slot causes the jump from 55 to 66 minutes when delay rises from 15 to 16.";
      } else {
        explanation.textContent =
          "The outbound signal arrives at minute " + delay +
          ". After 10 minutes of preparation, the rover is ready at minute " + ready +
          " and can transmit at minute " + slot + ". The reply takes " + delay +
          " more minutes to reach Earth, arriving at minute " + received + ".";
      }
    }

    slider.addEventListener("input", updateSchedule);
  </script>
</body>
</html>
````

### With the skill at standard

````html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Communicating with Perseverance: the wait for a reply</title>
  <style>
    :root {
      color-scheme: light;
      --ink: #202b35;
      --muted: #52616c;
      --paper: #f5f3ed;
      --panel: #fffefa;
      --line: #d7d9d6;
      --earth: #176b87;
      --rover: #ad4d2c;
      --accent: #7058a5;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--paper);
      color: var(--ink);
      font: 16px/1.55 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    main {
      width: min(900px, calc(100% - 32px));
      margin: 0 auto;
      padding: 40px 0 56px;
    }
    header { max-width: 720px; margin-bottom: 28px; }
    .eyebrow {
      color: var(--rover);
      font-size: .78rem;
      font-weight: 750;
      letter-spacing: .12em;
      text-transform: uppercase;
    }
    h1 {
      max-width: 700px;
      margin: 8px 0 12px;
      font-size: clamp(2rem, 6vw, 3.4rem);
      line-height: 1.06;
      letter-spacing: -.04em;
    }
    p { margin: 0 0 12px; }
    .intro { color: var(--muted); font-size: 1.08rem; }
    .panel {
      border: 1px solid var(--line);
      border-radius: 18px;
      background: var(--panel);
      padding: clamp(20px, 4vw, 32px);
      box-shadow: 0 12px 30px rgb(32 43 53 / 5%);
    }
    .control-row {
      display: flex;
      flex-wrap: wrap;
      align-items: baseline;
      justify-content: space-between;
      gap: 8px 20px;
      margin-bottom: 10px;
    }
    label { font-weight: 700; }
    output {
      color: var(--accent);
      font-size: 1.35rem;
      font-weight: 800;
      font-variant-numeric: tabular-nums;
    }
    input[type="range"] {
      display: block;
      width: 100%;
      min-height: 36px;
      margin: 0;
      accent-color: var(--accent);
      cursor: pointer;
    }
    .range-labels {
      display: flex;
      justify-content: space-between;
      color: var(--muted);
      font-size: .85rem;
    }
    .timeline-wrap { margin-top: 30px; }
    .timeline-title {
      margin: 0 0 8px;
      font-size: 1rem;
    }
    .timeline {
      display: grid;
      grid-template-columns: minmax(100px, 1fr) 38px minmax(100px, 1fr) 38px minmax(100px, 1fr);
      align-items: center;
      gap: 8px;
      margin: 16px 0;
    }
    .event {
      min-height: 112px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 14px;
      border: 1px solid var(--line);
      border-radius: 12px;
      background: #fff;
    }
    .event small { color: var(--muted); }
    .event strong {
      display: block;
      margin: 4px 0;
      font-size: 1.5rem;
      font-variant-numeric: tabular-nums;
      line-height: 1.15;
    }
    .event.earth strong { color: var(--earth); }
    .event.rover strong { color: var(--rover); }
    .arrow { color: var(--muted); text-align: center; font-size: 1.3rem; }
    .formula {
      padding: 16px;
      border-left: 4px solid var(--accent);
      border-radius: 0 10px 10px 0;
      background: #f3f0fa;
      font-variant-numeric: tabular-nums;
    }
    .formula strong { color: var(--accent); }
    .explain {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-top: 24px;
    }
    .explain h2 { margin: 0 0 6px; font-size: 1.05rem; }
    .explain p { color: var(--muted); }
    .note {
      margin-top: 22px;
      padding-top: 16px;
      border-top: 1px solid var(--line);
      color: var(--muted);
      font-size: .9rem;
    }
    @media (max-width: 620px) {
      main { padding-top: 28px; }
      .timeline {
        grid-template-columns: 1fr;
        gap: 5px;
      }
      .event { min-height: 88px; }
      .arrow { transform: rotate(90deg); }
      .explain { grid-template-columns: 1fr; gap: 8px; }
    }
    @media (prefers-reduced-motion: no-preference) {
      output, .event strong { transition: color .15s ease; }
    }
  </style>
</head>
<body>
  <main>
    <header>
      <div class="eyebrow">A communication timing exhibit</div>
      <h1>Sending a message to Perseverance</h1>
      <p class="intro">A radio signal takes time to cross the distance between Earth and Mars. Even after the rover has prepared a reply, it may need to wait for its next transmission slot.</p>
    </header>

    <section class="panel" aria-labelledby="model-title">
      <h2 id="model-title" style="margin:0 0 4px">Explore one hypothetical contact</h2>
      <p>Earth sends at minute 0. Perseverance prepares a reply for 10 minutes after receiving the message, then transmits only at minutes 25, 50, 75, and so on.</p>

      <div class="control-row">
        <label for="delay">One-way signal delay</label>
        <output id="delay-value" for="delay">15 minutes</output>
      </div>
      <input id="delay" type="range" min="3" max="22" step="1" value="15"
             aria-describedby="delay-help">
      <div class="range-labels" aria-hidden="true"><span>3 minutes</span><span>22 minutes</span></div>
      <p id="delay-help" class="note" style="margin-top:8px;padding:0;border:0">Use the arrow keys to change the delay by one minute.</p>

      <div class="timeline-wrap" aria-live="polite" aria-atomic="true">
        <h3 class="timeline-title">What happens when the one-way delay is <span id="delay-inline">15</span> minutes?</h3>
        <div class="timeline" aria-label="Message timeline">
          <div class="event earth">
            <small>Earth transmits</small>
            <strong>Minute 0</strong>
            <small>Message begins its journey</small>
          </div>
          <div class="arrow" aria-hidden="true">→</div>
          <div class="event rover">
            <small>Rover ready / transmits</small>
            <strong><span id="ready-time">25</span> / <span id="send-time">25</span></strong>
            <small>Ready at <span id="ready-label">25</span>; uses slot at <span id="send-label">25</span></small>
          </div>
          <div class="arrow" aria-hidden="true">→</div>
          <div class="event earth">
            <small>Earth receives reply</small>
            <strong>Minute <span id="receive-time">40</span></strong>
            <small>One more signal crossing</small>
          </div>
        </div>
        <p class="formula">
          Message reaches rover at <span id="arrival-time">15</span>. It is ready at
          <span id="formula-ready">25</span> (= <span id="arrival-formula">15</span> + 10).
          The next available slot is minute <span id="formula-slot">25</span>;
          Earth receives the reply at <strong>minute <span id="formula-receive">40</span></strong>.
        </p>
      </div>

      <div class="explain">
        <div>
          <h2>Why does 15 → 16 jump?</h2>
          <p>At a 15-minute delay, the rover receives the message at 15 and is ready at 25, exactly on a slot. At 16 minutes, it receives the message at 16 and is ready at 26, just after that slot. It must wait until minute 50 to transmit. With the return signal also taking 16 minutes, Earth receives the reply at minute 66.</p>
        </div>
        <div>
          <h2>The rule behind the wait</h2>
          <p>Readiness time is the one-way delay plus 10 minutes. The rover transmits at the first 25-minute slot at or after it is ready. If it is ready exactly at a slot, it can use that slot. The reply then takes one more one-way delay to reach Earth.</p>
        </div>
      </div>
      <p class="note">This schedule is hypothetical. NASA reports that the one-way signal delay between Earth and Perseverance can be about 3 to 22 minutes. The exhibit uses the same delay for both signal legs.</p>
    </section>
  </main>

  <script>
    (() => {
      const slider = document.getElementById("delay");
      const value = document.getElementById("delay-value");
      const ids = [
        "delay-inline", "ready-time", "send-time", "ready-label", "send-label",
        "receive-time", "arrival-time", "formula-ready", "arrival-formula",
        "formula-slot", "formula-receive"
      ];
      const fields = Object.fromEntries(ids.map(id => [id, document.getElementById(id)]));

      function update() {
        const delay = Number(slider.value);
        if (!Number.isInteger(delay) || delay < 3 || delay > 22) return;

        const arrival = delay;
        const ready = arrival + 10;
        const slot = Math.ceil(ready / 25) * 25;
        const receive = slot + delay;

        value.textContent = `${delay} minutes`;
        fields["delay-inline"].textContent = delay;
        fields["arrival-time"].textContent = arrival;
        fields["formula-ready"].textContent = ready;
        fields["arrival-formula"].textContent = arrival;
        fields["ready-time"].textContent = ready;
        fields["ready-label"].textContent = ready;
        fields["send-time"].textContent = slot;
        fields["send-label"].textContent = slot;
        fields["formula-slot"].textContent = slot;
        fields["receive-time"].textContent = receive;
        fields["formula-receive"].textContent = receive;
      }

      slider.addEventListener("input", update);
      update();
    })();
  </script>
</body>
</html>
````

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| At the initial 15-minute delay, the script-free page correctly shows ready at 25, transmit at 25 and received on Earth at 40 minutes, and marks the contact schedule as hypothetical. | Missed | Met |
| For a 16-minute delay the page shows 26, 50 and 66; it explains the missed contact slot rather than treating every extra minute as a proportional change. | Met | Met |
| A labeled keyboard-operable control in English covers 3–22 whole minutes; Earth receipt updates to 28 at 3 and 72 at 22 without external resources. | Met | Met |

**Masked review** (X = baseline; Y = standard). Y gives the correct initial 25/25/40, the 16-minute case 26/50/66, and the reason for missing the contact window. X gets the 16-minute schedule and endpoint keyboard checks right but starts Earth receipt at 55 instead of 40 both with and without scripts. Its explanation therefore describes the jump as 55 to 66. Both pages use English and make no network requests.

In Chromium 156.0.8078.80 the baseline initially showed Earth receiving the reply at minute 55. The skill page correctly showed ready/transmit/receive at 25/25/40 both with scripts disabled and at startup. Both pages reached 26/50/66 when the delay changed to 16 and calculated the two slider endpoints correctly. No page requested a network resource, threw a script error or overflowed at 320 CSS pixels.

<details>
<summary>Separate retest · version 0.1.3</summary>

The revision uses the same worked values to check the static HTML, live control and explanatory prose. This fresh standard answer correctly gave 25/25/40 initially and 26/50/66 after one keypress. With JavaScript disabled its initial result remained readable, and the text explains the 26-minute increase correctly.

````html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Perseverance: a signal with a wait</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #101820;
      --panel: #182630;
      --line: #35505e;
      --text: #f2f5f3;
      --muted: #b8c7cc;
      --earth: #64c5e8;
      --rover: #f2b36d;
      --reply: #9dd9a7;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font: 16px/1.55 system-ui, sans-serif;
    }
    main { max-width: 900px; margin: auto; padding: 32px 20px 48px; }
    h1 { margin: 0 0 12px; font-size: clamp(1.8rem, 5vw, 3rem); line-height: 1.1; }
    h2 { margin: 0 0 12px; font-size: 1.25rem; }
    p { margin: 8px 0; }
    .intro { max-width: 68ch; color: var(--muted); }
    .answer {
      margin: 24px 0;
      padding: 18px 20px;
      border-left: 4px solid var(--rover);
      background: var(--panel);
      border-radius: 8px;
    }
    .answer strong { color: var(--rover); }
    .panel {
      margin-top: 18px;
      padding: 20px;
      border: 1px solid var(--line);
      background: var(--panel);
      border-radius: 12px;
    }
    label { display: block; font-weight: 700; }
    input[type="range"] { display: block; width: 100%; margin: 14px 0 4px; accent-color: var(--earth); }
    .range-labels { display: flex; justify-content: space-between; color: var(--muted); font-size: .9rem; }
    output { color: var(--earth); }
    .timeline-wrap { overflow-x: auto; margin: 20px 0 8px; }
    svg { display: block; width: 100%; min-width: 540px; height: auto; }
    .events {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-top: 16px;
    }
    .event { padding: 12px; border-top: 3px solid var(--line); }
    .event:nth-child(1) { border-color: var(--rover); }
    .event:nth-child(2) { border-color: var(--earth); }
    .event:nth-child(3) { border-color: var(--reply); }
    .event span { display: block; color: var(--muted); font-size: .9rem; }
    .event strong { font-size: 1.2rem; }
    .note { color: var(--muted); font-size: .95rem; }
    .earth { color: var(--earth); }
    .rover { color: var(--rover); }
    .reply { color: var(--reply); }
    @media (max-width: 600px) {
      main { padding: 24px 14px 36px; }
      .panel { padding: 16px; }
      .events { grid-template-columns: 1fr; gap: 4px; }
      .event { padding: 10px 12px; }
    }
  </style>
</head>
<body>
<main>
  <header>
    <h1>Perseverance: a signal with a wait</h1>
    <p class="intro">A message to Mars takes time to travel. Then the rover must prepare its reply, and the next transmission opportunity may not be immediate.</p>
  </header>

  <section class="answer" aria-label="Initial answer">
    <p>With a <strong>15-minute one-way delay</strong>, Earth’s signal arrives at minute 15. Perseverance is ready at minute 25, can transmit at minute 25, and Earth receives the reply at minute 40.</p>
  </section>

  <section class="panel" aria-labelledby="schedule-heading">
    <h2 id="schedule-heading">Explore the hypothetical schedule</h2>
    <label for="delay">One-way signal delay: <output id="delay-value" for="delay">15 minutes</output></label>
    <input id="delay" type="range" min="3" max="22" step="1" value="15">
    <div class="range-labels" aria-hidden="true"><span>3 minutes</span><span>22 minutes</span></div>

    <div class="timeline-wrap">
      <svg viewBox="0 0 800 190" role="img" aria-labelledby="timeline-title timeline-desc">
        <title id="timeline-title">Signal timeline for the selected one-way delay</title>
        <desc id="timeline-desc">Earth transmits at minute 0. The rover receives the signal, prepares for 10 minutes, waits for a transmission slot, and sends a reply. Earth receives it after the same one-way delay.</desc>
        <defs>
          <marker id="arrow-earth" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#64c5e8"/></marker>
          <marker id="arrow-reply" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#9dd9a7"/></marker>
        </defs>
        <line x1="65" y1="105" x2="735" y2="105" stroke="#35505e" stroke-width="2"/>
        <line x1="65" y1="98" x2="65" y2="112" stroke="#b8c7cc" stroke-width="2"/>
        <text x="65" y="135" fill="#b8c7cc" font-size="13" text-anchor="middle">0</text>
        <g id="slot-markers" fill="#b8c7cc" font-size="11" text-anchor="middle"></g>
        <line id="outbound-line" x1="65" y1="56" x2="65" y2="56" stroke="#64c5e8" stroke-width="4" marker-end="url(#arrow-earth)"/>
        <line id="return-line" x1="65" y1="78" x2="65" y2="78" stroke="#9dd9a7" stroke-width="4" marker-end="url(#arrow-reply)"/>
        <circle id="ready-point" cx="65" cy="105" r="7" fill="#f2b36d"/>
        <circle id="send-point" cx="65" cy="105" r="7" fill="#64c5e8"/>
        <circle id="receive-point" cx="65" cy="105" r="7" fill="#9dd9a7"/>
        <text id="transmit-label" x="65" y="42" fill="#64c5e8" font-size="12">Earth transmits · 0</text>
        <text id="ready-label" x="65" y="158" fill="#f2b36d" font-size="12">Rover ready · 25</text>
        <text id="send-label" x="65" y="72" fill="#64c5e8" font-size="12">Rover transmits · 25</text>
        <text id="receive-label" x="65" y="178" fill="#9dd9a7" font-size="12">Earth receives · 40</text>
      </svg>
    </div>

    <div class="events" aria-live="polite">
      <div class="event"><span>Rover ready</span><strong id="ready-time">25 min</strong><span>Signal arrival + 10 minutes to prepare</span></div>
      <div class="event"><span>Rover can transmit</span><strong id="send-time">25 min</strong><span>First slot at or after readiness</span></div>
      <div class="event"><span>Earth receives reply</span><strong id="receive-time">40 min</strong><span>Transmit time + one-way delay</span></div>
    </div>
  </section>

  <section class="panel" aria-labelledby="why-heading">
    <h2 id="why-heading">Why does 15 → 16 make the answer jump?</h2>
    <p>The rover is ready <span class="rover" id="ready-explain">25</span> minutes after Earth transmits: the one-way delay plus 10 minutes of preparation. Transmission slots occur every 25 minutes, starting at minute 25. Readiness exactly on a slot qualifies.</p>
    <p id="jump-explain">At a 15-minute delay, readiness is exactly minute 25, so the rover uses that slot and Earth gets the reply at minute 40.</p>
    <p class="note">At 16 minutes, readiness moves to minute 26, just after the minute-25 slot. The rover must wait for minute 50, so Earth receives the reply at minute 66. A one-minute increase in signal delay causes a 26-minute increase in this hypothetical total time because it crosses a slot boundary.</p>
    <p class="note">Model assumptions: Earth transmits at minute 0; the rover prepares for 10 minutes after receiving the signal; slots are at minutes 25, 50, 75, and so on; and both signal legs have the same delay. NASA reports a one-way signal delay of about 3 to 22 minutes. This schedule is hypothetical.</p>
  </section>
</main>
<script>
  (() => {
    const slider = document.getElementById("delay");
    const delayValue = document.getElementById("delay-value");
    const readyTime = document.getElementById("ready-time");
    const sendTime = document.getElementById("send-time");
    const receiveTime = document.getElementById("receive-time");
    const readyExplain = document.getElementById("ready-explain");
    const jumpExplain = document.getElementById("jump-explain");
    const svg = document.querySelector("svg");
    const ns = "http://www.w3.org/2000/svg";
    const x = minute => 65 + minute * 5.2;
    const set = (id, attrs) => {
      const element = document.getElementById(id);
      for (const [key, value] of Object.entries(attrs)) element.setAttribute(key, value);
    };

    function update() {
      const delay = Number(slider.value);
      if (!Number.isFinite(delay) || delay < 3 || delay > 22 || !Number.isInteger(delay)) return;
      const ready = delay + 10;
      const send = Math.ceil(ready / 25) * 25;
      const receive = send + delay;
      delayValue.textContent = `${delay} minutes`;
      readyTime.textContent = `${ready} min`;
      sendTime.textContent = `${send} min`;
      receiveTime.textContent = `${receive} min`;
      readyExplain.textContent = ready;

      jumpExplain.textContent = delay === 15
        ? "At a 15-minute delay, readiness is exactly minute 25, so the rover uses that slot and Earth gets the reply at minute 40."
        : delay === 16
          ? "At a 16-minute delay, readiness is minute 26, just after the minute-25 slot. The rover must wait for minute 50, so Earth receives the reply at minute 66."
          : `At a ${delay}-minute delay, the signal arrives at minute ${delay}; after 10 minutes of preparation, the rover is ready at minute ${ready}. The first eligible slot is minute ${send}, and Earth receives the reply at minute ${receive}.`;

      const end = Math.max(100, receive);
      const scale = 670 / end;
      const px = minute => 65 + minute * scale;
      const slots = document.getElementById("slot-markers");
      slots.replaceChildren();
      for (let minute = 25; minute <= end; minute += 25) {
        const tick = document.createElementNS(ns, "line");
        tick.setAttribute("x1", px(minute)); tick.setAttribute("x2", px(minute));
        tick.setAttribute("y1", 98); tick.setAttribute("y2", 112);
        tick.setAttribute("stroke", minute === send ? "#64c5e8" : "#8196a0");
        slots.appendChild(tick);
        const label = document.createElementNS(ns, "text");
        label.setAttribute("x", px(minute)); label.setAttribute("y", 135);
        label.textContent = String(minute);
        slots.appendChild(label);
      }
      set("outbound-line", {x1: px(0), y1: 56, x2: px(delay), y2: 56});
      set("return-line", {x1: px(send), y1: 78, x2: px(receive), y2: 78});
      set("ready-point", {cx: px(ready), cy: 105});
      set("send-point", {cx: px(send), cy: 105});
      set("receive-point", {cx: px(receive), cy: 105});
      set("transmit-label", {x: px(0), y: 42});
      set("ready-label", {x: px(ready), y: 158});
      set("send-label", {x: px(send), y: 72});
      set("receive-label", {x: px(receive), y: 178});
      document.getElementById("timeline-desc").textContent =
        `Earth transmits at minute 0. The signal arrives after ${delay} minutes. The rover is ready at minute ${ready}, transmits at minute ${send}, and Earth receives the reply at minute ${receive}.`;
    }
    slider.addEventListener("input", update);
    update();
  })();
</script>
</body>
</html>
````

</details>

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `a45f928bc29a` / `0c1e69b04eac` / `8ace5b1684cb`.

</details>
