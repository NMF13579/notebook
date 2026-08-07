---
document_id: AOS-FEATURE-FTR-016
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-016
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
  - IDEA-035
  - IDEA-036
  - IDEA-037
  - IDEA-038
  - IDEA-085
human_review_required: true
---

# FTR-016 — Project Memory, Session Handoff, Context Priority and Task-Scoped Context Pack

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-016` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича восстанавливает project/session state из owned sources и собирает небольшой context pack для конкретной роли и задачи.

**Source-derived desired outcome:** Minimal durable project/session state derived from owned sources, plus a compact role/task-specific context pack that can be rebuilt and verified on resume.

## 3. Для кого и какую работу выполняет

**Target users:** User, new session/agent, task author, executor and reviewer.

Основные jobs-to-be-done:

- Ответить «на чём мы остановились?» на основании repository, а не только chat memory.
- Передать следующему agent только релевантный context.
- Сохранить decisions, blockers, candidate и next action между сессиями.
- Не создавать второй Source of Truth.
- Обнаружить stale context после repository change.

## 4. Проблема и ожидаемая ценность

### Проблема

State is scattered across chats, branches, docs and reports. Loading everything overwhelms the model; relying on chat memory misses repository changes and can carry stale authority.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Project Memory derived record.
- Session Handoff.
- Context priority rules.
- Task/role-scoped context pack.
- Resume delta and staleness checks.

### Out of scope / non-goals

- Full conversation archive as canonical state.
- Unbounded context loading.
- Automatic authority inheritance.
- Vector DB by default.
- Editing owners through generated summary.

## 6. Trigger и preconditions

### Triggers

- New session/agent starts.
- Stage completes or stops.
- User asks to resume.
- Task is routed to specialist/reviewer.
- Context window must be reduced.

### Preconditions

- Fact-class owners/source precedence defined.
- Repository/session subject can be verified.
- Generated memory is rebuildable.
- Sensitive sources can be excluded/redacted.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `repository_identity_and_state`
- `active_TaskBrief`
- `StageReports`
- `accepted_decisions`
- `current_candidate_and_evidence`
- `open_findings`
- `role_and_task_scope`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Project Memory record
- Session Handoff
- Task-scoped context pack
- Source/exclusion map
- Resume delta

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Read current owned facts.
2. Resolve source priority/conflicts.
3. Generate minimal state and role pack.
4. New session verifies repository facts.
5. Show deltas/staleness.
6. Continue only through current allowed stage.

### Иллюстративный сценарий

1. Возникает trigger: New session/agent starts.
2. Система принимает входы `repository_identity_and_state, active_TaskBrief, StageReports` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Project Memory record, Session Handoff, Task-scoped context pack.
5. При failure `Memory becomes duplicate Source of Truth.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
NO_CONTEXT → SOURCES_VERIFIED → MEMORY_REBUILT → PACK_ASSEMBLED → SESSION_ACTIVE → STALE_DETECTED | HANDOFF_READY
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Resume summary states last completed stage, current subject, blockers and one next action.
- Each memory item includes source owner and freshness.
- Context pack lists included and excluded sources.
- User can request details without loading everything.
- Stale/conflicting items are highlighted, not silently merged.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Repository/current artifacts outrank prior chat summaries.
- `FR-002` — Memory record is derived and rebuildable.
- `FR-003` — Only accepted decisions retain authority; copied text does not.
- `FR-004` — Task pack contains minimum sufficient context for assigned role.
- `FR-005` — Staleness checked against repository/subject identities.
- `FR-006` — Unknown/conflict survives handoff.
- `FR-007` — Sensitive data excluded according to policy.

## 13. Capabilities из source synthesis

- Persist identity, active slice/stage, selected task, decisions, findings, checks, permissions/non-grants and next action.
- Generate Session Handoff with exact sources and staleness markers.
- Context precedence: human decision → accepted canonical doc → current facts → task docs → lessons → reference.
- Task-scoped context packs by role: architect, executor, reviewer, docs agent.
- Explicit excluded/low-authority sources.
- Rebuild derived views from repository records.
- Detect drift between handoff and current state.
- Do not carry execution/Git authorization across sessions.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `ProjectMemory`: project_id, source_snapshot, active_work, accepted_decisions, candidates, blockers, lessons, next_action.
- `CTR-002` — `SessionHandoff`: previous_session, completed_stage, outputs, findings, not_run, unresolved_decisions, resume_requirements.
- `CTR-003` — `ContextPack`: role, task, included_refs, excerpts_or_summaries, exclusions, freshness, authority_notes.
- `CTR-004` — `ContextPriorityPolicy`: fact_class → owner/source precedence.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-002`, `FTR-008`, `FTR-014`, `FTR-021`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Memory records facts and non-grants; they do not approve or authorize. Persistence mechanism remains an architecture decision.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Memory becomes duplicate Source of Truth.
- Recency overrides authority.
- Authorization survives session change.
- Context pack omits material conflict.
- Full repository/chat loaded by default.
- Derived status edited manually.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Discard/rebuild derived view from current sources, mark conflicting facts and require human resolution only where authority is affected.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Fresh source snapshot used to rebuild memory.
- Included/excluded source map.
- Staleness/conflict checks.
- Context pack size/relevance and task outcome measurements.

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

- `AC-001` — New agent can resume without relying on hidden chat context.
- `AC-002` — Changed HEAD/candidate marks old handoff stale.
- `AC-003` — Accepted decision provenance is preserved.
- `AC-004` — Context pack omits unrelated material.
- `AC-005` — Unknowns/blockers are not lost.
- `AC-006` — Generated memory can be deleted and rebuilt.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Chat claim cannot override accepted repository fact.
- `NEG-002` — Stale context cannot authorize execution.
- `NEG-003` — Generated summary cannot become canonical owner.
- `NEG-004` — Secret/sensitive content is not copied blindly.
- `NEG-005` — Handoff cannot mark skipped validation complete.
- `NEG-006` — Pack for reviewer cannot include write authorization by implication.

## 22. Minimal implementation model — `PROPOSAL`

Repository-native memory/handoff documents with deterministic assembler. Use explicit source lists and summaries first; add RAG-Light only after scale/quality metrics show need.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: one Session Handoff template.
- M1: rebuildable Project Memory and `/resume`.
- M2: role/task-scoped context packs.
- M3: optional local index/retrieval.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-035` — Project Memory
- `IDEA-036` — Session Handoff
- `IDEA-037` — Context Priority Rules
- `IDEA-038` — Task-scoped Context Pack
- `IDEA-085` — Repository-Verified Session Resume: «На чём мы остановились?»

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- What artifact is the primary owner of current project state?
- Where should durable memory live in implementation repository?
- How much chat history should be retained?
- What freshness rules are sufficient?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-016`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
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

- [`IDEA-035` — Project Memory](../functions/IDEA-035_project-memory.md)
- [`IDEA-036` — Session Handoff](../functions/IDEA-036_session-handoff.md)
- [`IDEA-037` — Context Priority Rules](../functions/IDEA-037_context-priority-rules.md)
- [`IDEA-038` — Task-scoped Context Pack](../functions/IDEA-038_task-scoped-context-pack.md)
- [`IDEA-085` — Repository-Verified Session Resume: «На чём мы остановились?»](../functions/IDEA-085_repository-verified-session-resume.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_016`
