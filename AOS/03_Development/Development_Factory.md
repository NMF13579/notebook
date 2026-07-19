# Development Factory

## Назначение документа

Development Factory — набор процессов, artifacts и tools, поддерживающих создание нового AOS.

Она не является Product Runtime и не является обязательным foundation первой полезной версии.

## Legacy Reference Boundary

Global legacy authority and extraction rules are canonical in [`Project Principles`](../00_Core/Project_Principles.md#legacy-reference-boundary).

For this topic, legacy material may inform analysis, but it does not define active rules, architecture, lifecycle, authority, or readiness.


## Emergence Order

```text
manual workflow
→ repeated cycles
→ stable contracts
→ templates
→ helpers
→ controlled automation
→ enforcement where justified
```

Factory не проектируется путём копирования legacy factory topology.

## Minimal Factory

Начальная Factory может включать:

- Agent Contract;
- Task Brief template;
- Stage Report template;
- manual workflow;
- local checks;
- handoff;
- stop rules.

Не обязательны:

- Control Plane;
- central registry;
- database;
- autonomous loop;
- workflow engine;
- runtime approval service;
- multi-agent orchestrator.

## Automation Candidate Test

Операция может автоматизироваться, если:

- выполнялась вручную несколько раз;
- inputs и outputs стабильны;
- failure detectable;
- consequences bounded;
- result verifiable;
- human boundary ясна;
- removal path существует.

## What May Be Automated

- read-only fact collection;
- structure checks;
- hashes;
- deterministic tests;
- report formatting;
- missing-field detection;
- routing recommendation;
- candidate package preparation.

## What Must Remain Human

- Risk Profile assignment;
- approval;
- architecture acceptance;
- protected change authorization;
- destructive operation authorization;
- execution authorization;
- Commit, Push, Merge и Release authorization.

## Complexity Budget

Перед новым component отвечают:

1. Какую recurring problem он решает?
2. Почему manual process недостаточен?
3. Какова минимальная реализация?
4. Какие new failure modes появляются?
5. Как component отключить или удалить?

## Replaceable Internals

Factory contracts важнее конкретных:

- providers;
- frameworks;
- databases;
- orchestration engines;
- CLI libraries.

Новая implementation должна быть replaceable.

## Registry Boundary

Registry вводится только при реальной проблеме scale, search или relation management.

Он не должен дублировать facts, canonical в Markdown или Git.

## Database Boundary

Database оправдана при наличии operational state, concurrency или запросов, которые нельзя надёжно обслуживать файлами.

Premature database создаёт migrations, backups и recovery без product value.

## Control Plane Boundary

Control Plane относится к зрелой стадии и требует:

- recurring control need;
- устойчивых contracts;
- ясной authority model;
- доказанной недостаточности manual checkpoints;
- приемлемого complexity budget.

## One Run — One Stage

Automation не объединяет Planning, Execution, Validation и Review в autonomous loop.

После одного stage она формирует result и stop.

## Критерий полезной Factory

Factory:

- сокращает путь к product outcome;
- снижает повторение ошибок;
- сохраняет human authority;
- уменьшает recovery;
- не наследует legacy complexity;
- остаётся проще поддерживаемого продукта.
