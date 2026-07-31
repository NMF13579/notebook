---
artifact_id: AOS3-DPKG-DOC-007
artifact_type: IMPLEMENTATION_HANDOFF
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R12
status: DRAFT_R14_ROUTE_A_TRACE_CORRECTION_HANDOFF_READY_FOR_SEPARATE_VALIDATE
authority: PROPOSAL_AND_PORTABLE_ROUTING
exact_subject: Portable development order, contract acceptance gate, repository binding, Task compilation, checks, recovery, and transfer into a future AOS Core v1 implementation repository
created: '2026-07-30'
human_acceptance: C1_ACCEPTED_126_CURRENT_11_STALE_10_NEW_AC_AND_2_NEW_SCHEMA_DRAFT
provenance:
  - path: ../../docs/00_Core.md
    use: source precedence and human authority
  - path: ../../docs/03_Development.md
    use: PLAN through DELIVER workflow and Git boundaries
  - path: 00_Control_and_Source_Precedence.md
    use: package entrypoint and stage routing
  - path: 04_Runtime_and_Data_Contracts.md
    use: CTR-001 through CTR-007
  - path: 05_Quality_Recovery_and_Security.md
    use: acceptance, failures, recovery, and security checks
  - path: 06_Traceability_and_Readiness.md
    use: blockers, traceability, and post-C1 Task registry
  - path: decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
    use: exact C1 acceptance and accepted-subject manifest
  - path: decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
    use: package-local Task namespace and bounded correction authority
upstream_links:
  - 00_Control_and_Source_Precedence.md
  - 03_Architecture_and_Decisions.md
  - 04_Runtime_and_Data_Contracts.md
  - 05_Quality_Recovery_and_Security.md
  - 06_Traceability_and_Readiness.md
  - decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
downstream_links:
  - adapters/CODEX.md
  - tasks/TASK-TEMPLATE.md
  - tasks/TASK-GRAPH.md
  - tasks/AOS3-DPKG-TASK-001_Core_Scaffold.md
  - tasks/AOS3-DPKG-TASK-002_Local_Bootstrap.md
limitations:
  - Implementation repository is deliberately UNASSIGNED; repository creation is not authorized.
  - Exact repository baseline, paths, dependencies, and commands remain unresolved.
  - Task template, graph, and two Task Briefs are DRAFT candidates and are not human-accepted.
  - Corrected PSC-A-001, WFC-A-001, WFC-B-001, and WFC-C-001, seven stale WFC-A AC IDs, ten new WFC-B/C AC IDs, and two shared schemas are DRAFT and block only their dependent graph nodes.
  - BLK-006 prevents canonical TechnicalResult/ResultEnvelope conformance and readiness claims until a separate canonical decision.
  - This handoff does not authorize implementation or any Git action.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# 07 — Implementation Handoff

## 1. Current handoff state

