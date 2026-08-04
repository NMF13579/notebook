---
artifact_id: AOS-TARGET-BINDING-AND-TASK-CONVERSION-PROTOCOL-R1
document_type: TARGET_BINDING_AND_TASK_CONVERSION_PROTOCOL
revision: R1
status: DRAFT
candidate_role: DRAFT_CANDIDATE
task_id: INT-DOC-010
fact_class: TASK_CONVERSION_PROTOCOL
portable_candidate_contract: planning/AOS_Portable_Task_Candidate_Contract_R1.md
task_brief_contract_owner: docs/02_Architecture.md
workflow_owner: docs/03_Development.md
implementation_repository: UNASSIGNED
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# AOS Target Binding and Task Conversion Protocol R1

## 1. Purpose and authority boundary

This protocol converts one exact Portable Task Candidate into one target-bound
Task Brief only after the target and every material product/architecture
decision are supplied by their owners. Conversion is a bounded `PLAN` action.
It neither implements the task nor creates Execution Authorization.

```text
portable candidate
→ resolve protected human decisions
→ observe exact target read-only
→ reconcile candidate with target
→ produce DRAFT target-bound Task Brief
→ independent validation when required
→ human execution decision
```

The protocol cannot assign the implementation repository, select architecture,
change feature disposition, mint authority or activate a task.

## 2. Required inputs

```yaml
conversion_request:
  conversion_id: UNIQUE_STRING
  portable_candidate:
    path: REPOSITORY_RELATIVE_POSIX_PATH
    sha256: LOWERCASE_64_HEX
    manifest_sha256: LOWERCASE_64_HEX
    human_decision_record: EXACT_REFERENCE_OR_NULL
  target_decision:
    repository_role_decision: EXACT_HUMAN_RECORD
    repository_locator: NON_SECRET_LOCATOR
    intended_branch_or_ref: STRING
  required_product_decisions: [EXACT_HUMAN_RECORD]
  required_architecture_decisions: [EXACT_ACCEPTED_ADR_OR_NO_ADR_REQUIRED_RECORD]
  requested_stage: PLAN
  mutation_authorization: NONE
  git_authorization: NONE
```

If a required record is absent, ambiguous, stale or not bound to the exact
subject, return `BLOCKED`; do not choose a value.

## 3. Read-only target preflight

Observe at one timestamp:

- repository root and repository role;
- worktree identity and nested repository boundaries;
- branch or detached state and exact `HEAD`;
- baseline, staged, unstaged and untracked state;
- relevant existing paths, symlinks and case behavior;
- instruction files and exact authority scope;
- toolchain/dependency evidence required for planning;
- sandbox, network, data/provider and secret boundaries;
- conflicts with the candidate's included/excluded outcomes.

All mutable facts are `OBSERVED_AT_SNAPSHOT`. Remote URLs are redacted. A dirty
worktree is classified as in-scope task state, out-of-scope user state,
environment noise, generated disposable state or material unknown; it is not
automatically cleaned or treated as a global blocker.

## 4. Reconciliation matrix

| Candidate element | Target observation | Conversion action |
|---|---|---|
| purpose and user outcome | no conflict | preserve verbatim or traceably normalize |
| included/excluded outcome | conflict with accepted owner | `CONFLICT`; stop affected conversion |
| target paths | observed and within repository role | normalize exact allowlist/denylist |
| toolchain/checks | observed from target | bind commands and provenance |
| required architecture | accepted ADR present | reference exact record |
| architecture materially required but absent | none | `BLOCKED`; human decision |
| feature-specific behavior still generic | no accepted contract | `BLOCKED`; contract gap |
| unrelated dirty state | classified out of scope | preserve and list explicitly |
| implementation or Git permission | absent | keep `NONE` / `NOT_RUN` |

No candidate field outranks an accepted target owner. No target observation
silently changes the candidate's product outcome.

## 5. Target-bound Task Brief mapping

The output conforms to C-005 in [Architecture](../docs/02_Architecture.md):

