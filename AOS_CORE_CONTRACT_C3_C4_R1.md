---
document_type: AOS_CORE_CONTRACT_SLICE
contract_family: AOS_CORE_CONTRACT
contract_slice: C3_C4
revision: DRAFT-R1
status: HUMAN_REVIEW_REQUIRED
claim_class: DRAFT_CONTRACT_CANDIDATE
authority: NONE_UNTIL_HUMAN_ACCEPTANCE
authority_scope:
  - C3_PROJECT_MEMORY_AND_IMMUTABLE_RECORDS
  - C4_DOCTOR_SELF_TEST_STATUS_NEXT_DETAILS
task_id: DOC-007
technical_result: PASS
readiness: READY_FOR_FINAL_PACKAGE_REVIEW
human_acceptance: NOT_RUN
provisional_dependency_use: ALLOWED_BY_CURRENT_HUMAN_MANDATE
base_contract: AOS_CORE_CONTRACT_R1.md
base_contract_sha256: 24f1af001bc0249d9c8e40a9608c2c5b67ea047bf2307cbda251f184b223d5db
project_memory_schema: AOS_CORE_CONTRACT_C012_V2_R1.md
project_memory_schema_version: 2.0.0
nearest_unimplemented_task: Task-001-Scaffolding.md
new_implementation_task_created: false
implementation_repository_creation: NOT_RUN
execution_authorization: NOT_RUN
git_authorization: NONE
created: 2026-08-05
---

# AOS-3 — Core Contract C3–C4 R1

## 1. Назначение и нормативная граница

Этот candidate дополняет принятый `AOS_CORE_CONTRACT_R1.md` только в непересекающихся fact classes:

- `C3` владеет exact persistence, freshness, resume и conflict semantics для `C-012 Project Memory`;
- `C4` владеет read-only command/view contract `run → doctor → status → next → details`.

Принятый `C1–C2` subject не изменяется. Его schemas, closed enums, strict loader, authority и permission semantics являются обязательной base dependency. Единственное versioned исключение — отдельно предъявленная `C-012 Project Memory schema v2.0.0`, которая меняет только requiredness active-task fields по explicit human correction. При конфликте этот candidate не может ослабить остальные `C1–C2`, `docs/00_Core.md`, принятые `H1` decisions или explicit human authority.

```text
C1–C2 accepted exact subject
→ C-012 v2 provisional schema correction
→ C3–C4 provisional candidate
→ DOC-008 may consume it provisionally
→ one final package review
```

`technical_result: PASS` здесь означает только focused documentation self-check. Он не означает `HUMAN_ACCEPTED`, implementation readiness, repository creation или Execution Authorization.

## 2. Consumed decisions и owner boundaries

| Fact | Owner/binding |
|---|---|
| Current lifecycle persistence path | `AOS_IMPLEMENTATION_DECISIONS_R1.md`, H1-006: `.aos/state/project-memory.json` |
| Immutable record root | `AOS_IMPLEMENTATION_DECISIONS_R1.md`, H1-006: `.aos/records/` |
| First-cycle interface | H1-004/H1-011: local CLI + versioned JSON; read-only `doctor/status/next/details` |
| First-cycle Product Runtime output | H1-003: durable Project Memory reference, plain-language status, one next action |
| Record schemas/status/authority | accepted `AOS_CORE_CONTRACT_R1.md` (`C1–C2`), кроме current provisional `C-012 v2.0.0` exact correction |
| Project Memory schema | `AOS_CORE_CONTRACT_C012_V2_R1.md`: `active_task_status` и conditional stage/task ref |
| Current state | exactly one valid file at `.aos/state/project-memory.json` |
| Immutable history | content-addressed records under `.aos/records/`; never a second current-state owner |
| Registry/index/dashboard | derived navigation only; never authority |

Feature dispositions are consumed only from accepted `AOS_IMPLEMENTATION_DECISIONS_R1.md`. Conflicting older `docs/06_Features.md` dispositions do not override the later exact H1 decision.

## 3. C3 — Project Memory and immutable records

### 3.1. Exact paths and ownership

