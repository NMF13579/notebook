# Process Evolution

## Назначение документа

Process Evolution определяет, как Development process нового AOS улучшается на основании Evidence.

## Legacy Reference Boundary

Global legacy authority and extraction rules are canonical in [`Project Principles`](../00_Core/Project_Principles.md#legacy-reference-boundary).

For this topic, legacy material may inform analysis, but it does not define active rules, architecture, lifecycle, authority, or readiness.


## Maturity Path

```text
manual
→ repeatable
→ documented
→ assisted
→ controlled automation
→ justified enforcement
```

Каждый следующий уровень требует доказанной недостаточности предыдущего.

## Manual Stage

Manual cycles выявляют:

- реальные steps;
- необходимые artifacts;
- friction;
- failure modes;
- human boundaries.

Manual Stage является источником design knowledge, а не временной неудачей.

## Repeatable Stage

Процесс считается repeatable после нескольких сходных cycles с:

- устойчивыми inputs;
- одинаковыми outputs;
- ясными stop conditions;
- воспроизводимыми findings.

Один успешный случай недостаточен.

## Documented Stage

Документация описывает реально проверенный процесс.

Она не должна выдавать желаемую automation за действующую capability.

## Assisted Stage

Helpers могут:

- собирать facts;
- проверять structure;
- запускать checks;
- подготавливать reports;
- предлагать routing.

Они не заменяют human decisions.

## Controlled Automation

Automation требует:

- стабильной операции;
- bounded consequences;
- verifiable result;
- detectable failure;
- stop condition;
- removal path.

## Enforcement

Enforcement вводится только для recurring high-impact boundary.

Guideline не требует Runtime Enforcement автоматически.

## Improvement Cycle

```text
observe problem
→ collect Evidence
→ identify root cause
→ propose minimal change
→ bounded trial
→ evaluate
→ retain, revise or remove
```

## Root Cause Discipline

Новый process layer не считается default solution.

Причиной могут быть:

- unclear Product Contract;
- oversized Task;
- bad Task Brief;
- missing terminal state;
- mixed roles;
- unnecessary dependency;
- wrong baseline;
- excessive current complexity.

## Minimal Change Order

1. уточнить правило;
2. улучшить template;
3. добавить manual check;
4. создать small helper;
5. автоматизировать stable step;
6. вводить subsystem только при необходимости.

## Trial

Trial определяет:

- expected effect;
- Scope;
- success criteria;
- negative effects;
- duration;
- removal condition.

Trial не становится global standard автоматически.

## Evaluation

Возможные показатели:

- time to product result;
- scope expansions;
- recovery frequency;
- false PASS rate;
- repair loops;
- clarity of next action;
- cognitive load;
- manual interventions.

## Anti-Accumulation

Process review должен искать не только новые rules, но и:

- obsolete steps;
- duplicate artifacts;
- unused checks;
- temporary recovery rules;
- tools без измеримой пользы.

Удаление complexity является improvement.

## Architecture Boundary

Routine process improvement не должен скрыто менять:

- Source of Truth;
- authority;
- lifecycle;
- Product Contracts;
- protected boundaries;
- external interfaces.

Такие изменения требуют отдельного human-reviewed task.

## Критерий зрелого Process

Зрелый process:

- предсказуем;
- минимально достаточен;
- ускоряет product progress;
- создаёт terminal states;
- сохраняет human authority;
- умеет удалять собственную сложность;
- не копирует legacy process без независимого обоснования.
