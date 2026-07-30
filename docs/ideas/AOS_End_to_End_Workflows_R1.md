document_id: AOS-END-TO-END-WORKFLOWS
revision: R1
document_type: END_TO_END_WORKFLOW_CATALOG
status: DRAFT
authority: NONE
canonical_status: NOT_ASSIGNED
human_acceptance: NOT_REQUESTED
product_scope_effect: NONE
architecture_effect: NONE
implementation_authorization: NONE
execution_authorized: false
git_authorization: NONE
implementation_repository: UNASSIGNED
source_repository: NMF13579/notebook
source_branch_expected: dev
source_basis:

• project_chat_history_synthesis
• 00_AOS_Reconstruction_Project_Control_and_Source_Precedence
• 01_AOS_Documentation_Reconstruction_Workflow_and_Roadmap
• 02_AOS_Minimal_Safety_and_Authority_Rules
• 04_AOS_Model_Routing_and_Task_Decomposition_Research
• 05_AOS_FARM_Harness_Engineering_Reference
• 07_AOS_FARM_Proposed_Pipeline_Evolution
• 08_Architecture_Lifecycle_Integration_Plan
• AOS_Full_Feature_Catalog_R1
• AOS_Full_Feature_Catalog_From_Project_Chats_R1
created_from: available_project_chat_history_and_uploaded_sources
human_review_required: true

────────

AOS — End-to-End Workflows

0. Статус и назначение документа

Этот документ собирает в единую человекочитаемую систему сквозные процессы AOS: от появления идеи или подключения проекта до выполнения ограниченной задачи, технической проверки, решения человека, Git delivery, восстановления после остановки и последующего улучшения.

Документ отвечает на вопрос:

> **Как AOS должен проводить человека и агента через полный жизненный цикл работы, а не только выполнять отдельную функцию?**

Он не является:

• canonical workflow;
• утверждённой product architecture;
• roadmap;
• Task Brief;
• execution authorization;
• разрешением на dependency adoption;
• разрешением на Commit, Push, Merge или Release;
• доказательством существующей implementation.

Все целевые workflow и contracts, не подтверждённые current repository observation, имеют класс PROPOSAL. Исторические AOS-FARM, AOS-02 и AgentOS используются только как READ_ONLY_REFERENCE, authority: NONE.

────────

1. Главная модель

AOS должен соединять три разные системы работы, не смешивая их полномочия и результаты.

1.1 Product Runtime

Это путь пользователя, который применяет AOS для создания или изменения программного продукта:

```text
идея / проблема
→ уточнённый outcome
→ проектный контекст
→ Feature Passport / Specification
→ architecture и UX decisions при необходимости
→ vertical slice
→ bounded Task Brief
→ explicit Execution Authorization
→ scoped execution
→ validation
→ Evidence
→ human review
→ human decision
→ отдельная Git delivery
→ наблюдение и следующий цикл
```

1.2 AOS Development Factory

Это путь команды, создающей и развивающей сам AOS:

```text
проблема AOS
→ candidate feature
→ product-fit decision
→ contract
→ architecture proposal
→ bounded implementation task
→ EXECUTE
→ VALIDATE
→ REVIEW
→ human acceptance
→ отдельные Git/release decisions
→ dogfood
→ lessons и следующий improvement
```

1.3 Documentation Reconstruction

Это текущий процесс восстановления знаний, необходимых для воспроизведения AOS:

```text
source inventory
→ observations
→ product intent
→ features
→ user journeys
→ end-to-end workflows
→ contracts
→ states
→ acceptance tests
→ contradictions / unknowns
→ readiness audit
→ human transition decision
```

Эти контуры связаны, но не взаимозаменяемы:

```text
описание Product Runtime
≠ реализация Product Runtime

готовая документация
≠ готовый AOS

успешный workflow run
≠ human acceptance

human acceptance
≠ Merge или Release authorization
```

────────

2. Общие инварианты всех workflow

Каждый сквозной процесс AOS должен соблюдать следующие правила.

2.1 Authority

Только человек может:

• принять product scope;
• принять architecture;
• назначить Risk Profile;
• изменить Source of Truth;
• разрешить protected или destructive operation;
• разрешить execution;
• принять технический результат;
• разрешить Commit;
• разрешить Push;
• разрешить Merge;
• разрешить Release.

Agent может анализировать, создавать DRAFT, формировать варианты, Evidence и recommendation, но не может симулировать human decision.

2.2 Разделение результатов

```text
PASS ≠ approval
Evidence ≠ approval
CI PASS ≠ approval
Readiness ≠ authorization
Plan ≠ Task Brief
Task Brief ≠ Execution Authorization
Execution ≠ Validation
Validation ≠ Review
Review recommendation ≠ human decision
Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
UNKNOWN ≠ OK
NOT_RUN ≠ PASS
```

2.3 One run — one stage

Основные stages:

```text
PLAN → EXECUTE → VALIDATE → REVIEW
```

DELIVER является context package, а не самостоятельным разрешением или stage mutation.

Один run:

• не переходит автоматически к следующему stage;
• после completion, finding или failure создаёт report;
• останавливается;
• показывает один next_required_action.

2.4 Bound scope

До mutation должны быть известны:

• exact subject;
• repository / artifact;
• branch и baseline при работе с repository;
• allowed paths;
• forbidden paths;
• разрешённые operations;
• expected outputs;
• validation;
• stop conditions.

