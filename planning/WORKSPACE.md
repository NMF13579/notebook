---
document_type: PLANNING_WORKSPACE
revision: DRAFT-R2
status: DRAFT
authority: NONE
human_acceptance: NOT_REQUESTED
implementation_authorization: NONE
git_authorization: NONE
repository: NMF13579/notebook
target_branch: dev
repository_path: planning/WORKSPACE.md
updated: 2026-08-04
---

# AOS-3 — общий план создания системы

## 1. Назначение

Этот файл — единое рабочее место для общего плана AOS-3. Он показывает, **что создаётся, в какой очередности и как крупные части соединяются друг с другом**.

План объединяет:

1. строительные леса для будущей разработки;
2. постоянную базовую инфраструктуру AOS;
3. основной pipeline движения проекта;
4. завершающую сборку инструкций для агента.

Это `DRAFT`: рабочий план не является canonical project knowledge, Task Brief, architecture acceptance или разрешением на реализацию.

## 2. Границы владения

| Что | Владелец |
|---|---|
| Принятые сведения о проекте | `docs/00_Core.md` — `docs/06_Features.md` |
| Общий рабочий план | `planning/WORKSPACE.md` |
| Будущий принятый versioned plan | Отдельный artifact в `planning/` после human review |
| Состояние активной задачи | `planning/CURRENT.md` |
| Исполнимая задача | Отдельный `Task-xxx.md` после выбора bounded slice |

`WORKSPACE.md` связывает authoritative owners, но не заменяет их.

## 3. Общая последовательность

```text
0. Принять необходимые product и architecture decisions
→ 1. Создать строительные леса
→ 2. Создать базовую инфраструктуру: первоочередное ядро
→ 3. Запустить основной pipeline из трёх частей
→ 4. Подключать вторую группу базовой инфраструктуры перед её первым использованием
→ 5. Уточнить AGENTS.md для работы агента по собранной системе
```

Важно: вторая группа базовой инфраструктуры не обязательно реализуется одним пакетом после первой. Каждый компонент подключается перед первым сценарием, который от него зависит. Например, `Recovery / Resume / Rollback` обязателен до первой записывающей product-операции.

## 4. Этап 0 — необходимые решения до реализации

До создания runtime-кода человек должен определить минимум:

- implementation repository;
- первый Product Runtime domain и первый vertical slice;
- основной interface: CLI, local UI или другое;
- язык, framework, package manager и поддерживаемые версии;
- способ хранения Project Memory;
- supported environments;
- границы первого read-only пользовательского маршрута.

Пока решения отсутствуют, безопасная детализация документов может продолжаться, но реализация имеет статус `BLOCKED` или `NOT_RUN` в соответствующей boundary.

## 5. Этап 1 — строительные леса

### Цель

Один раз подготовить воспроизводимую и безопасную среду, чтобы coding agent не создавал структуру проекта, команды, проверки и правила записи на ходу.

### Состав

1. Зафиксировать технические решения и exact scope лесов.
2. Создать каркас репозитория и границы модулей.
3. Закрепить toolchain, package manager и зависимости.
4. Создать единый command surface: `setup`, `run`, `test`, `check`, `format`, `build`, `doctor`, `self-test`.
5. Подготовить typed configuration и разделение environments.
6. Создать минимальную запускаемую оболочку без product behavior.
7. Создать test harness и negative fixtures.
8. Настроить formatter, linter, type/schema checks и fail-closed aggregation.
9. Создать минимальный CI, вызывающий те же команды, что и local environment.
10. Подготовить каркас Registry и его read-only validator.
11. Подготовить минимальные technical contracts и templates.
12. Добавить repository preflight, allowed paths и проверку actual diff.
13. Создать безопасный development bootstrap с dry-run, idempotency и partial-write detection.
14. Добавить scaffold-level `doctor` и `self-test`.
15. Проверить леса из clean checkout и сформировать Evidence.

### Результат

Готовая среда для реализации первого real vertical slice: она воспроизводимо устанавливается, запускается, проверяется и диагностируется.

### Граница

Строительные леса не являются Product Runtime, consumer installer, полной Governance, release automation или реализацией product features.

## 6. Этап 2 — базовая инфраструктура

Базовая инфраструктура — постоянные механизмы AOS, которые обслуживают весь pipeline. Она делится на две группы.

### 6.1. Первоочередное ядро

