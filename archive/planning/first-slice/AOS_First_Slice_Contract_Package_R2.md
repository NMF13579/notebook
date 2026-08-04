---
artifact_id: AOS-FIRST-SLICE-CONTRACT-PACKAGE-R2
document_type: EXACT_FIRST_SLICE_CONTRACT_AND_HANDOFF_PACKAGE
revision: R2
status: DRAFT
task_id: X1-DOCUMENTATION-SUCCESSOR-CONTRACT-R2-001
execution_id: X1-DOCUMENTATION-SUCCESSOR-CONTRACT-R2-001
stage: EXECUTE
fact_class: SYNTHESIZED
output_path: planning/first-slice/AOS_First_Slice_Contract_Package_R2.md
predecessor:
  path: planning/first-slice/AOS_First_Slice_Contract_Package_R1.md
  byte_length: 47582
  sha256: 8c8169d5b45ebce7e6feacb49e9f058f3d08d0de2dea5ebee96cc3b73f4d85f0
  status: HUMAN_ACCEPTED_FROZEN
  mutation: NONE
selected_candidate: FS-CAND-001
selected_segment: NONPROGRAMMER_OR_DOMAIN_EXPERT_WITH_A_NEW_PRODUCT_IDEA
selected_interaction_surface: SURFACE-A_PROVIDER_NEUTRAL_GUIDED_CONVERSATION
feature_mapping: ACCEPTED_COMPOSITE_FTR_001_PLUS_FTR_003
primary_feature_refs: [FTR-001, FTR-003]
supporting_feature_refs: [FTR-005, FTR-006, FTR-011, FTR-012, FTR-013]
C002_feature_id_scope: OUTPUT_INSTANCE_SCOPED
static_composite_C002_feature_id: NOT_APPLICABLE
identifier_allocation_rule: TARGET_BOUND_UNDECIDED
architecture_need_result: NO_ADR_REQUIRED_WITH_EXPLICIT_RATIONALE
portable_task_candidate_id: PTC-AOS-FIRST-SLICE-001
portable_task_candidate_revision: 7
portable_task_candidate_manifest_sha256: 18816ffe7851b79e7c9f7cbd976fbc72c1936af233bd57e5e6ca71b6338cb370
human_decision_binding:
  id: X1-PD-C002-001
  subject: FS-CAND-001_C002_IDENTITY_SEMANTICS
  decision: C002_FEATURE_ID_IS_OUTPUT_INSTANCE_SCOPED
  fact_class: CURRENT_EXPLICIT_HUMAN_DECISION
  exact_payload_utf8_byte_length: 536
  exact_payload_sha256: 8dc24bf0390e3d8cce1e508b10224034203fc92fa8364be8f26c10c9cf4f162a
execution_authorization:
  actor_class: HUMAN
  task_id: X1-DOCUMENTATION-SUCCESSOR-CONTRACT-R2-001
  decision: AUTHORIZE
  locator: CODEX_CURRENT_THREAD_HUMAN_MESSAGE
  allowed_paths:
    - planning/first-slice/AOS_First_Slice_Contract_Package_R2.md
  operation: CREATE_TARGET_UNBOUND_R2_SUCCESSOR_PRODUCT_CONTRACT
  independent_validation: NOT_AUTHORIZED
  implementation: FORBIDDEN
  git_operations: FORBIDDEN
  one_shot: true
canonical_post_stop_validation: NOT_RUN
human_acceptance: NOT_RUN
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
authority_effect: NONE
---


# AOS First-Slice Contract and Handoff Package R2

## 1. Purpose and status boundary

This package defines the exact documentation-level contract for the
human-selected `FS-CAND-001` first Product Runtime slice. A nonprogrammer or
domain expert uses a provider-neutral guided conversation to turn an ordinary-
language product problem into a versioned Intent Record and one DRAFT Feature
Passport ready for human review.

This R2 successor preserves every accepted R1 product-behavior boundary. Its
only Product Contract deltas bind the accepted `FTR-001 + FTR-003` primary
mapping, the five supporting-control dispositions and the human decision that
C-002 `feature_id` is scoped to each produced Feature Passport instance. R1
remains frozen and independently identifiable.

The package is an implementation-handoff-ready logical contract. It is not a
runtime, accepted feature, target-bound Task Brief, Architecture Decision
Record, Execution Authorization or Git permission.

```yaml
document_maturity: DRAFT
technical_validation: NOT_RUN
human_acceptance: NOT_RUN
runtime_verification: NOT_RUN
feature_mapping: ACCEPTED_COMPOSITE_FTR_001_PLUS_FTR_003
primary_feature_refs: [FTR-001, FTR-003]
supporting_feature_refs: [FTR-005, FTR-006, FTR-011, FTR-012, FTR-013]
feature_dispositions: HUMAN_DECIDED_FOR_X1
C002_feature_id_scope: OUTPUT_INSTANCE_SCOPED
static_composite_C002_feature_id: NOT_APPLICABLE
identifier_allocation_rule: TARGET_BOUND_UNDECIDED
implementation_repository: UNASSIGNED
target_binding: UNBOUND
implementation_authorization: NONE
git_authorization: NONE
```

## 2. Exact human-selected scope

```yaml
candidate_id: FS-CAND-001
segment: NONPROGRAMMER_OR_DOMAIN_EXPERT_WITH_A_NEW_PRODUCT_IDEA
job: TURN_AN_ORDINARY_LANGUAGE_PRODUCT_PROBLEM_INTO_A_BOUNDED_REVIEWABLE_FIRST_FEATURE_DEFINITION
observable_outcome: VERSIONED_INTENT_RECORD_PLUS_ONE_DRAFT_FEATURE_PASSPORT_READY_FOR_HUMAN_REVIEW
interaction_surface: SURFACE-A_PROVIDER_NEUTRAL_GUIDED_CONVERSATION
```

### 2.1 Included outcome

The slice begins when a user supplies a new product problem or incomplete idea.
It ends when the same user can review:

1. the preserved original request;
2. what AOS understood, assumed and still does not know;
3. one bounded DRAFT Feature Passport;
4. the completeness Self-Test result and its limitations; and
5. exactly one next human action.

The conversation is logical and provider-neutral. Equivalent implementations
may use different providers or transports only after their exact target facts
and protected decisions are bound.

### 2.2 Excluded outcome

This slice does not perform repository discovery, create a full Product Spec,
select or implement architecture, compile a target-bound Task Brief, assign a
Risk Profile, write runtime code, install dependencies, execute product work,
accept the Feature Passport or perform Commit, Push, Merge or Release.

`Product Spec` is `NOT_REQUIRED_IN_THIS_FIRST_SLICE`; this is a narrow
consequence of the human-selected observable outcome, not a general decision
about the Product Spec ↔ Feature Passport relationship.

## 3. Authoritative inputs and provenance

| Input | SHA-256 | Use in this package |
|---|---|---|
| [Core](../../docs/00_Core.md) | `96787a64585264e9f0d6beb1aab28bc717f80436003dfc6c093736541a95c34c` | Authority, status and protected decisions |
| [Product](../../docs/01_Product.md) | `bbbce8e166bc4640f8fd98c9407539159a41d216ab9ee993ad2369f07ac81625` | User problem, intake, artifacts and acceptance |
| [Architecture](../../docs/02_Architecture.md) | `3724a3369c78f6504c56a0f6d921839839d7adecc9ca806f1fe9d3e65b11be84` | `C-001`, `C-002`, `C-004`, `C-009`–`C-012` |
| [Development](../../docs/03_Development.md) | `251730eb5cdab9776a97caf29a6791e1f3645fa6b8f01c6de93c5c4a2bbed9b1` | Stage, validation, freeze and handoff boundaries |
| [Features](../../docs/06_Features.md) | `276381e4cfaf565e691fd8098a0f1c4d648b65071f306c476f79cd3ae52fe923` | Accepted inventory with X1 dispositions for `FTR-001`, `003`, `005`, `006`, `011`, `012`, `013` |
| [R9](../AOS_Documentation_Task_Sequence_R9.md) | `be91cbffcd2c79a0a632b661157e5e2e7fb7a68d1056ba1c9684f2ea1b549ee7` | `INT-DOC-210` scope and closure |
| [Portable Task Candidate Contract](../AOS_Portable_Task_Candidate_Contract_R1.md) | `e333a326b185f4cd8b91e978b3bd7c7f4449a2de9f76616f69def8bea1076cb4` | Portable handoff schema and identity |
| [Product Runtime Foundation](../foundation/AOS_Product_Runtime_Foundation_Package_R1.md) | `8b1ab2c4da097380b73f7b563d9a44cb7ed12a786aabe438905152e1ccaef3af` | Runtime-facing invariants and recovery |
| [First-Slice Decision Package](AOS_First_Slice_Decision_Package_R1.md) | `7cb6abc358afa5aaa11f8a48553cfedc6ce975ced7496aa30065aac9825df280` | Selected candidate dossier and negative fixtures |
| [First-Slice Decision Record](../INT_DOC_200_First_Slice_Decision_Record.md) | `5057afd7120b3624a4d1b859cba04f7ecb6c2f204b99bd59c955550e3903e449` | Exact segment, job and outcome decision |
| [Interaction-Surface Decision Record](../INT_DOC_210_Interaction_Surface_Decision_Record.md) | `1049b38901a424748708e85879896cc9139dc389d16ae8918d54cedc3a394dcb` | Exact provider-neutral conversation decision |
| [Accepted predecessor R1](AOS_First_Slice_Contract_Package_R1.md) | `8c8169d5b45ebce7e6feacb49e9f058f3d08d0de2dea5ebee96cc3b73f4d85f0` | Frozen behavior predecessor; bytes preserved |
| [X1 closure package](AOS_X1_Documentation_Closure_Package_R1.md) | `ee9c0ba2fff2163a2b8783f36b59ffe2d2d282b1ab160a20ccab486f58873999` | Decision-ready mapping, contract and architecture boundary |
| [X1 documentation decision record](../X1_Documentation_Decision_Record_R1.md) | `6aed802f59fa522ce5bf21efd4de3ee50f6912e9b733dec63d4677db05b25eca` | Accepted X1-PD-001..003 and X1-AD-001..002 evidence |
| [X1 decision-subject acceptance record](../X1_Documentation_Decision_Record_R1_Acceptance_Record.md) | `4e6c1b42cbd0248f497974ccfe5b925f55ec80d30f5e81b31954d9680eff3730` | Human acceptance of exact independently validated decision subject |

