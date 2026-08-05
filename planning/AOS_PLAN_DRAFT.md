# План создания AOS-3

Статус: DRAFT

Этот файл — рабочая запись плана. Он не является принятой спецификацией, Task Brief, execution authorization или разрешением на дальнейшие Git-действия.

## Цель

Пока не определена.

## Основные блоки плана

### 1. `AGENTS.md`

Инструкции для будущего coding agent при разработке проекта.

Точный состав инструкций будет определён отдельно.

### 2. Строительные леса

Подготовленная среда и техническая основа, необходимые до начала создания product-кода.

```yaml
detail_status: DRAFT
detail_class: PROPOSAL
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
```

#### 2.1. Вывод

Этап строительных лесов должен один раз создать воспроизводимую, проверяемую и безопасную среду разработки. После его завершения coding agent не придумывает на ходу структуру проекта, команды, тестовый подход, правила конфигурации, формат реестра или способ диагностики — он использует уже подготовленный каркас.

Строительные леса **не являются работающим продуктом AOS-3**. Они только создают условия, в которых последующие vertical slices базовой инфраструктуры и pipeline можно реализовывать одинаковым способом.

Короткая граница:

> `AGENTS.md` объясняет агенту, как работать. Строительные леса дают ему среду для создания и проверки кода. Базовая инфраструктура создаёт постоянные возможности продукта. Pipeline определяет движение пользователя и работы внутри продукта.

#### 2.2. Цель этапа

Подготовить implementation repository так, чтобы новый агент из чистого checkout мог:

1. понять техническую структуру проекта;
2. установить закреплённые зависимости одной командой;
3. запустить минимальную оболочку проекта;
4. выполнить единые проверки качества и тесты;
5. проверить состояние окружения через scaffold-level `doctor`/`self-test`;
6. добавить пробный модуль по шаблону без изменения архитектурных границ;
7. безопасно остановиться и восстановиться после прерванной setup/mutation;
8. доказать, какие проверки выполнены, а какие имеют статус `NOT_RUN`.

#### 2.3. Что входит и не входит

##### Входит

- каркас implementation repository;
- закреплённый toolchain и зависимости;
- единый интерфейс команд разработки;
- конфигурация окружений и правила secrets;
- минимальная запускаемая техническая оболочка;
- тестовый каркас;
- formatter, linter, type-check и другие выбранные quality checks;
- минимальный CI, повторяющий локальные команды;
- механизм реестра `feature → function → module → tests`;
- технические шаблоны и один владелец каждого contract;
- безопасный development bootstrap;
- scaffold-level `doctor` и `self-test`;
- защита scope/path/Git boundaries для агентной работы;
- atomic/journaled writes и bounded recovery для скриптов лесов;
- итоговая clean-checkout проверка.

##### Не входит

- содержательное наполнение продукта всеми фичами и функциями;
- пользовательский UX, First-Start и Tutor как product capabilities;
- бизнес-логика базовой инфраструктуры;
- этапы пользовательского pipeline;
- полный runtime-механизм установки/обновления AOS;
- полный Product Runtime `Doctor`, unified validation или recovery;
- production deployment, cloud platform и release automation;
- full Governance, Control Plane, RAG/vector DB, multi-agent orchestration;
- автоматические Commit, Push, Merge или Release;
- выбор product scope или принятие архитектурных решений агентом.

Важно: safeguards из кандидатов `FTR-004`, `FTR-011`, `FTR-014`, `FTR-021` и `FTR-030` можно применять к самим лесам, но это **не означает реализацию или принятие этих product features**. Их `human_disposition` остаётся отдельным решением.

#### 2.4. Условия входа

План этапа можно принять до выбора технологий, но выполнять его нельзя, пока человек не определил минимум:

| Решение | Зачем требуется |
|---|---|
| Implementation repository | Определяет exact target изменений |
| Основной язык и framework | Определяет toolchain, commands и структуру |
| Package manager и поддерживаемые версии | Делает setup воспроизводимым |
| Первая interface boundary: CLI, local UI или другое | Определяет минимальную запускаемую оболочку |
| Подход к данным: без БД / файл / БД | Определяет migrations и test isolation |
| Поддерживаемые среды запуска | Определяет совместимость и CI matrix |
| Первый vertical slice | Позволяет не строить универсальную платформу заранее |

