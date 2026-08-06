---
document_type: H1_DECISION_READY_PACKAGE
revision: DRAFT-R1
status: HUMAN_REVIEW_REQUIRED
claim_class: SYNTHESIZED_PROPOSAL
authority: NONE_UNTIL_HUMAN_DECISION
task_id: DOC-001
stage: EXECUTE
technical_result: PASS
readiness: READY_FOR_HUMAN_REVIEW
human_decision: NOT_RUN
implementation_readiness: NOT_READY
implementation_authorization: NONE
git_authorization: NONE
knowledge_repository: NMF13579/notebook
implementation_repository: UNASSIGNED
candidate_id: AOS_3_H1_DECISION_PACKAGE_DRAFT_2026_08_05
created: 2026-08-05
updated: 2026-08-05
---

# AOS-3 — единый пакет решений H1

## 1. Вывод

Для первого цикла AOS-3 рекомендуется отдельный implementation repository и один небольшой Product Runtime slice:

```text
пользователь описывает идею в чате
→ AOS сохраняет исходный запрос
→ отделяет problem и desired outcome от предполагаемого solution
→ показывает assumptions, unknowns и material questions
→ создаёт reviewable Intent Record
→ сохраняет Project Memory
→ показывает Status и одно Next action
→ останавливается до Product Spec, Task Brief и любой реализации идеи
```

Это самый маленький user-visible результат, который одновременно:

- решает реальную проблему непрограммиста;
- проверяет Product Runtime раньше Development Factory;
- позволяет провести dogfood на реальном запросе;
- не требует executor, Git automation, RAG, SaaS UI или full Governance;
- оставляет архитектуру расширяемой без создания платформы заранее.

Этот документ содержит рекомендации агента. Ни одна рекомендация не является решением человека до explicit `ACCEPT` exact candidate.

## 2. Подтверждённая основа

| Fact | Класс | Owner |
|---|---|---|
| AOS предназначен для human-directed AI-assisted development и должен снижать стоимость постановки, координации, проверки и продолжения работы | `HUMAN_ACCEPTED_FACT` | [`docs/00_Core.md`](../docs/00_Core.md), §§2–4 |
| Первый продуктовый результат должен идти раньше Development Factory и усиленной Governance | `HUMAN_ACCEPTED_FACT` | [`docs/00_Core.md`](../docs/00_Core.md), §12 |
| Primary users — непрограммист/domain expert и vibe-coder; их проблемы включают потерю intent/state и неясное next action | `HUMAN_ACCEPTED_FACT` | [`docs/01_Product.md`](../docs/01_Product.md), §§2–4 |
| Product Runtime включает Intake, Status/Next/Details и Project Memory | `HUMAN_ACCEPTED_FACT` | [`docs/01_Product.md`](../docs/01_Product.md), §8 |
| First slice должен давать observable result при минимальных dependencies и без implicit Git delivery | `HUMAN_ACCEPTED_FACT` | [`docs/01_Product.md`](../docs/01_Product.md), §11 |
| Architecture direction — contract-first, manual-before-automation, small vertical slice, modular monorepo first и recoverable writes | `HUMAN_ACCEPTED_FACT` | [`docs/02_Architecture.md`](../docs/02_Architecture.md), §§2, 12–14 |
| `notebook` является knowledge repository; runtime code и implementation authorization в нём отсутствуют | `HUMAN_ACCEPTED_FACT` | [`docs/00_Core.md`](../docs/00_Core.md), §§2, 16; [`AGENTS.md`](../AGENTS.md) |
| Feature inventory принят, но item-level dispositions не приняты | `HUMAN_ACCEPTED_FACT` | [`docs/06_Features.md`](../docs/06_Features.md), §§1–3 |
| `PASS`, human decision, execution authorization и Git actions должны оставаться разными осями | `HUMAN_ACCEPTED_FACT` | [`docs/00_Core.md`](../docs/00_Core.md), §§9–10; [`docs/03_Development.md`](../docs/03_Development.md), §§2–3 |

## 3. Рекомендуемый связанный bundle

