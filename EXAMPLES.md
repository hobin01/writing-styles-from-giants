# What changes when you use a writing skill?

**22 real cases, answered twice.** Compare a [DNS record that still appears missing](#feynman-technique), [LIGO’s first black-hole merger observation](#imrad), or [Seoul’s redesigned subway map](#hunminjeongeum). Each entry links its sources and shows the full answers to the same request, with and without the writing skill.

**읽는 방법.** 관심 있는 사례를 골라 질문과 실제 답안 두 개를 읽어 보세요. ‘차이’에는 무엇이 달라졌는지 한국어로 적었습니다. 실제 시스템을 설명하기 위해 가정한 시각이나 서버 이름은 사례 안에서 따로 밝혔습니다.

## How the examples were made

On 2026-11-08 we ran separate baseline and standard sessions for each method with Codex CLI 0.167.0, requesting `gpt-6.1-sol` at low reasoning effort. Each answer came from a fresh ephemeral process in its own randomly named temporary directory outside the checkout. Both arms received the same task and its factual inputs. Only the treatment received the skill entrypoint, method and locale rules at `standard`. The shell and plugins were disabled; no tool calls were recorded. The model build behind the requested name was not reported.

We set checks before each pair, then compared the answers against the primary sources with the conditions visible. There are 44 final answers and 8 earlier answers. The Raft example was rerun with named candidates. The HTTP example was rerun after a correction to requirement strength and again after clarifying the timer in the input. The IMRaD example was rerun after correcting how the method describes the roles of researchers and instruments. The Social Security example was rerun against the edition served by the official link. The HTML answers were also rendered in Chromium 156.0.8078.80: at one-way delays of 3, 12 and 22 minutes the controls showed round trips of 6, 24 and 44 minutes. Both pages kept the initial 24-minute result with JavaScript disabled.

The original synthetic prompts, full outputs and earlier revisions remain in the [previous gallery](https://github.com/hobin01/writing-styles-from-giants/blob/dbcb48c0475647d5377eae635b1fbd6f9f40f426/EXAMPLES.md). These examples show what happened on one task per skill; no reader study or general quality ranking was performed.

Edit a method’s `examples/standard.md` and run `python3 scripts/build_example_gallery.py` to update this file.

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

**What Minneapolis’s I-35W collapse changes about a bridge review**

2026-11-08 · `amazon-six-page-narrative` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [NTSB, investigation HWY07MH024, Collapse of I-35W Highway Bridge, Minneapolis, Minnesota](https://www.ntsb.gov/investigations/Pages/HWY07MH024.aspx). What Happened and What We Found: 1 August 2007 collapse, inadequate U10 gusset plate capacity, combined loads, and omission of gusset plates from load-rating analyses. The proposed review by another owner is an exercise.

### Prompt

> Write the opening of a decision memo for a hypothetical public bridge owner reviewing its steel truss bridges after Minneapolis's I-35W bridge collapsed in 2007. Should the owner fund a review of gusset plates in the load ratings or rely on its existing inspection records alone? According to the NTSB, undersized connecting plates at the U10 joints failed under combined loads: earlier modifications had made the bridge heavier, and traffic and concentrated construction loads were present on the day of collapse. Excluding gusset plates from load-rating analyses was a contributing practice. We have no calculations for the hypothetical owner's bridges in this exercise. State what the proposed review would establish; don't declare the owner's bridges safe or unsafe. At most 110 words.

### Without a skill

> The owner should fund a gusset-plate review as part of its steel truss bridge load ratings; existing inspection records alone cannot establish capacity under combined loads. According to the NTSB, undersized U10 connecting plates failed in the 2007 I-35W collapse under loads from earlier modifications, traffic, and concentrated construction activity. Excluding gusset plates from load-rating analyses contributed to the failure. The proposed review would establish whether plate capacities adequately support applicable load combinations, accounting for modifications and construction loading, and identify any needed restrictions, further analysis, or strengthening. Without bridge-specific calculations, this memo makes no finding that the owner’s bridges are safe or unsafe.

### With the skill at standard

> I recommend funding a review of gusset plates in our steel truss bridge load ratings rather than relying on inspection records alone. According to the NTSB, undersized connecting plates at I-35W’s U10 joints failed under combined loads: earlier modifications had increased bridge weight, and traffic and concentrated construction loads were present that day. Excluding gusset plates from load-rating analyses contributed to the collapse. The proposed review would establish whether our ratings account for gusset-plate capacity under applicable combined loads and identify any needed analysis or action. We have no calculations for our bridges in this exercise and cannot conclude whether they are safe or unsafe.

### What changed

**Checks set before the run.** Recommend a specific review and distinguish capacity calculations from records of visible condition. Retain the joint and combined loads identified by the NTSB, and keep the hypothetical owner's bridge capacities unresolved.

Both recommend reviewing gusset plates and leave the hypothetical owner's bridge capacities open. The baseline lists possible follow-up decisions, including restrictions or strengthening. The skill answer spells out why the old bridge carried more weight and makes reviewing the owner's load ratings the immediate decision. Neither treats the Minneapolis finding as a diagnosis of another bridge.

**차이.** 두 답 모두 교량 연결판의 하중 평가를 권하고, 다른 교량의 안전 여부는 판단할 수 없다고 밝힙니다. 스킬 답안은 과거 개조로 교량 자체의 무게가 늘었다는 점을 분명하게 짚습니다.

## answer-with-html

**Why Perseverance cannot answer Earth immediately**

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

## aristotle-syllogism

**Does a new moon guarantee a total solar eclipse?**

2026-11-08 · `aristotle-syllogism` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [NASA, Why Do Eclipses Happen?](https://science.nasa.gov/eclipses/geometry/). Geometry, total and annular sections: solar eclipses occur at new moon; totality requires complete coverage, whereas an annular eclipse leaves a ring.
- [NASA, 2023 Annular Eclipse FAQ](https://science.nasa.gov/eclipses/future-eclipses/eclipse-2023/faq/). Eclipse science and the October 14, 2023 path of annularity identify the dated counterexample.

### Prompt

> Assess this planetarium visitor's argument in under 85 words: Every total solar eclipse on Earth occurs at new moon. On 14 October 2023 there was a new moon. Therefore there was a total solar eclipse on Earth that day. For the factual check, NASA identifies that day's eclipse as annular: even along the central path a ring of the Sun remained visible. Tell the visitor whether the inference follows and whether the actual event supplies a counterexample.

### Without a skill

> The inference does not follow: it affirms the consequent. Every total solar eclipse occurs at new moon, but not every new moon brings a total solar eclipse. NASA identifies the 14 October 2023 eclipse as annular: even along the central path, a ring of the Sun remained visible. Thus, that day is a counterexample to the converse claim that every new moon brings a total solar eclipse, not to the original claim that every total solar eclipse occurs at new moon.

### With the skill at standard

> The inference does not follow. The premises say every total solar eclipse on Earth occurs at new moon and that 14 October 2023 had a new moon. They do not say every new moon brings a total solar eclipse; that would be an extra premise. No existence follows from the universal premise alone.
>
> Factually, NASA identifies that day’s eclipse as annular: a ring remained visible even along the central path. Thus the actual event supplies a counterexample: both premises hold, but the conclusion fails.

### What changed

**Checks set before the run.** Keep both premises true while showing the conclusion was false on that date. Distinguish the direction of implication from the independent annular observation. Do not describe that eclipse as absent everywhere, or confuse the ring seen along the central path with totality.

Both keep the true premise and use the ring visible on 14 October 2023 to refute the converse. The baseline names the fallacy; the skill separates the inference from the dated observation. Its extra point about existence is logically correct, but the question already supplies a particular new moon.

**차이.** 두 답 모두 금환일식 때 태양의 고리가 남았다는 사실을 반례로 씁니다. 미적용 답은 오류의 이름을, 적용 답은 빠진 전제를 짚습니다.

## asd-ste100

**When to remove a Raspberry Pi 4 recovery card**

2026-11-08 · `asd-ste100` 0.1.3 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Raspberry Pi, Raspberry Pi computer hardware documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#reflash-the-bootloader). Reflash the bootloader, especially the last step for an HDMI-connected board. The prompt covers only completion of a prepared recovery on the Pi 4 Model B.

### Prompt

> Edit the following service note into a concise instruction for a Raspberry Pi 4 Model B technician with an HDMI display attached. The recovery microSD card has already been prepared and inserted for a bootloader reflash. Before disconnecting power, wait for both indications: a steady flashing pattern from the green activity LED and a green screen on the HDMI display. After the power is disconnected, remove the recovery microSD card. Give only these finishing steps. Use 'recovery microSD card' consistently.

### Without a skill

> 1. Wait for both a steady flashing pattern from the green activity LED and a green screen on the HDMI display.
> 2. Disconnect power.
> 3. Remove the recovery microSD card.

### With the skill at standard

> 1. Wait until both the green activity LED flashes in a steady pattern and the HDMI display shows a green screen.
> 2. Disconnect power.
> 3. Remove the recovery microSD card.

### What changed

**Checks set before the run.** Keep both independent visual completion conditions, then disconnect power, then remove the recovery microSD card. A continuously lit LED, one flash alone or an error screen is insufficient. Do not add a new formatting step or extend these instructions to every Pi model.

Both give the same three finishing steps. Each requires the flashing activity LED and the green HDMI screen before power is disconnected; each removes the recovery microSD card only afterward. The baseline already meets the procedure checks.

**차이.** 두 답 모두 초록색 LED의 점멸과 초록색 HDMI 화면을 함께 확인한 뒤 전원을 끊고 복구용 microSD 카드를 빼라고 안내합니다. 이 절차에서는 적용 전후 차이가 작습니다.

## boring-professor

**Why deleting a Linux log file may not free disk space**

2026-11-08 · `boring-professor` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Linux man-pages 6.19, unlink(2)](https://man7.org/linux/man-pages/man2/unlink.2.html). DESCRIPTION defines the effect of unlinking the last directory link with and without an open descriptor. The log filename and running service are an illustrative Linux scenario.

### Prompt

> Explain the following Linux incident drill for a systems engineer in at most 100 words. An administrator successfully unlinks /var/log/payments.log while a payment service still has it open for writing. Assume this was the file's last hard link and the service holds the only open descriptor. The directory no longer lists the pathname, yet the disk space is still in use. What survived unlink, can the service still write, and what event allows that storage to be reused? The pathname and service describe a drill, not a reported outage.

### Without a skill

> Unlink removes the directory entry for `/var/log/payments.log`, but the inode and its allocated data blocks survive because the service’s open file descriptor still references the file through an open file description. The service can continue writing to it, even though the pathname no longer exists.
>
> When the service closes that last descriptor—or exits, causing it to close—the final open reference disappears. With no hard links or open references remaining, the filesystem can reclaim the inode and data blocks, making the storage available for reuse.

### With the skill at standard

> `unlink` removes the directory entry associating `/var/log/payments.log` with its inode, the filesystem object recording metadata and references to file data. Because this was the last hard link, the inode’s link count becomes zero. The open file description, referenced by the service’s descriptor, still retains the inode and its allocated storage.
>
> The service can continue writing through that descriptor, assuming writes otherwise succeed. When the service closes its only descriptor, explicitly or on process exit, the final open reference is released. The filesystem can then reclaim the unlinked file’s inode and data blocks for reuse.

### What changed

**Checks set before the run.** Distinguish directory entry from open file and file descriptor. Explain continued writes and the last-close condition under the last-hard-link assumption. Do not imply instantaneous recovery of physical bytes or invent an outage.

Both explain why the pathname disappears while the service can still write, and why the space can be reused only after the last open descriptor closes in this drill. The skill answer explicitly identifies the zero link count and defines the inode. The baseline reaches the same conclusion in fewer words.

**차이.** 두 답 모두 로그 이름을 지워도 서비스는 열어 둔 파일에 계속 쓸 수 있고, 마지막 파일 디스크립터가 닫혀야 그 공간을 재사용할 수 있다고 설명합니다. 스킬 답은 이때 하드 링크 수가 0이라는 점과 inode의 역할을 덧붙였습니다.

## diataxis

**Watching a specific Kubernetes Deployment revision**

2026-11-08 · `diataxis` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/). Synopsis and flags document default revision tracking, --revision and --watch. checkout-api and revisions 7/8 are an illustrative release, not historical cluster telemetry.

### Prompt

> Write a compact lookup entry for a Kubernetes release engineer who uses kubectl rollout status. An illustrative Deployment named checkout-api is rolling out revision 7; revision 8 might start before 7 finishes. Without --revision, the command watches the latest rollout and follows a newer revision if one starts. With --revision=7, it monitors that particular revision and aborts if it is superseded. With --watch=false, it returns the current status without waiting. Supply the exact command to watch revision 7 and the two flag meanings. Do not claim either rollout actually succeeded.

### Without a skill

> `kubectl rollout status deployment/checkout-api --revision=7`
>
> - `--revision=7`: Watch revision 7; abort if a newer revision supersedes it. Without this flag, the command watches the latest rollout and follows newer revisions.
> - `--watch=false`: Return the current status immediately, without waiting for the rollout to finish.

### With the skill at standard

> Watch revision 7 of `checkout-api`:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> | Flag | Meaning |
> | --- | --- |
> | `--revision=7` | Monitors revision 7 and aborts if it is superseded, such as when revision 8 starts. Without `--revision`, the command watches the latest rollout and follows a newer revision if one starts. |
> | `--watch=false` | Returns the current status without waiting. |
>
> This example does not establish that either rollout succeeded.

### What changed

**Checks set before the run.** Use kubectl rollout status deployment/checkout-api --revision=7 (or equivalent); distinguish monitoring from starting or rolling back the Deployment, pinning from following the latest, and one-time status from waiting. The revision numbers are example inputs.

Both give a correct command for revision 7 and explain when --watch=false returns. The baseline is a short lookup list. The skill uses a table and names the concrete failure condition: revision 8 superseding revision 7. Neither reports a successful deployment.

**차이.** 두 답 모두 revision 7을 지정하는 명령과 기다리지 않고 상태만 읽는 옵션을 정확히 제시합니다. 스킬 답은 revision 8이 시작되면 revision 7을 지켜보던 명령이 중단된다는 상황을 표에서 보여 줍니다.

## eli5

**Why rescued sea otter pup 696 needed grooming**

2026-11-08 · `eli5` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Monterey Bay Aquarium, Life of a rescued sea otter](https://www.montereybayaquarium.org/about-us/stories/life-of-a-rescued-sea-otter). Pup 696's rescue and grooming sections describe the role of air in the fur in warmth and buoyancy.
- [Monterey Bay Aquarium, Sea otter](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/sea-otter). Species account, Adaptations and Grooming: unlike many marine mammals, a sea otter relies on fur in cold water and lacks a thick layer of blubber.

### Prompt

> A five-year-old at Monterey Bay Aquarium asks why caregivers groomed rescued sea otter pup 696. Answer in three or four sentences for the child. A sea otter lacks a thick blubber layer, and grooming fluffs its fur so little bubbles of air are trapped in it. That air helps keep the pup warm and helps it float. Explain what the child would see a caregiver doing and how that helps the pup in cold water.

### Without a skill

> You’d see a caregiver gently rubbing and brushing pup 696’s fur to make it fluffy. Sea otters don’t have a thick layer of fat called blubber to keep them warm. Fluffing the fur traps tiny bubbles of air that help keep the pup warm in cold water and help it float.

### With the skill at standard

> You might see a caregiver rubbing and brushing sea otter pup 696’s fur to make it fluffy. Fluffy fur traps tiny bubbles of air. That air helps keep the pup warm in cold water and helps it float. Sea otters don’t have a thick layer of fat called blubber to keep them warm, so their fur is very important.

### What changed

**Checks set before the run.** Connect a visible grooming action to fluffed fur, trapped air, warmth and flotation. Keep the explanation appropriate for a five-year-old and avoid implying that air bubbles generate heat or that the animal breathes through fur.

Both show the caregiver fluffing the fur so that it traps air, and connect the trapped air to warmth and flotation. The skill gives the trapped bubbles their own sentence; the baseline covers the same mechanism in three sentences. Neither answer measures whether a five-year-old understood it.

**차이.** 두 답 모두 털 손질로 공기가 갇히고, 그 공기가 새끼 해달의 체온 유지와 부력에 도움이 된다고 설명합니다. 적용 답은 공기 방울이 갇히는 단계를 한 문장으로 따로 보여 줍니다.

## federal-plain-language

**Which documents identify a child to Social Security?**

2026-11-08 · `federal-plain-language` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [SSA, U.S. Citizen/Child — Replacement Social Security Card (October 2026)](https://www.ssa.gov/pubs/EN-05-10514.pdf). English page of the October 2026 U.S. citizen/child replacement-card leaflet, sections on the child's and parent's identity, current originals, issuer-certified copies and unacceptable copies. The family’s two documents are an illustrative scenario.

### Prompt

> Write an answer for a parent reading the October 2026 U.S. Social Security Administration leaflet about replacing a U.S.-citizen child's Social Security card. The parent has only the child's birth certificate and a notarized photocopy of the parent's identification. Explain whether those establish identity and what forms of evidence the leaflet accepts. It requires evidence of both people's identities. A birth certificate can establish age or citizenship but not the child's identity; a child's U.S. passport is an example of identity evidence. A parent's U.S. driver's license is another example for the parent. Documents must be current originals or copies certified by the issuer; ordinary photocopies and notarized copies aren't accepted. Limit the answer to the evidence question, in 85 words or fewer.

### Without a skill

> No. The birth certificate can establish your child’s age or U.S. citizenship, but it does not establish the child’s identity. The notarized photocopy of your identification is not accepted.
>
> The leaflet requires identity evidence for both you and your child. Examples include your child’s U.S. passport and your U.S. driver’s license. Documents must be current originals or copies certified by the issuing agency. Ordinary photocopies and notarized copies are not accepted.

### With the skill at standard

> No. The child’s birth certificate can establish age or citizenship, but it does not establish the child’s identity. The notarized photocopy of your identification is not accepted.
>
> The leaflet requires evidence of both your child’s identity and your identity. Examples include a U.S. passport for your child and a U.S. driver’s license for you.
>
> Documents must be current originals or copies certified by the issuer. Ordinary photocopies and notarized copies are not accepted.

### What changed

**Checks set before the run.** Keep the October 2026 leaflet as the source, distinguish the child's identity from age or citizenship, require evidence for both people and distinguish issuer-certified copies from merely notarized copies. Do not imply the examples are the only acceptable documents.

Both answers reject the two documents for the identity check, distinguish the child's identity from age or citizenship, and give an acceptable example for each person. The skill gives the document-format rule its own paragraph. This is a difference in layout; the underlying evidence rule is the same.

**차이.** 두 답 모두 부모와 자녀에게 어떤 신원 증빙이 필요한지 정확히 설명합니다. 스킬 답은 원본·발급기관 인증 사본 요건을 별도 문단으로 나눴고, 인정되는 서류에 관한 결론은 같습니다.

<details>
<summary>Earlier attempts on this case</summary>

The first prompt named a July 2024 leaflet. The current SSA publication identifies itself as the October 2026 edition and says the July 2024 edition may still be used. We dated the question to the edition that the source link actually serves and ran a new matched pair.

**Attempt 1 — request**

> Write an answer for a parent reading the July 2024 U.S. Social Security Administration leaflet about replacing a U.S.-citizen child's Social Security card. The parent has only the child's birth certificate and a notarized photocopy of the parent's identification. Explain whether those establish identity and what forms of evidence the leaflet accepts. It requires evidence of both people's identities. A birth certificate can establish age or citizenship but not the child's identity; a child's U.S. passport is an example of identity evidence. A parent's U.S. driver's license is another example for the parent. Documents must be current originals or copies certified by the issuer; ordinary photocopies and notarized copies aren't accepted. Limit the answer to the evidence question, in 85 words or fewer.

**Without a skill**

> No. The birth certificate can establish your child’s age or U.S. citizenship, but it does not establish identity. Your notarized identification photocopy is also unacceptable.
>
> The leaflet requires evidence of both your child’s identity and your identity. Examples include a U.S. passport for your child and a U.S. driver’s license for you. Documents must be current originals or copies certified by the issuing agency. Ordinary photocopies and notarized copies are not accepted.

**With the skill at standard**

> No. Those documents do not establish both identities, as the leaflet requires. Your child’s birth certificate can establish age or citizenship, but it does not establish identity. The notarized photocopy of your identification is not accepted.
>
> Examples of accepted identity evidence include your child’s U.S. passport and your U.S. driver’s license. Documents must be current originals or copies certified by the agency that issued them. Ordinary photocopies and notarized copies are not accepted.

</details>

## feynman-technique

**Why a new DNS name can still return NXDOMAIN**

2026-11-08 · `feynman-technique` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [IETF RFC 2308, Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html#section-5). Sections 3 and 5 explain the SOA-based lifetime and expiry of negative responses. The hostname, TTL values and clock times are a worked trace, not production DNS records.

### Prompt

> Explain this DNS rollout to a developer in one short paragraph. In this worked example a recursive resolver looks up uploads.example.org at 12:00:00, receives NXDOMAIN (the name does not exist), and caches it. In the zone, the SOA record has a TTL of 900 seconds and a MINIMUM of 300 seconds; RFC 2308 uses the smaller value for the negative cache lifetime. At 12:01:00 the operator creates an A record for that name. What can the same resolver return at 12:02:00, and when does this cached answer expire? Assume no early eviction, refresh or local override; the authoritative server remains reachable. The clock times and record are illustrative.

### Without a skill

> The resolver caches the NXDOMAIN response for 300 seconds—the smaller of the SOA TTL (900 seconds) and MINIMUM (300 seconds). Creating the A record at 12:01:00 does not invalidate that cached response, so at 12:02:00 the same resolver can still return NXDOMAIN. The cached negative answer expires at 12:05:00, after which a new lookup can retrieve the A record from the authoritative server.

### With the skill at standard

> A recursive resolver caches DNS answers, including NXDOMAIN (“the name does not exist”). Here, RFC 2308 sets the negative cache lifetime to the smaller of the SOA TTL (900 seconds) and MINIMUM (300 seconds), so the NXDOMAIN cached at 12:00:00 lasts until 12:05:00. Creating the A record at 12:01:00 does not invalidate that resolver’s cached answer: at 12:02:00 it can still return NXDOMAIN, with 180 seconds remaining. Under the stated assumptions, the cached answer expires at 12:05:00; a subsequent lookup can query the reachable authoritative server and obtain the new A record.

### What changed

**Checks set before the run.** Compute a 300-second lifetime starting at 12:00, not at the record change. A cached NXDOMAIN can persist at 12:02; it expires at 12:05. Expiration permits a fresh lookup rather than proving that all resolvers update simultaneously.

Both answers start the 300-second lifetime when the resolver receives NXDOMAIN, retain the 12:02 negative response and calculate the 12:05 expiry. The skill answer also gives the 180 seconds left at 12:02. Both describe a later lookup rather than promising that all resolvers change together.

**차이.** 두 답 모두 12시 1분에 레코드를 추가해도 12시 2분에는 이전 NXDOMAIN을 돌려줄 수 있고, 캐시는 12시 5분에 만료된다고 설명합니다. 스킬 답은 12시 2분에 남은 시간이 180초라는 계산까지 보여 줍니다.

## google-design-doc

**Adding a PostgreSQL index while orders are still arriving**

2026-11-08 · `google-design-doc` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [PostgreSQL 17 documentation, CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY). Building Indexes Concurrently explains locking, table scans, waiting for transactions and invalid indexes after failure. The store, schema and decision are illustrative; no production benchmark is quoted.
- [PostgreSQL 17 system catalogs, pg_index](https://www.postgresql.org/docs/17/catalog-pg-index.html). The indisvalid field confirms the baseline’s suggested validity check. This catalog reference was checked after the runs.

### Prompt

> Write a design-review excerpt of at most 130 words for an illustrative online store on PostgreSQL 17. Its unpartitioned orders table keeps receiving INSERTs; the requirement is that an index build must not block those writes for the duration of the build. Compare ordinary CREATE INDEX on customer_id with CREATE INDEX CONCURRENTLY. The ordinary build blocks table writes; the concurrent build permits them but scans the table twice and waits for relevant transactions. Failure can leave an invalid index that queries ignore but writes still maintain. Recommend one path and name a rollout check. The store has measured neither build time nor order-write latency.

### Without a skill

> For this illustrative store on PostgreSQL 17, ordinary `CREATE INDEX ON orders (customer_id)` blocks table writes during the build, violating the requirement to keep accepting order INSERTs.
>
> Recommend `CREATE INDEX CONCURRENTLY ON orders (customer_id)`. It permits writes during construction, but scans the table twice and waits for relevant transactions. It can still increase resource use and affect write latency; the store has measured neither build time nor order-write latency, so neither should be promised.
>
> A failed concurrent build can leave an invalid index that queries ignore but writes still maintain. As a rollout check, verify `pg_index.indisvalid` before declaring success, and monitor order-write latency during the build.

### With the skill at standard

> Proposal for review: use `CREATE INDEX CONCURRENTLY` on `orders(customer_id)` in PostgreSQL 17. The requirement is to keep accepting INSERTs throughout the build.
>
> Ordinary `CREATE INDEX` blocks table writes for the build’s duration, so it fails this requirement. The concurrent build permits INSERTs but scans the table twice and waits for relevant transactions. An incoming order can therefore be inserted while the index builds, although its write latency has not been measured.
>
> If the concurrent build fails, it can leave an invalid index: queries ignore it, but writes still maintain it. Before rollout completion, verify index validity and investigate any invalid index.
>
> Approval remains pending. The store has measured neither build time nor order-write latency; measure both during a representative trial to assess rollout impact.

### What changed

**Checks set before the run.** Tie the recommendation to the write-availability requirement; explain scans/waits and invalid-index maintenance. Include an operational check without claiming zero overhead, no locks of any kind, or measured latency for this store.

Both recommend a concurrent build, explain its extra scans and waits, and keep latency unmeasured. The baseline gives the most actionable validity check, pg_index.indisvalid. The skill answer walks one incoming order through the design and proposes a representative trial. Its statement that approval is pending is plausible in a review draft, but the hypothetical store supplied no approval record.

**차이.** 두 답 모두 쓰기를 허용하는 동시 인덱스 생성을 권합니다. 미적용 답은 확인할 열인 pg_index.indisvalid까지 지정하고, 스킬 답은 주문 한 건이 들어올 때의 동작과 측정할 항목을 짚습니다. 실제 승인 상태는 예제에 주어지지 않았습니다.

## gtm-formal

**Proving at most one Raft leader per term in five-member etcd**

2026-11-08 · `gtm-formal` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm, §5.2](https://raft.github.io/raft.pdf). Section 5.2 and Figure 3 distinguish election safety, one vote per term, majority election and split votes.
- [etcd v3.5 FAQ, fault tolerance](https://etcd.io/docs/v3.5/faq/#what-is-failure-tolerance). The fault-tolerance table gives a quorum of three for five etcd members. The split vote is an illustrative configuration.

### Prompt

> For a distributed systems seminar, prove in at most 130 words why two candidates cannot both be elected leader in the same Raft term in a fixed five-voter etcd cluster. Use the illustrative member names etcd-east and etcd-west throughout the proof for the two candidates. Assume a candidate needs at least three distinct votes and each voter grants at most one vote per term. Show the intersection bound for the two voter sets and connect it to the vote rule. Finally explain whether this proof guarantees that a 2–2 split with the fifth voter unreachable elects anyone in that term. This is a worked configuration, not a claim about a live cluster.

### Without a skill

> Suppose etcd-east and etcd-west are both elected in the same term. Let $E$ and $W$ be their respective voter sets. Each requires at least three distinct votes among the five fixed voters, so
>
> $$
> |E\cap W|=|E|+|W|-|E\cup W|\ge 3+3-5=1.
> $$
>
> Thus at least one voter must have voted for both etcd-east and etcd-west in that term, contradicting the rule that each voter grants at most one vote per term. Therefore, both cannot be elected in the same term.
>
> This proves uniqueness, not that an election succeeds. In a 2–2 split between etcd-east and etcd-west with the fifth voter unreachable, neither has the required three votes; if that split persists, neither is elected in that term.

<details>
<summary>Original model text (math delimiters as returned)</summary>

````text
Suppose etcd-east and etcd-west are both elected in the same term. Let \(E\) and \(W\) be their respective voter sets. Each requires at least three distinct votes among the five fixed voters, so
\[
|E\cap W|=|E|+|W|-|E\cup W|\ge 3+3-5=1.
\]
Thus at least one voter must have voted for both etcd-east and etcd-west in that term, contradicting the rule that each voter grants at most one vote per term. Therefore, both cannot be elected in the same term.

This proves uniqueness, not that an election succeeds. In a 2–2 split between etcd-east and etcd-west with the fifth voter unreachable, neither has the required three votes; if that split persists, neither is elected in that term.
````

</details>

### With the skill at standard

> Let $V$ be the fixed voter set, with $|V|=5$, and fix a term $t$. Each voter grants at most one vote in $t$; election requires at least three distinct votes.
>
> Suppose etcd-east and etcd-west are both elected in $t$. Let $E,W\subseteq V$ be their respective voter sets. Then $|E|,|W|\ge3$, so
>
> $$
> |E\cap W|
> =|E|+|W|-|E\cup W|
> \ge3+3-5=1.
> $$
>
> Thus some voter voted for both etcd-east and etcd-west in $t$, contradicting the vote rule. Hence they cannot both be elected in that term.
>
> This proves uniqueness, not guaranteed election. In a 2–2 split between etcd-east and etcd-west, with the fifth voter unreachable, neither has three votes; neither is elected while that split persists.

<details>
<summary>Original model text (math delimiters as returned)</summary>

````text
Let \(V\) be the fixed voter set, with \(|V|=5\), and fix a term \(t\). Each voter grants at most one vote in \(t\); election requires at least three distinct votes.

Suppose etcd-east and etcd-west are both elected in \(t\). Let \(E,W\subseteq V\) be their respective voter sets. Then \(|E|,|W|\ge3\), so
\[
|E\cap W|
=|E|+|W|-|E\cup W|
\ge3+3-5=1.
\]
Thus some voter voted for both etcd-east and etcd-west in \(t\), contradicting the vote rule. Hence they cannot both be elected in that term.

This proves uniqueness, not guaranteed election. In a 2–2 split between etcd-east and etcd-west, with the fifth voter unreachable, neither has three votes; neither is elected while that split persists.
````

</details>

### What changed

**Checks set before the run.** Identify the two vote sets with their named candidates. Prove that two voter sets of at least 3 in a 5-voter universe overlap in at least 1 voter, contradicting one vote per term for distinct candidates. Distinguish election safety from progress: in the stated split neither has a majority; other terms or changing memberships are outside scope.

Both answers identify the candidates as etcd-east and etcd-west, define their vote sets and show why two sets of three among five share at least one voter. Both distinguish a unique possible leader from a guaranteed election in a 2–2 split. The skill starts by explicitly fixing the voter universe and term; the baseline begins directly with the two supposed winners. The earlier symbolic pair is retained below.

**차이.** 두 답 모두 etcd-east와 etcd-west가 각각 3표를 받았다면 5명 중 적어도 한 명이 두 후보에게 투표했다는 모순을 보입니다. 2대 2로 갈리면 승자가 없어도 된다는 점도 같습니다. 스킬 답은 증명 첫 줄에서 투표자 집합과 임기를 먼저 고정합니다.

<details>
<summary>Earlier attempts on this case</summary>

The first pair defined its voters correctly, but still referred to abstract candidates. We named the two example etcd members in the final prompt and reran both arms.

**Attempt 1 — request**

> For a distributed systems seminar, prove in at most 130 words why two candidates cannot both be elected leader in the same Raft term in a fixed five-voter etcd cluster. Assume a candidate needs at least three distinct votes and each voter grants at most one vote per term. Show the intersection bound for the two voter sets and connect it to the vote rule. Finally explain whether this proof guarantees that a 2–2 split with the fifth voter unreachable elects anyone in that term. This is a worked configuration, not a claim about a live cluster.

**Without a skill**

````text
Suppose distinct candidates \(A\) and \(B\) are both elected in term \(t\). Let \(V_A\) and \(V_B\) be their voter sets. Each contains at least three distinct voters from the fixed five-voter cluster, so
\[
|V_A\cap V_B|
=|V_A|+|V_B|-|V_A\cup V_B|
\ge 3+3-5=1.
\]
Thus at least one voter voted for both candidates in term \(t\), contradicting the rule that each voter grants at most one vote per term. Therefore, two candidates cannot both be elected leader in the same term.

This proves uniqueness, not election progress. In a 2–2 split with the fifth voter unreachable, neither candidate has the required three votes. No candidate is elected while that split persists; the proof does not guarantee an election in that term.
````

**With the skill at standard**

````text
Let \(V\) be the fixed set of five voters, and fix a term \(t\). Suppose distinct candidates \(A\) and \(B\) are both elected in \(t\). Let \(S_A,S_B\subseteq V\) be their respective voter sets. By assumption, \(|S_A|,|S_B|\ge3\). Hence
\[
|S_A\cap S_B|
=|S_A|+|S_B|-|S_A\cup S_B|
\ge3+3-5=1.
\]
Thus some voter granted votes to both distinct candidates in term \(t\), contradicting the rule that each voter grants at most one vote per term. Therefore at most one candidate can be elected in any given term.

This proves uniqueness, not guaranteed election. In a 2–2 split with the fifth voter unreachable, neither candidate has the required three votes; if that split persists, no leader is elected in that term.
````

</details>

## hunminjeongeum

**Finding a transfer on Seoul’s redesigned subway map**

2026-11-08 · `hunminjeongeum` 0.1.1 · Korean · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [서울특별시, 시민의 발, 디자인을 입다…서울시, 지하철 노선도 40년 만에 변경 (2023-09-13)](https://news.seoul.go.kr/culture/archives/520933). Design release on interchange markings, the circular Line 2 reference, and maximum time reduction in the 20s–30s domestic/foreign eye-tracking experiment.

### Prompt

> 서울을 처음 방문한 승객에게 서울시가 2023년 9월 지하철 노선도 개선안을 내놓은 이유를 한국어 세 문장으로 설명해 주세요. 기존 지도에서는 환승역이 일반역과 잘 구분되지 않았어요. 개선안은 환승할 수 있는 노선의 색을 한 표시에 연결해 놓았고, 원형으로 그린 2호선을 지도의 기준점으로 삼았어요. 서울시가 20~30대 내국인·외국인을 대상으로 진행한 시선 추적 실험에서는 환승역 길을 찾는 데 걸린 시간이 최대 약 69% 줄었어요. 이 수치가 무엇을 측정했는지도 알려 주세요.

### Without a skill

> 서울시가 2023년 9월 지하철 노선도 개선안을 내놓은 이유는 기존 지도에서 환승역과 일반역을 구분하기 어려워 서울을 처음 방문한 승객도 환승 경로를 쉽게 찾도록 돕기 위해서예요. 개선안은 환승 가능한 노선들의 색을 하나의 표시에 연결하고, 원형으로 그린 2호선을 지도의 기준점으로 삼았어요. 서울시가 20~30대 내국인과 외국인을 대상으로 진행한 시선 추적 실험에서 최대 약 69% 줄어든 것은 지도에서 환승역 길을 찾는 데 걸린 시간이며, 실제 지하철 이동 시간은 아니에요.

### With the skill at standard

> 서울을 처음 방문한 승객은 기존 지하철 노선도에서 환승역과 일반역을 구분하기 어려웠기 때문에, 서울시는 환승역과 이동 경로를 더 쉽게 찾도록 2023년 9월 노선도 개선안을 내놓았어요.
> 개선안은 환승할 수 있는 노선의 색을 하나의 표시에 연결해 보여 주고, 원형으로 그린 2호선을 지도의 기준점으로 삼아 위치를 파악하도록 했어요.
> 서울시가 20~30대 내국인·외국인을 대상으로 진행한 시선 추적 실험에서는 환승역 길을 찾는 데 걸린 시간이 최대 약 69% 줄었는데, 이는 실험에서 노선도를 보고 길을 찾는 데 걸린 시간을 측정한 결과이며 실제 열차 이동 시간의 감소를 뜻하지는 않아요.

### What changed

**Checks set before the run.** Begin with the first-time passenger's transfer difficulty. Connect linked line colours and circular Line 2 to finding the transfer. Keep the eye-tracking task, the participant ages and the 'up to about 69%' bound; do not turn it into a reduction in real journey time.

Both connect the transfer symbol and the circular Line 2 to the passenger's task. The baseline opens with the city announcing a change. The skill answer opens with the passenger struggling to distinguish stations. Both correctly identify the roughly 69% maximum as a map-reading result in the eye-tracking test; the skill's last sentence is longer without adding another finding.

**차이.** 미적용 답안은 서울시가 개선안을 낸 이유로, 스킬 답안은 처음 온 승객이 겪던 불편으로 시작합니다. 둘 다 최대 약 69% 줄어든 것은 열차 이동 시간이 아니라 실험에서 환승역 길을 찾는 데 걸린 시간이라고 설명합니다.

## ietf-rfc

**Specifying HTTP 429 for a rate-limited API**

2026-11-08 · `ietf-rfc` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [IETF RFC 6585 §4, 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4). Sections 4 and 7.2 cover explanation, optional Retry-After, cache prohibition, deliberately unspecified counting and a server’s discretion to omit 429.
- [IETF RFC 9110 §10.2.3, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3). The field accepts an HTTP date or nonnegative integer delay in seconds after response receipt. The 120-second header is an illustration.

### Prompt

> Draft a short internal HTTP API specification (at most 95 words) using BCP 14 keywords. Explain how a client interprets the worked header Retry-After: 120 and whether a subsequent request is guaranteed to succeed. Under RFC 6585 §§4 and 7.2 a server can choose 429 for too many requests in a time interval. If sent, its content should explain the condition and it may include Retry-After. A cache must not store a 429 response. RFC 9110 §10.2.3 permits an HTTP date or a nonnegative delay in seconds measured after receipt of the response. State the keyword convention and distinguish server, client and cache roles. No identity scheme or rate-limiting algorithm is specified.

### Without a skill

> The keywords MUST, MUST NOT, SHOULD, and MAY are interpreted as described in BCP 14 (RFC 2119 and RFC 8174) when capitalized.
>
> A server MAY return 429 for too many requests within a time interval. Its content SHOULD explain the condition; it MAY include Retry-After.
>
> Retry-After accepts an HTTP date or nonnegative delay in seconds. For `Retry-After: 120`, the client SHOULD wait at least 120 seconds after receiving the response before retrying. Success is not guaranteed.
>
> A cache MUST NOT store a 429 response.
>
> No identity scheme or rate-limiting algorithm is specified.

### With the skill at standard

> Internal draft: HTTP rate limiting
>
> Uppercase keywords use BCP 14 meanings (RFC 2119; RFC 8174).
>
> A server MAY send 429 for too many requests within a time interval. Its content SHOULD explain the condition; it MAY include Retry-After. A cache MUST NOT store 429 responses.
>
> Clients interpret `Retry-After: 120` as a suggested 120-second delay after response receipt; subsequent success is not guaranteed. An HTTP date is also permitted.
>
> Security: identity and rate-limiting algorithms remain unspecified.
> IANA: no action.
>
> Normative references: RFC 6585 §§4, 7.2; RFC 9110 §10.2.3.

### What changed

**Checks set before the run.** Keep explanatory details at SHOULD, Retry-After optional (MAY), and cache storage prohibited (MUST NOT). Interpret 120 as seconds after receipt and do not guarantee that the subsequent request succeeds. Do not invent per-user counting rules.

Both final answers keep sending HTTP 429 optional, prohibit cache storage and count 120 seconds from receipt, without promising a successful retry. The baseline makes waiting a client SHOULD under BCP 14. The skill describes the suggested wait without adding that normative client requirement. The first treatment had incorrectly made sending 429 mandatory.

**차이.** 두 최종 답 모두 서버의 429 전송은 선택 사항이고 캐시는 응답을 저장하면 안 된다는 점을 지킵니다. 응답 수신 후 120초를 세되 재시도 성공을 보장하지도 않습니다. 미적용 답은 클라이언트 대기에 대문자 SHOULD를 추가했고, 스킬 답은 이를 권장 대기 시간으로 설명했습니다.

<details>
<summary>Earlier attempts on this case</summary>

The first treatment made sending a 429 mandatory. We clarified that choosing to send a message differs from the obligations on its contents. The new treatment preserved that condition but left the timer origin implicit. We then supplied the receipt-time fact in the final prompt and reran both arms.

**Attempt 1 — request**

> Draft an internal HTTP API specification of at most 95 words using BCP 14 keywords. Adopt RFC 6585 section 4: a 429 response reports too many requests in a time interval; its content should explain the condition, it may include Retry-After, and a cache must not store the response. RFC 9110 section 10.2.3 permits either an HTTP date or a nonnegative delay in seconds. For a worked header, use Retry-After: 120. Do not prescribe an identity scheme or rate-limiting algorithm. State the keyword convention and distinguish the server, client and cache roles.

**With the skill at standard**

> # Internal HTTP API Draft
>
> This specification defines rate-limit responses. Uppercase keywords use BCP 14 meanings (RFC 2119; RFC 8174).
>
> The server MUST use 429 to report too many requests in a time interval. Response content SHOULD explain the condition; the server MAY include `Retry-After`.
>
> Clients can interpret `Retry-After` as an HTTP date or nonnegative delay in seconds.
>
> Example: `Retry-After: 120`
>
> A cache MUST NOT store the response.
>
> Identity schemes and rate-limiting algorithms remain unspecified; abuse resistance remains unresolved.
>
> IANA: no action.
>
> Normative references: RFC 6585 §4; RFC 9110 §10.2.3.

**Attempt 2 — request**

> Draft an internal HTTP API specification of at most 95 words using BCP 14 keywords. Adopt RFC 6585 section 4: a 429 response reports too many requests in a time interval; its content should explain the condition, it may include Retry-After, and a cache must not store the response. RFC 9110 section 10.2.3 permits either an HTTP date or a nonnegative delay in seconds. For a worked header, use Retry-After: 120. Do not prescribe an identity scheme or rate-limiting algorithm. State the keyword convention and distinguish the server, client and cache roles.

**Without a skill**

> The keywords MUST, MUST NOT, SHOULD, and MAY are interpreted as described in BCP 14 when, and only when, they appear in uppercase.
>
> Server: A 429 (Too Many Requests) response indicates too many requests in a time interval. Its content SHOULD explain the condition. The server MAY include Retry-After, using either an HTTP date or a nonnegative delay in seconds.
>
> Worked header:
> ```http
> Retry-After: 120
> ```
>
> Client: The client SHOULD wait for the indicated interval before retrying.
>
> Cache: A cache MUST NOT store a 429 response.

**With the skill at standard**

> Internal draft: HTTP rate-limit responses.
>
> Uppercase keywords use BCP 14 meanings (RFC 2119; RFC 8174).
>
> A server MAY send 429 to report too many client requests within a time interval. Its content SHOULD explain the condition; it MAY include Retry-After. A cache MUST NOT store the response.
>
> Retry-After permits an HTTP date or nonnegative delay in seconds, interpreted by the client. Example:
> ```http
> Retry-After: 120
> ```
>
> Identity schemes and limiting algorithms remain unspecified.
> Security: abuse resistance remains unresolved.
> IANA: no action.
>
> Normative references: RFC 6585 §4; RFC 9110 §10.2.3.

</details>

## imrad

**How LIGO recognized GW150914**

2026-11-08 · `imrad` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [LIGO Scientific Collaboration and Virgo Collaboration, Observation of Gravitational Waves from a Binary Black Hole Merger (2016)](https://dcc.ligo.org/public/0122/P150914/014/LIGO-P150914_Detection_of_GW150914.pdf). Abstract and §V.B, binary coalescence search: event date, two detectors, frequency sweep, peak strain, predicted waveform match and upper bound on the false-alarm rate.

### Prompt

> Write a research abstract of at most 110 words for a museum's science page about GW150914, keeping the measurement and its interpretation distinct. On 14 September 2015 both Advanced LIGO detectors, at Livingston and Hanford, recorded a transient signal. Its frequency rose from 35 to 250 Hz and its peak strain was 1.0 × 10⁻²¹. The signal matched the waveform predicted for two black holes spiraling together, merging and settling into one remnant. The paper estimated a false-alarm rate of less than one event per 203,000 years for its search. Explain what that rate measures.

### Without a skill

> On 14 September 2015, Advanced LIGO’s detectors at Livingston and Hanford recorded a transient signal whose frequency rose from 35 to 250 Hz, with a peak strain of 1.0 × 10⁻²¹. These measurements matched the predicted gravitational-wave signature of two black holes spiraling together, merging and settling into one remnant, supporting that interpretation of GW150914. The paper estimated a search false-alarm rate below one event per 203,000 years: how often detector noise would produce a candidate at least as significant under that search procedure. This rate is not the probability that this particular signal was noise.

### With the skill at standard

> **Introduction:** GW150914 tested whether gravitational-wave observations matched predictions for merging black holes.
>
> **Methods:** On 14 September 2015, the Advanced LIGO detectors at Livingston and Hanford recorded a transient signal.
>
> **Results:** Its frequency rose from 35 to 250 Hz, with a peak strain of 1.0 × 10⁻²¹. The paper estimated a false-alarm rate below one event per 203,000 years: how often noise would produce a candidate at least as significant in that search, not the probability this event was noise.
>
> **Discussion:** The waveform matched predictions for two black holes spiraling together, merging and settling into one remnant, supporting that interpretation.

### What changed

**Checks set before the run.** Keep the event date, both instruments, 35–250 Hz and the dimensionless peak strain. Distinguish the observed waveform from the black-hole-merger interpretation and the search's noise false-alarm rate from the rate of mergers.

Both final answers give the date, sites, frequency sweep, peak strain and the search-specific false-alarm rate. Both distinguish a noise-candidate rate from the probability that GW150914 was noise. The revised skill answer puts the detector reading in Methods and the merger interpretation in Discussion; the baseline makes the same distinction in one paragraph. The first skill answer assigned the waveform comparison to the detectors. After the instruction was clarified, the new answer no longer does so.

**차이.** 두 최종 답 모두 오경보율을 ‘이 신호가 잡음일 확률’과 구분합니다. 첫 적용 답은 검출기가 파형까지 비교한 것처럼 썼습니다. 재실행한 답은 검출기가 기록한 신호와 그 신호를 블랙홀 병합으로 해석한 근거를 따로 보여 줍니다.

<details>
<summary>Earlier attempts on this case</summary>

The first treatment assigned waveform comparison to the detectors. The revised method distinguishes the recording instrument from the analysis. We reran the same request with that change.

**Attempt 1 — request**

> Write a research abstract of at most 110 words for a museum's science page about GW150914, keeping the measurement and its interpretation distinct. On 14 September 2015 both Advanced LIGO detectors, at Livingston and Hanford, recorded a transient signal. Its frequency rose from 35 to 250 Hz and its peak strain was 1.0 × 10⁻²¹. The signal matched the waveform predicted for two black holes spiraling together, merging and settling into one remnant. The paper estimated a false-alarm rate of less than one event per 203,000 years for its search. Explain what that rate measures.

**With the skill at standard**

> **Introduction:** GW150914 tested predictions of gravitational waves from merging black holes.
>
> **Methods:** On 14 September 2015, both Advanced LIGO detectors, at Livingston and Hanford, recorded a transient signal and compared it with predicted waveforms.
>
> **Results:** Its frequency rose from 35 to 250 Hz, with peak strain 1.0 × 10⁻²¹. It matched the predicted waveform of two black holes spiraling together, merging and settling into one remnant. The search’s estimated false-alarm rate was less than one event per 203,000 years: how often noise would produce a candidate at least as significant.
>
> **Discussion:** This agreement supports interpreting GW150914 as gravitational waves from a black-hole merger.

</details>

## korean-plain-language

**How Seoul’s 2024 youth Climate Card refunds differed for physical and mobile cards**

2026-11-08 · `korean-plain-language` 0.1.1 · Korean · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [서울특별시 내 손안에 서울, ‘월 5만원대’ 청년 맞춤형 기후동행카드 나온다 (2024-02-21)](https://mediahub.seoul.go.kr/archives/2010350). City's February 2024 announcement, especially the retrospective refund, separate registration rule and monthly eligibility conditions under the original pilot.

### Prompt

> 2024년 서울 기후동행카드 시범사업을 소개하는 기록용 글이에요. 당시 청년 할인 대상자에게 실물카드와 모바일카드의 차이를 알려 주는 해요체 문구로, 아래 내용을 네 문장 이내로 다듬어 주세요. 실물카드는 티머니 홈페이지에 등록한 이후의 이용분만 환급 대상이었어요. 모바일카드는 환급을 위한 별도 카드 등록이 필요 없었어요. 둘 다 환불 없이 30일권을 끝까지 사용한 달에만 7,000원을 돌려받을 수 있었고, 환급은 자동 지급이 아니라 별도로 신청해야 했어요. 지금 신청할 수 있다는 뜻이 되면 안 돼요.

### Without a skill

> 2024년 서울 기후동행카드 시범사업 당시 청년 할인 대상자의 실물카드는 티머니 홈페이지에 등록한 이후의 이용분만 환급 대상이었어요. 모바일카드는 환급을 위한 별도 카드 등록이 필요 없었어요. 두 카드 모두 환불 없이 30일권을 끝까지 사용한 달에만 7,000원을 돌려받을 수 있었어요. 환급금은 자동으로 지급되지 않았고, 당시 별도로 환급 신청을 해야 했어요.

### With the skill at standard

> 2024년 서울 기후동행카드 시범사업 당시 청년 할인 대상자는 실물카드를 티머니 홈페이지에 등록한 이후의 이용분에 대해서만 환급받을 수 있었어요. 모바일카드는 환급을 위한 별도의 카드 등록이 필요 없었어요. 두 카드 모두 환불 없이 30일권을 끝까지 사용한 달에만 7,000원을 돌려받을 수 있었어요. 환급금은 자동으로 지급되지 않았고, 당시 별도로 환급을 신청해야 했어요.

### What changed

**Checks set before the run.** Keep the 2024 pilot in the past; distinguish mobile registration from the refund application required in both cases. Retain physical-card registration timing, full 30-day use without refund, the 7,000-won amount per qualifying month and 해요체.

Both distinguish registering the physical card from applying for the refund, and both keep the notice in the past. The baseline makes the physical card the topic of its first sentence. The skill answer makes the eligible rider the subject. Both preserve the four-sentence limit, full 30-day use, the monthly 7,000 won and 해요체.

**차이.** 첫 문장의 중심이 미적용 답안에서는 ‘실물카드’, 스킬 답안에서는 ‘청년 할인 대상자’입니다. 두 답 모두 실물카드 등록과 환급 신청을 구분하며, 30일 만기·월 7,000원·과거 시점이라는 조건을 지켰습니다.

## microsoft-writing-style

**Clearing Windows 11 Clipboard history without deleting a pinned entry**

2026-11-08 · `microsoft-writing-style` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Microsoft Support, Using the clipboard](https://support.microsoft.com/en-us/windows/apps/using-the-clipboard). Windows 11 section on clearing clipboard history gives the local shortcut, Clear all control and pinned-item exception. The delivery address describes an illustrative user task.

### Prompt

> Write brief Windows 11 help for a person with Clipboard history enabled on their PC. They pinned a frequently used delivery address and want to clear the other entries. Microsoft documents the Windows logo key + V shortcut to open Clipboard history and Clear all at the top of the panel to clear device history except pinned items. Tell the reader what to select and what will happen to the address. Write only the user-facing instructions, using the actual shortcut and control label; do not make a claim about synced devices.

### Without a skill

> Press **Windows logo key + V** to open Clipboard history, then select **Clear all** at the top of the panel. The other entries will be cleared, and your pinned delivery address will remain.

### With the skill at standard

> Press **Windows logo key + V** to open Clipboard history, then select **Clear all** at the top of the panel. This clears your device’s Clipboard history except pinned items. Your pinned delivery address will remain.

### What changed

**Checks set before the run.** Preserve the shortcut, the literal Clear all label and the pinned-address exception. Keep the answer scoped to this PC; no unrequested account, cloud deletion, or settings steps.

Both give the same Windows shortcut and Clear all label and correctly say the pinned address remains. The skill answer explicitly scopes the cleanup to this device and makes the general exception for pinned items clear. Both are usable here.

**차이.** 두 답 모두 Windows 로고 키 + V에서 Clear all을 누르면 고정한 주소가 남는다고 안내합니다. 스킬 답은 ‘이 장치’와 ‘고정 항목 제외’라는 범위를 한 번 더 명확히 합니다.

## minto-pyramid

**Should a city pilot an earlier WALK signal?**

2026-11-08 · `minto-pyramid` 0.2.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [FHWA, Leading Pedestrian Interval](https://highways.dot.gov/safety/proven-safety-countermeasures/leading-pedestrian-interval). Definition, timing, turning conflicts, visibility, accessibility and applicability at high-turning-volume crossings.
- [FHWA, Safety Evaluation of Protected Left-Turn Phasing and Leading Pedestrian Intervals on Pedestrian Safety (2018), FHWA-HRT-18-044](https://www.fhwa.dot.gov/publications/research/safety/18044/18044.pdf). Executive summary and combined leading-interval evaluation, including the Chicago, New York and Charlotte sites and pedestrian crash modification factor 0.87. The committee decision in the request is hypothetical.

### Prompt

> For a hypothetical city traffic committee, write an opening paragraph recommending whether to pilot a leading pedestrian interval at signalized crossings with many turning vehicles. In this arrangement WALK begins 3–7 seconds before drivers get green, so someone crossing can become visible before drivers turn. A 2018 FHWA evaluation across treated sites in Chicago, New York City and Charlotte estimated about 13% fewer vehicle–pedestrian crashes than expected without the treatment. This committee has not measured outcomes at its own crossings. Give a concrete next step and keep the opening under 90 words.

### Without a skill

> The committee should pilot a leading pedestrian interval at signalized crossings with many turning vehicles, giving pedestrians a 3–7-second head start to become visible before drivers turn. A 2018 FHWA evaluation of treated sites in Chicago, New York City and Charlotte estimated about 13% fewer vehicle–pedestrian crashes than expected without the treatment, though local results remain unmeasured. Next, select pilot crossings and establish baseline crash, turning-conflict and delay measures to compare with outcomes after installation.

### With the skill at standard

> At signalized crossings with many turning vehicles, a leading pedestrian interval starts WALK 3–7 seconds before drivers get green, helping pedestrians become visible before drivers turn. Should the city pilot it? A 2018 FHWA evaluation across treated sites in Chicago, New York City and Charlotte estimated about 13% fewer vehicle–pedestrian crashes than expected without treatment, but local outcomes remain unmeasured. Recommend a pilot at selected crossings, beginning with baseline crash and turning-conflict measurements and a plan to compare outcomes after implementation.

### What changed

**Checks set before the run.** Give the pilot decision, the 3–7-second mechanism, the three-city estimate and its vehicle–pedestrian crash outcome. Distinguish a proposed local check from an already measured local effect.

Both propose a pilot, give the three-city estimate and call for baseline measurements at the new sites. The baseline leads with the recommendation and includes delay among its suggested measures. The skill answer explains the WALK interval, asks the decision question, then gives its recommendation. Both keep the 13% estimate distinct from the local outcome.

**차이.** 두 답 모두 13%를 세 도시의 추정치로 남겨 두고, 새 교차로에서는 별도로 측정하자고 합니다. 미적용 답안은 시범 도입을 먼저 권하고, 스킬 답안은 신호의 원리와 결정할 질문을 제시한 뒤 권고합니다.

## new-harts-rules

**Copyediting a car-access statistic from the 2021 census**

2026-11-08 · `new-harts-rules` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Office for National Statistics, Housing, England and Wales: Census 2021 (5 January 2023)](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/housingenglandandwales/census2021). Section 6, Car or van availability, and title: 42.1% of London households versus 23.3% across England and Wales in 2021. Exhibition style and draft are original exercise inputs.

### Prompt

> Copyedit this original sentence for a UK transport exhibition label, followed by one short editorial note. Our exhibition house style spells out ‘per cent’ in prose. Preserve the ONS bulletin title verbatim. Draft: In ‘Housing, England and Wales: Census 2021’, the Office for National Statistics reported that 42.1% of London households had no car or van available in 2021, compared with 23.3% across England and Wales. No edition-specific passage from New Hart’s Rules has been supplied. Keep the finding at household level.

### Without a skill

> In ‘Housing, England and Wales: Census 2021’, the Office for National Statistics reported that 42.1 per cent of London households had no car or van available in 2021, compared with 23.3 per cent across England and Wales.
>
> Editorial note: ‘Per cent’ follows exhibition house style; the bulletin title and household-level finding are preserved.

### With the skill at standard

> In ‘Housing, England and Wales: Census 2021’, the Office for National Statistics reported that 42.1 per cent of London households had no car or van available in 2021, compared with 23.3 per cent across England and Wales.
>
> Editorial note: ‘Per cent’ follows exhibition house style; the bulletin title and household-level finding are preserved. No rule is attributed to New Hart’s Rules, second edition (2014), because no relevant passage was supplied.

### What changed

**Checks set before the run.** Apply the supplied exhibition convention to both percentages, preserve the exact title, household denominator, year and geographic comparison, and attribute the change to the house rather than to ONS or New Hart's Rules.

The edited sentence is identical in both runs. Each changes the two percent signs to the exhibition's house spelling and preserves the bulletin title and both household percentages. The skill adds a sentence explaining that there was no book passage to consult. It makes the source boundary explicit, but lengthens a note whose practical conclusion is the same.

**차이.** 두 답의 편집 문장은 같습니다. 42.1과 23.3을 해당 지역 가구의 비율로 유지하고 전시의 표기 지침을 따랐습니다. 스킬 답안의 편집 메모만 책의 해당 구절이 제공되지 않았다고 추가로 설명합니다.

## nist-technical-publication

**The uncertainty budget of the NIST-F2 cesium fountain**

2026-11-08 · `nist-technical-publication` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Heavner et al., First Accuracy Evaluation of NIST-F2, Metrologia (2014)](https://www.nist.gov/publications/first-accuracy-evaluation-nist-f2). Authors' abstract, including the July–August 2013 Type A and Type B fractional uncertainties, the 80 K interrogation environment and the reason for the dominant Type B contribution.

### Prompt

> For a metrology lab, summarize the July–August 2013 evaluation of NIST-F2 in at most 85 words. This cesium fountain interrogated atoms in an 80 K environment. Cooling cut the uncertainty from the blackbody-radiation shift by more than a factor of 50. The reported statistical (Type A) fractional frequency uncertainty was 0.44 × 10⁻¹⁵; the systematic (Type B) component was 0.11 × 10⁻¹⁵. Microwave-amplitude effects dominated the Type B component. Explain what the smaller number represents without presenting it as the clock's total uncertainty.

### Without a skill

> During its July–August 2013 evaluation, NIST-F2 interrogated cesium atoms in an 80 K environment, reducing uncertainty from the blackbody-radiation shift by more than a factor of 50. Its statistical (Type A) fractional frequency uncertainty was 0.44 × 10⁻¹⁵. The smaller value, 0.11 × 10⁻¹⁵, represents the systematic (Type B) uncertainty component, dominated by microwave-amplitude effects; it is not the clock’s total uncertainty.

### With the skill at standard

> The July–August 2013 evaluation of the NIST-F2 cesium fountain interrogated atoms in an 80 K environment, reducing uncertainty from the blackbody-radiation shift by more than a factor of 50. The reported statistical (Type A) fractional frequency uncertainty was 0.44 × 10⁻¹⁵. The smaller value, 0.11 × 10⁻¹⁵, represents the systematic (Type B) fractional frequency uncertainty component, dominated by microwave-amplitude effects; it is not the clock’s total uncertainty.

### What changed

**Checks set before the run.** Keep July–August 2013, 80 K and the factor greater than 50 attached only to uncertainty from the blackbody-radiation shift. Preserve each numeric fractional uncertainty with its correct component and keep microwave-amplitude effects tied to Type B; neither component alone is the total.

Both keep the 80 K setting, the time interval and the two numerical components. Both attach the factor above 50 to the blackbody-radiation contribution only. The skill spells out that the smaller component is a fractional frequency uncertainty; the baseline is already sufficient to keep it separate from the clock’s total uncertainty.

**차이.** 두 답 모두 50배 넘게 줄어든 것은 흑체복사에 따른 불확도라고 밝힙니다. 둘 다 0.11 × 10⁻¹⁵를 전체 불확도로 바꾸지 않았습니다.

## orwell-six-rules

**Why the Mars Climate Orbiter’s navigation estimate was wrong**

2026-11-08 · `orwell-six-rules` 0.1.2 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Cornelius J. Dennehy / NASA, Best Practices for the Design, Development, and Operation of Robust and Reliable Space Vehicle Guidance, Navigation, and Control Systems (NASA/TP–20230005922, April 2023)](https://ntrs.nasa.gov/api/citations/20230005922/downloads/20230005922.pdf). Appendix A-12, pp. 138–139, and lesson 0641: ground software/interface units, trajectory about 170 km low, and two possible outcomes after loss.

### Prompt

> Rewrite this draft for readers of a museum exhibit in at most 75 words. Draft: In September 1999, the loss of NASA's Mars Climate Orbiter took place. A ground program called SM_FORCES made provision for thruster impulse figures in pound-force seconds. The navigation team proceeded on the assumption that the figures were in newton-seconds as required by the software interface. The mismatch caused errors in the trajectory estimate to accumulate; the spacecraft arrived about 170 km lower than planned. NASA could not determine whether it was destroyed in the atmosphere or left Mars for an orbit around the Sun.

### Without a skill

> In September 1999, NASA lost the Mars Climate Orbiter after a mix-up in units. A ground program reported thruster impulses in pound-force seconds, but navigators treated them as newton-seconds, as the software interface required. Trajectory errors accumulated, bringing the spacecraft about 170 kilometers lower than planned. NASA could not determine whether it broke apart in Mars’s atmosphere or escaped into orbit around the Sun.

### With the skill at standard

> In September 1999, NASA lost the Mars Climate Orbiter. A ground program, SM_FORCES, supplied thruster impulse figures in pound-force seconds. The navigation team assumed they were in newton-seconds, as the software interface required. This mismatch caused errors to build up in the estimated trajectory. The spacecraft arrived about 170 km lower than planned. NASA could not determine whether it was destroyed in Mars’s atmosphere or left Mars to orbit the Sun.

### What changed

**Checks set before the run.** Cut inflated phrasing while accurately attributing the mismatch to ground data, preserving the two impulse units, the approximate 170 km trajectory error and both possible fates. Avoid inventing a collision or blaming a named individual.

Both replace the inflated wording, preserve the units mismatch and describe the two possible fates. The baseline drops the program name and compresses the navigation estimate into 'trajectory errors'. The skill answer keeps SM_FORCES and distinguishes errors accumulating in an estimate from the spacecraft arriving about 170 km lower than planned.

**차이.** 두 답 모두 단위 착오와 탐사선의 두 가지 가능한 최후를 보존합니다. 스킬 답안은 지상 프로그램 이름 SM_FORCES를 남기고, 먼저 오차가 쌓인 것은 궤도 추정값이었다고 정확히 짚습니다.

## socratic-self-questioning

**Did Finland’s basic income experiment prove a universal employment gain?**

2026-11-08 · `socratic-self-questioning` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [Finnish Ministry of Social Affairs and Health and Kela, Results of the basic income experiment (6 May 2020)](https://valtioneuvosto.fi/en/-/1271139/perustulokokeilun-tulokset-tyollisyysvaikutukset-vahaisia-toimeentulo-ja-psyykkinen-terveys-koettiin-paremmaksi?languageId=en_US). Employment results and experiment design: participating population, €560 payment, November 2017–October 2018 comparison, first-year finding, and asymmetric 2018 activation-policy change.

### Prompt

> Rewrite this claim for a public policy brief in no more than 95 words: ‘Finland proved that paying everyone a basic income creates six extra days of work.’ In its 2017–2018 experiment, 2,000 randomly selected unemployed benefit recipients received €560 a month. In November 2017–October 2018 recipients averaged 78 days employed, six more than the comparison group. The first year showed no group-level employment effect. A 2018 change in unemployment-benefit rules affected the groups differently, so researchers could not separate its effect from the second-year basic-income effect. Give a finished paragraph, not an interview.

### Without a skill

> Finland’s 2017–2018 experiment does not establish that paying everyone a basic income increases employment. It gave 2,000 randomly selected unemployed benefit recipients €560 a month. From November 2017 to October 2018, recipients averaged 78 days employed—six more than the comparison group—but the first year showed no group-level employment effect. A 2018 change in unemployment-benefit rules affected the groups differently, preventing researchers from separating its effect from that of basic income in the second year. The findings therefore cannot establish the employment effects of a universal basic income.

### With the skill at standard

> Finland’s 2017–2018 experiment does not establish that paying everyone a basic income creates six extra days of work. It provided €560 a month to 2,000 randomly selected unemployed benefit recipients. In November 2017–October 2018, recipients averaged 78 days employed, six more than the comparison group; the first year showed no group-level employment effect. A 2018 unemployment-benefit rule change affected the groups differently, preventing researchers from separating its effect from basic income’s second-year effect. The findings therefore neither establish causation nor show what universal basic income would achieve.

### What changed

**Checks set before the run.** Replace 'everyone' with the studied population and preserve the observation period, 78-day average and six-day difference. Distinguish year one from the later period and the unequal rule change from an identified basic-income-only effect.

Both limit the claim to unemployed benefit recipients, give the 78-day average and six-day difference for the correct period, and explain the 2018 rule change. The baseline's final limitation is about extending the result to a universal payment. The skill's final reference to causation reads too broadly in isolation: the specific obstacle was separating the payment from the changed rules in year two, as its preceding sentence explains.

**차이.** 두 답 모두 관찰된 6일 차이를 실업급여 수급자에게 한정하고 2018년 제도 변경을 설명합니다. 스킬 답안의 마지막 ‘인과관계를 입증하지 못한다’는 말은 바로 앞 문장처럼 2년 차 기본소득의 단독 효과에 한정해서 읽는 편이 정확합니다.

## steve-jobs-presentation

**What Ingenuity demonstrated in 39.1 seconds**

2026-11-08 · `steve-jobs-presentation` 0.1.1 · English · Codex CLI 0.167.0 / gpt-6.1-sol

### Case and sources

- [NASA, NASA’s Ingenuity Mars Helicopter Succeeds in Historic First Flight (April 19, 2021)](https://www.nasa.gov/news-release/nasas-ingenuity-mars-helicopter-succeeds-in-historic-first-flight/). Flight-day report: onboard control, altimeter-derived height and hover, total time, the airfield name and plans to analyze the data.

### Prompt

> Write three short speaker beats for a public briefing immediately after Ingenuity's first Mars flight on 19 April 2021. At Wright Brothers Field, onboard guidance flew the helicopter autonomously to about 3 metres. It hovered for 30 seconds and landed after 39.1 seconds of total flight. The team planned to review the flight data before deciding how to fly the next test. Make clear what this meant for powered, controlled flight on another planet. Speak as a presenter reporting the event, using only what was known from this flight.

### Without a skill

> 1. Today, 19 April 2021, Ingenuity achieved powered, controlled flight on another planet for the first time, lifting off from Wright Brothers Field on Mars.
>
> 2. Onboard guidance flew the helicopter autonomously to about three metres. It hovered for 30 seconds, then landed after a total flight time of 39.1 seconds.
>
> 3. This first flight demonstrated that powered, controlled flight is possible on Mars. The team will review the flight data before deciding how to fly the next test.

### With the skill at standard

> 1. Today, 19 April 2021, Ingenuity demonstrated powered, controlled flight on another planet—a first.
>
> 2. At Wright Brothers Field on Mars, its onboard guidance flew the helicopter autonomously to about 3 metres. It hovered for 30 seconds, then landed after a total flight time of 39.1 seconds.
>
> 3. This flight showed that powered, controlled flight on Mars was possible. The next step was to review the flight data before deciding how to fly the next test.

### What changed

**Checks set before the run.** Preserve the date, location, autonomous control, roughly 3 m, 30-second hover versus 39.1-second total and postflight review. Tie the demonstration to powered, controlled flight on Mars without guaranteeing future flights or capacities not tested.

Both distinguish the 30-second hover from the 39.1 seconds between takeoff and landing and end with a review before the next test. The baseline names Wright Brothers Field in the opening; the skill saves the location for the measurement beat. Neither presents a later flight as if it had already happened.

**차이.** 두 발표 모두 30초는 제자리 비행 시간이고 39.1초는 전체 비행 시간이라고 구분합니다. 기체가 뜬 장소를 소개하는 순서는 달라졌지만 두 답 모두 다음 시험의 성공을 약속하지 않습니다.
