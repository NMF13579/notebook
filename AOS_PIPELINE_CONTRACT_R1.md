---
document_type: AOS_PIPELINE_CONTRACT
revision: DRAFT-R1
status: HUMAN_REVIEW_REQUIRED
claim_class: DRAFT_CONTRACT_CANDIDATE
authority: NONE_UNTIL_HUMAN_ACCEPTANCE
authority_scope:
  - PART_1_IDEA_TO_EXACT_TASK_BRIEF
  - PART_2_AUTHORIZED_EXECUTION_TO_REVIEW_PACKAGE
  - PART_3_HUMAN_DECISION_TO_HANDOFF
documentation_tasks:
  - DOC-009
  - DOC-010
  - DOC-011
technical_result: PASS
readiness: READY_FOR_FINAL_PACKAGE_REVIEW
human_acceptance: NOT_RUN
provisional_dependencies:
  accepted:
    - AOS_CORE_CONTRACT_R1.md@24f1af001bc0249d9c8e40a9608c2c5b67ea047bf2307cbda251f184b223d5db
  candidates:
    - AOS_CORE_CONTRACT_C012_V2_R1.md@5e6f5ad2250167f4d71ee470b3a570e867fd6bc4a2eec79d5a2fffaace49b52d
    - AOS_CORE_CONTRACT_C3_C4_R1.md@7716d22f18daf1017d7a8659fc9625d8714b58cb72855a015f976bae92233821
    - AOS_CORE_CONTRACT_C5_C7_R1.md@89f524648ab688fde4475edaaa17e47839ebf6865c58b7302f05d544c6e1e67f
nearest_unimplemented_task: Task-001-Scaffolding.md
new_implementation_task_created: false
implementation_repository_creation: NOT_RUN
execution_authorization: NOT_RUN
git_authorization: NONE
created: 2026-08-05
---

# AOS-3 — Pipeline Contract R1

## 1. Назначение и scope

Документ определяет один greenfield journey:

```text
идея
→ reviewable Intent
→ Product Spec / exact Feature Contract
→ exact bounded Task Brief
→ separate authorization
→ scoped execution
→ Evidence / independent validation / Review Package
→ explicit human decision
→ authorized durable consequences or honest NOT_RUN
→ handoff and one next action
```

Pipeline не является новым owner для product facts, Task scope, current state, human decisions or permissions. Он связывает outputs их exact owners и задаёт переходы/гейты.

Full pipeline documentation does not expand the accepted first implementation slice. H1 first cycle remains:

```text
free-form idea → Intent Record → C-012 v2 Project Memory with `active_task_status: NONE`
→ Status/Next → stop before Product Spec/Task Brief/execution
```

Parts beyond that boundary are future contract candidates. They cannot be implemented until affected feature/scope/architecture/repository/risk decisions and a Task Brief are separately accepted.

## 2. Owner map and orthogonal axes

| Fact/axis | Exact owner |
|---|---|
| Original request and interpreted intent | `C-001 Intent Record` |
| Product scope/journeys/acceptance | human-accepted `C-003 Product Spec` |
| Selected feature behavior | human-accepted `C-002 Feature Contract` |
| Architecture choice | human-accepted `C-004 ADR` |
| Implementation scope | exact `C-005 Task Brief` |
| Permission | exact active `C-006 Execution Authorization` + C2 classifier |
| Mutable repository facts | fresh instrumental observation / `C-007 Preflight` |
| Technical execution/validation | `C-008/C-009` |
| Evidence | immutable `C-010` |
| Human decision | authentic `C-011` |
| Current lifecycle and next action | C3 `.aos/state/project-memory.json` using exact `C-012 v2.0.0` candidate |
| Git result | one `C-014` per action |

The pipeline preserves independent axes:

```text
document maturity
task stage
technical result
human decision
permission
authorization lifecycle
Git action lifecycle
```

No transition on one axis changes another unless an exact contract names the required record/gate.

## 3. End-to-end transition view

This table is a derived route, not persisted current state.

