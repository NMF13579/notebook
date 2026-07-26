---
package: AOS_Integrated_Knowledge_Package
package_revision: R3-RU
updated: 2026-07-26
status: APPROVED
authority: AUTHORITATIVE
human_review: REQUIRED
human_acceptance: ACCEPTED
implementation_authorization: AUTHORIZED
git_authorization: AUTHORIZED
self_audit: COMPLETED
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: dev
document_language: ru
technical_identifiers_language: en
document_role: LESSONS_AND_FAILURE_CATALOG
proposed_post_acceptance_role: ACCEPTED_LESSONS_AND_FAILURE_CATALOG
proposed_authority_scope:
  - historical_failures
  - preventive_rules
  - regression_catalog
source_files_bound_by_blob_sha: true
---
# 04 — Уроки и каталог ошибок

## 1. Назначение и правила статуса

Документ объединяет historical failures, root-cause candidates, preventive recommendations и regression checks.

```text
OBSERVED_FAILURE → LESSON_PROPOSAL → HUMAN_ACCEPTED_RULE
```

Историческое наблюдение не становится policy автоматически.

## 2. Каталог


## Documentation synthesis


### LES-001 — Exhaustive extraction produced low value

- **Наблюдение:** Полное извлечение создавало много артефактов, но мало помогало следующему design decision.
- **Предлагаемое правило:** Исследовать только selected feature gap с stop conditions.
- **Проверка:** Каждый inspected path отвечает на named question.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-002 — Too many documents created navigation debt

- **Наблюдение:** Большое число files/indexes/manifests создало duplicate owners и stale links.
- **Предлагаемое правило:** Сохранять семь top-level documents; operational artifacts — по необходимости.
- **Проверка:** One fact class — one owner.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-003 — Feature cards were too shallow

- **Наблюдение:** Короткие карточки не содержали actors, states, failures, recovery и tests.
- **Предлагаемое правило:** Использовать full Feature Passport до planning.
- **Проверка:** Не повышать feature без I/O, flow, boundaries, acceptance и negatives.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Product and Governance


### LES-004 — Governance preceded product value

- **Наблюдение:** Control Plane, registries и gates росли раньше Product Runtime.
- **Предлагаемое правило:** Сначала visible vertical slice, затем controls по incidents/metrics.
- **Проверка:** Control feature ссылается на real risk и measurable benefit.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-005 — Immature control validated itself

- **Наблюдение:** Незрелые control artifacts подтверждали собственный процесс.
- **Предлагаемое правило:** Immutable validation subject и independent witness when material.
- **Проверка:** Detect self-reference и write-after-freeze.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-006 — Planning acquired execution-grade ceremony

- **Наблюдение:** Routine work повторно входила в planning chains.
- **Предлагаемое правило:** Не перепланировать complete Task Brief без material change.
- **Проверка:** Planning gate называет exact missing field/decision.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-007 — Readiness artifacts became blockers

- **Наблюдение:** Readiness packages заменяли исправление продукта.
- **Предлагаемое правило:** Каждый artifact поддерживает capability/decision/check.
- **Проверка:** Orphan artifact review.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Authority and status


### LES-008 — Technical result was treated as human acceptance

- **Наблюдение:** PASS/Evidence/CI/readiness смешивались с approval.
- **Предлагаемое правило:** Separate technical result and human decision records.
- **Проверка:** Generated ACCEPT не открывает execution/Git.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-009 — Human decision was simulated

- **Наблюдение:** Decision-like fields не имели human provenance.
- **Предлагаемое правило:** Decision требует actor, subject, date и explicit human action.
- **Проверка:** Execution agent cannot manufacture authority.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-010 — NOT_RUN became PASS

- **Наблюдение:** Недоступные checks исчезали из aggregate success.
- **Предлагаемое правило:** Required NOT_RUN prevents PASS.
- **Проверка:** Mixed required/optional aggregation.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-011 — Unknown was hidden or blocked everything

- **Наблюдение:** Unknown либо скрывался, либо блокировал всё.
- **Предлагаемое правило:** Указывать affected claims/actions и блокировать только необходимое.
- **Проверка:** Informational unknown допускает read-only; safety unknown blocks mutation.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-012 — Authorization defaulted open

- **Наблюдение:** Templates могли иметь authorized:true.
- **Предлагаемое правило:** Authority-bearing defaults false.
- **Проверка:** Copied/stale/reused auth rejected.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Contracts and runtime


### LES-013 — Schema existed but runtime bypassed it

