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
audited_source_blob_sha: b978777097f08d544b9e02f08cf5716ea199998c
active_path: docs/05_Reference.md
document_language: ru
technical_identifiers_language: en
document_role: REFERENCE_AND_PROVENANCE_REGISTRY
authority_scope:
- source_provenance
- snapshot_identity
- targeted_research_routes
reference_authority_for_target_aos: NONE
---

# 05 — Источники и provenance

## 1. Назначение

Документ является единым provenance и research-routing layer. Он не является Product Contract, Architecture Contract, implementation authorization или источником полномочий legacy.

```text
reference occurrence ≠ current implementation
historical acceptance ≠ current acceptance
source mapping ≠ target requirement
stored PASS ≠ current PASS
GitHub URL ≠ загруженный source ChatGPT Project
```

## 2. Классы источников и authority

| Класс источника | Использование | Authority |
|---|---|---|
| Current explicit human decision | Exact decision boundary | Human-scoped |
| Accepted project artifact | Declared fact class | Fact-class scoped |
| Current repository observation | Mutable snapshot facts | Observation only |
| Historical repository snapshot | Behavior, failure, prior art | `NONE` for target |
| Chat summary, note или report | Intent, lessons, candidates | `NONE` |
| Generated synthesis | Navigation и inference | `NONE` |

## 3. Текущая принятая база знаний

```yaml
repository: NMF13579/notebook
branch: dev
audited_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
active_path: docs/
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
implementation_authorization: NONE
git_authorization: NONE
```

Текущие семь документов являются активными owners своих fact classes. Состояние ветки после указанного commit должно проверяться непосредственно перед mutable repository claim.

## 4. Provenance объединённого пакета

До консолидации исходные synthesis-наборы находились в `AOS-FARM/` и `AgentOS/` внутри `notebook`. Они доступны через Git history, а не как live paths:

```yaml
historical_notebook_commit: a27a47ed0a1610115ff88f4da6a898a1aaff778b
former_source_paths:
  - AOS-FARM/00_Core.md ... AOS-FARM/06_Features.md
  - AgentOS/00_Core.md ... AgentOS/06_Features.md
live_status: REMOVED_AFTER_SYNTHESIS
```

Отсутствие этих paths в текущем tree является ожидаемым и не означает потерю provenance.

## 5. Основные reference repositories

### AOS-FARM

```yaml
url: https://github.com/NMF13579/AOS-FARM/tree/dev
repository: NMF13579/AOS-FARM
branch_label: dev
pinned_snapshot_used_by_baseline: 71b87f3dfb9fe3735c7659c123cd86db3f577201
mode: READ_ONLY_REFERENCE
authority_for_target_aos: NONE
```

Использовать для targeted research по installer/doctor, preflight, validation, candidate identity, Git boundaries, closure, recovery, negative fixtures и environment hygiene.

### AgentOS

```yaml
url: https://github.com/NMF13579/AgentOS/tree/dev
repository: NMF13579/AgentOS
branch_label: dev
pinned_snapshot_used_by_baseline: e3a60a92fbd5e78e583cddb519d39527583f3433
mode: READ_ONLY_REFERENCE
authority_for_target_aos: NONE
commands_tests_build_in_baseline_audit: NOT_RUN
```

Использовать для Problem Interview, Product Spec, Task Contract, validation, state/handoff, adapters, context-index experiments и concrete failure cases.

`dev` является плавающей веткой. Новое research должно фиксировать actual commit/tree, даже если baseline уже содержит старый pinned snapshot.

### AOS-3

AOS-3 используется как `READ_ONLY_REFERENCE` для конкретных проблем реализации. Authority для target notebook: `NONE`. Его текущая роль implementation repository относится к AOS-3 и не меняет `implementation_repository: UNASSIGNED` в notebook.

Наблюдавшийся локальный checkout: `NMF13579/AOS-3`, ветка `dev`, HEAD `d2ad68169b07a090548cbefc5add74e8dd171045`, дата чтения 2026-09-13. Источники подготовки прочитаны выборочно. Полный аудит и текущие runtime/platform tests: `NOT_RUN`.

В рабочем дереве уже имелись изменённая `development/research/as-is-project-map/AS_IS_PROJECT_MAP.md` и untracked `docs/superpowers/plans/2026-09-12-aos-core-readiness-plan-r2.md`. Они не используются как нормативные требования или подтверждение текущей готовности. Sources AOS3-S03–S05 и AOS3-S07–S09 относятся к указанному committed snapshot; mutable состояние нужно перепроверять перед новым применением.

