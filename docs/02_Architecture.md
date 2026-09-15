---
package: AOS_Project_Knowledge_Baseline
package_revision: R7-RU
updated: '2026-09-13'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
current_change_subject: AOS_PRECOMMIT_DOCUMENTATION_CORRECTIONS_R7
current_change_authority: CURRENT_EXPLICIT_HUMAN_INSTRUCTION
current_change_status: SCAFFOLD_CORE_DRAFT
current_change_agent_review: PASS
current_change_agent_review_scope: DOCUMENTATION_AUTHOR_SELF_CHECK
current_change_human_review: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
semantic_audit: COMPLETED_WITH_CORRECTIONS
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: dev
audited_source_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
audited_source_blob_sha: cf4daddf0b82e8c804f301f91bc627512a91a6ce
active_path: docs/02_Architecture.md
document_language: ru
technical_identifiers_language: en
document_role: TARGET_ARCHITECTURE_BASELINE
authority_scope:
- architecture_principles
- layer_boundaries
- shared_contract_classes
- data_ownership
- deferred_complexity
---

# 02 — Архитектура

## 1. Граница статуса

Target architecture не является копией AOS-FARM, AgentOS или AOS-02. Historical code/documents используются как evidence/reference. Любое включение механизма в target design требует explicit human decision.

Документ задаёт принятый architecture baseline на уровне принципов, слоёв и contract classes, но не выбирает language, framework, database, dependencies или implementation repository. Candidate component map и `INFERENCE`-разделы остаются proposals.

## 2. Цели архитектуры

- contract-first implementation;
- observable behavior before topology;
- replaceable internals;
- minimal always-on safety;
- explicit human authority;
- repository-verifiable state;
- idempotent/recoverable writes;
- feature-scoped context;
- no hidden lifecycle mutation;
- portability across agent environments;
- smaller target than legacy unless measurements justify expansion.

## 3. Модель слоёв

### L1 — Interaction Surface

CLI, chat, local UI и future SaaS adapters. Surface отображает state и Evidence, но не является independent Source of Truth и не превращает click в approval без decision record.

### L2 — Product Runtime

Intent, Discovery, Specification, Feature Passport, Status/Next/Details, Review, Project Memory, First-Start и optional Architecture Support.

### L3 — Development Factory

Task Brief compiler, preflight/preview, scoped executor, validation/evidence, Context Pack builder, backlog, CI и release helpers.

### L4 — Minimal Safety / Governance

Authority checks, permission states, scope/path/Git boundaries, result semantics и stop rules. Stronger Governance — optional layer.

### L5 — Knowledge / Reference

Accepted documents, DRAFT Feature Passports, lessons, targeted findings, patterns и derived indexes.

### L6 — Optional Extensions

Граф RAG, model routing, runtime enforcement, plugins, domain modules, workbench/SaaS и observability.

## 4. Карта компонентов — кандидат

```text
Interaction Surface
├─ Intake
├─ Discovery
├─ Specification Builder
├─ Status / Next / Details
├─ Review Surface
└─ First-Start / Tutor

Product Runtime
├─ Feature / Journey Model
├─ Product Feature Registry
├─ Project Memory
├─ Architecture Decision Support
└─ Installer / Updater

Development Factory
├─ Task Brief Compiler
├─ Preflight / Preview
├─ Complete-Task Controller
├─ Scoped Executor
├─ Validation / Evidence
├─ Diagnostic Ladder / Corrector
├─ Context Pack Builder
├─ Handoff Builder
└─ Test / CI / Release Helpers

Safety and Control
├─ Authority Resolver
├─ Permission Classifier
├─ Scope / Path Guard
├─ Git Boundary Guard
└─ Optional Runtime Enforcement

Knowledge
├─ Canonical Documents
├─ Feature Passports
├─ Lessons / Patterns
├─ Reference Findings
└─ Derived Index
```

## 5. Модель authority

```text
system/owner instruction
> explicit human decision
> accepted current contract
> current instrumental repository observation
> implementation Evidence
> supporting report/document
> generated index/cache/retrieval
> legacy/reference proposal
```

Derived index, UI, adapter, validator или report не создают authority самостоятельно.

## 6. Общие классы contracts

Контракты строго разделены на архитектурные (формируются на этапе проектирования) и инженерные (используются исключительно при реализации).

### Архитектурные контракты (Architecture Contracts)

Используются в процессе проектирования документации. Определяют WHAT и не требуют `Execution Authorization`.

#### C-001 — Intent Record

```yaml
actor:
original_request:
problem:
desired_outcome:
context:
constraints: []
non_goals: []
assumptions: []
unknowns: []
sensitive_domain_flags: []
source:
```

#### C-002 — Feature Passport / Feature Contract

```yaml
feature_id:
purpose:
users: []
trigger:
preconditions: []
inputs: []
outputs: []
main_flow: []
states: []
transitions: []
failures: []
recovery:
dependencies: []
constraints: []
authority_boundaries: []
acceptance_criteria: []
negative_scenarios: []
maturity:
evidence_status:
human_disposition:
```

#### C-003 — Product Spec

Product-level problem, users, journeys, scope, non-goals, constraints, metrics, dependencies, acceptance и open decisions. Не разрешает execution.

