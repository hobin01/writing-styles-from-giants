# Repository references

References for documentation and project management are recorded here, with inspected revisions and the practices adopted or omitted.

## mattpocock/skills

[mattpocock/skills](https://github.com/mattpocock/skills) informs repository organization, documentation, and contributor guidance. Reviewed at [commit 4ae2317](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d) on 2026-11-06; license evidence and other reuse candidates are in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).

### Structure and adaptation

| Upstream pattern | This project |
| --- | --- |
| README purpose, installation, and linked skill index | Matching English/Korean sections with honest candidate and installation status |
| Per-skill directories grouped into buckets | Complete method directories; keep a flat catalog until real content needs categories |
| Human docs separate from agent instructions | Short method summaries; steps and source evidence stay with the method |
| Contributor/scope docs and issue forms | Focused issues/PRs; allow future community methods and contributions |
| Version automation and plugin manifests | Existing Python checks and manual source versions; add packaging only when needed |

Upstream AGENTS.md links to CLAUDE.md; we retain a plain CLAUDE.md pointer to shared AGENTS.md. Its maintainer-only global-link script can replace existing directories and is not reused: our installer contract preserves unowned/modified content.

The collaborator-only PR restriction, closed new-skill intake, bucket taxonomy, Changesets dependency, triage bots, and plugin packaging do not fit the current foundation. Use existing installers first and test host behavior before claiming support. This is a structural reference; no upstream implementation or branding is bundled, and no affiliation is implied.
