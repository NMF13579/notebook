---
document_type: IMPLEMENTATION_TASK_BRIEF
task_id: Task-001-Scaffolding
revision: DRAFT-R1
status: DRAFT
readiness: READY_FOR_HUMAN_REVIEW
authority: DERIVED_FROM_HUMAN_ACCEPTED_CONTRACT
authority_scope: EXACT_FIRST_AOS_3_SCAFFOLD_IMPLEMENTATION_SLICE
contract_owner: AOS_SCAFFOLDING_CONTRACT_R1.md
contract_owner_sha256: 2a76e94dc9ea534a89d045bd428a0f5b2f1be64b6824c0f7462f2529a6e17901
contract_acceptance_record: planning/07_SCAFFOLDING_CONTRACT_ACCEPTANCE_RECORD.md
target_repository: NMF13579/aos-3
target_repository_creation: NOT_RUN
implementation_authorization: NOT_RUN
git_authorization: NONE
created: 2026-08-05
---

# Task-001 — AOS-3 Scaffolding

## 1. Цель и результат для пользователя

Создать smallest coherent development scaffold AOS-3, чтобы независимый coding agent мог из clean checkout воспроизводимо подготовить среду, выполнить один официальный набор проверок, диагностировать проблемы и безопасно восстановиться после interrupted setup.

Это developer-enabling result, а не пользовательская Product Runtime feature. После задачи idea intake, Project Memory writes и `Status / Next` остаются `NOT_IMPLEMENTED`.

### До

- target repository физически ещё не создан;
- observed root, branch, HEAD и worktree неизвестны до fresh preflight;
- scaffold, lock, commands, tests и CI отсутствуют;
- root `AGENTS.md` activation и root `README.md` creation выполняются отдельными prerequisite tasks/repository setup.

### После успешного отдельно разрешённого выполнения

- exact scaffold tree и ownership manifest существуют в target repository;
- `./aos-dev` является единственным development entrypoint;
- Python `3.14.6`, uv `0.12.1` и `uv.lock` дают воспроизводимую среду;
- preview/apply, journal, recovery, doctor и self-test соответствуют accepted contract;
- required acceptance cases `SCF-001…SCF-026` имеют executable tests и Evidence;
- Product Runtime по-прежнему не заявляется реализованным;
- никакие `Commit`, `Push`, `Merge` или `Release` автоматически не выполняются.

## 2. Authoritative basis

| Fact class | Owner / exact binding |
|---|---|
| Scaffold behavior | `AOS_SCAFFOLDING_CONTRACT_R1.md@2a76e94d…7901`, human-accepted через `planning/07_SCAFFOLDING_CONTRACT_ACCEPTANCE_RECORD.md` |
| Implementation decisions | `AOS_IMPLEMENTATION_DECISIONS_R1.md@4cda4efc…6248`, human-accepted |
| Authority and safety | `docs/00_Core.md` |
| Architecture boundaries | `docs/02_Architecture.md` |
| Workflow, preflight, validation, recovery, Git | `docs/03_Development.md` |
| Regression basis | `docs/04_Lessons.md`, только с сохранением item-level classifications |
| Thin agent bootstrap candidate | `planning/02_AGENTS_DRAFT.md@5220864c…fd28`, human-accepted; root activation remains separate |

Если Task расходится со Scaffolding Contract, contract имеет приоритет и execution останавливается. Coding agent не исправляет contract внутри этой задачи.

## 3. Entry gate и fresh repository preflight

Execution может начаться только после отдельных действий человека по созданию/назначению repository и активации localized root instructions.

Перед первой mutation coding agent обязан read-only проверить и записать:

1. repository root и remote identity `NMF13579/aos-3` без раскрытия credentials;
2. текущие branch, HEAD, worktree, staged/unstaged/untracked paths;
3. отсутствие nested repository и symlink escape в affected paths;
4. наличие и exact accepted identity root `AGENTS.md`, а также наличие и preserved digest root `README.md`, либо остановиться;
5. expected baseline и отсутствие изменений после preflight;
6. Python/uv provenance, sandbox, network mode и temp boundary;
7. existing paths по классам `IN_SCOPE_EXISTING | OUT_OF_SCOPE_USER_STATE | ENVIRONMENT_NOISE | GENERATED_DISPOSABLE | UNKNOWN_MATERIAL`;
8. immutable SHA всех CI actions, выбранный на дату исполнения;
9. exact planned diff, preview ID и разрешённые write paths.

Любое несовпадение identity, material unknown, conflict или stale preview блокирует mutation и требует нового review/authorization subject.

## 4. Scope

