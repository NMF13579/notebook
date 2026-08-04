# AOS Documentation Routing R3 — Reliability First Implementation Plan (Superseded Mechanical Approach)

> **Supersession boundary — 2026-08-03:** The instruction-only/no-script
> mechanical approach in this file is superseded by the human-selected
> `DETERMINISTIC_EXECUTABLE_HARNESS`. The normative implementation plan is
> [AOS Documentation Routing R3 Deterministic Executable Harness Implementation
> Plan](2026-08-03-aos-documentation-routing-r3-deterministic-executable-harness.md),
> accepted at SHA-256
> `77ff1093da3462881cb658bf364675c2cc6467ea28fbd21577ffa2d409a00316`.
> Content below remains historical/provenance Evidence and may be used only
> where it does not conflict with the newer plan. It does not authorize work.

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. `superpowers:subagent-driven-development` is not permitted for implementation because the accepted design requires `SINGLE_WRITER`; subagents may perform only bounded, independent, read-only review or pilot requests explicitly scheduled by this plan.

**Historical goal:** Upgrade the existing pilot-only AOS documentation-routing package from R2 to the accepted reliability-first R3 contract, prove its static configuration and safe routing behavior, and leave exact package acceptance and activation to a separate human decision.

**Superseded architecture:** The primary `documentation_architect` remains the only writer and aggregate-verdict owner, but instruction-only mechanical enforcement was rejected after repeated transport/checker-envelope failures. The newer accepted plan adds the bounded executable harness while retaining every model-review, validation, acceptance, activation and Git boundary.

**Tech Stack:** Markdown, TOML 1.0, project-scoped Codex configuration, existing Codex custom-agent definitions, POSIX shell, Ruby standard library (`Digest`, `YAML`, `Pathname`), and the installed Codex CLI configuration parser.

## Global Constraints

- Repository: `NMF13579/notebook` at `/Users/muhammed/Documents/GitHub/notebook`.
- Plan-authoring branch and HEAD: `dev` at `d733eeb037a517634ecc37e8b19c8421c2d20530`.
- Predecessor human-accepted design: [AOS Documentation Routing R3 — Reliability First](../specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md), SHA-256 `0da5daa611e5aa2b9c1c965f7b41944b5160a81e76f9cd7f6fa6f2781a684cdf`.
- Current reconciled design candidate SHA-256: `40593088275aaddafb233562e58fa824035bb0317f9d2f8ec128e5449be72ebc`; human acceptance of these reconciled bytes is `NOT_RUN`.
- Result-algebra decision SHA-256: `d520c8d6d8866f088fa4162ce31e0cfe69c4f66961ca8df73a3b593bc431d48e`.
- Accepted design subject-set SHA-256: `c74bfd4c3a358607ee0131f608695e5fb4e731a545ad34f5768deb0bf0ce821e`.
- Exact-artifact acceptance decision SHA-256: `1a4a7f4988a3f43a67b2b44ac2bff61f902bb93d754b0cdc6f690407771e91b8`.
- Plan-authoring authorization SHA-256: `8eb5acbcb16362b3183c6c93442a17cda180ad4f80eee86e12739a53ba15b26d`, calculated over the 585 UTF-8 bytes of the exact visible authorization.
- Repository role remains `ACTIVE_PROJECT_KNOWLEDGE_REPOSITORY`; runtime AOS code is forbidden here.
- The R3 package remains `DRAFT_CANDIDATE` until exact hash-bound human acceptance and activation after static validation and the safe pilot.
- Primary thread role: `documentation_architect`; primary-writer count: exactly one.
- Maximum concurrent read-only subagents: two. Maximum delegation depth: one.
- Subagent same-request retry limit: zero. Automatic runtime model fallback limit: zero.
- Validator-harness correction budget per exact human authorization: one; a repeated harness defect terminates with `FAIL/NONE` and `DEFER_OR_REDESIGN_VALIDATOR` instead of another per-finding recovery.
- The static `mechanical_checker` binding remains `gpt-5.6-luna`; it is a configuration-time binding because Spark was absent from the relevant model catalog, not a runtime fallback.
- The historical six-file/no-script surface below is superseded. The exact current harness surface is owned by the 2026-08-03 plan and its separate implementation authorization; product runtime code, schemas, databases, CI/CD, hooks, plugins, catalogs and product packages remain forbidden.
- Canonical files `docs/00_Core.md` through `docs/06_Features.md`, `AGENTS.md`, `planning/CURRENT.md`, and all existing task-local planning artifacts are out of implementation scope.
- `planning/verification/runs/` is not materialized by the routing-package update. That namespace is used only by a later, separately authorized R3-governed documentation `EXECUTE` whose exact allowlist includes a new run-scoped Stage Report path.
- Documentation/configuration mutation, independent `VALIDATE`, safe pilot execution, package acceptance/activation, and each Git operation require their own exact authority.
- `Edit ≠ Commit ≠ Push ≠ Merge ≠ Release`. All Git mutation operations remain `NOT_RUN` throughout this plan unless a later exact Git authorization names the precise action and subject.
- Every stage ends with one report, one `next_required_action`, and `stop: true`; no stage starts its successor automatically.
- The predecessor design contains a repeated prose line in section 6.1. It is unrelated to this result-algebra correction; the current corrected design candidate is the binding technical source for the corrected package.

## Plan-authoring Boundary

This plan was authorized only for:

```yaml
task_id: ROUTING-R3-IMPLEMENTATION-PLAN-EXECUTE-001
stage: EXECUTE
operation: WRITE_IMPLEMENTATION_PLAN_AND_SELF_REVIEW_ONLY
allowed_paths:
  - docs/superpowers/plans/2026-08-02-aos-documentation-routing-r3-reliability-first.md
routing_configuration_mutation: FORBIDDEN
Git_operations:
  commit: FORBIDDEN
  push: FORBIDDEN
  merge: FORBIDDEN
  release: FORBIDDEN
one_shot: true
```

Writing this plan does not authorize any task below. A later implementation authorization must bind the accepted design hash, this plan hash, the exact six target paths, current target hashes, correction budget, and stop conditions.

## Authoritative Inputs and Precedence

Apply the following precedence during implementation:

1. current explicit human authorization and decisions;
2. repository [Core](../../00_Core.md) and [AGENTS.md](../../../AGENTS.md) boundaries;
3. the exact current corrected R3 design candidate hash named above;
4. this implementation plan;
5. the existing R2 routing design and configuration as implementation baselines only.

If a lower-precedence source conflicts with a higher-precedence source, preserve the conflict, stop the affected stage, and request one bounded human decision. Do not silently reconcile product, architecture, authority, or scope.

## Historical File Map (Do Not Execute)

| Path | Starting SHA-256 | R3 responsibility |
|---|---|---|
| `docs/ideas/AOS_Documentation_Agent_Routing_R1.md` | `5e7519963495e4e2a65660dbdcabcc21f60e10312f9c3e1550abbcfa47632cf3` | Upgrade the routing contract owner from revision R2 to revision R3 and bind it to the accepted reliability-first design. |
| `.codex/config.toml` | `d8d66986cd2c609ac2603193271b51aace88e4b0096d045332b301ce67b59e22` | Encode primary routing, deterministic triggers, scheduling, aggregation, freeze, Stage Report, recovery, and authority rules. |
| `.codex/agents/mechanical-checker.toml` | `cc8006cd2b73135bc53bb820b0b6217b3ec912f3eb2447709e2b68f18de30b10` | Define the candidate-bound deterministic mechanical gate without aggregate authority. |
| `.codex/agents/contract-analyst.toml` | `da7dc0fc6b9af6a7d3b30f8a1347a99643e636c6c358701884635fe105e89abc` | Define the mandatory contract gate for the closed trigger set and fail-closed findings. |
| `.codex/agents/semantic-reviewer.toml` | `7a082f510b59529d5f07e95d7a8ff2dd98b5b000b21b8bfa3cf9f9ca8fc7dd3f` | Define the sequential semantic gate over current candidate bytes and normalized upstream Evidence. |
| `.codex/agents/reference-explorer.toml` | `2ff0cd9503ae91a202ea6710ecdd4bbcd14dd0a1ea5ad539147f745bfd2218e6` | Define the non-default, exact repository/ref/commit/path research gate. |

These starting hashes are historical observations, not current baselines or permission to overwrite changed files. The newer deterministic-harness plan and exact implementation authorization own the current allowlist and baselines.

## Required R3 Data Contracts

### Reviewer request contract

Every dispatched request must carry all of these fields:

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

For inventory, exact-count, parser and structural checks, the request must bind
the exact structural unit in `invariant_semantics` and the preflight-observed
read-only capability in `method_contract`. Missing fields invalidate the request
before dispatch. Absence of a preferred-but-unrequired dependency is not a
subject finding and cannot be substituted for execution of the named method.

### Reviewer result contract

Every reviewer result must contain:

```yaml
task_id: REQUIRED
request_id: REQUIRED
parent_task_id: REQUIRED
task_class: REQUIRED
role: REQUIRED
model: REQUIRED
reasoning: REQUIRED
exact_subject: REQUIRED
subject_sha256: REQUIRED_LOWERCASE_64_HEX
source_boundary: REQUIRED
sources: REQUIRED
methods: REQUIRED
temporal_scope: REQUIRED_NONEMPTY_CURRENT_SNAPSHOT_OR_EXACT_ISO_8601_INTERVAL
classified_claims: REQUIRED
conflicts: REQUIRED
unknowns: REQUIRED
recommendations: REQUIRED
checks_run: REQUIRED
checks_not_run: REQUIRED
limitations: REQUIRED
model_binding: REQUIRED
repository_mutations: 0
git_operations: REQUIRED_ALL_MUTATIONS_NOT_RUN
result: PASS_OR_FAIL_OR_BLOCKED_OR_CONFLICT_OR_UNKNOWN_OR_NOT_RUN_OR_CONTRACT_VIOLATION
reason_code: REQUIRED_CLOSED_ENUM
next_required_action: REQUIRED_EXACTLY_ONE
stop: true
```

`temporal_scope` is one non-empty scalar: either `CURRENT_SNAPSHOT` or an exact
bounded interval in the form `<start-ISO-8601>/<end-ISO-8601>`. Missing, empty
or differently formed values make the Evidence contract-invalid.

Claim classes are restricted to `OBSERVED_AT_SNAPSHOT`, `REPORTED`, `SYNTHESIZED`, `CONFLICT`, `NOT_FOUND`, `UNKNOWN`, `NOT_RUN`, and `BLOCKED`.

### Primary-normalized gate record

```yaml
gate_id: STABLE_ID
required: true
role: mechanical_checker_or_contract_analyst_or_semantic_reviewer_or_reference_explorer_or_primary
request_id: EXACT_REQUEST_ID
subject_sha256: LOWERCASE_64_HEX
source_boundary: REQUIRED
result: PASS_OR_FAIL_OR_BLOCKED_OR_CONFLICT_OR_UNKNOWN_OR_NOT_RUN_OR_CONTRACT_VIOLATION
reason_code: REQUIRED_CLOSED_ENUM
finding_ids: REQUIRED
limitations: REQUIRED
repository_mutations: 0
stop: true
```

