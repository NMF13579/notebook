First Product Vertical Slice

Назначение документа

Этот документ определяет первый сквозной пользовательский сценарий Product Runtime, через который должна быть проверена основная ценность AOS.

First Product Vertical Slice должен связать в одном ограниченном цикле:

user intent
→ bounded task
→ explicit human decision
→ controlled execution
→ factual result
→ independent validation
→ human review
→ one next action
→ stop

Документ описывает:

* пользовательскую цель vertical slice;
* начальные и конечные условия;
* основные этапы взаимодействия;
* минимальное observable behavior;
* состояния и переходы;
* границы human authority;
* допустимую ручную работу;
* исключённые возможности;
* направление acceptance.

Документ не определяет:

* architecture;
* technology stack;
* database;
* API design;
* UI framework;
* agent framework;
* implementation plan;
* repository layout runtime-компонентов;
* production deployment;
* полный Product Runtime.

First Vertical Slice является product contract direction, а не утверждением о наличии implementation.

⸻

Почему нужен Vertical Slice

Первую версию AOS нельзя проверять только через:

* documentation;
* schemas;
* isolated utilities;
* agent prompts;
* reports;
* validation scripts;
* внутренние control mechanisms.

Такие artifacts могут быть необходимы, но они не доказывают пользовательскую ценность.

Первый vertical slice должен позволить реальному пользователю пройти сквозной цикл от намерения до понятного результата.

Главный проверяемый вопрос:

Может ли пользователь выполнить одно ограниченное изменение software product с помощью AI agent и после каждого этапа понимать состояние задачи, факты, unknowns, необходимые решения и одно следующее действие?

⸻

Цель Vertical Slice

Primary user должен иметь возможность передать AOS одно намерение, превратить его в bounded task и провести через контролируемый рабочий цикл.

В конце цикла пользователь должен понимать:

* была ли задача сформулирована достаточно точно;
* какой scope был разрешён;
* разрешал ли он execution;
* что фактически изменено;
* соответствовал ли результат scope;
* какие проверки были выполнены;
* что осталось UNKNOWN или NOT_RUN;
* какие findings обнаружены;
* требуется ли correction;
* разрешены ли дальнейшие Git actions;
* какое одно действие следует дальше.

Vertical slice должен быть полезен даже тогда, когда execution или validation завершились неуспешно.

⸻

Основной пользовательский сценарий

Пользователь приходит с намерением:

Измени ограниченную часть моего software project и покажи мне, что произошло и что делать дальше.

AOS помогает преобразовать это намерение в последовательный цикл:

1. Capture Intent
2. Establish Context
3. Bound the Task
4. Request Human Execution Decision
5. Execute One Bounded Change
6. Report Execution Facts
7. Validate Independently
8. Present Review Package
9. Record Human Direction
10. Show One Next Action
11. Stop

В рамках первого vertical slice выполняется только одна active task.

⸻

Product Boundary Vertical Slice

First Vertical Slice управляет не всем software development lifecycle, а одним ограниченным change cycle.

Внутри slice находятся:

* пользовательское намерение;
* active project context;
* bounded Task Brief;
* explicit execution decision;
* один execution stage;
* один execution result;
* один independent validation stage;
* один validation result;
* один human review point;
* одно следующее действие;
* явная остановка.

За пределами slice находятся:

* автоматическое создание roadmap;
* управление несколькими задачами;
* полный backlog;
* multi-project operation;
* autonomous retry loops;
* automatic correction;
* automatic Git mutations;
* merge orchestration;
* release orchestration;
* production monitoring;
* organization-wide Governance.

⸻

Primary User Story

Как человек, управляющий software project с помощью AI agents, я хочу провести одно изменение через ограниченный и проверяемый рабочий цикл, чтобы после каждого этапа понимать фактическое состояние задачи и сохранять право принимать все обязательные решения.

⸻

Starting Condition

Vertical slice начинается, когда пользователь имеет:

* существующий software project или минимальный test project;
* доступный repository;
* сформулированное намерение;
* возможность принимать human decisions;
* AI agent или другой исполнитель;
* средство запуска разрешённых checks.

Пользователь не обязан заранее иметь:

* полное техническое задание;
* готовый Task Brief;
* formal Governance;
* registry;
* Control Plane;
* автоматическую project memory;
* настроенную multi-agent infrastructure;
* production CI.

AOS должен помочь определить, достаточно ли исходного контекста для формирования bounded task.

⸻

Completion Condition

Vertical slice завершается, когда выполнено одно из условий:

Normal Completion

* execution stage завершён;
* Execution Report сформирован;
* independent validation завершена;
* Validation Report сформирован;
* human review point достигнут;
* одно следующее действие определено;
* workflow остановлен.

Controlled Block

* обнаружен blocking finding;
* сформирован соответствующий report;
* запрещённые дальнейшие действия не выполнялись;
* одно следующее действие определено;
* workflow остановлен.

Human Decision Required

* требуется обязательное human decision;
* решение отсутствует;
* состояние обозначено как HUMAN_REVIEW_REQUIRED или BLOCKED;
* одно следующее действие определено;
* workflow остановлен.

Scope Conflict

* необходимое действие выходит за allowed scope;
* scope автоматически не расширяется;
* conflict зафиксирован;
* одно следующее действие определено;
* workflow остановлен.

Vertical slice не обязан завершаться техническим PASS, чтобы быть корректно завершённым как workflow.

⸻

Этап 1 — Capture Intent

Цель

Получить исходное пользовательское намерение без преждевременного перехода к implementation.

Примеры намерений:

* исправить конкретную ошибку;
* изменить наблюдаемое поведение;
* добавить небольшую возможность;
* обновить один документ;
* провести bounded refactoring;
* проверить определённое предположение.

Observable Behavior

AOS должен показать краткое понимание:

* чего пользователь хочет достичь;
* какой объект затронут;
* какой результат ожидается;
* какие существенные детали пока неизвестны.

AOS не должен автоматически интерпретировать intent как execution authorization.

Product Rule

Intent ≠ Task Brief.
Intent ≠ approval.
Intent ≠ execution authorization.

⸻

Этап 2 — Establish Context

Цель

Определить минимальный factual context, необходимый для безопасного ограничения задачи.

Контекст может включать:

* project;
* repository;
* branch;
* baseline;
* target artifact;
* existing working tree state;
* relevant product contract;
* known constraints;
* доступность validation.

Observable Behavior

Пользователь должен видеть:

* какие факты известны;
* откуда они получены;
* какие факты остаются неизвестными;
* влияет ли unknown на возможность продолжения.

AOS не должен подменять отсутствующий factual state предположением без явного обозначения.

Допустимые состояния

KNOWN
UNKNOWN
CONFLICTING
NOT_APPLICABLE

Если необходимый context отсутствует, vertical slice должен остановиться на bounded planning или preflight boundary.

⸻

Этап 3 — Bound the Task

Цель

Преобразовать intent в ограниченную задачу.

Результатом является Task Brief, содержащий минимум:

* цель;
* expected result;
* allowed scope;
* forbidden scope;
* repository;
* branch;
* baseline;
* requirements;
* validation;
* stop conditions;
* permissions;
* запрещённые Git actions.

Observable Behavior

Пользователь должен иметь возможность быстро ответить:

* что будет изменено;
* что не должно изменяться;
* как будет проверен результат;
* когда работа должна остановиться;
* какие действия требуют отдельного решения.

Product Rule

Plan output ≠ Task Brief.
Task Brief ≠ approval.
Task Brief ≠ execution authorization.

Task Brief описывает границы задачи, но не разрешает выполнение автоматически.

⸻

Этап 4 — Human Execution Decision

Цель

Получить явное решение человека о переходе к execution.

Возможные направления:

AUTHORIZE_EXECUTION
REVISE_TASK_BRIEF
REJECT_TASK
DEFER_TASK

Observable Behavior

AOS должен:

* показать краткое описание bounded task;
* показать существенные риски и unknowns;
* указать proposed Risk Profile, если это требуется;
* не назначать Risk Profile самостоятельно;
* не продолжать без обязательного решения;
* отличать подтверждение Task Brief от execution authorization.

Human Authority Boundary

Risk Profile назначает человек.

Агент может только:

* предложить Risk Profile;
* объяснить reasoning;
* показать последствия;
* остановиться до human assignment.

Human approval не может быть выведен из:

* предыдущего PASS;
* CI result;
* Evidence;
* отсутствия ответа;
* содержания Task Brief;
* поведения агента.

⸻

Этап 5 — Execute One Bounded Change

Цель

Выполнить ровно одно разрешённое изменение в пределах Task Brief.

Ограничения

Execution stage должен:

* иметь одного writer;
* использовать разрешённый workspace;
* соблюдать allowed scope;
* не изменять forbidden scope;
* не расширять задачу;
* не начинать validation как отдельный stage;
* не выполнять запрещённые Git actions;
* остановиться при blocking finding.

Observable Behavior

Пользователь должен видеть:

* что execution начался;
* какой scope активен;
* какой stage выполняется;
* завершился ли stage;
* возник ли blocking finding;
* происходили ли незапланированные действия.

Scope Conflict

Если исполнение требует изменения вне allowed scope:

STOP
→ REPORT_SCOPE_CONFLICT
→ ONE_NEXT_ACTION

Агент не должен автоматически изменять Task Brief.

⸻

Этап 6 — Execution Report

Цель

Зафиксировать фактический результат execution stage.

Execution Report должен описывать:

* задачу;
* выполненный stage;
* результат;
* изменённые artifacts;
* неизменённые важные boundaries;
* использованные assumptions;
* выполненные checks;
* findings;
* unknowns;
* Git actions;
* одно следующее действие.

Result States

Минимальные состояния:

PASS
FAIL
UNKNOWN
NOT_RUN
BLOCKED

Значение PASS на этом этапе:

Execution stage завершился в пределах собственной заявленной boundary.

Это не означает:

* independent validation PASS;
* human acceptance;
* commit authorization;
* push authorization;
* merge readiness;
* release readiness.

Product Rule

Execution completion ≠ validation.
Execution PASS ≠ approval.

⸻

Этап 7 — Independent Validation

Цель

Проверить результат execution без изменения artifact.

Validation выполняется отдельным stage и, по возможности, отдельной agent session.

Validation Boundary

Validation должна быть:

* read-only относительно проверяемого результата;
* ограничена заявленными checks;
* независима от execution reasoning;
* способна показать UNKNOWN и NOT_RUN;
* остановлена после blocking finding;
* завершена report.

Validation не должна:

* исправлять code или documentation;
* расширять scope;
* запускать следующий stage;
* повторяться автоматически;
* превращаться в новую execution session.

Observable Behavior

Пользователь должен видеть:

* что именно проверяется;
* какими checks;
* что фактически было запущено;
* какие checks завершились;
* что не запускалось;
* какие findings получены;
* какие boundaries не были проверены.

⸻

Этап 8 — Validation Report

Цель

Представить результаты проверки в форме, пригодной для human review.

Validation Report должен содержать:

* validation target;
* baseline или candidate identity;
* заявленную validation boundary;
* выполненные checks;
* результаты;
* findings;
* unknowns;
* skipped или NOT_RUN checks;
* blocking status;
* одно следующее действие.

Product Rules

PASS ≠ approval.
Evidence ≠ approval.
CI PASS ≠ approval.
UNKNOWN ≠ OK.
NOT_RUN ≠ PASS.

Validation Report не должен утверждать, что artifact принят человеком.

⸻

Этап 9 — Human Review

Цель

Предоставить человеку достаточный контекст для решения о дальнейшем направлении.

Пользователь должен получить компактное представление:

* исходной цели;
* allowed scope;
* фактических изменений;
* validation results;
* findings;
* unknowns;
* незапущенных checks;
* Git state;
* доступных human decisions.

Возможные Human Decisions

В зависимости от результата:

ACCEPT_RESULT
REQUEST_CORRECTION
REVISE_SCOPE
DEFER
REJECT_RESULT
AUTHORIZE_COMMIT
STOP

Не все решения должны быть доступны одновременно.

AOS должен показывать только решения, допустимые в текущем состоянии.

Correction Boundary

Если требуется correction:

* текущий validation stage остаётся неизменным;
* finding не исправляется внутри validation;
* создаётся отдельная bounded correction task;
* новое execution требует отдельного authorization.

⸻

Этап 10 — Git Decision

Цель

Явно отделить product result от изменения Git history или remote state.

