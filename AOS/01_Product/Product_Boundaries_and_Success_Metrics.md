# Product Boundaries and Success Metrics

Назначение документа

Этот документ определяет:

* границы первой версии AOS;
* обязательный initial scope;
* возможности и сценарии вне initial scope;
* критерии допустимого расширения продукта;
* признаки достижения Product Outcome;
* предварительные success metrics;
* failure signals;
* порядок проверки пользовательской ценности.

Документ объединяет два взаимосвязанных вопроса:

что первая версия должна и не должна делать
+
как определить, что она действительно полезна

Product Boundaries защищают проект от преждевременного расширения.

Success Metrics защищают проект от ситуации, в которой documentation, infrastructure или automation ошибочно принимаются за product value.

Документ не определяет:

* architecture;
* implementation plan;
* technology stack;
* database;
* API;
* UI framework;
* полный roadmap;
* production readiness;
* release criteria;
* enterprise Governance;
* конкретный analytics system.

Описанные metrics являются направлениями последующей проверки, а не уже подтверждёнными результатами.

⸻

Основная Product Boundary

Первая версия AOS должна доказать одну ограниченную продуктовую гипотезу:

Один пользователь может провести одно AI-assisted изменение software product через понятный, ограниченный и проверяемый workflow, сохраняя понимание текущего состояния, human authority и одно следующее действие.

Первая версия не должна доказывать:

* возможность полной автономной разработки;
* готовность масштабной Development Factory;
* зрелость полного Governance;
* возможность управления множеством projects;
* готовность enterprise platform;
* наличие production Runtime Enforcement.

Главная boundary первой версии:

one user
→ one project
→ one repository
→ one active task
→ one bounded cycle
→ one clear outcome

⸻

Product Boundary как средство сохранения фокуса

Product Boundary определяет не только то, что запрещено.

Она отделяет:

* необходимое для проверки Product Outcome;
* полезное, но отложенное;
* неизвестное;
* неподтверждённое;
* преждевременную infrastructure.

Любая новая возможность должна сначала отвечать на вопрос:

Без этой возможности пользователь всё ещё способен пройти First Product Vertical Slice?

Если ответ — да, возможность не должна автоматически становиться обязательной частью первой версии.

⸻

Initial Product Scope

Первая версия ориентирована на следующий контекст.

Один Primary User

Система обслуживает одного человека, который:

* формулирует intent;
* определяет желаемый outcome;
* рассматривает Task Brief;
* назначает Risk Profile, когда это требуется;
* разрешает execution;
* рассматривает validation result;
* принимает human decisions;
* отдельно разрешает Git actions.

Multi-user coordination не является prerequisite первого Product Outcome.

⸻

Один Software Project

First Product Runtime работает с одним выбранным software project.

Не требуется:

* portfolio management;
* cross-project planning;
* shared organizational state;
* multi-project dependency graph;
* централизованный project registry.

⸻

Один Repository

Первый vertical slice предполагает один repository как основной factual source для:

* files;
* current diff;
* branch;
* commits;
* working tree;
* baseline.

Multi-repository operation откладывается до появления подтверждённой необходимости.

⸻

Одна Active Task

В рамках первого workflow существует одна active bounded task.

Не требуется:

* parallel backlog execution;
* automatic prioritization;
* task scheduling;
* dependency resolution между множеством задач;
* parallel write agents.

⸻

Один Writer на Execution Stage

В одном execution stage существует один writer.

Другие agents или sessions могут:

* читать;
* анализировать;
* валидировать;
* проводить review.

Они не должны параллельно изменять тот же workspace.

⸻

Последовательные Stages

Первая версия поддерживает последовательность:

planning
→ human decision
→ execution
→ reporting
→ validation
→ human review
→ next action
→ stop

Stages не объединяются в один непрерывный autonomous run.

⸻

Chat-First Interaction

Первая версия может использовать chat как основной interaction surface.

Chat-first означает, что пользователь может:

* выразить intent;
* увидеть current state;
* рассмотреть Task Brief;
* принять human decision;
* получить result summary;
* открыть technical details;
* увидеть one next action;
* возобновить session.

Chat-first не означает, что весь authoritative state хранится только в chat history.

⸻

Repository-First Factual State

Repository и Git являются основным источником фактов о текущем technical state.

Они не являются источником:

* approval;
* acceptance;
* execution authorization;
* Risk Profile assignment;
* release authorization.

Для разных классов фактов должны использоваться разные Source of Truth.

⸻

Manual Human Checkpoints

Первая версия допускает и требует ручные решения человека в обязательных boundaries.

Human checkpoints могут включать:

* acceptance of Task Brief;
* Risk Profile assignment;
* execution authorization;
* review of findings;
* result acceptance;
* commit authorization;
* push authorization;
* merge authorization;
* release authorization.

Human approval cannot be simulated.

⸻

Manual Workflow Before Automation

Первый workflow должен быть проведён вручную минимум два, предпочтительно три раза.

Manual cycle должен подтвердить:

* понятность stages;
* достаточность Task Brief;
* полезность reports;
* корректность stop conditions;
* необходимость human checkpoints;
* session continuity;
* возможность определить one next action.

Automation не должна предшествовать пониманию процесса.

⸻

Minimal Durable Artifacts

Первая версия может опираться на небольшой набор durable artifacts:

* Task Brief;
* Execution Report;
* Validation Report;
* Human Decision Record, когда он требуется;
* Session Handoff;
* relevant Product Contracts.

Не требуется универсальный registry всех состояний и отношений.

⸻

Minimal Safety Floor

Первая версия обязана сохранять:

* human authority;
* bounded scope;
* protected boundary;
* destructive authorization;
* explicit unknown handling;
* stage separation;
* independent validation;
* one writer;
* Git action separation;
* one next action;
* explicit stop.

Полный Governance не является prerequisite.

⸻

Required Product Capabilities

Первая версия должна обеспечивать ровно те возможности, которые необходимы для First Product Vertical Slice.

Current State Visibility

Пользователь видит:

* active project;
* repository;
* branch;
* baseline;
* active task;
* current stage;
* last result;
* blocking status;
* pending decision;
* next required action.

⸻

Intent Capture

Пользователь может сформулировать intent естественным языком.

AOS отражает:

* понятый goal;
* предполагаемый target;
* expected outcome;
* существенные unknowns.

Intent не запускает execution автоматически.

⸻

Bounded Task Definition

Пользователь получает Task Brief с:

* goal;
* expected result;
* allowed scope;
* forbidden scope;
* requirements;
* validation;
* stop conditions;
* permissions.

⸻

Explicit Human Decision

AOS показывает, где требуется human decision, и останавливается при его отсутствии.

⸻

Controlled Execution

Execution выполняется:

* одним writer;
* в allowed scope;
* в одном stage;
* без автоматического scope expansion;
* без запрещённых Git actions.

⸻

Factual Reporting

После execution пользователь получает factual Execution Report.

⸻

Independent Validation

Validation:

* запускается отдельно;
* работает read-only;
* не исправляет artifact;
* показывает PASS, FAIL, UNKNOWN, NOT_RUN или BLOCKED.

⸻

Human Review

Пользователь получает достаточно фактов для решения.

AOS не принимает решение вместо него.

⸻

One Next Action

После каждого stage существует одно основное следующее действие.

⸻

Session Resume

Новая session может восстановить минимальный factual context без полного чтения chat history.

⸻

Capabilities Outside Initial Scope

Следующие возможности не являются частью обязательного initial scope.

Они могут рассматриваться позднее только после подтверждения необходимости.

⸻

Полная автономность

Первая версия не должна:

* самостоятельно выбирать product goals;
* создавать roadmap;
* принимать architecture decisions;
* выполнять бесконечный autonomous loop;
* автоматически переходить между stages;
* автоматически исправлять все findings;
* самостоятельно завершать project.

AOS не является полностью автономным AI Developer.

⸻

Полный Development Factory

Не требуются:

* distributed execution platform;
* orchestration engine;
* agent scheduler;
* task queue;
* workflow compiler;
* autonomous planning pipeline;
* automatic role allocation;
* full development conveyor.

Development Factory развивается только после доказательства Product Runtime value.

⸻

Control Plane

Отдельный Control Plane не является обязательным.

Если contracts можно проверить через:

* repository artifacts;
* explicit prompts;
* separate sessions;
* human checkpoints;
* simple checks,

создание отдельной control service откладывается.

⸻

Global Registry

Не требуется централизованный registry:

* tasks;
* artifacts;
* approvals;
* Evidence;
* decisions;
* relationships;
* lifecycle states;
* agents;
* projects.

Registry может стать полезным после появления:

* большого числа durable objects;
* cross-session queries;
* multi-project operation;
* integrity problems;
* необходимости lifecycle automation.

⸻

Runtime Enforcement

Первая версия не реализует полный enforcement layer.

Не требуются:

* policy engine;
* cryptographic authorization;
* execution package enforcement;
* global claim ceilings;
* distributed permission checks;
* production runtime guards.

Сначала Product Contracts должны быть подтверждены manual workflows.

⸻

Полный Governance

Первая версия не должна строить:

* полную approval hierarchy;
* organization-wide risk management;
* lifecycle engine;
* policy compiler;
* enterprise audit system;
* regulatory compliance automation.

Требуется только Minimal Safety Floor.

⸻

Автоматическое Approval

AOS никогда не должен автоматически:

* принимать результат;
* назначать Risk Profile;
* выдавать Evidence за approval;
* интерпретировать CI PASS как approval;
* считать отсутствие ответа acceptance.

⸻

Automatic Git Mutations

Не входят в обязательный initial scope:

* automatic commit;
* automatic push;
* automatic merge;
* automatic release;
* automatic tag;
* automatic rebase;
* force push;
* branch deletion.

Git decisions остаются отдельными human boundaries.

⸻

Multi-Agent Swarm

Не требуются:

* agent swarm;
* parallel reasoning agents с write access;
* voting;
* automatic delegation tree;
* dynamic role network;
* long-running autonomous collaboration.

Для первой версии достаточно одного execution role и одного validation role.

⸻

Multi-Project Operation

Не входят:

* project portfolio;
* cross-project dependencies;
* global dashboard;
* shared organizational memory;
* project fleet management;
* cross-repository release coordination.

⸻

Enterprise Features

Не входят:

* multi-tenancy;
* billing;
* organization management;
* enterprise IAM;
* departmental approval chains;
* regulatory reporting;
* large-scale analytics;
* SLA management.

⸻

Rich User Interface

Не требуются:

* visual workflow builder;
* advanced dashboard;
* graphical project map;
* drag-and-drop;
* mobile application;
* analytics console;
* notification center.

Минимальный chat-first или command-oriented interface достаточен.

⸻

Database

Database не является prerequisite.

Сначала должен быть проверен repository-first approach.

Database добавляется только при доказанной необходимости persistent queries, scale или integrity constraints.

⸻

RAG

RAG не является обязательной частью первой версии.

До его добавления следует проверить, достаточно ли:

* bounded repository context;
* explicit handoff;
* Product Contracts;
* current state summary;
* targeted source selection.

⸻

Knowledge Graph

Не требуется строить полный graph:

* tasks;
* artifacts;
* decisions;
* Evidence;
* agents;
* stages;
* dependencies;
* lifecycle.

Связи могут быть представлены простыми durable references, пока этого достаточно.

⸻

Universal Project Memory

Первая версия не создаёт универсальную память обо всём project history.

Достаточно сохранять state, необходимый для active bounded workflow.

⸻

Architecture Automation

AOS первой версии не должен автоматически:

* выбирать architecture;
* изменять Source of Truth;
* переносить protected contracts;
* выбирать dependencies;
* утверждать ADR;
* расширять product scope.

Architecture decisions остаются отдельной human-controlled boundary.

⸻

Dependency Automation

Первая версия не должна автоматически:

* добавлять dependencies;
* обновлять их;
* включать network;
* выбирать package manager;
* менять runtime stack.

Такие изменения требуют отдельной bounded task.

⸻

Full Recovery Platform

Не требуется строить универсальную систему recovery до возникновения подтверждённой повторяющейся проблемы.

Recovery должен быть:

* bounded;
* временным;
* направленным на восстановление product work;
* не превращённым в постоянный основной workflow.

⸻

Legacy Reconstruction

Не является целью полное воспроизведение:

* AOS-FARM;
* AgentOS;
* AOS-1;
* их topology;
* control systems;
* dependencies;
* historical lifecycle.

Legacy materials используются только как reference.

⸻

Legacy Boundary

AOS-FARM имеет роль:

READ_ONLY_REFERENCE
authority: NONE

Из него можно извлекать:

* product intent;
* useful contracts;
* lessons;
* failure modes;
* negative examples;
* validated patterns.

Нельзя автоматически переносить:

* Source of Truth hierarchy;
* protected status;
* approval records;
* lifecycle state;
* execution authorization;
* architecture;
* Control Plane;
* registry;
* autonomous loops;
* dependency topology.

Каждый заимствованный элемент должен быть повторно оправдан через текущий Product Outcome.

⸻

Scope Expansion Rule

Initial Product Scope может быть расширен только при наличии явного основания.

Основанием может быть:

* повторяющийся user problem;
* подтверждённый failure mode;
* стабильный manual workflow;
* измеримый overhead;
* невозможность выполнить Product Contract без новой capability;
* явное human decision.

Scope не расширяется на основании:

* теоретической полезности;
* архитектурной красоты;
* availability technology;
* исторического наличия feature в AOS-FARM;
* желания автоматизировать единичный случай;
* agent recommendation без product evidence.

⸻

Capability Admission Test

Перед включением новой capability необходимо ответить на вопросы:

1. Какой шаг Primary User Journey она улучшает?
2. Какой Product Contract она реализует?
3. Какое observable user behavior изменится?
4. Какая повторяющаяся проблема подтверждает необходимость?
5. Можно ли временно выполнить процесс вручную?
6. Создаёт ли capability новую authority boundary?
7. Требует ли она full Governance раньше времени?
8. Увеличивает ли она recovery cost?
9. Можно ли реализовать её более простым способом?
10. Как будет измеряться её польза?

Если ответы отсутствуют, capability остаётся вне initial scope.

⸻

Success Metrics

Success Metrics должны измерять пользовательскую ценность, а не внутренний объём системы.

Нежелательные proxy metrics:

* количество документов;
* количество строк code;
* количество schemas;
* количество agents;
* количество automated stages;
* количество statuses;
* количество registry records;
* количество CI checks.

Они могут описывать систему, но не доказывают Product Outcome.

⸻

North Star Outcome

Главный outcome первой версии:

Пользователь может в любой момент правильно понять текущее состояние bounded AI-assisted development cycle и определить одно следующее действие.

Это направление измерения важнее количества automation.

⸻

Primary Success Questions

После реального workflow пользователь должен правильно ответить:

1. Какая задача сейчас активна?
2. Какой stage выполняется или завершён?
3. Какой scope был разрешён?
4. Что фактически изменено?
5. Что было проверено?
6. Что не проверялось?
7. Какие findings существуют?
8. Какие unknowns остаются?
9. Какое human decision требуется?
10. Какое одно действие следует дальше?

Если пользователь не может ответить хотя бы на существенную часть этих вопросов, Product Outcome не подтверждён.

⸻

Metric 1 — Current State Comprehension

Что измеряется

Способность пользователя понять current state без восстановления всей истории.

Признаки успеха

Пользователь может назвать:

* active task;
* current stage;
* last result;
* blocking status;
* pending decision;
* next action.

Возможный способ проверки

После открытия новой session попросить пользователя кратко описать состояние workflow.

Failure Signal

Пользователь вынужден:

* перечитывать предыдущий chat;
* искать несколько reports;
* просить повторный аудит;
* реконструировать Git state вручную.

⸻

Metric 2 — Time to Orientation

Что измеряется

Время от открытия project до понимания текущего рабочего состояния.

Направление улучшения

Время должно сокращаться по сравнению с обычным chat-only workflow.

Важная граница

Само по себе низкое время не является успехом, если summary содержит ложные или неполные claims.

Accuracy важнее скорости.

⸻

Metric 3 — Task Boundary Comprehension

Что измеряется

Понимает ли пользователь:

* allowed scope;
* forbidden scope;
* expected result;
* validation;
* stop conditions.

Признак успеха

Пользователь может объяснить, что agent имеет право изменить и что запрещено.

Failure Signal

Пользователь считает любое технически полезное изменение частью исходной задачи.

⸻

Metric 4 — Scope Integrity

Что измеряется

Доля workflows, в которых execution остаётся в allowed scope.

Признаки успеха

* unrelated files не изменяются;
* out-of-scope need приводит к stop;
* scope correction оформляется отдельно;
* architecture не меняется незаметно.

Failure Signal