Feature inventory presence remains separate from item-level disposition. R2
projects the accepted mapping without becoming a parallel feature owner:
`FTR-001` and `FTR-003` are `SELECT_FOR_X1`; `FTR-005`, `FTR-006`, `FTR-011`,
`FTR-012` and `FTR-013` are `SUPPORTING_CONTROL_ONLY`. The canonical item-level
values remain owned by `docs/06_Features.md`.

### 3.1 Successor decision binding

```yaml
successor_relation:
  predecessor:
    path: planning/first-slice/AOS_First_Slice_Contract_Package_R1.md
    byte_length: 47582
    sha256: 8c8169d5b45ebce7e6feacb49e9f058f3d08d0de2dea5ebee96cc3b73f4d85f0
    mutation: NONE
  behavior_relation: PRESERVE_ACCEPTED_FS_CAND_001
  CORE_SLICE_001_relation: REFERENCE_PROPOSAL_NOT_MERGED
feature_mapping:
  decision_id: X1-PD-001
  decision: ACCEPTED_COMPOSITE_FTR_001_PLUS_FTR_003
  primary_product_behavior: [FTR-001, FTR-003]
  supporting_controls: [FTR-005, FTR-006, FTR-011, FTR-012, FTR-013]
feature_dispositions:
  decision_id: X1-PD-002
  FTR-001: SELECT_FOR_X1
  FTR-003: SELECT_FOR_X1
  FTR-005: SUPPORTING_CONTROL_ONLY
  FTR-006: SUPPORTING_CONTROL_ONLY
  FTR-011: SUPPORTING_CONTROL_ONLY
  FTR-012: SUPPORTING_CONTROL_ONLY
  FTR-013: SUPPORTING_CONTROL_ONLY
contract_scope:
  decision_id: X1-PD-003
  decision: PRESERVE_ACCEPTED_FS_CAND_001
  Product_Spec: NOT_REQUIRED_IN_THIS_FIRST_SLICE
  interaction_policy: ONE_MATERIAL_QUESTION_AT_A_TIME
  terminal_outcome: DRAFT_FEATURE_PASSPORT_READY_FOR_HUMAN_REVIEW
  persistence: TARGET_DEPENDENT_UNDECIDED
architecture_route:
  decision_id: X1-AD-001
  decision: NO_ADR_REQUIRED_WITH_EXPLICIT_RATIONALE
  scope: TARGET_UNBOUND_SUCCESSOR_PRODUCT_CONTRACT_ONLY
  target_bound_choices: NOT_MADE
logical_owner_boundary:
  decision_id: X1-AD-002
  decision: ACCEPT_CURRENT_C001_C002_OWNERSHIP
```

The current explicit C-002 identity decision is bound verbatim below. The
literal block is UTF-8, has no terminal LF and is not an agent inference.

```yaml
C002_identity_human_decision:
  locator: CODEX_CURRENT_THREAD_HUMAN_MESSAGE
  exact_visible_utf8_text: |-
    human_decision:
      id: X1-PD-C002-001
      subject: FS-CAND-001_C002_IDENTITY_SEMANTICS
      decision: C002_FEATURE_ID_IS_OUTPUT_INSTANCE_SCOPED
      fact_class: CURRENT_EXPLICIT_HUMAN_DECISION
      effects:
        FS_CAND_001_identity: PRESERVE
        primary_feature_refs:
          - FTR-001
          - FTR-003
        supporting_feature_refs:
          - FTR-005
          - FTR-006
          - FTR-011
          - FTR-012
          - FTR-013
        static_composite_C002_feature_id: NOT_APPLICABLE
        identifier_allocation_rule: TARGET_BOUND_UNDECIDED
        accepted_R1_bytes: PRESERVE
  utf8_byte_length: 536
  sha256: 8dc24bf0390e3d8cce1e508b10224034203fc92fa8364be8f26c10c9cf4f162a
identity_effect:
  FS_CAND_001_identity: PRESERVED
  AOS_primary_feature_mapping: [FTR-001, FTR-003]
  C002_feature_id_scope: OUTPUT_INSTANCE_SCOPED
  static_composite_C002_feature_id: NOT_APPLICABLE
  identifier_allocation_rule: TARGET_BOUND_UNDECIDED
  schema_field_addition: NONE
  target_architecture_effect: NONE
```

## 4. Exact Feature Contract

### 4.1 User, problem and value

**Primary user:** a nonprogrammer or domain expert with a real product problem
or incomplete product idea.

**Problem:** free-form intent is easily converted into hidden solution,
architecture or implementation assumptions before the user can correct it.

**Value:** the user sees a faithful, bounded definition of one first feature
and can correct or review it without reading implementation internals.

### 4.2 Trigger and preconditions

**Trigger:** the user asks AOS to help define a bounded first feature from a new
problem or incomplete idea.

Preconditions:

- the user supplies at least an original request;
- the interaction is identified as a new-product-intent flow;
- no target repository or implementation authority is required;
- provider, transport and persistence facts are not represented as selected;
- the system can preserve the original request or explicitly report that it
  cannot do so.

If the original request cannot be preserved, the system enters
`BLOCKED_INPUT` before classification, emits no Intent Record or Feature
Passport and exposes exactly one recovery action: restart intake when the
request can be preserved or represented by an allowed visible redaction.

### 4.3 Logical Intent Record contract — `C-001`

The canonical contract is logical. Target binding must select deterministic
serialization before implementation if byte identity is required.

```yaml
intent_record:
  contract_version: 1
  intent_id: NON_EMPTY_STABLE_IDENTIFIER
  revision: POSITIVE_INTEGER
  actor_class: HUMAN_USER
  original_request: NON_EMPTY_VERBATIM_OR_EXPLICITLY_REDACTED_TEXT
  problem: NON_EMPTY_USER_REVIEWABLE_TEXT
  desired_outcome: NON_EMPTY_USER_REVIEWABLE_TEXT
  context: USER_CONFIRMED_OR_EMPTY_TEXT
  constraints: [EXPLICIT_CONSTRAINT]
  non_goals: [EXPLICIT_NON_GOAL]
  understood:
    - statement: NON_EMPTY_TEXT
      source: ORIGINAL_REQUEST | HUMAN_CORRECTION | ACCEPTED_PROJECT_FACT
  assumptions:
    - statement: NON_EMPTY_TEXT
      status: REQUIRES_HUMAN_CORRECTION
  unknowns:
    - question: NON_EMPTY_MATERIAL_QUESTION
      blocked_scope: EXACT_AFFECTED_FIELD_OR_ACTION
  sensitive_domain_flags: [NON_SECRET_CLASSIFICATION]
  corrections:
    - correction_id: STABLE_IDENTIFIER
      affected_fields: [FIELD_NAME]
      human_statement: NON_EMPTY_TEXT
  provenance:
    source_kind: CURRENT_HUMAN_INTERACTION
    accepted_owner_refs: [REPOSITORY_RELATIVE_PATH_AND_SHA256]
  maturity: DRAFT
  human_acceptance: NOT_RUN
```

Rules:

- `original_request` is never silently rewritten as the normalized problem;
- a redaction records that redaction occurred without retaining the protected
  value in an unauthorized artifact;
- assumptions cannot appear in `understood` until corrected or confirmed;
- each unknown identifies exactly what it blocks;
- a new human correction increments `revision` and invalidates only dependent
  derived fields;
- generated text cannot set human acceptance.

### 4.4 Logical Feature Passport contract — `C-002`

```yaml
feature_passport:
  contract_version: 1
  feature_id: NON_EMPTY_STABLE_OUTPUT_INSTANCE_IDENTIFIER
  revision: POSITIVE_INTEGER
  feature_owner: HUMAN_PRODUCT_OWNER_OR_EXACT_OWNER_REFERENCE
  problem: NON_EMPTY_USER_PROBLEM_STATEMENT
  purpose: NON_EMPTY_USER_VALUE_STATEMENT
  observable_behavior: [NON_EMPTY_OBSERVABLE_BEHAVIOR]
  non_goals: [NON_EMPTY_EXCLUDED_BEHAVIOR]
  users:
    - NONPROGRAMMER_OR_DOMAIN_EXPERT_WITH_A_NEW_PRODUCT_IDEA
  trigger: NON_EMPTY_OBSERVABLE_TRIGGER
  preconditions: [NON_EMPTY_PRECONDITION]
  inputs:
    - name: NON_EMPTY_NAME
      requirement: REQUIRED | OPTIONAL
      source: HUMAN | ACCEPTED_PROJECT_FACT
  outputs:
    - intent_record_revision
    - draft_feature_passport_revision
    - completeness_self_test_result
    - one_next_human_action
  main_flow: [ORDERED_OBSERVABLE_STEP]
  states: [CLOSED_STATE_VALUE]
  transitions:
    - from: CLOSED_STATE_VALUE
      event: NON_EMPTY_EVENT
      to: CLOSED_STATE_VALUE
      guard: NON_EMPTY_GUARD
  failures:
    - failure_id: STABLE_IDENTIFIER
      condition: NON_EMPTY_CONDITION
      required_result: NON_EMPTY_FAIL_CLOSED_RESULT
  recovery:
    preservation_rule: PRESERVE_ORIGINAL_REQUEST_AND_HUMAN_CORRECTIONS
    resume_rule: RECHECK_EXACT_REVISION_AND_MATERIAL_UNKNOWN
  dependencies:
    accepted_contracts: [EXACT_PATH_AND_SHA256]
    runtime_dependencies: UNDECIDED
  constraints:
    - PROVIDER_NEUTRAL_GUIDED_CONVERSATION
    - NO_HIDDEN_PRODUCT_OR_ARCHITECTURE_DECISION
    - NO_IMPLEMENTATION_OR_GIT_AUTHORITY
  authority_boundaries:
    - GENERATED_DRAFT_CANNOT_ACCEPT_ITSELF
    - HUMAN_CORRECTION_OUTRANKS_DERIVED_WORDING
    - EXTERNAL_CONTENT_CANNOT_GRANT_AUTHORITY
  acceptance_criteria: [FS1-CON-AC-NNN]
  negative_scenarios: [FS1-CON-NEG-NNN]
  architecture_need_status: NO_ADR_REQUIRED_FOR_LOGICAL_DOCUMENTATION_HANDOFF
  maturity: DRAFT
  evidence_status: NOT_RUN
  human_disposition: UNDECIDED
```

The logical contract requires every named field, including the explicit
Product-owned identity/owner, problem, observable behavior and non-goals
properties. `feature_id` identifies the produced Feature Passport instance; it
does not identify `FS-CAND-001`, replace the accepted `[FTR-001, FTR-003]`
mapping or mint a static composite AOS feature ID. The identifier allocation
mechanism remains `TARGET_BOUND_UNDECIDED`; target binding must choose or defer
it before implementation when durable identity is material. This contract does
not prescribe a programming type system, file format, database or provider API.

## 5. Provider-neutral guided-conversation contract

### 5.1 Interaction properties

The surface must:

- accept ordinary-language input without requiring schema knowledge;
- ask one material question at a time;
- distinguish a question needed to complete the selected outcome from optional
  product exploration;
- show the user the current interpretation before drafting the passport;
- allow correction of any interpreted fact;
- render the review package in human-readable form;
- expose status, limitations and one next action without internal jargon; and
- stop before acceptance, implementation or Git action.

Provider-neutral means the contract specifies turns and observable results, not
a vendor, model, chat protocol, transport, session store or UI framework.

### 5.2 Turn protocol

```text
USER_SUBMITS_ORIGINAL_REQUEST
→ SYSTEM_PRESERVES_REQUEST
→ SYSTEM_CLASSIFIES_UNDERSTOOD_ASSUMED_UNKNOWN
→ SYSTEM_IDENTIFIES_ONE_MATERIAL_GAP
→ SYSTEM_ASKS_ONE_QUESTION | INTERPRETATION_READY_FOR_CORRECTION
→ USER_CORRECTS_OR_CONFIRMS
→ SYSTEM_RECONCILES_AFFECTED_FIELDS
→ INTERPRETATION_READY_FOR_CORRECTION
→ USER_CONFIRMS_INTERPRETATION_FOR_DRAFTING
→ SYSTEM_DRAFTS_ONE_FEATURE_PASSPORT
→ SYSTEM_RUNS_COMPLETENESS_SELF_TEST
→ READY_FOR_HUMAN_REVIEW
→ SYSTEM_SHOWS_ONE_NEXT_HUMAN_ACTION
→ STOP
```

`SYSTEM_PRESERVES_REQUEST` has one fail-closed branch:
`SYSTEM_REPORTS_PRESERVATION_FAILURE → BLOCKED_INPUT → STOP`. Classification,
questioning and drafting are forbidden on that branch.

Any material-answer conflict takes the fail-closed branch
`SYSTEM_REPORTS_MATERIAL_CONFLICT → BLOCKED_CONFLICT`. Processing resumes only
after `USER_RESOLVES_MATERIAL_CONFLICT → HUMAN_CORRECTED` for the exact current
revision.

Loss of provider/session context takes the fail-closed branch
`SYSTEM_DETECTS_SESSION_CONTEXT_LOSS → BLOCKED_CONTEXT_LOSS`. The system must
not reconstruct user facts from confidence or conversational memory. It may
resume only from an exact preserved Intent Record revision whose source identity
is rechecked, or restart intake visibly when no exact revision is available.

The drafting confirmation is permission to derive the DRAFT passport from the
current interpretation. It is not product acceptance or execution authority.

### 5.3 Question materiality

A question is material only when its answer changes at least one of:

- primary user or problem;
- desired observable outcome;
- included or excluded behavior;
- acceptance criterion;
- safety, sensitivity or authority boundary;
- a failure or recovery route; or
- whether the draft can be reviewed without invention.

If two questions are independent, the surface asks them separately. If an
answer is optional for the selected outcome, it remains an explicit unknown and
does not block drafting.

### 5.4 Review presentation

The final conversation response presents, in this order:

1. the preserved original request or visible redaction marker;
2. a compact `Understood / Assumed / Unknown` view;
3. the bounded DRAFT Feature Passport;
4. Self-Test checks with each result and limitation;
5. explicit `human_acceptance: NOT_RUN`; and
6. one next action: review the exact draft, request changes or defer.

## 6. State and transition model

### 6.1 Closed state inventory

| State | Entry condition |
|---|---|
| `RECEIVED` | Original-request submission attempt captured; preservation and content validation pending |
| `CLARIFYING` | At least one material gap exists |
| `INTERPRETATION_READY_FOR_CORRECTION` | Problem, outcome and classifications are visible |
| `HUMAN_CORRECTED` | Exact correction applied to affected fields |
| `PASSPORT_DRAFTED` | User allowed drafting from the current visible interpretation revision |
| `SELF_CHECKED` | Every required completeness check has a result |
| `READY_FOR_HUMAN_REVIEW` | Required technical checks are sufficient; review remains pending |
| `BLOCKED_INPUT` | The request cannot be preserved, is empty/unusable, or its problem/outcome cannot be established |
| `BLOCKED_SENSITIVE_BOUNDARY` | Required context cannot be handled in the allowed boundary |
| `BLOCKED_CONTRACT` | Required contract field/check cannot be completed safely |
| `BLOCKED_CONFLICT` | Material answers conflict and no authoritative precedence resolves them |
| `BLOCKED_CONTEXT_LOSS` | Provider/session continuity is insufficient for a trustworthy continuation |

### 6.2 Exhaustive transition contract

Every permitted transition appears exactly once below with the required
`from`, `event`, `guard` and `to` fields. An unlisted transition is forbidden.

