---
document_type: AOS_SCAFFOLDING_CONTRACT
revision: R1
candidate_id: AOS_3_SCAFFOLDING_CONTRACT_R1_2026_08_05
status: DRAFT
authority: PROPOSAL_PENDING_HUMAN_REVIEW
authority_scope: EXACT_SCAFFOLD_BEHAVIOR_FOR_FIRST_IMPLEMENTATION_CYCLE
knowledge_repository: NMF13579/notebook
target_implementation_repository: NMF13579/aos-3
target_repository_creation: NOT_RUN
decision_basis: AOS_IMPLEMENTATION_DECISIONS_R1.md
decision_basis_sha256: 4cda4efcdd4611bf0b1cb6478151d1160799472c98442e1440c5c97f01c26248
runtime_implementation: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
created: 2026-08-05
---

# AOS-3 Scaffolding Contract R1

## 1. Назначение и граница

Этот документ определяет exact behavior будущих строительных лесов AOS-3: topology, ownership, toolchain, development command surface, deterministic bootstrap, safeguards, recovery и acceptance matrix до реализации product behavior.

Документ является candidate owner только для scaffold behavior. Он не заменяет владельцев product, architecture или development facts и не разрешает создать repository, сгенерировать scaffold, выполнить runtime implementation либо Git action.

```yaml
DOC-004:
  technical_result: PASS
  readiness: READY_FOR_HUMAN_REVIEW
  human_acceptance: NOT_RUN
DOC-005: NOT_RUN
target_repository_creation: NOT_RUN
runtime_implementation: NOT_RUN
implementation_authorization: NONE
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
```

Scaffold считается инфраструктурой разработки, а не реализованным продуктом. Наличие tree, schemas, tests или CI не позволяет заявлять first vertical slice как implemented.

## 2. Нормативная база и классификация

### 2.1. Accepted basis

| Source | Authority в этом contract |
|---|---|
| `docs/00_Core.md` | project identity, status semantics, Minimal Safety Floor |
| `AOS_IMPLEMENTATION_DECISIONS_R1.md` | accepted `H1-001…H1-011` decisions |
| `docs/02_Architecture.md` | architecture layers, ownership и contract classes |
| `docs/03_Development.md` | workflow, preflight, validation, recovery и Git boundaries |
| `docs/04_Lessons.md` | lesson proposals и regression cases с сохранением их item-level status; не отдельная human acceptance каждого `LES-*` |
| `planning/02_AGENTS_DRAFT.md@5220864c…fd28` | accepted thin-bootstrap candidate; root activation `NOT_RUN` |

### 2.2. Feature boundary

Accepted first-cycle dispositions: `FTR-001`, `FTR-008`, `FTR-011`, `FTR-016`, `FTR-019` в boundaries, записанных в `AOS_IMPLEMENTATION_DECISIONS_R1.md`.

`FTR-004`, `FTR-009`, `FTR-014`, `FTR-023` и `FTR-030` остаются `UNDECIDED`. Их dossiers использованы только как design references для infrastructure safeguards, требуемых documentation plan и общими safety contracts. Этот документ не меняет их item-level disposition и не включает полную реализацию этих features в первый product slice.

### 2.3. External toolchain observations

```yaml
observed_at: 2026-08-05
uv_latest_stable: 0.12.1
uv_release_source: https://github.com/astral-sh/uv/releases/tag/0.12.1
uv_ci_guidance: https://docs.astral.sh/uv/guides/integration/github/
python_latest_observed: 3.14.7
python_source: https://www.python.org/downloads/
contract_python_pin: 3.14.6
```

Python `3.14.6` сохраняется как exact accepted `H1-005` value. Наличие `3.14.7` не меняет accepted decision автоматически. Patch upgrade требует successful matrix на новом patch, отдельной candidate revision и human review.

## 3. Scaffold outcome

После разрешённого выполнения будущего `Task-001-Scaffolding` clean checkout должен обеспечивать:

1. один понятный development entrypoint `./aos-dev`;
2. pinned Python/uv и reproducible dependency lock;
3. физическое разделение `core`, `product`, `safety` и adapters;
4. strict versioned contract locations;
5. места для unit/contract/integration и negative fixtures;
6. read-only `doctor` и isolated `self-test`;
7. preview-bound, recoverable setup;
8. одинаковый official check surface локально и в CI;
9. сохранение user/project-owned state;
10. honest terminal status и одно следующее действие.

## 4. Target repository и branch model

```yaml
repository:
  expected_remote_identity: NMF13579/aos-3
  physical_creation: NOT_RUN
  topology: MODULAR_MONOREPO
  default_integration_branch_candidate: dev
  task_branch_pattern: agent/<task-id>
  protected_default_branch: HUMAN_CONFIGURATION_REQUIRED
  automatic_merge: false
  automatic_release: false
```

До physical creation все repository facts являются expected bindings, а не `OBSERVED_AT_SNAPSHOT`. Future Task Brief обязан повторно проверить repository root, branch, HEAD, worktree, remote и existing files. Несовпадение identity блокирует mutation, но не read-only diagnosis.

Branch creation, branch protection, remote assignment, Commit, Push, Merge и Release не входят в `DOC-004` и не разрешаются этим contract.

## 5. Exact first-cycle topology

```text
/
├── AGENTS.md
├── README.md
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
├── aos-dev
├── contracts/
│   ├── README.md
│   └── schemas/
│       └── README.md
├── docs/
│   ├── README.md
│   ├── decisions/
│   └── tasks/
├── scaffold/
│   └── manifest.v1.json
├── scripts/
│   └── aos_dev.py
├── src/
│   └── aos/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── core/
│       │   └── __init__.py
│       ├── product/
│       │   └── __init__.py
│       ├── safety/
│       │   └── __init__.py
│       └── adapters/
│           └── __init__.py
└── tests/
    ├── unit/
    ├── contract/
    ├── integration/
    └── fixtures/
        └── negative/
```

`src/aos/factory/` намеренно отсутствует в first-cycle scaffold. Development Factory появится только по отдельному accepted contract/task; пустой namespace не должен выглядеть как реализованная capability. `core`, `product`, `safety` и `adapters` содержат только package boundaries. Feature modules и product schemas появятся в соответствующих последующих contracts/tasks, а не как фиктивно готовые scaffold files.

`.aos/` также не создаётся scaffold setup автоматически. Это Project Memory boundary, создаваемая только первым отдельно подтверждённым product write (`aos intake --save`) по будущему feature contract.

## 6. Directory ownership matrix

Ownership classes:

```text
MANAGED        scaffold owns exact baseline; update requires manifest reconciliation
PROJECT_OWNED  project/user content; setup never overwrites or deletes
GENERATED      disposable and rebuildable; never authority
TEMPORARY      transaction-scoped; cleanup only after terminal reconciliation
PROTECTED      mutation requires a separate exact authorization
FORBIDDEN      scaffold must never write
```