| Step | Owner input | Output owner | Gate before next step | Failure/recovery |
|---|---|---|---|---|
| Intake | human original request | `C-001` | intent review/clarification | preserve original; ask one material question; no product choice |
| Product shaping | accepted intent | `C-003` | exact product acceptance/open decisions resolved | keep draft; affected scope blocked only |
| Feature contract | accepted product scope + selected disposition | `C-002` | exact behavior accepted | no generic dossier defaults |
| ADR/research | named material gap | `C-004`/reference finding | human architecture decision when required | no legacy authority promotion |
| Task compile | exact accepted contracts | `C-005` + validation matrix | complete/frozen task | no full backlog/auto-next |
| Preflight/preview | task + fresh repo | `C-007` | no conflicts/material unknowns | zero-write stop/new preview |
| Authorization | exact task/preview/risk | `C-006` + authentic `C-011` | `ACTIVE` exact one-shot auth | deny/invalidate without mutation |
| Execute | active auth | journal + `C-008/C-010` | reconciliation, checks, freeze | stop; recovery subject; auth consumed |
| Validate | frozen candidate | `C-009/C-010` | independent PASS/no mutation when required | named finding; separate correction |
| Review | exact candidate/evidence | Review Package | human decision | no simulated acceptance |
| Human decision | explicit exact statement | `C-011` | decision-specific route | invalid generated/stale decision rejected |
| Durable consequence | accepted decision + separate auth | C3 state / `C-014` | one action per permission | honest `NOT_RUN`; no auto-Git |
| Handoff | exact records/observations | handoff manifest | one human-selected next action | stale identity blocks affected continuation |

## 4. Part 1 — Idea to exact Task Brief

### 4.1. Intake entry profiles

Closed profiles:

```text
INCOMPLETE_IDEA | FULL_SPEC
```

Both preserve the original request verbatim in a versioned `C-001` record. `FULL_SPEC` skips no validation; it only reduces clarification if required fields are explicit.

Required capture:

- actor/user segment;
- problem and current workaround;
- desired outcome separate from proposed solution;
- goals/non-goals/constraints;
- assumptions and unknowns;
- sensitive domain/data/provider/network flags;
- source/provenance;
- material questions or explicit none.

Empty/whitespace-only input returns `CONTRACT_VIOLATION` and creates no successful Intent Record.

### 4.2. Progressive clarification and material-question rule

A question is material when its answer can change:

- actor/problem/outcome or success oracle;
- product/feature scope or priority;
- user-visible behavior/schema/state/recovery;
- repository/architecture/toolchain/dependency;
- privacy/security/provider/network/sensitive-data boundary;
- Risk Profile, human authenticity or protected action;
- acceptance/negative cases.

The interaction asks one highest-priority material question at a time. Priority:

```text
safety/provider ambiguity
→ actor/problem/outcome
→ scope/non-goals
→ observable acceptance/recovery
→ implementation-affecting decision
```

Non-material reversible details may remain explicit assumptions. The agent stops before selecting a product solution when a material answer is missing.

### 4.3. Intent lifecycle

```text
DRAFT
→ CLARIFYING when material questions remain
→ HUMAN_REVIEW_REQUIRED when complete
→ ACCEPTED only by exact C-011 human decision
→ SUPERSEDED by a new accepted revision
```

These are local intent-maturity labels; they do not replace the global document maturity enum or create execution permission.

### 4.4. Product Spec contract

Exact product-level content:

```text
ProductSpecProfile = {
  product_spec_ref: RecordRef!,
  accepted_intent_ref: RecordRef!,
  problem: NonEmptyText!,
  user_segments: list<NonEmptyText>!,
  JTBD: list<NonEmptyText>!,
  goals: list<NonEmptyText>!,
  non_goals: list<NonEmptyText>!,
  journeys: list<UserJourney>!,
  product_boundary: list<NonEmptyText>!,
  success_signals: list<SuccessSignal>!,
  constraints: list<NonEmptyText>!,
  dependencies: list<NonEmptyText>!,
  risks: list<NonEmptyText>!,
  acceptance: list<Criterion>!,
  open_decisions: list<UnknownItem>!,
  feature_contract_refs: list<SubjectRef>!
}
```

