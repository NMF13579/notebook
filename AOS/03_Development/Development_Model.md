# Development Model

## Назначение документа

Development Model определяет общую операционную модель разработки нового AOS.

Раздел отвечает на вопрос:

> Как создавать AOS последовательно, воспроизводимо и безопасно, не превращая сам процесс разработки в более сложный продукт, чем AOS?

Development существует ради создания и улучшения Product Runtime. Development Factory, Governance, automation и Runtime Enforcement являются вспомогательными уровнями зрелости, а не prerequisites первого полезного продукта.

## Legacy Reference Boundary

Global legacy authority and extraction rules are canonical in [`Project Principles`](../00_Core/Project_Principles.md#legacy-reference-boundary).

For this topic, legacy material may inform analysis, but it does not define active rules, architecture, lifecycle, authority, or readiness.


## Место Development в структуре AOS

Active documentation route образует последовательность:

```text
00_Core
→ 01_Product
→ 02_Architecture
→ 03_Development
```

`00_Core` определяет identity, principles и minimum safety boundaries.

`01_Product` определяет пользователя, outcome, contracts, journeys и acceptance.

`02_Architecture` задаёт минимальные structural foundations.

`03_Development` описывает, как продукт создаётся, изменяется и проверяется.

`04_Lessons` поддерживает active работу принятыми lessons и anti-patterns, но не заменяет canonical contracts соседних разделов.

`05_Reference` хранит non-authoritative reference и deferred Control, Advanced, Research, References и Archive materials. Их наличие не создаёт active architecture, lifecycle или execution authority.

Эта topology описывает расположение canonical документации, а не product evolution roadmap. Maturity sequence по-прежнему может развиваться от product contracts и первого vertical slice через manual development cycles к доказанно необходимым control и automation capabilities, но deferred capabilities не становятся active разделами документации автоматически.

## Основная проблема

Предыдущая разработка показала системный риск: процесс разработки может начать развиваться быстрее продукта.

Типичный цикл выглядел так:

```text
нужно создать product capability
→ сначала строится supporting process
→ процесс требует Governance
→ Governance требует Evidence и approval infrastructure
→ infrastructure требует recovery и validation
→ product capability не создаётся
```

Development Model должна разрывать этот цикл.

## Главный принцип

> Разработка существует ради пользовательской ценности.

Любой новый процесс, artifact, dependency или tool должен отвечать на вопросы:

1. Какую наблюдаемую проблему он решает?
2. Почему текущего более простого подхода недостаточно?
3. Какова минимальная реализация?
4. Как будет проверяться польза?
5. Как механизм можно удалить или заменить?

Если убедительного ответа нет, механизм не добавляется.

## Product First

Первым объектом развития остаётся Product Runtime.

Предпочтительная последовательность:

```text
Product intent
→ Product Contracts
→ first vertical slice
→ manual product cycles
→ product core expansion
→ Project Memory
→ Development Factory
→ progressive Control
→ controlled automation
→ Runtime Enforcement
```

Development Factory не должна блокировать первый Product Runtime vertical slice.

## Manual Before Automation

Новая операция сначала выполняется вручную.

Автоматизация рассматривается после нескольких успешных и сходных cycles:

```text
manual
→ repeatable
→ documented
→ assisted
→ controlled automation
→ enforcement where justified
```

Автоматизация нестабильного процесса закрепляет неопределённость и увеличивает recovery cost.

## Bounded Development

Любая работа выполняется как bounded task.

Задача должна иметь:

- одну основную цель;
- ожидаемый результат;
- allowed scope;
- forbidden scope;
- исходный baseline;
- validation expectations;
- stop conditions;
- разрешённые действия.

Scope не расширяется автоматически. Новый finding становится follow-up candidate, а не скрытым продолжением текущей задачи.

## Separation of Stages

Planning, Execution, Validation и Review являются отдельными stages.

```text
Planning
≠ Execution
≠ Validation
≠ Review
```

Каждый stage имеет:

- собственную роль;
- входные данные;
- разрешённые действия;
- output;
- stop condition.

Один запуск выполняет один stage.

После завершения формируется report, указывается одно следующее действие и работа останавливается.

## Human Authority

Human authority сохраняется на всех уровнях.

Агент может:

- анализировать;
- предложить Risk Profile;
- подготовить plan;
- выполнить разрешённое изменение;
- провести read-only Validation;
- подготовить recommendation.

Агент не может:

- назначить Risk Profile;
- расширить Scope;
- симулировать approval;
- принять architecture decision;
- разрешить protected или destructive operation;
- выдать execution authorization;
- выдать Commit, Push, Merge или Release authorization.

## Technical Result and Human Decision

Технический результат и человеческое решение хранятся раздельно.

```text
PASS ≠ approval
Evidence ≠ approval
CI PASS ≠ approval
```

Возможное состояние:

```text
technical result: PASS
human decision: NOT_RECORDED
```

является нормальным и не разрешает дальнейшее действие.

## Unknown Handling

Неизвестность отображается явно.

```text
UNKNOWN ≠ OK
NOT_RUN ≠ PASS
```

Fail-closed применяется только внутри затронутой boundary. Неопределённость в одном механизме не должна необоснованно блокировать весь проект, но рискованное действие внутри этой boundary не продолжается.

## Terminal Workflow

Каждый stage должен иметь terminal result.

На blocking finding:

```text
finding
→ report
→ one next action
→ stop
```

Automatic repair, automatic retry и automatic transition запрещены.

Correction оформляется отдельной bounded task.

## Minimal Complexity

Development Model предпочитает:

- простые файлы сложному registry;
- ясный contract сложному framework;
- local-first checks тяжёлому CI;
- manual checkpoint premature enforcement;
- replaceable internals tool lock-in;
- restart бесконечной recovery, когда restart безопаснее.

## Что не входит в документ

Документ не определяет:

- product features;
- implementation architecture;
- конкретный programming language;
- обязательный orchestration framework;
- полный Governance;
- Runtime Enforcement;
- active approval records;
- текущий lifecycle;
- implementation authorization.

Они рассматриваются в соответствующих документах и только в момент подтверждённой необходимости.

## Критерий качества Development Model

Модель полезна, если она:

- ускоряет путь к product outcome;
- делает Scope понятным;
- создаёт terminal states;
- сохраняет human authority;
- не скрывает unknowns;
- снижает recovery frequency;
- не переносит legacy complexity;
- допускает постепенное усложнение только по Evidence.
