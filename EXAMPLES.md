# Writing skills in English: 22 independent comparisons

[한국어 예제](EXAMPLES.ko.md)

Start with a question about [independent DNS caches](#feynman-technique), [a Mars rover that misses a contact slot](#answer-with-html), or [Seoul’s redesigned subway map](#hunminjeongeum). For every method, compare the baseline and standard answers to the same English request and see the three checks.

## How to read the evidence

Each method has one English request and three checks. The Korean gallery uses its own request and answers for the same case. For the November 9 repairs, we kept the November 8 baseline answers, questions and rubric wording. We revised the 13 methods that missed a standard check in either language, testing both languages again after each revision.

All 66 English standard checks are met on the displayed answers. Compared with the controls, **11** English standard answers meet more checks and **11** tie. Nine unchanged profiles keep their November 8 runs. Each revised method also has a different transfer problem. The record contains every accepted attempt, including earlier failures and cases where direct inspection overruled a masked grade. These development results describe the published questions. [Run details and raw records](evals/runs/2026-11-09-standard/README.md) · [November 8 English gallery](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/EXAMPLES.md).

Both conditions used GPT-6 Luna at low reasoning effort in independent read-only sessions. The writer saw only its own language’s request and, for standard, the selected method. Some answers visibly identify their method. English and Korean were generated separately, including mixed-language editing tasks.

Edit `skills/<id>/examples/standard.md` (English) or `standard.ko.md` (Korean) and run `python3 scripts/build_example_gallery.py` to rebuild both galleries.

<!-- Standard examples below are generated. -->

- [amazon-six-page-narrative](#amazon-six-page-narrative) · [portable example](skills/amazon-six-page-narrative/examples/standard.md) · [한국어](EXAMPLES.ko.md#amazon-six-page-narrative)
- [answer-with-html](#answer-with-html) · [portable example](skills/answer-with-html/examples/standard.md) · [한국어](EXAMPLES.ko.md#answer-with-html)
- [aristotle-syllogism](#aristotle-syllogism) · [portable example](skills/aristotle-syllogism/examples/standard.md) · [한국어](EXAMPLES.ko.md#aristotle-syllogism)
- [asd-ste100](#asd-ste100) · [portable example](skills/asd-ste100/examples/standard.md) · [한국어](EXAMPLES.ko.md#asd-ste100)
- [boring-professor](#boring-professor) · [portable example](skills/boring-professor/examples/standard.md) · [한국어](EXAMPLES.ko.md#boring-professor)
- [diataxis](#diataxis) · [portable example](skills/diataxis/examples/standard.md) · [한국어](EXAMPLES.ko.md#diataxis)
- [eli5](#eli5) · [portable example](skills/eli5/examples/standard.md) · [한국어](EXAMPLES.ko.md#eli5)
- [federal-plain-language](#federal-plain-language) · [portable example](skills/federal-plain-language/examples/standard.md) · [한국어](EXAMPLES.ko.md#federal-plain-language)
- [feynman-technique](#feynman-technique) · [portable example](skills/feynman-technique/examples/standard.md) · [한국어](EXAMPLES.ko.md#feynman-technique)
- [google-design-doc](#google-design-doc) · [portable example](skills/google-design-doc/examples/standard.md) · [한국어](EXAMPLES.ko.md#google-design-doc)
- [gtm-formal](#gtm-formal) · [portable example](skills/gtm-formal/examples/standard.md) · [한국어](EXAMPLES.ko.md#gtm-formal)
- [hunminjeongeum](#hunminjeongeum) · [portable example](skills/hunminjeongeum/examples/standard.md) · [한국어](EXAMPLES.ko.md#hunminjeongeum)
- [ietf-rfc](#ietf-rfc) · [portable example](skills/ietf-rfc/examples/standard.md) · [한국어](EXAMPLES.ko.md#ietf-rfc)
- [imrad](#imrad) · [portable example](skills/imrad/examples/standard.md) · [한국어](EXAMPLES.ko.md#imrad)
- [korean-plain-language](#korean-plain-language) · [portable example](skills/korean-plain-language/examples/standard.md) · [한국어](EXAMPLES.ko.md#korean-plain-language)
- [microsoft-writing-style](#microsoft-writing-style) · [portable example](skills/microsoft-writing-style/examples/standard.md) · [한국어](EXAMPLES.ko.md#microsoft-writing-style)
- [minto-pyramid](#minto-pyramid) · [portable example](skills/minto-pyramid/examples/standard.md) · [한국어](EXAMPLES.ko.md#minto-pyramid)
- [new-harts-rules](#new-harts-rules) · [portable example](skills/new-harts-rules/examples/standard.md) · [한국어](EXAMPLES.ko.md#new-harts-rules)
- [nist-technical-publication](#nist-technical-publication) · [portable example](skills/nist-technical-publication/examples/standard.md) · [한국어](EXAMPLES.ko.md#nist-technical-publication)
- [orwell-six-rules](#orwell-six-rules) · [portable example](skills/orwell-six-rules/examples/standard.md) · [한국어](EXAMPLES.ko.md#orwell-six-rules)
- [socratic-self-questioning](#socratic-self-questioning) · [portable example](skills/socratic-self-questioning/examples/standard.md) · [한국어](EXAMPLES.ko.md#socratic-self-questioning)
- [steve-jobs-presentation](#steve-jobs-presentation) · [portable example](skills/steve-jobs-presentation/examples/standard.md) · [한국어](EXAMPLES.ko.md#steve-jobs-presentation)

## amazon-six-page-narrative

**Which bridge review should happen before proposed stockpiling?**

[한국어](EXAMPLES.ko.md#amazon-six-page-narrative)

2026-11-08 · `amazon-six-page-narrative` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [NTSB, investigation HWY07MH024, Collapse of I-35W Highway Bridge, Minneapolis, Minnesota](https://www.ntsb.gov/investigations/Pages/HWY07MH024.aspx). What Happened and What We Found: 1 August 2007 collapse, inadequate U10 gusset plate capacity, combined loads, and omission of gusset plates from load-rating analyses. The proposed review by another owner is an exercise.

### Prompt

> Write one concise opening paragraph of a decision memo in English for a hypothetical owner considering material stockpiles on two truss bridges. At Minneapolis's I-35W bridge, NTSB found that undersized U10 gusset plates failed under combined loads from modifications, traffic and concentrated construction loads; load ratings had omitted the plates. This is a separate classroom screen, not actual ratings. For River Street, estimated plate capacity is 100 screening units and simultaneous loads are 68 existing + 18 deck modifications + 24 proposed construction. At Canal Street the corresponding loads are 66 + 14 + 15 and plate capacity is unknown. Visual inspections found no new visible damage. There is funding for one immediate load-rating review and neither site has a final engineering assessment. Choose the review priority, identify what to do about planned stockpiles at each site, and give leadership the reason.

### Without the skill

> Prioritize an immediate load-rating review of River Street: its estimated 100-unit plate capacity is exceeded by the simultaneous screening loads of 110 units, while Canal Street’s plate capacity is unknown despite a lower estimated combined load of 95 units. Defer River Street’s planned stockpiles until engineering review; at Canal Street, do not treat the lower screening total or clean visual inspection as proof of capacity—defer stockpiling pending an assessment or verified rating. This conservative approach reflects the I-35W finding that omitted gusset plates can govern under combined modification, traffic, and concentrated construction loads; neither site has a final engineering assessment.

### With the skill at standard

> Prioritize the immediate load-rating review for River Street: its estimated simultaneous load is 110 screening units (68 existing + 18 from deck modifications + 24 proposed construction) against an estimated plate capacity of 100. Until a final engineering assessment, defer the planned stockpile there; at Canal Street, where the corresponding load is 95 units but plate capacity is unknown, do not place the planned stockpile until a load rating establishes capacity. The I-35W investigation shows why gusset plates and combined, concentrated loads matter: ratings had omitted undersized plates that failed under combined loads. That case informs this separate classroom screen but does not establish either bridge’s actual capacity; no new visible damage does not resolve the uncertainty.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses the River Street figures to show combined demand 110 against estimated capacity 100 and gives it priority for the immediate review (or explicitly justifies a different priority while addressing that exceedance). | Met | Met |
| Uses Canal Street's 95-unit demand and missing capacity to leave its safety unresolved; does not clear either stockpile solely from a visual inspection. | Met | Met |
| The memo makes a concrete stockpiling decision for both sites and connects it to NTSB's plate/combined-load finding without declaring either real bridge unsafe. | Met | Met |

**Masked review** (X = baseline; Y = standard). Both defer both stockpiles and direct the immediate review to River Street: combined demand is 110 against an estimated 100, while Canal Street's demand is 95 and its capacity is unknown. Both connect the decision to the omitted gusset plates. X states the combined totals compactly; Y exposes River Street's three addends and explicitly labels the exercise.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `e75c268d420b` / `b036584868d4` / `19a6ebb19adb`.

</details>

## answer-with-html

**When one more minute of Mars delay costs a whole contact window**

[한국어](EXAMPLES.ko.md#answer-with-html)

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

## aristotle-syllogism

**Can new moon and central alignment alone establish a total solar eclipse?**

[한국어](EXAMPLES.ko.md#aristotle-syllogism)

2026-11-08 · `aristotle-syllogism` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [NASA, Why Do Eclipses Happen?](https://science.nasa.gov/eclipses/geometry/). Geometry, total and annular sections: solar eclipses occur at new moon; totality requires complete coverage, whereas an annular eclipse leaves a ring.
- [NASA, 2023 Annular Eclipse FAQ](https://science.nasa.gov/eclipses/future-eclipses/eclipse-2023/faq/). Eclipse science and the October 14, 2023 path of annularity identify the dated counterexample.

### Prompt

> A planetarium visitor reasons: 'Every total solar eclipse occurs at new moon; this is a new moon, so it is total.' They also argue that if it were not new moon, there could not be a total solar eclipse. Assess the two inferences separately. For a separate illustrative drawing, suppose an observer sees the two disks exactly centered, the Sun has angular diameter 0.53° and the Moon 0.50°. Calculate the angular width of the exposed rim on one side and infer what the observer would see. Then consider a centered 0.55° Moon instead. Use the actual annular solar eclipse of 14 October 2023 as a factual check, without attributing these invented diameters to it. Keep the answer concise enough to read beside the diagram. Write the answer in English.

### Without the skill

> The first inference reverses the implication: a total solar eclipse occurs at new moon, but a new moon does not guarantee a total eclipse. The Sun and Moon must also align closely, and the Moon must appear large enough to cover the Sun. The second inference is correct: without a new moon, there is no solar eclipse, total or otherwise.
>
> For the centered disks in the drawing, the 0.53° Sun exceeds the 0.50° Moon by 0.03°, leaving an exposed rim **0.015° wide on each side**. The observer would see an **annular eclipse**: a bright ring of sunlight around the Moon. With a centered 0.55° Moon, the Moon is larger than the Sun and would fully cover it, producing a **total eclipse**.
>
> As a factual check, the eclipse of 14 October 2023 was annular along its path: the Moon appeared too small to cover the Sun completely. The drawing’s invented diameters illustrate the geometry; they are not measurements from that eclipse.

### With the skill at standard

> ### The two inferences
>
> 1. **“Every total solar eclipse occurs at new moon; this is a new moon, so it is total.”**\
>    Premise: All total solar eclipses occur at new moon.\
>    Premise: This is a new moon.\
>    Conclusion: This is a total solar eclipse.
>
>    The conclusion does not follow: the first premise says total eclipses require a new moon, not that every new moon has a total eclipse. A new moon alone does not establish that the Moon is aligned with the Sun or appears large enough to cover it. The stated premise is a necessary condition, not a sufficient one.
>
> 2. **“If it were not new moon, there could not be a total solar eclipse.”**\
>    This is a valid restatement of the first premise: a total solar eclipse entails a new moon. It does not establish that any particular new moon produces a total eclipse. These are logical assessments; the premises’ factual support is separate.
>
> ### Disk drawing
>
> With the disks exactly centered, the 0.53° Sun and 0.50° Moon differ by 0.03° in diameter. The exposed rim on **one side** is half that difference: **0.015°**. In this simplified drawing, sunlight remains visible all around the Moon’s edge: an annular, “ring of fire” appearance.
>
> With a centered 0.55° Moon, the Moon is 0.02° wider than the Sun. It covers the Sun’s disk in the drawing, giving a total-eclipse appearance.
>
> These are illustrative angular diameters, not measurements of the 14 October 2023 eclipse. That event was an **annular solar eclipse**; the Moon did not completely cover the Sun along the path of annularity. The drawing’s exact centering and diameters are assumptions for the illustration, not claims about that event.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Explains that new moon is necessary but insufficient, rejects the converse, and accepts the contrapositive about a non-new moon. | Met | Met |
| Computes the one-sided rim as (0.53−0.50)/2 = 0.015°, leading to a ring; with the centered 0.55° Moon the solar disk is fully covered at that observer. | Met | Met |
| Uses the 14 October 2023 annular eclipse as a real counterexample without presenting the classroom drawing’s diameters as measured historical values. | Met | Met |

**Masked review** (Y = baseline; X = standard). Both reject the converse, accept the contrapositive and find the 0.015° rim; both distinguish the classroom geometry from the October 2023 eclipse. X separates premises, conclusion and drawing into sections. Y reaches the same results in fewer words, which better fits a diagram label.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `d69f028ec500` / `12e925d97f7e` / `ab6d3996f923`.

</details>

## asd-ste100

**When can each Raspberry Pi 4 recovery station be powered down?**

[한국어](EXAMPLES.ko.md#asd-ste100)

2026-11-09 · `asd-ste100` 0.1.4 · English · `gpt-6-luna`

### Case and sources

- [Raspberry Pi, Raspberry Pi computer hardware documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#reflash-the-bootloader). Reflash the bootloader, especially the last step for an HDMI-connected board. The prompt covers only completion of a prepared recovery on the Pi 4 Model B.

**Language scope.** This English handover uses the project’s STE-inspired standard profile. It does not verify official ASD-STE100 compliance.

### Prompt

> Write a concise English handover for technicians finishing a Raspberry Pi 4 Model B bootloader recovery with HDMI displays attached. Before disconnecting power they must observe both a steady flashing pattern on the green activity LED and a green HDMI screen. Remove the recovery microSD card only after power is disconnected. In this illustrative bench drill, staff check each board at 0, 15, 30, 45 and 60 seconds. Once an indication appears it persists. At North the LED pattern starts at 16 s and the HDMI screen turns green at 29 s. At South the screen turns green at 33 s and the LED pattern starts at 41 s. At East the LED pattern starts at 21 s and the screen is still not green at 60 s. No power has yet been disconnected. Give the first qualifying check for each station and the safe action there. Explain whether the elapsed time alone can authorize removal. Use one consistent name for the recovery microSD card.

### Without the skill

> **Bench drill handover — Raspberry Pi 4 Model B**
>
> Keep power connected until both the steady flashing green activity LED pattern and a green HDMI screen are visible. Then disconnect power before removing the recovery microSD card.
>
> | Station | First check showing both indications | Safe action |
> |---|---:|---|
> | North | 30 s | Disconnect power, then remove the recovery microSD card. |
> | South | 45 s | Disconnect power, then remove the recovery microSD card. |
> | East | None by 60 s | Keep power connected; do not remove the card. |
>
> Elapsed time alone does not authorize removal. At each check, confirm both indications are present; if either is absent, keep power connected and continue checking.

### With the skill at standard

> ## Bootloader recovery handover
>
> Keep the HDMI displays attached. At each check, observe both the steady flashing pattern on the green activity LED and a green HDMI screen. Disconnect power only after both indications are present. Remove the recovery microSD card only after power is disconnected.
>
> | Station | First check with both indications | Safe action |
> |---|---:|---|
> | North | 30 seconds | Disconnect power, then remove the recovery microSD card. |
> | South | 45 seconds | Disconnect power, then remove the recovery microSD card. |
> | East | None by 60 seconds | Keep power connected and the recovery microSD card installed. |
>
> Elapsed time alone does not authorize removal. At East, the HDMI screen is still not green at 60 seconds, so both required indications are not present.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Derives North’s first qualifying check as 30 s and South’s as 45 s, using observation times rather than the raw times at which indicators changed. | Met | Met |
| For East at 60 s, withholds disconnect/removal and does not imply that a fixed timeout proves success or establishes hardware failure. | Met | Met |
| States the correct sequence in technician-usable English: observe both signals, disconnect power, then remove the recovery microSD card; calls the card consistently by the same name. | Missed | Met |

**Review.** North qualifies at 30 seconds and South at 45. East stays powered with the recovery microSD card in place. The handover uses the required component name throughout.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/asd-ste100/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/asd-ste100.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `441382171a3a` / `9f618db8c88e` / `aba6aa20f2e6`.

</details>

## boring-professor

**Tracking two Linux log files behind the same pathname**

[한국어](EXAMPLES.ko.md#boring-professor)

2026-11-08 · `boring-professor` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [Linux man-pages 6.19, unlink(2)](https://man7.org/linux/man-pages/man2/unlink.2.html). DESCRIPTION defines the effect of unlinking the last directory link with and without an open descriptor. The filenames, monitor, allocation sizes and event times are illustrative.

### Prompt

> Explain this Linux drill to a systems student. At 09:00 an administrator unlinks the last hard link to /var/log/payments.log. The old file has 20 MiB of allocated data; the writer and a monitor each hold an open descriptor to it. At 09:02 the service creates a separate file at the same pathname, with 5 MiB allocated. At 09:03 the original writer appends 8 MiB through its old descriptor, then closes it at 09:04. The monitor closes its old descriptor at 09:06. Trace which file gets the append, the total allocated data across both files just after 09:04 and just after 09:06, and why the pathname alone is insufficient evidence. Assume no sparse allocation, duplication or other changes; ignore metadata. Keep the explanation literal and concise. Write your answer in English.

### Without the skill

> At 09:00, unlinking the last hard link removes the old file’s name, but the open descriptors keep that file alive. At 09:02, the service creates a new, separate file at `/var/log/payments.log`.
>
> The writer’s append at 09:03 goes to the **old file**, because its descriptor still refers to that file. The old file then has 20 + 8 = **28 MiB** allocated; the new file has **5 MiB**. Total just after 09:04: **33 MiB**.
>
> Closing the writer’s descriptor does not free the old file because the monitor still has it open. When the monitor closes its descriptor at 09:06, the old file is released. The new file remains at **5 MiB**. Total just after 09:06: **5 MiB**.
>
> The pathname alone is insufficient evidence because it names the new file after 09:02. An open descriptor can still refer to the old, unlinked file.

### With the skill at standard

> `unlink` removes a directory entry. An open file descriptor continues to refer to its file even after that file has no pathname.
>
> The 09:00 unlink removes the last hard link to the original file, but the writer’s and monitor’s descriptors keep it accessible. At 09:02, creating `/var/log/payments.log` creates a separate file; the pathname now refers to that file.
>
> The 09:03 append goes to the original file because the writer uses its old descriptor. Its allocated data becomes 20 + 8 = **28 MiB**. The new file remains **5 MiB**, so the total just after the writer closes at 09:04 is **33 MiB**.
>
> At 09:06, the monitor closes the last open descriptor to the original file. The original file is then released, leaving the new file’s **5 MiB** allocated. The total just after 09:06 is **5 MiB**.
>
> The pathname alone is insufficient evidence because, after 09:02, it identifies the new file, while the writer’s descriptor still identifies the unlinked original. These totals assume no sparse allocation, duplication, other changes, or metadata.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the append as going to the old, unlinked file through the writer's descriptor, not to the 5 MiB replacement at the reused pathname. | Met | Met |
| Gives 33 MiB just after 09:04 (28 old + 5 new) and 5 MiB just after 09:06; the monitor's descriptor delays release of the old file. | Met | Met |
| Explains the pathname/file-object distinction and the final-descriptor condition using literal technical terms, without implying that unlink disables existing writes. | Met | Met |

**Masked review** (Y = baseline; X = standard). Both identify the old object as the append target, compute 33 MiB at 09:04 and 5 MiB at 09:06, and connect delayed reclamation to the monitor’s descriptor. X defines a directory entry before tracing the events and restates the assumptions; Y gives a shorter event trace. No substantive difference on these checks.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `7920576bbe50` / `ae415a4a0b15` / `89fd5a38430b`.

</details>

## diataxis

**Which Kubernetes rollout did the green CI job actually observe?**

[한국어](EXAMPLES.ko.md#diataxis)

2026-11-08 · `diataxis` 0.1.1 · English · `gpt-6-luna`

### Case and sources

- [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/). Synopsis and flags document default revision tracking, --revision and --watch. checkout-api and revisions 7/8 are an illustrative release, not historical cluster telemetry.

### Prompt

> Write a short lookup entry for the release team using kubectl rollout status on Deployment checkout-api. CI starts watching revision 7 without flags at 09:00. Before 7 finishes, revision 8 starts; the command later reports success. A default watch follows the latest rollout across revisions; a watch pinned with --revision=N aborts if superseded, and --watch=false reads a snapshot without waiting. Explain what the green job does and does not establish about 7 and 8. Give the exact commands for a new CI job that must monitor revision 7 specifically and for an operator who wants the current status immediately. Assume 8 is the last revision during this example. Make this useful for lookup, not a tutorial. Write your answer in English.

### Without the skill

> ### `kubectl rollout status` — `checkout-api`
>
> At 09:00, CI runs `kubectl rollout status deployment/checkout-api` without flags while revision 7 is in progress. Revision 8 starts before 7 finishes, and the command later reports success. By default, the watch follows the latest rollout, so that green job establishes that **revision 8 completed**. It does **not** establish that revision 7 completed successfully.
>
> For a new CI job that must monitor revision 7 specifically, pin the watch:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> If revision 7 is superseded before the watch completes, the command aborts rather than switching to revision 8.
>
> For an immediate status snapshot without waiting:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```
>
> This reports the current rollout status; it does not establish that the rollout will finish successfully.

### With the skill at standard

> ## `kubectl rollout status` for `checkout-api`
>
> **Default behavior:** `kubectl rollout status deployment/checkout-api` follows the latest rollout. If revision 8 starts while the command is watching revision 7, the watch follows revision 8.
>
> In this example, the green CI job establishes that the latest rollout it followed—revision 8, assumed to be the last revision—completed successfully. It does **not** establish that revision 7 completed successfully: the command may have switched to watching revision 8 before 7 finished.
>
> | Need | Command | Behavior |
> |---|---|---|
> | CI job must monitor revision 7 specifically | `kubectl rollout status deployment/checkout-api --revision=7` | Watches revision 7; aborts if it is superseded. |
> | Operator wants the current status immediately | `kubectl rollout status deployment/checkout-api --watch=false` | Reads a snapshot and returns without waiting. |

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Attributes the successful default watch to latest revision 8 and says that its success does not establish success for revision 7. | Met | Met |
| Gives an executable kubectl rollout status command for deployment/checkout-api with --revision=7, and states that supersession causes the pinned watch to abort rather than follow 8. | Met | Met |
| Gives an executable command with --watch=false for a current snapshot, with purpose and commands easy to find in a compact lookup entry. | Met | Met |

**Masked review** (X = baseline; Y = standard). Both identify revision 8 as the successful rollout, give the two executable commands and explain why the unpinned watch cannot certify revision 7. X places the commands in separate code blocks and distinguishes a current snapshot from future success. Y groups each command and its behavior in a lookup table.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `1bf8f74acf77` / `80606212012a` / `67a7105766a3`.

</details>

## eli5

**Which model coat loses warmth faster, and what does that tell a child about pup 696?**

[한국어](EXAMPLES.ko.md#eli5)

2026-11-09 · `eli5` 0.1.18 · English · `gpt-6-luna`

### Case and sources

- [Monterey Bay Aquarium, Life of a rescued sea otter](https://www.montereybayaquarium.org/about-us/stories/life-of-a-rescued-sea-otter). Pup 696's rescue and grooming sections describe the role of air in the fur in warmth and buoyancy.
- [Monterey Bay Aquarium, Sea otter](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/sea-otter). Species account, Adaptations and Grooming: unlike many marine mammals, a sea otter relies on fur in cold water and lacks a thick layer of blubber.

### Prompt

> At Monterey Bay Aquarium, a five-year-old asks why caregivers groomed rescued sea otter pup 696. In a classroom demonstration invented for this question, two equally warm jars have identical model coats in the same cold bath. With air trapped in the fluffy coat, one jar cools 4 degrees in 20 minutes. With the coat wet and flat, the other cools 3 degrees in 10 minutes. A child says the fluffy jar lost warmth faster because four is more than three. Neither jar was tested for floating. Real sea otters lack thick blubber; grooming traps air in their fur, which helps them stay warm and float. Answer the child in at most five short sentences: use a fair comparison, explain whether air makes heat, and say what the jars can and cannot show about floating. Write the answer in English.

### Without the skill

> That comparison isn’t fair yet: the jars were measured for different lengths of time. Air doesn’t make heat; trapped air slows heat loss, so compare both coats over the same time. These jars can show how coats affect cooling, but they can’t tell us which coat floats better because floating wasn’t tested. Sea otters groom to trap air in their fur, which helps them stay warm and float.

### With the skill at standard

> The caregivers groomed pup 696 to help keep him warm.\
> The air trapped in his fluffy fur slows heat from escaping; it doesn’t make heat.\
> The flat wet coat cooled faster: on average, it lost 6 degrees in 20 minutes, while the fluffy coat lost 4.\
> The jars didn’t test floating.\
> In real sea otters, air trapped in their fur helps them float.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses an equal-time comparison to explain the apparent reversal (2 degrees versus 3 per 10 minutes, or equivalent rates) and identifies the fluffy coat as slower to cool on average. | Missed | Met |
| Connects grooming to trapped air keeping warmth from leaving as fast, without claiming that air creates heat or substituting an invented biological mechanism. | Met | Met |
| In at most five short child-facing sentences, separates the jars’ untested floating behavior from the fact that trapped air also helps real otters float. | Met | Met |

**Review.** The answer compares average losses of 6 and 4 degrees per 20 minutes (3 and 2 per 10). This rescales the wet jar’s 10-minute measurement. It tells the child why grooming matters, why air slows heat loss and why the jar test cannot establish buoyancy.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/eli5/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/eli5.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `fdd792c71803` / `b13daecf86ad` / `66f424b317e0`.

</details>

## federal-plain-language

**Which 40-minute document trip covers both identities?**

[한국어](EXAMPLES.ko.md#federal-plain-language)

2026-11-09 · `federal-plain-language` 0.1.22 · English · `gpt-6-luna`

### Case and sources

- [SSA, U.S. Citizen/Child — Replacement Social Security Card (October 2026)](https://www.ssa.gov/pubs/EN-05-10514.pdf). English page of the October 2026 U.S. citizen/child replacement-card leaflet, sections on the child's and parent's identity, current originals, issuer-certified copies and unacceptable copies. The family's options and collection times are hypothetical; the identification requirements come from the leaflet.

**Language scope.** This uses the method’s English public-information profile.

### Prompt

> A parent has 45 minutes to collect evidence for the identity part of a U.S.-citizen child's replacement Social Security card application. Write a parent-facing answer in English in no more than five sentences using the October 2026 SSA leaflet. Both people need identity evidence. The child can use a current U.S. passport or current state-issued non-driver ID. The parent can use a current U.S. passport or driver's license. SSA accepts originals or issuer-certified copies, not notarized photocopies; a birth certificate proves age or citizenship but not identity. Hypothetical collection times add: the child's original birth certificate is already in hand, original passport takes 40 minutes, and issuer-certified non-driver ID takes 15. For the parent, a notarized passport photocopy takes 5, an issuer-certified passport copy 25, and an original license 35. Which route fits? Point out why the tempting shortcut fails. Address identity evidence only.

### Without the skill

> Use the child’s issuer-certified state non-driver ID (15 minutes) and the parent’s issuer-certified U.S. passport copy (25 minutes): together they take 40 minutes. The tempting shortcut—a notarized photocopy of the parent’s passport—doesn’t count because SSA accepts originals or issuer-certified copies, not notarized photocopies. The child’s birth certificate proves age or citizenship, but not identity, so it cannot replace the child’s ID.

### With the skill at standard

> Use the child’s issuer-certified state non-driver ID (15 minutes) and the parent’s issuer-certified passport copy (25 minutes). Together they take 40 minutes, within the 45-minute limit. The notarized passport photocopy takes only 5 minutes, but SSA does not accept notarized photocopies as identity evidence. The birth certificate proves the child’s age or citizenship, not identity.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the child's issuer-certified non-driver ID plus the parent's issuer-certified passport copy, totals 40 minutes and fits the 45-minute limit. | Met | Met |
| Explains both rejected shortcuts: the original birth certificate is insufficient for the child's identity and the notarized copy is insufficient for the parent's identity. | Met | Met |
| Gives the parent an actionable English identity-only answer in no more than five sentences without implying the full application is complete. | Met | Met |

**Review.** The parent gets a feasible 40-minute plan and a reason to reject each shortcut. The answer stays within five sentences and addresses identity evidence only.

Masked reviewer assignment: Y was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/federal-plain-language/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/federal-plain-language.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `90ceac7f7264` / `cd08aed6cec9` / `68130696a7c4`.

</details>

## feynman-technique

**Why two DNS resolvers disagree after a record is created**

[한국어](EXAMPLES.ko.md#feynman-technique)

2026-11-09 · `feynman-technique` 0.1.8 · English · `gpt-6-luna`

### Case and sources

- [IETF RFC 2308, Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html#section-5). Sections 3 and 5 explain the SOA-based lifetime and expiry of negative responses. The hostname, TTL values and clock times are a worked trace, not production DNS records.

### Prompt

> Two teams query uploads.example.org through independent DNS resolvers. In this illustrative trace, Harbor gets NXDOMAIN at 12:00 and Hill gets NXDOMAIN at 12:03. Both cache the name's absence. The zone's SOA TTL is 900 seconds and its MINIMUM is 300 seconds; RFC 2308 uses the smaller value for a negative answer. At 12:04 the operator creates the A record. At 12:06 both teams query again. In a short incident explanation for a junior developer, predict what each team can see, when the later cache expires, and what would change if Hill had not queried before 12:04. Assume a reachable, updated authority; no evictions, refreshes or local overrides. Do not ask the developer a question. Write your answer in English.

### Without the skill

> Harbor and Hill can both still see `NXDOMAIN` at 12:06. Under RFC 2308, the negative cache lifetime is the smaller of the SOA TTL (900 seconds) and SOA MINIMUM (300 seconds), so each resolver can cache the absence for 300 seconds from its own NXDOMAIN response.
>
> Harbor’s entry expires at **12:05**, and Hill’s at **12:08**. At 12:06, Harbor’s cache has expired, so its next query can reach the updated authority and return the A record. Hill’s cache is still valid, so Hill can still receive NXDOMAIN until 12:08; after that, its next query can return the A record.
>
> If Hill had not queried before 12:04, it would have no cached negative answer. Its first query after the A record was created could reach the authority and return the A record immediately.

### With the skill at standard

> **Incident explanation (junior developer):** RFC 2308 sets the negative-cache lifetime to the smaller of the SOA TTL (900 seconds) and SOA MINIMUM (300 seconds), so each resolver can keep its own NXDOMAIN result for 300 seconds from when it received that answer. Harbor received NXDOMAIN at 12:00, so its entry expires at **12:05**. Hill received NXDOMAIN at 12:03, so its entry expires at **12:08**. The A record was created at 12:04, but that does not erase either resolver’s cached result. At 12:06, Harbor’s entry has expired and, with the authority reachable and updated, Harbor can see the A record; Hill’s entry is still valid, so Hill can still see NXDOMAIN until 12:08. If Hill had not queried before 12:04, it would have no negative entry to serve at 12:06 and could query the authority and see the A record. The two resolvers’ cache timers start independently when each receives NXDOMAIN.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 300-second lifetime and the 12:05 Harbor and 12:08 Hill expirations from their own original queries. | Met | Met |
| At 12:06 Harbor can fetch the new address while Hill can still serve NXDOMAIN; creating the record did not restart or invalidate Hill's cached lifetime. | Missed | Met |
| Explains for a junior developer why Hill with no earlier negative entry could fetch the new address at 12:06 under the stated assumptions, without implying a simultaneous global update. | Met | Met |

**Review.** The two expirations come from different first queries. At 12:06 only Hill can still reuse its negative entry; without that earlier query, Hill could fetch the new address.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/feynman-technique/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/feynman-technique.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `5527bddea967` / `dae944fee0be` / `e3260298686a`.

</details>

## google-design-doc

**Should PostgreSQL add the orders index during this shift?**

[한국어](EXAMPLES.ko.md#google-design-doc)

2026-11-08 · `google-design-doc` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [PostgreSQL 17 documentation, CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY). Building Indexes Concurrently explains locking, table scans, waiting for transactions and invalid indexes after failure. The store, schema and decision are illustrative; no production benchmark is quoted.
- [PostgreSQL 17 system catalogs, pg_index](https://www.postgresql.org/docs/17/catalog-pg-index.html). The indisvalid field records whether the index is valid for queries. The rehearsal metrics and release threshold are illustrative.

### Prompt

> Write a design-review excerpt for an illustrative PostgreSQL 17 store. The team cannot block order INSERTs throughout an index build. Its separate release gate is a rehearsal p95 write latency no more than 20% above the 40 ms baseline. A concurrent-build rehearsal measured 51 ms. Ordinary CREATE INDEX blocks writes; CREATE INDEX CONCURRENTLY lets writes continue, scans the table twice and can wait for transactions. A failed concurrent run can leave an invalid index that planners ignore but writes still maintain. Recommend what to authorize this shift, what to measure before retrying and how to handle an invalid result. The store has not measured production performance. Keep it concise. Write your answer in English.

### Without the skill

> ### Design-review excerpt
>
> Authorize a **concurrent index build**: order INSERTs must continue, and ordinary `CREATE INDEX` blocks writes. `CREATE INDEX CONCURRENTLY` keeps writes running, though it scans the table twice and may wait for transactions.
>
> The rehearsal result **fails the separate latency gate**: 51 ms is 27.5% above the 40 ms baseline, exceeding the 20% limit of 48 ms. Before retrying, measure rehearsal p95 write latency and identify the main contributors, including concurrent write load, transaction duration, and build-related resource use. Production performance is unmeasured, so do not treat the rehearsal as a production estimate.
>
> If a concurrent build fails, check whether it left an invalid index. Planners ignore it, but writes still maintain it; remove the invalid index before retrying, then verify the rebuilt index is valid.

### With the skill at standard

> ## Illustrative PostgreSQL 17 index build
>
> **Proposal for review.** Authorize `CREATE INDEX CONCURRENTLY` for the build, subject to the separate latency gate. The team cannot block order inserts throughout the build. The concurrent-build rehearsal measured 51 ms p95 against a 40 ms baseline: 27.5% higher, above the 20% limit of 48 ms. The rehearsal therefore does not pass the release gate. Production performance has not been measured.
>
> **Behavior and trade-offs.** An ordinary `CREATE INDEX` blocks writes, so it conflicts with the insert constraint. `CREATE INDEX CONCURRENTLY` lets writes continue, but scans the table twice and can wait for transactions. If it fails, it can leave an invalid index: planners ignore it, but writes still maintain it.
>
> **Before retrying.** Measure rehearsal p95 write latency under the same conditions as the 40 ms baseline, and identify what drove the 51 ms result. Retry only when the rehearsal meets the 48 ms limit; the current result does not authorize release.
>
> **Invalid result.** Check the index’s validity after a failed concurrent build. If invalid, account for its write-maintenance cost and remove it before retrying the build.
>
> **Status.** This is a proposal for review. No approval or production-performance evidence is provided.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 48 ms gate or the 27.5% increase and recognizes that the 51 ms concurrent rehearsal fails the allowed 20% increase. | Met | Met |
| Rejects an ordinary build during the shift because it blocks required INSERTs and holds the production rollout pending a passing new rehearsal; does not promise production latency. | Missed | Met |
| Gives a concrete review or recovery plan that checks validity and deals with an invalid index that still imposes write cost (for example, remove it and retry safely). | Met | Met |

**Masked review** (Y = baseline; X = standard). Both calculate a 48 ms ceiling and a 27.5% increase, explain why an ordinary build blocks required writes, and plan to inspect and remove an invalid index. X opens with conditional authorization and explicitly withholds production release until a new rehearsal passes. Y acknowledges the breach but opens by authorizing the concurrent build without limiting that authorization to rehearsal.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `96fbdfc6834c` / `22613968a7c4` / `7e00af2b235a`.

</details>

## gtm-formal

**When does a vote threshold exclude two Raft leaders?**

[한국어](EXAMPLES.ko.md#gtm-formal)

2026-11-08 · `gtm-formal` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm, §5.2](https://raft.github.io/raft.pdf). Section 5.2 and Figure 3 distinguish election safety, one vote per term, majority election and split votes.
- [etcd v3.5 FAQ, fault tolerance](https://etcd.io/docs/v3.5/faq/#what-is-failure-tolerance). The fault-tolerance table gives a quorum of three for five etcd members. The varied vote threshold is a mathematical exercise; real Raft uses a majority.

### Prompt

> In a formal note for a distributed-systems seminar, derive a necessary and sufficient inequality on a proposed election threshold q so that any two qualifying voter sets in a fixed cluster of n voters overlap (1 ≤ q ≤ n). Derive a lower bound for the number of voters shared by two qualifying sets in terms of n and q. Each voter grants at most one vote per term. Use the illustrative etcd-east and etcd-west candidates to connect the bound to election safety. Apply your result to normal majority voting with five voters and to a hypothetical threshold of three in a fixed six-voter cluster. Give a concrete six-voter counterexample if needed. Finally say what election safety alone implies about making progress when voters are unavailable. Keep it concise. Write your answer in English.

### Without the skill

> Let $A$ and $B$ be any two qualifying voter sets in a fixed cluster of $n$ voters, each containing at least $q$ voters, where $1\le q\le n$. Since $A\cup B$ has at most $n$ voters,
>
> $$
> |A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n.
> $$
>
> This bound is tight. Thus every two qualifying sets overlap **if and only if**
>
> $$
> 2q-n\ge1,\qquad\text{equivalently}\qquad q>\frac n2.
> $$
>
> When they overlap, they share at least $2q-n$ voters.
>
> For five voters, a majority threshold is $q=3$. Any two qualifying sets share at least $2(3)-5=1$ voter. If etcd-east and etcd-west each win an election using a majority, their voter sets therefore share a voter. Because each voter grants at most one vote per term, that shared voter cannot vote for both candidates in the same term; this prevents both candidates from winning that term.
>
> In a fixed six-voter cluster, threshold $q=3$ does not ensure overlap: the qualifying sets $\{1,2,3\}$ and $\{4,5,6\}$ are disjoint. A threshold of $q=4$ is needed to guarantee overlap, with at least $2(4)-6=2$ shared voters.
>
> Election safety alone does not guarantee progress: if too many voters are unavailable to form a qualifying set, no candidate can be elected.

<details>
<summary>Original math delimiters</summary>

````text
Let \(A\) and \(B\) be any two qualifying voter sets in a fixed cluster of \(n\) voters, each containing at least \(q\) voters, where \(1\le q\le n\). Since \(A\cup B\) has at most \(n\) voters,
\[
|A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n.
\]
This bound is tight. Thus every two qualifying sets overlap **if and only if**
\[
2q-n\ge1,\qquad\text{equivalently}\qquad q>\frac n2.
\]
When they overlap, they share at least \(2q-n\) voters.

For five voters, a majority threshold is \(q=3\). Any two qualifying sets share at least \(2(3)-5=1\) voter. If etcd-east and etcd-west each win an election using a majority, their voter sets therefore share a voter. Because each voter grants at most one vote per term, that shared voter cannot vote for both candidates in the same term; this prevents both candidates from winning that term.

In a fixed six-voter cluster, threshold \(q=3\) does not ensure overlap: the qualifying sets \(\{1,2,3\}\) and \(\{4,5,6\}\) are disjoint. A threshold of \(q=4\) is needed to guarantee overlap, with at least \(2(4)-6=2\) shared voters.

Election safety alone does not guarantee progress: if too many voters are unavailable to form a qualifying set, no candidate can be elected.
````

</details>

### With the skill at standard

> Fix a cluster of $n\ge 1$ voters. A qualifying set is a subset of at least $q$ voters, where $q$ is an integer with $1\le q\le n$. For any two qualifying sets $A,B\subseteq V$, inclusion–exclusion gives
>
> $$
> |A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n,
> $$
>
> since $|A\cup B|\le n$. Thus every pair overlaps if and only if
>
> $$
> \boxed{2q>n}\qquad\text{or, equivalently,}\qquad q>\frac n2.
> $$
>
> The bound on the overlap is $\max(0,2q-n)$. If $2q\le n$, two disjoint qualifying sets of size $q$ can be chosen, so overlap is not guaranteed.
>
> For example, with five voters, normal majority voting uses $q=3$. Any two qualifying sets share at least $2(3)-5=1$ voter. In a fixed six-voter cluster with hypothetical threshold $q=3$, the bound is zero: $\{\text{A},\text{B},\text{C}\}$ and $\{\text{D},\text{E},\text{F}\}$ are disjoint qualifying sets.
>
> Apply this to two candidates, etcd-east and etcd-west, each winning by collecting votes from a qualifying set. With a threshold satisfying $2q>n$, their voter sets intersect. Because each voter grants at most one vote per term, the shared voter cannot vote for both candidates in that term; hence both cannot win. With six voters and threshold three, disjoint winning sets are possible, so this overlap argument alone does not guarantee election safety.
>
> Election safety is a safety property: it rules out conflicting wins under its assumptions, but by itself guarantees no progress when voters are unavailable. Progress depends on whether enough voters remain available to form a qualifying set and on the election protocol’s other conditions.

<details>
<summary>Original math delimiters</summary>

````text
Fix a cluster of \(n\ge 1\) voters. A qualifying set is a subset of at least \(q\) voters, where \(q\) is an integer with \(1\le q\le n\). For any two qualifying sets \(A,B\subseteq V\), inclusion–exclusion gives
\[
|A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n,
\]
since \(|A\cup B|\le n\). Thus every pair overlaps if and only if
\[
\boxed{2q>n}\qquad\text{or, equivalently,}\qquad q>\frac n2.
\]
The bound on the overlap is \(\max(0,2q-n)\). If \(2q\le n\), two disjoint qualifying sets of size \(q\) can be chosen, so overlap is not guaranteed.

For example, with five voters, normal majority voting uses \(q=3\). Any two qualifying sets share at least \(2(3)-5=1\) voter. In a fixed six-voter cluster with hypothetical threshold \(q=3\), the bound is zero: \(\{\text{A},\text{B},\text{C}\}\) and \(\{\text{D},\text{E},\text{F}\}\) are disjoint qualifying sets.

Apply this to two candidates, etcd-east and etcd-west, each winning by collecting votes from a qualifying set. With a threshold satisfying \(2q>n\), their voter sets intersect. Because each voter grants at most one vote per term, the shared voter cannot vote for both candidates in that term; hence both cannot win. With six voters and threshold three, disjoint winning sets are possible, so this overlap argument alone does not guarantee election safety.

Election safety is a safety property: it rules out conflicting wins under its assumptions, but by itself guarantees no progress when voters are unavailable. Progress depends on whether enough voters remain available to form a qualifying set and on the election protocol’s other conditions.
````

</details>

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Proves the sufficient bound \|E∩W\| ≥ 2q−n for two qualifying sets and connects 2q>n and one vote per term to exclusion of two leaders. | Met | Met |
| Establishes necessity when 2q≤n using disjoint sets, computes the five-voter majority of three and illustrates disjoint groups of three in the hypothetical six-voter case. | Missed | Met |
| Explicitly distinguishes the hypothetical six-voter threshold from Raft's real majority and states why election safety alone does not guarantee progress when too few votes are available. | Met | Met |

**Masked review** (Y = baseline; X = standard). Both derive the inclusion–exclusion bound, apply one vote per term and distinguish safety from election progress. X explicitly constructs disjoint sets for the general case 2q ≤ n and gives the sharp nonnegative bound. Y demonstrates the six-voter split but does not establish general necessity and calls 2q−n tight without the lower limit of zero. Y explicitly computes the safe six-voter threshold of four.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `b351e00329c8` / `40b121481c1f` / `8b4494337284`.

</details>

## hunminjeongeum

**How much of a Seoul journey can a better map shorten?**

[한국어](EXAMPLES.ko.md#hunminjeongeum)

2026-11-08 · `hunminjeongeum` 0.1.1 · English · `gpt-6-luna`

### Case and sources

- [서울특별시, 시민의 발, 디자인을 입다…서울시, 지하철 노선도 40년 만에 변경 (2023-09-13)](https://news.seoul.go.kr/culture/archives/520933). Design release on interchange markings, the circular Line 2 reference, and maximum time reduction in the 20s–30s domestic/foreign eye-tracking experiment.

### Prompt

> Explain in English in at most four sentences to someone taking the Seoul subway for the first time why the city proposed a new map in 2023 and what its numbers mean. On the old map, transfers were hard to distinguish from ordinary stations. The redesign joins the colours of connecting lines in one transfer symbol. In an eye-tracking experiment with Korean and international participants in their twenties and thirties, the time to locate a transfer on the map fell by up to about 69%. For illustration, assume a passenger spends 100 seconds using the old map and then 12 minutes riding the train. If that maximum reduction applied to map reading, what would the new combined time be? Someone proposes saying the whole journey becomes 69% faster.

### Without the skill

> Seoul proposed the map in 2023 because transfers were hard to spot on the old one. The new map combines the colours of connecting lines in a single transfer symbol, and in an eye-tracking experiment, Korean and international participants in their twenties and thirties found transfers up to about 69% faster. If finding a transfer took 100 seconds before, a 69% reduction would bring map-reading time to 31 seconds; with a 12-minute train ride, the combined time would be 12 minutes 31 seconds. So it would be misleading to say the whole journey becomes 69% faster: only the map-reading time is reduced in this example.

### With the skill at standard

> On Seoul’s old subway map, transfers were hard to distinguish from ordinary stations, so the city proposed a redesign in 2023 to make transfers easier to spot. It joins the colours of connecting lines in one transfer symbol; in an eye-tracking experiment with Korean and international participants in their twenties and thirties, the time to locate a transfer on the map fell by up to about 69%. In the example, a 69% reduction cuts 100 seconds of map reading to 31 seconds; adding the unchanged 12-minute ride gives a total of 12 minutes 31 seconds. So “the whole journey becomes 69% faster” would be inaccurate: the reported reduction applies to finding transfers on the map, not to the train ride or total journey.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Opens by connecting the passenger's difficulty finding transfers to the linked line-colour transfer symbol. | Met | Met |
| Computes about 31 seconds looking at the new map and about 12 minutes 31 seconds for the hypothetical total (train ride remains 12 minutes). | Met | Met |
| Makes clear the up-to-about-69% result was for locating transfers in the map experiment, not a measured 69% reduction of actual whole journeys. | Met | Met |

**Masked review** (Y = baseline; X = standard). Both explain the transfer symbol and correctly combine 31 seconds of map reading with an unchanged 12-minute ride. X describes the measured quantity as time falling by up to about 69%. Y calls it finding transfers ‘69% faster’, which is less precise than a 69% reduction in time, then gives the correct calculation and limits the result to the map task.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `41f1b8c56caa` / `a341d5a5f712` / `43a2e90ed3f6`.

</details>

## ietf-rfc

**Interpreting two different HTTP 429 retry clocks**

[한국어](EXAMPLES.ko.md#ietf-rfc)

2026-11-09 · `ietf-rfc` 0.1.10 · English · `gpt-6-luna`

### Case and sources

- [IETF RFC 6585 §4, 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4). Sections 4 and 7.2 cover explanation, optional Retry-After, cache prohibition, deliberately unspecified counting and a server’s discretion to omit 429.
- [IETF RFC 9110 §10.2.3, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3). The field accepts an HTTP date or nonnegative integer delay in seconds after response receipt. The response times and example header values in the exercise are illustrative.

### Prompt

> Write an internal API specification for two illustrative rate-limit responses. Both are sent at 09:00:00 UTC and received by the client at 09:00:05 UTC. The first has Retry-After: 45; the second has an HTTP date equivalent to 09:01:00 UTC that day. Assume synchronized clocks. Under RFC 6585 the server can choose 429, its content should explain the condition, Retry-After is optional, and caches cannot store a 429. RFC 9110 permits either an HTTP date or a nonnegative delay measured after receipt. Declare the BCP 14 keyword convention, give the client’s suggested retry time in each case, and say what neither time promises. Do not add a client obligation absent from the sources. Keep it concise. Write your answer in English.

### Without the skill

> ## Rate-limit responses
>
> This illustrative API may return **429 Too Many Requests** when a client exceeds its rate limit. The response content should explain the condition. The server may include `Retry-After`; it is optional. Caches **MUST NOT** store a 429 response.
>
> **BCP 14 convention:** The key words **MUST**, **MUST NOT**, **SHOULD**, and **MAY** are to be interpreted as described in BCP 14 only when they appear in all capitals.
>
> Both responses are sent at **09:00:00 UTC** and received at **09:00:05 UTC**. Assume synchronized clocks.
>
> | `Retry-After` value | Suggested retry time |
> |---|---|
> | `45` | **09:00:50 UTC** — 45 seconds after receipt |
> | HTTP date equivalent to **09:01:00 UTC** | **09:01:00 UTC** |
>
> Neither time promises that a retry will succeed or that the server will be available then.

### With the skill at standard

> # Rate-Limit Response Examples
>
> **Status:** Internal illustrative specification.
>
> ## Scope and terminology
>
> This specification covers two illustrative HTTP 429 responses and the client’s suggested retry times. “Receipt” means receipt by the client. Clocks are assumed synchronized.
>
> ## Requirements
>
> The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when, and only when, they appear in uppercase.
>
> | Actor | BCP 14 | Behavior and condition |
> |---|---|---|
> | Server | MAY | Choose status code 429 to indicate that the client has sent too many requests in a given amount of time. |
> | Server | SHOULD | Include a response representation that explains the condition. |
> | Server | MAY | Include `Retry-After` in a 429 response. |
> | Cache | MUST NOT | Store a 429 response. |
>
> ## Suggested retry times
>
> RFC 9110 allows `Retry-After` to contain either an HTTP date or a nonnegative delay in seconds measured after receipt. In both examples, the response is sent at 09:00:00 UTC and received at 09:00:05 UTC.
>
> - With `Retry-After: 45`, the suggested retry time is **09:00:50 UTC** (45 seconds after receipt).
> - With `Retry-After` set to an HTTP date equivalent to **09:01:00 UTC** that day, the suggested retry time is **09:01:00 UTC**.
>
> Neither time promises that the rate limit will have cleared or that a subsequent request will succeed. The client has no retry obligation specified here.
>
> ## References
>
> **Normative:** RFC 6585 (429 responses); RFC 9110 (`Retry-After` formats). RFC 2119 and RFC 8174 define BCP 14 keyword meanings.
>
> **IANA:** No IANA action applies to these examples.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| States a BCP 14 convention and preserves optional server selection of 429, SHOULD explanatory content, optional Retry-After and the cache's MUST NOT store obligation. | Met | Met |
| Correctly computes 09:00:50 UTC for the 45-second delay after receipt and 09:01:00 UTC for the date value. | Met | Met |
| Frames those times as suggested waits rather than a new client MUST/SHOULD, and states that a retry is not guaranteed to succeed. | Met | Met |

**Review.** The specification keeps each requirement with its actor. The two retry times are 09:00:50 and 09:01:00 UTC; neither obliges the client to retry or promises success.

Masked reviewer assignment: Y was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/ietf-rfc/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/ietf-rfc.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `a03848dad0d2` / `0e16e6d9aec6` / `18eb49ccc918`.

</details>

## imrad

**What ten years of LIGO background would imply for GW150914**

[한국어](EXAMPLES.ko.md#imrad)

2026-11-08 · `imrad` 0.1.3 · English · `gpt-6-luna`

### Case and sources

- [LIGO Scientific Collaboration and Virgo Collaboration, Observation of Gravitational Waves from a Binary Black Hole Merger (2016)](https://dcc.ligo.org/public/0122/P150914/014/LIGO-P150914_Detection_of_GW150914.pdf). Abstract and §V.B, binary coalescence search: event date, two detectors, frequency sweep, peak strain, predicted waveform match and upper bound on the false-alarm rate.

### Prompt

> Write a museum research abstract in at most five sentences about LIGO’s GW150914. On 14 September 2015 the Livingston and Hanford instruments recorded a signal rising from 35 to 250 Hz with peak dimensionless strain 1.0 × 10⁻²¹. Researchers found that it matched a predicted binary black-hole merger waveform. The search put its rate of noise candidates at least this significant below one per 203,000 years. An editor concludes: “There would be no false alarms in ten years, so the chance this event was noise is zero.” For an illustrative ten years at the same rate, compute an upper bound on the expected number of such noise candidates. Use the result to assess the editor’s reasoning, while keeping instrument readings, analysis, and interpretation distinct. Write the answer in English.

### Without the skill

> On 14 September 2015, LIGO’s Livingston and Hanford instruments recorded a signal rising from 35 to 250 Hz, with peak dimensionless strain of $1.0 \times 10^{-21}$. Analysis found that the signal matched a predicted binary black-hole merger waveform. The search estimated fewer than one noise candidate of at least this significance per 203,000 years; at that rate, the expected number in ten years is less than $10/203{,}000 \approx 4.9 \times 10^{-5}$. This very small upper bound does not mean there would be no false alarms or that the chance this event was noise is zero: it describes an expected rate, not a guarantee or a direct probability for this particular event.

<details>
<summary>Original math delimiters</summary>

````text
On 14 September 2015, LIGO’s Livingston and Hanford instruments recorded a signal rising from 35 to 250 Hz, with peak dimensionless strain of \(1.0 \times 10^{-21}\). Analysis found that the signal matched a predicted binary black-hole merger waveform. The search estimated fewer than one noise candidate of at least this significance per 203,000 years; at that rate, the expected number in ten years is less than \(10/203{,}000 \approx 4.9 \times 10^{-5}\). This very small upper bound does not mean there would be no false alarms or that the chance this event was noise is zero: it describes an expected rate, not a guarantee or a direct probability for this particular event.
````

</details>

### With the skill at standard

> **Status: IMRaD, standard level**
>
> **Introduction:** On 14 September 2015, the Livingston and Hanford instruments recorded a signal consistent with a predicted binary black-hole merger waveform. **Methods:** The instruments recorded a signal rising from 35 to 250 Hz, with peak dimensionless strain of 1.0 × 10⁻²¹; researchers compared it with the predicted waveform and estimated the rate of noise candidates at least this significant. **Results:** That rate was below one per 203,000 years, giving an illustrative ten-year upper bound of 10/203,000 ≈ 4.9 × 10⁻⁵ expected noise candidates. **Discussion:** This rate-based bound does not imply there would be no false alarms in ten years, nor does it make the chance that this event was noise zero; it describes an expected count, not certainty about an individual event.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly attributes the dated 35–250 Hz, 1.0 × 10⁻²¹ strain signal to both detectors and the waveform comparison to analysis rather than to the detectors. | Met | Met |
| Computes an expected count strictly below 10/203,000 (about 4.93 × 10⁻⁵) over the hypothetical ten years at the stated rate, without labeling it an event probability. | Met | Met |
| Rejects both the guarantee of zero noise candidates and a zero probability for this event; the abstract distinguishes the measured signal from the supported merger interpretation. | Met | Met |

**Masked review** (X = baseline; Y = standard). Both assign the observations to the detectors and the waveform comparison to analysis, compute an expected count below 10/203,000 and reject both zero-risk claims. X gives a four-sentence paragraph. Y labels the scientific sections clearly, but prepends an unrequested method-and-level status that makes masking imperfect.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `85287f2bd34d` / `d792488d2fd9` / `89f688d01cd5`.

</details>

## korean-plain-language

**Which months qualified for Seoul’s pilot refund?**

[한국어](EXAMPLES.ko.md#korean-plain-language)

2026-11-09 · `korean-plain-language` 0.1.9 · English · `gpt-6-luna`

### Case and sources

- [서울특별시 내 손안에 서울, ‘월 5만원대’ 청년 맞춤형 기후동행카드 나온다 (2024-02-21)](https://mediahub.seoul.go.kr/archives/2010350). City's February 2024 announcement, especially the retrospective refund, separate registration rule and monthly eligibility conditions under the original pilot.

**Language scope.** The editor’s explanation is in English; the object being edited is Korean. Quoted Korean phrases demonstrate tense, modality and polite endings.

### Prompt

> Write a brief editorial memo in English for an editor working on a Korean exhibit about Seoul’s 2024 youth Climate Card pilot. The draft says ‘지우와 민서는 지금 환급금을 받아요’. At the time, each completed 30-day pass used without a refund could qualify for a 7,000-won refund. Physical cards counted only after registration; mobile cards required no separate card registration. Both types required a refund application. Assume all other eligibility conditions were met. Jiwoo completed a first physical pass before registration, completed the second after registration, and refunded a third on day 18. Minseo completed two mobile passes without refund. Explain how much each could have applied for and why. Explain the time and payment implication in the draft and suggest a short Korean 해요체 phrase to fix it. Keep the editorial explanation in English; retain Korean where discussing the actual wording.

### Without the skill

> **Editorial memo**
>
> The statement ‘지우와 민서는 지금 환급금을 받아요’ implies that both are receiving refunds now. That is not supported: the amounts described are potential refunds they could have applied for, and both card types required an application.
>
> Jiwoo could have applied for **7,000 won** for the second pass only. The first physical pass was completed before the card was registered, so it did not count. The third pass was refunded on day 18, so it was not a completed 30-day pass used without a refund.
>
> Minseo could have applied for **14,000 won**: two completed 30-day mobile passes used without refunds, at 7,000 won each. Mobile cards did not need separate card registration, but still required a refund application.
>
> A concise 해요체 replacement is: **‘지우와 민서는 환급금을 신청할 수 있어요.’** This makes clear that the refunds were available to apply for, not necessarily already paid.

### With the skill at standard

> The draft’s “지우와 민서는 지금 환급금을 받아요” says Jiwoo and Minseo are receiving refunds now. The pilot’s refund was a past opportunity to apply for payment, so this wording may wrongly suggest a current payment or a guaranteed one. Replace it with **“환급금을 신청할 수 있었어요”** (“They could apply for a refund”).
>
> - **Jiwoo — 7,000 won.** The first physical pass was completed before registration, so it did not qualify. The second was completed after registration and without a refund, so Jiwoo could apply for 7,000 won. The third was refunded on day 18, so it did not qualify as a completed 30-day pass used without a refund.
> - **Minseo — 14,000 won.** Both mobile passes were completed without refunds. Mobile cards did not need separate registration, so each pass could qualify for 7,000 won.
>
> Both still had to apply; eligibility did not mean the refund was already received.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly gives Jiwoo 7,000 won, counting only the second pass and explaining why the unregistered and refunded passes do not count. | Met | Met |
| Correctly gives Minseo 14,000 won for two completed passes; distinguishes not having to register the mobile card from having to apply for either refund. | Met | Met |
| Explains the draft's timing and payment implications in English and proposes Korean 해요체 wording that conveys past eligibility to apply without implying current entitlement or automatic payment. | Missed | Met |

**Review.** Jiwoo could apply for 7,000 won and Minseo for 14,000. Mobile registration was waived, but both people still needed to apply. The proposed Korean wording describes eligibility at the time.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/korean-plain-language/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/korean-plain-language.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `22797d4c7797` / `b2b7f3a4df0d` / `af8afbb2a4fc`.

</details>

## microsoft-writing-style

**Clearing a Windows clipboard without losing two keepers**

[한국어](EXAMPLES.ko.md#microsoft-writing-style)

2026-11-09 · `microsoft-writing-style` 0.1.11 · English · `gpt-6-luna`

### Case and sources

- [Microsoft Support, Using the clipboard](https://support.microsoft.com/en-us/windows/apps/using-the-clipboard). The Windows 11 sections document opening device history, clearing unpinned entries and deleting one selected item. The clipboard contents are hypothetical.

**Language scope.** This English example applies the English technology-writing profile to an English Windows interface.

### Prompt

> Write Windows 11 help for a person who wants exactly two entries left in this PC's clipboard history. The Windows interface is in English. In this example the delivery address and an obsolete access code are pinned; a return reference and two draft notes are unpinned. Keep the address and the return reference, remove the other three, and avoid retyping either keeper. Windows logo key + V opens Clipboard history. You can pin an entry; Clear all removes the unpinned entries. See more (...) then Delete removes a chosen entry. Give one reliable sequence using Clear all, explain which action must come first and how to tell the goal was met. Use the actual controls. They only asked about this PC. Keep it concise. Write your answer in English.

### Without the skill

> 1. Press **Windows logo key + V** to open Clipboard history.
> 2. Find the **delivery address** and **return reference**. For each one, select **See more (…) > Pin**. Do this **before** clearing anything, so both keepers survive.
> 3. Select **Clear all**. This removes the unpinned **obsolete access code** and **two draft notes**.
> 4. Check the history: it should show exactly the **delivery address** and **return reference**, both pinned. No retyping is needed.
>
> This changes clipboard history on this PC only.

### With the skill at standard

> To leave exactly the delivery address and return reference in this PC’s clipboard history, first protect the address, then remove the obsolete access code and both draft notes. **Clear all removes every unpinned entry**, so pin the return reference before you use it.
>
> Press **Windows logo key + V** to open Clipboard history.
>
> | Item | Current state | What to do now |
> |---|---|---|
> | Delivery address | Pinned | Leave it as it is. |
> | Obsolete access code | Pinned | Select **See more (...)**, then **Delete**. |
> | Return reference | Unpinned | Pin it. |
> | First draft note | Unpinned | Leave it for **Clear all**. |
> | Second draft note | Unpinned | Leave it for **Clear all**. |
>
> After those steps, select **Clear all**. Check Clipboard history: the delivery address and return reference should be the only two entries left.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses Windows logo key + V and pins the return reference before Clear all; keeps the already pinned delivery address. | Met | Met |
| Uses See more (...) then Delete for the obsolete pinned access code, or expressly unpins it before Clear all so it is removed; does not imply Clear all alone deletes pinned items. | Missed | Met |
| Gives user-facing steps that end with exactly the address and return reference, remove the two drafts and make no unsupported claim about other devices. | Missed | Met |

**Review.** The sequence protects the unpinned return reference, keeps the pinned address and removes the unwanted pinned code separately. The two drafts go in the bulk clear.

Masked reviewer assignment: Y was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/microsoft-writing-style/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/microsoft-writing-style.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `0478d6d5cc87` / `4df37c28e2f2` / `8db00fcc99c0`.

</details>

## minto-pyramid

**Which crossings should receive the pilot first?**

[한국어](EXAMPLES.ko.md#minto-pyramid)

2026-11-09 · `minto-pyramid` 0.2.6 · English · `gpt-6-luna`

### Case and sources

- [FHWA, Leading Pedestrian Interval](https://highways.dot.gov/safety/proven-safety-countermeasures/leading-pedestrian-interval). Definition, timing, turning conflicts, visibility, accessibility and applicability at high-turning-volume crossings.
- [FHWA, Safety Evaluation of Protected Left-Turn Phasing and Leading Pedestrian Intervals on Pedestrian Safety (2018), FHWA-HRT-18-044](https://www.fhwa.dot.gov/publications/research/safety/18044/18044.pdf). Executive summary and combined leading-interval evaluation, including the Chicago, New York and Charlotte sites and pedestrian crash modification factor 0.87. The committee decision in the request is hypothetical.

### Prompt

> Write one concise decision-opening paragraph in English for a city committee. It can fund one pilot at a group of signalized crossings with heavy turning traffic; either group costs the same and the goal is to avert the larger expected number of vehicle–pedestrian crashes. WALK would begin 3–7 seconds before drivers get green. In FHWA's three-city study the estimated crash modification factor was 0.87. In this hypothetical comparison, without treatment North's crossings are expected to have 20 such crashes and South's 5 over the same period. Estimate what difference applying the study factor would make at each group. Recommend a site, explain why the head start might matter at turns, and specify a local comparison that could measure the effect of the pilot against what would have happened without it.

### Without the skill

> Fund one pilot at **North’s signalized crossings**, where heavy turning traffic and an expected 20 vehicle–pedestrian crashes make the potential benefit larger: applying FHWA’s estimated crash modification factor of 0.87 implies about 2.6 fewer crashes over the comparison period, versus about 0.65 fewer at South’s crossings, which are expected to have 5. The 3–7 second WALK head start may give pedestrians time to enter the crosswalk and become more visible to turning drivers before those drivers receive green. To measure the pilot’s effect, compare North’s before-and-after crash rate with the change over the same period at similar untreated crossings, accounting for pedestrian and vehicle volumes and other relevant changes.

### With the skill at standard

> Cities face vehicle–pedestrian crash risks at both groups of signalized crossings, and the committee can fund one pilot at either site. Which should it choose to avert more crashes, and how can it assess the pilot’s effect? Apply FHWA’s three-city study factor of 0.87 as an estimate: North’s expected 20 crashes would fall to 17.4, or about 2.6 fewer; South’s 5 would fall to 4.35, or about 0.65 fewer. I recommend North because the same estimated proportional reduction yields a larger absolute decrease there. The 3–7 second WALK head start could give pedestrians time to enter the crossing before turning drivers get green, making them more visible to drivers turning through the intersection. To measure the local effect, compare the change in vehicle–pedestrian crashes at North before and after the pilot with the change over the same periods at comparable untreated signalized crossings; matching traffic, turning patterns, and crash trends would make that comparison more credible. The estimates transfer the study factor to North and South, so they are not guaranteed local results.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly derives expected reductions of 2.6 at North and 0.65 at South (or gives both treated counts and these reductions). | Met | Met |
| Recommends North under the stated equal-cost objective and explains how the early WALK relates to turning vehicles or pedestrian visibility. | Met | Met |
| Labels the estimates conditional on transfer from the study and proposes a local treated-versus-credible-without-treatment comparison to test the effect. | Met | Met |

**Review.** The recommendation rests on 2.6 versus 0.65 expected crashes prevented at equal cost, conditional on local transfer. Comparable untreated intersections give the city a way to test that forecast.

Masked reviewer assignment: Y was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/minto-pyramid/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/minto-pyramid.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `8063d7e2ee16` / `447627226ac3` / `e506e806dc95`.

</details>

## new-harts-rules

**Correcting a percentage-point claim for a UK census exhibit**

[한국어](EXAMPLES.ko.md#new-harts-rules)

2026-11-09 · `new-harts-rules` 0.1.6 · English · `gpt-6-luna`

### Case and sources

- [Office for National Statistics, Housing, England and Wales: Census 2021 (5 January 2023)](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/housingenglandandwales/census2021). Section 6, Car or van availability, and title: 42.1% of London households versus 23.3% across England and Wales in 2021. Exhibition style and draft are original exercise inputs.

**Language scope.** The edited label and editorial note are both in English.

### Prompt

> Copyedit this UK exhibition label in English and append a short English editorial note explaining the denominator and the basis of the spelling decision. Original draft: ‘In “Housing, England and Wales: Census 2021”, ONS showed that 42.1% of Londoners lacked a car in 2021, 18.8 per cent more than across England and Wales.’ The bulletin reports households with no car or van available: 42.1% in London and 23.3% across England and Wales. The editor needs both the percentage-point gap and the relative excess over the England-and-Wales share (round that excess to the nearest whole per cent). House style spells out ‘per cent’ in prose; keep the ONS title verbatim. No passage from New Hart's Rules was supplied. Keep the edited sentence intelligible to a visitor who might otherwise confuse the two comparisons.

### Without the skill

> In ‘Housing, England and Wales: Census 2021’, ONS reported that 42.1 per cent of London households had no car or van available, compared with 23.3 per cent across England and Wales. That is a gap of 18.8 percentage points; London’s share was 81 per cent higher.
>
> *Editorial note: The denominator is households, and “no car or van available” describes household vehicle availability. The 18.8-point gap is the subtraction of the two shares; the 81 per cent relative excess is that gap divided by the England-and-Wales share, rounded to the nearest whole per cent. “Per cent” is spelled out to follow house style; no New Hart’s Rules passage was supplied.*

### With the skill at standard

> In “Housing, England and Wales: Census 2021”, ONS reported that 42.1 per cent of households in London had no car or van available, compared with 23.3 per cent across England and Wales. The London share was 18.8 percentage points higher, or 81 per cent greater relative to the England-and-Wales share.
>
> Editorial note: The denominator is households, not Londoners. The spelling “per cent” follows the stated house style; no relevant passage from *New Hart’s Rules*, second edition (2014), was supplied, so this spelling decision is not attributed to the book.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Keeps the title 'Housing, England and Wales: Census 2021' verbatim and the measurements at the household level, including no car or van available. | Met | Met |
| Uses 18.8 percentage points and about 81 per cent relative excess over 23.3%, keeping the measures distinct. | Met | Met |
| Uses ‘per cent’ for percentages in English prose; the English note identifies the denominator and exhibition house style without claiming verification from the book. | Met | Met |

**Review.** The label measures households and distinguishes the 18.8-point difference from the roughly 81 per cent relative excess. The spelling choice comes from the exhibition’s own house style.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/new-harts-rules/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/new-harts-rules.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `9b8e75069344` / `59f8ac49842a` / `0f0790f8516b`.

</details>

## nist-technical-publication

**Which improvement would reduce the uncertainty of NIST-F2 more?**

[한국어](EXAMPLES.ko.md#nist-technical-publication)

2026-11-09 · `nist-technical-publication` 0.1.4 · English · `gpt-6-luna`

### Case and sources

- [Heavner et al., First Accuracy Evaluation of NIST-F2, Metrologia (2014)](https://www.nist.gov/publications/first-accuracy-evaluation-nist-f2). Authors' abstract, including the July–August 2013 Type A and Type B fractional uncertainties, the 80 K interrogation environment and the reason for the dominant Type B contribution.

### Prompt

> Prepare a short technical note for a metrology lab deciding which component to improve in NIST-F2. In the July–August 2013 evaluation, Type A statistical fractional frequency uncertainty was 0.44 × 10⁻¹⁵ and Type B systematic uncertainty was 0.11 × 10⁻¹⁵. The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold; microwave-amplitude effects dominated Type B. For this comparison only, assume the two components are independent, combine them by root-sum-square, and compare two equally costly hypothetical upgrades: halve Type A alone or halve Type B alone. Show the present and both projected combined uncertainties, recommend one upgrade on this metric, and state why cooling by itself does not establish a fiftyfold improvement in overall uncertainty. Write the answer in English.

### Without the skill

> ### NIST-F2 upgrade comparison
>
> Assuming independent Type A and Type B components, the combined fractional frequency uncertainty is their root-sum-square:
>
> | Scenario | Type A | Type B | Combined uncertainty |
> |---|---:|---:|---:|
> | Present | 0.44 | 0.11 | **0.454 × 10⁻¹⁵** |
> | Halve Type A | 0.22 | 0.11 | **0.246 × 10⁻¹⁵** |
> | Halve Type B | 0.44 | 0.055 | **0.443 × 10⁻¹⁵** |
>
> On this metric, **halving Type A is the better upgrade**: it lowers the combined uncertainty substantially, while halving Type B produces only a small change because Type A is much larger.
>
> Cooling to 80 K reduced the blackbody-radiation uncertainty by more than fiftyfold, but that is a reduction in one systematic contribution, not in total uncertainty. Microwave-amplitude effects dominated Type B, and the overall uncertainty also includes Type A; therefore, cooling alone does not imply a fiftyfold improvement in the combined uncertainty.

### With the skill at standard

> ## NIST-F2 uncertainty improvement note
>
> The July–August 2013 evaluation reported a Type A statistical fractional frequency uncertainty of **0.44 × 10⁻¹⁵** and a Type B systematic uncertainty of **0.11 × 10⁻¹⁵**. Microwave-amplitude effects dominated Type B; the 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold.
>
> For this comparison, assume the Type A and Type B components are independent and combine them by root-sum-square:
>
> $$
> u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
> $$
>
> | Scenario | Type A uncertainty (× 10⁻¹⁵) | Type B uncertainty (× 10⁻¹⁵) | Combined uncertainty (× 10⁻¹⁵) |
> |---|---:|---:|---:|
> | Present | 0.44 | 0.11 | 0.454 |
> | Halve Type A | 0.22 | 0.11 | 0.246 |
> | Halve Type B | 0.44 | 0.055 | 0.443 |
>
> The table values are coefficients on the stated common scale; for example, the present combined uncertainty is **0.454 × 10⁻¹⁵**. On this metric, choose the Type A upgrade: it lowers the combined uncertainty more than halving Type B.
>
> Cooling alone does not establish a fiftyfold improvement in overall uncertainty. The reported reduction applies to the blackbody-radiation component, while other uncertainty sources remain; microwave-amplitude effects dominated Type B, and Type A was larger than Type B in this evaluation.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the Type A/B values with labels and fractional units and derives a current combined value near 0.454 × 10⁻¹⁵ under the stated independence assumption. | Missed | Met |
| Correctly calculates both hypothetical totals (about 0.246 × 10⁻¹⁵ if Type A halves and 0.443 × 10⁻¹⁵ if Type B halves) and favors Type A for the larger reduction at equal cost. | Met | Met |
| Keeps the projections separate from the 2013 observations, bounds the fiftyfold reduction to the blackbody contribution, and identifies microwave amplitude as the dominant Type B effect. | Met | Met |

**Review.** With independent components, the current combined fractional uncertainty is about 0.454 × 10⁻¹⁵. Halving Type A gives 0.246 × 10⁻¹⁵ versus 0.443 × 10⁻¹⁵ for Type B. The fiftyfold change belongs to the blackbody contribution.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/nist-technical-publication/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/nist-technical-publication.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `d936b66143cd` / `25ee98c46dab` / `2e5b1c8bcbd6`.

</details>

## orwell-six-rules

**What a unit mix-up did to the Mars Climate Orbiter estimate**

[한국어](EXAMPLES.ko.md#orwell-six-rules)

2026-11-08 · `orwell-six-rules` 0.1.3 · English · `gpt-6-luna`

### Case and sources

- [Cornelius J. Dennehy / NASA, Best Practices for the Design, Development, and Operation of Robust and Reliable Space Vehicle Guidance, Navigation, and Control Systems (NASA/TP–20230005922, April 2023)](https://ntrs.nasa.gov/api/citations/20230005922/downloads/20230005922.pdf). Appendix A-12, pp. 138–139, and lesson 0641: ground software/interface units, trajectory about 170 km low, and two possible outcomes after loss.

### Prompt

> Rewrite this museum label as one concise English paragraph. Draft: ‘Operational misalignment effectuated a 170-km plunge. SM_FORCES supplied thruster impulses in pound-force seconds, which navigation read as newton-seconds. The craft burned up.’ The real 1999 navigation estimate accumulated error and the spacecraft approached Mars about 170 km lower than planned. NASA could not distinguish destruction in the atmosphere from escape into a solar orbit. To make the unit error concrete, use a clearly labelled illustrative impulse of 2 pound-force seconds. For this exercise use 1 pound-force second ≈ 4.45 newton-seconds. Work out what the number should have meant to navigation and how far its reading was off. Keep the illustration separate from the reported mission outcome.

### Without the skill

> A 1999 navigation error accumulated over time, bringing the spacecraft to Mars about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or escaped into solar orbit. **Illustrative impulse, not a mission measurement:** 2 pound-force seconds should have meant about 8.9 newton-seconds to navigation; reading it as 2 newton-seconds was off by 6.9 newton-seconds.

### With the skill at standard

> Navigation errors accumulated during the 1999 mission, bringing the spacecraft to Mars about 170 km lower than planned. SM_FORCES supplied thruster impulses in pound-force seconds, but navigation read them as newton-seconds. **Illustrative example:** an impulse of 2 pound-force seconds should have meant about 8.9 newton-seconds to navigation; reading it as 2 meant the value was about 6.9 newton-seconds too low. NASA could not determine whether the spacecraft was destroyed in the atmosphere or escaped into solar orbit.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| For the illustrative impulse, gives about 8.9 newton-seconds rather than the 2 read by navigation, with an understatement of about 6.9 newton-seconds or a factor of about 4.45. | Met | Met |
| Keeps the hypothetical impulse distinct from the mission record and attributes the roughly 170 km difference to the accumulated trajectory-estimate error/low approach rather than to a known plunge. | Met | Met |
| Retains both possible fates and makes the causal sequence understandable to a museum visitor in a concise paragraph. | Missed | Met |

**Masked review** (Y = baseline; X = standard). Both calculate 8.9 newton-seconds and an understatement of 6.9 for the illustration, preserve the low approach and leave both fates open. X explicitly names SM_FORCES and says which units it sent and navigation read. Y gives the mismatch only as an illustrative calculation, leaving the connection to the real accumulated error implicit.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `90ee273da21c` / `38676238d03e` / `0d49ca5b7959`.

</details>

## socratic-self-questioning

**Can Finland’s basic-income result justify a forecast for 500 workers?**

[한국어](EXAMPLES.ko.md#socratic-self-questioning)

2026-11-09 · `socratic-self-questioning` 0.1.6 · English · `gpt-6-luna`

### Case and sources

- [Finnish Ministry of Social Affairs and Health and Kela, Results of the basic income experiment (6 May 2020)](https://valtioneuvosto.fi/en/-/1271139/perustulokokeilun-tulokset-tyollisyysvaikutukset-vahaisia-toimeentulo-ja-psyykkinen-terveys-koettiin-paremmaksi?languageId=en_US). Employment results and experiment design: participating population, €560 payment, November 2017–October 2018 comparison, first-year finding, and asymmetric 2018 activation-policy change.

### Prompt

> A policy brief predicts ‘If we pay 500 local residents, their employment will rise by 3,000 days.’ Evaluate this inference in one concise English paragraph for publication. In Finland's 2017–2018 experiment, 2,000 randomly selected unemployed benefit recipients got €560 per month. During November 2017–October 2018 recipients averaged 78 employment days, six more than the comparison group. Year one showed no group-level employment effect. A 2018 unemployment-benefit reform affected the groups differently, so researchers could not separate that reform's effect from the second-year basic-income effect. Identify the comparison group’s mean employment days, show how the forecast total was derived and explain what would have to be true for it to apply locally.

### Without the skill

> The Finnish results do not support the forecast as a general prediction: recipients averaged 78 employment days from November 2017 to October 2018, six more than the comparison group, whose mean was therefore 72 days. Multiplying that observed difference by 500 gives 3,000 additional employment days, but this is an extrapolation from Finland’s second-year estimate, not evidence that paying 500 local residents would cause the same increase. For the forecast to apply locally, the residents and program would need to be sufficiently comparable to the Finnish participants and experiment, and local conditions would need to produce a similar causal effect. The caveat is substantial: there was no group-level employment effect in year one, and because a 2018 benefit reform affected the groups differently, researchers could not separate its effects from those of basic income in year two.

### With the skill at standard

> The brief predicts 3,000 additional employment days by multiplying 500 residents by six days each. In Finland, unemployed benefit recipients selected for the experiment averaged 78 employment days from November 2017 through October 2018—six more than the comparison group’s 72—but there was no group-level employment effect in year one. The comparison group’s mean was 78 − 6 = 72 days. Because the 2018 benefit reform affected the groups differently, researchers could not isolate its effect from the second-year basic-income effect. The Finnish result therefore does not establish that paying local residents would add six days per person; the forecast applies only if the local recipients and comparison group are comparable and the payment produces the same six-day difference under local conditions.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Recovers a comparison mean of 72 days and identifies 3,000 as 500 times the six-day observed difference, not an observed local gain. | Met | Met |
| Addresses both the lack of a first-year group-level effect and the asymmetric 2018 reform as a reason the second-year difference does not isolate basic income's effect. | Met | Met |
| Limits the evidence to unemployed benefit recipients and identifies a transfer assumption for 500 local residents, without claiming the experiment proves no effect in any year. | Missed | Met |

**Review.** The comparison mean is 72 days. The 3,000 days are an extrapolation from six days per person. The answer identifies the studied population, the uneven reform exposure and the assumption needed for a local forecast.

Masked reviewer assignment: Y was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/socratic-self-questioning/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/socratic-self-questioning.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `6c4c77094da2` / `b7784aaaace2` / `1af4e026b8f6`.

</details>

## steve-jobs-presentation

**What Ingenuity’s hover time can and cannot tell an audience**

[한국어](EXAMPLES.ko.md#steve-jobs-presentation)

2026-11-09 · `steve-jobs-presentation` 0.1.8 · English · `gpt-6-luna`

### Case and sources

- [NASA, NASA’s Ingenuity Mars Helicopter Succeeds in Historic First Flight (April 19, 2021)](https://www.nasa.gov/news-release/nasas-ingenuity-mars-helicopter-succeeds-in-historic-first-flight/). Flight-day report: onboard control, altimeter-derived height and hover, total time, the airfield name and plans to analyze the data.

### Prompt

> Write three short speaker beats for a museum briefing as of 19 April 2021. Ingenuity flew autonomously at Wright Brothers Field on Mars to about 3 m, hovered for 30 seconds, and landed 39.1 seconds after takeoff. The flight proves powered, controlled flight on another planet. A proposed slide calls 3 m divided by the whole flight time 'the average climb speed.' Decide whether to use that metric. Give the audience a defensible proportion for time spent hovering and explain why the remaining time does or does not identify climb speed. Close with what the team could decide after reviewing flight data; do not assume a later test succeeded. Write the answer in English.

### Without the skill

> 1. Ingenuity’s first flight at Wright Brothers Field was autonomous: it climbed to about 3 metres, hovered for 30 seconds, and landed 39.1 seconds after takeoff. It demonstrated powered, controlled flight on another planet.
>
> 2. I would not call 3 metres divided by the full 39.1 seconds the “average climb speed.” The hover alone was 30 of 39.1 seconds—about 77% of the flight. The remaining 9.1 seconds include both ascent and descent, so they do not tell us how long the climb took or establish a climb speed.
>
> 3. After reviewing the flight data, the team could assess how the helicopter and its systems performed and decide whether to attempt another flight. That decision would depend on the data; it does not mean a later test had succeeded.

### With the skill at standard

> 1. “On 19 April 2021, Ingenuity flew autonomously at Wright Brothers Field on Mars, reaching about 3 meters. The flight demonstrated powered, controlled flight on another planet.”
>
> 2. “It hovered for 30 seconds of its 39.1-second flight—about 77 percent. I would not label 3 meters divided by total flight time as average climb speed: the remaining 9.1 seconds include ascent and descent, so they do not tell us how long the climb took.”
>
> 3. “After reviewing the flight data, the team can decide what to change or measure in a future flight; that review alone cannot tell us whether a later test will succeed.”

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the first Mars flight as autonomous, powered and controlled, retains about 3 m and distinguishes 30 s of hover from 39.1 s total. | Met | Met |
| Derives roughly 77% hovering and identifies the remaining 9.1 s as non-hover time including ascent and descent; rejects using total time to infer climb speed. | Met | Met |
| Uses three short audience-facing beats and closes on reviewing the flight data to inform the next test, without claiming future success. | Met | Met |

**Review.** The three spoken beats distinguish the 30-second hover from the whole flight. Ascent and descent share the remaining 9.1 seconds; reviewing the flight data informs the next test.

Masked reviewer assignment: X was the revised answer. The table retains the original control grades. [Previous pair and scores](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/steve-jobs-presentation/examples/standard.md) · [All attempts and adjudications](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/steve-jobs-presentation.json).

<details>
<summary>Run record</summary>

Baseline generated 2026-11-08. Revised treatment generated independently on 2026-11-09 with Codex CLI 0.167.0, low reasoning, in a fresh read-only session. SHA-256 prefixes (entrypoint / original baseline / revised answer): `24a22d2a3e7c` / `7cd7cfac8849` / `5e0194f544ea`.

</details>