| Path | Purpose | Owner | Allowed writers | Lifecycle | Validation | Recovery |
|---|---|---|---|---|---|---|
| `AGENTS.md` | localized thin bootstrap | `PROTECTED` | separate activation task only | versioned | exact source/revision and placeholder audit | restore prior bytes; no automatic replacement |
| `README.md` | first-start route | `PROJECT_OWNED` after creation | explicit documentation task | versioned | links and command consistency | preserve user edits; conflict on update |
| `.python-version` | Python pin | `MANAGED` | scaffold task/update | versioned | exact `3.14.6` | fail closed on mismatch |
| `pyproject.toml` | package/dependency/tool config | `MANAGED` then protected | exact dependency task | versioned | strict parse + lock consistency | restore preimage or reconcile journal |
| `uv.lock` | exact dependency resolution | `MANAGED` generated canonical lock | exact dependency task | versioned | `uv sync --locked` | regenerate only from accepted metadata and review diff |
| `aos-dev` | official development wrapper | `MANAGED` | scaffold task | versioned | help zero-write + dispatch tests | restore preimage |
| `contracts/` | versioned machine contracts | `PROTECTED` | contract-specific task | versioned | strict schema and runtime drift tests | new schema revision; no in-place history rewrite |
| `docs/` | local implementation decisions/tasks | `PROJECT_OWNED` | bounded documentation tasks | versioned | repository-relative links | preserve; resolve conflict explicitly |
| `scaffold/manifest.v1.json` | path ownership/digest/operation manifest | `PROTECTED` | scaffold-contract task | versioned | strict loader + self-digest exclusion | new manifest revision; old remains evidence |
| `scripts/aos_dev.py` | development command implementation | `MANAGED` | scaffold task | versioned | command contract suite | journaled update/restore |
| `src/aos/core/` | shared contracts/status/paths | `PROTECTED` | exact product/core task | versioned | unit + contract tests | task-local rollback |
| `src/aos/product/` | first visible Product Runtime slice | `PROTECTED` | feature task only | versioned | feature acceptance/negative tests | feature recovery contract |
| `src/aos/safety/` | minimal action classification | `PROTECTED` | exact safety task | versioned | authority defaults false | fail closed; restore accepted baseline |
| `src/aos/adapters/` | thin non-authoritative adapters | `PROTECTED` | adapter task | versioned | drift check against common contracts | disable adapter without changing core |
| `tests/` | executable acceptance/regression | `PROJECT_OWNED` | bounded implementation tasks | versioned | collection + negative fixture audit | preserve unrelated tests |
| `.aos/state/` | future current Project Memory | `PROJECT_OWNED` | explicit product write only | durable | strict version/schema | atomic temp+fsync+rename; preserve preimage |
| `.aos/records/` | future immutable records | `PROJECT_OWNED` | explicit product write only | append-only | identifier/digest/link checks | never rewrite; append correction record |
| `.aos/.scaffold/transactions/` | setup journal | `TEMPORARY` | authorized setup apply only | until reconciliation | terminal journal state | resume/rollback from journal |
| `.venv/`, `.pytest_cache/`, `.ruff_cache/`, `__pycache__/` | local environment/cache | `GENERATED` | tools | disposable | excluded from candidate | delete/rebuild only exact generated paths |
| `.artifacts/` | local reports/build output | `GENERATED` | build/check/self-test | disposable | subject binding in report | delete/rebuild; not durable Evidence |
| OS temp outside repo | isolated self-test workspace | `TEMPORARY` | self-test | per run | cleanup result recorded | preserve on failed cleanup with locator |
| `.git/` | Git internals | `FORBIDDEN` | Git only under separate action | external | pre/post identity observation | stop; never direct-edit |
| unknown existing path | unclassified state | `FORBIDDEN` until classified | none | preserved | report `UNKNOWN_MATERIAL` | human decision or scoped classification |

No scaffold operation may use blanket deletion, recursive overwrite, `git add -A`, absolute user-machine links or direct writes into `.git/`.

## 7. Path and repository safety policy

Before any write:

1. resolve repository root without following a user-controlled path outside it;
2. reject nested Git repositories inside intended mutation paths;
3. normalize each relative path and reject `..`, absolute paths, NUL and empty segments;
4. evaluate existing parent/target symlinks and reject any escape;
5. compare case-folded paths on case-insensitive filesystems and reject collisions;
6. classify every existing affected path by ownership;
7. record unrelated dirty state without adding it to the candidate;
8. freeze intended operations and their content digests in a preview;
9. verify the same repository/HEAD/worktree/preview immediately before apply.

Portable links must be repository-relative. `file://`, `/Users/...`, `/home/...` and workspace-specific absolute links fail contract validation.

## 8. Toolchain and environment contract

### 8.1. Pins

```yaml
language: Python
implementation: CPython
python_exact: 3.14.6
python_constraint: ==3.14.6
uv_exact: 0.12.1
project_metadata: pyproject.toml
dependency_lock: uv.lock
application_framework: NONE_FIRST_CYCLE
runtime_dependencies_default: NONE_UNLESS_FEATURE_REQUIRES
development_dependencies:
  - pytest
  - ruff
development_dependency_exact_versions: OWNED_BY_UV_LOCK
```

