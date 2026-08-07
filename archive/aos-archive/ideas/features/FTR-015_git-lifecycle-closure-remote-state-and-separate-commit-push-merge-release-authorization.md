---
document_id: AOS-FEATURE-FTR-015
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-015
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
layer: "Development Factory / Control"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-033
human_review_required: true
---

# FTR-015 — Git Lifecycle Closure and Publication Boundaries

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-015` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича разделяет Commit, Push, PR create, Merge и Release на независимые операции с отдельным preflight, authorization и remote verification.

**Source-derived desired outcome:** Explicit per-operation Git lifecycle with fresh preflight, exact candidate, clean scope, remote result verification and separate authorization for every irreversible boundary.

## 3. Для кого и какую работу выполняет

**Target users:** Product owner, maintainer, Git operator, reviewer and release authorizer.

Основные jobs-to-be-done:

- Не перепутать edit completion с publication.
- Проверить repository/branch/HEAD/candidate before each Git boundary.
- Не повторить push/PR/merge после потерянного ответа.
- Сохранить exact scope and evidence for each operation.
- Понять, какая human authorization ещё отсутствует.

## 4. Проблема и ожидаемая ценность

### Проблема

Edit, commit, push, PR, merge and release are often treated as one closure action. Repository/remote identity may change, and lost responses can lead to duplicate operations.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Fresh Git preflight before each operation.
- Commit, Push, PR create, Merge result contracts.
- Remote identity and response verification.
- Duplicate/lost-response handling.
- Separate boundary to Release.

### Out of scope / non-goals

- Automatic commit/push/merge/release.
- Branch protection policy selection.
- Code review replacement.
- Changing candidate during Git delivery.
- Credential/network acquisition without permission.

## 6. Trigger и preconditions

### Triggers

- Human-authorized accepted candidate is ready for a specific Git operation.
- Prior Git response is missing/ambiguous.
- Remote state may have changed.
- PR review/merge decision is pending.

### Preconditions

- Exact frozen candidate and review/decision state known.
- Repository/worktree/branch/HEAD and clean scope verified.
- Operation-specific authorization exists.
- Network and credential permissions are explicit.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `candidate_identity`
- `repository_and_remote_identity`
- `operation_type`
- `authorization_record`
- `commit_message_or_pr_metadata`
- `review_and_ci_state`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Git preflight
- Operation preview
- Commit/push/PR/merge/release result
- Remote identity evidence
- Closure state

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Recheck repository and candidate.
2. Human authorizes exactly one Git operation.
3. Perform operation.
4. Verify local/remote result.
5. Report and stop.
6. Repeat only through a new authorization for the next boundary.

### Иллюстративный сценарий

1. Возникает trigger: Human-authorized accepted candidate is ready for a specific Git operation.
2. Система принимает входы `candidate_identity, repository_and_remote_identity, operation_type` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Git preflight, Operation preview, Commit/push/PR/merge/release result.
5. При failure `Accepted result treated as push permission.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
LOCAL_ACCEPTED → COMMIT_AUTH_REQUIRED → COMMITTED → PUSH_AUTH_REQUIRED → PUSHED → PR_AUTH_REQUIRED → PR_OPEN → MERGE_AUTH_REQUIRED → MERGED → RELEASE_SEPARATE
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Each operation card shows exact subject, target and non-grants.
- UI never offers Merge because Commit was authorized.
- Lost-response flow first checks remote state.
- Result shows local and remote IDs/URLs/status.
- Release is displayed as a separate future action.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Authorization is operation-specific, subject-bound and fresh.
- `FR-002` — Fresh preflight before every operation.
- `FR-003` — Commit includes only reconciled candidate scope.
- `FR-004` — Push verifies remote/ref after response.
- `FR-005` — PR create verifies whether equivalent PR already exists.
- `FR-006` — Merge verifies review/check requirements but does not infer human approval.
- `FR-007` — No operation chains automatically into next.

## 13. Capabilities из source synthesis

- Read-only Git preflight: repository, branch, HEAD, worktree, upstream, remote identity and candidate.
- Separate `Edit`, `Commit`, `Push`, `PR create`, `Merge`, `Tag`, `Release` decisions.
- Commit content preview and scope verification.
- Push/remote status recovery before retry.
- PR metadata linked to Task Brief, Evidence and human decision.
- Merge/release readiness package without automatic action.
- One operation per authorization and exact result report.
- Distinguish local technical closure from delivered/released state.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `GitOperationRequest`: operation, repository, branch/ref, candidate, target_remote, metadata, authorization_id.
- `CTR-002` — `GitPreflight`: local_head, target_ref, remote_identity, dirty_state, candidate_match, permissions.
- `CTR-003` — `GitOperationResult`: operation, status, local_before_after, remote_before_after, external_id, ambiguity, next_action.
- `CTR-004` — `GitAuthorization`: exact operation, subject, scope, target, expiration, grants, non_grants.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-012`, `FTR-013`, `FTR-014`, `FTR-021`, `FTR-024`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Commit ≠ push ≠ PR ≠ merge ≠ release. Each is human-authorized separately.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Accepted result treated as push permission.
- Wrong branch/remote/base selected.
- Unrelated work included.
- Lost response triggers duplicate push/PR.
- Merge/release inferred from CI PASS.
- One authorization cascades to later operations.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Inspect remote/local facts before retry; preserve exact operation result, use new authorization for correction or next action, never rewrite history destructively without explicit scope.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Local Git preflight and candidate-to-diff binding.
- Remote ref/PR/merge verification.
- Authorization identity and operation match.
- No-unrelated-file commit check.

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

- `AC-001` — Commit, Push, PR, Merge and Release remain independent.
- `AC-002` — Wrong remote/branch/HEAD blocks operation.
- `AC-003` — Lost response does not cause duplicate PR/push/merge.
- `AC-004` — Commit contains exact candidate only.
- `AC-005` — Remote result is verified.
- `AC-006` — No Git action occurs from technical PASS alone.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Push authorization cannot authorize merge.
- `NEG-002` — Changed candidate after review blocks commit.
- `NEG-003` — Dirty unrelated file cannot enter commit.
- `NEG-004` — Network unavailable returns BLOCKED/UNKNOWN, not success.
- `NEG-005` — Duplicate PR is detected.
- `NEG-006` — Merge cannot imply release.

## 22. Minimal implementation model — `PROPOSAL`

Begin as explicit Git operation assistant using `git` plus connector/API adapters when available. Each command is thin, inspect-before-act, and emits structured result. No autonomous delivery chain.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: documented operation boundaries.
- M1: commit/push preflight and structured results.
- M2: PR/merge remote verification.
- M3: release integration only after real target.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-033` — Git Lifecycle Closure

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Which Git hosting/providers must baseline support?
- How is operation authorization recorded/authenticated?
- What branch model will target AOS use?
- What remote review requirements are canonical?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-015`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
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

- [`IDEA-033` — Git Lifecycle Closure](../functions/IDEA-033_git-lifecycle-closure.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_015`
