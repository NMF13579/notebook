---
package: AOS_Project_Knowledge_Baseline
package_revision: R4-RU
updated: '2026-07-26'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
implementation_authorization: NONE
git_authorization: NONE
semantic_audit: COMPLETED_WITH_CORRECTIONS
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: dev
audited_source_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
audited_source_blob_sha: 5307c471efe8cc900c7348748294a60e73cd71fa
active_path: docs/06_Features.md
document_language: ru
technical_identifiers_language: en
document_role: AUTHORITATIVE_FEATURE_INVENTORY
authority_scope:
- feature_identity
- feature_dossiers
- source_crosswalk
feature_selection_authority: ITEM_SCOPED_HUMAN_DECISION_ONLY
implementation_planning_readiness: REQUIRES_FEATURE_SPECIFIC_CONTRACT
---

# 06 — Фичи

## 1. Назначение и статус

Принятый единый inventory известных фич и каталог design-level dossiers нового AOS. Принятие inventory не является item-level feature selection.

```yaml
catalog_status: HUMAN_ACCEPTED_INVENTORY
inventory_owner_after_acceptance: 06_Features.md
feature_count: 30
human_feature_selection: PARTIALLY_DECIDED_FOR_X1
implementation_verification: NOT_RUN
```

Наличие в каталоге ≠ приоритет roadmap ≠ принятая архитектура ≠ разрешение на реализацию.

## 2. Оси статуса

```text
Решение человека:
SELECT_FOR_X1 | SUPPORTING_CONTROL_ONLY | REQUIRED | OPTIONAL | DEFERRED | REFERENCE_ONLY | REJECTED | UNDECIDED

Рекомендация синтеза:
KEEP | SIMPLIFY | DEFER | REFERENCE_ONLY

Зрелость реализации:
NOT_ASSIGNED | DOCUMENTATION | SKELETON | PROTOTYPE | PARTIALLY_WORKING | PRODUCT_RUNTIME
```

## 3. Обязательные поля dossier

Problem/users, trigger/preconditions, inputs/outputs, main flow, states, failures/recovery, dependencies, authority boundaries, acceptance, negative scenarios, minimal model, targeted research, non-goals and crosswalk.

## 3.1. Граница готовности dossiers

Dossiers пригодны для отбора, сравнения и подготовки feature-specific Product Contract. Они не являются готовыми implementation specifications.

Следующие разделы содержат shared design defaults и требуют уточнения для выбранной feature: target users, preconditions, inputs, state effects, failure/recovery defaults, minimal implementation model и non-goals. Перед Task Brief необходимо заменить generic defaults точными feature-specific contracts, schemas, examples и executable acceptance tests.

```text
accepted inventory ≠ selected feature
selected feature ≠ implementation-ready contract
feature dossier ≠ execution authorization
```

## 4. Индекс каталога

