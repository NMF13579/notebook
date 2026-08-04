---
artifact_id: AOS3-DPKG-DOC-001
artifact_type: PRODUCT_AND_CORE_V1_SCOPE
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R7
status: DRAFT_SOURCE_WITH_PARTIAL_C1_ACCEPTANCE
authority: PROPOSAL_WITH_HUMAN_DECISION_INPUTS
exact_subject: AOS first user, job, outcomes, ordered Core v1 scope, non-goals, product owner boundaries, and first-slice product contract
created: '2026-07-30'
human_acceptance: C1_ACCEPTED_126_CURRENT_11_STALE_10_NEW_AC_AND_2_NEW_SCHEMA_DRAFT
provenance:
  - path: ../../docs/00_Core.md
    use: identity, authority, safety, and strategic sequence
  - path: ../../docs/01_Product.md
    use: canonical users, problems, journeys, and product boundaries
  - path: ../../docs/02_Architecture.md
    use: C-001 Intent Record, C-002 Feature Passport, and C-003 Product Spec classes
  - path: ../../docs/06_Features.md
    use: FTR-001, FTR-002, FTR-003, FTR-005, FTR-008, FTR-016, and FTR-019 dossiers
  - path: decisions/DEC-PROD-001_First_User_and_Job.md
    use: accepted first user and job
  - path: decisions/DEC-PROD-002_Observable_Outcome.md
    use: accepted first-slice outcome
  - path: decisions/DEC-PROD-003_Core_V1_Slice_Sequence.md
    use: accepted A to B to C sequence
  - path: decisions/DEC-PROD-004_Core_V1_Scope_and_Non_Goals.md
    use: accepted scope boundary
  - path: decisions/DEC-PROD-005_Product_Spec_and_Feature_Passport_Relation.md
    use: accepted artifact ownership
  - path: research/RSR-001_AgentOS_Interview_and_Product_Spec.md
    use: non-authoritative interview and Product Spec evidence
upstream_links:
  - 00_Control_and_Source_Precedence.md
  - decisions/DEC-PROD-001_First_User_and_Job.md
  - decisions/DEC-PROD-002_Observable_Outcome.md
  - decisions/DEC-PROD-003_Core_V1_Slice_Sequence.md
  - decisions/DEC-PROD-004_Core_V1_Scope_and_Non_Goals.md
  - decisions/DEC-PROD-005_Product_Spec_and_Feature_Passport_Relation.md
downstream_links:
  - 02_User_Journeys_and_Workflows.md
  - 03_Architecture_and_Decisions.md
  - 04_Runtime_and_Data_Contracts.md
  - 06_Traceability_and_Readiness.md
  - decisions/G2_ARCHITECTURE_OPTION_PACKAGE.md
limitations:
  - Authored DRAFT labels in the C1-frozen subject definitions remain historical; DEC-CONTRACT-001 owns their effective acceptance.
  - PSC-A-001 changed in DRAFT-R9 only by removal of its redundant scalar authority field; its historical C1 binding is stale while its operational authority map remains the sole authority field.
  - G1 accepts product direction and boundaries, not individual FTR dispositions or implementation contracts.
  - G2 accepted bundle A and the interaction surface; the later human clarification keeps documentation in NMF13579/notebook, forbids repository creation now, and leaves implementation_repository UNASSIGNED.
  - Task candidates remain unaccepted; all runtime behavior remains unimplemented and unverified.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# 01 — Product and Core v1 Scope

## 1. Status boundary

This owner translates exact G1 decisions into a reviewable product contract. It does not self-accept its requirements; `DEC-CONTRACT-001` owns their exact C1 acceptance.

```yaml
document_status: DRAFT_SOURCE_WITH_PARTIAL_C1_ACCEPTANCE
document_authority: PROPOSAL_WITH_HUMAN_DECISION_INPUTS
g1_decision_status: HUMAN_DECIDED
g2_architecture_status: HUMAN_DECIDED_WITH_IMPLEMENTATION_REPOSITORY_DEFERRED
product_contract_acceptance:
  current_accepted_subjects: 126
  stale_product_contract_subjects: [PSC-A-001]
  decision_owner: DEC-CONTRACT-001
implementation_readiness: false
implementation_authorization: NONE
git_authorization: NONE
```

