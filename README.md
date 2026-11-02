# Agent Identity and Trust

MrCakes931 Agent Intelligence Ecosystem · Identity and security layer

Defines principal identity, authentication context, authorization, delegation, revocation, and trust-boundary contracts.

## Scope
- Human, agent, service, and workload principals.
- Issuer-scoped identifiers and credential metadata.
- Default-deny authorization and bounded delegation.
- Key rotation, expiry, revocation, and security audit requirements.

## Current status
Scaffolded, version 0.1.0. The initial principal schema is [schemas/principal.schema.json](schemas/principal.schema.json); see [docs/IDENTITY-TRUST.md](docs/IDENTITY-TRUST.md).

A principal identifier is not proof of authentication, authorization, or human ownership. This repository does not yet operate an identity provider or issue credentials.

## Ecosystem
- Master registry: https://github.com/PCakes303/agent-intelligence-ecosystem
- Main public identity: https://github.com/HuffmanMainNode

## License
Apache-2.0.