Исследовать только конкретные gaps: first-start, применимость тестовой среды, подготовка разрешённого входа, передача между компонентами, отказ и сохранность Evidence, retry, identity и границы portability. Нумерация Features и Lessons и область принятия проверяются отдельно в каждом репозитории.

Accepted lessons AOS-3 являются источником для предложений notebook. Их authority, topology, артефакты, gates и support claims автоматически не переносятся. В частности, новые разделы о графе и переносимости в `d2ad681` описывают ограниченный эксперимент и кандидатную цель; результаты соответствующих запусков там `NOT_RUN` (`AOS3-S09`).

## 6. Secondary reference

Historical AOS-02 допускается только для конкретных gaps вокруг strict loader, CLI semantics, preview, scope, atomicity и recovery. Он не входит в default research route и не имеет target authority.

## 7. High-signal inspection order

```text
user-facing docs/commands
→ contracts/schemas
→ tests/negative fixtures
→ implementation paths
→ reports/plans/recovery artifacts
```

Historical report или README claim не считается current runtime Evidence без воспроизведения.

## 8. Targeted research record

```yaml
research_id:
feature_id:
question:
repository:
ref_or_branch:
commit_or_tree:
paths: []
methods_or_commands: []
read_only: true
findings:
  - evidence_status:
    statement:
    locator:
    temporal_scope:
useful_contracts: []
useful_negative_cases: []
rejected_legacy_complexity: []
limitations: []
remaining_unknowns: []
```

## 9. Research stop conditions

Остановить research, когда вопрос достаточно отвечен; snapshot/path недоступен; conflict меняет scope; требуется permission/network expansion; найдено protected architecture decision; исследование расширяется за selected feature; current state нельзя отделить от памяти.

Недопустимые задачи:

```text
понять весь AOS-FARM
понять весь AgentOS
извлечь всё полезное
```

## 10. Feature-to-reference routing

| Feature range | Первые reference questions |
|---|---|
| `FTR-001..006` | Intake, discovery, specification, install, ADR, Task Brief/auth |
| `FTR-007..012` | Decomposition, status UX, preflight, execution, validation, review |
| `FTR-013..018` | Freeze, recovery, Git closure, memory, search, routing |
| `FTR-019..024` | Trust, Governance, drift, patterns, CI, release |
| `FTR-025..030` | Incidents, plugins, domains, UI, packaging, internal tooling |

## 11. Promotion model

```text
reference idea
→ feature entry
→ product-fit review
→ item-scoped human disposition
→ Feature Contract
→ architecture decision when needed
→ Task Brief
→ Execution Authorization
```

## 12. Legacy locator registry

Registry позволяет разрешать legacy-упоминания из `06_Features.md` через следующие поля:

```yaml
locator_id:
repository:
snapshot_commit:
path_or_search_key:
evidence_class:
status:
```

Для ссылок, которые нельзя точно разрешить по текущим данным, используйте:

```yaml
status: UNRESOLVED
evidence_class: UNKNOWN
```

### Источники AOS-3 для уроков реализации

Пути в таблице считаются относительно корня AOS-3. Для repository-bound sources S03–S05 и S07–S09 snapshot: `d2ad68169b07a090548cbefc5add74e8dd171045`. «Класс» относится к используемому утверждению: наличие historical report на диске не повышает описанный в нём результат до свежего runtime observation.

