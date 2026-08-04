---
artifact_id: AOS3-R15-TEMPLATE-TASK-BRIEF
artifact_type: TARGET_BOUND_TASK_BRIEF_TEMPLATE
package_revision: DRAFT-R15
revision: R1
status: DRAFT
authority: TEMPLATE_ONLY
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# Target-Bound Task Brief template

Task Brief — единственный scope owner для одной bounded target task. Он не
может выдавать себе authorization.

```yaml
task_id: ""
revision: ""
task_candidate_role: TARGET_BOUND_DRAFT
feature_or_slice_id: ""
feature_selection_decision_id: ""
feature_contract_identity: ""
feature_contract_human_decision: NOT_RUN
required_adrs: []
material_adrs_resolved: false
target_binding_id: ""
target_binding_state: TARGET_BOUND_FOR_PLANNING
target_binding_current: false
repository_identity: ""
branch: ""
HEAD: ""
baseline: ""
goal: ""
user_outcome: ""
stage: PLAN
scope:
  allowed_paths: []
  forbidden_paths: []
allowed_operations: []
forbidden_operations: []
dependencies: []
acceptance_matrix: []
negative_test_matrix: []
validation_commands: []
expected_results: []
recovery: []
rollback: []
stop_conditions: []
evidence_requirements: []
proposed_Risk_Profile: ""
assigned_Risk_Profile: UNASSIGNED
human_task_decision: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

## Readiness requirements

Each `acceptance_matrix` row maps one accepted contract ID to an executable
check and expected result. Each `negative_test_matrix` row contains a scenario
ID, fixture or command, expected result and expected write set.

The brief is not ready when:

- feature selection or exact accepted Feature Contract is absent;
- required ADR is unresolved;
- target binding is incomplete or stale;
- allowed/forbidden paths or operations are empty;
- acceptance or negative scenarios lack executable mapping;
- recovery or stop conditions are absent;
- a hidden product/architecture decision remains;
- human Task decision is `NOT_RUN`;
- assigned Risk Profile remains `UNASSIGNED`.

Even a ready, human-accepted Task Brief requires a separate
`IMPLEMENTATION_EXECUTION_AUTHORIZATION`.
