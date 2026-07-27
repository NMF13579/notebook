---
document_id: AOS-CORE-ROADMAP
document_type: CORE_PRODUCT_DELIVERY_ROADMAP
revision: R2
status: DRAFT
authority: PROPOSAL
roadmap_scope: AOS_CORE_DELIVERY
includes_enabling_stage:
  - GREENFIELD_DEVELOPMENT_SCAFFOLD
scaffold_is_product_core_capability: false
optional_module_roadmap_included: false
source_repository: NMF13579/notebook
source_branch_observed_at_r2_write: dev
source_commit_observed_at_r2_write: d783f7d8cd0d2af2fb88fafa23ea16f289ef8ea6
r2_repository_preflight: PASS
target_path_state_before_r2_write: UNTRACKED
target_path: AOS-3/AOS_Core_Roadmap.md
implementation_authorization: NONE
git_authorization: NONE
human_review_required: true
---

# AOS Core Roadmap

## 1. Executive conclusion

Этот документ — `DRAFT`-roadmap поставки AOS Core и отдельного enabling stage `S0 — Greenfield Development Scaffold`. Он синтезирует accepted knowledge baseline в последовательность smallest vertical slices, но не заменяет `docs/`, не является architecture authority, implementation plan, feature selection или разрешением на mutation и Git delivery.

Целевой результат roadmap — **human-directed end-to-end cycle with explicit checkpoints**:

```text
установка AOS в пользовательский repository
→ Tutor / First-Start
→ Project Discovery
→ Problem Interview
→ FPF summary
→ Technical Assignment / Requirements Intake
→ draft product documentation
→ conditional UX / Experience Outline
→ Target Project / Feature Architecture Need Check
→ minimal hierarchical planning
→ one Task = one document
→ derived Queue / one next safe action
→ Human Activation
→ Preflight / Preview
→ Execution Authorization
→ bounded Execution
→ Candidate Freeze
→ Validation / Evidence
→ Human Decision
→ Closure / Recovery / Resume / Project Memory
```

Roadmap не выбирает:

- first user/job;
- first vertical slice;
- implementation repository;
- interface;
- language;
- framework;
- database;
- dependencies;
- provider.

Эти outcomes нельзя выводить из accepted baseline. Они остаются human decisions или `UNKNOWN`.

Один successful end-to-end dogfood демонстрирует first Core vertical slice, но не доказывает stable Core. Stable Core требует нескольких comparable manual cycles, включая:

- successful completion;
- `NEEDS_CHANGES` или validation failure;
- interruption / recovery / resume.

Точное количество циклов и admission threshold остаются human decisions.

## 2. Audit findings affecting roadmap

| Finding | Classification | Roadmap effect |
|---|---|---|
| `docs/` принят как knowledge baseline с `FACT_CLASS_SCOPED` authority; implementation и Git authorization отсутствуют | `HUMAN_ACCEPTED_FACT` | Roadmap остаётся `PROPOSAL` и не повышает maturity |
| R1 создавался на branch `dev`, commit `d783f7d8cd0d2af2fb88fafa23ea16f289ef8ea6` | `OBSERVED_AT_SNAPSHOT` | Это snapshot R1 creation, не current mutable fact для будущего execution |
| AOS — human-directed AI-assisted software development system; приоритет — снижение стоимости постановки, координации, проверки и продолжения, а не максимальная автономность | `HUMAN_ACCEPTED_FACT` | Все lifecycle transitions требуют явных checkpoints |
| Implementation repository имеет состояние `UNASSIGNED` | `HUMAN_ACCEPTED_FACT` | `S0` нельзя исполнять до отдельного human decision |
| Canonical contract taxonomy ограничена `C-001…C-014` | `HUMAN_ACCEPTED_FACT` | Phase-specific candidates не получают новые `C-*` IDs |
| Accepted feature catalog — inventory; item-level feature selection не выполнялся | `HUMAN_ACCEPTED_FACT` | Упоминание FTR означает traceability, а не selection |
| Core journey пересекает Product Runtime и минимальные Development Factory primitives | `SYNTHESIZED` | `Core` означает minimum viable end-to-end journey, а не переименование architecture layer |
| Manual cycle должен предшествовать automation; candidate frozen до validation; validation не исправляет subject | `HUMAN_ACCEPTED_FACT` | `EXECUTE`, `VALIDATE`, `REVIEW` и decision разделены |
| Skeleton, schemas, tests или documentation не доказывают Product Runtime capability | `SYNTHESIZED` | `S0` не создаёт product capability claim |
| Reference repositories для данного synthesis не потребовались | `NOT_RUN` | Targeted legacy research не выполнялся |

### Source classifications

- Accepted facts: `docs/00_Core.md`, `docs/01_Product.md`, `docs/02_Architecture.md`, `docs/03_Development.md`.
- Design candidates and inventory facts: релевантные dossiers `FTR-001…FTR-016`, `FTR-019` в `docs/06_Features.md`.
- Lesson proposals: релевантные `LES-*` в `docs/04_Lessons.md`; они влияют на risks и negative tests, но не становятся policy автоматически.
- Workspace rule: материалы в `AOS-3/` имеют статус `DRAFT` и не заменяют official baseline.

## 3. Core boundary

### 3.1 Included Core journey

Roadmap включает minimum viable journey от safe Product Bootstrap до closure и resume.

Core должен дать пользователю:

- один понятный пользовательский путь;
- несколько возможных `READY_FOR_QUEUE` tasks;
- не более одного `ACTIVE` task;
- не более одного recommended next safe action;
- отдельные решения перед mutation, acceptance и Git delivery.

В Core входят:

- preview-first installation, ownership boundary, authorized apply, First-Start и post-install verification;
- read-only Project Discovery для нового или существующего repository;
- adaptive Problem Interview, FPF summary и Requirements Intake;
- reviewed DRAFT product documentation;
- conditional UX / Experience Outline только при material UX/access gap;
- Target Project Architecture Need Check;
- minimal hierarchy и Task Documents;
- derived Queue и one next safe action;
- Human Activation;
- read-only Preflight / Preview;
- exact Execution Authorization bound to preview;
- bounded Execution и Stage Report;
- Candidate Freeze;
- separately scoped read-only Validation;
- Evidence, Human Review Package и explicit Human Decision;
- Closure / Recovery / Resume / Project Memory;
- Minimal Safety Floor на всём пути.

