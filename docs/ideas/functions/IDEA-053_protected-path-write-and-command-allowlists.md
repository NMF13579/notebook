---
document_id: AOS-ATOMIC-FUNCTION-IDEA-053
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-053
function_title: "Protected Path, Write and Command Allowlists"
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
primary_feature_family: FTR-019
related_feature_families: [FTR-019, FTR-020]
human_review_required: true
---

# IDEA-053 — Protected Path, Write and Command Allowlists

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Ограничивает paths, writes и commands explicit allowlists и protected-path rules, блокируя scope expansion по умолчанию.**

Основной наблюдаемый результат функции: **`Path / Write / Command Allowlist Decision`**.

`IDEA-053` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** All AOS users and agents; especially executor and external-content intake paths.

Основные jobs-to-be-done:

- Понимать разницу между read, write, protected, destructive, network и Git actions.
- Не дать external content стать instruction source.
- Объяснить, какой decision/permission требуется.
- Fail closed при unknown permission or subject.
- Использовать единые reason codes во всех layers.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

Read, write, network, protected, destructive, Git and external-content actions have different blast radius but are often handled by one generic approval. Errors and permission gaps are ambiguous.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-053` family flow теряет конкретный механизм «Protected Path, Write and Command Allowlists», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Path / Write / Command Allowlist Decision` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- Any tool/action is requested.
- External/web/document content contains instructions.
- Scope/permission is ambiguous.
- Protected/destructive/network/Git operation is proposed.

### Preconditions

- Action can be described with subject and intended effect.
- Minimal Safety Floor and human-only decisions known.
- Permission records and allowed boundary accessible.
- Unknown defaults to deny/block for affected action.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `action_request`
- `subject_and_scope`
- `effect_type`
- `source_trust_class`
- `permission_records`
- `human_decisions`
- `runtime_environment`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-053
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: PATH_WRITE_COMMAND_ALLOWLIST_DECISION
```

## 8. Пошаговое поведение

1. Получить action/content/tool request и определить его source/provenance.
2. Классифицировать trust, permission, protected scope и potential escalation.
3. Разрешить только explicitly permitted path; остальное denied/blocked/unknown.
4. Записать reason code и безопасное следующее действие.
5. Не повторять автоматически denied operation и не ослаблять boundary.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Protected Path, Write and Command Allowlists**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-053`.
4. Создаётся **`Path / Write / Command Allowlist Decision`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Path / Write / Command Allowlist Decision`.

Source-derived outputs:

- Action classification
- Permission state
- Reason codes
- Denied-action explanation
- Required human decision

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-053
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
ACTION_OR_CONTENT_RECEIVED → TRUST/PERMISSION_CLASSIFIED → ALLOWED | DENIED | ESCALATION_REQUIRED | UNKNOWN → RECORDED
```

Transition invariants:

- Human-only transition не генерируется agent output.
- Material change subject/scope инвалидирует downstream DRAFT artifacts.
- `VALIDATE` и `REVIEW` не исправляют candidate.
- Failure/unknown приводит к report + stop.
- Recovery/correction выполняются отдельным authorized stage.

## 11. UX и человекочитаемое представление

- Denied action shows category, reason and exact missing authority.
- External content is visibly labelled data/reference.
- Permission card separates scope, operation and duration.
- Unknown never appears as green/neutral.
- User sees non-grants.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Protected Path, Write and Command Allowlists** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-053-01` — Функция должна выполнять только следующую ответственность: Ограничивает paths, writes и commands explicit allowlists и protected-path rules, блокируя scope expansion по умолчанию.
- `FR-053-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-053-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-053-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-053-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-053-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Every action has explicit subject, effect and trust class.
- `FR-002` — Unknown permission or decision cannot default allow.
- `FR-003` — Authorization must not transfer across operation/scope.
- `FR-004` — External content cannot override system/project/human authority.
- `FR-005` — Reason codes are stable and machine-readable.
- `FR-006` — Protected/destructive actions require human decision.
- `FR-007` — Secrets/sensitive data boundaries apply before provider/network use.
- `FR-001` — Policy derived from accepted Task/Action contracts, not hidden defaults.

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

