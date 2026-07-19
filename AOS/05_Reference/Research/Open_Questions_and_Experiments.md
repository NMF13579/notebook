# 07.09 — Open Questions and Experiments

## Назначение

Документ хранит unresolved questions и bounded experiments, которые нужны для проверки assumptions нового AOS.

Это не implementation backlog и не список обязательных roadmap tasks.

## Open question format

```text
question_id:
question:
why_it_matters:
affected_boundary:
current_evidence:
unknowns:
possible_answers:
decision_needed:
blocking_scope:
next_safe_inquiry:
```

Unknown должен блокировать только affected boundary.

## Experiment format

```text
experiment_id:
hypothesis:
user_or_system_context:
minimal_setup:
controlled_variables:
observable_result:
success_criteria:
failure_criteria:
negative_checks:
allowed_scope:
forbidden_scope:
validation_method:
stop_conditions:
result_disposition:
```

Experiment plan не является execution authorization.

## Приоритетные product questions

- Кто является primary target user первой версии?
- Какой один outcome создаёт достаточную начальную ценность?
- Как пользователь формирует bounded task без знания внутреннего Governance?
- Какой минимальный session resume действительно полезен?
- Когда one next action уменьшает cognitive load, а когда скрывает важные alternatives?
- Какие human checkpoints понятны пользователю без control jargon?
- Как доказать ценность первого vertical slice вручную?

## Architecture questions

- Достаточно ли Markdown-first state для первой версии?
- Какие данные требуют machine-readable representation?
- Как определить один Source of Truth per fact class?
- Нужна ли persistent database до multi-project mode?
- Какие internal boundaries должны быть replaceable?

## Development questions

- Какой минимальный Task Brief достаточно исполним?
- Как отделить planning от execution без избыточного process overhead?
- Какие checks обязательны на documentation-only stage?
- После скольких manual cycles automation оправдана?
- Какие данные нужны для надёжного session handoff?

## Control questions

- Какие операции действительно требуют Runtime Enforcement?
- Какие protected/canonical classes нужны новому проекту?
- Как назначается Risk Profile без лишней bureaucratic burden?
- Где fail-closed обязателен, а где должен быть локальным?
- Какие claims требуют independent Evidence?

## Candidate experiments

### First vertical slice dogfood

Проверить, может ли пользователь пройти один bounded cycle от намерения до понятного результата и human decision без Control Plane и registry.

### Session resume test

После контролируемого перерыва проверить, может ли пользователь восстановить состояние по компактному handoff.

### One next action usability test

Проверить, уменьшает ли один следующий шаг неопределённость и не скрывает ли blocking decisions.

### Manual workflow repetition

Провести два или три manual cycles и зафиксировать повторяющиеся действия, ошибки и нагрузку до предложения automation.

### Contract negative cases

Проверить, что система не трактует `PASS`, Evidence или CI как approval и не смешивает Git boundaries.

## Experiment completion

Результат experiment должен содержать:

- observations;
- collected Evidence;
- deviations;
- findings;
- unknowns;
- conclusion strength;
- recommended disposition;
- одно следующее действие.

Experiment result не является human acceptance.

## Promotion boundary

Подтверждённый вывод переносится в active документ только после explicit human review.

Отрицательный результат сохраняется как lesson и может закрыть candidate без implementation.
