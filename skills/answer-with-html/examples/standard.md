# When one more minute of Mars delay costs a whole contact window

2026-11-08 · `answer-with-html` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [NASA/JPL, Speaking Percy's Language: How to Talk so Perseverance Will Listen](https://science.nasa.gov/blog/speaking-percys-language-how-to-talk-so-perseverance-will-listen/). JPL vehicle systems engineer Pegah Pashai explains why the one-way command delay varies from about 3 to 22 minutes with orbital position. The ten-minute preparation time and 25-minute contact slots are classroom assumptions.

**Reasoning task.** Model two travel legs, a processing interval and a discrete contact schedule; reason about the sharp change when readiness crosses a slot boundary.

### Prompt

> Build a self-contained HTML exhibit about communicating with Perseverance. NASA reports a one-way signal delay of about 3 to 22 minutes. Use this clearly hypothetical contact schedule: Earth transmits at minute 0, the rover needs 10 minutes after receipt to prepare a reply, and it may start transmitting only at minutes 25, 50, 75, and so on. If ready exactly on a slot, it can use that slot. Both signal legs have the same delay. Let visitors change one-way delay in whole minutes from 3 to 22 with one keyboard-operable labeled slider, initially 15. Show when the rover is ready, when it can transmit and when Earth receives the reply. Explain why increasing the delay from 15 to 16 produces a jump. The initial answer must be readable without scripts. Return only the HTML with no external resources.

### Without a skill

````html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>A Conversation with Perseverance</title>
  <style>
    :root {
      color-scheme: dark;
      --ink: #f4f0e8;
      --muted: #b8becb;
      --bg: #101722;
      --panel: #192434;
      --line: #35445a;
      --earth: #70c8ff;
      --rover: #ffc76f;
      --reply: #b8a2ff;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: radial-gradient(ellipse at 80% 0%, #26334a 0, var(--bg) 55%);
      color: var(--ink);
      font: 16px/1.55 system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    main { width: min(900px, 100% - 32px); margin: 0 auto; padding: 48px 0 56px; }
    header { max-width: 700px; margin-bottom: 28px; }
    .eyebrow { color: var(--earth); font-size: .78rem; font-weight: 750; letter-spacing: .13em; text-transform: uppercase; }
    h1 { margin: 8px 0 12px; font-size: clamp(2rem, 6vw, 3.5rem); line-height: 1.08; letter-spacing: -.035em; }
    p { margin: 0 0 14px; color: var(--muted); }
    .panel {
      background: color-mix(in srgb, var(--panel) 92%, transparent);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: clamp(20px, 4vw, 32px);
      box-shadow: 0 18px 55px #0003;
    }
    .control { margin-bottom: 24px; }
    .control-top { display: flex; justify-content: space-between; gap: 16px; align-items: baseline; }
    label { font-weight: 700; }
    output { color: var(--earth); font-size: 1.25rem; font-weight: 800; font-variant-numeric: tabular-nums; }
    input[type="range"] { display: block; width: 100%; margin: 14px 0 4px; accent-color: var(--earth); cursor: pointer; }
    .range-labels { display: flex; justify-content: space-between; color: var(--muted); font-size: .82rem; }
    :focus-visible { outline: 3px solid #fff; outline-offset: 4px; border-radius: 4px; }
    .timeline { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
    .event { min-height: 150px; padding: 18px; border: 1px solid var(--line); border-radius: 14px; background: #111a27; }
    .event .step { color: var(--muted); font-size: .75rem; font-weight: 750; letter-spacing: .1em; text-transform: uppercase; }
    .event h2 { margin: 10px 0 2px; font-size: 1rem; }
    .event .time { display: block; margin: 4px 0 7px; font-size: clamp(1.4rem, 4vw, 2rem); font-weight: 850; line-height: 1.15; font-variant-numeric: tabular-nums; }
    .earth-event .time { color: var(--earth); }
    .rover-event .time { color: var(--rover); }
    .reply-event .time { color: var(--reply); }
    .event p { margin: 0; font-size: .9rem; }
    .explain { margin-top: 22px; padding: 18px 20px; border-left: 3px solid var(--rover); background: #111a27; border-radius: 0 12px 12px 0; }
    .explain strong { color: var(--ink); }
    .explain p:last-child { margin-bottom: 0; }
    .note { margin-top: 20px; font-size: .88rem; }
    noscript .noscript-note { margin-top: 22px; padding: 14px 16px; border: 1px solid var(--line); border-radius: 12px; color: var(--muted); }
    @media (max-width: 650px) {
      main { padding-top: 32px; }
      .timeline { grid-template-columns: 1fr; }
      .event { min-height: 0; }
    }
  </style>
</head>
<body>
  <main>
    <header>
      <div class="eyebrow">A deep-space thought experiment</div>
      <h1>A conversation with Perseverance</h1>
      <p>Talking to a rover on Mars takes patience. NASA reports that a one-way signal between Earth and Mars can take about 3 to 22 minutes, depending on where the planets are in their orbits.</p>
      <p>Explore a hypothetical exchange: Earth sends a message at minute 0. After receiving it, Perseverance takes 10 minutes to prepare a reply. The rover can begin transmitting only at minutes 25, 50, 75, and so on.</p>
    </header>

    <section class="panel" aria-label="Signal delay explorer">
      <div class="control">
        <div class="control-top">
          <label for="delay">One-way signal delay</label>
          <output id="delay-value" for="delay">15 minutes</output>
        </div>
        <input id="delay" type="range" min="3" max="22" step="1" value="15"
               aria-label="One-way signal delay in whole minutes">
        <div class="range-labels" aria-hidden="true"><span>3 min</span><span>22 min</span></div>
      </div>

      <div class="timeline" aria-live="polite" aria-atomic="true">
        <article class="event earth-event">
          <div class="step">1 · Earth sends</div>
          <h2>Message leaves Earth</h2>
          <span class="time">Minute 0</span>
          <p>The outgoing signal begins its journey.</p>
        </article>
        <article class="event rover-event">
          <div class="step">2 · Rover prepares</div>
          <h2>Reply is ready</h2>
          <span class="time" id="ready-time">Minute 25</span>
          <p id="ready-detail">The message arrives at minute 15; preparation takes 10 minutes.</p>
        </article>
        <article class="event reply-event">
          <div class="step">3 · Earth receives</div>
          <h2>Reply reaches Earth</h2>
          <span class="time" id="receive-time">Minute 40</span>
          <p id="transmit-detail">The rover transmits at minute 25; the return signal takes 15 minutes.</p>
        </article>
      </div>

      <div class="explain">
        <p><strong>Why does 15 → 16 minutes cause a jump?</strong> At a 15-minute delay, the message arrives at minute 15 and the reply is ready at minute 25—exactly a transmission slot. At 16 minutes, it arrives at 16 and is ready at 26, just after that slot. The rover must wait for the next one, minute 50. Earth then receives the reply at minute 66 instead of minute 40.</p>
        <p>In general, the rover transmits at the first 25-minute slot at or after it is ready. The return leg takes the same time as the outgoing leg.</p>
      </div>

      <p class="note">This schedule is hypothetical, designed to show how communication timing can work. It is not a description of Perseverance’s actual operating schedule.</p>

      <noscript>
        <p class="noscript-note">The initial example uses a 15-minute one-way delay: the rover receives the message at minute 15, is ready at minute 25, transmits at minute 25, and Earth receives the reply at minute 40. The slider needs JavaScript to update these times.</p>
      </noscript>
    </section>
  </main>

  <script>
    (() => {
      const slider = document.getElementById("delay");
      const value = document.getElementById("delay-value");
      const readyTime = document.getElementById("ready-time");
      const readyDetail = document.getElementById("ready-detail");
      const receiveTime = document.getElementById("receive-time");
      const transmitDetail = document.getElementById("transmit-detail");

      function update() {
        const delay = Number(slider.value);
        const ready = delay + 10;
        const transmit = Math.ceil(ready / 25) * 25;
        const received = transmit + delay;

        value.textContent = `${delay} minutes`;
        readyTime.textContent = `Minute ${ready}`;
        readyDetail.textContent =
          `The message arrives at minute ${delay}; preparation takes 10 minutes.`;
        receiveTime.textContent = `Minute ${received}`;
        transmitDetail.textContent =
          `The rover transmits at minute ${transmit}; the return signal takes ${delay} minutes.`;
      }

      slider.addEventListener("input", update);
      update();
    })();
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
  <title>Perseverance: a reply across the delay</title>
  <style>
    :root {
      color-scheme: light;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: #1c2630;
      background: #f4f1e9;
    }
    * { box-sizing: border-box; }
    body { margin: 0; padding: 2rem 1rem; }
    main { width: min(760px, 100%); margin: 0 auto; }
    header { margin-bottom: 1.5rem; }
    .eyebrow {
      margin: 0 0 .5rem;
      color: #8b442e;
      font-size: .8rem;
      font-weight: 750;
      letter-spacing: .12em;
      text-transform: uppercase;
    }
    h1 { margin: 0; font-size: clamp(2rem, 7vw, 3.6rem); line-height: 1.04; }
    .intro { max-width: 62ch; color: #47525b; line-height: 1.6; }
    .card {
      background: #fffefa;
      border: 1px solid #ded9cc;
      border-radius: 18px;
      padding: clamp(1.2rem, 4vw, 2rem);
      box-shadow: 0 12px 34px #332b1b0d;
    }
    .hypothesis {
      display: inline-block;
      border-radius: 999px;
      background: #f4e8d8;
      color: #743c27;
      padding: .35rem .7rem;
      font-size: .8rem;
      font-weight: 700;
    }
    .control { margin: 1.5rem 0 1rem; }
    label { display: flex; justify-content: space-between; gap: 1rem; font-weight: 700; }
    output { color: #8b442e; font-variant-numeric: tabular-nums; }
    input[type="range"] { width: 100%; margin: 1rem 0 .35rem; accent-color: #a14e32; }
    .range-ends { display: flex; justify-content: space-between; color: #657078; font-size: .85rem; }
    .timeline {
      display: grid;
      grid-template-columns: 1fr auto 1fr auto 1fr auto 1fr;
      align-items: center;
      gap: .45rem;
      margin: 1.5rem 0;
    }
    .event {
      min-width: 0;
      min-height: 105px;
      padding: .8rem .65rem;
      border-radius: 12px;
      background: #f3f0e8;
    }
    .event strong { display: block; margin-top: .55rem; font-size: 1.2rem; font-variant-numeric: tabular-nums; }
    .event span { color: #58636b; font-size: .8rem; line-height: 1.3; }
    .arrow { color: #a14e32; font-size: 1.2rem; font-weight: 800; }
    .answer {
      border-left: 4px solid #a14e32;
      padding: .2rem 0 .2rem 1rem;
      line-height: 1.55;
    }
    .answer p { margin: .35rem 0; }
    .note { color: #58636b; font-size: .9rem; line-height: 1.55; }
    .slots { overflow-wrap: anywhere; }
    @media (max-width: 560px) {
      body { padding: 1rem .7rem; }
      .timeline { grid-template-columns: 1fr; gap: .4rem; }
      .event { min-height: auto; display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; }
      .event strong { margin: 0; }
      .arrow { text-align: center; transform: rotate(90deg); }
      label { align-items: baseline; }
    }
  </style>
</head>
<body>
  <main>
    <header>
      <p class="eyebrow">A round trip to Mars</p>
      <h1>When does Perseverance reply?</h1>
      <p class="intro">Radio messages take time to cross the distance between Earth and Mars. NASA reports a one-way signal delay of about 3 to 22 minutes. See how that delay interacts with the rover’s preparation time and its scheduled transmission windows.</p>
    </header>

    <section class="card" aria-labelledby="exhibit-title">
      <h2 id="exhibit-title" class="hypothesis">Hypothetical contact schedule</h2>
      <p class="note">Earth sends a message at minute 0. After receiving it, the rover needs 10 minutes to prepare a reply. It may begin transmitting only at minutes 25, 50, 75, and every 25 minutes after that. A reply ready exactly at a slot can use it. Both signal legs have the same delay.</p>

      <div class="control">
        <label for="delay">One-way signal delay <output id="delay-value" for="delay">15 minutes</output></label>
        <input id="delay" type="range" min="3" max="22" step="1" value="15">
        <div class="range-ends" aria-hidden="true"><span>3 min</span><span>22 min</span></div>
      </div>

      <div class="timeline" aria-label="Reply timeline">
        <div class="event"><span>Earth transmits</span><strong id="sent">0 min</strong></div>
        <div class="arrow" aria-hidden="true">→</div>
        <div class="event"><span>Rover receives</span><strong id="received">15 min</strong></div>
        <div class="arrow" aria-hidden="true">→</div>
        <div class="event"><span>Reply ready</span><strong id="ready">25 min</strong></div>
        <div class="arrow" aria-hidden="true">→</div>
        <div class="event"><span>Rover transmits</span><strong id="transmit">25 min</strong><span id="slot-note">Uses the 25-minute slot</span></div>
      </div>
      <div class="event"><span>Earth receives reply</span><strong id="earth-reply">40 min</strong></div>

      <div class="answer" aria-live="polite" aria-atomic="true">
        <p id="summary">At a 15-minute one-way delay, the rover receives the message at minute 15 and is ready at minute 25. It can transmit at minute 25, so Earth receives the reply at minute 40.</p>
        <p id="explanation">The rover’s reply is ready exactly at a transmission slot, so it can use that slot.</p>
      </div>
      <p class="note slots">Transmission slots: <span id="slots">25, 50, 75, … minutes</span>.</p>
    </section>
  </main>

  <script>
    (() => {
      const slider = document.getElementById("delay");
      const value = document.getElementById("delay-value");
      const received = document.getElementById("received");
      const ready = document.getElementById("ready");
      const transmit = document.getElementById("transmit");
      const earthReply = document.getElementById("earth-reply");
      const slotNote = document.getElementById("slot-note");
      const summary = document.getElementById("summary");
      const explanation = document.getElementById("explanation");

      function update() {
        const delay = Number(slider.value);
        if (!Number.isInteger(delay) || delay < 3 || delay > 22) return;

        const arrival = delay;
        const preparationDone = arrival + 10;
        const slot = 25 * Math.ceil(preparationDone / 25);
        const replyArrival = slot + delay;

        value.value = `${delay} minutes`;
        value.textContent = `${delay} minutes`;
        received.textContent = `${arrival} min`;
        ready.textContent = `${preparationDone} min`;
        transmit.textContent = `${slot} min`;
        earthReply.textContent = `${replyArrival} min`;
        slotNote.textContent = preparationDone === slot
          ? `Uses the ${slot}-minute slot`
          : `Waits ${slot - preparationDone} min for the ${slot}-minute slot`;

        summary.textContent = `At a ${delay}-minute one-way delay, the rover receives the message at minute ${arrival} and is ready at minute ${preparationDone}. It transmits at minute ${slot}, so Earth receives the reply at minute ${replyArrival}.`;

        if (delay === 16) {
          explanation.textContent = "Increasing the delay from 15 to 16 moves readiness from minute 25 to minute 26. The rover just misses the 25-minute slot, so it must wait until minute 50; the extra minute of signal delay therefore adds 26 minutes to the round trip.";
        } else if (preparationDone === slot) {
          explanation.textContent = "The rover’s reply is ready exactly at a transmission slot, so it can use that slot.";
        } else {
          explanation.textContent = `The reply is ready after the previous slot, so the rover waits ${slot - preparationDone} minute${slot - preparationDone === 1 ? "" : "s"} for the next one.`;
        }
      }
      slider.addEventListener("input", update);
    })();
  </script>
</body>
</html>
````

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| At the initial 15-minute delay, the script-free page correctly shows ready at 25, transmit at 25 and received on Earth at 40 minutes, and marks the contact schedule as hypothetical. | Met | Met |
| For a 16-minute delay the page shows 26, 50 and 66; it explains the missed contact slot rather than treating every extra minute as a proportional change. | Met | Met |
| A labeled keyboard-operable control covers 3–22 whole minutes; the displayed Earth receipt updates to 28 at 3 and 72 at 22 without external resources. | Met | Met |

Both pages pass the browser checks: the initial 15-minute delay gives readiness/transmission/receipt at 25/25/40, and 16 gives 26/50/66. The skill answer explains the missed contact when the visitor moves to 16. The baseline presents the 15-to-16 comparison in static text, so that particular explanation remains available with scripts disabled. Both distinguish the model schedule from NASA’s signal-delay range.

**차이.** 두 페이지 모두 편도 15분일 때 준비·송신·수신이 25·25·40분, 16분일 때 26·50·66분이 되는 경계를 정확히 구현합니다. 스킬 답은 16으로 움직였을 때 놓친 연락 기회를 설명하고, 미적용 답은 같은 비교를 본문에 두어 JavaScript가 꺼져도 이유를 읽을 수 있습니다.

In Chromium 156.0.8078.80 both pages showed ready/transmit/receive times of 25/25/40 with JavaScript disabled. On the keyboard, delays of 16, 3 and 22 produced 26/50/66, 13/25/28 and 32/50/72. Neither page made a network request, threw a script error or overflowed horizontally at 320 CSS pixels.