- **Наблюдение:** Docs/tests и runtime использовали разные validation paths.
- **Предлагаемое правило:** One strict contract implementation.
- **Проверка:** Bypass path и schema/runtime drift fixtures.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-014 — Invalid and empty states passed

- **Наблюдение:** Empty mapping, bogus status, free-form enum проходили.
- **Предлагаемое правило:** Closed vocabulary, required fields, explicit empty state.
- **Проверка:** Null/empty/unknown/extra/bool-as-int tests.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-015 — Malformed idle task bypassed validation

- **Наблюдение:** Повреждённый task мог считаться idle.
- **Предлагаемое правило:** Explicit validated idle representation.
- **Проверка:** Truncated active task rejected.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-016 — CLI failure looked successful

- **Наблюдение:** Invalid input мог вернуть exit 0.
- **Предлагаемое правило:** Stable terminal result and exit semantics.
- **Проверка:** Args/contract/environment/internal errors.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Scope, repository and environment


### LES-017 — Scope existed only in prose

- **Наблюдение:** Allowed paths не ограничивали mutation.
- **Предлагаемое правило:** Normalized allowlist + diff reconciliation.
- **Проверка:** Traversal/symlink/nested repo/case tests.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-018 — Dirty worktree contaminated candidate

- **Наблюдение:** Unrelated files попадали в diff/staging.
- **Предлагаемое правило:** Isolated subject; classify existing state; no add -A.
- **Проверка:** User files untouched.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-019 — Environment noise caused false blockers

- **Наблюдение:** .venv/generated noise блокировали задачи.
- **Предлагаемое правило:** Различать environment noise, user state, task state и material unknown.
- **Проверка:** Blocker names exact affected action.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-020 — Read-only command changed repository

- **Наблюдение:** Status/validation helper писал в source tree.
- **Предлагаемое правило:** Zero writes for read-only/help.
- **Проверка:** Before/after tree/status exact.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-021 — Raw remote data leaked

- **Наблюдение:** Raw remote URL мог раскрыть credentials.
- **Предлагаемое правило:** Redacting wrapper.
- **Проверка:** Token/userinfo/query/fragment absent.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-022 — Machine-local links broke portability

- **Наблюдение:** Absolute file:///Users links ломали переносимость.
- **Предлагаемое правило:** Repository-relative links.
- **Проверка:** Package works in new location.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Identity, mutation and recovery


### LES-023 — Mutation was non-atomic and unrecoverable

- **Наблюдение:** Partial write оставлял unknown state.
- **Предлагаемое правило:** Atomic publication или durable journal.
- **Проверка:** Interruption at each boundary.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-024 — Candidate changed after freeze

- **Наблюдение:** Evidence создавалась для moving subject.
- **Предлагаемое правило:** Finalize, freeze, verify, then validate.
- **Проверка:** Any byte change invalidates result.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-025 — Stale baseline was used

- **Наблюдение:** Validation использовала устаревший baseline.
- **Предлагаемое правило:** Bind exact baseline/candidate.
- **Проверка:** HEAD/worktree move invalidates.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-026 — Installer ownership was unclear

- **Наблюдение:** Managed/user/project state могли перезаписываться вместе.
- **Предлагаемое правило:** Classify paths; preview; preserve state.
- **Проверка:** Conflict/interruption/repeat/uninstall tests.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Drift and context


### LES-027 — Current status duplicated and drifted

- **Наблюдение:** README и HANDOFF расходились.
- **Предлагаемое правило:** One current-state owner; generated summaries.
- **Проверка:** Freshness and conflict detection.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-028 — Repository map and context index were stale

- **Наблюдение:** Derived maps имели старые commits/coverage.
- **Предлагаемое правило:** Commit/hash binding, coverage, rebuildability.
- **Проверка:** Stale index rejected.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-029 — Rules duplicated across adapters

- **Наблюдение:** Rules копировались в README/llms/agent files.
- **Предлагаемое правило:** One authority owner; thin generated adapters.
- **Проверка:** Duplicate authority wording report.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-030 — Context overload reduced correctness

- **Наблюдение:** Large startup context увеличивал conflicts.
- **Предлагаемое правило:** Minimal bootstrap and task-scoped Context Pack.
- **Проверка:** Measure size/missed rules/rework.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-031 — Validation entrypoints conflicted

- **Наблюдение:** Документы называли разные official commands.
- **Предлагаемое правило:** One official entrypoint.
- **Проверка:** Docs/CLI/CI consistency.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Product / implementation boundary


