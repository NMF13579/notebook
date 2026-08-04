---
document_id: AOS-DOCUMENTATION-ROUTING-R3-RELIABILITY-FIRST-DESIGN
document_type: APPROVED_DESIGN_SPEC_CANDIDATE
revision: R3
design_target_revision: ROUTING_R3
status: REFERENCE_ONLY
authority: NONE
task_id: ROUTING-R3-DESIGN-SPEC-EXECUTE-001
stage: EXECUTE
operation: WRITE_APPROVED_DESIGN_SPEC_AND_SELF_REVIEW_ONLY
output_path: docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md
design_priority: RELIABILITY_FIRST
selected_implementation_approach: DETERMINISTIC_EXECUTABLE_HARNESS
writer_policy: SINGLE_WRITER
max_concurrent_subagents: 2
routing_configuration_mutation: BOUNDED_BY_ROUTING_R3_DETERMINISTIC_HARNESS_EXECUTE_001
runtime_implementation: NOT_RUN
routing_harness_status: DRAFT_CANDIDATE_IMPLEMENTED
routing_harness_execution_id: ROUTING-R3-DETERMINISTIC-HARNESS-EXECUTE-001
human_acceptance_of_exact_artifact: NOT_RUN
git_authorization: NONE
predecessor_accepted_sha256: 0da5daa611e5aa2b9c1c965f7b41944b5160a81e76f9cd7f6fa6f2781a684cdf
last_correction_task_id: ROUTING-R3-VALIDATOR-HARNESS-CORRECTION-001
result_algebra_decision: B_GENERIC_RESULT_PLUS_REQUIRED_REASON_CODE
result_algebra_decision_sha256: d520c8d6d8866f088fa4162ce31e0cfe69c4f66961ca8df73a3b593bc431d48e
harness_architecture_decision_sha256: 6b975eb7673b763598fa43577fb207897807758b36ffc0ff2f14d8c585bfc7a8
harness_plan_sha256: 77ff1093da3462881cb658bf364675c2cc6467ea28fbd21577ffa2d409a00316
harness_plan_acceptance_decision_sha256: 985fa966654a2016e8f83fec0fe779091c7dd98c8854f94f682e6e5e3cc09bc2
authorization:
  actor_class: HUMAN
  authorization_id: ROUTING-R3-DESIGN-SPEC-EXECUTE-001
  runtime_turn_id: UNAVAILABLE_AT_RUNTIME
  allowed_paths:
    - docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md
  operation: WRITE_APPROVED_DESIGN_SPEC_AND_SELF_REVIEW_ONLY
  one_shot: true
  exact_visible_utf8_text: >-
    AUTHORIZE ROUTING-R3-DESIGN-SPEC-EXECUTE-001;
    allowed_path=docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md;
    operation=WRITE_APPROVED_DESIGN_SPEC_AND_SELF_REVIEW_ONLY;
    routing_configuration_mutation=FORBIDDEN; commit=FORBIDDEN;
    push=FORBIDDEN; merge=FORBIDDEN; release=FORBIDDEN; one_shot=true
  utf8_byte_length: 335
  sha256: 0ad23bb56ef0bf972cfa6f71aa07a61f051ef4472180ea1a2e65afdf3d91c60f
design_approval:
  source_class: CURRENT_EXPLICIT_HUMAN_DECISIONS
  choices:
    - {runtime_turn_id: 019fc368-5bf6-7e63-af60-393c37fbd872, choice: RELIABILITY_FIRST}
    - {runtime_turn_id: 019fc369-5123-7852-b44d-0f438e41b811, choice: REPOSITORY_RELATIVE_IMMUTABLE_STAGE_REPORT}
    - {runtime_turn_id: 019fc36a-0e20-7aa2-b744-0dfa9086e3e1, choice: CLOSED_DETERMINISTIC_CONTRACT_TRIGGERS}
    - {runtime_turn_id: 019fc36a-9712-7f71-a13a-d2bfc94586b0, choice: RUN_SCOPED_STAGE_REPORT_NAMESPACE}
    - {runtime_turn_id: 019fc36b-6912-7a72-9cba-625ee2175769, choice: CURRENT_UNCLOSED_AND_FUTURE_RUNS_WITHOUT_HISTORICAL_BACKFILL}
    - {runtime_turn_id: 019fc36c-9c17-7fb2-8abf-c757397bf370, choice: BOUNDED_CONTRACT_AND_CONFIGURATION_UPGRADE, status: SUPERSEDED}
    - {runtime_turn_id: UNAVAILABLE_AT_RUNTIME, choice: DETERMINISTIC_EXECUTABLE_HARNESS, decision_sha256: 6b975eb7673b763598fa43577fb207897807758b36ffc0ff2f14d8c585bfc7a8}
  section_approvals:
    - {runtime_turn_id: 019fc36e-c8af-7e22-bb06-cafd05c78061, section: ARCHITECTURE_AND_DATA_FLOW}
    - {runtime_turn_id: 019fc36f-5eb1-7410-8ca7-29d6ab0a5ecd, section: FAIL_CLOSED_AND_RECOVERY}
    - {runtime_turn_id: 019fc370-4318-7ce1-8ca5-7ccc3343c054, section: CHANGE_SURFACE_TESTING_AND_ACCEPTANCE}
