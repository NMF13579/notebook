# 05 — AOS Reference


> **Artifact status:** `DRAFT`  
> **Authority:** `NONE`  
> **Canonical status:** `NOT_ASSIGNED`  
> **Human acceptance:** `NOT_REQUESTED`  
> **Implementation authorization:** `NONE`  
> **Source basis:** доступная история чатов проекта, current Project Instructions и загруженные reference notes; current repository/runtime verification — `NOT_RUN`.


## 1. Назначение

Документ хранит provenance map, history coverage, source roles, targeted research protocol, decisions, unknowns and conflicts. Он помогает проверить происхождение идеи, но сам не является Product Contract, Architecture Contract или implementation authorization.

```text
reference occurrence ≠ current implementation
historical acceptance ≠ current acceptance
source mapping ≠ target requirement
```

## 2. Source classes and authority

| Source class | Use | Authority in new AOS |
|---|---|---|
| Current Project Instructions | Agent behavior, safety, current work mode | Behavior/safety only |
| Explicit human direction in current conversation | Exact stated decision boundary | Human-scoped |
| Human-accepted canonical repository document | Project fact within fact class | Fact-class scoped |
| Uploaded reconstruction source | DRAFT/research input | `NONE` unless separately accepted |
| Chat history / summaries | Intent, preference, lesson, rejected approach | `NONE` |
| Historical repository observation | Behavior/test/failure evidence for captured snapshot | `NONE` for target |
| Generated synthesis/audit | Navigation, inference, candidate docs | `NONE` |

## 3. Uploaded source register

### `CURRENT-INSTRUCTIONS`

Defines current mode, repository role, Minimal Safety Floor, stage boundaries, no implementation/Git authorization and exact seven-document request. Does not define product/architecture facts permanently.

### `SRC-001` — `00 — AOS Reconstruction Project Control and Source Precedence.txt`

Useful for project identity, authority model, source precedence, legacy/chat boundary, claim classes and current documentation-reconstruction mode.

### `SRC-002` — `01 — AOS Documentation Reconstruction Workflow and Roadmap.txt`

Useful for `REIMPLEMENTATION_READY_DOCUMENTATION`, product-first sequence, required Product Contract fields, shared contracts, test design and human decision boundaries.

### `SRC-003` — `02 — AOS Minimal Safety and Authority Rules.txt`

Useful for human authority, Minimal Safety Floor, Task Brief, one-run-one-stage, validation separation, protected/destructive scope and Git boundaries.

### `SRC-004` — `03 — AOS Future and Legacy Reference.txt`

Future/deferred idea source:

- Advanced Governance Gates;
- Runtime Enforcement;
- Registry/Drift;
- RAG-light;
- SaaS Dashboard;
- Design Module;
- Medical Module;
- Template Export/Install/Update;
- Multi-Agent Coordination;
- Beginner Tutor.

All remain proposals/reference.

### `SRC-005` — `04 — AOS Model Routing and Task Decomposition Research.txt`

Useful for:

- lazy decomposition;
- task roles: architect/executor/reviewer/documentation;
- context boundaries;
- advisory, explicit and runtime routing levels;
- provider/privacy/medical boundary;
- routing record and pilot metrics.

### `SRC-006` — `05 - AOS-FARM — справочные идеи из harness engineering.txt`

Useful for:

- Action Trust Boundary;
- permission states and error taxonomy;
- preflight;
- context priority;
- script/validator contracts;
- denied-action log;
- capability modules;
- Git safety;
- prompt-injection boundary;
- runtime guardrails;
- isolated environment;
- read-only subagents.

### `SRC-007` — `06 - AOS-FARM — Third Pass Temporary Implementation Plan.txt`

Historical implementation/tooling ideas:

- parser/status inventory;
- unified result contract / ValidationEnvelope;
- registry silent-data-loss audit;
- structured loader adapter;
- CI smoke;
- safe runner kernels;
- parser sunset;
- controlled execution guard.

Use mainly as automation-first lesson and internal tooling reference.

