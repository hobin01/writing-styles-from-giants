# How does GPT-6 Luna answer with and without a writing skill?

Every task uses a real case and asks the model to reason from evidence. For example, [two DNS caches](#feynman-technique) can return different answers at the same moment, [LIGO’s false-alarm rate](#imrad) bounds an expected count, and a [Seoul subway-map improvement](#hunminjeongeum) saves time on only one part of a trip. The target is at least high-school-level reasoning, even when the finished answer must suit a five-year-old. Difficulty is a design judgment; no student cohort has validated it.

**읽는 방법.** 같은 문제를 스킬 없이 푼 답과 `standard`로 푼 답을 비교했습니다. 먼저 두 답을 읽고, 아래 표에서 어느 판단이 달라졌는지 확인해 보세요. 형식이나 분량 문제는 표 아래 설명에도 기록했습니다.

## First-pass results

On **7** of 22 tasks, the standard answer met more of the three prespecified checks. On **12** it met the same number, and on **3** it met fewer. A tie can mean both answers missed a critical constraint. For example, both [PostgreSQL drafts](#google-design-doc) calculated the release threshold correctly and still recommended authorizing a build whose rehearsal failed it. The [NIST example](#nist-technical-publication) shows a case where the baseline calculated both projected uncertainties correctly and the skill answer did not.

## How the comparison was run

On 2026-11-08, Codex CLI 0.167.0 generated both arms with the explicit model ID `gpt-6-luna` and low reasoning effort. Every answer started in a fresh ephemeral session and a neutral directory outside this checkout. Both received identical task text. Only the treatment received the method entrypoint, method metadata, locale instructions and the `standard` level. Shell use and plugins were disabled, and the recorded final messages were checked against completed turns. The underlying model build was not exposed. To run a pair on a public prompt, use the [evaluation script](scripts/run_writing_pair.py) and [authoring instructions](docs/METHOD_AUTHORING.md).

For the initial 44 answers, reviewers wrote three binary checks before generation, then saw the answers as X and Y with the condition labels withheld. The label order varied across tasks. Some generated answers identified their own method or level, so masking was imperfect. Reviews are agent judgments; three checks do not cover every aspect of writing quality. Markdown hard line breaks are rendered equivalently in the quoted answers. In particular, a complete proof can miss an extra rubric demand that the original prompt left implicit. We report such cases in the comparison.

The initial tally stays fixed. On 15 tasks we revised a skill and ran a developmental check. On 3 of those tasks the request was clarified, so both answers were regenerated. The other retests reused the original baseline. A fresh reviewer assessed the masked retests, so even an unchanged answer may be judged differently. All 62 generated answers are available below; retest conclusions are separate from the initial comparison. One pair per task cannot establish a general performance advantage. The [previous gallery](https://github.com/hobin01/writing-styles-from-giants/blob/b230fdf3f3d7eb92f6707fe4da70d9764c0155ed/EXAMPLES.md) used `gpt-6.1-sol` and different questions.

To reproduce an initial prompt, use its initial method version from the previous gallery’s commit; the current checkout runs the latest version. The portable `skills/<id>/examples/standard.md` files own each comparison. After editing them, run `python3 scripts/build_example_gallery.py` to rebuild this page.

<!-- Standard examples below are generated. -->

- [amazon-six-page-narrative](#amazon-six-page-narrative) · [portable copy](skills/amazon-six-page-narrative/examples/standard.md)
- [answer-with-html](#answer-with-html) · [portable copy](skills/answer-with-html/examples/standard.md)
- [aristotle-syllogism](#aristotle-syllogism) · [portable copy](skills/aristotle-syllogism/examples/standard.md)
- [asd-ste100](#asd-ste100) · [portable copy](skills/asd-ste100/examples/standard.md)
- [boring-professor](#boring-professor) · [portable copy](skills/boring-professor/examples/standard.md)
- [diataxis](#diataxis) · [portable copy](skills/diataxis/examples/standard.md)
- [eli5](#eli5) · [portable copy](skills/eli5/examples/standard.md)
- [federal-plain-language](#federal-plain-language) · [portable copy](skills/federal-plain-language/examples/standard.md)
- [feynman-technique](#feynman-technique) · [portable copy](skills/feynman-technique/examples/standard.md)
- [google-design-doc](#google-design-doc) · [portable copy](skills/google-design-doc/examples/standard.md)
- [gtm-formal](#gtm-formal) · [portable copy](skills/gtm-formal/examples/standard.md)
- [hunminjeongeum](#hunminjeongeum) · [portable copy](skills/hunminjeongeum/examples/standard.md)
- [ietf-rfc](#ietf-rfc) · [portable copy](skills/ietf-rfc/examples/standard.md)
- [imrad](#imrad) · [portable copy](skills/imrad/examples/standard.md)
- [korean-plain-language](#korean-plain-language) · [portable copy](skills/korean-plain-language/examples/standard.md)
- [microsoft-writing-style](#microsoft-writing-style) · [portable copy](skills/microsoft-writing-style/examples/standard.md)
- [minto-pyramid](#minto-pyramid) · [portable copy](skills/minto-pyramid/examples/standard.md)
- [new-harts-rules](#new-harts-rules) · [portable copy](skills/new-harts-rules/examples/standard.md)
- [nist-technical-publication](#nist-technical-publication) · [portable copy](skills/nist-technical-publication/examples/standard.md)
- [orwell-six-rules](#orwell-six-rules) · [portable copy](skills/orwell-six-rules/examples/standard.md)
- [socratic-self-questioning](#socratic-self-questioning) · [portable copy](skills/socratic-self-questioning/examples/standard.md)
- [steve-jobs-presentation](#steve-jobs-presentation) · [portable copy](skills/steve-jobs-presentation/examples/standard.md)

## amazon-six-page-narrative

**Which bridge review should happen before proposed stockpiling?**

2026-11-08 · `amazon-six-page-narrative` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [NTSB, investigation HWY07MH024, Collapse of I-35W Highway Bridge, Minneapolis, Minnesota](https://www.ntsb.gov/investigations/Pages/HWY07MH024.aspx). What Happened and What We Found: 1 August 2007 collapse, inadequate U10 gusset plate capacity, combined loads, and omission of gusset plates from load-rating analyses. The proposed review by another owner is an exercise.

**Reasoning task.** Compare combined demand with estimated capacity, distinguish a computable warning from an unknown margin, and make a constrained decision grounded in the actual failure mechanism.

### Prompt

> Write the opening of a decision memo (at most 130 words) for a hypothetical owner considering material stockpiles on two truss bridges. At Minneapolis's I-35W bridge, NTSB found that undersized U10 gusset plates failed under combined loads from modifications, traffic and concentrated construction loads; load ratings had omitted the plates. This is a separate classroom screen, not actual ratings. For River Street, estimated plate capacity is 100 screening units and simultaneous loads are 68 existing + 18 deck modifications + 24 proposed construction. At Canal Street the corresponding loads are 66 + 14 + 15 and plate capacity is unknown. Visual inspections found no new visible damage. There is funding for one immediate load-rating review and neither site has a final engineering assessment. Choose the review priority, identify what to do about planned stockpiles at each site, and give leadership the reason.

### Without a skill

> **Recommendation:** Use the immediate load-rating review for River Street. Its screening loads total 110 units against an estimated 100-unit plate capacity, so defer the proposed stockpile there until engineers assess the bridge. At Canal Street, capacity is unknown; defer planned stockpiling until a load-rating review establishes whether it is safe, and seek the next available review there. No visible new damage does not establish capacity. The I-35W investigation showed that undersized gusset plates can fail under combined loads and that load ratings may omit plates. These classroom screening figures are not actual ratings, so they identify urgency, not safe load limits.

### With the skill at standard

> ## Decision requested
>
> Prioritize the immediate load-rating review for **River Street**. In this separate classroom screen, its estimated plate capacity is 100 screening units, while the simultaneous estimated loads total 110 (68 existing + 18 deck modifications + 24 proposed construction). This indicates a screening concern, not an actual rating or a final engineering assessment.
>
> For River Street, defer the planned stockpile until a qualified load-rating review determines whether it can proceed and under what conditions. At Canal Street, the estimated loads total 95 (66 + 14 + 15), but plate capacity is unknown. Defer that stockpile until capacity is assessed; the available review should go to Canal Street next.
>
> Leadership should act because NTSB found that undersized U10 gusset plates contributed to the I-35W bridge failure under combined loads, and its load ratings had omitted the plates. That precedent supports checking plate capacity under combined loads. No new visible damage was found at either site, but visual inspection does not resolve the unknown or screened capacity. The six-page budget is unverified.
>
> *Method: amazon-six-page-narrative v0.1.1, standard. Assumption: stockpiles are planned but not yet placed. No rendered page-count check was possible.*

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses the River Street figures to show combined demand 110 against estimated capacity 100 and gives it priority for the immediate review (or explicitly justifies a different priority while addressing that exceedance). | Met | Met |
| Uses Canal Street's 95-unit demand and missing capacity to leave its safety unresolved; does not clear either stockpile solely from a visual inspection. | Missed | Met |
| The memo makes a concrete stockpiling decision for both sites and connects it to NTSB's plate/combined-load finding without declaring either real bridge unsafe. | Met | Met |

Both prioritize River Street and defer the stockpiles at both sites. The baseline fits the 130-word opening and correctly calls Canal Street's capacity unknown, but never totals its 95 units of demand. The skill answer includes both totals and uncertainty, but exceeds the word budget even before its unsolicited method audit; ‘six-page budget’ adds a constraint the decision makers never supplied. The numerical checks do not capture that format cost.

**차이.** 두 답 모두 River Street를 먼저 검토하고 두 현장 모두 적재를 보류합니다. 미적용 답은 130단어 제한을 지키지만 Canal Street의 하중 합계 95를 생략합니다. 스킬 답은 두 하중을 모두 비교하지만 분량을 넘겼고, 요구하지 않은 6쪽 분량 점검과 스킬 정보를 덧붙입니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Constrain the excerpt to the requested audience and word budget; keep method auditing out of the memo. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> I recommend using the single immediate load-rating review for River Street and deferring its planned stockpile until the review is complete. In this separate classroom screen, River Street’s simultaneous loads total 110 screening units (68 existing + 18 deck modifications + 24 proposed construction) against an estimated plate capacity of 100. This is a screening result, not an actual rating or final engineering assessment. At Canal Street, the loads total 95 units (66 + 14 + 15), but plate capacity is unknown; defer the planned stockpile there too until qualified engineers assess the bridge. No new visible damage was found at either site, but visual inspection does not resolve capacity. The I-35W failure shows why gusset plates and combined loads matter: NTSB found that omitted load ratings missed undersized plates that failed under combined modification, traffic, and concentrated construction loads.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses the River Street figures to show combined demand 110 against estimated capacity 100 and gives it priority for the immediate review (or explicitly justifies a different priority while addressing that exceedance). | Met | Met |
| Uses Canal Street's 95-unit demand and missing capacity to leave its safety unresolved; does not clear either stockpile solely from a visual inspection. | Missed | Met |
| The memo makes a concrete stockpiling decision for both sites and connects it to NTSB's plate/combined-load finding without declaring either real bridge unsafe. | Met | Met |

Both the skill answer and the baseline prioritize River Street’s 110-unit load against estimated capacity of 100, defer both stockpiles, and connect the decision to the gusset plates and simultaneous loads at I-35W. The skill answer computes Canal Street’s 95-unit load and leaves capacity unresolved, but exceeds 130 words. The baseline identifies Canal Street’s unknown capacity and stays within the limit, but omits its 95-unit demand.

**차이.** 스킬 답과 미적용 답 모두 River Street의 하중 110이 추정 용량 100을 넘는다는 근거로 이곳을 우선하고, 두 곳의 자재 적치를 보류하며, I-35W의 거싯 플레이트와 복합 하중을 결정에 연결한다. 스킬 답은 Canal Street의 하중을 95로 계산하고 용량은 미확정으로 남기지만 130단어를 넘긴다. 미적용 답은 제한 안에서 용량을 알 수 없다고 밝히지만 그곳의 하중 95는 누락한다.

</details>

## answer-with-html

**When one more minute of Mars delay costs a whole contact window**

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

## aristotle-syllogism

**Can new moon and central alignment alone establish a total solar eclipse?**

2026-11-08 · `aristotle-syllogism` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [NASA, Why Do Eclipses Happen?](https://science.nasa.gov/eclipses/geometry/). Geometry, total and annular sections: solar eclipses occur at new moon; totality requires complete coverage, whereas an annular eclipse leaves a ring.
- [NASA, 2023 Annular Eclipse FAQ](https://science.nasa.gov/eclipses/future-eclipses/eclipse-2023/faq/). Eclipse science and the October 14, 2023 path of annularity identify the dated counterexample.

**Reasoning task.** Distinguish a converse from a contrapositive and use the radius difference of centered disks to test which geometry supplies a counterexample.

### Prompt

> A planetarium visitor reasons: 'Every total solar eclipse occurs at new moon; this is a new moon, so it is total.' They also argue that if it were not new moon, there could not be a total solar eclipse. Assess the two inferences separately. For a separate illustrative drawing, suppose an observer sees the two disks exactly centered, the Sun has angular diameter 0.53° and the Moon 0.50°. Calculate the angular width of the exposed rim on one side and infer what the observer would see. Then consider a centered 0.55° Moon instead. Use the actual annular solar eclipse of 14 October 2023 as a factual check, without attributing these invented diameters to it. Keep the answer concise enough to read beside the diagram.

### Without a skill

> **The logic.** “Every total eclipse happens at new moon” means a total eclipse requires a new moon. But it does not mean every new moon produces a total eclipse: the Moon must also pass directly in front of the Sun. The reverse claim is correct: without a new moon, there can be no total solar eclipse.
>
> **Illustrative drawing.** With the disks exactly centered, the 0.53° Sun and 0.50° Moon leave a diameter difference of 0.03°, so the exposed rim is **0.015° wide on each side**. The observer sees a bright ring of sunlight: an **annular eclipse**, not a total one. With a centered 0.55° Moon, it covers the 0.53° Sun completely, so the observer sees a **total eclipse**.
>
> **Factual check.** On 14 October 2023, an actual annular eclipse crossed the Americas: along its path, the Moon appeared too small to cover the Sun, leaving a bright ring. The invented diameters above are only for the drawing.

### With the skill at standard

> **Two inferences**
>
> Let total eclipses be events that occur at new moon. “Every total solar eclipse occurs at new moon” says total eclipses are included among new moons; it does not say every new moon produces a total eclipse. The first inference is invalid: the Moon could be new without a total eclipse occurring. A total eclipse also requires suitable alignment and apparent sizes.
>
> “If it were not new moon, there could not be a total solar eclipse” is the contrapositive of the first premise, so it follows: a total solar eclipse requires new moon. Neither inference establishes that the premise is factually supported; the first conclusion simply reverses its direction.
>
> **Illustrative drawing**
>
> With centered disks, the diameter difference is $0.53° - 0.50° = 0.03°$. The exposed rim on one side is half of that: **0.015°**. The Moon appears slightly smaller, leaving a thin ring of the Sun visible around it: an **annular** appearance, not a total eclipse.
>
> For a centered **0.55° Moon**, it exceeds the Sun’s diameter by $0.02°$, or **0.01° per side**. It would cover the Sun’s disk, producing a total-eclipse appearance, assuming the centers align exactly.
>
> As a factual check, the **14 October 2023** solar eclipse was annular along its path; that does not make the illustrative diameters actual measurements of that eclipse.

<details>
<summary>Original model text</summary>

````text
**Two inferences**

Let total eclipses be events that occur at new moon. “Every total solar eclipse occurs at new moon” says total eclipses are included among new moons; it does not say every new moon produces a total eclipse. The first inference is invalid: the Moon could be new without a total eclipse occurring. A total eclipse also requires suitable alignment and apparent sizes.

“If it were not new moon, there could not be a total solar eclipse” is the contrapositive of the first premise, so it follows: a total solar eclipse requires new moon. Neither inference establishes that the premise is factually supported; the first conclusion simply reverses its direction.

**Illustrative drawing**

With centered disks, the diameter difference is \(0.53° - 0.50° = 0.03°\). The exposed rim on one side is half of that: **0.015°**. The Moon appears slightly smaller, leaving a thin ring of the Sun visible around it: an **annular** appearance, not a total eclipse.

For a centered **0.55° Moon**, it exceeds the Sun’s diameter by \(0.02°\), or **0.01° per side**. It would cover the Sun’s disk, producing a total-eclipse appearance, assuming the centers align exactly.

As a factual check, the **14 October 2023** solar eclipse was annular along its path; that does not make the illustrative diameters actual measurements of that eclipse.
````

</details>

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Explains that new moon is necessary but insufficient, rejects the converse, and accepts the contrapositive about a non-new moon. | Met | Met |
| Computes the one-sided rim as (0.53−0.50)/2 = 0.015°, leading to a ring; with the centered 0.55° Moon the solar disk is fully covered at that observer. | Met | Met |
| Uses the 14 October 2023 annular eclipse as a real counterexample without presenting the classroom drawing’s diameters as measured historical values. | Met | Met |

Both reject the converse, accept the non-new-moon inference, and obtain a 0.015° rim or full coverage for the larger centered Moon. Both keep the 2023 event separate from the drawing. The baseline is shorter for a diagram label. The skill answer explicitly names the contrapositive and states the alignment and apparent-size conditions.

**차이.** 두 답 모두 역은 성립하지 않고 대우는 성립한다는 점, 한쪽 테두리가 0.015°라는 점, 실제 2023년 일식과 가상 그림의 차이를 지킵니다. 미적용 답은 도표 옆에 두기에 짧고, 스킬 답은 대우와 겉보기 크기 조건을 더 분명히 짚습니다.

## asd-ste100

**When can each Raspberry Pi 4 recovery station be powered down?**

2026-11-08 · `asd-ste100` 0.1.3 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Raspberry Pi, Raspberry Pi computer hardware documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#reflash-the-bootloader). Reflash the bootloader, especially the last step for an HDMI-connected board. The prompt covers only completion of a prepared recovery on the Pi 4 Model B.

**Reasoning task.** Combine two necessary conditions with discrete observation times, handle incomplete evidence at the last check, and preserve the ordered safety prerequisite in a technical handover.

### Prompt

> Write a concise English handover for technicians finishing a Raspberry Pi 4 Model B bootloader recovery with HDMI displays attached. Before disconnecting power they must observe both a steady flashing pattern on the green activity LED and a green HDMI screen. Remove the recovery microSD card only after power is disconnected. In this illustrative bench drill, staff check each board at 0, 15, 30, 45 and 60 seconds. Once an indication appears it persists. At North the LED pattern starts at 16 s and the HDMI screen turns green at 29 s. At South the screen turns green at 33 s and the LED pattern starts at 41 s. At East the LED pattern starts at 21 s and the screen is still not green at 60 s. No power has yet been disconnected. Give the first qualifying check for each station and the safe action there. Explain whether the elapsed time alone can authorize removal. Use one consistent name for the recovery microSD card.

### Without a skill

> ## Bench handover
>
> Keep both HDMI displays attached and leave power connected until each board shows **both** a steady flashing pattern on the green activity LED and a green HDMI screen. Remove the recovery microSD card only after disconnecting power.
>
> Checks are at 0, 15, 30, 45 and 60 seconds. Once an indication appears, it persists.
>
> | Station | First check showing both indications | Safe action |
> |---|---:|---|
> | North | 30 seconds | Disconnect power, then remove the recovery microSD card. |
> | South | 45 seconds | Disconnect power, then remove the recovery microSD card. |
> | East | No qualifying check by 60 seconds | Keep power connected and the card in place; wait for both indications, then disconnect power before removing the card. |
>
> Elapsed time alone does **not** authorize removal. Each board must show both indications first, and power must be disconnected before removing the recovery microSD card.

### With the skill at standard

> North first qualifies at 30 seconds: both indications are present. Disconnect power, then remove the recovery microSD card.
>
> South first qualifies at 45 seconds: both indications are present. Disconnect power, then remove the recovery microSD card.
>
> East does not qualify at any check through 60 seconds because its HDMI screen is not green. Keep power connected and the recovery microSD card in place; continue recovery until both indications are present.
>
> Elapsed time alone does not authorize removal. Disconnect power only after you observe both the steady flashing pattern on the green activity LED and a green HDMI screen. Remove the recovery microSD card only after power is disconnected.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Derives North’s first qualifying check as 30 s and South’s as 45 s, using observation times rather than the raw times at which indicators changed. | Met | Met |
| For East at 60 s, withholds disconnect/removal and does not imply that a fixed timeout proves success or establishes hardware failure. | Met | Met |
| States the correct sequence in technician-usable English: observe both signals, disconnect power, then remove the recovery microSD card; calls the card consistently by the same name. | Missed | Met |

Both schedule North at 30 s and South at 45 s and keep East powered at 60 s. Both place removal after disconnection. The baseline gives a useful table, but refers to “both HDMI displays” for a three-station drill and shortens the requested recovery microSD card name to “the card” in the East row. The skill answer keeps the specified name in its actions.

**차이.** 두 답 모두 North는 30초, South는 45초에 전원을 끊을 수 있고 East는 60초에도 기다려야 한다고 판단합니다. 미적용 답의 표는 읽기 쉽지만 세 작업대를 두고 ‘두 화면’이라고 쓰고 카드 이름도 한 곳에서 줄였습니다. 스킬 답은 작업 지시에서 지정한 카드 이름을 유지합니다.

## boring-professor

**Tracking two Linux log files behind the same pathname**

2026-11-08 · `boring-professor` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Linux man-pages 6.19, unlink(2)](https://man7.org/linux/man-pages/man2/unlink.2.html). DESCRIPTION defines the effect of unlinking the last directory link with and without an open descriptor. The filenames, monitor, allocation sizes and event times are illustrative.

**Reasoning task.** Track two distinct file objects, two references to the unlinked file and allocated bytes at successive times instead of inferring storage from the visible pathname.

### Prompt

> Explain this Linux drill to a systems student. At 09:00 an administrator unlinks the last hard link to /var/log/payments.log. The old file has 20 MiB of allocated data; the writer and a monitor each hold an open descriptor to it. At 09:02 the service creates a separate file at the same pathname, with 5 MiB allocated. At 09:03 the original writer appends 8 MiB through its old descriptor, then closes it at 09:04. The monitor closes its old descriptor at 09:06. Trace which file gets the append, how much allocated data belongs to the two files just after 09:04 and just after 09:06, and why the pathname alone is insufficient evidence. Assume no sparse allocation, duplication or other changes; ignore metadata. Keep the explanation literal and under 120 words.

### Without a skill

> The 8 MiB append goes to the original file: the writer’s open descriptor still refers to its inode, even after the last hard link is unlinked. The new file created at `/var/log/payments.log` is separate and receives none of that append.
>
> Just after 09:04, the original has 28 MiB allocated but is unlinked; the new pathname file has 5 MiB. Just after 09:06, the original’s last open descriptor has closed, so it is deleted and has no allocated data remaining; the new file still has 5 MiB.
>
> The pathname alone cannot identify the file held by an open descriptor: after 09:02 it names the new file, while the old descriptors still refer to the original inode.

### With the skill at standard

> `unlink` removes a directory entry. An open file description can still refer to the old file after its last hard link is removed.
>
> The writer’s descriptor still refers to the original file, so its 8 MiB append goes there. The new file at `/var/log/payments.log` is separate.
>
> Just after 09:04, the original file has 28 MiB allocated (20 + 8); the new file has 5 MiB. The monitor’s descriptor still keeps the original file alive. Just after 09:06, when the monitor closes it, the original file is released, leaving 0 MiB allocated to it; the new file remains at 5 MiB.
>
> The pathname identifies the new file after 09:02. It does not identify the original file still held by open descriptors.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the append as going to the old, unlinked file through the writer's descriptor, not to the 5 MiB replacement at the reused pathname. | Met | Met |
| Gives 33 MiB just after 09:04 (28 old + 5 new) and 5 MiB just after 09:06; the monitor's descriptor delays release of the old file. | Missed | Missed |
| Explains the pathname/file-object distinction and the final-descriptor condition using literal technical terms, without implying that unlink disables existing writes. | Met | Met |

Both assign the 8 MiB append to the old file and explain why the pathname now names its replacement. Both give the 09:04 components as 28 MiB and 5 MiB but leave the requested total of 33 MiB to the reader. Both leave 5 MiB after the final close. The skill answer specifically names the monitor as the reason storage survives 09:04.

**차이.** 두 답 모두 8 MiB는 이전 파일에 기록되며 현재 경로는 새 파일을 가리킨다고 설명합니다. 09:04의 28 MiB와 5 MiB를 제시했지만 합계 33 MiB는 독자가 직접 계산해야 합니다. 마지막에 남는 5 MiB는 두 답 모두 맞았습니다. 스킬 답은 모니터의 디스크립터가 이전 파일을 붙잡고 있다고 명시합니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Calculate requested totals from their components and account for each state change. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> At 09:00, unlinking removes the old file’s last directory entry. An open descriptor still refers to that file, so the writer’s 8 MiB append goes to the old file, not the new file created at the same pathname.
>
> Just after 09:04, the old file has 28 MiB allocated (20 + 8); the new file has 5 MiB. The old file remains allocated because the monitor still has it open.
>
> Just after 09:06, the old file’s final open descriptor is closed, so its 28 MiB is released. The new file still has 5 MiB allocated.
>
> The pathname identifies the new file after 09:02. It does not identify the old file referenced by the open descriptors, so pathname alone cannot establish which file received the append.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the append as going to the old, unlinked file through the writer's descriptor, not to the 5 MiB replacement at the reused pathname. | Met | Met |
| Gives 33 MiB just after 09:04 (28 old + 5 new) and 5 MiB just after 09:06; the monitor's descriptor delays release of the old file. | Missed | Missed |
| Explains the pathname/file-object distinction and the final-descriptor condition using literal technical terms, without implying that unlink disables existing writes. | Met | Met |

The baseline and the skill answer correctly trace the 8 MiB append to the unlinked file. Both give the 09:04 amounts separately as 28 MiB old and 5 MiB new. Neither states the required combined total of 33 MiB, so both miss the second criterion. Both correctly leave only the new file’s 5 MiB after the last descriptor closes at 09:06. The skill answer identifies the monitor as the remaining descriptor holder and exceeds the under-120-word limit.

**차이.** 미적용 답과 스킬 답 모두 링크가 제거된 기존 파일에 8 MiB가 추가된다고 정확히 설명한다. 둘 다 09:04의 기존 파일 28 MiB와 새 파일 5 MiB를 각각 제시하지만, 요구한 합계 33 MiB를 명시하지 않아 두 번째 기준을 충족하지 못한다. 09:06에 마지막 파일 디스크립터가 닫힌 뒤 새 파일의 5 MiB만 남는다는 설명은 둘 다 맞다. 스킬 답은 남은 디스크립터를 모니터가 보유한다고 명시하지만, 120단어 미만 요건을 넘긴다.

</details>

## diataxis

**Which Kubernetes rollout did the green CI job actually observe?**

2026-11-08 · `diataxis` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/). Synopsis and flags document default revision tracking, --revision and --watch. checkout-api and revisions 7/8 are an illustrative release, not historical cluster telemetry.

**Reasoning task.** Infer what an apparently successful deployment monitor actually witnessed after its target changed, and distinguish that evidence from a nonblocking snapshot.

### Prompt

> Write a short lookup entry for the release team using kubectl rollout status on Deployment checkout-api. CI starts watching revision 7 without flags at 09:00. Before 7 finishes, revision 8 starts; the command later reports success. A default watch follows the latest rollout across revisions; a watch pinned with --revision=N aborts if superseded, and --watch=false reads a snapshot without waiting. Explain what the green job does and does not establish about 7 and 8. Give the exact commands for a new CI job that must monitor revision 7 specifically and for an operator who wants the current status immediately. Assume 8 is the last revision during this example. Make this useful for lookup, not a tutorial.

### Without a skill

> `kubectl rollout status deployment/checkout-api` watches the latest rollout by default. If revision 8 starts before revision 7 finishes, the watch follows 8; a green job establishes that the latest rollout (revision 8 here) succeeded. It does **not** establish that revision 7 completed successfully.
>
> To monitor revision 7 specifically, pin the watch:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> If revision 8 supersedes it, that command aborts rather than reporting success for 8.
>
> To read the current status immediately, without waiting:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```

### With the skill at standard

> ## `kubectl rollout status` for `checkout-api`
>
> A watch without flags follows the latest rollout. If revision 8 starts while the command is watching revision 7, the command follows revision 8. Assuming 8 is the last revision in this example, a successful exit means revision 8 completed; it does **not** establish that revision 7 completed.
>
> | Need | Command | Behavior |
> |---|---|---|
> | CI job must monitor revision 7 specifically | `kubectl rollout status deployment/checkout-api --revision=7` | Watches revision 7; aborts if a newer rollout supersedes it. |
> | Operator wants the current status immediately | `kubectl rollout status deployment/checkout-api --watch=false` | Reads a status snapshot and exits without waiting. |
>
> **Example:** CI starts an unpinned watch at 09:00 while revision 7 is running. Revision 8 starts before 7 finishes, and the command later reports success. The green job establishes that the latest rollout it followed—revision 8—completed. It does not establish that revision 7 completed.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Attributes the successful default watch to latest revision 8 and says that its success does not establish success for revision 7. | Met | Met |
| Gives an executable kubectl rollout status command for deployment/checkout-api with --revision=7, and states that supersession causes the pinned watch to abort rather than follow 8. | Met | Met |
| Gives an executable command with --watch=false for a current snapshot, with purpose and commands easy to find in a compact lookup entry. | Met | Met |

Both say the successful watch refers to revision 8 and cannot certify revision 7; both give usable pinned-watch and snapshot commands. The skill answer puts the commands and effects in a lookup table but repeats the green-job explanation. The baseline uses two shorter command blocks.

**차이.** 두 답 모두 성공이 revision 8을 가리키므로 revision 7의 성공은 확정할 수 없다고 설명하며, 고정 감시와 즉시 조회에 맞는 명령을 제공합니다. 스킬 답은 목적별 표를 썼지만 성공의 의미를 반복했고, 미적용 답은 두 코드 블록으로 더 짧게 정리했습니다.

## eli5

**Which model coat loses warmth faster, and what does that tell a child about pup 696?**

2026-11-08 · `eli5` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Monterey Bay Aquarium, Life of a rescued sea otter](https://www.montereybayaquarium.org/about-us/stories/life-of-a-rescued-sea-otter). Pup 696's rescue and grooming sections describe the role of air in the fur in warmth and buoyancy.
- [Monterey Bay Aquarium, Sea otter](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/sea-otter). Species account, Adaptations and Grooming: unlike many marine mammals, a sea otter relies on fur in cold water and lacks a thick layer of blubber.

**Reasoning task.** Normalize temperature changes by unequal exposure times and distinguish experimental evidence for insulation from the separate biological buoyancy claim, in language a child can follow.

### Prompt

> At Monterey Bay Aquarium, a five-year-old asks why caregivers groomed rescued sea otter pup 696. In a classroom demonstration invented for this question, two equally warm jars have identical model coats in the same cold bath. With air trapped in the fluffy coat, one jar cools 4 degrees in 20 minutes. With the coat wet and flat, the other cools 3 degrees in 10 minutes. A child says the fluffy jar lost more warmth because four is more than three. Neither jar was tested for floating. Real sea otters lack thick blubber; grooming traps air in their fur, which helps them stay warm and float. Answer the child in at most five short sentences: use a fair comparison, explain whether air makes heat, and say what the jars can and cannot show about floating.

### Without a skill

> The jars were in the same cold bath, but they were watched for different amounts of time, so we can’t fairly compare 4 degrees with 3 degrees. The fluffy coat cooled 4 degrees in 20 minutes; the wet, flat coat cooled 3 degrees in 10 minutes. Trapped air doesn’t make heat; it slows heat from escaping. The jars can show how coats may help keep warmth in, but they weren’t tested for floating. In real sea otters, grooming traps air in their fur, helping them stay warm and float.

### With the skill at standard

> These jars have not had a fair test: one cooled for 20 minutes, and the other for 10. Air does not make heat; when it is trapped in fluffy fur, it slows heat from escaping. The jars can show how coats may help keep warmth, but they do not show whether a coat helps an otter float because neither jar was tested for floating. Sea otters have little blubber, so grooming helps keep their fur fluffy and full of air.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses an equal-time comparison to explain the apparent reversal (2 degrees versus 3 per 10 minutes, or equivalent rates) and identifies the fluffy coat as slower to cool on average. | Missed | Missed |
| Connects grooming to trapped air keeping warmth from leaving as fast, without claiming that air creates heat or substituting an invented biological mechanism. | Met | Met |
| In at most five short child-facing sentences, separates the jars’ untested floating behavior from the fact that trapped air also helps real otters float. | Met | Missed |

Both notice the unequal times and explain that trapped air slows heat loss, but neither compares the rates: the fluffy coat lost 2 degrees per 10 minutes on average, the flat coat 3. The baseline distinguishes the jars’ untested buoyancy from real grooming that helps an otter float. The skill answer states the jars were not tested for floating but leaves out the known benefit to the animal. The baseline’s first sentence would still be long to read to a five-year-old.

**차이.** 두 답 모두 시간 차이를 알아채고 공기가 열을 만들지 않는다고 설명하지만, 같은 10분당 평균 2도와 3도로 비교하지는 못했습니다. 미적용 답은 병의 실험과 실제 수달이 뜨는 데 도움이 되는 효과를 구분했습니다. 스킬 답은 부력을 시험하지 않았다고만 하고 실제 효과를 빠뜨렸습니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Resolve unequal bases before simplifying; distinguish what an example measures from what it leaves untested. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> Imagine the two jars are boats in a cold bath: the fluffy coat jar cooled 4 degrees in 20 minutes, or 2 degrees in 10 minutes, while the wet, flat coat jar cooled 3 degrees in 10 minutes. So, over the same 10 minutes, the wet, flat coat jar lost more warmth. Air in a sea otter’s fur doesn’t make heat; it gets trapped and helps slow heat from leaving. The jars show how the coats slowed cooling in this classroom demonstration, but they weren’t tested for floating, so they can’t tell us which coat floats better. Sea otters groom their fur to trap air, which helps them stay warm and float.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses an equal-time comparison to explain the apparent reversal (2 degrees versus 3 per 10 minutes, or equivalent rates) and identifies the fluffy coat as slower to cool on average. | Missed | Met |
| Connects grooming to trapped air keeping warmth from leaving as fast, without claiming that air creates heat or substituting an invented biological mechanism. | Met | Met |
| In at most five short child-facing sentences, separates the jars’ untested floating behavior from the fact that trapped air also helps real otters float. | Missed | Missed |

The skill answer compares the average drops over ten minutes, 2 degrees for fluffy fur and 3 for flat fur. The baseline notices the unequal observation times but never works out which coat cooled faster. Both explain that trapped air slows heat loss and distinguish what the jars showed from what helps an otter float. Both use five sentences, but their opening sentences run to 38 and 27 words, respectively, a poor fit for a five-year-old.

**차이.** 스킬 답은 10분당 평균 하락 폭이 보송한 털에서 2도, 납작한 털에서 3도라고 비교한다. 미적용 답은 관찰 시간이 다르다는 점만 짚고 어느 쪽이 더 빨리 식는지는 말하지 않는다. 둘 다 공기가 열 손실을 늦춘다는 점과, 병 실험에서 확인한 사실과 실제 수달의 부력을 구분한다. 각각 다섯 문장이지만 첫 문장이 스킬 답은 38단어, 미적용 답은 27단어로 다섯 살 아이에게 길다.

</details>

## federal-plain-language

**Which 40-minute document trip covers both identities?**

2026-11-08 · `federal-plain-language` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [SSA, U.S. Citizen/Child — Replacement Social Security Card (October 2026)](https://www.ssa.gov/pubs/EN-05-10514.pdf). English page of the October 2026 U.S. citizen/child replacement-card leaflet, sections on the child's and parent's identity, current originals, issuer-certified copies and unacceptable copies. The family's options and collection times are hypothetical; the identification requirements come from the leaflet.

**Reasoning task.** Find a feasible two-person document set under a time constraint, distinguishing the document’s purpose from who certified it.

### Prompt

> A parent has 45 minutes to collect evidence for the identity part of a U.S.-citizen child's replacement Social Security card application. Write a parent-facing answer under 100 words using the October 2026 SSA leaflet. Both people need identity evidence. The child can use a current U.S. passport or current state-issued non-driver ID. The parent can use a current U.S. passport or driver's license. SSA accepts originals or issuer-certified copies, not notarized photocopies; a birth certificate proves age or citizenship but not identity. Hypothetical collection times add: the child's original birth certificate is already in hand, original passport takes 40 minutes, and issuer-certified non-driver ID takes 15. For the parent, a notarized passport photocopy takes 5, an issuer-certified passport copy 25, and an original license 35. Which route fits? Point out why the tempting shortcut fails. Address identity evidence only.

### Without a skill

> The 15-minute route fits: get the child’s issuer-certified state non-driver ID and use the parent’s original driver’s license, which takes 35 minutes. Both are current identity evidence, and the total is 50 minutes—so that route misses the 45-minute limit. There is no listed combination that fits: the child’s fastest qualifying ID alone takes 15 minutes, and the parent’s fastest qualifying option is the 25-minute issuer-certified passport copy, totaling 40 minutes. The tempting 5-minute notarized passport photocopy fails because SSA does not accept notarized photocopies. The birth certificate proves age or citizenship, not identity.

### With the skill at standard

> Bring the child’s **issuer-certified state non-driver ID** (15 minutes) and your **issuer-certified U.S. passport copy** (25 minutes). Together, they take **40 minutes**, so they fit the 45-minute window.
>
> The tempting shortcut—using the child’s birth certificate and your notarized passport photocopy—fails: a birth certificate proves age or citizenship, not identity, and SSA does not accept notarized photocopies as identity evidence.
>
> *Method: federal-plain-language, standard.*

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the child's issuer-certified non-driver ID plus the parent's issuer-certified passport copy, totals 40 minutes and fits the 45-minute limit. | Missed | Met |
| Explains both rejected shortcuts: the original birth certificate is insufficient for the child's identity and the notarized copy is insufficient for the parent's identity. | Met | Met |
| Gives the parent an actionable identity-only answer in at most 100 words without implying the full application is complete. | Missed | Missed |

The skill answer gives the feasible 15 + 25 = 40 minute trip first and correctly rejects both shortcuts, but appends an unsolicited method label to a parent-facing reply. The baseline also identifies the components and rejects the shortcuts, yet calls a 50-minute route feasible and then says no route fits even as it calculates 40 minutes. Its recommendation contradicts its own arithmetic.

**차이.** 스킬 답은 가능한 40분 경로를 먼저 제시하지만, 부모용 안내에 스킬 이름을 덧붙입니다. 미적용 답은 40분 조합을 계산해 놓고도 가능한 조합이 없다고 결론 내립니다. 두 답 모두 출생증명서와 공증 사본이 왜 부족한지는 설명합니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Return public-facing text without an unsolicited method label. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> Use the child’s issuer-certified state non-driver ID and your original driver’s license. They take 15 + 35 = 50 minutes, so **no listed route fits 45 minutes**. The child’s original birth certificate is already in hand, but it proves age or citizenship—not identity.
>
> The fastest parent option is the notarized passport photocopy (5 minutes), but SSA does not accept notarized photocopies. The issuer-certified passport copy is accepted but takes 25 minutes; paired with the child’s non-driver ID, that route takes 40 minutes and fits.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Identifies the child's issuer-certified non-driver ID plus the parent's issuer-certified passport copy, totals 40 minutes and fits the 45-minute limit. | Missed | Missed |
| Explains both rejected shortcuts: the original birth certificate is insufficient for the child's identity and the notarized copy is insufficient for the parent's identity. | Met | Met |
| Gives the parent an actionable identity-only answer in at most 100 words without implying the full application is complete. | Missed | Missed |

Both the skill answer and the baseline correctly reject the child’s birth certificate and the parent’s notarized photocopy and add 15 + 25 to get 40 minutes. The skill answer finally says the certified ID and certified passport copy fit, contradicting its opening recommendation and categorical claim that no route fits. The baseline likewise denies any feasible combination while giving its 40-minute total; it also calls the 15-plus-35-minute route a fit before rejecting it. Neither gives the parent a consistent decision.

**차이.** 스킬 답과 미적용 답 모두 자녀의 출생증명서와 부모의 공증 복사본을 배제하고 15분과 25분을 합해 40분을 얻는다. 스킬 답은 끝에서 발급기관 인증 신분증과 여권 사본이 시간 안에 가능하다고 쓰지만 처음에는 다른 조합을 권하고 가능한 경로가 없다고 단언한다. 미적용 답도 가능한 조합이 없다고 하면서 40분을 계산하고, 15분과 35분이 걸리는 경로도 처음에는 가능하다고 했다가 기각한다. 어느 쪽도 부모에게 일관된 선택을 제시하지 못한다.

</details>

## feynman-technique

**Why two DNS resolvers disagree after a record is created**

2026-11-08 · `feynman-technique` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [IETF RFC 2308, Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html#section-5). Sections 3 and 5 explain the SOA-based lifetime and expiry of negative responses. The hostname, TTL values and clock times are a worked trace, not production DNS records.

**Reasoning task.** Reason from the minimum of two lifetimes and two independent cache insertion times, then change one initial condition while holding the DNS change fixed.

### Prompt

> Two teams query uploads.example.org through independent DNS resolvers. In this illustrative trace, Harbor gets NXDOMAIN at 12:00 and Hill gets NXDOMAIN at 12:03. Both cache the name's absence. The zone's SOA TTL is 900 seconds and its MINIMUM is 300 seconds; RFC 2308 uses the smaller value for a negative answer. At 12:04 the operator creates the A record. At 12:06 both teams query again. In a short incident explanation for a junior developer, predict what each team can see, when the later cache expires, and what would change if Hill had not queried before 12:04. Assume a reachable, updated authority; no evictions, refreshes or local overrides. Do not ask the developer a question.

### Without a skill

> Harbor and Hill can still see the cached NXDOMAIN at 12:06, even though the A record was created at 12:04. Their resolvers cached the name’s absence for the smaller of the SOA TTL (900 seconds) and MINIMUM (300 seconds), so each negative cache entry lasts 300 seconds from its own NXDOMAIN response.
>
> Harbor’s entry expires at 12:05; Hill’s expires at 12:08. At 12:06, Harbor’s resolver can query the updated authority and return the A record, while Hill’s can still return NXDOMAIN. Once Hill’s entry expires at 12:08, its next query can also retrieve the A record.
>
> If Hill had not queried before 12:04, it would have no cached NXDOMAIN. Its first query after the record was created could reach the updated authority and return the A record immediately.

### With the skill at standard

> ### Incident explanation
>
> Harbor and Hill use independent resolvers, so each resolver caches its own answer. Under RFC 2308, the negative-cache TTL is the smaller of the SOA TTL and SOA MINIMUM: **300 seconds** here.
>
> - **Harbor** cached NXDOMAIN at 12:00. Its negative entry expires at **12:05**.
> - **Hill** cached NXDOMAIN at 12:03. Its entry expires at **12:08**.
>
> The operator added the A record at 12:04, but that does not erase either resolver’s cached NXDOMAIN. At 12:06, Harbor’s entry has expired, so—given the reachable, updated authority—it can resolve the new record. Hill’s entry is still valid, so Hill can still get NXDOMAIN until **12:08**. After it expires, Hill can query the authority and see the record.
>
> If Hill had not queried before 12:04, it would have no negative entry to reuse. At 12:06, it could query the updated authority and see the A record immediately. The difference is each resolver’s cache start time: Hill’s pre-change query started its own 300-second negative-cache period.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 300-second lifetime and the 12:05 Harbor and 12:08 Hill expirations from their own original queries. | Met | Met |
| At 12:06 Harbor can fetch the new address while Hill can still serve NXDOMAIN; creating the record did not restart or invalidate Hill's cached lifetime. | Missed | Met |
| Explains for a junior developer why Hill with no earlier negative entry could fetch the new address at 12:06 under the stated assumptions, without implying a simultaneous global update. | Met | Met |

Both compute 12:05 and 12:08 and explain the no-prior-query counterfactual. The baseline opens by saying both resolvers can serve cached NXDOMAIN at 12:06, contradicting its own correct Harbor calculation and later explanation. The skill answer consistently says only Hill's negative entry is still valid.

**차이.** 두 답 모두 12:05와 12:08이라는 만료 시각과 사전 조회가 없을 때의 결과를 구했습니다. 미적용 답 첫 문장은 12:06에도 양쪽 모두 캐시된 NXDOMAIN을 볼 수 있다고 써서 뒤의 정확한 계산과 충돌합니다. 스킬 답은 그때 Hill의 음성 캐시만 유효하다고 일관되게 설명합니다.

<details>
<summary>Developmental retest · version 0.1.3</summary>

Keep the mechanism, exception and worked prediction within the requested format. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> An NXDOMAIN reply caches that the name does not exist. Under RFC 2308, the negative-cache lifetime here is the smaller of the SOA TTL and MINIMUM: 300 seconds (5 minutes). Harbor’s cache expires at 12:05, five minutes after its 12:00 reply; Hill’s expires at 12:08, five minutes after its 12:03 reply. So at 12:06, Harbor can see the new A record from the updated authority, while Hill can still see its cached NXDOMAIN until 12:08. If Hill had not queried before the record was created, it would have no cached negative answer and could see the A record on its first query after 12:04.
>
> **Method/status:** Feynman-inspired explanation, standard level. This is a prediction from the stated trace and assumptions; no learner response was assessed.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 300-second lifetime and the 12:05 Harbor and 12:08 Hill expirations from their own original queries. | Met | Met |
| At 12:06 Harbor can fetch the new address while Hill can still serve NXDOMAIN; creating the record did not restart or invalidate Hill's cached lifetime. | Missed | Met |
| Explains for a junior developer why Hill with no earlier negative entry could fetch the new address at 12:06 under the stated assumptions, without implying a simultaneous global update. | Met | Met |

The skill answer and the baseline derive five-minute negative-cache lifetimes and expiries of 12:05 for Harbor and 12:08 for Hill. Both explain why Hill could fetch the address without an earlier negative entry. The skill answer gives a consistent prediction, then adds a visible Feynman method/level status. The baseline first says both resolvers can still serve cached NXDOMAIN at 12:06, contradicting its own later, correct statement that Harbor’s entry has already expired.

**차이.** 스킬 답과 미적용 답은 모두 음성 캐시 수명을 5분으로 계산하고 Harbor와 Hill의 만료 시각을 각각 12:05와 12:08로 제시한다. Hill이 앞서 부정 응답을 받지 않았다면 새 주소를 조회할 수 있는 이유도 설명한다. 스킬 답의 예측은 일관되지만 끝에 파인만 방법과 적용 수준을 표시한다. 미적용 답은 처음에 12:06에 두 리졸버 모두 캐시된 NXDOMAIN을 반환할 수 있다고 써서, 뒤에서 Harbor의 항목이 이미 만료됐다고 한 설명과 모순된다.

</details>

## google-design-doc

**Should PostgreSQL add the orders index during this shift?**

2026-11-08 · `google-design-doc` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [PostgreSQL 17 documentation, CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY). Building Indexes Concurrently explains locking, table scans, waiting for transactions and invalid indexes after failure. The store, schema and decision are illustrative; no production benchmark is quoted.
- [PostgreSQL 17 system catalogs, pg_index](https://www.postgresql.org/docs/17/catalog-pg-index.html). The indisvalid field records whether the index is valid for queries. The rehearsal metrics and release threshold are illustrative.

**Reasoning task.** Apply two independent release constraints to an architectural choice, compute the latency budget and plan a recovery path without converting a rehearsal into production evidence.

### Prompt

> Write a design-review excerpt for an illustrative PostgreSQL 17 store. The team cannot block order INSERTs throughout an index build. Its separate release gate is a rehearsal p95 write latency no more than 20% above the 40 ms baseline. A concurrent-build rehearsal measured 51 ms. Ordinary CREATE INDEX blocks writes; CREATE INDEX CONCURRENTLY lets writes continue, scans the table twice and can wait for transactions. A failed concurrent run can leave an invalid index that planners ignore but writes still maintain. Recommend what to authorize this shift, what to measure before retrying and how to handle an invalid result. The store has not measured production performance. Keep the excerpt under 145 words.

### Without a skill

> ### Index build release decision
>
> Authorize `CREATE INDEX CONCURRENTLY` for this shift: ordinary `CREATE INDEX` blocks writes, which the store cannot accept. The concurrent rehearsal measured 51 ms p95, 27.5% above the 40 ms baseline, so it fails the separate release gate of no more than 20% above baseline (48 ms). Do not treat the rehearsal as evidence of production performance; production has not been measured.
>
> Before retrying, measure rehearsal p95 write latency against the 40 ms baseline and investigate why it exceeded the 48 ms limit. Also check for long-running transactions that could delay the build. Concurrent creation scans the table twice and may wait for transactions.
>
> If a concurrent build fails, inspect the resulting index. If it is invalid, planners ignore it but writes still maintain it. Drop the invalid index before retrying, then verify the new index is valid.

### With the skill at standard

> **Proposal for review — PostgreSQL 17 index build.** Authorize `CREATE INDEX CONCURRENTLY`: order `INSERT`s must continue during the build. Ordinary `CREATE INDEX` blocks writes, so it violates that constraint. Concurrent builds scan the table twice and can wait for transactions. The rehearsal’s p95 write latency was 51 ms, 27.5% above the 40 ms baseline, exceeding the separate release gate of no more than 20% above baseline (48 ms).
>
> Before retrying, measure rehearsal p95 write latency under the same workload and investigate transaction waits; production performance is unmeasured. If the concurrent build fails, check for an invalid index: planners ignore it, but writes still maintain it. Remove the invalid index before retrying, then verify the retry succeeds.
>
> **Review status:** Proposed; authorization is pending.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 48 ms gate or the 27.5% increase and recognizes that the 51 ms concurrent rehearsal fails the allowed 20% increase. | Met | Met |
| Rejects an ordinary build during the shift because it blocks required INSERTs and holds the production rollout pending a passing new rehearsal; does not promise production latency. | Missed | Missed |
| Gives a concrete review or recovery plan that checks validity and deals with an invalid index that still imposes write cost (for example, remove it and retry safely). | Met | Met |

Both calculate the 48 ms ceiling and 27.5% increase and describe invalid-index handling. Despite recognizing the failed gate, both recommend authorizing the concurrent build. The skill answer later labels authorization pending, leaving the decision internally inconsistent; the baseline expressly authorizes it for this shift. Neither recommends holding production rollout until a rehearsal passes.

**차이.** 두 답 모두 상한 48 ms와 27.5% 증가율을 계산하고 무효 인덱스 처리 방안도 제시했습니다. 그런데 스킬 답과 미적용 답 모두 기준을 넘긴 빌드를 승인하자고 합니다. 스킬 답은 끝에서 다시 승인 대기라고 적고, 미적용 답은 이번 근무 중 승인하자고 명시합니다. 재시험 통과 전에는 배포를 보류해야 한다는 판단이 빠졌습니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Check each independent release gate before authorizing a proposed operation. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> **Context and constraints.** The team needs to build an index without blocking order `INSERT`s. Release also requires rehearsal p95 write latency at most 20% above the 40 ms baseline: 48 ms. Production performance is unmeasured.
>
> **Proposal for review: authorize the concurrent build for rehearsal only.** `CREATE INDEX CONCURRENTLY` allows writes to continue, but scans the table twice and can wait for transactions. The rehearsal measured 51 ms, above the 48 ms gate, so this is not authorization to release. Ordinary `CREATE INDEX` blocks writes and fails the operational constraint.
>
> **Before retrying,** measure rehearsal p95 write latency under representative load and investigate transaction waits. Retry only when the rehearsal meets the 48 ms gate.
>
> **Failure handling.** If the concurrent build fails, check for an invalid index: planners ignore it, but writes still maintain it. Remove the invalid index before retrying.
>
> **Status:** Proposed; release approval remains open pending a passing rehearsal.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Computes the 48 ms gate or the 27.5% increase and recognizes that the 51 ms concurrent rehearsal fails the allowed 20% increase. | Met | Met |
| Rejects an ordinary build during the shift because it blocks required INSERTs and holds the production rollout pending a passing new rehearsal; does not promise production latency. | Missed | Met |
| Gives a concrete review or recovery plan that checks validity and deals with an invalid index that still imposes write cost (for example, remove it and retry safely). | Met | Met |

Both the skill answer and the baseline compute the 48 ms gate, reject a write-blocking ordinary build, and call for inspecting and removing an invalid index. The skill answer permits rehearsal only, with release pending a passing result, but exceeds the under-145-word limit. The baseline correctly calculates the 27.5% increase and then authorizes the concurrent build for this shift without limiting authorization to rehearsal, despite the failed gate.

**차이.** 스킬 답과 미적용 답 모두 허용치를 48ms로 계산하고, 쓰기를 막는 일반 인덱스 생성을 배제하며, 무효 인덱스를 확인해 제거하도록 한다. 스킬 답은 재연습만 허용하고 통과 전까지 배포를 보류하지만 145단어 미만 요건을 넘긴다. 미적용 답은 27.5% 증가를 올바르게 계산하고도 기준에 미달한 상태에서 승인을 연습에 한정하지 않은 채 이번 근무조의 동시 인덱스 생성을 허용한다.

</details>

## gtm-formal

**When does a vote threshold exclude two Raft leaders?**

2026-11-08 · `gtm-formal` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm, §5.2](https://raft.github.io/raft.pdf). Section 5.2 and Figure 3 distinguish election safety, one vote per term, majority election and split votes.
- [etcd v3.5 FAQ, fault tolerance](https://etcd.io/docs/v3.5/faq/#what-is-failure-tolerance). The fault-tolerance table gives a quorum of three for five etcd members. The varied vote threshold is a mathematical exercise; real Raft uses a majority.

**Reasoning task.** Prove the general intersection criterion in both directions, specialize it to two configurations and separate a safety guarantee from the possibility of an election.

### Prompt

> In a formal note for a distributed-systems seminar, derive a necessary and sufficient inequality on a proposed election threshold q so that any two qualifying voter sets in a fixed cluster of n voters overlap (1 ≤ q ≤ n). Each voter grants at most one vote per term. Use the illustrative etcd-east and etcd-west candidates to connect the bound to election safety. Apply your result to normal majority voting with five voters and to a hypothetical threshold of three in a fixed six-voter cluster. Give a concrete six-voter counterexample if needed. Finally say what election safety alone implies about making progress when voters are unavailable. Keep the proof under 170 words.

### Without a skill

> In a fixed cluster of $n$ voters, any two qualifying sets of size at least $q$ overlap **if and only if**
>
> $$
> 2q>n.
> $$
>
> If $2q\le n$, two disjoint sets of $q$ voters can fit in the cluster; if $2q>n$, two disjoint sets would require more than $n$ voters.
>
> For five voters, normal majority voting requires $q=3$, and $2q=6>5$. Thus, if etcd-east and etcd-west each win with three votes, their voter sets share at least one voter. Since each voter grants at most one vote per term, that shared voter cannot vote for both candidates in the same term. This prevents both candidates from winning in that term.
>
> In a fixed six-voter cluster, a threshold of three does not ensure overlap: etcd-east could receive votes from voters $\{1,2,3\}$, while etcd-west receives votes from $\{4,5,6\}$. The sets are disjoint, so both could qualify without any voter casting two votes.
>
> Election safety alone does not guarantee progress when voters are unavailable. It gives a condition for preventing conflicting elections; if too few voters can participate to form a qualifying set, no election can be completed.

<details>
<summary>Original model text</summary>

````text
In a fixed cluster of \(n\) voters, any two qualifying sets of size at least \(q\) overlap **if and only if**
\[
2q>n.
\]
If \(2q\le n\), two disjoint sets of \(q\) voters can fit in the cluster; if \(2q>n\), two disjoint sets would require more than \(n\) voters.

For five voters, normal majority voting requires \(q=3\), and \(2q=6>5\). Thus, if etcd-east and etcd-west each win with three votes, their voter sets share at least one voter. Since each voter grants at most one vote per term, that shared voter cannot vote for both candidates in the same term. This prevents both candidates from winning in that term.

In a fixed six-voter cluster, a threshold of three does not ensure overlap: etcd-east could receive votes from voters \(\{1,2,3\}\), while etcd-west receives votes from \(\{4,5,6\}\). The sets are disjoint, so both could qualify without any voter casting two votes.

Election safety alone does not guarantee progress when voters are unavailable. It gives a condition for preventing conflicting elections; if too few voters can participate to form a qualifying set, no election can be completed.
````

</details>

### With the skill at standard

> **Method/status:** gtm-formal, standard level (version 0.1.1).
>
> Let $V$ be a fixed cluster of $n$ voters, and let a qualifying set contain at least $q$ distinct voters, where $1\le q\le n$. The condition that each voter grants at most one vote per term means two elections in the same term cannot both be supported by the same voter.
>
> **Claim.** Every two qualifying subsets of $V$ overlap if and only if
>
> $$
> 2q>n.
> $$
>
>
> **Proof.** If $A,B\subseteq V$ are qualifying and disjoint, then $|A\cup B|=|A|+|B|\ge 2q$, while $|A\cup B|\le n$. Thus disjoint qualifying sets are impossible when $2q>n$. Conversely, if $2q\le n$, choose disjoint subsets $A,B$ of size $q$; they are qualifying, so universal overlap fails. Hence the inequality is necessary and sufficient. ∎
>
> For five voters, normal majority requires $q=3$, and $2q=6>5$. Thus two elections in one term cannot both obtain disjoint voter support: in the illustrative case, etcd-east and etcd-west cannot both win under the one-vote-per-term assumption.
>
> For six voters and hypothetical $q=3$, $2q=6$, so overlap is not guaranteed. For example, $\{\text{A,B,C}\}$ and $\{\text{D,E,F}\}$ are disjoint qualifying sets.
>
> Election safety alone does not guarantee progress: unavailable voters may prevent any candidate from obtaining a qualifying set.

<details>
<summary>Original model text</summary>

````text
**Method/status:** gtm-formal, standard level (version 0.1.1).

Let \(V\) be a fixed cluster of \(n\) voters, and let a qualifying set contain at least \(q\) distinct voters, where \(1\le q\le n\). The condition that each voter grants at most one vote per term means two elections in the same term cannot both be supported by the same voter.

**Claim.** Every two qualifying subsets of \(V\) overlap if and only if
\[
2q>n.
\]

**Proof.** If \(A,B\subseteq V\) are qualifying and disjoint, then \(|A\cup B|=|A|+|B|\ge 2q\), while \(|A\cup B|\le n\). Thus disjoint qualifying sets are impossible when \(2q>n\). Conversely, if \(2q\le n\), choose disjoint subsets \(A,B\) of size \(q\); they are qualifying, so universal overlap fails. Hence the inequality is necessary and sufficient. ∎

For five voters, normal majority requires \(q=3\), and \(2q=6>5\). Thus two elections in one term cannot both obtain disjoint voter support: in the illustrative case, etcd-east and etcd-west cannot both win under the one-vote-per-term assumption.

For six voters and hypothetical \(q=3\), \(2q=6\), so overlap is not guaranteed. For example, \(\{\text{A,B,C}\}\) and \(\{\text{D,E,F}\}\) are disjoint qualifying sets.

Election safety alone does not guarantee progress: unavailable voters may prevent any candidate from obtaining a qualifying set.
````

</details>

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Proves the sufficient bound \|E∩W\| ≥ 2q−n for two qualifying sets and connects 2q>n and one vote per term to exclusion of two leaders. | Missed | Missed |
| Establishes necessity when 2q≤n using disjoint sets, computes the five-voter majority of three and illustrates disjoint groups of three in the hypothetical six-voter case. | Met | Met |
| Explicitly distinguishes the hypothetical six-voter threshold from Raft's real majority and states why election safety alone does not guarantee progress when too few votes are available. | Missed | Met |

Both correctly prove the requested iff by ruling out disjoint sets when 2q exceeds n and constructing them otherwise. Neither states the stronger numerical lower bound |E ∩ W| ≥ 2q − n in the first scoring check; this is not a flaw in either proof of overlap. Both give the six-voter split and separate safety from progress. The skill answer calls the threshold of three hypothetical; the baseline does not explicitly distinguish it from the real six-voter majority. The skill answer also inserts an unrequested method/version label. Both exceed 170 whitespace-separated words.

**차이.** 두 증명 모두 두 집합이 겹칠 필요충분조건을 올바르게 보였습니다. 첫 채점 항목은 문제에서 꼭 필요하지 않은 더 강한 교집합 크기 하한까지 요구했고, 둘 다 이를 쓰지 않았습니다. 여섯 명을 3명씩 나눈 반례와 진행 가능성의 한계는 공통입니다. 스킬 답은 3표 기준이 가정임을 밝혔고 미적용 답은 실제 6명 과반수와 명시적으로 구분하지 않았습니다. 스킬 답은 요청하지 않은 스킬 버전도 썼습니다. 두 답 모두 공백 기준으로 170단어를 넘겼습니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Clarify the demand for a quantitative lower bound and keep an explicit proof within its requested format. This retest is excluded from the first-pass counts.

**Revised request (both answers regenerated)**

> In a formal note for a distributed-systems seminar, derive a necessary and sufficient inequality on a proposed election threshold q so that any two qualifying voter sets in a fixed cluster of n voters overlap (1 ≤ q ≤ n). Derive a lower bound for the number of voters shared by two qualifying sets in terms of n and q. Each voter grants at most one vote per term. Use the illustrative etcd-east and etcd-west candidates to connect the bound to election safety. Apply your result to normal majority voting with five voters and to a hypothetical threshold of three in a fixed six-voter cluster. Give a concrete six-voter counterexample if needed. Finally say what election safety alone implies about making progress when voters are unavailable. Keep the proof under 170 words.

**New baseline**

> ### Quorum overlap and election safety
>
> Let $A,B\subseteq V$ be qualifying voter sets, each of size at least $q$, where $|V|=n$. Since
>
> $$
> |A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n,
> $$
>
> any two qualifying sets share at least $\max(0,2q-n)$ voters. Thus every pair must overlap exactly when $2q>n$, or equivalently $q>n/2$. This is necessary: if $2q\le n$, the voters can be divided into two disjoint sets of size $q$.
>
> For five voters, majority means $q=3$: any two majorities share at least $2(3)-5=1$ voter. In a fixed six-voter cluster, threshold $q=3$ does not ensure overlap: $\{\text{A},\text{B},\text{C}\}$ and $\{\text{D},\text{E},\text{F}\}$ are disjoint qualifying sets.
>
> For example, if etcd-east and etcd-west each win with three votes in that six-voter cluster, each voter’s one-vote-per-term limit does not prevent the two elections: the disjoint sets can vote for different candidates. A threshold of four would force at least two shared voters; because each can grant at most one vote per term, both candidates cannot receive those shared votes in the same term.
>
> Election safety is about preventing conflicting elections; by itself, it does not guarantee progress when voters are unavailable.

<details>
<summary>Original model text</summary>

````text
### Quorum overlap and election safety

Let \(A,B\subseteq V\) be qualifying voter sets, each of size at least \(q\), where \(|V|=n\). Since
\[
|A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n,
\]
any two qualifying sets share at least \(\max(0,2q-n)\) voters. Thus every pair must overlap exactly when \(2q>n\), or equivalently \(q>n/2\). This is necessary: if \(2q\le n\), the voters can be divided into two disjoint sets of size \(q\).

For five voters, majority means \(q=3\): any two majorities share at least \(2(3)-5=1\) voter. In a fixed six-voter cluster, threshold \(q=3\) does not ensure overlap: \(\{\text{A},\text{B},\text{C}\}\) and \(\{\text{D},\text{E},\text{F}\}\) are disjoint qualifying sets.

For example, if etcd-east and etcd-west each win with three votes in that six-voter cluster, each voter’s one-vote-per-term limit does not prevent the two elections: the disjoint sets can vote for different candidates. A threshold of four would force at least two shared voters; because each can grant at most one vote per term, both candidates cannot receive those shared votes in the same term.

Election safety is about preventing conflicting elections; by itself, it does not guarantee progress when voters are unavailable.
````

</details>

**New standard answer**

> **Claim.** Let $V$ be a fixed set of $n$ voters, and call $A\subseteq V$ qualifying when $|A|\ge q$, where $1\le q\le n$ is an integer. Every two qualifying sets overlap if and only if
>
> $$
> 2q>n.
> $$
>
> Moreover, for all qualifying $A,B\subseteq V$,
>
> $$
> |A\cap B|\ge 2q-n.
> $$
>
>
> **Proof.** Since $|A\cup B|\le n$,
>
> $$
> |A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n.
> $$
>
> Thus $2q>n$ guarantees overlap. Conversely, if $2q\le n$, partition $2q$ voters into disjoint sets $A,B$ of size $q$; any remaining voters lie outside both. These are disjoint qualifying sets, so universal overlap fails. The bound is sharp when $2q>n$: two $q$-element sets can have intersection exactly $2q-n$.
>
> For five voters, majority means $q=3$, so any two qualifying sets share at least $2(3)-5=1$ voter. In a fixed six-voter cluster with threshold $q=3$, the bound is zero: $\{\text{etcd-east-1, etcd-east-2, etcd-east-3}\}$ and $\{\text{etcd-west-1, etcd-west-2, etcd-west-3}\}$ are disjoint qualifying sets. If each voter grants at most one vote per term, overlap prevents two candidates from each receiving $q$ votes in that term, assuming both vote sets are drawn from the same fixed cluster. This is the quorum-intersection basis for election safety. Safety alone does not guarantee progress when voters are unavailable; enough available voters and the system’s other progress conditions are also needed.

<details>
<summary>Original model text</summary>

````text
**Claim.** Let \(V\) be a fixed set of \(n\) voters, and call \(A\subseteq V\) qualifying when \(|A|\ge q\), where \(1\le q\le n\) is an integer. Every two qualifying sets overlap if and only if
\[
2q>n.
\]
Moreover, for all qualifying \(A,B\subseteq V\),
\[
|A\cap B|\ge 2q-n.
\]

**Proof.** Since \(|A\cup B|\le n\),
\[
|A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n.
\]
Thus \(2q>n\) guarantees overlap. Conversely, if \(2q\le n\), partition \(2q\) voters into disjoint sets \(A,B\) of size \(q\); any remaining voters lie outside both. These are disjoint qualifying sets, so universal overlap fails. The bound is sharp when \(2q>n\): two \(q\)-element sets can have intersection exactly \(2q-n\).

For five voters, majority means \(q=3\), so any two qualifying sets share at least \(2(3)-5=1\) voter. In a fixed six-voter cluster with threshold \(q=3\), the bound is zero: \(\{\text{etcd-east-1, etcd-east-2, etcd-east-3}\}\) and \(\{\text{etcd-west-1, etcd-west-2, etcd-west-3}\}\) are disjoint qualifying sets. If each voter grants at most one vote per term, overlap prevents two candidates from each receiving \(q\) votes in that term, assuming both vote sets are drawn from the same fixed cluster. This is the quorum-intersection basis for election safety. Safety alone does not guarantee progress when voters are unavailable; enough available voters and the system’s other progress conditions are also needed.
````

</details>

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Proves the sufficient bound \|E∩W\| ≥ 2q−n for two qualifying sets and connects 2q>n and one vote per term to exclusion of two leaders. | Met | Met |
| Establishes necessity when 2q≤n using disjoint sets, computes the five-voter majority of three and illustrates disjoint groups of three in the hypothetical six-voter case. | Missed | Met |
| Explicitly distinguishes the hypothetical six-voter threshold from Raft's real majority and states why election safety alone does not guarantee progress when too few votes are available. | Missed | Missed |

Both the skill answer and the baseline derive the 2q−n overlap bound and illustrate disjoint triples among six voters. The skill answer proves necessity with 2q chosen voters and explicitly leaves the rest unused. The baseline says all voters can be divided into two q-sized sets when 2q≤n, which fails as a partition if 2q<n. The skill answer names example voters rather than the two candidates; the baseline correctly uses the candidate names and shows why four votes suffice with six voters. Neither explicitly identifies four as Raft’s actual six-voter majority. The skill answer connects unavailable votes to failure to elect; the baseline states only that progress is not guaranteed. Counting the full notes, including headings and one word per formula, gives about 186 and 173 words; the baseline’s body alone is under 170.

**차이.** 스킬 답과 미적용 답 모두 교집합 크기의 하한 2q−n을 유도하고 6명 중 서로 겹치지 않는 3명씩의 예를 든다. 스킬 답은 2q명을 골라 나머지를 제외해 필요성을 보인다. 미적용 답은 2q≤n이면 전체를 크기 q인 두 집합으로 나눌 수 있다고 하는데, 2q<n이면 전원을 그렇게 나눌 수 없다. 스킬 답은 후보 이름 대신 투표자에게 예시 이름을 붙인다. 미적용 답은 후보 이름을 올바르게 쓰고 6명 중 4표면 충분한 이유를 보인다. 둘 다 4표가 실제 Raft의 6인 과반수임을 명시하지 않는다. 스킬 답은 필요한 표가 모자라면 선출할 수 없다고 짚고 미적용 답은 진전이 보장되지 않는다고만 한다. 제목을 포함하고 수식 하나를 한 단어로 세면 전문은 각각 약 186단어와 173단어이며, 미적용 답의 본문만 세면 170단어 미만이다.

</details>

## hunminjeongeum

**How much of a Seoul journey can a better map shorten?**

2026-11-08 · `hunminjeongeum` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [서울특별시, 시민의 발, 디자인을 입다…서울시, 지하철 노선도 40년 만에 변경 (2023-09-13)](https://news.seoul.go.kr/culture/archives/520933). Design release on interchange markings, the circular Line 2 reference, and maximum time reduction in the 20s–30s domestic/foreign eye-tracking experiment.

**Reasoning task.** Apply a relative reduction to the measured component of a journey, recombine durations and judge whether the headline generalizes from an eye-tracking task.

### Prompt

> 서울 지하철을 처음 타는 사람에게, 서울시가 2023년에 노선도를 고치려 한 이유와 숫자의 의미를 한국어 네 문장 이내로 설명해 주세요. 기존 지도에서는 환승역이 일반역과 잘 구분되지 않았고, 개선안은 환승할 노선들의 색을 한 표시에 연결했어요. 20~30대 내국인·외국인의 시선 추적 실험에서 환승역 길 찾기 시간이 최대 약 69% 줄었어요. 설명용으로 어떤 승객이 예전 지도에서 길을 찾는 데 100초, 이후 열차를 타는 데 12분이 걸린다고 가정해요. 지도 보는 시간에 그 최대 감소율을 적용한다면 지도를 보고 열차를 타는 데 걸리는 합계는 얼마일까요? 누군가 ‘여정 전체가 69% 빨라진다’고 소개하려고 해요.

### Without a skill

> 서울시는 기존 노선도에서 환승역이 일반역과 잘 구분되지 않아 길을 찾기 어려운 점을 개선하려 했고, 개선안은 환승 노선들의 색을 하나의 표시에 연결했습니다. 20~30대 내국인·외국인 실험에서 환승역 길 찾기 시간이 최대 약 69% 줄었다는 뜻이지, 모든 승객이나 전체 여정의 시간이 69% 줄었다는 뜻은 아닙니다. 예전 지도에서 100초 걸렸다고 가정하면 지도 보는 시간은 31초로 줄고, 열차 탑승까지의 12분을 더하면 합계는 12분 31초입니다. 따라서 ‘여정 전체가 69% 빨라진다’고 소개하면 실험 결과의 범위를 과장하게 됩니다.

### With the skill at standard

> 서울 지하철을 처음 타면 기존 노선도에서 환승역이 일반역과 잘 구분되지 않아 갈아탈 곳을 찾기 어려울 수 있어요. 서울시는 2023년 개선안에서 환승할 노선들의 색을 하나의 표시에 연결해 환승역을 알아보기 쉽게 하려 했고, 20~30대 내국인·외국인의 시선 추적 실험에서는 환승역 길 찾기 시간이 최대 약 69% 줄었어요. 설명용 가정에서 지도 보는 시간 100초에 이 감소율을 적용하면 31초가 되고, 열차를 타는 데 걸리는 12분을 더한 합계는 **12분 31초**예요. 이 계산은 지도 보는 시간에만 적용되므로, ‘여정 전체가 69% 빨라진다’고 말할 근거는 없습니다.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Opens by connecting the passenger's difficulty finding transfers to the linked line-colour transfer symbol. | Met | Met |
| Computes about 31 seconds looking at the new map and about 12 minutes 31 seconds for the hypothetical total (train ride remains 12 minutes). | Missed | Met |
| Makes clear the up-to-about-69% result was for locating transfers in the map experiment, not a measured 69% reduction of actual whole journeys. | Met | Met |

Both explain the transfer symbol and calculate 31 seconds of map reading and a total of 12 minutes 31 seconds; neither assigns the 69% reduction to the whole journey. The skill answer correctly describes the 12 minutes as the ride. The baseline calls it the time ‘until boarding’ (탑승까지), changing what that interval represents despite getting the sum right.

**차이.** 둘 다 지도 보는 시간 31초와 합계 12분 31초를 계산했고, 69%는 지도 실험의 수치라고 밝힙니다. 스킬 답은 12분을 열차를 타는 시간으로 유지합니다. 미적용 답은 이를 ‘탑승까지의 12분’이라고 바꿔, 합계는 맞지만 그 시간이 의미하는 구간이 달라졌습니다.

## ietf-rfc

**Interpreting two different HTTP 429 retry clocks**

2026-11-08 · `ietf-rfc` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [IETF RFC 6585 §4, 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4). Sections 4 and 7.2 cover explanation, optional Retry-After, cache prohibition, deliberately unspecified counting and a server’s discretion to omit 429.
- [IETF RFC 9110 §10.2.3, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3). The field accepts an HTTP date or nonnegative integer delay in seconds after response receipt. The response times and example header values in the exercise are illustrative.

**Reasoning task.** Distinguish a duration measured from response receipt from an absolute timestamp while preserving separate optional and mandatory actions for servers and caches.

### Prompt

> Write an internal API specification for two illustrative rate-limit responses. Both are sent at 09:00:00 UTC and received by the client at 09:00:05 UTC. The first has Retry-After: 45; the second has an HTTP date equivalent to 09:01:00 UTC that day. Assume synchronized clocks. Under RFC 6585 the server can choose 429, its content should explain the condition, Retry-After is optional, and caches cannot store a 429. RFC 9110 permits either an HTTP date or a nonnegative delay measured after receipt. Declare the BCP 14 keyword convention, give the client’s suggested retry time in each case, and say what neither time promises. Do not add a client obligation absent from the sources. Limit the specification to 125 words.

### Without a skill

> ## Rate-limit responses
>
> This specification uses the BCP 14 keywords **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** as described in RFC 2119 and RFC 8174, only when they appear in all capitals.
>
> A server **MAY** respond to a rate-limited request with `429 Too Many Requests`. The response content **SHOULD** explain the condition. `Retry-After` is **OPTIONAL**. A `429` response **MUST NOT** be stored by a cache.
>
> `Retry-After` **MAY** contain a nonnegative delay, measured after the client receives the response, or an HTTP date.
>
> For both examples, the response is sent at 09:00:00 UTC and received at 09:00:05 UTC; clocks are synchronized.
>
> - `Retry-After: 45` suggests retrying at **09:00:50 UTC**.
> - An HTTP date of **09:01:00 UTC** suggests retrying at **09:01:00 UTC**.
>
> Neither suggested time promises that retrying then will succeed.

### With the skill at standard

> # Rate-Limit Response Examples
>
> **Status:** Internal illustrative specification. It does not define a new protocol.
>
> ## Abstract
>
> This specification gives two illustrative HTTP 429 responses and the client’s suggested retry times.
>
> ## Specification
>
> The server MAY choose status code 429 (Too Many Requests). Its content SHOULD explain the rate-limit condition. The server MAY include `Retry-After`. A cache MUST NOT store a 429 response.
>
> In this specification, uppercase **MUST**, **MUST NOT**, **SHOULD**, and **MAY** have their BCP 14 meanings (RFC 2119 and RFC 8174).
>
> Assume synchronized clocks. Both responses are sent at 09:00:00 UTC and received at 09:00:05 UTC.
>
> - With `Retry-After: 45`, the suggested retry time is 09:00:50 UTC: 45 seconds after receipt.
> - With `Retry-After` set to an HTTP date equivalent to 09:01:00 UTC that day, the suggested retry time is 09:01:00 UTC.
>
> Neither time promises that a retry will succeed or that the rate limit will have cleared. These examples create no client retry obligation.
>
> ## Security Considerations
>
> These examples do not establish that a retry is safe or successful.
>
> ## IANA Considerations
>
> This internal specification requires no IANA action.
>
> ## References
>
> **Normative:** RFC 6585; RFC 9110; RFC 2119; RFC 8174.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| States a BCP 14 convention and preserves optional server selection of 429, SHOULD explanatory content, optional Retry-After and the cache's MUST NOT store obligation. | Met | Met |
| Correctly computes 09:00:50 UTC for the 45-second delay after receipt and 09:01:00 UTC for the date value. | Met | Met |
| Frames those times as suggested waits rather than a new client MUST/SHOULD, and states that a retry is not guaranteed to succeed. | Met | Met |

Both get the relative delay and date right (09:00:50 and 09:01:00 UTC), distinguish server choice from cache prohibition, and avoid promising success. Both exceed the requested 125 words by a whitespace count; that length limit is outside the three scored checks. The skill answer adds an abstract, security, IANA and reference sections; the baseline spends part of its budget listing the BCP 14 vocabulary.

**차이.** 두 답 모두 09:00:50과 09:01:00을 구분하고 서버의 선택권과 캐시 저장 금지를 보존합니다. 두 답 모두 세 채점 항목 밖의 125단어 제한은 넘겼습니다. 스킬 답은 초록·보안·IANA·참고문헌 절을 추가했고, 미적용 답은 BCP 14 용어를 길게 나열했습니다.

<details>
<summary>Developmental retest · version 0.1.3</summary>

Use only the structure needed for the requested specification excerpt and its word budget. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> ### Internal API specification: Illustrative 429 responses
>
> This internal specification covers two illustrative rate-limit responses. The server may choose status code 429. If it sends 429, its content should explain the condition; it may include `Retry-After`. Caches cannot store a 429.
>
> Uppercase requirement keywords have their BCP 14 meanings (RFC 2119 and RFC 8174).
>
> `Retry-After` may contain an HTTP date or a nonnegative delay in seconds measured after receipt (RFC 9110). With synchronized clocks, for a response sent at 09:00:00 UTC and received at 09:00:05 UTC:
>
> - `Retry-After: 45` suggests 09:00:50 UTC.
> - An HTTP date equivalent to 09:01:00 UTC suggests 09:01:00 UTC.
>
> Neither time promises that a retry will succeed or that the service will be available.
>
> **Security considerations:** No additional security consequences are specified.\
> **IANA:** No IANA action is specified.\
> **References:** Normative: RFC 6585, RFC 9110. BCP 14: RFC 2119, RFC 8174.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| States a BCP 14 convention and preserves optional server selection of 429, SHOULD explanatory content, optional Retry-After and the cache's MUST NOT store obligation. | Met | Met |
| Correctly computes 09:00:50 UTC for the 45-second delay after receipt and 09:01:00 UTC for the date value. | Met | Met |
| Frames those times as suggested waits rather than a new client MUST/SHOULD, and states that a retry is not guaranteed to succeed. | Met | Met |

The skill answer and the baseline both declare a BCP 14 convention and preserve server choice, recommended explanatory content, an optional header and the prohibition on caching. The skill answer uses lowercase prose for those rules; the baseline applies its uppercase convention directly. Both suggest 09:00:50 UTC from receipt and 09:01:00 UTC from the date, without imposing a retry obligation or promising success. Both exceed 125 words, including the skill answer’s extra end matter and the baseline’s list of keywords.

**차이.** 스킬 답과 미적용 답 모두 BCP 14 표기 규칙을 선언하고, 상태 코드 선택과 헤더는 선택 사항, 사유 설명은 권고 사항, 캐시 저장은 금지 사항으로 전달한다. 스킬 답은 실제 규칙을 소문자 일반 문장으로 쓰고 미적용 답은 선언한 대문자 키워드를 직접 쓴다. 둘 다 수신 시각 기준 09:00:50 UTC와 날짜값 기준 09:01:00 UTC를 권장 시점으로 제시하며 재시도 의무나 성공을 보장하지 않는다. 스킬 답의 부록과 미적용 답의 키워드 목록을 포함해 두 답 모두 125단어를 넘긴다.

</details>

## imrad

**What ten years of LIGO background would imply for GW150914**

2026-11-08 · `imrad` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [LIGO Scientific Collaboration and Virgo Collaboration, Observation of Gravitational Waves from a Binary Black Hole Merger (2016)](https://dcc.ligo.org/public/0122/P150914/014/LIGO-P150914_Detection_of_GW150914.pdf). Abstract and §V.B, binary coalescence search: event date, two detectors, frequency sweep, peak strain, predicted waveform match and upper bound on the false-alarm rate.

**Reasoning task.** Convert a bound on a search rate to a bound on an expected count; distinguish an expectation from a guarantee and from the posterior probability of a specific event.

### Prompt

> Write a museum research abstract of at most 145 words about LIGO’s GW150914. On 14 September 2015 the Livingston and Hanford instruments recorded a signal rising from 35 to 250 Hz with peak dimensionless strain 1.0 × 10⁻²¹. Researchers found that it matched a predicted binary black-hole merger waveform. The search put its rate of noise candidates at least this significant below one per 203,000 years. An editor concludes: “There would be no false alarms in ten years, so the chance this event was noise is zero.” For an illustrative ten years at the same rate, compute an upper bound on the expected number of such noise candidates. Use the result to assess the editor’s reasoning, while keeping instrument readings, analysis, and interpretation distinct.

### Without a skill

> On 14 September 2015, LIGO’s Livingston and Hanford instruments recorded a signal rising from 35 to 250 Hz, with peak dimensionless strain $1.0 \times 10^{-21}$. In the analysis, researchers found that the signal matched a predicted binary black-hole merger waveform. They estimated that noise candidates at least this significant would occur at a rate below one per 203,000 years. At that upper rate, ten years would yield fewer than $10/203{,}000 \approx 4.9 \times 10^{-5}$ expected noise candidates. This is an upper bound on the expected count, not a guarantee of zero candidates: a rare noise event remains possible. Nor does the rate alone give the probability that this particular event was noise. The editor’s conclusion therefore overstates what the rate establishes.

<details>
<summary>Original model text</summary>

````text
On 14 September 2015, LIGO’s Livingston and Hanford instruments recorded a signal rising from 35 to 250 Hz, with peak dimensionless strain \(1.0 \times 10^{-21}\). In the analysis, researchers found that the signal matched a predicted binary black-hole merger waveform. They estimated that noise candidates at least this significant would occur at a rate below one per 203,000 years. At that upper rate, ten years would yield fewer than \(10/203{,}000 \approx 4.9 \times 10^{-5}\) expected noise candidates. This is an upper bound on the expected count, not a guarantee of zero candidates: a rare noise event remains possible. Nor does the rate alone give the probability that this particular event was noise. The editor’s conclusion therefore overstates what the rate establishes.
````

</details>

### With the skill at standard

> **Introduction.** Detecting gravitational waves directly tests predictions of general relativity. We summarize the observation of GW150914 and assess whether a low background rate makes a noise explanation impossible.
>
> **Methods.** On 14 September 2015, the Livingston and Hanford instruments recorded a signal whose frequency rose from 35 to 250 Hz and whose peak dimensionless strain was 1.0 × 10⁻²¹. Researchers compared the signal with a predicted binary black-hole merger waveform and estimated the rate of noise candidates at least this significant.
>
> **Results.** The signal matched the predicted waveform. The estimated noise-candidate rate was below one per 203,000 years. At that upper rate, the expected number in ten years is less than 10/203,000 ≈ 4.9 × 10⁻⁵.
>
> **Discussion.** This bound indicates a very low expected background count, not zero false alarms or zero probability that this event was noise. An expected count is not a guarantee about what occurs in any particular interval.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly attributes the dated 35–250 Hz, 1.0 × 10⁻²¹ strain signal to both detectors and the waveform comparison to analysis rather than to the detectors. | Met | Met |
| Computes an expected count strictly below 10/203,000 (about 4.93 × 10⁻⁵) over the hypothetical ten years at the stated rate, without labeling it an event probability. | Met | Met |
| Rejects both the guarantee of zero noise candidates and a zero probability for this event; the abstract distinguishes the measured signal from the supported merger interpretation. | Met | Met |

Both distinguish the detectors’ readings from the researchers’ waveform comparison, and give the correct expected-count bound without turning it into a probability for GW150914. The baseline fits the word budget in one paragraph. The skill answer makes the measurement and interpretation easier to find with headings, but exceeds the requested 145 words by whitespace count. The three preregistered checks cover the science rather than the length.

**차이.** 두 답 모두 10년간 기대 오경보 건수가 약 4.93 × 10⁻⁵ 미만임을 구하고, 이를 이 사건이 잡음일 확률과 구분합니다. 미적용 답은 한 문단으로 분량을 지켰고, 스킬 답은 관측과 해석을 제목으로 구분했지만 공백 기준 145단어 제한을 넘겼습니다.

<details>
<summary>Developmental retest · version 0.1.3</summary>

Check the budget for the whole abstract, including section labels. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> **Method: IMRaD, standard level**
>
> **Introduction:** Detecting a gravitational-wave signal requires distinguishing a real astrophysical event from noise. This abstract describes the recorded signal and the search’s estimate of noise-candidate frequency.
>
> **Methods:** On 14 September 2015, the Livingston and Hanford instruments recorded the signal. Researchers compared it with a predicted binary black-hole merger waveform and estimated the rate of noise candidates at least this significant.
>
> **Results:** The signal rose from 35 to 250 Hz and had peak dimensionless strain of 1.0 × 10⁻²¹. It matched the predicted waveform. The estimated noise-candidate rate was below one per 203,000 years. At that upper rate, ten years would yield fewer than 10/203,000 ≈ 4.9 × 10⁻⁵ expected candidates.
>
> **Discussion:** This small expected count supports a low noise-candidate rate, not the editor’s claim of zero false alarms or zero probability that the event was noise. An expected count is not a guarantee that none will occur.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly attributes the dated 35–250 Hz, 1.0 × 10⁻²¹ strain signal to both detectors and the waveform comparison to analysis rather than to the detectors. | Met | Met |
| Computes an expected count strictly below 10/203,000 (about 4.93 × 10⁻⁵) over the hypothetical ten years at the stated rate, without labeling it an event probability. | Met | Met |
| Rejects both the guarantee of zero noise candidates and a zero probability for this event; the abstract distinguishes the measured signal from the supported merger interpretation. | Met | Met |

Both the baseline and the skill answer attribute the dated strain and frequency readings to the two detectors and the merger-waveform match to the analysis. Both bound the expected noise count below 10/203,000 over ten years and reject the editor’s two inferences. The baseline states explicitly that the rate alone cannot determine the probability for this event. The skill answer displays “Method: IMRaD, standard level” before the abstract; including its headings and label puts the delivered text over 145 words.

**차이.** 미적용 답과 스킬 답 모두 두 검출기의 관측 날짜·변형률·주파수를 연구진의 병합 파형 분석과 구분한다. 둘 다 10년간 기대하는 잡음 후보 수가 10/203,000 미만이라고 계산하고 편집자의 두 결론을 부정한다. 미적용 답은 이 비율만으로 개별 사건이 잡음일 확률을 정할 수 없다고 명시한다. 스킬 답에는 초록 앞에 ‘Method: IMRaD, standard level’이 노출되며, 이 표시와 소제목을 포함하면 145단어를 넘는다.

</details>

## korean-plain-language

**Which months qualified for Seoul’s pilot refund?**

2026-11-08 · `korean-plain-language` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [서울특별시 내 손안에 서울, ‘월 5만원대’ 청년 맞춤형 기후동행카드 나온다 (2024-02-21)](https://mediahub.seoul.go.kr/archives/2010350). City's February 2024 announcement, especially the retrospective refund, separate registration rule and monthly eligibility conditions under the original pilot.

**Reasoning task.** Intersect registration timing, completed 30-day periods and refund exclusions before calculating two riders' historical entitlements.

### Prompt

> 2024년 서울시 기후동행카드 시범사업을 돌아보는 전시 문구를 해요체 다섯 문장 이내로 써 주세요. 당시 원칙은 등록한 실물카드의 등록 이후 이용분 또는 별도 등록이 필요 없는 모바일카드 이용분 중, 환불 없이 30일 만기를 채운 달마다 7,000원이었고 두 종류 모두 별도 환급 신청이 필요했어요. 연령 등 나머지 조건은 충족했다고 가정해요. 가상 이용자 지우는 실물카드로 첫 30일권을 미등록 상태에서 끝까지 쓴 뒤 등록하고 둘째 권을 30일 만기로 썼지만 셋째 권은 18일째 환불했어요. 민서는 모바일카드로 30일권 두 장을 환불 없이 끝까지 썼어요. 각각 당시 얼마를 신청할 수 있었는지, 왜 금액이 달랐는지 독자가 따라갈 수 있게 해 주세요.

### Without a skill

> 실물카드를 쓴 지우는 첫 이용권을 다 쓴 뒤 등록했으므로, 등록 전 이용분은 환급 대상이 아니에요. 등록 이후 쓴 둘째 이용권은 30일 만기를 채워 7,000원을 신청할 수 있지만, 셋째 이용권은 18일째 환불해 대상이 아니에요. 따라서 지우가 신청할 수 있는 금액은 7,000원이에요. 모바일카드를 쓴 민서는 등록 없이도 이용분이 인정되므로, 환불 없이 만기를 채운 두 달에 대해 14,000원을 신청할 수 있어요. 두 사람 모두 별도 신청이 필요했고, 차이는 실물카드의 등록 시점과 만기·환불 조건을 충족한 달 수예요.

### With the skill at standard

> 지우는 실물카드 첫 이용분을 다 쓴 뒤 등록했으므로, 등록 전에 이용한 첫 30일권은 환급 대상이 아니에요.\
> 등록 후 이용한 둘째 30일권은 환불 없이 만기를 채웠으므로, 별도 신청을 하면 7,000원을 받을 수 있어요.\
> 셋째 권은 18일째 환불했으므로 만기 조건을 채우지 못해 환급액에 포함되지 않아요.\
> 민서는 등록이 필요 없는 모바일카드로 30일권 두 장을 모두 환불 없이 만기까지 이용해, 별도 신청으로 14,000원을 받을 수 있어요.\
> 따라서 지우는 7,000원, 민서는 14,000원을 신청할 수 있었고, 실물카드는 등록 이후 이용분만 인정된 반면 모바일카드는 등록 전 이용분 제한이 없었기 때문에 금액이 달랐어요.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly gives Jiwoo 7,000 won, counting only the second pass and explaining why the unregistered and refunded passes do not count. | Met | Met |
| Correctly gives Minseo 14,000 won for two completed passes; distinguishes not having to register the mobile card from having to apply for either refund. | Met | Met |
| Maintains 해요체 and the 2024 retrospective scope, without implying automatic payment or ongoing eligibility. | Missed | Missed |

Both calculate 7,000 won for Jiwoo and 14,000 for Minseo, exclude the first and third physical passes for different reasons, and require an application for both. Both keep 해요체, but their statements about what a rider can receive mostly use the present tense without anchoring eligibility to the 2024 pilot. The skill answer closes with a retrospective phrase; the baseline gives the two riders' results in a more compact sequence.

**차이.** 둘 다 지우 7,000원과 민서 14,000원을 정확히 계산하고, 별도 신청이 필요하다고 설명합니다. 스킬 답은 끝에서 과거형으로 정리하지만, 두 답 모두 환급 가능 여부를 주로 현재형으로 써서 2024년 시범사업에 한정된 조건임이 충분히 드러나지 않습니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Carry the historical date into the Korean wording of permission and eligibility. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> 2024년 서울시 기후동행카드 시범사업에서는 등록한 실물카드의 등록 이후 이용분이나 별도 등록이 필요 없는 모바일카드 이용분으로, 환불 없이 30일 만기를 채운 달마다 7,000원을 받을 수 있었어요. 다만 두 종류 모두 별도로 환급 신청을 해야 했어요. 지우는 첫 실물카드 이용분을 다 쓴 뒤 등록했기 때문에 그 이용분은 환급 대상이 아니었고, 둘째 권은 만기를 채워 7,000원을 신청할 수 있었어요. 셋째 권은 18일째 환불했으므로 환급 대상이 아니어서, 지우가 신청할 수 있는 금액은 총 7,000원이었어요. 민서는 모바일카드 두 장 모두 만기를 채우고 환불하지 않아 총 14,000원을 신청할 수 있었어요.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly gives Jiwoo 7,000 won, counting only the second pass and explaining why the unregistered and refunded passes do not count. | Met | Met |
| Correctly gives Minseo 14,000 won for two completed passes; distinguishes not having to register the mobile card from having to apply for either refund. | Met | Met |
| Maintains 해요체 and the 2024 retrospective scope, without implying automatic payment or ongoing eligibility. | Missed | Met |

Both the skill answer and the baseline correctly count only Jiwoo’s second pass (₩7,000), both of Minseo’s passes (₩14,000), and a separate application for each person despite mobile cards needing no registration. Both use five 해요체 sentences. The skill answer names the 2024 pilot and describes what riders could claim then; the baseline omits the historical date and uses present-tense eligibility that can read as current policy.

**차이.** 스킬 답과 미적용 답 모두 지우는 둘째 권만 7,000원, 민서는 두 권 합계 14,000원으로 계산한다. 모바일카드 등록 면제와 두 사람의 별도 환급 신청도 구분하고 해요체 다섯 문장을 쓴다. 스킬 답은 2024년 시범사업 당시 신청할 수 있었던 금액으로 서술한다. 미적용 답은 연도와 시범사업을 생략하고 ‘신청할 수 있어요’ 등 현재형을 써서 현행 제도로 읽힐 수 있다.

</details>

## microsoft-writing-style

**Clearing a Windows clipboard without losing two keepers**

2026-11-08 · `microsoft-writing-style` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Microsoft Support, Using the clipboard](https://support.microsoft.com/en-us/windows/apps/using-the-clipboard). The Windows 11 sections document opening device history, clearing unpinned entries and deleting one selected item. The clipboard contents are hypothetical.

**Reasoning task.** Plan operations that transform mixed pinned and unpinned entries into an exact target set, recognizing a preservation prerequisite and an exception to a bulk action.

### Prompt

> Write Windows 11 help for a person who wants exactly two entries left in this PC's clipboard history. In this example the delivery address and an obsolete access code are pinned; a return reference and two draft notes are unpinned. Keep the address and the return reference, remove the other three, and avoid retyping either keeper. Windows logo key + V opens Clipboard history. You can pin an entry; Clear all removes the unpinned entries. See more (...) then Delete removes a chosen entry. Give one reliable sequence using Clear all, explain which action must come first and how to tell the goal was met. Use the actual controls. They only asked about this PC. Keep the help under 90 words.

### Without a skill

> 1. Press **Windows logo key + V** to open Clipboard history.
> 2. On the pinned obsolete access code, select **See more (…) > Delete** first. This removes it while keeping the pinned delivery address.
> 3. Select **Clear all** to remove the unpinned return reference and two draft notes.
> 4. To keep the return reference without retyping it, copy it again before clearing, then pin it afterward.
>
> Check that only the delivery address and return reference remain.

### With the skill at standard

> Open Clipboard history with **Windows logo key + V**. Pin the delivery address and return reference first. Then select **Clear all** to remove the obsolete access code and two draft notes; **Clear all** removes unpinned entries. Confirm that only the two keepers remain. If you clear before pinning them, they will be removed too.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses Windows logo key + V and pins the return reference before Clear all; keeps the already pinned delivery address. | Missed | Met |
| Uses See more (...) then Delete for the obsolete pinned access code, or expressly unpins it before Clear all so it is removed; does not imply Clear all alone deletes pinned items. | Met | Missed |
| Gives user-facing steps that end with exactly the address and return reference, remove the two drafts and make no unsupported claim about other devices. | Missed | Missed |

Neither procedure leaves exactly the two desired entries. The baseline correctly targets the pinned access code with Delete but clears the still-unpinned return reference; copying it before clearing and pinning afterward does not protect it. The skill answer pins the return reference first but assumes Clear all will delete the obsolete access code even though it remains pinned. Its instruction to pin the already pinned address is redundant.

**차이.** 두 절차 모두 원하는 두 항목만 남기지 못합니다. 미적용 답은 고정된 접근 코드를 개별 삭제하지만 반품 참조번호를 고정하기 전에 지웁니다. 스킬 답은 참조번호를 먼저 고정하지만 여전히 고정된 접근 코드까지 ‘모두 지우기’로 삭제된다고 잘못 설명합니다. 이미 고정된 주소를 다시 고정하라는 단계도 중복입니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Trace the items retained and removed after every operation before writing the final procedure. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> 1. Press **Windows logo key + V** to open Clipboard history.
> 2. Pin the delivery address and the return reference. Confirm both show as pinned.
> 3. Select **Clear all**. This removes the unpinned obsolete access code and two draft notes. The pinned entries remain.
> 4. Select **See more (...)** next to the obsolete access code, then select **Delete**.
> 5. Check Clipboard history: the delivery address and return reference should be the only two entries.
>
> Pin both entries before **Clear all**; otherwise, **Clear all** removes them too. These steps affect this PC’s clipboard history.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Uses Windows logo key + V and pins the return reference before Clear all; keeps the already pinned delivery address. | Missed | Met |
| Uses See more (...) then Delete for the obsolete pinned access code, or expressly unpins it before Clear all so it is removed; does not imply Clear all alone deletes pinned items. | Met | Missed |
| Gives user-facing steps that end with exactly the address and return reference, remove the two drafts and make no unsupported claim about other devices. | Missed | Met |

The baseline explicitly deletes the pinned code, then clears the unpinned return reference before pinning it. Its later instruction to copy the reference again before clearing does not make that sequence reliable. The skill answer instructs the reader to confirm both keepers are pinned, clear the drafts, delete the code individually, and verify the final two entries. Those operations can work, but the skill answer wrongly says the initially pinned code was unpinned and removed by Clear all, immediately before directing the reader to delete it.

**차이.** 미적용 답은 고정된 코드를 개별 삭제하지만 반품 참조를 고정하기 전에 전체 지우기로 지운다. 나중에 지우기 전에 다시 복사하라는 지시로는 이 순서를 신뢰할 수 없다. 스킬 답은 남길 두 항목의 고정을 확인하고 초안을 지운 다음 코드를 개별 삭제하고 최종 두 항목을 확인하도록 한다. 이 조작 순서는 성립하지만, 원래 고정된 코드를 전체 지우기로 이미 지워진 미고정 항목이라고 설명한 직후 그 코드를 삭제하라고 한다.

</details>

## minto-pyramid

**Which crossings should receive the pilot first?**

2026-11-08 · `minto-pyramid` 0.2.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [FHWA, Leading Pedestrian Interval](https://highways.dot.gov/safety/proven-safety-countermeasures/leading-pedestrian-interval). Definition, timing, turning conflicts, visibility, accessibility and applicability at high-turning-volume crossings.
- [FHWA, Safety Evaluation of Protected Left-Turn Phasing and Leading Pedestrian Intervals on Pedestrian Safety (2018), FHWA-HRT-18-044](https://www.fhwa.dot.gov/publications/research/safety/18044/18044.pdf). Executive summary and combined leading-interval evaluation, including the Chicago, New York and Charlotte sites and pedestrian crash modification factor 0.87. The committee decision in the request is hypothetical.

**Reasoning task.** Translate a crash modification factor into absolute expected reductions using two different baselines, then separate the decision forecast from an observed local effect.

### Prompt

> Write a city committee's decision opening in at most 100 words. It can fund one pilot at a group of signalized crossings with heavy turning traffic; either group costs the same and the goal is to avert the larger expected number of vehicle–pedestrian crashes. WALK would begin 3–7 seconds before drivers get green. In FHWA's three-city study the estimated crash modification factor was 0.87. In this hypothetical comparison, without treatment North's crossings are expected to have 20 such crashes and South's 5 over the same period. Estimate what difference applying the study factor would make at each group. Recommend a site and say what comparison the committee should make before treating this forecast as a local result.

### Without a skill

> The committee recommends the North crossings for the pilot. Applying FHWA’s estimated crash modification factor of 0.87 implies a 13% reduction: about 2.6 fewer vehicle–pedestrian crashes in North, compared with 0.65 fewer in South over the same period. These are forecast differences, not local results. Before treating them as local evidence, compare treated crossings with similar untreated crossings over the same period, accounting for baseline crash risk and changes in traffic and pedestrian volumes.

### With the skill at standard

> The committee can fund one pilot at either group of signalized crossings, at the same cost. Which would avert more vehicle–pedestrian crashes, and what should be checked before treating the estimate as a local forecast?
>
> Use the FHWA study factor of 0.87, which implies an estimated 13% reduction: about 2.6 fewer crashes at North (20 × 0.13) versus 0.65 at South (5 × 0.13) over the same period. **Recommend North** to target the larger expected reduction. Before treating this as a local result, compare the study’s three-city sites and conditions with the proposed crossings, especially their traffic and crash patterns.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly derives expected reductions of 2.6 at North and 0.65 at South (or gives both treated counts and these reductions). | Met | Met |
| Recommends North under the stated equal-cost objective and explains how the early WALK relates to turning vehicles or pedestrian visibility. | Missed | Missed |
| Labels the estimates conditional on transfer from the study and proposes a local treated-versus-credible-without-treatment comparison to test the effect. | Met | Missed |

Both recommend North and correctly forecast 2.6 versus 0.65 fewer crashes; neither explains how starting WALK before drivers get green helps at turning conflicts. The baseline proposes measuring treated crossings against comparable untreated crossings locally. The skill answer checks how similar the city is to the source-study sites, which helps judge transfer but cannot measure the pilot's local effect.

**차이.** 두 답 모두 North를 권고하고 예상 감소량 2.6건과 0.65건을 구했지만, 보행 신호를 먼저 주는 원리는 설명하지 않았습니다. 미적용 답은 시범 교차로와 지역 내 미시행 교차로를 비교하자고 합니다. 스킬 답의 기존 연구 도시와의 비교만으로는 해당 도시의 실제 효과를 측정할 수 없습니다.

<details>
<summary>Developmental retest · version 0.2.2</summary>

Distinguish transfer from an external study from the local comparison needed to test the forecast. The prompt now asks for the mechanism explicitly. This retest is excluded from the first-pass counts.

**Revised request (both answers regenerated)**

> Write a city committee's decision opening in at most 100 words. It can fund one pilot at a group of signalized crossings with heavy turning traffic; either group costs the same and the goal is to avert the larger expected number of vehicle–pedestrian crashes. WALK would begin 3–7 seconds before drivers get green. In FHWA's three-city study the estimated crash modification factor was 0.87. In this hypothetical comparison, without treatment North's crossings are expected to have 20 such crashes and South's 5 over the same period. Estimate what difference applying the study factor would make at each group. Recommend a site, explain why the head start might matter at turns, and specify a local comparison that could measure the effect of the pilot against what would have happened without it.

**New baseline**

> The committee should fund the pilot at North’s crossings. Applying FHWA’s estimated crash modification factor of 0.87 suggests about 2.6 fewer vehicle–pedestrian crashes at North (20 × 13%) over the period, compared with about 0.65 fewer at South (5 × 13%). The 3–7-second WALK head start may give pedestrians time to enter the crossing and become more visible before turning drivers receive green. To assess the pilot, compare North’s post-installation crash experience with its expected no-treatment outcome, using matched untreated crossings and pre-pilot trends to account for changes over time.

**New standard answer**

> **Fund one pilot at North.** Without treatment, North is expected to have 20 vehicle–pedestrian crashes over the period, compared with 5 at South. Applying the study’s estimated crash modification factor of 0.87 implies about 2.6 fewer crashes at North (20 × 0.13), versus 0.65 at South (5 × 0.13). These are estimates, not guaranteed local outcomes.
>
> Starting WALK 3–7 seconds before drivers get green may let pedestrians enter the crossing and become more visible before turning vehicles move.
>
> To measure the pilot’s local effect, compare North’s before-and-after crash change with the change over the same periods at comparable untreated signalized crossings, accounting for traffic and other changes. The study factor estimates expected impact; it does not establish what would have happened locally.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Correctly derives expected reductions of 2.6 at North and 0.65 at South (or gives both treated counts and these reductions). | Met | Met |
| Recommends North under the stated equal-cost objective and explains how the early WALK relates to turning vehicles or pedestrian visibility. | Met | Met |
| Labels the estimates conditional on transfer from the study and proposes a local treated-versus-credible-without-treatment comparison to test the effect. | Met | Met |

Both the baseline and the skill answer apply the study estimate conditionally and obtain 2.6 fewer expected crashes at North versus 0.65 at South. Both recommend North, explain how the WALK head start can make pedestrians visible to turning drivers, and propose a comparison with untreated crossings over time. The baseline fits 100 words. The skill answer explicitly distinguishes the estimates from local outcomes and describes a before-and-after comparison, but exceeds 100 words.

**차이.** 미적용 답과 스킬 답 모두 연구 추정치를 적용했을 때 예상 사고 감소가 북쪽 2.6건과 남쪽 0.65건이라고 계산한다. 둘 다 북쪽을 권하고, 보행 신호를 먼저 주면 회전 운전자에게 보행자가 잘 보이는 이유와 미시행 횡단보도를 활용한 시기별 비교를 제시한다. 미적용 답은 100단어 이내다. 스킬 답은 추정치와 지역의 실제 결과를 명시적으로 구별하고 전후 비교를 설명하지만 100단어를 넘긴다.

</details>

## new-harts-rules

**Correcting a percentage-point claim for a UK census exhibit**

2026-11-08 · `new-harts-rules` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Office for National Statistics, Housing, England and Wales: Census 2021 (5 January 2023)](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/housingenglandandwales/census2021). Section 6, Car or van availability, and title: 42.1% of London households versus 23.3% across England and Wales in 2021. Exhibition style and draft are original exercise inputs.

**Reasoning task.** Correct the denominator and distinguish an absolute percentage-point difference from a relative percentage change, while protecting quoted material and the source of editorial choices.

### Prompt

> Copyedit this UK exhibition label and append one short editorial note. Original draft: ‘In “Housing, England and Wales: Census 2021”, ONS showed that 42.1% of Londoners lacked a car in 2021, 18.8 per cent more than across England and Wales.’ The bulletin reports households with no car or van available: 42.1% in London and 23.3% across England and Wales. The editor needs both the percentage-point gap and the relative excess over the England-and-Wales share (round that excess to the nearest whole per cent). House style spells out ‘per cent’ in prose; keep the ONS title verbatim. No passage from New Hart's Rules was supplied. Keep the edited sentence intelligible to a visitor who might otherwise confuse the two comparisons.

### Without a skill

> In “Housing, England and Wales: Census 2021”, ONS reported that 42.1% of London households had no car or van available, compared with 23.3% across England and Wales—a gap of 18.8 percentage points. London’s share was 81 per cent higher than the England-and-Wales share.
>
> Editorial note: The 18.8-point gap is the difference between the two shares; the 81 per cent figure is London’s relative excess over the England-and-Wales share.

### With the skill at standard

> In “Housing, England and Wales: Census 2021”, ONS showed that 42.1 per cent of London households had no car or van available in 2021, compared with 23.3 per cent across England and Wales. That is an 18.8 percentage-point gap, or 81 per cent higher than the England-and-Wales share.
>
> **Editorial note:** House style spells out “per cent”; the ONS title remains verbatim. The New Hart’s Rules second edition (2014) is identified, but no relevant passage was supplied, so no book-specific rule is claimed.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Keeps the title 'Housing, England and Wales: Census 2021' verbatim and the measurements at the household level, including no car or van available. | Met | Met |
| Uses 18.8 percentage points and about 81 per cent relative excess over 23.3%, keeping the measures distinct. | Met | Met |
| Uses 'per cent' in prose and gives a short editorial note identifying the house style or evidential basis without claiming verification from the book. | Missed | Met |

Both preserve the bulletin title and household denominator and distinguish 18.8 percentage points from an approximately 81 per cent relative excess. The skill answer writes out ‘per cent’ throughout and attributes the convention to house style. The baseline leaves 42.1% and 23.3% as symbols in prose despite the exhibition instruction.

**차이.** 두 답 모두 가구 단위, 원제, 18.8%포인트 차이와 약 81%의 상대 차이를 보존합니다. 스킬 답은 ‘per cent’를 일관되게 쓰고 전시 표기 지침임을 밝힙니다. 미적용 답은 본문의 42.1%와 23.3%에 기호를 남겼습니다.

## nist-technical-publication

**Which improvement would reduce the uncertainty of NIST-F2 more?**

2026-11-08 · `nist-technical-publication` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Heavner et al., First Accuracy Evaluation of NIST-F2, Metrologia (2014)](https://www.nist.gov/publications/first-accuracy-evaluation-nist-f2). Authors' abstract, including the July–August 2013 Type A and Type B fractional uncertainties, the 80 K interrogation environment and the reason for the dominant Type B contribution.

**Reasoning task.** Propagate independent uncertainties, compare two counterfactual interventions, and distinguish a reduction in a single physical contribution from a change in the total.

### Prompt

> Prepare a short technical note for a metrology lab deciding which component to improve in NIST-F2. In the July–August 2013 evaluation, Type A statistical fractional frequency uncertainty was 0.44 × 10⁻¹⁵ and Type B systematic uncertainty was 0.11 × 10⁻¹⁵. The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold; microwave-amplitude effects dominated Type B. For this comparison only, assume the two components are independent, combine them by root-sum-square, and compare two equally costly hypothetical upgrades: halve Type A alone or halve Type B alone. Show the present and both projected combined uncertainties, recommend one upgrade on this metric, and state why cooling by itself does not establish a fiftyfold improvement in overall uncertainty.

### Without a skill

> ### NIST-F2 uncertainty improvement
>
> Using the stated independence assumption, combine Type A and Type B uncertainties by root-sum-square:
>
>
> $$
> u_{\text{combined}}=\sqrt{u_A^2+u_B^2}.
> $$
>
>
> | Scenario | Type A | Type B | Combined uncertainty |
> |---|---:|---:|---:|
> | Present | 0.44 | 0.11 | **0.454** |
> | Halve Type A | 0.22 | 0.11 | **0.246** |
> | Halve Type B | 0.44 | 0.055 | **0.443** |
>
> All values are in $10^{-15}$ fractional frequency uncertainty.
>
> For an equally costly upgrade, **halve Type A**: it lowers the combined uncertainty substantially more (to about $0.246\times10^{-15}$, versus $0.443\times10^{-15}$ for halving Type B).
>
> The more-than-fiftyfold reduction from the 80 K environment applies to the blackbody-radiation uncertainty contribution. It does not imply the same reduction in overall uncertainty: other contributions remain, and microwave-amplitude effects dominate Type B.

<details>
<summary>Original model text</summary>

````text
### NIST-F2 uncertainty improvement

Using the stated independence assumption, combine Type A and Type B uncertainties by root-sum-square:

\[
u_{\text{combined}}=\sqrt{u_A^2+u_B^2}.
\]

| Scenario | Type A | Type B | Combined uncertainty |
|---|---:|---:|---:|
| Present | 0.44 | 0.11 | **0.454** |
| Halve Type A | 0.22 | 0.11 | **0.246** |
| Halve Type B | 0.44 | 0.055 | **0.443** |

All values are in \(10^{-15}\) fractional frequency uncertainty.

For an equally costly upgrade, **halve Type A**: it lowers the combined uncertainty substantially more (to about \(0.246\times10^{-15}\), versus \(0.443\times10^{-15}\) for halving Type B).

The more-than-fiftyfold reduction from the 80 K environment applies to the blackbody-radiation uncertainty contribution. It does not imply the same reduction in overall uncertainty: other contributions remain, and microwave-amplitude effects dominate Type B.
````

</details>

### With the skill at standard

> ## Technical note: Upgrade priority for NIST-F2
>
> **Purpose.** Compare two equally costly hypothetical upgrades using combined fractional frequency uncertainty as the decision metric.
>
> **Basis.** In the July–August 2013 evaluation, Type A statistical uncertainty was $0.44 \times 10^{-15}$, and Type B systematic uncertainty was $0.11 \times 10^{-15}$. For this comparison, the components are assumed independent and combined by root-sum-square (RSS):
>
>
> $$
> u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
> $$
>
>
> **Results.** The present combined uncertainty is $0.454 \times 10^{-15}$. Halving Type A alone gives $0.232 \times 10^{-15}$; halving Type B alone gives $0.427 \times 10^{-15}$. Values are rounded to three significant figures.
>
> | Case | Type A ($\times 10^{-15}$) | Type B ($\times 10^{-15}$) | Combined RSS uncertainty ($\times 10^{-15}$) |
> |---|---:|---:|---:|
> | Present | 0.44 | 0.11 | 0.454 |
> | Halve Type A | 0.22 | 0.11 | 0.232 |
> | Halve Type B | 0.44 | 0.055 | 0.427 |
>
> **Recommendation.** On the combined-uncertainty metric, prioritize halving Type A: it lowers the projected combined uncertainty more than halving Type B.
>
> The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold, while microwave-amplitude effects dominated Type B. That reduction applies to the blackbody-radiation contribution; it does not establish a fiftyfold reduction in overall uncertainty, which also includes Type A and other Type B contributions.
>
> **Method record.** Applied the NIST-inspired technical-publication method, version 0.1.2, at standard level. Assumed the stated independence and RSS combination for this comparison only. No figures or tables were supplied for audit.

<details>
<summary>Original model text</summary>

````text
## Technical note: Upgrade priority for NIST-F2

**Purpose.** Compare two equally costly hypothetical upgrades using combined fractional frequency uncertainty as the decision metric.

**Basis.** In the July–August 2013 evaluation, Type A statistical uncertainty was \(0.44 \times 10^{-15}\), and Type B systematic uncertainty was \(0.11 \times 10^{-15}\). For this comparison, the components are assumed independent and combined by root-sum-square (RSS):

\[
u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
\]

**Results.** The present combined uncertainty is \(0.454 \times 10^{-15}\). Halving Type A alone gives \(0.232 \times 10^{-15}\); halving Type B alone gives \(0.427 \times 10^{-15}\). Values are rounded to three significant figures.

| Case | Type A (\(\times 10^{-15}\)) | Type B (\(\times 10^{-15}\)) | Combined RSS uncertainty (\(\times 10^{-15}\)) |
|---|---:|---:|---:|
| Present | 0.44 | 0.11 | 0.454 |
| Halve Type A | 0.22 | 0.11 | 0.232 |
| Halve Type B | 0.44 | 0.055 | 0.427 |

**Recommendation.** On the combined-uncertainty metric, prioritize halving Type A: it lowers the projected combined uncertainty more than halving Type B.

The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold, while microwave-amplitude effects dominated Type B. That reduction applies to the blackbody-radiation contribution; it does not establish a fiftyfold reduction in overall uncertainty, which also includes Type A and other Type B contributions.

**Method record.** Applied the NIST-inspired technical-publication method, version 0.1.2, at standard level. Assumed the stated independence and RSS combination for this comparison only. No figures or tables were supplied for audit.
````

</details>

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the Type A/B values with labels and fractional units and derives a current combined value near 0.454 × 10⁻¹⁵ under the stated independence assumption. | Met | Met |
| Correctly calculates both hypothetical totals (about 0.246 × 10⁻¹⁵ if Type A halves and 0.443 × 10⁻¹⁵ if Type B halves) and favors Type A for the larger reduction at equal cost. | Met | Missed |
| Keeps the projections separate from the 2013 observations, bounds the fiftyfold reduction to the blackbody contribution, and identifies microwave amplitude as the dominant Type B effect. | Met | Met |

Both compute the current combined uncertainty and recommend reducing Type A. The baseline’s two projected values are 0.246 and 0.443 (in units of 10⁻¹⁵); the skill answer’s 0.232 and 0.427 do not follow from the RSS formula or from its own table inputs. The skill answer also appends an unrequested method/version record, which makes the condition potentially identifiable. Both correctly limit the fiftyfold improvement to the blackbody contribution.

**차이.** 두 답 모두 현재 합성 불확도와 개선 순위는 맞았습니다. 그러나 스킬 답은 올바른 식과 입력을 적고도 가상 개선 후 두 값을 잘못 계산했습니다. 미적용 답의 0.246과 0.443(각각 × 10⁻¹⁵)이 맞습니다. 스킬 답에는 요청하지 않은 방법명·버전도 드러났습니다.

<details>
<summary>Developmental retest · version 0.1.3</summary>

Recalculate derived values under each counterfactual, verify them against the defining relation and keep audit details out of the report. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> ## NIST-F2: uncertainty reduction options
>
> **Basis.** In the July–August 2013 evaluation, Type A statistical fractional frequency uncertainty was $0.44 \times 10^{-15}$, and Type B systematic uncertainty was $0.11 \times 10^{-15}$. The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold; microwave-amplitude effects dominated Type B.
>
> **Comparison.** Assuming the two components are independent, the combined uncertainty is their root-sum-square (RSS):
>
>
> $$
> u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
> $$
>
>
> | Case | Type A ($\times 10^{-15}$) | Type B ($\times 10^{-15}$) | Combined RSS ($\times 10^{-15}$) |
> |---|---:|---:|---:|
> | Present | 0.44 | 0.11 | 0.454 |
> | Halve Type A | 0.22 | 0.11 | 0.246 |
> | Halve Type B | 0.44 | 0.055 | 0.443 |
>
> Values are rounded to three significant figures after calculation. For example, the present value is $\sqrt{0.44^2+0.11^2}=0.4535\ldots$; squaring the rounded result gives approximately $0.206$, consistent with $0.44^2+0.11^2=0.206$.
>
> **Recommendation.** On combined uncertainty alone, choose the upgrade that halves Type A: it reduces the projected combined uncertainty to $0.246 \times 10^{-15}$, compared with $0.443 \times 10^{-15}$ for halving Type B. This comparison assumes the stated independence and equal upgrade cost.
>
> Cooling alone does not establish a fiftyfold improvement in overall uncertainty. The more-than-fiftyfold reduction applies to the blackbody-radiation uncertainty component; microwave-amplitude effects dominate Type B, and Type A also contributes. The overall result depends on the combined components, not on the blackbody component alone.

<details>
<summary>Original model text</summary>

````text
## NIST-F2: uncertainty reduction options

**Basis.** In the July–August 2013 evaluation, Type A statistical fractional frequency uncertainty was \(0.44 \times 10^{-15}\), and Type B systematic uncertainty was \(0.11 \times 10^{-15}\). The 80 K environment reduced the blackbody-radiation uncertainty by more than fiftyfold; microwave-amplitude effects dominated Type B.

**Comparison.** Assuming the two components are independent, the combined uncertainty is their root-sum-square (RSS):

\[
u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
\]

| Case | Type A (\(\times 10^{-15}\)) | Type B (\(\times 10^{-15}\)) | Combined RSS (\(\times 10^{-15}\)) |
|---|---:|---:|---:|
| Present | 0.44 | 0.11 | 0.454 |
| Halve Type A | 0.22 | 0.11 | 0.246 |
| Halve Type B | 0.44 | 0.055 | 0.443 |

Values are rounded to three significant figures after calculation. For example, the present value is \(\sqrt{0.44^2+0.11^2}=0.4535\ldots\); squaring the rounded result gives approximately \(0.206\), consistent with \(0.44^2+0.11^2=0.206\).

**Recommendation.** On combined uncertainty alone, choose the upgrade that halves Type A: it reduces the projected combined uncertainty to \(0.246 \times 10^{-15}\), compared with \(0.443 \times 10^{-15}\) for halving Type B. This comparison assumes the stated independence and equal upgrade cost.

Cooling alone does not establish a fiftyfold improvement in overall uncertainty. The more-than-fiftyfold reduction applies to the blackbody-radiation uncertainty component; microwave-amplitude effects dominate Type B, and Type A also contributes. The overall result depends on the combined components, not on the blackbody component alone.
````

</details>

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the Type A/B values with labels and fractional units and derives a current combined value near 0.454 × 10⁻¹⁵ under the stated independence assumption. | Met | Met |
| Correctly calculates both hypothetical totals (about 0.246 × 10⁻¹⁵ if Type A halves and 0.443 × 10⁻¹⁵ if Type B halves) and favors Type A for the larger reduction at equal cost. | Met | Met |
| Keeps the projections separate from the 2013 observations, bounds the fiftyfold reduction to the blackbody contribution, and identifies microwave amplitude as the dominant Type B effect. | Met | Met |

The baseline and the skill answer both apply root-sum-square under independence, give present, A-halved and B-halved fractional uncertainties of 0.454, 0.246 and 0.443 × 10⁻¹⁵, and choose A at equal cost. Both limit the more-than-fiftyfold improvement to blackbody-radiation uncertainty and identify microwave amplitude as the dominant Type B effect. The skill answer identifies the 2013 evaluation explicitly; the baseline distinguishes the scenarios with table labels.

**차이.** 미적용 답과 스킬 답 모두 독립성을 가정해 제곱합의 제곱근을 구한다. 현재와 A 또는 B를 절반으로 줄인 경우의 상대 불확도는 각각 0.454, 0.246, 0.443 × 10⁻¹⁵이며 비용이 같으면 A를 선택한다. 둘 다 50배가 넘는 감소를 흑체복사 불확도에 한정하고, B형의 지배적 요인으로 마이크로파 진폭을 든다. 스킬 답은 2013년 평가임을 명시하고 미적용 답은 표의 행으로 현재와 가상 조건을 구분한다.

</details>

## orwell-six-rules

**What a unit mix-up did to the Mars Climate Orbiter estimate**

2026-11-08 · `orwell-six-rules` 0.1.2 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Cornelius J. Dennehy / NASA, Best Practices for the Design, Development, and Operation of Robust and Reliable Space Vehicle Guidance, Navigation, and Control Systems (NASA/TP–20230005922, April 2023)](https://ntrs.nasa.gov/api/citations/20230005922/downloads/20230005922.pdf). Appendix A-12, pp. 138–139, and lesson 0641: ground software/interface units, trajectory about 170 km low, and two possible outcomes after loss.

**Reasoning task.** Translate an impulse into the interface's units, compare the mistaken and correct readings, and distinguish an error in an estimate from a proved spacecraft fate.

### Prompt

> Rewrite this museum label in at most 95 words. Draft: ‘Operational misalignment effectuated a 170-km plunge. SM_FORCES supplied thruster impulses in pound-force seconds, which navigation read as newton-seconds. The craft burned up.’ The real 1999 navigation estimate accumulated error and the spacecraft approached Mars about 170 km lower than planned. NASA could not distinguish destruction in the atmosphere from escape into a solar orbit. To make the unit error concrete, use a clearly labelled illustrative impulse of 2 pound-force seconds. For this exercise use 1 pound-force second ≈ 4.45 newton-seconds. Work out what the number should have meant to navigation and how far its reading was off. Keep the illustration separate from the reported mission outcome.

### Without a skill

> A 1999 navigation estimate accumulated error, bringing the spacecraft about 170 km lower over Mars than planned. NASA could not tell whether it burned up in the atmosphere or escaped into solar orbit.
>
> **Illustrative unit error:** A thruster impulse of 2 pound-force seconds should have meant about 8.9 newton-seconds to navigation. Read as only 2 newton-seconds, it was off by 6.9 newton-seconds.

### With the skill at standard

> A 1999 navigation estimate accumulated error, bringing the spacecraft about 170 km lower over Mars than planned. NASA could not tell whether it was destroyed in the atmosphere or escaped into solar orbit.
>
> **Illustrative unit error:** An impulse of 2 pound-force seconds equals about 8.9 newton-seconds. Navigation read it as 2 newton-seconds—about 6.9 newton-seconds too low. This example illustrates the unit mismatch; it does not establish what happened to the spacecraft.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| For the illustrative impulse, gives about 8.9 newton-seconds rather than the 2 read by navigation, with an understatement of about 6.9 newton-seconds or a factor of about 4.45. | Met | Met |
| Keeps the hypothetical impulse distinct from the mission record and attributes the roughly 170 km difference to the accumulated trajectory-estimate error/low approach rather than to a known plunge. | Met | Met |
| Retains both possible fates and makes the causal sequence understandable to a museum visitor in no more than 95 words. | Met | Met |

Both correctly convert the illustrative 2 pound-force seconds to about 8.9 newton-seconds, give the 6.9 newton-second understatement and preserve the low approach and two possible fates. The skill answer adds an explicit sentence separating the example from the spacecraft's fate. Neither identifies SM_FORCES as the ground program in the supplied draft.

**차이.** 두 답 모두 예시의 올바른 값 8.9뉴턴초와 과소평가분 6.9뉴턴초를 구하고 탐사선의 두 가능한 최후를 보존합니다. 스킬 답은 예시로 실제 최후를 판정할 수 없다고 한 번 더 밝힙니다. 둘 다 원문의 지상 프로그램 이름은 생략했습니다.

<details>
<summary>Developmental retest · version 0.1.3</summary>

Retain identifiers that a reader needs to locate the relevant program, object or source. This retest is excluded from the first-pass counts.

The request and original baseline are unchanged.

**New standard answer**

> The 1999 Mars mission’s navigation estimate accumulated error, bringing the spacecraft about 170 km lower than planned. NASA could not tell whether it burned up in the atmosphere or escaped into solar orbit.
>
> **Illustration, not a mission measurement:** An impulse of 2 pound-force seconds should have meant about 8.9 newton-seconds to navigation. If read as 2 newton-seconds, it was short by about 6.9 newton-seconds.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| For the illustrative impulse, gives about 8.9 newton-seconds rather than the 2 read by navigation, with an understatement of about 6.9 newton-seconds or a factor of about 4.45. | Met | Met |
| Keeps the hypothetical impulse distinct from the mission record and attributes the roughly 170 km difference to the accumulated trajectory-estimate error/low approach rather than to a known plunge. | Met | Met |
| Retains both possible fates and makes the causal sequence understandable to a museum visitor in no more than 95 words. | Missed | Missed |

Both the skill answer and the baseline separate the illustrative impulse from the mission, calculate 8.9 newton-seconds and a 6.9 newton-second shortfall, give the low approach of about 170 km, and retain both possible fates within 95 words. Neither says that the actual mission supplied impulses in pound-force seconds and navigation interpreted those numbers as newton-seconds. The reader must infer what caused the real estimate to drift from a separately marked illustration.

**차이.** 스킬 답과 미적용 답 모두 가상 충격량과 실제 임무를 구분하고, 올바른 값 8.9뉴턴초와 부족분 6.9뉴턴초를 계산한다. 실제 접근 고도가 계획보다 약 170km 낮았다는 점과 두 가지 가능한 최후도 95단어 안에 담는다. 그러나 둘 다 실제 임무에서 파운드힘초로 전달한 수치를 항법 측이 뉴턴초로 해석했다고 밝히지 않는다. 독자가 별도로 표시한 예시에서 실제 궤도 추정 오차의 원인을 유추해야 한다.

</details>

## socratic-self-questioning

**Can Finland’s basic-income result justify a forecast for 500 workers?**

2026-11-08 · `socratic-self-questioning` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [Finnish Ministry of Social Affairs and Health and Kela, Results of the basic income experiment (6 May 2020)](https://valtioneuvosto.fi/en/-/1271139/perustulokokeilun-tulokset-tyollisyysvaikutukset-vahaisia-toimeentulo-ja-psyykkinen-terveys-koettiin-paremmaksi?languageId=en_US). Employment results and experiment design: participating population, €560 payment, November 2017–October 2018 comparison, first-year finding, and asymmetric 2018 activation-policy change.

**Reasoning task.** Recover the comparison mean and extrapolated total, then distinguish statistical arithmetic, causal identification and transfer to a different population.

### Prompt

> A policy brief predicts ‘If we pay 500 local residents, their employment will rise by 3,000 days.’ Evaluate this inference in a finished paragraph of at most 110 words. In Finland's 2017–2018 experiment, 2,000 randomly selected unemployed benefit recipients got €560 per month. During November 2017–October 2018 recipients averaged 78 employment days, six more than the comparison group. Year one showed no group-level employment effect. A 2018 unemployment-benefit reform affected the groups differently, so researchers could not separate that reform's effect from the second-year basic-income effect. Reconstruct the arithmetic behind the forecast and explain what would have to be true for it to apply locally.

### Without a skill

> The forecast likely multiplies Finland’s second-year difference—six additional employment days per recipient—by 500 residents, yielding 3,000 days. But that arithmetic is not a local prediction: Finland’s first year showed no group-level employment effect, and the second-year estimate cannot be separated from the 2018 benefit reform, which affected the groups differently. Applying it locally would require the six-day difference to represent a causal basic-income effect, and for local recipients, benefit rules, labor markets, payment levels, and follow-up period to be sufficiently comparable. Without that evidence, 3,000 days is an extrapolation, not an established expected gain.

### With the skill at standard

> The forecast appears to scale Finland’s second-year difference of six employment days per recipient to 500 residents: 500 × 6 = 3,000 days. But “six more” was an average difference from the comparison group, not proof that basic income caused six extra days for each recipient. Year one showed no group-level employment effect, and in year two a benefit reform affected the groups differently, so researchers could not isolate the basic-income effect. The local forecast would require the six-day difference to represent a causal effect that transfers to these residents under a comparable payment, population, period, and policy context. The Finnish results alone do not establish that.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Recovers a comparison mean of 72 days and identifies 3,000 as 500 times the six-day observed difference, not an observed local gain. | Missed | Missed |
| Addresses both the lack of a first-year group-level effect and the asymmetric 2018 reform as a reason the second-year difference does not isolate basic income's effect. | Met | Met |
| Limits the evidence to unemployed benefit recipients and identifies a transfer assumption for 500 local residents, without claiming the experiment proves no effect in any year. | Missed | Missed |

Both recover 500 × 6 = 3,000, reject a guaranteed local gain, and explain the null first-year result and the asymmetric benefit reform. Neither gives the comparison mean of 72 days required by the rubric, although it isn't necessary to reconstruct the forecast itself. Both mention transfer assumptions but leave out that the Finnish participants were unemployed benefit recipients. The skill answer specifies a comparable payment, population and period; the baseline also mentions labour markets.

**차이.** 두 답 모두 500×6=3,000을 복원하고 1년 차 결과와 2년 차 제도 변경을 설명합니다. 다만 채점 기준에 있던 비교집단 평균 72일은 그 곱셈에 직접 필요하지 않아 둘 다 쓰지 않았습니다. 지역으로 일반화하려면 집단이 비슷해야 한다고 말하면서, 핀란드 참여자가 실업급여 수급자였다는 점도 명시하지 않았습니다.

<details>
<summary>Developmental retest · version 0.1.2</summary>

Identify who was studied before transferring the finding to a new population. The clarified prompt explicitly requests the comparison-group mean. This retest is excluded from the first-pass counts.

**Revised request (both answers regenerated)**

> A policy brief predicts ‘If we pay 500 local residents, their employment will rise by 3,000 days.’ Evaluate this inference in a finished paragraph of at most 110 words. In Finland's 2017–2018 experiment, 2,000 randomly selected unemployed benefit recipients got €560 per month. During November 2017–October 2018 recipients averaged 78 employment days, six more than the comparison group. Year one showed no group-level employment effect. A 2018 unemployment-benefit reform affected the groups differently, so researchers could not separate that reform's effect from the second-year basic-income effect. Identify the comparison group’s mean employment days, show how the forecast total was derived and explain what would have to be true for it to apply locally.

**New baseline**

> The comparison group averaged 72 employment days (78 minus six). The forecast appears to apply the estimated six-day difference to 500 people: 500 × 6 = 3,000 additional employment days. But Finland’s first year showed no group-level employment effect, and the second-year estimate cannot be separated from the effect of a benefit reform that affected the groups differently. The forecast therefore treats an uncertain, context-specific estimate as causal and transferable. For it to apply locally, paying 500 residents would need to produce the same six-day average increase there, under comparable conditions, with no offsetting effects.

**New standard answer**

> The forecast assumes a gain of six employment days per person: 500 residents × 6 days = 3,000 days. In Finland’s 2017–2018 experiment, recipients averaged 78 employment days, six more than the comparison group, whose mean was therefore 72 days. But year one showed no group-level employment effect, and in year two a benefit reform affected the groups differently, so researchers could not isolate basic income’s effect. The six-day difference is an observed comparison, not a settled causal effect. Applying it locally would require the local residents and program to be comparable to the Finnish participants and conditions, and the difference to reflect the payment rather than other factors.

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Recovers a comparison mean of 72 days and identifies 3,000 as 500 times the six-day observed difference, not an observed local gain. | Met | Met |
| Addresses both the lack of a first-year group-level effect and the asymmetric 2018 reform as a reason the second-year difference does not isolate basic income's effect. | Met | Met |
| Limits the evidence to unemployed benefit recipients and identifies a transfer assumption for 500 local residents, without claiming the experiment proves no effect in any year. | Missed | Missed |

The baseline and the skill answer both recover the 72-day comparison mean, derive 3,000 as 500 times the six-day observed difference, and explain the null first-year group result and differential second-year reform. Both describe conditions for local transfer, but neither identifies the original population as unemployed benefit recipients. The skill answer’s sentence giving the 78-day mean names the experiment’s full 2017–2018 span without specifying the November 2017–October 2018 measurement period.

**차이.** 미적용 답과 스킬 답 모두 비교집단 평균 72일을 구하고, 3,000일이 관측 차이 6일에 500명을 곱한 외삽임을 밝힌다. 첫해 집단 수준 효과가 관찰되지 않은 점과 둘째 해 제도 개편의 집단별 영향도 설명한다. 둘 다 지역 적용 조건은 제시하지만 원래 모집단이 실업급여 수급자였다고 밝히지 않는다. 스킬 답은 평균 78일을 설명하는 문장에서 실험 전체인 2017~2018년을 언급하면서 측정 기간인 2017년 11월~2018년 10월은 명시하지 않는다.

</details>

## steve-jobs-presentation

**What Ingenuity’s hover time can and cannot tell an audience**

2026-11-08 · `steve-jobs-presentation` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [NASA, NASA’s Ingenuity Mars Helicopter Succeeds in Historic First Flight (April 19, 2021)](https://www.nasa.gov/news-release/nasas-ingenuity-mars-helicopter-succeeds-in-historic-first-flight/). Flight-day report: onboard control, altimeter-derived height and hover, total time, the airfield name and plans to analyze the data.

**Reasoning task.** Calculate a meaningful time fraction, diagnose an invalid speed estimate that mixes flight phases, and turn a limited observation into a supported presentation decision.

### Prompt

> Write three short speaker beats for a museum briefing as of 19 April 2021. Ingenuity flew autonomously at Wright Brothers Field on Mars to about 3 m, hovered for 30 seconds, and landed 39.1 seconds after takeoff. The flight proves powered, controlled flight on another planet. A proposed slide calls 3 m divided by the whole flight time 'the average climb speed.' Decide whether to use that metric. Give the audience a defensible proportion for time spent hovering and explain why the remaining time does or does not identify climb speed. Close with what the team could decide after reviewing flight data; do not assume a later test succeeded.

### Without a skill

> **What happened:** On 19 April 2021, Ingenuity flew autonomously at Wright Brothers Field on Mars, rose to about 3 m, hovered for 30 seconds, then landed 39.1 seconds after takeoff. It demonstrated powered, controlled flight on another planet.
>
> **How to describe the timing:** I would not call 3 m divided by 39.1 seconds the “average climb speed.” The hover alone was about 77% of the flight (30 ÷ 39.1). The remaining 9.1 seconds include ascent and descent, so they do not tell us how long the climb took or its speed.
>
> **What comes next:** After reviewing the flight data, the team could decide whether to attempt another flight and what changes, if any, to make. The first flight’s success does not establish that a later test succeeded.

### With the skill at standard

> **Museum briefing speaker beats**
>
> 1. **The milestone:** On 19 April 2021, Ingenuity flew autonomously at Wright Brothers Field on Mars. It reached about 3 m, hovered for 30 seconds, and landed 39.1 seconds after takeoff. The flight proved powered, controlled flight on another planet.
>
> 2. **What the timing shows:** Keep the hover proportion: 30 of 39.1 seconds, or about 77% of the flight. Don’t call 3 m divided by 39.1 seconds the “average climb speed.” That calculation spreads the height over the *whole flight*, including the hover and descent. The remaining 9.1 seconds covers ascent and descent together, so it does not tell us how long the climb took or identify climb speed.
>
> 3. **What comes next:** After reviewing the flight data, the team can decide what the measured ascent and descent looked like and whether the evidence supports planning another flight. That decision depends on the data; it does not assume a later test succeeded.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Reports the first Mars flight as autonomous, powered and controlled, retains about 3 m and distinguishes 30 s of hover from 39.1 s total. | Met | Met |
| Derives roughly 77% hovering and identifies the remaining 9.1 s as non-hover time including ascent and descent; rejects using total time to infer climb speed. | Met | Met |
| Uses three short audience-facing beats and closes on reviewing the flight data to inform the next test, without claiming future success. | Met | Met |

Both give three beats, put about 77% of the flight into hover, and explain why the other 9.1 seconds do not isolate the climb. Both connect the next decision to reviewing the flight data. The baseline compresses the timing objection into a shorter spoken beat; the skill answer explicitly walks through which phases the slide’s denominator includes.

**차이.** 두 답 모두 체공이 비행 시간의 약 77%이고 나머지 9.1초에는 상승과 하강이 함께 들어간다고 설명합니다. 미적용 답은 잘못된 상승 속도 계산을 짧게 풀고, 스킬 답은 슬라이드의 분모에 섞인 각 비행 단계를 설명합니다.
