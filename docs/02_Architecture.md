---
package: AOS_Project_Knowledge_Baseline
package_revision: R4-RU
updated: '2026-09-13'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
current_change_subject: AOS_MODULAR_CORE_DOCUMENTATION_R1
current_change_authority: CURRENT_EXPLICIT_HUMAN_INSTRUCTION
current_change_agent_review: PASS
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

RAG-light, model routing, runtime enforcement, plugins, domain modules, workbench/SaaS и observability.

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
До отдельной выдачи он не содержит authorization identity. Фактический binding
сохраняется controller в Loop State без переписывания Task Brief. `requested_*`
никогда не трактуется как `allowed_*`.

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
envelope_schema_version: AOS_EFFECTFUL_STAGE_ENVELOPE_V1
envelope_id:
parent_authorization_id:
parent_authorization_digest:
parent_authorization_revision:
state_machine_version: AOS_COMPLETE_TASK_LOOP_V1
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
`AOS_COMPLETE_TASK_LOOP_V1`. Для `CORRECT` обязательны Correction Gate identity
и digest; для `EXECUTE` они отсутствуют.

Admission атомарно проверяет: текущие state/event/candidate; разрешённый
`{from,to}` из canonical transition matrix; exact action-spec digest; текущую
unexpired/unrevoked Parent Task Authorization с совпадающими
identity/revision/digest; subset allowed и superset forbidden fields; gate для
`CORRECT`; unused/unexpired envelope. После admission envelope потребляется до
effect. Cache или вложенный digest не заменяет чтение текущих records.

#### C-007 — Preflight / Preview

Exact repository/worktree/branch/HEAD/baseline/status/diff, planned actions, paths, conflicts, permissions и preview identity.

#### C-008 — Execution Record

Starting identity, Stage Envelope identity/digest, action-spec digest, actual
mutations, changed paths, side effects, checks, ending identity, limitations и
stop reason.

#### C-009 — ValidationEnvelope

```yaml
validation_envelope_version: AOS_VALIDATION_ENVELOPE_V1
validation_envelope_id:
state_machine_version: AOS_COMPLETE_TASK_LOOP_V1
task_id:
task_revision:
candidate_identity:
state_revision:
event_head_identity:
transition:
  from: EXECUTE | CORRECT | SELECT_NEXT_ACTION | CHECK
  to: CHECK | FINAL_VALIDATE
worker_action: CHECK | FINAL_VALIDATE
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

#### C-009A — Correction Gate

```yaml
gate_id:
gate_version: AOS_CORRECTION_GATE_V1
state_machine_version: AOS_COMPLETE_TASK_LOOP_V1
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
action. Controller является единственным владельцем переходов; worker output —
observation, а не authority изменить state или объявить completion. Concurrent
или stale update отклоняется: только один controller может подтвердить изменение
из одной исходной revision. Отказ ведёт к reconciliation; конкретный механизм
синхронизации выбирается при реализации.

#### C-013 — Install / Update Manifest

Package identity, ownership classes, operations, conflicts, preview binding, recovery и post-apply verification.

#### C-014 — Git Delivery Record

Separate records for Commit, Push, Merge и Release.

<a id="module-contracts"></a>

### 6.1. Композиция и сопровождение модулей — MODULAR_DRAFT