| ID | Семейство фич | Слой | Рекомендация | Решение человека |
|---|---|---|---|---|
| `FTR-001` | Приём намерения, проблемное интервью и уточнение результата | Product Runtime | `KEEP` | `SELECT_FOR_X1` |
| `FTR-002` | Read-only исследование проекта, карта возможностей и реестр gaps/conflicts | Product Runtime | `KEEP` | `UNDECIDED` |
| `FTR-003` | Спецификация продукта, паспорт фичи и выбор первого вертикального среза | Product Runtime | `KEEP` | `SELECT_FOR_X1` |
| `FTR-004` | Управляемый bootstrap, безопасная установка/обновление/удаление и First-Start | Product Runtime / Installation Boundary | `KEEP` | `UNDECIDED` |
| `FTR-005` | Проверка необходимости архитектуры, сравнение вариантов, ADR и traceability | Product Runtime Support / Architecture Boundary | `KEEP` | `SUPPORTING_CONTROL_ONLY` |
| `FTR-006` | Task Brief, подтверждение scope, Execution Authorization и Stage Report | Product Runtime / Development Factory Boundary | `KEEP` | `SUPPORTING_CONTROL_ONLY` |
| `FTR-007` | Иерархический backlog, lazy decomposition, кандидаты задач и queue | Development Factory | `DEFER` | `UNDECIDED` |
| `FTR-008` | Простая панель управления: Status / Next / Details, tutor и closure UX | Product Runtime | `KEEP` | `UNDECIDED` |
| `FTR-009` | Preflight репозитория и действий с точным execution preview | Development Factory / Safety Boundary | `KEEP` | `UNDECIDED` |
| `FTR-010` | Scoped execution workflow, Controlled Guard и безопасные runner kernels | Development Factory | `SIMPLIFY` | `UNDECIDED` |
| `FTR-011` | Единый Result Contract, Unified Validate, Doctor и Self-Test | Product Runtime Support / Development Factory | `KEEP` | `SUPPORTING_CONTROL_ONLY` |
| `FTR-012` | Сбор Evidence, компактный human review, semantic guard и Human Decision Record | Product Runtime / Review Boundary | `KEEP` | `SUPPORTING_CONTROL_ONLY` |
| `FTR-013` | Сверка diff/scope, изолированный validation subject и candidate freeze | Development Factory / Validation Boundary | `KEEP` | `SUPPORTING_CONTROL_ONLY` |
| `FTR-014` | Recovery, resume, rollback, denied-action log и session handoff | Product Runtime / Development Factory Boundary | `KEEP` | `UNDECIDED` |
| `FTR-015` | Завершение Git lifecycle, remote state и независимые permissions Commit/Push/Merge/Release | Development Factory / Delivery Boundary | `KEEP` | `UNDECIDED` |
| `FTR-016` | Project Memory, непрерывность sessions и task-scoped Context Pack | Product Runtime / Development Factory Boundary | `KEEP` | `UNDECIDED` |
| `FTR-017` | RAG-light индекс контекста и поиск | Supporting Runtime | `DEFER` | `UNDECIDED` |
| `FTR-018` | Advisory routing моделей, явные роли, аудит routing и оценка providers | Development Factory | `DEFER` | `UNDECIDED` |
| `FTR-019` | Action Trust Boundary, классификатор permissions и граница external content | Minimal Safety Floor | `KEEP` | `UNDECIDED` |
| `FTR-020` | Progressive Governance, Runtime Enforcement и изолированные execution modes | Governance / Runtime Enforcement | `DEFER` | `UNDECIDED` |
| `FTR-021` | Обнаружение registry/drift, Source-of-Truth guard и authenticity human decisions | Development Factory / Governance Support | `DEFER` | `UNDECIDED` |
| `FTR-022` | Библиотека решений и patterns, fit matrix и reusable UX/engineering patterns | Knowledge Support | `KEEP` | `UNDECIDED` |
| `FTR-023` | Advisory CI, smoke-проверки, safety regression fixtures и quality gates | Development Factory | `DEFER` | `UNDECIDED` |
| `FTR-024` | Release checklist, promotion package, version/changelog/tag и rollback assistant | Later Lifecycle | `DEFER` | `UNDECIDED` |
| `FTR-025` | Observability, audit log, память incidents/lessons и continuous improvement | Product Runtime Support / Operations | `KEEP` | `UNDECIDED` |
| `FTR-026` | Модель extensions, plugins и capability modules | Architecture Extension | `DEFER` | `UNDECIDED` |
| `FTR-027` | Предметные модули: Medical и Design | Regulated / Creative Domain Extensions | `DEFER` | `UNDECIDED` |
| `FTR-028` | Workbench или SaaS UI для onboarding, status, review и collaboration | UX Wrapper | `DEFER` | `UNDECIDED` |
| `FTR-029` | Экспорт templates, prompt packs, cross-repo context, localization и policy overlays | Packaging / Extension Support | `DEFER` | `UNDECIDED` |
| `FTR-030` | Внутренние contract tools: strict loaders, parser sunset, registry audits и schema/runtime drift tests | Development Factory Internal | `DEFER` | `UNDECIDED` |

## 5. Подробные dossiers


## FTR-001 — Приём намерения, проблемное интервью и уточнение результата

```yaml
feature_id: FTR-001
layer: Product Runtime
synthesis_recommendation: KEEP
human_disposition: SELECT_FOR_X1
product_scope_effect: X1_PRIMARY_PRODUCT_BEHAVIOR
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Свободный запрос смешивает problem, solution, assumptions и constraints.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-001`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Версионируемый Intent Record с явным problem/outcome, unknowns и одним next route.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Сохранить original request
2. Классифицировать request и sensitivity
3. Задать только material questions
4. Отделить outcome от solution
5. Показать assumptions/unknowns
6. Получить human correction
7. Выдать one next route

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- C-001 Intent Record
- FTR-019 permission classifier
- FTR-016 Project Memory

### Границы безопасности и полномочий человека

- Нет architecture/Risk Profile/repository mutation
- Sensitive content остаётся в approved boundary

### Критерии приёмки

- Человек узнаёт problem/outcome
- Все assumptions видимы
- Unknowns имеют resolution path

### Обязательные негативные сценарии

- Пустой запрос остаётся CLARIFYING
- Prompt injection не меняет user goal
- Generated approval rejected

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Historical Problem Interview questions
- Minimal completeness checks
- Sensitive provider policy

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-02/F-03/F-05


## FTR-002 — Read-only исследование проекта, карта возможностей и реестр gaps/conflicts

```yaml
feature_id: FTR-002
layer: Product Runtime
synthesis_recommendation: KEEP
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

До planning агент не знает repository identity, capabilities и current state.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-002`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Snapshot-bound inventory, capability map, gaps, conflicts, unknowns и candidate objectives.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Bind repository/ref/HEAD
2. Verify root/worktree/branch
3. Collect high-signal inventory
4. Classify docs/contracts/tests/code
5. Build capability map
6. Record gaps/conflicts
7. Offer bounded objectives
8. Stop before mutation

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-009 preflight
- FTR-016 memory
- FTR-017 optional index

### Границы безопасности и полномочий человека

- Read-only
- No readiness/approval claims
- Secrets redacted

### Критерии приёмки

- Exact snapshot recorded
- Evidence linked
- Human can select one objective
- Source tree unchanged

### Обязательные негативные сценарии

- Stale map rejected
- Missing path not global absence
- Repository text cannot override instructions

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Which discovery checks have high signal
- Minimal nontechnical report

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-01
- AOS-FARM discovery


