# Security

## Threat model

The skill consumes untrusted prose and code samples. An attacker can embed instructions to leak secrets, run commands, follow links, change rules or misstate a transaction outcome. The instruction boundary treats those passages as material. This mitigation is not an isolation mechanism: the host model and its permissions remain the security boundary.

The shipped plugin is skills-only: no hooks, apps, MCP servers, credential prompts, execution commands or network clients. Maintainer tools are optional standard-library Python programs; the plugin does not invoke them automatically. The public package contains only explicitly listed files. Never include customer text in a release, a CI artifact or a bug report.

## Safe use

- Use synthetic or redacted payment examples. Do not input live PANs, security codes, authentication data, API keys or private keys.
- Review the host's retention, training, access and data-residency settings. This package does not override them.
- Keep host sandbox and confirmation controls enabled. Editorial requests do not authorize transactions, commits, file rewrites or outbound transmissions.
- Treat outputs as proposed text. A human must approve changes that affect financial or contractual meaning.
- Pin a reviewed commit or release when organizational policy requires reproducibility. A mutable branch is not a security guarantee.

## Reporting

Report non-sensitive packaging defects through a GitHub issue. For a vulnerability involving sensitive material, first open a minimal issue requesting a private reporting channel, without exploit payloads, payment data or secrets. Do not disclose sensitive details publicly. No private vulnerability inbox or paid response SLA is configured yet.

## Maintenance

0.2.x is the supported public line. No guarantees are made for modified copies or unreviewed host/model upgrades. CI runs without repository write permissions or API secrets. Dependency-free local validators check packaging and selected response invariants; they are not a semantic or security certification.