Этот раздел уточняет предложение [MOD-DEC-01](01_Product.md#modular-decisions). Существующие C-001…C-014 сохраняют идентичности. Здесь описано содержание сообщений на уровне WHAT; wire format, внутреннее представление и алгоритм хранения не выбираются.

| Contract | Producer / владелец содержания | Данные и consumers | Отказ и область повторной проверки |
|---|---|---|---|
| C-001 | FTR-001; человек подтверждает intent | Original request, problem/outcome, assumptions/unknowns; FTR-003 | Неясная цель → уточнение; проверить перенос смысла в Spec |
| C-002/C-003 | FTR-003; принятый Product artifact | Actor, scope, behavior, I/O, failures, criteria, disposition; FTR-005/006/007/012 (FTR-012 читает критерии C-002) | Нет критерия → DRAFT без execution; проверить ADR, Brief, child contribution и полноту review criteria |
| C-004 | FTR-005 готовит; человек выбирает | Вопрос, варианты, Evidence, выбор/последствия; FTR-003/006/022 | Нет решения → selected_option отсутствует; проверить зависимые задачи и patterns |
| C-005 | FTR-006; Task Brief owner | Task/revision, requested/prohibited scope, criteria/checks/limits; FTR-007/009/010/012/013 | Противоречивый scope → отказ допуска; проверить preview/candidate, child task и criterion-to-Evidence review |
| C-006 | Человек — issuer; controller хранит binding | Subject, разрешённые/запрещённые effects, срок/отзыв; FTR-019/010/014 | Missing/stale/revoked → запрет эффекта; проверить admission и resume |
| C-006A | Controller — issuer stage envelope | Transition/action/state/candidate и parent binding; FTR-010 | Mismatch/replay → отказ до effect; проверить execute/correct paths |
| C-007 | FTR-009; наблюдение repository и preview | Root/worktree/baseline/dirty state/actions/permissions; FTR-002/004/010/013 | Изменён subject → новое preview; проверить discovery binding, preservation, admission и сверку validation subject |
| C-008 | Worker FTR-010; factual observation | До/после, envelope, effects/unknown effects, stop reason; FTR-013/014/025 | Неполный effect → reconciliation; проверить отсутствие двойного исполнения |
| C-009 | Controller выдаёт; FTR-011 возвращает observation | Candidate, required checks, results, limitations; FTR-008/010/011/012/023 | Required NOT_RUN/unknown impact → нет completion; проверить aggregation/staleness |
| C-009A | Controller оценивает diagnostic record | Signature, hypotheses, prediction, recovery, correction binding; FTR-010 | Слабое Evidence/replay → DENY; проверить D0…D5 и fresh correction |
| C-010 | Наблюдавший checker/worker; immutable Evidence | Метод, subject, результат, locator, limitations; FTR-008/011/012/021/023/025 | Недоступный источник → UNKNOWN; проверить ссылки, redaction и границу результата |
| C-011 | Человек — owner; FTR-012 готовит review | Actor/source, subject, decision, scope/время; FTR-006/008/012/015/019/021 | Неизвестный actor/stale subject → решение не применяется; проверить admission без audit-модуля |
| C-012 | Controller владеет lifecycle state; FTR-016 сохраняет/выдаёт | Versions, state axes, candidate, authority, ledger, decisions, next action; FTR-007/008/010/014/016/017 | Старая revision → recover, не overwrite; проверить старые задачи и concurrency |
| C-013 | FTR-004; план и наблюдённые результаты установки | Package/target, ownership, operations, preview, conflicts/recovery; FTR-004/009/011/014 | Конфликт user state → стоп apply; проверить install/update/uninstall и повтор |
| C-014 | FTR-015; отдельная запись каждого действия | Action, repo/source/target, candidate, authority, результат; FTR-012/014/015 | Remote uncertainty → проверить эффект до retry; проверить Git-действия отдельно |

Сверка карты влияния обязательна при изменении входа dossier: каждый именованный C-contract из раздела «Входные данные» должен иметь эту фичу среди consumers таблицы либо явное объяснение неприменимости. Чтение contract собственным producer также учитывается, если он принимает сохранённый record как вход. Проверка criteria-to-Evidence и stale review входит в область изменения C-002/C-005; изменение C-007 затрагивает сверку candidate в FTR-013.

Backlog, pattern и incident имеют владельцев содержания в своих feature contracts. Хранение через FTR-016 не передаёт ему это владение. Идентичность issuer/actor проверяется принятым способом capture, а не наличием имени в поле.

**Совместимость — предложение.** Необязательное пояснительное поле совместимо лишь если reader contract допускает его игнорирование и оно не влияет на authority/state/completion. Strict format с запретом неизвестных полей требует новой reader-version или явного отказа. Изменение смысла, обязательности, enums или state machine несовместимо до доказательства обратного. Совместимость определяется парой producer/consumer versions, а не только номером версии.

Старая задача допускает inspection без effects, если её формат поддержан. Resume требует поддержанного state-machine contract и fresh authority. При необходимом преобразовании видны исходная/целевая версия, затронутые данные и recovery; оно выполняется только в отдельно разрешённом scope. Исходный record сохраняется; новое представление не создаёт human approval. Прерванное преобразование требует reconciliation до resume. Диапазон поддерживаемых версий относится к MOD-DEC-02; пока он не выбран, runtime support UNKNOWN.

**Отказ и отключение.** Модуль может отсутствовать, работать, быть недоступным или завершать начатую операцию. Это описания capability, не новые task/run enums. Новая операция требует своих required capabilities. Отключение write-модуля начинается с определения effects и сохранения recoverable state; мгновенное безопасное удаление не обещается. Данные пользователя и Evidence не удаляются вместе с модулем. Отказ индекса допускает прямой поиск, отказ проверки authority блокирует effect. Обязательный CI без declared equivalent остаётся NOT_RUN. Ограничение покрытия видно пользователю и не выдаётся за полный PASS.

**Authority.** Базовый admission проверяет human provenance, срок, scope и subject до эффекта. FTR-021 аудитирует записи, но не служит обязательным сервисом выдачи разрешений. Отказ optional audit не отключает базовую проверку; отсутствие доверенного способа capture (MOD-DEC-03) блокирует затронутые действия. Включение модуля не предоставляет network/provider/Git/delete authority.

**Сопровождение.** Изменяется owner contract, затем проверяются его consumers и acceptance/negative cases из таблицы. Новое состояние или effect требует владельца, отказа и recovery. Неизвестное влияние требует расширения проверки. Derived index не изменяет Product facts. Эта таблица описывает межфичевые contracts; детализация конкретных сценариев находится в dossiers.

## 7. Ортогональная модель состояний

Оси не изменяют друг друга автоматически.

```text
Document maturity:
DRAFT | HUMAN_REVIEW_REQUIRED | HUMAN_ACCEPTED | SUPERSEDED

Lifecycle stage:
PLAN | EXECUTE | VALIDATE | REVIEW

Controller action (`AOS_COMPLETE_TASK_LOOP_V1`):
BIND_TASK | RECOVER_STATE | SELECT_NEXT_ACTION | EXECUTE | CHECK | DIAGNOSE |
CORRECT | FINAL_VALIDATE | IDLE

Task state:
ACTIVE | WAIT_HUMAN | WAIT_EVIDENCE | TECHNICALLY_COMPLETE |
TASK_FAILED | CANCELLED_BY_HUMAN | CONTRACT_VIOLATION

Run state:
RUNNING | PAUSED_RESOURCE | STOPPED

Technical result:
CONTRACT_VIOLATION | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PASS

Human decision:
ACCEPT | NEEDS_CHANGES | REJECT | DEFER

Permission:
ALLOWED | HUMAN_AUTHORIZATION_REQUIRED | BLOCKED_POLICY | BLOCKED_UNKNOWN | NOT_APPLICABLE
```

Canonical controller-action matrix `AOS_COMPLETE_TASK_LOOP_V1`:

| `from` | Допустимые `to` |
|---|---|
| `BIND_TASK` | `RECOVER_STATE`, `IDLE` |
| `RECOVER_STATE` | `SELECT_NEXT_ACTION`, `DIAGNOSE`, `IDLE` |
| `SELECT_NEXT_ACTION` | `EXECUTE`, `CHECK`, `FINAL_VALIDATE`, `IDLE` |
| `EXECUTE` | `CHECK`, `DIAGNOSE`, `IDLE` |
| `CHECK` | `SELECT_NEXT_ACTION`, `DIAGNOSE`, `FINAL_VALIDATE`, `IDLE` |
| `DIAGNOSE` | `CORRECT`, `IDLE` |
| `CORRECT` | `CHECK`, `DIAGNOSE`, `IDLE` |
| `FINAL_VALIDATE` | `DIAGNOSE`, `IDLE` |
| `IDLE` | `RECOVER_STATE` после resume event |

Матрица описывает только controller-action axis. `WAIT_HUMAN`,
`WAIT_EVIDENCE`, `TECHNICALLY_COMPLETE`, `TASK_FAILED`,
`CANCELLED_BY_HUMAN` и `CONTRACT_VIOLATION` изменяют task state и переводят
controller action в `IDLE`; `PAUSED_RESOURCE` изменяет run state, сохраняет task
`ACTIVE` и также переводит action в `IDLE`. Lifecycle stage меняется только по
своему workflow. Переходы между разными осями не записываются как `{from,to}`
controller actions.

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

RAG-light допустим только после measured search/context problem.

<a id="repository-graph-contract"></a>

### 10.1. Контракт проектного графа — PROPOSAL

Статус всех положений этого подраздела — `PROPOSAL` для возможной будущей реализации. Назначение и не-цели определены в [Product](01_Product.md#repository-graph-purpose); источник — [ТЗ R2](05_Reference.md#repository-graph-tz). Требования ниже не меняют владельцев фактов из §8, dispositions фич или полномочия на реализацию.

**Единый производный артефакт.** Один локальный worktree имеет один активный graph artifact с общей системой наблюдений; виды кода, данных и фич не ведутся как отдельные редактируемые карты. Допустим временный кандидат публикации. Обзор генерируется по запросу. Удаление графа не уничтожает первичные требования, решения или уникальный обязательный контекст.

Граф содержит сведения о версии схемы, extractor и профиле наблюдения, scope и source bindings, sources, nodes, edges, evidence, coverage, unresolved и pending refresh. Это логические части одного контракта, а не требование отдельных registries. Конкретный storage, parser, индексы, алгоритмы IDs/обхода и механика записи относятся к Engineering Design по `00_Core.md`, §12; они здесь не фиксируются.

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

Критерии проверки, последовательность срезов и решения перед реализацией принадлежат [Development](03_Development.md#repository-graph-pilot). Storage пересматривается по измеренным расходам и удобству review, а не произвольному размеру или числу файлов.

## 11. Адаптеры агентов

Один common rule source поддерживает thin adapters для Codex, Claude Code, Cursor, ChatGPT и других сред. Adapters не расширяют permissions, используют repository-relative links и должны быть generated или drift-checked.

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
