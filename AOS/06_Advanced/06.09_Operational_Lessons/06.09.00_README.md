# 06.09.00 Operational Lessons

## Назначение документа

Operational Lessons превращает подтверждённый опыт в проверяемые правила нового AOS.

История сохраняется не ради копирования старой системы, а ради уменьшения повторения ошибок.

## Lesson Qualification

Lesson становится durable, когда определены:

- observed problem;
- context;
- impact;
- root cause;
- Evidence;
- confidence;
- new project rule;
- verification;
- scope of applicability;
- exceptions;
- review condition.

Один incident не должен автоматически создавать global rule.

## Primary Lessons from AOS-FARM

### Product Value Before Governance Expansion

Governance, recovery и readiness не должны опережать executable product capability.

Проверка:

- roadmap сохраняет Product Runtime vertical slice раньше full Control Plane;
- internal workflow не подменяет user value.

### Do Not Use an Unfinished Control Plane to Build Itself

Development process не должен зависеть от незавершённой системы управления этим же process.

Проверка:

- manual fallback существует;
- Product Runtime и Development Factory разделены;
- failure внутреннего control tool не блокирует весь низкорисковый read-only work.

### Planning Is Not Execution

Planning artifacts не получают execution-grade authority.

Проверка:

- Plan ≠ Task Brief;
- Plan ≠ approval;
- execution требует exact bounded authorization.

### Recovery Must Be Temporary

Recovery artifacts не должны создавать бесконечную новую lifecycle chain.

Проверка:

- recovery имеет exit criteria;
- после finding формируется report и stop;
- нет automatic repair loop.

### Formal Readiness Must Not Replace Product Progress

PASS, Evidence и CI не являются пользовательской ценностью или acceptance.

Проверка:

- product metrics отделены от process metrics;
- первый vertical slice демонстрирует observable behavior.

### Keep Authority Local and Clear

State не должен быть распределён между repository, chats, source packs и generated registries без ясного precedence.

Проверка:

- one Source of Truth per fact class;
- chats и reports не становятся authority;
- derived views rebuildable.

### Thin Documentation

Документы не должны становиться чрезмерно взаимозависимыми.

Проверка:

- объект имеет один основной документ;
- соседние документы не копируют большие общие sections;
- links заменяют дублирование, где это безопасно.

### Manual Before Automation

Automation выводится из observed repeated work.

Проверка:

- существуют manual cycles;
- inputs, outputs и failure modes известны;
- removal path определён.

### Reimplement from Contract

Default reuse mode:

```text
REIMPLEMENT_FROM_CONTRACT
```

Copy допустим только после contract, dependency, security и test review.

### Unknown Is Scoped

`UNKNOWN` не превращается автоматически в `OK`, но и не обязан глобально блокировать не связанную low-risk работу.

Проверка:

- unknown имеет affected boundary;
- blocking scope указан явно.

## Positive Patterns Worth Re-Evaluating

Как candidates могут рассматриваться:

- explicit non-grants;
- exact baseline binding;
- false-PASS prevention;
- technical status отдельно от human decision;
- read-only prepare, verify и preview;
- one next action;
- immutable handoff;
- negative tests;
- portability checks.

Они не являются обязательными до независимого подтверждения потребности.

## Reference Provenance

При извлечении точного legacy artifact фиксируются:

- source repository;
- commit или tree;
- source path;
- digest;
- extraction date;
- classification;
- authority in new AOS: `NONE`.

## Review

Lesson пересматривается, если:

- изменился Product Contract;
- root cause оказался неверным;
- правило создаёт больше friction, чем предотвращает;
- появились новые Evidence;
- область применения расширилась.
