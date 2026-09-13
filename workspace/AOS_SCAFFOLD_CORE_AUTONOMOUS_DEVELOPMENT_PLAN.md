# AOS — план подготовки документации для автономной разработки scaffold и ядра

Дата: 2026-09-13. Текущий результат: подготовлена документация R1–R7; исправления пяти находок проверки перед коммитом и их статус — в §13. Исторические результаты R1–R7 сохранены ниже. Детализация остаётся SCAFFOLD_CORE_DRAFT; документационный результат не принимает contracts и не запускает runtime.

## 1. Цель и ожидаемый результат

Подготовить согласованные документы, по которым агент после исходного решения человека и отдельной авторизации способен построить scaffold и выбранное ядро, проверить результат, исправить обычные дефекты и восстановить работу после прерывания без ручного управления каждым шагом.

Первоначальная задача подготовила этот план. Последующая прямая инструкция «Реализуй план в созданном рабочем дереве» разрешила перечисленные документационные изменения. Она не запускает создание implementation repository, scaffold, runtime, product tests или Git delivery.

Результат будущего выполнения плана:

1. Один однозначный маршрут от актуальных источников к заданию на реализацию.
2. Определённые границы scaffold и первого ядра, достаточные входы, результаты и критерии завершения.
3. Согласованный порядок реализации и интеграции, включая способ ведения работы до появления собственного controller AOS.
4. Проверяемые сценарии основного цикла, failures/recovery и взаимодействия компонентов.
5. Один компактный implementation brief, производный от canonical owners, с конкретными условиями запуска.
6. Правило последующей доработки каждой фичи для автономной реализации и интеграции с ядром и другими модулями.

Полная проработка остальных фич переносится на их собственные будущие задачи. Их существующие описания сохраняются; в текущей работе уточняются только стыки, необходимые scaffold и ядру.

## 2. Основание и границы

Основание — повторный аудит в текущем диалоге и текущая инструкция пользователя. Проверенный checkout: `/Users/muhammed/Documents/GitHub/notebook`, ветка `dev`, HEAD `8627d1cc01b84a794827673e473850c0187abe5e`, чистое рабочее дерево. При запуске заново проверить mutable facts и применимые AGENTS; прежний worktree из другого плана не использовать автоматически.

Фактическое выполнение: `/Users/muhammed/Documents/GitHub/notebook/.worktrees/scaffold-core-autonomy`, ветка `work/scaffold-core-autonomy`, тот же starting HEAD. До edit единственным untracked input был этот перенесённый план; unrelated tracked changes отсутствовали. Worktree создан отдельной предыдущей командой; текущая работа не создаёт веток и не выполняет Git delivery.

План является рабочим документом, не новым владельцем product/architecture/workflow facts. Семь canonical owners сохраняются. Принятие плана, готовность документации, разрешение на её изменение и разрешение на runtime implementation различаются.

Не входят: переписывание всего репозитория, реализация продукта, перенос в AOS-3, создание CI/CD, установка зависимостей, запуск product tests, удаление или архивирование прежних документов, Commit/Push/Merge/Release. Без отдельного Reopen не изменять frozen subject `AOS/**`.

### Проверенные дефекты и ожидаемое закрытие

Номера ниже локальны для этого плана и не создают новый каталог дефектов.

