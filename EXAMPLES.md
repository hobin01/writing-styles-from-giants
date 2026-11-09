# Writing examples

[한국어 예제](EXAMPLES.ko.md)

For each question, compare the answer with the skill at `light`, `standard` or `strict` to the answer GPT-6 Luna gave without the skill. The question and the answer without the skill stay the same across all three levels. English and Korean were generated separately.

<!-- Generated from the portable examples. -->

- [amazon-six-page-narrative](#amazon-six-page-narrative) · Which bridge review should happen before proposed stockpiling? · [skill examples](skills/amazon-six-page-narrative/examples/README.md)
- [answer-with-html](#answer-with-html) · When one more minute of Mars delay costs a whole contact window · [skill examples](skills/answer-with-html/examples/README.md)
- [aristotle-syllogism](#aristotle-syllogism) · Can new moon and central alignment alone establish a total solar eclipse? · [skill examples](skills/aristotle-syllogism/examples/README.md)
- [asd-ste100](#asd-ste100) · When can each Raspberry Pi 4 recovery station be powered down? · [skill examples](skills/asd-ste100/examples/README.md)
- [boring-professor](#boring-professor) · Tracking two Linux log files behind the same pathname · [skill examples](skills/boring-professor/examples/README.md)
- [diataxis](#diataxis) · Which Kubernetes rollout did the green CI job actually observe? · [skill examples](skills/diataxis/examples/README.md)
- [eli5](#eli5) · What happens when floating ice melts? · [skill examples](skills/eli5/examples/README.md)
- [federal-plain-language](#federal-plain-language) · Which documents can a family collect in 45 minutes? · [skill examples](skills/federal-plain-language/examples/README.md)
- [feynman-technique](#feynman-technique) · Why two DNS resolvers disagree after a record is created · [skill examples](skills/feynman-technique/examples/README.md)
- [google-design-doc](#google-design-doc) · Should PostgreSQL add the orders index during this shift? · [skill examples](skills/google-design-doc/examples/README.md)
- [gtm-formal](#gtm-formal) · When do two Raft candidates need the same vote? · [skill examples](skills/gtm-formal/examples/README.md)
- [hunminjeongeum](#hunminjeongeum) · How much of a Seoul journey can a better map shorten? · [skill examples](skills/hunminjeongeum/examples/README.md)
- [ietf-rfc](#ietf-rfc) · Interpreting two different HTTP 429 retry clocks · [skill examples](skills/ietf-rfc/examples/README.md)
- [imrad](#imrad) · What ten years of LIGO background would imply for GW150914 · [skill examples](skills/imrad/examples/README.md)
- [korean-plain-language](#korean-plain-language) · Which passes qualified for Seoul’s 2024 refund? · [skill examples](skills/korean-plain-language/examples/README.md)
- [microsoft-writing-style](#microsoft-writing-style) · Clearing a Windows clipboard without losing two keepers · [skill examples](skills/microsoft-writing-style/examples/README.md)
- [minto-pyramid](#minto-pyramid) · Which crossings should receive the pilot first? · [skill examples](skills/minto-pyramid/examples/README.md)
- [new-harts-rules](#new-harts-rules) · What does the census say about households without a car? · [skill examples](skills/new-harts-rules/examples/README.md)
- [nist-technical-publication](#nist-technical-publication) · Which improvement would reduce the uncertainty of NIST-F2 more? · [skill examples](skills/nist-technical-publication/examples/README.md)
- [orwell-six-rules](#orwell-six-rules) · What a unit mix-up did to the Mars Climate Orbiter estimate · [skill examples](skills/orwell-six-rules/examples/README.md)
- [socratic-self-questioning](#socratic-self-questioning) · Can Finland’s basic-income study predict 2,400 extra employment days? · [skill examples](skills/socratic-self-questioning/examples/README.md)
- [steve-jobs-presentation](#steve-jobs-presentation) · What can Ingenuity’s flight times tell us? · [skill examples](skills/steve-jobs-presentation/examples/README.md)

## amazon-six-page-narrative

**Which bridge review should happen before proposed stockpiling?** · [한국어](EXAMPLES.ko.md#amazon-six-page-narrative)

### Question

> Investigators found that the I-35W bridge in Minneapolis had undersized U10 gusset plates that earlier load ratings had omitted. Modifications, traffic and construction loads acted together when the bridge collapsed. In a separate, hypothetical screening, River Street's plate has an estimated capacity of 100 units. Its existing load, deck modification and proposed stockpile would impose 68, 18 and 24 units simultaneously. Canal Street's corresponding loads are 66, 14 and 15 units; its plate capacity is unknown. Neither inspection found new visible damage. Neither bridge has a final engineering assessment, and funding covers only one immediate load-rating review. The owner’s priority is the clearest evidence that planned loading could exceed capacity. Which bridge should get the review? Can either stockpile go ahead now?

**Sources** · [NTSB, investigation HWY07MH024, Collapse of I-35W Highway Bridge, Minneapolis, Minnesota](https://www.ntsb.gov/investigations/Pages/HWY07MH024.aspx)

### Light

#### With the skill

> Prioritize the **River Street bridge** for the immediate load-rating review. Its estimated plate capacity is 100 units, while its existing load, deck modification, and proposed stockpile would impose a combined 110 units at the same time. That estimate indicates planned loading could exceed capacity by 10 units.
>
> Neither stockpile should go ahead now. River Street’s estimated combined load exceeds its estimated capacity. Canal Street’s plate capacity is unknown, so there is no evidence that its combined 95-unit load would stay within capacity. The absence of newly visible damage does not resolve either uncertainty, and neither bridge has a final engineering assessment.

#### Without the skill

> Review River Street first. The screening gives it the clearest evidence of a possible overload: its simultaneous loads total 110 units against an estimated capacity of 100.
>
> Do not approve either stockpile now. River Street’s proposed stockpile would bring the screened total above its estimated capacity. Canal Street’s capacity is unknown, and the combined loads alone do not establish that its stockpile is safe. Neither bridge has a final engineering assessment, so defer both stockpiles until qualified engineers complete the needed reviews and determine acceptable loading.

### Standard

#### With the skill

> River Street should receive the immediate load-rating review. The screening estimate gives its plate a capacity of 100 units, while its existing load, deck modification, and proposed stockpile would impose 68 + 18 + 24 = 110 units simultaneously—10 units above the estimate. That is the clearest evidence that planned loading could exceed capacity, matching the owner’s stated priority.
>
> Canal Street’s corresponding loads total 95 units, but its plate capacity is unknown. That missing capacity estimate prevents a comparison with the screening objective; it is not evidence that Canal Street is safe. The I-35W investigation also shows why omitted plate capacity and combined loads matter: investigators found undersized U10 gusset plates omitted from earlier load ratings, and modifications, traffic, and construction loads acted together at collapse.
>
> Neither stockpile should proceed now. River Street’s proposed loading exceeds its estimated capacity, and Canal Street has no known capacity for comparison. Neither bridge has a final engineering assessment, and the absence of new visible damage does not resolve that uncertainty. Proceed only after an engineering assessment supports the planned simultaneous loads.

#### Without the skill

> Review River Street first. The screening gives it the clearest evidence of a possible overload: its simultaneous loads total 110 units against an estimated capacity of 100.
>
> Do not approve either stockpile now. River Street’s proposed stockpile would bring the screened total above its estimated capacity. Canal Street’s capacity is unknown, and the combined loads alone do not establish that its stockpile is safe. Neither bridge has a final engineering assessment, so defer both stockpiles until qualified engineers complete the needed reviews and determine acceptable loading.

### Strict

#### With the skill

> Review River Street first. Its estimated capacity is 100 units, while its existing load, deck modification, and proposed stockpile would impose 68 + 18 + 24 = 110 units simultaneously—10 units above the estimate. That is the clearest evidence that planned loading could exceed capacity, matching the owner’s stated priority. The estimate is not a final engineering assessment, so the review should confirm the capacity and combined loading before any decision to proceed.
>
> Do not allow either stockpile to go ahead now. River Street’s proposed combined load exceeds its estimated capacity. Canal Street’s combined load would be 95 units, but its plate capacity is unknown, so there is not enough evidence to establish that the stockpile is within capacity. Neither inspection found new visible damage, but that does not resolve the capacity questions.

#### Without the skill

> Review River Street first. The screening gives it the clearest evidence of a possible overload: its simultaneous loads total 110 units against an estimated capacity of 100.
>
> Do not approve either stockpile now. River Street’s proposed stockpile would bring the screened total above its estimated capacity. Canal Street’s capacity is unknown, and the combined loads alone do not establish that its stockpile is safe. Neither bridge has a final engineering assessment, so defer both stockpiles until qualified engineers complete the needed reviews and determine acceptable loading.

## answer-with-html

**When one more minute of Mars delay costs a whole contact window** · [한국어](EXAMPLES.ko.md#answer-with-html)

### Question

> A signal from Earth to the Perseverance rover takes about 3 to 22 minutes one way. In this hypothetical schedule Earth sends at minute 0. The rover takes 10 minutes after receiving the signal to prepare its reply. It can start sending only at minute 25, 50, 75 and so on. If it is ready exactly on a slot, it can use that slot. The return trip takes as long as the outward trip. Why would increasing the one-way delay from 15 to 16 minutes change the time Earth receives the reply by more than a minute?

**Sources** · [NASA/JPL, Speaking Percy's Language: How to Talk so Perseverance Will Listen](https://science.nasa.gov/blog/speaking-percys-language-how-to-talk-so-perseverance-will-listen/)

### Light

#### With the skill

[HTML file · download and open in a browser](skills/answer-with-html/examples/light.html)

````html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Why one extra minute can delay the reply by 26 minutes</title>
  <style>
    body { margin: 0; padding: 1.5rem; color: #172033; background: #f5f7fb; font: 1rem/1.55 system-ui, sans-serif; }
    main { max-width: 52rem; margin: auto; padding: 1.5rem; background: white; border-radius: 1rem; box-shadow: 0 4px 24px #17203314; }
    h1 { line-height: 1.2; }
    .table-wrap { max-width: 100%; overflow-x: auto; }
    table { width: 100%; border-collapse: collapse; }
    th, td { padding: .65rem; border-bottom: 1px solid #dbe1ea; text-align: left; vertical-align: top; }
    th { background: #eef3fa; }
    button { margin: .4rem .4rem .4rem 0; padding: .55rem .8rem; border: 1px solid #52647e; border-radius: .4rem; background: #fff; color: inherit; font: inherit; cursor: pointer; }
    button[aria-pressed="true"] { background: #173b66; color: white; }
    #explanation { min-height: 3.2em; padding: .8rem; background: #f1f6fc; border-left: 4px solid #2874b8; }
    .math { font-variant-numeric: tabular-nums; }
  </style>
</head>
<body>
<main>
  <h1>Why one extra minute can delay the reply by 26 minutes</h1>
  <p>Earth sends at minute 0. The rover needs 10 minutes to prepare, can begin its reply at minutes 25, 50, 75, …, and the return trip takes the same time as the outward trip. Slot equality is allowed.</p>

  <div class="table-wrap">
    <table>
      <caption>Two hypothetical one-way delays</caption>
      <thead>
        <tr>
          <th scope="col">One-way delay</th>
          <th scope="col">Signal reaches rover</th>
          <th scope="col">Reply ready</th>
          <th scope="col">Next allowed send slot</th>
          <th scope="col">Reply reaches Earth</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">15 min</th>
          <td>0 + 15 = 15 min</td>
          <td>15 + 10 = 25 min</td>
          <td>25 min (ready exactly at slot)</td>
          <td>25 + 15 = 40 min</td>
        </tr>
        <tr>
          <th scope="row">16 min</th>
          <td>0 + 16 = 16 min</td>
          <td>16 + 10 = 26 min</td>
          <td>50 min (the 25-min slot has passed)</td>
          <td>50 + 16 = 66 min</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p class="math">Difference in Earth’s receipt times: 66 min − 40 min = 26 min.</p>

  <section aria-labelledby="cases-heading">
    <h2 id="cases-heading">Choose a case to see why</h2>
    <button type="button" data-case="15" aria-pressed="true">15-minute delay</button>
    <button type="button" data-case="16" aria-pressed="false">16-minute delay</button>
    <p id="explanation" aria-live="polite">At 15 minutes, the rover is ready exactly when the first send slot opens, so it can reply in that slot.</p>
  </section>

  <p>The extra minute crosses the first send-slot threshold: the rover misses that slot and must wait for the next one, so the reply’s arrival is delayed by more than the added travel time alone.</p>
</main>
<script>
  const explanations = {
    "15": "At 15 minutes, the rover is ready exactly when the first send slot opens, so it can reply in that slot.",
    "16": "At 16 minutes, the rover becomes ready just after the first slot, so it must wait for the next send slot."
  };
  const buttons = document.querySelectorAll("button[data-case]");
  const output = document.getElementById("explanation");
  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const key = button.dataset.case;
      output.textContent = explanations[key];
      buttons.forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
    });
  });
</script>
</body>
</html>
````

#### Without the skill

> At a 15-minute one-way delay, the signal reaches Perseverance at minute 15. It is ready to reply at minute 25, exactly when a sending slot opens. The reply then takes 15 minutes to reach Earth, arriving at minute 40.
>
> At a 16-minute delay, the signal arrives at minute 16, so the rover is ready at minute 26. It misses the minute-25 slot and must wait for the minute-50 slot. The reply takes 16 minutes to return, so Earth receives it at minute 66.
>
> A one-minute increase in travel time makes Earth wait 26 minutes longer because the rover’s fixed sending slots turn a small delay into a 25-minute wait for the next slot.

### Standard

#### With the skill

[HTML file · download and open in a browser](skills/answer-with-html/examples/standard.html)

````html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Why one extra minute can delay the reply by 26 minutes</title>
<style>
  :root { color-scheme: light; font: 16px/1.5 system-ui, sans-serif; color: #182230; background: #f5f7fa; }
  body { max-width: 850px; margin: 0 auto; padding: 2rem 1rem; }
  main { background: white; padding: clamp(1rem, 4vw, 2rem); border-radius: 1rem; box-shadow: 0 4px 20px #18223012; }
  h1 { line-height: 1.2; font-size: clamp(1.6rem, 5vw, 2.4rem); }
  .table-wrap { overflow-x: auto; }
  table { width: 100%; border-collapse: collapse; margin: 1rem 0 .5rem; }
  th, td { border: 1px solid #cbd5e1; padding: .65rem; text-align: left; vertical-align: top; }
  th { background: #eef3f8; }
  caption { text-align: left; font-weight: 650; padding-bottom: .5rem; }
  .check { margin: .5rem 0 1.25rem; padding: .8rem 1rem; background: #f1f7ff; border-left: 4px solid #2563eb; }
  fieldset { border: 1px solid #cbd5e1; border-radius: .65rem; padding: 1rem; margin: 1rem 0; }
  label { margin-right: 1.25rem; }
  #explanation { min-height: 3em; padding: .8rem 1rem; background: #f7f7f2; border-radius: .5rem; }
  tr[aria-current="true"] { background: #fff5d9; }
  @media (max-width: 560px) { th, td { padding: .45rem; } }
</style>
</head>
<body>
<main>
  <h1>Why one extra minute can delay the reply by 26 minutes</h1>
  <p>The reply’s arrival depends on when the rover is ready relative to its permitted sending slots. Select either delay to see the cause.</p>

  <div class="table-wrap">
    <table>
      <caption>Hypothetical schedule, with all times measured from Earth’s transmission at minute 0</caption>
      <thead>
        <tr>
          <th scope="col">One-way delay</th>
          <th scope="col">Signal reaches rover</th>
          <th scope="col">Rover ready (+10 min)</th>
          <th scope="col">First usable slot</th>
          <th scope="col">Reply reaches Earth (+ one-way delay)</th>
        </tr>
      </thead>
      <tbody>
        <tr id="case-15" aria-current="true">
          <th scope="row">15 min</th>
          <td>0 + 15 = 15 min</td>
          <td>15 + 10 = 25 min</td>
          <td>25 min</td>
          <td>25 + 15 = 40 min</td>
        </tr>
        <tr id="case-16" aria-current="false">
          <th scope="row">16 min</th>
          <td>0 + 16 = 16 min</td>
          <td>16 + 10 = 26 min</td>
          <td>50 min</td>
          <td>50 + 16 = 66 min</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p class="check"><strong>Difference in Earth’s receipt times:</strong> 66 min − 40 min = 26 min.</p>

  <fieldset>
    <legend>Choose a one-way delay</legend>
    <label><input type="radio" name="delay" value="15" checked> 15 minutes</label>
    <label><input type="radio" name="delay" value="16"> 16 minutes</label>
  </fieldset>

  <p id="explanation" aria-live="polite">At 15 minutes, the rover is ready exactly at the 25-minute slot, so it can send then. The readiness threshold is met right on time.</p>
</main>
<script>
  const radios = document.querySelectorAll('input[name="delay"]');
  const explanation = document.getElementById('explanation');
  const rows = {
    "15": document.getElementById("case-15"),
    "16": document.getElementById("case-16")
  };
  const messages = {
    "15": "At 15 minutes, the rover is ready exactly at the 25-minute slot, so it can send then. The readiness threshold is met right on time.",
    "16": "At 16 minutes, the rover becomes ready just after the 25-minute slot, so it must wait for the next slot. Crossing that cutoff creates the long wait."
  };
  radios.forEach((radio) => {
    radio.addEventListener("change", () => {
      if (!radio.checked || !messages[radio.value]) return;
      explanation.textContent = messages[radio.value];
      Object.entries(rows).forEach(([value, row]) => {
        row.setAttribute("aria-current", String(value === radio.value));
      });
    });
  });
</script>
</body>
</html>
````

#### Without the skill

> At a 15-minute one-way delay, the signal reaches Perseverance at minute 15. It is ready to reply at minute 25, exactly when a sending slot opens. The reply then takes 15 minutes to reach Earth, arriving at minute 40.
>
> At a 16-minute delay, the signal arrives at minute 16, so the rover is ready at minute 26. It misses the minute-25 slot and must wait for the minute-50 slot. The reply takes 16 minutes to return, so Earth receives it at minute 66.
>
> A one-minute increase in travel time makes Earth wait 26 minutes longer because the rover’s fixed sending slots turn a small delay into a 25-minute wait for the next slot.

### Strict

#### With the skill

[HTML file · download and open in a browser](skills/answer-with-html/examples/strict.html)

````html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Why one extra minute can cost more than a minute</title>
  <style>
    :root { color-scheme: light; font: 1rem/1.55 system-ui, sans-serif; color: #182333; background: #f4f7fb; }
    body { margin: 0; padding: 1.25rem; }
    main { max-width: 760px; margin: auto; padding: clamp(1rem, 4vw, 2rem); background: white; border: 1px solid #dce4ef; border-radius: 1rem; }
    h1 { line-height: 1.2; font-size: clamp(1.6rem, 5vw, 2.2rem); }
    p { max-width: 68ch; }
    .table-wrap { max-width: 100%; overflow-x: auto; }
    table { border-collapse: collapse; width: 100%; min-width: 560px; margin: 1rem 0 .5rem; }
    th, td { text-align: left; vertical-align: top; padding: .7rem; border: 1px solid #dce4ef; }
    th { background: #eef3fa; }
    caption { text-align: left; font-weight: 650; padding-bottom: .5rem; }
    fieldset { border: 1px solid #dce4ef; border-radius: .7rem; padding: .8rem 1rem; margin: 1.25rem 0; }
    label { margin-right: 1.2rem; display: inline-block; }
    #explanation { padding: .8rem 1rem; background: #eef6ff; border-left: 4px solid #3674bd; border-radius: .3rem; }
    .difference { font-weight: 650; }
    @media (max-width: 520px) { body { padding: .5rem; } main { padding: 1rem; } }
  </style>
</head>
<body>
<main>
  <h1>Why one extra minute can cost more than a minute</h1>
  <p>Earth sends at minute 0. The rover waits 10 minutes after receiving the signal to prepare, then can begin its reply at the first 25-minute slot at or after readiness. The return trip takes the same time as the outward trip.</p>

  <div class="table-wrap">
    <table>
      <caption>Two one-way-delay cases (all times in minutes after Earth sends)</caption>
      <thead>
        <tr>
          <th scope="col">One-way delay</th>
          <th scope="col">Rover receives</th>
          <th scope="col">Ready after 10 min</th>
          <th scope="col">Reply starts at eligible slot</th>
          <th scope="col">Earth receives reply</th>
        </tr>
      </thead>
      <tbody>
        <tr data-case="15">
          <th scope="row">15 min</th>
          <td>0 + 15 = 15</td>
          <td>15 + 10 = 25</td>
          <td>25</td>
          <td>25 + 15 = 40</td>
        </tr>
        <tr data-case="16">
          <th scope="row">16 min</th>
          <td>0 + 16 = 16</td>
          <td>16 + 10 = 26</td>
          <td>50</td>
          <td>50 + 16 = 66</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p class="difference">Difference in Earth’s reply receipt time: 66 − 40 = 26 minutes.</p>

  <fieldset>
    <legend>Select a delay to see what causes its outcome</legend>
    <label><input type="radio" name="case" value="15" checked> 15-minute one-way delay</label>
    <label><input type="radio" name="case" value="16"> 16-minute one-way delay</label>
  </fieldset>

  <p id="explanation" role="status" aria-live="polite">At 15 minutes, the rover is ready exactly at a reply slot, so it can send then. The threshold is met on time.</p>
  <p>The one-minute increase moves readiness past the 25-minute slot. Since the next permitted slot is much later, the reply waits for that slot; the threshold crossing creates the extra delay.</p>
</main>
<script>
  "use strict";
  const explanations = {
    "15": "At 15 minutes, the rover is ready exactly at a reply slot, so it can send then. The threshold is met on time.",
    "16": "At 16 minutes, the rover becomes ready just after the 25-minute slot, so it must wait for the next permitted slot. Missing that threshold adds a long scheduling wait."
  };
  const output = document.getElementById("explanation");
  document.querySelectorAll('input[name="case"]').forEach((control) => {
    control.addEventListener("change", (event) => {
      const selected = event.currentTarget.value;
      if (Object.prototype.hasOwnProperty.call(explanations, selected)) {
        output.textContent = explanations[selected];
      }
    });
  });
</script>
</body>
</html>
````

#### Without the skill

> At a 15-minute one-way delay, the signal reaches Perseverance at minute 15. It is ready to reply at minute 25, exactly when a sending slot opens. The reply then takes 15 minutes to reach Earth, arriving at minute 40.
>
> At a 16-minute delay, the signal arrives at minute 16, so the rover is ready at minute 26. It misses the minute-25 slot and must wait for the minute-50 slot. The reply takes 16 minutes to return, so Earth receives it at minute 66.
>
> A one-minute increase in travel time makes Earth wait 26 minutes longer because the rover’s fixed sending slots turn a small delay into a 25-minute wait for the next slot.

## aristotle-syllogism

**Can new moon and central alignment alone establish a total solar eclipse?** · [한국어](EXAMPLES.ko.md#aristotle-syllogism)

### Question

> Every total solar eclipse happens at new moon. A planetarium calendar lists an upcoming new moon but gives no other information. What can someone conclude about totality on that date, or on a date that is not a new moon? In a hypothetical view from one spot, the disks are exactly centered and the Sun is 0.54° across. What would be visible if the Moon were 0.48° across, and what if it were 0.56° across? The annular eclipse of 14 October 2023 is an actual event; neither drawing is a measurement of that event.

**Sources** · [NASA, Why Do Eclipses Happen?](https://science.nasa.gov/eclipses/geometry/) · [NASA, 2023 Annular Eclipse FAQ](https://science.nasa.gov/eclipses/future-eclipses/eclipse-2023/faq/)

### Light

#### With the skill

> The premise gives a one-way relation: every total solar eclipse happens at new moon. So a listed new moon alone does not establish that totality will happen; the calendar gives no further information. On a date that is not a new moon, there cannot be a total solar eclipse, given the premise.
>
> In the hypothetical view, the disks are exactly centered. If the Moon is 0.48° across and the Sun is 0.54° across, the Moon appears smaller and leaves a ring of the Sun visible. If the Moon is 0.56° across, it appears larger and covers the Sun’s disk completely. These are hypothetical comparisons, not measurements of the actual annular eclipse of 14 October 2023.

#### Without the skill

> A total solar eclipse can occur only at new moon, but a new moon does not guarantee totality. The Moon’s shadow must also cross the observer’s location.
>
> On a date that is not a new moon, there cannot be a solar eclipse. On a listed new moon date, the calendar alone tells you nothing about whether an eclipse occurs or whether it is total at any particular spot.
>
> In the hypothetical perfectly centered view, the Sun is 0.54° across:
>
> - If the Moon is 0.48° across, it is too small to cover the Sun fully, so a bright ring remains: an **annular eclipse**.
> - If the Moon is 0.56° across, it is large enough to cover the Sun fully: a **total eclipse**.
>
> These are hypothetical comparisons, not measurements of the 14 October 2023 annular eclipse.

### Standard

#### With the skill

> The premise says total solar eclipses occur only at new moon. It does not say that every new moon has a total eclipse, so the calendar entry alone provides no information about whether totality will occur on that date. On a date that is not a new moon, the premise rules out a total solar eclipse.
>
> For the hypothetical view from one spot, the disks are exactly centered and the Sun is 0.54° across:
>
> - If the Moon is 0.48° across, it would appear smaller than the Sun, leaving a bright ring visible around it.
> - If the Moon is 0.56° across, it would appear larger than the Sun and cover the Sun’s disk from that spot.
>
> These are deductions from the stated hypothetical sizes and alignment. The actual annular eclipse of 14 October 2023 is a separate event; neither hypothetical drawing measures it.

#### Without the skill

> A total solar eclipse can occur only at new moon, but a new moon does not guarantee totality. The Moon’s shadow must also cross the observer’s location.
>
> On a date that is not a new moon, there cannot be a solar eclipse. On a listed new moon date, the calendar alone tells you nothing about whether an eclipse occurs or whether it is total at any particular spot.
>
> In the hypothetical perfectly centered view, the Sun is 0.54° across:
>
> - If the Moon is 0.48° across, it is too small to cover the Sun fully, so a bright ring remains: an **annular eclipse**.
> - If the Moon is 0.56° across, it is large enough to cover the Sun fully: a **total eclipse**.
>
> These are hypothetical comparisons, not measurements of the 14 October 2023 annular eclipse.

### Strict

#### With the skill

> The claim is one-way: every total solar eclipse happens at new moon. It does not say that every new moon has a total solar eclipse.
>
> - **On the listed new moon date:** totality is undetermined. The calendar gives the date’s new-moon status, but no information that establishes a total eclipse.
> - **On a date that is not a new moon:** there cannot be a total solar eclipse on that date, if the supplied claim holds, because every total solar eclipse happens at new moon.
>
> For the hypothetical view from one spot, the disks are exactly centered and the Sun is 0.54° across:
>
> - If the Moon is **0.48° across**, it appears smaller than the Sun, leaving part of the Sun visible around it. That is an annular appearance, not totality.
> - If the Moon is **0.56° across**, it appears larger than the Sun and, with the disks exactly centered, covers the Sun’s disk. That gives total coverage in this hypothetical view.
>
> These are deductions from the stated sizes and alignment. They do not describe or measure the actual annular eclipse of 14 October 2023.

#### Without the skill

> A total solar eclipse can occur only at new moon, but a new moon does not guarantee totality. The Moon’s shadow must also cross the observer’s location.
>
> On a date that is not a new moon, there cannot be a solar eclipse. On a listed new moon date, the calendar alone tells you nothing about whether an eclipse occurs or whether it is total at any particular spot.
>
> In the hypothetical perfectly centered view, the Sun is 0.54° across:
>
> - If the Moon is 0.48° across, it is too small to cover the Sun fully, so a bright ring remains: an **annular eclipse**.
> - If the Moon is 0.56° across, it is large enough to cover the Sun fully: a **total eclipse**.
>
> These are hypothetical comparisons, not measurements of the 14 October 2023 annular eclipse.

## asd-ste100

**When can each Raspberry Pi 4 recovery station be powered down?** · [한국어](EXAMPLES.ko.md#asd-ste100)

### Question

> Three Raspberry Pi 4 Model B boards are finishing bootloader recovery with HDMI displays attached. Disconnect power only after both the green activity LED shows a steady flashing pattern and the HDMI screen is green. Remove the recovery microSD card only after disconnecting power. In this bench exercise the boards are checked at 0, 15, 30, 45 and 60 seconds. Once an indication appears, it stays. On North the LED pattern appears at 16 s and the green screen at 29 s. On South they appear at 41 s and 33 s respectively. On East the LED pattern appears at 21 s and the screen is still not green at 60 s. All three are still powered. At which check can each board be disconnected, and what happens to its recovery microSD card?

**Sources** · [Raspberry Pi, Raspberry Pi computer hardware documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#reflash-the-bootloader)

### Light

#### With the skill

> - **North:** Disconnect power at the 30-second check. Both indications have appeared by then. After disconnecting power, remove the recovery microSD card.
> - **South:** Disconnect power at the 45-second check. Both indications have appeared by then. After disconnecting power, remove the recovery microSD card.
> - **East:** Do not disconnect power at any listed check. The HDMI screen is still not green at 60 seconds, so both required indications are not present. Keep the recovery microSD card in place.

#### Without the skill

> - **North:** Disconnect at the **30-second check**; both indications have appeared by then. After disconnecting power, remove the recovery microSD card.
> - **South:** Disconnect at the **45-second check**; both indications have appeared by then. After disconnecting power, remove the recovery microSD card.
> - **East:** **Do not disconnect at any listed check.** The screen is not green by 60 seconds, so keep the board powered and leave the recovery microSD card in place.

### Standard

#### With the skill

> Disconnect power only after both indications are present. Use the first check at or after the later indication.
>
> | Board | Disconnect power at | Recovery microSD card |
> |---|---:|---|
> | North | 30 s | Remove after disconnecting power. |
> | South | 45 s | Remove after disconnecting power. |
> | East | No check time is safe | Keep the card in place. The screen is not green at 60 s, so both indications are not present. |

#### Without the skill

> - **North:** Disconnect at the **30-second check**; both indications have appeared by then. After disconnecting power, remove the recovery microSD card.
> - **South:** Disconnect at the **45-second check**; both indications have appeared by then. After disconnecting power, remove the recovery microSD card.
> - **East:** **Do not disconnect at any listed check.** The screen is not green by 60 seconds, so keep the board powered and leave the recovery microSD card in place.

### Strict

#### With the skill

> - **North:** Disconnect power at the 30-second check. Both indications are present. Then remove the recovery microSD card.
> - **South:** Disconnect power at the 45-second check. Both indications are present. Then remove the recovery microSD card.
> - **East:** Do not disconnect power during the 60-second exercise. The screen is not green, so the required indications are not both present. Leave the recovery microSD card in place.

#### Without the skill

> - **North:** Disconnect at the **30-second check**; both indications have appeared by then. After disconnecting power, remove the recovery microSD card.
> - **South:** Disconnect at the **45-second check**; both indications have appeared by then. After disconnecting power, remove the recovery microSD card.
> - **East:** **Do not disconnect at any listed check.** The screen is not green by 60 seconds, so keep the board powered and leave the recovery microSD card in place.

## boring-professor

**Tracking two Linux log files behind the same pathname** · [한국어](EXAMPLES.ko.md#boring-professor)

### Question

> At 18:20 the last hard link to /var/log/jobs.log is removed on Linux. Its file has 24 MiB allocated. A writer and a monitor each still have it open. At 18:22 a new file is created at the same pathname with 7 MiB allocated. At 18:23 the writer appends 4 MiB using its original descriptor and closes it. The monitor closes its original descriptor at 18:25. There are no other changes; ignore metadata and assume allocation equals data length. Which file contains the append, and how much file data remains allocated immediately after each close?

**Sources** · [Linux man-pages 6.19, unlink(2)](https://man7.org/linux/man-pages/man2/unlink.2.html)

### Light

#### With the skill

> The writer’s descriptor still refers to the original, unlinked file. Creating a new file at the same pathname does not change what existing descriptors refer to. Therefore, the 4 MiB append goes to the original file.
>
> - **18:23, writer closes:** Original file: 24 MiB + 4 MiB = **28 MiB**. New file: **7 MiB**. Total allocated file data: **35 MiB**.
> - **18:25, monitor closes:** The original file has no open descriptors or hard links, so its data is released. New file: **7 MiB**. Total allocated file data: **7 MiB**.

#### Without the skill

> The append goes to the original, unlinked file because the writer’s descriptor still refers to that inode. The new `/var/log/jobs.log` is a separate file and remains 7 MiB.
>
> - **18:23, writer closes:** The original file still has a linkless open descriptor held by the monitor, so its 28 MiB remains allocated. The new file has 7 MiB allocated.
> - **18:25, monitor closes:** The original file has no links or open descriptors, so it is deleted and its 28 MiB is freed. The new file’s 7 MiB remains allocated.

### Standard

#### With the skill

> A file descriptor refers to an open file independently of the pathname used to open it. Removing the last hard link removes the pathname reference; the file’s data remains allocated while an open descriptor still refers to it. Creating a new file at that pathname creates a separate file.
>
> The append at 18:23 goes to the original file, because the writer uses its original descriptor. The new file at `/var/log/jobs.log` remains 7 MiB.
>
> - **18:23, after the writer closes:** Original file: 24 MiB + 4 MiB = 28 MiB. New file: 7 MiB. **Total allocated file data: 28 MiB + 7 MiB = 35 MiB.**
> - **18:25, after the monitor closes:** The original file has no remaining open descriptors and no pathname, so its data is released. New file: 7 MiB. **Total allocated file data: 7 MiB.**
>
> These totals count the two files’ data and exclude metadata, as specified.

#### Without the skill

> The append goes to the original, unlinked file because the writer’s descriptor still refers to that inode. The new `/var/log/jobs.log` is a separate file and remains 7 MiB.
>
> - **18:23, writer closes:** The original file still has a linkless open descriptor held by the monitor, so its 28 MiB remains allocated. The new file has 7 MiB allocated.
> - **18:25, monitor closes:** The original file has no links or open descriptors, so it is deleted and its 28 MiB is freed. The new file’s 7 MiB remains allocated.

### Strict

#### With the skill

> A hard link is a directory entry that refers to a file’s inode. Removing the last hard link removes the pathname reference, but an open file descriptor can keep the original file’s inode and data available. Creating a new file at the same pathname creates a different file. An open descriptor continues to refer to the file it originally opened.
>
> Assume the writer and monitor descriptors refer to the original 24 MiB file. The new file at `/var/log/jobs.log` is a separate file with 7 MiB allocated. The writer’s append changes the original file by +4 MiB, making its allocated data 28 MiB.
>
> - **Immediately after the writer closes at 18:23:** original file: 28 MiB, still held open by the monitor; new file: 7 MiB. **Total: 28 MiB + 7 MiB = 35 MiB.**
> - **Immediately after the monitor closes at 18:25:** original file: 0 MiB, because it has no remaining hard links or open descriptors; new file: 7 MiB. **Total: 0 MiB + 7 MiB = 7 MiB.**
>
> The append is in the **original file**, which no longer has a pathname after 18:20. The total counts file data that remains allocated; it excludes metadata as specified.

#### Without the skill

> The append goes to the original, unlinked file because the writer’s descriptor still refers to that inode. The new `/var/log/jobs.log` is a separate file and remains 7 MiB.
>
> - **18:23, writer closes:** The original file still has a linkless open descriptor held by the monitor, so its 28 MiB remains allocated. The new file has 7 MiB allocated.
> - **18:25, monitor closes:** The original file has no links or open descriptors, so it is deleted and its 28 MiB is freed. The new file’s 7 MiB remains allocated.

## diataxis

**Which Kubernetes rollout did the green CI job actually observe?** · [한국어](EXAMPLES.ko.md#diataxis)

### Question

> At 09:00 CI ran kubectl rollout status deployment/checkout-api with no flags while revision 7 was rolling out. Revision 8 started before 7 finished. No later revision started, and the command eventually reported success. By default the watch follows the latest rollout. The --revision=N option pins the watch and aborts if that revision is superseded; --watch=false returns a snapshot. Which revision did CI actually verify? What command would watch only revision 7, and what command would return the current status immediately?

**Sources** · [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/)

### Light

#### With the skill

> CI verified **revision 8**, the latest rollout when the watch followed it. The command’s success does not establish that revision 7 finished successfully.
>
> To watch only revision 7:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> To return the current status immediately:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```

#### Without the skill

> CI watched the latest rollout, so it verified revision 8.
>
> Watch only revision 7:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> Return the current status immediately:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```

### Standard

#### With the skill

> CI followed the latest rollout, so it verified revision 8. The command’s success does not show that revision 7 completed.
>
> To watch only revision 7:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> To return the current status immediately:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```

#### Without the skill

> CI watched the latest rollout, so it verified revision 8.
>
> Watch only revision 7:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> Return the current status immediately:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```

### Strict

#### With the skill

> CI watched the latest rollout, so it verified **revision 8**. Revision 7 was superseded before the command succeeded.
>
> To watch only revision 7:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> To return the current status immediately:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```

#### Without the skill

> CI watched the latest rollout, so it verified revision 8.
>
> Watch only revision 7:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> Return the current status immediately:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```

## eli5

**What happens when floating ice melts?** · [한국어](EXAMPLES.ko.md#eli5)

### Question

> A piece of ice floats freely in a glass of fresh water. It weighs 90 grams and takes up 100 milliliters of space. One milliliter of liquid water weighs one gram in this example. The glass has room to spare, and no water spills or evaporates. How much of the ice sticks out of the water? Where will the water line be after the ice melts?

**Sources** · [USGS, Water Density](https://www.usgs.gov/water-science-school/science/water-density) · [NASA, Melting Ocean Ice Affects Sea Level – Unlike Ice Cubes in a Glass](https://sealevel.nasa.gov/news/261/melting-ocean-ice-affects-sea-level-unlike-ice-cubes-in-a-glass/)

### Light

#### With the skill

> Look at the ice floating in the glass. The part under the water pushes water aside. The ice weighs 90 grams, so it pushes aside 90 milliliters of water. Since the whole ice takes up 100 milliliters of space, 10 milliliters’ worth sticks out above the water.
>
> When the ice melts, it becomes 90 milliliters of liquid water. That is the same amount the ice pushed aside while floating, so the water line stays at the same height.

#### Without the skill

> The ice weighs 90 grams, so it must displace 90 milliliters of water to float. Since it takes up 100 milliliters, **10 milliliters of the ice sticks out**.
>
> After it melts, it becomes 90 milliliters of water. The floating ice had already displaced that same 90 milliliters, so **the water line stays at the same height**.

### Standard

#### With the skill

> Look at the ice floating in the glass. Some of it is under the water, and some sticks out.
>
> The ice weighs 90 grams. Since 1 milliliter of water weighs 1 gram in this example, the ice pushes aside 90 milliliters of water. That means 90 milliliters of the ice is under the water.
>
> The whole piece takes up 100 milliliters of space. So 10 milliliters sticks out above the water.
>
> When the ice melts, it becomes 90 milliliters of water. That is the same amount of water the floating ice pushed aside, so the water line stays at the same height.

#### Without the skill

> The ice weighs 90 grams, so it must displace 90 milliliters of water to float. Since it takes up 100 milliliters, **10 milliliters of the ice sticks out**.
>
> After it melts, it becomes 90 milliliters of water. The floating ice had already displaced that same 90 milliliters, so **the water line stays at the same height**.

### Strict

#### With the skill

> Look at the ice floating in the glass. The ice weighs 90 grams. In this example, each milliliter of water weighs 1 gram, so the ice pushes aside 90 milliliters of water to hold itself up.
>
> The whole piece of ice takes up 100 milliliters of space. The part under the water takes up 90 milliliters, so 10 milliliters’ worth sticks out above the water.
>
> When the ice melts, it becomes 90 milliliters of water. That is the same amount of water the floating ice pushed aside. So the water line will stay at the same height.

#### Without the skill

> The ice weighs 90 grams, so it must displace 90 milliliters of water to float. Since it takes up 100 milliliters, **10 milliliters of the ice sticks out**.
>
> After it melts, it becomes 90 milliliters of water. The floating ice had already displaced that same 90 milliliters, so **the water line stays at the same height**.

## federal-plain-language

**Which documents can a family collect in 45 minutes?** · [한국어](EXAMPLES.ko.md#federal-plain-language)

### Question

> I have 45 minutes to collect identity documents for my child’s replacement Social Security card. The October 2026 SSA leaflet says both of us need proof of identity. My child can use a current US passport or a state non-driver ID. I can use a current US passport or a driver’s license. We can use originals or copies certified by the issuer. A notarized photocopy does not count. A birth certificate can establish age or citizenship. All our IDs are current.
>
> Here are our available documents and collection times:
>
> | Owner | Document | Time |
> | --- | --- | --- |
> | Child | Original birth certificate | Already in hand |
> | Child | Original passport | 40 min |
> | Child | Issuer-certified copy of state non-driver ID | 15 min |
> | Parent | Notarized passport photocopy | 5 min |
> | Parent | Issuer-certified passport copy | 25 min |
> | Parent | Original driver’s license | 35 min |
>
> The times add together. What can I get in time that covers both of us?

**Sources** · [SSA, U.S. Citizen/Child — Replacement Social Security Card (October 2026)](https://www.ssa.gov/pubs/EN-05-10514.pdf) · The child’s certified ID copy and the parent’s certified passport copy take 40 minutes in this exercise (15 + 25).

### Light

#### With the skill

> You can collect the child’s issuer-certified state non-driver ID in 15 minutes and your issuer-certified passport copy in 25 minutes. Together, they take **40 minutes** and provide proof of identity for both of you.
>
> The birth certificate can establish age or citizenship, but it does not replace the child’s proof of identity. The notarized passport photocopy does not count.

#### Without the skill

> You can collect the child’s issuer-certified non-driver ID (15 minutes) and your issuer-certified passport copy (25 minutes). Together, they take **40 minutes** and provide proof of identity for both of you.
>
> Your birth certificate establishes the child’s age or citizenship, but it does not replace the child’s identity proof. The notarized passport photocopy does not count.

### Standard

#### With the skill

> For your child, an issuer-certified copy of the state non-driver ID takes 15 minutes. The birth certificate can establish age or citizenship, but it does not meet the leaflet’s identity requirement.
>
> For you, the issuer-certified passport copy takes 25 minutes. The notarized photocopy does not count, and the original driver’s license takes 35 minutes.
>
> Get the certified state ID copy and certified passport copy: 15 + 25 = 40 minutes. That covers both identity requirements within your 45 minutes.

#### Without the skill

> You can collect the child’s issuer-certified non-driver ID (15 minutes) and your issuer-certified passport copy (25 minutes). Together, they take **40 minutes** and provide proof of identity for both of you.
>
> Your birth certificate establishes the child’s age or citizenship, but it does not replace the child’s identity proof. The notarized passport photocopy does not count.

### Strict

#### With the skill

> **Child:** The state non-driver ID is accepted, and its issuer-certified copy takes 15 minutes. The birth certificate can establish age or citizenship, but it does not meet the child’s identity requirement.
>
> **Parent:** The issuer-certified passport copy is accepted and takes 25 minutes. The notarized photocopy is not accepted. The original driver’s license is accepted, but takes 35 minutes.
>
> **Get the child’s certified ID copy and your certified passport copy.** They take 15 + 25 = **40 minutes**, within your 45-minute limit. Both documents are originals or copies certified by the issuer.

#### Without the skill

> You can collect the child’s issuer-certified non-driver ID (15 minutes) and your issuer-certified passport copy (25 minutes). Together, they take **40 minutes** and provide proof of identity for both of you.
>
> Your birth certificate establishes the child’s age or citizenship, but it does not replace the child’s identity proof. The notarized passport photocopy does not count.

## feynman-technique

**Why two DNS resolvers disagree after a record is created** · [한국어](EXAMPLES.ko.md#feynman-technique)

### Question

> Two independent DNS resolvers look up photos.example.org. Bay gets NXDOMAIN at 09:10 and Ridge gets NXDOMAIN at 09:12. Each caches that answer for the smaller of the SOA TTL (240 seconds) and the SOA MINIMUM (600 seconds). At 09:13 the operator adds an A record. Both resolvers receive another query at 09:15. The updated authority is reachable; assume no eviction, early refresh or local override. Why can the two clients get different answers, and when can Ridge first pick up the new record?

**Sources** · [IETF RFC 2308, Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html#section-5)

### Light

#### With the skill

> Bay cached **NXDOMAIN**, meaning the name `photos.example.org` did not exist, at 09:10. Its negative-cache lifetime is the smaller of 240 and 600 seconds: 240 seconds, so that answer expires at 09:14. Ridge cached the same answer at 09:12; its 240-second lifetime expires at 09:16.
>
> The operator adds the A record at 09:13, but that does not change either resolver’s cached answer. At 09:15, Bay’s negative entry has expired, so it can query the reachable authority and return the new record. Ridge’s entry is still valid until 09:16, so it can still return NXDOMAIN. Ridge can first pick up the new record at or after 09:16, when its cached negative answer expires and a query can reach the authority.

#### Without the skill

> The negative-cache lifetime is the smaller of the SOA TTL and SOA MINIMUM: **240 seconds**. Bay’s NXDOMAIN cache expires at **09:14**; Ridge’s expires at **09:16**.
>
> So at 09:15, Bay can query the updated authority and get the new A record, while Ridge can still answer from its cached NXDOMAIN. Ridge can first pick up the new record at **09:16**, when its negative cache expires.

### Standard

#### With the skill

> NXDOMAIN means the resolver was told that `photos.example.org` does not exist. For each resolver, the negative-cache lifetime is the smaller of the SOA TTL and SOA MINIMUM: `min(240, 600) = 240` seconds.
>
> Bay received NXDOMAIN at 09:10, so its cached answer expires at 09:14. Ridge received NXDOMAIN at 09:12, so its answer expires at 09:16. Adding the A record at 09:13 updates the authority, but it does not erase either resolver’s cached answer. At 09:15, Bay’s negative entry has expired and it can query the updated authority and return the new record. Ridge’s entry is still valid until 09:16, so it can still return NXDOMAIN. Ridge can first pick up the new record at 09:16, when its cached answer expires and a subsequent query can reach the authority.

#### Without the skill

> The negative-cache lifetime is the smaller of the SOA TTL and SOA MINIMUM: **240 seconds**. Bay’s NXDOMAIN cache expires at **09:14**; Ridge’s expires at **09:16**.
>
> So at 09:15, Bay can query the updated authority and get the new A record, while Ridge can still answer from its cached NXDOMAIN. Ridge can first pick up the new record at **09:16**, when its negative cache expires.

### Strict

#### With the skill

> NXDOMAIN means the authoritative DNS response said **photos.example.org does not exist** when each resolver looked it up. A negative cache stores that answer temporarily so repeated queries do not have to go back to the authority. Here, each resolver’s cache time is the smaller of 240 and 600 seconds: 240 seconds.
>
> Bay’s timeline: it received NXDOMAIN at 09:10, so that cached answer expires at 09:14. Its 09:15 query comes after expiry; with the updated authority reachable, Bay can look up the name again and get the new A record.
>
> Ridge’s timeline: it received NXDOMAIN at 09:12, so its cached answer expires at 09:16. At 09:15 it can still answer from that cache, so its client can receive NXDOMAIN while Bay’s client gets the A record. Ridge can first pick up the new record on a query at or after 09:16, when the cached answer has expired and Ridge can ask the updated authority.
>
> For a transfer check, keep both lookup times and the record addition fixed, but move Ridge’s next query to 09:16: its old answer is expired then, so it can fetch the A record. The precise time that query arrives is separate; no new query is assumed to occur automatically at expiry.

#### Without the skill

> The negative-cache lifetime is the smaller of the SOA TTL and SOA MINIMUM: **240 seconds**. Bay’s NXDOMAIN cache expires at **09:14**; Ridge’s expires at **09:16**.
>
> So at 09:15, Bay can query the updated authority and get the new A record, while Ridge can still answer from its cached NXDOMAIN. Ridge can first pick up the new record at **09:16**, when its negative cache expires.

## google-design-doc

**Should PostgreSQL add the orders index during this shift?** · [한국어](EXAMPLES.ko.md#google-design-doc)

### Question

> A store running PostgreSQL 17 needs an index on its orders table. Order INSERTs must remain available during the build. Production rollout also requires rehearsal p95 write latency at most 20% above the 40 ms baseline. A concurrent-build rehearsal measured 51 ms; production performance has not been measured. Ordinary CREATE INDEX blocks writes. CREATE INDEX CONCURRENTLY permits writes but scans the table twice and can wait for transactions. If it fails, it can leave an invalid index that the planner ignores but writes still maintain. What should the store do on this shift, and what would justify a later production attempt?

**Sources** · [PostgreSQL 17 documentation, CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY) · [PostgreSQL 17 system catalogs, pg_index](https://www.postgresql.org/docs/17/catalog-pg-index.html)

### Light

#### With the skill

> ## Shift decision
>
> **Do not start the index build on this shift.** Ordinary `CREATE INDEX` violates the requirement that order inserts remain available. `CREATE INDEX CONCURRENTLY` permits writes, but its rehearsal p95 write latency was 51 ms.
>
> The rollout limit is 20% above the 40 ms baseline: at most **48 ms p95**. The rehearsal exceeded that limit by 3 ms, so concurrent build has not passed the release gate. Production performance is also unmeasured.
>
> ## Later production attempt
>
> A production attempt would be justified after a representative rehearsal of the concurrent build measures p95 write latency at or below **48 ms**, while confirming order inserts remain available. The rehearsal should account for the build’s two table scans and possible waits for transactions.
>
> If a concurrent build fails, check whether it left an invalid index. The planner ignores that index, but writes still maintain it; remove the invalid index before retrying. Production performance should be observed during any later approved rollout.

#### Without the skill

> Do not start the production index build on this shift. A concurrent build keeps INSERTs available, but the rehearsal p95 was 51 ms—27.5% above the 40 ms baseline, exceeding the 20% limit of 48 ms. Production performance is also unknown, and the build can take time or leave an invalid index that still adds write overhead if it fails.
>
> A later production attempt is justified after a rehearsal meets the 48 ms p95 limit and the rollout plan accounts for the two scans, possible waits on transactions, and checking for and removing any invalid index left by a failed build. During the production attempt, monitor write latency and build progress, with a rollback plan if the latency limit is breached.

### Standard

#### With the skill

> ## Proposal for this shift
>
> Do not attempt the index build on this shift. The store’s rehearsal p95 write latency limit is 48 ms: 20% above the 40 ms baseline. The concurrent-build rehearsal measured 51 ms, so it failed the release gate by 3 ms. Production performance has not been measured.
>
> ## Proposed design
>
> Use `CREATE INDEX CONCURRENTLY` for a later attempt. It permits order inserts during the build, meeting the availability constraint. It scans the table twice and may wait for transactions.
>
> If the build fails, check whether it left an invalid index. The planner ignores that index, but writes still maintain it. Drop the invalid index before retrying, accounting for its ongoing write cost until it is removed.
>
> ## Alternative
>
> Ordinary `CREATE INDEX` does not meet the availability constraint because it blocks writes during the build. It is therefore not a viable option for this rollout.
>
> ## What would justify a later production attempt
>
> First, repeat the concurrent-build rehearsal in a representative test setting and measure p95 write latency. A result at or below 48 ms would pass the latency gate; a result above 48 ms would not. Also assess transaction waits and the expected impact of the two table scans. Production performance remains unknown until a rollout is approved and observed.
>
> If the representative rehearsal passes and the store can preserve insert availability, reviewers can consider authorizing a production attempt. Approval has not been given.

#### Without the skill

> Do not start the production index build on this shift. A concurrent build keeps INSERTs available, but the rehearsal p95 was 51 ms—27.5% above the 40 ms baseline, exceeding the 20% limit of 48 ms. Production performance is also unknown, and the build can take time or leave an invalid index that still adds write overhead if it fails.
>
> A later production attempt is justified after a rehearsal meets the 48 ms p95 limit and the rollout plan accounts for the two scans, possible waits on transactions, and checking for and removing any invalid index left by a failed build. During the production attempt, monitor write latency and build progress, with a rollback plan if the latency limit is breached.

### Strict

#### With the skill

> # Index build proposal
>
> **Recommendation for this shift:** Defer the index build. The concurrent build keeps `INSERT`s available, but its rehearsal p95 write latency was 51 ms—27.5% above the 40 ms baseline. The release limit is 20% above baseline, or 48 ms. The rehearsal failed that gate, and production performance has not been measured.
>
> ## Goals and constraints
>
> - Keep order `INSERT`s available during the build.
> - Require rehearsal p95 write latency at most 20% above the 40 ms baseline: **48 ms**.
> - The store runs PostgreSQL 17.
>
> ## Proposed behavior
>
> Use `CREATE INDEX CONCURRENTLY` for a later attempt. It permits writes during the build, scans the table twice, and can wait for transactions.
>
> If the command fails, check whether it left an invalid index. The planner ignores that index, but writes still maintain it. Remove the invalid index before retrying; until it is removed, writes continue to pay its maintenance cost.
>
> ## Alternatives and trade-offs
>
> - **Ordinary `CREATE INDEX`:** Does not meet the requirement to keep `INSERT`s available during the build.
> - **`CREATE INDEX CONCURRENTLY`:** Meets the availability requirement, but the measured rehearsal p95 of 51 ms exceeds the 48 ms limit. It is not ready for production authorization.
>
> ## What would justify a later attempt
>
> Repeat the concurrent-build rehearsal in a representative test setting. Authorize a production attempt only if the rehearsal p95 write latency is **at most 48 ms** and the build keeps `INSERT`s available. Production performance remains unmeasured; observe it during any subsequently approved rollout. No production attempt is approved by this proposal.

#### Without the skill

> Do not start the production index build on this shift. A concurrent build keeps INSERTs available, but the rehearsal p95 was 51 ms—27.5% above the 40 ms baseline, exceeding the 20% limit of 48 ms. Production performance is also unknown, and the build can take time or leave an invalid index that still adds write overhead if it fails.
>
> A later production attempt is justified after a rehearsal meets the 48 ms p95 limit and the rollout plan accounts for the two scans, possible waits on transactions, and checking for and removing any invalid index left by a failed build. During the production attempt, monitor write latency and build progress, with a rollback plan if the latency limit is breached.

## gtm-formal

**When do two Raft candidates need the same vote?** · [한국어](EXAMPLES.ko.md#gtm-formal)

### Question

> Two candidates stand in the same election. The number of servers is fixed, each server can vote for at most one candidate for the term, and each candidate needs a set minimum number of votes to win. Raft normally requires a majority. A team proposes four votes as the minimum for either a seven-server or an eight-server cluster. When does a vote threshold prevent two winners? Is four safe in each cluster, and could an election with a safe threshold still have no winner?

**Sources** · [Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm, §5.2](https://raft.github.io/raft.pdf) · [etcd v3.5 FAQ, fault tolerance](https://etcd.io/docs/v3.5/faq/#what-is-failure-tolerance)

### Light

#### With the skill

> Let $N$ be the number of servers and $q$ the minimum votes required to win. Assume each server can vote for at most one of the two candidates during the term.
>
> Two candidates cannot both win exactly when
> $$
> 2q>N.
> $$
> If both won, they would need $2q$ distinct votes, but only $N$ servers can vote. Conversely, if $2q\le N$, the servers could give each candidate $q$ votes, so two winners are possible.
>
> Thus, a safe threshold is $q>\frac N2$, the majority rule:
>
> - For $N=7$, $q=4$ is safe because $8>7$.
> - For $N=8$, $q=4$ is not safe because $8\not>8$. Each candidate could receive four votes.
>
> A safe threshold prevents two winners but does not guarantee a winner. For example, in a seven-server cluster with threshold four, if the votes split $3$–$3$ and one server abstains, neither candidate reaches four.

#### Without the skill

> To prevent two candidates from winning the same term, the minimum vote threshold must be **more than half the servers**. If two candidates each reached that threshold, their vote sets would overlap, which is impossible when each server votes for at most one candidate.
>
> - **Seven servers:** Four votes is safe. Two sets of four would require eight votes, but only seven servers can vote.
> - **Eight servers:** Four votes is not safe. The votes could split four to each candidate, giving both a win. The threshold must be at least five.
>
> A safe threshold does not guarantee a winner. Votes might split among candidates so that none reaches the minimum—for example, in a seven-server cluster with a four-vote threshold, a 3–2–2 split leaves no winner.

### Standard

#### With the skill

> Let $N$ be the number of servers, and let $T$ be the minimum votes required for a candidate to win. Each server can vote for at most one candidate during the term. Thus, for any two distinct candidates with vote counts $v_1$ and $v_2$,
> $$
> v_1+v_2\le N.
> $$
>
> **Two winners are impossible exactly when $2T>N$.** Indeed, if both candidates win, then $v_1,v_2\ge T$, so $v_1+v_2\ge 2T$. This contradicts $v_1+v_2\le N$ when $2T>N$. Conversely, if $2T\le N$, two candidates can each receive $T$ votes, so the threshold alone does not prevent two winners.
>
> For $T=4$:
>
> - With $N=7$, $2T=8>7$, so **four votes is safe against two winners**.
> - With $N=8$, $2T=8\not>8$, so **four votes is not safe**: four servers can vote for each candidate, producing two winners.
>
> A safe threshold does not guarantee a winner. For example, with seven servers and threshold four, if votes split $3$–$3$ and one server abstains, neither candidate reaches four. Thus a threshold can prevent multiple winners while still allowing no winner.

#### Without the skill

> To prevent two candidates from winning the same term, the minimum vote threshold must be **more than half the servers**. If two candidates each reached that threshold, their vote sets would overlap, which is impossible when each server votes for at most one candidate.
>
> - **Seven servers:** Four votes is safe. Two sets of four would require eight votes, but only seven servers can vote.
> - **Eight servers:** Four votes is not safe. The votes could split four to each candidate, giving both a win. The threshold must be at least five.
>
> A safe threshold does not guarantee a winner. Votes might split among candidates so that none reaches the minimum—for example, in a seven-server cluster with a four-vote threshold, a 3–2–2 split leaves no winner.

### Strict

#### With the skill

> Let $N\in\{7,8\}$ be the number of servers, and let $T$ be the minimum number of votes each candidate needs to win. Assume each server casts at most one vote in the term, and both candidates win exactly when each receives at least $T$ votes.
>
> Two winners would require at least $2T$ votes in total. Since at most $N$ votes can be cast, two winners are impossible exactly when
> $$
> 2T>N,
> $$
> or, for integer $T$, when $T>\lfloor N/2\rfloor$. If $2T\le N$, two winners are possible: assign $T$ distinct servers to each candidate, leaving any remaining servers unassigned. Thus the condition is both necessary and sufficient.
>
> For $N=7$, four is safe because $2\cdot4=8>7$. For $N=8$, four is not safe: $2\cdot4=8$, and assigning four servers to each candidate gives both candidates the minimum required votes. A threshold of five would prevent two winners in an eight-server cluster.
>
> A safe threshold does not guarantee a winner. For example, in the seven-server cluster with threshold four, if no server votes, neither candidate reaches four votes. More generally, votes may be split so that each candidate receives fewer than $T$.

#### Without the skill

> To prevent two candidates from winning the same term, the minimum vote threshold must be **more than half the servers**. If two candidates each reached that threshold, their vote sets would overlap, which is impossible when each server votes for at most one candidate.
>
> - **Seven servers:** Four votes is safe. Two sets of four would require eight votes, but only seven servers can vote.
> - **Eight servers:** Four votes is not safe. The votes could split four to each candidate, giving both a win. The threshold must be at least five.
>
> A safe threshold does not guarantee a winner. Votes might split among candidates so that none reaches the minimum—for example, in a seven-server cluster with a four-vote threshold, a 3–2–2 split leaves no winner.

## hunminjeongeum

**How much of a Seoul journey can a better map shorten?** · [한국어](EXAMPLES.ko.md#hunminjeongeum)

### Question

> On Seoul’s old subway map, transfer stations were hard to distinguish from ordinary stops. The 2023 redesign put the connecting line colours in a single transfer symbol. In an eye-tracking experiment with Korean and international participants in their twenties and thirties, locating a transfer on the map took up to about 69% less time. Suppose someone previously took 200 seconds to find the transfer and then rode the train for nine minutes. What difference could the new map make to that trip if this passenger saw the largest reported reduction?

**Sources** · [서울특별시, 지하철 노선도 개선과 아이트래킹 실험](https://mediahub.seoul.go.kr/archives/2009054)

### Light

#### With the skill

> On the old map, this passenger needed 200 seconds to find the transfer because transfer stations were hard to distinguish from ordinary stops. The redesign puts the connecting line colours in a single transfer symbol, making the transfer easier to locate.
>
> Applying the largest reported reduction of about 69% saves about 138 seconds from the search time, leaving about 62 seconds. The nine-minute ride is unchanged, so the trip’s total time falls from 740 seconds to about 602 seconds—a saving of about 138 seconds, or 2 minutes 18 seconds. This is the result if the passenger experiences the largest reduction measured in the experiment; it does not mean every passenger will save that much.

#### Without the skill

> At a 69% reduction, finding the transfer would take about 62 seconds instead of 200, saving roughly 138 seconds (2 minutes 18 seconds). The trip would take about 10 minutes 2 seconds including the nine-minute ride.

### Standard

#### With the skill

> When transfer stations were hard to distinguish from ordinary stops, the 2023 map’s single symbol showing the connecting line colours helped passengers spot a transfer. If this passenger saw the largest reported reduction in search time, finding the transfer would take about 62 seconds instead of 200 seconds—a saving of about 138 seconds.
>
> The nine-minute ride is unchanged. In seconds, the trip’s total time would go from 740 seconds (200 + 540) to about 602 seconds (62 + 540), a reduction of about 138 seconds. This applies the experiment’s reported maximum reduction of about 69% to the time spent finding the transfer; the result is conditional, and the experiment does not establish that every passenger would save this much.

#### Without the skill

> At a 69% reduction, finding the transfer would take about 62 seconds instead of 200, saving roughly 138 seconds (2 minutes 18 seconds). The trip would take about 10 minutes 2 seconds including the nine-minute ride.

### Strict

#### With the skill

> For a passenger who had trouble spotting a transfer station among ordinary stops, the 2023 map’s single symbol showing the connecting line colours could make the transfer quicker to find.
>
> At the largest reported reduction, the 200-second search would take about 62 seconds: 200 × (1 − 0.69) = 62. The nine-minute train ride is unchanged, so the whole trip would go from 740 seconds to about 602 seconds—a saving of about 138 seconds.
>
> So, if this passenger saw the largest reduction measured in the experiment, the trip could be about 138 seconds shorter. The result comes from an eye-tracking experiment with Korean and international participants in their twenties and thirties; it does not establish the reduction for every passenger.

#### Without the skill

> At a 69% reduction, finding the transfer would take about 62 seconds instead of 200, saving roughly 138 seconds (2 minutes 18 seconds). The trip would take about 10 minutes 2 seconds including the nine-minute ride.

## ietf-rfc

**Interpreting two different HTTP 429 retry clocks** · [한국어](EXAMPLES.ko.md#ietf-rfc)

### Question

> Two HTTP 429 responses were sent at 09:00:00 UTC and received at 09:00:05 UTC. The first carried Retry-After: 45. The second contained an HTTP date for 09:01:00 UTC that day. The clocks agree. RFC 6585 permits a server to send 429 when a user sends too many requests in a period of time, recommends that the response explain the condition, permits Retry-After and forbids caches to store 429 responses. RFC 9110 allows Retry-After to be an HTTP date or a nonnegative number of seconds after receipt. What should the server, cache and client make of these responses? When would the client try again in each case, and what could still happen?

**Sources** · [IETF RFC 6585 §4, 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4) · [IETF RFC 9110 §10.2.3, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3)

### Light

#### With the skill

> ### Scope and roles
>
> This interpretation covers two HTTP 429 responses sent by a server and received by a client. The clocks agree. The server sent both responses at 09:00:00 UTC; the client received both at 09:00:05 UTC. The first carried `Retry-After: 45`; the second carried an HTTP date of 09:01:00 UTC that day.
>
> ### Server and cache
>
> RFC 6585 permits the server to send 429 when a user has sent too many requests in a period of time. It recommends that the response explain the condition. The server may include `Retry-After`.
>
> A cache must not store a 429 response.
>
> ### Client
>
> RFC 9110 permits `Retry-After` to contain either an HTTP date or a nonnegative number of seconds after receipt. The two values therefore indicate different retry times:
>
> - For `Retry-After: 45`, the client’s retry time is 45 seconds after receipt: 09:00:50 UTC.
> - For the HTTP date `09:01:00 UTC`, the client’s retry time is that stated date and time: 09:01:00 UTC.
>
> These are suggested retry times, not guarantees that a retry will succeed. The client could still receive another 429 or another response.

#### Without the skill

> The server has returned two valid indications of when to retry. RFC 9110 allows `Retry-After` to be either a delay in seconds or an HTTP date. The two responses therefore give:
>
> - **First response:** `45` seconds after receipt at 09:00:05 UTC, so the client should wait until **09:00:50 UTC**.
> - **Second response:** the date **09:01:00 UTC**, so the client should wait until that time.
>
> The client should treat each response on its own; the values are not cumulative. A 429 signals rate limiting, and the server should explain the condition when practical. It may use `Retry-After` to guide the client, but the header does not guarantee that a retry will succeed: the client could still be rate limited or receive another 429.
>
> A cache **must not store either 429 response**. That restriction does not prevent the client from receiving the responses or acting on their retry guidance.

### Standard

#### With the skill

> ### Interpretation of the 429 responses
>
> RFC 6585 permits a server to send **429 Too Many Requests** when a user has sent too many requests in a period of time. It recommends that the response explain the condition. The server may include `Retry-After`. A cache is forbidden to store a 429 response.
>
> RFC 9110 defines `Retry-After` as either an HTTP date or a nonnegative number of seconds after receipt of the response. The client can use that value to determine when to try again.
>
> | Response | Client’s retry time |
> |---|---|
> | First: `Retry-After: 45`, received at 09:00:05 UTC | 09:00:50 UTC, 45 seconds after receipt |
> | Second: HTTP date 09:01:00 UTC, received at 09:00:05 UTC | 09:01:00 UTC |
>
> These are the times indicated by `Retry-After`; the client may still receive another 429 if the rate limit remains in effect. The second date is later than the first response’s indicated retry time. The two response values do not establish whether they came from the same rate-limit state or which retry time should govern requests other than the one associated with each response.
>
> The cache must not store either 429 response. The stated rules do not specify how a client should reconcile multiple retry instructions beyond interpreting each value according to its form.
>
> IANA applicability: these rules do not request an IANA action.

#### Without the skill

> The server has returned two valid indications of when to retry. RFC 9110 allows `Retry-After` to be either a delay in seconds or an HTTP date. The two responses therefore give:
>
> - **First response:** `45` seconds after receipt at 09:00:05 UTC, so the client should wait until **09:00:50 UTC**.
> - **Second response:** the date **09:01:00 UTC**, so the client should wait until that time.
>
> The client should treat each response on its own; the values are not cumulative. A 429 signals rate limiting, and the server should explain the condition when practical. It may use `Retry-After` to guide the client, but the header does not guarantee that a retry will succeed: the client could still be rate limited or receive another 429.
>
> A cache **must not store either 429 response**. That restriction does not prevent the client from receiving the responses or acting on their retry guidance.

### Strict

#### With the skill

> ## Interpretation of the 429 responses
>
> This interpretation applies RFC 6585’s HTTP 429 behavior and RFC 9110’s `Retry-After` semantics to the two responses. The actors are the server that sends the responses, any cache that handles them, and the client that receives them. The clocks agree.
>
> ### Server
>
> - When a user sends too many requests within a period of time, the server may send a 429 response.
> - When sending a 429 response, the server is recommended to explain the condition.
> - The server may include `Retry-After` in a 429 response.
>
> ### Cache
>
> - A cache is forbidden to store a 429 response.
>
> ### Client
>
> - When `Retry-After` contains a nonnegative number of seconds, the client interprets it as a duration after receipt of the response.
> - When `Retry-After` contains an HTTP date, the client interprets it as the time indicated by that date.
>
> ### Response times and retry times
>
> | Response | Sent | Received | `Retry-After` | Client’s indicated retry time |
> |---|---|---|---|---|
> | First | 09:00:00 UTC | 09:00:05 UTC | `45` seconds | 09:00:50 UTC |
> | Second | 09:00:00 UTC | 09:00:05 UTC | HTTP date: 09:01:00 UTC that day | 09:01:00 UTC |
>
> The first value is relative to receipt, so the client adds 45 seconds to 09:00:05. The second value is an absolute time; the client uses 09:01:00 UTC unchanged. Both indicated times are after the responses were received.
>
> `Retry-After` indicates when to try again; it does not guarantee that a later request will succeed. The server could still send another 429 if the client retries while the rate condition persists.

#### Without the skill

> The server has returned two valid indications of when to retry. RFC 9110 allows `Retry-After` to be either a delay in seconds or an HTTP date. The two responses therefore give:
>
> - **First response:** `45` seconds after receipt at 09:00:05 UTC, so the client should wait until **09:00:50 UTC**.
> - **Second response:** the date **09:01:00 UTC**, so the client should wait until that time.
>
> The client should treat each response on its own; the values are not cumulative. A 429 signals rate limiting, and the server should explain the condition when practical. It may use `Retry-After` to guide the client, but the header does not guarantee that a retry will succeed: the client could still be rate limited or receive another 429.
>
> A cache **must not store either 429 response**. That restriction does not prevent the client from receiving the responses or acting on their retry guidance.

## imrad

**What ten years of LIGO background would imply for GW150914** · [한국어](EXAMPLES.ko.md#imrad)

### Question

> On 14 September 2015 LIGO's Livingston and Hanford instruments recorded GW150914, a signal rising from 35 to 250 Hz with peak dimensionless strain 1.0 × 10⁻²¹. Researchers found that it matched a predicted waveform for a binary black-hole merger. They estimated that noise candidates at least this significant would occur at a rate below one per 203,000 years in this search. Someone concludes that ten years are guaranteed to contain zero such false alarms, and that the probability GW150914 was noise is zero. What do the observations and the ten-year calculation actually establish if the rate stays the same?

**Sources** · [LIGO Scientific Collaboration and Virgo Collaboration, Observation of Gravitational Waves from a Binary Black Hole Merger (2016)](https://dcc.ligo.org/public/0122/P150914/014/LIGO-P150914_Detection_of_GW150914.pdf)

### Light

#### With the skill

> What do the GW150914 observations establish, and what does the ten-year rate imply if the rate stays the same?
>
> **Observations.** On 14 September 2015, the LIGO instruments at Livingston and Hanford recorded GW150914. The signal rose from 35 to 250 Hz and reached a peak dimensionless strain of $1.0 \times 10^{-21}$. Researchers found that it matched a predicted waveform for a binary black-hole merger. In this search, noise candidates at least this significant were estimated to occur at a rate below one per 203,000 years.
>
> **Interpretation.** The waveform match supports a binary black-hole merger interpretation. The rate estimate is an upper bound: it does not establish that the rate is zero, or give the probability that GW150914 was noise. If the rate stays the same for ten years, the expected number of such noise candidates is below $10/203{,}000 \approx 0.0000493$. Zero and some false alarms are both compatible with that bound. It cannot guarantee zero false alarms in ten years, and it does not establish that the probability GW150914 was noise is zero.

#### Without the skill

> The observations show that both LIGO instruments recorded a signal consistent with the predicted waveform of a binary black-hole merger. The stated rate means that, under the search’s noise model, candidates at least this significant would occur on average fewer than once per 203,000 years.
>
> If that rate stays the same, the expected number in ten years is fewer than $10/203{,}000 \approx 4.9\times10^{-5}$. That makes a false alarm over ten years very unlikely, but it does not guarantee zero: a rate is an average, and a rare event can still occur. Nor does this rate alone establish that the probability GW150914 was noise is zero; it quantifies how often noise would produce a candidate this significant under the model, not the probability that this particular candidate was noise.

### Standard

#### With the skill

> ## Introduction
>
> GW150914 was recorded by LIGO’s Livingston and Hanford instruments on 14 September 2015. What do the observations and a ten-year calculation establish about the chance of false alarms and the possibility that the signal was noise?
>
> ## Methods
>
> The two instruments recorded the signal. Researchers compared it with a predicted waveform for a binary black-hole merger. The search estimated the rate at which noise candidates at least as significant as GW150914 would occur. The supplied information does not specify the search’s rate-estimation procedure or uncertainty.
>
> ## Results
>
> The signal rose from 35 to 250 Hz and had a peak dimensionless strain of $1.0 \times 10^{-21}$. Researchers found that it matched the predicted merger waveform. The estimated rate of noise candidates at least this significant was below one per 203,000 years.
>
> If that rate stays the same, multiplying the upper rate bound by ten years gives an expected count below $10/203{,}000 \approx 4.93 \times 10^{-5}$ such candidates in ten years.
>
> ## Discussion
>
> The ten-year calculation bounds the expected count; it does not guarantee that ten years contain zero false alarms. Zero and some such candidates are both compatible with the bound. The rate estimate also does not establish that the probability GW150914 was noise is zero. The supplied observations support the waveform match and a very low estimated background rate, but they do not give a probability that this particular signal was noise.

#### Without the skill

> The observations show that both LIGO instruments recorded a signal consistent with the predicted waveform of a binary black-hole merger. The stated rate means that, under the search’s noise model, candidates at least this significant would occur on average fewer than once per 203,000 years.
>
> If that rate stays the same, the expected number in ten years is fewer than $10/203{,}000 \approx 4.9\times10^{-5}$. That makes a false alarm over ten years very unlikely, but it does not guarantee zero: a rate is an average, and a rare event can still occur. Nor does this rate alone establish that the probability GW150914 was noise is zero; it quantifies how often noise would produce a candidate this significant under the model, not the probability that this particular candidate was noise.

### Strict

#### With the skill

> ## Introduction
>
> What do the reported observations and the ten-year calculation establish about GW150914 and false alarms, assuming the estimated rate stays the same?
>
> ## Methods
>
> On 14 September 2015, the LIGO Livingston and Hanford instruments recorded GW150914. Researchers compared the signal with a predicted waveform for a binary black-hole merger. They estimated the rate at which noise candidates at least as significant as the signal would occur in this search.
>
> ## Results
>
> The signal rose from 35 to 250 Hz and had a peak dimensionless strain of $1.0 \times 10^{-21}$. Researchers found that it matched the predicted binary black-hole merger waveform. The estimated rate of noise candidates at least this significant was below one per 203,000 years. If that rate stays the same, the corresponding ten-year expected count is below $10/203{,}000$, or approximately $4.93 \times 10^{-5}$.
>
> ## Discussion
>
> The rate estimate implies an expected count below approximately $4.93 \times 10^{-5}$ such noise candidates in ten years. Zero candidates and some candidates are both compatible with this upper bound, so it cannot guarantee zero false alarms. The rate estimate also does not establish that the probability GW150914 was noise is zero; that probability requires separate evidence and a probability model.
>
> The supplied account does not specify how the rate was estimated, its uncertainty, or the comparison and analysis procedures in enough detail to assess reproducibility or the strength of the probability claim.

#### Without the skill

> The observations show that both LIGO instruments recorded a signal consistent with the predicted waveform of a binary black-hole merger. The stated rate means that, under the search’s noise model, candidates at least this significant would occur on average fewer than once per 203,000 years.
>
> If that rate stays the same, the expected number in ten years is fewer than $10/203{,}000 \approx 4.9\times10^{-5}$. That makes a false alarm over ten years very unlikely, but it does not guarantee zero: a rate is an average, and a rare event can still occur. Nor does this rate alone establish that the probability GW150914 was noise is zero; it quantifies how often noise would produce a candidate this significant under the model, not the probability that this particular candidate was noise.

## korean-plain-language

**Which passes qualified for Seoul’s 2024 refund?** · [한국어](EXAMPLES.ko.md#korean-plain-language)

### Question

> A Korean exhibit caption about Seoul’s 2024 youth Climate Card pilot says “지우와 민서는 지금 환급금을 받아요.” Under that pilot a completed 30-day pass used without a refund could qualify for 7,000 won. Physical cards counted only after registration; mobile cards needed no separate registration. A pass holder had to apply to receive the pilot payment, whichever card they used. Jiwoo finished one physical pass before registration and another after registration, then refunded a third pass on day 18. Minseo completed two mobile passes without refund. All other conditions were met. In English, explain how much each person was eligible to apply for and why. Then give the exhibit its replacement caption in Korean.

**Sources** · [서울특별시 내 손안에 서울, ‘월 5만원대’ 청년 맞춤형 기후동행카드 나온다 (2024-02-21)](https://mediahub.seoul.go.kr/archives/2010350)

### Light

#### With the skill

> Jiwoo: Only the physical pass completed after registration qualified. The pass completed before registration did not count, and the third pass was refunded on day 18, so it did not meet the completed 30-day condition. 1 × 7,000 won = 7,000 won.
>
> Minseo: Both completed mobile passes qualified; mobile cards did not need separate registration. 2 × 7,000 won = 14,000 won.
>
> Both had to apply to receive the payment, so the source does not establish that either person actually received it.
>
> > 2024년 서울 청년 기후동행카드 시범사업에서 지우는 7,000원을, 민서는 14,000원을 신청할 수 있었어요.

#### Without the skill

> Jiwoo was eligible to apply for ₩7,000 for the pass completed after registering the physical card. The earlier pass did not count because the card was unregistered, and the pass refunded on day 18 did not qualify. Minseo was eligible to apply for ₩14,000: both completed mobile passes went unused for a refund, and mobile cards did not require separate registration. Both had to apply to receive the payment.
>
> **Replacement caption:** 지우는 7천 원, 민서는 1만 4천 원의 환급금을 신청할 수 있어요.

### Standard

#### With the skill

> Jiwoo: Only the 30-day physical pass completed after registration counted. The pass completed before registration did not qualify, and the pass refunded on day 18 did not qualify. One pass × 7,000 won = 7,000 won.
>
> Minseo: Both completed mobile passes counted; mobile cards needed no separate registration. Two passes × 7,000 won = 14,000 won.
>
> Both had to apply to receive the pilot payment. The information does not establish that either person actually received it.
>
> 2024년 서울 청년 기후동행카드 시범사업에서 지우는 환급금 7,000원을, 민서는 14,000원을 신청할 수 있었어요. 두 사람 모두 지급을 신청해야 했어요.

#### Without the skill

> Jiwoo was eligible to apply for ₩7,000 for the pass completed after registering the physical card. The earlier pass did not count because the card was unregistered, and the pass refunded on day 18 did not qualify. Minseo was eligible to apply for ₩14,000: both completed mobile passes went unused for a refund, and mobile cards did not require separate registration. Both had to apply to receive the payment.
>
> **Replacement caption:** 지우는 7천 원, 민서는 1만 4천 원의 환급금을 신청할 수 있어요.

### Strict

#### With the skill

> Jiwoo: Only the physical pass completed after registration qualified; the pass completed before registration did not count, and the third pass was refunded before 30 days. Jiwoo was eligible to apply for 7,000 won.
>
> Minseo: Both completed mobile passes qualified. Mobile cards needed no separate registration. Minseo was eligible to apply for 14,000 won.
>
> Both had to apply to receive the pilot payment. The source establishes eligibility to apply, not that either person received the money.
>
> > 2024년 서울 청년 기후동행카드 시범사업에서 지우는 환급금 7,000원을 신청할 수 있었어요. 민서는 환급금 14,000원을 신청할 수 있었어요.

#### Without the skill

> Jiwoo was eligible to apply for ₩7,000 for the pass completed after registering the physical card. The earlier pass did not count because the card was unregistered, and the pass refunded on day 18 did not qualify. Minseo was eligible to apply for ₩14,000: both completed mobile passes went unused for a refund, and mobile cards did not require separate registration. Both had to apply to receive the payment.
>
> **Replacement caption:** 지우는 7천 원, 민서는 1만 4천 원의 환급금을 신청할 수 있어요.

## microsoft-writing-style

**Clearing a Windows clipboard without losing two keepers** · [한국어](EXAMPLES.ko.md#microsoft-writing-style)

### Question

> My Windows 11 clipboard history has five entries. A delivery address and an obsolete access code are pinned. A return reference and two draft notes are unpinned. I want to keep just the address and the return reference without typing either again. The interface is in English: Windows logo key + V opens Clipboard history, Pin protects an entry from Clear all, Clear all removes unpinned entries, and See more (...) > Delete removes one entry. How can I use Clear all on this PC and still end up with exactly those two items?

**Sources** · [Microsoft Support, Using the clipboard](https://support.microsoft.com/en-us/windows/apps/using-the-clipboard) · To keep the return reference, pin it before choosing **Clear all**.

### Light

#### With the skill

> 1. Press **Windows logo key + V** to open Clipboard history.
> 2. In Clipboard history, keep the pinned delivery address as it is.
> 3. Select **See more (...) > Delete** for the pinned obsolete access code.
> 4. Select **Pin** for the unpinned return reference.
> 5. Leave the two unpinned draft notes as they are.
> 6. Select **Clear all**.
>
> Check that the delivery address and return reference remain.

#### Without the skill

> In Clipboard history, delete the obsolete access code first:
>
> 1. Press **Windows logo key + V**.
> 2. Find the access code, select **See more (…) > Delete**.
> 3. Select **Clear all**.
>
> The pinned address stays protected, and Clear all removes the unpinned return reference and both draft notes. To keep the return reference without retyping it, copy it again from its original source and pin the new clipboard entry. You’ll then have exactly the address and return reference.

### Standard

#### With the skill

> Open Clipboard history with Windows logo key + V, then set up the entries:
>
> | Entry | Current state | Keep or remove | Action to take now |
> |---|---|---|---|
> | Delivery address | Pinned | Keep | Leave it pinned |
> | Obsolete access code | Pinned | Remove | Select See more (...) > Delete |
> | Return reference | Unpinned | Keep | Select Pin |
> | Draft note 1 | Unpinned | Remove | Leave it unpinned |
> | Draft note 2 | Unpinned | Remove | Leave it unpinned |
>
> After those steps, select **Clear all**. Check Clipboard history: it should contain only the delivery address and return reference.

#### Without the skill

> In Clipboard history, delete the obsolete access code first:
>
> 1. Press **Windows logo key + V**.
> 2. Find the access code, select **See more (…) > Delete**.
> 3. Select **Clear all**.
>
> The pinned address stays protected, and Clear all removes the unpinned return reference and both draft notes. To keep the return reference without retyping it, copy it again from its original source and pin the new clipboard entry. You’ll then have exactly the address and return reference.

### Strict

#### With the skill

> | Entry | Current state | Keep or remove | Action to take now |
> |---|---|---|---|
> | Delivery address | Pinned | Keep | Leave it pinned. |
> | Obsolete access code | Pinned | Remove | Select **See more (...) > Delete**. |
> | Return reference | Unpinned | Keep | Select **Pin**. |
> | Draft note 1 | Unpinned | Remove | Leave it unpinned. |
> | Draft note 2 | Unpinned | Remove | Leave it unpinned. |
>
> Press **Windows logo key + V** to open Clipboard history. After the setup actions above, select **Clear all**. The address stays pinned, the return reference is now pinned, and the unpinned draft notes are removed. Check that Clipboard history contains exactly the delivery address and return reference.

#### Without the skill

> In Clipboard history, delete the obsolete access code first:
>
> 1. Press **Windows logo key + V**.
> 2. Find the access code, select **See more (…) > Delete**.
> 3. Select **Clear all**.
>
> The pinned address stays protected, and Clear all removes the unpinned return reference and both draft notes. To keep the return reference without retyping it, copy it again from its original source and pin the new clipboard entry. You’ll then have exactly the address and return reference.

## minto-pyramid

**Which crossings should receive the pilot first?** · [한국어](EXAMPLES.ko.md#minto-pyramid)

### Question

> A city can fund a leading pedestrian interval at North or South, two groups of signalized crossings with heavy turning traffic. WALK would begin 3–7 seconds before drivers get green. Both projects cost the same; the city wants to prevent the larger expected number of vehicle–pedestrian crashes. Without the change, North expects 20 such crashes and South 5 over the same period. A three-city FHWA study estimated a crash modification factor of 0.87. Where should the city run its pilot? How could it find out whether the change made a difference locally?

**Sources** · [FHWA, Leading Pedestrian Interval](https://highways.dot.gov/safety/proven-safety-countermeasures/leading-pedestrian-interval) · [FHWA, Safety Evaluation of Protected Left-Turn Phasing and Leading Pedestrian Intervals on Pedestrian Safety (2018), FHWA-HRT-18-044](https://www.fhwa.dot.gov/publications/research/safety/18044/18044.pdf)

### Light

#### With the skill

> **Run the pilot at North.** If the three-city study’s crash modification factor (CMF) of 0.87 applies locally, the estimated reduction is 13%: about **2.6 crashes at North** (20 × 0.13) versus **0.65 at South** (5 × 0.13) over the same period. The estimate favors North because its baseline expected crash count is higher; it is a forecast based on transferring the study result, not a local effect measurement.
>
> To assess the local effect, compare changes in vehicle–pedestrian crashes at North before and after the pilot with changes over the same periods at comparable signalized crossings without the interval. Choose comparison crossings with similar turning traffic and crash patterns, and account for differences in exposure, such as pedestrian and vehicle volumes. This comparison helps separate the pilot’s effect from broader changes, though the result will remain uncertain if crash counts are small.

#### Without the skill

> Run the pilot at **North**. A crash modification factor (CMF) of 0.87 represents an estimated 13% reduction. Applied to the forecasts, that is about **2.6 crashes prevented at North** versus **0.65 at South** over the same period. North therefore offers the larger expected benefit, assuming the study’s estimate applies similarly at both locations.
>
> To learn whether the interval works locally, collect comparable before-and-after crash data at North and at a similar untreated site, ideally using several years of data because crashes are relatively rare. Compare how crashes change at the pilot site with changes at the comparison site, accounting for pedestrian and vehicle volumes and other changes in street conditions. Also track driver yielding and pedestrian conflicts as more frequent, early indicators. A single site’s before-and-after crash count may be too noisy to establish an effect.

### Standard

#### With the skill

> Run the pilot at **North**, assuming the FHWA estimate applies equally to both locations. Applying the crash modification factor of 0.87 implies a 13% reduction: about **2.6 fewer crashes at North** (20 × 0.13) versus **0.65 fewer at South** (5 × 0.13). These are forecasts based on transferring a three-city study result; the local effect may differ.
>
> To estimate the local effect, compare the change in vehicle–pedestrian crashes at North before and after the pilot with the change over the same periods at a similar untreated group of crossings. Choose comparison crossings with similar crash patterns, turning traffic, and pedestrian exposure, and account for differences in exposure or other safety changes. This comparison helps separate the pilot’s effect from citywide trends and other changes, though rare crashes and differences between sites may leave uncertainty.

#### Without the skill

> Run the pilot at **North**. A crash modification factor (CMF) of 0.87 represents an estimated 13% reduction. Applied to the forecasts, that is about **2.6 crashes prevented at North** versus **0.65 at South** over the same period. North therefore offers the larger expected benefit, assuming the study’s estimate applies similarly at both locations.
>
> To learn whether the interval works locally, collect comparable before-and-after crash data at North and at a similar untreated site, ideally using several years of data because crashes are relatively rare. Compare how crashes change at the pilot site with changes at the comparison site, accounting for pedestrian and vehicle volumes and other changes in street conditions. Also track driver yielding and pedestrian conflicts as more frequent, early indicators. A single site’s before-and-after crash count may be too noisy to establish an effect.

### Strict

#### With the skill

> Run the pilot at **North**. Assuming the three-city study’s crash modification factor (CMF) of 0.87 applies locally, it implies a 13% reduction in vehicle–pedestrian crashes:
>
> - **North:** 20 × (1 − 0.87) = **2.6 fewer expected crashes**; 17.4 remaining.
> - **South:** 5 × (1 − 0.87) = **0.65 fewer expected crashes**; 4.35 remaining.
>
> North therefore offers the larger expected reduction, though these are forecasts based on transferring the study result—not guaranteed local outcomes.
>
> To measure the local effect, compare changes in crashes at North with changes over the same periods at a comparable untreated group of crossings. Use multiple pre- and post-pilot periods and check that the groups had similar trends before the pilot. Account for exposure, such as pedestrian and turning-vehicle volumes, and report uncertainty; crashes may be too rare for a short pilot to show a clear difference.

#### Without the skill

> Run the pilot at **North**. A crash modification factor (CMF) of 0.87 represents an estimated 13% reduction. Applied to the forecasts, that is about **2.6 crashes prevented at North** versus **0.65 at South** over the same period. North therefore offers the larger expected benefit, assuming the study’s estimate applies similarly at both locations.
>
> To learn whether the interval works locally, collect comparable before-and-after crash data at North and at a similar untreated site, ideally using several years of data because crashes are relatively rare. Compare how crashes change at the pilot site with changes at the comparison site, accounting for pedestrian and vehicle volumes and other changes in street conditions. Also track driver yielding and pedestrian conflicts as more frequent, early indicators. A single site’s before-and-after crash count may be too noisy to establish an effect.

## new-harts-rules

**What does the census say about households without a car?** · [한국어](EXAMPLES.ko.md#new-harts-rules)

### Question

> Our exhibit has this English label: “In ‘Housing, England and Wales: Census 2021’, ONS showed that 42.1% of Londoners lacked a car in 2021, 18.8 per cent more than across England and Wales.” The bulletin counts households with no car or van available: 42.1% in London and 23.3% across England and Wales. What should the English label say if it needs to give both the gap in percentage points and the excess as a percentage of the England-and-Wales figure?

**Sources** · [Office for National Statistics, Housing, England and Wales: Census 2021 (5 January 2023)](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/housingenglandandwales/census2021)

### Light

#### With the skill

> “In ‘Housing, England and Wales: Census 2021’, ONS showed that 42.1% of London households had no car or van available in 2021, 18.8 percentage points higher than the 23.3% across England and Wales. This was 80.7% above the England-and-Wales figure.”

#### Without the skill

> “In ‘Housing, England and Wales: Census 2021’, ONS showed that 42.1% of London households had no car or van available in 2021, 18.8 percentage points higher than the 23.3% figure for England and Wales. That is about 80.7% higher than the England-and-Wales figure.”

### Standard

#### With the skill

> “In ‘Housing, England and Wales: Census 2021’, ONS showed that 42.1% of households in London had no car or van available in 2021, compared with 23.3% across England and Wales—a gap of 18.8 percentage points. London’s figure was 80.7% higher than the England-and-Wales figure.”

#### Without the skill

> “In ‘Housing, England and Wales: Census 2021’, ONS showed that 42.1% of London households had no car or van available in 2021, 18.8 percentage points higher than the 23.3% figure for England and Wales. That is about 80.7% higher than the England-and-Wales figure.”

### Strict

#### With the skill

> “In ‘Housing, England and Wales: Census 2021’, ONS showed that 42.1% of London households had no car or van available in 2021, compared with 23.3% of households across England and Wales. The London figure was 18.8 percentage points higher, or 80.7% higher than the England-and-Wales figure.”

#### Without the skill

> “In ‘Housing, England and Wales: Census 2021’, ONS showed that 42.1% of London households had no car or van available in 2021, 18.8 percentage points higher than the 23.3% figure for England and Wales. That is about 80.7% higher than the England-and-Wales figure.”

## nist-technical-publication

**Which improvement would reduce the uncertainty of NIST-F2 more?** · [한국어](EXAMPLES.ko.md#nist-technical-publication)

### Question

> The July–August 2013 NIST-F2 evaluation reported fractional frequency uncertainty components of 0.44 × 10⁻¹⁵ (Type A, statistical) and 0.11 × 10⁻¹⁵ (Type B, systematic). Its 80 K environment reduced blackbody-radiation uncertainty by more than a factor of 50. Microwave-amplitude effects dominated Type B. Suppose we can halve either component for the same cost, leaving the other unchanged. Assume the two components are independent and combine in quadrature. Which upgrade would reduce combined uncertainty more? Does the fiftyfold figure tell us how much the clock’s overall uncertainty improved?

**Sources** · [Heavner et al., First Accuracy Evaluation of NIST-F2, Metrologia (2014)](https://www.nist.gov/publications/first-accuracy-evaluation-nist-f2)

### Light

#### With the skill

> ## Comparison
>
> Assuming the Type A and Type B components are independent, the combined fractional frequency uncertainty is
>
> $$
> u=\sqrt{u_A^2+u_B^2}.
> $$
>
> Halving Type A gives
>
> $$
> u_{\text{half A}}
> =\sqrt{(0.22\times10^{-15})^2+(0.11\times10^{-15})^2}
> =\sqrt{0.0605}\times10^{-15}.
> $$
>
> Halving Type B gives
>
> $$
> u_{\text{half B}}
> =\sqrt{(0.44\times10^{-15})^2+(0.055\times10^{-15})^2}
> =\sqrt{0.196625}\times10^{-15}.
> $$
>
> **Halving Type A would reduce the combined uncertainty more.** The Type A component is larger, so reducing it has the greater effect under the stated quadrature assumption.
>
> ## What the 50-fold figure means
>
> No. The more-than-50-fold reduction applies to the **blackbody-radiation uncertainty** in the 80 K environment. It does not state how much the clock’s overall uncertainty improved. That would require the blackbody contribution before and after cooling and the other uncertainty components used in the overall combination.

#### Without the skill

> Halving the Type A component reduces combined uncertainty from $\sqrt{0.44^2+0.11^2}\approx0.454$ to $\sqrt{0.22^2+0.11^2}\approx0.246$, in units of $10^{-15}$.
>
> Halving Type B gives $\sqrt{0.44^2+0.055^2}\approx0.443$. So halving Type A reduces the combined uncertainty more.
>
> The factor of more than 50 applies to the blackbody-radiation uncertainty, not to the clock’s overall uncertainty. Without the other uncertainty contributions and the blackbody term’s size before the reduction, it does not tell us how much overall uncertainty improved.

### Standard

#### With the skill

> ## Comparison of the two upgrades
>
> Assuming the Type A and Type B components are independent, the combined fractional frequency uncertainty is their root-sum-square:
>
> $$
> u=\sqrt{u_A^2+u_B^2}.
> $$
>
> If the Type A component is halved:
>
> $$
> u_A'=\sqrt{(0.22\times10^{-15})^2+(0.11\times10^{-15})^2}
> =\sqrt{0.0605}\times10^{-15}.
> $$
>
> If the Type B component is halved:
>
> $$
> u_B'=\sqrt{(0.44\times10^{-15})^2+(0.055\times10^{-15})^2}
> =\sqrt{0.196625}\times10^{-15}.
> $$
>
> The Type A upgrade yields the lower combined uncertainty, so halving Type A would reduce the combined uncertainty more.
>
> ## What the fiftyfold figure means
>
> No. The statement that the 80 K environment reduced blackbody-radiation uncertainty by more than a factor of 50 applies to that uncertainty contribution. It does not give the clock’s overall uncertainty improvement. That would require the blackbody contribution before and after cooling, along with the other uncertainty components and how they combine.

#### Without the skill

> Halving the Type A component reduces combined uncertainty from $\sqrt{0.44^2+0.11^2}\approx0.454$ to $\sqrt{0.22^2+0.11^2}\approx0.246$, in units of $10^{-15}$.
>
> Halving Type B gives $\sqrt{0.44^2+0.055^2}\approx0.443$. So halving Type A reduces the combined uncertainty more.
>
> The factor of more than 50 applies to the blackbody-radiation uncertainty, not to the clock’s overall uncertainty. Without the other uncertainty contributions and the blackbody term’s size before the reduction, it does not tell us how much overall uncertainty improved.

### Strict

#### With the skill

> ## Comparison
>
> Assuming the Type A and Type B components are independent, the combined fractional frequency uncertainty is
>
> $$
> u_{\mathrm{combined}}=\sqrt{u_A^2+u_B^2}.
> $$
>
> Halving Type A gives
>
> $$
> \sqrt{(0.22\times10^{-15})^2+(0.11\times10^{-15})^2}
> =\sqrt{0.0605}\times10^{-15}.
> $$
>
> Halving Type B gives
>
> $$
> \sqrt{(0.44\times10^{-15})^2+(0.055\times10^{-15})^2}
> =\sqrt{0.196625}\times10^{-15}.
> $$
>
> The Type A upgrade leaves the lower combined uncertainty, so it would reduce combined uncertainty more under the stated assumptions.
>
> ## What the fiftyfold figure says
>
> No. The factor of more than 50 applies to the **blackbody-radiation uncertainty** in the 80 K environment. It does not give the clock’s overall uncertainty improvement. That would require the blackbody contribution before and after cooling, along with the other uncertainty contributions and their combination. The reported Type B total is also dominated by microwave-amplitude effects, so the blackbody reduction alone cannot determine the change in total uncertainty.

#### Without the skill

> Halving the Type A component reduces combined uncertainty from $\sqrt{0.44^2+0.11^2}\approx0.454$ to $\sqrt{0.22^2+0.11^2}\approx0.246$, in units of $10^{-15}$.
>
> Halving Type B gives $\sqrt{0.44^2+0.055^2}\approx0.443$. So halving Type A reduces the combined uncertainty more.
>
> The factor of more than 50 applies to the blackbody-radiation uncertainty, not to the clock’s overall uncertainty. Without the other uncertainty contributions and the blackbody term’s size before the reduction, it does not tell us how much overall uncertainty improved.

## orwell-six-rules

**What a unit mix-up did to the Mars Climate Orbiter estimate** · [한국어](EXAMPLES.ko.md#orwell-six-rules)

### Question

> A draft about the 1999 Mars Climate Orbiter says, ‘Operational misalignment effectuated a 170-km plunge. SM_FORCES supplied thruster impulses in pound-force seconds, which navigation read as newton-seconds. The craft burned up.’ The trajectory estimate accumulated error and the spacecraft approached Mars about 170 km lower than planned. NASA could not distinguish destruction in the atmosphere from escape into a solar orbit. Suppose SM_FORCES had sent the number 2; this is an illustration, not a flight measurement. Use 1 pound-force second ≈ 4.45 newton-seconds. What should the draft say about the unit error and the spacecraft’s fate?

**Sources** · [Cornelius J. Dennehy / NASA, Best Practices for the Design, Development, and Operation of Robust and Reliable Space Vehicle Guidance, Navigation, and Control Systems (NASA/TP–20230005922, April 2023)](https://ntrs.nasa.gov/api/citations/20230005922/downloads/20230005922.pdf)

### Light

#### With the skill

> SM_FORCES sent thruster impulses in pound-force seconds, but navigation treated the values as newton-seconds. For example, 2 pound-force seconds is about 8.9 newton-seconds; if navigation read the unchanged numeral as 2 newton-seconds, it undercounted the impulse. The number 2 is illustrative, not a flight measurement.
>
> The trajectory estimate accumulated error, and the spacecraft approached Mars about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or escaped into a solar orbit.

#### Without the skill

> “The navigation system treated SM_FORCES’ thruster impulses as newton-seconds, though they were in pound-force seconds. Thus a value of 2 pound-force seconds corresponds to about 8.9 newton-seconds; 2 is only an illustration, not a flight measurement. The resulting trajectory error brought the spacecraft to Mars about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or escaped into solar orbit.”

### Standard

#### With the skill

> The SM_FORCES component sent thruster impulses in pound-force seconds, but navigation read the values as newton-seconds. For example, 2 pound-force seconds × 4.45 newton-seconds per pound-force second ≈ 8.9 newton-seconds. If navigation treated the unchanged numeral 2 as newton-seconds, it read an impulse of 2 newton-seconds. The 2 is illustrative, not a flight measurement.
>
> The trajectory estimate accumulated error, and the spacecraft approached Mars about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or escaped into a solar orbit. Its fate remains unknown.

#### Without the skill

> “The navigation system treated SM_FORCES’ thruster impulses as newton-seconds, though they were in pound-force seconds. Thus a value of 2 pound-force seconds corresponds to about 8.9 newton-seconds; 2 is only an illustration, not a flight measurement. The resulting trajectory error brought the spacecraft to Mars about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or escaped into solar orbit.”

### Strict

#### With the skill

> SM_FORCES sent thruster impulses in pound-force seconds, but navigation read the values as newton-seconds. For example, 2 pound-force seconds is about 8.9 newton-seconds; if navigation treated the unchanged numeral 2 as newton-seconds, it read about 2 newton-seconds. The number 2 is illustrative, not a flight measurement.
>
> The trajectory estimate accumulated error, and the spacecraft approached Mars about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or escaped into a solar orbit.

#### Without the skill

> “The navigation system treated SM_FORCES’ thruster impulses as newton-seconds, though they were in pound-force seconds. Thus a value of 2 pound-force seconds corresponds to about 8.9 newton-seconds; 2 is only an illustration, not a flight measurement. The resulting trajectory error brought the spacecraft to Mars about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or escaped into solar orbit.”

## socratic-self-questioning

**Can Finland’s basic-income study predict 2,400 extra employment days?** · [한국어](EXAMPLES.ko.md#socratic-self-questioning)

### Question

> A city expects 2,400 extra employment days if it pays a basic income to 400 residents. It cites Finland’s 2017–2018 experiment, where 2,000 randomly selected unemployed benefit recipients got €560 a month. From November 2017 to October 2018 participants averaged 78 employment days, six more than the comparison group. In the first year there was no group-level employment effect. A 2018 benefit reform affected the groups differently, and its second-year effect could not be separated from that of basic income. What does the Finnish evidence support about the city’s estimate?

**Sources** · [Finnish Ministry of Social Affairs and Health and Kela, Results of the basic income experiment (6 May 2020)](https://valtioneuvosto.fi/en/-/1271139/perustulokokeilun-tulokset-tyollisyysvaikutukset-vahaisia-toimeentulo-ja-psyykkinen-terveys-koettiin-paremmaksi?languageId=en_US)

### Light

#### With the skill

> The key ambiguity is what the city means by “2,400 extra employment days”: compared with what would have happened without the basic income, over what period, and for whom?
>
> Among Finland’s 2,000 randomly selected unemployed benefit recipients, the reported average was 78 employment days from November 2017 to October 2018—six more than the comparison group. But there was no group-level employment effect in the first year. In the second year, a 2018 benefit reform affected the groups differently, and its effect could not be separated from basic income’s.
>
> So the Finnish evidence does not establish that basic income caused the six-day difference, or that it would apply to the city’s 400 residents. The estimate of 2,400 days is the arithmetic result of multiplying 400 by six; it is supported as a forecast only if the city’s residents and program resemble the Finnish study group and conditions, and if the second-year difference was caused by basic income rather than the reform.

#### Without the skill

> The arithmetic is clear: 400 residents × six additional employment days = 2,400 days. But the Finnish evidence does not establish that basic income caused those six days.
>
> In the first year, researchers found no group-level employment effect. In the second, participants averaged six more days than the comparison group, but a benefit reform affected the groups differently, so researchers could not separate the reform’s effect from basic income’s. The city can present 2,400 days as a scenario based on that observed difference, but not as an evidence-backed forecast of what its basic-income program will produce.

### Standard

#### With the skill

> The estimate assumes the Finnish result transfers to the city’s 400 residents. But what does “six more days” describe? It is the difference in average employment days between the trial groups from November 2017 to October 2018—not an increase caused by basic income across the full trial.
>
> Among Finland’s randomly selected unemployed benefit recipients, who received €560 a month, the basic income group averaged 78 employment days in that second-year period, six more than the comparison group. In the first year, there was no group-level employment effect. A benefit reform affected the groups differently in the second year, and its effect could not be separated from basic income’s.
>
> So the Finnish evidence does not establish that basic income caused the six-day difference, or that the city should expect 2,400 extra employment days. That forecast would require the second-year difference to be attributable to basic income and to carry over to the city’s 400 residents. The trial result alone does not establish either condition.

#### Without the skill

> The arithmetic is clear: 400 residents × six additional employment days = 2,400 days. But the Finnish evidence does not establish that basic income caused those six days.
>
> In the first year, researchers found no group-level employment effect. In the second, participants averaged six more days than the comparison group, but a benefit reform affected the groups differently, so researchers could not separate the reform’s effect from basic income’s. The city can present 2,400 days as a scenario based on that observed difference, but not as an evidence-backed forecast of what its basic-income program will produce.

### Strict

#### With the skill

> The city’s estimate is **2,400 extra employment days**, or six extra days for each of 400 residents. The Finnish result does not establish that rate as an effect of basic income: the six-day difference was observed from November 2017 to October 2018, after a benefit reform affected the groups differently. The experiment found no group-level employment effect in its first year, and it could not separate the reform’s second-year effect from basic income’s.
>
> So the Finnish evidence supports citing six days as an observed second-year difference among the 2,000 randomly selected unemployed benefit recipients who received €560 a month—not as six days caused by basic income or a reliable forecast for the city. The estimate would follow only if the city’s residents and program produced a comparable effect and other factors did not account for the Finnish difference; the evidence provided does not establish those conditions.

#### Without the skill

> The arithmetic is clear: 400 residents × six additional employment days = 2,400 days. But the Finnish evidence does not establish that basic income caused those six days.
>
> In the first year, researchers found no group-level employment effect. In the second, participants averaged six more days than the comparison group, but a benefit reform affected the groups differently, so researchers could not separate the reform’s effect from basic income’s. The city can present 2,400 days as a scenario based on that observed difference, but not as an evidence-backed forecast of what its basic-income program will produce.

## steve-jobs-presentation

**What can Ingenuity’s flight times tell us?** · [한국어](EXAMPLES.ko.md#steve-jobs-presentation)

### Question

> On 19 April 2021 Ingenuity flew autonomously at Wright Brothers Field on Mars. It rose to about 3 m, hovered for 30 seconds, and landed 39.1 seconds after takeoff. Someone calls 3 m divided by 39.1 s its average climb speed. What did the flight demonstrate? What can these times tell us about the hover and the climb, and how might the team use the first flight's data to decide what to try next?

**Sources** · [NASA, NASA’s Ingenuity Mars Helicopter Succeeds in Historic First Flight (April 19, 2021)](https://www.nasa.gov/news-release/nasas-ingenuity-mars-helicopter-succeeds-in-historic-first-flight/)

### Light

#### With the skill

> Ingenuity’s first flight showed that a powered, controlled flight on Mars was possible.
>
> The helicopter rose to about 3 m and landed 39.1 seconds after takeoff. The 30-second hover was about three quarters of the flight; rising and descending shared the other 9.1 seconds, so the total time does not tell us how long the climb took. Dividing 3 m by 39.1 seconds gives a rough height-over-total-time ratio, not its average climb speed.
>
> The team could review the flight data to assess how Ingenuity performed during takeoff, hover, and landing, then use that evidence to choose what to try on a later flight.

#### Without the skill

> The flight demonstrated that powered, controlled flight is possible in Mars’ thin atmosphere. Ingenuity rose, held position, and landed under its own control, guided by onboard systems rather than a pilot steering it in real time.
>
> Dividing 3 m by 39.1 s gives about **0.077 m/s**, but that is only the change in altitude divided by the *entire flight time*. It is not the average climb speed: the 39.1 seconds include the 30-second hover and the descent. The times show that the hover occupied most of the flight. They don’t tell us the climb duration or speed, or exactly how long the descent took. We’d need the flight’s altitude-versus-time data for that.
>
> The team could use that data, along with the helicopter’s sensor and performance records, to check how closely the flight matched its planned profile and how it handled takeoff, hovering, and landing. If the data showed stable control and adequate margins, they could try a modest next step—such as a higher or longer flight, or a short translation—while changing only what the results supported.

### Standard

#### With the skill

> The first flight showed that a powered, controlled aircraft could fly autonomously on Mars.
>
> Ingenuity hovered for 30 seconds of its 39.1-second flight—about 77% of the total. The other 9.1 seconds were shared by the climb and descent, so the flight time alone cannot tell us how long the climb took.
>
> Dividing 3 m by 39.1 s does not give the average climb speed: the total flight time includes the hover and descent. The times show that Ingenuity reached about 3 m and sustained a 30-second hover, but they don’t establish its climb speed. The team could review the first flight’s flight data to decide whether a later test should change the height, duration, or flight path; what to try next would depend on that review.

#### Without the skill

> The flight demonstrated that powered, controlled flight is possible in Mars’ thin atmosphere. Ingenuity rose, held position, and landed under its own control, guided by onboard systems rather than a pilot steering it in real time.
>
> Dividing 3 m by 39.1 s gives about **0.077 m/s**, but that is only the change in altitude divided by the *entire flight time*. It is not the average climb speed: the 39.1 seconds include the 30-second hover and the descent. The times show that the hover occupied most of the flight. They don’t tell us the climb duration or speed, or exactly how long the descent took. We’d need the flight’s altitude-versus-time data for that.
>
> The team could use that data, along with the helicopter’s sensor and performance records, to check how closely the flight matched its planned profile and how it handled takeoff, hovering, and landing. If the data showed stable control and adequate margins, they could try a modest next step—such as a higher or longer flight, or a short translation—while changing only what the results supported.

### Strict

#### With the skill

> Ingenuity’s first flight showed that a small rotorcraft could take off, hover, and land autonomously in the thin Martian atmosphere.
>
> It reached about 3 m and hovered for 30 of the flight’s 39.1 seconds—about 77% of the flight. Takeoff, climb, descent, and landing shared the remaining 9.1 seconds, so the total time cannot tell us how long the climb alone took. Dividing 3 m by 39.1 seconds gives about 0.077 m/s, but that is not its average climb speed: it divides the peak height by the entire flight duration, including the hover and other stages.
>
> The team could use the first flight’s recorded data to assess how the aircraft and its systems performed, then decide whether to adjust the next flight’s altitude, duration, or other conditions. Those data could guide the next attempt; they don’t by themselves establish how a changed flight would perform.

#### Without the skill

> The flight demonstrated that powered, controlled flight is possible in Mars’ thin atmosphere. Ingenuity rose, held position, and landed under its own control, guided by onboard systems rather than a pilot steering it in real time.
>
> Dividing 3 m by 39.1 s gives about **0.077 m/s**, but that is only the change in altitude divided by the *entire flight time*. It is not the average climb speed: the 39.1 seconds include the 30-second hover and the descent. The times show that the hover occupied most of the flight. They don’t tell us the climb duration or speed, or exactly how long the descent took. We’d need the flight’s altitude-versus-time data for that.
>
> The team could use that data, along with the helicopter’s sensor and performance records, to check how closely the flight matched its planned profile and how it handled takeoff, hovering, and landing. If the data showed stable control and adequate margins, they could try a modest next step—such as a higher or longer flight, or a short translation—while changing only what the results supported.