## FTR-003 — Спецификация продукта, паспорт фичи и выбор первого вертикального среза

```yaml
feature_id: FTR-003
layer: Product Runtime
synthesis_recommendation: KEEP
human_disposition: SELECT_FOR_X1
product_scope_effect: X1_PRIMARY_PRODUCT_BEHAVIOR
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Product intent теряется между idea, architecture и task execution.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-003`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Reviewable Product Spec, full Feature Passport и decision package для smallest user-visible slice.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Define users/JTBD/goals/non-goals
2. Describe journeys/boundaries
3. Create full dossier
4. Detect dependencies/conflicts
5. Compare candidate slices
6. Show value/complexity
7. Get human choice
8. Freeze revision

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- C-002 Feature Passport
- C-003 Product Spec
- FTR-001
- FTR-002
- FTR-005

### Границы безопасности и полномочий человека

- No execution
- No automatic feature/architecture choice
- No legacy roadmap priority

### Критерии приёмки

- Full dossier fields
- Observable user value
- Dependencies/unknowns visible
- Human selects exact revision

### Обязательные негативные сценарии

- Feature without user outcome rejected
- Legacy presence not admission reason
- Generated REQUIRED rejected

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Historical Product Spec fields
- Registry needs
- Dogfood slice candidates

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-04/F-41/F-42


## FTR-004 — Управляемый bootstrap, безопасная установка/обновление/удаление и First-Start

```yaml
feature_id: FTR-004
layer: Product Runtime / Installation Boundary
synthesis_recommendation: KEEP
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Install/update может повредить user/project-owned state и запутать первого пользователя.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-004`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Preview-first installation with ownership classes, exact apply, verification, recovery и first safe command.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Verify package/target
2. Inventory paths
3. Classify ownership
4. Render exact preview/conflicts
5. Get apply authorization
6. Atomic/journaled apply
7. Verify result
8. Show first-start/rollback

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- C-013 Manifest
- FTR-009
- FTR-014
- FTR-011

### Границы безопасности и полномочий человека

- No hidden writes
- Preserve user/project state
- Destructive uninstall separate

### Критерии приёмки

- Dry-run side-effect free
- Apply matches preview
- Idempotent repeat
- First-start understandable

### Обязательные негативные сценарии

- User file never overwritten silently
- Interrupted update recoverable
- Wrong repo blocks apply
- Uninstall without auth stops

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Historical installer behavior
- First-start friction
- Ownership edge cases

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-33
- AOS-FARM installer


## FTR-005 — Проверка необходимости архитектуры, сравнение вариантов, ADR и traceability

```yaml
feature_id: FTR-005
layer: Product Runtime Support / Architecture Boundary
synthesis_recommendation: KEEP
human_disposition: SUPPORTING_CONTROL_ONLY
product_scope_effect: X1_SUPPORTING_CONTROL_ONLY
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Architecture work либо пропускается, либо разрастается без связи с feature.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-005`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Decision-ready ADR process: need check, distinct options, tradeoffs, human choice and task traceability.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Check if ADR needed
2. Define exact question
3. Create distinct options
4. Compare tradeoffs/risks
5. Show evidence/unknowns
6. Get human decision
7. Record consequences/reversal
8. Link task

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- C-004 ADR
- FTR-003
- FTR-002

### Границы безопасности и полномочий человека

- Human selects architecture
- No dependency install
- DRAFT ADR no execution

### Критерии приёмки

- Need/no-need justified
- Options comparable
- Decision exact
- Traceability present

### Обязательные негативные сценарии

- Trivial task avoids ADR
- Single preselected option rejected
- Stale repo fact invalidates comparison

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Historical architecture checkpoints
- Minimal need heuristic

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AOS architecture lifecycle
- AgentOS architecture synthesis


## FTR-006 — Task Brief, подтверждение scope, Execution Authorization и Stage Report

```yaml
feature_id: FTR-006
layer: Product Runtime / Development Factory Boundary
synthesis_recommendation: KEEP
human_disposition: SUPPORTING_CONTROL_ONLY
product_scope_effect: X1_SUPPORTING_CONTROL_ONLY
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Free-form request не должен становиться executable work автоматически.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-006`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Bounded Task Brief, separate human authorization, preflight requirements and matching terminal report.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Define goal/outcome
2. Limit paths/operations
3. Record assumptions/unknowns
4. Propose risk
5. Define checks/stop conditions
6. Validate completeness
7. Get separate authorization
8. Emit report after execution

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- C-005 Task Brief
- C-006 Authorization
- FTR-009
- FTR-012

### Границы безопасности и полномочий человека

- Task Brief ≠ permission
- Risk Profile human-owned
- No implicit Git
- One active task

### Критерии приёмки

- Required fields complete
- Scope machine-checkable
- Auth exact/human-originated
- Report matches actual change

### Обязательные негативные сценарии

- Malformed idle rejected
- Copied/stale auth rejected
- Unexpected path blocks
- NOT_RUN cannot be PASS

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Historical Task Contract schemas
- Routine vs protected fields
- Idle-state failures

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-10/F-12
- Compact Safe Path


## FTR-007 — Иерархический backlog, lazy decomposition, кандидаты задач и queue