Scope не расширяется из-за того, что соседнее действие кажется полезным.

2.5 Durable artifacts

Каждый значимый результат должен иметь:

• stable ID;
• revision;
• status;
• exact subject;
• provenance;
• owner fact source;
• limitations;
• human-decision boundary;
• links к upstream и downstream artifacts.

Chat reply, temporary file и generated summary не становятся Source of Truth автоматически.

────────

3. Карта workflow

|ID     |Workflow                                                |Контур                     |Основной результат                       |
|-------|--------------------------------------------------------|---------------------------|-----------------------------------------|
|`WF-01`|Entry, Mode and Project Selection                       |Product Runtime / Control  |выбран правильный маршрут и subject      |
|`WF-02`|New Project Bootstrap and First Start                   |Product Runtime            |безопасно подготовленный новый проект    |
|`WF-03`|Existing Project Discovery and Capability Reconstruction|Product Runtime            |проверяемая карта существующего проекта  |
|`WF-04`|Problem / Idea Intake to Product Definition             |Product Runtime            |reviewable Product/Feature Passport      |
|`WF-05`|Architecture Decision                                   |Product Runtime            |human-selected architecture constraints  |
|`WF-06`|UX Skeleton to Vertical Slice                           |Product Runtime            |reviewed UX model и выбранный slice      |
|`WF-07`|Backlog, Lazy Decomposition and Task Brief              |Product Runtime            |одна исполнимая bounded задача           |
|`WF-08`|Repository Preflight and Execution Authorization        |Control                    |exact candidate и отдельная authorization|
|`WF-09`|Controlled Execution                                    |Product Runtime / Execution|одна ограниченная mutation и Stage Report|
|`WF-10`|Validation, Evidence, Review and Human Decision         |Quality                    |технический verdict и решение человека   |
|`WF-11`|Correction, Recovery and Resume                         |Recovery                   |безопасное продолжение без скрытого retry|
|`WF-12`|Git Delivery and Release                                |Delivery                   |отдельно разрешённая доставка результата |
|`WF-13`|Observability and Continuous Improvement                |Operations                 |новый bounded improvement input          |
|`WF-14`|AOS Feature Development                                 |AOS Development Factory    |принятая или отклонённая capability AOS  |
|`WF-15`|Documentation Reconstruction                            |Knowledge Factory          |пакет знаний для воспроизведения AOS     |

────────

4. WF-01 — Entry, Mode and Project Selection

4.1 Назначение

Определить, что именно хочет сделать человек, с каким проектом и на каком уровне полномочий. AOS не должен начинать planning или execution до выбора правильного режима.

4.2 Типовые triggers

• «Хочу создать новый проект».
• «Подключи AOS к существующему repository».
• «Хочу добавить фичу».
• «Исправь конкретную ошибку».
• «Проверь готовый результат».
• «Продолжи с места остановки».
• «Подготовь commit / PR».
• «Нужно спроектировать сам AOS».
• «Нужно восстановить документацию по истории».

4.3 Минимальные входы

• user intent;
• target project или repository;
• desired outcome;
• известная текущая стадия;
• запрошенный вид действия: analysis, planning, mutation, validation, review или Git delivery;
• ограничения пользователя.

4.4 Flow

```text
user request
→ classify target
→ classify requested action
→ resolve known context
→ identify missing material context
→ select workflow
→ show current status
→ show one next action
```

AOS должен различать:

```text
новый продукт
существующий продукт
сам AOS
documentation reconstruction
read-only review
mutation
Git delivery
```

4.5 Outputs

• Interaction Context;
• selected workflow ID;
• exact subject;
• current stage;
• required human decision, если она отсутствует;
• один next_required_action.

4.6 Failure behavior

AOS не должен:

• запускать generic planning, если задача уже полностью определена;
• считать repository из прошлого чата текущим без проверки mutable facts;
• переходить к execution из-за слова «сделай», если protected boundary неизвестна;
• смешивать validation и correction;
• интерпретировать просьбу «подготовь PR» как разрешение на merge.

4.7 Exit condition

Workflow завершён, когда выбран один следующий маршрут и его preconditions известны либо явно отмечены как UNKNOWN/BLOCKED.

────────

5. WF-02 — New Project Bootstrap and First Start

5.1 Назначение

Подготовить новый consumer project к работе с AOS без скрытой установки, перезаписи пользовательских данных и преждевременного создания тяжёлой инфраструктуры.

5.2 Trigger

Пользователь создаёт новый программный проект и хочет использовать AOS как управляемую среду разработки.

5.3 Inputs

• project name и problem domain;
• target repository или решение о его создании;
• выбранный минимальный AOS distribution;
• environment constraints;
• разрешённые files/directories;
• network и dependency permissions;
• existing user state, если repository не пуст.

5.4 Proposed flow

```text
bootstrap request
→ environment and destination preflight
→ install dry run / preview
→ conflict and overwrite report
→ human confirmation
→ safe apply или manual transfer
→ self-test
→ doctor
→ first-start guide
→ project intent intake
```

5.5 Observable outputs

• installation preview;
• destination inventory;
• conflict report;
• applied file list;
• self-test report;
• doctor report;
• First Start status;
• next product-intake action.

5.6 Safety rules

• dry-run не изменяет project;
• apply выполняется только после отдельного подтверждения;
• unknown existing file не перезаписывается молча;
• generated scaffold не считается working product;
• doctor PASS не является approval проекта;
• network/dependencies не включаются неявно;
• installer не меняет Git state без отдельного разрешения.