```yaml
project_memory:
  current_owner_path: .aos/state/project-memory.json
  lock_path: .aos/state/project-memory.lock
  temporary_path_pattern: .aos/state/.project-memory.json.tmp.<run_id>
  backup_path: NONE
  writer_model: SINGLE_WRITER_FIRST_CYCLE
immutable_records:
  root: .aos/records
  path_pattern: .aos/records/<record_kind>/<record_id>.<sha256>.json
  mutation_policy: APPEND_ONLY_CREATE_EXCLUSIVE
derived_indexes:
  authority: NONE
  rebuildable: true
```

Rules:

1. Only `.aos/state/project-memory.json` owns current lifecycle state.
2. Lock and temporary files are transport mechanisms, not state owners and not valid resume inputs.
3. Immutable record filenames bind record kind, ID and canonical payload digest. Existing bytes are never overwritten.
4. A current memory write may reference only records that strict-load successfully and whose digest matches the filename/ref.
5. Missing `.aos/` is a valid `NOT_INITIALIZED` condition for read-only commands; they must not create it.
6. No registry, handoff, chat transcript, CLI cache or dashboard may repair current state implicitly.

### 3.2. Exact C3 Project Memory payload profile

Accepted `C-012 v1` remains immutable. This provisional C3 consumer binds `aos.core.project_memory@2.0.0` from `AOS_CORE_CONTRACT_C012_V2_R1.md`. A `mode: CURRENT_STATE` record at the owner path MUST satisfy:

```text
C3CurrentMemoryProfile = {
  memory_id: Identifier!,
  mode: CURRENT_STATE!,
  repository_identity: RepositoryIdentity!,
  active_task_status: enum<ActiveTaskStatus>!,
  current_stage: enum<TaskStage>?,
  active_task_ref: RecordRef?,
  baseline_ref: SubjectRef!,
  candidate_refs: list<SubjectRef>!,
  accepted_decision_refs: list<RecordRef>!,
  findings: list<NonEmptyText>!,
  blockers: list<NonEmptyText>!,
  check_refs: list<RecordRef>!,
  authorization_status: enum<AuthorizationStatus>!,
  authorization_ref: RecordRef?,
  one_next_action: NonEmptyText!,
  freshness_checked_at: UtcTimestamp!
}
```

Additional invariants:

- `active_task_status: NONE` requires both `current_stage` and `active_task_ref` absent; it also requires `authorization_status: NONE` and absent `authorization_ref`.
- `active_task_status: ACTIVE` requires both `current_stage` and `active_task_ref`; the ref must resolve to a `TASK_BRIEF` record whose subject equals the exact active task identity.
- one conditional field without the other is always `CONTRACT_VIOLATION`.
- `baseline_ref.repository` must equal `repository_identity.repository` when present.
- `candidate_refs` are sorted by `(subject_kind, subject_id, revision, sha256)` and contain no duplicate subject identity.
- every `accepted_decision_ref` resolves to a valid human-authored `HUMAN_DECISION` record with `decision: ACCEPT` for its exact subject;
- `authorization_status: NONE` requires absent `authorization_ref`; all other states require the exact authorization ref;
- only `ACTIVE` may permit a protected action, and C2 must recheck it immediately before action;
- `one_next_action` is one bounded human-readable action or `NONE`; it cannot contain multiple alternatives or an implicit mutation;
- `freshness_checked_at` records the observation time, not a timeless freshness claim;
- findings/blockers are plain summaries linked to immutable records through `check_refs` or candidate/decision refs; they are not authority by themselves.

### 3.3. Atomic write protocol

Project Memory mutation is a protected `AUTHORITY_STATE_MUTATION` and requires an exact active authorization unless it is part of a separately authorized Product Runtime write whose Task Brief explicitly includes the owner path.

```text
strict-load current bytes if present
→ acquire exclusive lock without waiting indefinitely
→ re-observe repository identity and referenced subjects
→ render complete canonical replacement in memory
→ write unique temp file in same directory with create-exclusive
→ fsync temp file
→ strict-load temp file and verify canonical digest/references
→ atomic rename over owner path
→ fsync parent directory
→ release lock
→ emit immutable Stage/Evidence records
```

