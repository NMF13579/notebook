---
artifact_id: TASK-LOCAL-AUTONOMY-CONTRACT-R1
document_type: TASK_LOCAL_AUTONOMY_CONTRACT
revision: R1
status: DRAFT
fact_class: PROPOSAL
task_id: TASK-LOCAL-AUTONOMY
target_readiness: READY_FOR_HUMAN_REVIEW
authority_effect: NONE_UNTIL_EXACT_HUMAN_ACCEPTANCE_AND_SEPARATE_TASK_LOCAL_ACTIVATION
global_workflow_effect: TASK_LOCAL_EXCEPTION_PROPOSAL_ONLY
current_state_owner: planning/CURRENT.md
implementation_authorization: NONE
git_authorization: NONE
human_acceptance: NOT_RUN
independent_validation: NOT_RUN
correction_history:
  - cycle: 1
    source_candidate_sha256: 0cca00cd9cda2cc02cbae595038791f3d4dbbc8db2e7e31c152402cac4b236e1
    source_validation_result: FAIL
    finding_ids:
      - TLA-SEM-001
      - TLA-SEM-002
      - TLA-SEM-003
      - TLA-SEM-004
      - TLA-SEM-005
      - TLA-SEM-006
  - cycle: 2
    source_candidate_sha256: f919081a892be8aa7cb7dee2420c7621a0bffc38ae72578d35b2e557ac7071b1
    source_validation_result: FAIL
    finding_ids:
      - TLA2-SEM-001
      - TLA2-SEM-002
      - TLA2-SEM-003
      - TLA2-SEM-004
source_boundary:
  current_explicit_human_decision: OBSERVED_AT_SNAPSHOT
  requested_source_path: TASK_LOCAL_AUTONOMY_HIGH_LEVEL.md
  requested_source_path_observation: NOT_FOUND
  requested_source_search_boundary: REPOSITORY_AND_ACCESSIBLE_DOCUMENTS_TREE
authoritative_inputs:
  - path: docs/00_Core.md
    sha256: 96787a64585264e9f0d6beb1aab28bc717f80436003dfc6c093736541a95c34c
  - path: docs/03_Development.md
    sha256: 251730eb5cdab9776a97caf29a6791e1f3645fa6b8f01c6de93c5c4a2bbed9b1
  - path: planning/AOS_Documentation_Task_Sequence_R9.md
    sha256: be91cbffcd2c79a0a632b661157e5e2e7fb7a68d1056ba1c9684f2ea1b549ee7
  - path: planning/AOS_Authoritative_Owner_Map_R1.md
    sha256: 21d256eda56b528c3eb93aaf2120ee73ab5345d162906e2774a647e23b232909
  - path: planning/verification/POST_STOP_DOCUMENTATION_VALIDATION_CONTRACT_R1.md
    sha256: b35bf89e503c2cd86393c983ef26108858a5c1e697c09db5d497b8830ca122b9
---

# Task-local autonomy contract R1

## 1. Outcome and boundary

This DRAFT defines a thin task-local mandate and coordinator. One explicit
human command may authorize one exact task to progress through separately
bounded `PLAN`, `EXECUTE`, independent read-only `VALIDATE`, and at most three
technical correction/validation cycles before returning one candidate for
human review.

The coordinator is not a canonical stage, workflow engine, Control Plane,
durable state owner, multi-agent cascade or self-healing system. It only checks
the mandate, opens one stage-scoped run at a time, consumes a finite budget and
routes the terminal report to the next already-authorized action.

This artifact does not activate itself, authorize implementation, change an
authority owner, or authorize Commit, Push, Merge or Release. It is an explicit
proposal for a task-local exception to the active manual-dispatch and one-shot
post-validation correction rules. The exception has no effect unless a human
accepts this exact candidate and later activates it for one exact mandate. It
does not change those rules for any other task. Every use still requires a
separate task-local mandate bound to one exact task and subject.

