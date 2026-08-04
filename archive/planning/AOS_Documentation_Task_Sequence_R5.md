---
artifact_id: AOS-DOCUMENTATION-TASK-SEQUENCE-R5
document_type: DOCUMENTATION_TASK_SEQUENCE
revision: R5
status: DRAFT
fact_class: PROPOSAL
correction_of: AOS-DOCUMENTATION-TASK-SEQUENCE-R4
audit_basis: AOS-DOCUMENTATION-TASK-SEQUENCE-R4-AUDIT-R1
supersedes_if_human_accepted:
  - AOS-DOCUMENTATION-TASK-SEQUENCE-R4
scope:
  - DOCUMENTATION_TASK_ORDER
  - DOCUMENTATION_TO_TASK_CONVERSION_RULES
  - EXTERNAL_EVIDENCE_GATE_DEFINITIONS
excluded_from_scope:
  - IMPLEMENTATION_EXECUTION
  - OBSERVED_EVIDENCE_PRODUCTION
  - REPOSITORY_MUTATION
  - GIT_DELIVERY
target_use: CREATE_CLEAR_SEQUENTIAL_DOCUMENTATION_FOR_LATER_AGENT_IMPLEMENTATION
implementation_repository: UNASSIGNED
implementation_status: NOT_STARTED
external_evidence_status: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
human_review_required: true
human_acceptance: NOT_RUN
initial_wave_if_human_accepted: W0
initial_task_if_human_accepted: SEQ-DOC-001
active_wave: null
active_task: null
---

# AOS — Последовательность создания документации по задачам R5

## 1. Вывод

Документацию AOS следует создавать двумя связанными, но не смешанными контурами:

```text
Контур D — Documentation
contracts → procedures → task candidates → review

Контур X — External implementation / Evidence
target binding → separately authorized implementation
→ independent validation → observed Evidence → human decision
```

Исправленная последовательность:

```text
W0  Sequence, authority, status usage and minimum task contracts
W1  Base Architecture and Base Functions documentation
W2  First Product Runtime Vertical Slice documentation

X1  First-slice implementation and real-task Evidence checkpoint
    — external, separately authorized, initially NOT_RUN

W3  Complete Pipeline Development text contracts
W4  Manual pipeline dogfood protocols

X2  Manual dogfood Evidence checkpoint
    — external, separately authorized, initially NOT_RUN

W5  Bounded runner documentation, one interval package at a time
X3  After each package: implementation / validation / full-route regression

W6  Full Core Cycle Coordinator documentation
X4  Full-core Evidence and human stabilization checkpoint

W7  Conditional Extension Boundary Study
W8  Documentation of one separately selected extension
```

Ключевой порядок:

```text
Base Architecture / Base Functions
→ first Product Runtime slice
→ implementation and manual real-task feedback
→ full Pipeline Development text route
→ manual full-route proof
→ thin coordinator
→ one bounded interval runner
→ full-route regression
→ next bounded interval
→ full core coordinator
→ optional extensions
```

Это не implementation roadmap, а порядок создания документации и расположения внешних evidence gates.

---

## 2. Исправленные дефекты `R3`

| Finding `R3 Audit` | Исправление, сохранённое в `R5` |
|---|---|
| First slice delivery была после Factory и modules | `X1` расположен сразу после `W2` |
| Documentation tasks смешивались с observed Evidence | Введены отдельные `DOCUMENTATION_TASK` и `EXTERNAL_EVIDENCE_GATE` |
| First-slice portable tasks создавались до общего contract | Minimum Portable Task Candidate contract создаётся в `W0` |
| Optional modules блокировали первую implementation wave | `W7–W8` стали conditional branch после `X4` |
| Gate labels конфликтовали с canonical statuses | Используются canonical `technical_result` и `human_decision`; transition вынесен в `gate_effect` |
| `one run — one stage` был ослаблен | Инвариант теперь безусловный для всех runtime packages |
| Все extensions считались одинаковыми modules | Добавлена taxonomy extension kinds и lazy admission |

---

## 3. Статус и ограничения

`R5` является `DRAFT / PROPOSAL`.

Он не:

- принимает себя как active sequence;
- выбирает first segment или first vertical slice;
- меняет `human_disposition` любой `FTR-*`;
- назначает implementation repository;
- выбирает language/toolchain/dependencies;
- создаёт фактическую Evidence;
- разрешает mutation;
- создаёт Execution Authorization;
- разрешает Commit, Push, Merge или Release.

```text
Roadmap ≠ Task Brief
Documentation protocol ≠ observed Evidence
Portable Task Candidate ≠ Target-Bound Task Brief
Technical PASS ≠ human ACCEPT
Human ACCEPT ≠ Execution Authorization
Implementation Evidence ≠ Git permission
```

---

## 4. Authoritative owners

Этот документ владеет только порядком documentation tasks и их dependencies после explicit human acceptance exact revision.

| Fact class | Authoritative owner |
|---|---|
| Project identity, authority, statuses, Minimal Safety Floor | `docs/00_Core.md` |
| Users, problems, product boundaries, journeys | `docs/01_Product.md` |
| Layer boundaries, shared contract classes, data ownership | `docs/02_Architecture.md` |
| Task stages, validation, review, recovery and Git boundaries | `docs/03_Development.md` |
| Lessons and regression candidates | `docs/04_Lessons.md` |
| Research routing and provenance | `docs/05_Reference.md` |
| Feature inventory and dossiers | `docs/06_Features.md` |
| Documentation sequence and dependency order | `R5` only after human acceptance |
| Current progress | separate checklist derived from accepted sequence |
| Actual repository state | direct current repository observation |
| Human decision | exact human-authored or human-verified decision record |

