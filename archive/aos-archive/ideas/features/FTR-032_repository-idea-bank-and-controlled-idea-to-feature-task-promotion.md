---
document_id: AOS-FEATURE-FTR-032
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-032
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
layer: "Knowledge / Product planning support"
disposition: CANDIDATE_SUPPORT
source_basis: LATE_CHAT_ADDITION
source_atomic_functions: []
human_review_required: true
---

# FTR-032 — Repository Idea Bank and Controlled Idea → Feature/Task Promotion

> **Статус:** `DRAFT`, `authority: NONE`. Это подробное человекочитаемое описание candidate feature. Оно не делает feature обязательной и не разрешает implementation.

## 1. Что это

Feature family объединяет coherent user outcome и несколько атомарных функций, перечисленных в разделе 24. Она задаёт problem boundary и observable behavior, но не принимает architecture, dependencies или implementation model.

## 2. Проблема

Полезные идеи теряются в чатах или преждевременно превращаются в задачи без проверки product fit, duplicate/overlap, dependencies, scope и priority.

## 3. Пользователи

Product owner, agent, работающий с project knowledge, feature designer и task planner.

## 4. Trigger и inputs

Новая идея, lesson, external observation или feature suggestion заслуживает сохранения, но ещё не принята в product scope. Inputs: исходная формулировка, source/provenance, предполагаемый user/outcome, constraints, related features, risks и unknowns.

## 5. Observable behavior

Система сохраняет одну human-readable Idea Record, строит deterministic index, показывает duplicates, overlaps, dependencies и conflicts. Agent может подготовить promotion proposal, но только человек выбирает: Feature Contract candidate, roadmap/work package, DRAFT Task, deferred reference или rejected idea.

## 6. Outputs и state model

Outputs: idea document, idea index, duplicate/dependency map, promotion proposal и disposition history. States: `IDEA_CAPTURED → TRIAGED → DUPLICATE | NEEDS_RESEARCH | FEATURE_CANDIDATE | TASK_CANDIDATE | DEFERRED | REJECTED → HUMAN_SELECTED`.

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

- `FR-032-01` — Feature сохраняет один owner для каждого canonical fact/output.
- `FR-032-02` — Atomic function results собираются без потери individual statuses/limitations.
- `FR-032-03` — UI не скрывает `UNKNOWN`, `BLOCKED`, `NOT_RUN` или partial result.
- `FR-032-04` — Human decision/authorization не выводятся из agent result.
- `FR-032-05` — Material scope or subject change invalidates downstream DRAFT artifacts.
- `FR-032-06` — Failure приводит к report + stop; retries/stage transitions не автоматические.

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

Failure modes: repository root clutter, idea list становится backlog authority, agent создаёт executable task автоматически, старая идея silently overrides current scope. Recovery: сохранить `authority: NONE`, пересобрать derived index, отменить неавторизованную promotion и запросить human selection.

Общий recovery contract:

```text
failure/unknown
→ report + freeze observed state
→ human choice where required
→ separately authorized correction/recovery
→ separate targeted validation
```

## 13. Safety and authority

Idea, queue position и promotion proposal не авторизуют execution. Для текущего documentation repository предпочтительный storage — `docs/ideas/`, а не repository root; exact path целевого AOS остаётся отдельным repository decision.

Минимальные invariants:

- PASS/Evidence/CI/readiness ≠ approval.
- UNKNOWN/BLOCKED ≠ OK; NOT_RUN ≠ PASS.
- Agent output ≠ human decision.
- Plan/Task Brief/routing/preview ≠ execution authorization.
- Edit ≠ Commit ≠ Push ≠ PR create ≠ Merge ≠ Release.

## 14. Acceptance expectations — `DESIGNED`, tests `NOT_RUN`

Каждая идея сохраняет source и non-authority status; duplicates видимы; promotion record объясняет, почему и в какой artifact выполнено преобразование; deferred/rejected items остаются traceable. Negative case: наличие idea не означает roadmap commitment.

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

Markdown-first records и deterministic index. Consolidated `06_Features.md` может оставаться первым вариантом; split на отдельные files выполняется только при реальной пользе.

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

- Atomic function split: `NOT_DEFINED`.

`next_required_action: HUMAN_REVIEW_OF_FTR_032`
