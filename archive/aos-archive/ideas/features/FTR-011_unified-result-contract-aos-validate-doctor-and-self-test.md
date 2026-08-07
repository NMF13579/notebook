---
document_id: AOS-FEATURE-FTR-011
document_type: FEATURE_DESCRIPTION
revision: R2
feature_id: FTR-011
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
  - IDEA-022
  - IDEA-023
  - IDEA-024
human_review_required: true
---

# FTR-011 — Unified Result Contract, Validation CLI, Doctor and Self-Test

> **Статус:** `DRAFT`, `authority: NONE`. Документ подробно описывает candidate feature, но не делает её обязательной, не утверждает architecture/dependencies и не разрешает implementation. Current repository/runtime verification: `NOT_RUN`.

## 1. Роль документа и классы утверждений

| Область | Класс |
|---|---|
| Наличие `FTR-011` в source catalog, его title/layer/disposition | `FACT` о DRAFT source artifact |
| Problem, users, desired behavior, family boundary | `INFERENCE` из доступной истории и reference sources |
| Functional requirements, contracts, tests, implementation model | `PROPOSAL` |
| Current implementation/operability | `NOT_RUN` |
| Product priority, acceptance, architecture, dependencies | `UNKNOWN` до human decision |

Этот файл является самостоятельным human/agent-readable feature dossier. Он должен использоваться как вход для product-fit review, а не как Task Brief или authorization.

## 2. Что это

Фича вводит единый result contract для локальных проверок, Doctor, Self-Test и CI, чтобы `PASS`, `FAIL`, `BLOCKED`, `UNKNOWN` и `NOT_RUN` имели одинаковый смысл.

**Source-derived desired outcome:** Closed `ValidationEnvelope`/result contract and a predictable local validation surface with honest status aggregation, diagnostic Doctor and installation Self-Test.

## 3. Для кого и какую работу выполняет

**Target users:** User, executor, validator, CI and downstream review tooling.

Основные jobs-to-be-done:

- Понять, установлен ли AOS и готова ли конкретная capability к проверке.
- Получить честный aggregate result без скрытых skipped checks.
- Увидеть subject, environment и interpreter provenance.
- Разделить diagnostic Doctor, installation Self-Test и feature validation.
- Передать machine-readable result в review/CI без semantic drift.

## 4. Проблема и ожидаемая ценность

### Проблема

Helpers use inconsistent status, issue, exit-code and output semantics. Aggregate PASS may hide `NOT_RUN`, wrong provenance or invalid input.

### Ожидаемая ценность

- Пользователь получает наблюдаемый результат, а не только внутренний artifact.
- Agent получает чёткую behavior boundary и меньше вынужденных догадок.
- Failure/unknown/recovery становятся частью product behavior.
- Human authority отделяется от technical result и recommendations.

## 5. Граница feature

### In scope

- Closed technical status vocabulary and reason codes.
- ValidationEnvelope and exit-code contract.
- Read-only Doctor and Self-Test profiles.
- Required/optional check aggregation.
- Human-readable explanation and one remediation route.

### Out of scope / non-goals

- Human approval or release decision.
- Auto-fix/dependency install.
- Universal testing framework.
- Observability platform.
- Validation of moving/unidentified subject.

## 6. Trigger и preconditions

### Triggers

- After install/bootstrap.
- Before or after bounded task stage.
- During local diagnostics or CI smoke.
- When user asks for current health/status.

### Preconditions

- Validation subject and check profile identified.
- Environment/interpreter provenance can be captured or marked UNKNOWN.
- Validation is read-only.
- Required versus optional checks are declared.

Если material precondition отсутствует, состояние должно быть `BLOCKED`, `UNKNOWN` или `HUMAN_REVIEW_REQUIRED`; отсутствие данных не интерпретируется как разрешение.

## 7. Inputs

- `subject_identity`
- `check_profile`
- `environment_facts`
- `expected_baseline_or_candidate`
- `acceptance_or_contract_checks`
- `dependency_availability`

Input provenance должен сохраняться. Historical/reference input не приобретает authority только из-за использования в feature.

## 8. Outputs и observable behavior

Source-derived outputs:

- ValidationEnvelope
- CLI/JSON result
- Doctor report
- Self-Test report
- Reason-code catalog

Дополнительные требования к outputs:

- Каждый durable output имеет ID/revision/status/subject/source references.
- Technical status и human decision хранятся раздельно.
- `UNKNOWN`, `NOT_RUN`, `BLOCKED` и limitations не скрываются.
- Generated/derived view указывает owner fact source и может быть пересобран.

