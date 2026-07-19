Product Outcome

Назначение документа

Этот документ определяет основной пользовательский результат, который должна обеспечивать первая полезная версия AOS.

Он связывает:

primary user
→ core problem
→ observable product value

Документ описывает не внутреннее устройство системы, а изменение в состоянии пользователя после взаимодействия с продуктом.

Он не определяет:

* architecture;
* technology stack;
* implementation plan;
* полный feature list;
* Development Factory;
* Control Plane;
* registry;
* Runtime Enforcement;
* конкретную модель данных;
* конкретного AI provider.

Product Outcome должен оставаться проверяемым независимо от того, каким способом он будет реализован.

⸻

Исходное состояние пользователя

До использования AOS пользователь управляет AI-assisted development через набор слабо связанных инструментов и сообщений.

Он может иметь:

* repository;
* Git history;
* coding assistant;
* terminal;
* IDE;
* CI;
* documentation;
* issue tracker;
* chat history;
* локальные notes.

При этом у пользователя отсутствует единое понятное представление о текущем рабочем цикле.

Он не всегда может быстро установить:

* какая задача сейчас активна;
* откуда она появилась;
* какой scope был разрешён;
* какие assumptions сделал агент;
* что агент фактически изменил;
* что было проверено;
* какие проверки не запускались;
* где обнаружены проблемы;
* завершён ли текущий этап;
* требуется ли решение человека;
* какое действие должно быть выполнено следующим.

Пользователь вынужден восстанавливать это состояние вручную.

⸻

Желаемое состояние пользователя

После взаимодействия с AOS пользователь должен понимать текущую работу без необходимости перечитывать длинную историю сообщений или самостоятельно сопоставлять множество разрозненных artifacts.

В каждый момент ему должно быть ясно:

что происходит
→ почему это происходит
→ что разрешено
→ что уже сделано
→ что проверено
→ что неизвестно
→ что требует решения
→ какое одно действие следует дальше

Главный результат AOS — не количество выполненных агентом операций.

Главный результат — сохранение управляемости AI-assisted development.

⸻

Core Product Outcome

Основной Product Outcome первой версии:

Пользователь может провести одно изменение software product через ограниченный, последовательный и проверяемый рабочий цикл, сохраняя понимание scope, фактического состояния, результатов проверок, необходимых human decisions и следующего действия.

Этот outcome должен быть достижим без полной автоматизации процесса.

Первая версия может использовать:

* manual checkpoints;
* explicit prompts;
* repository files;
* human review;
* последовательные sessions;
* простые reports;
* минимальный chat-first interface.

Сложность внутреннего механизма не является частью Product Outcome.

⸻

Product Promise

AOS должен обеспечивать пользователю следующее обещание:

В любой момент вы можете понять, что сейчас происходит с задачей, что уже было сделано, что проверено, что требует вашего решения и какое одно действие следует выполнить дальше.

Это обещание должно сохраняться не только при успешном выполнении, но и при:

* FAIL;
* UNKNOWN;
* NOT_RUN;
* BLOCKED;
* scope conflict;
* изменении baseline;
* найденном противоречии;
* остановке workflow;
* переносе работы в новую session;
* передаче задачи другому agent.

Продукт не должен скрывать неопределённость ради ощущения progress.

⸻

Outcome, а не Feature List

Product Outcome не равен набору интерфейсных или технических возможностей.

Например, наличие следующих элементов само по себе не доказывает достижение outcome:

* dashboard;
* registry;
* database;
* workflow engine;
* agent router;
* schema;
* approval form;
* status label;
* CI pipeline;
* report generator;
* command palette;
* project memory;
* automation.

Эти элементы могут быть полезны только в том случае, если они улучшают observable state пользователя.

Каждая будущая feature должна оцениваться через вопрос:

Становится ли пользователю проще понять текущую задачу, фактический результат, нерешённые вопросы и следующее действие?

⸻

Observable User Outcomes

Product Outcome должен проявляться через наблюдаемое поведение системы и пользователя.

Пользователь понимает текущую задачу

Пользователь может определить:

* цель активной задачи;
* expected result;
* разрешённый scope;
* запрещённый scope;
* текущий stage;
* baseline;
* условия остановки.

Для этого не требуется восстанавливать контекст из нескольких chat sessions.