Если решение отсутствует, соответствующая реализация имеет статус `BLOCKED`; остальная безопасная детализация плана может продолжаться.

#### 2.5. Принципы выполнения

1. Modular monorepo first, если человек не выбрал иную topology.
2. Один официальный entrypoint на каждое действие.
3. Локальная команда и CI вызывают один и тот же underlying check.
4. Один contract — один authoritative owner.
5. Read-only команды не меняют source tree.
6. Setup повторяем и idempotent.
7. Mutation ограничена allowlist и сверяется с фактическим diff.
8. Writes выполняются atomically либо через journal.
9. `UNKNOWN` и required `NOT_RUN` не агрегируются в `PASS`.
10. Derived indexes и отчёты перестраиваемы и не владеют product truth.
11. Все paths и ссылки repository-relative.
12. Леса остаются минимальными: новый механизм добавляется только для реальной потребности первого slice.

#### 2.6. Последовательность работ

##### SF-00 — Зафиксировать технические решения и границу этапа

**Цель:** не дать лесам скрыто выбрать архитектуру вместо человека.

**Работы:**

- записать принятые решения из условий входа;
- перечислить assumptions, unknowns, supported и unsupported environments;
- определить allowed/forbidden paths этапа;
- определить, какие результаты являются scaffold-only;
- сформировать краткие ADR только для действительно material choices;
- задать stop conditions для расширения scope.

**Результат:** decision record, exact scope и список открытых блокеров.

**Проверка выхода:** ни framework, ни БД, ни deployment, ни repository topology не выбраны агентом молча.

##### SF-01 — Создать каркас репозитория и границы модулей

**Цель:** заранее определить, где располагаются разные классы кода и данных.

**Работы:**

- создать минимальные каталоги для application code, tests, docs, scripts/tools, config и temporary/generated outputs;
- отделить Product Runtime, Development Factory и adapters на уровне границ, не обязательно отдельных сервисов;
- определить public/internal boundaries;
- добавить правила именования и импорта;
- определить ownership для managed, project-owned, user-owned и generated paths;
- исключить generated/temp/secrets из version control.

**Результат:** минимальная topology и repository map.

**Проверка выхода:** пробный пустой модуль можно однозначно разместить; circular или запрещённая dependency обнаруживается выбранным check.

##### SF-02 — Закрепить toolchain и зависимости

**Цель:** исключить расхождение машин и произвольный выбор версий агентом.

**Работы:**

- закрепить версии языка/runtime/framework;
- выбрать один package manager;
- создать lock-файл;
- разделить runtime и development dependencies;
- определить политику обновления зависимостей;
- добавить проверку interpreter/import provenance;
- документировать минимальные системные prerequisites.

**Результат:** reproducible dependency set.

**Проверка выхода:** две чистые установки получают одинаковый dependency graph; отсутствие или неверная версия dependency даёт явный failure, а не ложный `PASS`.

##### SF-03 — Создать единый интерфейс команд разработки

**Цель:** агенту не нужно искать разные команды в документации и CI.

Минимальный command contract:

| Команда | Назначение |
|---|---|
| `setup` | Подготовить окружение из чистого checkout |
| `run` | Запустить минимальную оболочку |
| `test` | Запустить тесты |
| `check` | Выполнить обязательные проверки одним entrypoint |
| `format` | Проверить/применить единое форматирование с явным режимом |
| `build` | Проверить создаваемый artifact, если build применим |
| `doctor` | Диагностировать окружение и prerequisites |
| `self-test` | Проверить работоспособность самих лесов |
| `clean/reset` | Только безопасно очистить generated state; destructive режим отдельно |

Названия команд могут измениться после выбора toolchain, но их роли должны сохраниться.

**Результат:** один documented command surface.