### `SRC-008` — `07 - AOS-FARM — Proposed Pipeline Evolution.txt`

Pipeline candidates:

- Project Discovery;
- Architecture Decision;
- Architecture Assistant;
- Capability Reconstruction;
- Testing;
- Release;
- Observability;
- Continuous Improvement.

Not an accepted roadmap.

### `SRC-009` — `08 - Architecture Lifecycle Integration Plan.txt`

Useful for:

- architecture need check;
- architecture routing and validation;
- validate-all;
- dogfood;
- schema/cross-reference validation;
- human checkpoint;
- architecture-to-task traceability;
- read-only dashboard.

### `SRC-010` — `Декомпозиция ТЗ.txt`

Useful for hierarchy `Epic → Stage → Sub-stage → Task`, lazy decomposition and child-parent completion checks.

### `SRC-011` — `AOS_Chat_History_Extraction_Structure_Draft.md`

Earlier proposal for normalized chat knowledge: intent, problems, features, behavior, contracts, patterns, decisions, failures, lessons, tests, unknowns and reference map.

### `PREV-PACKAGE`

`AOS_Chat_History_Synthesis_With_Feature_Idea_Bank_RU` and its consolidated/JSONL artifacts. Useful as an inventory and source crosswalk. Audited as structurally fragmented and feature descriptions too shallow for reconstruction.

## 4. Chat-history source index

Coverage is reconstructed from available project conversation summaries and retained context, not a byte-complete export. Missing item means `NOT_FOUND_IN_CURRENT_SOURCE_SET`, not global absence.

| ID | Period / conversation | Durable contribution | Authority |
|---|---|---|---|
| `CHAT-001` | 2026-07-14–16 — recovery / AOS-FARM.683.15 | environment identity, baseline/candidate, freeze, stage separation, validation handoff, no auto transition | `NONE` |
| `CHAT-002` | 2026-07-17–18 — greenfield refoundation / AOS-02 | legacy boundary, Product First, first vertical slice, bootstrap limits, deferred Control Plane | `NONE` |
| `CHAT-003` | 2026-07-19 — documentation structure/simplification | taxonomy, Product/Factory/Control separation, duplicate reduction | `NONE` |
| `CHAT-004` | 2026-07-19 — documentation audit | reconstructability gaps, duplicated concepts, missing Product Runtime contracts | `NONE` |
| `CHAT-005` | 2026-07-19 — Compact Safe Path | one run/one stage, conditional planning, explicit stop, separate Git permissions | `NONE` |
| `CHAT-006` | 2026-07-20 — idea-to-acceptance pipeline | problem/brief/spec/task/execution/Evidence/review/human decision and closure | `NONE` |
| `CHAT-007` | 2026-07-20 — storage and human-readable feature docs | audience-centered feature overview, traceability and storage model | `NONE` |
| `CHAT-008` | 2026-07-20–23 — AOS-FARM/AgentOS extraction | reference extraction, bootstrap/doctor targets, limits of exhaustive reconstruction | `NONE` |
| `CHAT-009` | 2026-07-23 — architecture/modules | architecture after product definition, modular Governance, implementation-model questions | `NONE` |
| `CHAT-010` | 2026-07-23 — Codex routing/custom agents | role separation, registration, model routing and cross-environment handoff | `NONE` |
| `CHAT-011` | 2026-07-24–25 — synthesis/validation/readiness | claim discipline, evidence gaps, practical reconstruction usefulness | `NONE` |
| `CHAT-012` | 2026-07-26 — strategy pivot | stop exhaustive extraction; use chat synthesis and feature-scoped legacy research | Human-confirmed direction for current work |
| `CHAT-013` | 2026-07-02 — consumer dogfood and five control features | install/first-run, Unified Validate, Safety Fixtures, Intake Wizard, Review/Handoff, Lessons Memory | `NONE` |
| `CHAT-014` | 2026-07-04 — installation/transfer | dry-run installer, apply gap, root-template defect, prompt-pack drift and ownership/update concerns | `NONE` |
| `CHAT-015` | 2026-07-05 — documentation dedup / first-start | one authoritative install/first-start route; short pointers instead of full duplicates | `NONE` |
| `CHAT-016` | 2026-07-26 — seven-document and feature-depth decision | exactly `00_Core.md`…`06_Features.md`; no file proliferation; human/agent-readable dossiers | Human-confirmed for current artifact |

