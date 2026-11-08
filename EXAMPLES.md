# What changes when you use a writing skill?

Each of the 22 methods below has one new prompt, the full answer without the skill, the full answer with the skill at `standard`, and a short review. Read the whole gallery here or follow a link to one skill. Some pairs give equally useful answers.

**읽는 방법.** 각 스킬마다 같은 질문에 대한 미적용 답안과 `standard` 답안을 나란히 기록했습니다. 각 사례의 ‘차이’에서 무엇이 달라졌는지 한 줄로 볼 수 있습니다. 결과가 비슷한 사례와 수정 전 답안도 그대로 남겼습니다.

## How the examples were made

On 2026-11-08 we ran 22 pairs through Codex CLI 0.167.0. Every answer used a new ephemeral process in a separate, randomly named temporary directory outside the checkout. The request and format constraints were identical within each pair. Only the treatment received the selected `SKILL.md`, `method.json`, locale instructions and the `standard` level, supplied directly in its input. Neither arm received the other answer or the judging criteria. The CLI was instructed to work only from its input, shell and plugin features were disabled, and we checked the event stream for tool use. The model was the CLI default at low reasoning effort; its build identifier was not present in the returned event stream.

We wrote the checks before running the prompts. An authoring agent reviewed both answers against the source with the conditions visible. Two first treatments led to revisions and fresh runs on the original inputs. A sentence-count error in the editorial prompt also led to a corrected pair. The gallery contains 48 observed answers, including all four earlier attempts. Separate browser checks exercised all three HTML pages in Chrome 156.0.8078.80, with scripts both enabled and disabled. These examples show particular writing choices. They do not measure a general quality improvement, host command discovery or reader comprehension.

The per-skill `examples/standard.md` files own the comparisons. After changing one, run `python3 scripts/build_example_gallery.py` from this checkout.

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

**Amazon six-page narrative · Cold-room alarm pilot**

Run on 2026-11-08 • `amazon-six-page-narrative` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Write the opening of an internal decision memo in at most 110 words. Our existing cold-room alarm missed 2 of 18 simulated faults. A second probe costs $240 per room. We can test one room this month. We have no false-alarm measurements or live field data. Leadership must decide whether to buy probes for all eight rooms or run the trial first.

### Without a skill

> We recommend testing a second probe in one room this month before committing $1,920 to probes for all eight rooms. The existing cold-room alarm missed 2 of 18 simulated faults, showing a detection gap, but we do not yet know whether a second probe would close it. We also lack false-alarm measurements and live field data. The trial should measure fault detection and false alarms under defined conditions. Leadership must weigh the delay in broader coverage against the risk of buying eight probes before confirming their benefit.

### With the skill at standard

> I recommend testing a second probe in one room this month before buying probes for all eight rooms. Our existing cold-room alarm missed 2 of 18 simulated faults, showing a detection gap under test conditions. A second probe costs $240 per room, or $1,920 for eight rooms, but we have no evidence yet that it would reduce missed faults. We also lack false-alarm measurements and live field data. The proposed trial should measure missed faults and false alarms under comparable simulated conditions. Leadership can then assess whether broader purchase is justified, while recognizing that field performance remains unverified.

### What changed

**Checks set before the run.** Distinguish simulated faults from field performance; preserve costs, room counts and unknown false alarms; make a decision the supplied evidence supports.

Both recommend the one-room trial and keep field performance unknown. The baseline gives the derived $1,920 total; the skill also states the original $240 per room and confines the proposed comparison to simulated conditions.

**차이.** 두 답 모두 한 방에서 먼저 시험하자고 제안합니다. 스킬을 쓴 답에는 방당 비용과 모의 시험 범위도 명시돼 있습니다.

## answer-with-html

**Answer with HTML · How a fixed delay changes delivery time**

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

## aristotle-syllogism

**Aristotelian syllogistic argument checking · Following a hold rule backwards**

Run on 2026-11-08 • `aristotle-syllogism` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Assess this argument in a few sentences. Every sealed canister is on hold. Item D is on hold. Therefore D is sealed. Assume the two premises are true. Say whether the conclusion follows and give a small example if useful.

### Without a skill

> The conclusion does not follow. The premises say that being sealed guarantees being on hold, but they do not say that only sealed canisters are on hold. For example, D could be an unsealed canister placed on hold for inspection, while every sealed canister is also on hold. Both premises would be true, but the conclusion would be false.

### With the skill at standard

> The premises say that all sealed canisters are on hold and that D is on hold; the conclusion says D is sealed. The conclusion does not follow: being on hold does not establish that an item is sealed or even that it is a canister. For example, a sealed canister and an unsealed item D could both be on hold, satisfying both premises while D remains unsealed. The premises are assumed true; whether D is actually sealed requires additional evidence.

### What changed

