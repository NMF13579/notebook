---
document_id: AOS-FEATURE-FTR-030
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-030
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
layer: "Development Factory internal"
disposition: INTERNAL_RESEARCH_AFTER_CONTRACTS
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-071
  - IDEA-072
  - IDEA-073
  - IDEA-074
  - IDEA-075
  - IDEA-076
  - IDEA-077
  - IDEA-078
human_review_required: true
---

# FTR-030 — Internal Contract Tooling: Strict Loaders, Parser Sunset, Registry Audits, Manifest/Cross-Reference Validation and Schema/Runtime Drift Tests

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-030` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича создаёт небольшие strict loaders/validators/auditors вокруг уже стабильных contracts и мигрирует callers через adapter/dual-run/sunset без silent data loss.

**Source-derived desired outcome:** Small replaceable utilities that enforce accepted contracts, audit round trips/integrity, migrate callers safely and expose drift through negative tests.

## 3. Для кого и какую работу выполняет

**Target users:** AOS maintainers, test authors and tooling agents; not primary end users.

Основные jobs-to-be-done:

- Одинаково загружать/валидировать structured artifacts.
- Обнаружить parser/status fragmentation.
- Не потерять поля/items при registry round-trip.
- Проверить package manifest/cross-references.
- Безопасно вывести legacy path из эксплуатации.

## 4. Проблема и ожидаемая ценность

### Проблема

Parsers, loaders, registries, manifests and generated copies accept ambiguous input, silently lose fields or diverge. Building a generalized platform before stable contracts repeats legacy complexity.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Strict loaders and normalized models.
- Parser/status inventory and adapters.
- Round-trip no-loss audits.
- Manifest/cross-reference/schema-runtime validators.
- Golden positive/negative fixtures and sunset plan.

### Out of scope / non-goals

- Generalized Control Plane/platform.
- New central registry by default.
- Tooling before stable user need.
- Premature removal of legacy path.
- Product readiness claim.

## 6. Trigger и preconditions

### Triggers

- Stable contract has multiple callers.
- Documented data-loss/drift failure recurs.
- Package/reference integrity must be enforced.
- Legacy parser/loader needs migration.

### Preconditions

- Contract chosen and stable enough.
- Callers/formats inventoried.
- Compatibility/sunset criteria.
- Golden/negative fixtures.
- Rollback to old/adapter path.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `structured_artifacts`
- `schema_and_contract_version`
- `legacy_parser_outputs`
- `registry_or_manifest_data`
- `expected_cross_references`
- `caller_inventory`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Strict loader
- Drift/no-loss reports
- Validator utilities
- Migration/sunset plan
- Golden fixtures

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Select one stable contract and inventory callers.
2. Define strict behavior and fixtures.
3. Implement adapter beside old path.
4. Dual-run and compare.
5. Migrate callers incrementally.
6. Validate parity/no-loss.
7. Sunset old path only after accepted evidence.

### Иллюстративный сценарий

1. Возникает trigger: Stable contract has multiple callers.
2. Система принимает входы `structured_artifacts, schema_and_contract_version, legacy_parser_outputs` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Strict loader, Drift/no-loss reports, Validator utilities.
5. При failure `Tooling built before user need.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
FRAGMENTED → INVENTORIED → CONTRACT_DEFINED → ADAPTER_READY → DUAL_RUN → MIGRATED → LEGACY_SUNSET | BLOCKED_INCOMPATIBILITY
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Tools output precise field/path/reason errors.
- Migration report shows old/new parity and discrepancies.
- No-loss audit lists every dropped/coerced item.
- Sunset remains blocked until all callers migrated.
- Tool status never implies product acceptance.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Reject duplicate keys, unknown fields, unsafe aliases/paths and invalid types per contract.
- `FR-002` — Bool must not pass as integer where prohibited.
- `FR-003` — Round-trip preserves required fields/items.
- `FR-004` — Runtime and tests use same loader semantics.
- `FR-005` — Adapters support incremental migration.
- `FR-006` — Old path removal only after accepted evidence.
- `FR-007` — Utilities remain small/replaceable.

## 13. Capabilities из source synthesis

