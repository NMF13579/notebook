---
artifact_id: AOS-PRODUCT-RUNTIME-FOUNDATION-PACKAGE-R1
document_type: PRODUCT_RUNTIME_FOUNDATION_PACKAGE
revision: R1
status: DRAFT
task_id: INT-DOC-100
execution_id: INT-DOC-100-CORRECTION-003
source_execution_id: INT-DOC-100-EXECUTE-001
stage: EXECUTE
fact_class: SYNTHESIZED
scope_profile: SCOPE-A-CONTRACT-ONLY
scope_decision:
  actor_class: HUMAN
  decision: SCOPE-A_CONTRACT_ONLY
  runtime_turn_id: 019fc222-6932-7aa3-9495-ccf27ac667da
  exact_visible_utf8_text: "HUMAN_DECIDE_INT_DOC_100_FOUNDATION_SCOPE: SCOPE-A_CONTRACT_ONLY"
  utf8_byte_length: 64
  sha256: 8fe85f2b5a1d518ea32a0912f32aecdb3502ba5a7fc0e2e67fad58907c4a769a
  prior_reported_selection:
    classification: REPORTED
    runtime_turn_id: 019fc07c-2884-7030-b51a-29fca987c42a
    complete_source_byte_length: 306
    complete_source_sha256: 1beb6d1632b59f20f641d6467e130652b297d122afb6285684c83827aaf1ceaf
    selected_text: Выбираю SCOPE-A
    selected_text_sha256: 36e59de3508c649ca361002aa6335e47604a05be1c10e727a3502f63b6d1ead8
    authority_effect: NONE
execution_authorization:
  actor_class: HUMAN
  authorization_id: INT-DOC-100-CORRECTION-003
  runtime_turn_id: 019fc223-44cb-7f02-89dd-597f0293d5fc
  operation: PROVENANCE_CORRECTION_ONLY
  allowed_paths:
    - planning/foundation/AOS_Product_Runtime_Foundation_Package_R1.md
  one_shot: true
  exact_visible_utf8_text: >-
    AUTHORIZE INT-DOC-100-CORRECTION-003; decision_turn_id=019fc222-6932-7aa3-9495-ccf27ac667da;
    decision_sha256=8fe85f2b5a1d518ea32a0912f32aecdb3502ba5a7fc0e2e67fad58907c4a769a;
    candidate_sha256=d01f665aba6010768d84a272f97c38be539c592e49f9a90dfb771ef209ebfe04;
    stage_report_sha256=c61ca4eafbe89bab9aa9ec787ee50619df4ebab782d8cc8bbfe38f4e50025594;
    validation_id=INT-DOC-100-VALIDATE-002-SEM;
    finding_ids=INT-DOC-100-VALIDATE-002-SEM-F001,INT-DOC-100-VALIDATE-002-SEM-F002;
    allowed_path=planning/foundation/AOS_Product_Runtime_Foundation_Package_R1.md;
    operation=PROVENANCE_CORRECTION_ONLY; one_shot=true
  utf8_byte_length: 599
  sha256: 18fa1b288b8fbb162419c08baabd088d35b21594c4dab4130f46055757b8193f
  bound_input_candidate_sha256: d01f665aba6010768d84a272f97c38be539c592e49f9a90dfb771ef209ebfe04
  bound_input_stage_report_sha256: c61ca4eafbe89bab9aa9ec787ee50619df4ebab782d8cc8bbfe38f4e50025594
  bound_validation_id: INT-DOC-100-VALIDATE-002-SEM
  bound_finding_ids:
    - INT-DOC-100-VALIDATE-002-SEM-F001
    - INT-DOC-100-VALIDATE-002-SEM-F002
historical_execution_instruction:
  classification: UNKNOWN
  exact_visible_utf8_text: Выполняй
  utf8_byte_length: 16
  sha256: 310bb9610be06245e1e025b9e7000c2b0724e8c6085bec865079b69007f7d74b
  limitation: The literal instruction does not independently bind task and scope in a cold start.
  authority_effect_for_current_correction: NONE
correction_basis:
  validation_id: INT-DOC-100-VALIDATE-002-SEM
  validation_result: FAIL
  final_packet_identity_sha256: 63c06fc27ef04e57057867e71d4f4cf95e3505402ffa978d38a213eecee5a040
  admitted_finding_ids:
    - INT-DOC-100-VALIDATE-002-SEM-F001
    - INT-DOC-100-VALIDATE-002-SEM-F002
