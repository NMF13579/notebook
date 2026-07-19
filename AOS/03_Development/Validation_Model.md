# Validation Model

## Назначение документа

Validation Model определяет независимую проверку результата Task.

Validation отвечает на вопрос:

> Соответствует ли фактический candidate заранее определённым требованиям?

## Legacy Reference Boundary

Global legacy authority and extraction rules are canonical in [`Project Principles`](../00_Core/Project_Principles.md#legacy-reference-boundary).

For this topic, legacy material may inform analysis, but it does not define active rules, architecture, lifecycle, authority, or readiness.


## Independent Read-Only Stage

Validation выполняется отдельно от Execution.

Она:

- read-only;
- проверяет конкретный candidate;
- использует заранее определённый validation contract;
- не исправляет artifact;
- не начинает следующий stage.

## Validation Contract

До запуска известны:

- объект проверки;
- expected result;
- requirements;
- candidate identity;
- required checks;
- advisory checks;
- stop conditions;
- допустимые result states.

Отсутствие обязательного validation contract исключает PASS.

## Result States

### PASS

Все required checks выполнены и подтверждают expected result.

### FAIL

Хотя бы один required check показал несоответствие.

### UNKNOWN

Данных недостаточно для достоверного вывода.

### NOT_RUN

Проверка не запускалась.

### BLOCKED

Известное препятствие не позволяет выполнить проверку.

### UNKNOWN_BLOCKED

Состояние недостаточно известно, а безопасное продолжение невозможно.

## Fundamental Invariants

```text
PASS ≠ approval
Evidence ≠ approval
CI PASS ≠ approval
UNKNOWN ≠ OK
NOT_RUN ≠ PASS
```

## Candidate Binding

Validation должна доказать, что проверяет правильный candidate.

Могут фиксироваться:

- repository;
- branch;
- baseline;
- commit;
- tree ID;
- file digest;
- package digest;
- configuration.

Изменение candidate аннулирует применимость предыдущего результата в изменённой boundary.

## False PASS Protection

False PASS возможен, если:

- запущено 0 tests;
- проверена другая branch;
- CI относится к другому commit;
- skipped checks скрыты;
- required check заменён advisory check;
- проверена только документация при claims об implementation;
- manual check заменён предположением.

Validation должна явно показывать такие случаи.

## Evidence

Evidence связывается с:

- candidate;
- конкретной проверкой;
- фактическим output;
- exit code;
- временем или state.

Evidence поддерживает conclusion, но не создаёт approval.

## Documentation Validation

Для documentation Task могут проверяться:

- target path;
- document numbering;
- Markdown structure;
- headings;
- code fences;
- links;
- отсутствие YAML metadata, если оно запрещено;
- отсутствие Status и approval claims;
- target-only diff;
- `git diff --check`;
- отсутствие temporary files.

Корректный Markdown не доказывает implementation readiness.

## Implementation Validation

В зависимости от contracts используются:

- unit tests;
- integration tests;
- acceptance tests;
- negative tests;
- regression tests;
- lint;
- typing;
- build;
- dependency checks;
- security checks;
- manual observable behavior checks.

## CI Boundary

CI является исполнителем checks, а не human authority.

CI PASS не означает автоматически:

- acceptance;
- merge readiness;
- merge authorization;
- release authorization;
- отсутствие unknowns вне CI Scope.

## Failure Behavior

На blocking finding:

```text
finding
→ sufficient Evidence
→ Validation Report
→ one next action
→ stop
```

Validation не исправляет candidate и не повторяется автоматически.

## Retry Boundary

Повторная Validation требует изменившегося основания:

- новый candidate;
- исправленная environment;
- уточнённый contract;
- отдельное human decision.

Повтор без изменения условий не является прогрессом.

## Validation Report

Report содержит:

- task;
- candidate identity;
- Scope;
- required checks;
- executed checks;
- results;
- Evidence;
- findings;
- unknowns;
- NOT_RUN checks;
- technical result;
- одно следующее действие.

## Критерий качественной Validation

Validation:

- проверяет правильный candidate;
- не меняет его;
- не скрывает пропуски;
- не импортирует legacy claims;
- различает technical result и human decision;
- заканчивается terminal report.
