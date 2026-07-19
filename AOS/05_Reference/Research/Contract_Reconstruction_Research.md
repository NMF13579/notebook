# 07.04 — Contract Reconstruction Research

## Назначение

Документ определяет подход к извлечению candidate contracts из legacy behavior, документов и failure modes.

Контракт нового проекта должен описывать проверяемые границы и observable semantics, а не воспроизводить исторические schemas по умолчанию.

## Contract classes

### Product Contract

Определяет, что получает пользователь и какое поведение обязана обеспечивать система.

### Interaction Contract

Определяет вход, выход, допустимые состояния, ошибки и human checkpoints для конкретного interaction.

### Task Contract

Определяет bounded work unit, scope, validation и stop conditions.

### State Contract

Определяет значения состояний и запрещённые преобразования.

### Evidence Contract

Определяет, какие факты подтверждает Evidence и чего она не подтверждает.

### Git Action Contract

Разделяет edit, commit, push, merge и release authority.

### Handoff Contract

Определяет минимальный переносимый контекст между sessions и stages.

## Обязательные semantic invariants

```text
PASS ≠ approval.
Evidence ≠ approval.
CI PASS ≠ approval.
UNKNOWN ≠ OK.
NOT_RUN ≠ PASS.
BLOCKED ≠ PASS.
Plan output ≠ Task Brief.
Task Brief ≠ execution authorization.
Routing decision ≠ execution authorization.
Documentation ≠ technical completion.
Skeleton ≠ implementation.
Edit ≠ commit.
Commit ≠ push.
Push ≠ merge.
Merge ≠ release.
```

## Метод реконструкции contract

```text
observable behavior
→ actor and authority
→ preconditions
→ inputs
→ allowed transitions
→ outputs
→ failure semantics
→ negative guarantees
→ validation method
```

После этого legacy schema сравнивается с новым contract как один из implementation candidates.

## Contract quality test

Хороший contract:

- не зависит без необходимости от provider;
- проверяем;
- имеет bounded vocabulary;
- различает fact и decision;
- сохраняет unknown;
- указывает actor с authority;
- описывает negative behavior;
- не требует полной внутренней architecture;
- допускает replaceable implementation.

## Legacy contract disposition

Для каждого legacy contract выбирается одно:

```text
RETAIN_INTENT_REWRITE_CONTRACT
RETAIN_BEHAVIOR_SIMPLIFY_MECHANISM
KEEP_AS_REFERENCE
REJECT_AS_OVERCOMPLEX
REJECT_AS_UNSAFE
NEEDS_EXPERIMENT
```

`RETAIN` не означает копирование файла или schema.

## Validation

Contract считается кандидатом до проверки:

- consistency review;
- negative examples;
- edge cases;
- user journey mapping;
- implementation independence;
- conflict check с active Product Contracts;
- explicit human review.

## Promotion boundary

Принятый contract должен жить в соответствующем active разделе, а не в `07_Research`.

Research artifact сохраняет provenance и rationale, но не конкурирует с active Source of Truth.
