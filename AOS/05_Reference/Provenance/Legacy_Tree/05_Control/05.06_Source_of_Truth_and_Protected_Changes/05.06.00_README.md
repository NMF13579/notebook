# Source of Truth and Protected Changes

## Назначение

Один класс фактов должен иметь одного canonical owner. Цель — не единый registry, а отсутствие конфликтов между documentation, code, Git, chats, reports и legacy materials.

## Fact classes

Примеры:

- Project identity;
- Product intent;
- Product contracts;
- architecture decisions;
- implementation state;
- Git state;
- validation results;
- human decisions;
- dependencies;
- current task scope;
- release state.

## Canonical

Canonical artifact определяет факт для текущего проекта в своей boundary. Он не является автоматически approved, enforced или неизменяемым.

## Reference

AOS-FARM, AgentOS/AOS-1, legacy plans, raw chats и research являются reference.

```text
reference material
→ candidate insight
→ current-project analysis
→ human decision
→ возможное canonical правило
```

Reference не повышается до canonical автоматически.

## Derived artifacts

Generated index, cache, summary, report и visualization являются derived. При конфликте они пересоздаются из canonical source и не становятся вторым Source of Truth.

## Temporary artifacts

Temporary outputs хранятся в:

```text
/.aos-tmp/
```

Там нельзя хранить Evidence, approvals, checkpoints, canonical files, final reports или durable decisions.

## Git state

Branch, HEAD, index, working tree и history проверяются непосредственно. Chat statement или report не заменяет Git state.

## Human decisions

Record может сохранять решение, но автоматически созданный record не создаёт human decision.

## Protected changes

Protected classification назначается новым проектом. Она не наследуется из AOS-FARM.

К protected могут относиться Project identity, Product contracts, architecture foundations, authority model, Source of Truth rules, safety boundaries и release configuration.

Перед protected change определяются artifact, причина, impact, allowed/forbidden scope, validation и human checkpoint. Изменение выполняется отдельной bounded task и проверяется независимо.

## Conflicts и unknown ownership

При конфликте определяется fact class и current canonical owner. Reference или derived artifact не выбирается автоматически из-за нового timestamp.

Если ownership неизвестен, read-only analysis допускается, но mutation блокируется до human decision.

## Promotion из legacy

Для переноса legacy lesson необходимо сформулировать current-project problem, отделить contract от старой implementation, предложить минимальное новое правило и получить human decision.
