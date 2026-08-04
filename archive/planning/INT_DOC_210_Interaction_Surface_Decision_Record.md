---
record_id: INT-DOC-210-INTERACTION-SURFACE-DECISION-001
document_type: HUMAN_PRODUCT_ARCHITECTURE_DECISION_RECORD
status: HUMAN_DECISION_RECORDED
decision_actor: HUMAN
decision: SELECT
selected_option: SURFACE-A_PROVIDER_NEUTRAL_GUIDED_CONVERSATION
recorded_at: '2026-08-02T19:26:09+05:00'
decision_source:
  class: CURRENT_EXPLICIT_HUMAN_DECISION
  locator: CODEX_CURRENT_THREAD_PREVIOUS_USER_MESSAGE
  exact_visible_utf8_text: >-
    HUMAN_DECIDE_INT_DOC_210_INTERACTION_SURFACE: SELECT
    SURFACE-A_PROVIDER_NEUTRAL_GUIDED_CONVERSATION
  utf8_byte_length: 99
  sha256: b1e937261dd9f8fa5a60d1d7239ef4cad72ac179b04a31491b43c336f11cff29
  runtime_turn_id: UNAVAILABLE_AT_RUNTIME
persistence_authorization:
  class: CURRENT_EXPLICIT_HUMAN_DECISION
  locator: CODEX_CURRENT_THREAD_CURRENT_USER_MESSAGE
  exact_visible_utf8_text: >-
    AUTHORIZE INT-DOC-210-INTERACTION-SURFACE-RECORD-001;
    decision_sha256=b1e937261dd9f8fa5a60d1d7239ef4cad72ac179b04a31491b43c336f11cff29;
    current_sha256=befb44825ffe9ad80cc74d9feaad1f6f6465b8027ddb68b359d921ed08a3af8e;
    activation_record_sha256=322fffb169cd22bba3691f387c18e0227f2c9b730793885e011986be37a4abae;
    allowed_paths=planning/INT_DOC_210_Interaction_Surface_Decision_Record.md,planning/CURRENT.md;
    operation=RECORD_HUMAN_INTERACTION_SURFACE_DECISION_AND_RECONCILE_STATE;
    execution_resume=FORBIDDEN;
    implementation=FORBIDDEN;
    git_operations=FORBIDDEN;
    one_shot=true
  utf8_byte_length: 569
  sha256: 2f8051f1b682ad33feee72d933344eaa97c6710b45a71d02eb08da3eef33a3f4
  runtime_turn_id: UNAVAILABLE_AT_RUNTIME
  operation: RECORD_HUMAN_INTERACTION_SURFACE_DECISION_AND_RECONCILE_STATE
  one_shot: true
  allowed_paths:
    - planning/INT_DOC_210_Interaction_Surface_Decision_Record.md
    - planning/CURRENT.md
interval:
  interval_id: INT-DOC-210
  interval_instance_id: INT-DOC-210-ACTIVATION-001
  activation_record:
    path: planning/INT_DOC_210_Activation_Record.md
    byte_length: 3705
    sha256: 322fffb169cd22bba3691f387c18e0227f2c9b730793885e011986be37a4abae
selected_first_slice:
  candidate_id: FS-CAND-001
  segment: NONPROGRAMMER_OR_DOMAIN_EXPERT_WITH_A_NEW_PRODUCT_IDEA
  job: TURN_AN_ORDINARY_LANGUAGE_PRODUCT_PROBLEM_INTO_A_BOUNDED_REVIEWABLE_FIRST_FEATURE_DEFINITION
  observable_outcome: VERSIONED_INTENT_RECORD_PLUS_ONE_DRAFT_FEATURE_PASSPORT_READY_FOR_HUMAN_REVIEW
  decision_record:
    path: planning/INT_DOC_200_First_Slice_Decision_Record.md
    byte_length: 5467
    sha256: 5057afd7120b3624a4d1b859cba04f7ecb6c2f204b99bd59c955550e3903e449
interaction_surface_decision:
  scope: FIRST_SLICE_LOGICAL_INTERACTION_SURFACE
  selected_surface: SURFACE-A_PROVIDER_NEUTRAL_GUIDED_CONVERSATION
  required_behavior:
    - accept the user's ordinary-language problem or incomplete idea
    - ask only material clarification questions
    - make understood, assumed and unknown claims visible for correction
    - produce the selected versioned Intent Record and one DRAFT Feature Passport
    - show exactly one next human action and stop
  provider_binding: NONE
  concrete_transport: UNDECIDED
  UI_framework: UNDECIDED
  artifact_serialization: UNDECIDED
  persistence_backend: UNDECIDED
  human_decision_authenticity_mechanism: UNDECIDED
  implementation_repository: UNASSIGNED
lifecycle_effect:
  blocked_execution_id: INT-DOC-210-EXECUTE-001
  resolved_finding_id: INT-DOC-210-EXECUTE-001-F001
  finding_disposition: RESOLVED_BY_CURRENT_EXPLICIT_HUMAN_DECISION
  execution_resume: NONE
  next_interval_activation: NONE
authority_effects:
  product_interaction_surface: HUMAN_SELECTED_IN_DECLARED_SCOPE
  architecture_topology: NONE
  dependency_selection: NONE
  implementation_repository_assignment: NONE
  implementation: NONE
  commit: NONE
  push: NONE
  merge: NONE
  release: NONE
implementation_authorization: NONE
git_authorization: NONE
next_required_action: HUMAN_AUTHORIZE_EXACT_INT_DOC_210_EXECUTION_RESUME
stop: true
---

# Interaction-surface decision record — INT-DOC-210

The human selected a provider-neutral guided conversation as the logical
interaction surface for the exact `FS-CAND-001` first slice. The selection
closes only the interaction-surface gate that blocked `INT-DOC-210-EXECUTE-001`.

The contract may require conversational clarification and review behavior, but
must not infer a provider, transport, UI framework, artifact serialization,
persistence backend, decision-authenticity mechanism, implementation repository,
language, toolchain or dependency.

This persistence authorization does not resume `EXECUTE`, create the contract
package, authorize implementation or perform any Git operation. A separate
exact execution-resume authorization is required.