**Checks set before the run.** Separate the truth of the premises from whether D must be sealed. A counterexample must keep both premises true while D is on hold but unsealed.

Both give a counterexample that makes the premises true and the conclusion false. The skill also notices that the premises never say D is a canister and that D's actual condition requires evidence. Either answer settles validity.

**차이.** 두 답 모두 반례로 결론이 따라오지 않음을 보입니다. 스킬을 쓴 답은 D가 통이라는 전제조차 없다는 점까지 짚습니다.

## asd-ste100

**ASD-STE100-inspired technical English · Permission to move a tray**

Run on 2026-11-08 • `asd-ste100` 0.1.2 • English • Codex CLI 0.167.0

### Prompt

> Edit this note for a maintenance technician in at most four sentences. Use the glossary name 'transfer tray' for the movable tray. Source: Movement of the tray is permissible only while the handling cart is locked and the load is below 8 kg. The fixed shelf must not be moved. We have not identified why the tray tilted yesterday.

### Without a skill

> Move the transfer tray only when the handling cart is locked and the load is below 8 kg. Do not move the fixed shelf. The cause of yesterday’s transfer tray tilt is still unknown.

### With the skill at standard

> You may move the transfer tray only while the handling cart is locked and the load is below 8 kg. Do not move the fixed shelf. We have not identified why the transfer tray tilted yesterday.

### What changed

**Checks set before the run.** Preserve permission, cart lock and strict less-than-8 kg threshold, the fixed shelf prohibition, correct glossary referent and unknown cause of yesterday's tilt.

The baseline turns permission into the command “Move the transfer tray.” The skill preserves the choice with “You may move,” both safety conditions, the fixed-shelf prohibition and the unknown cause. Neither answer permits a load of exactly 8 kg.

**차이.** 미적용 답안은 허용을 작업 지시로 바꿨습니다. 스킬 답안은 옮겨도 된다는 뜻과 8 kg 미만이라는 조건을 함께 지켰습니다.

## boring-professor

**Boring Professor: literal technical explanation · Why one lock is insufficient**

Run on 2026-11-08 • `boring-professor` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Explain to a systems student, in at most 90 words, why locking only the final write cannot guarantee unique ticket numbers. Two workers can both read 17 before either writes. Each increments its local value and writes 18 under the write lock. Assume the counter starts at 17 and both operations succeed.

### Without a skill

> Locking only the final write prevents simultaneous writes, but it does not protect the full read–increment–write operation. Both workers can read 17, independently compute 18, then take turns acquiring the write lock and writing 18. Both operations succeed, yet both issue ticket 18, and the counter ends at 18 instead of 19. To guarantee unique ticket numbers, protect the entire read–increment–write sequence with one lock or use an atomic increment that returns a distinct value to each worker.

### With the skill at standard

> A lock provides mutual exclusion: only one worker can execute the protected code at a time. If it protects only the final write, both workers can read the initial counter value, 17, before either writes. Each independently computes 18. The lock then serializes two successful writes of 18, so both workers obtain the same ticket number.
>
> Uniqueness requires protecting the entire read–increment–write operation with the same lock, or using an atomic increment that returns a distinct value for each operation.

### What changed

**Checks set before the run.** Name the protected operation and the unprotected read–modify–write sequence. Trace both workers to 18. Keep the stated assumptions and avoid a metaphor.

Both trace two reads of 17 and two writes of 18, and suggest protecting the full operation. The skill defines mutual exclusion first; the baseline spells out that the counter ends at 18 instead of 19. Both are usable literal explanations.

**차이.** 두 답 모두 18번이 두 번 발급되는 과정을 설명합니다. 스킬 답안은 먼저 상호 배제를 정의하고, 미적용 답안은 최종 값이 19가 아닌 18임을 강조합니다.

## diataxis

**Diátaxis documentation · A lookup entry for snapshot retention**

Run on 2026-11-08 • `diataxis` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Write a short entry for people who already use our backup CLI and want to look up the flag `--keep N`. It accepts integers 1 through 14, defaults to 3, and applies only to completed snapshots. Pending snapshots stay untouched. No installation steps are needed.

### Without a skill

> `--keep N`
>
> Keep the N most recent completed snapshots. Accepts integers from 1 to 14; defaults to 3. Pending snapshots remain untouched.

### With the skill at standard

> ### `--keep N`
>
> Sets how many completed snapshots to keep.
>
> | Value | Constraint |
> | --- | --- |
> | Type | Integer |
> | Allowed range | 1–14 |
> | Default | 3 |
> | Applies to | Completed snapshots only |
>
> Pending snapshots stay untouched.

### What changed

**Checks set before the run.** Serve lookup readers with the flag's exact spelling, range, default and completed-only scope. Leave pending snapshots untouched and avoid unsupported CLI commands.

