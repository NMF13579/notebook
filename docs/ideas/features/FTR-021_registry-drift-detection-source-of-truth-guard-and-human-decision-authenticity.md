---
document_id: AOS-FEATURE-FTR-021
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-021
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
layer: "Shared control / Integrity"
disposition: CANDIDATE_CORE_SAFETY
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-028
  - IDEA-059
human_review_required: true
---

# FTR-021 — Source-of-Truth, Registry/Schema Drift and Human Decision Authenticity Guard

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-021` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича закрепляет одного owner для каждого fact class, проверяет drift между docs/schema/runtime/indexes и не допускает, чтобы generated data или agent output выглядели как human authority.

**Source-derived desired outcome:** One owner per fact class, derived/rebuildable indexes, strict drift detection, round-trip integrity and authentic human decision binding.

## 3. Для кого и какую работу выполняет

**Target users:** All tools consuming project state; maintainers, validators and reviewers.

Основные jobs-to-be-done:

- Понять, где находится authoritative owner конкретного факта.
- Обнаружить расхождение docs, schemas, runtime models и generated indexes.
- Не потерять данные при round-trip через loaders/registries.
- Проверить, что human decision относится к exact subject и действительно human-authored.
- Восстановить derived views без изменения owner source.

## 4. Проблема и ожидаемая ценность

### Проблема

Registries, generated indexes, schemas, runtime models and decision records can diverge or silently lose data. Multiple owners produce conflicting truth, and agent-generated decisions may look human.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Fact-class ownership map.
- Source-of-Truth precedence checks.
- Schema/runtime/document/registry drift detection.
- Round-trip no-loss audit.
- Human decision authenticity and subject binding.

### Out of scope / non-goals

- Создание central registry как default.
- Automatic canonicalization or conflict resolution.
- Identity provider selection без human decision.
- Исправление owner artifact during validation.
- Признание generated index authoritative.

## 6. Trigger и preconditions

### Triggers

- Несколько artifacts претендуют на один fact class.
- Schema/runtime/docs changed independently.
- Registry/index round-trip may drop fields.
- Human decision unlocks protected action.
- Derived view appears stale or conflicts with owner.

### Preconditions

- Fact classes and candidate owners enumerated.
- Accepted source precedence available.
- Exact subject/decision identity can be inspected.
- Derived artifacts can be rebuilt.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `ownership_declarations`
- `source_artifacts`
- `schemas_and_runtime_models`
- `derived_indexes_or_registries`
- `human_decision_records`
- `candidate_subject_identity`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Ownership map
- Drift report
- Round-trip audit
- Authenticity result
- Rebuilt derived index

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Identify owner and derived consumers.
2. Load records strictly.
3. Compare schema/runtime/docs/index.
4. Detect loss/conflict/staleness.
5. Block only affected authority-bearing action.
6. Human resolves source conflict when required.
7. Rebuild derived views.

### Иллюстративный сценарий

1. Возникает trigger: Несколько artifacts претендуют на один fact class.
2. Система принимает входы `ownership_declarations, source_artifacts, schemas_and_runtime_models` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Ownership map, Drift report, Round-trip audit.
5. При failure `Central registry becomes authority without decision.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
OWNERS_UNKNOWN → OWNERS_MAPPED → CONSISTENCY_CHECK → CONSISTENT | DRIFT_FOUND | OWNER_CONFLICT | DATA_LOSS_FOUND | DECISION_INVALID → HUMAN_REVIEW_REQUIRED
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Ownership map shows fact class, owner, projections and update direction.
- Drift report groups differences by impact, not just text diff.
- Decision authenticity failure explains exact missing binding/identity assurance.
- Derived view offers rebuild, not manual canonical edit.
- Conflicts remain visible until human resolution.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — One owner per fact class; projections declare derived status.
- `FR-002` — Round-trip must preserve all required fields/items/order semantics where defined.
- `FR-003` — Schema/runtime/docs compatibility checked against same version.
- `FR-004` — Human decision must bind exact subject, scope, decision type and identity.
- `FR-005` — Agent-generated decision is invalid.
- `FR-006` — Owner conflict yields HUMAN_REVIEW_REQUIRED.
- `FR-007` — Rebuild of derived index must not change owner data.

