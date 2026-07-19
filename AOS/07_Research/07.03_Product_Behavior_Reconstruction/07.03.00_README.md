# 07.03 — Product Behavior Reconstruction

## Назначение

Документ определяет, как извлекать из legacy материалов пользовательски значимое поведение, не копируя внутреннюю implementation.

Предмет реконструкции — то, что пользователь видит, понимает и может сделать.

## Приоритет источников

Для определения нового продукта приоритет имеют:

1. текущий product intent нового проекта;
2. исследование target user и core problem;
3. observable behavior;
4. новые Product Contracts и Acceptance Criteria;
5. legacy materials как `READ_ONLY_REFERENCE`.

Legacy feature list не является новым product scope.

## Единица реконструкции

Каждый behavior candidate описывается через:

```text
user:
context:
trigger:
user_intent:
input:
system_behavior:
observable_output:
human_decision_point:
failure_behavior:
resume_behavior:
acceptance_signal:
legacy_source:
unknowns:
```

## Ключевые behavior candidates

### Понятное текущее состояние

Пользователь должен понимать:

- что происходит;
- какая задача активна;
- что уже сделано;
- что не проверено;
- где нужен human decision.

### One next action

После каждого законченного этапа система показывает ровно одно следующее действие.

Это не означает автоматический запуск следующего этапа.

### Bounded task

Задача имеет явные:

- цель;
- expected result;
- allowed scope;
- forbidden scope;
- validation;
- stop conditions.

### Session resume

После перерыва пользователь должен восстановить рабочий контекст без перечитывания всей истории.

Resume state должен отделять:

- факты;
- decisions;
- unresolved questions;
- completed work;
- next required action.

### Progressive disclosure

Основной интерфейс показывает минимально необходимую информацию. Детали доступны по запросу, но не скрывают blockers или unknowns.

### Human checkpoint

Система явно останавливается перед действиями, требующими решения человека.

Human checkpoint не симулируется положительным статусом агента.

### Failure behavior

При failure или blocking finding система:

1. не исправляет проблему скрыто;
2. не повторяет этап автоматически;
3. фиксирует факт;
4. ограничивает affected boundary;
5. показывает одно следующее действие;
6. останавливается.

## Что не реконструируется автоматически

- legacy command names;
- folder topology;
- внутренние registries;
- конкретные schemas;
- старые status names;
- provider-specific prompts;
- orchestration framework;
- database model;
- historical lifecycle.

Эти элементы рассматриваются только после определения нового Product Contract.

## Behavior equivalence

Новая implementation не обязана повторять внутренний механизм legacy системы.

Она должна обеспечивать требуемый observable outcome с более простой, проверяемой и replaceable implementation.

## Negative behavior

Acceptance должна включать отсутствие опасных результатов:

- false PASS;
- fake approval;
- hidden execution;
- hidden scope expansion;
- automatic Git mutation;
- потеря unresolved unknown;
- выдача documentation за implementation;
- выдача skeleton за работающий product.

## Выход исследования

Результаты этого документа могут стать входом для:

- Target User;
- Product Outcome;
- User Journey;
- Product Contracts;
- Acceptance Criteria;
- First Vertical Slice.

Они не становятся активными требованиями без отдельного переноса в `03_Product` и human review.