### 3.2 Core maturity

Maturity должна описываться раздельно:

```text
first slice demonstrated
→ manual cycle completed
→ comparable cycles completed
→ stabilization candidate
→ stable Core demonstrated
```

Наличие scaffold, contracts или commands не подтверждает end-to-end behavior.

### 3.3 Incremental proof gates

Dogfood проводится не только в конце:

```text
C1 → First-Start comprehension dogfood
C2 → intake/specification dogfood
C3 → hierarchy/Task Document/next-action dogfood
C5 → first complete end-to-end dogfood
C6 → repeated comparable cycles, recovery and stabilization
```

### 3.4 FTR-007 boundary

```yaml
minimal_core_subset:
  classification: HUMAN_CONFIRMED_DIRECTION
  canonical_feature_disposition_changed: false
  capabilities:
    - minimal hierarchy
    - Task Documents
    - derived queue
    - one next safe action
    - one active task

advanced_ftr_007:
  classification: PROPOSAL
  placement: DEFERRED_MODULE
  capabilities:
    - advanced backlog orchestration
    - persistent scheduling
    - batch activation
    - batch execution
    - forecasting
    - velocity management
```

Accepted inventory остаётся без изменений:

```yaml
feature_id: FTR-007
synthesis_recommendation: DEFER
human_disposition: UNDECIDED
```

Это не unresolved authority conflict. Это bounded `HUMAN_CONFIRMED_DIRECTION` при неизменённом canonical inventory disposition.

### 3.5 Queue semantics

```yaml
queue_semantics:
  ready_for_queue_tasks: 0..N
  active_tasks: 0..1
  recommended_next_safe_action: 0..1
```

```text
Task created ≠ READY_FOR_QUEUE
READY_FOR_QUEUE ≠ ACTIVE
ACTIVE ≠ AUTHORIZED_FOR_EXECUTION
```

Queue является derived/rebuildable view и не владеет task truth.

### 3.6 Core invariants

```text
Knowledge baseline ≠ implementation
Roadmap ≠ implementation plan
Scaffold ≠ Product Runtime
Task created ≠ READY_FOR_QUEUE
READY_FOR_QUEUE ≠ ACTIVE
ACTIVE ≠ AUTHORIZED_FOR_EXECUTION
Human Activation ≠ Execution Authorization
Preflight PASS ≠ authorization
preview changed → authorization STALE
subject changed → preview and authorization STALE
Execution ≠ Validation
Validation does not fix
PASS ≠ approval
Evidence ≠ approval
Human acceptance ≠ Git delivery
UNKNOWN ≠ OK
NOT_RUN ≠ PASS
all children completed ≠ parent accepted
candidate changed → previous validation STALE
optional module cannot weaken Minimal Safety Floor
```

## 4. Development Scaffold boundary

### 4.1 Development Scaffold

```yaml
scaffold_classification: ENABLING_STAGE
scaffold_is_product_core_capability: false
authority: PROPOSAL
```

`Development Scaffold` — greenfield foundation для разработки самого AOS после отдельного выбора target implementation repository и AOS implementation architecture decisions. Его bounded scope:

- reproducible local environment;
- минимальная source/package/test topology без назначения её формы в этом roadmap;
- implementation of human-selected language/toolchain/dependency policy;
- one local entrypoint;
- unit/contract/smoke test skeleton;
- doctor / self-test;
- Minimal Safety Floor;
- явная maturity, запрещающая Product Runtime capability claim.

Scaffold не доказывает install, First-Start, intake, execution, validation или recovery behavior. Его acceptance ограничена воспроизводимостью development foundation и executable safety skeleton.

### 4.2 Product Bootstrap

`Product Bootstrap` — capability AOS для пользовательского repository:

- read-only discovery;
- install preview;
- ownership boundaries;
- apply only after authorization;
- First-Start;
- post-install verification;
- disable/remove/recovery boundary.

```text
Development Scaffold enables building Product Bootstrap.
Development Scaffold is not Product Bootstrap.
```

### 4.3 Two architecture decision domains

Не смешивать:

```text
C0 — AOS Implementation Architecture Decision Package
C2 — Target Project / Feature Architecture Need Check
```

Первый относится к созданию самого AOS. Второй — к пользовательскому проекту, обрабатываемому AOS.

## 5. Roadmap overview

| Phase | Role | Smallest bounded outcome | Incremental proof | Transition |
|---|---|---|---|---|
| `C0` | Human decision package | First job/slice and AOS implementation decisions made reviewable | Decision-package comprehension | Human decision required |
| `S0` | Enabling stage | Reproducible development foundation with Minimal Safety Floor | Scaffold reproducibility only | Separate implementation authorization required |
| `C1` | Product Bootstrap | Safe install preview/apply, Tutor / First-Start, route into Discovery | First-Start comprehension dogfood | Separate phase acceptance |
| `C2` | Product definition | Idea/brief becomes reviewed DRAFT specification | Intake/specification dogfood | Human review/selection |
| `C3` | Minimal planning | Specification becomes minimal hierarchy and queue-eligible Task Documents | Task/queue/next-action dogfood | Human Activation |
| `C4` | Bounded mutation | Activation, preview, exact authorization, one EXECUTE stage, report and stop | Execution-path observation | Separate C5 scope |
| `C5` | Validation and decision | Frozen candidate, validation, Evidence, explicit human decision, closure | First complete end-to-end dogfood | Acceptance does not imply Git delivery |
| `C6` | Recovery and stabilization | Comparable cycles prove resume/recovery and yield stabilization decisions | Repeated success/failure/interruption cycles | New bounded task |

Dependency-oriented default path:

```text
C0 → S0 → C1 → C2 → C3 → C4 → C5 → C6
```

Это не fixed feature priority. C0 может определить a thin vertical slice, пересекающий несколько phases. Ни одна стрелка не означает auto-advance.

## 6. Detailed phases

### C0 — Human Decision Package and DRAFT Core Product Contract Candidate

**purpose:** Сделать first Core slice decision-ready, зафиксировать Core boundary и подготовить AOS Implementation Architecture Decision Package без выдумывания outcomes.

**user_outcome:** Человек видит, для кого и какую первую проблему предлагается решать, какой smallest vertical slice сравнивается, какие решения уже приняты и какие ещё нужно принять.

**prerequisites:**