```yaml
artifact:
  path: AOS-3/AOS_Core_Roadmap.md
  artifact_id: AOS-CORE-ROADMAP
  role: HISTORICAL_EVIDENCE_OF_SEPARATE_PORTABLE_PACKAGE
  authority_over_current_documentation_sequence: NONE
  competing_owner: false
  supersession_effect: NONE
```

Coverage matrix не владеет feature disposition. Она только отображает:

```yaml
feature_id:
decision_ref:
observed_human_disposition:
coverage_scope:
last_verified_revision:
```

При расхождении с human decision coverage matrix считается stale.

---

## 5. Два типа work items

### 5.1. `DOCUMENTATION_TASK`

Создаёт только reviewable documentation artifact.

```yaml
work_item_type: DOCUMENTATION_TASK
repository_mutation_scope: DOCUMENTATION_REPOSITORY_ONLY_IF_AUTHORIZED
observed_runtime_evidence: NOT_APPLICABLE
implementation_authorization: NONE
```

Примеры outputs:

- boundary document;
- Product Contract;
- procedure;
- schema;
- task manifest;
- validation plan;
- dogfood protocol;
- runner contract.

### 5.2. `EXTERNAL_EVIDENCE_GATE`

Не является documentation task. Он фиксирует, что для продолжения нужна отдельно выполненная работа над exact subject.

```yaml
work_item_type: EXTERNAL_EVIDENCE_GATE
initial_status: NOT_RUN
requires:
  - exact subject identity
  - separate human authorization when mutation is involved
  - observed Evidence
  - separate human decision
```

Documentation plan может описать gate и expected records, но не может отметить его `PASS` без фактического выполнения.

---

## 6. Canonical status и gate model

### 6.1. Technical result

Используется vocabulary владельца `docs/00_Core.md`:

```text
CONTRACT_VIOLATION
FAIL
BLOCKED
UNKNOWN
NOT_RUN
PASS
HUMAN_REVIEW_REQUIRED
```

### 6.2. Human decision

```text
ACCEPT
NEEDS_CHANGES
REJECT
DEFER
```

Если решение не принималось:

```yaml
decision_record_status: NOT_RUN
human_decision: null
```

### 6.3. Gate effect

`gate_effect` — локальный результат перехода, а не новый technical status и не human decision.

```text
HOLD
RETURN_FOR_CORRECTION
PROCEED_TO_NEXT_DOCUMENTATION_WAVE
ACTIVATE_EXTERNAL_GATE
ACTIVATE_NEXT_RUNNER_PACKAGE
OPEN_CONDITIONAL_EXTENSION_STUDY
```

Пример:

```yaml
technical_result: PASS
decision_record_status: COMPLETED
human_decision: ACCEPT
gate_effect: PROCEED_TO_NEXT_DOCUMENTATION_WAVE
```

Ни `PASS`, ни `gate_effect` сами по себе не создают authority.

---

## 7. Безусловные инварианты

1. Один run выполняет один stage.
2. Terminal result создаёт report и `stop: true`.
3. Новый stage требует нового invocation.
4. Human Task Decision не создаётся runner.
5. Human Risk Profile не назначается runner.
6. Execution Authorization не выводится из Task Brief.
7. Validation не исправляет candidate.
8. Review не мутирует candidate и не симулирует acceptance.
9. Commit, Push, Merge и Release — отдельные stages и permissions.
10. Optional extension не меняет core safety и human authority.
11. Derived index, UI, adapter или registry не становится Source of Truth.
12. Actual Evidence требует exact observed subject.
13. Stale baseline, contract или authorization invalidates dependent task.
14. External gate блокирует только затронутый переход, не read-only analysis.

### Package ≠ runtime stage

Один documentation package может описывать несколько связанных entrypoints. Это не разрешает выполнить их в одном run.

Пример:

```text
RUN-DOC-301 package
  ├─ PREFLIGHT run → report → stop
  ├─ TARGET_BIND run → report → stop
  ├─ TASK_BRIEF_ASSEMBLY run → report → stop
  ├─ HUMAN_TASK_DECISION presentation → stop
  ├─ HUMAN_RISK_PROFILE presentation → stop
  └─ AUTHORIZATION_RECORDING run → report → stop
```

---

## 8. Feature integration и lazy decisions

### 8.1. Human disposition

```text
REQUIRED | OPTIONAL | DEFERRED | REFERENCE_ONLY | REJECTED | UNDECIDED
```

Решения принимаются just-in-time:

| До какого wave | Нужен bounded decision package |
|---|---|
| `W1` | Foundation features only |
| `W2` | First-slice candidates only |
| `W3` | Core Pipeline features only |
| `W7` | Split capabilities and extensions |
| `W8` | One selected extension only |

Остальные features остаются `UNDECIDED` и не блокируют ранние waves.

### 8.2. Core proposal

Пока human decision не принят, это только placement proposal.

```text
FTR-001…FTR-016
FTR-019
```

- `FTR-004` реализуется сначала в минимальной first-start boundary;
- `FTR-007` — только lazy decomposition, без full autonomous backlog;
- `FTR-010` — только scoped one-stage execution;
- `FTR-011` разделяется на foundation doctor и pipeline validation;
- `FTR-014/016/019` остаются core и не выносятся в optional extension.

### 8.3. Split / deferred-depth proposal

| Feature | Accepted invariant used earlier | Feature-specific advanced scope |
|---|---|---|
| `FTR-021` | SoT ownership уже задано `docs/02_Architecture.md` | registry/authenticity enforcement после measured drift |
| `FTR-025` | compact audit/report/lesson proposal | dashboards and analytics later |
| `FTR-029` | portable paths and ownership already required | templates/localization/export later |
| `FTR-030` | strict validation invariant already required | migration tools and broad drift suite later |

