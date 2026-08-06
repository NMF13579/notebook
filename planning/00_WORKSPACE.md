---
document_type: PLANNING_WORKSPACE
revision: DRAFT-R4
status: DRAFT
claim_class: SYNTHESIZED_PROPOSAL
authority: NONE
human_acceptance: NOT_RUN
documentation_plan_readiness: READY_FOR_HUMAN_REVIEW
implementation_readiness: BLOCKED_PENDING_DECISIONS
implementation_authorization: NONE
git_authorization: NONE
knowledge_repository: NMF13579/notebook
implementation_repository: UNASSIGNED
updated: 2026-08-04
active_path: planning/00_WORKSPACE.md
supersedes: planning/WORKSPACE.md@DRAFT-R3
documentation_detail_plan: planning/01_DOCUMENTATION_PRODUCTION_PLAN.md
agent_instruction_draft: planning/02_AGENTS_DRAFT.md
current_state_owner: planning/CURRENT.md
---

# AOS-3 — исправленный общий план создания проекта

## 1. Вывод

AOS-3 создаётся последовательно в пяти крупных этапах:

```text
1. Принять исходные решения и подготовить bootstrap-инструкции агенту
→ 2. Создать строительные леса
→ 3. Создать постоянное рабочее ядро
→ 4. Создать pipeline по трём частям
→ 5. Провести dogfood, расширить только доказанно нужное и финализировать AGENTS.md
```

Главное исправление относительно `DRAFT-R2`: базовая инфраструктура больше не делится на «обязательную сейчас» и единый этап «подключить потом». Каждый компонент создаётся **до первого шага, который не может безопасно работать без него**.

Этот документ показывает порядок создания проекта и связи между этапами. Он не является исполнимым roadmap, выбором конкретной feature, Task Brief, Execution Authorization или разрешением на Git-действия.

## 2. Как читать план

Этот файл является владельцем общей последовательности создания AOS-3. Подробный маршрут подготовки документации для передачи coding agent вынесен в `planning/01_DOCUMENTATION_PRODUCTION_PLAN.md`. Черновой operating contract будущего coding agent находится в `planning/02_AGENTS_DRAFT.md`. Текущее durable состояние документационного процесса хранится только в `planning/CURRENT.md`.

Эти связанные документы раскрывают общий план, но не меняют его authority и не предоставляют implementation или Git authorization.

### 2.1. Крупный этап

Крупный этап создаёт самостоятельный проверяемый результат, необходимый следующему этапу.

### 2.2. Подэтап

Подэтап — ограниченная часть работы внутри крупного этапа. Для его последующей реализации должен быть подготовлен отдельный contract в формате:

```text
input → action → output → dependency gate → owner
→ acceptance → negative tests → failure/recovery → next transition
```

### 2.3. Gate

Gate — условие, без которого зависимый шаг не начинается. Пояснение в тексте не заменяет machine-checkable gate.

## 3. Единая модель владения состоянием

Чтобы разные агенты не восстанавливали разные версии состояния, для каждого fact class устанавливается один owner.

| Fact class | Единственный owner | Что не является owner |
|---|---|---|
| Product truth | Human-accepted Product Spec / Feature Contract | Registry, UI, Context Pack |
| Scope одной задачи | Exact `Task Brief` | Project Memory, Stage Report |
| Execution permission | Exact `Execution Authorization Record` | Task Brief, кнопка UI, technical `PASS` |
| Текущее durable lifecycle state | `Project Memory` | Task Brief, Registry, dashboard |
| Текущее представление Project Memory в `notebook` | `planning/CURRENT.md` | Параллельный task-local state file |
| Факт конкретного запуска | Immutable `Stage Report` / Execution Record | Current-state dashboard |
| Evidence | Immutable subject-bound Evidence Record | Human decision |
| Human decision | Human-authored/verified Decision Record | Agent recommendation |
| Навигация и трассировка | Rebuildable Registry | Product truth или lifecycle state |
| Отображение состояния | Derived `Status / Next / Details` | Durable lifecycle state |
| Контекст агента | Temporary task-scoped Context Pack | Вторая постоянная память |

