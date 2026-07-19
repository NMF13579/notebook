# Claims, Evidence, Review and Decisions

## Назначение

Документ разделяет:

```text
claim
observation
technical result
validation result
Evidence
review
human decision
approval
acceptance
```

## Claim

Claim — утверждение участника или инструмента: «файл исправлен», «tests проходят», «feature готова». Claim не является доказательством и должен быть подтверждён, обозначен как unverified или опровергнут.

## Observation

Observation — непосредственно наблюдаемый факт: `git diff`, exit code, содержимое файла, test output, branch или HEAD.

Observation ограничен фактически просмотренной boundary.

## Validation result

Допустимые состояния:

```text
PASS
FAIL
UNKNOWN
NOT_RUN
BLOCKED
```

`PASS` подтверждает только проверенное требование.

```text
UNKNOWN ≠ OK
NOT_RUN ≠ PASS
```

`FAIL` не запускает correction внутри validation. `BLOCKED` означает отсутствие prerequisite, authority или environment.

## Evidence

Evidence подтверждает конкретный claim и должно быть инспектируемым, ограниченным своей областью и не скрывать unknowns.

```text
Evidence ≠ approval
```

Объём Evidence пропорционален риску. Низкорисковая работа не требует тяжёлого package только ради формальности.

## Review

Review оценивает correctness, scope, architecture impact, product intent, risks и качество Evidence. Review остаётся read-only и может завершиться findings или рекомендацией revision.

Review не является acceptance без соответствующего human decision right.

## Approval и acceptance

Approval — явное human decision, разрешающее конкретное действие или признающее конкретный результат приемлемым.

Approval ограничено объектом, scope и стадией.

```text
planning approval ≠ execution authorization
result acceptance ≠ commit authorization
commit authorization ≠ push authorization
CI PASS ≠ merge authorization
merge ≠ release
```

## Documentation claims

Необходимо различать:

```text
planned
documented
implemented
validated
accepted
released
```

Запрещённые подмены:

```text
skeleton → implementation
documented contract → working runtime
test plan → executed validation
generated report → human decision
```

## Минимальная отчётность

Stage Report сообщает задачу, фактический результат, checks, findings, unknowns, невыполненные действия и одно следующее действие. Он не имитирует approval record.