- accepted knowledge baseline доступен;
- source identity и mutable repository facts перепроверены;
- roadmap рассматривается только как `PROPOSAL`;
- ни один FTR не считается selected из-за наличия в inventory.

**in_scope:**

- first user/job candidates;
- first core vertical slice candidates;
- Core boundary и non-goals;
- DRAFT Core Product Contract candidate;
- AOS Implementation Architecture Decision Package по target implementation repository, interface candidate, language/toolchain, dependency policy, persistence и packaging/distribution;
- exact unknowns, conflicts, acceptance and negative-test expectations.

**out_of_scope:**

- выбор outcomes агентом;
- создание implementation repository;
- scaffold или Product Runtime mutation;
- dependency installation;
- feature disposition changes;
- Git delivery.

**deliverable classes:**

- decision-ready human review package;
- `DRAFT` product contract candidate;
- AOS Implementation Architecture Decision Package;
- unknown/conflict register;
- smallest-slice comparison.

**relevant canonical contracts:** `C-002`, `C-003`, `C-004`.

**proposed phase-specific artifacts:**

- Core Product Contract — `PROPOSAL_NAME`, mapped to `C-002` + `C-003`;
- Core Boundary Record — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`;
- First Slice Decision Package — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`.

**relevant FTR-*:** `FTR-001`, `FTR-002`, `FTR-003`, `FTR-005`, `FTR-019`.

**acceptance criteria:**

- first user/job and slice are either explicitly selected by a human or remain `UNKNOWN`;
- candidate value, observable outcome, I/O, failures, recovery, acceptance and non-goals are reviewable;
- unresolved repository/toolchain/dependency decisions are visible and unfilled;
- alternatives and reversal conditions are visible;
- no implementation or feature acceptance claim is made.

**executable negative scenarios:**

- Given no human first-slice decision, when C0 closes, then the slice remains `UNKNOWN` and S0 execution is blocked.
- Given a legacy topology, when preparing the candidate, then repository presence does not select that topology.
- Given a single architecture option presented as inevitable, when reviewing the package, then the comparison fails.
- Given generated `ACCEPT`, when checking authority provenance, then the decision is rejected.

**exit gate:** Human reviews the exact C0 package and records decisions or explicit deferrals; unresolved material decisions remain blockers.

**blockers:** Missing product owner decision, unresolved first job/slice, conflicting scope, missing implementation architecture decision.

**unknowns:** First user/job, first vertical slice, interface, implementation repository, persistence, toolchain and dependencies.

**next authority required:** Separately bounded S0 Task Brief, followed by read-only repository Preflight / Preview and then exact Execution Authorization bound to the resulting subject and preview identities.

> Phase completion does not authorize the next mutation or lifecycle stage.

### S0 — Greenfield Development Scaffold

**purpose:** Создать reproducible development foundation для AOS в отдельно выбранном target implementation repository, не выдавая foundation за Product Runtime.

**user_outcome:** Implementer может воспроизводимо открыть development environment, запустить one local entrypoint, unit/contract/smoke skeleton и doctor / self-test, а reviewer видит Minimal Safety Floor и честную maturity.

**prerequisites:**

- C0 human decisions bound to exact revision;
- target implementation repository выбран человеком и instrumentally verified;
- language/toolchain/dependency decisions приняты отдельно;
- bounded S0 Task Brief exists and is bound to the selected scaffold scope;
- repository Preflight / Preview has completed for the current repository/worktree/branch/HEAD and expected mutation;
- exact Execution Authorization was issued after Preflight and is bound to the current task, subject identity, preview identity, allowed paths and allowed operations.

**in_scope:**

- reproducible local environment;
- minimal source/package/test topology;
- implementation of selected dependency policy;
- one local entrypoint;
- unit/contract/smoke skeleton;
- doctor / self-test;
- baseline result vocabulary;
- Minimal Safety Floor checks;
- rationale, ownership, invariants and handoff.

**out_of_scope:**

- Product Bootstrap behavior;
- user-repository installation;
- Product Runtime capability claims;
- full Governance or Control Plane;
- CI/CD and remote gates;
- automatic Git actions;
- optional modules.

**deliverable classes:**

- development foundation;
- executable test skeleton;
- doctor / self-test evidence;
- selected environment/profile implementation record;
- S0 Stage Report.

**relevant canonical contracts:** `C-005`, `C-006`, `C-007`, `C-008`, `C-009`, `C-010`, `C-012`.

**proposed phase-specific artifacts:**

- Development Scaffold Contract — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`;
- Minimal Safety Floor fixture set — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`;

**relevant FTR-*:** `FTR-006`, `FTR-009`, `FTR-011`, `FTR-013`, `FTR-014`, `FTR-019`.

**acceptance criteria:**

- clean environment can reproduce the documented local checks;
- one local entrypoint has stable failure/result semantics;
- unit/contract/smoke skeleton and doctor / self-test run without claiming Product Runtime;
- authority defaults false and `NOT_RUN` cannot aggregate to `PASS`;
- read-only/help checks produce zero source-tree writes;
- actual diff stays within the S0 allowlist and is recoverable.

**executable negative scenarios:**

- Given only scaffold files, when product capability is queried, then result is `NOT_RUN`, not implemented.
- Given missing execution authorization, when scaffold mutation is requested, then mutation is blocked.
- Given an invalid contract or failing doctor check, when entrypoint exits, then it cannot report success.
- Given an optional test helper failure, when Minimal Safety Floor is evaluated, then the helper cannot weaken required safety checks.

**exit gate:** Exact scaffold candidate is frozen, validated against S0 acceptance, reviewed, and receives a human decision limited to scaffold maturity.

**blockers:** Implementation repository `UNASSIGNED`, missing toolchain/dependency decisions, missing S0 authorization, dirty/ambiguous subject, unreproducible environment.

**unknowns:** Exact topology and environment implementation details until C0 decisions.

**next authority required:** Separate C1 Product Contract acceptance and a bounded C1 implementation authorization.

> Phase completion does not authorize the next mutation or lifecycle stage.

### C1 — Product Bootstrap / Install / Tutor / First-Start

**purpose:** Дать пользователю безопасный вход в AOS через preview-first installation, ownership-aware apply, verification и понятный First-Start.

**user_outcome:** Пользователь понимает, что будет изменено в его repository, отдельно разрешает apply, получает verified installation state, Tutor и one next route в Project Discovery.