5.7 Exit conditions

Возможные результаты:

• BOOTSTRAP_READY_FOR_PRODUCT_INTAKE;
• BLOCKED_DESTINATION_CONFLICT;
• BLOCKED_ENVIRONMENT;
• MANUAL_TRANSFER_REQUIRED;
• UNKNOWN_EXISTING_STATE.

────────

6. WF-03 — Existing Project Discovery and Capability Reconstruction

6.1 Назначение

Понять существующий проект до предложения задач. Этот workflow не исправляет project автоматически.

6.2 Trigger

• AOS подключается к уже существующему repository;
• документация и code расходятся;
• пользователь не уверен, что реализовано;
• требуется план дальнейшей разработки;
• проект нужно продолжить после длительной паузы.

6.3 Inputs

• repository identity;
• branch / HEAD / baseline;
• allowed inspection scope;
• доступные product documents;
• code, tests, schemas и CI;
• user-declared goals;
• excluded/private areas.

6.4 Flow

```text
repository preflight
→ repository inventory
→ documentation scan
→ code and schema scan
→ test and CI scan
→ dependency inventory
→ workflow discovery
→ capability observations
→ docs↔code↔tests comparison
→ conflicts / gaps / unknowns
→ capability map
→ human review
→ selected next product action
```

6.5 Claim classes

Каждый finding классифицируется:

• FACT / current observation;
• REPORTED;
• INFERENCE;
• PROPOSAL;
• CONFLICT;
• NOT_FOUND;
• UNKNOWN;
• NOT_RUN;
• BLOCKED.

Наличие файла не доказывает behavior. Исторический report не доказывает current state.

6.5.2 Outputs

• Project Inventory;
• Capability Map;
• Documentation Drift Report;
• Architecture Reconstruction Candidate;
• Dependency Inventory;
• Initial Risk Register;
• Gap and Conflict Register;
• proposed next Feature/Task candidates.

6.7 Human checkpoint

Человек решает:

• какие observations считать достаточными;
• что является product priority;
• какие gaps нужно закрывать;
• требуется ли architecture recovery;
• допустима ли mutation;
• какой Risk Profile назначить следующей задаче.

6.8 Exit condition

Discovery заканчивается не «полным знанием всего repository», а когда закрыт заявленный вопрос и появился один bounded следующий action.

────────

7. WF-04 — Problem / Idea Intake to Product Definition

7.1 Назначение

Преобразовать свободное описание идеи в проверяемую product boundary, не переходя преждевременно к technology или task list.

7.2 Trigger

• новая идея;
• запрос пользователя;
• improvement candidate;
• observation из эксплуатации;
• feature proposal из Idea Bank;
• gap из discovery.

7.3 Flow

```text
raw idea
→ problem clarification
→ target user
→ context and current workaround
→ desired outcome
→ success signal
→ constraints and non-goals
→ unknowns and assumptions
→ duplicate / overlap check
→ Feature Passport candidate
→ human product-fit decision
```

7.4 Required questions

AOS должен установить:

1. Кто испытывает проблему?
2. В каком контексте?
3. Что пользователь пытается получить?
4. Почему текущий способ недостаточен?
5. Как будет выглядеть observable success?
6. Что явно не входит в scope?
7. Какие данные, permissions и providers затрагиваются?
8. Что неизвестно?
9. Есть ли существующая feature, которая уже покрывает проблему?
10. Требуется ли architecture или UX decision?

7.5 Outputs

• Problem Record;
• Feature Passport;
• actors;
• outcome;
• scope / non-goals;
• acceptance intent;
• unknowns;
• proposed disposition:
  • REQUIRED;
  • OPTIONAL;
  • DEFERRED;
  • REFERENCE_ONLY;
  • REJECTED;
  • UNDECIDED.

7.6 Non-grants

Feature Passport:

• не утверждает feature;
• не выбирает architecture;
• не создаёт Task Brief;
• не разрешает implementation;
• не создаёт Git permission.

7.7 Exit condition

Появился reviewable product artifact и explicit human product disposition либо HUMAN_REVIEW_REQUIRED.

────────

8. WF-05 — Architecture Decision

8.1 Назначение

Отделить material architecture choices от task generation. Простая reversible задача не должна автоматически получать тяжёлый architecture stage.

8.2 Architecture Need Check

Architecture workflow нужен, если присутствует хотя бы один material factor:

• новый runtime boundary;
• persistent storage;
• external provider;
• security/privacy boundary;
• dependency с долгосрочным lock-in;
• cross-repository integration;
• shared schema/API;
• migration;
• material performance/reliability requirement;
• изменение Source of Truth ownership.

Если material choice отсутствует:

```text
ARCHITECTURE_NOT_REQUIRED_WITH_REASON
```

8.3 Flow

```text
accepted/reviewable Specification
→ Architecture Need Check
→ Architecture Input
→ constraints and quality attributes
→ option generation
→ dependency/license/security analysis
→ trade-off comparison
→ unknown/conflict register
→ recommendation
→ Human Architecture Checkpoint
→ accepted ADR or revision request
→ architecture constraints export
```

8.4 Outputs

• Architecture Brief;
• architecture options;
• fit matrix;
• Evidence package;
• ADR candidate;
• human decision record;
• accepted constraints или BLOCKED.

8.5 Human-only decisions

Человек выбирает:

