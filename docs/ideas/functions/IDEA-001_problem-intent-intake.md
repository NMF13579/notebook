---
document_id: AOS-ATOMIC-FUNCTION-IDEA-001
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-001
function_title: "Problem / Intent Intake"
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
primary_feature_family: FTR-001
related_feature_families: [FTR-001]
human_review_required: true
---

# IDEA-001 — Problem / Intent Intake

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Принимает исходную формулировку пользователя и превращает её в версионируемую запись проблемы и намерения, не подменяя исходный смысл и не придумывая отсутствующие требования.**

Основной наблюдаемый результат функции: **`Intent Record`**.

`IDEA-001` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** Non-programmer product owner, product lead, intake agent; при sensitive/regulated context — designated human reviewer.

Основные jobs-to-be-done:

- Зафиксировать исходную идею без потери формулировки и контекста.
- Понять, достаточно ли данных для specification или нужен короткий interview.
- Отделить пользовательский результат от предложенного способа реализации.
- Рано обнаружить sensitive-domain, privacy и external-content boundaries.
- Получить один понятный следующий шаг вместо длинного универсального опросника.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

Исходный запрос обычно смешивает проблему, желаемый результат, готовое решение, ограничения и предположения. Без управляемого intake агент либо задаёт слишком много вопросов, либо сразу проектирует не ту систему.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-001` family flow теряет конкретный механизм «Problem / Intent Intake», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Intent Record` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- Пользователь впервые описывает проблему или проект.
- Поступает change request без полного контекста.
- Загружено готовое ТЗ, и требуется определить, можно ли идти напрямую к specification.
- Существующая постановка противоречива или смешивает несколько outcomes.

### Preconditions

- Известен язык взаимодействия и доступен исходный текст запроса.
- Ранее подтверждённый project context может быть прочитан, но не считается автоматически актуальным.
- Sensitive content не отправляется внешнему provider без разрешённой boundary.
- Intake выполняется read-only и не создаёт downstream authority.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `raw_request`
- `optional_ready_specification`
- `known_project_context`
- `user_constraints`
- `non_goals`
- `examples_or_reference_links`
- `sensitivity_hints`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-001
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: INTENT_RECORD
```

## 8. Пошаговое поведение

1. Сохранить исходный input и provenance без перефразирования, которое уничтожает исходный смысл.
2. Проверить, достаточно ли данных для этой функции и какие unknowns material для следующего шага.
3. Выполнить только функцию, названную в документе; не переходить автоматически к architecture, task generation или execution.
4. Показать человеку interpretation/result и дать возможность исправить его до downstream use.
5. Сформировать durable output и один следующий read-only route либо явный blocker.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Problem / Intent Intake**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-001`.
4. Создаётся **`Intent Record`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Intent Record`.

Source-derived outputs:

- Intent Record
- Clarification summary
- Sensitive-domain flags
- Unknown/decision register fragment
- Next-route recommendation

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-001
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
RAW_INPUT → CLASSIFIED → CLARIFICATION_REQUIRED | SUFFICIENT → DRAFT_READY → HUMAN_CORRECTION | ROUTE_READY | BLOCKED
```

Transition invariants:

- Human-only transition не генерируется agent output.
- Material change subject/scope инвалидирует downstream DRAFT artifacts.
- `VALIDATE` и `REVIEW` не исправляют candidate.
- Failure/unknown приводит к report + stop.
- Recovery/correction выполняются отдельным authorized stage.

## 11. UX и человекочитаемое представление

