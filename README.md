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

Активная база знаний находится в `docs/` и состоит ровно из семи документов:

- [00_Core.md](docs/00_Core.md) — identity, authority, source precedence и safety.
- [01_Product.md](docs/01_Product.md) — пользователи, проблемы и product boundaries.
- [02_Architecture.md](docs/02_Architecture.md) — architecture baseline и shared contracts.
- [03_Development.md](docs/03_Development.md) — workflow, validation, review и Git boundaries.
- [04_Lessons.md](docs/04_Lessons.md) — failures, lessons и regression catalog.
- [05_Reference.md](docs/05_Reference.md) — provenance и targeted research routes.
- [06_Features.md](docs/06_Features.md) — единый feature inventory и design-level dossiers.

Обязательная точка входа для агента: `docs/00_Core.md`.

### Рабочая область проектирования (AOS-3)

В репозитории также присутствует директория `archive/AOS-3/`.
Её цель — **собрать систематизированный материал** из официальной базы (`docs/`) и обсуждений (чатов) для проектирования новой документации. В дальнейшем эта "продуктовая папка" будет экспортирована и использована как активный источник знаний для применения в новом целевом репозитории. Материалы в `archive/AOS-3/` являются рабочими (drafts) и не переопределяют официальный baseline.

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
archive/.agents/rules/aos-documentation-repository.md
```

Правило следует включить как `Always On` в настройках workspace.

## Reference repositories

Primary historical references:

- AOS-FARM: https://github.com/NMF13579/AOS-FARM/tree/dev
- AgentOS: https://github.com/NMF13579/AgentOS/tree/dev

Они используются только read-only и только для targeted research. Их authority над target AOS — `NONE`. Exact snapshot и правила research указаны в `docs/05_Reference.md`.

## Изменения документации

Изменения должны быть bounded, сохранять семь fact-class owners, не создавать параллельные каталоги и не менять product/architecture/authority semantics без explicit human decision.
