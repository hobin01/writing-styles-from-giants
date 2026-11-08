# Korean plain-language companion · 내보내기 예약 안내

Run on 2026-11-08 • `korean-plain-language` 0.1.1 • Korean • Codex CLI 0.167.0

### Prompt

> 앱 사용자에게 보여 줄 문구만 네 문장 이내로 다듬어 주세요. 원래 해요체와 버튼 이름은 유지해 주세요. 원문: ‘내보내기 예약’은 관리자에게만 가능한 동작이에요. ‘예약’을 눌러도 지금 파일이 전송되지는 않아요. 전송은 확인이 끝난 후에만 시작될 수 있어요. 누가 확인하는지는 아직 정해지지 않았어요.

### Without a skill

> ‘내보내기 예약’은 관리자만 할 수 있어요. ‘예약’을 눌러도 파일이 바로 전송되지는 않아요. 전송은 확인이 끝난 뒤에만 시작할 수 있어요. 확인 담당자는 아직 정해지지 않았어요.

### With the skill at standard

> ‘내보내기 예약’은 관리자만 할 수 있어요. ‘예약’을 눌러도 지금 파일이 전송되지는 않아요. 확인이 끝난 후에만 전송을 시작할 수 있어요. 누가 확인할지는 아직 정해지지 않았어요.

### What changed

**Checks set before the run.** 관리자만 가능한 동작, 실제 버튼 이름, 즉시 전송되지 않음, 확인 후에도 시작은 가능성이라는 점, 확인 주체 미정과 해요체를 보존한다.

Both preserve 해요체, both labels, the administrator restriction, and the unknown person responsible. The baseline says ‘확인 담당자’; the skill says ‘누가 확인할지’. Both keep confirmation necessary without promising immediate transmission.

**차이.** 두 답 모두 조건과 해요체를 지켰습니다. 확인할 사람이 아직 정해지지 않은 점을 하나는 ‘확인 담당자’, 다른 하나는 ‘누가 확인할지’로 표현합니다.
