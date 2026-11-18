# Verification and release scope

Release: 0.2.0, 18 November 2026.

## Checks actually completed

| Check | Result | What it establishes |
|---|---|---|
| Release boundary and manifest/reference checks | Passed | Selected structural, link, identity, approval-state and privacy constraints |
| Skill Creator validator | Passed | Skill frontmatter and scaffold checks |
| Unit tests | 20 passed | Release packaging and response-grader behavior using synthetic responses |
| Reproducible archive check | Passed | Two builds produced identical bytes and an allowlisted file inventory |
| Codex CLI discovery, 0.167.0-alpha.4.1 | Passed | Native CLI found atlas-payments-english@atlas-payments, version 0.2.0, as an available local plugin |
| Claude Code 2.1.327 strict plugin validation | Passed | Manifest, declared skill and directory checks; no warnings reported |
| Claude Code 2.1.327 strict marketplace validation | Passed | Marketplace schema and local entry checks |

The native Codex discovery check used temporary command-line configuration overrides, not a persistent change to user settings. The Claude validator was obtained from Anthropic's official npm package, verified against the registry SHA-512 integrity value and run from a temporary directory. No model credentials were needed for these packaging checks.

## Behavior evidence and limits

An earlier ChatGPT package, version 0.1.0, was smoke-tested in two fresh conversations. Rewrite returned the accepted authorization-and-shipment sentence exactly, retaining may. Default Review returned PAY-03 and a focused state/operation question for “Reverse the payment.” These are baseline observations, not evidence that the current public package passed every case in Codex and Claude Code.

The 20 current acceptance fixtures are provided in evals/cases.json. **A complete model-run suite on both public host installations has not been executed.** Unit tests simulate responses to verify the grader and are not model runs. Native manifest validation is not runtime semantic validation. The hosts' official directory policy/security reviews have not been completed, and no official directory listing is claimed.

## Production adoption gate

Before using the plugin to approve operational documentation, run all fixtures on the selected host/model, review actual outputs and tool traces, validate the relevant terminology and source editions, and have a domain owner approve consequential changes. Repeat after meaningful rule, glossary or host/model changes. Never treat a passing format check as full Issue 9, legal, network or security conformance.

This is an installable public release with explicit limits, not an assurance that every payments meaning can be validated automatically.
