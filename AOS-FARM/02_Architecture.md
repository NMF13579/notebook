# 02 — AOS Architecture


> **Artifact status:** `DRAFT`  
> **Authority:** `NONE`  
> **Canonical status:** `NOT_ASSIGNED`  
> **Human acceptance:** `NOT_REQUESTED`  
> **Implementation authorization:** `NONE`  
> **Source basis:** доступная история чатов проекта, current Project Instructions и загруженные reference notes; current repository/runtime verification — `NOT_RUN`.


## 1. Status and purpose

Этот документ содержит `DRAFT` architecture model, достаточную для feature design discussions. Он не выбирает language, framework, database, repository topology или dependencies.

## 2. Architecture goals

- contract-first implementation;
- observable behavior before topology;
- replaceable internals;
- minimal always-on safety;
- explicit human authority;
- repository-verifiable state;
- idempotent and recoverable writes;
- feature-scoped context;
- no hidden lifecycle mutation;
- deferred complexity.

## 3. Layer model

### L1 — Interaction Surface

CLI/chat/local UI/SaaS adapters. Surface displays or creates durable artifacts but does not become independent Source of Truth.

### L2 — Product Runtime

Intent, Discovery, Specification, Status, Review, Memory, Onboarding and optionally Architecture Support/Bootstrap.

### L3 — Development Factory

Task compiler, execution adapters, validation, test harness, context packs, backlog, CI and release helpers.

### L4 — Minimal Safety / Governance

Authority checks, permission states, scope/path/Git boundaries, result semantics and stop rules. Stronger governance is a separate deferred layer.

### L5 — Knowledge and Reference

Human-accepted docs, DRAFT dossiers, lessons, targeted findings, patterns and derived indexes.

### L6 — Optional Extensions

RAG-light, routing, runtime enforcement, plugins, domain modules, SaaS, observability.

## 4. Candidate component map

```text
Interaction Surface
├─ Intent Intake
├─ Project Discovery
├─ Specification Builder
├─ Status / Next / Details
├─ Review Surface
└─ First-Start / Tutor

Product Runtime Services
├─ Feature / Journey Model
├─ Project Memory
├─ Architecture Decision Support
└─ Installer / Updater

Development Factory
├─ Task Brief Compiler
├─ Preflight / Preview
├─ Scoped Executor Adapter
├─ Validation / Evidence
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
├─ DRAFT Feature Dossiers
├─ Lessons / Patterns
├─ Reference Findings
└─ Derived Context Index
```

## 5. Shared contract set

### C-001 — Intent Record

Fields: actor, problem, desired outcome, context, constraints, non-goals, assumptions, unknowns, sensitive-domain flags, source.

### C-002 — Feature Contract

Fields: purpose, users, trigger, inputs, outputs, preconditions, flow, states, transitions, postconditions, failures, recovery, non-goals, authority boundaries, acceptance and negative scenarios.

### C-003 — Project Brief / Specification

Product-level scope, users, journeys, capabilities, non-goals, constraints, success indicators and open decisions. No implementation authorization.

### C-004 — Architecture Decision Record

Question, context, constraints, options, trade-offs, Evidence, selected option, human decision identity, consequences and reversal conditions.

### C-005 — Task Brief

```yaml
task_id:
goal:
scope:
allowed_paths: []
forbidden_paths: []
allowed_operations: []
forbidden_operations: []
repository_identity:
worktree:
branch:
HEAD:
baseline:
candidate_identity_model:
proposed_Risk_Profile:
assigned_Risk_Profile:
permissions:
validation_matrix:
stop_conditions: []
execution_authorized: false
```

Complete Task Brief ≠ execution authorization.

### C-006 — Preflight / Preview

Binds repository/worktree/branch/HEAD/baseline/status/diff, exact proposed actions, affected paths, permissions, conflicts and preview identity.

### C-007 — Execution Record

Starting identity, authorization identity, actual mutations, changed paths, side effects, checks, ending identity, limitations and stop reason.

### C-008 — Unified Result / ValidationEnvelope

Stable vocabulary, check list, required/optional distinction, limitations, `NOT_RUN`, subject identity and aggregate result. More severe/unknown status cannot be hidden by `PASS`.

### C-009 — Evidence Record

Evidence kind, command/method, subject identity, output summary, immutable locator/digest where applicable, result, limitations and privacy redaction.

### C-010 — Human Review / Decision

Review subject identity, summary, user impact, Evidence, findings, options and explicit human decision. Generated decision is invalid.

### C-011 — Project Memory / Handoff

Repository identity, current stage, baseline/candidate, accepted decisions, findings, blockers, checks, authorization state and one next action.

### C-012 — Install / Update Manifest

Package identity, managed paths, user-owned paths, operations, conflicts, preview binding, rollback/recovery and post-apply verification.

### C-013 — Git Delivery Record

