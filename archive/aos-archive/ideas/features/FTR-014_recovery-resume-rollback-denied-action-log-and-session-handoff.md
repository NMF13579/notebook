---
document_id: AOS-FEATURE-FTR-014
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-014
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
layer: "Product Runtime / Development Factory boundary"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-032
  - IDEA-034
  - IDEA-036
  - IDEA-085
human_review_required: true
---

# FTR-014 — Recovery, Resume, Rollback and Denied Action Log

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-014` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича после interruption, failure или denied action восстанавливает фактическое состояние, показывает partial effects и предлагает один безопасный recovery step.

**Source-derived desired outcome:** Read-only recovery assessment with current facts, partial effects, candidate identity, findings, denied-action reason, safe options and exactly one next required action.

## 3. Для кого и какую работу выполняет

**Target users:** User, executor, support agent and reviewer after interruption, failure or blocked action.

Основные jobs-to-be-done:

- Понять, что успело измениться до сбоя.
- Не повторить необратимую operation вслепую.
- Продолжить session с проверенного состояния.
- Выбрать resume, correction, rollback или restart.
- Сохранить denied-action reason и открытые blockers.

## 4. Проблема и ожидаемая ценность

### Проблема

Interrupted work causes recursive recovery plans, uncertain partial state, destructive cleanup or blind retries. Users cannot see what was denied and what remains safe.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Read-only recovery assessment.
- Resume Package and session reconstruction.
- Denied Action Log.
- Rollback proposal and separately authorized execution.
- Known-state restart guidance.

### Out of scope / non-goals

- Automatic destructive rollback.
- Recursive recovery planning loop.
- Blind retry or continuation after unknown partial effects.
- Changing artifact during VALIDATE/REVIEW.
- Consuming future authorization.

## 6. Trigger и preconditions

### Triggers

- Execution interruption or tool timeout.
- Partial install/write/Git/network result.
- Denied operation or permission boundary.
- User asks to resume after session gap.
- Candidate/repository state changed unexpectedly.

### Preconditions

- Available logs, manifests and repository state are readable.
- Recovery assessment itself is read-only.
- Known safe baselines/candidates are identifiable or UNKNOWN.
- Destructive rollback requires separate authorization.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `last_TaskBrief`
- `operation_log`
- `partial_change_manifest`
- `current_repository_state`
- `candidate_identity`
- `denied_action_records`
- `prior_handoff`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Recovery assessment
- Resume Package
- Denied Action Log
- Rollback proposal
- One next action

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Stop all mutation.
2. Inspect current state and logs.
3. Classify partial effects and certainty.
4. Build recovery/resume view.
5. Human chooses one bounded route.
6. Create new Task Brief/authorization if mutation is needed.
7. Execute/validate in separate stages.

### Иллюстративный сценарий

1. Возникает trigger: Execution interruption or tool timeout.
2. Система принимает входы `last_TaskBrief, operation_log, partial_change_manifest` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Recovery assessment, Resume Package, Denied Action Log.
5. При failure `Automatic retry duplicates writes/remote actions.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
INTERRUPTED_OR_BLOCKED → ASSESSING → STATE_KNOWN | STATE_PARTIAL | STATE_UNKNOWN → RESUME_OPTION | CORRECTION_TASK | ROLLBACK_DECISION | RESTART_FROM_BASELINE | HUMAN_REVIEW_REQUIRED
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Recovery view begins with facts: last confirmed stage, current HEAD/diff, partial effects.
- Options show risk and required authorization.
- Exactly one recommended next action is highlighted.
- Denied action explains which boundary blocked it.
- Resume summary distinguishes repository facts from chat memory.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Never assume operation succeeded because response was lost.
- `FR-002` — Re-inspect external/local state before retry.
- `FR-003` — Partial effects must be enumerated or UNKNOWN.
- `FR-004` — Resume cannot reuse stale authorization automatically.
- `FR-005` — Rollback plan states data-loss/irreversibility risk.
- `FR-006` — Recovery output does not mutate subject.
- `FR-007` — New correction requires separate Task Brief/EXECUTE.

