# 06 — AOS Features


> **Artifact status:** `DRAFT`  
> **Authority:** `NONE`  
> **Canonical status:** `NOT_ASSIGNED`  
> **Human acceptance:** `NOT_REQUESTED`  
> **Implementation authorization:** `NONE`  
> **Source basis:** доступная история чатов проекта, current Project Instructions и загруженные reference notes; current repository/runtime verification — `NOT_RUN`.


## 1. Назначение и audit correction

Этот документ — единый detailed Feature Idea Bank. Он заменяет прежние 78 поверхностных карточек и 10 domain files. Все 78 исходных `IDEA-*` сохранены в crosswalk, но объединены в **30 coherent feature families**, потому что многие micro-ideas описывали одну end-to-end capability с разных сторон.

```text
06_Features.md = detailed idea/source bank
01_Product.md = product intent, users, journeys and admission rules
```

Наличие dossier здесь не означает `REQUIRED`, roadmap priority, accepted architecture или implementation authorization. Каждая feature остаётся `DRAFT`, `authority: NONE`, пока человек отдельно не примет product disposition.

## 2. Почему предыдущие descriptions были недостаточны

Previous cards обычно содержали только `Problem`, `Idea`, `Minimal safe version`, `Key risks`, `Targeted research` и sources. Для human/agent reconstruction этого недостаточно. В этой revision каждая family обязательно содержит:

- user/problem/outcome;
- trigger/preconditions;
- inputs/outputs;
- main flow;
- states/transitions;
- failure and recovery behavior;
- dependencies/shared contracts;
- safety/human authority boundaries;
- acceptance criteria;
- negative scenarios;
- minimal implementation model;
- targeted research;
- non-goals.

## 3. Disposition vocabulary

| Disposition | Meaning |
|---|---|
| `CANDIDATE` | Worth product-fit review; not required |
| `CANDIDATE_SUPPORT` | Supporting knowledge/operations capability worth review; not core by default |
| `CANDIDATE_AFTER_MANUAL_NEED` | Admit only after repeated manual evidence |
| `CANDIDATE_AFTER_BASELINE` | Admit after an executable baseline and stable check subject exist |
| `CANDIDATE_CORE_SAFETY` | Candidate Minimal Safety Floor capability; exact mechanism unaccepted |
| `HUMAN_DECISION_REQUIRED` | Material product/path choice unresolved |
| `DEFERRED` | Preserve idea; do not include early foundation |
| `DEFERRED_RESEARCH` | Preserve for bounded research after a concrete use case appears |
| `DEFERRED_UNTIL_MEASURED` | Requires benchmarks/observed need |
| `DEFERRED_AFTER_MANUAL_FLOW` | Requires stable manual contracts and drift evidence |
| `DEFERRED_UNTIL_RELEASE_TARGET` | Requires a real distribution/deployment target |
| `DEFERRED_SEPARATE_DECISIONS` | Requires separate domain/architecture/compliance decisions |
| `INTERNAL_RESEARCH_AFTER_CONTRACTS` | Development tooling only after stable contract/user need |

## 4. Feature family index