| ID | Компонент | Роль |
|---|---|---|
| `BI-08` | Общие data contracts и strict loaders | Единые форматы и fail-closed validation |
| `BI-09` | Статусы и Result Contract | Разделение `PASS`, `FAIL`, `BLOCKED`, `UNKNOWN`, `NOT_RUN` |
| `BI-10` | Authority и permissions | Разделение facts, decisions и разрешений |
| `BI-05` | Минимальный Project Memory | Durable state, решения, blockers и next action |
| `BI-13` | Минимальные Evidence и technical logs | Доказательство выполненных действий и проверок |
| `BI-01` | UX-оболочка | Единая точка взаимодействия пользователя с AOS |
| `BI-02` | `Status / Next / Details` | Простое отображение текущего состояния |
| `BI-11` | Product-level Doctor и Self-Test | Диагностика contracts, state и возможности продолжения |

Первый пользовательский маршрут:

```text
запуск → doctor → status → next → details
```

Результат: пользователь видит честное состояние, проблему и одно следующее действие; технический `PASS` не смешивается с human acceptance или permission.

### 6.2. Подключить позже

| ID | Компонент | Обязательный момент подключения |
|---|---|---|
| `BI-12` | Recovery / Resume / Rollback | До первой записывающей product-операции |
| `BI-04` | Installer / updater | После выбора packaging и способа установки; updater/uninstaller — после стабилизации install |
| `BI-03` | First Start и Tutor | После стабилизации основного UX и first-start route |
| `BI-07` | Registry `feature → function → module → contract → tests` | До формирования implementation tasks и трассировки pipeline |
| `BI-06` | Context Manager / Context Pack | До полноценной работы coding agent с task-scoped context |
| `BI-14` | Knowledge, lessons и patterns | После появления реальных повторяемых задач; patterns остаются `REFERENCE_ONLY` |
| `BI-15` | Agent adapters | Первый — при подключении первого agent environment; следующие — по измеренной потребности |

«Позже» означает не необязательность, а **отсроченную реализацию до появления конкретного потребителя и проверяемого сценария**.

### 6.3. Правила совместимости

- Project Memory хранит текущее durable state.
- Registry индексирует связи и не становится owner product truth.
- `Status / Next / Details` только отображает производное состояние.
- Evidence и audit фиксируют действия и проверки, но не создают approval.
- Context Pack является временной минимальной выборкой из owners, а не второй памятью.
- UI и agent adapters не добавляют permissions и не копируют authority.
- Scaffold-level `doctor` проверяет среду разработки; Product-level Doctor проверяет runtime contracts и state. Оба используют общий Result Contract, но разные профили проверок.

## 7. Этап 3 — основной pipeline из трёх частей

Pipeline показывает пользовательский путь от идеи или готового ТЗ до принятого результата и следующего vertical slice.

### Часть 1. Проектирование и подготовка задачи

Превращает исходный intent в одну исполнимую задачу.

Составные части:

1. Приём идеи или готового ТЗ с сохранением original request.
2. Уточнение problem, actor, desired outcome, constraints, non-goals, assumptions и unknowns.
3. Формирование `Product Spec`.
4. Выделение фич, функций и пользовательских journeys.
5. Создание UX-скелета, если slice затрагивает интерфейс.
6. Выбор человеком ближайшего vertical slice.
7. Формирование feature-specific `Feature Contract`: actors, trigger, I/O, states, main flow, failures/recovery, dependencies, acceptance и negative scenarios.
8. Targeted research и `ADR` только при наличии конкретного material gap.
9. Облегчённая lazy decomposition только выбранного slice.
10. Создание одного bounded `Task Brief`.
11. Repository preflight и preview будущих изменений.

Результат: задача, готовая к отдельному `Execution Authorization`.

Граница: полный backlog всего проекта, автоматическая очередь и активация следующих задач в первый цикл не входят.

### Часть 2. Выполнение и проверка результата

Превращает отдельно разрешённую задачу в exact candidate с Evidence.

Составные части:

1. Получение отдельного `Execution Authorization`.
2. Проверка актуальности task, baseline, paths, operations и permissions.
3. Выполнение минимального изменения внутри allowed scope.
4. Targeted tests и обязательные negative tests.
5. Проверка actual diff и отсутствия scope creep.
6. Формирование Evidence и `Stage Report`.
7. Freeze exact candidate.
8. Отдельный read-only `VALIDATE`, если его требует риск.
9. Сверка acceptance criteria и relevant regression cases.
10. Формирование `Review Package`.

