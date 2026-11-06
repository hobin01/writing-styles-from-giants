# References

Project-wide bibliography of projects, websites, papers, books, and guides that inform the work.

## Recording references

Add or update a source in the same PR that uses it. Keep one entry per source and include:

- Author or responsible organization, title, and canonical URL or DOI.
- Inspected commit, version, edition, or publication date where available; access date and the pages, sections, or files actually read. Mark unknown details instead of guessing.
- What the source informed, the practices adopted or omitted, and links to affected documents or skills. Distinguish an unread candidate, a consulted reference, and an adopted implementation; reading documentation does not establish tested behavior.

Keep detailed evidence with each method under the [authoring contract](METHOD_AUTHORING.md), and link it from the bibliography entry. Link rights/reuse records in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). The bibliography does not replace source-to-rule provenance or required license notices. Add source candidates when relevant, clearly marked as unread until inspected.

## mattpocock/skills

Matt Pocock. [skills, commit 4ae2317](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d). Accessed 2026-11-06; inspected repository structure, README, agent/contributor guidance, and maintainer installation script. Informs documentation and repository organization under [CONTRIBUTING.md](../CONTRIBUTING.md). License evidence is in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).

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

## vercel-labs/skills

Vercel. [skills README, commit d3701c1](https://github.com/vercel-labs/skills/blob/d3701c11b1101251af14c9d148f026e1a47ebe17/README.md). Accessed 2026-11-07; scope: README. Identifies an existing installer candidate with project-scoped installation and agent selection, informing the reuse-first delivery plan in [PROJECT.md](PROJECT.md) and the installation contract in [ARCHITECTURE.md](ARCHITECTURE.md). No installer integration or behavior tests have been completed; license evidence is in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).

## Agent Skills

Agent Skills project. [Repository README, commit 83021e2](https://github.com/agentskills/agentskills/blob/83021e2be457a9b6679148719c1f6074f0ad975e/README.md) and [skills-ref README](https://github.com/agentskills/agentskills/blob/83021e2be457a9b6679148719c1f6074f0ad975e/skills-ref/README.md). Accessed 2026-11-07; scope: those two files. Consulted for portable skill-directory structure and validation references under [ARCHITECTURE.md](ARCHITECTURE.md). The library is explicitly demonstration-only, so it is not adopted as a production dependency. Code and documentation have distinct licenses recorded in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md); full format compliance and host compatibility remain unverified.
