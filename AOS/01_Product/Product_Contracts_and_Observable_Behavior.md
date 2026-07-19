Product Contracts and Observable Behavior

Назначение документа

Этот документ определяет основные Product Contracts первой версии AOS и связывает их с observable behavior.

Product Contract описывает не внутреннюю реализацию, а обязательное внешнее поведение продукта.

Он отвечает на вопросы:

* что пользователь вправе ожидать от AOS;
* какие состояния и границы должны быть видимы;
* какое поведение является допустимым;
* какое поведение нарушает product promise;
* какие claims должны подтверждаться фактами;
* где требуется human decision;
* когда workflow обязан остановиться.

Документ не определяет:

* architecture;
* API;
* database;
* formal schema;
* internal state machine;
* agent framework;
* implementation language;
* UI framework;
* storage format;
* Control Plane;
* registry;
* Runtime Enforcement;
* implementation plan.

Product Contracts должны оставаться применимыми независимо от выбранной технической реализации.

⸻

Что такое Product Contract

Product Contract — это проверяемое обязательство продукта перед пользователем.

Он связывает:

user expectation
→ system behavior
→ observable result
→ acceptance check

Product Contract считается полезным только тогда, когда его можно проверить через наблюдаемое поведение.

Недостаточно написать:

Система безопасна.

Необходимо определить:

* какую boundary система защищает;
* какое действие запрещено;
* при каком условии;
* что увидит пользователь;
* как проверить, что запрещённое действие не произошло.

⸻

Product Contract и Internal Mechanism

Один Product Contract может быть реализован разными способами.

Например, Contract:

После завершения stage пользователь получает одно следующее действие.

Он может быть реализован через:

* chat response;
* Markdown report;
* terminal command;
* web interface;
* local application;
* workflow service.

Контракт не должен зависеть от конкретного механизма, если механизм не является частью observable user value.

⸻

Product Contract и Claim

Product Contract не является claim о текущей готовности продукта.

Наличие этого документа означает:

expected behavior defined

Это не означает:

behavior implemented
behavior validated
behavior accepted
product ready

Сохраняются инварианты:

Skeleton ≠ implementation.
Documentation ≠ technical completion.
PASS ≠ approval.
Evidence ≠ approval.
CI PASS ≠ approval.

⸻

Contract 1 — Current State Visibility

Обязательство

AOS должен показывать пользователю текущее состояние active workflow в компактной и понятной форме.

Минимально должны быть видимы:

* active project;
* repository;
* branch;
* baseline, если он применим;
* active task;
* current stage;
* last completed stage;
* current result;
* blocking status;
* pending human decision;
* next required action.

Observable Behavior

Пользователь может открыть или возобновить project и получить summary вида:

Project: AOS
Active task: Rewrite Product Contract document
Current stage: VALIDATION
Last result: FAIL
Blocking finding: out-of-scope file changed
Pending human decision: REQUIRED
Next action: CREATE_CORRECTION_TASK

Нарушение Contract

Contract нарушен, если:

* current stage невозможно определить;
* active task существует только в chat history;
* execution result смешан с validation result;
* pending human decision не отображается;
* пользователь вынужден читать несколько документов, чтобы понять next action;
* устаревший state представлен как current.

Acceptance Direction

Пользователь должен правильно ответить:

1. Какая задача активна?
2. Какой stage текущий?
3. Что завершено?
4. Что блокирует продолжение?
5. Что требуется дальше?

⸻

Contract 2 — Intent Is Not Execution

Обязательство

Исходное пользовательское намерение не должно автоматически интерпретироваться как разрешение изменять project artifacts.

Observable Behavior

После сообщения:

Исправь описание Product Runtime.

AOS сначала определяет:

* intent;
* target;
* expected result;
* существенные unknowns;
* необходимость Task Brief.

Система не начинает execution, пока не выполнены необходимые границы.

Инварианты

Intent ≠ Task Brief.
Intent ≠ approval.
Intent ≠ execution authorization.

Нарушение Contract

Contract нарушен, если:

* files изменяются сразу после общего intent;
* agent сам выбирает расширенный scope;
* планирование и execution происходят неразделимо;
* пользователь не видит, что именно будет изменено.

