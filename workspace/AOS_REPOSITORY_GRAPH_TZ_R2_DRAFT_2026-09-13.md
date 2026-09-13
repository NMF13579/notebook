# AOS — техническое задание на компактную систему графа репозитория

Редакция: **R2** · Дата подготовки: **2026-09-13**.

Назначение: требования для возможной будущей пересборки AOS. Это не задача изменения действующего AOS-3 и не разрешение на создание runtime в notebook.

```yaml
document_id: AOS_REPOSITORY_GRAPH_TZ_R2
document_status: GENERATED_DRAFT
proposal_status: PROPOSAL
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
current_repository_migration: NOT_AUTHORIZED
```

R2 подготовлена из полного текста R1, предоставленного пользователем, и замечаний к нему. Разрешение подготовить R2 не означает принятия самого ТЗ или архитектуры. Это полный документ для рассмотрения; R1 не требуется читать как дополнение.

## 1. Решение в одном абзаце

Создать один локальный, производный, snapshot-bound граф фактического устройства репозитория. Он помогает агенту находить нужные участки, понимать подтверждённые связи, видеть границы знания и оценивать область проверки перед изменением. Один постоянный активный graph artifact является предлагаемым ограничением продукта. Человек и агент получают небольшие представления по запросу, с доступным продолжением. Создание и обновление вызываются явно и не меняют source. Граф не владеет требованиями, архитектурными решениями, разрешениями или статусами принятия.

Главный критерий: агент обнаруживает существенную связь до изменения и получает достаточно контекста для её проверки. Уменьшение первого ответа само по себе не является доказательством полезности.

Первый срез уже проверяет это на одном реальном вопросе в сравнении с обычным поиском. Разработка полноценного selective refresh не является предпосылкой первого такого сравнения.

## 2. Основания, статус требований и границы достоверности

Перед введением механизма требуется ответить: какой наблюдавшийся failure или дорогой необратимый риск он закрывает?

### 2.1. Что известно

| Основание | Класс и ограничение | Следствие |
|---|---|---|
| Пользователь сообщил о переделках из-за недостаточного понимания связей проекта | `REPORTED`; причины отдельных переделок независимо не разобраны | Проверять обнаружение существенных связей на реальных задачах |
| В переданном отчёте mapping refresh узкая выборка portability-участка заняла 6 432 bytes | `REPORTED`; не полный контекст FTR-001 | Нужны точные selectors и ограниченное извлечение |
| Bundle experiment: исходник 1 106 790 bytes, bundle 973 547 bytes; latency смешанная; рекомендация `KEEP_MONOLITH` | `REPORTED`; исходный отчёт прочитан при оценке R1, но эксперимент не повторялся | Многофайловое хранение не следует принимать как обязательную основу |
| В том же опыте более широкие запросы дали около 65 KB и были усечены | `REPORTED`; selectors и budgets отличаются от выборки 6 432 bytes | Размер первой страницы и полнота продолжения — разные требования |
| Baseline разделяет authority, task-local context, provenance и derived indexes | Принятый knowledge baseline в своей fact class | Граф не создаёт нового владельца product facts или дополнительного approval process |

`KEEP_MONOLITH` — рекомендация опыта, не автоматически принятое архитектурное решение. Сравнивать 6,4 KB и 65 KB как ухудшение одного запроса нельзя без одинаковых selectors, глубины, evidence и budgets. Размер scratch-стенда не равен эксплуатационной стоимости графа. Быстрый lookup не доказывает уменьшение переделок.

Текущие сведения о реализации AOS-3 и новые runtime results этим документом не устанавливаются. Исторические результаты остаются привязаны к источникам [S6–S7].

### 2.2. WHAT и инженерные кандидаты

Все требования R2 — `PROPOSAL` до принятия. Слова «должен» и «требуется» задают предлагаемый контракт, а не действующее разрешение.

- **Контрактные требования:** один активный graph artifact, границы чтения/записи, семантика records и запросов, воспроизводимость поддержанных наблюдений, freshness, целостность публикации, отказ и критерии полезности.
- **Инженерные кандидаты:** конкретный формат хранения, структура индексов, parser, алгоритм обхода, построение IDs, блокировка writers, временный файл и способ атомарной публикации. Они могут быть заменены эквивалентным решением, сохраняющим контракт.
- **Численные цели:** budgets и latency ниже — начальные цели pilot, не измеренные свойства готовой реализации.

Граница WHAT/HOW соответствует `00_Core.md`, §12 [S1]. Конкретный инженерный выбор не требует нового документа или дополнительного Human Gate, если это обратимое HOW внутри принятой задачи и он не меняет protected decision.

## 3. Назначение, пользователи и границы продукта

### 3.1. Пользователи

| Участник | Действие | Результат |
|---|---|---|
| Владелец проекта | Смотрит обзор и неизвестные области | Понимает, что исследовано и что остаётся неизвестным |
| Coding-agent | Ищет по path, ID или FTR, раскрывает связи и evidence | Получает проверяемый контекст задачи |
| Картограф / разработчик | Наблюдает участок в разрешённом scope | Добавляет подтверждённые записи либо явные ограничения |
| Reviewer | Проверяет semantic diff и источники | Понимает, какие утверждения изменились и почему |

Это роли одного workflow, не требование отдельных агентов или multi-agent orchestration.

### 3.2. Scope первой версии

Один локальный repository/worktree; source, tests, конфигурация и релевантные документы в объявленной области; существующие entrypoints, components, artifacts/contracts и feature records; bounded queries; freshness, coverage; ручной запуск создания и обновления.

Первый pilot ограничивается одним поддержанным языком, профилем окружения и несколькими явно перечисленными patterns связей. Полное извлечение всех отношений всего репозитория не требуется.

