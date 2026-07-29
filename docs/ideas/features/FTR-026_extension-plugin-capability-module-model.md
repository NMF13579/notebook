---
document_id: AOS-FEATURE-FTR-026
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-026
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
layer: "Architecture extension"
disposition: DEFERRED
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-065
  - IDEA-092
human_review_required: true
---

# FTR-026 — Extension/Plugin/Capability Module Model

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-026` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича определяет минимальный optional extension contract только после появления реальных повторяющихся extension points, сохраняя core работоспособным без extensions.

**Source-derived desired outcome:** Minimal optional extension contract admitted only after repeated real extension points, with capability declaration, compatibility, permissions, isolation, upgrade and removal.

## 3. Для кого и какую работу выполняет

**Target users:** AOS maintainer, extension developer, domain owner and product owner.

Основные jobs-to-be-done:

- Добавлять capability без раздувания core.
- Понимать extension permissions, dependencies и compatibility.
- Изолировать failure.
- Безопасно enable/disable/update/remove.
- Не позволить extension менять safety/authority.

## 4. Проблема и ожидаемая ценность

### Проблема

Future capabilities can bloat core; a speculative plugin system freezes wrong interfaces and creates dependency/security/versioning risks.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Extension manifest and capability declaration.
- Contract/API version compatibility.
- Permissions/dependencies/trust policy.
- Lifecycle enable/disable/update/remove.
- Failure isolation and health checks.

### Out of scope / non-goals

- Plugin marketplace.
- Speculative universal API.
- Third-party code loading by default.
- Extension override of core safety/Source of Truth.
- Core dependency on optional extensions.

## 6. Trigger и preconditions

### Triggers

- At least two real capabilities need same extension boundary.
- Core would otherwise accumulate domain-specific logic.
- Human accepts architecture/dependency/trust model.
- Removal/update lifecycle can be tested.

### Preconditions

- Stable core contracts.
- Observed extension points and use cases.
- Permission/trust/threat model.
- Compatibility and rollback strategy.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `extension_manifest`
- `capability_contract`
- `api_version`
- `dependencies_and_permissions`
- `source_trust`
- `configuration`
- `lifecycle_request`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Extension contract
- Manifest
- Compatibility status
- Capability index
- Lifecycle result

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Observe repeated extension need.
2. Human accepts extension boundary.
3. Validate manifest/version/permissions.
4. Load through narrow interface.
5. Run contract tests.
6. Isolate failure.
7. Support disable/update/remove.

### Иллюстративный сценарий

1. Возникает trigger: At least two real capabilities need same extension boundary.
2. Система принимает входы `extension_manifest, capability_contract, api_version` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Extension contract, Manifest, Compatibility status.
5. При failure `Plugin system before stable core.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
DISCOVERED → VALIDATED → INSTALLED_DISABLED → ENABLED → DEGRADED | DISABLED | UPDATE_READY | REMOVED | QUARANTINED
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Extension card shows source, version, capabilities, permissions and health.
- Enable preview lists effects.
- Incompatible/untrusted extension is blocked.
- Core fallback behavior visible.
- Uninstall shows owned state and preserved user data.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Core works without extensions.
- `FR-002` — Manifest declares all capabilities, permissions and dependencies.
- `FR-003` — Compatibility validated before load.
- `FR-004` — Extension cannot override human authority/Minimal Safety Floor.
- `FR-005` — Failure isolated and disableable.
- `FR-006` — Update/remove preserve user data and owned-state rules.
- `FR-007` — Third-party trust decision separate.

## 13. Capabilities из source synthesis

- Extension manifest and declared capabilities.
- Contract/API version compatibility.
- Explicit dependencies and permissions.
- Enable/disable/upgrade/remove lifecycle.
- Failure isolation and health checks.
- Derived capability index.
- Core operation without extensions.
- Third-party trust/source policy.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `ExtensionManifest`: id, version, api_version, capabilities, dependencies, permissions, entrypoint, owner, source.
- `CTR-002` — `ExtensionCompatibility`: core_version, contract_results, conflicts, status.
- `CTR-003` — `ExtensionLifecycleResult`: action, prior_state, new_state, effects, health, rollback.
- `CTR-004` — `CapabilityIndex`: derived list; authority NONE.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-004`, `FTR-019`, `FTR-020`, `FTR-021`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Deferred. Cannot override human authority or Minimal Safety Floor. Third-party loading requires separate trust decision.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Plugin system before stable core.
- Extension overrides safety/SoT.
- Dependency conflict breaks core.
- Uninstall leaves orphan state.
- Remote/malicious extension acts beyond declaration.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Disable/isolate extension, preserve core/user data, rebuild derived index and rollback extension version only where supported.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Contract/compatibility tests.
- Permission and trust review.
- Failure isolation fixtures.
- Update/uninstall preservation checks.

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

- `AC-001` — Core unaffected when extension disabled/fails.
- `AC-002` — Permissions visible and enforced.
- `AC-003` — Incompatible version rejected.
- `AC-004` — Uninstall leaves no ambiguous owned state.
- `AC-005` — Extension cannot weaken safety.
- `AC-006` — Need is based on real repeated use.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Extension loads undeclared dependency/network.
- `NEG-002` — Overrides Source of Truth.
- `NEG-003` — Failure crashes core.
- `NEG-004` — Update loses user data.
- `NEG-005` — Uninstall leaves orphan state.
- `NEG-006` — Marketplace trust implied by listing.

## 22. Minimal implementation model — `PROPOSAL`

Deferred. First identify one narrow stable interface from repeated cases. Prefer static capability modules before arbitrary code loading.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: no plugin system; document extension candidates.
- M1: one internal optional module boundary.
- M2: manifest/lifecycle/compatibility.
- M3: third-party support only after security/trust decisions.

**Disposition rule:** Не включать в ранний core; вернуться после стабилизации Product Runtime и появления реального extension need.

## 24. Related micro-features

- `IDEA-065` — Extension / Plugin Model
- `IDEA-092` — Full Multi-Agent Coordination

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Which real extension points will recur?
- What language/runtime packaging model?
- How are permissions enforced?
- What trust/signing model is needed?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-026`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
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

- [`IDEA-065` — Extension / Plugin Model](../functions/IDEA-065_extension-plugin-model.md)
- [`IDEA-092` — Full Multi-Agent Coordination](../functions/IDEA-092_full-multi-agent-coordination.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_026`