**Проверка выхода:** README, scripts и CI ссылаются на одни entrypoints; `help` и read-only modes не меняют дерево проекта.

##### SF-04 — Подготовить конфигурацию и environments

**Цель:** сделать local/test/CI различимыми и не допустить попадания secrets в repository.

**Работы:**

- определить typed/validated configuration contract;
- создать безопасный `.env.example` без реальных credentials;
- разделить local, test и production-like settings;
- задать precedence sources конфигурации;
- явно валидировать required, unknown и empty values;
- определить redaction для logs и reports;
- исключить скрытый network/provider access.

**Результат:** минимальный configuration layer.

**Проверка выхода:** missing, unknown, malformed и secret-bearing inputs обрабатываются предсказуемо; test configuration изолирована.

##### SF-05 — Создать минимальную запускаемую оболочку

**Цель:** доказать целостность toolchain до добавления product behavior.

**Работы:**

- создать пустой CLI/app entrypoint выбранного интерфейса;
- добавить базовый structured error/result contract;
- добавить минимальные logs с redaction;
- реализовать технический health/smoke signal;
- обеспечить корректные exit codes;
- явно маркировать оболочку как scaffold, а не implemented product.

**Результат:** приложение запускается, отвечает минимальным техническим результатом и корректно завершается.

**Проверка выхода:** success и intentional failure различимы человеком и машиной; failure не возвращает exit code успеха.

##### SF-06 — Создать тестовый каркас

**Цель:** каждый следующий slice получает готовый способ проверки.

**Работы:**

- выбрать test runner;
- создать структуру unit, contract, integration и E2E/smoke tests без обязательного заполнения всех уровней;
- подготовить fixtures, mocks/fakes и temporary directories;
- обеспечить isolation тестов от user state и network;
- добавить контрольные тесты самого scaffold;
- установить правила test naming и связи с acceptance criteria;
- предусмотреть отрицательные fixtures для malformed/empty/unknown states.

**Результат:** минимальный passing suite и минимум один intentional failing fixture/check.

**Проверка выхода:** тесты воспроизводимы, не зависят от порядка запуска и не оставляют изменения в source tree.

##### SF-07 — Настроить quality gates

**Цель:** единообразно ловить дефекты до review.

**Работы:**

- подключить formatter;
- подключить linter;
- подключить type/schema checks, если применимо;
- добавить dependency/security check только с понятным signal и policy;
- добавить проверку repository-relative links и отсутствия secrets;
- определить mandatory и optional checks;
- задать fail-closed aggregation результата.

**Результат:** одна команда `check` с явным перечнем выполненных и `NOT_RUN` checks.

**Проверка выхода:** required `NOT_RUN`, `UNKNOWN` или failure не превращаются в `PASS`; formatter не выполняет скрытую mutation в check-mode.

##### SF-08 — Создать минимальный CI

**Цель:** подтвердить, что clean environment воспроизводит локальные проверки.

**Работы:**

- установить проект из чистого checkout;
- вызвать те же `check`, `test` и `build`, что локально;
- закрепить поддерживаемую CI environment matrix;
- кэшировать только перестраиваемые данные;
- публиковать компактный результат и limitations;
- не включать автоматический release, merge или authority-bearing approval.

**Результат:** минимальный CI workflow.

**Проверка выхода:** local и CI entrypoints совпадают; stale cache не может скрыть failure; отсутствие CI check фиксируется как `NOT_RUN`.

##### SF-09 — Создать каркас реестра фич и функций

**Цель:** обеспечить трассируемость будущей реализации без превращения registry в Source of Truth.

Минимальная запись:

```yaml
feature_id:
name:
purpose:
type: BASE | PIPELINE
functions: []
dependencies: []
owning_module:
contracts: []
tests: []
planned_vertical_slice:
implementation_status:
source_artifact:
```

**Работы:**

- определить стабильные IDs `FTR-xxx` и `FN-xxx`;
- выбрать один authoritative source для содержательных записей;
- создать шаблон записи;
- реализовать read-only проверку schema, duplicates, missing links и orphan tests/modules;
- сделать derived indexes перестраиваемыми;
- запретить registry самостоятельно менять human disposition или readiness.