- Strict loader rejecting duplicate keys, aliases/anchors, unknown fields, bad types and unsafe paths.
- Parser/status fragmentation inventory.
- Adapter/dual-run/sunset migration.
- Registry no-loss round-trip audit.
- Manifest/package/cross-reference validator.
- Schema/runtime/module-boundary parity tests.
- Document/task registry and queue helpers.
- Task Brief compiler and report builder.
- Golden positive/negative fixtures.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `LoaderResult`: normalized_model_or_errors, schema_version, source, coercions_forbidden.
- `CTR-002` — `CallerInventory`: caller, format, loader, status_semantics, migration_state.
- `CTR-003` — `RoundTripAudit`: counts, field_map, losses, order_semantics, parity.
- `CTR-004` — `SunsetPlan`: old_path, adapters, migrated_callers, exit_criteria, rollback.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-006`, `FTR-007`, `FTR-011`, `FTR-021`, `FTR-023`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Internal tools do not prove product readiness or create authority. Dependencies/central registries require human decisions.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Tooling built before user need.
- Silent item/field loss.
- Legacy path removed too early.
- Schema version drift.
- Central registry created implicitly.
- Tool becomes irreplaceable framework.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Restore old/adapter path, stop on discrepancy, preserve audit outputs and continue migration only through a new bounded task.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Golden positive/negative fixtures.
- Old/new dual-run comparison.
- No-loss/manifest/reference reports.
- Caller migration coverage.

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

- `AC-001` — Invalid/ambiguous input rejected consistently.
- `AC-002` — No silent field/item loss.
- `AC-003` — Runtime/tests share semantics.
- `AC-004` — Migration reversible before sunset.
- `AC-005` — All callers inventoried.
- `AC-006` — Tool can be replaced without product redesign.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Duplicate key accepted.
- `NEG-002` — bool-as-int accepted.
- `NEG-003` — Unknown field discarded.
- `NEG-004` — Registry loses record.
- `NEG-005` — Manifest validates syntax but wrong subject.
- `NEG-006` — Legacy path removed with unmigrated caller.

## 22. Minimal implementation model — `PROPOSAL`

Small libraries/CLI checks organized per accepted contract. Use adapter/dual-run/sunset. Stdlib-first where practical; dependencies require human decision.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: inventory one fragmented contract.
- M1: strict loader + fixtures.
- M2: dual-run and migrate one caller.
- M3: manifest/drift utilities only as demanded.

**Disposition rule:** Internal tooling допускается только вокруг уже стабильного contract и конкретного recurring failure/consumer.

## 24. Related micro-features

- `IDEA-071` — Structured Loader Adapter and Strict Data Loader
- `IDEA-072` — Parser and Status Fragmentation Inventory with Sunset Plan
- `IDEA-073` — Registry Silent Data-Loss Audit
- `IDEA-074` — Safe Runner Kernels
- `IDEA-075` — Document, Task Registry and Queue Helpers
- `IDEA-076` — Task Brief Compiler and Report Builder
- `IDEA-077` — Manifest, Package Integrity and Cross-Reference Validator
- `IDEA-078` — Schema / Runtime Drift, Module Boundaries, Negative Fixtures, Bootstrap and Quality Tooling

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Which contract is first stable target?
- What compatibility with legacy is actually required?
- Which parser/schema library is accepted?
- When is central registry unnecessary?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-030`.

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

- [`IDEA-071` — Structured Loader Adapter and Strict Data Loader](../functions/IDEA-071_structured-loader-adapter-and-strict-data-loader.md)
- [`IDEA-072` — Parser and Status Fragmentation Inventory with Sunset Plan](../functions/IDEA-072_parser-and-status-fragmentation-inventory-with-sunset-plan.md)
- [`IDEA-073` — Registry Silent Data-Loss Audit](../functions/IDEA-073_registry-silent-data-loss-audit.md)
- [`IDEA-074` — Safe Runner Kernels](../functions/IDEA-074_safe-runner-kernels.md)
- [`IDEA-075` — Document, Task Registry and Queue Helpers](../functions/IDEA-075_document-task-registry-and-queue-helpers.md)
- [`IDEA-076` — Task Brief Compiler and Report Builder](../functions/IDEA-076_task-brief-compiler-and-report-builder.md)
- [`IDEA-077` — Manifest, Package Integrity and Cross-Reference Validator](../functions/IDEA-077_manifest-package-integrity-and-cross-reference-validator.md)
- [`IDEA-078` — Schema / Runtime Drift, Module Boundaries, Negative Fixtures, Bootstrap and Quality Tooling](../functions/IDEA-078_schema-runtime-drift-module-boundaries-negative-fixtures-bootstrap-and-quality-tooling.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_030`