```yaml
portable_core_contract_package: DRAFT_R14_ROUTE_A_TRACE_CORRECTION_CANDIDATE
logical_architecture: HUMAN_DECIDED
documentation_repository: NMF13579/notebook
repository_creation: DO_NOT_CREATE
implementation_repository: UNASSIGNED
contract_acceptance:
  current_accepted_subjects: 126
  stale_c1_subjects: [PSC-A-001, WFC-A-001, WFC-B-001, WFC-C-001, AC-WFC-A-001-01..07]
  new_draft_acceptance_ids: [AC-WFC-B-001-01..05, AC-WFC-C-001-01..05]
  new_draft_schema_ids: [SCH-PRODUCT-SPEC-001, SCH-FEATURE-PASSPORT-001]
accepted_subject_manifest_sha256: 2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
task_template: CREATED_DRAFT
task_graph: CREATED_DRAFT_SEVEN_NODES
task_briefs: [AOS3-DPKG-TASK-001, AOS3-DPKG-TASK-002]
materialized_task_projection_authority: EXISTING_TASK_BRIEF_DERIVED_FROM_FIELDS
materialized_forward_task_projection_invariant: MATERIALIZED_FORWARD_TASK_PROJECTION_EQUALS_INVERTED_TASK_BRIEF_REQUIREMENTS
materialized_reverse_task_projection_invariant: MATERIALIZED_REVERSE_TASK_PROJECTION_EQUALS_TASK_BRIEF_CONTRACTS
materialized_task_evidence_invariant: EVERY_MATERIALIZED_TASK_REQUIREMENT_CONTRACT_PATH_HAS_EXISTING_ACCEPTANCE_OR_SCENARIO_EVIDENCE
graph_only_task_ids: [AOS3-DPKG-TASK-003, AOS3-DPKG-TASK-004, AOS3-DPKG-TASK-005, AOS3-DPKG-TASK-006, AOS3-DPKG-TASK-007]
stale_or_draft_upstream_blocked_task_ids: [AOS3-DPKG-TASK-003, AOS3-DPKG-TASK-004, AOS3-DPKG-TASK-007]
human_task_acceptance: NOT_RUN
implementation: NOT_RUN
validation:
  DRAFT_R5: FAIL
  DRAFT_R6: FAIL
  DRAFT_R7: FAIL
  DRAFT_R8: FAIL
  DRAFT_R9: FAIL
  DRAFT_R10:
    overall: FAIL
    semantic: FAIL
    mechanical: UNKNOWN
  DRAFT_R11:
    overall: FAIL
    semantic: FAIL
    mechanical: UNKNOWN
  DRAFT_R12:
    overall: FAIL
    semantic: FAIL
    mechanical: UNKNOWN
  DRAFT_R13:
    overall: FAIL
    semantic: FAIL
    mechanical: UNKNOWN
  DRAFT_R14: NOT_RUN
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```

This document is a transfer contract, not a claim that transfer or implementation is currently permitted.

## 2. How a new agent resumes

1. Read [`00_Control_and_Source_Precedence.md`](00_Control_and_Source_Precedence.md).
2. Verify package revision, candidate digest from the latest stage report, and current repository facts.
3. Read only the owner needed for the current question:
   - product/scope: `01`;
   - workflows: `02`;
   - architecture/decisions: `03` and exact `DEC-ARCH-*`;
   - runtime/data: `04`;
   - quality/recovery/security: `05`;
   - traceability/readiness: `06`;
   - handoff/task routing: this document.
4. Treat canonical `../../docs/` as knowledge authority by fact class.
5. Treat `research/RSR-*` as exact reference Evidence with authority `NONE`.
6. Do not create a Task unless §5 returns `ELIGIBLE_FOR_PORTABLE_TASK_DRAFT` or `ELIGIBLE_FOR_REPOSITORY_BOUND_TASK_DRAFT`.
7. Perform one stage, produce one report, show one next action, and stop.

## 3. Portable package contents and ownership

| Artifact group | Purpose | Authority |
|---|---|---|
| `00..07` | Portable control and contract owners | Mixed; inspect each status |
| `decisions/DEC-PROD-*` | Exact G1 product decisions | Human decision in declared scope |
| `decisions/DEC-ARCH-*` | Exact G2 architecture decisions/ADRs | Human decision in declared scope |
| `decisions/DEC-CONTRACT-001*` | Exact C1 acceptance | Human decision for bound subject definitions only |
| `decisions/DEC-CORR-001*` | Package-local Task namespace and bounded DRAFT-R6/R7/R8 correction receipts | Human decision for exact subject and declared documentation grant only |
| `decisions/G2_*` | Historical option package | Proposal/Evidence of choice |
| `research/RSR-*` | Pinned reference findings | `NONE` |
| `adapters/CODEX.md` | Replaceable Codex routing | Adapter only; no portable-core authority |
| `tasks/TASK-TEMPLATE.md` | Portable Task schema | DRAFT proposal |
| `tasks/TASK-GRAPH.md` | Seven-node contract projection | DRAFT derived view |
| `tasks/AOS3-DPKG-TASK-001..002` | First bounded portable Task candidates | DRAFT; human Task acceptance NOT_RUN |

All documentation artifacts, including future portable Task candidates, are formed in `NMF13579/notebook`. A future implementation repository may receive a copy or export only after a separate exact repository and transfer-scope decision.

## 4. Deferred repository-binding contract

The current human decision is:

```yaml
documentation_repository: NMF13579/notebook
documentation_root: AOS-3/development-package/
repository_creation: DO_NOT_CREATE
implementation_repository: UNASSIGNED
```