`Task Brief` после подтверждения scope не хранит изменяющийся stage. `Project Memory` ссылается на Task Brief и Stage Reports, но не переписывает их историю.

## 4. Общая карта зависимостей

```text
Решения человека
  ↓
Bootstrap AGENTS_DRAFT
  ↓
Строительные леса
  ↓
Contracts + Statuses + Authority + Project Memory + Evidence
  ↓
Doctor + Status / Next / Details
  ↓
Registry + Context Pack
  ↓
Pipeline Part 1: Product Spec → Feature Contract → Task Brief → Preview
  ↓ отдельное Execution Authorization
Product Recovery + Scoped Executor + Validation Foundation
  ↓
Pipeline Part 2: Execute → Evidence → Freeze → VALIDATE → Review Package
  ↓ решение человека
Pipeline Part 3: Decision → отдельно разрешённые state/Git actions → Handoff
  ↓
Dogfood → corrections → final thin AGENTS.md
```

## 5. Крупный этап 1 — исходные решения и bootstrap агента

### Цель

Убрать решения, которые coding agent не вправе принимать сам, и дать ему минимальную временную инструкцию для создания следующих этапов.

### Подэтап 1.1 — единый decision package

Человек получает один компактный пакет связанных решений, а не серию технических вопросов.

Нужно определить:

1. implementation repository;
2. первый user problem и первый smallest vertical slice;
3. основной interface первого цикла: CLI, local UI или другой;
4. язык, framework, package manager и закреплённые версии;
5. модель данных первого цикла: file/no-DB/DB;
6. supported environments;
7. способ persistence для Project Memory;
8. primary agent environment;
9. границу первого read-only маршрута;
10. item-level disposition только для `FTR-*`, необходимых ближайшему этапу.

Агент должен предложить рекомендуемые defaults, trade-offs, affected decisions и один preferred вариант. Не относящиеся к текущему этапу решения остаются `UNDECIDED`.

### Подэтап 1.2 — bootstrap `AGENTS_DRAFT`

До scaffolding создаётся короткий временный operating contract для coding agent. Он содержит только:

- роль и objective;
- routing к `docs/00_Core.md` и релевантным owners;
- обязательные safety boundaries;
- startup/preflight algorithm;
- task-local autonomy, ask/stop rules;
- одного owner текущего состояния;
- запрет durable writes без exact authorization;
- placeholders для ещё не созданных commands и paths.

Он не дублирует весь pipeline, contracts и Stage Report из `00_Core.md`–`03_Development.md`.

### Подэтап 1.3 — принять exact scaffolding scope

Подготовить первый bounded Task Brief только для строительных лесов. Отдельно получить Execution Authorization на exact repository, paths и operations.

### Результат этапа

- приняты необходимые исходные решения;
- существует thin bootstrap-инструкция агенту;
- подготовлен и отдельно разрешён exact scaffolding task.

### Gate перехода

Нельзя начинать реализацию scaffolding, пока implementation repository, toolchain, first interface boundary и exact authorization имеют состояние, допускающее действие.

## 6. Крупный этап 2 — строительные леса

### Цель

Создать воспроизводимую среду, в которой агент реализует продуктовые компоненты одинаковым способом, а не проектирует структуру и проверки заново для каждой задачи.

### Подэтап 2.1 — topology и toolchain

1. Создать modular-monorepo skeleton.
2. Разделить Product Runtime, Development Factory, Safety и Knowledge boundaries.
3. Закрепить язык, runtime, package manager и зависимости.
4. Создать typed configuration и environment separation.
5. Зафиксировать ownership каталогов и protected paths.

### Подэтап 2.2 — единый command surface

Подготовить согласованные команды:

```text
setup | run | test | check | format | build | doctor | self-test
```

Команды должны иметь стабильные exit codes, `--help` без writes и одинаковое поведение локально и в CI.

### Подэтап 2.3 — минимальная техническая оболочка

