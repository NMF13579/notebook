---
document_id: AOS-FEATURE-FTR-004
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-004
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
layer: "Product Runtime candidate / Development Factory boundary"
disposition: HUMAN_DECISION_REQUIRED
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-042
  - IDEA-043
  - IDEA-044
  - IDEA-045
  - IDEA-046
human_review_required: true
---

# FTR-004 — Safe Install, Update, Uninstall, Bootstrap and Project Scaffolding

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-004` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича безопасно создаёт или подключает минимальную основу AOS в целевом repository через inspect, preview, human selection, bounded apply и verification.

**Source-derived desired outcome:** Predictable inspect → plan → human selection → safe materialization → verification → stop flow with exact manifest, conflict handling, version detection, update/uninstall safety and beginner onboarding.

## 3. Для кого и какую работу выполняет

**Target users:** Project owner adopting AOS, maintainer, installation agent and first-time user.

Основные jobs-to-be-done:

- Создать greenfield scaffold без копирования legacy complexity.
- Подключить AOS к существующему project без silent overwrite.
- Понять, какие файлы принадлежат installer, пользователю и shared ownership.
- Безопасно выполнить update, repair или uninstall.
- Дать новичку первый понятный маршрут после установки.

## 4. Проблема и ожидаемая ценность

### Проблема

Установка или scaffold может silently overwrite root files, копировать legacy complexity, создавать неверную project boundary или смешивать AOS product files с target-project data.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Repository identity и install mode selection.
- Dry-run/preview, conflict classification и ownership manifest.
- Minimal scaffold/materialization только разрешённых paths.
- Version detection, idempotency, update/uninstall planning.
- Post-install Self-Test/Doctor и FIRST-START instructions.

### Out of scope / non-goals

- Выбор implementation repository для AOS core.
- Установка runtime dependencies без отдельного решения.
- Silent merge root files или destructive cleanup.
- Копирование legacy implementation как default scaffold.
- Автоматический Commit/Push/PR.

## 6. Trigger и preconditions

### Triggers

- Новый AOS repository создаётся с нуля.
- AOS package подключается к existing target repository.
- Требуется update, repair, migration или uninstall.
- First-start diagnosis показывает неполную установку.

### Preconditions

- Repository/worktree/branch/HEAD проверены.
- Target boundary и install mode выбраны человеком.
- Package/template version известна.
- Write/network permissions и allowed paths явны.
- Backup/recovery conditions определены.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `target_repository`
- `operation_type`
- `package_or_template_identity`
- `install_profile`
- `existing_file_inventory`
- `ownership_policy`
- `authorization_record`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Install/scaffold plan
- Ownership manifest
- Materialized minimal structure
- Verification report
- Manual conflict instructions

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Inspect target repository and existing files.
2. Generate exact install/scaffold manifest.
3. Classify conflicts and ownership.
4. Human accepts file set and operation.
5. Materialize only allowed items.
6. Run self-test/doctor/manifest verification.
7. Report result and stop; update/uninstall are separate operations.

### Иллюстративный сценарий

1. Возникает trigger: Новый AOS repository создаётся с нуля.
2. Система принимает входы `target_repository, operation_type, package_or_template_identity` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Install/scaffold plan, Ownership manifest, Materialized minimal structure.
5. При failure `Root files overwritten or merged heuristically.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
UNINSPECTED → INSPECTED → PLAN_READY → HUMAN_SELECTION → APPLYING → VERIFIED → INSTALLED | UPDATE_READY | UNINSTALL_READY | CONFLICT | RECOVERY_REQUIRED
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Preview показывает exact create/modify/skip/conflict operations.
- Каждый conflict получает manual resolution instruction; overwrite никогда не скрыт.
- После apply пользователь видит, что изменилось, что осталось untouched и как откатить.
- FIRST-START содержит не более нескольких безопасных команд/действий.
- Scaffold описывает границу Product Runtime vs Development Factory.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Dry-run не должен иметь side effects и обязан быть repeatable.
- `FR-002` — Apply привязывается к неизменившемуся preview/baseline.
- `FR-003` — Installer не пишет за пределами allowed paths, включая symlink escapes.
- `FR-004` — Owned, shared и user-owned files различаются в manifest.
- `FR-005` — Update сохраняет local modifications либо останавливается с conflict.
- `FR-006` — Uninstall удаляет только доказанно owned assets и не удаляет user data.
- `FR-007` — Post-install validation отделяет technical result от human acceptance.

