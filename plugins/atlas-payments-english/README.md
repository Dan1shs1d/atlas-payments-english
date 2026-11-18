# Atlas Payments English

An ASD-STE100–inspired payments editor for Codex and Claude Code. Review API documentation, operational procedures and technical explanations, or request a rewrite. Review is the default. Results identify stable rule IDs and ask focused questions when facts affect payment meaning.

Preserve actors, states, event order, conditions, obligations, amounts, currencies, deadlines and exact identifiers. The 255 terminology records are scoped editorial proposals, not ASD-approved vocabulary. This independent adaptation does not certify full STE or operational conformance.

## Example

Before: Upon receipt of an approved authorization, the merchant may capture the payment after the order ships.

After: If the authorization is approved and the order has shipped, the merchant may capture the payment.

Both conditions remain. May remains may.

## Installation and support

Follow the [public installation instructions](https://github.com/Dan1shs1d/atlas-payments-english#install). In Codex, invoke `$atlas-payments-english`. In Claude Code, invoke `/atlas-payments-english:atlas-payments-english`.

In Claude Code 2.1.275 or later:

```text
/plugin install atlas-payments-english --marketplace Dan1shs1d/atlas-payments-english
```

## Data handling and license

This skills-only package includes no MCP server, hook, telemetry, billing or transaction execution. The host processes submitted text under its own policies. Use synthetic or redacted data. Do not paste live card data or secrets.

Read the [privacy notice](https://github.com/Dan1shs1d/atlas-payments-english/blob/main/PRIVACY.md), [MIT license](https://github.com/Dan1shs1d/atlas-payments-english/blob/main/LICENSE), and [security guidance](https://github.com/Dan1shs1d/atlas-payments-english/blob/main/SECURITY.md). Report non-sensitive defects through [GitHub issues](https://github.com/Dan1shs1d/atlas-payments-english/issues). No paid service or support SLA is included. Directory listing and Claude runtime validation are not claimed.
