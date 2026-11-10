# Offline installation · 오프라인 설치

## English

From v0.1.2, the GitHub **Source code (zip)** includes `install.py` at the top level. Transfer that ZIP to a computer with Python 3.10+ and extract it. To install for your user, run `python3 install.py install --host codex --global` from the extracted folder. For project scope, run the script by its full path from the target project and omit `--global`.

### Dedicated offline ZIP

1. On a connected computer, download the **wsg-offline-vX.Y.Z.zip** asset and **SHA256SUMS** from the same GitHub Release. Replace `vX.Y.Z` in these examples with the release tag. Transfer both files to the offline computer. It needs Python 3.10 or newer.
2. In the folder containing the downloads, check the ZIP's hash against the line for `wsg-offline-vX.Y.Z.zip` in `SHA256SUMS`. On Linux use `sha256sum wsg-offline-vX.Y.Z.zip`, on macOS use `shasum -a 256 wsg-offline-vX.Y.Z.zip`, or on Windows use `Get-FileHash wsg-offline-vX.Y.Z.zip -Algorithm SHA256`. Continue only if the values match. Extract the ZIP.
3. In your **target project**, run the command below. Replace the example path with the full path to the extracted installer. Use `python` if that is the name of your Python 3.10+ interpreter.

```sh
python3 "/path/to/wsg-offline-vX.Y.Z/install.py" install --host codex
```

Choose `codex`, `claude`, `opencode` or `pi` for `--host`. Add `--global` to install for your user or `--dry-run` to preview the destination. If a previous copy conflicts, move it outside the agent's skills directories and run the command again. The installed copy stays in place after you remove the extracted files.

Open a new session and enter `$wsg docs en` in Codex, `/wsg docs en` in Claude Code, `Load the wsg skill and run docs en` in OpenCode, or `/skill:wsg docs en` in Pi. Offline writing requires a host and model that can run offline.

## 한국어

v0.1.2부터 GitHub의 **Source code (zip)** 최상위 폴더에 `install.py`가 들어 있습니다. Python 3.10 이상이 설치된 컴퓨터로 ZIP을 옮겨 압축을 푸세요. 압축을 푼 폴더에서 `python3 install.py install --host codex --global`을 실행하면 사용자 전체에 설치됩니다. 한 프로젝트에만 설치하려면 해당 프로젝트에서 설치 파일의 전체 경로를 지정하고 `--global`을 빼세요.

### 전용 오프라인 ZIP

1. 인터넷에 연결된 컴퓨터에서 같은 GitHub 릴리스의 **wsg-offline-vX.Y.Z.zip**과 **SHA256SUMS**를 내려받아 오프라인 컴퓨터로 옮기세요. 아래 예제의 `vX.Y.Z`는 내려받은 릴리스 태그로 바꾸세요. 오프라인 컴퓨터에는 Python 3.10 이상이 필요합니다.
2. 다운로드한 폴더에서 ZIP의 SHA-256 해시를 구해 `SHA256SUMS`의 `wsg-offline-vX.Y.Z.zip` 줄과 대조하세요. Linux에서는 `sha256sum wsg-offline-vX.Y.Z.zip`, macOS에서는 `shasum -a 256 wsg-offline-vX.Y.Z.zip`, Windows에서는 `Get-FileHash wsg-offline-vX.Y.Z.zip -Algorithm SHA256`을 사용하세요. 해시가 일치하면 압축을 푸세요.
3. **설치할 프로젝트 폴더**에서 아래 명령을 실행하세요. 예시 경로를 압축을 푼 설치 파일의 전체 경로로 바꾸세요. Python 3.10 이상을 `python`으로 실행하는 환경에서는 `python3` 대신 `python`을 쓰세요.

```sh
python3 "/path/to/wsg-offline-vX.Y.Z/install.py" install --host codex
```

`--host`에 `codex`, `claude`, `opencode`, `pi` 중 하나를 넣으세요. 사용자 전체에 설치하려면 `--global`, 설치 경로만 먼저 확인하려면 `--dry-run`을 붙이세요. 이전 설치본과 충돌하면 기존 폴더를 스킬 검색 경로 밖으로 옮긴 뒤 다시 실행하세요. 설치가 끝나면 압축을 푼 폴더를 삭제해도 됩니다.

새 대화에서 Codex는 `$wsg docs ko`, Claude Code는 `/wsg docs ko`, OpenCode는 `wsg 스킬을 불러와서 docs ko를 실행해 줘`, Pi는 `/skill:wsg docs ko`를 입력하세요. 오프라인에서 글까지 생성하려면 해당 환경에서 실행할 수 있는 에이전트와 모델이 필요합니다.
