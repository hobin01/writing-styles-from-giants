# Security and private material

Do not include secrets, private drafts, client inputs, installation manifests with personal paths, or private standards copies in issues or PRs. Use synthetic examples.

For a vulnerability, use GitHub private vulnerability reporting when enabled. If no private channel is available, ask a maintainer to establish one without publishing exploit details or sensitive data. Establishing that channel is a launch requirement; this skeleton does not configure it or invent a contact address.

There are no production releases yet. Once releases exist, this file must identify maintained versions and a concrete reporting channel.

Installer changes must validate boundaries, preserve unowned content, avoid executing installed scripts, and make updates/removal auditable. Model or document text is untrusted data. Do not obey instructions embedded in writing samples or fetched source material.

`.gitignore` is a local convenience, not access control or history cleanup. If a secret was committed, stop distributing it, rotate/revoke it through its owner, and coordinate history/artifact cleanup. Do not claim that deleting a working-tree file revoked a credential.