• architecture option;
• dependencies;
• providers;
• criteria weights;
• accepted risks;
• patterns;
• migration strategy;
• whether implementation planning may continue.

8.6 Safety rules

• matrix score не является decision;
• recommendation не является approval;
• validator PASS не утверждает ADR;
• agent не назначает criteria weights от имени человека;
• preset/library suggestion не становится dependency автоматически;
• unresolved material conflict блокирует downstream task generation.

8.7 Exit condition

Downstream workflow получает exact accepted architecture constraints либо explicit NOT_REQUIRED, NEEDS_CHANGES, DEFERRED или BLOCKED.

────────

9. WF-06 — UX Skeleton to Vertical Slice

9.1 Назначение

Не позволять Specification переходить прямо в full-app code generation. Сначала должна появиться reviewable модель пользовательского поведения.

9.2 Trigger

• feature имеет пользовательский интерфейс;
• участвуют несколько actors/roles;
• важны состояния, navigation или permissions;
• code generation без UX model создаёт material риск.

9.3 Flow

```text
Specification + architecture constraints
→ UX Intake
→ DRAFT Project UX Skeleton
→ actors and journeys
→ pages/views and elements
→ states and transitions
→ navigation and access matrix
→ requirement coverage
→ deterministic validation
→ optional advisory pattern/research suggestions
→ human UX review
→ reviewed revision
→ vertical slice candidates
→ human selection of one slice
```

9.4 UX Skeleton должен содержать

• stable IDs;
• actors;
• user journeys;
• pages/views;
• components/elements;
• loading, empty, error, permission, offline, success states;
• transitions;
• role/access rules;
• failure and recovery paths;
• links к source requirements;
• provenance;
• explicit unknowns.

9.5 Human review package

Человеку показываются:

• application map;
• journeys;
• page inventory;
• state matrix;
• navigation;
• access matrix;
• uncovered requirements;
• unreachable states;
• advisory suggestions и provenance;
• accepted/rejected/deferred decisions;
• revision diff.

9.6 Vertical slice

Vertical slice — минимальная целостная возможность, проходящая через:

```text
user interaction
→ application logic
→ data / integration
→ validation
→ Evidence
```

Он не должен включать соседние будущие flows только ради «полноты».

9.7 Invariants

```text
UX Skeleton ≠ implementation
UX validation PASS ≠ human approval
Library suggestion ≠ project decision
Reviewed skeleton ≠ global execution authorization
Slice candidate ≠ Task Brief
```

9.8 Exit condition

Есть exact selected vertical slice, его inclusions/exclusions и links к requirements/UX IDs.

────────

10. WF-07 — Backlog, Lazy Decomposition and Task Brief

10.1 Назначение

Преобразовать выбранную capability или slice в одну исполнимую задачу без преждевременной декомпозиции всего проекта.

10.2 Hierarchy

```text
Epic → Stage → Sub-stage only when material → executable Task
```

Каждый уровень имеет:

• ID;
• parent ID;
• purpose;
• status;
• dependencies;
• acceptance / Definition of Done;
• human-checkpoint flag.

10.3 Lazy decomposition

Sub-stage создаётся только если:

• отдельная authority boundary;
• independent validation;
• material risk;
• protected operation;
• отдельный acceptance result;
• реальная dependency;
• задача слишком велика для одного bounded execution.

Не дробить задачу, если она решается одной reversible operation и focused check.

10.4 Task Brief compilation

Task Brief содержит:

• task ID;
• goal;
• exact subject;
• baseline;
• in-scope paths;
• forbidden paths;
• allowed changes;
• forbidden changes;
• preconditions;
• acceptance criteria;
• required checks;
• known risks;
• unknowns;
• expected report;
• stop conditions.

10.5 Bidirectional check

Перед execution:

```text
parent purpose
→ child task
```

После выполнения:

```text
task result
→ does it actually satisfy child?
→ does child progress parent?
```

Закрытая child task не доказывает completion parent.

10.6 Non-grants

```text
Plan ≠ Task Brief
Task Brief ≠ Risk assignment
Task Brief ≠ execution authorization
Task Brief ≠ Git authorization
```

10.7 Exit condition

Существует один complete bounded Task Brief, готовый к repository preflight и human authorization.

────────

11. WF-08 — Repository Preflight and Execution Authorization

11.1 Назначение

Связать будущую mutation с exact repository state и отдельным решением человека.

11.2 Preflight

Проверяются:

• repository root;
• worktree;
• branch;
• HEAD;
• baseline;
• staged / unstaged / untracked;
• diff;
• nested repositories;
• symlinks;
• target paths;
• interpreter/dependencies;
• sandbox;
• network;
• remote identity;
• temporary boundary;
• credentials/data boundary;
• stop conditions.

11.3 Existing state classification

• IN_SCOPE_EXISTING;
• OUT_OF_SCOPE_USER_STATE;
• ENVIRONMENT_NOISE;
• GENERATED_DISPOSABLE;
• UNKNOWN_MATERIAL.

AOS не должен silently clean unrelated user state.

11.4 Execution Authorization

Отдельный human record bind к:

• exact Task Brief;
• repository;
• branch;
• HEAD/baseline;
• stage;
• allowed operations;
• paths;
• conditions;
• expiry/consumption rule;
• explicit exclusions.

11.5 Preview

До mutation человек может видеть:

• что изменится;
• где изменится;
• какие commands будут выполнены;
• какие side effects возможны;
• что не будет выполнено;
• какие checks последуют.