Both give the correct range, default and scope. The baseline adds “most recent,” an ordering the supplied specification does not promise. The skill uses a small lookup table and leaves the ordering unspecified.

**차이.** 미적용 답안은 명세에 없는 ‘가장 최근’이라는 순서를 덧붙였습니다. 스킬 답안은 조회에 필요한 범위·기본값·적용 대상을 표로 보여 줍니다.

## eli5

**ELI5: explain to a five-year-old · How a zipper closes**

Run on 2026-11-08 • `eli5` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Explain to a five-year-old, in at most four sentences, how this zipper closes. Its two rows of teeth start apart. Moving the slider brings the rows together so their teeth fit between each other. A missing tooth can leave a gap.

### Without a skill

> A zipper has two rows of little teeth that start apart. When you pull the slider, it brings the rows together so the teeth fit between each other and hold the zipper closed. If a tooth is missing, it can leave a little gap.

### With the skill at standard

> Look at the zipper on a jacket: its two rows of little teeth start apart. When you pull the slider—the little piece that moves along the zipper—it brings the rows together. The teeth fit between each other, closing the zipper. If a tooth is missing, there can be a gap.

### What changed

**Checks set before the run.** Use a pictureable hand action, keep both rows and the slider's role, and retain the possible gap without implying every zipper fails.

Both give a literal sequence and preserve the possible gap. The skill places the zipper on a jacket and identifies the slider as the moving piece; the baseline is shorter. No child evaluated the language.

**차이.** 두 답 모두 이가 빠졌을 때 틈이 생길 수 있음을 설명합니다. 스킬 답안은 재킷의 지퍼를 예로 들어 슬라이더가 어떤 부품인지 알려 줍니다.

## federal-plain-language

**Federal Plain Language-inspired explanation · A correction without a new deadline**

Run on 2026-11-08 • `federal-plain-language` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Write a notice for applicants in no more than 65 words. Applications already submitted can be corrected through the portal until 4 p.m. Friday, but only if the status is 'Returned'. A correction does not change the original filing deadline. Paper corrections are not accepted.

### Without a skill

> Notice to Applicants
>
> Applications already submitted may be corrected through the portal until 4 p.m. Friday, but only if their status is “Returned.” A correction does not change the original filing deadline. Paper corrections are not accepted.

### With the skill at standard

> You can correct an application you have already submitted through the portal until 4 p.m. Friday, but only if its status is 'Returned'.
>
> A correction does not change the original filing deadline. Paper corrections are not accepted.

### What changed

**Checks set before the run.** Keep the status restriction, exact portal deadline, unchanged original deadline and paper exclusion. Let an applicant tell whether they can act.

Both retain the status restriction, time, original deadline and paper exclusion. The skill addresses the applicant as “you” and puts the two remaining constraints in a separate paragraph. The baseline adds a notice heading.

**차이.** 두 답 모두 수정 조건과 기한을 보존합니다. 스킬 답안은 신청자에게 직접 말하고, 서면 접수 제한을 따로 모았습니다.

## feynman-technique

**Feynman-inspired explanation and gap checking · Why a full buffer overwrites an item**

Run on 2026-11-08 • `feynman-technique` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Explain a two-slot buffer to a new operator in a short paragraph, without asking them a question. Each arrival writes to the next slot; after the second slot, writing returns to the first. Starting empty, A, B and C arrive in that order. The policy for simultaneous arrivals is unknown.

### Without a skill

> A two-slot buffer stores items in two positions, writing to each slot in turn. Starting empty, A goes into the first slot and B into the second. Writing then returns to the first slot, so C replaces A, leaving C in the first slot and B in the second. How simultaneous arrivals are handled is unknown.

### With the skill at standard

> A two-slot buffer has two places to hold items. Each arrival writes to the next slot, returning to the first after the second and replacing anything already there. Starting empty, A goes into slot 1, B into slot 2, and C into slot 1, replacing A. The buffer then holds C in slot 1 and B in slot 2; the next arrival will write to slot 2. The policy for simultaneous arrivals is unknown, so we cannot say how those arrivals would be ordered or stored.

### What changed

**Checks set before the run.** Explain where A, B and C go and why C overwrites A; leave simultaneous arrivals unresolved. At standard a learner quiz is unnecessary.

Both trace A, B and C correctly and leave simultaneous arrivals unresolved. The skill goes one step further and predicts which slot the next arrival will use. A learner’s response was not observed.

**차이.** 두 답 모두 C가 왜 A를 덮어쓰는지 설명합니다. 스킬 답안은 다음 항목이 어느 칸에 들어갈지도 예측합니다.

## google-design-doc

**Google-inspired design document · Choosing an index for a search service**

Run on 2026-11-08 • `google-design-doc` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Write a design proposal excerpt of at most 115 words. Goal: reduce lookups that currently scan the whole log. Option A adds an index updated during each write. Option B rebuilds the index every 10 minutes. Search must show records within 2 minutes; no latency measurements exist. Changing record format is out of scope.