| ID | Locator | Класс и подтверждаемый предмет | Ограничение |
|---|---|---|---|
| AOS3-S01 | External report `infrastructure-audit/REPORT.md`; полный locator ниже; «Результаты R1 и R2», «Findings и следующий шаг» | `REPORTED`: bootstrap с 21 collection error; воспроизведённый пропуск terminal preservation check | Аудит на `3b55c4397f93beeb0d279cf0201ecc232bd50166`; его неполный baseline дополнен S02 |
| AOS3-S02 | External report `infrastructure-audit/baseline-continuation/REPORT.md`; полный locator ниже; «Семь failures», «Skips» | `REPORTED`: 3805/7/6, metadata mismatch, native exclusions | Исторический прогон 2026-09-12 на `3b55c4397f93beeb0d279cf0201ecc232bd50166`, не сегодняшняя проверка |
| AOS3-S03 | [README.md](../../AOS-3/README.md), Local start; [requirements-dev.lock](../../AOS-3/requirements-dev.lock); [aos/pyproject.toml](../../AOS-3/aos/pyproject.toml), dependencies; [aos/requirements.lock](../../AOS-3/aos/requirements.lock) | `OBSERVED_AT_SNAPSHOT`: инструкция устанавливает только dev lock, runtime dependencies объявлены отдельно | Статическое чтение; fresh bootstrap в подготовке черновика `NOT_RUN` |
| AOS3-S04 | [tools/isolated_product_test.py](../../AOS-3/tools/isolated_product_test.py), `main`, ветви `result`, `install`, `import_check` | `OBSERVED_AT_SNAPSHOT`: ранние returns предшествуют финальному сравнению source snapshot | Не доказывает actual source mutation |
| AOS3-S05 | [LESSONS.md](../../AOS-3/LESSONS.md), LES-003–006, refinement LES-001, LES-012 и FTR-031 Evidence provenance | `SYNTHESIZED`: диагностические уроки; `REPORTED`: formatter/identity case | Исторические source bindings находятся внутри записей; принятие в AOS-3 не принимается за authority notebook |
| AOS3-S06 | External temporary report `aos-ftr010-brief-r20.xk45wwmw/REPORT.md`; полный locator ниже | `REPORTED`: Brief INCOMPLETE при корректной сериализации, stale subject fact, production effects не выполнялись | Временный кандидат R20; snapshot равенства с AOS-3 dev `NOT_RUN`; не доказывает цикличность всей архитектуры |
| AOS3-S07 | [tests/portability/test_ftr011_isolated.py](../../AOS-3/tests/portability/test_ftr011_isolated.py), `_run_installed_module` | `OBSERVED_AT_SNAPSHOT`: helper задаёт PYTHONPATH на copied source, сам distribution не устанавливает | Результат исторического прогона берётся из S02; название helper не доказывает installed provenance |
| AOS3-S08 | [development/evidence/FTR031-R25-OBSERVABILITY-EVIDENCE-R2/REPORT.md](../../AOS-3/development/evidence/FTR031-R25-OBSERVABILITY-EVIDENCE-R2/REPORT.md), HF-02, HF-05, HF-07 и Unknown/not-retained facts | `REPORTED`: потеря ordered reason_codes из-за порядка проверок и вывода | Основание отчёта — human attestation истории; original chat byte identity недоступна; underlying reason UNKNOWN |
| AOS3-S09 | [ARTIFACT_PROFILES.md](../../AOS-3/ARTIFACT_PROFILES.md), Cross-feature стыки; [FEATURE_DEVELOPMENT_CYCLE.md](../../AOS-3/FEATURE_DEVELOPMENT_CYCLE.md), Сопровождение проектного графа; [02_SYSTEM_ARCHITECTURE.md](../../AOS-3/docs/architecture/02_SYSTEM_ARCHITECTURE.md), §§18–19; [TEST_STRATEGY.md](../../AOS-3/docs/development/TEST_STRATEGY.md), Project graph и Минимальная проверяемая цель переносимости | `OBSERVED_AT_SNAPSHOT`: документационные дополнения уже существуют | Graph experiment и platform runs остаются `NOT_RUN`; документация не доказывает результат реализации |

Локальные relative links рассчитаны на соседний checkout `AOS-3`. Переносимость записи обеспечивают repository, exact commit, path и marker из таблицы; наличие соседнего каталога не является зависимостью runtime notebook. При недоступности источника фиксируется `BLOCKED_REFERENCE_ACCESS`, а факты не восстанавливаются по названию или памяти.

### Внешние отчёты и ограничения сохранности

Эти три источника не входят в Git snapshot AOS-3 или notebook. Пути ниже — locators наблюдавшихся файлов, а не инструкции на исполнение или копирование. Hash идентифицирует прочитанный отчёт, но не заменяет его содержимое, не доказывает правдивость и не обеспечивает доступность.

**AOS3-S01**

- Locator: `/Users/muhammed/.codex/visualizations/2026/09/12/01a093e0-c37a-7b63-9aad-5602d023e252/infrastructure-audit/REPORT.md`.
- SHA-256: `5eff19069c40da2e3c94dba6682a7318a17864da68e0a1815a6b36e337b23068`.
- Сохранённый смысл для данного урока: documented bootstrap не обеспечил runtime dependencies; проверка сохранности helper не достигалась на error returns. Причины/результаты тестов здесь сообщаются из исторического отчёта.

**AOS3-S02**

- Locator: `/Users/muhammed/.codex/visualizations/2026/09/12/01a093e0-c37a-7b63-9aad-5602d023e252/infrastructure-audit/baseline-continuation/REPORT.md`.
- SHA-256: `54052428932eeb1b0f5e86a7c150e2dac1e5fafb0bfcb2675f8cef9c36193594`.
- Сохранённый смысл: 3818 tests, 3805 passed, 7 failed, 6 skipped, exit 1; native module исключён; failures связаны с отсутствием installed metadata в source/copy environment. Отдельный последующий socket test PASS не переписывает эти counts.

