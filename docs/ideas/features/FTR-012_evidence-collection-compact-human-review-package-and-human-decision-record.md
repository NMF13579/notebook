---
document_id: AOS-FEATURE-FTR-012
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-012
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
layer: "Product Runtime / Review boundary"
disposition: CANDIDATE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-025
  - IDEA-026
  - IDEA-027
  - IDEA-028
  - IDEA-084
  - IDEA-091
human_review_required: true
---

# FTR-012 — Evidence Collection, Compact Human Review Package, Independent Review and Human Decision Record

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-012` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича собирает exact Evidence по candidate в один короткий review package и отделяет reviewer recommendation от подлинного human decision.

**Source-derived desired outcome:** Decision-ready package binding exact candidate, Task Brief, diff, checks, findings, limitations and options, followed by a separate authentic human decision record.

## 3. Для кого и какую работу выполняет

**Target users:** Product owner, reviewer, validator, maintainer and decision maker.

Основные jobs-to-be-done:

- Понять изменение без чтения raw logs.
- Сопоставить acceptance criteria с фактическими checks.
- Увидеть findings, deviations, NOT_RUN и limitations.
- Принять ACCEPT/NEEDS_CHANGES/REJECT/DEFER по exact subject.
- Передать следующий контекст без симуляции approval.

## 4. Проблема и ожидаемая ценность

### Проблема

Raw logs are too large for human judgment, while summaries can omit negative evidence or simulate acceptance. Reviewer recommendation and human decision are often conflated.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Evidence collection/index.
- Compact Human Review Package.
- Independent read-only review.
- Semantic/wording guard against overclaim.
- Separate Human Decision Record and supersession.

### Out of scope / non-goals

- Automatic acceptance or correction.
- Execution/Git/release authorization.
- Modification of candidate during REVIEW.
- Dumping secrets/raw logs into package.
- Treating reviewer recommendation as human decision.

## 6. Trigger и preconditions

### Triggers

- EXECUTE or VALIDATE reaches terminal report.
- Candidate needs independent review.
- Human decision is required before next stage.
- Session handoff must preserve open findings.

### Preconditions

- Exact immutable candidate identity known.
- Task Brief and acceptance criteria available.
- Evidence collected with provenance and redaction.
- Reviewer independence requirements known.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `TaskBrief`
- `candidate_identity`
- `actual_diff_or_artifacts`
- `ValidationEnvelope`
- `acceptance_criteria`
- `findings_and_limitations`
- `human_decision_channel`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Evidence Report
- Human Review Package
- Review recommendation
- Human Decision Record
- Wording/semantic guard result

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Freeze/bind candidate.
2. Collect declared Evidence.
3. Run independent review.
4. Compile concise package and decision options.
5. Human reviews and records explicit decision.
6. Store recommendation and decision separately.
7. Stop; correction or Git action requires new authorization.

### Иллюстративный сценарий

1. Возникает trigger: EXECUTE or VALIDATE reaches terminal report.
2. Система принимает входы `TaskBrief, candidate_identity, actual_diff_or_artifacts` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Evidence Report, Human Review Package, Review recommendation.
5. При failure `Logs dumped without interpretation.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
EVIDENCE_COLLECTING → PACKAGE_READY → INDEPENDENT_REVIEW → HUMAN_REVIEW_REQUIRED → ACCEPTED | NEEDS_CHANGES | REJECTED | DEFERRED | INVALIDATED_SUBJECT_CHANGED
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Package begins with purpose and user-visible before/after.
- Acceptance table maps each criterion to PASS/FAIL/NOT_RUN/BLOCKED and Evidence.
- Findings and limitations appear before recommendation.
- Decision options are unselected and include authority/non-grants.
- Human can supersede a prior decision explicitly.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Package bound to exact candidate/task/baseline.
- `FR-002` — Every claim maps to Evidence or explicit NOT_RUN/UNKNOWN.
- `FR-003` — Semantic guard checks meaning, not only forbidden words.
- `FR-004` — Reviewer recommendation stored separately from decision.
- `FR-005` — Agent-generated decision must be rejected.
- `FR-006` — Subject change invalidates package/decision.
- `FR-007` — Decision cannot grant undeclared Git/execution authority.

## 13. Capabilities из source synthesis

