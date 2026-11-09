# When one more minute of Mars delay costs a whole contact window

[한국어](light.ko.md) · [standard](standard.md) · [strict](strict.md)

[Question and sources](standard.md#question)

### Light

[HTML file · download and open in a browser](light.html)

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
