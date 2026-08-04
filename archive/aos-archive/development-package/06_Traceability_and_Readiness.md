---
artifact_id: AOS3-DPKG-DOC-006
artifact_type: TRACEABILITY_AND_READINESS
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R12
status: DRAFT_R14_ROUTE_A_TRACE_CORRECTION
authority: PROPOSAL_AND_DERIVED_VIEW
exact_subject: Bidirectional traceability across RMP-001 through RMP-008, requirements, decisions, contracts, scenarios, Tasks, blockers, optional dossiers, and readiness axes
created: '2026-07-30'
human_acceptance: C1_ACCEPTED_126_CURRENT_11_STALE_10_NEW_AC_AND_2_NEW_SCHEMA_DRAFT
independent_validation: DRAFT_R6_FAIL_DRAFT_R7_FAIL_DRAFT_R8_FAIL_DRAFT_R9_FAIL_DRAFT_R10_FAIL_DRAFT_R11_FAIL_DRAFT_R12_FAIL_DRAFT_R13_FAIL_DRAFT_R14_NOT_RUN
provenance:
  - path: ../AOS_Core_Roadmap.md
    use: RMP-001 through RMP-008 documentation items
  - path: 00_Control_and_Source_Precedence.md
    use: package control, IDs, stages, and source precedence
  - path: 01_Product_and_Core_V1_Scope.md
    use: REQ-CV1-001 through REQ-CV1-012
  - path: 02_User_Journeys_and_Workflows.md
    use: REQ-WF-001 through REQ-WF-010
  - path: 03_Architecture_and_Decisions.md
    use: REQ-ARCH-001 through REQ-ARCH-010 and DEC-ARCH records
  - path: 04_Runtime_and_Data_Contracts.md
    use: CTR-001 through CTR-007 and acceptance IDs
  - path: 05_Quality_Recovery_and_Security.md
    use: SCN-001 through SCN-044
  - path: decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
    use: package-local Task identity and bounded correction decision
upstream_links:
  - 00_Control_and_Source_Precedence.md
  - 01_Product_and_Core_V1_Scope.md
  - 02_User_Journeys_and_Workflows.md
  - 03_Architecture_and_Decisions.md
  - 04_Runtime_and_Data_Contracts.md
  - 05_Quality_Recovery_and_Security.md
  - decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
downstream_links:
  - 07_Implementation_Handoff.md
  - decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
  - tasks/TASK-TEMPLATE.md
  - tasks/TASK-GRAPH.md
  - tasks/AOS3-DPKG-TASK-001_Core_Scaffold.md
  - tasks/AOS3-DPKG-TASK-002_Local_Bootstrap.md
  - adapters/CODEX.md
limitations:
  - This is a derived traceability/readiness view and does not own product, contract, decision, repository, or Evidence facts.
  - DEC-CONTRACT-001 owns acceptance of the exact DRAFT-R4 subjects; changed PSC-A-001, WFC-A-001, WFC-B-001, WFC-C-001, and AC-WFC-A-001-01..07 are stale against that decision.
  - Ten AC-WFC-B/C IDs and two shared schemas are new DRAFT subjects and have no human acceptance.
  - Scenario execution remains NOT_RUN.
  - Task artifacts are DRAFT candidates and have not received human Task acceptance.
  - DRAFT-R10 semantic validation failed because the manual forward and reverse requirement-contract relation sets did not round-trip; its mechanical branch was UNKNOWN because required YAML, duplicate-key, A2, and exact projection checks were not completed.
  - DRAFT-R11 validation confirmed registry/projection equality but failed because three Task-002 requirements had no relation to its derived contract CTR-002.
  - DRAFT-R12 added those three exact relations and a materialized-Task relation-closure invariant; validation confirmed the 84-row registry and its two requirement-contract projections but found one omitted materialized Task projection for REQ-ARCH-003.
  - DRAFT-R13 validation failed because `REQ-ARCH-009 → CTR-002 → Task-002` lacked executable unknown-format Evidence and the `REQ-WF-006` Task cell contained a non-derived materialized Task note.
  - DRAFT-R14 removes only those unsupported derivations, regenerates the registry projections from 83 exact relations, and leaves independent validation NOT_RUN.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# 06 — Traceability and Readiness

## 1. Status and readiness boundary

