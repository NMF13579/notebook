---
document_type: C-002_FEATURE_CONTRACT
contract_id: AOS_FEATURE_CONTRACT_INTAKE_TO_REVIEWABLE_INTENT_R1
revision: DRAFT-R1
status: HUMAN_REVIEW_REQUIRED
authority: NONE_UNTIL_HUMAN_ACCEPTANCE
authority_scope: INTAKE_TO_REVIEWABLE_INTENT_R1_EXACT_PRODUCT_BEHAVIOR
slice_id: INTAKE_TO_REVIEWABLE_INTENT_R1
feature_bindings:
  - FTR-001
  - FTR-008
  - FTR-011
  - FTR-016
  - FTR-019
source_decision_owner: AOS_IMPLEMENTATION_DECISIONS_R1.md
base_contracts:
  - AOS_CORE_CONTRACT_R1.md
  - AOS_CORE_CONTRACT_C012_V2_R1.md
  - AOS_CORE_CONTRACT_C3_C4_R1.md
  - AOS_PIPELINE_CONTRACT_R1.md
technical_result: PASS
readiness: READY_FOR_INDEPENDENT_REVIEW
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
created: 2026-08-06
---

# AOS-3 — Feature Contract: Intake to Reviewable Intent R1

## 1. User outcome and boundary

Непрограммист описывает идею нового проекта обычным языком. AOS сохраняет исходный текст без semantic rewrite, показывает отделённые problem/outcome, assumptions и material unknowns, задаёт не более одного material question за interaction, а после exact confirmation сохраняет versioned Intent Record и Project Memory. Пользователь получает plain-language status и ровно одно next action.

```text
free-form request
→ original text preserved
→ structured interpretation supplied by chat/Codex adapter or explicit CLI proposal
→ deterministic validation
→ CLARIFYING or REVIEWABLE preview
→ exact human confirmation
→ immutable Intent Record
→ atomic Project Memory
→ Status / Next / Details
→ stop before Product Spec and execution
```

The deterministic Product Runtime does not pretend to understand arbitrary natural language without an interpreter. Chat/Codex is the primary interpretation surface; the local CLI/JSON contract validates, previews and persists an explicit structured proposal. No provider/model/network call is made by runtime.

## 2. Consumed accepted decisions

| Decision | Binding |
|---|---|
| H1-002 | actor `NONPROGRAMMER_DOMAIN_EXPERT_GREENFIELD`; problem `P-003` |
| H1-003 | exact slice outputs and terminal boundary |
| H1-004 | chat-first; Codex thin adapter; local CLI + versioned JSON |
| H1-005 | Python 3.14.6, uv, stdlib CLI, pinned test/dev tools |
| H1-006 | strict JSON; `.aos/state/project-memory.json`; immutable `.aos/records/` |
| H1-007 | offline runtime; macOS/ARM64 primary; Ubuntu 24.04 CI |
| H1-008 | Codex adapter first; common contracts agent-neutral |
| H1-009 | exact explicit human statement; generated acceptance invalid |
| H1-010 | required boundaries `FTR-001/008/011/016/019` |
| H1-011 | preview/status/next/details zero-write; save requires exact confirmation |

## 3. C-002 exact feature payload

