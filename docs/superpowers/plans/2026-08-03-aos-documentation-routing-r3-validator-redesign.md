# AOS Documentation Routing R3 Validator Result-Sealing Redesign Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use
> `superpowers:test-driven-development` while implementing each code task and
> `superpowers:verification-before-completion` before any completion claim.

**Goal:** Remove the repeated R3 validator/checker loop by preserving exact
request-to-result identity while eliminating reviewer-side reconstruction of
the nested `exact_subject` and `source_boundary` objects.

**Architecture:** A versioned V2 review request keeps the complete subject,
source, method, authority, and stop context, but separates stable echo fields
from request-only context. The deterministic harness computes a canonical
`request_sha256` and an immutable result-binding projection. A new read-only
`seal-result` command consumes the exact bound request plus a reviewer-authored
evidence body on standard input, copies all required binding fields from the
request, validates the evidence body, and emits the complete canonical reviewer
result. The reviewer returns those exact emitted bytes. The primary validates
the sealed result and never fills, repairs, or infers reviewer Evidence.

**Tech Stack:** Python 3.9.6 standard library, `unittest`, canonical compact
JSON, SHA-256, UTF-8/LF, stdin/stdout transport, Codex strict configuration
parser, read-only Git inspection.

## 1. Authority, status, and exact plan boundary

- Repository: `/Users/muhammed/Documents/GitHub/notebook`.
- Repository role remains `ACTIVE_PROJECT_KNOWLEDGE_REPOSITORY`; AOS product
  runtime code remains forbidden here.
- Observed branch at plan preflight: `dev`.
- Observed `HEAD` at plan preflight:
  `d733eeb037a517634ecc37e8b19c8421c2d20530`.
- Selected human decision visible-text SHA-256:
  `6d8dfeafd539cac6b58e1f8040b7821ab4ec829484ecc04a0b7f22bb8c71717f`
  over 267 UTF-8 bytes.
- Selected recovery-plan candidate:
  `docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-harness-recovery.md`,
  39,623 bytes, SHA-256
  `363be3287cb46efeacd9947b07460edb463d39f41bbf244b98763f1e75e47b21`.
- Exact PLAN authorization visible-text SHA-256:
  `bef47482cd2971a8414fb5750d0a706b595cd7f7a0b2ce25170410e47bcdd972`
  over 578 UTF-8 bytes.
- This PLAN authorization permits mutation of only this plan path. It does not
  authorize implementation, package correction, independent `VALIDATE`, safe
  pilot, acceptance, activation, Commit, Push, Merge, or Release.
- `planning/CURRENT.md` remains the sole lifecycle owner and is not modified by
  this plan.
- The R3 routing package remains pilot-only `DRAFT_CANDIDATE`. It is not active,
  is not accepted for mass documentation authoring, and cannot govern ordinary
  documentation runs.
- Existing dirty-worktree paths are pre-existing state and must be preserved.

## 2. Reported failure and observed executable root cause

### 2.1 Repeated failure sequence

The prior terminal gate Evidence reports two distinct failures; the original
request/result raw bytes are not repository artifacts and are not independently
replayed by this PLAN:

1. A mechanical request used a checker assertion that reported 50 Markdown
   fence delimiters while direct current-byte observation found 54. The primary
   correctly classified this as `REQUEST_OR_CHECKER_DEFECT`, preserved the
   candidate, and used the one authorized validator correction.
2. The fresh mechanical request bound the corrected current plan and added two
   request-context fields under `exact_subject`:
   `correction_authorization_visible_text_byte_length` and
   `correction_authorization_visible_text_sha256`. The reviewer checked the
   current plan but omitted those two fields when recreating `exact_subject` in
   its result. Current `check-result` therefore returned
   `CONTRACT_VIOLATION/NONE` with message
   `reviewer result exact_subject does not match request`.

The contract reviewer passed the same current plan bytes. The semantic gate was
correctly left `NOT_RUN` because required mechanical Evidence was non-PASS. The
candidate bytes were not the cause of the repeated finding.

### 2.2 Structural cause

Current-byte inspection confirms that `tools/routing_r3_harness.py` requires
both request and result to carry
the full `exact_subject` and `source_boundary`, then compares those values for
deep equality. The reviewer must manually reproduce an open-ended nested object
whose fields grow when correction, authorization, transport, or provenance
metadata is added. Current tests use a one-element list as `exact_subject` and
manually copy it into `valid_result()`, so they do not exercise the real
nested-envelope failure mode.

The defect is therefore at the request/result transport boundary:

```text
rich request context
-> reviewer manually reconstructs identity-bearing result fields
-> one omitted non-semantic metadata field
-> contract-invalid Evidence
-> validator correction budget consumed
-> repeated REQUEST_OR_CHECKER_DEFECT
-> DEFER_OR_REDESIGN_VALIDATOR
```

The redesign must not weaken subject binding, accept partial Evidence, hide a
missing field, retry a reviewer, or let the primary complete reviewer claims.
It must remove manual reconstruction from the valid path.

## 3. Selected validator architecture

### 3.1 Closed V2 request layers

Every new R3 reviewer request uses
`request_schema: ROUTING_R3_REVIEW_REQUEST_V2` and has three explicit layers:

1. **Stable result-binding fields** — the fields that every complete reviewer
   result must report:

   ```text
   task_id
   request_id
   parent_task_id
   task_class
   role
   exact_subject
   subject_sha256
   source_boundary
   ```

2. **Request-only bound context** — exact subject members, source members,
   human-decision references, finding IDs, Stage Report identity,
   `invariant_semantics`, `method_contract`, required output fields, stop
   conditions, `observation_contract`, `result_transport_contract`,
   allowed/forbidden operations, and retry limit. This context is included in
   `request_sha256` but is not manually echoed field-by-field in the result.
   `observation_contract` binds the repository root and exact raw-byte carrier
   used by both request and result checks. `result_transport_contract` is
   required for every reviewer role and binds the preflight-observed
   `seal-result` capability, exact command, expected canonical success object,
   and forbidden substitutions.
3. **Deterministic binding projection** — a harness-produced closed object
   containing the eight stable fields plus `request_sha256`. Its canonical
   digest is `result_binding_sha256`.

`exact_subject` becomes a closed stable reference, never an open container for
task chronology or authorization metadata:

```json
{
  "byte_length": 39623,
  "locator": "docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-harness-recovery.md",
  "schema": "ROUTING_R3_EXACT_SUBJECT_REFERENCE_V1",
  "subject_kind": "SINGLE_REGULAR_FILE",
  "subject_sha256": "363be3287cb46efeacd9947b07460edb463d39f41bbf244b98763f1e75e47b21"
}
```

For a multi-file subject, `locator` is the exact manifest identity, the object
uses `subject_kind: SUBJECT_SET_MANIFEST`, and it carries exact member count,
manifest byte length, and manifest SHA-256. The complete ordered member records
remain in request-only `subject_members`. `check-request` recomputes the stable
reference from those records. Unknown keys in the stable reference are a
request contract defect; human-decision or correction metadata belongs only in
`request_context`.

`source_boundary` follows the same rule:

```yaml
manifest_byte_length: POSITIVE_INTEGER
manifest_sha256: SHA256
member_count: POSITIVE_INTEGER
schema: ROUTING_R3_SOURCE_BOUNDARY_REFERENCE_V1
```

The canonical source-boundary manifest is exact:

```text
AOS-R3-SOURCE-BOUNDARY-MANIFEST-V1<LF>
<kind><TAB><locator><TAB><raw-source-byte-length><TAB><raw-source-sha256><LF>
```

Allowed `kind` values are `FILE`, `INLINE_DECISION`, `INLINE_EVIDENCE`, and
`REFERENCE`. `FILE` locators use normalized repository-relative paths.
`INLINE_DECISION` uses `RUNTIME_TURN_ID:<exact-runtime-turn-id>`.
`INLINE_EVIDENCE` uses
`REQUEST_ID:<exact-request-id>#<REQUEST|RESULT|GATE|REGISTRY>`. `REFERENCE` uses the
closed locator `<repository-url>@<exact-commit>:<normalized-path>` and requires
the exact referenced bytes; unavailable bytes block with
`BLOCKED_REFERENCE_ACCESS` before a boundary digest is produced. Records are
sorted by the UTF-8 bytes of `<kind><TAB><locator>`. Duplicate kind/locator pairs, unknown
kinds, control bytes, unavailable source bytes, zero members, stale lengths, or
digest mismatch fail before dispatch.