```yaml
feature_id: FTR-007
layer: Development Factory
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Large work needs ordering, but full upfront backlog creates premature complexity.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-007`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Candidate hierarchy created only as needed, preserving parent-child acceptance and human activation.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Define parent acceptance
2. Create only near-term children
3. Link contribution/dependencies
4. Detect blockers
5. Suggest order
6. Human selects one active task

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-003
- FTR-006
- FTR-016

### Границы безопасности и полномочий человека

- One active task
- No automatic activation
- Queue derived, not SoT

### Критерии приёмки

- Each child contributes
- Dependencies explicit
- Human selects next

### Обязательные негативные сценарии

- Orphan child rejected
- Circular dependency detected
- Closed child not parent completion

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Historical queue semantics
- When decomposition pays off

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-13
- AOS decomposition


## FTR-008 — Простая панель управления: Status / Next / Details, tutor и closure UX

```yaml
feature_id: FTR-008
layer: Product Runtime
synthesis_recommendation: KEEP
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Nontechnical user cannot understand state, blocker and next action.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-008`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Plain-language current status, one next action, optional details and closure explanation from source-owned records.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Load source-owned state
2. Refresh mutable facts
3. Determine blockers/permissions
4. Render concise status
5. Show one next action
6. Link details

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-016
- FTR-011
- FTR-012

### Границы безопасности и полномочий человека

- Display-only by default
- No lifecycle mutation
- UI ≠ approval

### Критерии приёмки

- User explains state
- One action actionable
- Sources/freshness visible

### Обязательные негативные сценарии

- Stale state cannot show READY
- Multiple next actions avoided
- NOT_RUN remains visible

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- First-contact usability
- Historical closure wording

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-17/F-23/F-39
- AOS Simple Control Surface


## FTR-009 — Preflight репозитория и действий с точным execution preview

```yaml
feature_id: FTR-009
layer: Development Factory / Safety Boundary
synthesis_recommendation: KEEP
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Mutation without exact identity, scope and environment risks contamination.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-009`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Read-only preflight binding repo/worktree/branch/HEAD/baseline/diff, permissions and exact actions.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Verify root/identity
2. Bind branch/HEAD/baseline
3. Classify dirty state
4. Normalize paths
5. Check environment/network/remote
6. Render actions
7. Freeze preview

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-006
- FTR-019
- FTR-014

### Границы безопасности и полномочий человека

- Read-only
- No raw secrets
- No implicit permission

### Критерии приёмки

- Zero writes
- Exact subject/actions
- Dirty state classified

### Обязательные негативные сценарии

- Changed HEAD invalidates preview
- Traversal/symlink rejected
- User files untouched

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Historical trust tables
- Cross-platform paths

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AOS-FARM preflight
- AOS-02 preview


## FTR-010 — Scoped execution workflow, Controlled Guard и безопасные runner kernels

```yaml
feature_id: FTR-010
layer: Development Factory
synthesis_recommendation: SIMPLIFY
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Scope in prose does not constrain actual mutation.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-010`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Thin executor consuming exact authorization/preview, journaling writes and reconciling actual diff.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Validate auth
2. Check preview freshness
3. Execute smallest action
4. Journal mutations
5. Run targeted checks
6. Reconcile diff
7. Stop with report

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-006
- FTR-009
- FTR-014
- FTR-013

### Границы безопасности и полномочий человека

- No scope expansion
- No Git delivery
- No privilege escalation
- One stage

### Критерии приёмки

- Only allowed paths change
- Diff reconciled
- Failure recoverable
- Auth consumed once

### Обязательные негативные сценарии

- Unexpected path blocks
- Stale preview rejected
- No automatic correction/retry after boundary change

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Minimal runner primitives
- Sandbox only after proof

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-14/F-21
- AOS controlled guard


## FTR-011 — Единый Result Contract, Unified Validate, Doctor и Self-Test

```yaml
feature_id: FTR-011
layer: Product Runtime Support / Development Factory
synthesis_recommendation: KEEP
human_disposition: SUPPORTING_CONTROL_ONLY
product_scope_effect: X1_SUPPORTING_CONTROL_ONLY
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Different validators/CLI paths produce incompatible status and false green.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-011`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

One ValidationEnvelope and official entrypoint preserving NOT_RUN, limitations and exit semantics.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Load strict contract
2. Verify subject/environment
3. Run required/optional checks
4. Record each result
5. Aggregate fail-closed
6. Emit machine/human report

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- C-009 ValidationEnvelope
- FTR-013
- FTR-023

### Границы безопасности и полномочий человека

- PASS never approval
- Read-only checks zero writes
- One official entrypoint

### Критерии приёмки

- Stable vocabulary
- Every exit machine-readable
- Required NOT_RUN prevents PASS

### Обязательные негативные сценарии

- Unknown enum rejected
- Exit 0 on failure rejected
- Wrong interpreter detected

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Historical entrypoint conflicts
- Minimal schema
- Doctor UX

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-19/F-20
- AOS ValidationEnvelope


## FTR-012 — Сбор Evidence, компактный human review, semantic guard и Human Decision Record

