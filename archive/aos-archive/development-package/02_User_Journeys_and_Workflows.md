---
artifact_id: AOS3-DPKG-DOC-002
artifact_type: USER_JOURNEYS_AND_WORKFLOWS
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R8
status: DRAFT_SOURCE_WITH_PARTIAL_C1_ACCEPTANCE
authority: PROPOSAL_WITH_HUMAN_DECISION_INPUTS
exact_subject: End-to-end AOS Core v1 journeys, states, transitions, human checkpoints, failures, and recovery for the accepted A to B to C sequence
created: '2026-07-30'
human_acceptance: C1_ACCEPTED_126_CURRENT_11_STALE_10_NEW_AC_AND_2_NEW_SCHEMA_DRAFT
provenance:
  - path: ../../docs/00_Core.md
    use: authority and safety invariants
  - path: ../../docs/01_Product.md
    use: canonical user journeys and product boundary
  - path: ../../docs/03_Development.md
    use: normative stage workflow and stop rules
  - path: ../../docs/04_Lessons.md
    use: applicable failure and recovery proposals
  - path: ../../docs/06_Features.md
    use: relevant feature behavior, states, failures, recovery, and negative scenarios
  - path: 01_Product_and_Core_V1_Scope.md
    use: Stage B product scope and first-slice product contract
  - path: research/RSR-001_AgentOS_Interview_and_Product_Spec.md
    use: non-authoritative interview and spec lifecycle evidence
  - path: research/RSR-002_AOS_FARM_Decision_and_Recovery_Boundaries.md
    use: non-authoritative decision, Risk Profile, candidate, and handoff evidence
upstream_links:
  - 00_Control_and_Source_Precedence.md
  - 01_Product_and_Core_V1_Scope.md
  - decisions/DEC-PROD-003_Core_V1_Slice_Sequence.md
  - decisions/DEC-PROD-004_Core_V1_Scope_and_Non_Goals.md
  - decisions/DEC-PROD-005_Product_Spec_and_Feature_Passport_Relation.md
  - decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
downstream_links:
  - decisions/G2_ARCHITECTURE_OPTION_PACKAGE.md
  - 03_Architecture_and_Decisions.md
  - 04_Runtime_and_Data_Contracts.md
  - 05_Quality_Recovery_and_Security.md
  - 06_Traceability_and_Readiness.md
limitations:
  - Upstream PSC-A-001 changed in DRAFT-R9 by removal of its redundant scalar authority field; its historical C1 binding is stale.
  - WFC-A-001 and AC-WFC-A-001-01..07 now have current envelope-owned definitions in DRAFT-R9; their historical C1 bindings are stale.
  - WFC-B-001 and WFC-C-001 changed in DRAFT-R6; their C1 acceptance remains stale and their ten new acceptance IDs remain DRAFT.
  - Unchanged C1-frozen workflow definitions retain their exact historical acceptance; Task candidates remain separately unaccepted.
  - Slice B and Slice C are dependency-bounded future journeys; only Slice A is selected as first.
  - G2 selected the interface, persistence, provider, authenticity, Risk, and compatibility boundaries.
  - Runtime Evidence remains NOT_RUN; implementation-repository binding is deliberately deferred.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# 02 — User Journeys and Workflows

## 1. Status boundary

This owner describes observable workflow contracts. It does not choose implementation topology or convert workflow readiness into permission.

```yaml
document_status: DRAFT_SOURCE_WITH_PARTIAL_C1_ACCEPTANCE
workflow_contract_acceptance:
  unchanged_subjects: HUMAN_ACCEPTED_VIA_DEC-CONTRACT-001
  current_accepted_subject_count: 126
  stale_product_contract_subjects: [PSC-A-001]
  stale_contract_subjects: [WFC-A-001, WFC-B-001, WFC-C-001]
  stale_acceptance_ids: [AC-WFC-A-001-01..07]
  new_draft_acceptance_ids: [AC-WFC-B-001-01..05, AC-WFC-C-001-01..05]
runtime_verification: NOT_RUN
implementation_repository: UNASSIGNED
g2_architecture_status: HUMAN_DECIDED_WITH_IMPLEMENTATION_REPOSITORY_DEFERRED
implementation_authorization: NONE
git_authorization: NONE
```

## 2. Workflow invariants