## 2. Human-decided product facts

| Decision | Accepted exact subject | Authority |
|---|---|---|
| [`DEC-PROD-001`](decisions/DEC-PROD-001_First_User_and_Job.md) | First user: non-programmer/domain expert; job: convert ambiguous intent into a reviewable product boundary | `HUMAN_DECISION` |
| [`DEC-PROD-002`](decisions/DEC-PROD-002_Observable_Outcome.md) | Reviewed DRAFT Product Spec and Feature Passport with visible uncertainty and one decision request | `HUMAN_DECISION` |
| [`DEC-PROD-003`](decisions/DEC-PROD-003_Core_V1_Slice_Sequence.md) | Ordered Core v1 direction `A → B → C`; A is the only first slice | `HUMAN_DECISION` |
| [`DEC-PROD-004`](decisions/DEC-PROD-004_Core_V1_Scope_and_Non_Goals.md) | Core v1 scope and exclusions | `HUMAN_DECISION` |
| [`DEC-PROD-005`](decisions/DEC-PROD-005_Product_Spec_and_Feature_Passport_Relation.md) | Product Spec and Feature Passport have separate fact ownership | `HUMAN_DECISION` |
| [`DEC-PROD-006`](decisions/DEC-PROD-006_RMP_004_005_Boundaries.md) | Keep `RMP-004` and `RMP-005` unsplit until a material boundary appears | `HUMAN_DECISION` |

None of these decisions changes `human_disposition` in canonical `FTR-001..030`.

## 3. First user and job

### Primary user

A non-programmer or domain expert who knows the problem domain and desired outcome but cannot safely control every repository, implementation, validation, provider, or Git detail.

### Job to be done

```text
When I have an incomplete or solution-shaped idea,
help me preserve what I actually said,
identify only material gaps,
and produce a reviewable product boundary
so that I can remain the decision owner without learning the internal machinery.
```

### Secondary users

- product builder who will later use an accepted contract to obtain one bounded Task Brief;
- AI agent that must operate without chat history;
- reviewer who needs provenance, unknowns, non-goals, and exact decision boundaries;
- maintainer who later resumes actual state and needs one safe next action.

Secondary users do not redefine the first slice.

## 4. Product problem

Current AI-assisted development commonly fails before implementation:

1. raw intent is rewritten as an assumed solution;
2. missing information is silently completed;
3. Product Spec, feature behavior, Task scope, execution permission, validation, acceptance, and Git authority collapse into one status;
4. context is trapped in chat;
5. optional automation is treated as Core necessity;
6. the user cannot identify the current blocker or one safe next action.

AOS Core v1 must reduce this coordination and authority cost before adding broad automation.

## 5. Product promise

AOS Core v1 provides an inspectable path:

```text
A — intent to reviewed product draft
→ B — accepted contract to bounded Task candidate
→ C — actual project state to one safe next action
```

The promise is not autonomous delivery. The promise is that each step preserves intent, state, scope, provenance, human authority, and an explicit stop.

## 6. Ordered Core v1 scope

### Slice A — `SLICE-A-INTENT-TO-REVIEW`

Status: `FIRST_SLICE_SELECTED`

In scope:

- preserve original user input;
- identify actor, problem, desired outcome, constraints, non-goals, assumptions, unknowns, and sensitive-data flags;
- ask only material clarification questions;
- distinguish `MISSING`, `UNKNOWN`, explicit `NONE`, and confirmed fact;
- produce a DRAFT Product Spec;
- produce at least one feature-specific DRAFT Feature Passport when a feature boundary exists;
- show sources, limitations, conflicts, and one decision request;
- stop at human product review.

### Slice B — `SLICE-B-CONTRACT-TO-TASK`

Status: `PLANNED_AFTER_ACCEPTED_UPSTREAM_CONTRACTS`

In scope direction:

- evaluate eligibility from accepted requirement/contract/scenario IDs;
- compile one bounded Task Brief candidate;
- show allowed/forbidden scope, checks, dependencies, and blockers;
- stop before execution authorization.

Slice B is not eligible while its source contract is `DRAFT`.

### Slice C — `SLICE-C-SAFE-RESUME`

Status: `PLANNED_AFTER_G2_PROJECT_MEMORY_DECISION`

In scope direction:

- bind actual repository/project identity read-only;
- recover accepted decisions, candidate identity, findings, blockers, checks, and permissions;
- detect stale or conflicting state;
- show one safe next action;
- stop before mutation or retry.

## 7. Scope-to-Roadmap mapping

| Product direction | Primary Roadmap items | Relationship |
|---|---|---|
| Slice A | `RMP-001`, `RMP-004` | Product boundary, intake, reviewed DRAFT specification |
| Slice B | `RMP-005` with dependencies on accepted `RMP-004` contracts | Task format and derived queue eligibility |
| Slice C | `RMP-008` with supporting `RMP-002`, `RMP-004`, `RMP-007` facts | Recovery, resume, and one safe next action |
| Cross-cutting safety | `RMP-006`, `RMP-007` | Authority, validation, Evidence, and human decision boundaries |
| Bootstrap | `RMP-002`, `RMP-003` | Remains dependent on G2 repository/toolchain/interface decisions |

This mapping is traceability, not implementation order or task admission.

## 8. Core v1 non-goals

- implementation inside the knowledge repository;
- automatic architecture, repository, language, dependency, provider, Risk Profile, or compatibility selection;
- Task generation from DRAFT or unaccepted contracts;
- automatic Task activation, execution, validation-to-correction transition, or retry;
- full backlog scheduling, forecasting, autonomous runner, or Control Plane;
- RAG/vector backend as a Core dependency;
- SaaS, marketplace, full dashboard, multi-agent orchestration, plugins, domain modules, and observability platform;
- automatic Commit, Push, Merge, Release, deployment, or publication;
- wholesale compatibility with AOS-FARM, AgentOS, or AOS-02.

## 9. Optional capability dispositions

These dispositions apply only within this package proposal and do not modify canonical feature decisions.

| Capability | Package disposition | Reason |
|---|---|---|
| RAG-light/context index | `DEFERRED` | No measured retrieval problem for first slice |
| Model routing | `DEFERRED` | Requires measurements and provider boundary |
| Progressive Governance beyond Minimal Safety Floor | `DEFERRED` | Manual product flow must be proven first |
| Plugins/extensions | `DEFERRED` | No first-slice dependency |
| Domain modules | `REFERENCE_ONLY` | First user is a domain expert, but domain-specific runtime is outside Core |
| Workbench/SaaS | `DEFERRED` | Interface and operational model remain G2 |
| Broad multi-agent orchestration | `DEFERRED` | Single-writer documentation and bounded read-only review are sufficient |
| Legacy topology and milestone systems | `REFERENCE_ONLY` | Evidence source only, authority `NONE` |

Optional capabilities cannot enter the Core v1 task queue without a later human decision and accepted upstream contract.

## 10. Product artifact ownership

### Product Spec

Owns:

- product problem and users;
- product-level JTBD, outcomes, scope, and non-goals;
- cross-feature journeys and constraints;
- product metrics, risks, dependencies, and open decisions;
- references to applicable Feature Passports.

### Feature Passport

Owns exactly one feature:

- identity, purpose, actors, trigger, and preconditions;
- inputs, outputs, behavior, states, and transitions;
- failures, recovery, constraints, dependencies, and authority;
- acceptance and negative scenarios;
- maturity, Evidence state, and human disposition.

### Relationship invariant

```text
Product Spec reference to Feature Passport ≠ Feature Passport acceptance
Feature Passport proposal ≠ Product Spec scope expansion
Duplicate claim → declared owner wins; conflict remains visible
```

Physical storage remains a G2 decision. Logical ownership is fixed by `DEC-PROD-005`.

## 11. C1-accepted product requirement register

The rows below were authored as `SYNTHESIZED`/`DRAFT` and are preserved byte-for-byte; their exact effective acceptance is owned by `DEC-CONTRACT-001`.

