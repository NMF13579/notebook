---
document_type: AOS_CORE_CONTRACT_SLICE
contract_family: AOS_CORE_CONTRACT
contract_slice: C5_C7
revision: DRAFT-R1
status: HUMAN_REVIEW_REQUIRED
claim_class: DRAFT_CONTRACT_CANDIDATE
authority: NONE_UNTIL_HUMAN_ACCEPTANCE
authority_scope:
  - C5_REGISTRIES_AND_CONTEXT_PACK
  - C6_TASK_LOCAL_COORDINATOR
  - C7_PRODUCT_RECOVERY_AND_SCOPED_EXECUTOR_FOUNDATION
task_id: DOC-008
technical_result: PASS
readiness: READY_FOR_FINAL_PACKAGE_REVIEW
human_acceptance: NOT_RUN
provisional_dependencies:
  - AOS_CORE_CONTRACT_R1.md@24f1af001bc0249d9c8e40a9608c2c5b67ea047bf2307cbda251f184b223d5db
  - AOS_CORE_CONTRACT_C012_V2_R1.md@5e6f5ad2250167f4d71ee470b3a570e867fd6bc4a2eec79d5a2fffaace49b52d
  - AOS_CORE_CONTRACT_C3_C4_R1.md@7716d22f18daf1017d7a8659fc9625d8714b58cb72855a015f976bae92233821
nearest_unimplemented_task: Task-001-Scaffolding.md
new_implementation_task_created: false
implementation_repository_creation: NOT_RUN
execution_authorization: NOT_RUN
git_authorization: NONE
created: 2026-08-05
---

# AOS-3 — Core Contract C5–C7 R1

## 1. Назначение и dependency boundary

Этот candidate определяет три оставшихся core fact classes:

- `C5`: два derived registry и deterministic task-scoped Context Pack;
- `C6`: pure task-local coordinator с конечной таблицей переходов;
- `C7`: journal/reconciliation/recovery/freeze foundation для будущего scoped executor.

Он потребляет принятый `C1–C2` exact subject, current provisional `C-012 v2.0.0` correction и технически проверенный, но не принятый `C3–C4` candidate. Provisional dependency не получает `HUMAN_ACCEPTED` через использование. При финальном `NEEDS_CHANGES` затронутые downstream candidates должны быть пересчитаны.

`C5–C7` не выбирают следующую product feature, не создают Task Brief, не запускают executor и не меняют item-level feature dispositions.

## 2. Shared invariants

1. Registries, indexes, Context Packs, coordinator outputs and journals have only their declared local fact classes.
2. None can create product truth, human acceptance or permission.
3. Current lifecycle remains owned only by `.aos/state/project-memory.json` under C3.
4. All record references strict-load through C1; all action classification goes through C2.
5. Every mutation is exact-task/subject/repository/preview/authorization bound.
6. Missing/stale required input returns a named non-PASS state; no inference from chat or filenames.
7. Feature dossiers with no current human disposition remain unselected; documenting safety mechanics does not select the full feature.

## 3. C5 — Registries

### 3.1. Registry classes and paths

```yaml
registries:
  product_feature:
    path: .aos/index/product-features.json
    schema_version: aos.product-feature-registry.v1
    authority: NONE_DERIVED
  execution_verification:
    path: .aos/index/execution-verification.json
    schema_version: aos.execution-verification-registry.v1
    authority: NONE_DERIVED
index_root:
  ownership: GENERATED_REBUILDABLE
  current_state_owner: false
```

Creating/updating these paths is a repository write and requires an exact authorized Task Brief. Read-only commands may diagnose missing/stale indexes but must not rebuild them.

### 3.2. Product Feature Registry schema

```text
ProductFeatureRegistry = {
  schema_version: "aos.product-feature-registry.v1"!,
  generated_at: UtcTimestamp!,
  source_set_digest: Sha256!,
  sources: list<RegistrySource>!,
  entries: list<ProductFeatureEntry>!,
  limitations: list<NonEmptyText>!
}

RegistrySource = {
  path: RelativePath!,
  revision: Identifier!,
  sha256: Sha256!,
  claim_class: enum<ClaimClass>!
}

ProductFeatureEntry = {
  feature_id: Identifier!,
  source_ref: RegistrySource!,
  title: ShortText!,
  human_disposition: enum<FeatureDisposition>!,
  contract_ref: SubjectRef?,
  function_ids: set<Identifier>!,
  dependency_feature_ids: set<Identifier>!,
  state: enum<FeatureRegistryState>!
}

FeatureRegistryState = INVENTORIED | SELECTED_NO_EXACT_CONTRACT | CONTRACTED | SUPERSEDED
```