`pyproject.toml` names direct dependencies and compatible bounds. `uv.lock` owns exact transitive resolution. No setup command may update the lock implicitly; `--locked`/`--frozen` behavior is mandatory outside a separate dependency-update task.

### 8.2. Supported matrix

| Environment | Role | Required result |
|---|---|---|
| macOS / ARM64 / zsh / CPython 3.14.6 | primary development | full scaffold matrix |
| Ubuntu 24.04 LTS / x86_64 / bash / CPython 3.14.6 | independent CI | same `check`/`self-test` surface |
| Windows | deferred | `NOT_RUN`, never implied PASS |
| Docker | not required | `NOT_APPLICABLE` first cycle |

### 8.3. Prerequisites

- POSIX-compatible shell for `./aos-dev`;
- Git only for identity observation; scaffold commands do not perform Git mutations;
- `uv 0.12.1` available on `PATH`;
- network only when explicitly allowed for first dependency/Python download;
- write access only to previewed allowed paths and configured temporary directory.

### 8.4. Environment variables

Allowed non-secret variables:

| Variable | Purpose | Default | Rule |
|---|---|---|---|
| `AOS_OUTPUT` | `human` or `json` result rendering | `human` on TTY, otherwise `json` | invalid value fails |
| `AOS_OFFLINE` | disallow network | `0` | `1` must pass `--offline` downstream |
| `AOS_ARTIFACTS_DIR` | generated output location inside repo | `.artifacts` | normalized repo-relative only |
| `UV_NO_MODIFY_PATH` | prevent installer PATH mutation | `1` in documented install path | never disabled by scaffold |
| `UV_LOCKED` | require unchanged lock | `1` in checks/CI | mutation task must opt out explicitly |
| `NO_COLOR` | disable ANSI output | unset | presentation only |

Secrets, tokens, credentials and provider keys are not scaffold inputs. Output redacts URL userinfo, query, fragment and values whose names match credential patterns.

### 8.5. Network and offline behavior

- `doctor`, `--help`, `status`, `check` after sync and all first-slice runtime reads require no network.
- `setup --preview` performs no network.
- `setup --apply` may use network only with `--allow-network` and only for pinned toolchain/dependency retrieval.
- without network and without a warm cache, return `BLOCKED` with missing artifact list and correction hint;
- no fallback to unpinned versions, alternate indexes or provider APIs.

## 9. Official command surface

The sole development entrypoint is:

```text
./aos-dev <command> [options]
```

Product-facing command remains `aos`; `./aos-dev run -- ...` is only a development bridge. Docs, CI and tests must not introduce a second official development entrypoint.

### 9.1. Wrapper bootstrap behavior

`aos-dev` is a checked-in POSIX `sh` wrapper, not an installer downloaded at execution time. It must:

1. render static `--help` before invoking `uv`, Python or any write-capable tool;
2. verify exact `uv 0.12.1` and report mismatch without self-update;
3. locate an already installed CPython `3.14.6` for read-only preview/doctor without downloading it;
4. return `BLOCKED` with a no-write correction hint when pinned Python is absent;
5. allow Python/dependency download only inside authorized `setup --apply --allow-network`;
6. after setup, dispatch through the locked `.venv` interpreter to `scripts/aos_dev.py`;
7. preserve argv without shell re-evaluation and never source project-controlled environment files;
8. propagate the exact terminal exit code from the dispatcher.

`scripts/aos_dev.py` uses Python standard library for scaffold control. It does not import Product Runtime packages to perform preflight, setup, doctor or recovery, so a broken/unimplemented product slice cannot silently bypass scaffold validation.

### 9.2. Common terminal result

Every command emits exactly one terminal result. JSON form:

```json
{
  "schema_version": "aos.dev-result.v1",
  "command": "check",
  "technical_result": "PASS",
  "required_checks": [],
  "optional_checks": [],
  "writes": [],
  "limitations": [],
  "unknowns": [],
  "next_action": "NONE"
}
```

