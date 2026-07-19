# 06.06.00 External Integrations

## Назначение документа

External Integrations подключают AOS к внешним systems только после появления конкретного user journey или operational requirement.

Integration не является признаком product completeness.

## Integration Trigger

Integration рассматривается, если:

- существует accepted use case;
- external system участвует в observable user outcome;
- manual alternative доказанно создаёт значимую friction;
- integration scope ограничен;
- data ownership понятен;
- failure mode определён;
- отсутствие provider не разрушает core Product Runtime.

## Examples

Возможные candidates:

- Git hosting;
- issue tracker;
- email;
- calendar;
- document storage;
- CI provider;
- model provider;
- notification service;
- identity provider.

Список не является roadmap.

## Contract Boundary

Integration contract описывает:

- purpose;
- exact operations;
- read/write permissions;
- data classes;
- authentication;
- rate limits;
- timeout;
- retries;
- idempotency;
- error mapping;
- offline behavior;
- provider-specific assumptions;
- removal path.

## Least Privilege

Integration получает минимальные permissions.

Read-only use case не должен получать write permission.

Write operation требует exact scope и не получает Git или human decision authority автоматически.

## Secrets

Secrets:

- не хранятся в repository;
- не попадают в logs и reports;
- не передаются агенту без необходимости;
- имеют rotation и revocation path;
- не включаются в downloadable documentation packages.

## Network Boundary

Network включается explicit и bounded.

Должны быть известны:

- destination;
- purpose;
- data sent;
- data received;
- caching;
- retention;
- verification.

## Provider Independence

Core contracts должны минимизировать привязку к конкретному provider.

Provider adapter вводится при реальной вариативности, а не заранее.

## Failure and Degradation

Integration failure должна:

- быть видимой;
- не создавать false PASS;
- не терять local canonical state;
- не запускать destructive retry;
- иметь bounded retry;
- позволять manual fallback, когда это возможно.

## Data and Privacy

До integration определяются:

- data classification;
- minimum transfer;
- retention;
- deletion;
- audit;
- user consent;
- cross-border или regulatory constraints при наличии.

## Legacy Boundary

Старые integrations используются как источник:

- behavior examples;
- failure modes;
- tests;
- provider constraints.

Они не задают current provider choice или architecture.
