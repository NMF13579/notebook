---
document_id: AOS3-REPOSITORY-ARCHITECTURE-MIGRATION-SPEC-R1
title: AOS-3 Repository Architecture and Migration Specification
status: DRAFT
authority: NONE
source_repository: NMF13579/notebook
target_repository: UNCREATED_AOS_3
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
document_language: ru
technical_identifiers_language: en
---

# AOS-3 — архитектура репозитория и спецификация переноса

## 1. Назначение

Этот документ фиксирует согласованный дизайн будущего репозитория `AOS-3` и
границы переноса проектной документации из `NMF13579/notebook`.

`AOS-3` должен одновременно обеспечивать:

1. разработку самого продукта AOS;
2. хранение принятой архитектуры и спецификаций AOS;
3. изолированную рабочую область для черновиков и исследований;
4. непосредственную разработку переносимого продукта в папке `aos/`;
5. проверку того, что `aos/` можно перенести в новый проект отдельно от
   остального репозитория;
6. создание в целевом проекте папки `project/`, содержащей техническую
   документацию конкретного разрабатываемого проекта.

Документ не создаёт репозиторий `AOS-3`, не переносит файлы, не выбирает
technology stack и не разрешает implementation или Git operations.

```yaml
specification_status: DRAFT
target_repository_creation: NOT_RUN
source_document_migration: NOT_RUN
runtime_implementation: NOT_RUN
human_acceptance: NOT_RUN
commit: NOT_RUN
push: NOT_RUN
merge: NOT_RUN
release: NOT_RUN
```

## 2. Принятые архитектурные решения

### 2.1 Product-in-place

`AOS-3/aos/` является непосредственно поддерживаемым source of truth для
поставляемого продукта. Продукт не генерируется заново из `development/` или
другой скрытой source tree.

```text
edit product in aos/
→ test exact aos/
→ verify isolated portability
→ bind package identity
→ review
→ distribute exact aos/
```

Сборочные инструменты могут проверять и упаковывать `aos/`, но не должны иметь
вторую конкурирующую реализацию продукта.

### 2.2 Переносимый гибридный продукт

`aos/` содержит:

- документы и правила работы;
- проектные шаблоны;
- стабильные алгоритмы разработки;
- проверяемые схемы и контракты;
- минимальные детерминированные инструменты;
- адаптеры к агентским средам;
- self-test и точную идентичность пакета.

AI-агент выполняет интеллектуальную разработку. Инструменты AOS выполняют
только ограниченные воспроизводимые операции и не принимают product decisions,
не создают human authority и не выполняют Git delivery без отдельного решения.

### 2.3 Разделение продукта и проектных данных

В целевом репозитории роли разделены:

```text
aos/     = как организована разработка
project/ = что именно разрабатывается
```

Обновление продукта `aos/` не должно автоматически перезаписывать данные в
`project/`.

## 3. Целевая структура репозитория AOS-3

```text
AOS-3/
├── aos/                    # готовый переносимый продукт
├── docs/                   # принятая архитектура и спецификации самого AOS
├── development/            # рабочие и неканонические материалы
├── tests/                  # проверки продукта и переносимости
├── tools/                  # инструменты разработки и упаковки AOS
├── .github/                # repository automation, если она будет выбрана
├── AGENTS.md               # правила работы агентов в AOS-3
├── README.md               # назначение, навигация и quick start
├── LICENSE                 # лицензия репозитория и продукта
├── CHANGELOG.md             # изменения поставляемого продукта
├── .gitignore
├── .editorconfig
└── stack-dependent files   # только после отдельного выбора toolchain
```

### 3.1 `aos/` — продукт

`aos/` — единственная папка, которую необходимо переносить в новый проект как
продукт AOS. Она должна оставаться работоспособной после удаления всех соседних
каталогов AOS-3.

### 3.2 `docs/` — проектирование AOS

`docs/` содержит developer-facing знания о продукте AOS:

- product definition самого AOS;
- архитектуру системы;
- архитектуру переносимого пакета;
- engineering и release design;
- принятые ADR;
- migration decisions и provenance.