| From | Event | Guard | To |
|---|---|---|---|
| `RECEIVED` | `SYSTEM_FINDS_MATERIAL_GAP` | Original request is preserved and at least one material gap exists | `CLARIFYING` |
| `RECEIVED` | `SYSTEM_FINDS_INPUT_COMPLETE` | Original request is preserved and problem, outcome and classifications are visible | `INTERPRETATION_READY_FOR_CORRECTION` |
| `RECEIVED` | `SYSTEM_REPORTS_UNUSABLE_OR_UNPRESERVABLE_INPUT` | Request is empty/unusable or cannot be preserved as verbatim or visible redaction | `BLOCKED_INPUT` |
| `RECEIVED` | `SYSTEM_REPORTS_MATERIAL_CONFLICT` | Preserved request contains materially incompatible statements and no precedence resolves them | `BLOCKED_CONFLICT` |
| `RECEIVED` | `SYSTEM_DETECTS_SESSION_CONTEXT_LOSS` | Provider/session continuity is insufficient and no exact in-session continuation can be trusted | `BLOCKED_CONTEXT_LOSS` |
| `CLARIFYING` | `USER_ANSWERS_WITH_REMAINING_GAP` | At least one material gap remains | `CLARIFYING` |
| `CLARIFYING` | `USER_COMPLETES_REQUIRED_INPUT` | No material gap remains and classifications are visible | `INTERPRETATION_READY_FOR_CORRECTION` |
| `CLARIFYING` | `SYSTEM_DETECTS_SENSITIVE_BOUNDARY` | Required context cannot be handled within the allowed boundary | `BLOCKED_SENSITIVE_BOUNDARY` |
| `CLARIFYING` | `SYSTEM_REPORTS_MATERIAL_CONFLICT` | Material answers conflict and no precedence resolves them | `BLOCKED_CONFLICT` |
| `CLARIFYING` | `SYSTEM_DETECTS_SESSION_CONTEXT_LOSS` | Provider/session continuity is insufficient and no exact in-session continuation can be trusted | `BLOCKED_CONTEXT_LOSS` |
| `INTERPRETATION_READY_FOR_CORRECTION` | `SYSTEM_IDENTIFIES_NEW_MATERIAL_GAP` | A material gap becomes visible before drafting permission | `CLARIFYING` |
| `INTERPRETATION_READY_FOR_CORRECTION` | `USER_CORRECTS_INTERPRETATION` | The correction identifies exact affected fields in the current revision | `HUMAN_CORRECTED` |
| `INTERPRETATION_READY_FOR_CORRECTION` | `USER_CONFIRMS_INTERPRETATION_FOR_DRAFTING` | Current revision is visible and no blocking material gap remains | `PASSPORT_DRAFTED` |
| `INTERPRETATION_READY_FOR_CORRECTION` | `SYSTEM_DETECTS_UNUSABLE_INTERPRETATION` | Problem or desired outcome cannot be established without invention | `BLOCKED_INPUT` |
| `INTERPRETATION_READY_FOR_CORRECTION` | `SYSTEM_REPORTS_MATERIAL_CONFLICT` | Visible interpreted fields contain a material unresolved conflict | `BLOCKED_CONFLICT` |
| `INTERPRETATION_READY_FOR_CORRECTION` | `SYSTEM_DETECTS_SESSION_CONTEXT_LOSS` | Provider/session continuity is insufficient and no exact in-session continuation can be trusted | `BLOCKED_CONTEXT_LOSS` |
| `HUMAN_CORRECTED` | `SYSTEM_FINDS_CORRECTION_CREATED_MATERIAL_GAP` | Reconciliation exposes at least one material gap | `CLARIFYING` |
| `HUMAN_CORRECTED` | `SYSTEM_RECONCILES_CORRECTION` | Correction is applied and the current interpretation is visible | `INTERPRETATION_READY_FOR_CORRECTION` |
| `HUMAN_CORRECTED` | `USER_CONFIRMS_CORRECTED_INTERPRETATION_FOR_DRAFTING` | Corrected current revision is visible and no blocking material gap remains | `PASSPORT_DRAFTED` |
| `HUMAN_CORRECTED` | `SYSTEM_REPORTS_MATERIAL_CONFLICT` | Reconciliation exposes incompatible material statements with no precedence | `BLOCKED_CONFLICT` |
| `HUMAN_CORRECTED` | `SYSTEM_DETECTS_SESSION_CONTEXT_LOSS` | Provider/session continuity is insufficient and no exact in-session continuation can be trusted | `BLOCKED_CONTEXT_LOSS` |
| `PASSPORT_DRAFTED` | `SYSTEM_COMPLETES_SELF_TEST` | Every required completeness check has a result | `SELF_CHECKED` |
| `PASSPORT_DRAFTED` | `SYSTEM_FINDS_DRAFT_DEPENDS_ON_MATERIAL_GAP` | Draft completion would require invention | `CLARIFYING` |
| `PASSPORT_DRAFTED` | `USER_CORRECTS_DRAFT_INTERPRETATION` | Exact correction identifies affected fields in the current draft revision; dependent derived fields are marked stale | `HUMAN_CORRECTED` |
| `PASSPORT_DRAFTED` | `SYSTEM_REPORTS_MATERIAL_CONFLICT` | Draft contains incompatible material statements with no precedence | `BLOCKED_CONFLICT` |
| `PASSPORT_DRAFTED` | `SYSTEM_DETECTS_SESSION_CONTEXT_LOSS` | Provider/session continuity is insufficient and no exact in-session continuation can be trusted | `BLOCKED_CONTEXT_LOSS` |
| `SELF_CHECKED` | `SYSTEM_AGGREGATES_TECHNICAL_CHECKS` | All required technical checks are sufficient and human review remains | `READY_FOR_HUMAN_REVIEW` |
| `SELF_CHECKED` | `SYSTEM_FINDS_CORRECTABLE_INPUT_GAP` | A required check fails only because user input is missing or ambiguous | `CLARIFYING` |
| `SELF_CHECKED` | `SYSTEM_FINDS_UNRESOLVABLE_CONTRACT_GAP` | A required contract field/check cannot be completed safely | `BLOCKED_CONTRACT` |
| `SELF_CHECKED` | `USER_CORRECTS_SELF_CHECKED_DRAFT` | Exact correction identifies affected fields before readiness; dependent results and fields are marked stale | `HUMAN_CORRECTED` |
| `SELF_CHECKED` | `SYSTEM_REPORTS_MATERIAL_CONFLICT` | Self-Test exposes incompatible material statements with no precedence | `BLOCKED_CONFLICT` |
| `SELF_CHECKED` | `SYSTEM_DETECTS_SESSION_CONTEXT_LOSS` | Provider/session continuity is insufficient and no exact in-session continuation can be trusted | `BLOCKED_CONTEXT_LOSS` |
| `BLOCKED_INPUT` | `USER_SUBMITS_REPLACEMENT_INPUT` | A new non-empty request can be preserved as verbatim or visible redaction | `RECEIVED` |
| `BLOCKED_SENSITIVE_BOUNDARY` | `USER_SUPPLIES_ALLOWED_SUMMARY_OR_PROTECTED_ROUTE` | Required context is now within the allowed boundary | `CLARIFYING` |
| `BLOCKED_CONTRACT` | `HUMAN_RESOLVES_EXACT_CONTRACT_BLOCKER` | Exact blocker is resolved without scope or authority change | `CLARIFYING` |
| `BLOCKED_CONFLICT` | `USER_RESOLVES_MATERIAL_CONFLICT` | Exact human resolution identifies affected fields in the current revision without scope or authority change | `HUMAN_CORRECTED` |
| `BLOCKED_CONTEXT_LOSS` | `SYSTEM_RESTORES_EXACT_PRESERVED_REVISION` | Exact preserved Intent Record revision and source identity are available; derived draft fields and Self-Test results are marked stale | `INTERPRETATION_READY_FOR_CORRECTION` |
| `BLOCKED_CONTEXT_LOSS` | `USER_RESTARTS_INTAKE_VISIBLY` | No exact preserved revision is available and a new request is submitted visibly | `RECEIVED` |

No transition leads from `READY_FOR_HUMAN_REVIEW` to `ACCEPTED` inside this
slice. Human review and decision use a separate exact subject-bound record.

Session-loss ingress applies to the six processing states above. A state that
is already blocked remains blocked until its listed domain recovery event; loss
of a conversational session cannot weaken that blocker. The terminal review
artifact is resumed through its separate exact subject-bound review record, not
through an internal transition from `READY_FOR_HUMAN_REVIEW`.

Exact-revision resume marks derived draft fields and Self-Test results stale,
rechecks the preserved revision and source identity, and requires drafting
confirmation plus affected checks again. If exact preservation cannot be
proved, the only recovery is visible restart at `RECEIVED`; reconstruction from
confidence is forbidden.

