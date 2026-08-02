---
artifact_id: AOS-PORTABLE-TASK-CANDIDATE-CONTRACT-R1
document_type: PORTABLE_TASK_CANDIDATE_CONTRACT
revision: R1
status: DRAFT
candidate_role: DRAFT_CANDIDATE
task_id: INT-DOC-010
fact_class: TASK_CANDIDATE_SCHEMA
target_binding_status: UNBOUND
implementation_repository: UNASSIGNED
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# AOS Portable Task Candidate Contract R1

## 1. Purpose and boundary

A Portable Task Candidate captures a bounded documentation-derived task before
a target repository is assigned or observed. It supports comparison, review and
later conversion. It is not a Task Brief, Execution Authorization, target
binding, implementation plan or Git permission.

```text
accepted source contracts
→ portable candidate
→ human target and material decisions
→ exact target binding
→ target-bound Task Brief
→ separate Execution Authorization
```

Any unknown target fact remains an explicit placeholder state, never an invented
repository, branch, `HEAD`, path, toolchain or command.

## 2. Canonical schema

```yaml
portable_task_candidate:
  schema_version: 1
  candidate_id: UNIQUE_STRING
  revision: POSITIVE_INTEGER
  maturity: DRAFT | HUMAN_REVIEW_REQUIRED | HUMAN_ACCEPTED | SUPERSEDED
  source_contracts:
    - path: REPOSITORY_RELATIVE_POSIX_PATH
      sha256: LOWERCASE_64_HEX
      fact_class: STRING
  purpose: NON_EMPTY_STRING
  user_outcome: NON_EMPTY_STRING
  feature_refs: [FTR-NNN]
  proposed_stage: PLAN
  scope_intent:
    included_outcomes: [NON_EMPTY_STRING]
    excluded_outcomes: [NON_EMPTY_STRING]
    candidate_artifact_kinds: [STRING]
  observable_acceptance:
    criteria: [NON_EMPTY_STRING]
    negative_scenarios: [NON_EMPTY_STRING]
    evidence_needed: [NON_EMPTY_STRING]
  dependencies:
    accepted_contracts: [EXACT_REFERENCE]
    human_decisions_required: [DECISION_ID_OR_DESCRIPTION]
    external_evidence_required: [EVIDENCE_DESCRIPTION]
  target_binding:
    status: UNBOUND
    repository: null
    worktree: null
    branch: null
    head_sha: null
    baseline: null
    allowed_paths: []
    forbidden_paths: []
    toolchain: []
  authority:
    candidate_owner: EXACT_SOURCE_OR_HUMAN_RECORD
    task_scope_owner: NOT_CREATED
    execution_authorization: NONE
    implementation_authorization: NONE
    git_authorization: NONE
  assumptions: [EXPLICIT_NON_TARGET_ASSUMPTION]
  unknowns: [EXPLICIT_UNKNOWN]
  risks: [RISK_CANDIDATE]
  validation_plan:
    required_checks: [CHECK_DESCRIPTION]
    independence_required: BOOLEAN
    expected_evidence: [EVIDENCE_DESCRIPTION]
  conversion_gate:
    readiness: READY_FOR_PORTABLE_TASK_DERIVATION | TARGET_REPOSITORY_ASSIGNMENT_REQUIRED | TARGET_BINDING_REQUIRED
    blockers: [EXACT_BLOCKER]
    one_next_action: ONE_BOUNDED_ACTION
  provenance:
    created_from_task_id: STRING
    candidate_manifest_sha256: LOWERCASE_64_HEX
  human_decision: null | ACCEPT | NEEDS_CHANGES | REJECT | DEFER
```

Null is permitted only for the five scalar target-binding fields shown while status is
`UNBOUND`. Empty strings and undocumented placeholders such as `TBD` are
invalid. A candidate accepted as documentation still has no execution authority.

## 3. Identity

Paths use repository-relative POSIX form and UTF-8 bytewise lexical order.
Source hashes are raw-file SHA-256. Construct the candidate manifest as:

```text
AOS-PORTABLE-TASK-CANDIDATE-V1<LF>
CANDIDATE<TAB><candidate-id><TAB><revision><LF>
SOURCE<TAB><path><TAB><sha256><TAB><fact-class><LF>
FEATURE<TAB><feature-id><LF>
DECISION_REQUIRED<TAB><decision><LF>
EVIDENCE_REQUIRED<TAB><evidence><LF>
TARGET_STATUS<TAB>UNBOUND<LF>
AUTHORIZATION<TAB>NONE<TAB>NONE<TAB>NONE<LF>
```

Repeated records are UTF-8-byte sorted. `candidate_manifest_sha256` is the
SHA-256 of the complete LF-terminated bytes. Any semantic or source-byte change
creates a new revision and identity.

## 4. Admissible source content

The candidate may copy exact bounded requirements from their authoritative
owners and may synthesize a traceable task outcome. It may not:

- select a product feature, first slice, architecture or implementation target;
- turn dossier shared defaults into feature-specific facts;
- inherit topology, dependencies or readiness from legacy/reference repositories;
- invent target paths, commands, tests, dependencies or Risk Profile;
- claim observed runtime behavior without subject-bound Evidence;
- authorize `EXECUTE` or any Git action.

## 5. Readiness rules

| Condition | Readiness | One next route |
|---|---|---|
| source contracts insufficient | `NOT_READY` in enclosing gate record | resolve exact documentation gap |
| documentation sufficient; candidate may be derived | `READY_FOR_PORTABLE_TASK_DERIVATION` | separately authorize candidate derivation |
| candidate exists; implementation repository unassigned | `TARGET_REPOSITORY_ASSIGNMENT_REQUIRED` | human assigns exact repository role/target |
| repository assigned but current identity/path facts absent | `TARGET_BINDING_REQUIRED` | read-only target preflight |
| target facts and required decisions bound | outside this contract | use Target Binding and Task Conversion Protocol |

## 6. Validation requirements

Required validation is `L0 + L1 + L2`:

- schema and identity are deterministic;
- every source claim traces to an owner and exact hash;
- all target facts remain null/empty exactly as permitted while unbound;
- acceptance and negative scenarios are executable in principle without
  selecting a toolchain;
- authority and Git boundaries remain `NONE`;
- a cold-start agent identifies every blocker and one next action without chat.

## 7. Negative cases

1. `repository`, `branch` or `HEAD` invented from a reference repository → `FAIL`.
2. portable candidate called a Task Brief or Execution Authorization → `FAIL`.
3. `human_disposition` inferred from coverage → `CONTRACT_VIOLATION`.
4. empty target field represented by a plausible fake value → `FAIL`.
5. source changed without revision/manifest change → `CONFLICT`.
6. required human decision hidden as an assumption → `BLOCKED`.
7. `PASS` or human acceptance interpreted as implementation permission → `CONTRACT_VIOLATION`.
8. absolute local path or credential-bearing locator included → `FAIL`.
9. target-specific test command added before toolchain observation → `UNKNOWN` or `FAIL`.
10. candidate automatically converted or activated → `BLOCKED`.

## 8. Status

```yaml
technical_result: NOT_RUN
readiness: NOT_READY
human_decision: null
implementation_authorization: NONE
git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
```