Preview сам по себе ничего не разрешает.

11.6 Exit conditions

• AUTHORIZED_FOR_EXACT_EXECUTE_STAGE;
• BLOCKED_CANDIDATE_IDENTITY_CHANGED;
• BLOCKED_UNRELATED_USER_STATE;
• HUMAN_REVIEW_REQUIRED;
• AUTHORIZATION_DECLINED.

────────

12. WF-09 — Controlled Execution

12.1 Назначение

Выполнить одну causal mutation внутри exact authorization.

12.2 Flow

```text
reverify candidate
→ verify authorization
→ verify scope and stop conditions
→ execute one bounded change
→ capture outputs and partial effects
→ focused checks permitted inside EXECUTE
→ Stage Report
→ stop
```

12.3 Rules

• no hidden next stage;
• no unrelated cleanup;
• no automatic retry после terminal failure;
• no git add -A в mixed worktree;
• no network expansion;
• no dependency adoption без решения;
• no mutation после authorization invalidation;
• only one writer for protected/shared state;
• partial write must be observable.

12.4 Outputs

Stage Report:

```yaml
task_id:
stage: EXECUTE
result:
starting_identity:
ending_identity:
changed_paths: []
checks_run: []
checks_not_run: []
findings: []
limitations: []
unknowns: []
out_of_scope_state: []
authorization_consumed:
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action:
stop: true
```

12.5 Result states

• COMPLETED;
• COMPLETED_WITH_FINDING;
• FAIL;
• BLOCKED;
• UNKNOWN;
• PARTIAL_MUTATION_REQUIRES_RECOVERY.

12.6 Exit condition

Execution всегда заканчивается report + stop. Следующий VALIDATE является отдельным stage.

────────

13. WF-10 — Validation, Evidence, Review and Human Decision

13.1 Назначение

Отделить техническую проверку результата от его исправления и от решения человека.

13.2 Validation flow

```text
freeze exact candidate
→ verify environment and provenance
→ run targeted checks
→ run relevant regression/smoke checks
→ inspect result and diff
→ record commands and outputs
→ classify NOT_RUN and limitations
→ verify validation caused no mutation
→ validation report
→ stop
```

13.3 Verification gates

1. Structure.
2. Scope.
3. Acceptance.
4. Regression / smoke.
5. Security / release blockers.

Precedence:

```text
CONTRACT_VIOLATION
> FAIL
> BLOCKED
> UNKNOWN
> NOT_RUN
> PASS
```

13.4 Evidence

Evidence связывает:

• acceptance criterion;
• exact subject/candidate;
• command/check;
• result;
• artifact/log;
• timestamp;
• provenance;
• limitations.

Evidence не утверждает результат.

13.5 Review

Reviewer оценивает:

• соответствует ли change stated goal;
• соблюдён ли scope;
• достаточны ли Evidence;
• остались ли material risks;
• не симулируется ли approval;
• можно ли предложить ACCEPT, NEEDS_CHANGES, REJECT или DEFER.

Review не исправляет artifact.

13.6 Human decision

Только человек устанавливает:

• ACCEPT;
• NEEDS_CHANGES;
• REJECT;
• DEFER.

Decision bind к exact candidate revision. Последующая mutation может сделать решение stale.

13.7 Exit condition

Есть:

• technical validation result;
• Evidence package;
• review recommendation;
• explicit human decision или HUMAN_REVIEW_REQUIRED.

────────

14. WF-11 — Correction, Recovery and Resume

14.1 Назначение

Продолжить работу после failure, interruption, stale context или validation finding, не скрывая partial state и не выполняя автоматический retry.

14.2 Correction after validation finding

```text
VALIDATE finding
→ report + stop
→ new bounded correction Task Brief
→ new Execution Authorization
→ EXECUTE correction
→ separate VALIDATE
```

Validator не исправляет subject внутри того же stage.

14.3 Recovery after execution failure

```text
failure
→ stop mutation
→ preserve logs and partial state
→ classify completed/partial/unknown effects
→ recovery facts
→ choose rollback / reconcile / resume candidate
→ human decision when material
→ separate recovery task
```

14.4 Recovery after session interruption

AOS восстанавливает:

• repository/branch/HEAD;
• active task;
• consumed permissions;
• last completed stage;
• current candidate;
• changed paths;
• checks run/not run;
• findings;
• human decisions;
• one next action.

Mutable facts перепроверяются; старый handoff не считается current observation.

14.5 Safe retry

Retry допустим только если:

• operation доказанно idempotent;
• exact candidate не изменился;
• authorization ещё применима;
• side effects известны;
• retry явно разрешён workflow/task contract.

Иначе создаётся новая task/recovery boundary.

14.6 Exit conditions

• RECOVERED_READY_FOR_VALIDATION;
• ROLLED_BACK;
• RESUME_READY;
• BLOCKED_PARTIAL_STATE;
• HUMAN_DECISION_REQUIRED.

────────

15. WF-12 — Git Delivery and Release

15.1 Назначение

Доставить принятый результат без объединения Git actions в одно общее разрешение.

15.2 Git chain

```text
accepted exact candidate
→ Commit authorization
→ reverify repository/candidate
→ Commit
→ Push authorization
→ reverify branch/remote/auth
→ Push
→ PR creation authorization
→ draft/ready PR
→ REVIEW / CI / human decision
→ Merge authorization
→ reverify expected head SHA
→ Merge
→ Release authorization
→ Release
```