**Результат:** пустой/минимально заполненный registry mechanism и validator.

**Проверка выхода:** duplicate ID, broken relation и stale derived index обнаруживаются; сам реестр не считается доказательством реализации.

Содержательное заполнение выполняется позже: `BASE` — при проектировании базовой инфраструктуры, `PIPELINE` — при проектировании pipeline.

##### SF-10 — Подготовить технические contracts и шаблоны

**Цель:** не создавать формат каждого нового модуля и проверки заново.

**Работы:**

- создать минимальные templates для feature/function link, module ownership, configuration, ADR и validation result;
- определить stable result vocabulary и exit semantics;
- закрепить одного владельца каждого contract;
- использовать один strict loader/validator в runtime tools, tests и CI;
- отклонять unexpected fields и invalid empty states там, где contract закрытый;
- проверить drift между template/schema/tool/test.

**Результат:** маленький набор реально используемых templates и strict validators.

**Проверка выхода:** нет двух конкурирующих форматов одного fact class; bypass permissive parser обнаруживается negative test.

##### SF-11 — Защитить работу агента с репозиторием

**Цель:** леса должны поддерживать bounded change, а не только компиляцию кода.

**Работы:**

- создать read-only preflight для root, branch, HEAD, worktree и baseline;
- классифицировать staged, unstaged, untracked и environment noise;
- определить allowed/forbidden path rules;
- нормализовать paths и проверять traversal, symlink и nested-repository escape;
- сверять changed-file inventory с разрешённым scope;
- запретить автоматический `git add -A`;
- разделить Edit, Commit, Push, Merge и Release;
- обеспечить redaction remote/credential-bearing data.

**Результат:** scaffold-level repository safety checks.

**Проверка выхода:** dirty user state сохраняется; mutation вне allowlist и stale baseline блокируют только затронутое действие.

##### SF-12 — Реализовать безопасный development bootstrap

**Цель:** setup лесов должен быть воспроизводимым и восстанавливаемым.

Процесс:

```text
verify target
→ inventory paths
→ classify ownership
→ dry-run/preview
→ apply
→ verify
→ report next action
```

**Работы:**

- сделать dry-run без side effects;
- bind apply к exact preview/target;
- не перезаписывать user/project-owned state молча;
- обеспечить idempotent repeat;
- применять atomic writes либо durable journal;
- обнаруживать partial write;
- определить bounded retry, cancellation и rollback boundary;
- сделать destructive reset/uninstall отдельной явно разрешаемой операцией.

**Результат:** development bootstrap, а не consumer installer AOS.

**Проверка выхода:** повторный setup безопасен; interruption на каждой material boundary оставляет диагностируемое и восстановимое состояние.

##### SF-13 — Добавить scaffold-level `doctor` и `self-test`

**Цель:** различать проблему окружения, проблему scaffold и проблему будущего product-кода.

`doctor` проверяет:

- правильность repository/root;
- версии runtime и package manager;
- наличие зависимостей;
- конфигурацию и permissions;
- доступность необходимых локальных сервисов;
- writable temp boundary;
- отсутствие запрещённого secret exposure.

`self-test` проверяет:

- команды scaffold;
- strict validators;
- test isolation;
- read-only zero-write guarantee;
- bootstrap idempotency;
- registry validation;
- local/CI entrypoint consistency.

**Результат:** human-readable и machine-readable diagnostics.

**Проверка выхода:** каждый check имеет status, reason и remedy; required `NOT_RUN` предотвращает общий `PASS`; неверный interpreter определяется явно.

##### SF-14 — Провести итоговую проверку с чистого состояния

**Цель:** доказать готовность лесов к созданию первого real vertical slice.

Сценарий:

1. Получить exact clean checkout.
2. Запустить `setup` по одной инструкции.
3. Запустить `doctor` и `self-test`.
4. Запустить минимальную оболочку.
5. Выполнить `check`, `test` и, если применимо, `build`.
6. Добавить пробный модуль по шаблону.
7. Связать его с тестом и тестовой записью registry.
8. Намеренно проверить несколько negative cases.
9. Удалить пробный модуль без остаточного drift либо оставить его только как scaffold fixture.
10. Зафиксировать Evidence и ограничения.

