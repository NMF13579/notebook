---
artifact_id: AOS-FIRST-SLICE-DECISION-PACKAGE-R1
document_type: FIRST_SLICE_HUMAN_DECISION_PACKAGE
revision: R1
status: DRAFT
task_id: INT-DOC-200
execution_id: INT-DOC-200-EXECUTE-001
stage: EXECUTE
fact_class: SYNTHESIZED
comparison_profile: OUTCOME_FIRST_THREE_EQUAL_CANDIDATES
execution_authorization:
  actor_class: HUMAN
  exact_visible_utf8_text: HUMAN_AUTHORIZE_EXACT_INT_DOC_200_EXECUTION
  utf8_byte_length: 43
  sha256: 42d746976548984db846f84da89d953ddf56b46d30e6f2d7fc9d138a60814e06
  runtime_turn_id: UNAVAILABLE_AT_RUNTIME
design_approval:
  breadth:
    actor_class: HUMAN
    decision: THREE_EQUAL_CANDIDATES
    exact_visible_utf8_text: Вариант А
    utf8_byte_length: 17
    sha256: 892c6126258887c630b7bc1f2eddef579f2c7f300e9d75162d2b982d8eafbf04
  method:
    actor_class: HUMAN
    decision: OUTCOME_FIRST_SCORECARD
    exact_visible_utf8_text: Вариант 1
    utf8_byte_length: 16
    sha256: f7a82cd6e1887bc43d54aa5c82f7490cdc97a5371ca309a180b18e97c4e6fd26
activation_record:
  path: planning/INT_DOC_200_Activation_Record.md
  byte_length: 3102
  sha256: d6225cb9be1d4413eff4aaf4e39729ea4e73efca697e2695f650fe869b1a52e6
accepted_predecessor:
  path: planning/foundation/AOS_Product_Runtime_Foundation_Package_R1.md
  byte_length: 31342
  sha256: 8b1ab2c4da097380b73f7b563d9a44cb7ed12a786aabe438905152e1ccaef3af
  subject_set_sha256: aba036501bdf97e660bf894c8b40ccce2ceec6db9103bc30569bd66ca1e78350
feature_refs: [FTR-001, FTR-002, FTR-003, FTR-005]
candidate_ids: [FS-CAND-001, FS-CAND-002, FS-CAND-003]
output_path: planning/first-slice/AOS_First_Slice_Decision_Package_R1.md
recommendation: FS-CAND-001_FOR_HUMAN_CONSIDERATION
recommendation_class: SYNTHESIZED
human_first_segment_decision: NOT_RUN
human_first_job_decision: NOT_RUN
human_first_slice_decision: NOT_RUN
canonical_post_stop_validation: NOT_RUN
human_acceptance: NOT_RUN
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
authority_effect: NONE
---

# AOS First-Slice Decision Package R1

## 1. Purpose and decision boundary

This package gives a human three equally structured candidates for the first
observable Product Runtime slice. It compares them against the accepted product
baseline and Product Runtime Foundation without selecting a segment, job or
slice on the human's behalf.

The package is decision support, not a Product Spec, accepted Feature Passport,
architecture decision, Task Brief, implementation plan or Execution
Authorization. Its recommendation is a `SYNTHESIZED` proposal and has no
authority effect.

```yaml
document_maturity: DRAFT
technical_validation: NOT_RUN
human_decision: NOT_RUN
selected_candidate: null
first_segment: UNDECIDED
first_job: UNDECIDED
first_vertical_slice: UNDECIDED
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
```

## 2. Authoritative inputs and provenance

