---
document_id: AOS-FEATURE-FTR-018
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-018
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
layer: "Development Factory candidate"
disposition: DEFERRED_UNTIL_MEASURED
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-040
  - IDEA-041
  - IDEA-092
human_review_required: true
---

# FTR-018 — Advisory Model/Agent Routing, Explicit Subagents, Routing Audit and Provider Evaluation

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-018` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича advisory-режима рекомендует model/agent role по task properties, фиксирует rationale и результаты, но не передаёт authority и не запускает full multi-agent autonomy.

**Source-derived desired outcome:** Measured advisory routing that selects a role/model/provider based on task properties, records the rationale and falls back safely; full multi-agent coordination remains deferred.

## 3. Для кого и какую работу выполняет

**Target users:** Product owner, orchestrating agent and maintainers optimizing quality/cost/context.

Основные jobs-to-be-done:

- Выбрать модель/роль с подходящим reasoning, context и cost.
- Не использовать дорогую модель для routine task без пользы.
- Не отправить sensitive context неподходящему provider.
- Передать subagent узкий context packet.
- Измерить качество routing и безопасно fallback-нуться.

## 4. Проблема и ожидаемая ценность

### Проблема

One model may be inefficient for all tasks, but opaque routing can lower quality, leak data, fragment context or appear to assign authority.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Advisory routing recommendation.
- Explicit specialist subagent packets/results.
- Provider/privacy/capability constraints.
- Routing audit and benchmark metrics.
- Visible fallback.

### Out of scope / non-goals

- Automatic Risk Profile/authority assignment.
- Hidden provider switching.
- Full autonomous multi-agent coordination.
- Parallel writes.
- Routing as substitute for task decomposition.

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

## 7. Inputs

- `task_class`
- `role`
- `context_size_and_type`
- `tool_requirements`
- `sensitivity_flags`
- `candidate_models_or_agents`
- `quality_cost_latency_metrics`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

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

## 9. Подробный workflow

1. Classify task and authority boundary.
2. Recommend role/model/provider.
3. Human/system policy confirms allowed provider.
4. Run bounded agent with exact context pack.
5. Validate result independently.
6. Record metrics and fallback behavior.

### Иллюстративный сценарий

1. Возникает trigger: Task has unusual context/reasoning/tool requirements.
2. Система принимает входы `task_class, role, context_size_and_type` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Routing recommendation, Subagent packet/result, Routing audit record.
5. При failure `Routing substitutes Risk Profile or approval.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
ROUTING_DISABLED → ADVISORY_ASSESSMENT → RECOMMENDED → HUMAN_OR_ORCHESTRATOR_SELECTION → RUN → AUDITED → FALLBACK | NO_MEASURED_VALUE
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Recommendation explains why this model/role fits.
- Provider, data boundary, cost and fallback are visible.
- Subagent result includes scope, sources, limitations and no authority.
- Routing failure is reported, not hidden.
- User can force a known model where allowed.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Routing record must include task, role, rationale, selected provider/model and fallback.
- `FR-002` — Sensitive-domain/provider rules override cost optimization.
- `FR-003` — Subagent context is minimal and task-scoped.
- `FR-004` — Subagent cannot mutate unless separately authorized and never in parallel.
- `FR-005` — Model output is evidence/recommendation, not human decision.
- `FR-006` — Routing quality is measured against baseline.
- `FR-007` — Fallback must not escalate permissions.

## 13. Capabilities из source synthesis

