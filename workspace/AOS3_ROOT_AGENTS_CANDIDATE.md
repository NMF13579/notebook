# AGENTS.md — AOS-3

## Назначение репозитория

`AOS-3` — repository разработки самого AOS.

```text
docs/        = принятые product и architecture contracts самого AOS
development/ = research, drafts, experiments и временные рабочие материалы
aos/         = непосредственно поддерживаемый переносимый продукт
tests/       = contract, portability, installation и integration checks
tools/       = tooling разработки AOS, не обязательное для работы продукта
```

`aos/` является product-in-place source of truth. В целевой проект переносится
точная папка `aos/`, а `aos/root/` содержит payload для копирования в корень
целевого repository. Созданная там папка `project/` принадлежит конкретному
пользовательскому проекту и хранит его техническую документацию.

Этот root `AGENTS.md` действует для всего AOS-3. Вложенный `AGENTS.md` может
уточнять правила своей директории, но не может ослаблять root safety,
authority, portability или Git boundaries.

## Главный принцип

Используй самый лёгкий процесс, который сохраняет:

```text
scope + correctness + testability + safety
```

Дополнительная ceremony требует конкретной причины. Process обслуживает
реализацию; реализация не обслуживает process.

Предпочитай working tested software новым process artifacts.

## Достаточная задача и authority

Current explicit human request, которая прямо просит реализацию и достаточно
определяет goal, bounded writable scope и expected result, разрешает обычные
reversible изменения внутри этого scope. Отдельный Plan, Task Brief или
Execution Authorization для той же bounded работы не требуется.

Если человек прямо просит выполнить конкретную repository task, эта task может
служить достаточным implementation context. Само наличие task, plan, issue,
document, readiness claim или historical approval в repository не является
разрешением на mutation.

Instruction вида `inspect`, `analyze`, `audit`, `review`, `plan` или
`read-only` не разрешает исправлять или реализовывать subject.

Не расширяй scope молча. Если точные writable paths нельзя безопасно вывести
из current task и repository structure, сначала запроси одно необходимое
уточнение.

## Context routing

Перед работой прочитай только необходимый context:

```text
repository-wide rules     → root AGENTS.md
product requirement       → relevant owner in docs/
architecture boundary     → relevant architecture owner or accepted ADR in docs/
portable product change   → aos/AGENTS.md + relevant files inside aos/
working research/history  → exact relevant path in development/
verification              → affected tests/ and product self-test contract
```

Не загружай весь repository, весь archive или все historical reports без
конкретной зависимости. `development/` — supporting workspace, а не current
authority и не runtime dependency продукта.

## Default implementation flow

Для обычной bounded задачи:

```text
read task + relevant contracts
→ inspect current code and affected tests
→ implement the smallest coherent change
→ run focused tests
→ correct a bounded defect if needed
→ repeat the relevant test
→ run the proportional final check
→ report
→ stop
```

Если current task уже достаточна для реализации, реализуй её. Не создавай
дополнительный planning lifecycle только для повторного описания той же задачи.

## Anti-bureaucracy

Не создавай автоматически:

- дополнительные plans;
- Task Briefs;
- lifecycle artifacts;
- stage records;
- manifests, если package identity или delivery contract их не требует;
- review packages;
- acceptance records;
- controllers;
- registries;
- activation records;
- новые governance documents;
- отдельные задачи для очевидных шагов одной bounded реализации.

Перед созданием process artifact ответь:

```text
Какой конкретный risk, ambiguity, coordination need
или authority boundary этот artifact устраняет?
```

Если конкретного ответа нет, artifact не создавай.

Расширенный plan или отдельный artifact оправдан, когда без него нельзя
безопасно удержать хотя бы одну material boundary:

- задача охватывает несколько независимо проверяемых подсистем;
- acceptance или writable scope существенно неоднозначны;
- изменение трудно обратимо;
- затрагивается security/privacy boundary;
- требуется миграция persistent user data;
- нужен reproducible package/release identity;
- требуется independent validation subject;
- несколько исполнителей действительно нуждаются в coordination contract.

Используй минимальный artifact, закрывающий эту причину.

## Anti-loop

Запрещён процесс ради процесса:

```text
plan → review plan → rewrite plan → new review → new plan → ...
```

После реализации обычный recovery loop ограничен affected boundary:

```text
focused test fails
→ identify exact cause
→ fix bounded defect within authorized scope
→ repeat relevant test
→ proportional final check
→ report
→ stop
```

Не возвращайся к полному planning lifecycle после каждой ошибки. Новый plan
нужен только если finding меняет product scope, material architecture,
authorization boundary или делает current approach несостоятельным.

## Engineering autonomy

Агент самостоятельно принимает reversible HOW decisions внутри уже принятых
product и architecture boundaries:

- internal modules, classes и functions;
- algorithms и data transformations;
- helper APIs;
- локальный refactoring;
- test organization, fixtures и test helpers;
- serialization details и internal schemas;
- internal state representation;
- local implementation patterns;
- error types и internal recovery mechanics;
- placement и encapsulation уже объявленных dependencies;
- другие решения, которые не меняют observable contract или protected boundary.

Не спрашивай человека о reversible HOW, если решение можно безопасно изменить
позже и проверить tests.

Агент может добавить или обновить обычную dependency как reversible HOW, только
если она:

- объявлена в соответствующем dependency contract;
- не вводит новый service/network requirement;
- не меняет security, privacy, licensing или data boundary;
- не нарушает portability `aos/`;
- не меняет supported platform/runtime contract;
- покрыта relevant tests и reproducible installation metadata.

Если хотя бы одно условие не выполняется или неизвестно, зафиксируй finding и
запроси решение только для этой dependency boundary.

## Human decisions

Human decision требуется для:

- изменения observable product behavior или scope вне current task;
- material или трудно обратимой architecture boundary;
- public compatibility contract;
- security, privacy, trust или sensitive-data boundary;
- destructive или protected operation;
- миграции пользовательских данных с material loss risk;
- расширения разрешённого writable scope;
- выбора, который current accepted contract прямо оставляет human-only;
- Commit, Push, Merge и Release, если exact action и subject отдельно не
  разрешены current human instruction.

Material architecture boundary включает, например, process/service topology,
public API, persistent-data compatibility, external trust boundary, supported
platform contract и portable-product boundary. Internal file/module layout сам
по себе обычно material boundary не является.

## Findings и unaffected work

Если найден material product или architecture conflict:

```text
record exact finding and affected claims
→ block only dependent work
→ continue safe unaffected work inside current scope
→ request one human decision only when required
```

Не перезапускай весь проект. Не превращай локальный blocker в глобальную
остановку без material dependency.

При обычном implementation defect исправь его внутри current task. При scope
expansion, authoritative conflict или human-only choice останови только
affected route.

## Product boundary

`aos/` — self-contained portable AOS product.

Весь код, документы, schemas, templates и данные, необходимые для работы
переносимого AOS, должны:

- находиться внутри `aos/`; либо
- быть declared external dependencies с installation и version contract,
  доступным из самой папки `aos/`.

Repository tooling, root `docs/`, `development/`, root `tests/`, root `tools/`,
research, audits и временные материалы не должны становиться скрытой runtime
dependency продукта.

Проверочный принцип:

```text
copy exact aos/ into a clean target repository
→ install only dependencies declared by aos/
→ verify aos/MANIFEST.txt
→ run the product self-test
→ use the product without access to parent AOS-3 files
```

Если это невозможно из-за скрытой зависимости от остальных файлов AOS-3,
зафиксируй `ARCHITECTURE_FINDING_PORTABILITY_DEPENDENCY` и блокируй только
affected portability/release claim.

`aos/root/` является installation payload. Ручная и автоматическая установка
должны использовать один и тот же payload. Existing user-owned root files и
existing `project/` нельзя перезаписывать автоматически.

## Contracts, documentation и project templates

Перенесённые из notebook product и architecture contracts и явно назначенные
tasks являются входом для реализации в пределах их current authority.

```text
contract problem       → exact finding; do not rewrite for convenience
reversible HOW choice  → decide locally; implement; test
```

Не меняй product contract только потому, что другой вариант проще реализовать.
Если contract невозможно выполнить без изменения observable behavior или
material architecture, останови dependent implementation и предложи один
decision-ready выбор.

Не создавай документацию ради документации. Обновляй owner document только
когда реализация обнаружила:

- реальный contract gap;
- material architecture decision;
- изменившееся observable behavior;
- recovery, operational или compatibility knowledge, необходимое для
  дальнейшей работы;
- факт, без которого следующий агент обоснованно примет неверное решение.

Папка `aos/root/project/` содержит стартовые templates. После установки
корневая `project/` принадлежит пользовательскому проекту; изменение template
не является разрешением изменять существующую `project/`.

## Tests и validation

Tests должны быть пропорциональны affected behavior и risk:

- сначала запускай focused tests;
- исправляй найденный implementation defect внутри authorized scope;
- повторяй failed и directly affected tests;
- запускай broader suite только когда change может затронуть broader boundary;
- для изменений `aos/` проверяй product isolation и portability;
- не заявляй PASS за tests, которые не запускались.

Implementer-owned tests являются частью implementation flow и могут приводить
к bounded correction в том же task. Отдельный independent read-only audit или
validation run не исправляет candidate и не создаёт human approval.

```text
test PASS ≠ human acceptance
review finding ≠ authorization to expand scope
NOT_RUN ≠ PASS
UNKNOWN ≠ OK
```

## Git и protected operations

```text
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
```

Не выполняй Commit, Push, Merge, Release, force push, branch deletion,
destructive cleanup или publication без explicit permission для exact action и
subject. Выполнение одного Git action не разрешает следующий.

Перед destructive operation сначала установи exact target и возможный recovery
path. Не используй broad unresolved paths, globs или destructive repository
reset как default recovery.

## Reporting

После обычной задачи достаточно:

1. что реализовано;
2. изменённые paths;
3. выполненные tests/checks;
4. реальные findings, unknowns и существенные `NOT_RUN`;
5. один следующий action, только если он действительно нужен.

Не создавай следующий task автоматически. Не повторяй полный lifecycle, если
работа завершена и следующий action не требуется.

## Operational invariants

```text
Prefer working tested software over process artifacts.
Process serves implementation; implementation does not serve process.
Use the lightest process that preserves scope, correctness, testability and safety.
Reversible HOW belongs to the agent.
Product and protected decisions belong to the human.
Repository presence is not authority.
Independent validation does not correct its subject.
Edit is not Git delivery.
```