1. One run performs one stage.
2. A terminal result produces a report and stops.
3. Human product, architecture, scope, acceptance, execution, and Git decisions remain separate.
4. A derived view never mutates source-owned state.
5. Material unknowns block only dependent work.
6. Validation never repairs its subject.
7. Task compilation requires accepted upstream IDs.
8. Repository discovery and resume are read-only until separately authorized.
9. No transition starts the next slice automatically.
10. Every visible status names provenance, freshness, limitations, and one next action.

## 3. Orthogonal state axes

The workflow must not compress these axes into one `status`:

| Axis | Example values | Owner |
|---|---|---|
| Journey phase | `INTAKE`, `CLARIFICATION`, `SPEC_DRAFT`, `HUMAN_REVIEW`, `TASK_COMPILATION`, `SAFE_RESUME` | Workflow record |
| Document maturity | `DRAFT`, `HUMAN_REVIEW_REQUIRED`, `HUMAN_ACCEPTED`, `STALE`, `SUPERSEDED` | Exact document |
| Human decision | `ACCEPT`, `NEEDS_CHANGES`, `REJECT`, `DEFER`, `NOT_RUN` | Exact human decision record |
| Technical result | `CONTRACT_VIOLATION`, `FAIL`, `BLOCKED`, `UNKNOWN`, `NOT_RUN`, `PASS` | Exact check/result |
| Permission | `ALLOWED`, `HUMAN_AUTHORIZATION_REQUIRED`, `BLOCKED_POLICY`, `BLOCKED_UNKNOWN`, `NOT_APPLICABLE` | Authority resolver/policy |
| Git authority | `NONE` or one exact separately granted action | Exact Git decision record |
| Freshness | `CURRENT_FOR_BINDING`, `STALE`, `UNKNOWN` | Source-bound observation |

No axis changes another automatically.

## 4. End-to-end Core v1 journey

```text
J-CV1-001 — Slice A
raw intent
→ preserve and classify
→ clarify material gaps
→ DRAFT Product Spec
→ DRAFT Feature Passport
→ human product review
→ stop

[requires accepted upstream contracts]

J-CV1-002 — Slice B
accepted requirement/contract/scenario IDs
→ task eligibility
→ one bounded Task Brief candidate
→ execution authorization required
→ stop

[requires G2 Project Memory decision and actual project state]

J-CV1-003 — Slice C
bind repository/project state read-only
→ reconcile decisions/candidate/findings/permissions
→ detect stale/conflicting state
→ show one safe next action
→ human review
→ stop
```

The bracketed boundaries are gates, not hidden transitions.

## 5. `J-CV1-001` — Intent to reviewed product draft

### Contract identity

