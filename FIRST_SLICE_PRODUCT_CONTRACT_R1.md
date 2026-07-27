---
artifact: FIRST_SLICE_PRODUCT_CONTRACT_R1
artifact_id: FIRST_SLICE_PRODUCT_CONTRACT
revision: R1
created: '2026-07-27'
status: DRAFT_FOR_HUMAN_DECISION
document_maturity: HUMAN_REVIEW_REQUIRED
authority: PROPOSAL
fact_class: FEATURE_SPECIFIC_PRODUCT_CONTRACT_PROPOSAL
scope: CORE-SLICE-001_ONLY
human_decision: null
implementation_readiness: false
implementation_authorization: NONE
execution_authorization: NONE
git_authorization: NONE
runtime_validation: NOT_RUN
status_model: ORTHOGONAL
technical_results:
  file_level_validation: NOT_RUN
  internal_consistency_validation: NOT_RUN
  runtime_validation: NOT_RUN
upstream_authority:
  c0_package:
    package_id: AOS-C0
    package_revision: C0-R4
    artifact_path: AOS_C0_Decision_Package_R4.md
    sha256: e9cf87df74419f152efd00f0c82af2b7d8d92b685df538e1ae71b31969308bc0
  human_decision:
    decision_record_id: AOS-C0-HUMAN-DECISION-001
    decision_record_revision: R1
    contract_class: C-011
    artifact_path: AOS_C0_Human_Decision_Record_R1.md
    sha256: e6e2968af134c5f2f2d41a3dd0b1a7a3a39cca55bcb52fd8ef435f2c9bc70201
    decision: ACCEPT
source_baseline:
  repository: NMF13579/notebook
  branch: dev
  head_commit: d783f7d8cd0d2af2fb88fafa23ea16f289ef8ea6
  source_document:
    path: docs/00_Core.md
    blob_sha: 24e2f4816946e91713280e881c74f391e7bc3795
    package: AOS_Project_Knowledge_Baseline
    package_revision: R4-RU
accepted_c0_selections:
  C0-D01: U-A_DOMAIN_EXPERT_TO_FIRST_PRODUCT_PACKAGE
  C0-D02: S-A_INTENT_TO_ACCEPTED_FIRST_FEATURE_PASSPORT
  C0-D03: A-B_LOCAL_FIRST_MODULAR_MONOLITH
  C0-D04: P-B_MINIMAL_C003_PLUS_ONE_C002
contract_classes_used:
  - C-001
  - C-003
  - C-002
  - C-011
new_canonical_contract_class_created: false
feature_dossier_admission:
  full_dossiers_accepted: false
  catalog_human_disposition_changed: false
  relation_scope: CORE-SLICE-001_ONLY
external_dependencies:
  - id: P2-01_CANONICAL_STATUS_AXIS_CONFLICT
    disposition: DEFERRED_SEPARATE_CORRECTION
    required_before: GLOBAL_STATUS_SCHEMA_IMPLEMENTATION
subject_binding:
  algorithm: SHA-256
  digest_location: DETACHED_CHECKSUM
  checksum_file: FIRST_SLICE_PRODUCT_CONTRACT_R1.md.sha256
---

# First Slice Product Contract — R1

## 1. Вывод и contract boundary

`FIRST_SLICE_PRODUCT_CONTRACT_R1` предлагает exact product behavior для
`CORE-SLICE-001`:

```text
one DOMAIN_EXPERT_PRODUCT_OWNER
→ supplies one incomplete intent
→ AOS preserves the source and exposes critical gaps
→ AOS asks bounded material questions
→ AOS produces one C-001 Intent Record
→ AOS produces one minimal-depth C-003 Product Spec
→ AOS produces one C-002 Feature Passport
→ AOS renders one exact review subject
→ explicit human action records one separate C-011 decision
→ AOS shows one bounded next action
```

This document is a `PROPOSAL`. It defines behavior required before
implementation planning, but it is not implementation-ready and creates no
permission to implement, execute, mutate a user repository, or perform Git
actions.

### 1.1. Success condition

The slice succeeds when a domain expert can start with an incomplete product
idea and reach one exact, understandable, reviewable first-feature package
without understanding repository mechanics. The user can identify the actor,
problem, desired outcome, slice boundary, assumptions, unknowns, non-goals,
observable behavior, decision options, and one next action.

### 1.2. Fixed boundaries

```yaml
layer: PRODUCT_RUNTIME
operating_model: SINGLE_USER_SINGLE_PROCESS
core_network_requirement: NONE
user_repository_access: NOT_REQUIRED
user_repository_mutation: FORBIDDEN
code_execution: FORBIDDEN
git_actions: FORBIDDEN
aos_local_state_writes: REQUIRED
write_model: ATOMIC_OR_JOURNALED
manual_structured_fallback: REQUIRED
```

## 2. Authority and actors

| Actor | Purpose | Authority | Must not do |
|---|---|---|---|
| `AOS_PRODUCT_OWNER` | Owns product direction of AOS itself | Accepts, changes, rejects, or defers this Product Contract and later AOS-level product policies | Decide a domain expert's product content automatically |
| `DOMAIN_EXPERT_PRODUCT_OWNER` | First user of the slice and owner of the submitted product intent | Corrects product facts and decides the exact first-slice product package | Grant implementation, execution, repository, or Git permission |
| `INTERACTION_OPERATOR` | Helps the user operate the local interaction surface | May capture input and persist an explicitly supplied action with provenance | Invent, infer, substitute, or own a product decision |
| `AGENT_ADAPTER` | Converts conversation into non-authoritative proposals | May propose questions, classifications, assumptions, and draft content | Create a valid decision, gain authority, write directly to canonical storage, or mutate a user repository |