Foundation документы ссылаются на accepted invariants. Они не объявляют `FTR-021/025/029/030` selected feature без отдельного decision record.

### 8.4. Extension-kind taxonomy

Не каждая optional capability является runtime module.

| Extension kind | Candidate features |
|---|---|
| `RUNTIME_MODULE` | `FTR-017` when local context index is selected |
| `FACTORY_ADAPTER` | `FTR-018`, `FTR-023` |
| `GOVERNANCE_EXTENSION` | `FTR-020`, advanced `FTR-021` |
| `KNOWLEDGE_PACK` | `FTR-022` |
| `DELIVERY_ADAPTER` | `FTR-024` |
| `OBSERVABILITY_EXTENSION` | advanced `FTR-025` |
| `DOMAIN_MODULE` | separate Medical and Design parts of `FTR-027` |
| `UI_CLIENT` | `FTR-028` |
| `TEMPLATE_PACK` | advanced `FTR-029` |
| `INTERNAL_TOOLING` | advanced `FTR-030` |
| `EXTENSION_SYSTEM_CANDIDATE` | `FTR-026`, only after repeated extension points |

### 8.5. Extension admission

Capability допускается как extension, если:

1. full core route работает без неё;
2. её отключение не повреждает core state;
3. она не создаёт human decision или authority;
4. permissions explicit;
5. failure isolated;
6. removal/recovery defined;
7. interface versioned;
8. measured need exists;
9. более простой dedicated adapter недостаточен.

---

## 9. Формат documentation task

```yaml
task_id:
work_item_type: DOCUMENTATION_TASK
title:
status: DRAFT

purpose:
questions_to_answer: []

authoritative_inputs: []
supporting_inputs: []
feature_refs: []
decision_refs: []

coverage_scope:
excluded_scope:

output_artifact:
output_path:
required_sections: []

depends_on: []
unlocks: []

review_criteria: []
negative_scenarios: []
known_unknowns: []
invalidation_conditions: []

external_gate_created: null

technical_result: NOT_RUN
decision_record_status: NOT_RUN
human_decision: null
gate_effect: HOLD

implementation_authorized: false
git_operations:
  commit: false
  push: false
  merge: false
  release: false

next_required_action:
stop: true
```

### Contract completeness

Capability/stage contract отвечает минимум на:

1. purpose/user value;
2. actors;
3. trigger/preconditions;
4. inputs/outputs;
5. states/transitions;
6. owner;
7. dependencies;
8. authority boundary;
9. failure classes;
10. recovery;
11. acceptance;
12. negative scenarios;
13. downstream consumer;
14. invalidation conditions;
15. one next action.

---

# 10. `W0` — Sequence, authority and minimum task contracts

## Цель

Создать минимальную navigation/sequence основу без принятия всех future features заранее.

| Task | Output | Depends on |
|---|---|---|
| `SEQ-DOC-001` | `planning/AOS_Authoritative_Owner_Map_R1.md` | accepted baseline |
| `SEQ-DOC-002` | `AOS_Documentation_Task_Manifest_R1.md` | `SEQ-DOC-001` |
| `SEQ-DOC-003` | `AOS_Gate_Status_Usage_Profile_R1.md` | `docs/00_Core.md`, `SEQ-DOC-001` |
| `SEQ-DOC-004` | `AOS_Feature_Coverage_Ledger_R1.md` | `docs/06_Features.md` |
| `TASK-DOC-001` | `AOS_Portable_Task_Candidate_Contract_R1.md` | `docs/02_Architecture.md`, `docs/03_Development.md` |
| `TASK-DOC-002` | `AOS_Target_Binding_And_Task_Conversion_Protocol_R1.md` | `TASK-DOC-001` |
| `SEQ-DOC-005` | `AOS_Documentation_Progress_Checklist_R2.md` | `SEQ-DOC-002…004` |

### `SEQ-DOC-001`

```yaml
task_id: SEQ-DOC-001
work_item_type: DOCUMENTATION_TASK
title: Create Authoritative Owner Map
status: DRAFT
purpose: >
  Создать один repository-local navigation artifact, который связывает
  fact classes с exact authoritative owners и не переопределяет их содержание.
authoritative_inputs:
  - docs/00_Core.md
  - docs/01_Product.md
  - docs/02_Architecture.md
  - docs/03_Development.md
  - docs/04_Lessons.md
  - docs/05_Reference.md
  - docs/06_Features.md
  - planning/AOS_Documentation_Task_Sequence_R5.md
supporting_inputs:
  - AOS-3/AOS_Core_Roadmap.md
  - AOS-3/AGENTS.md
  - AOS-3/development-package-state/CURRENT.md
output_path: planning/AOS_Authoritative_Owner_Map_R1.md
scope:
  - map each relevant fact class to one exact owner
  - classify supporting and historical artifacts
  - identify conflicts, missing owners and stale routes
  - define source precedence references
excluded_scope:
  - changing canonical source content
  - accepting features
  - selecting first vertical slice
  - implementation planning
  - modifying AOS-3
  - Git operations
required_sections:
  - purpose_and_scope
  - source_precedence
  - authoritative_owner_matrix
  - supporting_and_historical_artifacts
  - conflicts_and_unknowns
  - invalidation_conditions
  - next_bounded_action
review_criteria:
  - every owner path exists
  - each fact class has no more than one authoritative owner
  - historical artifacts are not presented as current owners
  - R5 is used only for sequence ownership after human acceptance
  - no content from owners is silently redefined
  - all conflicts and unknowns are explicit
negative_scenarios:
  - missing owner path
  - duplicate owner for one fact class
  - historical roadmap treated as current authority
  - roadmap treated as implementation authorization
  - inferred owner used without project evidence
invalidation_conditions:
  - accepted owner path changes
  - source-precedence rules change
  - a new exact human decision changes ownership
  - active roadmap revision changes
technical_result: NOT_RUN
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
next_required_action: READ_ONLY_REVIEW_SEQ_DOC_001_OUTPUT
stop: true
```

