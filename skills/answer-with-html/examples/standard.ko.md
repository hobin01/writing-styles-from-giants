# 화성의 통신 지연이 1분 늘면 지구는 얼마나 더 기다릴까?

[English](standard.md)

2026-11-08 · `answer-with-html` 0.1.2 · 한국어 · `gpt-6-luna`

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
  <title>화성에서 온 답신 — 퍼서비어런스 통신</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #10151b;
      --panel: #19212a;
      --line: #35424d;
      --text: #f1f4f6;
      --muted: #bdc7d0;
      --accent: #ffb36b;
      --earth: #77c8ff;
      --mars: #ff9273;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: radial-gradient(ellipse at 50% 0%, #26313a 0, var(--bg) 55%);
      color: var(--text);
      font-family: system-ui, -apple-system, "Malgun Gothic", sans-serif;
      line-height: 1.65;
    }
    main {
      width: min(900px, 100%);
      margin: 0 auto;
      padding: 32px 20px 52px;
    }
    header { margin-bottom: 24px; }
    .eyebrow {
      margin: 0 0 6px;
      color: var(--accent);
      font-size: .85rem;
      font-weight: 700;
      letter-spacing: .08em;
    }
    h1 { margin: 0; font-size: clamp(1.8rem, 6vw, 3rem); line-height: 1.2; }
    .intro { max-width: 66ch; color: var(--muted); margin: 14px 0 0; }
    .card {
      background: color-mix(in srgb, var(--panel) 94%, transparent);
      border: 1px solid var(--line);
      border-radius: 18px;
      padding: clamp(18px, 4vw, 30px);
      margin-top: 18px;
    }
    h2 { margin: 0 0 14px; font-size: 1.25rem; }
    .control-row {
      display: flex;
      justify-content: space-between;
      gap: 12px;
      align-items: baseline;
    }
    label { font-weight: 700; }
    output { color: var(--accent); font-weight: 800; font-variant-numeric: tabular-nums; }
    input[type="range"] {
      display: block;
      width: 100%;
      margin: 18px 0 4px;
      accent-color: var(--accent);
      min-height: 32px;
    }
    .range-labels {
      display: flex;
      justify-content: space-between;
      color: var(--muted);
      font-size: .85rem;
    }
    .results {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin: 22px 0 0;
    }
    .result {
      min-width: 0;
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 14px;
      background: #121920;
    }
    .result dt { color: var(--muted); font-size: .9rem; }
    .result dd {
      margin: 4px 0 0;
      font-size: clamp(1.3rem, 4vw, 1.8rem);
      font-weight: 800;
      font-variant-numeric: tabular-nums;
    }
    .timeline {
      margin: 20px 0 0;
      padding: 0;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 8px;
      list-style: none;
    }
    .timeline li {
      border-top: 2px solid var(--line);
      padding-top: 8px;
      color: var(--muted);
      font-size: .85rem;
    }
    .timeline strong { display: block; color: var(--text); font-size: 1rem; }
    .earth { color: var(--earth); }
    .mars { color: var(--mars); }
    .explain { margin: 0; }
    .equation {
      margin: 14px 0;
      padding: 12px 14px;
      border-left: 3px solid var(--accent);
      background: #121920;
      font-variant-numeric: tabular-nums;
    }
    .note { color: var(--muted); font-size: .92rem; }
    @media (max-width: 560px) {
      main { padding: 24px 14px 36px; }
      .results { grid-template-columns: 1fr; }
      .result { display: flex; justify-content: space-between; align-items: center; gap: 10px; }
      .result dd { margin: 0; }
    }
  </style>
