---
document_id: AOS-CORE-ROADMAP
document_type: PRIMARY_DOCUMENTATION_PIPELINE
revision: R3
supersedes_revision: R2
status: DRAFT
authority: PROPOSAL
basis: HUMAN_CONFIRMED_DIRECTION
scope: PRIMARY_DOCUMENTATION_CREATION
source_repository: NMF13579/notebook
target_path: AOS-3/AOS_Core_Roadmap.md
implementation_authorization: NONE
git_authorization: NONE
human_review_required: true
---

# AOS Core — Documentation Roadmap

## 1. Назначение и граница

Этот Roadmap — единственный pipeline owner последовательного создания первичной документации AOS. Он определяет, какие функциональные этапы нужно описать, зачем нужна их документация, какие `FTR-*` служат источниками, какие Task подготовлены и что остаётся сделать.

Roadmap не заменяет accepted owners в `docs/00_Core.md` — `docs/06_Features.md` и не повторяет полные feature dossiers.

```text
Создание документации
≠ реализация AOS
≠ implementation readiness
≠ Execution Authorization
≠ Commit / Push / Merge / Release
```

Этот документ:

- остаётся `DRAFT` и `PROPOSAL`;
- не выбирает first user/job или first vertical slice;
- не выбирает implementation architecture, repository, language, framework, database, dependencies или provider;
- не меняет item-level `human_disposition` в `docs/06_Features.md`;
- не создаёт implementation status;
- не создаёт permission на mutation или Git delivery.

## 2. Источники и authority

Работа по каждому пункту начинается с `docs/00_Core.md`, затем использует только релевантные sections остальных owners:

1. `docs/01_Product.md`;
2. `docs/02_Architecture.md`;
3. `docs/03_Development.md`;
4. `docs/04_Lessons.md` — только для применимых failures/regressions;
5. `docs/05_Reference.md` — только при exact targeted gap;
6. `docs/06_Features.md`;
7. этот Roadmap.

Authority применяется в следующем порядке:

```text
current explicit human decision
→ accepted project artifact в его fact class
→ current repository observation
→ DRAFT / PROPOSAL
→ reference material
→ agent inference
```

При conflict или `UNKNOWN` агент фиксирует вопрос и останавливает только затронутое действие. Reference repository не становится requirement без отдельного решения.

## 3. Правила Roadmap

### 3.1 Stable IDs

Roadmap использует отдельный namespace `RMP-###`:

```text
RMP-001
RMP-002
RMP-003
RMP-003.1
```

Правила:

1. ID не переиспользуется.
2. После создания пункт не перенумеровывается.
3. Обозначения `C0`, `S0`, `C1` — `C6` сохраняются как смысловые labels.
4. Подпункт `.N` создаётся только после material boundary decision.
5. Новый пункт или подпункт, предложенный агентом, остаётся `PROPOSAL` до human review.
6. Namespace `RMP-*` не пересекается с Product Problem IDs `P-001` — `P-015` из `docs/01_Product.md`.

### 3.2 Связь с Task

Task создаётся только после подготовки единого `AOS-3/tasks/TASK-TEMPLATE.md`.

```text
AOS_Core_Roadmap.md
→ RMP-XXX
→ task_refs
→ TASK-XXX.md
→ remaining
→ next_action
```

`task_refs` связывает Roadmap item только с реально существующим `TASK-XXX.md`. Task из `FEATURE` или `HUMAN_REQUEST` не становится частью Core или Roadmap автоматически.

Roadmap item описывает documentation outcome. Точная task-scoped specification, acceptance criteria, negative scenarios и clarification принадлежат соответствующему `TASK-XXX.md`, а не Roadmap.

### 3.3 Смысл YAML

YAML в конце каждого пункта является единственным владельцем:

- stable Roadmap ID;
- `source_features`;
- `task_refs`;
- завершённой документационной работы;
- оставшейся документационной работы;
- одного следующего действия пункта.

`completed` и `remaining` не описывают implementation progress. Наличие `FTR-*` в `source_features` означает traceability, а не feature selection.

## 4. Последовательность

| Roadmap item | Сохраняемый label | Предмет документации |
|---|---|---|
| `RMP-001` | `C0` | Core boundary и human decision package |
| `RMP-002` | `S0` | Greenfield Development Scaffold |
| `RMP-003` | `C1` | Product Bootstrap, Install и First-Start |
| `RMP-004` | `C2` | Discovery, intake и reviewed draft specification |
| `RMP-005` | `C3` | Minimal hierarchy, Task format и derived Queue |
| `RMP-006` | `C4` | Bounded execution behavior |
| `RMP-007` | `C5` | Validation, Evidence и Human Decision |
| `RMP-008` | `C6` | Recovery, resume и stabilization |

