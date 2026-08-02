---
artifact_id: AOS-GATE-STATUS-USAGE-PROFILE-R1
document_type: STATUS_AND_GATE_USAGE_PROFILE
revision: R1
status: DRAFT
candidate_role: DRAFT_CANDIDATE
task_id: INT-DOC-010
fact_class: DERIVED_STATUS_USAGE_PROFILE
status_owner: docs/00_Core.md
workflow_owner: docs/03_Development.md
validation_profile_owner: planning/verification/POST_STOP_DOCUMENTATION_VALIDATION_CONTRACT_R1.md
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# AOS Gate and Status Usage Profile R1

## 1. Purpose and authority boundary

This profile tells documentation authors and validators where each existing
status axis may be used. It narrows usage; it does not redefine the owner
vocabularies or create a lifecycle engine.

Owner precedence:

1. [Core](../docs/00_Core.md) — claim, technical-result and human-decision semantics;
2. [Architecture](../docs/02_Architecture.md) — orthogonal state axes;
3. [Development](../docs/03_Development.md) — stage workflow and gates;
4. [Post-Stop Validation Contract](verification/POST_STOP_DOCUMENTATION_VALIDATION_CONTRACT_R1.md) — validation aggregation and readiness;
5. [CURRENT](CURRENT.md) — persisted current lifecycle state only.

## 2. Closed axes

| Axis | Allowed values | Must not imply |
|---|---|---|
| Project claim class | `HUMAN_CONFIRMED_DIRECTION`, `HUMAN_ACCEPTED_FACT`, `OBSERVED_AT_SNAPSHOT`, `REPORTED`, `SYNTHESIZED`, `CONFLICT`, `NOT_FOUND`, `UNKNOWN`, `NOT_RUN`, `BLOCKED` | technical success or authority outside the exact human classes |
| Document maturity | `DRAFT`, `HUMAN_REVIEW_REQUIRED`, `HUMAN_ACCEPTED`, `SUPERSEDED` | execution permission |
| Task stage | `PLAN`, `EXECUTE`, `VALIDATE`, `REVIEW` | another stage or Git action |
| Technical result | `CONTRACT_VIOLATION`, `FAIL`, `BLOCKED`, `UNKNOWN`, `NOT_RUN`, `PASS`, `HUMAN_REVIEW_REQUIRED` | human decision |
| Readiness | `NOT_READY`, `READY_FOR_HUMAN_REVIEW`, `READY_FOR_NEXT_DOCUMENTATION_TASK`, `READY_FOR_PORTABLE_TASK_DERIVATION`, `TARGET_REPOSITORY_ASSIGNMENT_REQUIRED`, `TARGET_BINDING_REQUIRED`, `READY_FOR_TARGET_BOUND_TASK_BRIEF`, `READY_FOR_IMPLEMENTATION_HUMAN_DECISION`, `EXTERNAL_EVIDENCE_REQUIRED` | acceptance, activation or authorization |
| Human decision | `ACCEPT`, `NEEDS_CHANGES`, `REJECT`, `DEFER`, or `null` before decision | technical result or Git permission |
| Permission | `ALLOWED`, `HUMAN_AUTHORIZATION_REQUIRED`, `BLOCKED_POLICY`, `BLOCKED_UNKNOWN`, `NOT_APPLICABLE` | permission on another action |

Unqualified `READY`, `DONE`, `COMPLETE` and `IMPLEMENTATION_READY` are forbidden
as authoritative states. `NOT_RUN` is never rewritten as `PASS`.

The active validation finding schema uses the narrower non-authority subset
`OBSERVED_AT_SNAPSHOT | REPORTED | SYNTHESIZED | CONFLICT | NOT_FOUND |
UNKNOWN | NOT_RUN | BLOCKED`. It never emits either human claim class; those
require an exact human-authored or human-verified record.

## 3. Gate record schema