### `TASK-DOC-001`

Minimum Portable Task Candidate не содержит:

- repository path;
- branch/HEAD;
- target commands;
- exact toolchain facts;
- Execution Authorization.

Он содержит:

```yaml
task_candidate_id:
contract_revision:
goal:
observable_outcome:
scope_boundary:
requirements: []
acceptance: []
negative_scenarios: []
dependencies: []
target_requirements: []
unknowns: []
invalidation_conditions: []
```

### `TASK-DOC-002`

Описывает:

```text
Portable Task Candidate
→ human repository assignment
→ read-only preflight
→ Target Repository Binding
→ Target-Bound Task Brief
→ Human Task Decision
→ Human Risk Profile
→ Execution Authorization
```

## Gate `W0`

```yaml
technical_result: NOT_RUN
decision_record_status: NOT_RUN
human_decision: null
gate_effect: HOLD
```

Для перехода к `W1`:

- owner map reviewed;
- manifest acyclic;
- canonical status usage preserved;
- minimum portable contract available;
- только Foundation feature decision package готов;
- human decision по exact wave package: `ACCEPT`.

---

# 11. `W1` — Base Architecture and Base Functions

## Цель

Описать минимальную Product Runtime foundation отдельно от Pipeline Development.

Foundation включает:

- architecture skeleton;
- install/First-Start;
- interaction shell;
- state/continuity;
- doctor/self-test;
- foundation recovery;
- Minimal Safety application;
- поддержку first slice.

Foundation не включает:

- full task conveyor;
- full runner;
- generic plugin system;
- module marketplace;
- full Governance;
- RAG/vector DB;
- Workbench/SaaS;
- domain architecture.

| Task | Output | Feature refs | Depends on |
|---|---|---|---|
| `BASE-DOC-001` | Product foundation boundary | — | `W0` |
| `BASE-DOC-002` | Base architecture skeleton | — | `BASE-DOC-001` |
| `BASE-DOC-003` | Accepted core primitives reuse/gap map | `FTR-019` | `BASE-DOC-002` |
| `BASE-DOC-004` | Minimum bootstrap/install/First-Start contract | `FTR-004` | `BASE-DOC-002` |
| `BASE-DOC-005` | Interaction, Status, Next, Details and Tutor contract | `FTR-008` | `BASE-DOC-001` |
| `BASE-DOC-006` | Project state, memory and continuity contract | `FTR-014`, `FTR-016` | `BASE-DOC-002` |
| `BASE-DOC-007` | Doctor, self-test and foundation recovery contract | foundation part `FTR-011`, `FTR-014` | `BASE-DOC-003/004/006` |
| `BASE-DOC-008` | Foundation review package | accepted Foundation scope | `BASE-DOC-001…007` |

### Boundary `BASE-DOC-004`

Первый contract охватывает:

```text
preview
→ install/apply
→ First-Start
→ doctor
→ preservation of user/project state
```

Full reconcile, update orchestration, export, localization и policy overlays не блокируют first slice.

## Gate `W1`

Для перехода:

```yaml
technical_result: PASS
decision_record_status: COMPLETED
human_decision: ACCEPT
gate_effect: PROCEED_TO_NEXT_DOCUMENTATION_WAVE
```

Фактические значения до review остаются `NOT_RUN / null / HOLD`.

---

# 12. `W2` — First Product Runtime Vertical Slice

## Цель

Выбрать и описать один observable user journey до Factory automation.

| Task | Output | Depends on |
|---|---|---|
| `SLICE-DOC-001` | First segment/job/slice decision package | `W1` |
| `SLICE-DOC-002` | Exact first-slice Feature Contract | human slice selection |
| `SLICE-DOC-003` | Slice ADR or `NO_ADR_REQUIRED` | `SLICE-DOC-002` |
| `SLICE-DOC-004` | Slice UX and manual acceptance protocol | `SLICE-DOC-002` |
| `SLICE-DOC-005` | First-slice independent validation plan | `SLICE-DOC-002…004` |
| `SLICE-DOC-006` | First-slice Portable Task Manifest | `TASK-DOC-001`, `SLICE-DOC-002…005` |

Selection criteria:

- identified user problem;
- observable result;
- minimal dependency surface;
- explicit I/O/states/failures/recovery;
- manual testability;
- useful result without full Factory;
- no implicit Git delivery.

`SLICE-DOC-006` использует уже существующий `TASK-DOC-001`; он не создаёт новый competing task schema.

## Gate `W2`

Успешное завершение documentation wave активирует `X1`, а не `W3`.

```yaml
technical_result: PASS
decision_record_status: COMPLETED
human_decision: ACCEPT
gate_effect: ACTIVATE_EXTERNAL_GATE
external_gate: X1_FIRST_SLICE_DELIVERY
```

---

# 13. `X1` — First-slice implementation and real-task Evidence

## Статус

```yaml
work_item_type: EXTERNAL_EVIDENCE_GATE
status: NOT_RUN
implementation_repository: UNASSIGNED
implementation_authorization: NONE
```

Этот gate выполняется вне documentation plan и только по отдельным human decisions.

Required records:

| Record | Initial status |
|---|---|
| Human implementation repository assignment | `NOT_RUN` |
| Read-only target preflight | `NOT_RUN` |
| Target Repository Binding | `NOT_RUN` |
| First Target-Bound Task Brief | `NOT_RUN` |
| Human Task Decision | `NOT_RUN` |
| Human-assigned Risk Profile | `NOT_RUN` |
| Execution Authorization | `NONE` |
| EXECUTE Stage Report | `NOT_RUN` |
| Independent Validation Evidence | `NOT_RUN` |
| Manual real-task cycle Evidence | `NOT_RUN` |
| Human Slice Stabilization Decision | `NOT_RUN` |

### Gate effect

Только exact human `ACCEPT` first-slice stabilization decision разрешает активировать `W3`.

```text
No X1 Evidence
→ W3 may be discussed read-only
→ but detailed Factory automation documentation is not activated
```

Это предотвращает превращение documentation readiness в substitute product progress.

---

# 14. `W3` — Pipeline Development text contracts

## Цель

После first-slice feedback связать весь development route текстовыми contracts до automation.

## 14.1. Full-route interface baseline

| Task | Output |
|---|---|
| `PIPE-DOC-000` | Minimum end-to-end Pipeline Development interface map |

Маршрут:

```text
Problem Interview
→ Project Discovery
→ DRAFT Product Spec
→ Accepted Specification Baseline
→ Decomposition
→ Portable Task Candidate
→ Target assignment / preflight
→ Target Repository Binding
→ Target-Bound Task Brief
→ Human Task Decision
→ Human Risk Profile
→ Execution Authorization
→ EXECUTE
→ VALIDATE / Evidence
→ REVIEW / Human Decision
→ separate Git actions
→ Recovery / Context / Lessons
```

Для каждого handoff:

- producer;
- consumer;
- exact input/output;
- state transition;
- stage entrypoint;
- report/stop;
- human boundary;
- failure class;
- invalidation rule.

## 14.2. Problem, discovery and specification

| Task | Output | Features |
|---|---|---|
| `PIPE-DOC-101` | Problem Interview / Intent Record stage contract | `FTR-001` |
| `PIPE-DOC-102` | Read-only Project Discovery stage contract | `FTR-002` |
| `PIPE-DOC-201` | Product Spec / Feature Passport contract | `FTR-003` |
| `PIPE-DOC-202` | Conditional scenario/access/UX deepening contract | triggered only |
| `PIPE-DOC-203` | Architecture-needed check / ADR stage contract | `FTR-005` |
| `PIPE-DOC-301` | Accepted Specification Baseline contract | `FTR-003` |
| `PIPE-DOC-302` | Requirement traceability and acceptance coverage | core |

`PIPE-DOC-202` активируется только если `PIPE-DOC-201` фиксирует material gap в actors/access/UX flow и человек принимает deepening action.

## 14.3. Decomposition and task conversion

| Task | Output | Features |
|---|---|---|
| `PIPE-DOC-401` | Lazy decomposition / Task Map contract | simplified `FTR-007` |
| `PIPE-DOC-402` | Decomposition-to-Portable-Task mapping | `FTR-006`, reuses `TASK-DOC-001` |
| `PIPE-DOC-501` | Target assignment and read-only preflight contract | `FTR-009`, `FTR-019` |
| `PIPE-DOC-502` | Target Repository Binding contract | `FTR-006` |
| `PIPE-DOC-503` | Target-Bound Task Brief assembly contract | `FTR-006` |
| `PIPE-DOC-504` | Human Task Decision presentation/binding contract | `FTR-006` |
| `PIPE-DOC-505` | Human Risk Profile presentation/binding contract | `FTR-019` |
| `PIPE-DOC-506` | Execution Authorization recording contract | `FTR-006`, `FTR-019` |

`PIPE-DOC-402` не переопределяет portable schema. Он описывает traceable conversion из Task Map.

## 14.4. Execution, validation, review and closure

| Task | Output | Features |
|---|---|---|
| `PIPE-DOC-601` | Scoped EXECUTE stage and Stage Report contract | `FTR-010`, `FTR-019` |
| `PIPE-DOC-701` | Candidate freeze / VALIDATE / Evidence contract | `FTR-011`, `FTR-013` |
| `PIPE-DOC-801` | REVIEW Package / Human Decision binding contract | `FTR-012` |
| `PIPE-DOC-901` | Separate Commit / Push / Merge / Release contracts | `FTR-015` |
| `PIPE-DOC-1001` | Cross-stage recovery / context / invalidation contract | `FTR-014`, `FTR-016` |
| `PIPE-DOC-1002` | Compact audit / incident / lesson contract | core part `FTR-025`, pending decision |

`PIPE-DOC-1002` использует accepted reporting/lesson invariants. Advanced observability остаётся later extension.

## Gate `W3`

```yaml
technical_result: PASS
decision_record_status: COMPLETED
human_decision: ACCEPT
gate_effect: PROCEED_TO_NEXT_DOCUMENTATION_WAVE
```

Actual values remain `NOT_RUN / null / HOLD` until review.

---

# 15. `W4` — Manual pipeline dogfood protocols

## Цель

Создать procedures для проверки text route. Фактическая Evidence производится только в `X2`.

| Task | Output |
|---|---|
| `DOG-DOC-001` | Disposable fixture identity/reset/authorization specification |
| `DOG-DOC-002` | Manual idea-to-portable-task protocol |
| `DOG-DOC-003` | Manual target-binding-to-review protocol |
| `DOG-DOC-004` | Failure/interruption/recovery protocol |
| `DOG-DOC-005` | Evidence collection and measurement schema |
| `DOG-DOC-006` | Contract correction and invalidation protocol |

`DOG-DOC-001` обязательно содержит:

```yaml
subject_identity:
starting_state:
allowed_operations:
forbidden_operations:
reset_procedure:
evidence_paths:
authorization_requirement:
git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
```

Минимальные scenarios:

1. small positive feature;
2. ambiguous intent;
3. stale/dirty target;
4. denied authorization;
5. validation failure;
6. interruption/resume;
7. human `NEEDS_CHANGES`;
8. required check `NOT_RUN`.

## Gate `W4`

Documentation review активирует `X2`.

```yaml
gate_effect: ACTIVATE_EXTERNAL_GATE
external_gate: X2_MANUAL_PIPELINE_DOGFOOD
```

---

# 16. `X2` — Observed manual dogfood Evidence

```yaml
work_item_type: EXTERNAL_EVIDENCE_GATE
status: NOT_RUN
default_subject: DISPOSABLE_FIXTURE
implementation_authorization: NONE
```

Required observed outputs:

| Evidence | Initial status |
|---|---|
| At least two complete manual cycles | `NOT_RUN` |
| One failure/recovery cycle | `NOT_RUN` |
| Handoff/interface defect log | `NOT_RUN` |
| Clarification/scope-drift measurements | `NOT_RUN` |
| Correction Evidence | `NOT_RUN` |
| Human automation-admission decision | `NOT_RUN` |

Automation admission requires:

- proven repetition;
- stable contracts;
- known failures;
- fallback/removal;
- no authority expansion;
- exact human `ACCEPT`.

---

# 17. `W5` — Bounded runner documentation loop

## Цель

Документировать один bounded interval package, затем остановиться до external implementation/Evidence.

### 17.1. Thin cycle coordinator

| Task | Output |
|---|---|
| `RUN-DOC-000` | Thin Cycle Coordinator contract |

Coordinator:

- хранит current stage/state;
- показывает `/status`, `/next`, `/details`;
- проверяет allowed transition;
- запускает не более одного stage per run;
- останавливается после Stage Report;
- не выполняет automatic cascade;
- не создаёт human decisions;
- не переиспользует stale authorization.

### 17.2. Interval documentation packages

| Task | Documentation package | Separate runtime stages inside package |
|---|---|---|
| `RUN-DOC-101` | Intent / Discovery / Specification | `INTAKE`, `DISCOVERY`, `SPECIFICATION`, conditional `ARCHITECTURE_SUPPORT` |
| `RUN-DOC-201` | Decomposition / Portable Task | `DECOMPOSE`, `PORTABLE_TASK_BUILD` |
| `RUN-DOC-301` | Target Binding / Task Authority | `PREFLIGHT`, `TARGET_BIND`, `TASK_BRIEF_BUILD`, decision/risk/auth presentation/record stages |
| `RUN-DOC-401` | Scoped Execution | `EXECUTE` |
| `RUN-DOC-501` | Validation / Review | `VALIDATE`, `REVIEW` |
| `RUN-DOC-601` | Recovery / Context / Git Closure | `RECOVERY`, `HANDOFF`, `COMMIT`, `PUSH`, `MERGE`, `RELEASE` |

Каждый runtime stage имеет:

```text
new invocation
→ exact stage preflight
→ one bounded action or read-only assessment
→ Stage Report
→ stop
```

`COMMIT`, `PUSH`, `MERGE` и `RELEASE` никогда не каскадируются автоматически.

### 17.3. Порядок активации

```text
RUN-DOC-000
→ X3 evidence
→ RUN-DOC-101
→ X3 evidence
→ RUN-DOC-201
→ X3 evidence
→ RUN-DOC-301
→ X3 evidence
→ RUN-DOC-401
→ X3 evidence
→ RUN-DOC-501
→ X3 evidence
→ RUN-DOC-601
→ X3 evidence
```

Следующий package можно обсуждать read-only, но он не становится active implementation candidate до human stabilization предыдущего package.

---

# 18. `X3` — Per-package runner implementation and regression gate

Шаблон применяется после каждого `RUN-DOC-*`.

```yaml
work_item_type: EXTERNAL_EVIDENCE_GATE
package_id:
status: NOT_RUN
```

Required sequence:

```text
accepted runner package contract
→ Portable Task Candidate
→ target assignment/preflight
→ Target-Bound Task Brief
→ Human Task Decision
→ Human Risk Profile
→ Execution Authorization
→ one bounded implementation stage
→ validation appropriate to risk
→ full-route regression
→ human stabilization decision
```

Required records:

- exact package contract revision;
- target binding;
- implementation Stage Report;
- checks and `NOT_RUN`;
- negative fixtures;
- neighbor adapter Evidence;
- full-route regression Evidence;
- remaining limitations;
- human decision.

---

# 19. `W6` — Full Core Cycle Coordinator documentation

## Цель

Скомпоновать проверенные stage entrypoints, не создавая autonomous multi-stage run.

| Task | Output |
|---|---|
| `FULL-DOC-001` | Full core stage graph and transition contract |
| `FULL-DOC-002` | Cross-stage state, provenance and invalidation contract |
| `FULL-DOC-003` | Human checkpoint and permission composition contract |
| `FULL-DOC-004` | Full-cycle E2E protocol and acceptance package |

Full Core Cycle Coordinator:

- координирует несколько runs;
- один run выполняет один stage;
- после каждого stage показывает one next action;
- требует новый invocation;
- останавливается на human gates;
- работает без optional extensions;
- не создаёт autonomous loop;
- не превращает successful technical route в Release authorization.

## Gate `W6`

Review активирует `X4`, а не extension work автоматически.

---

# 20. `X4` — Full-core Evidence and stabilization

```yaml
work_item_type: EXTERNAL_EVIDENCE_GATE
status: NOT_RUN
```