Dependency-oriented documentation path:

```text
RMP-001
→ RMP-002
→ RMP-003
→ RMP-004
→ RMP-005
→ RMP-006
→ RMP-007
→ RMP-008
```

Стрелка означает documentation dependency по умолчанию, а не automatic transition, feature priority или execution authority.

## 5. Roadmap items

## RMP-001 — C0 — Core Boundary and Human Decision Package

### Зачем нужен этап

Зафиксировать документационную границу AOS Core и подготовить человеку понятную основу для решения о first user/job и smallest Core slice без выбора этих outcomes агентом.

### Ожидаемый результат документации

Подготовлен bounded `TASK-001`, который описывает создание decision-ready comparison: candidate users/jobs, candidate slices, observable outcomes, dependencies, non-goals, material unknowns и вопросы человека.

Само human decision не генерируется и не считается частью завершённой агентской работы.

### Что входит

- граница AOS Core и её non-goals;
- подтверждённые product facts и явные proposals;
- сравнение candidate slices без автоматического выбора;
- relation к Product Spec, Feature Passport и architecture need;
- список решений человека;
- первый кандидат на `TASK-001`.

### Что не входит

- выбор first user/job или first slice агентом;
- принятие feature;
- выбор implementation repository или implementation architecture;
- physical topology, language, framework, database, dependencies или provider;
- implementation planning;
- код, execution и Git operations.

### Связанные features

- `FTR-001`
- `FTR-002`
- `FTR-003`
- `FTR-005`
- `FTR-019`

### Открытые вопросы

- кто является first user и какую job необходимо закрыть первой;
- какой smallest Core slice человек выберет;
- как соотносятся Product Spec и Feature Passport;
- какие implementation decisions должны остаться `UNDECIDED` до отдельного architecture package.

```yaml
pipeline_item:
  id: RMP-001
  source_features:
    - FTR-001
    - FTR-002
    - FTR-003
    - FTR-005
    - FTR-019
  task_refs: []
  completed:
    - ROADMAP_ITEM_DEFINED
  remaining:
    - TASK_TEMPLATE
    - TASK_001
    - HUMAN_REVIEW
  next_action: Prepare TASK-001 after TASK-TEMPLATE.md is reviewed
```

## RMP-002 — S0 — Greenfield Development Scaffold

### Зачем нужен этап

Определить, какая документация потребуется для воспроизводимой development foundation AOS после human decisions, не выдавая scaffold за Product Runtime.

### Ожидаемый результат документации

Создана bounded task-scoped specification Development Scaffold: цели, observable development outcomes, non-goals, safety invariants, acceptance criteria и negative scenarios без выбора physical topology.

### Что входит

- reproducible local development foundation;
- один conceptual local entrypoint;
- test/doctor/self-test expectations;
- Minimal Safety Floor для scaffold;
- честная maturity boundary;
- dependency decisions как явные human inputs.

### Что не входит

- создание implementation repository;
- выбор language, framework, package layout или dependencies;
- dependency installation;
- Product Bootstrap и Product Runtime claims;
- CI/CD, remote gates и release;
- implementation или execution.

### Связанные features

- `FTR-006`
- `FTR-009`
- `FTR-011`
- `FTR-013`
- `FTR-014`
- `FTR-019`

### Открытые вопросы

- target implementation repository;
- language/toolchain/dependency policy;
- acceptable environment and portability boundary;
- minimum scaffold proof that does not claim Product Runtime.

```yaml
pipeline_item:
  id: RMP-002
  source_features:
    - FTR-006
    - FTR-009
    - FTR-011
    - FTR-013
    - FTR-014
    - FTR-019
  task_refs: []
  completed:
    - ROADMAP_ITEM_DEFINED
  remaining:
    - HUMAN_DECISIONS
    - TASK_SPECIFICATION
    - HUMAN_REVIEW
  next_action: Resolve the implementation repository and toolchain decisions before drafting the first RMP-002 Task
```

## RMP-003 — C1 — Product Bootstrap, Install and First-Start

### Зачем нужен этап

Описать безопасный и понятный вход пользователя в AOS через preview-first installation, ownership-aware apply, verification и First-Start.

