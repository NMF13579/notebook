---
document_type: IMPLEMENTATION_TASK_BRIEF
task_id: Task-002-Intake-to-Reviewable-Intent
revision: DRAFT-R1
status: HUMAN_REVIEW_REQUIRED
authority: NONE_UNTIL_HUMAN_ACCEPTANCE
authority_scope: FIRST_PRODUCT_RUNTIME_SLICE_IMPLEMENTATION
feature_contract: AOS_FEATURE_CONTRACT_INTAKE_TO_REVIEWABLE_INTENT_R1.md
target_repository: NMF13579/aos-3
baseline_requirement: POST_TASK-001_ACCEPTED_FRESH_PREFLIGHT
documentation_technical_result: PASS
implementation_result: NOT_RUN
readiness: BLOCKED_PENDING_TASK-001_AND_BASELINE_REBIND
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
created: 2026-08-06
---

# Task-002 — Intake to Reviewable Intent

## 1. Goal and sequencing

Implement the smallest user-visible AOS Product Runtime slice after scaffold completion:

```text
request + explicit structured proposal
→ read-only preview
→ exact confirmation
→ immutable Intent Record
→ atomic Project Memory
→ status / next / details / doctor / self-test
→ stop
```

This Task is not executable against an unknown or pre-scaffold baseline. Before authorization its identity must be rebound to the observed, human-accepted result of `Task-001-Scaffolding`.

## 2. Authoritative basis

| Fact class | Owner |
|---|---|
| Product behavior | `AOS_FEATURE_CONTRACT_INTAKE_TO_REVIEWABLE_INTENT_R1.md` |
| H1 decisions | `AOS_IMPLEMENTATION_DECISIONS_R1.md` |
| Schemas/authority/status | `AOS_CORE_CONTRACT_R1.md` |
| Project Memory v2 | `AOS_CORE_CONTRACT_C012_V2_R1.md` |
| Persistence and views | `AOS_CORE_CONTRACT_C3_C4_R1.md` |
| Development workflow | `docs/03_Development.md` |
| Regressions | only mapped `docs/04_Lessons.md` cases |

If Task prose conflicts with the accepted feature/core contract, execution stops. Coding agent does not edit contract meaning inside this Task.

## 3. Entry gate

Before any mutation:

1. `Task-001` implementation has technical validation and exact human acceptance.
2. Target remote/root/branch/HEAD/worktree match `NMF13579/aos-3` and fresh preflight.
3. Root `AGENTS.md` is active and its exact digest is recorded.
4. Accepted contract, Task and DSP digests match authorization.
5. Intended diff is frozen and contains only allowlisted paths.
6. Network is denied for runtime/test matrix unless dependency setup separately permits it.
7. Human assigns `Risk_Profile`.
8. One-shot exact Execution Authorization binds task, repository, baseline, preview and paths.

Any stale or missing binding blocks mutation.

## 4. In scope

- strict canonical JSON primitives required by the slice;
- C-001 Intent Record and C-012 v2 validators;
- deterministic intake proposal/preview schemas;
- `aos intake --preview` zero-write path;
- `aos intake --save` exact-confirmation path;
- immutable intent record and atomic Project Memory transaction;
- `status`, `next`, `details`, `doctor`, `self-test` first-cycle behavior;
- fail-closed permission check needed by the feature;
- human/JSON parity and stable exit codes;
- executable positive/negative/recovery fixtures;
- isolated OS-temp integration tests;
- minimal operator docs for these exact commands.

## 5. Out of scope

- natural-language model/provider implementation in local runtime;
- Product Spec, Feature Passport and `FTR-003`;
- user-project Task Brief/code execution;
- Product Feature Registry or Context Pack;
- Development Factory, controlled runner or multi-agent routing;
- network/provider calls, telemetry or SaaS;
- target repository `.aos/` initialization during implementation;
- Commit, Push, Merge, Release.

## 6. Allowed paths in target repository

