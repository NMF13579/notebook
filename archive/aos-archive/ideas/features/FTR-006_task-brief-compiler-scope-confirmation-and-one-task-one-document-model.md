---
document_id: AOS-FEATURE-FTR-006
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-006
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
layer: "Product Runtime / Development Factory boundary"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-015
  - IDEA-016
  - IDEA-076
  - IDEA-087
  - IDEA-091
human_review_required: true
---

# FTR-006 — Task Generation, Task Brief, Scope Confirmation and Task/Report Compiler

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-006` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича превращает выбранный scope в один самодостаточный DRAFT Task Brief с чёткими границами, checks, stop conditions и non-grants.

**Source-derived desired outcome:** One self-contained DRAFT Task Brief that an agent can execute only after separate human authorization, plus deterministic human-readable and machine-readable projections.

## 3. Для кого и какую работу выполняет

**Target users:** Product owner, task author, executor, validator and reviewer.

Основные jobs-to-be-done:

- Передать агенту задачу без чтения всей истории.
- Зафиксировать allowed/forbidden scope и baseline.
- Не смешать plan, Task Brief и execution authorization.
- Согласовать expected result, validation и stop conditions.
- Сформировать короткий Stage Report после run.

## 4. Проблема и ожидаемая ценность

### Проблема

Product documentation is too broad for a bounded run. Informal tasks omit allowed/forbidden scope, baseline, checks, stop conditions or human gates; generated plans can be mistaken for authorization.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Task generation из accepted product/architecture/UX context.
- Scope confirmation, allowed/forbidden paths и non-goals.
- Validation plan, required checks, stop conditions и outputs.
- Human-readable Markdown + optional machine projection.
- Stage Report template and traceability.

### Out of scope / non-goals

- Execution, validation, review или Git operation.
- Автоматическое назначение Risk Profile.
- Незаметное расширение feature scope.
- Full backlog decomposition.
- Authority transfer from source documents.

## 6. Trigger и preconditions

### Triggers

- Selected feature/slice готов к bounded work item.
- Correction task требуется после finding.
- Документационная задача имеет ясный exact output.
- Existing informal task needs normalization.

### Preconditions

- Goal/outcome и exact subject известны.
- Repository state либо известен, либо preflight указан как required.
- Material architecture/dependency decisions закрыты или task ограничен research.
- Human authority fields default false.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `selected_feature_or_slice`
- `accepted_decisions`
- `repository_subject`
- `in_scope_and_out_of_scope`
- `acceptance_criteria`
- `validation_plan`
- `risk_factors`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- DRAFT Task Brief
- Scope/non-goal map
- Validation plan
- Non-grants
- Stage Report template
- Traceability links

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Select one source item and exact outcome.
2. Resolve only information required for bounded execution.
3. Draft Task Brief with non-grants.
4. Run structural and semantic validation.
5. Human reviews scope/Risk Profile and may authorize a separate EXECUTE.
6. Compiler emits consistent task/report views.
7. Stop before mutation.

### Иллюстративный сценарий

1. Возникает trigger: Selected feature/slice готов к bounded work item.
2. Система принимает входы `selected_feature_or_slice, accepted_decisions, repository_subject` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: DRAFT Task Brief, Scope/non-goal map, Validation plan.
5. При failure `Brief becomes another broad plan.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
SOURCE_SELECTED → DRAFTING → COMPLETENESS_CHECK → HUMAN_SCOPE_REVIEW → COMPLETE_DRAFT | NEEDS_REVISION | BLOCKED_DECISION → AUTHORIZATION_SEPARATE
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Описание задачи идёт первым, компактный YAML — в конце или frontmatter.
- Пользователь видит «что будет изменено» и «что точно не будет изменено».
- Missing material field отображается как конкретный blocker, а не новый большой plan.
- Task Brief показывает one next stage и stop condition.
- Authorization fields визуально отделены и по умолчанию false.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Task Brief self-contained для назначенной роли.
- `FR-002` — Goal, expected result, scope, subject, checks и stop conditions обязательны.
- `FR-003` — Accepted source decisions связываются по ID/locator, а не копируются без provenance.
- `FR-004` — Risk Profile остаётся UNASSIGNED до human decision.
- `FR-005` — Protected/destructive/network/Git actions перечисляются отдельно.
- `FR-006` — Material scope change invalidates Task Brief.
- `FR-007` — Compiler cannot create approval or execution grant.

## 13. Capabilities из source synthesis

