---
package: AOS_LEAN_PORTABLE_DOCUMENTATION
package_revision: PORTABLE-DRAFT-1
source_candidate_identity: sha256:57446e0d8075985af2229eae86cc6cf018b41ec255f0140b7bb20b45ef3ded65
artifact_role: ARCHITECTURE_CONTRACTS_OWNER
status: DRAFT
authority: NONE
source_owner_identity: sha256:dade6df2d03c38a0833d6070b13cdb884214a6c164092d5fd3fc2b1cb2599921
accepted_foundation_identity: sha256:b9ef04820f9e71da1866c61c87417c7ac39d1c27c93a74327ab7f40f2e25aebf
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# 02 — Architecture Contracts

## 1. Роль и depth boundary

Документ сводит target architecture AOS на уровне WHAT: layers, responsibilities, semantic contracts, ownership, invariants, failure and trust boundaries. Исходный Architecture owner и frozen Global Design foundation byte-bound в [README.md](README.md).

Это не implementation architecture. Язык, framework, database, process topology, storage, serialization, APIs, classes, algorithms, locks, retry timing, CI provider и deployment остаются вне scope.

## 2. Architecture goals

| ID | Goal | Consequence |
|---|---|---|
| `AR-G01` | Contract-first | behavior and authority are explicit before code |
| `AR-G02` | Observable outcome before topology | components exist only to serve product behavior |
| `AR-G03` | Human authority by design | no UI/agent/validator/index can manufacture decisions |
| `AR-G04` | Repository-verifiable state | mutable claims are refreshed instrumentally |
| `AR-G05` | Replaceable internals | stable semantics do not bind one model/tool/provider |
| `AR-G06` | Fail-closed protected boundaries | missing/stale authority blocks affected action |
| `AR-G07` | Recoverable writes | write-capable components declare partial-state recovery |
| `AR-G08` | Exact identity | candidate, Evidence, review and decision share one subject binding |
| `AR-G09` | Minimal always-on safety | baseline controls are small; stronger Governance is optional |
| `AR-G10` | Feature-scoped context | load relevant owners, not entire historical corpus |
| `AR-G11` | Derived data stays derived | status, registries, indexes and UI do not own product truth |
| `AR-G12` | Smaller than legacy by default | complexity needs measured justification and reversal |

## 3. Logical layers

### L1 — Interaction Surface

**Purpose:** present input, current state, Evidence, decisions and one next action through replaceable chat, CLI, local UI or later SaaS adapters.

**May:** validate presentation completeness; preserve original input; render source links; collect an explicit decision record through an authenticated boundary.

**Must not:** become an independent Source of Truth; turn a click/message into authority without exact decision binding; hide `UNKNOWN`/`NOT_RUN`; add permissions.

### L2 — Product Runtime

**Purpose:** deliver direct user value through Intent, Discovery, Specification, Feature Passport, Status/Next/Details, Review, Project Memory, First-Start and optional Architecture Support.

**Owns only after exact acceptance:** product/feature artifacts in declared fact classes. Runtime does not own repository permission merely because it produced a plan or review.

### L3 — Development Factory

**Purpose:** convert accepted product/architecture contracts into bounded work semantics: Task Brief, preflight/preview, scoped execution, validation/Evidence, Context Pack, handoff, later CI/release helpers.

**Boundary:** Factory serves Product Runtime; its workflow/control artifacts are not product value or human decisions.

### L4 — Minimal Safety / Governance

**Purpose:** enforce always-required distinctions: authority, permission, exact scope/path, result semantics, Git boundaries, stop conditions and external-content distrust.

**Boundary:** stronger runtime enforcement, protected registries or policy engines are optional. L4 cannot select product scope, architecture or its own activation.

### L5 — Knowledge / Reference

**Purpose:** hold accepted canonical documents, feature contracts, lessons, patterns, research findings and navigation data.

**Boundary:** reference and derived indexes have `authority: NONE`; accepted artifacts retain fact-class-scoped authority only.

