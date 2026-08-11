---
package: AOS_LEAN_PORTABLE_DOCUMENTATION
package_revision: PORTABLE-DRAFT-1
source_candidate_identity: sha256:57446e0d8075985af2229eae86cc6cf018b41ec255f0140b7bb20b45ef3ded65
artifact_role: PRODUCT_MODEL_OWNER
status: DRAFT
authority: NONE
source_owner_identity: sha256:c119f8f301abcd93167e3f5b61272dfda7bb499fff58018e6163bb325308b2cb
accepted_extension_identity: sha256:3e9fbbcde2d07a8716f0dc28eb33e642e1c42766da738e41c7137abf358af197
implementation_authorization: NONE
git_authorization: NONE
---

# 01 — Product Model

## 1. Роль и ownership

Этот документ — полный portable product-level design view. Исходный Product owner byte-bound в [README.md](README.md). В соответствии с принятым `X1-DR-001: A`, будущий human-accepted Product Spec должен владеть cross-feature product facts, а каждый Feature Passport — только feature-specific behavior и ссылками на Product Spec.

Пока этот package не принят и не опубликован:

```yaml
product_spec_maturity: DRAFT
authority: NONE
feature_dispositions_mutated: false
implementation_readiness_claimed: false
```

## 2. Product problem

AOS решает не проблему «написать код вместо человека», а проблему управляемости AI-assisted development. Пользователь способен описать желаемый результат, но не обязан уметь контролировать каждую repository operation, permission, test, implementation detail и переход между tools/sessions.

| ID | Problem | User/system consequence |
|---|---|---|
| `P-001` | State распределён между chats, files, worktrees, reports и decisions | context теряется, planning повторяется |
| `P-002` | Непонятно, где работа остановилась | resume основан на stale assumptions |
| `P-003` | Free-form request смешивает problem, outcome и proposed solution | реализуется не та пользовательская потребность |
| `P-004` | Scope существует только в тексте или скрыто расширяется | contamination, difficult rollback, mistrust |
| `P-005` | PASS, Evidence, readiness и approval смешиваются | false completion и simulated acceptance |
| `P-006` | Implementation и validation выполняются одним субъектом без границы | hidden fixes и self-validation |
| `P-007` | Edit/Commit/Push/Merge/Release воспринимаются как одно действие | unauthorized publication/release |
| `P-008` | Legacy содержит полезное поведение и obsolete complexity | ошибочная target architecture |
| `P-009` | Exhaustive extraction имеет низкий ROI | product value отложена |
| `P-010` | Документы и views дублируют owners | drift и competing truth |
| `P-011` | Feature descriptions недостаточно конкретны | agent invents behavior, failures and tests |
| `P-012` | Install/update ownership неясен | потеря user/project state |
| `P-013` | Model/provider routing не измеряется | непредсказуемые cost, quality, privacy |
| `P-014` | Automation появляется до manual proof | автоматизирован плохой процесс |
| `P-015` | Blocker, limitation и next action непонятны | зависимость от specialist/operator |

## 3. Product promise

```text
пользователь описывает проблему или идею
→ AOS сохраняет original intent и показывает uncertainty
→ формирует reviewable product definition
→ отделяет planning от separately authorized work
→ связывает exact result с Evidence
→ человек принимает explicit decision
→ AOS сохраняет recoverable state и показывает one next action
```

### Value proposition by actor

| Actor | Value |
|---|---|
| Domain expert | управлять product outcome обычным языком и сохранять decision authority |
| Product builder | использовать разные coding agents без потери scope/state/safety |
| Implementer | получать достаточный contract и bounded work вместо догадок |
| Reviewer | видеть user impact, Evidence, limitations и remaining risk |
| Maintainer | воспроизводить state/rationale, находить drift и предотвращать recurrence |

## 4. Users and JTBD

### U-001 — Nonprogrammer / domain expert