```text
contracts/schemas/aos.core.intent_record.v1.json
contracts/schemas/aos.core.project_memory.v2.json
contracts/schemas/aos.intake_proposal.v1.json
contracts/schemas/aos.intake_preview.v1.json
contracts/schemas/aos.view_result.v1.json
docs/product-runtime/intake.md
src/aos/cli.py
src/aos/core/canonical_json.py
src/aos/core/records.py
src/aos/core/project_memory.py
src/aos/core/results.py
src/aos/product/intake.py
src/aos/product/views.py
src/aos/safety/permissions.py
tests/unit/test_canonical_json.py
tests/unit/test_intake_preview.py
tests/unit/test_permissions.py
tests/contract/test_intent_record.py
tests/contract/test_project_memory_v2.py
tests/contract/test_view_result.py
tests/integration/test_intake_flow.py
tests/integration/test_intake_recovery.py
tests/fixtures/negative/intake/
tests/fixtures/positive/intake/
.artifacts/task-002/
OS temporary directories created by tests
```

Existing scaffold files outside the exact allowlist are read-only. A fresh preview must enumerate every concrete fixture and generated Evidence path under allowed directories.

## 7. Forbidden paths and operations

```text
.git/**
AGENTS.md
README.md
pyproject.toml
uv.lock
.python-version
aos-dev
scaffold/**
scripts/aos_dev.py
.github/**
.aos/**
src/aos/factory/**
any absolute/normalized path outside target or explicit OS-temp test root
any unknown or unrelated user-owned path
```

Forbidden:

- target repository Project Memory creation during implementation/testing;
- dependency/toolchain changes;
- unpreviewed create/update/delete;
- broad recursive overwrite/delete;
- network/provider call;
- generated human decision or implicit save confirmation;
- Git staging/commit/push/merge/release.

## 8. Required behavior

Implement contract sections 4–10 exactly, including:

1. strict duplicate-key/unknown-field/null/enum rejection;
2. canonical JSON and stable digest;
3. original request preservation;
4. adapter/user-supplied proposal boundary;
5. one material question rule;
6. deterministic zero-write preview;
7. preview ID recheck on save;
8. exact confirmation;
9. exclusive immutable record create;
10. journaled/atomic Project Memory write;
11. `active_task_status: NONE` and absent conditional task/stage/auth fields;
12. read-only status/next/details/doctor/self-test;
13. false-PASS prevention and stable exits;
14. offline operation and no Git mutation;
15. stop before Product Spec or user-project task.

No behavior may be replaced with placeholders that return `PASS`.

## 9. Validation matrix

| Group | Required cases |
|---|---|
| Product positives | `X1-ACC-001…016` |
| Product negatives | `X1-NEG-001…020` |
| Core strictness | relevant `CORE-001…018` and C1/C2 negatives |
| Memory | `C012-V2-ACC/NEG` and `C3-ACC/NEG` used by slice |
| Views | relevant `C4-ACC/NEG` |
| Purity | before/after tree bytes and Git status |
| Recovery | injected failure at every save boundary |
| Scope | intended/actual path equality and denylist audit |

Each required case records command/fixture, exact candidate identity, result, exit code and Evidence locator. Required `NOT_RUN` blocks `PASS`.

## 10. Recovery boundary

The implementation may correct code/tests within the same Task up to three non-material cycles. Runtime recovery tests may:

- resume only an unchanged exact transaction;
- reject stale/conflicting resume;
- keep the previous owner authoritative before rename;
- revalidate owner/refs/journal after uncertain rename;
- remove only exact test-owned temp data.

The agent stops for:

- contract/schema/interface change;
- new dependency or path;
- expanded product behavior;
- target `.aos/` mutation;
- fourth correction cycle;
- user-state conflict;
- required test impossible without hidden decision.

## 11. Evidence

`.artifacts/task-002/` may contain disposable execution Evidence:

- starting/ending identity;
- planned/actual paths;
- exact Task/DSP/contract digests;
- per-case matrix;
- preview zero-write digest;
- persistence journal/recovery observations from isolated temp subjects;
- no-network/no-Git proofs;
- import provenance from current checkout/lock;
- checks run/not run;
- limitations and remaining risk.

The terminal Stage Report must summarize durable review evidence. Disposable artifacts are not authority or human acceptance.

## 12. Proposed risk and authorization

```yaml
proposed_risk_profile: ELEVATED
proposed_reason: IMPLEMENTS_AUTHORITY_STATE_MUTATION_BEHAVIOR_BUT_TESTS_ONLY_IN_ISOLATED_TEMP_SUBJECTS
assigned_risk_profile: UNASSIGNED
execution_authorization: NOT_RUN
Git_authorization: NONE
```

The human may assign another profile. The proposal has no permission effect.

## 13. Terminal report

```yaml
task_id: Task-002-Intake-to-Reviewable-Intent
stage: EXECUTE
result: CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS
starting_identity:
ending_identity:
task_subject_sha256:
DSP_subject_sha256:
feature_contract_sha256:
preview_id:
changed_paths: []
preserved_out_of_scope_state: []
checks_run: []
checks_not_run: []
acceptance_results: []
negative_results: []
evidence_locators: []
recovery_state:
findings: []
limitations: []
unknowns: []
authorization_consumed:
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action:
stop: true
```

## 14. Exact Task data

```yaml
task:
  task_id: Task-002-Intake-to-Reviewable-Intent
  title: Implement first AOS Product Runtime intent slice
  stage: EXECUTE
  goal: IMPLEMENT_ACCEPTED_INTAKE_TO_REVIEWABLE_INTENT_CONTRACT_ONLY
  user_outcome: REVIEWABLE_INTENT_WITH_VISIBLE_UNKNOWNS_AND_ONE_NEXT_ACTION
  feature_ids: [FTR-001, FTR-008, FTR-011, FTR-016, FTR-019]
  feature_contract_revision: AOS_FEATURE_CONTRACT_INTAKE_TO_REVIEWABLE_INTENT_R1_DRAFT-R1
  parent_stage: X1_PRODUCT_RUNTIME
  repository: NMF13579/aos-3
  baseline_requirement: POST_TASK-001_ACCEPTED_FRESH_PREFLIGHT
  dependencies:
    - TASK-001_IMPLEMENTATION_HUMAN_ACCEPTED
    - ROOT_AGENTS_ACTIVE
    - EXACT_FEATURE_CONTRACT_TASK_DSP_HUMAN_ACCEPTED
    - FRESH_PREFLIGHT_AND_PREVIEW
    - HUMAN_ASSIGNED_RISK_PROFILE
    - ONE_SHOT_EXECUTION_AUTHORIZATION
  allowed_paths: SECTION_6_EXACT_ALLOWLIST
  forbidden_paths: SECTION_7_EXACT_DENYLIST
  allowed_operations:
    - PREVIEW_BOUND_SOURCE_AND_TEST_EDIT
    - TASK_SCOPED_TEST_EXECUTION_IN_OS_TEMP
    - DISPOSABLE_EVIDENCE_WRITE
  forbidden_operations:
    - TARGET_PROJECT_MEMORY_INITIALIZATION
    - PRODUCT_SCOPE_EXPANSION
    - DEPENDENCY_OR_TOOLCHAIN_CHANGE
    - NETWORK_OR_GIT_MUTATION
  acceptance_criteria:
    - FEATURE_CONTRACT_X1-ACC-001_THROUGH_016
    - ALL_REQUIRED_NEGATIVES_EXECUTED
    - INTENDED_ACTUAL_DIFF_RECONCILED
    - ZERO_TARGET_AOS_STATE_MUTATION
    - TERMINAL_STAGE_REPORT_AND_STOP
  correction_boundary: MAX_3_NON_MATERIAL_CYCLES
  proposed_risk_profile: ELEVATED
  assigned_risk_profile: UNASSIGNED
  execution_authorization: NOT_RUN
  Git_authorization: NONE
```
