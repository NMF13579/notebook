# 07.06 — Model Routing and Task Decomposition

## Назначение

Документ перерабатывает исследования model routing, role separation и task decomposition в безопасные candidates для нового проекта.

Routing оптимизирует способ выполнения разрешённой работы. Он не создаёт authorization.

## Основной инвариант

```text
Routing decision ≠ execution authorization.
Model capability ≠ authority.
Higher reasoning ≠ permission.
Tool availability ≠ permission.
```

## Routing dimensions

Routing candidate может учитывать:

- task class;
- planning requirement;
- role;
- reasoning level;
- sandbox;
- network access;
- expected context size;
- validation independence;
- write permissions.

Risk Profile не назначается моделью автоматически. Агент может только предложить профиль для human decision.

## Role classes

### Planner

Read-only. Формирует `DRAFT`, boundaries, unknowns и next required action.

### Executor

Работает только по executable Task Brief в разрешённом scope.

### Validator

Read-only относительно проверяемого artifact. Не исправляет findings.

### Reviewer

Read-only. Оценивает результат и сообщает findings без изменения artifact.

### Researcher

Read-only. Извлекает facts, alternatives и lessons. Не меняет active architecture или roadmap.

## Decomposition principles

- декомпозиция должна защищать реальную boundary;
- каждый unit должен иметь independently observable result;
- unit не должен быть меньше, чем требуется для meaningful validation;
- новый этап не создаётся только ради отдельного отчёта;
- scope не расширяется при декомпозиции;
- parent outcome должен сохраняться;
- после failure работа останавливается.

## Lazy decomposition

Подробная декомпозиция выполняется только настолько, насколько требуется для следующего безопасного этапа.

Это снижает риск планирования далёких шагов на ложных assumptions.

## Anti-patterns

- routing по prestige модели;
- automatic downgrade без permission;
- sandbox expansion ради удобства;
- включение network без explicit need;
- parallel write agents;
- planner, который начинает execution;
- validator, который исправляет код;
- retry loops без stop condition;
- decomposition, скрывающая scope expansion;
- provider-specific behavior, выданное за product contract.

## Required routing record

Для сложной задачи рекомендуется фиксировать:

```text
task_class:
planning_required:
reason:
role:
reasoning:
sandbox:
network_access:
proposed_Risk_Profile:
assigned_Risk_Profile:
Task_Brief_status:
execution_authorized:
next_required_action:
```

## Validation candidates

Routing mechanism должен проверяться на:

- correctness of role selection;
- permission preservation;
- configuration mismatch;
- unavailable model behavior;
- scope preservation;
- no hidden execution;
- deterministic fallback to `BLOCKED` или `HUMAN_REVIEW_REQUIRED`.

## Promotion boundary

Advisory routing может быть введён раньше runtime routing.

Автоматический runtime router допускается только после успешного pilot, negative tests и explicit human decision.