### 2.1. Role combination

1. One physical human may hold both `AOS_PRODUCT_OWNER` and
   `DOMAIN_EXPERT_PRODUCT_OWNER`, but each action must name the role appropriate
   to its exact subject.
2. `DOMAIN_EXPERT_PRODUCT_OWNER` may also act as `INTERACTION_OPERATOR`.
3. A trusted human may operate the surface for a present
   `DOMAIN_EXPERT_PRODUCT_OWNER`; `decided_by` and `recorded_by` remain separate.
4. `AGENT_ADAPTER` can never satisfy a human role.
5. Self-attestation is permitted for the single-user first version.
   Cryptographic or multi-user identity assurance is not claimed.

### 2.2. Decision ownership

| Decision | Required actor |
|---|---|
| Accept/change/reject/defer this Product Contract | `AOS_PRODUCT_OWNER` |
| Correct human-provided product content | `DOMAIN_EXPERT_PRODUCT_OWNER` |
| Confirm or reject an assumption | `DOMAIN_EXPERT_PRODUCT_OWNER` |
| Accept/change/reject/defer the exact first-slice package | `DOMAIN_EXPERT_PRODUCT_OWNER` |
| Choose implementation repository, language, dependencies, or capture mechanism | Separate future human decision; not selected here |
| Authorize implementation, execution, or Git actions | Separate future human authority; not created here |

## 3. Trigger, preconditions, and input classification

### 3.1. Cycle trigger

A new cycle begins only after an explicit local action:

```yaml
operation: START_FIRST_SLICE_CYCLE
requested_by_role: DOMAIN_EXPERT_PRODUCT_OWNER
operator_role: DOMAIN_EXPERT_PRODUCT_OWNER | INTERACTION_OPERATOR
intent_input: REQUIRED
```

Conversation, file presence, agent inference, resume, or previous acceptance
must not start a new cycle automatically.

### 3.2. Minimum user input

The only mandatory user-supplied field at cycle start is:

```yaml
original_request:
  type: string
  minimum_semantics: >-
    One non-empty statement describing a software-product problem, pain,
    capability, idea, or desired outcome.
```

The capture boundary must also record actor role, source channel, and capture
time. These are provenance, not additional prose the user must type.

Optional initial input:

- context or current workaround;
- intended user;
- known constraints;
- explicit non-goals;
- success signals;
- sensitive-domain or provider flags;
- proposed solution.

An incomplete, solution-biased, informal, or internally inconsistent request is
valid intake. It is not automatically sufficient for contract assembly.

### 3.3. Missing input

Input is materially missing when it is:

- absent, null, empty, or whitespace-only;
- only a greeting, acknowledgement, or control phrase with no product idea;
- unreadable or truncated such that no problem, capability, or desired outcome
  can be recovered;
- presented without a human-controlled start action.

Required behavior:

```yaml
workflow_state: CLARIFICATION_REQUIRED
technical_result: BLOCKED
human_decision: null
durable_outputs:
  - original input capture, if any bytes were supplied
forbidden:
  - fabricated C-003
  - fabricated C-002
  - inferred ACCEPT
```

### 3.4. Material ambiguity

Input is materially ambiguous when at least two reasonable interpretations
would change one or more of:

- first user or beneficiary;
- problem or desired outcome;
- observable first-slice value;
- product boundary or non-goals;
- sensitive/provider boundary;
- acceptance criterion;
- authority or requested operation.

The system records the alternatives as `CONFLICT` and asks the human to resolve
them. It must not choose a side.

## 4. Common identity, revision, and provenance rules

### 4.1. Logical identity

Every canonical artifact carries:

```yaml
contract_class: C-001 | C-003 | C-002 | C-011
artifact_id: '<stable opaque identifier within its fact class>'
cycle_id: '<stable opaque identifier for one CORE-SLICE-001 cycle>'
revision: '<positive monotonically increasing integer>'
created_at: '<timestamp>'
created_by:
  actor_class: HUMAN | AGENT_ADAPTER | DETERMINISTIC_COMPONENT
  actor_identity: '<recorded identity>'
source_refs: []
```

Identifier generation format is an implementation choice. Required semantics
are uniqueness in the local store, stability across revisions of the same
logical artifact, and no reuse across unrelated cycles.

### 4.2. Revision semantics

1. Canonical revisions are immutable after durable publication.
2. Any content change creates a successor revision.
3. A successor includes `parent_revision_ref` with artifact ID, revision, and
   digest.
4. A valid decision remains bound only to the exact old subject.
5. Old revisions and decisions are preserved.
6. `current` is a derived pointer to the latest valid committed revision; it is
   not an independent product fact.
7. A partial or corrupt revision never becomes current.

### 4.3. Digest and byte identity

```yaml
digest_algorithm: SHA-256
digest_subject: EXACT_PERSISTED_ARTIFACT_BYTES
digest_required_for:
  - immutable artifact reference
  - review subject manifest
  - C-011 decision binding
```

The exact serialization format, encoding profile, and filesystem path are
deferred architecture/implementation decisions. Whichever profile is selected
must make persisted bytes deterministic and declare its media type and encoding
in the artifact metadata.

### 4.4. Canonical reference

```yaml
artifact_ref:
  contract_class: '<C-001 | C-003 | C-002 | C-011>'
  artifact_id: '<stable id>'
  revision: '<positive integer>'
  sha256: '<64 lowercase hexadecimal characters>'
```

References with missing fields or a digest mismatch are invalid.

## 5. Contract ownership map