### Ожидаемый результат документации

Создана точная specification Product Bootstrap с actors, target states, inputs/outputs, ownership conflicts, interruption/recovery behavior, acceptance criteria и negative scenarios.

### Что входит

- read-only target discovery;
- install/update preview;
- managed, user и project ownership boundaries;
- authorized apply как будущее observable behavior;
- post-install verification;
- Tutor / First-Start;
- disable/remove/recovery boundary.

### Что не входит

- реализация installer/updater;
- выбор distribution form или interface;
- silent overwrite или automatic removal;
- remote delivery;
- advanced UI, SaaS или marketplace;
- permission на apply, implementation или Git operation.

### Связанные features

- `FTR-004`
- `FTR-008`
- `FTR-009`
- `FTR-011`
- `FTR-014`
- `FTR-019`

### Открытые вопросы

- package distribution form;
- target compatibility scope;
- exact ownership taxonomy;
- First-Start interface;
- disable/remove and rollback boundaries.

```yaml
pipeline_item:
  id: RMP-003
  source_features:
    - FTR-004
    - FTR-008
    - FTR-009
    - FTR-011
    - FTR-014
    - FTR-019
  task_refs: []
  completed:
    - ROADMAP_ITEM_DEFINED
  remaining:
    - TASK_SPECIFICATION
    - HUMAN_REVIEW
  next_action: Prepare a bounded Product Bootstrap Task after RMP-001 human decisions
```

## RMP-004 — C2 — Discovery, Intake and Reviewed Draft Specification

### Зачем нужен этап

Описать путь от idea или existing brief к reviewed DRAFT specification, сохранив original intent, provenance, uncertainty и human authority.

### Ожидаемый результат документации

Созданы bounded specifications для read-only Project Discovery, Problem Interview, requirements intake, Product Spec/Feature Passport и conditional architecture/UX support. Граница между одной Roadmap item и возможными `RMP-004.N` остаётся human decision.

### Что входит

- read-only Project Discovery;
- Problem Interview и clarification;
- FPF summary как proposal;
- requirements intake;
- DRAFT Product Spec и feature-specific contract;
- conditional UX / Experience Outline;
- Target Project / Feature Architecture Need Check;
- assumptions, conflicts, unknowns и source provenance.

### Что не входит

- mutation пользовательского проекта;
- автоматическое product или architecture decision;
- full design system или Storybook;
- implementation planning;
- task activation;
- создание `RMP-004.N` без material boundary decision.

### Связанные features

- `FTR-001`
- `FTR-002`
- `FTR-003`
- `FTR-005`
- `FTR-008`
- `FTR-016`
- `FTR-019`

### Открытые вопросы

- должен ли `RMP-004` остаться одним пунктом или быть разделён;
- relation Product Spec ↔ Feature Passport;
- FPF и requirements formats;
- conditional UX trigger;
- architecture decision granularity.

```yaml
pipeline_item:
  id: RMP-004
  source_features:
    - FTR-001
    - FTR-002
    - FTR-003
    - FTR-005
    - FTR-008
    - FTR-016
    - FTR-019
  task_refs: []
  completed:
    - ROADMAP_ITEM_DEFINED
  remaining:
    - BOUNDARY_DECISION
    - TASK_SPECIFICATIONS
    - HUMAN_REVIEW
  next_action: Decide whether RMP-004 remains one item or receives material RMP-004.N sub-items
```

## RMP-005 — C3 — Minimal Hierarchy, Task Format and Derived Queue

### Зачем нужен этап

Определить минимальную planning documentation, которая превращает reviewed specification в bounded Task documents и один понятный следующий шаг без full backlog orchestration.

### Ожидаемый результат документации

Созданы единый `TASK-TEMPLATE.md` и bounded specifications для minimal hierarchy, task eligibility, derived Queue и one next action. Task files остаются документационными drafts и не получают implementation lifecycle metadata.

### Что входит

- один human-readable Task template;
- stable hierarchy references;
- lazy decomposition;
- task-scoped specification;
- task eligibility как derived result;
- derived/rebuildable Queue;
- `0..1` recommended next action;
- не более одного conceptual active task в будущем product behavior.

### Что не входит

- полный Spec Kit;
- persistent scheduling;
- batch activation или execution;
- forecasting и velocity management;
- automatic task activation;
- execution journal внутри draft Task;
- status, authorization или Git metadata в `TASK-XXX.md`.

### Связанные features

