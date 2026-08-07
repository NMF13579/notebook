---
document_id: AOS-FEATURE-FTR-020
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-020
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
layer: "Runtime Enforcement / Governance"
disposition: DEFERRED_AFTER_MANUAL_FLOW
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-021
  - IDEA-053
  - IDEA-054
  - IDEA-055
  - IDEA-056
  - IDEA-057
  - IDEA-058
human_review_required: true
---

# FTR-020 — Runtime Enforcement, Isolated Execution and Progressive Governance Modes

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-020` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича физически ограничивает execution через sandbox/policy только после того, как manual contracts и real risks доказали необходимость.

**Source-derived desired outcome:** Optional enforcement layer, introduced only after stable manual contracts, that blocks forbidden actions and scales governance by risk without disabling the Minimal Safety Floor.

## 3. Для кого и какую работу выполняет

**Target users:** Maintainers and teams that have proven need for stronger physical controls.

Основные jobs-to-be-done:

- Блокировать forbidden writes/commands/network physically.
- Изолировать risky execution.
- Применять stronger controls proportional to accepted risk.
- Не превращать safety в premature Control Plane.
- Собирать denial evidence and escape detection.

## 4. Проблема и ожидаемая ценность

### Проблема

Documentation and advisory checks cannot physically prevent forbidden writes/commands, but building a Control Plane too early reproduces legacy complexity and false assurance.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Optional enforcement runtime.
- Isolated execution environment.
- Policy adapter over accepted action/scope contracts.
- Progressive governance modes.
- Runtime decision/denial logs.

### Out of scope / non-goals

- Baseline Product Runtime requirement.
- Automatic Risk Profile assignment.
- Self-governing Control Plane.
- Universal container/orchestrator platform.
- Governance mode that disables Minimal Safety Floor.

## 6. Trigger и preconditions

### Triggers

- Manual workflow repeatedly violates/risks boundaries.
- Threat/risk analysis justifies physical enforcement.
- Stable action/scope/permission contracts exist.
- Human accepts enforcement architecture/dependencies.

### Preconditions

- FTR-019 classifications stable.
- Manual path works and is tested.
- Threat model and failure modes documented.
- Recovery/break-glass and observability defined.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `accepted_policy`
- `authorized_TaskBrief_and_preview`
- `action_descriptors`
- `sandbox_configuration`
- `risk_profile`
- `allowed_resources`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Enforcement policy/config
- Runtime decision log
- Sandbox result
- Denied-action evidence
- Mode/status

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Confirm stable manual workflow and observed incident.
2. Human accepts enforcement scope/architecture.
3. Configure minimal policy.
4. Run isolated dry-run/advisory mode.
5. Enable bounded enforcement.
6. Monitor false blocks/escapes.
7. Review and evolve policy separately.

### Иллюстративный сценарий

1. Возникает trigger: Manual workflow repeatedly violates/risks boundaries.
2. Система принимает входы `accepted_policy, authorized_TaskBrief_and_preview, action_descriptors` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Enforcement policy/config, Runtime decision log, Sandbox result.
5. При failure `Control Plane before product value.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
DISABLED → OBSERVE_ONLY → ENFORCED_LOW_RISK | ENFORCED_HIGH_RISK → VIOLATION_BLOCKED | SANDBOX_FAILED | BREAK_GLASS_HUMAN_DECISION
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Mode and enforced boundaries always visible.
- Denied action includes policy/rule and safe alternative.
- Observe-only warnings cannot be mistaken for enforcement.
- Break-glass is explicit, scoped and human-only.
- Sandbox failure stops work rather than silently degrading.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Policy derived from accepted Task/Action contracts, not hidden defaults.
- `FR-002` — Observe-only and enforced modes have distinct statuses.
- `FR-003` — Enforcement failure must fail closed for protected actions.
- `FR-004` — No extension can weaken Minimal Safety Floor.
- `FR-005` — Isolation must prevent path/network/process escape within declared threat model.
- `FR-006` — Every denial/override logged.
- `FR-007` — Mode changes require human decision.

## 13. Capabilities из source synthesis

