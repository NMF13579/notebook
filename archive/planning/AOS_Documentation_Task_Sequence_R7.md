---
artifact_id: AOS-DOCUMENTATION-TASK-SEQUENCE-R7
document_type: DOCUMENTATION_TASK_SEQUENCE
revision: R7
status: DRAFT
fact_class: PROPOSAL
revision_of: AOS-DOCUMENTATION-TASK-SEQUENCE-R6
source_revision:
  artifact_id: AOS-DOCUMENTATION-TASK-SEQUENCE-R6
  path: planning/AOS_Documentation_Task_Sequence_R6.md
  sha256: b6ab96bac6cc94add26d85a00c9dc781a49ee5465bc70356e4fea42190c34b89
  human_acceptance: ACCEPTED
supersedes_if_human_accepted:
  - AOS-DOCUMENTATION-TASK-SEQUENCE-R6
scope:
  - DOCUMENTATION_INTERVAL_ORDER
  - LARGE_AUTONOMOUS_DOCUMENTATION_INTERVALS
  - DOCUMENTATION_TO_TASK_CONVERSION_RULES
  - EXTERNAL_EVIDENCE_GATE_DEFINITIONS
excluded_from_scope:
  - IMPLEMENTATION_EXECUTION
  - OBSERVED_EVIDENCE_PRODUCTION
  - REPOSITORY_MUTATION_OUTSIDE_AUTHORIZED_DOCUMENTATION_INTERVAL
  - GIT_DELIVERY
target_use: CREATE_CLEAR_SEQUENTIAL_DOCUMENTATION_FOR_LATER_AGENT_IMPLEMENTATION
implementation_repository: UNASSIGNED
implementation_status: NOT_STARTED
external_evidence_status: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
human_review_required: true
human_acceptance: NOT_RUN
initial_interval_if_human_accepted: INT-DOC-001
active_interval: null
active_task: null
post_stop_validation_model:
  required_after_terminal_documentation_report: true
  canonical_stage: VALIDATE
  validation_profile: POST_STOP_DOCUMENTATION
  initial_trigger_mode: MANUAL_NEW_RUN
  automatic_dispatch_admission: NOT_RUN
  durable_report_persistence: SEPARATE_AUTHORIZED_EXECUTE_STAGE
  observed_validation_reports: NOT_RUN
planned_verification_state_owner_if_human_accepted:
  path: planning/CURRENT.md
  status: NOT_CREATED_OR_NOT_ACTIVATED
---

# AOS — Последовательность создания документации крупными автономными интервалами R7

## 1. Вывод

`R7` сохраняет authority, safety, validation и external-Evidence boundaries принятого `R6`, но заменяет множество коротких documentation tasks на крупные outcome-oriented интервалы.

```text
INT-DOC-001  Documentation Control Foundation
→ INT-DOC-100  Product Runtime Foundation
→ INT-DOC-200  First-Slice Human Decision Package
→ INT-DOC-210  Exact First-Slice Contract and Handoff Package
→ X1  separately authorized first-slice implementation and Evidence

→ INT-DOC-300  Manual-Ready Development Route
→ X2  observed manual dogfood Evidence

→ INT-DOC-400  one bounded runner package
→ X3  package implementation / validation / full-route regression
→ repeat INT-DOC-400 only for one explicitly selected next package

→ INT-DOC-500  Full Core Cycle Coordinator
→ X4  full-core Evidence and human stabilization

→ optional INT-DOC-600  Extension Boundary Study
→ optional INT-DOC-700  one selected extension package
```

Каждый `INT-DOC-*` имеет один итоговый результат, связанные внутренние шаги, exact scope, обязательный internal self-check, одну bounded correction pass внутри исходного scope, terminal Stage Report и `STOP`. Следующий интервал не запускается автоматически.

Это documentation roadmap. Он не является implementation roadmap, Task Brief, Execution Authorization, Git authorization, acceptance record или activation record.

---

## 2. Статус, activation и граница baseline

`R6` — exact human-accepted baseline, указанный человеком для этой revision. `R7` — новый `DRAFT / PROPOSAL`.

```yaml
R6:
  role: ACCEPTED_BASELINE_FOR_R7_AUTHORING
  mutation: FORBIDDEN
R7:
  human_acceptance: NOT_RUN
  roadmap_activation: NOT_RUN
  active_interval: null
  implementation_authorization: NONE
  git_authorization: NONE
```

До explicit human acceptance exact hash-bound `R7`:

- `R7` не становится current roadmap state;
- `INT-DOC-001` не начинается;
- `planning/CURRENT.md` не создаётся и не изменяется;
- `R6` не архивируется и сохраняет свой принятый baseline status;
- никакая documentation, implementation или Git mutation не разрешается этим документом.

После human acceptance exact `R7` activation остаётся отдельным действием. Acceptance не активирует интервал автоматически.

---

## 3. Authoritative owners

`R7` владеет только порядком documentation intervals и их dependencies после explicit human acceptance и activation exact revision.

| Fact class | Authoritative owner |
|---|---|
| Project identity, authority, statuses, Minimal Safety Floor | `docs/00_Core.md` |
| Users, problems, product boundaries, journeys | `docs/01_Product.md` |
| Layer boundaries, shared contract classes, data ownership | `docs/02_Architecture.md` |
| Task stages, validation, review, recovery and Git boundaries | `docs/03_Development.md` |
| Lessons and regression candidates | `docs/04_Lessons.md` |
| Research routing and provenance | `docs/05_Reference.md` |
| Feature inventory and dossiers | `docs/06_Features.md` |
| Documentation interval sequence and dependency order | exact accepted and activated `R7` |
| Current progress | future single state owner derived from accepted sequence |
| Actual repository state | direct current repository observation |
| Human decision | exact human-authored or human-verified decision record |

```yaml
artifact:
  path: AOS-3/AOS_Core_Roadmap.md
  artifact_id: AOS-CORE-ROADMAP
  role: HISTORICAL_EVIDENCE_OF_SEPARATE_PORTABLE_PACKAGE
  authority_over_current_documentation_sequence: NONE
  competing_owner: false
  supersession_effect: NONE
```