- `FTR-003`
- `FTR-006`
- minimal subset of `FTR-007`
- `FTR-008`
- `FTR-016`
- `FTR-019`

### Открытые вопросы

- должен ли `RMP-005` быть разделён на hierarchy, Task и Queue sub-items;
- durable hierarchy representation;
- exact eligibility vocabulary;
- queue derivation and tie-breaking;
- minimum Task information sufficient without chat history.

```yaml
pipeline_item:
  id: RMP-005
  source_features:
    - FTR-003
    - FTR-006
    - FTR-007
    - FTR-008
    - FTR-016
    - FTR-019
  task_refs: []
  completed:
    - ROADMAP_ITEM_DEFINED
  remaining:
    - TASK_TEMPLATE
    - BOUNDARY_DECISION
    - TASK_SPECIFICATIONS
    - HUMAN_REVIEW
  next_action: Prepare TASK-TEMPLATE.md in a separately authorized documentation stage
```

## RMP-006 — C4 — Bounded Execution Behavior

### Зачем нужен этап

Описать future AOS behavior для одной bounded mutation с явной human authority, exact preview, scope reconciliation и stop, не превращая documentation Task в executable authorization.

### Ожидаемый результат документации

Создана behavior specification bounded execution capability: actors, trigger, preconditions, inputs/outputs, states, failures, recovery, human/agent boundary, acceptance criteria и negative scenarios.

### Что входит

- Human Activation как будущий product behavior;
- read-only preflight and preview behavior;
- exact authorization boundary;
- one bounded execution behavior;
- partial-write detection and recovery expectations;
- observable result and stop semantics.

### Что не входит

- выполнение Preflight, Authorization или EXECUTE в documentation repository;
- отдельные Preflight, Authorization или Stage Report files;
- execution lifecycle metadata внутри `TASK-XXX.md`;
- automatic retry;
- final validation;
- Commit, Push, Merge или Release;
- runtime implementation.

### Связанные features

- `FTR-006`
- `FTR-009`
- `FTR-010`
- `FTR-014`
- `FTR-019`

### Открытые вопросы

- authorization identity and authenticity mechanism;
- isolation and atomic/journal boundary;
- authorization expiry/consumption semantics;
- Risk Profile vocabulary and thresholds;
- recovery boundary after partial mutation.

```yaml
pipeline_item:
  id: RMP-006
  source_features:
    - FTR-006
    - FTR-009
    - FTR-010
    - FTR-014
    - FTR-019
  task_refs: []
  completed:
    - ROADMAP_ITEM_DEFINED
  remaining:
    - TASK_SPECIFICATION
    - HUMAN_DECISIONS
    - HUMAN_REVIEW
  next_action: Prepare a behavior-only bounded execution Task after RMP-005 documentation is reviewed
```

## RMP-007 — C5 — Validation, Evidence and Human Decision

### Зачем нужен этап

Описать, как AOS проверяет exact candidate без исправлений, связывает acceptance с Evidence и отделяет technical result от human decision.

### Ожидаемый результат документации

Создана bounded behavior specification candidate freeze, read-only validation, Evidence, compact human review и explicit Human Decision с visible `NOT_RUN`, limitations и stale detection.

### Что входит

- candidate identity and freeze behavior;
- diff/scope reconciliation;
- read-only validation;
- Evidence mapped to acceptance;
- compact human review;
- explicit human decision boundary;
- continuity information without creating a separate Handoff file in this package.

### Что не входит

- validation execution в текущем repository;
- исправление findings во время validation;
- generated acceptance;
- отдельные Validation, Evidence, Review, Decision или Handoff files по умолчанию;
- implementation status в Task;
- automatic Git delivery.

### Связанные features

- `FTR-011`
- `FTR-012`
- `FTR-013`
- `FTR-014`
- `FTR-016`
- `FTR-019`

### Открытые вопросы

- exact candidate identity for uncommitted state;
- independent-validation threshold;
- human decision authenticity;
- Evidence persistence and redaction;
- boundary between closure information and Project Memory.

```yaml
pipeline_item:
  id: RMP-007
  source_features:
    - FTR-011
    - FTR-012
    - FTR-013
    - FTR-014
    - FTR-016
    - FTR-019
  task_refs: []
  completed:
    - ROADMAP_ITEM_DEFINED
  remaining:
    - TASK_SPECIFICATION
    - HUMAN_DECISIONS
    - HUMAN_REVIEW
  next_action: Prepare the validation and decision behavior Task after RMP-006 documentation is reviewed
```