| Decision | Preferred option | Почему |
|---|---|---|
| Implementation repository | Новый отдельный `NMF13579/aos-3` | Не меняет роль `notebook`; создаёт чистую runtime boundary |
| First segment | Непрограммист/domain expert, создающий новый проект | Это основной пользователь и текущий dogfood actor |
| First problem | `P-003` как primary; `P-001`, `P-002`, `P-015` как supporting | Сначала сохранить intent, показать понимание и не потерять продолжение |
| First vertical slice | `INTAKE_TO_REVIEWABLE_INTENT_R1` | Даёт observable Product Runtime value без coding pipeline |
| First interface | Chat-first UX через thin Codex adapter; deterministic CLI/JSON как machine boundary | Пользователю удобно в чате, contracts остаются тестируемыми и переносимыми |
| Toolchain | CPython `3.14.6`, `uv`, `pyproject.toml` + `uv.lock`, stdlib CLI, minimal pinned test/quality tools | Низкая сложность, читаемость, cross-platform lockfile, отсутствие app framework |
| Persistence | Repository-local versioned JSON files, atomic replace, no database | Достаточно для первого цикла, переносимо и легко диагностируется |
| Supported environments | macOS arm64 primary; Ubuntu 24.04 x86_64 CI; Windows deferred | Покрывает текущую разработку и независимую проверку без лишней матрицы |
| Primary agent environment | Codex over local checkout | Ближайшая реалистичная coding environment; core contracts остаются tool-neutral |
| Human decision authenticity | Explicit human decision bound to `candidate_id` + SHA-256; generated decisions invalid | Минимальная проверяемая provenance без PKI и отдельного сервиса |
| First-cycle features | `FTR-001`, `FTR-008`, `FTR-011`, `FTR-016`, `FTR-019` в узкой v1 boundary | Intake + понятный status + result semantics + continuity + minimal safety |
| Risk vocabulary | Отложить exact vocabulary до первого write-capable implementation Task Brief | Первый product slice не исполняет пользовательский код и не делает Git actions |

## 4. Карточки решений

### H1-001 — implementation repository и topology

```yaml
decision_id: H1-001
question: Где реализовывать runtime AOS-3?
recommended_option: CREATE_DEDICATED_REPOSITORY_NMF13579_AOS_3
repository_slug_proposal: NMF13579/aos-3
topology: MODULAR_MONOREPO_FIRST
alternatives:
  - USE_NOTEBOOK_AFTER_EXPLICIT_ROLE_CHANGE
  - ASSIGN_ANOTHER_EXISTING_REPOSITORY_AFTER_PREFLIGHT
reversibility: MEDIUM
latest_safe_decision_point: BEFORE_AOS_SCAFFOLDING_CONTRACT_R1_FREEZE
human_decision: NOT_RUN
```

Рекомендация сохраняет `notebook` как knowledge baseline и не смешивает документацию с runtime-кодом. В новом repository Product Runtime, Development Factory, Safety и Knowledge adapters остаются модулями одного monorepo; split допускается только после реальной ownership/release boundary.

`NMF13579/aos-3` — предлагаемое имя. Наличие свободного remote, его создание, visibility, default branch и доступы в `DOC-001` не проверялись и не разрешались.

### H1-002 — first segment, problem и desired outcome

```yaml
decision_id: H1-002
first_segment: NONPROGRAMMER_DOMAIN_EXPERT_GREENFIELD
primary_problem: P-003
supporting_problems: [P-001, P-002, P-015]
desired_outcome: REVIEWABLE_INTENT_WITH_VISIBLE_UNKNOWNS_AND_ONE_NEXT_ACTION
alternatives:
  - VIBE_CODER_EXISTING_REPOSITORY_DISCOVERY
  - DEVELOPER_TASK_EXECUTION_FIRST
reversibility: HIGH
latest_safe_decision_point: BEFORE_FIRST_FEATURE_CONTRACT
human_decision: NOT_RUN
```

Preferred actor описывает идею обычным языком и хочет понять, правильно ли агент понял проблему, что ещё неизвестно и что делать дальше. Existing-repository discovery откладывается: он добавляет repository preflight и gap mapping раньше проверки базовой product value.

### H1-003 — first vertical slice