### 3.1.1 Normative V2 JSON domains and closed schemas

All V2 objects are closed: a key not listed by the selected schema is invalid.
JSON `null`, floats, non-finite numbers, duplicate keys, lone surrogates, and
non-UTF-8 input are forbidden everywhere unless a field below explicitly says
otherwise. Scalar domains are:

```text
EXACT_STRING = non-empty JSON string whose value equals value.strip()
SHA256 = EXACT_STRING matching [0-9a-f]{64}
POSITIVE_INTEGER = JSON integer >= 1, excluding booleans
NONNEGATIVE_INTEGER = JSON integer >= 0, excluding booleans
EXACT_STRING_LIST = JSON array of unique EXACT_STRING values
NONEMPTY_EXACT_STRING_LIST = EXACT_STRING_LIST with length >= 1
JSON_BOOLEAN = literal JSON true or false
NORMALIZED_PATH = EXACT_STRING satisfying the R6 repository-relative POSIX path rules
ABSOLUTE_NORMALIZED_PATH = EXACT_STRING satisfying the absolute-path rules below
TECHNICAL_RESULT = PASS | FAIL | BLOCKED | CONFLICT | UNKNOWN | NOT_RUN | CONTRACT_VIOLATION
CLAIM_CLASS = OBSERVED_AT_SNAPSHOT | REPORTED | SYNTHESIZED | CONFLICT | NOT_FOUND | UNKNOWN | NOT_RUN | BLOCKED
```

The exact base request key set is:

```text
request_schema
request_sha256
task_id
execution_id
request_id
parent_task_id
task_class
role
exact_subject
subject_sha256
subject_members
source_boundary
source_boundary_members
request_context
observation_contract
result_transport_contract
required_output_fields
stop_conditions
allowed_operations
forbidden_operations
retry_limit
```

Every listed key is required. `request_schema` equals
`ROUTING_R3_REVIEW_REQUEST_V2`. Task, execution, request, and parent IDs, task
class, and role are `EXACT_STRING`;
role is one configured reviewer role. `subject_sha256` is `SHA256` and equals
the digest in `exact_subject`. `allowed_operations` equals `['READ']` in that
order. `forbidden_operations` contains exactly `WRITE`, `COMMIT`, `PUSH`,
`MERGE`, `RELEASE`, and `NESTED_DELEGATION`, each once. `retry_limit` is integer
zero. `stop_conditions` is a non-empty `EXACT_STRING_LIST`.

A mechanical request adds exactly `invariant_semantics` and `method_contract`.
`invariant_semantics` is a non-empty closed mapping whose keys are declared
invariant IDs and whose values are `EXACT_STRING`. `method_contract` has exactly
`preflight_observed_capability: EXACT_STRING`,
`exact_algorithm_or_command: EXACT_STRING`,
`expected_success_shape: EXACT_STRING`, and
`forbidden_substitutions: non-empty EXACT_STRING_LIST`. Non-mechanical roles
omit both keys unless the exact request declares a deterministic invariant; in
that case they use the same two-field extension and validation.

`subject_members` is a non-empty array of this exact record, ordered by path
UTF-8 bytes with no duplicate path:

```yaml
kind: FILE
path: NORMALIZED_PATH
byte_length: NONNEGATIVE_INTEGER
sha256: SHA256
```

Zero byte length is permitted only for a directly observed empty regular file.
Symlinks and non-regular files are forbidden. A single-file `exact_subject` has
exactly the five keys shown in section 3.1, requires exactly one member, and
must equal that member's path, byte length, and digest. A subject-set reference
has exactly:

```yaml
schema: ROUTING_R3_EXACT_SUBJECT_REFERENCE_V1
subject_kind: SUBJECT_SET_MANIFEST
locator: AOS-SUBJECT-SET-MANIFEST-V1
member_count: POSITIVE_INTEGER
manifest_byte_length: POSITIVE_INTEGER
manifest_sha256: SHA256
subject_sha256: SHA256
```

For a set, `member_count` equals the array length; manifest bytes use R6 section
4.3 exactly; `manifest_sha256` and `subject_sha256` both equal the digest of
those bytes.

`source_boundary_members` is a non-empty array ordered by UTF-8 bytes of
`<kind><TAB><locator>`, with no duplicate pair. Each record has exactly:

```yaml
kind: FILE | INLINE_DECISION | INLINE_EVIDENCE | REFERENCE
locator: EXACT_STRING
byte_length: NONNEGATIVE_INTEGER
sha256: SHA256
claim_class: CLAIM_CLASS
```

`FILE` locators additionally satisfy `NORMALIZED_PATH`; other locator grammars
are exactly those in section 3.1. Zero length is allowed only for directly
observed empty source bytes. `source_boundary` has exactly `schema`,
`member_count`, `manifest_byte_length`, and `manifest_sha256`, with the domains
in section 3.1; all values are recomputed from the member array and the exact
manifest algorithm.

`request_context` is an array, possibly empty, ordered by UTF-8 bytes of
`<context_kind><TAB><locator>` without duplicates. Each record has exactly:

```yaml
context_kind: AUTHORIZATION | DECISION | FINDING_SET | STAGE_REPORT | UPSTREAM_RESULT | UPSTREAM_GATE | TASK_METADATA
locator: EXACT_STRING
byte_length: NONNEGATIVE_INTEGER
sha256: SHA256
claim_class: REPORTED | OBSERVED_AT_SNAPSHOT
```

The referenced raw bytes must be present in `source_boundary_members` under a
compatible locator and identity. Context therefore grows by adding closed
records, never by adding keys to `exact_subject` or `source_boundary`.

`observation_contract` has exactly:

```yaml
schema: ROUTING_R3_RAW_BYTE_OBSERVATION_CONTRACT_V1
repository_root: ABSOLUTE_NORMALIZED_PATH
task_local_root: ABSOLUTE_NORMALIZED_PATH
source_blob_map_path: NORMALIZED_PATH
source_blob_map_byte_length: POSITIVE_INTEGER
source_blob_map_sha256: SHA256
reread_policy: CHECK_REQUEST_AND_CHECK_RESULT
reviewer_access: READ_ONLY_UNTIL_TERMINAL_RESULT_IS_CHECKED
```

`ABSOLUTE_NORMALIZED_PATH` is an absolute POSIX path with no control bytes,
dot segment, dot-dot segment, duplicate separator, trailing separator, or
ambiguous Unicode normalization. The controller supplies one canonical
`task_local_root` outside the repository and binds its exact absolute path in
the request. `source_blob_map_path` is relative to that root and resolves to one
canonical source-blob map. Its compact JSON plus one LF
has exactly `schema: ROUTING_R3_SOURCE_BLOB_MAP_V1` and `records`. `records` is
ordered by UTF-8 bytes of `<kind><TAB><locator>`, contains exactly one record for
every non-`FILE` source-boundary member and no other record, and each record has
exactly `kind`, `locator`, `blob_path`, `byte_length`, and `sha256`.
`blob_path` is a `NORMALIZED_PATH` relative to the exact `task_local_root`.
Neither the map nor a blob path may equal or contain another record's path, and
all must resolve through the descriptor-safe algorithm below without leaving
that root. The map's raw length and digest must equal the two bound fields
above. An empty non-`FILE` set uses a valid map with an empty `records` array;
it is never represented by a missing map.

The controller creates `task_local_root` with an exclusive temporary-directory
primitive before it authors the request. It materializes the exact request,
source map, and non-`FILE` source blobs as distinct new regular files, rereads
and binds their lengths and SHA-256 values, and grants the configured reviewer
read-only access to the exact repository root and task-local root. The request
file path, `task_local_root`, `source_blob_map_path`, and every relative
`blob_path` are delivered without retyping. These files remain readable and
immutable until the reviewer terminates and the primary completes
`check-result` and gate normalization. Only then may the controller remove the
task-local root. A reviewer that cannot read an exact `REFERENCE` blob returns
`BLOCKED/BLOCKED_REFERENCE_ACCESS`; inability to read any other bound blob
returns `BLOCKED/BLOCKED_SCOPE_OR_PROVENANCE`. No chat reconstruction, digest-
only substitute, or primary-authored review Evidence is allowed.

`result_transport_contract` has exactly:

```yaml
schema: ROUTING_R3_RESULT_TRANSPORT_CONTRACT_V1
preflight_observed_capability: EXACT_STRING
command_argv: NONEMPTY_EXACT_STRING_LIST
input_transport: STDIN_SINGLE_UTF8_JSON_OBJECT
expected_success_schema: ROUTING_R3_REVIEW_RESULT_V2
forbidden_substitutions: NONEMPTY_EXACT_STRING_LIST
```