| Input | Fact class used here | Role |
|---|---|---|
| [Core](../../docs/00_Core.md) | Human-accepted baseline | Authority, status and safety boundaries |
| [Product](../../docs/01_Product.md) | Human-accepted product baseline | Problems, users, journeys and slice criteria |
| [Architecture](../../docs/02_Architecture.md) | Human-accepted architecture baseline | Contract classes and layer boundaries |
| [Features](../../docs/06_Features.md) | Accepted inventory; item dispositions remain `UNDECIDED` | `FTR-001`, `FTR-002`, `FTR-003`, `FTR-005` dossiers |
| [Lessons](../../docs/04_Lessons.md) | `LESSON_PROPOSAL` regression candidates | Prevent shallow dossiers, simulated decisions and premature automation |
| [Product Runtime Foundation](../foundation/AOS_Product_Runtime_Foundation_Package_R1.md) | Human-accepted Foundation documentation | Runtime boundary, status, recovery, authority and handoff constraints |
| [R9](../AOS_Documentation_Task_Sequence_R9.md) | Human-accepted roadmap | `INT-DOC-200` outcome and stage route |
| [Task Manifest](../AOS_Documentation_Task_Manifest_R1.md) | Accepted documentation-control artifact | Start condition, closure and successor routing |
| [INT-DOC-100 acceptance](../INT_DOC_100_Acceptance_Record.md) | Human acceptance record | Exact predecessor closure |
| [INT-DOC-200 activation](../INT_DOC_200_Activation_Record.md) | Human activation record | Exact active interval and execution boundary |
| [CURRENT](../CURRENT.md) | Durable lifecycle owner | Current interval and authority state |

The candidate descriptions below are synthesis from these inputs. They are not
observed runtime behavior and do not change feature dispositions.

## 3. Outcome-first comparison method

### 3.1 Eligibility gates

Every candidate must satisfy all of these gates before it can be recommended
for a human decision:

1. solve an identified user problem rather than an internal agent problem;
2. produce one result visible and understandable without reading internals;
3. form one bounded end-to-end journey with described inputs and outputs;
4. expose states, failures, recovery, limitations and one next action;
5. support manual acceptance and negative scenarios;
6. work without a full Factory, Control Plane, extension system or Git delivery;
7. preserve `NOT_RUN`, `UNKNOWN`, `NOT_FOUND` and `CONFLICT` honestly;
8. require explicit human decisions for selection, architecture and mutation;
9. leave implementation repository, interface, language and dependencies
   unbound;
10. create useful learning for the next exact contract task.

Failure of a gate makes the candidate `NOT_ELIGIBLE` for selection from this
revision. Missing Evidence is `UNKNOWN`, not an automatic failure or a zero
score.

### 3.2 Qualitative ratings

| Rating | Meaning |
|---|---|
| `STRONG` | Directly supported by accepted inputs with few unbound dependencies |
| `MODERATE` | Plausible and bounded, but requires one or more material later decisions |
| `WEAK` | Value or feasibility depends heavily on unbound target facts |
| `UNKNOWN` | Current Evidence cannot support a comparative claim |

No numeric aggregate is produced. A recommendation must explain its trade-offs
and remains separate from human selection.

### 3.3 Comparison dimensions

- clarity of the user's observable outcome;
- minimal dependency surface;
- manual end-to-end testability;
- fit with the accepted Product Runtime Foundation;
- learning value for the next slice;
- amount of protected decision-making required before implementation;
- risk of leaking Development Factory or Governance scope into the slice.

## 4. Candidate `FS-CAND-001` — Guided intent to reviewable Feature Passport

### 4.1 Segment, job and observable outcome

```yaml
candidate_id: FS-CAND-001
segment_candidate: NONPROGRAMMER_OR_DOMAIN_EXPERT_WITH_A_NEW_PRODUCT_IDEA
job_candidate: >-
  Explain a real problem in ordinary language and receive a bounded,
  reviewable definition of the first feature without implementation assumptions.
observable_outcome_candidate: >-
  A versioned Intent Record plus one DRAFT Feature Passport whose problem,
  user outcome, assumptions, unknowns, boundaries, acceptance and one next
  decision are visible to the user.
primary_feature_refs: [FTR-001, FTR-003]
supporting_feature_refs: [FTR-005]
FTR-002_role: NOT_REQUIRED_FOR_GREENFIELD_BASELINE
human_selection_status: NOT_RUN
```

This candidate tests the central AOS promise: a nontechnical user can turn an
idea into a precise, reviewable product artifact while retaining decision
authority.