| ID | Feature family | Layer | Disposition | Human-readable outcome |
|---|---|---|---|---|
| `FTR-001` | Intent Intake, Task Intake Wizard and Outcome Clarification | Product Runtime | `CANDIDATE` | Создан Intent Record, в котором отдельно зафиксированы user, problem, desired outcome, context, constraints, non… |
| `FTR-002` | Read-only Project Discovery, Capability Map and Gap/Conflict Register | Product Runtime | `CANDIDATE` | Read-only Project Discovery package: verified repository identity, inventory, capability map, source/contract ma… |
| `FTR-003` | Project Brief, Specification, Technical Assignment and First Vertical Slice Selection | Product Runtime | `CANDIDATE` | Reviewable Project Brief/Specification with users, jobs, journeys, product boundaries, candidate capabilities, n… |
| `FTR-004` | Guided Bootstrap, Installer Dry-run, Safe Apply/Update/Uninstall and First-Start Experience | Product Runtime / Installation boundary | `HUMAN_DECISION_REQUIRED` | A guided, preview-first installation journey that classifies ownership, applies only authorized changes, verifie… |
| `FTR-005` | Architecture Need Check, Option Comparison, ADR Builder and Architecture-to-Task Traceability | Product Runtime support / Architecture boundary | `CANDIDATE` | A decision-ready architecture package that first decides whether architecture work is needed, compares bounded o… |
| `FTR-006` | Task Brief, Scope Confirmation, Task Compiler and Report Builder | Product Runtime / Development Factory boundary | `CANDIDATE` | A compact executable Task Brief and matching Stage Report schema, compiled from accepted inputs while preserving… |
| `FTR-007` | Hierarchical Backlog, Lazy Decomposition, Task Candidate Registry and Queue | Development Factory | `CANDIDATE_AFTER_MANUAL_NEED` | A navigable hierarchy that decomposes only when needed, preserves parent-child acceptance and clearly separates… |
| `FTR-008` | Simple Control Surface, Status/Next/Details, Beginner Tutor and Technical/Lifecycle Closure UX | Product Runtime | `CANDIDATE` | A compact control surface that derives current status, explains it in plain language, provides one next action,… |
| `FTR-009` | Repository/Action Preflight and Exact Execution Preview | Development Factory / Safety boundary | `CANDIDATE` | A read-only preflight and preview package binding subject identity, scope, planned actions, conflicts, permissio… |
| `FTR-010` | Scoped Execution Workflow, Controlled Execution Guard and Safe Runner Kernels | Development Factory | `CANDIDATE` | A bounded executor contract that consumes an authorized preview, performs only declared actions, records actual… |
| `FTR-011` | Unified Result Contract, Unified AOS Validate, Doctor and Self-Test | Product Runtime support / Development Factory | `CANDIDATE` | One strict ValidationEnvelope/result contract used by doctor, self-test, validators and CLI, preserving PASS/FAI… |
| `FTR-012` | Evidence Collection, Compact Human Review & Handoff Package, Semantic Guard and Human Decision Record | Product Runtime / Review boundary | `CANDIDATE` | One compact review document bound to exact candidate, with user-visible change, acceptance status, Evidence poin… |
| `FTR-013` | Diff/Scope Reconciliation, Disposable Validation Subject and Immutable Candidate Freeze | Development Factory / Validation boundary | `CANDIDATE` | Exact candidate identity and isolated validation subject, plus reconciliation of Task Brief/preview/actual diff… |
| `FTR-014` | Recovery, Resume, Rollback, Denied-Action Log and Session Handoff | Product Runtime / Development Factory boundary | `CANDIDATE` | A fail-closed recovery and resume package that preserves actual candidate/journal, denied actions, open findings… |
| `FTR-015` | Git Lifecycle Closure, Remote State, Commit/Push/Merge/Release Boundaries and Deterministic Merge Authorization | Development Factory / Delivery boundary | `CANDIDATE` | A closure package showing local candidate, validation, human acceptance, remote/PR/protection state and exactly… |
| `FTR-016` | Project Memory, Session Continuity, Context Priority and Task-scoped Context Pack | Product Runtime / Development Factory boundary | `CANDIDATE` | A minimal durable Project Memory and task-scoped Context Pack that preserve accepted decisions, current verified… |
| `FTR-017` | RAG-light Context Index and Search | Supporting runtime | `DEFERRED_UNTIL_MEASURED` | A rebuildable search index that retrieves candidate context with source, authority, freshness and confidence, wh… |
| `FTR-018` | Advisory Model Routing, Explicit Subagent Roles, Routing Audit and Provider Evaluation | Development Factory | `DEFERRED_UNTIL_MEASURED` | An auditable routing recommendation/record that separates roles, selects model/provider according to measured ta… |
| `FTR-019` | Action Trust Boundary, Permission-State Classifier, External-Content Boundary and Path/Command/Network Allowlists | Minimal Safety Floor | `CANDIDATE_CORE_SAFETY` | One consistent classifier that maps requested action and context to `ALLOWED`, `HUMAN_AUTHORIZATION_REQUIRED`, `… |
| `FTR-020` | Runtime Enforcement, Isolated Execution Environment and Progressive Governance Modes | Governance / Runtime Enforcement | `DEFERRED` | A progressive, disableable/replaceable enforcement layer admitted only after stable contracts and observed incid… |
| `FTR-021` | Registry/Drift Detection, Source-of-Truth Guard and Human-Decision Authenticity | Development Factory / Governance support | `DEFERRED_AFTER_MANUAL_FLOW` | Rebuildable consistency checks and authenticity gates that identify owner for each fact class, detect schema/doc… |
| `FTR-022` | Solution/Pattern Library, Fit Matrix and Reusable UX/Engineering Patterns | Knowledge support | `CANDIDATE_SUPPORT` | A curated library of problem→context→solution→trade-off→failure→test patterns with fit criteria, provenance, mat… |
| `FTR-023` | Advisory CI, CI Smoke, Safety Regression Fixtures and Quality Gates | Development Factory | `CANDIDATE_AFTER_BASELINE` | A staged test/CI profile with fast smoke, contract/negative fixtures and explicit NOT_RUN/optional quality check… |
| `FTR-024` | Release Checklist, Promotion Package, Version/Changelog/Tag and Rollback Assistant | Later lifecycle | `DEFERRED_UNTIL_RELEASE_TARGET` | A decision-ready release package that binds accepted merged artifacts, version/change summary, required checks,… |
| `FTR-025` | Observability, Audit Log, Incident/Lessons Memory and Continuous Improvement | Product Runtime support / Later operations | `CANDIDATE_SUPPORT` | A minimal event/incident/lesson loop that records material outcomes and converts them into reviewed preventive r… |
| `FTR-026` | Extension/Plugin/Capability Module Model | Architecture extension | `DEFERRED` | A minimal extension contract, admitted only after repeated extension points are observed, with versioning, capab… |
| `FTR-027` | Domain Modules: Medical and Design | Regulated/creative domain extensions | `DEFERRED_SEPARATE_DECISIONS` | Separate replaceable domain modules using stable core contracts, with domain-specific Feature Contracts, provide… |
| `FTR-028` | Workbench / SaaS UI for Onboarding, Status, Review and Collaboration | UX wrapper | `DEFERRED` | A UI that renders and edits accepted artifact contracts, shows source-linked status/Evidence and captures explic… |
| `FTR-029` | Template Export, Prompt Packs, Capability Modules, Cross-Repo Context, Localization and Policy Overlays | Packaging / Extension support | `DEFERRED_RESEARCH` | Versioned export/import/update contracts for templates and prompt/capability packs, with provenance, ownership,… |
| `FTR-030` | Internal Contract Tooling: Strict Loaders, Parser Sunset, Registry Audits, Manifest/Cross-reference Validation and Schema/Runtime Drift Tests | Development Factory internal | `INTERNAL_RESEARCH_AFTER_CONTRACTS` | A small set of strict, replaceable internal utilities that enforce accepted contracts, audit round trips and pac… |

## 5. Detailed feature dossiers

## FTR-001 — Intent Intake, Task Intake Wizard and Outcome Clarification

```yaml
feature_id: FTR-001
layer: Product Runtime
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-001` Problem / Intent Intake; `IDEA-002` Intake Classification and Sensitive-Domain Gate; `IDEA-003` User and Outcome Clarification  
**Source references:** `CHAT-002`, `CHAT-003`, `CHAT-006`, `CHAT-012`, `CHAT-013`, `CURRENT-INSTRUCTIONS`, `REF-AF-002`, `SRC-006`

### Problem

Пользователь начинает со свободного запроса, в котором цель, решение, constraints и implementation assumptions смешаны. Agent может сразу спроектировать не ту feature или пропустить sensitive-domain boundary.

### Target users

Non-programmer product owner, product lead, intake agent; при regulated context — designated human reviewer.

### Desired outcome

Создан Intent Record, в котором отдельно зафиксированы user, problem, desired outcome, context, constraints, non-goals, assumptions, unknowns и чувствительность данных. Пользователь видит точную переформулировку и выбирает следующий шаг.

### Trigger

Новая идея, problem report, change request или запрос «сделай проект/feature».

### Preconditions

- Известен язык взаимодействия и actor
- Если выбран existing project — repository только идентифицирован, но ещё не изменяется
- External/sensitive content помечен как untrusted data

### Inputs

- Свободный текст или voice-transcribed request
- Optional project/repository context
- Constraints: time, risk, compatibility, privacy, non-goals
- Known examples or desired observable result

### Outputs and observable behavior

- Versioned Intent Record
- Clarification summary approved or corrected by human
- Candidate problem/outcome statement
- Unknowns and required human decisions
- Recommended next route: Discovery, Project Brief, feature research or stop

### Main flow

1. Capture original request verbatim
2. Classify request type and sensitive-domain flags
3. Ask only material clarification questions; reuse known context
4. Separate outcome from proposed solution
5. State assumptions, non-goals and unknowns
6. Offer concise interpretation and wait for human correction/selection
7. Emit one next route without execution

### States and transitions

RAW → CLASSIFIED → CLARIFYING → READY_FOR_BRIEF | READY_FOR_DISCOVERY | BLOCKED_SENSITIVE | DEFERRED. Human correction can return any nonterminal state to CLARIFYING.

### Failure modes

- Leading interview forces a preferred architecture
- Known user context is asked again or contradicted
- Sensitive data is routed to an unapproved provider
- Long interview creates more friction than value
- Intent summary silently adds scope

### Recovery behavior

Preserve original request, show exact delta between original and normalized interpretation, allow human to edit/reject fields, and return to CLARIFYING. No downstream artifact remains authorized after material intent change.

### Dependencies and shared contracts

- Intent Record contract
- Permission/sensitive-domain classifier from FTR-019
- Project Memory lookup from FTR-016
- Product vocabulary from 01_Product.md

### Safety and human-authority boundaries

- No architecture selection
- No Risk Profile assignment
- No repository mutation
- No Task Brief or execution authorization generated implicitly
- Sensitive-domain classification advises/blocks routing but does not make clinical/legal decisions

### Acceptance criteria

- User can identify their problem and desired result in plain language
- Every added assumption is visible
- One next route is produced
- Human correction changes the durable record
- No implementation/Git operation occurs

### Required negative scenarios

- Empty request or vague “make it better” remains CLARIFYING
- Prompt-injected repository text cannot redefine user goal
- Generated approval/authorization field is rejected
- Sensitive input cannot be sent to unapproved provider

### Minimal implementation model candidate

Small schema-first intake service plus conversational adapter. Deterministic normalization stores original text, extracted fields and human edits. First version can be Markdown/JSON artifact generation without LLM routing automation.

### Targeted research before implementation

Inspect historical Task Intake Wizard, dogfood problem interview and Technical Assignment transitions. Determine which questions reduced ambiguity and which produced bureaucracy.

### Non-goals

- Automatic product approval
- Complete specification in one pass
- Architecture or dependency choice
- Autonomous execution
## FTR-002 — Read-only Project Discovery, Capability Map and Gap/Conflict Register

```yaml
feature_id: FTR-002
layer: Product Runtime
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-004` Project Discovery and Capability Map; `IDEA-005` Gap and Conflict Discovery  
**Source references:** `CHAT-009`, `CHAT-011`, `REF-A02-001`, `REF-AF-001`, `REF-AG-001`, `SRC-008`

### Problem

В existing project пользователь и agent не знают current capabilities, documentation/code boundaries, dependencies, conflicts, stale artifacts и missing contracts. Chat memory часто подменяет repository facts.

### Target users

Product owner, developer/agent, architecture reviewer and maintainer.

### Desired outcome

Read-only Project Discovery package: verified repository identity, inventory, capability map, source/contract map, gaps, conflicts, unknowns and bounded improvement candidates.

### Trigger

Пользователь подключает existing repository, спрашивает «что здесь есть/на чём остановились/что не так» или выбирает feature for reconstruction.

### Preconditions

- Read permission to exact repository/worktree
- Repository identity and inspection scope declared
- Network disabled unless separately authorized
- No cleanup or writes authorized

### Inputs

- Repository/worktree path
- Optional expected branch/baseline
- Discovery profile: product, architecture, workflow, feature or full orientation
- Known authoritative documents and ignore rules

### Outputs and observable behavior

- Repository identity snapshot
- Directory/artifact inventory with classes
- Capability map: observed, design-only, broken, unknown
- Gap and conflict register
- Candidate next objectives ranked by user value/risk, not automatically selected

### Main flow

1. Verify repository and worktree identity
2. Inventory high-signal artifacts and current diff
3. Locate accepted/draft/reference documents
4. Map user-facing commands, contracts, tests and implementation entry points
5. Classify observations and stale/conflicting claims
6. Build capability/gap map
7. Present one recommended bounded objective and alternatives for human choice

### States and transitions

UNBOUND → PREFLIGHTED → INVENTORIED → CLASSIFIED → REVIEW_READY | BLOCKED_IDENTITY | PARTIAL_WITH_GAPS.

### Failure modes

- Treats README claims as working code
- Scans huge generated/vendor trees and loses signal
- Current dirty state is ignored or mistaken for feature
- Discovery silently edits/fixes files
- Generated map becomes competing Source of Truth

### Recovery behavior

Record exact unreadable paths and partial coverage, preserve `UNKNOWN/NOT_FOUND/NOT_RUN`, let human narrow scope or authorize additional read access, and rerun against a fresh bound snapshot.

### Dependencies and shared contracts

- Repository preflight contract
- Claim/source model from 00_Core.md
- Reference classification from 05_Reference.md
- Optional pattern library FTR-022

### Safety and human-authority boundaries

- Strictly read-only
- No automatic cleanup, architecture acceptance or backlog mutation
- No current-state claim from chat history
- Derived map remains rebuildable

### Acceptance criteria

- Repository identity and temporal scope visible
- Every material capability claim has locator and classification
- Gaps distinguish missing evidence from confirmed absence
- No repository mutation
- Human can choose one bounded next objective

### Required negative scenarios

- Wrong repository or changed HEAD detected
- Missing tests cannot be reported as PASS
- Symlink/nested repository does not escape scope
- Untracked environment noise is classified, not blindly blocking

### Minimal implementation model candidate

Read-only inventory adapters plus pluggable classifiers producing a Markdown/JSON discovery package. Start with filesystem/Git and explicit document/command/test heuristics; no graph database required.

### Targeted research before implementation

Compare historical Project Discovery proposal with actual AOS-FARM/AgentOS analyzers, if any. Inspect whether capability map was generated from tests or narrative docs.

### Non-goals

- Automatic refactor
- Architecture decision
- Repository-wide semantic proof
- Continuous registry in first version
## FTR-003 — Project Brief, Specification, Technical Assignment and First Vertical Slice Selection

```yaml
feature_id: FTR-003
layer: Product Runtime
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-006` Project Brief and Specification Builder; `IDEA-007` Technical Assignment; `IDEA-008` First Vertical Slice Selector and Capability Reconstruction  
**Source references:** `CHAT-002`, `CHAT-006`, `CHAT-009`, `CHAT-012`, `REF-AF-002`, `SRC-008`

### Problem

После intake/discovery знания остаются разрозненными: непонятно, какой product boundary выбран, какая feature первая и что будет observable success. Technical Assignment может преждевременно превратиться в implementation plan.

### Target users

Product owner, domain stakeholder, architect and implementation agent.

### Desired outcome

Reviewable Project Brief/Specification with users, jobs, journeys, product boundaries, candidate capabilities, non-goals, success indicators and one proposed vertical slice. Technical Assignment describes behavior and constraints, not hidden authorization.

### Trigger

Intent approved enough for product definition, or Discovery reveals a candidate improvement.

### Preconditions

- Intent Record exists
- Material conflicts/unknowns disclosed
- No architecture or dependency assumed accepted
- Target user and outcome identifiable

### Inputs

- Intent Record
- Discovery package when applicable
- User constraints and non-goals
- Feature families from 06_Features.md
- Relevant lessons and reference findings

### Outputs and observable behavior

- Project Brief
- Feature/Technical Assignment candidate
- User journey and acceptance outline
- Vertical-slice comparison
- Decision package for human slice selection

### Main flow

1. Define product purpose and target users
2. Map problems to outcomes and journeys
3. Select in-scope/out-of-scope capabilities
4. Describe observable behavior and failure experience
5. Generate 1–3 vertical-slice options with value/risk/dependency trade-offs
6. Check each against Product Runtime criteria
7. Human selects/revises/defers
8. Only selected option proceeds to Architecture/Task Brief

### States and transitions

DRAFTING → PRODUCT_REVIEW → SLICE_OPTIONS → HUMAN_DECISION_REQUIRED → SELECTED | NEEDS_REVISION | DEFERRED.

### Failure modes

- Specification copies legacy topology
- Slice is internal governance/repository demo without user value
- Too many features bundled into “MVP”
- Technical Assignment assigns stack/dependencies without decision
- Acceptance is vague or nonobservable

### Recovery behavior

Return to the earliest unresolved product question, preserve rejected options/rationale, and narrow to one user/job/outcome. Material scope change invalidates downstream architecture/task artifacts.

### Dependencies and shared contracts

- Intent and Discovery artifacts
- Feature dossier schema
- Product acceptance model
- Architecture need check FTR-005

### Safety and human-authority boundaries

- No implementation authorization
- No required/deferred status without human decision
- No dependency selection
- No claim that documentation equals working product

### Acceptance criteria

- A non-technical stakeholder understands who gets what value
- Selected slice has inputs, outputs, failure/recovery and tests
- Internal machinery is separated from Product Runtime
- Non-goals and unknowns explicit
- Human selection exact and recorded

### Required negative scenarios

- A registry-only demo rejected as first product slice
- Scaffolding accepted only with direct user job/outcome
- Unresolved compatibility cannot be silently assumed
- A generated priority cannot become roadmap commitment

### Minimal implementation model candidate

Document compiler using normalized Intent, Discovery and Feature Dossiers. It can produce Markdown templates and consistency checks; slice ranking remains advisory and human-decided.

### Targeted research before implementation

Review historical Technical Assignment, task-candidate and capability-reconstruction flows. Identify useful structure without importing old task registry lifecycle.

### Non-goals

- Detailed code design
- Full roadmap
- Automatic priority acceptance
- Execution or Git delivery
## FTR-004 — Guided Bootstrap, Installer Dry-run, Safe Apply/Update/Uninstall and First-Start Experience

```yaml
feature_id: FTR-004
layer: Product Runtime / Installation boundary
disposition: HUMAN_DECISION_REQUIRED
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-042` Installer Dry-run; `IDEA-043` Safe Apply and Manual Transfer; `IDEA-044` Safe Update and Uninstall; `IDEA-045` Installation Manifest and Version Detection; `IDEA-046` Example Project and Onboarding  
**Source references:** `CHAT-002`, `CHAT-014`, `CHAT-015`, `REF-A02-001`, `REF-AF-001`, `REF-AG-001`, `SRC-004`

### Problem

Подключение AOS к project repository требует нескольких manual steps and overlapping guides. Installer/update can overwrite user state, while first-time user may not know the first safe commands or how to interpret status.

### Target users

Non-programmer adopter, project maintainer and support/reviewer.

### Desired outcome

A guided, preview-first installation journey that classifies ownership, applies only authorized changes, verifies installation, provides one authoritative FIRST-START path, example project and first safe command bundle.

### Trigger

User chooses to add, update, repair or remove AOS in a target project.

### Preconditions

- Target repository identity verified
- Install mode and target path human-selected
- Package/version identity known
- Write/network permissions explicit
- Backup/recovery conditions defined

### Inputs

- Target repository/worktree
- AOS package or template version
- Install profile
- Existing files and user modifications
- Desired operation: dry-run/apply/update/repair/remove

### Outputs and observable behavior

- Exact operation preview
- Conflict/ownership report
- Install/update manifest
- Applied state or no-change result
- Doctor/self-test result
- FIRST-START card and authoritative route
- Rollback/recovery instructions

### Main flow

1. Read-only inspect target and installed state
2. Classify paths as AOS-managed, user-config, project-state, generated cache, reports/decisions or temporary
3. Compute create/modify/delete/conflict set
4. Show dry-run and bind preview identity
5. Human authorizes exact operation
6. Apply atomically or journaled
7. Reconcile actual state
8. Run doctor/validation
9. Display first safe commands, status meanings and one next action

### States and transitions

NOT_INSTALLED → PLANNED → CONFLICTED | READY_TO_APPLY → APPLYING → INSTALLED | PARTIAL_RECOVERY_REQUIRED; INSTALLED → UPDATE_AVAILABLE → UPDATED; INSTALLED → REMOVE_PLANNED → REMOVED_WITH_STATE_PRESERVED.

### Failure modes

- Placeholder/root template shipped
- Apply path not implemented but docs imply it is
- FIRST-START/START_HERE/INSTALL docs conflict
- Preview becomes stale before apply
- User/project-owned state overwritten
- Partial transfer leaves mixed version
- Uninstall removes decisions/reports

### Recovery behavior

No writes on dry-run. Apply uses transaction/journal and records completed operations. On interruption, reconcile manifest vs actual tree; preserve human/user/project data; offer resume or explicitly authorized rollback.

### Dependencies and shared contracts

- Install/update manifest contract
- Preflight/preview FTR-009
- Doctor/validation FTR-011
- Permission/path guards FTR-019
- Status/tutor FTR-008

### Safety and human-authority boundaries

- Dry-run read-only
- Apply/update/remove require explicit authorization
- Exact path `/aos/` or alternative remains architecture/product decision
- No hidden package install/network
- Removal never deletes durable human decisions by default

### Acceptance criteria

- Second identical apply is idempotent
- Conflicts shown before mutation
- Existing user content preserved
- Doctor verifies exact installed subject
- One authoritative onboarding path; duplicate docs are pointers
- Beginner completes first safe action and understands result

### Required negative scenarios

- Changed target after preview rejects apply
- User-modified managed file produces conflict, not overwrite
- Interrupted write is recoverable
- Uninstall preserves declared durable state
- Unknown version does not report successful update

### Minimal implementation model candidate

Manifest-driven installer with pure planning function and transactional executor. First version may support local package copy only; update/remove reuse same ownership/reconciliation model. FIRST-START is generated from accepted command/status contracts, not duplicated prose.

### Targeted research before implementation

Inspect historical dry-run installer, manual transfer, `--apply` gap, root-template placeholder, FIRST-START dedup and prompt-pack boundary drift. Determine exact user-owned artifacts.

### Non-goals

- Remote SaaS provisioning
- Automatic dependency installation without permission
- Migration of every legacy folder
- Implicit Git commit/push
## FTR-005 — Architecture Need Check, Option Comparison, ADR Builder and Architecture-to-Task Traceability

```yaml
feature_id: FTR-005
layer: Product Runtime support / Architecture boundary
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-009` Architecture Need Check and Input Intake; `IDEA-010` Architecture Assistant; `IDEA-011` Architecture Option Comparison and ADR Builder; `IDEA-012` Stack Preset Registry; `IDEA-014` Architecture Evidence and Human Checkpoint Package; `IDEA-015` Architecture-to-Task Traceability  
**Source references:** `CHAT-006`, `CHAT-009`, `REF-A02-001`, `REF-AF-002`, `SRC-004`, `SRC-008`, `SRC-009`

### Problem

Material technical choices are either made implicitly by the coding agent or expanded into a heavy architecture program. Stack presets and historical patterns can be mistaken for approved architecture.

### Target users

Product owner, architect, lead developer, security/privacy reviewer and implementation agent.

### Desired outcome

A decision-ready architecture package that first decides whether architecture work is needed, compares bounded options, records trade-offs/evidence and links accepted decision to affected features/tasks/tests.

### Trigger

Selected feature has material choices involving interfaces, persistence, dependencies, security, compatibility, module boundary or irreversible cost.

### Preconditions

- Feature Product Contract sufficiently detailed
- Question and decision owner explicit
- Legacy/reference findings classified
- No option preselected as accepted

### Inputs

- Feature dossier
- Constraints and quality attributes
- Candidate options/presets/patterns
- Evidence, experiments and unknowns
- Relevant lessons and dependency/security boundaries

### Outputs and observable behavior

- Architecture-need result
- Option comparison
- DRAFT ADR
- Human checkpoint package
- Decision record when human acts
- Trace links to feature, contracts, tasks and tests

### Main flow

1. Run need check: routine/local vs material decision
2. Frame one architecture question
3. Generate or collect bounded options including simplest/no-new-component option
4. Compare value, complexity, dependencies, failure/recovery, reversibility, compatibility and security
5. Identify evidence gaps/prototypes
6. Present recommendation as proposal
7. Human ACCEPT/REVISE/DEFER/REJECT
8. Propagate accepted decision references without rewriting history

### States and transitions

NOT_REQUIRED | QUESTION_DRAFT → OPTIONS_READY → EVIDENCE_GAP | HUMAN_REVIEW_REQUIRED → ACCEPTED | NEEDS_REVISION | DEFERRED | REJECTED.

### Failure modes

- Architecture ceremony for routine task
- Stack preset auto-selected
- Legacy component existence used as justification
- ADR accepted by agent output
- Decision not propagated to Task Brief/tests
- Architecture dashboard becomes Source of Truth

### Recovery behavior

Preserve rejected/deferred options and rationale, reopen only on explicit trigger or changed constraints, invalidate downstream artifacts if accepted decision identity changes.

### Dependencies and shared contracts

- Feature Contract
- Pattern library FTR-022
- Decision authenticity/drift FTR-021
- Reference findings
- Task Brief FTR-006

### Safety and human-authority boundaries

- Human accepts architecture/dependency choices
- No execution or Git authorization
- Preset is evidence/starting point only
- Architecture support cannot create new product scope

### Acceptance criteria

- Need check avoids unnecessary ADR
- Options include trade-offs and recovery
- Unknowns/evidence gaps visible
- Human decision bound to exact artifact
- Accepted decision traceable to tasks/tests
- No hidden dependency introduced

### Required negative scenarios

- Single-option “comparison” rejected
- Generated ACCEPT rejected
- Stale ADR cannot authorize new candidate
- Missing security/privacy analysis blocks only affected decision
- Decision link mismatch detected

### Minimal implementation model candidate

Markdown/JSON ADR compiler plus consistency checker. Architecture Assistant may suggest options, but human checkpoint is mandatory. Read-only dashboard can be derived later.

### Targeted research before implementation

Inspect Architecture Lifecycle Integration artifacts, option/stack preset concepts and whether any dogfood showed measurable decision improvement. Separate useful schema from heavy lifecycle.

### Non-goals

- Automatic architecture
- Permanent stack registry in MVP
- Full enterprise governance
- Implementation or release
## FTR-006 — Task Brief, Scope Confirmation, Task Compiler and Report Builder

```yaml
feature_id: FTR-006
layer: Product Runtime / Development Factory boundary
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-016` Task Generation and Task Brief; `IDEA-076` Task Brief Compiler and Report Builder  
**Source references:** `CHAT-005`, `CHAT-006`, `REF-A02-001`, `REF-AF-002`, `REF-AG-001`, `SRC-007`

### Problem

User intent and feature contract do not directly constrain code-writing agent. Scope, repository identity, risk, checks and stop conditions can remain implicit; repeated manual formatting causes drift.

### Target users

Product owner, task author, coding agent, validator and reviewer.

### Desired outcome

A compact executable Task Brief and matching Stage Report schema, compiled from accepted inputs while preserving explicit human authorization boundaries.

### Trigger

A selected feature/change is ready for a bounded PLAN, EXECUTE, VALIDATE or REVIEW stage.

### Preconditions

- Goal/user outcome known
- Relevant product/architecture decisions available
- Repository target identifiable or marked unknown
- Required Risk Profile decision boundary understood

### Inputs

- Feature dossier and accepted decisions
- Repository/preflight facts
- Allowed/forbidden paths and operations
- Validation matrix
- Permissions, dependencies and stop conditions

### Outputs and observable behavior

- Task Brief draft
- Completeness diagnostics
- Human decision fields kept false/unassigned
- Stage-specific prompt/context pack
- Stage Report template matched to Brief

### Main flow

1. Collect authoritative inputs by fact class
2. Normalize scope and operations
3. Detect missing/contradictory fields
4. Classify planning_required
5. Generate bounded stage instructions
6. Present human-decision fields separately
7. After stage, compile actual report from observed facts and checks
8. Check report claims against Brief and Evidence

### States and transitions

INCOMPLETE → DRAFT_COMPLETE → HUMAN_AUTHORIZATION_REQUIRED → AUTHORIZED_FOR_EXACT_STAGE → CONSUMED | INVALIDATED | SUPERSEDED.

### Failure modes

- Compiler invents missing scope or Risk Profile
- Complete Brief treated as authorization
- Plan and execution merged
- Report copied expected instead of actual changes
- Authorization reused after subject changes
- Prompt too large and repeats all project context

### Recovery behavior

Return diagnostics listing exact missing/conflicting fields; preserve human-authored values; invalidate generated prompt/report when repository or decision identity changes; regenerate only affected sections.

### Dependencies and shared contracts

- Task Brief shared contract
- Project Memory/context pack FTR-016
- Preflight FTR-009
- Authority/permission FTR-019
- Evidence/review FTR-012

### Safety and human-authority boundaries

- Compiler cannot assign Risk Profile or human decision
- No scope/network/sandbox expansion
- No automatic execution
- Report generation cannot upgrade NOT_RUN/UNKNOWN

### Acceptance criteria

- Brief has exact goal, scope, identity, permissions, validation and stop conditions
- Planning decision is explainable
- Human authorization remains explicit
- Generated stage prompt contains minimally sufficient context
- Report shows actual vs planned and one next action

### Required negative scenarios

- Omitted authorization defaults false
- Changed HEAD invalidates exact Brief where required
- Out-of-scope path cannot enter compiled prompt silently
- Expected check not run remains NOT_RUN
- Copied authorization record rejected

### Minimal implementation model candidate

Schema-first compiler with deterministic merge precedence and validation diagnostics. Start as CLI/library creating Markdown plus JSON sidecar internally; no registry required.

### Targeted research before implementation

Inspect historical Task Brief compiler/report builder, task-candidate conversion and source precedence. Identify fields that prevented real failures versus fields adding ceremony.

### Non-goals

- Task execution
- Automatic prioritization
- Human approval
- Central workflow engine
## FTR-007 — Hierarchical Backlog, Lazy Decomposition, Task Candidate Registry and Queue

```yaml
feature_id: FTR-007
layer: Development Factory
disposition: CANDIDATE_AFTER_MANUAL_NEED
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-017` Hierarchical Backlog, Lazy Decomposition and Queue; `IDEA-075` Document, Task Registry and Queue Helpers  
**Source references:** `REF-AF-001`, `REF-AG-001`, `SRC-005`, `SRC-007`, `SRC-010`

### Problem

Large goals need decomposition, but early full backlog creates speculative tasks and status noise. Task candidate, actual task, queue membership, approval and execution can be conflated.

### Target users

Product owner, planner, team lead and implementation agents.

### Desired outcome

A navigable hierarchy that decomposes only when needed, preserves parent-child acceptance and clearly separates idea, task candidate, accepted task, queue state and execution authority.

### Trigger

Selected objective cannot be completed/reviewed as one bounded task or repeated work needs queue visibility.

### Preconditions

- Parent objective and acceptance known
- Decomposition reason material
- Status vocabulary and authority boundaries defined
- No assumption that registry is Source of Truth

### Inputs

- Epic/stage objective
- Feature dependencies
- Risk/authority boundaries
- Current accepted tasks and outcomes
- Capacity/ordering constraints where human-provided

### Outputs and observable behavior

- Hierarchy and child candidates
- Parent-child traceability
- Dependency/blocked reasons
- Queue view derived from accepted task records
- One next candidate for human selection

### Main flow

1. Evaluate whether split is necessary
2. Create minimum child set around distinct outcome/authority/validation boundary
3. Link each child contribution to parent acceptance
4. Human accepts/rejects candidates
5. Queue only accepted task records
6. Update parent progress from terminal child outcomes, not counts alone
7. Decompose deeper only when next child becomes actionable

### States and transitions

IDEA → TASK_CANDIDATE → HUMAN_SELECTED_TASK → QUEUED | DEFERRED | REJECTED → ACTIVE_STAGE → TERMINAL_RESULT. None implies approval of next state.

### Failure modes

- Speculative backlog explosion
- Closed children falsely complete parent
- Registry silently drops fields/items
- Queue order treated as authorization
- Agent mutates priorities
- Task candidate written as executable task without review

### Recovery behavior

Rebuild derived queue from durable task records; audit missing/lost fields; preserve superseded candidates; require human reselection after material decomposition change.

### Dependencies and shared contracts

- Task Brief FTR-006
- Project Memory FTR-016
- Drift/registry guard FTR-021
- Status surface FTR-008

### Safety and human-authority boundaries

- Backlog/queue is planning aid
- No auto scheduling/execution
- Priority and acceptance human-controlled
- Derived registry rebuildable

### Acceptance criteria

- Every child maps to parent outcome
- Task candidate/accepted task/queue/execution states distinct
- Lazy expansion reduces speculative records
- Registry round-trip preserves all fields
- One next action visible without auto-start

### Required negative scenarios

- Empty/malformed registry rejected
- Unknown child status cannot close parent
- Queue insertion does not set authorized=true
- Deleted/omitted record detected by reconciliation
- Parallel writes prevented

### Minimal implementation model candidate

Markdown/JSON task records with deterministic index/queue generator and integrity checks. Start without database or autonomous scheduler.

### Targeted research before implementation

Inspect `Декомпозиция ТЗ`, historical task registry/queue helpers and AOS-FARM.601 task-candidate conversion. Identify actual user need before building registry runtime.

### Non-goals

- Autonomous project management
- Dynamic resource scheduling
- Approval engine
- Mandatory central database
## FTR-008 — Simple Control Surface, Status/Next/Details, Beginner Tutor and Technical/Lifecycle Closure UX

```yaml
feature_id: FTR-008
layer: Product Runtime
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-047` Beginner Tutor; `IDEA-048` Simple Control Surface; `IDEA-049` Status / Next / Details, Stable CLI Output and First Safe Commands  
**Source references:** `CHAT-003`, `CHAT-013`, `CHAT-015`, `REF-A02-001`, `REF-A02-002`, `REF-AF-001`, `REF-AG-001`, `SRC-004`

### Problem

Non-programmer cannot quickly tell current state, what a blocker means, whether work is technically complete, or which safe command/action comes next. Commands and first-start guidance can be fragmented.

### Target users

Primary non-programmer/vibe-coder, maintainer and any agent resuming work.

### Desired outcome

A compact control surface that derives current status, explains it in plain language, provides one next action, optional details, first safe commands and a closure checklist without granting authority.

### Trigger

User enters project, completes a stage, encounters blocker, resumes session or asks “что дальше/на чём остановились?”.

### Preconditions

- Project Memory/current facts available
- Source owners identified
- Surface is read-only unless user explicitly invokes a separate operation
- Status vocabulary consistent

### Inputs

- Repository/project state
- Active Task Brief and stage result
- Validation/review/human decisions
- Git/local/remote closure facts where permitted
- User expertise profile

### Outputs and observable behavior

- `/status` summary
- `/next` one bounded action
- `/details` supporting context
- Plain-language blocker/status explanation
- FIRST-START card and first-safe-command bundle
- Technical/lifecycle closure view

### Main flow

1. Collect current facts from owned sources
2. Resolve conflicts/staleness
3. Compute technical stage status separately from human/Git state
4. Render beginner summary
5. Choose one next required action by deterministic priority
6. Offer details and source pointers
7. Stop; user explicitly invokes any mutation

### States and transitions

NO_CONTEXT | ORIENTED | ACTION_REQUIRED | BLOCKED | TECHNICALLY_COMPLETE | HUMAN_REVIEW_REQUIRED | ACCEPTED_NOT_DELIVERED | DELIVERED. Surface state is derived, not authoritative.

### Failure modes

- Dashboard cache diverges from repository
- `/next` auto-executes
- PASS displayed as accepted
- Too many statuses without explanation
- First-start docs duplicate/conflict
- Remote/Git closure guessed from local state

### Recovery behavior

Show stale/conflicting source and safe fallback status, require refresh/reinspection, keep last known status clearly historical, never auto-correct underlying artifacts.

### Dependencies and shared contracts

- Project Memory FTR-016
- Unified Result FTR-011
- Review/Decision FTR-012
- Git closure FTR-015
- Source-of-Truth guard FTR-021

### Safety and human-authority boundaries

- Read-only by default
- No Risk/approval/Git authorization
- Generated status is view only
- Remote checks require permission
- Tutor never hides technical limitations

### Acceptance criteria

- Beginner explains current state and next action correctly
- One next action, not a list of hidden stages
- Technical/human/Git statuses visually distinct
- Every status links to evidence/source
- No writes from status/help/details

### Required negative scenarios

- Missing validation remains NOT_RUN
- Stale candidate displays blocked refresh
- Accepted but unpushed is not “closed”
- Unknown remote state not inferred
- Help/status leaves tree unchanged

### Minimal implementation model candidate

Deterministic status compiler over Project Memory and repository adapters, with plain-language renderer. Start with CLI/chat commands; local UI later consumes same contract.

### Targeted research before implementation

Inspect Simple Control Surface, FIRST-START-CARD, status interpretation, AOS-FARM.610 lifecycle UX helper and technical closure evaluator. Measure first-contact dogfood comprehension.

### Non-goals

- Autonomous orchestrator
- Source of Truth database
- Automatic Git action
- Full IDE dashboard in first version
## FTR-009 — Repository/Action Preflight and Exact Execution Preview

```yaml
feature_id: FTR-009
layer: Development Factory / Safety boundary
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-018` Action Preflight; `IDEA-019` Execution Preview  
**Source references:** `CHAT-005`, `REF-A02-001`, `REF-AF-001`, `REF-AF-002`, `SRC-006`

### Problem

Mutation may begin with wrong repository, branch, baseline, dirty state, permissions or stale assumptions. Human cannot approve what they cannot preview exactly.

### Target users

Coding agent, task owner, validator and human authorizer.

### Desired outcome

A read-only preflight and preview package binding subject identity, scope, planned actions, conflicts, permissions, checks and stop conditions before any write.

### Trigger

Any Task Brief requests mutation, protected operation, network use, install/update or Git action.

### Preconditions

- Task Brief exists
- Read access to subject
- Expected identity available or explicitly unknown
- No writes yet

### Inputs

- Task Brief
- Repository/worktree path
- Expected branch/HEAD/baseline
- Allowed paths/commands
- Sandbox/network/Git permissions
- Planned operations

### Outputs and observable behavior

- Verified identity snapshot
- Dirty-state classification
- Normalized scope/allowlist
- Exact create/modify/delete/command preview
- Conflict/blocker list
- Preview digest/identity and authorization request

### Main flow

1. Verify repository/worktree/branch/HEAD/baseline
2. Capture staged/unstaged/relevant untracked state
3. Normalize paths and detect symlink/nested-repo escape
4. Classify requested operations and permissions
5. Compute exact preview
6. Run non-mutating feasibility checks
7. Show limitations and required human decision
8. Bind authorization to unchanged preview/subject

### States and transitions

UNBOUND → IDENTITY_VERIFIED → SCOPE_VERIFIED → PREVIEW_READY → HUMAN_AUTHORIZATION_REQUIRED | BLOCKED | INVALIDATED.

### Failure modes

- Raw remote secret printed
- All untracked files treated same
- Preview omits generated/deleted paths
- Subject changes after preview
- Command side effects not modeled
- Unknown permission silently allowed

### Recovery behavior

No mutation means rerun after resolving identity/scope/permission. Changed subject invalidates preview and any associated authorization. Preserve blocker report without secrets.

### Dependencies and shared contracts

- Task Brief FTR-006
- Permission taxonomy FTR-019
- Install manifest FTR-004 where applicable
- Project Memory FTR-016

### Safety and human-authority boundaries

- Strictly read-only
- Cannot assign Risk Profile
- Cannot execute or stage changes
- Network/remote inspection separately permissioned
- Preview identity single-purpose

### Acceptance criteria

- Wrong repo/branch/HEAD detected
- Planned paths and commands exact
- Out-of-scope state classified
- Human sees what will and will not change
- Stale preview rejected
- No repository side effect

### Required negative scenarios

- Path traversal/symlink/nested repo blocked
- Credential-bearing remote redacted
- Changed file after preview invalidates authorization
- Missing baseline produces scoped BLOCKED/UNKNOWN
- Read-only checker tree digest unchanged

### Minimal implementation model candidate

Pure preflight library plus repository adapters and preview renderer. Operation planners produce structured actions consumed by later executor; no shared mutable registry required.

### Targeted research before implementation

Inspect harness Action Trust table, AOS-02 execution preview and AOS-FARM repository checks. Retain high-value checks, remove hash ceremony without user/risk value.

### Non-goals

- Execution
- Automatic correction
- Risk assignment
- Remote mutation
## FTR-010 — Scoped Execution Workflow, Controlled Execution Guard and Safe Runner Kernels

```yaml
feature_id: FTR-010
layer: Development Factory
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-020` Scoped Execution; `IDEA-021` Controlled Execution Guard; `IDEA-074` Safe Runner Kernels  
**Source references:** `CHAT-005`, `CHAT-006`, `REF-AF-002`, `SRC-007`

### Problem

Even with a Task Brief, agents/scripts may expand scope, chain stages, run unsafe commands, mutate after failure or use inconsistent runner behavior.

### Target users

Coding agent, automation author, task owner and reviewer.

### Desired outcome

A bounded executor contract that consumes an authorized preview, performs only declared actions, records actual mutations/checks and stops after one stage or material finding.

### Trigger

Exact EXECUTE authorization for unchanged Task Brief/preview/candidate context.

### Preconditions

- Preflight PASS for required conditions
- Human execution authorization exact and current
- Runner environment identified
- Recovery/journal initialized before first write

### Inputs

- Authorized Task Brief and preview
- Structured action list
- Allowed commands/paths
- Environment/sandbox configuration
- Inline targeted checks

### Outputs and observable behavior

- Applied bounded change or fail-before-write result
- Operation journal
- Actual diff and changed paths
- Check results
- Stage Report with one next action

### Main flow

1. Verify authorization and subject freshness
2. Initialize transaction/journal
3. Execute actions sequentially through safe kernel
4. Before each action recheck class/scope where needed
5. Capture outputs/redact secrets
6. On material deviation/failure stop further writes
7. Reconcile intended vs actual
8. Run allowed targeted checks
9. Emit report and stop

### States and transitions

READY → AUTHORIZED → MUTATING → CHECKING → COMPLETED | FAILED_NO_WRITE | FAILED_PARTIAL | BLOCKED_DEVIATION. No automatic transition to VALIDATE.

### Failure modes

- Runner executes shell string outside contract
- Parallel writes race
- Agent fixes unexpected validation issue in same run
- Partial failure lacks recovery facts
- Command expands network/sandbox
- Report claims planned rather than actual changes

### Recovery behavior

If no write, close with blocker. If partial, freeze actual state and journal, prohibit retry until human-approved recovery Task Brief. Reconciliation determines resume vs rollback; both separately authorized.

### Dependencies and shared contracts

- Preflight FTR-009
- Permission/allowlists FTR-019
- Task Brief FTR-006
- Recovery FTR-014
- Evidence FTR-012

### Safety and human-authority boundaries

- One run one stage
- No auto retry/next task
- No validation fixes
- No commit/push/merge/release
- No permission expansion
- Protected/destructive operation exact human authorization

### Acceptance criteria

- Only allowed paths/commands changed
- Actual diff matches or is stricter than preview
- Failure stops safely
- Journal supports deterministic reconciliation
- Report honest and compact
- Tree not modified after terminal report/freeze

### Required negative scenarios

- Unauthorized command/path rejected
- Changed authorization/preview rejected
- Failure after each action boundary recoverable
- Parallel write attempt blocked
- External content cannot inject command
- Runner exception cannot return PASS

### Minimal implementation model candidate

Small execution kernel with typed action handlers (write/rename/delete/command) and policy hook. Start with limited actions and local environment; broader sandbox/enforcement deferred.

### Targeted research before implementation

Inspect controlled execution guard and safe runner kernels from Third Pass plan, plus actual scope failures. Determine minimum handler set for first slice.

### Non-goals

- Autonomous multi-stage workflow
- General shell replacement
- Full runtime enforcement platform
- Git delivery
## FTR-011 — Unified Result Contract, Unified AOS Validate, Doctor and Self-Test

```yaml
feature_id: FTR-011
layer: Product Runtime support / Development Factory
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-022` Unified Result Contract / ValidationEnvelope; `IDEA-023` Unified Validation CLI; `IDEA-024` Doctor and Self-Test  
**Source references:** `CHAT-013`, `REF-A02-001`, `REF-AF-001`, `REF-AF-002`, `REF-AG-001`, `SRC-007`, `SRC-009`

### Problem

Different commands/tests/reporters use inconsistent statuses, exit codes and output formats. Environment or missing checks can produce false-green results; beginners cannot interpret readiness.

### Target users

End user, developer, validator, CI and support agent.

### Desired outcome

One strict ValidationEnvelope/result contract used by doctor, self-test, validators and CLI, preserving PASS/FAIL/BLOCKED/UNKNOWN/NOT_RUN and exact subject/environment identity.

### Trigger

Post-install check, pre-task health check, feature validation, CI smoke or user command `/validate`/doctor.

### Preconditions

- Validation subject identified
- Required/optional check profile selected
- Environment/interpreter known or explicitly unknown
- Validation read-only

### Inputs

- Subject identity
- Check profile
- Environment/dependency facts
- Feature acceptance criteria or install manifest
- Optional expected baseline/candidate

### Outputs and observable behavior

- Machine-readable ValidationEnvelope
- Human-readable summary
- Exit code according to accepted CLI contract
- Per-check evidence/limitations
- One next action

### Main flow

1. Load strict check profile
2. Verify subject/import provenance
3. Run deterministic lightweight checks first
4. Run permitted deeper checks
5. Record each result and NOT_RUN reason
6. Aggregate fail-closed without hiding unknowns
7. Render beginner explanation and remediation category
8. Emit terminal result with no subject writes

### States and transitions

NOT_STARTED → RUNNING → PASS | FAIL | BLOCKED | UNKNOWN | PARTIAL_NOT_RUN. Aggregate policy distinguishes required and optional checks.

### Failure modes

- Unknown status accepted
- bool-as-int/schema drift
- CLI returns 0 on domain failure
- Missing dependency silently skipped
- Validator imports live checkout instead of installed subject
- Doctor modifies repository
- PASS wording implies approval

### Recovery behavior

Validation never repairs. It reports exact failing/unavailable checks and routes to environment resolution, correction Task Brief or human review. Re-run only against explicitly selected subject.

### Dependencies and shared contracts

- Unified Result contract
- Evidence FTR-012
- Disposable subject FTR-013
- CI profile FTR-023
- Status surface FTR-008

### Safety and human-authority boundaries

- PASS technical only
- No human acceptance
- No automatic dependency install/network
- Read-only
- Required NOT_RUN prevents PASS

### Acceptance criteria

- Same contract across CLI/doctor/tests
- Every exit path machine-readable
- Subject and interpreter provenance visible
- Required/optional distinction correct
- No repository mutation
- Beginner understands blocker and next action

### Required negative scenarios

- Empty/unknown/extra fields rejected
- Invalid args yield contract result and non-success exit
- Missing interpreter/dependency produces NOT_RUN/BLOCKED
- Wrong import path detected
- Validation side effect detected
- CI PASS cannot set human decision

### Minimal implementation model candidate

Strict data model and aggregator library used by all adapters. CLI commands are thin wrappers. Begin with stdlib/local checks and explicit profiles; no broad plugin system required.

### Targeted research before implementation

Inspect historical Unified AOS Validate, doctor, 503-test hygiene, ValidationEnvelope, CLI exit defects and self-test entrypoints. Preserve proven negative fixtures.

### Non-goals

- Approval engine
- Auto-fix
- Full observability platform
- Universal test framework
## FTR-012 — Evidence Collection, Compact Human Review & Handoff Package, Semantic Guard and Human Decision Record

```yaml
feature_id: FTR-012
layer: Product Runtime / Review boundary
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-025` Evidence Collection; `IDEA-026` Compact Human Review Package; `IDEA-027` Independent Read-only Review; `IDEA-028` Human Decision Record and False-PASS Wording Guard  
**Source references:** `CHAT-005`, `CHAT-006`, `CHAT-013`, `CURRENT-INSTRUCTIONS`, `REF-A02-001`, `REF-A02-002`, `REF-AF-002`, `REF-AG-001`, `SRC-006`

### Problem

User receives long technical logs or an overconfident summary; Evidence, recommendation and approval blur. Handoff packages may omit limitations or imply authorization.

### Target users

Human product owner/reviewer, validator, next-session agent and auditor.

### Desired outcome

One compact review document bound to exact candidate, with user-visible change, acceptance status, Evidence pointers, findings, NOT_RUN/limitations, decision options and a separate authentic human decision record.

### Trigger

EXECUTE/VALIDATE finishes, a task candidate needs review, or session handoff requires a reviewable closure package.

### Preconditions

- Exact candidate/stage identity known
- Evidence collected without secrets
- Acceptance criteria available
- Reviewer role independent where required

### Inputs

- Task Brief and Stage Report
- Actual diff/artifacts
- ValidationEnvelope and tests
- Feature acceptance/negative scenarios
- Known findings/limitations
- Human decision channel

### Outputs and observable behavior

- Compact Review & Handoff Package
- Evidence index
- Semantic guard result preventing overclaim
- Reviewer recommendation
- Separate Human Decision Record
- Next-stage handoff after human decision

### Main flow

1. Bind package to exact subject
2. Summarize purpose and user-visible before/after
3. Map acceptance criteria to Evidence/results
4. Expose findings, deviations, NOT_RUN and unknowns
5. Run wording/semantic guard against claim ceiling
6. Present decision options without preselection
7. Human records decision and constraints
8. Generate next handoff without consuming future authorization

### States and transitions

EVIDENCE_COLLECTING → REVIEW_PACKAGE_READY → REVIEWED_RECOMMENDATION → HUMAN_DECISION_REQUIRED → ACCEPTED | NEEDS_CHANGES | REJECTED | DEFERRED.

### Failure modes

- Logs dumped without interpretation
- Evidence omitted or overstated
- Generated ACCEPT stored as human decision
- Review package treated as execution/Git authorization
- Candidate changed after review
- Semantic guard checks keywords only and misses meaning
- Handoff loses open blockers

### Recovery behavior

Invalidate package if subject changes; regenerate summary from preserved Evidence; keep reviewer recommendation separate; human can correct/revoke decision with explicit supersession record.

### Dependencies and shared contracts

- Evidence/result contracts
- Candidate freeze FTR-013
- Human authenticity/drift FTR-021
- Project Memory FTR-016
- Status surface FTR-008

### Safety and human-authority boundaries

- Evidence ≠ approval
- Reviewer recommendation ≠ human decision
- Decision only human-authored/verified
- No auto correction or Git action
- Package contains redacted pointers, not secrets

### Acceptance criteria

- Human understands change without reading raw logs
- Every acceptance claim maps to Evidence or NOT_RUN
- Decision options explicit
- Candidate identity exact
- Open findings survive handoff
- Generated text cannot simulate acceptance

### Required negative scenarios

- Missing Evidence blocks only affected claim
- Stale package rejected
- Agent-written decision rejected
- PASS wording cannot imply release/merge
- Raw remote/token redacted
- Needs-changes does not auto-start correction

### Minimal implementation model candidate

Review compiler over Task Brief, diff and ValidationEnvelope; semantic rules plus optional model-assisted wording review. Human decision storage is separate immutable record/channel.

### Targeted research before implementation

Inspect AOS-FARM.662 Human Review Package Hardening, review/handoff generator, semantic guard and AOS-02 simulated-approval defects. Determine smallest one-document view.

### Non-goals

- Automated approval
- Full audit database
- Correction execution
- Commit/push/merge
## FTR-013 — Diff/Scope Reconciliation, Disposable Validation Subject and Immutable Candidate Freeze

```yaml
feature_id: FTR-013
layer: Development Factory / Validation boundary
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-029` Diff and Scope Reconciliation; `IDEA-030` Disposable Validation Subject; `IDEA-031` Candidate Freeze and Identity  
**Source references:** `CHAT-001`, `REF-A02-001`, `REF-A02-002`, `REF-AF-001`, `SRC-006`

### Problem

Validation can run against moving/live worktree, wrong import source or candidate that changes after Evidence collection. Planned and actual scope can diverge silently.

### Target users

Executor, validator, reviewer and release/merge authorizer.

### Desired outcome

Exact candidate identity and isolated validation subject, plus reconciliation of Task Brief/preview/actual diff and detection of write-after-freeze or stale baseline.

### Trigger

EXECUTE completes, independent validation required, or candidate is prepared for review/Git delivery.

### Preconditions

- Actual mutation stopped
- Task Brief/preview available
- Repository facts inspectable
- Temporary/disposable validation area permitted

### Inputs

- Baseline identity
- Actual worktree/tree/artifacts
- Expected allowed paths/actions
- Evidence inputs
- Validation environment/profile

### Outputs and observable behavior

- Scope reconciliation report
- Frozen candidate identity
- Disposable validation subject
- Provenance verification
- Mutation/drift detection
- Validation-ready handoff

### Main flow

1. Capture actual diff including relevant untracked state
2. Compare planned/allowed/actual
3. Resolve or report deviations
4. Finalize candidate content and supporting Evidence inputs
5. Compute stable identity without self-reference
6. Materialize disposable subject where needed
7. Verify import/runtime provenance
8. Mark freeze point
9. Monitor/recheck no writes after freeze

### States and transitions

MUTABLE_CANDIDATE → RECONCILING → DEVIATION_FOUND | FREEZE_READY → FROZEN → VALIDATING → DRIFT_DETECTED | VALIDATED.

### Failure modes

- Candidate identity provisional/self-referential
- Report/terminal file changes frozen tree
- Wrong package imported
- Untracked file omitted
- Baseline stale
- Validation modifies subject
- Out-of-scope change accepted as incidental

### Recovery behavior

Deviation returns to new authorized correction EXECUTE. Drift invalidates validation/review; refreeze new exact candidate. Disposable subject rebuilt from frozen content, never patched during validation.

### Dependencies and shared contracts

- Task Brief/preview FTR-006/FTR-009
- Scoped execution FTR-010
- Validation FTR-011
- Evidence/review FTR-012

### Safety and human-authority boundaries

- Freeze is technical identity, not approval
- Validation subject read-only
- No hidden correction
- Temporary artifacts disposable and outside canonical state

### Acceptance criteria

- Actual diff completely classified
- Frozen identity reproducible
- No self-reference
- Validation imports exact subject
- Write-after-freeze detected
- Report binds baseline and candidate

### Required negative scenarios

- Change one byte after freeze invalidates result
- Create untracked in-scope file and ensure captured
- Import live checkout while validating package detected
- Self-hash cycle rejected
- Validator side effect detected

### Minimal implementation model candidate

Git tree/content-manifest adapter and disposable copy/install harness. Use simplest reproducible identity; cryptographic package ceremony only where it prevents a concrete stale/identity risk.

### Targeted research before implementation

Inspect candidate freeze tasks 680/683, disposable subject validations and stale baseline incidents. Identify minimal identity model for non-Git artifacts.

### Non-goals

- Approval
- Permanent artifact registry
- Automatic correction
- Release signing in MVP
## FTR-014 — Recovery, Resume, Rollback, Denied-Action Log and Session Handoff

```yaml
feature_id: FTR-014
layer: Product Runtime / Development Factory boundary
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-032` Recovery, Resume and Rollback; `IDEA-034` Denied Action Log and State Recovery View; `IDEA-036` Session Handoff  
**Source references:** `CHAT-001`, `CHAT-010`, `CHAT-012`, `CURRENT-INSTRUCTIONS`, `REF-A02-002`, `REF-AG-001`, `SRC-006`

### Problem

Interrupted or failed work loses actual state and next step; agents may auto-retry or rollback destructively. Denied actions and open findings disappear between sessions.

### Target users

Non-programmer owner, implementation agent, recovery operator and next-session agent.

### Desired outcome

A fail-closed recovery and resume package that preserves actual candidate/journal, denied actions, open findings, authorization state and one safe next action; rollback remains separately authorized.

### Trigger

Execution interruption/failure, validation finding, denied operation, session/token/environment change or explicit resume request.

### Preconditions

- Available facts captured without further mutation
- Failure stage/subject identifiable
- No automatic retry in progress
- Durable human decisions preserved

### Inputs

- Operation journal and Stage Report
- Repository/worktree/current facts
- Candidate/baseline identity
- Denied-action records
- Validation findings
- Human decisions/permissions

### Outputs and observable behavior

- Recovery classification
- Resume/Handoff package
- Actual vs intended reconciliation
- Candidate options: resume, correction, rollback, abandon
- One next required action and explicit stop

### Main flow

1. Stop active writes/workers
2. Capture actual state and journal
3. Classify no-write/partial-write/post-execution/validation finding
4. Record denied actions and reasons
5. Recheck repository identity
6. Build compact handoff
7. Present recovery options and consequences
8. Human authorizes separate correction/resume/rollback Task Brief
9. New stage starts only after fresh preflight

### States and transitions

INTERRUPTED → FACTS_CAPTURED → RECOVERY_REVIEW → RESUME_READY | CORRECTION_REQUIRED | ROLLBACK_DECISION_REQUIRED | ABANDONED. Validation finding routes to correction, not inline fix.

### Failure modes

- Auto-retry repeats destructive action
- Rollback target unknown
- Handoff claims completion
- Denied action log contains secret/raw command output
- Old authorization carried forward
- Candidate facts stale after session switch

### Recovery behavior

This feature is the recovery mechanism: preserve immutable facts, make unknowns explicit, avoid mutation until human selection, and rebind all mutable facts/permissions before next stage.

### Dependencies and shared contracts

- Execution journal FTR-010
- Project Memory FTR-016
- Candidate identity FTR-013
- Status surface FTR-008
- Permission taxonomy FTR-019

### Safety and human-authority boundaries

- No automatic retry/rollback
- Rollback destructive and separately authorized
- Handoff does not authorize next stage
- Denied log redacted
- Historical status clearly marked

### Acceptance criteria

- New agent resumes without full chat replay
- Partial writes accurately classified
- Open blockers/NOT_RUN retained
- Stale facts rechecked
- Exactly one next action
- No mutation during recovery review

### Required negative scenarios

- Copied old authorization rejected
- Changed HEAD detected on resume
- Missing journal produces UNKNOWN/BLOCKED, not invented state
- Rollback without target/backup blocked
- Denied action never becomes allowed through retry

### Minimal implementation model candidate

Durable stage journal + compact resume record compiled from repository facts and existing artifacts. First version can be Markdown/JSON and explicit commands; no autonomous recovery engine.

### Targeted research before implementation

Inspect AOS-FARM recovery programs, 683.15 controlled suspension, lifecycle handoff and denied-action concepts. Retain facts, discard elaborate chains that created new blockers.

### Non-goals

- Self-healing autonomous system
- Automatic rollback
- Cross-project scheduler
- Git history rewrite
## FTR-015 — Git Lifecycle Closure, Remote State, Commit/Push/Merge/Release Boundaries and Deterministic Merge Authorization

```yaml
feature_id: FTR-015
layer: Development Factory / Delivery boundary
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-033` Git Lifecycle Closure  
**Source references:** `CURRENT-INSTRUCTIONS`, `REF-AF-001`, `REF-AF-002`, `SRC-006`

### Problem

A technically valid local candidate is often described as “done” while commit, remote push, review, merge or release remain separate and mutable. Stale remote/branch state can invalidate authorization.

### Target users

Human maintainer/reviewer, implementation agent and release operator.

### Desired outcome

A closure package showing local candidate, validation, human acceptance, remote/PR/protection state and exactly which Git operation—if any—can be separately authorized next.

### Trigger

Human-accepted or review-ready candidate approaches commit, push, merge or release.

### Preconditions

- Exact candidate frozen/validated as required
- Git repository/branch/remote identity verified
- No secrets exposed
- Operation-specific human decision available or requested

### Inputs

- Repository/branch/HEAD/candidate
- Working tree and staged state
- Review/human decision
- Remote/PR/protection/review checks where network authorized
- Requested Git operation

### Outputs and observable behavior

- Closure status matrix
- Operation-specific authorization request/record
- Safe command/action plan
- Post-operation verification result
- One next boundary

### Main flow

1. Verify local identity/cleanliness
2. Determine accepted candidate vs staged/commit state
3. For remote operations obtain authorized read-only remote/PR facts
4. Evaluate operation-specific preconditions
5. Present exact operation and resulting state
6. Human authorizes one operation
7. Perform only that operation
8. Reverify repository/remote facts
9. Report and stop

### States and transitions

VALIDATED_UNACCEPTED → HUMAN_ACCEPTED_UNCOMMITTED → COMMITTED_UNPUSHED → PUSHED_UNMERGED → MERGED_UNRELEASED → RELEASED. Each transition separately authorized.

### Failure modes

- Commit authorization reused for push
- Merge readiness inferred from CI only
- Remote URL/token leaked
- Branch/HEAD changes after review
- Wrong merge method
- Fast-forward assumption stale
- Release implied by merge

### Recovery behavior

Failed/no-op operation reports actual local/remote state and stops. Stale candidate or remote facts invalidate authorization; new preflight/decision required. No destructive Git recovery without explicit scope.

### Dependencies and shared contracts

- Candidate freeze FTR-013
- Review/Decision FTR-012
- Preflight FTR-009
- Status/closure surface FTR-008
- Permissions FTR-019

### Safety and human-authority boundaries

- Edit ≠ Commit ≠ Push ≠ Merge ≠ Release
- Network read/write separately permissioned
- Human authorizes exact operation/method/subject
- CI/Evidence never approval

### Acceptance criteria

- Each boundary visible to non-programmer
- Stale local/remote facts detected
- No operation beyond authorization
- Post-operation identity verified
- Merge package distinguishes required/optional checks
- One next action and stop

### Required negative scenarios

- Accepted candidate changed before commit rejected
- Commit record cannot authorize push
- CI PASS without required review cannot authorize merge
- Raw remote secret absent
- Merge cannot auto-release

### Minimal implementation model candidate

Git adapter plus closure state compiler and operation-specific commands. Begin with local commit boundary; push/PR/merge/release adapters only after network/provider contracts and permissions.

### Targeted research before implementation

Inspect merge/push boundary guard, deterministic merge authorization package, fast-forward gate and AOS-FARM.610 lifecycle closure UX. Separate useful state model from heavy merge machinery.

### Non-goals

- Automatic merge/release
- Git hosting platform replacement
- Branch protection configuration without separate authorization
- History rewrite
## FTR-016 — Project Memory, Session Continuity, Context Priority and Task-scoped Context Pack

```yaml
feature_id: FTR-016
layer: Product Runtime / Development Factory boundary
disposition: CANDIDATE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-035` Project Memory; `IDEA-036` Session Handoff; `IDEA-037` Context Priority Rules; `IDEA-038` Task-scoped Context Pack  
**Source references:** `CHAT-003`, `CHAT-006`, `CHAT-010`, `CHAT-012`, `CURRENT-INSTRUCTIONS`, `REF-AG-001`, `SRC-005`, `SRC-006`

### Problem

Project context is distributed across repository, chats, Task Briefs, reports, decisions and agent sessions. New agent either lacks critical facts or loads everything and is confused by stale/low-authority material.

### Target users

Product owner, any resuming agent, reviewer and maintainer.

### Desired outcome

A minimal durable Project Memory and task-scoped Context Pack that preserve accepted decisions, current verified state, open findings and one next action while enforcing source priority and freshness.

### Trigger

Session start/resume, model/agent handoff, new Task Brief, review or context-window pressure.

### Preconditions

- Project identity known
- Source precedence defined
- Durable artifacts available
- Sensitive content and access scope classified

### Inputs

- Canonical/DRAFT documents by fact class
- Repository facts
- Task Brief/stage reports
- Human decisions
- Reference findings and lessons
- User preferences/constraints relevant to task

### Outputs and observable behavior

- Current-state summary with freshness
- Resume record
- Task-scoped Context Pack
- Excluded/stale/conflicting-source list
- Context provenance and limitations
- One next action

### Main flow

1. Identify task/feature and required fact classes
2. Load highest-authority/current sources first
3. Verify mutable repository facts
4. Include only relevant contracts/lessons/findings
5. Mark stale/reference/proposal content
6. Detect conflicts and missing context
7. Compile compact pack and token/size summary
8. On resume, recheck identities before action

### States and transitions

NO_MEMORY → ORIENTED → CONTEXT_COMPILED → READY | STALE | CONFLICTED | INCOMPLETE. Derived packs are invalidated by source/subject changes.

### Failure modes

- Chat memory treated as repository fact
- Old accepted decision applied to new subject
- Pack too large and hides key scope
- RAG/index becomes competing SoT
- Sensitive data included without permission
- Handoff omits NOT_RUN/blocker/authorization state

### Recovery behavior

Regenerate from source owners, discard stale derived pack, disclose missing context and continue only with safe read-only analysis or block affected mutation. Never patch facts directly in cache.

### Dependencies and shared contracts

- Source/authority model
- Project state contract
- Task Brief FTR-006
- Recovery FTR-014
- Optional RAG FTR-017
- Routing FTR-018

### Safety and human-authority boundaries

- Derived and rebuildable
- No authority promotion
- No execution authorization transfer
- No cross-repository read without permission
- Minimal sufficient context, not full archive

### Acceptance criteria

- New agent identifies project/task/stage correctly
- Accepted decisions and open findings preserved
- Mutable facts freshness visible
- Pack excludes irrelevant legacy noise
- Conflicts/unknowns explicit
- One next action consistent with source state

### Required negative scenarios

- Changed HEAD invalidates old pack
- Lower-authority chat cannot override canonical fact
- Missing source not silently synthesized
- Sensitive file excluded/redacted
- Old authorization not carried forward

### Minimal implementation model candidate

Repository-first Markdown/JSON current-state and handoff records with deterministic context compiler. Use explicit source adapters and recency/authority rules before adding database or embeddings.

### Targeted research before implementation

Inspect Development Scaffolding ideas: Context Packager, Session Gatekeeper, Result Ingestor, Drift Detector, plus actual handoff pain. Determine minimum durable record and owner.

### Non-goals

- Permanent memory of all conversations
- Automatic task execution
- Independent knowledge database as SoT
- Unbounded cross-project context
## FTR-017 — RAG-light Context Index and Search

```yaml
feature_id: FTR-017
layer: Supporting runtime
disposition: DEFERRED_UNTIL_MEASURED
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-039` RAG-light Context Index  
**Source references:** `CHAT-003`, `SRC-004`, `SRC-006`

### Problem

As documentation and reference findings grow, keyword navigation may become slow; agents may miss relevant lessons/contracts. A vector/RAG layer, however, can add dependencies, stale results and authority confusion.

### Target users

Agent preparing a task/context pack, maintainer searching project knowledge, reviewer locating provenance.

### Desired outcome

A rebuildable search index that retrieves candidate context with source, authority, freshness and confidence, while never replacing original artifacts or deciding scope.

### Trigger

Measured failures of direct navigation/keyword search in a sufficiently large corpus.

### Preconditions

- Stable document IDs/source ownership
- Search use cases and metrics defined
- Corpus privacy/classification known
- Index rebuild and invalidation strategy available

### Inputs

- Approved document/reference corpus
- Metadata: fact class, authority, status, feature IDs, timestamps/digests
- Search query/task context

### Outputs and observable behavior

- Ranked source excerpts/locators
- Authority/freshness labels
- Missing/low-confidence notice
- Index health/invalidation status

### Main flow

1. Ingest only allowed sources
2. Chunk with stable source locators
3. Build lexical or lightweight semantic index
4. Query and rank with authority/filter constraints
5. Return citations, not synthesized facts
6. Context compiler/human selects relevant sources
7. Rebuild on source change

### States and transitions

NOT_CONFIGURED → BUILDING → READY → STALE → REBUILD_REQUIRED | DEGRADED. Query result remains proposal/reference.

### Failure modes

- Index treated as Source of Truth
- Stale chunk returned after source update
- Cross-project/private data leakage
- Semantic similarity overrides authority
- Vector dependency increases complexity before value
- Retrieval result silently used as approval

### Recovery behavior

Mark stale/degraded, fall back to direct document navigation or keyword search, rebuild from owned sources, and disclose missing coverage. No project action depends solely on index.

### Dependencies and shared contracts

- Project Memory FTR-016
- Source IDs and metadata
- Permission/privacy FTR-019
- Feature/contract terminology

### Safety and human-authority boundaries

- Derived/rebuildable
- Read-only
- No authority or product decision
- No external embedding provider without explicit privacy/network decision
- Can be removed without core breakage

### Acceptance criteria

- Retrieval improves measured context recall/time
- Every result links to exact source
- Authority/freshness shown
- Source change invalidates/rebuilds index
- Keyword fallback works
- No hidden external call

### Required negative scenarios

- Deleted/superseded source not returned as active
- Low-authority reference cannot outrank required canonical fact solely by similarity
- Private corpus not indexed across boundary
- Index absence does not block core workflow

### Minimal implementation model candidate

Start with SQLite FTS or deterministic lexical index only after measured need; semantic embeddings are later option. Index metadata stores source digests and feature/fact-class filters.

### Targeted research before implementation

Review historical RAG-light proposals and real search failures after seven-document consolidation. Benchmark direct headings/grep first.

### Non-goals

- Chatbot knowledge authority
- Universal enterprise search
- Mandatory vector database
- Automatic decision making
## FTR-018 — Advisory Model Routing, Explicit Subagent Roles, Routing Audit and Provider Evaluation

```yaml
feature_id: FTR-018
layer: Development Factory
disposition: DEFERRED_UNTIL_MEASURED
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-040` Advisory Model Routing; `IDEA-041` Explicit Subagent Routing, Routing Audit and Provider Evaluation  
**Source references:** `CHAT-010`, `SRC-005`, `SRC-006`

### Problem

Tasks differ in reasoning, coding, review and documentation needs, but model/agent selection may be ad hoc. Automatic routing can leak sensitive context, escalate privileges/cost or hide fallback.

### Target users

Task owner, orchestrating agent, architect, executor, reviewer and documentation agent.

### Desired outcome

An auditable routing recommendation/record that separates roles, selects model/provider according to measured task needs and privacy constraints, and keeps human control over explicit subagent invocation.

### Trigger

Task requires role specialization or there is evidence that one model profile is insufficient/costly.

### Preconditions

- Task Brief and context boundary known
- Available agents/models/providers enumerated
- Privacy/network/permission rules defined
- No automatic privilege escalation

### Inputs

- Task class/stage/risk/complexity
- Required capabilities and context size
- Provider/model characteristics
- Benchmark/quality/cost/latency data
- Sensitive-domain flags and permissions

### Outputs and observable behavior

- Advisory routing recommendation
- Explicit role assignments
- Minimal context pack per role
- Routing Record with selected/fallback model and rationale
- Outcome/quality metrics for later evaluation

### Main flow

1. Classify task and stage
2. Identify needed roles; avoid unnecessary parallelism
3. Filter providers/models by privacy/permissions/capability
4. Rank using measured criteria
5. Present recommendation or select only under accepted policy
6. Generate role-specific context
7. Record actual model/fallback
8. Compare outcome and update evaluation data

### States and transitions

UNROUTED → ADVISORY_READY → HUMAN_SELECTED | POLICY_SELECTED → RUNNING_ROLE → RESULT_RECORDED | FALLBACK_REQUIRED | BLOCKED_PROVIDER.

### Failure modes

- Role name exists but not registered
- Model fallback hidden
- Reviewer shares mutation permissions
- Parallel agents create conflicting writes
- Provider receives unapproved medical/private data
- Routing based on marketing rather than benchmark
- Routing output treated as authority

### Recovery behavior

Stop affected role, record actual model and context sent, reroute only with explicit permission and fresh context. No automatic switch that increases network, sandbox, scope or authority.

### Dependencies and shared contracts

- Task Brief FTR-006
- Context Pack FTR-016
- Permission/privacy FTR-019
- Model benchmark records
- One-run/one-stage workflow

### Safety and human-authority boundaries

- Advisory first
- Explicit human or accepted policy selection
- No Risk Profile/approval assignment
- No parallel writes
- Provider/privacy boundary enforced
- Agent output remains role-scoped

### Acceptance criteria

- Routing rationale and actual model visible
- Role permissions least-privilege
- Context minimized
- Fallback disclosed
- Quality/cost/latency measurable
- Removing router does not break manual workflow

### Required negative scenarios

- Unregistered role rejected
- Sensitive task cannot route to disallowed provider
- Fallback cannot gain write/network permission
- Two write agents prohibited
- Unknown model capability remains UNKNOWN

### Minimal implementation model candidate

Static routing rules and role config first; optional scorer after benchmark data. Routing record is simple structured artifact. Runtime auto-routing deferred.

### Targeted research before implementation

Inspect Model Routing source, Codex custom-agent registration issues and actual task outcomes. Pilot architect/executor/reviewer/docs roles on bounded tasks before automation.

### Non-goals

- Autonomous multi-agent swarm
- Provider procurement
- Hidden model switching
- Central Control Plane
## FTR-019 — Action Trust Boundary, Permission-State Classifier, External-Content Boundary and Path/Command/Network Allowlists

```yaml
feature_id: FTR-019
layer: Minimal Safety Floor
disposition: CANDIDATE_CORE_SAFETY
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-050` Action Trust Boundary; `IDEA-051` Permission State Classifier and Error Taxonomy; `IDEA-052` Prompt Injection Boundary for External Content; `IDEA-053` Protected Path, Write and Command Allowlists; `IDEA-054` Network, Sandbox and Git Permission Gate  
**Source references:** `CURRENT-INSTRUCTIONS`, `REF-A02-001`, `SRC-004`, `SRC-006`, `SRC-007`

### Problem

An agent can mistake untrusted content for instruction, conflate read/write/network/Git permissions, or use ambiguous errors and path/command rules. Convenience defaults can silently grant authority.

### Target users

All agents, task owner, security reviewer and runtime adapters.

### Desired outcome

One consistent classifier that maps requested action and context to `ALLOWED`, `HUMAN_AUTHORIZATION_REQUIRED`, `BLOCKED_POLICY`, `BLOCKED_UNKNOWN` or `NOT_APPLICABLE`, with exact reason and safe next action.

### Trigger

Any repository read/write, command, network/provider call, Git operation, protected path access or instruction sourced from external content.

### Preconditions

- Requested action structured
- Task/feature scope available
- Current permissions/policy/unknowns known
- Paths/commands normalized before classification

### Inputs

- Actor/role
- Action type and target
- Source of instruction
- Scope/allowlists
- Sandbox/network/Git permissions
- Risk/protected classification
- Sensitive-domain flags

### Outputs and observable behavior

- Permission state and reason code
- Affected operation/claim
- Required human authorization or policy decision
- Redacted denied-action record
- No-op/blocked terminal result where applicable

### Main flow

1. Separate system/human/task instructions from repository/web content
2. Normalize target/path/command
3. Classify operation and privilege
4. Apply exact allow/deny/unknown policy
5. Check sensitive/provider/network/Git boundaries
6. Return state and rationale
7. Log denied attempt safely
8. Executor proceeds only on ALLOWED or exact human authorization

### States and transitions

REQUESTED → CLASSIFIED → ALLOWED | HUMAN_REQUIRED | BLOCKED_POLICY | BLOCKED_UNKNOWN | NOT_APPLICABLE. New facts/decision cause reclassification, not silent upgrade.

### Failure modes

- Repository prompt injection changes scope
- Generic error hides permission cause
- Path allowlist permits traversal/symlink escape
- Network call implicit
- Git permission reused across operations
- Unknown treated allowed
- Denied log leaks secret

### Recovery behavior

No unauthorized mutation. Human can supply exact decision/permission, task can narrow scope, or action remains blocked. Reclassify against fresh facts; denied state never auto-retries.

### Dependencies and shared contracts

- Core authority/source model
- Task Brief FTR-006
- Preflight FTR-009
- Routing/provider policy FTR-018
- Runtime enforcement optional FTR-020

### Safety and human-authority boundaries

- Classifier does not assign Risk Profile or approval
- Defaults fail closed only for affected authority-bearing action
- External content is data
- Allowlists exact and normalized
- Remote secrets never exposed

### Acceptance criteria

- Same action receives consistent state across CLI/executor
- Reason and next action understandable
- Informational unknown does not globally block read-only work
- Protected/destructive/network/Git boundaries enforced
- No authority-bearing default true

### Required negative scenarios

- Prompt injection in README ignored as instruction
- `..`, absolute path, symlink escape rejected
- Unapproved network/provider call blocked
- Commit permission cannot allow push
- Unknown policy returns BLOCKED_UNKNOWN
- Secret-bearing command/output redacted

### Minimal implementation model candidate

Pure policy engine with typed action request and reason-code taxonomy, used first in advisory/preflight mode. Enforcement hooks can be added later without changing contract.

### Targeted research before implementation

Inspect harness Action Trust table, AOS-02 error/status handling and actual prompt-injection/remote-leak risks. Keep policy small and testable.

### Non-goals

- Full OS sandbox
- Automatic risk scoring/approval
- Enterprise IAM
- Content moderation system
## FTR-020 — Runtime Enforcement, Isolated Execution Environment and Progressive Governance Modes

```yaml
feature_id: FTR-020
layer: Governance / Runtime Enforcement
disposition: DEFERRED
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-055` Runtime Enforcement Layer; `IDEA-056` Isolated Execution Environment; `IDEA-057` Progressive Governance Modes; `IDEA-058` Advanced Governance Gates  
**Source references:** `CHAT-002`, `CURRENT-INSTRUCTIONS`, `SRC-004`, `SRC-006`

### Problem

Advisory rules can be ignored by agents/scripts, but early enforcement/sandbox/Governance can dominate product development and create self-hosting control complexity.

### Target users

Maintainer, security reviewer, execution agent and regulated/high-risk project owner.

### Desired outcome

A progressive, disableable/replaceable enforcement layer admitted only after stable contracts and observed incidents, with clear modes, least privilege and isolation of untrusted operations.

### Trigger

Evidence shows advisory controls insufficient for a concrete repeated risk, or regulated/high-risk environment requires technical enforcement.

### Preconditions

- Product Runtime useful and stable
- At least two successful manual cycles
- Permission/action contracts accepted
- Threat/incident model and bypass/removal path defined
- Human architecture/dependency decision

### Inputs

- Structured action requests
- Accepted policies and Risk Profile
- Sandbox/filesystem/network/Git capabilities
- Task authorization and subject identity
- Audit/incident data

### Outputs and observable behavior

- Enforced allow/deny decision
- Isolated execution result
- Policy/audit record
- Mode status and bypass/escalation request
- No-op when module disabled under allowed profile

### Main flow

1. Select governance mode (observe/advisory/enforced) under human policy
2. Materialize least-privilege environment
3. Validate action/authorization
4. Execute through enforcement boundary
5. Monitor forbidden side effects
6. Terminate/isolate on violation
7. Record incident and result
8. Return to normal workflow without automatic approval

### States and transitions

DISABLED → OBSERVE → ADVISORY → ENFORCED. Action: REQUESTED → ALLOWED_EXECUTED | DENIED | ISOLATED_FAILURE | POLICY_UNKNOWN.

### Failure modes

- Enforcement built before contract
- Sandbox gives false security
- Policy blocks routine work globally
- Governance module becomes mandatory SoT
- Bypass hidden
- Enforcement self-validates
- Platform-specific dependency locks architecture

### Recovery behavior

Fail closed for affected high-risk action; allow manual/advisory fallback only if policy explicitly permits. Disable/rollback module without corrupting project state. Incidents feed FTR-025.

### Dependencies and shared contracts

- Permission contract FTR-019
- Scoped executor FTR-010
- Architecture decision FTR-005
- Observability/incident memory FTR-025
- Project Memory FTR-016

### Safety and human-authority boundaries

- Human controls admission/mode/bypass
- No product-scope or approval authority
- Replaceable optional module
- No implicit network/package install
- Regulated domains require separate architecture

### Acceptance criteria

- Concrete risk reduction demonstrated
- Manual workflow remains possible where policy allows
- Mode/status visible
- Forbidden action technically blocked in ENFORCED mode
- Removal/fallback tested
- No competing Source of Truth

### Required negative scenarios

- Disabled module cannot silently enforce
- Observe mode cannot mutate outcome
- Bypass requires exact human decision
- Sandbox escape/side-effect tests
- Policy unknown cannot become allow
- Enforcement failure cannot report task PASS

### Minimal implementation model candidate

Adapter around accepted action contract, initially observe/advisory. OS/container sandbox and strong enforcement are separate pluggable backends after threat-model decision.

### Targeted research before implementation

Review Runtime Trust Architecture/OBSERVE-ENFORCED concepts and harness guardrails. Identify actual incidents before selecting mechanism.

### Non-goals

- First MVP foundation
- Universal secure sandbox
- Autonomous Governance service
- Automatic Risk Profile assignment
## FTR-021 — Registry/Drift Detection, Source-of-Truth Guard and Human-Decision Authenticity

```yaml
feature_id: FTR-021
layer: Development Factory / Governance support
disposition: DEFERRED_AFTER_MANUAL_FLOW
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-059` Registry / Drift, Source-of-Truth Guard and Human Decision Authenticity  
**Source references:** `REF-A02-001`, `REF-A02-002`, `SRC-004`

### Problem

Docs, schemas, runtime, generated views and decisions can diverge. A registry can detect drift but may silently lose data or become a second Source of Truth. Human decision records may be unauthentic or stale.

### Target users

Maintainer, reviewer, release operator and safety auditor.

### Desired outcome

Rebuildable consistency checks and authenticity gates that identify owner for each fact class, detect schema/docs/runtime/index drift and ensure authority-bearing decisions are human-authored and bound to exact subject.

### Trigger

Stable repeated artifacts exist and drift incidents are observed; an authority-bearing action needs decision verification.

### Preconditions

- One-owner/source model accepted
- Stable IDs/contracts
- Registry is derived/rebuildable
- Human decision channel/authenticity model selected

### Inputs

- Canonical/DRAFT docs
- Schemas/runtime adapters/tests
- Generated indexes/dashboards
- Task/candidate/decision identities
- Registry snapshots and change events

### Outputs and observable behavior

- Drift report by fact class
- Missing/duplicate/field-loss findings
- Rebuilt index/registry
- Decision authenticity result
- Blocked authority-bearing action where subject/decision mismatch

### Main flow

1. Inventory owners and derived consumers
2. Rebuild expected registry from sources
3. Round-trip compare all fields/items
4. Compare docs/schema/runtime/test vocabulary
5. Validate decision provenance/subject/revision/supersession
6. Classify drift severity/affected operation
7. Report and stop; correction separate

### States and transitions

UNCONFIGURED → BASELINED → CONSISTENT | DRIFT_DETECTED | AUTHENTICITY_UNKNOWN | DECISION_INVALID | REBUILD_REQUIRED.

### Failure modes

- Registry silently omits records/fields
- Generated view overrides source
- Semantic similarity substitutes fact-class coverage
- Old decision reused
- Agent-signed decision accepted
- Drift checker mutates target
- Every difference treated P0 blocker

### Recovery behavior

Rebuild derived data, preserve source artifacts, create bounded correction/decision package. Block only affected authority operation; do not auto-promote or rewrite canonical docs.

### Dependencies and shared contracts

- Source model
- Strict loader/internal tooling FTR-030
- Project Memory FTR-016
- Review/Decision FTR-012
- Feature/contract IDs

### Safety and human-authority boundaries

- Registry derived, not authority
- Only human can authenticate/accept project decision
- Read-only audit stage
- No automatic correction/canonicalization

### Acceptance criteria

- Round-trip has no silent loss
- Every fact class has one owner
- Schema/runtime/docs mismatches surfaced
- Stale/agent-generated decision rejected
- Affected scope clear
- Registry deletable/rebuildable

### Required negative scenarios

- Empty mapping/unknown status rejected
- Dropped field detected
- Canonical document wrong fact class cannot override
- Copied decision bound to old candidate rejected
- Audit produces zero target mutation

### Minimal implementation model candidate

Deterministic index builders and contract-diff checks; authenticity adapter starts with direct human submission/exact digest and explicit supersession, not complex cryptographic identity unless required.

### Targeted research before implementation

Inspect AOS-FARM Registry/Drift proposals, Third Pass silent-data-loss audit and AOS-02 decision simulation. Measure need before centralizing state.

### Non-goals

- Central Control Plane
- Automatic canonical promotion
- Enterprise identity platform
- Global blocker on all drift
## FTR-022 — Solution/Pattern Library, Fit Matrix and Reusable UX/Engineering Patterns

```yaml
feature_id: FTR-022
layer: Knowledge support
disposition: CANDIDATE_SUPPORT
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-013` Pattern / Solution Library and Fit Matrix  
**Source references:** `CHAT-003`, `REF-A02-002`, `SRC-009`

### Problem

Teams repeatedly solve similar UX, validation, recovery and architecture problems, but raw code/legacy references are hard to reuse and can carry wrong assumptions.

### Target users

Product designer, architect, coding agent, reviewer and maintainer.

### Desired outcome

A curated library of problem→context→solution→trade-off→failure→test patterns with fit criteria, provenance, maturity and explicit non-authority.

### Trigger

A repeated solution appears across tasks or a new feature needs design options.

### Preconditions

- Pattern observed or researched
- Problem/context and evidence distinguishable
- No automatic architecture authority
- Owner/review status defined

### Inputs

- Lessons/incidents
- Accepted feature/architecture outcomes
- Reference findings
- Tests and failures
- Usage feedback

### Outputs and observable behavior

- Pattern record
- Fit/anti-fit matrix
- Example and counterexample
- Required contracts/tests
- Maturity/provenance
- Candidate recommendation for selected feature

### Main flow

1. Identify repeated problem and contexts
2. Extract invariant behavior, not code topology
3. Record successful/failed variants
4. Define fit and anti-fit conditions
5. Link tests/lessons/evidence
6. Review pattern maturity
7. Use as option in feature/architecture work
8. Update after real outcomes

### States and transitions

IDEA → OBSERVED → REVIEWED_CANDIDATE → VALIDATED_PATTERN | REJECTED | SUPERSEDED. Even validated pattern is not automatic decision.

### Failure modes

- Pattern freezes legacy design
- One success generalized universally
- Library becomes huge parking lot
- Recommendation treated as architecture approval
- Examples stale
- Medical/domain pattern applied without compliance review

### Recovery behavior

Mark superseded/limited, preserve historical rationale, remove from default recommendations, and return feature to option comparison.

### Dependencies and shared contracts

- Lessons FTR-025/04_Lessons.md
- Architecture support FTR-005
- Source/provenance FTR-005 reference document
- Optional search FTR-017

### Safety and human-authority boundaries

- Advisory only
- No code copy by default
- No product scope or dependency authority
- Domain/security constraints explicit

### Acceptance criteria

- Pattern states problem/context/trade-offs/failures/tests
- Fit matrix prevents blind reuse
- Provenance and maturity visible
- At least one counterexample/non-fit
- Can be removed without runtime impact

### Required negative scenarios

- Single unverified idea cannot be “validated”
- Legacy folder structure alone not a pattern
- Pattern recommendation cannot set ADR decision
- Stale source status exposed

### Minimal implementation model candidate

Markdown records with stable IDs/tags and optional lightweight index. Curation/review more important than automation.

### Targeted research before implementation

Inspect architecture pattern library/fit matrix proposals and recurring safe-path/onboarding/review patterns from chats. Start with 5–10 high-value patterns.

### Non-goals

- Code package registry
- Automatic architecture selection
- Mass import of legacy snippets
- Marketplace
## FTR-023 — Advisory CI, CI Smoke, Safety Regression Fixtures and Quality Gates

```yaml
feature_id: FTR-023
layer: Development Factory
disposition: CANDIDATE_AFTER_BASELINE
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-060` Advisory CI and CI Smoke; `IDEA-078` Schema / Runtime Drift, Module Boundaries, Negative Fixtures, Bootstrap and Quality Tooling  
**Source references:** `CHAT-013`, `REF-A02-001`, `REF-AF-001`, `REF-AG-001`, `SRC-007`

### Problem

Historical failures recur because tests focus on happy path; CI success can still miss authority, scope, stale-state and packaging defects. Heavy quality tooling can also become false readiness.

### Target users

Developer, validator, maintainer and release reviewer.

### Desired outcome

A staged test/CI profile with fast smoke, contract/negative fixtures and explicit NOT_RUN/optional quality checks, producing technical Evidence only.

### Trigger

A stable executable baseline or feature candidate has repeatable checks; first vertical slice approaches validation/release.

### Preconditions

- Test subject/environment defined
- Accepted contracts/acceptance scenarios available
- Required vs optional checks declared
- CI/network/dependency policy decided

### Inputs

- Code/package/candidate
- Test and fixture catalog
- Environment/dependency lock/identity
- Feature acceptance and historical regression cases

### Outputs and observable behavior

- ValidationEnvelope per profile
- Smoke/full/negative check results
- Coverage/security/dependency findings with limitations
- Artifact provenance
- No approval or merge authorization

### Main flow

1. Run syntax/import/bootstrap smoke
2. Run contract and high-risk negative fixtures
3. Run feature unit/integration/E2E profile
4. Optionally run coverage/security/dependency checks
5. Aggregate with required/optional semantics
6. Publish redacted Evidence and subject identity
7. Reviewer interprets; human controls delivery

### States and transitions

NOT_CONFIGURED → SMOKE_READY → BASELINE_GREEN | FAILING → FULL_PROFILE_READY → RESULT_WITH_NOT_RUN. CI status separate from human/Git state.

### Failure modes

- CI PASS treated merge approval
- Coverage threshold freezes bad design
- Scanner unavailable silently skipped
- Tests import wrong checkout
- Negative fixtures missing
- Optional dependency explosion
- Flaky test causes blind retry

### Recovery behavior

Keep failure/NOT_RUN visible, fix in separate EXECUTE, validate exact candidate again. Disable flaky/optional check only through explicit profile change with limitation.

### Dependencies and shared contracts

- Validation FTR-011
- Candidate subject FTR-013
- Evidence/review FTR-012
- Contracts/feature dossiers
- Environment identity

### Safety and human-authority boundaries

- CI technical only
- No automatic merge/release
- No package install/network unless authorized
- Quality metric not product acceptance
- Advisory first

### Acceptance criteria

- Fast smoke catches bootstrap/import/schema wiring
- Historical safety failures have negative fixtures
- Required NOT_RUN prevents green
- Exact subject/interpreter recorded
- No CI-created repository drift
- Human sees limitations

### Required negative scenarios

- Invalid status/empty mapping/bool-int/session mismatch
- Unauthorized path/command/action
- Read-only side effect
- Stale baseline/freeze mutation
- Generated human decision
- Installer overwrite/partial recovery
- Raw secret output

### Minimal implementation model candidate

Small local test profiles mirrored in CI. Use existing test framework/toolchain selected by architecture; avoid new quality dependencies until justified.

### Targeted research before implementation

Inspect Safety Regression Fixtures, CI smoke in Third Pass, AOS-02 schema/module tests and doctor hygiene. Curate highest-risk fixtures first.

### Non-goals

- Automatic acceptance
- Perfect coverage
- All scanners from day one
- Release orchestration
## FTR-024 — Release Checklist, Promotion Package, Version/Changelog/Tag and Rollback Assistant

```yaml
feature_id: FTR-024
layer: Later lifecycle
disposition: DEFERRED_UNTIL_RELEASE_TARGET
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-061` Release Checklist and Promotion Package; `IDEA-062` Version, Changelog, Tag and Rollback Assistant  
**Source references:** `REF-A02-002`, `REF-AF-001`, `REF-AF-002`, `SRC-008`

### Problem

Merge can be confused with release; version, changelog, tag, deployment and rollback facts may drift. Premature release machinery adds complexity before a deployable product exists.

### Target users

Release owner, maintainer, reviewer and product owner.

### Desired outcome

A decision-ready release package that binds accepted merged artifacts, version/change summary, required checks, deployment target and rollback plan; each release action remains separately human-authorized.

### Trigger

A real Product Runtime candidate has a defined distribution/deployment target and is ready for release consideration.

### Preconditions

- Human-accepted product/candidate
- Merged/source artifact identity known
- Release target and compatibility policy defined
- Required validation/security/dependency checks declared
- Rollback mechanism tested

### Inputs

- Accepted/merged commit or package
- Release notes/changelog candidates
- Version policy
- Validation/security/dependency Evidence
- Deployment target and migration/rollback plan

### Outputs and observable behavior

- Release checklist and promotion package
- Version/tag/changelog proposal
- Compatibility/migration notice
- Rollback plan
- Release authorization request
- Post-release verification plan

### Main flow

1. Verify source artifact and branch/tag state
2. Compile user-visible changes and breaking risks
3. Run/collect required release checks
4. Confirm version and migration/rollback
5. Present exact release operation/target
6. Human authorizes release
7. Perform only authorized publish/deploy/tag action
8. Verify and observe
9. Report; rollback separately authorized if needed

### States and transitions

NOT_RELEASE_CANDIDATE → CANDIDATE → CHECKS_READY → HUMAN_RELEASE_DECISION → RELEASED | REJECTED | ROLLBACK_DECISION_REQUIRED | ROLLED_BACK.

### Failure modes

- Merge auto-promotes release
- Version/tag generated from stale commit
- Changelog overclaims features
- Rollback untested
- Deployment target unknown
- Security/dependency NOT_RUN hidden
- Release authorization reused

### Recovery behavior

Failed release stops, preserves exact published/partial state and requests recovery/rollback decision. No automatic rollback where data/state effects unknown.

### Dependencies and shared contracts

- Git closure FTR-015
- Validation/CI FTR-011/FTR-023
- Evidence/review FTR-012
- Observability FTR-025
- Install/update FTR-004 for package distribution

### Safety and human-authority boundaries

- Merge ≠ release
- Human release authorization exact
- Network/secrets/deployment separately permissioned
- No release before target exists
- Rollback destructive/operational and separate

### Acceptance criteria

- Release package bound to exact artifact
- User-visible changes accurate
- Required checks and NOT_RUN clear
- Rollback tested/understood
- Post-release verification defined
- No hidden publication

### Required negative scenarios

- Stale commit/tag mismatch detected
- CI PASS alone cannot release
- Missing rollback blocks affected release
- Unapproved network/credential use blocked
- Release cannot silently update docs/branch beyond scope

### Minimal implementation model candidate

Document/CLI assistant over Git/package metadata and accepted release adapter. Build only when first real distribution target chosen.

### Targeted research before implementation

Inspect Proposed Pipeline Release stage, historical merge/release gates and version/update paths. Determine minimal release target for AOS.

### Non-goals

- First MVP
- Automatic deployment
- Cloud platform selection
- Release approval by agent
## FTR-025 — Observability, Audit Log, Incident/Lessons Memory and Continuous Improvement

```yaml
feature_id: FTR-025
layer: Product Runtime support / Later operations
disposition: CANDIDATE_SUPPORT
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-063` Observability and Audit Log; `IDEA-064` Continuous Improvement, Lessons Feedback and Dependency/Security Audit  
**Source references:** `CHAT-013`, `REF-AF-001`, `REF-AG-001`, `SRC-006`, `SRC-008`

### Problem

Failures, denied actions, user confusion and repeated manual work are forgotten or buried in chats/reports. Metrics can also become vanity readiness signals.

### Target users

Product owner, maintainer, reviewer, support agent and future feature designer.

### Desired outcome

A minimal event/incident/lesson loop that records material outcomes and converts them into reviewed preventive rules, regression tests or backlog candidates without making logs a Source of Truth or automatic governance.

### Trigger

Material failure, near miss, denied action, user friction, repeated workaround, release/runtime event or completed dogfood cycle.

### Preconditions

- Event subject and temporal scope identifiable
- Privacy/redaction policy
- Lesson conversion process defined
- No automatic product/architecture acceptance

### Inputs

- Stage/validation/review results
- Denied-action and recovery records
- User feedback/support issue
- Runtime/release metrics when available
- Dependency/security findings

### Outputs and observable behavior

- Redacted audit event
- Incident record with impact/root-cause candidate
- Lesson candidate
- Preventive rule/test/backlog proposal
- Trend/metric view with limitations

### Main flow

1. Capture material event and subject identity
2. Classify severity/fact vs inference
3. Record user/system impact
4. Analyze root-cause candidate and contributing conditions
5. Propose preventive rule and test
6. Human/reviewer confirms/revises lesson
7. Link accepted rule to feature/test/docs
8. Track recurrence and close feedback loop

### States and transitions

EVENT → INCIDENT_CANDIDATE → ANALYZED → LESSON_CANDIDATE → CONFIRMED | REJECTED | MORE_EVIDENCE_REQUIRED → TEST/RULE_LINKED.

### Failure modes

- Every log line becomes incident
- Root cause asserted without evidence
- Lesson automatically changes policy
- Metrics treated as approval/success
- Sensitive data stored
- Audit log competes with current state
- No test/owner so lesson forgotten

### Recovery behavior

Correct/supersede incident/lesson transparently, retain provenance, remove sensitive data per policy, and keep unresolved cause as inference/unknown. Do not rewrite historical result.

### Dependencies and shared contracts

- Stage/Evidence records
- Recovery/denied actions FTR-014
- CI/regression FTR-023
- Pattern library FTR-022
- Project Memory FTR-016

### Safety and human-authority boundaries

- Lessons ≠ Source of Truth until accepted in proper fact class
- Metrics ≠ approval
- Privacy/redaction
- No automatic enforcement/backlog priority
- Runtime telemetry optional

### Acceptance criteria

- Material incident understandable and traceable
- Fact/inference separated
- Preventive proposal maps to test/check
- Human review recorded where rule changes behavior
- Recurrence measurable
- First-contact/user-friction lessons captured

### Required negative scenarios

- Unsupported root cause remains inference
- Secret/medical data redacted
- Historical PASS not changed by later incident
- Lesson cannot set authorized=true
- Vanity metric cannot close feature

### Minimal implementation model candidate

Markdown/JSON incident and lesson records plus simple trend index. Start with manual capture from real dogfood; observability backend only after runtime exists.

### Targeted research before implementation

Inspect Lessons Learned/Incident Memory feature, AOS-FARM reports and Continuous Improvement proposal. Identify repeated incidents worth first regression fixtures.

### Non-goals

- Full telemetry platform
- Automatic root-cause AI authority
- Performance monitoring before runtime
- Policy auto-update
## FTR-026 — Extension/Plugin/Capability Module Model

```yaml
feature_id: FTR-026
layer: Architecture extension
disposition: DEFERRED
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-065` Extension / Plugin Model  
**Source references:** `CHAT-009`, `SRC-004`

### Problem

Future capabilities may bloat core or create hard dependencies. A plugin system introduced before stable contracts can freeze wrong boundaries and multiply compatibility/security risks.

### Target users

AOS maintainer, extension developer, domain module owner and product owner.

### Desired outcome

A minimal extension contract, admitted only after repeated extension points are observed, with versioning, capability declaration, isolation, permissions and replaceability.

### Trigger

At least two real capabilities need the same stable extension point and cannot be cleanly implemented in core without unwanted coupling.

### Preconditions

- Stable core contracts and Product Runtime
- Observed extension use cases
- Security/dependency/versioning decision
- Failure isolation and uninstall path

### Inputs

- Extension manifest
- Declared capabilities/contracts
- Required permissions/dependencies
- Compatibility version
- Configuration and lifecycle hooks

### Outputs and observable behavior

- Loaded/disabled/rejected extension status
- Capability registry entry as derived data
- Isolated outputs/errors
- Compatibility diagnostics
- Uninstall/upgrade plan

### Main flow

1. Validate manifest/signature/source as policy requires
2. Check contract/version/dependencies/permissions
3. Load through narrow interface
4. Expose declared capabilities only
5. Run health/contract tests
6. Isolate failure
7. Support disable/upgrade/remove
8. Rebuild capability index

### States and transitions

DISCOVERED → VALIDATING → ENABLED | DISABLED | INCOMPATIBLE | BLOCKED_PERMISSION | FAILED_ISOLATED | REMOVED.

### Failure modes

- Plugin API designed speculatively
- Extension overrides core safety/SoT
- Dependency conflict breaks core
- Failure corrupts project state
- Uninstall leaves orphan state
- Capability registry becomes authority
- Malicious/untrusted extension

### Recovery behavior

Disable/isolate extension, preserve core and user data, rollback extension version if explicitly supported, rebuild derived index. Core workflow continues without optional module.

### Dependencies and shared contracts

- Stable shared contracts
- Permission/enforcement FTR-019/FTR-020
- Drift/registry FTR-021
- Install/update FTR-004
- Architecture decision FTR-005

### Safety and human-authority boundaries

- Deferred until real extension points
- Cannot override safety/human authority
- Explicit dependencies/permissions
- Optional and removable
- Separate decision for third-party trust

### Acceptance criteria

- Core works without extension
- Version/permission mismatch clear
- Failure isolated
- Upgrade/remove recoverable
- Capability declaration accurate
- No hidden Source of Truth

### Required negative scenarios

- Extension requesting undeclared network/write blocked
- Incompatible version rejected
- Disabled extension cannot act
- Failure does not alter core state
- Uninstall preserves user-owned data

### Minimal implementation model candidate

Begin with in-process capability interface/package modules only after stable contracts; avoid marketplace/dynamic remote loading initially.

### Targeted research before implementation

Review Future Reference capability modules and actual module candidates. Derive interface from two concrete modules, not imagined extensibility.

### Non-goals

- Plugin marketplace
- Remote arbitrary code loading
- First-slice requirement
- Governance bypass
## FTR-027 — Domain Modules: Medical and Design

```yaml
feature_id: FTR-027
layer: Regulated/creative domain extensions
disposition: DEFERRED_SEPARATE_DECISIONS
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-066` Domain Modules; `IDEA-067` Medical Domain Module; `IDEA-068` Design Module  
**Source references:** `CHAT-009`, `CURRENT-INSTRUCTIONS`, `SRC-004`

### Problem

Domain-specific workflows need specialized language, data, validation and tools. Embedding them in core leaks complexity and, for medical use, creates privacy/safety/compliance risk.

### Target users

Domain professional, domain reviewer, extension maintainer and end user; Medical module assumes qualified human authority.

### Desired outcome

Separate replaceable domain modules using stable core contracts, with domain-specific Feature Contracts, provider/privacy policy, validation and explicit human professional checkpoints.

### Trigger

Core Product Runtime stable and a validated domain user/job is selected.

### Preconditions

- Extension model or explicit module boundary
- Domain Product Contract
- Data classification/threat/compliance analysis
- Approved providers/tools
- Qualified human review model

### Inputs

- Domain intent/data/artifacts
- Core task/context contracts
- Domain policy/configuration
- Reference standards and accepted workflows

### Outputs and observable behavior

- Domain-specific brief/context/artifact
- Validation/review package
- Data-routing/audit record
- Explicit limitations and human decision

### Main flow

1. Classify domain request and data sensitivity
2. Apply domain intake and allowed-provider rules
3. Generate domain-specific plan/artifact through narrow interface
4. Run domain checks
5. Present professional review package
6. Human domain expert accepts/rejects
7. Store only permitted durable data

### States and transitions

UNAVAILABLE → DOMAIN_CONFIGURED → REQUEST_CLASSIFIED → PROCESSING → PROFESSIONAL_REVIEW_REQUIRED → ACCEPTED | REJECTED | BLOCKED_POLICY.

### Failure modes

- Medical data sent to unapproved provider
- AI output treated as medical decision
- Domain rules override core safety
- Design assets/licenses mishandled
- Core depends on domain module
- Compliance assumed from generic guard

### Recovery behavior

Stop routing/processing, preserve minimal audit without sensitive leakage, allow qualified human/manual workflow, disable/remove module without core impact.

### Dependencies and shared contracts

- Extension model FTR-026 or explicit boundary
- Permission/provider/routing FTR-018/FTR-019
- Human Review FTR-012
- Domain-specific accepted contracts
- Security/compliance architecture

### Safety and human-authority boundaries

- Medical: qualified human is final authority; no diagnosis/treatment automation authority
- Separate architecture/dependency/privacy decisions
- No sensitive cross-project memory/index by default
- Domain module cannot modify core policy

### Acceptance criteria

- Validated domain user/job
- Provider/data flow explicit
- Human professional checkpoint mandatory where applicable
- Module removable
- Domain failures isolated
- Outputs state limitations and provenance

### Required negative scenarios

- Unapproved provider blocked
- Sensitive data excluded from general RAG/log
- AI-generated medical acceptance rejected
- Module unavailable does not break core
- License/provenance missing blocks affected design asset

### Minimal implementation model candidate

Separate package/module after extension contracts; Medical and Design are distinct projects/modules, not one generic domain engine. Start with non-sensitive/local prototypes if authorized.

### Targeted research before implementation

Use Future Reference only as idea source. Before any implementation, conduct domain-specific product, privacy, legal/compliance and threat-model research.

### Non-goals

- Core MVP
- Autonomous medical decisions
- Generic compliance claim
- Shared domain database by default
## FTR-028 — Workbench / SaaS UI for Onboarding, Status, Review and Collaboration

```yaml
feature_id: FTR-028
layer: UX wrapper
disposition: DEFERRED
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-069` Workbench / SaaS UI  
**Source references:** `CHAT-009`, `SRC-004`

### Problem

CLI/chat artifacts may be difficult for broader teams; users may want project selection, onboarding, status, review queue and collaboration. UI built too early can duplicate state and create fake approval semantics.

### Target users

Non-programmer product owner, reviewer, team lead and collaborator.

### Desired outcome

A UI that renders and edits accepted artifact contracts, shows source-linked status/Evidence and captures explicit human decisions without becoming independent Source of Truth.

### Trigger

Stable CLI/artifact contracts and repeated UX evidence show a UI materially improves onboarding/review/collaboration.

### Preconditions

- Stable Product Runtime contracts
- Authentication/authorization/privacy architecture
- Project/decision Source of Truth selected
- API/adapters tested
- Deployment/operations target

### Inputs

- Projects/repositories connected under permission
- Intent/Brief/Status/Review artifacts
- Evidence and human decision forms
- User/team identity

### Outputs and observable behavior

- Onboarding and project views
- Task/status/next/details UI
- Review queue and one-document review
- Human decision records written to authoritative channel
- Notifications/audit according to policy

### Main flow

1. Authenticate and select project
2. Load authoritative/derived artifacts with freshness
3. Guide intake/onboarding
4. Display status and source-linked Evidence
5. Render review/decision form
6. Write decision through exact contract
7. Refresh from Source of Truth
8. Handle conflicts/offline/stale state explicitly

### States and transitions

UNAUTHENTICATED → CONNECTED → PROJECT_SELECTED → VIEWING | EDITING_DRAFT | REVIEWING → DECISION_RECORDED | STALE | PERMISSION_BLOCKED.

### Failure modes

- UI cache diverges
- Approval button lacks authenticity/subject binding
- Hidden auto-save mutates protected docs
- Auth/provider complexity dominates product
- Sensitive data exposed
- UI claims completion from cached PASS

### Recovery behavior

Treat UI as replaceable client; refresh/reconcile from Source of Truth, preserve unsaved draft separately, block decisions on stale subject, allow CLI/artifact fallback.

### Dependencies and shared contracts

- Stable contracts across FTR-001–016
- Decision authenticity FTR-021
- Permission/routing/privacy FTR-018/FTR-019
- Project Memory FTR-016
- Deployment/release FTR-024

### Safety and human-authority boundaries

- Deferred until core proven
- UI state derived except explicit draft/decision writes
- No implicit approval/Git action
- Auth/privacy separate architecture
- CLI/artifact workflow remains viable

### Acceptance criteria

- Same behavior/status as underlying contracts
- Stale data visible and blocks authority actions
- Decision bound to exact subject/human
- No duplicate SoT
- Onboarding/review time measurably improved
- Fallback works

### Required negative scenarios

- Cached PASS cannot approve
- Changed candidate invalidates open review form
- Unauthorized project hidden/blocked
- Offline draft cannot become canonical automatically
- UI failure does not corrupt repository

### Minimal implementation model candidate

Thin web/local client over versioned API/artifact adapters. Begin after one stable CLI/manual journey; avoid building backend collaboration platform prematurely.

### Targeted research before implementation

Review SaaS/dashboard proposals and actual non-programmer first-contact/review pain. Prototype read-only status/review UI before writes.

### Non-goals

- Initial implementation target
- Independent workflow engine
- Automatic deployment/Git
- Replacing repository knowledge
## FTR-029 — Template Export, Prompt Packs, Capability Modules, Cross-Repo Context, Localization and Policy Overlays

```yaml
feature_id: FTR-029
layer: Packaging / Extension support
disposition: DEFERRED_RESEARCH
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-070` Template Export, Prompt Packs, Capability Modules, Cross-Repo Context, Localization and Policy Overlays  
**Source references:** `REF-AF-001`, `SRC-004`, `SRC-006`

### Problem

Users need reusable templates/prompts/modules and possibly multi-repository/localized policies, but copied packs drift from source, overwrite local changes or carry hidden authority/instructions.

### Target users

AOS maintainer, project adopter, localization/policy owner and multi-repository team.

### Desired outcome

Versioned export/import/update contracts for templates and prompt/capability packs, with provenance, ownership, conflict handling, localization/policy layering and explicit cross-repository permissions.

### Trigger

Stable reusable artifact exists and more than one project needs it.

### Preconditions

- Artifact source/owner/version known
- Install/update ownership model FTR-004
- Prompt/external-content boundary
- Compatibility and localization policy
- Cross-repo scope human-authorized

### Inputs

- Template/prompt/module package
- Manifest/version/digest
- Target project/repository
- Local overrides/translations/policy overlays
- Requested operation

### Outputs and observable behavior

- Dry-run diff/conflicts
- Installed/exported pack with provenance
- Override/translation map
- Update status and migration notes
- Cross-repo context package with explicit boundaries

### Main flow

1. Classify artifact and authority
2. Validate manifest/source/version
3. Inspect target and local modifications
4. Compute preview
5. Human authorizes exact transfer/update
6. Apply atomically
7. Preserve local overrides/user state
8. Validate prompt references/contracts
9. Record provenance and future update path

### States and transitions

SOURCE_READY → EXPORTABLE → PREVIEW_READY → INSTALLED | CONFLICTED | INCOMPATIBLE → UPDATE_AVAILABLE | UPDATED | REMOVED_WITH_OVERRIDES_PRESERVED.

### Failure modes

- Dev prompt pack copied as consumer authority
- Template update overwrites local policy
- Localization changes semantics
- Cross-repo context leaks private data
- Pack references missing files
- Manifest/source drift
- Prompt injection embedded in imported content

### Recovery behavior

No writes on preview; conflict requires explicit resolution; rollback package version while preserving local/user data; disable/remove pack; revalidate references. Imported text remains untrusted until classified.

### Dependencies and shared contracts

- Install/update FTR-004
- Permission/content FTR-019
- Extension model FTR-026 when capability code involved
- Drift/source guard FTR-021
- Project Memory FTR-016

### Safety and human-authority boundaries

- Exported pack has no automatic target authority
- Cross-repo reads explicit
- Localization/policy overlays cannot override core safety
- No code execution from template import
- Separate release/version decision

### Acceptance criteria

- Exact provenance/version visible
- Local changes preserved or conflict shown
- Broken references detected
- Repeated update idempotent
- Cross-repo/sensitive boundaries enforced
- Uninstall safe

### Required negative scenarios

- Stale manifest/update rejected
- Imported prompt cannot grant execution
- Missing referenced file fails validation
- Translation cannot silently alter status enum/authority rule
- Unauthorized repo excluded

### Minimal implementation model candidate

Manifest-based package format reusing installer planner; first support static templates/prompts only. Cross-repo and executable capability modules later.

### Targeted research before implementation

Inspect historical prompt-pack boundary drift, Template Export/Install/Update and root consumer files. Define source vs generated copy ownership.

### Non-goals

- Plugin marketplace
- Automatic policy distribution
- Unbounded cross-repo RAG
- Target authority transfer
## FTR-030 — Internal Contract Tooling: Strict Loaders, Parser Sunset, Registry Audits, Manifest/Cross-reference Validation and Schema/Runtime Drift Tests

```yaml
feature_id: FTR-030
layer: Development Factory internal
disposition: INTERNAL_RESEARCH_AFTER_CONTRACTS
status: DRAFT_SYNTHESIS
product_scope_effect: NONE
current_AOS_implementation_verification: NOT_RUN
authority: NONE
```

**Source micro-ideas:** `IDEA-071` Structured Loader Adapter and Strict Data Loader; `IDEA-072` Parser and Status Fragmentation Inventory with Sunset Plan; `IDEA-073` Registry Silent Data-Loss Audit; `IDEA-075` Document, Task Registry and Queue Helpers; `IDEA-076` Task Brief Compiler and Report Builder; `IDEA-077` Manifest, Package Integrity and Cross-Reference Validator; `IDEA-078` Schema / Runtime Drift, Module Boundaries, Negative Fixtures, Bootstrap and Quality Tooling  
**Source references:** `CHAT-011`, `REF-A02-001`, `REF-AF-001`, `REF-AG-001`, `SRC-007`, `SRC-009`

### Problem

Internal parsers/loaders/status models/registries/package manifests and generated copies can fragment, silently lose fields, accept invalid data or diverge from runtime. Building tools without stable contracts, however, creates another platform.

### Target users

AOS maintainers, test authors and tooling agents; not a primary end-user feature.

### Desired outcome

A small set of strict, replaceable internal utilities that enforce accepted contracts, audit round trips and package integrity, migrate legacy callers safely and expose drift through negative tests.

### Trigger

A stable contract has multiple callers or a documented parser/registry/package drift failure recurs.

### Preconditions

- Accepted or stable DRAFT contract chosen
- Current callers/inventory known
- Migration and sunset criteria
- No assumption of new central registry
- Tests cover old/new boundary

### Inputs

- Structured data/documents
- Schema/contract version
- Legacy parser/loader outputs
- Registry/package manifests
- Expected cross-references/module boundaries

### Outputs and observable behavior

- Strict loaded model or explicit errors
- Parser/status fragmentation inventory
- Round-trip data-loss report
- Manifest/cross-reference validation
- Schema/runtime/module drift findings
- Migration/sunset plan

### Main flow

1. Inventory all parsers/loaders/status/registry callers
2. Define one strict normalized contract
3. Create adapter around legacy input
4. Run golden and negative fixtures
5. Audit round-trip field/item preservation
6. Migrate one bounded caller at a time
7. Compare old/new outputs where compatibility intended
8. Record deprecation and remove old path only after Evidence

### States and transitions

FRAGMENTED → INVENTORIED → CONTRACT_DEFINED → ADAPTER_READY → DUAL_RUN → MIGRATED → LEGACY_SUNSET | BLOCKED_INCOMPATIBILITY.

### Failure modes

- Strict loader accepts bool-as-int/duplicates/unknown fields
- Registry drops records silently
- Manifest self-reference/hash ambiguity
- Cross-reference validator checks syntax but not subject
- Tests freeze bad legacy behavior
- Tooling scope expands into Control Plane
- Migration removes old path early

### Recovery behavior

Keep adapter/old path during bounded migration, stop on discrepancy, classify compatibility need, restore caller to known path, preserve audit outputs. Sunset only after accepted migration Evidence.

### Dependencies and shared contracts

- Stable contracts from 02_Architecture.md
- Validation/CI FTR-011/FTR-023
- Drift guard FTR-021
- Task/report compiler FTR-006
- Backlog/queue FTR-007 where applicable

### Safety and human-authority boundaries

- Internal tooling does not create product value claim
- No canonical/authority promotion
- No automatic correction
- No central registry unless separately justified
- Stdlib-first where practical, dependencies human-decided

### Acceptance criteria

- All callers and formats inventoried
- Invalid/unknown input rejected consistently
- Round-trip preserves every field/item
- Runtime and tests use same loader
- Package identity policy non-self-referential
- Migration reversible until sunset
- Tool removable/replaceable

### Required negative scenarios

- Empty/duplicate/extra/unknown/bool-int inputs
- Silent item/field loss
- Wrong schema version
- Stale/cross-subject manifest
- Broken links/IDs
- Module bypass of shared validator
- Legacy removal before all callers migrated

### Minimal implementation model candidate

Small libraries/CLI checks organized around accepted contracts, not a generalized framework. Use adapter/dual-run/sunset sequence and high-risk golden fixtures.

### Targeted research before implementation

Inspect Third Pass Temporary Implementation Plan, AOS-02 schema/runtime failures, AOS-FARM negative fixtures and package self-reference audits. Select only tools needed by first implemented feature.

### Non-goals

- User-facing Product Runtime
- Full central registry/Control Plane
- Automatic refactor of all legacy code
- Quality tooling as readiness proof

## 6. Original 78-idea crosswalk

The crosswalk proves that no original idea record was silently dropped. One micro-idea may support more than one family when it describes a shared mechanism.

| Original idea | Original title | Consolidated family/families | Original source refs |
|---|---|---|---|
| `IDEA-001` | Problem / Intent Intake | `FTR-001` | `CHAT-002`, `CHAT-006`, `REF-AF-002` |
| `IDEA-002` | Intake Classification and Sensitive-Domain Gate | `FTR-001` | `CURRENT-INSTRUCTIONS`, `REF-AF-002`, `SRC-006` |
| `IDEA-003` | User and Outcome Clarification | `FTR-001` | `CHAT-002`, `CHAT-003`, `CHAT-012` |
| `IDEA-004` | Project Discovery and Capability Map | `FTR-002` | `CHAT-009`, `SRC-008`, `REF-AF-001`, `REF-AG-001` |
| `IDEA-005` | Gap and Conflict Discovery | `FTR-002` | `CHAT-011`, `REF-AG-001`, `REF-A02-001` |
| `IDEA-006` | Project Brief and Specification Builder | `FTR-003` | `CHAT-006`, `REF-AF-002`, `CHAT-009` |
| `IDEA-007` | Technical Assignment | `FTR-003` | `CHAT-006`, `REF-AF-002` |
| `IDEA-008` | First Vertical Slice Selector and Capability Reconstruction | `FTR-003` | `CHAT-002`, `CHAT-009`, `SRC-008`, `CHAT-012` |
| `IDEA-009` | Architecture Need Check and Input Intake | `FTR-005` | `REF-AF-002`, `SRC-009` |
| `IDEA-010` | Architecture Assistant | `FTR-005` | `SRC-008`, `SRC-009`, `CHAT-009` |
| `IDEA-011` | Architecture Option Comparison and ADR Builder | `FTR-005` | `SRC-009`, `REF-A02-001` |
| `IDEA-012` | Stack Preset Registry | `FTR-005` | `SRC-009`, `SRC-004` |
| `IDEA-013` | Pattern / Solution Library and Fit Matrix | `FTR-022` | `SRC-009`, `CHAT-003`, `REF-A02-002` |
| `IDEA-014` | Architecture Evidence and Human Checkpoint Package | `FTR-005` | `SRC-009`, `CHAT-006` |
| `IDEA-015` | Architecture-to-Task Traceability | `FTR-005` | `SRC-009`, `CHAT-009` |
| `IDEA-016` | Task Generation and Task Brief | `FTR-006` | `CHAT-005`, `CHAT-006`, `REF-AG-001`, `REF-AF-002` |
| `IDEA-017` | Hierarchical Backlog, Lazy Decomposition and Queue | `FTR-007` | `SRC-010`, `SRC-005`, `REF-AF-001` |
| `IDEA-018` | Action Preflight | `FTR-009` | `SRC-006`, `CHAT-005`, `REF-AF-002` |
| `IDEA-019` | Execution Preview | `FTR-009` | `REF-A02-001`, `REF-AF-001` |
| `IDEA-020` | Scoped Execution | `FTR-010` | `CHAT-005`, `CHAT-006`, `REF-AF-002` |
| `IDEA-021` | Controlled Execution Guard | `FTR-010` | `SRC-007`, `REF-AF-002` |
| `IDEA-022` | Unified Result Contract / ValidationEnvelope | `FTR-011` | `SRC-007`, `REF-A02-001` |
| `IDEA-023` | Unified Validation CLI | `FTR-011` | `REF-AG-001`, `REF-AF-001`, `SRC-009` |
| `IDEA-024` | Doctor and Self-Test | `FTR-011` | `REF-AF-001`, `REF-AF-002` |
| `IDEA-025` | Evidence Collection | `FTR-012` | `CHAT-006`, `SRC-006`, `REF-A02-002` |
| `IDEA-026` | Compact Human Review Package | `FTR-012` | `CHAT-006`, `REF-AF-002`, `REF-A02-002` |
| `IDEA-027` | Independent Read-only Review | `FTR-012` | `SRC-006`, `CHAT-005`, `REF-A02-002` |
| `IDEA-028` | Human Decision Record and False-PASS Wording Guard | `FTR-012` | `REF-A02-001`, `REF-AG-001`, `CURRENT-INSTRUCTIONS` |
| `IDEA-029` | Diff and Scope Reconciliation | `FTR-013` | `CHAT-001`, `REF-AF-001`, `SRC-006` |
| `IDEA-030` | Disposable Validation Subject | `FTR-013` | `CHAT-001`, `REF-A02-001` |
| `IDEA-031` | Candidate Freeze and Identity | `FTR-013` | `REF-A02-002`, `CHAT-001` |
| `IDEA-032` | Recovery, Resume and Rollback | `FTR-014` | `CHAT-001`, `REF-A02-002`, `CHAT-012` |
| `IDEA-033` | Git Lifecycle Closure | `FTR-015` | `REF-AF-002`, `SRC-006`, `CURRENT-INSTRUCTIONS` |
| `IDEA-034` | Denied Action Log and State Recovery View | `FTR-014` | `SRC-006`, `REF-AG-001` |
| `IDEA-035` | Project Memory | `FTR-016` | `CHAT-003`, `CHAT-010`, `CHAT-012` |
| `IDEA-036` | Session Handoff | `FTR-014`, `FTR-016` | `CHAT-010`, `REF-AG-001`, `CURRENT-INSTRUCTIONS` |
| `IDEA-037` | Context Priority Rules | `FTR-016` | `SRC-006`, `SRC-005` |
| `IDEA-038` | Task-scoped Context Pack | `FTR-016` | `SRC-005`, `CHAT-010` |
| `IDEA-039` | RAG-light Context Index | `FTR-017` | `SRC-004`, `SRC-006`, `CHAT-003` |
| `IDEA-040` | Advisory Model Routing | `FTR-018` | `SRC-005`, `CHAT-010` |
| `IDEA-041` | Explicit Subagent Routing, Routing Audit and Provider Evaluation | `FTR-018` | `SRC-005`, `SRC-006`, `CHAT-010` |
| `IDEA-042` | Installer Dry-run | `FTR-004` | `REF-AF-001`, `REF-AG-001`, `CHAT-002` |
| `IDEA-043` | Safe Apply and Manual Transfer | `FTR-004` | `REF-AF-001`, `REF-AG-001` |
| `IDEA-044` | Safe Update and Uninstall | `FTR-004` | `SRC-004`, `REF-AF-001` |
| `IDEA-045` | Installation Manifest and Version Detection | `FTR-004` | `REF-AF-001`, `REF-A02-001` |
| `IDEA-046` | Example Project and Onboarding | `FTR-004` | `REF-AG-001` |
| `IDEA-047` | Beginner Tutor | `FTR-008` | `SRC-004`, `CHAT-003`, `REF-AF-001` |
| `IDEA-048` | Simple Control Surface | `FTR-008` | `REF-AF-001`, `REF-A02-002`, `CHAT-003` |
| `IDEA-049` | Status / Next / Details, Stable CLI Output and First Safe Commands | `FTR-008` | `REF-AF-001`, `REF-AG-001`, `REF-A02-001` |
| `IDEA-050` | Action Trust Boundary | `FTR-019` | `SRC-006`, `CURRENT-INSTRUCTIONS` |
| `IDEA-051` | Permission State Classifier and Error Taxonomy | `FTR-019` | `SRC-006`, `SRC-007`, `REF-A02-001` |
| `IDEA-052` | Prompt Injection Boundary for External Content | `FTR-019` | `SRC-006` |
| `IDEA-053` | Protected Path, Write and Command Allowlists | `FTR-019` | `SRC-004`, `SRC-006`, `REF-A02-001` |
| `IDEA-054` | Network, Sandbox and Git Permission Gate | `FTR-019` | `CURRENT-INSTRUCTIONS`, `SRC-006` |
| `IDEA-055` | Runtime Enforcement Layer | `FTR-020` | `SRC-004`, `SRC-006` |
| `IDEA-056` | Isolated Execution Environment | `FTR-020` | `SRC-006` |
| `IDEA-057` | Progressive Governance Modes | `FTR-020` | `SRC-004`, `CHAT-002`, `CURRENT-INSTRUCTIONS` |
| `IDEA-058` | Advanced Governance Gates | `FTR-020` | `SRC-004` |
| `IDEA-059` | Registry / Drift, Source-of-Truth Guard and Human Decision Authenticity | `FTR-021` | `SRC-004`, `REF-A02-001`, `REF-A02-002` |
| `IDEA-060` | Advisory CI and CI Smoke | `FTR-023` | `SRC-007`, `REF-AF-001`, `REF-A02-001` |
| `IDEA-061` | Release Checklist and Promotion Package | `FTR-024` | `SRC-008`, `REF-AF-002`, `REF-A02-002` |
| `IDEA-062` | Version, Changelog, Tag and Rollback Assistant | `FTR-024` | `SRC-008`, `REF-AF-001` |
| `IDEA-063` | Observability and Audit Log | `FTR-025` | `SRC-008`, `SRC-006` |
| `IDEA-064` | Continuous Improvement, Lessons Feedback and Dependency/Security Audit | `FTR-025` | `SRC-008`, `REF-AG-001`, `REF-AF-001` |
| `IDEA-065` | Extension / Plugin Model | `FTR-026` | `SRC-004`, `CHAT-009` |
| `IDEA-066` | Domain Modules | `FTR-027` | `SRC-004`, `CHAT-009` |
| `IDEA-067` | Medical Domain Module | `FTR-027` | `SRC-004`, `CURRENT-INSTRUCTIONS` |
| `IDEA-068` | Design Module | `FTR-027` | `SRC-004` |
| `IDEA-069` | Workbench / SaaS UI | `FTR-028` | `SRC-004`, `CHAT-009` |
| `IDEA-070` | Template Export, Prompt Packs, Capability Modules, Cross-Repo Context, Localization and Policy Overlays | `FTR-029` | `SRC-004`, `SRC-006`, `REF-AF-001` |
| `IDEA-071` | Structured Loader Adapter and Strict Data Loader | `FTR-030` | `SRC-007`, `REF-A02-001` |
| `IDEA-072` | Parser and Status Fragmentation Inventory with Sunset Plan | `FTR-030` | `SRC-007` |
| `IDEA-073` | Registry Silent Data-Loss Audit | `FTR-030` | `SRC-007` |
| `IDEA-074` | Safe Runner Kernels | `FTR-010` | `SRC-007` |
| `IDEA-075` | Document, Task Registry and Queue Helpers | `FTR-007`, `FTR-030` | `SRC-007`, `REF-AF-001`, `REF-AG-001` |
| `IDEA-076` | Task Brief Compiler and Report Builder | `FTR-006`, `FTR-030` | `SRC-007`, `REF-A02-001` |
| `IDEA-077` | Manifest, Package Integrity and Cross-Reference Validator | `FTR-030` | `SRC-007`, `SRC-009`, `CHAT-011` |
| `IDEA-078` | Schema / Runtime Drift, Module Boundaries, Negative Fixtures, Bootstrap and Quality Tooling | `FTR-023`, `FTR-030` | `REF-A02-001`, `REF-AF-001`, `REF-AG-001` |

## 7. Promotion workflow

```text
source occurrence / micro-idea
→ detailed family dossier
→ product-fit review: user + problem + outcome
→ human disposition: REQUIRED | OPTIONAL | DEFERRED | REJECTED | UNKNOWN
→ Product Contract and acceptance scenarios
→ DRAFT architecture options
→ human architecture/dependency decision
→ Task Brief
→ explicit execution authorization
```

Before human disposition, even a detailed dossier has `product_scope_effect: NONE`.

## 8. Feature readiness checklist for an agent

Before proposing implementation, the agent must be able to answer:

1. What user job is solved and what is observable?
2. Which inputs/outputs and states are stable?
3. What can fail, what does the user see, and how is recovery performed?
4. Which shared contracts and other feature families are dependencies?
5. Which actions remain human-only?
6. Which acceptance and negative scenarios will be tested?
7. Which parts are historical observations versus target proposals?
8. What exact repository paths/tests must be inspected next?
9. What legacy complexity is explicitly rejected?
10. Which product/architecture/dependency decisions are still open?

If any material answer is absent, status is `PLAN`/`TARGETED_RESEARCH`, not implementation-ready.
