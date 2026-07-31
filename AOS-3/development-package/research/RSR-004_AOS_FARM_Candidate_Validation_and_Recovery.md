---
artifact_id: RSR-004
artifact_type: TARGETED_REFERENCE_RESEARCH_RECORD
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R2
status: COMPLETED_WITH_LIMITATIONS
authority: NONE
exact_subject: Historical AOS-FARM candidate, validation, handoff, and unknown-operation recovery evidence for Stage C
created: '2026-07-30'
source_repository: NMF13579/AOS-FARM
source_ref: dev
source_commit: 71b87f3dfb9fe3735c7659c123cd86db3f577201
provenance:
  - ../00_Control_and_Source_Precedence.md
  - ../../../docs/05_Reference.md
  - https://github.com/NMF13579/AOS-FARM/tree/71b87f3dfb9fe3735c7659c123cd86db3f577201
upstream_links:
  - ../00_Control_and_Source_Precedence.md
downstream_links:
  - ../04_Runtime_and_Data_Contracts.md
  - ../05_Quality_Recovery_and_Security.md
limitations:
  - Exact Git objects were inspected locally; current remote dev was not refreshed.
  - Schemas, fixtures, scripts, validators, and runtime were not executed.
  - Historical topology and policy have authority NONE.
implementation_authorization: NONE
git_authorization: NONE
---

# RSR-004 — AOS-FARM Candidate, Validation, and Recovery

## Research question

Which exact historical candidate, validation, handoff, and crash-recovery constraints should inform Stage C negative and recovery contracts?

## Source boundary

```yaml
repository_url: https://github.com/NMF13579/AOS-FARM
resolved_commit: 71b87f3dfb9fe3735c7659c123cd86db3f577201
paths:
  - aos/schemas/simple-control-candidate-manifest.schema.json
  - aos/schemas/simple-control-validation-result.schema.json
  - aos/schemas/aos-handoff-summary.schema.json
  - aos/reports/runtime/aos-farm-676-package-session-and-recovery-contract-report.md
  - aos/reports/examples/evidence-to-backlog/fixtures/negative/execution-authorized-inside-candidate.md
methods:
  - git ls-tree -r --name-only <commit>
  - git show <commit>:<path>
```

## Classified findings

### `RSR-004-F001` — Candidate identity must enumerate content and reject unexpected paths

`OBSERVED_AT_SNAPSHOT`

The candidate manifest binds repository/task/candidate, expected file states, content digests and sizes, forbidden paths, unexpected-path policy, deletions, and renames.

Evidence:

- [Candidate manifest schema](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/schemas/simple-control-candidate-manifest.schema.json)

Target use: require deterministic relative-path manifests and block unexpected candidate content; do not copy its permissive `additionalProperties`.

### `RSR-004-F002` — Validation and approval remain orthogonal

`OBSERVED_AT_SNAPSHOT`

The validation result keeps validation/evidence results separate from `approval_status: NOT_PROVIDED` and fixes `execution_authorized: false`.

Evidence:

- [Simple-control validation result schema](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/schemas/simple-control-validation-result.schema.json)

Target use: preserve separate axes and required `NOT_RUN`; use the canonical AOS precedence for aggregate results.

### `RSR-004-F003` — Handoff needs negative as well as positive state

`OBSERVED_AT_SNAPSHOT`

The handoff schema requires what was done, what was not done, Evidence, validation snapshot, unknowns, workspace, next safe step, forbidden actions, and a human checkpoint.

Evidence:

- [AOS-FARM handoff summary schema](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/schemas/aos-handoff-summary.schema.json)

Target use: include these fields plus exact repository/candidate/decision/permission bindings.

### `RSR-004-F004` — Unknown operation outcome forbids automatic recovery

`REPORTED`

The inspected recovery report proposes one mutating session, external-mutation blocking, durable violation lineage, and human reconciliation for unknown operation outcomes.

Evidence:

- [Package, session, and recovery contract report](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/reports/runtime/aos-farm-676-package-session-and-recovery-contract-report.md)

Target use: treat unknown outcome and concurrent mutation as fail-closed recovery cases. Strong signing/key-custody proposals are rejected because G2 selected `LOCAL_DECLARED_HASH_BOUND`.

### `RSR-004-F005` — A candidate cannot carry execution authorization

`OBSERVED_AT_SNAPSHOT`

The negative fixture blocks a DRAFT next-task candidate that declares `execution_authorized: true`.

Evidence:

- [Execution-authorized-inside-candidate fixture](https://github.com/NMF13579/AOS-FARM/blob/71b87f3dfb9fe3735c7659c123cd86db3f577201/aos/reports/examples/evidence-to-backlog/fixtures/negative/execution-authorized-inside-candidate.md)

Target use: Task and candidate schemas must not contain authority-bearing approval fields.

## Result

```yaml
result: RESEARCH_QUESTION_ANSWERED_WITH_RUNTIME_NOT_RUN
authority: NONE
copied_solution: false
checks_not_run:
  - schema_validation
  - fixture_execution
  - runtime
historical_next_action_at_research_time: USE_AS_NON_AUTHORITATIVE_INPUT_TO_CTR_005_THROUGH_CTR_007
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
