---
artifact_id: AOS3-DPKG-DOC-003
artifact_type: ARCHITECTURE_AND_DECISIONS
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R4
status: DRAFT_SOURCE_WITH_HUMAN_ARCHITECTURE_AND_C1_ACCEPTED_SUBJECTS
authority: MIXED_HUMAN_DECISIONS_AND_PROPOSAL
exact_subject: Accepted AOS Core v1 architecture boundaries, logical components, interfaces, data ownership, ADR registry, and unresolved physical decisions
created: '2026-07-30'
human_acceptance: DEC_ARCH_DECISIONS_AND_C1_EXACT_SUBJECTS
provenance:
  - path: ../../docs/00_Core.md
    use: authority, source precedence, safety, and human-only decisions
  - path: ../../docs/02_Architecture.md
    use: accepted layers, contract classes, ownership, and implementation patterns
  - path: ../../docs/03_Development.md
    use: stage, validation, recovery, and Git boundaries
  - path: decisions/G2_ARCHITECTURE_OPTION_PACKAGE.md
    use: hash-bound G2 options
  - path: decisions/DEC-ARCH-001_Implementation_Repository.md
    use: documentation-only notebook boundary and deferred implementation-repository identity
  - path: decisions/DEC-ARCH-002_Architecture_and_Topology.md
    use: accepted local modular-monolith and adapter architecture
  - path: decisions/DEC-ARCH-003_Toolchain_and_Dependencies.md
    use: accepted Python toolchain class
  - path: decisions/DEC-ARCH-004_Project_Memory.md
    use: accepted file-based Project Memory
  - path: decisions/DEC-ARCH-005_Provider_and_Privacy.md
    use: accepted local-only privacy boundary
  - path: decisions/DEC-ARCH-006_Human_Decision_Authenticity.md
    use: accepted local-declared hash-bound decisions
  - path: decisions/DEC-ARCH-007_Risk_Profile_Vocabulary.md
    use: accepted minimal human-owned action classes
  - path: decisions/DEC-ARCH-008_Compatibility.md
    use: accepted greenfield compatibility boundary
upstream_links:
  - 00_Control_and_Source_Precedence.md
  - 01_Product_and_Core_V1_Scope.md
  - 02_User_Journeys_and_Workflows.md
  - decisions/DEC-ARCH-001_Implementation_Repository.md
  - decisions/DEC-ARCH-002_Architecture_and_Topology.md
  - decisions/DEC-ARCH-003_Toolchain_and_Dependencies.md
  - decisions/DEC-ARCH-004_Project_Memory.md
  - decisions/DEC-ARCH-005_Provider_and_Privacy.md
  - decisions/DEC-ARCH-006_Human_Decision_Authenticity.md
  - decisions/DEC-ARCH-007_Risk_Profile_Vocabulary.md
  - decisions/DEC-ARCH-008_Compatibility.md
downstream_links:
  - 04_Runtime_and_Data_Contracts.md
  - 05_Quality_Recovery_and_Security.md
  - 06_Traceability_and_Readiness.md
  - 07_Implementation_Handoff.md
  - adapters/CODEX.md
limitations:
  - Logical architecture is accepted; repository creation is not authorized and implementation_repository remains UNASSIGNED.
  - Exact dependencies and operating-system support are not selected or verified.
  - No runtime, schema implementation, CLI, package, database, service, or deployment exists.
  - BLK-006 records an unresolved canonical status-axis conflict; this package cannot accept a canonical TechnicalResult vocabulary.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# 03 — Architecture and Decisions

## 1. Status and authority boundary

This document translates hash-bound G2 decisions into architecture contracts. Facts cited from `DEC-ARCH-001..008` have `HUMAN_DECISION` authority; `DEC-CONTRACT-001` separately owns acceptance of the exact C1 requirement definitions. Physical layout remains blocked while the implementation repository is `UNASSIGNED`.

