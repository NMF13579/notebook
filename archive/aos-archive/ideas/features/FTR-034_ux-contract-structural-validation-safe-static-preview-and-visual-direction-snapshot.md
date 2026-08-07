---
document_id: AOS-FEATURE-FTR-034
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-034
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
layer: "Product Runtime support / UX review boundary"
disposition: CANDIDATE_SUPPORT
source_basis: HISTORICAL_M47_RECONSTRUCTION_REFINED
source_atomic_functions: [IDEA-097, IDEA-098, IDEA-099, IDEA-100]
human_review_required: true
---

# FTR-034 — UX Contract, Structural Validation, Safe Static Preview and Visual-Direction Snapshot

> **Статус:** `DRAFT`, `authority: NONE`. Это подробное человекочитаемое описание candidate feature. Оно не делает feature обязательной и не разрешает implementation.

## 1. Что это

Feature family объединяет coherent user outcome и несколько атомарных функций, перечисленных в разделе 24. Она задаёт problem boundary и observable behavior, но не принимает architecture, dependencies или implementation model.

## 2. Проблема

Между Product Specification и frontend implementation нужен formal UX layer. Без него screens, flows, states, edge cases и approval points теряются, а visual preview может ошибочно выглядеть как working UI или acceptance.

## 3. Пользователи

Product owner, UX designer, frontend architect, validator и human reviewer.

## 4. Trigger и inputs

Product Specification содержит UX-relevant requirements, а `FTR-031` требует formal structure/review contract. Inputs: requirement IDs, actors, journeys, permissions, content constraints, accessibility expectations, non-goals и open questions.

## 5. Observable behavior

Feature создаёт UX Contract для screens/views, flows, states, elements, user actions, risk/approval points, edge cases, accessibility, non-goals и traceability. Validator проверяет vocabulary, required states, navigation, recovery и authority boundaries. Optional static HTML preview является visualization-only: без JavaScript, forms, enabled controls, inline handlers, network и external assets; он явно помечен `preview only, not approval`. Visual-Direction Snapshot фиксирует только reviewed direction и exact included/excluded scope.

## 6. Outputs и state model

Outputs: UX Contract, validation result, safe derived preview и Visual-Direction Snapshot. States: `SPEC_READY → UX_CONTRACT_DRAFT → VALIDATED | FAILED | BLOCKED → STRUCTURE_REVIEW → DIRECTION_RECORDED`; frontend implementation требует отдельный Task Brief.

## 7. Пользовательский flow

1. Пользователь инициирует feature через chat/CLI/UI и видит exact subject.
2. AOS проверяет upstream context, permissions и material unknowns.
3. Выполняются только необходимые atomic functions; каждая сохраняет собственный result/status.
4. Пользователь видит consolidated result, Evidence, limitations и один следующий шаг.
5. Любой human-only decision остаётся pending до реального human input.

## 8. Scope

### In scope

- Problem и observable outcome, описанные в этом dossier.
- Atomic functions из раздела 24.
- Stable IDs, provenance, explicit states, failure/recovery и human-readable outputs.

### Out of scope

- Автоматическое принятие feature в product scope.
- Неразрешённая implementation, Git delivery или release.
- Hidden dependency/provider/runtime choice.
- Scope expansion на соседние feature families без human decision.

## 9. Functional requirements — `PROPOSAL`

- `FR-034-01` — Feature сохраняет один owner для каждого canonical fact/output.
- `FR-034-02` — Atomic function results собираются без потери individual statuses/limitations.
- `FR-034-03` — UI не скрывает `UNKNOWN`, `BLOCKED`, `NOT_RUN` или partial result.
- `FR-034-04` — Human decision/authorization не выводятся из agent result.
- `FR-034-05` — Material scope or subject change invalidates downstream DRAFT artifacts.
- `FR-034-06` — Failure приводит к report + stop; retries/stage transitions не автоматические.

## 10. Contracts — `PROPOSAL`

- `FeatureInvocation`
- `AtomicFunctionResult[]`
- `FeatureAggregateView`
- `EvidenceReference[]`
- `HumanDecisionReference`
- `NextRequiredAction`

Contract invariants: stable IDs, explicit enums, source binding, no duplicate keys/silent coercion, result status separated from human acceptance.