The requested source `TASK_LOCAL_AUTONOMY_HIGH_LEVEL.md` was not found in the
declared search boundary. The current explicit human command supplied the goal,
permissions, forbidden actions, cycle limit and stop conditions used by this
candidate. The missing source remains a provenance limitation and creates no
authority.

## 2. Selected autonomy model

```text
one exact human command
-> immutable task-local mandate
-> thin coordinator
-> PLAN run -> report -> stop
-> EXECUTE run -> self-check -> report -> stop
-> independent VALIDATE run -> verification report -> stop
-> if eligible technical findings exist and budget remains:
     correction EXECUTE run -> report -> stop
     independent VALIDATE run -> verification report -> stop
-> READY_FOR_HUMAN_REVIEW or bounded terminal result
-> stop
```

Stage separation is literal. A run has exactly one canonical stage. The thin
coordinator may start the next run only because the initial human mandate
already authorized that exact transition and the preceding signed report
matches its admission rule. This is the exact task-local exception to
`MANUAL_NEW_RUN`, `automatic_dispatch_admission: NOT_RUN`, the one mechanically
unique preauthorized correction limit and a separate explicit repeat-VALIDATE
request in the active profile. Outside the activated mandate those active rules
remain unchanged. A `PASS` never grants authority.

The initial authoring/validation attempt is cycle `0`. A correction/validation
pair consumes one correction cycle. The only permitted values are `1`, `2` and
`3`; therefore one task has at most four `VALIDATE` runs and three correction
`EXECUTE` runs.

## 3. Non-negotiable invariants

1. One mandate is bound to one `task_id`, one outcome and one exact subject.
2. `planning/CURRENT.md` remains the only durable lifecycle state owner.
3. The owner map remains navigation/provenance-only.
4. Each stage run returns one report and stops before another stage starts.
5. `VALIDATE` is independent, read-only and zero-write; it never corrects.
6. Correction is a new `EXECUTE` run and is limited to eligible findings,
   exact allowed paths and the remaining cycle budget.
7. Product, architecture direction, scope and authority owners cannot be
   selected or changed by the agent.
8. Human acceptance and every Commit, Push, Merge and Release remain human
   actions outside the mandate.
9. Required `NOT_RUN`, `UNKNOWN`, `NOT_FOUND` and `BLOCKED` cannot become
   `PASS` by inference.
10. No runtime model fallback, recursive dispatch, nested task activation,
    unbounded retry, concurrent writer or automatic next task is permitted.

## 4. Task-local mandate schema

The human command is normalized once before `PLAN`. Normalization may make
technical details exact but may not add authority. Any missing required
authority-bearing field yields `BLOCKED`.

