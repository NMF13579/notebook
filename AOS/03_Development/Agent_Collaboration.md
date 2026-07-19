# Agent Collaboration

## Назначение документа

Agent Collaboration определяет разделение agent roles при разработке нового AOS.

Несколько agents не образуют автономную authority.

## Legacy Reference Boundary

Global legacy authority and extraction rules are canonical in [`Project Principles`](../00_Core/Project_Principles.md#legacy-reference-boundary).

For this topic, legacy material may inform analysis, but it does not define active rules, architecture, lifecycle, authority, or readiness.


## Roles

### Planning Role

Read-only анализирует Scope, dependencies, risks и execution path.

Output — DRAFT и `HUMAN_REVIEW_REQUIRED`.

### Execution Role

Создаёт bounded candidate по Task Brief и authorization.

### Validation Role

Read-only проверяет candidate и не исправляет findings.

### Review Role

Read-only интерпретирует facts и готовит recommendation.

### Research Role

Извлекает alternatives, lessons и reference material, не меняя active architecture.

### Routing Role

Предлагает workflow, role, reasoning и permissions.

Routing decision не назначает Risk Profile и не разрешает Execution.

## Human Role

Человек:

- принимает Scope;
- назначает Risk Profile;
- принимает architecture;
- разрешает protected и destructive actions;
- принимает или отклоняет результат;
- отдельно разрешает Git actions.

## One Session — One Stage

Planning, Execution, Validation и Review разделяются.

После stage:

- report;
- one next action;
- stop.

## Single Writer

Одна bounded Task имеет одного writer.

Parallel write agents запрещены.

Parallel read-only work допустим для независимых вопросов с единым synthesis.

## Handoff Contract

Handoff включает:

- task;
- stage;
- Scope;
- repository;
- branch;
- baseline/candidate;
- inputs;
- performed work;
- findings;
- unknowns;
- permissions;
- one next action.

Следующая role проверяет фактическое состояние.

## Role Purity

Planning не пишет implementation.

Execution не пересматривает Scope.

Validation не исправляет candidate.

Review не выдаёт human approval.

Research не импортирует legacy decisions.

Routing не выдаёт execution authorization.

## Configuration Verification

Проверяются:

- model;
- reasoning;
- sandbox;
- network;
- repository access;
- role instructions.

Configuration mismatch означает BLOCKED.

Automatic downgrade и permission expansion запрещены.

## Network

Network включается только при необходимости.

Research access не разрешает:

- dependency installation;
- executable download;
- remote mutation;
- secrets use;
- data publication.

## Disagreement

При разногласии agents фиксируются:

- common facts;
- competing interpretations;
- Evidence;
- unknowns;
- decision required from human.

Ложный consensus не создаётся.

## No Autonomous Repair Loop

Запрещён автоматический цикл:

```text
plan → execute → validate → repair → validate
```

Каждый переход является отдельным stage.

## Критерий качественной Collaboration

- роли понятны;
- writer один;
- candidate идентифицируем;
- handoff проверяем;
- legacy authority не переносится;
- human authority сохраняется;
- overhead меньше полученной пользы.