Only the primary validates these records and computes the aggregate outcome.

### Closed result algebra

The closed technical result enum is:

```text
PASS | FAIL | BLOCKED | CONFLICT | UNKNOWN | NOT_RUN | CONTRACT_VIOLATION
```

Every reviewer result, normalized gate record, and Stage Report must include a
mandatory `reason_code` from this closed enum:

```text
NONE
REVIEWER_EVIDENCE_CONFLICT
BLOCKED_REQUIRED_REVIEW_CAPABILITY
BLOCKED_STAGE_REPORT_PATH_COLLISION
BLOCKED_HUMAN_DECISION_REQUIRED
BLOCKED_UNRESOLVED_CONFLICT
BLOCKED_REFERENCE_ACCESS
BLOCKED_SUBJECT_IDENTITY_MISMATCH
BLOCKED_SCOPE_OR_PROVENANCE
BLOCKED_VALIDATION_SUBJECT_MISMATCH
BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH
```

`CONFLICT` requires `REVIEWER_EVIDENCE_CONFLICT`. `BLOCKED` requires exactly one
`BLOCKED_*` reason. Every other result requires `NONE`. A missing, unknown, or
incompatible pair is `CONTRACT_VIOLATION`. Lifecycle labels such as
`DRAFT_CANDIDATE` are never technical results.

---

## Stage A: R3 Package EXECUTE

Stage A is a future documentation/configuration `EXECUTE`. It requires a new exact human authorization. It performs the six-file bounded update, internal checks, and a terminal Stage Report under the currently governing pre-R3 transport. It does not run independent validation, the safe pilot, acceptance, activation, or Git delivery.

### Task 1: Bind Authorization and Preserve the Starting State

**Files:**

- Inspect: `AGENTS.md`
- Inspect: `docs/00_Core.md`
- Inspect: `docs/03_Development.md`
- Inspect: `docs/04_Lessons.md`
- Inspect: accepted design path
- Inspect: this plan
- Inspect: six File Map paths
- Modify: none

- [ ] **Step 1: Verify repository identity and mutable Git facts**

Run:

```bash
git rev-parse --show-toplevel
git branch --show-current
git rev-parse HEAD
git status --short
git diff --cached --name-only
```

Expected:

- repository root equals `/Users/muhammed/Documents/GitHub/notebook`;
- branch and HEAD equal the values bound by the new implementation authorization;
- pre-existing worktree entries are recorded and preserved;
- staging is empty unless the exact new authorization explicitly accepts a non-empty staged baseline.

An identity mismatch returns `result: BLOCKED` with
`reason_code: BLOCKED_SUBJECT_IDENTITY_MISMATCH`. Do not repair or clean the
worktree.

- [ ] **Step 2: Verify accepted design and plan identities**

Run:

```bash
shasum -a 256 \
  docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md \
  docs/superpowers/plans/2026-08-02-aos-documentation-routing-r3-reliability-first.md
```

Expected: the design equals the current corrected design candidate hash named in
Global Constraints; the plan equals the hash named in the new implementation
authorization. Any mismatch returns `result: BLOCKED` with
`reason_code: BLOCKED_SUBJECT_IDENTITY_MISMATCH`.

- [ ] **Step 3: Verify the exact six-path allowlist**

Compare the authorization's normalized allowlist with the six File Map paths. The
set must be equal, not merely a superset. A missing or additional path returns
`result: BLOCKED` with
`reason_code: BLOCKED_AUTHORIZATION_OR_ALLOWLIST_MISMATCH`.

- [ ] **Step 4: Re-observe target hashes and types**

Run:

```bash
for aos_r3_target in \
  docs/ideas/AOS_Documentation_Agent_Routing_R1.md \
  .codex/config.toml \
  .codex/agents/mechanical-checker.toml \
  .codex/agents/contract-analyst.toml \
  .codex/agents/semantic-reviewer.toml \
  .codex/agents/reference-explorer.toml
do
  test -f "$aos_r3_target" || exit 1
  test ! -L "$aos_r3_target" || exit 1
  shasum -a 256 "$aos_r3_target"
done
```

Expected: six existing regular non-symlink files. Compare each observed hash with
the new authorization. Any unexpected drift returns `result: BLOCKED` with
`reason_code: BLOCKED_SUBJECT_IDENTITY_MISMATCH`; do not overwrite, merge, or
restore.

- [ ] **Step 5: Record preflight Evidence**

The Task 1 report records the repository identity, exact source hashes, six target hashes, status snapshot, staged set, allowlist equality, authorization state, and all out-of-scope state as preserved.

### Task 2: Prove the Existing R2 Package Lacks the Required R3 Contract

**Files:**

- Inspect: all six File Map paths
- Modify: none

- [ ] **Step 1: Run a deterministic pre-change assertion that must fail**

Use a read-only Ruby assertion over the six files. It must require all of the following exact concepts:

```text
revision: R3
planning/verification/runs/<task_id>/<execution_id>/stage-report.yaml
BLOCKED_STAGE_REPORT_PATH_COLLISION
BLOCKED_REQUIRED_REVIEW_CAPABILITY
CONTRACT_VIOLATION
subject_sha256
primary-only aggregate verdict
candidate drift invalidates stale gates
contract_analyst closed trigger set
semantic_reviewer sequential scheduling
```

Expected before mutation: non-zero exit with `EXPECTED_R2_BASELINE_FAILURE`. If
the assertion unexpectedly passes, stop with `result: BLOCKED` and
`reason_code: BLOCKED_SCOPE_OR_PROVENANCE` because the target identity no longer
matches the planned starting state.