Failure before rename leaves the previous owner bytes authoritative. Failure after rename but before directory `fsync` returns `UNKNOWN`/recovery required; it never reports `PASS` until current bytes and referenced records are revalidated.

Lock acquisition rules:

- a live lock held by another writer returns `BLOCKED` and performs no write;
- an orphaned lock is not deleted automatically; recovery must prove owner process absence and revalidate memory identity;
- lock timeout and stale-lock evidence are recorded without exposing sensitive process data.

### 3.4. Immutable record protocol

1. Produce canonical bytes using C1.
2. Compute digest before final LF according to C1.
3. Create the exact content-addressed path with exclusive create.
4. If the path exists, compare bytes: identical is idempotent `PASS`; different is `CONTRACT_VIOLATION`.
5. `fsync` file and parent directory before a Project Memory reference can be committed.
6. A failed current-memory update leaves the new immutable record unreferenced but valid; it may be garbage-collected only by a separately authorized maintenance task, never during resume.

### 3.5. Freshness model

Freshness is a computed read-only result over these bindings:

| Binding | Freshness oracle | Stale result |
|---|---|---|
| Repository | root/branch/HEAD/worktree fingerprint equals memory | `STALE_REPOSITORY_IDENTITY` |
| Active task | when status `ACTIVE`, both conditional fields exist and task record digest/schema/subject match; when `NONE`, both are absent | `STALE_TASK_REF` or `CONTRACT_VIOLATION` |
| Baseline/candidates | every exact subject exists and digest matches | `STALE_SUBJECT_REF` |
| Decisions | authentic record exists and exact subject still matches | `STALE_DECISION_REF` |
| Authorization | lifecycle/time/subject/repository/preview bindings valid | `STALE_AUTHORIZATION` |
| Checks | required check records resolve; no required stale/`NOT_RUN` hidden | `STALE_CHECK_REF` |

Freshness status is closed:

```text
FRESH | STALE | CORRUPT | NOT_INITIALIZED | BLOCKED_UNKNOWN
```

It is a C3-local derived status, not a new global technical result. `FRESH` says only that bindings match at observation time; it does not mean acceptance or permission.

### 3.6. Resume algorithm without chat history

```text
1. Locate repository root read-only.
2. Read accepted bootstrap/owner routing.
3. Observe root/branch/HEAD/worktree without mutation.
4. If Project Memory missing, return NOT_INITIALIZED and one initialization decision/action.
5. Strict-load Project Memory using C1; reject temp/lock/index as substitutes.
6. Resolve every required RecordRef/SubjectRef and recompute freshness.
7. Reclassify authorization with C2; never trust stored ACTIVE alone.
8. Render status, blockers, permission state and exactly one recorded next action.
9. Do not execute that action; stop.
```

Chat history may help a human understand context but cannot repair missing authoritative refs or fill current state.

### 3.7. Conflict resolution

| Conflict | Resolution |
|---|---|
| Project Memory versus current repository observation | observation owns mutable repository facts; mark memory `STALE`; no automatic write |
| Project Memory versus authentic later human decision | human decision owns decision fact; mark memory stale; propose authorized update |
| Project Memory versus derived index/dashboard | Project Memory wins for current state; rebuild index |
| Two candidate current-memory files | canonical owner path only; other file is non-authoritative and a finding |
| Current path corrupt but handoff snapshot valid | snapshot is Evidence only; human/authorized recovery must reconstruct and validate a new current record |
| Stored `ACTIVE` authorization versus expired/drifted binding | C2 result wins; affected action denied and memory update proposed |

Conflict resolution never selects a new product/task decision automatically.

## 4. C4 — Doctor, Self-Test and read-only UX

### 4.1. Product command surface

The canonical product-facing executable is `aos`. The accepted development bridge remains `./aos-dev run -- <product args>`; it may not change product semantics.

```text
aos run
aos doctor [--format human|json]
aos self-test [--format human|json]
aos status [--format human|json]
aos next [--format human|json]
aos details [--format human|json] [--subject <id>]
```

