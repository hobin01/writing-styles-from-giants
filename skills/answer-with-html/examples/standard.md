# When one more minute of Mars delay costs a whole contact window

[한국어](standard.ko.md) · [light](light.md) · [strict](strict.md)

### Question

> A signal from Earth to the Perseverance rover takes about 3 to 22 minutes one way. In this hypothetical schedule Earth sends at minute 0. The rover takes 10 minutes after receiving the signal to prepare its reply. It can start sending only at minute 25, 50, 75 and so on. If it is ready exactly on a slot, it can use that slot. The return trip takes as long as the outward trip. Why would increasing the one-way delay from 15 to 16 minutes change the time Earth receives the reply by more than a minute?

**Sources** · [NASA/JPL, Speaking Percy's Language: How to Talk so Perseverance Will Listen](https://science.nasa.gov/blog/speaking-percys-language-how-to-talk-so-perseverance-will-listen/)

### Standard

[HTML file · download and open in a browser](standard.html)

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