source_snapshot:
  repository_root: /Users/muhammed/Documents/GitHub/notebook
  branch: dev
  HEAD: d733eeb037a517634ecc37e8b19c8421c2d20530
  files:
    - {path: AGENTS.md, sha256: f2442e1e2805baeea57b00a75466310245a0bf35c3dae76473a04539b8e343c3}
    - {path: docs/00_Core.md, sha256: 96787a64585264e9f0d6beb1aab28bc717f80436003dfc6c093736541a95c34c}
    - {path: docs/03_Development.md, sha256: 251730eb5cdab9776a97caf29a6791e1f3645fa6b8f01c6de93c5c4a2bbed9b1}
    - {path: docs/04_Lessons.md, sha256: e1edd62ec22f109a2b99ac7c4417e5ce94e4e9a0d0ed4c90161a05670d98e1b6}
    - {path: docs/06_Features.md, sha256: 4f6f0e02bc0f89d6f5707111b675962657872e27f29d83389fc8e07caf547cdd}
    - {path: docs/ideas/AOS_Documentation_Agent_Routing_R1.md, sha256: 5e7519963495e4e2a65660dbdcabcc21f60e10312f9c3e1550abbcfa47632cf3}
    - {path: docs/superpowers/plans/2026-07-30-aos-documentation-agent-routing.md, sha256: 8812b373a3513e913c125438f30622956f17dc8c90fb951de940708698c28330}
    - {path: .codex/config.toml, sha256: d8d66986cd2c609ac2603193271b51aace88e4b0096d045332b301ce67b59e22}
    - {path: .codex/agents/contract-analyst.toml, sha256: da7dc0fc6b9af6a7d3b30f8a1347a99643e636c6c358701884635fe105e89abc}
    - {path: .codex/agents/mechanical-checker.toml, sha256: cc8006cd2b73135bc53bb820b0b6217b3ec912f3eb2447709e2b68f18de30b10}
    - {path: .codex/agents/reference-explorer.toml, sha256: 2ff0cd9503ae91a202ea6710ecdd4bbcd14dd0a1ea5ad539147f745bfd2218e6}
    - {path: .codex/agents/semantic-reviewer.toml, sha256: 7a082f510b59529d5f07e95d7a8ff2dd98b5b000b21b8bfa3cf9f9ca8fc7dd3f}
archived_reason: SUPERSEDED_BY_SIMPLIFIED_PLANNING_MODEL
---

# AOS Documentation Routing R3 — Reliability First

## 1. Status and decision boundary

This specification records the approved design for a reliability-first revision
of the AOS documentation-agent routing package. It is a design artifact, not an
active routing configuration or an implementation authorization.

The design direction was approved incrementally in the current human dialogue:

1. reliability is the primary optimization target;
2. the exact Stage Report uses a repository-relative immutable artifact;
3. `contract_analyst` is mandatory for a closed trigger set;
4. Stage Reports use the run-scoped namespace defined below;
5. historical closed Evidence is not migrated;
6. the initially selected instruction-only implementation approach was later
   superseded by the exact human architecture decision
   `DETERMINISTIC_EXECUTABLE_HARNESS`;
7. the executable harness plan was accepted with exact SHA-256
   `77ff1093da3462881cb658bf364675c2cc6467ea28fbd21577ffa2d409a00316`;
8. the harness remains repository validation tooling, not AOS product runtime;
   and
9. architecture, failure/recovery, pilot and acceptance sections were confirmed
   by the human before this file-write authorization.

Approval of those design choices does not accept the exact bytes of this newly
written specification. Exact-artifact review remains a separate human gate.

```yaml
design_choice_status: HUMAN_APPROVED_IN_CURRENT_DIALOGUE
exact_artifact_status: DRAFT_CANDIDATE
exact_artifact_human_acceptance: NOT_RUN
active_routing_revision: R2_DRAFT_CANDIDATE
routing_configuration_changed_by_original_design_task: false
routing_harness_candidate: IMPLEMENTED_NOT_VALIDATED
mass_documentation_authoring_authorized: false
implementation_authorization: NONE
git_authorization: NONE
```

## 2. Authoritative context and observed problem

This design specializes, without replacing, the authority and safety rules in
[Core](../../00_Core.md), [Development](../../03_Development.md),
[Lessons](../../04_Lessons.md), [Features](../../06_Features.md), the existing
[routing design](../../ideas/AOS_Documentation_Agent_Routing_R1.md), the
[routing implementation plan](../plans/2026-07-30-aos-documentation-agent-routing.md),
the current [project routing controller](../../../.codex/config.toml), and the
repository [agent instructions](../../../AGENTS.md).