```yaml
task_local_mandate:
  schema_version: 1
  mandate_id: REQUIRED_UNIQUE_STRING
  task_id: REQUIRED_UNIQUE_STRING
  issued_by: HUMAN
  issued_at: RFC3339_TIMESTAMP
  authority_basis: CURRENT_EXPLICIT_HUMAN_DECISION
  human_command_locator: PROVIDER_THREAD_AND_MESSAGE_LOCATOR
  human_command_sha256: LOWERCASE_64_HEX | UNAVAILABLE_AT_RUNTIME
  exact_subject:
    kind: DOCUMENTATION_PATH_SET | CONFIGURATION_PATH_SET
    starting_identity:
      repository_root: REPOSITORY_RELATIVE_IDENTITY
      branch_or_detached: STRING
      head_sha: LOWERCASE_40_HEX
      subject_manifest_sha256_or_absent_marker: LOWERCASE_64_HEX_OR_MARKER
    allowed_paths: [REPOSITORY_RELATIVE_POSIX_PATH]
    forbidden_paths: [REPOSITORY_RELATIVE_POSIX_PATH]
  outcome: NON_EMPTY_STRING
  canonical_stages_authorized: [PLAN, EXECUTE, VALIDATE]
  mutation_authorization:
    documentation_or_configuration_only: true
    allowed_operations: [CREATE, MODIFY]
    forbidden_operations: [DELETE, RENAME, IMPLEMENTATION]
  validation:
    independent_required: true
    mode: READ_ONLY_NEW_RUN
    profile_id: REQUIRED_STRING
    validator_selector:
      role: INDEPENDENT_VALIDATOR
      configured_model: STRING
      reasoning_profile: STRING
      read_only: true
      runtime_fallback: FORBIDDEN
  correction_budget:
    max_correction_validation_cycles: 3
    eligible_finding_classes:
      - STRUCTURE
      - SCHEMA
      - HASH_OR_MANIFEST
      - LINK_OR_FENCE
      - TRACEABILITY
      - INTERNAL_CONSISTENCY
      - REPORT_OR_PACKET_MECHANICS
    same_scope_only: true
  state_persistence:
    owner_path: planning/CURRENT.md
    update_authorized: true
  protected_human_decisions:
    - PRODUCT_DIRECTION
    - ARCHITECTURE_DIRECTION
    - SCOPE_EXPANSION
    - AUTHORITY_OWNER_CHANGE
    - HUMAN_ACCEPTANCE
    - COMMIT
    - PUSH
    - MERGE
    - RELEASE
    - NEXT_TASK_OR_INTERVAL_ACTIVATION
  stop_conditions: [NON_EMPTY_STOP_CONDITION]
  expires_on:
    - terminal human-decision boundary reached
    - correction budget exhausted
    - unexpected subject mutation outside an admitted stage transition
    - starting baseline, allowed path set or owner changes
    - material protected decision becomes required
  git_authorization: NONE
```

The normalized mandate is immutable for the task instance. Its maximum budget
never changes; the consumed/remaining counters live only in the report chain
and `planning/CURRENT.md`. An expected subject mutation made by an admitted
`EXECUTE` creates the next subject generation and does not expire the mandate.
A changed path set, outcome, authority owner, starting baseline or protected
decision requires a new human command; it cannot be patched as a technical
correction.

## 5. Identity and packet mechanics

All path and byte identities use the rules of the active post-stop
documentation validation profile: repository-relative POSIX paths, UTF-8
without BOM, LF line endings, raw-file SHA-256 and bytewise lexical path order.

The task subject manifest is:

```text
AOS-TASK-LOCAL-SUBJECT-V1<LF>
TASK<TAB><task-id><LF>
FILE<TAB><path><TAB><byte-length><TAB><raw-file-sha256><LF>
```

The normalized mandate is serialized into exactly these UTF-8/LF records in
the shown order. Text fields reject TAB, CR, LF and NUL. List values are emitted
as one record per item in ascending UTF-8 byte order. Booleans use lowercase
`true`/`false`; integers use unsigned ASCII decimal without leading zeroes.

```text
AOS-TASK-LOCAL-MANDATE-V1<LF>
MANDATE<TAB><mandate-id><TAB><task-id><TAB><issued-at><LF>
AUTHORITY<TAB>CURRENT_EXPLICIT_HUMAN_DECISION<TAB><human-command-locator><TAB><human-command-sha256-or-UNAVAILABLE_AT_RUNTIME><LF>
SUBJECT<TAB><kind><TAB><repository-root><TAB><branch-or-detached><TAB><head-sha><TAB><starting-subject-manifest-sha256-or-absent-marker><LF>
OUTCOME<TAB><outcome><LF>
ALLOWED_PATH<TAB><path><LF>
FORBIDDEN_PATH<TAB><path><LF>
ALLOWED_OPERATION<TAB><operation><LF>
FORBIDDEN_OPERATION<TAB><operation><LF>
STAGE<TAB><stage><LF>
VALIDATION<TAB><profile-id><TAB>READ_ONLY_NEW_RUN<TAB>true<LF>
VALIDATOR_SELECTOR<TAB><role><TAB><configured-model><TAB><reasoning-profile><TAB>true<TAB>FORBIDDEN<LF>
CORRECTION_LIMIT<TAB>3<LF>
ELIGIBLE_FINDING<TAB><class><LF>
STATE_OWNER<TAB>planning/CURRENT.md<TAB>true<LF>
PROTECTED_DECISION<TAB><decision><LF>
STOP_CONDITION<TAB><condition><LF>
GIT_AUTHORIZATION<TAB>NONE<LF>
```