| Requirement ID | Requirement | First evidence of satisfaction |
|---|---|---|
| `REQ-CV1-001` | Preserve original input byte-for-byte or with an explicit transport-normalization record | Output contains source input or immutable locator and digest |
| `REQ-CV1-002` | Separate confirmed facts, assumptions, unknowns, explicit `NONE`, conflicts, and proposals | Each claim carries a class and source |
| `REQ-CV1-003` | Ask only questions that materially affect outcome, scope, safety, authority, or acceptance | Each question declares affected field/action |
| `REQ-CV1-004` | Produce a DRAFT Product Spec with product owner fields and open decisions | Schema-level review finds all required product fields |
| `REQ-CV1-005` | Produce a feature-specific DRAFT Feature Passport for each selected feature boundary | Passport contains actor through negative scenarios |
| `REQ-CV1-006` | Stop at human review without architecture, Task, execution, or Git authority | Output contains exact non-grants and one decision request |
| `REQ-CV1-007` | Compile Tasks only from human-accepted requirement/contract/scenario IDs | A DRAFT source produces `BLOCKED_DRAFT_UPSTREAM` |
| `REQ-CV1-008` | Resume from source-owned state and detect stale identity | Changed source/hash prevents current-state claims |
| `REQ-CV1-009` | Show exactly one safe next action and its required authority | Status view exposes one action or an explicit no-action blocker |
| `REQ-CV1-010` | Keep portable core independent of agent adapter | Replacing the adapter leaves core contracts unchanged |
| `REQ-CV1-011` | Keep optional capabilities outside the Core task queue by default | Deferred dossier cannot become Task input |
| `REQ-CV1-012` | Preserve implementation repository as `UNASSIGNED` until a separate exact human repository binding | No document treats the documentation repository or a placeholder as implementation identity |

## 12. First-slice product contract

```yaml
contract_id: PSC-A-001
revision: R2
status: DRAFT_UNACCEPTED_IN_DRAFT_R9
previous_acceptance: STALE_BY_SUBJECT_CHANGE
exact_subject: Intent to reviewed DRAFT Product Spec and Feature Passport
actor:
  primary: non-programmer or domain expert
  supporting:
    - documentation or product agent
    - human reviewer
trigger:
  User provides an idea, problem statement, or incomplete product/feature request
  and asks AOS to make it reviewable.
preconditions:
  - current product authority sources are identifiable
  - input boundary and sensitive-data handling are explicit
  - no implementation or Git authority is assumed
inputs:
  - original user input
  - known project/product context
  - explicit constraints and non-goals when provided
  - relevant accepted decisions
outputs:
  - Intent Record candidate
  - DRAFT Product Spec
  - one or more DRAFT Feature Passports by the human-review terminal; zero is allowed only before a feature boundary is identified
  - gap/conflict register
  - human review package with one decision request
states:
  - INTAKE_DRAFT
  - NEEDS_CLARIFICATION
  - READY_FOR_SPEC_DRAFT
  - SPEC_DRAFT
  - HUMAN_REVIEW_REQUIRED
side_effects:
  - documentation artifacts only inside an explicitly authorized path
authority:
  agent_may:
    - preserve and classify input
    - propose questions, requirements, and contracts
    - report gaps and recommend a next action
  human_only:
    - answer material product questions
    - accept product scope or contract revision
    - select architecture, implementation repository, execution, and Git actions
failures:
  - code: EMPTY_OR_UNUSABLE_INPUT
    effect: remain INTAKE_DRAFT
  - code: MATERIAL_INFORMATION_MISSING
    effect: enter NEEDS_CLARIFICATION
  - code: SOURCE_CONFLICT
    effect: block only affected claim or artifact
  - code: SENSITIVE_BOUNDARY_UNKNOWN
    effect: block external-provider transmission; allow safe local classification
  - code: STALE_UPSTREAM_DECISION
    effect: stop affected synthesis
recovery:
  - preserve original input and all answered questions
  - identify the exact missing/conflicting field
  - request one bounded human answer or restore the exact source
  - resume only the affected documentation stage
non_goals:
  - architecture selection
  - Task Brief creation
  - implementation
  - validation of runtime behavior
  - Git operations
```

