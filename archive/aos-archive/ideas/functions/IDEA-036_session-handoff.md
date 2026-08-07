---
document_id: AOS-ATOMIC-FUNCTION-IDEA-036
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-036
function_title: "Session Handoff"
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
primary_feature_family: FTR-014
related_feature_families: [FTR-014, FTR-016]
human_review_required: true
---

# IDEA-036 — Session Handoff

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Создаёт компактный session handoff с завершённым, незавершённым, blockers, exact subject и следующим допустимым действием.**

Основной наблюдаемый результат функции: **`Session Handoff`**.

`IDEA-036` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** User, executor, support agent and reviewer after interruption, failure or blocked action.

Основные jobs-to-be-done:

- Понять, что успело измениться до сбоя.
- Не повторить необратимую operation вслепую.
- Продолжить session с проверенного состояния.
- Выбрать resume, correction, rollback или restart.
- Сохранить denied-action reason и открытые blockers.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

Interrupted work causes recursive recovery plans, uncertain partial state, destructive cleanup or blind retries. Users cannot see what was denied and what remains safe.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-036` family flow теряет конкретный механизм «Session Handoff», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Session Handoff` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- Execution interruption or tool timeout.
- Partial install/write/Git/network result.
- Denied operation or permission boundary.
- User asks to resume after session gap.
- Candidate/repository state changed unexpectedly.

### Preconditions

- Available logs, manifests and repository state are readable.
- Recovery assessment itself is read-only.
- Known safe baselines/candidates are identifiable or UNKNOWN.
- Destructive rollback requires separate authorization.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `last_TaskBrief`
- `operation_log`
- `partial_change_manifest`
- `current_repository_state`
- `candidate_identity`
- `denied_action_records`
- `prior_handoff`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-036
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: SESSION_HANDOFF
```

## 8. Пошаговое поведение

1. Зафиксировать interruption/failure и observed partial state без mutation.
2. Определить, что можно безопасно resume, rollback, restart или оставить как есть.
3. Показать последствия и required permissions каждого recovery option.
4. Получить отдельный human choice/authorization для corrective action.
5. После correction выполнить отдельную targeted revalidation.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Session Handoff**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-036`.
4. Создаётся **`Session Handoff`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Session Handoff`.

Source-derived outputs:

- Recovery assessment
- Resume Package
- Denied Action Log
- Rollback proposal
- One next action

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-036
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
INTERRUPTED | FAILED → READ_ONLY_ASSESSMENT → RECOVERY_OPTIONS → HUMAN_CHOICE → SEPARATELY_AUTHORIZED_ACTION → REVALIDATION
```

Transition invariants:

- Human-only transition не генерируется agent output.
- Material change subject/scope инвалидирует downstream DRAFT artifacts.
- `VALIDATE` и `REVIEW` не исправляют candidate.
- Failure/unknown приводит к report + stop.
- Recovery/correction выполняются отдельным authorized stage.

## 11. UX и человекочитаемое представление

- Recovery view begins with facts: last confirmed stage, current HEAD/diff, partial effects.
- Options show risk and required authorization.
- Exactly one recommended next action is highlighted.
- Denied action explains which boundary blocked it.
- Resume summary distinguishes repository facts from chat memory.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Session Handoff** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-036-01` — Функция должна выполнять только следующую ответственность: Создаёт компактный session handoff с завершённым, незавершённым, blockers, exact subject и следующим допустимым действием.
- `FR-036-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-036-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-036-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-036-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-036-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Never assume operation succeeded because response was lost.
- `FR-002` — Re-inspect external/local state before retry.
- `FR-003` — Partial effects must be enumerated or UNKNOWN.
- `FR-004` — Resume cannot reuse stale authorization automatically.
- `FR-005` — Rollback plan states data-loss/irreversibility risk.
- `FR-006` — Recovery output does not mutate subject.
- `FR-007` — New correction requires separate Task Brief/EXECUTE.
- `FR-001` — Repository/current artifacts outrank prior chat summaries.

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

- `CTR-001` — `RecoveryAssessment`: incident, last_known_state, current_state, partial_effects, unknowns, safe_options, recommended_next_action.
- `CTR-002` — `DeniedActionRecord`: requested_action, classification, reason_code, missing_permission_or_decision, subject.
- `CTR-003` — `ResumePackage`: repository_identity, active_task, completed_stage, candidate, findings, open_decisions, delta.
- `CTR-004` — `RollbackProposal`: target_state, operations, risks, prerequisites, validation_plan, authorization_required.
- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.

## 14. Связь с feature families

- [`FTR-014` — Recovery, Resume, Rollback, Denied-Action Log and Session Handoff](../features/FTR-014_recovery-resume-rollback-denied-action-log-and-session-handoff.md)
- [`FTR-016` — Project Memory, Session Continuity, Context Priority and Task-Scoped Context Pack](../features/FTR-016_project-memory-session-continuity-context-priority-and-task-scoped-context-pack.md)

Primary family layer: `Product Runtime / Development Factory boundary`. Proposed disposition: `CANDIDATE`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

Recovery view and rollback proposal do not authorize mutation. Destructive rollback requires explicit scoped human decision.

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

- Automatic retry duplicates writes/remote actions.
- Destructive cleanup removes evidence or user work.
- Old authorization carried into new session.
- Recovery plan becomes new unbounded project.
- Stale handoff executed blindly.
- Пользователь видит terminal status, affected subject и partial effects.

## 17. Recovery behavior

**Source-derived recovery behavior:** Prefer restart-from-known-state over complex repair when cheaper and safer; preserve provenance and unrelated work; escalate unresolved state as `UNKNOWN_BLOCKED`.

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

- Fresh repository/remote state.
- Operation log and before/after manifests.
- Candidate/freeze identity.
- Prior response/authorization consumption state where available.

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

Каждый event содержит `function_id=IDEA-036`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-036-01` — Пользователь понимает назначение Session Handoff без чтения implementation internals.
- `AC-036-02` — Функция создаёт ровно `Session Handoff` либо честный terminal report.
- `AC-036-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-036-04` — Unknowns, exclusions и blockers видимы.
- `AC-036-05` — Human authority и downstream permissions не расширены.
- `AC-036-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — User sees exact partial state and unknowns.
- `AC-002` — Lost response does not trigger duplicate operation.
- `AC-003` — Safe resume detects changed HEAD/worktree.
- `AC-004` — Rollback is not executed without separate authorization.
- `AC-005` — Denied action reason is actionable.
- `AC-006` — Recovery ends with one next action and stop.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Session Handoff` для exact subject.
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

Start with read-only state reconstructor using Task/Stage Reports, Git status/diff, manifests and denied-action records. Rollback remains proposal until specific reversible operations are proven.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_036`