Acceptance Direction

До execution пользователь должен иметь возможность понять и ограничить будущую задачу.

⸻

Contract 3 — Bounded Task

Обязательство

Каждый execution stage должен опираться на bounded Task Brief.

Минимально Task Brief должен определять:

* goal;
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

Перед execution пользователь видит:

Allowed:
- one target Markdown file
Forbidden:
- all adjacent files
- YAML metadata
- lifecycle updates
- implementation
- commit
- push
Validation:
- target-only diff
- Markdown structure
- no approval claims

Нарушение Contract

Contract нарушен, если:

* scope описан неопределённо;
* отсутствует forbidden scope;
* validation не определена;
* agent может самостоятельно расширить scope;
* target artifacts неизвестны;
* stop conditions отсутствуют.

Product Rule

Plan output ≠ Task Brief.
Task Brief ≠ approval.
Task Brief ≠ execution authorization.

⸻

Contract 4 — Explicit Human Authority

Обязательство

Все обязательные human decisions должны приниматься человеком явно.

AOS не должен симулировать:

* approval;
* acceptance;
* authorization;
* Risk Profile assignment;
* destructive permission;
* commit permission;
* push permission;
* merge permission;
* release permission.

Observable Behavior

При необходимости решения система показывает:

Human decision: REQUIRED
Execution authorized: false
Next action: AUTHORIZE_EXECUTION

При отсутствии решения workflow останавливается.

Нарушение Contract

Contract нарушен, если approval выводится из:

* PASS;
* Evidence;
* CI;
* текста Task Brief;
* предыдущего решения;
* отсутствия ответа;
* optimistic assumption;
* agent recommendation.

Инвариант

Human approval cannot be simulated.

⸻

Contract 5 — Risk Profile Is Human-Assigned

Обязательство

Agent может предложить Risk Profile, но не может назначить его самостоятельно.

Observable Behavior

Система может показать:

Proposed Risk Profile: MEDIUM
Reason:
- production code change;
- limited file scope;
- no dependency changes;
- no destructive operations.
Assigned Risk Profile: UNASSIGNED
Next action: ASSIGN_RISK_PROFILE

Нарушение Contract

Contract нарушен, если:

* proposed profile автоматически становится assigned;
* agent повышает свои permissions на основании собственного reasoning;
* отсутствие profile интерпретируется как низкий риск;
* execution начинается до обязательного назначения.

Product Rule

Proposed Risk Profile ≠ assigned Risk Profile.

⸻

Contract 6 — One Run, One Stage

Обязательство

Один agent run должен выполнять один определённый stage.

Основные stages:

* planning;
* execution;
* validation;
* review.

Observable Behavior

Перед началом run видимы:

* current stage;
* role;
* permissions;
* writable scope;
* stop condition.

После завершения:

stage result
→ report
→ one next action
→ stop

Нарушение Contract

Contract нарушен, если один run:

* планирует;
* изменяет files;
* проверяет результат;
* исправляет findings;
* создаёт commit;
* начинает следующий этап.

Product Rule

One run = one stage.

⸻

Contract 7 — Single Writer

Обязательство

В рамках одного execution stage должен существовать один writer.

Parallel write agents запрещены.

Observable Behavior

Пользователь видит, какой agent или session имеет write authority.

Другие agents могут:

* читать;
* анализировать;
* проверять;
* формировать findings.

Они не изменяют те же artifacts параллельно.

Нарушение Contract

Contract нарушен, если:

* два agents одновременно меняют один workspace;
* невозможно определить источник изменения;
* validation session имеет скрытое write permission;
* conflicting changes автоматически объединяются.

Acceptance Direction

Каждое изменение должно иметь понятный execution source.

⸻

Contract 8 — Scope Enforcement

Обязательство

Execution изменяет только artifacts и действия, перечисленные в allowed scope.

Scope не расширяется без explicit human permission.

Observable Behavior

При необходимости out-of-scope изменения:

Result: BLOCKED
Finding: required change is outside allowed scope
Out-of-scope changes performed: NONE
Next action: REVISE_TASK_BRIEF