Rules:

- `SELECTED_NO_EXACT_CONTRACT` cannot be compiled into a Task Brief;
- `CONTRACTED` requires a human-accepted exact `contract_ref`;
- missing disposition is explicit `UNDECIDED`, not omitted;
- the registry copies no full behavior; consumers follow `source_ref`/`contract_ref`;
- source_set_digest is the canonical digest of ordered `(path, revision, sha256)` tuples.

### 3.3. Execution/Verification Registry schema

```text
ExecutionVerificationRegistry = {
  schema_version: "aos.execution-verification-registry.v1"!,
  generated_at: UtcTimestamp!,
  source_set_digest: Sha256!,
  sources: list<RegistrySource>!,
  entries: list<ExecutionVerificationEntry>!,
  limitations: list<NonEmptyText>!
}

ExecutionVerificationEntry = {
  task_ref: RecordRef!,
  feature_id: Identifier?,
  contract_refs: list<SubjectRef>!,
  stage_record_refs: list<RecordRef>!,
  validation_refs: list<RecordRef>!,
  evidence_refs: list<RecordRef>!,
  human_decision_refs: list<RecordRef>!,
  Git_delivery_refs: list<RecordRef>!,
  latest_observed_stage: enum<TaskStage>!,
  latest_technical_result: enum<TechnicalResult>!,
  human_decision: enum<HumanDecision>?,
  stale: boolean!
}
```

Technical result, human decision and Git delivery are separate fields. Empty ref lists mean no such record, not success. `stale: false` means source digests matched at rebuild time only.

### 3.4. Relation model

The registry expresses navigation edges only:

```text
feature
→ function
→ exact Feature Contract
→ Task Brief
→ requirement/criterion
→ positive test
→ negative test
→ Evidence
→ human decision
```

An edge exists only when both exact endpoints exist. Missing edges are explicit gaps; inferred edges are forbidden.

### 3.5. Rebuild and stale detection

Deterministic rebuild:

1. Resolve the accepted source-owner set from bootstrap/current Task Brief.
2. Strict-load and hash every source.
3. Sort sources by repository-relative path and entries by stable ID.
4. Reject duplicate IDs, dangling refs and conflicting human dispositions.
5. Render complete canonical registry to a temp file.
6. Recheck source digests before atomic replace.
7. Emit build Evidence and an authorized Stage Record.

Index status is closed:

```text
CURRENT | STALE_SOURCE_DIGEST | INCOMPLETE | CONFLICT | NOT_BUILT
```

No state maps automatically to technical `PASS`; the consuming command applies its own required/optional rule.

## 4. C5 — Context Pack

### 4.1. Request and manifest schema

```text
ContextPackRequest = {
  task_ref: RecordRef!,
  repository_identity: RepositoryIdentity!,
  purpose: ShortText!,
  required_fact_classes: set<Identifier>!,
  required_contract_refs: list<SubjectRef>!,
  max_total_bytes: PositiveInt!,
  max_file_count: PositiveInt!,
  excluded_paths: set<RelativePath>!,
  created_at: UtcTimestamp!
}

ContextPackManifest = {
  schema_version: "aos.context-pack.v1"!,
  request_digest: Sha256!,
  task_ref: RecordRef!,
  repository_identity: RepositoryIdentity!,
  generated_at: UtcTimestamp!,
  selected: list<ContextItem>!,
  excluded: list<ContextExclusion>!,
  total_bytes: PositiveInt!,
  freshness: enum<ContextFreshness>!,
  limitations: list<NonEmptyText>!
}

ContextItem = {
  path: RelativePath!,
  sha256: Sha256!,
  bytes: PositiveInt!,
  role: enum<ContextRole>!,
  inclusion_reason: NonEmptyText!,
  authority: enum<ContextAuthority>!
}

ContextExclusion = {
  path: RelativePath!,
  reason: enum<ExclusionReason>!,
  required: boolean!
}
```

Closed local enums:

```text
ContextRole = TASK | CONTRACT | DECISION | CURRENT_STATE | REGRESSION | REPOSITORY_OBSERVATION | SUPPORTING_REFERENCE
ContextAuthority = OWNER | ACCEPTED_DECISION | OBSERVATION_ONLY | NAVIGATION_ONLY | REFERENCE_NONE
ContextFreshness = FRESH | STALE | INCOMPLETE | BLOCKED_UNKNOWN
ExclusionReason = OUT_OF_SCOPE | DUPLICATE_FACT_CLASS | SUPERSEDED | STALE | BUDGET | FORBIDDEN | SENSITIVE | MISSING
```

### 4.2. Deterministic selection algorithm

1. Include exact Task Brief and its DSP.
2. Include every directly referenced contract/accepted decision and C3 current state ref required by the task.
3. Include fresh repository observations required by preflight; record them as observation only.
4. Include only regression/lesson sources explicitly mapped by the task validation matrix.
5. Deduplicate by `(fact_class, owner, sha256)`; keep the highest-authority exact owner.
6. Exclude superseded, unrelated, historical and chat-only sources.
7. Sort mandatory items by role order above, then path. Sort optional items by declared relevance, then path.
8. If mandatory items exceed `max_total_bytes` or `max_file_count`, return `BLOCKED`/`INCOMPLETE`; never truncate an owner silently.
9. Fill remaining budget only with explicitly relevant optional items; every exclusion receives a reason.
10. Recompute every digest and repository identity immediately before handoff.

Budget has no global implicit default. It is required in the Task Brief/DSP. This avoids hiding a material source due to an agent-chosen token budget.

### 4.3. Persistence and authority

Context Pack is derived and may be delivered as a manifest plus referenced files. If persisted, its candidate path is:

```text
.aos/index/context-packs/<task_id>.<request_digest>.json
```

It is rebuildable, never a current-state owner and never a substitute for the referenced source. External retrieved content is `REFERENCE_NONE` and untrusted data.

## 5. C6 — Task-local coordinator

### 5.1. Pure coordinator contract

The coordinator is a pure routing function:

```text
(fresh C-012 v2 Project Memory, exact terminal record when task ACTIVE,
 C2 permission result, task policy when task ACTIVE)
→ CoordinationDecision
```

It performs no file, process, network, Git, registry or lifecycle mutation. It validates one already recorded next action; it does not select a new feature/task or dispatch a run.

```text
CoordinationDecision = {
  schema_version: "aos.coordination-decision.v1"!,
  active_task_status: enum<ActiveTaskStatus>!,
  active_task_ref: RecordRef?,
  current_stage: enum<TaskStage>?,
  terminal_record_ref: RecordRef?,
  coordination_result: enum<TechnicalResultWithoutHumanReviewRequired>!,
  terminal_technical_result: enum<TechnicalResult>?,
  human_decision: enum<HumanDecision>?,
  permission: enum<PermissionClass>!,
  allowed_next_run: enum<AllowedNextRun>!,
  required_condition: enum<CoordinationCondition>!,
  forbidden_implicit_actions: set<enum<ImplicitAction>>!,
  one_next_action: NonEmptyText!,
  decision_basis_refs: list<RecordRef>!
}
```

Cross-field invariants:

- `coordination_result` reports evaluation of the routing inputs, not the prior run result: every valid row in section 5.2 returns `PASS`; malformed input returns `CONTRACT_VIOLATION`; missing/stale required input returns `BLOCKED` or `UNKNOWN`; it never returns `HUMAN_REVIEW_REQUIRED`;
- `terminal_technical_result` is the exact result from `terminal_record_ref`; both are present or absent together and may never be synthesized;
- `active_task_status: NONE` requires absent `active_task_ref`, `current_stage`, `terminal_record_ref`, `terminal_technical_result` and `human_decision`; `coordination_result` is `PASS`, `permission` is `HUMAN_AUTHORIZATION_REQUIRED`, and `allowed_next_run` is `NONE`;
- `active_task_status: ACTIVE` requires `active_task_ref` and `current_stage`; `terminal_record_ref` is required for any transition based on a completed stage and may be absent only before the first terminal record;
- coordinator never fabricates a Task Brief, stage or terminal record to make an inactive state routable;
- the `No active Task Brief` transition consumes the explicit `NONE` state from C-012 v2, not absence inferred from a malformed record.
- `permission` copies the exact C2 classification for the recorded `one_next_action`; it is never inferred from a technical result;
- `one_next_action` is copied byte-for-byte from fresh Project Memory; if it conflicts with the selected row/condition, `coordination_result` is `CONTRACT_VIOLATION`, `allowed_next_run` is `NONE` and no alternate action is invented;
- `decision_basis_refs` is the canonical unique ordered set of the Project Memory record, active Task Brief when present, terminal record when present, authentic Human Decision Record when present and exact authorization/permission Evidence ref when present; missing required basis makes coordination non-PASS.

