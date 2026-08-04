---
artifact_id: AOS3-R15-TEMPLATE-PORTABLE-TASK-CANDIDATE
artifact_type: PORTABLE_TASK_CANDIDATE_TEMPLATE
package_revision: DRAFT-R15
revision: R1
status: DRAFT
authority: TEMPLATE_ONLY
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# Portable Task Candidate template

Этот candidate описывает outcome и logical scope до target binding. Он не
содержит guessed repository facts.

```yaml
task_id: ""
revision: ""
task_class: ""
feature_or_slice_id: ""
feature_contract_identity: ""
goal: ""
user_outcome: ""
stage: PLAN
contract_dependencies: []
architecture_dependencies: []
scope_intent: ""
non_goals: []
acceptance_ids: []
negative_scenario_ids: []
assumptions: []
unknowns: []
stop_conditions: []
binding_state: PORTABLE_UNBOUND
task_candidate_role: DRAFT_PORTABLE_CANDIDATE
human_acceptance: NOT_RUN
assigned_Risk_Profile: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
```

Forbidden while `binding_state: PORTABLE_UNBOUND`:

- repository paths, repository identity, branch, HEAD or baseline;
- dependency or toolchain versions;
- executable target commands or rollback commands;
- assigned Risk Profile;
- human acceptance or execution authority.

The candidate may identify logical dependencies and required evidence. It
becomes neither a Target-Bound Task Brief nor an Execution Authorization by
adding target facts.
