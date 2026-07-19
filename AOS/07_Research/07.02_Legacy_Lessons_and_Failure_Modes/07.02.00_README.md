# 07.02 — Legacy Lessons and Failure Modes

## Назначение

Документ систематизирует полезный опыт и failure modes старого AOS-FARM, чтобы новый проект не повторил прежнюю сложность и контрольные ошибки.

Это не аудит для продолжения старой реализации и не список обязательных компонентов нового AOS.

## Главный системный урок

Наиболее существенная ошибка состояла не в отдельном модуле, а в порядке развития:

```text
Development Factory
+ Governance
+ Control Plane
+ recovery machinery
+ automation
строились раньше подтверждённого Product Runtime value
```

В результате formal readiness и обслуживание control machinery могли вытеснять product progress.

## Failure mode: Control Plane before product value

### Наблюдение

Контрольная система становилась prerequisite разработки самой себя и продукта.

### Последствие

Возникала циклическая зависимость:

```text
Control Plane нужен для разработки
→ Control Plane не готов
→ его разработка требует новых controls и approvals
→ продукт откладывается
```

### Reconstruction rule

Первый полезный Product Runtime vertical slice не должен зависеть от полного Control Plane, registry или Runtime Enforcement.

Минимальный safety floor обязателен, но progressive Governance добавляется после появления доказанной необходимости.

## Failure mode: automation before manual validation

Автоматизация процесса до нескольких успешных manual cycles закрепляет неизвестные ошибки и преждевременные assumptions.

Правило:

```text
manual workflow
→ repeated successful cycles
→ stable repeated burden
→ bounded automation candidate
```

## Failure mode: formal completion replacing user outcome

Большое количество plans, gates, Evidence packages и readiness labels может создать ощущение прогресса без полезного пользовательского результата.

Каждая стадия должна отвечать:

- какой observable user outcome появился;
- что пользователь теперь может сделать;
- какое утверждение проверено;
- что по-прежнему не реализовано.

## Failure mode: claims crossing authority boundaries

Опасные подмены:

```text
PASS → approval
Evidence → approval
CI PASS → approval
plan → execution authorization
routing → execution authorization
technical closure → human acceptance
```

Все такие преобразования запрещены без отдельного explicit human decision.

## Failure mode: mixed stages

Смешение planning, execution, validation и review снижает независимость проверки и создаёт скрытую мутацию scope.

Правило нового проекта:

```text
один запуск = один этап
validation не исправляет
review read-only
finding → report → stop
```

## Failure mode: recovery without terminal stop

Recovery loops могут бесконечно порождать новые repair tasks.

Новый механизм recovery должен иметь:

- bounded attempts;
- terminal conditions;
- один `next_required_action`;
- запрет автоматического запуска следующего этапа;
- explicit human decision при повторяющемся blocker.

## Failure mode: excessive decomposition

Слишком мелкая декомпозиция увеличивает coordination cost, объём Evidence и вероятность потери исходного outcome.

Используется кратчайший безопасный путь:

- минимальный достаточный scope;
- отдельный этап только для реальной boundary;
- отсутствие artificial milestones;
- отсутствие decomposition ради формальной управляемости.

## Failure mode: topology as identity

Копирование старых каталогов, классов, registries и pipelines может ошибочно представить историческую topology как сущность продукта.

Новый проект должен реконструировать:

1. user problem;
2. observable behavior;
3. Product Contract;
4. минимальную implementation boundary.

Legacy topology рассматривается только как один из alternatives.

## Failure mode: Source of Truth fragmentation

Один факт, записанный в нескольких Markdown, YAML, registries, databases и reports, приводит к drift.

Правило:

```text
one Source of Truth per fact class
```

Derived indexes, caches и dashboards не получают authority.

## Failure mode: hidden scope expansion

Исполнитель не должен включать «полезные сопутствующие улучшения», которые не входят в Task Brief.

Неожиданная необходимость расширения scope приводит к report и stop.

## Failure mode: premature dependencies

Database, RAG, orchestration frameworks, containers или external services не вводятся только потому, что они использовались или обсуждались ранее.

Dependency принимается, только если:

- решает подтверждённую проблему;
- проще локальной alternative;
- имеет понятную ownership boundary;
- может быть заменена;
- имеет validation strategy.

## Полезные элементы, которые можно сохранить как candidates

Не как готовые реализации, а как проверяемые идеи:

- bounded Task Brief;
- explicit allowed и forbidden scope;
- one writer;
- independent validation;
- session handoff;
- one next action;
- explicit Git boundaries;
- human authority;
- structured status semantics;
- deterministic reports;
- fail-closed внутри затронутой boundary;
- read-only audit roles.

## Итоговое reconstruction правило

```text
сохранить intent и lessons
→ удалить историческую authority
→ упростить mechanism
→ проверить behavior заново
→ принять новым human decision
```