Сначала инструмент служит разработке самого AOS. Переносимая возможность для любых чужих проектов — отдельное решение. FTR-002, FTR-016 и FTR-021 в inventory являются тематическими указателями, не выбранными фичами или обязательными зависимостями [S5].

### 3.3. Вне scope

Graph/vector DB, RAG, сервер, MCP, watcher/daemon, Git hooks, облачная синхронизация, marketplace, community detection, универсальный parser всех языков, runtime instrumentation, автоматическое исправление проекта, lifecycle mutation и автоматическая Git delivery.

Не создавать отдельно редактируемые графы кода, фич и данных: это представления одного набора наблюдений. Автоматическое сравнение AS-IS и TARGET не входит в первую версию. Существующий AOS-3 не мигрируется по этому ТЗ.

## 4. Обязательные свойства

| ID | Требование |
|---|---|
| GR-01 | Факты об устройстве выводятся из наблюдения выбранного subject; документированное поведение не выдаётся за реализацию |
| GR-02 | Каждая существенная связь имеет evidence и понятный способ проверки |
| GR-03 | `UNKNOWN`, `NOT_FOUND`, `NOT_RUN`, `CONFLICT` и неисследованные области видимы |
| GR-04 | Одинаковые inputs и revision детерминированного extractor дают одинаковые поддержанные структурные records |
| GR-05 | Удаление графа не уничтожает первичные требования, решения или уникальный обязательный контекст |
| GR-06 | Чтение, check, query, validate и help не создают записей в source, Git index/refs, graph, caches или lock files |
| GR-07 | Частичный refresh не повышает актуальность непроверенной области |
| GR-08 | Bounded ответ не объявляется полным при наличии невыданных подходящих records или неизвестных зависимостей |
| GR-09 | Сбой графа не блокирует безопасное прямое исследование; graph artifact не является runtime dependency продукта AOS |
| GR-10 | Нынешние paths/SHA не становятся конфигурацией будущей реализации |
| GR-11 | При выполненных prerequisites поддержанный положительный сценарий даёт полезный результат; правильный отказ проверяется отдельно |
| GR-12 | Первая реализация имеет объявленные пределы входа и обработки, а превышение не скрывается за `CURRENT` или `PASS` |

Эти свойства не добавляют Human Gates и не разрешают защищённые действия [S1–S3].

## 5. Один активный граф и логическая модель хранения

### 5.1. Контракт обработки

```text
repository + явный scope + поддержанный профиль
  → наблюдение bytes и связей
  → candidate graph
  → проверка integrity и source bindings
  → публикация одного активного graph artifact
  → ограниченное представление / продолжение / detail
```

Допустим временный candidate публикации; это не второй активный источник. Обзор человека генерируется по запросу. Обязательных отдельно редактируемых индексов и копий graph facts нет.

### 5.2. Логические секции

```text
schema_version + extractor_revision + observation_profile
scope + source_binding
sources
nodes
edges
evidence
coverage + unresolved + pending_refresh
```

Три основные сущности — node, edge, evidence. Остальные секции обслуживают наблюдение и его границы; это не отдельная платформа registries.

Формат обязан сохранять types, направления, parallel edges, source bindings, неизвестные значения и допустимые extension fields. Reader отвергает повреждённую структуру, duplicate IDs, неразрешённые ссылки и неподдержанную schema version. Если перенос не может сохранить поле, он явно отказывается вместо молчаливой потери данных.

### 5.3. Инженерный кандидат, не обязательный способ реализации

Для небольшого локального графа предлагаются UTF-8 `graph.json`, детерминированная сериализация и индексы `by_id`, `by_path`, `by_feature`, adjacency в памяти. При выборе JSON duplicate keys должны отклоняться. Иной формат допустим только с сохранением выбранного внешнего контракта и проверенной совместимости потребителей.

Размещение определяется в будущем выбранном repository: существующая область derived data, существующие development tools и tests. Короткая инструкция находится в owner/tool README; bootstrap содержит только маршрут.

Компактность достигается отсутствием повторов больших source texts и раздельным раскрытием evidence. Минимальный размер файла любой ценой не является целью.

## 6. Модель знаний

### 6.1. Node

Node представляет существующий component, entrypoint, symbol, artifact/contract, test, feature record или external reference. Inventory path сам по себе не требует semantic node.

Логические обязательные сведения: stable ID, kind, short label, source references, применимый locator, fact class, basis наблюдения, mapping state и evidence references. Exact field names фиксируются schema contract при реализации.

Факт существования и объяснение назначения — отдельные claims. Purpose/«зачем» имеет собственный источник и fact class. Объяснение агента остаётся `SYNTHESIZED`, даже если файл существует и его bytes проверены.

### 6.2. Edge

Edge содержит stable ID, source и target node IDs, typed relation, fact class, basis, evidence references и применимость к observation scope. Несколько связей между парой узлов допустимы; endpoint pair не является достаточной identity edge.

Повторное наблюдение того же утверждения может добавлять evidence. Разные отношения или утверждения не схлопываются.

| Relation | Направление и смысл |
|---|---|
| CONTAINS | Контейнер → существующий элемент |
| IMPORTS | Импортирующий модуль → разрешённый модуль/reference |
| CALLS | Caller → callee; basis отличает static от отдельно наблюдавшегося runtime |
| READS, WRITES | Компонент → читаемый/записываемый artifact/state |
| PRODUCES, CONSUMES | Компонент → производимый/потребляемый artifact/type |
| VALIDATES | Проверяющий компонент → объект проверки |
| TESTS | Тест → проверяемый subject; не утверждение о PASS |
| ROUTES_TO | Реальный dispatcher/configured route → target |
| BINDS_TO_FEATURE | Реализация/артефакт → существующий feature record |
| BINDS_TO_CONTRACT | Реализация/артефакт → существующий contract record |

