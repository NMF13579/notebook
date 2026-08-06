---
document_type: AOS_IMPLEMENTATION_DECISION_RECORD
revision: R1
status: HUMAN_REVIEW_REQUIRED
claim_class: HUMAN_ACCEPTED_FACTS_RECORDED_FROM_EXACT_SUBJECT
authority: DERIVED_FROM_CURRENT_EXPLICIT_HUMAN_DECISION
authority_scope: H1-001_THROUGH_H1-011_IMPLEMENTATION_DECISIONS
task_id: DOC-002
technical_result: PASS
readiness: READY_FOR_HUMAN_REVIEW
artifact_human_acceptance: NOT_RUN
source_candidate_id: AOS_3_H1_DECISION_PACKAGE_DRAFT_2026_08_05
source_candidate_sha256: 415a6043b1acc269e3c4bff0c5fb1a908d7c1fae98b91444b316ac6a5be8de09
source_acceptance_record: planning/04_H1_ACCEPTANCE_RECORD.md
decision_actor_class: HUMAN
decision_date: 2026-08-05
knowledge_repository: NMF13579/notebook
implementation_repository_decision: NMF13579/aos-3
implementation_repository_creation: NOT_RUN
implementation_readiness: NOT_READY
implementation_authorization: NONE
git_authorization: NONE
created: 2026-08-05
updated: 2026-08-05
---

# AOS-3 — Implementation Decision Record R1

## 1. Назначение и authority

Этот документ — владелец exact implementation decisions, принятых человеком на checkpoint `H1` для первого цикла AOS-3.

Он переносит без расширения решения `H1-001…H1-011` из принятого exact subject:

- [`planning/03_H1_DECISION_PACKAGE.md`](planning/03_H1_DECISION_PACKAGE.md);
- [`planning/04_H1_ACCEPTANCE_RECORD.md`](planning/04_H1_ACCEPTANCE_RECORD.md).

```yaml
human_statement: ACCEPT_ALL_RECOMMENDATIONS AOS_3_H1_DECISION_PACKAGE_DRAFT_2026_08_05 415a6043b1acc269e3c4bff0c5fb1a908d7c1fae98b91444b316ac6a5be8de09
subject_match: PASS
accepted_decision_ids:
  - H1-001
  - H1-002
  - H1-003
  - H1-004
  - H1-005
  - H1-006
  - H1-007
  - H1-008
  - H1-009
  - H1-010
  - H1-011
recording_changes_to_accepted_meaning: NONE
```

Принятие исходного `H1` package делает перечисленные решения `HUMAN_ACCEPTED_FACT` в их declared scope. Оно не означает human acceptance этой производной revision как exact artifact, создание implementation repository, implementation readiness, Execution Authorization или Git authorization.

## 2. Project и repository identity

```yaml
project_name: AOS-3
knowledge_repository:
  slug: NMF13579/notebook
  role: ACTIVE_PROJECT_KNOWLEDGE_REPOSITORY
  runtime_code_allowed_here: false
implementation_repository:
  decision: CREATE_DEDICATED_REPOSITORY
  slug: NMF13579/aos-3
  topology: MODULAR_MONOREPO_FIRST
  creation: NOT_RUN
  remote_assignment: NOT_RUN
  visibility: UNDECIDED
  default_branch: UNDECIDED
```

`NMF13579/notebook` сохраняет роль knowledge repository. Решение о target slug не подтверждает доступность имени и не разрешает физическое создание repository. Product Runtime, Development Factory, Safety и Knowledge adapters проектируются как модули одного monorepo; split допускается после появления измеримой ownership или release boundary.

## 3. Первый actor, problem и desired outcome

```yaml
decision_id: H1-002
actor: NONPROGRAMMER_DOMAIN_EXPERT_GREENFIELD
primary_problem: P-003
supporting_problems: [P-001, P-002, P-015]
desired_outcome: REVIEWABLE_INTENT_WITH_VISIBLE_UNKNOWNS_AND_ONE_NEXT_ACTION
```

Первый actor описывает идею нового проекта обычным языком. AOS должен сохранить исходный intent, отделить problem и desired outcome от предполагаемого solution, показать assumptions и material unknowns, а затем вывести одно понятное next action.

Existing-repository discovery и developer task execution не входят в первый slice.

