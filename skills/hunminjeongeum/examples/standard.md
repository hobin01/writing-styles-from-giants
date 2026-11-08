# Finding a transfer on Seoul’s redesigned subway map

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