### 4.2 Trigger, inputs and outputs

**Trigger:** a user supplies a new product problem or incomplete idea and asks
what a bounded first feature could be.

**Inputs:** original request, user corrections, constraints, non-goals,
sensitivity flags and accepted project facts if any.

**Outputs:**

- original-request-preserving Intent Record;
- explicit understood / assumed / unknown classification;
- one DRAFT Feature Passport with users, trigger, I/O, flow, states, failures,
  recovery, boundaries, acceptance and negative scenarios;
- architecture need status of `NEED_CHECK_PENDING`, `NO_ADR_PROPOSED` or
  `ADR_QUESTION_REQUIRED`, never a generated architecture decision;
- one next human action.

### 4.3 Minimal end-to-end flow

```text
first contact
→ preserve original request
→ separate problem/outcome from proposed solution
→ ask only material questions
→ show understood / assumed / unknown
→ human corrects the interpretation
→ construct one DRAFT Feature Passport
→ run completeness Self-Test over the artifact
→ show review package and one next decision
→ stop
```

### 4.4 States and transitions

```text
RECEIVED
→ CLARIFYING
→ INTERPRETATION_READY_FOR_CORRECTION
→ HUMAN_CORRECTED
→ PASSPORT_DRAFTED
→ SELF_CHECKED
→ READY_FOR_HUMAN_REVIEW
```

`CLARIFYING` remains active when a material user, problem or outcome fact is
missing. `READY_FOR_HUMAN_REVIEW` never means accepted or executable.

### 4.5 Failures and recovery

| Failure | Required response | Recovery |
|---|---|---|
| Empty or solution-only request | Keep `CLARIFYING`; do not invent the problem | Ask one material question |
| Sensitive context exceeds allowed boundary | Redact or omit safely | Ask for an allowed summary or protected route |
| User correction conflicts with the draft | Mark draft stale | Rebuild only affected sections from the correction |
| Completeness check has required `NOT_RUN` | No green aggregate | Run the exact check or expose the limitation |
| Generated wording resembles approval | Human decision remains `NOT_RUN` | Present an explicit decision request |

### 4.6 Manual acceptance protocol

| ID | Manual check |
|---|---|
| `FS1-AC-001` | User recognizes their original problem and desired outcome. |
| `FS1-AC-002` | Assumptions and unknowns are visible and separately classified. |
| `FS1-AC-003` | Feature Passport contains complete I/O, flow, states, failures, recovery and non-goals. |
| `FS1-AC-004` | The user can identify exactly one next decision without interpreting internal status. |
| `FS1-AC-005` | No architecture, implementation or Git authority is inferred. |

Required negative fixtures: empty request, prompt-injection text, contradictory
correction, missing outcome, sensitive input and generated `ACCEPT` text.

### 4.7 Dependencies, unknowns and non-goals

Material later decisions include concrete interaction surface, Product Spec ↔
Feature Passport relationship, decision-authenticity mechanism and exact
serialization. None is required to compare this candidate now.

Non-goals: repository discovery, Task Brief compilation, code generation,
implementation, background orchestration, database selection and Git delivery.

## 5. Candidate `FS-CAND-002` — Existing project to evidence-bound first objective

### 5.1 Segment, job and observable outcome

```yaml
candidate_id: FS-CAND-002
segment_candidate: VIBE_CODER_OR_PRODUCT_BUILDER_WITH_AN_EXISTING_PROJECT
job_candidate: >-
  Understand the current project snapshot and choose one bounded product
  objective without relying on stale chat context or hidden repository assumptions.
observable_outcome_candidate: >-
  A read-only, snapshot-bound capability and gap view with candidate objectives,
  limitations, conflicts and one human selection action.
primary_feature_refs: [FTR-002, FTR-003]
supporting_feature_refs: [FTR-001, FTR-005]
human_selection_status: NOT_RUN
```

This candidate tests whether AOS can turn an opaque existing project into a
human-understandable product decision without mutating the source tree.