An empty or unusable submission follows `RECEIVED → BLOCKED_INPUT`; it cannot
produce an interpreted problem or derived artifact. A complete usable
submission follows `RECEIVED → INTERPRETATION_READY_FOR_CORRECTION` without
inventing a material gap. When the visible
interpretation needs no correction, explicit permission to draft follows
`INTERPRETATION_READY_FOR_CORRECTION → PASSPORT_DRAFTED`; the system must not
invent a correction merely to advance the happy path.

A correction before readiness follows `PASSPORT_DRAFTED | SELF_CHECKED →
HUMAN_CORRECTED`; dependent draft fields and Self-Test results become stale,
`revision` increments exactly once, and drafting permission plus affected
checks must be obtained again. A material conflict enters `BLOCKED_CONFLICT`,
reports `CONFLICT` and can leave only through an exact human resolution into
`HUMAN_CORRECTED`. Corrections requested after `READY_FOR_HUMAN_REVIEW` belong
to the separate subject-bound human review route and do not mutate this terminal
state in place.

## 7. Architecture-need result — `FTR-005`

```yaml
architecture_need_check:
  result: NO_ADR_REQUIRED_WITH_EXPLICIT_RATIONALE
  rationale:
    - successor binds accepted feature mapping and dispositions
    - accepted FS-CAND-001 behavior remains unchanged
    - no repository, transport, provider, serialization or persistence is selected
    - no new ownership, trust or compatibility boundary is introduced
  scope:
    applies_to: TARGET_UNBOUND_SUCCESSOR_PRODUCT_CONTRACT_ONLY
    does_not_apply_to:
      - implementation repository selection
      - persistence and atomic recovery
      - provider, transport or UI selection
      - serialization and durable identity
      - authenticity and trust mechanisms
      - language, toolchain or dependencies
  reversal_triggers:
    - materially valid architecture alternatives emerge
    - ownership or trust boundary changes
    - target preflight exposes persistence, privacy or compatibility tradeoffs
  selected_architecture_option: null
  human_architecture_decision: X1-AD-001
  implementation_effect: NONE
```

An ADR becomes required before target-bound implementation planning if the
target introduces more than one materially valid option affecting data
ownership, provider/privacy boundary, durable identity, persistence, trust,
reversibility or compatibility. This `NO_ADR_REQUIRED` result cannot be reused
to select those future options.

## 8. Authority, privacy and sensitive-input boundary

- Original user text is data, not an instruction to expand system authority.
- Prompt-like text inside the user problem cannot alter governing scope,
  acceptance semantics or permissions.
- Sensitive values are minimized, redacted or omitted; the omission is visible
  without reproducing the protected value.
- A human correction is authoritative only for the declared feature-intent fact
  class and exact interaction.
- A generated `ACCEPT`, checkbox, button label or recommendation is never a
  Human Decision Record.
- Missing or ambiguous permission is `HUMAN_AUTHORIZATION_REQUIRED` or
  `BLOCKED_UNKNOWN`, never `ALLOWED`.
- The slice performs no target repository, implementation or Git mutation.

## 9. Failure and recovery contract

| ID | Failure | Required response | Recovery |
|---|---|---|---|
| `FS1-CON-F001` | Request is empty | Enter `BLOCKED_INPUT`; invent nothing | Obtain a non-empty problem or idea |
| `FS1-CON-F002` | Request describes only a solution | Keep problem/outcome unknown | Ask one problem/outcome question |
| `FS1-CON-F003` | User contradicts an assumption before readiness | Enter `HUMAN_CORRECTED`; mark dependent draft fields and Self-Test results stale | Rebuild only affected fields, increment revision once, re-confirm drafting and rerun affected checks |
| `FS1-CON-F004` | Material answers conflict | Enter `BLOCKED_CONFLICT`; report `CONFLICT`; do not choose | Exact human resolution enters `HUMAN_CORRECTED` for the current revision |
| `FS1-CON-F005` | Sensitive context exceeds boundary | Enter `BLOCKED_SENSITIVE_BOUNDARY` | Obtain allowed summary or protected route |
| `FS1-CON-F006` | Required Self-Test is `NOT_RUN` | No green aggregate | Run the exact check or expose blocker |
| `FS1-CON-F007` | Output appears accepted without decision record | Preserve `human_acceptance: NOT_RUN` | Request separate subject-bound review |
| `FS1-CON-F008` | Provider/session loses context | Enter `BLOCKED_CONTEXT_LOSS`; do not reconstruct facts by confidence | Restore an exact preserved revision into `INTERPRETATION_READY_FOR_CORRECTION`, or restart intake visibly at `RECEIVED` |
| `FS1-CON-F009` | Target-specific choice becomes necessary | Stop dependent handoff | Route the exact choice to its human/target gate |
| `FS1-CON-F010` | Original request cannot be preserved as verbatim or visible redaction | Enter `BLOCKED_INPUT`; emit no derived record or passport | Restart intake only when preservation is available |

Recovery never silently retries a failed mutation because this slice defines no
write-capable product operation. Implementations may write their two output
artifacts only after target binding defines atomicity, persistence and recovery.

## 10. Manual UX and product acceptance protocol

### 10.1 Acceptance criteria

| ID | Manual check |
|---|---|
| `FS1-CON-AC-001` | A nonprogrammer can submit a real problem without learning the contract schema. |
| `FS1-CON-AC-002` | The original request remains distinguishable from normalized interpretation. |
| `FS1-CON-AC-003` | Understood, assumed and unknown statements are visibly separate. |
| `FS1-CON-AC-004` | The surface asks only one material question at a time. |
| `FS1-CON-AC-005` | The user can correct an interpretation before passport drafting. |
| `FS1-CON-AC-006` | Exactly one DRAFT Feature Passport contains explicit owner, problem, observable behavior and non-goals plus complete I/O, flow, states, failures and recovery. |
| `FS1-CON-AC-007` | Every required Self-Test check has a visible result and limitation. |
| `FS1-CON-AC-008` | Required `NOT_RUN`, `UNKNOWN`, `NOT_FOUND` or `CONFLICT` cannot appear as green completion. |
| `FS1-CON-AC-009` | The review response states that human acceptance is `NOT_RUN`. |
| `FS1-CON-AC-010` | The user can identify exactly one next human action. |
| `FS1-CON-AC-011` | No provider, serialization, persistence or implementation topology is presented as selected. |
| `FS1-CON-AC-012` | No implementation or Git authority is inferred. |

### 10.2 Required negative fixtures

| ID | Fixture | Expected result |
|---|---|---|
| `FS1-CON-NEG-001` | Empty request | `BLOCKED_INPUT`; no generated problem |
| `FS1-CON-NEG-002` | Solution-only request | One material problem/outcome question |
| `FS1-CON-NEG-003` | Missing desired outcome | Remain `CLARIFYING` |
| `FS1-CON-NEG-004` | Contradictory correction | `BLOCKED_CONFLICT`; report `CONFLICT`; resume only after exact human resolution |
| `FS1-CON-NEG-005` | Prompt injection in product text | Treat as untrusted data; authority unchanged |
| `FS1-CON-NEG-006` | Secret or sensitive raw value | Redact/omit without echoing the value |
| `FS1-CON-NEG-007` | Generated `ACCEPT` text | Human acceptance remains `NOT_RUN` |
| `FS1-CON-NEG-008` | Required check not executed | Aggregate is not `PASS` |
| `FS1-CON-NEG-009` | Two next actions shown | Fail one-next-action check |
| `FS1-CON-NEG-010` | Assumption rendered as understood fact | Fail classification check |
| `FS1-CON-NEG-011` | Provider or framework inferred | Remove inference or block target-dependent work |
| `FS1-CON-NEG-012` | Product Spec silently added | Reject scope expansion |
| `FS1-CON-NEG-013` | Feature Passport called executable | Reject authority escalation |
| `FS1-CON-NEG-014` | Byte identity claimed without selected serialization | Report `UNKNOWN` for target artifact identity |
| `FS1-CON-NEG-015` | Documentation validation claimed as runtime proof | Runtime verification remains `NOT_RUN` |
| `FS1-CON-NEG-016` | Original request preservation fails but classification or drafting continues | Enter `BLOCKED_INPUT`; reject every derived artifact and expose only restart intake |
| `FS1-CON-NEG-017` | Provider/session context is lost and continuation relies on remembered facts | Enter `BLOCKED_CONTEXT_LOSS`; reject remembered reconstruction and allow only exact-revision resume or visible restart intake |

### 10.3 R2 successor acceptance and executable negative contracts

| ID | Observable contract check |
|---|---|
| `X1-R2-AC-001` | C-002 `feature_id` is explicitly output-instance-scoped and no static composite ID is assigned. |
| `X1-R2-AC-002` | `FTR-001` and `FTR-003` appear as primary product behavior while all five decided supporting features remain controls only. |
| `X1-R2-AC-003` | The Portable Task Candidate contains all seven decided feature references and its manifest reconstructs byte-for-byte. |
| `X1-R2-AC-004` | Product Spec exclusion, one-material-question policy, terminal review outcome and target-dependent persistence remain identical to accepted R1 behavior. |