Coverage artifacts mirror decisions and never own `human_disposition`. Any conflict with an exact human decision makes the mirror stale.

---

## 4. Interval boundary rule

### 4.1. When work stays inside one interval

Related work stays inside one interval when all of the following remain unchanged:

- one primary outcome;
- one authority boundary;
- one authorized path set;
- one set of authoritative inputs;
- no new required human product, architecture or authority decision;
- no external implementation/Evidence gate;
- one terminal Stage Report.

Research, outline, drafting, cross-document reconciliation, structural checks, semantic checks and correction of in-scope authoring defects are internal steps. They are not separate roadmap tasks.

### 4.2. When work becomes another interval

A new interval is required only when at least one material boundary changes:

1. the primary result changes;
2. an authority owner or authorized path set changes;
3. a new human decision is required;
4. an external Evidence dependency must close;
5. a separately validated subject is required before continuing;
6. the next work would expand the accepted scope.

### 4.3. One run — one stage

Canonical stages remain:

```text
PLAN | EXECUTE | VALIDATE | REVIEW | DELIVER
```

One documentation interval is one `EXECUTE` run. Internal authoring steps do not introduce new stages. The interval ends with Stage Report and `STOP`; the later `VALIDATE` run is a new invocation and cannot be embedded in the interval.

```text
internal self-check inside EXECUTE ≠ canonical VALIDATE
EXECUTE Stage Report → STOP
new read-only VALIDATE invocation → Verification Report → STOP
```

---

## 5. Work-item types

### 5.1. `DOCUMENTATION_INTERVAL`

```yaml
work_item_type: DOCUMENTATION_INTERVAL
canonical_stage: EXECUTE
one_primary_outcome: REQUIRED
internal_steps: ALLOWED_WITHIN_EXACT_SCOPE
internal_self_check: REQUIRED
in_scope_self_correction: BOUNDED
terminal_stage_report: REQUIRED
stop_after_report: true
automatic_next_interval_start: FORBIDDEN
implementation_authorization: NONE
git_authorization: NONE
```

### 5.2. `EXTERNAL_EVIDENCE_GATE`

An external gate is not a documentation interval and cannot be passed by writing a protocol.

```yaml
work_item_type: EXTERNAL_EVIDENCE_GATE
initial_status: NOT_RUN
requires:
  - exact subject identity
  - separate human authorization for mutation
  - observed Evidence
  - independent validation appropriate to risk
  - separate human decision
```

### 5.3. `POST_STOP_VERIFICATION`

```yaml
work_item_type: POST_STOP_VERIFICATION
stage: VALIDATE
validation_profile: POST_STOP_DOCUMENTATION
mode: READ_ONLY_NEW_RUN
subject_mutation: FORBIDDEN
repository_mutation: FORBIDDEN
report_persistence: NON_DURABLE_TERMINAL_RESPONSE
automatic_next_interval_start: FORBIDDEN
human_decision_creation: FORBIDDEN
implementation_authorization: NONE
git_authorization: NONE
```

### 5.4. `RECORD_VERIFICATION_RESULT`

Persistence is outside `VALIDATE` and requires a separate authorized `EXECUTE` run.

```yaml
work_item_type: RECORD_VERIFICATION_RESULT
stage: EXECUTE
initial_status: NOT_AUTHORIZED
allowed_mutation_if_separately_authorized:
  - persist exact Verification Report
  - atomically update exact verification lifecycle state owner
subject_mutation: FORBIDDEN
implementation_authorization: NONE
git_authorization: NONE
```

`R7` does not authorize this work item and does not create its state owner.

---

## 6. Internal self-check and bounded correction

### 6.1. Required internal check

At the end of every documentation interval, before the Stage Report, the authoring agent checks:

1. the declared scope is complete;
2. every expected output exists at the declared path;
3. Markdown/YAML structure, IDs, fences and relative links are valid;
4. the new material has no internal logical contradiction;
5. the outputs agree with declared authoritative project sources;
6. dependencies and traceability are complete;
7. the result is usable by the next interval without chat history;
8. no path outside the interval allowlist changed;
9. no human decision, acceptance, readiness or authorization was invented;
10. implementation and Git operations remain `NOT_RUN`.

The Stage Report records each check as `PASS | FAIL | BLOCKED | UNKNOWN | NOT_RUN`. Required `NOT_RUN` cannot aggregate to `PASS`.

### 6.2. In-scope correction pass

Internal correction belongs to the same `EXECUTE` interval only when it fixes an authoring defect and all of the following are true:

```yaml
subject: OUTPUTS_OF_CURRENT_INTERVAL_ONLY
allowed_paths: EXACT_INTERVAL_ALLOWLIST_ONLY
correction_source: DECLARED_AUTHORITATIVE_INPUT_OR_MECHANICALLY_UNIQUE_RESULT
max_correction_passes_after_initial_self_check: 1
scope_expansion: FORBIDDEN
new_output_class: FORBIDDEN
semantic_choice_among_valid_alternatives: FORBIDDEN
human_decisions: FORBIDDEN
product_decisions: FORBIDDEN
architecture_decisions: FORBIDDEN
authority_changes: FORBIDDEN
implementation: FORBIDDEN
git_operations: FORBIDDEN
recursive_task_creation: FORBIDDEN
```

The agent batches all detected in-scope defects into that correction pass and reruns the full internal check once. This is bounded authoring reconciliation, not a dispatcher, canonical `VALIDATE`, recursive retry or autonomous self-heal loop.

If an in-scope defect remains after the correction pass, the interval returns `FAIL`, reports the exact defect and stops. If a correction requires a product, architecture, authority or human decision, a scope expansion, a new path or new permission, the interval returns `BLOCKED` and stops without making that change.

### 6.3. Terminal behavior

```text
authoring steps
→ internal self-check
→ optional one in-scope correction pass
→ full internal recheck
→ terminal Stage Report
→ STOP
```

No result, including internal `PASS`, starts `VALIDATE`, REVIEW, the next interval, implementation or a Git action automatically.

---

## 7. Canonical post-stop validation model

### 7.1. Trigger and subjects