```text
AllowedNextRun = NONE | PLAN | EXECUTE | VALIDATE | REVIEW | DELIVER
ImplicitAction = AUTO_EXECUTE | AUTO_RETRY | AUTO_FIX | AUTO_VALIDATE | AUTO_ACCEPT | AUTO_DELIVER | AUTO_GIT | AUTO_NEXT_TASK | AUTO_RISK_ASSIGNMENT
CoordinationCondition =
  HUMAN_SELECT_TASK_AND_SCOPE |
  ACTIVE_TASK_PLAN_REQUIRED |
  HUMAN_RISK_AND_ACTION_AUTHORIZATION_REQUIRED |
  RESOLVE_PLAN_NON_PASS |
  EXACT_READ_ONLY_VALIDATION_REQUIRED |
  REVIEW_PACKAGE_REQUIRED |
  EXECUTION_CORRECTION_OR_RECOVERY_REQUIRED |
  EXACT_REVIEW_PACKAGE_REQUIRED |
  SEPARATE_CORRECTION_REQUIRED |
  HUMAN_DECISION_REQUIRED |
  AUTHORIZED_DELIVER_REQUIRED |
  BOUNDED_CORRECTION_REVISION_REQUIRED |
  DECISION_HANDOFF_REQUIRED |
  HUMAN_SELECT_LATER_TASK
```

### 5.2. Finite transition table

For every schema-valid row below, `coordination_result: PASS`. `allowed_next_run` is the shown value only when the exact C2 `permission` permits that read/write boundary; otherwise it is `NONE`. `human_decision` is present only in the three Human Decision rows and absent in all others.

| Current exact state | Terminal projection | Allowed next run | Exact `required_condition` | Exact `forbidden_implicit_actions` set |
|---|---|---|---|---|
| No active Task Brief | both terminal fields absent | `NONE` | `HUMAN_SELECT_TASK_AND_SCOPE` | `{AUTO_EXECUTE, AUTO_NEXT_TASK, AUTO_RISK_ASSIGNMENT}` |
| Active Task Brief at `PLAN`, no terminal record | both terminal fields absent | `PLAN` if permission `ALLOWED`, else `NONE` | `ACTIVE_TASK_PLAN_REQUIRED` | `{AUTO_EXECUTE, AUTO_RISK_ASSIGNMENT}` |
| `PLAN + PASS`, Task frozen, permission requires human authorization | exact PLAN ref + `PASS` | `NONE` | `HUMAN_RISK_AND_ACTION_AUTHORIZATION_REQUIRED` | `{AUTO_EXECUTE, AUTO_RISK_ASSIGNMENT}` |
| `PLAN + FAIL/BLOCKED/UNKNOWN/NOT_RUN` | exact PLAN ref + recorded non-PASS | `NONE` | `RESOLVE_PLAN_NON_PASS` | `{AUTO_RETRY, AUTO_FIX}` |
| `EXECUTE + PASS`, independent validation required | exact EXECUTE ref + `PASS` | `VALIDATE` if permission `ALLOWED`, else `NONE` | `EXACT_READ_ONLY_VALIDATION_REQUIRED` | `{AUTO_FIX, AUTO_NEXT_TASK}` |
| `EXECUTE + PASS`, validation not required | exact EXECUTE ref + `PASS` | `REVIEW` if permission `ALLOWED`, else `NONE` | `REVIEW_PACKAGE_REQUIRED` | `{AUTO_ACCEPT, AUTO_NEXT_TASK}` |
| `EXECUTE + FAIL/BLOCKED/UNKNOWN/CONTRACT_VIOLATION` | exact EXECUTE ref + recorded non-PASS | `NONE` | `EXECUTION_CORRECTION_OR_RECOVERY_REQUIRED` | `{AUTO_RETRY, AUTO_FIX}` |
| `VALIDATE + PASS`, no mutation observed | exact VALIDATE ref + `PASS` | `REVIEW` if permission `ALLOWED`, else `NONE` | `EXACT_REVIEW_PACKAGE_REQUIRED` | `{AUTO_ACCEPT, AUTO_DELIVER}` |
| `VALIDATE + finding/non-PASS` | exact VALIDATE ref + aggregate non-PASS | `NONE` | `SEPARATE_CORRECTION_REQUIRED` | `{AUTO_FIX, AUTO_VALIDATE}` |
| `REVIEW`, human decision absent | exact REVIEW ref + recorded result | `NONE` | `HUMAN_DECISION_REQUIRED` | `{AUTO_ACCEPT, AUTO_DELIVER}` |
| Human `ACCEPT` after review-ready terminal | exact REVIEW ref/result; `human_decision: ACCEPT` | `DELIVER` only if separately `ALLOWED`, else `NONE` | `AUTHORIZED_DELIVER_REQUIRED` | `{AUTO_DELIVER, AUTO_GIT, AUTO_NEXT_TASK}` |
| Human `NEEDS_CHANGES` | exact REVIEW ref/result; `human_decision: NEEDS_CHANGES` | `PLAN` if permission `ALLOWED`, else `NONE` | `BOUNDED_CORRECTION_REVISION_REQUIRED` | `{AUTO_FIX, AUTO_VALIDATE}` |
| Human `REJECT` or `DEFER` | exact REVIEW ref/result; exact decision | `DELIVER` read-only if `ALLOWED`, else `NONE` | `DECISION_HANDOFF_REQUIRED` | `{AUTO_FIX, AUTO_NEXT_TASK}` |
| `DELIVER` terminal | exact DELIVER ref/result | `NONE` | `HUMAN_SELECT_LATER_TASK` | `{AUTO_NEXT_TASK}` |

