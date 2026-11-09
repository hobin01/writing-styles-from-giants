# 화성의 통신 지연이 1분 늘면 지구는 얼마나 더 기다릴까?

[English](standard.md) · [light](light.ko.md) · **standard** · [strict](strict.ko.md)

### 질문

> 지구에서 퍼서비어런스 탐사차까지 신호가 가는 데는 편도로 약 3~22분이 걸린다. 다음은 가상의 교신 일정이다. 지구가 0분에 신호를 보내면 탐사차는 신호를 받은 뒤 답신을 준비하는 데 10분이 걸린다. 송신은 25분, 50분, 75분처럼 25분 간격으로만 시작할 수 있고, 준비가 정확히 그 시각에 끝나면 바로 송신할 수 있다. 돌아오는 신호도 가는 신호와 같은 시간이 걸린다. 편도 지연이 15분에서 16분으로 늘면 지구가 답신을 받는 시각이 왜 1분보다 더 늦어질까?

**출처** · [NASA/JPL, Speaking Percy's Language: How to Talk so Perseverance Will Listen](https://science.nasa.gov/blog/speaking-percys-language-how-to-talk-so-perseverance-will-listen/)

### 스킬 적용

[HTML 파일 · 내려받아 브라우저에서 열기](standard.ko.html)

````html
<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>편도 지연이 1분 늘 때 답신이 더 늦어지는 이유</title>
<style>
  :root { color-scheme: light; font-family: system-ui, -apple-system, "Malgun Gothic", sans-serif; }
  body { margin: 0; padding: 1.25rem; color: #172033; background: #f5f7fb; line-height: 1.55; }
  main { max-width: 850px; margin: auto; padding: clamp(1rem, 4vw, 2rem); background: white; border: 1px solid #dbe2ee; border-radius: 1rem; }
  h1 { font-size: clamp(1.4rem, 4vw, 2rem); line-height: 1.25; }
  .table-wrap { overflow-x: auto; }
  table { width: 100%; border-collapse: collapse; margin: 1rem 0 .5rem; }
  th, td { padding: .7rem; border: 1px solid #dbe2ee; text-align: left; vertical-align: top; }
  th { background: #edf2fa; }
  caption { text-align: left; font-weight: 650; padding-bottom: .5rem; }
  .equation { font-weight: 700; margin: .5rem 0 1rem; }
  fieldset { margin: 1.25rem 0; border: 1px solid #cbd5e1; border-radius: .75rem; padding: 1rem; }
  legend { font-weight: 700; padding: 0 .35rem; }
  .choices { display: flex; flex-wrap: wrap; gap: .75rem 1.25rem; }
  label { cursor: pointer; }
  #explanation { margin-top: .85rem; padding: .85rem 1rem; border-left: 4px solid #2563eb; background: #eff6ff; border-radius: .25rem; }
  .note { color: #475569; }
  @media (max-width: 520px) { body { padding: .5rem; } th, td { padding: .5rem; } }
</style>
</head>
<body>
<main>
  <h1>편도 지연이 1분 늘 때 답신은 왜 더 늦어질까?</h1>
  <p>가상의 일정에서 지구는 0분에 신호를 보내고, 탐사차는 받은 뒤 답신 준비에 10분을 씁니다. 송신은 25분 간격으로만 시작할 수 있으며, 준비가 송신 시각에 맞춰 끝나면 바로 보낼 수 있습니다.</p>

  <div class="table-wrap">
    <table>
      <caption>편도 지연에 따른 답신 일정 (단위: 분)</caption>
      <thead>
        <tr>
          <th scope="col">편도 지연</th>
          <th scope="col">탐사차가 받는 시각</th>
          <th scope="col">준비 완료 시각</th>
          <th scope="col">가능한 첫 송신 시각</th>
          <th scope="col">지구가 답신을 받는 시각</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">15분</th>
          <td>0 + 15 = 15</td>
          <td>15 + 10 = 25</td>
          <td>25</td>
          <td>25 + 15 = 40</td>
        </tr>
        <tr>
          <th scope="row">16분</th>
          <td>0 + 16 = 16</td>
          <td>16 + 10 = 26</td>
          <td>50</td>
          <td>50 + 16 = 66</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p class="equation">답신 도착 시각 차이: 66분 − 40분 = 26분</p>

  <fieldset>
    <legend>편도 지연 사례를 선택해 원인을 확인하세요</legend>
    <div class="choices">
      <label><input type="radio" name="case" value="15" checked> 15분 지연</label>
      <label><input type="radio" name="case" value="16"> 16분 지연</label>
    </div>
    <p id="explanation" aria-live="polite">준비가 송신 가능 시각에 맞춰 끝나므로 탐사차는 바로 답신을 보냅니다.</p>
  </fieldset>

  <p class="note">편도 지연이 16분일 때는 준비가 첫 송신 가능 시각을 지나 끝납니다. 다음 송신 기회를 기다려야 하므로, 왕복 전파 시간의 증가에 더해 일정 간격 때문에 추가 지연이 생깁니다.</p>
</main>
<script>
  const explanations = {
    "15": "준비가 송신 가능 시각에 맞춰 끝나므로 탐사차는 바로 답신을 보냅니다.",
    "16": "준비가 첫 송신 가능 시각을 놓친 뒤 끝나므로, 탐사차는 다음 25분 간격의 송신 기회까지 기다립니다."
  };
  document.querySelectorAll('input[name="case"]').forEach((control) => {
    control.addEventListener("change", (event) => {
      const message = explanations[event.target.value];
      if (message) document.getElementById("explanation").textContent = message;
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
