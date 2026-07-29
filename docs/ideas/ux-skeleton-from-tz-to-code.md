Фича: создание UX skeleton проекта по техническому заданию и преобразование в код

1. Краткое описание

Фича создаёт в AOS-FARM управляемый путь от технического задания к проверяемой структуре пользовательского интерфейса, а затем — к ограниченной реализации кода.

Система получает техническое задание, Specification, архитектурные ограничения, роли и процессы проекта. На их основе она формирует Project UX Skeleton: структурированную модель пользовательских путей, страниц, элементов, состояний, переходов, прав доступа и связей с требованиями.

После этого:

1. AOS-FARM проверяет внутреннюю целостность UX skeleton.
2. Необязательная библиотека AOS-Solution-Patterns напоминает о вероятно пропущенных страницах, состояниях, элементах и failure paths.
3. При необходимости отдельный online research слой собирает актуальные рыночные примеры и формирует только advisory-кандидаты.
4. Человек принимает, отклоняет, изменяет или откладывает каждое существенное предложение.
5. AOS-FARM обновляет проектный UX skeleton и формирует human review package.
6. После отдельного human decision UX skeleton декомпозируется на вертикальные функциональные срезы.
7. Каждый срез превращается в отдельный scoped Task Brief.
8. Code Assembly Pipeline реализует только явно разрешённый срез.
9. Validation и Evidence связываются обратно с требованиями, страницами, состояниями и задачами.

Главная формула:

```text
Техническое задание
→ Specification
→ Architecture
→ Project UX Skeleton
→ проверка полноты
→ human decision
→ vertical slices
→ scoped Task Briefs
→ код
→ validation
→ Evidence
→ human review
```

Критические инварианты:

```text
UX skeleton ≠ implementation
UX skeleton ≠ validation
UX skeleton ≠ approval
Library suggestion ≠ project decision
Task candidate ≠ execution authorization
Validator PASS ≠ approval
Evidence ≠ approval
```

2. Проблема

В обычной агентной разработке пользователь чаще всего описывает только основной продуктовый слой:

1. назначение продукта;
2. главные роли;
3. основные действия;
4. несколько ключевых страниц;
5. ожидаемый результат.

При этом часто остаются неописанными:

1. вспомогательные страницы;
2. loading, empty, error и recovery states;
3. отмена и повтор операции;
4. потеря сессии;
5. запрет доступа;
6. частичный отказ;
7. поведение внешнего провайдера;
8. accessibility;
9. навигационные развилки;
10. связь между требованиями, интерфейсом, кодом и проверками.

Без формализованного UX skeleton агент вынужден угадывать структуру приложения непосредственно во время написания кода. Это создаёт:

1. скрытое расширение scope;
2. несогласованные страницы;
3. потерянные пользовательские пути;
4. реализацию только happy path;
5. дублирование компонентов и экранов;
6. слабую traceability;
7. позднее обнаружение архитектурных конфликтов;
8. сложные и дорогие переделки;
9. ложное ощущение готовности после генерации визуального skeleton;
10. риск перехода от документации к реализации без human checkpoint.

Фича должна перенести основные решения о структуре продукта на стадию документации, где их можно проверить и изменить до написания production-кода.

3. Цель

Создать в AOS-FARM систему, которая позволяет человеку описать продукт на естественном языке, а агенту — преобразовать описание в структурированный UX-контракт, проверить его полноту и подготовить безопасный переход к реализации.

Фича должна обеспечивать:

1. сбор UX-информации из технического задания;
2. выявление недостающих данных;
3. создание единого проектного UX skeleton;
4. понятное представление skeleton человеку;
5. проверку структуры и traceability;
6. advisory-проверку через дополнительную библиотеку;
7. фиксацию human decisions;
8. контролируемое обновление UX skeleton;
9. декомпозицию на вертикальные срезы;
10. преобразование срезов в scoped Task Briefs;
11. реализацию кода строго внутри Task Brief;
12. обратную проверку кода относительно UX и требований.

4. Не-цели

Фича не должна:

1. автоматически утверждать UX;
2. автоматически принимать рекомендации библиотеки;
3. заменять Specification;
4. заменять архитектуру;
5. заменять human product decision;
6. создавать визуальный дизайн бренда;
7. выбирать окончательные цвета, шрифты и стили;
8. делать Figma единственным Source of Truth;
9. генерировать всё приложение одной задачей;
10. разрешать Code Assembly Pipeline самостоятельно;
11. назначать Risk Profile;
12. выполнять commit, push, merge или release;
13. считать наличие skeleton доказательством реализации;
14. считать validator PASS разрешением на execution;
15. переносить управление агентом в AOS-Solution-Patterns;
16. делать AOS-FARM зависимым от доступности внешней библиотеки или сети.

