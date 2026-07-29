---
document_id: AOS-ATOMIC-FUNCTION-IDEA-029
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-029
function_title: "Diff and Scope Reconciliation"
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
primary_feature_family: FTR-013
related_feature_families: [FTR-013]
human_review_required: true
---

# IDEA-029 — Diff and Scope Reconciliation

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Сопоставляет фактический diff и observed effects с authorized scope, выявляя лишние, отсутствующие или необъяснённые изменения.**

Основной наблюдаемый результат функции: **`Diff / Scope Reconciliation Report`**.

`IDEA-029` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** Executor, validator, reviewer and Git/release authorizer.

Основные jobs-to-be-done:

- Убедиться, что проверяется именно созданный candidate.
- Не потерять untracked/generated files из фактического diff.
- Отделить executor worktree от validator subject.
- Получить stable identity до REVIEW/Git.
- Обнаружить self-reference и provisional package identity.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

Validation may run against a moving worktree, omit untracked files, import a different package or bind evidence to a provisional/self-referential identity.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-029` family flow теряет конкретный механизм «Diff and Scope Reconciliation», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Diff / Scope Reconciliation Report` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- EXECUTE completes and candidate is ready for VALIDATE.
- Review/Git operation requires exact subject.
- Generated package has manifest/hash identity.
- Prior validation may have run on wrong checkout/import.

### Preconditions

- Task Brief planned scope known.
- Executor reports actual operations.
- Candidate can be materialized or snapshot.
- Temporary subject location is isolated and disposable.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `planned_scope`
- `actual_worktree_state`
- `operation_log`
- `candidate_artifacts`
- `identity_policy`
- `validation_profile`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-029
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: DIFF_SCOPE_RECONCILIATION_REPORT
```

## 8. Пошаговое поведение

1. Привязать проверку к exact immutable subject, baseline и expected contract.
2. Выполнить targeted positive, negative и boundary checks без исправления subject.
3. Собрать machine-readable result, Evidence и limitations.
4. Отличить PASS, FAIL, BLOCKED, NOT_RUN и UNKNOWN; не конвертировать их в approval.
5. Выпустить report и остановиться; correction требует отдельного EXECUTE.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Diff and Scope Reconciliation**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-029`.
4. Создаётся **`Diff / Scope Reconciliation Report`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Diff / Scope Reconciliation Report`.

Source-derived outputs:

- Scope reconciliation report
- Frozen candidate identity
- Disposable subject
- Provenance report
- Drift detection result

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-029
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
SUBJECT_BOUND → CHECKING → PASS | FAIL | BLOCKED | NOT_RUN → REPORT_EMITTED → STOP
```

Transition invariants:

- Human-only transition не генерируется agent output.
- Material change subject/scope инвалидирует downstream DRAFT artifacts.
- `VALIDATE` и `REVIEW` не исправляют candidate.
- Failure/unknown приводит к report + stop.
- Recovery/correction выполняются отдельным authorized stage.

## 11. UX и человекочитаемое представление

- Report shows planned vs actual paths and unexplained changes.
- Frozen identity is displayed in review/Git cards.
- Validator indicates source path, import provenance and environment.
- Any post-freeze mutation prominently invalidates results.
- Temporary subject cleanup occurs only after evidence is retained.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Diff and Scope Reconciliation** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-029-01` — Функция должна выполнять только следующую ответственность: Сопоставляет фактический diff и observed effects с authorized scope, выявляя лишние, отсутствующие или необъяснённые изменения.
- `FR-029-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-029-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-029-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-029-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-029-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Include tracked, untracked, generated and deleted artifacts.
- `FR-002` — No unexplained actual change may be silently excluded.
- `FR-003` — Candidate identity must be non-self-referential and reproducible.
- `FR-004` — Validation subject must be read-only or mutation-detecting.
- `FR-005` — Validator must not import from unintended checkout.
- `FR-006` — Freeze occurs after execution and before independent validation.
- `FR-007` — Changed candidate requires new validation/review.

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

- `CTR-001` — `ScopeReconciliation`: planned_paths, actual_paths, unexplained, excluded_noise, disposition.
- `CTR-002` — `CandidateIdentity`: candidate_id, content_digest, constituent_files, baseline, created_at, identity_policy.
- `CTR-003` — `ValidationSubject`: source_candidate, materialization_path, readonly_controls, environment_identity.
- `CTR-004` — `FreezeAudit`: pre_digest, post_digest, mutation_events, status.
- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.

## 14. Связь с feature families

- [`FTR-013` — Diff/Scope Reconciliation, Disposable Validation Subject and Immutable Candidate Freeze](../features/FTR-013_diff-scope-reconciliation-disposable-validation-subject-and-immutable-candidate-freeze.md)

Primary family layer: `Development Factory / Validation boundary`. Proposed disposition: `CANDIDATE`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

Freeze proves identity, not correctness or approval. Temporary subjects are not canonical state.

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

- Untracked in-scope file omitted.
- Candidate identity includes its own hash/report.
- Validation imports live checkout.
- Validator modifies candidate.
- Stale baseline or provisional tree used.
- Out-of-scope change accepted as incidental.

## 17. Recovery behavior

**Source-derived recovery behavior:** Any deviation or drift returns to a separately authorized correction EXECUTE, followed by new freeze and separate VALIDATE. Never patch disposable subject.

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

- Git/filesystem inventory including untracked.
- Candidate manifest and digest reproduction.
- Disposable subject creation log.
- Pre/post validation digest and import provenance.

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

Каждый event содержит `function_id=IDEA-029`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-029-01` — Пользователь понимает назначение Diff and Scope Reconciliation без чтения implementation internals.
- `AC-029-02` — Функция создаёт ровно `Diff / Scope Reconciliation Report` либо честный terminal report.
- `AC-029-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-029-04` — Unknowns, exclusions и blockers видимы.
- `AC-029-05` — Human authority и downstream permissions не расширены.
- `AC-029-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — Another validator can reconstruct the same subject.
- `AC-002` — Untracked files are included or explicitly excluded with reason.
- `AC-003` — Write-after-freeze is detected.
- `AC-004` — Self-referential manifest is rejected.
- `AC-005` — Evidence references frozen identity.
- `AC-006` — Wrong import/source path fails validation.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Diff / Scope Reconciliation Report` для exact subject.
- Output содержит provenance, revision, status и явные limitations.
- Повторный read-only запуск на неизменном subject даёт эквивалентный результат либо объяснённую разницу.
- Human-only decision не появляется без реального human input.

### Negative and boundary tests

- Missing prerequisite не трактуется как разрешение или PASS.
- Stale/legacy source не становится current Source of Truth только из-за наличия в context.
- Scope expansion, protected operation или permission escalation блокируются и объясняются.
- Failure/partial result не маскируется статусом success.
- Validator не исправляет candidate.
- `NOT_RUN` не конвертируется в PASS.

### Integration tests

- Upstream artifact revision mismatch приводит к `BLOCKED`, а не silent continuation.
- Downstream consumer принимает только explicit result schema.
- Cross-family use сохраняет один owner artifact и не создаёт conflicting copies.
- Audit trail позволяет восстановить, почему и на каком input был получен result.

## 21. Minimal implementation model — `PROPOSAL`

Use filesystem/Git snapshot or archive plus strict manifest and digest policy. Disposable copy/worktree/temporary package can be selected per accepted architecture; keep mechanism replaceable.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_029`
