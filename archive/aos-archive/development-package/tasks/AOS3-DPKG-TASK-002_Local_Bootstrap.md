---
artifact_id: AOS3-DPKG-TASK-002
artifact_type: PORTABLE_TASK_BRIEF
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R6
status: DRAFT_TASK_CANDIDATE
authority: PROPOSAL_DERIVED_FROM_ACCEPTED_CONTRACTS
exact_subject: Bounded local bootstrap and first-start flow with preview/apply parity, managed ownership, interruption recovery, and one safe next action
created: '2026-07-30'
human_task_acceptance: NOT_RUN
accepted_upstream_decision: ../decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
repository_binding_state: PORTABLE_UNBOUND
provenance:
  - ../decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
  - ../decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
  - ../03_Architecture_and_Decisions.md
  - ../04_Runtime_and_Data_Contracts.md
  - ../05_Quality_Recovery_and_Security.md
  - ../06_Traceability_and_Readiness.md
  - TASK-TEMPLATE.md
  - TASK-GRAPH.md
  - AOS3-DPKG-TASK-001_Core_Scaffold.md
upstream_links:
  - ../decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
  - ../decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
  - ../03_Architecture_and_Decisions.md
  - ../04_Runtime_and_Data_Contracts.md
  - ../05_Quality_Recovery_and_Security.md
  - ../06_Traceability_and_Readiness.md
  - TASK-TEMPLATE.md
  - TASK-GRAPH.md
  - AOS3-DPKG-TASK-001_Core_Scaffold.md
limitations:
  - No implementation repository, package format, install root, commands, dependency versions, or executable checks are assigned.
  - The Task is not human-accepted and does not authorize preview, install, update, first-start execution, or Git mutation.
  - AOS3-DPKG-TASK-001 is a graph dependency but is not accepted, implemented, or validated.
  - The Task source binding is the accepted DRAFT-R4 contract candidate, not the mutable DRAFT-R14 package candidate.
  - "`REQ-ARCH-009` and `DEC-ARCH-008` remain a deferred compatibility boundary and are not part of this Task derivation."
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# AOS3-DPKG-TASK-002 — Local bootstrap and first start

## 1. Identity and accepted derivation

```yaml
task_id: AOS3-DPKG-TASK-002
revision: R6
status: DRAFT_TASK_CANDIDATE
candidate_binding:
  binding_role: ACCEPTED_UPSTREAM_CONTRACT_CANDIDATE
  package_revision: DRAFT-R4
  aggregate_sha256: 00499af5d0f968481f0ed7e75c452bf74bf56eed380fd99d36a9a06dd8c54262
  accepted_subject_manifest_sha256: 2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
accepted_subject_binding:
  decision_id: DEC-CONTRACT-001
  decision_revision: R5
  accepted_candidate_sha256: 00499af5d0f968481f0ed7e75c452bf74bf56eed380fd99d36a9a06dd8c54262
  accepted_subject_manifest_sha256: 2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
derived_from:
  requirements:
    - REQ-CV1-009
    - REQ-WF-004
    - REQ-WF-008
    - REQ-WF-010
    - REQ-ARCH-002
    - REQ-ARCH-003
  contracts:
    - CTR-002
  acceptance_ids:
    - AC-CTR-002-01..05
  scenarios:
    - SCN-005..008
    - SCN-036
    - SCN-038
  decisions:
    - DEC-ARCH-002
    - DEC-ARCH-003
graph_dependencies:
  - AOS3-DPKG-TASK-001
```

## 2. Outcome contract

```yaml
actor: local project owner assisted by a coding agent under future exact authorization
trigger: The owner later requests preview and application of one exact managed Core package.
observable_user_outcome: The user can preview an exact local bootstrap/update, apply only that preview under separate authority, and reach a first-start status showing exactly one safe next action.
completion_boundary:
  - preview and apply identities are comparable
  - managed and user-owned files are distinct
  - interruption produces durable recovery state
  - first start reports status, blockers, permissions, and one next action
  - no Slice A output, provider action, validation claim, or Git action occurs
non_goals:
  - repository creation or selection
  - automatic dependency installation
  - migration of unknown user-owned files
  - implementing Product Spec/Feature Passport generation
  - CI/CD, deployment, database, or optional capabilities
```

