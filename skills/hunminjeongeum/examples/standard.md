# How much of a Seoul journey can a better map shorten?

2026-11-08 · `hunminjeongeum` 0.1.1 at first pass · `gpt-6-luna` · Codex CLI 0.167.0

### Case and sources

- [서울특별시, 시민의 발, 디자인을 입다…서울시, 지하철 노선도 40년 만에 변경 (2023-09-13)](https://news.seoul.go.kr/culture/archives/520933). Design release on interchange markings, the circular Line 2 reference, and maximum time reduction in the 20s–30s domestic/foreign eye-tracking experiment.

**Reasoning task.** Apply a relative reduction to the measured component of a journey, recombine durations and judge whether the headline generalizes from an eye-tracking task.

### Prompt

> 서울 지하철을 처음 타는 사람에게, 서울시가 2023년에 노선도를 고치려 한 이유와 숫자의 의미를 한국어 네 문장 이내로 설명해 주세요. 기존 지도에서는 환승역이 일반역과 잘 구분되지 않았고, 개선안은 환승할 노선들의 색을 한 표시에 연결했어요. 20~30대 내국인·외국인의 시선 추적 실험에서 환승역 길 찾기 시간이 최대 약 69% 줄었어요. 설명용으로 어떤 승객이 예전 지도에서 길을 찾는 데 100초, 이후 열차를 타는 데 12분이 걸린다고 가정해요. 지도 보는 시간에 그 최대 감소율을 적용한다면 지도를 보고 열차를 타는 데 걸리는 합계는 얼마일까요? 누군가 ‘여정 전체가 69% 빨라진다’고 소개하려고 해요.

### Without a skill

> 서울시는 기존 노선도에서 환승역이 일반역과 잘 구분되지 않아 길을 찾기 어려운 점을 개선하려 했고, 개선안은 환승 노선들의 색을 하나의 표시에 연결했습니다. 20~30대 내국인·외국인 실험에서 환승역 길 찾기 시간이 최대 약 69% 줄었다는 뜻이지, 모든 승객이나 전체 여정의 시간이 69% 줄었다는 뜻은 아닙니다. 예전 지도에서 100초 걸렸다고 가정하면 지도 보는 시간은 31초로 줄고, 열차 탑승까지의 12분을 더하면 합계는 12분 31초입니다. 따라서 ‘여정 전체가 69% 빨라진다’고 소개하면 실험 결과의 범위를 과장하게 됩니다.

### With the skill at standard

> 서울 지하철을 처음 타면 기존 노선도에서 환승역이 일반역과 잘 구분되지 않아 갈아탈 곳을 찾기 어려울 수 있어요. 서울시는 2023년 개선안에서 환승할 노선들의 색을 하나의 표시에 연결해 환승역을 알아보기 쉽게 하려 했고, 20~30대 내국인·외국인의 시선 추적 실험에서는 환승역 길 찾기 시간이 최대 약 69% 줄었어요. 설명용 가정에서 지도 보는 시간 100초에 이 감소율을 적용하면 31초가 되고, 열차를 타는 데 걸리는 12분을 더한 합계는 **12분 31초**예요. 이 계산은 지도 보는 시간에만 적용되므로, ‘여정 전체가 69% 빨라진다’고 말할 근거는 없습니다.

### First-pass assessment

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Opens by connecting the passenger's difficulty finding transfers to the linked line-colour transfer symbol. | Met | Met |
| Computes about 31 seconds looking at the new map and about 12 minutes 31 seconds for the hypothetical total (train ride remains 12 minutes). | Missed | Met |
| Makes clear the up-to-about-69% result was for locating transfers in the map experiment, not a measured 69% reduction of actual whole journeys. | Met | Met |

Both explain the transfer symbol and calculate 31 seconds of map reading and a total of 12 minutes 31 seconds; neither assigns the 69% reduction to the whole journey. The skill answer correctly describes the 12 minutes as the ride. The baseline calls it the time ‘until boarding’ (탑승까지), changing what that interval represents despite getting the sum right.

**차이.** 둘 다 지도 보는 시간 31초와 합계 12분 31초를 계산했고, 69%는 지도 실험의 수치라고 밝힙니다. 스킬 답은 12분을 열차를 타는 시간으로 유지합니다. 미적용 답은 이를 ‘탑승까지의 12분’이라고 바꿔, 합계는 맞지만 그 시간이 의미하는 구간이 달라졌습니다.