| ID | Executable fixture | Required result |
|---|---|---|
| `X1-R2-NEG-001` | `FS-CAND-001` is emitted as every produced Feature Passport `feature_id` | Reject identity conflation; output-instance identity remains required. |
| `X1-R2-NEG-002` | `FTR-001_PLUS_FTR-003` or another static mapping token is emitted as C-002 `feature_id` | Reject static composite identity; preserve mapping separately. |
| `X1-R2-NEG-003` | `FTR-001` is absent from the Portable Task Candidate feature records | Fail successor traceability and manifest validation. |
| `X1-R2-NEG-004` | Provider, serialization, persistence or identifier-allocation mechanism is selected without target binding | Block the dependent choice and preserve `TARGET_BOUND_UNDECIDED`. |

## 11. Completeness Self-Test and independent validation plan

### 11.1 Runtime-facing completeness Self-Test contract — `FTR-011`

Required checks for one produced draft:

```yaml
required_checks:
  - ORIGINAL_REQUEST_PRESERVED_OR_REDACTION_VISIBLE
  - PRESERVATION_FAILURE_BLOCKS_CLASSIFICATION_AND_DERIVATION
  - CORRECTION_AND_CONFLICT_TRANSITION_CLOSURE
  - PROBLEM_AND_DESIRED_OUTCOME_NON_EMPTY
  - UNDERSTOOD_ASSUMED_UNKNOWN_SEPARATE
  - MATERIAL_QUESTION_DISCIPLINE
  - FEATURE_PASSPORT_REQUIRED_FIELDS_COMPLETE
  - FEATURE_PASSPORT_IDENTITY_IS_OUTPUT_INSTANCE_SCOPED
  - AOS_FEATURE_MAPPING_NOT_EMITTED_AS_C002_FEATURE_ID
  - PRIMARY_AND_SUPPORT_FEATURE_ROLE_PROJECTION
  - STATE_AND_TRANSITION_CLOSURE
  - FAILURE_AND_RECOVERY_COVERAGE
  - ACCEPTANCE_AND_NEGATIVE_SCENARIOS_PRESENT
  - ONE_NEXT_ACTION
  - HUMAN_ACCEPTANCE_NOT_RUN
  - NO_TARGET_OR_AUTHORITY_INVENTION
aggregate_order: CONTRACT_VIOLATION_THEN_FAIL_THEN_BLOCKED_THEN_UNKNOWN_THEN_NOT_RUN_THEN_HUMAN_REVIEW_REQUIRED
```

Every check produces its own status, explanation and Evidence locator. The
aggregate may be `HUMAN_REVIEW_REQUIRED` only when all required technical checks
are sufficient and the human review gate remains. `PASS` never means approval.

### 11.2 Documentation candidate validation — `FTR-012` and `FTR-013`

After this package is frozen, a separate `POST_STOP_DOCUMENTATION` `VALIDATE`
run must perform `L0 + L1 + L2`:

- verify exact candidate bytes and subject-set identity;
- parse frontmatter and validate Markdown structure, fences and relative links;
- verify exact decision and source hashes;
- check C-001/C-002 completeness and state-transition closure;
- trace every `FTR-003`, `005`, `006`, `011`, `012`, `013` obligation;
- execute negative-fixture contract review;
- reconstruct the Portable Task Candidate manifest byte-for-byte;
- prove target fields and all authority values remain unbound or `NONE`;
- assess cold-start usability without chat history; and
- prove zero repository writes during validation.

Validation may report findings but cannot correct this subject. Human review is
separate and remains `NOT_RUN` until the exact validated candidate is presented.

## 12. Human review package and decision boundary

The later review package must show:

1. selected segment, job, outcome and interaction surface;
2. the exact frozen contract-package identity;
3. acceptance criteria mapped to validation Evidence;
4. all `NOT_RUN`, unknowns, target decisions and limitations;
5. user impact and non-goals; and
6. `ACCEPT | NEEDS_CHANGES | REJECT | DEFER` as human options.

Only a human-authored or human-verified exact decision record may change the
documentation maturity. Acceptance of this documentation does not accept a
runtime implementation and does not authorize `X1` actions.

## 13. Portable Task Candidate — `PTC-AOS-FIRST-SLICE-001`