Closed technical vocabulary:

```text
CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS
```

Precedence:

```text
CONTRACT_VIOLATION > FAIL > BLOCKED > UNKNOWN > NOT_RUN > PASS
```

Required `NOT_RUN`, `UNKNOWN` or `BLOCKED` prevents aggregate `PASS`. Optional `NOT_RUN` remains visible but does not fail an otherwise valid result.

Stable exit codes:

| Exit | Meaning |
|---:|---|
| `0` | terminal `PASS` only, or successful `--help` |
| `2` | invalid CLI usage |
| `3` | contract/input/schema violation |
| `4` | toolchain/environment mismatch |
| `5` | blocked identity/scope/permission/network precondition |
| `6` | technical check/test/build failure |
| `7` | partial state or recovery required |
| `8` | unexpected internal error |

### 9.3. Command contracts

| Command | Purpose | Writes by default | Success oracle | Idempotency / CI |
|---|---|---:|---|---|
| `--help` | show commands/options | none | exit `0`, unchanged repo tree/status | always; smoke in CI |
| `setup --preview` | inspect prerequisites and render exact planned writes | none | frozen preview ID + no conflicts | repeat same inputs → same preview |
| `setup --apply --preview-id ID` | create/sync development environment and managed generated paths | preview only | actual diff equals preview; journal terminal | repeat produces no additional state; CI uses clean checkout |
| `run -- ARGS` | execute product CLI in locked environment | product contract decides | terminal product Result Contract | CI smoke uses read-only args |
| `test [--unit|--contract|--integration|--all]` | run selected pytest profile | `.artifacts`/caches only | required tests collected and pass | `--all` in CI |
| `check` | official aggregate quality gate | `.artifacts` only | format-check + lint + tests + contract checks pass | sole CI quality command |
| `format --check` | verify formatting | none except disposable report | no diff required | included in `check` |
| `format --apply` | apply Ruff formatting | scoped source/test files | changed-path report, no unrelated files | developer-only, separate mutation |
| `build` | create wheel/sdist for validation | `.artifacts/dist/` only | clean build + package smoke import | CI optional until distribution is selected |
| `doctor` | read-only environment/repo diagnosis | none | every check explicit; required `NOT_RUN` prevents PASS | CI/local smoke |
| `self-test` | exercise scaffold invariants in isolated temp checkout | OS temp + `.artifacts` report | negative fixtures fail as expected; source unchanged | required in CI after Task-001 |

### 9.4. Doctor checks

Required:

- repository root and expected project markers;
- Python exact version and executable provenance;
- uv exact version and executable provenance;
- `pyproject.toml`/`uv.lock` consistency;
- source import provenance points inside current checkout;
- manifest parse/schema/version;
- path ownership collisions, symlinks and nested repositories;
- writable temp boundary;
- source-tree before/after digest for zero-write claim;
- official command references consistency.

Network, remote repository access, Windows and release checks are optional/`NOT_RUN` unless an exact task makes them required.

## 10. Scaffold manifest contract

`scaffold/manifest.v1.json` is the machine-readable owner of managed scaffold paths. Minimum fields:

```json
{
  "schema_version": "aos.scaffold-manifest.v1",
  "package_id": "aos-3-scaffold-r1",
  "target_repository": "NMF13579/aos-3",
  "entries": [
    {
      "path": ".python-version",
      "kind": "file",
      "ownership": "MANAGED",
      "operation": "create_or_verify",
      "content_sha256": "<sha256>"
    }
  ],
  "forbidden_roots": [".git"],
  "post_apply_checks": ["doctor", "self-test"]
}
```

Rules:

- schema rejects unknown ownership/operation enums and unexpected fields;
- every managed file has expected digest or explicit template identity;
- directories do not use content digests;
- manifest does not self-attest its own validity; candidate digest is computed externally;
- duplicate or case-colliding paths fail;
- any existing non-matching managed path becomes a conflict, not an overwrite;
- user/project-owned paths may be declared but never content-managed;
- deletion is absent from R1 manifest operations.