**Primary job:** превратить знание предметной области в проверяемый product outcome, не становясь operator каждого engineering step.

**Needs:** plain-language intake; visible assumptions; material questions only; explicit human checkpoints; before/after review; understandable failure/recovery; resume.

**Must never be required to:** infer authority from status codes; inspect every code line; understand hidden repository state; remember every prior session.

### U-002 — Vibe-coder / product builder

**Primary job:** быстро создавать продукт с AI while retaining product intent and repository control.

**Needs:** safe defaults; exact scope; replaceable agents; source-linked project memory; focused Evidence; no accidental Git delivery.

### U-003 — AI agent / implementer

**Primary job:** выполнить ровно один понятный outcome по достаточным contracts.

**Needs:** exact subject; owner/source routing; allowed/forbidden boundary; acceptance and negative cases; unknown resolution; terminal report schema.

### U-004 — Reviewer / auditor

**Primary job:** независимо определить, соответствует ли candidate declared contracts, не исправляя его и не подменяя human decision.

**Needs:** frozen identity; provenance; check matrix; limitations/NOT_RUN; impact summary; reproducible locators.

### U-005 — Maintainer / operator

**Primary job:** сохранить health, continuity and recoverability проекта после множества sessions/releases.

**Needs:** current state; owner map; decision rationale; audit/incident records; drift signals; bounded recovery.

## 5. Intake profiles

| Input profile | Product behavior |
|---|---|
| Complete specification | preserve original; check missing/contradictory fields; expose added assumptions; prepare reviewable Spec/Passports; stop before protected decisions |
| Incomplete idea | run problem interview; separate pain/outcome from solution; record current workaround, success signals, constraints, non-goals, unknowns and sensitive concerns |
| Existing repository goal | add read-only identity/discovery only when repository facts are material; never infer permissions from repository presence |
| Correction to prior intent | bind exact prior revision; preserve original; create distinguishable corrected revision; invalidate dependent stale review |
| Sensitive/regulated request | establish data/provider/specialist boundary before dependent processing; core agent does not acquire domain authority |

Progressive depth is risk- and outcome-scaled:

- small reversible: goal, scope, observable result, focused check;
- medium feature: users, flow, states, acceptance, dependencies, regression;
- high/protected: full constraints, authority checkpoints, failure/recovery, rollback boundary;
- sensitive/regulated: data/provider boundary and specialist decision.

Exact thresholds remain `OPEN-DECISION`.

## 6. Product artifacts and ownership

| Artifact | Product purpose | Owner rule | Authority boundary |
|---|---|---|---|
| Intent Record (`C-001`) | preserve original request and reviewed product intent | exact source-bound revision; human confirmation explicit | confirmation is not feature/architecture/execution acceptance |
| Product Spec (`C-003`) | own cross-feature problem, actors, journeys, scope, constraints, metrics and acceptance | accepted `X1-DR-001: A`: Product Spec owns cross-feature facts | DRAFT/accepted Spec never authorizes execution |
| Feature Passport (`C-002`) | own feature-specific observable behavior | one accepted Passport per feature revision; links to Product Spec | inventory presence/disposition and behavior acceptance are separate |
| ADR (`C-004`) | record a material architecture choice | exact human-accepted decision record | DRAFT comparison has no selected option |
| Review Package (`C-011` view) | make exact candidate, Evidence, findings and options reviewable | derived from owners and bound subject | display/technical PASS is not decision |
| Project Memory/Handoff (`C-012`) | preserve continuity and one next action | derived, source-linked and freshness-checked | no independent product or permission authority |
| Product Feature Registry | index accepted/draft Passports | rebuildable derived index | never owns feature behavior independently |

## 7. Product boundaries and capability domains

### Product Runtime

- Problem/Intent Intake;
- read-only Discovery when needed;
- Product Spec and Feature Passport authoring;
- Status / Next / Details;
- Review Package and explicit decision capture;
- Project Memory and Handoff;
- First-Start/Tutor;
- optional Architecture Support and guided bootstrap.