The current R2 pilot architecture has useful boundaries:

- one primary `documentation_architect` is the only writer;
- four specialized roles are read-only;
- concurrency is capped at two subagents;
- automatic runtime model fallback and retry are forbidden;
- technical Evidence does not create human authority; and
- PLAN, EXECUTE, VALIDATE and REVIEW remain separate.

Recent `INT-DOC-210` runs exposed reliability gaps in the operational protocol:

- a long inline Base64 Stage Report was not reliably available to every
  independent verifier;
- `contract_analyst` was omitted even though the subject contained schemas,
  state transitions, recovery and negative cases;
- a Stage Report claimed `PASS` and freeze before a complete semantic/contract
  check had closed; and
- primary synthesis had to normalize reviewer verdicts and manually relay
  Evidence.

These are protocol failures, not evidence that multi-agent routing should become
autonomous or acquire more authority.

## 3. Goals

R3 must:

1. make exact Stage Report bytes independently retrievable without chat history;
2. make contract-heavy pre-freeze review deterministic rather than discretionary;
3. prevent false `PASS` and false `final_candidate_frozen: true`;
4. preserve exactly one writer and at most two concurrent read-only subagents;
5. keep the aggregate technical verdict owned by the primary agent;
6. invalidate stale reviewer Evidence when candidate bytes change;
7. fail closed on unavailable reviewers, collisions, drift and unresolved conflict;
8. preserve task-local correction budgets and human decision boundaries;
9. enable a cold-start validator to bind candidate and Stage Report by exact
   repository-relative paths and hashes; and
10. remain harness-assisted, pilot-only and inactive until separately validated,
    safe-piloted, accepted and activated.

## 4. Non-goals

R3 does not:

- create runtime AOS code, CI/CD, hooks, services, databases or schemas;
- make multi-agent routing mandatory for all work;
- add a second documentation writer;
- authorize configuration edits through this specification;
- introduce automatic model fallback, automatic retry or nested delegation;
- infer product, architecture, dependency, Risk Profile or human acceptance;
- migrate, rewrite or synthesize missing historical Stage Reports;
- replace `planning/CURRENT.md` as lifecycle-state owner;
- authorize mass documentation authoring;
- measure or claim cost savings; or
- authorize Commit, Push, Merge or Release.

## 5. Reliability-first architecture

### 5.1 End-to-end flow

```text
separately authorized documentation EXECUTE
→ primary verifies task, subject, allowlist and report-path preconditions
→ primary drafts or corrects the candidate
→ primary performs deterministic trigger scan
→ primary uses the deterministic harness to bind the candidate manifest and
  validate every required request envelope before dispatch
→ mechanical_checker and contract_analyst run in parallel when both are required
→ semantic_reviewer runs sequentially when semantic triggers apply
→ primary uses the harness to reject stale or malformed reviewer results and
  normalized gate records before semantic consumption
→ primary verifies provenance, normalizes findings and resolves bounded conflicts
→ primary corrects only authorized in-scope technical findings
→ candidate change invalidates affected reviewer gates
→ primary repeats every invalidated required gate
→ primary evaluates freeze eligibility
→ primary freezes exact candidate bytes
→ primary rechecks report-path absence and invokes the one authorized
  exclusive-create Stage Report operation
→ terminal EXECUTE report and STOP
→ separately authorized read-only VALIDATE
→ validator reads candidate and Stage Report from exact paths and hashes
→ Verification Report and STOP
→ exact human decision
```

Only the primary thread may mutate the candidate or create the Stage Report.
Subagents return Evidence and findings; they never write, correct, freeze,
aggregate the overall result or make a human decision.

### 5.2 Components

| Component | Responsibility | Mutation authority |
|---|---|---|
| `documentation_architect` | Task binding, routing, synthesis, bounded corrections, freeze decision, Stage Report | Only exact human-authorized paths |
| deterministic executable harness | Byte-exact manifest, envelope/result/gate validation, canonical Stage Report create/verify | Read-only except one exact primary-authorized exclusive create |
| `mechanical_checker` | IDs, links, fences, manifests, hashes, counts and structural comparisons | None |
| `contract_analyst` | Schemas, transitions, failure/recovery, acceptance logic and negative cases | None |
| `semantic_reviewer` | Cross-document consistency, provenance, authority, readiness and handoff | None |
| `reference_explorer` | Exact repository/ref/commit/path research for a declared knowledge gap | None |
| post-stop validator | Independent candidate/report validation and zero-write Evidence | None |

The existing static model bindings remain unchanged by this design. In
particular, `mechanical_checker` remains statically configured to
`gpt-5.6-luna` because Spark was absent from the configuration-time catalog.
This is not a runtime fallback.

