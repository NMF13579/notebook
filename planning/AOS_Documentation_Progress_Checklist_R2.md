---
artifact_id: AOS-DOCUMENTATION-PROGRESS-CHECKLIST-R2
document_type: DERIVED_DOCUMENTATION_PROGRESS_CHECKLIST
revision: R2
status: DRAFT
candidate_role: DRAFT_CANDIDATE
task_id: INT-DOC-010
fact_class: DERIVED_PROGRESS_VIEW
sequence_owner: planning/AOS_Documentation_Task_Sequence_R9.md
current_state_owner: planning/CURRENT.md
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# AOS Documentation Progress Checklist R2

## 1. Purpose and boundary

This is a rebuildable checklist schema and cold-start view. It mirrors owners;
it does not own current state, sequence, acceptance, activation, authority or
Evidence. Never update lifecycle facts here instead of
[CURRENT](CURRENT.md).

```text
green row ≠ PASS
PASS ≠ acceptance
closed gate ≠ next-task activation
checklist ≠ authority owner
```

## 2. Row schema

```yaml
progress_row:
  node_id: UNIQUE_R9_NODE_OR_INSTANCE_ID
  sequence_position: POSITIVE_INTEGER
  owner_contract: REPOSITORY_RELATIVE_PATH
  recorded_lifecycle: REPORTED_VALUE_FROM_CURRENT
  terminal_report:
    status: OBSERVED_AT_SNAPSHOT | REPORTED | NOT_FOUND | UNKNOWN | NOT_RUN
    identity: EXACT_LOCATOR_AND_SHA256_OR_NULL
  validation:
    technical_result: REPORTED_RESULT_OR_NOT_RUN
    readiness: CLOSED_READINESS_VALUE
    report_identity: EXACT_LOCATOR_AND_SHA256_OR_NULL
  human_gate:
    required: BOOLEAN
    decision: ACCEPT | NEEDS_CHANGES | REJECT | DEFER | null
    decision_identity: EXACT_LOCATOR_AND_SHA256_OR_NULL
  external_gate:
    required: BOOLEAN
    evidence_status: OBSERVED_AT_SNAPSHOT | REPORTED | NOT_FOUND | UNKNOWN | NOT_RUN
  blockers: [EXACT_BLOCKER]
  next_bounded_action: ONE_ACTION_OR_NONE
  freshness:
    observed_at: RFC3339_TIMESTAMP
    source_hashes: [PATH_AND_SHA256]
  authority_effect: NONE
```

Required fields never use empty strings. `null` is permitted only where the
human decision or exact Evidence has not occurred and must remain visibly
separate from `NOT_RUN`.

## 3. Rebuild algorithm

1. Establish the current explicit human decision.
2. Read `planning/CURRENT.md`; verify its exact referenced identities.
3. Read the accepted R9 sequence and this task manifest for navigation.
4. Resolve each affected fact class through the Owner Map.
5. Re-observe mutable repository facts.
6. Populate only source-supported rows; use `REPORTED`, `NOT_FOUND`, `UNKNOWN`
   or `NOT_RUN` exactly.
7. Apply gate requirements from the Gate and Status Usage Profile.
8. Emit one next bounded action from `CURRENT` or one exact blocker; never
   activate it.

## 4. R9 checklist template