## 5. Historical repository/reference map

### Historical reference IDs used in `06_Features.md`

| ID | Meaning | Authority |
|---|---|---|
| `REF-AF-001` | Historical read-only AOS-FARM capability/repository analysis: installer, doctor, validation, queue, control and guard surfaces | `NONE` |
| `REF-AF-002` | Historical AOS-FARM install-to-human-acceptance pipeline reconstruction | `NONE` |
| `REF-AG-001` | Historical read-only AgentOS/AOS-1 research package: bootstrap, Task Contract, validation, install/update and lessons | `NONE` |
| `REF-A02-001` | Historical read-only AOS-02 audit: schemas, strict loader, CLI, preview and control-core failures | `NONE` |
| `REF-A02-002` | Historical AOS-02 handoff/reference: digest identity, candidate freeze, review and closure patterns | `NONE` |

### `NMF13579/AOS-FARM`

Potentially useful targets:

- installation/bootstrap/dry-run/manual transfer;
- `doctor`, self-test and validation aggregation;
- FIRST-START/onboarding and Simple Control Surface;
- intake/interview/Technical Assignment/task candidate;
- review/handoff and human decision boundaries;
- task registry/queue semantics;
- candidate freeze and execution package identity;
- Git push/merge guards and deterministic merge authorization;
- technical/lifecycle closure;
- negative fixtures, CLI status, parser/loader migration;
- lessons/incident memory;
- environment doctor/hygiene.

Do not import automatically:

- full Control Plane;
- task/lifecycle registry topology;
- historical task IDs/statuses;
- self-referential approval/recovery machinery;
- old branch/current-state claims;
- large planning chains.

### Historical `NMF13579/AOS-02`

Useful for:

- executable control-core prototype;
- schema/validator/CLI integration;
- preview/block mutation model;
- candidate identity and handoff;
- failure cases around human decision, empty mappings, bogus status, scope, atomicity and recovery.

Treat its target-repository role as historical. Current implementation repository is `UNASSIGNED`.

### `AgentOS` / `AOS-1`

Useful for:

- original product intent;
- bootstrap spine;
- install/update concepts;
- Task Contract;
- tutor/onboarding;
- RAG-light;
- packaging/module concepts;
- historical tests and lessons.

No active authority.

## 6. Feature-to-reference routing