Эти материалы предназначены для разработки AOS и не копируются автоматически
в пользовательские проекты.

### 3.3 `development/` — рабочая область

```text
development/
├── drafts/
├── research/
├── experiments/
├── audits/
└── fixtures/
```

Содержимое `development/`:

- не является частью продукта;
- не создаёт authority своим наличием;
- не является runtime dependency для `aos/`;
- может быть удалено без нарушения переносимого пакета;
- продвигается в `docs/` или `aos/` только как отдельное осознанное изменение.

### 3.4 `tests/` — внешняя проверка продукта

```text
tests/
├── contracts/
├── portability/
├── installation/
└── integration/
```

Root tests рассматривают `aos/` как поставляемый subject. Они не заменяют
self-test, который находится внутри продукта и доступен после переноса.

### 3.5 `tools/` — разработка AOS

Root `tools/` обслуживает разработчиков AOS-3: validation, packaging,
release preparation и isolated test setup. Эти инструменты не являются
обязательной частью целевого пользовательского проекта.

## 4. Внутренняя структура переносимого продукта

```text
aos/
├── root/                   # payload для корня целевого репозитория
├── docs/                   # документы пользователя и оператора AOS
├── workflows/              # стабильные алгоритмы разработки
├── templates/              # шаблоны создаваемых проектных артефактов
├── schemas/                # проверяемые структуры и контракты
├── tools/                  # минимальные переносимые инструменты
├── adapters/               # интеграция с Codex и другими агентами
├── examples/               # небольшие самодостаточные примеры
├── selftest/               # проверка установленного продукта
├── AGENTS.md               # package-local routing и boundaries
├── START_HERE.md           # основная точка входа в продукт
├── README.md
├── ROOT_INSTALL_GUIDE.md
├── VERSION
└── MANIFEST.txt
```

### 4.1 Правило автономности

Файлы внутри `aos/` не должны ссылаться на обязательные ресурсы за границами
папки. Запрещены runtime dependencies на:

- `../docs/`;
- `../development/`;
- `../tests/`;
- `../tools/`;
- историю Git исходного репозитория;
- audit/controller artifacts из notebook;
- недоступные локальные абсолютные пути.

Внешние источники могут быть указаны только как необязательная provenance.

### 4.2 `aos/workflows/`

Папка содержит стабильные продуктовые алгоритмы, описывающие переход от идеи
к проверенному результату:

```text
intent / idea intake
→ product definition
→ feature and architecture definition
→ bounded task preparation
→ explicit authorization where required
→ implementation by agent
→ independent or focused validation
→ human review and decision
→ delivery only with separate authority
→ project memory and continuation
```

Алгоритм может быть declarative contract или иметь минимальную executable
поддержку. Технологическая реализация остаётся отдельным engineering decision.

### 4.3 `aos/tools/`

Допустимые ответственности:

- проверка структуры и manifest;
- создание файлов по точным шаблонам;
- side-effect-free preview;
- сбор repository-derived статуса;
- проверка схем;
- создание bounded task/review artifacts;
- self-test и post-copy verification.

Недопустимые implicit responsibilities:

- выбор product scope или architecture;
- создание human approval;
- скрытое расширение allowed paths;
- автоматический Commit, Push, Merge или Release;
- неограниченное исправление пользовательских файлов;
- сохранение обязательного состояния только во внешнем сервисе.

## 5. Root installation payload

### 5.1 Назначение `aos/root/`

`aos/root/` содержит точное дерево файлов, предназначенных для размещения в
корне целевого репозитория.

```text
aos/root/<relative-path>
→ copy with conflict review
→ target-repository/<relative-path>
```

Один и тот же payload используется при ручной и автоматической установке.
Скрытый отдельный генератор root-файлов не допускается.

### 5.2 Copy, а не destructive move

При ручной установке пользователь копирует содержимое `aos/root/`. Исходные
файлы остаются внутри `aos/` для:

- проверки `MANIFEST.txt`;
- повторяемого развёртывания;
- диагностики установки;
- обновления;
- сравнения фактического root state с поставляемым payload.

### 5.3 Классы владения и установки