## 11. UX behavior

- Сначала краткий status/outcome, затем details.
- Каждый blocker объясняет cause, affected subject и required human action.
- Cards/views являются derived и не становятся Source of Truth.
- Beginner/Standard/Expert mode может менять presentation, но не safety semantics.

## 12. Failure and recovery

Failure modes: unknown element, missing state/traceability/recovery, active preview control, snapshot трактуется как implementation acceptance, generated view расходится с contract. Recovery: canonical UX Contract имеет приоритет; preview регенерируется; переход к task/code блокируется до устранения defects и human decision.

Общий recovery contract:

```text
failure/unknown
→ report + freeze observed state
→ human choice where required
→ separately authorized correction/recovery
→ separate targeted validation
```

## 13. Safety and authority

Preview и snapshot не разрешают implementation, execution, task generation, Commit, Push, Merge, Release или deployment. Exact canonical path/schema и accessibility target требуют human decision.

Минимальные invariants:

- PASS/Evidence/CI/readiness ≠ approval.
- UNKNOWN/BLOCKED ≠ OK; NOT_RUN ≠ PASS.
- Agent output ≠ human decision.
- Plan/Task Brief/routing/preview ≠ execution authorization.
- Edit ≠ Commit ≠ Push ≠ PR create ≠ Merge ≠ Release.

## 14. Acceptance expectations — `DESIGNED`, tests `NOT_RUN`

Validator обнаруживает structural/authority defects; preview не содержит active behavior/network; snapshot разделяет approved visual direction и excluded scope; `NOT_RUN` остаётся видимым. Negative case: screenshot/preview не считается working product.

## 15. Required negative behavior

- Feature не выполняет соседний stage автоматически.
- Missing source/permission не маскируется default value.
- Legacy/reference content не получает authority.
- Derived UI/index не расходится с owner artifacts.
- Failure/partial state не скрываются.

## 16. Observability and Evidence

Feature aggregate должен позволять восстановить:

```text
source / human decision
→ user problem
→ requirement
→ atomic function invocation
→ output/candidate
→ check result
→ finding/limitation
→ human decision
```

## 17. Minimal implementation model — `PROPOSAL`

YAML/Markdown schema, template и validator плюс optional static generator. Figma, Storybook и design-token adapters относятся к later versions.

## 18. Rollout

1. Documentation-only contract.
2. Manual checklist flow.
3. Advisory tool.
4. Guarded execution only if needed.
5. Enforced/automated mode only after architecture/risk decisions.

## 19. Dependencies

Dependencies remain design relationships until explicitly accepted. New libraries, services, providers, registries or Control Plane require human decision.

## 20. Test strategy — `NOT_RUN`

- Unit/contract tests per atomic function.
- Integration tests for family aggregate and status preservation.
- Negative fixtures for missing input, stale source, denied permission and partial failure.
- Human-authority tests: no synthetic approval.
- Traceability test from input to Evidence.

## 21. Open human decisions

- Accept, modify, split, merge, defer or reject this family.
- Assign Product Runtime/support/deferred role.
- Approve exact contracts, paths and dependencies.
- Assign Risk Profile.
- Define required independent validation.

## 22. Source basis and limitations

- Reconstructed from accessible project chat history and read-only reference artifacts.
- Full raw chat export completeness: `UNKNOWN`.
- Current repository/runtime implementation: `NOT_RUN`.
- Detailed requirements and implementation model: `PROPOSAL`.

## 23. Promotion path

```text
DRAFT dossier
→ human product review
→ accepted Feature Contract or DEFER/REJECT
→ Task Brief
→ explicit authorization
→ EXECUTE
→ VALIDATE
→ REVIEW
→ human decision
```

## 24. Отдельные документы атомарных функций

- [`IDEA-097` — UX Contract Builder](../functions/IDEA-097_ux-contract-builder.md)
- [`IDEA-098` — UX Structural Validator](../functions/IDEA-098_ux-structural-validator.md)
- [`IDEA-099` — Safe Static Preview Generator](../functions/IDEA-099_safe-static-preview-generator.md)
- [`IDEA-100` — Visual-Direction Snapshot](../functions/IDEA-100_visual-direction-snapshot.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_034`
