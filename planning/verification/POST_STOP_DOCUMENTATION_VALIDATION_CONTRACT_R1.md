---
document_type: POST_STOP_DOCUMENTATION_VALIDATION_CONTRACT
artifact_id: POST-STOP-DOCUMENTATION-VALIDATION-CONTRACT-R1
revision: R6
status: DRAFT_CANDIDATE
task_id: INT-DOC-001B-CORRECTION-006
source_task_id: INT-DOC-001B-EXECUTE-001
interval_id: INT-DOC-001B
authoring_stage: EXECUTE
canonical_validation_stage: VALIDATE
validation_mode: READ_ONLY_NEW_RUN
profile_lifecycle: DRAFT
durable_lifecycle_state_owner: planning/CURRENT.md
chat_history_required: false
automatic_validate_dispatch: FORBIDDEN
implementation_authorization: NONE
git_authorization: NONE
---

# Post-Stop Documentation Validation Contract R1 — Corrected Candidate R6

## 1. Purpose, status and authority boundary

This contract defines the candidate validation profiles, exact read-only
validator boundary, terminal report schemas, lifecycle, persistence boundary,
readiness vocabulary and post-validation correction route for bounded AOS
documentation intervals.

This exact revision is a pilot-only `DRAFT_CANDIDATE`. It does not govern
normal documentation validation until all of the following have occurred:

1. the exact candidate is frozen by its authoring `EXECUTE` Stage Report;
2. an independent `L2` validation of that exact candidate finishes and stops;
3. a human explicitly accepts the exact hash-bound revision;
4. a separate authorized activation records the profile lifecycle as active.

The document cannot validate, accept, activate or persist itself. Its presence,
an internal self-check, an independent validation `PASS`, readiness, Evidence or
a stored report does not create human acceptance, implementation authorization
or Git authorization.

Canonical boundaries:

```text
internal self-check inside EXECUTE != canonical VALIDATE
technical result != readiness
readiness != human decision
PASS != approval
Evidence != approval
Edit != Commit != Push != Merge != Release
```

## 2. Source boundary and precedence

The contract is derived only from the current explicit human decision and the
necessary sections of these repository owners:

- [Core authority and safety](../../docs/00_Core.md);
- [Architecture contracts and state axes](../../docs/02_Architecture.md);
- [Development stages, validation, recovery and Git boundaries](../../docs/03_Development.md);
- [Lessons and regression candidates](../../docs/04_Lessons.md);
- [Documentation Task Sequence R9](../AOS_Documentation_Task_Sequence_R9.md);
- [Authoritative Owner Map R1](../AOS_Authoritative_Owner_Map_R1.md);
- [Current persisted workflow state](../CURRENT.md);
- direct current repository observation for mutable repository facts.

Chat history, chat summaries, assistant notes and inferred target facts are not
canonical inputs. Authority remains limited to each owner's fact class. If this
contract conflicts with an authoritative owner, the affected contract claim is
stale; the validator reports the conflict and blocks only the affected action.

Claim classifications in validation records use only this closed vocabulary:

```text
OBSERVED_AT_SNAPSHOT | REPORTED | SYNTHESIZED | CONFLICT |
NOT_FOUND | UNKNOWN | NOT_RUN | BLOCKED
```

`PASS`, `FAIL` and the other technical results are not claim classifications.
Mutable Git and filesystem facts are always classified
`OBSERVED_AT_SNAPSHOT`, include their observation boundary, and are re-observed
before each validation or later authorized action.

## 3. Canonical stage and validation profiles

`VALIDATE` is the only canonical validation stage. A profile narrows checks and
applicability; it never creates another stage enum.

```yaml
canonical_stage: VALIDATE
mode: READ_ONLY_NEW_RUN
one_run_one_stage: true
subject_mutation: FORBIDDEN
repository_mutation: FORBIDDEN
automatic_dispatch: FORBIDDEN
automatic_retry: FORBIDDEN
automatic_transition: FORBIDDEN
terminal_report_required: true
stop_after_report: true
```

### 3.1. Profile registry and applicability

| Profile | Authority and lifecycle | Applicable subject | Required depth | Permitted result |
|---|---|---|---|---|
| `BOOTSTRAP_INLINE_R9_PROFILE_VALIDATION` | Owned by the exact accepted R9 bootstrap route; active only for bootstrap validation of this candidate; not created by this document | Exact frozen `INT-DOC-001B` artifact plus its terminal Stage Report | `L0 + L1 + L2`, independent verifier required | One non-durable Verification Report, then `STOP` |
| `POST_STOP_DOCUMENTATION` | Defined by this contract but `DRAFT` until exact human acceptance and separate activation | Every terminal documentation Stage Report, with a complete artifact, partial artifact or no artifact | `L0 + L1`; add `L2` when required by section 3.2 | One non-durable Verification Report, then `STOP` |

Normal use of `POST_STOP_DOCUMENTATION` is forbidden while its lifecycle is not
`HUMAN_ACCEPTED_ACTIVE`. Bootstrap validation therefore uses the inline R9
profile and never uses the candidate profile to validate itself.

### 3.2. Validation depth

```text
L0 - deterministic identity, paths, structure, schemas, links and hashes
L1 - semantic completeness, traceability, authority and readiness boundaries
L2 - independent cold-start agent usability without chat history
```

`L2` is mandatory for:

- this exact validation-contract bootstrap candidate;
- Product or Feature Contracts;
- task, runner or coordinator contracts;
- validation profiles;
- implementation handoff or readiness claims;
- any subject whose interval contract or explicit human decision requires it.

Depth is an applicability rule, not permission to widen subject scope. A check
that cannot be performed remains visible as `NOT_RUN`, `UNKNOWN` or `BLOCKED`;
it is never silently removed.

### 3.3. Closed validation-profile lifecycle

The validation-profile lifecycle is closed:

```text
DRAFT
-> HUMAN_ACCEPTED_INACTIVE
-> HUMAN_ACCEPTED_ACTIVE
-> SUPERSEDED

off-route terminal state: REVOKED
```

Only these transitions are permitted:

| From | To | Required authority and Evidence |
|---|---|---|
| `DRAFT` | `HUMAN_ACCEPTED_INACTIVE` | Exact human `ACCEPT` record bound to the exact profile identity |
| `HUMAN_ACCEPTED_INACTIVE` | `HUMAN_ACCEPTED_ACTIVE` | Separate exact human activation decision and activation record |
| `HUMAN_ACCEPTED_INACTIVE` | `SUPERSEDED` | Exact accepted successor identity and exact human supersession decision |
| `HUMAN_ACCEPTED_ACTIVE` | `SUPERSEDED` | Exact accepted successor identity, exact human supersession decision and removal of the old active reference |
| `DRAFT` | `REVOKED` | Exact human revocation decision |
| `HUMAN_ACCEPTED_INACTIVE` | `REVOKED` | Exact human revocation decision |
| `HUMAN_ACCEPTED_ACTIVE` | `REVOKED` | Exact human revocation decision and removal of the active reference |

Every unlisted transition is rejected. `SUPERSEDED` and `REVOKED` are terminal.
Technical `PASS` never changes profile lifecycle. Acceptance never implies
activation, and repository presence never implies either.

Exact profile identity is:

```yaml
validation_profile_identity:
  profile_id:
  revision:
  path:
  sha256:
  applicability_class:
```

The acceptance record is human-decision Evidence, not the current-state owner:

```yaml
validation_profile_acceptance_record:
  record_path:
  decision: ACCEPT
  actor:
  decided_at:
  profile_identity:
  decision_record_sha256:
  supersedes_profile_identity: null
```

The activation record is separate:

```yaml
validation_profile_activation_record:
  record_path:
  decision: ACTIVATE
  actor:
  decided_at:
  profile_identity:
  acceptance_record_identity:
  activation_record_sha256:
  applicability_class:
```

Only [planning/CURRENT.md](../CURRENT.md) may durably identify which accepted
profile is current and active for an applicability class. It references the
exact profile, acceptance record and activation record identities. At most one
profile may be active for one exact `applicability_class`; distinct classes may
have different active profiles. In normal persisted-profile use, an accepted
profile with no matching active identity in `planning/CURRENT.md` is
`HUMAN_ACCEPTED_INACTIVE` and cannot govern validation.

The sole bootstrap exception is the externally owned
`BOOTSTRAP_INLINE_R9_PROFILE_VALIDATION` route needed to validate this contract
before this contract can be accepted or activated. A current explicit human
decision may supply a non-durable, one-run bootstrap binding only when it binds
all of these fields exactly:

```yaml
bootstrap_profile_binding:
  decision_id:
  profile_identity:
    profile_id: BOOTSTRAP_INLINE_R9_PROFILE_VALIDATION
    revision:
    path: planning/AOS_Documentation_Task_Sequence_R9.md
    sha256:
  applicability:
    interval_instance_id: INT-DOC-001B
    validated_subject:
      path: planning/verification/POST_STOP_DOCUMENTATION_VALIDATION_CONTRACT_R1.md
      sha256:
    permitted_validation_task:
    validation_level: L2
    mode: READ_ONLY_NEW_RUN
  acceptance:
    decision: ACCEPT
    authority_basis: CURRENT_EXPLICIT_HUMAN_DECISION
  activation:
    decision: ACTIVATE
    authority_basis: CURRENT_EXPLICIT_HUMAN_DECISION
  max_validation_invocations: 1
  expiry: []
  reuse: FORBIDDEN
  scope_expansion: FORBIDDEN
  persistence: NOT_RUN
```

The `acceptance` and `activation` fields are two separately explicit human
decisions even when one exact human record carries both; `ACCEPT` alone never
implies `ACTIVATE`. This binding is run-local Evidence, not durable lifecycle
state, and does not compete with `planning/CURRENT.md`. It expires on its
terminal validation report, subject/profile/source drift, failed or consumed
runtime packet completion, or human revocation. It cannot govern another
candidate, task, interval or invocation and cannot authorize persistence,
correction, Git actions or a next task. Missing or mismatched binding fields are
`BLOCKED`; repository presence never substitutes for the decision.

Any profile byte drift changes its SHA-256 and invalidates acceptance/activation
binding for the changed bytes. No lifecycle transition occurs automatically:
the stale reference is reported as `CONFLICT`, affected use is blocked, and a
separate human decision plus separately authorized persistence action is
required. This R6 candidate remains `DRAFT`; it is neither accepted nor active,
and this correction does not modify `planning/CURRENT.md`.

Supersession preserves the old profile and decision records as historical
Evidence but permanently forbids reuse of the superseded identity. A successor
does not become active merely because it supersedes another profile; it still
needs its own acceptance, activation and CURRENT reference. Revocation blocks
all further use of the revoked identity, preserves its historical Evidence and
does not select a replacement. Any still-recorded active CURRENT reference to a
superseded or revoked identity is stale until a separately authorized update.

## 4. Trigger, subject kinds and freeze identity

Post-stop validation is required after every terminal documentation Stage
Report, including successful output, partial output, `FAIL`, `BLOCKED`, material
`UNKNOWN` and a run that produced no output artifact.

Closed subject kinds:

```text
OUTPUT_ARTIFACT_AND_STAGE_REPORT
PARTIAL_ARTIFACT_AND_STAGE_REPORT
STAGE_REPORT_ONLY
```

The authoring run ends before validation begins:

```text
DOCUMENTATION_INTERVAL / EXECUTE
-> internal self-check
-> bounded in-scope correction if needed
-> repeated self-check after every correction
-> successful self-check
-> candidate freeze
-> terminal Stage Report
-> STOP
-> manual separate READ_ONLY_NEW_RUN / VALIDATE
-> terminal Verification Report
-> STOP
```

The validation subject identity is:

```yaml
subject_identity:
  task_id_bound_to_interval_instance_id:
  interval_contract_revision_or_sha256:
  stage_report_sha256:
  subject_kind: >
    OUTPUT_ARTIFACT_AND_STAGE_REPORT |
    PARTIAL_ARTIFACT_AND_STAGE_REPORT |
    STAGE_REPORT_ONLY
  subject_paths: []
  subject_set_sha256_or_absent_marker:
  artifact_types: []
  validation_profile_revision_or_sha256:
  authoritative_dependency_set_sha256:
```

For `STAGE_REPORT_ONLY`, `subject_paths` is empty and
`subject_set_sha256_or_absent_marker` contains the declared absent marker. The
Stage Report bytes and its SHA-256 remain part of the frozen validation
subject. Absence is not inferred from chat history.

The final artifact SHA-256 is recorded outside the artifact in the authoring
Stage Report. The artifact does not embed its own digest. Any byte, path,
Stage Report or dependency change after freeze invalidates the validation
binding and requires a new explicit validation request.

### 4.1. Common byte and path rules

All identities below use SHA-256 and lowercase hexadecimal digests. Generated
identity manifests use UTF-8 without BOM and LF (`0A`) line endings. A manifest
ends with exactly one LF. Fields are separated by one TAB (`09`). Required
fields never accept null; a missing required field is malformed input. An
optional field is omitted from the manifest unless its record is explicitly
defined; when a schema permits explicit null, its manifest value is the literal
ASCII token `NULL`. Missing and null are not equivalent.

A repository path is valid only when its UTF-8 bytes:

- are a repository-relative POSIX path;
- contain no BOM, NUL, CR, LF or TAB;
- contain no empty, `.` or `..` component;
- contain no leading slash, trailing slash, repeated slash or backslash;
- are not Unicode-normalized or case-folded by the validator.

Invalid UTF-8, absolute paths, ambiguous normalization and duplicate normalized
paths are deterministic failures. Entries are sorted in ascending lexical order
of the normalized path's UTF-8 bytes. A directory is not a subject-set member;
its files are members individually.

Symlinks are rejected unless the selected profile explicitly permits them and
binds both link text and resolved target bytes. An allowed symlink record is:

```text
SYMLINK<TAB><normalized-path><TAB><target-utf8-byte-length><TAB><link-text><TAB><resolved-target-sha256><LF>
```

The link text is subject to the same control-byte rejection. A nested repository
is rejected unless the profile explicitly declares it as a separately pinned
dependency with repository-relative path and exact commit SHA. Neither an
unexpected symlink nor an unexpected nested repository may be silently followed.

### 4.2. Terminal Stage Report identity

The Stage Report identity is the SHA-256 of the exact Stage Report source bytes,
not a reserialization of parsed YAML. The bytes must be UTF-8 without BOM, use LF
line endings, contain one complete generic Stage Report mapping and be supplied
either by one repository-relative path or as exact inline bytes. If both forms
are supplied, their bytes must be identical. Field order, optional fields and
explicit nulls remain exactly as emitted; missing and null remain distinct.

```yaml
stage_report_identity:
  representation: REPOSITORY_RELATIVE_PATH | INLINE_UTF8_BASE64
  locator_or_inline_value:
  byte_length:
  sha256_of_exact_source_bytes:
```

This raw-byte rule is a validation-profile identity rule only. It does not
redefine project-wide YAML serialization.

### 4.3. Subject-set identity

For a non-empty artifact subject set, construct these exact manifest bytes:

```text
AOS-SUBJECT-SET-MANIFEST-V1<LF>
FILE<TAB><normalized-path><TAB><raw-file-byte-length><TAB><raw-file-sha256><LF>
```

There is one `FILE` record per regular-file subject, sorted by normalized path
bytes. File digests are over exact source bytes. Allowed symlink records use the
format in section 4.1 and participate in the same path sort. Duplicate paths,
unsupported file types, malformed records and ambiguous input fail before a
digest is produced. `subject_set_sha256_or_absent_marker` is the SHA-256 of the
complete manifest bytes.

For a `STAGE_REPORT_ONLY` subject, the exact absent marker literal is:

```text
AOS_ABSENT_SUBJECT_SET_V1
```

The marker is stored literally in `subject_set_sha256_or_absent_marker`; it is
not hashed and no empty subject manifest is substituted for it.

### 4.4. Validation-profile digest

The source file containing the selected profile is hashed as exact raw bytes.
Then construct exactly these records in the shown order:

```text
AOS-VALIDATION-PROFILE-IDENTITY-V1<LF>
PROFILE_ID<TAB><profile-id><LF>
REVISION<TAB><revision><LF>
PATH<TAB><normalized-profile-source-path><LF>
SOURCE_SHA256<TAB><raw-profile-source-file-sha256><LF>
```

`profile_sha256` is the SHA-256 of those manifest bytes. Profile ID and revision
must be non-empty UTF-8 without BOM, CR, LF, TAB or NUL. For
`BOOTSTRAP_INLINE_R9_PROFILE_VALIDATION`, the source path is
`planning/AOS_Documentation_Task_Sequence_R9.md`; the whole exact R9 file is the
source bytes, and its declared bootstrap profile ID/revision are included in the
manifest. For `POST_STOP_DOCUMENTATION`, the source path is this exact contract
and the whole contract file is the source bytes. No heading-range extraction is
permitted.