```yaml
journey_id: J-CV1-001
contract_id: WFC-A-001
revision: R3
status: DRAFT_UNACCEPTED_IN_DRAFT_R9
previous_acceptance: STALE_BY_SUBJECT_CHANGE
exact_subject: Intent intake through reviewed DRAFT Product Spec and Feature Passport with a human-review stop
roadmap_id: RMP-004
selected_as_first_slice: true
actor:
  primary: non-programmer or domain expert
  supporting:
    - product or documentation agent
    - optional developer, architect, legal, security, or domain reviewer
  decision_owner: human user
trigger: The user supplies a raw idea, problem, existing brief, or solution-shaped request and asks AOS to make it reviewable.
preconditions:
  - the original input boundary is known
  - canonical project sources are locatable
  - external content is treated as untrusted data
  - the sensitive-data/provider boundary is known or external transmission is blocked
  - implementation_authorization and git_authorization are NONE
  - documentation writes require an exact authorized path
inputs:
  - id: IN-A-001
    value: original user input
    handling: preserve exact content or record explicit normalization and digest
  - id: IN-A-002
    value: current accepted decisions
    handling: bind exact revision, hash, and fact-class scope
  - id: IN-A-003
    value: existing product or project context
    handling: classify source and freshness
  - id: IN-A-004
    value: external or reference evidence
    handling: preserve authority NONE unless promoted by a human decision
  - id: IN-A-005
    value: user answers
    handling: attribute each answer to its question and revision
outputs:
  - id: OUT-A-001
    value: Intent Record candidate
    status: DRAFT
  - id: OUT-A-002
    value: Product Spec
    status: DRAFT
  - id: OUT-A-003
    value: at least one Feature Passport by human review
    status: DRAFT
  - id: OUT-A-004
    value: gap, conflict, and unknown register
    status: CLASSIFIED_PROPOSAL
  - id: OUT-A-005
    value: human review package
    status: HUMAN_REVIEW_REQUIRED
  - id: OUT-A-006
    value: exactly one next action
    status: PROPOSAL_WITH_REQUIRED_AUTHORITY
states:
  initial: INTAKE_DRAFT
  intermediate:
    - NEEDS_CLARIFICATION
    - READY_FOR_SPEC_DRAFT
    - SPEC_DRAFT
    - SPEC_DRAFT_INCOMPLETE
    - BLOCKED_HUMAN_DECISION
    - DEFERRED_WITH_VISIBLE_UNKNOWN
  terminal:
    - HUMAN_REVIEW_REQUIRED
side_effects:
  allowed:
    - preserve source bindings and human answers
    - create or update DRAFT documentation only inside an exact authorized path
    - generate read-only review output
  forbidden:
    - source-project mutation
    - dependency installation
    - architecture selection
    - Task Brief creation from DRAFT inputs
    - implementation, validation-as-repair, or Git operations
authority:
  agent_may:
    - preserve and classify input
    - ask bounded material questions
    - draft product artifacts and report gaps
    - recommend exactly one next action
  human_only:
    - answer material product questions
    - accept, reject, defer, or request changes to exact product subjects
    - choose architecture, repository, provider, execution, validation, and Git actions
failures:
  - code: EMPTY_OR_UNUSABLE_INPUT
    detection: no usable intent or source boundary
    effect: remain INTAKE_DRAFT and request bounded clarification
  - code: MATERIAL_INFORMATION_MISSING
    detection: a required owner field cannot be derived
    effect: enter NEEDS_CLARIFICATION
  - code: SOURCE_CONFLICT
    detection: current sources disagree on an affected fact
    effect: block only the affected claim or artifact
  - code: SENSITIVE_BOUNDARY_UNKNOWN
    detection: external transmission safety is unresolved
    effect: block external transmission while allowing safe local classification
  - code: STALE_UPSTREAM_DECISION
    detection: an upstream revision or hash no longer matches
    effect: stop affected synthesis without rewriting accepted evidence
recovery:
  - preserve original input, answers, and current draft state
  - identify the exact missing, stale, or conflicting field
  - obtain one bounded human answer or restore the exact source
  - resume only the affected documentation stage
  - never infer acceptance or implementation authority during recovery
non_goals:
  - architecture or implementation-repository selection
  - Task Brief creation
  - implementation or runtime validation
  - automatic human acceptance
  - Commit, Push, Merge, or Release
executable_acceptance:
  - AC-WFC-A-001-01 original input identity is preserved
  - AC-WFC-A-001-02 material missing fields produce bounded questions without invented answers
  - AC-WFC-A-001-03 DRAFT Product Spec and Feature Passport expose facts, assumptions, unknowns, conflicts, scope, and non-goals
  - AC-WFC-A-001-04 every transition names actor, authority, state effect, and allowed side effect
  - AC-WFC-A-001-05 sensitive or conflicting input blocks only the affected external or product claim
  - AC-WFC-A-001-06 terminal state is HUMAN_REVIEW_REQUIRED with exactly one decision request
  - AC-WFC-A-001-07 no Task, implementation, validation, or Git authority is produced
```

### Actors

- primary: non-programmer or domain expert;
- supporting: product/documentation agent;
- decision owner: human user;
- optional reviewer: developer, architect, legal/security/domain owner when a material boundary requires them.

### Trigger

The primary user supplies a raw idea, problem, existing brief, or solution-shaped request and asks AOS to make it reviewable.

### Preconditions

- the original input boundary is known;
- canonical project sources are locatable;
- any external content is treated as untrusted data;
- sensitive-data/provider boundary is known or external transmission is blocked;
- implementation and Git authority are `NONE`;
- the agent can write only inside an explicitly authorized documentation path.

### Inputs

| Input ID | Input | Required handling |
|---|---|---|
| `IN-A-001` | Original user input | Preserve exact content or record explicit normalization and digest |
| `IN-A-002` | Current accepted decisions | Bind exact revision/hash and fact-class scope |
| `IN-A-003` | Existing product/project context | Classify source and freshness |
| `IN-A-004` | External/reference evidence | Treat as authority `NONE` unless promoted by human decision |
| `IN-A-005` | User answers | Attribute to question and revision |

### Outputs

| Output ID | Output | Status/authority |
|---|---|---|
| `OUT-A-001` | Intent Record candidate | `DRAFT`, proposal |
| `OUT-A-002` | DRAFT Product Spec | `DRAFT`, proposal |
| `OUT-A-003` | At least one DRAFT Feature Passport by human review | `DRAFT`, separate item-level disposition |
| `OUT-A-004` | Gap/conflict/unknown register | Classified observations/proposals |
| `OUT-A-005` | Human review package | Decision request, not approval |
| `OUT-A-006` | One next action | Derived recommendation with required authority |

