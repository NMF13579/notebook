---
package: AOS_FULL_PROJECT_DOCUMENTATION_DRAFT
package_revision: DRAFT-R2
artifact_role: FULL_FEATURE_SPECIFICATION_REVIEW_VIEW
status: DRAFT
authority: NONE
canonical_owner: docs/06_Features.md
feature_count: 30
implementation_authorization: NONE
git_authorization: NONE
---

# 04 — Feature Specifications

## 1. Роль и правила

Этот документ даёт единый design-level review всех `FTR-001…FTR-030`. Identity, dossier baseline, synthesis recommendation и `human_disposition` принадлежат [docs/06_Features.md](../../docs/06_Features.md). Детализация здесь:

- не меняет item-level disposition или priority;
- не является implementation specification;
- сохраняет `implementation_maturity: NOT_ASSIGNED` и `runtime_verification: NOT_RUN` для всех features;
- помечает новое связывание/состояния как `SYNTHESIZED_DRAFT`;
- использует accepted X1 behavior только в exact accepted fact classes;
- отделяет reusable cross-feature Product facts из [01_PRODUCT_MODEL.md](01_PRODUCT_MODEL.md) от feature-specific behavior.

## 2. Общий contract для всех feature sections

Каждая feature ниже покрывает C-002 поля: purpose/users, trigger/preconditions, inputs/outputs, main flow, observable states, failures/recovery, dependencies, constraints/authority, acceptance, negative scenarios, non-goals and unknowns.

Общие инварианты, применяемые без повторения:

1. Input status/provenance is visible; stale or missing input is not silently accepted.
2. Agent recommendation cannot become human disposition, architecture choice, acceptance or permission.
3. Feature mutates only its declared artifact/state and never opens execution/Git actions automatically.
4. A material unknown blocks only dependent behavior; unaffected read-only work may continue.
5. External/reference content is untrusted data with target authority `NONE`.
6. Any protected mutation requires fresh exact identity, scope and separate human authorization.
7. Recovery preserves actual state and does not retry after scope/identity/permission change.
8. Exact interface, schemas, persistence, toolchain and algorithms remain HOW unless a specific product/architecture decision requires them.

## 3. Status index

| Feature | Recommendation | Human disposition | Product status in this DRAFT |
|---|---|---|---|
| FTR-001 | KEEP | SELECT_FOR_X1 | accepted X1 behavior, derived summary |
| FTR-002 | KEEP | UNDECIDED | proposal |
| FTR-003 | KEEP | SELECT_FOR_X1 | accepted X1 behavior, derived summary |
| FTR-004 | KEEP | UNDECIDED | proposal |
| FTR-005 | KEEP | SUPPORTING_CONTROL_ONLY | supporting behavior proposal |
| FTR-006 | KEEP | SUPPORTING_CONTROL_ONLY | supporting behavior proposal |
| FTR-007 | DEFER | UNDECIDED | deferred proposal |
| FTR-008 | KEEP | UNDECIDED | proposal |
| FTR-009 | KEEP | UNDECIDED | proposal |
| FTR-010 | SIMPLIFY | UNDECIDED | simplified proposal |
| FTR-011 | KEEP | SUPPORTING_CONTROL_ONLY | supporting behavior proposal |
| FTR-012 | KEEP | SUPPORTING_CONTROL_ONLY | supporting behavior proposal |
| FTR-013 | KEEP | SUPPORTING_CONTROL_ONLY | supporting behavior proposal |
| FTR-014 | KEEP | UNDECIDED | proposal |
| FTR-015 | KEEP | UNDECIDED | proposal |
| FTR-016 | KEEP | UNDECIDED | proposal |
| FTR-017 | DEFER | UNDECIDED | deferred proposal |
| FTR-018 | DEFER | UNDECIDED | deferred proposal |
| FTR-019 | KEEP | UNDECIDED | proposal |
| FTR-020 | DEFER | UNDECIDED | deferred proposal |
| FTR-021 | DEFER | UNDECIDED | deferred proposal |
| FTR-022 | KEEP | UNDECIDED | proposal |
| FTR-023 | DEFER | UNDECIDED | deferred proposal |
| FTR-024 | DEFER | UNDECIDED | deferred proposal |
| FTR-025 | KEEP | UNDECIDED | proposal |
| FTR-026 | DEFER | UNDECIDED | deferred proposal |
| FTR-027 | DEFER | UNDECIDED | deferred proposal |
| FTR-028 | DEFER | UNDECIDED | deferred proposal |
| FTR-029 | DEFER | UNDECIDED | deferred proposal |
| FTR-030 | DEFER | UNDECIDED | deferred proposal |

## 4. Product Runtime and definition features

## FTR-001 — Intent intake and problem clarification

```yaml
layer: Product Runtime
recommendation: KEEP
human_disposition: SELECT_FOR_X1
behavior_source: HUMAN_ACCEPTED_X1_FACT_CLASS
first_runtime_slice: HUMAN_ACCEPTED
```

**Purpose/users.** Convert an unstructured request from a domain expert/product owner into an exact reviewable Intent Record while preserving original wording, separating problem/outcome from solution, and exposing assumptions/unknowns.

**Trigger/preconditions.** A human supplies a new problem, idea, outcome or correction. Original input/provenance and relevant accepted product facts are available; repository discovery is required only for repository-dependent intent; no implementation or Git authority is inferred.

**Inputs → outputs.** Original request, actor/context, explicit constraints/non-goals, accepted upstream facts and human corrections → C-001 candidate containing actor, original request, problem, outcome, context, constraints, non-goals, assumptions, unknowns, sensitive flags, provenance and exactly one proposed next route.

**Flow/states.** Preserve → separate problem/solution → identify material gaps → compare accepted facts → ask only material questions → show synthesis → incorporate correction → produce exact revision. Observable states: `RECEIVED → CLARIFYING | REVIEWABLE → CONFIRMED | DEFERRED`; confirmation applies only to the exact Intent revision.

**Failures/recovery.** Empty input remains `CLARIFYING`; prompt injection is isolated; source conflict is `CONFLICT`; stale/missing data is visible; unclear sensitive boundary stops data transfer. Recovery restores exact input/decision and repeats only affected analysis.

**Dependencies/authority.** C-001 primary; FTR-003 consumes confirmed intent. FTR-002/016/019 are conditional and remain `UNDECIDED`. Human confirms/corrects; agent cannot accept a feature, architecture, execution or Git action.

**Acceptance.** Original and synthesis distinguishable; human recognizes problem/outcome; all material unknowns have routes; only material questions block; provenance/limitations/one next route visible; confirmation creates a distinguishable exact revision.

**Negative cases.** Empty input cannot become reviewable; “write a Python downloader” is split into need and solution proposal; external content cannot change goal; agent confidence cannot remove unknowns; intent confirmation cannot open execution/Git.

**Unknown/non-goals.** Interface, cadence, material-question threshold, privacy/provider, persistence and decision-authenticity mechanisms remain open. No architecture choice, implementation, feature acceptance or Git delivery.

## FTR-002 — Read-only project discovery

