# Decision Model

## Назначение документа

Decision Model разделяет факты, recommendations, technical results и human decisions.

## Legacy Reference Boundary

Global legacy authority and extraction rules are canonical in [`Project Principles`](../00_Core/Project_Principles.md#legacy-reference-boundary).

For this topic, legacy material may inform analysis, but it does not define active rules, architecture, lifecycle, authority, or readiness.


## Human Authority

Human decision cannot be simulated.

Агент может подготовить:

- analysis;
- Evidence;
- recommendation;
- decision package;
- proposed Risk Profile.

Агент не может:

- назначить Risk Profile;
- принять architecture;
- выдать approval;
- разрешить protected change;
- разрешить destructive operation;
- выдать execution, Commit, Push, Merge или Release authorization.

## Technical Result

Technical result описывает состояние проверки:

- PASS;
- FAIL;
- UNKNOWN;
- NOT_RUN;
- BLOCKED.

Он не означает acceptance.

```text
technical result: PASS
human decision: NOT_RECORDED
```

является допустимым состоянием.

## Recommendation

Recommendation — совет, а не решение.

Она должна:

- опираться на facts;
- показывать risks;
- сохранять unknowns;
- предлагать одно следующее действие;
- не использовать язык fake approval.

## Decision Classes

### Scope Decision

Принимает, сокращает, расширяет или прекращает Scope.

### Risk Decision

Назначает Risk Profile.

### Architecture Decision

Определяет architecture, Source of Truth, dependencies или boundaries.

### Execution Decision

Разрешает конкретную bounded Task.

### Review Decision

Использует варианты:

- ACCEPT;
- REJECT;
- NEEDS_REVISION.

### Git Decision

Отдельно рассматривает:

- Commit;
- Push;
- Merge;
- Release.

### Lifecycle Decision

Изменяет durable lifecycle state, если lifecycle действительно используется.

## Approval Boundary

Следующее не является approval:

- PASS;
- Evidence;
- CI success;
- readiness report;
- checklist;
- generated package;
- отсутствие возражений;
- plan;
- Task Brief;
- routing decision;
- legacy approval.

## Risk Profile

Agent может предложить профиль и rationale.

До human assignment:

```text
Risk Profile: UNASSIGNED
```

Если профиль обязателен, дальнейшая работа получает `HUMAN_REVIEW_REQUIRED` или `BLOCKED`.

## Protected and Destructive Decisions

Protected/canonical changes и destructive operations требуют explicit human checkpoint.

Решение связывается с:

- task;
- Scope;
- target;
- baseline;
- known consequences.

## Decision Record

Durable decision фиксирует:

- что решено;
- кем;
- к какому объекту;
- при каких условиях;
- ограничения;
- superseded relationship;
- применимый repository state.

Chat memory не является достаточным durable record для значимого решения.

## Changed Conditions

Решение требует повторной оценки, если изменились:

- baseline;
- Scope;
- candidate;
- risk;
- architecture;
- dependencies;
- protected boundary.

## No Implied Continuation

```text
Plan complete ≠ execution authorized
Execution complete ≠ Validation PASS
Validation PASS ≠ accepted
Accepted ≠ Commit authorized
Commit authorized ≠ Push authorized
Push authorized ≠ Merge authorized
Merge authorized ≠ Release authorized
```

## Критерий качественной Decision Model

Модель полезна, если:

- authority видима;
- отсутствующее решение не симулируется;
- legacy approvals не переносятся;
- каждое действие имеет собственную boundary;
- человек получает краткий decision package и одно следующее действие.
