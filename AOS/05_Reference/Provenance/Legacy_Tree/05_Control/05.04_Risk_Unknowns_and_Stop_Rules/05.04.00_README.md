# Risk, Unknowns and Stop Rules

## Назначение

Control усиливается пропорционально потенциальному ущербу, обратимости и способности обнаружить ошибку. Формальная сложность текста или количество файлов сами по себе не определяют риск.

## Risk

При оценке учитываются:

- пользовательские данные;
- protected/canonical artifacts;
- external side effects;
- secrets;
- network;
- destructive commands;
- Git history;
- dependencies;
- architecture;
- authority;
- масштаб scope;
- возможность rollback.

Агент может предложить Risk Profile, но человек назначает его. До необходимости формальной taxonomy достаточно категорий `LOW`, `MEDIUM`, `HIGH`, `UNKNOWN`, определённых текущим проектом, а не legacy system.

## Unknown

Unknown возникает при отсутствии необходимого факта, неизвестном baseline, owner, protected boundary, environment или неоднозначном tool output.

```text
UNKNOWN ≠ OK
```

Unknown блокирует только затронутую boundary. Read-only analysis может продолжаться, если неизвестный факт не нужен для неё.

## Blocking finding

Finding является blocking, когда продолжение может нарушить scope, создать side effect без authority, скрыть false PASS, повредить canonical state, потерять данные или потребовать отсутствующее human decision.

После первого blocking finding текущая стадия формирует report и останавливается.

## Stop conditions

Типовые условия остановки:

- изменение вне allowed scope;
- baseline changed;
- unrelated dirty state;
- новая dependency;
- неразрешённый network;
- protected artifact;
- невозможная required validation;
- destructive side effect;
- architecture decision;
- отсутствующее human decision;
- environment mismatch.

## Scope expansion

Scope не расширяется автоматически. Текущая стадия останавливается, причина фиксируется, формируется bounded proposal, а расширение принимает человек.

## Validation failure

Validation не исправляет artifact. После `FAIL` формируется report, указывается одно следующее действие, а correction выполняется отдельной task.

## Recovery boundary

Recovery является временной. Она должна иметь конкретный объект, bounded scope, stop condition и критерий выхода.

Recovery не должна создавать self-referential approval chains или заменять Product reconstruction.

## Fail-closed

Fail-closed применяется в затронутой boundary, где продолжение создаёт реальный риск. Узкий unknown не должен блокировать независимую безопасную работу.

После completion, failure или blocking finding указывается ровно одно следующее действие.