`mandate_sha256` is SHA-256 of exactly those bytes. If the platform does not
expose exact human-message bytes, the literal marker
`UNAVAILABLE_AT_RUNTIME` is used together with the provider message locator;
this limitation is explicit and does not weaken the current live human authority
inside the uninterrupted orchestration session. It can never authenticate that
authority after session loss or cold start. A later cold start may continue
mutation only when the exact human-message digest and stable provider locator
are both available and verify. Otherwise it returns `BLOCKED` and requires the
human to reissue one exact command. Persisting a writer-normalized mandate does
not replace independently verifiable human-decision bytes.

The runner selector is serialized independently so the packet can bind it
before a runtime `run_id` exists:

```text
AOS-TASK-LOCAL-RUNNER-SELECTOR-V1<LF>
SELECTOR<TAB><role><TAB><configured-model><TAB><reasoning-profile><TAB><read-only-boolean><TAB><runtime-fallback-policy><LF>
```

`runner_selector_sha256` is SHA-256 of exactly those bytes.

The stage packet is immutable input to one run:

```yaml
stage_packet:
  schema_version: 1
  packet_id: LOWERCASE_64_HEX
  mandate_sha256: LOWERCASE_64_HEX
  task_id: STRING
  stage: PLAN | EXECUTE | VALIDATE
  cycle_index: 0 | 1 | 2 | 3
  attempt_kind: INITIAL | CORRECTION | RECOVERY | STATE_RECORD
  admitted_by_report_sha256: LOWERCASE_64_HEX | INITIAL_MANDATE
  starting_subject_manifest_sha256_or_absent_marker: STRING
  allowed_paths: [REPOSITORY_RELATIVE_POSIX_PATH]
  admitted_finding_ids: [STRING]
  runner_selector_sha256: LOWERCASE_64_HEX
  runtime_identity_finalization: REQUIRED_AT_RUN_START
  expected_report_schema: TASK_LOCAL_STAGE_REPORT_V1 | TASK_LOCAL_VERIFICATION_REPORT_V1
```

The packet manifest is emitted in exactly this order; repeated path and finding
records are sorted by UTF-8 bytes and use the same control-byte rejection:

```text
AOS-TASK-LOCAL-PACKET-V1<LF>
PACKET<TAB><mandate-sha256><TAB><task-id><TAB><stage><TAB><cycle-index><TAB><attempt-kind><LF>
ADMITTED_BY<TAB><report-sha256-or-INITIAL_MANDATE><LF>
STARTING_SUBJECT<TAB><manifest-sha256-or-absent-marker><LF>
ALLOWED_PATH<TAB><path><LF>
FINDING<TAB><finding-id><LF>
RUNNER_SELECTOR<TAB><runner-selector-sha256><LF>
REPORT_SCHEMA<TAB><schema-id><LF>
```

`packet_id` is SHA-256 of exactly those bytes. At run start, the selected runner
returns a runtime handshake before receiving the semantic subject locator or
write capability. The coordinator verifies the handshake against the immutable
selector and constructs these exact bytes:

```text
AOS-TASK-LOCAL-RUNTIME-PACKET-V1<LF>
BASE_PACKET<TAB><packet-id><LF>
RUNTIME<TAB><provider><TAB><role><TAB><model><TAB><reasoning-profile><TAB><run-id><TAB><stage><TAB><repository-root><TAB><branch-or-detached><TAB><head-sha><LF>
TOOLCHAIN<TAB><toolchain-version><LF>
INSTRUCTION<TAB><loaded-instruction-path><LF>
```