Пользователь различает планирование и выполнение

Пользователь видит разницу между:

идея
plan
Task Brief
execution authorization
execution

Наличие плана не воспринимается как разрешение на изменение repository.

Пользователь понимает фактический результат

После execution пользователь получает описание:

* что изменено;
* где изменено;
* что не изменялось;
* какие assumptions использовались;
* возник ли scope drift;
* были ли выполнены Git actions.

Claims должны быть связаны с наблюдаемыми artifacts или результатами проверок.

Пользователь различает execution и validation

Пользователь понимает:

* кто выполнял изменение;
* кто или что его проверяло;
* какие checks запускались;
* какие checks не запускались;
* какие findings обнаружены;
* исправлялись ли findings во время validation.

Validation не должна незаметно превращаться в новую execution session.

Пользователь видит uncertainty

Система явно показывает:

* UNKNOWN;
* NOT_RUN;
* BLOCKED;
* отсутствующие данные;
* недоступные проверки;
* непроверенные assumptions.

Неизвестное состояние не представляется как безопасное или успешное.

Пользователь видит границу human authority

AOS показывает, где требуется human decision.

Система не должна симулировать:

* approval;
* Risk Profile assignment;
* acceptance;
* authorization;
* destructive permission;
* commit permission;
* push permission;
* merge permission;
* release permission.

Пользователь получает одно следующее действие

После завершения этапа пользователь получает ровно одно основное действие.

Например:

REVIEW_TASK_BRIEF
AUTHORIZE_EXECUTION
RUN_VALIDATION
REVIEW_FINDINGS
AUTHORIZE_COMMIT
CREATE_CORRECTION_TASK
STOP

Система может сохранять дополнительные findings и context, но не должна превращать завершение этапа в список равнозначных направлений.

Пользователь может продолжить работу в новой session

Новая session должна иметь возможность восстановить:

* активную задачу;
* последний завершённый stage;
* фактический результат;
* findings;
* unresolved decisions;
* одно следующее действие.

Chat history не должна быть единственным носителем рабочего состояния.

⸻

Product Outcome по этапам рабочего цикла

До начала задачи

Пользователь понимает:

* какую проблему он решает;
* какой outcome ожидает;
* почему задача ограничена именно этим scope;
* какие действия пока запрещены.

После planning

Пользователь имеет bounded Task Brief.

При этом:

Plan output ≠ Task Brief.
Task Brief ≠ approval.
Task Brief ≠ execution authorization.

После execution

Пользователь понимает:

* что фактически изменено;
* соответствует ли изменение scope;
* завершился ли execution stage;
* какие проверки ещё необходимы.

Execution completion не означает technical acceptance.

После validation

Пользователь видит:

* PASS;
* FAIL;
* UNKNOWN;
* NOT_RUN;
* BLOCKED;
* findings;
* границы проверки.

При этом:

PASS ≠ approval.
Evidence ≠ approval.
CI PASS ≠ approval.

После human review

Пользователь принимает решение на основании:

* исходной цели;
* фактического diff;
* validation results;
* findings;
* unresolved unknowns;
* risk context.

Система не принимает это решение за него.

После Git decision

Пользователь отдельно решает, выполнять ли:

* commit;
* push;
* merge;
* release.

Эти действия не должны объединяться в одно implicit разрешение.

После завершения цикла

Пользователь знает:

* завершён ли текущий цикл;
* что стало новым factual state;
* остались ли незакрытые findings;
* какое одно действие следует дальше.

⸻

Outcome при успешном выполнении

Успешный цикл не означает, что система показала как можно больше PASS.

Успешный цикл означает, что:

* задача была ограничена;
* scope не расширился;
* разрешённое изменение выполнено;
* результат описан;
* проверки выполнены в заявленной границе;
* unknowns не скрыты;
* human decision не симулирован;
* следующее действие понятно;
* workflow остановился в определённой точке.

Даже при техническом PASS продукт не должен заявлять acceptance без решения человека.

⸻

Outcome при неуспешном выполнении

AOS должен сохранять полезность даже тогда, когда задача не завершена успешно.

При FAIL, BLOCKED или blocking finding пользователь должен получить:

* точное описание проблемы;
* stage, на котором она возникла;
* затронутую boundary;
* факты, подтверждающие finding;
* действия, которые не были выполнены;
* состояние repository;
* одно следующее действие;
* явную остановку workflow.

Неуспешный результат не должен запускать:

* automatic retry;
* silent correction;
* scope expansion;
* следующий stage;
* destructive recovery;
* изменение architecture.

Понятная остановка является полезным Product Outcome.

⸻

Outcome при Unknown

UNKNOWN является допустимым и честным состоянием.

Если система не может подтвердить факт, она должна показать:

UNKNOWN

а не:

OK
LIKELY_PASS
ASSUMED_SAFE
APPROVED

Пользователь должен понимать:

* какой именно факт неизвестен;
* почему он неизвестен;
* влияет ли это на текущую boundary;
* блокирует ли это продолжение;
* какое действие требуется для разрешения unknown.

AOS не должен пытаться устранять все неизвестные состояния глобально.

Fail-closed применяется только к затронутой boundary.

⸻

Outcome при Scope Conflict

Если в ходе работы обнаружено, что требуемое изменение выходит за разрешённый scope, AOS должен:

1. остановить текущий stage;
2. зафиксировать scope conflict;
3. не выполнять расширенное изменение;
4. сохранить уже известные факты;
5. сформировать одно следующее действие.

Например:

REVISE_TASK_BRIEF

или:

CREATE_SEPARATE_TASK

Scope expansion не должна происходить автоматически даже тогда, когда агент считает её технически полезной.

⸻

Outcome при Blocking Finding

На первом blocking finding текущий stage должен завершиться report.

Report должен объяснять:

* какой finding обнаружен;
* почему он blocking;
* что было проверено;
* что не проверялось;
* какие artifacts затронуты;
* что не было изменено после finding;
* какое одно действие требуется дальше.

После report система останавливается.

Следующий этап не запускается автоматически.

⸻

Outcome при Session Handoff

Session Handoff должен позволить продолжить работу без пересказа всей истории.

Минимально он должен сохранять:

* project;
* repository;
* branch;
* baseline;
* active task;
* task scope;
* completed stage;
* result;
* validation state;
* findings;
* unknowns;
* Git state;
* human decisions;
* pending human decisions;
* next required action.

Handoff не должен:

* объявлять approval;
* изменять lifecycle;
* расширять authority;
* разрешать execution;
* заменять repository state.

⸻

Outcome для Non-Programmer User

AOS должен снижать зависимость пользователя от глубоких знаний engineering tooling.

Это не означает скрытие технических фактов.

Система должна представлять их в форме, позволяющей понять:

* что изменено;
* почему это важно;
* какие риски существуют;
* что проверено;
* что не проверено;
* какое решение требуется.

Пользователь не обязан интерпретировать необработанный терминальный вывод, чтобы понять состояние задачи.

При этом AOS не должен упрощать информацию до ложных claims.

⸻

Outcome для Technical User

Технически опытный пользователь должен иметь возможность получить более подробный контекст:

* exact files;
* commands;
* exit codes;
* diffs;
* test names;
* baseline identifiers;
* validation boundaries;
* dependency changes;
* Git state;
* Evidence references.

Progressive disclosure должен позволять сочетать:

* краткий operational summary;
* подробные technical details.

Основной Product Outcome остаётся тем же: понимание текущего состояния и следующего действия.

⸻

Минимальный полезный Product Outcome

Первая полезная версия AOS не обязана управлять всем жизненным циклом разработки.

Минимально она должна позволять пройти один реальный bounded cycle:

user intent
→ bounded task
→ execution decision
→ controlled change
→ execution report
→ independent validation
→ validation report
→ human review
→ one next action
→ stop

Во время этого цикла пользователь должен иметь возможность ответить на пять вопросов:

1. Что сейчас происходит?
2. Что уже сделано?
3. Что проверено?
4. Что требует моего решения?
5. Какое одно действие следует дальше?

Если первая версия не обеспечивает эти ответы, дополнительная automation не должна считаться приоритетом.

⸻

Product Outcome не требует полной автономности

Полезность AOS не зависит от полной автономности.

На раннем этапе допустимы:

* ручное создание Task Brief;
* ручной запуск agent sessions;
* ручной запуск checks;
* ручное чтение reports;
* ручное принятие решений;
* ручные Git actions;
* ручной session handoff.