**prerequisites:**

- S0 foundation имеет ограниченный human decision, не Product Runtime claim;
- C1 feature-specific Product Contract принят;
- package and target identities проверены;
- ownership classes, conflict behavior, recovery boundary and disable/remove semantics определены;
- exact preview доступен до apply authorization.

**in_scope:**

- read-only target discovery;
- exact install preview;
- managed/user/project ownership boundaries;
- preview-bound authorization;
- atomic or journaled apply;
- post-install verification;
- Tutor / First-Start;
- first safe action;
- disable/remove/recovery boundary without implicit destructive action.

**out_of_scope:**

- silent overwrite of user/project state;
- automatic uninstall or cleanup;
- problem/specification completion;
- remote delivery;
- advanced UI or SaaS onboarding.

**deliverable classes:**

- Install / Update Manifest;
- Preflight / Preview;
- preview-bound authorization;
- Execution Record for apply;
- post-install Validation / Evidence;
- First-Start guidance;
- recovery/handoff record.

**relevant canonical contracts:** `C-013`, `C-006`, `C-007`, `C-008`, `C-009`, `C-010`, `C-012`.

**proposed phase-specific artifacts:**

- First-Start Guide Contract — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`;
- disable/remove boundary — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`.

**relevant FTR-*:** `FTR-004`, `FTR-008`, `FTR-009`, `FTR-011`, `FTR-014`, `FTR-019`.

**acceptance criteria:**

- dry-run is side-effect free and identifies ownership/conflicts;
- apply matches the authorized preview and preserves user/project state;
- interruption and repeat have defined recovery/idempotency behavior;
- post-install checks show exact results and `NOT_RUN`;
- a nonprogrammer can follow First-Start and reach one next safe action;
- disable/remove does nothing destructive without separate authority.

**executable negative scenarios:**

- Given a user-owned collision, when preview runs, then apply is not presented as safe overwrite.
- Given a changed target after preview, when apply starts, then preview and authorization are `STALE` and apply stops.
- Given interrupted update, when resume is requested, then actual state is reconciled before any retry.
- Given uninstall without exact human authorization, when removal is requested, then it stops without deletion.

**incremental proof:** First-Start comprehension dogfood with a nonprogrammer or representative user.

**exit gate:** Exact C1 candidate is manually demonstrated and human-reviewed.

**blockers:** Unknown ownership, stale preview, incomplete recovery, missing human apply decision, first-start path not understandable.

**unknowns:** Package distribution form, target compatibility scope, exact ownership taxonomy, First-Start interface.

**next authority required:** Separate C2 documentation-stage authorization or human instruction.

> Phase completion does not authorize the next mutation or lifecycle stage.

### C2 — Idea or Existing Brief → Reviewed Draft Specification

**purpose:** Превратить idea или existing brief в reviewed DRAFT specification, сохранив original intent, uncertainty и conditional design depth.

**user_outcome:** Пользователь узнаёт свою проблему и desired outcome, видит FPF summary, requirements, draft product documentation, conditional UX outline и target-project architecture need.

**prerequisites:**

- C1 provides a safe First-Start route or equivalent manually verified entry for dogfood;
- original request and source provenance are retained;
- Project Discovery is read-only and snapshot-bound;
- interview depth follows material risk/uncertainty;
- no architecture or implementation choice is pre-authorized.

**in_scope:**

- Project Discovery;
- Problem Interview;
- FPF summary;
- Technical Assignment / Requirements Intake;
- DRAFT Product Spec and feature-specific Product Contract;
- conditional UX / Experience Outline when actors/access/flow are materially underspecified;
- Target Project / Feature Architecture Need Check;
- DRAFT ADR only when needed;
- assumptions, conflicts, unknowns, acceptance and negative scenarios.

**out_of_scope:**

- mutation of the user project;
- automatic product/architecture decision;
- full design system or Storybook;
- task activation;
- implementation planning beyond one candidate slice.

**deliverable classes:**

- Problem Intake artifact;
- FPF summary;
- Technical Assignment / Requirements Draft;
- DRAFT Product Spec / Feature Contract;
- conditional UX / Experience Outline;
- Target Project Architecture Need Check and optional DRAFT ADR;
- review package.

**relevant canonical contracts:** `C-001`, `C-002`, `C-003`, conditionally `C-004`, `C-011`, `C-012`.

**proposed phase-specific artifacts:**

- FPF summary format — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`;
- Technical Assignment / Requirements Draft — `MAPPED_FORMAT_PROPOSAL`, mapped predominantly to `C-003`;
- UX / Experience Outline — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`.

**relevant FTR-*:** `FTR-001`, `FTR-002`, `FTR-003`, `FTR-005`, `FTR-008`, `FTR-016`, `FTR-019`.

**acceptance criteria:**

- original request, problem, user, desired outcome, constraints, non-goals, assumptions and unknowns are distinguishable;
- discovery records exact snapshot and does not mutate source;
- draft specification has observable behavior, failures/recovery, acceptance and negative cases;
- conditional UX is present only when its trigger is met;
- Target Project Architecture Need Check is justified; DRAFT ADR does not imply selection;
- human corrections bind to the exact draft revision.

**executable negative scenarios:**

- Given an empty request, when intake runs, then state remains clarifying and no specification is claimed complete.
- Given repository content that instructs the agent, when discovery runs, then it is treated as untrusted data.
- Given insufficient UX/access detail, when the UX trigger is evaluated, then the outline cannot be silently skipped.
- Given no material architecture question, when Target Project Architecture Need Check runs, then ADR ceremony is avoided.

**incremental proof:** Run intake/specification flow on one real idea or brief and verify user recognition, unknown visibility and correction loop.

**exit gate:** Human reviews exact draft, resolves material corrections or records unknowns, and selects whether one minimal hierarchy may be prepared.

**blockers:** Unrecognized problem/outcome, stale discovery, material unknown without resolution path, untrusted source override, missing human correction.

**unknowns:** Product Spec↔Feature Passport relation, UX trigger threshold, FPF format, requirements format, architecture decision granularity.

**next authority required:** Explicit human approval to prepare a bounded C3 planning artifact for the exact specification revision.

> Phase completion does not authorize the next mutation or lifecycle stage.

### C3 — Specification → Minimal Hierarchy → Queue-Eligible Task Documents

**purpose:** Декомпозировать exact specification только настолько, насколько нужно для bounded Task Documents и one explainable next safe action.