Portable contract and Task documentation does not require a repository binding. Before any repository-bound enrichment, physical planning, preflight, implementation, or execution, a separate future human decision must identify the repository and authorize only the intended observation or mutation stage. Then record:

```yaml
repository_binding:
  decision_id: DEC-ARCH-001
  repository: exact OWNER/REPOSITORY
  local_root: observed path
  repository_role: AOS_CORE_V1_IMPLEMENTATION
  branch: observed branch
  head: exact commit or NO_COMMITS_YET
  remote: redacted identity
  worktree_state:
    staged: classified
    unstaged: classified
    untracked: classified
  nested_repositories: []
  symlink_boundaries: []
  supported_python: observed version
  dependency_policy: DEC-ARCH-003
  observed_at: RFC3339 UTC
  observation_result: PASS | BLOCKED | UNKNOWN
```

Rules:

- the human supplies the exact repository; an agent may only inspect it;
- repository creation, `git init`, clone, remote setup, branch changes, or role changes require separate authority;
- `NMF13579/notebook` remains the documentation/knowledge repository and cannot be inferred as the implementation repository;
- credential-bearing remote data is redacted;
- repository binding enriches a portable Task as a new exact revision; it does not rewrite the frozen portable candidate;
- a changed repository identity invalidates only repository-bound Task fields and downstream execution subjects.

## 5. Task compilation gate

### 5.1 Required inputs

```yaml
task_compilation_input:
  documentation_repository: NMF13579/notebook
  implementation_repository: UNASSIGNED or exact human-bound OWNER/REPOSITORY
  accepted_product_spec: exact ID/revision/hash only when the Task consumes a Product Spec instance; otherwise NOT_APPLICABLE
  accepted_feature_passport: exact ID/revision/hash only when the Task consumes a Feature Passport instance; otherwise NOT_APPLICABLE
  accepted_requirements: [REQ-*, ...]
  accepted_contracts: [PSC-* | WFC-* | CTR-*, ...]
  accepted_acceptance_ids: [AC-*, ...]
  accepted_scenarios: [SCN-*, ...]
  dependencies: [accepted/current IDs, ...]
  optional_capability_admission: none or exact human decision
  documentation_mutation_authorization: exact tasks/ path scope
```

### 5.2 Eligibility algorithm

```text
verify every upstream status and subject digest
→ reject DRAFT, stale, rejected, missing, or deferred-only source
→ when a Task consumes Product Spec or Feature Passport instances, require exact HUMAN_ACCEPTED bindings for those instances
→ resolve dependency graph and scope boundary
→ verify one user-visible bounded outcome
→ compile zero or one portable Task candidate
→ if repository is UNASSIGNED, keep physical paths/commands/dependencies/execution eligibility UNASSIGNED or BLOCKED
→ if repository is human-bound, verify exact current repository before enriching repository-bound fields
→ validate traceability and forbidden authority fields
→ request separate human Task review
→ stop
```

### 5.3 Results

```text
ELIGIBLE_FOR_PORTABLE_TASK_DRAFT
ELIGIBLE_FOR_REPOSITORY_BOUND_TASK_DRAFT
INELIGIBLE_DRAFT_UPSTREAM
INELIGIBLE_STALE_UPSTREAM
INELIGIBLE_REPOSITORY_BOUND_REQUEST_WITHOUT_BINDING
INELIGIBLE_BLOCKED_DEPENDENCY
INELIGIBLE_SCOPE_OR_OPTIONAL_ADMISSION
UNKNOWN_MATERIAL
```

Current DRAFT-R14 projection:

```yaml
result: TWO_CURRENT_INPUT_DRAFT_TASK_CANDIDATES_WITH_FIVE_GRAPH_ONLY_NODES
accepted_upstream_decision: DEC-CONTRACT-001
task_namespace_decision: DEC-CORR-001
repository_binding_state: PORTABLE_UNBOUND
task_artifact_files_created: 4
task_briefs_created: [AOS3-DPKG-TASK-001, AOS3-DPKG-TASK-002]
materialized_task_projection_authority: EXISTING_TASK_BRIEF_DERIVED_FROM_FIELDS
graph_only_task_ids: [AOS3-DPKG-TASK-003, AOS3-DPKG-TASK-004, AOS3-DPKG-TASK-005, AOS3-DPKG-TASK-006, AOS3-DPKG-TASK-007]
blocked_by_stale_or_unaccepted_upstream: [AOS3-DPKG-TASK-003, AOS3-DPKG-TASK-004, AOS3-DPKG-TASK-007]
human_task_acceptance: NOT_RUN
```

