---
document_id: AOS-FEATURE-FTR-029
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-029
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
layer: "Packaging / Extension support"
disposition: DEFERRED_RESEARCH
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-070
  - IDEA-077
human_review_required: true
---

# FTR-029 — Template Export, Prompt Packs, Capability Modules, Cross-Repo Context, Localization and Policy Overlays

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-029` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича безопасно экспортирует, импортирует, обновляет и удаляет static template/prompt packs с manifest, provenance, conflict detection и без переноса authority.

**Source-derived desired outcome:** Versioned manifest-based export/import/update/uninstall for static packs with provenance, ownership, compatibility, conflict detection and no authority transfer.

## 3. Для кого и какую работу выполняет

**Target users:** AOS maintainers, adopters, teams sharing templates/prompts and multi-repository projects.

Основные jobs-to-be-done:

- Повторно использовать templates/prompts между проектами.
- Обновлять pack без потери local modifications.
- Поддерживать localization, сохраняя IDs/status semantics.
- Ограничивать cross-repo context.
- Отделить static pack от executable extension.

## 4. Проблема и ожидаемая ценность

### Проблема

Copies of templates/prompts drift, updates overwrite local changes, localization changes semantics, and imported packs can smuggle authority or executable instructions.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Static pack manifest/version/provenance.
- Previewed export/install/update/uninstall.
- Conflict and ownership handling.
- Localization/policy overlay validation.
- Explicit cross-repo source boundary.

### Out of scope / non-goals

- Executable plugin marketplace.
- Automatic policy distribution.
- Authority transfer to target.
- Unbounded cross-repo RAG.
- Silent overwrite of local content.

## 6. Trigger и preconditions

### Triggers

- Team shares templates/prompts/config across projects.
- Localized variant is needed.
- Pack update/uninstall requested.
- Task needs bounded cross-repo reference context.

### Preconditions

- Static content boundary clear.
- Source/provenance/version known.
- Ownership/conflict policy.
- Allowed repositories and permission.
- Localization semantics/tests.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `pack_manifest`
- `source_assets`
- `target_repository`
- `installed_manifest`
- `local_modifications`
- `locale_or_policy_overlay`
- `allowed_cross_repo_sources`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Pack manifest
- Export/import plan
- Installed static assets
- Conflict/update report
- Provenance/version

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Select pack/source and inspect manifest.
2. Validate provenance/version/references.
3. Preview target changes/conflicts.
4. Human authorizes import/update.
5. Apply static content only.
6. Verify idempotency/integrity.
7. Support safe uninstall.

### Иллюстративный сценарий

1. Возникает trigger: Team shares templates/prompts/config across projects.
2. Система принимает входы `pack_manifest, source_assets, target_repository` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Pack manifest, Export/import plan, Installed static assets.
5. При failure `Imported prompt grants execution.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
UNINSPECTED → VALIDATED → PREVIEW_READY → HUMAN_AUTHORIZED → INSTALLED | UPDATED | CONFLICT | REMOVED | REJECTED_UNSAFE
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Preview lists create/replace/merge/skip/conflict.
- Pack card shows source/version/license/authority NONE.
- Localization diff highlights status/authority semantic changes.
- Cross-repo sources are named explicitly.
- Executable content is rejected or routed to FTR-026.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Manifest covers all owned static assets and references.
- `FR-002` — Update detects local modifications.
- `FR-003` — Repeated install/update idempotent.
- `FR-004` — Imported prompt cannot grant execution/authority.
- `FR-005` — Localization preserves stable IDs/enums/decision semantics.
- `FR-006` — Cross-repo reads require explicit allowed list.
- `FR-007` — Uninstall removes only pack-owned unchanged assets.

## 13. Capabilities из source synthesis

- Static template/prompt pack manifest and version.
- Export/install/update/uninstall planning.
- Preserve local modifications and show conflicts.
- Cross-reference/package integrity validation.
- Cross-repo context with explicit allowed repositories.
- Localization preserving IDs/status/authority semantics.
- Policy overlays that cannot weaken core safety.
- Later capability modules only through FTR-026.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `PackManifest`: pack_id, version, type, source, license, assets, references, ownership, compatibility.
- `CTR-002` — `PackPlan`: operation, target, changes, conflicts, local_modifications, permissions.
- `CTR-003` — `LocalizationValidation`: source_locale, target_locale, stable_tokens, semantic_findings.
- `CTR-004` — `PackResult`: installed_version, effects, conflicts, verification, rollback.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-004`, `FTR-019`, `FTR-021`, `FTR-026`, `FTR-030`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

No target authority transfer, marketplace, automatic policy distribution or executable modules in baseline.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Imported prompt grants execution.
- Translation changes status semantics.
- Stale manifest overwrites local work.
- Broken references or missing source.
- Cross-repo reads exceed permission.
- Executable code loaded as template.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Abort/rollback owned static changes, preserve local files, reject unsafe pack and restore previous version from manifest.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Manifest/reference/integrity checks.
- Before/after ownership and local-modification comparison.
- Localization semantic tests.
- Cross-repo access audit.

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

- `AC-001` — Provenance/version visible.
- `AC-002` — Local changes preserved or conflict shown.
- `AC-003` — Broken references detected.
- `AC-004` — Repeated update idempotent.
- `AC-005` — Imported prompt cannot authorize action.
- `AC-006` — Uninstall is safe.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Stale manifest overwrites local work.
- `NEG-002` — Translation changes PASS/approval semantics.
- `NEG-003` — Missing referenced file accepted.
- `NEG-004` — Executable script hidden as template.
- `NEG-005` — Unauthorized repository indexed/read.
- `NEG-006` — Pack import creates canonical owner.

## 22. Minimal implementation model — `PROPOSAL`

Manifest-based static package format reusing installer planning/ownership. Support templates/prompts first; overlays/cross-repo later; executable modules only through FTR-026.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: manual static pack format.
- M1: preview/install/update/uninstall.
- M2: localization validation.
- M3: bounded cross-repo context and policy overlays.

**Disposition rule:** Сохранить как research candidate. Bounded research начинается только после конкретного use case и human scope decision.

## 24. Related micro-features

- `IDEA-070` — Template Export, Prompt Packs, Capability Modules, Cross-Repo Context, Localization and Policy Overlays
- `IDEA-077` — Manifest, Package Integrity and Cross-Reference Validator

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Which pack types are needed first?
- How to handle mergeable text versus owned immutable files?
- What localization languages/status tokens?
- What licensing/provenance requirements?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-029`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `03 — AOS Future and Legacy Reference.txt`
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

- [`IDEA-070` — Template Export, Prompt Packs, Capability Modules, Cross-Repo Context, Localization and Policy Overlays](../functions/IDEA-070_template-export-prompt-packs-capability-modules-cross-repo-context-localization-and-policy.md)
- [`IDEA-077` — Manifest, Package Integrity and Cross-Reference Validator](../functions/IDEA-077_manifest-package-integrity-and-cross-reference-validator.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_029`