```yaml
decision_id: H1-003
slice_id: INTAKE_TO_REVIEWABLE_INTENT_R1
trigger: USER_SUBMITS_FREE_FORM_PROJECT_IDEA
input: PLAIN_TEXT_REQUEST
outputs:
  - VERSIONED_INTENT_RECORD
  - VISIBLE_ASSUMPTIONS_AND_UNKNOWNS
  - MATERIAL_CLARIFICATION_QUESTIONS_OR_NONE
  - DURABLE_PROJECT_MEMORY_REFERENCE
  - PLAIN_LANGUAGE_STATUS
  - ONE_NEXT_ACTION
terminal_boundary: STOP_BEFORE_PRODUCT_SPEC_AND_EXECUTION
reversibility: HIGH
latest_safe_decision_point: BEFORE_FIRST_PRODUCT_RUNTIME_CONTRACT
human_decision: NOT_RUN
```

В slice не входят Product Spec, Feature Passport, architecture selection, Task Brief, execution пользовательского проекта, Git delivery, registry, RAG или web UI. Если вопрос material, результат остаётся `CLARIFYING`; пустой input не превращается в успешный Intent Record.

### H1-004 — first interface

```yaml
decision_id: H1-004
human_interface: CHAT_FIRST_GUIDED_FLOW
primary_adapter: CODEX_THIN_ADAPTER
canonical_machine_boundary: LOCAL_CLI_PLUS_VERSIONED_JSON
first_commands:
  - aos intake
  - aos status
  - aos next
  - aos details
alternatives:
  - INTERACTIVE_CLI_ONLY
  - LOCAL_WEB_UI
reversibility: MEDIUM_HIGH
latest_safe_decision_point: BEFORE_COMMAND_SURFACE_CONTRACT
human_decision: NOT_RUN
```

Chat является удобным interaction surface, но не Source of Truth. CLI/JSON делает поведение проверяемым и позволяет позже добавить ChatGPT Work, Claude Code, Cursor или local UI без переписывания Product Runtime.

### H1-005 — language, runtime и toolchain

```yaml
decision_id: H1-005
language: PYTHON
runtime: CPYTHON_3_14_6
python_compatibility_policy: SAME_MINOR_PATCH_UPDATES_ALLOWED_AFTER_TESTS
package_manager: UV
project_metadata: PYPROJECT_TOML
dependency_lock: UV_LOCK_COMMITTED
application_framework: NONE_FIRST_CYCLE
cli_foundation: PYTHON_STDLIB
test_runner: PYTEST_PINNED_BY_LOCKFILE
formatter_linter: RUFF_PINNED_BY_LOCKFILE
package_manager_exact_version: PIN_CURRENT_STABLE_IN_DOC_004_PREFLIGHT
alternatives:
  - TYPESCRIPT_NODE
  - PYTHON_WITH_APPLICATION_FRAMEWORK
reversibility: MEDIUM
latest_safe_decision_point: BEFORE_SCAFFOLD_GENERATION
human_decision: NOT_RUN
```

Python выбран за читаемость, быструю разработку deterministic tools и низкий порог сопровождения. На 2026-08-05 официальный current stable — Python `3.14.6`; `uv.lock` хранит exact dependency resolution и предназначен для reproducible cross-platform installs. Exact patch versions всех development dependencies и самого `uv` фиксируются в `AOS_SCAFFOLDING_CONTRACT_R1` после fresh preflight, а не становятся постоянным product decision.