### 4.5. Authoritative dependency-set digest

Membership is every declared authoritative input actually required by the
selected profile and task contract, including the exact current human decision
record when it is an input. Each member has one locator and exact source-byte
SHA-256. Repository files use `FILE`; an inline human decision uses
`INLINE_DECISION`. Construct:

```text
AOS-AUTHORITATIVE-DEPENDENCY-MANIFEST-V1<LF>
<kind><TAB><locator><TAB><raw-source-byte-length><TAB><raw-source-sha256><LF>
```

Repository-file locators follow section 4.1. An inline-decision locator is
constructed by this closed rule:

1. for a human decision supplied as a runtime message, the locator is always
   `RUNTIME_TURN_ID:<exact-runtime-turn-id>`, where the suffix is the exact
   runtime/session turn UUID that contains that human message;
2. the packet binds the runtime record selector, exact decision bytes, byte
   length and SHA-256; embedded Markdown, fenced blocks, `decision_id` keys and
   other message content are never parsed to construct the locator;
3. the source bytes are the complete
   `response_item.payload.content[0].text` UTF-8 bytes exactly as stored,
   preserving original line endings and terminal-newline presence;
4. a missing exact runtime turn ID, multiple matching messages, an invented
   descriptive label or any byte-boundary ambiguity is deterministic `BLOCKED`
   before a digest is produced;
5. a non-runtime inline decision is rejected unless the selected profile itself
   defines a complete byte-bound locator algorithm; no such alternative is
   defined by this bootstrap profile.

Inline locators are non-empty and reject BOM, NUL, CR, LF and TAB. Sort records
by the UTF-8 bytes of `<kind><TAB><locator>`. Duplicate `(kind, locator)` pairs,
unavailable bytes, malformed digests, undeclared additions and omitted required
dependencies fail deterministically. `authoritative_dependency_set_sha256` is
the SHA-256 of the complete manifest bytes. A separately permitted nested
repository is a `NESTED_REPOSITORY` dependency whose locator is its normalized
path and whose source identity binds the exact commit SHA in its raw dependency
record; otherwise it is rejected.

## 5. Read-only and zero-write invariant

A `VALIDATE` run may read, parse, hash, compare and report. It may not create,
modify, rename, delete, stage, commit, push, merge, release, cache, format,
repair or persist anything in the repository subject.

Before the first validation check and immediately before the Verification
Report, the verifier records fresh read-only observations:

```yaml
zero_write_evidence:
  repository_identity_before:
    repository_root:
    branch:
    HEAD:
    worktree_status:
    staging_status:
    changed_paths: []
  repository_identity_after:
    repository_root:
    branch:
    HEAD:
    worktree_status:
    staging_status:
    changed_paths: []
  subject_identity_before:
    subjects: []
    subject_set_sha256_or_absent_marker:
  subject_identity_after:
    subjects: []
    subject_set_sha256_or_absent_marker:
  repository_mutation_count:
  Git_operations:
    commit: NOT_RUN
    push: NOT_RUN
    merge: NOT_RUN
    release: NOT_RUN
  comparison_result:
  result:
```

`comparison_result: PASS` requires exact equality of repository root, branch,
HEAD, complete worktree-status bytes, complete staging-status bytes, changed-path
sets, every subject path/type/byte-length/SHA-256 record and the subject-set
identity before and after. It also requires `repository_mutation_count: 0` and
every Git operation `NOT_RUN`. Required observations must be classified
`OBSERVED_AT_SNAPSHOT`. A boolean summary never replaces this evidence object.

A repository mutation is any validator-caused creation, content change, rename
or deletion under the repository root; any index/staging change; any Git ref,
HEAD, config, worktree or submodule state change; or any subject identity change.
A temporary file outside the repository root is not a repository mutation when
it neither changes nor substitutes for repository/subject Evidence and is
removed by the external tool boundary. Filesystem access time is ignored.
Content-neutral metadata is ignored unless the selected profile explicitly
binds that metadata; bound metadata then participates in equality.

Result rules are mandatory:

1. Validator-caused repository content or Git-state mutation produces
   `comparison_result: FAIL`, `result: CONTRACT_VIOLATION` and immediate `STOP`.
2. A definite repository or subject identity mismatch not caused by the
   validator produces `comparison_result: FAIL`; the affected validation result
   is `FAIL` or `BLOCKED` according to the profile's fail-closed aggregation and
   no retry is authorized.
3. Unobservable required Evidence or unknown causality produces `result: UNKNOWN`.
4. A required comparison that was not executed produces `result: NOT_RUN`.
5. A pre-existing dirty path is classified and preserved. It blocks only a
   check whose exact subject cannot be isolated from that path.
6. A terminal response is non-durable and does not write a report file.
7. Tools whose read-only behavior cannot be established are `NOT_RUN`.

## 6. Terminal Stage Report schema

Every documentation `EXECUTE` run returns exactly one terminal Stage Report and
stops. The report is part of the later validation subject.

```yaml
task_id:
stage: EXECUTE
result: >
  CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN |
  NOT_RUN | PASS | HUMAN_REVIEW_REQUIRED
starting_identity:
ending_identity:
changed_paths: []
checks_run: []
checks_not_run: []
findings: []
limitations: []
unknowns: []
out_of_scope_state: []
authorization_consumed:
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action:
stop: true

documentation_validation_extension:
  report_kind: DOCUMENTATION_STAGE_REPORT
  interval_instance_id:
  authorization:
    authorization_id:
    authorization_state:
  output:
    expected_paths: []
    present_paths: []
    absent_paths: []
    partial_paths: []
    subject_kind: >
      OUTPUT_ARTIFACT_AND_STAGE_REPORT |
      PARTIAL_ARTIFACT_AND_STAGE_REPORT |
      STAGE_REPORT_ONLY
    subject_set_sha256_or_absent_marker:
    final_candidate_frozen: true | false
  validation_profile: null
  readiness: NOT_READY
  zero_write_evidence: null
  verification_identity: null
  human_decision: null
  implementation_authorization: NONE
  git_authorization: NONE
```

`final_candidate_frozen: true` is permitted only after the final internal
self-check passes. If an in-scope correction occurred, the Stage Report must
also record the repeated check after that correction. A terminal failure before
freeze reports `false` and the exact existing/absent/partial subject state.

The generic Stage Report fields above are authoritative and mandatory. The
extension is lossless and additive:

| Specialized meaning | Generic field | Extension field |
|---|---|---|
| Technical outcome | `result` | No substitute permitted |
| Authorization consumption | `authorization_consumed` | `authorization.authorization_id` and `authorization.authorization_state` add identity/state detail only |
| Git outcomes | `Git_operations` | No differently cased duplicate permitted |
| Repository start/end | `starting_identity`, `ending_identity` | No substitute permitted |
| Subject/output details | Not represented generically | `output` |
| Readiness | Not represented generically | `readiness` |
| Validation identity/Evidence | Not represented generically | `validation_profile`, `verification_identity`, `zero_write_evidence` |

An extension field never changes, shadows or overrides a generic field. A
specialized report is invalid when a required generic field is absent or when
generic and extension values conflict. Parsing the generic fields and preserving
the extension mapping loses no authoritative Stage Report semantics.

### 6.1. Terminal outcome coverage

| Authoring terminal outcome | Required subject kind | Validation obligation |
|---|---|---|
| Complete expected output and Stage Report | `OUTPUT_ARTIFACT_AND_STAGE_REPORT` | Validate artifact, Stage Report and their binding |
| Incomplete or partial output and Stage Report | `PARTIAL_ARTIFACT_AND_STAGE_REPORT` | Validate observed bytes, declared partial state, failure reporting and authority boundaries |
| `FAIL`, `BLOCKED` or material `UNKNOWN` with an artifact | Complete or partial kind matching observed bytes | Validate the report outcome and exact artifact state; do not treat authoring failure as validation failure automatically |
| No output artifact and terminal Stage Report | `STAGE_REPORT_ONLY` | Validate the report, absent marker, precondition/failure evidence and stop behavior |
| Stage Report claims `PASS` while expected output is absent or partial | Kind matching direct observation | `CONTRACT_VIOLATION`; never convert absence to success |
| Required Stage Report missing | No valid frozen subject | `BLOCKED` or `NOT_RUN` for validation; report the missing identity and stop |

