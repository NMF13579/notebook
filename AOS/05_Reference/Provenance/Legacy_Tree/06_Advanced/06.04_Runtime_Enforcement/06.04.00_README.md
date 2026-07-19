# 06.04.00 Runtime Enforcement

## Назначение документа

Runtime Enforcement физически предотвращает конкретные forbidden actions в подтверждённых high-impact boundaries.

Он вводится позднее documentation rules, manual checks и controlled automation.

## Rule

```text
guideline
≠
automatic requirement for Runtime Enforcement
```

Enforcement оправдан, когда нарушение:

- повторяется;
- имеет значимый impact;
- не предотвращается более простым механизмом;
- может быть определено детерминированно;
- может быть заблокировано без недопустимых false positives;
- имеет ясный recovery path.

## Enforcement Candidates

Возможные поздние boundaries:

- protected path writes;
- destructive commands;
- unauthorized Git actions;
- secret leakage;
- exact baseline mismatch;
- invalid execution package;
- expired capability;
- forbidden network access;
- scope violation;
- mutation during read-only validation.

Этот список не является implementation scope.

## Advisory Before Enforced

Предпочтительный путь:

```text
document rule
→ manual review
→ advisory check
→ measure violations
→ bounded enforcement trial
→ independent evaluation
```

## Fail-Closed Boundary

Fail-closed применяется внутри конкретной protected boundary.

Он не должен превращать любой unknown в глобальную остановку низкорискового read-only анализа.

При enforcement failure система должна:

- назвать blocking condition;
- не выполнять forbidden action;
- сохранить facts;
- не infer approval;
- показать одно следующее действие;
- остановиться.

## Human Authority

Runtime Enforcement не создаёт approval.

Успешная проверка означает только, что известные machine-checkable conditions выполнены.

```text
enforcement PASS
human decision: NOT_RECORDED
```

является допустимым состоянием.

## Capability and Identity

Если используются execution packages, tokens, nonce, expiration или digest binding, они должны:

- иметь точный subject;
- быть связаны с repository, branch и baseline;
- иметь ограниченный scope;
- иметь expiration;
- не расширяться автоматически;
- не переноситься между задачами;
- не означать Commit, Push, Merge или Release authorization.

Такие механизмы являются candidate design, а не обязательной foundation.

## Bypass

Bypass не должен быть скрытым.

Любое исключение требует:

- identity;
- reason;
- bounded scope;
- human authorization;
- expiration;
- auditability.

## Recovery

Enforcement не должен создавать recovery system сложнее защищаемой операции.

Recovery path должен быть коротким, понятным и не требовать симуляции approvals.

## Validation

Проверяются:

- positive cases;
- negative cases;
- false-positive risk;
- false-negative risk;
- baseline mismatch;
- expiration;
- partial failure;
- bypass;
- portability;
- uninstall или disable path.

## Legacy Boundary

Legacy enforcement ideas могут использоваться как research candidates.

Они не получают active authority и не копируются вместе со старым lifecycle или recovery coupling.
