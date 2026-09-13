---
package: AOS_Project_Knowledge_Baseline
package_revision: R7-RU
updated: '2026-09-13'
status: HUMAN_ACCEPTED_KNOWLEDGE_BASELINE
authority: FACT_CLASS_SCOPED
human_review: COMPLETED_FOR_ACCEPTED_CONTENT
human_acceptance: ACCEPTED
current_change_subject: AOS_MODULE_PROTOCOL_CONNECTORS_QUEUES_R7
current_change_authority: CURRENT_EXPLICIT_HUMAN_INSTRUCTION
current_change_status: SCAFFOLD_CORE_DRAFT
current_change_agent_review: PASS
current_change_agent_review_scope: DOCUMENTATION_AUTHOR_SELF_CHECK
current_change_human_review: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
semantic_audit: COMPLETED_WITH_CORRECTIONS
independent_semantic_validation: NOT_RUN
source_repository: NMF13579/notebook
source_branch: dev
audited_source_commit: c7b3f166d6eaeae78348f9291a4cc28ab18dc92c
audited_source_blob_sha: c7eaa210dcb92733dbee7a31668878b135b1887f
active_path: docs/01_Product.md
document_language: ru
technical_identifiers_language: en
document_role: CANONICAL_PRODUCT_BASELINE
authority_scope:
- target_users
- user_problems
- product_boundaries
- accepted_product_directions
- product_non_goals
---

# 01 — Продукт

## 1. Граница статуса

Документ является принятым product baseline. Подтверждённые product facts имеют fact-class-scoped authority; разделы, помеченные `PROPOSAL`, `OPTIONAL` или `UNDECIDED`, не становятся принятыми решениями. Ни один раздел не разрешает implementation.

## 2. Проблема продукта

Непрограммист может описать желаемый результат, но не способен надёжно контролировать каждую repository operation, permission, test и implementation detail. AI-агенты могут потерять product intent, расширить scope, завысить completion или создать maintenance debt.

| ID | Проблема | Последствие |
|---|---|---|
| `P-001` | State распределён между chats, worktrees, reports и decisions | Потеря context и повторный planning |
| `P-002` | Неясно, где остановились | Unsafe assumptions on resume |
| `P-003` | Free-form request превращается в implementation assumptions | Wrong feature/problem fit |
| `P-004` | Scope расширяется скрыто | Contamination и difficult rollback |
| `P-005` | PASS/Evidence/readiness смешиваются с approval | False completion |
| `P-006` | Implementation и validation смешиваются | Self-validation и hidden fixes |
| `P-007` | Git operations считаются одним действием | Unauthorized publication |
| `P-008` | Legacy содержит ценность и obsolete complexity | Wrong target architecture |
| `P-009` | Exhaustive extraction имеет low ROI | Product work delayed |
| `P-010` | Documentation дублирует fact owners | Drift и unclear SoT |
| `P-011` | Feature descriptions shallow | Agent invents behavior/tests |
| `P-012` | Install/update ownership unclear | User data loss |
| `P-013` | Model/agent routing lacks measurements | Cost/quality unpredictability |
| `P-014` | Automation precedes manual flow | Bad process automated |
| `P-015` | Blockers/next action не понятны | Dependence on specialists |

## 3. Обещание продукта

```text
пользователь формулирует проблему или идею
→ AOS делает понимание и uncertainty видимыми
→ создаёт bounded, reviewable development cycle
→ показывает Evidence и remaining risk
→ человек принимает решение
→ работа безопасно возобновляется
```

## 4. Пользователи и JTBD

### Непрограммист / domain expert

- объяснить problem обычным языком;
- увидеть understood/missing/assumed;
- утвердить product intent и high-risk actions;
- оценить user-visible result без чтения всего кода;
- resume after interruption.

### Vibe-coder / product builder

- получить safe default workflow;
- предотвращать scope drift и false completion;
- менять coding agents без переписывания rules;
- сохранять maintainable project knowledge.

### Agent / implementer / reviewer

