---
package: AOS_Integrated_Knowledge_Package
package_revision: R3-RU
updated: 2026-07-26
status: APPROVED
authority: AUTHORITATIVE
human_review: REQUIRED
human_acceptance: ACCEPTED
implementation_authorization: AUTHORIZED
git_authorization: AUTHORIZED
self_audit: COMPLETED
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: dev
document_language: ru
technical_identifiers_language: en
document_role: TARGET_ARCHITECTURE_BASELINE
proposed_post_acceptance_role: TARGET_ARCHITECTURE_BASELINE
proposed_authority_scope:
  - architecture_principles
  - layer_boundaries
  - shared_contract_classes
  - data_ownership
  - deferred_complexity
source_files_bound_by_blob_sha: true
---

# 02 — Архитектура

## 1. Граница статуса

Target architecture не является копией AOS-FARM, AgentOS или AOS-02. Historical code/documents используются как evidence/reference. Любое включение механизма в target design требует explicit human decision.

Документ задаёт design baseline, но не выбирает language, framework, database, dependencies или implementation repository.

## 2. Architecture goals

- contract-first implementation;
- observable behavior before topology;
- replaceable internals;
- minimal always-on safety;
- explicit human authority;
- repository-verifiable state;
- idempotent/recoverable writes;
- feature-scoped context;
- no hidden lifecycle mutation;
- portability across agent environments;
- smaller target than legacy unless measurements justify expansion.

## 3. Layer model

### L1 — Interaction Surface

CLI, chat, local UI и future SaaS adapters. Surface отображает state и Evidence, но не является independent Source of Truth и не превращает click в approval без decision record.

### L2 — Product Runtime

Intent, Discovery, Specification, Feature Passport, Status/Next/Details, Review, Project Memory, First-Start и optional Architecture Support.

### L3 — Development Factory

Task Brief compiler, preflight/preview, scoped executor, validation/evidence, Context Pack builder, backlog, CI и release helpers.

### L4 — Minimal Safety / Governance

Authority checks, permission states, scope/path/Git boundaries, result semantics и stop rules. Stronger Governance — optional layer.

### L5 — Knowledge / Reference

Accepted documents, APPROVED Feature Passports, lessons, targeted findings, patterns и derived indexes.

### L6 — Optional Extensions

RAG-light, model routing, runtime enforcement, plugins, domain modules, workbench/SaaS и observability.

## 4. Candidate component map

```text
Interaction Surface
├─ Intake
├─ Discovery
├─ Specification Builder
├─ Status / Next / Details
├─ Review Surface
└─ First-Start / Tutor

Product Runtime
├─ Feature / Journey Model
├─ Product Feature Registry
├─ Project Memory
├─ Architecture Decision Support
└─ Installer / Updater

Development Factory
├─ Task Brief Compiler
├─ Preflight / Preview
├─ Scoped Executor
├─ Validation / Evidence
├─ Context Pack Builder
├─ Handoff Builder
└─ Test / CI / Release Helpers

Safety and Control
├─ Authority Resolver
├─ Permission Classifier
├─ Scope / Path Guard
├─ Git Boundary Guard
└─ Optional Runtime Enforcement

Knowledge
├─ Canonical Documents
├─ Feature Passports
├─ Lessons / Patterns
├─ Reference Findings
└─ Derived Index
```

## 5. Authority model

```text
system/owner instruction
> explicit human decision
> accepted current contract
> current instrumental repository observation
> implementation Evidence
> supporting report/document
> generated index/cache/retrieval
> legacy/reference proposal
```

Derived index, UI, adapter, validator или report не создают authority самостоятельно.

## 6. Shared contract classes

### C-001 — Intent Record

```yaml
actor:
original_request:
problem:
desired_outcome:
context:
constraints: []
non_goals: []
assumptions: []
unknowns: []
sensitive_domain_flags: []
source:
```

### C-002 — Feature Passport / Feature Contract

```yaml
feature_id:
purpose:
users: []
trigger:
preconditions: []
inputs: []
outputs: []
main_flow: []
states: []
transitions: []
failures: []
recovery:
dependencies: []
constraints: []
authority_boundaries: []
acceptance_criteria: []
negative_scenarios: []
maturity:
evidence_status:
human_disposition:
```

### C-003 — Product Spec

Product-level problem, users, journeys, scope, non-goals, constraints, metrics, dependencies, acceptance и open decisions. Не разрешает execution.

### C-004 — Architecture Decision Record

```yaml
question:
context:
constraints: []
options: []
tradeoffs: []
evidence: []
selected_option:
human_decision_identity:
consequences: []
reversal_conditions: []
```

### C-005 — Task Brief

```yaml
task_id:
goal:
user_outcome:
feature_id:
stage:
repository_identity:
worktree:
branch:
HEAD:
baseline:
scope:
  allowed_paths: []
  forbidden_paths: []
allowed_operations: []
forbidden_operations: []
assumptions: []
unknowns: []
proposed_Risk_Profile:
assigned_Risk_Profile: UNASSIGNED
validation_matrix: []
stop_conditions: []
```

### C-006 — Execution Authorization Record