### 4.1. In scope

- exact first-cycle topology и ownership manifest accepted contract;
- pinned toolchain metadata и deterministic `uv.lock`;
- POSIX wrapper `./aos-dev` и scaffold-local dispatcher `scripts/aos_dev.py`;
- scaffold-only package boundaries и Product CLI placeholder с honest `NOT_IMPLEMENTED`/non-zero result;
- preview/apply reconciliation, transaction journal, resume and rollback boundary;
- scaffold tests, negative fixtures, result schemas and generated local reports;
- advisory GitHub Actions workflow using the official `./aos-dev check` and `./aos-dev self-test` surfaces;
- documentation needed only to operate this scaffold inside target repository.

### 4.2. Task-local technical bindings for human review

Accepted contract determines advisory GitHub CI but does not name its repository path. This candidate binds it to:

```text
.github/workflows/ci.yml
```

The workflow path is a reversible implementation detail. Its acceptance belongs to exact review of this Task/DSP; it does not amend product or architecture scope. The workflow must pin third-party actions to immutable commit SHAs observed during fresh preflight.

Exact pytest, Ruff and transitive versions are chosen by uv `0.12.1` during the authorized dependency-resolution step and become authoritative only through reviewed `uv.lock`. No alternate index, relaxed Python pin or implicit lock update is allowed.

The general statement that scaffold does not create Project Memory under `.aos/` is read together with the more specific accepted journal contract: only authorized `setup --apply` may create/use `.aos/.scaffold/transactions/`. It must never create or mutate `.aos/state/` or `.aos/records/`. Preview, help, doctor, check and self-test do not create `.aos/`. If human review rejects this specific-over-general reading, execution remains blocked pending a corrected Scaffolding Contract revision.

### 4.3. Out of scope

- repository creation, remote assignment, visibility and branch protection configuration;
- root `AGENTS.md` activation or replacement;
- Product Runtime behavior for intake, Project Memory writes or `Status / Next`;
- `.aos/state/`, `.aos/records/` and any Project Memory data creation or mutation; only the task-scoped transaction journal exception is in scope;
- `src/aos/factory/` and Development Factory;
- implementation of full `FTR-004`, `FTR-009`, `FTR-014`, `FTR-023` or `FTR-030` dossiers;
- feature schemas under `contracts/schemas/` beyond scaffold-local manifest/result/preview/journal validation;
- Windows support, Docker, deployment, release and provider integrations;
- automatic Git staging, Commit, Push, Merge, Release or branch deletion.

## 5. Allowed and forbidden paths

### Allowed paths in target repository

```text
.gitignore
.python-version
pyproject.toml
uv.lock
aos-dev
contracts/README.md
contracts/schemas/README.md
docs/README.md
docs/decisions/
docs/tasks/
scaffold/manifest.v1.json
scripts/aos_dev.py
src/aos/__init__.py
src/aos/__main__.py
src/aos/cli.py
src/aos/core/__init__.py
src/aos/product/__init__.py
src/aos/safety/__init__.py
src/aos/adapters/__init__.py
tests/unit/
tests/contract/
tests/integration/
tests/fixtures/negative/
.github/workflows/ci.yml
.artifacts/
.aos/.scaffold/transactions/
OS temporary directory selected by preflight
```

Within allowed directories, every created test/fixture/report path must be listed in the frozen preview before apply. Empty placeholder files are forbidden unless a tool requires them and their purpose is documented.

`README.md` at repository root and `AGENTS.md` are prerequisites or separate documentation/activation subjects; Task-001 must preserve their bytes.

### Forbidden paths

```text
.git/**
AGENTS.md
README.md
.aos/state/**
.aos/records/**
src/aos/factory/**
any absolute path or normalized path outside repository/temp boundary
any existing unknown or out-of-scope user-owned path
```

No blanket deletion, recursive overwrite, `git add -A`, direct `.git` edit, absolute machine link or credential-bearing output is allowed.

## 6. Required implementation behavior

### 6.1. Files and package boundary

1. Create only files/directories listed in the frozen preview and allowed path set.
2. Keep `core`, `product`, `safety` and `adapters` as package boundaries without fabricated feature behavior.
3. Product CLI placeholder returns stable non-zero `NOT_IMPLEMENTED`; it must never report `PASS` for unavailable Product Runtime behavior.
4. Do not create or mutate `.aos/state/` or `.aos/records/`; only authorized `setup --apply` may use `.aos/.scaffold/transactions/`, while preview, help, doctor, check and self-test remain zero-write with respect to `.aos/`.
5. Manifest loader rejects unexpected fields, enum values, duplicates, case collisions, absolute paths, traversal and self-attestation.

