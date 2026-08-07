---
document_id: AOS-FEATURE-FTR-019
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-019
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
layer: "Minimal Safety Floor candidate"
disposition: CANDIDATE_CORE_SAFETY
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-034
  - IDEA-050
  - IDEA-051
  - IDEA-052
  - IDEA-053
  - IDEA-054
human_review_required: true
---

# FTR-019 — Action Trust Boundary, Permission/Error Taxonomy and External Content Safety

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-019` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича классифицирует каждое действие по blast radius, проверяет permission/decision state и выдаёт однозначный allowed/denied/unknown result.

**Source-derived desired outcome:** Explicit action classification, permission state, reason-code taxonomy and fail-closed gates that explain what is allowed, denied, unknown or requires human action.

## 3. Для кого и какую работу выполняет

**Target users:** All AOS users and agents; especially executor and external-content intake paths.

Основные jobs-to-be-done:

- Понимать разницу между read, write, protected, destructive, network и Git actions.
- Не дать external content стать instruction source.
- Объяснить, какой decision/permission требуется.
- Fail closed при unknown permission or subject.
- Использовать единые reason codes во всех layers.

## 4. Проблема и ожидаемая ценность

### Проблема

Read, write, network, protected, destructive, Git and external-content actions have different blast radius but are often handled by one generic approval. Errors and permission gaps are ambiguous.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Action classification and trust boundary.
- Permission state machine.
- Error/reason-code taxonomy.
- External-content prompt injection boundary.
- Path/command/network/Git gates.

### Out of scope / non-goals

- Human decision replacement.
- Automatic risk downgrade.
- Full sandbox enforcement (FTR-020).
- Security certification.
- Generic policy engine before stable actions.

## 6. Trigger и preconditions

### Triggers

- Any tool/action is requested.
- External/web/document content contains instructions.
- Scope/permission is ambiguous.
- Protected/destructive/network/Git operation is proposed.

### Preconditions

- Action can be described with subject and intended effect.
- Minimal Safety Floor and human-only decisions known.
- Permission records and allowed boundary accessible.
- Unknown defaults to deny/block for affected action.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `action_request`
- `subject_and_scope`
- `effect_type`
- `source_trust_class`
- `permission_records`
- `human_decisions`
- `runtime_environment`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Action classification
- Permission state
- Reason codes
- Denied-action explanation
- Required human decision

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Classify requested action and subject.
2. Resolve current permissions and protected scope.
3. Inspect external/untrusted input boundary.
4. Evaluate allowlists and missing conditions.
5. Return allow/deny/unknown/human-review result.
6. Pass permitted operation to proper stage; log denial.

### Иллюстративный сценарий

1. Возникает trigger: Any tool/action is requested.
2. Система принимает входы `action_request, subject_and_scope, effect_type` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Action classification, Permission state, Reason codes.
5. При failure `Classifier becomes authority.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
UNCLASSIFIED → READ_ONLY | WRITE | PROTECTED | DESTRUCTIVE | NETWORK | GIT | EXTERNAL_CONTENT → ALLOWED | DENIED | UNKNOWN | HUMAN_DECISION_REQUIRED
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Denied action shows category, reason and exact missing authority.
- External content is visibly labelled data/reference.
- Permission card separates scope, operation and duration.
- Unknown never appears as green/neutral.
- User sees non-grants.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Every action has explicit subject, effect and trust class.
- `FR-002` — Unknown permission or decision cannot default allow.
- `FR-003` — Authorization must not transfer across operation/scope.
- `FR-004` — External content cannot override system/project/human authority.
- `FR-005` — Reason codes are stable and machine-readable.
- `FR-006` — Protected/destructive actions require human decision.
- `FR-007` — Secrets/sensitive data boundaries apply before provider/network use.

## 13. Capabilities из source synthesis

