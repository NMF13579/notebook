---
document_type: DOCUMENTATION_PRODUCTION_PLAN
revision: DRAFT-R2
status: DRAFT
claim_class: SYNTHESIZED_PROPOSAL
authority: NONE
human_acceptance: NOT_RUN
documentation_plan_readiness: READY_FOR_HUMAN_REVIEW
implementation_readiness: NOT_READY
implementation_authorization: NONE
git_authorization: NONE
knowledge_repository: NMF13579/notebook
implementation_repository: UNASSIGNED
active_path: planning/01_DOCUMENTATION_PRODUCTION_PLAN.md
supersedes: planning/AOS_DOCUMENTATION_PRODUCTION_PLAN_DRAFT_R1.md@DRAFT-R1
parent_plan: planning/00_WORKSPACE.md
agent_instruction_draft: planning/02_AGENTS_DRAFT.md
current_state_owner: planning/CURRENT.md
created: 2026-08-04
updated: 2026-08-04
---

# AOS-3 — план создания документации для передачи coding agent

## 1. Вывод

Этот план раскрывает `planning/00_WORKSPACE.md` до уровня, на котором documentation agent способен последовательно подготовить документацию для coding agent без использования истории чатов.

Документация создаётся в той же последовательности, в которой должен создаваться проект:

```text
D1. Закрыть обязательные решения и подготовить documentation baseline
→ D2. Описать строительные леса и подготовить первый Task Brief
→ D3. Описать постоянное рабочее ядро по implementation slices
→ D4. Описать pipeline по трём частям
→ D5. Проверить сквозную полноту и собрать Developer Handoff Package
```

Главный принцип:

```text
общие product/architecture/contracts можно проектировать заранее
→ exact Task Brief создаётся только для ближайшего implementation slice
→ coding agent получает один bounded package
→ следующий Task Brief создаётся после фактического результата предыдущего slice
```

Такой подход сочетает:

- достаточно полную документацию системы;
- `lazy decomposition`;
- один owner на fact class;
- минимальное участие человека;
- отсутствие преждевременного полного backlog;
- проверяемую передачу между documentation agent и coding agent.

План не выбирает implementation repository, feature, architecture или toolchain, не принимает документы и не разрешает mutation либо Git actions.

## 2. Назначение и границы

### 2.1. Назначение

План должен позволить documentation agent:

1. восстановить подтверждённый контекст из `docs/00_Core.md` и релевантных owners;
2. определить exact documentation stage;
3. найти решения, которых не хватает следующему implementation slice;
4. сгруппировать только material human decisions;
5. создать contracts, examples, acceptance и negative tests;
6. проверить согласованность документов между собой;
7. собрать один bounded package для coding agent;
8. остановиться до execution authorization.

### 2.2. Что этот план не разрешает

- писать runtime-код в knowledge repository;
- выбирать за человека product scope, first vertical slice, architecture или `Risk Profile`;
- назначать `human_disposition` фичам;
- симулировать human acceptance;
- создавать Execution Authorization от имени человека;
- выполнять `Commit`, `Push`, `Merge` или `Release`;
- выдавать полный documentation package за реализованный продукт.

### 2.3. Нормативная граница

```text
Documentation plan ≠ Documentation Task Brief
Documentation Task Brief ≠ accepted contract
Accepted contract ≠ implementation Task Brief
Implementation Task Brief ≠ Execution Authorization
Documentation PASS ≠ human acceptance
Developer handoff ≠ permission to mutate
```

## 3. Модель передачи между агентами

### 3.1. Две роли

| Роль | Отвечает | Не отвечает |
|---|---|---|
| Documentation agent | Product/feature/architecture contracts, exact task scope, validation design, traceability, handoff completeness | Runtime implementation, human decisions, execution/Git authorization |
| Coding agent | Реализация exact authorized task, tests, Evidence, Stage Report | Изменение product contract, выбор нового scope, human acceptance |

### 3.2. Единица передачи

Единицей передачи является `Documentation Slice Package` (`DSP`), а не весь репозиторий и не пересказ чата.

Каждый `DSP` содержит:

1. exact implementation objective;
2. ссылки на authoritative accepted facts;
3. exact Feature/System Contract в нужной boundary;
4. принятые ADR/decisions, если они требуются;
5. один Task Brief;
6. validation matrix;
7. required positive, negative и recovery cases;
8. repository preflight snapshot или требование выполнить fresh preflight;
9. known unknowns, blockers и out-of-scope state;
10. proposed authorization form, не подписанный человеком;
11. developer handoff manifest;
12. one next action и `stop: true`.

### 3.3. Когда package считается передаваемым

`DSP` можно передавать coding agent только если:

- у всех implementation-affecting facts есть один owner;
- required decisions имеют human provenance;
- generic dossier fields заменены exact contracts;
- нет material `UNKNOWN`, скрытого внутри assumption;
- acceptance criteria наблюдаемы;
- negative scenarios выполнимы как tests/checks;
- allowed и forbidden scope machine-checkable;
- recovery определён до первой write-capable operation;
- validation не требует от coding agent нового product/architecture решения;
- все ссылки repository-relative или устойчивые;
- handoff audit имеет technical `PASS`;
- human acceptance и execution authorization остаются отдельными `NOT_RUN`, если их ещё не было.

## 4. Владельцы документационных fact classes

Новый operational artifact создаётся только при distinct owner или downstream consumer.

