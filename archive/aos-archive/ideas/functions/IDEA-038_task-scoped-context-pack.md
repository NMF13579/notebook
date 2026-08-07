---
document_id: AOS-ATOMIC-FUNCTION-IDEA-038
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-038
function_title: "Task-scoped Context Pack"
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
primary_feature_family: FTR-016
related_feature_families: [FTR-016]
human_review_required: true
---

# IDEA-038 — Task-scoped Context Pack

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Собирает минимальный task-scoped context pack из релевантных requirements, decisions, files, constraints и evidence вместо загрузки всего проекта.**

Основной наблюдаемый результат функции: **`Task-Scoped Context Pack`**.

`IDEA-038` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** User, new session/agent, task author, executor and reviewer.

Основные jobs-to-be-done:

- Ответить «на чём мы остановились?» на основании repository, а не только chat memory.
- Передать следующему agent только релевантный context.
- Сохранить decisions, blockers, candidate и next action между сессиями.
- Не создавать второй Source of Truth.
- Обнаружить stale context после repository change.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

State is scattered across chats, branches, docs and reports. Loading everything overwhelms the model; relying on chat memory misses repository changes and can carry stale authority.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-038` family flow теряет конкретный механизм «Task-scoped Context Pack», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Task-Scoped Context Pack` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- New session/agent starts.
- Stage completes or stops.
- User asks to resume.
- Task is routed to specialist/reviewer.
- Context window must be reduced.

### Preconditions

- Fact-class owners/source precedence defined.
- Repository/session subject can be verified.
- Generated memory is rebuildable.
- Sensitive sources can be excluded/redacted.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `repository_identity_and_state`
- `active_TaskBrief`
- `StageReports`
- `accepted_decisions`
- `current_candidate_and_evidence`
- `open_findings`
- `role_and_task_scope`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-038
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: TASK_SCOPED_CONTEXT_PACK
```

## 8. Пошаговое поведение

1. Связать exact source boundary, subject, revision и temporal scope.
2. Собрать только данные, необходимые для заявленной функции; exhaustive extraction не является default.
3. Классифицировать каждое наблюдение как current fact, inference, proposal, stale reference, unknown или not run.
4. Сформировать rebuildable artifact/index и явно показать gaps, conflicts и omissions.
5. Остановиться на достаточном ответе или unresolved source conflict.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Task-scoped Context Pack**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-038`.
4. Создаётся **`Task-Scoped Context Pack`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Task-Scoped Context Pack`.

Source-derived outputs:

- Project Memory record
- Session Handoff
- Task-scoped context pack
- Source/exclusion map
- Resume delta

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-038
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
UNINSPECTED → BOUNDED_COLLECTION → INDEXED | CONFLICT_FOUND | PARTIAL → REVIEW_READY | BLOCKED
```

Transition invariants:

- Human-only transition не генерируется agent output.
- Material change subject/scope инвалидирует downstream DRAFT artifacts.
- `VALIDATE` и `REVIEW` не исправляют candidate.
- Failure/unknown приводит к report + stop.
- Recovery/correction выполняются отдельным authorized stage.

## 11. UX и человекочитаемое представление

- Resume summary states last completed stage, current subject, blockers and one next action.
- Each memory item includes source owner and freshness.
- Context pack lists included and excluded sources.
- User can request details without loading everything.
- Stale/conflicting items are highlighted, not silently merged.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Task-scoped Context Pack** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-038-01` — Функция должна выполнять только следующую ответственность: Собирает минимальный task-scoped context pack из релевантных requirements, decisions, files, constraints и evidence вместо загрузки всего проекта.
- `FR-038-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-038-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-038-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-038-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-038-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Repository/current artifacts outrank prior chat summaries.
- `FR-002` — Memory record is derived and rebuildable.
- `FR-003` — Only accepted decisions retain authority; copied text does not.
- `FR-004` — Task pack contains minimum sufficient context for assigned role.
- `FR-005` — Staleness checked against repository/subject identities.
- `FR-006` — Unknown/conflict survives handoff.
- `FR-007` — Sensitive data excluded according to policy.

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

- `CTR-001` — `ProjectMemory`: project_id, source_snapshot, active_work, accepted_decisions, candidates, blockers, lessons, next_action.
- `CTR-002` — `SessionHandoff`: previous_session, completed_stage, outputs, findings, not_run, unresolved_decisions, resume_requirements.
- `CTR-003` — `ContextPack`: role, task, included_refs, excerpts_or_summaries, exclusions, freshness, authority_notes.
- `CTR-004` — `ContextPriorityPolicy`: fact_class → owner/source precedence.
- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.

## 14. Связь с feature families

- [`FTR-016` — Project Memory, Session Continuity, Context Priority and Task-Scoped Context Pack](../features/FTR-016_project-memory-session-continuity-context-priority-and-task-scoped-context-pack.md)

Primary family layer: `Product Runtime / Development Factory boundary`. Proposed disposition: `CANDIDATE`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

Memory records facts and non-grants; they do not approve or authorize. Persistence mechanism remains an architecture decision.

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

- Memory becomes duplicate Source of Truth.
- Recency overrides authority.
- Authorization survives session change.
- Context pack omits material conflict.
- Full repository/chat loaded by default.
- Derived status edited manually.

## 17. Recovery behavior

**Source-derived recovery behavior:** Discard/rebuild derived view from current sources, mark conflicting facts and require human resolution only where authority is affected.

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

- Fresh source snapshot used to rebuild memory.
- Included/excluded source map.
- Staleness/conflict checks.
- Context pack size/relevance and task outcome measurements.

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

Каждый event содержит `function_id=IDEA-038`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-038-01` — Пользователь понимает назначение Task-scoped Context Pack без чтения implementation internals.
- `AC-038-02` — Функция создаёт ровно `Task-Scoped Context Pack` либо честный terminal report.
- `AC-038-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-038-04` — Unknowns, exclusions и blockers видимы.
- `AC-038-05` — Human authority и downstream permissions не расширены.
- `AC-038-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — New agent can resume without relying on hidden chat context.
- `AC-002` — Changed HEAD/candidate marks old handoff stale.
- `AC-003` — Accepted decision provenance is preserved.
- `AC-004` — Context pack omits unrelated material.
- `AC-005` — Unknowns/blockers are not lost.
- `AC-006` — Generated memory can be deleted and rebuilt.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Task-Scoped Context Pack` для exact subject.
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

Repository-native memory/handoff documents with deterministic assembler. Use explicit source lists and summaries first; add RAG-Light only after scale/quality metrics show need.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_038`
