# When one more minute of Mars delay costs a whole contact window

[한국어](standard.ko.md)

2026-11-09 · `answer-with-html` 0.1.8 · English · `gpt-6-luna`

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
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Communicating with Perseverance</title>
  <style>
    :root {
      color-scheme: light;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: #17212b;
      background: #f4f6f8;
    }
    * { box-sizing: border-box; }
    body { margin: 0; padding: 1.25rem; }
    main {
      width: min(100%, 42rem);
      margin: 0 auto;
      padding: clamp(1.1rem, 5vw, 2rem);
      background: #fff;
      border: 1px solid #d8e0e7;
      border-radius: 1rem;
      box-shadow: 0 0.5rem 1.5rem #17212b0d;
    }
    h1 { margin: 0 0 .5rem; font-size: clamp(1.5rem, 5vw, 2rem); line-height: 1.2; }
    p { line-height: 1.55; }
    .intro { margin-top: 0; color: #455462; }
    .assumptions {
      padding: .85rem 1rem;
      background: #f1f5f8;
      border-radius: .65rem;
    }
    label { display: block; margin: 1.35rem 0 .45rem; font-weight: 700; }
    input[type="range"] { width: 100%; accent-color: #176b87; }
    .range-labels {
      display: flex;
      justify-content: space-between;
      color: #536372;
      font-size: .9rem;
    }
    output {
      display: block;
      margin-top: 1.25rem;
      padding: 1rem;
      border-left: .3rem solid #176b87;
      background: #edf7fa;
      border-radius: .35rem;
      font-size: 1.08rem;
      font-weight: 650;
      line-height: 1.65;
      overflow-wrap: anywhere;
    }
    .explanation { margin-bottom: 0; color: #455462; }
    @media (max-width: 24rem) {
      body { padding: .6rem; }
      main { padding: 1rem; }
    }
  </style>
</head>
<body>
  <main>
    <h1>Communicating with Perseverance</h1>
    <p class="intro">A reply takes time to travel, be prepared, and wait for an available transmission slot.</p>

    <p class="assumptions"><strong>Hypothetical schedule:</strong> Earth transmits at minute 0. After receiving the signal, the rover needs 10 minutes to prepare its reply. It may begin transmitting at minutes 25, 50, 75, and so on. If it is ready exactly at a slot, it can use that slot. Both signal legs have the same one-way delay. NASA reports that the one-way signal delay is about 3 to 22 minutes.</p>

    <label for="delay">One-way signal delay: <span id="delay-value">15</span> minutes</label>
    <input id="delay" type="range" min="3" max="22" step="1" value="15" aria-describedby="range-hint">
    <div class="range-labels" id="range-hint"><span>3 minutes</span><span>22 minutes</span></div>

    <output id="result" aria-live="polite">Rover receives Earth’s signal at minute 15 · Reply ready at minute 25 · Rover transmits at minute 25 · Earth receives reply at minute 40</output>

    <p class="explanation">The rover’s preparation ends 10 minutes after it receives the signal. The transmission time is the first available 25-minute slot at or after that ready time. From a 15-minute delay, the rover is ready exactly at minute 25 and can transmit then. Increasing the delay to 16 moves readiness to minute 26, just past that slot, so the rover waits for the next one. Earth then receives the reply after the same one-way signal delay.</p>
  </main>

  <script>
    (() => {
      const slider = document.getElementById("delay");
      const delayValue = document.getElementById("delay-value");
      const result = document.getElementById("result");

      function calculate(rawValue) {
        const parsed = Number(rawValue);
        const delay = Number.isFinite(parsed)
          ? Math.min(22, Math.max(3, Math.round(parsed)))
          : 15;
        const ready = delay + 10;
        const transmit = Math.ceil(ready / 25) * 25;
        const earthReceives = transmit + delay;
        return { delay, ready, transmit, earthReceives };
      }

      function render() {
        const values = calculate(slider.value);
        delayValue.textContent = String(values.delay);
        result.textContent =
          `Rover receives Earth’s signal at minute ${values.delay} · ` +
          `Reply ready at minute ${values.ready} · ` +
          `Rover transmits at minute ${values.transmit} · ` +
          `Earth receives reply at minute ${values.earthReceives}`;
      }

      slider.addEventListener("input", render);
      render();
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

**Review.** Browser replay checks the script-free initial values (25/25/40), the missed slot at 16 minutes (26/50/66) and both keyboard endpoints. The timing explanation agrees with the display.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/answer-with-html/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/answer-with-html.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `318335a72a76` / `0c1e69b04eac` / `8ef4267b1104`.

</details>