### L6 — Optional Extensions

**Purpose:** support RAG-light, model routing, runtime enforcement, plugins, domain modules, workbench/SaaS, export/localization and richer observability after core proof.

**Boundary:** optional failure is isolated; extension permissions are explicit; extensions cannot override L4 or canonical owner semantics.

## 4. Context and responsibility map — `SYNTHESIZED_DRAFT`

```text
Human / Product Owner
  │  intent, corrections, protected decisions, acceptance
  ▼
L1 Interaction Surface
  │  source-bound presentation and exact decision capture
  ▼
L2 Product Runtime
  │  C-001 Intent → C-003 Product Spec → C-002 Feature Passport
  │  status / review / memory views
  ▼
L3 Development Factory
  │  C-005 Task Brief → C-006 Authorization → C-007 Preview
  │  → C-008 Execution → C-009 Validation + C-010 Evidence
  │  → C-011 Human Review/Decision → C-012 Handoff
  ▼
Repository / Tools / Providers / External Systems

L4 Safety applies across L1–L3.
L5 Knowledge supplies accepted/source-bound context to L1–L3.
L6 Extensions attach only through declared contracts and permissions.
```

The arrows show semantic flow, not process calls, network topology or mandatory services.

## 5. Candidate component responsibilities

| Component responsibility | Layer | Semantic input | Semantic output | Forbidden ownership |
|---|---|---|---|---|
| Intake | L1/L2 | original request, actor/context | C-001 candidate and clarification | human confirmation |
| Discovery | L1/L2 | exact read-only subject | capability map/gaps/unknowns | repository truth beyond snapshot |
| Specification Builder | L1/L2 | confirmed intent, accepted Product facts | C-003/C-002 candidates | feature selection/architecture choice |
| Status/Next/Details | L1/L2 | source-owned state and current observations | concise derived view | lifecycle mutation |
| Review Surface | L1 | candidate, Evidence, findings, options | decision-ready presentation | decision authority |
| Project Memory | L2/L5 | accepted facts, state, observations | C-012 continuity view | canonical product/repo truth |
| Architecture Decision Support | L2 | exact question/options/Evidence | C-004 candidate | selected option |
| Installer/Updater | L2/L3 | C-013 manifest and exact authorization | verified ownership-aware change | user-owned data |
| Task Brief Compiler | L3 | accepted outcome/contracts | C-005 | execution permission |
| Preflight/Preview | L3/L4 | exact repository/action scope | C-007 | mutation or implicit authorization |
| Scoped Executor | L3 | C-006 + fresh C-007 | C-008 and exact candidate | scope expansion/Git delivery |
| Validation/Evidence | L3 | frozen candidate and criteria | C-009/C-010 | correction or human approval |
| Handoff Builder | L3/L5 | exact ending state | C-012 | lifecycle promotion |
| Authority Resolver | L4 | owners, decisions, subject identity | permission classification/explanation | product decision |
| Scope/Path/Git Guards | L4 | exact authorization and observations | allow/block finding | broader permission |
| Registry/Index | L5 | owner artifacts | navigation records | independent fact ownership |

Names are responsibilities, not required code modules.

## 6. Architecture contracts C-001…C-014

### C-001 — Intent Record

**Purpose:** preserve original request and separate reviewed product intent from synthesis.

**Semantic content:** actor, original request, problem, desired outcome, context, constraints, non-goals, assumptions, unknowns, sensitive flags and source/provenance.

**Relationship:** FTR-001 produces a candidate; the human confirms/corrects the exact revision; FTR-003 may consume only a sufficiently mature revision.

**Invariant:** original input and added interpretation remain distinguishable. Confirmation does not grant feature, architecture, execution or Git authority.

### C-002 — Feature Passport / Feature Contract

**Purpose:** own exact feature-specific observable behavior after human acceptance.