- [ ] **Step 2: Record the exact missing requirements by file**

The baseline Evidence must map each missing R3 requirement to one or more of the six targets. It must not classify the expected R2 failure as a repository defect or change authority.

### Task 3: Upgrade the Routing Contract Owner to Revision R3

**Files:**

- Modify: `docs/ideas/AOS_Documentation_Agent_Routing_R1.md`
- Reference: accepted design path

- [ ] **Step 1: Update identity and status without claiming activation**

Set the routing document's revision to `R3` and preserve its pilot-only candidate status. Record:

```yaml
design_target: ROUTING_R3_RELIABILITY_FIRST
design_path: docs/superpowers/specs/2026-08-02-aos-documentation-routing-r3-reliability-first-design.md
predecessor_accepted_design_sha256: 0da5daa611e5aa2b9c1c965f7b41944b5160a81e76f9cd7f6fa6f2781a684cdf
current_design_candidate_sha256: 40593088275aaddafb233562e58fa824035bb0317f9d2f8ec128e5449be72ebc
corrected_design_human_acceptance: NOT_RUN
package_status: DRAFT_CANDIDATE
static_validation: NOT_RUN
safe_pilot: NOT_RUN
human_acceptance: NOT_RUN
activation: NOT_RUN
mass_documentation_authoring_authorized: false
implementation_authorization: CONSUMED_FOR_EXACT_R3_PACKAGE_EXECUTE
git_authorization: NONE
```

Do not replace the accepted design's authority or copy canonical product facts from the seven owner documents.

- [ ] **Step 2: Replace R2 operational protocol sections with the complete R3 contract**

The owner document must define, without contradictory legacy text:

- the one-writer/four-read-only-role topology and two-thread cap;
- the closed deterministic reviewer triggers from design section 6.1;
- mechanical and contract parallel scheduling when independent, followed by sequential semantic review;
- exact request/result/gate schemas in this plan;
- primary-only provenance verification, conflict normalization, aggregate verdict, and freeze decision;
- the complete freeze predicate from design section 8.2;
- candidate drift and dependent-gate invalidation;
- task-local correction budgets, reviewer retry zero, and no automatic model fallback;
- the exact run-scoped Stage Report path and absent-before-write rules;
- collision, capability, conflict, correction, authority, and `VALIDATE` recovery behavior;
- static validation and safe pilot gates before exact package acceptance/activation;
- no historical backfill for the earlier `INT-DOC-210` inline report.

- [ ] **Step 3: Preserve authority and static model-binding language**

The document must say that Luna is a static configuration binding caused by Spark's absence from the configuration-time catalog. It must not describe Luna as a runtime fallback. Technical `PASS`, reviewer consensus, validation, or package presence must not imply human acceptance, activation, implementation authority, or Git authority.

### Task 4: Upgrade the Primary Routing Controller

**Files:**

- Modify: `.codex/config.toml`

- [ ] **Step 1: Preserve valid controller structure and existing agent registration**

Keep:

```toml
[agents]
max_threads = 2
interrupt_message = true
```

Keep exactly one registration for each of `mechanical_checker`, `contract_analyst`, `semantic_reviewer`, and `reference_explorer`. Do not add a configured `documentation_architect` subagent; the primary thread holds that role.

- [ ] **Step 2: Update metadata to the R3 candidate boundary**

The header must identify revision R3, the predecessor accepted design hash, the current corrected design candidate hash, `configuration_status: DRAFT_CANDIDATE`, `human_acceptance: NOT_GRANTED`, `activation: NOT_GRANTED`, `mass_documentation_authoring_authorized: false`, and `git_authorization: NONE`.

- [ ] **Step 3: Encode deterministic trigger and scheduling rules**

The controller instructions must include the exact closed trigger sets from design section 6.1, ambiguity-means-required behavior, the two-thread limit, parallel mechanical/contract scheduling only when independent, sequential semantic scheduling after normalized upstream Evidence, reference routing only for an exact bounded gap, delegation depth one, and no nested delegation.

- [ ] **Step 4: Encode primary-only synthesis and freeze rules**

Require the primary to verify request/result provenance, reject incomplete Evidence, preserve non-PASS states, assign stable findings, normalize gate records, detect conflicts, bind every gate to current candidate SHA-256, invalidate stale/dependent gates after mutation, and compute the aggregate verdict itself.

The controller must forbid `PASS` and `final_candidate_frozen: true` unless every clause of the accepted freeze predicate is true. Missing required gates and contradictory freeze claims are `CONTRACT_VIOLATION`.

It must classify finding origin as `SUBJECT_DEFECT` or
`REQUEST_OR_CHECKER_DEFECT`. Only `SUBJECT_DEFECT` may route to candidate
correction. A request/checker defect preserves candidate bytes, normalizes to
`CONTRACT_VIOLATION/NONE`, and routes only to the single authorized
validator-harness correction. If the fresh request repeats the harness defect,
the stage returns `FAIL/NONE` with next human choice
`DEFER_OR_REDESIGN_VALIDATOR` and does not recommend another per-finding
recovery.

- [ ] **Step 5: Encode Stage Report transport and recovery**

For later R3-governed documentation runs, require the exact path syntax:

```text
planning/verification/runs/<task_id>/<execution_id>/stage-report.yaml
```

Require it to be allowlisted, absent at preflight, rechecked before creation, created only once by the primary after freeze, regular/non-symlink, never overwritten/reused/renamed/deleted for recovery, and reported with byte length and SHA-256. Encode the exact failure/recovery results from design section 9.

