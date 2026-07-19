Primary User Journey

Назначение документа

Этот документ описывает основной пользовательский путь первой версии AOS.

Он показывает, как primary user проходит от исходного намерения до понятного результата через один ограниченный Product Runtime cycle.

Документ определяет:

* точку входа пользователя;
* последовательность пользовательских шагов;
* информацию, которую AOS должен показывать на каждом этапе;
* решения, остающиеся за человеком;
* ожидаемые состояния пользователя;
* основные альтернативные и ошибочные пути;
* session resume;
* границы завершения;
* observable признаки успешного journey.

Документ не определяет:

* внутреннюю architecture;
* конкретный UI framework;
* implementation plan;
* API;
* database;
* formal state machine;
* orchestration engine;
* Control Plane;
* registry;
* Runtime Enforcement;
* полный набор будущих user journeys.

Primary User Journey является описанием пользовательского опыта и observable behavior, а не заявлением о наличии работающего Product Runtime.

⸻

Primary Journey Goal

Основная цель пользователя:

Провести одно ограниченное изменение software product с помощью AI agent, сохранив понимание задачи, scope, фактического результата, проверок, обязательных решений и следующего действия.

Пользователь не должен самостоятельно восстанавливать весь workflow из:

* длинной chat history;
* terminal output;
* Git history;
* нескольких reports;
* памяти предыдущих sessions;
* разрозненных project files.

AOS должен собирать минимально необходимое представление текущего состояния и показывать его в момент, когда оно требуется пользователю.

⸻

Journey Overview

Основной путь:

1. Enter Project
2. Understand Current State
3. Express Intent
4. Clarify Expected Outcome
5. Review Bounded Task
6. Make Execution Decision
7. Observe Execution Boundary
8. Review Execution Result
9. Start Independent Validation
10. Review Validation Result
11. Make Human Decision
12. Receive One Next Action
13. Stop or Resume Later

В сокращённой форме:

project
→ current state
→ intent
→ bounded task
→ human authorization
→ execution
→ factual report
→ independent validation
→ human review
→ one next action
→ stop

Один journey относится к:

* одному project;
* одному repository;
* одной active task;
* одному execution stage;
* одному validation stage;
* одному human review point.

⸻

Участники Journey

Primary User

Человек, который:

* формулирует product intent;
* определяет желаемый outcome;
* подтверждает или изменяет scope;
* назначает Risk Profile, когда это требуется;
* разрешает execution;
* рассматривает findings;
* принимает обязательные решения;
* отдельно разрешает Git actions.

AOS

Product Runtime, который:

* показывает current state;
* помогает ограничить задачу;
* различает факты, assumptions и decisions;
* отображает boundaries;
* сохраняет continuity;
* показывает reports;
* не скрывает unknowns;
* указывает одно следующее действие;
* останавливается в обязательных точках.

Execution Agent

Исполнитель, который:

* работает только в allowed scope;
* не расширяет authority;
* не назначает Risk Profile;
* выполняет один stage;
* сообщает фактический результат;
* останавливается после завершения или blocking finding.

Validation Agent

Независимый проверяющий, который:

* работает read-only относительно target artifacts;
* проверяет заявленную boundary;
* не исправляет findings;
* не повторяет validation автоматически;
* формирует Validation Report;
* останавливается.

В первой версии роли execution и validation могут использовать одного provider, но должны выполняться как отдельные sessions и этапы.

⸻

Пользовательское состояние до начала Journey

До входа в AOS пользователь может находиться в одном из следующих состояний:

New Intent

У пользователя есть новая идея или задача, но нет готового Task Brief.

Resume Work

Пользователь возвращается к ранее остановленной задаче.

Unclear State

Пользователь не уверен:

* на чём остановилась работа;
* что было выполнено;
* что осталось нерешённым;
* какой stage был последним;
* что делать дальше.

Finding Follow-Up

Пользователь возвращается после:

* FAIL;
* BLOCKED;
* scope conflict;
* validation finding;
* отсутствующего human decision.

AOS должен поддерживать все эти точки входа, но основной happy path начинается с нового intent.

⸻

Journey Stage 1 — Enter Project

Намерение пользователя

Пользователь выбирает или открывает project, в котором хочет продолжить работу.

Он ожидает сразу понять:

* какой project открыт;
* какой repository используется;
* какая branch активна;
* существует ли active task;
* есть ли незавершённый stage;
* требуется ли его решение.

Что показывает AOS

Минимальный Project Context:

* project name;
* repository;
* branch;
* known baseline;
* current working state;
* active task, если она существует;
* last completed stage;
* pending human decision;
* next required action.

Пример operational summary:

Project: AOS
Repository: /Users/muhammed/Documents/GitHub/notebook
Branch: dev
Active task: NONE
Working tree: CHANGES_PRESENT
Pending decision: NONE
Next action: DEFINE_TASK_INTENT

Пользовательский outcome

Пользователь понимает, находится ли он:

* в чистой начальной точке;
* внутри незавершённого workflow;
* перед обязательным решением;
* в состоянии, которое требует preflight review.

Обязательная граница

AOS не должен автоматически начинать новую задачу, если уже существует незавершённая active task, без явного решения пользователя.

⸻

Journey Stage 2 — Understand Current State

Намерение пользователя

Пользователь хочет понять фактическое состояние проекта до постановки новой задачи.

Что показывает AOS

AOS должен отделять:

Factual State

Факты, полученные из authoritative source:

* current branch;
* baseline;
* working tree state;
* existing task artifacts;
* last Stage Report;
* last Validation Report;
* recorded human decisions.

Claims

Утверждения, которые пока не подтверждены factual source.

Unknowns

Факты, которые невозможно определить.

Conflicts

Несовместимые данные из разных источников.

Пример

Current stage: HUMAN_REVIEW_REQUIRED
Execution result: PASS
Validation result: FAIL
Blocking finding: incorrect behavior in target case
Commit authorization: NOT_GRANTED
Next action: REVIEW_VALIDATION_FINDING

Пользовательский outcome

Пользователь может кратко ответить:

1. Что сейчас активно?
2. Что уже завершено?
3. Что не завершено?
4. Что требует решения?
5. Можно ли начинать новую задачу?

Обязательная граница

Если current state содержит blocking uncertainty, AOS не должен представлять его как нормальную ready state.

⸻

Journey Stage 3 — Express Intent

Намерение пользователя

Пользователь формулирует, чего хочет добиться.

Intent может быть выражен естественным языком:

Исправить неверное описание Product Runtime в одном документе.

или:

Добавить поддержку повторного открытия последней задачи.

Что делает AOS

AOS преобразует intent не в implementation plan, а в начальное понимание задачи.

Он выделяет:

* объект изменения;
* желаемый outcome;
* предполагаемую boundary;
* неизвестные детали;
* возможные scope risks.

Что видит пользователь

Краткое отражение intent:

Understood intent:
Update one Product document so that it clearly distinguishes
Product Runtime from Development Factory.
Target artifact: not yet confirmed
Expected observable result: documentation wording corrected
Execution authorization: not requested

Пользовательский outcome

Пользователь может подтвердить, что AOS понял его цель правильно, до начала детализации или изменения files.

Обязательная граница

Intent ≠ Task Brief.
Intent ≠ execution authorization.

⸻

Journey Stage 4 — Clarify Expected Outcome

Намерение пользователя

Пользователь уточняет, как должен выглядеть полезный результат.

AOS помогает определить

* что должно измениться для пользователя или продукта;
* какой observable result ожидается;
* что не является целью;
* какие ограничения существенны;
* как можно проверить результат.

Пример

Исходное намерение:

Исправить документ.

Уточнённый expected outcome:

The target Markdown document clearly explains:
- Product Runtime is the user-facing product;
- Development Factory is supporting infrastructure;
- first product value does not depend on full factory completion.
No other files are changed.
Markdown structure is preserved.

Пользовательский outcome

Пользователь видит результат как проверяемое состояние, а не как абстрактное пожелание.

Ошибочный путь

Если expected outcome невозможно сформулировать без выбора architecture или существенного расширения scope, AOS должен остановить переход к execution и показать:

PLANNING_REQUIRED

⸻

Journey Stage 5 — Review Bounded Task

Намерение пользователя

Пользователь рассматривает точную bounded task перед execution.

Что показывает AOS

Task Brief в компактной форме:

Goal

Что требуется получить.

Allowed Scope

Какие artifacts и действия разрешены.

Forbidden Scope

Что запрещено менять или выполнять.

Context

Repository, branch, baseline и relevant contracts.

Requirements

Обязательные свойства результата.

Validation

Какими checks результат должен быть проверен.

Stop Conditions

Когда agent обязан прекратить работу.

Permissions

Разрешённые и запрещённые Git, network и workspace actions.

Пример Task Summary

Goal:
Rewrite one Markdown document to clarify Product Runtime boundaries.
Allowed scope:
AOS/01_Product/Primary_User_Journey.md
Forbidden scope:
- all other files;
- YAML metadata;
- Status sections;
- index updates;
- implementation;
- commit;
- push.
Validation:
- target-only diff;
- Markdown structure preserved;
- no YAML metadata;
- no approval claims.
Stop conditions:
- another file must be changed;
- required context is conflicting;
- target file is missing;
- baseline changed.

Пользовательские решения

Пользователь может выбрать одно направление:

ACCEPT_TASK_BRIEF
REVISE_TASK_BRIEF
REJECT_TASK
DEFER_TASK

Важная граница

Подтверждение Task Brief означает согласие с описанием задачи.

Оно не означает автоматическое разрешение execution.

Task Brief acceptance ≠ execution authorization.

⸻

Journey Stage 6 — Make Execution Decision

Намерение пользователя

Пользователь решает, разрешать ли выполнение bounded task.

Что показывает AOS

Перед решением AOS кратко показывает:

* target;
* expected result;
* allowed scope;
* forbidden scope;
* proposed Risk Profile;
* known risks;
* unknowns;
* execution environment;
* запрещённые Git actions.

Risk Profile Boundary

Если Risk Profile требуется, AOS может предложить:

Proposed Risk Profile: LOW
Reason:
- one Markdown file;
- no runtime changes;
- no destructive actions;
- no Git mutations.

Но назначение выполняет человек.

Proposed Risk Profile ≠ assigned Risk Profile.

Возможные решения

AUTHORIZE_EXECUTION
REVISE_TASK
DEFER
REJECT

Пользовательский outcome

Пользователь понимает, что именно будет выполнено после его решения.

Обязательная остановка

При отсутствии необходимого решения:

HUMAN_REVIEW_REQUIRED

Workflow останавливается.

⸻

Journey Stage 7 — Observe Execution Boundary

Намерение пользователя

Пользователь ожидает, что agent выполнит только разрешённое изменение.

Что показывает AOS

Перед запуском:

Stage: EXECUTION
Writer: execution agent
Scope: one target file
Validation: not part of this stage
Git mutations: forbidden
Network: disabled

Во время выполнения AOS не обязан показывать каждый внутренний шаг агента.

Пользователю важно видеть:

* active stage;
* active scope;
* whether stage is still running;
* whether a blocking condition occurred.

Execution Rules

Agent должен:

* работать только в Task Brief;
* не изменять соседние artifacts;
* не начинать independent validation;
* не исправлять unrelated findings;
* не выполнять commit или push;
* остановиться на первом blocking finding.

Scope Conflict

Если требуется изменение вне allowed scope:

Execution stopped.
Reason: required change is outside allowed scope.
Result: BLOCKED
Next action: REVISE_TASK_BRIEF

Пользовательский outcome

Пользователь может доверять не внутреннему reasoning агента, а видимой boundary выполнения.

⸻

Journey Stage 8 — Review Execution Result

Намерение пользователя

Пользователь хочет понять, что фактически произошло.

Что показывает AOS

Execution Report должен иметь два уровня.

Operational Summary

Stage: EXECUTION
Result: PASS
Changed files: 1
Scope conflict: NO
Validation: NOT_RUN
Git actions: NONE
Next action: RUN_INDEPENDENT_VALIDATION

Technical Details

По запросу:

* exact file paths;
* summary of changes;
* diff;
* commands;
* outputs;
* assumptions;
* findings;
* unknowns;
* exit codes.

Пользовательский outcome

Пользователь различает:

* изменение выполнено;
* изменение проверено;
* изменение принято;
* изменение разрешено commit.

Эти состояния не объединяются.

Обязательные инварианты

Execution PASS ≠ Validation PASS.
Execution PASS ≠ approval.
Execution PASS ≠ commit authorization.

⸻

Journey Stage 9 — Start Independent Validation

Намерение пользователя

Пользователь запускает отдельную проверку результата.

Что показывает AOS

До validation:

* validation target;
* candidate identity или current diff;
* validation scope;
* checks;
* read-only boundary;
* stop conditions.

Пример:

Validation target:
AOS/01_Product/Primary_User_Journey.md
Checks:
- only target file changed;
- Markdown headings preserved;
- no YAML metadata;
- no Status section;
- no approval claims;
- no implementation claims.
Mode: READ_ONLY
Automatic correction: FORBIDDEN

Пользовательский outcome

Пользователь понимает, что validation не продолжает execution и не исправляет результат.

Обязательная граница

Validation запускается как отдельный stage.

One run = one stage.

⸻

Journey Stage 10 — Review Validation Result

Намерение пользователя

Пользователь хочет узнать, соответствует ли результат заявленным требованиям.

Что показывает AOS

Validation Report:

Stage: VALIDATION
Result: PASS
Checks passed: 6
Checks failed: 0
Unknown: 0
Not run: 0
Files modified during validation: 0
Next action: REVIEW_RESULT

При failure:

Stage: VALIDATION
Result: FAIL
Blocking finding:
Unexpected change in adjacent document.
Checks not completed:
- semantic consistency review
Files modified during validation: 0
Next action: CREATE_CORRECTION_TASK

Значение результатов

PASS

Проверки в заявленной boundary завершились успешно.

FAIL

Хотя бы одна обязательная проверка завершилась отрицательно.

UNKNOWN

Необходимый факт невозможно подтвердить.

NOT_RUN

Проверка не запускалась.

BLOCKED

Продолжение validation невозможно из-за blocking condition.

Пользовательский outcome

Пользователь понимает:

* что проверено;
* что не проверено;
* насколько широкой была проверка;
* какие findings требуют решения.

Инварианты

PASS ≠ approval.
Evidence ≠ approval.
CI PASS ≠ approval.
UNKNOWN ≠ OK.
NOT_RUN ≠ PASS.

⸻

Journey Stage 11 — Make Human Decision

Намерение пользователя

Пользователь принимает решение о результате, основываясь на фактах.

Что показывает AOS

Review Package должен кратко объединить:

* original intent;
* expected outcome;
* allowed scope;
* execution summary;
* validation summary;
* findings;
* unknowns;
* Git state;
* доступные решения.

Возможные решения

Accept Result

Пользователь считает результат содержательно приемлемым.

Это ещё не обязательно разрешает Git action.

Request Correction

Пользователь требует отдельную correction task.

Revise Scope

Исходная задача оказалась недостаточной или неверной.

Defer

Решение откладывается.

Reject Result

Результат не принимается.

Authorize Commit