| Дефект аудита | Текущее основание | Что должно измениться | Этап |
|---|---|---|---|
| Разные маршруты реализации и correction | [Development §11](../docs/03_Development.md), [frozen workflow](../AOS/03_ENGINEERING_PIPELINE.md) | Один актуальный вход; явная применимость прежних пакетов; отсутствие конкурирующих указаний агенту | 1 |
| Решения о repository, stack и first slice расходятся | [Core](../docs/00_Core.md), [прежний blueprint §2](AOS3_IMPLEMENTATION_READY_DRAFT.md) | Каждый существенный вопрос имеет текущее решение с основанием либо точный незакрытый запрос | 1–2 |
| Состав ядра остаётся предложением | [Product MOD-DEC-01…03](../docs/01_Product.md#modular-decisions), [feature inventory](../docs/06_Features.md#4-индекс-каталога) | Согласованные границы выбранных возможностей; поздние модули не превращаются в обязательные зависимости | 2 |
| Scaffold и запуск разработки не связаны с новой петлёй | [Product Foundation](../docs/01_Product.md), [прежняя sequence §16](AOS3_IMPLEMENTATION_READY_DRAFT.md) | Проверяемый scaffold contract, внешний development loop с начала работы, определённая передача собственному controller | 3–4 |
| Контракты связаны, но вход реализации не готов | [Architecture §6.1](../docs/02_Architecture.md#module-contracts), [MOD-S01…15](../docs/03_Development.md#modular-documentation-checks) | Критерии, checks, prerequisites и интеграционные результаты сведены для выбранного scaffold/core scope | 4–6 |
| Runtime-петля не проверена | [Development §§10.1–10.5](../docs/03_Development.md), [loop design](AOS_DEVELOPMENT_COMPLETION_LOOP_DESIGN.md) | Определён будущий способ доказать её работу; runtime остаётся NOT_RUN до отдельной реализации и запуска | 4, 6–7 |

### Paths будущей документационной работы

| Путь | Допустимая область изменения |
|---|---|
| `README.md`, `AGENTS.md` | Единый маршрут чтения и граница текущей документационной задачи; роль knowledge repository и safety сохраняются |
| `docs/00_Core.md` | Текущие решения, source precedence и границы автономности; без автоматической выдачи authority |
| `docs/01_Product.md` | Scope scaffold/core, результат пользователя, порядок срезов и необходимые решения |
| `docs/02_Architecture.md` | Контракты выбранного ядра, owners/consumers, состояния, совместимость и интеграционные границы |
| `docs/03_Development.md` | Вход реализации, внешний development loop, переходы между срезами, проверки, восстановление и handoff |
| `docs/05_Reference.md` | Применимость прежних пакетов и точечные provenance-ссылки, необходимые для закрытия конфликтов |
| `docs/06_Features.md` | Выбранные базовые возможности ядра; только затронутые связи поздних модулей |
| `workspace/AOS_SCAFFOLD_CORE_IMPLEMENTATION_BRIEF.md` | Один новый производный handoff: scope, порядок, ссылки на owners, проверки и условия запуска |
| Этот план | Краткий итог выполнения, незакрытые пункты и фактически выполненные проверки |

`docs/04_Lessons.md`, старые планы, decision records и manifests читаются по необходимости; их исправление не входит в текущий allowlist. Новые изменения вне таблицы требуют отдельного bounded решения. Не создавать новые canonical catalogs или отдельные отчёты на каждый этап.

## 3. Рабочее определение автономности

Человек до запуска определяет продуктовый результат, существенные архитектурные и средовые границы, Risk Profile и полномочия. После этого агент самостоятельно выбирает обратимый HOW, декомпозирует согласованный объём, реализует, проверяет и исправляет его в пределах полномочий.

Обычный дефект, смена worker, окончание одного среза или новая сессия не требуют повторного решения человека сами по себе. Переход к следующему срезу должен быть покрыт исходным scope и полномочиями. Существенное новое product/architecture решение, расширение доступа, неизвестный effect, недоступный обязательный input или исчерпание разрешённых ресурсов дают точную остановку/паузу по canonical правилам.

Целевой финал автономной работы — доказанное техническое завершение scaffold и согласованного ядра с review package. Human acceptance, protected actions и Git delivery сохраняют отдельные основания. Синтетические decisions в test fixtures не предоставляют реальных полномочий и не означают принятие продукта человеком.

Применить два разных предмета проверки:

- **Development loop внешнего агента:** кто начинает разработку, сохраняет прогресс, запускает следующий шаг и возобновляет работу до появления готового AOS.
- **Product loop AOS:** реализуемые controller, envelopes, diagnostics, checks и recovery, которые должны пройти собственную проверку.

Само наличие описания product loop не доказывает способность host продолжить работу после остановки процесса. Host lifecycle и повторный запуск должны иметь конкретное основание; agent prompt не заменяет отсутствующий механизм продолжения.

## 4. Последовательность выполнения

### Этап 1. Согласовать источники и текущие решения

**Пути:** Core, Product, Architecture, Development, Reference, README и AGENTS в пределах таблицы выше.

- Сопоставить текущие owners с frozen `AOS/`, принятым portable package, X1 decision record и прежним AOS-3 blueprint. Читать только разделы, относящиеся к найденным конфликтам.
- Для каждого решения указать предмет, source/record, exact scope, действующее значение либо unresolved conflict. Отделить наличие записи о решении от доказанной применимости к новому scaffold/core scope.
- Не просить повторно принять уже подтверждённое действующее решение. Конфликтующие, неприменимые и отсутствующие решения собрать в один список для итогового пакета.
- Рекомендуемый маршрут для нового scaffold/core: актуальные семь owners → выбранные contracts → производный implementation brief. Это предложение изменения handoff, требующее соответствующего human decision; до него сохранять его статус DRAFT.
- Явно описать роль прежних frozen/portable/blueprint пакетов для новой задачи. Сохранить их bytes и историческую acceptance; новый handoff не должен молча наследовать старые claims или обходить Freeze.
- Устранить в разрешённых навигационных разделах двусмысленность «продолжение одной task» versus «correction обязательно новая task». Не создавать новый владелец workflow.

**Готово, когда:** агент видит один предлагаемый или уже принятый маршрут и точный список оставшихся решений. Нельзя заявить готовность к реализации при unresolved source conflict. Независимые DRAFT-разделы следующих этапов можно готовить без ожидания решений.

### Этап 2. Зафиксировать scaffold/core scope и входные решения

**Пути:** Product, Features; authority/current-decision fields у соответствующих owners.

- Определить один наблюдаемый результат первого ядра и явно отделить его от полного функционала всех feature families.
- Использовать текущие 13 CORE-семейств как исходное предложение: FTR-001/002/003/006/008/009/010/011/012/013/014/016/019. Для каждого назвать необходимую базовую возможность, а не автоматически включать все сценарии семейства. Точный выбор остаётся product decision.
- Уточнить, что scaffold разработки AOS включает подготовку будущего implementation repository и окружения; полный продуктовый installer/bootstrap FTR-004 не становится обязательным только из-за слова «scaffold».
- Разделить объём на scaffold, ядро и будущие расширения. Определить зависимости и конечные критерии каждого среза; номера срезов не создают отдельные Human Gates.
- Согласовать существующее правило manual dogfood с автономной разработкой: пользовательские наблюдения, необходимые product decisions и будущие тесты должны быть названы явно. Если текущий обязательный ручной шаг препятствует целевому автономному интервалу, подготовить точное изменение границы, не обходить её.

До runtime должны быть определены, применительно только к выбранному scope:

| Входное решение | Что требуется |
|---|---|
| Источник истины и состав | Точные действующие owners/revisions, выбранные возможности и критерии scaffold/core |
| Implementation target | Repository/worktree, допустимое начальное состояние, разрешённые и защищённые пути; notebook сохраняет роль knowledge repository |
| Среда | Язык/runtime, допустимые зависимости, способ локальной подготовки и проверки окружения, поддержанный первоначальный platform envelope |
| Взаимодействие и данные | Нужная поверхность, гарантии хранения/восстановления, доверенный capture человеческих решений, data/provider boundary |
| Внешний host | Кто исполняет development loop, как продолжается работа между workers/runs, где сохраняется task state, какие ограничения host существенны |
| Полномочия | Risk Profile, разрешённые операции/effects, execution/correction scope, запреты, ресурсные пределы, срок и условия отзыва |

Не расширять эти решения до лицензии публичного релиза, всех платформ, CI providers или поздних модулей, если scaffold/core от них не зависит.

**Готово, когда:** scope и вопросы decision-ready; предметы, уже решённые authoritative source, не представлены как новые вопросы. До фактического закрытия существенных вопросов readiness ограничена human review.

### Этап 3. Описать scaffold и начало работы без готового AOS

**Пути:** Product, Architecture, Development; производный brief.

Сформировать компактный scaffold contract:

1. Actor, trigger, исходное состояние target и достаточные входы.
2. Наблюдаемый результат: минимальная запускаемая основа выбранного проекта, объявленные зависимости, локальные команды разработки/проверки, сохранение состояния и Evidence. Точный packaging scope выводится из решения этапа 2.
3. Условия успешного старта из чистого поддержанного окружения; distinction source execution, installed execution и native host checks там, где они обязательны для заявленного результата.
4. Отказы: неверный target, конфликт пользовательских файлов, symlink/containment escape, отсутствующая зависимость, невозможность запуска required check, прерывание и неизвестный partial effect.
5. Recovery без скрытой перезаписи, удаления или повторного эффекта.
6. Выходные данные для первого среза ядра и условия автоматического продолжения внутри исходных полномочий.

Определить внешний bootstrap workflow: чтение задания → fresh preflight → проверка исходных полномочий → действие → проверка → диагностика/исправление → фиксация состояния → следующий шаг. До готовности продукта он не вызывает отсутствующие команды, validators или controller AOS. Требуемые гарантии внешнего host должны быть обеспечены его действующими возможностями; если это невозможно, зависимая автономность остаётся BLOCKED.

**Готово, когда:** первый эффект не требует уже установленного AOS; scaffold имеет собственный completion predicate, проверяемые failures и достаточный handoff ядру.

### Этап 4. Довести contracts ядра и замкнуть петлю

**Пути:** Features, Architecture, Development; производный brief.

- Для выбранной базовой возможности проверить actor/trigger, предусловия, inputs/outputs, states/transitions, failures/recovery, constraints, acceptance, negatives и material unknowns. Уточнять только недостаточные разделы, сохраняя уже пригодные contracts.
- Для каждого перехода подтвердить producer, consumer, contract/version, обязательные данные, владелец state, момент доступности, failure и повторную проверку. Проверить обязательные зависимости именно запуска, а не только наличие взаимных ссылок.
- Сохранить canonical controller-action matrix, task/run separation, parent authorization, fresh envelopes, D0…D5, Correction Gate, anti-loop, reconciliation и completion predicate. Исправлять выявленную неоднозначность у соответствующего owner; не изобретать параллельную state machine.
- Определить, как одна общая scaffold/core-задача распадается на dependency-ready части без автоматического расширения scope. Evidence отдельных частей должно связываться с критериями целого; сумма закрытых частей не доказывает интеграцию.
- Описать переход от внешнего development loop к собственному controller AOS: обязательные результаты проверки, граница возможной передачи, сохранение authority/state/evidence и безопасное поведение при неготовности продукта. Внешний маршрут остаётся допустимым до доказанной готовности замены.
- Проверить, что работу не блокирует optional CI, индекс, installer, patterns или audit service, если их результат не нужен выбранному сценарию. Required check без заранее допустимого equivalent остаётся NOT_RUN.
- Определить какие public contract/error/version guarantees должны быть фиксированы до реализации. Классы, algorithms, storage engine, internal schemas и организация тестов остаются обратимым HOW агента внутри этих гарантий.

**Готово, когда:** полный core journey имеет все входы и выходы, correction не требует новой постановки той же задачи, а внешняя разработка не зависит от недостроенной собственной инфраструктуры.

### Этап 5. Определить порядок будущего добавления фич

**Пути:** Development, Architecture; затронутые ссылки Features.

Согласовать один короткий маршрут внутри существующего workflow:

выбранная фича → feature-specific contract → влияние на ядро/модули → достаточный implementation brief и отдельная authority → реализация → contract/integration/regression checks → review и решение.

До автономного запуска каждой будущей фичи должны быть определены:

- Пользовательский результат, exact scope, входы, выходы и критерии завершения.
- Consumers/producers в ядре и других модулях; required/conditional зависимости и отсутствие startup-циклов.
- Владелец данных и состояния, совместимость contracts и сохранённых задач, поведение старого consumer.
- Подключение, отсутствие/недоступность, отключение и прерывание операции; сохранность пользовательских данных.
- Permission/effect boundary и отсутствие обхода core safety.
- Проверки самой фичи, каждого затронутого стыка и сохранности базового core journey; матрица всех пар модулей не требуется без реального взаимодействия.

Полные ТЗ поздних модулей сейчас не перерабатывать. Не проектировать plugin framework, marketplace или универсальную platform ради будущей интеграции. Обнаруженная действительно обязательная возможность модуля требует явного решения о включении её минимального объёма либо сужении зависимого core-сценария.

**Готово, когда:** последующие фичи можно готовить по одной, а влияние каждой на существующий продукт проверяемо и ограничено.

### Этап 6. Собрать implementation handoff и матрицу проверок

**Пути:** `workspace/AOS_SCAFFOLD_CORE_IMPLEMENTATION_BRIEF.md`, Development; необходимые ссылки на owners.

Создать один компактный brief. Он ссылается на владельцев фактов и не копирует полные dossiers. Включить:

1. Цель scaffold/core, выбранный scope и non-goals.
2. Действующий маршрут источников и исходные решения.
3. Target, окружение, host, входы и preflight requirements.
4. Порядок dependency-ready срезов с observable outputs и критериями перехода.
5. Запрошенные operations/paths/effects, запреты и требования к отдельной авторизации; brief не содержит выданных агентом полномочий.
6. Внешний development loop, условия передачи продукту и recovery после остановки.
7. Матрицу «критерий → сценарий → observable expected result → required check → Evidence → affected consumers».
8. Обязательные ограничения результата, список remaining decisions и следующий допустимый шаг.

Для выбранного toolchain указать предполагаемый интерфейс запуска checks, предусловия, oracle и результат. Новая команда может быть deliverable будущей реализации, но должна быть так помечена; нельзя предписывать её как уже существующее условие первого запуска. Executable fixtures и tests создаются в implementation task, не в документационной работе.

Минимальные проверочные journeys:

| Сценарий | Что должен доказать будущий запуск |
|---|---|
| Чистое поддержанное окружение → scaffold | Воспроизводимый старт, объявленные зависимости, достаточный результат без ручной починки окружения |
| Scaffold → первый срез ядра | Выходные inputs достаточны; переход покрыт исходным scope/authority |
| Достаточная заранее заданная задача → core result | Связный основной путь до технического завершения без дополнительных постановок |
| Known defect → диагностика → correction | Подтверждаемая причина/прогноз, fresh envelope, новое Evidence и закрытый criterion |
| Повтор без прогресса | Ledger сохраняется, диагностика расширяется; бесконечная patch/retry-петля не возникает |
| Finding итогового validator | Отдельный corrector/new candidate и повторная affected validation; validator не меняет subject |
| Прерывание до/после effect, новая сессия | Reconciliation и отсутствие двойного эффекта; state/authority перепроверены |
| Пауза по run resources | Сохраняется active task, host resume не обнуляет ledger и не требует новой формулировки цели |
| Отзыв/истечение authority, stale identity, запрещённый effect | Отказ до эффекта; остановка не выдаётся за техническое завершение |
| Required check недоступен, Evidence stale или impact неизвестен | Нет ложного PASS; виден конкретный незакрытый критерий |
| Пользовательские изменения, path escape | Сохранность unrelated state и соблюдение scope |
| Ядро без optional-модулей | Базовый сценарий исполним; условные недоступные сценарии честно ограничены |
| Изменение общего contract / отключение модуля | Найдены affected consumers, совместимость и recovery; core safety сохраняется |
| Завершение всех частей | Итоговый integrated result доказан отдельно от количества выполненных задач |

**Готово, когда:** агенту достаточно brief и ограниченного набора owner-ссылок, чтобы составить инженерное выполнение; он не вынужден самостоятельно выбирать продуктовый scope, угадывать authority или восстанавливать решения по старым планам.

### Этап 7. Повторно проверить документацию и передать на решение

**Проверка:** read-only относительно зафиксированного результата authoring. Независимый reviewer — только если это отдельно требуется/разрешено; не объявлять self-check независимой валидацией.

- Пройти документально каждый journey этапа 6: input → owner → допустимое действие → output/state → следующий шаг → критерий завершения. Это проверка описания, не runtime simulation или Evidence исполнения.
- Проверить достижимость первого шага без продукта, конец каждого среза, resume с ограничениями host, correction и итоговую интеграцию.
- Убедиться, что нет обязательных ссылок на устаревшие workflow и скрытой необходимости человека для обычного обратимого HOW.
- Проверить scope/diff, Markdown links/fences, затронутые YAML, сохранность семи owners, уникальность FTR/LES и отсутствие authority promotion. `git diff --check` выполнить при наличии checkout.
- Отдельно проверить новые untracked artifacts: один `git diff --check` не проверяет их содержимое.
- Проверить, что frozen `AOS/**`, прежние acceptance records и unrelated state не изменены.
- По окончании authoring передать один конкретный decision-ready пакет: итоговые документы, остаточные вопросы с вариантами и последствиями, checks и NOT_RUN. Не запрашивать принятие каждого обычного редакционного шага.
- Finding независимой проверки не исправляется validator. Исправление выполняется отдельной разрешённой authoring/correction работой, затем повторяется affected verification.

**Готово, когда:** результат описан по фактическому уровню готовности ниже и работа остановлена после отчёта. Запуск runtime остаётся отдельной задачей.

## 5. Критерии завершения плана

| Уровень | Условие |
|---|---|
| Документация готова к решению человека | Все этапы authoring выполнены; conflicts не скрыты; оставшиеся вопросы конкретны; документальные checks прошли |
| Документация достаточна для реализации scaffold/core | Приняты точный scope и применимые contracts; существенные входные решения закрыты; scaffold/core sequence, host continuation, проверки и recovery однозначны; required inputs не зависят от ещё не созданного продукта |
| Реализация разрешена | Отдельная действующая авторизация на exact target/task/operations/effects; готовность документов сама её не создаёт |
| Автономное выполнение доказано | Отдельно реализованы и выполнены согласованные сценарии на exact candidate, включая host/resume и negative paths; в этом плане NOT_RUN |

Если остаётся существенное human-only решение, допустим только первый уровень, а зависимая готовность к реализации — BLOCKED. Готовность поздних модулей не требуется для закрытия scaffold/core, когда они не являются реальной required зависимостью. Product acceptance и Git delivery не включаются автоматически ни в один уровень таблицы.

## 6. Результат выполнения 2026-09-13

**Вывод:** документационная работа завершена в разрешённом scope. Подготовлен согласованный DRAFT для человеческого решения. Готовность к реализации остаётся BLOCKED до SC-DEC-01…03, фактического host conformance и отдельного launch SC-DEC-04. Это остаточные входные решения/проверки, а не скрытые claims о выполненном runtime.

| Этап | Сделано и где | Фактический outcome |
|---|---|---|
| 1. Источники/решения | README/AGENTS и Core §20 задают один маршрут новой задачи; Development отделяет старый frozen scope; Reference §14 связывает current owners, X1, portable, blueprint и loop design | Документальная сверка PASS; исторические source/decision оговорки сохранены. Применение нового handoff к runtime ожидает SC-DEC-01 |
| 2. Scope | Product §17 описывает S0–K4; Features §4.2 и 13 dossier-срезов ограничивают базовые возможности; поздние модули сохранены | DRAFT состава подготовлен; исходные human dispositions не изменены; SC-DEC-01…03 открыты |
| 3. Scaffold | Product задаёт actor/input/output/failure/recovery; Architecture §§6.2–6.3 — профиль/host; Development §24 — начало без готового AOS | Документальный bootstrap route замкнут; реальная host capability и environment verification NOT_RUN |
| 4. Ядро/петля | Уточнены consumers, 13 core-срезов и порядок обязательных гарантий до effect; внешний loop отделён от продукта и необязательной передачи controller | Canonical matrix и completion predicate сохранены; correction, anti-loop и recovery прослежены; runtime NOT_RUN |
| 5. Поздние фичи | Development §25 — одна фича за раз, реальные стыки/версии/ownership/permissions и core regression | Полные поздние dossiers не переработаны; plugin infrastructure не добавлена |
| 6. Handoff/checks | [Implementation brief](AOS_SCAFFOLD_CORE_IMPLEMENTATION_BRIEF.md), Development §24.4–24.5: command-binding contract и SC-T01…14 | Brief готов к рассмотрению; операции checks описаны как будущие entrypoints, не существующие команды |
| 7. Проверка | Самопроверка автора: semantic walkthrough, mechanical checks и byte/scope preservation | Документальные checks PASS. Независимая validation NOT_RUN; human review NOT_RUN |

### Смысловая самопроверка

Проверен маршрут каждого SC-T01…14 как описанного сценария, без запуска runtime:

- S0 получает внешний host/authority и test harness до собственного AOS; положительный запуск не зависит от missing product tools.
- K1 использует достаточные исходные contracts без выдуманного нового approval; material gap даёт точный gate.
- До K2 доступны state/authority/validation/recovery; named C-inputs в 23 уточнённых dossiers имеют consumers в Architecture.
- CHECK и FINAL_VALIDATE возвращают finding контроллеру; отдельный corrector, fresh gate/envelope/candidate и affected Evidence не смешаны с validator.
- Ledger, ресурсы и unknown effects сохраняются через worker stop/run pause/resume. Manual resume не повышен до automatic host continuation.
- SC-T12/13 проверяют отсутствие capability/совместимость через core consumers и contract fixtures, не требуют реализации всех поздних модулей.
- K4 и SC-T14 требуют интегрированного real-adapter результата; counts частей и synthetic tests не заменяют overall Evidence. Human acceptance и Git delivery остаются отдельно.

При self-check уточнены прямое чтение C-010 контроллером, передача C-008 именно владельцу scope reconciliation и остановка worker отдельно от task/run. Это исправления текущего authoring; независимый validator subject не менял и не запускался.

### Paths и проверки

Изменены только `README.md`, `AGENTS.md`, `docs/00_Core.md`, `docs/01_Product.md`, `docs/02_Architecture.md`, `docs/03_Development.md`, `docs/05_Reference.md`, `docs/06_Features.md`, этот план; создан один `workspace/AOS_SCAFFOLD_CORE_IMPLEMENTATION_BRIEF.md`.

PASS: scope относительно исходного snapshot; links/anchors/fences и whitespace, включая новые untracked artifacts; YAML frontmatter семи owners; семь canonical files; 30 уникальных FTR и 49 LES с сохранением LES-001…042; 13 core-срезов; 14 SC-T; unchanged dispositions; named input/consumer mapping; неизменность canonical state matrix и completion predicate; отсутствие runtime/Git authority grants; `git diff --check`.

Проверены actual hashes пяти X1 ARTIFACT records, 11 portable content files и трёх frozen subject files. Все 381 исходный tracked file сопоставлены с starting snapshot: вне разрешённых путей изменений нет. `AOS/**`, `docs/04_Lessons.md`, старые планы и decision records сохранены. 12 sibling-checkout links в Reference заменены exact repository/snapshot/path locators, сохранив их исходный предмет и устранив зависимость от глубины worktree.

NOT_RUN: реализация scaffold/ядра, executable product fixtures/tests, native/host conformance, самостоятельный S0–K4 development run, исторические runtime-аудиты, независимая validation, человеческое принятие нового candidate, Commit/Push/Merge/Release. Host identity/continuation, target binding, первоначальный environment и trusted capture остаются существенными открытыми входами; их нельзя признать решёнными из данного документа.

**Следующий bounded action:** рассмотреть [пакет SC-DEC-01…03](../docs/00_Core.md#scaffold-core-decisions) на подготовленных owners/brief. Отдельная runtime task и её полномочия SC-DEC-04 оформляются после этого; текущий документационный run завершается отчётом.


## 7. Исправление переходов и initial state — R2

Прямая инструкция «Implement the proposed plan» разрешила документационные
исправления четырёх находок в том же worktree. Цель — однозначные переходы
scaffold/core, без runtime, изменения frozen-пакетов, feature disposition или Git.

### Изменения

| Находка | Решение и owner | Проверяемый маршрут |
|---|---|---|
| Диагностический check не имел перехода | Architecture: матрица V2 и C-009 purpose; Development §10.3; FTR-010/011 | DIAGNOSE → CHECK → DIAGNOSE; correction либо SELECT_NEXT_ACTION без mutation, без переноса diagnostic PASS в acceptance |
| Конфликт state требовал отсутствующего ребра | Development: протокол конфликта; Architecture §7; FTR-014/016 | Loser stop без shared update → единственный владелец → fresh IDLE/resume/RECOVER_STATE; terminal/wait не обходятся |
| Один worker выполнял correction до stop | FTR-010: раздельные роли и передача C-008 → subject → C-009 | EXECUTE stop → checker observation → controller gate → отдельный CORRECT stop → affected/final checks |
| Не описан первый C-012 | Development: initial-state contract; Architecture C-012; FTR-016 | Явное создание при доказанной пустой истории → BIND_TASK → RECOVER_STATE; resume missing/corrupt record не создаёт пустую задачу |

V2 набор включает state machine, C-006A, C-009 и C-009A. C-005/C-006 остаются
V1; расширения authority нет. C-012 сохраняет V2 binding. Старые и смешанные
records не мигрируют и не получают V2 resume автоматически; host V1 report
не является V2 conformance. Runtime-применение требует принятия revision и
отдельного launch по остающимся SC-DEC решениям.

Изменены только пять paths относительно начала R2: `docs/02_Architecture.md`,
`docs/03_Development.md`, `docs/06_Features.md`,
`workspace/AOS_SCAFFOLD_CORE_IMPLEMENTATION_BRIEF.md` и этот план.
Существующие R1 изменения других файлов сохранены. Новых файлов в repository нет.

### Проверка R2

К SC-T01…14 добавлены SC-T15…18 с отдельными вариантами diagnostic purpose,
conflicting controllers, initial creation/resume и version compatibility.
Обязательная проверка — не только наличие ID: каждый маршрут прослеживается
через input → producer → consumer → transition → observation → next action.
Документальный author self-check R2: PASS. Это не independent validation.

- Проверен граф: 9 состояний, 26 рёбер, без неизвестных destinations. Пять составных
  маршрутов охватывают диагностику без mutation, final finding/correction,
  recovery из EXECUTE и CHECK, первоначальный запуск. C-009 purpose table сверена
  с допустимыми рёбрами; diagnostic return не закрывает acceptance criteria.
- Семантически прослежены четыре находки: отдельный worker stop, loser без shared
  writes, takeover с актуальным владельцем, initial creation отдельно от missing
  resume. Terminal/wait и uncertain effects не обходятся; новые checks SC-T15…18
  описывают наблюдаемые positive/negative outcomes, но пока не исполнены.
- Именованные C-inputs dossiers сверены с consumers, включая C-005/C-006 для
  initial state FTR-016. V2 bindings согласованы; C-005/C-006 и completion predicate
  не расширены. Исходные feature dispositions/maturity/runtime status сохранены.
- 168 локальных Markdown links/anchors и fences пяти файлов — PASS; frontmatter
  семи owners и 40 YAML blocks затронутых owners читаются; git diff --check — PASS.
- Сохранены семь canonical owners, 30 уникальных FTR и 49 уникальных LES,
  включая LES-001…042. Отсутствуют новые implementation/git authorization grants.
- Сверка с snapshot начала R2: изменены ровно пять разрешённых файлов, остальные
  378 файлов сохранены по bytes, новых/удалённых файлов нет. Основной checkout
  остаётся чистым; frozen/history вне пяти paths не менялись.

Сбой первой проверки LES был дефектом checker: он искал заголовки уровня 2,
тогда как каталог использует уровень 3. После исправления read-only проверки
полный затронутый набор invariants прошёл; документ Lessons не изменялся.

Runtime всех SC-T, real host conformance, independent validation, Human ACCEPT,
Commit/Push/Merge/Release — NOT_RUN. Исправление документа не доказывает работу
host или продукта. Следующий bounded action после документального self-check —
read-only семантическая проверка R2; runtime не запускается автоматически.


## 8. Переносимость и пакет открытых решений — R3

Основание: человек потребовал максимальную переносимость ОС, указал личное
использование macOS и выбрал «macOS первой» при сохранении целевых Linux/Windows.
Инструкция «Implement the proposed plan» разрешила только документационную правку
в текущем worktree. Ни runtime, ни Git delivery не выполняются.

### Выполненные изменения

- Product закрепляет переносимость ядра/предметных данных с S0 и первую native
  проверку на exact macOS profile. Linux/Windows остаются целевыми, непроверенными.
- Architecture отделяет OS effects от ядра: filesystem/process/permissions/tools,
  capabilities и проверенный fallback; чтение C-012 на другой ОС не разрешает
  resume, silent path rewrite или сброс ledger.
- Core сохраняет единственный SC-DEC реестр: рекомендация, альтернатива, требуемый
  ответ и срок. Переносимость/порядок ОС уже выбраны; target/stack/adapter/host/data
  остаются открытыми. SC-DEC-04 остаётся отдельным launch authorization.
- В FTR-002/008/009/010/011/013/014/016 уточнены только платформенные границы.
  Dispositions, состав ядра, C-contract versions и матрица V2 не меняются.
- Development добавляет SC-T19/20: capabilities/filesystem/process и перенос
  state/support claims; macOS-first не позволяет выдать fixtures за native
  Linux/Windows Evidence. Brief R3 ссылается на owners и пакет решений.

Набор изменений R3: `docs/00_Core.md`, `docs/01_Product.md`,
`docs/02_Architecture.md`, `docs/03_Development.md`, `docs/06_Features.md`,
`workspace/AOS_SCAFFOLD_CORE_IMPLEMENTATION_BRIEF.md` и этот план.
README/AGENTS, Reference, Lessons и frozen/history не изменяются в R3.

### Проверка и оставшиеся действия

Документальный author self-check R3 — PASS; independent validation не выполнена. Семантический маршрут:
Product portability → Architecture adapters/capabilities → восемь dossiers →
SC-T19/20 → brief и SC-DEC. Проверяются отсутствие macOS-only зависимости ядра,
отделение OS choice от platform Evidence, scoped failure и запрет silent resume.

Runtime/native проверки всех ОС и real-host conformance — NOT_RUN, пригодность
host — UNKNOWN. Independent validation и Human ACCEPT полного пакета — NOT_RUN.
Следующий bounded action — read-only рассмотрение R3 и конкретные ответы на
остаточные SC-DEC-01…03; SC-DEC-04 оформляется только перед отдельным запуском.


Фактически выполненные checks R3:

- Семантически сверены заданные требования ОС, рекомендации SC-DEC, платформенная
  граница и восемь dossiers. MacOS-first не превращён в обязательную macOS-зависимость
  ядра; Linux/Windows не получили native PASS. Выбор host отделён от conformance,
  перенос state — от resume, а локальный fallback — от выдачи полномочий.
- 207 локальных ссылок/anchors семи файлов и Markdown fences — PASS. Читаются
  frontmatter семи owners и 51 YAML block canonical package; git diff --check — PASS.
- Сохранены 7 owners, 30 FTR, 49 LES, feature dispositions/maturity/runtime status.
  Матрица V2 содержит прежние 9 states/26 edges. Добавлены только SC-T19/20;
  полный набор теперь SC-T01…20. Новые поля/версии C-contracts не вводились.
- SC-DEC-01…04 остаются единственным scoped реестром; выбранная часть SC-DEC-02
  выделена, остальные параметры OPEN, SC-DEC-01 WAIT_HUMAN, SC-DEC-04 NOT_RUN.
  В документах нет новых implementation/git authorization grants.
- Snapshot начала R3: изменены ровно 7 разрешённых файлов, остальные 376 файлов
  сохранены по bytes; новых/удалённых файлов нет. Основной checkout чистый,
  frozen/history вне allowlist сохранены.

Эти результаты относятся к документам. Runtime/OS/host conformance и выполнение
SC-T сценариев не запускались; синтетические проверки документа не выданы за
работоспособность платформы.


## 9. Модуль 005+022 и исправления аудита — R4

Человек выбрал «005+022 соберем в модуль», затем поручил выполнить предложенный
план исправлений. Работа ограничена документацией в текущем worktree;
остальные объединения, runtime, plugin framework и Git delivery не выполняются.

### Что изменено

- Модуль «Архитектурные решения и patterns» объединяет размещение FTR-005/022.
  Владение ADR и pattern cards, FTR-ID, acceptance и исходные X1 dispositions
  сохраняются раздельно. При отсутствии библиотеки ADR остаётся доступен;
  рекомендация не запускает обязательный human gate или execution.
- MOD-DEC-01 теперь различает 8 сценарных семейств и 7 модулей. 13 core-семейств,
  2 support-модуля и 7 отложенных семейств сохранены. Принята только группировка;
  остающиеся решения и полнота implementation contracts не повышены.
- C-011 указан как условный вход FTR-025; C-004 как условный вход reuse FTR-005/022;
  C-014 как результат handoff для FTR-024. Consumers согласованы у Architecture.
  Будущий результат не требуется до первоначальной подготовки.
- FTR-017 разделяет Query/Build/Refresh, FTR-030 — Check/Migration/Sunset;
  read-only запрос не запускает подготовительные effects автоматически.
- FTR-015 различает local Commit и операции с remote targets; явная policy
  сохраняется. FTR-024 готовит package/action request, FTR-015 единственный
  исполнитель возвращает C-014; unknown outcome reconciled без повторного dispatch.
- Добавлены MOD-S16…23. Это сценарии выбранных поздних модулей, не новые required
  capabilities минимального S0–K4. Development проверяет процесс, условные inputs
  и acceptance examples, а не только наличие названий contracts во входах.

Изменены `docs/00_Core.md`, `docs/01_Product.md`, `docs/02_Architecture.md`,
`docs/03_Development.md`, `docs/06_Features.md`,
`workspace/AOS_SCAFFOLD_CORE_IMPLEMENTATION_BRIEF.md` и этот план. В Features
затронуты каталог/общая граница и dossiers 005/015/017/022/024/025/030;
остальные dossiers не перерабатывались. FTR-024 остаётся shared-default,
его уточнение ограничено handoff. Public C-contract schemas и матрица V2 прежние.

### Проверка и ограничения

Документальный author self-check R4 — PASS; независимая validation не выполнялась.
Восемь MOD-S16…23 прослежены как описанные маршруты input → producer → consumer
→ transition → result → next action; они не исполнялись как runtime tests.

- Проверены no-need и ADR без библиотеки, recommendation без material gate,
  reuse/staleness, отказ/отключение, scoped C-011 processing, read-only Query/Check,
  local Commit и единственный Release executor. Обратная связь 005↔022 не создаёт
  recursive ADR: lookup из FTR-005 возвращает candidates в текущий анализ.
- 216 локальных links/anchors и Markdown fences — PASS; frontmatter 7 owners
  и 51 YAML block читаются; git diff --check — PASS.
- Проверены 40 именованных входных связей и отдельно условные C-004 → 005/022,
  C-011 → 025, C-014 → 024. В примерах проверено фактическое чтение, а не только
  совпадение имени contract; первоначальная подготовка не требует будущего result.
- 30 FTR, dispositions/maturity/runtime statuses, shared-default markers сохранены.
  Изменены только dossiers 005/015/017/022/024/025/030; остальные 23 byte-identical
  состоянию начала R4. Схемы Architecture, матрица V2 и completion predicate
  также byte-identical. Полный набор MOD-S01…23; SC-T01…20 не расширялся.
- Сверка snapshot начала R4: изменены ровно 7 разрешённых файлов, 376 остальных
  сохранены по bytes; новых/удалённых файлов нет. Основной checkout чистый.
  Frozen/history и существующие сторонние изменения не затронуты.

Группировка выбрана человеком; PASS относится к документационному исправлению,
не к принятию полного module contract или готовности implementation.

Runtime/native/module integration, независимая validation и принятие полных
contracts — NOT_RUN. Выбранная группировка не разрешает их implementation.
Следующий bounded action — read-only проверка R4 и рассмотрение оставшихся
решений; поздние фичи готовятся к автономной реализации отдельно по выбору.


## 10. Пять находок повторного аудита — R5

Цель — однозначный документальный проход S0–K4 после согласования входов.
Работа выполнена в существующем worktree; исторические R1–R4/frozen artifacts
не переписаны. Человек выбрал явные lifecycle-переходы внутри одной задачи;
полное принятие конкретного V3 contract и launch остаются отдельными фактами.

### Исправления и владельцы

1. Core ссылается на единый Result Contract C-009/Architecture; FTR-011 владеет
   поведением. HUMAN_REVIEW_REQUIRED — document maturity, WAIT_HUMAN — task state,
   неизвестное техническое значение не нормализуется.
2. Development §10.0 задаёт lifecycle transitions, текущий C-012 и исходный C-005,
   отдельные workers, atomic admission/state/event/consumption, pause и terminal
   REVIEW. Architecture связывает V3 envelopes/gate с exact исходным tuple.
   Девять controller actions и 26 рёбер сохранены; C-005/C-006 V1 без смены полей.
   Старые V1/V2/mixed records не получают V3 effect/resume.
3. FTR-014 использует полный/неполный/отсутствующий C-008; missing report не
   запрещает read-only reconciliation по admission/ledger/target. Recovery C-010
   имеет собственную provenance и передаётся FTR-013, не подделывая исходный C-008.
4. Stage report различает lifecycle/action, parent identity/revision/digest и
   отдельные kind/identity/digest/consumption envelope. Parent не расходуется;
   NONE/NOT_APPLICABLE требует причины, UNKNOWN не превращается в false/UNUSED.
5. Product/brief ссылаются на полный набор SC-T01…22. SC-T21/22 проверяют
   vocabulary/report/lifecycle, SC-T09/16 расширены missing report и atomicity cases.

Изменены Core, Product, Architecture, Development, затронутые core-досье Features,
существующие implementation brief и этот план. Scope, placements, 005+022,
feature dispositions, target/host decisions и repository role сохранены.

### Проверки R5

Author self-check R5: PASS, только DOCUMENTATION_AUTHOR_SELF_CHECK.

- Прослежён full-cycle путь с раздельными lifecycle/action: EXECUTE → CHECK →
  DIAGNOSE → CORRECT → CHECK → FINAL_VALIDATE → REVIEW. Исходный C-005 сохранён,
  переходы совместимы с 26 controller edges; standalone read-only mutation,
  неготовый PLAN и повтор terminal task отвергаются описанными правилами.
- Проверены документальные варианты SC-T21/22: шесть enums и invalid значения,
  отдельные parent/envelopes двух workers, replay/NONE/UNKNOWN, diagnostic PASS,
  final finding, повтор stage, pause/resume и конфликт/прерывание admission.
  Исходный tuple допуска и текущий active action различены; собственное durable
  admission не обесценивает observation. Это semantic walkthrough, не runtime tests.
- SC-T09/16: full/partial/missing C-008, effect/no-effect/UNKNOWN; read-only
  reconciliation и собственный C-010 доведены до FTR-013. Карта consumers включает
  чтение admission bindings recovery и сборщиком report.
- C-005/C-006 YAML byte-identical к исходному R4; в YAML C-006A/C-009/C-009A
  изменены только version identifiers. Девять controller actions/26 рёбер сохранены;
  новые обязательные lifecycle semantics явно требуют V3 compatibility.
- 236 локальных links/anchors и Markdown fences — PASS. 49 YAML blocks/frontmatter
  разобраны Ruby YAML.safe_load; PyYAML отсутствует в доступных Python runtimes,
  установка не требовалась. git diff --check — PASS.
- Из 383 исходных файлов изменены ровно семь разрешённых, остальные 376 сохранены.
  Остались семь canonical docs, 30 FTR и 13 core-срезов; placements/005+022 и
  dispositions неизменны. Изменены восемь core-досье 006/008/010/011/012/013/014/016,
  остальные 22 byte-identical к R4. Исторические R1–R4 сохранены.

Независимая semantic validation, runtime/native/host conformance, автоматический
S0–K4 development run и Git delivery — NOT_RUN. Документальный PASS не закрывает
SC-DEC-01…04 и не подтверждает работоспособность будущей реализации.


## 11. Требование автономной сборки каждого модуля — R6

Текущая инструкция человека распространяет требование автономной разработки на
каждый выбранный модуль целиком. Product задаёт общий outcome; Development §25
описывает достаточный пакет, parent loop и MOD-A01…05; Features применяет правило
к 005+022 без изменения FTR/dispositions. Brief больше не требует отдельного
ручного запуска каждой поздней фичи. Core фиксирует направление и сохраняет
отдельность принятия точных contracts и runtime authority.

Полный build включает внутренние фичи/стыки, declared интеграции, correction и
supported resume. Feature PASS не закрывает parent module; реальные human gates
продукта проверяются отдельно от authority разработки. Все поздние contracts
автоматически ready не объявлены. V3/C-схемы и controller matrix неизменны.

Author self-check R6: PASS, DOCUMENTATION_AUTHOR_SELF_CHECK.

- Достаточный module input доведён до одного parent run и общего completion;
  внутренние фичи не создают новые Human Gates. Missing consumer/material decision,
  дефект стыка при отдельных feature PASS, interruption и real integration
  regression имеют разные исходы в MOD-A01…05; это документальная проверка.
- 228 relative links/anchors, Markdown fences, 40 YAML blocks/frontmatter
  (Ruby YAML.safe_load) и git diff --check — PASS.
- Изменены ровно шесть существующих документов; остальные 377 файлов сохранены.
  Все 30 dossiers, placements и FTR dispositions неизменны; новые требования
  находятся у owners и в общей границе 005+022. Architecture/C-схемы/матрица V3
  byte-identical до/после; исторические R1–R5 не переписаны.

Runtime/module builds, real-host MOD-A01…05, независимая validation и Git delivery
— NOT_RUN. Общее требование не означает готовность или принятие всех модулей.


## 12. Протокол фич/модулей, коннекторы и очереди — R7

Человек выбрал смешанный exchange и минимальные локальные коннекторы/сохраняемую
очередь уже в первом ядре. Выполняется документационная подготовка в существующем
worktree; это не runtime implementation или автоматическое принятие full contracts.

### Выполненные изменения

- Core фиксирует выбранные решения и обязательную проверку агентом §25.4/25.5;
  Product задаёт outcome, операции подключения/удаления и уточнённые выходы S0–K4.
- Architecture добавляет C-015 Module Connection V1 и C-016 Message/Delivery V1:
  direct read, queued commands/events, current admission, operation identity,
  durable acceptance/result-before-ack, finite limits, cancellation и recovery.
  Очередь не backlog FTR-007 и не источник authority; bootstrap не зависит от
  ещё не созданной очереди. C-001…C-014 и controller matrix V3 сохранены.
- Development §25.4 задаёт формирование и semantic проверку фичи/модуля, §25.5 —
  add/enable/update/disable/remove implementation/delete data. Структура реализации
  описана ролями; конкретные directories/storage/transport — HOW принятого profile.
- SC-T23…26 расширяют первое ядро, MOD-A06/07 — module readiness и автономный build.
  Features описывает 005+022 как первый пример read/analysis/save/event и уточняет
  обязанности 004/005/007/008/009/010/011/014/016/019/022. Остальные dossiers сохранены.
- Brief R7 связывает current owners и SC-T01…26. Исторические R1–R6 не переписаны;
  семь canonical docs, 30 FTR identities и placements не расширены.

### Проверки и статус R7

Author self-check: PASS в пределах DOCUMENTATION_AUTHOR_SELF_CHECK.

- Scope/preservation: изменены только семь разрешённых файлов относительно входа
  R7; остальные 376 проинвентаризированных файлов сохранены. Состав 30 FTR,
  13 core families, placements и dispositions не изменён; 19 незатронутых dossiers
  сохранены побайтно. Исторические разделы плана/brief сохранены.
- Structural checks: 290 relative links/anchors, Markdown fences, 49 YAML blocks
  и frontmatter прошли проверку; `git diff --check` — PASS. В `docs/` остаются семь
  canonical Markdown owners. Существующие YAML schemas и controller matrix V3
  сохранены; 43 именованных input edges имеют declared consumers.
- Semantic self-review: прослежены C-015/C-016 producer/consumer responsibilities,
  S0 bootstrap → K2 dispatch → K3 recovery → K4 integration и 005+022
  lookup → analysis → save → observation. Проверены fresh authority/subject,
  duplicate/lost-ack/unknown effect, истёкший claim при живом worker, конечные
  limits, cancellation и сохранность pending/history при lifecycle operations.
  Analysis и save не ждут друг друга внутри занятого ordering key.
- Acceptance coverage: описаны 26 SC cases и семь MOD-A cases, включая отдельные
  positive/negative bindings и требования к независимому oracle. Это проверка
  документации сценариев, а не их выполнение.

Runtime/native/module builds, реальные SC-T23…26/MOD-A06/07, independent validation
и Git delivery — NOT_RUN. SC-DEC-01…04 остаются отдельными решениями/условиями;
implementation и Git authorization — NONE. Конкретные limits/profile и support
claims не выбраны догадкой; общее требование не означает готовность всех модулей.

## 13. Исправления перед коммитом R7

Прямая инструкция «Исправь» разрешила bounded документационную correction пяти
находок read-only аудита. Scope: AGENTS.md, Architecture, Development, Features,
существующие brief и план. Остальные owner-документы, frozen/history sources,
runtime и Git delivery не изменяются. Номера F01–F05 локальны для этого исправления.

| Находка | Исправление и затронутая проверка |
|---|---|
| F01 — recovery IDLE противоречил FTR-006.N01 | Development §10.2 определяет доказанный recovery checkpoint, owner/tuples/reconciliation и interruption/resume; Architecture и FTR-006.N01 согласованы. SC-T16 различает корректный takeover и произвольный/подменённый idle |
| F02 — EVENT без task требовал task-bound envelopes | C-016 разделяет COMMAND admission и read-only EVENT по действующей подписке/покрытому service scope. FTR-010 доставляет C-010 в FTR-008/012; Result Contract не требует фиктивного ValidationEnvelope. SC-T24 проверяет event без active task, terminal source, две подписки и запрещённый follow-up |
| F03 — local Commit требовал remote | Development §21 и FTR-015 output/process/recovery требуют только action/policy-specific remote facts. Local index/candidate/authority обязательны; MOD-S22 сохраняет positive local case и negative required-policy case |
| F04 — постоянный AGENTS поручал завершённую работу | Оставлен условный маршрут чтения для явно поставленной задачи; план — история подготовки, не повторная authorization |
| F05 — header плана остановился на R4 | Текущий статус ссылается на R7 и это исправление; исторические результаты не переписаны |

Author self-check исправления: PASS в пределах DOCUMENTATION_AUTHOR_SELF_CHECK.
Прослежены recovery checkpoint → прерывание → fresh resume и отказ при invalid
binding; taskless/terminal-source EVENT → read-only consumers, разрешённый
COMMAND follow-up и отказ без authority; local Commit и conditional remote policy.
SC-T16/24 и MOD-S22 остаются спецификациями будущих проверок, а не runtime PASS.

Проверки: изменены ровно шесть указанных файлов; остальные 377 сохранены.
Изменены четыре dossier (006/010/012/015), остальные 26, dispositions и placements
сохранены. Existing YAML schemas и 26 controller edges не менялись; исторические
разделы плана/brief сохранены. В полном текущем candidate проверены 331 локальная
ссылка/anchor, Markdown fences и 60 YAML blocks/frontmatter. Whitespace tracked
и обоих untracked документов — PASS; named input/consumer map согласована.

Предыдущие PASS остаются отчётами о своих scopes; independent validation,
runtime/native/host и module builds — NOT_RUN. Implementation/Git authorization
— NONE. Новых решений о scope/target/host или runtime launch не принято.