### State machine

```text
INTAKE_DRAFT
├─ unusable input → INTAKE_DRAFT + CLARIFICATION_REQUEST
├─ material gaps → NEEDS_CLARIFICATION
└─ sufficient input → READY_FOR_SPEC_DRAFT

NEEDS_CLARIFICATION
├─ answer received → re-evaluate affected fields
├─ external decision required → BLOCKED_HUMAN_DECISION
└─ user defers → DEFERRED_WITH_VISIBLE_UNKNOWN

READY_FOR_SPEC_DRAFT
→ SPEC_DRAFT

SPEC_DRAFT
├─ internal contradiction → NEEDS_CLARIFICATION
├─ missing required owner field → SPEC_DRAFT_INCOMPLETE
└─ review package complete → HUMAN_REVIEW_REQUIRED

HUMAN_REVIEW_REQUIRED
→ stop
```

No agent transition sets `HUMAN_ACCEPTED`.

### Transition table

| Transition ID | From → To | Condition | Actor/authority | Side effect |
|---|---|---|---|---|
| `TR-A-001` | start → `INTAKE_DRAFT` | Input received | Agent, read/classify | Preserve source |
| `TR-A-002` | `INTAKE_DRAFT` → `NEEDS_CLARIFICATION` | Material field missing/conflicting | Agent recommendation | Add bounded questions |
| `TR-A-003` | `NEEDS_CLARIFICATION` → `READY_FOR_SPEC_DRAFT` | Human answers sufficient for affected fields | Human answers; agent checks | Update classified record |
| `TR-A-004` | `READY_FOR_SPEC_DRAFT` → `SPEC_DRAFT` | Owner fields and sources known | Documentation mutation authorization | Create DRAFT artifacts |
| `TR-A-005` | `SPEC_DRAFT` → `HUMAN_REVIEW_REQUIRED` | Review checks complete | Agent report only | Freeze review candidate |
| `TR-A-006` | `HUMAN_REVIEW_REQUIRED` → human disposition | Separate exact decision | Human only | Decision record; no implementation grant |

### Human checkpoints

- answer material clarification;
- choose product scope when options diverge;
- accept, request changes, reject, or defer exact Product Spec/Feature Passport revisions;
- decide any sensitive-data/provider boundary;
- decide whether a material architecture need proceeds to G2.

### Side effects

Allowed:

- create/update DRAFT documentation within exact authorized paths;
- store source bindings and human answers;
- generate read-only review output.

Forbidden:

- source-project mutation;
- dependency install;
- architecture selection;
- Task Brief creation from DRAFT input;
- implementation, validation-as-repair, or Git action.

## 6. `J-CV1-002` — Accepted contract to bounded Task