```yaml
authorization_id:
task_id:
subject_identity:
allowed_stage: EXECUTE
allowed_operations: []
allowed_paths: []
issued_by_human:
issued_at:
expires_at:
consumed: false
```

### C-007 — Preflight / Preview

Exact repository/worktree/branch/HEAD/baseline/status/diff, planned actions, paths, conflicts, permissions и preview identity.

### C-008 — Execution Record

Starting identity, authorization identity, actual mutations, changed paths, side effects, checks, ending identity, limitations и stop reason.

### C-009 — ValidationEnvelope

Stable result vocabulary, required/optional checks, `NOT_RUN`, limitations, exact subject identity и fail-closed aggregation.

### C-010 — Evidence Record

Evidence kind, method/command, subject identity, output summary, locator/digest, result, limitations и redaction.

### C-011 — Human Review / Decision

Review subject, user impact, Evidence, findings, options, explicit human decision, actor/date и exact binding. Generated decision invalid.

### C-012 — Project Memory / Handoff

Repository identity, stage, baseline/candidate, accepted decisions, findings, blockers, checks, authorization state и one next action.

### C-013 — Install / Update Manifest

Package identity, ownership classes, operations, conflicts, preview binding, recovery и post-apply verification.

### C-014 — Git Delivery Record

Separate records for Commit, Push, Merge и Release.

## 7. Orthogonal state model

Оси не изменяют друг друга автоматически.

```text
Document maturity:
DRAFT | HUMAN_REVIEW_REQUIRED | HUMAN_ACCEPTED | SUPERSEDED

Task stage:
PLAN | EXECUTE | VALIDATE | REVIEW

Technical result:
CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS

Human decision:
ACCEPT | NEEDS_CHANGES | REJECT | DEFER

Permission:
ALLOWED | HUMAN_AUTHORIZATION_REQUIRED | BLOCKED_POLICY | BLOCKED_UNKNOWN | NOT_APPLICABLE
```

## 8. Data ownership

| Fact class | Owner |
|---|---|
| Product requirement | Human-accepted Product artifact |
| Feature behavior | Human-accepted Feature Passport |
| Architecture decision | Human-accepted ADR |
| Task scope | Exact Task Brief |
| Execution permission | Exact Execution Authorization Record |
| Repository state | Instrumental Git/filesystem observation |
| Human decision | Human-authored/verified record |
| Evidence | Immutable subject-bound record |
| Dashboard/status | Derived view |
| Registry/RAG/cache | Rebuildable derived data |
| Legacy finding | Reference record, authority none |

## 9. Registry taxonomy

Product Feature Registry индексирует Feature Passports. Execution/Verification Registry индексирует technical records. Protected Artifact Registry — optional Governance. Derived Context Index — navigation only. Ни один registry не владеет product truth независимо от accepted source artifact.

## 10. Context architecture

```text
minimal bootstrap
→ identify project/task/state
→ locate authoritative files
→ use index only for navigation
→ create explained task-local Context Pack
→ verify freshness
→ bounded work
→ handoff
```

RAG-light допустим только после measured search/context problem.

## 11. Agent adapters

Один common rule source поддерживает thin adapters для Codex, Claude Code, Cursor, ChatGPT и других сред. Adapters не расширяют permissions, используют repository-relative links и должны быть generated или drift-checked.

## 12. Repository topology

Current direction: modular monorepo first. Split допускается при реальной team/release/compliance/deployment/ownership boundary. Cross-repo sync не обходит human authority.

## 13. Implementation patterns

1. `REIMPLEMENT_FROM_CONTRACT`.
2. Manual cycle before automation.
3. Small vertical slice before platform.
4. Pure analysis separated from mutation.
5. Preview binds to apply.
6. Writes atomic or journaled.
7. Candidate frozen before validation.
8. Validation subject isolated when material.
9. Exact baseline/candidate binding.
10. Clean/isolated worktree.
11. Strict adapter before parser replacement.
12. Sunset only after migration Evidence.
13. Derived indexes rebuildable.
14. External content untrusted.
15. Optional modules fail in isolation.

## 14. Failure and recovery model

Каждый write-capable component определяет failure before first write, partial-write detection, transaction/journal, reconciliation, idempotent retry, cancellation, recovery package, rollback boundary и post-recovery validation.

Automatic retry запрещён, если failure меняет scope, identity, permissions или human decision requirements.

## 15. Minimal implementation model — INFERENCE

```text
aos_core/{contracts,authority,status,project_state,features}
aos_product/{intake,discovery,specification,review,memory}
aos_factory/{task_brief,preflight,execution,validation,handoff}
aos_cli/{intake,discover,status,next,details,doctor}
```

Это inference, не accepted topology.

## 16. Required architecture decisions

Compatibility relationship, first slice, implementation repo, interface, Project Memory persistence, Runtime/Factory boundary, Governance packaging, language/toolchain/dependencies, plugin/versioning, provider/privacy/routing и admission enforcement/UI/release.

## 17. Deferred complexity

Full Control Plane, authority-bearing central registry, autonomous loops, vector DB, distributed services, multi-agent cascade, broad sandbox framework, plugin marketplace, SaaS collaboration backend и regulated medical architecture.