### 6.2. Official command surface

Implement only:

```text
./aos-dev --help
./aos-dev setup --preview
./aos-dev setup --apply --preview-id ID [--allow-network]
./aos-dev run -- ARGS
./aos-dev test [--unit|--contract|--integration|--all]
./aos-dev check
./aos-dev format --check
./aos-dev format --apply
./aos-dev build
./aos-dev doctor
./aos-dev self-test
```

Command semantics, JSON result schema and exit codes are exactly those in contract sections 9–13. `--help`, preview and doctor are zero-write except declared disposable reporting where the contract permits it. Required `NOT_RUN`, `UNKNOWN` or `BLOCKED` prevents aggregate `PASS`.

### 6.3. Preview/apply and recovery

1. Freeze canonical preview inputs and compute `preview_id` excluding itself.
2. Reverify identity, affected paths, manifest, environment and authorization before apply.
3. Create durable journal before first target write.
4. Stage bytes, fsync, atomic-rename one operation at a time and record actual digest.
5. Run doctor and self-test before journal becomes `COMMITTED`.
6. On interruption, stop new writes, preserve recovery data and return exit `7`/`RECOVERY_REQUIRED`.
7. Resume only when all bound inputs and completed digests still match.
8. Rollback only transaction-created files and exact captured managed preimages.
9. Never modify/delete user-owned state during retry, resume or rollback.

### 6.4. Local/CI parity

- CI runs on Ubuntu 24.04 x86_64 with CPython `3.14.6` and uv `0.12.1`.
- Dependency installation uses the reviewed lock and `uv sync --locked`.
- Required commands are `./aos-dev check` and `./aos-dev self-test`.
- CI is advisory, publishes only disposable `.artifacts`, and performs no merge/release.
- Local macOS/ARM64 and CI use the same required checks and result schema.

## 7. Validation and acceptance

All `SCF-001…SCF-026` from accepted contract section 14 are mandatory. The implementation must bind each case to exact command, candidate identity, result, exit code and Evidence locator.

| Group | Required cases | Minimum executable proof |
|---|---|---|
| Bootstrap/idempotency | `SCF-001`, `002`, `018`, `019` | isolated clean/warm/offline setup runs and journal/diff evidence |
| Toolchain/help | `SCF-003…006` | version/missing-tool fixtures, exit/result assertions, before/after digest |
| State/path safety | `SCF-007…013`, `024`, `025` | dirty-state, Project Memory preservation, traversal/symlink/nested/case/drift/link/redaction negatives |
| Recovery | `SCF-014…017` | interruption injection at every operation boundary, resume/reject/rollback evidence |
| Diagnosis/quality | `SCF-020…023`, `026` | doctor/check/self-test, required-test absence, exit map, CI parity, source purity |

Acceptance requires:

1. every mandatory case executed with terminal result and locator;
2. no required `NOT_RUN`, `UNKNOWN` or `BLOCKED` in a claimed `PASS`;
3. exact intended/actual diff match and no forbidden-path mutation;
4. zero-write proofs compare repository bytes/status, not only process output;
5. dependency/import provenance points into current checkout and reviewed lock;
6. recovery evidence shows preservation of user/project-owned state;
7. Product Runtime remains honestly `NOT_IMPLEMENTED`;
8. `git diff --check` and scoped diff inspection pass;
9. local required matrix passes; Ubuntu CI evidence may remain `NOT_RUN` until separately permitted Push/CI execution, and then prevents overall implementation `PASS` until completed.

## 8. Required Evidence

Create a task-scoped Evidence index under `.artifacts/task-001/` during execution and report durable candidate paths separately. Evidence must include:

- starting and ending repository identity snapshots;
- exact accepted Task/DSP/contract digests;
- normalized affected-path inventory and preserved out-of-scope state;
- preview JSON, preview digest and actual reconciliation report;
- journal terminal state plus injected recovery run records;
- dependency lock digest and Python/uv/import provenance;
- per-case `SCF-001…026` command, result, exit code and locator;
- source-tree/status before/after digests for zero-write cases;
- secret-redaction check result without raw secret material;
- changed-path list and diff summary;
- checks run/not run and limitations;
- terminal Stage Report matching `docs/03_Development.md`.

`.artifacts/` is disposable technical output and not human acceptance or durable authority. Evidence needed for review must be copied or summarized into an immutable Stage Report by a later authorized workflow.

## 9. Correction and recovery boundary

Within the same authorized Task-001 execution, coding agent may perform up to three bounded correction cycles only when all remain unchanged:

- user/developer outcome;
- accepted topology and ownership classes;
- Python/uv pins and command surface;
- allowed/forbidden paths;
- Product Runtime exclusion;
- recovery and permission boundaries;
- Task/DSP candidate identity and authorization scope.

Any contract change, new dependency class, additional top-level path, feature implementation, permission expansion or fourth correction cycle requires stop and a separate Task/decision.

## 10. Stop conditions

Stop without mutation, or stop new writes and preserve recovery state, when:

- target repository/remote/baseline/root instructions do not match authorization;
- worktree contains an affected unknown/conflict or preview becomes stale;
- pinned Python/uv or locked artifacts cannot be obtained without unapproved fallback;
- a write would escape allowed paths or touch protected/user-owned state;
- manifest, preview, journal or result contract cannot be validated strictly;
- interruption or partial state requires recovery;
- required acceptance cannot be made executable;
- scope would expand into Product Runtime, Development Factory or a currently `UNDECIDED` feature;
- authorization is missing, expired, consumed or does not bind exact Task candidate;
- any Git action would be required;
- material external content or credential boundary is unresolved.

## 11. Proposed Execution Authorization form — unsigned

This block is a proposal only. It must be completed from fresh preflight and explicitly issued by the human as a separate decision.

```yaml
execution_authorization:
  status: NOT_RUN
  actor_class: HUMAN_REQUIRED
  task_id: Task-001-Scaffolding
  task_revision: DRAFT-R1
  task_subject_sha256: FROM_ACCEPTED_DSP-001
  DSP_id: DSP-001
  DSP_subject_sha256: FROM_ACCEPTED_DSP-001
  repository: NMF13579/aos-3
  repository_root: FRESH_PREFLIGHT_REQUIRED
  branch: FRESH_PREFLIGHT_REQUIRED
  baseline_HEAD: FRESH_PREFLIGHT_REQUIRED
  worktree_fingerprint: FRESH_PREFLIGHT_REQUIRED
  preview_id: FRESH_PREFLIGHT_REQUIRED
  allowed_paths: EXACT_TASK_ALLOWLIST
  allowed_operations:
    - CREATE_OR_VERIFY_SCAFFOLD_FILES
    - RESOLVE_AND_LOCK_DECLARED_DEV_DEPENDENCIES
    - RUN_TASK_SCOPED_TESTS_AND_CHECKS
    - WRITE_DECLARED_TEMPORARY_AND_ARTIFACT_OUTPUT
  forbidden_operations:
    - REPOSITORY_CREATION
    - ROOT_AGENTS_ACTIVATION
    - PRODUCT_RUNTIME_IMPLEMENTATION
    - GIT_COMMIT
    - GIT_PUSH
    - GIT_MERGE
    - RELEASE
  network: EXPLICIT_VALUE_REQUIRED
  expires_when:
    - SUBJECT_HASH_CHANGES
    - REPOSITORY_IDENTITY_CHANGES
    - BASELINE_OR_WORKTREE_CHANGES_MATERIALLY
    - PREVIEW_EXPIRES
    - AUTHORIZATION_CONSUMED
```

## 12. Terminal report schema