- Collect Evidence with exact subject and temporal binding.
- Compile concise review package with claims mapped to checks or `NOT_RUN`.
- Independent read-only review that cannot alter subject.
- Separate reviewer recommendation from human decision.
- Human decision options `ACCEPT`, `NEEDS_CHANGES`, `REJECT`, `DEFER` where applicable.
- False-PASS/approval wording guard.
- Decision authenticity/provenance fields and supersession/revocation.
- Open blockers and limitations survive handoff.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `EvidenceReport`: subject, criteria_results, checks, artifacts, findings, unknowns, not_run, limitations.
- `CTR-002` — `ReviewPackage`: summary, before_after, scope, acceptance_matrix, findings, recommendation, decision_options.
- `CTR-003` — `ReviewerRecord`: reviewer_identity, independence, recommendation, rationale, conflicts.
- `CTR-004` — `HumanDecisionRecord`: decision_id, exact_subject, value, decided_by, identity_assurance, grants, non_grants, supersedes.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-011`, `FTR-013`, `FTR-016`, `FTR-021`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Evidence ≠ approval; recommendation ≠ human decision; acceptance ≠ commit/push/merge/release.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Logs dumped without interpretation.
- Generated ACCEPT treated as human decision.
- Missing evidence hidden.
- Candidate changed after review.
- Review package interpreted as execution/Git authorization.
- Identity assurance overclaimed.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Invalidate stale package, regenerate from preserved evidence, keep historical decision with explicit supersession and return `HUMAN_REVIEW_REQUIRED`; never auto-start correction.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Candidate and package digests.
- Acceptance-to-check mapping.
- Reviewer independence declaration.
- Semantic guard result and redaction report.

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

- `AC-001` — Human can decide without raw-log archaeology.
- `AC-002` — Every positive claim is evidence-backed.
- `AC-003` — NOT_RUN and negative findings remain prominent.
- `AC-004` — Generated text cannot masquerade as human acceptance.
- `AC-005` — Changing candidate invalidates prior review package.
- `AC-006` — Decision grants only explicitly stated authority.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — PASS technical result cannot preselect ACCEPT.
- `NEG-002` — Stale package is rejected.
- `NEG-003` — Same agent cannot produce and authenticate human decision.
- `NEG-004` — Missing Evidence blocks only affected claim, not hidden.
- `NEG-005` — Needs Changes does not auto-start correction.
- `NEG-006` — Secrets/tokens are redacted.

## 22. Minimal implementation model — `PROPOSAL`

Markdown/JSON package assembler, acceptance matrix, redaction and semantic guard. Human decision storage should be simple and explicit; stronger identity assurance can be layered later.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: manual one-document review template.
- M1: Evidence index and acceptance matrix compiler.
- M2: independent reviewer workflow and semantic guard.
- M3: authenticated decision integration after human decision model is accepted.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-025` — Evidence Collection
- `IDEA-026` — Compact Human Review Package
- `IDEA-027` — Independent Read-only Review
- `IDEA-028` — Human Decision Record and False-PASS Wording Guard
- `IDEA-084` — Artifact, Decision, Blocker and Evidence Cards
- `IDEA-091` — Requirement → UX → Slice → Task → Code → Test/Evidence Traceability

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- What identity assurance is sufficient for initial human decisions?
- Should review package be one file or linked bundle?
- Which reviewer independence rules are mandatory?
- How are revoked/superseded decisions displayed?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-012`.

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

- [`IDEA-025` — Evidence Collection](../functions/IDEA-025_evidence-collection.md)
- [`IDEA-026` — Compact Human Review Package](../functions/IDEA-026_compact-human-review-package.md)
- [`IDEA-027` — Independent Read-only Review](../functions/IDEA-027_independent-read-only-review.md)
- [`IDEA-028` — Human Decision Record and False-PASS Wording Guard](../functions/IDEA-028_human-decision-record-and-false-pass-wording-guard.md)
- [`IDEA-084` — Artifact, Decision, Blocker and Evidence Cards](../functions/IDEA-084_artifact-decision-blocker-and-evidence-cards.md)
- [`IDEA-091` — Requirement → UX → Slice → Task → Code → Test/Evidence Traceability](../functions/IDEA-091_requirement-to-ux-to-slice-to-task-to-code-to-test-evidence-traceability.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_012`
