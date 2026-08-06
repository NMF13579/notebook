---
document_type: DEVELOPER_HANDOFF_MANIFEST
package_id: AOS-3-DOCUMENTATION-CORRECTION-PACKAGE-R1
package_revision: R2-CORRECTION-CANDIDATE
status: HUMAN_REVIEW_REQUIRED
authority: DERIVED_NAVIGATION_AND_IDENTITY_ONLY
authority_scope: CORRECTED_DOCUMENTATION_TO_IMPLEMENTATION_SEQUENCE
technical_result: PASS
independent_semantic_validation: NOT_RUN
human_acceptance: NOT_RUN
implementation_repository: NMF13579/aos-3
implementation_repository_creation: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
generated_at: 2026-08-06
---

# AOS-3 — Developer Handoff R2

## 1. Direct answer

The package has two implementation subjects, but only one may become current at a time:

1. `Task-001-Scaffolding` — first;
2. `Task-002-Intake-to-Reviewable-Intent` — only after accepted Task-001 result and fresh baseline rebinding.

This handoff does not authorize repository creation, implementation or Git.

## 2. Canonical entry route

```text
docs/00_Core.md
→ planning/CURRENT.md
→ DEVELOPER_HANDOFF_R2.md
→ current Task/DSP
→ exact behavior and decision owners
→ fresh repository facts
```

Agent must not read all project documents as one instruction set. It loads the task-scoped context for the current subject.

## 3. Current implementation subject — I0

```yaml
order: 1
task: Task-001-Scaffolding.md
DSP: DSP-001.md
contract: AOS_SCAFFOLDING_CONTRACT_R1.md
selected_feature: NONE_INFRASTRUCTURE_PREREQUISITE
user_outcome: REPRODUCIBLE_SAFE_DEVELOPMENT_BASE_WITHOUT_PRODUCT_BEHAVIOR
document_subject_acceptance: ACCEPTED_EXISTING_EXACT_RECORDS
execution_status: NOT_AUTHORIZED
```

Mandatory context:

- `docs/00_Core.md`;
- `docs/02_Architecture.md` relevant topology/safety sections;
- `docs/03_Development.md`;
- mapped `docs/04_Lessons.md`;
- `AOS_IMPLEMENTATION_DECISIONS_R1.md`;
- `AOS_SCAFFOLDING_CONTRACT_R1.md`;
- `Task-001-Scaffolding.md`;
- `DSP-001.md`;
- active root `AGENTS.md` after separate activation;
- fresh repository preflight.

Entry blockers:

```yaml
target_repository_physical_state: NOT_RUN
root_AGENTS_activation: NOT_RUN
fresh_preflight: NOT_RUN
assigned_risk_profile: UNASSIGNED
execution_authorization: NOT_RUN
Git_authorization: NONE
```

## 4. Later implementation subject — X1

```yaml
order: 2
task: Task-002-Intake-to-Reviewable-Intent.md
DSP: DSP-009.md
feature_contract: AOS_FEATURE_CONTRACT_INTAKE_TO_REVIEWABLE_INTENT_R1.md
selected_slice: INTAKE_TO_REVIEWABLE_INTENT_R1
feature_ids: [FTR-001, FTR-008, FTR-011, FTR-016, FTR-019]
FTR-003: UNDECIDED_OUT_OF_SCOPE
user_outcome: REVIEWABLE_INTENT_WITH_VISIBLE_UNKNOWNS_AND_ONE_NEXT_ACTION
document_subject_acceptance: NOT_RUN
execution_status: BLOCKED_UNTIL_I0_ACCEPTED_AND_REBOUND
```

Mandatory context is owned by `DSP-009`. Product Runtime scope never leaks backward into Task-001.

## 5. Repository fact separation

| Axis | State |
|---|---|
| target slug decision | `HUMAN_ACCEPTED: NMF13579/aos-3` |
| physical repository creation | `NOT_RUN` |
| current remote/root/branch/HEAD/worktree | `NOT_RUN / FRESH_OBSERVATION_REQUIRED` |
| implementation documentation | correction candidate under review |
| execution authorization | `NONE` |
| Git permissions | `NONE` |

The accepted target name cannot be used as evidence that a repository exists.

## 6. Package status

```yaml
handoff:
  package_id: AOS-3-DOCUMENTATION-CORRECTION-PACKAGE-R1
  package_revision: R2-CORRECTION-CANDIDATE
  documentation_technical_result: PASS
  package_freeze: NOT_RUN
  human_acceptance: NOT_RUN
  first_task:
    task: Task-001-Scaffolding.md
    DSP: DSP-001.md
    execution_authorization: NOT_RUN
  second_task:
    task: Task-002-Intake-to-Reviewable-Intent.md
    DSP: DSP-009.md
    feature_contract: AOS_FEATURE_CONTRACT_INTAKE_TO_REVIEWABLE_INTENT_R1.md
    baseline_binding: POST_TASK-001_REQUIRED
    human_acceptance: NOT_RUN
    execution_authorization: NOT_RUN
  required_package_checks:
    - CANONICAL_ROUTE_SIMULATION
    - H1_DISPOSITION_MATCH
    - OWNER_AND_STATUS_AUDIT
    - TASK-001_SCOPE_REGRESSION
    - PRODUCT_C002_COMPLETENESS
    - TASK-002_DETERMINACY
    - LINK_AND_HASH_FREEZE
  Git_authorizations:
    commit: NOT_RUN
    push: NOT_RUN
    merge: NOT_RUN
    release: NOT_RUN
  next_required_action: COMPLETE_VALIDATION_AND_EXACT_HUMAN_REVIEW
  stop: true
```

## 7. Agent stop rules

The receiving agent stops and reports one next action when:

- the package or required digest does not match;
- `planning/CURRENT.md` names another subject;
- repository facts are unobserved/stale;
- human acceptance or authorization is missing;
- Task-001 would gain Product Runtime scope;
- Task-002 would run before accepted scaffold baseline;
- any required test is `NOT_RUN/UNKNOWN/BLOCKED` in a claimed `PASS`;
- a Git action is requested without separate exact permission.
