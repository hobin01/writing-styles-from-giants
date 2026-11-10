# Host compatibility

The [installation guide](../README.md#install-for-a-local-agent) installs a complete `wsg` skill for the selected host. Project scope uses the current directory. User scope uses the host's default per-user skill directory. Existing or modified installations can be kept as backups by moving the whole `wsg` directory outside the host’s discovery paths before reinstalling. To remove the skill, move it out of each host where you installed it. To remove the separate CLI, run `uv tool uninstall writing-styles-from-giants`.

| Surface | Project / user skill directory | Invocation and evidence |
| --- | --- | --- |
| Codex CLI | `.agents/skills` / `~/.agents/skills` | Type `$`, select `wsg`, then supply the method ID, `auto` or `docs`. Checkout and user-link runs on 0.167.0 are recorded below. [OpenAI skill guide](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code | `.claude/skills` / `~/.claude/skills` | Installed skill: `/wsg docs en`, `/wsg auto REQUEST` or `/wsg ID REQUEST`. The checkout additionally registers colon aliases. [Anthropic skill guide](https://code.claude.com/docs/en/skills) |
| OpenCode | `.opencode/skills` / `~/.config/opencode/skills` | Ask the agent to load the `wsg` skill and pass `docs en` or a method and request. V2 also supports the explicit mention `@wsg docs en`. Custom shell-expanding command templates are unsuitable for quoting arbitrary writing samples on 1.16.2. [OpenCode skill discovery](https://opencode.ai/docs/skills/) |
| Pi | `.pi/skills` / `~/.pi/agent/skills` | `/skill:wsg docs en` or `/skill:wsg ID REQUEST`. Use `/reload` after installing into a running session. [Pi skill guide](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md) |
| ChatGPT desktop | Local project; check **Skills** in the sidebar | When `wsg` is listed, select it with `@` and give it the same arguments. Documented surface; WSG picker and generation untested. [OpenAI skill guide](https://learn.chatgpt.com/docs/build-skills) |
| ChatGPT web | Project **Sources** | Add one method’s files and ask ChatGPT to apply them. The [README](../README.md#chatgpt) walks through ELI5. Manual file-based use; WSG does not publish a ChatGPT directory plugin. [ChatGPT projects](https://learn.chatgpt.com/docs/projects) |

The release installer requires Python 3.10 or later and uses copies. Some hosts also scan other hosts’ directories. If a picker lists multiple `wsg` entries, check their paths and keep the intended version in one discoverable location. Windows host discovery and nondefault host directories require separate verification.

## Packaged skill discovery · 2026-11-10

On macOS 26.5.2 arm64, we installed the 0.1.0 wheel into separate project directories and started each host with isolated settings. Codex CLI 0.167.0 returned the project-scoped `wsg` path from app-server `skills/list`. Claude Code 2.1.228 listed the project’s `wsg` command at SDK initialization. OpenCode 1.16.2 listed only the WSG entrypoint in `opencode debug skill`. Pi 1.5.2 returned `skill:wsg` with its project path from RPC `get_commands`. The installer tests compare the bundled catalogs and method files with the source tree. These host probes exercise discovery; the model runs for the checkout are documented below.

## Codex user scope

For contributors who edit methods in a long-lived checkout, the original live-link setup is still available. From the checkout root, link its adapter into Codex’s user skills directory. Start a new Codex chat in another project and enter `$wsg docs ko` or `$wsg auto YOUR REQUEST`. Codex follows the link to the command guide and all 22 methods.

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