- получить bounded context и one task;
- знать allowed/forbidden changes;
- связать acceptance criteria с Evidence;
- сообщить uncertainty/remaining risk;
- оставить recoverable handoff.

### Maintainer / operator

- inspect current state/drift;
- понимать ownership/rationale;
- reproduce checks;
- отличать historical report от current result.

## 5. Адаптивный intake

### Готовая полная спецификация

AOS сохраняет original input, проверяет missing fields и contradictions, показывает added assumptions, задаёт только material questions, создаёт DRAFT Product Spec/Feature Passport и останавливается до architecture/execution authority.

### Неполная идея

Problem Interview определяет user/pain/current workaround, отделяет outcome от solution, фиксирует success signals, constraints, non-goals, unknowns, follow-up questions и sensitive/provider concerns.

### Прогрессивная глубина

| Profile | Minimum depth |
|---|---|
| Small reversible | Goal, scope, observable result, focused check |
| Medium feature | Users, flow, acceptance, dependencies, regression |
| High/protected | Full constraints, rollback, authority checkpoints |
| Sensitive/regulated | Data/provider boundary, specialist review |

Точные thresholds остаются `UNDECIDED`.

## 6. Артефакты продукта

### Intent Record

Original request, actor, problem, desired outcome, constraints, non-goals, assumptions, unknowns, source и sensitive flags.

### Product Spec

Problem, users/JTBD, goals/non-goals, journeys, product boundaries, constraints, risks, metrics, dependencies, acceptance и open decisions. Product Spec не разрешает execution.

### Feature Passport

Identity/owner, problem/user, observable behavior, trigger/preconditions, inputs/outputs, flow/states, failures/recovery, dependencies, constraints, authority boundaries, acceptance/negative scenarios, maturity, evidence status и human disposition.

### Product Feature Registry — architecture candidate

Registry индексирует Feature Passports, но не заменяет их и не смешивается с execution/verification/protected registries.

## 7. Pipeline сценариев, доступа и UX — optional

```text
Problem Interview
→ Problem Map
→ Scenario Interview
→ approved scenarios
→ access model
→ UX object inventory
→ grouping
→ screen map
→ human review
```

Запускается только когда Product Spec недостаточно описывает actors, access-sensitive behavior и UX flow.

## 8. Границы продукта

### Product Runtime

Intent/Problem Intake, Discovery, Product Spec/Feature Passport, Status/Next/Details, Review Package, Project Memory/Handoff, First-Start/Tutor и optional Architecture Support/Guided Bootstrap.

### Development Factory

Task Brief compiler, preflight/preview, persistent complete-task controller, execution adapters, validators/test harness, multi-stage diagnostics, Context Packs, backlog/decomposition, CI/release helpers, strict loaders/drift checks. Controller продолжает bounded task через отдельные stage workers до доказанного результата, но не расширяет authority и не выполняет protected/Git actions автоматически.

### Governance

Minimal Safety Floor всегда; stronger controls только после observed need. Governance не является product value сама по себе.

### Knowledge / Reference

Accepted documents, DRAFT Feature Passports, lessons/patterns, targeted findings и rebuildable indexes.

<a id="repository-graph-purpose"></a>

### Проектный граф репозитория — PROPOSAL

Предлагается локальная производная карта фактического устройства выбранного repository/worktree, привязанная к наблюдавшимся исходникам. Она помогает агенту до изменения обнаружить существенную связь, найти первичные источники и определить область проверки. Пользователь получает обзор исследованных областей и пробелов; reviewer — объяснение изменения связей. Снижение объёма выдачи само по себе не доказывает пользу.

Первая область применения — разработка самого AOS, в границе Development Factory и Knowledge. Это не первый Product Runtime slice и не автоматический выбор возможности для любых чужих проектов. В scope входят source, tests, конфигурация, релевантные документы и подтверждённые связи с существующими feature/contract records одного локального worktree. Pilot ограничивается одним языком, окружением и несколькими поддержанными способами обнаружения связей.

