---
document_id: AOS-FEATURE-FTR-022
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-022
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
layer: "Knowledge support"
disposition: CANDIDATE_SUPPORT
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-013
  - IDEA-089
  - IDEA-090
human_review_required: true
---

# FTR-022 — Solution/Pattern Library, Fit Matrix and Reusable UX/Engineering Patterns

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-022` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича хранит проверенные UX/engineering patterns вместе с context, fit/non-fit criteria, trade-offs, failure cases и tests, чтобы patterns оставались advisory reference.

**Source-derived desired outcome:** Curated reference library where each pattern states problem, context, fit/non-fit criteria, trade-offs, provenance, failures, tests, version, owner and deprecation path.

## 3. Для кого и какую работу выполняет

**Target users:** Product designer, architect, developer, reviewer and planning agent.

Основные jobs-to-be-done:

- Не изобретать повторно удачное решение.
- Не копировать legacy code или market pattern без context.
- Сравнить pattern fit с текущей feature.
- Связать lessons с preventive tests.
- Deprecate pattern, когда условия изменились.

## 4. Проблема и ожидаемая ценность

### Проблема

Useful solutions and lessons are repeatedly reinvented or copied as cargo cult. A pattern without context, failure cases and tests becomes hidden architecture.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Pattern cards and Fit Matrix.
- Provenance, version, owner and maturity.
- Positive/negative context and trade-offs.
- Test/incident/usage links.
- Deprecation and affected-use tracking.

### Out of scope / non-goals

- Automatic architecture/design adoption.
- Code copy marketplace.
- Unbounded online scraping.
- Pattern card as canonical product requirement.
- One universal solution per problem.

## 6. Trigger и preconditions

### Triggers

- Same solution/problem recurs.
- Lesson has a reusable preventive mechanism.
- UX Skeleton or architecture needs advisory options.
- Pattern failure or compatibility change is observed.

### Preconditions

- Source/provenance and licensing can be recorded.
- Pattern context and non-fit cases known.
- At least one usage/test/incident supports value.
- Human adoption decision remains separate.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `problem_and_context`
- `solution_description`
- `source_and_license`
- `tradeoffs_and_failures`
- `fit_non_fit_criteria`
- `tests_and_usage_records`
- `owner_and_version`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Pattern card
- Fit Matrix
- Usage/compatibility notes
- Test links
- Deprecation record

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Capture repeated problem/solution observation.
2. Document context, evidence and failures.
3. Review pattern quality and fit criteria.
4. Store as reference, not default architecture.
5. Apply to one feature through fit analysis.
6. Validate outcome and update/deprecate pattern.

### Иллюстративный сценарий

1. Возникает trigger: Same solution/problem recurs.
2. Система принимает входы `problem_and_context, solution_description, source_and_license` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Pattern card, Fit Matrix, Usage/compatibility notes.
5. При failure `One-off solution becomes universal.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
CANDIDATE → REVIEWED_REFERENCE → ACTIVE_REFERENCE → DEPRECATED | WITHDRAWN; usage decisions remain separate
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Pattern card starts with when to use and when not to use.
- Fit Matrix compares current feature conditions with pattern assumptions.
- Provenance/license/maturity visible before recommendation.
- Recommendation states confidence and missing evidence.
- Deprecated patterns show replacement and affected uses.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Every pattern must include problem, context, solution, trade-offs, failures and tests.
- `FR-002` — Pattern authority is NONE.
- `FR-003` — Usage requires explicit fit assessment.
- `FR-004` — Online/legacy sources retain provenance and licensing notes.
- `FR-005` — Pattern versions and compatibility are tracked.
- `FR-006` — Failure/incident can deprecate or narrow fit.
- `FR-007` — No pattern recommendation may silently modify architecture/UX.

## 13. Capabilities из source synthesis

- Pattern cards for architecture, engineering, UX, testing and recovery.
- Fit Matrix against project constraints and user journey.
- Version, provenance, compatibility and ownership.
- Positive/negative examples and regression tests.
- Deprecation/removal path and replacement links.
- Optional online market pattern research with source/licensing policy.
- Suggestions to UX Skeleton or architecture package as advisory candidates.
- Learning loop from accepted lessons/incidents.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `PatternCard`: pattern_id, problem, context, solution, fit, non_fit, tradeoffs, failures, tests, provenance, license, maturity, owner, version.
- `CTR-002` — `FitAssessment`: feature_id, pattern_id, matched_conditions, mismatches, unknowns, recommendation.
- `CTR-003` — `PatternUsage`: subject, decision_ref, version_used, adaptations, outcome.
- `CTR-004` — `DeprecationRecord`: reason, replacement, affected_usages, effective_at.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-005`, `FTR-025`, `FTR-031`, `FTR-021`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Pattern library has `authority: NONE`; architecture/product adoption requires human decision.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- One-off solution becomes universal.
- Legacy code copied without contract.
- Pattern recommendation interpreted as decision.
- Market research ignores licenses or context.
- Library grows without owners/tests.
- Deprecated pattern remains silently active.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Withdraw/deprecate pattern, show affected uses, revert to explicit feature design and retain lesson provenance.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Source/provenance/license records.
- Usage outcome and test links.
- Fit assessment rationale.
- Deprecation impact report.

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

- `AC-001` — User can tell when pattern does not fit.
- `AC-002` — Pattern adoption remains a separate human decision.
- `AC-003` — Every recommendation has provenance.
- `AC-004` — Failures/tests are as visible as benefits.
- `AC-005` — Deprecated version is not silently recommended.
- `AC-006` — Library remains curated rather than unlimited.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — One successful example becomes universal.
- `NEG-002` — Legacy code copied without contract/license context.
- `NEG-003` — Market screenshot becomes accepted design.
- `NEG-004` — Pattern with no owner/tests marked active.
- `NEG-005` — Deprecated pattern remains default.
- `NEG-006` — Fit unknowns omitted from recommendation.

## 22. Minimal implementation model — `PROPOSAL`

Repository-native Markdown/JSON pattern cards and deterministic Fit Matrix. Search can remain simple. Online research is separate and source-bound.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: small curated manual library.
- M1: fit template and usage links.
- M2: deprecation/compatibility tracking.
- M3: optional market research ingestion with source/license controls.

**Disposition rule:** Supporting capability; допускается только после связи с конкретным user-visible workflow и измеримой пользой.

## 24. Related micro-features

- `IDEA-013` — Pattern / Solution Library and Fit Matrix
- `IDEA-089` — UX Pattern Library Advisory Suggestions
- `IDEA-090` — Online Market Pattern Research with Source and License Policy

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Who curates and accepts pattern maturity?
- Which initial UX/engineering patterns are worth retaining?
- How are licenses and copied examples handled?
- What evidence threshold promotes a candidate pattern?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-022`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `03 — AOS Future and Legacy Reference.txt`
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

- [`IDEA-013` — Pattern / Solution Library and Fit Matrix](../functions/IDEA-013_pattern-solution-library-and-fit-matrix.md)
- [`IDEA-089` — UX Pattern Library Advisory Suggestions](../functions/IDEA-089_ux-pattern-library-advisory-suggestions.md)
- [`IDEA-090` — Online Market Pattern Research with Source and License Policy](../functions/IDEA-090_online-market-pattern-research-with-source-and-license-policy.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_022`
