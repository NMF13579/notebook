---
document_id: AOS-ATOMIC-FUNCTION-IDEA-016
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-016
function_title: "Task Generation and Task Brief"
status: DRAFT
authority: NONE
canonical_status: NOT_ASSIGNED
human_acceptance: NOT_REQUESTED
product_scope_effect: NONE
implementation_authorization: NONE
execution_authorized: false
git_authorization: NONE
implementation_repository: UNASSIGNED
repository_verification: NOT_RUN
source_origin: HISTORICAL_MICRO_IDEA_CROSSWALK
primary_feature_family: FTR-006
related_feature_families: [FTR-006]
human_review_required: true
---

# IDEA-016 — Task Generation and Task Brief

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Преобразует утверждённый bounded scope в один самодостаточный Task Brief с exact subject, allowed changes, validation и stop conditions.**

Основной наблюдаемый результат функции: **`Task Brief`**.

`IDEA-016` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** Product owner, task author, executor, validator and reviewer.

Основные jobs-to-be-done:

- Передать агенту задачу без чтения всей истории.
- Зафиксировать allowed/forbidden scope и baseline.
- Не смешать plan, Task Brief и execution authorization.
- Согласовать expected result, validation и stop conditions.
- Сформировать короткий Stage Report после run.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

Product documentation is too broad for a bounded run. Informal tasks omit allowed/forbidden scope, baseline, checks, stop conditions or human gates; generated plans can be mistaken for authorization.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-016` family flow теряет конкретный механизм «Task Generation and Task Brief», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Task Brief` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- Selected feature/slice готов к bounded work item.
- Correction task требуется после finding.
- Документационная задача имеет ясный exact output.
- Existing informal task needs normalization.

### Preconditions

- Goal/outcome и exact subject известны.
- Repository state либо известен, либо preflight указан как required.
- Material architecture/dependency decisions закрыты или task ограничен research.
- Human authority fields default false.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `selected_feature_or_slice`
- `accepted_decisions`
- `repository_subject`
- `in_scope_and_out_of_scope`
- `acceptance_criteria`
- `validation_plan`
- `risk_factors`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-016
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: TASK_BRIEF
```

## 8. Пошаговое поведение

1. Проверить наличие принятых upstream inputs и material unknowns.
2. Создать первый DRAFT строго для exact subject и сохранить links to source IDs.
3. Проверить completeness, internal consistency, non-goals, authority wording и downstream dependencies.
4. Показать человеку changes, alternatives и unresolved decisions.
5. Сохранить revisioned artifact; не считать его accepted или executable без отдельного decision.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Task Generation and Task Brief**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-016`.
4. Создаётся **`Task Brief`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Task Brief`.

Source-derived outputs:

- DRAFT Task Brief
- Scope/non-goal map
- Validation plan
- Non-grants
- Stage Report template
- Traceability links

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-016
subject_id: REQUIRED
subject_revision: REQUIRED
result_status: PASS | FAIL | BLOCKED | UNKNOWN | NOT_RUN | PARTIAL | READY_FOR_REVIEW
artifact_ref: REQUIRED_IF_CREATED
evidence_refs: []
limitations: []
partial_effects: []
next_required_action: REQUIRED
human_decision: NONE_UNLESS_ACTUAL_HUMAN_INPUT
```

## 10. State model

```text
INPUT_READY → DRAFTING → DRAFT_READY → CHECKED → HUMAN_REVIEW_REQUIRED | REWORK_REQUIRED | DEFERRED
```

Transition invariants:

- Human-only transition не генерируется agent output.
- Material change subject/scope инвалидирует downstream DRAFT artifacts.
- `VALIDATE` и `REVIEW` не исправляют candidate.
- Failure/unknown приводит к report + stop.
- Recovery/correction выполняются отдельным authorized stage.

## 11. UX и человекочитаемое представление