| Fact class | Canonical owner | References but must not duplicate |
|---|---|---|
| Original request, initial interpretation, input provenance, assumptions, unknowns | `C-001 Intent Record` | C-003/C-002 |
| Product-level problem, first user/JTBD, goal, journey, boundary, non-goals, metrics, dependencies, acceptance boundary, open decisions | minimal-depth `C-003 Product Spec` | C-002 |
| Exact first-feature behavior, trigger, I/O, flow, states, failures, recovery, acceptance and negative scenarios | one `C-002 Feature Passport` | C-003 |
| Human decision about exact review subject | separate `C-011 Human Decision Record` | All content artifacts |
| Review, status, next, and details presentation | Derived view | All canonical contracts |

`FIRST_SLICE_PRODUCT_CONTRACT_R1` is a feature-specific specification package,
not a new canonical contract class. The review-subject manifest defined below
contains only bindings; it owns no product fact.

## 6. `C-001 Intent Record`

### 6.1. Purpose and owner

`C-001` preserves the human's original input and the first bounded
interpretation without promoting inference to fact.

```yaml
contract_class: C-001
fact_owner: INTENT_AND_INTAKE_PROVENANCE
content_authority:
  human_provided_fields: DOMAIN_EXPERT_PRODUCT_OWNER
  assumptions: PROPOSAL_ONLY
  unknowns: EXPLICIT_UNRESOLVED_STATE
```

### 6.2. Logical schema

```yaml
contract_class: C-001
artifact_id: '<intent_id>'
cycle_id: '<cycle_id>'
revision: 1
parent_revision_ref: null
document_maturity: DRAFT | HUMAN_REVIEW_REQUIRED | SUPERSEDED
original_request:
  text: '<exact captured text>'
  captured_bytes_sha256: '<sha256>'
  captured_at: '<timestamp>'
  submitted_by_role: DOMAIN_EXPERT_PRODUCT_OWNER
source:
  channel_class: HUMAN_CONTROLLED_INPUT
  channel_identifier: '<actual channel>'
  recorded_by:
    recorder_class: SAME_HUMAN | TRUSTED_HUMAN_OPERATOR | DETERMINISTIC_CAPTURE_COMPONENT
    recorder_identity: '<actual recorder>'
problem:
  value: '<text or null>'
  classification: HUMAN_PROVIDED | HUMAN_CONFIRMED | ASSUMPTION | UNKNOWN
desired_outcome:
  value: '<text or null>'
  classification: HUMAN_PROVIDED | HUMAN_CONFIRMED | ASSUMPTION | UNKNOWN
initial_actor:
  value: '<text or null>'
  classification: HUMAN_PROVIDED | HUMAN_CONFIRMED | ASSUMPTION | UNKNOWN
context: []
constraints: []
non_goals: []
assumptions: []
unknowns: []
sensitive_domain_flags: []
conflicts: []
provenance_events: []
```

### 6.3. Required fields

The schema fields above are required, but `problem.value`,
`desired_outcome.value`, and `initial_actor.value` may be null only when their
classification is `UNKNOWN` and a resolution path exists.

Each assumption uses:

```yaml
assumption_id: '<stable within C-001>'
statement: '<proposed statement>'
basis: '<human input fragment or inference rationale>'
impact_if_wrong: '<affected artifact or decision>'
status: PROPOSED | HUMAN_CONFIRMED | HUMAN_REJECTED
confirmation_ref: null | '<human action provenance>'
```

Each unknown uses:

```yaml
unknown_id: '<stable within C-001>'
question: '<missing knowledge>'
materiality: CRITICAL | NON_CRITICAL
blocks:
  - '<artifact or action>'
resolution_path: '<one bounded human action>'
status: OPEN | RESOLVED | DEFERRED
```

### 6.4. Validation

- original request and capture provenance are present;
- original request digest matches captured bytes;
- every inferred statement is classified `ASSUMPTION`;
- every null material field has an `UNKNOWN`;
- every critical unknown names a blocked artifact/action;
- no feature behavior, architecture, execution permission, or Git permission is
  owned by C-001;
- no content is silently rewritten in place.

## 7. Minimal-depth `C-003 Product Spec`

### 7.1. Purpose and owner

`C-003` owns the minimum product context needed to understand one first
feature. It does not become a roadmap, broad platform specification, or
execution authorization.

```yaml
contract_class: C-003
fact_owner: PRODUCT_LEVEL_CONTEXT_FOR_CORE_SLICE_001
depends_on:
  - exact C-001 artifact_ref
```

### 7.2. Logical schema

```yaml
contract_class: C-003
artifact_id: '<product_spec_id>'
cycle_id: '<cycle_id>'
revision: '<positive integer>'
parent_revision_ref: null | '<artifact_ref>'
document_maturity: DRAFT | HUMAN_REVIEW_REQUIRED | SUPERSEDED
intent_record_ref: '<C-001 artifact_ref>'
product_problem:
  statement: '<text or explicit UNKNOWN>'
  provenance_refs: []
first_user_and_jtbd:
  user: '<text or explicit UNKNOWN>'
  job_to_be_done: '<text or explicit UNKNOWN>'
  provenance_refs: []
first_product_goal: '<text or explicit UNKNOWN>'
first_user_journey:
  start: '<trigger>'
  observable_end: '<user-visible result>'
  steps: []
first_slice_boundary:
  in_scope: []
  out_of_scope: []
product_non_goals: []
material_constraints: []
candidate_success_metrics:
  - metric: '<name>'
    collection_method: '<observable method>'
    threshold: UNDECIDED | '<human-decided value>'
product_level_dependencies: []
product_acceptance_boundary:
  review_subject: ONE_C003_PLUS_ONE_C002
  decision_actor_role: DOMAIN_EXPERT_PRODUCT_OWNER
  allowed_decisions:
    - ACCEPT
    - NEEDS_CHANGES
    - REJECT
    - DEFER
open_decisions: []
assumption_refs: []
unknown_refs: []
```