- Generate task from accepted requirement, selected idea, backlog item or architecture clause.
- Capture goal, expected outcome, in/out of scope, paths, operations, constraints, risks, checks, reports and stop conditions.
- Separate planning completeness from execution authorization.
- Bind task to repository/worktree/branch/HEAD/baseline when execution-grade.
- Record proposed and assigned Risk Profile separately.
- Compile Markdown/YAML/JSON views without losing fields.
- Generate Stage Report skeleton and expected final report.
- Support `IDEA → DRAFT TASK → HUMAN REVIEW → SELECTED TASK` bridge.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `TaskBrief`: task_id, stage, goal, expected_result, subject, in_scope, out_of_scope, allowed_paths, forbidden_paths, required_checks, stop_conditions, outputs.
- `CTR-002` — `AuthoritySection`: proposed_risk_profile, assigned_risk_profile, execution_authorized, git_authorizations, non_grants.
- `CTR-003` — `TraceBinding`: source_requirement, decision_id, feature_id, architecture_or_ux_constraint.
- `CTR-004` — `StageReport`: actual_outputs, actual_scope, checks, findings, limitations, terminal_status, next_required_action.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-003`, `FTR-005`, `FTR-007`, `FTR-009`, `FTR-030`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Task Brief, plan, routing and selection do not authorize execution, Git or release.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Brief becomes another broad plan.
- Risk Profile inferred by agent.
- `execution_authorized: true` generated without human action.
- Compiler drops fields or changes status semantics.
- Task silently expands paths/dependencies/network.
- One task contains multiple stages or unrelated outcomes.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Reject incomplete/contradictory brief, list exact missing field or conflict, preserve source item, and return to PLAN. Any material scope change requires a new or revised brief.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Completeness validator result.
- Trace links to product/architecture/UX sources.
- Scope diff between prior draft and final draft.
- Human scope review record if provided.

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

- `AC-001` — Executor can act without inventing missing material facts.
- `AC-002` — Scope and forbidden areas are explicit.
- `AC-003` — Validation plan is executable or marked NOT_RUN/BLOCKED.
- `AC-004` — All authorization fields default false.
- `AC-005` — Task Brief does not repeat unnecessary planning when complete.
- `AC-006` — Stage Report can be generated without overstating completion.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Plan text cannot be parsed as execution authorization.
- `NEG-002` — Missing baseline cannot be silently inferred for mutating task.
- `NEG-003` — Protected path change without decision remains blocked.
- `NEG-004` — Task compiler cannot assign HIGH/LOW Risk Profile.
- `NEG-005` — Output path outside scope is rejected.
- `NEG-006` — Completion report cannot mark skipped check PASS.

## 22. Minimal implementation model — `PROPOSAL`

Markdown-first compiler with strict schema, linting, source bindings and templates. Avoid central task registry initially; files can be repository-native and human-readable.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: single Task-xxx.md template.
- M1: completeness/scope validator.
- M2: deterministic Markdown↔machine projection and Stage Report builder.
- M3: backlog/queue integration after real use.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-015` — Architecture-to-Task Traceability
- `IDEA-016` — Task Generation and Task Brief
- `IDEA-076` — Task Brief Compiler and Report Builder
- `IDEA-087` — Idea Deduplication and Promotion to DRAFT Task
- `IDEA-091` — Requirement → UX → Slice → Task → Code → Test/Evidence Traceability

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Какой минимальный YAML набор полей будет окончательно принят?
- Где хранить Task Briefs в implementation repository?
- Нужен ли machine-readable projection в baseline?
- Как идентифицировать human execution authorization?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-006`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `06 - AOS-FARM — Third Pass Temporary Implementation Plan.txt`
- `Декомпозиция ТЗ.txt`

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

- [`IDEA-015` — Architecture-to-Task Traceability](../functions/IDEA-015_architecture-to-task-traceability.md)
- [`IDEA-016` — Task Generation and Task Brief](../functions/IDEA-016_task-generation-and-task-brief.md)
- [`IDEA-076` — Task Brief Compiler and Report Builder](../functions/IDEA-076_task-brief-compiler-and-report-builder.md)
- [`IDEA-087` — Idea Deduplication and Promotion to DRAFT Task](../functions/IDEA-087_idea-deduplication-and-promotion-to-draft-task.md)
- [`IDEA-091` — Requirement → UX → Slice → Task → Code → Test/Evidence Traceability](../functions/IDEA-091_requirement-to-ux-to-slice-to-task-to-code-to-test-evidence-traceability.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_006`
