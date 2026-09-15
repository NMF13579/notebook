# Граф RAG — единый вход будущей разработки модуля

Дата: 2026-09-14. Статус: `DRAFT_HANDOFF_WITH_OPEN_INPUTS`. Предмет: существующая **FTR-017 «Граф RAG»**, модуль **«Граф RAG»**, состав **[FTR-017]**. Документ производный; требования принадлежат перечисленным ниже owners. Реализация и Git-действия не разрешены этим brief.

**Аннотация простыми словами.** Модуль помогает агенту найти нужные документы и код, увидеть связи, сравнить наблюдаемое состояние с замыслом и подготовить контекст следующего действия. Он показывает пробелы и ограничения вместо догадок. Человек не обязан строить граф или разбираться в формате данных. Поиск и сравнение входят в одну фичу; работать с ними можно по отдельности, когда это достаточно для задачи.

## 1. Задача и результат переноса

Изучить предоставленный R3, адаптировать к нынешнему протоколу совместимости, включить в текущую RAG-фичу и использовать её для одноимённого модуля. Устранить столкновения с AOS-3 namespace/owners и прежним graph-only R2; сохранить происхождение и проверяемые критерии. Runtime, новые FTR, изменение frozen ТЗ интервью и Git delivery не входят в работу.

Направление, название и состав подтверждены текущей инструкцией пользователя. Это не утверждение всех technical HOW или выбора даты/среды реализации. Сохраняемый `human_disposition: UNDECIDED` в dossier относится к отбору для реализации; он не отменяет указанное решение о составе.