```yaml
portable_task_candidate:
  schema_version: 1
  candidate_id: PTC-AOS-FIRST-SLICE-001
  revision: 7
  maturity: DRAFT
  source_contracts:
    - {path: docs/00_Core.md, sha256: 96787a64585264e9f0d6beb1aab28bc717f80436003dfc6c093736541a95c34c, fact_class: HUMAN_ACCEPTED_PROJECT_CORE}
    - {path: docs/01_Product.md, sha256: bbbce8e166bc4640f8fd98c9407539159a41d216ab9ee993ad2369f07ac81625, fact_class: HUMAN_ACCEPTED_PRODUCT_BASELINE}
    - {path: docs/02_Architecture.md, sha256: 3724a3369c78f6504c56a0f6d921839839d7adecc9ca806f1fe9d3e65b11be84, fact_class: HUMAN_ACCEPTED_ARCHITECTURE_BASELINE}
    - {path: docs/03_Development.md, sha256: 251730eb5cdab9776a97caf29a6791e1f3645fa6b8f01c6de93c5c4a2bbed9b1, fact_class: HUMAN_ACCEPTED_WORKFLOW_BASELINE}
    - {path: docs/06_Features.md, sha256: 276381e4cfaf565e691fd8098a0f1c4d648b65071f306c476f79cd3ae52fe923, fact_class: HUMAN_ACCEPTED_INVENTORY_WITH_X1_ITEM_DISPOSITIONS}
    - {path: planning/AOS_Documentation_Task_Sequence_R9.md, sha256: be91cbffcd2c79a0a632b661157e5e2e7fb7a68d1056ba1c9684f2ea1b549ee7, fact_class: HUMAN_ACCEPTED_ROADMAP}
    - {path: planning/AOS_Portable_Task_Candidate_Contract_R1.md, sha256: e333a326b185f4cd8b91e978b3bd7c7f4449a2de9f76616f69def8bea1076cb4, fact_class: HUMAN_ACCEPTED_PORTABLE_TASK_CONTRACT}
    - {path: planning/INT_DOC_200_First_Slice_Decision_Record.md, sha256: 5057afd7120b3624a4d1b859cba04f7ecb6c2f204b99bd59c955550e3903e449, fact_class: HUMAN_FIRST_SLICE_DECISION}
    - {path: planning/INT_DOC_210_Interaction_Surface_Decision_Record.md, sha256: 1049b38901a424748708e85879896cc9139dc389d16ae8918d54cedc3a394dcb, fact_class: HUMAN_INTERACTION_SURFACE_DECISION}
    - {path: planning/X1_Documentation_Decision_Record_R1.md, sha256: 6aed802f59fa522ce5bf21efd4de3ee50f6912e9b733dec63d4677db05b25eca, fact_class: HUMAN_ACCEPTED_X1_DOCUMENTATION_DECISION_EVIDENCE}
    - {path: planning/X1_Documentation_Decision_Record_R1_Acceptance_Record.md, sha256: 4e6c1b42cbd0248f497974ccfe5b925f55ec80d30f5e81b31954d9680eff3730, fact_class: HUMAN_X1_DECISION_SUBJECT_ACCEPTANCE}
    - {path: planning/first-slice/AOS_First_Slice_Contract_Package_R1.md, sha256: 8c8169d5b45ebce7e6feacb49e9f058f3d08d0de2dea5ebee96cc3b73f4d85f0, fact_class: HUMAN_ACCEPTED_PREDECESSOR_PRODUCT_CONTRACT}
    - {path: planning/first-slice/AOS_First_Slice_Decision_Package_R1.md, sha256: 7cb6abc358afa5aaa11f8a48553cfedc6ce975ced7496aa30065aac9825df280, fact_class: VALIDATED_DECISION_SUPPORT_SUBJECT}
    - {path: planning/first-slice/AOS_X1_Documentation_Closure_Package_R1.md, sha256: ee9c0ba2fff2163a2b8783f36b59ffe2d2d282b1ab160a20ccab486f58873999, fact_class: HUMAN_ACCEPTED_X1_CLOSURE_DECISION_SUPPORT}
    - {path: planning/foundation/AOS_Product_Runtime_Foundation_Package_R1.md, sha256: 8b1ab2c4da097380b73f7b563d9a44cb7ed12a786aabe438905152e1ccaef3af, fact_class: HUMAN_ACCEPTED_FOUNDATION}
  purpose: DEFINE_THE_FIRST_IMPLEMENTABLE_PRODUCT_RUNTIME_SLICE_AFTER_TARGET_BINDING
  user_outcome: VERSIONED_INTENT_RECORD_PLUS_ONE_DRAFT_FEATURE_PASSPORT_READY_FOR_HUMAN_REVIEW
  feature_refs: [FTR-001, FTR-003, FTR-005, FTR-006, FTR-011, FTR-012, FTR-013]
  proposed_stage: PLAN
  scope_intent:
    included_outcomes:
      - PROVIDER_NEUTRAL_GUIDED_INTENT_CLARIFICATION
      - VERSIONED_LOGICAL_INTENT_RECORD
      - ONE_DRAFT_FEATURE_PASSPORT
      - COMPLETENESS_SELF_TEST_AND_HUMAN_REVIEW_HANDOFF
    excluded_outcomes:
      - PRODUCT_SPEC
      - REPOSITORY_DISCOVERY
      - ARCHITECTURE_OR_DEPENDENCY_SELECTION
      - IMPLEMENTATION_EXECUTION
      - GIT_DELIVERY
    candidate_artifact_kinds: [INTENT_RECORD, DRAFT_FEATURE_PASSPORT, VALIDATION_ENVELOPE, REVIEW_PACKAGE]
  observable_acceptance:
    criteria: [FS1-CON-AC-001, FS1-CON-AC-002, FS1-CON-AC-003, FS1-CON-AC-004, FS1-CON-AC-005, FS1-CON-AC-006, FS1-CON-AC-007, FS1-CON-AC-008, FS1-CON-AC-009, FS1-CON-AC-010, FS1-CON-AC-011, FS1-CON-AC-012, X1-R2-AC-001, X1-R2-AC-002, X1-R2-AC-003, X1-R2-AC-004]
    negative_scenarios: [FS1-CON-NEG-001, FS1-CON-NEG-002, FS1-CON-NEG-003, FS1-CON-NEG-004, FS1-CON-NEG-005, FS1-CON-NEG-006, FS1-CON-NEG-007, FS1-CON-NEG-008, FS1-CON-NEG-009, FS1-CON-NEG-010, FS1-CON-NEG-011, FS1-CON-NEG-012, FS1-CON-NEG-013, FS1-CON-NEG-014, FS1-CON-NEG-015, FS1-CON-NEG-016, FS1-CON-NEG-017, X1-R2-NEG-001, X1-R2-NEG-002, X1-R2-NEG-003, X1-R2-NEG-004]
    evidence_needed:
      - EXACT_TARGET_READ_ONLY_PREFLIGHT
      - INDEPENDENT_IMPLEMENTATION_VALIDATION_EVIDENCE
      - MANUAL_REAL_TASK_EVIDENCE_FOR_IMPLEMENTED_FIRST_SLICE
  dependencies:
    accepted_contracts:
      - AOS_PROJECT_KNOWLEDGE_BASELINE
      - AOS_PRODUCT_RUNTIME_FOUNDATION_R1
      - AOS_PORTABLE_TASK_CANDIDATE_CONTRACT_R1
      - AOS_FIRST_SLICE_CONTRACT_PACKAGE_R1
      - AOS_X1_DOCUMENTATION_DECISION_SUBJECT_R1
    human_decisions_required:
      - ASSIGN_EXACT_IMPLEMENTATION_REPOSITORY
      - ASSIGN_HUMAN_RISK_PROFILE
      - SELECT_OR_DEFER_ARTIFACT_SERIALIZATION_FOR_TARGET
      - SELECT_OR_DEFER_CONCRETE_INTERFACE_AND_UI_FRAMEWORK_FOR_TARGET
      - SELECT_OR_DEFER_HUMAN_DECISION_AUTHENTICITY_MECHANISM_FOR_TARGET
      - SELECT_OR_DEFER_LANGUAGE_TOOLCHAIN_AND_DEPENDENCIES_FOR_TARGET
      - SELECT_OR_DEFER_PROVIDER_TRANSPORT_AND_PERSISTENCE_FOR_TARGET
    external_evidence_required:
      - EXACT_TARGET_READ_ONLY_PREFLIGHT
      - INDEPENDENT_IMPLEMENTATION_VALIDATION_EVIDENCE
      - MANUAL_REAL_TASK_EVIDENCE_FOR_IMPLEMENTED_FIRST_SLICE
  target_binding:
    status: UNBOUND
    repository: null
    worktree: null
    branch: null
    head_sha: null
    baseline: null
    allowed_paths: []
    forbidden_paths: []
    toolchain: []
  authority:
    candidate_owner: planning/INT_DOC_200_First_Slice_Decision_Record.md
    task_scope_owner: NOT_CREATED
    execution_authorization: NONE
    implementation_authorization: NONE
    git_authorization: NONE
  assumptions:
    - A_PROVIDER_NEUTRAL_LOGICAL_CONVERSATION_CAN_BE_ADAPTED_AFTER_TARGET_BINDING
    - USER_CAN_REVIEW_A_HUMAN_READABLE_PROJECTION_OF_THE_LOGICAL_RECORDS
  unknowns:
    - TARGET_REPOSITORY_AND_CURRENT_IDENTITY
    - TARGET_CONCRETE_INTERFACE_AND_UI_FRAMEWORK
    - TARGET_PROVIDER_TRANSPORT_AND_SESSION_BOUNDARY
    - TARGET_ARTIFACT_SERIALIZATION_AND_PERSISTENCE
    - TARGET_FEATURE_PASSPORT_IDENTIFIER_ALLOCATION_MECHANISM
    - TARGET_DECISION_AUTHENTICITY_MECHANISM
    - TARGET_LANGUAGE_TOOLCHAIN_AND_DEPENDENCIES
  risks:
    - POLISHED_DOCUMENT_WITHOUT_USER_COMPREHENSION
    - ASSUMPTION_PROMOTED_TO_FACT
    - GENERATED_REVIEW_MISTAKEN_FOR_ACCEPTANCE
    - TARGET_CHOICE_INVENTED_BEFORE_BINDING
  validation_plan:
    required_checks:
      - CONTRACT_SCHEMA_AND_STATE_MACHINE
      - ACCEPTANCE_AND_NEGATIVE_FIXTURE_COVERAGE
      - SUCCESSOR_MAPPING_DISPOSITION_AND_IDENTITY_BINDING
      - TARGET_AND_AUTHORITY_NON_INVENTION
      - MANUAL_REAL_TASK_COMPREHENSION
    independence_required: true
    expected_evidence:
      - SUBJECT_BOUND_VALIDATION_ENVELOPE
      - ZERO_WRITE_PROOF_FOR_READ_ONLY_VALIDATION
      - HUMAN_REVIEW_RECORD_FOR_EXACT_CANDIDATE
  conversion_gate:
    readiness: DOCUMENTATION_VALIDATION_AND_HUMAN_ACCEPTANCE_REQUIRED
    blockers:
      - X1_R2_SUCCESSOR_REQUIRES_INDEPENDENT_VALIDATION_AND_HUMAN_ACCEPTANCE
      - IMPLEMENTATION_REPOSITORY_UNASSIGNED
      - TARGET_BINDING_NOT_RUN
    one_next_action: INDEPENDENT_VALIDATE_EXACT_X1_R2_SUCCESSOR
  provenance:
    created_from_task_id: X1-DOCUMENTATION-SUCCESSOR-CONTRACT-R2-001
    predecessor_contract_sha256: 8c8169d5b45ebce7e6feacb49e9f058f3d08d0de2dea5ebee96cc3b73f4d85f0
    C002_identity_decision_sha256: 8dc24bf0390e3d8cce1e508b10224034203fc92fa8364be8f26c10c9cf4f162a
    candidate_manifest_sha256: 18816ffe7851b79e7c9f7cbd976fbc72c1936af233bd57e5e6ca71b6338cb370
  human_decision: null
```

## 14. Portable Task Candidate identity manifest

The following block is exact UTF-8 with LF line endings and one final LF. Tabs
separate manifest fields. Repeated source, feature, decision and Evidence records
are UTF-8-byte sorted.