```yaml
feature_id: FTR-012
layer: Product Runtime / Review Boundary
synthesis_recommendation: KEEP
human_disposition: SUPPORTING_CONTROL_ONLY
product_scope_effect: X1_SUPPORTING_CONTROL_ONLY
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Technical output is difficult to review and may be mistaken for acceptance.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-012`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

One candidate-bound review package plus separate explicit Human Decision Record.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Verify candidate binding
2. Map Evidence to criteria
3. Summarize user impact
4. Expose NOT_RUN/limitations
5. Offer decision options
6. Capture human decision

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-011
- FTR-013
- C-011 Human Review

### Границы безопасности и полномочий человека

- Agent cannot approve
- Evidence ≠ authority
- Decision exact to subject

### Критерии приёмки

- Every criterion visible
- User impact understandable
- Actor/time recorded

### Обязательные негативные сценарии

- Missing actor rejected
- Generated ACCEPT rejected
- Stale candidate cannot be accepted

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Decision authenticity options
- Review usability dogfood

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-18/F-20
- AOS Human Review Package


## FTR-013 — Сверка diff/scope, изолированный validation subject и candidate freeze

```yaml
feature_id: FTR-013
layer: Development Factory / Validation Boundary
synthesis_recommendation: KEEP
human_disposition: SUPPORTING_CONTROL_ONLY
product_scope_effect: X1_SUPPORTING_CONTROL_ONLY
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Validation can target a moving or contaminated candidate.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-013`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Immutable subject bound to exact baseline/candidate with isolated validation and scope reconciliation.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Finalize evidence inputs
2. Compute identity
3. Freeze subject
4. Create isolated copy if needed
5. Validate exact subject
6. Compare Task Brief/preview/diff

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-009
- FTR-010
- FTR-011

### Границы безопасности и полномочий человека

- Validation no mutation
- Exact identity binding
- No provisional identity claim

### Критерии приёмки

- Any byte change detected
- Scope matches Task Brief
- Import provenance recorded

### Обязательные негативные сценарии

- Move HEAD invalidates
- Self-reference rejected
- Live checkout mismatch detected

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Identity model for uncommitted candidate
- Cross-platform isolation

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AOS-FARM candidate freeze
- AOS-02 identity


## FTR-014 — Recovery, resume, rollback, denied-action log и session handoff

```yaml
feature_id: FTR-014
layer: Product Runtime / Development Factory Boundary
synthesis_recommendation: KEEP
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Failure or interruption loses actual state and invites unsafe retry.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-014`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Recovery package preserving journal/candidate/findings, bounded resume/rollback and one next action.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Stop mutation
2. Preserve state/logs
3. Classify partial writes
4. Reconcile intended/actual
5. Determine options
6. Require human decision if needed
7. Resume after recheck

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-010
- FTR-016
- FTR-019

### Границы безопасности и полномочий человека

- No automatic authority/scope transition
- Destructive rollback separate
- One next action

### Критерии приёмки

- Partial writes detectable
- Resume reproducible
- Denied action visible
- No data loss

### Обязательные негативные сценарии

- Retry after permission violation rejected
- Stale handoff blocks action
- Unknown not READY

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Historical recovery packages
- Minimum handoff fields
- Resume UX

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-17/F-22/F-23
- AOS recovery


## FTR-015 — Завершение Git lifecycle, remote state и независимые permissions Commit/Push/Merge/Release

```yaml
feature_id: FTR-015
layer: Development Factory / Delivery Boundary
synthesis_recommendation: KEEP
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Edit, commit, push, merge and release are commonly collapsed.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-015`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Closure report and separately authorized Git/release actions bound to exact candidate and current remote state.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Verify local subject
2. Check remote/PR state
3. Confirm review/acceptance
4. Request exact action auth
5. Perform one action
6. Reverify
7. Stop

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- C-014 Git Delivery
- FTR-012
- FTR-013

### Границы безопасности и полномочий человека

- Each action separate
- No force default
- Secrets redacted

### Критерии приёмки

- Unauthorized action blocked
- Stale state invalidates readiness
- Exact result recorded

### Обязательные негативные сценарии

- Commit does not push
- Push does not merge
- Merge does not release
- Changed candidate revalidated

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Branch protection/PR states
- Release target requirements

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AOS-FARM Git guards
- Merge authorization


## FTR-016 — Project Memory, непрерывность sessions и task-scoped Context Pack

```yaml
feature_id: FTR-016
layer: Product Runtime / Development Factory Boundary
synthesis_recommendation: KEEP
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Context is lost between sessions/tools; agents read too much or omit relevant rules.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-016`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Compact durable state plus explained minimal context with provenance and freshness.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Load accepted facts
2. Refresh mutable repo facts
3. Select relevant sources
4. Explain inclusion
5. Check hashes/freshness
6. Emit context/handoff

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-008
- FTR-017 optional
- 00_Core precedence

### Границы безопасности и полномочий человека

- Derived memory has no independent authority
- No hidden background mutation
- Sensitive context policy

### Критерии приёмки

- New session resumes correctly
- Sources/reasons visible
- Stale data detected

### Обязательные негативные сценарии

- Old HEAD blocks execution claim
- Missing source not silently omitted
- Index cannot promote proposal

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Resume dogfood
- Context selection heuristics

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-23/F-25
- AOS handoff