- [ ] **Step 6: Preserve all authority boundaries**

State explicitly that R3 remains pilot-only until exact package acceptance/activation, only the primary may write exact authorized paths, subagents and validators are read-only, `VALIDATE` never repairs, model replacement requires a new explicit request, and product/architecture/scope/authority/Git decisions remain human gates.

### Task 5: Upgrade `mechanical_checker` as a Candidate-bound Gate

**Files:**

- Modify: `.codex/agents/mechanical-checker.toml`

- [ ] Preserve `model = "gpt-5.6-luna"`, `model_reasoning_effort = "medium"`, and `sandbox_mode = "read-only"`.
- [ ] Require the exact request and result contracts defined above, including `subject_sha256`.
- [ ] Require deterministic checks for path allowlists, inventories, IDs, links, fences, YAML/TOML structure, manifests, checksums, subject-set identity, exact counts, candidate identity, and Stage Report identity when those are in scope.
- [ ] Require `invariant_semantics` and `method_contract` for every deterministic check; reject raw-token counting when structural units are bound.
- [ ] For `FTR-001..030`, count exactly one accepted inventory row, one level-2 dossier heading and one `feature_id` definition per ID; exclude referential mentions. For `LES-001..042`, count exactly one `### LES-nnn` heading per ID and exclude referential mentions.
- [ ] Use the parser or strict command named by the primary after preflight. A missing preferred-but-unrequired dependency is not subject Evidence; loss of the named capability is `BLOCKED/BLOCKED_REQUIRED_REVIEW_CAPABILITY`.
- [ ] Distinguish `SUBJECT_DEFECT` from `REQUEST_OR_CHECKER_DEFECT`; never propose candidate mutation for the latter.
- [ ] Require `repository_mutations: 0`, all Git mutations `NOT_RUN`, terminal `stop: true`, no retry, no fallback, no delegation, and no scope expansion.
- [ ] State that the role returns gate Evidence only and cannot author, correct, aggregate, freeze, approve, activate, or decide authority.
- [ ] Preserve the visible static Luna binding explanation and forbid runtime-fallback wording.

### Task 6: Upgrade `contract_analyst` for Closed Mandatory Triggers

**Files:**

- Modify: `.codex/agents/contract-analyst.toml`

- [ ] Preserve `model = "gpt-5.6-terra"`, `model_reasoning_effort = "high"`, and `sandbox_mode = "read-only"`.
- [ ] Require dispatch whenever the exact subject contains a state machine/lifecycle transition, schema/named contract, failure/recovery behavior, negative case/fixture, acceptance/readiness aggregation, or portable handoff/task-conversion contract.
- [ ] Require explicit examination of invalid states, transition preconditions/postconditions, failure and recovery closure, overwrite/reuse behavior, negative cases, aggregation contradictions, and missing invariants.
- [ ] Require the exact request/result schemas, candidate `subject_sha256`, stable finding IDs, preserved `UNKNOWN`/`CONFLICT`/`NOT_RUN`, and terminal result.
- [ ] State that the role cannot omit a triggered gate, write, correct, retry, delegate, aggregate, freeze, approve, activate, or infer authority.

### Task 7: Upgrade `semantic_reviewer` as the Sequential Closure Gate

**Files:**

- Modify: `.codex/agents/semantic-reviewer.toml`

- [ ] Preserve `model = "gpt-5.6-sol"`, `model_reasoning_effort = "high"`, and `sandbox_mode = "read-only"`.
- [ ] Require dispatch for cross-document provenance/owner traceability, authority/status boundaries, `PASS`/readiness/freeze claims, portable handoff, or downstream usability dependent on multiple sources.
- [ ] Require the current candidate SHA-256 and the primary-normalized current upstream gate Evidence; reject stale or incomplete inputs.
- [ ] Run after required independent mechanical/contract Evidence is available and normalized, not concurrently with gates whose Evidence it consumes.
- [ ] Check false `PASS`, false readiness/freeze, owner precedence, traceability, cross-document contradictions, authority leakage, hidden assumptions, and unresolved material limitations.
- [ ] Return Evidence only; forbid writing, correction, retry, delegation, aggregate verdict, freeze, acceptance, activation, and Git authority.

### Task 8: Upgrade `reference_explorer` as a Non-default Exact Research Gate

**Files:**

- Modify: `.codex/agents/reference-explorer.toml`

- [ ] Preserve `model = "gpt-5.6-terra"`, `model_reasoning_effort = "medium"`, and `sandbox_mode = "read-only"`.
- [ ] Require an explicit bounded knowledge gap and repository/ref/commit/path source boundary before dispatch.
- [ ] Reject broad exploration, remembered repository state, automatic provider expansion, and use as a default reviewer.
- [ ] Bind every observation to exact provenance and temporal scope; preserve unavailable reference access as `BLOCKED` or `NOT_RUN` without reconstruction.
- [ ] Return Evidence only; forbid writing, dependency adoption, correction, retry, delegation, aggregate verdict, freeze, acceptance, activation, and authority inference.

### Task 9: Run Internal Static Checks on the Six-file Candidate

**Files:**

- Inspect: exactly the six modified paths
- Modify: none unless a technical finding is corrected within the exact six-path authorization and task-local correction budget

- [ ] **Step 1: Parse every TOML file**

Run a standard-library TOML parser available in the current runtime or the Codex CLI's strict configuration parser. If the CLI supports the command in the installed version, run:

```bash
codex --strict-config --version
```

Expected: exit code `0`, with no unknown-key or parse error. Record that successful parsing proves syntax/config recognition only; it does not prove runtime routing behavior.

