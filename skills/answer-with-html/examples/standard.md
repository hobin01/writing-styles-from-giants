# Answer with HTML · How a fixed delay changes delivery time

Run on 2026-11-08 • `answer-with-html` 0.1.2 • English • Codex CLI 0.167.0

### Prompt

> Return only one short self-contained HTML page. Teach why a courier travelling at 12 km/h with a fixed 10-minute loading delay takes 30 minutes to deliver 4 km. Add one distance slider from 0 to 8 whole km and update the total minutes. The initial page must show the 4 km result even without JavaScript. No internet dependencies.

### Without a skill

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Courier delivery time</title>
<style>
body{font:18px/1.6 system-ui,sans-serif;max-width:580px;margin:60px auto;padding:0 24px;color:#183143;background:#f4f8fb}
main{background:white;padding:28px;border-radius:18px}
h1{font-size:1.7rem;line-height:1.2}
input{width:100%;accent-color:#087e8b}
.result{font-size:1.5rem;font-weight:700;color:#087e8b}
</style>
</head>
<body>
<main>
<h1>A delivery includes loading time</h1>
<p>At <strong>12 km/h</strong>, the courier travels 1 km in 60 ÷ 12 = <strong>5 minutes</strong>.</p>
<p>For 4 km, travelling takes 4 × 5 = 20 minutes. Add the fixed 10-minute loading delay: <strong>20 + 10 = 30 minutes</strong>.</p>
<label for="distance">Delivery distance: <output id="km" for="distance">4</output> km</label>
<input id="distance" type="range" min="0" max="8" step="1" value="4">
<p>Total time = 10 minutes loading + 5 minutes × distance.</p>
<p class="result" aria-live="polite"><output id="total" for="distance">30</output> minutes total</p>
<p>Even at 0 km, the fixed loading delay takes 10 minutes.</p>
</main>
<script>
const distance = document.getElementById('distance');
function update() {
  document.getElementById('km').textContent = distance.value;
  document.getElementById('total').textContent = 10 + 5 * Number(distance.value);
}
distance.addEventListener('input', update);
update();
</script>
</body>
</html>
```

### With the skill at standard

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Courier delivery time</title>
<style>
body{font:1.1rem/1.6 system-ui,sans-serif;max-width:36rem;margin:3rem auto;padding:0 1.2rem;color:#183044;background:#f5f8fa}
main{background:white;padding:1.6rem;border-radius:1rem}
h1{font-size:1.6rem;line-height:1.2}
.result{font-size:1.8rem;font-weight:700}
input{display:block;width:100%;margin:1rem 0;accent-color:#176b87}
.formula{padding:1rem;background:#eaf4f7;border-radius:.5rem}
small{display:block}
</style>
</head>
<body>
<main>
<h1>Why does 4 km take 30 minutes?</h1>
<p>At a steady <strong>12 km/h</strong>, each kilometre takes <strong>5 minutes</strong>: 60 ÷ 12 = 5. Travelling 4 km takes 20 minutes. Add the fixed 10-minute loading delay, and the delivery takes 30 minutes.</p>
<p class="formula">Total minutes = 10 + (5 × distance in km)</p>
<label for="distance">Distance (whole km): <output id="distance-value" for="distance">4</output> km</label>
<input id="distance" type="range" min="0" max="8" step="1" value="4" aria-describedby="assumption">
<div aria-live="polite" aria-atomic="true">
<p class="result"><span id="total">30</span> minutes total</p>
<p id="calculation">10 minutes loading + 20 minutes travelling = 30 minutes.</p>
</div>
<small id="assumption">Assumes constant speed and no other delays. Loading still takes 10 minutes at 0 km.</small>
<noscript><p>The example above shows 4 km. Enable JavaScript to explore other distances.</p></noscript>
</main>
<script>
const slider = document.getElementById('distance');
function update() {
  const raw = slider.value;
  const distance = Number(raw);
  if (raw.trim() === '' || !Number.isFinite(distance) ||
      distance < 0 || distance > 8 || !Number.isInteger(distance)) return;
  const travel = distance * 5;
  const total = 10 + travel;
  document.getElementById('distance-value').textContent = distance;
  document.getElementById('total').textContent = total;
  document.getElementById('calculation').textContent =
    `10 minutes loading + ${travel} minutes travelling = ${total} minutes.`;
}
slider.addEventListener('input', update);
update();
</script>
</body>
</html>
```

### What changed

**Checks set before the run.** The formula gives 10, 30 and 50 minutes at 0, 4 and 8 km. The native control needs a label, keyboard access, and a readable initial answer without scripts.

Both final pages produced 30, 10 and 50 minutes at 4, 0 and 8 km. The revised page explains the fixed delay and adds the changing travel-time breakdown. The first treatment exposed the agent’s unfinished verification as a lesson footer. We clarified where to report verification, reran the same request and preserved that earlier output below.

**차이.** 두 페이지 모두 거리별 시간을 정확히 계산했습니다. 첫 스킬 답안은 검증 상태를 수업 본문에 노출해 지침을 고치고 다시 실행했습니다.

Chrome 156.0.8078.80 displayed 30 minutes initially and with JavaScript disabled. With JavaScript enabled, Home, End and ArrowLeft on the distance slider produced 10, 50 and 45 minutes. Both final pages and the earlier treatment stayed within 320 CSS pixels and made no external requests.

<details>
<summary>First treatment · version 0.1.1</summary>

The page calculated correctly, but its footer addressed the agent's browser checks instead of the lesson. The new instruction keeps test status in a separate delivery note when the requested format allows it. The rerun used the original input and a new context.

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Courier delivery time</title>
<style>
body{font:1.1rem/1.6 system-ui,sans-serif;max-width:38rem;margin:3rem auto;padding:0 1rem;color:#183047;background:#f5f8fb}
main{background:white;padding:1.5rem;border-radius:1rem}
h1{font-size:1.6rem;line-height:1.2}
.result{font-size:1.5rem;font-weight:700;color:#075d64}
input{width:100%;accent-color:#075d64}
.formula{padding:1rem;background:#edf5f5;border-radius:.5rem}
small{color:#526474}
</style>
</head>
<body>
<main>
<h1>Why does 4 km take 30 minutes?</h1>
<p>At 12 km/h, the courier travels 1 km every 5 minutes. Travelling 4 km therefore takes 20 minutes. Add the fixed 10-minute loading delay: <strong>30 minutes total.</strong></p>
<p class="formula">Total minutes = 10 + (distance ÷ 12) × 60<br>
= 10 + 5 × distance in km</p>
<section aria-labelledby="explore">
<h2 id="explore">Try another distance</h2>
<label for="distance">Distance: <output id="distance-value" for="distance">4</output> km</label>
<input id="distance" type="range" min="0" max="8" step="1" value="4">
<div aria-live="polite" aria-atomic="true">
<p id="breakdown">10 minutes loading + 20 minutes travelling</p>
<p class="result">Total: <span id="total">30</span> minutes</p>
</div>
<p><small>Assumes constant speed and no other delays. Loading takes 10 minutes even at 0 km; at 8 km, the total is 50 minutes.</small></p>
</section>
<footer><small>Self-contained; no internet needed. Browser execution and keyboard checks were not run.</small></footer>
</main>
<script>
const slider = document.getElementById('distance');
slider.addEventListener('input', () => {
  const raw = slider.value;
  const distance = Number(raw);
  if (raw.trim() === '' || !Number.isFinite(distance) ||
      !Number.isInteger(distance) || distance < 0 || distance > 8) return;
  const travel = distance * 5;
  document.getElementById('distance-value').textContent = distance;
  document.getElementById('breakdown').textContent =
    `10 minutes loading + ${travel} minutes travelling`;
  document.getElementById('total').textContent = 10 + travel;
});
</script>
</body>
</html>
```

</details>