## FTR-017 — RAG-light индекс контекста и поиск

```yaml
feature_id: FTR-017
layer: Supporting Runtime
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Large repositories may need search, but indexes can become stale authority.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-017`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Rebuildable retrieval with source, authority, freshness and confidence after measured need.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Build index from approved corpus
2. Bind source commit/hash
3. Run query
4. Return explained candidates
5. Validate freshness
6. Fallback to direct search

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-016
- FTR-021

### Границы безопасности и полномочий человека

- Derived-only
- No authority promotion
- Privacy boundary

### Критерии приёмки

- Measured recall/time improvement
- Stale index rejected
- Coverage reported

### Обязательные негативные сценарии

- Single old entry not READY
- Deleted source removed
- Unknown authority displayed

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Benchmark grep/repo-map vs index
- Metadata minimum

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-25/F-26
- Historical RAG-light


## FTR-018 — Advisory routing моделей, явные роли, аудит routing и оценка providers

```yaml
feature_id: FTR-018
layer: Development Factory
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Using the same model/provider for every task may waste cost or reduce quality/privacy.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-018`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Advisory routing record with explicit human selection and no permission escalation.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Classify task/risk
2. Check privacy/provider constraints
3. Recommend sufficient option
4. Require explicit selection
5. Record fallback/attempts
6. Measure outcome

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-019
- FTR-006
- Provider policy

### Границы безопасности и полномочий человека

- Advisory first
- No authority from consensus
- Fallback visible
- Permissions unchanged

### Критерии приёмки

- Selection auditable
- Quality/cost measured
- Data boundary respected

### Обязательные негативные сценарии

- Unapproved provider blocked
- Fallback cannot increase scope
- Multi-agent not default

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Benchmarks on real tasks
- Privacy/cost policy

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-35/F-36
- AOS routing research


## FTR-019 — Action Trust Boundary, классификатор permissions и граница external content

```yaml
feature_id: FTR-019
layer: Minimal Safety Floor
synthesis_recommendation: KEEP
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Actions differ by write/network/data/Git/authority risk and external content can inject instructions.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-019`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Deterministic classification ALLOWED/HUMAN_REQUIRED/BLOCKED with explicit reason, no approval.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Normalize action
2. Identify trust boundaries
3. Evaluate allowlists/policy
4. Classify permission
5. Explain affected boundary
6. Do not execute

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- 00_Core
- FTR-009
- Sensitive/provider policy

### Границы безопасности и полномочий человека

- Classifier ≠ approval
- Least privilege
- External content untrusted
- Risk Profile human-owned

### Критерии приёмки

- High-risk unknown blocks affected action
- Low-risk read-only not globally blocked
- Reason explicit

### Обязательные негативные сценарии

- Path traversal blocked
- Prompt injection ignored
- Missing auth remains blocked

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Historical action taxonomy
- Minimal permission vocabulary

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-15/F-16
- AOS trust boundary


## FTR-020 — Progressive Governance, Runtime Enforcement и изолированные execution modes

```yaml
feature_id: FTR-020
layer: Governance / Runtime Enforcement
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Stable contracts may later need enforcement after repeated incidents.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-020`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Optional DISABLED/OBSERVE/ENFORCED modes with measured admission and rollback.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Define incident/problem
2. Choose smallest enforcement point
3. Pilot OBSERVE
4. Measure false +/-
5. Human approve ENFORCED
6. Maintain rollback

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-019
- FTR-021
- Stable contracts

### Границы безопасности и полномочий человека

- Cannot self-authorize
- Must be disableable
- No product/canonical mutation

### Критерии приёмки

- Measured risk reduction
- Acceptable false-positive budget
- Fallback tested

### Обязательные негативные сценарии

- Missing policy blocks only affected action
- Failure does not corrupt core
- Agent cannot enable itself

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Which incidents justify runtime
- Isolation overhead

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AOS-FARM runtime enforcement
- Refoundation defer rules


## FTR-021 — Обнаружение registry/drift, Source-of-Truth guard и authenticity human decisions

```yaml
feature_id: FTR-021
layer: Development Factory / Governance Support
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Docs/schema/CLI/code/tests and decision records can diverge.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-021`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Read-only consistency/authenticity checks with one owner per fact and snapshot-bound findings.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Build derived artifact graph
2. Compare owners/representations
3. Check freshness/links
4. Verify decision actor/subject
5. Report findings
6. Do not auto-fix

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-017
- FTR-012
- FTR-030

### Границы безопасности и полномочий человека

- Derived-only
- Read-only default
- Missing authenticity blocks affected action

### Критерии приёмки

- Known drift detected
- One owner per fact
- Reports snapshot-bound

### Обязательные негативные сценарии

- Stale report not current PASS
- Unknown actor rejects authority
- Duplicate rule flagged not deleted

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Historical drift signals
- Decision identity mechanisms

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-26/F-29
- AOS-02 authenticity gaps


## FTR-022 — Библиотека решений и patterns, fit matrix и reusable UX/engineering patterns

