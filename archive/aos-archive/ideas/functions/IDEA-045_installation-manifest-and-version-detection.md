---
document_id: AOS-ATOMIC-FUNCTION-IDEA-045
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-045
function_title: "Installation Manifest and Version Detection"
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
primary_feature_family: FTR-004
related_feature_families: [FTR-004]
human_review_required: true
---

# IDEA-045 — Installation Manifest and Version Detection

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Ведёт installation manifest, ownership и version detection, позволяя отличать installed, mixed, stale и unknown package state.**

Основной наблюдаемый результат функции: **`Installation Manifest and Version Report`**.

`IDEA-045` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** Project owner adopting AOS, maintainer, installation agent and first-time user.

Основные jobs-to-be-done:

- Создать greenfield scaffold без копирования legacy complexity.
- Подключить AOS к существующему project без silent overwrite.
- Понять, какие файлы принадлежат installer, пользователю и shared ownership.
- Безопасно выполнить update, repair или uninstall.
- Дать новичку первый понятный маршрут после установки.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

Установка или scaffold может silently overwrite root files, копировать legacy complexity, создавать неверную project boundary или смешивать AOS product files с target-project data.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-045` family flow теряет конкретный механизм «Installation Manifest and Version Detection», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Installation Manifest and Version Report` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- Новый AOS repository создаётся с нуля.
- AOS package подключается к existing target repository.
- Требуется update, repair, migration или uninstall.
- First-start diagnosis показывает неполную установку.

### Preconditions

- Repository/worktree/branch/HEAD проверены.
- Target boundary и install mode выбраны человеком.
- Package/template version известна.
- Write/network permissions и allowed paths явны.
- Backup/recovery conditions определены.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `target_repository`
- `operation_type`
- `package_or_template_identity`
- `install_profile`
- `existing_file_inventory`
- `ownership_policy`
- `authorization_record`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-045
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: INSTALLATION_MANIFEST_AND_VERSION_REPORT
```

## 8. Пошаговое поведение

1. Подтвердить target repository/worktree/branch/HEAD и ownership model.
2. Построить deterministic file plan и выявить conflicts до mutation.
3. Получить отдельную authorization на exact apply/update/remove operation.
4. Выполнить idempotent operation с manifest/journal и preservation user-owned data.
5. Запустить doctor/self-test и выдать recovery path при partial result.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Installation Manifest and Version Detection**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-045`.
4. Создаётся **`Installation Manifest and Version Report`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Installation Manifest and Version Report`.

Source-derived outputs:

- Install/scaffold plan
- Ownership manifest
- Materialized minimal structure
- Verification report
- Manual conflict instructions

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-045
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
TARGET_BOUND → PLAN_READY → CONFLICTED | READY → APPLYING → INSTALLED | PARTIAL | FAILED → DOCTOR → STOP
```

Transition invariants:

- Human-only transition не генерируется agent output.
- Material change subject/scope инвалидирует downstream DRAFT artifacts.
- `VALIDATE` и `REVIEW` не исправляют candidate.
- Failure/unknown приводит к report + stop.
- Recovery/correction выполняются отдельным authorized stage.

## 11. UX и человекочитаемое представление

- Preview показывает exact create/modify/skip/conflict operations.
- Каждый conflict получает manual resolution instruction; overwrite никогда не скрыт.
- После apply пользователь видит, что изменилось, что осталось untouched и как откатить.
- FIRST-START содержит не более нескольких безопасных команд/действий.
- Scaffold описывает границу Product Runtime vs Development Factory.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Installation Manifest and Version Detection** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-045-01` — Функция должна выполнять только следующую ответственность: Ведёт installation manifest, ownership и version detection, позволяя отличать installed, mixed, stale и unknown package state.
- `FR-045-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-045-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-045-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-045-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-045-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Dry-run не должен иметь side effects и обязан быть repeatable.
- `FR-002` — Apply привязывается к неизменившемуся preview/baseline.
- `FR-003` — Installer не пишет за пределами allowed paths, включая symlink escapes.
- `FR-004` — Owned, shared и user-owned files различаются в manifest.
- `FR-005` — Update сохраняет local modifications либо останавливается с conflict.
- `FR-006` — Uninstall удаляет только доказанно owned assets и не удаляет user data.
- `FR-007` — Post-install validation отделяет technical result от human acceptance.

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

- `CTR-001` — `InstallPlan`: subject, operation, source_version, target_version, operations, conflicts, permissions, rollback_notes.
- `CTR-002` — `OwnershipManifest`: path, owner_class, source_digest, installed_digest, local_modified, removal_policy.
- `CTR-003` — `InstallResult`: applied_operations, skipped, conflicts, verification, partial_effects, recovery_required.
- `CTR-004` — `FirstStartCard`: current_status, first_safe_actions, documentation_entrypoint, support_diagnostics.
- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.

## 14. Связь с feature families

- [`FTR-004` — Greenfield Scaffold, Safe Install/Update/Uninstall, First-Start and Onboarding](../features/FTR-004_greenfield-scaffold-safe-install-update-uninstall-first-start-and-onboarding.md)

Primary family layer: `Product Runtime candidate / Enabling stage`. Proposed disposition: `HUMAN_DECISION_REQUIRED`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

Whether scaffolding is a Product Runtime feature or enabling stage remains a human product decision. No runtime/executor/CI/dependency installation is implied.

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

- Root files overwritten or merged heuristically.
- Generated scaffold is mistaken for implemented product.
- Uninstall removes user files.
- Version/update provenance is stale.
- Canonical artifacts stored under `/.aos-tmp/`.
- Scaffolding consumes first slice without user value.

## 17. Recovery behavior

**Source-derived recovery behavior:** Abort before write on unresolved conflict; after partial write, use manifest-driven rollback for owned additions only and leave ambiguous files untouched for human review.

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

- Before/after file inventory and ownership manifest.
- Dry-run/apply plan identity comparison.
- No-side-effect check for dry-run.
- Self-Test/Doctor/Validate results with NOT_RUN.
- Idempotency and uninstall preservation checks.

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

Каждый event содержит `function_id=IDEA-045`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-045-01` — Пользователь понимает назначение Installation Manifest and Version Detection без чтения implementation internals.
- `AC-045-02` — Функция создаёт ровно `Installation Manifest and Version Report` либо честный terminal report.
- `AC-045-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-045-04` — Unknowns, exclusions и blockers видимы.
- `AC-045-05` — Human authority и downstream permissions не расширены.
- `AC-045-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — Wrong repository/changed HEAD blocks apply.
- `AC-002` — No existing user file is silently overwritten.
- `AC-003` — Repeat install produces no unintended change.
- `AC-004` — Partial failure leaves recoverable state and exact manifest.
- `AC-005` — Uninstall preserves user/project data.
- `AC-006` — Новичок понимает первый safe action.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Installation Manifest and Version Report` для exact subject.
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

Минимальный вариант — planner + manifest + bounded file materializer + local verification adapters. Начать с scaffolding/static files; package manager, remote downloads и plugin installation отложить.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_045`
