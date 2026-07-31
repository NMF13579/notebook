---
artifact_id: DEC-CONTRACT-001
artifact_type: HUMAN_CONTRACT_ACCEPTANCE_DECISION
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R5
status: HUMAN_DECIDED
authority: HUMAN_DECISION
exact_subject: Human acceptance of all defined Stage C requirement, contract, acceptance, and scenario IDs in the exact DRAFT-R4 candidate
created: '2026-07-30'
gate_id: HUMAN_CONTRACT_GATE_C1
human_disposition: ACCEPT
human_decision_record:
  schema_version: aos.decision/v1
  decision_id: DEC-CONTRACT-001
  decision_type: CONTRACT
  decision_value: ACCEPT
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  decision_channel: PRIMARY_CODEX_THREAD
  subject:
    kind: ACCEPTED_SUBJECT_SET_WITH_PACKAGE_CANDIDATE
    package_revision: DRAFT-R4
    aggregate_sha256: 00499af5d0f968481f0ed7e75c452bf74bf56eed380fd99d36a9a06dd8c54262
    accepted_subject_manifest_sha256: 2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
    subject_ids:
      - REQ-CV1-001..012
      - REQ-WF-001..010
      - REQ-ARCH-001..010
      - PSC-A-001
      - WFC-A-001
      - WFC-B-001
      - WFC-C-001
      - CTR-001..007
      - AC-PSC-A-001-01..08
      - AC-WFC-A-001-01..07
      - AC-CTR-001-01..04
      - AC-CTR-002-01..05
      - AC-CTR-003-01..06
      - AC-CTR-004-01..05
      - AC-CTR-005-01..05
      - AC-CTR-006-01..05
      - AC-CTR-007-01..05
      - SCN-001..044
  issued_at: '2026-07-30T10:28:46Z'
  grants:
    - CONTRACT_ACCEPTANCE_FOR_137_EXACT_SUBJECTS
    - PORTABLE_TASK_COMPILATION_AS_DOCUMENTATION
  non_grants: [TASK_ACCEPTANCE, IMPLEMENTATION, EXECUTION, VALIDATION, COMMIT, PUSH, MERGE, RELEASE]
  expires_at: NOT_APPLICABLE
  stale_when:
    - any extracted subject definition, revision, or bound hash changes
    - decision value changes or the human revokes it
  consumption: NOT_APPLICABLE
candidate_binding:
  package_revision: DRAFT-R4
  aggregate_sha256: 00499af5d0f968481f0ed7e75c452bf74bf56eed380fd99d36a9a06dd8c54262
  manifest_basis: package-relative sorted SHA-256 lines for 30 DRAFT-R4 files
accepted_subject_manifest:
  manifest_id: AOS3-C1-SUBJECT-MANIFEST-001
  extraction_version: AOS3-C1-SUBJECT-MANIFEST-V1
  payload_path: C1_ACCEPTED_SUBJECT_MANIFEST.tsv
  payload_format: ID<TAB>owner_path<TAB>sha256<LF>
  sha256: 2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
  entries: 137
  requirements: 32
  contracts: 11
  acceptance_ids: 50
  scenarios: 44
provenance:
  - USER_C1_CONFIRMATION_IN_RESPONSE_ANNOTATION_2026-07-30
  - DRAFT_R4_DETERMINISTIC_EXTRACTOR_OUTPUT_RECOVERED_AND_HASH_VERIFIED_2026-07-30
  - C1_ACCEPTED_SUBJECT_MANIFEST.tsv
  - ../00_Control_and_Source_Precedence.md
  - ../01_Product_and_Core_V1_Scope.md
  - ../02_User_Journeys_and_Workflows.md
  - ../03_Architecture_and_Decisions.md
  - ../04_Runtime_and_Data_Contracts.md
  - ../05_Quality_Recovery_and_Security.md
upstream_links:
  - ../00_Control_and_Source_Precedence.md
  - ../01_Product_and_Core_V1_Scope.md
  - ../02_User_Journeys_and_Workflows.md
  - ../03_Architecture_and_Decisions.md
  - ../04_Runtime_and_Data_Contracts.md
  - ../05_Quality_Recovery_and_Security.md
  - ../06_Traceability_and_Readiness.md
  - ../07_Implementation_Handoff.md
downstream_links:
  - C1_ACCEPTED_SUBJECT_MANIFEST.tsv
  - ../tasks/TASK-TEMPLATE.md
  - ../tasks/TASK-GRAPH.md
  - ../tasks/AOS3-DPKG-TASK-001_Core_Scaffold.md
  - ../tasks/AOS3-DPKG-TASK-002_Local_Bootstrap.md
limitations:
  - Acceptance applies only to the exact IDs and definition bytes represented by the bound DRAFT-R4 aggregate and accepted-subject manifest.
  - Current DRAFT-R14 carries forward the post-Y1 PSC-A-001, WFC-A-001, WFC-B-001, and WFC-C-001 definitions whose bytes differ from C1, so this decision is stale for those four current subjects.
  - Under human-selected rule A2, the current envelope-owned AC-WFC-A-001-01..07 definitions differ from their persisted C1 rows, so this decision is stale for those seven current subjects.
  - AC-WFC-B-001-01..05 and AC-WFC-C-001-01..05 are new DRAFT subjects and are not accepted by this decision.
  - SCH-PRODUCT-SPEC-001 and SCH-FEATURE-PASSPORT-001 are new DRAFT schemas outside this C1 subject set.
  - This decision does not accept Task candidates created after C1.
  - A change to any extracted accepted subject definition makes this decision stale for that subject.
  - Downstream Task additions do not stale accepted subjects when the accepted-subject manifest remains byte-identical.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# DEC-CONTRACT-001 — Stage C Contract Acceptance

