# 07.05 — Architecture Alternatives

## Назначение

Документ задаёт способ сравнения архитектурных alternatives для нового AOS без предоставления приоритета старой architecture.

Ни один вариант в этом разделе не является active architecture.

## Architecture admission rule

Architecture выбирается только после определения:

- target user;
- core problem;
- Product Outcome;
- First Vertical Slice;
- Product Contracts;
- Acceptance Criteria;
- relevant non-functional constraints.

## Comparison dimensions

Каждый вариант оценивается по следующим критериям:

```text
user_value_support:
conceptual_complexity:
implementation_complexity:
operational_complexity:
data_ownership:
source_of_truth_clarity:
testability:
replaceability:
dependency_cost:
recovery_behavior:
security_boundary:
network_requirement:
observability:
migration_cost:
legacy_coupling:
```

## Candidate alternatives

### Markdown-first repository state

Подходит для прозрачных, versioned и human-readable contracts и decisions.

Риски:

- fragmentation;
- manual consistency burden;
- weak queryability при масштабировании.

### File-based structured state

JSON или YAML могут использоваться для machine-readable artifacts, если ownership и canonicalization определены.

### Database-backed state

Рассматривается только после появления подтверждённой потребности в query, concurrency или scale.

Database не должна автоматически становиться Source of Truth только из-за удобства runtime.

### Modular monolith

Предпочтительный базовый candidate для ранней стадии, если он позволяет один deployable unit и ясные internal boundaries.

Это hypothesis, а не принятое решение.

### Distributed services

Не рассматриваются как default. Требуют подтверждённой потребности в независимом scaling, isolation или deployment.

### Local-first execution

Предпочтительно для ранних manual cycles при отсутствии необходимости external services.

### External orchestration

LangGraph, CrewAI и аналогичные frameworks не вводятся без доказанной потребности, которую нельзя проще решить локальным code и explicit workflow.

## Legacy architecture treatment

Legacy architecture раскладывается на:

- resolved problem;
- useful boundary;
- accidental complexity;
- coupling;
- operational cost;
- failure mode;
- simpler alternative.

Она не рассматривается как baseline нового проекта.

## Architecture decision boundary

Research может подготовить comparison и recommendation, но не может:

- объявить active architecture;
- изменить Source of Truth;
- разрешить dependency;
- начать implementation;
- назначить Risk Profile;
- выполнить protected/canonical change.

Такие действия требуют отдельного architecture decision и human checkpoint.
