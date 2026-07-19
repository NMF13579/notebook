# Recovery Model

## Назначение документа

Recovery Model определяет ограниченное восстановление прерванной или неопределённой разработки нового AOS.

Recovery является временным режимом и должна возвращать проект в normal workflow.

## Legacy Reference Boundary

Global legacy authority and extraction rules are canonical in [`Project Principles`](../00_Core/Project_Principles.md#legacy-reference-boundary).

For this topic, legacy material may inform analysis, but it does not define active rules, architecture, lifecycle, authority, or readiness.


## Recovery Goal

Recovery восстанавливает только факты, необходимые для одного решения:

- безопасно resume;
- создать новую Task;
- зафиксировать BLOCKED;
- выполнить restart;
- abandon устаревшую работу.

Она не обязана реконструировать всю историю старого проекта.

## Recovery Trigger

Recovery начинается с конкретного вопроса:

- какой candidate создан;
- завершён ли stage;
- каков baseline;
- кому принадлежат uncommitted changes;
- применим ли Task Brief;
- произошло ли external action.

Широкое «восстановление всего» без bounded result не допускается.

## Read-Only First

Сначала исследуются:

- repository state;
- branch;
- HEAD;
- working tree;
- Git history;
- durable reports;
- decision records;
- external state, если доступ разрешён.

Write и destructive operations не используются для исследования.

## Fact Hierarchy

Предпочтение отдаётся:

1. фактическому состоянию нового repository;
2. Git identity и tracked artifacts;
3. durable reports нового проекта;
4. handoff;
5. chat summaries;
6. legacy reference.

Нижний уровень не переопределяет верхний без Evidence.

## Unknown Handling

Невосстановимый факт остаётся UNKNOWN.

Если безопасное продолжение невозможно:

```text
UNKNOWN_BLOCKED
```

является terminal result.

## No Recursive Recovery

Запрещён цикл:

```text
recovery
→ recovery plan
→ recovery validation
→ recovery of recovery
```

Recovery имеет bounded attempts и terminal report.

## Dirty Working Tree

Changes классифицируются как:

- current Task;
- unrelated;
- generated;
- temporary;
- unknown origin.

Recovery не выполняет delete, reset, clean или rewrite без explicit human authorization.

## External Actions

Перед повторением Push, Merge, Release, deployment или отправки сообщения сначала проверяется фактический remote result.

Локальная потеря ответа не означает, что действие не произошло.

## No Automatic Repair

```text
recover facts
→ Recovery Report
→ human decision
→ separate correction Task
```

Recovery не исправляет найденную проблему в том же stage.

## Terminal Outcomes

- RECOVERED;
- PARTIALLY_RECOVERED;
- BLOCKED;
- UNKNOWN_BLOCKED;
- RESTART_RECOMMENDED;
- ABANDON_RECOMMENDED.

Recommendation не является authorization.

## Restart

Restart предпочтителен, если:

- contracts изменились;
- candidate невозможно достоверно восстановить;
- recovery cost выше reimplementation;
- legacy state слишком связан с устаревшей architecture;
- новый bounded implementation безопаснее.

Старая работа сохраняется как reference, но не импортируется как active state.

## Критерий качественной Recovery

Recovery:

- короткая;
- read-only first;
- ограничена вопросом;
- не создаёт новую permanent infrastructure;
- не переносит legacy lifecycle;
- возвращает к normal workflow или честно останавливается.
