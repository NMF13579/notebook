---
artifact_id: AOS3-DPKG-ADAPTER-CODEX-001
artifact_type: AGENT_ENVIRONMENT_ADAPTER
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R12
status: DRAFT
authority: ADAPTER_ONLY
exact_subject: Thin Codex routing adapter for the portable AOS Core v1 documentation package
created: '2026-07-30'
human_acceptance: C1_ACCEPTED_126_CURRENT_11_STALE_10_NEW_AC_AND_2_NEW_SCHEMA_DRAFT
portable_core_entrypoint: ../00_Control_and_Source_Precedence.md
provenance:
  - ../00_Control_and_Source_Precedence.md
  - ../03_Architecture_and_Decisions.md
  - ../06_Traceability_and_Readiness.md
  - ../07_Implementation_Handoff.md
  - ../decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
upstream_links:
  - ../00_Control_and_Source_Precedence.md
  - ../03_Architecture_and_Decisions.md
  - ../06_Traceability_and_Readiness.md
  - ../07_Implementation_Handoff.md
  - ../decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
downstream_links: []
limitations:
  - Adapter instructions never override portable core, current system/developer instructions, repository instructions, or human decisions.
  - Model availability was not probed at runtime.
  - This adapter does not authorize subagents, Task acceptance, implementation, validation, or Git actions.
  - BLK-006 blocks canonical TechnicalResult/ResultEnvelope conformance and readiness claims.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# Codex Adapter

## 1. Entry and precedence

Start with [`../00_Control_and_Source_Precedence.md`](../00_Control_and_Source_Precedence.md). This file is replaceable routing glue. It must not own product, contract, decision, state, Evidence, or permission facts.

```text
current system/developer/repository instructions
→ exact human decision
→ portable core owner
→ this adapter
```

If this adapter conflicts with the portable core, report `CONFLICT` and stop only the affected action.

## 2. Current package state

```yaml
package_revision: DRAFT-R14
current_stage: CORRECTION_EXECUTE_DRAFT_R14_COMPLETED
traceability_registry:
  registry_id: TRC-REG-001
  owner: ../06_Traceability_and_Readiness.md
  row_count: 83
  payload_sha256: af15f5e0af1ca667136e1ffc2352e3acc7bf3cb5c037f62f558818889170aa69
  projection_invariant: FORWARD_EXPANSION_EQUALS_REGISTRY_EQUALS_INVERTED_REVERSE_EXPANSION
  task_projection_invariant: EVERY_MATERIALIZED_TASK_REQUIREMENT_HAS_AT_LEAST_ONE_RELATION_TO_A_DERIVED_CONTRACT_AND_EVERY_DERIVED_CONTRACT_HAS_AT_LEAST_ONE_RELATION_FROM_A_DERIVED_REQUIREMENT
materialized_task_projection:
  authority: EXISTING_TASK_BRIEF_DERIVED_FROM_FIELDS
  forward_invariant: MATERIALIZED_FORWARD_TASK_PROJECTION_EQUALS_INVERTED_TASK_BRIEF_REQUIREMENTS
  reverse_invariant: MATERIALIZED_REVERSE_TASK_PROJECTION_EQUALS_TASK_BRIEF_CONTRACTS
  evidence_invariant: EVERY_MATERIALIZED_TASK_REQUIREMENT_CONTRACT_PATH_HAS_EXISTING_ACCEPTANCE_OR_SCENARIO_EVIDENCE
  graph_only_projection_authority: AOS3-DPKG-TASK-GRAPH-001
contract_subjects:
  current_c1_accepted: 126
  stale_c1: [PSC-A-001, WFC-A-001, WFC-B-001, WFC-C-001, AC-WFC-A-001-01..07]
  new_draft_acceptance_ids: [AC-WFC-B-001-01..05, AC-WFC-C-001-01..05]
  new_draft_schema_ids: [SCH-PRODUCT-SPEC-001, SCH-FEATURE-PASSPORT-001]
accepted_subject_manifest_sha256: 2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
documentation_repository: NMF13579/notebook
repository_creation: DO_NOT_CREATE
implementation_repository: UNASSIGNED
task_files_created: 4
task_namespace: AOS3-DPKG-TASK-###
task_namespace_decision: DEC-CORR-001
task_briefs: [AOS3-DPKG-TASK-001, AOS3-DPKG-TASK-002]
task_graph_only_ids: [AOS3-DPKG-TASK-003, AOS3-DPKG-TASK-004, AOS3-DPKG-TASK-005, AOS3-DPKG-TASK-006, AOS3-DPKG-TASK-007]
stale_or_draft_upstream_blocked_task_ids: [AOS3-DPKG-TASK-003, AOS3-DPKG-TASK-004, AOS3-DPKG-TASK-007]
human_task_acceptance: NOT_RUN
independent_validation:
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
implementation_authorization: NONE
git_authorization: NONE
```

