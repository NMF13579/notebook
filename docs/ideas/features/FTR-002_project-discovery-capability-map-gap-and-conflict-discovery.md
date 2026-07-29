---
document_id: AOS-FEATURE-FTR-002
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-002
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
layer: "Product Runtime"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-004
  - IDEA-005
human_review_required: true
---

# FTR-002 — Project Discovery, Capability Map and Gap/Conflict Register

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-002` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича создаёт ограниченную read-only карту существующего проекта: что в нём действительно есть, какие capabilities подтверждены, где gaps и conflicts, и что осталось непроверенным.

**Source-derived desired outcome:** Bounded read-only Discovery Report: repository identity, structure, relevant capabilities, dependencies, workflows, owners, gaps, conflicts, confidence and explicit `NOT_FOUND`/`NOT_RUN`.

## 3. Для кого и какую работу выполняет

**Target users:** Product owner, maintainer, architect, agent entering a new or legacy repository.

Основные jobs-to-be-done:

- Быстро понять незнакомый repository до постановки изменения.
- Отделить реально наблюдаемое поведение от design docs и historical claims.
- Найти owners, contracts, commands, tests и зависимости, относящиеся к конкретной feature.
- Показать gaps, conflicting sources и stale paths без преждевременного исправления.
- Подготовить компактный context для Product Brief или Task Brief.

## 4. Проблема и ожидаемая ценность

### Проблема

Человек и агент не знают фактическую структуру проекта, текущие capabilities, owners, contracts, commands и conflicts. Широкий scan легко выглядит как полная architecture assessment, хотя факты могут быть устаревшими.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Repository/worktree/branch/HEAD/baseline preflight.
- Targeted inventory релевантных docs, code, tests, commands, configs и interfaces.
- Capability Map с evidence locator, temporal scope и confidence.
- Gap/Conflict Register с impact и resolution mode.
- Explicit NOT_FOUND, NOT_RUN и excluded scope.

### Out of scope / non-goals

- Exhaustive extraction всего legacy repository.
- Автоматическое исправление gaps, refactor или dependency installation.
- Утверждение architecture или Source of Truth.
- Доказательство полного поведения проекта на основании docs.
- Continuous centralized registry в первом варианте.

## 6. Trigger и preconditions

### Triggers

- Работа начинается в existing project.
- Feature затрагивает незнакомую область repository.
- Документы, code и tests расходятся.
- Требуется восстановить capability для clean-room reimplementation.

### Preconditions

- Exact subject и разрешённый source boundary определены.
- Read-only local access подтверждён; remote/network access запрашивается отдельно.
- Repository preflight возможен либо его отсутствие объявлено BLOCKED/NOT_RUN.
- Исследование привязано к конкретному вопросу или feature.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `repository_identity`
- `worktree_path`
- `expected_branch`
- `feature_or_question_scope`
- `allowed_paths`
- `known_source_pack`
- `baseline_expectation`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Repository preflight
- Capability Map
- Gap/Conflict Register
- Source inventory subset
- Research limitations

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Confirm exact subject and source boundary.
2. Run local read-only preflight.
3. Inspect only feature-relevant paths and records.
4. Classify each observation and temporal validity.
5. Build capability/gap/conflict maps.
6. Stop on source conflict, permission expansion or sufficient answer.
7. Return report and one next action.

### Иллюстративный сценарий

1. Возникает trigger: Работа начинается в existing project.
2. Система принимает входы `repository_identity, worktree_path, expected_branch` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Repository preflight, Capability Map, Gap/Conflict Register.
5. При failure `Scan объявляется complete architecture.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
SUBJECT_UNCONFIRMED → PREFLIGHTED → TARGETED_SCAN → CLASSIFICATION → CAPABILITY_MAP_READY → GAP_REVIEW_REQUIRED | COMPLETE_WITH_LIMITATIONS | BLOCKED_SOURCE_CONFLICT
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Сначала показывается identity card: repository, worktree, branch, HEAD, dirty state и scope.
- Каждая capability имеет ярлык OBSERVED | DOCUMENTED_ONLY | HISTORICAL | BROKEN | UNKNOWN.
- Gaps группируются по влиянию на текущую feature, а не по количеству файлов.
- Пользователь видит отдельный список «не проверено» и не принимает отсутствие finding за PASS.
- Основной результат помещается в краткую карту; raw paths и команды доступны в details.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Не продолжать scan, если exact subject не подтверждён.
- `FR-002` — Фиксировать repository state перед чтением и повторно проверять его при длительном исследовании.
- `FR-003` — Каждое утверждение о capability связывать минимум с одним evidence locator.
- `FR-004` — Различать отсутствие файла, отсутствие поиска и отсутствие capability.
- `FR-005` — Не делать current claim из historical source без temporal verification.
- `FR-006` — Останавливать исследование при достаточном ответе; не расширять scope ради полноты.
- `FR-007` — Конфликтующие owners/Source-of-Truth claims выводить как HUMAN_REVIEW_REQUIRED.