```yaml
journey_id: J-CV1-002
contract_id: WFC-B-001
revision: R2
status: DRAFT_UNACCEPTED_IN_DRAFT_R8
previous_acceptance: STALE_BY_SUBJECT_CHANGE
roadmap_id: RMP-005
actor:
  primary: product builder or coding agent
  decision_owner: human Task owner
trigger: The user requests one bounded package-local Task candidate from current accepted subjects.
preconditions:
  - every consumed requirement, contract, acceptance, and scenario ID is accepted and current
  - when the requested Task consumes Product Spec or Feature Passport instances, each consumed instance is HUMAN_ACCEPTED and exact-revision/hash bound
  - DEC-CORR-001 remains current for the AOS3-DPKG-TASK-### namespace
  - documentation mutation is authorized only inside AOS-3/development-package/tasks/
  - implementation repository may remain UNASSIGNED for portable compilation
  - optional or deferred capabilities are not admitted
inputs:
  - requested bounded outcome and actor
  - accepted current upstream IDs and DEC-CONTRACT-001 bindings
  - accepted Product Spec or Feature Passport bindings only when the Task consumes those instances
  - current dependency graph and repository-binding state
  - explicit scope, non-goals, authority, Risk, and validation state
outputs:
  - exactly one AOS3-DPKG-TASK-### DRAFT Task candidate when eligible
  - deterministic derived Queue projection or explicit NOT_MATERIALIZED
  - eligibility result with accepted/stale/DRAFT input classification
  - one human Task review request with explicit non-grants
states:
  - TASK_INPUT_RECEIVED
  - ELIGIBILITY_CHECK
  - INELIGIBLE_UPSTREAM
  - TASK_DRAFT
  - HUMAN_TASK_REVIEW_REQUIRED
side_effects:
  allowed:
    - write one bounded Task candidate only inside the authorized package task path
    - update a derived package-local graph or Queue in the same authorized candidate
  invalid_input:
    - write zero Task Brief files
    - materialize no Queue
  forbidden:
    - Roadmap mutation or Roadmap TASK-### allocation
    - implementation-repository inference
    - Task activation, execution, validation, or Git action
authority:
  agent_may:
    - inspect eligibility, compile an exact DRAFT candidate, and report blockers
  human_only:
    - accept the Task, assign Risk, bind a repository, authorize execution/validation, and authorize each Git action
failures:
  - BLOCKED_DRAFT_UPSTREAM
  - BLOCKED_STALE_UPSTREAM
  - BLOCKED_MISSING_ACCEPTED_INSTANCE_WHEN_CONSUMED
  - FAIL_ORPHAN_OR_CIRCULAR_DEPENDENCY
  - BLOCKED_SCOPE_EXPANSION
  - CONTRACT_VIOLATION_TASK_AUTHORITY
recovery:
  - preserve the exact rejected input set and eligibility result
  - correct or accept only the affected upstream subject in a new revision
  - rebuild deterministically from current accepted inputs
  - never materialize a Task or Queue from an ineligible input
non_goals:
  - accept Product Spec, Feature Passport, contract, or Task
  - assign physical repository paths or commands while unbound
  - execute, validate, implement, or perform Git operations
executable_acceptance:
  - AC-WFC-B-001-01 eligible current accepted input produces exactly one bounded AOS3-DPKG-TASK-### candidate
  - AC-WFC-B-001-02 every derived requirement, contract, acceptance, scenario, and decision binding is current and accepted
  - AC-WFC-B-001-03 PORTABLE_UNBOUND output leaves repository, paths, commands, dependencies, and executable checks UNASSIGNED
  - AC-WFC-B-001-04 DRAFT, stale, rejected, missing-required-instance, orphan, cycle, or scope-expanding input produces zero Task files and no Queue
  - AC-WFC-B-001-05 terminal output requests human Task review, names exactly one next action, preserves all implementation/validation/Git non-grants, and stops
```

### Observable path after new acceptance

```text
accepted upstream IDs
→ verify acceptance binding and freshness
→ evaluate task eligibility
→ choose one bounded outcome
→ compile portable Task Brief candidate
→ preserve implementation_repository as UNASSIGNED unless separately bound
→ reconcile logical scope/dependencies/checks
→ request separate human Task review
→ stop
```

The Product Spec/Feature Passport precondition is conditional: it applies only when a Task consumes those accepted instances. Contract-only infrastructure Tasks may derive from other current accepted subjects without inventing product-instance bindings.

## 7. `J-CV1-003` — Existing project to safe next action