### 7.3. Required-field semantics

All fields in §7.2 are structurally required. Material absence is represented
as explicit `UNKNOWN` plus resolution path; it is never omitted or fabricated.

`broader_journeys`, `additional_user_segments`, `multi_feature_roadmap`,
`registry_policy`, and `expansion_metrics_thresholds` are outside required
first-slice depth.

### 7.4. Expansion rule

The first-slice cycle must never auto-expand `C-003`. If a critical product
question cannot be represented at minimal depth:

```yaml
workflow_state: CLARIFICATION_REQUIRED
technical_result: BLOCKED
affected_action: REVIEW_READY
next_action: REQUEST_SEPARATE_PRODUCT_SCOPE_DECISION
```

Broader Product Spec expansion remains a separate human decision. It does not
silently enlarge this cycle.

### 7.5. Validation

- exact C-001 dependency binding is valid and current;
- all required fields are present or explicitly `UNKNOWN`;
- product-level facts are not duplicated in C-002;
- only one first user, one JTBD, one first goal, and one first journey are in
  scope;
- metrics without evidence retain `threshold: UNDECIDED`;
- no Task Brief, repository choice, architecture of the user's product,
  implementation claim, or permission is present.

## 8. One `C-002 Feature Passport`

### 8.1. Purpose and owner

`C-002` owns exact observable behavior of the one proposed first feature. It
references product facts by identity rather than duplicating them.

```yaml
contract_class: C-002
fact_owner: FIRST_FEATURE_BEHAVIOR_FOR_CORE_SLICE_001
cardinality_per_review_subject: EXACTLY_ONE
depends_on:
  - exact C-003 artifact_ref
  - exact C-001 artifact_ref
```

### 8.2. Logical schema

```yaml
contract_class: C-002
artifact_id: '<feature_passport_id>'
feature_id: '<stable first-feature id>'
cycle_id: '<cycle_id>'
revision: '<positive integer>'
parent_revision_ref: null | '<artifact_ref>'
document_maturity: DRAFT | HUMAN_REVIEW_REQUIRED | SUPERSEDED
intent_record_ref: '<C-001 artifact_ref>'
product_spec_ref: '<C-003 artifact_ref>'
purpose: '<observable first-feature value>'
users:
  - role: DOMAIN_EXPERT_PRODUCT_OWNER
    product_context_ref: '<C-003 field reference>'
trigger: '<observable trigger>'
preconditions: []
inputs: []
outputs: []
main_flow: []
states: []
transitions: []
failures: []
recovery: []
dependencies: []
constraints: []
authority_boundaries: []
acceptance_criteria: []
negative_scenarios: []
non_goals: []
assumption_refs: []
unknown_refs: []
evidence_status: NOT_RUN
human_disposition:
  value: UNDECIDED
  authority_ref: null
```

### 8.3. Required behavior

The passport must define:

1. the explicit cycle trigger;
2. minimum and optional inputs;
3. observable outputs;
4. the clarification flow;
5. workflow states and transitions;
6. invalid input and conflicting input behavior;
7. interruption, partial-write, corruption, stale-binding, and duplicate
   decision behavior;
8. recovery and idempotent retry;
9. authority and permission boundaries;
10. acceptance criteria and fail-closed negative tests.

### 8.4. Validation

- exactly one C-002 exists in a review subject;
- C-001 and C-003 references are valid and current;
- user/JTBD and product goal are referenced, not independently restated;
- all state transitions have a trigger, guard, effect, and failure outcome;
- each failure has a recovery path or explicit terminal stop;
- acceptance criteria are observable;
- `human_disposition.value` remains `UNDECIDED` inside frozen bytes;
- no technical `PASS` changes disposition or maturity;
- no repository mutation, execution, or Git action exists.

## 9. `C-011 Human Decision Record`

### 9.1. Purpose and owner

`C-011` is the only owner of the decision about an exact first-slice review
subject.

```yaml
contract_class: C-011
fact_owner: HUMAN_DECISION
required_actor_role: DOMAIN_EXPERT_PRODUCT_OWNER
generation_by_agent: INVALID
```

### 9.2. Review-subject manifest

The manifest is a binding structure, not a new canonical contract class. It
owns no product content.

```yaml
review_subject_manifest:
  package_id: '<first_slice_review_package_id>'
  package_revision: '<positive integer>'
  cycle_id: '<cycle_id>'
  intent_record_ref: '<C-001 artifact_ref>'
  product_spec_ref: '<C-003 artifact_ref>'
  feature_passport_ref: '<C-002 artifact_ref>'
  manifest_sha256: '<sha256 of exact persisted manifest bytes>'
```

### 9.3. Logical schema

```yaml
contract_class: C-011
decision_record_type: FIRST_SLICE_PRODUCT_PACKAGE_HUMAN_DECISION
artifact_id: '<decision_record_id>'
cycle_id: '<cycle_id>'
revision: 1
subject:
  manifest_ref:
    package_id: '<id>'
    package_revision: '<revision>'
    sha256: '<manifest digest>'
  product_spec_ref: '<C-003 artifact_ref>'
  feature_passport_ref: '<C-002 artifact_ref>'
  intent_dependency_ref: '<C-001 artifact_ref>'
decision: ACCEPT | NEEDS_CHANGES | REJECT | DEFER
accepted_artifact_refs: []
requested_changes: []
comment: ''
decided_by:
  actor_role: DOMAIN_EXPERT_PRODUCT_OWNER
  actor_identity: '<human-controlled self-attested identity>'
recorded_by:
  recorder_class: SAME_HUMAN | TRUSTED_HUMAN_OPERATOR | DETERMINISTIC_CAPTURE_COMPONENT
  recorder_identity: '<actual recorder>'
capture_channel:
  class: HUMAN_CONTROLLED_EXPLICIT_ACTION
  implementation: '<actual mechanism>'
  explicit_human_intent: true
agent_generated_decision: false
recorded_at: '<timestamp>'
implementation_authorization: NONE
execution_authorization: NONE
git_authorization: NONE
```

