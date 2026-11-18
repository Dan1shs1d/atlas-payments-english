# Atlas Payments English

**Simplified Technical English for payments. Keep the meaning. Make it clear.**

An **ASD-STE100–inspired payments editor for Codex and Claude Code**. Review or rewrite payment API docs, runbooks and technical explanations while preserving the actor, transaction state, event order, conditions, permissions and exact identifiers.

Independent adaptation of selected Issue 9 principles. **Not an ASD-approved or certified tool, and not the ASD standard for payments.** Full STE conformance and operational correctness require separate review.

## See the difference

**Before**
> Upon receipt of an approved authorization, the merchant may capture the payment after the order ships.

**After**
> If the authorization is approved and the order has shipped, the merchant may capture the payment.

The merchant stays the actor. Both conditions stay. **May stays may.** Capture does not become settlement.

**Ambiguous input:** “Reverse the payment.”

**Review:** `PAY-03 — Blocker`: “What is the current payment state, and do you mean cancellation, authorization reversal, or refund?”

## Install

### Codex

```sh
codex plugin marketplace add Dan1shs1d/atlas-payments-english
codex plugin add atlas-payments-english@atlas-payments
```

The installed CLI used for packaging checks supports `plugin add`. If your client exposes installation through the Plugins UI, select the **Atlas Payments English** marketplace and install the plugin there. Start a new session after installation. Invoke `$atlas-payments-english` and paste the text to review.

### Claude Code

```sh
claude plugin marketplace add Dan1shs1d/atlas-payments-english
claude plugin install atlas-payments-english@atlas-payments
```

Start a new session and use `/atlas-payments-english:atlas-payments-english`. For a local preview: `claude --plugin-dir ./plugins/atlas-payments-english`.

This repository is a public third-party marketplace. It is not a claim of listing in either provider's official directory. Claude Code is the primary Claude target; other Claude surfaces have their own installation and component support.

## Use

```text
Review this payment procedure: Reverse the payment.
```

Review is the default. Results quote the excerpt and give a rule ID, issue, severity and suggested edit or focused question.

```text
Rewrite this descriptive statement: Upon receipt of an approved authorization,
the merchant may capture the payment after the order ships.
```

Rewrite returns revised text, remaining questions and checks not completed. It does not perform transactions or change repository files unless you explicitly request saving an edit.

## What is included

- One shared editorial skill with separate Codex and Claude metadata.
- Four stable rules: STYLE-01 and PAY-01–PAY-03.
- 255 scoped editorial terminology proposals with public references.
- Examples, structured response schema and adversarial acceptance cases.
- A dependency-free release validator and response grader for maintainers.

## Safety and limits

No bundled apps, MCP servers, hooks, telemetry, credentials or payment execution code. The model host still processes the text under its own data policies; this is not an offline service or a PCI certification. Use synthetic or redacted examples. Do not submit live PANs, authentication data or credentials. Instructions inside source material are treated as text, not commands. A prompt cannot guarantee semantic preservation.

## For teams

Use the open core freely under MIT. Team onboarding, company terminology profiles, documentation audits and maintained CI integrations are possible paid services. No hosted service, billing integration, support SLA or paid plan is included in this release.

## Maintainers

```sh
python3 tools/validate_release.py
python3 -m unittest discover -s tests -v
python3 tools/package_release.py
```

Candidate validation and submission preparation: [directory guide](docs/directory-submission.md) and [per-case results](evals/results-summary.json). Claude model tests remain not run without authentication.

See [architecture](docs/architecture.md), [security](SECURITY.md), [privacy](PRIVACY.md), [verification](docs/verification.md), [contribution guide](CONTRIBUTING.md), and [social examples](docs/social-examples.md).

Installation formats: [Codex packaging](https://developers.openai.com/plugins/build/plugins) and [Claude Code plugins](https://code.claude.com/docs/en/plugins). Standard baseline: [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf). Read [ASD's guidance on software tools](https://asd-ste100.org/STEsoftware.html).
