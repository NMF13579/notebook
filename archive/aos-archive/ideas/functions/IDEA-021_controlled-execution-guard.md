---
document_id: AOS-ATOMIC-FUNCTION-IDEA-021
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-021
function_title: "Controlled Execution Guard"
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
primary_feature_family: FTR-010
related_feature_families: [FTR-010, FTR-020]
human_review_required: true
---

# IDEA-021 — Controlled Execution Guard

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Принудительно проверяет authorization, scope, protected operations и stop conditions непосредственно перед и во время execution.**

Основной наблюдаемый результат функции: **`Controlled Execution Guard Decision`**.

`IDEA-021` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** Authorized execution agent, maintainer and validator observing the result.

Основные jobs-to-be-done:

- Выполнить Task Brief без расширения scope.
- Не смешать EXECUTE с VALIDATE/REVIEW/Git.
- Остановиться после finding/failure/completion.
- Зафиксировать actual changes и partial effects.
- Предотвратить parallel writers и hidden retries.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

An agent can expand scope, combine stages, retry automatically, write through hidden helpers or continue after a finding. Documentation alone does not physically constrain writes.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-021` family flow теряет конкретный механизм «Controlled Execution Guard», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Controlled Execution Guard Decision` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- Complete Task Brief has explicit execution authorization.
- Correction Task Brief separately authorized.
- Bounded scaffold/document/code mutation requested.

### Preconditions

- Preflight READY and preview unchanged.
- Assigned Risk Profile and exact authorization exist.
- Allowed/forbidden paths and commands known.
- Recovery/stop conditions defined.
- No competing writer.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `authorized_TaskBrief`
- `ExecutionPreview`
- `authorization_record`
- `repository_baseline`
- `runner_kernel`
- `stop_conditions`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-021
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: CONTROLLED_EXECUTION_GUARD_DECISION
```

## 8. Пошаговое поведение

1. Проверить exact authorization, subject, repository state, scope и protected-operation gates.
2. Выполнить только заранее объявленные operations в bounded environment.
3. Записывать progress, side effects, denied actions и partial state.
4. На failure/unknown немедленно остановиться без automatic retry или scope expansion.
5. Выпустить result/report; последующая validation выполняется отдельным stage.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Controlled Execution Guard**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-021`.
4. Создаётся **`Controlled Execution Guard Decision`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Controlled Execution Guard Decision`.

Source-derived outputs:

- Changed artifact(s)
- Actual change manifest
- Execution log/result envelope
- Targeted check results
- Stage Report

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-021
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
AUTHORIZATION_BOUND → PRECHECK → RUNNING → SUCCEEDED | FAILED | PARTIAL | DENIED → REPORT_EMITTED → STOP
```

Transition invariants:

- Human-only transition не генерируется agent output.
- Material change subject/scope инвалидирует downstream DRAFT artifacts.
- `VALIDATE` и `REVIEW` не исправляют candidate.
- Failure/unknown приводит к report + stop.
- Recovery/correction выполняются отдельным authorized stage.

## 11. UX и человекочитаемое представление

- Перед mutation показывается preview identity and authorization scope.
- Progress reports only material milestones, not misleading percent completion.
- Any finding produces immediate stop reason and partial-state summary.
- Final report states changed paths, checks, NOT_RUN, limitations and one next action.
- No automatic prompt for next stage.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Controlled Execution Guard** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-021-01` — Функция должна выполнять только следующую ответственность: Принудительно проверяет authorization, scope, protected operations и stop conditions непосредственно перед и во время execution.
- `FR-021-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-021-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-021-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-021-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-021-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Executor may mutate only declared subject and paths.
- `FR-002` — One writer lock/session binding prevents concurrent writes.
- `FR-003` — Every operation logged with outcome and affected path/subject.
- `FR-004` — Unexpected effect or scope drift triggers stop.
- `FR-005` — Retries require explicit idempotent policy or new task; no blind automatic retry.
- `FR-006` — Inline checks may diagnose known cause but cannot become independent VALIDATE.
- `FR-007` — Terminal report is emitted on every exit path.
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

- `CTR-001` — `ExecutionSession`: session_id, task_id, subject, baseline, preview_id, authorization_id, writer_identity.
- `CTR-002` — `OperationResult`: operation_id, planned, actual, status, affected_subject, side_effects, error.
- `CTR-003` — `ChangeManifest`: created, modified, deleted, unchanged, unexpected.
- `CTR-004` — `StageReport`: terminal_status, findings, partial_effects, checks, not_run, next_required_action.
- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.

## 14. Связь с feature families

- [`FTR-010` — Scoped Execution Workflow, Controlled Guard and Safe Runner Kernels](../features/FTR-010_scoped-execution-workflow-controlled-guard-and-safe-runner-kernels.md)
- [`FTR-020` — Runtime Enforcement, Isolated Execution Environment and Progressive Governance Modes](../features/FTR-020_runtime-enforcement-isolated-execution-environment-and-progressive-governance-modes.md)

Primary family layer: `Development Factory`. Proposed disposition: `CANDIDATE`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

Only explicit human execution authorization permits mutation. Commit/push/merge/release remain separate.

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

- Hidden scope expansion.
- Automatic retry or next-stage transition.
- Architecture/dependency change during execution.
- Parallel writers or unrecorded side effects.
- Guard validates its own unsafe assumptions.
- Generated report changes frozen candidate.

## 17. Recovery behavior

**Source-derived recovery behavior:** Stop immediately, preserve state, classify partial effects and hand off to FTR-014. Correction is a new authorized EXECUTE; validation never patches the artifact.

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

- Session/authorization binding.
- Operation log and actual change manifest.
- Working tree/diff before and after.
- Single-writer and stop-condition checks.

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

Каждый event содержит `function_id=IDEA-021`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-021-01` — Пользователь понимает назначение Controlled Execution Guard без чтения implementation internals.
- `AC-021-02` — Функция создаёт ровно `Controlled Execution Guard Decision` либо честный terminal report.
- `AC-021-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-021-04` — Unknowns, exclusions и blockers видимы.
- `AC-021-05` — Human authority и downstream permissions не расширены.
- `AC-021-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — Only in-scope paths change.
- `AC-002` — No next stage starts automatically.
- `AC-003` — Every failure emits machine/human terminal result.
- `AC-004` — Parallel write attempt is blocked.
- `AC-005` — Unexpected diff stops execution.
- `AC-006` — Actual changes can be independently validated later.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Controlled Execution Guard Decision` для exact subject.
- Output содержит provenance, revision, status и явные limitations.
- Повторный read-only запуск на неизменном subject даёт эквивалентный результат либо объяснённую разницу.
- Human-only decision не появляется без реального human input.

### Negative and boundary tests

- Missing prerequisite не трактуется как разрешение или PASS.
- Stale/legacy source не становится current Source of Truth только из-за наличия в context.
- Scope expansion, protected operation или permission escalation блокируются и объясняются.
- Failure/partial result не маскируется статусом success.
- Команда вне allowlist не выполняется.
- Повтор после unknown/timeout не запускается автоматически.

### Integration tests

- Upstream artifact revision mismatch приводит к `BLOCKED`, а не silent continuation.
- Downstream consumer принимает только explicit result schema.
- Cross-family use сохраняет один owner artifact и не создаёт conflicting copies.
- Audit trail позволяет восстановить, почему и на каком input был получен result.

## 21. Minimal implementation model — `PROPOSAL`

Initially use narrow task-specific runners or direct bounded tools with wrapper logging, not a generalized autonomous executor. Physical enforcement belongs to FTR-020 later.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_021`