Every journey names actor, trigger, observable steps, terminal outcome and failure/recovery. A Product Spec may describe candidate features but cannot mark one selected without an exact human disposition. Feature Contract owns feature behavior; Product Spec owns product context/boundary.

### 4.5. Optional UX skeleton gate

UX skeleton is required only if one of these is material to acceptance:

- multiple user roles/access levels;
- more than one navigation destination;
- UI state/error/recovery not expressible by CLI/chat flow;
- accessibility or workflow sequencing materially changes behavior.

Sequence:

```text
approved scenarios
→ access model
→ UX object inventory
→ grouping/navigation
→ screen/view map
→ empty/loading/error/success/recovery states
→ human review
```

It is a behavior/navigation contract, not styling, visual direction, implementation or authority owner. If gate conditions are false, `NOT_APPLICABLE` is recorded instead of a ceremonial artifact.

### 4.6. Feature selection and exact Feature Contract

Entry gates:

1. accepted Product Spec or accepted first-slice decision names the user outcome;
2. exact item-level human disposition selects the bounded feature/slice;
3. generic dossier is treated as inventory input only;
4. no material product decision is hidden.

Required exact feature content:

- actors/trigger/preconditions;
- exact inputs/outputs and schema refs;
- states/transitions;
- main flow;
- failures/recovery;
- dependencies/constraints;
- authority boundaries;
- observable acceptance and executable negatives;
- non-goals;
- remaining research questions;
- exact revision/disposition/decision ref.

Shared defaults must be replaced, not copied as unresolved placeholders.

### 4.7. Targeted research and ADR

Research is allowed only for a named material gap:

```text
question
→ exact repository/ref/commit/path
→ docs/contracts/tests/code
→ classified observation with provenance
→ rejected legacy complexity
→ remaining unknown
```

Reference authority remains `NONE`. An ADR is required only when implementation-affecting options remain after accepted product/contract facts. ADR must name options, trade-offs, evidence, selected human option, consequences and reversal conditions. No selection means affected Task compilation stops.

### 4.8. Lazy decomposition

The Task compiler chooses the smallest executable causal change that:

- produces one observable outcome or prerequisite;
- has exact paths/operations;
- can be validated independently;
- has bounded recovery;
- does not require a hidden product/architecture decision.

A sub-stage exists only for authority boundary, material dependency/risk, separate validation, protected operation or distinct acceptance. Full backlog generation and automatic next-task activation are forbidden.

### 4.9. Task Brief compilation

Compilation input:

```text
accepted Product/Feature/ADR refs
+ fresh repository identity requirement
+ C1–C7 contracts
+ selected regression/lesson mappings
→ exact C-005 Task Brief
+ requirements-to-tests matrix
+ proposed C-007 preflight/preview plan
+ unsigned authorization form
```

Completeness checks:

1. user outcome and exact feature revision;
2. in/out scope, allowed/forbidden paths and operations;
3. baseline/repository identity requirement;
4. required behavior/invariants/assumptions/material unknowns;
5. acceptance, negatives, Evidence and recovery;
6. correction limit and stop conditions;
7. proposed Risk Profile; assigned remains `UNASSIGNED` until human decision;
8. terminal report schema;
9. execution/Git authorization `NOT_RUN`/`NONE`.

Any missing item that requires coding-agent invention blocks developer readiness.

### 4.10. Part 1 exit contract

```yaml
outputs:
  exact_Task_Brief: REQUIRED
  validation_matrix: REQUIRED
  preflight_preview_plan: REQUIRED
  proposed_authorization_form: UNSIGNED_ONLY
permission: HUMAN_AUTHORIZATION_REQUIRED
execution: NOT_RUN
Git_authorization: NONE
stop: true
```

## 5. Part 1 acceptance, negatives and recovery

### 5.1. Acceptance