```yaml
task_id: Task-001-Scaffolding
stage: EXECUTE
result: CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS
starting_identity:
ending_identity:
task_subject_sha256:
DSP_subject_sha256:
preview_id:
changed_paths: []
preserved_out_of_scope_state: []
checks_run: []
checks_not_run: []
acceptance_results: []
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

## 13. Exact Task Brief data

```yaml
task:
  task_id: Task-001-Scaffolding
  title: Build reproducible AOS-3 development scaffold
  stage: EXECUTE
  goal: IMPLEMENT_ACCEPTED_SCAFFOLD_CONTRACT_ONLY
  user_outcome: REPRODUCIBLE_SAFE_DEVELOPMENT_BASE_WITHOUT_PRODUCT_BEHAVIOR
  feature_id: NONE_INFRASTRUCTURE_PREREQUISITE
  feature_contract_revision: AOS_3_SCAFFOLDING_CONTRACT_R1_2026_08_05
  parent_stage: D2_SCAFFOLDING
  repository: NMF13579/aos-3
  repository_identity_requirement: EXACT_REMOTE_AND_ROOT_FROM_FRESH_PREFLIGHT
  baseline_requirement: EXACT_BRANCH_HEAD_WORKTREE_AND_PREVIEW_BOUND_AT_AUTHORIZATION
  dependencies:
    - PHYSICAL_REPOSITORY_CREATED_BY_SEPARATE_HUMAN_AUTHORIZED_ACTION
    - ROOT_AGENTS_ACTIVATED_BY_SEPARATE_TASK
    - ROOT_README_CREATED_BY_SEPARATE_REPOSITORY_OR_DOCUMENTATION_TASK
    - EXACT_TASK_AND_DSP_HUMAN_ACCEPTED
    - FRESH_PREFLIGHT_COMPLETED
    - EXPLICIT_EXECUTION_AUTHORIZATION_ISSUED
  in_scope:
    - CONTRACT_EXACT_TOPOLOGY_AND_OWNERSHIP
    - PINNED_TOOLCHAIN_AND_LOCK
    - AOS_DEV_COMMAND_SURFACE
    - SCAFFOLD_PREVIEW_APPLY_JOURNAL_RECOVERY
    - SCAFFOLD_TESTS_NEGATIVE_FIXTURES_AND_ADVISORY_CI
  out_of_scope:
    - REPOSITORY_CREATION
    - ROOT_AGENTS_ACTIVATION
    - PRODUCT_RUNTIME_FEATURES
    - PROJECT_MEMORY_WRITES
    - DEVELOPMENT_FACTORY
    - WINDOWS_DOCKER_DEPLOYMENT_RELEASE
    - FULL_UNDECIDED_FEATURE_IMPLEMENTATION
  allowed_paths: SEE_SECTION_5_EXACT_ALLOWLIST
  forbidden_paths: SEE_SECTION_5_EXACT_DENYLIST
  allowed_operations:
    - PREVIEW_BOUND_SCAFFOLD_CREATE_OR_VERIFY
    - DECLARED_DEPENDENCY_LOCK_RESOLUTION
    - TASK_SCOPED_FORMAT_TEST_CHECK_BUILD_DOCTOR_SELF_TEST
    - JOURNALED_RESUME_OR_ROLLBACK_WITHIN_TRANSACTION_BOUNDARY
  forbidden_operations:
    - UNPREVIEWED_WRITE_OR_DELETE
    - PROTECTED_OR_USER_STATE_MUTATION
    - PRODUCT_RUNTIME_IMPLEMENTATION
    - GIT_OR_RELEASE_ACTION
  required_behavior:
    - CONTRACT_SECTIONS_3_THROUGH_15
    - SCF-001_THROUGH_SCF-026
  invariants:
    - SCAFFOLD_IS_NOT_PRODUCT
    - ONE_OFFICIAL_DEVELOPMENT_ENTRYPOINT
    - REQUIRED_NOT_RUN_UNKNOWN_BLOCKED_PREVENT_PASS
    - PREVIEW_BINDS_APPLY
    - USER_STATE_PRESERVED
    - AUTHORITY_DEFAULTS_FALSE
    - EDIT_NE_COMMIT_NE_PUSH_NE_MERGE_NE_RELEASE
  assumptions: []
  material_unknowns: []
  dynamic_preflight_facts:
    - REPOSITORY_ROOT_BRANCH_HEAD_WORKTREE
    - DEPENDENCY_RESOLUTION_DIGESTS
    - CI_ACTION_IMMUTABLE_SHAS
    - NETWORK_AND_SANDBOX_CAPABILITY
  acceptance_criteria:
    - ALL_SCF-001_THROUGH_SCF-026_EXECUTED_OR_REQUIRED_NOT_RUN_BLOCKS_PASS
    - INTENDED_ACTUAL_DIFF_RECONCILED
    - NO_FORBIDDEN_PATH_OR_USER_STATE_MUTATION
    - PRODUCT_RUNTIME_HONESTLY_NOT_IMPLEMENTED
    - TERMINAL_STAGE_REPORT_EMITTED_AND_STOPPED
  negative_scenarios:
    - SCF-003_THROUGH_SCF-018
    - SCF-021_THROUGH_SCF-026
  validation_matrix:
    - AOS_SCAFFOLDING_CONTRACT_R1.md_SECTION_14
    - DSP-001.md_TRACEABILITY_MATRIX
  evidence_requirements:
    - SECTION_8
  recovery_requirements:
    - CONTRACT_SECTIONS_11_AND_12
    - SECTION_9
  correction_boundary: MAX_3_NON_MATERIAL_TASK_LOCAL_CYCLES
  proposed_risk_profile: HUMAN_ASSIGNMENT_REQUIRED_BEFORE_EXECUTION
  assigned_risk_profile: UNASSIGNED
  stop_conditions:
    - SECTION_10
  terminal_report_schema: SECTION_12
  execution_authorization: NOT_RUN
  Git_authorization: NONE
```
