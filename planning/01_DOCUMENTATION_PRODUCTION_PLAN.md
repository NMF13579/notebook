---
document_type: AOS_DOCUMENTATION_PRODUCTION_PLAN
revision: R3-CORRECTION-CANDIDATE
status: HUMAN_REVIEW_REQUIRED
authority: NONE_UNTIL_HUMAN_ACCEPTANCE
authority_scope: DOCUMENTATION_CORRECTION_AND_IMPLEMENTATION_HANDOFF_SEQUENCE
supersedes_candidate: planning/01_DOCUMENTATION_PRODUCTION_PLAN.md@DRAFT-R2
source_repository: NMF13579/notebook
source_branch: agent/aos-3-documentation-package
source_commit: 9fa079964ea86b33425337ba1706bd3da5bea7b8
technical_result: PASS
readiness: READY_FOR_INDEPENDENT_REVIEW
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
created: 2026-08-06
---

# AOS-3 — Documentation Production Plan R3

## 1. Вывод

План больше не описывает уже завершённые `DOC-001…DOC-013` как будущие действия. Он разделяет:

1. correction текущей navigation/authority topology;
2. первый implementation subject `Task-001-Scaffolding`;
3. отдельный Product Runtime subject `Task-002-Intake-to-Reviewable-Intent`.

`Task-002` не расширяет `Task-001` и не становится executable до завершения scaffold, fresh target baseline и отдельной authorization.

## 2. Authoritative basis

| Fact class | Owner |
|---|---|
| Project identity, source precedence, safety | `docs/00_Core.md` после exact acceptance correction revision |
| H1 implementation decisions | `AOS_IMPLEMENTATION_DECISIONS_R1.md` + exact acceptance records |
| Feature inventory and item dispositions | `docs/06_Features.md`, синхронизированный с H1 owner |
| Current documentation lifecycle | `planning/CURRENT.md` |
| Scaffold behavior | `AOS_SCAFFOLDING_CONTRACT_R1.md` |
| First implementation task | `Task-001-Scaffolding.md` + `DSP-001.md` |
| Core schemas/authority | `AOS_CORE_CONTRACT_R1.md` |
| Project Memory v2 | `AOS_CORE_CONTRACT_C012_V2_R1.md` |
| Project Memory and read-only UX | `AOS_CORE_CONTRACT_C3_C4_R1.md` |
| First Product Runtime behavior | `AOS_FEATURE_CONTRACT_INTAKE_TO_REVIEWABLE_INTENT_R1.md` |
| Product Runtime implementation scope | `Task-002-Intake-to-Reviewable-Intent.md` + `DSP-009.md` |
| Developer navigation | `DEVELOPER_HANDOFF_R2.md` |

Derived plans, manifests and handoffs do not override these owners.

## 3. Corrected current facts

```yaml
project: AOS-3
knowledge_repository: NMF13579/notebook
implementation_repository:
  accepted_target: NMF13579/aos-3
  physical_creation: NOT_RUN
  observed_baseline: NOT_RUN
first_actor: NONPROGRAMMER_DOMAIN_EXPERT_GREENFIELD
first_product_runtime_slice: INTAKE_TO_REVIEWABLE_INTENT_R1
required_first_cycle_features:
  - FTR-001
  - FTR-008
  - FTR-011
  - FTR-016
  - FTR-019
FTR-003: UNDECIDED
nearest_implementation_task: Task-001-Scaffolding
Product_Runtime_task: Task-002-Intake-to-Reviewable-Intent
implementation_authorization: NONE
Git_authorization: NONE
```

Repository target decision ≠ repository creation ≠ observed baseline.

## 4. Correction scope

### In scope

- route `00_Core → CURRENT → handoff → Task/DSP → owner`;
- correction `implementation_repository: UNASSIGNED` into separate decision/creation axes;
- exact H1 dispositions in `06_Features.md`;
- removal of `FTR-003` from first-cycle selection;
- replacement of stale R2 next-actions/statuses;
- feature-specific `C-002` for `INTAKE_TO_REVIEWABLE_INTENT_R1`;
- exact Product Runtime Task/DSP candidate;
- frozen hashes, link check, status/authority check and independent-agent simulation;
- one handoff that exposes sequencing and all blockers.

### Out of scope

- repository creation or configuration;
- root `AGENTS.md` activation;
- runtime/scaffold implementation;
- execution authorization;
- `Commit`, `Push`, `Merge`, `Release`;
- Product Spec, full Feature Passport, Development Factory, RAG, provider routing, SaaS or plugins.

## 5. Implementation sequence

### I0 — Scaffolding

Current exact subject:

```yaml
task: Task-001-Scaffolding.md
DSP: DSP-001.md
contract: AOS_SCAFFOLDING_CONTRACT_R1.md
user_outcome: REPRODUCIBLE_SAFE_DEVELOPMENT_BASE_WITHOUT_PRODUCT_BEHAVIOR
```