### Without a skill

> We propose adding an index to reduce lookups that currently scan the whole log, without changing the record format.
>
> Option A updates the index during each write. This supports the two-minute search visibility requirement, provided indexing completes within that window, but adds work to the write path.
>
> Option B rebuilds the index every 10 minutes. As proposed, it cannot meet the two-minute visibility requirement.
>
> Recommend Option A, subject to validation. No latency measurements exist, so performance gains and write overhead remain unverified. Measure lookup latency, write latency, and time to search visibility under representative load before rollout.

### With the skill at standard

> Proposal for review: choose Option A, subject to validation that records become searchable within 2 minutes. The goal is to reduce lookups that currently scan the whole log; record-format changes are out of scope.
>
> On each write, Option A updates an index; searches use that index to locate records. This adds write work. If an index update fails, search visibility may exceed 2 minutes; failure handling remains unresolved.
>
> Option B rebuilds the index every 10 minutes, avoiding per-write index updates but failing the visibility requirement without another mechanism.
>
> No latency measurements exist. Before approval, measure lookup latency, write overhead, and write-to-search visibility, including index-update failures.

### What changed

**Checks set before the run.** Compare the write-path cost with rebuild staleness, honor the two-minute requirement and unchanged record format, avoid invented measurements and identify what to test.

Both recommend A conditionally and reject a 10-minute rebuild as insufficient for a 2-minute deadline. The skill adds a concrete unresolved design question about failed index updates. Neither presents an unmeasured performance gain as observed.

**차이.** 두 답 모두 A를 조건부로 권합니다. 스킬 답안은 인덱스 갱신에 실패해 검색 반영이 늦어지는 경우까지 시험 대상으로 남깁니다.

## gtm-formal

**GTM-inspired formal mathematical explanation · When preimages preserve intersections**

Run on 2026-11-08 • `gtm-formal` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> For a graduate maths reader, prove in at most 110 words that for any function f:X→Y and any subsets A and B of Y, the inverse image of their intersection equals the intersection of their inverse images. State whether f must be injective and cover empty sets.

### Without a skill

> For every \(x\in X\),
> \[
> \begin{aligned}
> x\in f^{-1}(A\cap B)
> &\iff f(x)\in A\cap B\\
> &\iff f(x)\in A\ \text{and}\ f(x)\in B\\
> &\iff x\in f^{-1}(A)\cap f^{-1}(B).
> \end{aligned}
> \]
> Thus, by extensionality,
> \[
> f^{-1}(A\cap B)=f^{-1}(A)\cap f^{-1}(B).
> \]
> No injectivity assumption is needed. The argument also covers empty sets: \(f^{-1}(\varnothing)=\varnothing\), so if either \(A\) or \(B\) is empty, both sides are empty. If \(X=\varnothing\), both sides are likewise empty.

### With the skill at standard

> For \(S\subseteq Y\), define \(f^{-1}(S)=\{x\in X:f(x)\in S\}\). Let \(A,B\subseteq Y\). For every \(x\in X\),
> \[
> \begin{aligned}
> x\in f^{-1}(A\cap B)
> &\iff f(x)\in A\cap B\\
> &\iff f(x)\in A\ \text{and}\ f(x)\in B\\
> &\iff x\in f^{-1}(A)\cap f^{-1}(B).
> \end{aligned}
> \]
> Thus, by extensionality,
> \[
> f^{-1}(A\cap B)=f^{-1}(A)\cap f^{-1}(B).
> \]
> Injectivity is unnecessary: only the definition of inverse image is used. If \(A=\varnothing\) or \(B=\varnothing\), both sides are empty because \(f^{-1}(\varnothing)=\varnothing\). If \(X=\varnothing\), both sides are likewise empty.

### What changed

**Checks set before the run.** Quantify a general element of X and give equivalences in both directions; do not introduce an inverse function or require injectivity; account for empty sets.

Both prove the identity for each element of X, address empty sets, and explain why injectivity is unnecessary. The skill explicitly defines the inverse image before using it. The mathematical result is the same.

**차이.** 두 증명 모두 공집합과 단사성 조건을 다룹니다. 스킬 답안은 사용하는 기호의 뜻인 역상을 먼저 정의합니다.

## hunminjeongeum

**Hunminjeongeum-inspired purpose-first explanation · A guide for finding the correct locker**

Run on 2026-11-08 • `hunminjeongeum` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Explain in at most 80 words why we are rewriting our depot locker guide. Couriers at Gate 2 see locker numbers duplicated across two wings. The new guide will pair each locker number with its wing letter. It covers only Gate 2. No one has yet tested whether couriers find parcels faster.

### Without a skill

