# 06.03.00 Automation Principles

## Назначение документа

Automation Principles определяет, когда и как повторяемая ручная операция может стать assisted или automated capability.

Automation не является целью сама по себе.

## Maturity Path

```text
manual
→ repeatable
→ documented
→ assisted
→ controlled automation
→ justified enforcement
```

Каждый следующий уровень требует доказанной недостаточности предыдущего.

## Manual First

Manual cycles нужны для обнаружения:

- реальных steps;
- обязательных inputs;
- useful outputs;
- исключений;
- failure modes;
- human decisions;
- stop conditions.

Автоматизация процесса, который ещё не понят, закрепляет ошибки и увеличивает cost of change.

## Automation Candidate Test

Операция может стать candidate, если:

- выполнялась вручную несколько раз;
- inputs и outputs стабильны;
- правила достаточно детерминированы;
- failure detectable;
- consequences bounded;
- result independently verifiable;
- human boundary ясна;
- operation не скрывает uncertainty;
- существует disable и removal path.

## Preferred Automation Order

Сначала автоматизируются:

- read-only fact collection;
- structure checks;
- deterministic validation;
- missing-field detection;
- hashes и identity checks;
- report formatting;
- navigation и search indexes;
- candidate package preparation.

Позже могут рассматриваться controlled writes.

## Human Decisions

Automation не принимает:

- Scope expansion;
- Risk Profile assignment;
- architecture acceptance;
- protected change authorization;
- destructive operation authorization;
- execution authorization;
- Commit, Push, Merge или Release authorization.

Она может подготовить decision package, но не подменяет человека.

## Bounded Automation

Каждый automated run должен иметь:

- exact subject;
- exact scope;
- known baseline;
- permissions;
- expected outputs;
- stop conditions;
- timeout или bounded attempt policy;
- explicit failure state;
- report;
- отсутствие automatic stage transition.

Один run выполняет один stage.

## Failure Behavior

Automation должна:

- завершаться non-zero или explicit failure state при blocking failure;
- не преобразовывать `UNKNOWN` в `OK`;
- не считать skipped check успешным;
- не исправлять findings во время independent validation;
- не запускать бесконечные retries;
- не продолжать после scope drift;
- сохранять partial result только как факт, не как PASS.

## Retry Policy

Retry разрешён только когда:

- причина transient;
- повтор безопасен;
- attempts bounded;
- повтор не меняет authority;
- каждая попытка observable.

Repeated repair loop не должен становиться hidden lifecycle.

## Network

Network default — disabled.

Network включается только когда:

- операция действительно требует external data;
- разрешён exact purpose;
- определены hosts или service boundary;
- исключена передача secrets;
- result проверяем;
- отсутствие сети имеет ясный status.

## Agent Orchestration

Parallel read-only analysis может использоваться для независимых вопросов.

Parallel write agents запрещены.

Orchestrator не получает authority только потому, что координирует других агентов.

## Success Measure

Automation успешна, если она:

- уменьшает повторяемую работу;
- не увеличивает ambiguity;
- не замедляет user-facing progress;
- не создаёт новый Source of Truth;
- сохраняет human authority;
- легко отключается;
- делает failures заметнее, а не скрывает их.

## Legacy Lesson

AOS-FARM показал риск проектирования automation раньше успешных manual cycles и превращения unfinished Control Plane в prerequisite собственной разработки.

Новый AOS не импортирует этот порядок.