### 9.4. Validation

1. For `ACCEPT`, `accepted_artifact_refs` equals exactly the bound C-003 and
   C-002 references, and `requested_changes` is empty.
2. For `NEEDS_CHANGES`, `REJECT`, or `DEFER`,
   `accepted_artifact_refs` is empty.
3. Actor identity, role, timestamp, explicit intent, subject revision, and all
   digests are required.
4. The manifest, C-003, C-002, and C-001 dependency bindings must validate.
5. `agent_generated_decision` must be `false`.
6. The agent, adapter, operator, UI, validator, or `PASS` result cannot create
   or infer the decision.
7. The first valid terminal decision for an exact subject is immutable.
8. An identical repeated capture returns the existing record idempotently.
9. A different second decision for the same exact subject is rejected as
   `CONTRACT_VIOLATION`.
10. Reconsideration requires a successor review subject and a new C-011 record.

## 10. Clarification contract

### 10.1. Critical gaps

A gap is critical when it prevents a truthful, single interpretation of:

- the first user or beneficiary;
- the product problem or desired outcome;
- the first observable user value;
- the first-slice in-scope/out-of-scope boundary;
- a material constraint or contradiction;
- sensitive/provider routing;
- an acceptance criterion;
- human authority or requested operation.

### 10.2. Question policy

```yaml
questions_per_turn:
  maximum: 3
  selection: HIGHEST_MATERIALITY_FIRST
question_requirements:
  - resolves one named critical gap
  - explains why the answer matters
  - provides bounded choices when that does not distort the answer
  - never asks for implementation mechanics not required by product behavior
remaining_gaps:
  treatment: KEEP_VISIBLE_FOR_LATER_TURN
```

If one answer resolves or invalidates other gaps, the next turn recalculates the
question set. A fixed questionnaire is forbidden.

### 10.3. Assumption policy

An assumption is allowed only when the gap is:

- non-critical;
- reversible;
- not authority-, permission-, sensitive-data-, actor-, outcome-, or
  acceptance-defining;
- explicitly visible in C-001 and the review view.

An assumption never becomes a fact from repetition, confidence, model output,
or technical `PASS`. The human may confirm, reject, or leave it unresolved.
Confirmation or rejection creates a successor C-001 revision; old bytes remain
preserved.

### 10.4. Clarification stop conditions

| Condition | Workflow state | Technical result | Human decision |
|---|---|---|---|
| Critical gap remains after current bounded question turn | `CLARIFICATION_REQUIRED` | `BLOCKED` | `null` |
| Human cannot or does not wish to resolve now | `DECISION_RECORDED` after valid record | `NOT_RUN` or last exact result | `DEFER` |
| Answers conflict materially | `CLARIFICATION_REQUIRED` | `CONTRACT_VIOLATION` | `null` |
| Sensitive route lacks policy | State otherwise unchanged | `BLOCKED` for external route only | `null` |
| Manual/offline route remains sufficient | Continue current stage | Independent check result | `null` |

`DEFERRED` is not a workflow state or technical result in this contract.
`DEFER` is a human decision owned only by C-011.

## 11. End-to-end workflow and orthogonal state

### 11.1. Independent axes

```yaml
workflow_state:
  enum:
    - INTAKE_EMPTY
    - INTAKE_CAPTURED
    - CLARIFICATION_REQUIRED
    - CONTRACT_ASSEMBLY
    - REVIEW_READY
    - DECISION_RECORDED

document_maturity:
  enum:
    - DRAFT
    - HUMAN_REVIEW_REQUIRED
    - HUMAN_ACCEPTED
    - SUPERSEDED

technical_result:
  enum:
    - CONTRACT_VIOLATION
    - FAIL
    - BLOCKED
    - UNKNOWN
    - NOT_RUN
    - PASS

human_decision:
  nullable: true
  enum_when_present:
    - ACCEPT
    - NEEDS_CHANGES
    - REJECT
    - DEFER

permission:
  enum:
    - ALLOWED
    - HUMAN_AUTHORIZATION_REQUIRED
    - BLOCKED_POLICY
    - BLOCKED_UNKNOWN
    - NOT_APPLICABLE
```

`HUMAN_REVIEW_REQUIRED` is used only as document maturity. The external
`P2-01_CANONICAL_STATUS_AXIS_CONFLICT` remains unresolved and blocks only a
future global status-schema implementation.

### 11.2. Workflow transitions

| From | Trigger/guard | To | Required durable effect | Failure outcome |
|---|---|---|---|---|
| `INTAKE_EMPTY` | Explicit start plus non-empty input | `INTAKE_CAPTURED` | Immutable source capture and C-001 revision | Missing input → `CLARIFICATION_REQUIRED/BLOCKED` |
| `INTAKE_CAPTURED` | Critical gaps detected | `CLARIFICATION_REQUIRED` | Gap and question records | No fabricated product facts |
| `INTAKE_CAPTURED` | No critical gaps | `CONTRACT_ASSEMBLY` | Current valid C-001 reference | Binding failure → `BLOCKED` |
| `CLARIFICATION_REQUIRED` | Valid human answer | Re-evaluate, then same state or `CONTRACT_ASSEMBLY` | Successor C-001 revision | Conflict → `CONTRACT_VIOLATION` |
| `CONTRACT_ASSEMBLY` | Valid current C-001 | `CONTRACT_ASSEMBLY` | One C-003 and one C-002 DRAFT | Validation failure → no review subject |
| `CONTRACT_ASSEMBLY` | Deterministic checks pass and manifest commits | `REVIEW_READY` | Frozen C-003, C-002, and manifest | Partial write → previous durable state |
| `REVIEW_READY` | Explicit valid human decision | `DECISION_RECORDED` | One immutable C-011 | Invalid binding → remain `REVIEW_READY` |