Automation должна появляться только там, где manual cycles показывают:

* повторяемость;
* устойчивые contracts;
* низкую неоднозначность;
* понятную границу authority;
* измеримую экономию усилий;
* отсутствие чрезмерного риска.

⸻

Product Outcome не требует Control Plane

Первая версия не нуждается в отдельном Control Plane, если основной outcome можно обеспечить через:

* repository-first state;
* bounded Markdown artifacts;
* explicit prompts;
* stage separation;
* manual checkpoints;
* simple validation;
* human review.

Control Plane становится оправданным только после подтверждения, что существующий способ:

* не масштабируется;
* создаёт устойчивые ошибки;
* не обеспечивает необходимую consistency;
* мешает реальным пользовательским сценариям.

Внутренняя инфраструктура не должна становиться prerequisite product value.

⸻

Product Outcome не требует Registry

Global registry не является обязательным для первого полезного цикла.

На раннем этапе достаточно явных источников истины для ограниченного набора фактов:

* task definition;
* repository state;
* stage result;
* validation result;
* pending decision;
* next action.

Registry может появиться позднее, если manual workflow докажет необходимость:

* cross-session queries;
* multi-project state;
* relationship tracking;
* lifecycle automation;
* integrity enforcement.

Наличие registry само по себе не является Product Outcome.

⸻

Product Outcome и Human Authority

AOS должен усиливать human authority, а не заменять её.

Система должна помогать человеку:

* увидеть необходимые решения;
* получить достаточный контекст;
* различить факты и claims;
* оценить unknowns;
* остановить workflow;
* ограничить scope;
* отдельно разрешать рискованные действия.

Система не должна:

* самостоятельно назначать Risk Profile;
* выдавать Evidence за approval;
* интерпретировать silence как acceptance;
* автоматически продолжать workflow;
* объединять несколько Git authorizations;
* скрывать unresolved human decision.

При отсутствии обязательного human decision состояние должно быть:

HUMAN_REVIEW_REQUIRED

или:

BLOCKED

⸻

Product Outcome и Source of Truth

Пользователь должен понимать, где находится authoritative state для каждого класса фактов.

Например:

* repository и Git — фактическое состояние файлов и history;
* Task Brief — разрешённые границы задачи;
* Stage Report — результат конкретного этапа;
* Validation Report — результат конкретной проверки;
* human record — принятое человеком решение.

Не должно существовать нескольких конкурирующих Source of Truth для одного и того же факта без явного правила приоритета.

Chat response не должен автоматически становиться authoritative project state.

⸻

Product Outcome и Product Runtime

Product Runtime должен воплощать Product Outcome в пользовательском взаимодействии.

Он должен помогать пользователю:

* начать bounded cycle;
* увидеть current state;
* получить result summary;
* открыть details;
* увидеть findings;
* принять human decision;
* получить next action;
* остановить или продолжить работу.

Product Runtime не должен начинаться с реализации всей Development Factory.

Сначала необходимо доказать один пользовательский outcome через один vertical slice.

⸻

Product Outcome и Development Factory

Development Factory обслуживает создание и развитие AOS.

Она может включать:

* planning workflows;
* agent roles;
* validation tooling;
* project memory;
* report generation;
* automation;
* repository controls.

Но пользовательский Product Outcome не должен зависеть от полной готовности Development Factory.

В противном случае проект снова попадёт в циклическую зависимость:

продукт требует factory
→ factory требует control
→ control требует Governance
→ Governance требует automation
→ product value откладывается

Первая версия должна использовать минимальные строительные леса, достаточные для создания и проверки Product Runtime.

⸻

Product Outcome и Metrics

На раннем этапе измерение должно быть ориентировано на observable user value.

Потенциальные признаки достижения outcome:

* пользователь может правильно назвать active task;
* пользователь понимает текущий stage;
* пользователь различает executed и validated;
* пользователь видит UNKNOWN и NOT_RUN;
* пользователь понимает, где требуется human decision;
* пользователь может продолжить работу в новой session;
* пользователь получает одно следующее действие;
* число scope corrections уменьшается;
* число repair loops уменьшается;
* время восстановления контекста сокращается;
* пользователь реже перечитывает длинную chat history;
* пользователь может объяснить фактическое состояние проекта.