> We’re rewriting the depot locker guide because couriers at Gate 2 encounter the same locker numbers in two wings. The new guide will pair each locker number with its wing letter to make locations clearer. It covers only Gate 2. Whether this helps couriers find parcels faster has not yet been tested.

### With the skill at standard

> Couriers at Gate 2 see the same locker numbers in two wings, making the number alone insufficient to identify the right locker. We are rewriting the guide to pair each locker number with its wing letter so couriers can distinguish between them. The guide covers only Gate 2. No one has yet tested whether this change helps couriers find parcels faster.

### What changed

**Checks set before the run.** Open with the courier's concrete difficulty, connect wing letters to duplicates, and end on the same task while retaining Gate 2 and the untested benefit.

Both cover the Gate 2 scope and untested benefit. The baseline opens with the company's reason for rewriting; the skill opens with the obstacle faced by the couriers, then returns to their task in the final sentence.

**차이.** 두 답 모두 개선 효과를 단정하지 않습니다. 스킬 답안은 조직의 개편 결정 대신 배달원이 마주한 문제에서 시작합니다.

## ietf-rfc

**RFC-style technical specification · Optional reconnect with a hard deadline**

Run on 2026-11-08 • `ietf-rfc` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Draft a short internal protocol requirement using BCP 14 notation. A client may reconnect once only after error E7. It must wait at least 4 seconds before reconnecting. Error E8 does not permit a reconnect. There is no registry action. Keep the text to 90 words or fewer.

### Without a skill

> The key words “MUST”, “MUST NOT”, and “MAY” in this document are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174).
>
> A client MAY reconnect once after receiving error E7. It MUST wait at least 4 seconds after receiving E7 before reconnecting. It MUST NOT make a second reconnection attempt. A client MUST NOT reconnect after error E8 or any error other than E7.
>
> This document requires no registry action.

### With the skill at standard

> # Reconnection Requirement
>
> Status: Internal draft.
>
> This specification governs client reconnection after an error. Uppercase keywords MUST, MUST NOT, and MAY have their BCP 14 meanings (RFC 2119 and RFC 8174, normative references).
>
> After error E7, the client MAY reconnect once. It MUST wait at least 4 seconds after E7 before reconnecting. The client MUST NOT reconnect after E8 or any error other than E7.
>
> Security considerations: This rule does not define authentication for reconnected sessions.
>
> IANA considerations: No registry action is required.

### What changed

**Checks set before the run.** Keep reconnect optional and limited to once after E7, preserve the lower wait bound, exclude E8 and identify the absence of registry action. Use requirement keywords consistently.

Both specify the optional single reconnect, waiting period, E8 exclusion and no registry action. The skill adds explicit document status and a security boundary; the baseline states the second-attempt prohibition directly. For this narrow request the shorter baseline also works.

**차이.** 두 답 모두 재연결 횟수와 대기 시간을 정확히 적었습니다. 스킬 답안에는 문서 상태와 보안 범위가 추가돼 더 길어졌습니다.

## imrad

**IMRaD research-report structure · Reporting chipped parts in a test**

Run on 2026-11-08 • `imrad` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Turn these notes into a brief research abstract of no more than 100 words. Question: does liner L reduce chipped parts in a simulated route? Twenty crates with L and twenty without it followed one route. Staff counted 3 chipped parts with L and 7 without. We do not know how many parts were in each crate or which crates contained the chips.

### Without a skill

> We assessed whether liner L reduces chipped parts during a simulated route. Twenty crates with L and twenty without L followed the same route. Staff counted 3 chipped parts with L and 7 without. Although fewer chipped parts were observed with L, the number of parts per crate and the distribution of chips across crates were unknown. These limitations prevent calculation of chipping rates and assessment of crate-level variability. The results suggest a possible benefit but do not establish that L reduces chipping.

### With the skill at standard

> **Introduction:** We assessed whether liner L reduces chipped parts on a simulated route.
>
> **Methods:** Twenty crates with L and twenty without L followed one route. Staff counted chipped parts. The number of parts per crate and the distribution of chipped parts across crates were unknown.
>
> **Results:** Staff recorded 3 chipped parts with L and 7 without L.
>
> **Discussion:** Fewer chipped parts were observed with L, but missing part denominators and crate-level data prevent estimating chipping rates or the proportion of crates affected. This single-route simulation does not establish effects on other routes.

### What changed

**Checks set before the run.** Separate the comparison, method, observed counts and interpretation. Do not infer crate-level percentages, chip rates per part, or effects beyond the simulated route.

Both report counts of chipped parts rather than rates per crate. The skill labels the four section roles and makes the one-route limit explicit. The baseline reads as one continuous abstract.

**차이.** 두 답 모두 파손 부품 수를 상자별 파손률로 바꾸지 않았습니다. 스킬 답안은 네 부분을 구분하고 결론의 적용 범위를 한 경로로 한정합니다.