```yaml
journey_id: J-CV1-003
contract_id: WFC-C-001
revision: R2
status: DRAFT_UNACCEPTED_IN_DRAFT_R8
previous_acceptance: STALE_BY_SUBJECT_CHANGE
roadmap_id: RMP-008
actor:
  primary: product builder or new AI agent
  decision_owner: human project owner
trigger: A new session must resume an exact project subject and identify one safe next action without chat history.
preconditions:
  - Project Memory owner and persistence decisions are current
  - exact project or repository subject is supplied
  - read-only inspection of the exact subject is allowed
  - no repair, retry, execution, validation, or Git authority is inferred
inputs:
  - root, worktree, branch, HEAD, candidate, and baseline identities when applicable
  - accepted Human Decisions with exact revision/hash and staleness rules
  - active stage, candidate, findings, failures, blockers, and authority state
  - stored Project Memory and current source observations
  - reference repository/ref/commit/path bindings when a claim depends on them
outputs:
  - refreshed read-only ResumeRecord bound to the exact subject
  - classified CURRENT, STALE, CONFLICT, UNKNOWN, NOT_FOUND, and NOT_RUN facts
  - explicit changed, uncommitted, out-of-scope, partial, or unknown-outcome state
  - exactly one safe next action naming its required human authority
  - human review stop with all non-grants
states:
  - RESUME_SUBJECT_IDENTIFICATION
  - REFRESHING_READ_ONLY
  - STALE_OR_BLOCKED
  - CURRENT_STATE_READY
  - HUMAN_REVIEW_REQUIRED
side_effects:
  allowed:
    - read exact owners and refresh derived in-memory observations
    - emit a reviewable ResumeRecord outside the inspected subject only when separately authorized
  forbidden:
    - source-tree mutation during read-only resume
    - automatic retry after unknown operation outcome
    - remediation, cleanup, checkout, implementation, validation-as-repair, or Git action
authority:
  agent_may:
    - inspect, compare, classify staleness, and recommend one safe action
  human_only:
    - resolve stale/conflicting decisions, authorize recovery or mutation, and authorize every Git action
failures:
  - BLOCKED_INCOMPLETE_STATE_BINDING
  - BLOCKED_STALE_DECISION
  - BLOCKED_REFERENCE_ACCESS
  - FAIL_RESUME_READ_ONLY_MUTATION
  - BLOCKED_UNKNOWN_OPERATION_OUTCOME
  - BLOCKED_AUTHORITY_CONFLATION
recovery:
  - preserve stored and current identities without overwriting historical state
  - block only the dependent action or claim
  - restore the exact source or obtain a new hash-bound human decision
  - inspect actual state before any recovery proposal
  - require a new authorization for every write or retry
non_goals:
  - autonomous repair, retry, cleanup, or self-heal
  - selecting an implementation repository
  - accepting Evidence or technical PASS
  - implementation, validation mutation, or Git operations
executable_acceptance:
  - AC-WFC-C-001-01 ResumeRecord binds exact root, worktree, branch, HEAD, candidate, baseline, and decision identities, using explicit NOT_APPLICABLE only where the subject has no such axis
  - AC-WFC-C-001-02 every changed subject or decision hash is classified STALE and blocks only dependent claims/actions
  - AC-WFC-C-001-03 read-only resume produces zero inspected-source writes and reports before/after identity
  - AC-WFC-C-001-04 unknown operation outcome forbids automatic retry and requires actual-state reconciliation plus new human authority
  - AC-WFC-C-001-05 terminal output contains exactly one safe next action, names the required human authority, preserves implementation/validation/Git non-grants, and stops at human review
```

### Observable path after new acceptance

```text
identify project/repository
→ bind root/worktree/branch/HEAD/candidate
→ load accepted decisions and source-owned state
→ refresh mutable observations
→ classify gaps/conflicts/stale records
→ compute allowed next actions without performing them
→ show one safe next action
→ human review
→ stop
```

The minimal historical handoff inspected in `RSR-002` remains insufficient because it lacks most of these exact binding and authority fields.

## 8. Cross-journey authority checkpoints

| Checkpoint | Human decision | Technical output cannot substitute |
|---|---|---|
| `HUMAN_PRODUCT_GATE_G1` | User/job/outcome/slices/scope/ownership | Options or recommendation |
| `HUMAN_ARCHITECTURE_GATE_G2` | Repository, topology, toolchain, persistence, provider/privacy, authenticity, Risk Profile, compatibility | Architecture packet or matrix |
| `HUMAN_CONTRACT_ACCEPTANCE` | Exact Product Spec/Feature Passport/contract revisions | Completeness/readiness PASS |
| `HUMAN_EXECUTION_AUTHORIZATION` | Exact Task/stage/paths/operations | Task Brief or Risk recommendation |
| `HUMAN_RESULT_DECISION` | Accept result, needs changes, reject, or defer | Validation/Evidence |
| `HUMAN_GIT_ACTION` | One exact Commit, Push, Merge, or Release action | Acceptance or delivery recommendation |

## 9. Failure and recovery matrix

