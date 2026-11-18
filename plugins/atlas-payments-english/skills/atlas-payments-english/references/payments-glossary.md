# Payments glossary

255 original short editorial definitions. Each selects a meaning and a usage boundary. These are proposals for controlled payments writing, not an approved extension of the ASD dictionary. Check network/provider applicability. A linked concept source does not independently establish permission, eligibility or a deadline. Some source locators identify related concepts rather than a formal definition.

Use the published standard for its complete vocabulary and writing rules. Original manuals and the standard are not included in this package.

## G001: account

Record and contractual relationship used to hold a balance or process financial activity.

Recommended usage: Name the account type and its holder; distinguish a card account from a merchant or platform account.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Account); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Adyen account)

## G002: account holder

Person or entity that holds the specified account.

Recommended usage: Specify whether this means a cardholder, merchant, platform user, or bank-account holder.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Account Holder); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Cardholder)

## G003: account updater

Service that supplies changes to stored card-account details.

Recommended usage: Name the network or provider service. An update does not guarantee approval of a later payment.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Account Updater); [T15](https://stripe.com/guides/understanding-benefits-of-network-tokens) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G004: acquirer

Institution acting for the merchant in acquiring card transactions.

Recommended usage: Use the role name when responsibilities matter. A gateway or processor is not automatically the acquirer.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 840); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Acquirer); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Acquirer (or Acquiring bank))

## G005: acquiring

Activity of accepting and submitting merchant transactions into the applicable payment system.

Recommended usage: Identify the acquirer, processing route, and market. Do not equate acquiring with software gateway services.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 840); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Acquirer); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Acquirer (or Acquiring bank))

## G006: acquirer reference number (ARN)

Reference used to trace a card transaction or refund through acquiring and network processing.

Recommended usage: Write the full name before ARN. Keep it distinct from a provider payment ID and a Visa Transaction Identifier.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Acquirer Reference Number (ARN)); [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 15)

## G007: address verification service (AVS)

Service that compares supplied address information with issuer-held address information.

Recommended usage: Report the actual result and supported fields. An AVS match does not prove identity or eliminate fraud risk.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 31)

## G008: aggregator merchant

Intermediary that performs specified merchant-acquiring functions under an acquirer arrangement.

Recommended usage: Describe the contracted functions. Do not assume all aggregators, marketplaces, and payment facilitators have identical roles.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Aggregator merchant)

## G009: application programming interface (API)

Defined interface through which software requests data or operations from another system.

Recommended usage: Use exact endpoint, field, and enum names. Distinguish submitting a request from receiving its final outcome.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Application Programming Interface (API)); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G010: authentication

Assessment of identity or credential authenticity using the applicable authentication method.

Recommended usage: Specify shopper, device, credential, or chip authentication. It is separate from financial authorization.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Authentication); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 845); [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G011: authentication request

Message requesting an authentication assessment.

Recommended usage: For EMV 3DS, preserve the exact message name and version; do not call it an authorization request.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Authentication request (AReq)); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 844); [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G012: authentication response

Message carrying the result or next step of an authentication assessment.

Recommended usage: Preserve the protocol result and any challenge requirement. Do not translate it into payment approval.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Authentication response (ares)); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 846); [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G013: authorization

Decision by an authorized issuer, processor, or stand-in service to approve a transaction.

Recommended usage: Name the decision-maker and outcome. Approval is not capture, clearing, settlement, or a guarantee against disputes.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 907); [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Authorization); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Authorization)

## G014: authorization request

Request for authorization of the specified transaction.

Recommended usage: Identify the amount, currency, and transaction context. A submitted request does not establish that approval occurred.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 846); [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Authorization Request)

## G015: authorization response

Reply to an authorization or applicable account-verification request.

Recommended usage: Keep approval, decline, and other response outcomes separate; preserve provider and network codes.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 843); [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Authorization Response)

## G016: approval response

Authorization response indicating approval of the transaction.

Recommended usage: Describe the approved amount and relevant conditions. Do not describe it as a settled payment.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 843); [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Approval Response)

## G017: authorization code

Code returned to indicate authorization approval.

Recommended usage: Retain the exact value. It is not a generic payment ID or proof that the merchant received funds.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 846); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G018: authorization hold

Reservation of available funds or credit associated with an approved authorization.

Recommended usage: Separate the approved amount, held amount, hold release, and final debit. Do not promise a universal expiry period.

Status: editorial proposal.

Sources: [V4](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf) (2024 guide; PDF p. 1); [T1](https://docs.stripe.com/payments/paymentintents/lifecycle) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G019: preauthorization

Authorization category used when the final amount or completion is not yet certain, subject to network rules.

Recommended usage: Distinguish Mastercard preauthorization coding from a provider's informal pre-auth label.

Status: editorial proposal.

Sources: [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Preauthorizations); [V4](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf) (2024 guide; PDF p. 1)

## G020: estimated authorization

Authorization requested for a genuine estimate before the final transaction amount is known.

Recommended usage: Label the amount as an estimate. Apply the applicable network's eligibility and completion rules.

Status: editorial proposal.

Sources: [V4](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf) (2024 guide; PDF p. 2); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 868)

## G021: incremental authorization

Additional authorization associated with an existing transaction as the expected amount increases.

Recommended usage: Keep the original transaction linkage and distinguish the increment from the total authorized amount.

Status: editorial proposal.

Sources: [V4](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf) (2024 guide; PDF p. 1); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 874)

## G022: final authorization

Mastercard authorization classification for a final amount and expected completion.

Recommended usage: Use it as a network processing classification; it does not mean that settlement is final or irrevocable.

Status: editorial proposal.

Sources: [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Final Authorizations)

## G023: deferred authorization

Authorization submitted after a card-present transaction when online authorization was unavailable at the time.

Recommended usage: State the permitted context and network rules. Do not replace it with delayed capture.

Status: editorial proposal.

Sources: [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Deferred Authorization)

## G024: partial authorization

Approval for less than the originally requested transaction amount.

Recommended usage: State the requested and approved amounts. Use another permitted means to pay the remainder when applicable.

Status: editorial proposal.

Sources: [V7](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/visa-partial-authorization-service.pdf) (2017 historical service guide; PDF p. 1); [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: partial authorization); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G025: authorization reversal

Message that cancels or reduces a prior authorization under the applicable network rules.

Recommended usage: Specify full or partial reversal. Do not call it a refund or promise immediate restoration of available funds.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 847); [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Authorization Reversal); [V4](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf) (2024 guide; PDF p. 2)

## G026: full authorization reversal

Reversal that cancels the original authorization request in full.

Recommended usage: Identify the original authorization and full-reversal operation. Preserve the network's original-data linkage.

Status: editorial proposal.

Sources: [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Full and Partial Reversals); [V4](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf) (2024 guide; Related concept source; exact phrase not located)

## G027: partial authorization reversal

Reversal that reduces the amount of an existing approved authorization.

Recommended usage: Distinguish the remaining authorized amount from the amount released; do not substitute partial refund.

Status: editorial proposal.

Sources: [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Full and Partial Reversals); [V4](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf) (2024 guide; PDF p. 2)

## G028: capture

Provider operation that submits an authorized payment for financial completion.

Recommended usage: Name the provider operation and amount. Keep capture distinct from network clearing, settlement, and merchant payout.

Status: editorial proposal.

Sources: [T2](https://docs.stripe.com/api/payment_intents/capture) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Capture (or Clearing and settlement)); [V4](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf) (2024 guide; Related concept source; exact phrase not located)

## G029: partial capture

Capture for less than the currently capturable authorized amount.

Recommended usage: State whether further captures remain possible and how unused authorization is handled for that provider.

Status: editorial proposal.

Sources: [T2](https://docs.stripe.com/api/payment_intents/capture) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Capture (or Clearing and settlement))

## G030: delayed capture

Capture performed after authorization rather than immediately.

Recommended usage: Specify the provider's capture timing and authorization validity; do not call it deferred authorization.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Capture (or Clearing and settlement)); [T2](https://docs.stripe.com/api/payment_intents/capture) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G031: cancel a payment

Stop an uncaptured payment using the provider's cancellation operation.

Recommended usage: Use the exact provider state and operation. If capture already occurred, assess the refund operation instead.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Cancel a payment); [T1](https://docs.stripe.com/payments/paymentintents/lifecycle) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G032: void

Informal or provider-specific term for canceling a transaction or authorization.

Recommended usage: Prefer the exact cancellation or reversal operation and name the affected processing stage.

Status: editorial proposal.

Sources: [V4](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf) (2024 guide; PDF p. 1); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Cancel a payment)

## G033: clearing

Validation, exchange, and valuation of records used to establish payment obligations.

Recommended usage: Use it for the network processing stage, not as a synonym for merchant receipt of money.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 840); [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; PDF p. 4)

## G034: presentment

Submission of a transaction clearing record from an acquirer to an issuer.

Recommended usage: Identify the message system and whether this is first presentment or a later dispute-related submission.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 855); [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Presentment)

## G035: settlement

Reporting and transfer of amounts owed as a result of clearing.

Recommended usage: Identify the settlement participants, currency, and cycle. Merchant funding or payout may be a separate event.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 840); [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; Related concept source; exact phrase not located)

## G036: reconciliation

Comparison of transaction, accounting, and funds records to explain differences.

Recommended usage: Name the records, identifiers, dates, and amounts being compared. Reconciliation itself does not move money.

Status: editorial proposal.

Sources: [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; PDF p. 4); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Authorization)

## G037: payout

Transfer of available funds to a designated recipient or external account.

Recommended usage: State payer, recipient, amount, and destination. Distinguish a merchant payout from network settlement.