**Результат:** frozen scaffold candidate и review package.

**Проверка выхода:** независимый агент способен повторить сценарий без истории чата и без создания новых инфраструктурных механизмов на ходу.

#### 2.7. Обязательные негативные проверки

| Группа | Минимальный сценарий |
|---|---|
| Toolchain | Неверная версия runtime или отсутствующая dependency |
| Config | Missing, empty, unknown и malformed value |
| CLI | Failure с ошибочным exit code `0` |
| Read-only | `help`, `doctor` или check меняет source tree |
| Scope | Traversal, symlink или изменение вне allowlist |
| Worktree | Существующий пользовательский файл попадает в candidate |
| Bootstrap | Dry-run пишет; repeat повреждает state; setup прерывается |
| Recovery | Partial write не обнаружен или unsafe retry расширяет scope |
| Registry | Duplicate ID, broken link, orphan module/test, stale index |
| Contracts | Runtime/tool обходит strict validator |
| Status | `UNKNOWN` или required `NOT_RUN` превращается в `PASS` |
| CI | Локальная и CI-команда вызывают разные проверки |
| Secrets | Credential попадает в log/report/remote output |
| Portability | Absolute local path ломает запуск в новом location |

#### 2.8. Definition of Done этапа

Строительные леса готовы к human review только если одновременно выполнено следующее:

- [ ] implementation repository и exact scaffold candidate определены;
- [ ] структура и module boundaries задокументированы;
- [ ] toolchain и dependencies закреплены;
- [ ] clean `setup` воспроизводим;
- [ ] `run`, `check`, `test`, `doctor` и `self-test` имеют один официальный entrypoint;
- [ ] минимальная оболочка запускается, но не выдаётся за реализованный продукт;
- [ ] тестовый каркас и negative fixtures работают;
- [ ] CI повторяет локальные команды;
- [ ] registry mechanism проверяет IDs и связи;
- [ ] read-only operations подтверждённо не пишут в source tree;
- [ ] allowed paths и фактический diff сверяются;
- [ ] interruption/partial write обнаруживаются и имеют recovery path;
- [ ] secrets redacted, links repository-relative;
- [ ] clean-checkout сценарий повторён независимым агентом или в изолированном окружении;
- [ ] выполненные checks, `NOT_RUN`, limitations и remaining risks перечислены;
- [ ] результат имеет статус `READY_FOR_HUMAN_REVIEW`, но не `ACCEPTED`;
- [ ] Commit, Push, Merge и Release остаются `NOT_RUN`, если отдельно не разрешены.

#### 2.9. Артефакты результата

Минимально необходимы:

1. краткая repository map;
2. toolchain/dependency manifest и lock-файл;
3. единый command surface;
4. configuration example и validation contract;
5. minimal runnable shell;
6. test scaffold и negative fixtures;
7. quality configuration;
8. minimal CI workflow;
9. registry schema/template и read-only validator;
10. templates/strict contract validators;
11. repository preflight/scope checks;
12. development bootstrap с preview и recovery;
13. scaffold-level `doctor`/`self-test`;
14. один итоговый validation report.

Не нужно заранее создавать отдельный документ на каждый пункт. Где возможно, authoritative configuration/code и один компактный README/Stage Report предпочтительнее множества readiness-файлов.

#### 2.10. Зависимости и параллельность

```text
SF-00 decisions
→ SF-01 repository skeleton
→ SF-02 toolchain
→ SF-03 commands
→ SF-04 config + SF-05 runnable shell
→ SF-06 tests + SF-07 quality
→ SF-08 CI
→ SF-09 registry + SF-10 contracts + SF-11 guards
→ SF-12 bootstrap
→ SF-13 doctor/self-test
→ SF-14 clean-checkout validation
```

После `SF-03` часть работ можно выполнять параллельно, но итоговая `SF-14` начинается только после завершения всех обязательных ветвей.

