---
document_id: AOS-FEATURE-FTR-010
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-010
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
layer: "Development Factory"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-020
  - IDEA-021
  - IDEA-074
human_review_required: true
---

# FTR-010 — Scoped Controlled Execution, Guarded Workflow and Safe Runner Kernels

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-010` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича выполняет одну явно разрешённую bounded mutation в одном stage, фиксирует фактические изменения и всегда останавливается с Stage Report.

**Source-derived desired outcome:** Single-writer, one-run-one-stage execution of one authorized bounded mutation, surrounded by checks and ending with a short Stage Report and stop.

## 3. Для кого и какую работу выполняет

**Target users:** Authorized execution agent, maintainer and validator observing the result.

Основные jobs-to-be-done:

- Выполнить Task Brief без расширения scope.
- Не смешать EXECUTE с VALIDATE/REVIEW/Git.
- Остановиться после finding/failure/completion.
- Зафиксировать actual changes и partial effects.
- Предотвратить parallel writers и hidden retries.

## 4. Проблема и ожидаемая ценность

### Проблема

An agent can expand scope, combine stages, retry automatically, write through hidden helpers or continue after a finding. Documentation alone does not physically constrain writes.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Single-writer execution session.
- One run — one stage.
- Allowed operations through narrow runner kernels.
- Actual change manifest and targeted inline checks.
- Terminal Stage Report and stop.

### Out of scope / non-goals

- Autonomous retry/correction/next stage.
- Human approval, validation or review.
- Commit/Push/Merge/Release.
- Unbounded shell/agent autonomy.
- Runtime enforcement platform in baseline.

## 6. Trigger и preconditions

### Triggers

- Complete Task Brief has explicit execution authorization.
- Correction Task Brief separately authorized.
- Bounded scaffold/document/code mutation requested.

### Preconditions

- Preflight READY and preview unchanged.
- Assigned Risk Profile and exact authorization exist.
- Allowed/forbidden paths and commands known.
- Recovery/stop conditions defined.
- No competing writer.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `authorized_TaskBrief`
- `ExecutionPreview`
- `authorization_record`
- `repository_baseline`
- `runner_kernel`
- `stop_conditions`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Changed artifact(s)
- Actual change manifest
- Execution log/result envelope
- Targeted check results
- Stage Report

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Revalidate authorization and identity.
2. Enter EXECUTE stage.
3. Perform one bounded mutation.
4. Run declared targeted checks.
5. Reconcile immediate scope/result.
6. Write Stage Report.
7. Stop and await separate VALIDATE or correction decision.

### Иллюстративный сценарий

1. Возникает trigger: Complete Task Brief has explicit execution authorization.
2. Система принимает входы `authorized_TaskBrief, ExecutionPreview, authorization_record` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Changed artifact(s), Actual change manifest, Execution log/result envelope.
5. При failure `Hidden scope expansion.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
AUTHORIZED → SESSION_BOUND → MUTATING → INLINE_CHECKS → COMPLETE_REPORT | FAILED_REPORT | BLOCKED_REPORT → STOPPED
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Перед mutation показывается preview identity and authorization scope.
- Progress reports only material milestones, not misleading percent completion.
- Any finding produces immediate stop reason and partial-state summary.
- Final report states changed paths, checks, NOT_RUN, limitations and one next action.
- No automatic prompt for next stage.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Executor may mutate only declared subject and paths.
- `FR-002` — One writer lock/session binding prevents concurrent writes.
- `FR-003` — Every operation logged with outcome and affected path/subject.
- `FR-004` — Unexpected effect or scope drift triggers stop.
- `FR-005` — Retries require explicit idempotent policy or new task; no blind automatic retry.
- `FR-006` — Inline checks may diagnose known cause but cannot become independent VALIDATE.
- `FR-007` — Terminal report is emitted on every exit path.

## 13. Capabilities из source synthesis

- Execute only an exact authorized Task Brief and current preflight.
- Single-writer discipline; parallel writes forbidden.
- Guard phases: `precheck`, `scopecheck`, `sessioncheck`, `resultcheck`, `postcheck`.
- Safe runner kernels for file/command operations with explicit allowlists.
- Record actual changed files, commands, outputs and limitations.
- Run only declared targeted checks inside EXECUTE.
- Stop on completion, finding, failure, unknown or authority boundary.
- No automatic correction, retry, VALIDATE or REVIEW.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `ExecutionSession`: session_id, task_id, subject, baseline, preview_id, authorization_id, writer_identity.
- `CTR-002` — `OperationResult`: operation_id, planned, actual, status, affected_subject, side_effects, error.
- `CTR-003` — `ChangeManifest`: created, modified, deleted, unchanged, unexpected.
- `CTR-004` — `StageReport`: terminal_status, findings, partial_effects, checks, not_run, next_required_action.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-006`, `FTR-009`, `FTR-019`, `FTR-013`, `FTR-014`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Only explicit human execution authorization permits mutation. Commit/push/merge/release remain separate.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Hidden scope expansion.
- Automatic retry or next-stage transition.
- Architecture/dependency change during execution.
- Parallel writers or unrecorded side effects.
- Guard validates its own unsafe assumptions.
- Generated report changes frozen candidate.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Stop immediately, preserve state, classify partial effects and hand off to FTR-014. Correction is a new authorized EXECUTE; validation never patches the artifact.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Session/authorization binding.
- Operation log and actual change manifest.
- Working tree/diff before and after.
- Single-writer and stop-condition checks.

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

- `AC-001` — Only in-scope paths change.
- `AC-002` — No next stage starts automatically.
- `AC-003` — Every failure emits machine/human terminal result.
- `AC-004` — Parallel write attempt is blocked.
- `AC-005` — Unexpected diff stops execution.
- `AC-006` — Actual changes can be independently validated later.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Helper writes outside allowed path.
- `NEG-002` — Executor starts VALIDATE after completion.
- `NEG-003` — Failure is retried automatically with widened scope.
- `NEG-004` — Authorization for different task/baseline accepted.
- `NEG-005` — Lost terminal response does not cause duplicate mutation.
- `NEG-006` — Stage Report claims PASS for NOT_RUN checks.

## 22. Minimal implementation model — `PROPOSAL`

Initially use narrow task-specific runners or direct bounded tools with wrapper logging, not a generalized autonomous executor. Physical enforcement belongs to FTR-020 later.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: documented manual execution protocol.
- M1: execution session/result wrapper.
- M2: safe runner kernels for repeated operations.
- M3: optional runtime enforcement after manual flow proves stable.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-020` — Scoped Execution
- `IDEA-021` — Controlled Execution Guard
- `IDEA-074` — Safe Runner Kernels

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Какие first runner kernels реально нужны?
- Как реализовать single-writer lock across tools?
- Какая operation journal granularity нужна для recovery?
- Когда manual executor достаточен без FTR-020?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-010`.

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

- [`IDEA-020` — Scoped Execution](../functions/IDEA-020_scoped-execution.md)
- [`IDEA-021` — Controlled Execution Guard](../functions/IDEA-021_controlled-execution-guard.md)
- [`IDEA-074` — Safe Runner Kernels](../functions/IDEA-074_safe-runner-kernels.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_010`