Результат: exact candidate, готовый к human review.

Граница: technical `PASS` не означает approval или acceptance.

### Часть 3. Принятие, завершение и продолжение

Закрывает задачу и создаёт безопасную точку продолжения.

Составные части:

1. Human review exact candidate.
2. Явное решение: `ACCEPT`, `NEEDS_CHANGES`, `REJECT` или `DEFER`.
3. При `NEEDS_CHANGES` — новая bounded correction task и возврат в соответствующую часть pipeline.
4. Отдельное разрешение на каждое действие `Commit`, `Push`, `Merge` или `Release`.
5. Выполнение только разрешённых Git-действий.
6. Обновление Project Memory.
7. Обновление Registry и связей `feature → function → task → tests`.
8. Фиксация актуальных statuses, blockers, checks и Evidence.
9. Создание lesson/pattern proposal при необходимости.
10. Определение одного следующего действия или следующего vertical slice.

Результат: закрытая задача, актуальное состояние проекта и понятная точка продолжения.

### 7.1. Непрерывная схема

```text
Часть 1. Спроектировать и подготовить задачу
→ отдельное Execution Authorization
→ Часть 2. Выполнить и проверить результат
→ решение человека
→ Часть 3. Завершить и продолжить
↺ следующий vertical slice
```

Внутри трёх пользовательских частей сохраняются обязательные границы:

```text
Task Brief ≠ Execution Authorization
PASS ≠ Acceptance
Acceptance ≠ Commit ≠ Push ≠ Merge ≠ Release
```

## 8. Этап 4 — итоговый AGENTS.md

После стабилизации строительных лесов, базовой инфраструктуры и pipeline уточняется `AGENTS.md`, который объясняет агенту:

- где находятся authoritative owners;
- как определить текущую часть pipeline;
- как получать task-scoped context;
- как формировать ближайший bounded `Task Brief`;
- как проверять authorization перед mutation;
- как завершать stage отчётом и stop;
- как обновлять state без создания параллельного owner;
- какие действия всегда требуют отдельного решения человека.

`AGENTS.md` связывает уже определённые contracts и не должен создавать новую product architecture или отдельный workflow.

## 9. Что вынесено за границы первого цикла

- подключение AOS к уже разрабатываемому проекту;
- расширенный mechanism Doctor для такого подключения;
- полный hierarchical backlog и автоматическая очередь;
- multi-agent orchestration;
- full RAG/vector backend;
- сложный Workbench/SaaS UI;
- plugin marketplace;
- автоматические Git-действия;
- progressive Governance и enforcement без измеренной потребности.

Эти направления могут стать отдельными модулями после проверки greenfield pipeline на реальных задачах.

## 10. Решения человека, зафиксированные в рабочем плане

| ID | Дата | Решение | Boundary |
|---|---|---|---|
| `DEC-W-001` | 2026-08-04 | Создать единое рабочее пространство общего плана в `notebook` | Planning only |
| `DEC-W-002` | 2026-08-04 | Сохранить отдельный этап строительных лесов без изменения его принятого состава | General plan structure |
| `DEC-W-003` | 2026-08-04 | Разделить базовую инфраструктуру на первоочередное ядро и подключаемую позже группу | General plan structure |
| `DEC-W-004` | 2026-08-04 | Показывать основной pipeline в трёх частях; более мелкие блоки оставить внутренней детализацией | General plan structure |

Эти записи фиксируют текущие human-confirmed directions в рабочем плане, но не заменяют отдельную human acceptance будущего versioned artifact.

## 11. Текущий статус

| Блок | Планирование | Реализация |
|---|---|---|
| Строительные леса | Состав проработан; включён в общий план | `NOT_RUN` |
| Базовая инфраструктура | Разделена на две группы; состав проработан | `NOT_RUN` |
| Pipeline | Разделён на три пользовательские части; внутренний flow описан | `NOT_RUN` |
| Итоговый `AGENTS.md` | Ожидает стабилизации общего плана | `NOT_RUN` |

Открыты product и architecture decisions из раздела 4. Implementation repository остаётся `UNASSIGNED`.

## 12. Следующий bounded action

Отдельно проработать **часть 1 pipeline — «Проектирование и подготовка задачи»** в формате:

```text
input → action → output → human gate → failure/recovery → owner → related contracts/tests
```

После этого связать её с первоочередным ядром и определить первый planning slice, не переходя к runtime implementation.