`aos run` is a read-only orientation route, not a general executor. It performs `doctor → status → next` and returns locators for `details`; it never executes `one_next_action`.

### 4.2. Zero-write contract

All C4 commands:

- create no `.aos/`, cache, log, telemetry, lock or temp file in the repository;
- do not update `freshness_checked_at` or any lifecycle field;
- do not fetch network resources or call model/provider APIs;
- do not repair, migrate, rebuild or delete data;
- do not mutate Git/index/worktree;
- may use OS memory and write the requested terminal output only;
- may read an explicit caller-owned output destination only if a future separately accepted interface adds one; no such file output exists in R1.

The implementation test oracle is a before/after byte inventory plus Git status/worktree fingerprint equality.

### 4.3. Common output schema

Human and JSON views are two serializations of the same result object:

```text
C4ViewResult = {
  schema_version: "aos.view-result.v1"!,
  command: enum<C4Command>!,
  technical_result: enum<TechnicalResultWithoutHumanReviewRequired>!,
  freshness: enum<C3Freshness>!,
  repository: ShortText?,
  active_task_status: enum<ActiveTaskStatus>?,
  active_task: RecordRef?,
  current_stage: enum<TaskStage>?,
  permission: enum<PermissionClass>!,
  authorization_status: enum<AuthorizationStatus>?,
  required_checks: list<CheckResult>!,
  optional_checks: list<CheckResult>!,
  blockers: list<NonEmptyText>!,
  limitations: list<NonEmptyText>!,
  one_next_action: NonEmptyText!,
  detail_refs: list<RecordRef>!
}
```

Closed `C4Command` members:

```text
RUN | DOCTOR | SELF_TEST | STATUS | NEXT | DETAILS
```

`TechnicalResultWithoutHumanReviewRequired` is the C1 technical enum excluding `HUMAN_REVIEW_REQUIRED`, because a diagnostic command cannot create review readiness.

Common invariants:

- when Project Memory strict-loads (`FRESH` or schema-valid `STALE`), `active_task_status` and `authorization_status` are required; `NONE` requires `active_task` and `current_stage` absent; `ACTIVE` requires both present;
- when freshness is `NOT_INITIALIZED`, `CORRUPT` or `BLOCKED_UNKNOWN`, all lifecycle projections (`active_task_status`, `active_task`, `current_stage`, `authorization_status`) are absent; they are never synthesized from chat, indexes or directory heuristics;
- `PASS` requires every required check `PASS`, freshness `FRESH`, no blockers, and no required `NOT_RUN`;
- `NOT_INITIALIZED` freshness maps to technical `BLOCKED`, not `PASS`;
- `UNKNOWN`, `NOT_RUN` and `BLOCKED` remain distinct in JSON and human output;
- one_next_action is always present, including `NONE` after a valid terminal state;
- human rendering begins with a plain-language conclusion, then why, then one next action, then optional detail locators;
- JSON output is deterministic and contains no ANSI escapes, paths outside repository-relative locators or raw secrets.

#### `NOT_INITIALIZED` output profile

If `.aos/` or the owner path does not exist:

```text
freshness: NOT_INITIALIZED
technical_result: BLOCKED
permission: NOT_APPLICABLE
active_task_status: absent
active_task: absent
current_stage: absent
authorization_status: absent
blockers: [PROJECT_MEMORY_NOT_INITIALIZED]
one_next_action: one separately authorized initialization action
exit_code: 5
```

This is an observation about unavailable lifecycle state, not `active_task_status: NONE`. `NONE` is valid only inside a strict-loaded `C-012 v2` Project Memory record.

### 4.4. Source-owner read matrix

| Command | Required owners read | Behavior when unavailable |
|---|---|---|
| `run` | same as `doctor`, `status`, `next` | worst required result; no later step hidden |
| `doctor` | bootstrap markers, C1 schemas, Project Memory if present, exact refs, repository observation | missing owner → named `BLOCKED`/`CONTRACT_VIOLATION`; no repair |
| `self-test` | packaged schemas/fixtures and isolated OS-temp test subject | unavailable fixture/tool → required `NOT_RUN`; source repository unchanged |
| `status` | Project Memory + fresh repository observation | missing/corrupt memory → `BLOCKED`/`CONTRACT_VIOLATION` with one recovery action |
| `next` | valid fresh Project Memory `one_next_action` + C2 permission classification | stale/unauthorized action is displayed as blocked/proposed, never executed |
| `details` | exact refs named by current result/memory | missing ref reported individually; unrelated refs may still render |