## 4. Первый Product Runtime vertical slice

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
```

First-cycle flow:

```text
free-form idea
→ preserved source request
→ problem / desired outcome separation
→ visible assumptions and unknowns
→ reviewable Intent Record
→ durable Project Memory reference
→ Status + one Next action
→ stop
```

В slice не входят Product Spec, Feature Passport, architecture selection, Task Brief, выполнение пользовательского проекта, Git delivery, Product Feature Registry, RAG или web UI. Пустой input не создаёт успешный Intent Record; material question оставляет flow в `CLARIFYING`.

## 5. Runtime / Factory boundary

```yaml
first_cycle_priority: PRODUCT_RUNTIME_FIRST
included_runtime_capabilities:
  - INTENT_INTAKE
  - REVIEWABLE_INTENT_RECORD
  - STATUS_NEXT_DETAILS
  - PROJECT_MEMORY_CONTINUITY
  - MINIMAL_RESULT_AND_SAFETY_SEMANTICS
development_factory_execution: DEFERRED
user_project_code_generation: OUT_OF_SCOPE
git_automation: OUT_OF_SCOPE
```

Первый цикл проверяет user-visible Product Runtime value. Development Factory, controlled runner и автоматическое выполнение задач не являются скрытой частью первого slice.

## 6. Interface contract direction

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
```

Chat — interaction surface, но не Source of Truth. CLI и versioned JSON являются deterministic boundary для tests и будущих adapters.

## 7. Language, runtime и toolchain

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
```

Exact version `uv`, development dependency versions и repository-specific commands остаются будущими fresh preflight facts. Их нельзя выводить из этого decision record без наблюдения target repository и источников toolchain.

## 8. Persistence и data ownership direction

```yaml
decision_id: H1-006
model: FILE_NO_DATABASE
format: VERSIONED_STRICT_JSON
project_memory_owner: .aos/state/project-memory.json
immutable_records: .aos/records/
write_model: ATOMIC_TEMP_WRITE_FSYNC_RENAME
database: NONE_FIRST_CYCLE
network_storage: NONE_FIRST_CYCLE
concurrency_model: SINGLE_WRITER_FIRST_CYCLE
```

Project Memory хранит current durable state и ссылки на immutable records. Intent revisions, decisions и reports сохраняются как отдельные записи, а не переписываются как история. `.aos/` является project-owned state и не может молча перезаписываться setup/update operations.

SQLite или external database требуют отдельного решения после измеримой проблемы concurrency или query volume.

## 9. Supported environments

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
```

Первый runtime slice не вызывает provider APIs и не требует сети. Windows не отвергнут как future environment, но не входит в first-cycle acceptance matrix.

## 10. Primary agent adapter

```yaml
decision_id: H1-008
primary_agent_environment: CODEX_LOCAL_CHECKOUT_ADAPTER_FIRST
common_contracts: AGENT_ENVIRONMENT_NEUTRAL
adapter_authority: NONE
future_adapters:
  - CHATGPT_WORK
  - CLAUDE_CODE
  - CURSOR
```

Thin adapter маршрутизирует к общим contracts, не копирует authority rules и не расширяет permissions. Provider routing, automatic model selection и multi-agent orchestration не входят в первый цикл.

## 11. Human decision authenticity

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
```

Human acceptance действительно только для exact subject, к которому привязано явное решение. Generated acceptance fields не создают human authority. Криптографическая подпись, identity provider и central approval service отложены до доказанной необходимости.

## 12. Selected feature dispositions

Решение `H1-010` задаёт item-level dispositions только для first-cycle boundaries:

| Feature | Human disposition | Exact first-cycle boundary |
|---|---|---|
| `FTR-001` | `REQUIRED` | Free-form intake → versioned Intent Record → material clarification/next route |
| `FTR-008` | `REQUIRED` | Plain-language `Status / Next / Details`; без full tutor/workbench |
| `FTR-011` | `REQUIRED` | Minimal Result Contract, `doctor` и `self-test`; расширенный validator позднее |
| `FTR-016` | `REQUIRED` | Project Memory + resume; task-scoped Context Pack позднее |
| `FTR-019` | `REQUIRED` | Minimal read/write/network/Git classification; без runtime enforcement |

```yaml
all_other_feature_dispositions: UNDECIDED
next_slice_candidate_without_disposition: FTR-003
```

`FTR-002…FTR-030`, кроме пяти перечисленных, сохраняют `UNDECIDED`. Принятые dispositions не означают полную реализацию всего dossier каждой feature: нормативна только указанная first-cycle boundary.

## 13. Read-only-first и protected/destructive decision model

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
missing_authorization: NONE
```