```yaml
traceability_status: DRAFT_R14_ROUTE_A_TRACE_CORRECTION
RMP_coverage_claim: DOCUMENTED_AWAITING_DRAFT_R14_VALIDATION
contract_acceptance:
  accepted_decision: DEC-CONTRACT-001
  accepted_subject_manifest_sha256: 2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
  original_accepted_subjects: 137
  current_accepted_subjects: 126
  stale_c1_subjects: [PSC-A-001, WFC-A-001, WFC-B-001, WFC-C-001, AC-WFC-A-001-01..07]
  new_draft_acceptance_ids: [AC-WFC-B-001-01..05, AC-WFC-C-001-01..05]
  new_draft_schema_ids: [SCH-PRODUCT-SPEC-001, SCH-FEATURE-PASSPORT-001]
  current_requirement_contract_acceptance_scenario_and_schema_subjects: 149
task_compilation: TWO_CURRENT_ACCEPTED_INPUT_DRAFT_CANDIDATES_FIVE_GRAPH_ONLY
task_candidate_acceptance: NOT_RUN
runtime_readiness: NOT_RUN
independent_validation:
  DRAFT_R5: FAIL
  DRAFT_R6: FAIL
  DRAFT_R7: FAIL
  DRAFT_R8: FAIL
  DRAFT_R9: FAIL
  DRAFT_R10: FAIL
  DRAFT_R11: FAIL
  DRAFT_R12: FAIL
  DRAFT_R13: FAIL
  DRAFT_R14: NOT_RUN
human_review: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

Readiness is evaluated by axis. No green axis promotes another.

## 2. RMP coverage

| Roadmap item | Documentation owner(s) | Decisions | Contract | Scenarios | Current state |
|---|---|---|---|---|---|
| `RMP-001` | `00`, `01`, `02` | `DEC-PROD-001..006`, `DEC-CONTRACT-001` | changed `PSC-A-001`, `WFC-A-001`, and `AC-WFC-A-001-01..07` DRAFT/C1-stale | `SCN-009..012`, `SCN-014`, `SCN-025`, `SCN-029`, `SCN-032`, `SCN-035`, `SCN-037`, `SCN-039`; `NEG-PSC-*`, `NEG-WF-*` | AOS3-DPKG-TASK-003 graph-only and blocked pending new PSC/WFC/AC/schema acceptance |
| `RMP-002` | `03`, `04`, `05` | `DEC-ARCH-001`, `DEC-ARCH-003`, `DEC-CONTRACT-001` | `CTR-001` | `SCN-001..004` | Accepted; implementation repository intentionally deferred |
| `RMP-003` | `03`, `04`, `05` | `DEC-ARCH-002`, `DEC-ARCH-003`, `DEC-CONTRACT-001`; `DEC-ARCH-008` is a deferred compatibility boundary | `CTR-002` | `SCN-005..008`, `SCN-036` | Accepted bootstrap contract; compatibility import remains unadmitted and has no current contract/Task |
| `RMP-004` | `01`, `02`, `04`, `05` | `DEC-PROD-005`, `DEC-PROD-006`, `DEC-ARCH-002`, `DEC-ARCH-004`, `DEC-ARCH-005`, `DEC-CONTRACT-001` | accepted `CTR-003`; changed `PSC-A-001`, `WFC-A-001`, plus new shared schemas DRAFT | `SCN-009..012`, `SCN-029`, `SCN-037`, `SCN-039` | AOS3-DPKG-TASK-003 graph-only and blocked |
| `RMP-005` | `02`, `04`, `05` | `DEC-PROD-006`, `DEC-ARCH-001`, `DEC-ARCH-004`, `DEC-ARCH-007`, `DEC-CONTRACT-001`, `DEC-CORR-001` | accepted `CTR-004`; changed `WFC-B-001` DRAFT/C1-stale | `SCN-013..016`, `SCN-032`, `SCN-040`, `SCN-041` | AOS3-DPKG-TASK-004 graph-only and blocked pending new WFC acceptance |
| `RMP-006` | `02`, `04`, `05` | `DEC-ARCH-006`, `DEC-ARCH-007`, `DEC-CONTRACT-001` | `CTR-005` | `SCN-017..020`, `SCN-033`, `SCN-043`, `SCN-044` | Accepted; AOS3-DPKG-TASK-005 graph-only |
| `RMP-007` | `02`, `04`, `05` | `DEC-ARCH-006`, `DEC-ARCH-007`, `DEC-CONTRACT-001` | `CTR-006` | `SCN-021..024`, `SCN-034`, `SCN-035`, `SCN-042` | Accepted; AOS3-DPKG-TASK-006 graph-only |
| `RMP-008` | `02`, `04`, `05`, `07` | `DEC-ARCH-004`, `DEC-ARCH-006`, `DEC-CONTRACT-001`, `DEC-CORR-001` | accepted `CTR-007`; changed `WFC-C-001` DRAFT/C1-stale | `SCN-025..028`, `SCN-030`, `SCN-031`, `SCN-044` | AOS3-DPKG-TASK-007 graph-only and blocked pending new WFC acceptance |

Coverage means a named contract and scenario specification exists. C1 acceptance is projected subject-by-subject; changed definitions are never inherited from an older hash. Acceptance does not mean Task acceptance, implementation, execution, or validation.

Every `AOS3-DPKG-TASK-003` reference in the trace tables below is a prospective graph-node mapping only. No Task-003 document exists in DRAFT-R14; the node is blocked by stale `PSC-A-001`, stale `WFC-A-001`, stale `AC-WFC-A-001-01..07`, and new DRAFT `SCH-PRODUCT-SPEC-001`/`SCH-FEATURE-PASSPORT-001` schemas.

### 2.1 Exact scenario manifest

| Contract/subject | Positive | Negative | Failure | Recovery | Additional cross-contract scenarios |
|---|---|---|---|---|---|
| `CTR-001` | `SCN-001` | `SCN-002` | `SCN-003` | `SCN-004` | `SCN-036` |
| `CTR-002` | `SCN-005` | `SCN-006` | `SCN-007` | `SCN-008` | `SCN-036`, `SCN-038` |
| `CTR-003` | `SCN-009` | `SCN-010` | `SCN-011` | `SCN-012` | `SCN-029`, `SCN-031`, `SCN-037`, `SCN-039` |
| `CTR-004` | `SCN-013` | `SCN-014` | `SCN-015` | `SCN-016` | `SCN-032`, `SCN-040`, `SCN-041` |
| `CTR-005` | `SCN-017` | `SCN-018` | `SCN-019` | `SCN-020` | `SCN-033`, `SCN-036`, `SCN-040`, `SCN-043`, `SCN-044` |
| `CTR-006` | `SCN-021` | `SCN-022` | `SCN-023` | `SCN-024` | `SCN-034`, `SCN-035`, `SCN-042` |
| `CTR-007` | `SCN-025` | `SCN-026` | `SCN-027` | `SCN-028` | `SCN-030`, `SCN-031`, `SCN-044` |

Every `SCN-001..044` is defined in owner `05`; repeated cross-contract links express applicability, not duplicate scenario ownership.

### 2.2 `TRC-REG-001` atomic requirement-contract relation registry

`TRC-REG-001` is the sole owner of the DRAFT requirement-to-portable-contract relation set. A relation key is the tuple `(requirement_id, contract_id)`. The registry does not own or alter either endpoint definition, acceptance, scenario, decision, or Task semantics.

```yaml
registry_id: TRC-REG-001
revision: R3
status: DRAFT
authority: PROPOSAL_AND_DERIVED_TRACE_OWNER
atomic_key: [requirement_id, contract_id]
row_count: 83
payload_normalization: each registry table row becomes requirement_id<TAB>contract_id<TAB>origin<LF>, sorted lexicographically by requirement_id then contract_id
payload_sha256: af15f5e0af1ca667136e1ffc2352e3acc7bf3cb5c037f62f558818889170aa69
origin_counts:
  BOTH_CURRENT_VIEWS: 31
  FORWARD_ONLY_DRAFT_R10: 3
  REVERSE_ONLY_DRAFT_R10: 46
  SEMANTIC_COMPLETENESS_DRAFT_R12: 3