### 11.3. Terminal decision effects

| Decision | Effect |
|---|---|
| `ACCEPT` | Derived view marks exact C-003 and C-002 `HUMAN_ACCEPTED`; no artifact bytes are rewritten |
| `NEEDS_CHANGES` | Old subject remains closed; requested changes may seed successor revisions, but no successor starts automatically |
| `REJECT` | Old subject remains closed and unaccepted; no alternative is generated automatically |
| `DEFER` | Old subject remains closed and unaccepted; resumption requires explicit new action and successor review subject |

Derived acceptance:

```text
ACCEPTED_FIRST_FEATURE_PASSPORT =
  valid_C011.decision == ACCEPT
  AND valid_C011.actor_role == DOMAIN_EXPERT_PRODUCT_OWNER
  AND manifest_binding == VALID
  AND product_spec_binding == CURRENT
  AND feature_passport_binding == CURRENT
  AND intent_dependency_binding == VALID
```

It is a derived view, not a new authority-bearing state.

### 11.4. Cross-axis invariants

1. Workflow movement does not mutate maturity, technical result, decision, or
   permission automatically.
2. `PASS` means declared deterministic checks passed for exact bytes only.
3. `REVIEW_READY` and `HUMAN_REVIEW_REQUIRED` do not mean acceptance.
4. `ACCEPT` creates no Task Brief, execution, repository, or Git permission.
5. `BLOCKED` affects only the named operation.
6. `UNKNOWN` remains visible and blocks only its declared dependency.
7. A content change invalidates the old current binding but not historical
   evidence or decisions.

## 12. Observable outputs and derived views

### 12.1. Canonical outputs

Per cycle, before a terminal decision:

```yaml
canonical_outputs:
  C-001: EXACTLY_ONE_LOGICAL_ARTIFACT_WITH_REVISIONS
  C-003: EXACTLY_ONE_LOGICAL_ARTIFACT_WITH_REVISIONS
  C-002: EXACTLY_ONE_LOGICAL_ARTIFACT_WITH_REVISIONS
  C-011: ZERO
```

After an explicit terminal human action:

```yaml
canonical_outputs:
  C-011: EXACTLY_ONE_VALID_RECORD_FOR_EXACT_REVIEW_SUBJECT
```

### 12.2. Human-readable review view

The derived review view contains:

1. original request, visibly quoted or distinguished;
2. understood problem and desired outcome;
3. first user/JTBD and first product goal;
4. first-slice observable behavior;
5. in-scope and non-goals;
6. assumptions with status and impact;
7. unknowns with materiality and resolution path;
8. conflicts and limitations;
9. failures and recovery summary;
10. exact C-003/C-002 revision and digest;
11. decision options;
12. one next action.

The view must identify its source refs and freshness. Markdown/text rendering
owns no facts and can be rebuilt.

### 12.3. Status / Next / Details

- `Status` renders all five axes independently.
- `Next` renders exactly one currently permissible bounded action.
- `Details` exposes bindings, assumptions, unknowns, checks, failures, and
  limitations.
- None of these views may persist a decision without a separate valid C-011.

## 13. Permission model

| Requested operation | Permission |
|---|---|
| Capture explicit input into new AOS-local C-001 revision | `ALLOWED` |
| Persist valid DRAFT/HUMAN_REVIEW_REQUIRED AOS-local revisions | `ALLOWED` through accepted store boundary |
| Ask or answer clarification | `ALLOWED` |
| Render derived views | `ALLOWED` |
| Record first-slice human decision | `HUMAN_AUTHORIZATION_REQUIRED` until explicit valid human action |
| Agent-generated or inferred decision | `BLOCKED_POLICY` |
| External provider route with unresolved sensitive policy | `BLOCKED_UNKNOWN` |
| Mutate user repository | `BLOCKED_POLICY` |
| Execute user-project code or commands | `BLOCKED_POLICY` |
| Create Task Brief or implementation plan automatically | `BLOCKED_POLICY` |
| Commit, Push, Merge, or Release | `BLOCKED_POLICY` |
| No operation requested | `NOT_APPLICABLE` |

## 14. Deterministic validation rules

### 14.1. Validation order

```text
structure
→ identity and digest
→ ownership and non-duplication
→ required-field completeness
→ reference freshness
→ workflow transition
→ authority and permission
→ review-subject consistency
```

Fail-closed aggregation:

```text
CONTRACT_VIOLATION > FAIL > BLOCKED > UNKNOWN > NOT_RUN > PASS
```

This order applies only to the technical-result axis.

### 14.2. Review-ready gate

A cycle may enter `REVIEW_READY` only when:

- one current valid C-001 exists;
- one current C-003 references that C-001;
- one current C-002 references that C-003 and C-001;
- there is exactly one C-003 and one C-002 in the manifest;
- no critical unknown is open;
- all assumptions are visible;
- required acceptance and negative scenarios are present;
- all referenced digests validate;
- the manifest is durably committed;
- user-repository and Git mutation counters are zero.

A `PASS` at this gate does not create a decision.

## 15. Persistence, interruption, and recovery

