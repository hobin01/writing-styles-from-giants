# RFC-style technical specification · Optional reconnect with a hard deadline

Run on 2026-11-08 • `ietf-rfc` 0.1.1 • English • Codex CLI 0.167.0

### Prompt

> Draft a short internal protocol requirement using BCP 14 notation. A client may reconnect once only after error E7. It must wait at least 4 seconds before reconnecting. Error E8 does not permit a reconnect. There is no registry action. Keep the text to 90 words or fewer.

### Without a skill

> The key words “MUST”, “MUST NOT”, and “MAY” in this document are to be interpreted as described in BCP 14 (RFC 2119 and RFC 8174).
>
> A client MAY reconnect once after receiving error E7. It MUST wait at least 4 seconds after receiving E7 before reconnecting. It MUST NOT make a second reconnection attempt. A client MUST NOT reconnect after error E8 or any error other than E7.
>
> This document requires no registry action.

### With the skill at standard

> # Reconnection Requirement
>
> Status: Internal draft.
>
> This specification governs client reconnection after an error. Uppercase keywords MUST, MUST NOT, and MAY have their BCP 14 meanings (RFC 2119 and RFC 8174, normative references).
>
> After error E7, the client MAY reconnect once. It MUST wait at least 4 seconds after E7 before reconnecting. The client MUST NOT reconnect after E8 or any error other than E7.
>
> Security considerations: This rule does not define authentication for reconnected sessions.
>
> IANA considerations: No registry action is required.

### What changed

**Checks set before the run.** Keep reconnect optional and limited to once after E7, preserve the lower wait bound, exclude E8 and identify the absence of registry action. Use requirement keywords consistently.

Both specify the optional single reconnect, waiting period, E8 exclusion and no registry action. The skill adds explicit document status and a security boundary; the baseline states the second-attempt prohibition directly. For this narrow request the shorter baseline also works.

**차이.** 두 답 모두 재연결 횟수와 대기 시간을 정확히 적었습니다. 스킬 답안에는 문서 상태와 보안 범위가 추가돼 더 길어졌습니다.