## 3. Repository binding

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
  package_format: UNASSIGNED
  commands: UNASSIGNED
  dependency_versions: UNASSIGNED
  executable_check_commands: UNASSIGNED
execution_eligibility: BLOCKED_REPOSITORY_BINDING
```

## 4. Logical scope

```yaml
allowed_logical_components:
  - managed package manifest and ownership records
  - preview/apply planner
  - local bootstrap/update coordinator
  - first-start status and one-next-action projection
  - interruption journal and reconciliation contract
allowed_contract_effects:
  - generate a no-write preview
  - compare future apply input with preview identity
  - under future authorization, apply only exact managed effects
  - report terminal success, failure, or recovery-required state
forbidden_capabilities:
  - hidden network/provider behavior
  - implicit migration of user-owned state
  - optional capability installation
forbidden_operations:
  - preview treated as execution authority
  - automatic retry after unknown outcome
  - implementation before exact EXECUTE authorization
  - Commit
  - Push
  - Merge
  - Release
```

## 5. Preconditions, inputs, outputs, and states

```yaml
preconditions:
  - DEC-CONTRACT-001 remains current
  - AOS3-DPKG-TASK-001 has a future accepted and repository-bound successor when physical execution is requested
  - managed package, target, baseline, preview subject, and ownership are exact
  - future write authorization binds the preview and operation set
inputs:
  - accepted CTR-002
  - future package/candidate manifest
  - future read-only target inventory
  - future preview digest and authorization
outputs:
  - preview manifest and expected effects
  - apply journal and actual effects
  - managed ownership record
  - first-start ResultEnvelope
  - recovery handoff when interrupted
states:
  initial: PORTABLE_UNBOUND
  future_ready: PREVIEW_READY
  terminal_success: FIRST_START_HUMAN_ACTION_REQUIRED
  terminal_blocked: BLOCKED_TARGET_OR_AUTHORITY
  terminal_failure: RECOVERY_REQUIRED
side_effects:
  documentation_phase: this Task Brief only
  implementation_phase: NOT_AUTHORIZED
```

## 6. Failure and recovery

| Failure | Detection | Required effect | Recovery |
|---|---|---|---|
| `BLOCKED_UNKNOWN_OWNERSHIP` | target path ownership cannot be proven | preserve file; zero affected write | human resolves ownership or changes scope |
| `BLOCKED_PREVIEW_MISMATCH` | package, target, path set, or effects differ from preview | zero writes | issue a new preview and authorization |
| `FAIL_INTERRUPTED_APPLY` | journal shows incomplete managed publication | stop; report actual state | reconcile managed/user state before new authorization |
| `BLOCKED_UNKNOWN_OPERATION_OUTCOME` | write acknowledgment is uncertain | no retry | inspect actual state and obtain recovery decision |
| `FAIL_SECRET_REDACTION` | result would expose credential-bearing remote data | reject durable result | redact and create corrected Evidence revision |

## 7. Acceptance and negative matrix

| Acceptance ID | Scenarios | Required Evidence | Proposed check state |
|---|---|---|---|
| `AC-CTR-002-01` | `SCN-005` | before/after digest proving preview changes zero bytes | `UNASSIGNED_PENDING_REPOSITORY` |
| `AC-CTR-002-02` | `SCN-005`, `SCN-006`, `SCN-036` | rejection and zero-write proof when preview, target identity, ownership, or safe path set changes | `UNASSIGNED_PENDING_REPOSITORY` |
| `AC-CTR-002-03` | `SCN-005`, `SCN-008` | two identical authorized applies converge on one managed state with no duplicate effects | `UNASSIGNED_PENDING_REPOSITORY` |
| `AC-CTR-002-04` | `SCN-007`, `SCN-008` | durable interruption journal, actual-effect inventory, and user-data preservation | `UNASSIGNED_PENDING_REPOSITORY` |
| `AC-CTR-002-05` | `SCN-005`, `SCN-038` | first-start one-action result with redacted provenance | `UNASSIGNED_PENDING_REPOSITORY` |

Mandatory negative outcomes:

- conflicting user-owned files remain unchanged;
- changed preview/input cannot apply;
- interruption or unknown outcome cannot retry automatically;
- first-start `PASS` or Evidence cannot grant Git authority.

## 8. Authority and stop

```yaml
human_task_acceptance: NOT_RUN
assigned_risk_action_class: UNASSIGNED
execution_authorization: NONE
validation_authorization: NONE
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