## korean-plain-language

**Korean plain-language companion · 내보내기 예약 안내**

Run on 2026-11-08 • `korean-plain-language` 0.1.1 • Korean • Codex CLI 0.167.0

### Prompt

> 앱 사용자에게 보여 줄 문구만 네 문장 이내로 다듬어 주세요. 원래 해요체와 버튼 이름은 유지해 주세요. 원문: ‘내보내기 예약’은 관리자에게만 가능한 동작이에요. ‘예약’을 눌러도 지금 파일이 전송되지는 않아요. 전송은 확인이 끝난 후에만 시작될 수 있어요. 누가 확인하는지는 아직 정해지지 않았어요.

### Without a skill

> ‘내보내기 예약’은 관리자만 할 수 있어요. ‘예약’을 눌러도 파일이 바로 전송되지는 않아요. 전송은 확인이 끝난 뒤에만 시작할 수 있어요. 확인 담당자는 아직 정해지지 않았어요.

### With the skill at standard

> ‘내보내기 예약’은 관리자만 할 수 있어요. ‘예약’을 눌러도 지금 파일이 전송되지는 않아요. 확인이 끝난 후에만 전송을 시작할 수 있어요. 누가 확인할지는 아직 정해지지 않았어요.

### What changed

**Checks set before the run.** 관리자만 가능한 동작, 실제 버튼 이름, 즉시 전송되지 않음, 확인 후에도 시작은 가능성이라는 점, 확인 주체 미정과 해요체를 보존한다.

Both preserve 해요체, both labels, the administrator restriction, and the unknown person responsible. The baseline says ‘확인 담당자’; the skill says ‘누가 확인할지’. Both keep confirmation necessary without promising immediate transmission.

**차이.** 두 답 모두 조건과 해요체를 지켰습니다. 확인할 사람이 아직 정해지지 않은 점을 하나는 ‘확인 담당자’, 다른 하나는 ‘누가 확인할지’로 표현합니다.

## microsoft-writing-style

**Microsoft-inspired technology writing · Restoring a workspace from an archive**

Run on 2026-11-08 • `microsoft-writing-style` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Rewrite this help text for someone using the app. Keep it under 70 words. Only workspace owners may select the button labelled 'Restore copy'. They may do so only after the archive has been verified. The action creates a separate copy; it does not change the current workspace. A storage quota might block creation.

### Without a skill

> After the archive has been verified, workspace owners can select **Restore copy** to create a separate copy. The current workspace stays unchanged. If there isn’t enough available storage within your quota, the copy can’t be created.

### With the skill at standard

> Only workspace owners may select **Restore copy**, and only after the archive has been verified. This action creates a separate copy without changing the current workspace. A storage quota might prevent the copy from being created.

### What changed

**Checks set before the run.** Keep the exact UI label, owner restriction, verified archive prerequisite, separate copy and unchanged workspace. Preserve quota as a possibility.

Both preserve the label and separate-copy behavior. The baseline omits the explicit ‘only’ on the owner restriction and gives a more specific interpretation of the quota than the source. The skill keeps both restrictions and the possibility of a block visible.

**차이.** 미적용 답안에서는 소유자만 가능하다는 제한이 약해졌습니다. 스킬 답안은 권한·검증 조건을 버튼 이름 바로 앞에 놓습니다.

## minto-pyramid

**Minto-inspired Pyramid Principle · Where should we spend the training budget?**

Run on 2026-11-08 • `minto-pyramid` 0.2.1 • English • Codex CLI 0.167.0

### Prompt

> Write only the opening paragraph of a decision note in under 85 words. Choose between funding a second live induction session and printing more manuals. Last intake, 11 of 40 volunteers missed the only session because of shift clashes. All 40 already received a manual. The budget covers one option. A second session could run on Saturdays if a trainer is available. Its effect on attendance has not been measured.

### Without a skill

> Fund a second live induction session rather than print more manuals, subject to confirming a trainer for Saturday. Last intake, 11 of 40 volunteers missed the only session because of shift clashes, while all 40 already received a manual. A second session offers a way to address that scheduling barrier, though its effect on attendance is unmeasured; attendance should be tracked to assess whether the additional session helps.

### With the skill at standard

> Last intake, all 40 volunteers received a manual, but 11 missed the only live induction session because of shift clashes. With funding for one option, should we add a session or print more manuals? Fund a second session, conditional on trainer availability for a Saturday session, because it could address the scheduling barrier while more manuals would duplicate existing provision. Its effect on attendance remains unmeasured.

### What changed

**Checks set before the run.** Answer the decision with a supported reason. Keep the 11/40 denominator, existing manuals, either/or budget, trainer dependency and unmeasured effect. Stay within the opening.

Both recommend a second session, subject to trainer availability, and retain the unmeasured effect. The baseline leads with the recommendation; the skill lays out the evidence, asks the decision question and then answers. The latter also states the one-option budget explicitly.

