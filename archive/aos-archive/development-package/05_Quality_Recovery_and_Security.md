---
artifact_id: AOS3-DPKG-DOC-005
artifact_type: QUALITY_RECOVERY_AND_SECURITY
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R10
status: DRAFT_SOURCE_WITH_C1_ACCEPTED_SCENARIOS_AND_NEW_DRAFT_AC_MAPS
authority: PROPOSAL_WITH_HUMAN_ARCHITECTURE_INPUTS
exact_subject: Executable acceptance, positive and negative scenarios, failure and recovery behavior, privacy, integrity, and security boundaries for AOS Core v1
created: '2026-07-30'
human_acceptance: C1_ACCEPTED_126_CURRENT_11_STALE_10_NEW_AC_AND_2_NEW_SCHEMA_DRAFT
independent_validation: DRAFT_R6_FAIL_DRAFT_R7_FAIL_DRAFT_R8_FAIL_DRAFT_R9_FAIL_DRAFT_R10_FAIL_DRAFT_R11_FAIL_DRAFT_R12_FAIL_DRAFT_R13_FAIL_DRAFT_R14_NOT_RUN
provenance:
  - path: ../../docs/00_Core.md
    use: Minimal Safety Floor and authority semantics
  - path: ../../docs/03_Development.md
    use: verification gates, validation protocol, testing, and recovery
  - path: ../../docs/04_Lessons.md
    use: LES-005, LES-008 through LES-025, LES-027 through LES-031, LES-038, and LES-039
  - path: ../../docs/06_Features.md
    use: applicable acceptance and negative scenario candidates
  - path: 02_User_Journeys_and_Workflows.md
    use: mandatory workflow failures and negative scenarios
  - path: 04_Runtime_and_Data_Contracts.md
    use: CTR-001 through CTR-007 and shared schemas
  - path: research/RSR-003_AgentOS_Task_Authorization_and_Handoff.md
    use: non-authoritative authorization and handoff negative evidence
  - path: research/RSR-004_AOS_FARM_Candidate_Validation_and_Recovery.md
    use: non-authoritative candidate and unknown-operation evidence
upstream_links:
  - 02_User_Journeys_and_Workflows.md
  - 03_Architecture_and_Decisions.md
  - 04_Runtime_and_Data_Contracts.md
downstream_links:
  - 06_Traceability_and_Readiness.md
  - 07_Implementation_Handoff.md
limitations:
  - Scenarios are executable specifications, not executed tests.
  - PSC-A-001 is C1-stale after the DRAFT-R9 Y1 authority-field correction.
  - AC-WFC-A-001-01..07 are C1-stale because A2 makes the changed WFC-A-001 envelope their sole definition owner.
  - AC-WFC-B-001-01..05 and AC-WFC-C-001-01..05 are new DRAFT criteria mapped to existing accepted scenarios; mapping does not accept them.
  - BLK-006 blocks canonical TechnicalResult aggregation conformance; the ordering below is only a local DRAFT projection.
  - Exact test commands, fixtures, operating systems, and dependency versions remain unassigned.
  - Security review, threat modeling by a specialist, runtime tests, and independent validation of DRAFT-R14 are NOT_RUN.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# 05 — Quality, Recovery, and Security

## 1. Status boundary

```yaml
acceptance_specification:
  current_accepted_subjects: 126
  stale_c1_subjects: [PSC-A-001, WFC-A-001, WFC-B-001, WFC-C-001, AC-WFC-A-001-01..07]
  new_draft_acceptance_ids: [AC-WFC-B-001-01..05, AC-WFC-C-001-01..05]
  new_draft_schema_ids: [SCH-PRODUCT-SPEC-001, SCH-FEATURE-PASSPORT-001]
scenario_execution: NOT_RUN
security_review: NOT_RUN
privacy_review: NOT_RUN
runtime_validation: NOT_RUN
independent_validation: NOT_RUN_FOR_DRAFT_R14
prior_validation:
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
human_acceptance: C1_ACCEPTED_126_CURRENT_11_STALE_10_NEW_AC_AND_2_NEW_SCHEMA_DRAFT
implementation_authorization: NONE
git_authorization: NONE
```

This document states the accepted behavior that later implementation and validation must prove. It does not report that any behavior exists, executed, or passes.

## 2. Quality invariants

