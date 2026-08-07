---
document_id: AOS-FEATURE-FTR-009
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-009
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
layer: "Development Factory / Safety"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-018
  - IDEA-019
human_review_required: true
---

# FTR-009 — Action Preflight and Execution Preview

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-009` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича до любой mutation проверяет subject, scope, baseline, permissions и показывает точный execution preview без изменения файлов.

**Source-derived desired outcome:** Fail-closed preflight plus exact preview of subject, operations, paths, checks, permissions, unknowns and non-grants, without performing mutation.

## 3. Для кого и какую работу выполняет

**Target users:** Executor, product owner, reviewer and safety/control layer.

Основные jobs-to-be-done:

- Убедиться, что действие направлено в правильный repository/worktree/branch.
- Увидеть все planned writes, commands, network и Git side effects.
- Понять, каких permissions/decisions не хватает.
- Проверить, что Task Brief и current state всё ещё согласованы.
- Предотвратить hidden scope expansion.

## 4. Проблема и ожидаемая ценность

### Проблема

An apparently simple action may target the wrong repository, branch, baseline, path or permission boundary. Users cannot see planned side effects before execution.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Repository/task/authorization preflight.
- Scope/path/command/network classification.
- Planned operations and checks preview.
- Baseline/staleness and dirty-state assessment.
- Fail-closed reason codes.

### Out of scope / non-goals

- Mutation, auto-fix или authorization generation.
- Full validation of result.
- Risk Profile assignment.
- Recovery execution.
- Git operation itself.

## 6. Trigger и preconditions

### Triggers

- Перед каждым EXECUTE.
- Перед install/update/uninstall.
- Перед protected/destructive/network/Git operation.
- После material repository/task change.

### Preconditions

- Complete Task Brief or explicit planning blocker.
- Subject and expected baseline available.
- Requested operations can be enumerated.
- Human decisions/permissions accessible for verification.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `TaskBrief`
- `repository_state`
- `requested_operations`
- `authorization_records`
- `permission_policy`
- `expected_checks`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Preflight report
- Execution preview
- Reason codes
- Permission gaps
- Planned checks
- No-mutation claim

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Load exact Task Brief and current facts.
2. Recompute identity and permissions.
3. Classify actions and blast radius.
4. Compare requested operations to allowlists/non-goals.
5. Generate preview and unresolved conditions.
6. Human authorizes, revises or stops.
7. Execution layer must recheck at start.

### Иллюстративный сценарий

1. Возникает trigger: Перед каждым EXECUTE.
2. Система принимает входы `TaskBrief, repository_state, requested_operations` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Preflight report, Execution preview, Reason codes.
5. При failure `Preflight uses stale repository facts.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
REQUESTED → SUBJECT_CHECK → SCOPE_CHECK → AUTHORITY_CHECK → PREVIEW_READY | BLOCKED_MISMATCH | BLOCKED_PERMISSION | UNKNOWN
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Preview lists CREATE/MODIFY/DELETE/COMMAND/NETWORK/GIT separately.
- Each denied/unknown item has reason and required next action.
- No-change/read-only operations are explicitly identified.
- User confirmation refers to preview identity/digest.
- Non-grants are shown alongside granted operations.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Preflight must perform zero target mutation.
- `FR-002` — Exact repository/worktree/branch/HEAD/baseline recorded.
- `FR-003` — Planned paths normalized and checked for traversal/symlink escape.
- `FR-004` — Authorization must match subject, scope, operation and freshness.
- `FR-005` — Unexpected dirty state classified with impact.
- `FR-006` — Preview identity changes on any material input change.
- `FR-007` — Unknown required fact prevents READY.

## 13. Capabilities из source synthesis

- Verify repository/worktree/branch/HEAD/baseline and working-tree state.
- Validate complete Task Brief, exact scope, stop conditions and assigned Risk Profile.
- Classify operation: read, write, network, protected, destructive, external, Git.
- Check sandbox, network, dependencies, secrets and protected-path permissions.
- Render planned file/command mutations and validation steps.
- Detect unrelated changes and scope collisions.
- Return explicit reason codes: ready for human authorization, `BLOCKED`, `UNKNOWN`, `HUMAN_REVIEW_REQUIRED`.
- Bind preview identity to task/baseline without treating it as authorization.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `PreflightRequest`: task_id, subject, expected_baseline, requested_operations, authorization_refs.
- `CTR-002` — `PreflightCheck`: check_id, status, reason_code, evidence, remediation.
- `CTR-003` — `ExecutionPreview`: preview_id, exact_operations, paths, commands, side_effects, checks, rollback_notes, non_grants.
- `CTR-004` — `PreflightResult`: READY_FOR_AUTHORIZED_EXECUTE | BLOCKED | UNKNOWN; never approval.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-006`, `FTR-013`, `FTR-019`, `FTR-021`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Preflight/preview never grants execution, Git or architecture authority.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Preflight uses stale repository facts.
- Preview omits generated/untracked side effects.
- `READY` wording implies authorization.
- Network/destructive risk misclassified.
- Permissions inferred from prior session.
- Preflight itself mutates state.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Return fail-closed status with exact missing condition; update Task Brief or obtain scoped human permission in a separate step. Re-run preflight after any material change.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Repository preflight outputs.
- Path normalization/allowlist results.
- Authorization binding verification.
- Preview digest and no-write audit.

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

- `AC-001` — Wrong repository/branch/HEAD is detected.
- `AC-002` — All writes/commands/network/Git effects are visible.
- `AC-003` — Preflight itself leaves working tree unchanged.
- `AC-004` — Stale authorization is rejected.
- `AC-005` — Preview changes when plan changes.
- `AC-006` — User can understand exact blocker.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Symlink/path traversal outside allowed scope.
- `NEG-002` — Hidden helper command not listed in preview.
- `NEG-003` — Authorization for commit reused for push.
- `NEG-004` — Untracked file that would be overwritten detected.
- `NEG-005` — Network access attempted during local preflight without permission.
- `NEG-006` — Unknown required check cannot result READY.

## 22. Minimal implementation model — `PROPOSAL`

Thin local preflight engine over Git/filesystem/task/permission contracts. Produce machine + human preview. Do not combine with executor initially.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: Task Brief/repository identity check.
- M1: path/operation preview and reason codes.
- M2: authorization binding and plan digest.
- M3: adapters for install/Git/runtime operations.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-018` — Action Preflight
- `IDEA-019` — Execution Preview

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Какой preview identity mechanism будет принят?
- Какая freshness policy для authorization?
- Как обрабатывать benign dirty state?
- Какие commands могут быть represented safely before execution?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-009`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `05 - AOS-FARM — справочные идеи из harness engineering.txt`
- `06 - AOS-FARM — Third Pass Temporary Implementation Plan.txt`

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

- [`IDEA-018` — Action Preflight](../functions/IDEA-018_action-preflight.md)
- [`IDEA-019` — Execution Preview](../functions/IDEA-019_execution-preview.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_009`