| Fact class | Owner | Производные представления |
|---|---|---|
| Project identity, authority, safety | `docs/00_Core.md` | Handoff summary |
| Users, problem, product boundary, journeys | `docs/01_Product.md` | Slice overview |
| Layers, contracts, data ownership, recovery rules | `docs/02_Architecture.md` | Architecture view в DSP |
| Workflow, stages, validation, Git boundaries | `docs/03_Development.md` | Task procedure |
| Known failures и regression cases | `docs/04_Lessons.md` | Validation matrix |
| Provenance и targeted research | `docs/05_Reference.md` + bounded research record | Research summary |
| Feature inventory | `docs/06_Features.md` | Registry index |
| Exact human implementation decisions | `AOS_IMPLEMENTATION_DECISIONS_R1.md` | Decision package summary |
| Scaffolding behavior | `AOS_SCAFFOLDING_CONTRACT_R1.md` | Scaffold DSP |
| Permanent core behavior | `AOS_CORE_CONTRACT_R1.md` | Core DSPs |
| End-to-end pipeline behavior | `AOS_PIPELINE_CONTRACT_R1.md` | Pipeline DSPs |
| Exact implementation task scope | `Task-xxx.md` | Handoff manifest |
| Current durable lifecycle state | `Project Memory`; в notebook — `planning/CURRENT.md` до нового решения | `Status / Next / Details` |
| Exact run facts | Immutable `Stage Report` / Evidence | Project Memory reference |
| Package navigation | `DEVELOPER_HANDOFF_Rx.md` | Ничего authoritative |

`DEVELOPER_HANDOFF_Rx.md` не дублирует contracts. Он только связывает exact revisions, identities и next action.

## 5. Общий contract документационного подэтапа

Каждый подэтап `D*` оформляется по одному шаблону:

```yaml
documentation_slice:
  id:
  parent_stage:
  objective:
  downstream_consumer:
  input_owners: []
  required_human_decisions: []
  artifacts_to_create_or_update: []
  fact_classes_owned: []
  content_requirements: []
  traceability_requirements: []
  acceptance_checks: []
  negative_checks: []
  conflicts: []
  material_unknowns: []
  non_goals: []
  output_package:
  next_transition:
```

Для каждого подэтапа documentation agent выполняет:

```text
input inventory
→ authority classification
→ missing-decision analysis
→ compact human decision package when needed
→ draft/update exact owners
→ examples and validation matrix
→ cross-document consistency check
→ package freeze
→ read-only documentation validation
→ terminal report and stop
```

## 6. D1 — решения и documentation baseline

### 6.1. Цель

Закрыть только те product/architecture/implementation решения, без которых нельзя точно описать строительные леса и первый vertical slice.

### 6.2. Входы

- `docs/00_Core.md` как обязательная точка входа;
- `docs/01_Product.md` §§5–14;
- `docs/02_Architecture.md` §§3–16;
- `docs/03_Development.md` §§2–22;
- `docs/06_Features.md` inventory;
- `planning/00_WORKSPACE.md`;
- `planning/02_AGENTS_DRAFT.md` как proposal, не active instruction;
- current explicit human decisions;
- fresh read-only repository observations, если implementation repository уже назначен.

### 6.3. Подэтап D1.1 — decision gap register

Documentation agent создаёт таблицу только обязательных решений:

| Decision field | Почему нужен сейчас | Кто решает | Допустимый temporary state |
|---|---|---|---|
| `implementation_repository` | Определяет target paths и preflight | Человек | `UNASSIGNED`, но D2 blocked |
| `first_user_problem` | Определяет product value | Человек | `UNDECIDED`, но feature contract blocked |
| `first_vertical_slice` | Определяет первый user-visible result | Человек | `UNDECIDED`, но Task Brief blocked |
| `first_interface` | Определяет command/UI contract | Человек | `UNDECIDED`, D2 detail blocked |
| `language_toolchain_versions` | Определяет scaffold и commands | Человек принимает рекомендацию | `UNDECIDED`, D2 blocked |
| `data_persistence` | Определяет Project Memory contract | Человек принимает ADR | `UNDECIDED`, D3 blocked |
| `supported_environments` | Определяет reproducibility | Человек принимает recommendation | `UNDECIDED`, D2 gate blocked |
| `primary_agent_environment` | Определяет первый thin adapter | Человек | `UNDECIDED`, final adapter blocked |
| `human_decision_authenticity` | Определяет valid decision record | Человек принимает contract | `UNDECIDED`, execution blocked |
| `Risk_Profile_vocabulary` | Нужен protected routes | Человек | Можно отложить до первого risk-bearing task |
| `feature_dispositions` | Нужны только selected `FTR-*` | Человек | Все остальные остаются `UNDECIDED` |

Запрещено включать в package дальние решения, не влияющие на D2 или первый slice.

### 6.4. Подэтап D1.2 — compact decision package

Для каждого unresolved material decision показать:

```yaml
decision_id:
question:
recommended_option:
alternatives: []
tradeoffs: []
affected_artifacts: []
affected_actions: []
reversibility:
latest_safe_decision_point:
human_decision: NOT_RUN
```

Человеку показывается один связанный package, а не серия вопросов о внутренних engineering details.

### 6.5. Подэтап D1.3 — implementation decision record

Создать `AOS_IMPLEMENTATION_DECISIONS_R1.md`.

Обязательное содержание:

- project/repository identity;
- first problem, actor и desired outcome;
- selected first slice;
- selected `FTR-*` и exact `human_disposition`;
- interface;
- language/runtime/framework/package manager/version policy;
- persistence model;
- supported environments;
- repository topology decision;
- Runtime/Factory boundary;
- primary agent adapter;
- human acceptance identity model;
- protected/destructive decision model;
- explicitly deferred choices;
- decision actor, date и exact subject per decision;
- reversal conditions.

Непринятое поле остаётся `UNDECIDED`; агент не подставляет inference.

