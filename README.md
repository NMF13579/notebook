# AOS Project Knowledge Repository

`NMF13579/notebook` — активное хранилище принятой проектной базы знаний для проектирования и будущей разработки AOS.

```yaml
repository_role: ACTIVE_PROJECT_KNOWLEDGE_REPOSITORY
baseline_revision: R4-RU
source_snapshot_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
implementation_repository: NMF13579/AOS-3
implementation_authorization: NONE
git_authorization: NONE
```

Сам runtime AOS здесь не создаётся. Для первого ядра выбран AOS-3 с изолированной
branch/worktree; отдельная runtime launch authorization ещё не выдана.

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

### Scaffold и первое ядро

Для текущей подготовки автономной разработки читать [применимость решений](docs/00_Core.md#scaffold-core-decisions) → [результат и срезы](docs/01_Product.md#scaffold-core-outcome) → выбранные dossiers в `06_Features.md` → [стыки](docs/02_Architecture.md#scaffold-core-interfaces) → [внешний цикл разработки](docs/03_Development.md#scaffold-core-development) → [implementation brief](workspace/AOS_SCAFFOLD_CORE_IMPLEMENTATION_BRIEF.md).

First-core R7/V3 и HD-01…28 приняты в ограниченном scope у
[Core](docs/00_Core.md#scaffold-core-decisions). Это не выбор всех FTR и не
runtime proof/launch. Полномочия текущей задачи ограничены документацией.
Дальнейшие фичи готовятся отдельно по [правилу интеграции](docs/03_Development.md#feature-integration-readiness).

Замороженный `AOS/`, portable package и прежний AOS-3 blueprint сохраняют свои exact identities и исходные области принятия. Для новой задачи они используются через [provenance и границы применимости](docs/05_Reference.md#scaffold-core-sources); их прежний маршрут не является вторым активным заданием. Изменение frozen subject требует отдельного Reopen.

### Архив

Исторические материалы прежнего процесса находятся в [`archive/aos-archive/`](archive/aos-archive/README.md).

```yaml
status: REFERENCE_ONLY
authority: NONE
```

Архив не определяет текущий процесс, план, требования или разрешения. Активной принятой базой знаний остаются ровно семь документов `docs/00_Core.md`–`docs/06_Features.md`.

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

Архивные `.agents/rules/**` являются `REFERENCE_ONLY` и не должны включаться как `Always On`.

## Reference repositories

Primary historical references:

- AOS-FARM: https://github.com/NMF13579/AOS-FARM/tree/dev
- AgentOS: https://github.com/NMF13579/AgentOS/tree/dev

Они используются только read-only и только для targeted research. Их authority над target AOS — `NONE`. Exact snapshot и правила research указаны в `docs/05_Reference.md`.

## Изменения документации

Изменения должны быть bounded, сохранять семь fact-class owners, не создавать параллельные каталоги и не менять product/architecture/authority semantics без explicit human decision.