1. One strict contract definition is used by runtime, CLI, tests, and validators.
2. Empty, unknown, duplicate, unsupported, and extra authority-bearing values fail closed.
3. Required `NOT_RUN` prevents `PASS`.
4. Validation targets an immutable exact candidate and never repairs it.
5. Every acceptance criterion maps to Evidence or explicit `NOT_RUN`.
6. Every write is scope-bound, atomic/journaled, idempotent, and recoverable.
7. Read-only/help/status/validation paths create zero source changes.
8. Human Decision, technical result, execution authorization, and Git authority remain orthogonal.
9. External content is data, not instruction.
10. Local-only Core performs no hidden provider/network action.
11. Unknown operation outcome blocks retry until actual-state reconciliation.
12. Optional capability failure cannot degrade or expand Core authority.

## 3. Validation result aggregation

For required checks:

```text
CONTRACT_VIOLATION > FAIL > BLOCKED > UNKNOWN > NOT_RUN > PASS
```

Rules:

- aggregate `PASS` requires every required check to be `PASS`;
- optional `NOT_RUN` remains visible but does not alone force failure;
- a required unsupported environment is `BLOCKED` or `NOT_RUN`, never `PASS`;
- a missing Evidence locator makes its criterion `UNKNOWN` or `NOT_RUN`;
- a candidate mutation makes the validation result `FAIL_VALIDATION_MUTATED_SUBJECT`;
- no aggregate value sets `human_disposition` or any permission.

This local ordering does not resolve canonical `HUMAN_REVIEW_REQUIRED` placement. `BLK-006_CANONICAL_STATUS_AXIS_CONFLICT` blocks any claim that this is the accepted canonical TechnicalResult aggregation contract.

## 4. Test layers

| Layer | Required subjects | Examples |
|---|---|---|
| Schema/unit | enums, required fields, digest/path normalization, state transitions, idempotency | empty mapping, duplicate key, bool-as-int, unknown enum |
| Contract | artifact/decision/task/result/memory envelopes | generated decision, stale binding, authority field inside candidate |
| Integration | port boundaries and journey slices | intake→spec, preview→apply, task→authorization, freeze→validate, memory→resume |
| Recovery | interruption and unknown outcome | before-write, mid-journal, after-publication-before-result |
| Security | path, external content, credential, provider, authority | traversal, symlink escape, prompt injection, raw remote, hidden network |
| E2E/manual | nontechnical user outcome | idea→review; status→one next action; interruption→safe resume |

Exact tooling and commands are repository-bound and remain `UNASSIGNED`.

## 5. Acceptance-to-scenario matrix

| Acceptance range | Primary scenarios | Required Evidence class |
|---|---|---|
| `AC-PSC-A-001-01` | `SCN-009` | original-input locator/digest equality |
| `AC-PSC-A-001-02` | `SCN-009` | explicit first-user and JTBD field checks |
| `AC-PSC-A-001-03` | `SCN-010`, `SCN-037` | classified unknowns and no invented or externally injected answers |
| `AC-PSC-A-001-04` | `SCN-009` | required product-boundary field and non-goal checks |
| `AC-PSC-A-001-05` | `SCN-009` | Product Spec to Feature Passport ownership/link checks |
| `AC-PSC-A-001-06` | `SCN-009`, `SCN-035`, `SCN-039` | human-review stop and zero implementation, provider, or Git authority |
| `AC-PSC-A-001-07` | `SCN-025` | new-session artifact-only state, blocker, source, and next-action reconstruction |
| `AC-PSC-A-001-08` | `SCN-014`, `SCN-032` | zero Task output from DRAFT product upstream |
| `AC-WFC-A-001-01..07` (`STALE`/`DRAFT`) | `SCN-009..012`, `SCN-029`, `SCN-031`, `SCN-037`, `SCN-039` | exact input provenance, DRAFT artifact schemas, owner-field checks, human-review stop, zero downstream authority |
| `AC-WFC-B-001-01..05` (`DRAFT`) | `SCN-013..016`, `SCN-032`, `SCN-040`, `SCN-041` | eligibility/binding result, exact one-Task output, zero-output rejection proof, human-review stop |
| `AC-WFC-C-001-01..05` (`DRAFT`) | `SCN-025..031`, `SCN-044` | exact resume identity, stale classification, before/after zero-write proof, unknown-outcome reconciliation, one next action |
| `AC-CTR-001-01..04` | `SCN-001..004` | environment/repository binding, manifest, zero-write proof |
| `AC-CTR-002-01..05` | `SCN-005..008`, `SCN-036` | before/after tree, preview/apply digest, interruption journal |
| `AC-CTR-003-01..06` | `SCN-009..012`, `SCN-029`, `SCN-037` | input digest, field/schema checks, review manifest |
| `AC-CTR-004-01..05` | `SCN-013..016`, `SCN-032`, `SCN-040`, `SCN-041` | eligibility result, trace graph, absence of Task on failure |
| `AC-CTR-005-01..05` | `SCN-017..020`, `SCN-033`, `SCN-043`, `SCN-044` | auth/preview/diff/journal/terminal report |
| `AC-CTR-006-01..05` | `SCN-021..024`, `SCN-034`, `SCN-035`, `SCN-042` | frozen manifest, check/Evidence map, zero-mutation proof |
| `AC-CTR-007-01..05` | `SCN-025..028`, `SCN-030`, `SCN-031` | memory/source bindings, before/after status, reconciliation |