### 6.6. Подэтап D1.4 — thin documentation-agent instructions

Переработать `planning/02_AGENTS_DRAFT.md` в следующую exact revision как thin bootstrap candidate.

Он должен содержать только:

- role/objective;
- source routing;
- authority order;
- ask/stop rules;
- запрет runtime implementation в documentation task;
- one-owner rule;
- documentation package workflow;
- task-local correction limit;
- terminal report format;
- placeholders только для ещё не принятых real commands/paths.

Подробные contracts остаются в owners, а не копируются в `planning/02_AGENTS_DRAFT.md`.

### 6.7. D1 acceptance

- каждое решение имеет status и owner;
- ни одно human decision не создано агентом;
- решения, влияющие на D2, закрыты или D2 честно `BLOCKED`;
- selected features имеют item-level disposition;
- дальние feature dispositions не требуются;
- conflicts названы по affected fact class;
- документационный агент может однозначно определить следующий DSP.

### 6.8. Результат D1

```text
Implementation Decision Record
+ thin documentation-agent instruction candidate
+ first documentation Task Brief
```

## 7. D2 — документация строительных лесов

### 7.1. Цель

Подготовить полный contract воспроизводимой среды разработки до написания product behavior.

### 7.2. Главный artifact

Создать `AOS_SCAFFOLDING_CONTRACT_R1.md`.

Документ является владельцем exact scaffold behavior, но не заменяет общие architecture/development owners.

### 7.3. Подэтап D2.1 — repository topology и ownership

Документировать:

- target repository и branch model;
- directory tree первого цикла;
- границы Product Runtime / Development Factory / Safety / Knowledge;
- managed, user-owned, generated и temporary paths;
- protected и forbidden paths;
- config locations;
- test/fixture locations;
- output/evidence locations;
- symlink, nested repository и case-sensitivity policy;
- package/module ownership;
- правила portable links.

Для каждой directory указать:

```text
purpose → owner → allowed writers → lifecycle → validation → recovery
```

### 7.4. Подэтап D2.2 — toolchain и environment contract

Документировать:

- pinned runtime и package manager;
- dependency policy;
- setup prerequisites;
- supported OS/shell/container boundaries;
- environment variables без secrets;
- local/CI parity;
- offline/network assumptions;
- deterministic install/build rules;
- version mismatch behavior;
- clean-checkout bootstrap.

Приложить:

- valid environment example;
- missing dependency case;
- wrong version case;
- unavailable network case;
- unknown environment classification.

### 7.5. Подэтап D2.3 — command surface contract

Для команд `setup | run | test | check | format | build | doctor | self-test` определить:

- purpose;
- syntax;
- inputs/options;
- stdout/stderr contract;
- stable exit codes;
- read/write behavior;
- prerequisites;
- success oracle;
- failure classes;
- side effects;
- idempotency;
- examples;
- CI mapping.

Обязательные invariants:

- `--help` выполняется без writes;
- failure не возвращает success exit;
- required `NOT_RUN` не агрегируется в `PASS`;
- docs, CLI, CI и tests называют один official entrypoint.

### 7.6. Подэтап D2.4 — scaffold safeguards и recovery

До first scaffold mutation определить:

- preflight input/output;
- allowed-path normalization;
- intended/actual diff reconciliation;
- atomic write или journal;
- partial-write detection;
- interruption points;
- cleanup/resume rules;
- idempotent retry boundary;
- preservation of user/out-of-scope state;
- redaction/secret checks;
- scaffold rollback boundary;
- post-recovery validation.

### 7.7. Подэтап D2.5 — scaffold acceptance package

Сформировать executable validation matrix минимум для:

| Case | Expected observable result |
|---|---|
| Clean checkout setup | Environment готов, expected tree создан |
| Repeated setup | Нет duplicated/corrupted state |
| Missing dependency | Non-zero terminal result и correction hint |
| Wrong runtime version | Fail-closed до mutation |
| `--help` | Zero writes |
| Dirty unrelated user file | Сохранён и исключён из candidate |
| Path traversal/symlink escape | Отклонён |
| Interruption during write | Partial state detected and recoverable |
| Doctor after setup | Exact checks и honest `NOT_RUN` |
| CI/local parity | Одинаковый official check surface |

### 7.8. Подэтап D2.6 — first implementation Task Brief

Создать один `Task-001-Scaffolding.md`.

Task включает:

- smallest coherent scaffold slice;
- exact repository/baseline requirement;
- allowed/forbidden paths;
- allowed/forbidden operations;
- created tree;
- command behavior;
- validation matrix;
- required Evidence;
- stop conditions;
- correction boundary;
- proposed authorization form.

Не включать Product Runtime behavior.

### 7.9. D2 acceptance

- чистый checkout можно мысленно и инструментально провести от setup до checks без скрытого решения;
- каждая write имеет recovery contract;
- commands имеют stable behavior и exit semantics;
- tests проверяют не только наличие files;
- Task-001 не требует coding agent выбрать topology/toolchain;
- Task-001 связан с exact accepted decisions;
- developer handoff для Task-001 не содержит unresolved material choices.

### 7.10. Результат D2

```text
AOS_SCAFFOLDING_CONTRACT_R1
+ scaffold validation matrix
+ Task-001-Scaffolding
+ DSP-001
```

## 8. D3 — документация постоянного рабочего ядра

### 8.1. Цель

Описать постоянные contracts и mechanisms до первого потребляющего их pipeline step.

### 8.2. Главный artifact

Создать `AOS_CORE_CONTRACT_R1.md`.

Документ делится на implementation slices; один Task Brief готовится только для ближайшего slice.

