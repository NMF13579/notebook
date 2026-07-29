---
document_id: AOS-FEATURE-FTR-007
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-007
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
layer: "Development Factory candidate"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-017
  - IDEA-075
  - IDEA-086
  - IDEA-087
human_review_required: true
---

# FTR-007 — Hierarchical Backlog, Lazy Decomposition, Queue and Repository Ideas Workspace

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-007` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича хранит идеи и крупные цели в repository, дедуплицирует их и превращает только выбранную ближайшую работу в DRAFT Task Brief.

**Source-derived desired outcome:** Repository-native, human-readable hierarchy and queue that preserves intent and links `IDEA → feature candidate → DRAFT Task → selected task`, while decomposing only near execution.

## 3. Для кого и какую работу выполняет

**Target users:** Product owner, maintainer, planning agent and executor selecting the next bounded task.

Основные jobs-to-be-done:

- Не терять идеи из чатов и обсуждений.
- Видеть связь между goal, feature, slice и task.
- Не создавать сотни stale microtasks заранее.
- Выбирать следующий bounded task с учётом blockers/dependencies.
- Сохранять причины defer/reject и не путать idea с requirement.

## 4. Проблема и ожидаемая ценность

### Проблема

Large goals are either decomposed too early into stale microtasks or kept as vague epics. Ideas scattered across chats are lost, duplicated or treated as approved requirements.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Repository Ideas Workspace.
- Hierarchical backlog и parent-child links.
- Lazy decomposition near execution.
- Queue views and task candidate promotion.
- Deduplication and status/reason tracking.

### Out of scope / non-goals

- Автономное project management.
- Автоматический выбор приоритета/исполнителя.
- Execution authorization через queue state.
- Обязательная внешняя issue tracker integration.
- Central Control Plane.

## 6. Trigger и preconditions

### Triggers

- Новая idea появляется в chat/review/incident/lesson.
- Epic становится достаточно конкретным для slice options.
- User selects next work item.
- Duplicate idea or stale task is detected.

### Preconditions

- Idea status vocabulary and owner are defined.
- Source/provenance can be recorded.
- Promotion rules separate idea, feature candidate and task.
- Human selects priority.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `idea_text`
- `source_reference`
- `related_feature_ids`
- `parent_goal`
- `constraints`
- `duplicate_candidates`
- `human_priority_or_selection`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Idea index
- Backlog hierarchy
- Queue view
- Draft task candidates
- Parent-child traceability
- Blocked/deferred reasons

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Capture idea/backlog item with source and status.
2. Classify duplicate/overlap and missing information.
3. Human chooses clarify, defer, reject or promote.
4. Decompose only the selected near-term branch.
5. Generate DRAFT Task Brief candidate.
6. Human selects and authorizes separately.
7. Update derived queue after explicit outcomes.

### Иллюстративный сценарий

1. Возникает trigger: Новая idea появляется в chat/review/incident/lesson.
2. Система принимает входы `idea_text, source_reference, related_feature_ids` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Idea index, Backlog hierarchy, Queue view.
5. При failure `Backlog inflation and excessive depth.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
CAPTURED_IDEA → TRIAGED → DUPLICATE_LINKED | FEATURE_CANDIDATE | DEFERRED | REJECTED → SLICE_CANDIDATE → DRAFT_TASK → SELECTED_FOR_AUTHORIZATION
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Idea card is brief but explains problem, value, source and next maturity step.
- Backlog view defaults to current level; children expand on demand.
- Queue shows blocked/deferred reason and one next decision.
- Duplicate suggestions are advisory and require human confirmation.
- No queue state is labelled «approved for execution» without separate decision.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Every idea keeps source and original wording.
- `FR-002` — Deduplication must preserve aliases/unique details.
- `FR-003` — Decomposition occurs only when parent is selected or near-term.
- `FR-004` — Task promotion requires enough behavior/scope/acceptance detail.
- `FR-005` — Parent-child links are acyclic and validated.
- `FR-006` — Queue ordering is advisory unless human priority exists.
- `FR-007` — Deleting an idea must not erase decision/lesson provenance.