## 11. Preview, apply and reconciliation

### 11.1. Preview

`setup --preview` is read-only and produces:

```yaml
preview_schema: aos.scaffold-preview.v1
repository_identity:
baseline_identity:
manifest_sha256:
environment_fingerprint:
planned_operations: []
conflicts: []
preserved_paths: []
network_required: false
permissions_required: []
preview_id:
expires_when:
  - repository_identity_changes
  - baseline_changes
  - manifest_changes
  - affected_path_changes
  - environment_fingerprint_changes_materially
```

Preview ID is a digest of canonicalized fields excluding `preview_id`. Preview file, if persisted, goes only to `.artifacts/` and is not authorization.

### 11.2. Apply preconditions

Apply requires all:

1. exact `preview_id` supplied;
2. current identity still matches preview;
3. no unresolved conflict or material unknown;
4. explicit task-scoped human authorization for the planned writes;
5. allowed-path list contains every operation;
6. journal path is writable;
7. network permission explicitly present when preview says required.

Documentation acceptance of this contract is not apply authorization.

### 11.3. Apply algorithm

```text
reverify preview
→ create durable transaction journal
→ stage new file bytes beside destination
→ fsync staged files and journal
→ atomic rename one operation at a time
→ record actual digest after each operation
→ reconcile intended vs actual
→ run doctor
→ run self-test
→ mark journal COMMITTED only after required checks PASS
→ emit terminal result and stop
```

No automatic Commit, Push or cleanup of unrelated state follows successful apply.

## 12. Interruption, retry and recovery

### 12.1. Journal states

```text
PREPARED | APPLYING | APPLIED_UNVERIFIED | COMMITTED | RECOVERY_REQUIRED | ROLLED_BACK
```

Each journal records transaction ID, preview ID, starting identity, operations, preimage existence/digest, staged digest, completed step, actual digest, timestamps and terminal classification. Raw secret values are forbidden.

### 12.2. Interruption behavior

On signal, crash or detected partial state:

1. stop new writes;
2. preserve journal and staged/preimage data;
3. classify intended/actual operations;
4. emit exit `7` and `RECOVERY_REQUIRED` when a terminal result can be produced;
5. do not auto-retry;
6. show one exact next action: inspect, resume or rollback.

### 12.3. Resume

Resume is allowed only when repository identity, manifest, preview-bound unchanged inputs and completed-operation digests still match. It continues from the first incomplete operation and re-runs full post-apply validation.

Permission violation, path escape, changed human-owned file or changed scope forbids resume and requires a new preview/task decision.

### 12.4. Rollback

R1 rollback may remove only files created by the same transaction and restore exact captured preimages of managed files changed by that transaction. It never deletes user/project-owned data, `.git/`, `.aos/state/` or `.aos/records/`.

Destructive cleanup outside this boundary requires separate authorization. Failed rollback remains `RECOVERY_REQUIRED` with preserved journal.

## 13. CI/local parity

CI is advisory technical validation and never approval.

```yaml
ci_os: ubuntu-24.04
ci_arch: x86_64
python: 3.14.6
uv: 0.12.1
dependency_install: uv sync --locked
official_quality_command: ./aos-dev check
official_scaffold_command: ./aos-dev self-test
automatic_merge: false
automatic_release: false
```

CI setup action must be pinned to an immutable commit SHA and configured with `uv 0.12.1`. Cache is optional and disposable; cache miss cannot change dependency resolution. CI publishes `.artifacts` only as technical output and does not mutate project lifecycle.

## 14. Executable acceptance matrix