Эти признаки являются кандидатами для последующей проверки, а не уже подтверждёнными metrics.

⸻

Anti-Outcomes

AOS не достигает Product Outcome, если пользователь получает:

Больше документов, но не больше понимания

Documentation должна сокращать неопределённость.

Если документы создают дополнительную topology, lifecycle и terminology без улучшения рабочего цикла, это является anti-outcome.

Больше automation, но меньше контроля

Automation, которая скрывает:

* assumptions;
* failures;
* decisions;
* scope expansion;
* skipped checks,

ухудшает основной outcome.

Больше статусов, но меньше фактов

Status labels не должны заменять:

* observed result;
* validation Evidence;
* human decision;
* exact next action.

Больше agents, но размытая ответственность

Multi-agent workflow не должен использоваться, если невозможно определить:

* кто выполнял stage;
* кто проверял;
* какой scope использовался;
* где завершился каждый запуск.

Постоянный recovery вместо product progress

Если пользователь регулярно восстанавливает состояние control system, а не развивает продукт, Product Outcome не достигнут.

Иллюзия автономности

Система не должна создавать видимость самостоятельного управления проектом, если реальные decisions и boundaries не определены.

⸻

Acceptance Direction

Product Outcome может считаться подтверждённым только после наблюдения реального пользовательского цикла.

Необходимы как минимум:

* реальная bounded task;
* реальное изменение;
* execution result;
* независимая validation;
* human review;
* session handoff;
* next action;
* наблюдение за тем, понял ли пользователь состояние.

Documentation review недостаточно для подтверждения Product Outcome.

Skeleton недостаточно.

Implementation claim недостаточно.

CI PASS недостаточно.

⸻

Основные Product Assumptions

Product Outcome опирается на следующие гипотезы:

1. Пользователь испытывает существенную проблему сохранения контекста и контроля.
2. Эта проблема возникает даже при использовании качественного coding assistant.
3. Явное разделение stages повышает понимание.
4. Bounded scope уменьшает scope drift.
5. Independent validation повышает доверие.
6. Явное отображение unknowns полезнее optimistic status.
7. One next action уменьшает cognitive overload.
8. Repository-first state позволяет уменьшить зависимость от chat history.
9. Manual checkpoints приемлемы для первой версии.
10. Product value можно доказать до появления сложной automation.

Эти assumptions должны проверяться, а не превращаться в безусловные architectural requirements.

⸻

Product Outcome Statement

Полная формулировка:

AOS помогает человеку управлять AI-assisted development как последовательностью ограниченных и проверяемых этапов. После каждого этапа пользователь понимает фактическое состояние задачи, границы выполненной работы, результаты проверок, нерешённые вопросы, необходимые human decisions и одно следующее действие.

Сокращённая формулировка:

AOS сохраняет понимание и human control во время AI-assisted development.

⸻

Outcome Formula

clear intent
+
bounded scope
+
factual execution result
+
independent validation
+
visible unknowns
+
explicit human authority
+
one next action
=
controlled product progress

Ни один отдельный элемент не является достаточным самостоятельно.

⸻

Проверочный вопрос для дальнейшего проектирования

Каждый следующий Product artifact, contract или feature должен отвечать на вопрос:

Как именно это изменение помогает пользователю понять текущее состояние, сохранить контроль и выполнить одно следующее действие?

Если ответ нельзя выразить через observable user behavior, решение не должно становиться обязательной частью первого Product Runtime vertical slice.

⸻

Краткое резюме

Исходное состояние

Пользователь управляет AI-assisted development через разрозненные инструменты и не имеет устойчивого понимания текущего workflow.

Желаемое состояние

Пользователь в любой момент понимает:

что происходит
что сделано
что проверено
что неизвестно
что требует решения
что делать дальше

Основной Product Outcome

Один реальный change проходит через bounded, observable и проверяемый cycle без потери human authority.

Минимальное доказательство

Успешно проведённый manual vertical slice с реальной задачей, independent validation, human review, session handoff и одним next action.

Главная граница

AOS должен сначала обеспечить пользовательский outcome.

Development Factory, Governance, automation, registry и Runtime Enforcement добавляются только после доказанной необходимости.