Отдельное разрешение создать commit, если validation и review позволяют это действие.

Stop

Завершить работу без дальнейших действий.

Пользовательский outcome

Пользователь видит только решения, допустимые в текущем состоянии.

Например, при validation FAIL AOS не должен показывать merge или release как обычный следующий шаг.

Human Authority Boundary

AOS не должен выводить acceptance из:

* PASS;
* отсутствия возражений;
* предыдущего разрешения;
* Evidence;
* CI;
* agent recommendation.

Human approval cannot be simulated.

⸻

Journey Stage 12 — Receive One Next Action

Намерение пользователя

После решения пользователь хочет понять, что делать дальше.

Что показывает AOS

Ровно одно основное действие.

Примеры:

AUTHORIZE_EXECUTION
RUN_INDEPENDENT_VALIDATION
REVIEW_VALIDATION_FINDING
CREATE_CORRECTION_TASK
AUTHORIZE_COMMIT
RESOLVE_BASELINE_CONFLICT
STOP

Свойства Next Action

Next action должен быть:

* конкретным;
* выполнимым;
* относящимся к текущему состоянию;
* не скрывающим human checkpoint;
* не объединяющим несколько независимых authorizations;
* не расширяющим scope.

Неправильный пример:

Review the result, fix anything needed, commit, push and continue.

Правильный пример:

CREATE_CORRECTION_TASK

Пользовательский outcome

Пользователь не выбирает из длинного списка равнозначных направлений.

Он понимает ближайшую обязательную точку workflow.

⸻

Journey Stage 13 — Stop

Намерение пользователя

Пользователь завершает текущий этап и ожидает, что система не продолжит работу самостоятельно.

Что делает AOS

AOS фиксирует:

* last completed stage;
* result;
* findings;
* unknowns;
* pending decisions;
* Git state;
* next required action.

После этого workflow останавливается.

Обязательное правило

Stage complete
→ report
→ one next action
→ stop

AOS не должен автоматически:

* начинать correction;
* запускать validation повторно;
* переходить к следующему stage;
* выполнять commit;
* выполнять push;
* создавать новую task.

⸻

Session Resume Journey

Сценарий

Пользователь возвращается позже или открывает новую chat session.

Он говорит:

Продолжить работу.

Что показывает AOS

Resume Summary:

Project: AOS
Active task: update Primary User Journey document
Last completed stage: VALIDATION
Validation result: FAIL
Blocking finding: adjacent file changed
Pending human decision: correction direction
Git actions: NONE
Next required action: CREATE_CORRECTION_TASK

Пользовательский outcome

Пользователь может продолжить работу без:

* полного пересказа истории;
* чтения предыдущего chat;
* повторного анализа уже известных facts;
* повторного запуска завершённого stage.

Resume Boundary

AOS восстанавливает context, но не выполняет next action автоматически.

Resume ≠ authorization.

⸻

Alternative Journey — Blocking Finding During Execution

Сценарий

Во время execution agent обнаруживает, что необходимое изменение затрагивает protected или forbidden artifact.

Ожидаемый путь

execution started
→ blocking finding detected
→ no out-of-scope modification
→ Execution Report
→ result: BLOCKED
→ next action: REVISE_TASK_BRIEF
→ stop

Пользовательский outcome

Пользователь получает:

* конкретный finding;
* объяснение boundary;
* список невыполненных действий;
* factual Git state;
* одно следующее действие.

Agent не пытается решить проблему самостоятельно.

⸻

Alternative Journey — Validation Failure

Сценарий

Execution завершён, но validation обнаруживает нарушение requirements.

Ожидаемый путь

validation started
→ check failed
→ no correction performed
→ Validation Report
→ human review
→ next action: CREATE_CORRECTION_TASK
→ stop

Пользовательский outcome

Пользователь видит, что:

* validation сохранила независимость;
* artifact не был изменён во время проверки;
* failure не скрыт;
* correction требует новой bounded task.