### LES-032 — Product Runtime and Factory blurred

- **Наблюдение:** Internal conveyor выдавался за product progress.
- **Предлагаемое правило:** Runtime solves identified user job.
- **Проверка:** Outcome visible without internals.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-033 — Skeleton or documentation looked implemented

- **Наблюдение:** Files/schemas/CI воспринимались как working product.
- **Предлагаемое правило:** Use maturity vocabulary.
- **Проверка:** Runtime claim requires executable Evidence.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-034 — First-contact UX fragmented

- **Наблюдение:** Install/first-start/doctor/status жили отдельно.
- **Предлагаемое правило:** One authoritative first-start path.
- **Проверка:** Nonprogrammer completes journey.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-035 — Control features were not integrated as one journey

- **Наблюдение:** Intake/validate/review/lessons были разрознены.
- **Предлагаемое правило:** Dogfood one end-to-end task.
- **Проверка:** Journey covers intake→review→lesson.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-036 — Git closure was not user-facing

- **Наблюдение:** Local/remote/review/decision boundaries разрознены.
- **Предлагаемое правило:** Compact status + one next action.
- **Проверка:** Stale remote invalidates recommendation.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Automation and future systems


### LES-037 — Automation preceded manual proof

- **Наблюдение:** Automation проектировалась до stable manual cycles.
- **Предлагаемое правило:** Automate measured repetition only.
- **Проверка:** Frequency/failures/fallback/removal documented.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-038 — Unbounded retry became self-heal risk

- **Наблюдение:** Retry скрывал failure и расширял scope.
- **Предлагаемое правило:** Bound attempts and explicit escalation.
- **Проверка:** Repeated failure cannot expand scope.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-039 — UI appeared to create authority

- **Наблюдение:** Visual click выглядел как approval.
- **Предлагаемое правило:** UI records explicit decision contract.
- **Проверка:** Button without human record fails.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-040 — Model routing was assumed rather than measured

- **Наблюдение:** Models выбирались интуитивно.
- **Предлагаемое правило:** Advisory routing first; measure before runtime router.
- **Проверка:** Fallback visible, no permission escalation.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-041 — Multi-agent orchestration was premature

- **Наблюдение:** Roles added without measured deficit.
- **Предлагаемое правило:** Single-agent explicit stages first.
- **Проверка:** No authority from model consensus.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-042 — AI-written code accumulated maintainability debt

- **Наблюдение:** Generated code терял rationale/ownership/handoff.
- **Предлагаемое правило:** Preserve rationale, ownership, invariants, tests, debt, handoff.
- **Проверка:** Docs-code consistency review.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## 3. Successful patterns to retain

Product-first sequencing; Compact Safe Path; one run/one stage; independent validation where material; exact identity binding; isolated worktree; fail-closed semantics; one next action; one-document review; targeted findings; beginner status explanation; manual dogfood; strict adapter before parser replacement; negative fixtures; rebuildable indexes; thin adapters; risk-scaled ceremony; Feature Passport before planning.

## 4. Regression catalog

```text
AUTH-001 generated decision rejected
AUTH-002 authorization defaults false
AUTH-003 stale/reused authorization rejected
STATUS-001 unknown enum rejected
STATUS-002 required NOT_RUN prevents PASS
STATUS-003 Evidence cannot unlock approval
SCOPE-001 traversal/symlink escape rejected
SCOPE-002 unrelated dirty state excluded
CLI-001 every failure has terminal result
CLI-002 help/read-only has zero writes
ENV-001 interpreter/import provenance recorded
FREEZE-001 write-after-freeze detected
FREEZE-002 self-reference rejected
INSTALL-001 dry-run side-effect free
INSTALL-002 apply bound to preview
UPDATE-001 user/project state preserved
RECOVERY-001 interruption recoverable
REVIEW-001 package shows NOT_RUN honestly
GIT-001 permissions independent
ROUTING-001 fallback visible, no escalation
CONTENT-001 external instructions untrusted
DRIFT-001 docs/schema/CLI/code/tests compared
DRIFT-002 stale index rejected
ADAPTER-001 adapters match common source
DOGFOOD-001 beginner completes first journey
LESSON-001 incident creates proposal, not rule
IDLE-001 malformed idle task rejected
PORTABLE-001 no absolute local links
```

## 5. Promotion rule

Lesson becomes normative only after source incident, bounded root cause, applicability review, preventive rule, regression/review check and explicit human acceptance.