| # | Node | Primary gate before forward route | Owner of current status |
|---:|---|---|---|
| 1 | `INT-DOC-001A` | owner-map validation closed | `CURRENT.md` |
| 2 | `INT-DOC-001B` | independent L2 validation, human `ACCEPT`, profile activation | `CURRENT.md` |
| 3 | `INT-DOC-010` | terminal report, post-stop validation, applicable human review | `CURRENT.md` |
| 4 | `INT-DOC-100` | Foundation scope decision, validated accepted package | `CURRENT.md` |
| 5 | `INT-DOC-200` | validated first-slice decision package | `CURRENT.md` |
| 6 | `INT-DOC-210` | exact first-slice decision and validated accepted handoff | `CURRENT.md` |
| 7 | `X1` | authorized implementation Evidence and stabilization decision | immutable Evidence/decision records mirrored by `CURRENT.md` |
| 8 | `INT-DOC-300` | validated accepted manual-ready route | `CURRENT.md` |
| 9 | `X2` | dogfood Evidence and automation-admission decision | immutable Evidence/decision records mirrored by `CURRENT.md` |
| 10 | `INT-DOC-400/<selected_package_id>/<contract_revision>` | selected package, validated accepted runner contract | `CURRENT.md` |
| 11 | `X3` with exact `package_id` | observed package/regression Evidence and stabilization | immutable Evidence/decision records mirrored by `CURRENT.md` |
| 12 | `INT-DOC-500` | all required packages stable; validated accepted coordinator | `CURRENT.md` |
| 13 | `X4` | full-core Evidence and stabilization decision | immutable Evidence/decision records mirrored by `CURRENT.md` |
| 14 | `INT-DOC-600` | measured need and human study decision | `CURRENT.md` |
| 15 | `INT-DOC-700` | selected extension/disposition and validated package | `CURRENT.md` |

Optional nodes remain absent or `NOT_RUN` until their human gates occur. The
checklist never labels an unstarted optional node `BLOCKED` merely because it is
not selected.

## 5. INT-DOC-010 cold-start rule

For an exact frozen `INT-DOC-010` output set:

```yaml
required_outputs:
  - planning/AOS_Documentation_Task_Manifest_R1.md
  - planning/AOS_Gate_Status_Usage_Profile_R1.md
  - planning/AOS_Feature_Coverage_Ledger_R1.md
  - planning/AOS_Portable_Task_Candidate_Contract_R1.md
  - planning/AOS_Target_Binding_And_Task_Conversion_Protocol_R1.md
  - planning/AOS_Documentation_Progress_Checklist_R2.md
required_terminal_route:
  - internal self-check PASS
  - frozen output-set identity
  - terminal Stage Report
  - independent POST_STOP_DOCUMENTATION VALIDATE
  - task-local STATE_RECORD EXECUTE with PASS
  - applicable human review
next_interval: INT-DOC-100
next_interval_activation: FORBIDDEN_WITHOUT_SEPARATE_HUMAN_DECISION
material_gate_before_int_doc_100: FOUNDATION_SCOPE_HUMAN_DECISION
```

A cold-start agent therefore returns the exact unresolved item among validation,
the mandatory task-local state record, human review and Foundation scope. It
does not start `INT-DOC-100`.

## 6. Consistency checks

- every R9 base node appears exactly once;
- every runner repetition uses unique
  `INT-DOC-400/<selected_package_id>/<contract_revision>` identity and binds its
  exact `package_id` at `X3`;
- current row agrees with `CURRENT.md` or is marked `CONFLICT`;
- every result has an exact report locator or is `REPORTED`/`NOT_FOUND`;
- required `NOT_RUN` prevents a green aggregate;
- human decision remains `null` until an exact record exists;
- readiness uses only the closed vocabulary;
- Git actions remain four independent fields;
- relative links and source hashes are fresh;
- the checklist has `authority_effect: NONE`.

## 7. Negative cases

| Case | Required behavior |
|---|---|
| checklist disagrees with `CURRENT.md` | mark `CONFLICT`; route to owner |
| missing terminal report | `NOT_FOUND`; do not infer completion |
| historical `PASS` after subject change | mark stale; revalidate |
| human decision absent | keep `null`; stop at human boundary |
| required external Evidence absent | `NOT_RUN` or `UNKNOWN`; do not claim ready |
| derived row activates next interval | `CONTRACT_VIOLATION` |
| fourth correction cycle requested | `BLOCKED` |
| `VALIDATE` edits checklist or any subject | `CONTRACT_VIOLATION` |

## 8. Status

```yaml
technical_result: NOT_RUN
readiness: NOT_READY
human_decision: null
implementation_authorization: NONE
git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
```
