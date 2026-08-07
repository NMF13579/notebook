---
document_id: AOS-ATOMIC-FUNCTION-IDEA-090
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-090
function_title: "Online Market Pattern Research with Source and License Policy"
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
primary_feature_family: FTR-022
related_feature_families: [FTR-022, FTR-031]
human_review_required: true
---

# IDEA-090 — Online Market Pattern Research with Source and License Policy

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Исследует market products и public patterns с source, date, license и trust policy, не копируя proprietary design и не делая reference обязательным.**

Основной наблюдаемый результат функции: **`Market Pattern Research Report`**.

`IDEA-090` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** Product designer, architect, developer, reviewer and planning agent.

Основные jobs-to-be-done:

- Не изобретать повторно удачное решение.
- Не копировать legacy code или market pattern без context.
- Сравнить pattern fit с текущей feature.
- Связать lessons с preventive tests.
- Deprecate pattern, когда условия изменились.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

Useful solutions and lessons are repeatedly reinvented or copied as cargo cult. A pattern without context, failure cases and tests becomes hidden architecture.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-090` family flow теряет конкретный механизм «Online Market Pattern Research with Source and License Policy», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Market Pattern Research Report` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- Same solution/problem recurs.
- Lesson has a reusable preventive mechanism.
- UX Skeleton or architecture needs advisory options.
- Pattern failure or compatibility change is observed.

### Preconditions

- Source/provenance and licensing can be recorded.
- Pattern context and non-fit cases known.
- At least one usage/test/incident supports value.
- Human adoption decision remains separate.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `problem_and_context`
- `solution_description`
- `source_and_license`
- `tradeoffs_and_failures`
- `fit_non_fit_criteria`
- `tests_and_usage_records`
- `owner_and_version`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-090
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: MARKET_PATTERN_RESEARCH_REPORT
```

## 8. Пошаговое поведение

1. Получить canonical context и exact user-facing subject.
2. Сформировать human-readable view/artifact, не меняя underlying facts и permissions.
3. Показать states, edge cases, blockers, provenance и available actions.
4. Провести structural/human review и записать только явно принятый scope.
5. Не выдавать preview, mode или visual direction за working implementation/approval.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Online Market Pattern Research with Source and License Policy**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-090`.
4. Создаётся **`Market Pattern Research Report`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Market Pattern Research Report`.

Source-derived outputs:

- Pattern card
- Fit Matrix
- Usage/compatibility notes
- Test links
- Deprecation record

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-090
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
CONTEXT_READY → VIEW/ARTIFACT_DRAFT → STRUCTURE_CHECK → HUMAN_REVIEW → ACCEPTED_DIRECTION | REWORK | DEFERRED
```

Transition invariants:

- Human-only transition не генерируется agent output.
- Material change subject/scope инвалидирует downstream DRAFT artifacts.
- `VALIDATE` и `REVIEW` не исправляют candidate.
- Failure/unknown приводит к report + stop.
- Recovery/correction выполняются отдельным authorized stage.

## 11. UX и человекочитаемое представление

- Pattern card starts with when to use and when not to use.
- Fit Matrix compares current feature conditions with pattern assumptions.
- Provenance/license/maturity visible before recommendation.
- Recommendation states confidence and missing evidence.
- Deprecated patterns show replacement and affected uses.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Online Market Pattern Research with Source and License Policy** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-090-01` — Функция должна выполнять только следующую ответственность: Исследует market products и public patterns с source, date, license и trust policy, не копируя proprietary design и не делая reference обязательным.
- `FR-090-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-090-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-090-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-090-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-090-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Every pattern must include problem, context, solution, trade-offs, failures and tests.
- `FR-002` — Pattern authority is NONE.
- `FR-003` — Usage requires explicit fit assessment.
- `FR-004` — Online/legacy sources retain provenance and licensing notes.
- `FR-005` — Pattern versions and compatibility are tracked.
- `FR-006` — Failure/incident can deprecate or narrow fit.
- `FR-007` — No pattern recommendation may silently modify architecture/UX.
- `FR-001` — Every UX object has stable ID and source requirement.

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

- `CTR-001` — `PatternCard`: pattern_id, problem, context, solution, fit, non_fit, tradeoffs, failures, tests, provenance, license, maturity, owner, version.
- `CTR-002` — `FitAssessment`: feature_id, pattern_id, matched_conditions, mismatches, unknowns, recommendation.
- `CTR-003` — `PatternUsage`: subject, decision_ref, version_used, adaptations, outcome.
- `CTR-004` — `DeprecationRecord`: reason, replacement, affected_usages, effective_at.
- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.

## 14. Связь с feature families

- [`FTR-022` — Solution/Pattern Library, Fit Matrix and Reusable UX/Engineering Patterns](../features/FTR-022_solution-pattern-library-fit-matrix-and-reusable-ux-engineering-patterns.md)
- [`FTR-031` — Project UX Skeleton → Human Review → Vertical Slices → Task Briefs → Code](../features/FTR-031_project-ux-skeleton-to-human-review-to-vertical-slices-to-task-briefs-to-code.md)

Primary family layer: `Knowledge support`. Proposed disposition: `CANDIDATE_SUPPORT`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

Pattern library has `authority: NONE`; architecture/product adoption requires human decision.

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

- One-off solution becomes universal.
- Legacy code copied without contract.
- Pattern recommendation interpreted as decision.
- Market research ignores licenses or context.
- Library grows without owners/tests.
- Deprecated pattern remains silently active.

## 17. Recovery behavior

**Source-derived recovery behavior:** Withdraw/deprecate pattern, show affected uses, revert to explicit feature design and retain lesson provenance.

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

- Source/provenance/license records.
- Usage outcome and test links.
- Fit assessment rationale.
- Deprecation impact report.

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

Каждый event содержит `function_id=IDEA-090`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-090-01` — Пользователь понимает назначение Online Market Pattern Research with Source and License Policy без чтения implementation internals.
- `AC-090-02` — Функция создаёт ровно `Market Pattern Research Report` либо честный terminal report.
- `AC-090-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-090-04` — Unknowns, exclusions и blockers видимы.
- `AC-090-05` — Human authority и downstream permissions не расширены.
- `AC-090-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — User can tell when pattern does not fit.
- `AC-002` — Pattern adoption remains a separate human decision.
- `AC-003` — Every recommendation has provenance.
- `AC-004` — Failures/tests are as visible as benefits.
- `AC-005` — Deprecated version is not silently recommended.
- `AC-006` — Library remains curated rather than unlimited.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Market Pattern Research Report` для exact subject.
- Output содержит provenance, revision, status и явные limitations.
- Повторный read-only запуск на неизменном subject даёт эквивалентный результат либо объяснённую разницу.
- Human-only decision не появляется без реального human input.

### Negative and boundary tests

- Missing prerequisite не трактуется как разрешение или PASS.
- Stale/legacy source не становится current Source of Truth только из-за наличия в context.
- Scope expansion, protected operation или permission escalation блокируются и объясняются.
- Failure/partial result не маскируется статусом success.
- Presentation layer не изменяет permissions или canonical state.
- Preview/view не выглядит как approval или working implementation.

### Integration tests

- Upstream artifact revision mismatch приводит к `BLOCKED`, а не silent continuation.
- Downstream consumer принимает только explicit result schema.
- Cross-family use сохраняет один owner artifact и не создаёт conflicting copies.
- Audit trail позволяет восстановить, почему и на каком input был получен result.

## 21. Minimal implementation model — `PROPOSAL`

Repository-native Markdown/JSON pattern cards and deterministic Fit Matrix. Search can remain simple. Online research is separate and source-bound.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_090`