5. Место фичи в AOS-FARM

Фича принадлежит AOS-FARM, потому что она управляет документацией, проектными решениями, task decomposition и переходом к реализации.

Она расширяет Documentation Assembly Pipeline:

```text
Idea
→ Project Brief
→ Specification
→ Architecture
→ UX Intake
→ UX Skeleton Assembly
→ UX Completeness Review
→ Human UX Review
→ Task Decomposition
→ Task Brief
```

Code Assembly Pipeline остаётся отдельным слоем:

```text
Task Brief
→ scoped code change
→ diff
→ checks
→ Execution Report
→ Evidence Report
→ Human Review
```

Фича не создаёт третий независимый управляющий pipeline. Она является частью документационного потока и создаёт входные данные для существующего Code Assembly Pipeline.

6. Граница ответственности

6.1 AOS-FARM владеет

AOS-FARM владеет:

1. UX Intake;
2. Project UX Skeleton;
3. canonical UX artifact проекта;
4. статусами UX-документа;
5. revision history;
6. human decisions;
7. human checkpoints;
8. Risk Profile request;
9. impact analysis;
10. task decomposition;
11. vertical slice selection;
12. Task Brief generation;
13. execution authorization boundary;
14. validation;
15. Evidence;
16. project lifecycle;
17. переходом к реализации.

6.2 AOS-Solution-Patterns владеет

Дополнительная библиотека может владеть только:

1. UX archetypes;
2. типовыми user flows;
3. page obligations;
4. element obligations;
5. state catalogue;
6. accessibility obligations;
7. failure paths;
8. связями Solution Pattern → UX recommendations;
9. собственным Registry;
10. собственным schemas;
11. собственным advisory review engine;
12. собственным provenance.

Библиотека только рекомендует. Она не изменяет проект.

```text
AOS-FARM управляет.
AOS-Solution-Patterns рекомендует.
```

6.3 Online UX Research Layer

Online research является дополнительным режимом AOS-FARM и может:

1. искать актуальные рыночные примеры;
2. сравнивать несколько сервисов;
3. выделять повторяющиеся решения;
4. создавать нормализованные UX candidates;
5. сохранять provenance и дату наблюдения.

Online research не может:

1. копировать чужой продукт как готовое решение;
2. автоматически включать найденный экран в проект;
3. считать популярность доказательством качества;
4. обходить лицензии и условия источника;
5. становиться обязательной зависимостью AOS-FARM;
6. выдавать approval.

7. Пользователи фичи

7.1 Product Owner или автор идеи

Описывает:

1. проблему;
2. пользователей;
3. процессы;
4. основные действия;
5. ожидаемые результаты;
6. ограничения;
7. приоритеты;
8. известные страницы.

Не обязан знать все UX-детали.

7.2 Domain Expert

Проверяет:

1. корректность предметного процесса;
2. полноту критичных сценариев;
3. терминологию;
4. ограничения домена;
5. опасные ошибки.

7.3 UX Architect Agent

Формирует DRAFT UX skeleton, но не принимает решения за человека.

7.4 Requirements Agent

Связывает UX-объекты с требованиями и acceptance criteria.

7.5 Reviewer

Проверяет:

1. соответствие ТЗ;
2. полноту user journeys;
3. роли и доступ;
4. states и failure paths;
5. traceability;
6. отсутствие scope expansion.

Reviewer не заменяет human approval.

7.6 Implementation Agent

Получает только scoped Task Brief одного вертикального среза и не может расширять scope.

8. Входные данные

Минимальные входы:

1. Project Brief;
2. техническое задание или Specification;
3. список ролей;
4. основные пользовательские процессы;
5. основные сущности данных;
6. архитектурные ограничения;
7. требования к доступу;
8. известные внешние интеграции;
9. известные риски;
10. явно исключённый scope.

Дополнительные входы:

1. существующий интерфейс;
2. screenshots;
3. Figma;
4. BPMN или process diagrams;
5. API contracts;
6. data model;
7. design system;
8. результаты пользовательских исследований;
9. competitor references;
10. выбранные Solution Patterns.

Если обязательный вход отсутствует, агент обязан зафиксировать:

```text
UNKNOWN
NOT_FOUND
HUMAN_REVIEW_REQUIRED
UNKNOWN_BLOCKED
```

в зависимости от влияния пропуска.

9. UX Intake

UX Intake — управляемый диалог, который собирает только достаточный объём информации и не заставляет пользователя заранее проектировать всё приложение.

9.1 Блок продукта