`command_argv` must equal the complete `seal-result` invocation for this exact
request path, embedded-digest verification mode, role, and model; placeholders
and shell fragments are invalid. `required_output_fields` equals the following
exact ordered list:

```text
result_schema, request_sha256, result_binding_sha256,
task_id, request_id, parent_task_id, task_class, role, model, reasoning,
exact_subject, subject_sha256, source_boundary, sources, methods,
temporal_scope, classified_claims, conflicts, unknowns, recommendations,
checks_run, checks_not_run, limitations, model_binding,
repository_mutations, git_operations, result, reason_code,
next_required_action, stop
```

The reviewer-authored evidence-body object has exactly the fields shown in
section 3.3. Its nested record schemas are:

```yaml
source_record: {source_id: EXACT_STRING, kind: FILE | INLINE_DECISION | INLINE_EVIDENCE | REFERENCE, locator: EXACT_STRING, byte_length: NONNEGATIVE_INTEGER, sha256: SHA256, claim_class: CLAIM_CLASS, evidence: EXACT_STRING}
method_record: {method_id: EXACT_STRING, binding_kind: INVARIANT_METHOD_CONTRACT | RESULT_TRANSPORT_CONTRACT | REVIEWER_ANALYSIS, capability: EXACT_STRING, algorithm_or_command: EXACT_STRING, result: TECHNICAL_RESULT, evidence: EXACT_STRING}
claim_record: {claim_id: EXACT_STRING, claim_class: CLAIM_CLASS, statement: EXACT_STRING, source_ids: EXACT_STRING_LIST}
conflict_record: {conflict_id: EXACT_STRING, claim_class: CONFLICT, statement: EXACT_STRING, source_ids: EXACT_STRING_LIST, material: JSON_BOOLEAN}
unknown_record: {unknown_id: EXACT_STRING, claim_class: UNKNOWN | NOT_RUN | BLOCKED, statement: EXACT_STRING}
recommendation_record: {recommendation_id: EXACT_STRING, claim_class: SYNTHESIZED, action: EXACT_STRING}
```

`sources`, `methods`, and `classified_claims` are non-empty arrays of their
records with unique local IDs. `conflicts`, `unknowns`, and `recommendations`
are arrays of their records and may be empty. `checks_run`, `checks_not_run`,
and `limitations` are `EXACT_STRING_LIST` and may be empty. `temporal_scope`
uses the current exact scalar grammar. `model` and `reasoning` are exact static
role-binding values.

Every `source_record` must resolve to exactly one
`source_boundary_members` record with identical `kind`, `locator`,
`byte_length`, `sha256`, and `claim_class`; an unbound or partially identified
source is invalid. Every `source_id` used by a claim or conflict must resolve to
one such source record. A method with `binding_kind:
INVARIANT_METHOD_CONTRACT` must copy the request's exact
`preflight_observed_capability` and `exact_algorithm_or_command`. A method with
`binding_kind: RESULT_TRANSPORT_CONTRACT` must copy the exact transport
capability and canonical `command_argv` joined with one U+001F separator. A
method with `binding_kind: REVIEWER_ANALYSIS` must use capability
`BOUND_ROLE_ANALYSIS` and algorithm
`READ_ONLY_ANALYSIS_OF_EXACT_SOURCE_BOUNDARY`; it may support only
`SYNTHESIZED`, `CONFLICT`, `UNKNOWN`, `NOT_RUN`, or `BLOCKED` claims. Any
parser, manifest, checksum, inventory, exact-count, or structural observation
must instead use a bound invariant method contract. No free-form deterministic
method is accepted.

`model_binding` has exactly `binding_class`, `configured_model`,
`configured_reasoning`, and `reason`; mechanical adds `preferred_model`.
`binding_class` equals `STATIC_CONFIGURATION_BINDING`; model/reasoning equal the
configured role; `reason` is `EXACT_STRING`; mechanical `preferred_model`
equals `gpt-5.3-codex-spark`. `repository_mutations` equals integer zero.
`git_operations` has exactly `add`, `commit`, `push`, `merge`, and `release`,
each `NOT_RUN`. `next_required_action` is `EXACT_STRING`; `stop` is JSON true.
Result/reason compatibility uses the existing closed algebra.

The complete sealed result has exactly the `required_output_fields` key set.
Its first three fields use the literal result schema and recomputed digests; the
eight stable fields are copied from the request; every other field comes from
the validated evidence body. Canonical JSON object key order remains lexical,
regardless of the explanatory order above.

Command success and failure envelopes are also closed. `seal-result` success is
the complete sealed result itself. `check-request` success has exactly
`result: PASS`, `reason_code: NONE`, `validated_request_id`, `request_sha256`,
`result_binding`, `result_binding_sha256`, `request_registry_sha256`,
`repository_mutations: 0`, and `stop: true`. `check-result` success has exactly `result: PASS`,
`reason_code: NONE`, `validated_request_id`, `validated_reviewer_result`,
`validated_reason_code`, `request_sha256`, `result_binding_sha256`,
`repository_mutations: 0`, and `stop: true`. A contract failure has exactly
`result: CONTRACT_VIOLATION`, `reason_code: NONE`,
`finding_origin: REQUEST_OR_CHECKER_DEFECT`, `message: EXACT_STRING`,
`repository_mutations: 0`, and `stop: true`. Compatible subject and blocker
failures retain the existing harness closed envelopes and reason algebra.

### 3.2 Canonical request identity

`request_sha256` is self-excluding. The harness removes only the top-level
`request_sha256` field, serializes the remaining closed request object with
`json.dumps(..., ensure_ascii=False, sort_keys=True, separators=(",", ":"))`,
appends exactly one LF, encodes UTF-8 without BOM, and hashes those bytes.

The closed result-binding projection is:

```yaml
task_id: EXACT_REQUEST_VALUE
request_id: EXACT_REQUEST_VALUE
parent_task_id: EXACT_REQUEST_VALUE
task_class: EXACT_REQUEST_VALUE
role: EXACT_REQUEST_VALUE
exact_subject: EXACT_REQUEST_VALUE
subject_sha256: EXACT_REQUEST_VALUE
source_boundary: EXACT_REQUEST_VALUE
request_sha256: EXACT_RECOMPUTED_REQUEST_IDENTITY
```

`result_binding_sha256` is the SHA-256 of this projection serialized with the
same canonical compact-JSON-plus-one-LF algorithm. The digest is not a member
of its own projection.

The request delivered to a reviewer includes the computed `request_sha256`.
`check-request` recomputes it, validates the stable subject and boundary
references from their request-only member records, validates the configured
role/model binding, and returns the exact result-binding projection plus its
digest. A stale, missing, duplicated, caller-substituted, or self-inconsistent
identity fails before dispatch as
`CONTRACT_VIOLATION/NONE`, `REQUEST_OR_CHECKER_DEFECT`.

Neither request member metadata nor a caller-supplied digest is raw-byte
Evidence. V2 `check-request` and `check-result` therefore both require these
exact additional arguments:

```text
--repository-root <observation_contract.repository_root>
--task-local-root <observation_contract.task_local_root>
--source-blob-map <observation_contract.source_blob_map_path>
```

Both commands execute the same read-only observation algorithm. They first
require all three argument values to equal the request's
`observation_contract`; no equivalent path spelling is accepted. They open `/`
once as a directory descriptor and traverse every component of each absolute
root with descriptor-relative `os.open`, flags `O_RDONLY | O_DIRECTORY |
O_NOFOLLOW | O_CLOEXEC`, and a following `fstat` directory check. This proves
the bound roots without resolving through a symlink.

For every relative repository or task-local path, traversal restarts from the
already-open exact root descriptor. Each intermediate component is opened with
the same directory flags. For the final component, the command obtains
`os.stat(..., dir_fd=parent_fd, follow_symlinks=False)`, then opens with
`O_RDONLY | O_NOFOLLOW | O_CLOEXEC`, then obtains a pre-read `fstat`. It rejects
unless the no-follow stat and pre-read fstat have identical `st_dev`, `st_ino`,
and file-type mode and both identify a regular file. It reads from that
descriptor to EOF, computes raw length and SHA-256, obtains a post-read
`fstat`, and rejects unless pre/post `st_dev`, `st_ino`, `st_mode`, `st_size`,
`st_mtime_ns`, and `st_ctime_ns` are identical. Every descriptor is closed on
success or failure. Absence of the preflight-required descriptor APIs or flags
is `BLOCKED/BLOCKED_REQUIRED_REVIEW_CAPABILITY`; string-path `open`, `realpath`,
glob expansion, or metadata-only checking is a forbidden substitution.

