---
document_id: AOS-FEATURE-FTR-023
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-023
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
disposition: CANDIDATE_AFTER_BASELINE
source_catalog: AOS-FULL-FEATURE-CATALOG-R1
source_micro_features:
  - IDEA-060
  - IDEA-078
human_review_required: true
---

# FTR-023 — Advisory CI, CI Smoke, Safety Regression Fixtures and Quality Gates

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-023` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича запускает быстрые и целевые проверки в CI как Evidence, сохраняет `NOT_RUN` и negative fixtures и никогда не превращает CI PASS в approval.

**Source-derived desired outcome:** Staged advisory verification profile with fast smoke, targeted contract/negative tests, full suite when justified and explicit `NOT_RUN`/limitations.

## 3. Для кого и какую работу выполняет

**Target users:** Maintainers, validators, contributors and reviewers.

Основные jobs-to-be-done:

- Быстро ловить bootstrap/import/schema wiring failures.
- Запускать checks, соответствующие Task Brief.
- Не повторять ранее найденные safety regressions.
- Понимать, какой candidate/ref реально проверен.
- Сохранять local/CI parity и limitations.

## 4. Проблема и ожидаемая ценность

### Проблема

Checks are inconsistent or too slow; CI PASS can hide missing profiles and is often mistaken for approval. Control bugs recur without negative fixtures.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Fast smoke profile.
- Targeted feature/contract/negative tests.
- Optional full suite and audits.
- Exact subject/environment provenance.
- Advisory CI result through ValidationEnvelope.

### Out of scope / non-goals

- Automatic approval/merge/release.
- Perfect coverage target.
- All scanners/dependencies from day one.
- Fixing failures in CI stage.
- Branch protection decisions.

## 6. Trigger и preconditions

### Triggers

- Executable baseline exists.
- PR/branch/candidate needs repeatable checks.
- Historical failure needs regression fixture.
- Local validation profile stabilizes.

### Preconditions

- Candidate/ref exact.
- Check profile and required/optional semantics defined.
- CI permissions least privilege.
- Dependencies/actions accepted and pinned where appropriate.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `candidate_ref_or_package`
- `validation_profile`
- `test_and_fixture_sets`
- `environment_definition`
- `TaskBrief_required_checks`
- `optional_audit_configuration`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- CI/smoke results
- Fixture results
- Quality profile
- Evidence pointers
- Limitations

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Select profile and candidate.
2. Run fast smoke.
3. Run targeted safety/feature tests.
4. Run full suite/optional audits when required.
5. Aggregate through ValidationEnvelope.
6. Publish Evidence with `NOT_RUN`.
7. Human/reviewer uses result separately.

### Иллюстративный сценарий

1. Возникает trigger: Executable baseline exists.
2. Система принимает входы `candidate_ref_or_package, validation_profile, test_and_fixture_sets` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: CI/smoke results, Fixture results, Quality profile.
5. При failure `CI validates wrong ref/package.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
QUEUED → BOOTSTRAP_SMOKE → TARGETED_TESTS → OPTIONAL_FULL_SUITE → RESULT_PUBLISHED | FAIL | BLOCKED | PARTIAL_NOT_RUN
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Summary shows exact ref/package/interpreter.
- Required and optional checks are separate.
- Historical regression fixtures show linked lesson/failure.
- Flaky/unreliable checks are labelled, not hidden.
- CI UI/report explicitly says Evidence ≠ approval.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — CI checks exact candidate, not mutable branch head ambiguity.
- `FR-002` — Required NOT_RUN prevents green.
- `FR-003` — Negative fixtures cover authority/status/scope/freeze/install/recovery failures.
- `FR-004` — CI must not mutate tracked repository state.
- `FR-005` — Secrets and permissions minimized.
- `FR-006` — Local equivalent commands documented.
- `FR-007` — Flaky check treatment requires explicit profile change.

## 13. Capabilities из source synthesis

- Fast syntax/import/manifest/contract smoke.
- Targeted tests selected from Task Brief.
- Safety and regression negative fixtures.
- Schema/runtime/module-boundary and exit-code checks.
- CI configuration least privilege and pinned dependencies/actions where chosen.
- Local/CI parity and exact subject provenance.
- Coverage/change indicators with declared limitations.
- Advisory status only; no auto-approval/merge.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `QualityProfile`: profile_id, required_checks, optional_checks, environments, time_budget, owners.
- `CTR-002` — `CIResult`: candidate, run_id, environment, ValidationEnvelope, artifacts, limitations.
- `CTR-003` — `RegressionFixture`: fixture_id, source_failure, input, expected_result, protected_invariant.
- `CTR-004` — `CheckReliabilityRecord`: flake_rate, known_causes, status, disposition.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-011`, `FTR-013`, `FTR-021`, `FTR-030`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

CI is Evidence, not approval. Branch protections/merge policy require separate human decisions.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- CI validates wrong ref/package.
- Optional check hidden.
- Flaky check becomes authority.
- PASS used as merge/release decision.
- No negative tests for prior failure.
- Pipeline complexity exceeds product value.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Mark unreliable check, rerun locally against exact candidate, fix CI separately and preserve previous result as historical.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- CI run/ref/package identity.
- Local-vs-CI conformance.
- Negative fixture results.
- No-dirty-state and least-privilege checks.

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

- `AC-001` — Fast smoke catches broken bootstrap/import/schema wiring.
- `AC-002` — Required NOT_RUN prevents PASS.
- `AC-003` — Historical P0/P1 safety failures have fixtures.
- `AC-004` — Exact subject and environment are visible.
- `AC-005` — CI leaves no unexpected repository drift.
- `AC-006` — Human sees limitations and separate approval state.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — CI validates wrong ref.
- `NEG-002` — Unknown status coerced green.
- `NEG-003` — Skipped dependency silently omitted.
- `NEG-004` — Generated human decision fixture accepted.
- `NEG-005` — Write-after-freeze not detected.
- `NEG-006` — CI success triggers merge automatically.

## 22. Minimal implementation model — `PROPOSAL`

Reuse FTR-011 profiles in local test framework and CI. Begin with a small high-risk suite; avoid broad quality platform/dependency sprawl.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: local smoke/negative tests.
- M1: advisory CI mirror.
- M2: exact candidate and Evidence artifacts.
- M3: optional full/security/dependency audits when justified.

**Disposition rule:** Реализация допустима только после существования executable baseline и стабильного validation subject.

## 24. Related micro-features

- `IDEA-060` — Advisory CI and CI Smoke
- `IDEA-078` — Schema / Runtime Drift, Module Boundaries, Negative Fixtures, Bootstrap and Quality Tooling

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Which CI provider and branch policy will target repository use?
- What checks define baseline?
- How are flaky checks governed?
- Which dependency/security audits are justified?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-023`.

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

- [`IDEA-060` — Advisory CI and CI Smoke](../functions/IDEA-060_advisory-ci-and-ci-smoke.md)
- [`IDEA-078` — Schema / Runtime Drift, Module Boundaries, Negative Fixtures, Bootstrap and Quality Tooling](../functions/IDEA-078_schema-runtime-drift-module-boundaries-negative-fixtures-bootstrap-and-quality-tooling.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_023`
