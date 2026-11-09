# 화성의 통신 지연이 1분 늘면 지구는 얼마나 더 기다릴까?

[English](strict.md) · [light](light.ko.md) · [standard](standard.ko.md) · **strict**

### 질문

> 지구에서 퍼서비어런스 탐사차까지 신호가 가는 데는 편도로 약 3~22분이 걸린다. 다음은 가상의 교신 일정이다. 지구가 0분에 신호를 보내면 탐사차는 신호를 받은 뒤 답신을 준비하는 데 10분이 걸린다. 송신은 25분, 50분, 75분처럼 25분 간격으로만 시작할 수 있고, 준비가 정확히 그 시각에 끝나면 바로 송신할 수 있다. 돌아오는 신호도 가는 신호와 같은 시간이 걸린다. 편도 지연이 15분에서 16분으로 늘면 지구가 답신을 받는 시각이 왜 1분보다 더 늦어질까?

**출처** · [NASA/JPL, Speaking Percy's Language: How to Talk so Perseverance Will Listen](https://science.nasa.gov/blog/speaking-percys-language-how-to-talk-so-perseverance-will-listen/)

### 스킬 적용

[HTML 파일 · 내려받아 브라우저에서 열기](strict.ko.html)

````html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>편도 지연 1분 증가가 답신에 미치는 영향</title>
  <style>
    :root { color-scheme: light; font-family: system-ui, -apple-system, "Noto Sans KR", sans-serif; }
    body { margin: 0; background: #f4f7fb; color: #172238; line-height: 1.6; }
    main { box-sizing: border-box; max-width: 900px; margin: 0 auto; padding: 2rem 1rem 3rem; }
    h1 { font-size: clamp(1.45rem, 4vw, 2rem); line-height: 1.3; }
    .lead, .note, .cause, .subtraction { background: white; border: 1px solid #d9e2ef; border-radius: 12px; padding: 1rem; }
    .lead { border-left: 5px solid #3874d8; }
    .table-wrap { overflow-x: auto; margin: 1rem 0 .5rem; }
    table { border-collapse: collapse; width: 100%; min-width: 650px; background: white; }
    th, td { border: 1px solid #d9e2ef; text-align: left; padding: .7rem; vertical-align: top; }
    th { background: #eaf0f8; }
    .subtraction { font-weight: 650; margin: .75rem 0; }
    fieldset { margin: 1.25rem 0; padding: 1rem; border: 1px solid #c8d5e7; border-radius: 12px; }
    legend { font-weight: 700; padding: 0 .35rem; }
    label { display: inline-flex; gap: .5rem; align-items: center; margin: .25rem 1rem .25rem 0; }
    input { accent-color: #245fc4; }
    .cause { min-height: 3.5rem; }
    .small { color: #4a5870; font-size: .94rem; }
    @media (max-width: 520px) {
      main { padding: 1.25rem .75rem 2rem; }
      .table-wrap { margin-left: -.25rem; margin-right: -.25rem; }
    }
  </style>
</head>
<body>
<main>
  <h1>편도 지연이 1분 늘었는데, 답신은 왜 1분보다 더 늦을까?</h1>
  <p class="lead">탐사차의 답신 준비가 끝나는 시각과 다음 송신 가능 시각 사이에 25분 간격의 경계가 있다. 준비가 그 경계를 넘으면, 답신은 다음 송신 기회를 기다려야 한다.</p>

  <h2>가상 교신 일정</h2>
  <p class="small">지구는 0분에 송신한다. 탐사차는 신호를 받은 뒤 답신을 준비하는 데 10분이 걸리고, 송신은 25분 간격으로 시작한다. 편도 지연은 양방향에 동일하게 적용된다.</p>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th scope="col">편도 지연</th>
          <th scope="col">탐사차가 신호를 받음</th>
          <th scope="col">답신 준비 완료</th>
          <th scope="col">탐사차가 답신 송신</th>
          <th scope="col">지구가 답신 수신</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">15분</th>
          <td>0 + 15 = 15분</td>
          <td>15 + 10 = 25분</td>
          <td>25분<br><span class="small">정확히 송신 시각에 준비 완료</span></td>
          <td>25 + 15 = 40분</td>
        </tr>
        <tr>
          <th scope="row">16분</th>
          <td>0 + 16 = 16분</td>
          <td>16 + 10 = 26분</td>
          <td>50분<br><span class="small">25분 송신 기회를 지나침</span></td>
          <td>50 + 16 = 66분</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p class="subtraction">66분 − 40분 = 26분</p>

  <fieldset>
    <legend>사례를 선택해 원인을 확인하세요</legend>
    <label><input type="radio" name="case" value="15" checked> 편도 지연 15분</label>
    <label><input type="radio" name="case" value="16"> 편도 지연 16분</label>
  </fieldset>
  <section class="cause" id="cause" aria-live="polite" aria-atomic="true">
    <strong>15분 사례:</strong> 준비가 송신 경계에 맞춰 끝나므로 탐사차는 곧바로 답신을 보낼 수 있다.
  </section>

  <p class="note small">이 일정에서는 15분 지연일 때 준비가 송신 경계에 정확히 맞지만, 16분 지연일 때는 그 경계를 넘는다. 그 결과 답신은 다음 송신 기회까지 기다리며, 왕복 전파 지연 증가분에 대기 시간이 더해진다.</p>
</main>
<script>
  const explanations = {
    "15": "15분 사례: 준비가 송신 경계에 맞춰 끝나므로 탐사차는 곧바로 답신을 보낼 수 있다.",
    "16": "16분 사례: 준비가 25분 송신 경계를 지나 끝나므로 탐사차는 다음 송신 기회까지 기다려야 한다."
  };
  const cause = document.getElementById("cause");
  document.querySelectorAll('input[name="case"]').forEach((control) => {
    control.addEventListener("change", () => {
      if (control.checked && Object.hasOwn(explanations, control.value)) {
        cause.textContent = explanations[control.value];
      }
    });
  });
</script>
</body>
</html>
````

### 스킬 미적용

> 편도 지연이 15분이면 탐사차는 15분에 신호를 받고, 10분 뒤인 25분에 답신을 보낼 수 있습니다. 지구에는 40분에 답신이 도착합니다.
>
> 지연이 16분이면 신호가 16분에 도착하고 준비는 26분에 끝납니다. 하지만 송신은 25분 간격으로만 시작할 수 있으므로, 다음 송신 시각인 50분까지 기다려야 합니다. 답신은 지구에 66분에 도착합니다.
>
> 편도 지연은 1분 늘었지만 송신 시작이 25분에서 50분으로 밀려, 답신 도착은 26분 늦어집니다.