The source-blob map itself is read first by that algorithm relative to the
exact task-local root, then verified for bound length, SHA-256, closed schema,
order, and membership. For every `FILE` subject or source member, the commands
read its normalized path relative to the repository descriptor. For every
non-`FILE` source member, they resolve the unique map record and read its
normalized `blob_path` relative to the task-local descriptor. A stable empty
regular file is valid and produces byte length zero and the SHA-256 of empty
bytes. The commands then rebuild the subject and source manifests from the
observed bytes and compare every member length/digest and both stable
references.

Invalid arguments, root/path grammar, root containment, map schema, or duplicate
or overlapping map records are
`CONTRACT_VIOLATION/NONE` with origin `REQUEST_OR_CHECKER_DEFECT`. An unavailable
`REFERENCE` byte source is `BLOCKED/BLOCKED_REFERENCE_ACCESS`; missing or stale
subject bytes are `BLOCKED/BLOCKED_SUBJECT_IDENTITY_MISMATCH`; missing or stale
non-reference source bytes are `BLOCKED/BLOCKED_SCOPE_OR_PROVENANCE`. No
alternate parser, metadata-only comparison, cached digest, or caller assertion
may substitute. `check-result` repeats the complete observation rather than
trusting the earlier PASS, so a byte or membership change after request check is
terminally detected before Evidence is consumed.

The primary materializes canonical request bytes only at a distinct normalized
path inside the exact `task_local_root`, using exclusive creation. The exact
request path, byte length, and SHA-256 are supplied to the reviewer. The
reviewer has read-only access to that request, the repository root, the source
map, and every mapped blob. The external tool boundary removes the temporary
directory only after the reviewer has terminated and the primary has completed
`check-result` plus any gate normalization for that request. This temporary
transport is not repository or subject Evidence and cannot substitute for any
bound source. No request or result artifact is persisted in the repository.

### 3.2.1 Request identity lifecycle and no-reuse rule

The primary controller maintains a task-local in-memory registry keyed by
`<task_id, execution_id, request_id>`. Its closed states are `DRAFT`,
`CHECKED`, `DISPATCHED`, `TERMINAL`, and `ABANDONED_UNSENT`:

```text
DRAFT -> CHECKED       only after check-request PASS
DRAFT -> ABANDONED_UNSENT on any pre-dispatch contract failure or byte change
CHECKED -> DISPATCHED  exactly once
DISPATCHED -> TERMINAL exactly once on any reviewer terminal result
```

No reverse transition exists. A `DRAFT` envelope that fails `check-request` is
marked `ABANDONED_UNSENT`, its request ID and digest are abandoned, and a
corrected envelope must use a new request ID. This stricter identity rule does
not count as a reviewer retry because no dispatch occurred. A `CHECKED` request
whose bytes change is likewise abandoned and reissued under a new ID.

Once `DISPATCHED`, the request ID and `request_sha256` pair is immutable and may
never be dispatched again, whether its result is PASS, non-PASS, malformed,
unavailable, or contract-invalid. A candidate correction uses a new candidate
digest and new request ID. An authorized validator-harness correction preserves
candidate bytes but still uses a new request ID. Same-request retry, identical
request replay, automatic fallback, and re-entry are forbidden.

The task-local registry is controller state, not repository Evidence. A V2
`check-request` invocation takes the current registry projection as a read-only
input and rejects duplicate IDs, a second dispatch marker, or one ID paired with
different bytes. Tests exercise the state machine without repository writes.
If the controller process loses this registry after any dispatch, it must not
infer continuity or reuse an ID; recovery requires a new execution identity or
an exact human-authorized handoff that binds the terminal request records.

The registry projection is canonical compact JSON plus one LF with exactly
`schema: ROUTING_R3_REQUEST_REGISTRY_V1` and `records`. Each record has exactly
`task_id`, `execution_id`, `request_id`, `request_sha256_or_invalid_marker`, and
`state`; IDs are `EXACT_STRING`, the identity is `SHA256` or literal
`INVALID_UNSENT`, and state uses the closed enum above. Records are unique and
sorted by UTF-8 bytes of `<task_id><TAB><execution_id><TAB><request_id>`.
`check-request` receives it through exact argument
`--request-registry <task-local-registry-path>`. The controller, not a reviewer,
updates the task-local registry between terminal commands; no registry is
written under the repository root.

### 3.3 Reviewer-authored evidence body

The reviewer authors only this closed body:

```yaml
model: REQUIRED
reasoning: REQUIRED
sources: REQUIRED_LIST
methods: REQUIRED_LIST
temporal_scope: REQUIRED_NONEMPTY_CURRENT_SNAPSHOT_OR_EXACT_INTERVAL
classified_claims: REQUIRED_LIST
conflicts: REQUIRED_LIST
unknowns: REQUIRED_LIST
recommendations: REQUIRED_LIST
checks_run: REQUIRED_LIST
checks_not_run: REQUIRED_LIST
limitations: REQUIRED_LIST
model_binding: REQUIRED
repository_mutations: 0
git_operations:
  add: NOT_RUN
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
result: PASS | FAIL | BLOCKED | CONFLICT | UNKNOWN | NOT_RUN | CONTRACT_VIOLATION
reason_code: REQUIRED_CLOSED_ENUM
next_required_action: REQUIRED_EXACTLY_ONE
stop: true
```

Binding fields are forbidden in the evidence body. This makes accidental
reviewer overrides mechanically impossible.

### 3.4 Read-only `seal-result` command

The new command surface is:

```text
python3 tools/routing_r3_harness.py seal-result \
  --request <exact-task-local-request-json> \
  --verify-embedded-request-sha256 \
  --expected-role <configured-role> \
  --expected-model <configured-model> \
  --review-body-stdin
```

The command reads exactly one UTF-8 JSON object from stdin, rejects duplicate
keys, floats, non-finite numbers, trailing non-whitespace bytes, unknown fields,
and any binding-field injection. It recomputes and verifies the request's
embedded self-excluding digest, then validates the V2 request and evidence body,
then copies the eight stable binding fields and `request_sha256` from the bound
request, adds `result_schema: ROUTING_R3_REVIEW_RESULT_V2` and the computed
`result_binding_sha256`, and emits one complete canonical result to stdout.

`seal-result` is read-only. It creates no file, changes no repository byte,
changes no Git state, dispatches no agent, computes no aggregate verdict, and
makes no semantic or human decision. The reviewer must return the exact stdout
object as its result. The primary must not run `seal-result` on the reviewer's
behalf because that would blur authorship and could complete incomplete Evidence.
This is a normative role/authority rule, not a property inferable from result
bytes alone.

The seal is deterministic integrity Evidence, not cryptographic attestation of
which process invoked the command. A complete manually assembled object with
identical canonical bytes is indistinguishable to `check-result` and therefore
passes the deterministic byte/schema gate. It is not acceptable workflow
Evidence unless the bound reviewer run also reports the exact sealing method.
Reviewer run identity, `result_transport_contract`, and the reviewer's
`methods` record preserve reported authorship provenance; the later safe pilot
tests that the configured role follows this protocol. The harness must not
claim actor verification or stronger provenance than it can observe.

Preflight must prove Python and the exact `seal-result` command are available
before dispatch. If the required capability is unavailable, dispatch is
`BLOCKED/BLOCKED_REQUIRED_REVIEW_CAPABILITY`; no parser, manual merge, fallback,
or same-request retry is permitted.

### 3.5 V2 `check-result`

For new requests, `check-result` must:

1. validate the exact V2 request and recompute `request_sha256`;
2. recompute the result-binding projection and `result_binding_sha256`;
3. require all current reviewer result fields at top level, including the eight
   stable binding fields;
4. require exact equality between result and request binding fields;
5. require exact equality of both deterministic digests;
6. validate role/model/reasoning, temporal scope, claim classes, result/reason
   algebra, zero repository mutations, complete Git `NOT_RUN`, one next action,
   and `stop: true`;
7. return deterministic Evidence only.

