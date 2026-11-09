# 화성의 통신 지연이 1분 늘면 지구는 얼마나 더 기다릴까?

[English](standard.md)

2026-11-09 · `answer-with-html` 0.1.8 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [NASA/JPL, Speaking Percy's Language: How to Talk so Perseverance Will Listen](https://science.nasa.gov/blog/speaking-percys-language-how-to-talk-so-perseverance-will-listen/)

NASA/JPL 자료는 지구·화성의 위치에 따라 편도 통신 지연이 약 3~22분이라는 근거를 제공합니다. 준비 시간 10분과 25분 간격의 송신 기회는 이 문제의 가정입니다.

### 질문

> 화성 탐사차 퍼서비어런스와 지구 사이의 통신을 설명하는 한국어 HTML 전시 페이지를 만들어 주세요. NASA에 따르면 전파가 편도로 이동하는 데 약 3~22분이 걸립니다. 다음 송신 일정은 전시를 위해 만든 가정입니다. 지구는 0분에 메시지를 보내고, 탐사차는 받은 뒤 10분간 응답을 준비합니다. 답신 전송은 25분, 50분, 75분처럼 25분 간격의 정해진 시각에만 시작할 수 있습니다. 준비가 끝난 순간이 송신 시각과 정확히 같으면 바로 보낼 수 있습니다. 전파가 양방향에서 걸리는 시간은 같습니다. 편도 지연을 3분부터 22분까지 1분씩 바꿀 수 있도록, 이름이 표시되고 키보드로 조작할 수 있는 슬라이더 하나를 두세요. 초기값은 15분입니다. 답신 준비가 끝나는 시각, 전송 시각, 지구 도착 시각을 보여 주고, 지연을 15분에서 16분으로 올릴 때 도착 시각이 크게 뛰는 이유를 설명해 주세요. 스크립트를 끄더라도 초기 결과를 읽을 수 있어야 합니다. 작은 화면에서도 읽을 수 있게 구성하고, 문서 언어는 ko로 설정하고 화면 안내와 설명은 한국어로 작성하세요. 외부 리소스 없이 HTML 전체만 반환하세요.

### 스킬 미적용 답안

````html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>화성에서 온 답신 — 퍼서비어런스 통신</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #111719;
      --panel: #1c2628;
      --text: #f4f1e8;
      --muted: #bdc8c5;
      --accent: #ffad7a;
      --line: #445251;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: system-ui, -apple-system, "Segoe UI", sans-serif;
      line-height: 1.65;
    }
    main { width: min(100% - 2rem, 760px); margin: 0 auto; padding: 2rem 0 3rem; }
    header { padding: 1.5rem 0 1.25rem; }
    .eyebrow { color: var(--accent); font-size: .85rem; font-weight: 700; letter-spacing: .08em; }
    h1 { margin: .4rem 0 .65rem; font-size: clamp(2rem, 7vw, 3.5rem); line-height: 1.12; }
    h2 { margin: 0 0 .75rem; font-size: 1.25rem; }
    p { margin: .5rem 0; }
    .intro { max-width: 60ch; color: var(--muted); font-size: 1.05rem; }
    .panel {
      margin-top: 1rem;
      padding: clamp(1rem, 4vw, 1.5rem);
      border: 1px solid var(--line);
      border-radius: 1rem;
      background: var(--panel);
    }
    .range-row { display: flex; justify-content: space-between; align-items: baseline; gap: 1rem; }
    output { color: var(--accent); font-size: 1.4rem; font-weight: 800; font-variant-numeric: tabular-nums; }
    input[type="range"] { display: block; width: 100%; margin: 1rem 0 .25rem; accent-color: var(--accent); }
    .range-labels { display: flex; justify-content: space-between; color: var(--muted); font-size: .85rem; }
    .results { display: grid; grid-template-columns: repeat(3, 1fr); gap: .75rem; margin-top: 1rem; }
    .result { padding: 1rem; border-radius: .75rem; background: #121a1b; }
    .result span { display: block; color: var(--muted); font-size: .88rem; }
    .result strong { display: block; margin-top: .25rem; font-size: clamp(1.2rem, 5vw, 1.7rem); font-variant-numeric: tabular-nums; }
    .arrival { color: var(--accent); }
    .note { color: var(--muted); font-size: .92rem; }
    .explain { border-left: 3px solid var(--accent); padding-left: 1rem; }
    .formula { display: inline-block; margin: .4rem 0; padding: .2rem .55rem; border-radius: .4rem; background: #121a1b; font-variant-numeric: tabular-nums; }
    @media (max-width: 560px) {
      main { width: min(100% - 1.25rem, 760px); padding-top: 1rem; }
      .results { grid-template-columns: 1fr; }
      .result { display: flex; align-items: center; justify-content: space-between; gap: .75rem; }
      .result strong { margin: 0; }
    }
  </style>
</head>
<body>
  <main>
    <header>
      <div class="eyebrow">화성 탐사 통신 전시</div>
      <h1>화성에서 온 답신</h1>
      <p class="intro">퍼서비어런스가 지구의 메시지를 받고 답장을 보내기까지, 빛의 속도로도 시간이 걸립니다. 편도 전파 지연을 바꾸며 답신이 지구에 도착하는 시각을 살펴보세요.</p>
    </header>

    <section class="panel" aria-labelledby="control-title">
      <h2 id="control-title">편도 전파 지연</h2>
      <div class="range-row">
        <label for="delay">지구와 화성 사이, 한쪽 방향의 이동 시간</label>
        <output id="delay-value" for="delay">15분</output>
      </div>
      <input id="delay" type="range" min="3" max="22" step="1" value="15"
             aria-describedby="range-help">
      <div class="range-labels" id="range-help"><span>3분</span><span>22분</span></div>

      <div class="results" aria-live="polite">
        <div class="result">
          <span>답신 준비 완료</span>
          <strong id="ready-time">25분</strong>
        </div>
        <div class="result">
          <span>답신 전송 시작</span>
          <strong id="send-time">25분</strong>
        </div>
        <div class="result">
          <span>지구 도착</span>
          <strong class="arrival" id="arrival-time">40분</strong>
        </div>
      </div>
      <p class="note">시간은 지구가 메시지를 보낸 순간을 0분으로 한 경과 시간입니다.</p>
    </section>

    <section class="panel" aria-labelledby="why-title">
      <h2 id="why-title">왜 15분에서 16분으로 바꾸면 크게 늦어질까요?</h2>
      <div class="explain">
        <p>지구의 메시지는 0분에 출발하고, 화성까지 <strong>편도 지연만큼</strong> 걸립니다. 탐사차는 받은 뒤 10분 동안 답신을 준비합니다. 답신은 25분 간격으로 정해진 시각에만 출발할 수 있습니다.</p>
        <p>편도 지연이 15분이면 메시지가 15분에 도착하고, 준비는 25분에 끝납니다. 그 순간이 송신 시각과 같으므로 곧바로 보낼 수 있어 답신은 25분에 출발해 40분에 지구에 도착합니다.</p>
        <p>지연이 16분이면 메시지가 16분에 도착하고 준비는 26분에 끝납니다. 25분 송신 시각을 1분 놓쳐 다음 기회인 50분까지 기다립니다. 왕복 전파 시간도 1분씩 늘어나므로 지구 도착은 40분에서 82분으로, 총 42분 늦어집니다.</p>
        <p class="formula">준비 완료 = 편도 지연 + 10분 · 송신 = 준비 완료 이후 첫 25분 간격 시각 · 지구 도착 = 송신 + 편도 지연</p>
      </div>
    </section>

    <p class="note">NASA에 따르면 퍼서비어런스와 지구 사이의 전파는 편도로 약 3~22분 걸릴 수 있습니다. 이 전시의 10분 준비 시간과 25분 간격 송신 일정은 설명을 위한 가정입니다.</p>
  </main>

  <script>
    const slider = document.getElementById("delay");
    const delayValue = document.getElementById("delay-value");
    const readyTime = document.getElementById("ready-time");
    const sendTime = document.getElementById("send-time");
    const arrivalTime = document.getElementById("arrival-time");

    function update() {
      const delay = Number(slider.value);
      const ready = delay + 10;
      const send = Math.ceil(ready / 25) * 25;
      delayValue.textContent = delay + "분";
      readyTime.textContent = ready + "분";
      sendTime.textContent = send + "분";
      arrivalTime.textContent = (send + delay) + "분";
    }

    slider.addEventListener("input", update);
    update();
  </script>
</body>
</html>
````

### 스킬 적용 답안 · standard

````html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>화성과 지구 사이, 답신은 언제 도착할까?</title>
  <style>
    :root {
      color-scheme: dark;
      font-family: system-ui, -apple-system, "Malgun Gothic", sans-serif;
      background: #101827;
      color: #f3f6fb;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      padding: clamp(1rem, 5vw, 3rem);
      background:
        radial-gradient(ellipse at 80% 5%, #273b63 0, transparent 38rem),
        #101827;
    }
    main { width: min(100%, 48rem); margin: 0 auto; }
    .eyebrow { color: #a9c5ff; letter-spacing: .08em; font-size: .82rem; }
    h1 { line-height: 1.2; font-size: clamp(1.8rem, 7vw, 3rem); margin: .5rem 0 1rem; }
    p { line-height: 1.65; color: #d1d9e8; }
    .card {
      margin-top: 1.5rem;
      padding: clamp(1rem, 4vw, 1.6rem);
      border: 1px solid #3b4b67;
      border-radius: 1rem;
      background: #182337;
    }
    label { display: block; font-weight: 700; margin-bottom: .75rem; }
    input[type="range"] { width: 100%; accent-color: #9cc4ff; }
    .range-labels { display: flex; justify-content: space-between; color: #aebbd0; font-size: .9rem; }
    output {
      display: block;
      margin-top: 1.3rem;
      padding: 1rem;
      border-radius: .75rem;
      background: #101827;
      color: #fff;
      line-height: 1.8;
      overflow-wrap: anywhere;
    }
    output strong { color: #a9c5ff; }
    .note { font-size: .9rem; color: #aebbd0; }
    :focus-visible { outline: 3px solid #ffd166; outline-offset: 4px; }
  </style>
</head>
<body>
  <main>
    <p class="eyebrow">화성 탐사 통신 전시</p>
    <h1>답신은 언제 지구에 도착할까?</h1>
    <p>지구에서 보낸 메시지가 퍼서비어런스에 도착한 뒤, 탐사차는 10분 동안 답신을 준비합니다. 하지만 답신은 정해진 송신 시각에만 보낼 수 있습니다. 편도 전파 지연을 바꾸며 도착 시각이 어떻게 달라지는지 살펴보세요.</p>

    <section class="card" aria-labelledby="assumptions-title">
      <h2 id="assumptions-title">전시의 가정</h2>
      <p>지구는 0분에 메시지를 보냅니다. 편도 지연은 양방향에서 같고, 답신 송신은 25분 간격의 시각(25분, 50분, 75분…)에 시작할 수 있습니다. 준비 완료 시각과 송신 시각이 같으면 바로 전송합니다. NASA에 따르면 실제 편도 전파 시간은 약 3~22분입니다. 송신 일정과 준비 시간은 전시를 위해 정한 가정입니다.</p>
    </section>

    <section class="card" aria-labelledby="control-title">
      <h2 id="control-title">편도 지연 조절</h2>
      <label for="delay">편도 전파 지연: <span id="delay-value">15</span>분</label>
      <input id="delay" type="range" min="3" max="22" step="1" value="15"
             aria-label="편도 전파 지연, 3분부터 22분까지">
      <div class="range-labels" aria-hidden="true"><span>3분</span><span>22분</span></div>

      <output id="result" aria-live="polite">
        편도 지연 15분 · 답신 준비 완료 25분 · 답신 전송 25분 · 지구 도착 40분
      </output>
    </section>

    <section class="card" aria-labelledby="why-title">
      <h2 id="why-title">15분에서 16분으로 바꾸면 왜 크게 뛸까?</h2>
      <p>15분 지연이면 메시지가 탐사차에 15분에 도착하고, 10분 준비 뒤 25분에 답신을 보낼 수 있습니다. 지연이 16분이면 준비 완료는 26분입니다. 25분 송신 시각을 이미 지나서 다음 기회인 50분까지 기다려야 하므로, 도착 시각도 크게 늦어집니다. 정해진 송신 시각 사이에서는 준비 완료 시각이 다음 송신 기회를 넘기는 순간 대기 시간이 한 번에 늘어납니다.</p>
    </section>
  </main>
  <script>
    const slider = document.getElementById("delay");
    const delayValue = document.getElementById("delay-value");
    const result = document.getElementById("result");

    function calculate(rawValue) {
      const delay = Number(rawValue);
      if (!Number.isFinite(delay) || delay < 3 || delay > 22) return null;
      const ready = delay + 10;
      const send = Math.ceil(ready / 25) * 25;
      const arrival = send + delay;
      return { delay, ready, send, arrival };
    }

    function render() {
      const values = calculate(slider.value);
      if (!values) return;
      delayValue.textContent = String(values.delay);
      result.textContent =
        `편도 지연 ${values.delay}분 · 답신 준비 완료 ${values.ready}분 · ` +
        `답신 전송 ${values.send}분 · 지구 도착 ${values.arrival}분`;
    }

    slider.addEventListener("input", render);
    render();
  </script>
</body>
</html>
````

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 초기 편도 지연 15분일 때 스크립트 없이도 준비 25분·전송 25분·지구 도착 40분을 확인할 수 있고, 송신 일정이 가정임을 밝힌다. | 충족 | 충족 |
| 편도 지연 16분에서는 26분·50분·66분을 표시하고, 25분 송신 시각을 놓쳤기 때문에 도착 시각이 뛰는 이유를 설명한다. | 미충족 | 충족 |
| 한국어로 이름을 표시한 키보드 조작 슬라이더가 3~22분을 1분씩 바꾸며, 양 끝에서 지구 도착이 각각 28분·72분으로 갱신된다. 외부 리소스를 쓰지 않는다. | 충족 | 충족 |

**검토 결과.** 스크립트를 끈 첫 화면에서 25·25·40분을 확인했습니다. 편도 16분에서는 송신 시각을 놓쳐 26·50·66분이 되고, 키보드로 양 끝을 선택하면 지구 도착이 28분과 72분으로 바뀝니다.

익명 채점에서 개정 답안은 Y였습니다. 표에는 기존 미적용 답안의 판정을 그대로 실었습니다. [이전 답안과 점수](https://github.com/hobin01/writing-styles-from-giants/blob/20f24c66c7e89e6ce1007249c83c33932998bf01/skills/answer-with-html/examples/standard.ko.md) · [모든 시도와 판정 근거](https://github.com/hobin01/writing-styles-from-giants/blob/main/evals/runs/2026-11-09-standard/records/answer-with-html.json).

<details>
<summary>실행 기록</summary>

미적용 답안은 2026-11-08에 생성했습니다. 개정 답안은 2026-11-09에 Codex CLI 0.167.0, low 추론 설정으로 읽기 전용 독립 세션에서 생성했습니다. SHA-256 앞 12자리 (스킬 지침 / 기존 미적용 원문 / 개정 답안): `318335a72a76` / `aa3daa7508a3` / `7a548d0ad983`.

</details>