Новый relation вводится для реального отношения, не выражаемого текущими типами и qualifiers. Обобщённый IMPLEMENTS не должен подразумевать полноту фичи. DEPENDS_ON не заменяет известную конкретную связь.

```text
producer --PRODUCES--> artifact <--CONSUMES-- consumer
```

Flow view может показать producer → artifact → consumer, но сохраняет смысл и направление исходного CONSUMES. Совпадение типов не доказывает фактическое wiring.

### 6.3. Sources и evidence

Source идентифицирует конкретную версию: repo-relative path, content digest и file kind. Evidence содержит собственный ID, source-version ID, symbol/anchor/range, вид наблюдения и короткое проверяемое утверждение.

При изменении bytes создаётся новый source-version binding; старое evidence не перепривязывается к новым bytes. В partial graph прежние bindings допустимы только с явной неприменимостью к текущей affected области.

Полный AST, документы и логи не копируются в граф. Для static evidence достаточно locator и binding. Runtime evidence ссылается на отдельный immutable test/run artifact с exact subject binding; граф не запускает тесты самостоятельно.

Digest доказывает привязку к bytes, а не правильность интерпретации. Семантический claim проверяется соответствующим extractor case или bounded review.

### 6.4. Identity и статусы

IDs не зависят от строки, позиции в массиве или текущего content hash. Способ построения ID — инженерный выбор. Кандидат для первого adapter: entity kind, repo-relative path и qualified symbol с явным различением коллизий. Rename без доказанной преемственности — remove/add. Преемственность при доказанном rename сохраняется лишь в поддержанном контракте identity.

Разделяются fact class, mapping state и execution status. Их сведения относятся к конкретному record/claim и scope; свежий node не повышает stale edge до current. Наличие теста допускает TESTS edge, но не execution PASS.

Неразрешённый callee/consumer хранится как unresolved: вопрос, evidence, search boundary и следующий read-only probe. Фиктивный internal node ради целостности ссылок запрещён. External dependency node не означает исследования её реализации.

`NOT_FOUND` ограничен поиском; `UNKNOWN` не означает отсутствие; `NOT_RUN` не означает отсутствие или неисправность кода.

## 7. Поддерживаемое извлечение и семантические наблюдения

### 7.1. Структурный минимум

Inventory paths, package/module boundaries, entrypoints, публичные symbols и нужные endpoints, imports, однозначные static calls, существующие schemas/types, тестовые связи и явные FTR/contract references.

Граф каждого AST-узла, local variable и строки документа не нужен. Coverage различает inventory, структурный разбор и исследованные data flows.

Первый adapter соответствует языку будущего проекта. Если выбран Python, stdlib ast — кандидат для структуры; parse success не доказывает исполнимость [W1].

### 7.2. Ограниченные semantic patterns

До реализации первого pilot перечисляются несколько поддержанных способов явного wiring, например разрешённый вызов, передача конкретного artifact между компонентами или явно заданная test binding. Для каждого указываются признаки достаточного evidence и случай, который должен остаться unresolved.

Похожие имена и типы не являются доказательством связи. Dynamic dispatch и неоднозначное разрешение остаются `UNKNOWN` либо отдельным `SYNTHESIZED` claim. «Один язык» не обещает полное семантическое понимание всех программ на этом языке.

Slice 1 не требует произвольного модельного обогащения. Сначала проверяются выбранные deterministic patterns и честное отображение их границ.

### 7.3. Необязательный observation batch

Если pilot выявит необходимость агентского исследования, `build` или `refresh` может принимать batch как **явный дополнительный input**, в поддерживаемом schema profile. Неявное получение batch из беседы или выполнение его содержимого запрещено.

Контракт batch включает собственную identity/revision, source bindings, список claims и locators, fact classes, declared search scope, unresolved и ограничения. Tool проверяет schema, ссылки, source identity, scope и конфликты; это не автоматическое признание модельной интерпретации фактом. Техническое принятие batch как входа не является Human acceptance.

Batch либо уже хранится вне active graph в разрешённом долговременном artifact существующего workflow, либо его claims считаются невоспроизводимым optional enrichment. Во втором случае они не могут быть единственным обязательным контекстом для работы или основанием обещания reproducible rebuild. Tool не создаёт автоматически новый registry, datastore или копию разговора.

Восстановление deterministic records обещается по source + extractor/profile. Восстановление batch claims обещается только при наличии exact batch и его source bindings. При изменении исходников такие claims пересматриваются, остаются stale/unresolved либо исключаются; прежнее толкование не переносится автоматически.

### 7.4. Документы и целевая архитектура

Наличие Product Contract наблюдаемо; его требования представляются как утверждения документа. Из них не создаются observed CALLS/PRODUCES к несуществующему коду. Принятие документа связывается с exact acceptance source, а не именем файла.

AS-IS не достраивается до желаемой target-схемы. Расхождения можно показать, но инструмент их не исправляет.

## 8. Пять операций и границы effects

Названия ниже — предлагаемый интерфейс, не команды, уже существующие в AOS.

| Операция | Input → output | Разрешённые effects при наличии write scope |
|---|---|---|
| build | Repo/scope/profile + optional supported batch → первоначальный graph и coverage | Только объявленный output и temporary publication resources |
| check | Graph + repo + declared scope → freshness/delta report | Нет |
| query | Graph + selector/mode/options → bounded result | Нет |
| refresh | Graph + repo/scope/profile + optional supported batch → graph/semantic diff | Только объявленный output и temporary publication resources |
| validate | Graph → integrity findings | Нет; validator не ремонтирует subject |