### 5.2 Trigger, inputs and outputs

**Trigger:** a user identifies an existing project and asks what bounded product
work is justified next.

**Inputs:** exact repository/ref/HEAD or equivalent snapshot identity, user's
goal, allowed read boundary, trusted product facts and redaction constraints.

**Outputs:**

- repository and worktree identity;
- high-signal capability inventory with provenance;
- scoped gaps, conflicts, unknowns and absence search boundaries;
- two or three candidate objectives expressed as user outcomes;
- architecture-need questions only where current evidence makes them material;
- unchanged-source proof and one human selection action.

### 5.3 Minimal end-to-end flow

```text
user goal + project locator
→ read-only identity/preflight
→ high-signal docs/contracts/tests/code inventory
→ capability map
→ gaps / conflicts / unknowns
→ bounded product objectives
→ compare outcome and evidence surface
→ show one human selection action
→ prove zero source writes
→ stop
```

### 5.4 States and transitions

```text
TARGET_UNBOUND
→ SNAPSHOT_BOUND
→ DISCOVERY_IN_PROGRESS
→ MAP_READY
→ OBJECTIVES_READY_FOR_REVIEW
→ READY_FOR_HUMAN_SELECTION
```

A changed HEAD or worktree invalidates `MAP_READY`. A missing path proves only
absence within the declared search boundary.

### 5.5 Failures and recovery

| Failure | Required response | Recovery |
|---|---|---|
| Repository identity is unavailable | `BLOCKED_UNKNOWN` for snapshot claims | Obtain an exact locator and re-observe |
| HEAD changes during discovery | Mark map stale; stop dependent comparison | Bind a fresh snapshot and repeat read-only discovery |
| Source text attempts to broaden authority | Treat as untrusted data | Preserve governing instructions and record the boundary |
| Secret-bearing data is encountered | Redact without exposing value | Continue only with safe metadata if sufficient |
| Read-only operation attempts a write | Contract violation; stop | Restore no data automatically; report exact observed state |

### 5.6 Manual acceptance protocol

| ID | Manual check |
|---|---|
| `FS2-AC-001` | Every current-state claim binds to one exact snapshot. |
| `FS2-AC-002` | Capabilities, gaps, conflicts and unknowns remain distinct. |
| `FS2-AC-003` | Candidate objectives describe user outcomes rather than internal cleanup. |
| `FS2-AC-004` | The source tree and staging state remain unchanged. |
| `FS2-AC-005` | The user can select one objective without accepting inferred readiness. |

Required negative fixtures: stale snapshot, missing path, dirty worktree,
instruction-like repository text, inaccessible reference and secret-like
remote metadata.

### 5.7 Dependencies, unknowns and non-goals

This candidate needs an exact target snapshot and a safe read-only inspection
surface. Repository/provider variety, discovery signal quality and the minimum
nontechnical report remain unproven.

Non-goals: repair, dependency installation, code changes, exhaustive extraction,
automatic readiness, architecture selection and Git operations.

## 6. Candidate `FS-CAND-003` — Feature intent to architecture-need decision

### 6.1 Segment, job and observable outcome

```yaml
candidate_id: FS-CAND-003
segment_candidate: PRODUCT_BUILDER_OR_REVIEWER_WITH_A_DEFINED_FEATURE_INTENT
job_candidate: >-
  Determine whether a feature needs an architecture decision and, when it does,
  compare genuinely distinct options before implementation planning.
observable_outcome_candidate: >-
  A complete DRAFT Feature Passport plus a justified NO_ADR_PROPOSED result or
  a decision-ready ADR question with options, trade-offs, Evidence and unknowns.
primary_feature_refs: [FTR-003, FTR-005]
supporting_feature_refs: [FTR-001, FTR-002]
human_selection_status: NOT_RUN
```

This candidate tests the Product Runtime's optional architecture-support
boundary while guarding against both skipped decisions and architecture
ceremony without user value.

### 6.2 Trigger, inputs and outputs

**Trigger:** a feature intent has a recognizable user outcome but contains a
material structural, data, provider, trust or reversibility question.