## 7. Stage Report-only validation

`STAGE_REPORT_ONLY` is a first-class subject, not a waiver. The verifier:

1. confirms the expected output path and direct absence at the observed
   snapshot;
2. verifies that the Stage Report identifies its pre-mutation or terminal
   subject identity, technical result, authorization state, checks, limitations,
   one next action and `stop: true`;
3. verifies that the reported absence is consistent with the failure or blocker
   and that `PASS` was not claimed;
4. verifies that no unauthorized path was changed and that Git operations remain
   `NOT_RUN`;
5. performs applicable authority, traceability and cold-start checks against the
   report itself;
6. returns a Verification Report and stops without creating the absent artifact.

A validation `PASS` for a Stage Report-only subject means that the exact
failure/blocker report satisfies its contract. It does not change the authoring
technical result, create the missing artifact or make the interval ready.

## 8. Terminal Verification Report schema

```yaml
task_id:
stage: VALIDATE
result: >
  CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN |
  NOT_RUN | PASS | HUMAN_REVIEW_REQUIRED
starting_identity:
ending_identity:
changed_paths: []
checks_run: []
checks_not_run: []
findings: []
limitations: []
unknowns: []
out_of_scope_state: []
authorization_consumed: false
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action:
stop: true

documentation_validation_extension:
  report_kind: POST_STOP_VERIFICATION_REPORT
  validation_profile: >
    BOOTSTRAP_INLINE_R9_PROFILE_VALIDATION |
    POST_STOP_DOCUMENTATION
  work_item_type: POST_STOP_VERIFICATION
  mode: READ_ONLY_NEW_RUN
  subject:
    task_id:
    interval_instance_id:
    stage_report_identity:
    subject_kind:
    paths: []
    subject_set_sha256_or_absent_marker:
    artifact_types: []
    interval_contract_revision_or_sha256:
  verification_identity:
    profile_sha256:
    authoritative_dependency_set_sha256:
    verifier_agent_identity:
    verifier_version:
    verification_id:
    independence_required: true | false
    independence_basis:
  checks:
    identity: {required: true, result: null}
    structural_contract: {required: true, result: null}
    authoritative_inputs: {required: true, result: null}
    semantic_completeness: {required: true, result: null}
    traceability: {required: true, result: null}
    agent_usability: {required: null, result: null}
    authority_safety: {required: true, result: null}
    downstream_readiness: {required: true, result: null}
    zero_write: {required: true, result: null}
  zero_write_evidence:
    repository_identity_before:
      repository_root:
      branch:
      HEAD:
      worktree_status:
      staging_status:
      changed_paths: []
    repository_identity_after:
      repository_root:
      branch:
      HEAD:
      worktree_status:
      staging_status:
      changed_paths: []
    subject_identity_before:
      subjects: []
      subject_set_sha256_or_absent_marker:
    subject_identity_after:
      subjects: []
      subject_set_sha256_or_absent_marker:
    repository_mutation_count:
    Git_operations:
      commit: NOT_RUN
      push: NOT_RUN
      merge: NOT_RUN
      release: NOT_RUN
    comparison_result:
    result:
  authoring_result:
  readiness: NOT_READY
  readiness_reason:
  human_decision: null
  human_decision_ref: null
  implementation_authorization: NONE
  git_authorization: NONE
  report_persistence: NOT_RUN
  required_corrections: []
  blockers: []
  stale_current_findings: []
  next_bounded_action:
```

The Verification Report is a non-durable terminal response. It cannot mutate
`planning/CURRENT.md`, persist itself, create acceptance, activate a profile,
dispatch correction, start a next interval or authorize any Git action.
The embedded `zero_write_evidence` object is mandatory and is governed by
section 5; `checks.zero_write.result` is only its summary. The generic fields
remain authoritative, and the lossless mapping rules in section 6 also apply to
this specialized terminal Stage Report.

## 9. Check aggregation and finding classification

Required checks aggregate fail-closed in this order:

```text
validator contract violation -> CONTRACT_VIOLATION
else required FAIL -> FAIL
else required BLOCKED -> BLOCKED
else required UNKNOWN -> UNKNOWN
else required NOT_RUN -> NOT_RUN
else applicable human gate required -> HUMAN_REVIEW_REQUIRED
else -> PASS
```

An optional `NOT_RUN` may remain visible without blocking only when the profile
explicitly marks that check optional. No omitted, unavailable or unsupported
required check can aggregate to `PASS`.

Every finding uses this schema:

```yaml
finding:
  finding_id:
  claim_class: >
    OBSERVED_AT_SNAPSHOT | REPORTED | SYNTHESIZED | CONFLICT |
    NOT_FOUND | UNKNOWN | NOT_RUN | BLOCKED
  finding_type: >
    CONTRACT_VIOLATION | REQUIRED_CHECK_FAILURE | BLOCKER |
    MATERIAL_UNKNOWN | REQUIRED_NOT_RUN | HUMAN_REVIEW_GATE |
    INFORMATIONAL
  summary:
  confirmed_facts: []
  evidence_refs: []
  affected_fact_class:
  affected_claim:
  affected_action:
  blocked_scope:
  required_resolution:
```

Affected-action boundaries:

| Finding type | Minimum technical effect | Boundary |
|---|---|---|
| `CONTRACT_VIOLATION` | `CONTRACT_VIOLATION` | Invalidates this validation result; no repair or retry in the run |
| `REQUIRED_CHECK_FAILURE` | `FAIL` | Blocks only claims/actions requiring the failed check |
| `BLOCKER` | `BLOCKED` | Blocks the named action until its exact prerequisite closes |
| `MATERIAL_UNKNOWN` | `UNKNOWN` | Blocks only the claim/action that depends on missing Evidence; safe unrelated read-only reporting may continue |
| `REQUIRED_NOT_RUN` | `NOT_RUN` | Prevents aggregate `PASS`; does not masquerade as failure Evidence |
| `HUMAN_REVIEW_GATE` | `HUMAN_REVIEW_REQUIRED` when otherwise technically sufficient | Routes to a human; creates no decision |
| `INFORMATIONAL` | No automatic downgrade | Remains visible and cannot create readiness or authority |

The verifier never guesses a missing owner, fact, subject identity or human
decision. `NOT_FOUND` applies only inside the declared search boundary.

## 10. Technical result, readiness and human decision

The three axes are recorded independently.

Technical result vocabulary:

```text
CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN |
NOT_RUN | PASS | HUMAN_REVIEW_REQUIRED
```

Readiness vocabulary:

```text
NOT_READY
READY_FOR_HUMAN_REVIEW
READY_FOR_NEXT_DOCUMENTATION_TASK
READY_FOR_PORTABLE_TASK_DERIVATION
TARGET_REPOSITORY_ASSIGNMENT_REQUIRED
TARGET_BINDING_REQUIRED
READY_FOR_TARGET_BOUND_TASK_BRIEF
READY_FOR_IMPLEMENTATION_HUMAN_DECISION
EXTERNAL_EVIDENCE_REQUIRED
```

Human decision vocabulary, only in an exact human-authored or human-verified
record:

```text
ACCEPT | NEEDS_CHANGES | REJECT | DEFER
```

`NEEDS_CHANGES` and `BLOCKED` are not readiness states. Unqualified `READY`,
`DONE`, `COMPLETE` and `IMPLEMENTATION_READY` are forbidden as authoritative
readiness states.

### 10.1. Readiness matrix

The matrix constrains eligible readiness; it does not derive readiness from a
technical result automatically.

| Conditions at exact validation subject | Eligible readiness | Human decision in Verification Report | Authorized transition |
|---|---|---|---|
| `CONTRACT_VIOLATION`, `FAIL`, `BLOCKED`, `UNKNOWN` or required `NOT_RUN` | `NOT_READY` | `null` | None; one bounded resolution action only |
| Checks technically sufficient but exact human review is applicable and pending | `READY_FOR_HUMAN_REVIEW` | `null` | Human review may be proposed, not performed |
| Exact `INT-DOC-001B` bootstrap candidate passes independent `L2` | `READY_FOR_HUMAN_REVIEW` | `null` | Exact human decision on the hash-bound profile only |
| Technically valid subject still needs external Evidence | `EXTERNAL_EVIDENCE_REQUIRED` | `null` | Separate external Evidence gate only |
| Accepted documentation subject and all applicable validation, human and external gates are closed | `READY_FOR_NEXT_DOCUMENTATION_TASK` | Referenced exact separate record, never generated | A separately authorized next task may be proposed |
| Documentation is sufficient to derive a portable task but target repository is intentionally unbound | `READY_FOR_PORTABLE_TASK_DERIVATION` | Referenced exact separate record if required | Separate task derivation only |
| A target repository decision is missing | `TARGET_REPOSITORY_ASSIGNMENT_REQUIRED` | `null` | Exact human repository-assignment decision |
| Repository exists but exact ref/commit/path binding is missing | `TARGET_BINDING_REQUIRED` | `null` | Separate read-only binding or human decision route |
| Accepted target identity and required contracts permit planning | `READY_FOR_TARGET_BOUND_TASK_BRIEF` | Referenced exact separate record if applicable | `PLAN` only; no execution authority |
| Task Brief and Evidence are decision-ready but implementation permission is absent | `READY_FOR_IMPLEMENTATION_HUMAN_DECISION` | `null` | Exact human implementation decision only |