projection_invariant: FORWARD_EXPANSION_EQUALS_REGISTRY_EQUALS_INVERTED_REVERSE_EXPANSION
task_projection_invariant: EVERY_MATERIALIZED_TASK_REQUIREMENT_HAS_AT_LEAST_ONE_RELATION_TO_A_DERIVED_CONTRACT_AND_EVERY_DERIVED_CONTRACT_HAS_AT_LEAST_ONE_RELATION_FROM_A_DERIVED_REQUIREMENT
materialized_task_projection_authority: EXISTING_TASK_BRIEF_DERIVED_FROM_FIELDS
materialized_forward_task_projection_invariant: MATERIALIZED_FORWARD_TASK_PROJECTION_EQUALS_INVERTED_TASK_BRIEF_REQUIREMENTS
materialized_reverse_task_projection_invariant: MATERIALIZED_REVERSE_TASK_PROJECTION_EQUALS_TASK_BRIEF_CONTRACTS
materialized_task_evidence_invariant: EVERY_MATERIALIZED_TASK_REQUIREMENT_CONTRACT_PATH_HAS_EXISTING_ACCEPTANCE_OR_SCENARIO_EVIDENCE
graph_only_task_projection_authority: AOS3-DPKG-TASK-GRAPH-001
acceptance_effect: NONE
task_effect: NONE
```

| Requirement ID | Portable contract ID | Relation provenance |
|---|---|---|
| `REQ-ARCH-002` | `CTR-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-ARCH-002` | `CTR-002` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-ARCH-002` | `CTR-005` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-ARCH-003` | `CTR-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-ARCH-003` | `CTR-002` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-ARCH-003` | `CTR-006` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-ARCH-004` | `CTR-004` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-ARCH-004` | `CTR-007` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-ARCH-005` | `CTR-007` | `BOTH_CURRENT_VIEWS` |
| `REQ-ARCH-007` | `CTR-005` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-ARCH-007` | `CTR-006` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-ARCH-008` | `CTR-004` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-ARCH-008` | `CTR-005` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-ARCH-010` | `CTR-001` | `BOTH_CURRENT_VIEWS` |
| `REQ-ARCH-010` | `CTR-004` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-001` | `CTR-003` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-001` | `PSC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-CV1-002` | `CTR-003` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-002` | `PSC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-CV1-003` | `CTR-003` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-003` | `PSC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-CV1-004` | `CTR-003` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-004` | `PSC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-CV1-005` | `CTR-003` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-005` | `PSC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-CV1-006` | `CTR-003` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-006` | `CTR-006` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-006` | `PSC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-CV1-007` | `CTR-004` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-008` | `CTR-007` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-009` | `CTR-002` | `SEMANTIC_COMPLETENESS_DRAFT_R12` |
| `REQ-CV1-009` | `CTR-003` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-009` | `CTR-007` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-010` | `PSC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-CV1-011` | `CTR-004` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-011` | `PSC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-CV1-012` | `CTR-001` | `BOTH_CURRENT_VIEWS` |
| `REQ-CV1-012` | `PSC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-001` | `CTR-003` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-001` | `WFC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-002` | `CTR-003` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-002` | `CTR-004` | `FORWARD_ONLY_DRAFT_R10` |
| `REQ-WF-002` | `CTR-005` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-002` | `CTR-006` | `FORWARD_ONLY_DRAFT_R10` |
| `REQ-WF-002` | `CTR-007` | `FORWARD_ONLY_DRAFT_R10` |
| `REQ-WF-002` | `WFC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-002` | `WFC-B-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-002` | `WFC-C-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-003` | `CTR-003` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-003` | `CTR-007` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-003` | `WFC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-003` | `WFC-C-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-004` | `CTR-001` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-004` | `CTR-002` | `SEMANTIC_COMPLETENESS_DRAFT_R12` |
| `REQ-WF-004` | `CTR-003` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-004` | `CTR-004` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-004` | `CTR-005` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-004` | `WFC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-004` | `WFC-B-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-004` | `WFC-C-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-005` | `CTR-003` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-005` | `CTR-006` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-005` | `WFC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-006` | `CTR-004` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-006` | `WFC-B-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-007` | `CTR-007` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-007` | `WFC-C-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-008` | `CTR-002` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-008` | `CTR-003` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-008` | `CTR-005` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-008` | `CTR-007` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-008` | `WFC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-008` | `WFC-B-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-008` | `WFC-C-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-009` | `CTR-006` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-009` | `WFC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-009` | `WFC-C-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-010` | `CTR-002` | `SEMANTIC_COMPLETENESS_DRAFT_R12` |
| `REQ-WF-010` | `CTR-003` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-010` | `CTR-007` | `BOTH_CURRENT_VIEWS` |
| `REQ-WF-010` | `WFC-A-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-010` | `WFC-B-001` | `REVERSE_ONLY_DRAFT_R10` |
| `REQ-WF-010` | `WFC-C-001` | `REVERSE_ONLY_DRAFT_R10` |

Registry and projection checks are deterministic:

1. every tuple is unique and sorted;
2. each endpoint resolves to its existing definition owner;
3. registry normalization reproduces the declared payload SHA-256;
4. grouping by `requirement_id` exactly reproduces §§3–5;
5. grouping by `contract_id` exactly reproduces §6;
6. range compression is forbidden in the registry and may appear only in non-authoritative prose;
7. missing, additional, duplicate, unknown-endpoint, or out-of-order tuples fail the check;
8. registry or projection state never changes endpoint acceptance, Task derivation, implementation authority, or Git authority.
9. for every materialized Task, each `derived_from.requirements` ID has a registry relation to at least one `derived_from.contracts` ID, and each derived contract has a registry relation from at least one derived requirement.
10. the materialized Task entries in §§3–5 equal the inversion of the `derived_from.requirements` fields in the existing Task Briefs;
11. the materialized Task entries in §6 equal the `derived_from.contracts` fields in those same Task Briefs;
12. graph-only Task entries are a separately labelled projection of `tasks/TASK-GRAPH.md` and never masquerade as materialized briefs;
13. every materialized Task requirement-contract path retains at least one existing acceptance or scenario Evidence path from that Task Brief; no projection creates a new endpoint definition.

## 3. Product requirement traceability — derived forward projection

The portable-contract columns in §§3–5 are derived from `TRC-REG-001`. Materialized Task entries are derived only by inverting `derived_from.requirements` in the existing Task Briefs. Graph-only Task entries are a separate labelled projection from `tasks/TASK-GRAPH.md`.

```yaml
materialized_task_projection:
  source: existing Task Brief derived_from.requirements
  task_ids: [AOS3-DPKG-TASK-001, AOS3-DPKG-TASK-002]