```yaml
stage_b_candidate_sha256: d8170b28019310126932fa80b6bae411a36215def03bb53011561364f604917d
selected_bundle: G2-OPT-A
accepted_architecture_decisions:
  - DEC-ARCH-002
  - DEC-ARCH-003
  - DEC-ARCH-004
  - DEC-ARCH-005
  - DEC-ARCH-006
  - DEC-ARCH-007
  - DEC-ARCH-008
repository_decision:
  id: DEC-ARCH-001
  documentation_repository: NMF13579/notebook
  repository_creation: DO_NOT_CREATE
  exact_repository: UNASSIGNED
  future_binding: REQUIRES_SEPARATE_HUMAN_DECISION
contract_acceptance: HUMAN_ACCEPTED_EXACT_SUBJECTS_VIA_DEC_CONTRACT_001
runtime_verification: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

## 2. Accepted architecture constraints

| Decision | Accepted boundary | Does not decide |
|---|---|---|
| `DEC-ARCH-001` | Documentation is formed only in `NMF13579/notebook`; no implementation repository is created now | Future implementation owner/name, branch, remote, or repository existence |
| `DEC-ARCH-002` | Local modular monolith with ports/adapters; conversational adapter plus portable text/JSON and CLI | Physical directories or UI framework |
| `DEC-ARCH-003` | Python 3.12+, local package/CLI, minimal pinned dependencies | Exact dependencies, package manager, OS matrix |
| `DEC-ARCH-004` | Repository-relative Markdown/YAML/JSON Project Memory; versioned owners; rebuildable indexes | Exact storage paths |
| `DEC-ARCH-005` | Local-only Core; no provider transmission by default; external content untrusted | Provider adapter or consent policy |
| `DEC-ARCH-006` | `LOCAL_DECLARED_HASH_BOUND` Human Decisions | Cryptographic authentication |
| `DEC-ARCH-007` | Human-owned minimal action classes | Automatic Risk assignment or execution permission |
| `DEC-ARCH-008` | Greenfield contracts and portable interchange | Legacy runtime/CLI compatibility |

## 3. Logical architecture

```text
Conversational / CLI / text-json adapters
                    │
                    ▼
Application services and stage coordinators
  intake │ specification │ review │ status │ task compile │ resume
                    │
                    ▼
Domain contracts and policies
  claims │ authority │ identity │ workflow │ validation │ recovery
                    │
                    ▼
Ports
  artifact store │ clock │ digest │ repository observer │ provider
                    │
                    ▼
Local adapters
  Markdown/YAML/JSON │ filesystem │ Git read-only │ optional provider
