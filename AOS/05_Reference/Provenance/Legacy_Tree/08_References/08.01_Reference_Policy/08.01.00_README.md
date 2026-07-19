# Reference Policy

## Назначение

Этот документ определяет, как AOS использует исторические и внешние материалы при реконструкции проекта.

Reference помогает понять прошлый опыт. Reference не управляет новым проектом.

## Что считается Reference

Reference — это материал, который может содержать полезную информацию, но не обладает authority в новом AOS.

К reference относятся:

- старые repositories;
- historical branches и commits;
- прежняя документация;
- AgentOS и AOS-1 materials;
- AOS-FARM;
- research notes;
- внешние проекты;
- standards и specifications;
- статьи и книги;
- исторические чаты;
- rejected, superseded и obsolete artifacts.

## Reference и Source of Truth

`Reference` отвечает на вопрос:

> Откуда могла появиться идея или наблюдение?

`Source of Truth` отвечает на вопрос:

> Какое правило, contract или решение действует в новом проекте сейчас?

Reference не становится Source of Truth автоматически, даже если:

- материал ранее использовался в production;
- решение когда-то было approved;
- старые tests проходили;
- старый CI показывал PASS;
- документ назывался canonical;
- implementation существовала и работала.

Authority старого проекта не переносится между проектами.

## Reference и Research

Reference сохраняет исходный материал или его точное описание.

Research анализирует материалы, сравнивает варианты и формирует гипотезы.

Research output также не является project decision, Task Brief, approval или execution authorization.

## Reference и Archive

Reference используется как потенциальный источник знаний.

Archive хранит материалы, которые больше не должны участвовать в активной работе, но сохраняются для истории, traceability или предотвращения повторения ошибок.

## Разрешённое извлечение

Из reference можно извлекать:

- product intent;
- user problems;
- user journeys;
- observable behavior;
- contracts;
- acceptance examples;
- successful patterns;
- failure modes;
- rejected approaches и причины отказа;
- safety lessons;
- operational lessons;
- UX lessons;
- dependency lessons;
- architecture trade-offs;
- migration constraints.

## Запрещённый автоматический перенос

Нельзя автоматически переносить:

- architecture;
- repository topology;
- directory structure;
- implementation;
- dependencies;
- schemas;
- Control Plane;
- registry;
- database model;
- lifecycle;
- approval records;
- Risk Profiles;
- execution authority;
- CI configuration;
- release process;
- security assumptions;
- claims о readiness.

Каждый такой элемент должен быть заново обоснован в контексте нового проекта.

## Правило независимой формулировки

Знание, принятое новым AOS, должно быть сформулировано как самостоятельный contract или project rule.

Canonical документы нового проекта не должны требовать наличия старого repository для понимания обязательного поведения.

Допустимо указывать provenance. Недопустимо делегировать meaning или authority внешнему source.

## Правило проверки

Перед переносом знания необходимо проверить:

1. Какую реальную проблему оно решало.
2. Было ли поведение подтверждено или только заявлено.
3. Какие assumptions существовали.
4. Какие failure modes наблюдались.
5. Сохраняются ли исходные constraints.
6. Не существует ли более простого решения.
7. Не переносится ли вместе с пользой лишняя сложность.
8. Можно ли выразить знание как testable rule или observable contract.

## Human authority

Агент может:

- находить источники;
- извлекать факты;
- сравнивать варианты;
- выявлять противоречия;
- предлагать формулировки;
- указывать uncertainty.

Агент не может:

- объявлять reference canonical;
- назначать Source of Truth;
- симулировать human acceptance;
- назначать Risk Profile;
- расширять scope;
- разрешать implementation;
- переносить protected decisions без human checkpoint.

## Базовые инварианты

```text
Reference ≠ Source of Truth
Historical approval ≠ current approval
Legacy PASS ≠ current PASS
Evidence ≠ approval
Documentation ≠ implementation
Similarity ≠ compatibility
Copying ≠ reconstruction
```

## Критерий успешного использования Reference

Reference использован правильно, если новый проект получил полезное, проверяемое знание и при этом остаётся независимым от старой implementation, authority и topology.