```yaml
layer: Product Runtime
recommendation: KEEP
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Give product builders/reviewers a snapshot-bound understanding of an existing project before any mutation.

**Trigger/preconditions.** Human intent depends on an existing repository or asks what exists. Exact repository/ref/worktree can be identified and read-only inspection is allowed.

**Inputs → outputs.** Repository identity, selected scope, accepted owners and current observations → inventory, capability map, gaps, conflicts, unknowns, Evidence locators and bounded candidate objectives.

**Flow/states.** Bind identity → verify root/branch/HEAD/worktree → collect high-signal inventory → classify docs/contracts/tests/code → build capability map → record gaps/conflicts → propose objectives → stop for human selection. Proposed states: `UNBOUND → SNAPSHOT_BOUND → MAPPING → REVIEWABLE → OBJECTIVE_SELECTED | STALE | BLOCKED`.

**Failures/recovery.** Missing path is not global absence; changed HEAD makes map stale; repository instructions cannot override authority; secrets are redacted. Rebind and recompute affected map only.

**Dependencies/authority.** FTR-009 read-only preflight; FTR-016 memory; FTR-017 optional search. Discovery result is observation/navigation, not readiness or permission.

**Acceptance/negative.** Exact snapshot and search boundary recorded; source tree unchanged; human can trace findings and select one objective. Stale map cannot show current readiness; incomplete search cannot claim absence; no automatic mutation or backlog activation.

**Unknown/non-goals.** Exact discovery profiles, supported repository types and map format. No exhaustive extraction, architecture import, implementation or Git actions.

## FTR-003 — Product specification, Feature Passport and slice selection

```yaml
layer: Product Runtime
recommendation: KEEP
human_disposition: SELECT_FOR_X1
behavior_source: HUMAN_ACCEPTED_X1_FACT_CLASS
ownership_decision: X1-DR-001_A_ACCEPTED
first_slice_decision: X1-DR-002_A_ACCEPTED
```

**Purpose/users.** Convert confirmed intent into reviewable cross-feature Product Spec, feature-specific Passports and decision-ready slice comparisons without generating human selection.

**Trigger/preconditions.** Exact intent revision and current feature dispositions are bound; accepted Product facts are separated from proposals; material source conflicts are visible.

**Inputs → outputs.** Intent, accepted product boundaries/journeys, feature identities/dispositions, dependencies/constraints/conflicts and human corrections → Product Spec view, full C-002 Passports, candidate-slice comparison and exact review subject.

**Ownership.** Accepted option A applies: Product Spec owns cross-feature facts; each Passport owns its feature behavior and links to compatible Product Spec revision.

**Flow/states.** Bind inputs → define problem/users/goals/non-goals → draft Product Spec/Passports → detect gaps/dependencies → compare distinct observable slices → present exact options → human selects exact revision. Proposed states: `INPUT_BOUND → SPEC_DRAFT → PASSPORT_DRAFT → SLICE_OPTIONS_READY → WAITING_HUMAN_DECISION → REVISION_SELECTED | DEFERRED`; invalid input goes `BLOCKED_INPUT`.

**Failures/recovery.** Missing/stale intent or disposition stops affected claim; duplicate/conflicting owners become `CONFLICT`; incomplete slice cannot be ready; generated `REQUIRED` or selection is rejected; changed candidate invalidates review. Rebind/correct only affected revision.

**Dependencies/authority.** FTR-001 upstream; C-003/C-002 primary; FTR-005 supporting control. Accepted first runtime slice is FTR-001 alone. FTR-003 does not choose implementation repo/interface/toolchain or authorize execution.

**Acceptance/negative.** Product facts and feature behavior are source-classified; Passports contain all required fields or bounded unknowns; options are distinct and observable; exact revisions bind decisions. Legacy presence, technical PASS or agent recommendation cannot select/admit a feature.

**Unknown/non-goals.** Registry implementation, persistence, metrics, exact schemas/interface/toolchain remain open. No canonical publication or runtime implementation in this DRAFT.

## FTR-004 — Managed bootstrap, install/update/remove and First-Start

```yaml
layer: Product Runtime / Installation Boundary
recommendation: KEEP
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Let a user install, update or remove AOS without hidden writes or loss of user/project-owned state, then understand the first safe action.

**Trigger/preconditions.** Human requests a named operation; package and target identities are exact; ownership policy, conflicts, recovery and authorization boundaries are known.

**Inputs → outputs.** C-013 manifest, target inventory, ownership classes, desired operation, preview and exact authorization → verified installation/update/removal result, preserved conflicts/state, recovery data and First-Start guidance.

**Flow/states.** Verify package/target → inventory/classify ownership → exact dry-run → show conflicts → authorize apply → perform the bounded change → verify intended and actual state → show first command/recovery options. The observable outcome is either verified intended state or an exact recoverable partial state, never false success. Proposed states: `DISCOVERED → PREVIEW_READY → WAITING_AUTH → APPLYING → VERIFIED | RECOVERY_REQUIRED`; uninstall is a distinct authorized branch.

**Failures/recovery.** Wrong repo, user-owned collision, interrupted update, checksum mismatch or incomplete rollback stops apply; preserve exact effects, reconcile intended/actual state and retain user data. Changed preview requires reauthorization.

**Dependencies/authority.** C-013, FTR-009 preflight, FTR-011 validation, FTR-014 recovery, FTR-019 permissions. Installer cannot own project files or grant itself uninstall/network/Git authority.

**Acceptance/negative.** Dry-run zero-write; apply matches preview; repeating from verified state does not duplicate effects or erase user state; user state is preserved; first-start is understandable. Silent overwrite, wrong-target apply, unauthorized uninstall and incomplete verification fail.

**Unknown/non-goals.** Distribution format, OS support, install locations, ownership taxonomy and update channel. No auto-update, cloud account or chosen implementation mechanism.

## 5. Architecture and task-control features

## FTR-005 — Architecture need check, options, ADR and traceability

```yaml
layer: Product Runtime Support / Architecture Boundary
recommendation: KEEP
human_disposition: SUPPORTING_CONTROL_ONLY
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Help product owner/architect decide whether a material architecture decision is needed and compare real options without platform-first ceremony.

**Trigger/preconditions.** A selected feature exposes a non-reversible boundary, competing viable approaches or material ownership/security/dependency question.

**Inputs → outputs.** Exact question, accepted constraints, current observations and targeted Evidence → need/no-need rationale or DRAFT C-004 with options, trade-offs, unknowns and decision request.

**Flow/states.** Test need → frame question → form distinct options → compare value/risk/reversibility → expose Evidence/unknowns → human selects/defer → record consequences/traceability. States: `NEED_CHECK → NOT_REQUIRED | OPTIONS_DRAFT → WAITING_DECISION → DECIDED | DEFERRED`.

**Failures/recovery.** Trivial change gets unnecessary ADR; one preselected option is presented; stale repository facts bias comparison; proposal is written as selected. Restore exact question/source and leave selection empty.

**Dependencies/authority.** C-004, FTR-003, optional FTR-002. Human selects architecture. `SUPPORTING_CONTROL_ONLY` does not make FTR-005 independent product scope.

**Acceptance/negative.** Need decision justified; options distinct/comparable; consequences/reversal visible; exact human record linked. No dependency install, architecture mutation, generated selection or legacy topology import.

**Unknown/non-goals.** Need heuristic and ADR presentation. No universal architecture phase for every task.

## FTR-006 — Task Brief, scope confirmation, authorization and Stage Report

```yaml
layer: Product Runtime / Development Factory Boundary
recommendation: KEEP
human_disposition: SUPPORTING_CONTROL_ONLY
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Convert accepted outcome into one bounded, reviewable task while separating description, human authorization and actual report.