## 6. Task artifact boundary

The post-C1 Task template and every Task Brief must:

- contain one exact goal and observable user outcome;
- trace to accepted requirement/contract/acceptance/scenario IDs;
- declare `repository_binding_state: PORTABLE_UNBOUND | REPOSITORY_BOUND`;
- when portable/unbound, preserve `implementation_repository`, physical paths, commands, dependency versions, branch, and HEAD as `UNASSIGNED`;
- when repository-bound, bind repository/worktree/branch/HEAD/baseline in a new exact Task revision;
- declare logical allowed/forbidden scope and operations; physical paths require repository binding;
- declare dependencies, assumptions, unknowns, checks, negative cases, recovery, and stop conditions;
- show proposed Risk class but keep assigned Risk `UNASSIGNED` until human choice;
- exclude execution journal, implementation status, approval, and Git permissions;
- state `Task Brief ≠ Execution Authorization`.

The template, graph, and `AOS3-DPKG-TASK-001..002` are authored against this documentation boundary and await separate validation. Their physical fields remain `UNASSIGNED`, and no Task file grants acceptance, Risk, execution, validation, or Git authority. `AOS3-DPKG-TASK-003..007` are graph-only identities.

## 7. Prospective implementation order

The detailed graph is owned by [`tasks/TASK-GRAPH.md`](tasks/TASK-GRAPH.md). This sequence is routing, not implementation authorization:

```text
validate exact post-C1 package candidate
→ semantic review and human Task disposition
→ separate human Risk decision if a Task is accepted
→ future human implementation-repository decision
→ bind repository and enrich physical fields as a new Task revision
→ separate repository preflight
→ separate EXECUTE authorization
→ Stage Report and stop
→ separate VALIDATE
→ REVIEW and human result decision
→ separate Git decisions if requested
→ manual cycle Evidence
→ only then consider later RMP-005..008 Tasks
```

`CTR-001` scaffold work may precede Slice A implementation only after the repository/toolchain/dependency subject is exact. It cannot claim user-visible Slice A completion.

## 8. First-slice prospective transfer set

The prospective graph-only node `AOS3-DPKG-TASK-003` would reference:

- product facts and G1 decisions;
- `PSC-A-001`, `WFC-A-001`, and `CTR-003`;
- `SCH-PRODUCT-SPEC-001` and `SCH-FEATURE-PASSPORT-001`, the shared schemas needed to make owner-field checks deterministic;
- applicable scenarios `SCN-009..012`, `SCN-029`, `SCN-031`, `SCN-035`, `SCN-037`, and `SCN-039`;
- `DEC-ARCH-002..008`;
- `DEC-ARCH-001` R4 record with `implementation_repository: UNASSIGNED`;
- non-goals and optional capability exclusions;
- the selected adapter interface boundary.

No Task Brief may be materialized while `PSC-A-001`, `WFC-A-001`, and `AC-WFC-A-001-01..07` are C1-stale and the two shared schemas are DRAFT/unaccepted. After a new exact human acceptance decision and a separate Task-compilation authorization, a future portable Task candidate may be compiled; any later repository-bound successor would add exact repository binding without changing its accepted portable contract sources.

It should not import:

- AOS-FARM/AgentOS topology, milestones, stored readiness, or legacy risk labels;
- full `CTR-004..007` implementation scope into Slice A;
- optional RAG, routing, SaaS, plugin, domain, or Governance features;
- implementation/Git permission from this package.

## 9. Pre-execution checks

Before any implementation request can be decision-ready:

1. exact accepted Task and candidate digest;
2. repository root/worktree/branch/HEAD/baseline/status;
3. allowed/forbidden paths normalized;
4. dependency/interpreter provenance;
5. provider/network/data boundary;
6. symlink/nested-repository/path collision checks;
7. preview of operations and side effects;
8. assigned human Risk class;
9. exact Human Execution Authorization with grants/non-grants;
10. recovery and idempotency boundary;
11. Commit/Push/Merge/Release all `NONE`.