Vertical slice может завершиться без commit.

Если пользователь рассматривает Git action, должны сохраняться границы:

Edit ≠ commit.
Commit ≠ push.
Push ≠ merge.
Merge ≠ release.

Каждое действие требует отдельного разрешения, когда оно входит в текущий product workflow.

First Slice Restriction

First Vertical Slice не должен автоматически выполнять:

* commit;
* push;
* merge;
* release;
* tag creation;
* force push;
* rebase;
* reset;
* clean;
* branch deletion.

Git automation не является prerequisite доказательства Product Outcome.

⸻

Этап 11 — One Next Action

Цель

После каждого завершённого stage показать одно основное действие.

Примеры:

COMPLETE_TASK_BRIEF
ASSIGN_RISK_PROFILE
AUTHORIZE_EXECUTION
RUN_EXECUTION
RUN_INDEPENDENT_VALIDATION
REVIEW_VALIDATION_FINDINGS
CREATE_CORRECTION_TASK
AUTHORIZE_COMMIT
STOP

Требования

Next action должен быть:

* конкретным;
* допустимым;
* связанным с текущим состоянием;
* не скрывающим обязательный human decision;
* единственным основным действием.

Дополнительные findings могут сохраняться в details, но не должны превращаться в несколько равнозначных следующих путей.

⸻

Этап 12 — Stop

Цель

Явно завершить текущий запуск и не переходить к следующему stage автоматически.

Остановка должна происходить:

* после завершения stage;
* после blocking finding;
* при отсутствии обязательного human decision;
* при scope conflict;
* при baseline conflict;
* при configuration mismatch;
* при запрещённом действии;
* при недоступной обязательной validation.

Product Rule

One run = one stage.
Stage complete → report → one next action → stop.

Stop является частью корректного Product Runtime behavior, а не признаком отказа системы.

⸻

Минимальный Product Runtime Surface

First Vertical Slice должен предоставлять пользователю минимальный набор действий.

Конкретный interface пока не фиксируется, но conceptually пользователь должен иметь возможность:

start
inspect
plan
review task
authorize
execute
validate
review result
see next action
stop
resume

Это может быть реализовано через:

* chat-first interaction;
* command-oriented interface;
* minimal terminal interface;
* простой web interface;
* сочетание интерфейсов.

Выбор interface является отдельным design decision.

⸻

Минимальная модель Current State

Vertical slice должен уметь показать компактное представление current state.

Минимальные классы фактов:

* active project;
* repository;
* branch;
* baseline;
* active task;
* current stage;
* stage result;
* allowed scope;
* findings;
* unknowns;
* pending human decision;
* Git state;
* next required action.

Это не требует глобального registry.

На первом этапе state может храниться в bounded repository artifacts и session handoff.

⸻

Primary State Sequence

Нормальная последовательность первого vertical slice:

NO_ACTIVE_TASK
→ INTENT_CAPTURED
→ CONTEXT_ESTABLISHED
→ TASK_BRIEF_PREPARED
→ HUMAN_EXECUTION_DECISION_REQUIRED
→ EXECUTION_AUTHORIZED
→ EXECUTION_COMPLETED
→ VALIDATION_REQUIRED
→ VALIDATION_COMPLETED
→ HUMAN_REVIEW_REQUIRED
→ NEXT_ACTION_RECORDED
→ STOPPED

Это conceptual sequence, а не требование создать формальную state machine.

Система не должна преждевременно строить сложный lifecycle engine только ради представления этих состояний.

⸻

Blocked State Sequence

Пример controlled block:

EXECUTION_AUTHORIZED
→ EXECUTION_STARTED
→ BLOCKING_FINDING
→ EXECUTION_REPORT_CREATED
→ HUMAN_REVIEW_REQUIRED
→ ONE_NEXT_ACTION
→ STOPPED

Пример scope conflict:

EXECUTION_STARTED
→ OUT_OF_SCOPE_CHANGE_REQUIRED
→ SCOPE_CONFLICT_REPORTED
→ REVISE_TASK_BRIEF
→ STOPPED

Пример unknown:

VALIDATION_STARTED
→ REQUIRED_FACT_UNAVAILABLE
→ UNKNOWN_BLOCKED
→ VALIDATION_REPORT_CREATED
→ RESOLVE_REQUIRED_FACT
→ STOPPED