**Trigger/preconditions.** Accepted product/feature/architecture inputs exist and a future implementation action is requested in an exact repository.

**Inputs → outputs.** Goal/outcome, exact subject, scope, operations, constraints, unknowns, risk factors, acceptance and stop conditions → C-005 Task Brief; separate C-006 authorization when issued; C-008/Stage Report after execution.

**Flow/states.** Draft goal/scope → classify unknown/risk → define checks/stops → validate brief → request exact authorization → future executor consumes once → report actual result. States: `DRAFT → REVIEWABLE → WAITING_AUTH → AUTHORIZED | REJECTED/EXPIRED → CONSUMED → REPORTED` across separate orthogonal records.

**Failures/recovery.** Malformed/idle task bypass, stale/copied auth, mismatch paths/operations, unassigned human risk or NOT_RUN→PASS. Reject affected transition and regenerate/reconfirm exact record.

**Dependencies/authority.** C-005/C-006/C-008, FTR-009/012. Brief never grants permission; authorization never grants Git; report never grants acceptance.

**Acceptance/negative.** Machine-reviewable bounded scope; exact auth actor/subject; one stage; actual diff/checks reported honestly. No implicit task activation, risk assignment, scope expansion or hidden next stage.

**Unknown/non-goals.** Exact schema/expiry/consumption mechanism and routine-vs-protected thresholds. No implementation in documentation repository.

## FTR-007 — Hierarchical backlog and lazy decomposition

```yaml
layer: Development Factory
recommendation: DEFER
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Help product builders order large work without speculative full decomposition or automatic activation.

**Trigger/preconditions.** Accepted outcome cannot be executed safely as one bounded task and material child boundaries are identifiable.

**Inputs → outputs.** Parent outcome/acceptance, dependencies, blockers and near-term decisions → derived candidate hierarchy and ordered queue with one human-selected active task.

**Flow/states.** Define parent acceptance → create only near-term children → explain contribution/dependencies → detect cycles/blockers → propose order → human activates one. States: `PARENT_DEFINED → CANDIDATES → ORDER_PROPOSED → ONE_ACTIVE | BLOCKED | DEFERRED`.

**Failures/recovery.** Orphan child, circular dependency, closed-child-as-parent-complete, stale derived queue or automatic activation. Rebuild queue from owner artifacts and exact decisions.

**Dependencies/authority.** FTR-003, FTR-006, FTR-016. Queue is navigation, not Source of Truth; human selects/activates work.

**Acceptance/negative.** Every child contributes to parent acceptance and exposes dependency; no unnecessary descendants; one exact next task. No full upfront program bureaucracy, autonomous scheduling or scope creation.

**Unknown/non-goals.** Queue persistence, hierarchy limits and collaboration behavior; deferred until repeated multi-task need.

## FTR-008 — Status / Next / Details, tutor and closure UX

```yaml
layer: Product Runtime
recommendation: KEEP
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Let a nontechnical user understand current state, blocker, missing authority and one next action without navigating raw artifacts.

**Trigger/preconditions.** User starts/resumes work or a run terminates; source-owned state and current observations can be refreshed.

**Inputs → outputs.** Owners, exact subject, mutable repository facts, findings, decisions, permissions and freshness → plain-language `Status`, one `Next`, optional `Details`, source links and closure explanation.

**Flow/states.** Load owners → refresh mutable facts → detect stale/conflict/blocker → derive concise status → select one safe next route → expose details/provenance. View states reflect sources: `CURRENT`, `WAITING_HUMAN`, `BLOCKED`, `STALE`, `COMPLETE_FOR_SCOPE`; they do not mutate lifecycle.

**Failures/recovery.** Stale projection says READY; multiple equal “next” actions; NOT_RUN hidden; UI creates approval. Mark view stale, rebind sources and show exact decision requirement.

**Dependencies/authority.** FTR-016, FTR-011/012. Display-only by default; source artifacts and human records retain authority.

**Acceptance/negative.** User can explain state and act on one next route; freshness and limitations visible; details optional. No color-only status, jargon-only blocker, implicit permission or dashboard truth.

**Unknown/non-goals.** Exact interface, notification/push behavior and personalization. No mandatory dashboard/SaaS.

## FTR-009 — Repository/action preflight and exact preview

```yaml
layer: Development Factory / Safety Boundary
recommendation: KEEP
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Prevent mutation against the wrong repository, stale baseline, contaminated worktree or ambiguous action set.

**Trigger/preconditions.** Any repository-dependent planning/protected action or exact discovery snapshot requires current identity.

**Inputs → outputs.** Task/subject, repository locator, expected branch/HEAD/baseline, path/operation scope, environment/network/remote expectations → read-only C-007 preview with classifications, conflicts, permissions and identity.

**Flow/states.** Verify root/worktree → bind branch/HEAD/baseline → classify dirty state → normalize paths → inspect relevant environment/remote → render exact operations → freeze preview. States: `UNBOUND → INSPECTING → PREVIEW_READY | BLOCKED`; any drift becomes `STALE`.

**Failures/recovery.** Traversal/symlink escape, wrong repo, changed HEAD, raw secret output, read-only side effect or user state contamination. Stop, preserve state, correct locator/scope and rerun read-only.

**Dependencies/authority.** FTR-006, FTR-019, FTR-014. Preflight can classify permission but cannot issue it or execute.

**Acceptance/negative.** Zero writes; exact subject/actions/paths; dirty state and limitations visible; changed premise invalidates preview. No cleanup, staging, fetch/pull or network action without separate scope.

**Unknown/non-goals.** Cross-platform path/environment profiles and remote-provider checks. No universal environment scan.

## FTR-010 — Scoped execution workflow and bounded execution outcomes

```yaml
layer: Development Factory
recommendation: SIMPLIFY
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Ensure actual mutation cannot exceed prose scope and produces the smallest observable execution outcome needed, without requiring a broad Control Plane.

**Trigger/preconditions.** Exact accepted task outcome, fresh C-007 preview and valid unconsumed C-006 authorization exist.

**Inputs → outputs.** Authorization, preview, bounded operation and recovery/check plan → actual mutation, exact effect record, intended-versus-actual reconciliation, focused checks, C-008 Stage Report and new candidate identity.

**Flow/states.** Validate auth/preview → perform smallest operation → record every mutation/side effect → run authorized check → reconcile intended/actual → terminal report/stop. States: `READY → EXECUTING → RECONCILING → REPORTED` or `FAILED/RECOVERY_REQUIRED`.

**Failures/recovery.** Unexpected path, stale preview, permission boundary, partial write or tool failure immediately stops further mutation. Preserve exact partial state and observable effects, then require bounded recovery/correction; no automatic retry after boundary change.

