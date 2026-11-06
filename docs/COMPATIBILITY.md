# Host compatibility

**No host integration is runtime-verified in this project.** The following are planned targets. The linked upstream documentation is a starting point, not a recorded compatibility test.

| Host | Status | Documentation starting point |
| --- | --- | --- |
| Codex | planned | [Skills](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code | planned | [Skills](https://code.claude.com/docs/en/skills) |
| OpenCode | planned | [Skills](https://opencode.ai/docs/skills/) and [V2 skills](https://opencode.ai/v2/docs/skills) |
| Antigravity | planned | [Skills](https://antigravity.google/docs/skills) |
| Pi | planned | [Skills](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md) |
| Cline | planned | [Skills](https://docs.cline.bot/customization/skills) |

Verify current official documentation before selecting installation paths or asserting precedence. Record the host's product surface and version: a CLI, app, and IDE extension may differ. Derive paths from that evidence rather than copying an untested path table.

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