Temporary resources writers входят в разрешённый output scope; они не создаются reader/check/validate/help. Существующий чужой output не перезаписывается без явной применимой write authority. `build` не означает автоматическое разрешение заменить существующую карту.

Offline query сообщает stored binding и `repository_currentness: NOT_RUN`. Свежесть может подтверждаться только отдельным применимым check result, связанным с exact graph digest, repository/scope и observed inputs; parse success не устанавливает CURRENT. Способ передачи такого результата — часть выбранного интерфейса, а не неявное доверие старому процессу или timestamp.

Разрешённый graph update не требует нового approval на каждую запись. При отсутствии write authority доступен read-only check. Пустой новый repository допускает HEAD null с причиной; граф остаётся пустым или отражает существующие docs.

## 9. Запросы, impact и управляемое раскрытие

### 9.1. Selectors и смысловой запрос

Selectors: exact typed ID, repo-relative path, exact FTR-ID через существующие bindings. Неоднозначный ID возвращает неоднозначность, а не первый результат. Поиск по имени выдаёт кандидатов, не подменяет exact lookup.

Смысловой запрос определяется selector, mode, filters, direction и depth. Он задаёт множество подходящих записей в конкретном graph snapshot. Бюджеты страницы влияют только на представление этого множества.

| Mode | Результат и начальный depth |
|---|---|
| overview | Области, coverage, freshness и unknown boundaries; depth неприменим |
| context | Seeds и ближайшие связи с locators/evidence refs; direction both, depth 1 |
| impact | Потенциально затронутые mapped nodes и объясняющие цепочки; direction both, depth 2 |
| detail | Exact records/evidence с полными сохранёнными полями; обход не подразумевается |

Defaults — начальное предложение. Пользователь может явно изменить параметры. `impact` является областью проверки по известным связям, не доказанным радиусом воздействия.

### 9.2. Обязательное поведение impact

На поддержанном примере `P --PRODUCES--> A <--CONSUMES-- C` запрос `impact(P)` с defaults включает P, A, C и обе объясняющие связи, даже если они приходят на разных страницах. Направление CONSUMES не меняется при отображении цепочки.

Если пользователь задаёт depth 1, применимые filters или другую direction, исключающую C, ответ явно показывает смысловую границу: путь дальше не исследован данным запросом. Такой ответ не называется полным impact изменения P. Наличие продолжения страницы не снимает ограничение глубины.

Влияние дальше выбранной глубины остаётся за frontier запроса. Runtime effects, неизвестные consumers и неподдержанные semantic patterns не выводятся из успешного обхода.

### 9.3. Бюджеты страницы

Начальные defaults: `max_nodes_per_page: 40`, `max_edges_per_page: 80`, `max_output_bytes_per_page: 16384`. Для overview начальный byte budget — 8192. Размер считается в UTF-8 для всего ответа с metadata, не в tokens.

Node stubs входят в node budget страницы; каждый distinct node ID считается один раз на странице. Edge считается в edge budget. Metadata, evidence refs и uncertainty summaries входят в byte budget. Повтор stub на следующей странице допустим и не означает новый graph node.

Количество всех seeds не ограничивается node budget первой страницы. Ответ сообщает общий seed count, IDs seeds, показанных на этой странице, и способ раскрыть остальные. Полный список seeds доступен через continuation.

Все whole records выдаются без обрезки полей. Endpoints каждой выданной edge присутствуют на этой же странице как nodes или stubs. Подходящие records сверх лимитов откладываются в продолжение, а не теряются.

### 9.4. Полнота и continuation

Обязательная metadata: graph digest, selector/mode, применённые filters/direction/depth и page budgets, freshness scope, seed counts/IDs данной страницы, coverage limitations, page truncation, причины ограничения и continuation.

Глубина и filters — ограничения смысла запроса. Нехватка места на странице — truncation выдачи. Полнота выданного результата по graph не равна полноте знания о repository.

Продолжение детерминировано для graph digest и всех параметров запроса, включая page budgets. Старый cursor при изменении graph или параметров явно отклоняется. Все страницы одного запроса позволяют восстановить все подходящие records без потери parallel edges; дублированные stubs объединяются по ID.

Uncertainty не удаляется ради размера. Уже первая страница сообщает наличие критичных unknowns, их ограниченный summary и способ раскрыть все записи. Если полный список unknowns велик, он также раскрывается по страницам; отсутствие списка на первой странице не означает отсутствие неизвестного.

Если неделимый record вместе с обязательным envelope/endpoint stubs не помещается, вернуть `BLOCKED_OUTPUT_BUDGET` с требуемым действием. Бюджет меньше минимального поддержанного terminal envelope отклоняется как невалидный параметр. Exact errors фиксируются интерфейсом до реализации; нельзя обрезать JSON или объявлять результат полным.

### 9.5. Порядок

Сначала exact seeds и сведения о границах знания, затем прямые material interfaces/data/test relations, затем остальные records. Порядок страниц не скрывает подходящие связи и не изменяет определённое запросом множество.

Вся фича не обязана помещаться в 16 KiB. Требуются небольшой первый ответ, честные ограничения и доступность полного результата объявленного запроса.

## 10. Snapshot, freshness и selective refresh

### 10.1. Identity наблюдения

Отдельно фиксируются repository/worktree и режим наблюдения; HEAD при наличии; реально наблюдавшиеся paths/bytes и exclusions; schema/extractor/config/profile revisions; graph artifact digest.

Working-tree mode наблюдает допустимые dirty/untracked disk bytes, не подставляет commit state. Одинаковый HEAD не доказывает неизменность files; новый HEAD не доказывает изменение семантики.