Для [выбранной версии проекта](01_Product.md#autonomous-project-outcome) — DRAFT:
эти существующие сведения определяют включённые части и общий результат версии;
подробности частей остаются в C-002. Связь с общей C-005 и её проверками задаёт
[Development §25.0](03_Development.md#autonomous-project-development), без нового
владельца требований или схемы Product Spec.

<a id="quality-requirements-contract"></a>

##### C-002/C-003: существенные условия качества и их передача — DRAFT

Для [текущего уточнения FTR-003](06_Features.md#quality-requirements-behavior) используется производное структурированное представление существующих constraints/metrics/acceptance. Это способ разрешённой документационной адаптации, не принятие runtime schema. Общие схемы C-002/C-003 не получают обязательных quality_* fields. Каждый quality fact хранится один раз у существующего владельца; остальные разделы ссылаются или суммируют его с явной ссылкой. Quality Profile допустим как название представления, без отдельного артефакта/registry. Markdown остаётся читаемым источником, machine representation — производным.

Содержание представления, независимо от оформления: смысл условия; exact owner requirement ref/revision и source locator; статус; область/условия применения; проверяемый outcome или названный gap. Предположение не становится human decision. Для cross-artifact refs нужен устойчивый ID/anchor, отличный от content revision; один source может поддерживать несколько requirements, одно требование — несколько checks. Concerns — необязательные labels, не новая глобальная таксономия. Внутреннее хранение, сериализация и алгоритм сборки относятся к HOW.

Продуктовый факт принадлежит C-003, feature-specific addition — C-002. Применимость определяется scope исходного требования, а не наличием заполненного списка ссылок. Отсутствие quality-раздела у мелкой фичи допустимо; неизвестная применимость оформляется как unknown для затронутого решения, а не отрицание наследования. Исторические документы без нового представления читаются по прежним constraints/acceptance; обязательного backfill нет.

Отклонение в C-002 содержит ссылку на исходное product requirement/revision, ограниченную область, замену/исключение, rationale и ссылку на решение, действительно допускающее это изменение. C-003 не копируется и не переписывается ради одной фичи. До применимого решения deviation остаётся DRAFT; после решения меняется только указанный scope. Несовместимые действующие требования дают conflict, не last-writer-wins. Common safety/data/authority boundaries не снимаются присутствием записи deviation.

| Producer → contract → consumer | Передаваемый смысл и исход |
|---|---|
| FTR-001/разрешённые source artifacts → C-001/ответы → FTR-003 | Исходные слова, context и provenance. Нормализованное условие возвращается на обычный review, а не принимается по факту заполнения |
| FTR-003 → C-003/C-002 exact constraints/acceptance refs → FTR-005 | Только material architecture question; owner need/no-need/ADR остаётся FTR-005, ранее принятое применимое решение не выбирается заново |
| FTR-003 → C-003/C-002 → FTR-006 | Принятый outcome/область либо явный unknown; FTR-006 связывает requirement refs с отдельными check IDs в C-005.validation_matrix |
| FTR-006 → C-005 → существующий controller/VALIDATE → FTR-011/C-009 → C-010/FTR-012 | Exact subject, required checks, пригодный метод и фактические результаты; используются AOS_VALIDATION_ENVELOPE_V3, check_results/aggregate_result и полный vocabulary C-009, включая CONTRACT_VIOLATION. Нет отдельного quality verdict или прямой записи FTR-003 в validator |

Для проверки измеримого условия должны быть известны применимый сценарий, subject/revision, среда/fixture/load, измеряемый outcome/метрика, источник критерия, метод и ограничения. Достаточные сведения можно передать ссылками; точные числа не обязательны для любого требования и не придумываются. Например, проверка времени на пустой базе не подтверждает условие при заданной нагрузке, а проверка сохранности требует обозначенного failure scenario. Если метод отсутствует, соответствующая проверка NOT_RUN с причиной; безопасный PLAN может подготовить метод. Required NOT_RUN запрещает PASS своего aggregate, не аннулируя независимые результаты.

Изменение исходного требования, scope или решения делает зависимые projections/Brief/check applicability требующими пересмотра. Старые Evidence не редактируются в «новый результат». Consumer проверяет exact references и полноту applicable requirements, включая обычный текст; сводка без раздела или потерянный ref не разрешает молча пропустить constraint. Unsupported format/revision требует явного отказа либо поддержанного чтения canonical sources с сохранением смысла. Additive compatibility не заявляется только по добавлению поля.

Граница C-015/C-016 не расширяется: текущее изменение — документация и смысл существующих данных, новых endpoints, подписок и очередей нет. Будущие read/persist операции выполняются по bindings/effects владельца; чтение представления не сохраняет скрытый cache и не создаёт result. ADD/ENABLE представления не активирует другие фичи; UPDATE сверяет revisions/consumers; DISABLE/REMOVE убирает только представление и сохраняет обычный Spec/Brief flow; DELETE не распространяется на исходные ответы, requirements, decisions или Evidence. Сохранение/удаление по-прежнему требует своего покрытого scope. Наличие FTR-005/011 в выбранных supporting controls не доказывает их runtime availability; FTR-023 не required dependency этого пути.

Изменения условий применимости отражаются в существующей карте §6.1: FTR-005/006/007/012/032 и сценарные consumers 031/033 получают тот же C-002/C-003 с актуальным смыслом; FTR-016 переносит owner refs, FTR-017 не выводит authority из ranking. Их форматы и dispositions здесь не изменяются. Проверяются затронутые потребители, не проводится миграция всех dossiers. [QR-C01–12](03_Development.md#quality-requirements-verification) проверяют сохранение смысла и отказ при потере условий.

#### C-004 — Architecture Decision Record

```yaml
question:
context:
constraints: []
options: []
tradeoffs: []
evidence: []
selected_option:
human_decision_identity:
consequences: []
reversal_conditions: []
```

<a id="architecture-output-handoff"></a>

#### Целостный архитектурный результат и передача в планирование — DRAFT

Этот contract уточняет принятый [порядок после ТЗ](01_Product.md#технические-решения-при-подготовке-тз).
FTR-005 владеет содержанием архитектурного документа для выбранной системы;
FTR-003 сохраняет владение требованиями C-002/C-003. C-004 фиксирует отдельный
существенный выбор и входит в документ ссылкой, когда применим. Набор ADR или
rationale «ADR не нужен» сам по себе не заменяет целостный результат.

| Обязательное содержание | Что должно быть проверяемо перед зависимой реализацией |
|---|---|
| Subject и источники | Точная версия ТЗ, scope системы, revision архитектурного документа и ссылки на применимые требования/решения; ни одно требование не изменено архитектурой |
| Компоненты и связи | Ответственность частей, границы и I/O существенных стыков, интеграции и внешние зависимости; связь с процессами и критериями ТЗ |
| Технологии и данные | Подход к реализации, хранению и движению данных в пределах подтверждённых ограничений; существенный выбор отделён от обратимого HOW исполнителя |
| Проверки | Как проверить требования через компоненты и реальные стыки, включая отрицательные исходы; какие методы/inputs ещё недоступны |
| Отказы и восстановление | Существенные failure paths, сохранность данных, наблюдаемый результат восстановления и ограничения повторов |
| Развёртывание | Условия запуска выбранной системы, необходимые зависимости и границы эффектов; описание не разрешает deploy или подключение сервиса |

Неприменимая область имеет явное обоснование; существенный unknown остаётся
видимым и блокирует зависимое действие. Этот contract не предписывает новый формат
хранения, wire schema или стек AOS. Обычные обратимые решения будущего исполнителя
не превращаются в обязательный пользовательский выбор.

**Передача.** Для этого пути FTR-006 — обязательный потребитель exact revision
документа: ограничения, стыки и проверки учитываются при подготовке C-005.
Участие FTR-007 определяется выбранным scope текущего сценария:

- Без FTR-007 передача в планирование завершается через FTR-006; зависимости
  и следующий внутренний action ведёт существующий controller по Development
  §25.0. Отсутствие backlog не требует его реализации/подключения или нового
  Human Gate и не отменяет проверки ограничений и порядка зависимых работ.
- Когда FTR-007 выбран потребителем, он получает ту же exact revision для
  contribution/dependencies. Обязательная интеграция входит в критерии handoff;
  недоступный/несовместимый consumer или неподтверждённая передача блокируют
  зависимую работу. Нельзя исключить эту интеграцию как неприменимую или заменить
  её fixtures ради PASS. Создаваемый в scope consumer готовится до использования
  по Development §25.0; его отсутствие не расширяет scope автоматически.

В уже принятой общей task архитектурный документ служит входом покрытых внутренних
работ; controller сохраняет их зависимости и результаты в C-012, не переписывая
исходный C-005. Изменение принятой цели/contract/scope следует отдельному решению
и fresh binding по Development §10.0, а обычный HOW не создаёт новую task.
До готовности документа допустима подготовка плана с явной зависимостью;
завершённость ADR не снимает её. Проверка полноты и согласованности описана в
[Development](03_Development.md#architecture-handoff-checks). Техническая проверка
не означает Human ACCEPT или доказанную работу будущей системы.

**Версии и продолжение.** Сохранение использует существующую границу FTR-016,
C-012/C-016; владение содержанием остаётся у FTR-005. До handoff доступен сам
документ его exact revision, а не только acknowledgement записи. Смена ТЗ,
решения или значимого discovery fact требует повторной оценки затронутой части
архитектуры и зависимых Brief/планов; прежние revisions/Evidence сохраняются,
их проверка и authority не переносятся автоматически. При потере подтверждения
сохранения сначала reconciliation по §6.1 и Development §10.2.

Уточнение не принимает полный contract FTR-005 и не расширяет S0–K4. Заранее
подготовленный применимый документ может прийти извне; для его чтения не требуется
сначала реализовать модуль 005+022. Самостоятельный запрос ADR не запускает
подготовку всей архитектуры. Продолжение разработки внутри уже покрытой общей
task следует Development §25.0; новый scope или защищённый effect требуют своей authority.

### Инженерные контракты (Engineering Contracts)

Применяются только при runtime-реализации и не требуются для редактирования документации.

#### C-005 — Task Brief

```yaml
task_contract_version: AOS_TASK_CONTRACT_V1
task_id:
task_revision:
goal:
user_outcome:
feature_id:
lifecycle_stage: PLAN | EXECUTE | VALIDATE | REVIEW
repository_identity:
worktree:
branch:
HEAD:
baseline:
requested_paths: []
prohibited_paths: []
requested_operations: []
prohibited_operations: []
requested_effects: []
prohibited_effects: []
assumptions: []
unknowns: []
proposed_Risk_Profile:
assigned_Risk_Profile: UNASSIGNED
validation_matrix: []
acceptance_criteria: []
parent_task_authority_requirements:
  requested_worker_actions: []
  requested_task_hard_limits:
run_allowance:
human_only_boundaries: []
stop_conditions: []
```

Task Brief фиксирует только request/prohibition и не предоставляет authority.
C-005 lifecycle_stage задаёт только исходную стадию. Текущая lifecycle stage
принадлежит C-012 и меняется по [правилам Development](03_Development.md#core-lifecycle-transitions),
без переписывания task revision или исходного scope. Разрешённость полного цикла
должна быть явной в принятом task scope; имя исходной стадии не даёт authority.
До отдельной выдачи он не содержит authorization identity. Фактический binding
сохраняется controller в Loop State без переписывания Task Brief. `requested_*`
никогда не трактуется как `allowed_*`.

**Применение к версии проекта — DRAFT.** Общая C-005 связывает exact C-003/C-002,
scope версии и её критерии; внутренняя декомпозиция не меняет task identity.
Различение внутренних работ и самостоятельных tasks принадлежит
[Development §7/§25.0](03_Development.md#autonomous-project-development).
Это применение существующих goal/scope/criteria и ссылок, не новые поля или
версии C-005/C-006. Authority другой task не наследуется по общей цели проекта.

#### C-006 — Parent Task Authorization Record

```yaml
authorization_schema_version: AOS_PARENT_TASK_AUTHORIZATION_V1
authorization_id:
authorization_revision:
task_id:
task_revision:
subject_identity:
allowed_worker_actions: []
allowed_operations: []
allowed_paths: []
allowed_effects: []
forbidden_operations: []
forbidden_paths: []
forbidden_effects: []
human_only_boundaries: []
task_hard_limits:
issued_by_human:
issued_at:
expires_at:
revoked: false
```

Parent Task Authorization задаёт предел effectful worker dispatches и никогда
не изменяет state-machine graph. Отсутствующие, `null` и пустые allowlists
означают отсутствие разрешения; forbidden fields и human-only boundaries имеют
приоритет. Допустимые значения `allowed_worker_actions` — `EXECUTE` и
`CORRECT`. Wildcard допустим только как явный pattern с bounded canonical root.

#### C-006A — Effectful Stage Envelope

```yaml
envelope_schema_version: AOS_EFFECTFUL_STAGE_ENVELOPE_V3
envelope_id:
parent_authorization_id:
parent_authorization_digest:
parent_authorization_revision:
state_machine_version: AOS_COMPLETE_TASK_LOOP_V3
task_id:
task_revision:
candidate_identity:
state_revision:
event_head_identity:
transition:
  from: SELECT_NEXT_ACTION | DIAGNOSE
  to: EXECUTE | CORRECT
worker_action: EXECUTE | CORRECT
action_spec_digest:
correction_gate_id:
correction_gate_digest:
allowed_operations: []
allowed_paths: []
allowed_effects: []
forbidden_operations: []
forbidden_paths: []
forbidden_effects: []
attempt_ordinal:
issued_by_controller_identity:
issued_at:
expires_at:
consumed: false
```

Controller выводит fresh Stage Envelope только для `EXECUTE` или `CORRECT`.
Envelope обязан быть сужением актуальной Parent Task Authorization и связывает
exact action, candidate, state revision/event head и переход
`AOS_COMPLETE_TASK_LOOP_V3`. Для `CORRECT` обязательны Correction Gate identity
и digest; для `EXECUTE` они отсутствуют.

Admission атомарно проверяет: текущие state/event/candidate; разрешённый
`{from,to}` из canonical transition matrix; exact action-spec digest; текущую
unexpired/unrevoked Parent Task Authorization с совпадающими
identity/revision/digest; subset allowed и superset forbidden fields; gate для
`CORRECT`; unused/unexpired envelope. После admission envelope потребляется до
effect. Cache или вложенный digest не заменяет чтение текущих records.

V3 дополнительно проверяет допустимость lifecycle-перехода для этой task.
Исходная lifecycle читается из exact C-012, связанного state revision/event head;
целевая EXECUTE определяется worker action и правилами Development. Отдельная
несвязанная копия lifecycle в envelope не вводится. Проверка исходного tuple,
смена lifecycle/controller action и consumption публикуются как одна атомарная
операция; при отказе ничто из них не меняется. Envelope/gate остаются привязаны
к исходному tuple допуска, а новый state хранит результат admission. Нельзя
повторно допускать тот же envelope относительно уже изменившейся revision.


#### C-007 — Preflight / Preview

Exact repository/worktree/branch/HEAD/baseline/status/diff, planned actions, paths, conflicts, permissions и preview identity.

#### C-008 — Execution Record

Starting identity, Stage Envelope identity/digest, action-spec digest, actual
mutations, changed paths, side effects, checks, ending identity, limitations и
stop reason.

#### C-009 — ValidationEnvelope

<a id="technical-result-contract"></a>

**Единый technical Result Contract (R5).** Владелец поведения — FTR-011;
producer, validator, controller, status и review используют ровно эти значения:
`CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS`.
HUMAN_REVIEW_REQUIRED относится только к document maturity, WAIT_HUMAN — к task
state. Они и любой неизвестный enum отвергаются как technical result, не
переводятся в PASS, BLOCKED или другой результат догадкой. Raw invalid value
сохраняется как observation; ошибка contract оформляется отдельным валидным
CONTRACT_VIOLATION. Проверки vocabulary и consumers — SC-T21.

```yaml
validation_envelope_version: AOS_VALIDATION_ENVELOPE_V3
validation_envelope_id:
state_machine_version: AOS_COMPLETE_TASK_LOOP_V3
task_id:
task_revision:
candidate_identity:
state_revision:
event_head_identity:
transition:
  from: EXECUTE | CORRECT | SELECT_NEXT_ACTION | CHECK | DIAGNOSE
  to: CHECK | FINAL_VALIDATE
worker_action: CHECK | FINAL_VALIDATE
check_purpose: DIAGNOSTIC | ACCEPTANCE | FINAL
required_check_ids: []
read_scope: []
issued_by_controller_identity:
issued_at:
expires_at:
consumed: false
check_results: []
aggregate_result: NOT_RUN
evidence_refs: []
limitations: []
```

ValidationEnvelope всегда read-only. Он сохраняет stable result vocabulary,
required/optional checks, `NOT_RUN`, limitations, exact subject identity и
fail-closed aggregation. Его нельзя преобразовать в Stage Envelope.

`check_purpose` обязателен. Допустимы только следующие сочетания; списки enum
в schema не разрешают их произвольное декартово произведение:

| Purpose | Исходный action → worker action | Возврат observation |
|---|---|---|
| DIAGNOSTIC | DIAGNOSE → CHECK | CHECK → DIAGNOSE при любом результате; уточняет diagnostic record, не закрывает acceptance criterion |
| ACCEPTANCE | EXECUTE / CORRECT / SELECT_NEXT_ACTION → CHECK | Controller выбирает допустимый переход из CHECK по результатам критериев |
| FINAL | SELECT_NEXT_ACTION / CHECK → FINAL_VALIDATE | Finding → DIAGNOSE; доказанный completion или точная остановка → IDLE |

До запуска controller проверяет exact task/candidate/state revision/event head,
issuer, срок, unused envelope, read scope, check IDs и сочетание purpose/transition
с §7 и допустимость lifecycle VALIDATE по Development. Исходная lifecycle берётся
из связанного C-012. Lifecycle/controller transition и consumption атомарны по
тем же правилам, что C-006A; отказ сохраняет исходные state и unused envelope.
Envelope потребляется до запуска check; повторный запуск получает новый.
Результат связывает исходный envelope и проверенный subject; stale или mismatched
observation не закрывает критерий. Required/optional состав берётся из явно
связанного check binding, а не выводится из успешного exit. Diagnostic PASS не
заменяет ACCEPTANCE или FINAL Evidence. Запись результатов и test outputs
допускается только в объявленной области вне read-only subject. Checker получает
доказательство состоявшегося admission: consumed у допущенного envelope не
запрещает единственный уже допущенный check, но запрещает новый dispatch/replay.
Observation проверяется по исходному binding допуска и текущему active action;
смена state при самом admission не делает его результат автоматически stale.

#### C-009A — Correction Gate

```yaml
gate_id:
gate_version: AOS_CORRECTION_GATE_V3
state_machine_version: AOS_COMPLETE_TASK_LOOP_V3
parent_authorization_id:
parent_authorization_revision:
parent_authorization_digest:
task_id:
task_revision:
state_revision:
event_head_identity:
diagnostic_id:
failure_signature:
candidate_before_identity:
proposed_correction_digest:
authority_match: true
cause_status: PROVEN | PLAUSIBLE
confidence: MEDIUM | HIGH
material_competing_hypotheses: 0
correction_class: REVERSIBLE_BOUNDED | REVERSIBLE_DIAGNOSTIC
falsifiable_prediction_id:
verification_check_ids: []
rollback_or_recovery_ref:
evaluated_by_controller_identity:
evaluated_at:
decision: ALLOW | DENY
```

`ALLOW` допустим только для `PROVEN + MEDIUM|HIGH + REVERSIBLE_BOUNDED` либо
`PLAUSIBLE + HIGH + REVERSIBLE_DIAGNOSTIC`. Gate относится только к exact
authorization/state/diagnostic/failure/candidate/proposed-correction tuple. Он
вычисляется до Stage Envelope. При `ALLOW` controller создаёт `CORRECT` envelope
с тем же `action_spec_digest` и gate identity/digest. Missing, stale, replayed
или mismatched binding даёт `DENY`.

#### C-010 — Evidence Record

Evidence kind, method/command, subject identity, output summary, locator/digest, result, limitations и redaction.

#### C-011 — Human Review / Decision

Review subject, user impact, Evidence, findings, options, explicit human decision, actor/date и exact binding. Generated decision invalid.

#### C-012 — Project Memory / Handoff

Loop-state schema/state-machine version, repository identity, lifecycle stage,
controller action, task/run state, state revision/digest/event head,
parent authorization identity/revision/digest, baseline/candidate,
accepted decisions, findings, blockers, checks, diagnostic level, attempt ledger,
resource usage, active Stage/Validation Envelope state и one deterministic next
action. Текущая lifecycle stage и её изменения принадлежат controller по
[workflow](03_Development.md#core-lifecycle-transitions), исходная — C-005.
Сохраняются before/after stage, причина, task/authority binding и исходный/новый
state/event tuple каждого перехода. Это часть C-012/history, не новый authority
record. Controller является единственным владельцем переходов; worker output —
observation, а не authority изменить state или объявить completion. Concurrent
или stale update отклоняется: только один controller может подтвердить изменение
из одной исходной revision. Отказ ведёт к reconciliation; конкретный механизм
синхронизации выбирается при реализации.

Для первого core-профиля C-012 фиксирует `AOS_COMPLETE_TASK_LOOP_V3` и purpose
активной проверки через её C-009 binding. Первоначальное создание и resume —
разные входные сценарии [Development](03_Development.md#initial-product-state).
Новый record содержит BIND_TASK/ACTIVE/RUNNING, исходную revision/event identity,
current candidate и authority binding, критерии с NOT_RUN, пустой attempt ledger
и отсутствие envelopes/effects. Resource usage учитывает уже затраченный ресурс
этого запуска; создание state не обнуляет внешний budget. Missing checkpoint
существующей задачи не является таким начальным состоянием.

Уточнение C-012 — DRAFT: восстановимый record сохраняет доступную exact связь
с C-005 и его ограничениями, выполненные действия и наблюдённые эффекты (включая
неизвестный исход), результаты/актуальность проверок, незавершённые операции и
следующий допустимый шаг. Контекстная сводка не заменяет эти источники. Недоступная
связь ограничивает продолжение; актуальность authority проверяется заново по
[Development §10.2](03_Development.md#state-conflict-recovery).

Для общей задачи версии те же C-012 bindings сохраняют критерии частей и общих
стыков, выполненную, непроверенную и stale работу, оставшиеся dependencies и
next action по [Development](03_Development.md#autonomous-project-development).
Это DRAFT применения существующего state: завершение части не создаёт новый
controller, пустой ledger или terminal state общей задачи. Формат и схема не меняются.

#### C-013 — Install / Update Manifest

Package identity, ownership classes, operations, conflicts, preview binding, recovery и post-apply verification.

#### C-014 — Git Delivery Record

Separate records for Commit, Push, Merge и Release.

<a id="module-connector-queue"></a>

#### C-015 — Module Connection Contract (R7, DRAFT)

Версия: AOS_MODULE_CONNECTION_V1. Immutable contract описывает WHAT подключения;
формат serialization и layout выбираются в implementation profile.

| Обязательный предмет | Содержание |
|---|---|
| Identity | Module identity/revision, список FTR и exact принятые C-002/contracts, источник и digest; identity не выдаёт authority |
| Provided/required interfaces | Имена и версии операций, capabilities, payload/result/error contracts, реальные producers/consumers; required/optional и условия fallback |
| Mode | DIRECT_READ для быстрого чтения; QUEUED_COMMAND для effects/отложенных запросов; QUEUED_EVENT для фактов объявленным subscribers |
| Boundary | Read/write/effect/data/provider scope, ownership state, зависимости, transport limits profile, support envelope ОС/runtime |
| Lifecycle | Условия регистрации/включения/обновления/отключения/удаления, совместимость данных и сообщений, recoverable migration, независимое чтение сохранённых artifacts |
| Acceptance | Критерии фич/модуля, реальных стыков и core regression, negative cases, oracle/Evidence; justified NOT_APPLICABLE для отсутствующего собственного storage/migration |

Module contract identity не является новой FTR и не создаёт параллельный каталог:
состав остаётся в Features. Изменение контракта создаёт revision; runtime
регистрация связывает exact C-015 с instance/generation и поддержанным handler.
Регистрацией/маршрутизацией владеет core FTR-010, FTR-016 сохраняет bindings,
FTR-019 проверяет полномочия, FTR-009 — target/capabilities. Contract автора модуля
не может самостоятельно включить код или подписку.

Первый профиль допускает статическую локальную композицию; никакого auto-discovery
с исполнением найденного кода, обязательного внешнего broker или plugin loader.
DIRECT_READ проверяет текущую регистрацию, interface/payload versions и scope,
не пишет product state, не публикует скрытые команды и не выполняет fallback с
эффектом. Ответ использует C-009 Result Contract/C-010 provenance. Неизвестный
интерфейс, несовместимость и недоступность возвращаются явно. Технические
log/evidence outputs допустимы только в отдельно покрытой служебной области.

#### C-016 — Message and Delivery Contract (R7, DRAFT)

Версия: AOS_MODULE_MESSAGE_V1. Сообщение — immutable request/observation, delivery
state хранится отдельно и не подменяет task/run/lifecycle C-012.

| Обязательный предмет | Содержание |
|---|---|
| Identity | Message ID и stable logical operation ID, source identity, kind COMMAND/EVENT, correlation/causation |
| Destination | Receiver instance/generation, interface/version, exact C-015 binding; для события — конкретные объявленные subscriber bindings |
| Payload | Версия payload и bounded содержимое либо immutable reference/digest с разрешённым доступом; ожидаемый subject/candidate и preconditions |
| Context | Для COMMAND — exact C-005/task revision и reference на проверяемую current authority; для EVENT — source observation C-010 и явно применимый subscription scope, без выдуманного task/approval |
| Limits | Issued/expiry, queue/ordering key и finite profile: capacity/bytes/payload, ожидание, claim duration, retry budget/backoff и retention; численные значения фиксируются до запуска |
| Delivery observation | Ссылки на message/operation и attempt/owner, durable admission при наличии, timestamps, состояние доставки/причина, C-009 result/C-010 Evidence; acceptance/ack отдельно от результата операции |

Пустой/неизвестный обязательный profile не означает unlimited. Admission в очередь
проверяет C-015, размер/формат, destination, scope и доступ к данным. При переполнении
enqueue явно отклонён без обещания accepted; accepted выдаётся только после durable
сохранения. Отказ записи и неизвестный исход публикации требуют query/reconciliation
по message/operation ID, а не новой identity для обхода неопределённости.

Повтор тех же identity/payload/bindings возвращает существующую delivery/operation
связь; та же identity с другим содержимым отклоняется. Для fan-out сохраняется
отдельная доставка на каждую declared subscription; потеря ack не повторяет уже
закрытую доставку этому consumer. Событие не создаёт authority: handler с эффектом
может лишь сформировать запрос в явно разрешённом task scope, который снова
проходит current admission. Нет подходящей authority — нет эффекта.

Для выполнения COMMAND в task controller проверяет текущие registration/generation, versions,
subject/preconditions, expiry, permission и current C-006. Stale message не
перепривязывается молча к новому candidate. C-006A/C-009 выдаётся fresh при
фактическом dispatch по V3; очередь не хранит заранее выданный Stage Envelope
как будущую authority. Логический operation ID связывает message, admission,
C-008/recovery observation и C-012 ledger, переживая redelivery и новый run.

QUEUED_EVENT имеет отдельный read-only маршрут. FTR-010 проверяет current
registration/subscription binding, versions, источник C-010, payload access,
expiry и действующий permission/read scope подписки. Текст C-015/C-016 сам
не предоставляет доступ: основание scope имеет trusted provenance и проверяется
на отзыв. Активная C-005, current C-006 исходной задачи и C-012 для самого
read-only consumer не требуются; C-006A/ValidationEnvelope ему не выдаются.
Используются только technical Result Contract из C-009 и C-010 provenance.
Receipt/result/delivery state записываются отдельно от product subject и C-012
только по действующему отдельно покрытому служебному scope; отсутствие этого
допуска не маскируется успешным ack. Это не исключение для product mutation.

Terminal исходной задачи не мешает чтению её наблюдения по независимо действующей
подписке, но не возобновляет задачу и не продлевает её authority. Read-only
consumer не изменяет product artifacts, task/lifecycle state и не исполняет
команду из payload. Effectful follow-up требует отдельного COMMAND, exact active
C-005 и current C-006 с обычным V3 admission; событие не создаёт их автоматически.
Для architecture.analysis_observed FTR-010 владеет C-016 delivery и передаёт
payload C-010 readers FTR-008 (status) и FTR-012 (review). FTR-012 не обязан читать
transport record напрямую; FTR-008 отдельно читает delivery observation для
отображения состояния очереди. Каждая declared subscription имеет собственный
delivery/result binding. Положительный и отрицательные маршруты проверяет SC-T24.

Доставка допускает повторы; универсальное exactly-once исполнение не заявляется.
До effect durable dispatch/admission связывается с operation; после него result
сохраняется до acknowledgement. Повтор completed operation возвращает существующий
наблюдённый результат с его исходным subject/limitations, а не новый PASS текущему
candidate. Неизвестный effect сначала reconciled FTR-014; consumed envelope не
dispatch повторно. Только доказанное отсутствие исполнения позволяет fresh
attempt того же логического запроса по current scope, без потери ledger.

В пределах receiver/ordering key действует последовательная обработка и один
active delivery owner. Глобальный порядок независимых ключей не требуется.
Истечение claim не доказывает прекращение старого worker: новый владелец сначала
исключает дальнейший dispatch прежним, сверяет in-flight admission/effects и
следует existing conflict/recovery protocol. Механизм fencing/locking — HOW,
наблюдаемые гарантии обязательны. До unresolved reconciliation следующая операция
того же ключа не обходит порядок; независимые ключи могут продолжаться.

Transient delivery failure допускает конечные повторы в исходном scope/profile.
Malformed/incompatible input и revoked/stale authority не исправляются blind retry.
Исчерпанные/expired доставки сохраняют причину и Evidence в отдельном удержанном
состоянии; не удаляются и не возвращаются автоматически с обнулённым budget. Retention
не уничтожает dedup/admission evidence, пока возможны допустимая redelivery или
resume связанной задачи; недоступная история даёт UNKNOWN, не новую пустую
operation. Capacity учитывает retained данные по объявленному profile; очистка
не следует из TTL и требует своей покрытой операции.
Отмена ожидающей работы атомарно исключает её будущий dispatch. Для already
admitted action отмена — отдельный запрос: проверить поддержку остановки и actual
effects; нельзя заявить CANCELLED/no-effect без доказательства. Отмена сообщения
не отменяет автоматически parent task или другие сообщения.

Queue acceptance/claim/ack — transport observations. ACK означает durable
результат доставки/обработки, в том числе FAIL/BLOCKED, а не technical PASS,
закрытие criterion или Human ACCEPT. FTR-010 владеет доставкой и отдельно
controller decisions, FTR-016 — storage, FTR-014 — reconciliation, FTR-011 —
result validation, FTR-008 — derived status; очередь не новый центр authority.
Storage/indices не включаются в identity проверяемого product subject по
самоссылке; служебные изменения остаются наблюдаемыми и внутри своей authority.

C-015/C-016 V1 добавлены к текущему профилю V3 без изменения schemas C-001…C-014
или 26 controller edges. Старые задачи без message context не объявляются
queued; неизвестные C-015/C-016 версии допускают лишь поддержанное inspection,
не activation/delivery/migration. Эти contracts реализуют границу подключения
ядра и модулей, не требуют backlog FTR-007. Алгоритм операций —
[Development](03_Development.md#module-connection-lifecycle).

<a id="module-contracts"></a>

### 6.1. Композиция и сопровождение модулей — MODULAR_DRAFT

Этот раздел уточняет предложение [MOD-DEC-01](01_Product.md#modular-decisions). Существующие C-001…C-014 сохраняют идентичности; R7 добавляет C-015/C-016 для подключения и доставки. Здесь описано содержание сообщений на уровне WHAT; wire format, внутреннее представление и алгоритм хранения не выбираются.

| Contract | Producer / владелец содержания | Данные и consumers | Отказ и область повторной проверки |
|---|---|---|---|
| C-001 | FTR-001; человек подтверждает intent | Original request, problem/outcome, assumptions/unknowns; FTR-003; FTR-033 читает intent для Recovery Intake | Неясная цель → уточнение; проверить перенос смысла в Spec |
| C-002/C-003 | FTR-003; принятый Product artifact | Actor, scope, behavior, I/O, failures, criteria, disposition; FTR-005/006/007/012/032 (FTR-012 читает критерии C-002; FTR-032 — выбранные требования, journey и expected set); подготовка FTR-031 читает бизнес-сценарии доступа для application binding; FTR-033 читает принятые desired/protected sources выбранного next PLAN | Нет критерия → DRAFT без execution; проверить ADR, Brief, child contribution, полноту review criteria, UX mapping/context FTR-032 и ожидаемые решения доступа FTR-031 |
| C-004 | FTR-005 готовит; человек выбирает | Вопрос, варианты, Evidence, выбор/последствия; FTR-003/005/006/022 | Нет решения → selected_option отсутствует; проверить зависимые задачи и patterns |
| C-005 | FTR-006; Task Brief owner | Task/revision, requested/prohibited scope, criteria/checks/limits; FTR-007/009/010/012/013/016/032; FTR-032 читает scope/checks выбранной задачи, не выдаёт её authority; FTR-033 читает scope/checks текущей assessment/handoff task; будущую C-005 оформляет FTR-006 | Противоречивый scope → отказ допуска; проверить preview/candidate, child task, criterion-to-Evidence review и соответствие UX pack запрошенной FRONTEND/INTEGRATION задаче |
| C-006 | Человек — issuer; controller хранит binding | Subject, разрешённые/запрещённые effects, срок/отзыв; FTR-006 (report binding)/019/010/014/016; FTR-033 сверяет текущие read/output effects, не переносит authority на будущий ремонт | Missing/stale/revoked → запрет эффекта; проверить admission и resume |
| C-006A | Controller — issuer stage envelope | Transition/action/state/candidate и parent binding; FTR-006 (report binding)/010/014 | Mismatch/replay → отказ до effect; проверить execute/correct paths |
| C-007 | FTR-009; наблюдение repository и preview | Root/worktree/baseline/dirty state/actions/permissions; FTR-002/004/010/013; FTR-033 использует subject/read boundary Git и directory через разрешённый collector | Изменён subject → новое preview; проверить discovery binding, preservation, admission и сверку validation subject |
| C-008 | Worker FTR-010; factual observation (при потере не синтезируется recovery) | До/после, envelope, effects/unknown effects, stop reason; FTR-013/014/025, controller FTR-010 как reader observations | Неполный effect → reconciliation; проверить отсутствие двойного исполнения |
| C-009 | Controller выдаёт; FTR-011 возвращает observation | Purpose/transition, candidate, required checks, results, limitations; FTR-006 (report binding)/008/010/011/012/014/023; FTR-032 читает technical results/limitations, не получает полномочия ValidationEnvelope для отображения; FTR-033 читает purpose-bound outcomes, не aggregate health score | Required NOT_RUN/unknown impact → нет completion; проверить aggregation/staleness и разделение coverage/verification в UX surfaces |
| C-009A | Controller оценивает diagnostic record | Signature, hypotheses, prediction, recovery, correction binding; FTR-010 | Слабое Evidence/replay → DENY; проверить D0…D5 и fresh correction |
| C-010 | Наблюдавший checker/worker либо FTR-014 для recovery observation; immutable Evidence | Метод, subject, результат, locator, limitations; FTR-008/010/011/012/013/014/021/023/025/032; FTR-032 читает Evidence для surfaces/pack; FTR-033 импортирует Evidence с исходным subject, без объявления нового run | Недоступный источник → UNKNOWN; проверить ссылки, redaction, границу результата и применимость UX Evidence к page/runtime/source snapshot |
| C-011 | Человек — owner; FTR-012 готовит review | Actor/source, subject, decision, scope/время; FTR-006/008/012/015/019/021/025/032; FTR-032 читает запись и её применимость через FTR-012, не создаёт решение из viewer; FTR-033 читает origin/scope решения по Assessment, не создаёт human selection | Неизвестный actor/stale subject → решение не применяется; проверить admission без audit-модуля, UX badge/index и handoff по exact decision scope |
| C-012 | Controller создаёт первый record и владеет controller/lifecycle transitions по workflow; FTR-016 сохраняет/выдаёт | Versions, creation/resume context, state axes, candidate, authority, ledger, decisions, next action; FTR-007/008/010/014/016/017; продолжение FTR-032 обслуживают controller и FTR-016/014, без второго state owner; FTR-033 сохраняет continuity через FTR-016/controller; после handoff records historical | Старая revision → recover, не overwrite; проверить старые задачи, concurrency и продолжение UX page/index/pack operations |
| C-013 | FTR-004; план и наблюдённые результаты установки | Package/target, ownership, operations, preview, conflicts/recovery; FTR-004/009/011/014 | Конфликт user state → стоп apply; проверить install/update/uninstall и повтор |
| C-014 | FTR-015; отдельная запись каждого действия | Action, repo/source/target, candidate, authority, результат; FTR-012/014/015/024 | Remote uncertainty → проверить эффект до retry; проверить Git-действия отдельно |
| C-015 | Автор module contract; FTR-010 проверяет registration, FTR-016 хранит runtime binding | Identity/revision/interfaces/capabilities/lifecycle; FTR-004/005/009/010/011/014/016/019/022; contract FTR-032 и его вызовы проверяются через FTR-010/009/019, без собственной registry; FTR-033 recovery имеет отдельный module binding по §10.4, без собственной registry | Unknown/incompatible/disabled → нет нового вызова; проверить consumers, lifecycle и recovery, включая direct/queued операции FTR-032 |
| C-016 | Разрешённый caller/publisher формирует сообщение; FTR-010 владеет delivery, FTR-016 хранит | Operation/message/subject/authority refs, bounded payload, delivery/result; FTR-005/008/010/011/014/016/019; FTR-032 формирует запросы записи и получает связанные outcomes через FTR-010, не читает storage очереди напрямую; FTR-033 сохраняет external outputs/передаёт handoff через core; ack не receipt | Duplicate/stale/unknown effect → dedup/reconciliation; ack не закрывает task; проверить повтор и прерывание page/index/pack writes FTR-032 |

Сверка карты влияния обязательна при изменении входа dossier: каждый именованный C-contract из раздела «Входные данные» должен иметь эту фичу среди consumers таблицы либо явное объяснение неприменимости. Чтение contract собственным producer также учитывается, если он принимает сохранённый record как вход. Проверка criteria-to-Evidence и stale review входит в область изменения C-002/C-005; изменение C-007 затрагивает сверку candidate в FTR-013.

**Маршрут влияния FTR-032 — DRAFT.** Таблица включает как чтение источников,
так и явно названные делегированные пути [UX-модуля](#ux-pages-contract);
она не назначает FTR-032 reader всех внутренних records ядра.
При изменении C-002/C-003 сверяются expected set, mapping, UX-права и состав
journey/pack по [DS-T02/03/05/15–17/21](06_Features.md#ux-pages-cases).
Изменение C-005 затрагивает exact scope/criteria экспортируемой задачи;
C-009/C-010 — различение coverage и verification, subject/Evidence и ограничения
по DS-T01/04/10/11/18/21. Изменение C-011 ведёт к проверке применимости решения,
badge/index и handoff по DS-T06–09/18/19; отсутствие writer не обходится.
Для C-012/C-015/C-016 проверяются соответствующие core paths и операции FTR-032:
прерывание записи страницы/index/pack, потеря ответа, смена generation и
disable/remove с pending effects — по [§25.8](03_Development.md#ux-pages-verification),
[SC-T23–26](03_Development.md#core-transport-checks) и §25.5.
Это маршрут выбора affected checks, не заявление об их выполнении и не требование
перезапускать все проверки при любом изменении: scope определяется изменённой
гарантией; неизвестное влияние обрабатывается по [§18.1](03_Development.md#modular-maintenance).

Backlog, pattern и incident имеют владельцев содержания в своих feature contracts. Хранение через FTR-016 не передаёт ему это владение. Идентичность issuer/actor проверяется принятым способом capture, а не наличием имени в поле.

**Прикладной модуль FTR-031 — DRAFT.** Подготовка его application binding использует
C-002/C-003 через выбранное ТЗ; изменение ролей, полей, обязательных каналов или
правил доступа затрагивает [RA-T01–26](06_Features.md#rbac-abac-cases) по изменённой
гарантии. Runtime `rbac_abac` не читает Markdown ТЗ на каждом запросе. Его реальные
producers/consumers принадлежат host-приложению и перечислены в
[§10.3](#rbac-abac-contract). C-005/C-006/C-009/C-012 регулируют работу coding agent,
а не каждое прикладное решение ALLOW/DENY или применение AccessModel. C-015/C-016
не навязываются компоненту пользовательского приложения (§25.0 Development);
подключение этой capability как runtime extension самого AOS здесь не задано.
Нельзя добавлять FTR-031 reader внутренних records/очереди AOS по одному совпадению
слов «модуль», «решение» или «active». Возможная UX-проекция FTR-032 остаётся
производной; изменение её макета не активирует прикладную policy.

**Recovery / FTR-033 — DRAFT.** Изменение intent/desired sources затрагивает
Assessment/NextAction; subject/index/coverage и Evidence — claims/freshness;
origin/scope C-011 — human disposition, не наблюдаемые факты; C-005/C-006 —
допуск только текущей задачи. Изменения C-012/C-015/C-016 затрагивают saved state,
versions и передачу. [§10.4](#recovery-contract) задаёт реальные readers/writers;
[REC checks](03_Development.md#recovery-verification) повторяются по affected
claims/операциям, не всем FTR. Optional C-004/C-013 относятся к отдельным
последующим задачам, не required входам Recovery и не fallback authority.

<a id="architecture-patterns-interfaces"></a>

**Граница модуля FTR-005+022.** Группировка выбрана человеком; feature ownership
и [полный scope](06_Features.md#architecture-patterns-module) остаются у dossiers.
Внешние входы — C-002/C-003 и scoped discovery facts FTR-002; pattern corpus
принадлежит FTR-022 и необязателен для самостоятельного ADR. Выходы — rationale
«ADR не нужен», source-bound recommendation либо C-004 для существующих consumers;
для запроса архитектуры системы — [целостный документ](#architecture-output-handoff)
для FTR-006 и, когда выбран потребителем сценария, FTR-007. Применимость и критерий
handoff определены по ссылке выше; документ не является новым видом C-004.
Материальный human choice проходит существующую trusted review boundary;
recommendation не подменяет решение. Самостоятельный запрос анализа не разрешает
применение решения; уже покрытая разработка продолжается по Development §25.0.

FTR-005 владеет архитектурным документом и ADR, FTR-022 — pattern cards; FTR-016 может сохранять
артефакты без передачи владения. Изменение pattern revision не переписывает C-004,
а stale source требует повторной оценки зависимой recommendation. Сохранённый
C-004 читается FTR-005/022 с проверкой subject/условий до reuse. Отказ библиотеки
не запускает её install; отключение модуля не удаляет artifacts/Evidence и не
отключает чтение ранее принятых facts ядром. FTR-025 даёт optional observations,
его отсутствие не блокирует ADR. Группировка R4 сама не вводила transport contracts. Теперь подключение следует общим C-015/C-016 R7, без обязательного plugin framework или запуска FTR-007.

<a id="architecture-patterns-save-recovery"></a>

**Документальный пример MOD-S18: потеря подтверждения — DRAFT.** Для
`architecture.save_draft` сохранён admission операции O по task/revision T/R,
точному draft D и owned destination P; запись могла завершиться, но C-008/ответ
потерян. Единственный продолжатель сначала восстанавливает C-012, проверяет
current authority и сверяет O, ledger и фактическое содержимое P в разрешённом
read scope. Если подтверждены именно D и эффект O, повтор записи не нужен:
recovery observation C-010 связывает найденный эффект с admission; он не
подделывает C-008 и не принимает ADR за человека. Если доказано отсутствие
эффекта и завершение прежней попытки, допустим fresh attempt той же logical O
по C-016 и новому admission. Если данные неоднозначны или worker ещё действует,
зависимая запись не повторяется; сохраняются unknown/in-flight и WAIT_EVIDENCE
до достаточной reconciliation. Одного отсутствия ответа или файла недостаточно,
чтобы доказать отсутствие всех effects. Следующий шаг определяется §10.2/§10.5
Development. Пример проверяет описание; реальная потеря процесса и автоматическое
возобновление остаются NOT_RUN до наблюдения в выбранной среде.

**Сценарные readers.** FTR-025 читает C-011 при обработке решения по lesson,
не при первоначальной записи incident. FTR-024 читает C-014 как результат exact
запроса к FTR-015; единственным исполнителем Git/Release остаётся FTR-015.
Карты входов/consumers учитывают эти условные маршруты и примеры, а не делают
будущий результат обязательным входом первоначальной подготовки.

**Совместимость — предложение.** Необязательное пояснительное поле совместимо лишь если reader contract допускает его игнорирование и оно не влияет на authority/state/completion. Strict format с запретом неизвестных полей требует новой reader-version или явного отказа. Изменение смысла, обязательности, enums или state machine несовместимо до доказательства обратного. Совместимость определяется парой producer/consumer versions, а не только номером версии.

Старая задача допускает inspection без effects, если её формат поддержан. Resume требует поддержанного state-machine contract и fresh authority. При необходимом преобразовании видны исходная/целевая версия, затронутые данные и recovery; оно выполняется только в отдельно разрешённом scope. Исходный record сохраняется; новое представление не создаёт human approval. Прерванное преобразование требует reconciliation до resume. Диапазон поддерживаемых версий относится к MOD-DEC-02; пока он не выбран, runtime support UNKNOWN.

**Отказ и отключение.** Модуль может отсутствовать, работать, быть недоступным или завершать начатую операцию. Это описания capability, не новые task/run enums. Новая операция требует своих required capabilities. Отключение write-модуля начинается с определения effects и сохранения recoverable state; мгновенное безопасное удаление не обещается. Данные пользователя и Evidence не удаляются вместе с модулем. Отказ индекса допускает прямой поиск, отказ проверки authority блокирует effect. Обязательный CI без declared equivalent остаётся NOT_RUN. Ограничение покрытия видно пользователю и не выдаётся за полный PASS.

**Authority.** Базовый admission проверяет human provenance, срок, scope и subject до эффекта. FTR-021 аудитирует записи, но не служит обязательным сервисом выдачи разрешений. Отказ optional audit не отключает базовую проверку; отсутствие доверенного способа capture (MOD-DEC-03) блокирует затронутые действия. Включение модуля не предоставляет network/provider/Git/delete authority.

**Сопровождение.** Изменяется owner contract, затем проверяются его consumers и acceptance/negative cases из таблицы. Новое состояние или effect требует владельца, отказа и recovery. Неизвестное влияние требует расширения проверки. Derived index не изменяет Product facts. Эта таблица описывает межфичевые contracts; детализация конкретных сценариев находится в dossiers.

<a id="scaffold-core-profile"></a>

### 6.2. Первоначальный профиль scaffold/core — SCAFFOLD_CORE_DRAFT

Предлагается проверить применимость прежнего AOS-3 профиля: local modular monolith, Python 3.12+, минимальные зафиксированные зависимости, локальная CLI-поверхность, repository-relative данные, отсутствие обязательного network client в продукте. Это предложение SC-DEC-02 с [provenance](05_Reference.md#scaffold-core-sources), не новое утверждение о существующем runtime или stack selection.

До реализации профиль должен назвать конкретные OS/runtime versions, target role и base, путь локальных state/evidence и queue/registration storage, допустимую dependency policy, finite queue profile C-016 и test command binding. Support claim первой версии ограничен проверенным macOS envelope; требование переносимости ядра сохраняется для целевых Linux/Windows. Внутренний storage engine и serialization HOW остаются за агентом; гарантии current identity, integrity, durable recovery и human provenance обязательны при любом представлении. Работа coding host с внешним provider отдельно проверяется по SC-DEC-03 даже при local-only продукте.

**Граница версии:** исходно поддерживаются только явно принятые Task/Authorization/Envelope/State contracts и их зафиксированные версии из этого owner. Неизвестная версия read-only показывается как unsupported, если не может быть безопасно разобрана; effect/resume запрещён. Старые AOS-3 данные не импортируются автоматически. Обязательный новый field, изменение enum/authority/completion или meaning создаёт несовместимость; producer/consumer compatibility проверяется до принятия сохранённой задачи. Optional field можно игнорировать только при явном разрешении reader contract.

<a id="core-platform-boundary"></a>

**Переносимое ядро и платформенная граница — SCAFFOLD_CORE_DRAFT.** Product
[задаёт переносимость](01_Product.md#core-os-portability); macOS — первая
проверяемая среда. Предложенный execution adapter — минимальный локальный adapter
с переносимым интерфейсом и платформенной реализацией. Конкретное средство
исполнения ещё не выбрано (SC-DEC-02).

Ядро владеет смыслом task/authority/results/state; adapters изолируют операции
файловой системы, процессы, права и системные инструменты. Зависимость от Unix
shell, терминала или macOS-приложения не становится обязательной для ядра.
Профиль adapter объявляет необходимые capabilities и ограничения. Preflight
проверяет реальные возможности; имя ОС само по себе не доказывает поддержку.

Пути, пробелы/Unicode, разделители и чувствительность к регистру обрабатываются
по фактам target filesystem. Нормализация не должна объединять разные subjects,
расширять allowed scope или скрывать collision/traversal. Process completion,
termination, permissions и interrupted file operations имеют наблюдаемые
результаты; отсутствие механизма не заменяется фиктивным success.

Missing required capability блокирует её сценарий. Независимое чтение/проверки
остаются доступны. Fallback разрешён только при доказанном сохранении authority,
result/recovery guarantees и покрытом scope; capability check не выдаёт доступ.

C-012 сохраняет переносимые предметные данные и явные environment/path bindings.
Поддержанное inspection на другой ОС не разрешает effect/resume: текущие paths,
permissions, runtime/adapter, authority и незавершённые effects должны быть
повторно связаны. Неизвестное соответствие блокирует продолжение; нельзя молча
переписать абсолютные пути или сбросить ledger. В R3 новые поля, wire formats и
версии C-contracts не вводятся: это уточнение существующих identity/environment,
read-only inspection и fresh admission требований V2.

<a id="core-loop-v2"></a>
<a id="core-loop-v3"></a>

**Версии первого core-профиля — SCAFFOLD_CORE_DRAFT R5.** Текущий набор:
`AOS_COMPLETE_TASK_LOOP_V3`, `AOS_EFFECTFUL_STAGE_ENVELOPE_V3`,
`AOS_VALIDATION_ENVELOPE_V3`, `AOS_CORRECTION_GATE_V3`; C-012 сохраняет V3
state-machine binding. C-005/C-006 остаются V1 с неизменными полями. Девять
controller actions и 26 рёбер сохранены; V3 добавляет обязательные lifecycle
условия допуска и атомарность их применения, а не новые полномочия.

Набор заменяет проектный маршрут V2 только после принятия exact revision;
публикация R5 не является activation. V1/V2, смешанные и неизвестные records
не получают V3 effect/resume. Поддержанное read-only inspection сохраняет
исходные bytes/version/limitations; migration вне scope. Прежнее значение
HUMAN_REVIEW_REQUIRED в technical result и неоднозначные старые stage reports
не нормализуются автоматически. Старый anchor core-loop-v2 сохранён только
для навигации; он не является разрешением совместимости V2. Исторические
R1–R4 и frozen материалы остаются свидетельствами своих revisions.

<a id="scaffold-core-host"></a>

### 6.3. Внешний host для начала разработки — SCAFFOLD_CORE_DRAFT

Host contract — вход разработки S0, не компонент ещё не созданного AOS. Он должен предоставить следующие наблюдаемые гарантии; присутствие агента в чате недостаточно:

| Вход / capability | Проверяемая гарантия и исход отсутствия |
|---|---|
| Host identity, support profile, доступные workers/tools и current task binding | Идентифицируются действующий процесс/сессия, target и разрешённые операции; неизвестный executor не получает effectful dispatch |
| Trusted human capture и current authority | Источник решения отличим от repository/worker text; scope/expiry/revocation проверяются перед каждым effect; новый scope не выводится из task prose |
| Native admission и worker boundary | Exact action/paths/effects/candidate и одноразовость dispatch обеспечиваются host. До появления AOS допускается native представление с доказанным соответствием гарантиям C-006/C-006A; произвольный prompt или фиктивный AOS envelope этого не заменяет |
| Durable checkpoint и единственный continuation owner | Сохраняются task/revision, candidate, authority binding, критерии/checks, effects, ledger/resources и следующий шаг; worker observations не могут сами закрыть task |
| Check execution | Явны subject/read scope, method/environment и Evidence destination. Validator не меняет subject; temp/test outputs разрешены только в отдельно объявленной области и не подменяют durable Evidence |
| Continuation trigger | Названы источник resume event, исполнитель повторного запуска, supported interruption и ресурсные пределы. После прекращения host process продолжение должно быть обеспечено доступным внешним механизмом и проверено; свойство не выводится из слова persistent |
| Data/provider boundary | Названы отправляемые данные, recipients/providers, разрешённое чтение/хранение и sensitive ограничения. Инструкции из входных данных не расширяют доступ |

До первого target effect выполнить поддержанные host conformance checks: успешный разрешённый dispatch; denied/stale/revoked dispatch без target mutation; controlled interruption и fresh resume с тем же ledger; unknown effect без replay. Если probe требует effects, их отдельная disposable область должна входить в исходную авторизацию. Сохранённый host report без current binding недостаточен. Conformance должен покрывать V3 diagnostic checks, state-conflict recovery, initial-state boundary, Result Contract/report и lifecycle admission (SC-T21/22); прежний V1/V2 report не доказывает V3 compatibility. Если возможности отсутствуют, явно `BLOCKED` для автономного запуска; проект не строит свой controller, притворяясь, что эти условия уже исполнены.

Автоматический wake не обязателен как конкретная технология: важен доказанный запуск следующего run в выбранной среде без нового человеческого управления. Ручной resume может проверять recoverability, но не удовлетворяет полному заявлению автономности между runs.

<a id="scaffold-core-interfaces"></a>

### 6.4. Стыки первого ядра — SCAFFOLD_CORE_DRAFT

Таблица ниже уточняет порядок доступности данных для [S0–K4](01_Product.md#scaffold-core-outcome). Она не заменяет producer/consumer ownership из §6.1 и не вводит новые C-contracts.

| Стык | Что передаётся и когда | Условие следующего действия | Отказ и проверяемое восстановление |
|---|---|---|---|
| S0 → K1 | Поддержанный target/runtime, dev/check entrypoints, candidate и внешний checkpoint до продуктового цикла | Независимый от AOS host может начать реализацию/проверку K1 | Missing tool/dependency блокирует criterion S0; повторная подготовка в scope, без удаления user state |
| FTR-001/002 → FTR-003 | C-001, подтверждённые ответы, source-bound findings либо явное отсутствие проекта | Requirements сохраняют смысл входа; достаточные ранее принятые ответы не запрашиваются повторно | Material gap видим; частичное knowledge не становится полным Spec |
| FTR-003 → FTR-006 | Принятый C-002/C-003, критерии и constraints до requested scope | Brief содержит task/revision и проверяемые критерии, но не выданную authority | Changed contract делает зависимый Brief stale; rebind без подмены human choice |
| FTR-006 / trusted capture → FTR-019/009 → FTR-010 | C-005/action, отдельный current C-006, permission, C-007 до dispatch; при correction C-009A | Controller сужает scope до C-006A; current action/state/candidate и authority совпадают | Denied/missing/replayed input запрещает effect; DRAFT Brief и безопасное read-only исследование доступны |
| FTR-010 → FTR-013/011 | FTR-013 получает C-008 и actual candidate после worker, либо независимый recovery observation C-010/FTR-014 при потере C-008; FTR-011 — подготовленный validation subject и C-009/read scope от controller до checks | Validation subject exact; observer/provenance доказаны; required results не stale | Partial/unknown effect или missing C-008 → FTR-014 для reconciliation по admission/ledger/target до retry; validator не делает correction |
| FTR-011 → controller FTR-010 | C-009 purpose-bound results и C-010 Evidence после CHECK/FINAL_VALIDATE | DIAGNOSTIC возвращается в DIAGNOSE без закрытия критериев; ACCEPTANCE/FINAL PASS закрывает только проверенные критерии; failure/unknown направляется в D0…D5 | Correction Gate bind diagnostic/candidate/action; новый effect требует нового gate/envelope и affected checks |
| Controller ↔ FTR-016 / FTR-014 | C-012: отдельные создание первой задачи и resume; effect/authority observations при checkpoint | Один владелец controller-action transitions; storage не решает lifecycle, resume rebind current facts | Concurrent/stale state не перезаписывает принятое; unsupported version/unknown effect запрещает continuation до reconciliation |
| FTR-011/013/016 → FTR-008/012 | Current criteria/results/candidate/context для status и review | Каждый criterion виден, отдельный Human Decision применим только к своему subject | Missing result остаётся NOT_RUN; новый candidate не наследует human acceptance |
| Внешний host → product controller | Task/authority/criteria, candidate, effects, непрерывный ledger/resources и supported state representation | Все обязательные гарантии обоих routes проверены; есть один active continuation owner | Неподдержанная передача сохраняет внешний route. Частичная передача сначала reconciled; обратно переносить state можно только с доказанной совместимостью |

К моменту первого product effect должны быть доступны минимальные FTR-011/013/014/016 гарантии; порядок срезов не разрешает mutation без них. Backlog FTR-007 не требуется для конечной dependency-ready последовательности критериев одного C-005. Сохраняемая transport queue C-016 — отдельная обязательная capability первого ядра для queued exchange; она не выбирает критерии и не выдаёт authority. Предварительно выбранные product inputs позволяют проверить целый цикл без новых продуктовых решений в середине run.

Замена общего contract требует определить всех его реальных consumers, проверить supported versions, invalid inputs и прошлые saved tasks. Новая фича имеет свой owner, явно declared effects и восстановление; отсутствие/отключение optional capability не отключает обязательную authority или result validation ядра. Изменение такого baseline оформляется отдельной принятой contract revision; реализация нового модуля не может сама переписать базовый safety contract.

### 6.5. Доступность коннекторов и очереди в первом ядре — R7

S0 объявляет C-015/C-016 и profile подготовки. До первого queued effect K2
готовы минимальные registration, durable enqueue/claim, current admission,
operation ledger, result validation и recovery; K3 доказывает redelivery и
interruption, K4 — integrated direct/queued journey. Обязанности распределены
между существующими core FTR-009/010/011/014/016/019 и status FTR-008, новые FTR
или внешний broker не добавляются. Очередь не требуется для direct read-only
запроса; pending сообщение не гарантирует начало работы без доступного executor.

Первоначальные registry/queue storage создаются как отдельно покрытая служебная
операция controller по initial-state guarantees: exact root/profile/authority,
create-if-absent, existing ownership/history, recovery при partial publication.
Создание очереди не enqueue в ещё не существующую очередь и не выполняет product
effect. Resume не пересоздаёт потерянную историю. Внешний development host ведёт
разработку независимо от создаваемого product transport; его capabilities V3
не доказываются запуском ещё не созданных коннекторов. SC-T23…26 выполняются
на продукте по мере готовности; early host conformance не требует собственной
реализации C-015/C-016 очереди до S0.

## 7. Ортогональная модель состояний

Оси не изменяют друг друга автоматически.

```text
Document maturity:
DRAFT | HUMAN_REVIEW_REQUIRED | HUMAN_ACCEPTED | SUPERSEDED

Lifecycle stage:
PLAN | EXECUTE | VALIDATE | REVIEW

Controller action (`AOS_COMPLETE_TASK_LOOP_V3`):
BIND_TASK | RECOVER_STATE | SELECT_NEXT_ACTION | EXECUTE | CHECK | DIAGNOSE |
CORRECT | FINAL_VALIDATE | IDLE

Task state:
ACTIVE | WAIT_HUMAN | WAIT_EVIDENCE | TECHNICALLY_COMPLETE |
TASK_FAILED | CANCELLED_BY_HUMAN | CONTRACT_VIOLATION

Run state:
RUNNING | PAUSED_RESOURCE | STOPPED

Human decision:
ACCEPT | NEEDS_CHANGES | REJECT | DEFER

Permission:
ALLOWED | HUMAN_AUTHORIZATION_REQUIRED | BLOCKED_POLICY | BLOCKED_UNKNOWN | NOT_APPLICABLE
```

Technical result определяется только [единым C-009](#technical-result-contract);
перечисленные выше оси не добавляют ему допустимых значений.

Canonical controller-action matrix `AOS_COMPLETE_TASK_LOOP_V3`:

| `from` | Допустимые `to` |
|---|---|
| `BIND_TASK` | `RECOVER_STATE`, `IDLE` |
| `RECOVER_STATE` | `SELECT_NEXT_ACTION`, `DIAGNOSE`, `IDLE` |
| `SELECT_NEXT_ACTION` | `EXECUTE`, `CHECK`, `FINAL_VALIDATE`, `IDLE` |
| `EXECUTE` | `CHECK`, `DIAGNOSE`, `IDLE` |
| `CHECK` | `SELECT_NEXT_ACTION`, `DIAGNOSE`, `FINAL_VALIDATE`, `IDLE` |
| `DIAGNOSE` | `CHECK`, `SELECT_NEXT_ACTION`, `CORRECT`, `IDLE` |
| `CORRECT` | `CHECK`, `DIAGNOSE`, `IDLE` |
| `FINAL_VALIDATE` | `DIAGNOSE`, `IDLE` |
| `IDLE` | `RECOVER_STATE` после resume event |

Матрица описывает только controller-action axis. `WAIT_HUMAN`,
`WAIT_EVIDENCE`, `TECHNICALLY_COMPLETE`, `TASK_FAILED`,
`CANCELLED_BY_HUMAN` и `CONTRACT_VIOLATION` изменяют task state и переводят
controller action в `IDLE`; `PAUSED_RESOURCE` изменяет run state, сохраняет task
`ACTIVE` и также переводит action в `IDLE`. Lifecycle stage меняется controller только по
[явным правилам workflow](03_Development.md#core-lifecycle-transitions). Переходы между разными осями не записываются как `{from,to}`
controller actions.

Отдельное допустимое основание `ACTIVE/RUNNING/IDLE` — доказанный recovery
checkpoint при takeover по [Development §10.2](03_Development.md#state-conflict-recovery).
Его owner/reconciliation bindings сохраняются durable; без них произвольный idle
невалиден. Это не новая ось или controller edge и не разрешение на dispatch.

`DIAGNOSE → CHECK` выдаёт только C-009 с purpose DIAGNOSTIC; его завершение
возвращает `CHECK → DIAGNOSE`, сохраняя signature/level/ledger. Переход
`DIAGNOSE → SELECT_NEXT_ACTION` допустим после Evidence-bound разрешения finding
без mutation: записаны причина отсутствия correction и оставшиеся required
checks. Он не означает PASS этих checks или task completion. При необходимости
mutation сохраняются C-009A и отдельный CORRECT worker.

При конфликте state действует [recovery protocol](03_Development.md#state-conflict-recovery):
отклонённая запись не создаёт переход. Прямые CHECK/EXECUTE/DIAGNOSE → RECOVER_STATE
не разрешены; следующий владелец использует свежий state и IDLE/resume route.

## 8. Владение данными

| Fact class | Owner |
|---|---|
| Product requirement | Human-accepted Product artifact |
| Feature behavior | Human-accepted Feature Passport |
| Architecture decision | Human-accepted ADR |
| Task scope | Exact Task Brief |
| Execution permission | Exact Execution Authorization Record |
| Repository state | Instrumental Git/filesystem observation |
| Human decision | Human-authored/verified record |
| Evidence | Immutable subject-bound record |
| Dashboard/status | Derived view |
| Registry/RAG/cache | Rebuildable derived data |
| Legacy finding | Reference record, authority none |

<a id="event-diagnostics-contract"></a>

### FTR-025: диагностическая projection действия — DRAFT

Контракт уточняет [минимальное поведение](06_Features.md#event-diagnostics-behavior), не весь incident/lesson scope. FTR-025 владеет своим диагностическим представлением; C-008/C-010 остаются источниками наблюдений, C-012/controller — единственным владельцем текущего исполнения, FTR-011/C-009 — результата проверки. Raw ledger/store не читается сторонним writer: adapter передаёт только разрешённую projection. До появления C-008 старт/отказ берётся из фактического наблюдения adapter, не из придуманного execution record.

| Producer → существующая boundary → consumer | Смысл, mode и проверяемая граница |
|---|---|
| Trusted action adapter/FTR-010 → supplied context и C-008/C-010 refs при наличии → FTR-025 | Action kind/binding revision, безопасная task/run/attempt/operation correlation, наблюдение и фактический исход. Нормализация данных сама не создаёт запись/authority |
| FTR-025 → диагностический результат в versioned contract выбранного action → caller/report → пользователь | Совместимый payload и безопасный код причины, с ограничениями; исходный result/exit code не меняется. Отдельный новый viewer CLI не требуется |
| Caller с покрытой служебной записью → действующий EXECUTE COMMAND C-016/FTR-010 → диагностическая запись внутри declared effects | Если сохранение нужно, оно входит в уже admitted command и bound C-015 action profile. Нельзя спрятать запись в DIRECT_READ/QUEUED_EVENT или выдать новое разрешение из event payload |
| Разрешённый reader → сохранённые observations → пользователь/отдельный Evidence owner | Read-only чтение не создаёт отсутствующее хранилище и не ремонтирует его. Mutable diagnostics не C-010: при отдельном экспорте owner связывает exact bytes/subject/limitations |

Подключается один существующий action с точным interface/version/generation и диагностической projection, не самостоятельный обязательный logging service. Внутренний вызов writer — HOW; отдельная доставка команды на каждое событие не требуется. Если позднее нужен самостоятельный receiver/подписчик, его C-015/C-016 effects и consumers рассматриваются отдельно. Новый broker/registry/FTR-026 не prerequisite. Отключённая диагностика не отменяет обязательные C-008/C-010/C-012 reports.

Identity сохраняет смысл своего owner. Run, invocation, task и logical operation не объявляются взаимозаменяемыми и не преобразуются в UUID ради формата. Adapter либо передаёт безопасный существующий handle, либо явно опускает неподтверждённое необязательное значение; нужная для положительного сценария корреляция должна быть доказана. Константа component допустима вместо отдельного action name только если exact binding однозначно обозначает выбранное действие. Branch/HEAD сами по себе не exact subject, а timestamp не доказательство порядка или полноты. Counter/locator не создаёт новую authority identity.

Technical result использует текущий C-009: CONTRACT_VIOLATION/FAIL/BLOCKED/UNKNOWN/NOT_RUN/PASS. HUMAN_REVIEW_REQUIRED — maturity, не event result; ACCEPT и прочие human decisions также исключены. Отдельный caller enum нельзя молча переименовать или объединить с C-009: до подключения определяется поддержанный semantic mapping либо ограничение несовместимого caller. Ошибка адаптации результата ограничивает диагностику и сохраняет исходный ответ primary. Локальный outcome «записано / пропущено / ошибка или неизвестный исход» не подменяет C-009 result. Required Evidence/checks продолжают ограничивать aggregate независимо от optional diagnostics.

Privacy boundary допускает только закрытые поля projection и коды, заранее обеспеченные выбранным action binding. Коды должны сохранять нужное различие причин в первом сценарии; если его нельзя безопасно передать, limitation видима и usefulness не считается доказанной. Free-form payload/stack trace/URLs/секреты не добавляются. Проверяются происхождение IDs и реальный adapter, а не только regex/schema writer. При disabled/read-only профиль пропускает диагностическую запись до связанных с ней filesystem I/O/queue operations; прочие разрешённые действия primary не приписываются logger.

Для persistent профиля объявляются один совместимый destination у существующего runtime-state owner, access/effects, finite record/storage/work limits и retention boundary. Никаких defaults из cwd, новой `.aos/` topology, автоматического ignore/untrack или обхода frozen subject. Guard проверяет actual target; конфликты user-owned data, небезопасные links/access или неподдержанная filesystem boundary дают отказ диагностики. Поддержка разных worktrees не объединяет их хранилища автоматически. Метод проверки, file format, permissions primitives и синхронизация остаются HOW выбранного profile.

Concurrent attempts не смешивают записи и не превышают declared limits: успешная целая запись либо явный ограниченный failure/занятость. Ожидание конечно; нет скрытого бесконечного retry. Partial/unknown append не объявляется подтверждённым и не повторяется автоматически; остаётся возможность прочесть прежние complete observations с честными ограничениями. Core redelivery того же COMMAND не создаёт новый primary action ради журнала; исход unknown effect сверяется текущим owner. Запись не обещает audit-grade/power-loss durability, если она отдельно не определена и не проверена; обязательная durable history не заменяется этим профилем.

При ошибке используется совместимый существующий report/diagnostic channel: одно безопасное уведомление на invocation без raw пути/payload, рекурсивного события или повреждения JSON stdout. Если сообщение не удалось доставить, writer/adapter не утверждает обратное. Primary outcome и отдельная recording limitation различимы; aggregate owner может независимо признать отсутствие required Evidence. Это уточняет FTR-025.N03, не гарантирует фиксацию при потере всех каналов.

Lifecycle следует §6.1/C-015: ADD/ENABLE проверяет пользу, exact binding и scope до записи; UPDATE проверяет reader/payload/profile versions и in-flight command outcomes без silent migration; DISABLE прекращает новую optional запись и reconciles начатое; REMOVE implementation не удаляет observations/ledger/owner records; DELETE DATA требует отдельного scope/решения, не следует из возраста/переполнения. Диагностику можно убрать без отказа обычного action/report. Несовместимый сохранённый формат не переписывается автоматически; читается поддержанная история либо сообщается ограничение.

FTR-014 нужен сценарию recovery observations, а не как обязательный запуск перед записью; FTR-021 остаётся CHECK_ONLY. Logging не активирует FTR-023, поиск incidents или обучение lessons. Перед runtime связываются action, caller result/identity contract, diagnostic channel, storage/support/limits/retention и имеющиеся utilities; отсутствие этих inputs ограничивает запуск, но не документальную оценку. [EV-C01–12](03_Development.md#event-diagnostics-verification) проверяют и допустимый сквозной результат, и нарушения границ.

## 9. Таксономия registries

Product Feature Registry индексирует Feature Passports. Execution/Verification Registry индексирует technical records. Protected Artifact Registry — optional Governance. Derived Context Index — navigation only. Ни один registry не владеет product truth независимо от accepted source artifact.

## 10. Архитектура контекста

```text
minimal bootstrap
→ identify project/task/state
→ locate authoritative files
→ use index only for navigation
→ create explained task-local Context Pack
→ verify freshness
→ bounded work
→ handoff
```

Индекс модуля «Граф RAG» (FTR-017) активируется после measured search/context problem; [контракт](#graph-rag-module-contract) сохраняет прямой поиск без обязательного индекса.

Для 005+022 task-local context начинается с [короткого входа модуля](06_Features.md#architecture-patterns-entry),
затем содержит относящиеся к вопросу current constraints, source/subject revisions,
критерии, неизвестные данные и ссылки на owners. После остановки фактический
state берётся из C-012 и observations, а не из пересказа brief. Это уточнение
существующего context route — DRAFT, без нового хранилища или обязательного RAG.

<a id="repository-graph-contract"></a>

### 10.1. Производный граф модуля «Граф RAG» — DRAFT

Этот DRAFT адаптирует прежний [R2](05_Reference.md#repository-graph-tz) для одной FTR-017 «Граф RAG». Название/состав определены в [Product](01_Product.md#repository-graph-purpose); расширение поиска/сравнения и подключения — [ниже](#graph-rag-module-contract). Старые graph-only budgets и широкие parser/pagination возможности — кандидаты расширенного профиля, а не все обязательства первого lexical/graph subset. Гарантии source binding, coverage, authority и безопасных effects применяются с первого среза. Это не разрешение реализации.

**Единая производная модель.** Для объявленного worktree/scope профиль связывает активные graph/index projections с собственными input revisions. Target и Observed различимы, но не ведутся как две редактируемые базы истины. Допустим временный кандидат публикации; общий source manifest не создаёт ложного общего fresh-флага. Обзор генерируется по запросу. Удаление производных данных не уничтожает первичные требования, решения или уникальный обязательный контекст; число файлов/storage layout не фиксируется.

Граф содержит сведения о версии схемы, extractor и профиле наблюдения, scope и source bindings, sources, nodes, edges, evidence, coverage, unresolved и pending refresh. Это логические части одного контракта, а не требование отдельных registries. Конкретный storage, parser, индексы, алгоритмы IDs/обхода и механика записи относятся к Engineering Design по `00_Core.md`, §12; они здесь не фиксируются. Набор поддержанных extractors объявляется профилем; перечень R2 ниже не обещает полную поддержку в первой версии.

#### Наблюдения, идентичность и доказательства

- Node представляет существующий component, entrypoint, symbol, artifact/contract, test, feature record или external reference. Одно наличие path в inventory не требует semantic node. Обязательные сведения: stable identity, kind/label, source references, применимый locator, fact class, basis, mapping state и evidence references.
- Edge имеет собственную stable identity, направленные endpoints, конкретное отношение, fact class, basis, evidence и область применимости. Пара endpoints не является identity связи. Разные утверждения и parallel edges сохраняются; повторное наблюдение одного утверждения может добавлять evidence.
- Source связывает repo-relative path с digest конкретных наблюдавшихся bytes и file kind. Evidence имеет identity, source-version reference, locator, вид наблюдения и краткое проверяемое утверждение. Новые bytes не получают прежнее evidence через автоматическую перепривязку. Большие исходные тексты, полный AST и логи в граф не копируются.
- IDs не зависят от строки, позиции в выдаче или текущего content hash. Rename без доказанной преемственности означает remove/add. Способ доказательства и сохранения identity объявляется поддержанным контрактом.
- Fact class, mapping state и execution status разделены на уровне конкретного claim. Назначение сущности является отдельным утверждением со своим источником; модельное объяснение остаётся `SYNTHESIZED`. Свежий node не делает свежей stale edge. Наличие теста не означает его PASS.
- Runtime evidence ссылается на отдельный immutable run/test artifact с exact subject binding. Граф не запускает проверки скрыто. Digest подтверждает привязку к bytes, а не истинность интерпретации; семантика проверяется отдельными cases и review.

Начальный словарь отношений:

| Relation | Направление и смысл |
|---|---|
| CONTAINS | Контейнер → существующий элемент |
| IMPORTS | Импортирующий модуль → разрешённый модуль/reference |
| CALLS | Caller → callee; static и observed-runtime basis различаются |
| READS, WRITES | Компонент → читаемый/изменяемый artifact или state |
| PRODUCES, CONSUMES | Компонент → производимый/потребляемый artifact или type |
| VALIDATES | Проверяющий компонент → объект проверки |
| TESTS | Тест → проверяемый subject, без утверждения о результате запуска |
| ROUTES_TO | Наблюдаемый dispatcher/configured route → target |
| BINDS_TO_FEATURE, BINDS_TO_CONTRACT | Реализация/артефакт → существующий feature/contract record |

`producer --PRODUCES--> artifact <--CONSUMES-- consumer` сохраняет направление CONSUMES во всех представлениях. Совпадение имён или типов не доказывает wiring. Обобщённые IMPLEMENTS/DEPENDS_ON не должны скрывать конкретное отношение или подразумевать полноту фичи. Новое отношение вводится только для смысла, не выражаемого текущими типами и qualifiers.

#### Coverage и границы извлечения

Поддержанный scope включает inventory, package/module boundaries, entrypoints, нужные публичные symbols/endpoints, imports, однозначные static calls, schemas/types, tests и явные feature/contract references. Coverage различает inventory, структурный разбор и исследованные data flows. Полная модель каждого AST-узла и всех программ на выбранном языке не требуется.

Семантические связи допускаются по явному wiring/configuration/binding либо ограниченному исследованию с проверяемым основанием. Неоднозначный callee/consumer остаётся unresolved с вопросом, evidence, search boundary и следующим read-only probe. Фиктивный internal node ради целостности запрещён; external reference не означает исследования внешней реализации. `NOT_FOUND` ограничен поиском, `UNKNOWN` не означает отсутствие, `NOT_RUN` не означает неисправность. Утверждения документа о целевом поведении не создают observed runtime edges; acceptance требует своего exact source.

Optional observation batch допускается только как явный поддержанный input build/refresh: identity/revision, source bindings, claims/locators, fact classes, search scope, unresolved и ограничения. Проверка схемы, ссылок, scope и конфликтов не превращает интерпретацию агента в факт или Human acceptance. Содержимое batch не исполняется и не извлекается неявно из беседы. Exact batch либо доступен вне графа в разрешённом долговременном артефакте существующего workflow, либо его claims считаются невоспроизводимым optional enrichment и не могут быть единственным обязательным контекстом.

#### Операции и границы изменений

Названия операций описывают предлагаемый интерфейс, а не существующие команды AOS.

| Операция | Input → output | Допустимые изменения |
|---|---|---|
| build | Repo/scope/profile и optional supported batch → первоначальный граф/coverage | Только разрешённый output и временные ресурсы публикации |
| check | Graph + repository/scope → freshness/delta report | Нет |
| query | Graph + selector/mode/options → ограниченная выдача | Нет |
| refresh | Graph + repo/scope/profile и optional supported batch → graph/semantic diff | Только разрешённый output и временные ресурсы публикации |
| validate | Graph → integrity findings | Нет; validator не ремонтирует subject |

Reader, check, query, validate и help не записывают source, Git index/refs, graph, caches или lock files. Build не разрешает заменить существующий чужой output. Разрешённый task scope на обновление графа не требует approval каждой записи. Сканирование не импортирует и не исполняет код проекта; тесты не являются неявным действием.

#### Ограниченная выдача и impact

Selectors: exact typed ID, repo-relative path и exact FTR-ID через существующие bindings. Неоднозначность возвращается явно; поиск по имени даёт кандидатов, не подменяет exact lookup. Overview показывает области и границы знания; context — seeds и ближайшие связи; impact — потенциальную область проверки с объясняющими цепочками; detail — полные сохранённые records/evidence.

Для pilot предлагаются direction both, depth 1 для context и depth 2 для impact. На поддержанной цепочке producer → artifact ← consumer стандартный impact(producer) должен включать обе связи и consumer, возможно на продолжении. Более узкая depth/direction/filter явно оставляет frontier; глубина ограничивает смысл запроса, а page budget — только его выдачу. Impact не доказывает полный радиус runtime effects или отсутствие неизвестных consumers.

Начальные цели страницы: 40 nodes, 80 edges, 16 KiB UTF-8 целого ответа с metadata; overview — 8 KiB. Пользователь может явно изменить budgets. Stubs считаются в node budget, distinct node учитывается один раз на странице; повтор stub на следующей допустим. Seeds не обрезаются общим лимитом первой страницы. Whole records не теряют полей; endpoints каждой edge присутствуют на той же странице хотя бы как stubs. Evidence доступно через detail.

Ответ сообщает graph digest, selector/mode, применённые filters/direction/depth/budgets, freshness scope, общее число seeds и IDs seeds страницы, coverage limitations, truncation, причины ограничения и продолжение. Первая страница показывает наличие критичных unknowns, краткий summary и путь раскрытия. Приоритет seeds и существенных interfaces/data/test relations влияет на порядок, но не исключает прочие подходящие связи.

Continuation детерминировано и привязано к graph digest и всем параметрам запроса, включая budgets; несовместимый cursor явно отклоняется. Все страницы восстанавливают весь результат объявленного запроса без потери parallel edges. Полнота по графу не является полнотой знания о repository. Если неделимая запись с обязательными metadata/stubs не помещается, возвращается `BLOCKED_OUTPUT_BUDGET` с действием для продолжения; бюджет меньше минимального terminal envelope отклоняется. Обрезанный payload и ложная полнота недопустимы.

#### Snapshot, freshness и refresh

Отдельно идентифицируются repository/worktree и режим наблюдения, HEAD при наличии, реально наблюдавшиеся paths/bytes с exclusions, schema/extractor/config/profile revisions и digest graph artifact. Пустой repository допускает HEAD null с причиной. Working-tree mode включает разрешённые dirty/untracked disk bytes и не выдаёт их за commit state. Fingerprint определяется inventory/bytes/scope, а не временем; graph output, временные кандидаты и derived views исключаются из собственного наблюдаемого inventory. Применимость extractor/config/profile проверяется отдельно. Digest относится ко всему сохранённому artifact, без самоссылки.

Offline query возвращает stored binding и `repository_currentness: NOT_RUN`. CURRENT устанавливается применимым результатом check, связанным с exact graph, repository/scope и наблюдавшимися inputs; успешный parse не проверяет свежесть. Check сравнивает inventory и bytes в объявленной области; Git diff — только подсказка. Одинаковый HEAD не исключает изменения файлов; новый HEAD не доказывает изменения семантики. CURRENT/STALE/UNKNOWN всегда относятся к scope, а не обещают полное знание или неизменность будущего состояния.

Refresh учитывает changed/new/deleted sources, затронутое evidence, условия разрешения связей, новых callers/consumers и изменения потенциальных targets/config даже при неизменном caller. Docs не считаются несущественными автоматически. Если область влияния не установлена, требуется более широкое разрешённое исследование либо явный pending refresh. Удалённые сущности и невалидные links исключаются из active topology с semantic diff.

Partial graph сохраняет целостные ссылки и прежние bindings с явными stale/pending/unknown областями. Это не один свежий snapshot разных версий. Parse/access/limit failure не повышает актуальность пропущенного участка. При неизменных source, scope, extractor/profile и graph state `NO_CHANGE` сохраняет persistent bytes и modification time; время новой проверки находится в ответе. Изменение только derived graph и его Git metadata не создаёт self-refresh loop.

#### Публикация, восстановление и пределы

С первого writer требуется целостная публикация: при сбое до публикации старый граф сохранён; после неё доступен целостный новый artifact. Конкурирующий writer не вызывает silent overwrite или потерю обновления; busy/conflict возвращает отказ без force takeover. Concurrent source changes не маскируются под согласованный fresh snapshot. Захват bytes без source lock доказывает только ограниченное наблюдение; последующая актуальность проверяется отдельно. Поддержанные OS/filesystem и проверенная crash-durability boundary объявляются явно.

Каждый worktree использует свою карту и binding; общая Git metadata не подменяет source delta. Перенос карты сохраняет прежний subject до проверки нового. После интеграции source проверяется результат интеграции; textual merge generated graphs не доказывает freshness. Tool не создаёт worktrees и не меняет refs/config.

Повреждённый граф не считается evidence. Recovery затрагивает только разрешённый output, не исправляет source и не удаляет чужие artifacts. Одинаковые inputs и revision детерминированного extractor/profile воспроизводят поддержанные structural semantic records. Batch claims восстанавливаются только с exact batch и bindings; вариативные model summaries не входят в обещание byte-identical rebuild. Types, направления, parallel edges, evidence, uncertainty и допустимые extension fields сохраняются. Повреждённая структура, duplicate IDs, dangling references и неподдержанная schema отклоняются; перенос отказывается от неподдержанного поля вместо молчаливой потери. Если выбран JSON, duplicate keys также отклоняются.

Scope имеет allowlist/exclusions; symlink/traversal не расширяет root. Secrets, credentials, Git internals и private areas не читаются для содержания по умолчанию; credential-bearing URLs не выводятся. Sources, docs, graph и batches — untrusted data. Допустимые metadata-эффекты чтения оговариваются профилем и не разрешают скрытые writes инструмента. Сеть и новая внешняя инфраструктура не требуются.

До pilot объявляются пределы source file, суммарного scope, graph/batch input, числа records, времени и памяти обработки. Output budget не заменяет processing budget. Превышение даёт явную причину/affected scope и сохраняет active graph; unsupported input не становится отсутствующей сущностью. Partial result допустим лишь с проверенной integrity и видимой coverage, иначе публикации нет. При аварийном завершении сохраняется явный failure без повреждения active graph. Непроверенная гарантия окружения не объявляется поддержанной.

Критерии проверки, последовательность срезов и решения перед реализацией принадлежат [Development](03_Development.md#graph-rag-verification). Storage пересматривается по измеренным расходам и удобству review, а не произвольному размеру или числу файлов.

<a id="graph-rag-module-contract"></a>

#### Граф RAG: композиция и подключение C-015/C-016

**Аннотация:** один модуль из FTR-017 находит контекст и объясняет отличия. Он читает разрешённые источники; сохранение результата является отдельной операцией. Это контракт будущего подключения к AOS, а не существующий API.

Контракт-кандидат `AOS_GRAPH_RAG_V1` объединяет retrieval и graph comparison в одной FTR-017; digest принятой revision связывается в runtime C-015 после принятия. Версии ниже — предлагаемые интерфейсы WHAT, не новый глобальный каталог. Используются `AOS_MODULE_CONNECTION_V1` и, для effects, `AOS_MODULE_MESSAGE_V1`; текущие C-009/C-010 и controller сохраняют смысл.

| Producer → interface/version → consumer | Mode и результат | Ownership и эффекты |
|---|---|---|
| Разрешённый host/caller → `graph_rag.find/v1` → caller или FTR-016 | DIRECT_READ: запрос/scope/mandatory/budget → source-faithful candidates, paths, reasons, coverage/freshness; поддержанный impact-профиль → раздельные зависимости/потребители и возможное влияние | FTR-017 владеет derived index, факты у source owner; in-memory поиск без persistent writes/network |
| Host/FTR-002 observations + применимые Product/Architecture refs → `graph_rag.compare/v1` → caller/FTR-005/reviewer | DIRECT_READ: exact Target/Observed/Mapping → Delta, witnesses, applicability и ограничения | Сравнение отдельно от top-k; не меняет ADR/дизайн/код, не дублирует FTR-021 authenticity |
| Host с task refs/FTR-016 → `graph_rag.context/v1` → FTR-016 → существующий host | DIRECT_READ: задача/mandatory sources → кандидаты контекста, missing inputs, relevant Delta, next-action recommendation | Итоговый Context Pack и session/task state принадлежат FTR-016; нет task selection/dispatch |
| Host/FTR-016 continuation refs → `graph_rag.check/v1` → caller/FTR-014/FTR-016 | DIRECT_READ: текущая применимость либо явно historical/unknown | Нет записи cache/pending registry; resume не replay внешней mutation |
| Caller с разрешённой задачей → `graph_rag.refresh/v1` или `graph_rag.save/v1` → FTR-010 dispatch → FTR-017 handler → caller/FTR-016 receipt | QUEUED_COMMAND C-016: создать/обновить derived destination либо сохранить reference bundle, подтвердить revision/result | Read scope, destination и operation binding объявлены; current authority перед эффектом, unknown publication требует reconciliation |

`refresh` включает первоначальный build при отсутствующем собственном output; чужой output не разрешает overwrite. `save` получает refs от owners, сохраняет свой bundle и не меняет task/decision/current. Имена операций — contract-кандидат, не команды нынешнего AOS. Standalone find/check не требуют выдуманной C-005; эффекты требуют C-005/C-006 и current registration/subject. N/A недопустим, если заявленный сценарий фактически пользуется интерфейсом.

Required boundaries: разрешённый reader/exclusion policy под FTR-009/019; registration/version routing FTR-010 с хранением bindings FTR-016; C-009 Result/C-010 provenance. Для context/resume required FTR-016, для persistence — scoped writer и C-016 controller. Они не объявляются существующими по AOS-3 source path. Optional: FTR-002 map, FTR-007 task candidates, FTR-021 аудит. Нет цикла «контекст нужен для создания индекса, индекс нужен для контекста»: FTR-016 поддерживает прямые источники, FTR-017 принимает явный corpus.

Локальная композиция не требует plugin loader/брокера/FTR-026. QUEUED_EVENT subscriptions в базовом профиле отсутствуют (`NOT_APPLICABLE`: нет background consumer); внешний результат передаёт caller при следующем check/context. Event-driven refresh потребует revision C-015/C-016. Очередь и finite limits принадлежат core, модуль не заводит свою. До эффекта профиль задаёт versions, handlers/generation, read/write/service scope, limits, supported target/host/OS и Error/Result binding. `RESULT/PARTIAL/NO_MATCHES/STALE/UNSUPPORTED` и Delta labels — payload semantics внутри C-009, не новые глобальные result enums.

<a id="graph-rag-impact-contract"></a>

#### Граф RAG: типизированное impact-представление — DRAFT

Владелец наблюдаемого поведения — [FTR-017](06_Features.md#graph-rag-impact-behavior). Это уточнение contract-кандидата C-015, а не новый Dependency Graph owner, API service или schema registry. Impact проходит через `graph_rag.find/v1`; `context/v1` может передать его FTR-016 с теми же основаниями и ограничениями. `compare/v1` сохраняет отдельный смысл Delta. До подключения фиксируются exact contract/payload revision, профиль и поддержка consumers: прежний find без impact сохраняет поисковую семантику; неподдержанный impact/profile/revision явно отклоняется, не подменяется обычным поиском. Имена `/v1` здесь не доказывают совместимость с работающим API.

Первый профиль-кандидат `DATA_CONTRACT_IMPACT_V1` внутри `LEXICAL_GRAPH_CONTEXT_V1` использует уже существующие PRODUCES/CONSUMES. Это ограниченный набор правил интерпретации, не пользовательский DSL. Другие семейства (например, статические IMPORTS или work prerequisites) не продолжают его closure без отдельно поддержанного правила и проверки. Общий словарь не переименовывается ради DIP.

| Отношение/ситуация | Допустимый результат профиля |
|---|---|
| `P --PRODUCES--> D <--CONSUMES-- C` | CONSUMES задаёт C → D; при изменении D C — прямой consumer candidate. При изменении P C — кандидат через derived dependency C → P только при совместимых identity/revision D, аспекте изменения и установленном provider binding потребителя. При обоих применимых основаниях upstream(C) содержит прямые D и P; одно PRODUCES не добавляет D → P |
| Несколько возможных P у D | Без exact provider binding нет зависимости C от каждого P; есть условный кандидат/неизвестный переход. Похожие label/type не создают join |
| `TESTS` / `VALIDATES`: проверка → subject | Обратное чтение даёт revalidation candidate, не продолжение dependency closure. DIP `VALIDATED_BY` — допустимое объяснение обратного вида, не новая хранимая стрелка |
| `BINDS_TO_CONTRACT` / `BINDS_TO_FEATURE` | Сопоставление и кандидат проверки соответствия при применимом изменении; не автоматически data-flow или утверждение «реализовано» |
| `REFERENCES`, Target/Observed Mapping | Навигация/сравнение; не проводят transitive impact. Unsupported relation явно ограничена, а если нужна запрошенному профилю — профиль запроса отклоняется |
| DIP `DEPENDS_ON` / `IMPLEMENTS` / `PERMITS` | Не импортируются как универсальные синонимы. Отдельная декларация требует явного поддержанного mapping смысла; PERMITS не участвует в dependency traversal и не выдаёт permission |

Исторический неизменяемый D не меняется задним числом от изменения P: без подходящего аспекта изменения propagation через этот результат недопустима. Пути разных Target/Observed views и семейств отношений не смешиваются. Product/Data/Execution — предметные проекции, а не замена оси Target/Observed; переход между ними требует конкретного поддержанного отношения.

Подтверждение каждого шага содержит исходные edge identities и направления, правило интерпретации, exact source revisions/locators, scope и применимость. Источник должен подтверждать именно вид отношения, не только наличие упомянутых объектов. В одной группе поддержки необходимы все её источники; между независимыми достаточными группами достаточно одной действительной. Потеря обязательного witness лишает силы эту группу, а не автоматически все остальные. Проверка source identity/hash не доказывает семантику или human acceptance; `REPORTED`/`SYNTHESIZED` остаются отдельными гипотезами.

Текущая обязательная цепочка содержит только шаги с подтверждёнными основаниями, применимой актуальностью, текущей фазой, обязательностью и истинными условиями. Условия FALSE исключают переход; OPTIONAL/FUTURE/UNKNOWN, material conflict, stale и evaluation error дают явно ограниченный результат вне этой цепочки. Ошибка одного независимого пути не отменяет другой действительный witness. Если профиль поддерживает отдельно запрошенный исследовательский путь за неизвестным переходом, все его продолжения остаются гипотезами. Accepted expectation и отличающееся observation сосуществуют как основания Delta; это не автоматически конфликт authority.

Результат различает число **исходных hops** и **dependency steps**: P → D ← C сохраняет два исходных hops; подтверждённый derived C → P считается одним dependency step. Прежние hop limits и output caps §10.1 не меняются. Профиль объявляет также конечные пределы dependency depth, посещений и рассмотренных связей; их исчерпание нельзя скрыть за pagination. Оба ограничения применяются, derived join не обходит raw-hop budget. Числа DIP 3/256/1024 не принимаются как новые defaults. Точные поддержанные limits относятся к profile binding, а структуры/алгоритм обхода и сериализацию выбирает исполнитель.

Для одинаковых immutable inputs/profile/policy выдача детерминирована: дистанция, endpoint identity, witness identity; root attribution и ограничения сохраняются. Циклы завершаются в пределах budgets без включения root в собственные зависимые sets. Result-only filter не удаляет нужный промежуточный D; traversal filter ограничивает сам исследованный путь и отражается в coverage. Access/exclusion policy применяется до обоих: скрытый intermediary нельзя раскрыть через path, ID, count, error или cursor.

Coverage сообщает четыре независимые границы: (1) inventory/прочитанный corpus с exclusions; (2) поддержанные predicate/profile и их область; (3) завершённость обхода, depth/resource cuts и неизвестные продолжения; (4) полноту представления результата/continuation. «Полно в объявленной модели отношений» допустимо только при достаточном corpus/predicate coverage и завершённом обходе без влияющих unresolved frontiers; это не `actual_program_impact_complete`. Полная последняя страница не делает частичное исследование полным. Недостаточный byte budget не удаляет существенные ограничения; действует прежний bounded error/continuation contract.

Current query требует разрешённого current capture либо достаточного подтверждения неизменности области; явно historical query не становится current evidence. Continuation/result binding включает capture/generation, subjects, view, profile/revision, условия и аспект изменения, filters/limits/access policy. Изменение binding требует нового запроса. Новые consumers и изменение resolution могут затронуть старые неизменённые sources; проверка только прежнего reverse index недостаточна. Полное перестроение bounded scope допустимо; selective refresh остаётся оптимизацией с проверкой эквивалентности, включая joins, coverage и прежние отрицательные выводы.

I/O и lifecycle остаются у существующего C-015/C-016: find/check не сохраняют cache, usage или hidden refresh; сохранение нового derived результата требует покрытого queued effect. При UPDATE consumers проверяют новую семантическую revision и cursor bindings; несовместимый старый результат не переинтерпретируется. DISABLE/REMOVE оставляют разрешённый direct flow с честной неполнотой impact, DELETE DATA требует отдельного scope и не удаляет owner facts/Evidence. FTR-021 не становится required query gate; собственную целостность входа проверяет FTR-017. [GR-DI01–10](03_Development.md#graph-rag-impact-verification) проверяют эти уточнения вместе с прежними GR-C01–10.

#### Граф RAG: corpus, поиск и сравнение

Capture связывает project/worktree/scope, фактически прочитанные bytes, revisions/locators, method/config и coverage. Fact class/role/authority и relevance раздельны: label/hash без применимого owner binding не принимают норму. Inventory учитывает additions/untracked; generated outputs исключены. Нет чтения закрытых материалов через graph paths или диагностику. Interval observation не объявляется atomic snapshot при произвольном writer.

Source-faithful fragment имеет revision и span; объяснение не цитата, chunk не отрывает существенное отрицание/ограничение. Exact ID/path сохраняется независимо от score. Dedup не сливает conflicting revisions/roles. Mandatory refs приходят от task/context routing, ranking их не отменяет. Budget измеряет весь ответ, включая metadata/errors; точный token limit требует заданного tokenizer. Невмещаемый mandatory/minimum envelope явно ограничивает или отклоняет запрос. Graph expansion сохраняет directed paths; seeds/hops/node/byte/time limits объявлены, truncation видима. Producer → artifact ← consumer требует двух связей: один hop не выдаётся за полный consumer impact.

Начальный extractor scope: Markdown/text, explicit JSON refs, Python definitions/direct imports при известном package mapping. Dynamic/ambiguous import не даёт runtime CALLS. Inferred/declared/extracted — происхождение, не authority. REFERENCES отображается в конкретное отношение/qualifier с проверенным смыслом, без молчаливых синонимов. Import сохраняет поддержанные identities/directions/provenance; unsupported явно ограничено/отклонено. Он не переносит AOS-3 lifecycle/readiness/topology в новый AOS.

Target — source-bound expectation с REQUIRED/FORBIDDEN/OPTIONAL/GUIDANCE и current/future applicability; Observed — конкретное наблюдение поддержанного свойства, runtime Evidence отдельно. Mapping явный однозначный либо конечный declared source-set; semantic similarity не identity. Initial predicates-кандидаты: наличие файла, явная ссылка, статический Python import, ссылка на результат проверки. Их wire names/format относятся к HOW; наблюдаемая семантика обязательна.

| Delta payload | Условие и предел вывода |
|---|---|
| MATCHED | Подтверждено конкретное сопоставимое свойство; не общий PASS |
| MISSING_EXPECTED / FORBIDDEN_PRESENT | Required/current отсутствие при достаточном отрицательном покрытии либо witness применимого запрета |
| PLANNED_DIFFERENCE / OPTIONAL_ABSENT | Future difference либо доказанное optional отсутствие; не текущая обязательная неисправность |
| UNMODELED | Не описано target; не дефект без запрета/исчерпывающей границы |
| UNVERIFIED / CONFLICT | Нет достаточных свежих/сопоставимых оснований либо material противоречие |

Coverage, freshness и applicability независимы. Наличие теста не execution Evidence; top-k/неполный parser не доказывают missing. Delta предлагает проверить observation/mapping, обратиться к design owner либо подготовить разрешённую correction; не исправляет owners и не запускает код.

#### Граф RAG: persistence, версии и lifecycle

Cache/index/maps принадлежат FTR-017 и восстановимы; task/decision/Evidence — своим owners. Writer публикует подтверждённую целостную revision; conflict/partial save не теряют предыдущую, повтор operation не удваивает учёт. Не доказанный atomic writer не объявляется доступным: safe single-writer либо отдельный candidate/conflict без смены shared pointer. Access policy ограничивает выдачу немедленно; очистка derived копий требует delete scope.

| Операция по §25.5 Development | Специфика Граф RAG |
|---|---|
| ADD/ENABLE | Проверить C-015/consumers/read route; разрешённые отсутствующие cache/config; register inactive → проверить direct/queued journeys → enable; conflict оставляет inactive |
| UPDATE | Приостановить affected calls/commands, reconcile in-flight; rebuild derived либо покрытая migration; sources/history сохраняются. Новая generation не принимает старые сообщения молча |
| DISABLE | Остановить новые business calls/enqueue; pending удержать с причиной, in-flight drain/reconcile; до этого не disabled. Direct-source flow FTR-016 доступен |
| REMOVE | Проверить consumers/fallback, disable/reconcile, снять handlers/bindings; удалить только разрешённые implementation paths; bundles/Evidence сохраняются и читаются независимым owner route |
| DELETE DATA | Отдельная authority на exact owned derived paths, проверка consumers/in-flight; disable/remove/TTL не дают delete permission. Unknown purge видим без раскрытия скрытого содержимого |

Unknown interface/schema/data revision даёт unsupported или поддержанное inspection; downgrade не принимает непроверенный формат, rollback только по доказанному пути. Bundles не единственный owner обязательных решений. [Lifecycle checks](03_Development.md#graph-rag-verification) обязательны для соответствующих операций; конкретная реализация и runtime support пока `NOT_RUN`.

<a id="ux-pages-contract"></a>

### 10.2. Repository UX Pages / FTR-032 — DRAFT contract

Применение C-002/C-009…C-012 и C-015/C-016 к
[FTR-032](06_Features.md#ftr-032-contract), по
[R2](05_Reference.md#ux-pages-r2-source). Это не новая схема всего ядра и не
разрешение запуска. UI/behavior и expected cases принадлежат Features,
пользовательский результат — [Product](01_Product.md#ux-pages-product).

**Owner и snapshot.** Одна логическая страница имеет один owning HTML с embedded
YAML: HTML/CSS задают представление, YAML — page-level behavior. Нет второго
редактируемого JSON/DOM owner этих фактов. Product/Feature/API/design sources
сохраняют собственные области authority; спецификацию API нельзя заменить mock.
Внешние C-011 решения и C-010 Evidence не хранятся как актуальная истина в page bytes.
Index, summaries, completeness и context packs — производные. Нормализация для
runtime тоже производна; форматы parser, helper layout и алгоритмы — HOW.

Snapshot связывает выбранные page identities/revisions, материальные source
versions, внешние records, converter и влияющие на вид/поведение runtime/assets.
Human и Engineering Surface читают один этот набор; preview-преобразование имеет
прослеживаемую связь с исходными bytes. Page identity включает весь HTML без
исключений status-панели. Изменение любых bytes создаёт другой subject, не переписывая
историю прежнего решения. Встроенная запись статуса — явно историческая; актуальность
решения определяется по C-011 и текущим inputs. Изменение runtime/CSS/converter
инвалидирует зависимые interactive/render conclusions; не означает, что человек
принял новую редакцию. Цена повторного review измеряется, semantic hash не вводится.

**Expected set и контекст.** Ожидаемые требования берутся из выбранных upstream
sources/acceptance до сопоставления с page links. Каждый имеет source, применимость,
mapping либо gap; duplicate mapping не увеличивает число требований. UNKNOWN
expected set не даёт знаменатель для «100%». Обоснованный NOT_APPLICABLE не равен
PASS. В Completeness Report ортогональны applicability
(`APPLICABLE / NOT_APPLICABLE / UNKNOWN`), coverage
(`COMPLETE / PARTIAL / MISSING / UNKNOWN`), verification.result и findings
(в том числе CONFLICT). Первые поля — proposal отчёта, не статусы lifecycle;
verification.result использует только [единый Result Contract](#technical-result-contract).

Journey определяется выбранным Product/Feature scenario; карта лишь ссылается на
page/state/action и entry/exit. Циклические ссылки A↔B не расширяют pack бесконечно:
точная версия участника включается один раз; способ обхода выбирает агент.
Обязательные участки/источники реально доступны в разрешённой среде либо включены
в разрешённый pack. Неопределённый required target — gap, а не справочная ссылка;
sidebar не требует экспорта всего проекта. Источники вне data scope не копируются.

**Реальные стыки / кандидат C-015.** Один модуль содержит FTR-032; иные FTR —
потребляемые возможности, не новое объединение. Имена операций ниже обозначают
смысл контрактов, exact supported schema/version определяются в DS-O03.

| Producer → consumer | Передаваемое содержание и допустимое действие | Отказ / владелец |
|---|---|---|
| Product/Feature sources (FTR-003) и разрешённые page/API/design owners → FTR-032 | Exact выбранные требования, UX scope, ограничения и view model; optional ADR/patterns читаются только при необходимости | Отсутствующий обязательный вход даёт scoped gap. FTR-032 не выбирает product truth; библиотека 022 и индекс 017 не обязательны |
| FTR-032 → CHECK / Engineering Surface | Нормализованное чтение контракта, expected set, gaps, subject-bound observations; DIRECT_READ не меняет page или status | Runtime не требуется для разбора. Неподдержанная schema явно отклоняется; нет silent fallback на пример D02/D03 |
| FTR-032 → Human Surface / host preview adapter | Проверенный snapshot и scope ограниченной симуляции; запуск только в отдельно проверенной среде с покрытыми effects | Недоказанный preview не запускается; безопасный разбор/производная статическая визуализация остаются доступны. Host не получает права из HTML |
| FTR-032 → генерация/коррекция pages, BUILD_INDEX или запись pack | QUEUED_COMMAND при записи с C-005/current authority и C-016; before/after subject, owned outputs и результат C-008/C-010 | Память/доставка через ядро 016/010, допуск 009/019; нет скрытой записи из CHECK. Повтор/неизвестный effect идёт на reconciliation 014 |
| Человек через действующий trusted channel → FTR-012/C-011 → FTR-032 | Exact показанный review subject, scope/исключения, explicit decision; результат проверенной записи читается для нового index | Generated viewer/симуляция не issuer и не writer. Missing adapter, stale subject и ошибка записи различимы. Неизвестный исход записи сначала выясняется через владельца record, не создаётся второй decision |
| FTR-032 EXPORT_CONTEXT → внешний coding agent в FRONTEND / INTEGRATION task | Task-scoped page contract, применимые sources, checks/Evidence, decision scope и gaps. DIRECT_READ для выдачи; сохранение pack — отдельный covered write | EXPORT_CONTEXT не исполняет следующую task и не даёт authority. Перед потреблением сверяются actual inputs/decisions; unresolved refs не считаются достаточным заданием |

Требования FRONTEND/INTEGRATION — в dossier, admission/порядок цикла — Development.
Необязательный writable decision adapter не является предпосылкой создания viewer;
внешний доверенный канал нужен для обещанного реального принятия. Без него можно
подготовить review, но нельзя закрыть весь пользовательский путь. Нет зависимости
от ещё не созданного index при первом чтении owners; index обновляется по запросу
агента, не watcher. observed_at/набор сборки видны; возраст файла не доказывает drift.

**Preview boundary.** Generated content не получает filesystem handles, agent bridge,
decision writer, credentials, shell, сетевые effects либо доступ к outer review
controls. Pinned viewer/runtime и authored HTML/CSS/YAML различаются по доверию.
Запрет authored iframe не запрещает trusted viewer использовать проверенную
изолированную поверхность. Выбор parser/profile, DOM/CSS/URL limits и средств
изоляции — Engineering Design в пределах этих guarantees; произвольный JS/eval,
plugin hooks и скрытая сеть не являются fallback. CSP — дополнительная защита;
`sandbox` нельзя доставить через CSP meta, и одна CSP не доказывает изоляцию
([E01](05_Reference.md#ux-pages-r2-source)). До DS-O04 интерактивный запуск NOT_RUN.

**Сохранение/обновление.** Page update проверяет exact base до замены, сохраняет
восстановимый принятый subject, не затирает competing edit. История C-010/C-011 и
task ledger принадлежат прежним owners; временный simulation state не durable Evidence.
При потере подтверждения сначала сверить actual effects, затем допустимый повтор
по C-012/C-016. Успешный decision и failed rebuild index — разные outcomes: решение
сохранено, projection требует восстановления. Нельзя восстановить потерянный C-011
из badge. Представления воспроизводимы из pages, sources/records и версий инструментов,
а не только HTML. Semantic diff объясняет проверенные before/after; не владеет фактами.

Для ADD/ENABLE/UPDATE/DISABLE/REMOVE применяется Development §25.5: проверить
связанные consumers/версии, reconcile pending/in-flight; без модуля сохраняются
pages, accepted snapshots и внешние records, ядро может читать их в read scope.
Обновлённый runtime/converter получает новую binding; старый pack не становится
current автоматически. REMOVE implementation не удаляет пользовательские данные;
DELETE DATA — отдельная authority. Сам модуль не имеет scheduler/completion owner.

<a id="rbac-abac-contract"></a>

### 10.3. rbac abac / FTR-031 — прикладной DRAFT contract

[Product](01_Product.md#rbac-abac-product) и [FTR-031](06_Features.md#ftr-031-contract)
задают WHAT минимального `2.0-candidate`. Это компонент в процессе приложения,
не новый controller/PDP-сервис AOS. Public contracts ниже описывают логические
границы, не обязательные имена функций или serialization.

**Владение.** Host владеет identity, актуальными role assignments, tenant/project
и object authorization, доменными данными, бизнес-переходами и каталогом полей.
Каталог задаёт stable field IDs, типы, server mapping, ceilings допустимых
role/field/action, обязательные условия и security attribute bindings.
Единственный owner настроек — активная AccessModel в хранилище host: grants и
версионная история. Каталог/роль/admin permission не редактируются этой моделью.
UI, YAML export, документация и preview — производные; шаблон AOS не перезаписывает
активные настройки. Одна active model относится к точно определённой области.

**Два вида полномочий.** AccessDecision содержит request_id, policy_revision,
scope, action, field ID, ALLOW/DENY и безопасную причину. Эти два значения —
решение о прикладном доступе, не расширение technical enum C-009 и не C-011.
DRAFT/ACTIVE/RETIRED также относятся только к AccessModel. MANAGE_FIELD_ACCESS
выдаётся приложением; scoped применение модели не требует development approval
на каждую настройку. Coding agent по-прежнему действует по Core и C-005/C-006;
FTR-019 не заменяет object/field authorization приложения и наоборот.

| Логическая точка / producer → consumer | Необходимое содержание и результат | Ошибка / граница |
|---|---|---|
| resolve_subject: identity/role services host → evaluator/admin | Проверенная identity, текущие роли и их scope; доверенность и актуальность проверяются сервером | Клиентская роль/tenant не источник; missing/stale вход блокирует затронутое решение |
| authorize_object: domain access host → field evaluator | Доступ к записи/области для точной READ/CREATE/UPDATE операции; pre-state или проверенный create context | Field grant только сужает разрешение; CREATE не зависит автоматически от object.READ |
| field_catalog: schema/domain owner → editor/evaluator | Совместимые IDs/descriptors/server mapping, editable ceilings и подключённые attributes; правила NOT_LOCKED и server-owned полей | Неизвестная/нерассмотренная привязка закрыта; неподключённый шаблон недоступен; ошибка неиспользуемого атрибута не блокирует другие решения |
| project_read: evaluator + row scope → serializer/UI | Индивидуальная разрешённая проекция до выдачи detail/list/create/update response | Скрытие в браузере не защита; response metadata имеет отдельный фиксированный контракт и не дублирует запрещённые значения |
| validate_write: evaluator → domain mutation host | Решение по всему payload/точный allowlist до binding и effects, затем собственная business validation host | Одно запрещённое/неизвестное поле — отказ всего запроса; null/старое значение не исключение |
| policy_store: уполномоченная admin operation → store/evaluator | Active revision, история, сравнение expected revision, единая публикация новой версии/pointer/change event | Подтверждённый отказ проверки/публикации оставляет прежнюю active; потеря ответа не доказывает отказ, unknown outcome выясняется до повтора |
| admin_access: host admin authorization → editor/apply/rollback | MANAGE_FIELD_ACCESS в конкретной области, проверяется заново при mutation; bootstrap/recovery у host | Модель не назначает admin/роли, не меняет ceilings и чужую область; отсутствие admin READ не означает право чтения значений |
| preview: synthetic fixture + model → тот же evaluator → admin explanation | Решение/объяснение для искусственного контекста, без выполнения action/impersonation | Результат не переносится как permit, draft не активирован, не-admin не получает policy dump |

**Режим и совместимость обмена (§25.4, шаги 3–4).** Состав модуля — только
FTR-031: editor/preview, evaluator и host adapter, без нового объединения FTR.
В минимальном candidate вызовы идут напрямую через сервер host с ответом на
текущий запрос. Это прикладной request/response, не режим DIRECT_READ C-015:
write/apply/rollback могут иметь эффекты без очереди AOS. Собственных queued
commands, subscribers и scheduler здесь нет; change event — сохраняемый факт
в policy store, а не обещание доставки C-016. Если host уже имеет фоновые пути,
они остаются в inventory и проходят enforcement либо закрываются.

Предоставляемые возможности — field decision, read projection, write allowlist,
admin apply/rollback и synthetic preview. Обязательные producers — семь host
точек таблицы выше; фактические consumers — editor, serializer, domain mutation
и policy store. FTR-032 — необязательный инструмент подготовки UX; отсутствие
этого инструмента не отменяет обязательный editor внутри готового приложения.
Ни один consumer не читает чужое storage в обход host interface.

До первого зависимого вызова binding сопоставляет поддержанные версии public
contract модуля, формата AccessModel, каталога/security bindings и каждого host
adapter/consumer. Policy revision обозначает конкретные правила, не версию
схемы. Неизвестный или несовместимый набор блокирует затронутый путь до effects
и выдачи данных; старое имя поля/старый PASS не доказывают совместимость.
Поддержанный старый reader допускается по явно проверенному mapping, иначе —
явный отказ без silent conversion. Конкретные номера, encoding и способ
проверки выбираются при Engineering Design; migration сохраняет исходные данные
и не назначается автоматически. Изменение binding требует проверки его реальных
consumers, а не всего каталога AOS.

Граница effects: evaluator/preview сами не меняют доменные данные, active policy,
роль или authority; project_read выдаёт только разрешённые значения. Domain
mutation принадлежит host и допускается после validate_write и business checks.
Apply/rollback меняют только разрешённую модель, её историю/pointer/change event;
они не отменяют уже совершённые доменные writes. Собственное сетевое обращение,
новый provider или доступ к данным за scope этим подключением не предоставлены.
Audit host, если он требуется приложению, остаётся отдельным объявленным эффектом.

**Application binding перед зависимой реализацией.** Связать exact ТЗ/бизнес-сценарии,
объект и область, роли/админ-делегацию, версию каталога/модели/адаптера, supported
field/action/condition и правила доступности security inputs. Перечислить реальные
producers и все пути к защищённой сущности: serializers, detail/list, writes и их
responses, filter/sort/search/export/reports/aggregate/bulk/subscriptions, aliases,
background jobs и иные имеющиеся endpoints. Для каждого — проверяемая точка
enforcement либо закрытый путь. Это ограниченная карта одного application binding,
не новая глобальная registry и не поиск всех возможных пар FTR.

Тот же binding задаёт domain defaults/creation context, pre-state и границу
проверки/commit, response metadata, безопасные причины отказа, наблюдаемое
восстановление и обязательные проверки по [Development](03_Development.md#rbac-abac-verification).
При UPDATE host связывает policy/record version с фактическим применением; изменение
до commit требует fresh оценки либо безопасного отказа. При CREATE решение использует
серверные значения до client binding. SET_ON_CREATE без READ не запрещает создание;
успешность записи сообщается без выдачи запрещённых полей по согласованному response
contract. Неподдержанный режим не включается. Механизм транзакций, хранения и
синхронизации — HOW; JSON Schema не доказывает эти гарантии.

**Версии и восстановление.** Apply сверяет current admin permission, draft/catalog
и expected_active_revision; модель, active pointer и change event публикуются
совместно либо не публикуются. Event содержит actor/scope/старую и новую revision/
изменение правил, без значений защищённых полей. При потерянном ответе сначала
сопоставить исходный запрос, фактическую active revision, историю и event. Доказанную
активацию не повторять; неизвестность не считать отказом и не компенсировать
слепым rollback. Повтор после доказанного отсутствия эффекта заново проверяет
authority/revision; конкурирующее новое состояние не затирается. Способ корреляции
и атомарности выбирается host implementation, новый сервис журнала не требуется.

Для CREATE/UPDATE доменной записи потерянный ответ также не означает отсутствие
эффекта. Host связывает исходную операцию с наблюдаемым исходом/идентичностью
записи и проверяет его до повтора; модуль не создаёт вторую запись и не повторяет
write по одному timeout. Если исход недоступен в текущих полномочиях, повтор
этой операции остаётся заблокированным до разрешённого выяснения состояния.
Доказанный успех сообщается без выдачи запрещённых полей; доказанное отсутствие
эффекта допускает новый вызов с актуальными policy, identity и pre-state.
Способ корреляции/защиты от повторов задаёт host; отмена UI-запроса не доказывает
отмену серверной операции. Это обязательство application binding, не использование
C-012 AOS как runtime-журнала прикладных записей.

Rollback — новая revision из старых правил с новой проверкой прав/совместимости.
Межзапросного ALLOW/DENY cache в candidate нет; каждый новый запрос использует
активную policy и актуальные роли. Новое поле UNREVIEWED/закрыто; совпадение имени
не доказывает совместимость rename/type/source. Неизменённые поля работают только
при подтверждённых descriptors и используемых attributes. Старые explicit-deny
политики не импортируются автоматически. Поддержка версий фиксируется в binding;
миграция и изменение бизнес-смысла требуют отдельного покрытого действия.

**Lifecycle компонента.** Гарантии [§25.5](03_Development.md#module-connection-lifecycle)
применяются к host binding, без обязательной очереди/registry AOS. Для операций
над implementation действует authority задачи разработки; MANAGE_FIELD_ACCESS
разрешает только прикладное управление правилами и не разрешает uninstall/migration.

| Операция | Допуск, переход и проверяемый выход |
|---|---|
| ADD / ENABLE | Подготовить host identity/object/catalog/store и проверить совместимые consumers до открытия защищённых путей. До пригодной policy доступ закрыт; partial setup остаётся закрытым и восстановимым, не затирает существующие данные. UI может создаваться позже enforcement, но обязателен к общему результату |
| UPDATE | Прекратить новые вызовы затронутого binding; учесть начатые read/write/apply/rollback. Дождаться завершения или подтвердить отмену, неизвестные effects выяснить до переключения. Только покрытая migration, затем проверка новых consumers перед открытием; старые вызовы не перенаправляются молча на новую семантику |
| DISABLE | Отключение editor не выключает enforcement. При отключении enforcement сначала закрыть новые зависимые запросы, затем завершить/reconcile начатые операции; draining не выдаётся за disabled. Непригодная policy не открывает обход; inspection сохранённых данных требует соответствующих host прав |
| REMOVE IMPLEMENTATION | Сначала disable/reconcile и проверка всех consumers. Обязательный consumer без проверенной замены блокирует удаление; закрытие endpoint защищает данные, но не выполняет обязательную функцию приложения. Исключить её можно только изменением согласованного scope. Убрать только owned bindings/implementation в разрешённой задаче, сохранить данные/историю; re-install не повторяет старые effects |
| DELETE DATA | Отдельно определить exact datasets/owners, ограничения хранения, backup/recovery, зависимых consumers, незавершённые операции и delete authority по §25.5. Ни remove, ни admin apply, ни истечение срока хранения сами не разрешают удаление |

FTR-032 может при выбранном UX-сценарии описывать UI этих правил, но не является
required runtime dependency и не владеет AccessModel. Принятие UX-макета C-011
не применяет policy; прикладное apply не принимает модель FTR-031 или код AOS.
FTR-016/025 не становятся хранилищами runtime policy/change event: это host owners.
Проверка/разработка самого компонента следует общему coding workflow; память и
completion этого процесса остаются у существующего controller.

<a id="recovery-contract"></a>

### 10.4. Recovery / FTR-033 — DRAFT contract v0.2

[Product](01_Product.md#recovery-product) задаёт результат,
[Features](06_Features.md#ftr-033-contract) — поведение и REC cases. Recovery
владеет смыслом Intake/Assessment, сравнением стратегий и составом next context.
Он не владеет source project facts вместо их источников, человеческим решением,
общим controller state, scanner, executor или новым хранилищем Project Memory.
Состав — одна FTR-033 с внешними dependencies, без присоединения их FTR к модулю.

**Subject, данные и чтение.** Один primary root, scope/coverage/exclusions,
observed_at и manifest прочитанных bytes. Git binding включает доступные HEAD,
branch, worktree/index и staged/unstaged/untracked; unborn/detached значения
nullable с причиной. Directory использует manifest без git init. В manifest:
relative path, entry type, digest прочитанного regular file с алгоритмом, значимые
mode flags и link target как данные. Nested/submodule/внешние links не обходятся
автоматически; непрочитанные/binary/large/secret-excluded части явно перечислены.
Missing digest не заменяется фиктивным. Чтение по очереди не доказывает атомарный
snapshot: backend даёт свою гарантию либо проверку согласованности с пределами.
Drift не смешивается в один subject; только affected claims STALE/UNKNOWN.

Source tree/VCS не изменяются; отчёт/continuity пишутся только в разрешённый
external workspace. Остальная среда/network не разрешены этим фактом. Reader
не исполняет target code/hooks/helpers/config instructions. Before/after equality
доказывает лишь конечное равенство; zero-write claim требует наблюдаемой boundary
и проверенных возможностей reader. Непроверенная часть NOT_RUN, не safe-by-name.
Known credential stores/keys/secret .env/production datasets исключены; случайный
секрет не попадает в prompt/output/Details. Разрешён redacted finding. Перенос
пакета использует разрешённые relative locators/attachments, без raw credentials
и раскрытия sensitive absolute root. Неизвестная data/provider boundary блокирует
затронутое чтение/передачу, не безопасный intake.

**Records: один семантический контракт, не executable schema.** Text/ID непустые,
ID уникальны в session; Ref связывает id/revision/locator и digest либо null с
ограничением. Digest именует алгоритм; Instant имеет timezone, неизвестное время
не заменяется временем анализа. Claim/Evidence/Decision/Subject/Action refs
типизированы. [] означает известное отсутствие, UNKNOWN — отдельный claim.
Unknown enum, duplicate ID, missing required/незадокументированное поле или неверный
тип дают contract error; boolean не revision/counter. Формат и parser — HOW,
расширение требует явной schema revision, без угадывания принимающей стороной.

| Record / логическая группа | Обязательное содержание и ограничения |
|---|---|
| SubjectIdentity | id, kind GIT_WORKTREE/DIRECTORY_SNAPSHOT, root_binding, observed_at, scope_paths, manifest_ref, coverage, freshness, limitations; только для Git: nullable head/branch, worktree_state, nullable index_binding |
| Claim | id, statement, Core fact_class, source_refs, nullable subject_ref/observed_at, scope, limitations. OBSERVED_AT_SNAPSHOT требует subject/Evidence; HUMAN_ACCEPTED_FACT — подлинного exact decision, не названия файла |
| CheckRecord | id, purpose, nullable required_for_action, method_ref, subject_ref, execution RUN/NOT_RUN, C-009 result, evidence_refs, limitations. NOT_RUN → result NOT_RUN; RUN требует actual outcome/Evidence. Imported run сохраняет старый subject/time, не объявляется исполнением текущей сессии |
| Finding | id, symptom_claim_refs, nullable root_cause_claim_ref, affected_action, impact, resolution_step, evidence_refs; причина hypothesis, пока метод не различил альтернативы |
| DispositionCandidate | id, disposition из Features, scope, rationale_claim_refs, benefits, costs_and_risks, unknowns, reversal_conditions; не selection, количественная оценка только с методом/assumptions |
| DecisionBinding | decision_ref, subject_refs, scope, effect, origin_ref, actor, decided_at; projection проверенного C-011, не новый writer человеческой authority |
| NextAction | id, purpose, target_stage PLAN, allowed_analysis_scope, out_of_scope, input_refs, completion_conditions, negative_checks, stop_conditions, unresolved_inputs |
| A — Intake | schema_version/recovery_id/revision/created_at; intent_ref C-001; mode ADOPT/RECOVER; subject_request (не verified subject); nullable decision_owner_ref/output_workspace_ref; read_scope; data_boundary с explicit unknown; согласованный analysis_budget с единицей/значением; initial_unknowns ClaimRefs |
| B — Assessment | schema_version/recovery_id/revision, intake_ref, subject_ref, coverage, claims/checks/findings/candidate_dispositions, nullable recommended_candidate_id, limitations, next_action, created_at. Families product_state/technical_state/behavior_state/delivery_state/source_authority_map имеют claim_refs и limitations |
| C — Decision + Handoff | schema_version/recovery_id/revision, assessment_ref, recovery_state, nullable decision_binding/MMB/first_recovery_slice, handoff, created_at. До human event — DRAFT с decision null. Handoff: target_stage PLAN, input_refs, must_recheck_on_resume, missing_contracts, execution_authorization_ref null, git_authorization_ref null, nullable receipt_ref |

B различает observed/desired/protected behavior; последние ссылаются на принятый
источник либо proposal/unknown. Build/run/test entrypoints — claims о declarations,
исполнение только в CheckRecord. last_known_good требует subject, критерий good,
Evidence/limits либо UNKNOWN; tag не доказывает restore. data_state отдельно
описывает сведения о DB/migrations/services/backup, не выводится из Git.
Без verified subject сохраняется Intake/явно incomplete draft, а не фиктивно
полный B. Partial coverage допустима при пригодном ограниченном subject.
Упаковка C не создаёт новых фактов. Receipt — не C-011 и не transport ack.

**Привязка выбора к C-011.** Recovery dispositions не расширяют enum человеческих
решений ACCEPT/NEEDS_CHANGES/REJECT/DEFER. Перед подтверждением показать exact
Assessment revision, выбранный DispositionCandidate и NextAction с её scope/stage.
DecisionBinding.effect сохраняет ссылки на этот выбор и next objective из
проверенного C-011; это projection, не inference по recommended_candidate_id.
Общее ACCEPT отчёта с несколькими вариантами без определённого выбора не допускает
PREPARING_HANDOFF. Уже принятое exact направление/задание не спрашивать снова;
смена рекомендации агента сама не меняет выбор человека. DEFER/REJECT отражают
паузу/отказ продолжать, но не разрешают архивирование, deletion или исполнение.

**Получение пакета и начало работы — разные события.** Receipt связывает свою
identity/origin, receiving workflow/consumer, exact package revision/digest,
NextAction ref/stage PLAN и результат проверки доступности required input refs
в разрешённой среде receiver. Его producer — принимающая сторона, не отправитель
Recovery. C-016 delivery ack без такого результата не становится receipt.
Неверный subject/receiver, missing input или непроверенный origin оставляют
HANDOFF_PREPARED с причиной; receipt старой редакции не относится к новой.
Подтверждение получения не создаёт автоматически новую C-005, ACTIVE C-012 либо
запуск PLAN. Принимающая FTR-006 отдельно формирует task по текущему поручению;
если задача уже существует, связывает пакет с ней без повторного создания.
Один logical handoff operation при redelivery возвращает прежний receipt;
тот же operation с иным payload отклоняется по C-016. Это не global exactly-once
обещание, а проверяемая привязка конкретной доставки/приёмки.

<a id="recovery-mmb"></a>

**Minimum Managed Baseline — единственное определение.** Versioned evidence-bound
вход одной NextAction, не global SoT/backup/authorization. Required fields:

| Поля | Смысл |
|---|---|
| subject_ref, assessment_ref, goal_ref | Exact subject/scope, immutable assessment и подтверждённая цель next task |
| decision_refs, source_refs | Применимые решения направления/scope/protected behavior; минимальные разрешённые inputs с fact class/назначением |
| critical_flow_refs, entrypoint_claim_refs, check_refs | Flows/entrypoints либо explicit UNKNOWN для задачи уточнения; actual и необходимые NOT_RUN проверки |
| preservation_refs, blocker_refs, unknown_refs | Пользовательские изменения, protected behavior/data, ограничения и affected actions |
| last_known_good_claim_ref | Scoped подтверждение либо explicit UNKNOWN |
| next_action_ref, recheck_refs | Одна NextAction и mutable facts для проверки до применения пакета |

Условие достаточности — Features: missing input может быть предметом безопасного
PLAN, но не исчезает из required inputs другой задачи. Нет blanket acceptance
каждого наблюдения. Если направление/next objective уже подтверждены, повторный
Human Gate неизменного scope не нужен.

**Runtime composition C-015/C-016.** В отличие от прикладного FTR-031, Recovery —
модуль самого AOS. C-015 связывает recovery revision/FTR-033 с exact accepted
contract, handler/instance/generation, версиями records/interfaces, capabilities,
support envelope и finite C-016 profile; это описание будущего подключения,
не найденные APIs и не разрешение активации. FTR-010 регистрирует/доставляет,
FTR-016 сохраняет, FTR-009/019 проверяют допуск. Предлагаемые operation names ниже
логические; точная command grammar/transport — Engineering Design.

| Producer → consumer / contract | Когда required, режим и fallback |
|---|---|
| FTR-001 / C-001 → Recovery intake | Intent всегда нужен; actual user input с provenance допустим вручную, не invented owner decision |
| FTR-009/019 / C-007 и текущая C-006 → разрешённый collector FTR-002 → Recovery | До instrumented read: subject/capability/scope/authority. Нет safe reader → intake/import bounded evidence, не обход на target helper |
| FTR-002/C-010 и принятые C-002/C-003 sources → Assessment | Read доступных observations/desired/protected refs; unsupported часть UNKNOWN, не собственный второй scanner |
| FTR-011/012 / C-009/C-010/C-011 → Recovery | Check outcomes, Evidence/origin и exact decision. Manual records допустимы только с проверяемым origin; иначе authority-dependent transition blocked |
| Recovery → FTR-008 и читатель пакета | DIRECT_READ сохранённого summary/context: registration/version/scope checks, без скрытого persistence/следования refs за data boundary |
| Recovery → FTR-016 через FTR-010 / C-016 → saved revision | QUEUED_COMMAND только по отдельному допустимому task/stage binding записи external output, не из read-only PLAN. Один operation/subject/expected output base/authority binding; partial/duplicate/error по общему transport |
| Recovery → FTR-003/006, FTR-016 / C-016,C-012 | QUEUED_COMMAND разрешённой передачи exact package с отдельным effectful binding; receiver проверяет refs/revision и возвращает receipt. C-012 текущей задачи сохраняет observation; новая задача не создаётся по ack |
| FTR-014 + controller → восстановление записи/сессии | При unknown effect/interruption, до retry; последний complete artifact остаётся читаемым. Нет другого scheduler/current-state owner |
| FTR-004 / C-013; FTR-005 / C-004; FTR-010/011/013 | Только отдельные optional install/architecture support/последующие execution-validation tasks. Не prerequisites static assessment; они не запускаются по рекомендации Recovery |

Recovery читает текущие C-005/C-006 своей задачи, но не заполняет полномочия
будущего ремонта из них. Null execution/Git refs в handoff относятся к следующей
работе; текущий разрешённый output persistence имеет собственный проверенный
binding. Нет разрешения на output → transient summary, durable handoff не заявлен.
DIRECT_READ не пишет product state; effectful requests идут через существующий
controller/admission. Служебный COMMAND не получает C-006A с lifecycle PLAN:
при использовании этого маршрута требуется действующая задача разрешённого
persistence/delivery с допустимой EXECUTE стадией и fresh envelope, ограниченным
только external output/receipt. Это не EXECUTE ремонта и не разрешение target code.
Recovery не переводит standalone PLAN в EXECUTE автоматически и не запускает
служебную задачу по собственному решению. Если такого binding нет, возможны
подготовка/transient output или разрешённое документальное сохранение по §9
Development; они не объявляются выполненным C-016 journey. Exact профиль должен
назвать фактически поддержанный путь. Отдельно выданное разрешение на одну такую
задачу не требует повторного human approval каждого её штатного сохранения.
QUEUED_EVENT нужен только при объявленном реальном subscriber;
новые подписчики и обязательный event bus не добавляются этим candidate.

**Durability/resume.** External sidecar — место размещения records, не новый owner
controller state. Complete revision публикуется атомарно/принятым primitive через
FTR-016; partial не заменяет последнюю полную, tmp не единственное Evidence.
До публикации writer проверяет expected base внешнего output: конкурирующая
revision не затирается, stale writer получает conflict/reconciliation. Source
subject и output revision — разные identities; неизменный HEAD source не
доказывает неизменность sidecar. При lost response сопоставить operation, сохранённые bytes/base, delivery state и
receipt до retry; не дублировать C-011. Mutable inputs recheck перед handoff/resume,
старый business intent сохраняется, но не даёт authority новым effects. После
передачи ongoing state принадлежит C-012 workflow; Recovery records historical,
не второй editable current. Receiver unavailable оставляет prepared без receipt.
Sensitive retention/deletion boundary определяют до записи, путь/serializer — HOW.

**Lifecycle §25.5.** ADD/ENABLE требует совместимого C-015, объявленных capabilities,
разрешённых config/storage и проверенных journeys допускаемых операций до включения;
partial registration остаётся inactive/recoverable. Reader/writer/receiver required
по соответствующей операции таблицы: нет receiver — запрещён HANDED_OFF, но возможен
Assessment/prepared; нет writer — только разрешённый transient результат. Не объявлять
полную capability по одному degraded пути. Установка самого модуля в AOS не означает installation
в обследуемый source root. UPDATE прекращает affected delivery, reconcile in-flight,
сохраняет старые records/messages и применяет лишь покрытую migration; unknown version
не получает silent conversion. DISABLE закрывает новые вызовы/enqueue, pending удерживает
с причиной, in-flight выясняет до disabled. Saved packages читаются разрешённым
независимым reader. REMOVE требует disable/reconciliation и замены required consumers,
снимает только owned bindings/code; пакеты, human decisions и source не удаляются.
Re-install не повторяет старые сообщения. DELETE DATA — отдельно по §25.5 с exact
datasets/owners/retention/backup/consumers/authority; удаление sidecar не меняет source.

Нельзя создать цикл recovery → install в target → recovery. Manual review внешнего
пакета возможен до runtime-модуля, но не доказывает C-015 integration. Проверки —
[Development](03_Development.md#recovery-verification), inputs/profile UNKNOWN.

## 11. Адаптеры агентов

Один common rule source поддерживает thin adapters для Codex, Claude Code, Cursor, ChatGPT и других сред. Adapters не расширяют permissions, используют repository-relative links и должны быть generated или drift-checked.

Для сценария интервью адаптер читает и обновляет общий переносимый контракт
состояния, а не хранит продолжение только в памяти чата. Контракт содержит exact
revision черновика, текущий вопрос, отвеченные темы, открытые вопросы, конфликты,
число ответов после последней сводки, source bindings и статусы предложений.
Markdown остаётся читаемым человеком источником; машиночитаемое представление
является проверяемой производной и может быть пересобрано.

Conformance каждой агентной среды проверяется новым сеансом: он открывает файлы
проекта, правильно определяет ближайший неотвеченный вопрос, не повторяет
закрытые темы, сохраняет маркировку решений и рекомендаций и не переносит
утверждение на новую редакцию. Успех одного адаптера не доказывает совместимость
другого; общий формат без такого journey доказывает только статическую переносимость.

## 12. Топология репозитория

Current direction: modular monorepo first. Split допускается при реальной team/release/compliance/deployment/ownership boundary. Cross-repo sync не обходит human authority.

## 13. Паттерны реализации

1. `REIMPLEMENT_FROM_CONTRACT`.
2. Manual cycle before automation.
3. Small vertical slice before platform.
4. Pure analysis separated from mutation.
5. Preview binds to apply.
6. Writes atomic or journaled.
7. Candidate frozen before validation.
8. Validation subject isolated when material.
9. Exact baseline/candidate binding.
10. Clean/isolated worktree.
11. Strict adapter before parser replacement.
12. Sunset only after migration Evidence.
13. Derived indexes rebuildable.
14. External content untrusted.
15. Optional modules fail in isolation.

## 14. Модель failures и recovery

Каждый write-capable component определяет failure before first write, partial-write detection, transaction/journal, reconciliation, idempotent retry, cancellation, recovery package, rollback boundary и post-recovery validation.

Automatic retry запрещён, если failure меняет scope, identity, permissions или human decision requirements.

Для failure внутри действующей complete-task authority применяется
многоступенчатая read-first диагностика: bind failure/observer → локальная
причина → различение гипотез → соседняя causal boundary → environment/system →
trajectory/architecture review. Если причина не найдена, Evidence совместимо с
несколькими существенными причинами, observer ненадёжен или confidence
недостаточен для обратимой correction, диагностика обязана расшириться на
следующий уровень без расширения mutation/access authority.

Stable failure signature продолжает достигнутый diagnostic level после
correction; новая signature начинает новый record с первого уровня, не
сбрасывая общий ledger. Повтор unchanged check, equivalent patch и explanation
без information gain не являются progress. Исчерпание run allowance создаёт
resumable pause; только human-defined task hard limit либо доказанная
невозможность может завершить незакрытую task с failure.

## 15. Минимальная модель реализации — INFERENCE

```text
aos_core/{contracts,authority,status,project_state,features}
aos_product/{intake,discovery,specification,review,memory}
aos_factory/{task_brief,preflight,execution,validation,handoff}
aos_cli/{intake,discover,status,next,details,doctor}
```

Это inference, не accepted topology.

## 16. Необходимые architecture decisions

Compatibility relationship, first slice, implementation repo, interface, Project Memory persistence, Runtime/Factory boundary, Governance packaging, language/toolchain/dependencies, plugin/versioning, provider/privacy/routing и admission enforcement/UI/release.

## 17. Отложенная сложность

Full Control Plane, authority-bearing central registry, unbounded autonomous
loops вне parent task authority/stage envelopes, broad autonomous self-heal,
vector DB, distributed services, multi-agent cascade, broad sandbox framework,
plugin marketplace, SaaS collaboration backend и regulated medical architecture.
Bounded complete-task loop из разделов 5, 6 и 14 в эту deferred category не
входит.