### 15.1. Store requirements

- local-first, single-process structured-file store;
- immutable artifact revisions;
- append-only decision records;
- atomic replace or write-ahead journal before exposure as current;
- previous durable revision retained;
- derived Markdown/text rebuildable;
- no database or network dependency;
- exact path and serialization profile deferred.

### 15.2. Journal semantics

Logical journal states:

```yaml
journal_state:
  enum:
    - PREPARED
    - COMMITTED
    - ABORTED
    - RECOVERY_REQUIRED
```

`PREPARED` content is never current. `COMMITTED` requires artifact bytes,
digests, references, and current-pointer update to agree. Detection of an
incomplete commit changes the journal to `RECOVERY_REQUIRED`; it does not
complete the product workflow.

### 15.3. Atomic units

1. Source capture and each C-001 successor revision are atomic operations.
2. Publication of a review subject atomically exposes exact C-003, exact C-002,
   and their manifest, all referring to an already durable C-001.
3. C-011 persistence is a separate atomic append after explicit human action.
4. No transaction combines a human decision with later workflow or permission
   changes.

### 15.4. Idempotency

Each write-capable operation uses a logical idempotency key derived from:

```text
operation type
+ cycle_id
+ input subject digest
+ requested target revision
```

- exact replay returns the prior committed result without new revision;
- same key with different content returns `CONTRACT_VIOLATION`;
- retry is forbidden if scope, subject, permission, or required human decision
  changed.

### 15.5. Failure and recovery matrix

| Failure | Fail-closed result | Recovery |
|---|---|---|
| Invalid or empty input | `CLARIFICATION_REQUIRED/BLOCKED`; no C-003/C-002 | Preserve capture; request bounded clarification |
| Interruption before durable write | No new current revision | Discard uncommitted temp state or replay exact idempotent operation |
| Partial write | `RECOVERY_REQUIRED`; partial state not current | Reconcile journal; restore previous durable revision or complete exact prepared transaction |
| Corrupted artifact | `FAIL`; artifact quarantined from current view | Load last digest-valid revision and emit recovery details |
| Duplicate identical decision | Return existing C-011 | No new write |
| Conflicting duplicate decision | `CONTRACT_VIOLATION`; no new record | Require successor review subject |
| Stale subject binding | Decision invalid; remain `REVIEW_READY` | Re-render current exact subject and request new action |
| Checksum mismatch | `FAIL`; affected artifact not current/accepted | Recover valid bytes or create successor revision |
| Clarification cannot complete | `BLOCKED` until human action or valid `DEFER` | Preserve current state and one next action |
| Restart | Load only committed journal/artifact state | Reconcile pending journal before showing current |
| External agent unavailable | Core continues manually/offline | Use structured manual input |

No recovery path overwrites the last valid revision with corrupted or partial
bytes.

## 16. Acceptance criteria

| ID | Observable criterion |
|---|---|
| `AC-001` | A non-empty incomplete idea starts one cycle without requiring repository knowledge |
| `AC-002` | Empty input is blocked without fabricated artifacts |
| `AC-003` | Every critical gap is named and linked to at most one bounded question at a time; no turn contains more than three questions |
| `AC-004` | Every agent-added statement is visibly classified as assumption until human confirmation |
| `AC-005` | Review subject contains exactly one C-003 and exactly one C-002 |
| `AC-006` | C-003 owns product context and C-002 references it without duplicating product-level facts |
| `AC-007` | The review view is understandable to the domain expert without repository mechanics |
| `AC-008` | Assumptions, unknowns, non-goals, conflicts, limitations, and one next action are visible |
| `AC-009` | No `ACCEPT` exists until a valid explicit human-controlled C-011 is durably recorded |
| `AC-010` | Technical `PASS` never changes the human-decision or permission axes |
| `AC-011` | User-repository mutation and Git-action counters remain zero |
| `AC-012` | Interruption exposes either the previous durable state or a recoverable journal, never accepted partial state |
| `AC-013` | Restart resumes from committed bindings and detects stale/corrupt state |
| `AC-014` | External agent/network absence does not prevent manual core operation |

## 17. Executable negative-test contract

These cases are implementation-independent test specifications. An eventual
implementation must make them executable through its official validation
entrypoint.

| ID | Stimulus | Expected fail-closed result |
|---|---|---|
| `NT-001` | `AGENT_ADAPTER` submits `ACCEPT` | Reject C-011; `BLOCKED_POLICY`; decision remains null |
| `NT-002` | Missing required semantic field is silently filled as fact | `CONTRACT_VIOLATION`; field becomes visible `UNKNOWN` or cycle remains clarification-required |
| `NT-003` | Agent assumption is omitted from review view | `FAIL`; subject cannot enter `REVIEW_READY` |
| `NT-004` | Validator returns `PASS` and system sets `ACCEPT` | `CONTRACT_VIOLATION`; technical result remains separate and decision remains null |
| `NT-005` | Manifest contains two competing C-003 artifacts | `CONTRACT_VIOLATION`; manifest is not committed/current |
| `NT-006` | C-011 references another manifest or artifact digest | Reject decision as stale/invalid; remain `REVIEW_READY` |
| `NT-007` | Corrupted revision attempts to replace last valid current revision | `FAIL`; preserve prior current revision and create recovery evidence |
| `NT-008` | Interruption occurs after some review-subject files are written | No partial subject is current or accepted; journal becomes recoverable |
| `NT-009` | Adapter/operator is recorded as `decided_by` | Reject C-011; require `DOMAIN_EXPERT_PRODUCT_OWNER` |
| `NT-010` | Any operation writes to user repository or performs Git mutation | `BLOCKED_POLICY`; mutation count remains zero |
| `NT-011` | Same decision is captured twice with identical content | Return existing C-011 idempotently; no duplicate record |
| `NT-012` | Same idempotency key carries different bytes | `CONTRACT_VIOLATION`; no write |
| `NT-013` | Sensitive input is sent to external provider without policy | Block external route only; manual/local route remains available |
| `NT-014` | Derived Markdown view is edited and treated as canonical | Reject binding; rebuild from canonical structured artifacts |

