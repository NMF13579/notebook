---
document_id: AOS-FEATURE-FTR-031
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-031
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
layer: "Product Runtime / Design-to-Development bridge"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-088
  - IDEA-089
  - IDEA-090
  - IDEA-091
human_review_required: true
---

# FTR-031 — Project UX Skeleton → Vertical Slice → Code Traceability

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-031` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича создаёт проверяемый Project UX Skeleton из Specification, получает human review, делит его на vertical slices и сохраняет traceability до Task Brief, code и Evidence.

**Source-derived desired outcome:** A versioned Project UX Skeleton describing actors, journeys, pages, elements, states, navigation, permissions and requirement provenance, validated and human-reviewed before decomposition into vertical slices and Task Briefs.

## 3. Для кого и какую работу выполняет

**Target users:** Product owner, UX/product designer, non-programmer founder, architect, developer and reviewer.

Основные jobs-to-be-done:

- Увидеть interaction model до написания кода.
- Проверить actors, journeys, pages, states, transitions, permissions и failure paths.
- Обнаружить missing/unreachable/uncovered UX objects.
- Выбрать smallest useful vertical slice.
- Не допустить drift между requirement, design, task, code и test.

## 4. Проблема и ожидаемая ценность

### Проблема

A specification can jump directly to code without a reviewable interaction model. Pages, states, permissions, failure paths and requirement coverage are discovered late; visual tools may become untraceable design sources.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Actors/journeys/pages/components/states/navigation/access model.
- Requirement-to-UX coverage and structural validation.
- Advisory pattern/market research suggestions.
- Human accept/modify/reject/defer.
- Vertical-slice decomposition and traceability bridge.

### Out of scope / non-goals

- Full Figma/browser editor baseline.
- Full-app code generation from one prompt.
- Automatic design system.
- Autonomous online scraping.
- Visual regression platform and runtime enforcement in MVP.

## 6. Trigger и preconditions

### Triggers

- Specification includes user interaction.
- Implementation would otherwise jump directly to UI code.
- Existing UX/code drift needs reconstruction.
- Vertical slice selection requires interaction coverage.

### Preconditions

- Specification and accepted architecture constraints.
- Roles/permissions and domain boundaries known enough.
- Human review available.
- Pattern/market sources treated as advisory.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `accepted_or_reviewable_specification`
- `architecture_constraints`
- `actors_roles_permissions`
- `requirements_and_acceptance_expectations`
- `pattern_library_refs`
- `optional_market_research`
- `existing_ui_observations`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Project UX Skeleton
- Actors/journeys/pages/states/navigation/access artifacts
- Coverage and validation report
- Human review package
- Vertical-slice candidates
- Task Brief bridge
- Code/Evidence trace map

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Load accepted specification and architecture constraints.
2. Generate DRAFT UX Skeleton.
3. Run deterministic structural/coverage validation.
4. Add advisory pattern/research suggestions.
5. Human reviews and revises/accepts.
6. Select smallest vertical slice.
7. Create DRAFT Task Brief.
8. After separate authorization, assemble code for that slice.
9. Validate Evidence and update trace/drift view.

### Иллюстративный сценарий

1. Возникает trigger: Specification includes user interaction.
2. Система принимает входы `accepted_or_reviewable_specification, architecture_constraints, actors_roles_permissions` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Project UX Skeleton, Actors/journeys/pages/states/navigation/access artifacts, Coverage and validation report.
5. При failure `Skeleton becomes pretty sitemap without behavior/states.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
SPEC_LOADED → UX_DRAFT → STRUCTURAL_VALIDATION → HUMAN_REVIEW → ACCEPTED_SKELETON | NEEDS_REVISION | DEFERRED → SLICE_CANDIDATES → SELECTED_SLICE → DRAFT_TASK → AUTHORIZED_CODE → VALIDATED_TRACE
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Skeleton is readable as journeys/pages/states, not only graph/json.
- Every page/state shows actor, entry, exit, permissions and failure behavior.
- Coverage report highlights orphan requirements and unreachable states.
- Pattern/market suggestions visibly remain advisory with provenance/license.
- Selected slice shows exact included journey and excluded future states.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Every UX object has stable ID and source requirement.
- `FR-002` — Loading/empty/error/permission/offline/success states modeled where relevant.
- `FR-003` — Navigation graph and access matrix validated.
- `FR-004` — Generated UX cannot invent accepted requirement silently.
- `FR-005` — Human decision required before slice/task/code progression.
- `FR-006` — Trace chain maintained through code/test/Evidence.
- `FR-007` — Drift invalidates affected slice/task and requires review.

## 13. Capabilities из source synthesis