Нарушение Contract

Contract нарушен, если agent:

* делает соседний refactoring;
* обновляет unrelated documentation;
* добавляет dependency;
* меняет architecture;
* создаёт дополнительные artifacts;
* выполняет Git action вне scope.

Инвариант

Scope does not expand without explicit human permission.

⸻

Contract 9 — Protected and Canonical Boundary

Обязательство

Изменения protected или canonical artifacts требуют отдельного human checkpoint.

Observable Behavior

Если task затрагивает protected artifact, AOS показывает:

* protected target;
* причина защиты;
* proposed change boundary;
* required human checkpoint;
* execution status.

До решения:

execution_authorized: false
result: HUMAN_REVIEW_REQUIRED

Нарушение Contract

Contract нарушен, если:

* protected file изменяется как часть routine task;
* approval предполагается из общего intent;
* соседнее разрешение распространяется на canonical change;
* agent сам снимает protected status.

⸻

Contract 10 — Destructive Operations Require Explicit Authorization

Обязательство

Destructive operations выполняются только после явного human authorization.

К ним могут относиться:

* delete;
* reset;
* clean;
* force push;
* destructive migration;
* overwrite without recovery;
* branch deletion;
* irreversible external mutation.

Observable Behavior

До destructive action система показывает:

* точное действие;
* target;
* последствия;
* rollback possibility;
* authorization state.

Без разрешения:

Result: BLOCKED
Next action: AUTHORIZE_DESTRUCTIVE_OPERATION

Нарушение Contract

Contract нарушен, если destructive operation:

* выполняется как cleanup;
* считается implied;
* объединяется с execution authorization;
* скрывается внутри команды или script;
* запускается автоматически после failure.

⸻

Contract 11 — Factual Execution Reporting

Обязательство

После execution пользователь получает factual Execution Report.

Report должен отделять:

* выполненные действия;
* изменённые artifacts;
* невыполненные действия;
* assumptions;
* findings;
* unknowns;
* checks;
* Git actions;
* next action.

Observable Behavior

Пример:

Stage: EXECUTION
Result: PASS
Changed files:
- AOS/01_Product/Product_Contracts_and_Observable_Behavior.md
Validation: NOT_RUN
Scope conflict: NO
Git actions: NONE
Next action: RUN_INDEPENDENT_VALIDATION

Нарушение Contract

Contract нарушен, если report:

* говорит только «готово»;
* не перечисляет changed files;
* не показывает validation state;
* скрывает unknowns;
* заявляет acceptance;
* не показывает Git actions;
* не содержит next action.

⸻

Contract 12 — Validation Is Independent and Read-Only

Обязательство

Validation должна выполняться отдельно от execution и не должна исправлять проверяемый artifact.

Observable Behavior

До validation видимы:

* target;
* candidate identity;
* checks;
* read-only boundary;
* stop conditions.

После validation:

* files modified during validation: 0;
* result;
* findings;
* unknowns;
* NOT_RUN checks;
* next action.

Нарушение Contract

Contract нарушен, если validation:

* исправляет finding;
* меняет test;
* обновляет documentation;
* повторяется автоматически;
* начинает correction;
* объявляет acceptance;
* выполняется внутри execution stage без явной boundary.

Product Rule

Validation checks.
Validation does not repair.

⸻

Contract 13 — Result State Semantics

Обязательство

AOS должен использовать результаты с однозначным значением.

Минимальный набор:

PASS
FAIL
UNKNOWN
NOT_RUN
BLOCKED

PASS

Обязательные проверки в заявленной boundary завершились успешно.

PASS не означает:

* approval;
* acceptance;
* global correctness;
* readiness;
* merge authorization;
* release authorization.

FAIL

Хотя бы одно обязательное условие в заявленной boundary нарушено.

UNKNOWN

Необходимый факт невозможно подтвердить.

NOT_RUN

Проверка не запускалась.

BLOCKED

Stage не может быть продолжен из-за blocking condition.

Нарушение Contract

Contract нарушен, если:

* UNKNOWN показывается как safe;
* skipped check считается PASS;
* zero tests считается PASS;
* частичный успех обозначается как полный;
* статус не имеет определённой boundary.

Инварианты

UNKNOWN ≠ OK.
NOT_RUN ≠ PASS.
PASS ≠ approval.

⸻

Contract 14 — Honest Unknown Handling

Обязательство

Неизвестные факты должны отображаться явно.

AOS не должен скрывать unknowns ради ощущения progress.

Observable Behavior

Пример:

Baseline: UNKNOWN
Impact: execution boundary cannot be confirmed
Result: UNKNOWN_BLOCKED
Next action: RESOLVE_BASELINE

Boundary-Limited Fail-Closed

Unknown должен блокировать только затронутую boundary.

Система не должна останавливать весь project, если неизвестный факт не влияет на текущую задачу.

Нарушение Contract

Contract нарушен, если:

* unknown заменяется assumption;
* система пишет likely safe;
* весь workflow глобально блокируется без необходимости;
* влияние unknown не объясняется;
* next action отсутствует.

⸻

Contract 15 — First Blocking Finding Stops the Stage

Обязательство

После первого blocking finding текущий stage должен завершиться report и stop.

Observable Behavior

Blocking finding detected
→ no further stage actions
→ report created
→ one next action
→ stop

Нарушение Contract

Contract нарушен, если agent:

* продолжает искать и исправлять другие проблемы;
* выполняет partial recovery;
* запускает новый stage;
* делает out-of-scope changes;
* автоматически повторяет попытку.

Product Outcome

Пользователь получает контролируемую остановку вместо непредсказуемого repair loop.

⸻

Contract 16 — No Automatic Retry

Обязательство

FAIL, BLOCKED или blocking finding не должны автоматически запускать повторную попытку.

Observable Behavior

После failure пользователь видит:

* result;
* finding;
* affected boundary;
* current repository state;
* next action.

Следующая попытка требует отдельного решения или новой bounded task.

Нарушение Contract

Contract нарушен, если:

* agent исправляет failure без review;
* validation запускается повторно после self-correction;
* несколько attempts скрываются за одним итоговым PASS;
* scope расширяется ради прохождения check.

⸻

Contract 17 — Correction Is a Separate Task

Обязательство

Correction после validation finding должна оформляться как отдельная bounded task.

Observable Behavior

После validation FAIL:

Current stage: VALIDATION
Result: FAIL
Artifact modified during validation: NO
Next action: CREATE_CORRECTION_TASK

Correction должна иметь:

* отдельный scope;
* requirements;
* validation;
* authorization;
* execution stage.

Нарушение Contract

Contract нарушен, если correction:

* выполняется validator;
* происходит до human review;
* не имеет Task Brief;
* использует старое execution authorization;
* скрывает предыдущий failure.

⸻

Contract 18 — Evidence Is Not Approval

Обязательство

Evidence подтверждает наблюдаемый факт, но не заменяет human decision.

Observable Behavior

AOS различает:

Evidence available: YES
Validation result: PASS
Human acceptance: NOT_RECORDED
Commit authorization: NOT_GRANTED

Нарушение Contract

Contract нарушен, если:

* Evidence автоматически закрывает review;
* test output считается approval;
* CI status считается merge decision;
* report подписывает решение вместо человека.

Инварианты

Evidence ≠ approval.
CI PASS ≠ approval.

⸻

Contract 19 — Git Actions Are Separate Decisions

Обязательство

Git actions должны быть разделены.

Edit ≠ commit.
Commit ≠ push.
Push ≠ merge.
Merge ≠ release.

Observable Behavior

После accepted result система может показать:

Working tree changes: PRESENT
Human acceptance: RECORDED
Commit authorization: NOT_GRANTED
Next action: AUTHORIZE_COMMIT

После commit:

Commit created: YES
Push authorization: NOT_GRANTED
Next action: REVIEW_PUSH_DECISION

Нарушение Contract

Contract нарушен, если:

* execution authorization включает commit;
* commit authorization включает push;
* push включает merge;
* merge включает release;
* Git actions выполняются по умолчанию.

⸻

Contract 20 — One Next Action