</head>
<body>
  <main>
    <header>
      <p class="eyebrow">지구 ↔ 화성 · 빛의 속도로 오가는 메시지</p>
      <h1>화성에서 온 답신</h1>
      <p class="intro">
        지구가 보낸 신호를 퍼서비어런스가 받고, 답신을 준비해 다시 지구로 보냅니다.
        전파는 편도로 약 3~22분 걸립니다. 거리가 멀수록 대화에는 기다림이 생깁니다.
      </p>
    </header>

    <section class="card" aria-labelledby="controls-title">
      <h2 id="controls-title">전파 지연을 바꿔 보기</h2>
      <div class="control-row">
        <label for="delay">편도 전파 지연</label>
        <output id="delay-value" for="delay">15분</output>
      </div>
      <input id="delay" type="range" min="3" max="22" step="1" value="15"
             aria-label="편도 전파 지연, 3분에서 22분">
      <div class="range-labels" aria-hidden="true"><span>3분</span><span>22분</span></div>

      <dl class="results" aria-live="polite">
        <div class="result">
          <dt>탐사차가 받은 시각</dt>
          <dd><span id="received">15</span>분</dd>
        </div>
        <div class="result">
          <dt>답신 준비 완료</dt>
          <dd><span id="ready">25</span>분</dd>
        </div>
        <div class="result">
          <dt>지구에 도착</dt>
          <dd><span id="arrival">65</span>분</dd>
        </div>
      </dl>

      <ol class="timeline" aria-label="현재 지연에서 메시지가 오가는 순서">
        <li><strong class="earth">0분</strong>지구가 메시지 전송</li>
        <li><strong class="mars"><span id="received-timeline">15</span>분</strong>탐사차가 수신</li>
        <li><strong class="earth"><span id="send">25</span>분 전송</strong>답신, 지구에는 <span id="arrival-timeline">65</span>분 도착</li>
      </ol>
      <p class="note">전시를 위해 설정한 일정: 수신 후 준비에 10분이 걸리고, 답신은 25분 간격의 시각(25분, 50분, 75분…)에만 전송을 시작합니다. 준비 완료와 전송 시각이 같으면 바로 보냅니다.</p>
    </section>

    <section class="card" aria-labelledby="why-title">
      <h2 id="why-title">15분에서 16분으로 바꾸면 왜 크게 늦어질까요?</h2>
      <p class="explain">
        15분 지연이면 탐사차는 15분에 메시지를 받고, 10분 뒤인 25분에 준비를 마칩니다.
        이때는 전송 시작 시각과 딱 맞아 바로 답신을 보냅니다. 답신은 15분 더 이동해 40분에 지구에 도착합니다.
      </p>
      <p class="equation">15분 지연: 수신 15분 → 준비 완료 25분 → 전송 25분 → 지구 도착 40분</p>
      <p class="explain">
        지연이 16분이면 수신은 16분, 준비 완료는 26분입니다. 25분 전송 시각을 놓쳤으므로 다음 기회인 50분까지 기다립니다.
        왕복 전파 시간은 32분으로 2분만 늘었지만, 전송 대기 시간이 0분에서 24분으로 늘어 도착은 40분에서 82분으로 42분 늦어집니다.
      </p>
      <p class="equation">16분 지연: 수신 16분 → 준비 완료 26분 → 다음 전송 50분 → 지구 도착 82분</p>
      <p class="note">모형의 계산: 준비 완료 = 편도 지연 + 10분. 전송 시각은 준비 완료 이후 처음 만나는 25분 간격 시각이며, 도착 시각 = 전송 시각 + 편도 지연. 실제 통신 지연은 화성과 지구의 위치에 따라 달라집니다.</p>
    </section>
  </main>

  <script>
    const slider = document.getElementById("delay");
    const delayValue = document.getElementById("delay-value");
    const received = document.getElementById("received");
    const ready = document.getElementById("ready");
    const send = document.getElementById("send");
    const arrival = document.getElementById("arrival");
    const receivedTimeline = document.getElementById("received-timeline");
    const arrivalTimeline = document.getElementById("arrival-timeline");

    function update() {
      const delay = Number(slider.value);
      if (!Number.isFinite(delay) || delay < 3 || delay > 22) return;

      const receivedAt = delay;
      const readyAt = receivedAt + 10;
      const sendAt = Math.ceil(readyAt / 25) * 25;
      const arrivalAt = sendAt + delay;

      delayValue.textContent = delay + "분";
      received.textContent = receivedAt;
      ready.textContent = readyAt;
      send.textContent = sendAt + "분 전송";
      arrival.textContent = arrivalAt;
      receivedTimeline.textContent = receivedAt;
      arrivalTimeline.textContent = arrivalAt;
    }

    slider.addEventListener("input", update);
  </script>