The full result continues to satisfy the current R3 requirement that every
subagent result report task/request/parent IDs, task class, role, exact subject,
subject SHA-256, source boundary, model binding, methods, claims, limitations,
result algebra, zero-write status, one next action, and stop. The difference is
that the harness, invoked by the reviewer, copies the identity-bearing fields;
the reviewer no longer reconstructs them.

### 3.6 Historical V1 boundary

No historical request, result, inline Stage Report, or validation report is
migrated, recreated, repaired, or backfilled. The old V1 validator remains only
as an explicit read-only diagnostic path:

```text
--contract-version ROUTING_R3_REVIEW_V1_HISTORICAL
```

V1 Evidence can explain a historical run but cannot satisfy a new required
gate, aggregate, freeze, Stage Report, safe pilot, acceptance, or activation.
V2 may be used before activation only inside the exact authorized
`PRE_R3_BOOTSTRAP` validator-redesign package execution to review its own
current harness candidate. After exact R3 acceptance and activation, every new
R3-governed request must use V2. It remains forbidden for ordinary or mass
documentation routing before activation. There is no implicit version detection
and no fallback from V2 to V1.

### 3.7 Clause-level precedence and six-plus-five preservation

This precedence applies only to exact execution
`ROUTING-R3-DETERMINISTIC-HARNESS-RECOVERY-EXECUTE-001` when its future human
authorization binds accepted SHA-256 identities for both this plan and
`docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-harness-recovery.md`.
It makes these exact replacements:

1. In the pinned plan, section `Harness Contract / Commands`, replace the
   six-command list only for this execution with this closed list:
   `manifest`, `check-request`, `seal-result`, `check-result`, `check-gate`,
   `freeze-package-binding`, `verify-package-binding`, `create-stage-report`,
   and `verify-stage-report`. `check-request` and `check-result` additionally
   require the explicit contract-version selector. Every command except
   `create-stage-report` remains read-only.
2. In the recovery plan, section `Identity Model / Clause-level precedence over
   the pinned legacy plan`, replace numbered clause 2, which says the command
   list is extended only by `freeze-package-binding` and
   `verify-package-binding`, with replacement 1 above. Numbered manifest clause
   1 remains unchanged.
3. In the pinned plan, section `Stage C / Task 6 / Step 4`, retain rejection of
   every missing or mismatched mandatory result field, but replace reviewer
   reconstruction of open-ended `exact_subject` and `source_boundary` values
   with the closed stable V2 references, `request_sha256`, reviewer-side
   `seal-result`, and V2 `check-result` defined here. The checker still never
   fills missing Evidence from chat or primary inference.
4. In the recovery plan, section `Task 5 / Step 3`, interpret “a result whose
   exact_subject drops one bound token” as a V2 result that omits or changes any
   key/value of the closed stable subject reference. Request-only context tokens
   are instead protected by `request_sha256` and are not manually echoed.
5. In the recovery plan, section `Task 7 / Step 2`, replace manual echo of the
   complete authoritative-dependency identity with the V2 compact
   `source_boundary` reference plus `request_sha256`. The complete authoritative
   dependency manifest and digest remain required request-bound context and are
   still verified before dispatch; they are not reconstructed by the reviewer.

Every other sentence, task, invariant, negative case, acceptance criterion, and
authority boundary in both plans remains non-superseded. In particular, the
canonical six-file output subject, five pinned dependencies, R6 subject
identity, `freeze-package-binding`, `verify-package-binding`, immutable recovery
Stage Report, single writer, zero reviewer writes, no retry/fallback, and all
lifecycle/Git boundaries remain applicable. The four `.codex/agents/*.toml`
role definitions remain pinned read-only dependencies; V2 behavior is bound by
each request's `result_transport_contract` and the mutable primary controller.

Without both accepted plan hashes and this exact five-replacement applicability
predicate in the future authorization, execution is
`BLOCKED/BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH`. This plan does not modify
or silently accept the current recovery-plan candidate.

## 4. Failure and recovery behavior

| Condition | Classification | Candidate mutation | Next action |
|---|---|---:|---|
| Invalid V2 request before dispatch | `CONTRACT_VIOLATION/NONE`, `REQUEST_OR_CHECKER_DEFECT` | 0 | Correct unsent request envelope; this is not a retry |
| Required sealing capability absent at preflight | `BLOCKED/BLOCKED_REQUIRED_REVIEW_CAPABILITY` | 0 | New human decision or environment recovery |
| Reviewer returns unsealed, partial, stale, or altered result | `CONTRACT_VIOLATION/NONE`, `REQUEST_OR_CHECKER_DEFECT` | 0 | Apply existing one-correction loop breaker only |
| Reviewer Evidence identifies a subject defect | Compatible reviewer technical result with `NONE` unless blocked/conflict algebra applies | 0 in review | Separately authorized candidate correction |
| Result/request binding mismatch | `CONTRACT_VIOLATION/NONE`, `REQUEST_OR_CHECKER_DEFECT` | 0 | Preserve candidate; no result repair |
| Bound model unavailable or materially insufficient | `BLOCKED/BLOCKED_REQUIRED_REVIEW_CAPABILITY` | 0 | New explicit request after human/environment decision |
| Required upstream gate non-PASS | Preserve exact result | 0 | Dependent semantic gate `NOT_RUN`; aggregate cannot PASS |
| Repeated request/checker defect after one authorized validator correction | aggregate `FAIL/NONE` | 0 | Exactly `DEFER_OR_REDESIGN_VALIDATOR`; no finding-specific loop |

This redesign is intended to make the omitted-binding-field failure impossible
on the conforming path. It does not remove the existing fail-closed loop breaker
for a nonconforming reviewer or future validator defect.

## 5. Implementation tasks

### Task 1: Freeze the observed defect with failing tests

**Files:**

- Modify: `tests/test_routing_r3_harness.py`
- Inspect: `tools/routing_r3_harness.py`
- Inspect: exact prior recovery-plan request/result Evidence supplied to the
  implementation run

**Interfaces:**

- Consumes: current `valid_request()`, `valid_result()`, `check-request`, and
  `check-result` helpers.
- Produces: RED tests proving the real nested-echo failure and the desired V2
  sealed path.

- [ ] Add a regression request whose request-only context contains the two
  exact fields omitted by the failed reviewer:
  `correction_authorization_visible_text_byte_length` and
  `correction_authorization_visible_text_sha256`.
- [ ] Prove current V1 `check-result` rejects a result that omits those nested
  fields with the exact current message
  `reviewer result exact_subject does not match request`.
- [ ] Add a V2 fixture in which those fields are under `request_context`, the
  stable `exact_subject` remains unchanged, and the expected sealed result is
  complete.
- [ ] Add a regression showing a third arbitrary context field changes
  `request_sha256` but does not change the stable result-binding field set.
- [ ] Run only the new tests and prove RED because V2 schemas and `seal-result`
  do not exist.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_routing_r3_harness.ValidatorRedesignTests -v
