---
document_id: AOS-FEATURE-FTR-008
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-008
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
  - IDEA-047
  - IDEA-048
  - IDEA-049
  - IDEA-082
  - IDEA-083
  - IDEA-084
  - IDEA-085
human_review_required: true
---

# FTR-008 — Chat-First Interaction Surface, Simple Control Surface, Status/Next/Details and Beginner Tutor

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-008` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича даёт пользователю единый chat-first интерфейс: подтверждённый status, один следующий шаг, details по запросу, понятные cards и безопасное восстановление сессии.

**Source-derived desired outcome:** Chat-first control surface that explains verified state in plain language, shows one next action, offers details/cards, supports resume and forwards only explicitly selected operations to proper layers.

## 3. Для кого и какую работу выполняет

**Target users:** Non-programmer/vibe-coder, product owner, maintainer and any agent resuming a session.

Основные jobs-to-be-done:

- Понять, где находится проект и что уже сделано.
- Увидеть blocker/unknown/NOT_RUN без чтения внутренних logs.
- Получить один следующий безопасный шаг.
- Принять human decision через понятную форму, не давая скрытых полномочий.
- Переключать Beginner/Standard/Expert detail level.

## 4. Проблема и ожидаемая ценность

### Проблема

Пользователь не понимает текущую стадию, blocker, Evidence, authority boundary или следующий безопасный шаг и вынужден знать внутренние scripts/statuses.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Status/Next/Details interaction model.
- Artifact, Decision, Blocker and Evidence cards.
- Beginner Tutor and stable commands.
- Repository-verified session resume.
- Adapters to chat, CLI/TUI/web without duplicating facts.

### Out of scope / non-goals

- Собственная authoritative state database.
- Execution logic внутри UI/chat layer.
- Автоматическое approval/routing/merge.
- Сокрытие limitations ради простоты.
- Full SaaS collaboration platform.

## 6. Trigger и preconditions

### Triggers

- Пользователь открывает AOS или спрашивает «на чём остановились?»
- Stage завершён, blocked или ждёт human decision.
- Пользователь просит details/evidence.
- Нужно выбрать разрешённую operation.

### Preconditions

- Status owners and source priority defined.
- Repository/session state can be verified or clearly marked unavailable.
- Interaction layer read-only by default.
- Mutations delegated to owner feature after fresh authorization check.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `project_memory`
- `repository_preflight`
- `current_task_and_stage`
- `validation_and_review_results`
- `open_decisions`
- `user_detail_mode`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Status summary
- One next action
- Details/source pointers
- Decision/blocker cards
- Resume summary
- Stable JSON/CLI/chat response

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Read project/session facts from owned sources.
2. Resolve staleness/conflicts or choose safe fallback.
3. Render concise state and limitations.
4. Select one deterministic next action.
5. Human asks details or invokes a separate operation.
6. Operation layer rechecks all preconditions.
7. Show result/new state and stop.

### Иллюстративный сценарий

1. Возникает trigger: Пользователь открывает AOS или спрашивает «на чём остановились?»
2. Система принимает входы `project_memory, repository_preflight, current_task_and_stage` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Status summary, One next action, Details/source pointers.
5. При failure `Dashboard/chat cache diverges from repository.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
OPENED → STATE_LOADING → VERIFIED_SUMMARY | STATE_CONFLICT | NO_ACTIVE_TASK → USER_SELECTS_DETAILS_OR_ACTION → DELEGATED | HUMAN_DECISION_REQUIRED | STOP
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Первый экран/ответ содержит: current state, why, one next action.
- Beginner mode объясняет terms; Expert mode показывает IDs/paths/commands.
- Cards всегда содержат source/subject/status и authority effect.
- Unknown/NOT_RUN/BLOCKED отображаются явно, а не как нейтральный текст.
- Action confirmation показывает exact preview и delegating feature.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — UI/chat state derived from owned sources and refreshable.
- `FR-002` — One next action must be valid under current authority/state.
- `FR-003` — Details cannot change the underlying status.
- `FR-004` — Decision card records human input separately from recommendation.
- `FR-005` — Resume verifies repository delta before repeating prior context.
- `FR-006` — Stable machine response schema supports adapters.
- `FR-007` — Interface cannot bypass permission/preflight layers.

## 13. Capabilities из source synthesis