Обязательство

После каждого завершённого stage AOS показывает ровно одно основное следующее действие.

Observable Behavior

Примеры:

REVIEW_TASK_BRIEF
AUTHORIZE_EXECUTION
RUN_INDEPENDENT_VALIDATION
REVIEW_FINDING
CREATE_CORRECTION_TASK
AUTHORIZE_COMMIT
STOP

Нарушение Contract

Contract нарушен, если пользователь получает:

* несколько равнозначных вариантов;
* длинный список recommendations;
* следующий roadmap;
* скрытый multi-step command;
* действие, которое объединяет несколько authorizations.

Неправильно:

Review, correct if needed, commit, push and continue.

Правильно:

REVIEW_VALIDATION_FINDING

⸻

Contract 21 — Explicit Stop

Обязательство

После report текущий run должен остановиться.

Observable Behavior

Stage: VALIDATION
Result: PASS
Next action: REVIEW_RESULT
Run state: STOPPED

Нарушение Contract

Contract нарушен, если система автоматически:

* начинает review;
* создаёт correction;
* выполняет commit;
* запускает следующий task;
* продолжает до terminal success.

Product Rule

Stage complete
→ report
→ one next action
→ stop

⸻

Contract 22 — Session Continuity

Обязательство

Новая session должна восстанавливать минимальный factual context текущего workflow.

Минимальный Handoff State

* project;
* repository;
* branch;
* baseline;
* active task;
* Task Brief;
* last completed stage;
* stage result;
* findings;
* unknowns;
* Git state;
* recorded human decisions;
* pending human decisions;
* next required action.

Observable Behavior

После команды продолжения пользователь получает:

Last completed stage: VALIDATION
Result: FAIL
Blocking finding: scope violation
Pending decision: correction direction
Next action: CREATE_CORRECTION_TASK

Нарушение Contract

Contract нарушен, если:

* пользователь должен пересказать весь chat;
* прошлые permissions наследуются неявно;
* stage выполняется повторно без необходимости;
* next action теряется;
* handoff объявляет approval.

Product Rule

Resume ≠ authorization.

⸻

Contract 23 — Repository-First Factual State

Обязательство

Фактическое состояние files и Git должно определяться из repository и Git, а не из agent memory или chat claim.

Observable Behavior

AOS различает:

* repository-observed fact;
* report claim;
* user statement;
* unknown;
* conflict.

Пример

Agent claim: file unchanged
Repository observation: file modified
Resolved factual state: MODIFIED
Conflict: RECORDED

Нарушение Contract

Contract нарушен, если:

* chat summary считается точнее Git;
* outdated report переопределяет current diff;
* current branch предполагается без проверки;
* baseline берётся из памяти session.

⸻

Contract 24 — One Source of Truth per Fact Class

Обязательство

Для каждого класса фактов должен существовать один authoritative source.

Пример распределения:

* repository и Git — files, branch, commits, diff;
* Task Brief — scope, requirements, stop conditions;
* Stage Report — заявленный результат stage;
* Validation Evidence — выполненные checks;
* human record — решения человека.

Observable Behavior

При конфликте AOS показывает:

* conflicting sources;
* правило приоритета;
* resolved fact или UNKNOWN;
* affected boundary.

Нарушение Contract

Contract нарушен, если:

* несколько документов одновременно объявлены authoritative;
* chat и report имеют одинаковый приоритет;
* conflict скрывается;
* источник факта невозможно определить.

⸻

Contract 25 — Progressive Disclosure

Обязательство

AOS должен показывать пользователю сначала operational summary, сохраняя доступ к technical details.

Default View

* current stage;
* result;
* blocking status;
* pending decision;
* next action.

Detailed View

* paths;
* baseline;
* diff;
* commands;
* exit codes;
* tests;
* raw findings;
* Evidence references.

Нарушение Contract

Contract нарушен, если:

* non-programmer обязан читать raw terminal output;
* technical details скрыты полностью;
* summary упрощает состояние до ложного OK;
* critical unknown доступен только в details.

⸻

Contract 26 — Claims Must Be Boundary-Specific

Обязательство

