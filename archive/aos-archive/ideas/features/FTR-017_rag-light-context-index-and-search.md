---
document_id: AOS-FEATURE-FTR-017
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-017
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
layer: "Supporting runtime"
disposition: DEFERRED_RESEARCH
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-039
human_review_required: true
---

# FTR-017 — RAG-Light Context Index

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-017` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича создаёт необязательный локальный индекс для точечного поиска по большой документации, но возвращает только pointers/excerpts и не становится источником правды.

**Source-derived desired outcome:** Optional local provenance-aware index that returns small relevant excerpts/paths while authoritative facts remain in original repository documents.

## 3. Для кого и какую работу выполняет

**Target users:** Agents and maintainers needing targeted retrieval from larger documentation sets.

Основные jobs-to-be-done:

- Найти несколько релевантных sources без загрузки всего repository.
- Сократить token/context cost.
- Сохранить provenance и staleness каждого result.
- Измерить retrieval quality до внедрения vector infrastructure.
- Удалить/rebuild index без потери authoritative data.

## 4. Проблема и ожидаемая ценность

### Проблема

Manual context selection becomes slow as docs grow, but early vector DB/RAG infrastructure adds cost, privacy risk and a competing truth layer.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Local derived index over allowed sources.
- Keyword/metadata and optional embeddings after decision.
- Ranked source pointers with provenance.
- Staleness/invalidation.
- Retrieval quality metrics.

### Out of scope / non-goals

- Canonical knowledge base.
- Mandatory DB/vector store.
- Unbounded cross-repo retrieval.
- Automatic decision/authority from retrieved text.
- Remote embeddings for sensitive data without permission.

## 6. Trigger и preconditions

### Triggers

- Manual context selection repeatedly exceeds budget.
- Documentation volume materially slows tasks.
- Measured retrieval baseline exists.
- Specific role/task needs recurring source lookup.

### Preconditions

- Project Memory/context ownership stable.
- Allowed source boundary and privacy policy defined.
- Evaluation set and fallback search available.
- Human accepts dependencies/provider if used.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `allowed_source_files`
- `metadata_and_fact_classes`
- `index_configuration`
- `query_and_task_context`
- `freshness_snapshot`
- `evaluation_queries`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Derived context index
- Ranked source pointers
- Staleness report
- Retrieval metrics

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Select approved source boundary.
2. Build disposable/derived local index.
3. Query for one task.
4. Return small ranked source set.
5. Agent reads originals and cites them.
6. Rebuild/discard index on drift.

### Иллюстративный сценарий

1. Возникает trigger: Manual context selection repeatedly exceeds budget.
2. Система принимает входы `allowed_source_files, metadata_and_fact_classes, index_configuration` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Derived context index, Ranked source pointers, Staleness report.
5. При failure `Index becomes Source of Truth.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
DISABLED → BUILD_PLANNED → INDEXED → QUERYING → STALE → REBUILD_REQUIRED | DISABLED_NO_VALUE
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Results show file/path/section and why it matched.
- Stale index warning blocks overconfident use.
- User can open original source.
- Fallback to direct search is explicit.
- Metrics distinguish recall, precision, latency and token savings.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Index is derived and fully rebuildable.
- `FR-002` — Every result carries original source locator and snapshot identity.
- `FR-003` — Unsupported/forbidden sources excluded.
- `FR-004` — Staleness detected on source changes.
- `FR-005` — No retrieved excerpt inherits authority automatically.
- `FR-006` — Evaluation compares against simple keyword/manual baseline.
- `FR-007` — Sensitive content never leaves allowed boundary.

## 13. Capabilities из source synthesis

- Index file metadata, headings, IDs, links and compact summaries.
- Keyword/BM25-like local retrieval before embeddings.
- Filter by task, role, authority, temporal scope and repository.
- Return source pointers and confidence, not synthesized truth.
- Respect excluded/sensitive paths.
- Rebuild index deterministically and detect staleness.
- Measure retrieval value before adding vector database or remote embeddings.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `IndexManifest`: sources, snapshot, index_type, provider, privacy_mode, build_status.
- `CTR-002` — `RetrievalResult`: query, source_ref, excerpt_or_pointer, score, rationale, freshness, authority_class.
- `CTR-003` — `RetrievalEvaluation`: dataset, baseline, precision_recall, latency, token_savings, failures.
- `CTR-004` — `InvalidationRecord`: changed_sources, affected_index, rebuild_required.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-016`, `FTR-019`, `FTR-021`, `FTR-030`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Deferred until repeated retrieval pain is measured. No mandatory DB/vector store in baseline.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Index becomes Source of Truth.
- Stale summary overrides current doc.
- Sensitive data sent to provider.
- Retrieval hides conflicting documents.
- Heavy RAG built before measured need.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Invalidate index, fall back to direct repository search, expose missing/conflicting sources and keep task blocked only where necessary.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Index manifest/source coverage.
- Evaluation against known relevant sources.
- Staleness/invalidation tests.
- Privacy/provider audit.

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

- `AC-001` — Relevant sources are found at least as reliably as simple baseline.
- `AC-002` — Every result opens original source.
- `AC-003` — Stale index is detected.
- `AC-004` — Index deletion does not lose project facts.
- `AC-005` — No authority is inferred from score.
- `AC-006` — Measured benefit justifies complexity.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Changed source remains silently current.
- `NEG-002` — Forbidden repository enters index.
- `NEG-003` — Remote provider receives sensitive text without decision.
- `NEG-004` — High score treated as accepted fact.
- `NEG-005` — Index-only result with missing original source is rejected.
- `NEG-006` — Vector DB required before baseline need.

## 22. Minimal implementation model — `PROPOSAL`

Start with stdlib filename/heading/full-text index and metadata filters. Embeddings/vector store are optional later and require measured benefit, privacy and dependency decisions.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: direct search and manual benchmark.
- M1: local keyword/metadata index.
- M2: staleness and evaluation harness.
- M3: optional embeddings only if threshold met.

**Disposition rule:** Сохранить как research candidate. Bounded research начинается только после конкретного use case и human scope decision.

## 24. Related micro-features

- `IDEA-039` — RAG-light Context Index

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- What documentation scale triggers need?
- Which evaluation threshold justifies embeddings?
- Can all baseline data remain local?
- How to represent multilingual retrieval?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-017`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `04 — AOS Model Routing and Task Decomposition Research.txt`
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

- [`IDEA-039` — RAG-light Context Index](../functions/IDEA-039_rag-light-context-index.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_017`