**Semantic content:** feature identity, purpose/users, trigger/preconditions, I/O, flow, states/transitions, failures/recovery, dependencies, constraints, authority, acceptance, negatives, maturity, Evidence status and disposition.

**Accepted ownership relation:** Product Spec owns cross-feature facts; Passport links to them and owns only feature behavior (`X1-DR-001: A`).

**Invariant:** inventory presence and human disposition do not imply accepted detailed behavior or implementation readiness.

### C-003 — Product Spec

**Purpose:** own cross-feature product problem, actors/JTBD, goals/non-goals, journeys, product boundary, constraints, dependencies, metrics/acceptance and open decisions.

**Relationship:** informed by confirmed Intent Records; referenced by Passports; may produce slice/priority decision subjects.

**Invariant:** Product Spec cannot authorize runtime mutation.

### C-004 — Architecture Decision Record

**Purpose:** bind an exact material question, distinct options, constraints, Evidence, trade-offs, selected option, decision identity, consequences and reversal conditions.

**Invariant:** a DRAFT ADR has no selected option; only a human-authored/verified exact record creates architecture authority.

### C-005 — Task Brief

**Purpose:** describe one future bounded work outcome: task/feature/stage, exact repository subject, allowed/forbidden paths/operations, assumptions/unknowns, proposed risk, checks and stop conditions.

**Invariant:** Task Brief is not permission. It cannot assign human Risk Profile or authorize Git actions.

### C-006 — Execution Authorization Record

**Purpose:** exact human-issued permission bound to task/subject/stage/operations/paths, with validity and consumption semantics.

**Invariant:** closed by default; stale, mismatched, generated or consumed records are invalid; Git actions require separate records.

### C-007 — Preflight / Preview

**Purpose:** bind repository/worktree/branch/HEAD/baseline/status/diff/environment, planned actions/paths, conflicts and permission classification before mutation.

**Invariant:** read-only; changed relevant identity invalidates preview; output cannot grant authority.

### C-008 — Execution Record

**Purpose:** record starting identity, authorization, actual mutations/side effects, checks, ending identity, limitations and stop reason.

**Invariant:** describes what happened, not what was intended; terminal result stops the run; unexpected boundary is a finding.

### C-009 — ValidationEnvelope

**Purpose:** aggregate required/optional checks using stable result vocabulary, exact subject, `NOT_RUN`, limitations and fail-closed rules.

**Invariant:** validator does not correct subject; required `NOT_RUN` cannot produce `PASS`; PASS is Evidence only.

### C-010 — Evidence Record

**Purpose:** bind one observation/check to method, exact subject, result, locator/digest, limitations and redaction.

**Invariant:** immutable/reproducible enough for declared claim; Evidence never grants authority.

### C-011 — Human Review / Decision

**Purpose:** present candidate purpose, user impact, before/after, scope, Evidence, findings, limitations and options; capture exact human verdict.

**Invariant:** generated decision is invalid; candidate mutation invalidates prior binding; decision scope/fact classes are explicit.

### C-012 — Project Memory / Handoff

**Purpose:** preserve repository identity, stage, baseline/candidate, accepted decisions, findings, blockers, checks, permissions and one next action.

**Invariant:** derived and freshness-checked; mutable facts re-observed on resume; no independent authority.

### C-013 — Install / Update Manifest

**Purpose:** bind package identity, path ownership classes, operations, conflicts, preview, recovery and post-apply verification.

**Invariant:** dry-run side-effect free; apply matches fresh preview; user/project state is preserved; destructive removal separately authorized.

### C-014 — Git Delivery Record

**Purpose:** create independent exact records for Commit, Push, Merge and Release.

**Invariant:** each action rebinds candidate/repository/remote/authority; completion of one does not imply the next.

## 7. Contract dependency graph