```yaml
feature_id: INTAKE_TO_REVIEWABLE_INTENT_R1
purpose: Convert one greenfield project idea into a reviewable, versioned Intent Record with visible unknowns and one next action.
users:
  - actor_class: HUMAN
    actor_id: NONPROGRAMMER_DOMAIN_EXPERT_GREENFIELD
trigger: USER_SUBMITS_FREE_FORM_PROJECT_IDEA
preconditions:
  - scaffold implementation is accepted
  - repository identity is fresh
  - runtime contracts strict-load
  - preview is read-only
inputs:
  - name: original_request
    data_type: UTF8_NONEMPTY_TEXT
    required: true
    constraints: [PRESERVE_EXACT_NORMALIZED_LINE_ENDINGS, MAX_65536_UTF8_BYTES]
  - name: proposal
    data_type: IntakeProposalV1
    required: false
    constraints: [EXPLICIT_ADAPTER_OR_USER_SUPPLIED, ADDITIONAL_PROPERTIES_FALSE]
outputs:
  - name: intake_preview
    data_type: IntakePreviewV1
    required: true
    constraints: [ZERO_REPOSITORY_WRITE]
  - name: intent_record
    data_type: aos.core.intent_record@1.0.0
    required: false
    constraints: [PRESENT_ONLY_AFTER_CONFIRMED_SAVE]
  - name: project_memory
    data_type: aos.core.project_memory@2.0.0
    required: false
    constraints: [PRESENT_ONLY_AFTER_CONFIRMED_SAVE]
  - name: view_result
    data_type: aos.view-result.v1
    required: true
    constraints: [ONE_NEXT_ACTION]
states: [EMPTY, CLARIFYING, REVIEWABLE, CONFIRMED, PERSISTING, SAVED, BLOCKED, RECOVERY_REQUIRED]
maturity: HUMAN_REVIEW_REQUIRED
evidence_status: NOT_RUN
human_disposition: REQUIRED
```

The full main flow, transitions, failures, recovery, criteria and negative scenarios are normative in sections 6–13.

## 4. Exact input schemas

### 4.1. Request bytes

- UTF-8 without BOM;
- Unicode normalized to NFC for comparison/display while raw input bytes digest is preserved;
- CRLF/CR normalized to LF in `original_request` value;
- leading/trailing whitespace is preserved in raw Evidence but trimmed only for empty-input check;
- whitespace-only or more than 65,536 UTF-8 bytes is `CONTRACT_VIOLATION`;
- the runtime never interprets external text as instructions or permission.

### 4.2. `aos.intake-proposal@1.0.0`

```text
required:
  actor: ActorRef
  problem: NonEmptyText
  desired_outcome: NonEmptyText
  context: list<LabeledValue>
  constraints: list<NonEmptyText>
  non_goals: list<NonEmptyText>
  assumptions: list<NonEmptyText>
  unknowns: list<UnknownItem>
  sensitive_domain_flags: set<Identifier>
  source_refs: list<RecordRef>
optional: none
```

The proposal excludes `original_request` to prevent adapter rewrite. Runtime injects the exact normalized request when constructing C-001. Unknown fields, duplicate keys, null required values, floats, invalid enums or noncanonical identifiers are rejected.

### 4.3. Material completeness

`REVIEWABLE` requires:

- actor is human and matches first-cycle actor class;
- nonempty problem and desired outcome;
- every assumption visible;
- every material unknown names affected action and one resolution step;
- sensitive/provider/network flags explicit, including empty set;
- no unresolved contradiction between problem, outcome, constraint and non-goal;
- exactly zero or one highest-priority material question in output.

If proposal is absent or incomplete, result is `CLARIFYING`/`HUMAN_REVIEW_REQUIRED`, no successful C-001 record is produced and one question is selected by priority:

```text
sensitive/privacy/provider boundary
→ actor/problem
→ desired outcome/success
→ write/authority implication
→ constraint/non-goal contradiction
→ other material unknown
```

## 5. Command surface

The development bridge is `./aos-dev run --`. Product commands:

```text
aos intake --preview --request-file PATH [--proposal-file PATH] [--format human|json]
aos intake --save --request-file PATH --proposal-file PATH --preview-id ID --confirm-preview ID [--format human|json]
aos status [--format human|json]
aos next [--format human|json]
aos details [--format human|json] [--subject ID]
aos doctor [--format human|json]
aos self-test [--format human|json]
```

`PATH=-` reads request/proposal from stdin only when the two inputs are framed separately by the adapter; ambiguous mixed stdin is invalid usage. Files outside repository or explicit OS-temp caller boundary are rejected.