Source fingerprint зависит от inventory, bytes и правил scope, а не времени запуска. Graph digest относится к полным сохранённым bytes и не включается в собственный хешируемый payload. Output graph, временные candidates и derived views исключаются из собственного source inventory. Revision extractor/config проверяется как условие применимости.

### 10.2. Freshness contract

Check сравнивает inventory и hashes в объявленной области. Git diff допустим как подсказка, но не единственное доказательство. Новый файл в проверяемом scope обнаруживается, даже если старый граф на него не ссылался.

Freshness: CURRENT, STALE, UNKNOWN с exact scope. CURRENT означает применимость проверенной части в пределах наблюдения, не полную карту и не гарантию будущего состояния.

Docs/config могут менять bindings и resolution; они не считаются несущественными автоматически. Scope/extractor/profile changes пересматривают применимую coverage.

### 10.3. Контракт обновления

Refresh учитывает изменённые, новые и удалённые sources, claims с затронутым evidence и условия разрешения связей. Ищутся также новые callers/consumers в declared search scope, а не только известные backlinks.

Даже неизменный caller может требовать повторного resolution после изменения target/config. Если узкую область определить нельзя, расширить разрешённое исследование либо оставить pending_refresh. Нельзя объявлять complete refresh на основании недоказанного предположения.

Удалённая сущность исключается из active topology вместе с невалидными links; semantic diff показывает удаление. Бесконечный tombstone journal внутри active graph не нужен. Исторические records сохраняются вне него только по существующему workflow.

Partial graph может содержать records разных наблюдавшихся версий, если их bindings, mapping states и coverage однозначны и ссылки целостны. Это не разрешение назвать их одним свежим snapshot. При parse/access/limit failure affected область не становится CURRENT; невозможно проверить перенесённый claim — значит он stale/pending/unknown в соответствующей boundary.

### 10.4. NO_CHANGE и физическая запись

Selective refresh означает повторное исследование необходимой области. Он не требует in-place изменения файла: полная сериализация небольшого artifact допустима.

При неизменных source, scope, extractor/profile и graph state результат `NO_CHANGE` сохраняет persistent bytes и modification time. Время check отражается в ответе, не создаёт пустой graph diff.

Commit только derived graph не создаёт self-refresh loop. Stored HEAD остаётся историей наблюдения; check отдельно сообщает текущий HEAD и применимость source bytes. Новая metadata сама по себе не требует перезаписи graph.

Порядок вычисления delta, индексы затронутых records и внутренний алгоритм обхода — инженерные решения, проверяемые указанными исходами.

## 11. Worktrees, публикация и восстановление

Каждый worktree имеет собственную локальную карту и binding. Общий mutable graph нескольких веток не требуется. Linked worktree не считается отдельным Git repository или security sandbox: часть metadata/refs общая [W2]. Tool не создаёт worktrees и не меняет refs/config.

После интеграции source карта проверяется/обновляется для результата интеграции. Textual merge generated graphs не доказывает актуальность. Перенесённый graph сначала остаётся snapshot прежнего subject.

### 11.1. Гарантии с первого writer

Безопасная публикация обязательна уже в Slice 1, где появляется build. При сбое до публикации существующий graph сохраняется. После публикации доступен целостный допустимый новый artifact, не промежуточный payload. Конкурирующая запись не приводит к молчаливой потере обновления; busy/conflict даёт явный отказ, без force takeover.

Перед объявлением fresh claim проверяется применимость source observation. Нет source lock — значит immutable captured bytes доказывают только ограниченный захват, а актуальность после него проверяется отдельно. Concurrent source changes не маскируются под согласованный fresh snapshot.

Способ publication, блокировки и контроля предыдущей revision выбирается реализацией. Кандидат: временный файл на той же файловой системе, проверка candidate, simple single-writer coordination, проверка expected previous digest и replace внутри согласованной writer boundary. Этот пример не предписывает lock protocol или отдельный сервис.

Успешный atomic replace не доказывает power-loss durability, не блокирует source files и не защищает от несогласованных внешних writers [W3]. Поддерживаемые OS/filesystem и фактически проверенная crash boundary объявляются явно.

### 11.2. Recovery и rebuild

Повреждённый graph не считается evidence. Recovery ограничен разрешённым output scope; source не ремонтируется, чужие artifacts автоматически не удаляются.

Derived graph восстанавливается из source + поддержанных extractor/profile inputs. Structural rebuild сохраняет те же поддержанные semantic records. Optional model summaries могут отличаться и не входят в обещание byte-identical rebuild. Batch-derived claims восстанавливаются только в условиях §7.3.

## 12. Безопасность, пределы обработки и сопровождение

### 12.1. Граница чтения

Сканирование не импортирует и не исполняет код проекта. Comments, docs, batches и graph payload — untrusted data, а не инструкции. Scope имеет allowlist/exclusions. Secrets, credentials, Git internals и private areas не читаются для содержания по умолчанию. Credential-bearing URLs не выводятся.

Symlink/traversal не расширяет разрешённый root. Access errors фиксируются как ограничения. Известные допустимые metadata-эффекты файлового чтения оговариваются профилем наблюдения; они не позволяют скрытые записи tooling или приписывание изменения неустановленному actor.

Сеть и новая внешняя инфраструктура первой версии не требуются. Выбирается уже принятый toolchain. Для Python-кандидата stdlib предпочтительна, но не служит доказательством безопасности неограниченного входа [W1].

### 12.2. Обязательный ресурсный профиль

До запуска pilot фиксируется поддержанный профиль: максимальный source file, суммарный source scope, graph input, optional batch, число records и допустимые затраты времени/памяти обработки. Числа выбираются по корпусу и среде, а не переносятся из старых AOS limits. Необъявленный предел не трактуется как обещание неограниченной поддержки.