Agent регулярно выполняет дополнительные улучшения, которые затем приходится вручную отделять или отменять.

⸻

Metric 5 — Stage Separation Clarity

Что измеряется

Различает ли пользователь:

* planning;
* execution;
* validation;
* review;
* Git decision.

Признак успеха

Пользователь не интерпретирует:

* plan как authorization;
* execution completion как validation;
* validation PASS как approval;
* acceptance как commit permission.

⸻

Metric 6 — Validation Independence

Что измеряется

Сохраняется ли read-only boundary validation.

Признаки успеха

* validation не изменяет artifacts;
* findings не исправляются внутри validation;
* correction получает отдельную task;
* failure не скрывается последующим self-repair.

Failure Signal

Validator исправляет проблему и сообщает только итоговый PASS.

⸻

Metric 7 — Unknown Visibility

Что измеряется

Насколько ясно система показывает:

* UNKNOWN;
* NOT_RUN;
* unavailable checks;
* conflicting facts.

Признак успеха

Пользователь может отличить:

* проверенный факт;
* assumption;
* неизвестный факт;
* незапущенную проверку.

Failure Signal

Пользователь считает incomplete validation полной.

⸻

Metric 8 — Human Decision Clarity

Что измеряется

Понимает ли пользователь:

* требуется ли его решение;
* какое именно;
* почему оно необходимо;
* какие последствия имеют варианты.

Признак успеха

Human checkpoint появляется своевременно и не смешивается с technical result.

Failure Signal

Пользователь не понимает, разрешил ли он:

* execution;
* commit;
* push;
* merge;
* release.

⸻

Metric 9 — One Next Action Clarity

Что измеряется

Способность пользователя определить ближайшее обязательное действие.

Признак успеха

После каждого stage существует одно основное next action.

Failure Signal

Пользователь получает:

* длинный список рекомендаций;
* несколько равнозначных направлений;
* roadmap вместо текущего действия;
* объединённую команду из нескольких independent decisions.

⸻

Metric 10 — Session Resume Success

Что измеряется

Может ли пользователь или новый agent продолжить workflow в новой session.

Признаки успеха

Новая session восстанавливает:

* active task;
* last stage;
* result;
* findings;
* pending decision;
* Git state;
* next action.

Failure Signal

Требуется полный ручной пересказ предыдущей conversation.

⸻

Metric 11 — Recovery Loop Reduction

Что измеряется

Снижается ли число циклов, посвящённых восстановлению состояния вместо развития продукта.

Признаки успеха

* меньше повторных аудитов одной и той же boundary;
* меньше противоречивых reports;
* меньше незавершённых hidden stages;
* меньше повторного анализа уже известных facts.

Failure Signal

Большая часть времени снова уходит на recovery control system.

⸻

Metric 12 — Manual Workflow Reproducibility

Что измеряется

Можно ли провести один и тот же Product Runtime cycle повторно с разными bounded tasks.

Признаки успеха

Минимум два, предпочтительно три manual cycles:

* используют одинаковые основные stages;
* сохраняют contracts;
* дают понятные reports;
* завершаются one next action;
* не требуют уникальной improvisation каждый раз.

Failure Signal

Каждая задача требует нового process design.

⸻

Metric 13 — User Effort

Что измеряется

Сколько ручной работы необходимо пользователю для сохранения понимания и контроля.

Направление успеха

AOS должен снижать effort на:

* восстановление контекста;
* поиск текущего state;
* сравнение reports;
* определение next action;
* объяснение задачи новой session.

Ограничение

AOS не должен снижать effort путём скрытия critical details или автоматического принятия решений.

⸻

Metric 14 — Ceremony-to-Value Ratio

Что измеряется

Не становится ли control workflow тяжелее самой bounded task.

Признаки успеха

* documentation task не требует enterprise workflow;
* low-risk change использует короткий safe path;
* reports достаточно компактны;
* human checkpoints возникают только в нужных boundaries.

Failure Signal

Подготовка и обслуживание control artifacts занимают больше времени, чем полезное изменение.

⸻

Metric 15 — Product Value Before Infrastructure

Что измеряется

Появляется ли observable user value до построения полной infrastructure.

Признаки успеха

Первый полезный cycle работает без:

* Control Plane;
* global registry;
* database;
* Runtime Enforcement;
* multi-agent orchestration;
* enterprise Governance.