Post-stop validation is required after every terminal documentation Stage Report: successful output, partial output, `FAIL`, `BLOCKED`, material `UNKNOWN` and no output artifact.

```yaml
trigger_requirement: VALIDATION_MUST_FOLLOW
initial_trigger_mode: MANUAL_NEW_RUN
automatic_dispatch_admission: NOT_RUN
```

Subject kinds:

```text
OUTPUT_ARTIFACT_AND_STAGE_REPORT
PARTIAL_ARTIFACT_AND_STAGE_REPORT
STAGE_REPORT_ONLY
```

Normative flow:

```text
DOCUMENTATION_INTERVAL
→ terminal Stage Report
→ STOP
→ VERIFICATION_PENDING
→ separate new invocation:
    stage = VALIDATE
    validation_profile = POST_STOP_DOCUMENTATION
→ non-durable Verification Report
→ STOP
→ separate persistence / correction / human / next-interval route
```

`POST_STOP_DOCUMENTATION` is a profile, not a stage enum. `POST_STOP_VERIFY` is not introduced.

### 7.2. Validator boundary

The separate `VALIDATE` run:

- is read-only and zero-write;
- freezes and verifies the exact subject identity;
- does not mutate or correct the subject;
- does not persist its own report;
- does not create a human decision;
- does not start a next interval;
- does not authorize implementation or Git;
- returns one terminal Verification Report and stops.

Verification `PASS` means only that required checks passed for the exact subject, profile, task/interval contract and dependency identities.

Verification Report schema remains explicit:

```yaml
stage: VALIDATE
validation_profile: POST_STOP_DOCUMENTATION
work_item_type: POST_STOP_VERIFICATION
mode: READ_ONLY_NEW_RUN

subject:
  task_id:
  interval_instance_id:
  stage_report_identity:
  subject_kind:
  paths: []
  subject_set_sha256_or_absent_marker:
  artifact_types: []
  interval_contract_revision:

validation_identity:
  profile_sha256:
  dependency_set_sha256:
  verifier_identity:
  verifier_version:
  verification_id:

technical_result: >
  CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN |
  NOT_RUN | PASS | HUMAN_REVIEW_REQUIRED

checks:
  identity:
    required: true
    result:
  structural_contract:
    required: true
    result:
  authoritative_inputs:
    required: true
    result:
  semantic_completeness:
    required: true
    result:
  traceability:
    required: true
    result:
  agent_usability:
    required:
    result:
  authority_safety:
    required: true
    result:
  downstream_readiness:
    required: true
    result:
  zero_write:
    required: true
    result:

readiness_state:
readiness_reason:
human_decision: null
implementation_authorization: NONE
git_authorization: NONE
report_persistence: NOT_RUN

findings: []
required_corrections: []
blockers: []
next_bounded_action:
stop: true
```

Zero-write Evidence records repository identity before/after, changed paths, every subject SHA before/after and staging-area change. Any mutation caused by `VALIDATE` is a contract violation.

### 7.3. Persistent lifecycle

```text
TASK_ACTIVE
→ TASK_REPORTED
→ VERIFICATION_PENDING
→ VERIFICATION_RUNNING
→ VERIFIED_PASS
  | VERIFIED_CONTRACT_VIOLATION
  | VERIFIED_FAIL
  | VERIFIED_BLOCKED
  | VERIFIED_UNKNOWN
  | VERIFIED_NOT_RUN
  | VERIFIED_HUMAN_REVIEW_REQUIRED
→ CORRECTION_PENDING
  | HUMAN_REVIEW_PENDING
  | EXTERNAL_EVIDENCE_PENDING
  | NEXT_INTERVAL_PROPOSED
```

For an interval, canonical `current_task_id` is populated with the exact interval-instance ID. `R7` does not introduce competing lifecycle tokens such as `INTERVAL_ACTIVE`.

Planned single durable owner after acceptance and separate activation:

```yaml
state_owner: planning/CURRENT.md
ownership_status_before_human_acceptance: NOT_ACTIVE
creation_or_mutation_authorized_by_R7: false
```

Read-only `VALIDATE` cannot mutate durable state. Durable recording requires separately authorized `RECORD_VERIFICATION_RESULT`. The next interval is forbidden until the validation route closes and every applicable human/external gate closes.

### 7.4. Technical result, readiness and human decision

Technical result:

```text
CONTRACT_VIOLATION
FAIL
BLOCKED
UNKNOWN
NOT_RUN
PASS
HUMAN_REVIEW_REQUIRED
```

Human decision:

```text
ACCEPT | NEEDS_CHANGES | REJECT | DEFER
```

Closed readiness vocabulary:

```text
NOT_READY
READY_FOR_HUMAN_REVIEW
READY_FOR_NEXT_DOCUMENTATION_TASK
READY_FOR_PORTABLE_TASK_DERIVATION
TARGET_REPOSITORY_ASSIGNMENT_REQUIRED
TARGET_BINDING_REQUIRED
READY_FOR_TARGET_BOUND_TASK_BRIEF
READY_FOR_IMPLEMENTATION_HUMAN_DECISION
EXTERNAL_EVIDENCE_REQUIRED
```

`NEEDS_CHANGES` and `BLOCKED` are not readiness states. Unqualified `READY`, `DONE`, `COMPLETE` and `IMPLEMENTATION_READY` are forbidden as authoritative states. Technical result, readiness and human decision remain independent; none creates acceptance or authorization.

### 7.5. Fail-closed aggregation

```text
contract violation → CONTRACT_VIOLATION
else required FAIL → FAIL
else required BLOCKED → BLOCKED
else required UNKNOWN → UNKNOWN
else required NOT_RUN → NOT_RUN
else human gate required → HUMAN_REVIEW_REQUIRED
else → PASS
```

Optional `NOT_RUN` may remain visible without blocking only when the check is explicitly optional.

### 7.6. Verification identity and invalidation

```yaml
verification_identity_inputs:
  - task_id_bound_to_interval_instance_id
  - task_or_interval_contract_revision_or_sha256
  - stage_report_sha256
  - subject_set_sha256_or_absent_marker
  - validation_profile_sha256
  - authoritative_dependency_set_sha256
  - verifier_identity_and_version
```