Repeated `TOOLCHAIN` and `INSTRUCTION` records are UTF-8-byte sorted and use the
same control-byte rules. `runtime_packet_sha256` is SHA-256 of exactly those
bytes. Only after this digest is sealed and the selector check passes may the
coordinator release the frozen validation subject or mutation capability. The
actual `run_id` is therefore absent from the immutable mandate/base packet but
present in the pre-work finalized runtime packet. Reports bind `packet_id`,
`runtime_packet_sha256`, mandate digest, runtime identity and observed repository
state. Any mismatch fails closed before semantic inspection or mutation.

## 6. Runtime and independence identity

```yaml
runtime_identity:
  provider: STRING
  role: PRIMARY_WRITER | INDEPENDENT_VALIDATOR
  model: STRING
  reasoning_profile: STRING
  run_id: STRING
  stage: PLAN | EXECUTE | VALIDATE
  repository_root: STRING
  branch_or_detached: STRING
  head_sha: LOWERCASE_40_HEX
  toolchain_versions: [STRING]
  loaded_instruction_paths: [STRING]
```

The writer may perform `PLAN` and mutating `EXECUTE` runs. The independent
validator selector is fixed in the mandate; the actual runtime identity is
finalized only after dispatch and must satisfy that selector before semantic
subject inspection. The validator must use a distinct `run_id`, receive only
the frozen packet and declared sources, have read-only repository authority,
perform no Git mutation, and report `repository_mutations: []`. Different model
identity is optional; separate runtime context, role, packet and zero-write
Evidence are mandatory.

If the bound validator is unavailable or materially insufficient, the result is
`BLOCKED` and the run stops. Automatic model fallback and same-request retry are
forbidden.

## 7. Canonical stage contracts

### 7.1. PLAN

`PLAN` is read-only. It resolves the exact path set, decomposition, validation
matrix, negative cases and stop conditions. It may choose technical schemas,
hash mechanics, report fields and routing that do not alter protected human
decisions. Its report either admits the initial `EXECUTE` packet or stops.

### 7.2. Initial EXECUTE

The writer re-observes root, branch, HEAD, worktree, status, candidate identity
and allowlist. It performs only the documentation/configuration mutation in the
packet, runs the complete internal self-check, corrects only its own in-run
eligible findings within the same allowed paths, repeats the full check after
every such correction, freezes the subject, returns a Stage Report and stops.

Internal authoring corrections do not consume the post-`VALIDATE` correction
budget, but they cannot continue after freeze or cross a protected boundary.

### 7.3. Independent VALIDATE

The validator reconstructs every identity from raw bytes, verifies authoritative
inputs, structure, semantics, traceability, negative cases, authority safety,
downstream usability and zero-write behavior. It does not accept author claims
as Evidence, does not mutate the subject or `planning/CURRENT.md`, returns one
Verification Report and stops.

The coordinator captures the exact validator transport payload bytes before any
parse, summarization or field extraction. The payload must be UTF-8 without BOM
and LF-normalized by the transport contract; otherwise validation is `BLOCKED`.
Its raw SHA-256 and byte length become the only admissible validation-report
identity. A primary-authored summary or field-subset receipt is `REPORTED` and
can never admit correction.

### 7.4. Correction or recovery EXECUTE

A correction or partial-write recovery packet is eligible only when every
finding is mechanically mapped to an existing allowed path, has one unambiguous
same-scope resolution, changes no protected decision and the correction budget
is positive. The writer may resolve only admitted finding IDs and observed
partial paths. It reruns the full internal check, freezes a new subject identity,
consumes exactly one correction cycle, reports and stops. A failed initial or
correction `EXECUTE` may admit this recovery route once per remaining cycle; it
is never a retry of the same packet.

### 7.5. State-recording EXECUTE

