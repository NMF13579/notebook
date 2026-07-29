---
document_id: AOS-FEATURE-FTR-028
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-028
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
layer: "UX wrapper"
disposition: DEFERRED
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-069
human_review_required: true
---

# FTR-028 — Workbench / SaaS UI for Onboarding, Status, Review and Collaboration

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-028` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича добавляет optional Workbench/SaaS UI поверх стабильных repository-backed contracts, не создавая отдельный источник состояния или небезопасные approval shortcuts.

**Source-derived desired outcome:** Optional UI that renders and edits accepted artifact contracts, shows source-linked state/Evidence and captures explicit human decisions while repository artifacts remain authoritative.

## 3. Для кого и какую работу выполняет

**Target users:** Non-programmer users, teams, reviewers, support and administrators.

Основные jobs-to-be-done:

- Упростить onboarding/status/review для non-programmers and teams.
- Просматривать artifacts/Evidence/decisions с provenance.
- Совместно комментировать и распределять review.
- Запускать разрешённые operations через backend boundary.
- Видеть stale/conflicting state.

## 4. Проблема и ожидаемая ценность

### Проблема

CLI/Markdown may be hard for wider teams, but building a UI before stable artifact contracts creates a second state system and unsafe approval buttons.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Onboarding/project selection.
- Status/task/review queues.
- Artifact viewers/editors through validated APIs.
- Decision/comment/collaboration records.
- Safe operation delegation and refresh.

### Out of scope / non-goals

- UI database as Source of Truth.
- Approval button without decision contract.
- Backend execution bypass.
- Mandatory SaaS for core.
- Hiding NOT_RUN/unknowns.

## 6. Trigger и preconditions

### Triggers

- CLI/chat/Markdown contracts are stable.
- Real multi-user/collaboration need observed.
- Product Runtime value proven.
- Authentication/authorization/privacy decisions accepted.

### Preconditions

- Stable artifact/status/decision APIs.
- Repository/source reconciliation.
- Identity/role model.
- Security/privacy/threat model.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `repository_backed_artifacts`
- `project_memory`
- `review_and_decision_contracts`
- `user_identity_and_roles`
- `comments_collaboration_data`
- `operation_requests`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Workbench views
- Review queue
- Artifact/decision forms
- Collaboration records
- Operation results

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Read current repository-backed artifacts.
2. Render derived UI state.
3. User edits draft or records explicit decision.
4. Write through validated contract/API.
5. Operation layer rechecks permissions.
6. Refresh and show exact result.

### Иллюстративный сценарий

1. Возникает trigger: CLI/chat/Markdown contracts are stable.
2. Система принимает входы `repository_backed_artifacts, project_memory, review_and_decision_contracts` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Workbench views, Review queue, Artifact/decision forms.
5. При failure `UI database becomes Source of Truth.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
DISCONNECTED → SYNCING → CURRENT | STALE | CONFLICT → VIEW_OR_EDIT_DRAFT → VALIDATED_WRITE → OPERATION_DELEGATED | READ_ONLY_DEGRADED
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Every view shows source freshness and provenance.
- Unknown/NOT_RUN/status semantics preserved visually.
- Decision forms show exact subject and grants/non-grants.
- Conflict disables unsafe mutation.
- Accessibility/localization included from design stage.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Repository artifacts remain authoritative.
- `FR-002` — UI writes only through validated contract/API.
- `FR-003` — Operation layer rechecks authorization.
- `FR-004` — Stale cache cannot enable action.
- `FR-005` — Decision identity/subject binding required.
- `FR-006` — Comments do not change artifact authority.
- `FR-007` — Read-only degraded mode available.

## 13. Capabilities из source synthesis

- Onboarding and project selection.
- Status/next/details and task/review queues.
- Artifact viewers/editors with provenance.
- Evidence and decision cards.
- Collaboration/comments/roles when accepted.
- Safe invocation of backend operations with rechecked authorization.
- Conflict/staleness display.
- Accessibility/localization.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `WorkbenchSnapshot`: project, source_snapshot, freshness, views, permissions.
- `CTR-002` — `ArtifactMutationRequest`: artifact_id, expected_version, patch_or_replacement, user_identity.
- `CTR-003` — `DecisionFormSubmission`: exact_subject, decision_type, value, grants, identity.
- `CTR-004` — `CollaborationRecord`: comment, location, author, status; authority NONE.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-008`, `FTR-012`, `FTR-016`, `FTR-021`, `FTR-031`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Deferred until stable CLI/artifact contracts and real collaboration need. UI cannot grant authority.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- UI database becomes Source of Truth.
- Approval button bypasses decision contract.
- Stale cache shows wrong next action.
- UI hides `NOT_RUN`/unknowns.
- Untrusted content executes in browser/backend.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Disable mutations, refresh/reconcile from repository, expose conflict and require explicit repair/decision.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Repository/UI round-trip and conflict tests.
- Authorization recheck logs.
- Accessibility/security tests.
- Stale-cache/decision negative fixtures.

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

- `AC-001` — UI reflects repository state accurately.
- `AC-002` — Stale/conflict state blocks unsafe writes.
- `AC-003` — Approval cannot bypass decision contract.
- `AC-004` — NOT_RUN/unknowns visible.
- `AC-005` — Core remains usable without UI.
- `AC-006` — Accessibility baseline met.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — UI cache shows completed task after repository change.
- `NEG-002` — Database record overrides file owner.
- `NEG-003` — Button performs merge with review authorization only.
- `NEG-004` — Untrusted artifact content executes.
- `NEG-005` — Comment interpreted as human decision.
- `NEG-006` — UI outage blocks local core workflow.

## 22. Minimal implementation model — `PROPOSAL`

Deferred. Build after stable chat/CLI/artifact contracts. Use repository-backed API and derived cache only; start read-only before mutations/collaboration.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: no UI; stable contracts.
- M1: read-only status/review dashboard.
- M2: draft artifact editing and decision forms.
- M3: collaboration/operations after security validation.

**Disposition rule:** Не включать в ранний core; вернуться после стабилизации Product Runtime и появления реального extension need.

## 24. Related micro-features

- `IDEA-069` — Workbench / SaaS UI

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Is SaaS actually needed versus local app/TUI?
- What identity/role model?
- Where is data hosted and retained?
- Which collaboration features justify complexity?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-028`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
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

- [`IDEA-069` — Workbench / SaaS UI](../functions/IDEA-069_workbench-saas-ui.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_028`
