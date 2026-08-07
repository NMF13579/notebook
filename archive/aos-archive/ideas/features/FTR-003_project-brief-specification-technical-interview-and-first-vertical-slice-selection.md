---
document_id: AOS-FEATURE-FTR-003
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-003
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
layer: "Product Runtime"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-006
  - IDEA-007
  - IDEA-008
  - IDEA-080
  - IDEA-081
human_review_required: true
---

# FTR-003 — Project Brief, Specification Support, Technical Assignment and First Vertical Slice Selection

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-003` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича собирает Intent и Discovery в понятный Project Brief/Specification и помогает человеку выбрать первый вертикальный срез, который показывает реальную пользовательскую ценность.

**Source-derived desired outcome:** Один human-readable Project Brief/Specification candidate с users, problems, outcomes, boundaries, observable behavior, non-goals, acceptance expectations, unknowns и candidate first vertical slice.

## 3. Для кого и какую работу выполняет

**Target users:** Product owner, non-programmer founder, product analyst, architect and task author.

Основные jobs-to-be-done:

- Сформулировать, для кого и зачем создаётся продукт или изменение.
- Определить in-scope/out-of-scope behavior и наблюдаемый success.
- Не смешать Product Runtime с внутренней Development Factory.
- Сравнить несколько first-slice options по value, risk и dependencies.
- Передать выбранный scope дальше без скрытого implementation plan.

## 4. Проблема и ожидаемая ценность

### Проблема

Intent слишком свободен для разработки, а implementation Task Brief слишком узок для описания продукта. Без промежуточного product contract требования дублируются, scope расползается, а первый slice демонстрирует tooling вместо user value.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Project Brief, feature description, user journeys, observable outcomes и non-goals.
- Specification candidate с acceptance expectations, failures и recovery.
- Optional Technical Assignment как behavioral boundary.
- 1–3 candidate vertical slices и human decision package.
- Requirement trace map до architecture/UX/task.

### Out of scope / non-goals

- Утверждение architecture, stack или dependencies.
- Полный roadmap и backlog декомпозиция.
- Execution authorization и Git delivery.
- Копирование legacy topology как target requirement.
- Автоматическое принятие приоритета.

## 6. Trigger и preconditions

### Triggers

- Intent Record готов для product definition.
- Discovery выявил material improvement opportunity.
- Нужно решить, какая feature станет первым Product Runtime slice.
- Existing specification требует упрощения или consistency review.

### Preconditions

- Target user и desired outcome хотя бы предварительно определены.
- Material source conflicts и unknowns раскрыты.
- Historical mechanisms помечены как reference, а не requirement.
- Human decision channel для выбора slice доступен.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `IntentRecord`
- `DiscoveryReport`
- `feature_family_candidates`
- `constraints_and_non_goals`
- `lessons_and_failure_patterns`
- `domain_requirements`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Project Brief
- Specification candidate
- Optional Technical Assignment
- First-slice decision package
- Requirement trace map

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Read accepted/corrected Intent Record.
2. Use Discovery findings where an existing project is involved.
3. Draft users, scope, behavior, non-goals and unknowns.
4. Identify material architecture questions but do not resolve them.
5. Generate first-slice options and trade-offs.
6. Human reviews and selects/revises/defer.
7. Produce input for architecture check, UX skeleton or Task Brief.

### Иллюстративный сценарий

1. Возникает trigger: Intent Record готов для product definition.
2. Система принимает входы `IntentRecord, DiscoveryReport, feature_family_candidates` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Project Brief, Specification candidate, Optional Technical Assignment.
5. При failure `Specification становится энциклопедией.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
DRAFTING → PRODUCT_REVIEW → SLICE_OPTIONS → HUMAN_DECISION_REQUIRED → SELECTED | NEEDS_REVISION | DEFERRED | REJECTED
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Brief начинается с простого ответа: кто получает какую ценность.
- Каждая candidate feature показана через observable before/after, а не внутренние components.
- Slice options сравниваются в одной таблице с explicit trade-offs.
- Пользователь может принять, изменить, отклонить или отложить вариант.
- Selected slice визуально отделён от остальных идей и не считается execution-ready.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — У каждого requirement должен быть actor, expected outcome и проверяемое observation.
- `FR-002` — Non-goals и deferred capabilities обязательны.
- `FR-003` — First slice должен быть end-to-end и user-visible, а не registry/control-plane demo.
- `FR-004` — Technical Assignment не может включать unaccepted stack/dependencies как факт.
- `FR-005` — Material scope change должен инвалидировать downstream draft artifacts.
- `FR-006` — Каждый unknown помечается impact на slice/architecture/task.
- `FR-007` — Выбор человека сохраняет rationale и rejected alternatives.