## 13. Capabilities из source synthesis

- Source-of-Truth ownership map by fact class.
- Registry/index derived-state rule and rebuild checks.
- Schema ↔ runtime ↔ documentation parity tests.
- Round-trip no-field/no-item-loss audits.
- Duplicate IDs, broken links and stale references detection.
- Human decision authenticity, exact subject binding, supersession and revocation.
- Temporal/conflict reporting rather than silent precedence invention.
- Drift status exposed to control surface and validation.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `FactOwnershipMap`: fact_class, owner_artifact, projections, update_direction, authority.
- `CTR-002` — `DriftFinding`: sources, differing_field_or_semantics, impact, severity, resolution_owner.
- `CTR-003` — `RoundTripAudit`: input_count_fields, output_count_fields, losses, coercions, status.
- `CTR-004` — `DecisionAuthenticityResult`: decision_id, subject_match, identity_assurance, origin, freshness, valid_for_action.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-011`, `FTR-012`, `FTR-016`, `FTR-030`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Source-of-Truth and authenticity policy are protected. Human decides canonical owners and resolves material conflicts.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Central registry becomes authority without decision.
- Silent data loss.
- Schema accepts what runtime rejects or vice versa.
- Generated decision passes as human.
- Conflict resolution based on filename/recency alone.
- Drift warning treated as global blocker.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Use owner source, rebuild derived artifacts, preserve conflicting records and mark affected claims/operations `UNKNOWN_BLOCKED`; never auto-promote a source.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Source/version/digest comparison.
- Round-trip golden fixtures.
- Decision origin/subject/identity records.
- Rebuild parity results.

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

- `AC-001` — Every material fact class has one declared owner or explicit UNKNOWN.
- `AC-002` — Silent field/item loss is detected.
- `AC-003` — Generated index cannot override owner.
- `AC-004` — Agent-generated/stale/wrong-subject decision is rejected.
- `AC-005` — Drift report identifies affected feature/action.
- `AC-006` — Derived state can be rebuilt deterministically.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Two files both labelled canonical for same fact class.
- `NEG-002` — Loader drops unknown-but-required field silently.
- `NEG-003` — Schema accepts value runtime rejects.
- `NEG-004` — Decision for old candidate reused.
- `NEG-005` — Reviewer recommendation accepted as human decision.
- `NEG-006` — Generated dashboard edited as Source of Truth.

## 22. Minimal implementation model — `PROPOSAL`

Start with explicit ownership table, strict comparators and a small decision-binding validator. Do not create a generalized registry. Rebuildable indexes only.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: ownership/source-precedence documentation.
- M1: drift and round-trip checks for first contracts.
- M2: human decision authenticity guard.
- M3: broader registry/index audits as real consumers appear.

**Disposition rule:** Направление рассматривается как candidate Minimal Safety Floor, но exact mechanism, contracts и implementation требуют human decision.

## 24. Related micro-features

- `IDEA-028` — Human Decision Record and False-PASS Wording Guard
- `IDEA-059` — Registry / Drift, Source-of-Truth Guard and Human Decision Authenticity

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Which artifact owns each initial fact class?
- How is human identity assured in local/chat workflows?
- What schema/version compatibility policy is accepted?
- Which drift types are blocking versus advisory?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-021`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
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

- [`IDEA-028` — Human Decision Record and False-PASS Wording Guard](../functions/IDEA-028_human-decision-record-and-false-pass-wording-guard.md)
- [`IDEA-059` — Registry / Drift, Source-of-Truth Guard and Human Decision Authenticity](../functions/IDEA-059_registry-drift-source-of-truth-guard-and-human-decision-authenticity.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_021`