### 8.3. Порядок core slices

```text
C1 Contracts + closed statuses
→ C2 Authority + permissions
→ C3 Project Memory + immutable records
→ C4 Doctor / Self-Test + read-only Status / Next / Details
→ C5 Registries + Context Pack
→ C6 Task-local coordinator
→ C7 Product Recovery + scoped executor foundation
```

### 8.4. C1 — data contracts и Result Contract

Обязательная документация:

- contract catalog и versioning rules;
- exact schemas для required records;
- required/optional fields;
- closed enums;
- null/empty/unknown semantics;
- strict load/validation path;
- serialization/canonicalization;
- migration/compatibility boundary;
- schema/runtime drift checks;
- valid и invalid examples.

Минимальные records:

- Intent Record;
- Product Spec;
- Feature Contract;
- ADR;
- Task Brief;
- Execution Authorization;
- Preflight/Preview;
- Execution/Stage Record;
- ValidationEnvelope;
- Evidence Record;
- Human Decision Record;
- Project Memory/Handoff;
- Git Delivery Record.

### 8.5. C2 — authority и permissions

Документировать:

- authority precedence per fact class;
- Action Trust Boundary;
- permission classifier;
- human decision authenticity;
- authorization creation, expiry, consumption и invalidation;
- exact binding к task/subject/stage/operations/paths;
- UI/generated/external content non-authority;
- protected/destructive/sensitive stop rules;
- denied-action record;
- negative authorization fixtures.

### 8.6. C3 — Project Memory и immutable records

Документировать:

- единственного owner current lifecycle state;
- schema и exact path после human decision;
- atomic read/write;
- repository/candidate identity binding;
- stage, blockers, decisions, permissions и one next action;
- ссылки на immutable Task Brief, Evidence и Stage Reports;
- freshness/stale detection;
- resume algorithm без истории чата;
- conflict resolution;
- no duplicate current-state owner.

Обязательные resume cases:

- clean resume;
- stale HEAD;
- changed worktree;
- missing/corrupt memory;
- conflicting index;
- expired authorization;
- candidate changed after freeze.

### 8.7. C4 — Doctor, Self-Test и read-only UX

Для маршрута `run → doctor → status → next → details` определить:

- user-facing inputs/outputs;
- source owners, которые читает каждая command/view;
- zero-write contract;
- freshness explanation;
- beginner-readable result;
- exact distinction `PASS / FAIL / BLOCKED / UNKNOWN / NOT_RUN`;
- one next action;
- machine-readable и human-readable output;
- exit codes;
- unavailable owner behavior.

### 8.8. C5 — registries и Context Pack

Документировать отдельно:

- Product Feature Registry;
- Execution/Verification Registry;
- rebuild rules;
- source links/digests;
- stale index detection;
- relation `feature → function → task → contract → tests`;
- Context Pack selection algorithm;
- inclusion rationale;
- freshness check;
- size/budget rule;
- exclusion of irrelevant sources;
- no authority expansion.

### 8.9. C6 — task-local coordinator

Документировать finite transition table:

| Current terminal record | Allowed next run | Required condition | Forbidden implicit action |
|---|---|---|---|
| `PLAN + HUMAN_AUTHORIZATION_REQUIRED` | None | Exact human authorization | Auto-EXECUTE |
| `EXECUTE + PASS + frozen` | `VALIDATE` when required | Same exact candidate | New task activation |
| `EXECUTE + FAIL/BLOCKED/UNKNOWN` | None | Human/new bounded correction | Auto-retry |
| `VALIDATE + PASS` | `REVIEW` | No candidate mutation | Simulated acceptance |
| `VALIDATE + finding` | None | New correction boundary | Validation fixing subject |
| `REVIEW` | None | Human decision | Auto-delivery |

### 8.10. C7 — Product Recovery и scoped executor foundation

До первой Product Runtime write документировать:

- executor inputs only from exact authorization;
- operation journal;
- pre-write failure handling;
- partial-write detection;
- intended/actual reconciliation;
- bounded resume;
- rollback boundary;
- destructive rollback authorization;
- post-recovery validation;
- candidate freeze;
- write-after-freeze rejection.

### 8.11. Documentation Slice Package для каждого C-slice

Для `C1–C7` documentation agent создаёт:

1. section-level contract;
2. examples and fixtures list;
3. acceptance/negative/recovery matrix;
4. traceability to `FTR-*`, `C-*` и `LES-*`;
5. один Task Brief только для ближайшего not-implemented slice;
6. proposed next Task Brief outline, не executable backlog item;
7. DSP manifest.

### 8.12. D3 acceptance

- core order соответствует first-consumer gates;
- один owner существует для lifecycle state;
- registries являются derived/rebuildable;
- status/read-only routes не мутируют state;
- Evidence не открывает permissions;
- required `NOT_RUN` предотвращает `PASS`;
- recovery описан до write;
- coordinator не выбирает next task;
- coding agent не должен изобретать schema, statuses или authority behavior.

### 8.13. Результат D3

```text
AOS_CORE_CONTRACT_R1
+ C1–C7 validation matrices
+ one current Task-xxx
+ sequential DSPs as slices become current
```

## 9. D4 — документация pipeline по трём частям

### 9.1. Цель

Описать один end-to-end greenfield journey от идеи до принятого результата и безопасной точки продолжения.

### 9.2. Главный artifact

Создать `AOS_PIPELINE_CONTRACT_R1.md`.

Документ должен иметь три части и один общий state-transition view. Он не создаёт отдельный owner для facts, уже принадлежащих Product Spec, Feature Contract, Task Brief или Project Memory.