Система спрашивает:

1. Что делает продукт?
2. Какую проблему решает?
3. Какой главный результат получает пользователь?
4. Какие действия являются центральными?
5. Что точно не входит в первую версию?

9.2 Блок ролей

1. Какие типы пользователей существуют?
2. Чем отличаются их права?
3. Есть ли администратор?
4. Есть ли оператор, эксперт или внешний участник?
5. Может ли одна роль переключаться на другую?

9.3 Блок пользовательских процессов

Для каждого процесса:

1. кто его начинает;
2. что является trigger;
3. какие шаги проходит пользователь;
4. где он принимает решение;
5. что считается успешным завершением;
6. можно ли отменить процесс;
7. как восстановиться после ошибки;
8. какие внешние сервисы участвуют.

9.4 Блок данных

1. Какие данные пользователь видит?
2. Какие данные вводит?
3. Какие данные изменяет?
4. Какие данные запрещено показывать другим ролям?
5. Какие данные являются чувствительными?

9.5 Блок критичных действий

1. Есть ли удаление?
2. Есть ли платежи?
3. Есть ли изменение доступа?
4. Есть ли массовая отправка?
5. Есть ли необратимые действия?
6. Есть ли клинические или персональные данные?
7. Есть ли юридически значимые подтверждения?

9.6 Фиксация происхождения

Каждый факт должен иметь происхождение:

```yaml
source:
  source_type: HUMAN_INPUT | SPECIFICATION | ARCHITECTURE | INFERENCE | LIBRARY | ONLINE_RESEARCH
  source_reference:
  captured_at:
  confidence:
```

10. Project UX Skeleton

10.1 Назначение

Project UX Skeleton — структурированная модель пользовательского опыта конкретного проекта.

Он описывает не внешний стиль, а функциональную структуру:

1. кто пользуется системой;
2. чего хочет добиться;
3. какие пути проходит;
4. какие страницы открывает;
5. какие элементы использует;
6. какие состояния видит;
7. какие переходы доступны;
8. какие требования покрываются;
9. какие решения остаются неизвестными.

10.2 Canonical artifact

Предлагается один структурированный артефакт:

```text
ux-skeleton.yaml
```

Точный canonical path является архитектурным решением и должен быть принят человеком. До принятия пути документ остаётся PROPOSAL.

Производные представления:

```text
ux-overview.md
application-map.md
user-journeys.md
page-inventory.md
navigation-map.md
state-matrix.md
ux-coverage.md
```

Производные файлы не являются независимыми Source of Truth.

10.3 Минимальная структура

```yaml
document_id:
schema_version:
project_id:
revision:
status:

source_inputs: []
actors: []
capabilities: []
entities: []
journeys: []
pages: []
navigation: []
global_states: []
ux_decisions: []
unknowns: []
coverage: []

validation:
  status: NOT_RUN

authority:
  human_reviewed: false
  approved: false
  implementation_authorized: false
```

11. Модель UX-объектов

11.1 Actor

```yaml
actor_id:
title:
description:
goals: []
permissions: []
restrictions: []
entry_points: []
primary_journeys: []
source_requirements: []
```

11.2 User Journey

```yaml
journey_id:
title:
actor_id:
goal:
trigger:
preconditions: []
steps: []
decision_points: []
failure_paths: []
cancel_path:
recovery_path:
completion_state:
related_pages: []
source_requirements: []
```

11.3 Page

```yaml
page_id:
title:
purpose:
page_type:
actors: []
entry_points: []
exit_points: []
elements: []
states: []
permissions: []
data_dependencies: []
actions: []
related_solution_patterns: []
source_requirements: []
```

11.4 Element

```yaml
element_id:
element_type:
purpose:
required:
visible_to: []
enabled_when:
action:
data_source:
validation: []
states: []
accessibility: []
source_requirements: []
customizable: []
```

11.5 State

```yaml
state_id:
trigger:
visible_elements: []
disabled_elements: []
message_intent:
allowed_actions: []
recovery_action:
next_state:
```

11.6 Navigation Edge

```yaml
from_page:
action:
to_page:
actors: []
conditions: []
fallback:
```

12. Обязательные классы состояний

Система должна проверять применимость следующих состояний:

```text
initial
loading
empty
ready
submitting
submitted
success
validation_error
network_error
permission_denied
not_found
rate_limited
session_expired
partial_failure
external_service_unavailable
disabled
cancelled
```

Не все состояния обязательны для каждой страницы. Обязательность выводится из типа страницы, пользовательского пути, Solution Pattern и архитектуры.

Пример:

1. loading требуется странице, которая получает удалённые данные;
2. empty требуется списку, который может не содержать записей;
3. validation_error требуется форме;
4. permission_denied требуется защищённому маршруту;
5. partial_failure требуется массовой операции;
6. expired_token требуется восстановлению пароля;
7. external_service_unavailable требуется критичной внешней интеграции.

13. Классы свойств UX

13.1 Functional Invariants

Не могут быть удалены как визуальная правка:

1. обязательный пользовательский путь;
2. проверка доступа;
3. error recovery;
4. подтверждение опасной операции;
5. обязательные states;
6. accessibility;
7. security feedback;
8. сохранение результата операции.

13.2 Structural Decisions

Могут быть изменены человеком после impact analysis:

1. объединение страниц;
2. разделение длинной формы;
3. изменение порядка шагов;
4. перенос функции в другой раздел;
5. добавление промежуточного review step;
6. изменение навигационной модели.

13.3 Visual Customization

Может изменяться без изменения функционального контракта, если инварианты сохраняются:

1. цвета;
2. typography;
3. spacing;
4. illustration;
5. visual theme;
6. component library;
7. форма карточек;
8. расположение декоративных элементов.

14. Автоматическая сборка DRAFT

UX Skeleton Assembler должен:

1. прочитать структурированные входы;
2. создать stable IDs;
3. выделить actors;
4. выделить capabilities;
5. построить journeys;
6. построить application map;
7. создать page candidates;
8. добавить element candidates;
9. определить применимые states;
10. построить navigation edges;
11. связать объекты с требованиями;
12. зафиксировать unknowns;
13. создать DRAFT.

Assembler обязан разделять классы утверждений:

```text
FACT
INFERENCE
PROPOSAL
UNKNOWN
NOT_FOUND
```

Для INFERENCE должны храниться:

1. основание;
2. confidence;
3. affected objects;
4. необходимость human confirmation.

15. Проверка полноты локальными правилами

До внешней библиотеки AOS-FARM выполняет базовую внутреннюю проверку:

1. journey имеет начало и результат;
2. journey с ошибкой имеет recovery path;
3. page с удалёнными данными имеет loading/error;
4. list page имеет empty state;
5. form page имеет validation и submitting state;
6. protected page имеет permission handling;
7. destructive action имеет confirmation/cancel;
8. actor не получает неизвестное разрешение;
9. navigation не ведёт на отсутствующую страницу;
10. каждый существенный объект имеет requirement source;
11. отсутствуют duplicate IDs;
12. отсутствуют orphan pages и orphan journeys.

Это минимальный встроенный уровень AOS-FARM. Он должен работать без внешней библиотеки.

16. Проверка через AOS-Solution-Patterns

16.1 Назначение

Библиотека расширяет полноту и скорость, но не управляет проектом.

AOS-FARM формирует ограниченный запрос:

```yaml
request_id:
library_version:
selected_solution_patterns: []
actors: []
journeys: []
pages: []
known_constraints: {}
excluded_recommendations: []
```

16.2 Ответ библиотеки

```yaml
review_status: REVIEW_COMPLETE_WITH_SUGGESTIONS
suggestions:
  - suggestion_id:
    suggestion_type:
    target:
    proposed_item:
    reason:
    importance:
    source_solution_patterns: []
    source_ux_patterns: []
    decision_required: true

authority:
  project_updated: false
  approval_granted: false
  execution_authorized: false
```

16.3 Типы рекомендаций

```text
missing_page
missing_flow
missing_element
missing_state
missing_failure_path
missing_accessibility_obligation
possible_access_conflict
possible_navigation_gap
possible_duplicate_page
unresolved_condition
```

16.4 Importance

```text
REQUIRED_BY_SPECIFICATION
REQUIRED_FOR_SELECTED_PATTERN
CONDITIONAL
RECOMMENDED
OPTIONAL
POSSIBLE_CONFLICT
```

REQUIRED_FOR_SELECTED_PATTERN не является project approval. Это только утверждение библиотеки о собственном pattern contract.

17. Online UX Market Research

17.1 Когда применяется

Онлайн-поиск используется, если:

1. локальная библиотека не покрывает capability;
2. требуется актуальная рыночная практика;
3. существует несколько спорных UX-вариантов;
4. пользователь просит сравнить современные сервисы;
5. доменный процесс недостаточно понятен;
6. нужен reference для human decision.

17.2 Порядок

```text
UX gap
→ bounded research question
→ source policy check
→ online research
→ observation extraction
→ cross-product comparison
→ normalized candidate
→ human review
```

17.3 Классы результата

```text
OBSERVED
INFERRED
SYNTHESIZED
HUMAN_ACCEPTED
```

17.4 Ограничения