Каждая операция имеет отдельный subject и permission.

15.3 Commit

Commit должен быть:

• atomic;
• limited to allowed paths;
• free of unrelated user state;
• bound к validated candidate;
• accompanied by exact message and identity.

15.4 Push

Перед push проверяются:

• remote identity;
• branch;
• upstream;
• credentials;
• current HEAD;
• absence of unexpected mutation.

15.5 Pull Request

PR содержит:

• purpose;
• exact diff boundary;
• changed paths;
• validation;
• NOT_RUN;
• risks/limitations;
• human decision status;
• explicit non-grants.

Draft PR не является merge authorization.

15.6 Merge

Merge выполняется только после exact permission, preferably bound к expected head SHA.

```text
mergeable: true
≠ merge approved
```

15.7 Release

Release может включать:

• checklist;
• version;
• changelog;
• dependency/security checks;
• rollback plan;
• release Evidence;
• operator handoff.

Human acceptance implementation не означает автоматический Release.

────────

16. WF-13 — Observability and Continuous Improvement

16.1 Назначение

Использовать реальные эксплуатационные данные для новых bounded improvements, не позволяя системе самовольно менять product или process.

16.2 Inputs

• runtime metrics;
• incidents;
• support feedback;
• task/review friction;
• failed checks;
• recurring clarification loops;
• scope drift observations;
• user comprehension data;
• handoff quality;
• governance overhead.

16.3 Flow

```text
observation
→ provenance and data boundary
→ signal classification
→ incident / improvement record
→ duplicate and impact analysis
→ candidate problem
→ human triage
→ Idea Bank / Feature Passport / Task candidate
→ normal product workflow
```

16.4 Continuous Improvement scope

Может улучшаться:

• product behavior;
• templates;
• validators;
• onboarding;
• interaction;
• workflow friction;
• context loading;
• test coverage;
• recovery;
• documentation.

16.5 Safety boundary

• metric не является product decision;
• alert не разрешает mutation;
• incident не создаёт automatic fix;
• AI recommendation не изменяет policy;
• process optimization не отменяет Minimal Safety Floor.

16.6 Exit condition

Observation превращена в explicit bounded candidate либо закрыта как noise/duplicate/reference.

────────

17. WF-14 — Development of an AOS Feature

17.1 Назначение

Определить сквозной процесс создания capability самого AOS, а не consumer project.

17.2 Flow

```text
AOS problem / observed gap
→ Idea Record
→ feature overlap and dependency check
→ detailed Feature Passport
→ human product disposition
→ user journey and workflow impact
→ Product Contract
→ acceptance scenarios
→ DRAFT architecture options when material
→ human architecture/dependency decision
→ bounded Task Brief
→ repository preflight
→ explicit execution authorization
→ EXECUTE
→ VALIDATE
→ REVIEW
→ human result decision
→ separate Git delivery
→ dogfood in real workflow
→ improvement/lesson proposal
```

17.3 Required gates

AOS feature не переходит дальше, пока не ясны:

• user/problem/outcome;
• observable behavior;
• Product Runtime vs Development Factory layer;
• non-goals;
• states;
• authority boundary;
• failure/recovery;
• acceptance;
• dependencies;
• effect on existing workflows.

17.4 First implementation principle

Сначала:

• manual;
• read-only where possible;
• user-visible;
• narrow;
• replaceable;
• Markdown/JSON/local utility.

Не создавать заранее:

• full Control Plane;
• mandatory DB;
• full RAG;
• multi-agent orchestration;
• autonomous self-heal;
• central Control Plane.

17.5 Dogfood

Feature должна быть проверена в реальном AOS workflow:

• уменьшает ли она число clarification loops;
• улучшает ли понимание current status;
• уменьшает ли scope drift;
• сохраняет ли human authority;
• создаёт ли полезный Evidence;
• можно ли удалить feature без разрушения core;
• не превышает ли overhead пользу.

Этот slice должен сначала доказать:

• понятность для непрограммиста;
• сохранение authority;
• отсутствие scope drift;
• корректное разделение stages;
• восстановимость состояния;
• переносимость между agent environments.

────────

18. WF-15 — Documentation Reconstruction

18.1 Назначение

Собрать пакет документов, достаточный для независимого проектирования и будущей реализации AOS без копирования legacy complexity.

18.2 Flow

```text
project and authority alignment
→ source inventory and provenance
→ targeted extraction
→ product definition
→ feature catalog
→ user journeys
→ end-to-end workflows
→ product contracts and acceptance
→ shared technical contracts
→ DRAFT implementation specifications
→ test design and traceability
→ contradiction and decision closure
→ readiness audit
→ human transition decision
```

18.3 Required outputs

Пакет должен отвечать:

• кто пользователь;
• какую проблему решает AOS;
• какие capabilities существуют;
• как пользователь проходит сквозные workflows;
• какие artifacts и states связывают stages;
• где требуется человек;
• какие failures/recovery предусмотрены;
• как проверяется acceptance;
• какие решения неизвестны;
• какая минимальная implementation model предлагается.

18.4 Targeted research

Research выполняется только при exact gap:

```text
selected workflow / feature
→ exact unknown
→ bounded research question
→ source policy
→ repository/path/snapshot
→ classified observation
→ update DRAFT
→ stop
```

Полная повторная extraction legacy не требуется, если она не закрывает конкретный implementation question.

18.5 Readiness outcomes