No readiness state grants execution, implementation, Commit, Push, Merge or
Release permission. Human acceptance does not persist or transition lifecycle
state automatically.

## 11. Validation lifecycle, terminal states and durable owner

Logical lifecycle vocabulary:

```text
TASK_ACTIVE
-> TASK_REPORTED
-> VERIFICATION_PENDING
-> VERIFICATION_RUNNING
-> VERIFIED_PASS
 | VERIFIED_CONTRACT_VIOLATION
 | VERIFIED_FAIL
 | VERIFIED_BLOCKED
 | VERIFIED_UNKNOWN
 | VERIFIED_NOT_RUN
 | VERIFIED_HUMAN_REVIEW_REQUIRED
-> CORRECTION_PENDING
 | HUMAN_REVIEW_PENDING
 | EXTERNAL_EVIDENCE_PENDING
 | NEXT_INTERVAL_PROPOSED
```

Only [planning/CURRENT.md](../CURRENT.md) may be the durable owner of recorded
validation lifecycle state and one recorded `next_bounded_action`. This
contract, R9, Stage Reports, Verification Reports, status views, indexes,
dashboards and chat messages are not competing lifecycle owners.

During a read-only `VALIDATE` run, `VERIFICATION_RUNNING` and its terminal state
are run-local observations. They are not persisted automatically. Durable
recording requires a separate exact `RECORD_VERIFICATION_RESULT` authorization
for an `EXECUTE` run bound to:

- the exact `planning/CURRENT.md` path and current SHA-256;
- exact verification subject and Verification Report identities;
- one declared lifecycle transition;
- default-deny allowed operations and paths.

That recording run may persist the report and atomically update only the
affected lifecycle claims. It may not mutate the validated subject, infer a
human decision, start a next interval or perform Git operations.

### 11.1. Persistence and invalidation boundaries

Validation identity is invalidated by any applicable change to:

- task or interval instance identity;
- task/interval contract revision or bytes;
- Stage Report bytes or SHA-256;
- artifact path set, bytes, SHA-256 or absent marker;
- validation profile revision or bytes;
- authoritative dependency set, owner, revision or accepted human decision;
- verifier identity, version or independence basis;
- relevant repository/worktree/branch/HEAD/index state;
- target binding or other fact used by an affected readiness claim.

Invalidation does not delete history, self-heal, rerun validation, alter a human
decision or mutate `planning/CURRENT.md`. The affected result becomes stale for
the affected claim/action until a new explicit request revalidates a newly
frozen exact subject. Cached results cannot be rebound by inference.

### 11.2. Bounded stale-CURRENT handling

For an active run, the current explicit human decision governs the authorized
scope, while fresh direct repository observation governs mutable repository
facts. If either conflicts with a stored claim in `planning/CURRENT.md`, the
stored claim is a bounded `CONFLICT`; it is not silently treated as current and
is not corrected by the active run.

Read-only validation may continue only for checks whose exact subject,
validation authority/profile and repository identity are independently bound
without relying on the stale claim. Stale CURRENT blocks only:

- durable profile acceptance or activation claims that rely on a CURRENT
  reference;
- durable persistence or current-state claims;
- next-task or next-interval activation;
- any claim that the disputed workflow state is current.

It does not block independently bound read-only inspection or reporting. It
also does not invalidate the exact run-local bootstrap exception in section
3.3 when the current human decision, profile identity, subject, validation task,
repository identity and one-run expiry are independently bound without relying
on the stale CURRENT claim. That exception creates no durable acceptance or
activation claim and cannot be reused. Any mismatch blocks the bootstrap run.
Correcting CURRENT requires a separate authorized persistence-stage `EXECUTE`
action. `VALIDATE` and a correction task whose allowlist excludes CURRENT never
modify it.

Every terminal report affected by stale CURRENT includes:

```yaml
stale_current_finding:
  classification: CONFLICT
  stale_claims: []
  superseding_current_human_decision:
  superseding_direct_observations: []
  affected_actions: []
  unaffected_read_only_checks: []
  resolution_action: HUMAN_AUTHORIZE_BOUNDED_CURRENT_RECONCILIATION
```

The finding supplies no persistence authorization. If exact subject,
authorization or repository binding also cannot be established independently,
the affected validation returns `BLOCKED` and stops.

## 12. Independent L2 cold-start validation

An `L2` verifier must be independent of the authoring agent. Packet binding has
two deterministic phases because the verifier runtime identity does not exist
before its separate invocation:

1. packet assembly produces a dispatchable static template with only the exact
   runtime-bound fields replaced by the literal `RUNTIME_BOUND_REQUIRED`;
2. after the separately human-authorized verifier starts, it binds its exact
   runtime identity, constructs the final packet and passes the packet gate
   before any semantic validation.

The static template is assembly Evidence only. It is not a completed validation
packet, does not consume a validation invocation and grants no authority to
dispatch `VALIDATE`. The final packet is:

```yaml
l2_validation_packet:
  task_identity:
  interval_instance_id:
  candidate:
    path:
    sha256:
  terminal_stage_report:
    path_or_inline_bytes:
      representation: REPOSITORY_RELATIVE_PATH | INLINE_UTF8_BASE64
      value:
    sha256:
  validation_profile:
    profile_id:
    revision:
    path:
    sha256:
    lifecycle_state:
  authoritative_dependency_manifest:
    entries: []
    sha256:
  author_identity:
    agent_run_id:
    role:
    model_binding:
    model:
  verifier_identity:
    agent_run_id:
    role: semantic_reviewer
    model_binding:
    model:
  independence_basis:
    separate_invocation: true
    verifier_stage: VALIDATE
    repository_access: READ_ONLY
    mutation_authorization: NONE
    authoring_scratchpad_access: false
    distinct_agent_run_id_from_author: true
  starting_repository_identity:
    repository_root:
    branch:
    HEAD:
    worktree_status:
    staging_status:
  absent_marker_rule: AOS_ABSENT_SUBJECT_SET_V1
  static_packet_template_sha256:
  final_packet_identity_sha256:
```

Every field shown is required in the final packet. `INLINE_UTF8_BASE64`
contains the exact Stage Report UTF-8 bytes encoded with standard padded
base64; its decoded bytes obey section 4.2. A repository-relative
representation obeys section 4.1. The packet binds the selected profile digest
and dependency manifest produced by sections 4.4 and 4.5.

### 12.1 Static packet template

The static template has the same structure as the final packet except for
these and only these runtime-bound values:

```yaml
verifier_identity:
  agent_run_id: RUNTIME_BOUND_REQUIRED
  role: semantic_reviewer
  model_binding: RUNTIME_BOUND_REQUIRED
  model: RUNTIME_BOUND_REQUIRED
independence_basis:
  distinct_agent_run_id_from_author: RUNTIME_BOUND_REQUIRED
final_packet_identity_sha256: RUNTIME_BOUND_REQUIRED
```

No other field may contain the marker. Construct the static-template manifest
from the template values in this exact order. Status values are represented by
the SHA-256 of their exact UTF-8/LF bytes:

```text
AOS-L2-VALIDATION-PACKET-TEMPLATE-V1<LF>
TASK_ID<TAB><task-identity><LF>
INTERVAL_ID<TAB><interval-instance-id><LF>
CANDIDATE<TAB><normalized-path><TAB><candidate-sha256><LF>
STAGE_REPORT<TAB><representation><TAB><stage-report-sha256><LF>
PROFILE<TAB><profile-id><TAB><revision><TAB><normalized-path><TAB><profile-sha256><TAB><lifecycle-state><LF>
DEPENDENCIES<TAB><authoritative-dependency-set-sha256><LF>
AUTHOR<TAB><agent-run-id><TAB><role><TAB><model-binding><TAB><model-or-NULL><LF>
VERIFIER<TAB>RUNTIME_BOUND_REQUIRED<TAB>semantic_reviewer<TAB>RUNTIME_BOUND_REQUIRED<TAB>RUNTIME_BOUND_REQUIRED<LF>
INDEPENDENCE<TAB>true<TAB>VALIDATE<TAB>READ_ONLY<TAB>NONE<TAB>false<TAB>RUNTIME_BOUND_REQUIRED<LF>
REPOSITORY<TAB><repository-root><TAB><branch><TAB><HEAD><LF>
WORKTREE_STATUS_SHA256<TAB><exact-status-bytes-sha256><LF>
STAGING_STATUS_SHA256<TAB><exact-staging-bytes-sha256><LF>
ABSENT_MARKER<TAB>AOS_ABSENT_SUBJECT_SET_V1<LF>
```

`static_packet_template_sha256` is SHA-256 over exactly these manifest bytes.
The digest is stored outside the manifest and therefore does not hash itself.
Any other placeholder, an omitted required static value or a marker in an
unlisted field makes assembly `BLOCKED`.

### 12.2 Runtime binding and final packet identity

At the start of the separately authorized `VALIDATE` run, before semantic
review, the verifier must perform all of these steps once:

1. record its exact runtime `agent_run_id`, `model_binding` and `model`, retaining
   the static role `semantic_reviewer`;
2. prove its `agent_run_id` differs from the bound author `agent_run_id` and set
   `distinct_agent_run_id_from_author` to the literal boolean `true`;
3. reconstruct the static template from the supplied final static fields using
   the exact marker rules in section 12.1 and require equality with
   `static_packet_template_sha256`;
4. replace every runtime marker with the observed runtime value, construct the
   final manifest below and compute `final_packet_identity_sha256`;
5. require the completed packet to contain no `RUNTIME_BOUND_REQUIRED` marker
   and pass every identity, profile, dependency and independence check;
6. only after that gate passes, begin semantic validation.

The final manifest binds the static template and uses these exact records in
the shown order:

```text
AOS-L2-VALIDATION-PACKET-V1<LF>
STATIC_TEMPLATE_SHA256<TAB><static-packet-template-sha256><LF>
TASK_ID<TAB><task-identity><LF>
INTERVAL_ID<TAB><interval-instance-id><LF>
CANDIDATE<TAB><normalized-path><TAB><candidate-sha256><LF>
STAGE_REPORT<TAB><representation><TAB><stage-report-sha256><LF>
PROFILE<TAB><profile-id><TAB><revision><TAB><normalized-path><TAB><profile-sha256><TAB><lifecycle-state><LF>
DEPENDENCIES<TAB><authoritative-dependency-set-sha256><LF>
AUTHOR<TAB><agent-run-id><TAB><role><TAB><model-binding><TAB><model-or-NULL><LF>
VERIFIER<TAB><agent-run-id><TAB>semantic_reviewer<TAB><model-binding><TAB><model-or-NULL><LF>
INDEPENDENCE<TAB>true<TAB>VALIDATE<TAB>READ_ONLY<TAB>NONE<TAB>false<TAB>true<LF>
REPOSITORY<TAB><repository-root><TAB><branch><TAB><HEAD><LF>
WORKTREE_STATUS_SHA256<TAB><exact-status-bytes-sha256><LF>
STAGING_STATUS_SHA256<TAB><exact-staging-bytes-sha256><LF>
ABSENT_MARKER<TAB>AOS_ABSENT_SUBJECT_SET_V1<LF>
```

All scalar manifest values reject BOM, NUL, CR, LF and TAB. Required final
values cannot be null. The verifier model may be null only as the literal
`NULL`; model difference is supporting Evidence and is not required unless a
separately accepted profile rule says otherwise.
`final_packet_identity_sha256` is SHA-256 over the complete final manifest
bytes. The field is stored outside the manifest and therefore does not hash
itself. Malformed base64, missing bytes, a template or final digest mismatch,
an unresolved marker, ambiguous representation or duplicate identity is
deterministic `BLOCKED`.

Minimum independence acceptance requires every value below exactly:

```yaml
independence_basis:
  separate_invocation: true
  verifier_stage: VALIDATE
  repository_access: READ_ONLY
  mutation_authorization: NONE
  authoring_scratchpad_access: false
  distinct_agent_run_id_from_author: true
```

The author and verifier `agent_run_id` values must differ. The verifier receives
no authoring scratchpad or chat summary. A different model may strengthen
Evidence but is not mandatory without a separately accepted rule.

No chat summary is supplied or required. From that packet, the verifier must:

- state the subject's purpose, scope, non-goals and authority boundary;
- identify every applicable profile, check and terminal outcome route;
- identify missing human decisions, external Evidence and material unknowns;
- derive acceptance and negative scenarios where the subject type requires it;
- identify one next bounded action or exact blocker;
- avoid inferred target repository, product, architecture, acceptance or
  authorization facts;
- demonstrate that an agent can execute the contract without hidden context.

For this bootstrap, the verifier uses
`BOOTSTRAP_INLINE_R9_PROFILE_VALIDATION`, not `POST_STOP_DOCUMENTATION`. A
candidate profile cannot supply the authority for its own validation or
activation.

Missing, malformed, ambiguous or mismatched required packet content produces:

```yaml
task_id:
stage: VALIDATE
result: BLOCKED
starting_identity:
ending_identity:
changed_paths: []
checks_run: []
checks_not_run: []
findings: []
limitations: []
unknowns: []
out_of_scope_state: []
authorization_consumed: false
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: HUMAN_RESOLVE_VALIDATION_PACKET
stop: true
documentation_validation_extension:
  readiness: NOT_READY
  affected_action: COMPLETE_EXACT_FREEZE_AND_INDEPENDENCE_BINDING
  repository_mutations: 0
```

Runtime binding under sections 12.1–12.2 is the required construction of the
originally supplied static template, not packet repair or discretionary
rebinding. A failed binding or packet gate terminates the run. No inference,
repair, alternate binding, automatic retry or alternate-verifier dispatch is
allowed inside `VALIDATE`.

## 13. Default-deny authorization

Authorization defaults to denial unless an exact current human authorization
record is active and bound to the exact task, subject, stage, operation, path,
identity, time and consumption state.

```yaml
authorization_default: DENY_UNLESS_EXACT_ACTIVE_RECORD
validate_repository_mutation: FORBIDDEN
report_persistence_without_separate_EXECUTE: FORBIDDEN
correction_without_separate_EXECUTE: FORBIDDEN
human_decision_creation_by_agent: FORBIDDEN
implementation_authorization: NONE
git_authorization: NONE
automatic_validate_dispatch: FORBIDDEN
automatic_next_interval_start: FORBIDDEN
```

Acceptance, activation, `PASS`, readiness, Evidence, repository presence,
historical status, task planning and a previous authorization do not carry
permission into a new action. Commit, Push, Merge and Release each require a
separate explicit human decision for the exact action and subject.

## 14. Correction after canonical VALIDATE

Canonical `VALIDATE` detects, classifies, reports and stops. It never corrects
the subject.

A correction may occur only in a new separately authorized `EXECUTE` run bound
to all of:

```yaml
correction_authorization_binding:
  exact_subject_paths: []
  exact_subject_sha256_or_absent_marker:
  exact_stage_report_sha256:
  exact_verification_report_identity:
  finding_ids: []
  allowed_paths: []
  allowed_operations: []
  one_shot: true
  status: ACTIVE
```

Preauthorization is absent by default. One mechanically unique correction
attempt may be preauthorized only by an exact human decision. Semantic,
product, architecture, authority, human-decision, implementation and Git
changes always require a new explicit human authorization.

The correction route is:

```text
VALIDATE finding
-> terminal Verification Report
-> STOP
-> separate explicit correction authorization
-> new EXECUTE correction run
-> internal self-check
-> bounded correction only within exact authorization
-> repeated self-check after any correction
-> new candidate freeze
-> terminal Stage Report
-> STOP
-> separate explicit new VALIDATE request
```

There is no automatic correction, retry, re-entry, stage transition, dispatcher,
recursive repair or autonomous loop. A failed correction returns a terminal
Stage Report and stops. It never expands scope or retries itself.

## 15. Candidate freeze and internal authoring self-check