⸻

Alternative Journey — Unknown Blocks Continuation

Сценарий

AOS не может определить baseline или current branch.

Ожидаемый путь

context inspection
→ required fact unavailable
→ UNKNOWN_BLOCKED
→ report
→ next action: RESOLVE_REPOSITORY_CONTEXT
→ stop

Пользовательский outcome

Пользователь понимает:

* какой факт неизвестен;
* почему он необходим;
* какую boundary он блокирует;
* что требуется сделать дальше.

Unknown не преобразуется в optimistic assumption.

⸻

Alternative Journey — Baseline Changed

Сценарий

Между Task Brief и execution изменился baseline.

Ожидаемый путь

pre-execution check
→ baseline mismatch
→ execution not started
→ report
→ next action: REVALIDATE_TASK_BRIEF
→ stop

Пользовательский outcome

Пользователь не получает изменение, выполненное относительно неожиданного состояния repository.

⸻

Alternative Journey — User Rejects Task Brief

Сценарий

Пользователь считает предложенный scope неправильным.

Ожидаемый путь

Task Brief presented
→ user rejects or requests revision
→ no execution
→ next action: REVISE_TASK_BRIEF
→ stop

Пользовательский outcome

Пользователь сохраняет контроль до изменения repository.

⸻

Alternative Journey — Result Accepted Without Git Action

Сценарий

Пользователь принимает результат, но не хочет создавать commit.

Ожидаемый путь

human review
→ result accepted
→ commit not authorized
→ working tree remains modified
→ next action: STOP

Пользовательский outcome

AOS не считает acceptance автоматическим разрешением изменить Git history.

⸻

Alternative Journey — Commit Requested

Сценарий

После human review пользователь отдельно разрешает commit.

Ожидаемый путь

Commit становится отдельной bounded task или отдельным stage.

Перед commit проверяются:

* exact diff;
* staged files;
* unrelated changes;
* commit message;
* branch;
* commit authorization.

После commit:

* push не выполняется автоматически;
* merge не выполняется автоматически;
* release не выполняется автоматически.

Инвариант

Commit ≠ push ≠ merge ≠ release.

⸻

Emotional and Cognitive Journey

Primary User Journey должен учитывать не только последовательность операций, но и состояние пользователя.

До AOS

Пользователь может испытывать:

* неопределённость;
* потерю контекста;
* недоверие к agent claims;
* страх повредить repository;
* перегрузку длинными reports;
* необходимость постоянно перепроверять работу;
* трудность выбора следующего действия.

Во время корректного Journey

Пользователь должен постепенно получать:

Orientation

Я понимаю, где нахожусь.

Clarity

Я понимаю, какая задача активна.

Control

Я понимаю, что разрешено и что запрещено.

Trust Through Evidence

Я вижу, что фактически было сделано и проверено.

Honest Uncertainty

Я вижу, что неизвестно или не запускалось.

Decision Readiness

Я понимаю, какое решение требуется от меня.

Direction

Я знаю одно следующее действие.

AOS не должен создавать доверие за счёт уверенного тона. Доверие должно возникать из observable boundaries и factual reporting.

⸻

Information Hierarchy

На каждом этапе информация должна показываться в следующем порядке.

1. Current Stage

Что происходит сейчас.

2. Current Result

Что произошло на этом этапе.

3. Blocking State

Есть ли причина, запрещающая продолжение.

4. Human Decision

Требуется ли решение пользователя.

5. Next Action

Какое действие следует дальше.

6. Details

Technical context по запросу.

Пример:

Stage: VALIDATION
Result: FAIL
Blocking: YES
Human decision: REQUIRED
Next action: REVIEW_FINDING
Details:
- failed check;
- exact file;
- command;
- output;
- affected boundary.

⸻

Progressive Disclosure

Primary Journey должен быть пригоден для non-programmer и technical user.

Default View