Read-only commands не создают cache, logs или state в source tree. Первый write route требует отдельного явного подтверждения уже отображённого Intent. `Risk_Profile` остаётся human-owned и должен быть определён в exact write-capable Task Brief до protected action.

Destructive operations, repository creation, runtime execution, network mutation и `Commit`/`Push`/`Merge`/`Release` не разрешены этим record и требуют отдельных exact human decisions.

## 14. Explicitly deferred и `UNDECIDED`

Следующие choices намеренно не приняты в `H1`:

- physical repository creation, availability, visibility, access model, default branch и branch policy;
- exact directory tree и module names;
- exact version `uv` и development dependencies до fresh `DOC-004` preflight;
- Product Spec ↔ Feature Passport final relationship;
- Product Feature Registry;
- existing-project integration module и Doctor для внешних проектов;
- execution adapter, controlled runner и runtime enforcement;
- Git automation;
- RAG/vector DB;
- provider/model routing и multi-agent coordination;
- web/SaaS UI;
- plugin и domain modules;
- regulated medical architecture;
- cryptographic human signature и identity provider;
- release/versioning policy после первого cycle;
- exact `Risk_Profile` vocabulary до первого write-capable implementation Task Brief;
- dispositions всех features кроме `FTR-001`, `FTR-008`, `FTR-011`, `FTR-016`, `FTR-019`.

Отсутствующие решения нельзя заполнять inference. Блокируется только action, которому конкретное решение необходимо.

## 15. Decision provenance и reversal conditions

| Decision | Actor | Date | Exact accepted subject | Reversal condition |
|---|---|---|---|---|
| `H1-001` | `HUMAN` | `2026-08-05` | `AOS_3_H1_DECISION_PACKAGE_DRAFT_2026_08_05@415a6043…de09` | До freeze `AOS_SCAFFOLDING_CONTRACT_R1`; смена требует нового target decision и repository preflight |
| `H1-002` | `HUMAN` | `2026-08-05` | то же | До первого feature contract; смена требует пересобрать actor/problem/outcome boundary |
| `H1-003` | `HUMAN` | `2026-08-05` | то же | До первого Product Runtime contract; после — новая slice revision и traceability update |
| `H1-004` | `HUMAN` | `2026-08-05` | то же | До command-surface contract; после — migration/compatibility decision |
| `H1-005` | `HUMAN` | `2026-08-05` | то же | До scaffold generation; после — новый toolchain decision и lock/scaffold validation |
| `H1-006` | `HUMAN` | `2026-08-05` | то же | До Project Memory schema freeze; после — data migration/recovery contract |
| `H1-007` | `HUMAN` | `2026-08-05` | то же | До scaffold acceptance matrix; расширение требует exact environment evidence |
| `H1-008` | `HUMAN` | `2026-08-05` | то же | До первого adapter task; новый adapter не меняет common-contract authority |
| `H1-009` | `HUMAN` | `2026-08-05` | то же | До первого authority-bearing record; изменение требует authenticity migration rule |
| `H1-010` | `HUMAN` | `2026-08-05` | то же | До feature-specific contracts; изменение требует explicit item-level disposition decision |
| `H1-011` | `HUMAN` | `2026-08-05` | то же | До command-surface freeze; write-capable task отдельно определяет risk vocabulary |

Полный SHA-256 accepted subject: `415a6043b1acc269e3c4bff0c5fb1a908d7c1fae98b91444b316ac6a5be8de09`.

Reversal — это новое explicit human decision для affected subject, а не автоматическое изменение агентом. Изменение одного решения не отменяет автоматически независимые decisions.

## 16. Текущая readiness boundary

```yaml
DOC-002:
  technical_result: PASS
  readiness: READY_FOR_HUMAN_REVIEW
  artifact_human_acceptance: NOT_RUN
DOC-003: NOT_RUN
implementation_repository_creation: NOT_RUN
remote_repository_assignment: NOT_RUN
runtime_implementation: NOT_RUN
implementation_readiness: NOT_READY
implementation_authorization: NONE
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
stop: true
```

`technical_result: PASS` означает только, что принятые `H1` decisions записаны без намеренного расширения. Он не является approval этой revision и не запускает следующий documentation task.