**Dependencies/authority.** FTR-006/009/013/014/019. One stage; no scope expansion, privilege escalation, validation claim or Git delivery.

**Acceptance/negative.** Only authorized changes occur; actual diff matches report; partial failure detectable/recoverable; authorization consumed once. No hidden retry, background mutation, unrelated cleanup or automatic next stage.

**Unknown/non-goals.** Exact execution primitives, sandbox and process model. Full orchestration, distributed execution and self-heal are deferred.

## 6. Validation, review, recovery and continuity features

## FTR-011 — Unified Result Contract, Validate, Doctor and Self-Test

```yaml
layer: Product Runtime Support / Development Factory
recommendation: KEEP
human_disposition: SUPPORTING_CONTROL_ONLY
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Give implementers/reviewers one stable technical-result contract and official validation entrypoint so incompatible validators cannot create false green.

**Trigger/preconditions.** An exact candidate and declared required/optional checks exist; validator environment/import provenance is knowable; validation is read-only.

**Inputs → outputs.** Candidate identity, contract/acceptance matrix, check profile and environment → C-009 ValidationEnvelope with per-check results, `NOT_RUN`, limitations, findings, exit semantics and human-readable summary.

**Flow/states.** Strict-load contract → verify subject/environment → run required then relevant optional checks → record Evidence → aggregate fail-closed → emit machine/human result → stop. States: `SUBJECT_BOUND → CHECKING → PASS | FAIL | BLOCKED | UNKNOWN | CONTRACT_VIOLATION`.

**Failures/recovery.** Unknown enum, wrong interpreter/import, exit 0 on failure, optional checker mistaken as required, required check omitted or read-only write. Report exact defect; repair checker/candidate in a separate boundary and rerun full applicable suite.

**Dependencies/authority.** C-009, FTR-013, optional FTR-023. `SUPPORTING_CONTROL_ONLY`; PASS never accepts product/candidate or starts correction.

**Acceptance/negative.** Stable vocabulary/exit mapping; every required check has terminal state; required `NOT_RUN` prevents PASS; subject/method/limitations reproducible. No self-approval, hidden candidate edit or multiple conflicting official entrypoints.

**Unknown/non-goals.** Exact executable/schema/plugin profiles. No runtime implementation or universal test tool in this documentation.

## FTR-012 — Evidence, human review, semantic guard and decision record

```yaml
layer: Product Runtime / Review Boundary
recommendation: KEEP
human_disposition: SUPPORTING_CONTROL_ONLY
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Present an exact result to a nontechnical human with enough Evidence, limitations and options to make a real decision without confusing technical success with acceptance.

**Trigger/preconditions.** Exact candidate and available Evidence are frozen; review criteria and decision scope/fact classes are known.

**Inputs → outputs.** Candidate, before/after, scope, C-009/C-010 records, findings, `NOT_RUN`, remaining risk and options → one review package; later exact human-authored C-011 decision record.

**Flow/states.** Verify candidate → map Evidence to criteria → summarize user impact → expose gaps/limitations → offer valid options → capture/verify human record. States: `EVIDENCE_READY → REVIEWABLE → WAITING_HUMAN → ACCEPTED | NEEDS_CHANGES | REJECTED | DEFERRED`; decision axis remains separate.

**Failures/recovery.** Missing actor/subject, generated ACCEPT, stale candidate, Evidence without criterion, hidden negative result or semantic claim unsupported by mechanical checks. Reject invalid record and return to exact candidate/Evidence boundary.

**Dependencies/authority.** C-010/C-011, FTR-011/013. Agent/reviewer cannot approve; Evidence/report/UI has no human authority.

**Acceptance/negative.** Every criterion/result/limitation visible; user impact understandable; exact actor/source/time/subject/fact classes recorded. No decision inference from PASS, candidate presence, click without record or prior historical acceptance.

**Unknown/non-goals.** Future identity/authenticity mechanism, presentation modality and signature policy. No automatic approval/canonical publication/Git action.

## FTR-013 — Scope reconciliation, isolated validation and candidate freeze

```yaml
layer: Development Factory / Validation Boundary
recommendation: KEEP
human_disposition: SUPPORTING_CONTROL_ONLY
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Ensure validators/reviewers examine one immutable, uncontaminated candidate that matches the authorized scope.

**Trigger/preconditions.** Authoring/execution ends; exact artifact inventory, baseline and candidate bytes can be computed; no further mutation is planned inside subject.

**Inputs → outputs.** Task/preview/execution records, baseline, exact files/bytes and source provenance → deterministic candidate manifest/identity, optional isolated subject and scope-reconciliation Evidence.

**Flow/states.** Finalize inventory → compute hashes → reject self-reference/collision → freeze subject → copy/isolate when material → compare brief/preview/diff → validate exact identity. States: `MUTABLE → BINDING → FROZEN → VALIDATING → INVALIDATED | REVIEW_READY`.

**Failures/recovery.** Byte change, moved HEAD, extra/missing file, self-reference, import from live checkout or contaminated worktree invalidates candidate. Restore intended scope, create new identity and rerun validation.

**Dependencies/authority.** FTR-009/010/011. `SUPPORTING_CONTROL_ONLY`; validation subject binding creates no acceptance or Git permission.

**Acceptance/negative.** Every included artifact byte-bound; any change detected; actual scope matches task; isolation/provenance explicit. No provisional identity, silent file inclusion, live-candidate mutation or reuse of old PASS.

**Unknown/non-goals.** Exact manifest format per future implementation and isolation strategy. No mandatory container/worktree for every low-risk task.

## FTR-014 — Recovery, resume, rollback and session handoff

```yaml
layer: Product Runtime / Development Factory Boundary
recommendation: KEEP
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Preserve truthful state after failure/interruption so a user or new agent can choose a bounded resume, correction or rollback without unsafe guessing.

**Trigger/preconditions.** A run stops unexpectedly, produces partial writes, is denied, reaches a blocker or must hand off across sessions/tools.

**Inputs → outputs.** Intended scope, authorization, exact effect record/diff, last exact identity, checks/findings/decisions/permissions → recovery package/C-012 handoff with options and exactly one recommended next action.

**Flow/states.** Stop mutation → preserve state/logs → classify partial changes → reconcile intended/actual → identify safe options → request human decision if destructive/material → recheck before resume. States: `INTERRUPTED → ASSESSED → RECOVERY_READY → RESUMED | ROLLED_BACK | DEFERRED`; denied actions remain logged.

**Failures/recovery.** Blind retry after permission violation, stale handoff, unknown shown as READY, destructive rollback inferred or partial data erased. Rebind sources/identity and obtain exact decision where needed.

**Dependencies/authority.** FTR-010/016/019 and C-012. Recovery cannot expand scope/authority; rollback is separate protected mutation when material.

**Acceptance/negative.** Partial writes detectable; resume reproducible; denied boundary visible; user data preserved; next action exact. No automatic retry, silent cleanup, stale permission reuse or handoff-as-Source-of-Truth.

**Unknown/non-goals.** Recovery storage/retention, rollback mechanisms and cross-tool handoff format. No universal transaction engine.

## FTR-015 — Git lifecycle and independent delivery permissions