Показывает:

* current stage;
* short result;
* findings;
* pending decision;
* next action.

Detailed View

Показывает:

* exact paths;
* baseline;
* commands;
* exit codes;
* diffs;
* test output;
* Evidence;
* validation scope;
* source references.

Пользователь не должен быть вынужден читать raw technical output для понимания основного результата.

При этом detailed information должна оставаться доступной.

⸻

Chat-First Journey Hypothesis

Первая версия может использовать chat-first interaction.

Пример основного диалога:

User:
Исправь описание Product Outcome.
AOS:
Current project identified.
No active task.
Understood intent:
Rewrite one Product Outcome document.
Next action:
REVIEW_TASK_BRIEF

После review:

AOS:
Task Brief accepted.
Execution is not yet authorized.
Proposed Risk Profile: LOW
Next action:
AUTHORIZE_EXECUTION

После execution:

AOS:
Execution completed.
Changed files: 1
Validation: NOT_RUN
Git actions: NONE
Next action:
RUN_INDEPENDENT_VALIDATION

После validation:

AOS:
Validation result: PASS
Human acceptance: NOT_RECORDED
Next action:
REVIEW_RESULT

Chat-first является interaction hypothesis, а не зафиксированной architecture.

⸻

Journey Data That Must Persist

Для continuity между sessions необходимо сохранять минимальный набор фактов:

* project identity;
* repository;
* branch;
* baseline;
* active task identity;
* Task Brief;
* current stage;
* completed stage reports;
* validation results;
* findings;
* unknowns;
* recorded human decisions;
* pending human decisions;
* Git state;
* next required action.

Эти данные могут храниться в простых repository artifacts.

Первая версия не требует database или global registry.

⸻

Source of Truth During Journey

Для разных классов фактов должны использоваться разные authoritative sources.

Repository and Git

Источник истины для:

* files;
* diff;
* branch;
* commit history;
* working tree;
* baseline identity.

Task Brief

Источник истины для:

* allowed scope;
* forbidden scope;
* requirements;
* validation;
* stop conditions;
* permissions.

Stage Report

Источник истины для заявленного результата конкретного stage.

Validation Evidence

Источник истины для выполненных checks и их outputs.

Human Decision Record

Источник истины для explicit human authorization или acceptance.

Chat

Chat является interaction surface.

Chat не должен автоматически заменять durable factual records.

⸻

Journey Boundaries

Planning Boundary

Planning описывает возможное решение.

Planning не разрешает execution.

Execution Boundary

Execution изменяет только allowed artifacts.

Execution не подтверждает correctness.

Validation Boundary

Validation проверяет, но не исправляет.

Review Boundary

Review анализирует результат read-only.

Human Authority Boundary

Human decisions принимаются только человеком.

Git Boundary

Edit, commit, push, merge и release разделены.

Session Boundary

Новая session восстанавливает context, но не наследует скрытые permissions.

⸻

Journey Anti-Patterns

Immediate Execution

AOS начинает изменять files сразу после intent без bounded Task Brief.

Implicit Approval

AOS интерпретирует «продолжай» как разрешение на execution, commit и push одновременно.

Mixed Stage

Одна session планирует, изменяет, проверяет, исправляет и создаёт commit.

Validation Repair

Validation исправляет найденную проблему и затем сама объявляет PASS.

Hidden Unknown

Недоступная проверка не показывается пользователю.

Multiple Next Actions

Пользователь получает длинный список равнозначных рекомендаций.

Automatic Retry

Failure запускает новую попытку без решения человека.

Scope Expansion

Agent добавляет «полезные» изменения вне Task Brief.

Chat-Only State

Весь meaningful state остаётся только в conversation history.

Infrastructure Detour

Для одного bounded journey сначала строится registry, Control Plane или orchestration platform.

⸻

Journey Success Criteria

Primary User Journey является полезным, если пользователь может пройти один реальный cycle и после каждого этапа правильно ответить на вопросы:

1. Какая задача сейчас активна?
2. Какой stage выполняется или завершён?
3. Что разрешено изменять?
4. Что фактически изменено?
5. Какие проверки выполнены?
6. Какие проверки не запускались?
7. Какие findings существуют?
8. Есть ли unresolved unknown?
9. Какое решение требуется от человека?
10. Какое одно действие следует дальше?

Дополнительно:

* новая session восстанавливает context;
* execution и validation разделены;
* validation не исправляет;
* blocking finding вызывает stop;
* scope не расширяется;
* Git actions не выполняются неявно.

⸻

Journey Failure Criteria

Journey требует пересмотра, если:

* пользователь не понимает current stage;
* reports не помогают принять решение;
* Task Brief сложнее самой задачи;
* пользователь не различает PASS и approval;
* unknowns теряются;
* next action неоднозначен;
* session resume требует полного чтения history;
* система регулярно предлагает automation вместо product result;
* manual workflow вызывает больше overhead, чем снижает;
* correction loops происходят внутри одного stage;
* Git boundaries размыты;
* agent claims заменяют factual state.

⸻

Manual Journey Validation

До automation Primary User Journey должен быть проведён вручную минимум два, предпочтительно три раза.

Каждый cycle должен использовать реальную bounded task.

Следует наблюдать:

* где пользователь задаёт дополнительные вопросы;
* какие поля Task Brief реально нужны;
* какие сведения в reports избыточны;
* где пользователь теряет понимание;
* понятен ли human checkpoint;
* полезен ли one next action;
* возможно ли resume без chat history;
* какие steps повторяются стабильно;
* где требуется automation;
* где automation преждевременна.

Только повторяющиеся и понятные элементы могут становиться кандидатами на автоматизацию.

⸻

Minimal Journey

Минимальная реализация journey:

User states intent
→ AOS presents bounded Task Brief
→ user authorizes execution
→ agent performs one change
→ AOS presents Execution Report
→ user starts independent validation
→ validator presents Validation Report
→ user reviews result
→ AOS presents one next action
→ stop

Для первой проверки не требуются:

* dashboard;
* database;
* global registry;
* autonomous agents;
* automatic approval;
* automatic Git mutations;
* multi-project support;
* enterprise Governance;
* Runtime Enforcement.

⸻

Primary Journey Statement

Полная формулировка:

Primary User Journey позволяет человеку открыть project, понять current state, сформулировать intent, согласовать bounded task, отдельно разрешить execution, получить factual Execution Report, провести independent validation, принять human decision и завершить этап с одним следующим действием.

Сокращённая формулировка:

Пользователь проходит одно изменение от намерения до проверенного и понятного результата без потери human control.

⸻

Проверочный вопрос для будущих Features

Каждая будущая feature должна отвечать:

Какой конкретный шаг Primary User Journey она улучшает?

Если feature:

* не сокращает неопределённость;
* не улучшает boundary visibility;
* не делает результат проверяемее;
* не поддерживает session continuity;
* не упрощает human decision;
* не делает next action понятнее,

она не должна становиться prerequisite первого Product Runtime.

⸻

Краткое резюме

Точка входа

Пользователь открывает project и видит current state.

Намерение

Пользователь формулирует желаемое изменение.

Ограничение задачи

AOS помогает создать bounded Task Brief.

Human Decision

Пользователь отдельно разрешает execution.

Execution

Agent выполняет один stage в allowed scope.

Reporting

Пользователь получает factual Execution Report.

Validation

Отдельная read-only session проверяет результат.

Review

Пользователь рассматривает facts, findings и unknowns.

Direction

AOS показывает одно следующее действие.

Stop

Текущий stage завершается без автоматического продолжения.

Основной outcome

Пользователь в любой момент понимает:

что происходит
что сделано
что проверено
что неизвестно
что требует решения
что делать дальше