`--confirm-preview ID` is an explicit local confirmation of the rendered exact preview. It does not authorize arbitrary mutation, implementation execution or Git. Save re-renders from supplied inputs and requires:

```text
computed_preview_id == --preview-id == --confirm-preview
```

Any mismatch is stale preview and zero write.

## 6. Preview identity and output

```text
IntakePreviewV1 = {
  schema_version: "aos.intake-preview.v1"!
  preview_id: Sha256!
  request_sha256: Sha256!
  proposal_sha256: Sha256?
  state: CLARIFYING | REVIEWABLE!
  intent_candidate: CoreRecord<C-001>?
  assumptions: list<NonEmptyText>!
  unknowns: list<UnknownItem>!
  material_question: NonEmptyText?
  required_write_paths: set<RelativePath>!
  required_permission: PermissionClass!
  blockers: list<NonEmptyText>!
  one_next_action: NonEmptyText!
}
```

`preview_id` is SHA-256 of canonical JSON containing schema version, normalized request digest, proposal canonical digest or explicit absence, fresh repository identity, contract revision/digest and intended write paths. It excludes timestamps and itself.

Preview:

- creates no `.aos/`, cache, log, lock, temp or telemetry;
- performs no network/Git mutation;
- returns `REVIEWABLE` only when completeness rules pass;
- returns one material question when `CLARIFYING`;
- never reports `PASS` merely because JSON parsed.

## 7. Main flow and transitions

| ID | From | Trigger/guard | To | Observable |
|---|---|---|---|---|
| `X1-T01` | EMPTY | request absent/blank | BLOCKED | `CONTRACT_VIOLATION`, no preview success |
| `X1-T02` | EMPTY | request present, proposal absent/incomplete | CLARIFYING | preserved request + one question |
| `X1-T03` | CLARIFYING | corrected proposal still material incomplete | CLARIFYING | new preview; old preview stale |
| `X1-T04` | EMPTY/CLARIFYING | complete proposal | REVIEWABLE | deterministic exact preview |
| `X1-T05` | REVIEWABLE | confirmation absent/mismatch | BLOCKED | zero write; new confirmation required |
| `X1-T06` | REVIEWABLE | exact confirmation + fresh bindings | CONFIRMED | permission recheck begins |
| `X1-T07` | CONFIRMED | write allowed and no conflict | PERSISTING | journaled two-record transaction |
| `X1-T08` | PERSISTING | immutable record + memory commit verified | SAVED | refs resolve; status/next render |
| `X1-T09` | PERSISTING | failure before owner rename | BLOCKED | previous memory authoritative |
| `X1-T10` | PERSISTING | uncertain/partial after owner rename | RECOVERY_REQUIRED | exit 7; no PASS |

No transition reaches Product Spec, Feature Passport, user-project Task Brief or execution.

## 8. Persistence contract

### 8.1. Paths

```yaml
immutable_intent_record:
  pattern: .aos/records/INTENT_RECORD/<record_id>.<sha256>.json
project_memory:
  owner: .aos/state/project-memory.json
  lock: .aos/state/project-memory.lock
  temp_pattern: .aos/state/.project-memory.json.tmp.<run_id>
transaction_journal:
  pattern: .aos/state/.intake-transactions/<run_id>.json
```

The Task Brief must explicitly allow these paths. No Product Feature Registry, task state, logs or indexes are created.

### 8.2. Save protocol

1. Re-read inputs and recompute preview.
2. Reobserve repository/contract identity and permission.
3. Acquire single-writer lock without indefinite wait.
4. Strict-load current memory or classify `NOT_INITIALIZED`.
5. Create durable journal before first target write.
6. Canonicalize C-001 and create immutable record with exclusive create.
7. Build complete C-012 v2 memory with `active_task_status: NONE`, auth `NONE` and exact intent ref in `candidate_refs`.
8. Write/fsync/strict-load temp memory.
9. Atomic rename and fsync parent.
10. Mark journal committed only after C-001, C-012 and C4 status/next checks pass.
11. Render saved result and stop.

