---
document_id: AOS-FEATURE-FTR-024
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-024
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
layer: "Later lifecycle"
disposition: DEFERRED_UNTIL_RELEASE_TARGET
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-061
  - IDEA-062
human_review_required: true
---

# FTR-024 — Release Checklist, Promotion Package, Version/Changelog/Tag and Rollback Assistant

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-024` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича готовит release/promotion package для реального distribution target и требует отдельную human authorization на каждый publish/deploy/tag action.

**Source-derived desired outcome:** Decision-ready promotion package binding accepted candidate, version/change summary, required checks, compatibility, deployment/rollback plan and separate release authorization.

## 3. Для кого и какую работу выполняет

**Target users:** Release owner, maintainer, product owner and reviewer.

Основные jobs-to-be-done:

- Понять, что именно и куда выпускается.
- Сформировать точные version/changelog/compatibility notes.
- Проверить release-specific Evidence и rollback readiness.
- Не спутать merge или acceptance с release.
- Наблюдать результат и безопасно инициировать rollback.

## 4. Проблема и ожидаемая ценность

### Проблема

Technical acceptance can be mistaken for release readiness. Versioning, changes, deployment target and rollback are undefined until a real distribution target exists.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Release target and source artifact binding.
- Release checklist and promotion package.
- Version/changelog/tag proposal.
- Compatibility/migration and rollback plan.
- Post-release verification.

### Out of scope / non-goals

- Automatic deployment.
- Cloud/platform selection.
- Release without real target.
- Release approval by agent/CI.
- Automatic destructive rollback.

## 6. Trigger и preconditions

### Triggers

- Accepted/merged product candidate has a distribution target.
- Version/tag/package publication is proposed.
- Promotion between environments is required.
- Release failure may require rollback.

### Preconditions

- Exact accepted source artifact.
- Release target/environment and version policy.
- Required validation/security/dependency checks declared.
- Migration and rollback mechanism understood/tested.
- Network/secrets permissions.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `accepted_merged_artifact`
- `release_target`
- `version_policy`
- `change_summary`
- `compatibility_and_migration_notes`
- `validation_security_dependency_evidence`
- `rollback_plan`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- Release checklist
- Promotion package
- Version/changelog candidate
- Tag/package identity
- Rollback plan

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Confirm real release target.
2. Bind accepted merged artifact.
3. Generate version/change/compatibility package.
4. Run required release checks.
5. Human authorizes one promotion/release action.
6. Execute through delivery tooling.
7. Verify and report; rollback separately if needed.

### Иллюстративный сценарий

1. Возникает trigger: Accepted/merged product candidate has a distribution target.
2. Система принимает входы `accepted_merged_artifact, release_target, version_policy` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: Release checklist, Promotion package, Version/changelog candidate.
5. При failure `Release inferred from acceptance/merge.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
NOT_RELEASE_CANDIDATE → CANDIDATE → CHECKS_READY → HUMAN_RELEASE_DECISION → RELEASED | REJECTED | FAILED_PARTIAL → ROLLBACK_DECISION_REQUIRED → ROLLED_BACK
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Package begins with artifact, target, version and user-visible changes.
- Breaking changes and NOT_RUN checks are prominent.
- Release button/command shows exact external side effects.
- Rollback conditions and data implications are visible.
- Post-release status is distinct from release authorization.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Release source must match accepted merged artifact.
- `FR-002` — Version/changelog cannot overclaim unaccepted features.
- `FR-003` — Required checks/NOT_RUN explicit.
- `FR-004` — Release authorization exact to target/action/version.
- `FR-005` — Publish/deploy/tag operations separated where material.
- `FR-006` — Post-release verification required.
- `FR-007` — Rollback separately authorized if effects are material/unknown.

## 13. Capabilities из source synthesis

- Release target/environment identification.
- Checklist derived from accepted contracts.
- Version/SemVer candidate and changelog generation.
- Tag/package identity and provenance.
- Compatibility/migration/deprecation notes.
- Rollback plan and verification criteria.
- Promotion across environments only through explicit decisions.
- Post-release verification and incident link.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `ReleaseCandidate`: source_artifact, version, target, changes, compatibility, migration, checks.
- `CTR-002` — `PromotionPackage`: checklist, evidence, rollout_steps, observability, rollback, permissions.
- `CTR-003` — `ReleaseAuthorization`: exact action, target, version, artifact, expiry, human identity.
- `CTR-004` — `ReleaseResult`: published_ids, target_state, verification, partial_effects, rollback_required.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-012`, `FTR-015`, `FTR-023`, `FTR-025`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Deferred until real target. Release authorization is separate from acceptance, merge and CI.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Release inferred from acceptance/merge.
- Wrong artifact/version promoted.
- Rollback untested.
- Changelog omits breaking change.
- Automatic deployment introduced without decision.
- Metrics treated as release approval.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Stop promotion, verify target and artifact, invoke separately authorized rollback, record incident/lesson and create correction task.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Artifact/version/tag/package identity.
- Release checks and security/dependency results.
- Rollback rehearsal or justification.
- Post-release observations.

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

- `AC-001` — Release package binds exact artifact and target.
- `AC-002` — User-visible changes are accurate.
- `AC-003` — Required NOT_RUN is visible.
- `AC-004` — Rollback path is tested/understood.
- `AC-005` — Release does not follow merge automatically.
- `AC-006` — Post-release verification reports honest state.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Tag points to stale commit.
- `NEG-002` — CI PASS alone releases.
- `NEG-003` — Unknown target/credentials used.
- `NEG-004` — Changelog includes deferred feature.
- `NEG-005` — Rollback untested but hidden.
- `NEG-006` — Release authorization reused for another environment.

## 22. Minimal implementation model — `PROPOSAL`

Deferred until a real distribution target. First version should be document/CLI assistant over Git/package metadata and a single accepted release adapter.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: define distribution target and manual checklist.
- M1: release package compiler.
- M2: one publish/tag/deploy adapter with verification.
- M3: environment promotion only after repeated need.

**Disposition rule:** Не внедрять до назначения real distribution/deployment target.

## 24. Related micro-features

- `IDEA-061` — Release Checklist and Promotion Package
- `IDEA-062` — Version, Changelog, Tag and Rollback Assistant

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- What is the first AOS distribution/deployment target?
- What versioning policy applies?
- Which security/dependency checks are mandatory?
- What rollback semantics are feasible?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-024`.

Supporting sources:

- `00 — AOS Reconstruction Project Control and Source Precedence.txt`
- `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`
- `02 — AOS Minimal Safety and Authority Rules.txt`
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

- [`IDEA-061` — Release Checklist and Promotion Package](../functions/IDEA-061_release-checklist-and-promotion-package.md)
- [`IDEA-062` — Version, Changelog, Tag and Rollback Assistant](../functions/IDEA-062_version-changelog-tag-and-rollback-assistant.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_024`