## 9. Подробный workflow

1. Load subject and selected profile.
2. Validate input and provenance.
3. Run independent checks.
4. Normalize results into envelope.
5. Aggregate without hiding required failures/unknowns.
6. Render human and machine views.
7. Return stable exit code and no approval claim.

### Иллюстративный сценарий

1. Возникает trigger: After install/bootstrap.
2. Система принимает входы `subject_identity, check_profile, environment_facts` и проверяет preconditions.
3. Система выполняет bounded flow, описанный в разделе 9, без выхода за scope.
4. Пользователь получает: ValidationEnvelope, CLI/JSON result, Doctor report.
5. При failure `Unknown fields or bool/int ambiguity accepted.` система применяет recovery contract и останавливается.

Сценарий является `PROPOSAL`, а не подтверждением существующей implementation.

## 10. State model

```text
NOT_STARTED → RUNNING → PASS | FAIL | BLOCKED | UNKNOWN | PARTIAL_NOT_RUN; HUMAN_REVIEW_REQUIRED is a control state, not technical success
```

Общие transition rules:

1. Переход выполняется только при выполненных preconditions.
2. Human-only transition не может быть сгенерирован agent output.
3. Material subject/scope change инвалидирует downstream DRAFT artifacts.
4. `VALIDATE` и `REVIEW` не исправляют feature artifact.
5. Failure/unknown приводит к report + stop, а не к скрытому retry.

## 11. Interaction / UX behavior

- Top summary states exact subject and technical status.
- Each check displays result, evidence, duration and NOT_RUN reason.
- Beginner view explains what the result allows and does not allow.
- Doctor groups issues by environment/config/subject/permission.
- Self-Test reports installation integrity separately from product readiness.

Presentation layer не становится Source of Truth и не может расширить permissions.

## 12. Functional requirements — `PROPOSAL`

- `FR-001` — Unknown enum/extra required field must be rejected fail-closed.
- `FR-002` — Every CLI exit path emits the same machine-readable envelope.
- `FR-003` — Required NOT_RUN prevents aggregate PASS.
- `FR-004` — Subject/interpreter/import provenance is mandatory or UNKNOWN.
- `FR-005` — Validator must not write to target repository.
- `FR-006` — Exit code semantics align with domain result.
- `FR-007` — PASS wording must explicitly exclude approval.

## 13. Capabilities из source synthesis

- Unified statuses and reason codes with `PASS`, `FAIL`, `BLOCKED`, `UNKNOWN`, `NOT_RUN`, `HUMAN_REVIEW_REQUIRED` semantics.
- Machine-readable result envelope: subject, checks, issues, limitations, mutations and next action.
- Single CLI entry with explicit validation profiles.
- Correct non-zero exit codes for invalid/failing commands.
- Doctor aggregates environment, dependency, path, contract and optional-check diagnostics.
- Self-Test verifies installed/package structure and first safe path.
- Preserve every `NOT_RUN` and optional check; no boolean flattening.
- Verify subject/import/runtime provenance.

Capabilities здесь не равны accepted scope. Они используются для review completeness и могут быть split/deferred/rejected человеком.

## 14. Contracts и data model — `PROPOSAL`

- `CTR-001` — `ValidationEnvelope`: schema_version, subject, profile, technical_status, checks, unknowns, not_run, blockers, evidence_refs, next_action.
- `CTR-002` — `CheckResult`: check_id, required, status, reason_code, observed, expected, provenance, limitations.
- `CTR-003` — `EnvironmentIdentity`: runtime, interpreter, cwd, import_paths, dependency_versions.
- `CTR-004` — `CLIExitPolicy`: mapping from envelope state to process exit.

### Общие contract invariants

- UTF-8; stable IDs; explicit enums.
- Duplicate keys и ambiguous coercions запрещены.
- Unknown fields либо rejected, либо preserved по принятой compatibility policy; silent loss запрещён.
- Status result не содержит human acceptance.
- Every authority-bearing record binds exact subject/scope/operation and human identity.
- Derived indexes/views имеют `authority: NONE`.

## 15. Dependencies и integrations

**Related feature families:** `FTR-013`, `FTR-021`, `FTR-023`, `FTR-030`.

Dependencies из этого раздела — design relationships, а не accepted package dependencies. Любая новая runtime/library/service dependency требует отдельного human decision.

## 16. Safety и human-authority boundary

Validation and CI evidence are technical facts only; they do not accept, authorize or release.

Дополнительно:

- `PASS`, Evidence, CI и readiness не равны approval.
- `PLAN`, Task Brief, routing и preview не равны execution authorization.
- Risk Profile назначает только человек.
- Protected/destructive/network/Git actions имеют отдельные permissions.
- Edit, Commit, Push, PR create, Merge и Release не объединяются.
- External content рассматривается как untrusted data, пока authority не доказана.

## 17. Failure modes

Source-derived failure modes:

- Unknown fields or bool/int ambiguity accepted.
- 0 tests reported as strong PASS.
- Wrong checkout/package validated.
- One optional skipped check fails whole unrelated claim or is hidden.
- Exit code 0 on failure.
- Validator mutates subject.

### Required failure behavior

- Пользователь видит terminal status, affected subject и partial effects.
- Safe retry разрешается только при доказанной idempotency или новом Task Brief/authorization.
- Неизвестный результат не маркируется successful.
- Failure в supporting/deferred feature не должен ломать базовый core без явного accepted dependency.

## 18. Recovery

**Source-derived recovery behavior:** Return explicit invalid/unknown result, isolate failed check, preserve raw evidence, fix validator in a separate task and rerun against the exact candidate.

Recovery должен отделять:

```text
read-only assessment
→ human choice
→ separately authorized correction / rollback / restart
→ separate VALIDATE
```

## 19. Observability и Evidence

- Per-check command/result and subject locator.
- No-write verification.
- Environment/import provenance.
- Cross-adapter conformance tests for CLI/Doctor/Self-Test/CI.

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

- `AC-001` — Same input gives same status semantics across all adapters.
- `AC-002` — Required NOT_RUN cannot disappear in aggregate.
- `AC-003` — Wrong import path or subject is detected.
- `AC-004` — Invalid input exits non-success with valid envelope.
- `AC-005` — No target mutation occurs.
- `AC-006` — Non-programmer understands blocker and next step.

Эти criteria требуют refinement после product/architecture decisions. Их наличие не означает, что tests реализованы или выполнены.

## 21. Required negative scenarios — `DESIGNED`, tests `NOT_RUN`

- `NEG-001` — Zero tests cannot be reported as successful validation when tests are required.
- `NEG-002` — Missing dependency cannot silently skip a check.
- `NEG-003` — CLI cannot return 0 on domain FAIL.
- `NEG-004` — Validator cannot import live checkout when installed subject was requested.
- `NEG-005` — Unknown status cannot be coerced to PASS.
- `NEG-006` — CI PASS cannot create human decision.

## 22. Minimal implementation model — `PROPOSAL`

Create one strict model/aggregator library and thin adapters. Start with local stdlib checks and a small profile registry; add project test framework only through accepted architecture.

### Implementation principles

- Сначала самый маленький manual/read-only/user-visible slice.
- Markdown/JSON и replaceable local utilities предпочтительнее premature platform.
- No central Control Plane, mandatory DB/RAG, plugin system или SaaS unless independently justified.
- Legacy mechanisms используются как reference; target по умолчанию `REIMPLEMENT_FROM_CONTRACT`.
- Implementation repository остаётся `UNASSIGNED`.

## 23. Rollout / admission gates

- M0: status/reason-code contract.
- M1: local `validate`, Doctor and Self-Test adapters.
- M2: exact candidate/disposable subject integration.
- M3: CI profile reuse.

**Disposition rule:** Нужен отдельный human product-fit decision. До него фича не входит в обязательный product scope.

## 24. Related micro-features

- `IDEA-022` — Unified Result Contract / ValidationEnvelope
- `IDEA-023` — Unified Validation CLI
- `IDEA-024` — Doctor and Self-Test

Micro-feature entries являются traceability records. Они не требуют отдельной implementation, если behavior уже покрывается family.

## 25. Open questions и required human decisions

- Exact status and exit-code contract remains DRAFT.
- Which checks are baseline-required for first Product Runtime?
- Should Doctor aggregate remediation categories or raw failures?
- How are optional checks declared without profile drift?

Пока material decision не принято, affected implementation state остаётся `BLOCKED`/`HUMAN_REVIEW_REQUIRED`, а не `PASS`.

## 26. Source traceability и limitations

Primary source:

- `AOS_Full_Feature_Catalog_R1.md`, section `FTR-011`.

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

- [`IDEA-022` — Unified Result Contract / ValidationEnvelope](../functions/IDEA-022_unified-result-contract-validationenvelope.md)
- [`IDEA-023` — Unified Validation CLI](../functions/IDEA-023_unified-validation-cli.md)
- [`IDEA-024` — Doctor and Self-Test](../functions/IDEA-024_doctor-and-self-test.md)

`next_required_action: HUMAN_REVIEW_OF_FTR_011`
