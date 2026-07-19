# 06.08.00 Scaling

## Назначение документа

Scaling описывает рост нагрузки, пользователей, projects, data и execution concurrency без преждевременного усложнения architecture.

## Measure Before Scale

Scale problem должен быть измерен.

Примеры signals:

- response time нарушает requirement;
- throughput недостаточен;
- storage растёт неприемлемо;
- concurrent writes создают conflicts;
- manual coordination стала bottleneck;
- provider limits регулярно нарушают workflow;
- operational cost непропорционален value.

Speculative scale не является requirement.

## Scaling Dimensions

Различаются:

- product users;
- active projects;
- repository size;
- artifact count;
- task concurrency;
- model calls;
- external integrations;
- validation workload;
- retained history.

Разные dimensions требуют разных решений.

## Vertical Before Distributed

Предпочтительный порядок:

1. удалить лишнюю работу;
2. упростить data flow;
3. добавить measurement;
4. оптимизировать локальные bottlenecks;
5. кэшировать только derived data;
6. разделить независимые read workloads;
7. вводить concurrency;
8. рассматривать distributed components.

## Concurrency

Parallel writes запрещены без специально принятой concurrency model.

До неё используется one-writer principle.

Read concurrency допустима, если results independently attributable и synthesis не скрывает conflicts.

## Queues and Workers

Queue или worker system вводится только при устойчивой asynchronous workload.

Необходимо определить:

- delivery semantics;
- idempotency;
- ordering;
- retries;
- dead-letter behavior;
- cancellation;
- observability;
- duplicate handling.

## Caching

Cache является derived state.

Он должен иметь:

- invalidation rule;
- version binding;
- rebuild;
- stale detection;
- bounded retention.

Cache miss не должен изменять canonical fact.

## Cost

Scaling decision учитывает:

- engineering complexity;
- operational burden;
- provider cost;
- latency;
- support;
- failure recovery;
- user value.

## Reliability

Reliability target выводится из Product Contract, а не из абстрактного стремления к максимальной availability.

## Legacy Boundary

Legacy scale mechanisms не переносятся без измеренной нагрузки нового AOS.