## 9.3. Part 1 — проектирование и подготовка задачи

### P1.1. Intake contract

Определить:

- full-spec и incomplete-idea entry profiles;
- original input preservation;
- actor/problem/outcome/current workaround;
- goals/non-goals/constraints;
- assumptions/unknowns;
- sensitive/provider flags;
- progressive question depth;
- material-question rule;
- stop before product choice.

### P1.2. Product Spec contract

Определить:

- problem и user segments;
- JTBD;
- goals/non-goals;
- user journeys;
- product boundary;
- success signals/metrics;
- dependencies/risks;
- acceptance;
- open decisions;
- relation Product Spec ↔ Feature Contract.

### P1.3. Optional UX-skeleton contract

Только при UI/access complexity:

```text
approved scenarios
→ access model
→ UX object inventory
→ grouping/navigation
→ screen map
→ states/errors/recovery
→ human review
```

UX-skeleton не выбирает styling и не заменяет behavior contract.

### P1.4. Feature selection и Feature Contract

Для selected slice generic dossier превращается в exact contract:

- actors;
- trigger/preconditions;
- exact inputs/outputs/schemas;
- states/transitions;
- main flow;
- failures/recovery;
- dependencies;
- authority boundaries;
- observable acceptance;
- executable negative cases;
- non-goals;
- remaining research questions;
- human disposition and exact revision identity.

### P1.5. Targeted research / ADR

Research запускается только для named material gap:

```text
question → exact repo/ref/commit/path → high-signal evidence
→ classified finding → rejected legacy complexity → remaining unknown
```

ADR создаётся только для decision, не разрешённого accepted contract. Он содержит options, tradeoffs, evidence, human-selected option, consequences и reversal conditions.

### P1.6. Lazy decomposition и Task Brief compiler

Документировать:

- правило выбора next smallest executable task;
- material reasons для sub-stage;
- dependency checks;
- task completeness rules;
- exact Task Brief schema;
- validation matrix generation;
- preflight and preview;
- compact decision/authorization package;
- запрет full backlog и auto-next.

### Part 1 exit contract

```text
Exact Task Brief
+ validation matrix
+ preflight/preview
+ proposed authorization form
→ Permission: HUMAN_AUTHORIZATION_REQUIRED
```

## 9.4. Part 2 — выполнение и проверка

### P2.1. Authorization recheck

Определить:

- authorization identity;
- exact task/subject binding;
- allowed stage/operations/paths;
- expiry/consumption;
- repository/branch/HEAD/worktree re-preflight;
- stale or mismatched stop behavior.

### P2.2. Scoped execution

Определить:

- one causal change;
- journaled durable mutations;
- no unrelated cleanup;
- scope expansion stop;
- out-of-scope user-state preservation;
- bounded technical correction cycles;
- max cycles and escalation rule;
- no hidden next stage.

### P2.3. Tests, Evidence и reconciliation

Связать каждый requirement с:

- positive acceptance test;
- negative case;
- relevant regression;
- Evidence method/locator;
- required/optional status;
- expected terminal result;
- limitation classification.

### P2.4. Freeze и Stage Report

Определить:

- candidate identity;
- freeze mechanism;
- write-after-freeze invalidation;
- terminal Stage Report fields;
- checks run/not run;
- changed paths;
- limitations/unknowns;
- authorization consumption;
- stop reason.

### P2.5. Separate VALIDATE

Определить:

- when independent validation is required;
- exact frozen subject;
- read-only enforcement;
- acceptance/scope/regression checks;
- self-reference detection;
- no-fix rule;
- finding and correction transition.

### P2.6. Review Package

Один human-facing document содержит:

- purpose и user impact;
- before/after;
- exact changed paths;
- acceptance Evidence;
- negative cases;
- `NOT_RUN`/limitations;
- findings/deviations;
- recommendation;
- decision options;
- one next action.

### Part 2 exit contract

```text
Frozen exact candidate
+ immutable reports/Evidence
+ validation result when required
+ Review Package
→ Human decision: NOT_RUN
```

## 9.5. Part 3 — принятие, завершение и продолжение

### P3.1. Human Decision Record

Определить:

- exact candidate binding;
- actor/date/action provenance;
- `ACCEPT | NEEDS_CHANGES | REJECT | DEFER`;
- generated decision rejection;
- consequences without implicit permissions.

### P3.2. Correction loop

Определить:

- new bounded correction task;
- invalidation of old authorization;
- candidate/version change;
- required re-validation;
- max bounded cycles within unchanged scope;
- return to human when product/architecture/scope/risk changes.

### P3.3. Durable state transition

Определить:

- authorized update to Project Memory;
- Registry rebuild/update rules;
- immutable links to reports/decision;
- one next action;
- read-only proposed update when mutation authorization absent.

### P3.4. Git lifecycle

Для `Commit`, `Push`, `Merge`, `Release` отдельно определить:

- decision/permission record;
- fresh preflight;
- exact candidate binding;
- allowed operation;
- terminal record;
- invalidation on later mutation;
- `NOT_RUN` handling.

### P3.5. Handoff и lesson proposal

Определить:

- repository and candidate identity;
- task/result/decision;
- actual changes;
- checks and blockers;
- current permission state;
- one next action;
- lesson proposal only from observed repeatable signal;
- no automatic next slice activation.

### Part 3 exit contract

```text
Human Decision Record
+ authorized state/Git consequences or honest NOT_RUN
+ updated Project Memory
+ compact handoff
+ one next action
```

### 9.6. D4 acceptance