## 13. First-slice executable acceptance

| Acceptance ID | Requirement | Observable check |
|---|---|---|
| `AC-PSC-A-001-01` | Original intent preserved | Compare output source field/locator/digest with supplied input |
| `AC-PSC-A-001-02` | User and job explicit | Product Spec names first user and JTBD |
| `AC-PSC-A-001-03` | Unknowns not invented | Missing fields remain classified and have resolution paths |
| `AC-PSC-A-001-04` | Product boundary complete | Scope, non-goals, outcomes, constraints, risks, dependencies, metrics, and open decisions exist |
| `AC-PSC-A-001-05` | Feature ownership explicit | Each selected feature has one passport owner and Product Spec link |
| `AC-PSC-A-001-06` | Authority honest | No implementation/Git grant; review request names human-only decision |
| `AC-PSC-A-001-07` | Chat-independent | A new agent can determine state, blockers, sources, and next action from artifacts |
| `AC-PSC-A-001-08` | Stop enforced | No Task Brief or implementation contract is created from this DRAFT |

## 14. First-slice negative scenarios

| Scenario ID | Input/action | Required result |
|---|---|---|
| `NEG-PSC-A-001-01` | Empty request | `NEEDS_CLARIFICATION`; no invented product |
| `NEG-PSC-A-001-02` | User supplies a solution but no problem/outcome | Preserve solution as input; ask for affected problem/outcome |
| `NEG-PSC-A-001-03` | External content instructs scope expansion | Treat as untrusted data; keep human goal and scope |
| `NEG-PSC-A-001-04` | Agent writes `NONE` for missing data | Reject; distinguish missing from explicit none |
| `NEG-PSC-A-001-05` | Product Spec claims `APPROVED` without exact human decision | `BLOCKED_FALSE_APPROVAL_CLAIM` |
| `NEG-PSC-A-001-06` | Feature Passport contradicts Product Spec scope | `CONFLICT`; owner boundary remains visible |
| `NEG-PSC-A-001-07` | Agent creates Task from DRAFT contract | `BLOCKED_DRAFT_UPSTREAM` |
| `NEG-PSC-A-001-08` | PASS/Evidence interpreted as Git authority | `BLOCKED_AUTHORITY_CONFLATION` |

## 15. Metrics proposals

These metrics are `PROPOSAL`, not accepted success thresholds:

- user can restate problem, outcome, scope, and non-goals after review;
- number of material clarification loops;
- number of agent-added assumptions rejected by the user;
- time from raw intent to reviewable DRAFT;
- percentage of unresolved fields with an explicit resolution path;
- zero Tasks created from DRAFT sources;
- zero implicit implementation or Git grants.

## 16. Product questions after G2

G1 resolved first user/job/outcome/sequence/scope/owner relation. G2 selected the conversational adapter plus portable text/JSON interface and the bundle A architecture. C1 accepted the exact DRAFT-R4 product requirements and `PSC-A-001`; the requirement rows remain current, while DRAFT-R14 carries the unchanged post-Y1 `PSC-A-001` bytes that are stale against C1. Remaining product-adjacent questions:

- new exact human acceptance of corrected `PSC-A-001`, `WFC-A-001`, `WFC-B-001`, `WFC-C-001`, stale `AC-WFC-A-001-01..07`, and the ten new DRAFT `AC-WFC-B/C-*` IDs after DRAFT-R14 validation/review;
- human disposition for the two new shared DRAFT `SCH-PRODUCT-SPEC-001`/`SCH-FEATURE-PASSPORT-001` schemas before they can become normative Task inputs;
- initial Product Feature Registry necessity;
- whether Slice C recovery UX is part of the same surface or a later adapter.

The implementation repository is intentionally deferred. Physical repository paths, dependencies, commands, and execution remain blocked by `DEC-ARCH-001`; portable documentation and, after contract acceptance, portable Task candidates remain in `notebook`.

## 17. One next action

```yaml
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