1. один продукт является example, а не pattern;
2. несколько независимых наблюдений могут стать pattern candidate;
3. популярность не равна качеству;
4. dark patterns не должны нормализоваться как рекомендации;
5. screenshot не должен автоматически сохраняться в durable library;
6. лицензия и условия источника должны быть известны;
7. при неизвестных условиях прямое копирование получает UNKNOWN_BLOCKED;
8. online result не входит в canonical UX skeleton без human decision.

18. Human Suggestion Review

AOS-FARM группирует предложения по пользовательским решениям, а не показывает человеку сотни низкоуровневых замечаний.

Пример:

```text
Вы указали вход по паролю.
В UX skeleton отсутствует восстановление доступа.

Предлагается:
1. страница запроса восстановления;
2. страница смены пароля;
3. expired-token state;
4. consumed-token state;
5. возврат к sign-in.

Основание:
SOL-IDENTITY-PASSWORD-AUTHENTICATION
SOL-IDENTITY-PASSWORD-RECOVERY

Решение:
1. ACCEPTED
2. REJECTED
3. MODIFIED
4. DEFERRED
5. NEEDS_CLARIFICATION
```

Каждое решение записывается в отдельный проектный decision artifact:

```yaml
decision_id:
suggestion_id:
result:
decided_by:
decided_at:
reason:
affected_requirements: []
affected_pages: []
```

Агент не может создавать фиктивный decided_by: human.

19. Статусы UX skeleton

Предлагаемая локальная статусная модель:

```text
DRAFT
INCOMPLETE
READY_FOR_REVIEW
HUMAN_REVIEW_REQUIRED
APPROVED
REJECTED
BLOCKED
UNKNOWN_BLOCKED
SUPERSEDED
```

Правила:

1. агент может создать DRAFT;
2. validator может определить INCOMPLETE;
3. AOS-FARM может подготовить READY_FOR_REVIEW;
4. только человек может установить APPROVED или REJECTED;
5. validator PASS не создаёт APPROVED;
6. approved UX skeleton не является общей execution authorization;
7. изменение approved skeleton создаёт новую revision;
8. существенное изменение требует повторного human review.

20. Validator

UX validator проверяет только формальные и логические свойства.

Минимальные checks:

1. schema validity;
2. уникальность IDs;
3. корректность references;
4. actors существуют;
5. pages существуют;
6. journey steps разрешимы;
7. navigation edges разрешимы;
8. states известны;
9. requirements linked;
10. provenance присутствует;
11. decisions имеют human witness;
12. library suggestion не помечена принятой без human decision;
13. NOT_RUN не превращён в PASS;
14. authority flags не сфальсифицированы;
15. canonical/generated drift отсутствует;
16. version binding библиотеки корректен.

Validator не оценивает субъективную красоту интерфейса.

```text
Validator PASS
→ structural contract satisfied
→ approval absent
```

21. Human UX Review Package

Перед переходом к task decomposition AOS-FARM формирует пакет:

1. краткое описание продукта;
2. роли;
3. application map;
4. user journeys;
5. page inventory;
6. page elements;
7. state matrix;
8. navigation map;
9. role-access matrix;
10. library suggestions;
11. online research candidates;
12. accepted/rejected/deferred decisions;
13. unknowns;
14. conflicts;
15. coverage report;
16. validator report;
17. revision diff.

Human review отвечает:

1. правильно ли отражены процессы;
2. все ли роли представлены;
3. не добавлен ли лишний scope;
4. покрыты ли критичные states;
5. корректны ли права доступа;
6. соответствует ли UX архитектуре;
7. какие решения нужно изменить;
8. можно ли утвердить UX structure для декомпозиции.

22. Переход от UX skeleton к коду

Прямой переход:

```text
APPROVED UX Skeleton
→ generate entire application
```

запрещён.

Правильный переход:

```text
APPROVED UX Skeleton
→ vertical slice candidates
→ dependency analysis
→ scoped Task Brief
→ Risk Profile assignment
→ execution authorization
→ Code Assembly Pipeline
```

23. Вертикальный срез

Вертикальный срез — минимальная целостная пользовательская возможность, проходящая через интерфейс, логику, данные и validation.

Он включает:

1. user goal;
2. journey или его законченный участок;
3. страницы;
4. элементы;
5. states;
6. backend behavior;
7. data contracts;
8. access rules;
9. failure paths;
10. validation obligations;
11. Evidence expectations.

Пример:

```text
Password Recovery
→ recovery request page
→ request API
→ message delivery
→ token validation
→ password reset page
→ session behavior
→ failure states
→ negative tests
```

24. Декомпозиция

