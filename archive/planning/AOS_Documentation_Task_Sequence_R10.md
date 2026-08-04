# AOS — компактный план документационной работы R10

| Поле | Значение |
|---|---|
| Revision | `R10` |
| Status | `DRAFT_FOR_HUMAN_REVIEW` |
| Role | Рабочая последовательность документационных результатов |
| Authority | `PROPOSAL` |
| Implementation authorization | `NONE` |
| Git authorization | `NONE` |

## 1. Цель

R10 помогает человеку и агенту быстро понять:

1. какой результат нужен следующим;
2. какие источники для него релевантны;
3. что разрешено и запрещено менять;
4. по каким признакам работа закончена;
5. когда нужно остановиться и запросить решение.

Документация должна помогать последующей реализации продукта. Само создание
документации не является implementation и не должно порождать отдельную
lifecycle-систему без доказанной необходимости.

## 2. Владение фактами и статусом

R10 не создаёт новых fact owners и не копирует их содержание:

- `docs/00_Core.md`–`docs/06_Features.md` владеют принятой базой знаний;
- `docs/03_Development.md` владеет нормативным workflow;
- `planning/CURRENT.md` остаётся единственным владельцем текущего состояния и
  следующего активного действия;
- R10 определяет только понятную последовательность результатов.

Перед работой агент читает `docs/00_Core.md`, затем только релевантный owner.
`planning/CURRENT.md` читается, когда задача зависит от текущего состояния,
принятого решения или предыдущего результата.

Прямое текущее решение человека имеет приоритет над устаревшей записью.
Существенное расхождение не исправляется молча: агент сообщает его и
останавливается.

## 3. Обычная документационная задача

Default route:

```text
Short Markdown Task
→ bounded edit
→ focused checks
→ concise report
→ stop
```

Short Markdown Task содержит только:

1. **Цель** — какой понятный результат нужен.
2. **Контекст** — релевантные owners, решения и ограничения.
3. **Сделать** — точный предмет и ожидаемое изменение.
4. **Не делать** — границы и запрещённое расширение scope.
5. **Готово, когда** — наблюдаемые критерии завершения.
6. **Проверки** — только проверки, пропорциональные изменению.

Для обычной обратимой правки не требуются отдельные YAML task blocks, stage
reports, acceptance/activation records, manifests, hashes, lifecycle diagrams
или отдельный документ для каждой стадии.

Task Brief или план не разрешает implementation, Commit, Push, Merge или
Release. Эти действия требуют отдельного прямого решения человека.

## 4. Формат понятного рабочего плана

Если задача требует нескольких связанных шагов, агент создаёт один план по
этому шаблону:

```markdown
# <Короткое название результата>

## Цель
<Что должно стать истинным после работы.>

## Контекст
- <релевантный owner или исходный документ>
- <принятое решение или существенное ограничение>

## Сделать
1. <первый необходимый шаг>
2. <следующий зависимый шаг>

## Не делать
- <явная граница scope>
- <неразрешённые implementation или Git actions>

## Готово, когда
- <наблюдаемый критерий результата>
- <наблюдаемый критерий качества>

## Проверки
- <focused check>
- `git diff --check`, если доступен Git checkout
```

Правила для такого плана:

- один plan обслуживает один outcome;
- шаг добавляется только при реальной зависимости;
- точные paths указываются до edit;
- product facts не копируются из canonical owner;
- неизвестное записывается как `UNKNOWN`, а не заполняется догадкой;
- новый material decision или scope expansion возвращается человеку;
- progress не хранится в плане параллельно `planning/CURRENT.md`.

## 5. Последовательность результатов

R10 использует outcomes вместо множества lifecycle-артефактов. Точный текущий
пункт определяется по `planning/CURRENT.md` и последнему прямому решению
человека.

### R10-01 — Завершить документацию первого vertical slice

**Результат:** один компактный и непротиворечивый Product Contract или
implementation brief для выбранного первого slice.

Он должен содержать actor, trigger, inputs/outputs, main flow, состояния,
failures/recovery, constraints, acceptance, negative cases и material unknowns.
Существующий принятый contract сохраняется; successor создаётся только для
конкретного изменения, которое нельзя корректно внести в canonical owner.

**Готово, когда:** человек и cold-start agent одинаково понимают поведение,
границы и оставшиеся решения, не обращаясь к chat history.

**Остановиться, если:** не выбран exact slice, конфликтуют human decisions или
нужно назначить implementation repository, stack либо dependency.

### GATE-01 — Решение о target implementation repository

Это решение человека, а не документационная задача. До него разрешены анализ,
decision-ready proposal и target-unbound brief. Runtime implementation,
scaffolding, dependencies, CI/CD и deployment здесь не создаются.