## 13. Capabilities из source synthesis

- Hierarchy `Epic → Stage → Sub-stage → Task` with recommended depth 3–4.
- Lazy decomposition based on current blockers, dependencies and available evidence.
- Parent-child outcome and acceptance traceability.
- Queue views: list, next candidates, blocked, deferred and completed.
- `docs/ideas/README.md` style index with separate `IDEA-*` records and archive.
- Duplicate detection and merge proposals without automatic deletion/status change.
- Agent-generated DRAFT tasks from sufficiently mature ideas.
- Reverse verification: child result must contribute to parent outcome.
- One-document-per-feature/task preference to avoid registry sprawl.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `IdeaRecord`: idea_id, title, problem, value, source_refs, related_features, status, duplicate_of, notes.
- `CTR-002` — `BacklogNode`: node_id, type, parent_id, child_ids, maturity, blockers, dependencies.
- `CTR-003` — `QueueEntry`: candidate_id, readiness, priority_source, blocked_by, next_action.
- `CTR-004` — `PromotionRecord`: from_type, to_type, rationale, human_selection, created_task_id.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-006`, `FTR-016`, `FTR-021`, `FTR-030`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Idea, queue position and DRAFT task are not product acceptance or execution authorization. Human chooses priorities and promotion.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Backlog inflation and excessive depth.
- Derived queue becomes Source of Truth.
- Agent changes idea status or priority without human decision.
- Stale tasks survive product changes.
- One idea is promoted directly to execution.
- Completed child does not prove parent progress.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Rebuild views from owned records, archive superseded ideas transparently, invalidate stale tasks and return them to clarification; never auto-execute the next item.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Deduplication comparison and human choice.
- Acyclic/ID/reference validation.
- Trace from idea to feature/slice/task.
- List of stale/deferred items with reasons.

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

- `AC-001` — Idea can be found later with original context.
- `AC-002` — Duplicate merge does not lose material information.
- `AC-003` — Large goal is not fully decomposed before need.
- `AC-004` — Only selected item becomes DRAFT Task.
- `AC-005` — Queue cannot authorize execution.
- `AC-006` — Blocked reason and next action are visible.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Similar title does not auto-merge distinct ideas.
- `NEG-002` — Deleted parent cannot orphan children silently.
- `NEG-003` — Generated priority cannot overwrite human priority.
- `NEG-004` — Queue move cannot set execution_authorized true.
- `NEG-005` — Circular dependency is rejected.
- `NEG-006` — Chat history is not treated as sole durable backlog.

## 22. Minimal implementation model — `PROPOSAL`

Repository-native Markdown files plus lightweight index generator and validator. Start without database; regenerate derived views from files. Full issue tracker sync is later.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: `/ideas/` convention and single index.
- M1: deduplication suggestions + promotion template.
- M2: hierarchical backlog/queue derived view.
- M3: optional tracker integration after stable contracts.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-017` — Hierarchical Backlog, Lazy Decomposition and Queue
- `IDEA-075` — Document, Task Registry and Queue Helpers
- `IDEA-086` — Repository Ideas Workspace
- `IDEA-087` — Idea Deduplication and Promotion to DRAFT Task

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Размещать Ideas Workspace в repository root или AOS subtree?
- Какой минимальный status set нужен?
- Кто human owner priority?
- Нужен ли automatic similarity search, и после какого scale?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-007`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `Декомпозиция ТЗ.txt`
- `04 — AOS Model Routing and Task Decomposition Research.txt`

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

- [`IDEA-017` — Hierarchical Backlog, Lazy Decomposition and Queue](../functions/IDEA-017_hierarchical-backlog-lazy-decomposition-and-queue.md)
- [`IDEA-075` — Document, Task Registry and Queue Helpers](../functions/IDEA-075_document-task-registry-and-queue-helpers.md)
- [`IDEA-086` — Repository Ideas Workspace](../functions/IDEA-086_repository-ideas-workspace.md)
- [`IDEA-087` — Idea Deduplication and Promotion to DRAFT Task](../functions/IDEA-087_idea-deduplication-and-promotion-to-draft-task.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_007`