| ID | Case | Expected observable result |
|---|---|---|
| `P1-ACC-001` | incomplete idea | original preserved; material question or reviewable Intent; no hidden product choice |
| `P1-ACC-002` | full spec | same strict validation; missing material fields asked explicitly |
| `P1-ACC-003` | accepted Intent | exact C-011 binding; no execution permission |
| `P1-ACC-004` | Product Spec | problem/users/journeys/scope/signals/acceptance/open decisions complete |
| `P1-ACC-005` | UX gate false | `NOT_APPLICABLE`; no empty UX artifact |
| `P1-ACC-006` | UX gate true | roles/objects/map/states/recovery reviewed without styling choice |
| `P1-ACC-007` | selected feature | exact disposition and Feature Contract revision bound |
| `P1-ACC-008` | research gap | exact narrow provenance and authority NONE |
| `P1-ACC-009` | architecture decision | accepted ADR bound before Task compilation |
| `P1-ACC-010` | lazy decomposition | one smallest task; no full backlog/auto-next |
| `P1-ACC-011` | exact Task Brief | all completeness checks machine-reviewable |
| `P1-ACC-012` | exit | permission `HUMAN_AUTHORIZATION_REQUIRED`, execution/Git `NOT_RUN` |

### 5.2. Negative fixtures

| Fixture | Defect | Expected result |
|---|---|---|
| `P1-NEG-001-empty-intake` | blank request | contract violation; no successful record |
| `P1-NEG-002-solution-as-problem` | assumed solution copied as outcome | clarification required |
| `P1-NEG-003-hidden-material-question` | security/scope unknown left as harmless assumption | affected route blocked |
| `P1-NEG-004-generic-feature-dossier` | dossier treated as exact contract | Task compile rejected |
| `P1-NEG-005-unselected-feature` | no human disposition | no implementation task |
| `P1-NEG-006-legacy-authority` | historical topology adopted automatically | rejected/reference only |
| `P1-NEG-007-ADR-agent-selected` | agent chooses material option | no accepted ADR; stop |
| `P1-NEG-008-full-backlog` | all future tasks generated/activated | prohibited |
| `P1-NEG-009-task-missing-negative` | acceptance only positive prose | not developer-ready |
| `P1-NEG-010-task-authorizes-itself` | Task Brief says authorized | invalid; permission remains absent |
| `P1-NEG-011-risk-agent-assigned` | agent assigns Risk Profile | invalid human-owned field |
| `P1-NEG-012-chat-only-fact` | required decision only in chat summary | gap; exact record required |

### 5.3. Recovery

| ID | Failure | Recovery |
|---|---|---|
| `P1-REC-001` | clarification changes intent | create new Intent revision; preserve original and supersession link |
| `P1-REC-002` | Product Spec conflict | keep candidate DRAFT; resolve only affected decision |
| `P1-REC-003` | selected feature lacks exact contract | return to feature contract; do not ask coder to decide |
| `P1-REC-004` | research unavailable | `BLOCKED_REFERENCE_ACCESS`/remaining unknown; no invented finding |
| `P1-REC-005` | Task completeness failure | bounded documentation correction, same scope, new digest |
| `P1-REC-006` | baseline becomes stale before auth | fresh preflight/preview; Task changes only if scope/contract changes |

## 6. Part 2 — Authorized execution to Review Package

### 6.1. Authorization recheck

Immediately before each action, revalidate:

- exact authorization/task/subject/preview identities;
- status `ACTIVE`, expiry and one-shot state;
- repository root/branch/HEAD/worktree/baseline;
- assigned Risk Profile;
- action/path allow/deny sets;
- network/credential/sensitive/Git boundaries;
- candidate not frozen;
- no material unknown/scope expansion.

Mismatch stops before the affected mutation, records denial and invalidates/consumes authorization per C2/C7.

### 6.2. Scoped execution

One run performs one stage and one causal change. It may execute only journaled operations from the exact preview. It preserves unrelated user state and reports environment noise separately.

Bounded technical correction is allowed only if the exact Task Brief permits it and product outcome, architecture, scope, authority/risk and downstream identity do not change. Maximum cycles are explicit; absent value means no correction. For this documentation sequence maximum is three, but future implementation tasks must state their own bound.

No correction may activate `VALIDATE`, another task or Git action automatically.

### 6.3. Requirement-to-test/Evidence binding

Every mandatory requirement has one row:

| Field | Requirement |
|---|---|
| `requirement_id` | stable ID from exact contract/task |
| `owner_ref` | contract owner/revision |
| `implementation_surface` | exact module/path/interface |
| `positive_test` | command/fixture + oracle |
| `negative_test` | command/fixture + oracle |
| `regression_refs` | relevant LES/fixture IDs |
| `evidence_method` | command/digest/diff/runtime observation |
| `evidence_locator` | durable subject-bound locator |
| `required` | boolean |
| `result` | closed check status |
| `limitations` | explicit list |

Required `NOT_RUN/UNKNOWN/BLOCKED/FAIL` prevents PASS. Evidence without subject binding is invalid and never grants permission.

### 6.4. Reconciliation and freeze

At EXECUTE termination:

1. compare intended/actual operations and changed paths;
2. verify allowed/forbidden scope and out-of-scope preservation;
3. run required checks or report honest `NOT_RUN`;
4. emit immutable Evidence and C-008 Stage Record;
5. compute frozen candidate identity under C7;
6. consume authorization;
7. stop.

Stage Record includes starting/ending identity, operations, checks run/not run, findings/limitations/unknowns, out-of-scope state, stop reason and one next action.

### 6.5. Separate VALIDATE

Independent validation is required when the Task Brief/risk demands it or the candidate changes contracts, authority, persistence, recovery, security or developer handoff.

Validator requirements:

- exact frozen subject and environment identity;
- read-only/zero subject mutation;
- scope/acceptance/negative/regression/recovery checks;
- self-reference and stale identity detection;
- required/optional separation;
- no correction of findings;
- C-009 envelope and immutable Evidence;
- one next action and stop.

Any subject mutation invalidates the validation run. A finding routes to a new bounded correction candidate and later new validation.

### 6.6. Review Package

One human-facing package contains:

1. purpose/user impact;
2. before/after;
3. exact candidate and changed paths;
4. acceptance Evidence;
5. negative/regression/recovery results;
6. required/optional checks and `NOT_RUN`;
7. findings/deviations/limitations;
8. recommendation;
9. `ACCEPT | NEEDS_CHANGES | REJECT | DEFER` options;
10. one next action.

It contains no generated human decision or implicit Git permission.

### 6.7. Part 2 exit contract

```yaml
outputs:
  frozen_exact_candidate: REQUIRED
  Stage_Record: REQUIRED
  Evidence: REQUIRED
  ValidationEnvelope: REQUIRED_WHEN_TASK_DEMANDS
  Review_Package: REQUIRED
human_decision: NOT_RUN
execution_authorization: CONSUMED_OR_INVALIDATED
Git_authorization: NONE
stop: true
```

## 7. Part 2 acceptance, negatives and recovery

### 7.1. Acceptance

| ID | Case | Expected observable result |
|---|---|---|
| `P2-ACC-001` | fresh exact auth | all bindings match before first action |
| `P2-ACC-002` | one causal change | actual operations remain in preview/task scope |
| `P2-ACC-003` | bounded correction | within unchanged scope and explicit max; new candidate identity |
| `P2-ACC-004` | complete tests | every requirement has positive/negative/Evidence row |
| `P2-ACC-005` | required NOT_RUN | aggregate non-PASS and visible limitation |
| `P2-ACC-006` | reconciliation | intended/actual and out-of-scope preservation proven |
| `P2-ACC-007` | freeze | exact candidate identity immutable before validation |
| `P2-ACC-008` | independent validate | exact subject, zero mutation, complete C-009 envelope |
| `P2-ACC-009` | validation finding | named finding; no fix; correction route only |
| `P2-ACC-010` | review package | decision-ready and no generated decision |
| `P2-ACC-011` | authorization terminal | consumed on first terminal Stage Record |
| `P2-ACC-012` | exit | human decision/Git remain `NOT_RUN`/`NONE` |

### 7.2. Negative fixtures