```yaml
feature_id: FTR-022
layer: Knowledge Support
synthesis_recommendation: KEEP
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Teams repeatedly rediscover solutions and repeat known failures.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-022`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Curated problem→context→solution→tradeoff→failure→test patterns with explicit applicability.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Identify pattern
2. Compare target context
3. Assess fit/anti-fit
4. Show tradeoffs/alternatives
5. Select only by design decision
6. Record result

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-005
- FTR-025
- 05_Reference

### Границы безопасности и полномочий человека

- Reference authority none by default
- Applicability explicit

### Критерии приёмки

- Agent explains why fit
- Failures/tests included
- Alternative visible

### Обязательные негативные сценарии

- Different context prevents blind reuse
- Deprecated pattern not silently recommended

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Reusable historical solutions
- Taxonomy by problem

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AOS pattern discussions


## FTR-023 — Advisory CI, smoke-проверки, safety regression fixtures и quality gates

```yaml
feature_id: FTR-023
layer: Development Factory
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Manual checks may miss regressions; CI can be mistaken for approval.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-023`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Pinned technical checks with negative fixtures and explicit NOT_RUN, no lifecycle authority.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Select profile
2. Run structure/contract/negative tests
3. Run relevant regression
4. Record optional NOT_RUN
5. Publish technical result
6. Stop before approval

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-011
- FTR-013
- Regression catalog

### Границы безопасности и полномочий человека

- CI ≠ approval
- No lifecycle mutation
- Subject-bound evidence

### Критерии приёмки

- Known negatives fail
- Fast feedback
- Required checks explicit

### Обязательные негативные сценарии

- Required test missing prevents PASS
- CI cannot merge
- Changed subject invalidates

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Runtime/toolchain after selection
- Check duration budgets

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS quality/security
- AOS safety fixtures


## FTR-024 — Release checklist, promotion package, version/changelog/tag и rollback assistant

```yaml
feature_id: FTR-024
layer: Later Lifecycle
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Release combines accepted code, versioning, deployment and rollback and must remain separate from merge.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-024`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Decision-ready release package bound to exact merged artifact and explicit release authorization.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Bind merged artifact
2. Compile changes/compatibility
3. Check blockers
4. Prepare version/tag
5. Request release auth
6. Execute one action
7. Verify

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-015
- FTR-011
- FTR-014

### Границы безопасности и полномочий человека

- Release separate from merge
- No production mutation without auth
- No secrets

### Критерии приёмки

- Artifact/version exact
- Rollback bounded
- Post-release check defined

### Обязательные негативные сценарии

- Stale SHA rejected
- Missing blocker visible
- Failed release not complete

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Actual distribution model
- Versioning policy

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AOS-FARM release proposals


## FTR-025 — Observability, audit log, память incidents/lessons и continuous improvement

```yaml
feature_id: FTR-025
layer: Product Runtime Support / Operations
synthesis_recommendation: KEEP
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Material outcomes and failures are lost, causing recurrence.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-025`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Minimal incident record that produces human-reviewed lesson and regression candidates.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Record event
2. Bind Evidence
3. Analyze root-cause candidate
4. Define correction
5. Propose lesson/check
6. Human review
7. Track recurrence

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-014
- FTR-021
- 04_Lessons

### Границы безопасности и полномочий человека

- No automatic rule mutation
- Privacy/minimization
- Evidence ≠ decision

### Критерии приёмки

- Incident searchable
- Lesson source-linked
- Regression defined

### Обязательные негативные сценарии

- Missing evidence keeps root cause candidate
- Rejected lesson no policy change
- Log failure not hide incident

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Useful event taxonomy
- Retention/privacy

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-24
- AOS continuous improvement


## FTR-026 — Модель extensions, plugins и capability modules

```yaml
feature_id: FTR-026
layer: Architecture Extension
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Future domains may need extension without coupling or overriding core.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-026`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Optional module contract with versioning, permissions, compatibility, isolation and safe removal.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Define extension point
2. Specify interface/version
3. Declare permissions
4. Validate isolation
5. Install explicitly
6. Monitor compatibility
7. Remove safely

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-004
- FTR-019
- FTR-021

### Границы безопасности и полномочий человека

- Cannot override core authority
- Optional failure isolated
- Explicit install/update/remove

### Критерии приёмки

- Core works without module
- Compatibility deterministic
- Removal safe

### Обязательные негативные сценарии

- Unknown version blocked
- Undeclared permission rejected
- Module failure isolated

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Repeated extension points
- Versioning strategy

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AOS module references


## FTR-027 — Предметные модули: Medical и Design

```yaml
feature_id: FTR-027
layer: Regulated / Creative Domain Extensions
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Regulated and creative domains need separate contracts, providers and specialist decisions.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-027`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Replaceable domain modules over neutral core with data/provider/compliance boundaries.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Define domain boundary
2. Identify regulated decisions/data
3. Create domain contracts
4. Add specialist checkpoints
5. Validate isolation
6. Pilot bounded task

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-019
- FTR-026
- Domain policy

### Границы безопасности и полномочий человека

- No clinical/legal authority for agent
- Separate compliance decision
- Least data exposure

### Критерии приёмки

- Core domain-neutral
- Specialist decision explicit
- Data boundary tested

### Обязательные негативные сценарии

- Unapproved provider blocked
- Missing specialist review blocks affected action
- Module removable

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Medical privacy/provider requirements
- Design workflow needs

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AOS medical/design references