| Feature family | First targeted references/questions |
|---|---|
| `FTR-001` Intent Intake | dogfood intake/interview; classification and sensitive-domain gates |
| `FTR-002` Project Discovery | Proposed Pipeline Evolution; existing analyzer/capability map behavior |
| `FTR-003` Specification/Slice | Technical Assignment flow; first-slice/refoundation discussions |
| `FTR-004` Install/First-Start | installer dry-run/apply, FIRST-START dedup, doctor/onboarding tests |
| `FTR-005` Architecture Support | Architecture Lifecycle source, ADR/checkpoint artifacts |
| `FTR-006` Task Brief Compiler | Task Brief templates, task candidate conversion, compiler/report builder |
| `FTR-007` Backlog/Queue | decomposition source, historical registry/queue semantics |
| `FTR-008` Control Surface/Closure | `/status`, `/next`, `/details`, first safe commands, technical closure |
| `FTR-009` Preflight/Preview | harness trust table, AOS-02 preview, repository checks |
| `FTR-010` Scoped Execution | controlled guard, runner kernels, Task Brief scope enforcement |
| `FTR-011` Validate/Doctor | Unified AOS Validate, ValidationEnvelope, doctor and exit codes |
| `FTR-012` Evidence/Review | review/handoff package, semantic guard, human-decision failures |
| `FTR-013` Freeze/Reconcile | candidate freeze, disposable subject, diff/scope checks |
| `FTR-014` Recovery/Handoff | 683.15 recovery, denied-action log, session resume |
| `FTR-015` Git Closure | push/merge boundary, merge authorization, remote closure |
| `FTR-016` Project Memory/Context | scaffolding context, handoff, context priority |
| `FTR-017` RAG-light | future reference only; determine whether search problem exists |
| `FTR-018` Routing | model-routing research, custom agents, provider evaluation |
| `FTR-019` Permissions/External Content | trust boundary, allowlists, injection boundary |
| `FTR-020` Enforcement/Governance | harness runtime guard; refoundation defer rules |
| `FTR-021` Drift/SoT/Auth | registry drift, AOS-02 authenticity, schema/runtime checks |
| `FTR-022` Pattern Library | architecture fit matrix and solution-pattern discussions |
| `FTR-023` CI/Safety Fixtures | consumer safety fixtures, CI smoke, negative cases |
| `FTR-024` Release | release/promotion/checklist/tag/rollback proposals |
| `FTR-025` Observability/Lessons | audit log, continuous improvement, incident memory |
| `FTR-026` Plugin Model | future module boundaries and capability modules |
| `FTR-027` Domain Modules | Medical/Design references; privacy/compliance boundary |
| `FTR-028` Workbench UI | SaaS/dashboard proposals after artifact contracts |
| `FTR-029` Export/Prompt Packs | template export/update, prompt-pack boundary drift, localization |
| `FTR-030` Internal Tooling | loader/parser/registry/manifest/schema/runtime drift sources |

## 7. Targeted research record

For each future inspection use one record:

```yaml
research_id:
feature_id:
question:
repository:
ref_or_branch:
commit_or_tree:
paths: []
methods_or_commands: []
read_only: true
findings:
  - class: SOURCE_ASSERTION | VERIFIED_OBSERVATION | INFERENCE | PROPOSAL | UNKNOWN
    statement:
    evidence_locator:
    temporal_scope:
legacy_capability_status:
useful_contracts: []
useful_negative_cases: []
rejected_legacy_complexity: []
limitations: []
remaining_unknowns: []
```

## 8. Research stop conditions

Stop and report when:

- question answered with sufficient Evidence;
- source snapshot unavailable;
- required path/object missing;
- conflict changes feature scope;
- inspection requires network/permission expansion;
- finding indicates protected architecture decision;
- research begins expanding beyond selected feature;
- repository current state cannot be distinguished from chat memory.

## 9. Promotion model

```text
reference idea
→ feature family in 06_Features.md
→ product-fit review
→ human product disposition
→ Product Contract
→ DRAFT architecture
→ human architecture/dependency decisions
→ Task Brief
→ execution authorization
```

Before promotion:

- idea has `authority: NONE`;
- source count is not product validation;
- historical implementation quality is not assumed;
- no roadmap priority is created.

## 10. Recorded current directions

| ID | Direction | Status |
|---|---|---|
| `DIR-001` | New documentation package uses seven files | Human-confirmed for current artifact |
| `DIR-002` | Feature descriptions must be understandable to human and agent | Human-confirmed |
| `DIR-003` | Stop exhaustive extraction | Human-confirmed |
| `DIR-004` | Use feature-scoped reference research | Human-confirmed |
| `DIR-005` | Product Runtime first | Human-confirmed strategic direction |
| `DIR-006` | Legacy read-only, authority none | Human-confirmed |
| `DIR-007` | Current implementation repository unassigned | Current safe fact |

## 11. Decision candidates requiring human action