## 6. Deterministic routing and scheduling

### 6.1 Closed reviewer triggers

`mechanical_checker` is required before freeze when the output has any declared
path, ID inventory, link, fence, YAML/TOML structure, manifest, checksum,
subject-set identity, exact count or allowlist invariant. A documentation
candidate with a byte-bound freeze therefore normally requires this gate.

`contract_analyst` is required when the exact subject contains at least one of:

- a state machine or lifecycle transition;
- a schema or named contract;
- failure or recovery behavior;
- negative cases or negative fixtures;
- acceptance aggregation or readiness logic; or
- a portable handoff or task-conversion contract.

`semantic_reviewer` is required when the exact subject contains at least one of:

- cross-document provenance or owner traceability;
- authority or status boundaries;
- `PASS`, readiness or freeze claims;
- a portable handoff; or
- a downstream gate whose usability depends on multiple sources.

`reference_explorer` is required only for an explicit, bounded knowledge gap
that names the repository/ref/commit/path boundary to be inspected. It is not a
default reviewer and reference availability never grants authority.

If the trigger scan is ambiguous for a material gate, the gate is required.
Primary discretion may add a read-only gate, but may not omit a triggered gate.

### 6.2 Scheduling

```yaml
primary_writer_threads: 1
max_concurrent_subagents: 2
max_delegation_depth: 1
subagent_retry_limit_per_request: 0
automatic_runtime_fallback_limit_per_request: 0
```

When both are required and their source boundaries are independent,
`mechanical_checker` and `contract_analyst` run in parallel. The
`semantic_reviewer` runs after their results because it may consume their
Evidence and must review the primary's normalized candidate state.

If `reference_explorer` is required, it occupies one of the two available
subagent slots. The primary schedules remaining gates without exceeding the cap;
latency never justifies a third concurrent subagent.

### 6.3 Request and result boundaries

Every subagent request remains bound to:

```yaml
task_id: REQUIRED
request_id: REQUIRED
parent_task_id: REQUIRED
task_class: REQUIRED
role: REQUIRED
exact_subject: REQUIRED
subject_sha256: REQUIRED_LOWERCASE_64_HEX
source_boundary: REQUIRED
invariant_semantics: REQUIRED_FOR_EACH_DECLARED_DETERMINISTIC_INVARIANT
method_contract:
  preflight_observed_capability: REQUIRED_FOR_TOOL_OR_PARSER_DEPENDENT_CHECK
  exact_algorithm_or_command: REQUIRED
  expected_success_shape: REQUIRED
  forbidden_substitutions: REQUIRED
required_output_fields: REQUIRED
stop_conditions: REQUIRED
allowed_operations: [READ]
forbidden_operations: [WRITE, COMMIT, PUSH, MERGE, RELEASE, NESTED_DELEGATION]
retry_limit: 0
```

Every reviewer result must preserve sources, methods, `temporal_scope`,
classified claims, conflicts, unknowns, recommendations, checks run/not run,
limitations, model binding, repository mutations, Git operations, `result`,
`reason_code`, one next action and `stop: true`. For reviewer Evidence,
`temporal_scope` is a required non-empty scalar whose value is either
`CURRENT_SNAPSHOT` or an exact bounded interval in the form
`<start-ISO-8601>/<end-ISO-8601>`. A missing, empty or differently formed value
makes the reviewer Evidence contract-invalid. The primary rejects incomplete
reviewer Evidence rather than silently completing it.

For every deterministic inventory, exact-count, parser or structural check,
the request must define the unit being counted or parsed in
`invariant_semantics` and bind the allowed implementation in `method_contract`.
A request that omits either field is contract-invalid before dispatch; repairing
that unsent envelope is not a reviewer retry and does not mutate candidate bytes.

The repository-wide ID invariant is interpreted structurally:

```yaml
FTR-001..030:
  accepted_inventory_row: EXACTLY_ONE_PER_ID
  dossier_heading: EXACTLY_ONE_LEVEL_2_FTR_HEADING_PER_ID
  feature_id_definition: EXACTLY_ONE_PER_ID
  referential_mentions: EXCLUDED_FROM_DUPLICATE_COUNT
LES-001..042:
  lesson_heading: EXACTLY_ONE_LEVEL_3_LES_HEADING_PER_ID
  referential_mentions: EXCLUDED_FROM_DUPLICATE_COUNT
```

For YAML/TOML parsing, the primary first observes an available read-only parser
or strict configuration command and names that exact capability in the request.
Absence of a preferred-but-unrequired dependency is not a subject finding and
must not turn valid bytes into `FAIL`. If the named capability is unavailable at
review time, the gate returns `BLOCKED` with
`BLOCKED_REQUIRED_REVIEW_CAPABILITY`; it does not substitute another parser or
claim that the subject is invalid.