• REIMPLEMENTATION_READY;
• READY_WITH_DECLARED_GAPS;
• NOT_READY.

Readiness report не является authorization implementation.

────────

19. Cross-workflow artifacts

|Artifact                      |Producer|Consumer          |Non-grant                               |
|------------------------------|--------|------------------|----------------------------------------|
|Interaction Context           |`WF-01` |selected workflow |не разрешает action                     |
|Bootstrap Preview             |`WF-02` |human confirmation|не изменяет project                     |
|Capability Map                |`WF-03` |product planning  |не утверждает current behavior полностью|
|Feature Passport              |`WF-04` |product decision  |не разрешает implementation             |
|ADR / Architecture Constraints|`WF-05` |UX/task generation|не является execution authorization     |
|UX Skeleton                   |`WF-06` |slice selection   |не является implementation              |
|Vertical Slice Record         |`WF-06` |`WF-07`           |не является Task Brief                  |
|Task Brief                    |`WF-07` |`WF-08`           |не является authorization               |
|Execution Authorization       |`WF-08` |`WF-09`           |не разрешает Git                        |
|Stage Report                  |`WF-09` |`WF-10`           |не является validation                  |
|Validation Report             |`WF-10` |Review            |не является approval                    |
|Evidence Package              |`WF-10` |Review/Human      |не является approval                    |
|Human Decision Record         |`WF-10` |Git/next cycle    |ограничен exact subject                 |
|Recovery Record               |`WF-11` |resume/correction |не разрешает retry автоматически        |
|Delivery Record               |`WF-12` |operations        |не является Release                     |
|Observation/Incident Record   |`WF-13` |product intake    |не разрешает fix                        |

────────

20. Global state model

AOS не должен иметь одну смешанную шкалу статуса. Нужны независимые оси.

20.1 Artifact maturity

```text
DRAFT
READY_FOR_REVIEW
HUMAN_REVIEW_REQUIRED
ACCEPTED
NEEDS_CHANGES
REJECTED
DEFERRED
SUPERSEDED
```

20.2 Technical result

```text
CONTRACT_VIOLATION
FAIL
BLOCKED
UNKNOWN
NOT_RUN
PASS
```

20.3 Execution authorization

```text
NOT_REQUESTED
REQUESTED
AUTHORIZED
DECLINED
EXPIRED
CONSUMED
INVALIDATED
```

20.4 Git state

```text
EDIT_NOT_STARTED
EDIT_COMPLETE
COMMIT_NOT_AUTHORIZED
COMMITTED
PUSH_NOT_AUTHORIZED
PUSHED
PR_DRAFT
PR_READY
MERGE_NOT_AUTHORIZED
MERGED
RELEASE_NOT_AUTHORIZED
RELEASED
```

20.5 Workflow state

```text
NOT_STARTED
ACTIVE
STOPPED_WITH_REPORT
WAITING_FOR_HUMAN
BLOCKED
COMPLETED_FOR_STAGE
STALE
```

Переход одной оси не мутирует другие автоматически.

────────

21. UX of workflow interaction

Пользователь не должен читать внутренний state machine для каждого действия. Chat-first interface показывает:

1. Что сейчас происходит.
2. Какой exact subject.
3. Что уже подтверждено.
4. Что не проверялось.
5. Что блокирует продолжение.
6. Какое решение требуется от человека.
7. Одно следующее действие.

Минимальные команды/действия:

```text
/status
/next
/details
/evidence
/changes
/risks
/approve <bounded subject>
/reject
/stop
/resume
```

Presentation layer:

• не владеет facts;
• не скрывает UNKNOWN, BLOCKED, NOT_RUN;
• не превращает UI click в расширенную authorization;
• показывает disabled actions и причину;
• связывает каждое решение с exact subject.

────────

22. Workflow selection rules

22.1 Не запускать architecture всегда

Architecture workflow включается только для material choice.

22.2 Не запускать discovery без необходимости

Для нового пустого проекта достаточно bootstrap + intake. Для узкой задачи в хорошо известном repository нужен targeted preflight, а не полный census.

22.3 Не создавать весь backlog заранее

Декомпозиция выполняется лениво вокруг ближайшего slice/stage.

22.4 Не создавать Governance раньше повторяемой проблемы

Automation admission:

```text
manual repetition
→ stable contract
→ known failures
→ measurable benefit
→ safe fallback/removal
→ bounded automation
```

22.5 Не повторять уже принятый context

При переходе между sessions передаётся delta и mutable facts перепроверяются.

────────

23. Минимальный первый Product Runtime slice

Предлагаемый первый сквозной slice, который доказывает основную ценность AOS:

```text
человек описывает небольшую feature
→ AOS уточняет problem/outcome
→ создаёт Feature Passport
→ формирует один bounded Task Brief
→ показывает execution preview
→ человек отдельно разрешает execution
→ агент выполняет одну reversible change
→ отдельный validation проверяет acceptance
→ AOS собирает compact Evidence
→ человек принимает или отправляет на correction
→ AOS показывает одно следующее действие
```

MVP не требует:

• полной Architecture Assistant;
• UX editor;
• full RAG;
• multi-agent orchestration;
• release automation;
• observability platform;
• autonomous recovery;
• central Control Plane.

Этот slice должен сначала доказать:

• понятность для непрограммиста;
• сохранение authority;
• отсутствие scope drift;
• корректное разделение stages;
• восстановимость состояния;
• переносимость между agent environments.