### 4.5. Exact command behavior

#### `aos doctor`

Required checks:

1. repository root/markers;
2. installed product/schema version compatibility;
3. Project Memory strict-load or explicit `NOT_INITIALIZED`;
4. referenced record/digest integrity;
5. repository freshness;
6. authorization freshness without using it;
7. read-only command purity capability;
8. required owner/index distinction.

Doctor is diagnosis, not comprehensive implementation validation. It may report optional checks as `NOT_RUN` without hiding them.

#### `aos self-test`

Runs packaged deterministic contract fixtures in an isolated OS temporary directory. It must cover strict-loader negatives, false-PASS aggregation, zero-write commands, stale memory and permission denial. It does not exercise network, Git mutation, provider calls or product writes in R1.

#### `aos status`

Returns explicit active-task status, conditional stage/task, candidate, freshness, blockers, permission state and checks. It never synthesizes a Task Brief or missing lifecycle state from chat, registry or filesystem heuristics.

#### `aos next`

Returns exactly the recorded `one_next_action`, plus its current C2 permission. If the action is stale, unbound or protected without authorization, the human output says it is not executable and names one resolution step. It does not choose another task.

#### `aos details`

Without `--subject`, expands refs in the current status. With `--subject`, it reads only an exact referenced ID. Arbitrary filesystem paths, globbing and unreferenced records are rejected.

### 4.6. Stable exit codes

| Exit | Meaning |
|---:|---|
| `0` | `PASS` only, or successful static `--help` |
| `2` | invalid CLI usage |
| `3` | contract/schema/input violation |
| `4` | incompatible tool/runtime environment |
| `5` | blocked identity/scope/permission/freshness precondition |
| `6` | technical check failure |
| `7` | partial/corrupt state requiring recovery |
| `8` | unexpected internal error |

Exit `0` is forbidden for required `FAIL`, `BLOCKED`, `UNKNOWN` or `NOT_RUN`. Human and JSON modes return the same exit code and semantic result.

## 5. Acceptance matrix

| ID | Contract | Case | Expected observable result |
|---|---|---|---|
| `C3-ACC-001` | C3 | clean memory write | atomic owner replacement; refs resolve; old or new complete bytes only |
| `C3-ACC-002` | C3 | immutable record duplicate | identical bytes idempotent; different bytes same path rejected |
| `C3-ACC-003` | C3 | clean resume | no chat needed; exact current state and one next action rendered |
| `C3-ACC-004` | C3 | missing state | `NOT_INITIALIZED`/`BLOCKED`; zero-write initialization guidance |
| `C3-ACC-005` | C3 | stale repository | exact stale binding named; safe read-only analysis remains available |
| `C3-ACC-006` | C3 | expired authorization | permission denied; authorization not reused or auto-renewed |
| `C3-ACC-007` | C3 | changed frozen candidate | stale subject detected; dependent action blocked |
| `C3-ACC-008` | C3 | derived index conflict | owner state retained; index marked rebuildable/non-authoritative |
| `C3-ACC-009` | C3 | first-cycle memory before Task Brief | `active_task_status: NONE`; stage/task/auth refs absent; resume succeeds without fabricated task |
| `C4-ACC-001` | C4 | doctor healthy | all required checks PASS; exit `0`; zero repository writes |
| `C4-ACC-002` | C4 | status healthy | exact memory facts and freshness explanation, no synthesis |
| `C4-ACC-003` | C4 | next protected | recorded action shown with `HUMAN_AUTHORIZATION_REQUIRED`; not executed |
| `C4-ACC-004` | C4 | details partial missing ref | missing ref visible; other refs rendered; worst required result honest |
| `C4-ACC-005` | C4 | self-test negatives | invalid fixtures fail as expected; aggregate PASS only when all required tests ran |
| `C4-ACC-006` | C4 | run orientation | doctor/status/next results combined; one next action; no mutation |
| `C4-ACC-007` | C4 | human/JSON parity | same semantic result and exit code |
| `C4-ACC-008` | C4 | no state directory | command does not create `.aos/` or cache |
| `C4-ACC-009` | C4 | healthy state without active task | explicit `NONE`; conditional fields absent; one next action rendered; no false blocker |
| `C4-ACC-010` | C4 | Project Memory not initialized | `BLOCKED`/exit `5`; lifecycle projection fields absent; zero writes; one initialization action |