| Fixture | Defect | Expected result |
|---|---|---|
| `P2-NEG-001-stale-head` | repository identity drift | auth invalidated; zero affected mutation |
| `P2-NEG-002-preview-mismatch` | operation/path differs | denied/new preview required |
| `P2-NEG-003-unrelated-cleanup` | modifies unrelated path | scope failure/recovery required |
| `P2-NEG-004-hidden-next-stage` | EXECUTE launches VALIDATE | prohibited |
| `P2-NEG-005-auto-retry` | failure reruns automatically | prohibited |
| `P2-NEG-006-not-run-pass` | required test skipped but PASS | contract violation |
| `P2-NEG-007-evidence-self-auth` | Evidence used as permission | denied |
| `P2-NEG-008-write-after-freeze` | subject mutated after identity | freeze/validation invalid |
| `P2-NEG-009-validator-fixes` | validator edits subject | validation invalid |
| `P2-NEG-010-self-validation` | author-only claim with no independent subject check | required independent gate fails |
| `P2-NEG-011-partial-no-journal` | interruption not recoverable | critical execution failure |
| `P2-NEG-012-review-autoaccept` | package contains generated ACCEPT | invalid human decision source |

### 7.3. Recovery

| ID | Failure | Recovery |
|---|---|---|
| `P2-REC-001` | auth/preflight mismatch before write | new preflight/preview and human authorization |
| `P2-REC-002` | partial mutation | stop; preserve journal; new recovery Task/auth; reconcile and revalidate |
| `P2-REC-003` | scope expansion discovered | stop; revise Task/contract/authorization as affected |
| `P2-REC-004` | required test unavailable | explicit `NOT_RUN`; restore capability then rerun exact check/candidate |
| `P2-REC-005` | validation finding | separate bounded correction, new freeze, full affected revalidation |
| `P2-REC-006` | correction limit exhausted | human decision; no self-heal loop |

## 8. Part 3 — Human decision to handoff

### 8.1. Human Decision Record

An authentic C-011 record must bind:

- candidate ID/revision/SHA;
- explicit human actor/channel/time;
- verbatim or normalized statement naming subject;
- decision `ACCEPT | NEEDS_CHANGES | REJECT | DEFER`;
- changes empty for `ACCEPT`;
- superseded decision refs when applicable.

Agent recommendation, UI state, copied text, Evidence, PASS or stale-subject statement is invalid.

### 8.2. Decision consequences

| Decision | Allowed consequence | Forbidden implication |
|---|---|---|
| `ACCEPT` | exact artifact becomes accepted in declared fact class; propose state/handoff update | execution or Git authorization |
| `NEEDS_CHANGES` | new bounded correction task/candidate | modify frozen accepted/review subject in place |
| `REJECT` | close/reject exact subject; preserve evidence | auto-create replacement |
| `DEFER` | preserve subject and stop | treat as accepted or continue implementation |

### 8.3. Correction loop

`NEEDS_CHANGES` invalidates old execution authorization, freeze and validation for the changed subject. Correction creates a new revision/digest, binds named findings and reruns all affected checks. Up to the unchanged-scope limit may be performed. Any product/architecture/scope/authority/Risk Profile change returns to a human decision, irrespective of remaining cycles.

### 8.4. Durable state transition

After an exact human decision, Project Memory may be updated only through separately authorized C3 atomic write. Without that permission, the pipeline emits a read-only proposed update:

```text
ProposedMemoryUpdate = {
  current_memory_ref,
  decision_ref,
  intended_field_changes,
  expected_new_refs,
  one_next_action,
  permission: HUMAN_AUTHORIZATION_REQUIRED
}
```

Registries are rebuilt from new authoritative sources after the memory/record writes, not patched as owners. Missing state-write permission is honest `NOT_RUN`, not failure of the accepted decision itself.

### 8.5. Git lifecycle

Each action has separate preflight, authorization and `C-014` record:

```text
candidate acceptance
≠ Commit authorization
≠ Push authorization
≠ Merge authorization
≠ Release authorization
```

| Action | Fresh observations | Exact binding | Invalidation |
|---|---|---|---|
| Commit | worktree/index/diff/HEAD | exact accepted candidate/path set | any candidate/index drift |
| Push | local commit/remote/branch/divergence | exact commit and remote branch | local/remote drift |
| Merge | source/target heads/PR/checks/conflicts | exact source/target/candidate | head/check/conflict change |
| Release | accepted merged commit/version/artifacts/checks | exact release subject | any artifact/commit/version change |