- Role classes: Architect, Executor, Reviewer, Documentation Agent.
- Criteria: ambiguity, risk, context size, determinism, need for independent review and cost.
- Advisory model recommendation before automatic switching.
- Explicit subagent packets with bounded scope and read-only/write permissions.
- Routing record: task, role, model, reason, inputs, outputs, limitations.
- Provider evaluation for privacy, context, reliability, latency and cost.
- Local benchmark and quality/cost metrics.
- Independent read-only reviewer agents.
- Future multi-agent coordination only after stable contracts and demonstrated value.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `RoutingAssessment`: task_properties, candidates, constraints, recommendation, confidence, unknowns.
- `CTR-002` — `SubagentPacket`: role, task, allowed_sources, context_pack, expected_output, prohibited_actions.
- `CTR-003` — `SubagentResult`: result, sources, findings, limitations, status, no_authority.
- `CTR-004` — `RoutingAudit`: selected_model, provider, rationale, cost, latency, quality, fallback_events.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-016`, `FTR-019`, `FTR-021`, `FTR-023`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Model choice never grants execution or human authority. Automatic routing and multi-agent runtime are deferred until measured.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Routing substitutes Risk Profile or approval.
- Cheap model used for ambiguous/high-risk task.
- Provider receives prohibited data.
- Subagents write concurrently.
- Context split loses critical constraint.
- Cost/quality claims lack benchmark.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Fallback to known capable model/manual route, preserve task state, rerun only with explicit context and no carried authority.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

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

## 20. Acceptance criteria — `DESIGNED`, tests `NOT_RUN`

- `AC-001` — Routing rationale is reproducible and visible.
- `AC-002` — Sensitive context stays within allowed provider.
- `AC-003` — Subagent stays in scope.
- `AC-004` — Fallback does not widen permissions.
- `AC-005` — Measured quality/cost benefit exists.
- `AC-006` — Recommendation cannot create authority.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Cheap model selected despite prohibited data boundary.
- `NEG-002` — Subagent reads unrelated repositories.
- `NEG-003` — Routing silently changes model/provider.
- `NEG-004` — Two subagents write same scope.
- `NEG-005` — Fallback consumes larger authority.
- `NEG-006` — Routing metric PASS interpreted as product acceptance.

## 22. Minimal implementation model — `PROPOSAL`

Start with static advisory matrix and explicit packets. Add small benchmark/evaluation harness. No dynamic router service or multi-agent graph until repeated measured need.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: role/task routing guidelines.
- M1: recorded advisory recommendation.
- M2: explicit read-only subagents and audit.
- M3: limited runtime routing only after measured threshold.

**Disposition rule:** Не внедрять до baseline metrics и доказанного value/need.

## 24. Related micro-features

- `IDEA-040` — Advisory Model Routing
- `IDEA-041` — Explicit Subagent Routing, Routing Audit and Provider Evaluation
- `IDEA-092` — Full Multi-Agent Coordination

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Which models/providers are approved at implementation time?
- What metrics and threshold justify routing?
- How should model capabilities be refreshed?
- Which roles warrant explicit subagents?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-018`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `04 — AOS Model Routing and Task Decomposition Research.txt`
- `03 — AOS Future and Legacy Reference.txt`

Limitations:

- Full raw export всех historical chats не доказан.
- Current repository/worktree/branch/HEAD/baseline и runtime implementation не проверялись: `NOT_RUN`.
- Legacy AOS-FARM/AOS-02/AgentOS materials имеют `READ_ONLY_REFERENCE`, `authority: NONE`.
- Requirements/contracts/tests в этом файле являются clean-room `PROPOSAL`.
- Family boundary может быть пересмотрена после Product Contract и human review.

## 27. Promotion path

```text
DRAFT feature description
→ human product-fit decision
→ Product Contract and refined acceptance scenarios
→ DRAFT architecture options
→ human architecture/dependency decision
→ bounded Task Brief
→ explicit execution authorization
→ EXECUTE
→ separate VALIDATE
→ separate REVIEW
→ human decision
→ separately authorized Git/release operations
```

## 28. Отдельные документы атомарных функций

Каждая функция ниже имеет собственный standalone document; ссылки не означают product acceptance.

- [`IDEA-040` — Advisory Model Routing](../functions/IDEA-040_advisory-model-routing.md)
- [`IDEA-041` — Explicit Subagent Routing, Routing Audit and Provider Evaluation](../functions/IDEA-041_explicit-subagent-routing-routing-audit-and-provider-evaluation.md)
- [`IDEA-092` — Full Multi-Agent Coordination](../functions/IDEA-092_full-multi-agent-coordination.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_018`