**AOS3-S06**

- Locator: `/private/tmp/aos-ftr010-brief-r20.xk45wwmw/REPORT.md`.
- SHA-256: `8b72720077aa94e0b0c80a30a105fcfa1e56a5604d4afd113c1b3956e6c8bfa7`.
- Сохранённый смысл: стандартный компилятор вернул `INCOMPLETE` с единственным отсутствующим фактом `SOURCE_NOT_CURRENT:subject_state_identity`; загрузка сериализованного Brief прошла; public prepare, registration, consumption и live attempt не выполнялись.
- Источник временный и может исчезнуть. Полная история повторных попыток, identity всего candidate tree и правильность архитектурного диагноза этим отчётом не подтверждаются.

Во всех трёх случаях пересказ остаётся `REPORTED`, а не самостоятельным durable runtime Evidence. Перенос полного отчёта или минимальной проверенной выдержки в долговременное хранилище источников: `NOT_RUN`. Если решение зависит от более широкого утверждения, чем сохранённый здесь смысл, перед его принятием требуется доступный исходный отчёт или заново полученное соответствующее Evidence. Неполнота S06 ограничивает зависимые утверждения о FTR-010 и не блокирует применение других источников.

<a id="repository-graph-tz"></a>

### ТЗ проектного графа R2 и перенос в владельцев notebook

Источник: [AOS_REPOSITORY_GRAPH_TZ_R2_DRAFT_2026-09-13.md](../workspace/AOS_REPOSITORY_GRAPH_TZ_R2_DRAFT_2026-09-13.md), `document_id: AOS_REPOSITORY_GRAPH_TZ_R2`, редакция R2 от 2026-09-13. Класс — проектный синтез `SYNTHESIZED`, статус `GENERATED_DRAFT` / `PROPOSAL`. Системное ревью и инструкция пользователя на внесение документации не являются результатом pilot, выбором FTR, принятием implementation architecture или разрешением миграции AOS-3.

Черновик сохраняется как исходный материал: он содержит rationale, инженерные кандидаты и подробные fixtures. Владельцы перенесённых положений находятся в canonical docs; при дальнейшем изменении этих положений редактируется соответствующий owner, а исходный черновик не становится вторым редактируемым контрактом.

| Материал R2 | Владелец перенесённых положений |
|---|---|
| §§1–3: назначение, роли и границы | [Product: проектный граф](01_Product.md#repository-graph-purpose) |
| §§4–12: наблюдения, операции, queries, freshness, публикация и ограничения | [Architecture: контракт графа](02_Architecture.md#repository-graph-contract); конкретные storage/parser/index/lock HOW не приняты в baseline |
| §§13–16: рабочий цикл, AC/N, usefulness, срезы и поставка | [Development: pilot](03_Development.md#repository-graph-pilot) |
| Смежные dossiers | [FTR-002, FTR-016, FTR-017, FTR-021](06_Features.md): routing без изменения dispositions и зависимостей |

Уточнения системного ревью, перенесённые вместе с R2: кандидат pilot проверяет существенный стык AOS и условия окружения; графовый рабочий цикл применяется только при выборе карты для задачи; FTR-017 добавлен как тематический маршрут. Эти уточнения остаются частью предложения. Кандидат сценария «подготовленная задача → preflight → условия допуска исполнения» имеет документационное основание `AOS3-S09`; reference не выбирает будущую topology или обязательный сценарий автоматически.

Числа mapping/bundle из rationale R2 остаются историческими `REPORTED` из его источников: выборки около 6,4 KB и 65 KB не считаются одинаковыми запросами; `KEEP_MONOLITH` — рекомендация эксперимента, не самостоятельное human architecture decision. Время lookup и размер storage не доказывают уменьшения переделок. Этот перенос не воспроизводил исторические отчёты и не устанавливает новые mutable facts AOS-3.

Budgets и latency в canonical proposal — проектные цели pilot. Реализация, runtime validation, сравнительный pilot и миграция по данному ТЗ: `NOT_RUN`. Нынешние SHA, абсолютные paths и выбранные в эксперименте tools не являются конфигурацией будущего repository.

## 13. Ограничения

- Byte-complete chat export: `NOT_RUN`.
- Historical runtime execution: `NOT_RUN`.
- Current legacy test/CI reproduction: `NOT_RUN`.
- Independent semantic validation: `NOT_RUN`.
- GitHub links в ChatGPT Project являются routing pointers, а не автоматически импортированными sources.
- Reference repositories не предоставляют approval, implementation или Git authority.