**차이.** 두 답 모두 추가 교육을 조건부로 권합니다. 미적용 답은 권고를 먼저 쓰고, 스킬 답은 근거와 질문을 놓은 뒤 권고합니다.

## new-harts-rules

**New Hart’s Rules source-assisted editing · House spelling and a protected citation**

Run on 2026-11-08 • `new-harts-rules` 0.1.2 • English • Codex CLI 0.167.0

### Prompt

> Copyedit the sentence below, then add one short editorial note. House style requires 'on-site' before a noun in editable prose. Quoted titles must stay verbatim. No book passage is supplied for serial-comma style. Draft: Our onsite team read the article ‘The Onsite Team’ and checked labels, seals and lids.

### Without a skill

> Our on-site team read the article ‘The Onsite Team’ and checked labels, seals and lids.
>
> Editorial note: Changed “onsite” to “on-site” before a noun; preserved the quoted title and existing comma style.

### With the skill at standard

> Our on-site team read the article ‘The Onsite Team’ and checked labels, seals and lids.
>
> Editorial note: ‘On-site’ follows house style; the quoted title stays verbatim. Serial-comma usage is unchanged because no relevant passage from New Hart’s Rules, second edition (2014), was supplied.

### What changed

**Checks set before the run.** Change the editable modifier, preserve the exact quoted title and list facts. Attribute the spelling to house style and avoid claiming a book rule for the unresolved comma.

Both final edits change only the editable spelling and preserve the quoted title and list. The skill's note identifies house style and the absent book passage; the baseline explains what it changed without naming the authority. The earlier treatments and the corrected fixture are documented below.

**차이.** 두 최종 답안의 편집 문장은 같습니다. 스킬 답안은 사내 표기와 확인하지 못한 책의 규칙을 구분합니다. 수정 전 답안도 아래에 남겼습니다.

<details>
<summary>Earlier prompt, answers and revision</summary>

The earlier prompt said “two sentences” but supplied one. We corrected that mismatch before publishing the main pair above. The three earlier answers below used this same original prompt.

> Copyedit the two sentences below, then add one short editorial note. House style requires 'on-site' before a noun in editable prose. Quoted titles must stay verbatim. No book passage is supplied for serial-comma style. Draft: Our onsite team read the article ‘The Onsite Team’ and checked labels, seals and lids.

**Without a skill**

> Our on-site team read the article ‘The Onsite Team’ and checked labels, seals and lids.
>
> Editorial note: Changed “onsite” to “on-site” in prose; preserved the quoted title and existing serial-comma style because no book passage was supplied.

**First treatment, version 0.1.1**

> Our on-site team read the article ‘The Onsite Team’ and checked labels, seals and lids.
>
> Editorial note: Applied new-harts-rules v0.1.1 at standard level, referencing the second edition (2014). ‘On-site’ follows house style; the quoted title is unchanged. Serial-comma style remains unverified, so the existing punctuation is retained.

The note named the method version and described an edition as a reference without a relevant passage. We clarified the difference between an editorial note and a method audit, then reran the original prompt in a fresh context.

**Revised treatment, version 0.1.2**

> Our on-site team read the article ‘The Onsite Team’ and checked labels, seals and lids.
>
> Editorial note: Applied house style to ‘on-site’; preserved the quoted title verbatim. Left serial-comma style unchanged because no relevant passage from New Hart’s Rules, second edition (2014), was supplied.

</details>

## nist-technical-publication

**NIST-inspired technical publication · Reporting a temperature test**

Run on 2026-11-08 • `nist-technical-publication` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Write a traceable measurement summary in at most 75 words. At a chamber setpoint of 30 °C, sensor Q reported 18.40 mV with stated uncertainty ±0.06 mV. Five readings were taken. The record gives neither their individual values nor a coverage factor. No NIST publication identifier is assigned.

### Without a skill

> At a chamber setpoint of 30 °C, sensor Q reported 18.40 mV with stated uncertainty ±0.06 mV. Five readings were taken, but individual values are unavailable, preventing independent assessment of variability. The coverage factor and uncertainty coverage probability are unspecified. No NIST publication identifier is assigned. The supplied record does not establish metrological traceability.

### With the skill at standard

> At a chamber setpoint of 30 °C, five readings were taken with sensor Q. The reported value was 18.40 mV with a stated uncertainty of ±0.06 mV. The record provides neither the individual readings nor a coverage factor; it does not establish that the reported value is a mean or specify a coverage probability. No NIST publication identifier is assigned.

### What changed

**Checks set before the run.** Retain the distinction between setpoint and measured voltage, decimal precision, units, count, missing raw values and coverage factor. Do not invent an average, interval interpretation or identifier.