```text
AOS-PORTABLE-TASK-CANDIDATE-V1
CANDIDATE	PTC-AOS-FIRST-SLICE-001	7
SOURCE	docs/00_Core.md	96787a64585264e9f0d6beb1aab28bc717f80436003dfc6c093736541a95c34c	HUMAN_ACCEPTED_PROJECT_CORE
SOURCE	docs/01_Product.md	bbbce8e166bc4640f8fd98c9407539159a41d216ab9ee993ad2369f07ac81625	HUMAN_ACCEPTED_PRODUCT_BASELINE
SOURCE	docs/02_Architecture.md	3724a3369c78f6504c56a0f6d921839839d7adecc9ca806f1fe9d3e65b11be84	HUMAN_ACCEPTED_ARCHITECTURE_BASELINE
SOURCE	docs/03_Development.md	251730eb5cdab9776a97caf29a6791e1f3645fa6b8f01c6de93c5c4a2bbed9b1	HUMAN_ACCEPTED_WORKFLOW_BASELINE
SOURCE	docs/06_Features.md	276381e4cfaf565e691fd8098a0f1c4d648b65071f306c476f79cd3ae52fe923	HUMAN_ACCEPTED_INVENTORY_WITH_X1_ITEM_DISPOSITIONS
SOURCE	planning/AOS_Documentation_Task_Sequence_R9.md	be91cbffcd2c79a0a632b661157e5e2e7fb7a68d1056ba1c9684f2ea1b549ee7	HUMAN_ACCEPTED_ROADMAP
SOURCE	planning/AOS_Portable_Task_Candidate_Contract_R1.md	e333a326b185f4cd8b91e978b3bd7c7f4449a2de9f76616f69def8bea1076cb4	HUMAN_ACCEPTED_PORTABLE_TASK_CONTRACT
SOURCE	planning/INT_DOC_200_First_Slice_Decision_Record.md	5057afd7120b3624a4d1b859cba04f7ecb6c2f204b99bd59c955550e3903e449	HUMAN_FIRST_SLICE_DECISION
SOURCE	planning/INT_DOC_210_Interaction_Surface_Decision_Record.md	1049b38901a424748708e85879896cc9139dc389d16ae8918d54cedc3a394dcb	HUMAN_INTERACTION_SURFACE_DECISION
SOURCE	planning/X1_Documentation_Decision_Record_R1.md	6aed802f59fa522ce5bf21efd4de3ee50f6912e9b733dec63d4677db05b25eca	HUMAN_ACCEPTED_X1_DOCUMENTATION_DECISION_EVIDENCE
SOURCE	planning/X1_Documentation_Decision_Record_R1_Acceptance_Record.md	4e6c1b42cbd0248f497974ccfe5b925f55ec80d30f5e81b31954d9680eff3730	HUMAN_X1_DECISION_SUBJECT_ACCEPTANCE
SOURCE	planning/first-slice/AOS_First_Slice_Contract_Package_R1.md	8c8169d5b45ebce7e6feacb49e9f058f3d08d0de2dea5ebee96cc3b73f4d85f0	HUMAN_ACCEPTED_PREDECESSOR_PRODUCT_CONTRACT
SOURCE	planning/first-slice/AOS_First_Slice_Decision_Package_R1.md	7cb6abc358afa5aaa11f8a48553cfedc6ce975ced7496aa30065aac9825df280	VALIDATED_DECISION_SUPPORT_SUBJECT
SOURCE	planning/first-slice/AOS_X1_Documentation_Closure_Package_R1.md	ee9c0ba2fff2163a2b8783f36b59ffe2d2d282b1ab160a20ccab486f58873999	HUMAN_ACCEPTED_X1_CLOSURE_DECISION_SUPPORT
SOURCE	planning/foundation/AOS_Product_Runtime_Foundation_Package_R1.md	8b1ab2c4da097380b73f7b563d9a44cb7ed12a786aabe438905152e1ccaef3af	HUMAN_ACCEPTED_FOUNDATION
FEATURE	FTR-001
FEATURE	FTR-003
FEATURE	FTR-005
FEATURE	FTR-006
FEATURE	FTR-011
FEATURE	FTR-012
FEATURE	FTR-013
DECISION_REQUIRED	ASSIGN_EXACT_IMPLEMENTATION_REPOSITORY
DECISION_REQUIRED	ASSIGN_HUMAN_RISK_PROFILE
DECISION_REQUIRED	SELECT_OR_DEFER_ARTIFACT_SERIALIZATION_FOR_TARGET
DECISION_REQUIRED	SELECT_OR_DEFER_CONCRETE_INTERFACE_AND_UI_FRAMEWORK_FOR_TARGET
DECISION_REQUIRED	SELECT_OR_DEFER_HUMAN_DECISION_AUTHENTICITY_MECHANISM_FOR_TARGET
DECISION_REQUIRED	SELECT_OR_DEFER_LANGUAGE_TOOLCHAIN_AND_DEPENDENCIES_FOR_TARGET
DECISION_REQUIRED	SELECT_OR_DEFER_PROVIDER_TRANSPORT_AND_PERSISTENCE_FOR_TARGET
EVIDENCE_REQUIRED	EXACT_TARGET_READ_ONLY_PREFLIGHT
EVIDENCE_REQUIRED	INDEPENDENT_IMPLEMENTATION_VALIDATION_EVIDENCE
EVIDENCE_REQUIRED	MANUAL_REAL_TASK_EVIDENCE_FOR_IMPLEMENTED_FIRST_SLICE
TARGET_STATUS	UNBOUND
AUTHORIZATION	NONE	NONE	NONE
```

```yaml
manifest_byte_length: 3207
manifest_sha256: 18816ffe7851b79e7c9f7cbd976fbc72c1936af233bd57e5e6ca71b6338cb370
```

## 15. Traceability matrix

| Contract concern | Owner / feature | Specialized result |
|---|---|---|
| Intent preservation and classification | `FTR-001`; `C-001` | Logical Intent Record and correction rules |
| Full first-feature definition | `FTR-003`; `C-002` | Exact DRAFT Feature Passport contract |
| Architecture need | `FTR-005`; `C-004` | Documentation-level `NO_ADR_REQUIRED`; target choices gated |
| Bounded handoff and authority | `FTR-006`; `C-005`, `C-006` | Portable candidate only; no Task Brief or authorization |
| Result and Self-Test | `FTR-011`; `C-009` | Required checks and fail-closed aggregation |
| Human review separation | `FTR-012`; `C-011` | Candidate-bound review; decision remains human-owned |
| Freeze and isolated validation | `FTR-013` | Exact candidate identity and separate zero-write validation |
| Recovery and continuity | Foundation; `C-012` | Revision-bound correction, resume and handoff rules |

## 16. Known unknowns and X1 handoff boundary

| Unknown or decision | Current state | Required later gate |
|---|---|---|
| Implementation repository | `UNASSIGNED` | Exact human repository-role assignment |
| Target repository identity and paths | `UNBOUND` | Read-only Target Repository Binding |
| Concrete interface and UI framework | `UNDECIDED` | Target-specific human product/architecture decision |
| Provider, transport and session boundary | `UNDECIDED` | Target-specific human product/architecture decision |
| Artifact serialization and persistence | `UNDECIDED` | Target contract decision before byte-bound implementation |
| Feature Passport identifier allocation | `TARGET_BOUND_UNDECIDED` | Target contract decision; static composite ID is not applicable |
| Decision-authenticity mechanism | `UNDECIDED` | Human product/security decision |
| Language, toolchain and dependencies | `UNDECIDED` | Target-bound architecture/implementation decision |
| Risk Profile | `UNASSIGNED` | Human assignment for exact target-bound task |
| Runtime feasibility and user comprehension | `NOT_RUN` | `X1` implementation and manual real-task Evidence |

After independent validation and exact human `ACCEPT` of this documentation,
the package may support `X1`. It does not activate or pass `X1`. The next chain
remains:

```text
human assigns exact implementation repository
→ read-only target preflight
→ Target Repository Binding
→ resolve exact target-dependent decisions
→ target-bound Task Brief
→ human assigns Risk Profile
→ separate Execution Authorization
→ implementation Stage Report
→ independent validation and manual real-task Evidence
→ Human Slice Stabilization Decision
```

## 17. Completion and validation route

This `X1-DOCUMENTATION-SUCCESSOR-CONTRACT-R2-001` candidate is internally complete only when:

1. selected segment, job, outcome and interaction surface bind to exact human
   decision records;
2. the accepted composite mapping, item dispositions and output-instance C-002
   identity semantics bind to exact human decisions without changing R1 behavior;
3. C-001 and C-002 logical schemas, states, failures and recovery are complete;
4. `NO_ADR_REQUIRED` is scoped only to the logical documentation handoff;
5. acceptance and all required negative fixtures are explicit;
6. the independent validation plan supports `L0 + L1 + L2` and zero-write;
7. the Portable Task Candidate validates against its accepted contract and
   exact manifest identity;
8. target facts, implementation, acceptance and Git authority are not invented;
9. a cold-start agent can identify all remaining gates without chat history;
10. Markdown, frontmatter, links, fences, IDs and allowed paths pass internal
    checks; and
11. the final bytes are frozen in the terminal Stage Report.

After freeze:

```text
terminal EXECUTE Stage Report
→ STOP
→ separately authorized POST_STOP_DOCUMENTATION VALIDATE
→ Verification Report
→ STOP
→ human review of the exact validated candidate
```

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
