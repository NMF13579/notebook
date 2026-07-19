# 09 — Archive

## Назначение раздела

Раздел `09_Archive` хранит выведенную из active use историю нового AOS.

Он нужен для того, чтобы:

- сохранять причины и контекст прошлых решений;
- не терять lessons learned;
- отделять действующее знание от заменённого, отклонённого или утратившего применимость;
- не позволять устаревшим материалам незаметно возвращаться в роль Source of Truth;
- поддерживать воспроизводимость развития проекта;
- предотвращать повторение уже выявленных ошибок.

Archive не является мусорной корзиной и не является хранилищем legacy repositories.

## Фундаментальная граница

Старые проекты и материалы:

- `NMF13579/AOS-FARM`;
- AgentOS;
- AOS-1;
- прежние chats, audits, reports и raw notes;

используются только как:

```text
role: READ_ONLY_REFERENCE
authority: NONE
```

Они принадлежат разделу `08_References`, а не становятся бывшими нормативными частями нового AOS.

Новый AOS наследует не authority, topology и implementation старого проекта, а только проверяемые знания, извлечённые из его опыта.

```text
legacy observation
→ проверка контекста
→ lesson learned
→ новая формулировка проблемы
→ самостоятельное решение нового проекта
→ active artifact нового AOS
```

## Что хранится в Archive

Раздел предназначен для собственных artifacts нового проекта:

- superseded documents;
- rejected proposals;
- obsolete project plans;
- closed temporary artifacts;
- записи о причинах архивирования и replacement links.

Artifact может считаться архивным только после того, как он перестал быть active knowledge.

## Что не хранится в Archive

В Archive не помещаются:

- legacy repositories как foundation;
- raw external references;
- active canonical documents;
- Evidence, требующее durable active custody;
- approval records, остающиеся частью действующего governance trail;
- незавершённые материалы без понятной классификации;
- временные outputs из `/.aos-tmp/`;
- файлы, которые просто неудобно классифицировать;
- secrets;
- generated caches;
- материалы, удалённые только ради уменьшения видимости проблемы.

## Связь с соседними разделами

### `07_Research`

Используется для анализа:

- lessons;
- alternatives;
- hypotheses;
- failure modes;
- future ideas.

Research не становится автоматически active decision.

### `08_References`

Используется для хранения и описания исходных материалов:

- legacy repositories;
- historical documents;
- chats;
- audits;
- external sources;
- raw source material.

Reference не является authority.

### `09_Archive`

Используется для истории уже нового проекта:

- что было active;
- что было предложено;
- что было заменено;
- что было отклонено;
- что завершило временную функцию.

## Структура раздела

```text
09_Archive/
├── 09.00_README.md
├── 09.01_Archive_Policy/
├── 09.02_Superseded_Project_Artifacts/
├── 09.03_Rejected_Project_Proposals/
├── 09.04_Obsolete_Project_Plans/
├── 09.05_Closed_Temporary_Artifacts/
└── 09.06_Archive_Register/
```

## Основные инварианты

```text
Archived ≠ active.
Archived ≠ approved.
Reference ≠ authority.
Historical existence ≠ current validity.
Previous PASS ≠ current PASS.
Evidence ≠ approval.
CI PASS ≠ approval.
UNKNOWN ≠ OK.
NOT_RUN ≠ PASS.
```

Дополнительно:

- архивирование не меняет историю Git;
- архивирование не подтверждает правильность artifact;
- архивирование не отменяет необходимость replacement;
- artifact без replacement не становится автоматически удалённым;
- возвращение artifact в active knowledge требует нового рассмотрения;
- human approval cannot be simulated;
- scope не расширяется через восстановление старого artifact;
- legacy solution не активируется только потому, что аналогичная проблема появилась снова.

## Навигация

- `09.01_Archive_Policy` — правила архивирования.
- `09.02_Superseded_Project_Artifacts` — заменённые active artifacts.
- `09.03_Rejected_Project_Proposals` — рассмотренные, но не принятые предложения.
- `09.04_Obsolete_Project_Plans` — планы, утратившие применимость.
- `09.05_Closed_Temporary_Artifacts` — завершённые временные материалы.
- `09.06_Archive_Register` — будущий реестр архивных записей.

## Критерий корректности раздела

Раздел работает правильно, если пользователь может однозначно понять:

- почему artifact больше не active;
- был ли он когда-либо принят;
- что пришло ему на смену;
- какие lessons следует сохранить;
- можно ли повторно рассматривать artifact;
- почему legacy material не является Source of Truth нового проекта.