No action is bundled or inferred. If authorization is absent, record `NOT_RUN` and continue read-only handoff.

### 8.6. Handoff and lesson proposal

Handoff contains:

- repository/candidate/task identities and freshness timestamp;
- technical result and human decision as separate axes;
- actual changes and preserved out-of-scope state;
- checks run/not run/findings/blockers/limitations;
- current permission/authorization/Git states;
- recovery status;
- task-scoped context refs;
- one next action and terminal stop.

A lesson proposal is allowed only from repeatable observed signal with provenance, affected mechanism, prevention and regression candidate. It does not become accepted rule automatically and cannot activate the next slice.

### 8.7. Part 3 exit contract

```yaml
outputs:
  Human_Decision_Record: REQUIRED
  Project_Memory_update: AUTHORIZED_OR_NOT_RUN
  Registry_rebuild: AUTHORIZED_OR_NOT_RUN
  Git_records:
    commit: AUTHORIZED_AND_RUN_OR_NOT_RUN
    push: AUTHORIZED_AND_RUN_OR_NOT_RUN
    merge: AUTHORIZED_AND_RUN_OR_NOT_RUN
    release: AUTHORIZED_AND_RUN_OR_NOT_RUN
  handoff: REQUIRED
  one_next_action: REQUIRED
automatic_next_slice_activation: FORBIDDEN
stop: true
```

## 9. Part 3 acceptance, negatives and recovery

### 9.1. Acceptance

| ID | Case | Expected observable result |
|---|---|---|
| `P3-ACC-001` | exact ACCEPT | authentic exact binding; no implied permission |
| `P3-ACC-002` | NEEDS_CHANGES | new correction revision; old auth/freeze/validation invalid |
| `P3-ACC-003` | REJECT/DEFER | subject preserved and route stopped honestly |
| `P3-ACC-004` | no state-write auth | proposed memory update; actual update `NOT_RUN` |
| `P3-ACC-005` | authorized state update | atomic C3 write with decision refs and one next action |
| `P3-ACC-006` | registry consequence | complete rebuild after owner update; registry authority none |
| `P3-ACC-007` | Git absent | all four actions explicitly `NOT_RUN` |
| `P3-ACC-008` | Git authorized separately | one action/record, exact preflight and binding |
| `P3-ACC-009` | handoff | exact current identities/permissions/recovery/one next action |
| `P3-ACC-010` | lesson proposal | observed repeatable signal only; status proposal |
| `P3-ACC-011` | continuation | no automatic next feature/task/slice |

### 9.2. Negative fixtures

| Fixture | Defect | Expected result |
|---|---|---|
| `P3-NEG-001-generated-accept` | agent/UI emits ACCEPT | no human authority |
| `P3-NEG-002-stale-subject-decision` | digest differs | decision invalid for current candidate |
| `P3-NEG-003-accept-with-changes` | ACCEPT lists modifications | invalid; new subject required |
| `P3-NEG-004-accept-as-exec-auth` | acceptance used to execute | denied |
| `P3-NEG-005-state-write-without-auth` | memory updated automatically | prohibited mutation |
| `P3-NEG-006-registry-patched-as-owner` | status changed only in index | stale/invalid state |
| `P3-NEG-007-commit-implies-push` | one Git decision reused | denied |
| `P3-NEG-008-push-implies-merge` | continuation automatic | denied |
| `P3-NEG-009-handoff-stale-head` | old repo identity described current | affected handoff invalid |
| `P3-NEG-010-auto-lesson-rule` | single anomaly becomes normative | remains proposal/rejected |
| `P3-NEG-011-auto-next-slice` | accepted task starts next | prohibited |

### 9.3. Recovery

| ID | Failure | Recovery |
|---|---|---|
| `P3-REC-001` | human decision authenticity failure | obtain explicit exact statement; do not infer |
| `P3-REC-002` | correction changes material boundary | stop for new human product/architecture/scope/risk decision |
| `P3-REC-003` | memory update interrupted | C3 recovery; decision record remains immutable |
| `P3-REC-004` | Git preflight stale | do not run action; fresh preflight/new authorization |
| `P3-REC-005` | Git partial/remote uncertainty | preserve terminal evidence; re-observe remote/local state before any next action |
| `P3-REC-006` | handoff identity stale | regenerate read-only handoff from fresh observation/refs |