Каждый claim должен относиться к конкретной boundary.

Правильно:

Target Markdown document passed the declared structure checks.

Неправильно:

Project is correct and ready.

Observable Behavior

Result сопровождается:

* target;
* checks;
* scope;
* excluded boundaries;
* unknowns.

Нарушение Contract

Contract нарушен, если используются неопределённые claims:

* ready;
* safe;
* complete;
* production-ready;
* fully validated;
* approved,

без точного определения boundary и human decision.

⸻

Contract 27 — No False Readiness

Обязательство

AOS не должен заявлять readiness на основании неполных или несвязанных сигналов.

Недостаточные основания

Сами по себе не доказывают readiness:

* documentation complete;
* skeleton exists;
* tests pass;
* CI PASS;
* Evidence collected;
* report generated;
* code compiles;
* agent says complete.

Observable Behavior

Система должна показывать отдельные факты:

Documentation: PRESENT
Implementation: NOT_CONFIRMED
Validation: PARTIAL
Human acceptance: NOT_RECORDED
Release authorization: NOT_GRANTED

Нарушение Contract

Contract нарушен, если несколько частичных результатов объединяются в общий статус READY.

⸻

Contract 28 — Minimal Safety Floor from the Start

Обязательство

Первая версия должна соблюдать минимальные safety boundaries без обязательного построения полного Governance.

Минимально:

* human authority;
* bounded scope;
* stage separation;
* explicit unknowns;
* protected boundary;
* destructive authorization;
* Git separation;
* one writer;
* one next action;
* stop behavior.

Нарушение Contract

Contract нарушен, если безопасность полностью откладывается до позднего Governance.

Одновременно Contract нарушен, если ради одной bounded task создаётся избыточная control infrastructure.

Product Principle

Minimal Safety Floor
+
minimal product workflow
before
full Governance

⸻

Contract 29 — Manual Before Automation

Обязательство

Workflow сначала должен быть подтверждён manual cycles.

Observable Behavior

До автоматизации существует возможность вручную провести:

* intent capture;
* Task Brief;
* execution authorization;
* execution;
* reporting;
* validation;
* human review;
* handoff;
* stop.

Нарушение Contract

Contract нарушен, если automation создаётся до того, как:

* понятны contracts;
* workflow повторялся;
* boundaries подтверждены;
* failure behavior проверено;
* human checkpoints признаны полезными.

⸻

Contract 30 — Legacy Is Reference, Not Authority

Обязательство

AOS-FARM и AgentOS/AOS-1 могут использоваться как reference material, но не управляют текущими Product Contracts.

Допустимое использование

Можно извлекать:

* product intent;
* lessons;
* failure modes;
* useful patterns;
* negative examples;
* validated concepts.

Запрещённое использование

Нельзя автоматически переносить:

* legacy topology;
* Control Plane;
* registry;
* lifecycle complexity;
* authority model;
* dependencies;
* autonomous workflows;
* historical Source of Truth hierarchy.

Observable Behavior

Каждое заимствование должно быть оправдано текущим Product Outcome.

⸻

Contract 31 — Replaceable Internals

Обязательство

Product Contracts не должны зависеть от конкретного provider или внутреннего компонента без product necessity.

Observable Behavior

Execution Agent может быть заменён, если новый agent соблюдает те же contracts:

* bounded scope;
* one stage;
* factual report;
* stop;
* no simulated authority.

Нарушение Contract

Contract нарушен, если product behavior существует только благодаря скрытым особенностям одной модели или одной chat session.

⸻

Contract 32 — Configuration Mismatch Blocks Execution

Обязательство

Если требуемая configuration недоступна, система не должна автоматически снижать требования.

Configuration может включать:

* model;
* reasoning level;
* sandbox;
* workspace permissions;
* network access;
* validation capability.

Observable Behavior

Required configuration: read-only validation
Available configuration: workspace-write
Result: BLOCKED
Next action: RESOLVE_CONFIGURATION

Нарушение Contract

Contract нарушен, если система автоматически:

* downgrades model;
* lowers reasoning;
* expands sandbox;
* enables network;
* changes required role.

⸻