⸻

Vertical Slice Example

Intent

Пользователь хочет изменить текст одного product document.

Bounded Task

Разрешено:

* изменить один конкретный Markdown file;
* сохранить headings;
* сохранить code fences;
* исправить определённую смысловую проблему.

Запрещено:

* менять соседние документы;
* обновлять metadata;
* изменять lifecycle;
* создавать commit;
* выполнять push;
* менять project structure.

Execution

Один agent переписывает документ целиком в пределах разрешённого scope.

Execution Report

Показывает:

* изменённый file;
* основные смысловые изменения;
* сохранённые boundaries;
* checks;
* unknowns;
* отсутствие Git actions.

Validation

Другая session проверяет:

* изменение только target file;
* сохранение Markdown structure;
* отсутствие YAML metadata;
* отсутствие Status;
* отсутствие approval claims;
* отсутствие scope expansion.

Human Review

Пользователь принимает или отклоняет содержательный результат.

Next Action

AUTHORIZE_COMMIT

или:

CREATE_CORRECTION_TASK

После этого текущий slice останавливается.

⸻

Более технический Example

Intent

Исправить одну воспроизводимую ошибку в существующей функции.

Bounded Task

Разрешено:

* изменить один production module;
* изменить один связанный test file.

Запрещено:

* менять public architecture;
* добавлять dependency;
* изменять unrelated code;
* выполнять commit или push.

Execution

Agent:

* воспроизводит ошибку в разрешённой boundary;
* вносит минимальное исправление;
* добавляет или корректирует test;
* формирует Execution Report;
* останавливается.

Validation

Independent validation:

* запускает target test;
* запускает релевантный regression set;
* проверяет diff;
* не изменяет files;
* формирует Validation Report;
* останавливается.

Human Review

Пользователь видит:

* что изменилось;
* какие tests прошли;
* какие tests не запускались;
* остались ли unknowns;
* какое действие требуется дальше.

⸻

Manual Before Automation

Первый vertical slice должен сначала быть проведён вручную.

Manual execution позволяет проверить:

* понятность stages;
* достаточность Task Brief;
* правильность stop conditions;
* полезность reports;
* необходимость human checkpoints;
* качество session handoff;
* достаточность one next action.

До добавления automation следует провести минимум два, предпочтительно три реальных manual cycles.

Automation не должна добавляться после единичного успешного случая.

⸻

Допустимые ручные элементы

На первом этапе допускается, что человек вручную:

* формулирует intent;
* уточняет Task Brief;
* назначает Risk Profile;
* разрешает execution;
* запускает agent session;
* запускает validation session;
* читает reports;
* принимает result;
* выполняет Git actions;
* переносит handoff.

Ручная операция не является дефектом vertical slice, если пользовательский outcome достигается.

⸻

Минимальная роль AOS

В первом vertical slice AOS должен выполнять пять ключевых функций:

1. Framing

Преобразовывать намерение в понятную bounded task.

2. Boundary Visibility

Показывать:

* allowed scope;
* forbidden scope;
* current stage;
* human authority boundaries.

3. Factual Reporting

Отделять:

* выполненные действия;
* claims;
* validation results;
* unknowns;
* human decisions.

4. Continuity

Сохранять минимальный контекст между stages и sessions.

5. Direction

После каждого этапа показывать одно следующее действие и останавливаться.

⸻

Что не должно быть частью First Vertical Slice

Полный Development Factory

Не требуется:

* автоматический planning pipeline;
* agent registry;
* multi-agent scheduling;
* automatic role assignment;
* autonomous correction;
* workflow compiler;
* global project memory.

Полный Governance

Не требуется:

* policy engine;
* complete lifecycle model;
* enterprise approvals;
* organization-wide Risk governance;
* automatic compliance checks.

Требуется только Minimal Safety Floor.

Control Plane

Не требуется отдельная control service, если workflow можно проверить через простые bounded artifacts.

Global Registry

Не требуется централизованный registry всех:

* tasks;
* artifacts;
* relationships;
* approvals;
* Evidence;
* lifecycle states.

Runtime Enforcement

