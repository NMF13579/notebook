# Control Points in Product and Development Workflows

## Назначение

Control point — место в реальном workflow, где перед продолжением проверяется конкретное условие или требуется human decision.

```text
workflow сначала
→ control point только там, где есть реальный риск перехода
```

Control points выводятся из `03_Product` и `04_Development`, а не копируются из legacy gate catalog.

## Product control points

Human checkpoint нужен перед изменением:

- primary target user;
- core user problem;
- product promise;
- first vertical slice;
- Product contracts;
- acceptance criteria;
- explicit non-goals.

Product hypothesis не становится contract автоматически. Нужны observable behavior, boundary, verification method и human review.

Заявление о working feature требует implementation, validation и раскрытых limitations. Documentation или skeleton недостаточны.

## Development control points

### Перед planning

Проверяются цель, expected result, scope и наличие architecture, dependency или protected decisions.

### Перед execution

Проверяются execution authorization, bounded scope, workspace, branch и baseline при необходимости, validation, stop conditions, network и destructive boundaries.

### После execution

Исполнитель не начинает independent validation автоматически. Он сообщает фактические изменения и одно следующее действие.

### Перед validation

Должны существовать конкретный candidate, validation scope, expected checks и read-only validator boundary.

### После validation

`PASS` не создаёт approval. `FAIL` или blocking finding приводит к report и stop. Correction является отдельной task.

### Перед review

Claims отделяются от Evidence, findings и unknowns раскрываются, review остаётся read-only.

## Dependencies

Новая dependency требует отдельного решения, если влияет на runtime architecture, network, security, reproducibility или operational complexity. Она не принимается только потому, что использовалась в AOS-FARM.

## Architecture

Architecture checkpoint нужен при изменении component boundaries, Source of Truth, persistent services, database, shared authority или трудно обратимой foundation.

Локальная implementation detail не должна превращаться в architecture gate.

## Automation

До automation нужны несколько успешных manual cycles, стабильные inputs/outputs, известные failure modes, измеримая выгода и rollback.

## Минимизация

Каждый control point должен иметь проверяемое условие, владельца, failure result, причину и критерий удаления. Механизм, который создаёт задержку без предотвращения реальной проблемы, пересматривается.