```

Expected before implementation: V2 tests fail; the historical reproduction
test passes and records the current defect without modifying candidate bytes.

### Task 2: Implement closed subject and source references

**Files:**

- Modify: `tools/routing_r3_harness.py`
- Test: `tests/test_routing_r3_harness.py`

**Interfaces:**

- Produces:
  - `validate_exact_subject_reference(value, subject_members)`;
  - `build_source_boundary_manifest(members) -> bytes`;
  - `validate_source_boundary_reference(value, members)`;
  - closed schema constants for V2.

- [ ] Define exact allowed keys and value types for single-file and subject-set
  references. Reject unknown keys, empty locators, invalid paths, invalid
  digests, negative file lengths, inconsistent member counts, duplicate
  members, symlinks, and computed identity mismatch. Accept zero only when the
  direct raw-byte observation proves a stable empty regular file.
- [ ] Define one canonical source-boundary manifest with explicit record kind,
  normalized locator, byte length, and digest. Bind repository paths, exact
  inline decision identities, and task-local Evidence as distinct record kinds;
  do not let one kind substitute for another.
- [ ] Recompute the reference from member records rather than trusting a
  caller-authored digest.
- [ ] Implement the exact `observation_contract`, repository-root validation,
  exact task-local-root and relative map transport, canonical source-blob-map
  parser, descriptor-relative component traversal, no-follow open,
  lstat/pre-read-fstat identity comparison, post-read-fstat stability check,
  and identity rebuild specified in section 3.2. Do not accept member metadata
  without these observations.
- [ ] Reject authorization, correction chronology, finding IDs, prose, or
  arbitrary metadata under `exact_subject` and `source_boundary`; those fields
  belong in request-only context.
- [ ] Run the focused subject/boundary tests until GREEN.

### Task 3: Implement canonical V2 request binding

**Files:**

- Modify: `tools/routing_r3_harness.py`
- Test: `tests/test_routing_r3_harness.py`

**Interfaces:**

- Produces:
  - `canonical_request_body_bytes(request) -> bytes`;
  - `compute_request_sha256(request) -> str`;
  - `build_result_binding(request) -> dict`;
  - `compute_result_binding_sha256(binding) -> str`;
  - `validate_request_lifecycle(registry, request) -> None`;
  - V2 branch of `check-request`.

- [ ] Add `request_schema`, `request_sha256`, `subject_members`,
  `source_boundary_members`, `request_context`, `observation_contract`, and the closed
  `result_transport_contract` to the V2 request schema while preserving every
  currently required request field.
- [ ] Implement the exact self-excluding canonicalization algorithm from
  section 3.2. Reject noncanonical domains, duplicate keys, floats, unknown
  schema versions, missing context maps, and caller-supplied alternate hashes.
- [ ] Validate request role/model and the existing mechanical
  `invariant_semantics`/`method_contract` contract before producing a binding.
- [ ] For every role, require `result_transport_contract` to name the exact
  preflight-observed `seal-result` capability, exact command, expected canonical
  success shape, and forbidden manual-merge/parser/fallback substitutions.
- [ ] Make V2 `check-request` return `request_sha256`, the complete
  `result_binding`, `result_binding_sha256`, `request_registry_sha256`,
  `repository_mutations: 0`, `result: PASS`, `reason_code: NONE`, and
  `stop: true`.
- [ ] Require the exact `--repository-root`, `--task-local-root`, and
  `--source-blob-map` inputs, observe all current raw bytes, and reject a
  request before dispatch when the observed members cannot reproduce its
  subject and source references.
- [ ] Preflight the exact descriptor APIs/flags and reviewer read access to the
  bound request, repository root, map, and blobs. Preserve every carrier until
  terminal result checking and gate normalization complete; map unavailable
  bytes to the exact closed blocker without fallback.
- [ ] Require explicit `--contract-version`; do not infer V1 or V2 from fields.
- [ ] Implement the exact task-local request lifecycle from section 3.2.1 and
  reject abandoned, duplicate, changed, or already-dispatched request IDs.
- [ ] Run request-binding tests until GREEN.

### Task 4: Implement reviewer-side deterministic result sealing

**Files:**

- Modify: `tools/routing_r3_harness.py`
- Test: `tests/test_routing_r3_harness.py`

**Interfaces:**

- Produces:
  - `REVIEW_BODY_FIELDS` closed set;
  - `validate_review_body(body, request)`;
  - `seal_reviewer_result(request, body) -> dict`;
  - CLI command `seal-result`.

- [ ] Add exact CLI arguments from section 3.4 and require stdin only when
  `--review-body-stdin` is present. Reject a positional payload, file-output
  option, alternate parser, or more than one JSON object.
- [ ] Validate the body with current role/model/reasoning, temporal-scope,
  claim-class, result/reason-code, zero-write, Git, one-next-action, and stop
  rules.
- [ ] Require every `source_record` to match one exact bound source member and
  every deterministic `method_record` to match the bound invariant or result
  transport contract. Reject free-form deterministic Evidence.
- [ ] Reject every stable binding field and every unknown field in the body.
- [ ] Copy all required binding fields only from the validated request, compute
  `result_binding_sha256`, and emit one complete
  `ROUTING_R3_REVIEW_RESULT_V2` canonical object.
- [ ] Observe repository and request bytes before and after sealing in tests;
  require byte equality and `repository_mutations: 0`.
- [ ] Add a test in which context grows by ten arbitrary fields while sealed
  identity fields remain complete and exact without body changes.
- [ ] Add a test that the primary cannot use a partial body as Evidence; only
  complete sealed output proceeds to `check-result`.
- [ ] Add a test proving a complete byte-equivalent hand-assembled result is
  indistinguishable to the deterministic checker. Record this as the explicit
  actor-provenance limitation; do not falsely claim mechanical rejection.
- [ ] Run `ValidatorRedesignTests` until GREEN.

### Task 5: Upgrade `check-result` without weakening Evidence

**Files:**

- Modify: `tools/routing_r3_harness.py`
- Test: `tests/test_routing_r3_harness.py`

**Interfaces:**

- Consumes: exact V2 request plus sealed V2 result.
- Produces: V2 `check-result` deterministic Evidence.

- [ ] Require `result_schema`, `request_sha256`, and
  `result_binding_sha256` in addition to every current reviewer result field.
- [ ] Recompute request and binding identities, compare every stable field, and
  validate all reviewer-authored evidence fields.
- [ ] Repeat the complete raw-byte observation using the bound repository root,
  task-local root, and source-blob map before accepting the result; never trust
  the earlier request-check snapshot or caller-provided member metadata.
- [ ] Reject an unsealed body, manually assembled partial result, stale request
  digest, changed context, changed subject bytes, changed source membership,
  unbound source Evidence, unbound deterministic method Evidence,
  wrong role/model/reasoning, invalid temporal scope, incompatible result/reason
  pair, nonzero mutation, Git action, multiple next actions, or `stop != true`.
- [ ] Keep error origin `REQUEST_OR_CHECKER_DEFECT` for envelope/checker defects
  and never recommend candidate mutation from such a failure.
- [ ] Retain V1 only behind the explicit historical diagnostic selector. Add a
  test proving V1 cannot normalize a current required gate.
- [ ] Run all request/result/gate contract tests until GREEN.

### Task 6: Reconcile the routing contract owners

**Files:**

- Modify:
  `docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md`
- Modify:
  `docs/superpowers/plans/2026-08-02-aos-documentation-routing-r3-reliability-first.md`
- Modify: `docs/ideas/AOS_Documentation_Agent_Routing_R1.md`
- Modify: `.codex/config.toml`
- Inspect and preserve: `.codex/agents/mechanical-checker.toml`
- Inspect and preserve: `.codex/agents/contract-analyst.toml`
- Inspect and preserve: `.codex/agents/semantic-reviewer.toml`
- Inspect and preserve: `.codex/agents/reference-explorer.toml`
- Inspect and preserve:
  `docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-harness-recovery.md`

**Interfaces:**

- Consumes: implemented V2 schemas and commands.
- Produces: one identical request-sealing contract across every owner and role.

- [ ] Replace reviewer reconstruction wording with the exact V2 workflow:
  preflight capability, V2 `check-request`, reviewer-run `seal-result`, primary
  V2 `check-result`, primary normalization, and no same-request retry.
- [ ] Record the exact five-replacement precedence from section 3.7 in each mutable
  owner, and require the future recovery authorization to bind both accepted
  plan hashes.
- [ ] Preserve the requirement that the final reviewer result contains every
  currently mandatory field. Do not describe the evidence body as a reviewer
  result.
- [ ] Require each reviewer to run `seal-result` itself and return exact stdout.
  Explicitly forbid primary-side sealing, manual merge, omitted Evidence
  completion, alternate parser, fallback, or automatic retry.
- [ ] Record `mechanical_checker` as statically bound to `gpt-5.6-luna` because
  `gpt-5.3-codex-spark` was absent from the configuration-time catalog; never
  describe this as a runtime fallback.
- [ ] Preserve the result/reason algebra, temporal-scope grammar, structural
  FTR/LES invariant, gate ordering, maximum two concurrent agents, depth one,
  single writer, candidate invalidation rules, Stage Report collision rule, and
  one-correction loop breaker.
- [ ] Mark V1 historical-only. Permit V2 before activation solely for the exact
  authorized `PRE_R3_BOOTSTRAP` redesign-package self-review, and require V2 for
  every new R3-governed request only after exact package acceptance and
  activation. No historical report or request is rewritten.
- [ ] Preserve the recovery plan and four role-definition bytes exactly. Bind
  V2 result sealing through the accepted amendment, each request's
  `result_transport_contract`, and the mutable primary controller. Do not change
  the six-subject/five-dependency recovery model or invent
  acceptance/activation.
- [ ] After final design bytes, recompute and update only exact derived design
  SHA references. Do not substitute subject-set or plan identities.

### Task 7: Add the closed negative-fixture matrix

**Files:**

- Modify: `tests/test_routing_r3_harness.py`
- Modify only when a test proves a harness defect:
  `tools/routing_r3_harness.py`

- [ ] Add `VRD-NC-001`: rich request context grows; sealed result stays complete
  and passes binding validation.
- [ ] Add `VRD-NC-002`: one stable subject field changes; `check-request` fails
  before dispatch.
- [ ] Add `VRD-NC-003`: request context changes after sealing; `check-result`
  rejects stale `request_sha256`.
- [ ] Add `VRD-NC-004`: review body injects `exact_subject`; `seal-result`
  rejects it.
- [ ] Add `VRD-NC-005`: review body omits temporal scope; sealing fails.
- [ ] Add `VRD-NC-006`: result omits one required top-level binding field;
  `check-result` fails.
- [ ] Add `VRD-NC-007`: result carries wrong static model/reasoning; sealing or
  checking fails.
- [ ] Add `VRD-NC-008`: bound model capability disappears before dispatch;
  primary returns `BLOCKED/BLOCKED_REQUIRED_REVIEW_CAPABILITY` and does not
  dispatch.
- [ ] Add `VRD-NC-009`: stdin has duplicate keys, two objects, float, NaN,
  invalid UTF-8, or trailing payload; sealing fails closed.
- [ ] Add `VRD-NC-010`: any Git operation is not `NOT_RUN` or repository
  mutation is nonzero; sealing fails.
- [ ] Add `VRD-NC-011`: result/reason pair violates the closed algebra; sealing
  fails.
- [ ] Add `VRD-NC-012`: a complete hand-assembled result with byte-identical
  binding passes deterministic `check-result`, while the workflow review marks
  sealing-method provenance `UNKNOWN` unless the bound reviewer reports the
  exact method. The harness must not claim actor detection.
- [ ] Add `VRD-NC-013`: current required gate uses V1; gate normalization
  rejects it.
- [ ] Add `VRD-NC-014`: reviewer returns valid sealed non-PASS; primary
  preserves it and does not coerce PASS.
- [ ] Add `VRD-NC-015`: semantic review is requested before current upstream
  PASS gates; request is rejected before dispatch.
- [ ] Add `VRD-NC-016`: one validator correction followed by a fresh repeated
  checker defect; aggregate remains `FAIL/NONE` with exactly
  `DEFER_OR_REDESIGN_VALIDATOR`.
- [ ] Add `VRD-NC-017`: an invalid unsent envelope is abandoned; the corrected
  envelope requires a new request ID and is not counted as reviewer retry.
- [ ] Add `VRD-NC-018`: identical or changed bytes under an already dispatched
  request ID are rejected without redispatch.
- [ ] Add `VRD-NC-019`: a directly observed stable empty regular file with
  declared byte length zero is accepted, while a negative length, symlink,
  non-regular file, or file changed during the read is rejected.
- [ ] Add `VRD-NC-020`: a source record with an unbound locator, altered
  length/digest/class, or a deterministic method not equal to its bound method
  or transport contract is rejected before Evidence consumption.
- [ ] Add `VRD-NC-021`: mutate one subject file, one source file, and one
  task-local source blob separately after `check-request` PASS; each fresh
  `check-result` invocation rereads bytes and returns the exact applicable
  closed blocker without accepting the sealed result.
- [ ] Add `VRD-NC-022`: omit, alter, duplicate, move inside the repository, or
  symlink a source-blob-map entry; request checking fails closed and performs no
  substitution.
- [ ] Add `VRD-NC-023`: substitute an unbound task-local root, equivalent path
  spelling, absolute blob path, escaped relative blob path, unreadable map, or
  unreadable blob; preflight or review returns the exact closed contract or
  blocker result and never reconstructs bytes from chat.
- [ ] Add `VRD-NC-024`: replace the final path component or introduce an
  ancestor symlink between no-follow stat and descriptor open; lstat/pre-read
  fstat identity or descriptor traversal rejects it. Mutate size, mtime, or
  ctime during the read; the post-read stability check rejects it.
- [ ] Add `VRD-NC-025`: remove reviewer access to one exact non-`FILE` blob
  after preflight. The reviewer returns `BLOCKED_REFERENCE_ACCESS` for a
  `REFERENCE` and `BLOCKED_SCOPE_OR_PROVENANCE` for another kind, with no
  fallback, result completion by the primary, or same-request retry.

Run the complete harness suite:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s tests -p 'test_routing_r3_harness.py' -v
```

