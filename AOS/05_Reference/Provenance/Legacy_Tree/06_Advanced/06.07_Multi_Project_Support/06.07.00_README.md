# 06.07.00 Multi-Project Support

## Назначение документа

Multi-Project Support рассматривается после доказанной устойчивости AOS в одном проекте.

Поддержка нескольких проектов не должна усложнять первый Product Runtime.

## Entry Conditions

До multi-project capability желательно иметь:

- working single-project Product Runtime;
- несколько завершённых workflows;
- стабильную project identity;
- ясные Source of Truth rules;
- isolated project state;
- predictable handoff;
- подтверждённые use cases для переключения или агрегации проектов.

## Isolation

Каждый проект должен иметь независимые:

- repository identity;
- project root;
- branch;
- baseline;
- contracts;
- permissions;
- secrets;
- temporary workspace;
- reports;
- human decisions.

State одного проекта не должен становиться authority другого.

## Cross-Project Knowledge

Разрешено разделять:

- generic templates;
- validated patterns;
- provider adapters;
- reusable tools;
- public schemas.

Не разрешено автоматически разделять:

- approvals;
- Risk Profiles;
- execution packages;
- secrets;
- baselines;
- project-specific decisions;
- protected state.

## Pattern Libraries

Reusable pattern не является default solution.

Перед применением проверяются:

- problem fit;
- contract compatibility;
- dependency compatibility;
- license;
- security;
- version;
- local constraints.

## Aggregated Views

Cross-project dashboard или index является derived view.

Он не заменяет project-local canonical sources.

## Routing

Routing между проектами должен требовать exact project identity.

Ambiguous project target приводит к stop до write operation.

## Multi-Repository Change

Change, затрагивающий несколько repositories, должен быть разбит на:

- отдельные baselines;
- отдельные scopes;
- отдельные validations;
- coordinated human decision.

Одна authorization не распространяется автоматически на все repositories.

## Legacy Lesson

Сложная multi-repository factory не должна появляться раньше работающего single-project workflow и подтверждённой необходимости.