- один example проходит через все три части без chat context;
- every state transition names owner, input, output and gate;
- product decision, execution authorization, technical result, human decision и Git permissions не смешиваются;
- failures/recovery описаны для каждого write-capable step;
- correction loops не создают autonomous self-heal;
- pipeline не требует full backlog;
- developer agent получает exact task, а не обязан проектировать процесс заново.

### 9.7. Результат D4

```text
AOS_PIPELINE_CONTRACT_R1
+ end-to-end state/sequence model
+ validation matrices per Part
+ one current Task-xxx
+ current DSP
```

## 10. D5 — сквозная проверка и Developer Handoff Package

### 10.1. Цель

Доказать, что документация достаточна для реализации exact slice независимым coding agent без истории чатов и скрытых решений.

### 10.2. Подэтап D5.1 — documentation topology audit

Проверить:

- один owner на fact class;
- отсутствие contradictory statuses;
- absence of duplicate current state;
- все links существуют и portable;
- derived indexes marked non-authoritative;
- DRAFT/accepted/observed facts не смешаны;
- selected feature revision pinned;
- mutable repository facts требуют fresh observation;
- handoff не содержит stale identity.

### 10.3. Подэтап D5.2 — requirements-to-tests traceability

Для exact Task Brief создать matrix:

| Requirement ID | Contract owner | Implementation surface | Positive test | Negative test | Evidence | Required? |
|---|---|---|---|---|---|---|

Ни один mandatory acceptance criterion не остаётся только prose claim.

### 10.4. Подэтап D5.3 — independent-agent simulation

Read-only reviewer, не использующий историю чатов, должен ответить:

1. Какой exact user outcome реализуется?
2. Какой repository/baseline является subject?
3. Какие files/operations разрешены и запрещены?
4. Какие contracts нельзя менять?
5. Что должно наблюдаться при успехе?
6. Какие negative cases обязательны?
7. Как обнаружить partial failure?
8. Как восстановиться без потери user state?
9. Какие checks required, optional или `NOT_RUN`?
10. Где coding agent должен остановиться?
11. Какой результат требует human decision?
12. Какие Git actions не разрешены?

Любой неоднозначный ответ становится named finding, а не заполняется inference.

### 10.5. Подэтап D5.4 — Developer Handoff Manifest

Создать `DEVELOPER_HANDOFF_R1.md` со следующими exact ссылками:

```yaml
handoff:
  package_id:
  package_revision:
  generated_at:
  documentation_status:
  human_acceptance:
  implementation_repository:
  repository_identity_requirement:
  selected_feature:
  selected_feature_revision:
  user_outcome:
  active_task:
  active_task_revision:
  contract_sources: []
  accepted_decisions: []
  relevant_adrs: []
  context_pack: []
  allowed_paths: []
  forbidden_paths: []
  allowed_operations: []
  forbidden_operations: []
  required_checks: []
  optional_checks: []
  required_negative_cases: []
  evidence_requirements: []
  recovery_contract:
  stop_conditions: []
  material_unknowns: []
  out_of_scope_state: []
  proposed_risk_profile:
  assigned_risk_profile: UNASSIGNED
  execution_authorization: NOT_RUN
  Git_authorizations:
    commit: NOT_RUN
    push: NOT_RUN
    merge: NOT_RUN
    release: NOT_RUN
  next_required_action:
  stop: true
```

Manifest — navigation/identity layer. Facts остаются у source owners.

### 10.6. Подэтап D5.5 — package freeze and validation

1. Зафиксировать exact revisions/digests всех package files.
2. Проверить отсутствие изменений после freeze.
3. Выполнить read-only semantic validation.
4. Записать checks run/not run, findings и limitations.
5. Выдать technical result.
6. Остановиться на human review.

### 10.7. D5 acceptance

Package получает documentation technical `PASS` только если:

- все required content checks выполнены;
- нет blocking contradiction;
- required `NOT_RUN` отсутствуют;
- независимый reviewer не нуждается в chat context;
- coding agent не должен принимать protected product/architecture decisions;
- exact Task Brief согласован с contracts;
- acceptance и negatives executable;
- recovery и stop rules достаточны;
- package frozen and identity-bound;
- technical `PASS` не записан как human acceptance или authorization.

### 10.8. Результат D5

```text
Frozen Documentation Slice Package
+ Documentation Validation Report
+ Developer Handoff Manifest
→ HUMAN_REVIEW_REQUIRED
```

## 11. Минимальное содержание exact Task Brief

Каждый `Task-xxx.md` должен содержать:

```yaml
task:
  task_id:
  title:
  stage: EXECUTE
  goal:
  user_outcome:
  feature_id:
  feature_contract_revision:
  parent_stage:
  repository:
  repository_identity_requirement:
  baseline_requirement:
  dependencies: []
  in_scope: []
  out_of_scope: []
  allowed_paths: []
  forbidden_paths: []
  allowed_operations: []
  forbidden_operations: []
  required_behavior: []
  invariants: []
  assumptions: []
  material_unknowns: []
  acceptance_criteria: []
  negative_scenarios: []
  validation_matrix: []
  evidence_requirements: []
  recovery_requirements: []
  correction_boundary:
  proposed_risk_profile:
  assigned_risk_profile: UNASSIGNED
  stop_conditions: []
  terminal_report_schema:
  execution_authorization: NOT_RUN
  Git_authorization: NONE
```

Prose до YAML объясняет user outcome, before/after, constraints и non-obvious decisions простым языком.

Task Brief запрещено объявлять developer-ready, если coding agent должен самостоятельно определить:

- что считается успехом;
- какой behavior нужен пользователю;
- какую architecture выбрать;
- какую schema считать authoritative;
- какие paths можно менять;
- какие negative cases обязательны;
- что делать при partial write;
- где остановиться.