Обязательное поведение при превышении: явная причина и affected scope; отсутствие source mutation; старый graph остаётся целым; unsupported source не превращается в отсутствие сущности. Успешный partial graph допустим только с visible coverage/pending и без ложного CURRENT для пропущенной области. Если целостность partial result недоказуема, candidate не публикуется.

Контракт отделяет budget ответа от budget обработки. Маленькая выдача не разрешает неограниченное потребление ресурсов. Способ ограничения parser/process — инженерное HOW. Если environment не позволяет обеспечить заявленную гарантию, поддержка такого профиля не объявляется.

Negative fixtures включают слишком большой source, слишком сложный input, oversized graph/batch и исчерпание времени/памяти в пределах проверяемой среды. Требуется terminal result там, где процесс способен его безопасно выдать; при аварийном завершении внешний результат остаётся явным failure, а active graph не повреждается.

### 12.3. Стоимость сопровождения

Обычное использование — явный разрешённый refresh и короткий semantic summary. Markdown-map и JSON-map не поддерживаются как два редактируемых owners. Неточность графа ограничивает affected claims; безопасное прямое исследование продолжается.

Storage пересматривается по измеренным расходам чтения, записи, памяти, конфликтам и review, а не по произвольному числу bytes. Увеличение числа файлов само по себе не считается улучшением.

## 13. Рабочий цикл

1. **Bootstrap:** выбрать root/scope/profile; создать только наблюдаемые nodes. В пустом проекте не предсказывать runtime.
2. **До задачи:** check применимой области → context/impact → чтение первичных источников существенных решений. Freshness не заменяет семантическую проверку.
3. **После изменения:** разрешённый refresh или, в Slice 1, разрешённая полная пересборка малого scope → semantic diff и проверка coverage. Product tests не запускаются неявно.
4. **Handoff:** graph digest, observation boundary, запрос и следующий probe. Новый агент не обязан читать полный graph payload.

Это встраивание в существующий task workflow. Оно не создаёт новую lifecycle-машину или execution authority.

## 14. Проверяемые критерии приёмки

### 14.1. Функциональные сценарии

| ID | Сценарий | Условие успешной проверки |
|---|---|---|
| AC-01 | Пустой проект | Нет выдуманной реализации; HEAD null допустим; coverage ограничена |
| AC-02 | P → artifact ← C + test | Типы, направления, wiring/evidence сохранены; runtime PASS не выдуман |
| AC-03 | Lookup ID/path/FTR | Correct deterministic seeds, неоднозначность видима; FTR — только если binding поддержан |
| AC-04 | Context + continuation + detail | Страницы в budgets; полный результат объявленного запроса восстановим |
| AC-05 | Изменён shared type, добавлен consumer | Обнаружен новый path; рассмотрены старые и новые отношения |
| AC-06 | Dirty bytes, прежний HEAD | Disk delta распознана, commit не подставлен вместо disk |
| AC-07 | Partial refresh | Непроверенная область не стала CURRENT; старые bindings и pending читаемы |
| AC-08 | Повтор без изменений | NO_CHANGE, persistent bytes/mtime сохранены |
| AC-09 | Сбой publication, другой writer | Старый graph цел; нет silent overwrite/source mutation |
| AC-10 | Rebuild/round-trip | Сохранены types, directions, uncertainty и поддержанные claims; counts недостаточны |
| AC-11 | Два worktrees | Bindings и bytes не смешаны; чужой graph не признан current |
| AC-12 | Реальный вопрос уже в Slice 1 | Правильный ответ сверяем с независимым oracle; польза сравнивается с обычным поиском |
| AC-13 | impact(P) по defaults | Показаны artifact, consumer и объясняющие связи; depth 1 показывает frontier |
| AC-14 | Несколько страниц seeds/edges | Page limits не ограничивают всё множество; stubs учтены; parallel edges не потеряны |
| AC-15 | Optional batch, если включён | Input identity/claims/provenance сохранены; rebuild учитывает доступность batch |
| AC-16 | Processing limits | Превышение видно; старый graph цел; нет ложной current/full coverage |

### 14.2. Negative fixtures

Это требования к будущим проверкам, не отчёт об их выполнении.

| ID | Fixture | Ожидаемый результат |
|---|---|---|
| N-01 | Duplicate IDs, dangling refs, malformed payload; duplicate keys при JSON | validate FAIL без ремонта subject |
| N-02 | Две A → B связи и B → A | Все сохраняются после записи, чтения и query |
| N-03 | Документ утверждает «реализовано» без проверки | REPORTED; observed implementation не появляется |
| N-04 | Тест существует, не запускался | TESTS binding, execution NOT_RUN |
| N-05 | Проверена A, B не читалась | No match в A не означает отсутствие во всём repo |
| N-06 | Новый C, неизменный P | C обнаружен либо явный pending; нет ложного complete refresh |
| N-07 | Удалён symbol, недоказанный rename | Нет dangling edges; identity не угадывается |
| N-08 | Изменён только graph output | Нет self-refresh loop |
| N-09 | High-degree graph, много seeds/unknowns | Whole records, counted stubs, budgets, продолжение и честные summaries |
| N-10 | Новые bytes по прежнему path | Старое evidence не считается свежим |
| N-11 | Cursor от другого digest/параметров | Явный отказ без смешивания страниц |
| N-12 | Parse/access failure | Affected records не повышаются до CURRENT |
| N-13 | Symlink escape, traversal, инструкции в source/batch | Scope не расширяется; payload не исполняется |
| N-14 | Второй writer, сбой до публикации | Old/new целостность, отсутствие потерянного обновления |
| N-15 | Изменились только shared Git metadata другого worktree | Не подменяют source delta выбранного worktree |
| N-16 | Reader/check/query/validate/help | Нет hidden writes, locks, caches или test execution |
| N-17 | impact(P), depth 1 | Consumer за frontier не выдан как проверенно отсутствующий |
| N-18 | Page cap 40 при 41 подходящем node | Остаток доступен продолжением; полный запрос не урезан до 40 |
| N-19 | Single record/endpoint envelope больше page budget | BLOCKED_OUTPUT_BUDGET, не обрезанный payload |
| N-20 | Batch stale, конфликтующий или недоступен при rebuild | Claims не повышены; ограничение/отказ явны |
| N-21 | Source/graph/batch превышает ресурсный профиль | Явный limit result, сохранность active graph |
| N-22 | Слишком сложный input или processing failure | Нет ложного PASS; проверена заявленная boundary сохранности |

