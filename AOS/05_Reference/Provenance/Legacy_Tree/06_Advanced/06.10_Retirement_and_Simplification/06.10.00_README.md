# 06.10.00 Retirement and Simplification

## Назначение документа

Retirement and Simplification определяет, как удалять capabilities, abstractions, dependencies и process layers, которые не подтверждают ценность.

Удаление является частью architecture evolution.

## Retirement Triggers

Capability рассматривается к удалению, если:

- не используется;
- решаемая проблема исчезла;
- simpler mechanism достаточен;
- cost превышает value;
- создаёт frequent false positives;
- затрудняет product changes;
- дублирует canonical source;
- создаёт ambiguity authority;
- зависит от obsolete provider;
- поддерживает только recovery-specific workflow;
- не имеет владельца;
- не проходит validation;
- Product Runtime больше не нуждается в ней.

## Simplification Priority

Предпочтительный порядок:

1. остановить дальнейшее расширение;
2. определить affected contracts;
3. отключить optional path;
4. проверить manual fallback;
5. экспортировать durable facts;
6. удалить derived state;
7. удалить implementation;
8. удалить obsolete documentation;
9. сохранить короткую historical reference;
10. проверить отсутствие hidden dependency.

## Protected and Destructive Boundary

Удаление может быть destructive.

Если затрагиваются:

- canonical contracts;
- durable data;
- public interface;
- user content;
- security controls;
- repository history;
- protected files;

требуется explicit human authorization и bounded migration plan.

## Data Preservation

Перед removal определяется:

- что является canonical;
- что derived;
- что необходимо сохранить;
- что можно rebuild;
- retention;
- export format;
- verification.

Derived registry или cache не должен удерживать проект от simplification.

## Compatibility

Backward compatibility сохраняется только при принятой необходимости.

Legacy compatibility не является default requirement нового AOS.

## Tombstone

Для значимого retired object сохраняется короткая запись:

- что удалено;
- почему;
- чем заменено;
- какие migrations выполнены;
- где находится historical reference;
- какие assumptions больше не действуют.

Tombstone не должен выглядеть как active Source of Truth.

## Decommission Validation

Проверяется:

- Product Runtime продолжает давать expected behavior;
- canonical knowledge сохранено;
- secrets revoked;
- network permissions removed;
- scheduled jobs stopped;
- integrations disconnected;
- generated indexes rebuilt;
- documentation updated;
- no hidden writers remain;
- rollback condition понятна.

## Anti-Accumulation Rule

Новый AOS не обязан сохранять каждую когда-либо созданную capability.

Architecture quality оценивается не количеством компонентов, а:

- ясностью;
- соответствием Product Contract;
- observable behavior;
- безопасностью;
- replaceability;
- стоимостью изменения;
- возможностью удаления.

## Legacy Cleanup

Legacy artifacts не мигрируются только ради полноты архива.

Reference сохраняется отдельно от active project knowledge и никогда не получает authority автоматически.