## 12. Алгоритм documentation agent

### 12.1. Startup

1. Определить repository root и действующие instructions.
2. Прочитать `docs/00_Core.md` полностью.
3. Определить текущий `D-stage`, target artifact и downstream consumer.
4. Читать только релевантные sections `01–06`.
5. Прочитать current Project Memory и exact active documentation task.
6. Проверить mutable repository facts read-only.
7. Составить authority/unknown/conflict inventory.

### 12.2. Drafting

1. Обновлять существующего owner, если fact class уже имеет owner.
2. Создавать новый artifact только для distinct implementation boundary.
3. Сначала определить behavior и contracts, затем implementation task.
4. Generic dossier fields заменить exact examples/schemas.
5. Каждый acceptance связать с Evidence.
6. Добавить negative и recovery cases из релевантных `LES-*`.
7. Сформировать один current Task Brief.
8. Дальние задачи оставить outlines/dependencies, не executable backlog.

### 12.3. Questions to human

Documentation agent задаёт вопрос только если выбор меняет:

- user problem/outcome/scope/priority;
- selected feature/vertical slice/disposition;
- user-visible behavior or data contract;
- architecture/repository/toolchain/dependency;
- privacy/security/provider boundary;
- human decision authenticity;
- `Risk Profile`;
- protected/destructive operation;
- acceptance;
- execution or Git permission.

Безопасные обратимые technical details агент выбирает самостоятельно и фиксирует rationale только если решение non-obvious.

### 12.4. Bounded corrections

До трёх correction cycles разрешены внутри того же documentation task, если не меняются:

- product outcome;
- architecture decision;
- selected feature/scope;
- authority/permission boundary;
- risk classification requirement;
- downstream Task Brief identity.

После трёх циклов или material boundary change агент останавливается с one next action.

### 12.5. Terminal report

```yaml
task_id:
stage: PLAN
result:
documentation_stage:
starting_identity:
ending_identity:
artifacts_created: []
artifacts_updated: []
owners_changed: []
decisions_required: []
checks_run: []
checks_not_run: []
findings: []
limitations: []
material_unknowns: []
developer_handoff_status:
implementation_authorization: NONE
Git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
next_required_action:
stop: true
```

## 13. Quality gates документации

### Gate Q1 — Authority

- claims classified;
- human decisions have provenance;
- inventory presence not treated as selection;
- no legacy authority promotion.

### Gate Q2 — Ownership

- one fact class, one owner;
- Project Memory is sole current lifecycle owner;
- registry/handoff/dashboard remain derived.

### Gate Q3 — Behavioral completeness

- actors, trigger, inputs/outputs, states, transitions;
- success, failures and recovery;
- authority boundaries;
- non-goals.

### Gate Q4 — Implementation determinacy

- topology/toolchain/interfaces decided in required boundary;
- schemas/examples available;
- dependencies and sequence explicit;
- coding agent has no hidden product/architecture choice.

### Gate Q5 — Scope and permissions

- allowed/forbidden paths and operations;
- exact repository identity requirement;
- no default authorization;
- Git permissions separate.

### Gate Q6 — Validation

- observable acceptance;
- executable negative cases;
- required vs optional checks;
- honest `NOT_RUN`;
- Evidence mapping.

### Gate Q7 — Recovery

- pre-write failure;
- partial-write detection;
- journal/atomicity;
- resume/rollback boundary;
- post-recovery validation.

### Gate Q8 — Handoff

- exact revisions and identities;
- task-scoped context only;
- no chat dependency;
- one next action;
- terminal stop.

## 14. Traceability к feature families

Все mappings ниже — `PROPOSAL`; item-level selection остаётся human decision.

| Documentation stage | Основные feature candidates | Main developer artifact |
|---|---|---|
| D1 Decisions | `FTR-001`, `003`, `005`, `006`, `016`, `019` | Decision Record |
| D2 Scaffolding | `FTR-004`, `009`, `011`, `014`, `019`, `023`, `030` | Scaffolding Contract + Task-001 |
| D3 Core C1–C2 | `FTR-006`, `011`, `019`, `030` | Core Contract slice |
| D3 Core C3–C6 | `FTR-008`, `011`, `012`, `014`, `016` | Core Contract slice |
| D3 Core C7 | `FTR-009`, `010`, `013`, `014`, `019` | Recovery/Executor slice |
| D4 Part 1 | `FTR-001`, `003`, `005`, `006`, simplified `007`, `009`, `016` | Pipeline Contract Part 1 |
| D4 Part 2 | `FTR-006`, `009`, `010`, `011`, `012`, `013`, `014`, `019` | Pipeline Contract Part 2 |
| D4 Part 3 | `FTR-012`, `014`, `015`, `016`, `025` | Pipeline Contract Part 3 |
| D5 Handoff/Dogfood | `FTR-008`, `011`, `012`, `014`, `016`, `025` | Frozen DSP + Handoff |

Для каждого selected mapping добавить:

```text
D-stage → selected FTR disposition → exact contract revision
→ requirement → task → test → Evidence → human decision
```

## 15. Последовательность документационных задач

Документационные задачи создаются последовательно.