- Build actors, journeys, page/view inventory, components/elements and navigation graph from specification.
- Model loading/empty/error/permission/offline/success states and transition rules.
- Access/role matrix and requirement-to-UX coverage map.
- Deterministic assembler and validator for missing/unreachable/uncovered UX objects.
- Pattern Library suggestions for missing pages/states/failure paths as advisory candidates.
- Optional online market pattern research with provenance, licensing and no hidden adoption.
- Human accept/modify/reject/defer decision on skeleton.
- Decompose accepted skeleton into testable vertical slices.
- Generate scoped Task Briefs and code-skeleton candidates only for authorized slices.
- Trace `requirement → UX object → slice → task → code → test/Evidence` and detect drift.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `UXSkeleton`: actors, journeys, views, elements, states, transitions, access_rules, requirement_refs, version.
- `CTR-002` — `UXValidationReport`: missing_refs, unreachable_nodes, uncovered_requirements, invalid_transitions, accessibility/security_gaps.
- `CTR-003` — `UXReviewDecision`: ACCEPT | MODIFY | REJECT | DEFER; exact skeleton version.
- `CTR-004` — `VerticalSlice`: journey_fragment, UX_objects, requirements, non_goals, dependencies, acceptance.
- `CTR-005` — `TraceMap`: requirement → UX object → slice → task → code locator → test/Evidence.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-003`, `FTR-005`, `FTR-006`, `FTR-010`, `FTR-012`, `FTR-022`, `FTR-027`, `FTR-028`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Working synthesis ID introduced in this document; not canonical. MVP excludes full Figma editor, full-app codegen, automatic design system, autonomous online scraping, runtime enforcement and visual regression platform.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Skeleton becomes pretty sitemap without behavior/states.
- Generated UI invents requirements.
- Pattern/market reference becomes accepted design silently.
- Skeleton and code drift.
- Full app code generated before slice authorization.
- Accessibility/security/error states omitted.
- Figma/browser editor becomes competing Source of Truth.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Return skeleton to DRAFT, show uncovered requirement/unreachable state/drift, invalidate affected slice/task and require revised human review before new code execution.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Specification-to-UX coverage.
- Structural/navigation/access validation.
- Human review record.
- Slice/task/code/test trace and drift checks.
- Pattern/market provenance and license notes.

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

- `AC-001` — Every in-scope requirement maps to UX object or explicit non-UX rationale.
- `AC-002` — No unreachable/orphan critical view/state.
- `AC-003` — Failure/accessibility/security states covered.
- `AC-004` — Human reviews exact skeleton version.
- `AC-005` — Selected slice is independently testable and user-visible.
- `AC-006` — Code/tests trace back without hidden full-app expansion.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Pretty sitemap with no states/transitions.
- `NEG-002` — Generated page invents requirement.
- `NEG-003` — Market pattern silently becomes accepted design.
- `NEG-004` — Full app code generated before slice authorization.
- `NEG-005` — Figma/file becomes competing Source of Truth.
- `NEG-006` — Code drift leaves trace marked current.

## 22. Minimal implementation model — `PROPOSAL`

Start as Markdown/JSON UX model, deterministic assembler/validator and trace map. Optional diagrams/Figma export are projections. Code generation limited to one authorized slice.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: human-readable UX Skeleton template.
- M1: structural/coverage validator.
- M2: slice decomposition and Task Brief bridge.
- M3: bounded code skeleton generation and drift detection.
- M4: optional design-tool integrations.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-088` — Project UX Skeleton
- `IDEA-089` — UX Pattern Library Advisory Suggestions
- `IDEA-090` — Online Market Pattern Research with Source and License Policy
- `IDEA-091` — Requirement → UX → Slice → Task → Code → Test/Evidence Traceability

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Is FTR-031 accepted as product feature?
- What representation is primary: Markdown/JSON/diagram?
- Which accessibility/security checks are baseline?
- How should design-tool artifacts relate to Source of Truth?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-031`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `03 — AOS Future and Legacy Reference.txt`
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

- [`IDEA-088` — Project UX Skeleton](../functions/IDEA-088_project-ux-skeleton.md)
- [`IDEA-089` — UX Pattern Library Advisory Suggestions](../functions/IDEA-089_ux-pattern-library-advisory-suggestions.md)
- [`IDEA-090` — Online Market Pattern Research with Source and License Policy](../functions/IDEA-090_online-market-pattern-research-with-source-and-license-policy.md)
- [`IDEA-091` — Requirement → UX → Slice → Task → Code → Test/Evidence Traceability](../functions/IDEA-091_requirement-to-ux-to-slice-to-task-to-code-to-test-evidence-traceability.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_031`