### 6.3.1 Deterministic executable harness boundary

The repository-local standard-library CLI at `tools/routing_r3_harness.py`
implements the deterministic boundary selected by the human. Its closed command
surface is:

```text
manifest
check-request
check-result
check-gate
create-stage-report
verify-stage-report
```

`manifest`, `check-request`, `check-result`, `check-gate`, and
`verify-stage-report` are read-only. `create-stage-report` is available only to
the primary writer inside an exact `EXECUTE` authorization that names the one
output path. It uses exclusive creation, rejects symlinked paths, never
overwrites a collision, re-reads the new bytes, and returns exact length and
SHA-256.

The harness validates deterministic Evidence; it never dispatches reviewers,
judges semantics, assigns human authority, computes the aggregate readiness
verdict, accepts or activates R3, or performs Git operations. Required model
gates therefore remain required. Harness `PASS` is Evidence, not package
validation or acceptance.

Every subject manifest record is byte-exact and sorted by UTF-8 path bytes:

```text
<lowercase-file-sha256><SP><SP><decimal-byte-length><SP><SP><normalized-path><LF>
```

The harness rejects empty, absolute, non-NFC, duplicated or ambiguous paths,
backslashes, control bytes, `.`/`..`, symlink subjects and symlink ancestors.
It emits one canonical JSON object per operation; Stage Report JSON is rendered
with sorted keys, compact separators, UTF-8, and one terminal LF, producing
bytes that are also valid YAML 1.2.

### 6.4 Closed result algebra

Technical result and lifecycle status are separate axes. Reviewer results,
normalized gate records and Stage Reports use this closed technical result enum:

```yaml
result: PASS | FAIL | BLOCKED | CONFLICT | UNKNOWN | NOT_RUN | CONTRACT_VIOLATION
```

Every result also carries exactly one value from this closed reason enum:

```yaml
reason_code:
  - NONE
  - REVIEWER_EVIDENCE_CONFLICT
  - BLOCKED_REQUIRED_REVIEW_CAPABILITY
  - BLOCKED_STAGE_REPORT_PATH_COLLISION
  - BLOCKED_HUMAN_DECISION_REQUIRED
  - BLOCKED_UNRESOLVED_CONFLICT
  - BLOCKED_REFERENCE_ACCESS
  - BLOCKED_SUBJECT_IDENTITY_MISMATCH
  - BLOCKED_SCOPE_OR_PROVENANCE
  - BLOCKED_VALIDATION_SUBJECT_MISMATCH
  - BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH
```

The mapping is deterministic:

- `CONFLICT` requires `REVIEWER_EVIDENCE_CONFLICT`;
- `BLOCKED` requires one `BLOCKED_*` value from the closed enum;
- every other result requires `NONE`;
- a missing, unknown or incompatible result/reason pair is a
  `CONTRACT_VIOLATION`.

`DRAFT_CANDIDATE`, accepted/active state and other lifecycle labels never appear
in `result`. A successful authoring EXECUTE may report `result: PASS` while the
artifact independently remains `lifecycle_status: DRAFT_CANDIDATE`.

### 6.5 Defect origin and harness-loop breaker

Every non-PASS deterministic finding is classified on a separate origin axis:

```yaml
finding_origin: SUBJECT_DEFECT | REQUEST_OR_CHECKER_DEFECT
```

`SUBJECT_DEFECT` requires Evidence that current subject bytes violate the bound
`invariant_semantics` using the bound `method_contract`; only this origin may
route to candidate correction. `REQUEST_OR_CHECKER_DEFECT` covers an incomplete
envelope, a forbidden substitution, an unexecuted required method, or a checker
conclusion that contradicts its bound method. It normalizes to
`CONTRACT_VIOLATION` with `reason_code: NONE`, preserves candidate bytes, and
routes only to validator-harness correction.

One exact human authorization may permit at most one validator-harness
correction followed by one fresh request with a new `request_id`. Same-request
retry remains zero. If that fresh request again produces
`REQUEST_OR_CHECKER_DEFECT`, the harness-correction budget is exhausted: the
stage aggregate is `FAIL` with `reason_code: NONE`, the exact next human choice
is `DEFER_OR_REDESIGN_VALIDATOR`, and another finding-specific recovery request
must not be recommended.

## 7. Immutable Stage Report transport

### 7.0 Pre-activation bootstrap transport

This R3 package cannot use its own active transport before validation,
safe-pilot acceptance and activation. The deterministic-harness implementation
therefore uses one separately authorized bootstrap report under the already
active post-stop validation boundary:

```text
planning/verification/bootstrap/routing-r3-harness/<execution_id>/stage-report.yaml
```

The bootstrap profile is `PRE_R3_BOOTSTRAP`. It is bound to one exact execution
identity and allowlist, follows the same absent-before-write, regular-file,
exclusive-create, length and SHA-256 rules, and is a separate validation
subject. It does not activate R3, does not authorize the active namespace, and
must never migrate, recreate or backfill a historical inline Stage Report.