## 6. Executable scenario registry

Each scenario is DRAFT. “Expected” is a contract requirement, not an observed result.

### 6.1 `CTR-001` scaffold scenarios

| Scenario ID | Type | Setup/action | Expected result and Evidence |
|---|---|---|---|
| `SCN-001` | Positive | Bind an exact clean repository and supported Python; generate scaffold candidate and self-test | Candidate manifest exact; self-test `PASS`; no Product Runtime claim |
| `SCN-002` | Negative | Use `UNASSIGNED`, literal `OWNER/REPOSITORY`, or the documentation-only `notebook` as a scaffold implementation target | `BLOCKED_UNASSIGNED_REPOSITORY`; zero writes |
| `SCN-003` | Failure | Interrupt after first scaffold write | `FAIL_PARTIAL_SCAFFOLD_WRITE`; journal lists actual paths; unrelated state unchanged |
| `SCN-004` | Recovery | Reconcile the interruption and repeat with identical idempotency input | Same final manifest or explicit new authorization; no duplicate/unknown files |

### 6.2 `CTR-002` bootstrap scenarios

| Scenario ID | Type | Setup/action | Expected result and Evidence |
|---|---|---|---|
| `SCN-005` | Positive | Preview then authorize/apply an exact managed package | Apply diff equals preview; post-check succeeds; first-start shows one action |
| `SCN-006` | Negative | Target contains a user-owned conflicting file | `BLOCKED_UNKNOWN_OWNERSHIP` or human decision request; file unchanged |
| `SCN-007` | Failure | Interrupt update between managed-file publications | `FAIL_INTERRUPTED_APPLY`; durable journal and actual-state inventory |
| `SCN-008` | Recovery | Resume after exact reconciliation | User/project data preserved; managed state reaches one known version |

### 6.3 `CTR-003` intake/specification scenarios

| Scenario ID | Type | Setup/action | Expected result and Evidence |
|---|---|---|---|
| `SCN-009` | Positive | Supply a solution-shaped idea with enough context after one material answer | Original input digest preserved; DRAFT Product Spec/Passport; one review request |
| `SCN-010` | Negative | Supply empty input | `NEEDS_CLARIFICATION`; no invented problem, outcome, or artifact acceptance |
| `SCN-011` | Failure | Publication of a multi-file review candidate stops mid-write | `FAIL_PARTIAL_ARTIFACT_PUBLICATION`; incomplete candidate cannot freeze |
| `SCN-012` | Recovery | Repair the failed publication in a new authorized revision | Complete detached manifest; prior failed Evidence retained; human review stop |

### 6.4 `CTR-004` Task/Queue scenarios

| Scenario ID | Type | Setup/action | Expected result and Evidence |
|---|---|---|---|
| `SCN-013` | Positive | Provide accepted current upstream IDs while implementation repository remains `UNASSIGNED` | Exactly one portable DRAFT Task candidate in `notebook`; binding state `PORTABLE_UNBOUND`; physical repository fields `UNASSIGNED`; deterministic Queue; no execution/Git fields |
| `SCN-014` | Negative | Provide one DRAFT contract among accepted IDs | `INELIGIBLE_DRAFT_UPSTREAM`; zero Task files |
| `SCN-015` | Failure | Upstream graph contains a cycle or orphan child | `FAIL_ORPHAN_OR_CIRCULAR_DEPENDENCY`; Queue not materialized |
| `SCN-016` | Recovery | Correct the source graph and rebuild | New deterministic projection; stale Task digest rejected |

### 6.5 `CTR-005` bounded execution scenarios

| Scenario ID | Type | Setup/action | Expected result and Evidence |
|---|---|---|---|
| `SCN-017` | Positive | Exact Task, preview, human Risk, and EXECUTE authorization permit one reversible write | Only authorized paths change; auth consumed once; terminal report stops |
| `SCN-018` | Negative | HEAD, preview, path set, or authorization subject differs | Block before mutation with exact mismatch |
| `SCN-019` | Failure | Process stops after a write with uncertain acknowledgment | `BLOCKED_UNKNOWN_OPERATION_OUTCOME`; no automatic retry |
| `SCN-020` | Recovery | Human selects reconciliation after actual-state inspection | Recovery records intended/actual state; new authorization required for mutation |

