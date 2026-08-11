---
package: AOS_LEAN_PORTABLE_DOCUMENTATION
package_revision: PORTABLE-DRAFT-1
artifact_role: PACKAGE_ENTRYPOINT
status: DRAFT
authority: NONE
source_candidate_identity: sha256:57446e0d8075985af2229eae86cc6cf018b41ec255f0140b7bb20b45ef3ded65
source_audit_identity: sha256:b6cd639302fb719ab7ef47e894075c791d683c3e46b35291c11a2c591f989cfe
source_acceptance_identity: sha256:0353347d106d1985e7b296f721ade4b9e51a1a26a304468b97dc39b00c7598df
frozen_foundation_identity: sha256:b9ef04820f9e71da1866c61c87417c7ac39d1c27c93a74327ab7f40f2e25aebf
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# AOS — Lean Portable Documentation Package

## 1. Outcome

This package is a compact, self-contained handoff for understanding AOS and preparing a future implementation. It retains the accepted full-project design content while removing repository-specific construction history and external navigation dependencies.

AOS is a human-directed, AI-assisted software-development system. Its goal is not maximum agent autonomy, but lower cost of defining, coordinating, checking and continuing software work while the human retains product and protected-action authority.

## 2. Current status

```yaml
candidate_status: DRAFT
authority: NONE
construction_result: PASS
independent_audit: NOT_RUN
human_package_decision: NOT_RUN
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
```

The source DRAFT-R2 content was human-accepted in its declared fact classes. This portable harmonization has different bytes and therefore requires its own manifest, audit and exact package decision.

## 3. Inventory

The candidate contains exactly eleven manifest-bound Markdown content files:

| Order | Artifact | Responsibility |
|---:|---|---|
| 1 | [AGENTS.md](AGENTS.md) | package-local routing and authority boundaries |
| 2 | [README.md](README.md) | entrypoint, status, inventory, portability and identity |
| 3 | [00_PROJECT_CORE.md](00_PROJECT_CORE.md) | identity, mission, precedence, safety and vocabulary |
| 4 | [01_PRODUCT_MODEL.md](01_PRODUCT_MODEL.md) | product problems, users, requirements and capabilities |
| 5 | [02_ARCHITECTURE_CONTRACTS.md](02_ARCHITECTURE_CONTRACTS.md) | WHAT-level architecture and semantic contracts |
| 6 | [03_ENGINEERING_WORKFLOW.md](03_ENGINEERING_WORKFLOW.md) | future engineering workflow and evidence semantics |
| 7 | [04_FEATURE_SPECIFICATIONS.md](04_FEATURE_SPECIFICATIONS.md) | design specifications for `FTR-001…FTR-030` |
| 8 | [05_USER_JOURNEYS_AND_UX.md](05_USER_JOURNEYS_AND_UX.md) | journeys and interface-neutral UX requirements |
| 9 | [06_PROJECT_ROADMAP.md](06_PROJECT_ROADMAP.md) | proposed phases, dependencies and gates |
| 10 | [07_DECISION_REGISTER.md](07_DECISION_REGISTER.md) | accepted ledger, safe states and open choices |
| 11 | [08_TRACEABILITY.md](08_TRACEABILITY.md) | live trace graph and coverage |

[MANIFEST.txt](MANIFEST.txt) binds those eleven files and excludes itself. `PACKAGE_ACCEPTANCE.yaml` is absent until a successful separate audit and exact human `ACCEPT`; it is also excluded from the manifest to avoid recursion.

## 4. Reading order

For a full review, read `00` through `08` in order. For targeted work, use the routes in [AGENTS.md](AGENTS.md). A future coding agent should normally start with Core, Product, the selected Feature, Architecture and Workflow, then consult Roadmap and Decisions only for the affected boundary.

## 5. Portable ownership model

Inside a copied package, the numbered owner documents are the complete local design context. Navigation and traceability files may summarize or link, but do not own Product, Architecture, Workflow or Feature facts.

External repository files named below are provenance, not runtime dependencies. A copied package must remain readable without them. If a newer human decision or accepted owner is supplied with an exact binding, it takes precedence only in its declared fact class.

## 6. Exact source provenance

| Subject | SHA-256 | Effect |
|---|---|---|
| accepted DRAFT-R2 candidate manifest | `57446e0d8075985af2229eae86cc6cf018b41ec255f0140b7bb20b45ef3ded65` | primary content source |
| independent DRAFT-R2 completeness re-audit | `b6cd639302fb719ab7ef47e894075c791d683c3e46b35291c11a2c591f989cfe` | technical `PASS`, no material findings |
| DRAFT-R2 human decision record | `0353347d106d1985e7b296f721ade4b9e51a1a26a304468b97dc39b00c7598df` | `DR-FULL-001: ACCEPT` for exact R2 fact classes |
| frozen Global Design ordered manifest | `b9ef04820f9e71da1866c61c87417c7ac39d1c27c93a74327ab7f40f2e25aebf` | accepted upstream foundation, unchanged |
| accepted X1 candidate manifest | `1f0d12c3328348126a5882f05e52a512157075e852993018ffb023cd979bf42d` | accepted FTR-001/FTR-003 package |
| accepted X1 decision record | `3e9fbbcde2d07a8716f0dc28eb33e642e1c42766da738e41c7137abf358af197` | Product Spec/Passport and first-slice options A/A |

The accepted canonical source identities carried by DRAFT-R2 are:

| Source role | SHA-256 |
|---|---|
| repository rules | `fd47fe24d77ba0864ffae9025e434588967741b9935dcd26d6e1efbe047bf458` |
| Core | `d5bd30ed1e819f348f2ae044ffe77cf14e72ddae1d8576c1a2f392e6f7e70e1b` |
| Product | `c119f8f301abcd93167e3f5b61272dfda7bb499fff58018e6163bb325308b2cb` |
| Architecture | `dade6df2d03c38a0833d6070b13cdb884214a6c164092d5fd3fc2b1cb2599921` |
| Development workflow | `3f880c14b9e00e9428032bc07b29cc18d46b7eed6ceac1084f6ef7745f684fab` |
| Lessons | `5bff781c83546ec5cfca2093ab1cde61fc17a662346a752762433e6fa2553b3d` |
| Reference routing | `e7d0dc9aef509853e0f750aa81286eb4a646e6f36c78fb235c9a0d318162287f` |
| Feature inventory | `f0ade2e1f76368cc909302dae7d87f1e4b7297a23c44566aee06c84a1f2f0ea0` |

## 7. Identity model

Each manifest record contains lowercase file SHA-256, exact byte count and package-relative path, sorted by UTF-8 path bytes. Candidate identity is SHA-256 of exact [MANIFEST.txt](MANIFEST.txt) bytes.

Any byte change to a bound file creates a new candidate identity. An audit or acceptance for an earlier identity does not transfer.

## 8. Exclusions

This package intentionally excludes source workspaces, audits, controllers, correction history, canonical-document copies, X1 working artifacts and runtime implementation material. It does not select the implementation repository, stack, interface, persistence, provider, release model or any still-open feature disposition.

## 9. Next gate

After construction checks and exact manifest binding, the next action is a separate independent read-only audit. Human package acceptance and any Git delivery remain later, separate actions.