- По умолчанию показывается краткая интерпретация: «Я понял задачу так…».
- Вопросы задаются только там, где отсутствие ответа меняет scope, safety или observable outcome.
- Пользователь всегда видит исходный текст рядом с normalized interpretation.
- Для готового ТЗ интерфейс должен позволять выбрать direct path без повторного интервью.
- Sensitive-domain blocker формулируется простым языком и указывает, какое human decision требуется.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Problem / Intent Intake** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-001-01` — Функция должна выполнять только следующую ответственность: Принимает исходную формулировку пользователя и превращает её в версионируемую запись проблемы и намерения, не подменяя исходный смысл и не придумывая отсутствующие требования.
- `FR-001-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-001-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-001-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-001-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-001-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Сохранять immutable copy исходного запроса и revision history интерпретаций.
- `FR-002` — Не заполнять отсутствующие требования догадками; использовать UNKNOWN.
- `FR-003` — Различать user problem, desired outcome, proposed solution и implementation assumption.
- `FR-004` — Проверять, есть ли уже ответ в подтверждённом context pack, прежде чем задавать вопрос.
- `FR-005` — Ограничивать один clarification round только material неизвестными; следующий round допускается при новом conflict.
- `FR-006` — Формировать ровно один recommended route и перечислять альтернативы только при реальной развилке.
- `FR-007` — Не переводить interpretation approval в product acceptance.

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

- `CTR-001` — `IntentRecord`: id, revision, raw_request, actor, problem, desired_outcome, constraints, non_goals, assumptions, unknowns, sensitivity_flags, source_refs.
- `CTR-002` — `ClarificationItem`: question, materiality, affected_fields, answer, answer_source, status.
- `CTR-003` — `IntakeRoute`: route_type, rationale, prerequisites, blocked_by, next_required_action.
- `CTR-004` — `HumanInterpretationResponse`: CORRECT | ACCEPT_FOR_DRAFTING | DEFER | REJECT; не является Product Decision.
- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.

## 14. Связь с feature families

- [`FTR-001` — Intent Intake, Problem Interview and Outcome Clarification](../features/FTR-001_intent-intake-problem-interview-and-outcome-clarification.md)

Primary family layer: `Product Runtime`. Proposed disposition: `CANDIDATE`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

Не выбирает architecture, dependencies, Risk Profile и не создаёт execution authorization. Human acceptance of interpretation не равна product acceptance.

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

- Intake превращается в oversized questionnaire.
- Agent придумывает requirements или silently converts an idea into accepted scope.
- Sensitive data попадает в неподходящий provider/context.
- Ready specification повторно разбирается без необходимости.
- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.

## 17. Recovery behavior

**Source-derived recovery behavior:** Вернуться в `CLARIFYING`, показать конкретную неоднозначность, сохранить исходный текст и пометить неподтверждённые поля как `UNKNOWN`; не продолжать к architecture или execution.

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

- Сравнение raw_request и normalized interpretation.
- Список заданных вопросов с объяснением materiality.
- Отчёт о повторном использовании context и исключённых stale facts.
- Reason codes для sensitive/blocking cases.

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

Каждый event содержит `function_id=IDEA-001`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-001-01` — Пользователь понимает назначение Problem / Intent Intake без чтения implementation internals.
- `AC-001-02` — Функция создаёт ровно `Intent Record` либо честный terminal report.
- `AC-001-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-001-04` — Unknowns, exclusions и blockers видимы.
- `AC-001-05` — Human authority и downstream permissions не расширены.
- `AC-001-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — Пользователь узнаёт собственный запрос и не обнаруживает придуманных requirements.
- `AC-002` — Каждое неизвестное, влияющее на следующий route, явно помечено.
- `AC-003` — Готовое ТЗ проходит direct path без ненужного interview.
- `AC-004` — Новый пользователь понимает, почему выбран следующий шаг.
- `AC-005` — Intake не создаёт mutation, architecture decision или execution authorization.
- `AC-006` — Sensitive data boundary проявляется до передачи данных неподходящему provider.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Intent Record` для exact subject.
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

Первый вариант может быть Markdown/JSON document compiler с rule-based completeness check и chat adapter. Никакой DB, RAG или agent orchestration не требуется. Сначала достаточно шаблона, closed enums и deterministic validation.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_001`