</body>
</html>
````

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 초기 편도 지연 15분일 때 스크립트 없이도 준비 25분·전송 25분·지구 도착 40분을 확인할 수 있고, 송신 일정이 가정임을 밝힌다. | 충족 | 미충족 |
| 편도 지연 16분에서는 26분·50분·66분을 표시하고, 25분 송신 시각을 놓쳤기 때문에 도착 시각이 뛰는 이유를 설명한다. | 미충족 | 미충족 |
| 한국어로 이름을 표시한 키보드 조작 슬라이더가 3~22분을 1분씩 바꾸며, 양 끝에서 지구 도착이 각각 28분·72분으로 갱신된다. 외부 리소스를 쓰지 않는다. | 충족 | 충족 |

**블라인드 검토** (X = 미적용, Y = 스킬 적용). 양쪽 모두 한국어 화면에서 키보드로 편도 3분과 22분을 골랐을 때 지구 도착을 각각 28분과 72분으로 표시합니다. 스크립트를 끈 초기 화면에서 X 쪽은 25·25·40분으로 맞지만, Y 쪽은 지구 도착을 65분으로 표시합니다. 편도 16분의 동적 표시는 양쪽 모두 26·50·66분입니다. 그러나 고정 설명문은 둘 다 지구 도착을 82분으로 써서 표시된 계산과 모순됩니다.

Chromium 156.0.8078.80에서 편도 15분일 때 미적용 페이지는 25/25/40분을, 스킬 페이지는 25/25/65분을 표시했습니다. 스크립트를 끈 상태에서도 같았습니다. 편도 16분의 동적 표시는 두 페이지 모두 26/50/66분이었지만 본문에는 각각 82분으로 잘못 적혔습니다. 양 끝값과 키보드 조작은 동작했고, 외부 요청이나 스크립트 오류, 320 CSS 픽셀에서의 가로 넘침은 없었습니다.

<details>
<summary>별도 재실행 · 버전 0.1.3</summary>

정적 HTML·슬라이더·본문을 같은 계산으로 확인하도록 수정하고 동일한 한국어 질문으로 다시 실행했습니다. 새 답안은 초기 25/25/40분과 변경 후 26/50/66분을 표시하며 본문의 82분 오류도 고쳤습니다. 다만 대기 시간이 “25분 늘어”났다는 문장은 여전히 부정확합니다. 전송 시각이 25분에서 50분으로 이동하고, 준비 후 대기는 0분에서 24분으로 늘며, 최종 도착은 26분 늦어집니다.

