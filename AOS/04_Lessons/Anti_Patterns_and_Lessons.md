# Anti-Patterns and Lessons

## Назначение документа

Документ фиксирует lessons, извлечённые из предыдущей разработки, без превращения старого проекта в Source of Truth нового AOS.

## Legacy Reference Boundary

Global legacy authority and extraction rules are canonical in [`Project Principles`](../00_Core/Project_Principles.md#legacy-reference-boundary).

For this topic, legacy material may inform analysis, but it does not define active rules, architecture, lifecycle, authority, or readiness.


## Process Before Product

### Anti-pattern

Development Factory, Governance и Control Plane строятся раньше Product Runtime.

### Lesson

Сначала Product Contracts, vertical slice и manual product cycles.

## Self-Referential Control Loop

### Anti-pattern

Незрелая control system управляет созданием самой себя.

### Lesson

Использовать минимальные human checkpoints до появления устойчивой operational need.

## Overplanning

### Anti-pattern

Plans, revisions и plans of plans заменяют bounded execution.

### Lesson

Повторный planning не запускается при полном Task Brief и неизменных условиях.

## Scope Drift

### Anti-pattern

Unrelated findings исправляются внутри текущей Task.

### Lesson

Finding → report → separate follow-up Task.

## Validation-Repair Loop

### Anti-pattern

Validation исправляет candidate и повторяется.

### Lesson

Validation read-only; correction — отдельная Task.

## Recovery as Normal Workflow

### Anti-pattern

Recovery становится permanent development mode.

### Lesson

Recovery bounded, terminal и возвращает к normal workflow либо `UNKNOWN_BLOCKED`.

## Approval Simulation

### Anti-pattern

PASS, Evidence или CI success превращаются в approval.

### Lesson

```text
PASS ≠ approval
Evidence ≠ approval
CI PASS ≠ approval
Human approval cannot be simulated
```

## Git Boundary Collapse

### Anti-pattern

Edit автоматически ведёт к Commit, Push, Merge или Release.

### Lesson

```text
Edit ≠ Commit
Commit ≠ Push
Push ≠ Merge
Merge ≠ Release
```

## State Explosion

### Anti-pattern

Создаются многочисленные states и transitions до operational need.

### Lesson

Начинать с смысловой модели и простых artifacts; runtime state machine вводить позже.

## Registry Explosion

### Anti-pattern

Registry дублирует facts из Markdown и Git.

### Lesson

One Source of Truth per fact class.

## Premature Database

### Anti-pattern

Database появляется раньше operational state и concurrency.

### Lesson

Использовать files и Git до доказанной недостаточности.

## Premature Automation

### Anti-pattern

Автоматизируется изменяющийся process.

### Lesson

Сначала несколько successful manual cycles.

## Documentation as Completion

### Anti-pattern

Document, skeleton или plan выдаются за implemented capability.

### Lesson

```text
Skeleton ≠ implementation
Documentation ≠ technical completion
```

## Architecture by Inheritance

### Anti-pattern

Legacy topology переносится потому, что уже существует.

### Lesson

Reimplement from contract by default.

Legacy используется только для behavior, lessons и failure modes.

## Tool-Driven Architecture

### Anti-pattern

Product design подстраивается под framework или agent platform.

### Lesson

Сначала contracts и observable behavior, затем replaceable tools.

## Missing Terminal State

### Anti-pattern

Stage автоматически переходит в следующий.

### Lesson

Каждый stage заканчивается result, report, one next action и stop.

## Hidden Unknowns

### Anti-pattern

Unknown заменяется оптимистичным предположением.

### Lesson

```text
UNKNOWN ≠ OK
NOT_RUN ≠ PASS
```

## Parallel Writers

### Anti-pattern

Несколько agents меняют один candidate.

### Lesson

Одна Task — один writer; parallelism только read-only и bounded.

## Configuration Drift

### Anti-pattern

Model, reasoning, sandbox или network меняются скрыто.

### Lesson

Configuration mismatch означает BLOCKED.

## Complexity Without Exit

### Anti-pattern

Mechanism добавляется без removal path.

### Lesson

Каждый component требует problem statement, success criteria и removal path.

## Global Rule from One Incident

### Anti-pattern

Один finding создаёт permanent global gate.

### Lesson

Durable rule требует Evidence, root cause и review.

## Reference Contamination

### Anti-pattern

Legacy status, approval, architecture или unfinished implementation переносятся в новый project documentation как active fact.

### Lesson

Каждый imported lesson должен быть:

1. отделён от legacy authority;
2. независимо проверен;
3. переписан в терминах нового проекта;
4. принят отдельным human decision, если он меняет canon.

## Кратчайший безопасный путь

Главный lesson:

> Выбирать наиболее простой путь, который сохраняет product value, проверяемость и необходимые human boundaries.

Кратчайший путь не означает обход безопасности.

Безопасность не означает максимальную формализацию.