```yaml
layer: Development Factory / Delivery Boundary
recommendation: KEEP
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Let the human complete repository delivery deliberately, with Commit, Push, Merge and Release treated as distinct actions bound to current state.

**Trigger/preconditions.** Exact accepted/reviewed candidate exists and user requests one named Git/release action; repository/remote state and action authority are current.

**Inputs → outputs.** Candidate identity, repo/branch/HEAD/status, remote/PR/release facts and exact authorization → one C-014 action record plus reverified resulting state.

**Flow/states.** Rebind local/remote → confirm exact action/subject → execute only named action → verify result → report/stop. Separate branches: `READY_FOR_COMMIT`, `COMMITTED`, `READY_FOR_PUSH`, `PUSHED`, `READY_FOR_MERGE`, `MERGED`, `READY_FOR_RELEASE`, `RELEASED`; no automatic transition.

**Failures/recovery.** Stale SHA, changed worktree, remote divergence, branch protection, auth failure, secret-bearing output or partial remote action. Stop, preserve exact result and request a new bounded action.

**Dependencies/authority.** C-014, FTR-012/013/019; FTR-024 for release package. Each action human-authorized separately; no force default.

**Acceptance/negative.** Unauthorized action blocked; result/repo/remote exact; no unrelated staging. Commit cannot push; push cannot merge; merge cannot release; changed candidate requires revalidation.

**Unknown/non-goals.** Hosting/PR/release provider, branching/versioning policies. No auto-merge, force push, tag, deployment or release by implication.

## FTR-016 — Project Memory, session continuity and Context Pack

```yaml
layer: Product Runtime / Development Factory Boundary
recommendation: KEEP
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Preserve minimal durable context between sessions/agents while avoiding context overload or a stale competing Source of Truth.

**Trigger/preconditions.** A task starts/resumes/hands off; authoritative owners and mutable repository facts can be identified.

**Inputs → outputs.** Accepted decisions/contracts, current observations, candidate/results/findings/permissions and task need → source-linked Project Memory/C-012 and explained task-scoped Context Pack.

**Flow/states.** Load accepted facts → refresh mutable observations → select relevant owners/fragments → explain inclusion → verify hash/freshness → present context/handoff. States: `UNBOUND → SOURCE_BOUND → CURRENT | STALE | INCOMPLETE`.

**Failures/recovery.** Old HEAD, omitted material owner, sensitive leakage, index-promoted proposal, excessive unrelated context or silent background mutation. Rebuild from owners and re-observe current state.

**Dependencies/authority.** FTR-008; optional FTR-017. Memory/index are derived and cannot own product, repository, decision or permission facts.

**Acceptance/negative.** New session identifies exact status/next action; every included fact links to source/reason/freshness; stale/missing data visible. No memory-as-authority, hidden broad ingestion or permanent prompt dump.

**Unknown/non-goals.** Persistence, retention, selection heuristics, privacy and cross-agent format. No full RAG prerequisite.

## 7. Search, routing, trust and Governance features

## FTR-017 — RAG-light context index and search

```yaml
layer: Supporting Runtime
recommendation: DEFER
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Improve retrieval in large source sets only after direct search/context selection is measurably insufficient.

**Trigger/preconditions.** Search benchmark demonstrates material recall/time/context problem; approved corpus, authority metadata and rebuild rules exist.

**Inputs → outputs.** Source-bound corpus/commit/hashes, query and access policy → explained candidate results with source, authority, freshness, confidence/coverage and direct-search fallback.

**Flow/states.** Build/rebuild approved index → bind source identity → query → return ranked candidates with provenance → validate freshness → fall back to direct source. States: `ABSENT → BUILDING → CURRENT → STALE → REBUILD_REQUIRED`.

**Failures/recovery.** Stale/deleted sources, incomplete coverage, privacy leak, old entry shown as current truth or index used to promote proposal. Reject stale result and rebuild/delete affected index data.

**Dependencies/authority.** FTR-016/021. Derived-only; no authority or permission; privacy boundary explicit.

**Acceptance/negative.** Demonstrable retrieval improvement; stale index rejected; coverage/limits visible; direct source remains available. No vector DB by default, hidden corpus ingestion or readiness from retrieval alone.

**Unknown/non-goals.** Need benchmark, indexing method, metadata/retention and provider choice. Deferred until measured need.

## FTR-018 — Advisory model/provider routing

```yaml
layer: Development Factory
recommendation: DEFER
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Recommend a sufficient model/provider/role for a task using measured quality, cost and privacy, without changing scope or permission.

**Trigger/preconditions.** Multiple viable approved options exist and routing benefit can be measured on real task classes; provider/data policy is explicit.

**Inputs → outputs.** Task/risk classification, privacy policy, provider capabilities/costs, measurements and human preferences → advisory routing record with selected human option, attempts/fallback and outcome metrics.

**Flow/states.** Classify task → filter policy-compatible providers → compare sufficient options → recommend → human selects → execute under unchanged permissions → record outcome. States: `UNCLASSIFIED → OPTIONS_READY → WAITING_SELECTION → ROUTED | BLOCKED_POLICY`.

**Failures/recovery.** Unapproved provider, silent fallback, fallback raises privilege/scope, consensus treated as authority or assumed benchmark. Stop transfer/action; return to approved option/human selection.

**Dependencies/authority.** FTR-019, FTR-006 and provider policy. Advisory first; explicit roles; no authority from model count or confidence.

**Acceptance/negative.** Selection/audit visible; data boundary honored; quality/cost measured; fallback explicit. No mandatory multi-agent cascade, hidden provider switch or static preference described as guaranteed runtime fallback.

**Unknown/non-goals.** Providers/models, evaluation set, pricing/privacy and routing thresholds. Deferred until real measurements.

## FTR-019 — Action Trust Boundary and permission classifier

```yaml
layer: Minimal Safety Floor
recommendation: KEEP
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Classify proposed actions deterministically by write/network/data/Git/authority risk and isolate untrusted external instructions.

**Trigger/preconditions.** A proposed action crosses or may cross a repository, filesystem, network, provider, sensitive-data, human-authority or Git boundary.

**Inputs → outputs.** Normalized action, exact subject/scope, current policy/allowlists, required authority and unknowns → `ALLOWED | HUMAN_AUTHORIZATION_REQUIRED | BLOCKED_POLICY | BLOCKED_UNKNOWN | NOT_APPLICABLE` with exact reason/affected boundary.

**Flow/states.** Normalize action → identify trust boundaries → evaluate policy/authority → classify → explain → do not execute. Re-evaluate on relevant drift.

**Failures/recovery.** Path traversal, prompt injection, missing auth treated as allowed, classifier output treated as approval, or low-risk unknown blocking everything. Deny only affected action and restore trusted sources/decision.

**Dependencies/authority.** Core Minimal Safety, FTR-009 and provider/sensitive policy. Classifier cannot approve, assign human Risk Profile or expand permissions.

**Acceptance/negative.** High-risk unknown blocks affected action; safe read-only route may continue; reason and required resolution explicit. No privilege escalation, external instruction authority or default-true protected permission.

**Unknown/non-goals.** Exact taxonomy, policy format and enforcement integration. No full Governance engine required for conceptual classifier.

## FTR-020 — Progressive Governance and isolated enforcement modes

```yaml
layer: Governance / Runtime Enforcement
recommendation: DEFER
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Add runtime enforcement only when stable contracts and repeated incidents show that documentation/manual checks are insufficient.