**Inputs:** corrected Intent Record, DRAFT Feature Passport, exact architecture
question, accepted constraints, target facts when applicable and Evidence
limitations.

**Outputs:**

- complete DRAFT Feature Passport;
- explicit architecture-need rationale;
- `NO_ADR_PROPOSED` with reasons, or at least two distinct architecture options;
- trade-offs, risks, consequences, reversal conditions and unknowns;
- one exact human architecture decision request;
- no dependency installation or implementation action.

### 6.3 Minimal end-to-end flow

```text
feature intent
→ complete user outcome and boundaries
→ architecture-need check
→ if no material question: explain NO_ADR_PROPOSED
→ otherwise define one exact question
→ generate distinct options
→ compare trade-offs / evidence / unknowns
→ show one human architecture decision action
→ stop before Task Brief or implementation
```

### 6.4 States and transitions

```text
FEATURE_INTENT_READY
→ PASSPORT_COMPLETE
→ ARCHITECTURE_NEED_CHECKED
→ NO_ADR_PROPOSED | ADR_OPTIONS_READY
→ READY_FOR_HUMAN_DECISION
```

No state records a selected architecture without an exact human decision.

### 6.5 Failures and recovery

| Failure | Required response | Recovery |
|---|---|---|
| Feature lacks an observable user outcome | Reject architecture-first route | Return to bounded feature clarification |
| Only one preselected option is presented | Decision package is insufficient | Derive a distinct alternative or expose the blocker |
| Target fact is stale or missing | Mark affected comparison `UNKNOWN` | Refresh the exact fact or narrow the decision |
| Trivial reversible choice triggers ceremony | Propose `NO_ADR_PROPOSED` | Record rationale and continue only after review |
| Recommendation is treated as selection | Human decision remains `NOT_RUN` | Request an exact human decision |

### 6.6 Manual acceptance protocol

| ID | Manual check |
|---|---|
| `FS3-AC-001` | Architecture work is linked to one observable feature outcome. |
| `FS3-AC-002` | Need/no-need rationale is explicit and reversible. |
| `FS3-AC-003` | Any ADR route contains at least two genuinely distinct options. |
| `FS3-AC-004` | Evidence and unknowns are visible per option. |
| `FS3-AC-005` | No architecture decision, dependency or implementation is selected automatically. |

Required negative fixtures: missing user outcome, single-option ADR, stale target
fact, architecture wording copied from legacy and generated selection text.

### 6.7 Dependencies, unknowns and non-goals

This candidate depends on a sufficiently complete feature intent. Concrete
architecture questions may also require a target snapshot, data/provider
constraints and human risk direction that are currently unbound.

Non-goals: general architecture synthesis, framework selection, dependency
installation, implementation topology, Task Brief generation and execution.

## 7. Comparative scorecard

| Dimension | `FS-CAND-001` Guided intent | `FS-CAND-002` Existing project | `FS-CAND-003` Architecture need |
|---|---|---|---|
| Observable user outcome | `STRONG` | `STRONG` | `MODERATE` |
| Minimal dependency surface | `STRONG` | `WEAK` | `MODERATE` |
| Manual end-to-end testability | `STRONG` | `MODERATE` | `MODERATE` |
| Product Runtime Foundation fit | `STRONG` | `STRONG` | `MODERATE` |
| Learning value for later slices | `STRONG` | `STRONG` | `MODERATE` |
| Can avoid target binding initially | `STRONG` | `WEAK` | `MODERATE` |
| Can avoid Factory/Governance leakage | `STRONG` | `MODERATE` | `WEAK` |

### 7.1 Material trade-offs

`FS-CAND-001` has the shortest route to a nontechnical, user-visible result and
the fewest target-specific dependencies. Its main risk is producing a polished
document without proving that the user can understand and correct it.

`FS-CAND-002` exercises valuable repository Evidence and read-only safety, but
it requires target binding and representative project fixtures before its
observable claims can be tested honestly.

