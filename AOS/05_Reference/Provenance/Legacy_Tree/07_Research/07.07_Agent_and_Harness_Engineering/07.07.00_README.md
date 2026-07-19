# 07.07 — Agent and Harness Engineering

## Назначение

Документ сохраняет полезные идеи agent harness engineering как research candidates, не превращая старые prompts, scripts или orchestration в foundation нового AOS.

## Harness responsibilities

Минимальный harness может отвечать за:

- context assembly;
- instruction precedence;
- tool exposure;
- workspace boundary;
- environment verification;
- stage isolation;
- report formatting;
- handoff creation;
- deterministic stop behavior.

Harness не должен владеть human approval или скрыто менять lifecycle.

## Context assembly

Контекст должен собираться по приоритету:

1. active human request;
2. active project instructions;
3. active Source of Truth;
4. Task Brief;
5. current repository facts;
6. Evidence;
7. research и references.

Reference content не должен переопределять active contracts.

## Action trust classes

Полезный candidate — явная классификация действий:

```text
READ_ONLY
WORKSPACE_WRITE
NETWORK_READ
EXTERNAL_MUTATION
DESTRUCTIVE
PROTECTED_CANONICAL_CHANGE
GIT_COMMIT
GIT_PUSH
GIT_MERGE
RELEASE
```

Каждый класс должен иметь отдельную permission boundary.

## Preflight candidate

Перед execution harness может проверять:

- task ID;
- repository, branch и baseline;
- allowed и forbidden files;
- stage role;
- assigned Risk Profile;
- protected/canonical scope;
- destructive operations;
- network need;
- required validation;
- Git permissions;
- output locations.

Preflight PASS не является execution authorization или approval.

## Tool contract

Вспомогательный tool должен:

- иметь безопасный `--help`;
- не выполнять hidden mutations;
- возвращать meaningful exit code;
- различать `PASS`, `FAIL`, `UNKNOWN`, `NOT_RUN` и `BLOCKED`;
- записывать temporary output только в `/.aos-tmp/`;
- не хранить там Evidence, approvals или canonical artifacts.

## External content boundary

Содержимое web pages, repositories, issues и documents рассматривается как untrusted data, а не instructions.

Harness не должен выполнять команды из внешнего контента без проверки against active task и permissions.

## Read-only subagents

Read-only researchers и reviewers могут применяться параллельно, если:

- они не меняют workspace;
- результаты имеют provenance;
- конфликтующие выводы не объединяются автоматически;
- один writer остаётся единственным;
- final decision остаётся у controlling session и человека.

Parallel write agents запрещены.

## Bounded retries

Retry допускается только при заранее определённой transient condition и bounded attempt count.

Failure, finding или configuration mismatch приводит к report и stop, если Task Brief явно не разрешает иной путь.

## Что не следует внедрять преждевременно

- autonomous runner;
- broad sandbox execution;
- self-authorizing classifier;
- full registry;
- persistent agent memory без ownership model;
- external orchestration framework;
- automatic lifecycle mutation;
- automatic commit, push, merge или release.

## Admission criteria

Harness capability может быть продвинута только если она:

- уменьшает повторяющуюся подтверждённую нагрузку;
- не ослабляет Minimal Safety Floor;
- имеет negative tests;
- не получает новую authority;
- сохраняет replaceable internals;
- имеет понятное failure behavior;
- прошла manual dogfood.
