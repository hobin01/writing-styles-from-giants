# 화성의 통신 지연이 1분 늘면 지구는 얼마나 더 기다릴까?

[English](light.md) · **light** · [standard](standard.ko.md) · [strict](strict.ko.md)

### 질문

> 지구에서 퍼서비어런스 탐사차까지 신호가 가는 데는 편도로 약 3~22분이 걸린다. 다음은 가상의 교신 일정이다. 지구가 0분에 신호를 보내면 탐사차는 신호를 받은 뒤 답신을 준비하는 데 10분이 걸린다. 송신은 25분, 50분, 75분처럼 25분 간격으로만 시작할 수 있고, 준비가 정확히 그 시각에 끝나면 바로 송신할 수 있다. 돌아오는 신호도 가는 신호와 같은 시간이 걸린다. 편도 지연이 15분에서 16분으로 늘면 지구가 답신을 받는 시각이 왜 1분보다 더 늦어질까?

**출처** · [NASA/JPL, Speaking Percy's Language: How to Talk so Perseverance Will Listen](https://science.nasa.gov/blog/speaking-percys-language-how-to-talk-so-perseverance-will-listen/)

### 스킬 적용

[HTML 파일 · 내려받아 브라우저에서 열기](light.ko.html)

````html
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>편도 지연 1분이 답신 시각을 더 늦추는 이유</title>
  <style>
    body { max-width: 760px; margin: 2rem auto; padding: 0 1rem; font: 1rem/1.6 system-ui, sans-serif; color: #182230; }
    h1 { font-size: 1.5rem; line-height: 1.3; }
    table { width: 100%; border-collapse: collapse; margin: 1rem 0; }
    th, td { border: 1px solid #bac5d1; padding: .65rem; text-align: left; overflow-wrap: anywhere; }
    th { background: #f0f4f8; }
    fieldset { border: 1px solid #bac5d1; border-radius: .5rem; margin: 1rem 0; padding: .8rem 1rem; }
    label { margin-right: 1rem; }
    output { display: block; padding: .8rem; border-left: 4px solid #287a63; background: #f0f8f5; }
  </style>
</head>
<body>
  <main>
    <h1>편도 지연이 1분 늘었는데, 답신은 왜 더 늦어질까?</h1>
    <p>가상 일정에서 지구는 0분에 신호를 보내고, 퍼서비어런스는 신호를 받은 뒤 답신 준비에 10분을 쓴다. 답신 송신은 25분 간격 시각에만 시작할 수 있으며, 준비가 그 시각에 끝나면 바로 송신한다.</p>

    <table>
      <thead>
        <tr>
          <th scope="col">편도 지연</th>
          <th scope="col">탐사차 수신</th>
          <th scope="col">준비 완료</th>
          <th scope="col">답신 송신</th>
          <th scope="col">지구 수신</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">15분</th>
          <td>0 + 15 = 15분</td>
          <td>15 + 10 = 25분</td>
          <td>25분</td>
          <td>25 + 15 = 40분</td>
        </tr>
        <tr>
          <th scope="row">16분</th>
          <td>0 + 16 = 16분</td>
          <td>16 + 10 = 26분</td>
          <td>50분</td>
          <td>50 + 16 = 66분</td>
        </tr>
      </tbody>
    </table>

    <p>지구 수신 시각 차이: 66분 − 40분 = 26분.</p>

    <fieldset>
      <legend>편도 지연 사례를 선택해 원인을 확인하세요</legend>
      <label><input type="radio" name="case" value="15" checked> 15분</label>
      <label><input type="radio" name="case" value="16"> 16분</label>
    </fieldset>
    <output id="reason" aria-live="polite">15분 사례: 준비가 송신 가능 시각에 맞춰 끝나므로, 첫 번째 송신 기회를 이용합니다.</output>
    <p>16분 사례에서는 준비 완료가 첫 송신 시각을 지나쳐, 다음 송신 기회까지 기다려야 합니다. 그 결과 송신 일정의 경계가 넘어가며 지구의 답신 수신이 크게 늦어집니다.</p>
  </main>
  <script>
    const reason = document.getElementById("reason");
    document.querySelectorAll('input[name="case"]').forEach((control) => {
      control.addEventListener("change", () => {
        reason.textContent = control.value === "15"
          ? "15분 사례: 준비가 송신 가능 시각에 맞춰 끝나므로, 첫 번째 송신 기회를 이용합니다."
          : "16분 사례: 준비가 첫 송신 가능 시각을 1분 지나 끝나므로, 다음 송신 기회까지 기다려야 합니다.";
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