## 13. Capabilities из source synthesis

- `Installer Dry-run` с exact file/action plan и conflict list.
- `Safe Apply` или manual transfer без silent overwrite.
- Installation manifest, source/version/provenance detection and idempotency.
- Safe update preserving local changes; explicit conflicts instead of blind replacement.
- Safe uninstall removing only owned files and retaining user-owned data.
- Minimal project scaffold from accepted scope: directories, agent instructions, task/report templates and first checks.
- Example project, first-start guide and Beginner Tutor.
- Explicit separation of `/aos/` product package, target `drafts/`, `tasks/`, `reports/` and temporary `/.aos-tmp/`.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `InstallPlan`: subject, operation, source_version, target_version, operations, conflicts, permissions, rollback_notes.
- `CTR-002` — `OwnershipManifest`: path, owner_class, source_digest, installed_digest, local_modified, removal_policy.
- `CTR-003` — `InstallResult`: applied_operations, skipped, conflicts, verification, partial_effects, recovery_required.
- `CTR-004` — `FirstStartCard`: current_status, first_safe_actions, documentation_entrypoint, support_diagnostics.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-009`, `FTR-011`, `FTR-016`, `FTR-019`, `FTR-029`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Whether scaffolding is a Product Runtime feature or enabling stage remains a human product decision. No runtime/executor/CI/dependency installation is implied.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Root files overwritten or merged heuristically.
- Generated scaffold is mistaken for implemented product.
- Uninstall removes user files.
- Version/update provenance is stale.
- Canonical artifacts stored under `/.aos-tmp/`.
- Scaffolding consumes first slice without user value.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Abort before write on unresolved conflict; after partial write, use manifest-driven rollback for owned additions only and leave ambiguous files untouched for human review.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Before/after file inventory and ownership manifest.
- Dry-run/apply plan identity comparison.
- No-side-effect check for dry-run.
- Self-Test/Doctor/Validate results with NOT_RUN.
- Idempotency and uninstall preservation checks.

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

- `AC-001` — Wrong repository/changed HEAD blocks apply.
- `AC-002` — No existing user file is silently overwritten.
- `AC-003` — Repeat install produces no unintended change.
- `AC-004` — Partial failure leaves recoverable state and exact manifest.
- `AC-005` — Uninstall preserves user/project data.
- `AC-006` — Новичок понимает первый safe action.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Preview and apply baseline mismatch.
- `NEG-002` — Symlink escapes target boundary.
- `NEG-003` — Existing AGENTS/README/config conflicts are not overwritten.
- `NEG-004` — Missing verification cannot produce PASS.
- `NEG-005` — Update from unknown version stops.
- `NEG-006` — Uninstall with ambiguous ownership refuses deletion.

## 22. Minimal implementation model — `PROPOSAL`

Минимальный вариант — planner + manifest + bounded file materializer + local verification adapters. Начать с scaffolding/static files; package manager, remote downloads и plugin installation отложить.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: documentation-only greenfield scaffold specification.
- M1: local dry-run and manifest generator.
- M2: safe apply/update/uninstall for static owned files.
- M3: packaging/distribution only after product repository and target format are accepted.

**Disposition rule:** Сначала требуется human decision о самой product boundary; реализация и priority остаются BLOCKED для обязательного scope.

## 24. Related micro-features

- `IDEA-042` — Installer Dry-run
- `IDEA-043` — Safe Apply and Manual Transfer
- `IDEA-044` — Safe Update and Uninstall
- `IDEA-045` — Installation Manifest and Version Detection
- `IDEA-046` — Example Project and Onboarding

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Scaffolding — product feature или enabling stage?
- Какая минимальная directory structure нужна first Product Runtime task?
- Какой install distribution target выбран?
- Какие root files допускают shared ownership?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-004`.

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

- [`IDEA-042` — Installer Dry-run](../functions/IDEA-042_installer-dry-run.md)
- [`IDEA-043` — Safe Apply and Manual Transfer](../functions/IDEA-043_safe-apply-and-manual-transfer.md)
- [`IDEA-044` — Safe Update and Uninstall](../functions/IDEA-044_safe-update-and-uninstall.md)
- [`IDEA-045` — Installation Manifest and Version Detection](../functions/IDEA-045_installation-manifest-and-version-detection.md)
- [`IDEA-046` — Example Project and Onboarding](../functions/IDEA-046_example-project-and-onboarding.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_004`