**user_outcome:** Пользователь видит traceable hierarchy, ready candidates, active task boundary и blockers.

**prerequisites:**

- exact C2 specification revision reviewed;
- parent outcome and acceptance defined;
- one candidate vertical slice selected by a human;
- decomposition is justified by near-term execution, not future forecasting;
- Task Document contract is agreed as a proposal for this slice.

**in_scope:**

```text
Plan
→ Stage
→ Work Package
→ Task
```

Each node has:

- stable ID;
- `parent_id`;
- source requirement refs;
- own acceptance;
- revision;
- state;
- lazy decomposition;
- bottom-up verification;
- revision propagation.

Also in scope:

- Task Documents;
- derived Queue;
- queue eligibility;
- one next safe action;
- maximum one `ACTIVE` task.

**out_of_scope:**

- advanced backlog orchestration;
- persistent scheduling;
- batch activation or execution;
- forecasting and velocity management;
- automatic task activation;
- claiming parent acceptance from child completion.

**deliverable classes:**

- minimal hierarchy;
- one or more queue-eligible Task Documents;
- eligibility result;
- derived Queue view;
- one next safe action and blockers.

**relevant canonical contracts:** `C-003`, `C-005`, `C-012`; later activation uses `C-006`.

**proposed phase-specific artifacts:**

- Hierarchy Node Contract — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`;
- Queue Eligibility Contract — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`;
- Resolver Contract — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`;
- Task Document — `MAPPED_WITH_PROPOSAL`, mapped to `C-005` plus presentation/journal convention.

**relevant FTR-*:** `FTR-003`, minimal subset of `FTR-007`, `FTR-006`, `FTR-008`, `FTR-016`, `FTR-019`.

**acceptance criteria:**

- every child traces to source requirement and parent acceptance;
- `READY_FOR_QUEUE` count may be `0..N`;
- `ACTIVE` count is `0..1`;
- recommended next safe action is `0..1`;
- eligibility is derived from exact contract completeness/dependencies and does not create authority;
- Queue is rebuildable and not Source of Truth;
- next action is singular, explainable and safe;
- parent completion requires own verification/human decision;
- parent revision marks affected children/validation as `STALE`;
- advanced FTR-007 capabilities are absent.

**executable negative scenarios:**

- Given an orphan child, when hierarchy validation runs, then the child is rejected.
- Given a dependency cycle, when eligibility is computed, then task is not `READY_FOR_QUEUE`.
- Given all children technically complete, when parent state is evaluated, then parent is not accepted without human decision.
- Given a queue-eligible task, when no `C-006` record exists, then execution remains blocked.
- Given a parent revision, when affected children are evaluated, then their status and prior validation are recalculated or marked `STALE`.

**incremental proof:** Use one reviewed specification to create hierarchy, Task Documents, derived Queue and one next action; verify user understands why the next action is selected.

**exit gate:** Exact Task Document contract revision and digest are frozen for activation review; human selects at most one active task.

**blockers:** Missing parent acceptance, orphan/circular dependency, incomplete Task Brief fields, multiple active tasks, material unknown.

**unknowns:** Durable hierarchy representation, queue derivation mechanism, resolver tie-breaking, exact eligibility vocabulary.

**next authority required:** C4 Human Activation, followed by Preflight and exact Execution Authorization.

> Phase completion does not authorize the next mutation or lifecycle stage.

### C4 — Human Activation → Preflight → Execution Authorization → Bounded Execution

**purpose:** Выполнить one bounded mutation stage against a fresh preview and stop with Stage Report.

**user_outcome:** Пользователь выбирает task, видит exact current subject and preview, authorizes the precise mutation, получает bounded change and report.

**prerequisites:**

- one Task Document activated by human;
- immutable contract identity;
- machine-checkable allowed/forbidden paths and operations;
- stop conditions, checks and recovery boundary;
- repository subject available for preflight.

**in_scope:**

- Human Activation;
- read-only preflight and preview;
- exact preview-bound authorization;
- one bounded EXECUTE stage;
- mutation journal or atomic boundary;
- actual diff/scope reconciliation;
- targeted execution-time checks;
- Stage Report and stop.

**out_of_scope:**

- implicit activation;
- authorization before preview;
- hidden scope expansion;
- validation of the frozen candidate;
- self-correction after a validation finding;
- Commit, Push, Merge or Release;
- automatic retry after identity/permission/scope change.

**deliverable classes:**

- Execution Authorization;
- Preflight / Preview;
- Execution Record;
- Stage Report;
- recovery facts when execution does not complete cleanly.

**relevant canonical contracts:** `C-005`, `C-006`, `C-007`, `C-008`, `C-012`.

**proposed phase-specific artifacts:**

- Task Document presentation/journal convention — `PROPOSAL`, mapped with `C-005`;
- Stage Report presentation — `PROPOSAL`, mapped to `C-008` + `C-012`.

**relevant FTR-*:** `FTR-006`, `FTR-009`, `FTR-010`, `FTR-014`, `FTR-019`.

#### C4-A Human Activation

Human selects exact Task Document as `ACTIVE`.

```text
Human Activation ≠ Execution Authorization
```

No mutation is permitted yet.

#### C4-B read-only Preflight / Preview

- Reverify repository/worktree/branch/HEAD/baseline/status, paths, environment and permissions.
- Render exact planned actions and side effects.
- Produce zero source-tree writes.
- `PASS` confirms only the observed preflight contract; it is not authorization.

#### C4-C Exact Execution Authorization

Human authorizes exact:

```text
task_id
+ contract_revision
+ contract_digest
+ subject_identity
+ preview_identity
+ allowed_paths
+ allowed_operations
```

```text
Preflight PASS ≠ authorization
preview changed → authorization STALE
subject changed → preview and authorization STALE
```

Missing, copied, consumed, expired or stale authorization blocks execution.

#### C4-D EXECUTE

- Consume exact authorization once.
- Execute smallest authorized mutation only.
- Journal or atomically contain writes.
- Stop on unexpected path, changed identity, permission conflict, partial write or material unknown.
- Do not perform final validation or auto-fix.

#### C4-E Stage Report and stop

- Record starting/ending identity, actual mutations, changed paths, side effects, checks, limitations and stop reason.
- Preserve unrelated user state.
- Set `VALIDATE: NOT_RUN` and Git operations to `NOT_RUN`.
- Stop without auto-advancing to C5.

**acceptance criteria:**

- C4-A…C4-E are distinct and evidenced in order;
- preview precedes authorization;
- authorization matches current preview and subject;
- preflight is read-only;
- only allowed paths/operations change;
- execution produces an exact Stage Report and stops;
- no claim of validation, acceptance or Git delivery appears.

**executable negative scenarios:**

- Given a changed immutable task contract, when authorization is checked, then previous authorization and preview are `STALE`.
- Given Preflight `PASS` but no valid human authorization, when EXECUTE is requested, then execution remains blocked.
- Given a changed subject after authorization, when EXECUTE is requested, then execution remains blocked.
- Given an unexpected path in actual diff, when reconciliation runs, then execution returns non-`PASS` and stops.
- Given a partial write, when failure is detected, then no automatic retry occurs and recovery facts are preserved.

**exit gate:** C4-E Stage Report identifies an exact candidate or recoverable partial state; C5 is separately scoped.

**blockers:** Stale/missing authorization, dirty subject contamination, changed HEAD, preview drift, unexpected path, partial mutation, missing recovery facts.

**unknowns:** Exact authorization expiry/consumption policy, isolation mechanism, atomic/journal technique, risk thresholds.

**next authority required:** Separately scoped C5 validation activity; explicit human authorization only if validation needs protected/external operations.

> Phase completion does not authorize the next mutation or lifecycle stage.

### C5 — Validation → Evidence → Human Decision → Closure

**purpose:** Проверить immutable candidate without fixes, present Evidence and obtain exact human decision.

**user_outcome:** Пользователь видит exact subject, checks run/not run, remaining risk and decision options.

**prerequisites:**

- exact C4 Stage Report;
- candidate can be finalized and identified without self-reference;
- validation matrix distinguishes required/optional checks;
- validator has read-only boundary;
- protected/external validation operations separately authorized when applicable.

**in_scope:**

- candidate freeze;
- exact identity and scope reconciliation;
- read-only validation;
- Evidence Records;
- Human Review Package;
- explicit Human Decision;
- Closure / Handoff;
- stale detection.

**out_of_scope:**

- fixing validation findings;
- changing candidate after freeze;
- generated human acceptance;
- automatic Commit/Push/Merge/Release;
- treating `NOT_RUN` as `PASS`.

**deliverable classes:**

- frozen candidate identity;
- ValidationEnvelope;
- Evidence Records;
- Human Review / Decision;
- Closure Record candidate;
- Project Memory / Handoff.

**relevant canonical contracts:** `C-009`, `C-010`, `C-011`, `C-012`; subject traceability also uses `C-005`, `C-007`, `C-008`.

**proposed phase-specific artifacts:**

- Closure Record — `PROPOSAL`, mapped to `C-011` + `C-012` until separately accepted;
- candidate freeze marker/model — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`.

