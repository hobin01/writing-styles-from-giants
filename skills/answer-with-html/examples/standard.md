# Why Perseverance cannot answer Earth immediately

2026-11-08 · `answer-with-html` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [NASA/JPL, Speaking Percy's Language: How to Talk so Perseverance Will Listen](https://science.nasa.gov/blog/speaking-percys-language-how-to-talk-so-perseverance-will-listen/). JPL vehicle systems engineer Pegah Pashai explains why the one-way command delay varies from about 3 to 22 minutes with orbital position. The doubled time is this exhibit's idealized calculation.

### Prompt

> Return only a short self-contained HTML page for a Mars exhibit. NASA describes commands to the Perseverance rover as taking about 3 to 22 minutes one way as Earth and Mars change position. Give the visitor one labeled slider for whole minutes in that range. Start at 12 minutes and show how long Earth would wait for a reply if the rover replied immediately and the return signal took as long as the outgoing one. Explain why the result is a minimum in this model, not an actual scheduled reply time. The initial result must be readable without scripts; use no external resources.

### Without a skill

````html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mars: Waiting for a Reply</title>
<style>
body{margin:0;background:#201519;color:#fff0df;font:18px/1.6 system-ui,sans-serif}
main{max-width:36rem;margin:4rem auto;padding:1.5rem}
h1{line-height:1.15;color:#ffad80}
input{width:100%;accent-color:#ffad80}
.result{font-size:1.5rem;font-weight:bold}
</style>
</head>
<body>
<main>
<h1>A message to Mars—and back</h1>
<p>NASA describes commands to the Perseverance rover as taking about 3 to 22 minutes one way, depending on the positions of Earth and Mars.</p>
<label for="delay">One-way signal travel time: <output id="minutes" for="delay">12</output> minutes</label>
<input id="delay" type="range" min="3" max="22" step="1" value="12">
<p class="result" aria-live="polite">Minimum wait for a reply: <output id="wait" for="delay">24 minutes</output></p>
<p>The calculation is twice the one-way travel time: out to Mars, then back to Earth. It assumes the rover replies immediately and the return signal takes just as long.</p>
<p>This is a minimum in this model, not a scheduled reply time. Processing, carrying out a command, and waiting for communication opportunities can all add time.</p>
<noscript><p>The example above uses 12 minutes each way. Enable JavaScript to update the result with the slider.</p></noscript>
</main>
<script>
const slider = document.getElementById('delay');
slider.addEventListener('input', () => {
  document.getElementById('minutes').textContent = slider.value;
  document.getElementById('wait').textContent = `${Number(slider.value) * 2} minutes`;
});
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
<title>A message to Mars</title>
<style>
  body { margin: 0; background: #171d29; color: #f6f1e9; font: 1.1rem/1.6 system-ui, sans-serif; }
  main { max-width: 38rem; margin: auto; padding: 2rem 1.3rem; }
  h1 { line-height: 1.15; color: #ffb088; }
  label, output { display: block; }
  input { width: 100%; margin: 1rem 0; accent-color: #ffb088; }
  input:focus-visible { outline: 3px solid #fff; outline-offset: 5px; }
  .trip { padding: 1rem; border: 1px solid #8793a7; border-radius: .7rem; text-align: center; }
  .result { font-size: 1.5rem; font-weight: bold; color: #ffb088; }
</style>
</head>
<body>
<main>
  <h1>A message to Mars</h1>
  <p>NASA describes commands to the Perseverance rover as taking about 3 to 22 minutes one way, depending on the positions of Earth and Mars.</p>
  <p>If the rover replied immediately and the return signal took just as long, Earth would wait twice the one-way travel time.</p>

  <label for="delay">One-way signal travel time: <strong id="minutes">12 minutes</strong></label>
  <input id="delay" type="range" min="3" max="22" step="1" value="12">

  <div class="trip" aria-label="Signal travels from Earth to Mars, then a reply travels back to Earth">
    Earth → Mars → Earth
  </div>
  <output for="delay" aria-live="polite">
    <span class="result" id="result">24 minutes minimum</span><br>
    <span id="calculation">12 minutes out + 12 minutes back = 24 minutes</span>
  </output>

  <p>This is a minimum <em>in this model</em>: it includes only signal travel and assumes an immediate reply. Rover processing, communication availability, and mission operations can add waiting time. This is not an actual scheduled reply time.</p>
  <noscript><p>The example above uses a 12-minute one-way journey. Enable JavaScript to explore other travel times.</p></noscript>
</main>
<script>
  const slider = document.getElementById('delay');
  slider.addEventListener('input', () => {
    const minutes = Number(slider.value);
    if (slider.value.trim() === '' || !Number.isFinite(minutes) ||
        !Number.isInteger(minutes) || minutes < 3 || minutes > 22) return;
    const total = 2 * minutes;
    document.getElementById('minutes').textContent = minutes + ' minutes';
    document.getElementById('result').textContent = total + ' minutes minimum';
    document.getElementById('calculation').textContent =
      minutes + ' minutes out + ' + minutes + ' minutes back = ' + total + ' minutes';
  });
</script>
</body>
</html>
````

### What changed

**Checks set before the run.** At one-way delays of 3, 12 and 22 minutes, show modeled round trips of 6, 24 and 44 minutes. Preserve the idealized equal return path and immediate reply, distinguish real operations from that model, label the control, support keyboard navigation and show 24 minutes with scripts disabled.

Both pages model the radio trip as twice the one-way delay and put 24 minutes in the initial HTML. The baseline changes the total next to the slider. The skill also updates the outbound and return values in a displayed addition and shows the Earth–Mars–Earth path. Both warn that real mission operations can take longer. Browser checks confirmed 6, 24, 44 and 42 minutes for inputs of 3, 12, 22 and 21 in both pages; the initial 24 remained visible with scripts disabled.

**차이.** 두 페이지 모두 편도 12분일 때 왕복 최소 24분임을 보여 줍니다. 적용 답은 슬라이더를 움직이면 왕복 합계뿐 아니라 가는 시간과 오는 시간을 더하는 식도 함께 바뀝니다.