Any material mismatch blocks only the dependent action.

## 10. Stage report contract

Every later stage returns:

```yaml
task_id:
stage: PLAN | EXECUTE | VALIDATE | REVIEW
result: CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS
technical_result_vocabulary_status: BLOCKED_BLK_006
starting_identity:
ending_identity:
changed_paths: []
side_effects: []
checks_run: []
checks_not_run: []
findings: []
limitations: []
unknowns: []
out_of_scope_state: []
authorization_consumed: false | true | NOT_APPLICABLE
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: exactly one action
stop: true
```

## 11. Validation and review transfer

Correction authoring does not authorize a new Stage D. DRAFT-R6 through DRAFT-R12 each have a hash-bound Stage D `FAIL` recorded in the package history. DRAFT-R13 Stage D also returned `FAIL` for exact candidate `880dfdd3260beb19fa73078c9df50b84172ebbeec9719d62ad23b81c1407044c`: `VAL-R13-001` found no executable unknown-format Evidence for the projected `REQ-ARCH-009 → CTR-002 → Task-002` path, and `VAL-R13-002` found a non-derived materialized Task range in the `REQ-WF-006` forward Task cell. All results remain bound to their superseded exact candidates.

A separate read-only VALIDATE request must bind the final DRAFT-R14 candidate digest and verify the inventory, YAML, fences, links, IDs, RMP coverage, exact 83-row `TRC-REG-001` payload/hash/order/uniqueness, equality of the registry with both expanded requirement-contract projections, materialized-Task relation closure, materialized forward/reverse Task projection equality with existing Task Brief `derived_from` fields, graph-only projection separation, absence of a current `REQ-ARCH-009` contract/Task derivation, absence of a non-derived `REQ-WF-006` materialized Task entry, existing acceptance/scenario Evidence paths, contract field completeness, D1 decision-record conformance, A2 WFC acceptance ownership/mirror equality, unique YAML mapping keys, acceptance projection, negative scenarios, false-authority claims, Task gate, canonical-doc immutability, allowed paths, and zero validation mutations.

`PASS` from that validation would mean only that the declared technical checks passed. It would not accept contracts or authorize implementation/Git.

## 12. Completed human contract gate and future repository gate

The human completed C1 for the exact Stage C contract candidate:

```yaml
gate_id: HUMAN_CONTRACT_GATE_C1
candidate_binding: 00499af5d0f968481f0ed7e75c452bf74bf56eed380fd99d36a9a06dd8c54262
accepted_subject_manifest_sha256: 2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
accepted_requirement_ids: REQ-CV1-001..012, REQ-WF-001..010, REQ-ARCH-001..010
accepted_contract_ids: PSC-A-001, WFC-A-001, WFC-B-001, WFC-C-001, CTR-001..007
accepted_acceptance_ids: all 50 defined AC IDs
accepted_scenario_ids: SCN-001..044
human_disposition: ACCEPT
implementation_authorization: NONE
git_authorization: NONE
```

[`DEC-CONTRACT-001`](decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md) is the decision owner. It accepts no Task candidate and grants no repository, implementation, validation, or Git authority.

In DRAFT-R14, 126 unchanged subjects from the persisted C1 manifest remain current. The changed `PSC-A-001`, `WFC-A-001`, `WFC-B-001`, and `WFC-C-001` definitions and A2-owned `AC-WFC-A-001-01..07` definitions are not covered by their old accepted bytes. `AC-WFC-B-001-01..05`, `AC-WFC-C-001-01..05`, `SCH-PRODUCT-SPEC-001`, and `SCH-FEATURE-PASSPORT-001` are new DRAFT subjects. No Task Brief is materialized from those 23 stale or current DRAFT subjects.

Any later repository-dependent stage requires:

```yaml
gate_id: HUMAN_IMPLEMENTATION_REPOSITORY_BINDING_GATE_R1
portable_task_binding: exact accepted Task ID/revision/hash
exact_implementation_repository: actual OWNER/REPOSITORY
repository_observation_authorization: exact read-only subject
implementation_authorization: NONE
git_authorization: NONE
```

## 13. One next action

```yaml
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