## 10. Synthetic end-to-end simulation fixture

This is a non-authoritative documentation fixture, not a selected AOS product feature.

### 10.1. Scenario

Human intent: “Нужен локальный трекер прочитанных книг, чтобы сохранять название и отмечать завершение без облака.”

Expected route:

1. `INCOMPLETE_IDEA` intake preserves text; clarifies primary user/outcome only if material.
2. C-001 separates problem/outcome from “tracker” solution and records offline constraint.
3. Human accepts exact Intent revision.
4. Product Spec defines one user, local-only boundary, journey and success signal.
5. Human selects one feature: add/list/complete a book; exact Feature Contract defines JSON/file behavior and recovery.
6. Architecture choice only if persistence option remains material; otherwise accepted default/decision ref used.
7. Task compiler emits one smallest task with paths/tests/recovery; no full backlog.
8. Preflight/preview observes repository; human assigns Risk Profile and separately authorizes exact execution.
9. Executor journals one causal change, runs positive/negative tests, reconciles and freezes candidate.
10. Independent validator reads the same frozen candidate and produces C-009 without mutation.
11. Review Package presents Evidence and decision options; human explicitly accepts/changes/rejects/defers.
12. State/Git consequences run only when separately authorized; otherwise `NOT_RUN`.
13. Handoff records exact state, permissions and one next action; no auto-next feature.

### 10.2. Simulation oracles

- no step requires chat-only facts;
- every state transition names input/output owner and gate;
- acceptance never becomes execution/Git permission;
- partial write has journal/recovery;
- one exact Task Brief exists, not a generated backlog;
- required checks and negatives have Evidence locators;
- final handoff is usable from repository records alone.

## 11. Cross-part traceability

| Part | Feature relationship | Core contracts | Lessons/regressions |
|---|---|---|---|
| Part 1 | H1 `FTR-001`; later relationships `FTR-003/005/006/007/009/016` do not alter dispositions | `C-001…C-007`, C3/C5/C6 | `LES-001…007`, `017`, `022`, `030`, `032…035`, `037`; `SCOPE`, `LINK`, `STATE` |
| Part 2 | supporting `FTR-006/011/012/013`; future `FTR-009/010/014/019` only as contract relationship | `C-005…C-010`, C2/C6/C7 | `LES-005`, `008…025`, `031`, `038`; `AUTH`, `STATUS`, `SCOPE`, `PARTIAL`, `FREEZE`, `SELFREF` |
| Part 3 | `FTR-012`; future `FTR-014/015/016/025` relationship | `C-008…C-014`, C3/C5/C6 | `LES-008…012`, `023…028`, `036`, `038`, `039`; `AUTH`, `STATE`, `GIT`, `BASELINE` |

Normative first-cycle feature scope remains owned by accepted H1. This table is traceability, not selection.

## 12. Package acceptance matrix

| Gate | Required result |
|---|---|
| one example traverses all parts without chat | `PASS` |
| every transition names owner/input/output/gate | `PASS` |
| product/technical/human/permission/Git axes separate | `PASS` |
| every write-capable step has pre-write/partial/recovery | `PASS` |
| correction loop bounded and no self-heal | `PASS` |
| no full backlog or auto-next | `PASS` |
| coding agent receives exact task rather than redesigning process | `PASS` |

## 13. Candidate status

```yaml
DOC-009:
  part: PART_1
  technical_result: PASS
  human_acceptance: NOT_RUN
DOC-010:
  part: PART_2
  technical_result: PASS
  human_acceptance: NOT_RUN
DOC-011:
  part: PART_3
  technical_result: PASS
  human_acceptance: NOT_RUN
pipeline_contract:
  readiness: READY_FOR_FINAL_PACKAGE_REVIEW
  dependency_status: PROVISIONAL_C012_V2_CORE_C3_C7
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
next_required_action: CONTINUE_DOC-012_INDEPENDENT_READ_ONLY_SIMULATION
stop: false
```