**Trigger/preconditions.** Exact incident/problem, stable rule, measurable risk/false-positive budget, isolation and rollback are known; human admits feature and mode.

**Inputs → outputs.** Accepted policy contract, target action boundary, measurements and selected mode → `DISABLED | OBSERVE | ENFORCED` operation with findings, metrics and disable/rollback path.

**Flow/states.** Define incident → choose smallest enforcement point → pilot `OBSERVE` → measure false positives/negatives/overhead → human selects `ENFORCED` or disables → monitor/review. Transitions require explicit decision.

**Failures/recovery.** Agent self-enables, missing policy blocks whole product, enforcement corrupts core, false positives exceed budget or optional module cannot be removed. Disable/isolate and revert to manual boundary.

**Dependencies/authority.** FTR-019/021 and stable contracts. Governance cannot create product value/scope, mutate canonical policy or authorize itself.

**Acceptance/negative.** Measured risk reduction, bounded overhead, tested fallback/removal and no authority expansion. No platform-first Control Plane, hidden enforcement or irreversible admission.

**Unknown/non-goals.** Which incidents justify enforcement, isolation mechanism and budgets. Deferred by default.

## 8. Knowledge, quality, operations and extension features

## FTR-021 — Registry/drift detection, Source-of-Truth guard and decision authenticity

```yaml
layer: Development Factory / Governance Support
recommendation: DEFER
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Detect divergence between docs, schemas, CLI, code, tests, registries and human decisions without auto-fixing or creating a new owner.

**Trigger/preconditions.** Multiple representations of one accepted contract exist or a protected decision depends on authenticity/freshness.

**Inputs → outputs.** Owner map, exact representations/snapshots, link/identity rules and decision records → read-only drift/authenticity findings with owner, affected claim, Evidence and resolution requirement.

**Flow/states.** Build derived artifact graph → resolve owners → compare representations → check freshness/links/actor/subject → classify findings → report/stop. States: `BOUND → CONSISTENT | DRIFT_FOUND | AUTHENTICITY_UNKNOWN | BLOCKED`.

**Failures/recovery.** Stale report reused as current PASS; unknown actor accepted; duplicate rule auto-deleted; derived registry becomes canonical. Rebind current sources and create separate correction/decision task.

**Dependencies/authority.** FTR-012/017/030. Read-only and derived; missing authenticity blocks dependent protected transition only.

**Acceptance/negative.** Known seeded drift detected; one owner per fact; report snapshot-bound; decision actor/subject requirements visible. No auto-fix, canonical mutation, generated authenticity or global block from unrelated drift.

**Unknown/non-goals.** Authenticity mechanism, representation graph and check cadence. Deferred until multiple runtime representations exist.

## FTR-022 — Decision and pattern library

```yaml
layer: Knowledge Support
recommendation: KEEP
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Let product builders/agents reuse proven solutions and avoid repeated failures while preserving context, trade-offs and target authority boundaries.

**Trigger/preconditions.** A recurring problem has source Evidence, bounded applicability and reviewed lesson/pattern candidate.

**Inputs → outputs.** Problem, context, solution/alternative, trade-offs, failures, tests, source/temporal scope and fit criteria → curated pattern plus fit/anti-fit assessment for current question.

**Flow/states.** Identify candidate → verify source → define context/forces → compare target fit → present alternatives/risks/tests → human accepts pattern entry or selects design → record outcome. States: `CANDIDATE → REVIEWABLE → ACCEPTED_REFERENCE | REJECTED | DEPRECATED`.

**Failures/recovery.** Blind reuse across context, deprecated pattern recommended, missing failure/test evidence or reference treated as requirement. Return to exact target gap and classify fit honestly.

**Dependencies/authority.** FTR-005/025 and docs/05 Reference. Pattern authority is only its accepted reference fact class; use still requires design decision.

**Acceptance/negative.** Agent explains why fit/anti-fit; alternatives, failures and tests visible; provenance exact. No automatic architecture choice, code/template import or legacy authority transfer.

**Unknown/non-goals.** Taxonomy, curation cadence, deprecation policy and search presentation. No broad knowledge platform required initially.

## FTR-023 — Advisory CI, smoke checks and safety regression fixtures

```yaml
layer: Development Factory
recommendation: DEFER
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Provide repeatable technical feedback and safety regressions without treating CI as approval or lifecycle authority.

**Trigger/preconditions.** Runtime/toolchain/repository and stable contracts are selected; repeated checks justify automation; candidate identity is exact.

**Inputs → outputs.** Candidate, pinned environment/profile, required/optional checks and negative fixtures → C-009/C-010 compatible technical result with timings, `NOT_RUN`, artifacts and limitations.

**Flow/states.** Select profile → verify subject/environment → run structure/contract/negative/regression/smoke checks → aggregate fail-closed → publish technical result → stop. States reflect result only.

**Failures/recovery.** Required test missing, CI runs wrong subject, green exit hides failure, flaky result, secret leak, auto-merge or changed candidate. Report and create separate correction/infrastructure task.

**Dependencies/authority.** FTR-011/013 and regression catalog. CI has no human/product/Git authority.

**Acceptance/negative.** Known negatives fail; feedback bounded/fast enough; required checks explicit; exact subject retained. No automatic approval/merge, universal suite before toolchain decision or historical green reuse.

**Unknown/non-goals.** CI provider, profiles, duration/flakiness budgets and artifact retention. Deferred until implementation exists.

## FTR-024 — Release checklist and promotion package

```yaml
layer: Later Lifecycle
recommendation: DEFER
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Make release a distinct human-controlled promotion of an exact merged artifact, with compatibility, version, changelog, rollback and post-release checks.

**Trigger/preconditions.** Exact merged artifact exists; distribution/deployment/versioning policy and release target are selected; blockers and rollback boundary are known.

**Inputs → outputs.** Merged SHA/artifact, accepted changes, compatibility statement, validation/review, version/tag proposal, distribution target and exact release authorization → release package, one release action record and verified result.

**Flow/states.** Bind artifact → compile changes/compatibility → check blockers → prepare version/tag/rollback → request release auth → execute one action → post-check/report. States: `PACKAGE_DRAFT → REVIEWABLE → WAITING_AUTH → RELEASING → RELEASED | FAILED/ROLLBACK_DECISION`.

**Failures/recovery.** Stale artifact, missing blocker, version collision, partial publication, failed post-check or release inferred from merge. Stop, preserve remote result and present bounded rollback/correction options.

**Dependencies/authority.** FTR-011/014/015. Release separately authorized; no production mutation from merge/acceptance alone.

**Acceptance/negative.** Artifact/version/target exact; compatibility/remaining risk visible; rollback and post-check defined. No auto-tag/deploy/release, secret exposure or false completion after partial failure.

**Unknown/non-goals.** Distribution, deployment, versioning/changelog and rollback policies. Deferred until real release target exists.

