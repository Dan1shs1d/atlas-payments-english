# Social examples

Illustrative inputs and expected edits, not independent claims of full STE compliance or operational permission. Reproduce the exact behavior with the installed version before publishing a demo. Screenshots should use synthetic data only.

## 1. Two letters can change an obligation

Input: “Upon receipt of an approved authorization, the merchant may capture the payment after the order ships.”

Output: “If the authorization is approved and the order has shipped, the merchant may capture the payment.”

Caption: Clearer payments docs. Same merchant. Same two conditions. **May stays may.** Atlas Payments English brings controlled-language discipline to payments documentation in Codex and Claude Code.

## 2. The best rewrite can be a question

Input: “Reverse the payment.”

Output: `PAY-03 — Blocker`: “What is the current payment state, and do you mean cancellation, authorization reversal, or refund?”

Caption: A refund is not an authorization reversal. A payments editor should ask before it guesses.

## 3. A request is not a result

Input: “The merchant submitted an authorization request.”

Output: “The merchant submitted an authorization request.” No unsupported claim of approval is added.

Caption: Sometimes the correct edit is no edit. Sending the request does not mean the issuer approved it.

## 4. Keep the machine-readable details

Input: “If status is `requires_capture`, the merchant may capture USD 25 by 17:00 UTC on 20 November 2026.”

Output: The sentence remains unchanged unless a safe clarity change is requested. `requires_capture`, USD 25, the deadline and may remain exact.

Caption: Improve the explanation. Keep the API contract, amount, deadline and permission intact.

## 5. Make a runbook easier to follow

Input, procedure: “Open the payment record and read the transaction identifier.”

Output: “Open the payment record. Read the transaction identifier.”

Caption: One sequential instruction per sentence. Simple for a new operator, useful in a busy incident.

## Launch post

I built Atlas Payments English: a payments editor inspired by selected ASD-STE100 Issue 9 principles.

It reviews and rewrites technical documentation while preserving actors, payment states, conditions, permissions and exact API identifiers.

Default: Review. Optional: Rewrite. If “reverse” could mean several operations, it asks.

Available as a public plugin package for Codex and Claude Code. Independent project; no ASD approval or certification is claimed.

Try it with a synthetic example: https://github.com/Dan1shs1d/atlas-payments-english