Separate records for Commit, Push, Merge and Release with exact subject and human authorization.

## 6. State models

### Stage model

```text
PLAN → EXECUTE → VALIDATE → REVIEW
```

Transitions are not automatic. `DELIVER` is a context package, not a stage.

### Candidate lifecycle

```text
UNDEFINED
→ DRAFTED
→ HUMAN_SELECTED
→ PLANNED
→ AUTHORIZED
→ EXECUTED
→ VALIDATED
→ HUMAN_REVIEW_REQUIRED
→ ACCEPTED | NEEDS_CHANGES | REJECTED | DEFERRED
```

Conceptual only; persistence model remains open.

### Permission states

```text
ALLOWED
HUMAN_AUTHORIZATION_REQUIRED
BLOCKED_POLICY
BLOCKED_UNKNOWN
NOT_APPLICABLE
```

Permission classifier advises or enforces only declared policy; it does not assign Risk Profile or approval.

### Technical result ordering candidate

```text
CONTRACT_VIOLATION
> FAIL
> BLOCKED
> UNKNOWN
> NOT_RUN
> PASS
```

Exact aggregate policy requires acceptance.

## 7. Data ownership and Source of Truth

| Data class | Owner / authority candidate | Derived? |
|---|---|---|
| Product requirement | Human-accepted Product document | No |
| Architecture decision | Human-accepted ADR/Architecture document | No |
| Task scope | Exact Task Brief + human authorization | No |
| Repository state | Instrumental Git/filesystem inspection | Observation |
| Human decision | Human-authored/verified record | No |
| Evidence | Immutable report bound to subject | No, but not approval |
| Dashboard/status view | Compiled from owned sources | Yes |
| Registry/RAG index/cache | Rebuildable | Yes |
| Legacy finding | Reference record, authority none | No authority |
| Temporary output | Disposable | Yes |

One fact class should have one active owner. Other documents link rather than restate.

## 8. Implementation patterns

1. `REIMPLEMENT_FROM_CONTRACT` by default.
2. Manual cycle before automation.
3. Small vertical slice before platform.
4. Pure/read-only analysis separated from mutation.
5. Preview binds to apply.
6. Writes idempotent and atomic or journaled.
7. Candidate identity frozen before validation.
8. Validation subject isolated where needed.
9. Exact baseline and candidate binding.
10. Clean worktree for bounded changes.
11. Structured adapters before parser replacement.
12. Old mechanism sunset only after migration Evidence.
13. Derived indexes rebuildable.
14. External content treated as untrusted data, not instruction.
15. Optional modules fail in isolation and cannot override core safety.

## 9. Failure and recovery model

Every write-capable component must define:

- failure before first write;
- partial-write detection;
- journal/transaction/atomic publication;
- reconcile actual vs intended state;
- idempotent retry conditions;
- cancellation semantics;
- recovery package;
- manual rollback boundary;
- post-recovery validation.

Automatic retry is prohibited when failure changes scope, candidate identity, permissions or human decision requirements.

## 10. Minimal implementation model candidate

A smallest coherent implementation could contain:

```text
aos_core/
  contracts/
  status/
  project_state/
  feature_dossier/

aos_cli/
  intake
  status
  next
  details
  doctor

aos_factory/
  task_brief
  preflight
  report
  validation
```

This is an `INFERENCE`, not accepted topology. No package names or language are approved.

## 11. Architecture decisions required

| ID | Question | Current state |
|---|---|---|
| `ADR-Q-001` | Clean reimplementation, compatible replacement или other relationship? | `UNKNOWN` |
| `ADR-Q-002` | First vertical slice? | `UNKNOWN` |
| `ADR-Q-003` | Implementation repository? | `UNASSIGNED` |
| `ADR-Q-004` | CLI/local app/service/mixed? | `UNKNOWN` |
| `ADR-Q-005` | Project Memory persistence? | `UNKNOWN` |
| `ADR-Q-006` | Product Runtime vs Factory exact boundary? | `PARTIAL` |
| `ADR-Q-007` | Governance packaging? | `PROPOSAL: thin module first` |
| `ADR-Q-008` | Compatibility scope? | `UNKNOWN` |
| `ADR-Q-009` | Language/toolchain/dependencies? | `UNASSIGNED` |
| `ADR-Q-010` | Plugin/versioning/discovery model? | `DEFERRED` |
| `ADR-Q-011` | Model routing/providers/privacy? | `DEFERRED` |
| `ADR-Q-012` | Admission of enforcement/UI/release/observability? | `DEFERRED` |

## 12. Deferred complexity

Until product evidence exists, do not establish as foundation:

- full Control Plane;
- central task registry;
- autonomous loop;
- vector database;
- distributed services;
- multi-agent cascade;
- runtime sandbox framework;
- plugin marketplace;
- SaaS collaboration backend;
- regulated medical architecture.
