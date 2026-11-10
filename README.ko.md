# writing-styles-from-giants

[English](README.md)

AI한테 “쉽게 설명해 줘”라고 하면, 제가 궁금했던 부분까지 빼고 짧게 끝낼 때가 있어요. 다섯 살 아이에게 자전거 브레이크를 설명하는 것과, 엔지니어에게 브레이크의 작동 원리를 설명하는 건 꽤 다른 일이잖아요. 그래서 **누구에게, 어떤 방식으로 설명할지** 직접 고를 수 있게 만들었습니다. 앞선 사람들의 글쓰기 방식을 제 질문에 빌려 쓴다는 뜻에서 이름도 ‘거인의 어깨 위에 선다’는 말에서 따왔어요.

물에 뜬 얼음이 녹으면 수위가 달라질까요? GPT-6 Luna가 그냥 답했을 때와 ELI5를 적용했을 때의 설명을 한 페이지에서 읽어 보세요. 두 DNS 리졸버가 왜 다른 답을 주는지 물어본 파인만 예제도 있습니다. [얼음 예제](skills/eli5/examples/standard.ko.md) · [DNS 예제](skills/feynman-technique/examples/standard.ko.md)

각 예제에는 질문과 두 답변이 있습니다. 같은 질문에 스킬 없이 받은 답 하나와 `light`, `standard`, `strict`로 받은 답 하나씩을 실었어요. 어느 레벨을 열어도 스킬 없이 받은 답이 같아서 바로 비교할 수 있습니다. 한국어와 영어는 새 대화에서 각 언어로 직접 물었습니다. [한국어 예제](EXAMPLES.ko.md) · [영어 예제](EXAMPLES.md)

## 내 에이전트에 설치하기

### 릴리스를 복제하고 `install.py` 실행하기

Git과 Python 3.10 이상이 있으면 저장소를 계속 보관할 위치에 복제하세요. 설치기는 `PATH`에서 에이전트 명령을 찾습니다. 목록에서 쓸 도구의 이름을 `codex claude`처럼 공백으로 구분해 입력하세요. 빈 줄에서 Enter를 누르면 취소됩니다. 아래 명령으로 연결하면 모든 프로젝트에서 사용할 수 있습니다.

```sh
git clone --branch v0.2.0 --depth 1 https://github.com/hobin01/writing-styles-from-giants.git
cd writing-styles-from-giants
python3 install.py install --global --link
```

`--link`는 에이전트의 스킬 폴더에 복제한 저장소를 가리키는 심볼릭 링크를 만듭니다. 저장소를 같은 위치에 두세요. 저장소의 스킬을 수정하면 연결된 에이전트에도 반영됩니다. 독립 복사본이 필요하거나 시스템에서 심볼릭 링크 생성을 제한하면 `--link`를 빼세요.

**한 프로젝트에서만** 쓰려면 그 프로젝트에서 터미널을 열고 설치 파일의 전체 경로를 지정하세요. 아래 명령처럼 Codex를 직접 지정하면 스크립트로 설치하거나 도구가 `PATH`에 없을 때도 사용할 수 있습니다.

```sh
python3 "/path/to/writing-styles-from-giants/install.py" install --host codex --link
```

다른 도구를 지정하려면 `--host claude`, `--host opencode`, `--host pi` 중 하나를 쓰세요. 설치할 위치에 다른 `wsg`가 있으면 기존 설치본을 에이전트의 스킬 검색 경로 밖으로 옮긴 뒤 전환하세요. [도구별 설치 경로](docs/COMPATIBILITY.md)

### uv로 wheel 설치하기