`HUMAN_AUTHORIZATION_REQUIRED` is a C2 permission, not a technical result. Axes must not be collapsed.

### 5.3. Correction limit

Within one unchanged documentation/implementation scope, maximum correction cycles are read from the exact Task Brief. For this documentation production sequence the accepted plan allows at most three. The coordinator counts only completed correction candidates, not validation reruns. At limit, `allowed_next_run: NONE` and one human decision is required.

## 6. C7 — Scoped executor foundation

### 6.1. Entry gates

Before any target write all must pass:

1. strict valid Task Brief and exact active one-shot authorization;
2. human-assigned Risk Profile;
3. fresh repository identity and preview;
4. normalized non-overlapping path/operation allow/deny sets;
5. resolved symlink/nested-repository/case-collision boundary;
6. recovery strategy for every planned operation;
7. credentials/sensitive/network/Git boundaries explicitly classified;
8. journal path writable without touching forbidden/user-owned state.

Failure returns before first target write and emits denial/preflight Evidence. No journal is created when authorization itself is invalid.

### 6.2. Exact operation journal

Journal path:

```text
.aos/state/transactions/<run_id>/journal.json
```

This journal owns only in-progress transaction facts, not current lifecycle. C3 Project Memory may reference a recovery-required transaction after an authorized state update.

```text
OperationJournal = {
  schema_version: "aos.operation-journal.v1"!,
  run_id: Identifier!,
  task_ref: RecordRef!,
  authorization_ref: RecordRef!,
  preview_ref: RecordRef!,
  starting_identity: RepositoryIdentity!,
  state: enum<JournalState>!,
  planned: list<JournalOperation>!,
  completed_operation_ids: set<Identifier>!,
  next_operation_id: Identifier?,
  last_updated_at: UtcTimestamp!,
  failure: NonEmptyText?
}

JournalOperation = {
  operation_id: Identifier!,
  action_class: enum<ActionClass>!,
  path: RelativePath!,
  intended_sha256: Sha256?,
  preimage_sha256: Sha256?,
  ownership: enum<OperationOwnership>!,
  rollback_mode: enum<RollbackMode>!
}

JournalState = PREPARED | APPLYING | RECOVERY_REQUIRED | RECONCILING | COMPLETED | ROLLED_BACK
OperationOwnership = MANAGED_NEW | MANAGED_EXISTING | USER_OWNED_FORBIDDEN | GENERATED_DISPOSABLE
RollbackMode = DELETE_CREATED | RESTORE_EXACT_PREIMAGE | DISCARD_GENERATED | NONE_STOP_ONLY
```

