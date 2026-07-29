---
document_id: AOS-FEATURE-FTR-013
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-013
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
layer: "Development Factory / Validation boundary"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-029
  - IDEA-030
  - IDEA-031
human_review_required: true
---

# FTR-013 — Diff/Scope Reconciliation, Disposable Validation Subject and Immutable Candidate Freeze

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-013` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича связывает Evidence с неизменным candidate: сверяет planned и actual scope, создаёт reproducible validation subject и обнаруживает write-after-freeze.

**Source-derived desired outcome:** Complete planned-vs-actual scope reconciliation, reproducible candidate identity and isolated read-only validation subject with mutation/provenance detection.

## 3. Для кого и какую работу выполняет

**Target users:** Executor, validator, reviewer and Git/release authorizer.

Основные jobs-to-be-done:

- Убедиться, что проверяется именно созданный candidate.
- Не потерять untracked/generated files из фактического diff.
- Отделить executor worktree от validator subject.
- Получить stable identity до REVIEW/Git.
- Обнаружить self-reference и provisional package identity.

## 4. Проблема и ожидаемая ценность

### Проблема

Validation may run against a moving worktree, omit untracked files, import a different package or bind evidence to a provisional/self-referential identity.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Planned-vs-actual scope reconciliation.
- Candidate freeze and content identity.
- Disposable/read-only validation subject.
- Provenance/import/environment checks.
- Mutation and staleness detection.

### Out of scope / non-goals

- Fixing scope drift.
- Human acceptance or Git delivery.
- Universal build artifact system.
- Self-referential identity schemes.
- Validation inside mutable executor context by default.

## 6. Trigger и preconditions

### Triggers

- EXECUTE completes and candidate is ready for VALIDATE.
- Review/Git operation requires exact subject.
- Generated package has manifest/hash identity.
- Prior validation may have run on wrong checkout/import.

### Preconditions

- Task Brief planned scope known.
- Executor reports actual operations.
- Candidate can be materialized or snapshot.
- Temporary subject location is isolated and disposable.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `planned_scope`
- `actual_worktree_state`
- `operation_log`
- `candidate_artifacts`
- `identity_policy`
- `validation_profile`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Scope reconciliation report
- Frozen candidate identity
- Disposable subject
- Provenance report
- Drift detection result

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Stop mutation.
2. Capture and classify actual diff.
3. Resolve/report deviations.
4. Finalize content and compute identity.
5. Create disposable subject.
6. Verify provenance and freeze point.
7. Validate/read-only review.
8. Invalidate on any drift.

### Иллюстративный сценарий

1. Возникает trigger: EXECUTE completes and candidate is ready for VALIDATE.
2. Система принимает входы `planned_scope, actual_worktree_state, operation_log` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Scope reconciliation report, Frozen candidate identity, Disposable subject.
5. При failure `Untracked in-scope file omitted.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
UNRECONCILED → SCOPE_RECONCILED | DRIFT_FOUND → FREEZING → FROZEN → VALIDATION_SUBJECT_READY → VALIDATED | MUTATION_DETECTED | INVALID_IDENTITY
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Report shows planned vs actual paths and unexplained changes.
- Frozen identity is displayed in review/Git cards.
- Validator indicates source path, import provenance and environment.
- Any post-freeze mutation prominently invalidates results.
- Temporary subject cleanup occurs only after evidence is retained.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Include tracked, untracked, generated and deleted artifacts.
- `FR-002` — No unexplained actual change may be silently excluded.
- `FR-003` — Candidate identity must be non-self-referential and reproducible.
- `FR-004` — Validation subject must be read-only or mutation-detecting.
- `FR-005` — Validator must not import from unintended checkout.
- `FR-006` — Freeze occurs after execution and before independent validation.
- `FR-007` — Changed candidate requires new validation/review.

## 13. Capabilities из source synthesis

- Capture tracked and relevant untracked changes.
- Classify each path as task, unrelated, generated, temporary or unknown.
- Compare Task Brief, preview and actual diff.
- Compute stable candidate identity without self-reference.
- Materialize disposable external worktree/directory/package.
- Verify import/runtime provenance.
- Detect write-after-freeze and validator side effects.
- Bind reports to baseline and candidate.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `ScopeReconciliation`: planned_paths, actual_paths, unexplained, excluded_noise, disposition.
- `CTR-002` — `CandidateIdentity`: candidate_id, content_digest, constituent_files, baseline, created_at, identity_policy.
- `CTR-003` — `ValidationSubject`: source_candidate, materialization_path, readonly_controls, environment_identity.
- `CTR-004` — `FreezeAudit`: pre_digest, post_digest, mutation_events, status.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-006`, `FTR-009`, `FTR-010`, `FTR-011`, `FTR-012`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Freeze proves identity, not correctness or approval. Temporary subjects are not canonical state.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Untracked in-scope file omitted.
- Candidate identity includes its own hash/report.
- Validation imports live checkout.
- Validator modifies candidate.
- Stale baseline or provisional tree used.
- Out-of-scope change accepted as incidental.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Any deviation or drift returns to a separately authorized correction EXECUTE, followed by new freeze and separate VALIDATE. Never patch disposable subject.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Git/filesystem inventory including untracked.
- Candidate manifest and digest reproduction.
- Disposable subject creation log.
- Pre/post validation digest and import provenance.

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

- `AC-001` — Another validator can reconstruct the same subject.
- `AC-002` — Untracked files are included or explicitly excluded with reason.
- `AC-003` — Write-after-freeze is detected.
- `AC-004` — Self-referential manifest is rejected.
- `AC-005` — Evidence references frozen identity.
- `AC-006` — Wrong import/source path fails validation.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Validation on moving worktree.
- `NEG-002` — Manifest omits file used by runtime.
- `NEG-003` — Digest includes its own final digest field ambiguously.
- `NEG-004` — Validator mutates candidate.
- `NEG-005` — Nested/symlink content escapes subject.
- `NEG-006` — Review proceeds after candidate changed.

## 22. Minimal implementation model — `PROPOSAL`

Use filesystem/Git snapshot or archive plus strict manifest and digest policy. Disposable copy/worktree/temporary package can be selected per accepted architecture; keep mechanism replaceable.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: planned-vs-actual diff checklist.
- M1: candidate manifest/digest.
- M2: disposable subject and mutation detection.
- M3: integration with review/Git/release.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-029` — Diff and Scope Reconciliation
- `IDEA-030` — Disposable Validation Subject
- `IDEA-031` — Candidate Freeze and Identity

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Which snapshot mechanism suits the future implementation repository?
- Exact package identity and self-reference policy?
- How to handle large/binary generated artifacts?
- When is a Git tree sufficient versus explicit package manifest?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-013`.

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

- [`IDEA-029` — Diff and Scope Reconciliation](../functions/IDEA-029_diff-and-scope-reconciliation.md)
- [`IDEA-030` — Disposable Validation Subject](../functions/IDEA-030_disposable-validation-subject.md)
- [`IDEA-031` — Candidate Freeze and Identity](../functions/IDEA-031_candidate-freeze-and-identity.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_013`