Failure Signal

Product Runtime не может быть проверен, пока не завершена большая infrastructure program.

⸻

Metric 16 — Trust Through Facts

Что измеряется

Основано ли доверие пользователя на observable facts, а не на уверенности agent response.

Признаки успеха

Пользователь получает:

* exact scope;
* changed artifacts;
* checks;
* results;
* unknowns;
* Git state;
* human decision boundary.

Failure Signal

Основное доказательство звучит как:

Agent сказал, что всё готово.

⸻

Metric 17 — Product Outcome Completion

Что измеряется

Достигнут ли основной Product Outcome конкретного cycle.

Product Outcome считается достигнутым, если

Пользователь:

* понимает intent;
* видит bounded task;
* отдельно разрешает execution;
* понимает factual execution result;
* видит independent validation result;
* понимает unknowns;
* принимает human decision;
* получает одно next action;
* может возобновить работу позднее.

⸻

Metric 18 — Failure Usefulness

Что измеряется

Сохраняет ли продукт ценность при FAIL, BLOCKED или UNKNOWN.

Признаки успеха

При failure пользователь получает:

* точный finding;
* affected boundary;
* выполненные и невыполненные действия;
* current repository state;
* одно next action;
* явный stop.

Failure Signal

Неуспешный stage приводит к:

* automatic retry;
* silent correction;
* scope expansion;
* потере state;
* непонятному завершению.

⸻

Metric 19 — Git Boundary Comprehension

Что измеряется

Понимает ли пользователь текущее Git state и необходимые отдельные решения.

Признаки успеха

Пользователь различает:

Edit
Commit
Push
Merge
Release

и понимает, что каждое действие имеет собственную authorization boundary.

Failure Signal

Пользователь считает, что принятие результата автоматически означает push или merge.

⸻

Metric 20 — Replaceability of Agent

Что измеряется

Может ли другой agent продолжить workflow на основании durable context и Product Contracts.

Признак успеха

Смена provider или session не требует восстановления hidden reasoning.

Failure Signal

Workflow работает только с одной моделью или одним длинным chat.

⸻

Qualitative Success Signals

На раннем этапе qualitative observations важнее сложной аналитики.

Полезные сигналы:

* пользователь реже спрашивает: «На чём мы остановились?»;
* пользователь быстрее понимает current state;
* пользователь реже путает PASS и approval;
* пользователь замечает unknowns;
* пользователь уверен, что scope ограничен;
* следующий шаг воспринимается как однозначный;
* новая session продолжает работу без полного пересказа;
* количество repair loops сокращается;
* control process не вытесняет product work.

⸻

Quantitative Metric Candidates

После появления working prototype можно измерять:

* median time to understand current state;
* median time to resume a task;
* percentage of stages with one unambiguous next action;
* percentage of execution stages without scope drift;
* percentage of validation stages with zero artifact changes;
* percentage of reports with explicit unknown handling;
* number of manual clarification turns per Task Brief;
* number of recovery sessions per completed task;
* number of hidden or implicit Git actions;
* number of user corrections caused by misunderstood state;
* completion rate of bounded manual cycles;
* percentage of users able to explain current state correctly.

Точные target values должны определяться только после получения baseline observations.

⸻

Metrics That Must Not Become Goals

Некоторые показатели легко улучшить искусственно.

Нельзя оптимизировать продукт только под:

Количество PASS

Система может увеличить количество PASS, скрывая UNKNOWN и NOT_RUN.

Это недопустимо.

⸻

Скорость Completion

Workflow можно ускорить, убрав human checkpoints.

Это может разрушить Product Contracts.

⸻

Количество Automation

Больше automation не означает больше user value.

⸻

Количество Tasks

Высокая throughput не доказывает понимание и контроль.

⸻

Минимум Stops

Stop является корректным результатом при blocking finding.

Снижение числа stops любой ценой опасно.

⸻

Минимум Human Decisions

Human decisions являются частью Product Outcome, а не дефектом системы.

⸻

Максимум Context

Большой объём context может увеличивать cognitive load и создавать новые contradictions.

⸻

Failure Signals

Следующие признаки означают, что Product Boundary или Product Outcome требуют пересмотра.

⸻

User Cannot Explain Current State

Пользователь не понимает:

* что активно;
* что завершено;
* что проверено;
* что делать дальше.

⸻

Workflow Depends on Chat History

Без предыдущей conversation невозможно продолжить работу.

⸻

Task Brief Is Heavier Than Task

Для небольшого изменения требуется чрезмерная ceremony.

⸻

Scope Drift Remains Common

Agent регулярно меняет unrelated artifacts.

⸻

Validation Repairs Artifacts

Independent validation не сохраняет read-only boundary.

⸻

PASS Is Interpreted as Approval

Пользователь или система смешивает technical result и human decision.

⸻

Unknowns Are Hidden

Непроверенные факты представлены как безопасные.

⸻

One Next Action Is Missing

После stage остаётся множество равнозначных направлений.

⸻

Recovery Dominates Product Work

Проект снова большую часть времени восстанавливает собственный control state.

⸻

Infrastructure Becomes Prerequisite

Для первого user outcome требуется завершить:

* registry;
* Control Plane;
* full Governance;
* Runtime Enforcement;
* complex agent orchestration.

⸻

Product Contracts Require Provider-Specific Behavior

Смена agent разрушает workflow.

⸻

Automation Expands Authority

Автоматизированный механизм начинает:

* назначать Risk Profile;
* принимать result;
* расширять scope;
* выполнять Git actions.

⸻

Metrics Encourage False Claims

Система оптимизируется под optimistic status вместо truthful state.

⸻

Manual Validation of Product Value

До автоматизации metrics First Product Vertical Slice должен быть проверен через manual observation.

Для каждого cycle необходимо зафиксировать:

* исходный intent;
* время до понятного Task Brief;
* число scope clarifications;
* понимание allowed и forbidden scope;
* execution result;
* validation result;
* unknowns;
* human decision;
* next action;
* успешность session resume;
* субъективную понятность workflow;
* признаки лишней ceremony;
* признаки missing capability.

⸻

Minimum Number of Manual Cycles

До controlled automation следует провести:

minimum: 2
preferred: 3

real manual cycles.

Один успешный cycle недостаточен для вывода о стабильности workflow.

Необходимо проверить:

* обычный successful case;
* case с validation finding;
* case с UNKNOWN, BLOCKED или scope conflict.

⸻

Suggested Manual Cycle Set

Cycle 1 — Documentation Change

Проверяет:

* bounded scope;
* rewrite workflow;
* target-only validation;
* human review;
* one next action.

⸻

Cycle 2 — Small Code Fix

Проверяет:

* reproducible defect;
* production code boundary;
* test update;
* independent validation;
* Git decision separation.

⸻

Cycle 3 — Blocking or Unknown Case

Проверяет:

* honest unknown handling;
* blocking finding;
* no automatic retry;
* report and stop;
* session resume.

⸻

Product Value Review Questions

После каждого manual cycle пользователь должен ответить:

1. Было ли сразу понятно, где начинается task?
2. Был ли scope достаточно ограничен?
3. Было ли понятно, когда требовалось human decision?
4. Было ли видно, что execution завершён, но validation ещё нет?
5. Было ли ясно, что именно проверялось?
6. Были ли видимы unknowns и NOT_RUN?
7. Был ли следующий шаг однозначным?
8. Можно ли было продолжить workflow в новой session?
9. Снизилась ли необходимость самостоятельно восстанавливать context?
10. Был ли процесс легче, чем обычный chat-only workflow?

⸻

Conditions for Product Scope Expansion

Расширение initial scope допустимо, когда одновременно выполнены условия:

1. First Vertical Slice реально проведён.
2. Минимум два manual cycles завершены.
3. Product Contracts показали устойчивость.
4. Повторяющаяся проблема подтверждена observations.
5. Новая capability напрямую улучшает Primary User Journey.
6. Более простой manual solution признан недостаточным.
7. Human authority boundary определена.
8. Validation approach определён.
9. Дополнительная complexity оправдана.
10. Human явно разрешил scope expansion.

⸻

Conditions for Automation

Automation допустима только для шага, который:

* повторился в нескольких cycles;
* имеет стабильный input;
* имеет однозначный output;
* имеет определённые failure states;
* сохраняет human authority;
* может быть independently validated;
* не расширяет scope;
* имеет понятный stop condition;
* уменьшает effort;
* не скрывает important facts.

⸻

Conditions for Registry