Cached verification is invalidated by any subject change, Stage Report change, interval-contract change, profile change, authoritative owner/dependency change, verifier implementation/version change, relevant human decision or stale target binding.

### 7.7. Risk-scaled depth and cold-start usability

```text
L0 — deterministic identity and structure
L1 — semantic completeness and authority
L2 — independent cold-start agent usability
```

Product/Feature Contracts, task contracts, runner/coordinator contracts, validation profiles and implementation-handoff/readiness claims require `L2`.

At `L2`, an independent agent receives only declared authoritative inputs and must identify purpose/scope, missing human decisions and one next bounded interval/task or blocker; derive acceptance and negative scenarios where applicable; avoid chat history; and avoid inferred target facts. This produces Evidence only.

### 7.8. Bootstrap independence

`INT-DOC-001` outputs use the inline rules in this exact `R7` only for bootstrap validation:

```text
R7 inline bootstrap contract
→ separate independent VALIDATE of exact INT-DOC-001 output set and Stage Report
→ author/verifier identities recorded
→ human review of exact validation profile artifact
→ explicit human decision
→ profile lifecycle may become HUMAN_ACCEPTED
→ normal POST_STOP_DOCUMENTATION use
```

The profile cannot validate and activate itself. Profile acceptance is not roadmap activation, implementation authorization or Git authorization.

### 7.9. Correction after canonical VALIDATE

`VALIDATE` only detects, classifies and routes findings. Any post-stop correction is a new `EXECUTE` run bound to the exact subject path/set, SHA-256, finding IDs and authorized paths. Preauthorization may cover one mechanically unique correction attempt only; semantic, product, architecture, authority, human-decision, implementation and Git changes require new explicit human authorization. Failed correction stops and returns to the human route. No recursive correction loop is permitted.

---

## 8. Documentation interval contract

Every activated interval must be instantiated from this format. Internal steps are not child tasks.

```yaml
interval_id:
work_item_type: DOCUMENTATION_INTERVAL
stage: EXECUTE
title:
status: DRAFT

primary_outcome:
authoritative_inputs: []
supporting_inputs: []
feature_refs: []
decision_refs: []

start_conditions: []
allowed_paths: []
forbidden_changes: []
expected_outputs: []
internal_steps: []
dependencies: []

completion_conditions: []
internal_self_check:
  required: true
  checks: []
  max_correction_passes_after_initial_check: 1
  repeat_full_check_after_correction: true
  block_on_new_decision_or_scope: true

negative_scenarios: []
known_unknowns: []
invalidation_conditions: []

post_stop_validation:
  required: true
  canonical_stage: VALIDATE
  validation_profile: POST_STOP_DOCUMENTATION
  mode: READ_ONLY_NEW_RUN
  initial_trigger_mode: MANUAL_NEW_RUN
  automatic_dispatch: NOT_AUTHORIZED
  next_interval_start_before_validation_close: FORBIDDEN

correction_policy:
  preauthorized: false
  exact_subject_paths: []
  allowed_finding_classes: []
  max_attempts: 0
  scope_expansion: FORBIDDEN
  semantic_change: FORBIDDEN
  human_decisions: FORBIDDEN
  product_decisions: FORBIDDEN
  architecture_decisions: FORBIDDEN
  authority_changes: FORBIDDEN
  implementation: FORBIDDEN
  git_operations: FORBIDDEN

technical_result: NOT_RUN
readiness_state: NOT_READY
decision_record_status: NOT_RUN
human_decision: null
implementation_authorization: NONE
git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action:
stop: true
```

The Stage Report uses the canonical schema in `docs/03_Development.md` and additionally records interval ID, exact output-set identity, internal check results, correction-pass count and out-of-scope reconciliation.

---

## 9. Feature coverage and lazy decisions

The accepted inventory owner remains `docs/06_Features.md`. `R7` does not change any `human_disposition`.

| Coverage | Placement proposal | Critical-path effect |
|---|---|---|
| `FTR-001`, `FTR-002`, `FTR-003`, `FTR-005` | `INT-DOC-200/210/300` | Core documentation |
| `FTR-004`, `FTR-008`, `FTR-011`, `FTR-014`, `FTR-016`, `FTR-019` | `INT-DOC-100`, then integrated by later intervals | Core documentation |
| `FTR-006`, `FTR-007`, `FTR-009`, `FTR-010`, `FTR-012`, `FTR-013`, `FTR-015` | `INT-DOC-001/300/400/500` | Core documentation; backlog depth and runner scope remain simplified/bounded |
| `FTR-021`, `FTR-025`, `FTR-029`, `FTR-030` | accepted invariants used where applicable; advanced depth stays conditional | Does not silently select advanced scope |
| `FTR-017`, `FTR-018`, `FTR-020`, `FTR-022`, `FTR-023`, `FTR-024`, `FTR-026`, `FTR-027`, `FTR-028` | `INT-DOC-600/700` only after exact gates | Outside core critical path |

All IDs `FTR-001…FTR-030` are present exactly once in this placement matrix. Presence is coverage, not selection, priority, acceptance or implementation authorization.

Just-in-time decision boundaries:

| Before interval | Required bounded human decision |
|---|---|
| `INT-DOC-100` | Foundation scope only |
| `INT-DOC-210` | exact first segment/job/slice |
| `INT-DOC-300` | core Pipeline scope informed by `X1` |
| each `INT-DOC-400` instance | one next runner package identity |
| `INT-DOC-600` | measured extension-study need |
| `INT-DOC-700` | one exact selected extension and its disposition |

Unselected features remain `UNDECIDED` and do not block earlier intervals.

Extension-kind taxonomy remains:

| Extension kind | Candidate features |
|---|---|
| `RUNTIME_MODULE` | `FTR-017` |
| `FACTORY_ADAPTER` | `FTR-018`, `FTR-023` |
| `GOVERNANCE_EXTENSION` | `FTR-020`, advanced `FTR-021` |
| `KNOWLEDGE_PACK` | `FTR-022` |
| `DELIVERY_ADAPTER` | `FTR-024` |
| `OBSERVABILITY_EXTENSION` | advanced `FTR-025` |
| `DOMAIN_MODULE` | separate Medical and Design parts of `FTR-027` |
| `UI_CLIENT` | `FTR-028` |
| `TEMPLATE_PACK` | advanced `FTR-029` |
| `INTERNAL_TOOLING` | advanced `FTR-030` |
| `EXTENSION_SYSTEM_CANDIDATE` | `FTR-026`, after repeated extension cases only |