graph_only_task_projection:
  source: tasks/TASK-GRAPH.md
  task_ids: [AOS3-DPKG-TASK-003, AOS3-DPKG-TASK-004, AOS3-DPKG-TASK-005, AOS3-DPKG-TASK-006, AOS3-DPKG-TASK-007]
```

Every appearance of `AOS3-DPKG-TASK-003..007` in a Task cell is graph-only even when a compact cell omits the repeated suffix; it never asserts a Task Brief exists.

| Requirement | Portable contracts from `TRC-REG-001` | Additional non-registry owner(s) | Scenario/Evidence requirement | Task |
|---|---|---|---|---|
| `REQ-CV1-001` preserve original input | `CTR-003`, `PSC-A-001` | `NONE` | `SCN-009`, `SCN-010`; input bytes/digest | `AOS3-DPKG-TASK-003` |
| `REQ-CV1-002` separate claim classes | `CTR-003`, `PSC-A-001` | shared vocab | `SCN-009`, `SCN-010`, `SCN-037`; classified record | `AOS3-DPKG-TASK-003` |
| `REQ-CV1-003` material questions only | `CTR-003`, `PSC-A-001` | `NONE` | `SCN-009`; question affected-field record | `AOS3-DPKG-TASK-003` |
| `REQ-CV1-004` DRAFT Product Spec | `CTR-003`, `PSC-A-001` | `NONE` | `SCN-009`, `SCN-012`; schema and manifest | `AOS3-DPKG-TASK-003` |
| `REQ-CV1-005` feature-specific Passport | `CTR-003`, `PSC-A-001` | `NONE` | `SCN-009`, `SCN-012`; owner fields | `AOS3-DPKG-TASK-003` |
| `REQ-CV1-006` stop without downstream authority | `CTR-003`, `CTR-006`, `PSC-A-001` | `NONE` | `SCN-009`, `SCN-035`, `SCN-041`; non-grants | `AOS3-DPKG-TASK-003`; `AOS3-DPKG-TASK-006` graph-only |
| `REQ-CV1-007` Tasks only from accepted IDs | `CTR-004` | `NONE` | `SCN-014`, `SCN-032`; zero Task output | `AOS3-DPKG-TASK-004` graph-only |
| `REQ-CV1-008` resume and stale detection | `CTR-007` | `NONE` | `SCN-026`, `SCN-031`; stale classification | `AOS3-DPKG-TASK-007` graph-only |
| `REQ-CV1-009` one safe next action | `CTR-002`, `CTR-003`, `CTR-007` | `NONE` | `SCN-009`, `SCN-025`; exactly-one check | `AOS3-DPKG-TASK-002`, `AOS3-DPKG-TASK-003`; `AOS3-DPKG-TASK-007` graph-only |
| `REQ-CV1-010` adapter-independent core | `PSC-A-001` | `REQ-ARCH-001`, `CMP-009` | dependency/drift check; `SCN-039` | `AOS3-DPKG-TASK-003`; graph-wide invariant |
| `REQ-CV1-011` optional features excluded | `CTR-004`, `PSC-A-001` | `NONE` | optional-admission fixture | `AOS3-DPKG-TASK-004` graph-only |
| `REQ-CV1-012` repository unassigned until separate binding | `CTR-001`, `PSC-A-001` | `DEC-ARCH-001` | `SCN-002`; placeholder and notebook-as-implementation rejected | `AOS3-DPKG-TASK-001` |

## 4. Workflow requirement traceability — derived forward projection

| Requirement | Portable contracts from `TRC-REG-001` | Additional non-registry owner(s) | Scenario/Evidence requirement | Task |
|---|---|---|---|---|
| `REQ-WF-001` provenance for input/answers | `CTR-003`, `WFC-A-001` | `NONE` | `SCN-009`, `SCN-012` | `AOS3-DPKG-TASK-003` |
| `REQ-WF-002` actor/authority per transition | `CTR-003`, `CTR-004`, `CTR-005`, `CTR-006`, `CTR-007`, `WFC-A-001`, `WFC-B-001`, `WFC-C-001` | `NONE` | contract-schema inspection | `AOS3-DPKG-TASK-003`; `AOS3-DPKG-TASK-004..007` graph-only |
| `REQ-WF-003` visible missing/unknown/conflict | `CTR-003`, `CTR-007`, `WFC-A-001`, `WFC-C-001` | `NONE` | `SCN-010`, `SCN-026`, `SCN-037` | `AOS3-DPKG-TASK-003`; `AOS3-DPKG-TASK-007` graph-only |
| `REQ-WF-004` gate blocks dependent work only | `CTR-001`, `CTR-002`, `CTR-003`, `CTR-004`, `CTR-005`, `WFC-A-001`, `WFC-B-001`, `WFC-C-001` | `03` §10 | `SCN-002`, `SCN-014`, `SCN-032` | `AOS3-DPKG-TASK-001`, `AOS3-DPKG-TASK-002`, `AOS3-DPKG-TASK-003`; `AOS3-DPKG-TASK-004` graph-only |
| `REQ-WF-005` review candidate freeze | `CTR-003`, `CTR-006`, `WFC-A-001` | `CandidateManifest` | `SCN-021`, `SCN-023`, `SCN-034` | `AOS3-DPKG-TASK-003`; `AOS3-DPKG-TASK-006` graph-only |
| `REQ-WF-006` accepted upstream for Task | `CTR-004`, `WFC-B-001` | `NONE` | `SCN-014`, `SCN-032` | `AOS3-DPKG-TASK-004` graph-only |
| `REQ-WF-007` refresh mutable facts | `CTR-007`, `WFC-C-001` | `NONE` | `SCN-025`, `SCN-026` | `AOS3-DPKG-TASK-007` graph-only |
| `REQ-WF-008` failure recovery and stop | `CTR-002`, `CTR-003`, `CTR-005`, `CTR-007`, `WFC-A-001`, `WFC-B-001`, `WFC-C-001` | `NONE` | `SCN-007`, `SCN-019`, `SCN-027`, `SCN-044` | `AOS3-DPKG-TASK-002`, `AOS3-DPKG-TASK-003`; `AOS3-DPKG-TASK-005`, `AOS3-DPKG-TASK-007` graph-only |
| `REQ-WF-009` validation read-only | `CTR-006`, `WFC-A-001`, `WFC-C-001` | `NONE` | `SCN-023`, `SCN-034` | `AOS3-DPKG-TASK-006` graph-only |
| `REQ-WF-010` one next action and authority | `CTR-002`, `CTR-003`, `CTR-007`, `WFC-A-001`, `WFC-B-001`, `WFC-C-001` | `ResultEnvelope` | `SCN-025` | `AOS3-DPKG-TASK-002`, `AOS3-DPKG-TASK-003`; `AOS3-DPKG-TASK-007` graph-only |

## 5. Architecture requirement traceability — derived forward projection

| Requirement | Portable contracts from `TRC-REG-001` | Additional non-registry owner(s) | Scenario/check | Task |
|---|---|---|---|---|
| `REQ-ARCH-001` adapter-independent contracts | `NONE` | `DEC-ARCH-002`, `CMP-009` | dependency and adapter drift check | `AOS3-DPKG-TASK-003`; graph-wide invariant |
| `REQ-ARCH-002` mutation only via explicit operation | `CTR-001`, `CTR-002`, `CTR-005` | `PORT-002`, write request | architecture and call-path test | `AOS3-DPKG-TASK-001`, `AOS3-DPKG-TASK-002`; `AOS3-DPKG-TASK-005` graph-only |
| `REQ-ARCH-003` read-only cannot reach writes | `CTR-001`, `CTR-002`, `CTR-006` | `PORT-001`, `PORT-005`, `PORT-008` | `AC-CTR-002-01`, `SCN-005`, `SCN-023`, `SCN-027`; zero-write preview/validation proof | `AOS3-DPKG-TASK-001`, `AOS3-DPKG-TASK-002`, `AOS3-DPKG-TASK-003`; `AOS3-DPKG-TASK-006`, `AOS3-DPKG-TASK-007` graph-only |
| `REQ-ARCH-004` one fact owner | `CTR-004`, `CTR-007` | `03` §6 | owner/projection drift fixture | `AOS3-DPKG-TASK-003`; `AOS3-DPKG-TASK-004`, `AOS3-DPKG-TASK-007` graph-only |
| `REQ-ARCH-005` relative memory and rebuildable index | `CTR-007` | `DEC-ARCH-004` | `SCN-025`, `SCN-026`; rebuild determinism | `AOS3-DPKG-TASK-007` graph-only |
| `REQ-ARCH-006` no hidden provider | `NONE` | `DEC-ARCH-005` | `SCN-039`; network-deny test | `AOS3-DPKG-TASK-003` |
| `REQ-ARCH-007` exact local Human Decisions | `CTR-005`, `CTR-006` | `DEC-ARCH-006`, `HumanDecisionRecord` | `SCN-031`, `SCN-035`, `SCN-041` | `AOS3-DPKG-TASK-003`; `AOS3-DPKG-TASK-005`, `AOS3-DPKG-TASK-006` graph-only |
| `REQ-ARCH-008` human-owned Risk | `CTR-004`, `CTR-005` | `DEC-ARCH-007` | `SCN-040` | `AOS3-DPKG-TASK-004`, `AOS3-DPKG-TASK-005` graph-only |
| `REQ-ARCH-009` no silent legacy compatibility | `NONE` | `DEC-ARCH-008` deferred compatibility boundary | future accepted compatibility/import contract plus executable unknown-format rejection | `NONE`; no current Task derivation |
| `REQ-ARCH-010` physical topology/execution waits for repo while portable Task docs may remain unbound | `CTR-001`, `CTR-004` | `DEC-ARCH-001` | `SCN-002`, `SCN-013` | `AOS3-DPKG-TASK-001`; `AOS3-DPKG-TASK-004` graph-only |

## 6. Reverse traceability — derived contract projection

The `Requirements from TRC-REG-001` column is generated only by grouping the atomic registry by `contract_id`. Acceptance references remain a separate non-registry projection and do not participate in the bidirectional requirement-contract equality check. Materialized Task entries in `Task eligibility` are generated from each existing Task Brief's `derived_from.contracts`; graph-only entries remain a separately labelled `TASK-GRAPH` projection.

| Contract | Requirements from `TRC-REG-001` | Acceptance refs | Decisions | Primary scenarios | Task eligibility |
|---|---|---|---|---|---|
| `PSC-A-001` R2 DRAFT/C1-stale | `REQ-CV1-001`, `REQ-CV1-002`, `REQ-CV1-003`, `REQ-CV1-004`, `REQ-CV1-005`, `REQ-CV1-006`, `REQ-CV1-010`, `REQ-CV1-011`, `REQ-CV1-012` | `AC-PSC-A-001-01..08` | `DEC-PROD-001..006`; `DEC-CONTRACT-001` is stale for the changed PSC definition | `SCN-009..012`, `SCN-014`, `SCN-025`, `SCN-032`, `SCN-035`, `SCN-037`, `SCN-039`; `NEG-PSC-A-001-01..08` | `AOS3-DPKG-TASK-003` graph-only and blocked |
| `WFC-A-001` R3 DRAFT | `REQ-WF-001`, `REQ-WF-002`, `REQ-WF-003`, `REQ-WF-004`, `REQ-WF-005`, `REQ-WF-008`, `REQ-WF-009`, `REQ-WF-010` | `AC-WFC-A-001-01..07` DRAFT/C1-stale | `DEC-PROD-003..006`; `DEC-CONTRACT-001` is stale for the changed WFC and its A2-owned AC definitions | `NEG-WF-001..011` | `AOS3-DPKG-TASK-003` graph-only and blocked |
| `WFC-B-001` R2 DRAFT | `REQ-WF-002`, `REQ-WF-004`, `REQ-WF-006`, `REQ-WF-008`, `REQ-WF-010` | `AC-WFC-B-001-01..05` DRAFT | `DEC-PROD-003`, `DEC-PROD-006`; `DEC-CONTRACT-001` is stale for this changed subject | `SCN-013..016`, `SCN-032` | `AOS3-DPKG-TASK-004` graph-only and blocked |
| `WFC-C-001` R2 DRAFT | `REQ-WF-002`, `REQ-WF-003`, `REQ-WF-004`, `REQ-WF-007`, `REQ-WF-008`, `REQ-WF-009`, `REQ-WF-010` | `AC-WFC-C-001-01..05` DRAFT | `DEC-PROD-003`; `DEC-CONTRACT-001` is stale for this changed subject | `SCN-025..031`, `SCN-044` | `AOS3-DPKG-TASK-007` graph-only and blocked |
| `CTR-001` | `REQ-ARCH-002`, `REQ-ARCH-003`, `REQ-ARCH-010`, `REQ-CV1-012`, `REQ-WF-004` | `AC-CTR-001-01..04` | `DEC-ARCH-001`, `DEC-ARCH-003`, `DEC-CONTRACT-001` | `SCN-001..004` | `AOS3-DPKG-TASK-001`; repository required for bound enrichment/execution |
| `CTR-002` | `REQ-ARCH-002`, `REQ-ARCH-003`, `REQ-CV1-009`, `REQ-WF-004`, `REQ-WF-008`, `REQ-WF-010` | `AC-CTR-002-01..05` | `DEC-ARCH-002`, `DEC-ARCH-003`, `DEC-CONTRACT-001` | `SCN-005..008`, `SCN-036` | `AOS3-DPKG-TASK-002` |
| `CTR-003` | `REQ-CV1-001`, `REQ-CV1-002`, `REQ-CV1-003`, `REQ-CV1-004`, `REQ-CV1-005`, `REQ-CV1-006`, `REQ-CV1-009`, `REQ-WF-001`, `REQ-WF-002`, `REQ-WF-003`, `REQ-WF-004`, `REQ-WF-005`, `REQ-WF-008`, `REQ-WF-010` | `AC-CTR-003-01..06` | `DEC-PROD-*`, `DEC-ARCH-002`, `DEC-ARCH-004`, `DEC-ARCH-005`, `DEC-CONTRACT-001` | `SCN-009..012`, `SCN-029`, `SCN-037`, `SCN-039` | `AOS3-DPKG-TASK-003` graph-only; blocked by other upstream subjects |
| `CTR-004` | `REQ-ARCH-004`, `REQ-ARCH-008`, `REQ-ARCH-010`, `REQ-CV1-007`, `REQ-CV1-011`, `REQ-WF-002`, `REQ-WF-004`, `REQ-WF-006` | `AC-CTR-004-01..05` | `DEC-ARCH-001`, `DEC-ARCH-004`, `DEC-ARCH-007`, `DEC-CONTRACT-001` | `SCN-013..016`, `SCN-032`, `SCN-040`, `SCN-041` | `AOS3-DPKG-TASK-004` graph-only; repository required only for bound enrichment/execution |
| `CTR-005` | `REQ-ARCH-002`, `REQ-ARCH-007`, `REQ-ARCH-008`, `REQ-WF-002`, `REQ-WF-004`, `REQ-WF-008` | `AC-CTR-005-01..05` | `DEC-ARCH-006`, `DEC-ARCH-007`, `DEC-CONTRACT-001` | `SCN-017..020`, `SCN-033`, `SCN-043`, `SCN-044` | `AOS3-DPKG-TASK-005` graph-only |
| `CTR-006` | `REQ-ARCH-003`, `REQ-ARCH-007`, `REQ-CV1-006`, `REQ-WF-002`, `REQ-WF-005`, `REQ-WF-009` | `AC-CTR-006-01..05` | `DEC-ARCH-006`, `DEC-CONTRACT-001` | `SCN-021..024`, `SCN-034`, `SCN-035`, `SCN-042` | `AOS3-DPKG-TASK-006` graph-only |
| `CTR-007` | `REQ-ARCH-004`, `REQ-ARCH-005`, `REQ-CV1-008`, `REQ-CV1-009`, `REQ-WF-002`, `REQ-WF-003`, `REQ-WF-007`, `REQ-WF-008`, `REQ-WF-010` | `AC-CTR-007-01..05` | `DEC-ARCH-004`, `DEC-ARCH-006`, `DEC-CONTRACT-001` | `SCN-025..028`, `SCN-030`, `SCN-031`, `SCN-044` | `AOS3-DPKG-TASK-007` graph-only |

## 7. Task boundary and registry

```yaml
task_template:
  status: CREATED_DRAFT
  path: tasks/TASK-TEMPLATE.md
  namespace_decision: DEC-CORR-001
  namespace: AOS3-DPKG-TASK-###