## FTR-025 — Observability, audit log, incidents and continuous improvement

```yaml
layer: Product Runtime Support / Operations
recommendation: KEEP
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Preserve material outcomes/failures so maintainers can learn, diagnose recurrence and propose bounded preventive rules without automatic policy mutation.

**Trigger/preconditions.** A material run/result/denied action/failure/near miss occurs within an explicit retention/privacy boundary.

**Inputs → outputs.** Event, subject/actor/time, Evidence, impact, root-cause candidate, correction and recurrence data → minimal incident record, human-reviewed lesson candidate and regression proposal.

**Flow/states.** Record event → bind Evidence → analyze bounded cause candidate → describe correction/prevention/test → human review → accept/reject lesson → monitor recurrence. States: `RECORDED → ANALYZED → LESSON_PROPOSED → ACCEPTED | REJECTED | NEEDS_EVIDENCE`.

**Failures/recovery.** Missing Evidence shown as proven cause; rejected lesson changes policy; log failure hides original incident; excessive sensitive retention. Preserve unknown cause, protect primary state and repair logging separately.

**Dependencies/authority.** FTR-014/021 and docs/04 Lessons. Evidence/incident is not decision; lesson becomes normative only after explicit acceptance.

**Acceptance/negative.** Incident searchable/source-bound; cause confidence explicit; regression test/review prompt actionable; recurrence measurable. No surveillance-by-default, automatic policy/roadmap mutation or indefinite raw sensitive logs.

**Unknown/non-goals.** Event taxonomy, retention/privacy, observability backend and alerting. Core can begin with minimal records, not a telemetry platform.

## FTR-026 — Extensions, plugins and capability modules

```yaml
layer: Architecture Extension
recommendation: DEFER
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Add optional capabilities/domains without coupling, hidden permissions or override of core contracts.

**Trigger/preconditions.** Repeated extension need and stable extension point exist; module version, permissions, compatibility, isolation and removal are designed and human-selected.

**Inputs → outputs.** Core extension contract, module manifest/version, declared capabilities/permissions, compatibility range and install decision → isolated installed/updated/removed module state with Evidence.

**Flow/states.** Define extension point → specify contract/version → declare permissions → validate compatibility/isolation → explicit install → monitor → safe update/remove. States: `AVAILABLE → COMPATIBLE → WAITING_INSTALL_AUTH → ENABLED | DISABLED | INCOMPATIBLE | FAILED_ISOLATED`.

**Failures/recovery.** Unknown version, undeclared permission, module overrides core, failure propagates or removal loses core/user data. Block/isolate/disable and restore core without module.

**Dependencies/authority.** FTR-004/019/021. Optional modules never own core authority or self-install/update.

**Acceptance/negative.** Core works without module; compatibility deterministic; permissions explicit; failure isolated; removal safe. No marketplace/platform, hidden network/provider or premature general plugin API.

**Unknown/non-goals.** Actual extension points, packaging/versioning, signature/trust and discovery. Deferred until repeated need.

## FTR-027 — Domain profiles: Medical or Design

```yaml
layer: Regulated / Creative Domain Extensions
recommendation: DEFER
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
available_domain_profiles: [MEDICAL, DESIGN]
selected_domain_profile: null
```

**Shared purpose/boundary.** Support one separately selected specialist workflow through a replaceable domain profile while keeping core domain-neutral. `MEDICAL` and `DESIGN` are distinct decision subjects; they do not share users, authority, data classes, acceptance or risk defaults. This DRAFT selects neither.

### Medical domain profile (`FTR-027/MEDICAL`)

```yaml
profile_status: PROPOSAL
selected: false
selection_decision: DR-LIFE-004
specialist_authority_required: true
```

**Purpose/users.** Help a medical domain expert and authorized clinical/compliance reviewer define and review a bounded software workflow without giving AOS diagnostic, treatment, legal or regulatory authority.

**Trigger/preconditions.** A human names one exact medical job and jurisdiction/use boundary. Data classes, consent/provider boundary, prohibited clinical decisions, qualified specialist role and applicable policy are explicit before affected processing.

**Inputs → outputs.** Neutral core contracts, exact medical job, vocabulary, sensitive-data classes, constraints, provider boundary, specialist checkpoints and acceptance criteria → isolated Medical profile contract and bounded pilot review subject.

**Flow/states.** Bind job/jurisdiction/data boundary → identify decisions reserved to qualified humans → draft observable domain behavior and negatives → specialist review → bounded pilot → evidence-based review. Observable states: `PROFILE_UNBOUND → BOUNDARY_READY → SPECIALIST_REVIEW → PILOT_READY → REVIEWED | BLOCKED_AFFECTED_ACTION`.

**Failures/recovery.** Missing specialist, consent/policy or allowed provider is `BLOCKED_AFFECTED_ACTION`; no data transfer or inferred approval occurs. Partial or stale pilot state is exposed and the profile can be disabled without changing core truth.

**Acceptance/negative.** Exact specialist decision and scope are visible; least necessary data is used; prohibited advice/diagnosis/treatment actions are testable; core works with the profile absent. Agent-generated clinical judgment, unapproved sensitive-data transfer, compliance inference and use outside the selected jurisdiction/job fail closed.

**Unknown/non-goals.** Exact medical job, jurisdiction, providers, consent/retention policy and professional validation method. No diagnosis, treatment recommendation, emergency routing or regulatory certification is claimed.

### Design domain profile (`FTR-027/DESIGN`)

```yaml
profile_status: PROPOSAL
selected: false
selection_decision: DR-LIFE-004
specialist_authority_required: true
```

**Purpose/users.** Help a product/design professional define and review a bounded design workflow while preserving creative ownership, product decisions, accessibility requirements, source provenance and asset rights.

**Trigger/preconditions.** A human names one exact design job and target artifact. Product context, brand/design-system owners, asset/source rights, accessibility boundary, collaboration roles and acceptance reviewers are explicit.

**Inputs → outputs.** Neutral core contracts, design brief, target users/artifact, product/design constraints, source assets and rights, design-system rules, accessibility criteria and reviewer checkpoints → isolated Design profile contract and bounded design review subject.

**Flow/states.** Bind brief/artifact/owners → separate product facts from creative proposals → preserve source/rights provenance → compare reviewable alternatives → accessibility/specialist review → exact human selection or defer. Observable states: `PROFILE_UNBOUND → BRIEF_BOUND → OPTIONS_REVIEWABLE → SPECIALIST_REVIEW → SELECTED | DEFERRED | BLOCKED_AFFECTED_ACTION`.

**Failures/recovery.** Missing rights, owner conflict or stale design source blocks the affected output; rejected alternatives remain proposals and core state is unchanged. Rebind the exact source/rights/owner boundary before affected review continues.

**Acceptance/negative.** Reviewer can trace each material design choice to the brief and source; accessibility and rights criteria are visible; unselected alternatives remain unselected; core works with the profile absent. The profile cannot invent brand authority, overwrite product facts, treat aesthetic preference as acceptance or reuse unlicensed assets.

**Unknown/non-goals.** Exact design job, artifact/tool surface, design-system owner, asset license policy and evaluation method. No mandatory visual tool, autonomous brand decision or bundled Medical behavior.

