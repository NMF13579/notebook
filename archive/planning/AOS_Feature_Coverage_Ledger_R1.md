---
artifact_id: AOS-FEATURE-COVERAGE-LEDGER-R1
document_type: FEATURE_COVERAGE_LEDGER
revision: R1
status: DRAFT
candidate_role: DRAFT_CANDIDATE
task_id: INT-DOC-010
fact_class: DERIVED_COVERAGE_VIEW
feature_inventory_owner: docs/06_Features.md
sequence_owner: planning/AOS_Documentation_Task_Sequence_R9.md
feature_selection_authority: ITEM_SCOPED_HUMAN_DECISION_ONLY
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# AOS Feature Coverage Ledger R1

## 1. Purpose and boundary

This ledger expands the R9 placement matrix to one row per accepted inventory
ID. It proves coverage only. It does not select, prioritize, accept, reject or
authorize implementation of any feature.

- Identity and dossier content come from [06_Features](../docs/06_Features.md).
- Placement comes from [R9](AOS_Documentation_Task_Sequence_R9.md).
- An exact item-scoped human decision record is the only owner of a feature
  disposition; this ledger contains no disposition field or value.

## 2. Ledger schema

```yaml
coverage_row:
  feature_id: FTR-NNN
  inventory_presence: OBSERVED_AT_SNAPSHOT
  placement: [R9_INTERVAL_OR_GATE]
  critical_path_effect: STRING
  coverage_effect: NAVIGATION_ONLY
  implementation_authorization: NONE
```

## 3. Coverage rows

| Feature | R9 placement | Critical-path effect |
|---|---|---|
| `FTR-001` | `INT-DOC-200/210/300` | Core documentation |
| `FTR-002` | `INT-DOC-200/210/300` | Core documentation |
| `FTR-003` | `INT-DOC-200/210/300` | Core documentation |
| `FTR-004` | `INT-DOC-100`, integrated later | Core documentation |
| `FTR-005` | `INT-DOC-200/210/300` | Core documentation |
| `FTR-006` | `INT-DOC-010/300/400/500` | Core documentation; exact Task Brief and authority boundaries |
| `FTR-007` | `INT-DOC-010/300/400/500` | Core documentation; backlog depth remains simplified and bounded |
| `FTR-008` | `INT-DOC-100`, integrated later | Core documentation |
| `FTR-009` | `INT-DOC-010/300/400/500` | Core documentation; exact preflight boundary |
| `FTR-010` | `INT-DOC-010/300/400/500` | Core documentation; runner scope remains simplified and bounded |
| `FTR-011` | `INT-DOC-100`, integrated later | Core documentation |
| `FTR-012` | `INT-DOC-010/300/400/500` | Core documentation; Evidence and review remain authority-neutral |
| `FTR-013` | `INT-DOC-010/300/400/500` | Core documentation; freeze and validation identity |
| `FTR-014` | `INT-DOC-100`, integrated later | Core documentation |
| `FTR-015` | `INT-DOC-010/300/400/500` | Core documentation; Git permissions remain independent |
| `FTR-016` | `INT-DOC-100`, integrated later | Core documentation |
| `FTR-017` | `INT-DOC-600/700` | Outside core critical path; measured need required |
| `FTR-018` | `INT-DOC-600/700` | Outside core critical path; advisory only before evidence |
| `FTR-019` | `INT-DOC-100`, integrated later | Core documentation and Minimal Safety Floor |
| `FTR-020` | `INT-DOC-600/700` | Outside core critical path |
| `FTR-021` | invariant where applicable; advanced depth conditional | No silent advanced-scope selection |
| `FTR-022` | `INT-DOC-600/700` | Outside core critical path |
| `FTR-023` | `INT-DOC-600/700` | Outside core critical path |
| `FTR-024` | `INT-DOC-600/700` | Outside core critical path |
| `FTR-025` | invariant where applicable; advanced depth conditional | No silent advanced-scope selection |
| `FTR-026` | `INT-DOC-600/700` | Outside core critical path |
| `FTR-027` | `INT-DOC-600/700` | Outside core critical path; domain decision required |
| `FTR-028` | `INT-DOC-600/700` | Outside core critical path |
| `FTR-029` | invariant where applicable; advanced depth conditional | No silent advanced-scope selection |
| `FTR-030` | invariant where applicable; advanced depth conditional | No silent advanced-scope selection |

## 4. Completeness invariants

```yaml
expected_id_range: FTR-001..FTR-030
expected_unique_count: 30
allowed_row_count_per_id: 1
disposition_mutation_allowed: false
selection_effect: NONE
priority_effect: NONE
architecture_effect: NONE
implementation_effect: NONE
```

The ledger fails validation if an ID is absent, duplicated or outside the range.
Disposition lookup always routes to the exact item-scoped human decision record
and its inventory mirror; no disposition is stored here.

## 5. Just-in-time decision boundaries

| Boundary | Human decision still required |
|---|---|
| before `INT-DOC-100` | Foundation scope only |
| before `INT-DOC-210` | exact first segment, job and slice |
| before `INT-DOC-300` | core Pipeline scope informed by `X1` |
| before each `INT-DOC-400` instance | one runner package identity |
| before `INT-DOC-600` | measured extension-study need |
| before `INT-DOC-700` | one extension and its disposition |

Features without an item-scoped decision do not block earlier intervals unless
an exact later contract depends on that decision.

## 6. Negative cases

- coverage treated as selection or priority → `CONTRACT_VIOLATION`;
- `UNDECIDED` rewritten by synthesis → `CONTRACT_VIOLATION`;
- advanced feature moved into core without human scope decision → `BLOCKED`;
- absent or duplicate inventory ID → `FAIL`;
- stale inventory mirror → `CONFLICT`;
- repository presence treated as implementation Evidence → `UNKNOWN` or `NOT_RUN`.

## 7. Status

```yaml
technical_result: NOT_RUN
readiness: NOT_READY
human_decision: null
implementation_authorization: NONE
git_authorization: NONE
```