Contract 33 — Network Boundary

Обязательство

Network access должен быть явным и минимально необходимым.

Observable Behavior

Перед stage видимы:

Network access: DISABLED

или:

Network access: ENABLED
Purpose: retrieve exact dependency metadata
Allowed targets: defined

Нарушение Contract

Contract нарушен, если:

* network включается автоматически;
* scope доступа не определён;
* external mutation происходит без authorization;
* результаты сети представлены как repository facts без проверки.

⸻

Contract 34 — Secrets Boundary

Обязательство

Secrets не должны попадать в:

* repository;
* reports;
* Evidence;
* logs;
* prompts;
* temporary outputs;
* generated examples.

Observable Behavior

При обнаружении secret-like data:

* stage останавливается в затронутой boundary;
* значение не воспроизводится;
* finding фиксируется безопасно;
* next action указывает на remediation.

Нарушение Contract

Contract нарушен, если secret копируется в report или chat.

⸻

Contract 35 — Temporary Workspace Is Disposable

Обязательство

Temporary outputs хранятся только в:

/.aos-tmp/

и считаются disposable.

Там нельзя хранить:

* Evidence;
* approvals;
* checkpoints;
* canonical files;
* final reports;
* durable decisions.

Observable Behavior

Temporary artifacts можно удалить без потери authoritative project state.

Нарушение Contract

Contract нарушен, если workflow зависит от temporary file как от единственного Source of Truth.

⸻

Contract 36 — Shortest Safe Path

Обязательство

AOS должен выбирать минимальный путь, который:

* достигает Product Outcome;
* сохраняет mandatory safety boundaries;
* не расширяет scope;
* не добавляет преждевременную infrastructure;
* остаётся проверяемым.

Observable Behavior

Для одного documentation change AOS не требует:

* registry;
* database;
* Control Plane;
* complex lifecycle;
* autonomous orchestration.

Но сохраняет:

* Task Brief;
* execution decision;
* target-only scope;
* validation;
* human review;
* Git boundaries.

Нарушение Contract

Contract нарушен, если система:

* выбирает наиболее сложный процесс по умолчанию;
* устраняет все возможные риски глобально;
* строит infrastructure до user value;
* пропускает обязательную safety boundary ради скорости.

⸻

Cross-Contract Invariants

