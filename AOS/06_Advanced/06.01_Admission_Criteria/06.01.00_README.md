# 06.01.00 Advanced Capability Admission Criteria

## Назначение документа

Этот документ определяет единый admission contract для любой capability раздела `06_Advanced`.

Ни одна advanced capability не считается обязательной только потому, что она перечислена в документации.

## Admission Principle

Новая capability допускается только когда подтверждено:

```text
реальная проблема существует
∧ проблема повторяется
∧ текущий простой механизм недостаточен
∧ последствия автоматизации ограничены
∧ результат проверяем
∧ failure обнаружим
∧ human boundary сохранена
∧ существует removal path
```

Если хотя бы одна обязательная часть неизвестна, решение не подменяется предположением.

## Required Problem Statement

Proposal должен определить:

- какого пользователя или operator затрагивает проблема;
- в каком workflow она возникает;
- как часто повторяется;
- какие потери создаёт;
- какие Evidence подтверждают проблему;
- почему это root cause, а не симптом;
- относится ли проблема к Product Runtime, Development Factory или Control;
- почему решение должно находиться именно в AOS.

Нельзя обосновывать capability только словами:

- «так надёжнее»;
- «так масштабируемее»;
- «это стандартная architecture»;
- «так было в AOS-FARM»;
- «это понадобится позже».

## Required Prior Experience

До admission должны существовать несколько bounded manual cycles, достаточных для понимания:

- stable inputs;
- stable outputs;
- recurring decisions;
- failure modes;
- human checkpoints;
- исключений;
- реальной стоимости ручной операции.

Один cycle может выявить гипотезу, но не формирует устойчивый automation contract.

## Simpler Alternatives

До создания subsystem рассматриваются более простые варианты:

1. уточнить правило;
2. исправить documentation;
3. улучшить template;
4. добавить checklist;
5. добавить local deterministic check;
6. создать read-only helper;
7. использовать bounded script;
8. автоматизировать только стабильную часть;
9. отказаться от capability.

Выбранный вариант должен быть минимальным достаточным изменением.

## Capability Proposal

Bounded proposal должен описывать:

- objective;
- expected user or operational outcome;
- allowed scope;
- forbidden scope;
- affected contracts;
- canonical Source of Truth;
- derived artifacts;
- permissions;
- network requirements;
- data retention;
- trust boundaries;
- failure behavior;
- stop conditions;
- validation strategy;
- rollback или removal path;
- known unknowns;
- rejected alternatives.

Proposal не является Task Brief, approval или execution authorization.

## Authority Test

Capability не должна:

- симулировать human approval;
- назначать Risk Profile;
- самостоятельно расширять Scope;
- превращать recommendation в decision;
- трактовать PASS как acceptance;
- разрешать Commit, Push, Merge или Release;
- изменять protected/canonical state без human checkpoint;
- выполнять destructive operation без explicit authorization.

## Source of Truth Test

До admission должно быть явно определено:

- какая fact class затрагивается;
- где находится её canonical source;
- является ли новый output canonical или derived;
- как выявляется conflict;
- какой source побеждает;
- как восстанавливается derived state.

Generated index, cache, dashboard или registry не должны незаметно становиться вторым Source of Truth.

## Complexity Budget

Для каждого нового component необходимо ответить:

1. Какую recurring problem он решает?
2. Почему текущий manual или lightweight process недостаточен?
3. Какова минимальная реализация?
4. Какие новые failure modes он создаёт?
5. Каков blast radius ошибки?
6. Как проверить корректность?
7. Как отключить или удалить component?
8. Что произойдёт с Product Runtime после удаления?

Если Product Runtime перестаёт работать без внутренней Development Factory capability, граница слоёв требует пересмотра.

## Trial

Первое внедрение должно быть:

- bounded;
- reversible;
- observable;
- isolated;
- минимальным;
- без необязательной migration;
- без bulk conversion legacy artifacts;
- без расширения на соседние workflows.

Trial не означает принятие capability как permanent standard.

## Validation

Validation выполняется отдельно от implementation и проверяет:

- заявленный outcome;
- отсутствие scope expansion;
- correct failure handling;
- preservation of human authority;
- Source of Truth consistency;
- reproducibility;
- removal path;
- отсутствие ложного PASS;
- влияние на user-facing progress.

Validation не исправляет implementation.

## Admission Outcomes

Возможные human decisions:

- `ADMIT_FOR_BOUNDED_TRIAL`;
- `NEEDS_REVISION`;
- `DEFER`;
- `REJECT`;
- `REMOVE_AFTER_TRIAL`.

Technical PASS не выбирает решение автоматически.

## Stop Conditions

Работа останавливается, если обнаружено:

- отсутствие подтверждённой проблемы;
- неясный Source of Truth;
- неназначенный required Risk Profile;
- необходимость расширить scope;
- destructive migration без authorization;
- скрытая зависимость Product Runtime от Development Factory;
- невозможность обнаружить failure;
- отсутствие rollback или removal path;
- попытка импортировать legacy authority;
- конфликт с protected/canonical contract.

## Legacy Use

Legacy может предоставить:

- пример;
- negative lesson;
- candidate test;
- observed behavior;
- failure mode.

Legacy не предоставляет admission.

Сходство с AOS-FARM не является Evidence необходимости capability в новом проекте.
