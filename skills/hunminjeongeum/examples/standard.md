# How much of a Seoul journey can a better map shorten?

[한국어](standard.ko.md)

2026-11-08 · `hunminjeongeum` 0.1.1 · English · `gpt-6-luna`

### Case and sources

- [서울특별시, 시민의 발, 디자인을 입다…서울시, 지하철 노선도 40년 만에 변경 (2023-09-13)](https://news.seoul.go.kr/culture/archives/520933). Design release on interchange markings, the circular Line 2 reference, and maximum time reduction in the 20s–30s domestic/foreign eye-tracking experiment.

### Prompt

> Explain in English in at most four sentences to someone taking the Seoul subway for the first time why the city proposed a new map in 2023 and what its numbers mean. On the old map, transfers were hard to distinguish from ordinary stations. The redesign joins the colours of connecting lines in one transfer symbol. In an eye-tracking experiment with Korean and international participants in their twenties and thirties, the time to locate a transfer on the map fell by up to about 69%. For illustration, assume a passenger spends 100 seconds using the old map and then 12 minutes riding the train. If that maximum reduction applied to map reading, what would the new combined time be? Someone proposes saying the whole journey becomes 69% faster.

### Without the skill

> Seoul proposed the map in 2023 because transfers were hard to spot on the old one. The new map combines the colours of connecting lines in a single transfer symbol, and in an eye-tracking experiment, Korean and international participants in their twenties and thirties found transfers up to about 69% faster. If finding a transfer took 100 seconds before, a 69% reduction would bring map-reading time to 31 seconds; with a 12-minute train ride, the combined time would be 12 minutes 31 seconds. So it would be misleading to say the whole journey becomes 69% faster: only the map-reading time is reduced in this example.

### With the skill at standard

> On Seoul’s old subway map, transfers were hard to distinguish from ordinary stations, so the city proposed a redesign in 2023 to make transfers easier to spot. It joins the colours of connecting lines in one transfer symbol; in an eye-tracking experiment with Korean and international participants in their twenties and thirties, the time to locate a transfer on the map fell by up to about 69%. In the example, a 69% reduction cuts 100 seconds of map reading to 31 seconds; adding the unchanged 12-minute ride gives a total of 12 minutes 31 seconds. So “the whole journey becomes 69% faster” would be inaccurate: the reported reduction applies to finding transfers on the map, not to the train ride or total journey.

### What changed

| Check fixed before generation | Without | Standard |
| --- | --- | --- |
| Opens by connecting the passenger's difficulty finding transfers to the linked line-colour transfer symbol. | Met | Met |
| Computes about 31 seconds looking at the new map and about 12 minutes 31 seconds for the hypothetical total (train ride remains 12 minutes). | Met | Met |
| Makes clear the up-to-about-69% result was for locating transfers in the map experiment, not a measured 69% reduction of actual whole journeys. | Met | Met |

**Masked review** (Y = baseline; X = standard). Both explain the transfer symbol and correctly combine 31 seconds of map reading with an unchanged 12-minute ride. X describes the measured quantity as time falling by up to about 69%. Y calls it finding transfers ‘69% faster’, which is less precise than a 69% reduction in time, then gives the correct calculation and limits the result to the map task.

<details>
<summary>Run record</summary>

Each arm was a separate ephemeral read-only Codex CLI 0.167.0 session with low reasoning effort. Neither session was given the other answer or an answer in the other language.

SHA-256 prefixes (entrypoint / baseline answer / standard answer): `41f1b8c56caa` / `a341d5a5f712` / `43a2e90ed3f6`.

</details>