1. Создать запускаемую оболочку без product behavior.
2. Добавить test harness и negative fixtures.
3. Настроить formatter, linter, type/schema checks.
4. Настроить fail-closed aggregation результатов.
5. Добавить минимальный CI, вызывающий локальные команды.

### Подэтап 2.4 — safeguards для разработки

1. Repository preflight.
2. Allowed-path и actual-diff checks.
3. Safe temp boundary.
4. Secrets/redaction check.
5. Atomic/journaled scaffold writes.
6. Idempotent development bootstrap.
7. Partial-write detection и scaffold-level recovery.

Это recovery самих лесов, а не реализация Product Runtime `FTR-014`.

### Подэтап 2.5 — scaffold diagnostics

1. Scaffold-level `doctor`.
2. Scaffold-level `self-test`.
3. Clean-checkout setup.
4. Повторный запуск setup без повреждения состояния.
5. Intentional interruption и безопасное resume.
6. Evidence выполненных и `NOT_RUN` проверок.

### Результат этапа

Из чистого checkout агент может установить среду, запустить оболочку, выполнить единые проверки, диагностировать проблему и добавить тестовый модуль по установленному шаблону.

### Gate перехода

Все scaffold acceptance и negative checks проходят на exact candidate; human decision и Git delivery оформлены отдельно.

## 7. Крупный этап 3 — постоянное рабочее ядро AOS

### Цель

Создать минимальные постоянные механизмы, на которых будут работать все три части pipeline.

### Подэтап 3.1 — contracts, statuses и authority

Создать и проверить:

1. versioned data contracts и strict loaders;
2. ортогональные оси `Task stage`, `Technical result`, `Human decision`, `Permission`;
3. fail-closed Result Contract;
4. Authority Resolver;
5. permission classifier и Action Trust Boundary;
6. запрет превращать Evidence, UI action или generated text в approval.

Не вводить дополнительные free-form readiness statuses. До отдельного принятия readiness axis используются существующие `HUMAN_REVIEW_REQUIRED` и `HUMAN_AUTHORIZATION_REQUIRED` в своих осях.

### Подэтап 3.2 — Project Memory как один current-state owner

Создать:

1. schema Project Memory;
2. атомарную загрузку/запись;
3. freshness и repository-identity checks;
4. ссылки на immutable Task Brief, candidate, Stage Reports и decisions;
5. blockers, authorization state и one next action;
6. resume после новой session без истории чата.

В `notebook` current implementation этого contract представляется `planning/CURRENT.md` до отдельного решения о target path.

### Подэтап 3.3 — Evidence и immutable event records

Создать Evidence Record и Stage Report foundation с exact subject identity, checks run/not run, limitations, changed paths и stop reason.

### Подэтап 3.4 — read-only пользовательская оболочка

Создать минимальный маршрут:

```text
run → doctor → status → next → details
```

Surface читает Project Memory и contracts, но не изменяет lifecycle state.

### Подэтап 3.5 — Product-level Doctor / Self-Test

Проверять:

- доступность и валидность owners;
- status vocabulary;
- Project Memory freshness;
- repository identity;
- отсутствие conflicting owners;
- возможность безопасно продолжить;
- честные `UNKNOWN`, `NOT_RUN` и `BLOCKED`.

### Подэтап 3.6 — Registry и Context Pack

До создания implementation tasks необходимо реализовать минимально:

1. Product Feature Registry как rebuildable index;
2. Execution/Verification Registry как rebuildable index;
3. связи `feature → function → task → contract → tests`;
4. minimal task-scoped Context Pack;
5. freshness/provenance explanation;
6. rebuild без утраты product truth или lifecycle state.

Registry и Context Pack не получают authority и не становятся второй памятью.

### Подэтап 3.7 — task-local coordinator contract

Coordinator читает terminal record и может открыть только разрешённый следующий run. Он не получает mutation authority и не выбирает следующую task.