Required Evidence:

1. idea → reviewed implementation;
2. existing repository discovery → bounded task;
3. interruption and resume;
4. protected action blocked;
5. validation failure;
6. human `NEEDS_CHANGES`;
7. separately authorized Git action;
8. no-module core operation;
9. stale state/authorization invalidation;
10. human full-core stabilization decision.

Only exact human `ACCEPT` may produce:

```yaml
gate_effect: OPEN_CONDITIONAL_EXTENSION_STUDY
```

Extensions remain optional.

---

# 21. `W7` — Conditional Extension Boundary Study

## Activation

`W7` is not in the critical path of first slice, core Pipeline Development or first implementation wave.

Prerequisites:

- `X4` full-core Evidence;
- at least one measured extension need;
- human decision to study extension boundary.

| Task | Output |
|---|---|
| `EXT-DOC-001` | Real extension-case inventory |
| `EXT-DOC-002` | Extension-kind classification |
| `EXT-DOC-003` | Dedicated adapter vs shared extension system decision package |
| `EXT-DOC-004` | One reference extension selection package |

### Shared module system admission

`FTR-026` становится active candidate только если:

- существуют минимум два real extension cases;
- у них есть повторяющиеся lifecycle/version/permission needs;
- dedicated adapters создают material duplication;
- core remains independent;
- человек принимает exact `FTR-026` Product Contract.

Если условия не выполнены:

```text
use dedicated adapter / knowledge pack / UI client / domain package
```

Generic plugin marketplace, remote loading и broad admission framework остаются out of scope.

---

# 22. Conditional shared extension-system documentation

Создаётся только после positive `EXT-DOC-003` и human disposition `FTR-026`.

| Task | Output |
|---|---|
| `MOD-SYS-DOC-001` | Minimum shared extension contract |
| `MOD-SYS-DOC-002` | Version/dependency/lifecycle contract |
| `MOD-SYS-DOC-003` | Permission/state/isolation contract |
| `MOD-SYS-DOC-004` | Safe disable/remove/recovery contract |
| `MOD-SYS-DOC-005` | Extension-aware coordinator adapter contract |

Это conditional branch, не prerequisite core.

---

# 23. `W8` — Documentation of one selected extension

Создаётся только один accepted package at a time.

Generic sequence:

```text
<EXT>-DOC-001  Problem and measured-need package
<EXT>-DOC-002  Exact Product Contract
<EXT>-DOC-003  Architecture/permission/state delta
<EXT>-DOC-004  Failure isolation and negative tests
<EXT>-DOC-005  Portable implementation candidates
```

Reserved mappings:

| Extension | Prefix | Kind | Feature basis |
|---|---|---|---|
| Context Index | `CTX-DOC-*` | `RUNTIME_MODULE` | `FTR-017` |
| Provider Router | `ROUTE-DOC-*` | `FACTORY_ADAPTER` | `FTR-018` |
| Governance Enforcement | `GOV-DOC-*` | `GOVERNANCE_EXTENSION` | `FTR-020`, advanced `FTR-021` |
| Pattern Library | `PAT-DOC-*` | `KNOWLEDGE_PACK` | `FTR-022` |
| CI Adapter | `CI-DOC-*` | `FACTORY_ADAPTER` | `FTR-023` |
| Release Assistant | `REL-DOC-*` | `DELIVERY_ADAPTER` | `FTR-024` |
| Advanced Observability | `OBS-DOC-*` | `OBSERVABILITY_EXTENSION` | advanced `FTR-025` |
| Medical Domain | `MED-DOC-*` | `DOMAIN_MODULE` | part of `FTR-027` |
| Design Domain | `DESIGN-DOC-*` | `DOMAIN_MODULE` | part of `FTR-027` |
| Workbench | `UI-DOC-*` | `UI_CLIENT` | `FTR-028` |
| Packaging Extensions | `PACKEXT-DOC-*` | `TEMPLATE_PACK` | advanced `FTR-029` |
| Advanced Contract Tools | `QUAL-DOC-*` | `INTERNAL_TOOLING` | advanced `FTR-030` |

Medical и Design требуют независимых Product Contracts, risk profiles и acceptance.

---

## 24. Recurring documentation-to-implementation conversion lane

Conversion не является финальным `W9`. Он применяется после каждого accepted contract package, впервые после `W2`.

```text
accepted documentation package
→ Portable Task Candidate
→ human target assignment
→ read-only preflight
→ Target Repository Binding
→ Target-Bound Task Brief
→ Human Task Decision
→ Human Risk Profile
→ Execution Authorization
```

Rules:

1. Полностью target-bound создаётся только одна следующая task.
2. Остальные остаются portable.
3. Target facts не угадываются.
4. Contract revision change invalidates dependent candidates.
5. Repository mutation invalidates stale binding.
6. Authorization bind к exact task/subject/stage.
7. Git permissions всегда отдельны.
8. Documentation package может быть accepted, даже если external implementation gate остаётся `NOT_RUN`; но dependent automation wave не активируется.

---

## 25. Порядок выпуска

### Release D1 — Sequence and Foundation

```text
W0
→ W1
```

### Release D2 — First Product Runtime Slice

```text
W2
→ external X1
```

`X1` не является documentation release.

### Release D3 — Pipeline Development text contracts

```text
W3
```

### Release D4 — Manual dogfood protocols

```text
W4
→ external X2
```

### Release D5 — Bounded runner loop

```text
RUN-DOC-000 → X3
RUN-DOC-101 → X3
RUN-DOC-201 → X3
RUN-DOC-301 → X3
RUN-DOC-401 → X3
RUN-DOC-501 → X3
RUN-DOC-601 → X3
```