| Класс | Семантика |
|---|---|
| `CREATE_ONLY` | Создать только при отсутствии target path |
| `MERGE_REQUIRED` | При наличии target требуется явное объединение |
| `OPTIONAL` | Установка выбирается пользователем |
| `AOS_OWNED` | Поставляемый AOS файл с declared update policy |
| `USER_OWNED` | Пользовательские данные; автоматическая перезапись запрещена |

Класс владения и операция должны быть указаны в install/update manifest до
автоматической записи.

## 6. Целевой репозиторий после установки

Минимальный результат развёртывания:

```text
target-repository/
├── aos/                    # установленный переносимый продукт
├── project/                # знания о конкретном проекте
├── AGENTS.md               # root routing к AOS и project state
├── START_HERE.md           # human-facing entrypoint, если выбран
└── existing project files
```

`aos/` предоставляет метод и инструменты. `project/` является persistent
user/project-owned knowledge space.

## 7. Папка `project/`

### 7.1 Создание

Starter tree поставляется в `aos/root/project/` и появляется в корне после
копирования root payload.

```text
aos/root/project/
→ target-repository/project/
```

Папка не должна быть пустой: необходимые entrypoints и templates должны быть
реальными файлами, пригодными для Git и ручного использования.

### 7.2 Рекомендуемая структура

```text
project/
├── README.md               # назначение и навигация
├── CURRENT.md              # текущее состояние и один следующий шаг
├── 00_PROJECT.md           # идея, цель, scope и ограничения
├── 01_PRODUCT.md           # users, problems, journeys и requirements
├── 02_ARCHITECTURE.md      # архитектура создаваемого проекта
├── 03_DEVELOPMENT.md       # правила и процесс разработки
├── features/               # feature-specific specifications
├── decisions/              # product и architecture decisions
├── tasks/                  # подготовленные bounded задачи
├── evidence/               # долговременные результаты проверок
├── research/               # targeted findings с provenance
└── lessons/                # ошибки, regressions и reusable lessons
```

Структура является стартовым контрактом. Её расширение должно быть обусловлено
потребностью проекта, а не стремлением создать полный bureaucracy framework.

### 7.3 Правила владения

- `project/` принадлежит конкретному пользовательскому проекту.
- Диалог с агентом создаёт и обновляет знания в `project/`.
- Продукт `aos/` не становится owner фактов конкретного проекта.
- Обновление или замена `aos/` не перезаписывает `project/`.
- Существующая `project/` всегда рассматривается как `USER_OWNED`.
- В `project/` сохраняются только материалы, необходимые для понимания,
  реализации, проверки и продолжения проекта.
- Временные логи, caches и повторяемый tool output не становятся канонической
  документацией автоматически.

## 8. Dependency и authority boundaries

### 8.1 Допустимое направление зависимостей

```text
docs/ and development/ ──human-reviewed promotion──> aos/
tests/ and tools/ ─────────────────────────────────> inspect aos/
aos/ ─────────────────────────────────────────────> no required parent dependency

installed aos/ ──templates/tools──> project/
project/ ─────────────────────────> no source dependency on AOS-3 development files
```

### 8.2 Authority

- `development/` не создаёт authority.
- `docs/` владеет принятыми фактами о разработке самого AOS в declared scope.
- `aos/` владеет поведением поставляемого продукта в пределах принятой версии.
- `project/` владеет принятыми фактами конкретного пользовательского проекта.
- Tool output, audit result, manifest и PASS не создают human approval.
- Присутствие файла не разрешает mutation или Git operation.

## 9. Установка

### 9.1 Ручной маршрут

```text
copy exact aos/ into target repository
→ verify aos/MANIFEST.txt
→ read aos/ROOT_INSTALL_GUIDE.md
→ inspect aos/root/ payload
→ copy non-conflicting root files
→ review every existing-path conflict
→ verify project/ entrypoints
→ run available self-test
→ start through root or package START_HERE.md
```

### 9.2 Автоматический маршрут

Автоматический installer должен применять тот же payload и те же ownership
classes:

```text
observe exact target
→ build side-effect-free plan
→ classify conflicts
→ show preview
→ obtain required authorization
→ apply exact fresh plan
→ verify paths and bytes
→ report changed and preserved paths
```

Ручной и автоматический маршруты должны приводить к семантически одинаковой
структуре.

### 9.3 Fail-closed behavior

| Условие | Результат |
|---|---|
| Manifest mismatch | Остановить affected installation |
| Existing `USER_OWNED` path | Не перезаписывать; запросить решение |
| Existing `project/` | Сохранить; предложить только bounded additions |
| Stale preview | Пересобрать preview до записи |
| Partial write | Зафиксировать exact partial state и recovery action |
| Unknown ownership | Не выполнять автоматическую запись |
| Missing optional tool | Сохранить manual path; не заявлять automated PASS |
| Git permission absent | Не выполнять Git operation |

## 10. Обновление продукта

Обновление рассматривает `aos/` и `project/` независимо.

```text
new exact aos candidate
→ compare installed product identity
→ classify AOS-owned changes
→ preview conflicts and local modifications
→ update only authorized AOS-owned paths
→ preserve project/ and user-owned root paths
→ rerun self-test
```

Нельзя использовать обновление продукта как скрытую миграцию пользовательской
документации.

## 11. Проверки AOS-3

### 11.1 Contract checks

- required product entrypoints присутствуют;
- manifest exact и детерминирован;
- схемы и templates согласованы;
- ownership classes полны для root payload;
- ссылки внутри `aos/` разрешаются без parent repository;
- отсутствуют абсолютные локальные paths и скрытые dependencies;
- product и Git authorization не повышаются автоматически.

### 11.2 Portability checks

```text
create clean temporary repository
→ copy only aos/
→ remove access to AOS-3 parent materials
→ verify manifest
→ perform manual-install simulation
→ perform automated preview where available
→ create root project/ scaffold
→ run self-test
→ confirm no unexpected external writes
```

### 11.3 Conflict checks

- target root is empty;
- target contains existing `AGENTS.md`;
- target contains an existing `project/`;
- target contains partially installed AOS;
- target contains locally modified AOS-owned file;
- target lacks optional runtime/tooling;
- installation is interrupted after a bounded subset of writes.

### 11.4 Content-boundary checks

- `development/` materials отсутствуют в package manifest;
- audits и migration history не входят в продукт без необходимости;
- root developer tools не требуются установленному AOS;
- `project/` templates не содержат факты исходного notebook project;
- examples не воспринимаются как current project truth.

## 12. Процесс разработки самого AOS

```text
research or draft in development/
→ architecture/product decision in docs/
→ bounded product edit directly in aos/
→ focused contract checks
→ root test suite
→ isolated portability test
→ exact product manifest
→ independent review when material
→ human decision
→ separately authorized versioning and Git delivery
```

Отдельный working material не должен автоматически становиться продуктом.
Изменение `aos/` должно быть обозримо как обычный repository diff.

## 13. Карта переноса из notebook

Перенос выполняется через классификацию, а не через полное копирование
repository history или workspace.

| Notebook source | Target role | Правило |
|---|---|---|
| `AOS/portable/**` | начальная основа `AOS-3/aos/` | переносить как exact accepted source candidate, затем адаптировать отдельными изменениями |
| `docs/00_Core.md`–`docs/06_Features.md` | `AOS-3/docs/product/` и `docs/architecture/` | сохранить owner semantics; устранить notebook-specific routing |
| принятые full-project drafts | supporting source для root `docs/` | не создавать второй competing owner |
| `AOS/**` вне portable | source candidates | классифицировать по product/development/reference role |
| `archive/aos-archive/**` | `development/research/legacy-aos3/` или provenance index | authority отсутствует; не переносить автоматически в продукт |
| selected lessons and algorithms | сначала `development/` | продвижение в `docs/` или `aos/` только после review |
| `workspace/audits/**` | migration evidence при необходимости | не включать в `aos/` |
| controller/correction history | обычно не переносить | сохранить только необходимую provenance |
| временные workspace drafts | exclude by default | переносить только при явной уникальной ценности |