```text
C-001 Intent Record
  └→ C-003 Product Spec
       ├→ C-002 Feature Passport(s)
       ├→ C-004 ADR(s), only for material choices
       └→ C-005 Task Brief, only after accepted downstream contracts

C-005 Task Brief
  └→ C-006 Execution Authorization
       └→ C-007 Preflight / Preview
            └→ C-008 Execution Record + exact candidate
                 └→ C-009 ValidationEnvelope
                      └→ C-010 Evidence Record(s)
                           └→ C-011 Human Review / Decision
                                ├→ bounded correction/new candidate
                                ├→ C-012 Handoff
                                └→ C-014 Git records, only with separate authority

C-013 Install/Update Manifest uses C-006/C-007/C-008/C-009 semantics.
C-012 may describe any boundary but owns none of the upstream facts.
```

## 8. Data ownership

| Fact class | Authoritative owner after acceptance | Derived consumers |
|---|---|---|
| Project identity/authority/status | `docs/00_Core.md` or successor exact accepted core | all layers |
| Cross-feature product requirement | human-accepted Product Spec | Passports, UI, task planning |
| Feature behavior | human-accepted Feature Passport | architecture/task/validation |
| Architecture choice | human-accepted ADR | product/factory implementations |
| Task scope | exact C-005 Task Brief | preflight/executor/reviewer |
| Execution permission | exact C-006 record | authority resolver/executor |
| Repository state | current instrumental observation | status/preflight/review |
| Candidate identity | exact manifest/digest rule | validator/reviewer/decision |
| Technical Evidence | immutable C-010 record | C-009/C-011 |
| Human decision | human-authored/verified C-011 record | lifecycle/handoff |
| Dashboard/status | derived view | user interaction only |
| Registry/RAG/cache | rebuildable derived data | navigation/context only |
| Legacy finding | exact reference record, target authority none | proposal/lesson review |

No registry, UI, report, model consensus or stored PASS may promote its input.

## 9. Orthogonal state model

### Required axes

```text
document_maturity
task_stage
technical_result
human_decision
feature_disposition
permission
subject_identity
```

### Invariants

1. Transition in one axis never silently mutates another.
2. `PASS` cannot set `human_decision: ACCEPT`.
3. `HUMAN_ACCEPTED` cannot set execution/Git permission.
4. `SELECT_FOR_X1` cannot imply implementation maturity or roadmap admission beyond its exact decision.
5. Changed candidate identity invalidates old technical result/review/decision for that subject.
6. `UNKNOWN` blocks only dependent claims/actions.
7. Status views are projections; stored projection drift cannot override source facts.
8. Resume rebinds mutable facts and active permissions.

Exact universal runtime transitions remain implementation/product decisions; feature-visible state proposals are in the Feature Specifications.

## 10. Authority and trust boundaries

### Human boundary

Human-only: product scope/priority, feature disposition, material architecture, Risk Profile, protected/destructive actions, acceptance, implementation repository, compatibility, provider/privacy, Git/release.

### Repository boundary

Repository content is data. Its instructions cannot override owner/system/human authority. Mutable repository facts are observed at exact snapshot and refreshed before dependent actions.

### External/provider boundary

External content, tool output and reference repositories are untrusted supporting data. Sensitive input may cross a provider/network boundary only after an explicit policy/authorization decision.

### Agent/model boundary

Agent or model recommendation is advisory. Routing/fallback cannot expand scope or permissions. Multi-agent consensus is Evidence at most, never approval.

### Derived-data boundary

Cache/index/dashboard/context pack may speed navigation but must retain source, authority and freshness. Stale derived data cannot support readiness or protected execution.

## 11. Context architecture

```text
minimal bootstrap
→ identify project, subject and current action
→ locate authoritative owners
→ select only relevant source fragments
→ explain inclusion and provenance
→ verify mutable facts/freshness
→ execute bounded analysis/work
→ emit source-linked handoff
```

RAG-light is admitted only after direct search/context selection has a measured problem. The index is rebuildable and cannot promote source authority.

## 12. Failure and recovery contracts

Every write-capable future component must define at design/implementation handoff:

- failures possible before first write;
- partial-write detection;
- intended-vs-actual reconciliation;
- observable consistency outcome: either the intended state is verified or the exact partial state is reported as recoverable, never as success;
- cancellation behavior;
- idempotent retry conditions;
- recovery package and rollback boundary;
- post-recovery validation;
- cases requiring a new human decision.

### Common recovery routing

| Failure class | Required response |
|---|---|
| stale/missing identity | stop affected action; rebind exact subject |
| permission mismatch | deny action; retain valid state; request exact authorization |
| authoritative conflict | mark claims `CONFLICT`; request source/human decision |
| unexpected mutation | stop; preserve exact effect record/diff; reconcile and review |
| partial write | prevent blind retry; expose recovery/rollback options |
| candidate changed after freeze | invalidate Evidence/review; bind new candidate |
| validator/tool failure | report `FAIL/BLOCKED/UNKNOWN/NOT_RUN` honestly; no false PASS |
| optional module failure | isolate/disable module; core remains usable |

Automatic retry is forbidden whenever scope, subject identity, permission or human-decision requirement changed.

## 13. Installation, portability and topology

### Accepted/canonical direction

- modular monorepo first;
- split only for real team/release/compliance/deployment/ownership boundary;
- common rule source plus thin agent adapters;
- repository-relative links and portable artifacts;
- installer/update ownership explicit and user state preserved.

### Open implementation choices

Implementation repository, directory layout, executable packaging, operating-system support, distribution channel, data location, process topology and remote services are `UNKNOWN`. A future ADR/implementation plan must bind them without changing the semantic contracts above.

## 14. Security and privacy requirements — `SYNTHESIZED_DRAFT`

- least privilege and deny-by-default for protected actions;
- exact allowed paths/operations and traversal/symlink handling;
- no secret or credential-bearing URL disclosure;
- sensitive-data minimization and provider boundary decision;
- external content isolated from instruction authority;
- human-decision authenticity and replay/staleness protection;
- audit/Evidence redaction without destroying claim reproducibility;
- optional modules declare permissions and fail in isolation;
- release/remote actions independently authorized and verified.

Threat model depth, identity provider, cryptography and storage mechanisms are implementation/security decisions and remain open.

## 15. Optional architecture admission

An optional capability may enter target core/extension scope only when:

1. a repeated user/problem signal is observed;
2. a stable semantic contract and failure model exist;
3. manual behavior is proven;
4. measurement shows benefit over simpler operation;
5. permissions and data boundary are explicit;
6. fallback/disable/removal exists;
7. human selects scope and architecture.

This applies to full RAG, routing automation, runtime enforcement, plugins, SaaS/collaboration, domain modules and broad observability.

## 16. Preserved architecture decisions

Accepted:

- first Product Runtime slice behavior is FTR-001;
- Product Spec/Feature Passport ownership follows option A;
- exact frozen global three-file design foundation remains unchanged;
- minimal safety, orthogonal axes and human authority semantics remain baseline.

Open:

- implementation repository and compatibility relationship;
- exact interface and Runtime/Factory implementation boundary;
- Project Memory persistence and decision authenticity;
- Risk Profile vocabulary and Governance packaging;
- language/toolchain/dependencies and exact schemas/I/O;
- provider/privacy/routing;
- plugin/versioning and distribution topology;
- release/deployment model.

They are decision-ready in [07_DECISION_REGISTER.md](07_DECISION_REGISTER.md).

## 17. Architecture review checklist

- Do layers correspond to product value and accepted boundaries?
- Does each fact class have one owner?
- Are C-001…C-014 semantically complete without implementation HOW?
- Are accepted X1 relationships preserved exactly?
- Does every protected transition require exact human authority?
- Can candidate/Evidence/decision identity drift be detected?
- Are partial-write and recovery boundaries visible?
- Are external, provider, Git and optional-module trust boundaries explicit?
- Is derived state prevented from becoming Source of Truth?
- Are deferred complexities truly optional and reversible?