`FS-CAND-003` exercises an important optional boundary, but its value depends on
a feature mature enough to contain a real architecture question. It has the
highest risk of turning planning ceremony into the product.

### 7.2 Eligibility result

All three candidates remain eligible for human consideration at documentation
level. No current Evidence establishes runtime feasibility or product-market
priority. Ratings compare only the accepted contract inputs.

## 8. Recommendation — separate from selection

```yaml
recommendation:
  candidate_id: FS-CAND-001
  classification: SYNTHESIZED
  reason: >-
    It most directly tests the accepted AOS promise for a nontechnical user,
    has the smallest unbound dependency surface, is manually testable without
    an implementation repository, and creates an artifact usable by later
    exact-slice and Task Brief work.
  human_decision_effect: NONE
  implementation_effect: NONE
```

The recommendation is not a selection. A human may select another candidate,
request changes to the comparison or defer the decision.

## 9. Evidence gaps and questions for the human

| ID | Gap or question | Affected candidates | Effect before human selection |
|---|---|---|---|
| `FS-GAP-001` | Which first segment has the strongest real need: domain expert, existing-project builder or feature reviewer? | All | Human product decision required |
| `FS-GAP-002` | What concrete user problem and success signal will be used for dogfood? | All | Exact job/outcome decision required |
| `FS-GAP-003` | Is an existing repository required for the first proof? | 002, 003 | Target-binding dependency remains `UNKNOWN` |
| `FS-GAP-004` | What interaction surface is acceptable for manual proof? | All | Deferred until exact slice contract |
| `FS-GAP-005` | How is the human decision authenticated and persisted? | All | Decision-record contract remains open |
| `FS-GAP-006` | Which data/provider sensitivity constraints apply? | All | Affected context may require a protected route |

These gaps do not block read-only human comparison. They block only the
dependent contract or implementation action.

## 10. Human decision protocol

The human decision must identify this exact frozen document revision and one
candidate. A suitable exact decision form after canonical validation is:

```text
HUMAN_DECIDE_INT_DOC_200_FIRST_SLICE: SELECT <FS-CAND-001|FS-CAND-002|FS-CAND-003>;
candidate_sha256=<frozen-document-sha256>;
validation_id=<exact-validation-id>;
segment=<human-authored-segment>;
job=<human-authored-job>;
observable_outcome=<human-authored-outcome>
```

Other valid decisions are `NEEDS_CHANGES`, `REJECT` or `DEFER`, bound to the
same exact candidate. Generated or inferred text cannot fill this field.

## 11. Handoff boundary to `INT-DOC-210`

Only an exact human selection after canonical validation may unblock
`INT-DOC-210`. The handoff then consists of:

- selected candidate ID and exact human-authored segment/job/outcome;
- frozen `INT-DOC-200` document identity and validation identity;
- applicable candidate dossier, acceptance and negative scenarios;
- unresolved Evidence gaps and protected decisions;
- accepted Product Runtime Foundation identity;
- explicit non-authority for repository, implementation and Git actions.

`INT-DOC-210` must turn that selection into an exact First-Slice Contract and
portable handoff package. It must not treat this comparison or recommendation
as the human decision.

## 12. Traceability matrix

| Concern | Owner or feature | Package coverage |
|---|---|---|
| Original problem and explicit unknowns | `FTR-001`, `C-001` | Candidate 001 intake; supporting boundary in 002/003 |
| Read-only project Evidence | `FTR-002` | Candidate 002 primary; optional target facts in 003 |
| Product Spec, Feature Passport and slice comparison | `FTR-003`, `C-002`, `C-003` | All three dossiers and scorecard |
| Architecture need and options | `FTR-005`, `C-004` | Candidate 003 primary; bounded need check in 001/002 |
| Status, one next action and no false green | Accepted Foundation | Every candidate flow and failure route |
| Human decision authenticity | `C-011`, Core authority model | Section 10 exact human gate |
| Runtime/Factory separation | Product and Architecture baselines | Non-goals and handoff boundaries |
| Avoid shallow feature artifacts | `LES-003` proposal | Complete I/O, states, failures, recovery and tests |
| Avoid premature Governance/ceremony | `LES-004`, `LES-006`, `LES-037` proposals | Eligibility gates and comparative risks |
| Do not simulate human decisions | `LES-008`, `LES-009`, `LES-011` proposals | Recommendation/selection split and scoped unknowns |
| Keep Runtime outcome visible | `LES-032`, `LES-033`, `LES-034`, `LES-035` proposals | Observable outcomes and end-to-end manual checks |