| Что нужно прочитать | Единственный владелец |
|---|---|
| Назначение, users, первая область и не-цели | [Product](../docs/01_Product.md#repository-graph-purpose) |
| C-002: trigger, I/O, flow/states, failures/recovery, constraints, 62 критерия G/R, прежние S/N | [FTR-017](../docs/06_Features.md#ftr-017-contract) |
| Source identities, Target/Observed/Mapping/Delta, интерфейсы, ownership, effects/versions/lifecycle | [Architecture](../docs/02_Architecture.md#graph-rag-module-contract) |
| Один parent, внутренний порядок, 96 source cases, GR-C01–10 совместимости и GR-DI01–10 impact, installed/E2E и benchmark | [Development](../docs/03_Development.md#graph-rag-verification) |
| Источник, SHA, преобразования и ограничения проверки | [Reference](../docs/05_Reference.md#graph-rag-r3-source) |

## 2. Сверка с протоколом совместимости фич

Это self-check документационного контракта по [§25.4](../docs/03_Development.md#feature-module-protocol), а не runtime admission.

| Шаг | Результат/основание | Что ещё требуется для исполнения |
|---|---|---|
| 1. Предмет/дубли | Существующая FTR-017 расширена, новая Graph FTR не создана; одна запись модуля в inventory | Принятая revision контракта и scoped implementation decision |
| 2. Поведение C-002 | Dossier содержит процесс, ограничения, отказы/recovery и индивидуальные G01–38/R01–24 | Привязка критериев к actual tests/oracles |
| 3. Composition/data ownership | Поиск и сравнение используют corpus независимо; FTR-016 остаётся Context Pack owner; нет cyclic bootstrap или второго scheduler | Сверить реальные producers/consumers выбранной реализации |
| 4. C-015/C-016 | find/compare/context/check — DIRECT_READ; refresh/save — QUEUED_COMMAND через core; event subscriptions N/A с причиной | Concrete profile: versions/handlers/generation, finite limits и текущие read/write capabilities |
| 5. Lifecycle | ADD/ENABLE/UPDATE/DISABLE/REMOVE/DELETE разделены, in-flight reconciliation и сохранение user records описаны | Испытать writer/migration/disable/fallback на disposable target |
| 6. Semantic readiness | 62 source criteria, 96 source scenarios, GR-C01–10 и уточнения GR-DI01–10 связаны с current contracts; отсутствие runtime Evidence явно | Actual public boundary и independent oracle; missing input ограничивает dependent readiness |
| 7. Автономный вход | Один этот brief собирает goal, состав, dependency order и вопросы; HOW не требует нового planning каждого шага | Exact target/effects/check commands/budgets/resume и отдельная C-005/C-006 authority |
| 8. Completion | Whole-project integration/installed journey/core fallback и единый review определены у Development | Реализация, Validate/Review и applicable human acceptance не выполнены |

Техническое соответствие структуры документации не доказывает runtime совместимость. Общий статус готовности к исполнению — `BLOCKED` незаданными exact inputs; это не блокирует дальнейшее обсуждение и документационные изменения.

## 3. Снятые противоречия источников

1. R3 предлагал новую Graph candidate + существующую retrieval FTR. Текущая инструкция объединяет их в FTR-017, сохраняя отдельные группы поведения и критериев.
2. Notebook R2 исключал RAG и Target/Observed comparison из первой версии. Текущий Product scope расширен; старый файл R2 остаётся историческим источником, а не конкурирующим owner.
3. Архивные AOS-3 IDs, `aos/src/...`, `build_context_pack(...)` и 31-feature inventory не являются API/структурой будущего AOS. Перенесена семантика owners, не topology.
4. Архивный local save/refresh согласован с current C-016. Read-only query не пишет cache и не создаёт скрытую команду ради результата.
5. Две проекции не две нормативные базы. Freshness каждой зависит от её inputs; general coherence/hash/relevance не подтверждают истинность, authority или completion.
6. Численные budgets, scorer, JSON wire schema, storage и macOS arm64 из R3 остаются предложениями профиля. Один hop поиска не обещает двухшаговый consumer impact. Exact поддержка доказывается на выбранной среде.
7. `PASS` source package checker сохранён как исторический отчёт; он не доказывает работу модуля. Архивные scripts не запускались и не устанавливались.

## 4. Оставшиеся входы перед реализацией

Агент сначала читает текущие документы и использует уже принятые применимые решения, а не спрашивает их повторно. Обратимые HOW выбирает внутри scope. Материальные product/authority решения не придумывает.

| ID | Что выяснить простыми словами | Действие агента и влияние |
|---|---|---|
| GR-I01 | Где будем создавать и проверять работающий модуль? | Связать exact implementation repo/target/base и paths/effects. Notebook остаётся knowledge repository; отсутствие блокирует реализацию, не документы |
| GR-I02 | Через какие разрешённые средства модуль читает файлы и сохраняет свои результаты? | Найти current admitted reader/writer/registration/queue, профиль metadata/service effects; подтвердить safe capture/publication/recovery на disposable subject. Не переносить обход FTR-009 из предположения о host |
| GR-I03 | В какой конкретной версии агентной среды должен работать первый полный путь? | Учесть ранее выбранное направление Codex первым и нейтральность ядра; связать фактический host/version/OS/transport/dependencies/tokenizer при необходимости. Это уточнение технического профиля, не повторный выбор продукта за человека |
| GR-I04 | Какие старые карты действительно нужно импортировать? | Optional: определить exact format/IDs и проверить сохранение semantics. Без импорта поддержанный local build остаётся допустим; полная AS-IS AOS-3 карта в R3 не была прочитана |
| GR-I05 | Какие точные интерфейсы, форматы и пределы поддерживает выбранная сборка? | Сверить текущих consumers/C-009/C-010/C-015/C-016, конечные лимиты, data revisions, roles/paths и test commands. HOW выбирается после проверки возможностей; не копировать schema/scorer автоматически |
| GR-I06 | На каком реальном примере проверим, что модуль помогает? | Подготовить bounded corpus/query/source oracle и сравнение direct/lexical/graph. Измерить качество, cold/refresh/retries/host/human effort. До этого поддержка/экономия не заявляются |

Для первого build агент формирует один конкретный пакет недостающих решений после сверки существующих. Материальный unknown блокирует только зависимые эффекты/claims; optional import или embeddings не становятся условием всего модуля. При принятом scope обычные коррекции не требуют повторного продуктового интервью.

## 5. Исторический статус проверок переноса R3

- `PASS` — проверка контейнера ZIP и всех внутренних SHA-256 bindings; оригинал сохранён как source.
- `PASS` — source критерии G/R перенесены с mapping на исходные scenario IDs; current module protocol дополнен в owners.
- `NOT_RUN` — выполнение архивных Python scripts, runtime/installed/native E2E, benchmark, independent validation, Git delivery.
- `PASS` — затронутые Markdown links/anchors/fences, YAML frontmatter и `git diff --check`; сохранены семь canonical owners и 33 уникальных FTR. Кроме FTR-017, в трёх смежных dossiers изменены только routing-ссылки на модуль.
- `PASS` — утверждённое ТЗ интервью и approval совпадают с bytes до переноса; SHA ТЗ остался `7ff1e6f74f26c72ae7ee1df4138c6ce2570c6002e973efdbef5ced537e07bc5b`.

Следующий предмет после документационного review — закрытие необходимых inputs одной будущей сборки. Само наличие brief не запускает её.

## 6. DIP-R1: ограниченное уточнение существующей фичи — 2026-09-15

Текущая инструкция разрешила документационное встраивание полезного impact-поведения. [Provenance и исключения](../docs/05_Reference.md#graph-rag-dip-source), [поведение](../docs/06_Features.md#graph-rag-impact-behavior), [C-015 profile/совместимость](../docs/02_Architecture.md#graph-rag-impact-contract), [GR-DI01–10](../docs/03_Development.md#graph-rag-impact-verification) остаются у owners. Это одна FTR-017, прежний parent и внутренний LINKED_CONTEXT; новое feature selection или runtime admission не выполнялись.

В GR-I05 теперь явно входит связывание DATA_CONTRACT_IMPACT_V1 с поддержанной payload revision, limits и caller/FTR-016. Старый consumer не должен принимать impact как обычный поиск; обычный find сохраняется. Импорт DIP schema, graph database, отдельный registry и selective refresh не являются предпосылками. GR-I01–06 остаются входами будущей реализации; реализационные структуры/алгоритмы не задаются этой документацией.

Авторская репетиция изменённого контракта по §25.7, без runtime:

| Ситуация | Следующий шаг и документальное основание |
|---|---|
| Достаточный вход | Один связанный producer/data/consumer → find → объяснение host, GR-DI01/10. Возвращаются potential candidates, не утверждение о дефекте |
| Неполный вход | Нет provider binding — условный результат GR-DI06; неоднозначный subject — одно уточнение. Не выбирать связь по label |
| Противоречие | Conflicting применимые claims ограничивают путь, GR-DI04; valid независимое основание сохраняется, GR-DI05. Material owner decision не синтезируется |
| Недоступная зависимость | Permitted direct fallback без заявления полного impact, GR-DI09; FTR-021 не required. Отказ в чтении не обходится |
| Обычный дефект | Неверное направление/смешение hops обнаруживает GR-DI01/02; будущий исполнитель исправляет реализацию в покрытом scope и повторяет affected checks. Обратимый HOW не требует нового product decision |
| Прерывание/повтор | Новый query binding не продолжает старую страницу, GR-DI09; неизвестный save разрешается через прежние GR-C04–06, не скрытый replay |
| Сломанный стык | Caller теряет ограничения или old consumer принимает чужую revision — GR-DI09/10 и GR-C07/C09 отклоняют общий результат при unit PASS |
| Завершение | Нужны действительный public/installed путь, negatives и актуальное Evidence; документальная таблица не закрывает parent. Текущий runtime, benchmark и independent review — NOT_RUN |

Попытка «две реализации»: обход всех REFERENCES и typed data-contract traversal давали бы разные affected sets; первый исключён Architecture impact и GR-DI03. Свобода выбрать in-memory или file-based представление сохраняется, если наблюдаемое поведение одинаково. Попытка «плохая реализация проходит»: всегда UNKNOWN/пустые sets либо ответ по case ID отвергнуты positive GR-DI01/02/10 и независимым source oracle. Это авторская проверка содержания; фактическая работоспособность адаптера/host остаётся `NOT_RUN`.
