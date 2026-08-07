# SLICE_04_PORTABLE_TASK
## Status
```yaml
status: ACCEPTED
human_acceptance: ACCEPTED
fact_class: PORTABLE_TASK
phase_a_run_id: PHASE_A_001
feature_id: FTR-001
```

## Task Goal
Реализовать механизм приёма свободного запроса пользователя, отделения problem от solution и формирования формализованного Intent Record (FTR-001) в виде Markdown/YAML файла.

## Scope boundaries
- **Allowed**: Создание структуры файла Intent Record, реализация парсера запроса (выделение problem, solution, assumptions), логика остановки для запроса Human Approval.
- **Forbidden**: Написание кода оркестратора, интеграция с Git, интеграция с БД, автоматический запуск задач.

## Actionable Chunks
1. Разработать шаблон Markdown/YAML для Intent Record.
2. Реализовать логику классификации свободного текста (разбор problem, solution, unknowns).
3. Реализовать логику формирования уточняющих вопросов (material questions) при нехватке данных.
4. Разработать механизм безопасной остановки (WAITING_FOR_HUMAN_APPROVAL).

## Constraints
- Никаких скрытых сайд-эффектов на репозиторий.
- Завершение задачи должно возвращать контроль пользователю.

## Validation Status
- self_review: PASS
- independent_validation: NOT_RUN
- bounded_correction: NOT_NEEDED
- final_status: PENDING
