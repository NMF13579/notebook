# AOS — scaffold и первое ядро: implementation brief

Дата интеграции: 2026-09-15. Revision: R7 + HD-01…28. Принятое содержание
первого ядра; runtime launch NOT_RUN. Implementation authorization: NONE.
Git authorization текущей documentation task: NONE.

Это производный handoff к canonical owners, не новый владелец требований.
[Core](../docs/00_Core.md#scaffold-core-decisions) фиксирует Human решения и
SC-DEC; [Reference](../docs/05_Reference.md#first-core-human-source) — exact
исходный R7 subject. Принятие HD не выбирает все 33 FTR и не разрешает эту сборку.

## 1. Результат и scope

Полный предложенный first-core package [S0→K4 / HD-01](../docs/01_Product.md#first-core-selected-scope):
13 core-срезов, минимальные local connectors, durable queue C-015/C-016 и V3
complete-task loop. Никакого уменьшения до X1-only; поздние модули не prerequisite.
Реальный first-core E2E включает весь [HD-28 путь](../docs/03_Development.md#first-core-autonomy-proof),
а не только отдельный product test. Human ACCEPT и последующий local Commit
имеют отдельные проверяемые результаты по HD-26. Push/Merge/Release отдельно.

## 2. Маршрут чтения

| Owner | Что определяет |
|---|---|
| [Core §20](../docs/00_Core.md#scaffold-core-decisions) | Authority, принятые решения, data/dependencies/retention, SC-DEC |
| [Product](../docs/01_Product.md#first-core-selected-scope) | Scope и результат S0–K4 |
| [Features §4.2](../docs/06_Features.md#core-first-scope) | Core-срезы и применимые family safety/negative требования |
| [Architecture](../docs/02_Architecture.md#first-core-build-boundary) | Изоляция, reimplementation/legacy, технический профиль; далее C-015/C-016, V3, state и host |
| [Development §24](../docs/03_Development.md#scaffold-core-development) | Порядок preparation/build, B1, correction, final validation и обязательный HD-28 E2E |
| [Reference](../docs/05_Reference.md#scaffold-core-sources) | Provenance; старый AOS-3 не нормативный owner новой сборки |

## 3. Входы implementation preparation

| Предмет | Принято / оставшаяся работа |
|---|---|
| Scope/contracts | SC-DEC-01 ACCEPTED: current R7/V3 по HD-01 и уточнениям HD-02…28; exact будущий candidate связывается с owners |
| Target/изоляция | AOS-3 выбран; отдельная branch/worktree обязательна. Конкретные имена/path/base/dirty facts выбираются и наблюдаются при preparation; AOS-3 сейчас не меняется |
| Профиль | Python 3.12+, local modular monolith, CLI, macOS-first; Linux/Windows позже. Actual versions/architecture/adapter и команды ещё связать |
| Данные/dependencies | LOCAL_FIRST и bounded dependency policy приняты у Core; разрешённые state/evidence paths, queue limits и фактические existing data routes уточняет исполнитель. Новый external access отдельно |
| Host | Codex выбран первым; core agent-agnostic. Actual capture/admission/checkpoint/wake conformance UNKNOWN/NOT_RUN |
| Parent | B1 и adaptive decomposition приняты. Exact task/revision, outcome/check bindings, finite budget в Human constraints и текущие effects ещё подготовить |
| Launch | SC-DEC-04 NOT_RUN: отдельная explicit runtime authorization с Risk Profile, paths/operations/effects, limits/expiry; этот brief её не выдаёт |

## 4. Нормативность и HOW

Current accepted notebook определяет новое ядро; legacy AOS-3 process docs
REFERENCE_ONLY. Default REIMPLEMENT_FROM_CONTRACT, isolated build, сохранение
старого кода вне active runtime/dependency graph. Exact reuse требует доказанной
совместимости. Малый implementation router и local run/test инструкции подчинены
notebook; копирование всей базы как новых owners не требуется.

Классы, filenames, serializer, state layout, locking, storage engine, queue
implementation и test organization — обратимый HOW. Material новый механизм
рассматривается по HD-13; неизвестный обязательный эффект не маскируется выбором HOW.

## 5. Один parent и продолжение

Применять [HD-08…10](../docs/03_Development.md#first-core-parent-autonomy): внутренние
шаги/переразбиение/обычная correction без новых Human Gates, без расширения scope
и без автоматического выбора следующего независимого parent. Durable state вне
чата обновляется по [HD-16/17](../docs/02_Architecture.md#first-core-durable-state).
Unknown effect сверяется до retry; budgets/история не обнуляются. Наличие записей
не доказывает automatic wake.

## 6. Проверки и завершение

SC-T01…26 и OSS-C01…06 сохраняются; обязательный общий
[HD-28 E2E](../docs/03_Development.md#first-core-autonomy-proof) связывает реальную
разработку, correction, interruption, fresh-session automatic resume, final
validation, настоящий ACCEPT и local Commit. До checks известны команды,
subject/environment, независимый oracle, expected outcomes и Evidence boundary.
Final validator — свежий read-only контекст по HD-21. Findings исправляет отдельный
executor, затем новый candidate и свежая итоговая проверка. Required NOT_RUN/UNKNOWN
не скрываются в PASS. Actual runtime/host/E2E — NOT_RUN.

## 7. Human review и доставка

[HD-22/26](../docs/03_Development.md#first-core-final-review) задают короткую сводку,
optional Details и одно действие review. Только реальный ACCEPT exact candidate
активирует один local Commit в принятом first-core workflow. Этот документационный
пакет не является таким implementation subject и не разрешает Commit сейчас.
Push/Merge/Release не следуют из ACCEPT и требуют отдельных решений.

## 8. Следующий ограниченный предмет

Подготовить exact implementation handoff/preflight package для isolated first-core
build в AOS-3: связать mutable target/profile/inputs и доступные host capabilities,
показать actual NOT_RUN и подготовить SC-DEC-04 packet без выдачи launch authority.
Принятые policy решения SC-DEC-01…03 не спрашивать заново.

---

**История подготовки R4–R7 ниже.** Это прежние authoring/review observations,
не текущий список непринятых решений. Их DRAFT/WAIT_HUMAN/V2 формулировки относятся
к исходным revisions; текущая применимость определяется Core §20 и разделами 1–8.
Исторические PASS не становятся runtime Evidence нынешней сборки.

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
