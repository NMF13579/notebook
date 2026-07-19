# 06.05.00 Registries and Indexes

## Назначение документа

Документ разделяет lightweight navigation indexes, derived registries и authoritative state.

Registry не создаётся по умолчанию.

## Start Without Central Registry

Начальный AOS использует:

- predictable paths;
- Markdown;
- Git;
- локальные manifests при необходимости;
- явные links;
- ограниченные reports;
- search по repository.

Central registry рассматривается только после появления подтверждённой query, consistency или drift problem.

## Index

Index помогает находить canonical artifacts.

Он должен быть:

- generated или легко восстанавливаемым;
- derived;
- non-authoritative;
- проверяемым;
- удаляемым без потери facts.

Если index конфликтует с canonical source, побеждает canonical source.

## Registry Admission

Registry может рассматриваться, если:

- object classes стабильны;
- queries повторяются;
- ручная навигация доказанно недостаточна;
- consistency невозможно обеспечить simpler checks;
- ownership каждой fact class известен;
- rebuild strategy существует;
- stale state обнаружим;
- registry не становится скрытым approval system.

## One Source of Truth per Fact Class

До создания registry составляется карта:

| Fact class | Canonical source | Derived view | Conflict behavior |
|---|---|---|---|

Один факт не должен независимо редактироваться в нескольких местах.

## Database Boundary

Database оправдана только при доказанной потребности в:

- runtime persistence;
- concurrency;
- transactional consistency;
- query volume;
- event processing;
- multi-user operational state.

Database не вводится только ради «серьёзной architecture».

Markdown/YAML и Git остаются предпочтительными для human-readable project knowledge, пока они достаточны.

## Drift

Drift означает расхождение derived representation с canonical source.

Drift detection должна:

- указывать exact objects;
- не исправлять canonical content автоматически;
- не считать stale registry новым truth;
- поддерживать rebuild;
- отделять missing data от invalid data.

## Lifecycle Risk

Registry не должна незаметно вводить новую lifecycle model.

Добавление статусов, transitions и ownership требует отдельного обоснования и human decision.

## Migration

Bulk census legacy artifacts запрещён по умолчанию.

Импортируется только то, что:

- нужно новому продукту;
- имеет provenance;
- прошло classification;
- имеет accepted target contract;
- не переносит legacy authority.

## Removal

Registry должна иметь export или rebuild path.

Удаление registry не должно уничтожать canonical knowledge.