After every valid terminal stage report other than a `STATE_RECORD` report, the primary writer runs one bounded
`STATE_RECORD` `EXECUTE` packet whose only allowed path is
`planning/CURRENT.md`. It persists the immutable mandate manifest/digest, latest
report exact transport bytes or inline base64 plus raw digest, subject generation,
consumed and remaining cycle count, pending stage and readiness already observed.
It creates no new transition or authority, returns a non-recursively-recorded
Stage Report and stops. A failed state record blocks the next stage; it does not
consume a correction cycle or permit validator writes. A `STATE_RECORD` report
is never itself input to another `STATE_RECORD` operation.

### 7.6. Human review boundary

When independent validation is technically sufficient, the coordinator may
classify readiness as `READY_FOR_HUMAN_REVIEW`. The primary writer records that
observed result through the final `STATE_RECORD` packet, then expires the
mandate, records no human decision, activates no next task or interval and
stops.

## 8. Finite coordinator transition table

| Current terminal report | Admission | Next action |
|---|---|---|
| Valid `PLAN` report; no material blocker | Report matches mandate | Run `STATE_RECORD`, then start initial `EXECUTE` only after its PASS report |
| Valid initial/correction/recovery `EXECUTE` report; frozen subject and internal check pass | Exact report and subject identities match | Run `STATE_RECORD`, then start independent `VALIDATE` only after its PASS report |
| Failed `EXECUTE` with eligible partial writes | Budget positive; one exact mapping per finding/partial path | Run `STATE_RECORD`, consume one cycle, then start one `RECOVERY` `EXECUTE` packet |
| Failed `EXECUTE` with no eligible recovery | None | Run terminal `STATE_RECORD`; `BLOCKED`; stop |
| `VALIDATE: PASS` or `HUMAN_REVIEW_REQUIRED`; review applicable | Required checks pass; no required `NOT_RUN` | Run final `STATE_RECORD`; set `READY_FOR_HUMAN_REVIEW`; expire mandate; stop |
| `VALIDATE: FAIL` with only eligible findings | Budget positive; one exact mapping per finding | Run `STATE_RECORD`, consume one cycle, then start one correction `EXECUTE` packet |
| `VALIDATE: BLOCKED` caused only by eligible packet/identity mechanics | Budget positive; same scope and subject recoverable | Run `STATE_RECORD`, consume one cycle, then start one correction `EXECUTE` packet |
| `STATE_RECORD: PASS` | Report binds the expected preceding report and exact pending stage | Start that one pending stage directly; do not record the `STATE_RECORD` report |
| Any required `STATE_RECORD` result is not PASS | None | Preserve preceding report; `BLOCKED`; stop |
| Any result requiring protected decision, scope/owner/baseline change or forbidden operation | None | `BLOCKED`; stop for human decision |
| Budget is zero and validation is not sufficient | None | `NOT_READY`; stop for human decision |
| Report/packet/identity mismatch or validator mutation | None | `CONTRACT_VIOLATION`; stop |

The coordinator has no general queue and no discovery of additional work. The
next action must be a literal transition in this table and must remain inside
the same mandate. A correction packet's `ADMITTED_BY` value is always the raw
SHA-256 of the exact captured independent Verification Report bytes stored by
the preceding `STATE_RECORD`; a summary, receipt, reserialization or extracted
field set is forbidden.

## 9. Correction algorithm

```text
validate frozen subject
if technically sufficient:
    readiness = READY_FOR_HUMAN_REVIEW
    run final STATE_RECORD EXECUTE
    stop
else if findings contain any protected or non-eligible item:
    result = BLOCKED
    run terminal STATE_RECORD EXECUTE
    stop
else if remaining_cycles == 0:
    readiness = NOT_READY
    run terminal STATE_RECORD EXECUTE
    stop
else:
    bind exact finding IDs and current subject identity
    remaining_cycles -= 1
    run STATE_RECORD EXECUTE with the consumed budget and pending correction
    run one correction EXECUTE
    freeze new subject
    run STATE_RECORD EXECUTE with the new subject generation
    run one independent VALIDATE
    repeat from first line
```

