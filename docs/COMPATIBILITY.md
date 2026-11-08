# Host compatibility

Open this checkout in your agent, or use the Codex user-scope setup below to work elsewhere. The adapters use the host's model and read the same [command guide](../commands/WSG.md).

| Host | Status | Documentation starting point |
| --- | --- | --- |
| Codex CLI and app-server | Smoke-tested in the checkout and via a user-scope link from an unrelated project | [Repository and user skills, directory symlinks and explicit invocation](https://learn.chatgpt.com/docs/build-skills) · [CLI slash-command menu](https://learn.chatgpt.com/docs/developer-commands?surface=cli) |
| Claude Code | Project slash-command discovery and expansion verified: `/wsg`, `/wsg:auto`, `/wsg:docs`. Live Claude generation untested. | [Project command names and arguments](https://code.claude.com/docs/en/skills#how-a-skill-gets-its-command-name) |
| OpenCode | No native slash adapter shipped | [Skills](https://opencode.ai/docs/skills/) and [V2 skills](https://opencode.ai/v2/docs/skills) |
| Antigravity | planned | [Skills](https://antigravity.google/docs/skills) |
| Pi | planned | [Skills](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md) |
| Cline | planned | [Skills](https://docs.cline.bot/customization/skills) |

## Codex user scope

From the root of a checkout you intend to keep, link the adapter into Codex's user skills directory. Start a new Codex chat in another project and enter `$wsg docs ko` or `$wsg auto YOUR REQUEST`. Codex follows the link to the command guide and all 22 methods.

```sh
python3 - <<'PY'
from pathlib import Path

adapter = Path(".agents/skills/wsg").resolve(strict=True)
link = Path.home() / ".agents/skills/wsg"
link.parent.mkdir(parents=True, exist_ok=True)
if link.is_symlink() and link.resolve() == adapter:
    print("WSG already points to this checkout.")
else:
    link.symlink_to(adapter, target_is_directory=True)
PY
```

An existing different file, directory or link causes the command to stop. The link follows the local checkout's current files, including working edits and branch switches. When a change is only on GitHub, fast-forward the clean source checkout on `main` with `git pull --ff-only origin main`. If a running Codex session still shows an old skill listing, start a new session. Keep the checkout in place for as long as you use the link.

**Verified on 2026-11-09.** Codex app-server 0.167.0 on macOS discovered one enabled `wsg` skill at user scope from a separate Git repository. That repository had its own unrelated `commands/WSG.md`. A native `$wsg docs ko` turn read the WSG checkout’s Korean catalog and returned all 22 IDs. A separate `$wsg auto` turn read ELI5’s instructions, metadata and locale in that checkout and applied `standard`. The user link and source adapter referenced the same file after the adapter was edited.

## Checkout checks · 2026-11-08

- **Codex 0.167.0, macOS 26.5.2 arm64.** App-server `skills/list` discovered the [WSG adapter](../.agents/skills/wsg/SKILL.md) at repository scope from the root and from `skills/eli5/`. Choose `$wsg` in the composer. The [adapter policy](../.agents/skills/wsg/agents/openai.yaml) enables explicit invocation only. App-server tests supplied a native skill selection and the user's text to ordinary read-only turns. An explicit `eli5 light` request read the method and its locale and explained melting ice. `docs ko` read the Korean catalog and returned all 22 IDs. These runs exercise the service behind the composer; the desktop picker itself was not UI-tested.
- **Codex level reset.** Two native invocations in the same app-server chat produced `eli5 · strict` on the first request and `eli5 · standard` on the next request with no level. The second selection appeared in a status before the answer.
- **Codex CLI generation.** Fresh `codex exec` runs on `gpt-6.1-sol` returned the English catalog by default, selected Google design docs at `standard` for a Korean cache proposal, and applied ASD's strict reference to a conditional service instruction. Sorting words produced an ordinary answer without selecting a method. A request after `--` preserved “light” and “strict” as source words at the default level. A separate `$wsg off` call returned exactly the requested two words.
- **Claude Code 2.1.228, same OS.** SDK initialization returned the three checkout commands from [the project command directory](../.claude/commands/). Headless invocations expanded all three with their arguments. A probe with inline and newline shell-looking text preserved the original command arguments, escaped the executable syntax in the expanded prompt and created no marker file. The probe used an isolated configuration and no provider account. It verifies the native parser, not a generated Claude answer.
- **OpenCode 1.16.2.** Its [command implementation](https://github.com/anomalyco/opencode/blob/v1.16.2/packages/opencode/src/session/prompt.ts#L1436-L1448) expands user arguments before executing inline shell substitutions. A project command template on that version would let supplied writing samples trigger shell commands, so this checkout does not register one.

## Evidence levels

| Status | Required evidence |
| --- | --- |
| `planned` | Intended target; no current verification record |
| `docs-confirmed` | Dated source links, host/surface/version, and the documented discovery/invocation behavior |
| `smoke-tested` | Recorded discovery, invocation, and reference-access runs on a specified host/version/OS |
| `release-tested` | Smoke tests plus the released method set and installation/update/removal scenarios |

Only the latter two support runtime claims, within the actual tested scope. A supported file format or an existing directory does not establish invocation, hook execution, symlink discovery, or equivalent permissions.

For each verified delivery path, record the installer/version, host/surface/version, OS, scope, resolved destination, discovery evidence, explicit invocation, reference access, and limitations. Test global/project same-name conflicts, shared roots, paths with spaces/non-ASCII characters, existing and modified user content, link/copy behavior, interrupted updates, and removal preservation. Windows support requires its own permission and link/copy evidence.

Portable content follows the [Agent Skills specification](https://agentskills.io/specification). [Agent Plugins](https://agent-plugins.org/specification) are a separate packaging surface. Host tool names, metadata, lifecycle hooks, and authorization semantics stay outside the portable core.
