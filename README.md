# AOS Project Knowledge Repository

`NMF13579/notebook` — активное хранилище принятой проектной базы знаний для проектирования и будущей разработки AOS.

```yaml
repository_role: ACTIVE_PROJECT_KNOWLEDGE_REPOSITORY
baseline_revision: R4-RU
source_snapshot_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
```

Сам runtime AOS в этом репозитории не создаётся без отдельного решения о target implementation repository.

## Документация

Активная база знаний находится в `AOS-3/` и состоит ровно из семи документов:

- [00_Core.md](AOS-3/00_Core.md) — identity, authority, source precedence и safety.
- [01_Product.md](AOS-3/01_Product.md) — пользователи, проблемы и product boundaries.
- [02_Architecture.md](AOS-3/02_Architecture.md) — architecture baseline и shared contracts.
- [03_Development.md](AOS-3/03_Development.md) — workflow, validation, review и Git boundaries.
- [04_Lessons.md](AOS-3/04_Lessons.md) — failures, lessons и regression catalog.
- [05_Reference.md](AOS-3/05_Reference.md) — provenance и targeted research routes.
- [06_Features.md](AOS-3/06_Features.md) — единый feature inventory и design-level dossiers.

Обязательная точка входа для агента: `AOS-3/00_Core.md`.

## Статус и authority

Пакет принят человеком как knowledge baseline. Authority ограничена fact class конкретного документа и статусом конкретного утверждения.

```text
Knowledge baseline ≠ implementation
Feature inventory ≠ approved roadmap
Documentation ≠ runtime Evidence
PASS ≠ approval
Evidence ≠ approval
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Принятие документации не предоставляет implementation или Git authorization.

## Инструкции для агентов

Repository-aware agents должны соблюдать [AGENTS.md](AGENTS.md).

Для Google Antigravity добавлено workspace rule:

```text
.agents/rules/aos-documentation-repository.md
```

Правило следует включить как `Always On` в настройках workspace.

## Reference repositories

Primary historical references:

- AOS-FARM: https://github.com/NMF13579/AOS-FARM/tree/dev
- AgentOS: https://github.com/NMF13579/AgentOS/tree/dev

Они используются только read-only и только для targeted research. Их authority над target AOS — `NONE`. Exact snapshot и правила research указаны в `AOS-3/05_Reference.md`.

## Изменения документации

Изменения должны быть bounded, сохранять семь fact-class owners, не создавать параллельные каталоги и не менять product/architecture/authority semantics без explicit human decision.