There is no retry of the same stage packet. A new correction packet has a new
identity and can exist only after a terminal validation report. Concurrency is
forbidden for writer runs and for writer/validator access to the subject.
`remaining_cycles` is derived as `3 - count(unique consumed cycle indexes)`
from the report chain and is mirrored in `planning/CURRENT.md`; it is not a
mutable mandate field.

## 10. Reports and evidence

Every stage report preserves the generic schema owned by
`docs/03_Development.md` and adds this mapping:

```yaml
task_local_extension:
  schema_version: 1
  mandate_id: STRING
  mandate_sha256: LOWERCASE_64_HEX
  packet_id: LOWERCASE_64_HEX
  runtime_packet_sha256: LOWERCASE_64_HEX
  cycle_index: 0 | 1 | 2 | 3
  attempt_kind: INITIAL | CORRECTION | RECOVERY | STATE_RECORD
  runner_selector_sha256: LOWERCASE_64_HEX
  runner_identity: RUNTIME_IDENTITY
  input_subject_manifest_sha256_or_absent_marker: STRING
  output_subject_manifest_sha256_or_absent_marker: STRING
  admitted_finding_ids: [STRING]
  resolved_finding_ids: [STRING]
  remaining_correction_cycles: 0 | 1 | 2 | 3
  state_owner_update: NOT_RUN | PERFORMED
  readiness: NOT_READY | READY_FOR_HUMAN_REVIEW
  human_decision: null
  implementation_authorization: NONE
  git_authorization: NONE
```

The independent Verification Report additionally records exact checks, source
hashes, findings, required corrections, subject hashes before/after, worktree
status before/after, staged state before/after and `zero_write: PASS | FAIL`.
Report bytes are Evidence, not acceptance or authority.

## 11. Durable state projection

Only `planning/CURRENT.md` may persist task progress. The coordinator may ask
the primary writer to update it only when the exact mandate authorizes that path
and the update records an already-observed transition. The state projection
contains:

```yaml
task_local_autonomy:
  task_id: STRING
  contract_identity: PATH_AND_SHA256
  mandate_manifest: INLINE_UTF8_BASE64
  mandate_sha256: LOWERCASE_64_HEX
  mandate_status: ACTIVE | CONSUMED | EXPIRED | BLOCKED
  current_stage: PLAN | EXECUTE | VALIDATE | NONE
  cycle_index: 0 | 1 | 2 | 3
  remaining_correction_cycles: 0 | 1 | 2 | 3
  subject_generation: UNSIGNED_INTEGER
  subject_manifest_sha256_or_absent_marker: STRING
  last_terminal_report:
    locator: REPOSITORY_RELATIVE_PATH | INLINE_UTF8_BASE64 | EXACT_TRANSPORT_PAYLOAD_BASE64
    byte_length: UNSIGNED_INTEGER
    sha256: LOWERCASE_64_HEX
    result: REPORTED_RESULT
  pending_stage: PLAN | EXECUTE | VALIDATE | NONE
  readiness: NOT_READY | READY_FOR_HUMAN_REVIEW
  human_decision: null
```

This is a projection, not a second owner. It cannot mint or extend a mandate.
A current explicit human decision outranks it. `VALIDATE` never writes it;
recording a validation result is a separate bounded `STATE_RECORD` `EXECUTE`
operation explicitly included in the finite transition table. The first such
record makes cold-start recovery possible; absence or mismatch of its mandate
or report identity blocks continuation.

## 12. Failure and recovery matrix