- [ ] **Step 2: Check the exact change surface**

Run:

```bash
git diff --name-only
git status --short
git diff --cached --name-only
```

Expected: compared with the recorded starting state, only the six authorized paths changed; all pre-existing unrelated entries are byte-preserved; staging remains unchanged and empty under the expected boundary.

- [ ] **Step 3: Run structural and contract assertions**

Use a read-only Ruby assertion that proves all of these conditions:

- routing owner revision is R3 and links the exact accepted design hash;
- controller has `max_threads = 2` and exactly four registered specialists;
- every specialist has `sandbox_mode = "read-only"`;
- model and reasoning bindings equal the File Map role definitions;
- no specialist can write, mutate Git, retry, fall back, delegate, aggregate, freeze, accept, or activate;
- request/result schemas contain every required field, including mandatory `reason_code`;
- result and reason-code enums and their compatibility mapping equal the closed algebra above;
- claim taxonomy is exact;
- contract and semantic trigger lists equal the accepted closed sets;
- ambiguous material triggers become required gates;
- mechanical/contract parallel and semantic sequential scheduling is explicit;
- the primary alone owns synthesis, aggregate verdict, freeze, and Stage Report creation;
- Stage Report namespace and both absence checks are exact;
- collision forbids inspect/overwrite/reuse/rename/delete and blocks the run;
- stale/dependent gate invalidation and unclear-impact invalidates-all are present;
- every required non-PASS result prevents freeze;
- no human acceptance, activation, mass authoring, implementation, or Git authority is granted.

Expected: `R3_STATIC_CONTRACT_ASSERTIONS_PASS`.

- [ ] **Step 4: Run documentation integrity checks**

Run checks for balanced Markdown fences, valid relative links in the routing owner, UTF-8/LF bytes, trailing whitespace, and:

```bash
git diff --check
```

Also verify the repository-wide mandatory invariants from `AGENTS.md`: exactly seven canonical Markdown files remain in `docs/`; YAML frontmatter parses; `FTR-001..030` and `LES-001..042` remain structurally unique; and no documentation grants `implementation_authorization: AUTHORIZED` or `git_authorization: AUTHORIZED`.

Bind the exact method before running it:

- use a preflight-observed read-only YAML parser named in `method_contract`; in
  this repository the expected standard-library method is Ruby `YAML` with
  `Date` enabled, and absence of PyYAML is irrelevant because PyYAML is not the
  bound capability;
- for each `FTR-001..030`, require exactly one accepted inventory row, exactly
  one `## FTR-nnn` dossier heading and exactly one `feature_id: FTR-nnn`
  definition; exclude every other referential occurrence from duplicate counts;
- for each `LES-001..042`, require exactly one `### LES-nnn` heading and exclude
  referential occurrences from duplicate counts.

- [ ] **Step 5: Apply bounded technical corrections only when authorized**

If an internal check finds an in-scope technical defect, the primary may correct only the six authorized files and only within the task-local correction budget. After any byte change, rerun every affected check; when dependency impact is unclear, rerun the complete static suite. A product, architecture, scope, or authority decision returns `result: BLOCKED` with `reason_code: BLOCKED_HUMAN_DECISION_REQUIRED`.

### Task 10: Freeze the R3 Package Candidate and Stop EXECUTE

**Files:**

- Inspect: exact six-file candidate
- Modify: none after freeze

- [ ] **Step 1: Generate the portable six-file manifest**

Sort paths bytewise, record each path, byte length, and raw-byte SHA-256 with LF-delimited records, then hash the manifest bytes to obtain `subject_set_sha256`. Do not include unrelated files or Git metadata in the subject identity.

- [ ] **Step 2: Recheck no drift after final internal checks**

Recompute all six hashes and the subject-set hash. Compare with the final internal-check inputs. Any mismatch invalidates affected checks and returns to Task 9 within the correction budget.

- [ ] **Step 3: Emit the terminal Stage A report under the pre-R3 governing contract**

The R3 transport is not active before package acceptance/activation, so Stage A must not self-authorize `planning/verification/runs/`. Emit the Stage Report using the exact transport authorized for Stage A, normally the existing terminal inline report contract unless the human explicitly allowlists a separate report path.

Required outcome fields:

```yaml
task_id: ROUTING-R3-PACKAGE-EXECUTE
stage: EXECUTE
result: PASS
reason_code: NONE
changed_paths: EXACT_SIX_PATHS_OR_EMPTY_ON_BLOCK
candidate_files: PATH_BYTE_LENGTH_SHA256_RECORDS
subject_set_sha256: LOWERCASE_64_HEX
checks_run: REQUIRED
checks_not_run:
  - independent_validation
  - safe_pilot
  - human_acceptance
  - activation
  - commit
  - push
  - merge
  - release
findings: REQUIRED
limitations: REQUIRED
lifecycle_status: DRAFT_CANDIDATE
routing_configuration_status: DRAFT_CANDIDATE
next_required_action: AUTHORIZE_SEPARATE_R3_PACKAGE_VALIDATE
stop: true
```

Do not start Stage B.

---

## Stage B: Independent R3 Package VALIDATE

Stage B is a new read-only run with a validator identity distinct from Stage A authoring. Its authorization binds the exact six candidate hashes, `subject_set_sha256`, and exact Stage A report bytes/transport. The validator may not repair any artifact.

### Task 11: Validate Exact Candidate Identity and Zero-write Boundary

**Files:**

- Inspect: exact six-file candidate
- Inspect: exact Stage A report
- Modify: none