| Terminal state | Следующий run | Условие |
|---|---|---|
| `PLAN + HUMAN_AUTHORIZATION_REQUIRED` | Нет | Нужен exact human authorization |
| `EXECUTE + PASS + candidate frozen` | `VALIDATE` | Только read-only; предусмотрено Task Brief/risk |
| `EXECUTE + FAIL/BLOCKED/UNKNOWN` | Нет | Report, stop, one next action |
| `VALIDATE + PASS` | `REVIEW` | Exact candidate не изменён |
| `VALIDATE + finding` | Нет | Отдельная correction boundary |
| `REVIEW` | Нет | Нужен human decision |

Ни один terminal state не активирует автоматически следующую task или vertical slice.

### Результат этапа

AOS умеет честно хранить и показывать текущее состояние, проверять своё ядро, восстанавливать task-scoped context и координировать безопасные read-only transitions.

### Gate перехода

До формирования первого real Task Brief должны быть готовы и проверены Registry, minimal Context Pack, Project Memory, Result/Authority contracts и repository preflight foundation.

## 8. Крупный этап 4 — создание pipeline по трём частям

Этап 4 создаётся в той же последовательности, в которой пользователь будет проходить pipeline.

## 8.1. Часть 1 — проектирование и подготовка задачи

### Цель

Превратить идею или готовое ТЗ в одну ближайшую исполнимую задачу.

### Подэтап 4.1.1 — intake и discovery

1. Сохранить original request.
2. Определить actor, problem, desired outcome и current workaround.
3. Зафиксировать constraints, non-goals, assumptions и unknowns.
4. Задать только material questions.

### Подэтап 4.1.2 — Product Spec и карта поведения

1. Сформировать Product Spec.
2. Выделить features, functions и journeys.
3. При необходимости создать UX-skeleton: scenarios, access, objects, screen map и user review.

### Подэтап 4.1.3 — выбор vertical slice и Feature Contract

Человек выбирает smallest user-visible slice. Для него создаётся exact Feature Contract: actors, trigger, I/O, states, transitions, main flow, failures/recovery, dependencies, constraints, acceptance и negative scenarios.

### Подэтап 4.1.4 — targeted research и ADR

Только при material gap:

```text
selected feature → narrow question → exact repo/ref/commit/path
→ high-signal evidence → classified finding → remaining unknown
```

Architecture decision создаётся только если Feature Contract не позволяет выбрать реализацию без скрытого product/architecture решения.

### Подэтап 4.1.5 — облегчённая декомпозиция

Создаётся только одна ближайшая задача:

```text
Goal → Stage → Sub-stage только при material boundary → executable Task
```

Полный hierarchical backlog, автоматическая очередь и автозапуск следующей задачи не входят в первый цикл.

### Подэтап 4.1.6 — Task Brief, validation matrix и preview

1. Скомпилировать exact Task Brief.
2. Проверить связь с Feature Contract и Registry.
3. Сформировать acceptance/negative validation matrix.
4. Провести repository preflight.
5. Показать planned paths, operations, conflicts и exact execution preview.
6. Сформировать compact decision package.

В одном пользовательском package можно показать выбор slice, Feature Contract, Task Brief и authorization form, но эти сущности остаются отдельными records.

### Результат части 1

Exact Task Brief и preview; Permission state — `HUMAN_AUTHORIZATION_REQUIRED`.

### Hard gates

- Registry и minimal Context Pack готовы до Task Brief.
- Task Brief не изменяет Project Memory без отдельной authorized operation.
- Execution не начинается без exact Execution Authorization.

## 8.2. Часть 2 — выполнение и проверка результата

### Цель

Превратить отдельно разрешённую задачу в frozen exact candidate с Evidence.

### Подэтап 4.2.0 — hard gate до первой Product Runtime write

До любой write-capable product operation создать и проверить:

1. Product Recovery Contract;
2. operation journal;
3. partial-write detection;
4. intended/actual reconciliation;
5. idempotent retry только при неизменных scope, identity и permission;
6. bounded resume/rollback;
7. denied-action log;
8. post-recovery validation;
9. thin scoped executor consuming exact authorization;
10. freeze и validation boundary.

Destructive rollback требует отдельного human authorization.