Expected: all tests pass, no repository mutation occurs during read-only
commands, and no test treats harness PASS as semantic validation or acceptance.

### Task 8: Run internal gates through the redesigned path

**Files:**

- Read: exact final implementation subject and authoritative dependencies
- Write: none during reviewer gates

- [ ] Preflight the configured models and the exact `seal-result` command.
- [ ] Build and V2-check independent mechanical and contract requests. Their
  stable references bind the same current candidate, while their request-only
  context remains role-specific.
- [ ] Dispatch mechanical and contract reviewers in parallel, maximum two.
  Each reviewer runs `seal-result` and returns exact canonical stdout.
- [ ] V2-check each sealed result before consuming it. Normalize findings and
  gates only after complete current Evidence passes the result contract.
- [ ] If both upstream gates are PASS, dispatch one sequential semantic
  reviewer bound to current candidate bytes and primary-normalized upstream
  Evidence. Seal and check its result the same way.
- [ ] Correct only proven `SUBJECT_DEFECT` findings within the future exact
  implementation allowlist and correction budget. Any candidate mutation
  invalidates affected gates; rerun with new request IDs and current hashes.
- [ ] Do not correct `REQUEST_OR_CHECKER_DEFECT` by changing candidate content.
  Apply at most one separately authorized validator correction, then one fresh
  request; a repeated defect terminates at the existing human loop breaker.

### Task 9: Freeze and create the exact recovery bootstrap Stage Report

**Files:**

- Create exactly once only under a future exact `EXECUTE` authorization:
  `planning/verification/bootstrap/routing-r3-harness/ROUTING-R3-DETERMINISTIC-HARNESS-RECOVERY-EXECUTE-001/stage-report.yaml`

- [ ] Require the future authorization to name exact execution ID
  `ROUTING-R3-DETERMINISTIC-HARNESS-RECOVERY-EXECUTE-001`,
  exact report path, complete implementation allowlist, starting baselines,
  both accepted plan identities, the five-replacement precedence, absent-before-write
  condition, correction budget, and `PRE_R3_BOOTSTRAP` profile.
- [ ] Run all required final gates on unchanged current bytes. Every required
  gate must be V2, current, complete, sealed, and PASS; material findings must
  be empty.
- [ ] Recheck report-path absence immediately before exclusive creation. A
  collision returns `BLOCKED/BLOCKED_STAGE_REPORT_PATH_COLLISION`; never inspect,
  overwrite, reuse, rename, delete, or backfill it.
- [ ] Create the report only through the primary and only after freeze. Record
  exact byte length and SHA-256 by direct re-read.
- [ ] Keep lifecycle status `DRAFT_CANDIDATE`, static validation `NOT_RUN`, safe
  pilot `NOT_RUN`, human acceptance `NOT_RUN`, activation `NOT_RUN`, and every
  Git action `NOT_RUN`.
- [ ] End EXECUTE with exactly one next action: authorize separate read-only
  package validation. Stop.

### Task 10: Separately validate and pilot

**Files:** read only in each separately authorized stage.

- [ ] Run a new `POST_STOP_DOCUMENTATION` `READ_ONLY_NEW_RUN` bound to exact
  candidate, authoritative dependencies, V2 gate Evidence, and repository
  Stage Report bytes.
- [ ] `VALIDATE` must not repair, reseal on behalf of a reviewer, mutate a
  request, create a report file, or start a pilot.
- [ ] If and only if static validation passes, request a separate safe-pilot
  authorization. The pilot must be one bounded non-mass documentation-routing
  case and must not activate R3.
- [ ] Human acceptance and exact hash-bound activation remain two later,
  separate decisions. Commit, Push, Merge, and Release remain separate from all
  documentation lifecycle stages.

## 6. Future implementation allowlist

An implementation authorization derived from accepted versions of this plan
and the recovery plan may name only the exact canonical six-file subject plus
the exact recovery bootstrap Stage Report path below. The five dependencies
remain pinned read-only inputs:

```text
tools/routing_r3_harness.py
tests/test_routing_r3_harness.py
docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md
docs/superpowers/plans/2026-08-02-aos-documentation-routing-r3-reliability-first.md
docs/ideas/AOS_Documentation_Agent_Routing_R1.md
.codex/config.toml
planning/verification/bootstrap/routing-r3-harness/ROUTING-R3-DETERMINISTIC-HARNESS-RECOVERY-EXECUTE-001/stage-report.yaml
```

