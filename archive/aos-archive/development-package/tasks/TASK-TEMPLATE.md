---
artifact_id: AOS3-DPKG-TPL-TASK-001
artifact_type: PORTABLE_TASK_BRIEF_TEMPLATE
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R3
status: DRAFT
authority: PROPOSAL
exact_subject: Portable schema for one bounded Task Brief derived only from accepted requirement, contract, acceptance, and scenario IDs
created: '2026-07-30'
human_acceptance: NOT_RUN
provenance:
  - ../00_Control_and_Source_Precedence.md
  - ../04_Runtime_and_Data_Contracts.md
  - ../05_Quality_Recovery_and_Security.md
  - ../06_Traceability_and_Readiness.md
  - ../07_Implementation_Handoff.md
  - ../decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
  - ../decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
upstream_links:
  - ../00_Control_and_Source_Precedence.md
  - ../04_Runtime_and_Data_Contracts.md
  - ../05_Quality_Recovery_and_Security.md
  - ../06_Traceability_and_Readiness.md
  - ../07_Implementation_Handoff.md
  - ../decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
  - ../decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
downstream_links:
  - TASK-GRAPH.md
  - AOS3-DPKG-TASK-001_Core_Scaffold.md
  - AOS3-DPKG-TASK-002_Local_Bootstrap.md
limitations:
  - A Task Brief created from this template is documentation and not execution authorization.
  - Package-local Task IDs use AOS3-DPKG-TASK-### and do not populate Roadmap TASK-### identities or task_refs.
  - PORTABLE_UNBOUND Tasks cannot name physical implementation paths, commands, branch, HEAD, dependencies, or executable checks as current facts.
  - Repository binding, Task acceptance, Risk assignment, EXECUTE, VALIDATE, and every Git action remain separate decisions.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# TASK-TEMPLATE — Portable bounded Task Brief

## 1. Frontmatter contract

```yaml
artifact_id: AOS3-DPKG-TASK-###
artifact_type: PORTABLE_TASK_BRIEF
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: exact current package revision
revision: R1
status: DRAFT_TASK_CANDIDATE
authority: PROPOSAL_DERIVED_FROM_ACCEPTED_CONTRACTS
exact_subject: one bounded outcome
created: YYYY-MM-DD
human_task_acceptance: NOT_RUN
accepted_upstream_decision: ../decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
repository_binding_state: PORTABLE_UNBOUND | REPOSITORY_BOUND
implementation_repository: UNASSIGNED or exact human-bound OWNER/REPOSITORY
implementation_authorization: NONE
git_authorization: NONE
```

## 2. Identity and derivation

Every Task must declare:

```yaml
task:
  id: AOS3-DPKG-TASK-###
  revision: R1
  status: DRAFT_TASK_CANDIDATE
  exact_subject:
  candidate_binding:
    binding_role: ACCEPTED_UPSTREAM_CONTRACT_CANDIDATE
    package_revision:
    aggregate_sha256:
    accepted_subject_manifest_sha256:
  accepted_subject_binding:
    decision_id: DEC-CONTRACT-001
    decision_revision:
    accepted_candidate_sha256:
    accepted_subject_manifest_sha256:
  derived_from:
    requirements: []
    contracts: []
    acceptance_ids: []
    scenarios: []
    decisions: []
  graph_dependencies: []
```

Rules:

- the top-level `package_revision` records Task membership in the current package candidate;
- `candidate_binding` binds the frozen accepted upstream contract candidate and must never self-bind to the mutable Task-containing package revision;
- every `REQ`, contract, `AC`, and `SCN` must appear in the exact accepted C1 scope;
- derived Task prose cannot widen an accepted source;
- deferred/optional dossiers cannot become Task input without a separate human admission decision;
- one `AOS3-DPKG-TASK-###` ID owns one exact package-local outcome and is never reused for a different subject;
- Roadmap `TASK-###` IDs remain owned by `AOS-3/AOS_Core_Roadmap.md` and are never inferred from this package.

## 3. Outcome contract

```yaml
outcome:
  actor:
  trigger:
  observable_user_outcome:
  completion_boundary:
  non_goals: []
```

The outcome must be externally observable or deterministically inspectable. “Implement the system,” “make it work,” and milestone-only wording are invalid.

## 4. Repository-binding state

### `PORTABLE_UNBOUND`

```yaml
repository:
  binding_state: PORTABLE_UNBOUND
  implementation_repository: UNASSIGNED
  local_root: UNASSIGNED
  branch: UNASSIGNED
  head: UNASSIGNED
  baseline: UNASSIGNED
  physical_allowed_paths: UNASSIGNED
  physical_forbidden_paths: UNASSIGNED
  commands: UNASSIGNED
  dependency_versions: UNASSIGNED
  executable_check_commands: UNASSIGNED
execution_eligibility: BLOCKED_REPOSITORY_BINDING
```

An unbound Task may specify logical components, contracts, operations, invariants, and required checks. It must not disguise proposals as observed repository facts.

### `REPOSITORY_BOUND`

A new Task revision may replace `UNASSIGNED` fields only after `HUMAN_IMPLEMENTATION_REPOSITORY_BINDING_GATE_R1`, fresh read-only observation, and exact subject-hash comparison. The portable revision remains immutable Evidence.

## 5. Logical scope

```yaml
scope:
  allowed_logical_components: []
  allowed_contract_effects: []
  forbidden_capabilities: []
  forbidden_operations:
    - implementation before exact EXECUTE authorization
    - dependency installation before exact authorization
    - provider or network use outside accepted local-only boundary
    - canonical docs mutation unless explicitly included
    - Commit
    - Push
    - Merge
    - Release
```

## 6. Preconditions, inputs, outputs, and state

```yaml
preconditions: []
inputs: []
outputs: []
states:
  initial:
  terminal_success:
  terminal_blocked:
side_effects:
  documentation_phase: exact Task artifact only
  implementation_phase: NOT_AUTHORIZED
```

## 7. Authority and Risk boundary

```yaml
authority:
  task_documentation_authority: exact bounded path
  human_task_acceptance: NOT_RUN
  assigned_risk_action_class: UNASSIGNED
  execution_authorization: NONE
  validation_authorization: NONE
  git_authorization: NONE
```

`Task Brief ≠ Task acceptance ≠ Risk assignment ≠ Execution Authorization ≠ Git authority`.

## 8. Failure and recovery

```yaml
failures:
  - code:
    detection:
    effect:
recovery:
  - preserve exact subject and actual Evidence
  - change no frozen source in VALIDATE
  - request one bounded human decision for a material blocker
  - create a new revision rather than rewriting accepted or failed Evidence
```

## 9. Acceptance and negative cases

```yaml
acceptance_matrix:
  - acceptance_id:
    scenario_ids: []
    required_evidence:
    proposed_check:
negative_cases:
  - scenario_id:
    prohibited_outcome:
```

An unbound Task describes proposed checks but keeps executable commands `UNASSIGNED`.

## 10. Stage and stop contract

```yaml
stage_contract:
  current_stage: DOCUMENTATION_TASK_COMPILATION
  implementation: NOT_RUN
  validation: NOT_RUN
  Git_operations:
    commit: NOT_RUN
    push: NOT_RUN
    merge: NOT_RUN
    release: NOT_RUN
  next_required_action: exactly one bounded action
  stop: true
```