### 7.1 Run-scoped namespace

Only after exact package acceptance and activation, an R3-governed
documentation EXECUTE uses:

```text
planning/verification/runs/<task_id>/<execution_id>/stage-report.yaml
```

`<task_id>` and `<execution_id>` are syntax parameters supplied by the exact
task and authorization records. They are not unresolved design placeholders.
Each component must satisfy repository-relative path rules and must not contain
an empty component, `.`, `..`, a slash, backslash, control byte or ambiguous
normalization.

### 7.2 Creation contract

The Stage Report path:

1. is included in the exact EXECUTE allowlist together with the candidate path;
2. must be absent during preflight;
3. is rechecked immediately before creation;
4. is created only by the primary writer after candidate freeze;
5. must be a new regular file, not a symlink or nested repository path;
6. is never overwritten, amended, reused or deleted by routing recovery;
7. receives an exact byte length and SHA-256 in the terminal response; and
8. becomes part of the separate validation subject.

Repository-relative immutability is a workflow invariant, not a claim that the
filesystem is cryptographically immutable. Any later byte change invalidates
the Stage Report identity and every validation bound to it.

### 7.3 Collision and correction behavior

If the path exists at preflight or immediately before creation, the operation
returns `result: BLOCKED` with
`reason_code: BLOCKED_STAGE_REPORT_PATH_COLLISION`. It does not inspect, overwrite,
reuse, rename or delete the existing artifact.

Every separately authorized correction EXECUTE receives a new `execution_id`
and therefore a new Stage Report path. Earlier reports remain historical
Evidence. A new report references predecessor identities but never replaces
their bytes.

### 7.4 Validation transport

Validation binds exactly one declared transport profile. Package bootstrap
validation receives the exact `PRE_R3_BOOTSTRAP` path; validation of a later
accepted-and-active R3 run receives:

```yaml
candidate:
  path: REPOSITORY_RELATIVE_PATH
  byte_length: POSITIVE_INTEGER
  sha256: LOWERCASE_64_HEX
  subject_set_sha256: LOWERCASE_64_HEX
stage_report:
  representation: REPOSITORY_RELATIVE_PATH
  path: planning/verification/runs/<task_id>/<execution_id>/stage-report.yaml
  byte_length: POSITIVE_INTEGER
  sha256: LOWERCASE_64_HEX
```

Inline Base64 may be displayed as a convenience copy only when a later contract
explicitly permits it. It is not the sole canonical transport for an R3 run.
If both path and inline forms are supplied, exact byte equality is required.
The validator reads the repository file directly and must not reconstruct either
profile from chat text.

## 8. Gate aggregation and freeze eligibility

### 8.1 Gate record

Each required gate produces a primary-normalized record:

```yaml
gate_id: STABLE_ID
required: true
role: mechanical_checker | contract_analyst | semantic_reviewer | reference_explorer | primary
request_id: EXACT_REQUEST_ID
subject_sha256: LOWERCASE_64_HEX
source_boundary: []
result: PASS | FAIL | BLOCKED | CONFLICT | UNKNOWN | NOT_RUN | CONTRACT_VIOLATION
reason_code: CLOSED_ENUM_VALUE
finding_ids: []
limitations: []
repository_mutations: 0
stop: true
```

Subagent-local result wording does not become the aggregate outcome. The
primary checks the result contract and computes the aggregate from all required
gate records.

### 8.2 Freeze predicate

`PASS` and `final_candidate_frozen: true` are permitted only when:

```text
all required gates exist
AND every required gate result = PASS
AND unresolved material findings = []
AND required NOT_RUN/UNKNOWN/CONFLICT/BLOCKED/FAIL/CONTRACT_VIOLATION = absent
AND every gate is bound to the current candidate SHA-256
AND candidate bytes are unchanged after the final required gate
AND Stage Report path was absent at preflight
AND Stage Report path remains absent immediately before creation
```

Any false `PASS`, missing required gate or contradictory freeze claim is a
`CONTRACT_VIOLATION`, not a warning.

### 8.3 Candidate drift and invalidation

Every gate records the candidate SHA-256 it reviewed. After a bounded correction:

- gates whose subject or derived Evidence changed are invalidated;
- gates depending on an invalidated result are also invalidated;
- if dependency impact cannot be proven narrowly, all required gates are
  invalidated; and
- freeze evaluation cannot use a gate bound to older bytes.

The task-local contract remains the owner of the permitted correction budget.
R3 neither increases that budget nor treats a new reviewer request after a
candidate correction as retrying the terminal subagent request. When the
task-local correction budget is exhausted, the EXECUTE result is `FAIL`.

## 9. Failure, conflict and recovery