### Development Factory

- Task Brief compiler;
- repository preflight and execution preview;
- scoped executor/adapters;
- validation and Evidence;
- Context Pack and handoff builders;
- lazy backlog/decomposition;
- later CI/release helpers and strict drift tools.

### Minimal Safety / Governance

Always-on boundaries: authority, permission, scope/path/Git, status semantics, stop rules and external-content distrust. Stronger enforcement is optional and must be admitted after measured incidents/need.

### Knowledge / Reference

Accepted documents, DRAFT/accepted Feature Passports, lessons, patterns, exact research findings and rebuildable navigation indexes.

### Optional Extensions

RAG-light, model routing, runtime enforcement, plugins, domain modules, workbench/SaaS, packaging/localization and extended observability. None is a prerequisite for first product value by default.

## 8. Product requirements

### Intent and definition

| ID | Requirement | Verification intent |
|---|---|---|
| `PR-001` | Preserve original human input and provenance | review can distinguish original from synthesis |
| `PR-002` | Separate problem/outcome from proposed solution | solution wording cannot erase underlying need |
| `PR-003` | Expose assumptions, constraints, non-goals and material unknowns | each unknown has affected boundary and route |
| `PR-004` | Ask only questions capable of changing outcome, scope, safety or routing | non-material clarification is not a blocker |
| `PR-005` | Require exact human confirmation for intent/product decisions | generated confirmation is invalid |
| `PR-006` | Produce Product Spec and feature-specific Passports with one-owner links | duplicate cross-feature facts are detected |

### Scope, authority and execution boundary

| ID | Requirement | Verification intent |
|---|---|---|
| `PR-007` | Describe future work through a bounded Task Brief | allowed/forbidden scope is reviewable |
| `PR-008` | Keep Task Brief separate from Execution Authorization | task presence cannot unlock mutation |
| `PR-009` | Bind protected authorization to exact subject/stage/paths/operations | stale or copied auth is rejected |
| `PR-010` | Show an exact preflight/preview before mutation | changed identity invalidates preview |
| `PR-011` | Reconcile intended and actual mutation | unexpected path/action becomes terminal finding |
| `PR-012` | Keep each protected run to one stage | no hidden validate/deliver transition |

### Evidence, review and decision

| ID | Requirement | Verification intent |
|---|---|---|
| `PR-013` | Bind Evidence to exact candidate and acceptance criterion | candidate byte change invalidates old Evidence |
| `PR-014` | Preserve `NOT_RUN`, limitations and remaining risk | required `NOT_RUN` cannot aggregate to PASS |
| `PR-015` | Separate authoring/correction from independent validation | validator mutation is detected |
| `PR-016` | Present concise before/after, scope, Evidence and findings | nontechnical reviewer understands impact |
| `PR-017` | Capture `ACCEPT/NEEDS_CHANGES/REJECT/DEFER` as human-authored exact record | UI/agent cannot simulate decision |

### Continuity and recovery

| ID | Requirement | Verification intent |
|---|---|---|
| `PR-018` | Reconstruct current status from authoritative sources and mutable observations | stale memory cannot show READY |
| `PR-019` | Show exactly one recommended next action and optional details | closure does not present ambiguous queue |
| `PR-020` | Preserve partial writes, findings, permissions and exact resume boundary | interruption can be recovered without guessing |
| `PR-021` | Block unsafe retry when scope/identity/permission/decision changed | retry requires rebind or human decision |

### Portability, safety and lifecycle

