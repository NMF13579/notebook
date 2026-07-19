# 09.05 — Closed Temporary Artifacts

## Назначение

Этот объект хранит временные artifacts нового проекта, завершившие свою ограниченную функцию.

Цель — не позволить temporary process стать permanent architecture.

## Типичные материалы

- recovery checklist;
- incident-specific instructions;
- temporary migration notes;
- stabilization procedures;
- reconciliation packages;
- bounded workaround;
- transition map;
- one-time compatibility guidance;
- temporary review package;
- controlled cleanup plan.

## Критерий закрытия

Temporary artifact может быть закрыт, когда:

- его задача выполнена;
- underlying problem устранена;
- permanent replacement создан;
- процедура больше не нужна;
- условия применения больше не существуют;
- продолжение использования создаёт риск;
- human decision прекратил соответствующий workflow.

## Temporary boundary

```text
Temporary ≠ canonical.
Temporary success ≠ permanent requirement.
Recovery ≠ product architecture.
Workaround ≠ target design.
```

Длительное существование temporary artifact не превращает его в active Source of Truth.

## Что должно быть сохранено

При закрытии следует сохранить:

- исходную проблему;
- условия применения;
- сделанные действия;
- фактический результат;
- unresolved findings;
- lessons;
- permanent replacement, если он существует;
- ограничения повторного использования.

## Что не должно происходить

Нельзя:

- объявлять recovery завершённым без Evidence;
- считать closed artifact approved permanent solution;
- переносить workaround в новый проект без re-evaluation;
- скрывать unresolved failure через архивирование;
- сохранять secrets;
- хранить temporary outputs из `/.aos-tmp/` как durable archive без отдельного решения;
- использовать закрытый checklist как execution authorization.

## Validation boundary

Закрытие temporary artifact не означает:

- что связанная implementation прошла validation;
- что product outcome достигнут;
- что CI PASS;
- что human acceptance получено;
- что commit, push, merge или release разрешены.

Каждый такой факт должен иметь собственное подтверждение.

## Recovery lessons

Recovery materials особенно важны для извлечения anti-patterns:

- бесконечные repair loops;
- смешивание diagnosis и execution;
- automatic retry после failure;
- расширение scope ради закрытия текущей задачи;
- превращение recovery tooling в product foundation;
- накопление control complexity без product value;
- использование временного state как нового canonical state.

## Legacy boundary

Recovery artifacts AOS-FARM остаются references.

Новый проект может извлечь из них lessons, но не должен:

- продолжать старую recovery chain;
- наследовать старые task IDs;
- принимать старые checkpoints;
- переносить прежние approvals;
- считать legacy Evidence актуальным;
- воспроизводить recovery topology как foundation.