### Подэтап 4.2.1 — authorization и re-preflight

1. Получить exact Execution Authorization.
2. Проверить task, repository, worktree, branch, HEAD, baseline и candidate identity.
3. Сверить allowed operations/paths, expiry и consumption.
4. При stale identity или material unknown остановиться.

### Подэтап 4.2.2 — smallest scoped execution

1. Выполнить только разрешённую causal change.
2. Journal каждую durable mutation.
3. Не исправлять unrelated defects.
4. При scope expansion остановиться и запросить новую boundary.

### Подэтап 4.2.3 — tests, Evidence и diff

1. Targeted positive tests.
2. Обязательные negative tests.
3. Relevant regression/smoke checks.
4. Actual diff и changed-file allowlist.
5. Security/release blockers в требуемом scope.
6. Evidence с exact subject identity и `NOT_RUN` limitations.

### Подэтап 4.2.4 — Stage Report и freeze

Сформировать immutable Stage Report, зафиксировать exact candidate и остановить `EXECUTE`.

### Подэтап 4.2.5 — отдельный VALIDATE

Read-only validation:

1. проверяет exact frozen candidate;
2. не исправляет findings;
3. повторяет только необходимые проверки;
4. сверяет acceptance, negative cases, scope и regression;
5. останавливается при finding.

### Подэтап 4.2.6 — Review Package

Один компактный документ показывает before/after, user impact, exact paths, Evidence, `NOT_RUN`, limitations, findings, decision options и one next action.

### Результат части 2

Frozen exact candidate и Review Package. Technical `PASS` не является human acceptance.

## 8.3. Часть 3 — принятие, завершение и продолжение

### Цель

Получить явное решение человека, безопасно зафиксировать разрешённые последствия и оставить одну точку продолжения.

### Подэтап 4.3.1 — human review

Человек выбирает:

```text
ACCEPT | NEEDS_CHANGES | REJECT | DEFER
```

Decision Record bind к exact candidate. Agent recommendation не создаёт decision.

### Подэтап 4.3.2 — correction loop

При `NEEDS_CHANGES` создаётся отдельная bounded correction task. Старое authorization не переносится автоматически. После correction создаётся новый candidate и повторяется требуемая validation/review boundary.

### Подэтап 4.3.3 — отдельно разрешённые durable state updates

Обновление Project Memory, Registry или любого lifecycle record является mutation и должно быть:

- включено в exact `allowed_operations/allowed_paths`; или
- выполнено отдельной authorized state-transition task.

Если authorization отсутствует, агент формирует read-only proposed update и останавливается. `Status / Next / Details` никогда не мутирует state.

### Подэтап 4.3.4 — отдельно разрешённый Git lifecycle

Каждое действие имеет отдельное решение и повторный preflight:

```text
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Acceptance не разрешает Git delivery автоматически.

### Подэтап 4.3.5 — handoff, lesson и one next action

1. Сформировать compact handoff.
2. Обновить разрешённые derived indexes.
3. Создать lesson/pattern proposal при реальном повторяемом сигнале.
4. Показать одно следующее действие.
5. Не активировать автоматически следующий vertical slice.

### Результат части 3

Задача имеет явное human decision, разрешённые state/Git consequences выполнены или честно `NOT_RUN`, а Project Memory показывает одну безопасную точку продолжения.

## 9. Крупный этап 5 — dogfood, условное расширение и финализация

### Цель

Проверить не только компоненты по отдельности, но и весь greenfield путь глазами непрограммиста; затем оставить только доказанно полезную automation.

### Подэтап 5.1 — сквозной manual dogfood

Выполнить несколько полных циклов:

```text
idea → Product Spec → Feature Contract → Task Brief → authorization
→ execution → Evidence → VALIDATE → review → decision → handoff
```

Проверить interruption/resume на границах writes и переходы между sessions/agent environments.

### Подэтап 5.2 — измерение

Измерять:

- time intent → Task Brief;
- количество material clarification loops;
- scope drift;
- resume time;
- time to Evidence/review;
- authority confusion;
- false-green incidents;
- handoff quality;
- долю задач без повторного planning;
- Governance overhead.

### Подэтап 5.3 — bounded corrections

Исправлять только повторяемые проблемы с известной причиной, acceptance, negative cases и recovery. Не строить full platform по единичному случаю.

### Подэтап 5.4 — capability-on-demand

Следующие компоненты создаются только перед первым подтверждённым consumer scenario:

| Capability | Момент подключения |
|---|---|
| Consumer installer/update | После принятия packaging/ownership contract и до первого consumer install |
| First-Start/Tutor | После стабилизации основного UX и до первого неподготовленного пользователя |
| Дополнительный agent adapter | Перед подключением конкретной среды |
| Knowledge/pattern library | После появления повторяемых lessons |
| Advanced registry drift guard | После измеренного drift problem |
| RAG-light | После измеренной проблемы поиска/контекста |
| CI/release expansion | После стабилизации checks и release route |

Подключение AOS к уже разрабатываемому проекту и расширенный Doctor для такого подключения остаются отдельным будущим модулем. Greenfield pipeline сначала должен пройти dogfood.

### Подэтап 5.5 — final thin root `AGENTS.md`

После dogfood bootstrap draft сокращается и уточняется до root-инструкции, которая:

1. направляет к owners;
2. содержит только non-negotiable boundaries;
3. знает реальные commands и paths;
4. использует exact Project Memory contract;
5. содержит coordinator/stop rules;
6. не дублирует документацию pipeline;
7. получает отдельный semantic audit и human acceptance.

### Результат этапа

Есть проверенный greenfield workflow, измеренные ограничения, thin root `AGENTS.md` и ясный список capability-on-demand без преждевременной платформизации.

## 10. Traceability базовой инфраструктуры

Все строки ниже имеют статус `PROPOSAL`. Mapping не означает item-level selection: в `06_Features.md` соответствующие `human_disposition` остаются `UNDECIDED`, пока человек не примет exact feature revision.

| BI | Постоянный механизм | Связанные feature families | Первый consumer / gate |
|---|---|---|---|
| `BI-01` | UX-оболочка | `FTR-008` | Read-only core route |
| `BI-02` | `Status / Next / Details` | `FTR-008` | Первый status request |
| `BI-03` | First-Start / Tutor | `FTR-004`, `FTR-008` | Первый неподготовленный пользователь |
| `BI-04` | Installer / updater | `FTR-004` | Первый consumer install |
| `BI-05` | Project Memory | `FTR-016` | Первый durable lifecycle state |
| `BI-06` | Context Pack | `FTR-016` | Первый Task Brief coding agent |
| `BI-07` | Registries / traceability | `FTR-003`, `FTR-006`, `FTR-016` | Первый Task Brief |
| `BI-08` | Data contracts / strict loaders | `FTR-011` | Первый persistent contract |
| `BI-09` | Result/status contract | `FTR-011` | Первый reported result |
| `BI-10` | Authority / permissions | `FTR-006`, `FTR-019` | Первый authorization request |
| `BI-11` | Doctor / Self-Test | `FTR-011` | Первый resumable core route |
| `BI-12` | Recovery / Resume / Rollback | `FTR-014` | До первой Product Runtime write |
| `BI-13` | Evidence / technical log | `FTR-012` | Первый technical claim |
| `BI-14` | Knowledge / lessons / patterns | `FTR-022`, `FTR-025` | Первый repeatable lesson |
| `BI-15` | Agent adapters | `FTR-016`, `FTR-029` | Первый дополнительный agent environment |

Для каждого выбранного mapping до implementation дополнительно создаётся строка:

```text
BI → accepted FTR disposition → contract owner → exact first consumer
→ acceptance criteria → negative tests → implementation Task Brief
```

## 11. Человеческое участие: минимальное, но достаточное

Агент не спрашивает человека о безопасных обратимых технических деталях внутри принятого scope. Человеку показываются компактные decision-ready packages в ключевых точках:

| Точка | Что можно показать вместе | Что остаётся раздельным по смыслу |
|---|---|---|
| До scaffolding | Repository, toolchain, interface, first slice, persistence | Каждое принятое decision field |
| После Part 1 | Slice, Feature Contract, Task Brief, preview, authorization form | Product decision, Task Brief и Execution Authorization |
| После Part 2 | Candidate, Evidence, limitations, recommendation | Technical result и human decision |
| После acceptance | Proposed state update и Git options | State authorization, Commit, Push, Merge, Release |

Агент самостоятельно выполняет preflight, технический выбор внутри принятых границ, checks и bounded correction cycles только пока не меняются product behavior, architecture, scope, authority или risk.

## 12. Границы первого цикла

Не входят в foundation первого greenfield цикла:

- полный hierarchical backlog и автоматическая очередь;
- автоматическая активация следующей task;
- multi-agent cascade;
- full RAG/vector DB;
- full Control Plane и progressive enforcement без measured need;
- Workbench/SaaS UI;
- plugin marketplace;
- предметные regulated-domain modules;
- automatic Commit/Push/Merge/Release;
- самостоятельное подключение к существующему разрабатываемому проекту.

## 13. Статус крупных этапов

| Этап | Планирование | Реализация | Текущий blocker |
|---|---|---|---|
| 1. Решения и bootstrap | Исправленный состав предложен | `NOT_RUN` | Exact human decisions |
| 2. Строительные леса | Подробный DRAFT существует | `NOT_RUN` | Stage 1 + Task Brief + authorization |
| 3. Постоянное ядро | Последовательность исправлена | `NOT_RUN` | Scaffolding + selected contracts/features |
| 4. Pipeline | Три части и gates описаны | `NOT_RUN` | Core prerequisites + feature contracts |
| 5. Dogfood/finalization | Состав определён | `NOT_RUN` | Работающий pipeline |

## 14. Что исправлено по итогам аудита

| Finding | Исправление в DRAFT-R3 |
|---|---|
| `F-01` | Открытые implementation decisions вынесены в Stage 1; inference запрещён |
| `F-02` | `BI-*` привязаны к exact first-consumer gates; поздний общий infrastructure stage удалён |
| `F-03` | Project Memory назначен единственным owner current lifecycle state |
| `F-04` | Любая durable lifecycle/Registry mutation требует exact authorization |
| `F-05` | Добавлен минимальный coordinator transition contract |
| `F-06` | План требует thin bootstrap/final `AGENTS.md`; подробный pipeline остаётся вне root |
| `F-07` | Новые readiness statuses не используются без отдельного accepted contract |
| `F-08` | Добавлена `BI ↔ FTR ↔ first consumer` traceability |
| `F-09` | Bootstrap agent instructions перенесены до scaffolding; final root оставлен после dogfood |
| `F-10` | Для будущих stage contracts задан обязательный executable template |
| `F-11` | Human choices группируются в compact decision packages без смешения records |

## 15. Следующий bounded action

Провести human review exact revision активного planning package, зафиксированного в `planning/CURRENT.md`. Предмет review ограничен порядком создания проекта, последовательностью документационных задач и связанными planning guidance.

Этот review не включает и не разрешает:

1. запуск `DOC-001`;
2. выбор implementation repository, first vertical slice, interface, toolchain или feature dispositions;
3. активацию `planning/02_AGENTS_DRAFT.md` как root `AGENTS.md`;
4. runtime implementation;
5. `Commit`, `Push`, `Merge` или `Release`.

После exact human acceptance отдельным следующим действием может быть запуск `DOC-001` для подготовки единого decision-ready package checkpoint `H1`.

```yaml
plan_status: DRAFT
macro_sequence: CORRECTED_PROPOSAL
documentation_plan_readiness: READY_FOR_HUMAN_REVIEW
human_acceptance: NOT_RUN
DOC-001: NOT_RUN
implementation_readiness: BLOCKED_PENDING_DECISIONS
implementation_authorization: NONE
git_authorization: NONE
next_action: HUMAN_REVIEW_EXACT_DOCUMENTATION_PLAN_REVISION
stop: true
```