```yaml
task_brief:
  schema_version: 1
  task_id: UNIQUE_STRING
  source_candidate_identity: PATH_SHA256_AND_MANIFEST
  goal: FROM_PORTABLE_CANDIDATE
  user_outcome: FROM_PORTABLE_CANDIDATE
  feature_id: FTR-NNN_OR_NULL
  stage: PLAN
  repository_identity:
    root: OBSERVED_REPOSITORY_ROOT
    repository_role: HUMAN_DECIDED_ROLE
  worktree: OBSERVED_WORKTREE
  branch: OBSERVED_BRANCH_OR_DETACHED
  HEAD: LOWERCASE_40_HEX
  baseline: EXACT_BASELINE
  scope:
    allowed_paths: [OBSERVED_REPOSITORY_RELATIVE_POSIX_PATH]
    forbidden_paths: [OBSERVED_REPOSITORY_RELATIVE_POSIX_PATH]
  allowed_operations: [PLAN_OPERATION]
  forbidden_operations: [IMPLEMENTATION, COMMIT, PUSH, MERGE, RELEASE]
  assumptions: [TRACEABLE_ASSUMPTION]
  unknowns: [EXPLICIT_UNKNOWN]
  proposed_Risk_Profile: STRING_OR_NULL
  assigned_Risk_Profile: UNASSIGNED
  validation_matrix:
    - criterion: NON_EMPTY_STRING
      method: EXACT_OBSERVED_OR_CONTRACT_DERIVED_METHOD
      evidence_required: NON_EMPTY_STRING
  stop_conditions: [NON_EMPTY_STRING]
  authority:
    execution_authorization: NONE
    implementation_authorization: NONE
    git_authorization: NONE
```

The human assigns Risk Profile separately. The generated Task Brief remains
`stage: PLAN`; execution requires an exact C-006 record bound to the final brief
and current target identity.

## 6. Conversion result and identity

The conversion report records input candidate identity, all decision-record
identities, before/after repository observations, normalized mappings, rejected
candidate fields, conflicts, unknowns, checks, and output Task Brief hash.

```text
AOS-TARGET-BOUND-TASK-BRIEF-V1<LF>
SOURCE_CANDIDATE<TAB><path><TAB><raw-file-sha256><TAB><source-candidate-manifest-sha256><LF>
TASK<TAB><task-id><LF>
TARGET<TAB><repository-id><TAB><worktree><TAB><branch-or-detached><TAB><head-sha><LF>
REPOSITORY_ROLE<TAB><human-decided-role><LF>
BASELINE<TAB><exact-baseline><LF>
DECISION<TAB><record-path><TAB><sha256><LF>
TOOLCHAIN<TAB><observed-toolchain-record><LF>
ALLOWED_PATH<TAB><path><LF>
FORBIDDEN_PATH<TAB><path><LF>
CHECK<TAB><criterion-id><TAB><method-id><LF>
AUTHORIZATION<TAB>NONE<TAB>NONE<TAB>NONE<LF>
```

Repeated `DECISION`, `TOOLCHAIN`, path and `CHECK` records use ascending UTF-8
byte order inside their record kind. The three authorization values bind
execution, implementation and Git authorization in that order. The manifest is
raw-byte SHA-256 bound. Any candidate, target, repository-role, baseline,
decision, path, toolchain, check or authority change invalidates conversion and
requires fresh read-only reconciliation.

## 7. Result routing

| Observed result | Readiness | One next action |
|---|---|---|
| target not human-assigned | `TARGET_REPOSITORY_ASSIGNMENT_REQUIRED` | human assigns exact implementation repository role |
| assigned target not observed or stale | `TARGET_BINDING_REQUIRED` | repeat read-only target preflight |
| material product/architecture decision missing | `NOT_READY` | human resolves the exact decision |
| feature-specific contract incomplete | `NOT_READY` | author and review exact contract under separate task |
| conversion checks sufficient | `READY_FOR_TARGET_BOUND_TASK_BRIEF` | human reviews exact Task Brief and execution boundary |

`READY_FOR_TARGET_BOUND_TASK_BRIEF` permits planning only. It is not
`READY_FOR_IMPLEMENTATION_HUMAN_DECISION` unless all separately owned planning
and validation gates required by the exact task have also closed.

## 8. Failure and recovery

- mismatch before output publication: write nothing and report `FAIL` or `BLOCKED`;
- partial output: preserve inventory, stop, and require a bounded recovery task;
- subject changes after freeze: invalidate result and re-observe;
- unknown protected decision: stop for human decision;
- changed scope/owner/repository role: new explicit task required;
- validator finding: separate correction `EXECUTE`, never mutate in `VALIDATE`.

## 9. Negative cases

1. repository inferred from the notebook or a legacy URL;
2. target paths invented before observation;
3. generic dossier defaults treated as a complete Feature Contract;
4. candidate acceptance treated as task execution approval;
5. architecture option selected by the converter;
6. Risk Profile assigned by the agent;
7. dirty user state cleaned or staged;
8. stale `HEAD` reused after repository mutation;
9. Commit, Push, Merge or Release bundled with conversion;
10. next task activated automatically.

Each case must fail closed for the affected action and preserve one bounded next
human or technical route.

## 10. Status

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