## RMP-008 — C6 — Recovery, Resume and Stabilization

### Зачем нужен этап

Описать continuity после interruption, failure или human decision так, чтобы новая session восстанавливала actual state, blockers и один safe next action без hidden retry.

### Ожидаемый результат документации

Создана bounded behavior specification recovery, resume, Project Memory и repeated manual-cycle evaluation с explicit failure paths, recovery limits и stabilization criteria proposals.

### Что входит

- interruption and partial-state recovery;
- repository-derived resume;
- denied-action visibility;
- task-scoped Project Memory;
- comparable manual cycles: success, failure, interruption;
- stabilization findings and proposals;
- one next action.

### Что не входит

- autonomous retry, remediation или self-heal;
- broad automation after one cycle;
- automatic promotion of lessons;
- optional module implementation;
- automatic Commit, Push, Merge или Release;
- claim of stable Core without comparable Evidence.

### Связанные features

- `FTR-008`
- `FTR-011`
- `FTR-012`
- `FTR-014`
- `FTR-016`
- `FTR-019`

### Открытые вопросы

- Project Memory persistence and authenticity;
- resume UX;
- recovery and rollback boundary;
- stabilization metrics;
- required cycle count and admission threshold.

```yaml
pipeline_item:
  id: RMP-008
  source_features:
    - FTR-008
    - FTR-011
    - FTR-012
    - FTR-014
    - FTR-016
    - FTR-019
  task_refs: []
  completed:
    - ROADMAP_ITEM_DEFINED
  remaining:
    - TASK_SPECIFICATION
    - HUMAN_DECISIONS
    - HUMAN_REVIEW
  next_action: Prepare the recovery and resume behavior Task after RMP-007 documentation is reviewed
```

## 6. FEATURE-origin documentation

Feature может получить `TASK-XXX.md` напрямую из `docs/06_Features.md`, если она не обязана быть последовательным Core Roadmap item.

Примеры:

- `FTR-015` — Git lifecycle;
- `FTR-017` — RAG-light;
- `FTR-018` — model routing;
- `FTR-020` — progressive Governance;
- `FTR-022` — patterns library;
- `FTR-025` — observability and incidents;
- `FTR-026` — extensions/plugins;
- `FTR-027` — domain modules;
- `FTR-028` — Workbench/SaaS;
- другие bounded feature subjects после human decision.

```text
FEATURE-origin Task
≠ Core admission
≠ Roadmap insertion
≠ feature acceptance
≠ implementation authorization
```

Новый Roadmap item создаётся только если человек подтверждает, что capability является последовательным этапом этого pipeline.

## 7. Текущие conflicts и unknowns

### Подтверждённые границы

- `RMP-*` используется вместо `P-*`, чтобы не конфликтовать с Product Problem IDs.
- `source_features` в item YAML заменяет отдельную ручную traceability matrix.
- Roadmap больше не владеет полными acceptance/negative scenarios feature dossiers.
- Draft Task не содержит execution journal, authorization metadata или implementation status.
- `C0`, `S0`, `C1` — `C6` сохранены как labels, но не являются execution stages этого documentation repository.

### Material unknowns

- first user/job и first Core slice;
- граница `RMP-004` и необходимость `RMP-004.N`;
- граница `RMP-005` и необходимость `RMP-005.N`;
- implementation repository и implementation architecture;
- Product Spec ↔ Feature Passport relation;
- Project Memory persistence;
- human decision authenticity;
- Risk Profile vocabulary;
- compatibility and provider/privacy boundaries;
- stabilization metrics and cycle threshold.

Эти unknowns блокируют только затронутую documentation specification или claim.

## 8. Текущее состояние пакета

На revision `R3`:

- Roadmap structure подготовлена;
- `RMP-001` — `RMP-008` определены;
- `task_refs` пусты, потому что `TASK-XXX.md` ещё не создавались;
- `AOS-3/tasks/TASK-TEMPLATE.md` ещё не создан;
- first candidate для будущего `TASK-001` связан с `RMP-001`;
- implementation, validation и Git operations не выполнялись.

## 9. Одно следующее действие

Провести human review exact Roadmap revision `R3`.

До отдельного решения:

- не создавать `TASK-TEMPLATE.md`;
- не создавать `TASK-001.md`;
- не изменять accepted `docs/00_Core.md` — `docs/06_Features.md`;
- не выполнять implementation;
- не выполнять Commit, Push, Merge или Release.