### 14.3. Доказательство полезности и стоимость

**В Slice 1** выбирается один реальный вопрос о зависимости. До использования графа задаются exact snapshot, вопрос, существенные правильные связи, допустимые unknowns и oracle из первичных источников. Затем сравниваются обычный поиск и graph-assisted поиск. Evaluated reader не определяет собственный правильный ответ.

Подготовка oracle не подсказывает искомые связи участнику измерения. Если один агент повторяет поиск уже зная ответ, эффект обучения фиксируется; второе время не выдаётся за чистое преимущество инструмента. Отдельные агенты не обязательны: допустимы равноценные задачи или ограниченный честно описанный trial.

Технический PASS требует правильного положительного ответа в поддержанном случае и ожидаемых negative outcomes. Система, всегда возвращающая UNKNOWN или корректный отказ, не проходит положительный сценарий. Недоступный positive run остаётся NOT_RUN/BLOCKED.

Результат пользы отделяется от correctness. Само обнаружение связи недостаточно, если обычный поиск обнаруживает её с теми же или меньшими затратами. Для продолжения разработки требуется хотя бы начальный сравнительный сигнал: предотвращённый material miss относительно baseline либо снижение суммарных затрат без роста material misses/false positives. Если преимуществ нет или данные неразличимы, это прямо фиксируется и расширение до следующих срезов не обосновывается одним technical PASS.

**Для решения о дальнейшем внедрении** сравниваются минимум три вида задач на сопоставимых условиях: локальная правка, изменение общего контракта и добавление consumer. Учитываются:

- missed material relations и ложные связи;
- время поиска/ориентации и дополнительного чтения первичных источников;
- стоимость первоначального построения, semantic review, refresh/rebuild, исправления mapping и сопровождения batch;
- bytes первой страницы и всех страниц, число source reads;
- peak memory, cold load, warm query, refresh и объём persistent data;
- tool revision, hardware, profile, selectors, budgets, порядок и число повторений.

Initial build cost показывается отдельно и включается в суммарное сравнение на заранее объявленном числе задач. Нельзя амортизировать её на произвольное будущее число использований только ради положительного результата.

Начальные цели: context first page до 16 KiB, overview до 8 KiB; warm context на фиксированном локальном корпусе масштаба прежней карты — median до 1 секунды. Это кандидатные budgets/SLA, не proof of utility. Cold load и полное раскрытие измеряются отдельно; превышение требует анализа, не автоматического внедрения БД.

Один положительный trial — сигнал для следующего ограниченного шага, не доказательство универсальной эффективности. Исторические timings из S6 не являются нормативом нового инструмента.

## 15. Срезы и поставка

### Slice 1 — полезный проверяемый ответ

Один язык, одно окружение, небольшой реальный scope, несколько поддержанных patterns. Build, validate, exact query и минимальный impact/context, достаточный для выбранного вопроса. Coverage/unknowns и безопасная публикация присутствуют сразу. Full rebuild малого scope допустим вместо selective refresh.

Обязательная проверка среза: реальный вопрос и oracle из §14.3; корректный положительный ответ и отдельный отрицательный случай. Применимые AC-01–03, AC-09–10, AC-12–13, AC-16 и negatives для integrity, untrusted input, source binding, publication и limits. Полная general-purpose pagination и optional batch не обязательны, если pilot честно ограничивает корпус/запрос и явно отказывает на превышении без ложной полноты.

Выход: фактический полезный ответ, измерение против обычного поиска, limits и решение о целесообразности следующего среза по существующему workflow. Не требуется сначала завершить инфраструктуру всего проекта.

### Slice 2 — сопровождение доказанного участка

Check; changed/new/deleted sources; selective refresh; partial coverage; NO_CHANGE; worktree binding; дополнительные recovery/concurrency cases. При необходимости поддерживается явный observation batch по §7.3. Реальный сценарий повторяется после source changes; correctness старого graph не переносится автоматически.

### Slice 3 — расширение выдачи и повторяемость пользы

Полные context/impact/detail с page budgets и continuation, нужные feature/contract bindings, task comparison минимум трёх видов. Срез завершает применимые AC/N всей выбранной версии. Optional batch без доказанной необходимости остаётся вне реализации.

Первый usable вариант допускает отказ от graph-assisted маршрута и продолжение обычной разработки. Автоматизация не добавляется до доказанного повторения ручного сценария.

### Поставка

Небольшой tool/module в выбранном repository, schema contract, fixtures/tests, короткая инструкция в существующем owner, один воспроизводимый example graph и report с metrics/limitations. В каждом срезе перечисляются реализованные требования и оставшиеся NOT_RUN; неполный срез не выдаётся за весь R2.

Десятки мегабайт replay artifacts не включаются в active graph или обязательную поставку. Нужные доказательства сохраняются по существующему workflow.