**relevant FTR-*:** `FTR-011`, `FTR-012`, `FTR-013`, `FTR-014`, `FTR-016`, `FTR-019`.

#### C5-A Candidate Freeze

- Finalize candidate inputs and compute exact subject identity.
- Reconcile Task Document, preview, execution record and actual diff.
- Any candidate mutation after freeze makes previous validation `STALE`.

#### C5-B VALIDATE — read-only, no fix

- Verify exact subject and environment/import provenance.
- Run required/optional checks and executable negative scenarios.
- Preserve `FAIL`, `BLOCKED`, `UNKNOWN` and `NOT_RUN`.
- Do not modify candidate, even for an obvious fix.

Ordinary local read-only validation does not automatically require human authorization. Explicit human authorization is required only when validation itself uses:

- protected data;
- secrets;
- network;
- paid/external resources;
- destructive or separately controlled operation.

#### C5-C Human Review Package

- Map every acceptance criterion to Evidence or explicit `NOT_RUN`.
- Show user-visible impact, findings, limitations and remaining risk.
- Offer decision options without selecting one.

#### C5-D Human Decision

- Human records `ACCEPT | NEEDS_CHANGES | REJECT | DEFER` for exact candidate identity.
- Generated or stale decisions are invalid.
- Technical `PASS` does not imply `ACCEPT`.

#### C5-E Closure / Handoff

- Record exact identity, decision, blockers, validation state, recovery state and one next action.
- Closure does not create Git authorization.
- A correction requires a new Task Document revision and lifecycle.

**acceptance criteria:**

- C5-A…C5-E remain distinct and no validator writes to the candidate;
- every required check has a result; required `NOT_RUN` prevents aggregate `PASS`;
- Evidence is subject-bound and limitations are visible;
- human decision has actor and exact binding;
- closure preserves one next action and separate Git permissions;
- candidate change invalidates prior validation and decision readiness.

**executable negative scenarios:**

- Given a candidate byte change after freeze, when validation identity is compared, then previous validation is `STALE`.
- Given a required `NOT_RUN`, when aggregate result is computed, then aggregate cannot be `PASS`.
- Given a validation failure with an obvious fix, when validator runs, then candidate remains unchanged and a correction task is proposed.
- Given Evidence without human decision, when closure is evaluated, then acceptance remains unset.
- Given human `ACCEPT` without Git authorization, when Commit is requested, then Commit remains blocked.

**incremental proof:** First complete C1→C5 end-to-end dogfood cycle.

**exit gate:** Exact candidate has an honest validation package and explicit human decision or an explicit unresolved decision state; closure/handoff is complete for that state.

**blockers:** Unfreezable subject, validation writes, self-reference, missing required result, stale candidate, missing human actor/binding.

**unknowns:** Candidate identity for uncommitted state, independent-validation threshold, human decision authenticity mechanism, Closure Record adoption.

**next authority required:** New correction Task Document, deferment, or separate Git action authorization.

> Phase completion does not authorize the next mutation or lifecycle stage.

### C6 — Recovery / Resume / Repeated Dogfood / Core Stabilization

**purpose:** Проверить continuity and recovery across comparable manual cycles before broad automation.

**user_outcome:** Пользователь может понять actual state, recovery options, one next safe action and resume in a new session without unsafe assumptions or lost authority.

**prerequisites:**

- at least one complete cycle or recoverable failure;
- exact handoff and repository-derived state;
- mutable facts refreshed on resume;
- recovery action classified by scope, reversibility and human authority;
- incidents remain findings/lesson proposals, not automatic rules.

