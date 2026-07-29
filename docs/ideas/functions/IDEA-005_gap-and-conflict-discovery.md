---
document_id: AOS-ATOMIC-FUNCTION-IDEA-005
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-005
function_title: "Gap and Conflict Discovery"
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
primary_feature_family: FTR-002
related_feature_families: [FTR-002]
human_review_required: true
---

# IDEA-005 — Gap and Conflict Discovery

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Находит отсутствующие элементы, противоречия, stale claims и competing owners, фиксируя impact и требуемый способ разрешения без самостоятельного выбора Source of Truth.**

Основной наблюдаемый результат функции: **`Gap and Conflict Register`**.

`IDEA-005` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** Product owner, maintainer, architect, agent entering a new or legacy repository.

Основные jobs-to-be-done:

- Быстро понять незнакомый repository до постановки изменения.
- Отделить реально наблюдаемое поведение от design docs и historical claims.
- Найти owners, contracts, commands, tests и зависимости, относящиеся к конкретной feature.
- Показать gaps, conflicting sources и stale paths без преждевременного исправления.
- Подготовить компактный context для Product Brief или Task Brief.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

Человек и агент не знают фактическую структуру проекта, текущие capabilities, owners, contracts, commands и conflicts. Широкий scan легко выглядит как полная architecture assessment, хотя факты могут быть устаревшими.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-005` family flow теряет конкретный механизм «Gap and Conflict Discovery», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Gap and Conflict Register` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- Работа начинается в existing project.
- Feature затрагивает незнакомую область repository.
- Документы, code и tests расходятся.
- Требуется восстановить capability для clean-room reimplementation.

### Preconditions

- Exact subject и разрешённый source boundary определены.
- Read-only local access подтверждён; remote/network access запрашивается отдельно.
- Repository preflight возможен либо его отсутствие объявлено BLOCKED/NOT_RUN.
- Исследование привязано к конкретному вопросу или feature.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `repository_identity`
- `worktree_path`
- `expected_branch`
- `feature_or_question_scope`
- `allowed_paths`
- `known_source_pack`
- `baseline_expectation`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-005
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: GAP_AND_CONFLICT_REGISTER
```

## 8. Пошаговое поведение

1. Связать exact source boundary, subject, revision и temporal scope.
2. Собрать только данные, необходимые для заявленной функции; exhaustive extraction не является default.
3. Классифицировать каждое наблюдение как current fact, inference, proposal, stale reference, unknown или not run.
4. Сформировать rebuildable artifact/index и явно показать gaps, conflicts и omissions.
5. Остановиться на достаточном ответе или unresolved source conflict.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Gap and Conflict Discovery**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-005`.
4. Создаётся **`Gap and Conflict Register`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Gap and Conflict Register`.

Source-derived outputs:

- Repository preflight
- Capability Map
- Gap/Conflict Register
- Source inventory subset
- Research limitations

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-005
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

- Сначала показывается identity card: repository, worktree, branch, HEAD, dirty state и scope.
- Каждая capability имеет ярлык OBSERVED | DOCUMENTED_ONLY | HISTORICAL | BROKEN | UNKNOWN.
- Gaps группируются по влиянию на текущую feature, а не по количеству файлов.
- Пользователь видит отдельный список «не проверено» и не принимает отсутствие finding за PASS.
- Основной результат помещается в краткую карту; raw paths и команды доступны в details.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Gap and Conflict Discovery** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-005-01` — Функция должна выполнять только следующую ответственность: Находит отсутствующие элементы, противоречия, stale claims и competing owners, фиксируя impact и требуемый способ разрешения без самостоятельного выбора Source of Truth.
- `FR-005-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-005-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-005-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-005-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-005-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Не продолжать scan, если exact subject не подтверждён.
- `FR-002` — Фиксировать repository state перед чтением и повторно проверять его при длительном исследовании.
- `FR-003` — Каждое утверждение о capability связывать минимум с одним evidence locator.
- `FR-004` — Различать отсутствие файла, отсутствие поиска и отсутствие capability.
- `FR-005` — Не делать current claim из historical source без temporal verification.
- `FR-006` — Останавливать исследование при достаточном ответе; не расширять scope ради полноты.
- `FR-007` — Конфликтующие owners/Source-of-Truth claims выводить как HUMAN_REVIEW_REQUIRED.

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

- `CTR-001` — `DiscoverySubject`: repository, worktree, branch, head, baseline, dirty_state_digest, inspected_at.
- `CTR-002` — `CapabilityObservation`: capability_id, classification, evidence_refs, temporal_scope, confidence, limitations.
- `CTR-003` — `GapRecord`: gap_id, affected_feature, missing_or_conflicting_fact, impact, resolution_mode, severity.
- `CTR-004` — `DiscoveryReport`: scope, included_paths, excluded_paths, commands_run, NOT_RUN, findings, next_required_action.
- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.

## 14. Связь с feature families

- [`FTR-002` — Project Discovery, Capability Map, Gap and Conflict Discovery](../features/FTR-002_project-discovery-capability-map-gap-and-conflict-discovery.md)

Primary family layer: `Product Runtime`. Proposed disposition: `CANDIDATE`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

Read-only. Discovery evidence не является approval, current readiness или architecture decision.

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

- Scan объявляется complete architecture.
- Metadata recency подменяет content recency.
- Legacy design считается implemented capability.
- Discovery расширяется на весь repository без необходимости.
- Conflicting sources silently merged.
- Пользователь видит terminal status, affected subject и partial effects.

## 17. Recovery behavior

**Source-derived recovery behavior:** Сузить scope, пометить affected claim `UNKNOWN_BLOCKED`/`HUMAN_REVIEW_REQUIRED`, указать exact missing source or conflict; не выбирать победивший Source of Truth самостоятельно.

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

- Git/repository preflight output.
- Path/line/command locators for each observation.
- List of search terms and excluded areas.
- Current-vs-historical classification rationale.
- Digest or timestamp proving which repository state was inspected.

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

Каждый event содержит `function_id=IDEA-005`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-005-01` — Пользователь понимает назначение Gap and Conflict Discovery без чтения implementation internals.
- `AC-005-02` — Функция создаёт ровно `Gap and Conflict Register` либо честный terminal report.
- `AC-005-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-005-04` — Unknowns, exclusions и blockers видимы.
- `AC-005-05` — Human authority и downstream permissions не расширены.
- `AC-005-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — Другой агент может воспроизвести, где был найден каждый material fact.
- `AC-002` — Capability Map не смешивает design-only и implemented behavior.
- `AC-003` — Wrong branch/HEAD или changed subject обнаруживаются.
- `AC-004` — Untracked/dirty state классифицирован, а не автоматически скрыт или объявлен blocker.
- `AC-005` — Каждый gap имеет impact и next resolution mode.
- `AC-006` — Report не утверждает architecture completeness.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Gap and Conflict Register` для exact subject.
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

Минимальная реализация — local Git/filesystem adapters, Markdown/JSON report builder и набор явных classifiers. Graph DB и semantic indexing не нужны; сначала важны provenance и honest limitations.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_005`