## 18. Manual dogfood and measurement capture

First dogfood uses one facilitated local session with one low-sensitivity real
product idea.

```yaml
dogfood_requirements:
  named_domain_expert: REQUIRED
  named_facilitator_or_operator: REQUIRED
  external_provider_route:
    default: BLOCKED_UNLESS_POLICY_AND_CONSENT
  manual_or_offline_fallback: REQUIRED
  measurements:
    - time_intent_to_review_ready
    - material_clarification_loops
    - hidden_assumptions_detected
    - unresolved_material_unknowns_at_decision
    - revision_count_before_terminal_decision
    - user_comprehension
    - authority_confusion_incidents
    - operator_assistance_events
    - stale_or_invalid_binding_attempts
```

Thresholds remain `UNDECIDED` until evidence exists. One successful case
demonstrates only the slice; it does not establish stable Product Core or
justify automation.

## 19. Unknowns and deferred decisions

### 19.1. Product unknowns requiring human decision

| ID | Unknown | Blocks | Resolution |
|---|---|---|---|
| `FSPC-U01` | Acceptance of this exact Product Contract | Any implementation planning from it | `AOS_PRODUCT_OWNER` reviews exact frozen subject |
| `FSPC-U02` | Broader C-003 expansion policy beyond this slice | Broader Product Spec only | Separate product decision; no auto-expansion |
| `FSPC-U03` | Representative dogfood idea and facilitator | Dogfood only | Select one low-sensitivity real case |
| `FSPC-U04` | Dogfood success thresholds | Product success claims | Collect baseline, then decide thresholds |
| `FSPC-U05` | Provider/privacy policy | Sensitive external-agent route only | Separate human policy decision |
| `FSPC-U06` | Whether three questions per turn is optimal | Stable UX claim, not initial contract behavior | Measure clarification friction during dogfood |

The proposed value `maximum: 3` is exact behavior for this revision if
accepted. `FSPC-U06` is its future reversal question, not permission for an
implementation to choose another value.

### 19.2. Deferred architecture details

- exact filesystem paths;
- serialization and encoding profile;
- exact journal file layout;
- current-pointer representation;
- concrete human-decision capture mechanism;
- final interaction surface;
- installer/bootstrap;
- multi-user or cryptographic identity;
- broader Product Spec expansion mechanism.

These details require later scoped decisions when they block a concrete next
artifact. They do not permit implementation guesses.

### 19.3. Forbidden implementation choices at this stage

This contract does not select:

- implementation repository;
- programming language or runtime;
- framework or dependency manager;
- dependency names or versions;
- exact CLI framework or command syntax;
- serialization library;
- database;
- cloud/provider or agent vendor;
- deployment or CI/CD;
- Task Brief, Risk Profile, or Execution Authorization.

## 20. External conflict dependency

```yaml
issue_id: P2-01_CANONICAL_STATUS_AXIS_CONFLICT
classification: CONFLICT
disposition: DEFERRED_SEPARATE_CORRECTION
required_before: GLOBAL_STATUS_SCHEMA_IMPLEMENTATION
local_contract_rule:
  HUMAN_REVIEW_REQUIRED: DOCUMENT_MATURITY_ONLY
  technical_result:
    - CONTRACT_VIOLATION
    - FAIL
    - BLOCKED
    - UNKNOWN
    - NOT_RUN
    - PASS
effect_on_contract_review: NON_BLOCKING
```

This Product Contract does not modify `docs/00_Core.md` or
`docs/02_Architecture.md`. A separate human-approved canonical correction is
required before implementing a global status schema.

## 21. Explicit non-goals

- implementation code or scaffold;
- user-repository discovery or mutation;
- Task Brief compilation;
- command or code execution;
- Git automation or Git delivery;
- CI/CD, deployment, installer, or updater;
- Development Factory;
- full Control Plane or central authority registry;
- RAG or vector database;
- multi-agent orchestration or autonomous execution;
- cloud/SaaS backend;
- plugin marketplace;
- full Product Spec, roadmap, or multi-feature registry;
- acceptance of complete `FTR-001`, `FTR-003`, `FTR-008`, `FTR-012`, or
  `FTR-016` dossiers;
- architecture of the domain expert's software product.

## 22. Product Contract review rule

This proposal may be accepted only through a separate human-authored/verified
`C-011` record:

```yaml
decision_subject:
  artifact_id: FIRST_SLICE_PRODUCT_CONTRACT
  revision: R1
  sha256: REQUIRED_FROM_FROZEN_FILE
decision_actor_role: AOS_PRODUCT_OWNER
allowed_decisions:
  - ACCEPT
  - NEEDS_CHANGES
  - REJECT
  - DEFER
implementation_authorization: NONE
execution_authorization: NONE
git_authorization: NONE
```

Technical validation of structure or consistency is not product acceptance.

## 23. One next bounded action

After external file-level validation, `AOS_PRODUCT_OWNER` reviews the exact
frozen `FIRST_SLICE_PRODUCT_CONTRACT_R1.md` subject and records exactly one
decision:

```text
ACCEPT | NEEDS_CHANGES | REJECT | DEFER
```

Do not start implementation planning, choose a repository/toolchain, create a
Task Brief, execute code, or perform Git actions before that decision.