Рекомендуемая иерархия:

```text
Feature
→ User Journey
→ Vertical Slice
→ Task Brief
→ Validation
→ Evidence
```

Не нужно заранее дробить весь продукт на сотни мелких tasks. Используется ленивая декомпозиция:

1. общий task graph фиксирует крупные вертикальные срезы;
2. детальный Task Brief создаётся перед выполнением конкретного среза;
3. дальние задачи не детализируются без необходимости;
4. после реализации выполняется обратная проверка Task → Slice → Journey → Requirement.

25. Task Brief для реализации

Каждый Task Brief должен содержать:

1. task identity;
2. parent vertical slice;
3. related requirement IDs;
4. related journey IDs;
5. related page IDs;
6. related state IDs;
7. allowed files;
8. forbidden files;
9. expected behavior;
10. non-goals;
11. validation;
12. Evidence requirements;
13. stop conditions;
14. Risk Profile assignment;
15. execution authorization status.

UX skeleton или task candidate не заменяет Task Brief.

26. Code Assembly

Implementation Agent должен:

1. прочитать Task Brief;
2. проверить repository, worktree, branch, HEAD и baseline;
3. реализовать только разрешённый vertical slice;
4. использовать UX IDs в traceability;
5. не менять соседние flows без permission;
6. реализовать required states;
7. реализовать access behavior;
8. добавить targeted validation;
9. сформировать diff;
10. создать Execution Report и Evidence Report;
11. остановиться перед следующей стадией.

Наличие не реализованных страниц в UX skeleton не является разрешением реализовать их в текущей Task.

27. Traceability

Система должна обеспечивать двустороннюю связь:

```text
Requirement
→ Actor
→ Journey
→ Page
→ Element
→ State
→ Vertical Slice
→ Task
→ Code
→ Validation
→ Evidence
```

И обратную проверку:

```text
Evidence
→ Validation
→ Code
→ Task
→ Vertical Slice
→ UX object
→ Requirement
```

Каждый объект должен иметь stable ID.

Пример:

```yaml
coverage:
  - requirement_id: REQ-AUTH-014
    actor_ids:
      - ACTOR-GUEST
    journey_ids:
      - JOURNEY-PASSWORD-RECOVERY
    page_ids:
      - PAGE-PASSWORD-RECOVERY
      - PAGE-PASSWORD-RESET
    element_ids:
      - EMAIL-FIELD
      - NEW-PASSWORD-FIELD
    state_ids:
      - SUBMITTED
      - EXPIRED-TOKEN
      - NETWORK-ERROR
    vertical_slice_ids:
      - SLICE-PASSWORD-RECOVERY
    task_ids: []
    validation_ids: []
    evidence_ids: []
```

Пустые task, validation и Evidence IDs на стадии документации являются допустимыми, но не должны обозначаться PASS.

28. Impact Analysis

Если после реализации меняется UX skeleton, AOS-FARM должен определить:

1. какие requirements изменены;
2. какие journeys затронуты;
3. какие pages изменены;
4. какие states добавлены или удалены;
5. какие vertical slices устарели;
6. какие Task Briefs требуют обновления;
7. какой код может быть несовместим;
8. какие tests устарели;
9. какая Evidence больше не подтверждает текущее состояние;
10. нужен ли повторный human review;
11. нужен ли новый Risk Profile assignment.

Визуальные изменения обычно имеют меньший impact. Изменение роли, доступа, обязательного процесса или protected invariant имеет повышенный impact.

29. Failure Modes

29.1 Недостаточное ТЗ

Симптом:

1. неясные роли;
2. отсутствует результат процесса;
3. не определены ошибки;
4. неизвестен доступ.

Поведение:

```text
HUMAN_REVIEW_REQUIRED
```

или:

```text
UNKNOWN_BLOCKED
```

29.2 Агент добавил scope

Симптом: появились страницы или функции без основания.

Поведение:

1. отметить как PROPOSAL;
2. не включать в canonical skeleton;
3. показать человеку;
4. запретить автоматическую декомпозицию предложения.

29.3 Библиотека недоступна

Поведение:

1. AOS-FARM продолжает базовую сборку;
2. library review получает NOT_RUN;
3. отсутствие библиотеки не считается PASS;
4. при критичной зависимости — UNKNOWN_BLOCKED.

29.4 Online source недоступен или лицензия неясна

Поведение:

1. исключить источник;
2. не копировать материал;
3. зафиксировать UNKNOWN;
4. продолжить по локальным данным, если это безопасно.

29.5 Library suggestion автоматически принято

Это дефект authority boundary.

Поведение:

```text
BLOCKED
```

до появления явного human decision.