#### 2.11. Риски из предыдущего опыта и защита

| Риск | Защита в плане |
|---|---|
| Леса превращаются в платформу до первой product value | minimal scope, first-slice orientation, deferred complexity |
| Документы/CI выглядят как готовый продукт | явная scaffold maturity и executable Evidence |
| Разные validators дают разные результаты | one official entrypoint и strict shared validator |
| Dirty worktree загрязняет результат | preflight, state classification, changed-file allowlist |
| Read-only check выполняет mutation | before/after tree/status verification |
| Setup повреждает user state | ownership classes, preview binding, idempotency |
| Прерывание оставляет unknown state | atomic write/journal, partial-write detection, recovery |
| Registry становится вторым Source of Truth | derived-only index, explicit source artifact |
| Правила дублируются в adapters | один common source; `AGENTS.md` остаётся отдельным владельцем инструкций |
| Контекст становится слишком большим | minimal bootstrap, task-scoped loading |
| CI и local расходятся | CI вызывает те же commands |
| Формальная готовность заменяет реальную проверку | clean-checkout dogfood и negative cases |

#### 2.12. Основание и статус утверждений

##### Подтверждённые основания

- `00_Core.md` §§10–12, 17: Minimal Safety Floor, граница продукта, последовательность и правила агента.
- `02_Architecture.md` §§1–3, 6, 8–17: contract-first, layers, ownership, registries, context, modular monorepo direction, recovery и deferred complexity.
- `03_Development.md` §§4, 9–21: preflight, stages, scope control, verification, testing, negative scenarios, recovery, Git boundaries и manual dogfood.
- `04_Lessons.md` `LES-001`–`LES-007`, `LES-013`–`LES-042`: ошибки избыточной документации, schema/runtime drift, scope, dirty state, non-atomic writes, duplicated state, first-contact fragmentation и premature automation.
- `06_Features.md`: inventory и design candidates `FTR-004`, `FTR-011`, `FTR-014`, `FTR-021`, `FTR-030`; их наличие не является human disposition или execution authority.

##### Классификация

- Наличие отдельного этапа строительных лесов — `HUMAN_CONFIRMED_DIRECTION` из текущего решения пользователя.
- Состав `SF-00`–`SF-14`, порядок и Definition of Done — `PROPOSAL`.
- Implementation repository, toolchain, first interface, data approach и first vertical slice — `UNKNOWN`/`UNASSIGNED` до отдельного решения человека.
- Реализация, validation, human acceptance и Git delivery — `NOT_RUN`.

#### 2.13. Рекомендуемый следующий bounded action

Провести human review границ и состава этапа: подтвердить, удалить или перенести пункты `SF-00`–`SF-14`. Выбор технологий, implementation repository и создание executable Task Brief выполнить отдельными последующими решениями.

### 3. Базовая инфраструктура

Постоянная основа проекта, которая не является pipeline, но участвует в работе системы и создании проекта.

К этому блоку относится пользовательский UX. Остальной состав будет определён отдельно на основании документов и истории обсуждений.

### 4. Pipeline

Последовательность движения работы внутри проекта.

Точные этапы, входы, выходы и границы pipeline будут определены отдельно.

## Принятые направления

- План формируется постепенно, небольшими шагами.
- План должен включать четыре отдельных блока: `AGENTS.md`, строительные леса, базовую инфраструктуру и pipeline.
- Базовая инфраструктура и pipeline не должны смешиваться.
- Пользовательский UX относится к базовой инфраструктуре.
- Каркас реестра фич и функций относится к строительным лесам; содержательное наполнение выполняется в блоках базовой инфраструктуры и pipeline.
- Порядок реализации четырёх блоков пока не утверждён.

## Открытые вопросы

- Какие элементы предложенного состава строительных лесов `SF-00`–`SF-14` следует принять, перенести или удалить?
- Что именно входит в остальные три блока?
- В какой последовательности блоки должны подготавливаться и реализовываться?
- Где проходят точные границы между строительными лесами, базовой инфраструктурой и pipeline?