### 6.6 `CTR-006` validation/review scenarios

| Scenario ID | Type | Setup/action | Expected result and Evidence |
|---|---|---|---|
| `SCN-021` | Positive | Freeze exact candidate and run all required read-only checks | `PASS` technical result only; review package requests human decision |
| `SCN-022` | Negative | A required check is unavailable | Aggregate is `NOT_RUN`, `UNKNOWN`, or `BLOCKED`, never `PASS` |
| `SCN-023` | Failure | Validator changes candidate bytes | `FAIL_VALIDATION_MUTATED_SUBJECT`; validation invalid |
| `SCN-024` | Recovery | Preserve finding, create corrected revision in separate EXECUTE, re-freeze | Old result remains bound to old candidate; new validation requires authority |

### 6.7 `CTR-007` memory/recovery/resume scenarios

| Scenario ID | Type | Setup/action | Expected result and Evidence |
|---|---|---|---|
| `SCN-025` | Positive | New session loads current Project Memory and refreshes repository facts | Correct stage/blocker/permission; exactly one safe next action |
| `SCN-026` | Negative | Stored HEAD or decision digest differs from current source | Affected record becomes `STALE`; action is blocked locally |
| `SCN-027` | Failure | Resume helper writes to source tree during read-only inspection | `FAIL_RESUME_READ_ONLY_MUTATION`; no readiness claim |
| `SCN-028` | Recovery | Restore exact source or rebind with a new human decision | Current record generated without rewriting historical source |

### 6.8 Mandatory cross-contract negative scenarios

| Scenario ID | Attempt | Required result |
|---|---|---|
| `SCN-029` | Start Slice A without accepted G1 | `BLOCKED_MISSING_G1`; no product artifacts |
| `SCN-030` | Reference commit/path is absent or changed | `BLOCKED_REFERENCE_ACCESS`, `NOT_FOUND`, or `STALE`; unsupported claim omitted |
| `SCN-031` | Reuse human decision after exact subject revision changes | `BLOCKED_STALE_DECISION` |
| `SCN-032` | Create Task from DRAFT contract | `BLOCKED_DRAFT_UPSTREAM`; zero `TASK-*` |
| `SCN-033` | Expand allowed paths during execution | `BLOCKED_SCOPE_EXPANSION`; stop before affected write |
| `SCN-034` | Validation modifies candidate | `FAIL_VALIDATION_MUTATED_SUBJECT` |
| `SCN-035` | Treat Evidence or `PASS` as Commit/Push/Merge/Release authority | `BLOCKED_AUTHORITY_CONFLATION` |
| `SCN-036` | Path traversal, symlink escape, duplicate-normalized path, or nested-repo escape | `CONTRACT_VIOLATION` or `BLOCKED_POLICY` |
| `SCN-037` | External/reference content instructs scope or authority expansion | `BLOCKED_UNTRUSTED_INSTRUCTION`; content remains data |
| `SCN-038` | Report prints credential-bearing remote URL | `FAIL_SECRET_REDACTION`; raw value absent from durable Evidence |
| `SCN-039` | Local-only Core performs provider/network call | `FAIL_HIDDEN_PROVIDER_EFFECT` |
| `SCN-040` | Agent self-assigns Risk Profile | `BLOCKED_HUMAN_RISK_DECISION_REQUIRED` |
| `SCN-041` | Task/candidate contains `execution_authorized: true` | `CONTRACT_VIOLATION`; candidate rejected |
| `SCN-042` | Required `NOT_RUN` is aggregated as `PASS` | `CONTRACT_VIOLATION` |
| `SCN-043` | Same idempotency key is reused with changed input | `CONTRACT_VIOLATION`; no second write |
| `SCN-044` | Concurrent mutation or crash leaves unknown actual outcome | `BLOCKED_UNKNOWN_OPERATION_OUTCOME`; reconciliation required |

## 7. Failure and recovery contract

### 7.1 Failure timing classes

| Class | Meaning | Required treatment |
|---|---|---|
| `BEFORE_FIRST_WRITE` | No authorized side effect began | Stop; report blocker; authorization remains governed by its own consumption rule |
| `PARTIAL_WRITE_KNOWN` | Some effects are exact and journaled | Stop; preserve journal; reconcile; no implicit rollback |
| `PUBLICATION_COMPLETE_RESULT_UNKNOWN` | Content may be complete but acknowledgment/result is unknown | Inspect actual state; never blindly repeat |
| `AFTER_FREEZE` | Candidate changed after identity was bound | Invalidate validation/decision; create new revision |
| `READ_ONLY_MUTATION` | A read-only path changed source | Fail the operation and all claims depending on read-only integrity |