```yaml
gate_record:
  gate_id: UNIQUE_STRING
  subject_identity: EXACT_PATH_SET_AND_SHA256
  required_checks:
    - check_id: UNIQUE_STRING
      required: true
      result: CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS
      claim_class: OBSERVED_AT_SNAPSHOT | REPORTED | SYNTHESIZED | CONFLICT | NOT_FOUND | UNKNOWN | NOT_RUN | BLOCKED
      evidence_ref: EXACT_LOCATOR_OR_NULL
  aggregate_technical_result: CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS | HUMAN_REVIEW_REQUIRED
  readiness: CLOSED_READINESS_VALUE
  human_decision: null | ACCEPT | NEEDS_CHANGES | REJECT | DEFER
  authorization_effect: NONE
  next_required_action: ONE_BOUNDED_ACTION
```

A missing required field makes the gate record malformed. An optional check
must be explicitly marked optional before `NOT_RUN` can be non-blocking.

## 4. Fail-closed aggregation

Apply exactly this order across required checks:

```text
CONTRACT_VIOLATION
else FAIL
else BLOCKED
else UNKNOWN
else NOT_RUN
else HUMAN_REVIEW_REQUIRED when an applicable human gate remains
else PASS
```

Do not average, vote or promote results. When review is applicable and all
technical checks are otherwise sufficient, the aggregate result is
`HUMAN_REVIEW_REQUIRED`, readiness may be `READY_FOR_HUMAN_REVIEW`, and
`human_decision` remains `null`. `PASS` is reserved for a route with no pending
applicable human gate.

## 5. Gate usage matrix

| Gate | Required subject | Sufficient technical state | Next bounded route |
|---|---|---|---|
| Documentation freeze | Exact output-set manifest plus terminal Stage Report | internal required checks `PASS` | separate `VALIDATE` |
| Post-stop validation | Frozen subject, Stage Report, profile and authoritative dependency identities | aggregate `PASS` or `HUMAN_REVIEW_REQUIRED` with no required `NOT_RUN` | `READY_FOR_HUMAN_REVIEW` when review applies |
| Human review | Exact review subject and Evidence package | technical result remains supporting Evidence | human chooses one exact decision |
| Portable derivation | Accepted documentation sufficient for a task candidate; target intentionally unbound | `READY_FOR_PORTABLE_TASK_DERIVATION` | create candidate only under separate task authority |
| Target binding | Accepted target repository/worktree/branch/HEAD plus required product/architecture contracts | `READY_FOR_TARGET_BOUND_TASK_BRIEF` | `PLAN` only |
| Execution | Exact Task Brief plus unexpired, unconsumed Execution Authorization | permission `ALLOWED` for exact `EXECUTE` | execute exact authorized operations only |
| Git delivery | Exact current candidate and separately authorized Git action | action-specific preflight `PASS` | only the named Commit, Push, Merge or Release |
| External Evidence | Exact implementation subject and observed method | required Evidence present and bound | human stabilization decision |

## 6. Stage usage

```text
PLAN     read-only; produces a decision-ready plan
EXECUTE  mutates only exact authorized paths; reports and stops
VALIDATE read-only and zero-write; never corrects
REVIEW   assesses and recommends; never accepts or mutates
```

`DELIVER` is a handoff concept, not an authority-bearing stage or Git permission.
Documentation correction is a new `EXECUTE` subtype admitted by exact findings.

## 7. Status projection rules

- `planning/CURRENT.md` is the sole durable progress owner.
- Checklists, manifests, dashboards and ledgers are derived views.
- Mutable repository facts require fresh direct observation and
  `OBSERVED_AT_SNAPSHOT`.
- Historical results remain `REPORTED` until reproduced against the current
  exact subject.
- A stale derived view is corrected from the owner; it never corrects the owner
  by inference.

## 8. Negative cases

| Input or claim | Required result |
|---|---|
| required check is `NOT_RUN`, aggregate claimed `PASS` | `CONTRACT_VIOLATION` |
| Evidence or readiness used as human acceptance | `CONTRACT_VIOLATION` |
| `VALIDATE` changes subject or Git state | `CONTRACT_VIOLATION` |
| unknown owner or subject identity | `UNKNOWN` or `BLOCKED` for affected action |
| generated UI/checklist emits `ACCEPT` | reject generated decision |
| one Git permission reused for another action | `BLOCKED` |
| next task activated from a green checklist row | `BLOCKED` |
| invalid free-form enum | `FAIL` |

## 9. Status

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