## 13. Capabilities из source synthesis

- Проверять repository root, worktree, branch, HEAD, baseline, working tree status и relevant diff.
- Строить targeted inventory документов, кода, commands, tests, dependencies и interfaces.
- Различать current observation, historical reference, design-only, broken, obsolete и unknown.
- Формировать Capability Map с evidence locator и temporal scope.
- Выявлять competing Source-of-Truth claims, stale paths, duplicate owners и missing contracts.
- Собирать gap/conflict register с impact и требуемым resolution mode.
- Ограничивать исследование выбранной feature вместо exhaustive extraction.
- Показывать, что не было прочитано или выполнено.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `DiscoverySubject`: repository, worktree, branch, head, baseline, dirty_state_digest, inspected_at.
- `CTR-002` — `CapabilityObservation`: capability_id, classification, evidence_refs, temporal_scope, confidence, limitations.
- `CTR-003` — `GapRecord`: gap_id, affected_feature, missing_or_conflicting_fact, impact, resolution_mode, severity.
- `CTR-004` — `DiscoveryReport`: scope, included_paths, excluded_paths, commands_run, NOT_RUN, findings, next_required_action.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-016`, `FTR-021`, `FTR-011`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Read-only. Discovery evidence не является approval, current readiness или architecture decision.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Scan объявляется complete architecture.
- Metadata recency подменяет content recency.
- Legacy design считается implemented capability.
- Discovery расширяется на весь repository без необходимости.
- Conflicting sources silently merged.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Сузить scope, пометить affected claim `UNKNOWN_BLOCKED`/`HUMAN_REVIEW_REQUIRED`, указать exact missing source or conflict; не выбирать победивший Source of Truth самостоятельно.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Git/repository preflight output.
- Path/line/command locators for each observation.
- List of search terms and excluded areas.
- Current-vs-historical classification rationale.
- Digest or timestamp proving which repository state was inspected.

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

- `AC-001` — Другой агент может воспроизвести, где был найден каждый material fact.
- `AC-002` — Capability Map не смешивает design-only и implemented behavior.
- `AC-003` — Wrong branch/HEAD или changed subject обнаруживаются.
- `AC-004` — Untracked/dirty state классифицирован, а не автоматически скрыт или объявлен blocker.
- `AC-005` — Каждый gap имеет impact и next resolution mode.
- `AC-006` — Report не утверждает architecture completeness.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Поиск README не должен считаться проверкой runtime.
- `NEG-002` — Отсутствие теста после неполного scan не должно маркироваться NOT_FOUND.
- `NEG-003` — Historical PASS не переносится на current HEAD.
- `NEG-004` — Nested repository/symlink не расширяет scope.
- `NEG-005` — Remote search не запускается без network permission.
- `NEG-006` — Discovery не исправляет найденный conflict.

## 22. Minimal implementation model — `PROPOSAL`

Минимальная реализация — local Git/filesystem adapters, Markdown/JSON report builder и набор явных classifiers. Graph DB и semantic indexing не нужны; сначала важны provenance и honest limitations.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: manual repository preflight + targeted research template.
- M1: local CLI для identity, file inventory и evidence locators.
- M2: capability/gap schema и feature-scoped reports.
- M3: optional RAG-Light только при измеренной проблеме context selection.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-004` — Project Discovery and Capability Map
- `IDEA-005` — Gap and Conflict Discovery

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Какой минимальный набор repository facts обязателен для Product Runtime?
- Нужен ли единый capability taxonomy или достаточно feature-local IDs?
- Какие temporal/staleness thresholds допустимы?
- Какие remote sources разрешены и как оформляется network permission?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-002`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `03 — AOS Future and Legacy Reference.txt`
- `05 - AOS-FARM — справочные идеи из harness engineering.txt`

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

- [`IDEA-004` — Project Discovery and Capability Map](../functions/IDEA-004_project-discovery-and-capability-map.md)
- [`IDEA-005` — Gap and Conflict Discovery](../functions/IDEA-005_gap-and-conflict-discovery.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_002`
