---
document_id: AOS-FEATURE-FTR-027
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-027
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
layer: "Regulated/creative domain extensions"
disposition: DEFERRED_SEPARATE_DECISIONS
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-066
  - IDEA-067
  - IDEA-068
human_review_required: true
---

# FTR-027 — Domain Modules: Design, Medical and Other Specialized Capabilities

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-027` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича выносит Design, Medical и другие domain-specific workflows в отдельные modules с собственными product, privacy, provider, validation и human-checkpoint contracts.

**Source-derived desired outcome:** Separate replaceable modules using stable core contracts, each with domain Product Contract, provider/privacy policy, specialized validators and human checkpoints.

## 3. Для кого и какую работу выполняет

**Target users:** Domain specialists, product owners and users of domain-specific AOS workflows.

Основные jobs-to-be-done:

- Использовать domain terminology/workflows без загрязнения core.
- Применить domain-specific privacy/compliance rules.
- Проверить outputs специализированными validators.
- Подключить design tools/providers через controlled boundary.
- Отключить module и вернуться к generic safe path.

## 4. Проблема и ожидаемая ценность

### Проблема

Domain rules, vocabulary, privacy and validation differ substantially. Embedding them in core increases complexity and can expose sensitive data to unapproved providers.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Domain manifest and Product Contract.
- Domain-specific intake/artifacts/validators.
- Provider/privacy/compliance policy.
- Separate threat/risk model.
- Independent lifecycle and core regression.

### Out of scope / non-goals

- Generic agent as medical/legal authority.
- Sensitive data to unapproved provider.
- Domain rules embedded in core.
- Single tool/framework lock-in.
- Automatic compliance certification.

## 6. Trigger и preconditions

### Triggers

- Concrete domain use case selected.
- Generic core cannot safely/adequately handle workflow.
- Domain expert and human owner available.
- Separate product/architecture/privacy decisions accepted.

### Preconditions

- Stable core extension contracts.
- Domain Product Contract and target users.
- Privacy/compliance/provider boundary.
- Domain expert review and negative tests.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `domain_context`
- `domain_manifest`
- `specialized_requirements`
- `sensitive_data_classification`
- `approved_providers_tools`
- `domain_patterns`
- `human_expert_decisions`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Domain contract
- Module configuration
- Specialized artifacts/validators
- Privacy/compliance record

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Select validated domain need.
2. Define domain contract and compliance constraints.
3. Human accepts module architecture/provider/dependencies.
4. Implement through extension boundary.
5. Run domain and core regression tests.
6. Enable for explicit projects/users.

### Иллюстративный сценарий

1. Возникает trigger: Concrete domain use case selected.
2. Система принимает входы `domain_context, domain_manifest, specialized_requirements` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Domain contract, Module configuration, Specialized artifacts/validators.
5. При failure `Domain complexity leaks into core.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
DOMAIN_CANDIDATE → CONTRACT_DRAFT → DOMAIN_HUMAN_REVIEW → MODULE_ENABLED | DEFERRED | REJECTED → ACTIVE → DISABLED_OR_QUARANTINED
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- User sees when domain mode is active and who reviews.
- Sensitive data/provider notice appears before transfer.
- Domain-specific outputs include limitations and human checkpoint.
- Fallback to generic mode is explicit.
- Design module shows tool/source provenance; Medical module shows privacy boundary.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Each domain has separate Product Contract and human owner.
- `FR-002` — Domain module cannot override core safety.
- `FR-003` — Sensitive data/provider policy enforced before processing.
- `FR-004` — Domain validators and negative scenarios required.
- `FR-005` — Generic model output cannot claim professional authority.
- `FR-006` — Module independently enable/disable/versioned.
- `FR-007` — Core regression tests run when module changes.

## 13. Capabilities из source synthesis

- Domain manifest and capability declaration.
- Domain-specific intake, terminology, patterns and validation.
- Medical data/provider/privacy fast-exit and compliance boundary.
- Design module for UX/UI workflows, design artifacts and optional Figma integrations.
- Separate domain risk/threat model.
- Module-specific acceptance/negative tests.
- Core fallback when module disabled.
- Independent lifecycle/versioning.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `DomainManifest`: domain_id, capabilities, data_classes, providers, validators, human_roles, version.
- `CTR-002` — `DomainPolicy`: privacy, retention, provider, compliance, prohibited_actions, escalation.
- `CTR-003` — `DomainArtifact`: type, subject, provenance, limitations, required_human_review.
- `CTR-004` — `DomainValidationResult`: specialized_checks, generic_core_checks, status, blockers.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-019`, `FTR-026`, `FTR-022`, `FTR-031`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Each domain requires separate product, architecture, dependency, privacy/compliance and human decisions.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Domain complexity leaks into core.
- Sensitive medical data sent to wrong provider.
- Generic agent claims domain authority.
- Design module hardcodes one tool/framework.
- Module changes core safety.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Disable module, revert to generic safe path, preserve user data, escalate to domain human and record incident.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Domain expert review.
- Provider/privacy/compliance decision records.
- Domain and core negative tests.
- Module enable/disable/fallback tests.

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

- `AC-001` — Domain rules do not leak into core.
- `AC-002` — Sensitive data never reaches unapproved provider.
- `AC-003` — Human/domain expert checkpoints are explicit.
- `AC-004` — Module can be disabled without corrupting project.
- `AC-005` — Generic mode remains available.
- `AC-006` — Outputs state limitations.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Medical module sends PHI to wrong provider.
- `NEG-002` — Agent gives definitive diagnosis/authorization.
- `NEG-003` — Design module hardcodes Figma as Source of Truth.
- `NEG-004` — Domain module weakens status/authority semantics.
- `NEG-005` — Disabled module leaves active hooks.
- `NEG-006` — Domain acceptance inferred from generic tests.

## 22. Minimal implementation model — `PROPOSAL`

Deferred separate decisions. Begin with one bounded module and static artifact/validator contracts; avoid broad domain framework.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: select one domain and document contract.
- M1: read-only/advisory artifact generation.
- M2: specialized validation and controlled tool integration.
- M3: additional domains only through separate decisions.

**Disposition rule:** Каждый domain/module требует отдельных product, architecture, dependency, privacy/compliance и human decisions.

## 24. Related micro-features

- `IDEA-066` — Domain Modules
- `IDEA-067` — Medical Domain Module
- `IDEA-068` — Design Module

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Which domain is first and why?
- What privacy/compliance regime applies?
- Which providers/tools are acceptable?
- Who is the designated domain human reviewer?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-027`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `03 — AOS Future and Legacy Reference.txt`
- `04 — AOS Model Routing and Task Decomposition Research.txt`
- `08 - Architecture Lifecycle Integration Plan.txt`

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

- [`IDEA-066` — Domain Modules](../functions/IDEA-066_domain-modules.md)
- [`IDEA-067` — Medical Domain Module](../functions/IDEA-067_medical-domain-module.md)
- [`IDEA-068` — Design Module](../functions/IDEA-068_design-module.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_027`
