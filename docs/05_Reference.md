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

## 12. Ограничения

- Byte-complete chat export: `NOT_RUN`.
- Historical runtime execution: `NOT_RUN`.
- Current legacy test/CI reproduction: `NOT_RUN`.
- Independent semantic validation: `NOT_RUN`.
- GitHub links в ChatGPT Project являются routing pointers, а не автоматически импортированными sources.
- Reference repositories не предоставляют approval, implementation или Git authority.