[uv](https://docs.astral.sh/uv/getting-started/installation/)를 사용한다면 릴리스의 wheel을 설치해 터미널에서 `wsg` 명령을 쓸 수 있습니다. 설치할 프로젝트에서 다음 명령을 실행하세요.

```sh
uv tool install https://github.com/hobin01/writing-styles-from-giants/releases/download/v0.2.0/writing_styles_from_giants-0.2.0-py3-none-any.whl
wsg install --host codex
```

사용자 전체에 설치하려면 두 번째 명령에 `--global`을 붙이세요. 터미널에서 `wsg`를 찾을 수 없다면 `uv tool update-shell`을 실행하고 새 터미널을 여세요.

### 오프라인 설치

인터넷에 연결된 컴퓨터에서 [Source code (zip)](https://github.com/hobin01/writing-styles-from-giants/archive/refs/tags/v0.2.0.zip)을 내려받아 오프라인 컴퓨터로 옮기고 압축을 푸세요. Python 3.10 이상이 있으면 압축을 푼 폴더에서 같은 설치기를 실행할 수 있습니다.

```sh
python3 install.py install --host codex --global
```

한 프로젝트에만 설치하려면 대상 프로젝트에서 압축을 푼 `install.py`의 전체 경로를 지정하고 `--global`을 빼세요. [오프라인 설치 안내](docs/OFFLINE.md)

## 에이전트에서 사용하기

설치한 뒤 새 대화를 열고 **대화창에** 예제를 입력하세요.

| 도구 | `--host` | 대화창에 입력할 예제 |
| --- | --- | --- |
| Codex CLI | `codex` | `$wsg eli5 자전거 브레이크를 잡으면 왜 바퀴가 느려지는지 설명해 줘.` |
| Claude Code | `claude` | `/wsg auto 캐시를 쓸지 결정해야 해. DB를 매번 읽는 방식과 비교하는 설계 문서 초안을 써 줘.` |
| OpenCode | `opencode` | `wsg 스킬을 불러와서 docs ko를 실행해 줘.` |
| Pi | `pi` | `/skill:wsg feynman-technique DNS 리졸버 두 곳의 응답이 왜 다를 수 있는지 설명해 줘.` |

스킬을 부른 뒤 `방법-ID [단계] 요청`으로 방법을 지정하세요. `auto [단계] 요청`을 쓰면 WSG가 방법을 골라 이유와 함께 답합니다. `docs ko`는 한국어 목록, `docs en`은 영어 목록을 엽니다. 글쓰기 단계의 기본값은 매번 `standard`입니다. 가볍게 다듬으려면 `light`, 해당 규칙을 모두 점검하려면 `strict`를 쓰세요. [도구별 설치 경로와 검증 범위](docs/COMPATIBILITY.md)

### ChatGPT에서 쓰기

**데스크톱의 로컬 프로젝트**에서는 `--host codex`로 설치하세요. ChatGPT 데스크톱 앱에서 해당 프로젝트를 열고 사이드바의 **스킬**을 확인하세요. `wsg`가 보이면 대화창에 `@`를 입력해 선택하고 `docs ko`를 입력하세요. [OpenAI 스킬 안내](https://learn.chatgpt.com/docs/build-skills)

**웹**에서는 ChatGPT 프로젝트를 만들고 **소스**에 사용할 방법의 파일을 추가하세요. ELI5라면 [지침](skills/eli5/SKILL.md), [규칙](skills/eli5/method.json), [언어 프로필](skills/eli5/locales/en.json)을 내려받아 올리세요. 프로젝트에서 새 대화를 열고 “첨부한 ELI5 지침과 규칙을 standard 단계로 적용해 줘. 자전거 브레이크를 잡으면 왜 바퀴가 느려져?”라고 물어보세요. 같은 프로젝트의 다음 대화에서도 이 파일을 쓸 수 있습니다. 이 방식은 사용할 방법을 하나씩 직접 추가합니다. 다른 방법을 쓸 때는 선택한 단계의 지침이 요구하는 참고 파일도 함께 올리세요. [ChatGPT 프로젝트 안내](https://learn.chatgpt.com/docs/projects)

## 어느 스킬을 고르면 될까?

같은 설명 요청이라도 원하는 결과에 따라 선택이 달라집니다. 아이가 손잡이에서 바퀴까지의 움직임을 따라가게 하려면 **ELI5**, 설명에서 빠진 단계를 찾으려면 **Feynman**, 수식으로 주장을 증명하려면 **GTM**이 맞습니다. 각 이름을 누르면 작성 지침과 예제를 볼 수 있어요. 명령에 넣을 정확한 이름은 [스킬 ID와 용도](commands/catalog.ko.md)에서 복사할 수 있습니다. 예를 들어 Feynman의 ID는 `feynman-technique`입니다.

| 하고 싶은 일 | 스킬 |
| --- | --- |
| 설명하기 | [ELI5](skills/eli5/SKILL.md) · [Feynman](skills/feynman-technique/SKILL.md) · [Boring Professor](skills/boring-professor/SKILL.md) · [인터랙티브 HTML](skills/answer-with-html/SKILL.md) · [Jobs 발표](skills/steve-jobs-presentation/SKILL.md) |
| 논리 세우기 | [GTM 증명](skills/gtm-formal/SKILL.md) · [아리스토텔레스 삼단논법](skills/aristotle-syllogism/SKILL.md) · [소크라테스식 질문](skills/socratic-self-questioning/SKILL.md) · [훈민정음](skills/hunminjeongeum/SKILL.md) · [민토 피라미드](skills/minto-pyramid/SKILL.md) |
| 문장 다듬기 | [ASD-STE100 기반 기술 영어](skills/asd-ste100/SKILL.md) · [오웰 6원칙](skills/orwell-six-rules/SKILL.md) · [미국 연방 평문](skills/federal-plain-language/SKILL.md) · [Microsoft 문체](skills/microsoft-writing-style/SKILL.md) · [New Hart’s Rules](skills/new-harts-rules/SKILL.md) · [한국어 평문](skills/korean-plain-language/SKILL.md) |
| 문서 쓰기 | [Diátaxis](skills/diataxis/SKILL.md) · [Google 설계 문서](skills/google-design-doc/SKILL.md) · [Amazon 6-pager](skills/amazon-six-page-narrative/SKILL.md) · [IETF RFC](skills/ietf-rfc/SKILL.md) · [IMRaD](skills/imrad/SKILL.md) · [NIST 기술 보고서](skills/nist-technical-publication/SKILL.md) |

ASD의 `normal`은 `standard`의 별칭입니다. `strict`는 이 프로젝트가 구현한 규칙을 가장 엄격하게 적용하는 단계이며, 공식 ASD-STE100 준수 인증을 뜻하지 않습니다.

방법별 출처는 [참고 자료](docs/REFERENCE.md)에 있습니다. 직접 만든 내용에는 [MIT 라이선스](LICENSE)를 적용합니다. [외부 자료의 권리](THIRD_PARTY_NOTICES.md)와 [기여 방법](CONTRIBUTING.md)도 확인할 수 있습니다.