Primary references: [Python downloads](https://www.python.org/downloads/), [uv project locking](https://docs.astral.sh/uv/concepts/projects/sync/), [uv project guide](https://docs.astral.sh/uv/guides/projects/).

### H1-006 — data и Project Memory persistence

```yaml
decision_id: H1-006
model: FILE_NO_DATABASE
format: VERSIONED_STRICT_JSON
project_memory_owner: .aos/state/project-memory.json
immutable_records: .aos/records/
write_model: ATOMIC_TEMP_WRITE_FSYNC_RENAME
database: NONE_FIRST_CYCLE
network_storage: NONE_FIRST_CYCLE
alternatives:
  - SQLITE_LOCAL
  - EXTERNAL_DATABASE
reversibility: MEDIUM_HIGH
latest_safe_decision_point: BEFORE_PROJECT_MEMORY_SCHEMA_FREEZE
human_decision: NOT_RUN
```

Project Memory хранит только current durable state и ссылки на immutable records. Intent revisions, decisions и reports не переписываются как история. `.aos/` классифицируется как project-owned state: setup/update не вправе молча перезаписывать его. SQLite рассматривается только после измеренной проблемы concurrency/query volume.

### H1-007 — supported environments

```yaml
decision_id: H1-007
primary_development:
  os: MACOS
  architecture: ARM64
  shell: ZSH
independent_ci:
  os: UBUNTU_24_04_LTS
  architecture: X86_64
runtime_python: CPYTHON_3_14_X
docker_required: false
windows_support: DEFERRED
offline_runtime: REQUIRED_FOR_FIRST_SLICE
network_during_setup: ALLOWED_WHEN_EXPLICIT
reversibility: HIGH
latest_safe_decision_point: BEFORE_SCAFFOLD_ACCEPTANCE_MATRIX
human_decision: NOT_RUN
```

Первый runtime slice не вызывает provider APIs и не требует сети. Это упрощает privacy boundary и делает dogfood воспроизводимым. Windows не объявляется неподдерживаемым навсегда — только не входит в first-cycle acceptance matrix.

### H1-008 — primary agent environment

```yaml
decision_id: H1-008
recommended_option: CODEX_LOCAL_CHECKOUT_ADAPTER_FIRST
common_contracts: AGENT_ENVIRONMENT_NEUTRAL
adapter_authority: NONE
future_adapters:
  - CHATGPT_WORK
  - CLAUDE_CODE
  - CURSOR
reversibility: HIGH
latest_safe_decision_point: BEFORE_FIRST_AGENT_ADAPTER_TASK
human_decision: NOT_RUN
```

Первый adapter должен быть thin: он маршрутизирует к общим contracts, но не копирует authority rules и не расширяет permissions. Provider routing, автоматический выбор моделей и multi-agent orchestration не входят в первый цикл.

### H1-009 — authenticity human decisions

```yaml
decision_id: H1-009
model: EXPLICIT_HUMAN_STATEMENT_BOUND_TO_EXACT_SUBJECT
required_fields:
  - decision_id
  - candidate_id
  - candidate_sha256
  - decision
  - actor_class: HUMAN
  - decision_timestamp
  - verbatim_or_normalized_human_statement
invalid_sources:
  - AGENT_RECOMMENDATION
  - GENERATED_ACCEPT_FIELD
  - UI_CLICK_WITHOUT_DECISION_RECORD
  - STALE_OR_DIFFERENT_SUBJECT_ACCEPTANCE
cryptographic_signature: DEFERRED
reversibility: MEDIUM
latest_safe_decision_point: BEFORE_FIRST_AUTHORITY_BEARING_RECORD
human_decision: NOT_RUN
```

Для v1 достаточно явной команды человека, связанной с exact candidate. Например: `ACCEPT AOS_3_H1_DECISION_PACKAGE_DRAFT_2026_08_05 <sha256>`. Криптографическая подпись, аккаунтный identity provider и central approval service откладываются до доказанной необходимости.

### H1-010 — proposed feature dispositions

Это предложения item-level решений, а не фактическое изменение `docs/06_Features.md`.

| Feature | Proposed human disposition | Boundary первого цикла | Почему сейчас |
|---|---|---|---|
| `FTR-001` | `REQUIRED` | Free-form intake → versioned Intent Record → material clarification/next route | Основная product value slice |
| `FTR-008` | `REQUIRED` | Только plain-language `Status / Next / Details`; без full tutor/workbench | Пользователь должен понимать state и next action |
| `FTR-011` | `REQUIRED` | Minimal Result Contract, `doctor` и `self-test`; full validator expansion later | Stable failure/`NOT_RUN` semantics и scaffold diagnostics |
| `FTR-016` | `REQUIRED` | Project Memory + resume; task-scoped Context Pack later | Slice должен переживать новую session |
| `FTR-019` | `REQUIRED` | Minimal read/write/network/Git classification; no runtime enforcement | Default-deny и external-content boundary |

`FTR-002…030`, кроме перечисленных, сохраняют `UNDECIDED`. В частности, `FTR-003` является логичным следующим Product Runtime slice, но не принимается и не реализуется автоматически вместе с первым.

```yaml
decision_id: H1-010
proposed_required: [FTR-001, FTR-008, FTR-011, FTR-016, FTR-019]
all_other_feature_dispositions: UNDECIDED
reversibility: MEDIUM
latest_safe_decision_point: BEFORE_FEATURE_SPECIFIC_CONTRACTS
human_decision: NOT_RUN
```

### H1-011 — first read-only route и Risk Profile timing

```yaml
decision_id: H1-011
read_only_commands:
  - aos --help
  - aos doctor
  - aos status
  - aos next
  - aos details
  - aos intake --preview
zero_write_required: true
first_write_route: aos intake --save
write_precondition: EXPLICIT_USER_CONFIRMATION_OF_RENDERED_INTENT
risk_profile_vocabulary: DEFER_TO_FIRST_WRITE_CAPABLE_IMPLEMENTATION_TASK_BRIEF
git_actions: OUT_OF_SCOPE
reversibility: HIGH
latest_safe_decision_point: BEFORE_COMMAND_SURFACE_FREEZE
human_decision: NOT_RUN
```

`Risk_Profile` остаётся human-owned. Отсрочка vocabulary не отменяет Minimal Safety Floor: missing authorization остаётся `NONE`, а read-only команды не должны создавать cache, logs или state в source tree.

## 5. Что намеренно не решается в H1

- exact directory tree и module names внутри нового repository;
- exact version самого `uv` и development dependencies до fresh D2 preflight;
- Product Spec ↔ Feature Passport final relationship;
- Product Feature Registry;
- existing-project integration module и Doctor-механизм для внешних проектов;
- execution adapter и controlled runner;
- Git automation;
- RAG/vector DB;
- provider/model routing;
- multi-agent coordination;
- web/SaaS UI;
- plugins и domain modules;
- regulated medical architecture;
- release/versioning policy после первого cycle.

Эти choices не блокируют `AOS_SCAFFOLDING_CONTRACT_R1` и первый Product Runtime contract.

## 6. Риски и mitigations

| Risk | Affected action | Mitigation |
|---|---|---|
| Новый repository ещё не создан и не проверен | D2 repository-specific paths и Task Brief | После H1 выполнить exact repository assignment/creation и fresh preflight |
| Chat adapter может смешать UI и authority | Human acceptance / execution | Chat только отображает recommendation; decision record bind к exact candidate |
| File persistence может усложниться при concurrency | Project Memory writes | Single-writer first cycle; SQLite admission только по измеренной проблеме |
| Пять selected features могут выглядеть как пять полных implementations | First slice scope | Feature-specific contracts фиксируют только перечисленную v1 boundary |
| Python/dependency versions меняются | Reproducible scaffold | CPython minor policy + exact lockfile + fresh D2 version observation |
| `FTR-003` не входит в первый slice | Полный idea→slice journey | Это намеренная stop boundary; `FTR-003` — candidate следующего slice после dogfood |

## 7. Решение, требуемое от человека

Допустимые ответы:

1. `ACCEPT_ALL_RECOMMENDATIONS` — принять H1-001…H1-011 одним решением.
2. `ACCEPT_WITH_CHANGES` — принять пакет с перечисленными поправками по `H1-*`.
3. `NEEDS_CHANGES` — вернуть package на correction, указав affected `H1-*`.
4. `DEFER` — не продолжать `DOC-002`.

До human decision:

```yaml
DOC-001:
  technical_result: PASS
  readiness: READY_FOR_HUMAN_REVIEW
H1_package:
  completeness: PASS
  human_decision: NOT_RUN
DOC-002: BLOCKED_PENDING_H1_DECISION
implementation_readiness: NOT_READY
implementation_authorization: NONE
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
stop: true
```

## 8. После принятия

Только после explicit H1 decision следующий bounded action:

```text
DOC-002
→ создать AOS_IMPLEMENTATION_DECISIONS_R1.md
→ записать только принятые H1 decisions с human provenance
→ оставить исправленные/непринятые поля UNDECIDED
→ провести focused semantic check
→ остановиться до DOC-003, repository creation и implementation
```