---

## 10. Sequence and dependency matrix

| Order | Interval/gate | One primary result | Starts only after | Ends with |
|---|---|---|---|---|
| 1 | `INT-DOC-001` | usable documentation control foundation | accepted and activated exact `R7` | internal check, Stage Report, STOP |
| 2 | separate `VALIDATE` + human profile decision | independently validated bootstrap and exact profile decision | terminal `INT-DOC-001` report | Verification Report, STOP; then human decision |
| 3 | `INT-DOC-100` | coherent Product Runtime foundation package | control foundation route closed; Foundation scope decision | internal check, Stage Report, STOP |
| 4 | `INT-DOC-200` | decision-ready first-slice selection package | accepted foundation package | internal check, Stage Report, STOP |
| 5 | `INT-DOC-210` | exact first-slice contract and portable handoff package | exact human first-slice decision | internal check, Stage Report, STOP |
| 6 | `X1` | observed first-slice implementation and real-task Evidence | accepted first-slice documentation; separate permissions | external Evidence and human stabilization decision |
| 7 | `INT-DOC-300` | complete manual-ready development route | exact human `ACCEPT` at `X1` | internal check, Stage Report, STOP |
| 8 | `X2` | observed manual dogfood Evidence | accepted manual-ready route; separate permissions | external Evidence and human automation-admission decision |
| 9 | `INT-DOC-400` | one coherent runner package | exact `X2` admission or prior `X3` stabilization; selected package ID | internal check, Stage Report, STOP |
| 10 | `X3` | implementation/regression Evidence for exact runner package | accepted exact runner package; separate permissions | external Evidence and human stabilization decision |
| 11 | `INT-DOC-500` | full-core coordination package | all required runner packages stabilized through `X3` | internal check, Stage Report, STOP |
| 12 | `X4` | full-core Evidence and stabilization | accepted full-core package; separate permissions | external Evidence and human decision |
| 13 | optional `INT-DOC-600` | decision-ready extension boundary study | `X4`, measured need, human study decision | internal check, Stage Report, STOP |
| 14 | optional `INT-DOC-700` | one exact extension documentation package | human selection after boundary study | internal check, Stage Report, STOP |

Every documentation interval is followed by a separate `VALIDATE` run and any declared human review before the dependency in the next row is considered closed. The table never authorizes automatic transition.

---

## 11. `INT-DOC-001` — Documentation Control Foundation

This is the first interval that may be handed to a documentation-capable coding agent after exact `R7` acceptance and separate activation.

```yaml
interval_id: INT-DOC-001
work_item_type: DOCUMENTATION_INTERVAL
stage: EXECUTE
title: Create Documentation Control Foundation
status: DRAFT

primary_outcome: >
  Create one coherent, reviewable control foundation that lets a cold-start
  agent locate authority, instantiate later intervals, validate terminal
  documentation outputs, preserve feature coverage and report progress.

authoritative_inputs:
  - docs/00_Core.md
  - docs/01_Product.md
  - docs/02_Architecture.md
  - docs/03_Development.md
  - docs/04_Lessons.md
  - docs/05_Reference.md
  - docs/06_Features.md
  - planning/AOS_Documentation_Task_Sequence_R7.md
supporting_inputs:
  - planning/AOS_Documentation_Task_Sequence_R6.md
  - AOS-3/AOS_Core_Roadmap.md

start_conditions:
  - exact R7 human acceptance recorded
  - separate activation of INT-DOC-001 recorded
  - repository and source identities observed read-only
  - allowed paths confirmed absent or explicitly authorized for replacement

allowed_paths:
  - planning/AOS_Authoritative_Owner_Map_R1.md
  - planning/verification/POST_STOP_DOCUMENTATION_VALIDATION_CONTRACT_R1.md
  - planning/AOS_Documentation_Task_Manifest_R1.md
  - planning/AOS_Gate_Status_Usage_Profile_R1.md
  - planning/AOS_Feature_Coverage_Ledger_R1.md
  - planning/AOS_Portable_Task_Candidate_Contract_R1.md
  - planning/AOS_Target_Binding_And_Task_Conversion_Protocol_R1.md
  - planning/AOS_Documentation_Progress_Checklist_R2.md

expected_outputs:
  - authoritative owner map
  - post-stop documentation validation contract
  - interval manifest and dependency graph
  - canonical status/gate usage profile
  - feature coverage ledger with no dispositions
  - portable task candidate contract
  - target binding and task conversion protocol
  - progress checklist schema

internal_steps:
  - map fact classes to exact owners and classify historical/supporting artifacts
  - define the bootstrap validation contract without activating it
  - derive the interval manifest and acyclic dependencies from R7
  - bind status, readiness and human-decision vocabularies to canonical owners
  - map FTR-001 through FTR-030 without changing human dispositions
  - define portable-to-target-bound conversion and exact authority boundaries
  - define progress views as derived state, not competing owners
  - reconcile cross-artifact references and run the required internal self-check

forbidden_changes:
  - modification of docs owners, R6, R7 or AOS-3
  - profile self-activation or self-acceptance
  - creation or modification of planning/CURRENT.md
  - product/architecture decisions
  - feature selection or disposition changes
  - implementation or Git operations

completion_conditions:
  - all eight expected outputs exist at the exact allowed paths
  - owner map has one owner per fact class and preserves historical boundary
  - manifest is acyclic and names interval-level outcomes, not step-level tasks
  - validation contract covers all terminal report kinds and remains read-only
  - task conversion does not infer target facts or authorization
  - cold-start agent can identify INT-DOC-100 or an exact blocker
  - full internal self-check passes after at most one correction pass

negative_scenarios:
  - missing or duplicate authority owner
  - historical roadmap treated as current authority
  - validation profile activates itself
  - internal check presented as canonical VALIDATE
  - feature ledger changes human disposition
  - portable candidate contains invented target facts
  - next interval starts before post-stop validation closes
  - any path outside allowlist changes

post_stop_validation:
  required: true
  canonical_stage: VALIDATE
  validation_profile: BOOTSTRAP_INLINE_R7_DOCUMENTATION_VALIDATION
  mode: READ_ONLY_NEW_RUN
  independence_required: true
  next_interval_start_before_validation_close: FORBIDDEN

technical_result: NOT_RUN
readiness_state: NOT_READY
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
next_required_action: INDEPENDENT_VALIDATE_EXACT_INT_DOC_001_OUTPUT_SET
stop: true
```