| Condition | `result` | `reason_code` | Recovery boundary |
|---|---|---|---|
| Required reviewer unavailable or materially insufficient | `BLOCKED` | `BLOCKED_REQUIRED_REVIEW_CAPABILITY` | New explicit request; no same-request fallback |
| Stage Report path exists | `BLOCKED` | `BLOCKED_STAGE_REPORT_PATH_COLLISION` | New authorization and execution identity |
| Candidate changes after a gate | `NOT_RUN` for invalidated gates | `NONE` | Rerun invalidated gates within task-local budget |
| Current candidate bytes violate bound invariant (`SUBJECT_DEFECT`) | `FAIL` until corrected | `NONE` | Primary bounded candidate correction, then repeat affected gates |
| Request/checker violates assertion envelope (`REQUEST_OR_CHECKER_DEFECT`) | `CONTRACT_VIOLATION` | `NONE` | Preserve candidate; validator-harness correction only |
| Fresh request repeats `REQUEST_OR_CHECKER_DEFECT` after one authorized harness correction | `FAIL` | `NONE` | Stop; exact next human choice `DEFER_OR_REDESIGN_VALIDATOR` |
| Product/architecture/authority decision required | `BLOCKED` | `BLOCKED_HUMAN_DECISION_REQUIRED` | Exact human decision |
| Reviewer results conflict | `CONFLICT` | `REVIEWER_EVIDENCE_CONFLICT` | One bounded primary conflict review |
| Material conflict remains unresolved | `BLOCKED` | `BLOCKED_UNRESOLVED_CONFLICT` | Human resolution or new scoped Evidence |
| Correction budget exhausted | `FAIL` | `NONE` | New separately authorized correction task |
| Subagent writes, expands scope, retries or delegates | `CONTRACT_VIOLATION` | `NONE` | Preserve Evidence and stop |
| VALIDATE finds a defect | `FAIL` | `NONE` | Separate correction EXECUTE; validator never edits |

No recovery route increases permissions, selects a replacement model, mutates
historical Evidence or starts the next stage automatically.

## 10. Primary-only synthesis

The primary agent must, before using subagent Evidence:

1. verify task/request/parent identifiers;
2. verify role and configured model binding;
3. verify exact subject and source boundary;
4. verify sources, methods and temporal scope;
5. reject missing required output fields;
6. compare findings for duplicates and contradictions;
7. preserve `UNKNOWN`, `NOT_RUN`, `CONFLICT` and limitations;
8. map each accepted finding to a stable ID and affected gate; and
9. compute the aggregate result using the freeze predicate.

Model prestige, confidence, majority vote and consensus never resolve authority
or replace Evidence.

## 11. Validation and safe pilot

### 11.1 Static validation

An R3 package cannot be proposed for acceptance until a separate read-only
validation proves:

- design/configuration/agent-instruction parity;
- valid TOML and required custom-agent schemas;
- exactly one writer and read-only specialist roles;
- `max_threads = 2` and no nested delegation;
- closed contract and semantic trigger sets;
- primary-only aggregate verdict;
- exact Stage Report namespace and absent-before-write rules;
- collision blocking and overwrite prohibition;
- required reviewer omission prevents `PASS`;
- candidate drift invalidates stale gates;
- required non-PASS states prevent freeze;
- no automatic fallback or retry; and
- no implementation or Git authority.

### 11.2 Pilot cases

The safe pilot is read-only and includes:

1. contract-heavy routing to `contract_analyst`;
2. deterministic structure routing to `mechanical_checker`;
3. provenance/readiness routing to `semantic_reviewer`;
4. one exact targeted question for `reference_explorer`;
5. false-PASS/freeze rejection;
6. Stage Report collision rejection;
7. required-reviewer-unavailable behavior;
8. candidate-drift invalidation;
9. conflicting reviewer Evidence; and
10. zero repository mutations by every reviewer and validator.

The approval-time regression target was the pre-correction `INT-DOC-210`
candidate with SHA-256
`38a2e1a58e4baaa5f96ab32e5d450cbc49cca2f75008c124715ebd6b1be7176c`
and findings F002–F005. At specification authoring, those exact candidate bytes
are not present at the active candidate path. R3 must not reconstruct them from
chat memory or claim the regression reproduced. A pilot may use those bytes
only if they are supplied as an exact immutable fixture under a separate
authorization; otherwise it uses a separately authorized safe negative fixture
with equivalent contract failures.

### 11.3 Pilot acceptance

Pilot success requires:

```yaml
static_checks: PASS
positive_routes: PASS
negative_routes: PASS
required_reviewer_omissions: 0
false_pass_or_freeze: 0
repository_mutations_by_subagents: 0
nested_delegations: 0
automatic_runtime_fallbacks: 0
same_request_retries: 0
scope_expansions: 0
authority_changes: 0
human_acceptance: NOT_RUN
```

Cost, latency and savings remain `NOT_MEASURED` unless a separate measurement
stage compares exact representative tasks against a bound baseline.