Не требуется production enforcement layer до подтверждения contracts через manual cycles.

Rich User Interface

Не требуется:

* dashboard;
* visual workflow builder;
* advanced analytics;
* multi-pane IDE;
* mobile application.

Chat-first или minimal command interface достаточно для проверки Product Outcome.

Multi-Project Support

First Vertical Slice работает с:

* одним project;
* одним repository;
* одной active task;
* одним cycle.

⸻

Non-Goals

First Vertical Slice не должен:

* автоматически принимать product decisions;
* автоматически назначать Risk Profile;
* симулировать human approval;
* выполнять destructive operations;
* автоматически исправлять validation findings;
* автоматически повторять failed stage;
* автоматически начинать следующий stage;
* управлять несколькими writers;
* выполнять parallel write agents;
* скрывать UNKNOWN;
* преобразовывать NOT_RUN в PASS;
* считать CI PASS достаточным для acceptance;
* считать Evidence approval;
* выполнять commit, push, merge или release без отдельного разрешения;
* импортировать legacy architecture AOS-FARM;
* воспроизводить старую topology без product necessity.

⸻

Legacy Boundary

AOS-FARM может использоваться для извлечения:

* product intent;
* useful contracts;
* failure modes;
* lessons;
* negative examples;
* validated patterns.

Он не является authority для First Vertical Slice.

Нельзя автоматически переносить:

* старый Control Plane;
* registry;
* Governance topology;
* lifecycle complexity;
* recovery mechanisms;
* autonomous workflows;
* dependency structure;
* historical source hierarchy.

Каждый заимствованный принцип должен быть оправдан текущим Product Outcome.

⸻

Error Handling

Vertical slice должен обеспечивать понятное поведение при ошибках.

Execution Failure

Показать:

* что не получилось;
* где остановилось выполнение;
* что было изменено до failure;
* какие checks не запускались;
* какое одно действие требуется.

Validation Failure

Показать:

* какой check завершился FAIL;
* какие findings получены;
* какие проверки остались NOT_RUN;
* что validation не исправляла artifact;
* какое одно действие требуется.

Context Conflict

Показать:

* какие источники противоречат друг другу;
* какой факт нельзя определить;
* какую boundary это блокирует;
* какое одно действие требуется.

Baseline Change

Если baseline изменился:

* не продолжать автоматически;
* определить, остаётся ли Task Brief применимым;
* зафиксировать conflict;
* остановиться.

Configuration Mismatch

Если требуемая model, reasoning mode, sandbox или permission configuration недоступна:

BLOCKED

Automatic downgrade или sandbox expansion не допускаются.

⸻

Session Resume

Пользователь должен иметь возможность вернуться к vertical slice после остановки.

Resume должен восстановить:

* project identity;
* active task;
* Task Brief;
* текущий stage;
* последний завершённый report;
* findings;
* unknowns;
* pending human decision;
* Git state;
* next required action.

Resume не должен автоматически выполнять next action.

После восстановления пользователь сначала видит current state.

⸻

Progressive Disclosure

Информация должна быть доступна на двух уровнях.

Operational Summary

Кратко:

* current stage;
* result;
* blocking status;
* pending decision;
* next action.

Technical Details

По запросу:

* exact paths;
* commands;
* outputs;
* exit codes;
* diffs;
* test names;
* baseline identifiers;
* scope details;
* Evidence references.

Primary user не должен быть перегружен всеми technical details по умолчанию.

Технические факты при этом не должны скрываться.

⸻

Минимальные Product Contracts Vertical Slice

First Vertical Slice должен соблюдать следующие contracts.

Scope Contract

Изменения выполняются только в allowed scope.

Stage Contract

Один запуск выполняет один stage.

Reporting Contract

Каждый stage заканчивается factual report.

Validation Contract

Validation проверяет, но не исправляет.

Human Authority Contract

Обязательные human decisions не симулируются.

Unknown Contract

Неизвестное состояние показывается явно.

Git Boundary Contract

Git actions разделены и требуют соответствующего разрешения.

Next Action Contract

После завершения stage показывается одно следующее действие.

Stop Contract

После report текущий запуск останавливается.

Continuity Contract

Следующая session может восстановить минимальный factual context.

