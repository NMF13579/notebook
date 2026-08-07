---
document_id: AOS-FEATURE-FTR-005
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-005
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
layer: "Product Runtime / Architecture boundary"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-009
  - IDEA-010
  - IDEA-011
  - IDEA-012
  - IDEA-014
  - IDEA-015
human_review_required: true
---

# FTR-005 — Architecture Need Check, Decision Support, ADR Builder and Human Checkpoint

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-005` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича определяет, действительно ли нужен architecture decision, сравнивает варианты и готовит human checkpoint, не принимая решение за человека.

**Source-derived desired outcome:** Read-only architecture decision package with need classification, constraints, options, fit criteria, consequences, reversibility, dependencies, risks, testability, evidence and explicit human decision fields.

## 3. Для кого и какую работу выполняет

**Target users:** Product owner, architect, technical lead and non-programmer who must understand trade-offs.

Основные jobs-to-be-done:

- Не создавать ADR для routine work без material choice.
- Не пропускать выбор, который влияет на interfaces, dependencies, data, security или reversibility.
- Понять trade-offs вариантов простым языком.
- Связать принятое решение с requirements, tasks и tests.
- Сохранить отклонённые варианты и условия пересмотра.

## 4. Проблема и ожидаемая ценность

### Проблема

Routine work can acquire unnecessary architecture ceremony, while material choices can pass unnoticed. Generated recommendations may be mistaken for authority.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Architecture Need Check.
- Constraint/evidence intake.
- 2–4 option comparison и fit criteria.
- ADR candidate и human checkpoint package.
- Architecture-to-requirement/task/test traceability.

### Out of scope / non-goals

- Автоматическое утверждение architecture/dependencies.
- Full enterprise architecture modeling.
- Выбор stack preset без contextual fit.
- Implementation planning при незакрытом decision.
- Изменение accepted architecture в VALIDATE/REVIEW.

## 6. Trigger и preconditions

### Triggers

- Новый component/interface/data store/provider/dependency.
- Irreversible или costly-to-change choice.
- Material security/privacy/operational impact.
- Conflict между accepted constraints и task design.
- Repeated implementation divergence показывает missing decision.

### Preconditions

- Product problem/outcome и relevant requirements известны.
- Decision scope и owner определены.
- Available evidence и unknowns перечислены.
- Architecture authority принадлежит человеку.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `requirements_and_constraints`
- `current_architecture_observations`
- `candidate_options`
- `pattern_library_refs`
- `risk_and_reversibility_factors`
- `dependency_candidates`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Architecture need result
- Options comparison
- ADR candidate
- Human checkpoint package
- Architecture-to-task trace links

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Assess whether a material architecture choice exists.
2. Collect exact constraints and accepted product inputs.
3. Generate viable options and expose assumptions.
4. Compare trade-offs and negative evidence.
5. Draft ADR/checkpoint package as `PROPOSAL`.
6. Human accepts, revises, defers or rejects.
7. Only accepted decision becomes input to downstream tasks.

### Иллюстративный сценарий

1. Возникает trigger: Новый component/interface/data store/provider/dependency.
2. Система принимает входы `requirements_and_constraints, current_architecture_observations, candidate_options` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Architecture need result, Options comparison, ADR candidate.
5. При failure `Classifier decides architecture.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
NEED_UNASSESSED → NO_ADR_NEEDED | ADR_REQUIRED → OPTIONS_READY → HUMAN_CHECKPOINT → ACCEPTED | NEEDS_RESEARCH | DEFERRED | REJECTED | SUPERSEDED
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Need Check объясняет, почему решение material или routine.
- Option comparison использует одинаковые dimensions: fit, cost, risk, reversibility, testability, lock-in.
- Recommendation помечена advisory и отделена от human decision.
- Unknowns, которые меняют ranking, видимы рядом.
- Accepted decision показывает consequences и revisit triggers.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Architecture decision создаётся только при material choice.
- `FR-002` — Каждый option должен быть implementable enough для сравнения, но не full design.
- `FR-003` — Dependencies помечаются proposed до human acceptance.
- `FR-004` — No-option/keep-current option включается, если применим.
- `FR-005` — Decision binding включает exact scope, requirements и temporal context.
- `FR-006` — Accepted ADR не предоставляет execution authorization.
- `FR-007` — Material scope change требует нового decision или supersession.

## 13. Capabilities из source synthesis