Normal `POST_STOP_DOCUMENTATION` use begins only after independent validation and exact human acceptance of its profile artifact. `R7` does not perform or record that decision.

After the internal self-check and at most one correction pass, `INT-DOC-001` returns its terminal Stage Report and `STOP`; bootstrap validation starts only in a new invocation.

---

## 12. `INT-DOC-100` — Product Runtime Foundation

**Primary result:** one coherent foundation package for a minimal Product Runtime that supports the first slice without importing full Factory or optional-extension complexity.

```yaml
depends_on:
  - closed INT-DOC-001 validation/profile route
  - exact human Foundation scope decision
output_path: planning/foundation/AOS_Product_Runtime_Foundation_Package_R1.md
feature_refs: [FTR-004, FTR-008, FTR-011, FTR-014, FTR-016, FTR-019]
```

Internal steps cover the Product Runtime boundary, architecture skeleton, accepted primitive reuse/gaps, bootstrap/install/First-Start, interaction/status/tutor, project state/continuity, doctor/self-test and foundation recovery. They produce one integrated contract package, not eight independent roadmap tasks.

The interval excludes full task conveyor, full runner, generic plugin system, module marketplace, full Governance, RAG/vector DB, Workbench/SaaS and domain architecture. Any unresolved architecture choice with more than one valid option returns `BLOCKED` for human decision.

Completion requires a cross-section consistency check, exact traceability to owners/features, negative scenarios, recovery, next-interval usability and allowed-path reconciliation. Then Stage Report → `STOP` → separate `VALIDATE`.

---

## 13. `INT-DOC-200` — First-Slice Human Decision Package

**Primary result:** one decision-ready package enabling a human to select the exact first segment, job and observable vertical slice.

```yaml
depends_on:
  - accepted Product Runtime Foundation package
output_path: planning/first-slice/AOS_First_Slice_Decision_Package_R1.md
feature_refs: [FTR-001, FTR-002, FTR-003, FTR-005]
human_decision_created_by_agent: false
```

Internal steps compare bounded candidates against user problem, observable result, dependency surface, I/O/states/failures/recovery, manual testability and Foundation fit. The agent may identify missing Evidence and recommend options, but cannot select the slice.

Completion means the package is decision-ready, not that a decision exists. Stage Report → `STOP` → separate `VALIDATE` → human decision. `INT-DOC-210` remains blocked until an exact human selection exists.

---

## 14. `INT-DOC-210` — Exact First-Slice Contract and Handoff Package

**Primary result:** one implementation-handoff-ready documentation package for the exact human-selected first slice.

```yaml
depends_on:
  - exact human first segment/job/slice decision
output_path: planning/first-slice/AOS_First_Slice_Contract_Package_R1.md
feature_refs: [FTR-003, FTR-005, FTR-006, FTR-011, FTR-012, FTR-013]
```

Internal steps define the exact Feature Contract, required ADR or `NO_ADR_REQUIRED`, UX/manual acceptance protocol, independent validation plan and Portable Task Candidate manifest using the contract from `INT-DOC-001`. The interval does not assign an implementation repository, bind target facts or create Execution Authorization.

Completion requires L2 cold-start usability, traceability, acceptance/negative tests and consistent handoff boundaries. Stage Report → `STOP` → separate `VALIDATE` → human review. Only accepted documentation may open external gate `X1`; it does not pass `X1`.

---

## 15. `X1` — First-slice implementation and real-task Evidence

```yaml
work_item_type: EXTERNAL_EVIDENCE_GATE
status: NOT_RUN
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
```

Required records remain: human implementation-repository assignment, read-only target preflight, Target Repository Binding, Target-Bound Task Brief, Human Task Decision, human-assigned Risk Profile, Execution Authorization, EXECUTE Stage Report, independent Validation Evidence, manual real-task Evidence and Human Slice Stabilization Decision.

Only exact human `ACCEPT` of first-slice stabilization may unblock `INT-DOC-300`. Without it, later work may be discussed read-only but is not activated.

---

## 16. `INT-DOC-300` — Manual-Ready Development Route

**Primary result:** one coherent text contract package for the complete manual development route, including its dogfood and recovery protocols.

```yaml
depends_on:
  - exact human ACCEPT at X1
output_path: planning/pipeline/AOS_Manual_Development_Route_Package_R1.md
feature_refs:
  - FTR-001
  - FTR-002
  - FTR-003
  - FTR-005
  - FTR-006
  - FTR-007
  - FTR-009
  - FTR-010
  - FTR-011
  - FTR-012
  - FTR-013
  - FTR-014
  - FTR-015
  - FTR-016
  - FTR-019
  - FTR-025
```

Internal steps define and reconcile:

```text
Problem Interview
→ Project Discovery
→ DRAFT Product Spec / Feature Contract
→ Accepted Specification Baseline
→ lazy decomposition
→ Portable Task Candidate
→ target assignment / read-only preflight
→ Target Repository Binding
→ Target-Bound Task Brief
→ Human Task Decision
→ Human Risk Profile
→ Execution Authorization
→ EXECUTE
→ VALIDATE / Evidence
→ REVIEW / Human Decision
→ separately authorized Git actions
→ recovery / context / lessons
```

The same interval adds manual dogfood protocols for a disposable fixture, positive/ambiguous/stale/denied/failure/interruption/`NEEDS_CHANGES`/required-`NOT_RUN` scenarios, Evidence collection and contract correction/invalidation. Protocols do not claim observed Evidence.