Before an authoring `EXECUTE` Stage Report may declare a final candidate frozen,
the writer verifies:

1. expected outputs exist at exact declared paths;
2. changed paths are limited to the authorized allowlist;
3. Markdown, YAML, IDs, fences and relative links are structurally valid;
4. the subject is semantically complete and internally consistent;
5. claims follow source precedence and owner boundaries;
6. traceability and downstream agent usability are complete;
7. technical result, readiness and human decision remain separate;
8. no acceptance, authorization, implementation or Git action was invented;
9. required checks are not hidden or promoted from `NOT_RUN`;
10. the final candidate identity and external SHA-256 are recorded.

The writer may correct an internal self-check finding only inside the same exact
authorized output scope and declared primary outcome. Every correction requires
a complete repeated self-check. Freeze occurs only after the final complete
check passes. A finding requiring scope expansion or a new human, product,
architecture or authority decision yields `BLOCKED`, a terminal Stage Report
and `STOP`.

Internal self-check is authoring quality control. It is not independent Evidence
and cannot replace the mandatory independent post-stop `VALIDATE` run.

## 16. Required negative cases

These documentation-level cases are mechanically reviewable contract fixtures;
they do not authorize executable tests or runtime implementation in this
repository.

```yaml
negative_cases:
  - case_id: PSDV-NC-001
    preconditions: [generic Stage Report is required]
    input_or_mutation: malformed or missing mandatory generic Stage Report field
    expected_result: FAIL
    expected_readiness: NOT_READY
    expected_authorization_state: UNCHANGED
    expected_repository_mutations: 0
    affected_action: VALIDATE_STAGE_REPORT
    next_required_action: HUMAN_PROVIDE_CONFORMING_STAGE_REPORT
    stop: true

  - case_id: PSDV-NC-002
    preconditions: [specialized report is supplied]
    input_or_mutation: specialized report lacks lossless generic-field mapping
    expected_result: FAIL
    expected_readiness: NOT_READY
    expected_authorization_state: UNCHANGED
    expected_repository_mutations: 0
    affected_action: ACCEPT_SPECIALIZED_REPORT
    next_required_action: HUMAN_AUTHORIZE_REPORT_SCHEMA_CORRECTION
    stop: true

  - case_id: PSDV-NC-003
    preconditions: [zero-write check is required]
    input_or_mutation: zero_write_evidence object is absent
    expected_result: FAIL
    expected_readiness: NOT_READY
    expected_authorization_state: UNCHANGED
    expected_repository_mutations: 0
    affected_action: CLAIM_ZERO_WRITE_PASS
    next_required_action: HUMAN_PROVIDE_COMPLETE_VALIDATION_PACKET
    stop: true

  - case_id: PSDV-NC-004
    preconditions: [zero_write_evidence object exists]
    input_or_mutation: before or after repository or subject identity is incomplete
    expected_result: UNKNOWN
    expected_readiness: NOT_READY
    expected_authorization_state: UNCHANGED
    expected_repository_mutations: 0
    affected_action: COMPLETE_ZERO_WRITE_COMPARISON
    next_required_action: HUMAN_RESOLVE_MISSING_ZERO_WRITE_EVIDENCE
    stop: true

  - case_id: PSDV-NC-005
    preconditions: [VALIDATE is running read-only]
    input_or_mutation: validator changes repository content, index, ref or Git state
    expected_result: CONTRACT_VIOLATION
    expected_readiness: NOT_READY
    expected_authorization_state: INVALIDATED
    expected_repository_mutations: GREATER_THAN_ZERO_DETECTED
    affected_action: CONTINUE_VALIDATION
    next_required_action: HUMAN_REVIEW_VALIDATION_MUTATION
    stop: true

  - case_id: PSDV-NC-006
    preconditions: [candidate was frozen]
    input_or_mutation: candidate path or exact bytes differ from the packet identity
    expected_result: FAIL
    expected_readiness: NOT_READY
    expected_authorization_state: INVALIDATED
    expected_repository_mutations: 0
    affected_action: VALIDATE_FROZEN_CANDIDATE
    next_required_action: HUMAN_RESOLVE_CANDIDATE_DRIFT
    stop: true

  - case_id: PSDV-NC-007
    preconditions: [dependency manifest was bound]
    input_or_mutation: an authoritative dependency path or digest differs
    expected_result: FAIL
    expected_readiness: NOT_READY
    expected_authorization_state: INVALIDATED
    expected_repository_mutations: 0
    affected_action: VALIDATE_AGAINST_DEPENDENCIES
    next_required_action: HUMAN_RESOLVE_DEPENDENCY_DRIFT
    stop: true

  - case_id: PSDV-NC-008
    preconditions: [validation profile identity was bound]
    input_or_mutation: computed validation-profile digest mismatches the packet
    expected_result: FAIL
    expected_readiness: NOT_READY
    expected_authorization_state: INVALIDATED
    expected_repository_mutations: 0
    affected_action: APPLY_VALIDATION_PROFILE
    next_required_action: HUMAN_RESOLVE_PROFILE_IDENTITY
    stop: true

  - case_id: PSDV-NC-009
    preconditions: [identity manifest is being constructed]
    input_or_mutation: two entries normalize to the same repository path
    expected_result: FAIL
    expected_readiness: NOT_READY
    expected_authorization_state: UNCHANGED
    expected_repository_mutations: 0
    affected_action: CONSTRUCT_IDENTITY_MANIFEST
    next_required_action: HUMAN_RESOLVE_DUPLICATE_PATH
    stop: true

  - case_id: PSDV-NC-010
    preconditions: [identity manifest is being constructed]
    input_or_mutation: path is absolute, non-normalized or contains a forbidden component
    expected_result: FAIL
    expected_readiness: NOT_READY
    expected_authorization_state: UNCHANGED
    expected_repository_mutations: 0
    affected_action: CONSTRUCT_IDENTITY_MANIFEST
    next_required_action: HUMAN_RESOLVE_INVALID_PATH_IDENTITY
    stop: true

  - case_id: PSDV-NC-011
    preconditions: [profile does not explicitly allow symlinks]
    input_or_mutation: subject or dependency path is an unexpected symlink
    expected_result: BLOCKED
    expected_readiness: NOT_READY
    expected_authorization_state: INVALIDATED
    expected_repository_mutations: 0
    affected_action: BIND_SYMLINKED_SUBJECT
    next_required_action: HUMAN_RESOLVE_SYMLINK_BOUNDARY
    stop: true

  - case_id: PSDV-NC-012
    preconditions: [L2 packet is required]
    input_or_mutation: Stage Report exact bytes or digest is missing
    expected_result: BLOCKED
    expected_readiness: NOT_READY
    expected_authorization_state: UNCHANGED
    expected_repository_mutations: 0
    affected_action: COMPLETE_EXACT_FREEZE_BINDING
    next_required_action: HUMAN_RESOLVE_VALIDATION_PACKET
    stop: true

  - case_id: PSDV-NC-013
    preconditions: [L2 independence is required]
    input_or_mutation: author identity or author agent_run_id is missing
    expected_result: BLOCKED
    expected_readiness: NOT_READY
    expected_authorization_state: UNCHANGED
    expected_repository_mutations: 0
    affected_action: ESTABLISH_VERIFIER_INDEPENDENCE
    next_required_action: HUMAN_RESOLVE_VALIDATION_PACKET
    stop: true

  - case_id: PSDV-NC-014
    preconditions: [author and verifier identities are present]
    input_or_mutation: author and verifier agent_run_id values are equal
    expected_result: BLOCKED
    expected_readiness: NOT_READY
    expected_authorization_state: INVALIDATED
    expected_repository_mutations: 0
    affected_action: CLAIM_INDEPENDENT_L2_VALIDATION
    next_required_action: HUMAN_RESOLVE_VERIFIER_INDEPENDENCE
    stop: true

  - case_id: PSDV-NC-015
    preconditions: [verifier identity is present]
    input_or_mutation: verifier has repository mutation authorization
    expected_result: BLOCKED
    expected_readiness: NOT_READY
    expected_authorization_state: INVALIDATED
    expected_repository_mutations: 0
    affected_action: START_READ_ONLY_VALIDATE
    next_required_action: HUMAN_RESOLVE_VERIFIER_AUTHORITY
    stop: true

  - case_id: PSDV-NC-016
    preconditions: [required before and after observations are available]
    input_or_mutation: required comparison is not executed
    expected_result: NOT_RUN
    expected_readiness: NOT_READY
    expected_authorization_state: UNCHANGED
    expected_repository_mutations: 0
    affected_action: CLAIM_REQUIRED_CHECK_PASS
    next_required_action: HUMAN_RESOLVE_REQUIRED_NOT_RUN
    stop: true

  - case_id: PSDV-NC-017
    preconditions: [planning/CURRENT.md contains a bounded stale claim]
    input_or_mutation: validator attempts a durable persistence or current-state claim
    expected_result: BLOCKED
    expected_readiness: NOT_READY
    expected_authorization_state: DENY_PERSISTENCE
    expected_repository_mutations: 0
    affected_action: PERSIST_VALIDATION_OR_CURRENT_STATE
    next_required_action: HUMAN_AUTHORIZE_BOUNDED_CURRENT_RECONCILIATION
    stop: true

  - case_id: PSDV-NC-018
    preconditions: [profile file exists]
    input_or_mutation: repository presence is treated as acceptance or activation
    expected_result: BLOCKED
    expected_readiness: NOT_READY
    expected_authorization_state: DENY_PROFILE_USE
    expected_repository_mutations: 0
    affected_action: APPLY_UNACTIVATED_PROFILE
    next_required_action: HUMAN_RESOLVE_PROFILE_LIFECYCLE
    stop: true

  - case_id: PSDV-NC-019
    preconditions: [validation result is PASS]
    input_or_mutation: PASS is treated as human acceptance or authorization
    expected_result: CONTRACT_VIOLATION
    expected_readiness: NOT_READY
    expected_authorization_state: DENY_AUTHORITY_ESCALATION
    expected_repository_mutations: 0
    affected_action: CREATE_HUMAN_DECISION_OR_AUTHORITY
    next_required_action: HUMAN_REVIEW_AUTHORITY_VIOLATION
    stop: true

  - case_id: PSDV-NC-020
    preconditions: [VALIDATE packet is missing, stale or mismatched]
    input_or_mutation: validator repairs, rebinds or retries the packet or subject
    expected_result: CONTRACT_VIOLATION
    expected_readiness: NOT_READY
    expected_authorization_state: INVALIDATED
    expected_repository_mutations: 0
    affected_action: CONTINUE_OR_RETRY_VALIDATION
    next_required_action: HUMAN_RESOLVE_VALIDATION_PACKET
    stop: true

  - case_id: PSDV-NC-021
    preconditions: [static packet template is supplied to a new VALIDATE run]
    input_or_mutation: exact verifier runtime identity is unavailable at the binding gate
    expected_result: BLOCKED
    expected_readiness: NOT_READY
    expected_authorization_state: VALIDATE_READ_ONLY_ACTIVE
    expected_repository_mutations: 0
    affected_action: CLAIM_COMPLETE_L2_PACKET_OR_BEGIN_SEMANTIC_VALIDATION
    next_required_action: HUMAN_RESOLVE_EXACT_VERIFIER_RUNTIME_IDENTITY
    stop: true

  - case_id: PSDV-NC-022
    preconditions: [static packet template and its claimed digest are supplied]
    input_or_mutation: reconstructed static-template digest differs from static_packet_template_sha256
    expected_result: BLOCKED
    expected_readiness: NOT_READY
    expected_authorization_state: VALIDATE_READ_ONLY_ACTIVE
    expected_repository_mutations: 0
    affected_action: COMPLETE_EXACT_FREEZE_AND_INDEPENDENCE_BINDING
    next_required_action: HUMAN_RESOLVE_VALIDATION_PACKET
    stop: true

  - case_id: PSDV-NC-023
    preconditions: [runtime binding is attempted]
    input_or_mutation: final packet retains RUNTIME_BOUND_REQUIRED or claims a final digest before exact binding
    expected_result: BLOCKED
    expected_readiness: NOT_READY
    expected_authorization_state: VALIDATE_READ_ONLY_ACTIVE
    expected_repository_mutations: 0
    affected_action: BEGIN_SEMANTIC_VALIDATION
    next_required_action: HUMAN_RESOLVE_VALIDATION_PACKET
    stop: true

  - case_id: PSDV-NC-024
    preconditions: [an inline human decision is a required authoritative dependency]
    input_or_mutation: runtime turn ID or exact whole-message byte selector is missing, duplicated or ambiguous
    expected_result: BLOCKED
    expected_readiness: NOT_READY
    expected_authorization_state: UNCHANGED
    expected_repository_mutations: 0
    affected_action: CONSTRUCT_AUTHORITATIVE_DEPENDENCY_MANIFEST
    next_required_action: HUMAN_COMPLETE_OR_RESOLVE_EXACT_VALIDATION_INPUT
    stop: true
```