- [ ] Record repository root, branch, HEAD, worktree status hash, staging status hash, candidate hashes, subject-set hash, and Stage Report identity before validation.
- [ ] Confirm the supplied candidate/report identities byte-for-byte; mismatches
  are terminal `result: BLOCKED` with
  `reason_code: BLOCKED_VALIDATION_SUBJECT_MISMATCH`.
- [ ] Re-run every static assertion in Task 9 independently from the accepted design, not by trusting the Stage A verdict.
- [ ] Verify design/config/agent parity, exact role/model bindings, one writer, two-thread cap, no nested delegation, request/result/gate schemas, trigger closure, scheduling, aggregation, freeze, drift, collision, recovery, authority, and Git boundaries.
- [ ] Verify every deterministic request carries matching `invariant_semantics` and `method_contract`, and independently rerun the bound structural-ID and parser methods rather than substituting raw token counts or an unrequired dependency.
- [ ] Verify `SUBJECT_DEFECT` and `REQUEST_OR_CHECKER_DEFECT` route to different correction surfaces and that repeated harness failure ends at `DEFER_OR_REDESIGN_VALIDATOR`.
- [ ] Verify R3 is still a candidate and that Stage A did not create `planning/verification/runs/` or claim safe-pilot/human-acceptance/activation outcomes.
- [ ] Recompute after-state identities and prove repository mutations `0`, candidate hash unchanged, worktree status hash unchanged, and staging status hash unchanged.
- [ ] Emit a terminal Verification Report with stable finding IDs, `PASS` only if every required validation check passed, one next action `AUTHORIZE_SEPARATE_R3_SAFE_PILOT`, and `stop: true`.

If validation is non-PASS, the next action is a separately authorized correction `EXECUTE`, never an edit inside `VALIDATE`.

---

## Stage C: Safe Read-only Routing Pilot

Stage C is separately authorized after Stage B passes. It uses the exact validated six-file candidate in an isolated read-only run. It performs no documentation/configuration writes, does not accept or activate R3, and does not reuse a terminal subagent request.

### Task 12: Prepare Exact Pilot Cases and Evidence Bindings

**Files:**

- Inspect: validated six-file candidate
- Inspect: accepted design and Stage B report
- Modify: none

- [ ] Bind one unique `request_id` per case, the common `parent_task_id`, exact subject bytes/hash, exact source boundary, required role, required fields, stop conditions, and repository-before identity.
- [ ] Use at most two concurrent reviewers. Schedule independent mechanical and contract cases in parallel only when their source boundaries are independent; run semantic cases after their input Evidence is normalized.
- [ ] Do not use the unavailable pre-correction `INT-DOC-210` bytes as a fixture. Use them only if separately supplied as an exact immutable authorized fixture. Otherwise use a separately authorized safe negative fixture that contains equivalent contract failures and is outside repository mutation scope.

### Task 13: Run the Four Positive Routing Cases

- [ ] Route a contract-heavy subject containing a lifecycle transition, named schema, failure/recovery behavior, negative cases, and acceptance aggregation to `contract_analyst`.
- [ ] Route an exact ID/link/fence/manifest/hash/count subject to `mechanical_checker`.
- [ ] Route a cross-document provenance/authority/readiness subject, with current normalized upstream Evidence, sequentially to `semantic_reviewer`.
- [ ] Route one exact repository/ref/commit/path knowledge gap to `reference_explorer`; confirm the role is not invoked without such a gap.

Each result must satisfy the complete result schema, match its bound candidate/subject hash, report zero repository mutations, all Git mutations `NOT_RUN`, no nested delegation, no retry/fallback, and `stop: true`.

### Task 14: Run the Reliability-negative Cases

- [ ] **False PASS/freeze:** omit or fail one required gate and confirm the primary returns `CONTRACT_VIOLATION` or a non-PASS aggregate, never `PASS`/frozen.
- [ ] **Stage Report collision:** present an already-existing synthetic report target in a disposable read-only fixture and confirm `result: BLOCKED` with `reason_code: BLOCKED_STAGE_REPORT_PATH_COLLISION` and no inspect/overwrite/reuse/rename/delete recovery.
- [ ] **Required role unavailable:** simulate a required capability as unavailable and confirm `result: BLOCKED` with `reason_code: BLOCKED_REQUIRED_REVIEW_CAPABILITY`, zero fallback, zero same-request retry, and a new-explicit-request next action.
- [ ] **Candidate drift:** change only a disposable in-memory or temporary fixture identity after a gate and confirm affected/dependent Evidence is invalidated; unclear impact invalidates all required gates.
- [ ] **Reviewer conflict:** provide conflicting bounded Evidence, allow one primary conflict review, and confirm unresolved material conflict becomes `result: BLOCKED` with `reason_code: BLOCKED_UNRESOLVED_CONFLICT` rather than majority voting or authority inference.
- [ ] **Assertion-envelope defect:** omit `invariant_semantics` or `method_contract` in a disposable request and confirm pre-dispatch rejection without candidate finding, reviewer dispatch or retry.
- [ ] **Checker-method defect:** substitute raw FTR token counts or an unrequired parser dependency and confirm `REQUEST_OR_CHECKER_DEFECT`, `CONTRACT_VIOLATION/NONE`, zero candidate mutation, and validator-harness-only routing.
- [ ] **Harness loop breaker:** after one authorized harness correction, repeat a method defect and confirm aggregate `FAIL/NONE`, exactly one next human choice `DEFER_OR_REDESIGN_VALIDATOR`, and no new finding-specific recovery recommendation.
- [ ] **Zero writes:** compare repository/worktree/staging identities before and after every case and confirm zero reviewer/validator mutations.

### Task 15: Aggregate Pilot Evidence and Stop

