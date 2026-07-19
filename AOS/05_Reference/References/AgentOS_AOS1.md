# AgentOS and AOS-1 Reference

## Роль исторических материалов

AgentOS, AOS-1 и связанные historical materials используются только для понимания ранних product hypotheses, terminology evolution и прежних architecture experiments.

```text
reference_mode: READ_ONLY_REFERENCE
authority: NONE
active_foundation: NO
import_by_default: FORBIDDEN
```

## Допустимая ценность

Из этих материалов можно извлекать:

- ранние формулировки пользовательской проблемы;
- идеи об agent-assisted development;
- hypotheses о project memory;
- UX concepts;
- terminology history;
- reasons, по которым отдельные approaches были изменены;
- failure modes ранних architecture attempts;
- product capabilities, которые стоит заново оценить.

## Основные риски

Исторические материалы могут:

- использовать устаревшие названия;
- предполагать уже отвергнутую architecture;
- смешивать product и internal development tooling;
- содержать incomplete или aspirational claims;
- ссылаться на несуществующие contracts;
- предполагать authority, которая отсутствует в новом проекте;
- описывать prototype как готовую систему;
- отражать прежний repository context.

## Запрет foundation import

Нельзя импортировать AgentOS или AOS-1 как:

- base repository;
- active architecture;
- Source of Truth;
- dependency;
- governance model;
- lifecycle model;
- approval model;
- runtime contract;
- default naming system.

Любая сохранившаяся идея должна пройти Knowledge Extraction и быть заново сформулирована в терминах нового AOS.

## Terminology handling

Старые названия допустимы только при описании historical context.

Active terminology нового проекта определяется его собственными документами. Совпадение названий не означает совместимость contracts.

## Приоритет observable evidence

При конфликте между historical claim и наблюдаемым artifact следует различать:

- что было задумано;
- что было документировано;
- что было реализовано;
- что было проверено;
- что было принято человеком.

Эти состояния нельзя объединять в одно утверждение.

## Результат использования

Успешное использование AgentOS/AOS-1 означает, что новый проект сохранил полезную исходную идею или lesson, не унаследовав historical authority и связанную с ней сложность.