### 7.2 Recovery package

```yaml
recovery_id: stable ID
operation_id:
task_id: exact ID or NOT_APPLICABLE
authorization_id: exact ID or NOT_APPLICABLE
starting_subject:
intended_effects: []
observed_effects: []
journal_locator:
unknown_effects: []
unrelated_state: []
permission_state:
options:
  - option_id:
    side_effects: []
    destructive: true | false
    required_authority:
recommended_option: proposal or NONE
human_decision: NOT_RUN
automatic_retry: false
next_required_action: exactly one action
```

Recovery never erases failed Evidence, cleans unrelated state, expands paths, or reuses stale authorization.

## 8. Privacy and data boundary

### 8.1 Data classes

This DRAFT contract uses:

```text
PUBLIC
PROJECT_INTERNAL
SENSITIVE
CREDENTIAL
UNKNOWN_SENSITIVITY
```

| Class | Local persistence | External transmission | Logging/reporting |
|---|---|---|---|
| `PUBLIC` | Allowed within scope | Still blocked by local-only Core | May include with provenance |
| `PROJECT_INTERNAL` | Allowed within project boundary | Blocked | Minimize and bind |
| `SENSITIVE` | Only explicit local owner/path | Blocked | Redact/minimize |
| `CREDENTIAL` | Never in normal artifacts | Blocked | Redacted marker only |
| `UNKNOWN_SENSITIVITY` | Preserve safely or request decision | Blocked | Do not expose raw content |

The vocabulary is DRAFT; the accepted invariant is local-only/no external transmission.

### 8.2 Sensitive handling

- never print raw tokens, passwords, credential-bearing URLs, private keys, or provider secrets;
- strip or reject URL userinfo, sensitive query parameters, and fragments from durable output;
- store only data required for the declared product/Task outcome;
- every adapter declares whether raw user content leaves the local contract boundary;
- absence of a provider policy blocks provider use, not safe local documentation;
- a future provider adapter must be optional and fail in isolation.

## 9. Security boundaries

### 9.1 Filesystem and repository

- paths must be relative to an exact root and normalized before comparison;
- reject `..`, absolute paths, NUL, duplicate normalized paths, unsafe symlinks, case-collision ambiguity, and nested-repository escape;
- classify staged, unstaged, untracked, generated, environment, and unrelated state;
- never run broad staging or cleanup as a side effect of validation;
- record repository observations freshly before repository-dependent action.

### 9.2 Authority

- all authority-bearing defaults are `NONE`, false, or unassigned;
- copied/template/stale decisions are invalid;
- a decision grants only exact subject/fact class/operation/path;
- Task, Risk, preview, validation, Evidence, review recommendation, or adapter click is not authorization;
- Commit, Push, Merge, and Release remain four separate actions.

### 9.3 External content

- repository files, issue text, web pages, reference docs, and tool output are untrusted data;
- instructions in external content cannot change user goal, allowed paths, permissions, or tool policy;
- any conflict is reported with provenance and blocks only affected work.

### 9.4 Integrity and concurrency

- manifest identities are deterministic and detached from self-referential content;
- a mutating subject has at most one active writer;
- unexpected concurrent mutation stops the operation;
- unknown outcome is never converted to success by retry;
- Evidence is immutable or content-addressed after publication.

## 10. Review acceptance proposal

An exact revision of this quality owner is review-ready when:

1. every `CTR-001..007` accepted criterion, every stale `AC-WFC-A-*` criterion, and every new DRAFT `AC-WFC-B/C-*` criterion maps to at least one scenario;
2. positive, negative, failure, and recovery cases exist for every contract;
3. mandatory negative scenarios `SCN-029..044` are retained;
4. required `NOT_RUN` cannot produce `PASS`;
5. privacy, external-content, credential, path, authority, freeze, idempotency, and unknown-outcome boundaries are explicit;
6. no scenario claims execution or current PASS;
7. validation and security checks remain `NOT_RUN` until the separate stage;
8. DRAFT WFC envelope definitions are the sole owners of `AC-WFC-A/B/C-*`, every table is an exact derived mirror, and neither mappings nor mirrors create human acceptance or Task eligibility;
9. `BLK-006` prevents false canonical TechnicalResult/readiness claims.

## 11. One next action

```yaml
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