## 1. Exact human decision

```yaml
gate_id: HUMAN_CONTRACT_GATE_C1
candidate_sha256: 00499af5d0f968481f0ed7e75c452bf74bf56eed380fd99d36a9a06dd8c54262
human_disposition: ACCEPT
implementation_authorization: NONE
git_authorization: NONE
```

The human accepted every requirement, contract, acceptance, and scenario ID listed below as defined in the exact candidate. This decision is the acceptance owner; authored `DRAFT` labels inside the frozen candidate remain historical source-state labels and do not override this higher-precedence human decision.

## 2. Accepted requirements

```yaml
accepted_requirement_ids:
  - REQ-CV1-001..012
  - REQ-WF-001..010
  - REQ-ARCH-001..010
count: 32
```

## 3. Accepted contracts

```yaml
accepted_contract_ids:
  - PSC-A-001
  - WFC-A-001
  - WFC-B-001
  - WFC-C-001
  - CTR-001..007
count: 11
```

Acceptance does not erase dependency states:

- `CTR-001..003` retain current C1 acceptance; corrected `PSC-A-001` and the revised complete `WFC-A-001` envelope require a new exact contract decision before either may feed a Task Brief;
- `WFC-B-001`, `WFC-C-001`, and `CTR-004..007` remain ordered by their declared dependencies;
- no contract becomes implementation, execution, validation, or Git authority.

## 4. Accepted executable acceptance IDs

```yaml
accepted_acceptance_ids:
  - AC-PSC-A-001-01..08
  - AC-WFC-A-001-01..07
  - AC-CTR-001-01..04
  - AC-CTR-002-01..05
  - AC-CTR-003-01..06
  - AC-CTR-004-01..05
  - AC-CTR-005-01..05
  - AC-CTR-006-01..05
  - AC-CTR-007-01..05
count: 50
```

## 5. Accepted scenarios

```yaml
accepted_scenario_ids:
  - SCN-001..044
count: 44
execution_state: NOT_RUN
```

Scenario acceptance means the expected behavior is accepted as a contract. It does not claim that any scenario executed or passed.

## 6. Subject-staleness rule

`AOS3-C1-SUBJECT-MANIFEST-V1` deterministically hashes:

1. each exact `REQ-*` defining table row in owners `01..03`;
2. each complete fenced contract block for `PSC-*`, `WFC-*`, and `CTR-*` in owners `01`, `02`, and `04`;
3. each exact `AC-*` defining row or contract line in owners `01`, `02`, and `04`;
4. each exact `SCN-*` defining row in owner `05`;
5. sorted manifest lines formatted as `ID<TAB>owner_path<TAB>sha256<LF>`.

The accepted subject manifest contains 137 unique entries and hashes to:

```text
2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
```

The byte-exact payload is persisted as [`C1_ACCEPTED_SUBJECT_MANIFEST.tsv`](C1_ACCEPTED_SUBJECT_MANIFEST.tsv). A later package may add decisions, derived views, Task candidates, adapters, or reports without invalidating C1 only when an extracted subject line remains identical to its persisted line. Any changed accepted definition requires a new exact human contract decision.

### 6.1 Current DRAFT-R14 acceptance projection

```yaml
original_accepted_subjects: 137
current_accepted_unchanged_subjects: 126
stale_c1_subject_bindings:
  - PSC-A-001
  - WFC-A-001
  - WFC-B-001
  - WFC-C-001
  - AC-WFC-A-001-01..07
current_changed_contract_disposition:
  PSC-A-001: DRAFT_UNACCEPTED_IN_DRAFT_R14
  WFC-A-001: DRAFT_UNACCEPTED_IN_DRAFT_R14
  WFC-B-001: DRAFT_UNACCEPTED_IN_DRAFT_R14
  WFC-C-001: DRAFT_UNACCEPTED_IN_DRAFT_R14
current_changed_acceptance_disposition:
  AC-WFC-A-001-01..07: STALE_C1_DRAFT_UNACCEPTED_IN_DRAFT_R14
new_draft_unaccepted_subjects:
  - AC-WFC-B-001-01..05
  - AC-WFC-C-001-01..05
  - SCH-PRODUCT-SPEC-001
  - SCH-FEATURE-PASSPORT-001
task_materialization_from_stale_or_new_draft_subjects: FORBIDDEN
```

This projection does not revoke the historical decision or rewrite accepted Evidence. It applies the declared staleness rule to current bytes and blocks only dependent work.

## 7. Downstream authority

```yaml
portable_task_compilation: ALLOWED_AS_DOCUMENTATION_ONLY_FROM_CURRENT_ACCEPTED_SUBJECTS
slice_a_task_compilation: BLOCKED_STALE_PSC_A_WFC_A_AC_AND_DRAFT_SCHEMAS
task_candidate_acceptance: NOT_RUN
implementation_repository: UNASSIGNED
repository_bound_enrichment: BLOCKED_PENDING_FUTURE_HUMAN_DECISION
implementation_authorization: NONE
git_authorization: NONE
```

## 8. One next action

```yaml
historical_next_action_at_decision_time: COMPILE_PORTABLE_TASK_ARTIFACTS_IN_NOTEBOOK
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