```

The arrows are dependency direction, not automatic lifecycle transitions.

### 3.1 Logical components

| Component ID | Responsibility | Inputs/outputs | Must not own |
|---|---|---|---|
| `CMP-001` — Intake | Preserve/classify intent and material gaps | `IntentRecord` | Product approval or architecture |
| `CMP-002` — Specification | Compile Product Spec and Feature Passport candidates | source claims → DRAFT artifacts | Human acceptance |
| `CMP-003` — Review | Bind exact candidate and prepare one decision request | candidate/Evidence → review package | Decision value |
| `CMP-004` — Authority | Validate decision, permission, Risk, and Git boundaries | proposed action + records → classification | Human identity or automatic permission |
| `CMP-005` — Task Compiler | Derive one Task candidate from accepted IDs | accepted graph → Task candidate | Execution authorization or queue authority |
| `CMP-006` — Validation | Run/read checks against frozen subject | candidate + check plan → result/Evidence | Correction or acceptance |
| `CMP-007` — Project Memory | Persist source-owned durable state and derive resume view | exact records → handoff/status | Independent truth or hidden mutation |
| `CMP-008` — Recovery | Reconcile partial/unknown outcomes and options | journal/actual state → recovery package | Automatic retry after material failure |
| `CMP-009` — Adapter Boundary | Convert environment I/O to/from portable contracts | chat/CLI/text/JSON | Lifecycle, authority, or product truth |

These IDs describe logical responsibilities. They are not physical modules or implementation completion claims.

### 3.2 Slice A dependency path

```text
adapter input
→ CMP-001 preserve/classify
→ CMP-002 compile DRAFT artifacts
→ CMP-003 freeze review candidate
→ human review request
→ stop
```

`CMP-005..008` are supporting/future Core v1 contracts and cannot widen the first Slice A runtime.

## 4. Port boundaries

| Port ID | Operation class | Contract | Side-effect rule |
|---|---|---|---|
| `PORT-001` — Artifact Reader | read | Read exact relative artifact and digest | Zero writes |
| `PORT-002` — Artifact Publisher | write | Publish versioned artifact set atomically or journaled | Requires scoped documentation/runtime authority |
| `PORT-003` — Digest | pure | SHA-256 of canonical bytes/manifest | Deterministic |
| `PORT-004` — Clock | read | UTC timestamp with declared source | Does not prove trusted time |
| `PORT-005` — Repository Observer | read | Root/worktree/branch/HEAD/status/path facts | Zero source writes; secrets redacted |
| `PORT-006` — Decision Witness | read/append | Validate exact local-declared human record | Cannot manufacture a decision |
| `PORT-007` — Provider | external | Optional explicit opt-in exchange | Absent/disabled in Core v1 default |
| `PORT-008` — Renderer | pure/read | Human and machine views from source records | Derived view has authority `NONE` |

All port definitions are DRAFT contract content. No library or protocol is selected by these names.

## 5. Dependency direction and isolation rules

1. Domain contracts import no Codex, UI, database, provider, or Git implementation.
2. Application services depend on domain ports, not local adapters.
3. Adapters depend inward and cannot mutate domain state outside an explicit application operation.
4. Read-only operations use reader/observer ports only.
5. Project Memory owners are versioned files; indexes/status views are rebuildable.
6. Provider capability is absent by default and must fail closed without reducing local behavior.
7. Validation uses the same contract definitions as runtime but cannot call mutation ports.
8. A write operation has one idempotency key, one bounded subject, and one publication/journal boundary.
9. Physical repository topology cannot be inferred from this knowledge repository.
10. Optional modules cannot become dependencies of `CMP-001..004`.

## 6. Data ownership

| Fact class | Single owner | Derived consumers |
|---|---|---|
| Original intent and clarifications | `IntentRecord` | Product Spec compiler, review |
| Product boundary | Human-accepted Product Spec | Feature Passports, Task compiler |
| Feature behavior | Human-accepted Feature Passport | Task compiler, validator |
| Architecture | `DEC-ARCH-*`/ADR exact decision record | Contracts, handoff |
| Task scope | Exact Task Brief | Preflight, executor, validation |
| Execution permission | Exact Human Execution Authorization | Authority resolver, executor |
| Repository state | Fresh repository observation | Preflight, resume, review |
| Candidate identity | Candidate manifest | Validation, review, decision |
| Evidence | Subject-bound Evidence record | Review |
| Human decision | Human-originated decision record | State/status projections |
| Current continuity | Project Memory owners | Status/Next/Details, adapters |
| Queue/index/status | Rebuildable projection | Interaction surfaces |

An adapter, UI, queue, cache, generated index, validation result, or Evidence record never becomes the owner of a different fact class.

## 7. State separation

The following axes are stored and validated independently:

```text
DocumentMaturity:
  DRAFT | HUMAN_REVIEW_REQUIRED | HUMAN_ACCEPTED | STALE | SUPERSEDED

TechnicalResult (local DRAFT projection; canonical conformance blocked by BLK-006):
  CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS

HumanDisposition:
  ACCEPT | NEEDS_CHANGES | REJECT | DEFER | NOT_RUN

Permission:
  ALLOWED | HUMAN_AUTHORIZATION_REQUIRED | BLOCKED_POLICY
  | BLOCKED_UNKNOWN | NOT_APPLICABLE

RiskActionClass:
  UNASSIGNED | READ_ONLY | REVERSIBLE_WRITE
  | PROTECTED_WRITE | DESTRUCTIVE_OR_PUBLISHING

Freshness:
  CURRENT_FOR_BINDING | STALE | UNKNOWN