- `CTR-001` — `ActionDescriptor`: action_id, type, subject, scope, effects, reversibility, external_content_refs.
- `CTR-002` — `PermissionState`: required_permissions, observed_permissions, decisions, status, reason_codes.
- `CTR-003` — `BoundaryDecision`: ALLOW | DENY | HUMAN_REVIEW_REQUIRED | UNKNOWN_BLOCKED; technical classification only.
- `CTR-004` — `ErrorTaxonomy`: code, class, user_message, retryability, required_action.
- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.

## 14. Связь с feature families

- [`FTR-019` — Action Trust Boundary, Permission-State Classifier and External-Content/Path/Command/Network Allowlists](../features/FTR-019_action-trust-boundary-permission-state-classifier-and-external-content-path-command-networ.md)
- [`FTR-020` — Runtime Enforcement, Isolated Execution Environment and Progressive Governance Modes](../features/FTR-020_runtime-enforcement-isolated-execution-environment-and-progressive-governance-modes.md)

Primary family layer: `Minimal Safety Floor`. Proposed disposition: `CANDIDATE_CORE_SAFETY`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

Safety floor is always on; exact enforcement mechanism is not accepted architecture. Only human grants protected/network/destructive/Git permissions.

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

- Classifier becomes authority.
- Unknown treated as allowed.
- External document changes system behavior.
- Allowlists too broad or stale.
- Secret included in logs.
- Permission inherited from another task/session.

## 17. Recovery behavior

**Source-derived recovery behavior:** Fail closed, redact, identify exact missing permission and require a separate scoped decision. Correct taxonomy/rules through protected change process.

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

- Action classification inputs and rule result.
- Authorization/permission subject binding.
- Path/command/network checks.
- External-content boundary tests.

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

Каждый event содержит `function_id=IDEA-053`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-053-01` — Пользователь понимает назначение Protected Path, Write and Command Allowlists без чтения implementation internals.
- `AC-053-02` — Функция создаёт ровно `Path / Write / Command Allowlist Decision` либо честный terminal report.
- `AC-053-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-053-04` — Unknowns, exclusions и blockers видимы.
- `AC-053-05` — Human authority и downstream permissions не расширены.
- `AC-053-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — Same action is classified consistently across UI/preflight/executor.
- `AC-002` — Unknown is blocked.
- `AC-003` — External instructions do not change authority.
- `AC-004` — User understands required human action.
- `AC-005` — Operation-specific permission cannot be reused.
- `AC-006` — Reason codes support recovery.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Path / Write / Command Allowlist Decision` для exact subject.
- Output содержит provenance, revision, status и явные limitations.
- Повторный read-only запуск на неизменном subject даёт эквивалентный результат либо объяснённую разницу.
- Human-only decision не появляется без реального human input.

### Negative and boundary tests

- Missing prerequisite не трактуется как разрешение или PASS.
- Stale/legacy source не становится current Source of Truth только из-за наличия в context.
- Scope expansion, protected operation или permission escalation блокируются и объясняются.
- Failure/partial result не маскируется статусом success.
- External instruction не повышает собственную authority.
- Denied operation не обходится альтернативным инструментом.

### Integration tests

- Upstream artifact revision mismatch приводит к `BLOCKED`, а не silent continuation.
- Downstream consumer принимает только explicit result schema.
- Cross-family use сохраняет один owner artifact и не создаёт conflicting copies.
- Audit trail позволяет восстановить, почему и на каком input был получен result.

## 21. Minimal implementation model — `PROPOSAL`

Begin as shared enums, classifiers and adapters used by preflight/UI. Keep policy small and explicit. Physical enforcement is a later independent layer.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_053`