Journal updates use the C3 atomic protocol. It is created and fsynced before first target write. Every completed operation is journaled and fsynced before the next begins.

### 6.3. Scoped apply protocol

```text
recheck C2 authorization and preview
→ create PREPARED journal
→ for each exact planned operation:
     recheck operation/path boundary
     capture/verify preimage
     mark APPLYING
     perform one atomic or journaled operation
     verify intended bytes/state
     append completed operation id and fsync journal
→ reconcile intended versus actual paths/digests
→ run required post-write checks
→ freeze candidate when task requires it
→ emit terminal Stage Record and immutable Evidence
→ consume authorization
→ stop
```

No unrelated cleanup, formatting or dependency update is allowed. A newly discovered causal change outside scope stops the run.

### 6.4. Partial-write detection and reconciliation

Detection compares:

- journal planned/completed operation IDs;
- preimage/intended/actual digests;
- preview path set versus actual changed paths;
- repository identity before/after;
- out-of-scope user-state inventory;
- temp/staging artifacts.

Any unjournaled changed path, missing completed write, digest mismatch or identity drift returns `RECOVERY_REQUIRED`/exit `7`; authorization is consumed. `PASS` is impossible until post-recovery validation completes in a separate run.

### 6.5. Bounded resume

Resume is allowed only when:

- journal strict-loads and is `RECOVERY_REQUIRED`;
- task/auth/preview/start identity and already-completed operations match exact evidence;
- authorization for the original run is consumed and a new exact recovery authorization covers resume;
- remaining operations are unchanged and safe;
- user-owned/out-of-scope state did not change materially.

Otherwise stop. Resume does not mean generic retry.

### 6.6. Rollback boundary

Non-destructive rollback may delete only `MANAGED_NEW` paths created by this transaction, restore only exact captured `MANAGED_EXISTING` preimages, or discard declared generated artifacts. It never uses broad `rm`, `git reset`, `git checkout`, wildcard cleanup or guessed preimages.

Any destructive rollback, user-owned path change or uncertain ownership requires a separate `DESTRUCTIVE_RECOVERY` authorization. If exact recovery cannot be proven, preserve state/journal and stop for human decision.

### 6.7. Candidate freeze

Candidate freeze identity is computed from:

```text
task_ref
+ contract refs
+ starting repository identity
+ sorted actual changed paths with digests/modes
+ Stage Record ref
→ candidate SubjectRef
```

Freeze rules:

1. freeze occurs only after scoped reconciliation and required execution checks;
2. the frozen manifest is immutable Evidence/Stage output;
3. any subsequent candidate-path change invalidates freeze, validation and dependent authorization;
4. write-after-freeze is rejected even if path was previously allowed;
5. correction creates a new revision/SubjectRef and requires revalidation;
6. validation never repairs the frozen subject.

## 7. First-consumer gates

| Consumer | Required core contract before implementation | Current state |
|---|---|---|
| Product Runtime Intent save | C1 strict Intent/Memory schemas, C2 permission, C3 atomic state, C7 write/recovery | documented; not authorized/implemented |
| Status/Next/Details | C3 owner/freshness + C4 zero-write outputs | documented; not implemented |
| Task Brief compiler | C1/C2 + C5 registries/context + C6 coordinator | future; feature/task selection not implied |
| Scoped executor | C1/C2 + C3 state + C6 stage route + C7 journal/recovery | future; `FTR-010` remains unselected |
| Current Task-001 scaffold | accepted scaffold contract/Task/DSP | remains nearest unimplemented task; C5–C7 do not modify it |

## 8. Acceptance matrix