Миграция нынешней карты AOS-3 — отдельное решение. Если она выбрана, importer доказывает round-trip с сохранением unknown fields/statuses и поддержанной семантики; иначе отказывается от неподдержанного переноса. Наблюдение будущего repo с нуля допустимо. Это не разрешение удалить прежнюю карту.

## 16. Решения перед запуском и следующий шаг

Перед реализацией выбранного Slice 1 определяются: будущий repository/worktree и write scope; поддержанные язык/OS/filesystem; реальный вопрос и corpus; patterns, inputs и oracle; schema/interface/error contract; ресурсный профиль. Это уточнение выбранной задачи, не требование полного проектирования всех срезов.

Формат хранения, структура индексов и механика публикации выбираются как reversible HOW в допустимой boundary. Optional batch и legacy import явно включаются или остаются вне scope. Необходимые protected product/architecture decisions принимаются по существующим владельцам.

ТЗ не выбирает FTR, не разрешает пересборку AOS, runtime notebook или Git delivery. Feature-specific contract и разрешение на execution оформляются в существующем процессе; R2 может служить их основой, но не подменяет их.

Один следующий bounded action: рассмотреть R2 как proposal. При явном выборе будущей реализации уточнить Slice 1 вокруг одного реального пользовательского вопроса и проверить полезность до развития инфраструктуры сопровождения.

Текущий статус: создание черновика выполнено; implementation, product/runtime validation, pilot и независимое review R2 — `NOT_RUN`. Уверенность в provenance, authority separation и bounded retrieval высокая; полезность инструмента, ресурсные числа и SLA остаются гипотезами до измерения.

## Источники и provenance

### Project sources

- **S0 — исходный R1:** полный текст `AOS_REPOSITORY_GRAPH_TZ_R1`, предоставленный пользователем в этом диалоге 2026-09-13. Это основа редакции, не принятая архитектура. Отдельная byte-identical копия R1 и её hash в рамках R2 не создавались.
- **S1 — [00_Core.md](../docs/00_Core.md):** authority/fact classes, Minimal Safety Floor, WHAT/HOW, future decisions. Применяется к notebook; исторический `UNASSIGNED` не переносится на AOS-3 как current runtime fact.
- **S2 — [02_Architecture.md](../docs/02_Architecture.md):** §§8–14,17; ownership, derived context, recovery и отложенная сложность. Candidate topology не принимается за обязательную реализацию.
- **S3 — [03_Development.md](../docs/03_Development.md):** §§16–22; verification, validation boundary, recovery, Git и manual dogfood. Manual dogfood находится в §22; ссылка R1 на §21 для него уточнена.
- **S4 — [04_Lessons.md](../docs/04_Lessons.md):** LES-028,030,035,038,047–049. Использованы task-scoped context, положительный journey, применимость reproducer, диагностика и сохранность причин отказа. Lesson proposal не становится policy от ссылки в R2.
- **S5 — [06_Features.md](../docs/06_Features.md):** FTR-002,016,021 — тематические dossiers, не выбор implementation scope.
- **S6 — [EXPERIMENT_REPORT.md](../../AOS-3-as-is-graph-bundle-r2/development/research/as-is-project-map-experiment/reports/EXPERIMENT_REPORT.md):** исходный отчёт `AOS3_AS_IS_GRAPH_BUNDLE_EXPERIMENT_R2`, прочитан при оценке R1. Исторический base `3b55c4397f93beeb0d279cf0201ecc232bd50166`, captured map SHA-256 `2db923e4ff79bcde3d9f05a2c81b0f3c9f845c5d2487be43aea9bf2f1f5ef627`. Результаты остаются REPORTED; независимое воспроизведение в R2 NOT_RUN. Отчёт содержит рекомендацию KEEP_MONOLITH, смешанную latency и отсутствие измерения реальных переделок.
- **S7 — mapping refresh и terminal-state reports:** в R1 переданы пользователем в виде сводных результатов. Выборка 6 432 bytes здесь сохраняется как REPORTED из S0; первичный отчёт этой выборки отдельно для R2 не проверялся. Эта величина не обосновывает SLA и не используется как норматив нового инструмента.

Локальные ссылки на S1–S5 относятся к текущим файлам notebook, включая разрешённые изменения уроков и provenance перед подготовкой R2. Они не являются byte-identical копиями `.txt`, перечисленными в R1. Старые `.txt` hashes не переносятся как hashes прочитанных файлов R2. Разрешимость ссылок проверяется при подготовке; future mutable state проверяется перед применением.

S6 находится в отдельном локальном experiment worktree, не является runtime dependency и может стать недоступен. При отсутствии source нельзя восстановить факты из имени файла; зависимый research получает BLOCKED_REFERENCE_ACCESS. Historical report не подтверждает текущую готовность AOS-3.

### Технические источники

- **W1 — [Python ast](https://docs.python.org/3/library/ast.html#ast.parse):** проверено при оценке R1 2026-09-13. AST parse не гарантирует исполнимость; достаточно большой/сложный input способен привести к отказу интерпретатора. Основание для ограничения claims и обработки inputs, не выбора Python заранее.
- **W2 — [Git worktree](https://git-scm.com/docs/git-worktree):** REFS и DETAILS проверены при оценке R1 2026-09-13. Часть refs/config общая, часть state специфична worktree. Это не authorization на Git actions.
- **W3 — [Python os.replace](https://docs.python.org/3/library/os.html#os.replace):** проверено при оценке R1 2026-09-13. Успешный rename atomic в оговорённых документацией условиях; полная crash durability и конкурентная безопасность не следуют из одного вызова.

В подготовке R2 внешние эксперименты и runtime не запускались. Редакционные и Markdown-проверки сообщаются отдельно от product acceptance.