────────

24. Acceptance criteria документа workflow

Документ может быть предложен для human review, если:

1. Product Runtime и AOS Development Factory разделены.
2. Новый и существующий project имеют разные entry workflows.
3. Product definition предшествует task generation.
4. Architecture включается условно, а не всегда.
5. UX Skeleton не подменяет implementation.
6. Lazy decomposition не создаёт полный backlog заранее.
7. Task Brief и Execution Authorization разделены.
8. Repository preflight bind к candidate identity.
9. EXECUTE, VALIDATE и REVIEW разделены.
10. Validation не исправляет subject.
11. Evidence не выдаётся за approval.
12. Human decision bind к exact revision.
13. Correction выполняется отдельным task/stage.
14. Resume перепроверяет mutable facts.
15. Commit, Push, PR, Merge и Release имеют отдельные permissions.
16. Observability создаёт candidate input, а не automatic fix.
17. Workflow states и technical results не смешаны.
18. Каждый terminal result заканчивается report + stop.
19. Каждый workflow показывает один next action.
20. Документ не объявляет proposal canonical или implemented.

────────

25. Open decisions

До implementation planning человек должен отдельно решить:

1. Какие workflows входят в обязательный Product Runtime MVP.
2. Какой первый dogfood project использовать.
3. Где хранится canonical state каждого workflow.
4. Какие artifacts будут Markdown, YAML или JSON.
5. Как аутентифицируется Human Decision Record.
6. Какой workflow engine нужен и нужен ли он вообще на первом этапе.
7. Как реализуется cross-session resume.
8. Как AOS интегрируется с ChatGPT, Codex и AntiGravity.
9. Где проходит trusted execution boundary.
10. Какие Git operations поддерживает MVP.
11. Нужна ли Architecture Assistant в первой версии.
12. Нужен ли UX Skeleton в первой версии или после core execution slice.
13. Какой минимальный Evidence package достаточен.
14. Когда optional Governance module допускается к разработке.
15. Какой repository станет implementation repository.

Пока решения отсутствуют:

```text
HUMAN_REVIEW_REQUIRED
```

или, если решение блокирует конкретную реализацию:

```text
BLOCKED
```

────────

26. Source classification and limitations

FACT

• История проекта последовательно использует разделение PLAN → EXECUTE → VALIDATE → REVIEW.
• Task Brief, execution authorization и Git permissions должны быть разделены.
• Product-first и shortest-safe-path являются устойчивыми направлениями проекта.
• Feature Catalog и отдельные feature/function dossiers уже созданы как DRAFT artifacts.
• Ошибки и lessons уже выделены отдельно и в этот документ намеренно не дублируются.

INFERENCE

• Для воспроизводимого AOS требуется не один общий pipeline, а набор связанных end-to-end workflows.
• Product Runtime, Development Factory и Documentation Reconstruction должны иметь раздельные state/authority boundaries.
• Первый полезный AOS slice должен связывать intent, bounded task, execution, Evidence и human decision.

PROPOSAL

• IDs WF-01..WF-15;
• точные artifact names;
• global state vocabulary;
• workflow selection rules;
• минимальный Product Runtime slice;
• acceptance criteria и open-decision list.

UNKNOWN / NOT_RUN

• Current implementation каждого workflow;
• accepted architecture;
• implementation repository;
• runtime stack;
• workflow engine;
• durability/state backend;
• exact integration contracts с agent environments;
• fresh independent semantic validation этого документа.

Доступная история чатов не является доказанным byte-complete export всех сообщений. Отсутствие пункта означает NOT_FOUND_IN_CURRENT_SOURCE_SET, а не доказательство глобального отсутствия.

────────

27. Финальная схема

```text
ENTRY
→ выбрать правильный workflow и exact subject

NEW PROJECT
→ bootstrap → doctor → intake

EXISTING PROJECT
→ discovery → capability map → selected gap

PRODUCT
→ problem → Feature Passport → human product decision

DESIGN
→ conditional architecture → conditional UX skeleton → vertical slice

TASK
→ lazy decomposition → bounded Task Brief

AUTHORITY
→ repository preflight → explicit Execution Authorization

CHANGE
→ one bounded EXECUTE → report → stop

QUALITY
→ separate VALIDATE → Evidence → REVIEW → human decision

RECOVERY
→ separate correction / rollback / resume

DELIVERY
→ separate Commit → Push → PR → Merge → Release permissions

LEARNING
→ observations → candidate improvement → normal product workflow
```

Главный принцип:

> **AOS не должен автоматически проталкивать работу по pipeline. Он должен делать текущее состояние, границы, Evidence и требуемое человеческое решение очевидными, а затем безопасно проводить только через один следующий разрешённый шаг.**

────────

```yaml
task_class: DOCUMENTATION_RECONSTRUCTION
stage: AUTHORING
result: DRAFT_CREATED
artifact: AOS_End_to_End_Workflows_R1.md
authority: NONE
canonical_status: NOT_ASSIGNED
execution_authorized: false
repository_changes: NOT_PERFORMED
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
checks_run:
  - document_structure_review
  - workflow_id_uniqueness
  - cross_workflow_boundary_review
  - safety_invariant_presence
checks_not_run:
  - independent_semantic_review
  - repository_integration_validation
  - implementation_validation
next_required_action: HUMAN_REVIEW_OF_WORKFLOW_BOUNDARIES_AND_MVP_SELECTION
stop: true
```