Lesson references are regression candidates, not independent authority.

## 13. Required package-level negative scenarios

| ID | Scenario | Required result |
|---|---|---|
| `FSD-NEG-001` | Agent marks its recommendation as selected | Reject; `human_first_slice_decision` remains `NOT_RUN` |
| `FSD-NEG-002` | Candidate lacks an observable user outcome | Candidate becomes `NOT_ELIGIBLE` |
| `FSD-NEG-003` | Missing Evidence is converted to a low score | Replace with `UNKNOWN` and scope the affected claim |
| `FSD-NEG-004` | Comparison silently assumes repository, language or framework | Remove assumption or expose a protected later decision |
| `FSD-NEG-005` | Internal control machinery is presented as product value | Reject or reframe as a user-visible outcome |
| `FSD-NEG-006` | Candidate requires full Factory or Governance | Candidate becomes `NOT_ELIGIBLE` for the first Runtime slice |
| `FSD-NEG-007` | Successful documentation validation is treated as runtime proof | Runtime verification remains `NOT_RUN` |
| `FSD-NEG-008` | Human selects a candidate without exact frozen identity | Decision is not sufficient for `INT-DOC-210` |
| `FSD-NEG-009` | Architecture recommendation is treated as an ADR decision | Human architecture decision remains `NOT_RUN` |
| `FSD-NEG-010` | Git or implementation action is inferred from selection | Permission remains `HUMAN_AUTHORIZATION_REQUIRED` or `NONE` |

## 14. Known unknowns and deferred decisions

```yaml
first_segment: UNDECIDED
first_job: UNDECIDED
first_vertical_slice: UNDECIDED
concrete_interface: UNDECIDED
implementation_repository: UNASSIGNED
target_repository_identity: UNBOUND
language: UNDECIDED
toolchain: UNDECIDED
dependencies: UNDECIDED
project_memory_persistence: UNDECIDED
decision_authenticity_mechanism: UNDECIDED
risk_profile: UNASSIGNED
runtime_evidence: NOT_RUN
```

These facts are intentionally deferred. This package is usable for human
comparison without resolving them and cannot resolve them by inference.

## 15. Completion and validation route

The `INT-DOC-200` `EXECUTE` candidate is internally complete only when:

1. exactly three candidates use the same dossier and comparison method;
2. every candidate states segment, job, observable outcome, I/O, states,
   failures, recovery, dependencies, non-goals and manual checks;
3. all four feature references are traceable without changing disposition;
4. the scorecard uses qualitative Evidence-bound ratings without false
   precision;
5. recommendation and human selection remain separate;
6. unresolved decisions remain visible and owner-bound;
7. `INT-DOC-210`, implementation and Git boundaries remain closed;
8. Markdown, frontmatter, links, IDs and allowed paths pass internal checks;
9. the final candidate is frozen by exact byte identity in the terminal Stage
   Report.

After freeze, the route is:

```text
terminal EXECUTE Stage Report
→ STOP
→ separately authorized read-only POST_STOP_DOCUMENTATION VALIDATE
→ human first-slice decision over the exact validated candidate
```

```yaml
artifact_status: DRAFT
internal_check_result_owner: TERMINAL_EXECUTE_STAGE_REPORT
freeze_identity_owner: TERMINAL_EXECUTE_STAGE_REPORT
canonical_post_stop_validation: NOT_RUN
human_first_slice_decision: NOT_RUN
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_operations:
  commit: NOT_RUN
  push: NOT_RUN
  merge: NOT_RUN
  release: NOT_RUN
authority_effect: NONE
```