Registry становится кандидатом, если manual workflow показывает:

* большое число связанных durable artifacts;
* частые cross-session queries;
* противоречия идентичности;
* невозможность надёжно найти current state;
* multi-project need;
* необходимость integrity validation.

До этого registry остаётся вне initial scope.

⸻

Conditions for Control Plane

Control Plane становится кандидатом, если:

* repository-first artifacts больше не обеспечивают consistency;
* возникает повторяющаяся проблема enforcement;
* multiple tools нарушают contracts;
* human checkpoints невозможно поддерживать вручную;
* простой interface не может показать authoritative state.

Control Plane не создаётся только потому, что он существовал в legacy project.

⸻

Conditions for Runtime Enforcement

Runtime Enforcement рассматривается после того, как:

* Product Contracts подтверждены manual cycles;
* enforcement targets стабильны;
* false positive и false block risks понятны;
* human override boundary определена;
* enforcement полезнее manual checks;
* Product Runtime уже создаёт observable value.

⸻

Conditions for Rich UI

Rich UI становится кандидатом, если chat-first workflow показывает устойчивые ограничения:

* current state трудно воспринимать;
* details сложно раскрывать;
* visual comparison действительно помогает;
* user decisions требуют structured controls;
* workflow используется достаточно часто.

UI не должен проектироваться раньше понимания journey.

⸻

Product Boundary Invariants

Глобальные safety, authority, stage и Git invariants определены только в
[`../00_Core/Minimal_Safety_Floor.md`](../00_Core/Minimal_Safety_Floor.md).
Этот документ применяет их к Product Boundary и не переопределяет.

Product-specific scope, capability-admission и success rules определены в следующих разделах этого документа.

⸻

Success Definition for First Product Version

Первая версия AOS может считаться product-success candidate, если подтверждено следующее:

User Outcome

Пользователь проходит один real bounded cycle и сохраняет понимание состояния.

Scope Integrity

Execution не выходит за allowed scope.

Stage Integrity

Planning, execution, validation и review разделены.

Human Authority

Обязательные решения не симулируются.

Truthful State

UNKNOWN и NOT_RUN показываются явно.

Validation Integrity

Validation не исправляет artifact.

Continuity

Новая session восстанавливает minimal factual context.

Direction

После каждого stage существует one next action.

Simplicity

Workflow работает без преждевременного Control Plane, registry и full Governance.

Reproducibility

Manual workflow успешно повторён минимум два раза.

⸻

What Success Does Not Mean

Даже если первая версия достигает Product Outcome, это не означает:

* product-market fit;
* production readiness;
* scalability;
* enterprise readiness;
* release authorization;
* security completeness;
* architectural finality;
* завершённость Development Factory;
* готовность Runtime Enforcement.

Success всегда относится к явно определённой boundary.

⸻

Product Boundary Statement

Полная формулировка:

Первая версия AOS ограничена одним пользователем, одним software project, одним repository и одним bounded AI-assisted change cycle. Она должна доказать observable user value через current state visibility, bounded task, explicit human authority, controlled execution, independent validation, session continuity и one next action. Любая дополнительная infrastructure добавляется только после подтверждённой повторяющейся необходимости.

⸻

Success Metrics Statement

Полная формулировка:

Успех первой версии определяется не количеством automation или artifacts, а способностью пользователя правильно понимать текущее состояние workflow, сохранять control над scope и decisions, различать execution, validation и approval, продолжать работу между sessions и всегда видеть одно следующее действие.

⸻

Краткое резюме

Initial Scope

one user
one project
one repository
one active task
one writer
one bounded cycle
manual checkpoints
repository-first state
chat-first interaction

Required Value

Пользователь понимает:

что происходит
что разрешено
что сделано
что проверено
что неизвестно
что требует решения
что делать дальше

Outside Initial Scope

* full Development Factory;
* Control Plane;
* global registry;
* full Governance;
* Runtime Enforcement;
* autonomous workflows;
* automatic Git mutations;
* multi-project operation;
* enterprise features;
* rich UI;
* database;
* RAG;
* universal project memory.

Main Success Signal

Пользователь может провести и затем возобновить один real bounded workflow без ручного восстановления всей истории.

Main Failure Signal

Control infrastructure снова начинает развиваться быстрее, чем observable Product Runtime value.