### Release D6 — Full Core Cycle Coordinator

```text
W6
→ external X4
```

### Conditional Release E1 — Extension study

```text
W7
```

### Conditional Release E2 — One selected extension

```text
W8
```

Modules/extensions не блокируют Releases D1–D6.

---

## 26. Progress tracking

После human acceptance `R5` необходимо создать:

```text
AOS_Documentation_Progress_Checklist_R2.md
```

Он отдельно показывает:

```yaml
documentation_artifact:
review_result:
decision_record_status:
human_decision:
gate_effect:
external_gate_status:
invalidated_by:
blocker:
next_bounded_action:
```

Progress считается по трём независимым осям:

```text
Artifact progress
Review progress
Human acceptance progress
```

External Evidence gates имеют отдельный показатель и не включаются в documentation artifact percentage.

Начальное состояние:

```yaml
active_wave: W0
active_task: SEQ-DOC-001

documentation_tasks_started: 0
documentation_tasks_reviewed: 0
documentation_tasks_human_accepted: 0

external_gates:
  X1: NOT_RUN
  X2: NOT_RUN
  X3: NOT_RUN
  X4: NOT_RUN

implementation_repository: UNASSIGNED
implementation_authorization: NONE
```

---

## 27. Quality criteria

### Product

- first slice даёт observable user result;
- actual first-slice Evidence появляется до detailed Factory automation;
- Factory не выдаётся за Product Runtime;
- optional extensions не блокируют core value.

### Architecture

- one owner per fact class;
- core works without extensions;
- durable state and authority remain core-owned;
- extension kind соответствует реальной integration boundary;
- generic module system требует repeated extension cases.

### Pipeline

- full text route precedes automation;
- manual proof precedes bounded runner;
- one run — one stage;
- each package followed by external regression gate;
- human decisions and permissions never generated by runner;
- Git operations separate.

### Documentation

- protocol does not claim observed Evidence;
- exact output path and owner exist;
- task files created just-in-time;
- later features remain visible but nonblocking;
- no orphan readiness artifacts;
- one next action.

### Agent usability

- no chat history required;
- authoritative inputs exact;
- unknowns explicit;
- target paths only after binding;
- stop conditions explicit;
- invalidation rules explicit.

---

## 28. Что не следует делать

- принимать `R5` без exact human decision;
- создавать все task files одновременно;
- требовать extension decisions before Foundation;
- создавать module system before real extension cases;
- называть UI client, knowledge pack и CI adapter одним runtime plugin type;
- отмечать protocol как Evidence;
- переходить к detailed Factory automation без `X1`;
- создавать first-slice portable tasks без `TASK-DOC-001`;
- использовать noncanonical gate statuses как decisions;
- выполнять несколько stages в одном run;
- выполнять automatic Commit → Push → Merge → Release cascade;
- считать full coordinator autonomous runner;
- выносить `FTR-014`, `FTR-016` или `FTR-019` из core;
- считать split-feature advanced scope accepted без decision record.

---

## 29. Correction closure matrix

| Audit finding | R5 closure |
|---|---|
| `B-01` first slice delayed | Closed by `W2 → X1 → W3` |
| `B-02` docs mixed with Evidence | Closed by work-item separation and `X1–X4` |
| `B-03` portable contract inversion | Closed by `TASK-DOC-001` in `W0` |
| `B-04` modules in critical path | Closed by conditional `W7–W8` after `X4` |
| `B-05` noncanonical statuses | Closed by §6 canonical model |
| `B-06` one-stage invariant weakened | Closed by §§7 and 17 |
| `M-01` universal module system too early | Closed by `EXT-DOC-003` admission decision |
| `M-02` all extensions treated as modules | Closed by extension-kind taxonomy |
| `M-03` deferred feature fragments in Foundation | Closed by direct accepted invariant references |
| `M-04` coverage matrix as disposition owner | Closed by decision-ref mirror model |
| `M-05` too many early decisions | Closed by just-in-time feature decisions |
| `M-07` independent first-slice validation absent | Closed by `SLICE-DOC-005` and `X1` |
| `M-08` dogfood subject insufficient | Closed by `DOG-DOC-001` fields |

Closure означает исправление design defect в proposal, а не independent validation или human acceptance.

---

## 30. Итоговая последовательность

```text
Accepted baseline
→ human review R5

W0 sequence/minimum task contracts
→ W1 Base Architecture and Base Functions
→ W2 first-slice documentation
→ X1 separately authorized first-slice implementation and Evidence

→ W3 complete Pipeline Development text contracts
→ W4 dogfood protocols
→ X2 observed manual dogfood Evidence

→ W5 one bounded runner package
→ X3 implementation/validation/full-route regression
→ repeat package-by-package

→ W6 Full Core Cycle Coordinator documentation
→ X4 full-core Evidence and human stabilization

→ optional W7 extension boundary study
→ optional W8 one selected extension
```

## Один следующий bounded action

Провести read-only audit exact `AOS_Documentation_Task_Sequence_R5.md`.

Audit должен проверить:

1. `W2 → X1 → W3` dependency;
2. отсутствие observed Evidence внутри documentation tasks;
3. canonical status/decision vocabulary;
4. unconditional `one run — one stage`;
5. отсутствие extensions в core critical path;
6. coverage `FTR-001…FTR-030`;
7. отсутствие competing owners;
8. достаточность `W0` для создания первой exact task `SEQ-DOC-001`.

До окончания review:

```yaml
documentation_task_creation: NOT_STARTED
implementation_repository: UNASSIGNED
external_evidence: NOT_RUN
execution_authorization: NONE
git_operations: NOT_RUN
```
