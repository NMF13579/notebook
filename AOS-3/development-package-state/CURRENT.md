---
artifact_id: AOS3-DPKG-CURRENT-R16
artifact_type: CURRENT_STATE_POINTER
package_revision: DRAFT-R16
revision: R2
status: DRAFT
authority: ROUTING_AND_LIFECYCLE_STATE_ONLY
current_candidate_revision: DRAFT-R16
latest_human_accepted_revision: DRAFT-R14
latest_acceptance_sidecar: R14_ACCEPTANCE_AND_DELIVERY.md
candidate_internal_state_role: HISTORICAL_SNAPSHOT
current_lifecycle_state_owner: development-package-state/CURRENT.md
portable_state: PORTABLE_UNBOUND
active_subject_registry: ACTIVE_SUBJECTS_R16.txt
author_self_check_entrypoint: validation/validate_portable_package.py
independent_validation: NOT_RUN
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# Current package state

Это единственный current-state pointer. Он маршрутизирует к fact owners, но не
заменяет их и не создаёт acceptance или permission.

```yaml
current_candidate_revision: DRAFT-R16
working_baseline_revision: DRAFT-R15
working_baseline_disposition: USE_AS_EXACT_WORKING_BASELINE
previous_independent_validation:
  revision: DRAFT-R15
  technical_result: PASS
latest_human_accepted_revision: DRAFT-R14
latest_acceptance_sidecar: AOS-3/development-package-state/R14_ACCEPTANCE_AND_DELIVERY.md
candidate_internal_state_role: HISTORICAL_SNAPSHOT
current_lifecycle_state_owner: AOS-3/development-package-state/CURRENT.md
portable_state: PORTABLE_UNBOUND
active_subject_registry: AOS-3/ACTIVE_SUBJECTS_R16.txt
root_payload_manifest: AOS-3/ROOT_FILES_MANIFEST.yaml
root_payload_target_class: GREENFIELD_OR_EMPTY_ROOT
root_materialization_authorization: SEPARATE_HUMAN_DECISION_REQUIRED
author_self_check_entrypoint: AOS-3/validation/validate_portable_package.py
DRAFT_R16_independent_validation: NOT_RUN
DRAFT_R16_human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
active_blockers:
  - id: HUMAN_FEATURE_SELECTION_NOT_RUN
    blocking_scope: FEATURE_CONTRACT_FINALIZATION_AND_TASK_DERIVATION
  - id: TARGET_REPOSITORY_BINDING_NOT_RUN
    blocking_scope: TARGET_BOUND_TASK_BRIEF_AND_IMPLEMENTATION_PLANNING
  - id: ROOT_MATERIALIZATION_AUTHORIZATION_NOT_GRANTED
    blocking_scope: TARGET_ROOT_PAYLOAD_MATERIALIZATION_ONLY
  - id: R16_INDEPENDENT_VALIDATION_NOT_RUN
    blocking_scope: R16_VALIDATION_AND_HUMAN_ACCEPTANCE_CLAIMS
expected_human_gates:
  - ROOT_MATERIALIZATION_AUTHORIZATION_FOR_EXACT_TARGET
  - ANTIGRAVITY_ALWAYS_ON_WORKSPACE_VERIFICATION
  - FIRST_VERTICAL_SLICE_SELECTION
  - FEATURE_CONTRACT_DECISION
  - TASK_BRIEF_DECISION
  - RISK_PROFILE_ASSIGNMENT
  - IMPLEMENTATION_EXECUTION_AUTHORIZATION
  - SEPARATE_GIT_LIFECYCLE_DECISIONS
current_allowed_automatic_work:
  - READ_PACKAGE
  - READ_ROOT_MATERIALIZATION_CONTRACT
  - RUN_PACKAGE_AUTHOR_SELF_CHECK
  - READ_ONLY_TARGET_REPOSITORY_PREFLIGHT_AFTER_COPY
  - PREPARE_UNFILLED_HUMAN_DECISION_CANDIDATES
one_next_action: RUN_SEPARATE_READ_ONLY_INDEPENDENT_VALIDATE_OVER_FROZEN_DRAFT_R16
```

## Acceptance partition

```yaml
acceptance_partition:
  r14_aggregate:
    identity: EXACT_R14_AGGREGATE_ONLY
    aggregate_sha256: 6f5ee03c0c32787d47f9132e0eaa280bc6e6d5cfd42519814db78f4b4f725493
    status: HUMAN_ACCEPTED_IN_DECLARED_SCOPE
  r15_working_baseline:
    active_content_sha256: 74e2e54078fa36e8c5913c4ed3e254a795461e05df6b47243d13b25a0544dfc8
    full_candidate_sha256: 93475ec3f8c5613663251306474da28fe934a81c494657b182087b70c8378256
    full_candidate_path_count: 24
    independent_validation: PASS
    disposition: USE_AS_EXACT_WORKING_BASELINE
    acceptance_effect: NONE
  r16_aggregate:
    status: DRAFT
    independent_validation: NOT_RUN
    human_acceptance: NOT_RUN
  new_or_modified_r16_subjects:
    status: DRAFT
    acceptance_inheritance: FORBIDDEN
```

R15 working-baseline disposition не является acceptance. R15-named Evidence
сохраняется как historical candidate Evidence. R16 не наследует acceptance от
R14 или validation `PASS` от R15.

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
full_target_repository_preflight:
  technical_result: NOT_RUN
human_feature_selection:
  technical_result: NOT_RUN
feature_contract_readiness:
  readiness_state: NOT_APPLICABLE
  reason: HUMAN_FEATURE_SELECTION_NOT_RUN
task_derivation:
  readiness_state: BLOCKED_BY_HUMAN_GATE
  reason: FIRST_VERTICAL_SLICE_SELECTION_REQUIRED
implementation_planning:
  readiness_state: NOT_READY
execution_readiness:
  readiness_state: NOT_READY
```

DRAFT-R16 independent validation и human acceptance остаются `NOT_RUN`.
