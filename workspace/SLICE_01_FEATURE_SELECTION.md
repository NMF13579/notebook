# SLICE_01_FEATURE_SELECTION
## Status
```yaml
status: ACCEPTED
fact_class: HUMAN_DECISION_RECORD
human_acceptance: ACCEPTED
acceptance_scope: PHASE_A_DOCUMENTATION_ONLY
implementation_authorization: NONE
git_authorization: NONE
```

⸻

## Identity
```yaml
phase_a_run_id: PHASE_A_001
```

## Methodology Reference
```yaml
method_profile:
  IMPLEMENTATION_ARTIFACT_PROFILE: R4
planning_pipeline:
  IMPLEMENTATION_PLANNING_PIPELINE: R9
```

⸻

## Purpose

Зафиксировать первую реальную Feature AOS, которая становится объектом полного Phase A implementation-planning.

Документ не определяет Product Contract.

Документ не определяет Engineering Design.

Документ не содержит implementation decisions.

Единственная задача документа — определить предмет дальнейшего проектирования.

⸻

## Loop Prevention

Данный документ существует для предотвращения следующей петли:

Product Contract
↓
смена Feature
↓
переписывание Product Contract
↓
переписывание Engineering Design
↓
переписывание Portable Task

После принятия Feature Selection объект проектирования считается неизменным до завершения текущего Phase A.

Изменение выбранной Feature требует нового Phase A run.

```yaml
feature_change_after_acceptance:
  allowed: NO
  exception:
    NEW_HUMAN_DECISION
  effect:
    terminate_current_phase_a
    start_new_phase_a
```

```yaml
method_revision_change:
  allowed: NO
  effect:
    terminate_current_phase_a
    start_new_phase_a
```

⸻

## Selected Feature

feature_id: FTR-001
feature_name: Приём намерения, проблемное интервью и уточнение результата
human_disposition: SELECTED_FOR_X1

⸻

## Selection Scope

### Included

- Приём намерения
- Проблемное интервью
- Уточнение результата (Intent Record)
- Отделение problem/outcome от solution
- Прояснение assumptions/unknowns

### Explicitly Excluded

Все остальные Feature AOS.

⸻

## Business Motivation

Причина выбора первой Feature:

Необходимость формализации входных запросов в строгий Intent Record (FTR-001) перед их исполнением, как основа для всего Development Factory.

⸻

## Expected Result

После завершения текущего Phase A должна существовать полностью сформированная цепочка документов:

Product Contract
↓
Engineering Design
↓
Portable Task
↓
Validation Plan
↓
Implementation Package

для выбранной Feature.

⸻

## Authority

feature_selection_authority: HUMAN
engineering_authority: NONE
implementation_authority: NONE
git_authorization: NONE
repository_binding: NOT_RUN

⸻

## Exit Criteria

Feature Selection считается завершённой после принятия человеком следующих полей:

* feature_id
* feature_name
* included scope
* excluded scope

После этого допускается создание Product Contract.

⸻

## Loop Guard

Перед созданием следующего артефакта необходимо проверить:

feature_selected: YES
feature_changed: NO
method_revision_locked: YES
authority_known: YES
loop_risk: LOW
previous_stage_closed: YES
downstream_started: NO

Если хотя бы одно условие нарушено:

Product Contract не создаётся.

⸻

## Current State

feature_id: FTR-001
state: PRE_ARTIFACT_GATE_PASSED
next_artifact:
Product Contract
