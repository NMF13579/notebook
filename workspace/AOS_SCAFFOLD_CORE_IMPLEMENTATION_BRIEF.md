# AOS — scaffold и первое ядро: implementation brief

Дата: 2026-09-13. Revision: R7. Статус: SCAFFOLD_CORE_DRAFT, предмет человеческого решения. Runtime implementation authorization: NONE. Git authorization: NONE.

Этот brief подготовлен по [документационному плану](AOS_SCAFFOLD_CORE_AUTONOMOUS_DEVELOPMENT_PLAN.md) в worktree `work/scaffold-core-autonomy`, от HEAD `8627d1cc01b84a794827673e473850c0187abe5e`. Это checkout документации, а не implementation target. Изменённые owner bytes входят в новый candidate; прежние acceptance и audit hashes не принимают его автоматически.

## 1. Цель, объём и non-goals

После отдельного принятия contracts и launch authority внешний агент строит development scaffold и первое ядро AOS до проверенного технического результата, включая обычную correction, сохранение состояния и supported resume. Человек заранее задаёт outcome и существенные границы; внутри согласованного интервала не требуется ручная постановка каждого следующего шага.

Владелец продукта получает один review package: что сделано, какие критерии доказаны, что осталось NOT_RUN/UNKNOWN, какой exact candidate проверен и как продолжить работу. Human acceptance и Git delivery следуют отдельно.