| ID | Requirement | Verification intent |
|---|---|---|
| `PR-022` | Keep adapters replaceable and sourced from common rules | adapter cannot add authority |
| `PR-023` | Treat external/legacy content as untrusted reference | injected instruction cannot change goal/scope |
| `PR-024` | Preserve user/project-owned state during install/update/remove | dry-run and ownership conflict behavior are explicit |
| `PR-025` | Keep Commit, Push, Merge and Release separately authorized | success of one cannot imply another |
| `PR-026` | Promote automation only after manual repetition and measured value | optional control can be disabled/removed |
| `PR-027` | Turn incidents into human-reviewed lesson/regression proposals | log cannot mutate canonical policy automatically |

## 9. Product qualities — `SYNTHESIZED_DRAFT`

These are reviewable quality requirements, not measured claims:

| Quality | Requirement |
|---|---|
| Comprehensibility | primary status/review is understandable without repository expertise |
| Traceability | accepted outcome traces to intent, contracts, candidate and Evidence |
| Safety | authority defaults closed; protected mutations require exact explicit permission |
| Recoverability | partial state and next route survive interruption |
| Portability | core semantics are independent of one agent/provider/interface |
| Maintainability | one owner per fact class; derived views rebuildable; legacy complexity excluded |
| Privacy | sensitive content stays within an explicitly selected data/provider boundary |
| Accessibility | state, errors and decisions are not color-only or jargon-only |
| Observability | material actions/results/limitations are explainable and subject-bound |
| Proportionality | ceremony and Governance grow with observed risk, not by default |

Targets, service levels and measurable thresholds remain human decisions.

## 10. Capability and feature map

| Capability group | Features | Current disposition summary |
|---|---|---|
| Intent and product definition | `FTR-001`, `FTR-003` | both `SELECT_FOR_X1`; behavior accepted in exact X1 fact classes |
| Discovery and bootstrap | `FTR-002`, `FTR-004` | `UNDECIDED` |
| Architecture/task controls | `FTR-005`, `FTR-006` | `SUPPORTING_CONTROL_ONLY` for X1 |
| Backlog and status UX | `FTR-007`, `FTR-008` | `UNDECIDED` |
| Preflight and scoped execution | `FTR-009`, `FTR-010` | `UNDECIDED` |
| Validation/review/freeze | `FTR-011`, `FTR-012`, `FTR-013` | `SUPPORTING_CONTROL_ONLY` for X1 |
| Recovery/delivery/continuity | `FTR-014`, `FTR-015`, `FTR-016` | `UNDECIDED` |
| Search/routing/trust | `FTR-017`, `FTR-018`, `FTR-019` | `UNDECIDED` |
| Governance/drift/patterns | `FTR-020`, `FTR-021`, `FTR-022` | `UNDECIDED` |
| CI/release/operations | `FTR-023`, `FTR-024`, `FTR-025` | `UNDECIDED` |
| Extensions/domains/UI/package/tools | `FTR-026…030` | `UNDECIDED` |

Detailed DRAFT behavior is in [04_FEATURE_SPECIFICATIONS.md](04_FEATURE_SPECIFICATIONS.md). Roadmap grouping does not change these dispositions.

## 11. Primary user journeys

| Journey | Observable outcome | Core features |
|---|---|---|
| `J-001` New project | exact human-confirmed intent, then decision-ready product definition | FTR-001, FTR-003 |
| `J-002` Existing-project discovery | snapshot-bound capability map and human-selected objective | FTR-002, FTR-009 |
| `J-003` One-feature development | exact feature outcome with Evidence and human decision | FTR-003, 005, 006, 009–013 |
| `J-004` Resume | trusted current status and one safe next action | FTR-008, 014, 016 |
| `J-005` Review and decision | candidate-bound verdict without reading all code | FTR-011–013 |
| `J-006` Protected delivery | separately authorized Commit/Push/Merge/Release | FTR-015, 019, 024 |
| `J-007` Targeted reconstruction | bounded evidence finding without legacy authority transfer | FTR-002, 005, 022 |

Full flow and UX requirements are in [05_USER_JOURNEYS_AND_UX.md](05_USER_JOURNEYS_AND_UX.md).