The package must define each handoff's producer, consumer, input/output, state transition, authority boundary, failure class, invalidation rule and report/stop behavior. Internal self-check must verify route closure and protocol-to-contract traceability. Then Stage Report → `STOP` → separate `VALIDATE`. Accepted documentation opens `X2` only.

---

## 17. `X2` — Observed manual dogfood Evidence

```yaml
work_item_type: EXTERNAL_EVIDENCE_GATE
status: NOT_RUN
default_subject: DISPOSABLE_FIXTURE
implementation_authorization: NONE
git_authorization: NONE
```

Required Evidence remains: at least two complete manual cycles, one failure/recovery cycle, handoff/interface defect log, clarification/scope-drift measurements, correction Evidence and an exact human automation-admission decision.

Admission requires proven repetition, stable contracts, known failures, fallback/removal, no authority expansion and explicit human `ACCEPT`.

---

## 18. `INT-DOC-400` — One Bounded Runner Package

**Primary result:** one coherent runner package for one explicitly selected bounded capability, including coordinator integration and full-route regression contract.

```yaml
interval_pattern_id: INT-DOC-400
instance_identity: INT-DOC-400/<selected_package_id>/<contract_revision>
depends_on:
  first_instance: exact human automation-admission decision at X2
  later_instance: exact human stabilization of prior package at X3
output_path_pattern: planning/runner/AOS_Bounded_Runner_<selected_package_id>_R1.md
one_selected_package_per_interval: true
```

Allowed package candidates preserve the R6 route:

| Package ID | One package outcome | Runtime entrypoints described, not executed |
|---|---|---|
| `CYCLE-COORDINATOR` | thin state/transition coordinator | status, next, details, allowed transition, stop |
| `INTENT-SPEC` | intent/discovery/specification runner contract | intake, discovery, specification, conditional architecture support |
| `PORTABLE-TASK` | decomposition and portable-task runner contract | decompose, portable task build |
| `TARGET-AUTHORITY` | target binding and task-authority runner contract | preflight, target bind, task brief, decision/risk/auth recording boundaries |
| `SCOPED-EXECUTION` | bounded execution runner contract | EXECUTE only |
| `VALIDATION-REVIEW` | validation/review runner contract | VALIDATE, REVIEW |
| `RECOVERY-CLOSURE` | recovery/context/Git-boundary contract | recovery, handoff, separately authorized Git operations |

Within one instance, the agent may research, draft all related entrypoint contracts, integrate with the thin coordinator, define failure/recovery, build negative fixtures and reconcile neighbor interfaces. These are internal steps, not separate roadmap tasks or runtime stages.

Every described runtime stage still requires a new invocation, exact preflight, one bounded action/read-only assessment, Stage Report and stop. `COMMIT`, `PUSH`, `MERGE` and `RELEASE` never cascade.

The interval ends after its internal self-check with Stage Report → `STOP`. A separate `VALIDATE`, human documentation decision and external `X3` must close before another package instance may be activated. One interval never silently expands to a second package.

---

## 19. `X3` — Per-package implementation and regression Evidence

```yaml
work_item_type: EXTERNAL_EVIDENCE_GATE
package_id: exact
status: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

Required route remains: accepted exact runner package → Portable Task Candidate → target assignment/preflight → Target-Bound Task Brief → Human Task Decision → Human Risk Profile → Execution Authorization → one bounded implementation stage → risk-appropriate validation → full-route regression → human stabilization decision.

The next `INT-DOC-400` instance or `INT-DOC-500` requires explicit selection after this gate. No loop dispatches itself.

---

## 20. `INT-DOC-500` — Full Core Cycle Coordinator

**Primary result:** one full-core coordination package composed from stabilized entrypoints without creating an autonomous multi-stage runner.

```yaml
depends_on:
  - all required INT-DOC-400 packages stabilized through X3
output_path: planning/core/AOS_Full_Core_Cycle_Coordinator_Package_R1.md
```

Internal steps compose the stage graph, cross-stage state/provenance/invalidation, human checkpoints/permissions and full-cycle E2E acceptance protocol. The coordinator may propose one next action, but every stage uses a new invocation and stops at human gates. Core operation must not require extensions.

Completion requires L2 cold-start usability, no autonomous cascade, no generated human authority, explicit stale-state handling and negative scenarios. Stage Report → `STOP` → separate `VALIDATE`. Accepted documentation opens `X4` only.

---

## 21. `X4` — Full-core Evidence and stabilization

```yaml
work_item_type: EXTERNAL_EVIDENCE_GATE
status: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

Evidence scenarios remain: idea-to-reviewed-implementation, existing-repository discovery, interruption/resume, protected-action block, validation failure, human `NEEDS_CHANGES`, separately authorized Git action, no-extension core operation, stale state/authorization invalidation and human full-core stabilization.

Only exact human `ACCEPT` plus a measured extension need may support a separate decision to activate `INT-DOC-600`. Extensions remain outside the core critical path.

---

## 22. `INT-DOC-600` — Conditional Extension Boundary Study

**Primary result:** one decision-ready study that determines whether a measured need should use a dedicated adapter/package/client or justify a shared extension system.

```yaml
activation: CONDITIONAL
depends_on:
  - exact X4 stabilization decision
  - at least one measured extension need
  - explicit human decision to study the boundary
output_path: planning/extensions/AOS_Extension_Boundary_Study_R1.md
```

Internal steps inventory real cases, classify extension kinds, compare dedicated boundaries against shared machinery and prepare one selection package. `FTR-026` requires at least two real extension cases with repeated lifecycle/version/permission needs, material duplication in dedicated adapters, independent core operation and a separate human decision.

No generic plugin marketplace, remote loading, broad admission framework, implementation or automation is authorized. Stage Report → `STOP` → separate `VALIDATE` → human decision.

---

## 23. `INT-DOC-700` — One Selected Extension Package

**Primary result:** one complete documentation package for one exact human-selected extension.

```yaml
activation: CONDITIONAL
one_extension_per_interval: true
depends_on:
  - accepted extension-boundary decision or explicit dedicated-extension decision
  - exact human feature disposition and scope
output_path_pattern: planning/extensions/<selected_extension>/AOS_<selected_extension>_Contract_Package_R1.md
```

