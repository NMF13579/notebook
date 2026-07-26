---
package: AOS_Project_Knowledge_Baseline
package_revision: R4-RU
updated: '2026-07-26'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
implementation_authorization: NONE
git_authorization: NONE
semantic_audit: COMPLETED_WITH_CORRECTIONS
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: dev
audited_source_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
audited_source_blob_sha: a54de39bdd76994c0d3641a3008b688a1509984f
active_path: AOS-3/04_Lessons.md
document_language: ru
technical_identifiers_language: en
document_role: AUTHORITATIVE_LESSONS_AND_FAILURE_INVENTORY
authority_scope:
- historical_failures
- lesson_inventory
- regression_catalog
item_policy_effect: REQUIRES_ITEM_SCOPED_HUMAN_DECISION
lesson_observation_default_class: SYNTHESIZED
---

# 04 — Уроки и каталог ошибок

## 1. Назначение и правила статуса

Документ объединяет historical failures, root-cause candidates, preventive recommendations и regression checks.

```text
OBSERVED_FAILURE → LESSON_PROPOSAL → HUMAN_ACCEPTED_RULE
```

Каталог принят как knowledge inventory. Историческое наблюдение или lesson proposal не становится обязательной policy автоматически: policy effect требует item-scoped human decision. Отдельные lessons не объявляются принятыми rules по умолчанию.

**Классы наблюдений (observations):**
- Классы `OBSERVED_AT_SNAPSHOT` и `REPORTED` допустимы только при наличии конкретного source locator.
- При отсутствии точного source locator применяется общий класс `SYNTHESIZED`.

## 2. Каталог


## Синтез документации


### LES-001 — Полная экстракция дала низкую практическую ценность

- **Наблюдение:** Полное извлечение создавало много артефактов, но мало помогало следующему design decision.
- **Предлагаемое правило:** Исследовать только selected feature gap с stop conditions.
- **Проверка:** Каждый inspected path отвечает на named question.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-002 — Избыточное количество документов создало навигационный долг

- **Наблюдение:** Большое число files/indexes/manifests создало duplicate owners и stale links.
- **Предлагаемое правило:** Сохранять семь top-level documents; operational artifacts — по необходимости.
- **Проверка:** One fact class — one owner.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-003 — Карточки фич были слишком поверхностными

- **Наблюдение:** Короткие карточки не содержали actors, states, failures, recovery и tests.
- **Предлагаемое правило:** Использовать full Feature Passport до planning.
- **Проверка:** Не повышать feature без I/O, flow, boundaries, acceptance и negatives.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Продукт и Governance


### LES-004 — Governance появился раньше доказанной продуктовой ценности

- **Наблюдение:** Control Plane, registries и gates росли раньше Product Runtime.
- **Предлагаемое правило:** Сначала visible vertical slice, затем controls по incidents/metrics.
- **Проверка:** Control feature ссылается на real risk и measurable benefit.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-005 — Незрелый контроль валидировал сам себя

- **Наблюдение:** Незрелые control artifacts подтверждали собственный процесс.
- **Предлагаемое правило:** Immutable validation subject и independent witness when material.
- **Проверка:** Detect self-reference и write-after-freeze.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-006 — Планирование приобрело церемонию уровня execution

- **Наблюдение:** Routine work повторно входила в planning chains.
- **Предлагаемое правило:** Не перепланировать complete Task Brief без material change.
- **Проверка:** Planning gate называет exact missing field/decision.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-007 — Артефакты готовности стали блокерами

- **Наблюдение:** Readiness packages заменяли исправление продукта.
- **Предлагаемое правило:** Каждый artifact поддерживает capability/decision/check.
- **Проверка:** Orphan artifact review.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Полномочия и статусы


### LES-008 — Технический результат приняли за human acceptance

- **Наблюдение:** PASS/Evidence/CI/readiness смешивались с approval.
- **Предлагаемое правило:** Separate technical result and human decision records.
- **Проверка:** Generated ACCEPT не открывает execution/Git.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-009 — Решение человека было симулировано