bounded_task_graph:
  status: CREATED_DRAFT
  path: tasks/TASK-GRAPH.md
  nodes: 7
task_briefs:
  materialized_count: 2
  materialized_ids: [AOS3-DPKG-TASK-001, AOS3-DPKG-TASK-002]
  graph_only_count: 5
  graph_only_ids: [AOS3-DPKG-TASK-003, AOS3-DPKG-TASK-004, AOS3-DPKG-TASK-005, AOS3-DPKG-TASK-006, AOS3-DPKG-TASK-007]
  stale_or_draft_upstream_blocked_ids: [AOS3-DPKG-TASK-003, AOS3-DPKG-TASK-004, AOS3-DPKG-TASK-007]
  repository_binding_state: PORTABLE_UNBOUND
human_task_acceptance: NOT_RUN
task_execution: NOT_RUN
```

The two materialized briefs derive only from current unchanged C1-accepted subjects and do not depend on any of the eleven stale or twelve new DRAFT subjects. No brief is materialized for changed `PSC-A-001`, `WFC-A-001`, `WFC-B-001`, `WFC-C-001`, stale `AC-WFC-A-001-01..07`, the ten new DRAFT `AC-WFC-B/C-*` IDs, or the two new DRAFT shared schemas. Task candidates do not satisfy human Task acceptance and cannot activate graph nodes, bind a repository, or authorize implementation.

## 8. Optional capability dossiers

| Capability | Package disposition | Trace | Core task queue |
|---|---|---|---|
| RAG-light / vector retrieval | `DEFERRED` | `FTR-017` | Excluded |
| Runtime model routing | `DEFERRED` | `FTR-018` | Excluded |
| Progressive Governance/enforcement | `DEFERRED` | `FTR-020/021` | Excluded |
| Patterns library | `REFERENCE_ONLY` | `FTR-022` | Excluded |
| Broad CI/release automation | `DEFERRED` | `FTR-023/024` | Excluded |
| Observability/incident platform | `DEFERRED` | `FTR-025` | Excluded |
| Plugins/extensions | `DEFERRED` | `FTR-026` | Excluded |
| Domain modules | `REFERENCE_ONLY` | `FTR-027` | Excluded |
| Workbench/SaaS | `DEFERRED` | `FTR-028` | Excluded |
| Packaging/prompt packs/policy overlays | `DEFERRED` | `FTR-029` | Excluded |
| Internal contract tools beyond first-slice need | `DEFERRED` | `FTR-030` | Excluded |

Admission requires an exact product need, item-scoped human disposition, accepted contract, scenarios, architecture decision when material, and a new Task decision.

## 9. Readiness axes

| Axis | State | Evidence | Effect |
|---|---|---|---|
| Product direction | `HUMAN_DECIDED` | `DEC-PROD-001..006` | Allows DRAFT contracts |
| Stage B candidate/G2 input | `HASH_BOUND_ACCEPTED_FOR_G2` | user decision + `d8170b...` | Supports architecture decisions |
| Logical architecture | `HUMAN_DECIDED` | `DEC-ARCH-002..008` | Allows Stage C contract authoring |
| Exact implementation repository | `HUMAN_DEFERRED_UNASSIGNED` | `DEC-ARCH-001` R4 record | Blocks physical paths, bound enrichment, and execution; does not block accepted portable Task docs |
| Contract subjects | `PARTIAL_CURRENT_ACCEPTANCE` | 126 unchanged current accepted; 1 changed PSC, 3 changed WFC, and 7 A2-owned AC subjects C1-stale; 10 new AC plus 2 schema subjects DRAFT | Allows only Tasks derived from the 126 current accepted subjects |
| Contract scenario execution | `NOT_RUN` | `05` | No runtime claim |
| Task template/graph/briefs | `DRAFT_CANDIDATES_CREATED_WITH_BLOCKED_GRAPH_NODES` | §7; four Task files and seven graph nodes | Requires separate validation; nodes 003/004/007 also require new upstream acceptance |
| Implementation | `NOT_RUN` | implementation repository deliberately `UNASSIGNED` | No runtime claim |
| Independent validation | `NOT_RUN_FOR_DRAFT_R14` | DRAFT-R6 through DRAFT-R13 Stage D results were `FAIL`, all bound to their exact superseded candidates | No current validation result |
| Human contract gate C1 | `PARTIALLY_CURRENT` | `DEC-CONTRACT-001` plus persisted accepted-subject manifest | 126 unchanged subjects current; no current acceptance for changed PSC/WFCs, stale A2-owned ACs, new B/C ACs, or new schemas |
| Human review of post-C1 Task package | `NOT_RUN` | Stage D and Stage E not authorized | No Task acceptance |
| Git delivery | `NOT_RUN` | authority `NONE` | No Commit/Push/Merge/Release |

## 10. Blocker register

| Blocker ID | Exact subject | Claim class | Blocks | Resolution authority |
|---|---|---|---|---|
| `BLK-001` | Implementation repository is deliberately `UNASSIGNED`; repository creation is not authorized | `OBSERVED_AT_SNAPSHOT` | physical topology, repository-bound enrichment, preflight, implementation/execution | Future separate human repository-binding decision |
| `BLK-002` | Acceptance of corrected PSC-A-001, WFC-A-001, WFC-B-001, WFC-C-001, stale AC-WFC-A-001-01..07, new AC-WFC-B/C-001-01..05, and SCH-PRODUCT-SPEC-001/SCH-FEATURE-PASSPORT-001 | `OBSERVED_AT_SNAPSHOT` — C1 stale/new DRAFT for these subjects | AOS3-DPKG-TASK-003, AOS3-DPKG-TASK-004, and AOS3-DPKG-TASK-007 materialization and dependent graph progression | New exact human contract decision after DRAFT-R14 validation/review |
| `BLK-003` | Exact dependency set and environment matrix unverified | `UNKNOWN` | scaffold Task/acceptance commands | Repository-bound architecture/dependency review |
| `BLK-004` | Scenario execution and runtime Evidence absent | `NOT_RUN` | implementation/runtime/readiness claims | Later implementation and VALIDATE stages |
| `BLK-005` | Stabilization metrics/cycle threshold undecided | `UNKNOWN` | stable-Core claim and automation admission | Human product decision after comparable cycles |
| `BLK-006_CANONICAL_STATUS_AXIS_CONFLICT` | `docs/00_Core.md` includes `HUMAN_REVIEW_REQUIRED` in TechnicalResult while `docs/03_Development.md` and the package use it as maturity/control state | `CONFLICT` | canonical TechnicalResult/ResultEnvelope conformance and dependent readiness claims | Separate human decision and separately authorized canonical `/docs` correction; no automatic repair here |

## 11. Package human-review acceptance tests

The Stage C contract candidate is ready to request human review when:

1. a new agent starts at `00` and identifies the current gate without chat;
2. every `CTR-001..007` includes actor, trigger, preconditions, I/O, states, side effects, authority, failures, recovery, non-goals, and executable acceptance;
3. `TRC-REG-001` has the authorized 83-row payload and both derived requirement-contract projections expand exactly to that registry;
4. both materialized Tasks satisfy the Task relation-closure invariant, forward materialized Task entries equal the inversion of Task Brief `derived_from.requirements`, reverse materialized Task entries equal Task Brief `derived_from.contracts`, graph-only mappings remain separately labelled, each materialized requirement-contract path has existing acceptance/scenario Evidence, `REQ-ARCH-009` has no current contract/Task derivation, and `REQ-WF-006` has no non-derived materialized Task entry;
5. every `RMP-001..008` maps bidirectionally to owners, contracts, and scenarios;
6. every materialized Task artifact derives only from current exact C1-accepted IDs and remains a non-accepted candidate;
7. deferred implementation repository blocks only repository-bound enrichment and execution;
8. reference records retain exact repository/ref/commit/path and authority `NONE`;
9. optional capabilities remain outside the Core queue;
10. adapters cannot alter portable core authority;
11. implementation, runtime, validation, acceptance, and Git claims remain separate;
12. post-change checks find no package-structure, link, fence, YAML, ID, scope, or authorization violation;
13. changed PSC/WFCs, stale A2-owned WFC-A ACs, new WFC-B/C ACs, and new shared schemas remain DRAFT, block only their dependent graph nodes, and are not compiled into Task Briefs;
14. `BLK-006` remains visible without a false canonical status-schema or readiness claim.

These tests prepare a post-C1 package candidate; Stage D validation and later Task review remain separate.

## 12. One next action

```yaml
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