Both preserve the setpoint, the 18.40 mV precision, the stated uncertainty and the missing data. The baseline flags unestablished metrological traceability. The skill specifically avoids inferring that 18.40 mV is a mean. Both leave coverage and the identifier unresolved.

**차이.** 두 답 모두 정밀도와 불확도를 지켰습니다. 스킬 답안은 18.40 mV를 평균으로 단정하지 않았고, 미적용 답안은 계측학적 소급성을 입증하지 못했다고 적었습니다.

## orwell-six-rules

**Orwell: six rules for clear prose · Removing filler while keeping uncertainty**

Run on 2026-11-08 • `orwell-six-rules` 0.1.2 • English • Codex CLI 0.167.0

### Prompt

> Edit for a general reader in at most 55 words. Source: At the present moment in time the team is in the process of conducting an assessment of a crack near the latch. The latch was damaged during transit. The responsible party has not been identified. Operation may resume only after inspection.

### Without a skill

> The team is assessing a crack near the latch, which was damaged during transit. It is not yet known who is responsible for the damage. Operation may resume only after inspection.

### With the skill at standard

> The team is assessing a crack near the latch. The latch was damaged during transit. The responsible party remains unknown. Operation may resume only after inspection.

### What changed

**Checks set before the run.** Remove filler; keep the assessment ongoing and the location of the crack, damage in transit, unknown actor and inspection as a necessary condition for permission.

Both cut the opening filler and preserve the inspection condition and unknown actor. The skill gives the damage its own sentence and repeats ‘latch’, making its referent explicit. The baseline attaches it as a relative clause.

**차이.** 두 답 모두 군더더기를 덜었습니다. 스킬 답안은 파손된 대상이 걸쇠라는 점을 별도 문장으로 명확하게 했습니다.

## socratic-self-questioning

**Socratic self-questioning · Can faster replies establish a cause?**

Run on 2026-11-08 • `socratic-self-questioning` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Our team claims a new rota caused faster replies because median reply time fell from 13 minutes to 9 minutes during its first week. Ticket volume fell too; no comparison team was tracked. Give a finished revision of that claim in at most 70 words, not a dialogue.

### Without a skill

> Median reply time fell from 13 to 9 minutes during the new rota’s first week. This suggests an improvement, but it does not establish that the rota caused faster replies: ticket volume also fell, and no comparison team was tracked. Further observation, accounting for workload and using a comparison group, would help assess the rota’s effect.

### With the skill at standard

> Median reply time fell from 13 minutes to 9 minutes during the new rota’s first week. This shows faster median replies that week, but does not establish that the rota caused the improvement. Ticket volume also fell, which could help explain the change, and no comparison team was tracked to help distinguish the rota’s effect from other influences.

### What changed

**Checks set before the run.** Preserve the median, numbers and week; separate observation from causation; treat volume as a possible explanation rather than a demonstrated cause.

Both replace the causal claim with the observed median change and flag volume and the missing comparison. The baseline proposes further observation; the skill keeps the revision focused on what the current evidence can support.

**차이.** 두 답 모두 13분에서 9분으로 줄었다는 관찰과 원인을 구분합니다. 미적용 답안은 후속 관찰을 제안하고 스킬 답안은 현재 근거로 할 수 있는 주장에 집중합니다.

## steve-jobs-presentation

**Jobs-inspired presentation structure · A presentation to a mapping team**

Run on 2026-11-08 • `steve-jobs-presentation` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Write 3 short speaker beats for a team deciding whether to try a map export tool. On one test laptop it exported 6 GB in 70 seconds. No field run has been timed. The audience works offline; production export time is unknown. Do not invent more demo results.

### Without a skill

> 1. “On one test laptop, the tool exported 6 GB in 70 seconds. That gives us a reason to try it.”
> 2. “We haven’t timed a field run, so production export time is still unknown.”
> 3. “Let’s test it in our offline workflow and time a representative export before deciding whether to adopt it.”

### With the skill at standard

> 1. “Can this tool help us get maps ready for offline work? First, here’s what we’ve measured: it exported 6 GB in 70 seconds on one test laptop.”
>
> 2. “That gives us a starting point. No field run has been timed, and production export time is still unknown.”
>
> 3. “Let’s try a timed export with a workload and equipment that reflect our offline work. That will help us judge whether it fits our preparation window.”

### What changed

**Checks set before the run.** Connect the benefit to the offline audience; retain device, size and time; distinguish the demonstration from field performance and give a supported next step.

Both retain the test laptop, 6 GB, 70 seconds and the missing field measurement. The skill opens with the team's offline need and proposes timing representative equipment. The baseline also offers a usable three-beat presentation.

**차이.** 두 답 모두 시험 수치를 현장 성능으로 일반화하지 않습니다. 스킬 답안은 오프라인에서 지도를 준비하는 팀의 질문으로 발표를 시작합니다.