- Описание задачи идёт первым, компактный YAML — в конце или frontmatter.
- Пользователь видит «что будет изменено» и «что точно не будет изменено».
- Missing material field отображается как конкретный blocker, а не новый большой plan.
- Task Brief показывает one next stage и stop condition.
- Authorization fields визуально отделены и по умолчанию false.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Task Generation and Task Brief** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-016-01` — Функция должна выполнять только следующую ответственность: Преобразует утверждённый bounded scope в один самодостаточный Task Brief с exact subject, allowed changes, validation и stop conditions.
- `FR-016-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-016-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-016-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-016-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-016-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Task Brief self-contained для назначенной роли.
- `FR-002` — Goal, expected result, scope, subject, checks и stop conditions обязательны.
- `FR-003` — Accepted source decisions связываются по ID/locator, а не копируются без provenance.
- `FR-004` — Risk Profile остаётся UNASSIGNED до human decision.
- `FR-005` — Protected/destructive/network/Git actions перечисляются отдельно.
- `FR-006` — Material scope change invalidates Task Brief.
- `FR-007` — Compiler cannot create approval or execution grant.

## 13. Data and contract model — `PROPOSAL`

Минимальные сущности:

- `FunctionInvocation` — exact request, actor, subject, inputs, permissions, started/finished timestamps.
- `FunctionResult` — status, artifact reference, evidence, limitations, partial effects, next action.
- `SourceBinding` — source ID/revision/location, claim class, freshness and authority.
- `HumanDecisionReference` — только ссылка на реальный human record; функция не создаёт его самостоятельно.

Contract invariants:

- UTF-8, stable IDs, explicit enums, deterministic serialization where identity matters.
- Duplicate keys и silent coercion запрещены.
- Unknown fields обрабатываются по явной compatibility policy; silent loss запрещён.
- Result status и human acceptance — разные поля и разные owners.
- Authority-bearing record binds exact subject/scope/operation and human identity.

Family-derived contract constraints:

- `CTR-001` — `TaskBrief`: task_id, stage, goal, expected_result, subject, in_scope, out_of_scope, allowed_paths, forbidden_paths, required_checks, stop_conditions, outputs.
- `CTR-002` — `AuthoritySection`: proposed_risk_profile, assigned_risk_profile, execution_authorized, git_authorizations, non_grants.
- `CTR-003` — `TraceBinding`: source_requirement, decision_id, feature_id, architecture_or_ux_constraint.
- `CTR-004` — `StageReport`: actual_outputs, actual_scope, checks, findings, limitations, terminal_status, next_required_action.
- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.

## 14. Связь с feature families

- [`FTR-006` — Task Brief Compiler, Scope Confirmation and One-Task-One-Document Model](../features/FTR-006_task-brief-compiler-scope-confirmation-and-one-task-one-document-model.md)

Primary family layer: `Product Runtime / Development Factory boundary`. Proposed disposition: `CANDIDATE`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

Task Brief, plan, routing and selection do not authorize execution, Git or release.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

Обязательные правила:

- `PASS`, Evidence, CI, readiness и metrics не равны approval.
- `UNKNOWN/BLOCKED` не равны OK; `NOT_RUN` не равен PASS.
- Agent output не является human decision.
- Plan, Task Brief, route и preview не являются execution authorization.
- Edit, Commit, Push, PR create, Merge и Release требуют раздельных permissions.
- External content остаётся untrusted data, пока authority не доказана.

## 16. Failure modes

Function-specific failure classes:

- Output не связан с exact subject или input revision.
- Функция захватывает ответственность соседней функции и скрыто расширяет scope.
- Missing data заменяется уверенной inference без маркировки.
- Derived view расходится с owner artifact.
- Result wording создаёт ложное впечатление acceptance/readiness.

Family-derived failure modes:

- Brief becomes another broad plan.
- Risk Profile inferred by agent.
- `execution_authorized: true` generated without human action.
- Compiler drops fields or changes status semantics.
- Task silently expands paths/dependencies/network.
- One task contains multiple stages or unrelated outcomes.

## 17. Recovery behavior

**Source-derived recovery behavior:** Reject incomplete/contradictory brief, list exact missing field or conflict, preserve source item, and return to PLAN. Any material scope change requires a new or revised brief.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

Recovery sequence:

```text
failure / denial / unknown
→ freeze observed state
→ emit reason + partial effects
→ present safe options
→ human choice where required
→ separately authorized correction/resume/rollback
→ separate targeted validation
```

## 18. Observability и Evidence

- Completeness validator result.
- Trace links to product/architecture/UX sources.
- Scope diff between prior draft and final draft.
- Human scope review record if provided.

Минимальный Evidence package связывает:

```text
source / human decision
→ user problem
→ expected outcome
→ feature requirement
→ candidate / output
→ check result
→ finding / limitation
→ human decision
```

Минимальные events:

- `function_requested`
- `precondition_checked`
- `function_started`
- `artifact_created_or_reused`
- `function_blocked_or_failed`
- `function_completed`
- `human_review_requested`

Каждый event содержит `function_id=IDEA-016`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-016-01` — Пользователь понимает назначение Task Generation and Task Brief без чтения implementation internals.
- `AC-016-02` — Функция создаёт ровно `Task Brief` либо честный terminal report.
- `AC-016-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-016-04` — Unknowns, exclusions и blockers видимы.
- `AC-016-05` — Human authority и downstream permissions не расширены.
- `AC-016-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — Executor can act without inventing missing material facts.
- `AC-002` — Scope and forbidden areas are explicit.
- `AC-003` — Validation plan is executable or marked NOT_RUN/BLOCKED.
- `AC-004` — All authorization fields default false.
- `AC-005` — Task Brief does not repeat unnecessary planning when complete.
- `AC-006` — Stage Report can be generated without overstating completion.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Task Brief` для exact subject.
- Output содержит provenance, revision, status и явные limitations.
- Повторный read-only запуск на неизменном subject даёт эквивалентный результат либо объяснённую разницу.
- Human-only decision не появляется без реального human input.

### Negative and boundary tests

- Missing prerequisite не трактуется как разрешение или PASS.
- Stale/legacy source не становится current Source of Truth только из-за наличия в context.
- Scope expansion, protected operation или permission escalation блокируются и объясняются.
- Failure/partial result не маскируется статусом success.

### Integration tests

- Upstream artifact revision mismatch приводит к `BLOCKED`, а не silent continuation.
- Downstream consumer принимает только explicit result schema.
- Cross-family use сохраняет один owner artifact и не создаёт conflicting copies.
- Audit trail позволяет восстановить, почему и на каком input был получен result.

## 21. Minimal implementation model — `PROPOSAL`

Markdown-first compiler with strict schema, linting, source bindings and templates. Avoid central task registry initially; files can be repository-native and human-readable.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

Atomic implementation следует начинать с минимального boundary:

1. Typed input/output contract.
2. Pure/deterministic core where possible.
3. Thin adapters for filesystem, Git, provider or UI only when required.
4. Targeted tests for success, denial, unknown, stale input and partial failure.
5. No autonomous loop, registry platform or external dependency unless separately accepted.

## 22. Rollout path

1. `DOCUMENT_ONLY` — terminology, inputs, outputs, examples, failure semantics.
2. `MANUAL_FLOW` — человек выполняет steps по checklist.
3. `ADVISORY_TOOL` — tool создаёт proposal/report, но не mutates subject.
4. `GUARDED_EXECUTION` — только при доказанной необходимости, accepted contracts и explicit authorization.
5. `ENFORCED/AUTOMATED` — отдельное architecture and risk decision.

Переход между уровнями не автоматический.

## 23. Open questions и human decisions

- Нужна ли эта функция в early Product Runtime, supporting layer или она остаётся deferred?
- Кто владеет canonical schema/output?
- Какой exact subject и repository path используются?
- Какие dependencies/providers допустимы?
- Какой Risk Profile назначает человек?
- Какие operations, если они вообще есть, разрешены функции?
- Какая независимая validation обязательна перед promotion?

## 24. Source traceability и limitations

- Source catalogs: `AOS_Full_Feature_Catalog_R1.md`, `AOS_Full_Feature_Catalog_From_Project_Chats_R1.md`.
- Related family dossiers перечислены в разделе 14.
- Доступная project chat history не доказана как byte-complete export всех сообщений.
- Current repository/worktree/branch/HEAD/baseline/runtime implementation: `NOT_RUN`.
- Все detailed requirements/tests/contracts в этом файле — `PROPOSAL`, если явно не указано иное.

## 25. Promotion path

```text
DRAFT atomic function description
→ human review
→ ACCEPT / MODIFY / SPLIT / MERGE / DEFER / REJECT
→ accepted Product/Feature Contract if selected
→ bounded Task Brief
→ explicit execution authorization
→ EXECUTE
→ separate VALIDATE
→ separate REVIEW
→ human decision
```

`next_required_action: HUMAN_REVIEW_OF_IDEA_016`