Все Product Contracts применяют полный canonical invariant set из [`Minimal Safety Floor`](../00_Core/Minimal_Safety_Floor.md#всегда-действующие-инварианты).

Domain-specific contract rule: каждый claim должен связывать user expectation, observable behavior и проверяемую acceptance boundary; механизм реализации не создаёт новый product promise.

Operational boundaries:

One run = one stage.
Validation does not repair.
Review is read-only.
Scope does not expand without explicit permission.
First blocking finding → report → one next action → stop.

⸻

Observable Behavior Matrix

Situation	Required observable behavior
User states broad intent	Clarify intent; do not execute
Task scope incomplete	PLANNING_REQUIRED
Task Brief prepared	Show scope and validation; do not execute
Risk Profile unassigned	HUMAN_REVIEW_REQUIRED or BLOCKED
Execution authorized	Run one execution stage
Scope expansion required	Stop and report conflict
Execution completed	Produce Execution Report
Validation requested	Start separate read-only stage
Validation finds defect	Report FAIL; do not repair
Required fact unavailable	Show UNKNOWN or UNKNOWN_BLOCKED
Check not executed	Show NOT_RUN
Blocking finding	Report and stop
Validation PASS	Show technical result; no approval claim
Human acceptance absent	Show NOT_RECORDED
Commit not authorized	Do not commit
Session resumed	Show current state; do not auto-continue
Configuration mismatch	BLOCKED; no automatic downgrade
Stage completed	Show one next action and stop

⸻

Product Contract Priorities

При конфликте product behaviors используется следующий порядок:

1. Human authority.
2. Protected and destructive boundaries.
3. Scope integrity.
4. Factual state and honest unknown handling.
5. Stage separation.
6. Validation independence.
7. Session continuity.
8. One next action.
9. Convenience and automation.

Удобство не должно переопределять human authority или safety boundary.

Automation не должна переопределять factual truth.

Progress не должен достигаться за счёт скрытого scope expansion.

⸻

Contract Failure Handling

Если Product Contract нарушен во время stage, AOS должен:

1. определить затронутый Contract;
2. остановить действия в этой boundary;
3. не скрывать нарушение;
4. зафиксировать фактический state;
5. сформировать finding;
6. показать impact;
7. указать одно следующее действие;
8. остановиться.

Contract violation не должен автоматически запускать correction.

⸻

Contract Validation Direction

Product Contracts должны проверяться через реальные user journeys.

Для каждого Contract необходимо определить:

* trigger;
* expected behavior;
* forbidden behavior;
* observable evidence;
* negative case;
* stop behavior.

Пример для Scope Contract:

Trigger

Execution требует соседний file.

Expected Behavior

Agent останавливается и сообщает scope conflict.

Forbidden Behavior

Agent изменяет соседний file.

Evidence

Target-only diff и Execution Report.

Negative Case

Out-of-scope artifact намеренно необходим для завершения задачи.

Expected Result

BLOCKED, а не расширенный execution.

⸻

Minimum Contract Set for First Vertical Slice

Для первого working Product Runtime обязательны:

1. Current State Visibility.
2. Intent Is Not Execution.
3. Bounded Task.
4. Explicit Human Authority.
5. One Run, One Stage.
6. Scope Enforcement.
7. Factual Execution Reporting.
8. Independent Read-Only Validation.
9. Honest Result States.
10. First Blocking Finding Stops the Stage.
11. Evidence Is Not Approval.
12. Git Actions Are Separate Decisions.
13. One Next Action.
14. Explicit Stop.
15. Session Continuity.
16. Repository-First Factual State.

Остальные Contracts могут расширять или уточнять это ядро, но не должны задерживать первый vertical slice без доказанной необходимости.

⸻

Что не требуется для соблюдения Contracts

Product Contracts первой версии не требуют автоматически:

* database;
* registry;
* workflow engine;
* policy engine;
* distributed system;
* multi-agent scheduler;
* cryptographic authorization;
* global lifecycle model;
* enterprise IAM;
* cloud deployment;
* rich dashboard;
* autonomous recovery;
* automatic merge;
* Runtime Enforcement.

Сначала Contracts могут быть подтверждены через:

* repository artifacts;
* explicit prompts;
* manual checkpoints;
* separate sessions;
* simple checks;
* human review.

⸻

Acceptance Direction

Документ Product Contracts содержательно достаточен, если для First Vertical Slice можно определить:

* обязательное observable behavior;
* запрещённое behavior;
* human boundaries;
* scope boundaries;
* validation boundaries;
* unknown semantics;
* failure behavior;
* Git boundaries;
* continuity behavior;
* stop behavior.

Это не означает, что Contracts реализованы или validated.

⸻

Product Contract Statement

Полная формулировка:

AOS должен управлять одним AI-assisted development cycle через видимые boundaries, factual state, bounded scope, independent validation, explicit human authority, honest unknown handling, одно следующее действие и обязательную остановку после каждого stage.

Сокращённая формулировка:

AOS не обещает автономность; он обещает понятный и контролируемый workflow.

⸻

Проверочный вопрос для Implementation

Для каждого будущего component следует задать:

Какой Product Contract он реализует и какое observable behavior подтверждает?

Если component нельзя связать с конкретным Contract, он не должен становиться prerequisite First Vertical Slice.

⸻

Краткое резюме

Product Contracts определяют

* что пользователь должен видеть;
* какие решения остаются за человеком;
* какие действия разрешены;
* какие состояния считаются честными;
* где workflow останавливается.

Основные обязательства

visible current state
+
bounded task
+
explicit human authority
+
one stage per run
+
scope enforcement
+
factual reports
+
independent validation
+
honest unknowns
+
separate Git decisions
+
one next action
+
stop
+
session continuity

Главная граница

Contracts должны сначала подтверждаться через observable manual workflow.

Полный Governance, automation, registry и Runtime Enforcement добавляются только после появления доказанной необходимости.