## 12. Planned implementation surface

The human-selected implementation is a bounded deterministic harness plus its
contract integration:

```text
tools/routing_r3_harness.py
tests/test_routing_r3_harness.py
docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md
docs/superpowers/plans/2026-08-02-aos-documentation-routing-r3-reliability-first.md
docs/superpowers/plans/2026-08-03-aos-documentation-routing-r3-deterministic-executable-harness.md
docs/ideas/AOS_Documentation_Agent_Routing_R1.md  → frontmatter revision R3
.codex/config.toml
.codex/agents/mechanical-checker.toml
.codex/agents/reference-explorer.toml
.codex/agents/contract-analyst.toml
.codex/agents/semantic-reviewer.toml
```

The four `.codex/agents/*.toml` files are parity-checked read-only inputs unless
a concrete later defect receives a separately expanded allowlist. The current
harness implementation authorization permits only the exact code/test,
design/supersession/routing/config paths and one bootstrap Stage Report path.
It does not materialize `planning/verification/runs/`; that active namespace is
available only after package acceptance/activation to a separately authorized
R3-governed run.

The Python CLI is repository validation tooling, not AOS product runtime code.
No product code, CI/CD, schema owner, database or top-level knowledge catalog is
added. Its bytes and contract integration remain `DRAFT_CANDIDATE` until
separate static validation, safe pilot, exact acceptance and activation.

## 13. Applicability and temporal reconciliation

The approved design selected the then-unclosed `INT-DOC-210` and future runs as
the intended applicability boundary, with no historical backfill. That choice
does not retroactively activate R3.

Since the design dialogue, `INT-DOC-210-CORRECTION-001` ran under the existing
boundary and emitted an inline Stage Report before this R3 specification was
written or accepted. That report is historical Evidence and is not migrated.

R3 may govern a remaining or future `INT-DOC-210` run only after all of these
separate gates close:

```text
exact R3 design artifact human review
→ separately authorized deterministic harness and configuration integration
→ separate package validation
→ safe routing pilot
→ exact hash-bound R3 package human acceptance/activation
→ separately authorized task run whose paths use the R3 contract
```

Until then, the R3 candidate has no active operational authority. Presence of
the harness or configuration bytes does not activate routing.

## 14. Design acceptance criteria

This exact design specification is review-ready when:

1. the one-writer and two-read-only-reviewer boundary is explicit;
2. immutable Stage Report path, creation, collision and validation rules are
   deterministic;
3. contract and semantic triggers form closed mandatory sets;
4. primary-only aggregation and freeze predicate are explicit;
5. candidate drift and gate invalidation are explicit;
6. correction budgets remain task-local and subagent retry remains zero;
7. failures, conflicts and recovery stop conditions are closed;
8. technical results include `CONFLICT`, typed blockers use a mandatory closed
   `reason_code`, and lifecycle status is a separate axis;
9. static and pilot checks include positive and negative cases;
10. current/historical `INT-DOC-210` Evidence is reconciled without migration;
11. implementation surface is bounded to the exact harness, tests, routing
    contracts/configuration and one bootstrap Stage Report;
12. repository validation tooling remains distinct from AOS product runtime,
    acceptance, activation and Git authority;
    and
13. the exact written bytes receive separate human review.

## 15. Self-review result

The authoring self-review must check the final file for:

- unresolved drafting or placeholder markers;
- contradictory writer, concurrency, fallback, retry or stage rules;
- ambiguous Stage Report creation and collision behavior;
- unrepresentable conflict/blocker outcomes or lifecycle labels used as results;
- accidental configuration or implementation authorization;
- scope expansion beyond the single authorized specification path;
- broken relative links, malformed frontmatter or unbalanced fences; and
- false claims that the R3 package, pilot or `INT-DOC-210` migration already
  occurred.

The terminal EXECUTE report records the observed result. Self-review is not
independent validation or human acceptance.

## 16. Current outcome and stop

```yaml
task_id: ROUTING-R3-DETERMINISTIC-HARNESS
stage: EXECUTE
artifact_status: DRAFT_CANDIDATE
design_scope: RELIABILITY_FIRST_ROUTING_R3
routing_harness_architecture: DETERMINISTIC_EXECUTABLE_HARNESS
routing_harness_candidate: IMPLEMENTED_NOT_INDEPENDENTLY_VALIDATED
routing_configuration_mutation: BOUNDED_EXECUTE
runtime_implementation: NOT_RUN
independent_validation: NOT_RUN
safe_pilot: NOT_RUN
human_acceptance_of_exact_artifact: NOT_RUN
activation: NOT_RUN
mass_documentation_authoring_authorized: false
Git_operations:
  add: NOT_RUN
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: AUTHORIZE_SEPARATE_ROUTING_R3_HARNESS_PACKAGE_VALIDATE
stop: true
```
