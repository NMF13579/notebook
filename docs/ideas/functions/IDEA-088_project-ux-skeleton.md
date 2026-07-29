---
document_id: AOS-ATOMIC-FUNCTION-IDEA-088
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-088
function_title: "Project UX Skeleton"
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
primary_feature_family: FTR-031
related_feature_families: [FTR-031]
human_review_required: true
---

# IDEA-088 — Project UX Skeleton

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Строит Project UX Skeleton из requirements: actors, journeys, screens, elements, states, navigation, permissions, edge cases и provenance.**

Основной наблюдаемый результат функции: **`Project UX Skeleton`**.

`IDEA-088` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** Product owner, UX/product designer, non-programmer founder, architect, developer and reviewer.

Основные jobs-to-be-done:

- Увидеть interaction model до написания кода.
- Проверить actors, journeys, pages, states, transitions, permissions и failure paths.
- Обнаружить missing/unreachable/uncovered UX objects.
- Выбрать smallest useful vertical slice.
- Не допустить drift между requirement, design, task, code и test.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

A specification can jump directly to code without a reviewable interaction model. Pages, states, permissions, failure paths and requirement coverage are discovered late; visual tools may become untraceable design sources.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-088` family flow теряет конкретный механизм «Project UX Skeleton», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Project UX Skeleton` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- Specification includes user interaction.
- Implementation would otherwise jump directly to UI code.
- Existing UX/code drift needs reconstruction.
- Vertical slice selection requires interaction coverage.

### Preconditions

- Specification and accepted architecture constraints.
- Roles/permissions and domain boundaries known enough.
- Human review available.
- Pattern/market sources treated as advisory.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `accepted_or_reviewable_specification`
- `architecture_constraints`
- `actors_roles_permissions`
- `requirements_and_acceptance_expectations`
- `pattern_library_refs`
- `optional_market_research`
- `existing_ui_observations`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-088
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: PROJECT_UX_SKELETON
```

## 8. Пошаговое поведение

1. Получить canonical context и exact user-facing subject.
2. Сформировать human-readable view/artifact, не меняя underlying facts и permissions.
3. Показать states, edge cases, blockers, provenance и available actions.
4. Провести structural/human review и записать только явно принятый scope.
5. Не выдавать preview, mode или visual direction за working implementation/approval.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Project UX Skeleton**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-088`.
4. Создаётся **`Project UX Skeleton`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Project UX Skeleton`.

Source-derived outputs:

- Project UX Skeleton
- Actors/journeys/pages/states/navigation/access artifacts
- Coverage and validation report
- Human review package
- Vertical-slice candidates
- Task Brief bridge
- Code/Evidence trace map

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-088
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

- Skeleton is readable as journeys/pages/states, not only graph/json.
- Every page/state shows actor, entry, exit, permissions and failure behavior.
- Coverage report highlights orphan requirements and unreachable states.
- Pattern/market suggestions visibly remain advisory with provenance/license.
- Selected slice shows exact included journey and excluded future states.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Project UX Skeleton** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-088-01` — Функция должна выполнять только следующую ответственность: Строит Project UX Skeleton из requirements: actors, journeys, screens, elements, states, navigation, permissions, edge cases и provenance.
- `FR-088-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-088-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-088-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-088-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-088-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Every UX object has stable ID and source requirement.
- `FR-002` — Loading/empty/error/permission/offline/success states modeled where relevant.
- `FR-003` — Navigation graph and access matrix validated.
- `FR-004` — Generated UX cannot invent accepted requirement silently.
- `FR-005` — Human decision required before slice/task/code progression.
- `FR-006` — Trace chain maintained through code/test/Evidence.
- `FR-007` — Drift invalidates affected slice/task and requires review.

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

- `CTR-001` — `UXSkeleton`: actors, journeys, views, elements, states, transitions, access_rules, requirement_refs, version.
- `CTR-002` — `UXValidationReport`: missing_refs, unreachable_nodes, uncovered_requirements, invalid_transitions, accessibility/security_gaps.
- `CTR-003` — `UXReviewDecision`: ACCEPT | MODIFY | REJECT | DEFER; exact skeleton version.
- `CTR-004` — `VerticalSlice`: journey_fragment, UX_objects, requirements, non_goals, dependencies, acceptance.
- `CTR-005` — `TraceMap`: requirement → UX object → slice → task → code locator → test/Evidence.
- UTF-8; stable IDs; explicit enums.

## 14. Связь с feature families

- [`FTR-031` — Project UX Skeleton → Human Review → Vertical Slices → Task Briefs → Code](../features/FTR-031_project-ux-skeleton-to-human-review-to-vertical-slices-to-task-briefs-to-code.md)

Primary family layer: `Product Runtime / Documentation-to-Code bridge`. Proposed disposition: `CANDIDATE`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

Working synthesis ID introduced in this document; not canonical. MVP excludes full Figma editor, full-app codegen, automatic design system, autonomous online scraping, runtime enforcement and visual regression platform.

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

- Skeleton becomes pretty sitemap without behavior/states.
- Generated UI invents requirements.
- Pattern/market reference becomes accepted design silently.
- Skeleton and code drift.
- Full app code generated before slice authorization.
- Accessibility/security/error states omitted.

## 17. Recovery behavior

**Source-derived recovery behavior:** Return skeleton to DRAFT, show uncovered requirement/unreachable state/drift, invalidate affected slice/task and require revised human review before new code execution.

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

- Specification-to-UX coverage.
- Structural/navigation/access validation.
- Human review record.
- Slice/task/code/test trace and drift checks.
- Pattern/market provenance and license notes.

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

Каждый event содержит `function_id=IDEA-088`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-088-01` — Пользователь понимает назначение Project UX Skeleton без чтения implementation internals.
- `AC-088-02` — Функция создаёт ровно `Project UX Skeleton` либо честный terminal report.
- `AC-088-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-088-04` — Unknowns, exclusions и blockers видимы.
- `AC-088-05` — Human authority и downstream permissions не расширены.
- `AC-088-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — Every in-scope requirement maps to UX object or explicit non-UX rationale.
- `AC-002` — No unreachable/orphan critical view/state.
- `AC-003` — Failure/accessibility/security states covered.
- `AC-004` — Human reviews exact skeleton version.
- `AC-005` — Selected slice is independently testable and user-visible.
- `AC-006` — Code/tests trace back without hidden full-app expansion.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Project UX Skeleton` для exact subject.
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

Start as Markdown/JSON UX model, deterministic assembler/validator and trace map. Optional diagrams/Figma export are projections. Code generation limited to one authorized slice.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_088`