## 6. Negative fixtures

| Fixture | Defect/attack | Expected result |
|---|---|---|
| `C3-NEG-001-two-current-owners` | valid-looking second memory file | ignore as owner; named conflict; no auto-merge |
| `C3-NEG-002-corrupt-current.json` | invalid JSON/unknown field | `CONTRACT_VIOLATION`; original bytes preserved |
| `C3-NEG-003-ref-digest-mismatch.json` | referenced bytes do not match digest | `STALE`/affected action blocked |
| `C3-NEG-004-index-newer-than-memory.json` | index claims later status | index has no authority; rebuild proposed |
| `C3-NEG-005-stored-active-expired.json` | memory says `ACTIVE`, expiry passed | C2 classifies expired; no permission |
| `C3-NEG-006-temp-as-owner.json` | current missing but temp exists | temp never promoted automatically |
| `C3-NEG-007-write-without-auth.json` | state update lacks exact authorization | zero write; denied-action evidence |
| `C3-NEG-008-candidate-after-freeze.json` | same revision, different digest | stale/tamper finding; validation/execute blocked |
| `C3-NEG-009-none-with-task-fields.json` | `active_task_status: NONE` plus stage/ref | `CONTRACT_VIOLATION`; no fabricated compatibility |
| `C3-NEG-010-active-missing-task-field.json` | `ACTIVE` with only one conditional field | `CONTRACT_VIOLATION`; previous owner preserved |
| `C4-NEG-001-read-command-writes` | status creates cache/log | acceptance `FAIL`; source purity violated |
| `C4-NEG-002-false-pass-not-run` | required check `NOT_RUN`, aggregate `PASS` | contract violation |
| `C4-NEG-003-unknown-as-pass` | unresolved ref reported healthy | contract violation/non-zero exit |
| `C4-NEG-004-next-autoexec` | next invokes proposed command | prohibited mutation; test fails |
| `C4-NEG-005-details-path-traversal` | `--subject ../../x` | invalid CLI/input; no filesystem read |
| `C4-NEG-006-chat-fallback` | memory missing, chat has status | chat ignored for authority; `BLOCKED` |
| `C4-NEG-007-json-secret` | record includes credential-shaped remote | output redacted; raw scan negative |
| `C4-NEG-008-exit-zero-failure` | command returns `FAIL` with exit `0` | contract violation |
| `C4-NEG-009-synthesized-none-without-memory` | missing owner rendered as `active_task_status: NONE` | contract violation; `NOT_INITIALIZED` profile required |
| `C4-NEG-010-not-initialized-with-lifecycle-fields` | unavailable/corrupt owner output includes task/stage/auth projection | contract violation; fields must be absent |

## 7. Recovery matrix