Эти contracts будут подробнее раскрыты в отдельном документе Product Contracts and Observable Behavior.

⸻

Acceptance Direction

First Vertical Slice считается содержательно определённым, если можно ответить:

1. Кто является primary user?
2. С каким намерением он входит в цикл?
3. Как intent превращается в bounded task?
4. Где требуется human execution decision?
5. Что именно выполняется?
6. Как фиксируется execution result?
7. Как проводится independent validation?
8. Как отображаются UNKNOWN и NOT_RUN?
9. Где происходит human review?
10. Как определяется одно следующее действие?
11. Где workflow обязан остановиться?
12. Что явно исключено из первой версии?

Это ещё не является acceptance работающего продукта.

⸻

Product Validation Direction

Работающий vertical slice должен проверяться через реальную задачу.

Необходимо наблюдать:

* понял ли пользователь Task Brief;
* заметил ли он boundaries;
* различил ли execution и validation;
* понял ли значение результатов;
* увидел ли unknowns;
* понял ли, где требуется его решение;
* смог ли продолжить работу после session handoff;
* получил ли одно следующее действие;
* снизилась ли необходимость восстанавливать контекст вручную.

Оценка только технических artifacts недостаточна.

⸻

Success Signals

Предварительные признаки успешного vertical slice:

* пользователь может описать active task без перечитывания chat history;
* пользователь знает allowed и forbidden scope;
* agent не расширяет scope;
* execution и validation проходят раздельно;
* validation не изменяет files;
* blocking finding приводит к report и stop;
* unknowns не скрываются;
* human decision появляется в правильной точке;
* следующий шаг однозначен;
* новая session восстанавливает context;
* пользователь понимает Git state;
* workflow не создаёт recovery loop.

Эти признаки являются гипотезами для последующей проверки.

⸻

Failure Signals

Vertical slice требует пересмотра, если:

* Task Brief сложнее самой пользовательской задачи;
* пользователь не понимает, что ему нужно решить;
* stages создают избыточную ceremony;
* один stage регулярно требует нескольких correction loops;
* reports дублируют chat и не помогают resume;
* one next action невозможно определить;
* unknowns блокируют весь workflow без необходимости;
* AOS требует Control Plane до первого полезного результата;
* пользователь тратит больше времени на управление AOS, чем на продукт;
* manual workflow не воспроизводится;
* разные agents интерпретируют contracts несовместимо;
* продукт снова превращается в Development Factory.

⸻

Кратчайшая реализация Product Value

Минимальный путь:

один пользователь
→ один repository
→ одна bounded task
→ один execution stage
→ один independent validation stage
→ один human review
→ один next action
→ stop

Всё, что не требуется для этого пути, не должно становиться prerequisite First Vertical Slice.

⸻

Vertical Slice Statement

Полная формулировка:

Первый Product Runtime vertical slice позволяет одному пользователю провести одну bounded software task от исходного намерения до independently validated result, сохраняя явные scope boundaries, human authority, truthful unknown handling, session continuity и одно следующее действие.

Сокращённая формулировка:

Один пользователь проводит одно изменение через понятный, ограниченный и проверяемый цикл.

⸻

Проверочный вопрос

Каждая возможность, предлагаемая для First Vertical Slice, должна отвечать:

Без этой возможности пользователь всё ещё может провести один bounded change cycle и понять результат?

Если ответ — да, возможность не должна становиться обязательной частью первой реализации.

⸻

Краткое резюме

Пользовательская цель

Провести одно изменение software product с помощью AI agent без потери понимания и контроля.

Начало

Пользователь формулирует intent.

Основной цикл

intent
→ context
→ Task Brief
→ human decision
→ execution
→ Execution Report
→ independent validation
→ Validation Report
→ human review
→ one next action
→ stop

Минимальная ценность

Пользователь понимает:

* что происходит;
* что разрешено;
* что сделано;
* что проверено;
* что неизвестно;
* что требует решения;
* что делать дальше.

Основные исключения

Не требуются:

* Control Plane;
* registry;
* full Governance;
* autonomous orchestration;
* Runtime Enforcement;
* automatic Git actions;
* rich UI;
* multi-project support.

Главная граница

First Vertical Slice должен доказать Product Outcome до построения расширенной Development Factory и control infrastructure.