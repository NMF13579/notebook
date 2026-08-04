---
artifact_id: AOS3-DPKG-TASK-GRAPH-001
artifact_type: PORTABLE_BOUNDED_TASK_GRAPH
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R5
status: DRAFT_DERIVED_VIEW
authority: PROPOSAL_DERIVED_FROM_MIXED_ACCEPTANCE_STATE
exact_subject: Seven-node package-local Core v1 Task dependency graph with current acceptance and staleness projection
created: '2026-07-30'
human_task_graph_acceptance: NOT_RUN
provenance:
  - ../00_Control_and_Source_Precedence.md
  - ../06_Traceability_and_Readiness.md
  - ../07_Implementation_Handoff.md
  - ../decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
  - ../decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
upstream_links:
  - ../decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
  - ../decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
  - ../04_Runtime_and_Data_Contracts.md
  - ../05_Quality_Recovery_and_Security.md
  - ../06_Traceability_and_Readiness.md
  - ../07_Implementation_Handoff.md
  - TASK-TEMPLATE.md
downstream_links:
  - AOS3-DPKG-TASK-001_Core_Scaffold.md
  - AOS3-DPKG-TASK-002_Local_Bootstrap.md
limitations:
  - The graph is a DRAFT dependency projection and has no activation, scheduling, implementation, or Git authority.
  - AOS3-DPKG-TASK-003 through AOS3-DPKG-TASK-007 are graph-only planned IDs; no Task Brief exists for them in this revision.
  - PSC-A-001, WFC-A-001, WFC-B-001, WFC-C-001, and AC-WFC-A-001-01..07 changed after C1 and are stale against DEC-CONTRACT-001; their dependent graph nodes remain blocked.
  - SCH-PRODUCT-SPEC-001 and SCH-FEATURE-PASSPORT-001 are new DRAFT subjects and additionally block AOS3-DPKG-TASK-003.
  - Every node is PORTABLE_UNBOUND because implementation_repository is UNASSIGNED.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# TASK-GRAPH — Core v1 portable dependency graph

## 1. Graph state