- Runtime guards around file writes, commands, network, protected paths and Git.
- Isolated execution environment/sandbox.
- Capability/token-scoped permissions.
- Progressive modes such as `MINIMAL`, `STANDARD`, `STRICT` while protected operations stay strict.
- Advanced gates only for observed high-risk cases.
- Audit of enforcement decisions and side effects.
- Fail-safe disable/remove path.
- Separation between policy definition, enforcement and human decisions.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `EnforcementPolicy`: version, allowed_actions, paths, commands, network, resources, mode, owner.
- `CTR-002` — `RuntimeDecision`: action, policy_version, decision, reason, evidence, override_ref.
- `CTR-003` — `SandboxResult`: environment, controls, resource_usage, violations, terminal_status.
- `CTR-004` — `GovernanceModeDecision`: mode, scope, rationale, effective_at, human_decision_id.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-019`, `FTR-021`, `FTR-026`, `FTR-023`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Deferred; architecture, dependencies and governance contract require human decisions. Agent cannot downgrade protection.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Control Plane before product value.
- Optional mode bypasses safety floor.
- Enforcer self-authorizes or self-validates.
- False sense of security.
- Policy drift blocks routine work.
- Enforcement failure corrupts state.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Disable/isolate faulty module, return to manual safe workflow, preserve logs and require protected human decision for policy changes.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Escape/negative fixtures.
- Observe-vs-enforce parity.
- Policy/version binding.
- Denial/break-glass audit.

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

- `AC-001` — Forbidden action is physically blocked.
- `AC-002` — Observe-only never claims enforcement.
- `AC-003` — Sandbox failure cannot silently run unisolated.
- `AC-004` — Mode cannot weaken core safety.
- `AC-005` — Policy matches exact task/subject.
- `AC-006` — Benefit justifies operational complexity.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Path/process/network escape.
- `NEG-002` — Plugin overrides policy.
- `NEG-003` — Mode downgrade without human decision.
- `NEG-004` — Unknown policy version defaults allow.
- `NEG-005` — Break-glass reused outside scope.
- `NEG-006` — Enforcement log interpreted as approval.

## 22. Minimal implementation model — `PROPOSAL`

Deferred. Candidate mechanisms may include OS sandbox/container/allowlisted runner, but architecture and dependencies require human decision. Start only after manual incidents demonstrate need.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: manual/advisory controls only.
- M1: observe-only instrumentation.
- M2: enforce one proven high-risk boundary.
- M3: progressive profiles after independent validation.

**Disposition rule:** Не внедрять до стабильного manual flow, contract maturity и evidence реальной потребности.

## 24. Related micro-features

- `IDEA-021` — Controlled Execution Guard
- `IDEA-053` — Protected Path, Write and Command Allowlists
- `IDEA-054` — Network, Sandbox and Git Permission Gate
- `IDEA-055` — Runtime Enforcement Layer
- `IDEA-056` — Isolated Execution Environment
- `IDEA-057` — Progressive Governance Modes
- `IDEA-058` — Advanced Governance Gates

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Which threat model and platforms matter?
- Which enforcement mechanism fits implementation environment?
- What governance modes are actually needed?
- How is break-glass authenticated and audited?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-020`.

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

- [`IDEA-021` — Controlled Execution Guard](../functions/IDEA-021_controlled-execution-guard.md)
- [`IDEA-053` — Protected Path, Write and Command Allowlists](../functions/IDEA-053_protected-path-write-and-command-allowlists.md)
- [`IDEA-054` — Network, Sandbox and Git Permission Gate](../functions/IDEA-054_network-sandbox-and-git-permission-gate.md)
- [`IDEA-055` — Runtime Enforcement Layer](../functions/IDEA-055_runtime-enforcement-layer.md)
- [`IDEA-056` — Isolated Execution Environment](../functions/IDEA-056_isolated-execution-environment.md)
- [`IDEA-057` — Progressive Governance Modes](../functions/IDEA-057_progressive-governance-modes.md)
- [`IDEA-058` — Advanced Governance Gates](../functions/IDEA-058_advanced-governance-gates.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_020`