- **Наблюдение:** Decision-like fields не имели human provenance.
- **Предлагаемое правило:** Decision требует actor, subject, date и explicit human action.
- **Проверка:** Execution agent cannot manufacture authority.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-010 — NOT_RUN превращался в PASS

- **Наблюдение:** Недоступные checks исчезали из aggregate success.
- **Предлагаемое правило:** Required NOT_RUN prevents PASS.
- **Проверка:** Mixed required/optional aggregation.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-011 — Unknown скрывался или блокировал всё

- **Наблюдение:** Unknown либо скрывался, либо блокировал всё.
- **Предлагаемое правило:** Указывать affected claims/actions и блокировать только необходимое.
- **Проверка:** Informational unknown допускает read-only; safety unknown blocks mutation.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-012 — Авторизация была открыта по умолчанию

- **Наблюдение:** Templates могли иметь authorized:true.
- **Предлагаемое правило:** Authority-bearing defaults false.
- **Проверка:** Copied/stale/reused auth rejected.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Контракты и runtime


### LES-013 — Schema существовала, но runtime обходил её

- **Наблюдение:** Docs/tests и runtime использовали разные validation paths.
- **Предлагаемое правило:** One strict contract implementation.
- **Проверка:** Bypass path и schema/runtime drift fixtures.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-014 — Невалидные и пустые состояния проходили проверку

- **Наблюдение:** Empty mapping, bogus status, free-form enum проходили.
- **Предлагаемое правило:** Closed vocabulary, required fields, explicit empty state.
- **Проверка:** Null/empty/unknown/extra/bool-as-int tests.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-015 — Повреждённая idle-задача обходила validation

- **Наблюдение:** Повреждённый task мог считаться idle.
- **Предлагаемое правило:** Explicit validated idle representation.
- **Проверка:** Truncated active task rejected.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-016 — Ошибка CLI выглядела как успех

- **Наблюдение:** Invalid input мог вернуть exit 0.
- **Предлагаемое правило:** Stable terminal result and exit semantics.
- **Проверка:** Args/contract/environment/internal errors.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Scope, репозиторий и окружение


### LES-017 — Scope существовал только в тексте

- **Наблюдение:** Allowed paths не ограничивали mutation.
- **Предлагаемое правило:** Normalized allowlist + diff reconciliation.
- **Проверка:** Traversal/symlink/nested repo/case tests.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-018 — Dirty worktree загрязнял candidate

- **Наблюдение:** Unrelated files попадали в diff/staging.
- **Предлагаемое правило:** Isolated subject; classify existing state; no add -A.
- **Проверка:** User files untouched.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-019 — Шум окружения создавал ложные blockers

- **Наблюдение:** .venv/generated noise блокировали задачи.
- **Предлагаемое правило:** Различать environment noise, user state, task state и material unknown.
- **Проверка:** Blocker names exact affected action.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-020 — Read-only команда изменяла репозиторий

- **Наблюдение:** Status/validation helper писал в source tree.
- **Предлагаемое правило:** Zero writes for read-only/help.
- **Проверка:** Before/after tree/status exact.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-021 — Raw remote data утекали

- **Наблюдение:** Raw remote URL мог раскрыть credentials.
- **Предлагаемое правило:** Redacting wrapper.
- **Проверка:** Token/userinfo/query/fragment absent.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-022 — Локальные ссылки ломали переносимость

- **Наблюдение:** Absolute file:///Users links ломали переносимость.
- **Предлагаемое правило:** Repository-relative links.
- **Проверка:** Package works in new location.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Идентичность, mutation и recovery


### LES-023 — Mutation была неатомарной и невосстановимой

- **Наблюдение:** Partial write оставлял unknown state.
- **Предлагаемое правило:** Atomic publication или durable journal.
- **Проверка:** Interruption at each boundary.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-024 — Candidate изменялся после freeze

- **Наблюдение:** Evidence создавалась для moving subject.
- **Предлагаемое правило:** Finalize, freeze, verify, then validate.
- **Проверка:** Any byte change invalidates result.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-025 — Использовался устаревший baseline

- **Наблюдение:** Validation использовала устаревший baseline.
- **Предлагаемое правило:** Bind exact baseline/candidate.
- **Проверка:** HEAD/worktree move invalidates.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-026 — Ownership installer был неясен

