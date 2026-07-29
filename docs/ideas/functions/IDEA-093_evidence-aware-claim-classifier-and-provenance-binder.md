---
document_id: AOS-ATOMIC-FUNCTION-IDEA-093
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-093
function_title: "Evidence-Aware Claim Classifier and Provenance Binder"
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
source_origin: PROPOSED_ATOMIC_SPLIT_R2
primary_feature_family: FTR-033
related_feature_families: [FTR-033]
human_review_required: true
---

# IDEA-093 — Evidence-Aware Claim Classifier and Provenance Binder

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Классифицирует claims как FACT, HYPOTHESIS, ASSUMPTION, PROPOSAL или UNKNOWN и связывает каждое утверждение с provenance, temporal scope и evidence.**

Основной наблюдаемый результат функции: **`Evidence-Aware Claim Record`**.

`IDEA-093` — Новый working ID, введённый только в R2 для атомарного разделения FTR-033/FTR-034; это `PROPOSAL`, не historical fact.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

Analyst, architect, task planner, reviewer и human decision maker.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

Specification и architecture proposal могут перескакивать от слабого наблюдения к уверенной рекомендации, не сравнивать alternatives или продолжать использовать stale Evidence.

**Atomic focus:** без `IDEA-093` family flow теряет конкретный механизм «Evidence-Aware Claim Classifier and Provenance Binder», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Evidence-Aware Claim Record` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

Material claim, ambiguity, contradiction или product/architecture decision требуют явного reasoning. Preconditions: уже существуют requirement IDs, decomposition и traceability foundation. Inputs: claims, source references, alternatives, observations, assumptions и decision subject.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

Material claim, ambiguity, contradiction или product/architecture decision требуют явного reasoning. Preconditions: уже существуют requirement IDs, decomposition и traceability foundation. Inputs: claims, source references, alternatives, observations, assumptions и decision subject.

Минимальный atomic input contract:

```yaml
function_id: IDEA-093
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: EVIDENCE_AWARE_CLAIM_RECORD
```

## 8. Пошаговое поведение

1. Проверить наличие принятых upstream inputs и material unknowns.
2. Создать первый DRAFT строго для exact subject и сохранить links to source IDs.
3. Проверить completeness, internal consistency, non-goals, authority wording и downstream dependencies.
4. Показать человеку changes, alternatives и unresolved decisions.
5. Сохранить revisioned artifact; не считать его accepted или executable без отдельного decision.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Evidence-Aware Claim Classifier and Provenance Binder**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-093`.
4. Создаётся **`Evidence-Aware Claim Record`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Evidence-Aware Claim Record`.

Outputs: Problem Analysis, hypothesis/alternative matrix, Decision Rationale candidate, weakest-link notice, evidence freshness/revalidation notice и review inputs. States: `CLAIMS_COLLECTED → CLASSIFIED → ALTERNATIVES_READY → ADI_CHECK → WEAK_LINK_FOUND | EVIDENCE_SUFFICIENT | REVALIDATION_REQUIRED → HUMAN_DECISION_REQUIRED`.

Atomic output должен содержать:

```yaml
function_id: IDEA-093
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
INPUT_READY → DRAFTING → DRAFT_READY → CHECKED → HUMAN_REVIEW_REQUIRED | REWORK_REQUIRED | DEFERRED
```

Transition invariants:

- Human-only transition не генерируется agent output.
- Material change subject/scope инвалидирует downstream DRAFT artifacts.
- `VALIDATE` и `REVIEW` не исправляют candidate.
- Failure/unknown приводит к report + stop.
- Recovery/correction выполняются отдельным authorized stage.

## 11. UX и человекочитаемое представление

`FPF Lite` разделяет `FACT`, `HYPOTHESIS`, `ASSUMPTION`, `PROPOSAL` и `UNKNOWN`, связывает claims с provenance и Evidence, применяет компактный ADI cycle — Abduction создаёт hypotheses, Deduction выводит проверяемые consequences, Induction обновляет confidence по observations. Дополнительно выявляются weakest link и revalidation triggers. Full DRR, quantitative decay/`R_eff`, external retrieval и agent cascade остаются optional later modules.

Для этой функции интерфейс обязан показывать:

- название **Evidence-Aware Claim Classifier and Provenance Binder** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-093-01` — Функция должна выполнять только следующую ответственность: Классифицирует claims как FACT, HYPOTHESIS, ASSUMPTION, PROPOSAL или UNKNOWN и связывает каждое утверждение с provenance, temporal scope и evidence.
- `FR-093-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-093-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-093-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-093-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-093-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

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


## 14. Связь с feature families

- [`FTR-033` — FPF Reasoning Integration: Evidence-Aware Claims, ADI Loop and Revalidation](../features/FTR-033_fpf-reasoning-integration-evidence-aware-claims-adi-loop-and-revalidation.md)

Primary family layer: `Documentation Assembly / Reasoning support`. Proposed disposition: `CANDIDATE_SUPPORT`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

FPF — external methodology/support layer, не governance и не approval authority. Он не заменяет requirements, task dependencies, acceptance criteria, Validation, Evidence или human checkpoints.

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


## 17. Recovery behavior

Failure modes: reasoning graph превращается в bureaucracy, confidence score подменяет judgment, stale Evidence silently поддерживает conclusion, FPF имитирует approval authority. Recovery: свернуть analysis до compact claims/unknowns, явно пометить stale Evidence и запросить targeted revalidation или human decision.

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

Evidence должен быть привязан к exact subject, invocation и output.

Минимальные events:

- `function_requested`
- `precondition_checked`
- `function_started`
- `artifact_created_or_reused`
- `function_blocked_or_failed`
- `function_completed`
- `human_review_requested`

Каждый event содержит `function_id=IDEA-093`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-093-01` — Пользователь понимает назначение Evidence-Aware Claim Classifier and Provenance Binder без чтения implementation internals.
- `AC-093-02` — Функция создаёт ровно `Evidence-Aware Claim Record` либо честный terminal report.
- `AC-093-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-093-04` — Unknowns, exclusions и blockers видимы.
- `AC-093-05` — Human authority и downstream permissions не расширены.
- `AC-093-06` — Failure behavior соответствует report + stop.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Evidence-Aware Claim Record` для exact subject.
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

Markdown sections/checklists и небольшой rationale validator после decomposition/traceability. Full evidence graph не является early-core dependency.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_093`