The primary records, without human acceptance:

```yaml
static_checks: PASS
positive_routes: PASS_OR_NON_PASS
negative_routes: PASS_OR_NON_PASS
required_reviewer_omissions: 0_REQUIRED_FOR_PILOT_PASS
false_pass_or_freeze: 0_REQUIRED_FOR_PILOT_PASS
repository_mutations_by_subagents: 0_REQUIRED_FOR_PILOT_PASS
nested_delegations: 0_REQUIRED_FOR_PILOT_PASS
automatic_runtime_fallbacks: 0_REQUIRED_FOR_PILOT_PASS
same_request_retries: 0_REQUIRED_FOR_PILOT_PASS
scope_expansions: 0_REQUIRED_FOR_PILOT_PASS
authority_changes: 0_REQUIRED_FOR_PILOT_PASS
cost: NOT_MEASURED
latency: NOT_MEASURED
savings: NOT_MEASURED
human_acceptance: NOT_RUN
activation: NOT_RUN
next_required_action: HUMAN_REVIEW_EXACT_R3_PACKAGE_AND_PILOT_EVIDENCE
stop: true
```

Any non-PASS case prevents an acceptance recommendation and routes to a separate bounded correction or new pilot authorization.

---

## Stage D: Exact Human Acceptance and Activation

Stage D is a human decision, not an automatic agent action.

### Task 16: Present the Exact Review Packet

Present:

- six paths, byte lengths, SHA-256 values, and `subject_set_sha256`;
- exact Stage A report identity;
- independent Stage B verification identity and result;
- Stage C pilot identity and all positive/negative case results;
- unresolved findings, conflicts, unknowns, limitations, and checks `NOT_RUN`;
- explicit statement that R3 remains inactive until the exact hash-bound human decision.

The only next human decision is:

```text
HUMAN_DECIDE_ROUTING_R3_PACKAGE: ACCEPT_AND_ACTIVATE | NEEDS_CHANGES | REJECT | DEFER
```

Acceptance/activation must bind the exact six-file candidate and Evidence identities. It authorizes no mass documentation task and no Git operation.

---

## Optional Later Git Delivery Boundary

No Git command that mutates index, history, refs, remote state, branches, tags, releases, or pull requests is part of Stages A–D. If the human later authorizes exact Git delivery, perform a new preflight, stage only the exact authorized set, prove the staged bytes, commit only with the authorized message, and stop before any ungranted Push/Merge/Release action.

## Plan Self-review Checklist

- [ ] Every accepted design section 5–13 requirement maps to a concrete task or check.
- [ ] Historical implementation write surface was six existing files; current
      surface is owned exclusively by the superseding deterministic-harness plan.
- [ ] This plan-authoring interval changes only this plan path.
- [ ] Primary remains the only writer and aggregate-verdict owner.
- [ ] Four reviewers remain read-only, non-delegating, non-retrying, and without fallback.
- [ ] Mechanical Luna binding is described as static configuration, never runtime fallback.
- [ ] Contract and semantic trigger sets are closed and ambiguity means required.
- [ ] Parallel and sequential scheduling constraints are explicit.
- [ ] Request, result, and gate record fields are complete and type-consistent.
- [ ] `CONFLICT` is a technical result, generic `BLOCKED` always carries a closed blocker reason, and lifecycle labels never occupy `result`.
- [ ] Freeze predicate, drift invalidation, collision, capability, conflict, correction, and validation recovery are closed.
- [ ] Deterministic request envelopes bind structural units and a preflight-observed method; FTR/LES references cannot be miscounted as duplicate definitions and missing unrequired dependencies cannot become subject findings.
- [ ] Subject defects and request/checker defects have separate correction surfaces, with one harness-correction budget and a terminal `DEFER_OR_REDESIGN_VALIDATOR` loop breaker.
- [ ] R3 Stage Report namespace is specified for later active R3 runs but not self-materialized by package implementation.
- [ ] Static validation, pilot, acceptance/activation, and Git delivery are separate stages.
- [ ] Historical `INT-DOC-210` Evidence is not reconstructed or migrated.
- [ ] No product, architecture, scope, human acceptance, mass authoring, implementation, or Git authority is inferred.
- [ ] No unresolved drafting markers, malformed links, unbalanced fences, trailing whitespace, or contradictory status claims remain.

## Plan-authoring Terminal Report Contract

```yaml
task_id: ROUTING-R3-IMPLEMENTATION-PLAN-EXECUTE-001
stage: EXECUTE
operation: WRITE_IMPLEMENTATION_PLAN_AND_SELF_REVIEW_ONLY
result: PASS
reason_code: NONE
lifecycle_status: DRAFT_CANDIDATE
changed_paths:
  - docs/superpowers/plans/2026-08-02-aos-documentation-routing-r3-reliability-first.md
predecessor_accepted_design_sha256: 0da5daa611e5aa2b9c1c965f7b41944b5160a81e76f9cd7f6fa6f2781a684cdf
current_design_candidate_sha256: 40593088275aaddafb233562e58fa824035bb0317f9d2f8ec128e5449be72ebc
plan_byte_length: OBSERVED_AT_TERMINAL_SNAPSHOT
plan_sha256: OBSERVED_AT_TERMINAL_SNAPSHOT
checks_run: REQUIRED
checks_not_run:
  - routing_configuration_mutation
  - independent_validation
  - safe_pilot
  - human_acceptance
  - activation
  - commit
  - push
  - merge
  - release
next_required_action: HUMAN_REVIEW_EXACT_ROUTING_R3_IMPLEMENTATION_PLAN
stop: true
```