Граф не владеет требованиями, архитектурными решениями, Project Memory, разрешениями или статусами принятия. Его сбой не блокирует безопасное прямое исследование и работу без карты; graph artifact не становится runtime dependency продукта. Роли пользователя, агента, картографа и reviewer не требуют отдельных агентов.

В первую версию не входят Graph/vector DB, RAG, сервер/MCP, watcher/daemon, Git hooks, облачная синхронизация, marketplace, универсальный parser всех языков, runtime instrumentation, автоматическое исправление проекта и сравнение AS-IS с TARGET. Lifecycle и Git delivery сохраняют существующие границы.

Это перенесённое предложение ТЗ R2, не принятое решение о пересборке, выборе FTR или миграции AOS-3. [Архитектурный контракт](02_Architecture.md#repository-graph-contract), [pilot и рабочий цикл](03_Development.md#repository-graph-pilot), [provenance](05_Reference.md#repository-graph-tz). Смежные FTR-002, FTR-016, FTR-017 и FTR-021 остаются тематическими маршрутами с собственными dispositions.

## 9. Основные пользовательские journeys

### J-001 — Запуск нового проекта

```text
intent → clarification → problem/outcome → Product Spec → slice choice
→ architecture decision if needed → Task Brief → authorization
→ implementation → validation → review → human decision
```

### J-002 — Исследование существующего проекта

```text
repository → read-only identity/preflight → capability map
→ gaps/conflicts/unknowns → candidate objectives → human selection
```

### J-003 — Реализация одной feature

```text
Feature Passport → targeted research → Product Contract → architecture
→ Task Brief → parent task authority → controller
→ EXECUTE → CHECK → при failure многоступенчатая DIAGNOSE → CORRECT
→ FINAL_VALIDATE → REVIEW → decision
```

### J-004 — Возобновление работы

```text
/status → persistent task/run state → repository-derived rebind
→ exact candidate/authority/attempt ledger → blockers/decisions
→ deterministic /next → optional /details
```

### J-005 — Проверка и решение

```text
before/after → scope → Evidence → NOT_RUN/limitations → findings
→ ACCEPT | NEEDS_CHANGES | REJECT | DEFER
```

### J-006 — Защищённая доставка

```text
protected scope → plan → human Risk Profile → authorized EXECUTE
→ independent VALIDATE → REVIEW → separate Commit/Push/Merge/Release
```

### J-007 — Reconstruction по reference

```text
feature gap → narrow question → pinned snapshot → inspect evidence
→ classify → reject legacy complexity → update dossier → human decision
```

## 10. MVP-кандидат — PROPOSAL

Safe entry/discovery, adaptive intake, Product Spec/Feature Passport, one Task Brief, separate Execution Authorization, scope/risk/human authority, one change, Evidence mapped to acceptance, human acceptance, compact handoff и lesson proposal.

## 11. Критерии первого vertical slice

Slice решает identified user problem, даёт observable result, имеет described I/O/states/failures/recovery, executable acceptance/negative cases, работает без full Control Plane, имеет minimal dependencies, создаёт learning и не включает implicit Git delivery.

## 12. Модель product acceptance

Feature documentation-ready, когда определены users, trigger, I/O, observable result, states, failures/recovery, non-goals, acceptance, negative cases, human decisions и research gaps.

Product acceptance требует explicit human decision по exact revision.

## 13. Кандидатные показатели успеха — PROPOSAL

Time intent→Task Brief, clarification loops, scope drift, resume time, review time, false-green incidents, tasks without re-planning, lesson reuse, user understanding, Governance overhead и maintainability.

## 14. Необходимые product decisions

Для X1 зафиксированы Product Spec↔Feature Passport ownership и first FTR-001 slice; [применимость этих решений](00_Core.md#scaffold-core-decisions) ограничена исходным scope. Для более широкого продукта остаются segment/job, Feature Registry, scenario/access/UX timing, interface, acceptance identity, install ownership, feature dispositions и metrics.

## 15. Жизненный цикл внедрения (Project Roadmap)

Прежняя общая последовательность покрывает Runtime Pipeline. Она не является одновременно вторым заданием на новый scaffold/core; для этой задачи подготовлено уточнение [S0–K4](#scaffold-core-outcome), ожидающее SC-DEC-01:

- **Foundation:** Базовый репозиторий, CLI skeleton и Logger.
- **Slice 1 (Intake & Definition):** Приём намерения и формализация контрактов (Intent Contract).
- **Slice 2 (Bounded Execution):** Безопасное выполнение задачи в изолированной среде без скрытого изменения глобального состояния.
- **Slice 3 (Verification & Evidence):** Сбор независимых и неизменяемых доказательств работоспособности.
- **Slice 4 (Decision & Integration):** Механизм явного Human Decision и перенос изменений в глобальное состояние после аппрува.


<a id="modular-core"></a>

## 16. Модульное ядро — DRAFT состава

Пользователь подтвердил направление: полные описания выбранных фич при небольшом обязательном ядре. Этот раздел формирует продуктовый contract предложения; утверждение точного состава остаётся отдельным решением MOD-DEC-01. Единственный индекс возможностей и их placements находится в [06_Features](06_Features.md#4-индекс-каталога).

Основной пользователь — владелец проекта, ставящий ограниченную задачу агенту. Основной результат: понятный проверенный итог одной разрешённой задачи с доказательствами, решением человека и возможностью продолжения. Система должна обеспечивать цепь:

намерение → уточнённые требования и контекст → одна задача и отдельные полномочия → выполнение → проверка → при дефекте расширяемая диагностика/исправление → итоговая проверка → review и человеческое решение → сохранённое состояние.

Для нового проекта discovery фиксирует отсутствие существующего repository и запрашивает лишь необходимые сведения; для существующего исследует разрешённую область. Архитектурная необходимость выявляется до исполнения: если без решения задачу нельзя выполнить, модуль FTR-005 либо явное внешнее человеческое решение требуется для этого сценария. Git-доставка FTR-015 следует после результата только при отдельном запросе; её отсутствие не отменяет техническое завершение.

Полные модули сохраняют задачи установки/обновления/удаления, backlog, архитектурного выбора, Git-доставки, audits, patterns, CI и incidents. Отсутствие модуля допускается лишь для сценария, который не требует его результата. Невозможность выполнить required check никогда не заменяется PASS; модуль не получает право менять scope, authority или state другого владельца.

В scope первой документационной версии входит описание конечного поведения выбранных возможностей и требования переносимости; реализация и одновременное подтверждение поддержки всех ОС сюда не входят. Полнота ТЗ не означает одновременный запуск всех модулей. FTR-017/FTR-030 предлагаются как поддерживающие модули: их контракт описывается полностью, но индекс активируется после измеренной поисковой потребности, strict tools — для определённых стабильных contracts. Локальная базовая проверка валидности данных не зависит от установки отдельного модуля tools.

<a id="autonomous-module-outcome"></a>

### Автономная сборка каждого выбранного модуля

Требование человека: единицей автономной разработки является весь выбранный
модуль. Для модуля из одной фичи границы совпадают; для составного модуля
внутренние FTR сохраняют contracts и критерии, но не требуют отдельных ручных
запусков, разрешений на каждый обычный шаг или промежуточного Human ACCEPT.

До запуска согласованы результат модуля, входящие FTR и exact contracts,
внешние интерфейсы/версии, target/environment, dependencies, данные/providers,
полномочия, лимиты и проверяемые критерии. Агент затем самостоятельно выполняет
декомпозицию, сборку фич, внутреннюю интеграцию, проверки, диагностику/correction,
сохранение состояния и supported resume до единого технического результата.
Declared интеграции с ядром и уже доступными модулями входят в тот же scope.
Успешные отдельные фичи при неработающем модуле не означают completion.

Человек получает один итоговый review package. Пользовательский dogfood,
принятие результата и protected/Git delivery остаются отдельно от технической
сборки. Human gates, являющиеся поведением самого продукта, реализуются и
проверяются с явно синтетическими fixtures; такие fixtures не выдаются за
реальные человеческие решения или полномочия разработки.

Если обязательное решение, доступ или внешняя зависимость отсутствует до старта,
модуль не готов к автономному запуску. Неожиданный material conflict либо выход
за authority даёт точную остановку; это незавершённый автономный run, а не PASS.
Обычный дефект и выбор обратимого HOW в согласованных границах решает агент.
Правило относится ко всем модулям по мере их выбора; полная подготовка всех
поздних dossiers одновременно не требуется. [Development](03_Development.md#autonomous-module-development)
задаёт достаточность входа и доказательства результата.

<a id="core-connector-outcome"></a>

### Подключение к ядру: коннекторы и очереди — R7

Человек выбрал смешанную модель обмена и наличие минимальных локальных
коннекторов/очереди уже в первом ядре. Ядро предоставляет объявленные точки
подключения: быстрый read-only запрос возвращает результат напрямую, команда
с эффектом или отложенная работа доставляется через сохраняемую очередь,
событие сообщает наблюдение объявленным consumers. Вызов внутренних классов
или storage другого модуля не заменяет публичный интерфейс.

Пользователь видит отдельно приём запроса, ожидание/доставку, фактическое выполнение,
результат и причину остановки. Повтор доставки не должен повторять завершённый
логический эффект. Отказ optional-модуля не выключает независимые возможности
ядра; required недоступная capability сохраняет незавершённый критерий.

Модуль подключается после проверки contracts/capabilities и интеграционных
сценариев. При отключении новая работа больше не принимается, ожидающая явно
приостанавливается, выполняющаяся reconciled. Удаление реализации не означает
удаление данных; зависимые consumers и сохранённые сообщения учитываются до
удаления. Обновление, удаление данных и migration имеют отдельный объявленный scope.

Это расширение базовых обязанностей core, а не новый backlog FTR-007 или
обязательный внешний broker, daemon/service либо dynamic plugin loader.
Локальная композиция допустима. [C-015/C-016](02_Architecture.md#module-connector-queue)
задают contracts; [протокол агента](03_Development.md#feature-module-protocol)
определяет подготовку, подключение и проверку каждого выбранного модуля.

<a id="modular-decisions"></a>

### Решения для принятия точного состава

| ID | Вопрос и рекомендуемая граница | Альтернатива и последствие | Статус |
|---|---|---|---|
| MOD-DEC-01 | Принять placements в индексе: 13 core-семейств, 7 сценарных модулей для 8 семейств (FTR-005+022 объединены), 2 support-модуля; остальные 7 семейств не расширять. Принять классификацию зависимостей вместо обязательного запуска всех связанных фич | Оставить только исходный X1: потребуется сузить заявленный полный цикл. Сделать все 23 обязательными: увеличится минимальная зависимость и стоимость сопровождения | WAIT_HUMAN по оставшемуся составу; группировка FTR-005+022 выбрана человеком |
| MOD-DEC-02 | Подтвердить interface/support envelope перед реализацией FTR-004/015/023: допустимые поверхности, платформы, способ поставки, Git-host/CI providers и совместимость версий | Ограничиться platform-neutral контрактом; допустимо для обзора дизайна, не даёт implementation-ready утверждения по integrations | OPEN; точный выбор не сделан |
| MOD-DEC-03 | Определить trusted capture человеческого решения и правила sensitive/provider-data, доступа и хранения для выбранного deployment context | До определения запретить неизвестные external effects и не устанавливать универсальный retention срок | OPEN; блокирует зависимые runtime claims |

Человек прямо выбрал объединение FTR-005 и FTR-022 в один модуль
«Архитектурные решения и patterns». Это решение о группировке, а не принятие
полного implementation contract. Две FTR identities, их критерии и исходные
X1 dispositions сохраняются. Остальные объединения не выбраны; модуль не входит
в обязательный S0–K4. Границы — [Features](06_Features.md#architecture-patterns-module).

Эти вопросы сгруппированы по материальному решению, а не по каждой редакции. Неопределённые параметры не заполняются догадкой. ТЗ и review могут быть готовы как DRAFT с указанными границами; статусы принятия и implementation readiness не повышаются.

<a id="scaffold-core-outcome"></a>

## 17. Scaffold и первое ядро — SCAFFOLD_CORE_DRAFT

Пользователь результата — владелец проекта, заранее задавший достаточную bounded задачу и полномочия. Наблюдаемый итог первого ядра: одна разрешённая локальная задача проходит от достаточного input через execution/check/diagnose/correct до проверенного результата, понятного review package и состояния, из которого работа воспроизводимо продолжается. Владелец не управляет каждой correction и каждым переходом между согласованными срезами.

**Scaffold разработки AOS** — подготовленная запускаемая основа implementation target и локального dev/check cycle. Она не устанавливает AOS в произвольные чужие проекты и не включает полный installer/update/uninstall FTR-004. Его базовый контракт:

- **Actor/trigger:** внешний агент получает принятую задачу S0, exact target и отдельную authority.
- **Входы:** согласованный [профиль](02_Architecture.md#scaffold-core-profile), достаточный исходный Product/Feature Contract, поддержанное окружение, path/operation boundary и проверенный внешний host.
- **Результат:** минимальная запускаемая поверхность продукта, объявленные runtime/dev dependencies, инструкции и entrypoints локальных checks, воспроизводимая идентификация candidate, durable state/evidence для разработки. Toolchain и test harness доступны без запуска ещё не реализованного AOS.
- **Порядок:** наблюдение target → подготовка только отсутствующей разрешённой основы → проверка запуска/окружения → сохранение candidate и handoff K1. Существующий target допускается только после inventory; scaffold не очищает его до «чистого» состояния.
- **Отказы:** wrong root/identity, конфликт user files, path escape, missing dependency, unavailable required check или прерванный effect дают точную причину и незавершённый критерий; automatic overwrite и слепой retry запрещены.
- **Recovery:** сохранить observations; reconcile planned/actual effects; повторить только доказанно незавершённое действие по fresh boundary. Разрушительный rollback не входит автоматически.

| Срез | Достаточный вход | Результат и критерий выхода |
|---|---|---|
| S0 — development scaffold | Решения SC-DEC-01…03, фактический launch SC-DEC-04, внешний host/preflight | В чистом поддержанном окружении воспроизводимы prepare/start/check; dependencies объявлены, source/installed claims различены, unrelated state сохранено. Handoff содержит candidate, commands/provenance, объявленные интерфейсы C-015/C-016 и профиль подготовки подключения/очереди; следующий K1 |
| K1 — достаточная задача | S0, заранее подтверждённые problem/outcome/scope и source inputs | Базовые FTR-001/002/003/006 формируют source-bound Intent/Spec/Passport/Brief. Существующие решения читаются без повторного интервью; material missing input блокирует только зависимое действие. End-to-end отрицательный пример не получает выдуманное approval |
| K2 — один разрешённый effect | K1, current parent authority, preview и permission; базовые state/validation capabilities доступны до effect | FTR-009/019/010 создают точный candidate и effect record; FTR-013/011 проверяют scope/result. Положительный effect проходит, denial не меняет target. До первого queued effect доступны регистрация коннектора, durable queue, persistence, validation и reconciliation; сообщение не заменяет fresh admission |
| K3 — correction и continuation | K2, известные критерии/checks, durable observations | При дефекте полный controller loop диагностирует, выполняет bounded correction и перепроверяет candidate. Прерывание до/после effect, run pause и fresh-session resume не теряют ledger и не повторяют effect; duplicate delivery/потерянный acknowledgement и отмена различены |
| K4 — цельный core result | K1–K3, финальный exact candidate и применимые required checks | FTR-008/012/016 дают понятный status/review/handoff. Интегрированный direct/queued journey с коннекторами подтверждает каждый критерий, сохраняет NOT_RUN/UNKNOWN и не выдаёт технический результат за Human ACCEPT или Git delivery |

S0–K4 — порядок доказательства результатов, а не запрет заранее реализовать обязательного consumer. Минимальные state/identity/authority/check гарантии должны появиться до первого effect K2; детализацию реализации выбирает агент. Все срезы могут принадлежать одной исходной task; переходы не требуют нового человеческого решения, если цель, contracts и полномочия сохраняются. Человек выбрал явные lifecycle-переходы execution → validation → при дефекте execution; их применимость и atomic admission задаёт [Development](03_Development.md#core-lifecycle-transitions). Сами S0–K4 не являются lifecycle stages.

В автономном положительном journey execution ссылается на exact Product/Feature Contract, принятый до run и переданный во входах. K1 может прочитать его напрямую или подготовить производные DRAFT-представления, сохранив исходную ссылку; смысловая похожесть нового текста не переносит human acceptance на новые bytes. Если для дальнейшего effect требуется принять именно новую product revision, это уже материальный input gap и Human Gate, а не повод автоматически подтвердить её агентом.

**Приёмка автономного интервала:** заранее достаточные inputs позволяют дойти до K4 без новых product решений; обычный дефект исправляется в scope; после поддержанного host interruption работа продолжается по сохранённому состоянию; required checks и effects согласованы с exact candidate. Проверки [SC-T01…26](03_Development.md#scaffold-core-checks) задают наблюдаемые Evidence. Usability claims «человек понял результат» остаются отдельным human observation и не заменяются агентской оценкой.

Правило manual dogfood сохраняет смысл проверки пользовательской пользы. Для этого DRAFT предлагается: сначала разрешённая техническая реализация S0–K4 и воспроизводимые positive/negative journeys, затем пользовательский dogfood для принятия/расширения продукта. Рутинная correction не требует повторного ручного dogfood; изменение этого порядка относится к SC-DEC-01. Без принятия уточнения нельзя заявлять весь интервал как уже разрешённую automation.

Будущие фичи прорабатываются по одной после выбора человеком. Они не входят в первое ядро автоматически. Полный backlog, installer, архитектурный модуль, CI/Git delivery, search/index, patterns, audit tools, UI и domains остаются вне этого интервала, кроме явно названной необходимой базовой гарантии. [Точный scope каждой core-возможности](06_Features.md#core-first-scope) принадлежит dossier; [правило расширения](03_Development.md#feature-integration-readiness) проверяет только реальные стыки.


<a id="core-os-portability"></a>

## 18. Переносимость первого ядра

Человек задал переносимость системы между ОС и выбрал macOS первой средой
проверки. Ядро и форматы сохраняемых предметных данных не должны зависеть от
конкретной ОС. Linux и Windows — целевые платформы, поддержка которых
подтверждается последующими запусками; непроверенное не объявляется поддержанным.

Первое ядро должно пройти проверки на выбранном профиле macOS. Версия ОС,
архитектура машины, runtime и ограничения adapter фиксируются до launch;
одна проверенная конфигурация не доказывает все версии macOS. Разработка сначала
на macOS не допускает macOS-only зависимости в ядре. Переносимость обязательна
с S0, но создание всех платформенных adapters в первой реализации не требуется.

ОС-специфические возможности доступны через объявленные adapters/capabilities.
Нет обязательной зависимости ядра от macOS-приложений, Unix shell или конкретного
терминала. Отсутствие capability блокирует зависимый сценарий; независимые
возможности сохраняются. Альтернатива допустима только при сохранении authority,
result validation и recovery, иначе нужен точный BLOCKED/UNKNOWN.

Чтение переносимого state на другой ОС не означает разрешение resume: paths,
permissions, environment, authority и actual effects проверяются заново.
Поведение и проверки принадлежат [Architecture](02_Architecture.md#core-platform-boundary)
и [Development](03_Development.md#core-platform-checks). Выбор stack/target/host
остаётся в существующем SC-DEC реестре; здесь не создаётся новый набор решений.