source_roadmap:
  path: planning/AOS_Documentation_Task_Sequence_R9.md
  sha256: be91cbffcd2c79a0a632b661157e5e2e7fb7a68d1056ba1c9684f2ea1b549ee7
feature_refs: [FTR-004, FTR-008, FTR-011, FTR-014, FTR-016, FTR-019]
output_path: planning/foundation/AOS_Product_Runtime_Foundation_Package_R1.md
human_acceptance: NOT_RUN
canonical_post_stop_validation: NOT_RUN
implementation_repository: UNASSIGNED
implementation_status: NOT_STARTED
implementation_authorization: NONE
git_authorization: NONE
---

# AOS Product Runtime Foundation Package R1

## 1. Purpose and status boundary

This package defines one coherent documentation foundation for the minimal AOS
Product Runtime. It is the `SCOPE-A — CONTRACT_ONLY` result of `INT-DOC-100`.
It gives later product and first-slice documentation a stable logical boundary,
shared semantics, conceptual interfaces, negative cases and recovery rules.

This package is documentation, not Product Runtime implementation or runtime
Evidence. It does not select a first user segment, job or vertical slice; assign
an implementation repository; choose an interface, persistence backend,
language, toolchain or dependency; change a feature disposition; create an
Execution Authorization for implementation; or authorize any Git action.

```yaml
authority_effect: NONE
product_scope_effect: HUMAN_SELECTED_FOUNDATION_SCOPE_ONLY
architecture_effect: LOGICAL_CONTRACT_BOUNDARY_ONLY
runtime_claim: NOT_MADE
runtime_verification: NOT_RUN
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

## 2. Exact scope decision

The human-selected Foundation scope is `SCOPE-A — CONTRACT_ONLY`.

### 2.1 Included

- the Product Runtime boundary needed to support a later first slice;
- a logical architecture skeleton without implementation topology;
- accepted primitive reuse and explicit gaps;
- bootstrap, installation boundary and First-Start behavior;
- Status / Next / Details, tutor and closure behavior;
- Project Memory, state continuity and task-scoped context behavior;
- Doctor, Self-Test and validation-result behavior;
- recovery, resume and handoff behavior;
- the Action Trust Boundary and external-content boundary;
- cross-feature flows, failures, negative scenarios and traceability.

### 2.2 Excluded

- full task conveyor, full runner or generic execution engine;
- exact CLI, chat, local UI or API selection;
- language, toolchain, dependency, storage or serialization choice;
- implementation repository or repository topology;
- schema files, runtime code, tests, CI/CD or deployment configuration;
- generic plugin system, module marketplace or remote loading;
- full Governance, authority-bearing Control Plane or automatic enforcement;
- RAG/vector database, model router, multi-agent orchestration or autonomous
  self-heal;
- Workbench/SaaS, collaboration backend or domain architecture;
- first-segment, first-job, first-slice or item-level feature disposition.

An excluded choice is intentionally deferred by the exact human scope decision;
it is not silently resolved by this package.

## 3. Authority and source binding

### 3.1 Authoritative owners

| Fact class used here | Owner | Use in this package |
|---|---|---|
| Identity, status semantics, authority, Minimal Safety Floor | [Core](../../docs/00_Core.md) | Normative invariants and protected human decisions |
| Users, problems, Product Runtime boundary and journeys | [Product](../../docs/01_Product.md) | Product value and observable journeys |
| Layers, contract classes and data ownership | [Architecture](../../docs/02_Architecture.md) | Logical skeleton and reusable primitives |
| Stages, validation, recovery and Git boundaries | [Development](../../docs/03_Development.md) | Lifecycle and verification behavior |
| Failures and regression candidates | [Lessons](../../docs/04_Lessons.md) | Negative-case input; proposals remain proposals |
| Feature identities and dossiers | [Features](../../docs/06_Features.md) | Exact six-feature coverage and design constraints |
| Interval order and required result | [R9](../AOS_Documentation_Task_Sequence_R9.md) | `INT-DOC-100` scope and closure route |
| Recorded lifecycle state | [CURRENT](../CURRENT.md) | Read-only persisted-state observation only |

Current explicit human decisions outrank persisted state. Derived status,
indexes, reports and context packs have no independent authority. If this
package conflicts with an authoritative owner, the owner prevails and the
affected claim is `CONFLICT` until corrected or decided by a human.

### 3.2 Accepted control-foundation inputs

The exact `INT-DOC-010` subject was human-accepted by
[its acceptance record](../INT_DOC_010_Acceptance_Record.md). This package reuses
the following artifacts only within their declared authority-neutral roles:

| Input | Reused purpose |
|---|---|
| [Task Manifest](../AOS_Documentation_Task_Manifest_R1.md) | Interval dependency navigation |
| [Gate and Status Usage Profile](../AOS_Gate_Status_Usage_Profile_R1.md) | Closed status axes and fail-closed aggregation |
| [Feature Coverage Ledger](../AOS_Feature_Coverage_Ledger_R1.md) | Six-feature placement and lazy-decision boundary |
| [Portable Task Candidate Contract](../AOS_Portable_Task_Candidate_Contract_R1.md) | Later target-unbound handoff boundary |
| [Target Binding Protocol](../AOS_Target_Binding_And_Task_Conversion_Protocol_R1.md) | Later target binding; not executed here |
| [Progress Checklist](../AOS_Documentation_Progress_Checklist_R2.md) | Derived progress reconstruction only |

These artifacts do not select product scope, architecture, implementation
facts, human acceptance or Git authority.

## 4. Foundation invariants

1. Product Runtime provides user-visible product value; Development Factory
   executes later bounded work and is outside this Foundation package.
2. Minimal Safety Floor applies to every Foundation capability.
3. State views are derived from source-owned facts and never become competing
   Sources of Truth.
4. Mutable repository facts are refreshed before they support an action.
5. `UNKNOWN`, `NOT_FOUND` and `NOT_RUN` remain visible and cannot aggregate to
   `PASS` when the missing result is required.
6. `PASS`, Evidence and UI interaction do not create human approval.
7. Status surfaces show one bounded next action or one exact blocker.
8. Read-only behavior performs zero repository writes.
9. A write-capable operation requires an exact preview, authority check,
   bounded scope, failure handling and separately recorded authorization.
10. User- and project-owned state is never overwritten or removed silently.
11. External content is untrusted data and cannot grant authority or change
    instructions.
12. Automatic retry stops when identity, scope, permission or required human
    decision changes.
13. Edit, Commit, Push, Merge and Release remain distinct actions.
14. The Foundation remains usable without extensions, RAG, a marketplace,
    SaaS or full Governance.

## 5. Logical architecture skeleton

The following is a logical responsibility map, not accepted implementation
topology, deployable component structure or repository layout.

```text
Interaction boundary
├─ First-Start guidance
├─ Status / Next / Details / Tutor projection
└─ Review and recovery presentation