**in_scope:**

- interruption and partial-write recovery;
- denied-action visibility;
- bounded resume after re-preflight;
- comparable manual cycles:
  - success;
  - `NEEDS_CHANGES` or validation failure;
  - interruption/recovery;
- Project Memory / Handoff;
- status / one next action;
- Core regression findings and bounded stabilization proposals;
- measured readiness discussion for later automation.

**out_of_scope:**

- autonomous retry/remediation/self-heal;
- broad automation after one cycle;
- automatic promotion of lessons;
- optional module implementation;
- Git delivery without separate action-specific authority.

**deliverable classes:**

- recovery package;
- refreshed Project Memory / Handoff;
- manual dogfood Evidence;
- incident and lesson proposals;
- bounded stabilization candidate list;
- one next action.

**relevant canonical contracts:** `C-007`, `C-008`, `C-009`, `C-010`, `C-011`, `C-012`; destructive recovery or later delivery needs separate applicable authority.

**proposed phase-specific artifacts:**

- Recovery Option Record — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`;
- Dogfood Observation Record — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`;
- Core Stabilization Candidate List — `PROPOSAL`, `canonical_contract_id: NONE`, `human_decision_required: true`.

**relevant FTR-*:** `FTR-008`, `FTR-011`, `FTR-012`, `FTR-014`, `FTR-016`, `FTR-019`; lessons remain proposals.

**acceptance criteria:**

- new session reconstructs exact state, authority and one next action from source-owned records;
- stale handoff or changed repository identity blocks affected mutation only;
- partial writes are detectable and recovery options do not hide data loss;
- comparable cycles cover success, failure and interruption;
- stabilization candidates are traced to observed failure/overhead;
- stable Core claim requires repeated comparable behavior, not one case;
- no automation or optional module is admitted without a separate decision.

**executable negative scenarios:**

- Given a stale handoff, when resume is requested, then mutable repository facts are refreshed before any action.
- Given a permission violation, when retry is requested, then retry cannot expand scope or inherit authority.
- Given an incident, when lesson is recorded, then it remains a proposal until explicit acceptance.
- Given one successful dogfood run, when automation readiness is evaluated, then broad automation is not declared proven.
- Given failed recovery, when state is reported, then an exact blocker is recorded and no self-heal claim is made.

**exit gate:** Human reviews repeated-cycle Evidence and selects bounded stabilization work or deferment.

**blockers:** Missing actual-state evidence, unreconciled partial writes, stale identity, unclear recovery authority, no representative manual cycle.

**unknowns:** Project Memory persistence, resume UX, recovery boundary, stabilization metrics and cycle threshold.

**next authority required:** Separately scoped stabilization Task Brief or explicit deferment.

> Phase completion does not authorize the next mutation or lifecycle stage.

## 7. Task Document model

Следующая модель фиксируется только как `PROPOSAL`:

```text
Task Document
=
immutable contract section
+ human-readable body
+ append-only execution journal
```

Immutable contract section владеет goal, subject, scope, allowed/forbidden operations, acceptance, negative scenarios, stop conditions and lifecycle binding. Human-readable body объясняет intent и context, не расширяя contract. Append-only execution journal хранит события и results, но не меняет authorization subject.

Authorization привязывается к:

```text
task_id
+ contract_revision
+ contract_digest
+ subject_identity
+ preview_identity
```

Authorization **не** привязывается к изменяемому journal digest.

Если immutable contract section меняется:

```text
previous preview → STALE
previous authorization → STALE
```

Task creation не создаёт `READY_FOR_QUEUE`; eligibility не создаёт `AUTHORIZED_FOR_EXECUTION`.

## 8. Canonical contract mapping and proposed phase-specific artifacts

Ниже `classification` описывает mapping, а не расширяет canonical taxonomy.

| Candidate artifact | Canonical mapping | Classification | Authority |
|---|---|---|---|
| Core Product Contract | `C-002` + `C-003` | `PROPOSAL_NAME` | `PROPOSAL` |
| Development Scaffold Contract | no direct canonical class | `PROPOSAL` | `canonical_contract_id: NONE` |
| Install / Update Manifest | `C-013` | `CANONICAL_CLASS` | no execution authority |
| Problem Intake artifact | `C-001` + `C-003` | `MAPPED` | exact artifact requires review |
| Technical Assignment / Requirements Draft | primarily `C-003` | `MAPPED_FORMAT_PROPOSAL` | format remains proposal |
| Task Document | `C-005` + presentation/journal convention | `MAPPED_WITH_PROPOSAL` | authorization separate |
| Hierarchy Node Contract | no direct canonical class | `PROPOSAL` | `canonical_contract_id: NONE` |
| Queue Eligibility Contract | no direct canonical class | `PROPOSAL` | `canonical_contract_id: NONE` |
| Resolver Contract | no direct canonical class | `PROPOSAL` | `canonical_contract_id: NONE` |
| Execution Authorization | `C-006` | `CANONICAL_CLASS` | human-issued exact record |
| Preflight / Preview | `C-007` | `CANONICAL_CLASS` | `PASS` is not authorization |
| Execution Record | `C-008` | `CANONICAL_CLASS` | does not validate |
| Validation / Evidence | `C-009` + `C-010` | `CANONICAL_CLASSES` | does not approve |
| Human Decision | `C-011` | `CANONICAL_CLASS` | exact human binding |
| Closure Record | `C-011` + `C-012` | `PROPOSAL` | `canonical_contract_id: NONE` |
| Project Memory / Handoff | `C-012` | `CANONICAL_CLASS` | derived memory has no independent authority |

No new `C-*` IDs are created.

## 9. Core traceability matrix