| Failure ID | Detection | Immediate result | Recovery | Automatic retry |
|---|---|---|---|---|
| `FAIL-WF-001` — empty/unusable intent | Required source absent | `NEEDS_CLARIFICATION` | Preserve input; ask one material question | No |
| `FAIL-WF-002` — ambiguous answer | Multiple plausible meanings affect scope/outcome | `NEEDS_CLARIFICATION` | Ask user to select/clarify | No |
| `FAIL-WF-003` — source contradiction | Owners disagree | `CONFLICT` | Identify fact owner; block affected artifact | No |
| `FAIL-WF-004` — stale decision | Bound revision/hash changed | `BLOCKED_STALE_DECISION` | Rebind or obtain new decision | No |
| `FAIL-WF-005` — missing reference commit/path | Exact Git object/path unavailable | `BLOCKED_REFERENCE_ACCESS` or `NOT_FOUND` | Restore exact source or continue without unsupported claim | No |
| `FAIL-WF-006` — DRAFT-to-Task attempt | Upstream maturity not accepted | `BLOCKED_DRAFT_UPSTREAM` | Human contract review first | No |
| `FAIL-WF-007` — scope expansion | Proposed path/operation outside boundary | `BLOCKED_SCOPE_EXPANSION` | Request explicit new scope | No |
| `FAIL-WF-008` — candidate changed after freeze | Digest mismatch | `BLOCKED_STALE_CANDIDATE` | Create new revision and repeat later gate | No |
| `FAIL-WF-009` — validation mutation | Ending identity differs | `FAIL_VALIDATION_MUTATED_SUBJECT` | Preserve evidence; separate correction stage | No |
| `FAIL-WF-010` — Evidence treated as approval | Authority mapping violation | `BLOCKED_AUTHORITY_CONFLATION` | Obtain exact human decision | No |
| `FAIL-WF-011` — external instruction injection | External content requests action/scope change | `BLOCKED_UNTRUSTED_INSTRUCTION` | Treat content as data; return to human goal | No |
| `FAIL-WF-012` — partial documentation write | Expected inventory/content incomplete | `FAIL_PARTIAL_WRITE` | Preserve state; report exact files; separate correction | No |

## 10. Mandatory negative scenarios

| Scenario ID | Attempt | Expected result |
|---|---|---|
| `NEG-WF-001` | Start Slice A without accepted G1 | `BLOCKED_MISSING_G1` |
| `NEG-WF-002` | Use missing or changed reference commit as current Evidence | `BLOCKED_REFERENCE_ACCESS` or `STALE` |
| `NEG-WF-003` | Reuse human decision after bound subject revision changes | `BLOCKED_STALE_DECISION` |
| `NEG-WF-004` | Create Task from DRAFT contract | `BLOCKED_DRAFT_UPSTREAM` |
| `NEG-WF-005` | Expand allowed paths during execution | `BLOCKED_SCOPE_EXPANSION` |
| `NEG-WF-006` | Validation changes candidate | `FAIL_VALIDATION_MUTATED_SUBJECT` |
| `NEG-WF-007` | Treat Evidence or PASS as Git authority | `BLOCKED_AUTHORITY_CONFLATION` |
| `NEG-WF-008` | Agent self-assigns Risk Profile | `BLOCKED_HUMAN_RISK_DECISION_REQUIRED` |
| `NEG-WF-009` | Dashboard or adapter changes lifecycle state | `BLOCKED_DERIVED_VIEW_MUTATION` |
| `NEG-WF-010` | Missing answer converted to explicit `NONE` | `CONTRACT_VIOLATION` |
| `NEG-WF-011` | Product review automatically begins Task compilation | `BLOCKED_AUTOMATIC_TRANSITION` |
| `NEG-WF-012` | Resume record omits dirty/uncommitted state | `BLOCKED_INCOMPLETE_STATE_BINDING` |

## 11. Recovery principles

1. Preserve original input and actual repository state.
2. Identify whether failure occurred before write, during partial write, after freeze, or during read-only validation.
3. Record exact changed paths and side effects.
4. Never clean unrelated user state.
5. Never retry after scope, identity, authority, or human-decision failure.
6. Restore exact source or create a new explicit revision; do not silently rewrite evidence.
7. Correction is a separate `EXECUTE` stage.
8. Re-validation is separately authorized and uses the new candidate identity.

## 12. DRAFT workflow requirement register

| Requirement ID | Workflow requirement | Trace |
|---|---|---|
| `REQ-WF-001` | Original input and every clarification answer retain provenance | `J-CV1-001`, `REQ-CV1-001` |
| `REQ-WF-002` | Each transition declares actor and authority | `TR-A-001..006` |
| `REQ-WF-003` | Missing/unknown/conflict state remains visible | `FAIL-WF-001..004` |
| `REQ-WF-004` | Human gate blocks dependent transition only | G1/G2/contract acceptance tables |
| `REQ-WF-005` | Review candidate freezes exact revision/hash | `TR-A-005`, `FAIL-WF-008` |
| `REQ-WF-006` | Task eligibility requires accepted upstream IDs | `J-CV1-002`, `NEG-WF-004` |
| `REQ-WF-007` | Resume refreshes mutable repository facts | `J-CV1-003` |
| `REQ-WF-008` | Failure produces recovery facts and stop | Failure/recovery matrix |
| `REQ-WF-009` | Validation remains read-only | `NEG-WF-006` |
| `REQ-WF-010` | One next action names required authority | All journey terminals |

