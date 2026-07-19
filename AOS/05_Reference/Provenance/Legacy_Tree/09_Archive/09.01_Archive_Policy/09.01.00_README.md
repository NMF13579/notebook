# 09.01 — Archive Policy

## Назначение

Archive Policy определяет, когда и как artifacts нового AOS выводятся из active knowledge.

Политика должна:

- сохранять историю без сохранения устаревшей authority;
- предотвращать скрытое возвращение superseded решений;
- отделять archive от references, research и temporary workspace;
- сохранять причины решений;
- поддерживать воспроизводимость развития проекта;
- превращать прошлые ошибки в доступные lessons, а не в действующие правила.

## Область действия

Политика применяется к собственным artifacts нового AOS:

- documentation;
- project plans;
- proposals;
- architecture alternatives;
- workflow descriptions;
- temporary recovery materials;
- implementation-oriented design artifacts;
- локальным правилам, которые были заменены или отменены.

Политика не превращает AOS-FARM, AgentOS или AOS-1 в часть active history нового проекта.

Для legacy materials действует граница:

```text
source_class: REFERENCE
authority: NONE
active_by_default: false
```

## Классы архивирования

### Superseded

Artifact был active или принят для использования, но позднее заменён другим artifact.

Примеры:

- предыдущий product contract;
- заменённое architecture decision;
- прежняя структура документации;
- workflow, заменённый более точной версией.

Superseded artifact должен указывать replacement либо объяснять, почему replacement отсутствует.

### Rejected

Artifact был предложен и рассмотрен, но не был принят.

Rejected artifact нельзя описывать так, будто он когда-либо был active.

### Obsolete

Artifact потерял применимость из-за изменения контекста, scope, technology, assumptions или project direction.

Obsolete не обязательно означает, что artifact был ошибочным в момент создания.

### Closed Temporary

Artifact выполнял временную функцию и больше не должен управлять проектом.

Примеры:

- recovery plan;
- stabilization checklist;
- migration note;
- incident-specific workaround;
- temporary reconciliation procedure.

Temporary solution не должна становиться permanent architecture только из-за длительного существования.

## Условия архивирования

Artifact может быть архивирован, когда выполнено хотя бы одно условие:

- существует принятый replacement;
- предложение явно отклонено;
- assumptions потеряли актуальность;
- временная задача завершена;
- artifact больше не соответствует project scope;
- artifact дублирует active Source of Truth;
- artifact создаёт риск противоречивой authority.

Архивирование не должно использоваться для сокрытия:

- unresolved finding;
- validation failure;
- unknown;
- disagreement;
- отсутствующего human decision;
- недостатка Evidence.

## Обязательная информация

Для каждого durable archived artifact должна быть понятна следующая информация:

- исходное назначение;
- категория архивирования;
- причина вывода из active use;
- был ли artifact когда-либо active или approved;
- replacement, если он существует;
- lessons learned;
- ограничения повторного использования;
- возможность повторного рассмотрения;
- дата или Git reference, позволяющие восстановить контекст.

На текущем documentation stage эта информация может быть записана в Markdown без служебного YAML.

## Граница authority

Архивный artifact не является:

- current Source of Truth;
- execution authorization;
- implementation authorization;
- approval;
- active contract;
- current architecture;
- current lifecycle state;
- доказательством readiness.

```text
Archived PASS ≠ current PASS.
Archived Evidence ≠ current Evidence.
Archived approval ≠ approval нового решения.
Historical decision ≠ current decision.
```

## Legacy boundary

AOS-FARM и AgentOS/AOS-1 не архивируются как бывшие части нового AOS.

Допустимый путь использования legacy knowledge:

```text
reference
→ observation
→ analysis
→ extracted lesson
→ independent project proposal
→ explicit human decision
→ active new-project artifact
```

Недопустимый путь:

```text
legacy file
→ copy
→ rename
→ declare active
```

Из legacy material можно извлекать:

- product intent;
- observable behavior;
- failure modes;
- anti-patterns;
- useful constraints;
- lessons;
- hypotheses для новой проверки.

Нельзя автоматически наследовать:

- architecture;
- topology;
- schemas;
- dependencies;
- statuses;
- approval history;
- lifecycle;
- Control Plane;
- registry;
- automation model;
- recovery procedures;
- implementation details.

## Архивирование и Git

Git history и Archive решают разные задачи.

Git history показывает:

- какие изменения были сделаны;
- когда;
- в каком commit;
- кем был создан commit.

Archive объясняет:

- почему artifact перестал быть active;
- чем он был заменён;
- какие lessons следует сохранить;
- какие ограничения действуют на повторное использование.

Поэтому Git history не заменяет Archive, а Archive не заменяет Git history.

## Перемещение и копирование

Предпочтительная модель:

- active artifact остаётся в active tree до явного replacement decision;
- после решения он перемещается или воспроизводится в соответствующем archive object;
- active links обновляются отдельно;
- исходный контекст сохраняется;
- массовая ренумерация не выполняется;
- history не переписывается без отдельной необходимости.

Destructive removal требует explicit human authorization.

## Возврат из Archive

Archived artifact нельзя просто вернуть в active tree.

Перед возвратом необходимо:

1. проверить текущий контекст;
2. определить, сохранились ли assumptions;
3. сравнить artifact с active Source of Truth;
4. проверить lessons и причины архивирования;
5. сформировать новое предложение;
6. провести отдельное human decision.

Возвращённый artifact становится новым решением, а не продолжением старой authority.

## Отсутствие replacement

Иногда artifact выводится из active use без прямой замены.

В этом случае необходимо явно указать:

- почему replacement не требуется;
- какая capability или rule удалена;
- какие последствия ожидаются;
- не остаётся ли gap;
- требуется ли future decision.

`No replacement` не означает `no impact`.

## Неопределённость

Если невозможно определить правильную категорию:

```text
UNKNOWN ≠ archived.
```

Artifact должен оставаться на месте либо быть помещён в bounded review area, но не классифицироваться как superseded, rejected или obsolete без основания.

## Human authority

Решение об архивировании artifacts, влияющих на:

- canonical knowledge;
- architecture;
- product contracts;
- governance;
- lifecycle;
- protected rules;
- destructive operations;

требует human checkpoint.

Агент может:

- выявить кандидата;
- предложить категорию;
- собрать связи;
- сформулировать lessons;
- подготовить draft.

Агент не может симулировать решение человека.

## Кратчайший безопасный путь

```text
identify candidate
→ determine class
→ preserve context
→ identify replacement
→ record lessons
→ human checkpoint when required
→ move out of active knowledge
→ stop
```

Не следует одновременно:

- архивировать artifact;
- переписывать replacement;
- менять architecture;
- исправлять implementation;
- выполнять commit;
- выполнять push;
- выполнять merge.

Один запуск выполняет один этап.