````html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>화성에서 온 답신 — 퍼서비어런스와 지구의 통신</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #101820;
      --panel: #192630;
      --text: #f3efe5;
      --muted: #bac5c9;
      --accent: #ffb36b;
      --line: #42535b;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      background: radial-gradient(ellipse at 80% 0%, #293841 0, var(--bg) 58%);
      color: var(--text);
      font: 1rem/1.6 system-ui, -apple-system, "Noto Sans KR", sans-serif;
    }
    main {
      width: min(100% - 2rem, 850px);
      margin: 0 auto;
      padding: clamp(1.5rem, 5vw, 3.5rem) 0;
    }
    header { margin-bottom: 1.5rem; }
    .eyebrow { color: var(--accent); font-weight: 700; letter-spacing: .08em; }
    h1 { margin: .3rem 0 .7rem; font-size: clamp(1.8rem, 6vw, 3rem); line-height: 1.2; }
    h2 { margin-top: 0; font-size: 1.25rem; }
    p { margin: .6rem 0; }
    .muted { color: var(--muted); }
    .panel {
      margin: 1rem 0;
      padding: clamp(1rem, 4vw, 1.5rem);
      background: color-mix(in srgb, var(--panel) 92%, transparent);
      border: 1px solid var(--line);
      border-radius: 1rem;
    }
    .range-row {
      display: flex;
      justify-content: space-between;
      gap: 1rem;
      align-items: baseline;
    }
    output { color: var(--accent); font-size: 1.35rem; font-weight: 750; }
    input[type="range"] { width: 100%; margin: 1rem 0 .25rem; accent-color: var(--accent); }
    input:focus-visible { outline: 3px solid #fff; outline-offset: 4px; }
    .bounds { display: flex; justify-content: space-between; color: var(--muted); font-size: .9rem; }
    .timeline {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: .7rem;
      margin-top: 1rem;
    }
    .event {
      padding: .9rem;
      border-left: 3px solid var(--accent);
      background: #111b22;
      border-radius: .25rem .7rem .7rem .25rem;
    }
    .event span { display: block; color: var(--muted); font-size: .9rem; }
    .event strong { display: block; margin-top: .2rem; font-size: 1.25rem; }
    .diagram { width: 100%; height: auto; display: block; margin: 1rem 0 .3rem; }
    .callout { border-left: 3px solid var(--accent); padding-left: 1rem; }
    code { color: #ffd0a4; }
    @media (max-width: 560px) {
      .timeline { grid-template-columns: 1fr; }
      .event strong { font-size: 1.15rem; }
    }
  </style>
</head>
<body>
<main>
  <header>
    <div class="eyebrow">화성 통신 전시</div>
    <h1>화성에서 온 답신은 언제 도착할까?</h1>
    <p>퍼서비어런스와 지구 사이의 전파는 빛의 속도로 이동하지만, 거리가 멀어 편도에 약 3~22분이 걸립니다. 그래서 지구의 메시지를 받은 뒤 답신을 준비해도, 지구에는 한참 뒤에 도착합니다.</p>
  </header>

  <section class="panel" aria-labelledby="model-title">
    <h2 id="model-title">전시의 가정</h2>
    <p>지구는 0분에 메시지를 보냅니다. 탐사차는 메시지를 받은 뒤 10분 동안 답신을 준비합니다. 답신은 전시를 위해 정한 25분 간격의 시각(25분, 50분, 75분 …)에만 전송을 시작할 수 있습니다. 준비가 그 시각에 정확히 끝나면 바로 전송합니다. 왕복 편도 지연은 같다고 가정합니다.</p>
    <p class="muted">아래 일정은 설명을 위한 가정이며 실제 퍼서비어런스의 송신 일정이 아닙니다.</p>
  </section>

  <section class="panel" aria-labelledby="explorer-title">
    <h2 id="explorer-title">편도 지연을 바꿔 보기</h2>
    <div class="range-row">
      <label for="delay">전파의 편도 지연</label>
      <output id="delay-value" for="delay">15분</output>
    </div>
    <input id="delay" type="range" min="3" max="22" step="1" value="15" aria-describedby="range-hint">
    <div class="bounds" id="range-hint"><span>3분</span><span>22분</span></div>

    <div class="timeline" aria-live="polite" aria-atomic="true">
      <div class="event">
        <span>답신 준비 완료</span>
        <strong id="ready-time">25분</strong>
      </div>
      <div class="event">
        <span>답신 전송 시작</span>
        <strong id="send-time">25분</strong>
      </div>
      <div class="event">
        <span>지구 도착</span>
        <strong id="arrival-time">40분</strong>
      </div>
    </div>

    <svg class="diagram" viewBox="0 0 760 145" role="img" aria-labelledby="diagram-title diagram-desc">
      <title id="diagram-title">지구와 화성 탐사차 사이의 왕복 통신</title>
      <desc id="diagram-desc">지구에서 보낸 메시지가 편도 지연 뒤 화성에 도착하고, 준비된 답신이 정해진 송신 시각에 출발해 같은 편도 지연 뒤 지구에 도착합니다.</desc>
      <defs>
        <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
          <path d="M0,0 L0,6 L7,3 z" fill="#ffb36b"></path>
        </marker>
      </defs>
      <circle cx="70" cy="73" r="25" fill="#6bb8e8"></circle>
      <text x="70" y="78" text-anchor="middle" fill="#101820" font-size="14" font-weight="700">지구</text>
      <circle cx="690" cy="73" r="25" fill="#d8754d"></circle>
      <text x="690" y="78" text-anchor="middle" fill="#101820" font-size="12" font-weight="700">화성</text>
      <line x1="110" y1="49" x2="646" y2="49" stroke="#ffb36b" stroke-width="3" marker-end="url(#arrow)"></line>
      <text x="378" y="38" text-anchor="middle" fill="#f3efe5" font-size="14">메시지: 편도 지연</text>
      <line x1="650" y1="103" x2="114" y2="103" stroke="#ffb36b" stroke-width="3" marker-end="url(#arrow)"></line>
      <text x="378" y="133" text-anchor="middle" fill="#f3efe5" font-size="14">답신: 전송 시각 이후 같은 편도 지연</text>
    </svg>
    <p class="muted">그림은 통신 방향을 나타냅니다. 실제 거리나 이동 경로의 축척은 아닙니다.</p>
  </section>

  <section class="panel" aria-labelledby="jump-title">
    <h2 id="jump-title">15분에서 16분으로 바꾸면 왜 크게 뛸까?</h2>
    <p>지연이 15분이면 메시지는 15분에 화성에 도착하고, 10분 준비를 마친 시각은 25분입니다. 이 시각이 송신 가능 시각과 일치하므로 답신을 바로 보내고, 15분 뒤인 40분에 지구에 도착합니다.</p>
    <p>지연을 16분으로 늘리면 준비 완료 시각은 26분입니다. 25분 송신 시각은 이미 지나갔으므로 다음 기회인 50분까지 기다려야 합니다. 답신은 50분에 출발해 16분 뒤인 66분에 도착합니다. 편도 지연은 1분만 늘었지만, 송신 일정의 경계가 바뀌면서 대기 시간이 25분 늘어나 도착은 26분 늦어집니다.</p>
    <p class="callout"><strong>계산 규칙</strong><br>
      준비 완료 = 편도 지연 + 10분<br>
      전송 시각 = 준비 완료 이후 처음 만나는 25분 간격의 시각(같으면 즉시)<br>
      지구 도착 = 전송 시각 + 편도 지연
    </p>
  </section>

  <footer class="muted">
    <p>편도 지연 범위(약 3~22분)는 NASA가 제시한 값입니다. 전송 간격과 준비 시간은 이 전시의 가정입니다.</p>
  </footer>
</main>
<script>
  (() => {
    const slider = document.getElementById("delay");
    const delayValue = document.getElementById("delay-value");
    const readyTime = document.getElementById("ready-time");
    const sendTime = document.getElementById("send-time");
    const arrivalTime = document.getElementById("arrival-time");

    function update() {
      const delay = Number(slider.value);
      if (!Number.isFinite(delay) || delay < 3 || delay > 22) return;
      const ready = delay + 10;
      const send = Math.ceil(ready / 25) * 25;
      const arrival = send + delay;
      delayValue.textContent = `${delay}분`;
      readyTime.textContent = `${ready}분`;
      sendTime.textContent = `${send}분`;
      arrivalTime.textContent = `${arrival}분`;
    }

    slider.addEventListener("input", update);
  })();
</script>
</body>
</html>
````

</details>

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `a45f928bc29a` / `aa3daa7508a3` / `6326ba04aeda`.

</details>
