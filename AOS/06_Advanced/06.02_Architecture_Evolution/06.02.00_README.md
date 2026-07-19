# 06.02.00 Architecture Evolution

## Назначение документа

Architecture Evolution определяет, как architecture нового AOS изменяется после появления реальных product и operational needs.

Architecture не восстанавливается путём копирования старой topology.

## Starting Principle

Начальная architecture должна быть минимальной, проверяемой и replaceable.

```text
accepted product contracts
→ minimum Product Runtime
→ observable behavior
→ repeated use
→ Evidence-backed evolution
```

## Architecture Change Triggers

Изменение может рассматриваться, если существует подтверждённая проблема:

- текущая boundary нарушает Product Contract;
- компонент невозможно безопасно изменять;
- повторяющиеся failures имеют общий root cause;
- производительность не соответствует принятому requirement;
- data consistency невозможно обеспечить простым способом;
- extension need подтверждена несколькими use cases;
- security или safety boundary требует усиления;
- operational burden стабильно превышает complexity cost изменения.

## Non-Triggers

Не являются достаточными основаниями:

- популярность framework;
- legacy implementation;
- speculative scale;
- preference конкретного агента;
- желание заранее поддержать все providers;
- формальная «enterprise readiness»;
- один неудобный change;
- возможность добавить abstraction.

## Contract Before Internals

Перед изменением implementation фиксируются:

- observable behavior;
- inputs и outputs;
- invariants;
- failure semantics;
- compatibility requirements;
- migration boundary;
- acceptance criteria.

Default подход к legacy:

```text
understand behavior
→ extract candidate contract
→ independently validate need
→ reimplement minimal capability
```

## Architecture Decision Boundary

Architecture change требует human decision, когда затрагивает:

- Source of Truth;
- canonical contracts;
- persistence model;
- security boundary;
- dependency policy;
- Product Runtime boundaries;
- public interfaces;
- destructive migration;
- cross-project behavior;
- lifecycle или approval semantics.

Агент может подготовить recommendation, но не принять architecture.

## Replaceable Internals

Предпочтение отдаётся contracts, которые не привязывают AOS к:

- одному model provider;
- одному agent runtime;
- одному database;
- одному orchestration framework;
- одному cloud;
- одному UI;
- одному CI provider.

Replaceability не требует premature abstraction. Interface вводится только при подтверждённой вариативности.

## Migration

Migration должна быть:

- explicit;
- bounded;
- проверяемой;
- обратимой, когда это возможно;
- отделённой от feature implementation;
- связанной с exact baseline;
- безопасной при partial failure.

Destructive migration требует explicit human authorization.

## Architecture Drift

Drift выявляется сравнением implementation с accepted contracts, а не сравнением с legacy repository.

Legacy может показать исторический вариант, но не определяет правильное current state.

## Simplification

Architecture evolution включает удаление.

Удаление abstraction, service, registry, state machine или dependency является нормальным результатом, если capability не подтверждает ценность.

## Required Output

Architecture proposal должен показывать:

- problem;
- Evidence;
- existing boundary;
- proposed boundary;
- alternatives;
- trade-offs;
- affected contracts;
- migration;
- validation;
- rollback;
- one next action.