Pinned read-only dependencies:

```text
.codex/agents/mechanical-checker.toml
.codex/agents/contract-analyst.toml
.codex/agents/semantic-reviewer.toml
.codex/agents/reference-explorer.toml
docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-deterministic-executable-harness.md
```

This list is a plan proposal, not present implementation authority. If final
implementation needs another repository path, that is scope expansion and
requires a new human decision before mutation.

## 7. Implementation acceptance criteria

The validator redesign is ready for separate static validation only when all
conditions below are simultaneously true:

1. The exact historical omitted-field failure is covered by a deterministic
   regression.
2. V2 requests use closed stable `exact_subject` and `source_boundary`
   references; chronology and authorization metadata cannot enter their echo
   surface.
3. `request_sha256` binds the complete request-only context with one documented
   canonical algorithm.
4. `seal-result` is the normative construction method for a new V2 reviewer
   result; deterministic validation proves binding and schema, not actor
   provenance.
5. `seal-result` is invoked by the reviewer, is read-only, and copies every
   required identity-bearing result field from the checked request.
6. The reviewer still authors every semantic observation, method, claim,
   conflict, unknown, limitation, technical result, reason code, and next
   action; the harness does not make those judgments.
7. The primary never fills or repairs reviewer Evidence.
8. V2 `check-result` recomputes request and result-binding identities and
   validates every current result field, every source/method relationship, and
   a fresh direct observation of all bound subject and source bytes.
9. All parser, temporal-scope, result-algebra, model-binding, authority,
   zero-write, Git, stale-Evidence, and negative-fixture tests pass.
10. New required gates cannot use V1; historical V1 Evidence is not migrated or
    promoted.
11. The four role-definition files and pinned deterministic-harness plan remain
    byte-identical read-only dependencies; the canonical subject remains the
    same six output files selected by the recovery model.
12. Mechanical and contract gates can run in parallel; semantic remains
    sequential after normalized upstream PASS Evidence.
13. Candidate mutation invalidates every affected gate; no stale gate can
    contribute to freeze.
14. No same-request retry or runtime model fallback exists.
15. Repeated checker defects still terminate once at
    `DEFER_OR_REDESIGN_VALIDATOR`; the redesign removes the known cause rather
    than removing the guard.
16. Stage Report creation remains exclusive, primary-only, path-bound, and
    separate from `VALIDATE`.
17. R3 remains inactive `DRAFT_CANDIDATE`; safe pilot, acceptance, activation,
   implementation authority, and Git authority are not inferred.
18. A stable directly observed empty regular file is accepted consistently;
   negative length, symlink, non-regular file, and mid-read mutation are rejected.
19. Both V2 request and result checks require the bound repository root and
   exact task-local root plus canonical relative source-blob map, reread every
   raw byte through descriptor-safe traversal, and fail closed when current
   bytes cannot reproduce the declared identities.
20. Every result source resolves to one exact source-boundary member, and every
   deterministic result method resolves to the request's invariant or transport
   contract; no unbound Evidence can enter a normalized gate.
21. The reviewer receives exact read-only access to the bound request,
   repository root, source map, and non-`FILE` blobs until its terminal result
   has passed result checking and gate normalization; unavailable bytes produce
   the exact closed blocker and never a reconstructed substitute.
22. Root and file access uses preflight-required descriptor-relative,
   no-follow traversal with lstat/pre-read-fstat identity equality and
   post-read metadata stability; final-component replacement and ancestor
   symlink races are covered by negative fixtures.

## 8. Internal correction traceability

The first contract review result was envelope-valid and returned `FAIL/NONE`.
Its subject findings are closed in this corrected candidate as follows:

| Finding | Correction | Required recheck |
|---|---|---|
| `CF-001` | Section 3.1.1 defines exact scalar domains, closed request/member/context/transport/body/result schemas, nested records, and success/error envelopes. | Mechanical structure plus contract completeness |
| `CF-002` | Section 3.4 narrows sealing to deterministic integrity and explicitly denies actor attestation. | Contract and semantic authority review |
| `CF-003` | Section 3.7 identifies exact source headings, replaced behavior, applicability predicate, replacement behavior, and non-superseded remainder. | Cross-document contract and semantic review |
| `CF-004` | Tasks 4 and 7 add the complete hand-assembled-result limitation fixture instead of a false actor-detection test. | Contract negative-case review |
| `CF-005` | Section 3.2.1 adds an immutable task-local request lifecycle, exact registry schema, new-ID rule, and replay prohibition. | Mechanical state-machine and contract recovery review |

The second contract review was envelope-valid and returned `FAIL/NONE`. Its
three subject findings are closed in this candidate as follows:

| Finding | Correction | Required recheck |
|---|---|---|
| `NF-001` | The normative schema and Task 2 now permit zero only for a directly observed stable empty regular file and reject only negative declared lengths; `VRD-NC-019` covers both sides. | Contract consistency plus mechanical fixture inventory |
| `NF-002` | Result source records now carry full member identity and must resolve exactly to the boundary; deterministic method records must resolve to the bound invariant or transport contract; `VRD-NC-020` rejects unbound Evidence. | Contract relational-binding and semantic Evidence review |
| `NF-003` | The bound observation contract, repository root, canonical source-blob map, direct no-symlink read algorithm, second result-time reread, blocker mapping, and `VRD-NC-021..022` make current-byte verification executable from exact inputs. | Mechanical command/schema review plus contract recovery review |

The third contract review was envelope-valid and returned `FAIL/NONE`. Its
three subject findings are closed in this final bounded correction as follows:

| Finding | Correction | Required recheck |
|---|---|---|
| `NF-004` | `observation_contract` now binds the exact absolute task-local root and relative map path; every mapped blob is a normalized relative path, and argument/path equivalence substitutions are rejected. | Contract cold-start containment plus mechanical schema review |
| `NF-005` | Section 3.2 now mandates component-by-component descriptor traversal, no-follow opens, lstat/pre-read-fstat identity equality, post-read metadata equality, exact capability blocking, and race fixtures `VRD-NC-024`. | Contract race-safety plus mechanical fixture review |
| `NF-006` | The controller now grants the reviewer exact read-only access to the bound request, repository root, map, and blobs until result checking and normalization complete; inaccessible source kinds map to exact blockers in `VRD-NC-023..025`. | Contract transport and semantic provenance review |

The first mechanical result was rejected by `check-result` as
`REQUEST_OR_CHECKER_DEFECT`: the reviewer used an invalid manifest invocation,
substituted an identity method, and returned a nonconforming `reasoning` field.
That result is not a subject finding and did not authorize candidate mutation.
It remains non-PASS Evidence. After this subject correction, every required gate
must use a fresh request ID bound to the new candidate and a literal complete
method command; no same-request retry occurs.

## 9. Internal plan review checklist

- [x] Root cause is tied to current executable code and the exact repeated
  omitted-field failure.
- [x] The proposed architecture retains every mandatory subagent result field.
- [x] Reviewer-authored Evidence and machine-copied binding fields have a clear,
  non-overlapping ownership boundary.
- [x] `seal-result` has one exact input/output transport and performs zero
  writes.
- [x] Request and binding hash algorithms are complete and self-reference-free.
- [x] Stable references are closed and cannot absorb future task chronology.
- [x] V1 historical handling cannot satisfy a current gate.
- [x] Negative cases cover missing, stale, injected, malformed, unavailable,
  non-PASS, and ordering failures.
- [x] The implementation allowlist is bounded and contains no AOS product
  runtime path.
- [x] The recovery plan remains a separate candidate and is not silently
  accepted by this plan.
- [x] Independent validation, safe pilot, acceptance, activation, and Git
  delivery remain separate and `NOT_RUN`.

## 10. Terminal PLAN boundary

This PLAN writes only
`docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-validator-redesign.md`
and performs internal review of that plan. It does not implement V2, modify the
R3 package or recovery plan, create a Stage Report, run independent validation,
run a pilot, accept or activate R3, or perform any Git mutation.

Exactly one next required action after terminal PLAN review is a hash-bound
human decision over this plan:

```text
HUMAN_DECIDE_ROUTING_R3_HARNESS_RECOVERY_VALIDATOR_REDESIGN_PLAN: ACCEPT | NEEDS_CHANGES | REJECT | DEFER
```