```

No value on one axis changes another automatically.

`docs/00_Core.md` currently includes `HUMAN_REVIEW_REQUIRED` in `Technical result`, while `docs/03_Development.md` and this package treat it as a document/control maturity state. The package preserves its local `DocumentMaturity` placement only as a DRAFT projection and does not claim to resolve the canonical owner conflict. Until a separately authorized human decision changes the canonical schema, any dependent TechnicalResult/ResultEnvelope conformance or readiness claim is blocked by `BLK-006_CANONICAL_STATUS_AXIS_CONFLICT`.

## 8. Decision and ADR registry

| Decision/ADR | Status | Consequence |
|---|---|---|
| [`DEC-ARCH-001 / ADR-001`](decisions/DEC-ARCH-001_Implementation_Repository.md) | `HUMAN_DECIDED_IMPLEMENTATION_REPOSITORY_DEFERRED` | Documentation stays in notebook; no repo creation; physical work remains deferred |
| [`DEC-ARCH-002 / ADR-002`](decisions/DEC-ARCH-002_Architecture_and_Topology.md) | `HUMAN_DECIDED` | Local modular monolith; ports/adapters; portable interfaces |
| [`DEC-ARCH-003 / ADR-003`](decisions/DEC-ARCH-003_Toolchain_and_Dependencies.md) | `HUMAN_DECIDED` | Python 3.12+; minimal pinned dependencies |
| [`DEC-ARCH-004 / ADR-004`](decisions/DEC-ARCH-004_Project_Memory.md) | `HUMAN_DECIDED` | Repository-relative files; rebuildable views |
| [`DEC-ARCH-005 / ADR-005`](decisions/DEC-ARCH-005_Provider_and_Privacy.md) | `HUMAN_DECIDED` | Local-only Core |
| [`DEC-ARCH-006 / ADR-006`](decisions/DEC-ARCH-006_Human_Decision_Authenticity.md) | `HUMAN_DECIDED` | Local-declared hash-bound decisions |
| [`DEC-ARCH-007 / ADR-007`](decisions/DEC-ARCH-007_Risk_Profile_Vocabulary.md) | `HUMAN_DECIDED` | Minimal human-owned action classes |
| [`DEC-ARCH-008 / ADR-008`](decisions/DEC-ARCH-008_Compatibility.md) | `HUMAN_DECIDED` | Greenfield compatibility only |

## 9. DRAFT architecture requirements

| Requirement ID | Requirement | Evidence expected before acceptance |
|---|---|---|
| `REQ-ARCH-001` | Portable domain contracts have no agent-environment dependency | Dependency/import review |
| `REQ-ARCH-002` | Every mutation is exposed only through an explicit application operation and write port | Architecture test and call-graph review |
| `REQ-ARCH-003` | Read-only paths cannot reach mutation ports | Negative architecture test |
| `REQ-ARCH-004` | One fact class has one owner; projections carry source/freshness | Ownership matrix and drift fixture |
| `REQ-ARCH-005` | Project Memory uses relative versioned files and rebuildable indexes | Round-trip and stale-index tests |
| `REQ-ARCH-006` | Local-only Core performs no hidden provider/network action | Network-deny integration test |
| `REQ-ARCH-007` | Human Decision validity is exact-subject, local-declared, and non-authorizing outside grants | Generated/stale/wrong-subject fixtures |
| `REQ-ARCH-008` | Risk classification is human-owned and separate from authorization | Self-assignment negative test |
| `REQ-ARCH-009` | Greenfield contracts do not silently accept legacy formats | Unknown-format rejection |
| `REQ-ARCH-010` | Physical topology and execution remain blocked while implementation_repository is `UNASSIGNED`; portable Task documentation may exist after contract acceptance | Notebook-as-implementation negative fixture plus portable-unbound Task fixture |

All `REQ-ARCH-*` entries are `DRAFT`; this document does not accept them.

## 10. Unknowns and local blocking

| Unknown/blocker | Blocks | Does not block |
|---|---|---|
| Exact implementation repository | Physical paths, repository preflight, dependency verification, repository-bound Task enrichment, implementation/execution | Portable schemas, logical contracts, quality scenarios, and accepted portable Task documentation |
| Exact dependency set | Scaffold implementation and reproducible environment checks | Language-independent contract semantics |
| OS support matrix | Cross-platform acceptance | Local behavior contract |
| Contract acceptance | Task template/graph/briefs and implementation planning | DRAFT review package |
| Stabilization thresholds | Claim that Core is stable | Definition of comparable cycle Evidence |
| `BLK-006_CANONICAL_STATUS_AXIS_CONFLICT` | Canonical TechnicalResult schema conformance, ResultEnvelope schema acceptance, and readiness claims that depend on the disputed axis | DRAFT package correction, raw status preservation, read-only conflict validation, and unrelated contract structure |

## 11. Architecture acceptance proposal

An exact revision of this document is acceptable only when:

1. every accepted statement traces to a `DEC-ARCH-*` record;
2. every remaining choice is marked DRAFT, `UNKNOWN`, or blocked;
3. adapter replacement does not alter portable core contracts;
4. local-only behavior has no hidden provider dependency;
5. one source owner exists for every fact class;
6. read-only, validation, decision, implementation, and Git boundaries are orthogonal;
7. physical repository claims remain absent until a future exact repository-binding decision supersedes the current deferred state;
8. executable negative scenarios exist in document `05`;
9. the package reports `BLK-006` without silently repairing canonical `/docs` or treating its local projection as accepted.

## 12. One next action

```yaml
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
