# SLICE_02_PRODUCT_CONTRACT
## Status
```yaml
status: ACCEPTED
human_acceptance: ACCEPTED
fact_class: PRODUCT_CONTRACT
phase_a_run_id: PHASE_A_001
feature_id: FTR-001
```

## Problem & Outcome
**Problem**: Свободный текстовый запрос часто смешивает problem, solution, assumptions и constraints, что приводит к некорректной реализации и scope creep.
**Outcome**: Получение строго формализованного версионируемого Intent Record с явным problem/outcome, unknowns и одним next route.

## Target Users
- Владелец продукта или отраслевой эксперт, которому нужен результат.
- Агент или исполнитель, работающий по контракту (Intent Record).
- Reviewer или operator для затронутой границы (boundary).

## Triggers & Preconditions
- **Trigger**: Выбранная человеком цель или условие workflow, инициирующая приём свободного намерения.
- **Preconditions**: Релевантные authority sources определены, human disposition запроса = `UNDECIDED`.

## Inputs & Outputs
- **Inputs**: Свободный текст (original request). Опциональный контекст из текущего состояния.
- **Outputs**: Версионируемый Intent Record (C-001) с явным статусом, provenance, limitations и одним next route.

## Main Flow
1. Сохранить original request.
2. Классифицировать request и sensitivity.
3. Задать только material questions.
4. Отделить outcome от solution.
5. Показать assumptions/unknowns.
6. Получить human correction.
7. Выдать one next route.

## State Effects
Формируется новый артефакт (Intent Record). Фича не вызывает автоматического перехода к исполнению, аппруву или Git delivery.

## Failures & Recovery
- **Failures**: Missing/stale input; рекомендация выдаётся за решение человека; скрытое расширение scope.
- **Recovery**: Остановить операцию, сохранить состояние, пометить stale, запросить решение человека (Fail Closed).

## Acceptance Criteria
- Человек узнаёт problem/outcome.
- Все assumptions видимы.
- Unknowns имеют resolution path.

## Negative Scenarios
- Пустой запрос остаётся CLARIFYING (не запускает исполнение).
- Prompt injection не меняет user goal.
- Сгенерированный аппрув может быть отклонён.

## Validation Status
- self_review: PASS
- independent_validation: NOT_RUN
- bounded_correction: NOT_NEEDED
- final_status: PENDING