Status: editorial proposal.

Sources: [PAYOUT](https://docs.stripe.com/payouts) (Living documentation; retrieved 18 November 2026; linked documentation, relevant heading)

## G038: refund

Merchant-initiated return of funds associated with a prior purchase.

Recommended usage: State the original transaction, refund amount, currency, and processing outcome. Do not equate refund submission with receipt by the customer.

Status: editorial proposal.

Sources: [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Refund Transactions); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Refund)

## G039: partial refund

Refund for less than the original purchase amount.

Recommended usage: State the amount and remaining refundable balance. Do not confuse it with partial authorization or partial capture.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Refund); [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Refund)

## G040: refund authorization

Authorization assessment of a refund transaction.

Recommended usage: Name the network or provider flow. Refund approval is separate from credit posting and customer availability of funds.

Status: editorial proposal.

Sources: [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Refund Transactions); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 886)

## G041: reversal

Operation that negates or corrects a prior message or transaction at a specified processing stage.

Recommended usage: Always qualify the stage and operation: authorization reversal, clearing reversal, or provider-specific reversal.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 847); [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Reversal)

## G042: transaction

Payment-system event involving the use of a credential to make a payment or exchange value.

Recommended usage: State the transaction type and stage. Avoid using transaction for a request, purchase, dispute, and payout without distinction.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 841); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Transaction); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Transaction (or Tx))

## G043: transaction identifier

Identifier used to link a transaction and associated lifecycle events.

Recommended usage: Name the identifier owner and field. Visa Transaction Identifier, ARN, PSP reference, and merchant reference are different identifiers.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 911); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. PSP reference)

## G044: transaction receipt

Electronic or paper record generated for a transaction.

Recommended usage: Use the receipt as evidence of the recorded event; do not assume it proves final settlement or cardholder authorization.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 846); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G045: payment credential

Account-identifying number or credential used to initiate a transaction.

Recommended usage: Specify PAN, network token, or another credential type. Do not assume every credential is a physical card number.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 840); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Payment Credential)

## G046: primary account number (PAN)

Account number allocated by an issuer to identify a card account.

Recommended usage: Use PAN for the issuer account number. Distinguish it from a payment token, PAR, and truncated display value.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Account PAN); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Card number (PAN)); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G047: bank identification number (BIN)

Licensed leading digits used to identify an issuing institution or designated account range.

Recommended usage: Use the applicable network's BIN length; legacy six-digit and eight-digit BINs can coexist. Do not infer arbitrary prefix lengths.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 849); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: BIN); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Bank Identification Number (BIN))

## G048: account range

Defined subset of account numbers with specified processing or product attributes.

Recommended usage: State the range length and data source. Do not call every longer card prefix a separate BIN.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 6); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Account Range)

## G049: BIN attributes

Data describing the issuer, funding source, product, and other attributes associated with a BIN or range.

Recommended usage: Record provider, range granularity, and update date. An attribute lookup does not prove the cardholder's location or identity.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 849); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G050: cardholder

Person to whom a card or account credential is issued, subject to the network's specific definitions.

Recommended usage: Distinguish the cardholder from the shopper, purchaser, delivery recipient, and account holder when they differ.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 840); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Cardholder); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Cardholder)

## G051: issuer

Institution responsible for issuing the card or maintaining the relevant card account.

Recommended usage: Use issuer or issuing bank for this role. A card-network brand alone does not identify the issuer.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 840); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Issuer); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Issuer (or Issuing bank))

## G052: merchant

Entity accepting payment for the sale of goods or services.

Recommended usage: Name the seller and its contracted role. Distinguish it from a marketplace operator, payment facilitator, and processor.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 866); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Merchant); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Merchant)

## G053: merchant of record (MoR)

Entity presented as the seller for the transaction and responsible for the applicable merchant obligations.

Recommended usage: Use the actual contractual seller and transaction context. A descriptor alone does not settle every legal responsibility.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Merchant of Record (MoR)); [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 65)

## G054: payment facilitator

Entity contracted or registered with an acquirer to provide acquiring services for sponsored merchants.

Recommended usage: Use the network-specific role and obligations. Do not treat every PSP, marketplace, or software platform as a payment facilitator.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 873); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Payment Facilitator); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Payment facilitator (payfac))

## G055: sponsored merchant

Merchant accepting transactions under an arrangement with a payment facilitator.

Recommended usage: Preserve the network-specific designation; verify whether a provider's sub-merchant label denotes the same role.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 873); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Sponsored Merchant)

## G056: marketplace

Business arrangement that connects buyers and sellers and may perform specified payment functions for those sellers.

Recommended usage: Distinguish the general business model from the network's registered marketplace classification for the transaction.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 863); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Marketplace); [V3](https://www.visa.com/vcom-assets/content/dam/VCOM/download/merchants/visa-merchant-data-standards-manual.pdf) (October 2026; PDF p. 4)

## G057: payment gateway

Service that accepts and routes payment requests between merchant systems and payment-processing services.

Recommended usage: Describe its interface and routing role. Do not assume it is also the acquirer or merchant of record.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Payment gateway)

## G058: payment processor

Service that processes payment messages and connects relevant parties to complete payment operations.

Recommended usage: Name the processor and its processing role; distinguish software processing from acquiring membership.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Payment processor)

## G059: payment service provider (PSP)

Provider offering a set of payment acceptance and processing services to merchants.

Recommended usage: State the actual services and region. PSP does not identify a universal regulatory or card-network role.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Payment Service Provider (PSP)); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; Related concept source; exact phrase not located)

## G060: card network

Organization and system that defines and supports participation and transaction processing for its card brand.

Recommended usage: Use the relevant network name when rules differ. Do not describe the network as the issuer merely because its brand is on a card.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Card networks (or Card schemes)); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 857); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Card networks)

## G061: cross-border transaction

Card transaction whose acceptance country differs from its issuing country under the relevant network definition.

Recommended usage: State both countries and the network rule. Currency difference alone does not establish a cross-border transaction.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Cross-border Transaction); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; Related concept source; exact phrase not located); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Cross-border payment)

## G062: local acquiring

Acquiring arrangement established for the specified local market.

Recommended usage: Identify the merchant entity, acquirer, and country. Do not promise domestic treatment or higher approval merely from a local route.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Acquirer (or Acquiring bank)); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Acquirer)

## G063: merchant account

Merchant-side account or processing configuration used for payment acceptance.

Recommended usage: Name the provider and account layer. Do not confuse an Adyen merchant account, bank account, MID, and legal entity.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Adyen account); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 1)

## G064: merchant identifier (MID)

Identifier used by an acquirer or provider to identify a merchant in a specified system.

Recommended usage: Name the system and field. Do not assume a provider merchant-account name equals network DE 42.

Status: editorial proposal.

Sources: [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 1); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Merchant)

## G065: merchant category code (MCC)

Code classifying the merchant's business activity for payment processing.

Recommended usage: Use the applicable network's current classification and merchant activity. Do not infer it from the company name alone.

Status: editorial proposal.

Sources: [V3](https://www.visa.com/vcom-assets/content/dam/VCOM/download/merchants/visa-merchant-data-standards-manual.pdf) (October 2026; PDF p. 3); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; Related concept source; exact phrase not located); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Merchant Category Code)

## G066: merchant descriptor

Merchant-identifying text supplied in transaction and statement data.

Recommended usage: Use recognizable merchant information and the actual field specification. Keep dynamic and static parts separate.

Status: editorial proposal.

Sources: [V3](https://www.visa.com/vcom-assets/content/dam/VCOM/download/merchants/visa-merchant-data-standards-manual.pdf) (October 2026; PDF p. 1); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Merchant); [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 2)

## G067: doing business as (DBA)

Business name under which an entity presents its trading activity.

Recommended usage: Use the recognizable trading name where the network requires it; distinguish it from the legal entity name.

Status: editorial proposal.

Sources: [V3](https://www.visa.com/vcom-assets/content/dam/VCOM/download/merchants/visa-merchant-data-standards-manual.pdf) (October 2026; PDF p. 7); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Doing Business As (DBA)); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; Related concept source; exact phrase not located)

## G068: legal entity

Person or organization recognized as having legal rights and obligations.

Recommended usage: Name the exact entity and jurisdiction when allocating payment responsibilities. Do not substitute brand or website name.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Legal entity); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Legal entity)

## G069: payment modification

Provider operation that changes an existing payment, such as capture, cancellation, or refund.

Recommended usage: Use the exact operation and current payment state. An API acknowledgement may precede the final modification outcome.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Payment modifications)

## G070: webhook

HTTP notification sent by a system to another system when a subscribed event occurs.