### R10-02 — Подготовить target-bound implementation handoff

**Результат:** короткий handoff, который связывает принятый contract с exact
target repository, путями, ограничениями, acceptance criteria и проверками.

Handoff не дублирует Product Contract и не выдаёт Execution Authorization. Если
target ещё не назначен или не проверен, результат остаётся target-unbound и это
указывается явно.

**Готово, когда:** будущий implementer понимает, что создавать, где создавать,
что не менять и как доказать результат.

### GATE-02 — Реализация и реальная Evidence

Implementation выполняется только в отдельно выбранном repository и по
отдельной авторизации. После реализации нужны наблюдаемые Evidence, human review
и решение. `PASS` проверки не заменяет human acceptance.

### R10-03 — Скорректировать knowledge baseline по Evidence

**Результат:** только подтверждённые product facts, architecture decisions,
lessons или regression cases внесены в соответствующие canonical owners.

Не переносить runtime topology или случайные implementation details в target
architecture автоматически.

**Готово, когда:** каждое изменение имеет понятный provenance, owner и влияние
на будущую работу; неподтверждённые выводы остаются proposal или `UNKNOWN`.

### R10-04 — Описать полный manual development route

Этот результат нужен только после успешного первого slice или при явной
необходимости подготовить следующий bounded implementation cycle.

**Результат:** один читаемый маршрут от problem/intent до implementation
handoff, validation, human decision, recovery и отдельно разрешённых Git
actions. Он ссылается на существующие contracts вместо их копирования.

**Готово, когда:** маршрут можно проверить вручную на реальной задаче без
скрытой automation и без неоднозначной authority.

### R10-05 — Документировать одну оправданную automation capability

Automation рассматривается только после повторяемой manual practice с
известными failure modes, fallback и измеримой пользой.

**Результат:** contract одной bounded capability. Один документ не должен
одновременно проектировать runner, coordinator, plugin system, UI и release
pipeline.

**Остановиться, если:** нет минимум двух наблюдаемых повторений, стабильного
contract или отдельного human decision о необходимости automation.

### R10-06 — Рассматривать extensions по измеренной потребности

Extension package создаётся только для одного exact use case после отдельного
product decision. Core должен работать без extensions.

Medical, Design, SaaS, marketplace, RAG и broad multi-agent orchestration не
объединяются в один общий roadmap item и не включаются в critical path без
явного решения человека.

## 6. Когда нужен formal process

Расширенный процесс используется только когда присутствует хотя бы одно:

- material product, architecture или authority decision;
- high-risk, protected, destructive или sensitive operation;
- independent validation, требуемая задачей или риском;
- exact immutable candidate или внешний Evidence package;
- изменение security boundary, repository role или implementation target.

Даже в formal process не создаются артефакты «на всякий случай». Каждый
дополнительный plan, record, manifest или report должен иметь конкретного
consumer и отвечать на вопрос, который нельзя надёжно закрыть коротким планом и
отчётом.

## 7. Проверки документации

Для обычной Markdown-правки достаточно:

1. проверить соответствие goal, paths и scope;
2. проверить затронутые Markdown fences и relative links;
3. выполнить `git diff --check`;
4. убедиться, что не появились новые authority claims;
5. перечислить фактически выполненные checks и существенные `NOT_RUN`.

Package-wide проверки выполняются только при изменении package-wide предмета.
Validation остаётся read-only и не исправляет проверяемый subject.

## 8. Краткий отчёт

После обычной задачи агент сообщает:

1. что сделано;
2. какие paths изменены;
3. какие checks выполнены;
4. что осталось `NOT_RUN`, `UNKNOWN` или вне scope.

После completion, finding или failure агент останавливается. Следующая
документационная задача, implementation или Git action не запускается
автоматически.

## 9. Связь с R9

`planning/AOS_Documentation_Task_Sequence_R9.md` остаётся неизменным
историческим predecessor с собственной byte/hash identity.

R10 не переписывает историю R9, не обновляет `planning/CURRENT.md` и не меняет
существующие acceptance/activation records. После явного human acceptance R10
может стать рабочим roadmap отдельным bounded изменением `planning/CURRENT.md`.
Для самого принятия достаточно прямого решения человека; отдельный acceptance
record создаётся только по явному запросу или material risk.

## 10. Следующее решение

Человек выбирает одно:

- `ACCEPT` — использовать R10 как новый рабочий roadmap;
- `NEEDS_CHANGES` — указать exact изменения;
- `REJECT` — сохранить R9 без замены.

До этого решения R10 остаётся `DRAFT_FOR_HUMAN_REVIEW`. Commit, Push, Merge,
Release, implementation и изменение `planning/CURRENT.md` — `NOT_RUN`.