- Architecture Need Check returning `ARCHITECTURE_NOT_REQUIRED` or `HUMAN_ARCHITECTURE_REVIEW_REQUIRED`.
- Architecture Input Intake: constraints, compatibility, security, data, operations and unknowns.
- Plain-language Architecture Assistant comparing alternatives.
- ADR candidate builder with context, options, decision criteria, consequences and reversal conditions.
- Stack preset candidates and explicit fit/non-fit conditions.
- Architecture Evidence and Human Checkpoint package.
- Traceability from accepted ADR/contract clauses to Task Briefs and tests.
- Conflict hierarchy for external documents and current project sources.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `ArchitectureNeedAssessment`: trigger, affected_contracts, materiality_factors, result, rationale.
- `CTR-002` — `ArchitectureOption`: option_id, description, fit, tradeoffs, risks, dependencies, reversibility, tests, unknowns.
- `CTR-003` — `ADRCandidate`: context, decision_question, options, recommendation, consequences, revisit_triggers.
- `CTR-004` — `HumanArchitectureDecision`: ACCEPT_OPTION | REQUEST_RESEARCH | DEFER | REJECT; exact subject binding.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-003`, `FTR-022`, `FTR-012`, `FTR-021`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Architecture is protected. Only human can accept architecture and dependencies. A DRAFT ADR has `authority: NONE`.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Classifier decides architecture.
- One option presented as inevitable.
- Recommendation tone simulates acceptance.
- Stack preset introduces hidden dependencies.
- Trace graph becomes competing Source of Truth.
- Architecture process runs for routine task.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Return to options/constraints, mark disputed items `UNKNOWN`, invalidate downstream drafts bound to a superseded ADR; no automatic correction or task execution.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Requirement/constraint references.
- Option evidence and pattern provenance.
- Dependency/license/security facts where applicable.
- Decision-to-task/test trace links.

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

- `AC-001` — Routine task can pass with documented NO_ADR_NEEDED rationale.
- `AC-002` — Material option comparison does not hide unknowns.
- `AC-003` — Human understands consequences and reversibility.
- `AC-004` — No generated recommendation appears as accepted decision.
- `AC-005` — Selected option traces to affected tasks/tests.
- `AC-006` — Rejected/deferred options remain recoverable.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Stack preset cannot auto-select dependency.
- `NEG-002` — Old ADR for different scope cannot authorize current change.
- `NEG-003` — Architecture PASS cannot mean product acceptance.
- `NEG-004` — Missing material evidence results in NEEDS_RESEARCH, not fabricated ranking.
- `NEG-005` — VALIDATE cannot rewrite ADR.
- `NEG-006` — Agent cannot assign decision identity.

## 22. Minimal implementation model — `PROPOSAL`

Сначала Markdown/JSON templates, deterministic need checklist и comparison matrix. Pattern Library integration advisory. Graph tooling or architecture platform is unnecessary.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: manual Architecture Need Check.
- M1: ADR candidate compiler and validator.
- M2: requirement/task/test trace integration.
- M3: pattern-assisted suggestions after pattern quality is proven.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-009` — Architecture Need Check and Input Intake
- `IDEA-010` — Architecture Assistant
- `IDEA-011` — Architecture Option Comparison and ADR Builder
- `IDEA-012` — Stack Preset Registry
- `IDEA-014` — Architecture Evidence and Human Checkpoint Package
- `IDEA-015` — Architecture-to-Task Traceability

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Какой exact threshold делает choice material?
- Какие dependency/license/security checks обязательны?
- Где хранится accepted architecture Source of Truth?
- Какие decision identity/authenticity guarantees нужны?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-005`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `05 - AOS-FARM — справочные идеи из harness engineering.txt`
- `08 - Architecture Lifecycle Integration Plan.txt`

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

- [`IDEA-009` — Architecture Need Check and Input Intake](../functions/IDEA-009_architecture-need-check-and-input-intake.md)
- [`IDEA-010` — Architecture Assistant](../functions/IDEA-010_architecture-assistant.md)
- [`IDEA-011` — Architecture Option Comparison and ADR Builder](../functions/IDEA-011_architecture-option-comparison-and-adr-builder.md)
- [`IDEA-012` — Stack Preset Registry](../functions/IDEA-012_stack-preset-registry.md)
- [`IDEA-014` — Architecture Evidence and Human Checkpoint Package](../functions/IDEA-014_architecture-evidence-and-human-checkpoint-package.md)
- [`IDEA-015` — Architecture-to-Task Traceability](../functions/IDEA-015_architecture-to-task-traceability.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_005`
