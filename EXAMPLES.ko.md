# 한국어로 직접 실행한 글쓰기 스킬 22개

[English examples](EXAMPLES.md)

[서로 다른 시각에 조회한 DNS 리졸버](#feynman-technique), [송신 기회를 놓친 화성 탐사차](#answer-with-html), [서울 지하철 노선도](#hunminjeongeum) 중 하나를 골라 보세요. 각 항목에는 한국어 질문, 스킬 없이 쓴 답, `standard`로 쓴 답과 판정 기준 세 가지가 있습니다.

## 어떻게 비교했나요?

2026년 11월 8일, 영어와 한국어에 같은 사례와 계산 조건을 주되 각 언어에 맞는 질문으로 따로 실행했습니다. 예를 들어 한국어 평문 스킬의 영문 예제에서는 편집자가 한국어 문장을 영어로 검토합니다. New Hart’s Rules의 한국어 예제에서는 편집할 영문 전시 문구는 유지하고, 편집 이유를 한국어로 설명합니다.

Codex CLI 0.167.0에서 평가 모델을 `gpt-6-luna`, 추론 설정을 low로 지정했습니다. 답안마다 저장소 밖의 새 임시 디렉터리에서 읽기 전용 세션을 열었습니다. 미적용 세션에는 그 언어의 질문만, 적용 세션에는 같은 질문과 해당 스킬 지침을 주었습니다. 어느 세션에도 다른 답안이나 번역할 원문 답안을 주지 않았고, 도구를 사용한 실행은 채택하지 않았습니다. 모델의 세부 빌드 번호는 제공되지 않았습니다. 수식과 줄바꿈, 빈 줄의 공백은 마크다운에 맞게 표시했고, 각 예제에 원문 해시를 기록했습니다.

판정 기준 세 개를 먼저 정한 뒤, 검토자에게 어느 답이 스킬을 썼는지 가리고 비교했습니다. 일부 답이 스스로 방법 이름을 밝혀 가림이 완전하지는 않았습니다. 한국어 22문항에서 스킬 답이 더 많은 기준을 충족한 경우는 4개, 같은 개수는 13개, 더 적게 충족한 경우는 5개였습니다. 각 언어에서 문항별로 답안 한 쌍을 본 결과이므로 언어 간 성능 순위를 뜻하지 않습니다.

영어·한국어의 본 비교에는 답안 88개가 있습니다. 영어 ELI5와 한국어 서울 지하철 노선도 예제에는 표현을 명확히 하기 전의 답안도 각각 두 개 남겼습니다. 화성 기후 궤도선 예제는 생성 후 한국어 판정 기준의 표현 한 곳을 바로잡고 익명으로 재검토했습니다. HTML 예제에는 본문과 화면의 수치가 달랐던 첫 답안과, 지침 수정 후 각 언어에서 새로 생성한 스킬 답안 한 개씩을 실었습니다. 추가 답안 여섯 개는 위 집계에서 제외했습니다. [이전 Luna 평가 기록](https://github.com/hobin01/writing-styles-from-giants/blob/06f7e14e4b9f1e1081e817d7f828278def138742/EXAMPLES.md)도 확인할 수 있습니다. 읽기 쉽게 마크다운 줄바꿈과 수식 표기를 조정한 곳이 있으며, 각 항목의 실행 기록에서 원문 해시를 확인할 수 있습니다.

스킬별 `examples/standard.md`(영어), `examples/standard.ko.md`(한국어)를 수정한 뒤 `python3 scripts/build_example_gallery.py`를 실행하면 두 모음이 함께 갱신됩니다.

<!-- Standard examples below are generated. -->

- [amazon-six-page-narrative](#amazon-six-page-narrative) · [스킬별 예제](skills/amazon-six-page-narrative/examples/standard.ko.md) · [English](EXAMPLES.md#amazon-six-page-narrative)
- [answer-with-html](#answer-with-html) · [스킬별 예제](skills/answer-with-html/examples/standard.ko.md) · [English](EXAMPLES.md#answer-with-html)
- [aristotle-syllogism](#aristotle-syllogism) · [스킬별 예제](skills/aristotle-syllogism/examples/standard.ko.md) · [English](EXAMPLES.md#aristotle-syllogism)
- [asd-ste100](#asd-ste100) · [스킬별 예제](skills/asd-ste100/examples/standard.ko.md) · [English](EXAMPLES.md#asd-ste100)
- [boring-professor](#boring-professor) · [스킬별 예제](skills/boring-professor/examples/standard.ko.md) · [English](EXAMPLES.md#boring-professor)
- [diataxis](#diataxis) · [스킬별 예제](skills/diataxis/examples/standard.ko.md) · [English](EXAMPLES.md#diataxis)
- [eli5](#eli5) · [스킬별 예제](skills/eli5/examples/standard.ko.md) · [English](EXAMPLES.md#eli5)
- [federal-plain-language](#federal-plain-language) · [스킬별 예제](skills/federal-plain-language/examples/standard.ko.md) · [English](EXAMPLES.md#federal-plain-language)
- [feynman-technique](#feynman-technique) · [스킬별 예제](skills/feynman-technique/examples/standard.ko.md) · [English](EXAMPLES.md#feynman-technique)
- [google-design-doc](#google-design-doc) · [스킬별 예제](skills/google-design-doc/examples/standard.ko.md) · [English](EXAMPLES.md#google-design-doc)
- [gtm-formal](#gtm-formal) · [스킬별 예제](skills/gtm-formal/examples/standard.ko.md) · [English](EXAMPLES.md#gtm-formal)
- [hunminjeongeum](#hunminjeongeum) · [스킬별 예제](skills/hunminjeongeum/examples/standard.ko.md) · [English](EXAMPLES.md#hunminjeongeum)
- [ietf-rfc](#ietf-rfc) · [스킬별 예제](skills/ietf-rfc/examples/standard.ko.md) · [English](EXAMPLES.md#ietf-rfc)
- [imrad](#imrad) · [스킬별 예제](skills/imrad/examples/standard.ko.md) · [English](EXAMPLES.md#imrad)
- [korean-plain-language](#korean-plain-language) · [스킬별 예제](skills/korean-plain-language/examples/standard.ko.md) · [English](EXAMPLES.md#korean-plain-language)
- [microsoft-writing-style](#microsoft-writing-style) · [스킬별 예제](skills/microsoft-writing-style/examples/standard.ko.md) · [English](EXAMPLES.md#microsoft-writing-style)
- [minto-pyramid](#minto-pyramid) · [스킬별 예제](skills/minto-pyramid/examples/standard.ko.md) · [English](EXAMPLES.md#minto-pyramid)
- [new-harts-rules](#new-harts-rules) · [스킬별 예제](skills/new-harts-rules/examples/standard.ko.md) · [English](EXAMPLES.md#new-harts-rules)
- [nist-technical-publication](#nist-technical-publication) · [스킬별 예제](skills/nist-technical-publication/examples/standard.ko.md) · [English](EXAMPLES.md#nist-technical-publication)
- [orwell-six-rules](#orwell-six-rules) · [스킬별 예제](skills/orwell-six-rules/examples/standard.ko.md) · [English](EXAMPLES.md#orwell-six-rules)
- [socratic-self-questioning](#socratic-self-questioning) · [스킬별 예제](skills/socratic-self-questioning/examples/standard.ko.md) · [English](EXAMPLES.md#socratic-self-questioning)
- [steve-jobs-presentation](#steve-jobs-presentation) · [스킬별 예제](skills/steve-jobs-presentation/examples/standard.ko.md) · [English](EXAMPLES.md#steve-jobs-presentation)

## amazon-six-page-narrative

**두 교량 중 어느 쪽의 하중 평가부터 해야 할까요?**

[English](EXAMPLES.md#amazon-six-page-narrative)

2026-11-08 · `amazon-six-page-narrative` 0.1.2 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [NTSB, investigation HWY07MH024, Collapse of I-35W Highway Bridge, Minneapolis, Minnesota](https://www.ntsb.gov/investigations/Pages/HWY07MH024.aspx)

NTSB는 미니애폴리스 I-35W 교량 붕괴의 원인으로 U10 연결판의 부족한 용량과 복합 하중을 조사했습니다. 다른 두 교량의 이름과 하중 단위는 의사결정 연습을 위한 가정입니다.

### 질문

> 두 강트러스교에 건설 자재를 쌓아 둘지 검토하는 가상의 교량 관리기관을 위해 한국어 의사결정 메모의 첫 문단을 써 주세요. 미니애폴리스 I-35W 붕괴 조사에서 미국 국가교통안전위원회(NTSB)는 U10 이음부의 거싯 플레이트가 증설·교통·집중된 공사 하중을 함께 견디기에 부족했으며, 기존 하중 평가에서는 이 판이 빠졌다고 판단했습니다. 다음은 실제 교량 평가가 아닌 교육용 예비 검토입니다. 리버 스트리트 교량은 연결판의 추정 용량이 100이고 기존 하중 68, 증설 하중 18, 적재 예정 하중 24가 동시에 작용합니다. 커낼 스트리트 교량의 해당 하중은 66, 14, 15이며 용량은 모릅니다. 두 교량 모두 육안 검사에서 새 손상은 보이지 않았고 최종 공학 평가는 없습니다. 즉시 정밀 하중 평가를 할 예산은 한 곳분입니다. 평가 우선순위, 두 곳의 자재 적재 여부, 그 이유를 한 문단에 담아 주세요.

### 스킬 미적용 답안

> 예산이 한 곳분인 정밀 하중 평가는 리버 스트리트 교량에 우선 배정해야 합니다. 추정 용량 100에 기존 하중 68, 증설 하중 18, 예정 적재 하중 24를 합하면 총 110으로 용량을 넘으며, 하중이 동시에 작용하는 조건은 I-35W 조사에서 확인된 위험과 관련이 있습니다. 따라서 정밀 평가가 끝날 때까지 리버에는 자재를 적재하지 않는 것이 타당합니다. 커낼 스트리트는 합산 하중이 95이지만 용량을 모르므로, 안전하다고 단정하거나 적재를 승인할 근거가 없습니다. 우선 적재를 보류하고, 리버 평가 뒤 확보되는 예산으로 정밀 평가를 받도록 해야 합니다. 두 교량 모두 새 손상이 보이지 않았다는 육안 검사 결과만으로는 하중 안전성을 판단할 수 없으며, 이는 실제 교량 평가가 아닌 교육용 예비 검토입니다.

### 스킬 적용 답안 · standard

> 커낼 스트리트 교량의 정밀 하중 평가를 먼저 승인하고, 평가가 끝날 때까지 두 교량 모두에 자재를 적재하지 않을 것을 권고합니다. 리버 스트리트 교량은 교육용 예비 검토에서 추정 용량 100에 기존 하중 68, 증설 하중 18, 예정 적재 하중 24가 동시에 작용해 합계 110으로 추정 용량을 넘습니다. 커낼 스트리트 교량은 해당 하중이 66, 14, 15로 합계 95이지만 용량을 모릅니다. I-35W 붕괴 조사에서 NTSB는 U10 거싯 플레이트가 여러 하중을 함께 견디기에 부족했고 기존 평가에서 그 판이 빠졌다고 판단했습니다. 이는 연결부의 용량과 동시 하중을 확인해야 할 이유를 뒷받침하지만, 이 예비 검토를 실제 안전 판정으로 만들지는 않습니다. 두 교량 모두 새 육안 손상은 없고 최종 공학 평가도 없으므로, 한 곳에만 평가 예산을 쓸 수 있다면 용량을 모르는 커낼을 먼저 평가하고, 평가 전에는 어느 곳에도 적재하지 않는 편이 타당합니다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 리버 스트리트의 합계 하중 110이 추정 용량 100을 넘는다는 계산을 제시하고 이를 근거로 즉시 평가 대상을 선택한다. | 충족 | 충족 |
| 커낼 스트리트의 하중은 95이지만 용량을 몰라 안전 여유를 판단할 수 없다고 밝힌다. 육안 검사만으로 적재를 허용하지 않는다. | 충족 | 충족 |
| 두 곳의 자재 적재 여부를 구체적으로 정하고 NTSB의 연결판·복합 하중 결과와 연결하되, 교육용 수치로 실재 교량의 안전성을 단정하지 않는다. | 충족 | 충족 |

**블라인드 검토** (Y = 미적용, X = 스킬 적용). 두 답 모두 리버의 하중 110과 용량 100, 커낼의 하중 95와 용량 미상을 밝히고 두 곳의 적재를 보류합니다. X의 우선순위는 용량을 모르는 커낼이고 Y의 우선순위는 추정 용량을 넘긴 리버입니다. 조건을 근거로 다른 우선순위를 설명하는 것도 기준상 허용되지만, 두 제안이 같은 결정은 아닙니다. Y는 아직 주어지지 않은 후속 예산도 언급합니다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `e75c268d420b` / `f21acaaff574` / `f78edf440a2a`.

</details>

## answer-with-html

**화성의 통신 지연이 1분 늘면 지구는 얼마나 더 기다릴까?**

[English](EXAMPLES.md#answer-with-html)

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

## aristotle-syllogism

**삭(새달)에 두 원반의 중심이 겹치면 반드시 개기일식일까?**

[English](EXAMPLES.md#aristotle-syllogism)

2026-11-08 · `aristotle-syllogism` 0.1.2 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [NASA, Why Do Eclipses Happen?](https://science.nasa.gov/eclipses/geometry/)
- [NASA, 2023 Annular Eclipse FAQ](https://science.nasa.gov/eclipses/future-eclipses/eclipse-2023/faq/)

NASA 자료에서 2023년 10월 14일의 금환일식과 개기·금환일식의 기하학적 차이를 확인할 수 있습니다. 그림에 주어진 각지름은 그날의 실측치가 아닙니다.

### 질문

> 천체투영관의 관람객이 이렇게 추론합니다. “개기일식은 항상 삭(새달)일 때 일어난다. 지금 삭이므로 개기일식이다.” 또 “삭이 아니라면 개기일식일 수 없다”고 말합니다. 두 추론이 각각 타당한지 판단해 주세요. 별도의 설명용 그림에서는 관측자에게 보이는 태양과 달 원반의 중심이 정확히 겹칩니다. 태양의 각지름은 0.53°, 달의 각지름은 0.50°입니다. 한쪽 가장자리에 남는 고리의 각폭과 그때 보이는 현상을 구해 주세요. 같은 그림에서 달의 각지름만 0.55°가 되면 무엇이 달라질까요? 2023년 10월 14일 실제 금환일식을 근거로 추론을 점검하되 그림의 가상 수치를 그날의 관측값으로 쓰지 마세요. 도표 옆에서 읽을 간결한 한국어 설명으로 답해 주세요.

### 스킬 미적용 답안

> 개기일식은 삭일 때 일어나므로 “개기일식이면 삭이다”는 맞습니다. 하지만 삭이라고 해서 매번 개기일식이 일어나는 것은 아닙니다. 달의 그림자가 지구에 닿도록 태양·달·지구가 충분히 일직선에 가까워야 합니다. 따라서 “지금 삭이므로 개기일식이다”는 타당하지 않고, “삭이 아니라면 개기일식일 수 없다”는 타당합니다.
>
> **그림의 가상 수치:** 중심이 정확히 겹치고 태양의 각지름이 0.53°, 달이 0.50°라면 태양이 달보다 0.03° 더 큽니다. 중심에서 한쪽 가장자리까지 남는 고리의 각폭은 그 차이의 절반인 **0.015°**입니다. 태양 가장자리가 고리처럼 남아 보이는 **금환일식**입니다. 달의 각지름이 0.55°라면 달이 태양보다 커져 태양 원반을 완전히 가리므로 **개기일식**이 됩니다.
>
> **실제 사례:** 2023년 10월 14일에는 삭 무렵 금환일식이 일어났습니다. 이는 삭만으로 개기일식이 보장되지는 않는다는 점을 보여 줍니다. 위 그림의 각지름은 설명용 가상 수치이며, 그날의 관측값이 아닙니다.

### 스킬 적용 답안 · standard

> **추론 점검**
>
> - “개기일식은 항상 삭일 때 일어난다”와 “지금 삭이다”만으로는 “지금 개기일식이다”가 따라오지 않습니다. 삭은 태양과 달이 같은 방향에 놓이는 위상 조건이지, 관측자에게 달이 태양 원반을 완전히 가린다는 뜻은 아닙니다. 주어진 문장만으로는 추론이 **타당하지 않습니다**.
> - “삭이 아니라면 개기일식일 수 없다”는 첫 문장의 대우입니다. 삭이 개기일식의 필요조건이라는 뜻이므로, 그 전제가 참이라면 이 추론은 **타당합니다**. 다만 전제의 사실 여부는 논리적 타당성과 별도로 확인해야 합니다.
>
> **그림의 가상 수치**
>
> 두 원반의 중심이 겹치고 태양 지름이 달보다 크므로, 한쪽 가장자리에 남는 고리의 각폭은 지름 차이의 절반입니다.
>
>
> $$
> (0.53^\circ-0.50^\circ)/2=0.015^\circ
> $$
>
>
> 양쪽 가장자리의 폭은 각각 **0.015°**입니다. 태양 원반이 달 둘레로 드러나는 **금환일식**을 나타냅니다.
>
> 달의 각지름이 **0.55°**라면 태양보다 크므로 태양 원반을 완전히 덮습니다. 중심이 정확히 겹친다는 가정 아래 태양 가장자리에 고리는 남지 않고 **개기일식**이 됩니다.
>
> **실제 사례와 비교**
>
> 2023년 10월 14일 금환일식은 삭만으로 개기일식이 결론 나지 않음을 보여 줍니다. 달이 삭에 있어도 태양을 완전히 가리지 못하면 금환일식이 일어납니다. 이 실제 사례는 두 번째 추론의 방향, 즉 개기일식이라면 삭이어야 한다는 주장과도 모순되지 않습니다. 위의 각폭 계산은 설명용 가상 수치에만 적용한 것이며, 그날의 관측값을 뜻하지 않습니다.

<details>
<summary>원래 수식 표기로 보기</summary>

````text
**추론 점검**

- “개기일식은 항상 삭일 때 일어난다”와 “지금 삭이다”만으로는 “지금 개기일식이다”가 따라오지 않습니다. 삭은 태양과 달이 같은 방향에 놓이는 위상 조건이지, 관측자에게 달이 태양 원반을 완전히 가린다는 뜻은 아닙니다. 주어진 문장만으로는 추론이 **타당하지 않습니다**.
- “삭이 아니라면 개기일식일 수 없다”는 첫 문장의 대우입니다. 삭이 개기일식의 필요조건이라는 뜻이므로, 그 전제가 참이라면 이 추론은 **타당합니다**. 다만 전제의 사실 여부는 논리적 타당성과 별도로 확인해야 합니다.

**그림의 가상 수치**

두 원반의 중심이 겹치고 태양 지름이 달보다 크므로, 한쪽 가장자리에 남는 고리의 각폭은 지름 차이의 절반입니다.

\[
(0.53^\circ-0.50^\circ)/2=0.015^\circ
\]

양쪽 가장자리의 폭은 각각 **0.015°**입니다. 태양 원반이 달 둘레로 드러나는 **금환일식**을 나타냅니다.

달의 각지름이 **0.55°**라면 태양보다 크므로 태양 원반을 완전히 덮습니다. 중심이 정확히 겹친다는 가정 아래 태양 가장자리에 고리는 남지 않고 **개기일식**이 됩니다.

**실제 사례와 비교**

2023년 10월 14일 금환일식은 삭만으로 개기일식이 결론 나지 않음을 보여 줍니다. 달이 삭에 있어도 태양을 완전히 가리지 못하면 금환일식이 일어납니다. 이 실제 사례는 두 번째 추론의 방향, 즉 개기일식이라면 삭이어야 한다는 주장과도 모순되지 않습니다. 위의 각폭 계산은 설명용 가상 수치에만 적용한 것이며, 그날의 관측값을 뜻하지 않습니다.
````

</details>

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 삭은 필요조건이지만 충분조건이 아님을 설명해 첫 번째 역명제를 배척하고, 삭이 아니면 개기일식일 수 없다는 대우를 받아들인다. | 충족 | 충족 |
| 한쪽 고리의 각폭을 (0.53−0.50)/2 = 0.015°로 구한다. 중심이 같고 달이 0.55°면 그 관측자에게 태양 원반이 완전히 가려짐을 설명한다. | 미충족 | 충족 |
| 2023년 10월 14일 금환일식을 실제 반례로 들고 설명용 그림의 각지름을 역사적 관측값으로 돌리지 않는다. | 충족 | 충족 |

**블라인드 검토** (Y = 미적용, X = 스킬 적용). X와 Y 모두 삭만으로는 개기일식을 결론 낼 수 없고 대우는 타당하다고 판단하며, 2023년 금환일식을 가상 각지름과 구별한다. X는 0.015°가 한쪽에 드러난 고리 폭임을 정확히 설명한다. Y는 수치는 맞지만 ‘중심에서 한쪽 가장자리까지’라고 해 측정 구간을 잘못 설명한다. 태양 중심에서 가장자리까지는 0.265°이고 0.015°는 달 가장자리와 태양 가장자리 사이의 차이다. 두 답 모두 중심이 겹친 0.55° 달이 태양 원반을 완전히 가린다고 설명한다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `d69f028ec500` / `15076d2660f0` / `38636190c91c`.

</details>

## asd-ste100

**라즈베리 파이 4 복구 작업대별로 언제 전원을 끌 수 있을까?**

[English](EXAMPLES.md#asd-ste100)

2026-11-08 · `asd-ste100` 0.1.3 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [Raspberry Pi, Raspberry Pi computer hardware documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#reflash-the-bootloader)

Raspberry Pi 문서에서 HDMI가 연결된 보드의 복구 완료 표시와 전원 분리 순서를 확인할 수 있습니다. 작업대별 표시 시각과 관측 간격은 연습용입니다.

**언어 적용 범위.** 한국어 답은 조건과 작업 순서, 용어의 일관성을 다루는 구조적 응용입니다. 영어 문법·단어 수·승인 어휘를 한국어에 적용하거나 공식 ASD-STE100 준수를 판정하지 않습니다.

### 질문

> HDMI 화면이 연결된 Raspberry Pi 4 Model B의 부트로더 복구 마무리 절차를 기술자에게 인계할 한국어 메모를 간결하게 써 주세요. 전원을 분리하려면 녹색 활동 LED가 일정하게 깜박이는 상태와 HDMI 화면이 녹색으로 표시되는 상태를 모두 확인해야 합니다. 복구용 microSD 카드는 전원을 분리한 다음에만 뺍니다. 이 가상 훈련에서는 각 작업대를 0초, 15초, 30초, 45초, 60초에 점검합니다. 한번 나타난 신호는 유지됩니다. North에서는 16초에 LED가 해당 패턴으로 깜박이기 시작하고 29초에 화면이 녹색이 됩니다. South에서는 33초에 화면이 녹색이 되고 41초에 LED가 해당 패턴으로 깜박이기 시작합니다. East에서는 21초에 LED가 해당 패턴으로 깜박이기 시작하지만 60초에도 화면이 녹색이 아닙니다. 아직 어느 작업대에서도 전원을 분리하지 않았습니다. 각 작업대에서 두 신호를 처음 확인할 수 있는 점검 시각과 그때 취할 안전한 조치를 알려 주세요. 경과 시간만으로 카드를 빼도 되는지도 설명하고, 카드 이름은 ‘복구용 microSD 카드’로 통일해 주세요.

### 스킬 미적용 답안

> 기술자 인계 메모
>
> - **North:** 두 신호를 처음 함께 확인하는 시각은 **30초**입니다. 녹색 활동 LED의 일정한 깜박임과 HDMI 화면의 녹색 표시를 모두 확인한 뒤 전원을 분리하세요. 전원이 분리된 다음에만 **복구용 microSD 카드**를 빼세요.
> - **South:** 두 신호를 처음 함께 확인하는 시각은 **45초**입니다. 두 신호를 확인한 뒤 전원을 분리하고, 전원 분리 후 **복구용 microSD 카드**를 빼세요.
> - **East:** **60초까지 두 신호를 함께 확인할 수 없습니다.** 화면이 녹색으로 표시될 때까지 전원을 분리하거나 **복구용 microSD 카드**를 빼지 마세요.
>
> 경과 시간만으로는 안전하게 전원을 분리하거나 카드를 뺄 수 없습니다. 전원 분리는 두 신호를 모두 확인한 뒤에만 하고, 카드는 전원이 분리된 다음에만 빼세요.

### 스킬 적용 답안 · standard

> ## 기술자 인계 메모
>
> | 작업대 | 두 신호를 처음 확인할 수 있는 점검 시각 | 안전한 조치 |
> |---|---:|---|
> | North | 30초 | 녹색 활동 LED가 일정하게 깜박이고 HDMI 화면이 녹색인 것을 확인했습니다. 전원을 분리한 다음 복구용 microSD 카드를 뺍니다. |
> | South | 45초 | 두 신호를 모두 확인했습니다. 전원을 분리한 다음 복구용 microSD 카드를 뺍니다. |
> | East | 확인 불가 | 60초에도 HDMI 화면이 녹색이 아닙니다. 전원을 분리하거나 복구용 microSD 카드를 빼지 말고, 두 신호가 모두 확인될 때까지 기다립니다. |
>
> 경과 시간만으로 복구용 microSD 카드를 빼면 안 됩니다. 카드를 빼기 전에 두 신호를 모두 확인하고, 먼저 전원을 분리해야 합니다.
>
> *구조 적응: 한국어 문장 길이나 사전 규칙은 적용하지 않고, 용어를 통일하고 조건과 조치를 명확히 했습니다.*

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 신호가 실제로 나타난 순간과 점검 시각을 구분해, North의 첫 적격 점검은 30초, South는 45초라고 판단한다. | 충족 | 충족 |
| East는 60초에도 전원을 분리하거나 카드를 빼지 않는다. 경과 시간만으로 성공이나 하드웨어 고장을 단정하지 않는다. | 충족 | 충족 |
| 기술자가 따를 순서인 두 신호 확인 → 전원 분리 → 복구용 microSD 카드 제거를 지키고 카드 이름을 일관되게 쓴다. | 미충족 | 미충족 |

**블라인드 검토** (X = 미적용, Y = 스킬 적용). 두 답 모두 North는 30초, South는 45초로 판단하고, East는 60초에도 전원을 분리하거나 카드를 빼지 않도록 합니다. 각 작업대의 조치에는 ‘복구용 microSD 카드’를 쓰지만 끝부분에서는 둘 다 ‘카드’로 줄여 일관된 명칭이라는 기준을 온전히 충족하지 못했습니다. X 쪽은 목록으로, Y 쪽은 표로 정리하고 한국어 적용 범위도 덧붙입니다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `6600af844428` / `0dd8cfece084` / `521d854c379c`.

</details>

## boring-professor

**같은 경로를 쓴 두 Linux 로그 파일의 디스크 공간**

[English](EXAMPLES.md#boring-professor)

2026-11-08 · `boring-professor` 0.1.2 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [Linux man-pages 6.19, unlink(2)](https://man7.org/linux/man-pages/man2/unlink.2.html)

Linux의 unlink(2) 문서는 이름을 삭제해도 마지막 파일 디스크립터가 열린 동안 파일이 유지되는 이유를 설명합니다. 파일 이름과 용량, 시간은 가상의 장애 훈련에 쓰는 값입니다.

### 질문

> 다음 Linux 실습을 시스템 수업을 듣는 학생에게 비유 없이 한국어로 간결하게 설명하세요. 09:00에 관리자가 /var/log/payments.log의 마지막 하드 링크를 삭제합니다. 기존 파일에 할당된 데이터는 20 MiB이고 기록 프로세스와 모니터 프로세스가 각자 파일 디스크립터 하나를 열어 둔 상태입니다. 09:02에 서비스는 같은 경로에 별도 파일을 만들고 5 MiB를 할당합니다. 09:03에 기록 프로세스는 원래 디스크립터로 8 MiB를 덧붙이고 09:04에 그 디스크립터를 닫습니다. 모니터는 09:06에 기존 디스크립터를 닫습니다. 어느 파일에 8 MiB가 추가되는지, 09:04 직후와 09:06 직후 두 파일에 할당된 데이터가 각각 합계 몇 MiB인지, 경로 이름만 보고 판단할 수 없는 이유를 설명하세요. 희소 할당이나 중복 할당, 그 밖의 변화는 없고 메타데이터 크기는 제외합니다.

### 스킬 미적용 답안

> 8 MiB는 삭제 전 파일을 가리키는 기록 프로세스의 기존 디스크립터를 통해 기록되므로, 새 파일이 아니라 **기존 파일**에 추가됩니다. 하드 링크가 삭제돼 경로에서 사라져도, 열린 디스크립터가 남아 있으면 기존 파일은 계속 접근할 수 있습니다.
>
> - **09:04 직후:** 기존 파일은 디스크립터를 연 모니터가 남아 있으므로 20 + 8 = **28 MiB**가 할당되어 있습니다. 새 파일은 **5 MiB**입니다.
> - **09:06 직후:** 모니터도 디스크립터를 닫아 기존 파일에 대한 참조가 없어지면 기존 파일의 할당 데이터는 회수됩니다. 새 파일은 계속 **5 MiB**입니다.
>
> `/var/log/payments.log`라는 경로는 현재 새 파일을 가리킵니다. 기존 파일은 그 경로에서 분리된 뒤에도 열린 디스크립터로 참조되므로, 경로 이름만으로는 두 파일의 정체나 할당량을 모두 판단할 수 없습니다.

### 스킬 적용 답안 · standard

> 하드 링크는 파일을 가리키는 디렉터리 항목입니다. 파일 디스크립터는 프로세스가 이미 연 파일 객체를 참조합니다. 따라서 경로 이름이 삭제되어도 열린 디스크립터가 남아 있으면 기존 파일 객체에 계속 접근할 수 있습니다. 마지막 하드 링크와 마지막 열린 디스크립터가 모두 사라질 때 기존 파일의 할당 데이터가 해제됩니다.
>
> 09:00에 경로의 마지막 하드 링크가 삭제됐지만 두 프로세스의 디스크립터는 기존 파일 객체를 계속 가리킵니다. 09:02에 같은 경로로 만든 파일은 별도 파일 객체입니다. 그러므로 09:03에 기록 프로세스가 덧붙인 8 MiB는 새 파일이 아니라 기존 파일에 추가됩니다.
>
> - **09:04 직후:** 기존 파일은 20 + 8 = **28 MiB**, 새 파일은 **5 MiB**입니다. 합계는 **33 MiB**입니다.
> - **09:06 직후:** 모니터가 기존 파일의 마지막 디스크립터를 닫으므로 기존 파일의 할당 데이터는 해제됩니다. 새 파일은 **5 MiB**이며, 두 파일에 남아 있는 할당 데이터의 합계도 **5 MiB**입니다.
>
> 경로 이름은 디렉터리 항목이 가리키는 파일 객체를 식별하지만, 이미 열린 디스크립터가 가리키는 객체까지 보여 주지는 않습니다. 따라서 같은 경로에 새 파일을 만들었다는 사실만으로 기존 디스크립터가 새 파일을 가리킨다고 판단할 수 없습니다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 추가 쓰기는 같은 경로의 새 파일(5 MiB)이 아니라 기존 디스크립터가 가리키는 링크 없는 파일에 반영된다고 밝힌다. | 충족 | 충족 |
| 09:04 직후 합계 33 MiB(기존 28, 새 파일 5), 09:06 직후 합계 5 MiB를 명시하고 모니터의 디스크립터가 기존 공간 반환을 지연시켰다고 설명한다. | 미충족 | 충족 |
| 경로와 파일 객체의 차이, 마지막 디스크립터가 닫혀야 공간을 다시 쓸 수 있다는 조건을 설명하며 unlink가 기존 디스크립터의 쓰기를 막는다고 하지 않는다. | 충족 | 충족 |

**블라인드 검토** (Y = 미적용, X = 스킬 적용). 두 답 모두 8 MiB가 기존 파일에 추가되고 모니터가 마지막 디스크립터를 닫아야 그 공간을 회수할 수 있다고 설명한다. X 쪽은 09:04의 합계 33 MiB와 09:06의 합계 5 MiB를 모두 명시한다. Y 쪽은 09:04의 구성값 28 MiB와 5 MiB는 구했지만 요청한 합계를 독자가 직접 더해야 한다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `7920576bbe50` / `b433842f01c2` / `699659287da0`.

</details>

## diataxis

**초록색 CI 결과는 어떤 Kubernetes 배포를 확인했을까?**

[English](EXAMPLES.md#diataxis)

2026-11-08 · `diataxis` 0.1.1 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [Kubernetes command reference, kubectl rollout status](https://kubernetes.io/docs/reference/kubectl/generated/kubectl_rollout/kubectl_rollout_status/)

Kubernetes 문서는 진행 상태를 조회할 때 기본으로 추적하는 리비전과 --revision, --watch 옵션의 동작을 설명합니다. checkout-api의 배포 상황은 예제입니다.

### 질문

> 배포팀을 위한 짧은 한국어 명령 참조 항목을 써 주세요. Deployment checkout-api를 대상으로 CI가 09:00에 별도 플래그 없이 kubectl rollout status를 실행해 리비전 7을 지켜봅니다. 7이 끝나기 전에 리비전 8이 시작되고, 명령은 나중에 성공을 보고합니다. 기본 감시는 최신 롤아웃으로 넘어갑니다. --revision=N을 주면 해당 리비전을 감시하다가 새 리비전에 대체될 때 중단하고, --watch=false는 기다리지 않고 현재 상태를 읽습니다. 이 예에서는 8이 마지막 리비전입니다. CI 성공이 7과 8에 대해 무엇을 입증하고 무엇은 입증하지 않는지 밝히세요. 새 CI 작업에서 리비전 7만 감시할 명령, 운영자가 즉시 현재 상태를 조회할 명령을 각각 정확히 제시하세요. 따라 하는 튜토리얼보다 필요할 때 바로 찾을 수 있는 참조 문서가 필요합니다.

### 스킬 미적용 답안

> ### `kubectl rollout status` 명령 참조
>
> 배포 `checkout-api`의 롤아웃 상태를 확인합니다. 기본 동작은 최신 롤아웃을 감시하므로, 리비전 7을 지켜보던 CI 명령은 리비전 8이 시작되면 새 롤아웃으로 넘어갑니다. 나중에 보고된 성공은 마지막 리비전인 **8이 완료됐음**을 입증하지만, **7이 완료됐음**을 입증하지는 않습니다.
>
> - **새 CI 작업에서 리비전 7만 감시:** `kubectl rollout status deployment/checkout-api --revision=7`
>
>   리비전 7이 새 리비전으로 대체되면 감시를 중단합니다. 성공 여부를 확인하려면 명령의 종료 결과를 확인하세요.
>
> - **운영자가 현재 상태를 즉시 조회:** `kubectl rollout status deployment/checkout-api --watch=false`
>
>   기다리지 않고 현재 롤아웃 상태를 한 번 읽습니다.

### 스킬 적용 답안 · standard

> ### `kubectl rollout status` 참조
>
> 기본 감시는 진행 중인 롤아웃을 따라갑니다. 09:00에 시작한 CI 작업은 별도 플래그 없이 `deployment/checkout-api`의 리비전 7을 감시했지만, 7이 끝나기 전에 8이 시작되어 기본 감시가 최신 롤아웃인 8로 넘어갔습니다. 이후 명령의 성공은 **리비전 8의 롤아웃이 완료됐음**을 입증합니다. 리비전 7의 완료를 입증하지는 않습니다. 이 예에서는 8이 마지막 리비전입니다.
>
> 새 CI 작업에서 리비전 7만 감시하려면:
>
> ```sh
> kubectl rollout status deployment/checkout-api --revision=7
> ```
>
> `--revision=7`은 해당 리비전을 감시하며, 새 리비전으로 대체되면 감시를 중단합니다. 운영자가 기다리지 않고 현재 상태를 즉시 조회하려면:
>
> ```sh
> kubectl rollout status deployment/checkout-api --watch=false
> ```
>
> 이 명령은 현재 상태를 읽고 기다리지 않습니다. 조회 결과만으로 롤아웃 완료를 입증하지는 않습니다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 기본 감시가 마지막 리비전 8의 성공을 확인했으나 리비전 7의 성공은 입증하지 못한다고 밝힌다. | 충족 | 충족 |
| deployment/checkout-api에 --revision=7을 주는 실행 가능한 명령을 제시하고, 리비전 7이 대체되면 8을 따라가지 않고 감시가 중단된다고 설명한다. | 충족 | 충족 |
| --watch=false를 쓰는 실행 가능한 현재 상태 조회 명령을 담고, 두 명령의 목적을 간결한 참조 항목에서 쉽게 찾을 수 있다. | 충족 | 충족 |

**블라인드 검토** (Y = 미적용, X = 스킬 적용). 두 답 모두 CI 성공이 리비전 8을 확인한 것이고 리비전 7의 성공은 입증하지 않는다고 설명한다. X 쪽은 명령을 각각 코드 블록에 싣고, Y 쪽은 두 사용 목적을 강조한 목록에 명령을 나란히 배치한다. 둘 다 리비전 고정 감시가 대체 시 중단되는 조건과 즉시 조회 옵션을 정확히 안내한다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `1bf8f74acf77` / `ef4253e91603` / `4138d1891549`.

</details>

## eli5

**시간을 맞춰 보면 어느 병이 더 빨리 식었을까?**

[English](EXAMPLES.md#eli5)

2026-11-08 · `eli5` 0.1.2 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [Monterey Bay Aquarium, Life of a rescued sea otter](https://www.montereybayaquarium.org/about-us/stories/life-of-a-rescued-sea-otter)
- [Monterey Bay Aquarium, Sea otter](https://www.montereybayaquarium.org/animals-the-ocean/animals-a-to-z/sea-otter)

몬터레이 베이 수족관은 새끼 해달 696의 구조·털 손질과 털 속 공기가 보온·부력에 하는 역할을 설명합니다. 병의 냉각 수치는 별도의 가상 실험값입니다.

### 질문

> 몬터레이 베이 아쿠아리움에서 다섯 살 아이가 구조된 아기 해달 696의 털을 왜 돌봐 주었는지 궁금해합니다. 이 질문을 위해 만든 교실 실험에서는 똑같이 따뜻한 병 두 개에 같은 재질의 모형 털옷을 입혀 같은 찬물에 넣었습니다. 공기가 들어 있는 보송한 털옷을 입힌 병은 20분에 4도 식었습니다. 젖어서 납작해진 털옷을 입힌 병은 10분에 3도 식었습니다. 아이는 4가 3보다 크니 보송한 병에서 온기가 더 빨리 빠져나갔다고 말합니다. 병이 물에 뜨는지는 실험하지 않았습니다. 실제 해달은 두꺼운 지방층이 없고, 손질한 털 사이에 갇힌 공기 덕분에 따뜻함을 유지하고 물에도 잘 뜹니다. 아이에게 들려줄 한국어 답을 짧은 다섯 문장 이내로 써 주세요. 같은 기준으로 두 병을 비교하고, 공기가 열을 만들어 내는지, 물에 뜨는 것에 대해서는 병 실험으로 무엇까지 알 수 있는지 설명해 주세요.

### 스킬 미적용 답안

> 같은 기준으로 보면, 보송한 털옷을 입힌 병은 20분 동안 4도 식었고 젖은 털옷을 입힌 병은 10분 동안 3도 식었어요. 식은 정도만 보면 4도가 더 크지만, 시간까지 맞춰 비교하면 보송한 병은 10분에 2도씩 식어 젖은 병보다 온기가 천천히 빠져나갔어요. 털 사이의 공기는 열을 만들지는 않고, 온기가 빠져나가는 것을 늦춰 줘요. 실제 해달은 이 공기 덕분에 따뜻함을 지켜요. 병 실험은 물에 잘 뜨는지는 알려 주지 않아요.

### 스킬 적용 답안 · standard

> 해달이 털을 돌보는 건 털 사이에 공기를 가둬 따뜻하게 지내기 위해서야. 실험에서 보송한 털옷을 입은 병은 20분에 4도 식고, 젖은 털옷을 입은 병은 20분에 6도 식었어. 그래서 같은 20분 동안 보송한 병에서 온기가 더 천천히 빠져나갔어. 공기는 따뜻함을 만들지는 않고, 온기가 빠져나가는 걸 늦춰 줘. 해달 털의 공기는 물에 뜨는 데도 도움이 되지만, 이 병 실험은 병이 뜨는지는 알려 주지 않아.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 같은 시간으로 환산해 10분당 평균 2도와 3도(또는 동등한 식는 속도)를 비교하고, 보송한 털옷을 입힌 쪽이 평균적으로 더 천천히 식었다고 설명한다. | 충족 | 미충족 |
| 털 손질로 갇힌 공기가 온기가 빠져나가는 속도를 늦춘다고 설명한다. 공기가 열을 만든다고 하거나 근거 없는 원리를 도입하지 않는다. | 충족 | 충족 |
| 아이에게 들려줄 짧은 다섯 문장 이내에서, 병이 뜨는지는 시험하지 않았다는 점과 실제 해달은 갇힌 공기의 도움으로 뜬다는 사실을 구분한다. | 미충족 | 충족 |

**블라인드 검토** (Y = 미적용, X = 스킬 적용). X 쪽은 젖은 병이 20분에 6도 식었다고 쓰지만, 실제로 주어진 것은 10분에 3도라는 관찰입니다. 같은 속도가 유지된다는 가정 없이 그 수치를 20분의 관찰값으로 바꿀 수 없습니다. Y 쪽은 같은 10분 기준에서 2도와 3도를 비교하지만, 병의 부력은 시험하지 않았다는 점만 말하고 갇힌 공기가 실제 해달이 뜨는 데 도움이 된다는 사실은 빼먹습니다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `10536a49c052` / `358d2614595e` / `f85bcafcc28c`.

</details>

## federal-plain-language

**부모와 아이의 신원을 45분 안에 어떻게 증명할 수 있나요?**

[English](EXAMPLES.md#federal-plain-language)

2026-11-08 · `federal-plain-language` 0.1.2 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [SSA, U.S. Citizen/Child — Replacement Social Security Card (October 2026)](https://www.ssa.gov/pubs/EN-05-10514.pdf)

미국 사회보장국의 2026년 10월 안내문은 부모·자녀 각각의 신원 증빙 및 발급기관 인증 사본 요건을 설명합니다. 이 가족의 서류 수집 시간은 가정한 값입니다.

**언어 적용 범위.** 한국어에서는 독자의 질문, 절차, 서류의 조건을 명확히 하는 구조만 적용합니다. 연방 지침에 따른 한국어 문법 검증을 뜻하지 않습니다.

### 질문

> 미국 시민권자인 자녀의 사회보장카드 재발급 신청을 준비하는 부모에게 한국어로 짧은 안내문을 써 주세요. 질문은 2026년 10월 미국 사회보장국(SSA) 안내문에 따른 신원 증빙에만 관한 것이고, 서류를 모을 수 있는 시간은 45분입니다. 아이와 부모 모두 신원 증빙이 필요합니다. 아이는 유효한 미국 여권이나 주 정부가 발급한 유효한 비운전자 신분증, 부모는 유효한 미국 여권이나 운전면허증을 쓸 수 있습니다. 원본 또는 발급기관이 인증한 사본은 인정되지만, 공증받은 복사본은 인정되지 않습니다. 출생증명서는 나이나 시민권을 증명할 수 있지만 신원 증빙은 아닙니다. 다음 소요 시간은 가정값이며 합산합니다. 아이의 출생증명서 원본은 이미 있고, 여권 원본은 40분, 비운전자 신분증의 발급기관 인증 사본은 15분 걸립니다. 부모의 여권 공증 복사본은 5분, 여권의 발급기관 인증 사본은 25분, 운전면허증 원본은 35분입니다. 어떤 조합을 가져가야 하나요? 손쉬워 보이는 조합이 안 되는 이유까지 다섯 문장 이내로 설명해 주세요.

### 스킬 미적용 답안

> 45분 안에 준비하려면 **아이의 주 정부 발급 유효한 비운전자 신분증의 발급기관 인증 사본(15분)**과 **부모의 유효한 미국 운전면허증 원본(35분)**을 가져가세요. 총 50분이므로, 주어진 시간 안에 두 사람의 신원 증빙을 모두 마련할 수 있는 조합은 없습니다. 아이의 여권 원본과 부모의 운전면허증 원본 조합도 75분이 걸립니다. 부모 여권 공증 복사본은 인정되지 않고, 아이의 출생증명서는 나이나 시민권을 증명할 수 있어도 신원 증빙을 대신하지 못합니다.

### 스킬 적용 답안 · standard

> 아이 신원 증빙으로 유효한 미국 여권 원본(40분)을, 부모 신원 증빙으로 운전면허증 원본(35분)을 준비하세요. 두 서류 모두 인정되는 원본이며, 합계 75분이 필요해 45분 안에 준비할 수는 없습니다. 아이의 비운전자 신분증 발급기관 인증 사본(15분)과 부모의 운전면허증 원본(35분)을 조합해도 합계 50분입니다. 부모 여권의 공증 복사본은 인정되지 않고, 발급기관 인증 사본은 인정되지만 25분이 걸립니다. 아이의 출생증명서는 나이나 시민권을 증명할 수 있어도 신원 증빙은 아니므로, 주어진 시간과 서류만으로는 두 사람의 신원 증빙을 모두 준비할 수 없습니다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 아이의 비운전자 신분증 발급기관 인증 사본과 부모의 여권 발급기관 인증 사본을 골라 총 40분이므로 45분 안에 가능하다고 밝힌다. | 미충족 | 미충족 |
| 출생증명서 원본으로는 아이의 신원을 증명할 수 없고, 공증받은 여권 복사본으로는 부모의 신원을 증명할 수 없다는 두 이유를 구분한다. | 충족 | 충족 |
| 부모가 바로 실행할 수 있는 한국어 신원 증빙 안내를 다섯 문장 이내로 쓰고, 이 조합으로 전체 신청이 완료된다고 단정하지 않는다. | 미충족 | 미충족 |

**블라인드 검토** (Y = 미적용, X = 스킬 적용). 두 답 모두 출생증명서와 공증 복사본이 왜 안 되는지는 정확히 설명합니다. 하지만 15분짜리 아이 신분증과 25분짜리 부모 여권 인증 사본을 조합하면 40분인데도 가능한 조합이 없다고 결론 내립니다. X는 75분, Y는 50분이 걸리는 경로를 첫 문장에 권합니다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `5ba332f74f16` / `50ea09db03d5` / `2e32db00c4d7`.

</details>

## feynman-technique

**DNS 응답이 리졸버마다 달라지는 이유**

[English](EXAMPLES.md#feynman-technique)

2026-11-08 · `feynman-technique` 0.1.3 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [IETF RFC 2308, Negative Caching of DNS Queries](https://www.rfc-editor.org/rfc/rfc2308.html#section-5)

RFC 2308은 DNS 음성 응답의 캐시 수명과 만료를 설명합니다. 호스트 이름, 두 리졸버의 조회 시각과 TTL 값은 이 계산을 위한 예시입니다.

### 질문

> 두 팀은 서로 다른 DNS 리졸버를 통해 uploads.example.org를 조회합니다. 다음은 가상의 장애 기록입니다. Harbor는 12:00에, Hill은 12:03에 NXDOMAIN 응답을 받아 이름이 없다는 결과를 캐시했습니다. 이 영역의 SOA TTL은 900초이고 MINIMUM은 300초입니다. RFC 2308에 따라 음성 응답에는 둘 중 작은 값을 씁니다. 운영자는 12:04에 A 레코드를 만들었고 두 팀은 12:06에 다시 조회합니다. 신입 개발자를 위한 짧은 한국어 장애 설명을 써 주세요. 두 팀이 각각 무엇을 받을 수 있는지, 더 늦게 저장된 캐시는 언제 만료되는지, Hill이 12:04 전에 조회하지 않았다면 결과가 어떻게 달라질지 설명하세요. 권한 서버에는 새 주소가 반영됐고 연결할 수 있습니다. 조기 삭제나 갱신, 로컬 재정의는 없습니다. 독자에게 다시 질문하지 마세요.

### 스킬 미적용 답안

> **장애 설명**
>
> RFC 2308에 따라 음성 응답의 캐시 시간은 SOA TTL 900초와 MINIMUM 300초 중 작은 값인 **300초(5분)**입니다.
>
> Harbor는 12:00에 NXDOMAIN을 받아 12:05에 캐시가 만료됩니다. 따라서 12:06 조회는 캐시를 다시 사용하지 않고, 권한 서버에서 새 A 레코드를 확인해 **새 주소를 받을 수 있습니다**.
>
> Hill은 12:03에 NXDOMAIN을 받아 12:08에 만료됩니다. 그러므로 12:06에는 아직 유효한 음성 캐시가 남아 있어 **계속 NXDOMAIN을 받을 수 있습니다**. 두 팀의 결과가 다른 이유는 각 리졸버가 별도로 캐시하고 만료 시점도 다르기 때문입니다.
>
> Hill이 12:04 전에 조회한 적이 없어 NXDOMAIN을 저장하지 않았다면, 12:06 조회 때 권한 서버에서 새 A 레코드를 받아 **새 주소를 받을 수 있습니다**.

### 스킬 적용 답안 · standard

> 유효한 음성 캐시 시간은 SOA TTL 900초와 MINIMUM 300초 중 작은 값인 **300초**입니다. Harbor는 12:00에 NXDOMAIN을 캐시했으므로 12:05에 만료됩니다. Hill은 12:03에 저장했으므로 12:06 조회 시점에는 아직 캐시가 유효해, 두 팀 모두 그때까지 조회한 적이 있다면 NXDOMAIN을 받을 수 있습니다. 권한 서버에 A 레코드가 생겼어도 각 리졸버의 음성 캐시는 만료 전까지 남습니다.
>
> Hill이 12:04 전에 조회한 적이 없다면 저장된 NXDOMAIN이 없습니다. 따라서 12:06 조회는 권한 서버의 새 A 레코드를 확인해 주소를 받을 수 있습니다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 음성 캐시 수명 300초와 Harbor의 12:05, Hill의 12:08 만료를 각 리졸버의 최초 조회 시각에서 구한다. | 충족 | 미충족 |
| 12:06에 Harbor는 새 주소를 조회할 수 있고 Hill은 NXDOMAIN을 줄 수 있다고 설명한다. 레코드 생성이 Hill의 캐시를 지우거나 수명을 다시 시작한 것으로 쓰지 않는다. | 충족 | 미충족 |
| Hill에 이전 음성 항목이 없었다면 12:06에 새 주소를 조회할 수 있는 이유를 신입 개발자가 이해할 수 있게 설명하며, 모든 리졸버가 동시에 바뀐다고 하지 않는다. | 충족 | 충족 |

**블라인드 검토** (X = 미적용, Y = 스킬 적용). 두 답 모두 음성 캐시 수명을 300초로 계산하고, Hill이 먼저 조회하지 않았다면 새 주소를 받을 수 있다고 설명한다. X 쪽은 Harbor의 12:05와 Hill의 12:08 만료를 비교해 12:06에 Hill만 캐시된 NXDOMAIN을 줄 수 있다고 짚는다. Y 쪽은 Hill의 만료 시각을 명시하지 않고 두 팀 모두 이전 음성 응답을 받을 수 있다고 잘못 말한다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `9249d0cc1aa8` / `90b434c4a7c3` / `54201b2c506a`.

</details>

## google-design-doc

**주문을 받는 동안 인덱스 생성을 승인할 수 있을까?**

[English](EXAMPLES.md#google-design-doc)

2026-11-08 · `google-design-doc` 0.1.2 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [PostgreSQL 17 documentation, CREATE INDEX](https://www.postgresql.org/docs/17/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY)
- [PostgreSQL 17 system catalogs, pg_index](https://www.postgresql.org/docs/17/catalog-pg-index.html)

PostgreSQL 17 문서는 일반 인덱스와 동시 인덱스 생성의 잠금·대기 동작, 실패한 인덱스의 상태를 설명합니다. 상점의 지연 시간 측정값과 배포 기준은 가정입니다.

### 질문

> PostgreSQL 17을 쓰는 가상의 쇼핑몰에 대해 한국어 설계 검토 문단을 써 주세요. 인덱스를 만드는 내내 주문 INSERT를 막는 방식은 쓸 수 없습니다. 이와 별개로, 운영 반영 전에 리허설의 p95 쓰기 지연 시간이 기준값 40 ms보다 20% 넘게 늘어나지 않아야 합니다. 동시 인덱스 생성 리허설에서는 51 ms를 측정했습니다. 일반 CREATE INDEX는 쓰기를 막습니다. CREATE INDEX CONCURRENTLY는 쓰기를 허용하지만 테이블을 두 번 스캔하고 트랜잭션을 기다릴 수 있습니다. 실패하면 플래너는 사용하지 않지만 쓰기 때는 계속 갱신되는 무효 인덱스가 남을 수 있습니다. 이번 근무 시간에 무엇을 승인할지, 재시도하기 전에 무엇을 측정할지, 무효 인덱스는 어떻게 처리할지 간결하게 권고하세요. 운영 환경의 성능은 측정하지 않았습니다.

### 스킬 미적용 답안

> 이번 근무 시간에는 인덱스 생성을 승인하지 마세요. `CREATE INDEX`는 주문 쓰기를 막으므로 운영 제약에 맞지 않고, `CREATE INDEX CONCURRENTLY` 리허설은 51 ms로 기준 40 ms보다 27.5% 높아 허용 한도인 48 ms를 넘었습니다. 다만 운영 성능은 측정하지 않았으므로, 이 결과만으로 운영 영향까지 단정할 수는 없습니다.
>
> 재시도 전에는 리허설에서 쓰기 부하와 트랜잭션 대기 조건을 점검하고, 동시 생성 중 p95 쓰기 지연 시간과 완료 여부를 다시 측정하세요. 실패 시에는 무효 인덱스가 남았는지 확인하고, 남아 있으면 플래너가 쓰지 않는다는 점만 믿고 방치하지 말고 제거한 뒤 원인을 해결하고 재시도하세요.

### 스킬 적용 답안 · standard

> ### 설계 검토 권고
>
> **이번 근무 시간에는 운영 반영을 승인하지 않습니다.** 주문 INSERT를 인덱스 생성 내내 막을 수 없으므로 일반 `CREATE INDEX`는 제약을 위반합니다. `CREATE INDEX CONCURRENTLY`는 쓰기를 허용해 이 제약은 충족하지만, 운영 반영 전 리허설의 p95 쓰기 지연 시간이 기준값 40 ms보다 20% 넘게 늘지 않아야 한다는 조건에는 미달했습니다. 허용 상한은 48 ms인데 리허설에서 51 ms를 측정했습니다. 운영 성능도 아직 측정되지 않았습니다.
>
> 재시도 전에는 같은 기준값과 작업 부하를 사용해 리허설을 반복하고 p95 쓰기 지연을 측정합니다. **48 ms 이하**가 확인되면 운영 반영을 다시 검토합니다. 동시 생성이 실패하면 남은 무효 인덱스는 플래너가 사용하지 않더라도 쓰기 때 계속 갱신될 수 있으므로, 재시도 전에 해당 인덱스를 제거하고 제거 여부를 확인합니다. 이 권고는 제안이며, 승인된 결정은 없습니다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 허용 한도 48 ms 또는 증가율 27.5%를 구하고, 리허설의 51 ms가 허용 기준을 초과한다고 판단한다. | 충족 | 충족 |
| 주문 INSERT를 막는 일반 방식은 이번 작업에 쓸 수 없다고 판단하고, 새 리허설이 통과할 때까지 운영 반영을 보류한다. 운영 성능을 측정한 것처럼 쓰지 않는다. | 충족 | 충족 |
| 무효 인덱스의 유효성을 확인하고 쓰기 비용이 남는 인덱스를 처리하는 구체적인 재시도 계획을 제시한다. | 충족 | 충족 |

**블라인드 검토** (X = 미적용, Y = 스킬 적용). 두 답 모두 허용 한도 48 ms를 넘긴 51 ms 리허설을 근거로 운영 반영을 보류하고, 실패 시 무효 인덱스를 확인해 제거하도록 한다. X 쪽은 지연 증가율 27.5%도 계산한다. Y 쪽은 무효 인덱스를 방치하면 플래너가 쓰지 않더라도 쓰기 비용이 남는다는 이유를 명시한다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `96fbdfc6834c` / `11153554b6ca` / `fb809a2d0596`.

</details>

## gtm-formal

**etcd의 두 후보가 동시에 당선되지 않으려면 몇 표가 필요할까?**

[English](EXAMPLES.md#gtm-formal)

2026-11-08 · `gtm-formal` 0.1.2 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [Ongaro and Ousterhout, In Search of an Understandable Consensus Algorithm, §5.2](https://raft.github.io/raft.pdf)
- [etcd v3.5 FAQ, fault tolerance](https://etcd.io/docs/v3.5/faq/#what-is-failure-tolerance)

Raft 논문은 한 임기의 단일 투표와 과반 선출을, etcd 문서는 다섯 투표자의 정족수를 설명합니다. 여섯 투표자에게 다른 문턱값을 적용하는 논증은 가상의 수학 문제입니다.

### 질문

> 분산 시스템 세미나에서 읽을 짧은 한국어 증명을 써 주세요. 투표자 n명이 고정된 클러스터에서 당선에 필요한 표 수를 q라고 할 때(1 ≤ q ≤ n), 요건을 충족한 두 투표자 집합이 반드시 겹칠 필요충분조건을 구하세요. 두 집합에 공통으로 속하는 투표자 수의 하한도 n과 q로 유도하세요. 한 투표자는 한 임기에 최대 한 표만 줍니다. 가상의 후보 etcd-east와 etcd-west로 이 조건을 리더 선출의 안전성과 연결하세요. 투표자 5명의 실제 과반수 선거와, 투표자가 6명인데 3표만으로 당선된다고 가정한 경우를 각각 따져 보세요. 필요하면 6명으로 반례를 구성하세요. 일부 투표자와 연락할 수 없을 때, 안전성만으로 선거의 진행을 보장할 수 있는지도 밝히세요.

### 스킬 미적용 답안

> ### 정족수 겹침과 리더 선출 안전성
>
> 투표자 집합을 $V$, $|V|=n$이라 하고, 당선에 필요한 표 수를 $q$라 하자. 크기가 각각 $q$인 두 당선 집합 $A,B\subseteq V$에 대해 포함배제 원리로
>
>
> $$
> |A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n.
> $$
>
>
> 따라서 $2q>n$, 즉 $q>n/2$이면 두 집합은 반드시 겹친다. 반대로 $2q\le n$이면 서로소인 크기 $q$의 집합을 만들 수 있으므로, 모든 두 당선 집합이 반드시 겹치는 필요충분조건은
>
>
> $$
> \boxed{q>n/2}
> $$
>
>
> 이다. 두 집합의 공통 투표자 수에 대한 일반적인 하한은 $\max(0,\,2q-n)$명이다.
>
> 이 겹침은 리더 선출의 안전성에 쓰인다. 예를 들어 etcd-east와 etcd-west가 같은 임기에 각각 $q$표를 얻었다고 하자. 두 당선 집합이 겹치고, 겹친 투표자가 한 임기에 최대 한 표만 준다면 두 후보 모두 당선될 수 없다. 그러므로 $q>n/2$는 같은 임기에 두 리더가 선출되는 것을 막는 데 필요한 정족수 조건이다. 이는 두 후보가 실제로 모두 당선된다는 뜻이 아니라, 그런 동시 당선이 불가능하다는 뜻이다.
>
> 투표자 5명인 클러스터의 실제 과반수는 $q=3$이다. 두 3인 집합은 최소 $2\cdot3-5=1$명 겹친다. 겹친 투표자는 같은 임기에 두 후보에게 표를 줄 수 없으므로, 두 후보의 동시 당선은 불가능하다.
>
> 반면 투표자 6명에게 3표만 있으면 당선된다고 하면 $q=3$이고, $2q-n=0$이다. 실제로
>
>
> $$
> A=\{1,2,3\},\qquad B=\{4,5,6\}
> $$
>
>
> 처럼 서로소인 당선 집합을 만들 수 있다. 앞의 세 명이 etcd-east에, 나머지 세 명이 etcd-west에 표를 주면 두 후보가 모두 당선될 수 있다. 따라서 이 규칙은 해당 안전성 보장을 제공하지 않는다.
>
> 마지막으로, 정족수 겹침은 안전성 조건이지 진행 보장 조건은 아니다. 일부 투표자와 연락할 수 없어 어떤 후보도 $q$표를 모으지 못한다면 선거는 완료되지 않는다. 안전성만으로는 선거가 반드시 진행된다고 보장할 수 없다.

<details>
<summary>원래 수식 표기로 보기</summary>

````text
### 정족수 겹침과 리더 선출 안전성

투표자 집합을 \(V\), \(|V|=n\)이라 하고, 당선에 필요한 표 수를 \(q\)라 하자. 크기가 각각 \(q\)인 두 당선 집합 \(A,B\subseteq V\)에 대해 포함배제 원리로

\[
|A\cap B|=|A|+|B|-|A\cup B|\ge 2q-n.
\]

따라서 \(2q>n\), 즉 \(q>n/2\)이면 두 집합은 반드시 겹친다. 반대로 \(2q\le n\)이면 서로소인 크기 \(q\)의 집합을 만들 수 있으므로, 모든 두 당선 집합이 반드시 겹치는 필요충분조건은

\[
\boxed{q>n/2}
\]

이다. 두 집합의 공통 투표자 수에 대한 일반적인 하한은 \(\max(0,\,2q-n)\)명이다.

이 겹침은 리더 선출의 안전성에 쓰인다. 예를 들어 etcd-east와 etcd-west가 같은 임기에 각각 \(q\)표를 얻었다고 하자. 두 당선 집합이 겹치고, 겹친 투표자가 한 임기에 최대 한 표만 준다면 두 후보 모두 당선될 수 없다. 그러므로 \(q>n/2\)는 같은 임기에 두 리더가 선출되는 것을 막는 데 필요한 정족수 조건이다. 이는 두 후보가 실제로 모두 당선된다는 뜻이 아니라, 그런 동시 당선이 불가능하다는 뜻이다.

투표자 5명인 클러스터의 실제 과반수는 \(q=3\)이다. 두 3인 집합은 최소 \(2\cdot3-5=1\)명 겹친다. 겹친 투표자는 같은 임기에 두 후보에게 표를 줄 수 없으므로, 두 후보의 동시 당선은 불가능하다.

반면 투표자 6명에게 3표만 있으면 당선된다고 하면 \(q=3\)이고, \(2q-n=0\)이다. 실제로

\[
A=\{1,2,3\},\qquad B=\{4,5,6\}
\]

처럼 서로소인 당선 집합을 만들 수 있다. 앞의 세 명이 etcd-east에, 나머지 세 명이 etcd-west에 표를 주면 두 후보가 모두 당선될 수 있다. 따라서 이 규칙은 해당 안전성 보장을 제공하지 않는다.

마지막으로, 정족수 겹침은 안전성 조건이지 진행 보장 조건은 아니다. 일부 투표자와 연락할 수 없어 어떤 후보도 \(q\)표를 모으지 못한다면 선거는 완료되지 않는다. 안전성만으로는 선거가 반드시 진행된다고 보장할 수 없다.
````

</details>

### 스킬 적용 답안 · standard

> 투표자 집합을 $V$, $|V|=n$이라 하자. 한 임기에 각 투표자는 최대 한 표만 주며, **요건을 충족한 집합**은 $V$의 원소를 $q$명 이상 포함하는 부분집합이다. 두 요건 충족 집합이 반드시 겹친다는 말은 임의의 두 그런 집합의 교집합이 공집합이 아니라는 뜻이다.
>
> **명제.** 두 요건 충족 집합이 반드시 겹칠 필요충분조건은
>
> $$
> 2q>n
> $$
>
> 이다. 임의의 두 요건 충족 집합 $A,B$에 대해 공통 투표자 수는
>
> $$
> |A\cap B|\ge \max(0,\,2q-n)
> $$
>
> 이다.
>
> **증명.** 포함배제에 의해
>
> $$
> |A\cap B|=|A|+|B|-|A\cup B|\ge q+q-n=2q-n.
> $$
>
> 교집합 크기는 음수가 될 수 없으므로 하한은 $\max(0,2q-n)$이다. 따라서 $2q>n$이면 교집합은 적어도 한 명이다.
>
> 역으로 $2q\le n$이라 하자. $V$에서 서로소인 $q$명짜리 부분집합 두 개를 고를 수 있다. 두 집합은 모두 요건을 충족하지만 겹치지 않으므로, 반드시 겹친다는 조건은 성립하지 않는다. 이로써 필요충분성이 증명된다. $2q=n$인 경계에서도 하한은 0이며, 서로소인 두 집합이 가능하다.
>
> **리더 선출에의 적용.** 같은 임기에서 `etcd-east`와 `etcd-west`가 각각 당선되려면 서로 다른 투표자 집합으로부터 $q$표를 받아야 한다. $2q>n$이면 두 집합이 적어도 한 투표자를 공유한다. 각 투표자가 임기에 최대 한 표만 주므로 그 공통 투표자는 두 후보 모두에게 투표할 수 없다. 따라서 두 후보가 모두 당선될 수 없다. 이는 이 투표 모델에서의 안전성, 즉 한 임기에 두 후보가 동시에 당선되지 않는다는 성질이다.
>
> **사례.** 투표자가 5명이고 실제 과반수로 선출한다면 $q=3$이다. 두 당선 집합의 교집합 크기는 적어도 $2\cdot3-5=1$이므로 반드시 겹친다. 반면 투표자가 6명인데 3표만으로 당선된다고 가정하면 $q=3$이고 $2q=n$이다. 다음 두 집합은 서로소이면서 각각 요건을 충족한다.
>
> $$
> A=\{1,2,3\},\qquad B=\{4,5,6\}.
> $$
>
> 따라서 이 규칙만으로는 같은 임기에 `etcd-east`와 `etcd-west`가 각각 당선되는 경우를 배제할 수 없다.
>
> 마지막으로, 안전성은 선거의 진행을 보장하지 않는다. 연락 가능한 투표자가 $q$명보다 적으면 어떤 후보도 필요한 표를 모을 수 없다. 따라서 $2q>n$은 당선 집합 간의 겹침을 통한 안전성 조건이지, 일부 투표자와 연락할 수 없는 상황에서 선거가 반드시 완료된다는 진행성 보장은 아니다.

<details>
<summary>원래 수식 표기로 보기</summary>

````text
투표자 집합을 \(V\), \(|V|=n\)이라 하자. 한 임기에 각 투표자는 최대 한 표만 주며, **요건을 충족한 집합**은 \(V\)의 원소를 \(q\)명 이상 포함하는 부분집합이다. 두 요건 충족 집합이 반드시 겹친다는 말은 임의의 두 그런 집합의 교집합이 공집합이 아니라는 뜻이다.

**명제.** 두 요건 충족 집합이 반드시 겹칠 필요충분조건은
\[
2q>n
\]
이다. 임의의 두 요건 충족 집합 \(A,B\)에 대해 공통 투표자 수는
\[
|A\cap B|\ge \max(0,\,2q-n)
\]
이다.

**증명.** 포함배제에 의해
\[
|A\cap B|=|A|+|B|-|A\cup B|\ge q+q-n=2q-n.
\]
교집합 크기는 음수가 될 수 없으므로 하한은 \(\max(0,2q-n)\)이다. 따라서 \(2q>n\)이면 교집합은 적어도 한 명이다.

역으로 \(2q\le n\)이라 하자. \(V\)에서 서로소인 \(q\)명짜리 부분집합 두 개를 고를 수 있다. 두 집합은 모두 요건을 충족하지만 겹치지 않으므로, 반드시 겹친다는 조건은 성립하지 않는다. 이로써 필요충분성이 증명된다. \(2q=n\)인 경계에서도 하한은 0이며, 서로소인 두 집합이 가능하다.

**리더 선출에의 적용.** 같은 임기에서 `etcd-east`와 `etcd-west`가 각각 당선되려면 서로 다른 투표자 집합으로부터 \(q\)표를 받아야 한다. \(2q>n\)이면 두 집합이 적어도 한 투표자를 공유한다. 각 투표자가 임기에 최대 한 표만 주므로 그 공통 투표자는 두 후보 모두에게 투표할 수 없다. 따라서 두 후보가 모두 당선될 수 없다. 이는 이 투표 모델에서의 안전성, 즉 한 임기에 두 후보가 동시에 당선되지 않는다는 성질이다.

**사례.** 투표자가 5명이고 실제 과반수로 선출한다면 \(q=3\)이다. 두 당선 집합의 교집합 크기는 적어도 \(2\cdot3-5=1\)이므로 반드시 겹친다. 반면 투표자가 6명인데 3표만으로 당선된다고 가정하면 \(q=3\)이고 \(2q=n\)이다. 다음 두 집합은 서로소이면서 각각 요건을 충족한다.
\[
A=\{1,2,3\},\qquad B=\{4,5,6\}.
\]
따라서 이 규칙만으로는 같은 임기에 `etcd-east`와 `etcd-west`가 각각 당선되는 경우를 배제할 수 없다.

마지막으로, 안전성은 선거의 진행을 보장하지 않는다. 연락 가능한 투표자가 \(q\)명보다 적으면 어떤 후보도 필요한 표를 모을 수 없다. 따라서 \(2q>n\)은 당선 집합 간의 겹침을 통한 안전성 조건이지, 일부 투표자와 연락할 수 없는 상황에서 선거가 반드시 완료된다는 진행성 보장은 아니다.
````

</details>

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 요건을 충족한 두 집합에 대해 \|E∩W\| ≥ 2q−n을 유도하고, 2q>n과 임기당 한 표 규칙 때문에 두 리더가 동시에 당선되지 못함을 보인다. | 충족 | 충족 |
| 2q≤n이면 서로 겹치지 않는 집합을 구성할 수 있어 필요조건임을 보인다. 5명의 과반수 3표와 6명이 두 그룹으로 3표씩 나뉠 수 있는 반례를 제시한다. | 충족 | 충족 |
| 가상의 6명 중 3표와 실제 Raft 과반수를 구분하고, 투표 부족 시 안전성이 진전을 보장하지 않는 이유를 밝힌다. | 충족 | 충족 |

**블라인드 검토** (Y = 미적용, X = 스킬 적용). 두 증명 모두 2q−n의 하한을 유도하고 q가 n의 절반을 넘어야 하는 이유와 임기당 한 표의 의미를 설명한다. X 쪽은 경계 2q=n에서 하한이 0임을 따로 짚는다. Y 쪽은 두 집단이 각각 누구에게 투표하면 함께 당선될 수 있는지 보여 준다. 둘 다 6명 중 3표를 가정한 규칙과 실제 과반수 원리를 구분하고, 정족수가 없으면 선거가 진행되지 않을 수 있다고 밝힌다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `b351e00329c8` / `b2bffd7272a2` / `5ec37cc9df03`.

</details>

## hunminjeongeum

**서울 지하철 노선도를 빨리 읽으면 전체 여정은 얼마나 줄어드나요?**

[English](EXAMPLES.md#hunminjeongeum)

2026-11-08 · `hunminjeongeum` 0.1.1 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [서울특별시, 시민의 발, 디자인을 입다…서울시, 지하철 노선도 40년 만에 변경 (2023-09-13)](https://news.seoul.go.kr/culture/archives/520933)

서울시 발표의 최대 약 69% 감소는 실험에서 환승역 길을 찾는 데 걸린 시간에 관한 수치입니다. 예시 여행의 지도 탐색 시간 및 승차 시간은 따로 주어진 가정입니다.

### 질문

> 서울 지하철을 처음 타는 사람에게, 서울시가 2023년에 노선도를 고치려 한 이유와 숫자의 의미를 한국어 네 문장 이내로 설명해 주세요. 기존 지도에서는 환승역이 일반역과 잘 구분되지 않았고, 개선안은 환승할 노선들의 색을 한 표시에 연결했어요. 20~30대 내국인·외국인의 시선 추적 실험에서 환승역 길 찾기 시간이 최대 약 69% 줄었어요. 설명용으로 어떤 승객이 예전 지도에서 길을 찾는 데 100초, 이후 열차 안에서 이동하는 시간이 12분이라고 가정해요. 지도 보는 시간에 그 최대 감소율을 적용한다면 지도 탐색 시간과 열차 안에서 이동하는 시간의 합계는 얼마일까요? 누군가 ‘여정 전체가 69% 빨라진다’고 소개하려고 해요.

### 스킬 미적용 답안

> 서울시는 기존 노선도에서 환승역이 일반역과 잘 구분되지 않아 길 찾기가 어려운 점을 개선하려고 했어요. 개선안은 환승역에서 갈아탈 노선들의 색을 하나의 표시에 연결해 환승 정보를 쉽게 알아보도록 했고, 20~30대 내국인·외국인의 시선 추적 실험에서는 환승역 길 찾기 시간이 최대 약 69% 줄었어요. 예전 지도에서 100초 걸렸다고 가정하면 지도 탐색 시간은 최대 감소율 적용 후 31초이고, 열차 안 이동 시간 12분을 더하면 합계는 12분 31초예요. 따라서 69%는 지도 탐색 시간에 적용한 수치이지, 여정 전체가 69% 빨라진다는 뜻은 아니에요.

### 스킬 적용 답안 · standard

> 서울 지하철을 처음 타면 환승역 표시가 일반역과 비슷해 길을 찾기 어려울 수 있어, 서울시는 2023년 노선도에서 환승할 노선들의 색을 하나의 표시에 연결하는 개선안을 내놓았습니다. 20~30대 내국인·외국인을 대상으로 한 시선 추적 실험에서 환승역 길 찾기 시간이 최대 약 69% 줄었다는 뜻입니다. 설명을 위해 예전 지도에서 찾는 데 100초 걸렸다고 가정하면, 그 시간에 69% 감소를 적용한 탐색 시간은 31초이고, 열차 이동 12분을 더한 합계는 12분 31초입니다. 이 계산은 지도 탐색 시간에만 감소율을 적용한 것이므로, ‘여정 전체가 69% 빨라진다’고 말할 근거는 아닙니다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 환승역과 일반역을 구분하기 어려웠던 승객의 문제에서 시작해, 환승 노선 색을 연결한 표식이 그 문제를 어떻게 해결하는지 설명한다. | 충족 | 충족 |
| 새 지도 탐색 시간은 약 31초이고 열차 탑승 시간은 여전히 12분이어서 가상 여정의 합계가 약 12분 31초라고 계산한다. | 충족 | 충족 |
| 최대 약 69% 감소한 것은 시선 추적 실험에서의 환승역 길 찾기 시간이며, 실제 전체 이동 시간이 그렇게 줄었다는 뜻이 아님을 분명히 한다. | 충족 | 충족 |

**블라인드 검토** (Y = 미적용, X = 스킬 적용). X와 Y 모두 환승역을 일반역과 구별하기 어려웠다는 문제를 노선 색을 연결한 표식과 연결한다. 지도 탐색만 100초에서 31초로 줄고 열차 안 이동은 12분이어서 합계가 12분 31초라는 계산과 실험 범위를 네 문장 안에 담는다. 개선안의 연도(2023년)는 X에만 있다.

<details>
<summary>표현을 명확히 하기 전의 질문과 답안</summary>

“열차를 타는 데”가 탑승 대기처럼 읽힐 수 있어 “열차 안에서 이동하는 시간”으로 구체화하고 한국어 양쪽 답을 새로 생성했습니다. 위 판정은 최종 질문에 대해서만 이뤄졌습니다.

**이전 질문**

> 서울 지하철을 처음 타는 사람에게, 서울시가 2023년에 노선도를 고치려 한 이유와 숫자의 의미를 한국어 네 문장 이내로 설명해 주세요. 기존 지도에서는 환승역이 일반역과 잘 구분되지 않았고, 개선안은 환승할 노선들의 색을 한 표시에 연결했어요. 20~30대 내국인·외국인의 시선 추적 실험에서 환승역 길 찾기 시간이 최대 약 69% 줄었어요. 설명용으로 어떤 승객이 예전 지도에서 길을 찾는 데 100초, 이후 열차를 타는 데 12분이 걸린다고 가정해요. 지도 보는 시간에 그 최대 감소율을 적용한다면 지도를 보고 열차를 타는 데 걸리는 합계는 얼마일까요? 누군가 ‘여정 전체가 69% 빨라진다’고 소개하려고 해요.

**이전 미적용 답안**

> 서울시는 기존 노선도에서 환승역이 일반역과 잘 구분되지 않아 길 찾기가 어려운 점을 개선하려 했고, 개선안은 환승 노선들의 색을 한 표시에 연결했어요. 20~30대 내국인·외국인 실험에서 환승역 길 찾기 시간은 최대 약 69% 줄었지만, 이는 실험에서 측정한 길 찾기 시간에 관한 수치예요. 설명용 가정에 따르면 지도 보는 시간은 100초에서 약 31초로 줄고, 열차 탑승까지 12분을 더하면 합계는 **12분 31초**예요. 따라서 ‘여정 전체가 69% 빨라진다’고 말할 수는 없어요.

**이전 적용 답안**

> 처음 서울 지하철을 타면 환승역이 일반역과 잘 구분되지 않아, 갈아탈 곳을 찾기 어려울 수 있습니다. 서울시는 환승할 노선들의 색을 한 표시에 연결해 환승역을 알아보기 쉽도록 노선도를 고치려 했고, 20~30대 내국인·외국인의 시선 추적 실험에서는 환승역 길 찾기 시간이 최대 약 69% 줄었습니다. 설명용 가정에서 예전 지도 보는 시간 100초에 이 감소율을 적용하면 31초이고, 이후 열차를 타는 데 걸리는 12분을 더한 합계는 12분 31초입니다. 이 계산은 지도 보는 시간에만 최대 감소율을 적용한 것이므로, ‘여정 전체가 69% 빨라진다’고 말할 근거는 되지 않습니다.

</details>

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `41f1b8c56caa` / `3ed4cb7760bb` / `aef558c2f63e`.

</details>

## ietf-rfc

**HTTP 429 응답에서 두 가지 재시도 시각 계산하기**

[English](EXAMPLES.md#ietf-rfc)

2026-11-08 · `ietf-rfc` 0.1.3 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [IETF RFC 6585 §4, 429 Too Many Requests](https://www.rfc-editor.org/rfc/rfc6585.html#section-4)
- [IETF RFC 9110 §10.2.3, Retry-After](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.2.3)

RFC 6585는 429 응답의 선택과 캐시 저장 금지를, RFC 9110은 Retry-After의 HTTP 날짜 및 수신 이후의 초 단위를 설명합니다. 두 응답의 시각은 예시입니다.

### 질문

> 가상의 요청 제한 응답 두 건을 다루는 짧은 한국어 내부 API 명세를 써 주세요. 둘 다 09:00:00 UTC에 보냈고 클라이언트는 09:00:05 UTC에 받았습니다. 첫 응답은 Retry-After: 45를, 둘째 응답은 그날 09:01:00 UTC에 해당하는 HTTP 날짜를 담았습니다. 시계는 동기화되어 있습니다. RFC 6585에 따르면 서버는 429 응답을 보낼지 선택할 수 있고, 응답 본문에는 제한 사유를 설명하는 것이 권장되며 Retry-After를 포함할지는 선택 사항입니다. 캐시는 429 응답을 저장할 수 없습니다. RFC 9110에서는 HTTP 날짜 또는 응답 수신 시점부터 세는 0 이상의 초 단위를 허용합니다. 대문자 BCP 14 키워드의 의미를 먼저 밝히고, 각 경우 클라이언트에 제시되는 재시도 시각과 두 시각 모두 보장하지 않는 것을 설명하세요. 근거가 없는 클라이언트 의무는 추가하지 마세요.

### 스킬 미적용 답안

> ## 내부 API 명세: 429 요청 제한 응답
>
> 이 명세에서 대문자 **MUST**, **SHOULD**, **MAY**는 BCP 14에서 정의한 규범 키워드입니다. 대문자로 쓰인 경우에만 그 의미를 갖습니다.
>
> 서버는 요청을 제한할 때 429 응답을 **MAY** 보낼 수 있습니다. 응답 본문은 제한 사유를 설명하는 것이 **SHOULD**이며, `Retry-After`를 포함하는 것은 **MAY**입니다. 캐시는 429 응답을 저장할 수 없습니다.
>
> 두 응답 모두 서버가 09:00:00 UTC에 보냈고 클라이언트가 09:00:05 UTC에 받았습니다. 시계는 동기화되어 있습니다. HTTP 날짜 형식은 재시도 시각을 나타내고, 초 단위 형식은 응답 수신 시점부터 세는 0 이상의 대기 시간을 나타냅니다.
>
> | `Retry-After` 값 | 클라이언트에 제시되는 재시도 시각 |
> |---|---|
> | `45` | 수신 시각 09:00:05 UTC부터 45초 뒤인 **09:00:50 UTC** |
> | 해당 날짜의 09:01:00 UTC를 나타내는 HTTP 날짜 | **09:01:00 UTC** |
>
> 두 시각 모두 해당 시각에 재시도가 성공한다거나, 서버가 그때까지 제한을 해제한다는 것을 보장하지 않습니다.

### 스킬 적용 답안 · standard

> 이 내부 API 명세는 두 가상 `429 Too Many Requests` 응답에서 `Retry-After` 값을 해석하는 클라이언트 동작을 다룹니다. 클라이언트는 두 응답을 모두 `09:00:05 UTC`에 받았으며 시계는 동기화되어 있습니다. 이 문서에서 대문자 요구 키워드는 RFC 2119와 RFC 8174의 BCP 14 의미로 사용합니다.
>
> 서버는 `429` 응답을 보낼지 선택할 수 있습니다. 응답을 보낼 경우 본문에 제한 사유를 설명하는 것이 권장되며, `Retry-After` 헤더를 포함할지는 선택 사항입니다. 캐시는 `429` 응답을 저장할 수 없습니다.
>
> 첫 응답의 `Retry-After: 45`는 응답 수신 시점부터 45초를 뜻하므로, 클라이언트에 제시되는 재시도 시각은 `09:00:50 UTC`입니다. 둘째 응답의 `Retry-After`는 그날 `09:01:00 UTC`를 나타내는 HTTP 날짜이므로, 제시되는 재시도 시각은 `09:01:00 UTC`입니다. 두 시각 모두 재시도를 보장하거나 요구하지 않습니다.
>
> 참고 자료: [RFC 6585](https://www.rfc-editor.org/rfc/rfc6585.html), [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html).
>
> **작성 기록:** `ietf-rfc` 방법론 v0.1.3, standard 수준 적용. 요청에 제공된 동작과 시각을 전제로 했습니다. 내부 명세이며 별도의 클라이언트 재시도 의무를 추가하지 않았습니다. IANA 조치는 해당되지 않습니다. Normative reference: RFC 9110. Informative reference: RFC 6585.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| BCP 14 키워드의 표기 규칙을 밝히고, 429 전송과 Retry-After 포함은 선택 사항, 사유 설명은 SHOULD, 캐시 저장은 MUST NOT이라는 강도를 보존한다. | 충족 | 충족 |
| 수신 후 45초인 첫 경우를 09:00:50 UTC, 날짜로 정한 둘째 경우를 09:01:00 UTC로 계산한다. | 충족 | 충족 |
| 두 시각은 재시도 권고이며 성공을 보장하지 않는다고 밝힌다. 클라이언트에 새로운 MUST나 SHOULD를 부과하지 않는다. | 충족 | 미충족 |

**블라인드 검토** (X = 미적용, Y = 스킬 적용). X와 Y 모두 서버의 선택권·본문 설명 권고·캐시 저장 금지를 유지하고, 수신 후 45초인 09:00:50 UTC와 날짜가 지정한 09:01:00 UTC를 구분한다. X는 재시도 성공이나 제한 해제를 보장하지 않는다고 명시한다. Y의 ‘재시도를 보장하거나 요구하지 않습니다’는 재시도 자체에 관한 말로, 시도했을 때의 성공 여부를 설명하지 않는다. Y는 429의 의무를 정한 RFC 6585를 참고용(informative)으로 분류한 점도 부정확하다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `1613a9080cdb` / `c460af81b495` / `602495001ecb`.

</details>

## imrad

**LIGO의 오경보율을 10년에 적용하면 무엇을 말할 수 있을까?**

[English](EXAMPLES.md#imrad)

2026-11-08 · `imrad` 0.1.3 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [LIGO Scientific Collaboration and Virgo Collaboration, Observation of Gravitational Waves from a Binary Black Hole Merger (2016)](https://dcc.ligo.org/public/0122/P150914/014/LIGO-P150914_Detection_of_GW150914.pdf)

LIGO 논문의 초록과 제V.B절은 신호 관측, 파형 비교, 잡음 오경보율의 상한을 제시합니다. 같은 비율을 가정한 10년의 기대 건수는 이 문제에서 유도할 값입니다.

### 질문

> 박물관에서 읽을 수 있도록 LIGO의 GW150914 관측을 한국어 연구 초록으로 다섯 문장 이내에 설명해 주세요. 2015년 9월 14일 리빙스턴과 핸퍼드 검출기는 주파수가 35 Hz에서 250 Hz까지 상승한 신호를 기록했습니다. 차원이 없는 변형률의 최댓값은 1.0 × 10⁻²¹이었습니다. 연구진은 이 신호가 두 블랙홀의 병합을 예측한 파형과 일치함을 확인했습니다. 이 탐색에서 잡음이 관측 신호만큼 또는 그보다 유의한 후보로 검출될 비율은 203,000년에 한 건 미만으로 추정됐습니다. 편집자는 “10년 동안 오경보가 단 한 건도 없을 테니 이 신호가 잡음일 확률은 0이다”라고 주장합니다. 같은 비율이 유지되는 가상의 10년 동안 그런 잡음 후보 수의 기댓값에 어떤 상한을 둘 수 있는지 계산해 주세요. 검출기의 측정, 연구진의 분석, 그에 따른 해석을 구분해서 편집자의 주장을 평가해 주세요.

### 스킬 미적용 답안

> **관측과 분석.** 2015년 9월 14일 리빙스턴과 핸퍼드의 LIGO 검출기는 35 Hz에서 250 Hz까지 주파수가 상승하는 중력파 신호를 기록했으며, 차원이 없는 변형률의 최댓값은 $1.0 \times 10^{-21}$이었다. 연구진은 관측 파형이 두 블랙홀의 병합을 예측한 파형과 일치한다고 분석했다. 이 탐색에서 관측 신호만큼 또는 그보다 유의한 잡음 후보가 검출될 비율은 203,000년에 한 건 미만으로 추정됐다. **10년간의 기대 건수.** 같은 비율이 유지된다고 가정하면, 10년 동안 그런 잡음 후보 수의 기댓값은 $10/203{,}000 \approx 4.93 \times 10^{-5}$건 미만이다. **해석.** 이는 기대 건수가 매우 작다는 뜻이지, 오경보가 반드시 한 건도 없거나 신호가 잡음일 확률이 0이라는 뜻은 아니다.

<details>
<summary>원래 수식 표기로 보기</summary>

````text
**관측과 분석.** 2015년 9월 14일 리빙스턴과 핸퍼드의 LIGO 검출기는 35 Hz에서 250 Hz까지 주파수가 상승하는 중력파 신호를 기록했으며, 차원이 없는 변형률의 최댓값은 \(1.0 \times 10^{-21}\)이었다. 연구진은 관측 파형이 두 블랙홀의 병합을 예측한 파형과 일치한다고 분석했다. 이 탐색에서 관측 신호만큼 또는 그보다 유의한 잡음 후보가 검출될 비율은 203,000년에 한 건 미만으로 추정됐다. **10년간의 기대 건수.** 같은 비율이 유지된다고 가정하면, 10년 동안 그런 잡음 후보 수의 기댓값은 \(10/203{,}000 \approx 4.93 \times 10^{-5}\)건 미만이다. **해석.** 이는 기대 건수가 매우 작다는 뜻이지, 오경보가 반드시 한 건도 없거나 신호가 잡음일 확률이 0이라는 뜻은 아니다.
````

</details>

### 스킬 적용 답안 · standard

> **방법·수준: IMRaD, 표준**
>
> 2015년 9월 14일 리빙스턴과 핸퍼드의 LIGO 검출기는 주파수가 35 Hz에서 250 Hz로 상승하고 최댓값이 1.0 × 10⁻²¹인 무차원 변형률 신호를 기록했다. 연구진은 분석 결과 이 신호가 두 블랙홀 병합을 예측한 파형과 일치한다고 판단했다. 이 탐색에서 관측 신호만큼 또는 그보다 유의한 잡음 후보의 추정 비율은 203,000년에 한 건 미만이었다. 같은 비율이 10년간 유지된다고 가정하면 그런 잡음 후보 수의 기댓값은 10/203,000, 즉 약 4.93 × 10⁻⁵건 미만이다. 이는 기대되는 잡음 후보 수의 상한이지, 10년 동안 오경보가 없음을 보장하거나 이 신호가 잡음일 확률을 0으로 만드는 값은 아니므로 편집자의 주장은 근거를 넘어선다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 두 검출기, 관측 날짜, 35~250 Hz와 변형률 1.0 × 10⁻²¹을 보존하고, 파형 비교의 주체를 검출기가 아닌 연구진의 분석으로 구분한다. | 충족 | 충족 |
| 가정한 10년 동안 후보 수의 기댓값이 10/203,000(약 4.93 × 10⁻⁵)보다 작다고 계산하며, 이를 개별 사건의 확률로 제시하지 않는다. | 충족 | 충족 |
| 잡음 후보가 0건일 것이 보장된다거나 이 사건이 잡음일 확률이 0이라는 결론을 둘 다 배척한다. 관측 신호와 그 신호가 뒷받침하는 블랙홀 병합 해석을 구분한다. | 충족 | 충족 |

**블라인드 검토** (X = 미적용, Y = 스킬 적용). 두 답 모두 기댓값이 10/203,000 미만이라는 점과 ‘오경보가 절대로 없다’는 주장 사이의 차이를 정확히 설명합니다. X 쪽은 관측·분석과 해석을 문장 안의 표지로 나눕니다. Y 쪽은 초록 앞에 방법과 수준을 밝혀, 답만 보아도 적용 조건을 짐작할 수 있습니다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `85287f2bd34d` / `e95fcfb40e21` / `e86f8f801cba`.

</details>

## korean-plain-language

**서울 기후동행카드 환급 안내에서 시점과 신청 가능성을 어떻게 살릴까요?**

[English](EXAMPLES.md#korean-plain-language)

2026-11-08 · `korean-plain-language` 0.1.2 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [서울특별시 내 손안에 서울, ‘월 5만원대’ 청년 맞춤형 기후동행카드 나온다 (2024-02-21)](https://mediahub.seoul.go.kr/archives/2010350)

서울시의 2024년 시범사업 안내에 따른 당시 환급 조건을 다룹니다. 지우·민서의 이용 내역은 조건을 적용해 보기 위해 만든 사례입니다.

**언어 적용 범위.** 한국어 원문에서 시점과 신청 가능성, 해요체 표현을 직접 점검합니다.

### 질문

> 서울의 2024년 기후동행카드 시범사업을 다룬 전시 문구를 편집합니다. 초안은 ‘지우와 민서는 지금 환급금을 받아요’입니다. 당시 청년 할인 대상자는 실물카드 등록 후 이용분이나 별도 등록이 필요 없는 모바일카드 이용분 중 환불 없이 30일 만기를 채운 달마다 7,000원을 신청할 수 있었고, 두 카드 모두 환급을 별도로 신청해야 했어요. 연령 등 나머지 조건은 충족했다고 가정합니다. 지우는 실물카드 첫 30일권을 미등록 상태로 끝까지 쓴 뒤 등록하고, 둘째 권은 만기까지, 셋째 권은 18일째 환불했어요. 민서는 모바일카드 두 장을 각각 30일 만기까지 썼어요. 편집자에게 한국어로 짧은 메모를 써 주세요. 두 사람이 얼마를 신청할 수 있었는지와 그 이유를 밝히고, 초안이 잘못 전달하는 시점과 자동 지급 여부를 바로잡을 해요체 표현을 제시해 주세요.

### 스킬 미적용 답안

> 편집 메모: 지우는 실물카드를 등록하기 전에 쓴 첫 이용분은 환급 대상에서 빠지고, 등록 후 만기를 채운 둘째 이용분만 신청할 수 있어요. 셋째 이용분은 18일째 환불했으므로 대상이 아니에요. 따라서 7,000원을 신청할 수 있어요. 민서는 모바일카드 두 장 모두 30일 만기를 채웠으므로 합계 14,000원을 신청할 수 있어요. 두 사람 모두 환급금이 자동 지급되는 건 아니고 별도로 신청해야 해요.
>
> 표현 제안: **“지우와 민서는 환급금을 신청할 수 있어요.”**

### 스킬 적용 답안 · standard

> - 지우: **7,000원**을 신청할 수 있었어요. 첫 실물카드는 이용 중 등록하지 않아 대상이 아니었고, 둘째 카드만 환불 없이 30일 만기를 채웠어요. 셋째 카드는 18일째 환불해 만기를 채우지 못했어요.
> - 민서: **14,000원**을 신청할 수 있었어요. 모바일카드 두 장 모두 만기까지 사용했어요.
> - 환급금은 당시 이용 실적에 대해 신청할 수 있었어요. 두 카드 모두 자동 지급이 아니라 별도 신청이 필요했어요.
>
> **수정 문구:** “지우와 민서는 당시 조건을 충족한 이용분에 대해 환급금을 별도로 신청할 수 있었어요.”

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 지우는 등록 후 만기를 채운 둘째 권만 해당해 7,000원이며, 첫 권과 셋째 권은 각각 미등록과 중도 환불로 제외됨을 설명한다. | 충족 | 충족 |
| 민서는 만기 두 번으로 14,000원이고, 모바일카드 등록 면제와 두 종류 모두 별도의 환급 신청이 필요했던 점을 구분한다. | 미충족 | 미충족 |
| 2024년 당시 신청할 수 있었다는 뜻을 전달하는 해요체 표현을 제시하고, 현재 신청 가능이나 자동 지급을 암시하는 원문의 문제를 고친다. | 미충족 | 충족 |

**블라인드 검토** (X = 미적용, Y = 스킬 적용). 두 답 모두 지우의 7,000원과 민서의 14,000원을 계산하고, 실물카드의 미등록·중도 환불 이용분을 제외합니다. 둘 다 모바일카드는 별도 카드 등록이 필요 없었다는 점을 명시하지 않습니다. X의 제안 문구는 여전히 ‘신청할 수 있어요’라고 해 현재의 자격처럼 읽힙니다. Y의 ‘당시 … 신청할 수 있었어요’는 과거의 신청 가능성을 살립니다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `c0be7cf32505` / `bb769f285186` / `b4951e717a02`.

</details>

## microsoft-writing-style

**Windows 클립보드에서 필요한 항목만 두 개 남기기**

[English](EXAMPLES.md#microsoft-writing-style)

2026-11-08 · `microsoft-writing-style` 0.1.2 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [Microsoft Support, Using the clipboard](https://support.microsoft.com/en-us/windows/apps/using-the-clipboard)

Microsoft 문서는 Windows 11 장치의 클립보드 기록 열기, 고정 항목을 제외한 일괄 지우기, 항목별 삭제를 설명합니다. 클립보드의 내용은 가정입니다.

**언어 적용 범위.** 이 스킬은 영어 기술 문서를 위한 프로필입니다. 한국어 예제는 작업 순서와 조건을 설명하는 구조를 적용하고 영어 UI의 실제 이름을 보존합니다. 한국어 문법의 검증이나 공식 한국어 UI 명칭을 뜻하지 않습니다.

### 질문

> Windows 11에서 이 PC의 클립보드 기록에 두 항목만 남기려는 사람을 위해 짧은 한국어 도움말을 써 주세요. 사용자의 Windows 화면은 영어로 표시됩니다. 배송 주소와 더 이상 쓰지 않는 출입 코드가 고정되어 있고, 반품 참조 번호와 메모 두 개는 고정되지 않은 상태입니다. 배송 주소와 반품 참조 번호는 다시 입력할 필요 없이 남기고 나머지 세 항목을 지워야 합니다. Windows logo key + V로 클립보드 기록을 엽니다. 항목을 고정할 수 있고, Clear all은 고정되지 않은 항목을 삭제합니다. See more (...)에서 Delete를 선택하면 해당 항목을 지울 수 있습니다. Clear all을 사용하는 확실한 절차 하나를 제시하고, 어떤 작업을 먼저 해야 하는지와 완료 여부를 확인할 방법을 알려 주세요. 실제 영문 버튼 이름은 그대로 쓰세요. 대상은 이 PC뿐입니다.

### 스킬 미적용 답안

> Windows logo key + V를 눌러 클립보드 기록을 엽니다. 배송 주소와 반품 참조 번호가 **고정되어 있지 않다면** 각각의 See more (...)에서 **Pin**을 선택합니다. 두 항목이 고정된 것을 확인한 뒤 **Clear all**을 선택하세요. 고정되지 않은 항목만 삭제되므로 출입 코드와 메모 두 개가 지워집니다.
>
> 완료 여부는 기록을 다시 확인해 배송 주소와 반품 참조 번호만 남아 있는지 보면 됩니다. 고정된 출입 코드도 그대로 남아 있을 수 있으니, 남아 있다면 See more (...)에서 **Delete**를 선택해 지우세요.

### 스킬 적용 답안 · standard

> Windows 11에서 이 PC의 클립보드 기록에 배송 주소와 반품 참조 번호만 남기려면, 먼저 두 항목을 고정하세요. 그래야 **Clear all**을 선택해도 남습니다.
>
> 1. **Windows logo key + V**를 눌러 클립보드 기록을 엽니다.
> 2. 배송 주소에서 **See more (...)** > **Pin**을 선택합니다. 반품 참조 번호도 같은 방법으로 고정합니다.
> 3. 두 항목에 고정 표시가 있는지 확인한 다음 **Clear all**을 선택합니다. 고정되지 않은 항목은 삭제됩니다.
> 4. 클립보드 기록에 배송 주소와 반품 참조 번호만 남았는지 확인합니다. 출입 코드와 메모 두 개가 없으면 완료입니다.
>
> *작성 상태: microsoft-writing-style v0.1.2, standard 수준을 적용했습니다. 한국어 전반의 이해도와 작업 순서를 검토했습니다. UI 항목명은 화면에 표시되는 영문 그대로 유지했습니다. 자세한 항목별 감사는 요청되지 않아 생략했습니다. ც

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| Windows logo key + V로 기록을 열고 Clear all 전에 반품 참조 번호를 고정한다. 이미 고정된 배송 주소는 유지한다. | 충족 | 충족 |
| See more (...)의 Delete로 고정된 출입 코드를 지우거나, 명시적으로 고정을 해제한 뒤 Clear all로 없앤다. Clear all만으로 고정된 코드가 사라진다고 하지 않는다. | 미충족 | 미충족 |
| 최종적으로 주소와 반품 참조 번호만 남고 메모 두 개가 삭제되는 사용자용 절차를 제공한다. 다른 기기 상태에 관한 근거 없는 주장은 하지 않는다. | 충족 | 미충족 |

**블라인드 검토** (X = 미적용, Y = 스킬 적용). 두 답 모두 반품 참조 번호를 먼저 고정한다. X 쪽은 Clear all로 고정된 출입 코드도 지워진다고 잘못 설명하지만, 마지막에 실제로 남은 코드를 See more (...)의 Delete로 지우는 단계를 제시해 목표 상태에 도달할 수 있다. Y 쪽은 이미 고정된 주소를 다시 고정하도록 하고 코드 삭제 단계를 빠뜨린다. 요청하지 않은 방법 이름·수준과 불필요한 문자도 덧붙였다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `fe6a3443c596` / `49b13f22cab5` / `0659b269dc01`.

</details>

## minto-pyramid

**보행 선행신호 시범사업은 어느 교차로에 먼저 도입할까요?**

[English](EXAMPLES.md#minto-pyramid)

2026-11-08 · `minto-pyramid` 0.2.2 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [FHWA, Leading Pedestrian Interval](https://highways.dot.gov/safety/proven-safety-countermeasures/leading-pedestrian-interval)
- [FHWA, Safety Evaluation of Protected Left-Turn Phasing and Leading Pedestrian Intervals on Pedestrian Safety (2018), FHWA-HRT-18-044](https://www.fhwa.dot.gov/publications/research/safety/18044/18044.pdf)

FHWA는 보행 선행신호의 원리와 세 도시의 충돌 변화 계수 0.87을 보고했습니다. 두 후보 지역의 기준 건수는 시범사업 의사결정을 위한 가정이며 실제 지역 조사 결과가 아닙니다.

### 질문

> 시 교통위원회가 선회 차량이 많은 신호 교차로 두 집단 중 한 곳에서만 시범사업을 할 수 있습니다. 사업비는 같고 목표는 차량·보행자 충돌의 예상 감소 건수를 최대화하는 것입니다. 보행 신호는 차량 녹색 신호보다 3~7초 먼저 켜집니다. 미국 연방도로청의 세 도시 연구에서 추정된 충돌수정계수는 0.87입니다. 가상 비교에서 같은 기간 사업을 하지 않을 때 북부에서는 20건, 남부에서는 5건의 차량·보행자 충돌이 예상됩니다. 연구의 계수를 그대로 적용할 경우 각 집단의 예상 감소 건수를 계산하세요. 위원회 결정문의 첫 문단을 한국어로 작성해 시범 지역을 추천하고 선회 차량에 보행 선행신호가 왜 도움이 될 수 있는지, 현지에서 사업을 하지 않았을 경우와 견주어 효과를 측정하려면 무엇을 비교해야 하는지 설명해 주세요.

### 스킬 미적용 답안

> 연방도로청의 세 도시 연구에서 추정된 충돌수정계수 0.87을 그대로 적용하면 충돌 감소율은 13%입니다. 이에 따라 같은 기간 사업을 하지 않을 때 예상 충돌이 북부 20건인 경우 감소 예상 건수는 **2.6건**, 남부 5건인 경우는 **0.65건**입니다. 사업비가 같고 목표가 예상 감소 건수의 최대화라면 **북부를 시범 지역으로 추천합니다**. 보행 선행신호는 보행자에게 차량 녹색보다 3~7초 먼저 길을 건너기 시작할 시간을 주어, 뒤이어 진입하는 선회 차량 운전자가 보행자를 더 잘 보고 양보하도록 도울 수 있습니다. 효과를 측정할 때는 사업 전후의 충돌 건수만 비교하지 말고, 같은 기간 사업을 하지 않았을 경우 북부에서 발생했을 충돌을 나타내는 신뢰할 만한 비교 기준과 시범사업 후 실제 충돌 건수를 비교해야 합니다.

### 스킬 적용 답안 · standard

> 선회 차량이 많은 교차로에 보행 선행신호를 적용하면 보행자가 차량보다 먼저 횡단을 시작해 선회 차량 운전자에게 더 잘 보일 수 있습니다. 위원회는 두 지역 중 어디에 시범사업을 해야 예상 충돌 감소 건수를 극대화할 수 있을까요? 연구의 충돌수정계수 0.87을 그대로 적용하면 북부는 예상 충돌 20건에서 2.6건 감소, 남부는 5건에서 0.65건 감소합니다. 따라서 **북부를 시범 지역으로 추천합니다.** 현지 효과는 북부에서 사업을 시행했을 때의 충돌 건수를 같은 기간 사업을 하지 않았을 경우의 예상치와 비교해 측정해야 합니다. *(감소 추정치 = 기준 충돌 건수 × (1−0.87); 이는 연구 계수를 그대로 적용한 가상 추정입니다.)*

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 북부와 남부의 예상 감소 건수를 각각 2.6건, 0.65건으로 계산한다. | 충족 | 충족 |
| 같은 비용으로 더 큰 절대 감소를 얻으려는 목적에 따라 북부를 권하고, 보행 신호가 앞서면 선회 차량 운전자가 보행자를 알아보기 쉬워지는 등의 이유를 제시한다. | 충족 | 충족 |
| 연구 결과를 현지에 적용할 수 있다는 가정하의 예상치임을 밝히고, 처리 교차로와 믿을 만한 현지 미도입 상황을 비교하는 측정 방법을 제안한다. | 미충족 | 미충족 |

**블라인드 검토** (X = 미적용, Y = 스킬 적용). 두 답 모두 북부를 권하고, 예상 감소량 2.6건과 0.65건 및 선회 차량에 보행자가 먼저 보이는 원리를 설명합니다. 두 답 모두 실제 충돌 건수와 미도입 시의 예상 건수를 비교하자고 하지만, 비슷한 미도입 교차로 등 현지에서 그 예상치를 뒷받침할 비교 대상을 제시하지 않습니다. X는 단순 전후 비교의 한계도 지적합니다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `1c5f170eb9d4` / `018c20fe2c01` / `b4944b8d1e69`.

</details>

## new-harts-rules

**영국 인구총조사 전시문에서 퍼센트포인트와 상대 차이를 어떻게 구분할까요?**

[English](EXAMPLES.md#new-harts-rules)

2026-11-08 · `new-harts-rules` 0.1.2 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [Office for National Statistics, Housing, England and Wales: Census 2021 (5 January 2023)](https://www.ons.gov.uk/peoplepopulationandcommunity/housing/bulletins/housingenglandandwales/census2021)

영국 통계청의 2021년 인구조사 자료는 자동차나 밴을 이용할 수 없는 가구의 비율을 제시합니다. 전시의 표기 지침과 편집 초안은 이 연습에서만 사용합니다.

**언어 적용 범위.** 영어 출판물 편집이 적용 대상이므로 전시 문장은 영어로 유지하고 분모와 표기 선택을 설명하는 편집 메모를 한국어로 새로 생성합니다.

### 질문

> 영국 교통 전시회에 실을 영어 문장과 한국어 편집 메모를 제출해 주세요. 영국 통계청(ONS) 원자료는 2021년 자동차나 승합차를 이용할 수 없는 가구의 비율이 런던 42.1%, 잉글랜드·웨일스 전체 23.3%라고 보고했습니다. 영어 초안은 ‘In “Housing, England and Wales: Census 2021”, ONS showed that 42.1% of Londoners lacked a car in 2021, 18.8 per cent more than across England and Wales.’입니다. 자료 제목은 한 글자도 바꾸지 말고, 영어 전시문은 본문의 백분율을 ‘per cent’로 적는 전시회 자체 표기 지침을 따르세요. 런던 비율과 전체 비율의 퍼센트포인트 차이, 전체 비율을 기준으로 한 상대 초과 비율(가장 가까운 정수 퍼센트)을 분명히 구분해 영어 문장을 고친 다음, 한국어로 두세 문장짜리 편집 메모를 써 주세요. 메모에서는 무엇을 분모로 삼았는지와 표기 판단의 근거를 설명하세요. New Hart’s Rules 원문 구절은 제공되지 않았습니다.

### 스킬 미적용 답안

> **English exhibition text**
>
> In “Housing, England and Wales: Census 2021”, ONS reported that 42.1 per cent of households in London could not use a car or van in 2021, 18.8 percentage points higher than the 23.3 per cent across England and Wales. This is an 81 per cent relative excess over the England and Wales rate.
>
> **편집 메모**
>
> 42.1%와 23.3%의 차이는 18.8퍼센트포인트이며, 상대 초과율은 잉글랜드·웨일스 전체 비율 23.3%를 분모로 계산해 `(42.1−23.3)÷23.3×100`으로 구한 약 81%입니다. 원자료의 지표는 자동차나 승합차를 이용할 수 없는 **가구**의 비율이므로 ‘Londoners lacked a car’ 대신 가구 기준으로 바로잡았습니다. 자료 제목은 그대로 두고, 전시회 표기 지침에 따라 본문 백분율은 ‘per cent’로 썼습니다.

### 스킬 적용 답안 · standard

> ### English exhibition text
>
> In “Housing, England and Wales: Census 2021”, ONS reported that 42.1 per cent of London households could not access a car or van in 2021, a difference of 18.8 percentage points from the 23.3 per cent across England and Wales. This is 81 per cent higher than the England and Wales rate.
>
> ### 편집 메모
>
> 분모를 구분했습니다. 18.8퍼센트포인트는 두 비율의 차이(42.1−23.3)이고, 상대 초과율 81퍼센트는 그 차이를 잉글랜드·웨일스 전체 비율 23.3으로 나눈 뒤 가장 가까운 정수로 반올림한 값입니다. 본문의 백분율은 전시회 자체 지침에 따라 ‘per cent’로 표기했으며, New Hart’s Rules 원문 구절이 제공되지 않아 해당 표기 판단을 그 책의 규칙으로 돌리지 않았습니다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 영문 제목 Housing, England and Wales: Census 2021을 그대로 보존하고 측정 대상이 자동차나 승합차를 이용할 수 없는 가구임을 유지한다. | 충족 | 충족 |
| 18.8퍼센트포인트 차이와 23.3%를 기준으로 한 약 81% 상대 초과를 구분한다. | 충족 | 충족 |
| 영어 본문의 백분율에 per cent를 사용하고, 한국어 편집 메모가 분모와 전시회의 표기 지침을 설명하며 확인하지 않은 책 규칙을 근거로 삼지 않는다. | 충족 | 충족 |

**블라인드 검토** (Y = 미적용, X = 스킬 적용). 두 답 모두 영어 전시문에서 자료 제목과 가구 단위를 지키고, 18.8퍼센트포인트와 약 81% 상대 초과를 구분합니다. 한국어 편집 메모에서 두 답 모두 23.3을 상대 비교의 분모로 제시하고 영어 본문의 ‘per cent’를 전시회 표기 지침으로 설명합니다. Y는 가구 단위로 초안을 고친 이유도 명시합니다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `984d898d4573` / `401e71e2374b` / `d56137d09d96`.

</details>

## nist-technical-publication

**NIST-F2의 어느 불확도를 줄이는 쪽이 더 효과적일까?**

[English](EXAMPLES.md#nist-technical-publication)

2026-11-08 · `nist-technical-publication` 0.1.3 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [Heavner et al., First Accuracy Evaluation of NIST-F2, Metrologia (2014)](https://www.nist.gov/publications/first-accuracy-evaluation-nist-f2)

NIST-F2 논문은 2013년 측정의 두 불확도 성분과 냉각 환경을 설명합니다. 독립성, 비용, 개선 후의 두 시나리오는 비교를 위한 가정입니다.

### 질문

> 측정 연구실이 NIST-F2의 어느 부분을 개선할지 결정할 수 있도록 간단한 한국어 기술 메모를 작성해 주세요. 2013년 7~8월 평가에서 통계적 A형 상대 주파수 불확도는 0.44 × 10⁻¹⁵, 계통적 B형 불확도는 0.11 × 10⁻¹⁵였습니다. 80 K 환경은 흑체복사에 따른 불확도를 50분의 1 미만으로 줄였고, B형에서는 마이크로파 진폭에 따른 영향이 가장 컸습니다. 이번 계산에 한해서 두 성분은 독립이라고 가정하고, 각각을 제곱해 합한 뒤 제곱근을 취해 결합하세요. 비용이 같은 두 가지 가상 방안, 즉 A형 성분만 절반으로 줄이는 방안과 B형 성분만 절반으로 줄이는 방안을 비교해 주세요. 현재의 결합 불확도와 두 방안에서 예상되는 결합 불확도를 구하고, 이 지표에 비춰 한 방안을 추천해 주세요. 냉각 효과만으로 전체 불확도가 50분의 1 미만이 됐다고 결론 낼 수 있는지도 설명해 주세요.

### 스킬 미적용 답안

> **기술 메모 — NIST-F2 불확도 개선 우선순위**
>
> 2013년 7~8월 평가의 상대 주파수 불확도는 A형이 $0.44\times10^{-15}$, B형이 $0.11\times10^{-15}$였습니다. 두 성분을 독립으로 보고 제곱합의 제곱근으로 결합하면 현재 불확도는
>
>
> $$
> \sqrt{0.44^2+0.11^2}\times10^{-15}\approx 0.454\times10^{-15}
> $$
>
>
> 입니다.
>
> 비용이 같은 두 가상 방안의 예상치는 다음과 같습니다.
>
> | 방안 | 변경 후 A형 | 변경 후 B형 | 결합 불확도 |
> |---|---:|---:|---:|
> | A형만 절반으로 감소 | 0.22 | 0.11 | $0.246\times10^{-15}$ |
> | B형만 절반으로 감소 | 0.44 | 0.055 | $0.443\times10^{-15}$ |
>
> 따라서 이 지표만 보면 **A형 성분을 절반으로 줄이는 방안**을 추천합니다. 결합 불확도가 약 $0.454$에서 $0.246\times10^{-15}$로 낮아지는 반면, B형만 줄이면 약 $0.443\times10^{-15}$에 그칩니다. B형에서는 마이크로파 진폭 영향이 가장 크지만, 현재 결합값에서는 더 큰 A형 성분을 줄이는 편이 효과가 큽니다.
>
> 80 K 환경이 흑체복사에 따른 **불확도**를 50분의 1 미만으로 줄였다는 사실만으로 전체 불확도도 50분의 1 미만이 됐다고 결론 낼 수는 없습니다. 이는 흑체복사 기여분에 관한 결과이며, 전체 결합 불확도에는 A형 통계 성분과 다른 B형 기여분도 포함됩니다.

<details>
<summary>원래 수식 표기로 보기</summary>

````text
**기술 메모 — NIST-F2 불확도 개선 우선순위**

2013년 7~8월 평가의 상대 주파수 불확도는 A형이 \(0.44\times10^{-15}\), B형이 \(0.11\times10^{-15}\)였습니다. 두 성분을 독립으로 보고 제곱합의 제곱근으로 결합하면 현재 불확도는

\[
\sqrt{0.44^2+0.11^2}\times10^{-15}\approx 0.454\times10^{-15}
\]

입니다.

비용이 같은 두 가상 방안의 예상치는 다음과 같습니다.

| 방안 | 변경 후 A형 | 변경 후 B형 | 결합 불확도 |
|---|---:|---:|---:|
| A형만 절반으로 감소 | 0.22 | 0.11 | \(0.246\times10^{-15}\) |
| B형만 절반으로 감소 | 0.44 | 0.055 | \(0.443\times10^{-15}\) |

따라서 이 지표만 보면 **A형 성분을 절반으로 줄이는 방안**을 추천합니다. 결합 불확도가 약 \(0.454\)에서 \(0.246\times10^{-15}\)로 낮아지는 반면, B형만 줄이면 약 \(0.443\times10^{-15}\)에 그칩니다. B형에서는 마이크로파 진폭 영향이 가장 크지만, 현재 결합값에서는 더 큰 A형 성분을 줄이는 편이 효과가 큽니다.

80 K 환경이 흑체복사에 따른 **불확도**를 50분의 1 미만으로 줄였다는 사실만으로 전체 불확도도 50분의 1 미만이 됐다고 결론 낼 수는 없습니다. 이는 흑체복사 기여분에 관한 결과이며, 전체 결합 불확도에는 A형 통계 성분과 다른 B형 기여분도 포함됩니다.
````

</details>

### 스킬 적용 답안 · standard

> **기술 메모 — NIST-F2 불확도 개선 방안**
>
> **목적.** 2013년 7~8월 평가의 상대 주파수 불확도를 바탕으로, 같은 비용의 두 가상 개선 방안 중 하나를 추천합니다. 두 성분은 이번 계산에서만 서로 독립이라고 가정하고, 제곱합 제곱근으로 결합했습니다.
>
> **기준과 계산.** 통계적 A형 성분은 0.44 × 10⁻¹⁵, 계통적 B형 성분은 0.11 × 10⁻¹⁵입니다. 현재 결합 불확도는 √(0.44² + 0.11²) = **0.454 × 10⁻¹⁵**입니다.
>
> | 가상 방안 | A형 상대 주파수 불확도 | B형 상대 주파수 불확도 | 예상 결합 불확도 |
> |---|---:|---:|---:|
> | A형만 절반으로 감소 | 0.22 × 10⁻¹⁵ | 0.11 × 10⁻¹⁵ | **0.246 × 10⁻¹⁵** |
> | B형만 절반으로 감소 | 0.44 × 10⁻¹⁵ | 0.055 × 10⁻¹⁵ | **0.443 × 10⁻¹⁵** |
>
> **권고.** 이 지표만 보면 **A형 성분을 절반으로 줄이는 방안**을 권합니다. 예상 결합 불확도는 약 0.454 × 10⁻¹⁵에서 0.246 × 10⁻¹⁵로 낮아집니다. B형에서 마이크로파 진폭 영향이 가장 컸다는 사실은 해당 효과를 우선 조사할 근거가 될 수 있지만, 주어진 비교에서는 B형 전체를 절반으로 줄여도 결합 불확도 변화가 작습니다. 이 권고는 명시된 두 가상 방안과 독립성 가정 아래에서만 성립합니다.
>
> **냉각 효과의 해석.** 80 K 환경은 흑체복사에 따른 불확도를 50분의 1 미만으로 줄였습니다. 이는 **흑체복사 기여분**에 관한 결과입니다. A형·B형을 포함한 전체 불확도가 50분의 1 미만으로 줄었다고 결론 내릴 수는 없습니다. 각 성분에서 흑체복사 기여가 차지하는 비율과 다른 기여분에 관한 정보가 주어지지 않았기 때문입니다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| A형과 B형의 값이 상대 주파수 불확도임을 구분하고, 독립이라는 가정 아래 현재 결합값이 약 0.454 × 10⁻¹⁵임을 계산한다. | 미충족 | 미충족 |
| A형만 절반이면 약 0.246 × 10⁻¹⁵, B형만 절반이면 약 0.443 × 10⁻¹⁵로 계산하고 같은 비용이라면 감소량이 큰 A형 개선을 선택한다. | 충족 | 충족 |
| 가상 방안의 예측값과 2013년 관측 결과를 구분한다. 50배 넘는 감소는 흑체복사 불확도에 한정하고, B형에서 주된 영향이 마이크로파 진폭임을 밝힌다. | 충족 | 충족 |

**블라인드 검토** (Y = 미적용, X = 스킬 적용). X는 현재값의 지수를 올바르게 적었지만 식 왼쪽에서 ×10⁻¹⁵를 빠뜨려 양변의 크기가 다르다. Y의 첫 식은 맞지만 권고문에서 현재값을 0.454로 적고 표의 변경 후 A·B 성분에도 ×10⁻¹⁵ 단위를 표시하지 않았다. 둘 다 예상 결합값 0.246 × 10⁻¹⁵와 0.443 × 10⁻¹⁵를 맞게 제시해 A형 개선을 택한다. 50배 넘는 감소를 흑체복사 기여분으로 한정하고 마이크로파 진폭을 B형의 주된 영향으로 식별한다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `33e35b943513` / `ff875254df61` / `8f7535325e38`.

</details>

## orwell-six-rules

**화성 기후 궤도선의 항법 추정은 단위 착오로 어떻게 빗나갔을까요?**

[English](EXAMPLES.md#orwell-six-rules)

2026-11-08 · `orwell-six-rules` 0.1.3 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [Cornelius J. Dennehy / NASA, Best Practices for the Design, Development, and Operation of Robust and Reliable Space Vehicle Guidance, Navigation, and Control Systems (NASA/TP–20230005922, April 2023)](https://ntrs.nasa.gov/api/citations/20230005922/downloads/20230005922.pdf)

NASA 자료는 지상 프로그램의 단위 불일치, 계획보다 낮아진 접근 궤도와 탐사선의 두 가지 가능한 최후를 설명합니다. 변환에 쓰는 충격량은 실제 임무 측정값이 아닙니다.

**언어 적용 범위.** 한국어에서는 군더더기를 줄이되 단위·조건·책임 주체를 정확히 보존하는 편집 원리를 적용합니다. 영어 단어 길이, 태, 어원에 관한 규칙은 한국어 규칙으로 옮기지 않습니다.

### 질문

> 박물관 설명문 초안을 간결한 한국어 한 문단으로 고쳐 주세요. 초안은 ‘운용상의 불일치가 170 km 추락을 야기했다. SM_FORCES가 추력기 충격량을 파운드힘초로 넘겼는데 항법 팀은 뉴턴초로 읽었다. 탐사선은 대기에서 불탔다’입니다. 실제 1999년 임무에서는 항법 궤도 추정의 오차가 누적돼 탐사선이 계획보다 약 170 km 더 낮게 화성에 접근했습니다. NASA는 대기 중 파괴됐는지 태양 궤도로 빠져나갔는지 판별하지 못했습니다. 단위 오류는 실제 측정값이 아닌 가상의 충격량 2파운드힘초로 보여 주세요. 이 문제에서 1파운드힘초는 약 4.45뉴턴초입니다. 항법 팀이 받아야 했던 값과 잘못 읽은 값의 차이를 계산하고, 이 예시와 실제 임무의 결과를 분리해 주세요.

### 스킬 미적용 답안

> 1999년 화성 기후 궤도선 임무에서는 항법 궤도 추정의 오차가 누적돼 탐사선이 계획보다 약 170 km 낮게 화성에 접근했습니다. NASA는 탐사선이 대기 중 파괴됐는지, 태양 궤도로 빠져나갔는지 판별하지 못했습니다. 단위 혼동을 설명하는 가상 예시로, SM_FORCES가 충격량 2파운드힘초를 전달했다면 항법 팀이 받아야 할 값은 약 8.90뉴턴초입니다(1파운드힘초 ≈ 4.45뉴턴초). 이를 2뉴턴초로 잘못 읽으면 차이는 약 6.90뉴턴초입니다.

### 스킬 적용 답안 · standard

> 실제 1999년 화성 기후 궤도선 임무에서는 항법 궤도 추정의 오차가 누적돼 탐사선이 계획보다 약 170 km 더 낮은 고도로 화성에 접근했습니다. NASA는 탐사선이 대기 중에 파괴됐는지, 태양 궤도로 빠져나갔는지 판별하지 못했습니다. 별도의 가상 예로, SM_FORCES가 충격량 2파운드힘초를 보냈다면 항법 팀은 약 8.90뉴턴초를 받아야 했습니다. 이를 2뉴턴초로 잘못 읽으면 약 6.90뉴턴초의 차이가 납니다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 가상 충격량은 약 8.9뉴턴초이고 항법 팀이 2뉴턴초로 읽었으므로 약 6.9뉴턴초 작게 읽었다고 설명한다(올바른 값이 약 4.45배라는 설명도 가능). | 충족 | 충족 |
| 예제 수치와 실제 임무를 구분하고, 약 170 km를 추락 거리로 쓰지 않으며 궤도 추정 오차가 쌓여 낮게 접근한 결과로 설명한다. | 충족 | 충족 |
| 박물관 독자가 원인과 결과를 따라갈 수 있게 한 문단에 쓰고 대기 중 파괴됐을 가능성과 태양을 도는 궤도로 빠져나갔을 가능성을 모두 남긴다. | 충족 | 충족 |

**블라인드 검토** (X = 미적용, Y = 스킬 적용). X와 Y 모두 가상 충격량 2파운드힘초를 약 8.90뉴턴초로 환산하고, 2뉴턴초로 읽었을 때의 차이를 약 6.90뉴턴초로 계산한다. 계획보다 약 170 km 낮게 접근한 실제 임무와 대기 중 파괴·태양 궤도로 탈출이라는 두 가능성을 보존한다. X는 환산 계수도 제시한다. 둘 다 실제 추력기 자료의 단위 혼동이 궤도 추정 오차를 일으켰다는 연결은 가상 예시로만 암시한다.

**기준 문구 정정.** 세 번째 기준의 초기 표현 “태양 궤도 이탈”은 방향이 모호해 영어 원기준과 한국어 질문에 맞춰 바로잡았습니다. 질문과 답안은 그대로 두고, 정정한 기준으로 답안의 조건을 가린 채 다시 판정했습니다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `90ee273da21c` / `4d416ff1a41c` / `d5a5549a64f2`.

</details>

## socratic-self-questioning

**핀란드 기본소득 실험에서 지역 주민 500명의 취업일수를 예측할 수 있을까요?**

[English](EXAMPLES.md#socratic-self-questioning)

2026-11-08 · `socratic-self-questioning` 0.1.2 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [Finnish Ministry of Social Affairs and Health and Kela, Results of the basic income experiment (6 May 2020)](https://valtioneuvosto.fi/en/-/1271139/perustulokokeilun-tulokset-tyollisyysvaikutukset-vahaisia-toimeentulo-ja-psyykkinen-terveys-koettiin-paremmaksi?languageId=en_US)

핀란드 정부 자료는 실험 참여 집단, 고용일수 차이, 2018년 제도 변경의 영향을 설명합니다. 지역 주민 500명에 대한 전망은 검토 대상인 가정입니다.

### 질문

> 정책 브리프 초안이 ‘지역 주민 500명에게 기본소득을 지급하면 취업일수가 3,000일 늘어난다’고 예측합니다. 핀란드의 2017~2018년 실험에서는 무작위로 선정된 실업급여 수급자 2,000명에게 매월 560유로를 지급했습니다. 2017년 11월부터 2018년 10월까지 지급 집단의 평균 취업일수는 78일로, 비교집단보다 6일 많았습니다. 첫해에는 집단 수준의 고용 효과가 없었습니다. 2018년 실업급여 제도 개편은 두 집단에 다르게 작용해, 연구진은 둘째 해에 기본소득만의 효과를 분리할 수 없었습니다. 비교집단 평균과 예측 총계가 나온 계산을 밝히고, 지역에 그 값을 적용하려면 어떤 가정이 필요할지 짚어 주세요. 브리프에 실을 한국어 한 문단으로 작성하세요.

### 스킬 미적용 답안

> 핀란드 실험에서 2017년 11월부터 2018년 10월까지 기본소득 집단의 평균 취업일수는 78일로 비교집단보다 6일 많았으므로, 비교집단 평균은 72일(78−6일)입니다. 이 6일 차이를 무작위 선정된 수급자 2,000명에게 적용하면 집단 전체에서 12,000일의 차이에 해당합니다. 초안의 3,000일은 그 차이를 지역 주민 500명에게 그대로 적용한 값(500×6일)으로 보입니다. 그러나 이는 첫해에 관찰된 집단 수준의 고용 효과가 없었다는 결과와 맞지 않으며, 둘째 해의 6일 차이도 제도 개편이 두 집단에 다르게 작용해 기본소득만의 효과로 분리할 수 없습니다. 따라서 지역에 3,000일을 적용하려면 주민 500명이 실험 참가자와 비슷한 대상이고, 참여·수급 조건과 노동시장 여건이 유사하며, 관찰된 6일 차이가 기본소득으로 인한 인과 효과이고 지역에서도 같은 기간·규모로 재현된다고 가정해야 합니다.

### 스킬 적용 답안 · standard

> 핀란드 실험 결과를 “지역 주민 500명에게 기본소득을 지급하면 취업일수가 3,000일 늘어난다”고 옮기려면, 먼저 6일의 기준이 무엇인지 밝혀야 합니다. 이 6일은 2017년 11월부터 2018년 10월까지 기본소득 집단의 평균 취업일수 78일과 비교집단 평균의 차이이므로, 비교집단 평균은 72일입니다. 3,000일은 1인당 6일 차이가 지역의 500명 모두에게 나타난다고 보고 500을 곱한 계산으로 추정됩니다. 그러나 실험 대상은 지역 주민 일반이 아니라 무작위 선정된 실업급여 수급자 2,000명이었고, 첫해에는 집단 수준의 고용 효과가 없었습니다. 둘째 해에는 실업급여 제도 개편이 두 집단에 다르게 작용해 기본소득만의 효과를 분리할 수 없었습니다. 따라서 3,000일은 확정된 지역 예측이 아니라, 지역의 500명에게도 실험의 6일 차이가 그대로 적용된다는 가정에 따른 추정치입니다. 이 가정이 타당하려면 지역 대상자의 고용 여건과 구성, 제도 환경이 실험 대상 및 비교 조건과 충분히 비슷해야 합니다.

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 비교집단 평균이 72일이며 3,000일은 관측된 6일 차이를 500명에게 곱한 외삽이지 지역에서 관측된 증가가 아님을 밝힌다. | 충족 | 충족 |
| 첫해 집단 수준의 효과가 없었다는 점과 2018년 제도 개편이 두 집단에 다르게 작용해 둘째 해 기본소득만의 효과를 분리할 수 없다는 점을 모두 설명한다. | 충족 | 충족 |
| 실험 참여자를 실업급여 수급자로 한정해 설명하고 일반 지역 주민에게 적용하려면 필요한 가정을 제시한다. 실험이 모든 연도에서 효과가 없었다고 단정하지 않는다. | 미충족 | 충족 |

**블라인드 검토** (X = 미적용, Y = 스킬 적용). 두 답 모두 비교집단 평균 72일과 500×6일의 외삽, 둘째 해 제도 개편을 구분합니다. Y는 실험 대상이 실업급여 수급자였다는 점을 명시합니다. X의 ‘수급자’는 무엇을 받던 집단인지 밝히지 않으며, 첫해 효과가 없었다는 관찰을 둘째 해 수치와 직접 충돌하는 결과처럼 서술합니다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `73849e50a54b` / `5f10922f41d2` / `d0baaafcd370`.

</details>

## steve-jobs-presentation

**인제뉴어티가 떠 있던 30초로 무엇을 알 수 있을까?**

[English](EXAMPLES.md#steve-jobs-presentation)

2026-11-08 · `steve-jobs-presentation` 0.1.1 · 한국어 · `gpt-6-luna`

### 사례와 출처

- [NASA, NASA’s Ingenuity Mars Helicopter Succeeds in Historic First Flight (April 19, 2021)](https://www.nasa.gov/news-release/nasas-ingenuity-mars-helicopter-succeeds-in-historic-first-flight/)

NASA의 첫 비행 발표는 Ingenuity의 전체 비행 시간, 제자리 비행 시간과 고도를 구분합니다. 주어진 수치만으로 상승 속도를 계산할 수 있는지는 별도로 판단해야 합니다.

### 질문

> 2021년 4월 19일을 기준으로 박물관에서 발표할 짧은 한국어 발화 세 대목을 써 주세요. 인제뉴어티는 화성의 라이트 브라더스 비행장에서 자율 비행으로 약 3 m까지 올라가 30초간 제자리 비행을 했고, 이륙 후 39.1초에 착륙했습니다. 다른 행성에서 동력을 사용해 제어 비행을 할 수 있음을 보여 준 비행입니다. 준비 중인 슬라이드에는 3 m를 전체 비행 시간으로 나눈 값을 ‘평균 상승 속도’라고 적었습니다. 이 지표를 쓸지 결정해 주세요. 비행 시간 중 제자리 비행의 비율을 제시하고 나머지 시간으로 상승 속도를 알아낼 수 있는지 설명해 주세요. 비행 자료를 검토한 뒤 연구진이 다음 시험에 대해 무엇을 결정할 수 있는지로 마무리하세요. 후속 비행이 이미 성공했다고 가정하지 마세요.

### 스킬 미적용 답안

> 인제뉴어티는 2021년 4월 19일 화성의 라이트 브라더스 비행장에서 자율 비행으로 약 3미터까지 올라갔습니다. 이번 비행은 다른 행성에서 동력을 사용해 제어 비행을 할 수 있음을 보여 줬습니다.
>
> 전체 비행 시간 39.1초 가운데 약 30초, 즉 약 77%는 제자리 비행이었습니다. 따라서 3미터를 전체 시간으로 나눈 값은 상승 속도가 아니므로 슬라이드의 ‘평균 상승 속도’로 쓰지 않는 편이 맞습니다.
>
> 제자리 비행 시간을 빼면 약 9.1초가 남지만, 이 시간에는 상승뿐 아니라 하강과 착륙도 포함됩니다. 그러므로 그 값만으로 상승 속도를 알아낼 수는 없습니다. 연구진은 비행 자료를 검토해 기체가 어떻게 작동했는지 평가하고, 다음 시험의 목표와 비행 계획을 정할 수 있습니다.

### 스킬 적용 답안 · standard

> **세 대목**
>
> “인제뉴어티는 화성의 라이트 브라더스 비행장에서 자율 비행을 했습니다. 화성에서도 동력을 사용해 제어 비행을 할 수 있음을 보여 준 비행입니다.”
>
> “기체는 약 3 m까지 올라가 30초간 제자리 비행을 한 뒤, 이륙 후 39.1초에 착륙했습니다. 전체 비행 시간으로 높이 3 m를 나눈 값은 약 0.077 m/s지만, 이 값은 ‘평균 상승 속도’가 아니라 **전체 비행 시간에 대한 높이의 비율**입니다. 제자리 비행은 전체 시간의 약 76.7%입니다. 그 시간을 빼면 약 9.1초가 남지만, 그 시간에는 하강과 착륙도 포함됩니다. 따라서 이 정보만으로 상승에 걸린 시간이나 상승 속도를 알아낼 수는 없습니다.”
>
> “비행 자료를 검토하면 연구진은 실제 상승·하강 구간과 기체의 성능을 평가해 다음 시험에서 무엇을 바꿀지, 또는 어떤 조건으로 시험할지 결정할 수 있습니다. 이 비행은 동력 제어 비행의 가능성을 보여 줬지만, 후속 비행의 성공을 미리 말해 주지는 않습니다.”
>
> **방법 상태:** Jobs-inspired presentation structure · standard

### 두 답안의 차이

| 실행 전에 정한 기준 | 스킬 미적용 | 스킬 적용 |
| --- | --- | --- |
| 화성 최초의 자율 동력·제어 비행이라는 의미와 약 3 m 높이를 유지하고, 30초 제자리 비행과 전체 39.1초를 구분한다. | 충족 | 충족 |
| 제자리 비행은 약 77%이며 남은 9.1초에는 상승과 하강이 들어감을 설명한다. 전체 시간에서 상승 속도를 유도하는 계산을 배척한다. | 충족 | 충족 |
| 관객에게 말할 짧은 세 대목으로 구성하고, 앞으로의 성공을 단언하지 않고 비행 자료 검토가 다음 시험을 정하는 근거라고 마무리한다. | 충족 | 미충족 |

**블라인드 검토** (X = 미적용, Y = 스킬 적용). 두 답 모두 30초는 전체 39.1초의 약 77%이고, 남은 9.1초에는 하강도 포함돼 상승 속도를 구할 수 없다고 설명합니다. X 쪽은 이 판단과 다음 시험 결정을 세 단락으로 전합니다. Y 쪽은 계산 근거를 자세히 쓰지만 둘째 대목이 길고 발표와 별개인 방법 상태까지 붙였습니다.

<details>
<summary>실행 기록</summary>

각 답안은 Codex CLI 0.167.0, low 추론 설정의 별도 임시 읽기 전용 세션에서 생성했습니다. 같은 문항의 다른 답안이나 다른 언어의 답안은 입력하지 않았습니다.

SHA-256 앞 12자리 (스킬 지침 / 미적용 원문 / 적용 원문): `172a5e6964a7` / `ff6014188315` / `e98f1437f81d`.

</details>