## 13. Capabilities из source synthesis

- Преобразовывать accepted intake interpretation в coherent product context.
- Фиксировать user roles, jobs, journeys, functional and non-functional requirements.
- Разделять product requirement, architecture constraint и implementation task.
- Формировать Technical Assignment только когда нужен bridge к engineering scope.
- Сравнивать 2–4 first-slice options по direct user value, dependencies, reversibility и testability.
- Выбирать только recommended candidate; final selection остаётся human decision.
- Поддерживать capability reconstruction by need, а не полное копирование legacy.
- Создавать trace links от intent/problem к requirement и acceptance scenario.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `ProjectBrief`: purpose, users, jobs, outcomes, constraints, boundaries, non_goals, unknowns, source_refs.
- `CTR-002` — `FeatureSpecification`: behaviors, triggers, inputs, outputs, states, failures, recovery, acceptance expectations.
- `CTR-003` — `SliceOption`: slice_id, user_value, included_behavior, excluded_behavior, dependencies, risks, estimated_learning.
- `CTR-004` — `ProductDispositionDecision`: SELECT | REVISE | DEFER | REJECT; отдельный human record.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-001`, `FTR-002`, `FTR-005`, `FTR-006`, `FTR-031`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Не утверждает architecture, implementation repository, dependencies, roadmap priority или execution.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Specification становится энциклопедией.
- Proposal воспринимается как accepted requirement.
- Technical Assignment дублирует Project Brief/Task Brief.
- First slice выбирается по internal completeness, а не user outcome.
- Legacy compatibility assumed without decision.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Удалить неиспользуемые sections, вернуть disputed requirement в `PROPOSAL`/`UNKNOWN`, показать варианты и human decision needed; не переходить к implementation.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Trace from Intent/Discovery facts to each requirement.
- Coverage map: user job → behavior → acceptance expectation.
- Comparison rationale for first-slice options.
- List of legacy assumptions intentionally rejected.

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

- `AC-001` — Non-technical stakeholder может объяснить purpose, user и outcome.
- `AC-002` — Selected slice даёт завершённый user-visible result.
- `AC-003` — Inputs, outputs, failures и recovery описаны.
- `AC-004` — Development Factory mechanics не подменяют product value.
- `AC-005` — Non-goals и unresolved decisions видимы.
- `AC-006` — Human selection recorded separately and exactly.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Scaffolding не выбирается first slice без direct user job/outcome.
- `NEG-002` — Feature «создать registry» отклоняется как продуктовый slice без user value.
- `NEG-003` — Legacy component name не превращается в requirement автоматически.
- `NEG-004` — Generated priority не становится roadmap commitment.
- `NEG-005` — Неверифицированная compatibility не скрывается.
- `NEG-006` — Project Brief не считается implementation.

## 22. Minimal implementation model — `PROPOSAL`

Первый вариант — document compiler над Intent/Discovery records, шаблон feature specification и deterministic completeness checks. Slice ranking остаётся advisory; достаточно Markdown + JSON projections.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: human-authored brief template and review checklist.
- M1: compiler/validator from Intent + Discovery.
- M2: slice comparison and trace map.
- M3: integration with UX Skeleton and Task Brief.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-006` — Project Brief and Specification Builder
- `IDEA-007` — Technical Assignment
- `IDEA-008` — First Vertical Slice Selector and Capability Reconstruction
- `IDEA-080` — Ready-Spec vs Build-from-Scratch Entry
- `IDEA-081` — Problem Interview with Draft Capture

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Какой user/persona является primary для первого AOS Product Runtime?
- Какой exact first slice человек выберет?
- Какова relationship to legacy AOS-FARM/AOS-02?
- Нужно ли Technical Assignment хранить отдельно от Specification?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-003`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `03 — AOS Future and Legacy Reference.txt`
- `07 - AOS-FARM — Proposed Pipeline Evolution.txt`

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

- [`IDEA-006` — Project Brief and Specification Builder](../functions/IDEA-006_project-brief-and-specification-builder.md)
- [`IDEA-007` — Technical Assignment](../functions/IDEA-007_technical-assignment.md)
- [`IDEA-008` — First Vertical Slice Selector and Capability Reconstruction](../functions/IDEA-008_first-vertical-slice-selector-and-capability-reconstruction.md)
- [`IDEA-080` — Ready-Spec vs Build-from-Scratch Entry](../functions/IDEA-080_ready-spec-vs-build-from-scratch-entry.md)
- [`IDEA-081` — Problem Interview with Draft Capture](../functions/IDEA-081_problem-interview-with-draft-capture.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_003`