Internal steps cover measured need, Product/Feature Contract, architecture/permission/state delta, failure isolation, negative tests and portable implementation candidates. Medical and Design remain separate packages with separate contracts, risk profiles and acceptance.

One extension interval cannot activate another extension, a shared system or implementation. Stage Report → `STOP` → separate `VALIDATE`.

---

## 24. Manual-first automation admission

No dispatcher, automatic trigger or persistence implementation is part of the core sequence.

```yaml
task_id: VERIFY-AUTO-DOC-001
work_item_type: DOCUMENTATION_TASK
status: DEFERRED_UNTIL_MANUAL_VALIDATION_EVIDENCE
critical_path: false
implementation_authorization: NONE
```

Future consideration requires an accepted validation contract, repeated successful manual validations, known failure modes, bounded correction Evidence, fallback/removal and a separate human automation-admission decision. Any future contract must specify trigger event/owner, durable pending state, dedupe key, lock scope, max attempts, retry policy, no retry on material failure, persistence authorization, correction authorization check, fallback/removal and observability.

This deferred item does not block `INT-DOC-001…500`, authorize automatic dispatch or persistence, or change the manual-new-run requirement.

---

## 25. Documentation-to-implementation conversion lane

The recurring conversion lane is unchanged in meaning:

```text
accepted documentation package
→ Portable Task Candidate
→ human target assignment
→ read-only preflight
→ Target Repository Binding
→ Target-Bound Task Brief
→ Human Task Decision
→ Human Risk Profile
→ Execution Authorization
```

Only one next task becomes target-bound. Target facts are never inferred. Contract changes invalidate dependent candidates; repository changes invalidate stale binding; authorization binds to exact task/subject/stage; Git permissions remain separate.

---

## 26. Progress and current-state boundary

After exact `R7` acceptance and a separate authorized activation/state-creation action, a single progress owner may represent:

```yaml
active_interval:
interval_instance:
output_set_identity:
internal_check_result:
stage_report_identity:
verification_status:
verification_report_identity:
human_decision_status:
external_gate_status:
invalidated_by: []
blocker:
next_bounded_action:
```

This document does not create or modify `planning/CURRENT.md`. Progress views are derived and cannot own authority, human decisions or Evidence.

---

## 27. Quality criteria

### Product and architecture

- first slice provides an observable user result before detailed Factory automation;
- core works without extensions;
- one owner exists per fact class;
- optional complexity follows measured need;
- documentation does not claim runtime behavior or Evidence.

### Interval execution

- each interval has one primary outcome and exact scope;
- related authoring steps remain internal;
- internal self-check is complete and one correction pass is bounded;
- new decisions or scope return `BLOCKED`;
- Stage Report and `STOP` end the interval;
- the next interval never starts automatically.

### Validation and authority

- canonical `VALIDATE` is a separate zero-write run;
- internal self-check does not substitute for independent validation;
- technical result, readiness and human decision remain separate;
- acceptance, activation, implementation and Git authority are never inferred;
- validation/persistence/correction use separate boundaries.

### Agent usability

- a cold-start agent can locate exact inputs and allowed paths;
- outputs and completion conditions are observable;
- unknowns and invalidation conditions are explicit;
- one bounded next action is visible;
- no chat history, invented target facts or premature implementation detail is required.

---

## 28. Prohibited shortcuts

- splitting every research, drafting or check step into a roadmap task;
- combining different primary outcomes or human decisions into one interval;
- treating internal self-check as canonical `VALIDATE`;
- correcting a post-stop validation finding inside `VALIDATE`;
- using an in-scope correction pass to expand scope or invent a decision;
- starting the next interval after Stage Report without a new invocation and closed gates;
- treating protocol as observed Evidence;
- activating extensions before full-core Evidence and measured need;
- creating a dispatcher, recursive retry or autonomous self-heal loop;
- executing multiple canonical stages in one run;
- automatic Commit → Push → Merge → Release;
- treating `PASS`, readiness or human acceptance as implementation/Git permission;
- modifying `R6`, archiving prior roadmaps or creating `planning/CURRENT.md` through `R7` authoring.

---

## 29. R6 → R7 structured semantic-diff boundary

```yaml
source_revision: R6
target_revision: R7
allowed_change_classes:
  - frontmatter revision/source fields
  - task_to_large_autonomous_interval_granularity
  - interval_internal_step_grouping
  - internal_self_check_model
  - bounded_in_scope_author_correction_pass
  - interval_level_dependency_and_completion_rules
  - first_handoff_ready_interval_contract
  - task_wording_to_interval_wording_where_required
preserved_without_semantic_weakening:
  - exact_authoritative_owner_routes
  - historical_roadmap_boundary
  - conditional_activation_state
  - documentation_vs_implementation_boundary
  - canonical_stage_vocabulary
  - technical_result_vocabulary
  - readiness_and_human_decision_separation
  - one_run_one_stage
  - terminal_report_and_stop
  - separate_read_only_VALIDATE
  - post_stop_validation_lifecycle
  - validation_persistence_and_correction_separation
  - no_automatic_acceptance
  - no_implementation_or_Git_authorization
  - external_Evidence_gates_X1_X4
  - W2_X1_W3_dependency_semantics
  - FTR_001_FTR_030_coverage_without_disposition_change
  - extensions_outside_core_critical_path
unexpected_change_classes: []
```

The `W0 → W1 → W2 → X1 → W3 → W4 → X2 → W5/X3 → W6 → X4 → W7 → W8` meaning is preserved as `INT-DOC-001 → INT-DOC-100 → INT-DOC-200/210 → X1 → INT-DOC-300 → X2 → INT-DOC-400/X3 → INT-DOC-500 → X4 → optional INT-DOC-600/700`. The only intended design change is authoring granularity plus the bounded internal self-check/correction model requested for large intervals.

---

## 30. One next bounded action

```yaml
next_bounded_action: INDEPENDENT_REVIEW_EXACT_R7
required_mode: READ_ONLY_NEW_RUN
subject_path: planning/AOS_Documentation_Task_Sequence_R7.md
human_acceptance: NOT_RUN
roadmap_activation: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
stop: true
```