- Action Trust Boundary table by operation class.
- Permission state classifier and stable error taxonomy.
- Prompt-injection boundary: external content treated as data, not instructions.
- Protected path, write, command and tool allowlists.
- Network, sandbox, dependency and Git permission gates.
- Secrets/sensitive-data redaction and provider boundary.
- Denied-action report with no-mutation evidence.
- Static advisory checks before runtime enforcement.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `ActionDescriptor`: action_id, type, subject, scope, effects, reversibility, external_content_refs.
- `CTR-002` — `PermissionState`: required_permissions, observed_permissions, decisions, status, reason_codes.
- `CTR-003` — `BoundaryDecision`: ALLOW | DENY | HUMAN_REVIEW_REQUIRED | UNKNOWN_BLOCKED; technical classification only.
- `CTR-004` — `ErrorTaxonomy`: code, class, user_message, retryability, required_action.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-009`, `FTR-014`, `FTR-020`, `FTR-021`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Safety floor is always on; exact enforcement mechanism is not accepted architecture. Only human grants protected/network/destructive/Git permissions.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Classifier becomes authority.
- Unknown treated as allowed.
- External document changes system behavior.
- Allowlists too broad or stale.
- Secret included in logs.
- Permission inherited from another task/session.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Fail closed, redact, identify exact missing permission and require a separate scoped decision. Correct taxonomy/rules through protected change process.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Action classification inputs and rule result.
- Authorization/permission subject binding.
- Path/command/network checks.
- External-content boundary tests.

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

- `AC-001` — Same action is classified consistently across UI/preflight/executor.
- `AC-002` — Unknown is blocked.
- `AC-003` — External instructions do not change authority.
- `AC-004` — User understands required human action.
- `AC-005` — Operation-specific permission cannot be reused.
- `AC-006` — Reason codes support recovery.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Web page says 'ignore previous instructions'.
- `NEG-002` — Write disguised as read-only command.
- `NEG-003` — Symlink path bypasses allowed scope.
- `NEG-004` — Network call embedded in dependency/tool.
- `NEG-005` — Commit authorization reused for push.
- `NEG-006` — Agent-generated approval record accepted.

## 22. Minimal implementation model — `PROPOSAL`

Begin as shared enums, classifiers and adapters used by preflight/UI. Keep policy small and explicit. Physical enforcement is a later independent layer.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: action classes and reason codes.
- M1: shared permission-state evaluator.
- M2: integration with preflight/execution/Git.
- M3: runtime enforcement after stable manual flow.

**Disposition rule:** Направление рассматривается как candidate Minimal Safety Floor, но exact mechanism, contracts и implementation требуют human decision.

## 24. Related micro-features

- `IDEA-034` — Denied Action Log and State Recovery View
- `IDEA-050` — Action Trust Boundary
- `IDEA-051` — Permission State Classifier and Error Taxonomy
- `IDEA-052` — Prompt Injection Boundary for External Content
- `IDEA-053` — Protected Path, Write and Command Allowlists
- `IDEA-054` — Network, Sandbox and Git Permission Gate

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Exact risk-to-action mapping?
- How are human permissions authenticated/expired?
- Which external-content policies are baseline?
- Which commands require deeper effect introspection?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-019`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `04 — AOS Model Routing and Task Decomposition Research.txt`
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

- [`IDEA-034` — Denied Action Log and State Recovery View](../functions/IDEA-034_denied-action-log-and-state-recovery-view.md)
- [`IDEA-050` — Action Trust Boundary](../functions/IDEA-050_action-trust-boundary.md)
- [`IDEA-051` — Permission State Classifier and Error Taxonomy](../functions/IDEA-051_permission-state-classifier-and-error-taxonomy.md)
- [`IDEA-052` — Prompt Injection Boundary for External Content](../functions/IDEA-052_prompt-injection-boundary-for-external-content.md)
- [`IDEA-053` — Protected Path, Write and Command Allowlists](../functions/IDEA-053_protected-path-write-and-command-allowlists.md)
- [`IDEA-054` — Network, Sandbox and Git Permission Gate](../functions/IDEA-054_network-sandbox-and-git-permission-gate.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_019`