Recommended usage: Validate the event and its identifiers; distinguish receipt of a webhook from successful business processing of the event.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Webhooks); [T1](https://docs.stripe.com/payments/paymentintents/lifecycle) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G071: PaymentIntent

Stripe object tracking the attempt to collect a payment through its lifecycle.

Recommended usage: Preserve the exact object and status names. Do not replace a Stripe status with a generic network stage.

Status: editorial proposal.

Sources: [T1](https://docs.stripe.com/payments/paymentintents/lifecycle) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T2](https://docs.stripe.com/api/payment_intents/capture) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G072: SetupIntent

Stripe object used to prepare payment credentials for future use without collecting a payment itself.

Recommended usage: Distinguish setup authentication or consent from authorization or capture of a subsequent payment.

Status: editorial proposal.

Sources: [T1](https://docs.stripe.com/payments/paymentintents/lifecycle) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G073: PSP reference

Provider-assigned reference for a payment or related operation.

Recommended usage: Preserve the exact provider field, such as Adyen pspReference. Do not substitute ARN or merchant reference.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. PSP reference)

## G074: merchant reference

Merchant-assigned reference used to identify an order or payment request.

Recommended usage: State its uniqueness and reuse rules. Distinguish it from network and provider transaction identifiers.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Acquirer Reference Number (ARN)); [T1](https://docs.stripe.com/payments/paymentintents/lifecycle) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G075: card-not-present transaction (CNP)

Card acceptance in a remote environment, such as ecommerce or mail and telephone ordering.

Recommended usage: Apply the network's environment classification. A manually keyed transaction or digital wallet is not automatically CNP in every context.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Card Not Present (CNP)); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 849)

## G076: card-present transaction (CP)

Card acceptance in a physical payment environment under the applicable network interaction rules.

Recommended usage: Describe chip, contactless, or other accepted interaction. Do not infer classification solely from the presence of a physical card.

Status: editorial proposal.

Sources: [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Card-Present); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Point of sale)

## G077: cardholder verification method (CVM)

Method used to establish that the person presenting the card or device is authorized to use it.

Recommended usage: Name the method, such as PIN or an applicable device method; distinguish verification from authorization.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Cardholder Verification Method); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Cardholder Verification Method (CVM))

## G078: contactless

Payment interaction using a supported short-range wireless interface.

Recommended usage: Identify the payment method and acceptance mode. Contactless does not itself specify the cardholder verification method.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 843); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Contactless or Near Field Communication (NFC))

## G079: point of sale (POS)

Physical acceptance environment or system used to initiate in-person sales and payments.

Recommended usage: Specify whether POS means the business location, application, terminal, or network data field.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Point of sale); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G080: mail order/telephone order (MOTO)

Remote card-payment channel in which an order is placed by mail or telephone.

Recommended usage: Preserve the applicable channel coding. Do not classify every manually keyed ecommerce transaction as MOTO.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Mail Order/Telephone Order (MOTO)); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G081: ecommerce payment

Payment initiated through an online commerce interaction.

Recommended usage: Identify the acceptance channel, credential, and payment method. Do not assume a universal authentication or liability outcome.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Ecommerce payments (or Online payments)); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; Related concept source; exact phrase not located)

## G082: digital wallet

Service or application that enables use of payment credentials or stored value.

Recommended usage: Name the wallet and operating model; distinguish pass-through, staged, stored-value, and merchant wallets where applicable.

Status: editorial proposal.

Sources: [V5](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/digital-wallet-guide-october-2024.pdf) (October 2024; PDF p. 1); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Aggregator merchant)

## G083: pass-through digital wallet

Wallet arrangement that passes payment credential information to support a merchant payment.

Recommended usage: Use the network's exact wallet definition. Do not assume the wallet holds the customer's funds.

Status: editorial proposal.

Sources: [V5](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/digital-wallet-guide-october-2024.pdf) (October 2024; PDF p. 2); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Pass-through)

## G084: staged digital wallet

Wallet arrangement with a funding stage separate from the subsequent merchant-payment stage.

Recommended usage: Describe both stages and the wallet operator's role; do not treat the funding transaction as the merchant purchase.

Status: editorial proposal.

Sources: [V5](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/digital-wallet-guide-october-2024.pdf) (October 2024; PDF p. 3); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Staged Digital Wallet)

## G085: stored-value wallet

Wallet arrangement using a stored balance for payment.

Recommended usage: Distinguish the stored balance from a tokenized credential linked directly to a card account.

Status: editorial proposal.

Sources: [V5](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/digital-wallet-guide-october-2024.pdf) (October 2024; PDF p. 2); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Stored-value card)

## G086: credit card

Card product that provides access to a credit account under the issuer's terms.

Recommended usage: Distinguish funding source, product type, and transaction channel; do not infer them from a card-network brand.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Credit Card); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Cards)

## G087: debit card

Card linked to a deposit, debit, or equivalent account as defined by the applicable rules.

Recommended usage: Specify the funding account or product when relevant. Debit does not imply one universal message or settlement model.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 851); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Bank Identification Number (BIN))

## G088: prepaid card

Card linked to a previously funded account or stored value.

Recommended usage: Specify reloadable or non-reloadable when relevant. Prepaid is a funding model, not a synonym for virtual.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 846); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Stored-value card)

## G089: virtual card

Card credential provided for use without requiring a physical card.

Recommended usage: Identify the issuer product and controls. Virtual does not imply single-use, prepaid, or exemption from authentication.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 850); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Cards)

## G090: gift card

Card or credential carrying value for redemption under the issuer's program.

Recommended usage: State issuer, redemption scope, and balance rules. Distinguish closed-loop merchant value from network-branded prepaid products.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Stored-value card); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 846)

## G091: closed-loop payment arrangement

Payment arrangement restricted to a defined issuer or merchant ecosystem.

Recommended usage: State the actual redemption and acceptance scope. Do not assume every gift card is closed-loop.

Status: editorial proposal.

Sources: [V5](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/digital-wallet-guide-october-2024.pdf) (October 2024; PDF p. 2); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Stored-value card)

## G092: stored credential

Payment-account information retained for future transactions under an appropriate agreement or consent.

Recommended usage: State who stores it, its type, and its permitted future use. Storage does not itself make every payment merchant-initiated.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 840); [V6](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf) (2017 historical guide; PDF p. 1); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Stored Credential)

## G093: credential-on-file transaction (COF)

Transaction using a payment credential previously stored for future use.

Recommended usage: Use COF only with the payments context stated. It can mean cost of funds in a different financial context.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Credential-on-File); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Card on File (CoF)); [V6](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf) (2017 historical guide; PDF p. 5)

## G094: cardholder-initiated transaction (CIT)

Transaction initiated through active participation of the cardholder.

Recommended usage: Identify the initiator and applicable stored-credential framework. CIT is not determined solely by whether a credential was stored.

Status: editorial proposal.

Sources: [V6](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf) (2017 historical guide; PDF p. 6); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G095: merchant-initiated transaction (MIT)

Transaction initiated by a merchant under an agreement without active cardholder participation at that time.

Recommended usage: Preserve the reason, consent, and required linkage. Recurring payment is one possible MIT type, not the whole category.

Status: editorial proposal.

Sources: [V6](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf) (2017 historical guide; PDF p. 6); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Merchant-Initiated); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. ContAuth (Continuous Authorization))

## G096: recurring payment

Series of payments under an agreement for goods or services supplied at regular intervals.

Recommended usage: State the schedule, amounts, cancellation terms, and network classification. Do not use recurring for every later stored-card payment.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 890); [V6](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf) (2017 historical guide; PDF p. 6); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Recurring payments)

## G097: unscheduled credential-on-file transaction

Later stored-credential transaction made under an agreement without a fixed recurring schedule.

Recommended usage: Use the network or provider's exact category; distinguish it from a scheduled recurring installment.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 848); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Unscheduled Card on File (UCoF)); [V6](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf) (2017 historical guide; PDF p. 5)

## G098: installment payment

One payment in an agreed series used to pay for a purchase over time.

Recommended usage: State the plan, initiator, and provider or network classification. Do not assume every installment plan is BNPL.

Status: editorial proposal.

Sources: [V6](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf) (2017 historical guide; PDF p. 7); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Installment); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Recurring payments)

## G099: subscription

Agreement for continuing access to goods or services, usually with renewal or repeated billing.

Recommended usage: Distinguish the commercial agreement from the individual payments and their payment-network classifications.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Subscriptions); [T11](https://docs.stripe.com/billing/revenue-recovery) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G100: tokenization

Replacement of sensitive payment-account data with a substitute value managed under a defined token system.

Recommended usage: Name the token type and provider. Network payment tokens and provider vault tokens have different scopes and rules.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Tokenization); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Tokenization); [T14](https://docs.adyen.com/online-payments/tokenization) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T17](https://docs.adyen.com/online-payments/network-tokenization) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G101: payment token

Substitute payment credential used under the applicable tokenization framework.

Recommended usage: Keep it distinct from PAN, PAR, cryptogram, and provider reference. Do not assume universal portability or usability.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 840); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Token); [T17](https://docs.adyen.com/online-payments/network-tokenization) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G102: token service provider (TSP)

Entity that issues and manages tokens for token requestors under the relevant framework.

Recommended usage: Name the token system. TSP has other meanings outside payment tokenization.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 910); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Token Service Provider); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G103: token requestor

Entity requesting a token for an eligible payment-account credential and use case.

Recommended usage: Use the assigned requestor identity and token domain where relevant; do not confuse it with the cardholder or issuer.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Token Requestor); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 840)

## G104: token vault

System or service maintaining token records and the authorized relationship to underlying account data.

Recommended usage: Distinguish a network token vault from a merchant or PSP vault. State who controls access and lifecycle operations.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Token Vault); [T14](https://docs.adyen.com/online-payments/tokenization) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G105: payment account reference (PAR)

Non-financial reference linking activity associated with an underlying payment account.

Recommended usage: Do not use PAR as an authorizable payment credential or as a replacement for PAN in a payment request.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 892); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Payment Account Reference); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G106: DPAN

Term used for a device or digital payment account number in tokenized-payment contexts.

Recommended usage: State the wallet or network context and prefer its official token field name. Do not assume every DPAN is the underlying PAN.

Status: editorial proposal.