| ID | Decision | Why it matters |
|---|---|---|
| `DEC-001` | Relationship to AOS-FARM: clean reimplementation/compatible replacement/other | Sets compatibility and research burden |
| `DEC-002` | Priority user and first job | Determines Product Runtime |
| `DEC-003` | First vertical slice | Determines first implementation package |
| `DEC-004` | Implementation repository | Required before bootstrap/Git work |
| `DEC-005` | Initial interface | Shapes contracts and tests |
| `DEC-006` | Project Memory persistence | Avoids premature DB or insufficient resume state |
| `DEC-007` | Governance packaging and admission | Prevents control from becoming foundation |
| `DEC-008` | Compatibility target | Determines differential tests and migration |
| `DEC-009` | Language/toolchain/dependencies | Architecture/dependency decision |
| `DEC-010` | Human decision authenticity | Required before authority-bearing runtime |
| `DEC-011` | Provider/privacy/model-routing policy | Required before external or regulated workloads |
| `DEC-012` | Required/optional/deferred feature set | Product scope decision |

## 12. Preserved conflicts

### `CONFLICT-001` — Implementation repository

Historical discussions used `NMF13579/AOS-02` as target. Current Project Instructions say `Implementation repository: UNASSIGNED`.

**Safe state:** `UNASSIGNED`. Resolution requires human project/architecture decision.

### `CONFLICT-002` — `/aos/` workspace

Historical installer/scaffolding discussions assumed `/aos/`; greenfield bootstrap discussions sometimes prohibited early workspace creation.

**Safe state:** path and ownership model `UNKNOWN`; feature remains candidate.

### `CONFLICT-003` — Scaffolding as first slice

Scaffolding was proposed as an early slice, while product-first rule rejects internal repository management as substitute for user value.

**Safe state:** admissible only if Product Contract demonstrates direct user job/outcome.

### `CONFLICT-004` — Minimal control vs rich Governance

Historical AOS-FARM invested in extensive control machinery; refoundation chose Minimal Safety Floor and late progressive Governance.

**Safe state:** retain invariants and failure cases, not full topology.

### `CONFLICT-005` — One central registry vs repository-derived state

Registry helps navigation/drift but can become competing Source of Truth.

**Safe state:** derived/rebuildable registry only until explicit architecture decision.

### `CONFLICT-006` — Broad autonomy vs one-stage stop

Some discussions sought fully automatic completion; current safety rules require bounded stages and human authority boundaries.

**Safe state:** no autonomous stage/authority transition.

## 13. Open unknowns

1. Exact first Product Runtime feature and interface.
2. Which legacy capabilities are currently working, partial, design-only, broken or obsolete.
3. Required compatibility with AOS-FARM/AgentOS artifacts.
4. Exact Source of Truth for project state and human decisions.
5. Persistence format for Project Memory.
6. Exact install/update ownership classes and path.
7. Risk Profile vocabulary for future runtime.
8. Independent validator/environment strategy.
9. Model/provider/privacy policy.
10. Domain/compliance requirements for Medical module.
11. Metrics proving routing/RAG/automation value.
12. Which of 30 feature families become `REQUIRED`, `OPTIONAL`, `DEFERRED` or `REJECTED`.

## 14. Audit method and limitations

This revision compared:

- available project conversation summaries and retained personal context;
- uploaded sources `00`–`08` and `Декомпозиция ТЗ`;
- previous consolidated package and 78-record JSONL idea bank;
- historical repository/audit summaries available in the project context.

Performed:

- structural inventory of previous package;
- field-level audit of all 78 idea records;
- source-to-idea crosswalk preservation;
- thematic consolidation into 30 families;
- reclassification Product/Factory/Governance/Extension/Internal;
- insertion of missing behavior, contract, failure, recovery and test fields;
- reconciliation with named chat-history features, including first contact, Unified Validate, Safety Fixtures, Intake Wizard, Review/Handoff, Lessons Memory, lifecycle closure, candidate freeze, merge authorization, routing, Project Memory and safe install/update.

Not performed:

- byte-complete export of all chats;
- current checkout of `NMF13579/notebook`, `AOS-FARM` or `AOS-02`;
- branch/HEAD/baseline/worktree verification;
- current code search or runtime execution;
- test execution;
- independent semantic validation by another reviewer;
- human acceptance/canonicalization.

Therefore:

```text
current repository verification: NOT_RUN
runtime verification: NOT_RUN
independent validation: NOT_RUN
human acceptance: NOT_REQUESTED
```