| Finding | Classification | Automatic technical action allowed |
|---|---|---|
| YAML/schema/hash/manifest/link/fence defect in allowed path | `FAIL` | One bound correction cycle if unambiguous |
| Traceability or internal contradiction resolvable from authoritative inputs | `FAIL` | One bound correction cycle if no decision is selected |
| Stale baseline or changed allowed path set | `BLOCKED` | None; new human command required |
| Missing product or architecture direction | `BLOCKED` | None |
| Scope or authority owner must change | `BLOCKED` | None |
| Validator unavailable under exact binding | `BLOCKED` | None; no fallback |
| Validator wrote any repository byte or Git state | `CONTRACT_VIOLATION` | None |
| Required Evidence absent | `UNKNOWN` or `NOT_RUN` | None unless its collection is already exact, read-only and in scope |
| Eligible initial/correction `EXECUTE` leaves partial writes | `FAIL` | Preserve inventory; consume one cycle; run one new recovery packet |
| Failed or mismatched state-recording `EXECUTE` | `BLOCKED` | None; preserve preceding terminal report |
| Correction budget exhausted | `FAIL` or `BLOCKED` as observed | None |
| Human acceptance, Commit, Push, Merge, Release or next task required | Human boundary | None |

Partial writes are inventoried and preserved. Recovery may repair them only
inside the exact allowed paths, from a new packet admitted by the failed report,
and only when the original mandate still binds the starting baseline plus every
observed subject generation. It consumes one correction cycle. A second failure
may enter another new recovery packet only if budget remains; the fourth cycle
is forbidden. Otherwise the task stops with one next human decision.

## 13. Required negative cases

An independent validator must test or inspect at least these cases:

1. a `PASS` report with a required check `NOT_RUN`;
2. mutation performed during `VALIDATE`;
3. correction changes a non-allowed path;
4. correction attempts a product or architecture choice;
5. subject bytes change between freeze and validation;
6. report, packet, mandate or runtime identity mismatch;
7. a fourth correction cycle is requested;
8. validator binding is unavailable and a fallback is attempted;
9. `READY_FOR_HUMAN_REVIEW` is treated as acceptance;
10. Commit, Push, Merge, Release or next-task activation is inferred;
11. two writers mutate concurrently;
12. `planning/CURRENT.md` is replaced by a competing state owner;
13. missing high-level source is silently described as observed;
14. validator or coordinator recursively spawns a new task.
15. an expected admitted subject generation incorrectly expires the mandate;
16. actual validator runtime identity does not satisfy the immutable selector;
17. a terminal report advances without the required `STATE_RECORD` PASS;
18. partial-write recovery reuses the failed packet or avoids cycle consumption.
19. a primary-authored validation summary admits correction;
20. semantic subject access occurs before runtime-packet finalization;
21. a `STATE_RECORD` report recursively triggers another `STATE_RECORD`;
22. cold-start mutation proceeds with `UNAVAILABLE_AT_RUNTIME` human identity.

## 14. Validation requirements for this candidate

The exact candidate must receive an independent read-only validation bound to
its raw bytes and authoritative input hashes. Required levels are:

- `L0`: identity, YAML/frontmatter, Markdown structure, fences and links;
- `L1`: scope, owner boundaries, stage separation, report schemas, finite cycle
  budget, failure/recovery and negative cases;
- `L2`: cold-start usability, deterministic transition routing, absence of a
  global engine/cascade/self-heal, and consistency with the active owners.

The validation result may recommend `READY_FOR_HUMAN_REVIEW`; it must set
`human_decision: null`, `implementation_authorization: NONE` and
`git_authorization: NONE`.

## 15. Acceptance and activation boundary

Human review may choose `ACCEPT`, `NEEDS_CHANGES`, `REJECT` or `DEFER` for the
exact hash-bound candidate. `PASS` and `READY_FOR_HUMAN_REVIEW` do not perform
that decision.

If accepted later, a separate exact activation decision is still required
before this model governs another task. Activation must bind the contract hash,
one mandate, exact task/subject/paths, validation profile, runtime identities,
cycle budget and stop conditions. It cannot activate `INT-DOC-010` or any other
task or interval.

```yaml
technical_result: NOT_RUN
readiness: NOT_READY
human_decision: null
implementation_authorization: NONE
git_authorization: NONE
next_required_action: INDEPENDENT_VALIDATE_EXACT_TASK_LOCAL_AUTONOMY_CONTRACT_R1
stop: true
```
