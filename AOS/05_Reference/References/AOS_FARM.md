# AOS-FARM Reference

## Роль AOS-FARM

Repository `NMF13579/AOS-FARM` используется при реконструкции нового AOS исключительно как historical engineering reference.

```text
reference_mode: READ_ONLY_REFERENCE
authority: NONE
source_of_truth: NO
foundation: NO
implementation_source: NO
architecture_source: NO
approval_source: NO
lifecycle_source: NO
execution_authority: NO
```

Эти обозначения описывают границу использования source. Они не являются lifecycle metadata нового проекта.

## Почему AOS-FARM полезен

AOS-FARM содержит накопленный опыт разработки сложной AI-assisted development system:

- product hypotheses;
- workflow experiments;
- contracts;
- safety invariants;
- validation patterns;
- Git boundaries;
- human authority boundaries;
- failure modes;
- rejected approaches;
- evidence о чрезмерной сложности;
- lessons из recovery и control-heavy workflows.

Этот опыт необходимо сохранить, чтобы новый проект не повторил те же ошибки.

## Почему AOS-FARM не является foundation

AOS-FARM создавался в другом историческом контексте и накопил связанную между собой сложность:

- Product Runtime и Development Factory развивались одновременно;
- Governance и Control Plane частично становились prerequisites самой разработки;
- recovery workflows разрастались;
- readiness могла подменять product progress;
- formal control artifacts могли опережать observable user value;
- architecture отражала прежние constraints и accumulated decisions;
- большое число mechanisms затрудняло понимание одного следующего действия.

Поэтому перенос repository topology или implementation целиком может перенести не только полезные решения, но и причины прежних проблем.

## Что следует извлекать

Приоритетные классы знаний:

### Product knowledge

- исходная пользовательская проблема;
- chat-first interaction hypothesis;
- session resume;
- bounded task workflow;
- one next action;
- progressive disclosure;
- различие Product Runtime и Development Factory.

### Contract knowledge

- PASS не означает approval;
- Evidence не означает approval;
- CI PASS не означает approval;
- UNKNOWN не означает OK;
- NOT_RUN не означает PASS;
- human approval cannot be simulated;
- Git actions имеют отдельные authorization boundaries;
- scope не расширяется автоматически.

### Failure knowledge

- premature Control Plane;
- premature registry или database;
- automation before validated manual workflow;
- recovery becoming permanent architecture;
- skeleton being described as implementation;
- plan being treated as execution authority;
- excessive coupling между documentation, authority и runtime;
- false confidence from incomplete validation;
- autonomous continuation после failure или finding.

### Engineering knowledge

- repository-first factual state;
- explicit baseline binding;
- deterministic validation;
- target-only diff checks;
- independent validation;
- single writer;
- bounded retries;
- explicit stop conditions;
- reproducible setup;
- negative tests для control boundaries.

## Что нельзя переносить автоматически

Нельзя автоматически копировать:

- folder structure;
- old stage numbering;
- current или historical roadmap;
- schemas;
- executors;
- registries;
- Control Plane;
- database;
- CI workflows;
- dependency set;
- approval records;
- Evidence packages;
- Risk Profile assignments;
- branch rules;
- lifecycle states;
- protected file lists;
- active task state;
- claims о readiness;
- legacy terminology как обязательный vocabulary.

## Правило reimplementation

По умолчанию новое поведение следует reimplement from contract.

Существующий код может использоваться для анализа, examples или comparison. Его прямой импорт требует отдельного обоснования, проверки license, dependency review, security review и explicit human decision.

## Правило provenance

Когда lesson происходит из AOS-FARM, новый документ может указать происхождение идеи. Но обязательное правило должно быть полностью сформулировано внутри нового AOS.

Новый документ не должен говорить:

> Действовать так, как определено в AOS-FARM.

Он должен самостоятельно определить:

- требуемое поведение;
- границы;
- exceptions;
- validation;
- unknown handling.

## Центральный вывод

Новый AOS не является продолжением AOS-FARM.

Он является самостоятельным продуктом, который использует AOS-FARM как источник проверяемых lessons и anti-patterns, но не наследует его authority, lifecycle, implementation или architecture.