## 13. Capabilities из source synthesis

- Recover repository/task/session facts without mutation.
- Detect completed, partial, failed, stale and unknown states.
- Record denied action, missing condition, affected scope and no-mutation claim.
- Generate Resume Package with non-grants and stale detection.
- Offer separate options: continue with new authorization, correct, rollback, restart or defer.
- Rollback only from an explicit reversible plan and scoped human authorization.
- Detect lost-response cases before repeating remote actions.
- Prevent recovery-of-recovery loops.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `RecoveryAssessment`: incident, last_known_state, current_state, partial_effects, unknowns, safe_options, recommended_next_action.
- `CTR-002` — `DeniedActionRecord`: requested_action, classification, reason_code, missing_permission_or_decision, subject.
- `CTR-003` — `ResumePackage`: repository_identity, active_task, completed_stage, candidate, findings, open_decisions, delta.
- `CTR-004` — `RollbackProposal`: target_state, operations, risks, prerequisites, validation_plan, authorization_required.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-008`, `FTR-010`, `FTR-013`, `FTR-015`, `FTR-016`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Recovery view and rollback proposal do not authorize mutation. Destructive rollback requires explicit scoped human decision.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Automatic retry duplicates writes/remote actions.
- Destructive cleanup removes evidence or user work.
- Old authorization carried into new session.
- Recovery plan becomes new unbounded project.
- Stale handoff executed blindly.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Prefer restart-from-known-state over complex repair when cheaper and safer; preserve provenance and unrelated work; escalate unresolved state as `UNKNOWN_BLOCKED`.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Fresh repository/remote state.
- Operation log and before/after manifests.
- Candidate/freeze identity.
- Prior response/authorization consumption state where available.

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

- `AC-001` — User sees exact partial state and unknowns.
- `AC-002` — Lost response does not trigger duplicate operation.
- `AC-003` — Safe resume detects changed HEAD/worktree.
- `AC-004` — Rollback is not executed without separate authorization.
- `AC-005` — Denied action reason is actionable.
- `AC-006` — Recovery ends with one next action and stop.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Automatic cleanup deletes ambiguous files.
- `NEG-002` — Old authorization reused after material change.
- `NEG-003` — Recovery report marks unknown operation complete.
- `NEG-004` — Nested recovery task starts itself.
- `NEG-005` — Rollback plan ignores data migration/remote side effects.
- `NEG-006` — Chat summary overrides repository facts.

## 22. Minimal implementation model — `PROPOSAL`

Start with read-only state reconstructor using Task/Stage Reports, Git status/diff, manifests and denied-action records. Rollback remains proposal until specific reversible operations are proven.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: recovery checklist + Resume Package.
- M1: denied-action and partial-effect records.
- M2: safe retry/idempotency adapters.
- M3: bounded rollback helpers for proven cases.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-032` — Recovery, Resume and Rollback
- `IDEA-034` — Denied Action Log and State Recovery View
- `IDEA-036` — Session Handoff
- `IDEA-085` — Repository-Verified Session Resume: «На чём мы остановились?»

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Which operations require journaling in baseline?
- How to detect authorization consumption after lost response?
- What is the canonical Project Memory owner?
- Which rollback operations are sufficiently deterministic?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-014`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
- `05 - AOS-FARM — справочные идеи из harness engineering.txt`
- `06 - AOS-FARM — Third Pass Temporary Implementation Plan.txt`
- `07 - AOS-FARM — Proposed Pipeline Evolution.txt`

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

- [`IDEA-032` — Recovery, Resume and Rollback](../functions/IDEA-032_recovery-resume-and-rollback.md)
- [`IDEA-034` — Denied Action Log and State Recovery View](../functions/IDEA-034_denied-action-log-and-state-recovery-view.md)
- [`IDEA-036` — Session Handoff](../functions/IDEA-036_session-handoff.md)
- [`IDEA-085` — Repository-Verified Session Resume: «На чём мы остановились?»](../functions/IDEA-085_repository-verified-session-resume.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_014`