Sources: [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row); [T17](https://docs.adyen.com/online-payments/network-tokenization) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G107: token lifecycle management

Management of token activation, suspension, replacement, and other supported lifecycle changes.

Recommended usage: Name the supported token state and operation. A lifecycle update is not payment approval.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Token Management); [T12](https://docs.stripe.com/issuing/controls/token-management) (Living documentation; retrieved 18 November 2026; linked documentation, relevant heading); [T17](https://docs.adyen.com/online-payments/network-tokenization) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G108: token migration

Transfer or replacement of stored payment-token arrangements between systems.

Recommended usage: State token type, provider permissions, security controls, and required re-enrollment. Portability must be verified for the specific arrangement.

Status: editorial proposal.

Sources: [T14](https://docs.adyen.com/online-payments/tokenization) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T17](https://docs.adyen.com/online-payments/network-tokenization) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T15](https://stripe.com/guides/understanding-benefits-of-network-tokens) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G109: 3-D Secure (3DS)

Protocol framework for authenticating cardholders in supported remote card-payment flows.

Recommended usage: State the EMV 3DS version, result, and implementation. Authentication does not guarantee authorization or a universal liability shift.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 931); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Access Control Server (ACS)); [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T31S](https://docs.stripe.com/payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; page text)

## G110: EMV 3DS

EMVCo's 3-D Secure specifications for cardholder authentication in remote commerce.

Recommended usage: Use the precise version and message names. Do not treat 3DS 1 and EMV 3DS 2 as interchangeable implementations.

Status: editorial proposal.

Sources: [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T31S](https://docs.stripe.com/payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; page text); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 228)

## G111: access control server (ACS)

Issuer-side 3DS component that assesses authentication and may conduct a cardholder challenge.

Recommended usage: Use ACS for the authentication component; it is not the acquirer or a payment authorization server.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Access Control Server (ACS)); [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G112: 3DS server

Merchant-side or provider-side component that initiates and manages 3DS authentication interactions.

Recommended usage: Name the provider and protocol version. Distinguish its reference from Directory Server and ACS identifiers.

Status: editorial proposal.

Sources: [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Access Control Server (ACS))

## G113: frictionless authentication

3DS flow in which the issuer assesses authentication without an interactive cardholder challenge.

Recommended usage: Report the actual authentication result. Frictionless does not mean unauthenticated, fraud-free, or automatically exempt from SCA.

Status: editorial proposal.

Sources: [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T31S](https://docs.stripe.com/payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Authentication request (AReq))

## G114: challenge flow

Authentication interaction requiring the cardholder to complete an additional verification step.

Recommended usage: Describe the required action and final result. Starting a challenge does not establish that it was completed successfully.

Status: editorial proposal.

Sources: [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T31S](https://docs.stripe.com/payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Challenge request (creq))

## G115: challenge request

3DS protocol message requesting a challenge interaction.

Recommended usage: Preserve CReq and the version-specific fields. Do not replace it with a financial authorization request.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Challenge request (creq)); [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G116: challenge response

3DS protocol message carrying challenge interaction data or results.

Recommended usage: Preserve CRes and the final protocol outcome. Do not assume every response indicates successful authentication.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Challenge response (cres)); [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G117: attempt response

Visa Secure response indicating that the authentication request reached an attempts-related outcome defined by the network.

Recommended usage: Keep the exact result and eligible transaction context. Do not promise liability shift from the word attempts alone.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 844); [T31S](https://docs.stripe.com/payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G118: strong customer authentication (SCA)

Authentication requirement defined in the applicable payment-services regulatory framework.

Recommended usage: Use Strong, not Secure, in this expansion. State the jurisdiction and applicable rules before describing requirements or exemptions.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Strong Customer Authentication); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Strong Customer Authentication (SCA)); [T27](https://docs.adyen.com/online-payments/3d-secure-for-regulation-compliance) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G119: SCA exemption

Permitted exception to applying SCA for a transaction that remains within the relevant regulatory scope.

Recommended usage: Name the exemption and decision-maker. An exemption request can be rejected and is not the same as an out-of-scope transaction.

Status: editorial proposal.

Sources: [T27](https://docs.adyen.com/online-payments/3d-secure-for-regulation-compliance) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T31S](https://docs.stripe.com/payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G120: out-of-scope transaction

Transaction that does not fall within the stated authentication requirement's scope.

Recommended usage: State the specific scope test. Do not use out of scope as a synonym for an exemption or frictionless authentication.

Status: editorial proposal.

Sources: [T27](https://docs.adyen.com/online-payments/3d-secure-for-regulation-compliance) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G121: transaction risk analysis (TRA)

Risk-based assessment used in the applicable framework to support a permitted authentication exemption.

Recommended usage: State the provider, region, and legal conditions. Do not publish one universal TRA amount or fraud threshold.

Status: editorial proposal.

Sources: [T27](https://docs.adyen.com/online-payments/3d-secure-for-regulation-compliance) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G122: delegated authentication

Arrangement in which an approved party performs specified authentication functions under applicable rules.

Recommended usage: Name the delegating party, authenticating party, and scope. Do not infer delegation merely because a merchant uses biometrics.

Status: editorial proposal.

Sources: [T27](https://docs.adyen.com/online-payments/3d-secure-for-regulation-compliance) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [T29](https://docs.adyen.com/online-payments/authentication) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G123: liability shift

Rule-based transfer of responsibility for specified fraud losses between participating parties.

Recommended usage: State the network, environment, fraud category, authentication outcome, and exceptions. It is not a guarantee of winning every dispute.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 4); [T31S](https://docs.stripe.com/payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; PDF p. 7)

## G124: two-factor authentication (2FA)

Authentication using two distinct factors from the applicable authentication categories.

Recommended usage: Name the factors. Two steps or two credentials of the same factor type do not necessarily constitute two factors.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Two-factor authentication (2FA) / one-time password (OTP)); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row); [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G125: multi-factor authentication (MFA)

Authentication requiring more than one distinct factor under the relevant method.

Recommended usage: Describe factor independence and the authentication context. Do not treat every SMS or challenge flow as MFA automatically.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Multi-Factor); [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Two-factor authentication (2FA) / one-time password (OTP))

## G126: one-time password (OTP)

Password or code intended for one authentication use or a limited validity period.

Recommended usage: State the channel, expiry, and validation outcome where relevant. An OTP is a mechanism, not evidence that SCA always applies or is satisfied.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Two-factor authentication (2FA) / one-time password (OTP)); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; Related concept source; exact phrase not located); [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G127: PIN

Personal identification code used in the applicable cardholder-verification or authorization process.

Recommended usage: Use the network's exact PIN context. Do not use PIN as a generic term for every verification code.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 852); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. PIN bypass); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G128: card security code

Card verification or validation value used under the relevant network's scheme.

Recommended usage: Use CVV2 for the applicable Visa value and CVC 2 for the applicable Mastercard value. Do not replace an authentication cryptogram with a card security code.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 852); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 3); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Card security code (CVC, CVV, CID))

## G129: cardholder authentication verification value (CAVV)

Visa authentication value associated with the result of a cardholder authentication request.

Recommended usage: Keep CAVV distinct from CVV2, authorization code, ECI, and a payment token.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 852); [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 104)

## G130: cryptogram

Cryptographic value used to validate specified data, its source, or its integrity.

Recommended usage: Name the cryptogram type and protocol. It is not a reusable card number, ordinary password, or general approval code.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 846); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 70)

## G131: electronic commerce indicator (ECI)

Network data indicator describing the ecommerce authentication or transaction context.