29.6 Validator PASS интерпретирован как approval

Это false PASS.

Поведение:

```text
BLOCKED
```

29.7 Code generation вышла за Task Brief

Поведение:

1. прекратить execution;
2. сформировать scope violation report;
3. не продолжать автоматически;
4. запросить human review.

29.8 UX и архитектура конфликтуют

Пример: UX требует realtime, а архитектура допускает только batch processing.

Поведение:

1. зафиксировать conflict artifact;
2. указать affected decisions;
3. не выбирать сторону автоматически;
4. HUMAN_REVIEW_REQUIRED.

29.9 Generated views расходятся с canonical YAML

Побеждает canonical YAML. Производные документы должны быть пересобраны.

29.10 Approved skeleton изменён без новой revision

Это нарушение lifecycle и traceability.

Поведение:

```text
BLOCKED
```

30. Security, Privacy и Accessibility

UX skeleton должен позволять фиксировать:

1. trust boundaries;
2. роли и permissions;
3. sensitive data visibility;
4. confirmation опасных действий;
5. audit feedback;
6. session behavior;
7. privacy-preserving messages;
8. data retention notices;
9. keyboard behavior;
10. focus management;
11. error announcement;
12. отсутствие color-only meaning.

Для медицинских, финансовых, юридических или других высокорисковых систем UX review не заменяет domain review.

31. MVP

Первый MVP включает:

1. UX Intake schema;
2. UX Skeleton schema;
3. actors;
4. journeys;
5. pages;
6. elements;
7. states;
8. navigation;
9. provenance;
10. coverage;
11. deterministic assembler;
12. internal validator;
13. library request/report contract;
14. human decision artifact;
15. derived Markdown views;
16. vertical slice candidates;
17. Task Brief bridge;
18. один dogfood project.

MVP не включает:

1. Figma integration;
2. browser-based visual editor;
3. production code generation всего приложения;
4. online scraping;
5. автоматический design system;
6. автоматический approval;
7. runtime enforcement;
8. multi-repository orchestration;
9. полноценную visual regression platform.

32. Последующие версии

32.1 Версия 2

1. расширенная UX library integration;
2. state applicability rules;
3. access matrix validator;
4. impact analysis;
5. несколько dogfood projects;
6. visual diagrams;
7. change suggestions grouping.

32.2 Версия 3

1. online research adapters;
2. source policy registry;
3. market pattern comparison;
4. normalized research candidates;
5. license/provenance checks;
6. domain-specific UX packs.

32.3 Версия 4

1. Figma adapter;
2. design token adapter;
3. Storybook mapping;
4. visual state coverage;
5. code-to-skeleton drift checks;
6. stronger Runtime Enforcement.

33. Критерии приёмки фичи

Фича может быть принята человеком, если доказано:

1. из тестового ТЗ формируется воспроизводимый DRAFT UX skeleton;
2. все основные объекты имеют stable IDs;
3. объекты связаны с source requirements;
4. неизвестности не подменяются предположениями;
5. внутренний validator находит structural defects;
6. библиотека возвращает advisory suggestions;
7. suggestions не изменяют проект автоматически;
8. человек может принять, отклонить, изменить или отложить предложение;
9. решения человека сохраняются с provenance;
10. canonical skeleton получает новую revision;
11. формируется Human UX Review Package;
12. approved skeleton разбивается на vertical slices;
13. Task Brief ограничивает реализацию одного среза;
14. Code Assembly Pipeline не расширяет scope;
15. код связан с UX IDs;
16. validation проверяет required states;
17. Evidence связывается обратно с требованиями;
18. отсутствие библиотеки не ломает AOS-FARM;
19. validator PASS не выдаётся как approval;
20. commit/push/release не выполняются без отдельной authorization.

34. Dogfood-сценарии

34.1 Password Recovery

Проверить:

1. запрос восстановления;
2. нейтральный результат;
3. отправку сообщения;
4. reset page;
5. expired token;
6. consumed token;
7. network error;
8. rate limit;
9. возврат к sign-in;
10. negative validation.

34.2 CRUD Service

Проверить:

1. list;
2. empty;
3. search/filter;
4. detail;
5. create;
6. edit;
7. delete confirmation;
8. permission denied;
9. stale data;
10. not found.

34.3 Bulk Messaging

Проверить:

1. campaign list;
2. draft;
3. audience selection;
4. review page;
5. send confirmation;
6. progress;
7. partial failure;
8. stop/cancel;
9. results;
10. role access.

35. Метрики качества

Метрики являются наблюдением, а не approval.

Можно измерять:

1. долю requirements, связанных с UX objects;
2. долю journeys с failure/recovery paths;
3. долю страниц с применимыми states;
4. число orphan pages;
5. число unresolved unknowns;
6. число library suggestions;
7. долю accepted/rejected/deferred suggestions;
8. число scope violations при реализации;
9. число UX defects, найденных до кода;
10. число drift conflicts после реализации.

Нельзя утверждать универсальную точность или гарантированный процент успешной генерации кода без отдельного benchmark.

36. Authority и Risk

Этот документ является DRAFT и не меняет архитектуру AOS-FARM.

Будущая реализация затрагивает:

1. Documentation Assembly Pipeline;
2. architecture authority;
3. canonical artifact ownership;
4. validator behavior;
5. human decision boundary;
6. integration contract;
7. Task Brief generation;
8. переход к Code Assembly Pipeline.

Поэтому предлагаемый минимальный Risk Profile для архитектурного принятия и реализации:

```text
HIGH_RISK_PROTECTED
```

Risk Profile должен назначить человек.

Отдельно требуются:

1. architecture decision;
2. human acceptance feature contract;
3. execution authorization;
4. commit authorization;
5. push authorization;
6. merge authorization;
7. release authorization.

37. Открытые решения

До реализации человек должен определить:

1. canonical path ux-skeleton.yaml;
2. точное место фичи в /aos/;
3. schema versioning policy;
4. status integration с общим lifecycle;
5. формат human decision witness;
6. обязательность architecture input для простых проектов;
7. минимальный набор встроенных completeness rules;
8. границу между AOS-FARM rules и внешней UX library;
9. формат vertical slice candidate;
10. способ связывания кода с UX IDs;
11. первый dogfood project;
12. необходимость online research в MVP;
13. разрешённые источники для online research;
14. момент подключения Figma adapter;
15. правила изменения approved UX skeleton.

Пока решения не приняты, соответствующие пункты имеют статус:

```text
HUMAN_REVIEW_REQUIRED
```

38. Implementation Model

Предлагаемая компонентная модель:

```text
UX Intake Collector
→ Requirements Normalizer
→ UX Skeleton Assembler
→ Internal Completeness Validator
→ Library Review Adapter
→ Online Research Adapter (optional)
→ Suggestion Review Builder
→ Human Decision Recorder
→ Canonical Revision Manager
→ Derived View Generator
→ Coverage Builder
→ Vertical Slice Planner
→ Task Brief Generator
→ Code Assembly Pipeline
→ Validation/Evidence Linker
→ Drift and Impact Analyzer
```

Все управляющие компоненты находятся в AOS-FARM.

AOS-Solution-Patterns предоставляет только данные и advisory review result.

39. Финальное правило

Фича должна реализовать управляемую цепочку:

```text
Человек описывает продукт и процессы.
AOS-FARM создаёт DRAFT UX skeleton.
Библиотека и research помогают найти пропуски.
Человек принимает решения.
AOS-FARM фиксирует утверждённую структуру.
Структура преобразуется в вертикальные срезы.
Каждый срез получает отдельный Task Brief.
Код создаётся только внутри разрешённой задачи.
Validation и Evidence подтверждают результат.
Человек принимает итоговое решение.
```

Фича не является генератором случайных экранов. Она является specification-driven, human-controlled и traceable системой преобразования технического задания в UX-контракт и далее в ограниченную реализацию кода.

40. Источники и классы утверждений

40.1 FACT

На основании обязательных источников AOS-FARM:

1. Documentation Assembly Pipeline формирует документы и scope.
2. Code Assembly Pipeline работает только после появления scoped Task Brief.
3. Minimal Safety Floor действует всегда.
4. PASS, Evidence и CI PASS не являются approval.
5. Skeleton не является implementation, validation или approval.
6. Human approval нельзя симулировать.
7. Scope нельзя расширять без human permission.
8. Protected/canonical changes требуют human checkpoint.
9. Risk Profile назначается человеком.
10. Commit, push, merge и release имеют отдельные authorization boundaries.

40.2 PROPOSAL

В этом документе предложены:

1. отдельный UX Intake;
2. структура ux-skeleton.yaml;
3. локальная статусная модель UX;
4. компонентная модель фичи;
5. integration contract с UX library;
6. online research layer;
7. vertical slice bridge;
8. MVP и последовательность версий.

40.3 UNKNOWN

Не подтверждены:

1. canonical path;
2. окончательная schema;
3. точная lifecycle integration;
4. первая implementation branch;
5. первый dogfood project;
6. обязательность online research;
7. Figma integration boundary.

40.4 Human decision required

Документ может стать основанием для архитектурного решения только после отдельного human review и explicit acceptance.