**Dependencies/authority.** FTR-019/026 and the selected profile policy. `DR-FTR-027` owns the feature disposition route; `DR-LIFE-004` owns profile selection. Human/domain specialist owns domain decisions; core remains neutral; `selected_domain_profile` stays `null` until an exact human decision.

## FTR-028 — Workbench or SaaS UX wrapper

```yaml
layer: UX Wrapper
recommendation: DEFER
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Offer visual onboarding, status, review and collaboration after core journeys prove that chat/CLI/local surfaces create material friction.

**Trigger/preconditions.** Measured UX/collaboration need, source-owned runtime state, identity/access model and chosen hosting/privacy boundary exist.

**Inputs → outputs.** Source-linked contracts/state/Evidence/chat/decision options and authenticated actors → accessible visual views and exact decision records synchronized without duplicate truth.

**Flow/states.** Load source state → render Status/Next/Details → edit through contracts → show risk/Evidence/unknowns → capture exact decision → refresh or mark stale. UI state never exceeds source state.

**Failures/recovery.** Offline/stale UI approves, generated decision, unauthorized access, duplicate database truth or UI hides NOT_RUN. Disable decision action, rebind owners and recover from source records.

**Dependencies/authority.** FTR-008/012/016 and identity/access policy. UI display/click is not authority without exact human record.

**Acceptance/negative.** Journey measurably clearer/faster; displayed state matches sources; accessibility and access control tested. No SaaS prerequisite, hidden lifecycle mutation or independent product truth.

**Unknown/non-goals.** UI form, collaboration model, auth, hosting, offline behavior and business model. Deferred until core proof.

## FTR-029 — Templates, prompt packs, cross-repo context, localization and policy overlays

```yaml
layer: Packaging / Extension Support
recommendation: DEFER
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Port common AOS semantics across tools/repos/languages without drift, hidden authority or overwrite of local/project-owned state.

**Trigger/preconditions.** Accepted common owner sources and target adapter/locale requirements exist; export/install boundaries and local ownership are explicit.

**Inputs → outputs.** Exact common sources, target format/locale/policy and ownership/conflict rules → versioned package with thin adapters, provenance, semantic checks and update preview.

**Flow/states.** Build from owners → generate adapters/translations → validate links/semantic invariants → preview target conflicts → explicit apply → drift-check/rebuild. States: `SOURCE_BOUND → GENERATED → VERIFIED → READY_TO_APPLY → APPLIED | CONFLICT`.

**Failures/recovery.** Missing owner, local modification overwrite, locale changes meaning, adapter adds permission or cross-repo source goes stale. Preserve local state, surface conflict and rebuild from exact owners.

**Dependencies/authority.** FTR-004/016/021. Package/translation/adapter is derived and cannot add authority or permissions.

**Acceptance/negative.** Portable relative links; common semantics consistent; ownership/conflicts visible; RU/EN meaning aligned. No automatic cross-repo mutation, prompt pack as policy owner or hidden sync.

**Unknown/non-goals.** Target formats/tools/locales, policy overlay precedence and distribution. Deferred until concrete consumers exist.

## FTR-030 — Strict contract tools and schema/runtime drift tests

```yaml
layer: Development Factory Internal
recommendation: DEFER
human_disposition: UNDECIDED
behavior_status: SYNTHESIZED_DRAFT
```

**Purpose/users.** Remove permissive parser/registry drift and AI-code debt after contracts stabilize, using small strict utilities and migration Evidence.

**Trigger/preconditions.** Multiple runtime representations/callers exist; accepted schema/contract owner is stable; actual parser/drift defect or maintenance need is measured.

**Inputs → outputs.** Owner contract/schema, caller inventory, invalid/legacy fixtures and migration boundary → strict adapter/loader contract, bounded migrated callers, negative tests, drift report and sunset Evidence.

**Flow/states.** Inventory representations → introduce strict adapter → migrate bounded callers → add invalid-state tests → compare docs/schema/runtime → sunset legacy only after Evidence. States: `LEGACY_ACTIVE → ADAPTER_READY → MIGRATING → STRICT_PRIMARY → LEGACY_REMOVED`; rollback until proven.

**Failures/recovery.** Bypass path remains, unexpected field accepted, docs/code drift hidden, old parser removed early or internal tool mistaken as product value. Restore bounded compatibility path and correct in a separate task.

**Dependencies/authority.** FTR-011/021 and canonical workflow. Internal tools cannot mutate contracts/canonical docs automatically.

**Acceptance/negative.** Runtime/tests use same strict owner; invalid states rejected; all callers accounted; old parser removed only after migration Evidence. No broad rewrite, premature tooling platform or implementation before stable contracts.

**Unknown/non-goals.** Runtime language/schema/loader/test infrastructure and stewardship metadata. Deferred until implementation choices and real drift exist.

## 9. Cross-feature dependency summary

| Foundation | Direct dependents | Boundary |
|---|---|---|
| FTR-001 | FTR-003 | accepted first slice stops at confirmed Intent Record |
| FTR-003 | FTR-005/006/007 and later feature planning | Product Spec/Passport ownership option A applies |
| FTR-006 + FTR-009 + FTR-019 | FTR-010, FTR-004, protected delivery | description/preview/classification do not grant permission |
| FTR-010 | FTR-013/014 | exact candidate and recovery follow mutation |
| FTR-011 + FTR-013 | FTR-012/023 | technical result remains separate from decision |
| FTR-012 | FTR-015/021/024 | exact acceptance/authenticity required before dependent route |
| FTR-014 + FTR-016 | all resumable flows | handoff is derived and refreshed |
| FTR-019 | protected/extension/provider features | classifier is not approval |
| FTR-021 + FTR-025 | FTR-020/022/030 | evidence/lessons precede stronger enforcement/tooling |
| FTR-026 | FTR-027/029 | extensions are optional and isolated |

Dependency references never change human disposition or roadmap priority.

## 10. Feature review decisions required

The DRAFT is complete enough for behavioral review, but item-level decisions remain:

- accept/change/reject the proposed behavior for each non-X1 feature;
- select `REQUIRED/OPTIONAL/DEFERRED/REFERENCE_ONLY/REJECTED` dispositions when appropriate;
- decide roadmap admission after the already accepted FTR-001 slice;
- resolve feature-specific interface, persistence, provider/data, install, compatibility and release questions only when their dependent phase approaches;
- commission targeted reference research only for exact remaining gaps.

The consolidated decision sequence is in [07_DECISION_REGISTER.md](07_DECISION_REGISTER.md).

## 11. Feature package completeness checklist

- Exactly 30 unique feature IDs are present.
- Recommendation and human disposition match `docs/06_Features.md`.
- FTR-001/FTR-003 accepted X1 behavior is not weakened or widened.
- Supporting-control features are not admitted as independent X1 product scope.
- Each section covers purpose/users, trigger, I/O, flow/state, failure/recovery, dependencies/authority, acceptance/negative and unknown/non-goal.
- Proposed states are feature-visible WHAT, not mandatory implementation machinery.
- No feature self-authorizes, mutates canonical owners or implies Git delivery.
- Deferred capabilities remain optional and justified by measured need.