| ID | Case | Preconditions/action | Expected observable result |
|---|---|---|---|
| `SCF-001` | Clean checkout setup | correct pins; `preview` then authorized `apply` | expected tree/env created; journal `COMMITTED`; doctor PASS |
| `SCF-002` | Repeated setup | run same setup again | zero managed content changes; no duplicate state |
| `SCF-003` | Missing uv | invoke preview/doctor | non-zero exit `4`; exact install hint; zero writes |
| `SCF-004` | Wrong uv version | uv other than `0.12.1` | fail closed before mutation; observed/expected shown |
| `SCF-005` | Wrong Python version | Python other than `3.14.6` selected | fail closed before mutation; no implicit patch upgrade |
| `SCF-006` | `--help` | snapshot tree/status; invoke help | exit `0`; byte/status unchanged |
| `SCF-007` | Dirty unrelated user file | untracked/modified out-of-scope file present | preserved; classified; absent from actual candidate |
| `SCF-008` | Existing project-owned state | `.aos/state` and records exist | setup does not modify/delete them |
| `SCF-009` | Path traversal | manifest entry contains `../` or absolute path | contract violation exit `3`; zero writes |
| `SCF-010` | Symlink escape | affected parent/target resolves outside root | blocked exit `5`; zero writes |
| `SCF-011` | Nested repository | target path crosses nested `.git` boundary | blocked; exact path reported |
| `SCF-012` | Case collision | two paths collide under case fold | contract violation; zero writes |
| `SCF-013` | Preview drift | affected file changes after preview | apply rejected; new preview required |
| `SCF-014` | Interrupted write | inject interruption at every operation boundary | partial state detected; journal recoverable; exit `7` |
| `SCF-015` | Idempotent resume | resume unchanged partial transaction | remaining operations only; full validation rerun |
| `SCF-016` | Unsafe retry | scope/permission/identity changed | resume rejected; no scope expansion |
| `SCF-017` | Rollback | rollback transaction with created/managed files | only transaction-owned changes reverted; user state preserved |
| `SCF-018` | Network unavailable | cold cache, network not allowed/unavailable | `BLOCKED`; missing artifacts listed; no unpinned fallback |
| `SCF-019` | Offline warm cache | all pinned artifacts cached; offline enabled | setup/check succeed without network |
| `SCF-020` | Doctor after setup | invoke read-only doctor | exact required checks; honest optional `NOT_RUN`; zero writes |
| `SCF-021` | Required test absent | remove/skip required test group | aggregate cannot PASS |
| `SCF-022` | Failure exit semantics | force contract/env/test/internal failures | each maps to stable non-zero exit and JSON result |
| `SCF-023` | Local/CI parity | run official commands both environments | same command/result schema and required check set |
| `SCF-024` | Absolute link | introduce `file://` or machine path | portable-link check FAIL |
| `SCF-025` | Secret redaction | credential-bearing URL/input in fixture | terminal output contains no raw credential material |
| `SCF-026` | Source tree purity | run doctor/check/self-test | only declared generated/temp output; source digest unchanged |

Every case must bind command, exact candidate, result, exit code and output locator. A test that did not run remains `NOT_RUN`; it cannot be inferred from another test.

## 15. Scaffold implementation slice boundary

Future `Task-001-Scaffolding` may implement only:

- the exact tree and ownership manifest in this contract;
- toolchain pins and locked development dependencies;
- `./aos-dev` surface;
- только scaffold-local manifest/result parsing внутри `scripts/aos_dev.py`, не будущие Product Runtime contracts;
- scaffold tests/fixtures and advisory CI;
- localized bootstrap only after its separate activation prerequisites are met.

It must not implement Product Runtime behavior for intake, Project Memory writes or Status/Next. Product CLI placeholder может только сообщить `NOT_IMPLEMENTED`/non-zero; feature modules и schemas создаются последующими exact tasks, а не scaffold task.

`DOC-005` must derive an exact Task Brief and Developer Specification Package from this candidate after human review. Task Brief remains distinct from Execution Authorization.

## 16. Deferred, dynamic and non-blocking bindings

