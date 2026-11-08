# Writing skills in English: 22 independent comparisons

[한국어 예제](EXAMPLES.ko.md)

Start with a question about [independent DNS caches](#feynman-technique), [a Mars rover that misses a contact slot](#answer-with-html), or [Seoul’s redesigned subway map](#hunminjeongeum). For every method, compare the baseline and standard answers to the same English request and see the three checks.

## How to read the evidence

We generated the English and Korean examples independently on 2026-11-08. Both languages use the same case facts and comparable reasoning, with format and language scope stated in the prompts. For example, the Korean plain-language task in this gallery asks for an English editorial explanation of Korean wording. The Korean New Hart’s example retains an English exhibition label and requests a Korean editorial note.

Codex CLI 0.167.0 requested `gpt-6-luna` at low reasoning effort. Each answer ran in a fresh read-only session in its own temporary directory outside the checkout. Both arms received only their own request; the treatment also received the selected method and its applicable instructions. No session received another answer, and the run checker rejected tool activity. The backend model build was not reported. Markdown math delimiters, hard breaks and whitespace-only lines are formatted for display; each page records hashes of the raw answers.

Reviewers set three checks per language before generation and graded with condition labels withheld. Some outputs revealed a method name or audit, limiting masking. In the 22 English pairs, the standard answer met more checks in 7 tasks, the same number in 12 and fewer in 3. These checks do not measure general writing quality or establish a language ranking. Each skill has one final pair per language.

The two galleries contain 88 primary answers. The English ELI5 page and the Korean Seoul subway-map page each preserve two answers to an earlier wording. One Korean rubric gloss on the Mars Climate Orbiter page was corrected after generation, then assessed again without condition labels. The HTML pages keep the first results and one fresh treatment per language after an inconsistency between the page text and displayed numbers. These six additional answers are outside the counts above. The [previous gallery](https://github.com/hobin01/writing-styles-from-giants/blob/06f7e14e4b9f1e1081e817d7f828278def138742/EXAMPLES.md) preserves the earlier Luna assessment and its retests.

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

2026-11-08 · `asd-ste100` 0.1.3 · English · `gpt-6-luna`

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

> ## Recovery handover
>
> Keep power connected until both indications are present: a steady flashing pattern on the green activity LED and a green HDMI screen. Disconnect power only after you observe both indications. Remove the recovery microSD card only after power is disconnected.
>
> In this bench drill, staff check each board at 0, 15, 30, 45, and 60 seconds. Once an indication appears, it persists.
>
> | Station | First check with both indications | Safe action |
> |---|---:|---|
> | North | 30 seconds | Both indications are present. Disconnect power, then remove the recovery microSD card. |
> | South | 45 seconds | Both indications are present. Disconnect power, then remove the recovery microSD card. |
> | East | None by 60 seconds | Keep power connected. Do not remove the recovery microSD card; wait until both indications are present. |
>
> Elapsed time alone does not authorize removal. North and South qualify at their first listed check when both indications are present. East does not qualify at 60 seconds because its HDMI screen is not green.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Derives North’s first qualifying check as 30 s and South’s as 45 s, using observation times rather than the raw times at which indicators changed. | Met | Met |
| For East at 60 s, withholds disconnect/removal and does not imply that a fixed timeout proves success or establishes hardware failure. | Met | Met |
| States the correct sequence in technician-usable English: observe both signals, disconnect power, then remove the recovery microSD card; calls the card consistently by the same name. | Missed | Met |

**Masked review** (Y = baseline; X = standard). Both give 30 s for North, 45 s for South and no qualifying observation for East by 60 s. Both keep East powered and put disconnection before removal. X repeats “recovery microSD card” in each station row; Y shortens it to “the card” in the East row. The safety decisions agree.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `6600af844428` / `9f618db8c88e` / `369141520448`.

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

2026-11-08 · `eli5` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [Monterey Bay Aquarium, Life of a rescued sea otter](https://www.montereybayaquarium.org/about-us/stories/life-of-a-rescued-sea-otter). Pup 696's rescue and grooming sections describe the role of air in the fur in warmth and buoyancy.
- [Monterey Bay Aquarium, Sea otter](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/sea-otter). Species account, Adaptations and Grooming: unlike many marine mammals, a sea otter relies on fur in cold water and lacks a thick layer of blubber.

### Prompt

> At Monterey Bay Aquarium, a five-year-old asks why caregivers groomed rescued sea otter pup 696. In a classroom demonstration invented for this question, two equally warm jars have identical model coats in the same cold bath. With air trapped in the fluffy coat, one jar cools 4 degrees in 20 minutes. With the coat wet and flat, the other cools 3 degrees in 10 minutes. A child says the fluffy jar lost warmth faster because four is more than three. Neither jar was tested for floating. Real sea otters lack thick blubber; grooming traps air in their fur, which helps them stay warm and float. Answer the child in at most five short sentences: use a fair comparison, explain whether air makes heat, and say what the jars can and cannot show about floating. Write the answer in English.

### Without the skill

> That comparison isn’t fair yet: the jars were measured for different lengths of time. Air doesn’t make heat; trapped air slows heat loss, so compare both coats over the same time. These jars can show how coats affect cooling, but they can’t tell us which coat floats better because floating wasn’t tested. Sea otters groom to trap air in their fur, which helps them stay warm and float.

### With the skill at standard

> When you fluff a blanket, it traps air in its little spaces. The air does not make heat; it slows heat from leaving, so let’s compare the jars over the same 10 minutes: the fluffy jar lost 2 degrees, and the wet, flat one lost 3. So the fluffy jar cooled more slowly. These jars show how coat air can help keep an otter warm, but they were not tested for floating, so they cannot show that. Real sea otters groom their fur to trap air, which helps them stay warm and float.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses an equal-time comparison to explain the apparent reversal (2 degrees versus 3 per 10 minutes, or equivalent rates) and identifies the fluffy coat as slower to cool on average. | Missed | Met |
| Connects grooming to trapped air keeping warmth from leaving as fast, without claiming that air creates heat or substituting an invented biological mechanism. | Met | Met |
| In at most five short child-facing sentences, separates the jars’ untested floating behavior from the fact that trapped air also helps real otters float. | Met | Missed |

**Masked review** (Y = baseline; X = standard). X computes 2 versus 3 degrees per ten minutes; Y notices the unequal observation times but leaves the normalized comparison for the child to calculate. Both explain that air slows heat loss, that the jars were not tested for floating, and that trapped air helps actual otters float. X fits five sentences but packs the calculation, a semicolon and a colon into one long sentence for a five-year-old; Y fits the shorter, child-facing format better. The 2 degrees per ten minutes is a normalized average. The demonstration did not measure the fluffy jar's drop in its first ten minutes.

<details>
<summary>Earlier wording and both returned answers</summary>

The initial prompt compared total heat loss in unequal intervals. We clarified that the child was comparing cooling rates and reran both English arms. Only the final pair is scored above.

**Earlier prompt**

> At Monterey Bay Aquarium, a five-year-old asks why caregivers groomed rescued sea otter pup 696. In a classroom demonstration invented for this question, two equally warm jars have identical model coats in the same cold bath. With air trapped in the fluffy coat, one jar cools 4 degrees in 20 minutes. With the coat wet and flat, the other cools 3 degrees in 10 minutes. A child says the fluffy jar lost more warmth because four is more than three. Neither jar was tested for floating. Real sea otters lack thick blubber; grooming traps air in their fur, which helps them stay warm and float. Answer the child in at most five short sentences: use a fair comparison, explain whether air makes heat, and say what the jars can and cannot show about floating. Write the answer in English.

**Earlier baseline**

> You’re right that 4 is more than 3, but the jars were checked for different lengths of time, so that isn’t a fair comparison. Air doesn’t make heat; trapped air slows heat from escaping, like a blanket. The jars suggest that fluffy fur can help keep warmth in. They weren’t tested for floating, so they can’t show whether the fur helps otters float.

**Earlier standard answer**

> Sea otters groom their fur to keep it fluffy, with tiny pockets of air inside. The jars cooled at different speeds: the fluffy jar lost 2 degrees in 10 minutes, while the wet jar lost 3 degrees in 10 minutes, so the wet one cooled faster. The air does not make heat; it helps the otter keep its body heat. The jars show how the coats slow cooling, but they cannot show whether air helps an otter float because neither jar was tested for floating.

</details>

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `10536a49c052` / `b13daecf86ad` / `a8ba35d193a1`.

</details>

## federal-plain-language

**Which 40-minute document trip covers both identities?**

[한국어](EXAMPLES.ko.md#federal-plain-language)

2026-11-08 · `federal-plain-language` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [SSA, U.S. Citizen/Child — Replacement Social Security Card (October 2026)](https://www.ssa.gov/pubs/EN-05-10514.pdf). English page of the October 2026 U.S. citizen/child replacement-card leaflet, sections on the child's and parent's identity, current originals, issuer-certified copies and unacceptable copies. The family's options and collection times are hypothetical; the identification requirements come from the leaflet.

**Language scope.** This uses the method’s English public-information profile.

### Prompt

> A parent has 45 minutes to collect evidence for the identity part of a U.S.-citizen child's replacement Social Security card application. Write a parent-facing answer in English in no more than five sentences using the October 2026 SSA leaflet. Both people need identity evidence. The child can use a current U.S. passport or current state-issued non-driver ID. The parent can use a current U.S. passport or driver's license. SSA accepts originals or issuer-certified copies, not notarized photocopies; a birth certificate proves age or citizenship but not identity. Hypothetical collection times add: the child's original birth certificate is already in hand, original passport takes 40 minutes, and issuer-certified non-driver ID takes 15. For the parent, a notarized passport photocopy takes 5, an issuer-certified passport copy 25, and an original license 35. Which route fits? Point out why the tempting shortcut fails. Address identity evidence only.

### Without the skill

> Use the child’s issuer-certified state non-driver ID (15 minutes) and the parent’s issuer-certified U.S. passport copy (25 minutes): together they take 40 minutes. The tempting shortcut—a notarized photocopy of the parent’s passport—doesn’t count because SSA accepts originals or issuer-certified copies, not notarized photocopies. The child’s birth certificate proves age or citizenship, but not identity, so it cannot replace the child’s ID.

### With the skill at standard

> Both you and your child need identity evidence for the replacement card application. For your child, get an issuer-certified copy of a current state-issued non-driver ID; it takes 15 minutes, while the original passport takes 40. For yourself, use your original driver’s license; it takes 35 minutes, while an issuer-certified passport copy takes 25. The fastest valid route is the child’s certified ID and your certified passport copy, which takes 40 minutes total. The notarized passport photocopy is not accepted, and the birth certificate proves age or citizenship, not identity.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the child's issuer-certified non-driver ID plus the parent's issuer-certified passport copy, totals 40 minutes and fits the 45-minute limit. | Met | Met |
| Explains both rejected shortcuts: the original birth certificate is insufficient for the child's identity and the notarized copy is insufficient for the parent's identity. | Met | Met |
| Gives the parent an actionable English identity-only answer in no more than five sentences without implying the full application is complete. | Met | Missed |

**Masked review** (X = baseline; Y = standard). Both identify the 15 + 25 = 40 minute combination and reject the birth certificate and notarized photocopy as identity shortcuts. X gives one consistent route. Y first tells the parent to use a 35-minute license, making that trip 50 minutes, then recommends the 25-minute passport copy instead.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `5ba332f74f16` / `cd08aed6cec9` / `6dc26dbd3b6c`.

</details>

## feynman-technique

**Why two DNS resolvers disagree after a record is created**

[한국어](EXAMPLES.ko.md#feynman-technique)

2026-11-08 · `feynman-technique` 0.1.3 · English · `gpt-6-luna`

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

> Harbor’s NXDOMAIN at 12:00 is cached for 300 seconds: RFC 2308 uses the smaller of the SOA TTL (900 seconds) and MINIMUM (300 seconds). The cache stores that the name does not exist, so at 12:06 Harbor can still receive NXDOMAIN even though the operator added the A record at 12:04. Harbor’s negative cache expires at 12:05.
>
> Hill’s independent resolver starts its own 300-second timer from its NXDOMAIN at 12:03, so it can also receive NXDOMAIN at 12:06; that cache expires at 12:08. After each cache expires, a query can reach the updated authority and see the A record. If Hill had not queried before 12:04, it would have no cached NXDOMAIN, so its first query at 12:06 could reach the authority and return the A record.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 300-second lifetime and the 12:05 Harbor and 12:08 Hill expirations from their own original queries. | Met | Met |
| At 12:06 Harbor can fetch the new address while Hill can still serve NXDOMAIN; creating the record did not restart or invalidate Hill's cached lifetime. | Missed | Missed |
| Explains for a junior developer why Hill with no earlier negative entry could fetch the new address at 12:06 under the stated assumptions, without implying a simultaneous global update. | Met | Met |

**Masked review** (X = baseline; Y = standard). Both derive 300 seconds, the 12:05 and 12:08 expirations, and Hill’s counterfactual. X initially says both resolvers can still return the cached negative answer at 12:06, then corrects itself for Harbor. Y says Harbor can still see NXDOMAIN at 12:06 even though it gives Harbor’s earlier expiration. Only Hill can reuse that negative entry.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `9249d0cc1aa8` / `dae944fee0be` / `1f151137eb92`.

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

2026-11-08 · `ietf-rfc` 0.1.3 · English · `gpt-6-luna`

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

> ## Retry timing for illustrative rate-limit responses
>
> This internal specification covers the client’s suggested retry time for two illustrative HTTP 429 responses. The server chooses whether to send a 429 response; if it does, RFC 6585 says its content should explain the condition, `Retry-After` is optional, and caches cannot store the response. The examples assume synchronized clocks.
>
> In this specification, uppercase requirement keywords have their BCP 14 meanings (RFC 2119 and RFC 8174). **MUST** and **MAY** describe requirements and permissions; they do not add client behavior beyond the cited sources.
>
> In both examples, the server sends the response at 09:00:00 UTC and the client receives it at 09:00:05 UTC.
>
> - With `Retry-After: 45`, the value is a nonnegative delay measured after receipt. The client’s suggested retry time is **09:00:50 UTC**.
> - With `Retry-After` set to an HTTP date equivalent to **09:01:00 UTC** that day, the client’s suggested retry time is **09:01:00 UTC**.
>
> Neither time promises that a retry will succeed or that the rate limit will have cleared.
>
> **References.** RFC 6585 and RFC 9110 are normative for this behavior; RFC 2119 and RFC 8174 define the stated keyword convention. No IANA action is required.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| States a BCP 14 convention and preserves optional server selection of 429, SHOULD explanatory content, optional Retry-After and the cache's MUST NOT store obligation. | Met | Met |
| Correctly computes 09:00:50 UTC for the 45-second delay after receipt and 09:01:00 UTC for the date value. | Met | Met |
| Frames those times as suggested waits rather than a new client MUST/SHOULD, and states that a retry is not guaranteed to succeed. | Met | Met |

**Masked review** (X = baseline; Y = standard). Both give the two times (09:00:50 and 09:01:00 UTC), preserve the server’s choice and retry semantics, and withhold any guarantee of success. X uses a table and an explicit cache MUST NOT. Y explains the cache prohibition in prose and supplies references. Both convey the content recommendation using lowercase “should,” rather than an uppercase BCP 14 keyword.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `1613a9080cdb` / `0e16e6d9aec6` / `db3dd8aedeae`.

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

2026-11-08 · `korean-plain-language` 0.1.2 · English · `gpt-6-luna`

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

> **Editorial memo**
>
> The draft, “지우와 민서는 지금 환급금을 받아요” (“Jiwoo and Minseo receive refunds now”), makes a past pilot sound current and suggests payment is automatic. Both are misleading: the refunds were available during the 2024 pilot, and eligible participants still had to apply.
>
> Jiwoo could have applied for **7,000 won**. The first physical pass was completed before registration, so it did not count; the second was completed after registration and was not refunded, so it qualified. The third pass was refunded on day 18 and was not a completed, unrefunded 30-day pass.
>
> Minseo could have applied for **14,000 won**. Both completed mobile passes were unrefunded and qualified; mobile cards did not require separate card registration. Minseo still needed to submit a refund application.
>
> A short 해요체 replacement is: **“2024년 시범사업 당시, 조건을 충족한 이용자는 환급을 신청할 수 있었어요.”** This makes the timing past and preserves the meaning as permission to apply, not a promise of payment.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly gives Jiwoo 7,000 won, counting only the second pass and explaining why the unregistered and refunded passes do not count. | Met | Met |
| Correctly gives Minseo 14,000 won for two completed passes; distinguishes not having to register the mobile card from having to apply for either refund. | Met | Met |
| Explains the draft's timing and payment implications in English and proposes Korean 해요체 wording that conveys past eligibility to apply without implying current entitlement or automatic payment. | Missed | Met |

**Masked review** (Y = baseline; X = standard). Both calculate 7,000 won for Jiwoo and 14,000 for Minseo, distinguish registration from applying, and explain the draft’s misleading present tense in English. X proposes Korean wording anchored to the 2024 pilot and uses 신청할 수 있었어요. Y’s replacement uses 신청할 수 있어요, which can still suggest current eligibility despite the accurate English explanation.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `c0be7cf32505` / `b2b7f3a4df0d` / `cdfd5fc43c0c`.

</details>

## microsoft-writing-style

**Clearing a Windows clipboard without losing two keepers**

[한국어](EXAMPLES.ko.md#microsoft-writing-style)

2026-11-08 · `microsoft-writing-style` 0.1.2 · English · `gpt-6-luna`

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

> Open Clipboard history with **Windows logo key + V**. To keep the delivery address and return reference without retyping either:
>
> 1. If the return reference is not pinned, select **See more (...)** next to it, then **Pin**.
> 2. Select **Clear all**. This removes the unpinned obsolete access code and both draft notes. The address and return reference stay because they’re pinned.
> 3. Check Clipboard history. Exactly two entries should remain: the delivery address and return reference. Both should show as pinned.
>
> Pin the return reference before selecting **Clear all**; otherwise, Clear all removes it. These steps affect clipboard history on this PC.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses Windows logo key + V and pins the return reference before Clear all; keeps the already pinned delivery address. | Met | Met |
| Uses See more (...) then Delete for the obsolete pinned access code, or expressly unpins it before Clear all so it is removed; does not imply Clear all alone deletes pinned items. | Missed | Missed |
| Gives user-facing steps that end with exactly the address and return reference, remove the two drafts and make no unsupported claim about other devices. | Missed | Missed |

**Masked review** (X = baseline; Y = standard). Both tell the reader to pin the return reference before Clear all. X unnecessarily asks the reader to pin the already pinned address as well. Both incorrectly describe the obsolete access code as unpinned: it survives Clear all, and neither answer deletes or unpins it. Their checks for a final two-item history cannot repair that missing step.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `fe6a3443c596` / `4df37c28e2f2` / `3db328b316a7`.

</details>

## minto-pyramid

**Which crossings should receive the pilot first?**

[한국어](EXAMPLES.ko.md#minto-pyramid)

2026-11-08 · `minto-pyramid` 0.2.2 · English · `gpt-6-luna`

### Case and sources

- [FHWA, Leading Pedestrian Interval](https://highways.dot.gov/safety/proven-safety-countermeasures/leading-pedestrian-interval). Definition, timing, turning conflicts, visibility, accessibility and applicability at high-turning-volume crossings.
- [FHWA, Safety Evaluation of Protected Left-Turn Phasing and Leading Pedestrian Intervals on Pedestrian Safety (2018), FHWA-HRT-18-044](https://www.fhwa.dot.gov/publications/research/safety/18044/18044.pdf). Executive summary and combined leading-interval evaluation, including the Chicago, New York and Charlotte sites and pedestrian crash modification factor 0.87. The committee decision in the request is hypothetical.

### Prompt

> Write one concise decision-opening paragraph in English for a city committee. It can fund one pilot at a group of signalized crossings with heavy turning traffic; either group costs the same and the goal is to avert the larger expected number of vehicle–pedestrian crashes. WALK would begin 3–7 seconds before drivers get green. In FHWA's three-city study the estimated crash modification factor was 0.87. In this hypothetical comparison, without treatment North's crossings are expected to have 20 such crashes and South's 5 over the same period. Estimate what difference applying the study factor would make at each group. Recommend a site, explain why the head start might matter at turns, and specify a local comparison that could measure the effect of the pilot against what would have happened without it.

### Without the skill

> Fund one pilot at **North’s signalized crossings**, where heavy turning traffic and an expected 20 vehicle–pedestrian crashes make the potential benefit larger: applying FHWA’s estimated crash modification factor of 0.87 implies about 2.6 fewer crashes over the comparison period, versus about 0.65 fewer at South’s crossings, which are expected to have 5. The 3–7 second WALK head start may give pedestrians time to enter the crosswalk and become more visible to turning drivers before those drivers receive green. To measure the pilot’s effect, compare North’s before-and-after crash rate with the change over the same period at similar untreated crossings, accounting for pedestrian and vehicle volumes and other relevant changes.

### With the skill at standard

> North is the stronger pilot choice: applying FHWA’s estimated crash modification factor of 0.87 to the expected counts implies about 2.6 fewer vehicle–pedestrian crashes at North’s crossings (20 × 0.13), compared with 0.65 fewer at South’s (5 × 0.13). The 3–7 second WALK head start may give pedestrians time to enter the crossing before turning drivers receive green, making them more visible and reducing conflicts. To measure the pilot’s local effect, compare crash changes at the treated crossings before and after installation with changes over the same periods at similar untreated crossings, accounting for differences in baseline crash trends and exposure.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly derives expected reductions of 2.6 at North and 0.65 at South (or gives both treated counts and these reductions). | Met | Met |
| Recommends North under the stated equal-cost objective and explains how the early WALK relates to turning vehicles or pedestrian visibility. | Met | Met |
| Labels the estimates conditional on transfer from the study and proposes a local treated-versus-credible-without-treatment comparison to test the effect. | Met | Met |

**Masked review** (Y = baseline; X = standard). Both recommend North, project reductions of 2.6 versus 0.65, explain the visibility mechanism and propose comparing changes with similar untreated crossings over the same periods. X mentions baseline trends and exposure; Y names pedestrian and vehicle volumes. Neither presents the forecast as a measured local benefit.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `1c5f170eb9d4` / `447627226ac3` / `60b342fd8bcc`.

</details>

## new-harts-rules

**Correcting a percentage-point claim for a UK census exhibit**

[한국어](EXAMPLES.ko.md#new-harts-rules)

2026-11-08 · `new-harts-rules` 0.1.2 · English · `gpt-6-luna`

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

> “In ‘Housing, England and Wales: Census 2021’, ONS reported that 42.1 per cent of London households had no car or van available, compared with 23.3 per cent across England and Wales—a gap of 18.8 percentage points. The London share was 81 per cent higher.”
>
> **Editorial note:** The denominator is households with no car or van available, not Londoners. The 18.8-point gap is 42.1 minus 23.3; the 81 per cent relative excess is that gap divided by 23.3, rounded to the nearest whole per cent. “Per cent” follows the stated house style; the ONS title remains verbatim. Edition: *New Hart’s Rules*, second edition (2014); level: standard. No relevant passage was supplied, so the spelling decision is attributed to house style, not to the book.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Keeps the title 'Housing, England and Wales: Census 2021' verbatim and the measurements at the household level, including no car or van available. | Met | Met |
| Uses 18.8 percentage points and about 81 per cent relative excess over 23.3%, keeping the measures distinct. | Met | Met |
| Uses ‘per cent’ for percentages in English prose; the English note identifies the denominator and exhibition house style without claiming verification from the book. | Met | Missed |

**Masked review** (Y = baseline; X = standard). Both retain the bulletin title, report household shares, and distinguish 18.8 percentage points from an 81 per cent relative excess. Y correctly describes households as the denominator. X calls households *with no car or van* the denominator in its note; those households form the numerator of each area's share. X also adds an unrequested edition and level, which may reveal the condition.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `984d898d4573` / `59f8ac49842a` / `0fe1907dab99`.

</details>

## nist-technical-publication

**Which improvement would reduce the uncertainty of NIST-F2 more?**

[한국어](EXAMPLES.ko.md#nist-technical-publication)

2026-11-08 · `nist-technical-publication` 0.1.3 · English · `gpt-6-luna`

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

> ## NIST-F2: upgrade comparison
>
> ### Basis
>
> During the July–August 2013 evaluation, Type A statistical fractional frequency uncertainty was $0.44 \times 10^{-15}$, and Type B systematic uncertainty was $0.11 \times 10^{-15}$. The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold, while microwave-amplitude effects dominated Type B.
>
> For this comparison, the two uncertainty components are assumed independent and combined by root-sum-square:
>
>
> $$
> u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
> $$
>
>
> ### Results
>
> | Case | Type A ($\times 10^{-15}$) | Type B ($\times 10^{-15}$) | Combined ($\times 10^{-15}$) |
> |---|---:|---:|---:|
> | Present | 0.44 | 0.11 | 0.454 |
> | Halve Type A | 0.22 | 0.11 | 0.246 |
> | Halve Type B | 0.44 | 0.055 | 0.443 |
>
> Values are rounded to three significant figures. For example, the present result is $\sqrt{0.44^2+0.11^2}=0.4536$, in units of $10^{-15}$.
>
> ### Recommendation
>
> On combined uncertainty alone, choose the hypothetical Type A upgrade: it lowers the result to $0.246 \times 10^{-15}$, compared with $0.443 \times 10^{-15}$ for halving Type B. This comparison assumes the upgrades cost the same and affect only the stated component.
>
> Cooling reduced the blackbody-radiation contribution, but that contribution is only one part of Type B, which is dominated by microwave-amplitude effects; Type A also contributes to the combined uncertainty. Therefore, the more-than-fiftyfold reduction in blackbody-radiation uncertainty does not establish a fiftyfold reduction in overall uncertainty.

<details>
<summary>Original math delimiters</summary>

````text
## NIST-F2: upgrade comparison

### Basis

During the July–August 2013 evaluation, Type A statistical fractional frequency uncertainty was \(0.44 \times 10^{-15}\), and Type B systematic uncertainty was \(0.11 \times 10^{-15}\). The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold, while microwave-amplitude effects dominated Type B.

For this comparison, the two uncertainty components are assumed independent and combined by root-sum-square:

\[
u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
\]

### Results

| Case | Type A (\(\times 10^{-15}\)) | Type B (\(\times 10^{-15}\)) | Combined (\(\times 10^{-15}\)) |
|---|---:|---:|---:|
| Present | 0.44 | 0.11 | 0.454 |
| Halve Type A | 0.22 | 0.11 | 0.246 |
| Halve Type B | 0.44 | 0.055 | 0.443 |

Values are rounded to three significant figures. For example, the present result is \(\sqrt{0.44^2+0.11^2}=0.4536\), in units of \(10^{-15}\).

### Recommendation

On combined uncertainty alone, choose the hypothetical Type A upgrade: it lowers the result to \(0.246 \times 10^{-15}\), compared with \(0.443 \times 10^{-15}\) for halving Type B. This comparison assumes the upgrades cost the same and affect only the stated component.

Cooling reduced the blackbody-radiation contribution, but that contribution is only one part of Type B, which is dominated by microwave-amplitude effects; Type A also contributes to the combined uncertainty. Therefore, the more-than-fiftyfold reduction in blackbody-radiation uncertainty does not establish a fiftyfold reduction in overall uncertainty.
````

</details>

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the Type A/B values with labels and fractional units and derives a current combined value near 0.454 × 10⁻¹⁵ under the stated independence assumption. | Missed | Met |
| Correctly calculates both hypothetical totals (about 0.246 × 10⁻¹⁵ if Type A halves and 0.443 × 10⁻¹⁵ if Type B halves) and favors Type A for the larger reduction at equal cost. | Met | Met |
| Keeps the projections separate from the 2013 observations, bounds the fiftyfold reduction to the blackbody contribution, and identifies microwave amplitude as the dominant Type B effect. | Met | Met |

**Masked review** (X = baseline; Y = standard). Both give the three combined values as 0.454, 0.246 and 0.443 × 10⁻¹⁵, choose Type A, and keep the fiftyfold reduction specific to blackbody radiation. X gives the component values as bare decimals in its table without stating their scale; Y labels all columns and identifies the 2013 measurements. Y's intermediate 0.4536 should be about 0.45354, which still rounds to the stated 0.454.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `33e35b943513` / `25ee98c46dab` / `97c03562d708`.

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

2026-11-08 · `socratic-self-questioning` 0.1.2 · English · `gpt-6-luna`

### Case and sources

- [Finnish Ministry of Social Affairs and Health and Kela, Results of the basic income experiment (6 May 2020)](https://valtioneuvosto.fi/en/-/1271139/perustulokokeilun-tulokset-tyollisyysvaikutukset-vahaisia-toimeentulo-ja-psyykkinen-terveys-koettiin-paremmaksi?languageId=en_US). Employment results and experiment design: participating population, €560 payment, November 2017–October 2018 comparison, first-year finding, and asymmetric 2018 activation-policy change.

### Prompt

> A policy brief predicts ‘If we pay 500 local residents, their employment will rise by 3,000 days.’ Evaluate this inference in one concise English paragraph for publication. In Finland's 2017–2018 experiment, 2,000 randomly selected unemployed benefit recipients got €560 per month. During November 2017–October 2018 recipients averaged 78 employment days, six more than the comparison group. Year one showed no group-level employment effect. A 2018 unemployment-benefit reform affected the groups differently, so researchers could not separate that reform's effect from the second-year basic-income effect. Identify the comparison group’s mean employment days, show how the forecast total was derived and explain what would have to be true for it to apply locally.

### Without the skill

> The Finnish results do not support the forecast as a general prediction: recipients averaged 78 employment days from November 2017 to October 2018, six more than the comparison group, whose mean was therefore 72 days. Multiplying that observed difference by 500 gives 3,000 additional employment days, but this is an extrapolation from Finland’s second-year estimate, not evidence that paying 500 local residents would cause the same increase. For the forecast to apply locally, the residents and program would need to be sufficiently comparable to the Finnish participants and experiment, and local conditions would need to produce a similar causal effect. The caveat is substantial: there was no group-level employment effect in year one, and because a 2018 benefit reform affected the groups differently, researchers could not separate its effects from those of basic income in year two.

### With the skill at standard

> The forecast implies six additional employment days for each of 500 residents, since 3,000 ÷ 500 = 6. In Finland’s experiment, recipients averaged 78 employment days—six more than the comparison group, whose mean was therefore 72 days. But that second-year difference cannot be attributed to basic income alone: a 2018 benefit reform affected the groups differently, and researchers could not separate its effect from the basic-income effect; year one showed no group-level employment effect. The local forecast would apply only if paying these residents produced the same six-day difference against a comparable local comparison group, with relevant conditions and policy effects sufficiently similar.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Recovers a comparison mean of 72 days and identifies 3,000 as 500 times the six-day observed difference, not an observed local gain. | Met | Met |
| Addresses both the lack of a first-year group-level effect and the asymmetric 2018 reform as a reason the second-year difference does not isolate basic income's effect. | Met | Met |
| Limits the evidence to unemployed benefit recipients and identifies a transfer assumption for 500 local residents, without claiming the experiment proves no effect in any year. | Missed | Missed |

**Masked review** (Y = baseline; X = standard). Both recover the 72-day comparison mean and explain the limitations from the first-year result and the 2018 reform. Both recognize that transferring the six-day difference requires comparable local conditions, but omit that the Finnish participants were unemployed benefit recipients. Y explicitly calls the 3,000 days an extrapolation; X reconstructs it by division.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `73849e50a54b` / `b7784aaaace2` / `15fcfc0f0a6a`.

</details>

## steve-jobs-presentation

**What Ingenuity’s hover time can and cannot tell an audience**

[한국어](EXAMPLES.ko.md#steve-jobs-presentation)

2026-11-08 · `steve-jobs-presentation` 0.1.1 · English · `gpt-6-luna`

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

> **Method status:** Jobs-inspired presentation structure · standard
>
> 1. **The milestone:** “On 19 April 2021, Ingenuity flew autonomously at Wright Brothers Field on Mars. It reached about 3 metres, hovered for 30 seconds, and landed 39.1 seconds after takeoff. The flight demonstrated powered, controlled flight on another planet.”
>
> 2. **What the timing tells us:** “The hover took about 77% of the flight: 30 divided by 39.1. I would not label 3 metres divided by the whole flight time—about 0.077 metres per second—as the average climb speed. The total includes the 30-second hover and time spent descending, so the remaining 9.1 seconds cannot tell us how long the climb took.”
>
> 3. **What comes next:** “The flight establishes the milestone; the timing alone does not establish climb speed. After reviewing the flight data, the team could decide whether it supports a climb-speed estimate and what, if anything, to investigate in a later flight. That would be a decision based on the data, not a claim that a later test succeeded.”

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the first Mars flight as autonomous, powered and controlled, retains about 3 m and distinguishes 30 s of hover from 39.1 s total. | Met | Met |
| Derives roughly 77% hovering and identifies the remaining 9.1 s as non-hover time including ascent and descent; rejects using total time to infer climb speed. | Met | Met |
| Uses three short audience-facing beats and closes on reviewing the flight data to inform the next test, without claiming future success. | Met | Missed |

**Masked review** (X = baseline; Y = standard). Both give the roughly 77% hover share, separate the 9.1 seconds of ascent and descent, and decline to infer climb speed. X gives three brief, speakable beats. Y's second beat is longer and the visible method status is additional material outside the requested three beats; its closing decision is still conditional on the data.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `172a5e6964a7` / `7cd7cfac8849` / `b1d810da602d`.

</details>
