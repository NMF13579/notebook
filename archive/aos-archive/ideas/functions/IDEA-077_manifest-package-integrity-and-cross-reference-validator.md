---
document_id: AOS-ATOMIC-FUNCTION-IDEA-077
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-077
function_title: "Manifest, Package Integrity and Cross-Reference Validator"
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
primary_feature_family: FTR-029
related_feature_families: [FTR-029, FTR-030]
human_review_required: true
---

# IDEA-077 — Manifest, Package Integrity and Cross-Reference Validator

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Проверяет manifest, package integrity, checksums и cross-references, обнаруживая missing, duplicate, stale и orphan artifacts.**

Основной наблюдаемый результат функции: **`Package Integrity Validation Report`**.

`IDEA-077` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** AOS maintainers, adopters, teams sharing templates/prompts and multi-repository projects.

Основные jobs-to-be-done:

- Повторно использовать templates/prompts между проектами.
- Обновлять pack без потери local modifications.
- Поддерживать localization, сохраняя IDs/status semantics.
- Ограничивать cross-repo context.
- Отделить static pack от executable extension.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

Copies of templates/prompts drift, updates overwrite local changes, localization changes semantics, and imported packs can smuggle authority or executable instructions.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-077` family flow теряет конкретный механизм «Manifest, Package Integrity and Cross-Reference Validator», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Package Integrity Validation Report` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- Team shares templates/prompts/config across projects.
- Localized variant is needed.
- Pack update/uninstall requested.
- Task needs bounded cross-repo reference context.

### Preconditions

- Static content boundary clear.
- Source/provenance/version known.
- Ownership/conflict policy.
- Allowed repositories and permission.
- Localization semantics/tests.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `pack_manifest`
- `source_assets`
- `target_repository`
- `installed_manifest`
- `local_modifications`
- `locale_or_policy_overlay`
- `allowed_cross_repo_sources`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-077
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: PACKAGE_INTEGRITY_VALIDATION_REPORT
```

## 8. Пошаговое поведение

1. Привязать проверку к exact immutable subject, baseline и expected contract.
2. Выполнить targeted positive, negative и boundary checks без исправления subject.
3. Собрать machine-readable result, Evidence и limitations.
4. Отличить PASS, FAIL, BLOCKED, NOT_RUN и UNKNOWN; не конвертировать их в approval.
5. Выпустить report и остановиться; correction требует отдельного EXECUTE.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Manifest, Package Integrity and Cross-Reference Validator**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-077`.
4. Создаётся **`Package Integrity Validation Report`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Package Integrity Validation Report`.

Source-derived outputs:

- Pack manifest
- Export/import plan
- Installed static assets
- Conflict/update report
- Provenance/version

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-077
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

- Preview lists create/replace/merge/skip/conflict.
- Pack card shows source/version/license/authority NONE.
- Localization diff highlights status/authority semantic changes.
- Cross-repo sources are named explicitly.
- Executable content is rejected or routed to FTR-026.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Manifest, Package Integrity and Cross-Reference Validator** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-077-01` — Функция должна выполнять только следующую ответственность: Проверяет manifest, package integrity, checksums и cross-references, обнаруживая missing, duplicate, stale и orphan artifacts.
- `FR-077-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-077-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-077-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-077-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-077-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Manifest covers all owned static assets and references.
- `FR-002` — Update detects local modifications.
- `FR-003` — Repeated install/update idempotent.
- `FR-004` — Imported prompt cannot grant execution/authority.
- `FR-005` — Localization preserves stable IDs/enums/decision semantics.
- `FR-006` — Cross-repo reads require explicit allowed list.
- `FR-007` — Uninstall removes only pack-owned unchanged assets.
- `FR-001` — Reject duplicate keys, unknown fields, unsafe aliases/paths and invalid types per contract.

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

- `CTR-001` — `PackManifest`: pack_id, version, type, source, license, assets, references, ownership, compatibility.
- `CTR-002` — `PackPlan`: operation, target, changes, conflicts, local_modifications, permissions.
- `CTR-003` — `LocalizationValidation`: source_locale, target_locale, stable_tokens, semantic_findings.
- `CTR-004` — `PackResult`: installed_version, effects, conflicts, verification, rollback.
- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.

## 14. Связь с feature families

- [`FTR-029` — Template Export, Prompt Packs, Cross-Repo Context, Localization and Policy Overlays](../features/FTR-029_template-export-prompt-packs-cross-repo-context-localization-and-policy-overlays.md)
- [`FTR-030` — Internal Contract Tooling: Strict Loaders, Parser Sunset, Registry Audits and Drift Tests](../features/FTR-030_internal-contract-tooling-strict-loaders-parser-sunset-registry-audits-and-drift-tests.md)

Primary family layer: `Packaging / Extension support`. Proposed disposition: `DEFERRED_RESEARCH`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

No target authority transfer, marketplace, automatic policy distribution or executable modules in baseline.

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

- Imported prompt grants execution.
- Translation changes status semantics.
- Stale manifest overwrites local work.
- Broken references or missing source.
- Cross-repo reads exceed permission.
- Executable code loaded as template.

## 17. Recovery behavior

**Source-derived recovery behavior:** Abort/rollback owned static changes, preserve local files, reject unsafe pack and restore previous version from manifest.

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

- Manifest/reference/integrity checks.
- Before/after ownership and local-modification comparison.
- Localization semantic tests.
- Cross-repo access audit.

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

Каждый event содержит `function_id=IDEA-077`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-077-01` — Пользователь понимает назначение Manifest, Package Integrity and Cross-Reference Validator без чтения implementation internals.
- `AC-077-02` — Функция создаёт ровно `Package Integrity Validation Report` либо честный terminal report.
- `AC-077-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-077-04` — Unknowns, exclusions и blockers видимы.
- `AC-077-05` — Human authority и downstream permissions не расширены.
- `AC-077-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — Provenance/version visible.
- `AC-002` — Local changes preserved or conflict shown.
- `AC-003` — Broken references detected.
- `AC-004` — Repeated update idempotent.
- `AC-005` — Imported prompt cannot authorize action.
- `AC-006` — Uninstall is safe.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Package Integrity Validation Report` для exact subject.
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

Manifest-based static package format reusing installer planning/ownership. Support templates/prompts first; overlays/cross-repo later; executable modules only through FTR-026.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_077`