| Order | Documentation task | Выход | Gate следующей задачи |
|---|---|---|---|
| `DOC-001` | Decision gaps + compact decision package | Human decision-ready package | Required decisions answered |
| `DOC-002` | Implementation Decision Record | Accepted exact decision candidate | Human review exact revision |
| `DOC-003` | Следующая revision `02_AGENTS_DRAFT.md` | Bootstrap instruction candidate | Semantic audit |
| `DOC-004` | Scaffolding Contract | Full scaffold behavior | No material unknowns |
| `DOC-005` | Task-001 + DSP-001 | Developer-ready scaffold package | Human review + authorization separately |
| `DOC-006` | Core Contract C1–C2 | Contracts/authority package | C1–C2 documentation PASS |
| `DOC-007` | Core Contract C3–C4 | Memory/doctor/status package | Owner/recovery checks PASS |
| `DOC-008` | Core Contract C5–C7 | Registry/context/coordinator/recovery package | First-consumer gates covered |
| `DOC-009` | Pipeline Contract Part 1 | Idea→Task Brief contract | Part 1 simulation PASS |
| `DOC-010` | Pipeline Contract Part 2 | Execute→Review Package contract | Part 2 recovery/validation PASS |
| `DOC-011` | Pipeline Contract Part 3 | Decision→Handoff contract | Permission separation PASS |
| `DOC-012` | End-to-end traceability and independent simulation | Findings/corrections | All blockers resolved |
| `DOC-013` | Frozen Developer Handoff Package | `HUMAN_REVIEW_REQUIRED` | Human decision |

Эта таблица задаёт documentation sequence, но не является execution authorization. После каждого реализованного slice точный следующий Task Brief пересобирается по observed repository state.

## 16. Human checkpoints

Человеческое участие объединяется в четыре decision-ready точки:

| Checkpoint | Решение человека | Что агент делает самостоятельно до checkpoint |
|---|---|---|
| H1 | Repository, first problem/slice, interface, toolchain, persistence, selected feature dispositions | Gap analysis, preferred options, tradeoffs |
| H2 | Human acceptance exact contracts/Task Brief | Drafting, consistency checks, bounded corrections |
| H3 | Execution Authorization exact DSP | Preflight proposal, scope/validation/recovery package |
| H4 | Candidate acceptance и отдельные Git actions | Technical validation, Review Package, proposed state update |

Нельзя объединять в одно автоматическое решение:

- product choice и execution authorization;
- technical `PASS` и acceptance;
- acceptance и `Commit/Push/Merge/Release`.

## 17. Stop conditions

Documentation agent останавливает только affected work, если:

- required owner отсутствует;
- sources конфликтуют в implementation-affecting fact class;
- first consumer невозможно определить;
- implementation repository/toolchain/slice остаётся `UNDECIDED` для dependent DSP;
- selected feature не имеет human disposition;
- exact contract требует hidden human decision;
- acceptance cannot be observed;
- required negative/recovery case невозможно сформулировать;
- Task Brief scope нельзя сделать machine-checkable;
- package зависит от chat-only fact;
- source revision/identity устарели;
- correction limit исчерпан;
- requested action выходит за documentation authorization.

Безопасный read-only analysis остальных блоков может продолжаться.

## 18. Definition of Documentation Ready for Development

Exact slice получает status `HUMAN_REVIEW_REQUIRED` для передачи только когда:

```yaml
documentation_ready_check:
  user_outcome_exact: PASS
  selected_feature_human_disposition: PASS
  product_contract_exact: PASS
  required_architecture_decisions: PASS
  repository_and_toolchain_boundary: PASS
  data_and_interface_contracts: PASS
  state_failure_recovery_model: PASS
  allowed_forbidden_scope: PASS
  acceptance_executable: PASS
  negative_tests_executable: PASS
  evidence_requirements: PASS
  traceability: PASS
  no_chat_dependency: PASS
  one_fact_class_one_owner: PASS
  package_frozen: PASS
  independent_documentation_validation: PASS
  human_acceptance: NOT_RUN
  execution_authorization: NOT_RUN
  Git_authorization: NONE
```

Если любой required check имеет `NOT_RUN`, `UNKNOWN`, `FAIL` или `BLOCKED`, documentation technical `PASS` недопустим.

## 19. Границы первого документационного цикла

Не создавать заранее:

- полный hierarchical backlog;
- Task Briefs для всех будущих slices;
- full Control Plane;
- multi-agent orchestration contract;
- autonomous self-heal;
- RAG/vector architecture без measured need;
- SaaS/Workbench;
- plugin marketplace;
- regulated-domain architecture;
- automatic Git delivery;
- модуль подключения AOS к уже разрабатываемому проекту.

Допустимо оставить dependency outlines и capability-on-demand gates без implementation details.

## 20. Следующий bounded action

Провести human review exact revision этого документа вместе с `planning/00_WORKSPACE.md`; exact identities зафиксированы в `planning/CURRENT.md`. Не запускать `DOC-001` в рамках review или acceptance.

После отдельного exact human acceptance следующим bounded action становится `DOC-001` в `PLAN / read-only`:

```text
На основании docs/00_Core.md и только релевантных sections 01–06
подготовь единый decision-ready package для D1.
Включи только решения, без которых нельзя создать
AOS_SCAFFOLDING_CONTRACT_R1 и выбрать первый vertical slice.
Предложи preferred defaults и tradeoffs, не симулируй human decision,
не создавай runtime-код, не выполняй Git actions.
Доведи exact documentation task до HUMAN_REVIEW_REQUIRED,
выполнив не более трёх bounded correction cycles внутри того же scope.
```

## 21. Текущий статус

```yaml
plan_status: DRAFT
parent_plan_status: DRAFT
documentation_sequence: READY_FOR_HUMAN_REVIEW
documentation_execution: NOT_RUN
DOC-001: NOT_RUN
developer_handoff: NOT_RUN
human_acceptance: NOT_RUN
implementation_readiness: NOT_READY
implementation_authorization: NONE
git_authorization: NONE
next_required_action: HUMAN_REVIEW_EXACT_DOCUMENTATION_PLAN_REVISION
stop: true
```