| Phase | Capability | FTR | Contract | Acceptance signal | Executable negative tests |
|---|---|---|---|---|---|
| `C0` | Product and AOS implementation decision package | `FTR-001`, `FTR-003`, `FTR-005` | `C-002…C-004` | Human decisions or explicit unknowns | Generated selection rejected |
| `S0` | Development foundation | `FTR-006`, `FTR-009`, `FTR-011`, `FTR-019` | `C-005…C-010`, `C-012` | Reproducible scaffold, no runtime claim | Missing auth blocks write |
| `C1` | Product Bootstrap / First-Start | `FTR-004`, `FTR-008`, `FTR-014` | `C-006…C-010`, `C-012`, `C-013` | Preview-bound apply and comprehension dogfood | Target drift stales auth |
| `C2` | Intake/specification | `FTR-001…FTR-005`, `FTR-016` | `C-001…C-004`, `C-011`, `C-012` | Reviewed exact draft | Empty input remains clarifying |
| `C3` | Hierarchy/Task/Queue | minimal `FTR-007`, `FTR-006`, `FTR-008` | `C-003`, `C-005`, `C-012` | `0..N` ready, `0..1` active, one next action | Eligible does not authorize |
| `C4` | Preview-bound execution | `FTR-006`, `FTR-009`, `FTR-010`, `FTR-019` | `C-005…C-008`, `C-012` | C4-A…E distinct | Preview/subject drift blocks |
| `C5` | Freeze/validate/review/decision | `FTR-011…FTR-014`, `FTR-016` | `C-009…C-012` | No-fix validation and exact human decision | Evidence cannot approve |
| `C6` | Recovery/repeated cycles/stabilization | `FTR-008`, `FTR-011`, `FTR-014`, `FTR-016`, `FTR-019` | `C-007…C-012` | Comparable cycles and safe resume | One cycle not stable Core |

Диапазоны в matrix являются compact notation только для уже canonical IDs внутри `C-001…C-014`; они не создают новых contracts.

## 10. Out of Core / Deferred Modules

Следующие capabilities не входят как mandatory implementation в Core:

- full Control Plane;
- full Governance beyond Minimal Safety Floor;
- Cucumber as architecture foundation;
- CI/CD and remote merge gates;
- Commit/Push/Merge/Release automation;
- RAG/vector database;
- MCP feedback server;
- observability dashboards;
- multi-agent orchestration;
- model routing;
- Figma/Storybook;
- SaaS/workbench;
- plugin marketplace;
- domain modules;
- cryptographic signing;
- autonomous retry;
- autonomous remediation;
- self-heal;
- batch planning and execution.

Это неоднородный список. Часть относится к later Development Factory, часть — к optional architecture/extensions, а часть — к advanced portions feature families с разными synthesis recommendations. Roadmap не утверждает, что всё перечисленное принадлежит `L6` или имеет одинаковый `DEFER` status.

Deferred module может быть рассмотрен только после:

1. manual Core proof;
2. observed bounded problem;
3. measurable benefit;
4. explicit contract and failure isolation;
5. human decision;
6. подтверждения, что module не ослабляет Minimal Safety Floor.

## 11. Conflicts, risks and unknowns

### Resolved boundary tensions

| Subject | Classification | Treatment |
|---|---|---|
| Minimal subset of `FTR-007` with unchanged inventory disposition | `HUMAN_CONFIRMED_DIRECTION_WITH_UNCHANGED_INVENTORY` | Bounded subset in Core; advanced portion deferred |
| Core journey crosses Product Runtime and Factory primitives | `SYNTHESIZED` | Core means minimum end-to-end journey |
| Development Scaffold нужен до Product Bootstrap, но direct canonical contract class отсутствует | `NOT_FOUND` | Scaffold Contract остаётся `PROPOSAL` с `canonical_contract_id: NONE` |
| Closure нужен journey, но отдельного canonical Closure Contract нет | `NOT_FOUND` | Candidate mapped to `C-011` + `C-012` и остаётся `PROPOSAL` |
| Composite Task Document не задан canonical contract как единый immutable/body/journal artifact | `NOT_FOUND` | Model остаётся `MAPPED_WITH_PROPOSAL` вокруг `C-005` |

### Risks

- Scaffold может быть ошибочно назван Product Runtime; mitigation — explicit maturity and negative capability test.
- Roadmap может быть ошибочно прочитан как feature selection; mitigation — сохранять `human_disposition: UNDECIDED` до item-level decision.
- Preview и authorization могут drift independently; mitigation — bind authorization to exact `preview_identity` and subject.
- C4/C5 могут быть сжаты в один agent loop; mitigation — distinct artifacts, identities, authority and stop rules.
- Task journal может сделать authorization unstable; mitigation — bind only immutable contract identity.
- Queue может стать competing Source of Truth; mitigation — derived/rebuildable queue.
- First-Start может быть технически корректным, но непонятным nonprogrammer; mitigation — manual dogfood.
- Recovery может превратиться в self-heal; mitigation — no auto-retry after scope/identity/permission change.
- Optional module может ослабить safety; mitigation — Minimal Safety Floor remains mandatory and independent.
- Один successful cycle может быть ошибочно назван stable Core; mitigation — comparable success/failure/interruption cycles.

### Unknowns

- first user/job and first vertical slice;
- implementation repository;
- interface and Product Bootstrap distribution;
- language/toolchain/dependencies;
- Product Spec↔Feature Passport relation;
- FPF and Technical Assignment formats;
- Project Memory persistence and authenticity;
- Risk Profile vocabulary and thresholds;
- human decision authenticity mechanism;
- install ownership taxonomy and compatibility scope;
- candidate identity for uncommitted state;
- independent validation threshold;
- recovery boundary;
- stabilization metrics and cycle threshold.

Все material unknowns блокируют только affected mutation/claim; они не превращаются в `OK` и не блокируют unrelated read-only analysis.

## 12. Human decisions required

1. Принять, изменить или отклонить boundary этого exact roadmap revision.
2. Выбрать first user/job и first Core vertical slice.
3. Решить item-level dispositions только для реально выбранных feature contracts.
4. Выбрать target implementation repository.
5. Выбрать AOS implementation architecture, interface, persistence, language/toolchain/dependencies после comparison.
6. Принять или отклонить non-canonical proposals: Development Scaffold Contract, Task Document convention, hierarchy/queue/resolver contracts and Closure Record.
7. Выдать отдельный bounded Task Brief and Execution Authorization для каждого mutation stage.
8. Принять exact candidate после Evidence; `PASS` не заменяет этот decision.
9. Отдельно разрешать Commit, Push, Merge и Release для exact subject, если delivery требуется.

## 13. One next bounded action

Провести read-only human review exact revision `R2` и вернуть:

```text
ACCEPT
NEEDS_CHANGES
REJECT
```

Если `ACCEPT`, следующий action — отдельный C0 decision package.

До такого решения:

- не создавать implementation repository;
- не выполнять `S0`;
- не менять feature dispositions;
- не выполнять Commit или Push.