| ID | Contract | Case | Expected observable result |
|---|---|---|---|
| `C5-ACC-001` | registry | deterministic rebuild | same exact sources produce identical canonical bytes/digest |
| `C5-ACC-002` | registry | source changes | registry reports `STALE_SOURCE_DIGEST`; no stale authority |
| `C5-ACC-003` | registry | missing edge | explicit gap; no inferred task/test/Evidence link |
| `C5-ACC-004` | Context Pack | mandatory set fits | all owners included with reason/digest and fresh identity |
| `C5-ACC-005` | Context Pack | mandatory exceeds budget | `BLOCKED/INCOMPLETE`; no silent truncation |
| `C5-ACC-006` | Context Pack | irrelevant legacy/chat | excluded with reason and no authority |
| `C6-ACC-001` | coordinator | PLAN ready, no auth | `NONE`; exact human authorization required |
| `C6-ACC-002` | coordinator | EXECUTE PASS/frozen | VALIDATE or REVIEW only per task policy; no next task |
| `C6-ACC-003` | coordinator | validation finding | stop; separate correction boundary |
| `C6-ACC-004` | coordinator | human ACCEPT | only authorized DELIVER proposal; Git still `NOT_RUN` |
| `C6-ACC-005` | coordinator | correction limit | stop for human decision |
| `C6-ACC-006` | coordinator | Project Memory has no active task | exact `NONE`; refs/results absent; coordination `PASS`; permission `HUMAN_AUTHORIZATION_REQUIRED`; allowed next run `NONE` |
| `C6-ACC-007` | coordinator | active Task Brief before first terminal record | PLAN route only when C2 says `ALLOWED`; terminal projection absent; exact condition/forbidden set/basis refs |
| `C7-ACC-001` | executor | valid scoped apply | journaled exact writes, reconciliation, Stage Record, auth consumed |
| `C7-ACC-002` | executor | pre-write blocker | zero target writes and named denial/recovery step |
| `C7-ACC-003` | executor | interruption | partial state detected, journal preserved, exit `7` |
| `C7-ACC-004` | recovery | safe exact resume | only remaining unchanged operations applied under new recovery auth |
| `C7-ACC-005` | recovery | safe rollback | only transaction-created/exact-preimage paths restored |
| `C7-ACC-006` | freeze | post-freeze write | rejected; old validation/auth invalidated |
| `C7-ACC-007` | reconciliation | unrelated user state | preserved and reported; candidate cannot PASS if modified |

## 9. Negative fixtures

| Fixture | Defect/attack | Expected result |
|---|---|---|
| `C5-NEG-001-duplicate-feature-id` | two sources claim same ID incompatibly | registry `CONFLICT`; no winner inferred |
| `C5-NEG-002-registry-as-owner` | consumer treats index status as current truth | contract failure |
| `C5-NEG-003-dangling-ref` | task/test/Evidence endpoint missing | `INCOMPLETE`; edge omitted with gap |
| `C5-NEG-004-budget-truncates-owner` | owner dropped to fit bytes | `BLOCKED`; pack invalid |
| `C5-NEG-005-chat-only-context` | chat supplies missing decision | excluded/non-authoritative |
| `C5-NEG-006-stale-observation` | old HEAD packaged as current | pack `STALE` |
| `C6-NEG-001-auto-execute` | coordinator dispatches after PLAN | prohibited |
| `C6-NEG-002-auto-retry` | failed EXECUTE reruns itself | prohibited |
| `C6-NEG-003-validation-fixes` | validator mutates candidate | validation invalid |
| `C6-NEG-004-pass-as-accept` | PASS produces human ACCEPT | contract violation |
| `C6-NEG-005-auto-git` | accepted candidate commits/pushes | denied; separate permission required |
| `C6-NEG-006-axis-collapse` | permission encoded as technical result | contract violation |
| `C6-NEG-007-none-with-task-ref` | coordinator output says `NONE` but includes task/stage/terminal ref | contract violation |
| `C6-NEG-008-active-without-task` | coordinator output says `ACTIVE` without required task/stage | contract violation |
| `C6-NEG-009-result-axis-collapse` | prior terminal result stored as coordinator evaluation or `NONE` fabricates terminal result | contract violation |
| `C6-NEG-010-incomplete-row-output` | permission/condition/forbidden set/action/basis ref omitted or prose not in closed enum | contract violation; no route |
| `C7-NEG-001-no-journal` | first target write precedes journal fsync | stop/fail fixture |
| `C7-NEG-002-unjournaled-path` | actual path absent from preview | recovery required; no PASS |
| `C7-NEG-003-reuse-consumed-auth` | resume uses original auth | denied |
| `C7-NEG-004-broad-rollback` | recovery uses Git reset/wildcard delete | blocked policy |
| `C7-NEG-005-user-owned-preimage` | uncertain user path restoration | destructive authorization/human decision required |
| `C7-NEG-006-write-after-freeze` | candidate mutated in place | freeze invalid; validation cannot proceed |
| `C7-NEG-007-hidden-scope-expansion` | causal change needs extra path | stop; new Task Brief/authorization |
| `C7-NEG-008-partial-pass` | interrupted run reports PASS | contract violation |

