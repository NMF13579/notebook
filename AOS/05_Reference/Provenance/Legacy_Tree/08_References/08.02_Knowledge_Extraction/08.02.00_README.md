# Knowledge Extraction

## Назначение

Этот документ задаёт повторяемую процедуру переноса опыта из reference materials в самостоятельное знание нового AOS.

Цель процесса — не пересказать старый проект, а отделить полезные contracts и lessons от исторической сложности.

## Единица извлечения

Knowledge item должен описывать одну проверяемую мысль:

- user need;
- observable behavior;
- contract;
- failure mode;
- constraint;
- lesson;
- trade-off;
- rejected approach;
- validation method.

Нельзя объединять несвязанные выводы только потому, что они находились в одном legacy artifact.

## Процесс извлечения

### 1. Identify source

Зафиксировать конкретный source:

- repository;
- path;
- document;
- commit или version, если известны;
- conversation или date range;
- external publication.

### 2. Extract factual observation

Отделить наблюдаемый факт от интерпретации.

Примеры фактов:

- команда возвращала конкретный exit code;
- пользователь не мог понять следующее действие;
- два документа противоречили друг другу;
- automation запускала следующий stage без human decision;
- тест проверял только наличие файла, но не behavior.

### 3. Identify intent

Определить, какую проблему пыталось решить старое решение.

Legacy implementation может быть неудачной, но исходная проблема может оставаться актуальной.

### 4. Identify assumptions

Выявить assumptions:

- repository model;
- provider;
- operating system;
- team size;
- network availability;
- trust model;
- maturity stage;
- dependency availability;
- governance requirements.

### 5. Identify outcomes

Разделить:

- подтверждённый результат;
- частичный результат;
- заявленный результат;
- неизвестный результат;
- failure.

`UNKNOWN` не преобразуется в `OK`.

### 6. Extract lesson

Сформулировать lesson без привязки к legacy topology.

Плохая формулировка:

> Новый проект должен скопировать старый registry.

Хорошая формулировка:

> Для каждого активного artifact class должен существовать один понятный владелец факта; механизм реализации выбирается отдельно.

### 7. Minimize

Найти минимальную форму, сохраняющую ценность.

Следует предпочитать:

- contract вместо framework;
- manual cycle вместо automation;
- file вместо database, пока database не требуется;
- explicit state вместо inference;
- one next action вместо autonomous loop;
- local check вместо сложной CI orchestration, пока она не обоснована.

### 8. Verify relevance

Проверить, относится ли lesson к текущему продукту, stage и scope.

Полезная идея может быть преждевременной. В таком случае она остаётся research/reference и не становится active requirement.

### 9. Propose destination

Для каждого принятого knowledge item определить целевой класс:

- Product Contract;
- Acceptance Criteria;
- Project Principle;
- Architecture Decision;
- Development rule;
- Safety rule;
- Research hypothesis;
- Non-goal;
- Archive note.

### 10. Human decision

Human решает:

- принять;
- отклонить;
- отправить на доработку;
- сохранить как research;
- сохранить только как historical reference.

Отсутствие human decision не означает принятие.

## Минимальная карточка Knowledge Item

```text
Source:
Observed fact:
Original intent:
Assumptions:
Outcome confidence:
Failure modes:
Extracted lesson:
Simpler formulation:
Proposed destination:
Open questions:
Human decision:
```

Поле `Human decision` не заполняется агентом от имени человека.

## Защита от legacy bias

Для каждого предложения необходимо задать вопросы:

- Создали бы мы это решение, не видя старую implementation?
- Требует ли проблема именно такого механизма?
- Можно ли проверить contract без старого repository?
- Не является ли сложность следствием прежнего процесса, а не продукта?
- Не пытаемся ли мы сохранить sunk cost?

## Stop conditions

Извлечение останавливается и помечается `HUMAN_REVIEW_REQUIRED`, если:

- source противоречит active project rule;
- provenance неизвестен;
- факт невозможно отделить от claim;
- требуется architecture decision;
- затрагивается protected/canonical boundary;
- предлагается destructive migration;
- scope начинает расширяться;
- невозможно определить, что именно подтверждено.

## Результат

Результатом процесса является не копия source, а самостоятельная, ограниченная и проверяемая формулировка знания с сохранённым provenance.
