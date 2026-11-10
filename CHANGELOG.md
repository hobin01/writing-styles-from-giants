# Changelog

## [0.1.1]

- Add a checksum-verified offline ZIP with the full catalog, installer and English/Korean instructions. On a disconnected machine, Python 3.10+ can install it into a project or user skill directory without uv, pip or a build step.
- To upgrade a 0.1.0 deployment, move the previous `wsg` skill directory outside the host's search paths, install the new version and rerun the host install command. This preserves existing edits as a backup.

## [0.1.0]

- First public release. Install the `wsg` command from the versioned GitHub wheel using uv, then choose a host and project or user scope.
- Select one of 22 experimental writing methods, request automatic selection, or browse the English and Korean catalogs. Examples show each level beside a response to the same question without the skill.
- Add installation and usage examples for ChatGPT, Codex CLI, Claude Code, OpenCode, and Pi. See [host compatibility](docs/COMPATIBILITY.md) for the evidence for each surface.
- The existing live Codex checkout link remains available. An existing installation at the same location must be resolved before switching delivery paths.