## 17. Correction traceability and freeze gate

The correction input findings are `REPORTED` review Evidence adopted by the
current explicit human decision. They do not become a competing authority owner.
Earlier workflow-automation proposals remain `PROPOSAL`, have operative effect
`NONE` and are outside this correction. No proposal term is incorporated here.

| Finding | Exact correction location | Required closure |
|---|---|---|
| `INT-DOC-001B-VF-002` | Sections 6 and 8 | Generic Stage Report fields preserved; specialized mapping additive and lossless |
| `INT-DOC-001B-VF-003` | Sections 5 and 8 | Complete mandatory `zero_write_evidence` embedded in the Verification Report |
| `INT-DOC-001B-VF-004` | Sections 4.1–4.5 and 12 | Exact byte, path, manifest, absent-marker and SHA-256 algorithms |
| `INT-DOC-001B-VF-005` | Section 3.3 | Closed profile lifecycle, decision records and CURRENT reference boundary |
| `INT-DOC-001B-VF-006` | Section 12 | Complete L2 packet, deterministic packet identity and minimum independence rule |
| `INT-DOC-001B-VF-007` | Section 11.2 | Bounded stale-CURRENT conflict and separately authorized persistence route |
| `INT-DOC-001B-L2-RUNTIME-BINDING-CYCLE-001` | Sections 12.1–12.2 and cases `PSDV-NC-021`–`023` | Dispatchable static template and exact runtime-bound finalization before semantic validation |
| `INT-DOC-001B-L2-DEPENDENCY-LOCATOR-001` | Section 4.5 and case `PSDV-NC-024` | Closed inline-decision locator and exact runtime-message byte boundary |
| `INT-DOC-001B-VF-005-R3-001` | Sections 3.3 and 11.2 | One-run non-durable external bootstrap binding without a competing CURRENT owner |
| `INT-DOC-001B-L2-DEPENDENCY-LOCATOR-R4-001` | Section 4.5 and case `PSDV-NC-024` | Runtime-turn locator removes all embedded `decision_id` fields from locator competition |
| `INT-DOC-001B-L2-DEPENDENCY-SELECTOR-PARSER-001` | Section 4.5 and case `PSDV-NC-024` | Runtime message locator uses only exact turn identity and never parses Markdown or embedded records |

Before final freeze, the correction writer checks every row above and also
verifies:

- generic Stage Report compatibility and exact field case;
- complete before/after zero-write identity;
- parseable YAML examples, balanced Markdown fences and resolving relative links;
- all twenty-four negative cases use the required schema;
- CURRENT remains the sole durable current-state owner and is unchanged;
- the candidate remains `DRAFT` and claims no acceptance or activation;
- no task-wide multi-stage authorization construct was introduced;
- `automatic_validate_dispatch: FORBIDDEN` remains explicit;
- no automatic correction, retry, next task/interval or Git path was added;
- only this exact candidate changed and staging remains empty;
- `git diff --check` passes.

Any failed required check prevents freeze. Refinement is allowed only before
freeze, inside this exact candidate and under the same consumed one-shot
correction authorization. After freeze, no candidate byte changes are allowed.

## 18. Bootstrap closure for INT-DOC-001B

This exact R6 corrected candidate remains `DRAFT` and inactive after its
terminal Stage Report. If its bounded correction Stage Report result is `PASS`,
the one required next action is:

```text
INDEPENDENT_L2_VALIDATE_EXACT_CORRECTED_INT_DOC_001B_OUTPUT
```

That action is not dispatched by this contract. It requires a separate manual
new invocation using canonical stage `VALIDATE`, profile
`BOOTSTRAP_INLINE_R9_PROFILE_VALIDATION`, the complete packet from section 12,
an independent verifier and the zero-write invariant. It returns one
Verification Report and stops. Human acceptance, profile activation, durable
persistence, any further correction, the next interval, implementation and all
Git operations remain separate and `NOT_RUN`.
