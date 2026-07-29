---
document_id: AOS-ATOMIC-FUNCTION-IDEA-041
document_type: ATOMIC_FUNCTION_DESCRIPTION
revision: R2
function_id: IDEA-041
function_title: "Explicit Subagent Routing, Routing Audit and Provider Evaluation"
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
primary_feature_family: FTR-018
related_feature_families: [FTR-018]
human_review_required: true
---

# IDEA-041 — Explicit Subagent Routing, Routing Audit and Provider Evaluation

> **Статус:** `DRAFT`, `authority: NONE`. Этот файл описывает **одну атомарную функцию**. Он не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Что это

**Назначает явные agent roles, записывает routing rationale и оценивает providers/outputs, сохраняя ответственность и review boundary.**

Основной наблюдаемый результат функции: **`Subagent Routing and Audit Record`**.

`IDEA-041` — Исторический/reconstructed micro-feature ID, сохранённый из source crosswalk.

## 2. Пользовательская ценность

Функция должна уменьшить неопределённость и ручную координацию в пределах своей ответственности. Пользователь получает не внутренний agent monologue, а понятный artifact/status: что было входом, что функция сделала, что осталось неизвестным, какие ограничения сработали и какое одно следующее действие допустимо.

Она полезна только тогда, когда результат можно проверить независимо и связать с exact subject. Наличие красивого текста, PASS или Evidence само по себе не означает product acceptance.

## 3. Для кого

**Target users:** Product owner, orchestrating agent and maintainers optimizing quality/cost/context.

Основные jobs-to-be-done:

- Выбрать модель/роль с подходящим reasoning, context и cost.
- Не использовать дорогую модель для routine task без пользы.
- Не отправить sensitive context неподходящему provider.
- Передать subagent узкий context packet.
- Измерить качество routing и безопасно fallback-нуться.

В atomic boundary роль пользователя уточняется так:

- **инициатор** предоставляет input или trigger;
- **оператор/agent** выполняет bounded processing;
- **reviewer** проверяет artifact и limitations;
- **human decision maker** принимает только те решения, которые явно отнесены к human authority.

## 4. Проблема, которую решает функция

### Проблема

One model may be inefficient for all tasks, but opaque routing can lower quality, leak data, fragment context or appear to assign authority.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

**Atomic focus:** без `IDEA-041` family flow теряет конкретный механизм «Explicit Subagent Routing, Routing Audit and Provider Evaluation», из-за чего ответственность либо выполняется вручную, либо расплывается между несколькими modules и становится непроверяемой.

## 5. Scope функции

### In scope

- Выполнить ровно ответственность, сформулированную в разделе 1.
- Проверить preconditions и exact subject.
- Сохранить source/provenance и status semantics.
- Создать или обновить только `Subagent Routing and Audit Record` и прямо связанные derived views.
- Выдать explicit limitations, blockers и один `next_required_action`.

### Out of scope

- Самостоятельно принимать product, architecture, dependency, Risk Profile или Source-of-Truth decisions.
- Неявно переходить к следующему stage.
- Выполнять Commit, Push, PR create, Merge, Release или deployment без отдельных authorizations.
- Превращать DRAFT/result/Evidence/PASS в human approval.
- Расширять repository paths, network, sandbox или provider boundary без permission.

## 6. Trigger и preconditions

### Triggers

- Task has unusual context/reasoning/tool requirements.
- Cost/latency optimization is measured.
- Specialist read-only analysis/review is useful.
- Primary model unavailable or insufficient.

### Preconditions

- Task Brief/role/context boundary clear.
- Provider permissions and sensitivity policy known.
- Benchmark/evaluation method available.
- Subagents cannot exceed parent scope/authority.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

Дополнительно для atomic function:

1. Exact subject и expected output известны.
2. Upstream input имеет revision/status и не конфликтует с более авторитетным source.
3. Required permissions доступны либо функция остаётся read-only.
4. Material unknowns перечислены до processing.
5. Stop conditions определены заранее.

## 7. Inputs

- `task_class`
- `role`
- `context_size_and_type`
- `tool_requirements`
- `sensitivity_flags`
- `candidate_models_or_agents`
- `quality_cost_latency_metrics`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

Минимальный atomic input contract:

```yaml
function_id: IDEA-041
subject_id: REQUIRED
subject_revision: REQUIRED
source_refs: []
constraints: []
permissions: []
material_unknowns: []
requested_output: SUBAGENT_ROUTING_AND_AUDIT_RECORD
```

## 8. Пошаговое поведение

1. Классифицировать task, required capabilities, sensitivity и constraints.
2. Сравнить доступные models/agents/providers по declared и measured fit.
3. Сформировать advisory route с rationale, fallbacks и limitations.
4. Проверить permission/provider boundary до передачи context.
5. Записать actual route и outcome для последующего evaluation.

### Пример наблюдаемого сценария

1. Пользователь или upstream stage передаёт exact input для **Explicit Subagent Routing, Routing Audit and Provider Evaluation**.
2. Функция связывает input с `subject_id`, проверяет authority/permissions и перечисляет unknowns.
3. Выполняется только bounded responsibility `IDEA-041`.
4. Создаётся **`Subagent Routing and Audit Record`** с Evidence и limitations.
5. При success функция предлагает один следующий stage; при conflict/failure выпускает report и останавливается.

## 9. Outputs и observable behavior

**Primary output:** `Subagent Routing and Audit Record`.

Source-derived outputs:

- Routing recommendation
- Subagent packet/result
- Routing audit record
- Provider evaluation
- Benchmark metrics

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

Atomic output должен содержать:

```yaml
function_id: IDEA-041
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
TASK_CLASSIFIED → CANDIDATES_EVALUATED → ROUTE_PROPOSED → HUMAN/CONTROL_CHECK → ROUTED | BLOCKED
```

Transition invariants:

- Human-only transition не генерируется agent output.
- Material change subject/scope инвалидирует downstream DRAFT artifacts.
- `VALIDATE` и `REVIEW` не исправляют candidate.
- Failure/unknown приводит к report + stop.
- Recovery/correction выполняются отдельным authorized stage.

## 11. UX и человекочитаемое представление

- Recommendation explains why this model/role fits.
- Provider, data boundary, cost and fallback are visible.
- Subagent result includes scope, sources, limitations and no authority.
- Routing failure is reported, not hidden.
- User can force a known model where allowed.

Presentation layer не становится Source of Truth и не может расширить permissions.

Для этой функции интерфейс обязан показывать:

- название **Explicit Subagent Routing, Routing Audit and Provider Evaluation** и exact subject;
- что функция получила и что не получила;
- краткий result до technical details;
- affected artifacts и Evidence;
- blocker/reason code без расплывчатого «что-то пошло не так»;
- разницу между recommendation, technical result и human decision.

## 12. Functional requirements — `PROPOSAL`

- `FR-041-01` — Функция должна выполнять только следующую ответственность: Назначает явные agent roles, записывает routing rationale и оценивает providers/outputs, сохраняя ответственность и review boundary.
- `FR-041-02` — Exact subject, input revision, provenance и temporal scope должны сохраняться в output.
- `FR-041-03` — Missing material data должны иметь status `UNKNOWN`, `BLOCKED` или `HUMAN_REVIEW_REQUIRED`, а не заполняться догадкой.
- `FR-041-04` — Technical result не должен содержать или имитировать human acceptance/authorization.
- `FR-041-05` — На failure, denied action или unresolved conflict функция выпускает report и останавливается; automatic retry запрещён.
- `FR-041-06` — Derived UI/index/report должен ссылаться на owner facts и быть rebuildable.

### Family-level requirements, ограничивающие функцию

- `FR-001` — Routing record must include task, role, rationale, selected provider/model and fallback.
- `FR-002` — Sensitive-domain/provider rules override cost optimization.
- `FR-003` — Subagent context is minimal and task-scoped.
- `FR-004` — Subagent cannot mutate unless separately authorized and never in parallel.
- `FR-005` — Model output is evidence/recommendation, not human decision.
- `FR-006` — Routing quality is measured against baseline.
- `FR-007` — Fallback must not escalate permissions.

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

- `CTR-001` — `RoutingAssessment`: task_properties, candidates, constraints, recommendation, confidence, unknowns.
- `CTR-002` — `SubagentPacket`: role, task, allowed_sources, context_pack, expected_output, prohibited_actions.
- `CTR-003` — `SubagentResult`: result, sources, findings, limitations, status, no_authority.
- `CTR-004` — `RoutingAudit`: selected_model, provider, rationale, cost, latency, quality, fallback_events.
- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.

## 14. Связь с feature families

- [`FTR-018` — Advisory Model Routing, Explicit Agent Roles, Routing Audit and Provider Evaluation](../features/FTR-018_advisory-model-routing-explicit-agent-roles-routing-audit-and-provider-evaluation.md)

Primary family layer: `Development Factory`. Proposed disposition: `DEFERRED_UNTIL_MEASURED`.

Эти связи описывают design context. Они **не** принимают dependency package и не делают функцию core.

## 15. Safety и human authority

Model choice never grants execution or human authority. Automatic routing and multi-agent runtime are deferred until measured.

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

- Routing substitutes Risk Profile or approval.
- Cheap model used for ambiguous/high-risk task.
- Provider receives prohibited data.
- Subagents write concurrently.
- Context split loses critical constraint.
- Cost/quality claims lack benchmark.

## 17. Recovery behavior

**Source-derived recovery behavior:** Fallback to known capable model/manual route, preserve task state, rerun only with explicit context and no carried authority.

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

- Benchmark tasks and reviewer scores.
- Routing decision/audit logs.
- Provider/sensitivity policy checks.
- Fallback and privilege non-escalation tests.

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

Каждый event содержит `function_id=IDEA-041`, `subject_id`, actor/tool, timestamp, status и correlation ID.

## 19. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-041-01` — Пользователь понимает назначение Explicit Subagent Routing, Routing Audit and Provider Evaluation без чтения implementation internals.
- `AC-041-02` — Функция создаёт ровно `Subagent Routing and Audit Record` либо честный terminal report.
- `AC-041-03` — Result связан с exact subject, source revisions и Evidence.
- `AC-041-04` — Unknowns, exclusions и blockers видимы.
- `AC-041-05` — Human authority и downstream permissions не расширены.
- `AC-041-06` — Failure behavior соответствует report + stop.

Family-derived acceptance expectations:

- `AC-001` — Routing rationale is reproducible and visible.
- `AC-002` — Sensitive context stays within allowed provider.
- `AC-003` — Subagent stays in scope.
- `AC-004` — Fallback does not widen permissions.
- `AC-005` — Measured quality/cost benefit exists.
- `AC-006` — Recommendation cannot create authority.

## 20. Test design — `NOT_RUN`

### Positive tests

- При валидных входах создаётся `Subagent Routing and Audit Record` для exact subject.
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

Start with static advisory matrix and explicit packets. Add small benchmark/evaluation harness. No dynamic router service or multi-agent graph until repeated measured need.

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

`next_required_action: HUMAN_REVIEW_OF_IDEA_041`