## 10. Recovery matrix

| ID | Failure | Preserved facts | Bounded route | Revalidation |
|---|---|---|---|---|
| `C5-REC-001` | registry build interrupted | old registry and source set | discard exact temp; rebuild from sources | digest/ref/duplicate audit |
| `C5-REC-002` | stale registry | stale bytes and new source digests | authorized rebuild; never patch entries manually | complete rebuild comparison |
| `C5-REC-003` | Context Pack stale | manifest and changed source identity | regenerate from exact request/new repo identity | budget + all digests |
| `C6-REC-001` | invalid terminal record | raw record/evidence | correct source in separate task; no inferred transition | C1 strict load + transition table |
| `C6-REC-002` | wrong next action | current Project Memory preserved | human/authorized C3 state correction | C3 freshness + C6 pure evaluation |
| `C6-REC-003` | active-task conditional fields invalid | previous valid Project Memory/output | reject routing; correct source through bounded C3 recovery | C-012 v2 strict load + C6 invariants |
| `C7-REC-001` | pre-write failure | zero target diff, denial/preview facts | resolve named gate and request new auth | all entry gates |
| `C7-REC-002` | partial write | journal, actual paths/digests, user state | separate recovery Task/auth for resume or rollback | intended/actual + post-recovery suite |
| `C7-REC-003` | journal corrupt | target state preserved, raw journal | do not guess; read-only inventory and human decision | journal schema + full repository reconciliation |
| `C7-REC-004` | rollback partial | journal/recovery evidence | stop; new recovery subject and authorization | affected paths + full required tests |
| `C7-REC-005` | candidate changed after freeze | old manifest and new observation | new candidate revision, new validation/auth | freeze identity + scope/tests |

## 11. Traceability

| Concern | Feature relationship | Contracts | Lessons/regressions |
|---|---|---|---|
| Derived registries | broader `FTR-003/FTR-030` mechanics; no new selection | `C-002`, `C-005`, `C-008…C-012` + C5 | `LES-013`, `027`, `028`; `DRIFT-001`, `STATE-001` |
| Context Pack | later boundary of H1 `FTR-016`; not first Product slice | `C-005`, `C-012` + C5 | `LES-022`, `028…030`; `LINK-001`, `ADAPTER-001` |
| Coordinator | supporting `FTR-006`; full backlog/orchestration not selected | `C-005…C-012` + C6 | `LES-006…012`, `037`, `038`; `AUTH`, `STATUS`, `IDLE` |
| Scoped execution | `FTR-009/010/013/014` remain unselected; only future safety foundation | `C-006…C-010`, `C-012` + C7 | `LES-017…025`, `038`; `SCOPE`, `PARTIAL`, `FREEZE`, `BASELINE` |
| Trust boundary | H1-required `FTR-019` minimal boundary | C2 + C7 | `LES-012`, `017`, `020`, `021`, `039`; `AUTH`, `CONTENT`, `GIT` |

## 12. Proposed implementation outline — non-executable

No new Task Brief is created while `Task-001-Scaffolding` remains unimplemented. A future dependency outline is:

```text
C5 strict derived registries/context manifest
→ C6 pure transition evaluator
→ C7 preflight/journal/reconciliation primitives
```

This outline has no task ID, repository preflight, assigned Risk Profile or authorization.

## 13. Candidate status

```yaml
DOC-008:
  technical_result: PASS
  readiness: READY_FOR_FINAL_PACKAGE_REVIEW
  human_acceptance: NOT_RUN
  dependency_status: PROVISIONAL_CANDIDATES
contract_scope:
  C5: DOCUMENTED_AS_CANDIDATE
  C6: DOCUMENTED_AS_CANDIDATE
  C7: DOCUMENTED_AS_CANDIDATE
nearest_unimplemented_task: Task-001-Scaffolding.md
new_implementation_task: NOT_CREATED
implementation_repository_creation: NOT_RUN
runtime_implementation: NOT_RUN
execution_authorization: NOT_RUN
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: CONTINUE_DOC-009_UNDER_CURRENT_AUTONOMOUS_MANDATE
stop: false
```