## 14. Этапы будущего переноса

### M0 — Read-only inventory

- зафиксировать source branch/HEAD;
- построить exact inventory релевантных документов;
- классифицировать `PRODUCT`, `AOS3_DOCS`, `DEVELOPMENT`, `REFERENCE`, `EXCLUDE`;
- выявить competing owners и conflicts;
- подготовить decision-ready migration map.

### M1 — Repository foundation

- создать новый repository только после отдельного human decision;
- добавить минимальные root entrypoints и directory skeleton;
- не выбирать runtime stack неявно;
- подтвердить repository role и Git boundaries.

### M2 — Documentation migration

- перенести принятые product/architecture sources в root `docs/`;
- сохранить provenance;
- адаптировать routing к AOS-3;
- не переносить historical statuses как current claims.

### M3 — Portable product seed

- поместить принятую portable основу непосредственно в `aos/`;
- добавить согласованные `root/` и `project/` templates;
- проверить автономность;
- создать новый exact manifest после любых byte changes.

### M4 — Development architecture

- определить implementation architecture, toolchain и module boundaries;
- спроектировать минимальные portable tools;
- определить install/update and self-test contracts;
- отделить reversible engineering HOW от принятых product semantics.

### M5 — Implementation and verification

- выполнять только после отдельной implementation authorization;
- реализовать по bounded tasks;
- проверить contract, conflict и portability suites;
- провести human review точного product candidate.

### M6 — Delivery

- Commit, Push, Merge и Release являются отдельными explicit actions;
- release identity связывает exact `aos/` manifest и version;
- опубликованный продукт не включает `development/`.

## 15. Root files AOS-3

### 15.1 Обязательные независимо от stack

- `AGENTS.md`;
- `README.md`;
- `LICENSE`;
- `CHANGELOG.md`;
- `.gitignore`;
- `.editorconfig`;
- routing к `docs/`, `development/`, `tests/`, `tools/` и `aos/`.

### 15.2 Условные после выбора stack

- package/project configuration;
- dependency and lock files;
- formatter/linter/test configuration;
- build configuration;
- CI workflows;
- release automation.

Условные файлы нельзя придумывать до выбора implementation architecture.

## 16. Non-goals

Эта спецификация не требует:

- SaaS или hosted control plane;
- обязательной базы данных;
- обязательного multi-agent orchestration;
- генерации `aos/` из второй source tree;
- переноса всего notebook archive;
- хранения временных логов как canonical knowledge;
- автоматического изменения пользовательской `project/`;
- автоматического Git delivery;
- выбора языка, framework или provider на стадии migration design.

## 17. Критерии готовности архитектуры репозитория

Архитектура считается достаточно определённой для подготовки implementation
plan, когда:

1. exact source inventory и migration map проверены человеком;
2. состав root `docs/` и `development/` не создаёт competing owners;
3. начальный exact состав `aos/` определён;
4. payload `aos/root/` и ownership classes определены;
5. starter tree `project/` определён;
6. manual installation contract согласован;
7. automatic installation boundary согласован;
8. portability and conflict test matrix согласована;
9. implementation stack и repository creation имеют отдельные решения;
10. implementation и Git authority явно заданы либо остаются `NONE`.

## 18. Open decisions

Следующие решения этой спецификацией не принимаются:

- exact URL/owner/visibility нового repository `AOS-3`;
- способ сохранения или отсутствия Git history при переносе;
- programming language и supported versions;
- packaging/dependency/lock strategy;
- точный executable CLI/API surface;
- serialization и persistent state layout;
- точный список root payload files кроме согласованных ролей;
- update transaction и rollback implementation;
- supported operating systems и agent environments;
- release/versioning scheme;
- license choice, если она ещё не утверждена отдельно.

## 19. Следующий bounded action

```text
READ_ONLY_NOTEBOOK_TO_AOS3_MIGRATION_INVENTORY
```

Следующий этап должен только прочитать current notebook sources и создать
decision-ready exact migration map. Создание нового repository, перенос файлов,
implementation, Commit, Push, Merge и Release требуют отдельных решений.