Recommended usage: Interpret the exact value using the network and protocol version. The same numeric value is not universally meaningful across networks.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 866); [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G132: identity verification

Assessment of evidence linking a person or entity to a claimed identity.

Recommended usage: Distinguish identity verification from address matching, payment authorization, and customer-account authentication.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Identification and Verification); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Know Your Customer (KYC)); [T26](https://docs.adyen.com/platforms/identify-account-holder-risk) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G133: know your customer (KYC)

Customer-identification and due-diligence activities required for the relevant financial or business relationship.

Recommended usage: State the obligated entity, jurisdiction, and relationship. Do not imply that an ordinary merchant fraud check satisfies every KYC duty.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Know Your Customer (KYC)); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row); [T26](https://docs.adyen.com/platforms/identify-account-holder-risk) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G134: know your business (KYB)

Verification and due diligence relating to a business customer or counterparty.

Recommended usage: Identify the business, controlling persons, and applicable requirements. Do not treat a company-name match as complete due diligence.

Status: editorial proposal.

Sources: [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row); [T26](https://docs.adyen.com/platforms/identify-account-holder-risk) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G135: fraud

Deceptive or unauthorized activity intended to obtain value or cause an improper payment outcome.

Recommended usage: Identify the evidence and fraud type. Do not label every failed payment, dispute, or suspicious signal as confirmed fraud.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Fraud); [T9](https://docs.stripe.com/disputes/prevention/fraud-types) (Living documentation; retrieved 17–18 November 2026; page text); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 4)

## G136: third-party payment fraud

Unauthorized payment activity using another person's account or payment credentials.

Recommended usage: Distinguish it from cardholder-authorized purchases and legitimate consumer disputes.

Status: editorial proposal.

Sources: [T9](https://docs.stripe.com/disputes/prevention/fraud-types) (Living documentation; retrieved 17–18 November 2026; page text); [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 4)

## G137: first-party misuse

Misuse of a purchase or dispute process by a purchaser or another authorized participant.

Recommended usage: State the observed facts. Do not assume intentional fraud solely because the customer disputed a purchase.

Status: editorial proposal.

Sources: [T9](https://docs.stripe.com/disputes/prevention/fraud-types) (Living documentation; retrieved 17–18 November 2026; page text); [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; Related concept source; exact phrase not located)

## G138: account takeover (ATO)

Unauthorized control or use of an existing customer or user account.

Recommended usage: Separate account compromise, payment-credential theft, and the later payment outcome; one does not automatically prove the others.

Status: editorial proposal.

Sources: [T9](https://docs.stripe.com/disputes/prevention/fraud-types) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [V9](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/pfd-biannual-threats-report-december-2023.pdf) (December 2023 historical threat report; Related concept source; exact phrase not located)

## G139: credential stuffing

Automated use of previously obtained credential pairs to try to access other accounts.

Recommended usage: Distinguish it from guessing new passwords, card enumeration, and ordinary failed logins.

Status: editorial proposal.

Sources: [T35](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [V9](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/pfd-biannual-threats-report-december-2023.pdf) (December 2023 historical threat report; PDF p. 13)

## G140: brute-force attack

Repeated attempts to discover a secret or valid value by trying possibilities.

Recommended usage: Name the target, such as passwords or card values; do not conflate all automated testing with credential stuffing.

Status: editorial proposal.

Sources: [T35](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [V9](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/pfd-biannual-threats-report-december-2023.pdf) (December 2023 historical threat report; PDF p. 29)

## G141: card testing

Attempts to determine whether card credentials can be used successfully, commonly through payment or setup requests.

Recommended usage: Identify the tested credentials and request types. Failed attempts can still be relevant attack evidence.

Status: editorial proposal.

Sources: [T4](https://docs.stripe.com/disputes/prevention/card-testing) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 12); [V9](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/pfd-biannual-threats-report-december-2023.pdf) (December 2023 historical threat report; Related concept source; exact phrase not located)

## G142: enumeration attack

Systematic submission of transaction data to discover or validate payment-account information.

Recommended usage: Use the network's measured event definition when calculating a program ratio. Do not substitute ordinary decline counts for confirmed enumeration.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 868); [V9](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/pfd-biannual-threats-report-december-2023.pdf) (December 2023 historical threat report; PDF p. 2); [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1)

## G143: bot

Software that performs interactions automatically.

Recommended usage: Describe the activity and evidence. Automation alone does not prove malicious intent or payment fraud.

Status: editorial proposal.

Sources: [T4](https://docs.stripe.com/disputes/prevention/card-testing) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [T35](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [V9](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/pfd-biannual-threats-report-december-2023.pdf) (December 2023 historical threat report; PDF p. 19)

## G144: fraud signal

Observed attribute or event used as evidence in a risk assessment.

Recommended usage: Separate a signal from a rule decision, model score, and confirmed fraud outcome.

Status: editorial proposal.

Sources: [T5](https://docs.stripe.com/radar/risk-evaluation) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T19](https://docs.adyen.com/risk-management/fraud-data-collection) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T3](https://docs.stripe.com/radar/rules) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G145: risk score

Model or system output expressing an estimated level of risk under a specified scale.

Recommended usage: Name the provider, model, scale, and decision rule. Scores from different systems are not automatically comparable.

Status: editorial proposal.

Sources: [T5](https://docs.stripe.com/radar/risk-evaluation) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T6](https://docs.stripe.com/radar/risk-settings) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T20](https://docs.adyen.com/risk-management/configure-automated-risk) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G146: risk assessment

Evaluation of available evidence to estimate risk and determine the appropriate treatment.

Recommended usage: State the scope and evidence. It is not proof of fraud and does not necessarily make the authorization decision.

Status: editorial proposal.

Sources: [T5](https://docs.stripe.com/radar/risk-evaluation) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T20](https://docs.adyen.com/risk-management/configure-automated-risk) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Risk management)

## G147: fraud screening

Evaluation of an account, order, or transaction for indicators of fraud.

Recommended usage: State whether screening occurs before authorization, after authorization, or during fulfillment.

Status: editorial proposal.

Sources: [T3](https://docs.stripe.com/radar/rules) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T5](https://docs.stripe.com/radar/risk-evaluation) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T20](https://docs.adyen.com/risk-management/configure-automated-risk) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G148: risk rule

Specified condition and action used to evaluate or treat a payment or account risk.

Recommended usage: Name the exact condition, action, precedence, and provider. A rule match is not a confirmed fraud label.

Status: editorial proposal.

Sources: [T3](https://docs.stripe.com/radar/rules) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T20](https://docs.adyen.com/risk-management/configure-automated-risk) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T6](https://docs.stripe.com/radar/risk-settings) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G149: manual review

Human assessment of a transaction or account that needs further evaluation.

Recommended usage: Identify the reviewer decision and its effect. Review approval is separate from issuer authorization and capture.

Status: editorial proposal.

Sources: [T3](https://docs.stripe.com/radar/rules) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T5](https://docs.stripe.com/radar/risk-evaluation) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Manual Keyed Entry (MKE)/Keyed)

## G150: allow list

List of entities or attributes given a specified permitted treatment by a risk system.

Recommended usage: State the matching scope and action. Listing a customer does not override issuer declines or every provider control.

Status: editorial proposal.

Sources: [T3](https://docs.stripe.com/radar/rules) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T6](https://docs.stripe.com/radar/risk-settings) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G151: block list

List of entities or attributes to which a specified blocking rule applies.

Recommended usage: Name the list owner, matching criteria, and duration. Prefer block list to ambiguous blacklist in Atlas prose.

Status: editorial proposal.

Sources: [T3](https://docs.stripe.com/radar/rules) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T6](https://docs.stripe.com/radar/risk-settings) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G152: device fingerprint

Collection or representation of device and browser attributes used to recognize a device or assess risk.

Recommended usage: State provider and collection context. A fingerprint is not an infallible person identifier and may change.

Status: editorial proposal.

Sources: [T18](https://docs.adyen.com/risk-management/device-fingerprinting) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T19](https://docs.adyen.com/risk-management/fraud-data-collection) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G153: IP address

Address used to identify a network endpoint in the relevant internet protocol context.

Recommended usage: Do not treat an IP address as a unique person, payment account, or reliable physical address.

Status: editorial proposal.

Sources: [T19](https://docs.adyen.com/risk-management/fraud-data-collection) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T35](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G154: IP geolocation

Estimate of geographic location based on an IP address and a data service.

Recommended usage: Label the result as an estimate, name the source, and account for proxies, mobile networks, and VPNs.

Status: editorial proposal.

Sources: [T19](https://docs.adyen.com/risk-management/fraud-data-collection) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T5](https://docs.stripe.com/radar/risk-evaluation) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G155: proxy

Intermediary through which network traffic is relayed.

Recommended usage: Describe the observed network arrangement. Proxy use alone does not establish fraudulent intent.

Status: editorial proposal.

Sources: [T19](https://docs.adyen.com/risk-management/fraud-data-collection) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [T35](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G156: virtual private network (VPN)

Network arrangement that carries traffic through an encrypted or controlled tunnel.

Recommended usage: Treat its presence as contextual evidence, not proof of a shopper's true location or fraud.

Status: editorial proposal.

Sources: [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row); [T19](https://docs.adyen.com/risk-management/fraud-data-collection) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [T35](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G157: email verification

Checks used to assess an email address, domain, or its control by a user.

Recommended usage: State what was checked: syntax, deliverability, ownership, age, or reputation. Do not claim these checks prove identity.

Status: editorial proposal.

Sources: [T7](https://docs.stripe.com/disputes/prevention/best-practices) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T19](https://docs.adyen.com/risk-management/fraud-data-collection) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G158: disposable email address

Email address supplied for temporary or easily replaced use.

Recommended usage: Describe the identified domain or service. Temporary use alone does not establish payment fraud.

Status: editorial proposal.

Sources: [T19](https://docs.adyen.com/risk-management/fraud-data-collection) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [T7](https://docs.stripe.com/disputes/prevention/best-practices) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G159: behavioral biometrics

Analysis of interaction patterns used to distinguish activity or support an identity and risk assessment.

Recommended usage: Describe the measured behavior and confidence. Do not equate probabilistic behavior analysis with certain identity proof.

Status: editorial proposal.

Sources: [T19](https://docs.adyen.com/risk-management/fraud-data-collection) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T20](https://docs.adyen.com/risk-management/configure-automated-risk) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G160: machine learning

Use of models learned from data to estimate outcomes or classify events.

Recommended usage: State the model's purpose and evaluation basis. A model prediction is not a confirmed fraud outcome.

Status: editorial proposal.

Sources: [T5](https://docs.stripe.com/radar/risk-evaluation) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [T23](https://docs.adyen.com/risk-management/configure-your-risk-profile/machine-learning-rules) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G161: false positive

Legitimate case incorrectly classified as fraud or another positive condition in the stated evaluation.

Recommended usage: Name the label, decision, and ground-truth method. Do not equate all customer complaints or issuer declines with false positives.

Status: editorial proposal.

Sources: [T5](https://docs.stripe.com/radar/risk-evaluation) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T6](https://docs.stripe.com/radar/risk-settings) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T20](https://docs.adyen.com/risk-management/configure-automated-risk) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G162: false decline

Decline of a payment that would otherwise be legitimate under the stated assessment.

Recommended usage: Identify who declined and why. A false-positive fraud decision and an issuer decline are not necessarily the same event.

Status: editorial proposal.

Sources: [T5](https://docs.stripe.com/radar/risk-evaluation) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T6](https://docs.stripe.com/radar/risk-settings) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Authentication)

## G163: fraud loss

Financial loss attributable to the stated fraudulent activity under a defined accounting method.

Recommended usage: Specify included amounts, recoveries, fees, timing, and loss owner. Do not substitute fraud-report counts for monetary loss.

Status: editorial proposal.

Sources: [V9](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/pfd-biannual-threats-report-december-2023.pdf) (December 2023 historical threat report; PDF p. 1); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 3); [T9](https://docs.stripe.com/disputes/prevention/fraud-types) (Living documentation; retrieved 17–18 November 2026; page text)

## G164: social engineering

Manipulation of a person to disclose information, transfer money, or perform another harmful action.

Recommended usage: Describe the deception and observed result. Distinguish it from the payment network's formal dispute classification.

Status: editorial proposal.

Sources: [V8](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/pfd-fraud-protection-guide-social-engineering.pdf) (2023 fraud guide; PDF p. 1); [V9](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/pfd-biannual-threats-report-december-2023.pdf) (December 2023 historical threat report; PDF p. 4)

## G165: phishing

Deceptive communication or site used to obtain information or induce an unsafe action by impersonating a trusted party.

Recommended usage: Name the channel and impersonated party. Do not label every unsolicited message or suspicious domain as confirmed phishing.

Status: editorial proposal.

Sources: [V9](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/pfd-biannual-threats-report-december-2023.pdf) (December 2023 historical threat report; PDF p. 10); [T35](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G166: spoofing

Falsification of an apparent identity, address, or source to mislead a recipient or system.

Recommended usage: State what was falsified and the supporting evidence; do not infer spoofing solely from a data mismatch.

Status: editorial proposal.

Sources: [V8](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/pfd-fraud-protection-guide-social-engineering.pdf) (2023 fraud guide; PDF p. 1); [V9](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/pfd-biannual-threats-report-december-2023.pdf) (December 2023 historical threat report; Related concept source; exact phrase not located)

## G167: data breach

Unauthorized exposure of or access to protected data.

Recommended usage: State the data and event scope. A suspicious transaction alone does not establish a breach.

Status: editorial proposal.

Sources: [V9](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/pfd-biannual-threats-report-december-2023.pdf) (December 2023 historical threat report; PDF p. 2); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 7)

## G168: data protection

Controls and obligations used to safeguard data and regulate its processing.

Recommended usage: State the applicable data category, purpose, access, retention, and governing requirements.

Status: editorial proposal.

Sources: [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 2); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 842); [T28](https://www.pcisecuritystandards.org/glossary) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G169: sensitive authentication data

Security information used to authenticate cardholders or authorize transactions under PCI definitions.

Recommended usage: Use the current PCI category and handling requirements; do not treat every card-data field as belonging to the same category.

Status: editorial proposal.

Sources: [T28](https://www.pcisecuritystandards.org/glossary) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 18)

## G170: cardholder data

Payment-card data classified as cardholder data under the applicable PCI definition.

Recommended usage: Use the defined data elements and scope. Keep it distinct from sensitive authentication data and general personal information.

Status: editorial proposal.

Sources: [T28](https://www.pcisecuritystandards.org/glossary) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 10)

## G171: PCI DSS

Payment Card Industry Data Security Standard.

Recommended usage: Use the applicable version and scope. Do not describe a payment flow as compliant solely because it uses tokens or a compliant provider.

Status: editorial proposal.

Sources: [T28](https://www.pcisecuritystandards.org/glossary) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 20)

## G172: encryption

Cryptographic transformation that makes data unreadable without the required key or process.

Recommended usage: Distinguish encryption from hashing, truncation, and tokenization. State the protection context rather than claiming complete security.

Status: editorial proposal.

Sources: [T28](https://www.pcisecuritystandards.org/glossary) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 21)

## G173: hashing

Transformation of input data into a fixed representation using a defined hash function.

Recommended usage: Distinguish a hash from reversible encryption and payment tokenization; state the function and use case when relevant.

Status: editorial proposal.

Sources: [T28](https://www.pcisecuritystandards.org/glossary) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; Related concept source; exact phrase not located)

## G174: personal data

Information relating to an identified or identifiable person under the applicable legal definition.

Recommended usage: State the jurisdiction and processing purpose. Do not assume a single worldwide definition or retention requirement.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 842); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Personal Data); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 8)

## G175: dispute

Challenge to a transaction handled under an applicable provider or network dispute process.

Recommended usage: Distinguish the customer's complaint from a formally initiated network dispute. For Visa, use its official dispute stage names.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 844); [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 1); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Dispute)

## G176: chargeback

Issuer-initiated return of a disputed transaction through a card-network mechanism.

Recommended usage: Name the network and stage. It is not a merchant refund, an informal complaint, or every pre-dispute alert.

Status: editorial proposal.

Sources: [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; PDF p. 11); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Chargeback); [T8](https://docs.stripe.com/disputes/categories) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G177: dispute condition

Network-defined basis and requirements for raising and responding to a dispute.

Recommended usage: Preserve the network, identifier, title, and edition. A similar reason on another network is not automatically equivalent.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 12); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 24)

## G178: dispute response

Submission responding to a formal dispute under the applicable network or provider process.

Recommended usage: Name the stage and grounds. Supplying evidence does not guarantee acceptance or a reversal of liability.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 855); [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 9); [T8](https://docs.stripe.com/disputes/categories) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G179: second presentment

Mastercard acquirer submission responding to a chargeback with the grounds and supporting information for rejecting it.

Recommended usage: Use the Mastercard stage name. Do not replace Visa dispute response with second presentment without a verified cross-network mapping.

Status: editorial proposal.

Sources: [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; PDF p. 11)

## G180: representment

Industry or provider term for returning a disputed transaction with a response to the chargeback.

Recommended usage: Prefer the exact network stage, such as Mastercard second presentment or Visa dispute response, in network-specific instructions.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Chargeback); [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; PDF p. 11); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 854)

## G181: pre-arbitration

Dispute escalation or response stage before network arbitration when the applicable process permits or requires it.

Recommended usage: State the network and dispute flow. Do not imply that it is mandatory or available in every case.

Status: editorial proposal.

Sources: [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; PDF p. 11); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 855)

## G182: arbitration

Network process for deciding financial responsibility in an eligible escalated case.

Recommended usage: Name the network. Keep this payment-network process distinct from court proceedings or consumer-contract arbitration.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 844); [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; PDF p. 11)

## G183: compliance case

Process addressing a financial loss attributed to a network-rule violation under the applicable eligibility rules.

Recommended usage: Do not present compliance as an unrestricted alternative when chargeback rights are unavailable or prohibited.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 844); [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; PDF p. 11)

## G184: supporting documentation

Records submitted to support a position or required fact in a payment or dispute process.

Recommended usage: Provide relevant, transaction-linked material for the specified condition and stage. More documents do not necessarily establish a stronger case.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 12); [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; PDF p. 7)

## G185: proof of delivery

Records offered to show that goods or services were delivered or received as agreed.

Recommended usage: State what the record actually establishes and who received the item. A delivery scan does not automatically prove cardholder authorization.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 6); [T8](https://docs.stripe.com/disputes/categories) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G186: compelling evidence 3.0 (CE3.0)

Visa framework for qualifying evidence in specified card-absent fraud dispute circumstances.

Recommended usage: State the condition and qualification criteria. It does not apply to every dispute or guarantee that a claim will be prevented or defeated.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 5); [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1)

## G187: fraud report

Record submitted or supplied to identify an event reported as fraudulent.

Recommended usage: Name the reporting system and label status. A fraud report is not automatically a chargeback or a proven fraud loss.

Status: editorial proposal.

Sources: [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 4); [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 4)

## G188: TC40

Visa transaction-code reference associated with issuer-reported fraud information.

Recommended usage: Distinguish fraud reporting from TC15 disputes. State the reporting extract and program treatment before calculating a ratio.

Status: editorial proposal.

Sources: [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1)

## G189: TC15

Visa transaction-code reference used for disputes in the cited VAMP metric.

Recommended usage: State the eligible count, exclusions, time period, and data-extract timing. Do not equate it with all customer complaints.

Status: editorial proposal.

Sources: [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1)

## G190: TC05

Visa transaction-code reference used for settled transactions in the cited VAMP denominator.

Recommended usage: Use the program's stated eligible transaction population. Do not substitute authorization attempts or order count.

Status: editorial proposal.

Sources: [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1)

## G191: System to Avoid Fraud Effectively (SAFE)

Mastercard fraud-reporting system identified in Mastercard security requirements.

Recommended usage: Use SAFE as a network-qualified system name; do not call Mastercard reporting TC40 or treat a report as a chargeback.

Status: editorial proposal.

Sources: [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; Related concept source; exact phrase not located); [EFW](https://docs.stripe.com/disputes/how-disputes-work) (Living documentation; retrieved 18 November 2026; Early fraud warnings)

## G192: early fraud warning

Provider notification that an issuer or network has reported suspected or confirmed fraud under that notification system.

Recommended usage: Name the provider and source system. A warning is not itself a dispute, automatic refund instruction, or guaranteed chargeback.

Status: editorial proposal.

Sources: [EFW](https://docs.stripe.com/disputes/how-disputes-work) (Living documentation; retrieved 18 November 2026; Early fraud warnings)

## G193: pre-dispute alert

Notification intended to allow review or resolution before a formal network dispute progresses.

Recommended usage: Name the alert service and its rules. Do not assume every alert has identical deadlines, refund requirements, or counting treatment.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 6); [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G194: rapid dispute resolution (RDR)

Visa pre-dispute service supporting automated acceptance of liability for eligible disputes.

Recommended usage: State the service and configured decision. Acceptance is not the same as winning a contested dispute.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 901); [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 6)

## G195: chargeback deflection

Activity or service intended to resolve or prevent an eligible issue before a chargeback progresses.

Recommended usage: Name the specific service and outcome. Do not promise that an alert, data-sharing service, or refund always prevents a dispute.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 6); [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1)

## G196: duplicate refund risk

Risk that a merchant refund and a separate dispute-related credit return value for the same purchase.

Recommended usage: Check the payment, refund, and dispute records before issuing another credit; do not assume provider offsets are automatic.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 3); [T8](https://docs.stripe.com/disputes/categories) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G197: unauthorized transaction

Transaction asserted or determined not to have been authorized by the relevant account holder under the applicable process.

Recommended usage: Separate the customer's allegation from an established finding and the network's required dispute evidence.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 4); [T8](https://docs.stripe.com/disputes/categories) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G198: goods or services not received

Dispute basis alleging that agreed goods or services were not provided as required.

Recommended usage: Use the exact network condition and expected delivery facts. Do not merge it with unauthorized-use or not-as-described disputes.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 62); [T8](https://docs.stripe.com/disputes/categories) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G199: not as described

Dispute basis alleging that goods or services differed from the agreed description or condition.

Recommended usage: Use the exact condition and supporting facts. Do not automatically classify a quality complaint as third-party fraud.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 4); [T8](https://docs.stripe.com/disputes/categories) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G200: credit not processed

Dispute basis alleging that an agreed or required credit was not completed.

Recommended usage: Check the credit agreement, processing records, timing, and exact network condition. A refund request alone does not establish completed credit.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 4); [T8](https://docs.stripe.com/disputes/categories) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G201: canceled recurring transaction dispute

Dispute basis concerning a recurring payment processed after the relevant cancellation.

Recommended usage: Use the network condition and cancellation evidence. Do not infer whether a claim is valid from the merchant's subscription label alone.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 4); [T8](https://docs.stripe.com/disputes/categories) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G202: VAMP

Visa Acquirer Monitoring Program, which monitors specified fraud, dispute, and enumeration activity.

Recommended usage: Use the current program guide for the region and date. Do not substitute historical VFMP or VDMP criteria.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 110); [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1)

## G203: VAMP ratio

Count-based ratio of eligible fraud and disputes to settled transactions under the applicable VAMP rules.

Recommended usage: Use the stated eligible TC40, TC15, and TC05 populations, extract timing, exclusions, and reporting period. Keep thresholds in versioned rules.

Status: editorial proposal.

Sources: [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1)

## G204: VAMP enumeration ratio

Ratio of eligible enumerated authorization transactions to eligible authorization transactions under VAMP.

Recommended usage: Include approved and declined events as specified. Do not substitute the fraud-and-dispute ratio or ordinary decline rate.

Status: editorial proposal.

Sources: [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1)

## G205: Visa Fraud Monitoring Program (VFMP)

Historical Visa program name for fraud monitoring.

Recommended usage: Retain it in historical material and verify the relevant region and effective date; do not present its old thresholds as current VAMP rules.

Status: editorial proposal.

Sources: [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1)

## G206: Visa Dispute Monitoring Program (VDMP)

Historical Visa program name for dispute monitoring.

Recommended usage: Preserve it when describing historical periods. Check the current VAMP framework before giving current obligations or calculations.

Status: editorial proposal.

Sources: [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1)

## G207: excessive chargeback program (ECP)

Mastercard program for monitoring merchant chargeback performance under its defined rules.

Recommended usage: Use Mastercard ECP in this context. ECP can mean electronic check presentment elsewhere, so never expand it without context.

Status: editorial proposal.

Sources: [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 5)

## G208: excessive chargeback merchant (ECM)

Merchant identified in Mastercard's ECM category under the relevant monitoring rules.

Recommended usage: Keep category, program, month, and MID scope together. Do not treat ECM as the name of a separate universal program.

Status: editorial proposal.

Sources: [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 82)

## G209: high excessive chargeback merchant (HECM)

Merchant identified in Mastercard's HECM category under the relevant monitoring rules.

Recommended usage: Use the exact category and current rule source. Do not infer a current threshold from an old merchant discussion.

Status: editorial proposal.

Sources: [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 88)

## G210: merchant monitoring program (MMP)

Mastercard program covering the merchant-monitoring obligations described in the applicable security rules.

Recommended usage: Use the full network-qualified program title and edition. Do not assume similarly named monitoring programs use the same scope or metric.

Status: editorial proposal.

Sources: [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 6)

## G211: questionable merchant audit program (QMAP)

Mastercard program for investigating merchant activity under its defined audit rules.

Recommended usage: Describe the identified program and finding, rather than calling every high-risk merchant questionable.

Status: editorial proposal.

Sources: [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 5)

## G212: excessive fraud merchant (EFM)

Mastercard merchant classification under the applicable excessive-fraud monitoring provisions.

Recommended usage: Use the current program definition, market, and date. Do not substitute a generic fraud rate or historical threshold.

Status: editorial proposal.

Sources: [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 82)

## G213: MATCH

Mastercard system used for specified merchant-termination and acquiring-risk information.

Recommended usage: Use the current system and rule terminology. A MATCH result is not a general-purpose proof of criminal fraud.

Status: editorial proposal.

Sources: [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 6); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: MATCH); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G214: interchange

Exchange of clearing records between participating network institutions.

Recommended usage: Distinguish the processing exchange from interchange reimbursement fees when using the standalone word.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 876)

## G215: interchange fee

Fee applied between acquiring and issuing participants under the relevant payment-network fee framework.

Recommended usage: Name the network, market, product, and fee basis. Do not equate interchange with the merchant's entire processing cost.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Interchange fee); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 876); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Interchange fee)

## G216: scheme fee

Fee charged under a card network's pricing framework for specified participation or transaction services.

Recommended usage: State the network and charge basis. Keep it distinct from interchange and the PSP or acquirer margin.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Scheme fee); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 844); [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Scheme fee)

## G217: merchant discount fee

Fee a merchant pays an acquirer for acquiring the merchant's transactions.

Recommended usage: State what the quoted fee includes and how it is calculated. It is not necessarily identical to interchange alone.

Status: editorial proposal.

Sources: [M1](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/mastercard-rules.pdf) (2 June 2026; Related term lookup: Merchant discount fee); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G218: interchange-plus-plus pricing (IC++)

Pricing presentation separating interchange, network fees, and the provider's acquiring or processing charge.

Recommended usage: Specify the contract and included fee categories. Do not assume all providers present identical IC++ components.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Scheme fee)

## G219: basis point

One hundredth of one percentage point, equal to 0.01%.

Recommended usage: Use basis points for the unit. A change from 1% to 2% is 100 basis points, not a 1% relative increase.

Status: editorial proposal.

Sources: [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 45)

## G220: authorization approval rate

Proportion of the stated authorization-request population that received approval.

Recommended usage: Specify counting unit, attempts or unique payments, dates, exclusions, and partial approvals. This is a measurement definition, not a universal network formula.

Status: editorial proposal.

Sources: [V4](https://usa.visa.com/content/dam/VCOM/regional/na/us/support-legal/documents/authorization-and-reversal-processing-best-practices-for-merchants.pdf) (2024 guide; PDF p. 1); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Authorization); [T6](https://docs.stripe.com/radar/risk-settings) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G221: payment conversion rate

Proportion of the stated payment or checkout population that reaches the defined successful outcome.

Recommended usage: Name the funnel stage and denominator. Do not automatically substitute issuer approval rate, capture rate, or order conversion.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Payment conversion rate)

## G222: success rate

Proportion reaching a stated successful outcome in a specified population and period.

Recommended usage: Always name the successful state, counting unit, denominator, and measurement window.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Payment conversion rate); [T1](https://docs.stripe.com/payments/paymentintents/lifecycle) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G223: chargeback ratio

Ratio of eligible chargebacks to the transaction population specified by the relevant program or measurement policy.

Recommended usage: State the network formula and periods; the numerator and denominator may use different months. Do not replace it with VAMP ratio.

Status: editorial proposal.

Sources: [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 5); [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; Related concept source; exact phrase not located)

## G224: fraud rate

Ratio expressing fraud frequency or value in a specified payment population.

Recommended usage: State whether it is count-based or amount-based, the label source, denominator, and period. Do not treat all fraud-rate formulas as equivalent.

Status: editorial proposal.

Sources: [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 4)

## G225: dispute win rate

Proportion of the stated resolved dispute population with the defined favorable outcome.

Recommended usage: Define favorable outcome, contested versus all disputes, cohort, reversals, and unresolved cases. Do not count automatic liability acceptance as a contested win.

Status: editorial proposal.

Sources: [V2](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/merchants-dispute-management-guidelines.pdf) (October 2026; PDF p. 1); [T8](https://docs.stripe.com/disputes/categories) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G226: false-positive rate

Proportion of actual negative or legitimate cases incorrectly classified as positive in the stated evaluation.

Recommended usage: Define ground truth and population. Do not divide by all flagged cases and call that the false-positive rate.

Status: editorial proposal.

Sources: [T5](https://docs.stripe.com/radar/risk-evaluation) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T6](https://docs.stripe.com/radar/risk-settings) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T20](https://docs.adyen.com/risk-management/configure-automated-risk) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G227: refund rate

Ratio of refunds to a stated purchase or payment population under a defined measurement policy.

Recommended usage: State whether the ratio uses counts or amounts, transaction or processing dates, and partial-refund treatment.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Refund); [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Refund)

## G228: threshold

Boundary used to trigger a stated classification, action, or program outcome.

Recommended usage: Include the unit, comparison operator, scope, effective date, and complete conditions. Do not transfer thresholds between programs or providers.

Status: editorial proposal.

Sources: [V10](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf) (2025 fact sheet, with 2026 implementation notes; PDF p. 1); [M3](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/SPME-Manual.pdf) (4 August 2026; PDF p. 69); [T6](https://docs.stripe.com/radar/risk-settings) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G229: dunning

Process for recovering an unpaid amount, often through payment retries and customer communication.

Recommended usage: Describe the permitted recovery actions. Do not confuse dunning with chargeback representment or collections after a dispute.

Status: editorial proposal.

Sources: [T10](https://docs.stripe.com/billing/revenue-recovery/smart-retries) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T11](https://docs.stripe.com/billing/revenue-recovery) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T13](https://docs.stripe.com/invoicing/automatic-collection) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G230: payment retry

New attempt to collect a payment after a prior unsuccessful attempt.

Recommended usage: Identify the previous outcome, applicable advice, consent, and permitted retry policy. Never prescribe a universal retry count or interval.

Status: editorial proposal.

Sources: [T10](https://docs.stripe.com/billing/revenue-recovery/smart-retries) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [M2](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/transaction-processing-rules.pdf) (9 June 2026; Related term lookup: Retries)

## G231: soft decline

Provider or scheme classification indicating that another action or a later permitted attempt may succeed.

Recommended usage: Preserve the exact code and required action. Soft does not authorize unlimited retries or bypass required authentication.

Status: editorial proposal.

Sources: [P1](https://docs.stripe.com/declines/codes) (Living documentation; retrieved 17–18 November 2026; page text); [T10](https://docs.stripe.com/billing/revenue-recovery/smart-retries) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T27](https://docs.adyen.com/online-payments/3d-secure-for-regulation-compliance) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G232: hard decline

Provider or scheme classification for a decline that requires correction or disallows the stated retry path.

Recommended usage: Interpret the specific code and advice. Do not infer the same retry treatment across every processor from the label hard.

Status: editorial proposal.

Sources: [P1](https://docs.stripe.com/declines/codes) (Living documentation; retrieved 17–18 November 2026; page text); [T10](https://docs.stripe.com/billing/revenue-recovery/smart-retries) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G233: involuntary churn

Loss of an otherwise continuing subscription or customer relationship because payment collection fails.

Recommended usage: Distinguish payment failure from the customer's deliberate cancellation and define how churn is measured.

Status: editorial proposal.

Sources: [T10](https://docs.stripe.com/billing/revenue-recovery/smart-retries) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T11](https://docs.stripe.com/billing/revenue-recovery) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G234: revenue recovery

Activities to collect eligible unpaid revenue, including supported retry and customer-notification processes.

Recommended usage: State the unpaid amount and permitted actions; do not equate recovered revenue with chargeback wins or guaranteed future payments.

Status: editorial proposal.

Sources: [T11](https://docs.stripe.com/billing/revenue-recovery) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T10](https://docs.stripe.com/billing/revenue-recovery/smart-retries) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G235: manual review queue

Set of cases waiting for or undergoing human risk assessment.

Recommended usage: Name the case population, entry and exit states, priority, and service target. Queue volume is not necessarily fraud volume.

Status: editorial proposal.

Sources: [T3](https://docs.stripe.com/radar/rules) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T5](https://docs.stripe.com/radar/risk-evaluation) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G236: velocity rule

Risk rule evaluating counts or values of activity over a specified interval and matching key.

Recommended usage: State key, event types, window, reset behavior, and action. Do not count retries as unique customers unless intended.

Status: editorial proposal.

Sources: [T3](https://docs.stripe.com/radar/rules) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located); [T20](https://docs.adyen.com/risk-management/configure-automated-risk) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G237: device spoofing

Manipulation of reported device or browser attributes to misrepresent the device context.

Recommended usage: Describe the inconsistent or altered attributes and evidence. A changed fingerprint does not alone establish deliberate spoofing.

Status: editorial proposal.

Sources: [T18](https://docs.adyen.com/risk-management/device-fingerprinting) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T19](https://docs.adyen.com/risk-management/fraud-data-collection) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G238: account verification

Assessment of specified account details, ownership, status, or usability.

Recommended usage: State what is verified and by which mechanism. A zero-value card check is not the same as bank-account ownership verification.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Zero-value auth); [T21](https://docs.stripe.com/payments/ach-direct-debit) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 840)

## G239: zero-value authorization

Authorization or verification request using a zero amount in a supported card-verification flow.

Recommended usage: Use the exact network and provider operation. Do not treat it as a completed purchase or an automatic consent record.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Zero-value auth); [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 837)

## G240: mandate

Recorded permission or agreement for specified payment actions under the applicable method and rules.

Recommended usage: State the payment method, parties, permitted actions, and cancellation terms. A saved credential alone does not establish every required mandate.

Status: editorial proposal.

Sources: [T1](https://docs.stripe.com/payments/paymentintents/lifecycle) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [T21](https://docs.stripe.com/payments/ach-direct-debit) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [V6](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/stored-credential-transaction-framework-vbs-10-may-17.pdf) (2017 historical guide; PDF p. 10)

## G241: direct debit

Payment method in which a creditor or its provider initiates a debit under the applicable authorization framework.

Recommended usage: Name the scheme and mandate. Card recurring payments and bank direct debits have different rules and return processes.

Status: editorial proposal.

Sources: [T21](https://docs.stripe.com/payments/ach-direct-debit) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Local payment methods (or Alternative payment methods)); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G242: ACH

US Automated Clearing House system and associated payment arrangements.

Recommended usage: Specify ACH credit or debit and the applicable entry and return rules. Do not use ACH chargeback as a substitute for an exact ACH return code.

Status: editorial proposal.

Sources: [T21](https://docs.stripe.com/payments/ach-direct-debit) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G243: ACH return

Return of an ACH entry using the applicable return process and code.

Recommended usage: Retain the precise code and return context. Do not apply card-network dispute stages or deadlines to ACH returns.

Status: editorial proposal.

Sources: [T21](https://docs.stripe.com/payments/ach-direct-debit) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading)

## G244: SEPA

Single Euro Payments Area framework for specified euro payment schemes.

Recommended usage: Name the scheme, such as credit transfer or direct debit, and the relevant scheme rules. SEPA is not a single payment product.

Status: editorial proposal.

Sources: [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G245: IBAN

International Bank Account Number used to identify a bank account under the applicable standard.

Recommended usage: Preserve the value and check format where required. A valid format does not establish ownership, available funds, or payment success.

Status: editorial proposal.

Sources: [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G246: SWIFT

Organization and messaging ecosystem supporting standardized financial communications.

Recommended usage: Name the message or service used. Do not treat a SWIFT message as identical to settlement or guaranteed fund availability.

Status: editorial proposal.

Sources: [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G247: buy now, pay later (BNPL)

Payment arrangement allowing a customer to defer or divide payment under the provider's terms.

Recommended usage: Name the provider and product. Do not assume that every installment payment is BNPL or has identical fraud and dispute rules.

Status: editorial proposal.

Sources: [BNPL](https://docs.stripe.com/payments/buy-now-pay-later) (Living documentation; retrieved 18 November 2026; linked documentation, relevant heading)

## G248: local payment method

Payment method with adoption or operation tied to specified markets or customer groups.

Recommended usage: Name the actual method and market. Local and alternative are contextual labels, not universal method classifications.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Local payment methods (or Alternative payment methods))

## G249: split tender

Use of more than one payment method to pay for one purchase.

Recommended usage: State each amount and method. Do not confuse split tender with splitting a marketplace payout among recipients.

Status: editorial proposal.

Sources: [V7](https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/visa-partial-authorization-service.pdf) (2017 historical service guide; PDF p. 1); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Tender)

## G250: overcapture

Capture exceeding the original authorized amount when the provider and network permit it.

Recommended usage: State the eligible payment type, permitted limit, and provider settings. Do not treat overcapture as universally supported.

Status: editorial proposal.

Sources: [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Overcapture)

## G251: dual message system

Processing arrangement with separate authorization and clearing message stages.

Recommended usage: Use the network-specific system and message names; do not impose the same sequence on single-message processing.

Status: editorial proposal.

Sources: [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; PDF p. 5); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Dual Message System (DMS))

## G252: single message system

Processing arrangement using one message format for authorization and financial processing as specified by the network.

Recommended usage: Qualify SMS as Single Message System in payments processing; SMS also means Short Message Service in communications.

Status: editorial proposal.

Sources: [M4](https://www.mastercard.com/content/dam/mccom/shared/business/support/rules-pdfs/chargebacks-made-simple-guide.pdf) (July 2025; PDF p. 5); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Single Message System (SMS)); [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row)

## G253: interchange downgrade

Application of a different interchange qualification or category because a transaction does not meet the relevant criteria.

Recommended usage: Name the network qualification and fee outcome. Do not use downgrade for every higher processor fee.

Status: editorial proposal.

Sources: [V1](https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf) (24 October 2026; PDF p. 876); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Interchange fee)

## G254: FIDO

Family of authentication standards and associated ecosystem identified by the FIDO Alliance.

Recommended usage: Name the applicable standard or implementation. Do not infer SCA compliance merely from the FIDO label.

Status: editorial proposal.

Sources: [B1](https://glenbrook.com/wp-content/uploads/Glenbrook-Key-Payments-Terminology.pdf) (Undated public terminology PDF; terminology table; exact abbreviation row); [T31](https://docs.adyen.com/online-payments/3d-secure) (Living documentation; retrieved 17–18 November 2026; Related concept source; exact phrase not located)

## G255: application status

Recorded state of an object in a specified provider or application lifecycle.

Recommended usage: Preserve exact enum names and distinguish them from network stages and financial outcomes.

Status: editorial proposal.

Sources: [T1](https://docs.stripe.com/payments/paymentintents/lifecycle) (Living documentation; retrieved 17–18 November 2026; page text; use the linked page heading); [A1](https://docs.adyen.com/adyen-glossary) (Living documentation; retrieved 17–18 November 2026; s.v. Challenge response (cres))