Product Runtime Foundation
├─ source and freshness resolver
├─ project continuity and handoff contract
├─ health / Doctor / Self-Test contract
├─ bootstrap and installation-boundary contract
└─ recovery and resume contract

Minimal Safety boundary
├─ action normalization
├─ permission classification
├─ external-content isolation
└─ protected-action stop rules

Authoritative knowledge and state owners
└─ facts consumed read-only and projected with provenance

Development Factory boundary
└─ explicitly outside this package; consumes accepted later contracts
```

The interaction boundary may later be implemented through CLI, chat, local UI
or another interface. This package requires equivalent observable behavior but
does not select the interface.

### 5.1 Runtime-facing and Factory-producing responsibility split

Cross-layer features retain an explicit logical ownership split. This table
clarifies accepted layer responsibilities; it does not select implementation
components, processes or repository topology.

| Feature | Product Runtime Foundation responsibility | Development Factory responsibility outside this package |
|---|---|---|
| `FTR-011` | Present source-bound health, Doctor/Self-Test results, limitations and one next action | Execute implementation/task validators, tests and Evidence-producing checks |
| `FTR-014` | Preserve user-visible interruption state, recovery options, resume conditions and handoff | Produce execution journals, detect execution partial writes and perform separately authorized rollback/resume operations |
| `FTR-016` | Own authority-neutral Project Memory and user-visible continuity semantics | Build execution-specific Context Packs and task handoffs from authoritative inputs |

The Runtime side consumes exact Factory results when they exist; it never
simulates a missing Factory run. The Factory side cannot promote its result to
product status, human acceptance or authority.

## 6. Integrated Foundation journey

### 6.1 Normal flow

```text
user enters a project context
→ Foundation resolves project and source identity
→ mutable facts and required owners are refreshed
→ Action Trust Boundary classifies the requested capability
→ First-Start or Status projection explains current state
→ Doctor / Self-Test reports health with NOT_RUN and limitations preserved
→ one next action or one blocker is shown
→ any later mutation requires a separate exact authorization
→ result, recovery facts and handoff preserve continuity
```

### 6.2 First-contact outcome

A nontechnical user must be able to determine:

- which project or subject is in view;
- whether the available information is fresh enough;
- what is known, unknown, missing or not run;
- whether the current capability is read-only or may mutate state;
- what one bounded action is available next;
- what requires a human decision;
- how to inspect details and recover after interruption.

First-Start is not complete merely because files exist. Completion requires an
understandable first safe action and a visible route back after failure.

## 7. Capability contracts

### 7.1 Bootstrap, installation boundary and First-Start — `FTR-004`

**Consumes:** exact package/subject identity, target identity when applicable,
ownership classification, current facts, requested operation and authorization
state.

**Produces:** a side-effect-free preview, conflicts, ownership effects,
required decision, verification route, recovery route and first safe action.

**Required behavior:**

1. verify package and target identities before any write;
2. inventory affected paths or state classes;
3. distinguish tool-owned, shared and user/project-owned state;
4. render the exact intended change and conflicts;
5. require separate apply authorization;
6. bind any later apply to the preview identity;
7. verify the result and show rollback or recovery boundaries;
8. explain the first safe command or interaction without selecting its
   concrete interface here.

An identical apply over the same preview, target identity, scope and authority
must be idempotent or return a safe no-op. A retry after any of those bindings
changes requires a new preview and authorization.

Safe uninstall or destructive rollback is a separate protected action.

### 7.2 Status / Next / Details, tutor and closure — `FTR-008`

**Consumes:** source-owned lifecycle facts, refreshed mutable facts, validation
results, human decisions, permissions, blockers and provenance.

**Produces:** plain-language status, exactly one next action or blocker,
optional details, source/freshness information and closure explanation.

The projection is display-only by default. It cannot mutate lifecycle state,
turn a recommendation into approval or hide required `NOT_RUN`. If sources
conflict, it reports `CONFLICT` and blocks only the affected recommendation.

### 7.3 Result, Doctor and Self-Test — `FTR-011`

**Consumes:** exact subject identity, environment identity, required/optional
check inventory and authoritative result vocabulary.

**Produces:** a Runtime-facing projection of one
`ValidationEnvelope`-compatible result with per-check status, limitations,
provenance, aggregate technical result and one next action.

Doctor describes environment or installation health. Self-Test proves only the
declared checks over the exact subject. Neither proves product acceptance or
runtime value outside its Evidence boundary. A required `NOT_RUN`, malformed
status, wrong interpreter/environment provenance or incompatible result blocks
a green aggregate. Execution of implementation/task validators, tests and
Evidence-producing checks belongs to the later Development Factory; this
Foundation consumes and presents their exact results.

### 7.4 Recovery, resume and handoff — `FTR-014`

**Consumes:** intended operation, actual observed state, journal or equivalent
Evidence when available, partial-write classification, findings and authority
state.

**Produces:** preserved facts, reconciliation result, safe recovery options,
required human decision, bounded resume conditions and one next action.

Recovery stops the affected mutation first. Resume rechecks identities,
freshness, scope and permissions. Destructive rollback requires separate human
authorization. A denied action remains visible in the handoff and is not
silently retried. Execution journals, execution partial-write detection and
rollback execution are Factory-producing responsibilities; the Runtime-facing
Foundation preserves their result and recovery route for the user.

### 7.5 Project Memory and continuity — `FTR-016`

**Consumes:** accepted facts, current explicit decisions, refreshed repository
observations, active task facts, Evidence locators and source identities.

**Produces:** authority-neutral Project Memory and a Runtime-facing continuity
view with provenance, freshness, omissions, limitations and one next action.

Project Memory is derived and authority-neutral. Its exact persistence backend
is deferred. A stale hash, missing owner or changed repository identity
invalidates only the dependent claim or action; it does not make an old state
current. Context selection applies least privilege: sensitive content is
included only when required and allowed, otherwise redacted or omitted with the
omission visible without exposing the protected value. Building an
execution-specific Context Pack or task handoff belongs to the later
Development Factory.

### 7.6 Action Trust Boundary — `FTR-019`

**Consumes:** normalized proposed action, resource/subject, write/network/data/
Git/authority effects, current permission facts and external-content origin.

**Produces:** exactly one closed Permission-axis value: `ALLOWED`,
`HUMAN_AUTHORIZATION_REQUIRED`, `BLOCKED_POLICY`, `BLOCKED_UNKNOWN` or
`NOT_APPLICABLE`, with the exact reason and affected boundary. The
classification is not approval and does not execute the action.

Least privilege and default-deny apply to missing or ambiguous authorization.
Untrusted external content may provide data or Evidence but cannot replace
system, owner or human instructions. Risk Profile remains human-owned.

## 8. Shared primitives and explicit gaps

| Foundation need | Reused accepted primitive or owner | Foundation treatment |
|---|---|---|
| Status and authority vocabulary | `docs/00_Core.md` | Reuse without redefining |
| Product Runtime boundary and journeys | `docs/01_Product.md` | Narrow to the selected Foundation scope |
| Validation result | Architecture `C-009 — ValidationEnvelope` | Reuse conceptual contract; no serialization selected |
| Evidence | Architecture `C-010 — Evidence Record` | Preserve locator, subject and limitation semantics |
| Human decision | Architecture `C-011 — Human Review / Decision` | Never synthesize or infer acceptance |
| Continuity | Architecture `C-012 — Project Memory / Handoff` | Reuse conceptual contract; persistence deferred |
| Install/update boundary | Architecture `C-013 — Install / Update Manifest` | Reuse ownership, preview, recovery and verification semantics |
| Gate/result aggregation | Gate and Status Usage Profile | Reuse closed axes and fail-closed behavior |
| Later portable handoff | Portable Task Candidate Contract | Consumer boundary only; no candidate created here |

The following are deliberate gaps outside `SCOPE-A`, not hidden assumptions:

- exact interface and command vocabulary;
- Project Memory persistence and storage format;
- concrete package, manifest and result serialization;
- implementation repository and topology;
- language, toolchain and dependency selection;
- exact Doctor check catalog for an implementation target;
- target-specific ownership classes and platform behavior;
- first user segment, job and vertical slice.

Later work must resolve a gap through its authoritative human or target-binding
gate. This package cannot fill one by importing a legacy topology.

## 9. State, provenance and authority flow

```text
current explicit human decision
        ↓