- Interaction modes `BEGINNER`, `STANDARD`, `EXPERT` without changing safety semantics.
- Commands/surfaces such as `/help`, `/status`, `/next`, `/details`, `/resume`, `/analyze`, `/plan`, `/validate`, `/execute`.
- One-next-action policy with explicit reason and preconditions.
- Artifact, decision, blocker, Evidence and stage-result cards.
- Question «На чём мы остановились?» reconstructed from current facts, not chat memory alone.
- First Safe Commands and beginner explanations.
- Separate technical status, lifecycle state, human decision and Git state.
- Stable machine-readable response envelope and human-readable rendering.
- Read-only by default; mutation requires a separate operation and authorization.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `InteractionSnapshot`: project, subject, stage, technical_status, human_state, blockers, not_run, next_action, source_refs.
- `CTR-002` — `Card`: card_type, title, summary, status, subject, evidence_refs, allowed_responses, authority_effect.
- `CTR-003` — `UserSelection`: selected_action_or_decision, exact_subject, timestamp, identity_assurance.
- `CTR-004` — `InteractionMode`: BEGINNER | STANDARD | EXPERT; presentation only.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-011`, `FTR-012`, `FTR-014`, `FTR-015`, `FTR-016`, `FTR-021`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Interface is a non-authority adapter. It cannot approve, assign Risk Profile, grant execution/Git/release or override safety.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Dashboard/chat cache diverges from repository.
- `/next` auto-executes.
- PASS shown as accepted or released.
- Too many statuses without explanation.
- Beginner mode hides material risk.
- Commands promise unavailable capability.
- Chat history becomes Source of Truth.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Show `STALE`/`CONFLICTING_SOURCE`, refresh from repository, keep historical status labeled, and require explicit operation retry. Never fix underlying artifact from the display layer.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Source pointers used for current summary.
- Repository/session delta on resume.
- Action delegation and reauthorization result.
- Usability/dogfood observations.

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

- `AC-001` — Non-programmer correctly identifies current state and next action.
- `AC-002` — Status matches repository/contracts and is not inferred from chat alone.
- `AC-003` — NOT_RUN and unknowns remain visible in Beginner mode.
- `AC-004` — Decision/review recommendation are distinct.
- `AC-005` — Resuming after changed HEAD detects staleness.
- `AC-006` — UI cannot execute without owner-layer authorization.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Cached status cannot override repository conflict.
- `NEG-002` — Button labelled Accept cannot create decision without identity/subject binding.
- `NEG-003` — Chat summary cannot claim PASS from partial checks.
- `NEG-004` — Beginner mode cannot omit material blocker.
- `NEG-005` — Details view cannot mutate artifact.
- `NEG-006` — Lost response does not repeat Git/execution action blindly.

## 22. Minimal implementation model — `PROPOSAL`

Start with deterministic status assembler and Markdown/JSON response, then chat adapter. CLI/TUI/web are projections over the same contracts. Avoid separate UI database.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: `/status`, `/next`, `/details`, `/resume` contract.
- M1: chat-first cards and Beginner/Expert modes.
- M2: operation delegation with preflight.
- M3: optional Workbench UI after artifact contracts stabilize.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-047` — Beginner Tutor
- `IDEA-048` — Simple Control Surface
- `IDEA-049` — Status / Next / Details, Stable CLI Output and First Safe Commands
- `IDEA-082` — AOS Chat Interaction Surface
- `IDEA-083` — Beginner / Standard / Expert Interaction Modes
- `IDEA-084` — Artifact, Decision, Blocker and Evidence Cards
- `IDEA-085` — Repository-Verified Session Resume: «На чём мы остановились?»

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Какой initial interface выбран: chat/CLI/TUI/web/hybrid?
- Какие commands/statuses должны быть stable baseline?
- Как подтверждать human identity in chat?
- Где проходит boundary между Interaction Surface и Project Memory?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-008`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
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

- [`IDEA-047` — Beginner Tutor](../functions/IDEA-047_beginner-tutor.md)
- [`IDEA-048` — Simple Control Surface](../functions/IDEA-048_simple-control-surface.md)
- [`IDEA-049` — Status / Next / Details, Stable CLI Output and First Safe Commands](../functions/IDEA-049_status-next-details-stable-cli-output-and-first-safe-commands.md)
- [`IDEA-082` — AOS Chat Interaction Surface](../functions/IDEA-082_aos-chat-interaction-surface.md)
- [`IDEA-083` — Beginner / Standard / Expert Interaction Modes](../functions/IDEA-083_beginner-standard-expert-interaction-modes.md)
- [`IDEA-084` — Artifact, Decision, Blocker and Evidence Cards](../functions/IDEA-084_artifact-decision-blocker-and-evidence-cards.md)
- [`IDEA-085` — Repository-Verified Session Resume: «На чём мы остановились?»](../functions/IDEA-085_repository-verified-session-resume.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_008`