Scope принадлежит [Product S0–K4](../docs/01_Product.md#scaffold-core-outcome) и [базовым возможностям dossiers](../docs/06_Features.md#core-first-scope). Используется предложенный минимальный объём 13 CORE-семейств; это не принятие полного функционала каждой семьи. Scaffold разработки не включает полный installer FTR-004. Optional-модули не реализуются одновременно с ядром только ради общих ссылок.

Вне интервала: миграция/очистка старых repositories, автоматические Git actions, public release, одновременное подтверждение поддержки всех ОС, plugin platform, remote CI, RAG/graph, routing, SaaS/UI и domain modules. Необходимый новый material contract или effect требует отдельного решения; обратимый implementation HOW остаётся за агентом.

Переносимость архитектуры обязательна с S0. Человек выбрал macOS первой
проверяемой средой; Linux/Windows — целевые платформы с последующим native
подтверждением. macOS-first не означает macOS-only. Владельцы требований:
[Product](../docs/01_Product.md#core-os-portability),
[Architecture](../docs/02_Architecture.md#core-platform-boundary),
[проверки ОС](../docs/03_Development.md#core-platform-checks).

## 2. Ограниченный маршрут чтения

| Порядок | Owner и что из него необходимо |
|---|---|
| 1 | [Core: решения и authority](../docs/00_Core.md#scaffold-core-decisions) — применимость старых решений, SC-DEC-01…04 и Human boundaries |
| 2 | [Product: результат/S0–K4](../docs/01_Product.md#scaffold-core-outcome) — цель, достаточные входы и критерии каждого среза |
| 3 | [Features: первый core](../docs/06_Features.md#core-first-scope) — только 13 указанных dossiers и разделы «Первый core-срез», полные safety/negative требования выбранных сценариев |
| 4 | [Architecture: профиль](../docs/02_Architecture.md#scaffold-core-profile), [host](../docs/02_Architecture.md#scaffold-core-host), [стыки](../docs/02_Architecture.md#scaffold-core-interfaces) и C-005…C-012, [C-015/C-016](../docs/02_Architecture.md#module-connector-queue) — обязательные гарантии, owner/consumer и versions |
| 5 | [Development: исполнение](../docs/03_Development.md#scaffold-core-development) — внешний loop, preflight, worker boundaries, checks, interruption и итоговое завершение |
| По точному gap | [Reference](../docs/05_Reference.md#scaffold-core-sources), затем названный source; lesson применяется только к соответствующему failure |

Brief — производный handoff, не новый владелец contracts. При расхождении возвращаться к owner и разрешать exact conflict до зависимого effect. Не читать/переносить весь archive, frozen package или прежний blueprint вместо этого маршрута.

## 3. Входной пакет будущего запуска

Сейчас ни один placeholder не является разрешением. Перед launch эти inputs должны быть конкретными и согласованными:

| Вход | Предложение / требуемое заполнение | Текущее ограничение |
|---|---|---|
| Product subject | Принятые exact S0–K4, core-срезы dossiers и current owner revisions | SC-DEC-01: WAIT_HUMAN; направление автономной разработки уже задано |
| Task subject | Один C-005 с task/revision, criteria IDs, dependency order и проверяемым overall outcome | Этот brief описывает будущую task; issued task/authority binding отсутствует |
| Repository | Exact repository/root/worktree/branch/base; исходный inventory и allowed/protected paths | SC-DEC-02: OPEN. Старое имя AOS-3 не означает разрешение менять существующий checkout. Notebook остаётся knowledge repository |
| Runtime/environment | Минимальные локальные коннекторы/сохраняемая очередь и смешанный direct/queued exchange выбраны человеком. Переносимое ядро, macOS проверяется первой. Предложены local Python 3.12+/CLI и минимальный локальный adapter с переносимым интерфейсом; exact OS/runtime/architecture, adapter tool, dependencies, outputs ещё определить | Порядок ОС задан человеком; остальные параметры SC-DEC-02 OPEN. Native support NOT_RUN |
| Product data | Repository-relative durable state/evidence, registration/queue/operation history и finite capacity/payload/wait/claim/retry/retention profile; исходные user inputs, ownership/access и sensitive ограничения | Storage HOW — агентский выбор в принятом contract; data/capture policy требует SC-DEC-03 |
| External host | Identity, trusted human capture/admission, real tools/adapter, checkpoint и continuation trigger | SC-DEC-03: OPEN. Получить текущее conformance Evidence; prompt не является механизмом wake |
| Runtime authority | Assigned Risk Profile, parent task/revision/subject, requested→allowed operations/paths/effects, запреты, limits, expiry/revocation | SC-DEC-04: NOT_RUN; parent создаётся человеком отдельно, worker envelope выводится controller/host в более узком scope |

В предлагаемом запросе runtime authority нужны: ограниченное локальное создание/изменение продукта и его tests/docs в выбранном target, запуск объявленных local checks, bounded reversible correction, запись state/evidence и разрешённые disposable probes. Конкретные paths/commands/effects фиксируются до dispatch в task/action binding. Установка зависимостей, provider use и test-generated artifacts требуют своей явно покрытой области; их нельзя выводить из общего «сделай проект».

По умолчанию запрещены выход за target/test boundary, изменение unrelated user state, secret access, неразрешённые network/provider effects, destructive recovery, изменение принятых product/security boundaries, Commit/Push/Merge/Release. Пустые allowlists запрещают effects, а пустые limits не означают бесконечный ресурс.

Используется предложенный [согласованный набор V3](../docs/02_Architecture.md#core-loop-v3).
Он остаётся DRAFT до принятия; V1/V2 records и host reports не получают автоматического
V3 resume. SC-DEC-04 должен покрывать создание служебного state/evidence; bootstrap
controller не получает через это права на product mutation. Новая задача и resume
различаются по [initial-state contract](../docs/03_Development.md#initial-product-state),
конфликт владельцев — по [recovery protocol](../docs/03_Development.md#state-conflict-recovery).

Незакрытые вопросы не дублируются здесь: [реестр SC-DEC](../docs/00_Core.md#scaffold-core-decisions)
задаёт рекомендацию, альтернативу, нужный ответ и срок. SC-DEC-01 требует принятия
exact scope/V3, SC-DEC-02 — target/profile/adapter, SC-DEC-03 — host/capture/data.
Переносимость, macOS-first, смешанный exchange и наличие коннекторов/очереди в первом ядре уже выбраны. Их повторное подтверждение не требуется; точные contracts/profile остаются предметом принятия.
Пригодность имеющегося host UNKNOWN до V3 conformance; выбор имени не является
Evidence. SC-DEC-04 оформляется только перед launch. Storage, identity HOW,
организация tests и конкретные команды выбираются агентом в принятых границах.

## 4. Порядок реализации и доказательства

Условия выхода принадлежат Product, проверки — Development. Ниже только связывается их порядок:

| Часть | Основная работа | Требуемая проверка перед продолжением |
|---|---|---|
| До S0 | Fresh target/authority/environment/host binding и достаточные product inputs | Host admission/capture/probe и supported resume доказаны; SC-T01/04/09/10/15…18/21/22 в применимой host boundary. Не запускать отсутствующие команды AOS |
| S0 | Воспроизводимая основа проекта, local dev/check entrypoints и внешний checkpoint | SC-T01/02; объявлены C-015/C-016/profile подготовки, deps и scope preservation; sufficient handoff K1 |
| K1 | Достаточные source-bound Intent/Spec/Passport/Brief inputs без повторного выбора неизменной цели | SC-T03; invalid inputs не создают approval |
| K2 | Минимальные state/authority/validation/recovery guarantees и один допустимый effect | SC-T04/05/17 и случаи admission/report SC-T21/22, registration/durable enqueue/admission SC-T23/24; первый product checkpoint, exact subject, one-time effect и negative denial |
| K3 | Полный correction/completion loop, ledger, interruption и resource resume | SC-T06…10/15/16 и случаи correction/pause SC-T22, recovery/limits SC-T25/26; diagnostic checks имеют purpose, weak evidence не запускает correction; новая сессия сохраняет историю |
| K4 | Current status/review/handoff и интегрированный результат ядра | SC-T11…26 и все ранее required checks на final candidate; части сами по себе не доказывают parent completion |

До первого queued product effect K2 доступны registration, queue storage,
current admission, operation ledger и recovery. Создание registry/queue —
отдельно покрытая служебная операция, без собственной queue как prerequisite.
Внешний host не обязан заранее реализовать product transport: SC-T23…26
проверяют создаваемое ядро по мере готовности, не блокируют S0 отсутствием AOS.

Runtime dependencies реализуются до первого использования независимо от названия среза. Внешний development loop работает с S0 и может остаться ведущим до конца интервала. Разработка не должна зависеть от наличия собственных незаконченных controller, guard или validator.

В положительном автономном product journey actual C-005 сохраняет ссылку на заранее принятый exact Product/Feature Contract. Производные DRAFT-артефакты K1 не наследуют acceptance и не заменяют этот input. Если требуется принять новое product meaning/revision, действует Human Gate; тесты генерации draft проверяются отдельно от реальной authority исполнения.

Передача текущей development task product controller в предлагаемом минимальном scope необязательна. Если она включена отдельным точным решением, проверяются сохранение task/authority/criteria/ledger/resources, compatibility, reconciliation и один active continuation owner. Без доказанной передачи продолжает внешний host; task history не обнуляется.

## 5. Проверки и Evidence

Единая acceptance matrix находится в [Development SC-T01…26](../docs/03_Development.md#scaffold-core-checks); здесь не хранится её независимая копия. Реализация создаёт executable fixtures и command bindings для каждого required случая. До исполнения конкретного check известны inputs, независимый oracle, expected outcome, subject/environment, Evidence destination и ограничения.

Профиль проверок включает PREPARE, START, CHECK-SCAFFOLD, CHECK-CORE, CHECK-HOST и FINAL-CHECK по контракту Development §24.4. Это логические имена будущих операций, а не существующие CLI-команды. Implementation agent самостоятельно выбирает reversible harness/flags, документирует фактический запуск и не требует ещё не созданный продукт как условие запуска harness.

Каждый критерий связан с check IDs и current candidate-bound Evidence. После relevant mutation его результат stale до affected verification. При неизвестном impact требуется broader check либо UNKNOWN. Required missing/unsupported check не исключается из списка для получения PASS. Synthetic, installed и real-host результаты различаются; real selected adapter и самостоятельный resume не закрываются fake fixtures.

Минимальный реальный product example SC-T14: по достаточной заранее заданной задаче создать один файл с заданными bytes в разрешённом disposable target, проверить его внешним oracle и выдать review/handoff. Отдельные варианты вводят controlled defect и interruption. R7 добавляет direct status/read и queued file-effect через C-015/C-016 с duplicate/lost-ack/recovery variants; accepted/ack не являются выполнением или PASS. Synthetic human decision используется только как test input; действительная runtime authority для effects выдаётся отдельно. Успешный пример проверяет работу ядра, но не доказывает, что весь проект был разработан автономно: для этого необходима история внешнего development run S0–K4.

## 6. Продолжение, correction и завершение

Текущая lifecycle находится в C-012; C-005 сохраняет исходную stage и scope.
Человек выбрал явные переходы: execute/correct в EXECUTE, checks в VALIDATE,
после predicate — REVIEW без Human ACCEPT. Допуск атомарно связывает смену stage,
controller action и consumption; pause/resume сохраняют stage. Standalone
read-only task не получает correction authority. Полные условия —
[Development](../docs/03_Development.md#core-lifecycle-transitions).

External host/product controller следует canonical next-action priority: reconciliation → authority/identity → recovery → failing check diagnostics → material unknown → dependency-ready criterion → affected checks → final validation. Source of truth и authority не возникают из worker report.

После ordinary defect применяется D0…D5: DIAGNOSTIC CHECK возвращается в
DIAGNOSE без закрытия acceptance criteria. Finding, разрешённый без mutation,
ведёт в SELECT_NEXT_ACTION с сохранением required checks. Если correction нужна,
применяются fresh Correction Gate, отдельный worker, новый action binding/candidate
и повторная проверка. Validator не исправляет subject. Эквивалентные patches или unchanged checks без новой информации не являются progress; ledger сохраняется между workers и runs. Material product/architecture/security change возвращает точный decision request, а не speculative implementation.

Checkpoint сохраняет task/revision, candidate, критерии/results/evidence, effects, diagnostics/attempts/resources, current authority binding и next action. После supported host stop внешний trigger запускает восстановление без новой постановки задачи. Manual resume доказывает recoverability, но не полную автономность. Missing/partial C-008 не запрещает scoped reconciliation по admission/ledger и независимым target observations; её C-010 не подменяет отчёт worker. Unknown effect сначала reconciled; expired/revoked authority не переиспользуется.

Техническое завершение определяется [Development §10.5](../docs/03_Development.md): каждый criterion доказан, required checks current PASS, scope соблюдён, material unknowns и required findings закрыты законным способом, effects reconciled, state recoverable. Финальный результат содержит before/after, Evidence, limitations, NOT_RUN, remaining Human decisions и один допустимый следующий шаг. Human acceptance и Git delivery не имитируются.

## 7. Следующие фичи

Каждый выбранный поздний модуль получает одну parent task для автономной сборки целиком: contracts всех входящих фич → внутренние/внешние стыки → достаточный общий brief/authority → самостоятельная декомпозиция, реализация, интеграция/check/correction и supported resume → единый технический review. Внутренние фичи не требуют отдельных ручных запусков или промежуточного Human ACCEPT. Обязательный алгоритм формирования, semantic readiness и lifecycle подключения/удаления — [Development §25.4/25.5](../docs/03_Development.md#feature-module-protocol). Полный маршрут и MOD-A01…07 — [Development](../docs/03_Development.md#autonomous-module-development). [Правило готовности и интеграции](../docs/03_Development.md#feature-integration-readiness) требует public input/output/version guarantees, data/state owner, declared effects, отказ/отключение/recovery, проверку фактических стыков и сохранности базового core journey. Полные dossiers всех optional-модулей сейчас не являются prerequisites.

## 8. Пакет решений и фактическая готовность

Человеку передаётся один пакет: этот brief и перечисленные current owner sections. Предлагается принять scope/route SC-DEC-01, определить применимый target/environment SC-DEC-02 и host/capture/data profile SC-DEC-03. Точные вопросы, рекомендуемые варианты и последствия находятся у [Core](../docs/00_Core.md#scaffold-core-decisions); прежние действующие X1 решения повторно не запрашиваются. Отдельный launch SC-DEC-04 возможен после принятия exact subject и fresh preflight, не выполняется ответом о документационном PASS.

Готовность этого документа к рассмотрению не означает готовность к runtime launch. До закрытия названных входов и host conformance зависимая implementation readiness остаётся BLOCKED. Runtime, native adapter, автономный S0–K4 run и Git delivery — NOT_RUN.


## 9. Поздние модули: уточнение R4

Человек выбрал группировку [FTR-005+022](../docs/06_Features.md#architecture-patterns-module)
в модуль «Архитектурные решения и patterns». Он остаётся вне обязательного ядра;
полный contract не принят автоматически, отдельные FTR/dispositions сохранены.
Остальные группировки не выбраны. Внешние стыки принадлежат
[Architecture](../docs/02_Architecture.md#architecture-patterns-interfaces).

Исправлены C-011 → FTR-025, Query/Build/Refresh FTR-017, Check/Migration/Sunset
FTR-030, local Commit FTR-015 и handoff FTR-024 → FTR-015 → C-014. Это не добавляет
поздние capabilities в S0–K4, не запускает plugin framework и не меняет V2.
[Development](../docs/03_Development.md#module-consistency-checks) содержит
MOD-S16…23 для будущей проверки выбранных модулей. Семь shared-default dossiers
не объявлены implementation-ready; FTR-024 уточнён только в части handoff.


## 10. Исправления повторного аудита — R5

R4 выше описывает историческую модульную правку; текущий core-профиль —
[V3](../docs/02_Architecture.md#core-loop-v3). R5 согласует technical vocabulary,
явные lifecycle-переходы, recovery без C-008 и отдельные parent/envelope bindings
в [stage report](../docs/03_Development.md#12-отчёт-стадии).
[SC-T21/22](../docs/03_Development.md#core-r5-checks) и расширенные SC-T09/16
добавлены к прежним проверкам. Новых core-фич/optional dependencies нет.

R5 остаётся SCAFFOLD_CORE_DRAFT: принятие contracts SC-DEC-01, точные target/profile
SC-DEC-02 и host/data SC-DEC-03 не подменены документационной правкой. SC-DEC-04,
real-host/native execution, самостоятельная разработка S0–K4 и Git — NOT_RUN.


## 11. Автономность каждого модуля — R6

Человек потребовал автономную сборку каждого выбранного модуля, включая его
внутренние фичи и стыки. Общая достаточность входа и MOD-A01…05 теперь определены
у Development; Product владеет outcome, Features — составом модуля. Это применение
существующего V3 к очередной принятой full-cycle task, без изменения C-схем и
матрицы. Подготовка всех поздних фич одновременно, новый host или runtime здесь
не выполняются. Неожиданный material gap сохраняет точный gate/незавершённый run;
обычные внутренние шаги выполняются агентом по исходному scope.


## 12. Формирование, коннекторы и очереди — R7

Текущий профиль дополняет V3 контрактами [C-015/C-016](../docs/02_Architecture.md#module-connector-queue)
и [SC-T23…26](../docs/03_Development.md#core-transport-checks). Человек выбрал
смешанный exchange и минимальный transport уже в первом ядре. Состав 13 core FTR
сохранён, их обязанности расширены; FTR-007 backlog, полный installer и dynamic
plugin framework не обязательны. Внешний broker/storage engine не выбран.

Каждая новая или изменяемая фича/модуль проходит [обязательный протокол](../docs/03_Development.md#feature-module-protocol)
до dependent implementation; add/enable/update/disable/remove implementation/delete
data различены. [005+022](../docs/06_Features.md#architecture-patterns-module) —
первый документальный пример с отдельными read/analysis/save/event boundaries.
MOD-A06/07 проверяют semantic readiness и весь автономный module build.

Исторические R4–R6 выше относятся к своим revisions. Runtime реализация и
подключение всех модулей этим brief не выполняются. SC-DEC-01…04 остаются
фактически незакрытыми; точные accepted contracts, target/profile/limits,
реальные integrations и host evidence нужны до соответствующего запуска.

Исправления перед коммитом R7 согласуют recovery checkpoint и FTR-006.N01:
доказанный промежуточный ACTIVE/RUNNING/IDLE поддерживает interruption/resume,
произвольный idle остаётся запрещённым (SC-T16). C-016 отдельно доставляет
read-only EVENT в status/review по действующей подписке без фиктивной task или
ValidationEnvelope; effectful follow-up проходит COMMAND/current authority
(SC-T24). Это уточнения текущего DRAFT, не новые controller edges или runtime
Evidence. Результат scoped исправления пяти находок записан в [плане §13](AOS_SCAFFOLD_CORE_AUTONOMOUS_DEVELOPMENT_PLAN.md#13-исправления-перед-коммитом-r7).

<a id="quality-requirements-review"></a>

## 13. FTR-003: условия качества и проверка совместимости — 2026-09-15

**Предмет и покрытие.** Авторская документационная правка и проверка по Development §25.4–25.7: производное представление существенных условий качества внутри существующей FTR-003; стыки с FTR-005/006 и существующим C-009/FTR-011. Это дополнение маршрута K1, не новый модуль, пересборка scaffold или проверка полного ядра. Владелец смысла — [Product](../docs/01_Product.md#quality-requirements-purpose), поведения — [FTR-003](../docs/06_Features.md#quality-requirements-behavior), данных/совместимости — [Architecture](../docs/02_Architecture.md#quality-requirements-contract), scenarios/pilot — [Development](../docs/03_Development.md#quality-requirements-verification), происхождения — [Reference](../docs/05_Reference.md#quality-requirements-source). Проверена локальная редакция notebook; AOS-3 runtime и фактические adapters не обследовались. Это self-check автора, independent review NOT_RUN.

Постановка для исполнителя: получить source-bound intent/требования и scope фичи; сохранить существенные условия у прежних owners; дать производные ссылки/пояснения и передать проверяемые implications в C-005. Верный результат сохраняет смысл/область/статус, не теряет inherited constraint и не выдаёт предложение за решение. Layout/внутреннее представление выбирает агент; отсутствующее product condition или отклонение требует только применимого недостающего решения. Реальный запуск остаётся отдельным действием.

**К1–К10 — оценка содержания после правки.** Все статусы ниже относятся только к этому документальному scope, не к runtime validation.

| Критерий | Итог | Основание и предел |
|---|---|---|
| К1, назначение | PASS | Product quality-purpose и FTR-003 quality-behavior: ограниченное представление, без новой фичи/schema/gate; исходный сбор условий уже существует |
| К2, входы | PASS | FTR-003 шаги 1–3; QR-C01–03/06: sources/revisions, material gaps, пустые/неполные входы и сохранение прежних ответов |
| К3, поведение | PASS | FTR-003 шаги 1–6: нормализация → applicable refs/additions/deviations → need/no-need → проект проверки; DRAFT/принятое/unknown различены |
| К4, ownership/стыки | PASS | Architecture quality-contract: один owner, C-003/C-002 → FTR-006/C-005 → действующий C-009; producer/consumer и fallback без нового wire format |
| К5, recovery | PASS | FTR-003 recovery и QR-C10/12: rebind после изменения, сохранение history, несохранённое не durable, повтор effect не выдуман |
| К6, критерии | PASS | QR-C01–12: есть positive наследование, разрешённое scoped exception, source-bound измеримое условие и отрицательные случаи. Это заданные oracles, исполнение NOT_RUN |
| К7, смысл | PASS | QR-C03/06–08: исходные слова, отсутствие false precision, различение solution и явного constraint; oracle не выводится из compiler output |
| К8, самостоятельность | PASS | FTR-003 open inputs + Architecture WHAT/HOW + этот brief: scope/выход/checks достаточны для документационной работы; обычное оформление не вызывает новое интервью |
| К9, интеграция | PASS | Новый состав модуля N/A: меняется существующая фича. Реальные стыки не исключены — QR-C08/10–12 обнаруживают потерю условия, old consumer и disable; runtime стык NOT_RUN |
| К10, согласованность | PASS | Product/Features/Architecture/Development/Reference согласованы; старые статусы R2 и C-009 исправлены в адаптации. Frozen ТЗ интервью не переписано |

**Замечания исходного кандидата и исправления.** Закрыты в разрешённой правке, не являются обещанием runtime conformance:

| Finding | Исходный пробел и последствие | Исправление / проверка |
|---|---|---|
| QR-F01 | R2 §2 считает 003/005/011 UNDECIDED; это могло вызвать повторный selection | Current dispositions сохранены, источник ограничен в Reference; новые Human Gates не введены |
| QR-F02 | R2 §5 оставляет два варианта owner; два независимых порога сделали бы Brief неоднозначным | Производное представление existing constraints/metrics/acceptance без migration; Architecture + QR-C04 |
| QR-F03 | R2 §§6/8 не закрывает empty refs и source-only deviation; возможна потеря/ослабление requirement | Scope-based applicability, exact human binding исключения; FTR-003 + QR-C01/05/10 |
| QR-F04 | R2 §11 не связывает конкретные условия измерения/множество checks с нынешним C-009 | FTR-006 owner compilation, separate check IDs, method/context refs и current V3; Architecture + QR-C08/09/12 |

**Восемь репетиций без исполнения.** Сопоставлены ожидаемый исход и разрешённый следующий шаг; расхождений с изменённым текстом не найдено. Речь о чтении контрактов, не о проверенном поведении программы.

| Ситуация | Результат репетиции и следующий шаг |
|---|---|
| Достаточный вход | QR-C08: source/revision/условия доходят до проекта C-005; можно подготовить проверку без вопроса о layout |
| Неполный вход | QR-C02/03: unknown вместо threshold; уточнить только существенное условие, продолжать независимое |
| Противоречие | QR-C04/05: действующее требование сохраняется, proposal не override; показать owner точный конфликт |
| Недоступная зависимость | QR-C11: подготовить документы по доступным sources; не утверждать запуск FTR-005/011. Runtime следующего шага требует фактического adapter |
| Обычный дефект | QR-C03/08: найти потерю смысла/условия, исправить у разрешённого owner и повторить затронутую проверку; новое product decision нужно только при изменении требуемого поведения |
| Прерывание/повтор | QR-C12: сверить подтверждённую revision и фактический исход сохранения; не предъявлять неподтверждённое как durable и не повторять неизвестный effect |
| Сломанный стык | QR-C12: локальный PASS частей не закрывает потерянный requirement ref; исправить передачу в покрытом scope и перепроверить общий путь |
| Завершение | Для текущей работы достаточно согласованных owner docs и проверок; runtime completion требует actual public journey/current Evidence. Таблица не закрывает будущую task |

**Опровержения.** «Две реализации»: compiler, который игнорирует product constraints при пустом quality-разделе, и compiler, сохраняющий применимые ограничения, дают разные результаты. Первую запрещают Architecture applicability и QR-C01; разные Markdown layouts при одинаковом смысле допустимы. «Плохая реализация проходит»: формально заполненный check на пустой базе вместо заданной нагрузки исключён QR-C08; всегда UNKNOWN/отказ не проходит positive inherited/deviation/compilation cases. Синтетический oracle не доказывает работающий runtime.

**Решения и предпосылки.** Для завершения этой документационной правки новых product decisions не требуется. Для реального pilot человек/владелец выбирает одну фичу, цель и допустимые расходы; агент находит источники, готовит method/fixtures и объясняет отсутствующие условия. Для runtime нужны exact implementation target, пригодные environment/adapter, read/output/effects scope, current authorization и resume boundary; они в этой работе не назначались. Это ограничения запуска, а не причина переписать достаточное описание. Permanent schema/словарь/автоматизация отложены, не являются blockers текущего scope.

**Итог:** описание достаточно для указанного документационного применения и подготовки ограниченного эксперимента; исполнимость реального validation пути не проверена. Runtime/pilot/измерение пользы/independent review — NOT_RUN. Существующие requirement owners, feature dispositions и authority сохранены; весь scaffold/core и соседние модули повторно не аудированы.
