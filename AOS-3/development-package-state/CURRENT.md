---
artifact_id: AOS3-DPKG-CURRENT-R17
artifact_type: CURRENT_STATE_POINTER
package_revision: DRAFT-R17
revision: R3
status: DRAFT
authority: ROUTING_AND_LIFECYCLE_STATE_ONLY
current_candidate_revision: DRAFT-R17
latest_human_accepted_revision: DRAFT-R16
latest_acceptance_sidecar: R16_ACCEPTANCE_AND_DELIVERY.md
accepted_composite_sha256: 5ac5b606960fc4f533cdfe7ca3bc95c879c62a3d8f95d1bc10270a469a286a61
candidate_internal_state_role: HISTORICAL_SNAPSHOT
current_lifecycle_state_owner: development-package-state/CURRENT.md
portable_state: PORTABLE_UNBOUND
active_subject_registry: ACTIVE_SUBJECTS_R17.txt
author_self_check_entrypoint: validation/validate_portable_package.py
independent_validation: NOT_RUN
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
merge_authorization: NONE
release_authorization: NONE
---

# Current package state

Это единственный current-state pointer. Он маршрутизирует к fact owners, но не
заменяет их и не создаёт acceptance или permission.

```yaml
current_candidate_revision: DRAFT-R17
working_baseline_revision: DRAFT-R16
working_baseline_disposition: USE_AS_EXACT_HUMAN_ACCEPTED_BASELINE
previous_independent_validation:
  revision: DRAFT-R16
  technical_result: PASS
previous_human_acceptance:
  revision: DRAFT-R16
  human_decision: ACCEPT
latest_human_accepted_revision: DRAFT-R16
latest_acceptance_sidecar: AOS-3/development-package-state/R16_ACCEPTANCE_AND_DELIVERY.md
accepted_composite_sha256: 5ac5b606960fc4f533cdfe7ca3bc95c879c62a3d8f95d1bc10270a469a286a61
candidate_internal_state_role: HISTORICAL_SNAPSHOT
current_lifecycle_state_owner: AOS-3/development-package-state/CURRENT.md
portable_state: PORTABLE_UNBOUND
active_subject_registry: AOS-3/ACTIVE_SUBJECTS_R17.txt
root_payload_manifest: AOS-3/ROOT_FILES_MANIFEST.yaml
root_payload_target_class: GREENFIELD_OR_EMPTY_ROOT
root_materialization_authorization: SEPARATE_HUMAN_DECISION_REQUIRED
author_self_check_entrypoint: AOS-3/validation/validate_portable_package.py
DRAFT_R17_independent_validation: NOT_RUN
DRAFT_R17_human_acceptance: NOT_RUN
human_first_vertical_slice_selection: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
merge_authorization: NONE
release_authorization: NONE
active_blockers:
  - id: R17_INDEPENDENT_VALIDATION_NOT_RUN
    blocking_scope: R17_VALIDATION_AND_HUMAN_ACCEPTANCE_CLAIMS
  - id: R17_HUMAN_ACCEPTANCE_NOT_RUN
    blocking_scope: HUMAN_FIRST_VERTICAL_SLICE_SELECTION_FOR_R17_LIFECYCLE
  - id: HUMAN_FEATURE_SELECTION_NOT_RUN
    blocking_scope: FEATURE_CONTRACT_FINALIZATION_AND_TASK_DERIVATION
  - id: TARGET_REPOSITORY_BINDING_NOT_RUN
    blocking_scope: TARGET_BOUND_TASK_BRIEF_AND_PHYSICAL_IMPLEMENTATION_PLANNING
  - id: ROOT_MATERIALIZATION_AUTHORIZATION_NOT_GRANTED
    blocking_scope: TARGET_ROOT_PAYLOAD_MATERIALIZATION_ONLY
expected_human_gates:
  - R17_HUMAN_REVIEW_AND_DECISION_AFTER_INDEPENDENT_VALIDATION
  - FIRST_VERTICAL_SLICE_SELECTION_AFTER_R17_ACCEPTANCE
  - FEATURE_CONTRACT_DECISION
  - EXACT_TARGET_REPOSITORY_ASSIGNMENT
  - TASK_BRIEF_DECISION
  - RISK_PROFILE_ASSIGNMENT
  - IMPLEMENTATION_EXECUTION_AUTHORIZATION
  - ROOT_MATERIALIZATION_AUTHORIZATION_FOR_EXACT_TARGET
  - ANTIGRAVITY_ALWAYS_ON_WORKSPACE_VERIFICATION
  - SEPARATE_GIT_LIFECYCLE_DECISIONS
current_allowed_automatic_work:
  - READ_PACKAGE
  - RUN_PACKAGE_AUTHOR_SELF_CHECK
  - PREPARE_SEPARATE_READ_ONLY_R17_VALIDATION
  - PREPARE_UNFILLED_HUMAN_DECISION_CANDIDATES
one_next_action: RUN_SEPARATE_READ_ONLY_INDEPENDENT_VALIDATE_OVER_FROZEN_DRAFT_R17
```

## Acceptance partition

```yaml
acceptance_partition:
  r16_aggregate:
    identity: EXACT_R16_35_PATH_COMPOSITE_ONLY
    composite_content_aggregate_sha256: 5ac5b606960fc4f533cdfe7ca3bc95c879c62a3d8f95d1bc10270a469a286a61
    status: HUMAN_ACCEPTED_IN_DECLARED_SCOPE
    independent_validation: PASS
    human_acceptance: ACCEPT
  r17_aggregate:
    status: DRAFT
    independent_validation: NOT_RUN
    human_acceptance: NOT_RUN
  new_or_modified_r17_subjects:
    status: DRAFT
    acceptance_inheritance: FORBIDDEN
```

R16 остаётся exact human-accepted baseline. R17 не наследует acceptance или
validation `PASS`: его final bytes должны быть отдельно validated и представлены
человеку для exact decision.

## Readiness

```yaml
portable_package_candidate:
  status: DRAFT
root_payload_source:
  status: DRAFT
  target_repository_class: GREENFIELD_OR_EMPTY_ROOT
root_payload_materialization:
  technical_result: NOT_RUN
  reason: SEPARATE_TARGET_AUTHORIZATION_AND_PREFLIGHT_REQUIRED
antigravity_rule_activation:
  technical_result: NOT_RUN
  reason: HUMAN_WORKSPACE_VERIFICATION_REQUIRED
DRAFT_R17_independent_validation:
  technical_result: NOT_RUN
DRAFT_R17_human_acceptance:
  human_decision: NOT_RUN
human_feature_selection:
  technical_result: NOT_RUN
  readiness_state: NOT_READY
  reason: R17_HUMAN_ACCEPTANCE_NOT_RUN
feature_contract_readiness:
  readiness_state: NOT_APPLICABLE
  reason: HUMAN_FEATURE_SELECTION_NOT_RUN
portable_task_derivation:
  readiness_state: BLOCKED_BY_HUMAN_GATE
  reason: ACCEPTED_FEATURE_CONTRACT_REQUIRED
target_repository_assignment:
  technical_result: NOT_RUN
target_bound_task_brief:
  readiness_state: NOT_READY
  reason: TARGET_REPOSITORY_BINDING_NOT_RUN
implementation_planning:
  readiness_state: NOT_READY
execution_readiness:
  readiness_state: NOT_READY
```

DRAFT-R17 independent validation и human acceptance остаются `NOT_RUN`.