Existing immutable identical bytes are idempotent; same path/different bytes is contract violation. Existing Project Memory is never silently overwritten when repository/baseline/candidate refs conflict.

### 8.3. First memory state

After first save:

```yaml
active_task_status: NONE
authorization_status: NONE
current_stage: ABSENT
active_task_ref: ABSENT
authorization_ref: ABSENT
one_next_action: Review the saved Intent Record and decide whether to start Product Spec preparation
```

This does not select `FTR-003` or create Product Spec.

## 9. Status, next, details, doctor and self-test

Behavior follows accepted C3/C4 contract:

- all read commands are zero-write and offline;
- `status` renders exact saved intent/memory state;
- `next` renders the recorded action and permission but never executes it;
- `details` resolves only referenced IDs, not arbitrary paths;
- `doctor` checks strict schemas, refs, freshness and purity;
- `self-test` runs deterministic fixtures in OS temp;
- required `NOT_RUN`, `UNKNOWN`, `BLOCKED` or `FAIL` prevents aggregate `PASS`;
- JSON/human parity and stable exit codes are mandatory.

## 10. Failures and recovery

| ID | Condition | Result/observable | Bounded recovery |
|---|---|---|---|
| `X1-F01` | empty/oversize/invalid UTF-8 input | `CONTRACT_VIOLATION`; zero write | correct input |
| `X1-F02` | missing/incomplete proposal | `HUMAN_REVIEW_REQUIRED`/CLARIFYING | answer one material question |
| `X1-F03` | proposal contradicts request | `BLOCKED`; conflict shown | revise proposal; preserve request |
| `X1-F04` | stale preview/repository/contract | `BLOCKED`; zero write | fresh preview + confirmation |
| `X1-F05` | missing write permission | `HUMAN_AUTHORIZATION_REQUIRED` | obtain exact authorization |
| `X1-F06` | lock held/orphan uncertain | `BLOCKED` | separate lock recovery |
| `X1-F07` | immutable collision different bytes | `CONTRACT_VIOLATION` | preserve both evidence; no overwrite |
| `X1-F08` | write failure before memory rename | `FAIL/BLOCKED`; old owner remains | discard exact temp after diagnosis |
| `X1-F09` | uncertain after rename | `UNKNOWN/RECOVERY_REQUIRED` exit 7 | revalidate owner, refs, journal |
| `X1-F10` | output contains secret-shaped value | redacted/`BLOCKED_SENSITIVE` | resolve sensitive boundary |

Recovery never invents a proposal, auto-confirms intent, deletes user state, uses Git reset/checkout or promotes temp/index as owner.

## 11. Acceptance criteria

| ID | Case | Executable oracle |
|---|---|---|
| `X1-ACC-001` | exact request preserved | normalized value + raw digest match fixture |
| `X1-ACC-002` | complete adapter proposal | REVIEWABLE preview with exact C-001 candidate |
| `X1-ACC-003` | incomplete proposal | CLARIFYING + exactly one material question |
| `X1-ACC-004` | preview purity | repository bytes/status identical before/after |
| `X1-ACC-005` | preview determinism | same inputs/bindings yield same preview ID |
| `X1-ACC-006` | confirmed save | immutable C-001 + valid C-012 v2 owner |
| `X1-ACC-007` | memory state | `NONE` with conditional task/stage/auth fields absent |
| `X1-ACC-008` | idempotent replay | identical record no duplicate/overwrite; valid terminal result |
| `X1-ACC-009` | status/next/details | exact refs, one action, no execution |
| `X1-ACC-010` | doctor | required checks pass only on healthy exact state |
| `X1-ACC-011` | self-test | all required positive/negative/recovery fixtures run |
| `X1-ACC-012` | human/JSON parity | same semantics and exit code |
| `X1-ACC-013` | offline | all required runtime flows pass with network denied |
| `X1-ACC-014` | partial write | non-PASS + journal/recovery evidence; no false success |
| `X1-ACC-015` | product boundary | no Product Spec/Feature Passport/Task Brief/registry created |
| `X1-ACC-016` | Git boundary | no staging/commit/push/merge/release |