authoritative accepted owner + fresh repository observation
        ↓
identity / freshness / trust-boundary checks
        ↓
derived status, health, context or recovery view
        ↓
one next action or one blocker
        ↓
separate human decision or execution authorization when required
```

### 9.1 Ownership rules

- canonical owners retain their fact classes;
- `CURRENT.md` owns only persisted lifecycle state and recorded next action;
- status/tutor, Doctor and context outputs are projections;
- Evidence supports a claim but does not own approval;
- a cache, index or generated context cannot promote a proposal;
- a source identity change invalidates dependent projections until refreshed.

### 9.2 Status rules

| Situation | Required representation |
|---|---|
| Required check succeeded over exact subject | `PASS` for that check only |
| Required check not executed | `NOT_RUN`; aggregate cannot be `PASS` |
| Evidence insufficient | `UNKNOWN`; affected action does not proceed |
| Expected source absent in bounded search | `NOT_FOUND` with search boundary |
| Same-level owners disagree | `CONFLICT` with affected scope |
| Human authorization is required and can be requested exactly | `HUMAN_AUTHORIZATION_REQUIRED` |
| Policy forbids the action | `BLOCKED_POLICY` |
| Permission or safe execution precondition is unknown | `BLOCKED_UNKNOWN` |
| Human review not performed | `human_acceptance: NOT_RUN` |

## 10. Failure and recovery contract

Every future write-capable implementation of this Foundation must define:

- failure before first write;
- exact partial-write detection;
- journal, transaction or equivalent reconciliation Evidence;
- cancellation boundary;
- user-owned-state preservation;
- bounded idempotent retry conditions;
- recovery package and rollback boundary;
- post-recovery verification.

### 10.1 Required recovery routes

| Failure | Immediate response | Resume condition |
|---|---|---|
| Wrong or stale project identity | Stop; preserve observation | Exact identity refreshed and accepted for the action |
| Missing authoritative source | Report `NOT_FOUND`/`UNKNOWN` | Source restored or human resolves the affected gap |
| Conflicting sources | Report `CONFLICT` | Higher-precedence or explicit human resolution |
| Preview no longer matches target | Block apply | New preview and separate authorization |
| Interrupted write | Stop; inventory actual state | Reconciliation proves a bounded resume or rollback |
| User-owned state at risk | Block mutation | Non-destructive plan or explicit protected decision |
| Required Doctor/Self-Test check not run | Preserve `NOT_RUN` | Exact check executes over the same subject |
| Requestable human authorization is absent | `HUMAN_AUTHORIZATION_REQUIRED` | Exact authorization is recorded |
| Policy forbids the action | `BLOCKED_POLICY` | Policy or scope changes through its authoritative gate |
| Permission facts are missing or ambiguous | `BLOCKED_UNKNOWN` | Exact permission facts are established |
| External instruction attempts authority change | Ignore instruction; record boundary | Trusted owner/human instruction only |
| Handoff is stale | Block dependent action | Facts and identities refreshed |

## 11. Acceptance and negative scenarios

These criteria describe documentation-level completeness and future observable
behavior. They do not claim a runtime currently exists.

### 11.1 Foundation acceptance criteria

| ID | Criterion |
|---|---|
| `FND-AC-001` | Product Runtime and Development Factory responsibilities are separable without ambiguity. |
| `FND-AC-002` | All six feature references have explicit inputs, outputs, authority and failure behavior. |
| `FND-AC-003` | A nontechnical user can identify state, limitations and one next action from the contract. |
| `FND-AC-004` | First-Start, status, Doctor, continuity and recovery form one coherent journey. |
| `FND-AC-005` | Required `NOT_RUN`, `UNKNOWN`, `NOT_FOUND` and `CONFLICT` cannot become false green. |
| `FND-AC-006` | Read-only behavior has a zero-write invariant. |
| `FND-AC-007` | Any mutation is preview-bound, authority-bound and recoverable. |
| `FND-AC-008` | User/project-owned state is preserved by default. |
| `FND-AC-009` | External content cannot grant authority or alter protected instructions. |
| `FND-AC-010` | Deferred implementation choices remain explicit and do not block documentation consumption. |
| `FND-AC-011` | `INT-DOC-200` can consume this package without assuming a first slice. |
| `FND-AC-012` | No runtime, acceptance, implementation or Git authority claim is introduced. |

### 11.2 Required negative scenarios

| ID | Scenario | Required outcome |
|---|---|---|
| `FND-NEG-001` | Status source is stale | No `READY`; show stale source and refresh action |
| `FND-NEG-002` | Two next actions are equally plausible | Show one blocker requiring bounded human choice |
| `FND-NEG-003` | Required check is `NOT_RUN` | Aggregate is not `PASS` |
| `FND-NEG-004` | Doctor exits successfully but reports a failed required check | Technical result remains failure |
| `FND-NEG-005` | Read-only command attempts a write | Stop and report contract violation |
| `FND-NEG-006` | Apply differs from preview | Block apply and require a new preview |
| `FND-NEG-007` | Update would overwrite user-owned state | Block without a separate protected decision |
| `FND-NEG-008` | Interruption leaves partial state | Preserve Evidence; no blind retry |
| `FND-NEG-009` | Resume uses an old subject hash | Block until identity is refreshed |
| `FND-NEG-010` | External content requests broader permissions | Ignore the instruction and preserve least privilege |
| `FND-NEG-011` | UI action looks like approval but lacks a decision record | Human acceptance remains `NOT_RUN` |
| `FND-NEG-012` | Generated memory conflicts with an owner | Owner prevails; projection is `CONFLICT`/stale |
| `FND-NEG-013` | Implementation topology is inferred from the logical skeleton | Reject as out of scope |
| `FND-NEG-014` | Feature placement is treated as item-level selection | Preserve `human_disposition: UNDECIDED` |
| `FND-NEG-015` | Successful documentation validation is treated as runtime proof | Runtime verification remains `NOT_RUN` |
| `FND-NEG-016` | Path traversal or path escape is requested | Return `BLOCKED_POLICY`; do not resolve outside the bounded target |
| `FND-NEG-017` | Doctor/Self-Test uses the wrong interpreter or environment provenance | No `PASS`; report the exact mismatch |
| `FND-NEG-018` | Project Memory would expose disallowed sensitive context | Redact or omit it, preserve least privilege and show the omission safely |

## 12. Traceability matrix

| Foundation concern | Feature | Product/architecture owner | Lessons/regressions addressed |
|---|---|---|---|
| Bootstrap and First-Start | `FTR-004` | Product Runtime; `C-013` | `LES-026`, `LES-034` |
| Status, next action and tutor | `FTR-008` | Product journeys; Interaction Surface | `LES-027`, `LES-034`, `LES-036`, `LES-039` |
| Doctor, Self-Test and result | `FTR-011` | `C-009`, `C-010`; Development validation | `LES-005`, `LES-010`, `LES-016`, `LES-031` |
| Recovery and handoff | `FTR-014` | Recovery model; `C-012` | `LES-023`, `LES-024`, `LES-038` |
| Project continuity and context | `FTR-016` | Project Memory; data ownership | `LES-025`, `LES-027`, `LES-028`, `LES-030` |
| Permission and external-content boundary | `FTR-019` | Minimal Safety Floor; authority model | `LES-009`, `LES-012`, `LES-020`, `LES-021`, `LES-039` |
| Runtime/Factory separation | all six | Product and layer boundaries | `LES-004`, `LES-032`, `LES-033`, `LES-037`, `LES-041` |

Lessons remain `LESSON_PROPOSAL` unless separately human-accepted. This matrix
uses them as regression candidates, not as independent authority.

## 13. Handoff to `INT-DOC-200`

After exact canonical post-stop validation and human acceptance, this package may give
`INT-DOC-200` the following stable constraints for a first-slice decision
package:

- the first slice must produce a user-visible Product Runtime outcome;
- it must operate without full Factory, extensions or full Governance;
- its state, status, failure, recovery and authority behavior must map to this
  Foundation;
- it must preserve one-next-action and no-false-green semantics;
- any mutation or implementation remains separately authorized;
- target-specific choices remain unbound until their proper gate.

This package does not start, authorize or accept `INT-DOC-200`.

## 14. Known unknowns and protected later decisions

| Decision or unknown | Current state | Required owner/gate |
|---|---|---|
| First segment, job and vertical slice | `UNDECIDED` | Human decision prepared by `INT-DOC-200` |
| Concrete interface | `UNDECIDED` | Human product/architecture decision |
| Implementation repository | `UNASSIGNED` | Human repository-role decision |
| Project Memory persistence | `UNDECIDED` | Human architecture decision before implementation planning |
| Language, toolchain and dependencies | `UNDECIDED` | Human architecture/implementation decision |
| Concrete serialization and schemas | `UNDECIDED` | Exact feature/target contract task |
| Target ownership classes and install mechanics | `UNBOUND` | Target-binding protocol and human protected decisions |
| Exact Doctor check catalog | `UNBOUND` | Implementation-target contract and validation plan |
| Human-decision authenticity mechanism | `UNDECIDED` | Human product/security decision |

These items are visible handoff constraints. This Foundation neither guesses
nor imports them from reference repositories.

## 15. Completion and validation route

The `INT-DOC-100` EXECUTE candidate is complete only when its internal check
confirms:

1. this is the sole changed output path;
2. frontmatter and Markdown structure are valid;
3. all relative links resolve;
4. the exact six feature IDs are covered without changing dispositions;
5. logical architecture does not become implementation topology;
6. authority, status and Git boundaries match their owners;
7. failures, recovery, negative scenarios and next-interval usability are
   internally consistent;
8. no excluded Product Runtime, Factory or extension scope is introduced;
9. the final candidate is frozen by exact byte identity.

Internal self-check is not canonical validation. The next stage is a separate
read-only `POST_STOP_DOCUMENTATION` `VALIDATE` over the frozen exact candidate.
Validation must not correct this file or mutate repository state.

```yaml
artifact_status: DRAFT
internal_check_result_owner: TERMINAL_EXECUTE_STAGE_REPORT
freeze_identity_owner: TERMINAL_EXECUTE_STAGE_REPORT
canonical_post_stop_validation: NOT_RUN
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
authority_effect: NONE
```