| Binding | State in this contract | Resolution point |
|---|---|---|
| physical remote repository, visibility/access | `NOT_RUN` | separate repository-creation decision |
| observed root/branch/HEAD/worktree | `UNKNOWN_UNTIL_REPOSITORY_EXISTS` | Task-001 preflight |
| branch protection configuration | `HUMAN_CONFIGURATION_REQUIRED` | repository setup task |
| exact pytest/Ruff/transitive versions | `OWNED_BY_FUTURE_UV_LOCK` | DOC-005/Task-001 dependency resolution and review |
| CI action immutable SHA at implementation date | `FRESH_PREFLIGHT_REQUIRED` | Task-001 |
| root `AGENTS.md` activation/localized paths | `NOT_RUN` | separate activation task after repository preflight |
| Project Memory schema semantics | outside scaffold owner | later core/product contract |
| `Risk_Profile` vocabulary | `DEFERRED` | first write-capable implementation Task Brief |
| Windows support | `DEFERRED` | separate environment decision/evidence |

These bindings do not make scaffold behavior ambiguous: their owner, required observation and stop condition are explicit. They block only the affected mutation, not contract review or read-only preflight.

## 17. Material unknown assessment

```yaml
material_unknowns_for_contract_review: []
dynamic_preflight_facts:
  - physical_repository_identity
  - repository_HEAD_and_worktree
  - dependency_resolution_digests
  - CI_action_commit_SHA
blocked_actions:
  - REPOSITORY_CREATION
  - SCAFFOLD_GENERATION
  - ROOT_AGENTS_ACTIVATION
  - RUNTIME_IMPLEMENTATION
  - GIT_DELIVERY
```

Dynamic mutable facts are deliberately re-observed at execution time and are not guessed in documentation. If human review rejects topology, pins, branch candidate or command surface, this candidate requires correction before `DOC-005`.

## 18. Traceability

| Contract requirement | Source/decision | Planned Evidence |
|---|---|---|
| target `NMF13579/aos-3` | `H1-001` | repository preflight |
| Product Runtime before Factory | `H1-003`, Architecture layers | topology and no `aos/factory` package |
| chat-first + deterministic CLI/JSON | `H1-004` | CLI contract tests |
| Python 3.14.6 + uv | `H1-005` | version/lock tests |
| file-based Project Memory preserved | `H1-006` | `SCF-008`, update preservation |
| macOS/ARM64 + Ubuntu CI | `H1-007` | matrix `SCF-023` |
| Codex thin adapter | `H1-008` | adapter drift check |
| exact human decisions only | `H1-009` | generated acceptance negative fixture |
| Result/doctor and action boundary | `H1-010`, `FTR-011`, `FTR-019` | terminal result, doctor, zero-write tests |
| read-only first | `H1-011` | `SCF-006`, `020`, `026` |
| path scope and user-state preservation | Development + `LES-017/018/026` | traversal/symlink/dirty-state tests |
| atomic/journaled recovery | Architecture + `LES-023` | interruption/resume/rollback tests |
| one entrypoint, honest statuses | `LES-010/016/031` | parity and exit/result tests |
| scaffold ≠ product | `LES-032/033` | scope audit and false-PASS negative fixture |

## 19. DOC-004 terminal status

```yaml
task_id: DOC-004
stage: EXECUTE
technical_result: PASS
readiness: READY_FOR_HUMAN_REVIEW
starting_subject:
  DOC-003: COMPLETED_HUMAN_ACCEPTED
ending_subject: AOS_SCAFFOLDING_CONTRACT_R1.md
changed_paths:
  - AOS_SCAFFOLDING_CONTRACT_R1.md
  - planning/CURRENT.md
checks_run:
  - SOURCE_AND_DECISION_BINDING
  - TOOLCHAIN_FRESH_PREFLIGHT
  - TOPOLOGY_AND_OWNERSHIP_COVERAGE
  - COMMAND_SURFACE_COVERAGE
  - SAFEGUARD_AND_RECOVERY_COVERAGE
  - ACCEPTANCE_MATRIX_COVERAGE
checks_not_run:
  - RUNTIME_TESTS
  - TARGET_REPOSITORY_PREFLIGHT
  - INDEPENDENT_VALIDATE
human_acceptance: NOT_RUN
implementation_authorization: NONE
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action: HUMAN_REVIEW_EXACT_DOC-004_CANDIDATE
stop: true
```