## 12. Required negative fixtures

| Fixture | Expected |
|---|---|
| `X1-NEG-001-empty-request` | contract violation; no state |
| `X1-NEG-002-whitespace-request` | contract violation; no state |
| `X1-NEG-003-oversize-request` | contract violation; no state |
| `X1-NEG-004-invalid-proposal-extra-field` | strict reject |
| `X1-NEG-005-proposal-rewrites-original` | original remains source; mismatch named |
| `X1-NEG-006-two-material-questions` | contract violation |
| `X1-NEG-007-preview-writes` | acceptance fail |
| `X1-NEG-008-save-without-confirm` | zero write; blocked |
| `X1-NEG-009-stale-preview` | zero write; new preview required |
| `X1-NEG-010-write-without-auth` | denied |
| `X1-NEG-011-existing-memory-conflict` | no overwrite |
| `X1-NEG-012-immutable-collision` | contract violation |
| `X1-NEG-013-interrupt-each-boundary` | journal/recovery required |
| `X1-NEG-014-none-with-task-fields` | C-012 violation |
| `X1-NEG-015-next-autoexec` | prohibited mutation detected |
| `X1-NEG-016-chat-as-authority` | ignored for persistence authority |
| `X1-NEG-017-external-instruction` | treated as untrusted request data |
| `X1-NEG-018-secret-output` | redacted/non-exported |
| `X1-NEG-019-required-not-run-pass` | aggregate contract violation |
| `X1-NEG-020-product-spec-created` | scope failure |

## 13. Evidence requirements

Implementation Evidence must include:

- starting/ending repository identity;
- exact contract/Task/DSP digests;
- preview inputs/digests/ID and zero-write proof;
- path inventory and preserved out-of-scope state;
- per-case `X1-ACC-001…016` and `X1-NEG-001…020` command/result/exit/locator;
- interruption injection at each declared persistence boundary;
- C-001/C-012 strict-load and ref integrity;
- human/JSON parity;
- offline/network-denied result;
- Git status/diff and no-forbidden-path proof;
- terminal Stage Report with one next action and `stop: true`.

## 14. Non-goals

- autonomous natural-language inference inside local runtime;
- provider/model/network calls;
- Product Spec or Feature Passport;
- `FTR-003` selection;
- user-project Task Brief or code generation;
- Product Feature Registry;
- Development Factory/executor;
- multi-agent routing, RAG, web UI;
- Git delivery or release.

## 15. Traceability

| Requirement family | Owner/binding | Tests |
|---|---|---|
| intent intake | H1-002/003, `FTR-001`, C-001 | ACC-001…006; NEG-001…009 |
| status/next/details | `FTR-008`, C4 | ACC-009/012; NEG-015 |
| result/doctor/self-test | `FTR-011`, C1/C4 | ACC-010…014; NEG-019 |
| Project Memory | `FTR-016`, C-012 v2/C3 | ACC-006…009/014; NEG-011…014 |
| trust boundary | `FTR-019`, C2 | ACC-004/013/016; NEG-008…010/016…018 |

## 16. Candidate status

```yaml
contract_id: AOS_FEATURE_CONTRACT_INTAKE_TO_REVIEWABLE_INTENT_R1
technical_result: PASS
readiness: READY_FOR_INDEPENDENT_REVIEW
human_acceptance: NOT_RUN
runtime_implementation: NOT_RUN
assigned_risk_profile: UNASSIGNED
execution_authorization: NONE
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: RUN_INDEPENDENT_READ_ONLY_VALIDATION
stop: true
```