Form package documentation only in `NMF13579/notebook`. Do not infer that the current notebook path is an implementation repository. Until a separate future human binding, portable Task candidates may declare `implementation_repository: UNASSIGNED`, but repository-bound fields and execution remain blocked.

## 3. Primary writer

The primary Codex thread is `documentation_architect` and the only writer. It:

- reads the portable owners;
- applies exact authorized documentation mutations;
- reconciles evidence/conflicts;
- produces the stage report;
- never delegates writes or human decisions.

No spawned thread may write files, mutate Git, choose product/architecture, expand scope, retry a terminal result, or spawn another agent.

## 4. Read-only roles

Use a role only for a bounded independent read-only question, only when the current environment/instructions permit delegation, and with no more than two read-only subagents concurrently.

| Role | Route only | Mutation |
|---|---|---|
| `mechanical_checker` | inventory, counts, IDs, links, fences, manifests, checksums, structural comparisons | `NONE` |
| `reference_explorer` | exact repository/ref/commit/path research | `NONE` |
| `contract_analyst` | contract contradictions, failures, recovery, negative cases | `NONE` |
| `semantic_reviewer` | cross-document consistency, traceability, authority, false readiness | `NONE` |

`mechanical_checker` is statically bound to `gpt-5.6-luna` because `gpt-5.3-codex-spark` was absent from the configuration-time model catalog. This is a configuration binding, not an observed runtime fallback.

Codex Spark must not be declared active without a current availability check and an explicit new binding decision.

## 5. Request contract

Every delegated request must bind:

```yaml
task_id:
request_id:
parent_task_id:
task_class:
role:
exact_subject:
source_boundary:
  repository:
  ref:
  commit:
  paths: []
allowed_methods: []
forbidden_actions:
  - file mutation
  - Git mutation
  - human decision
  - scope expansion
  - terminal-result retry
required_output_fields:
  - task_id
  - request_id
  - parent_task_id
  - task_class
  - role
  - model
  - reasoning
  - exact_subject
  - source_boundary
  - sources
  - methods
  - classified_claims
  - conflicts
  - unknowns
  - recommendations
  - checks_run
  - checks_not_run
  - limitations
  - model_binding
  - repository_mutations
  - Git_operations
  - result
  - next_required_action
  - stop
stop_conditions: []
```

Allowed claim classes:

```text
OBSERVED_AT_SNAPSHOT
REPORTED
SYNTHESIZED
CONFLICT
NOT_FOUND
UNKNOWN
NOT_RUN
BLOCKED
```

## 6. Result admission

Before synthesis, the primary writer must:

1. verify the reported role/model binding;
2. verify repository/ref/commit/path provenance;
3. verify `repository_mutations: NONE`;
4. verify all Git operations are `NOT_RUN`;
5. classify conflicts with portable owners and other Evidence;
6. reject claims outside the source boundary;
7. preserve `UNKNOWN`, `NOT_FOUND`, and `NOT_RUN`;
8. use recommendations only as proposals.

Model consensus, a checker result, Evidence, or `PASS` cannot create human acceptance or authority.

Preserve `BLK-006_CANONICAL_STATUS_AXIS_CONFLICT`: do not normalize `HUMAN_REVIEW_REQUIRED` onto an unapproved axis and do not claim canonical ResultEnvelope/readiness conformance.

## 7. No fallback or retry

- no automatic runtime model fallback;
- no same-request retry after a terminal result;
- if the bound model is unavailable or materially insufficient, return `BLOCKED`;
- a replacement model requires a new explicit request and visible binding;
- failure never expands source paths, methods, network, or permissions.

## 8. Stage routing

```text
PLAN
→ exact Task/decision package
→ stop

EXECUTE
→ exact authorized documentation mutation
→ stage report
→ stop

VALIDATE
→ read-only exact frozen candidate
→ validation report
→ stop

REVIEW
→ semantic assessment and recommendation
→ human disposition
→ stop
```

Do not auto-advance between stages. Documentation correction is a new `EXECUTE`, not part of `VALIDATE` or `REVIEW`.

## 9. Git and implementation

```text
Documentation ≠ implementation
Task Brief ≠ Execution Authorization
PASS ≠ approval
Evidence ≠ approval
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Explicit read-only Git identity/status inspection is not a Git mutation. Commit, Push, Merge, Release, branch mutation, repository creation, remote configuration, implementation, dependency installation, and runtime execution remain `NOT_RUN` until separately authorized.

## 10. Adapter replacement test

The adapter is valid only if:

- removing/replacing it leaves `00..07`, decisions, contracts, scenarios, and traceability unchanged;
- it contains no product or architecture decision absent from portable owners;
- all links are repository-relative;
- it does not grant permissions;
- another agent environment can implement the same role/request/result contract without changing portable core.

## 11. One next action

```yaml
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
