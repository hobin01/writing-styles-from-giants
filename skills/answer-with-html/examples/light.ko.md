# 화성의 통신 지연이 1분 늘면 지구는 얼마나 더 기다릴까?

[English](light.md) · [standard](standard.ko.md) · [strict](strict.ko.md)

[질문과 출처](standard.ko.md#질문)

### Light

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