Entry gates:

1. correction package exact human acceptance;
2. target repository creation/assignment through separate action;
3. root `README.md` preservation and root `AGENTS.md` activation through separate subject;
4. fresh read-only preflight and frozen preview;
5. human-assigned `Risk_Profile`;
6. one-shot exact Execution Authorization.

Exit gate:

- all `SCF-001…SCF-026` required checks terminal;
- intended/actual diff reconciled;
- Product Runtime still honestly `NOT_IMPLEMENTED`;
- Stage Report emitted and agent stops;
- human review/acceptance remains separate.

### X1 — Intake to reviewable intent

Candidate exact subject:

```yaml
feature_contract: AOS_FEATURE_CONTRACT_INTAKE_TO_REVIEWABLE_INTENT_R1.md
task: Task-002-Intake-to-Reviewable-Intent.md
DSP: DSP-009.md
user_outcome: REVIEWABLE_INTENT_WITH_VISIBLE_UNKNOWNS_AND_ONE_NEXT_ACTION
```

Additional entry gates:

1. I0 implementation accepted;
2. Task-002 baseline rebound to observed post-I0 `HEAD`/worktree;
3. exact feature contract/Task/DSP accepted;
4. fresh preview and separate Execution Authorization.

X1 stop boundary:

```text
free-form request
→ deterministic reviewable Intent candidate
→ explicit confirmation
→ immutable Intent Record
→ atomic Project Memory
→ status/next/details
→ stop before Product Spec, Task Brief for user project or execution
```

## 6. Documentation quality gates

| Gate | Required oracle |
|---|---|
| Q1 Authority | one owner per fact class; acceptance records exact; no generated authority |
| Q2 Status | `PASS ≠ approval`; `NOT_RUN/UNKNOWN/BLOCKED` never hidden |
| Q3 Product | actor, trigger, I/O, states, failure/recovery, non-goals exact |
| Q4 Determinacy | coding agent makes no product/architecture/schema choice |
| Q5 Scope | allowed/forbidden paths and operations machine-checkable |
| Q6 Tests | every mandatory criterion has positive/negative executable oracle |
| Q7 Recovery | pre-write, partial-write, stale-preview and resume boundaries explicit |
| Q8 Handoff | 12/12 independent-agent questions answerable without chat |

Any required non-PASS blocks documentation `PASS`.

## 7. Independent-agent simulation questions

The reviewer must answer:

1. What exact user outcome is current?
2. Which task is executable first?
3. Which repository facts are accepted decisions and which are unobserved?
4. Which files own behavior, lifecycle and navigation?
5. What paths/operations are allowed and forbidden?
6. What must be observed for success?
7. Which negative cases are mandatory?
8. How is partial write detected and recovered?
9. Which checks are required versus optional?
10. Where must the agent stop?
11. What requires human decision?
12. Which Git actions remain unauthorized?

Any ambiguous answer is a named finding.

## 8. Definition of documentation-ready

```yaml
documentation_ready:
  corrected_canonical_route: REQUIRED_PASS
  repository_axes_separated: REQUIRED_PASS
  feature_dispositions_match_H1: REQUIRED_PASS
  stale_plan_state_removed: REQUIRED_PASS
  Task-001_scope_preserved: REQUIRED_PASS
  Product_Runtime_C002_exact: REQUIRED_PASS
  Task-002_scope_exact: REQUIRED_PASS
  acceptance_and_negative_tests_executable: REQUIRED_PASS
  recovery_and_stop_rules: REQUIRED_PASS
  hashes_and_links: REQUIRED_PASS
  independent_agent_simulation: REQUIRED_PASS
  package_frozen: REQUIRED_PASS
  human_acceptance: NOT_RUN
  implementation_authorization: NONE
  Git_authorization: NONE
```

## 9. Human checkpoints

| Checkpoint | Exact decision |
|---|---|
| H-CORR | accept/changes/reject/defer exact correction package |
| H-I0 | repository/preflight/Risk/Execution Authorization for Task-001 |
| H-I0-RESULT | accept/changes/reject/defer scaffold candidate |
| H-X1 | accept/rebind/authorize exact Task-002 after post-I0 observation |
| H-X1-RESULT | accept/changes/reject/defer Product Runtime candidate |

No checkpoint implies another.

## 10. Terminal status

```yaml
plan_revision: R3-CORRECTION-CANDIDATE
  technical_result: PASS
  readiness: READY_FOR_INDEPENDENT_REVIEW
human_acceptance: NOT_RUN
implementation_repository_creation: NOT_RUN
runtime_implementation: NOT_RUN
execution_authorization: NONE
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: RUN_INDEPENDENT_READ_ONLY_VALIDATION
stop: true
```
