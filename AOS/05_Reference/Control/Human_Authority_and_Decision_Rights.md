# Human Authority and Decision Rights

## Основной принцип

Человек остаётся владельцем проекта и финальным источником authority для решений, меняющих scope, риск, protected state или внешнее состояние.

```text
capability ≠ authority
access ≠ permission
successful command ≠ authorized action
```

## Агент может

- анализировать;
- предлагать scope, decomposition и validation;
- предложить Risk Profile;
- выполнить явно разрешённую bounded task;
- сообщить findings и unknowns;
- указать одно следующее действие.

## Агент не может

- назначать себе authority;
- симулировать human approval;
- считать молчание согласием;
- выводить approval из PASS;
- назначать Risk Profile вместо человека;
- расширять scope;
- авторизовать destructive operation;
- автоматически запускать следующий этап;
- трактовать documentation как execution permission.

## Human-only decisions

Явного human decision требуют:

- принятие или изменение Product scope;
- назначение Risk Profile, если он применяется;
- protected/canonical changes;
- destructive operations;
- принятие residual risk;
- execution после отдельного planning stage;
- commit;
- push;
- merge;
- release;
- product acceptance;
- изменение authority или lifecycle boundary.

## Делегированное исполнение

Bounded execution может быть делегировано заранее, если определены цель, expected result, allowed и forbidden scope, workspace, validation, stop conditions и разрешённые side effects.

Делегирование не переносится автоматически на соседние файлы, новую branch, новый baseline, dependencies, network, protected changes или Git actions.

## Отсутствующая authority

Если обязательное human decision отсутствует, действие не выполняется. Результат ограничивается:

```text
HUMAN_REVIEW_REQUIRED
```

или:

```text
BLOCKED
```

Агент не заменяет отсутствие authority догадкой.

## Human checkpoint

Checkpoint должен быть связан с одним конкретным решением. Acceptance, commit, push, merge и release не объединяются в одно разрешение.

Human authority не означает approval на каждую мелкую обратимую операцию. Контроль концентрируется на meaningful decisions, а безопасная работа внутри принятой bounded task не должна превращаться в бесконечную очередь approvals.
