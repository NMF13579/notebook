---
artifact_id: AOS3-DPKG-TASK-001
artifact_type: PORTABLE_TASK_BRIEF
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R5
status: DRAFT_TASK_CANDIDATE
authority: PROPOSAL_DERIVED_FROM_ACCEPTED_CONTRACTS
exact_subject: Bounded Core v1 scaffold candidate with exact manifest, ownership, zero-hidden-file behavior, and fail-closed repository binding
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
upstream_links:
  - ../decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
  - ../decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
  - ../03_Architecture_and_Decisions.md
  - ../04_Runtime_and_Data_Contracts.md
  - ../05_Quality_Recovery_and_Security.md
  - ../06_Traceability_and_Readiness.md
  - TASK-TEMPLATE.md
  - TASK-GRAPH.md
downstream_links:
  - AOS3-DPKG-TASK-002_Local_Bootstrap.md
limitations:
  - No implementation repository, paths, commands, dependency versions, OS matrix, or executable checks are assigned.
  - The Task is not human-accepted and cannot authorize scaffold creation or any repository/Git mutation.
  - Exact physical topology requires a future repository-bound revision.
  - The Task source binding is the accepted DRAFT-R4 contract candidate, not the mutable DRAFT-R14 package candidate.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# AOS3-DPKG-TASK-001 — Core scaffold

## 1. Identity and accepted derivation

```yaml
task_id: AOS3-DPKG-TASK-001
revision: R5
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
    - REQ-CV1-012
    - REQ-WF-004
    - REQ-ARCH-002
    - REQ-ARCH-003
    - REQ-ARCH-010
  contracts:
    - CTR-001
  acceptance_ids:
    - AC-CTR-001-01..04
  scenarios:
    - SCN-001..004
    - SCN-036
  decisions:
    - DEC-ARCH-001
    - DEC-ARCH-002
    - DEC-ARCH-003
graph_dependencies: []
```

## 2. Outcome contract

```yaml
actor: coding agent under a future exact execution authorization
trigger: A human later binds an implementation repository and requests the Core scaffold subject.
observable_user_outcome: The selected empty or compatible target can receive one exact, inspectable Core scaffold candidate with declared ownership and no hidden files or authority.
completion_boundary:
  - exact candidate manifest exists
  - every proposed path has an owner and purpose
  - supported interpreter/dependency assumptions are explicit
  - self-test requirements and zero-write negative behavior are specified
  - no bootstrap, product flow, execution, validation, or Git claim is included
non_goals:
  - creating or selecting a repository
  - installing dependencies
  - implementing bootstrap or Slice A
  - CI/CD, deployment, database, provider, or optional capabilities
  - Commit, Push, Merge, or Release
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
  commands: UNASSIGNED
  dependency_versions: UNASSIGNED
  executable_check_commands: UNASSIGNED
execution_eligibility: BLOCKED_REPOSITORY_BINDING
```

`NMF13579/notebook` is the documentation repository and is forbidden as an inferred implementation target.

## 4. Logical scope

```yaml
allowed_logical_components:
  - package boundary for portable core
  - local adapter boundary
  - artifact, digest, manifest, authority, and ResultEnvelope primitives required by CTR-001
  - deterministic scaffold candidate generation and ownership metadata
allowed_contract_effects:
  - preview an exact candidate
  - under future authorization, create only manifest-listed paths
  - run future repository-bound self-tests
forbidden_capabilities:
  - product runtime beyond scaffold
  - external provider/network use
  - optional feature dossiers
forbidden_operations:
  - repository creation
  - implementation before exact EXECUTE authorization
  - dependency installation before exact authorization
  - canonical docs mutation
  - Commit
  - Push
  - Merge
  - Release
```

## 5. Preconditions, inputs, outputs, and states

```yaml
preconditions:
  - DEC-CONTRACT-001 remains current for every derived ID
  - a future human repository-binding decision identifies one exact target
  - target preflight establishes ownership, baseline, collisions, symlinks, nested repositories, and supported Python
  - a future Task revision binds physical paths and proposed checks
inputs:
  - accepted CTR-001 and architecture requirements
  - future exact repository observation
  - future exact dependency/toolchain decision
  - future allowed/forbidden physical path set
outputs:
  - candidate scaffold manifest
  - owner/purpose map
  - before/after or zero-write Evidence contract
  - self-test result contract
  - one terminal ResultEnvelope
states:
  initial: PORTABLE_UNBOUND
  future_ready: REPOSITORY_BOUND_PREFLIGHTED
  terminal_success: SCAFFOLD_CANDIDATE_MATERIALIZED_UNVALIDATED
  terminal_blocked: BLOCKED_REPOSITORY_OR_PREFLIGHT
side_effects:
  documentation_phase: this Task Brief only
  implementation_phase: NOT_AUTHORIZED
```

## 6. Failure and recovery

| Failure | Detection | Required effect | Recovery |
|---|---|---|---|
| `BLOCKED_UNASSIGNED_REPOSITORY` | repository binding is absent or points to `notebook` | zero target writes | obtain a separate exact human binding |
| `BLOCKED_UNSUPPORTED_PYTHON` | observed interpreter is outside accepted toolchain class | zero writes | human decides toolchain/repository change |
| `BLOCKED_DIRTY_OR_WRONG_SUBJECT` | baseline/status differs from future Task binding | zero writes | rebaseline and issue a new Task revision |
| `FAIL_MANIFEST_DRIFT` | actual path/effect differs from candidate manifest | stop; classify actual state | preserve Evidence; reconcile before any retry |
| `FAIL_PARTIAL_SCAFFOLD_WRITE` | interruption leaves a subset of intended paths | no automatic retry | inventory actual paths and require recovery authorization |

## 7. Acceptance and negative matrix

| Acceptance ID | Scenarios | Required Evidence | Proposed check state |
|---|---|---|---|
| `AC-CTR-001-01` | `SCN-001` | exact target/interpreter binding | `UNASSIGNED_PENDING_REPOSITORY` |
| `AC-CTR-001-02` | `SCN-001`, `SCN-004` | declared inputs, reproducible clean scaffold, and repeatable self-test result | `UNASSIGNED_PENDING_REPOSITORY` |
| `AC-CTR-001-03` | `SCN-002`, `SCN-036` | before/after digest proving help and doctor read-only modes write zero source bytes | `UNASSIGNED_PENDING_REPOSITORY` |
| `AC-CTR-001-04` | `SCN-001`, `SCN-003`, `SCN-004` | result vocabulary scan proving no Product Runtime or implementation-readiness claim | `UNASSIGNED_PENDING_REPOSITORY` |

Mandatory negative outcomes:

- `SCN-002`: `UNASSIGNED`, placeholder, or documentation-only `notebook` target produces zero writes;
- `SCN-036`: traversal, symlink, normalized-path collision, or nested-repository escape fails closed;
- Task, Evidence, or self-test result never grants implementation or Git authority.

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