| ID | Failure | Preserved state | Bounded recovery | Required revalidation |
|---|---|---|---|---|
| `C3-REC-001` | write fails before rename | previous memory authoritative; temp retained/removed safely | discard exact temp after diagnosis | strict-load old memory + ref freshness |
| `C3-REC-002` | uncertain durability after rename | current bytes and journal/evidence | classify current file, refs and fsync state; do not claim PASS | full C3 freshness + Stage Record |
| `C3-REC-003` | orphaned lock | lock metadata, current bytes | separate recovery proves no active writer | strict-load/freshness before new write |
| `C3-REC-004` | corrupt memory | corrupt bytes preserved | reconstruct candidate only from immutable refs and authentic decisions; human/authorization gate | C1 strict load + cross-ref audit |
| `C3-REC-005` | stale HEAD/worktree | stale memory and fresh observation | proposed state update; no automatic rewrite | fresh preflight and ref binding |
| `C3-REC-006` | expired authorization | immutable auth/decision records | request new preview and human authorization | C2 creation gates |
| `C3-REC-007` | frozen candidate changed | both observed identities | freeze new revision; invalidate old validation/auth | digest, scope and validation rerun |
| `C3-REC-008` | future runtime observes v1 memory | source v1 bytes/digest | explicit v1→v2 migration; no silent relabel | both versions strict-load + migration Evidence |
| `C4-REC-001` | owner unavailable | no writes | return one owner-restoration step | rerun exact command |
| `C4-REC-002` | required check unavailable | explicit `NOT_RUN` | restore dependency/fixture outside read command | required check rerun |
| `C4-REC-003` | command internal error | source unchanged; safe diagnostic | bounded defect task, no retry loop | zero-write and negative fixture suite |
| `C4-REC-004` | partial/corrupt state detected | evidence locators only | route to C3 recovery; C4 does not repair | post-recovery doctor/status |
| `C4-REC-005` | owner not initialized | repository observation only | separately authorized first Product Runtime initialization; C4 remains zero-write | rerun doctor/status and strict-load C-012 v2 |

## 8. Traceability

| Requirement family | Feature boundary | Architecture contracts | Lessons/regressions |
|---|---|---|---|
| Current state, resume, handoff | H1-required `FTR-016` boundary | `C-012`, C3 | `LES-023…025`, `027`, `028`, `030`; `STATE-001`, `BASELINE-001`, `FREEZE-001` |
| Status/Next/Details | H1-required `FTR-008` boundary | `C-009`, `C-012`, C4 | `LES-010`, `011`, `016`, `020`, `027`, `034`, `035`; `STATUS-001…003`, `CLI-001`, `READONLY-001` |
| Doctor/Self-Test | H1-required `FTR-011` boundary | `C-008…C-010`, C4 | `LES-005`, `010`, `013…016`, `020`, `031`; `SELFREF-001`, `DRIFT-001` |
| Evidence/review refs | supporting `FTR-012` only; not newly selected | `C-010…C-012` | `LES-008`, `024`; `STATUS-003`, `FREEZE-001` |
| Recovery | `FTR-014` remains `UNDECIDED`; only required C3 safety semantics are specified | `C-008`, `C-010`, `C-012` | `LES-023…025`, `038`; `PARTIAL-001`, `BASELINE-001` |

This traceability does not change item-level feature dispositions. Normative first-cycle scope is the accepted H1 boundary, not the broader dossier text.

## 9. Proposed next implementation outline — non-executable

After `Task-001-Scaffolding` is implemented and accepted, the smallest Product Runtime consumer may be:

```text
strict C-001 Intent Record
→ immutable save
→ atomic C3 Project Memory update
→ C4 status/next/details read path
→ doctor/self-test fixtures
```

This is not a Task Brief, selected next task, Risk Profile, authorization or backlog activation.

## 10. Candidate status

```yaml
DOC-007:
  technical_result: PASS
  readiness: READY_FOR_FINAL_PACKAGE_REVIEW
  human_acceptance: NOT_RUN
  dependency_status: PROVISIONAL_CANDIDATE
contract_scope:
  C3: DOCUMENTED_AS_CANDIDATE
  C4: DOCUMENTED_AS_CANDIDATE
base_C1_C2_subject:
  path: AOS_CORE_CONTRACT_R1.md
  sha256: 24f1af001bc0249d9c8e40a9608c2c5b67ea047bf2307cbda251f184b223d5db
  human_acceptance: ACCEPTED
project_memory_schema_correction:
  path: AOS_CORE_CONTRACT_C012_V2_R1.md
  schema_version: 2.0.0
  human_acceptance: NOT_RUN
  runtime_migration: NOT_RUN
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
next_required_action: CONTINUE_DOC-008_UNDER_CURRENT_AUTONOMOUS_MANDATE
stop: false
```