```yaml
graph_id: AOS3-DPKG-TASK-GRAPH-001
revision: R5
status: DRAFT_DERIVED_VIEW
accepted_upstream_decision: DEC-CONTRACT-001
accepted_candidate_sha256: 00499af5d0f968481f0ed7e75c452bf74bf56eed380fd99d36a9a06dd8c54262
accepted_subject_manifest_sha256: 2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
task_namespace_decision: DEC-CORR-001
task_namespace: AOS3-DPKG-TASK-###
repository_binding_state: PORTABLE_UNBOUND
implementation_repository: UNASSIGNED
materialized_task_briefs: [AOS3-DPKG-TASK-001, AOS3-DPKG-TASK-002]
graph_only_task_ids: [AOS3-DPKG-TASK-003, AOS3-DPKG-TASK-004, AOS3-DPKG-TASK-005, AOS3-DPKG-TASK-006, AOS3-DPKG-TASK-007]
human_task_graph_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

## 2. Nodes

| Task ID | Exact bounded outcome | Primary contract projection | Dependency | Brief state | Execution state |
|---|---|---|---|---|---|
| `AOS3-DPKG-TASK-001` | Exact candidate scaffold can be planned and later materialized without hidden files or authority | `CTR-001` | none in graph; future repository binding required | `DRAFT_TASK_CANDIDATE` | `BLOCKED_REPOSITORY_BINDING` |
| `AOS3-DPKG-TASK-002` | An exact managed local package can preview/apply bootstrap and show one first-start action | `CTR-002` | `AOS3-DPKG-TASK-001` | `DRAFT_TASK_CANDIDATE` | `BLOCKED_REPOSITORY_BINDING` |
| `AOS3-DPKG-TASK-003` | User intent becomes a reviewable DRAFT Product Spec and Feature Passport with one decision request | accepted `CTR-003`; changed `PSC-A-001`, `WFC-A-001`, and `AC-WFC-A-001-01..07` are `STALE`/`DRAFT`; `SCH-PRODUCT-SPEC-001`/`SCH-FEATURE-PASSPORT-001` are `DRAFT` | new exact acceptance of PSC-A-001, WFC-A-001, its seven A2-owned AC definitions, and schemas; `AOS3-DPKG-TASK-002` for future physical execution | `GRAPH_ONLY` | `BLOCKED_STALE_PSC_WFC_AC_AND_DRAFT_SCHEMAS` |
| `AOS3-DPKG-TASK-004` | Accepted product subjects compile into one bounded portable Task and derived Queue | `CTR-004`; changed `WFC-B-001` and new `AC-WFC-B-001-01..05` are `STALE`/`DRAFT` | `AOS3-DPKG-TASK-003` plus new acceptance of WFC-B-001 and its AC definitions | `GRAPH_ONLY` | `BLOCKED_STALE_UNACCEPTED_WFC_AC` |
| `AOS3-DPKG-TASK-005` | One accepted Task executes only under exact human authorization and bounded effects | `CTR-005` | `AOS3-DPKG-TASK-004` plus future repository binding | `GRAPH_ONLY` | `BLOCKED_DEPENDENCY_AND_NO_BRIEF` |
| `AOS3-DPKG-TASK-006` | An exact frozen candidate receives read-only validation Evidence and human review routing | `CTR-006` | `AOS3-DPKG-TASK-005` | `GRAPH_ONLY` | `BLOCKED_DEPENDENCY_AND_NO_BRIEF` |
| `AOS3-DPKG-TASK-007` | A new agent resumes from Project Memory, detects stale state, and returns one safe next action | `CTR-007`; changed `WFC-C-001` and new `AC-WFC-C-001-01..05` are `STALE`/`DRAFT` | `AOS3-DPKG-TASK-003` plus new acceptance of WFC-C-001 and its AC definitions | `GRAPH_ONLY` | `BLOCKED_STALE_UNACCEPTED_WFC_AC` |

One accepted `CTR-*` owns one primary graph node. Cross-contract dependencies do not create duplicate owners.

## 3. Dependency views

### First implementation path after future repository binding

```text
AOS3-DPKG-TASK-001 scaffold
→ AOS3-DPKG-TASK-002 bootstrap
→ new human acceptance of corrected PSC-A-001, WFC-A-001, AC-WFC-A-001-01..07, and shared schemas
→ separate Task-compilation authorization
→ AOS3-DPKG-TASK-003 Slice A
→ human review of observable Slice A outcome
```

### Later controlled-development path

```text
AOS3-DPKG-TASK-003 accepted product output
→ new human acceptance of corrected WFC-B-001 and AC-WFC-B-001-01..05
→ AOS3-DPKG-TASK-004 portable Task/Queue
→ future repository binding and Task revision
→ AOS3-DPKG-TASK-005 bounded execution
→ AOS3-DPKG-TASK-006 read-only validation/review
→ new human acceptance of corrected WFC-C-001 and AC-WFC-C-001-01..05
→ AOS3-DPKG-TASK-007 safe resume and recovery projection
```

The arrows express contract dependency, not automatic activation.

## 4. Coverage

| Roadmap item | Task node | Contract coverage |
|---|---|---|
| `RMP-002` | `AOS3-DPKG-TASK-001` | `CTR-001` |
| `RMP-003` | `AOS3-DPKG-TASK-002` | `CTR-002` |
| `RMP-004` | `AOS3-DPKG-TASK-003` | accepted `CTR-003`; changed `PSC-A-001`, `WFC-A-001`, stale `AC-WFC-A-001-01..07`, and new shared schemas `STALE`/`DRAFT` |
| `RMP-005` | `AOS3-DPKG-TASK-004` | changed `WFC-B-001` and new `AC-WFC-B-001-01..05` (`STALE`/`DRAFT`), accepted `CTR-004` |
| `RMP-006` | `AOS3-DPKG-TASK-005` | `CTR-005` |
| `RMP-007` | `AOS3-DPKG-TASK-006` | `CTR-006` |
| `RMP-008` | `AOS3-DPKG-TASK-007` | changed `WFC-C-001` and new `AC-WFC-C-001-01..05` (`STALE`/`DRAFT`), accepted `CTR-007` |

`RMP-001` is the documentation/control foundation owned by `00`, G1/G2/C1 decisions, and the Task template/graph rather than a runtime Task node.

## 5. Optional capability exclusion

No Task node admits RAG, model routing, Governance automation, SaaS/workbench, plugins, domain modules, broad CI/release automation, or other optional dossiers. Admission requires a new exact human product decision and accepted contract.

## 6. One next action

```yaml
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