## FTR-028 — Workbench или SaaS UI для onboarding, status, review и collaboration

```yaml
feature_id: FTR-028
layer: UX Wrapper
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Nonprogrammers may need visual collaboration, but UI can become hidden authority.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-028`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

UI rendering source-linked contracts, Evidence, chat and explicit decision records after core proof.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Render source state
2. Edit through contracts
3. Show risk/Evidence/unknowns
4. Capture explicit decision
5. Sync without duplicate truth

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-008
- FTR-012
- FTR-016

### Границы безопасности и полномочий человека

- UI display ≠ authority
- Source-linked state
- Explicit identity/auth

### Критерии приёмки

- Journey understandable/faster
- Displayed state matches sources
- Accessibility tested

### Обязательные негативные сценарии

- Stale/offline UI cannot approve
- Generated decision rejected
- Unauthorized access blocked

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Measure CLI/chat friction
- Auth/collaboration requirements

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-39/F-40
- Historical UI roadmap


## FTR-029 — Экспорт templates, prompt packs, cross-repo context, localization и policy overlays

```yaml
feature_id: FTR-029
layer: Packaging / Extension Support
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Rules/templates drift across tools, repositories and languages.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-029`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Versioned package/export/update with common source, thin adapters, provenance, ownership and localization.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Build from owner sources
2. Generate adapters
3. Validate links/paths
4. Preview conflicts
5. Apply explicitly
6. Drift-check update

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-004
- FTR-016
- FTR-021

### Границы безопасности и полномочий человека

- Source repo read-only during extraction
- No authority duplication
- Locale does not change semantics

### Критерии приёмки

- Portable package
- Adapters consistent
- Relative links
- RU/EN meaning aligned

### Обязательные негативные сценарии

- Missing owner blocks generation
- Local modifications preserved/conflicted
- Adapter cannot add permission

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Tool-specific formats
- Localization glossary/semantic tests

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-27/F-28
- Prompt-pack history


## FTR-030 — Внутренние contract tools: strict loaders, parser sunset, registry audits и schema/runtime drift tests

```yaml
feature_id: FTR-030
layer: Development Factory Internal
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
product_scope_effect: NONE_UNTIL_HUMAN_DECISION
implementation_maturity: NOT_ASSIGNED
current_runtime_verification: NOT_RUN
dossier_readiness: DESIGN_CANDIDATE
feature_specific_contract_required: true
shared_defaults_present: true
```

**Проблема**

Permissive parsers, representation drift and AI-code debt undermine accepted contracts.

### Целевые пользователи

- Владелец продукта или отраслевой эксперт, которому нужен результат capability
- Агент или исполнитель, работающий по её contract
- Reviewer или operator для затронутой boundary

### Условие запуска (`Trigger`)

Выбранная человеком цель или условие workflow требует capability `FTR-030`.

### Предварительные условия

- Релевантные product facts и authority sources определены
- Required repository/subject identity проверена, если feature работает с repository
- Human disposition остаётся `UNDECIDED`, пока нет явного решения человека

### Входные данные

- Принятые или DRAFT upstream artifacts с явным статусом
- Exact scope, constraints, unknowns и ссылки на источники
- Релевантные repository facts и Evidence, если применимо

### Результаты и наблюдаемое поведение

Small strict utilities, migration evidence and maintainability metadata after contracts stabilize.

- Результат имеет явный статус и provenance
- Пользователь видит limitations, unknowns и одно следующее действие

### Основной процесс

1. Inventory representations
2. Introduce strict adapter
3. Migrate bounded callers
4. Add negative tests
5. Compare docs/schema/runtime
6. Sunset legacy after Evidence

### Изменения состояния

Фича изменяет только заявленный ею класс артефакта или состояния. Переход в execution, approval или Git delivery автоматически не выполняется.

### Сценарии отказа

- Missing или stale input используется как текущий факт
- Рекомендация выдаётся за решение человека
- Scope скрыто расширяется
- Derived artifact становится конкурирующим Source of Truth

### Восстановление

Остановить затронутую операцию, сохранить фактическое состояние и Evidence, пометить stale/unknown, восстановить exact input или получить решение человека и повторить только затронутый stage.

### Зависимости и общие contracts

- FTR-011
- FTR-021
- 03_Development

### Границы безопасности и полномочий человека

- Internal tool ≠ product value
- No automatic canonical mutation
- Scope bounded

### Критерии приёмки

- Runtime/tests use same loader
- Invalid states rejected
- Old parser removed after migration evidence

### Обязательные негативные сценарии

- Bypass path fails
- Unexpected field rejected
- Docs-code drift detected

### Минимальная модель реализации — кандидат

Начать с Markdown/YAML/JSON contracts и тонких deterministic tools. База данных, distributed services, широкая orchestration и full Governance не являются зависимостями по умолчанию.

### Точечное исследование перед реализацией

- Historical parser/registry defects
- Minimum stewardship metadata

### Не-цели

- Автоматическое human approval
- Скрытое расширение scope или permissions
- Автоматические Commit, Push, Merge или Release
- Полный импорт legacy topology

### Связь с AgentOS и legacy

- AgentOS F-29/F-30/F-31/F-32/F-34