- **Наблюдение:** Managed/user/project state могли перезаписываться вместе.
- **Предлагаемое правило:** Classify paths; preview; preserve state.
- **Проверка:** Conflict/interruption/repeat/uninstall tests.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Drift и контекст


### LES-027 — Current status дублировался и расходился

- **Наблюдение:** README и HANDOFF расходились.
- **Предлагаемое правило:** One current-state owner; generated summaries.
- **Проверка:** Freshness and conflict detection.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-028 — Карта репозитория и context index устаревали

- **Наблюдение:** Derived maps имели старые commits/coverage.
- **Предлагаемое правило:** Commit/hash binding, coverage, rebuildability.
- **Проверка:** Stale index rejected.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-029 — Правила дублировались между adapters

- **Наблюдение:** Rules копировались в README/llms/agent files.
- **Предлагаемое правило:** One authority owner; thin generated adapters.
- **Проверка:** Duplicate authority wording report.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-030 — Перегрузка контекстом снижала корректность

- **Наблюдение:** Large startup context увеличивал conflicts.
- **Предлагаемое правило:** Minimal bootstrap and task-scoped Context Pack.
- **Проверка:** Measure size/missed rules/rework.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-031 — Validation entrypoints конфликтовали

- **Наблюдение:** Документы называли разные official commands.
- **Предлагаемое правило:** One official entrypoint.
- **Проверка:** Docs/CLI/CI consistency.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Граница Product / implementation


### LES-032 — Граница Product Runtime и Factory размывалась

- **Наблюдение:** Internal conveyor выдавался за product progress.
- **Предлагаемое правило:** Runtime solves identified user job.
- **Проверка:** Outcome visible without internals.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-033 — Skeleton или документация выглядели реализованным продуктом

- **Наблюдение:** Files/schemas/CI воспринимались как working product.
- **Предлагаемое правило:** Use maturity vocabulary.
- **Проверка:** Runtime claim requires executable Evidence.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-034 — First-contact UX был фрагментирован

- **Наблюдение:** Install/first-start/doctor/status жили отдельно.
- **Предлагаемое правило:** One authoritative first-start path.
- **Проверка:** Nonprogrammer completes journey.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-035 — Контрольные фичи не были объединены в единый journey

- **Наблюдение:** Intake/validate/review/lessons были разрознены.
- **Предлагаемое правило:** Dogfood one end-to-end task.
- **Проверка:** Journey covers intake→review→lesson.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-036 — Git closure не был понятен пользователю

- **Наблюдение:** Local/remote/review/decision boundaries разрознены.
- **Предлагаемое правило:** Compact status + one next action.
- **Проверка:** Stale remote invalidates recommendation.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


## Автоматизация и будущие системы


### LES-037 — Automation появилась раньше manual proof

- **Наблюдение:** Automation проектировалась до stable manual cycles.
- **Предлагаемое правило:** Automate measured repetition only.
- **Проверка:** Frequency/failures/fallback/removal documented.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-038 — Неограниченный retry создавал риск self-heal

- **Наблюдение:** Retry скрывал failure и расширял scope.
- **Предлагаемое правило:** Bound attempts and explicit escalation.
- **Проверка:** Repeated failure cannot expand scope.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-039 — UI создавал видимость authority

- **Наблюдение:** Visual click выглядел как approval.
- **Предлагаемое правило:** UI records explicit decision contract.
- **Проверка:** Button without human record fails.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-040 — Model routing основывался на предположениях, а не измерениях

- **Наблюдение:** Models выбирались интуитивно.
- **Предлагаемое правило:** Advisory routing first; measure before runtime router.
- **Проверка:** Fallback visible, no permission escalation.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-041 — Multi-agent orchestration был преждевременным

- **Наблюдение:** Roles added without measured deficit.
- **Предлагаемое правило:** Single-agent explicit stages first.
- **Проверка:** No authority from model consensus.
- **Статус:** `LESSON_PROPOSAL` до explicit human acceptance.


### LES-042 — AI-written code накапливал maintenance debt

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