## 12. First Product Runtime slice

Exact accepted decision `X1-DR-002: A`:

```text
human request
→ FTR-001 preserves original input
→ separates problem/outcome from solution
→ exposes constraints/assumptions/unknowns
→ asks material questions
→ presents exact reviewable Intent Record
→ human confirms or corrects exact revision
```

This is the first Product Runtime vertical slice. It does not require FTR-003 in the same runtime slice, an implementation repository, Product Feature Registry, full Control Plane or implicit Git delivery. Implementation planning and repository binding remain separate and `NOT_RUN`.

## 13. Product acceptance model

### Documentation readiness

A product/feature document is reviewable when it covers actors, trigger, preconditions, semantic I/O, observable flow, states, failures/recovery, dependencies, authority boundaries, acceptance, negative cases, unknowns and source status.

### Product acceptance

```text
reviewable exact revision
→ exact technical audit when required
→ explicit human decision
→ accepted fact classes declared
```

Acceptance does not imply architecture acceptance, implementation readiness, execution permission or Git delivery.

### Future runtime outcome acceptance

A runtime outcome requires:

- exact accepted upstream product/feature contract;
- bounded authorized subject;
- acceptance criteria mapped to Evidence;
- visible `NOT_RUN`/limitations;
- explicit human verdict on exact candidate.

## 14. Candidate success measures — `PROPOSAL`

| Metric | Why it matters | Initial measurement form |
|---|---|---|
| intent-to-reviewable time | intake efficiency | elapsed time and clarification count |
| clarification quality | avoids over-questioning and wrong outcome | material questions / corrections |
| scope drift rate | boundary safety | unexpected changed paths/actions per task |
| resume time | continuity | time to correct next action after interruption |
| review time | accessibility of Evidence | time and clarification needed for verdict |
| false-green incidents | technical truthfulness | accepted findings where PASS was invalid |
| re-planning rate | quality of contracts/handoff | tasks restarted due to missing context |
| user comprehension | product usability | user explains state, risk and next action |
| lesson recurrence | continuous improvement | repeated incident after accepted regression |
| Governance overhead | proportionality | control time/effort vs risk reduction |
| maintainability | long-term cost | drift, duplicate owners and unsupported adapters |

No target values are selected in this DRAFT.

## 15. Product non-goals

- replace human product ownership or approval;
- optimize for maximum autonomous coding;
- promise a specific model/provider as permanent core;
- require a visual UI, cloud service or database for first value;
- make Governance/control artifacts the main user value;
- copy legacy architecture or claim compatibility without decision/Evidence;
- implement domain medical/legal decisions in neutral core;
- infer product scope from feature inventory or roadmap placement;
- hide unknowns to create apparent readiness;
- execute implementation or Git operations from documentation acceptance.

## 16. Material product decisions

Accepted:

- FTR-001 is the first Product Runtime slice;
- Product Spec owns cross-feature facts; Passports own feature behavior.

Still open:

- first commercial/user segment and first concrete job context;
- exact interface and onboarding surface;
- Product Feature Registry admission/presentation;
- scenario/access/UX pipeline timing;
- acceptance authenticity mechanism;
- install ownership model;
- metrics and thresholds;
- item-level feature dispositions beyond X1;
- compatibility target and distribution model.

Decision-ready options are in [07_DECISION_REGISTER.md](07_DECISION_REGISTER.md).

## 17. Product review checklist

- Do the problem and promise match the intended future project?
- Are target actors distinct enough for product and review design?
- Does the artifact ownership rule avoid duplicate truth?
- Are requirements user-observable and free of implementation HOW?
- Is the accepted first slice preserved without accidental scope expansion?
- Are all 30 features represented without changing dispositions?
- Are proposed metrics and roadmap clearly separate from accepted decisions?
- Are sensitive/provider, install, interface and compatibility gaps visible?
- Is there any statement that incorrectly grants implementation or Git authority?