The 32 requirement definitions remain accepted because their exact rows are unchanged. Upstream `PSC-A-001` and the three `WFC-A/B/C-001` contracts changed and are stale against `DEC-CONTRACT-001`. Under human-selected rule `A2`, the current `AC-WFC-A-001-01..07` definitions are owned by the WFC-A envelope and differ from the persisted C1 rows, so their historical C1 bindings are also stale. The ten `AC-WFC-B/C-*` definitions and the two shared schema records are new DRAFT subjects.

## 13. Workflow acceptance owner and derived mirror

The fenced `executable_acceptance` list inside each `WFC-*` contract envelope is the single normative definition owner. The tables below are exact derived mirrors for navigation and disposition only; they have no independent definition authority.

| Acceptance ID | Exact envelope-owned observable condition | Current disposition |
|---|---|---|
| `AC-WFC-A-001-01` | original input identity is preserved | `STALE` |
| `AC-WFC-A-001-02` | material missing fields produce bounded questions without invented answers | `STALE` |
| `AC-WFC-A-001-03` | DRAFT Product Spec and Feature Passport expose facts, assumptions, unknowns, conflicts, scope, and non-goals | `STALE` |
| `AC-WFC-A-001-04` | every transition names actor, authority, state effect, and allowed side effect | `STALE` |
| `AC-WFC-A-001-05` | sensitive or conflicting input blocks only the affected external or product claim | `STALE` |
| `AC-WFC-A-001-06` | terminal state is HUMAN_REVIEW_REQUIRED with exactly one decision request | `STALE` |
| `AC-WFC-A-001-07` | no Task, implementation, validation, or Git authority is produced | `STALE` |

### New DRAFT acceptance IDs requiring a separate human contract decision

| Acceptance ID | Exact envelope-owned observable condition | Current disposition |
|---|---|---|
| `AC-WFC-B-001-01` | eligible current accepted input produces exactly one bounded AOS3-DPKG-TASK-### candidate | `DRAFT` |
| `AC-WFC-B-001-02` | every derived requirement, contract, acceptance, scenario, and decision binding is current and accepted | `DRAFT` |
| `AC-WFC-B-001-03` | PORTABLE_UNBOUND output leaves repository, paths, commands, dependencies, and executable checks UNASSIGNED | `DRAFT` |
| `AC-WFC-B-001-04` | DRAFT, stale, rejected, missing-required-instance, orphan, cycle, or scope-expanding input produces zero Task files and no Queue | `DRAFT` |
| `AC-WFC-B-001-05` | terminal output requests human Task review, names exactly one next action, preserves all implementation/validation/Git non-grants, and stops | `DRAFT` |
| `AC-WFC-C-001-01` | ResumeRecord binds exact root, worktree, branch, HEAD, candidate, baseline, and decision identities, using explicit NOT_APPLICABLE only where the subject has no such axis | `DRAFT` |
| `AC-WFC-C-001-02` | every changed subject or decision hash is classified STALE and blocks only dependent claims/actions | `DRAFT` |
| `AC-WFC-C-001-03` | read-only resume produces zero inspected-source writes and reports before/after identity | `DRAFT` |
| `AC-WFC-C-001-04` | unknown operation outcome forbids automatic retry and requires actual-state reconciliation plus new human authority | `DRAFT` |
| `AC-WFC-C-001-05` | terminal output contains exactly one safe next action, names the required human authority, preserves implementation/validation/Git non-grants, and stops at human review | `DRAFT` |

## 14. G2 outcomes and remaining workflow questions

G2 decided:

- conversational adapter plus portable text/JSON and CLI boundary;
- repository-relative Markdown/YAML/JSON Project Memory;
- `LOCAL_DECLARED_HASH_BOUND` Human Decisions;
- minimal human-owned Risk action classes;
- local-only Core with no external provider transmission;
- greenfield compatibility.

Remaining:

  - new exact acceptance for corrected `PSC-A-001`, `WFC-A-001`, `WFC-B-001`, `WFC-C-001`, stale `AC-WFC-A-001-01..07`, new DRAFT `AC-WFC-B/C-001-01..05`, `SCH-PRODUCT-SPEC-001`, and `SCH-FEATURE-PASSPORT-001`;
- future exact implementation-repository binding before physical preflight/execution;
- exact dependency/test entrypoints after that future binding;
- later human decision on stabilization thresholds.

## 15. One next action

```yaml
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
