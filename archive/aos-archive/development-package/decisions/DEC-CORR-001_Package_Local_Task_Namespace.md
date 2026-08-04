---
artifact_id: DEC-CORR-001
artifact_type: HUMAN_CONTRACT_DECISION_AND_CORRECTION_AUTHORIZATION_RECORD
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R9
status: HUMAN_DECIDED
authority: HUMAN_DECISION
exact_subject: Package-local Task namespace and bounded DRAFT-R6/DRAFT-R7/DRAFT-R8/DRAFT-R9/DRAFT-R10/DRAFT-R11/DRAFT-R12/DRAFT-R13/DRAFT-R14 documentation correction receipts
created: '2026-07-30'
gate_id: HUMAN_CORRECTION_GATE_D1
human_disposition: ACCEPT
human_decision_record:
  schema_version: aos.decision/v1
  decision_id: DEC-CORR-001
  decision_type: CONTRACT
  decision_value: USE_AOS3_DPKG_TASK_NAMESPACE
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  decision_channel: PRIMARY_CODEX_THREAD
  subject:
    kind: TASK_NAMESPACE_DECISION_WITH_SOURCE_CANDIDATE
    task_ids:
      - AOS3-DPKG-TASK-001
      - AOS3-DPKG-TASK-002
      - AOS3-DPKG-TASK-003
      - AOS3-DPKG-TASK-004
      - AOS3-DPKG-TASK-005
      - AOS3-DPKG-TASK-006
      - AOS3-DPKG-TASK-007
    source_package_revision: DRAFT-R5
    source_candidate_sha256: c21bf54b62cfe78b4c72527390c834fbe4534acca0ff730bdcde70f5b5316bed
    manifest_basis: package-relative sorted SHA-256 lines for 36 DRAFT-R5 files
  issued_at: '2026-07-30T10:28:46Z'
  grants:
    - PACKAGE_LOCAL_TASK_IDENTITY_FOR_AOS-3/development-package/tasks/
  non_grants: [ROADMAP_MUTATION, TASK_ACCEPTANCE, IMPLEMENTATION, EXECUTION, VALIDATION, COMMIT, PUSH, MERGE, RELEASE]
  expires_at: NOT_APPLICABLE
  stale_when:
    - package-local Task namespace or exact source candidate changes
    - decision value changes or the human revokes it
  consumption: NOT_APPLICABLE
candidate_binding:
  package_revision: DRAFT-R5
  aggregate_sha256: c21bf54b62cfe78b4c72527390c834fbe4534acca0ff730bdcde70f5b5316bed
  manifest_basis: package-relative sorted SHA-256 lines for 36 DRAFT-R5 files
correction_execute_authorization:
  action: AUTHORIZE_CORRECTION_EXECUTE_DRAFT_R6
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  decision_channel: PRIMARY_CODEX_THREAD
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  exact_source_candidate_sha256: c21bf54b62cfe78b4c72527390c834fbe4534acca0ff730bdcde70f5b5316bed
  allowed_root: AOS-3/development-package/
  received_at: '2026-07-30T10:37:20Z'
  grants:
    - BOUNDED_DOCUMENTATION_MUTATION_FOR_DRAFT_R6
  non_grants:
    - CANONICAL_DOCS_MUTATION
    - ROADMAP_MUTATION
    - VALIDATION
    - IMPLEMENTATION
    - COMMIT
    - PUSH
    - MERGE
    - RELEASE
  expires_at: CONSUMED_FOR_DRAFT_R6_CANDIDATE
  stale_when:
    - exact source candidate or allowed root changes
    - the human revokes or replaces the authorization
  consumption: CONSUMED_FOR_DRAFT_R6_CANDIDATE
draft_r7_correction_execute_authorization:
  action: AUTHORIZE_CORRECTION_EXECUTE_DRAFT_R7
  selected_route: RECOVER_DURABLE_C1_MANIFEST_AND_DEMATERIALIZE_TASK_003
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  decision_channel: PRIMARY_CODEX_THREAD_RESPONSE_ANNOTATION
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  authorization_text_sha256: 4295f1677a69f0e57ce8027066a4214012c27d88db74dda30206adfb87f853d1
  authorization_text_normalization: UTF-8 exact text plus LF
  exact_source_candidate_sha256: 0309143fa4d048af18c9bdfdc27acd356e927facf1f7c3add39fcece2f529efe
  allowed_root: AOS-3/development-package/
  allow_create_exact_path:
    - AOS-3/development-package/decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv
  allow_delete_exact_path:
    - AOS-3/development-package/tasks/AOS3-DPKG-TASK-003_Slice_A_Intake_to_Review.md
  allowed_changes: VAL-R6-001_FINDINGS_ONLY
  received_at: '2026-07-30T12:37:42Z'
  grants:
    - BOUNDED_DOCUMENTATION_MUTATION_FOR_DRAFT_R7
    - PERSIST_RECOVERED_C1_MANIFEST
    - DEMATERIALIZE_CURRENT_TASK_003_BRIEF
  non_grants:
    - CANONICAL_DOCS_MUTATION
    - ROADMAP_MUTATION
    - CONTRACT_ACCEPTANCE
    - TASK_ACCEPTANCE
    - INDEPENDENT_VALIDATION
    - IMPLEMENTATION
    - COMMIT
    - PUSH
    - MERGE
    - RELEASE
  expires_at: CONSUMED_FOR_DRAFT_R7_CANDIDATE
  stale_when:
    - exact source candidate or selected route changes
    - allowed create/delete paths or root change
    - the human revokes or replaces the authorization
  consumption: CONSUMED_FOR_DRAFT_R7_CANDIDATE
draft_r8_correction_execute_authorization:
  action: CORRECTION_EXECUTE_DRAFT_R8_FOR_VAL_R7_001
  human_design_disposition: ACCEPT
  selected_rules: [D1, A2]
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  decision_channel: PRIMARY_CODEX_THREAD
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  authorization_text_sha256: 7cd4332510e7b57a15120b3d75fb543f5d91b70bac37ce88446e49ff6aa278d0
  authorization_text_normalization: UTF-8 exact text plus LF
  exact_source_candidate_sha256: 6a06c761c9c722141efb4d2a900632ec4ab59ef9b921645ae028fb39d51db65b
  allowed_paths:
    - AOS-3/development-package/**/*.md
  forbidden_paths:
    - AOS-3/development-package/decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv
    - docs/**
    - AOS-3/AOS_Core_Roadmap.md
  allowed_changes: VAL-R7-001_FINDINGS_AND_APPROVED_D1_A2_DETERMINISTIC_CONSEQUENCES_ONLY
  received_at: '2026-07-30T14:01:13Z'
  grants:
    - BOUNDED_DOCUMENTATION_MUTATION_FOR_DRAFT_R8
    - D1_CLOSED_TAGGED_HUMAN_DECISION_RECORD_UNION
    - A2_WFC_ENVELOPE_ACCEPTANCE_OWNERSHIP_AND_EXACT_DERIVED_MIRRORS
  non_grants:
    - C1_ACCEPTED_SUBJECT_MANIFEST_MUTATION
    - CANONICAL_DOCS_MUTATION
    - ROADMAP_MUTATION
    - CONTRACT_ACCEPTANCE
    - TASK_ACCEPTANCE
    - INDEPENDENT_VALIDATION
    - IMPLEMENTATION
    - COMMIT
    - PUSH
    - MERGE
    - RELEASE
  expires_at: CONSUMED_FOR_DRAFT_R8_CANDIDATE
  stale_when:
    - exact source candidate, selected rules, allowed paths, or forbidden paths change
    - the human revokes or replaces the authorization
  consumption: CONSUMED_FOR_DRAFT_R8_CANDIDATE
draft_r9_correction_execute_authorization:
  action: CORRECTION_EXECUTE_DRAFT_R9_FOR_VAL_R8_001
  selected_route: Y1_REMOVE_REDUNDANT_SCALAR_AUTHORITY_KEEP_OPERATIONAL_AUTHORITY_MAP
  acceptance_projection_consequence: 126_CURRENT_11_STALE_12_NEW_DRAFT
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  decision_channel: PRIMARY_CODEX_THREAD
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  authorization_text_sha256: 207d56d68c83763a844d8abc4f64a5d58f43b472021bfe4353a27edfbc05348d
  authorization_text_normalization: UTF-8 exact text plus LF
  exact_source_candidate_sha256: f6443683a12094d1357ae8c44b5937f1aaf4f276e088b9c9c1e99b1dcfc4ac97
  allowed_paths:
    - AOS-3/development-package/**/*.md
  forbidden_paths:
    - AOS-3/development-package/decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv
    - docs/**
    - AOS-3/AOS_Core_Roadmap.md
  allowed_changes: VAL-R8-001_DUPLICATE_SCALAR_AUTHORITY_FINDING_AND_APPROVED_Y1_DETERMINISTIC_CONSEQUENCES_ONLY
  received_at: '2026-07-30T14:35:12Z'
  grants:
    - BOUNDED_DOCUMENTATION_MUTATION_FOR_DRAFT_R9
    - REMOVE_REDUNDANT_SCALAR_AUTHORITY_FROM_PSC-A-001_AND_WFC-A-001
    - KEEP_OPERATIONAL_AUTHORITY_MAPS
    - APPLY_126_CURRENT_11_STALE_12_NEW_DRAFT_PROJECTION
  non_grants:
    - C1_ACCEPTED_SUBJECT_MANIFEST_MUTATION
    - CANONICAL_DOCS_MUTATION
    - ROADMAP_MUTATION
    - CONTRACT_ACCEPTANCE
    - TASK_ACCEPTANCE
    - INDEPENDENT_VALIDATION
    - IMPLEMENTATION
    - COMMIT
    - PUSH
    - MERGE
    - RELEASE
  expires_at: CONSUMED_FOR_DRAFT_R9_CANDIDATE
  stale_when:
    - exact source candidate, selected route, allowed paths, or forbidden paths change
    - the human revokes or replaces the authorization
  consumption: CONSUMED_FOR_DRAFT_R9_CANDIDATE
draft_r10_correction_execute_authorization:
  action: CORRECTION_EXECUTE_DRAFT_R10_FOR_VAL_R9_001
  human_design_disposition: ACCEPT
  selected_route: T2_EXPLICIT_AC_PSC_TO_EXISTING_SCENARIOS_AND_REVERSE_TRACE_REPAIR
  acceptance_projection_consequence: UNCHANGED_126_CURRENT_11_STALE_12_NEW_DRAFT
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  decision_channel: PRIMARY_CODEX_THREAD
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  authorization_text_sha256: 97bad8cd023055f70ee89f733b0125d4d0efefaa9f316a9f6c32fedeab77b1c7
  authorization_text_normalization: UTF-8 exact text plus LF
  exact_source_candidate_sha256: 61ebdaa63d4fce3034db1c3fceaa3d86c35e5849cc1fc3f5bdb75e8cf3ea2bad
  allowed_paths:
    - AOS-3/development-package/**/*.md
  allowed_changes:
    - ADD_EIGHT_EXPLICIT_AC_PSC_A_001_01_THROUGH_08_TO_EXISTING_SCN_MAPPINGS
    - ADD_REVERSE_REQ_WF_004_TO_CTR_001_AND_CTR_004
    - ADD_REVERSE_REQ_WF_008_TO_CTR_002
    - RECORD_VAL_R9_001_AND_DRAFT_R10_CORRECTION_RECEIPT
    - PROPAGATE_DRAFT_R10_PACKAGE_REVISION_STATUS_AND_NEXT_ACTION_METADATA
  forbidden_changes:
    - ACCEPTED_REQUIREMENT_CONTRACT_ACCEPTANCE_OR_SCENARIO_DEFINITIONS
    - TASK_BRIEF_MATERIALIZATION_OR_TASK_DERIVATION
    - C1_ACCEPTANCE_PROJECTION
  forbidden_paths:
    - AOS-3/development-package/decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv
    - docs/**
    - AOS-3/AOS_Core_Roadmap.md
  received_at: '2026-07-30T15:37:06Z'
  grants:
    - BOUNDED_DOCUMENTATION_MUTATION_FOR_DRAFT_R10
    - DERIVED_AC_PSC_TO_EXISTING_SCENARIO_TRACE_REPAIR
    - DERIVED_REVERSE_REQUIREMENT_TO_CONTRACT_TRACE_REPAIR
    - PACKAGE_REVISION_STATUS_RECEIPT_AND_NEXT_ACTION_PROPAGATION
  non_grants:
    - C1_ACCEPTED_SUBJECT_MANIFEST_MUTATION
    - CANONICAL_DOCS_MUTATION
    - ROADMAP_MUTATION
    - ACCEPTED_SUBJECT_DEFINITION_MUTATION
    - CONTRACT_ACCEPTANCE
    - TASK_DERIVATION_OR_MATERIALIZATION
    - TASK_ACCEPTANCE
    - INDEPENDENT_VALIDATION
    - IMPLEMENTATION
    - COMMIT
    - PUSH
    - MERGE
    - RELEASE
  expires_at: CONSUMED_FOR_DRAFT_R10_CANDIDATE
  stale_when:
    - exact source candidate, selected route, allowed changes, allowed paths, or forbidden boundaries change
    - the human revokes or replaces the authorization
  consumption: CONSUMED_FOR_DRAFT_R10_CANDIDATE
draft_r11_correction_execute_authorization:
  action: CORRECTION_EXECUTE_DRAFT_R11_FOR_VAL_R10_001
  human_design_disposition: ACCEPT
  selected_route: R10_TRACE_C_ATOMIC_RELATION_REGISTRY_WITH_DERIVED_PROJECTIONS
  acceptance_projection_consequence: UNCHANGED_126_CURRENT_11_STALE_12_NEW_DRAFT
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  decision_channel: PRIMARY_CODEX_THREAD
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  authorization_text_sha256: 7c61c4747743445a096ba91836c1e3c79de326b9d56b9d56d086148fb0a13c2c
  authorization_text_normalization: UTF-8 exact text plus LF
  exact_source_candidate_sha256: 8b815b48fc6b3114e6bbaf1b8cfa3ac1cace7bb1b3119929a8f023ea2343b5b6
  source_validation_receipt:
    validation_id: VAL-R10-001
    semantic_result: FAIL
    mechanical_result: UNKNOWN
    semantic_finding: MANUAL_FORWARD_AND_REVERSE_REQUIREMENT_CONTRACT_RELATIONS_DO_NOT_ROUND_TRIP
    mechanical_limitation: YAML_DUPLICATE_KEY_A2_AND_EXACT_PROJECTION_CHECKS_NOT_COMPLETED
  relation_registry:
    registry_id: TRC-REG-001
    owner_path: AOS-3/development-package/06_Traceability_and_Readiness.md
    atomic_key: [requirement_id, contract_id]
    row_count: 81
    payload_format: requirement_id<TAB>contract_id<TAB>origin<LF>
    payload_sha256: d55e8b3603a5bf64f97ef43f9569e7aebfad51fe20f180991cb5c1026b78ba15
    projection_invariant: FORWARD_EXPANSION_EQUALS_REGISTRY_EQUALS_INVERTED_REVERSE_EXPANSION
  allowed_paths:
    - AOS-3/development-package/**/*.md
  allowed_changes:
    - MATERIALIZE_EXACT_TRC_REG_001_AND_BOTH_DERIVED_PROJECTIONS
    - ADD_DETERMINISTIC_REGISTRY_AND_PROJECTION_INVARIANTS
    - RECORD_VAL_R10_001_AND_DRAFT_R11_CORRECTION_RECEIPT
    - PROPAGATE_DRAFT_R11_PACKAGE_REVISION_STATUS_VALIDATION_HISTORY_AND_NEXT_ACTION_METADATA
  forbidden_changes:
    - REQUIREMENT_PSC_WFC_CTR_ACCEPTANCE_OR_SCENARIO_DEFINITIONS
    - C1_ACCEPTED_SUBJECT_MANIFEST_OR_ACCEPTANCE_PROJECTION
    - TASK_BRIEF_MATERIALIZATION_GRAPH_SEMANTICS_OR_TASK_DERIVATION
    - IMPLEMENTATION_REPOSITORY_ASSIGNMENT_OR_RUNTIME_CODE
  forbidden_paths:
    - AOS-3/development-package/decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv
    - docs/**
    - AOS-3/AOS_Core_Roadmap.md
  received_at: '2026-07-30T16:47:55Z'
  grants:
    - BOUNDED_DOCUMENTATION_MUTATION_FOR_DRAFT_R11
    - ATOMIC_REQUIREMENT_CONTRACT_RELATION_REGISTRY
    - DERIVED_FORWARD_AND_REVERSE_RELATION_PROJECTIONS
    - PACKAGE_REVISION_STATUS_VALIDATION_HISTORY_RECEIPT_AND_NEXT_ACTION_PROPAGATION
  non_grants:
    - C1_ACCEPTED_SUBJECT_MANIFEST_MUTATION
    - CANONICAL_DOCS_MUTATION
    - ROADMAP_MUTATION
    - ACCEPTED_SUBJECT_DEFINITION_MUTATION
    - CONTRACT_ACCEPTANCE
    - TASK_DERIVATION_OR_MATERIALIZATION
    - TASK_ACCEPTANCE
    - INDEPENDENT_VALIDATION
    - IMPLEMENTATION
    - COMMIT
    - PUSH
    - MERGE
    - RELEASE
  expires_at: CONSUMED_FOR_DRAFT_R11_CANDIDATE
  stale_when:
    - exact source candidate, selected route, registry payload, allowed changes, allowed paths, or forbidden boundaries change
    - the human revokes or replaces the authorization
  consumption: CONSUMED_FOR_DRAFT_R11_CANDIDATE
draft_r12_correction_execute_authorization:
  action: CORRECTION_EXECUTE_DRAFT_R12_FOR_VAL_R11_001
  human_design_disposition: ACCEPT
  selected_route: R11_FIX_A_ADD_THREE_RELATIONS_AND_TASK_CLOSURE_INVARIANT
  acceptance_projection_consequence: UNCHANGED_126_CURRENT_11_STALE_12_NEW_DRAFT
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  decision_channel: PRIMARY_CODEX_THREAD
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  authorization_text_sha256: f611e4693a741cf33d95daa44445a455d7693f286ca5e549a1c98fd3bb0afa04
  authorization_text_normalization: UTF-8 exact text plus LF
  exact_source_candidate_sha256: 88eefc88a9e2a1ebfe06b4be6becec9a807452e7c1ff2092eef60a0d751eb5a4
  source_validation_receipt:
    validation_id: VAL-R11-001
    overall_result: FAIL
    semantic_result: FAIL
    mechanical_result: UNKNOWN
    candidate_pre_post_identity: UNCHANGED
    semantic_finding: TASK_002_HAS_THREE_DERIVED_REQUIREMENTS_WITHOUT_A_RELATION_TO_DERIVED_CONTRACT_CTR_002
    missing_relations:
      - [REQ-CV1-009, CTR-002]
      - [REQ-WF-004, CTR-002]
      - [REQ-WF-010, CTR-002]
  relation_registry:
    registry_id: TRC-REG-001
    owner_path: AOS-3/development-package/06_Traceability_and_Readiness.md
    target_revision: R2
    atomic_key: [requirement_id, contract_id]
    row_count: 84
    payload_format: requirement_id<TAB>contract_id<TAB>origin<LF>
    payload_sha256: 87972f97bafe77c621ce01b90bfd60681dd617e3108de38a13b5ecd03d7c110c
    new_rows:
      - [REQ-CV1-009, CTR-002, SEMANTIC_COMPLETENESS_DRAFT_R12]
      - [REQ-WF-004, CTR-002, SEMANTIC_COMPLETENESS_DRAFT_R12]
      - [REQ-WF-010, CTR-002, SEMANTIC_COMPLETENESS_DRAFT_R12]
    projection_invariant: FORWARD_EXPANSION_EQUALS_REGISTRY_EQUALS_INVERTED_REVERSE_EXPANSION
    task_projection_invariant: EVERY_MATERIALIZED_TASK_REQUIREMENT_HAS_AT_LEAST_ONE_RELATION_TO_A_DERIVED_CONTRACT_AND_EVERY_DERIVED_CONTRACT_HAS_AT_LEAST_ONE_RELATION_FROM_A_DERIVED_REQUIREMENT
  allowed_paths:
    - AOS-3/development-package/**/*.md
  allowed_changes:
    - ADD_THREE_EXACT_SEMANTIC_COMPLETENESS_RELATIONS
    - UPDATE_TRC_REG_001_REVISION_ROW_COUNT_PAYLOAD_PROVENANCE_AND_ORIGIN_COUNTS
    - REGENERATE_BOTH_REQUIREMENT_CONTRACT_PROJECTIONS_ONLY_FROM_TRC_REG_001
    - ADD_MATERIALIZED_TASK_RELATION_CLOSURE_INVARIANT
    - RECORD_VAL_R11_001_AND_DRAFT_R12_CORRECTION_RECEIPT
    - PROPAGATE_DRAFT_R12_PACKAGE_REVISION_STATUS_VALIDATION_HISTORY_AND_NEXT_ACTION_METADATA
  forbidden_changes:
    - REQUIREMENT_PSC_WFC_CTR_ACCEPTANCE_OR_SCENARIO_DEFINITIONS
    - C1_ACCEPTED_SUBJECT_MANIFEST_OR_ACCEPTANCE_PROJECTION
    - TASK_BRIEF_CONTENT_DERIVATION_MATERIALIZATION_OR_GRAPH_SEMANTICS_EXCEPT_PACKAGE_METADATA
    - IMPLEMENTATION_REPOSITORY_ASSIGNMENT_OR_RUNTIME_CODE
    - INDEPENDENT_VALIDATION
    - GIT_MUTATION
  forbidden_paths:
    - AOS-3/development-package/decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv
    - docs/**
    - AOS-3/AOS_Core_Roadmap.md
  received_at: '2026-07-31T02:56:14Z'
  grants:
    - BOUNDED_DOCUMENTATION_MUTATION_FOR_DRAFT_R12
    - THREE_EXACT_SEMANTIC_COMPLETENESS_RELATIONS
    - MATERIALIZED_TASK_RELATION_CLOSURE_INVARIANT
    - PACKAGE_REVISION_STATUS_VALIDATION_HISTORY_RECEIPT_AND_NEXT_ACTION_PROPAGATION
  non_grants:
    - C1_ACCEPTED_SUBJECT_MANIFEST_MUTATION
    - CANONICAL_DOCS_MUTATION
    - ROADMAP_MUTATION
    - ACCEPTED_SUBJECT_DEFINITION_MUTATION
    - CONTRACT_ACCEPTANCE
    - TASK_CONTENT_DERIVATION_OR_MATERIALIZATION
    - TASK_ACCEPTANCE
    - INDEPENDENT_VALIDATION
    - IMPLEMENTATION
    - COMMIT
    - PUSH
    - MERGE
    - RELEASE
  expires_at: CONSUMED_FOR_DRAFT_R12_CANDIDATE
  stale_when:
    - exact source candidate, selected route, registry payload, task projection invariant, allowed changes, allowed paths, or forbidden boundaries change
    - the human revokes or replaces the authorization
  consumption: CONSUMED_FOR_DRAFT_R12_CANDIDATE
draft_r13_correction_execute_authorization:
  action: CORRECTION_EXECUTE_DRAFT_R13_FOR_VAL_R12_001
  human_design_disposition: ACCEPT
  selected_route: R12_FIX_B_DERIVE_MATERIALIZED_TASK_PROJECTIONS_FROM_TASK_BRIEF_DERIVED_FROM
  route_definition_source: PRIMARY_CODEX_THREAD_PROPOSAL_BOUND_TO_THE_SAME_SOURCE_CANDIDATE
  acceptance_projection_consequence: UNCHANGED_126_CURRENT_11_STALE_12_NEW_DRAFT
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  decision_channel: PRIMARY_CODEX_THREAD
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  authorization_text_sha256: fd57c35d16acde4746a96bea26b78dd45bf46c6488c651487d3ae39478011aff
  authorization_text_normalization: UTF-8 exact text plus LF
  exact_source_candidate_sha256: 291d3771e0b652cc152a8b706fcdeeb1479ac268c1837fd0cce721d7a11f5a8a
  source_validation_receipt:
    validation_id: VAL-R12-001
    overall_result: FAIL
    semantic_result: FAIL
    mechanical_result: UNKNOWN
    candidate_pre_post_identity: UNCHANGED
    finding: FORWARD_REQ_ARCH_003_PROJECTION_OMITS_MATERIALIZED_TASK_002_AND_ITS_EXISTING_CTR_002_ZERO_WRITE_EVIDENCE_PATH
    registry_result: TRC_REG_001_84_ROWS_AND_BOTH_REQUIREMENT_CONTRACT_PROJECTIONS_MATCH
    omitted_task_id: AOS3-DPKG-TASK-002
    requirement_id: REQ-ARCH-003
    contract_id: CTR-002
    existing_evidence_path: [AC-CTR-002-01, SCN-005]
  materialized_task_projection:
    authority: EXISTING_TASK_BRIEF_DERIVED_FROM_FIELDS
    materialized_task_ids: [AOS3-DPKG-TASK-001, AOS3-DPKG-TASK-002]
    forward_invariant: MATERIALIZED_FORWARD_TASK_PROJECTION_EQUALS_INVERTED_TASK_BRIEF_REQUIREMENTS
    reverse_invariant: MATERIALIZED_REVERSE_TASK_PROJECTION_EQUALS_TASK_BRIEF_CONTRACTS
    evidence_invariant: EVERY_MATERIALIZED_TASK_REQUIREMENT_CONTRACT_PATH_HAS_EXISTING_ACCEPTANCE_OR_SCENARIO_EVIDENCE
    graph_only_projection_authority: AOS3-DPKG-TASK-GRAPH-001
  relation_registry:
    registry_id: TRC-REG-001
    row_count: 84
    payload_sha256: 87972f97bafe77c621ce01b90bfd60681dd617e3108de38a13b5ecd03d7c110c
    mutation: FORBIDDEN
  allowed_paths:
    - AOS-3/development-package/**/*.md
  allowed_changes:
    - ADD_TASK_002_TO_REQ_ARCH_003_FORWARD_TASK_PROJECTION
    - ADD_EXISTING_AC_CTR_002_01_AND_SCN_005_ZERO_WRITE_EVIDENCE_PATH_TO_REQ_ARCH_003_PROJECTION
    - DERIVE_MATERIALIZED_FORWARD_AND_REVERSE_TASK_PROJECTIONS_FROM_EXISTING_TASK_BRIEF_DERIVED_FROM_FIELDS
    - KEEP_GRAPH_ONLY_TASK_MAPPINGS_AS_SEPARATELY_LABELLED_TASK_GRAPH_PROJECTION
    - ADD_DETERMINISTIC_MATERIALIZED_TASK_PROJECTION_AND_EVIDENCE_INVARIANTS
    - RECORD_VAL_R12_001_AND_DRAFT_R13_CORRECTION_RECEIPT
    - PROPAGATE_DRAFT_R13_PACKAGE_REVISION_STATUS_VALIDATION_HISTORY_AND_NEXT_ACTION_METADATA
  forbidden_changes:
    - TRC_REG_001_ROWS_REVISION_PAYLOAD_OR_PAYLOAD_SHA256
    - REQUIREMENT_PSC_WFC_CTR_ACCEPTANCE_SCENARIO_OR_SCHEMA_DEFINITIONS
    - TASK_BRIEF_DERIVATION_MATERIALIZATION_OUTCOME_SCOPE_OR_GRAPH_SEMANTICS_EXCEPT_PACKAGE_METADATA
    - C1_ACCEPTED_SUBJECT_MANIFEST_OR_ACCEPTANCE_PROJECTION
    - IMPLEMENTATION_REPOSITORY_ASSIGNMENT_OR_RUNTIME_CODE
    - INDEPENDENT_VALIDATION
    - GIT_MUTATION
  forbidden_paths:
    - AOS-3/development-package/decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv
    - docs/**
    - AOS-3/AOS_Core_Roadmap.md
  received_at: '2026-07-31T03:42:53Z'
  grants:
    - BOUNDED_DOCUMENTATION_MUTATION_FOR_DRAFT_R13
    - MATERIALIZED_TASK_PROJECTIONS_DERIVED_FROM_EXISTING_TASK_BRIEF_FIELDS
    - EXISTING_CTR_002_ZERO_WRITE_EVIDENCE_PATH_PROJECTION
    - PACKAGE_REVISION_STATUS_VALIDATION_HISTORY_RECEIPT_AND_NEXT_ACTION_PROPAGATION
  non_grants:
    - TRC_REG_001_MUTATION
    - C1_ACCEPTED_SUBJECT_MANIFEST_MUTATION
    - CANONICAL_DOCS_MUTATION
    - ROADMAP_MUTATION
    - ACCEPTED_SUBJECT_DEFINITION_MUTATION
    - CONTRACT_ACCEPTANCE
    - TASK_CONTENT_DERIVATION_OR_MATERIALIZATION
    - TASK_ACCEPTANCE
    - INDEPENDENT_VALIDATION
    - IMPLEMENTATION
    - COMMIT
    - PUSH
    - MERGE
    - RELEASE
  expires_at: CONSUMED_FOR_DRAFT_R13_CANDIDATE
  stale_when:
    - exact source candidate, selected route, projection authority, allowed changes, allowed paths, or forbidden boundaries change
    - the human revokes or replaces the authorization
  consumption: CONSUMED_FOR_DRAFT_R13_CANDIDATE
draft_r14_correction_execute_authorization:
  action: CORRECTION_EXECUTE_DRAFT_R14_FOR_VAL_R13_001_AND_VAL_R13_002
  human_design_disposition: ACCEPT
  selected_route: R13_FIX_A_REMOVE_UNSUPPORTED_REQ_ARCH_009_DERIVATION_AND_CLEAN_TASK_PROJECTION
  route_definition_source: PRIMARY_CODEX_THREAD_PROPOSAL_BOUND_TO_THE_SAME_SOURCE_CANDIDATE
  acceptance_projection_consequence: UNCHANGED_126_CURRENT_11_STALE_12_NEW_DRAFT
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  decision_channel: PRIMARY_CODEX_THREAD_RESPONSE_ANNOTATION
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  authorization_text_sha256: 9e857a410cbc0c710da8f51d6751a2720128d335a6c25f52d034fdf00725cda6
  authorization_text_normalization: UTF-8 exact text plus LF
  exact_source_candidate_sha256: 880dfdd3260beb19fa73078c9df50b84172ebbeec9719d62ad23b81c1407044c
  source_validation_receipts:
    - validation_id: VAL-R13-001
      overall_result: FAIL
      semantic_result: FAIL
      mechanical_result: UNKNOWN
      candidate_pre_post_identity: UNCHANGED
      finding: REQ_ARCH_009_TO_CTR_002_TO_TASK_002_LACKS_EXECUTABLE_UNKNOWN_FORMAT_REJECTION_EVIDENCE
      requirement_id: REQ-ARCH-009
      contract_id: CTR-002
      task_id: AOS3-DPKG-TASK-002
      retained_boundary_owner: DEC-ARCH-008
    - validation_id: VAL-R13-002
      overall_result: FAIL
      primary_deterministic_result: FAIL
      candidate_pre_post_identity: UNCHANGED
      finding: REQ_WF_006_FORWARD_TASK_CELL_CONTAINS_NON_DERIVED_MATERIALIZED_TASK_RANGE
      requirement_id: REQ-WF-006
      unsupported_task_ids: [AOS3-DPKG-TASK-001, AOS3-DPKG-TASK-002]
      retained_graph_only_task_id: AOS3-DPKG-TASK-004
  relation_registry:
    registry_id: TRC-REG-001
    revision: R3
    row_count: 83
    payload_sha256: af15f5e0af1ca667136e1ffc2352e3acc7bf3cb5c037f62f558818889170aa69
    removed_relation: "REQ-ARCH-009<TAB>CTR-002<TAB>REVERSE_ONLY_DRAFT_R10<LF>"
  allowed_paths:
    - AOS-3/development-package/**/*.md
  allowed_changes:
    - REMOVE_REQ_ARCH_009_AND_DEC_ARCH_008_FROM_TASK_002_DERIVED_FROM_ONLY
    - REMOVE_EXACT_REQ_ARCH_009_CTR_002_RELATION_AND_REGENERATE_BOTH_PROJECTIONS
    - RETAIN_REQ_ARCH_009_UNDER_DEC_ARCH_008_AS_DEFERRED_BOUNDARY_WITH_NO_CURRENT_CONTRACT_OR_TASK
    - REMOVE_NON_DERIVED_TASK_001_002_REFERENCE_FROM_REQ_WF_006_TASK_PROJECTION
    - RECORD_VAL_R13_001_VAL_R13_002_AND_DRAFT_R14_CORRECTION_RECEIPT
    - PROPAGATE_DRAFT_R14_PACKAGE_REVISION_STATUS_VALIDATION_HISTORY_AND_NEXT_ACTION_METADATA
  forbidden_changes:
    - REQUIREMENT_PSC_WFC_CTR_ACCEPTANCE_SCENARIO_OR_SCHEMA_DEFINITIONS
    - DEC_ARCH_008_DECISION_DEFINITION
    - C1_ACCEPTED_SUBJECT_MANIFEST_OR_ACCEPTANCE_PROJECTION
    - TASK_001_DERIVATION_OR_SUBJECT_CONTENT
    - TASK_002_OUTCOME_SCOPE_CONTRACTS_ACCEPTANCE_IDS_OR_SCENARIOS
    - TASK_GRAPH_SEMANTICS_OR_TASK_MATERIALIZATION
    - IMPLEMENTATION_REPOSITORY_ASSIGNMENT_OR_RUNTIME_CODE
    - INDEPENDENT_VALIDATION
    - GIT_MUTATION
  forbidden_paths:
    - AOS-3/development-package/decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv
    - docs/**
    - AOS-3/AOS_Core_Roadmap.md
  received_at: '2026-07-31T04:38:14Z'
  grants:
    - BOUNDED_DOCUMENTATION_MUTATION_FOR_DRAFT_R14
    - EXACT_RELATION_AND_DERIVATION_REMOVAL
    - REGENERATED_REQUIREMENT_CONTRACT_PROJECTIONS
    - PACKAGE_REVISION_STATUS_VALIDATION_HISTORY_RECEIPT_AND_NEXT_ACTION_PROPAGATION
  non_grants:
    - C1_ACCEPTED_SUBJECT_MANIFEST_MUTATION
    - CANONICAL_DOCS_MUTATION
    - ROADMAP_MUTATION
    - ACCEPTED_SUBJECT_DEFINITION_MUTATION
    - CONTRACT_ACCEPTANCE
    - TASK_ACCEPTANCE
    - TASK_GRAPH_OR_MATERIALIZATION_CHANGE
    - INDEPENDENT_VALIDATION
    - IMPLEMENTATION
    - COMMIT
    - PUSH
    - MERGE
    - RELEASE
  expires_at: CONSUMED_FOR_DRAFT_R14_CANDIDATE
  stale_when:
    - exact source candidate, selected route, relation removal, allowed changes, allowed paths, or forbidden boundaries change
    - the human revokes or replaces the authorization
  consumption: CONSUMED_FOR_DRAFT_R14_CANDIDATE
provenance:
  - USER_D1_NAMESPACE_CONFIRMATION_IN_PRIMARY_CODEX_THREAD_2026-07-30
  - USER_CORRECTION_EXECUTE_AUTHORIZATION_IN_RESPONSE_ANNOTATION_2026-07-30
  - USER_DRAFT_R7_NARROW_CORRECTION_AUTHORIZATION_IN_RESPONSE_ANNOTATION_2026-07-30
  - USER_D1_AND_A2_DESIGN_CONFIRMATIONS_IN_PRIMARY_CODEX_THREAD_2026-07-30
  - USER_DRAFT_R8_BOUNDED_CORRECTION_AUTHORIZATION_IN_PRIMARY_CODEX_THREAD_2026-07-30
  - USER_DRAFT_R9_Y1_BOUNDED_CORRECTION_AUTHORIZATION_IN_PRIMARY_CODEX_THREAD_2026-07-30
  - USER_DRAFT_R10_T2_BOUNDED_CORRECTION_AUTHORIZATION_IN_PRIMARY_CODEX_THREAD_2026-07-30
  - USER_DRAFT_R11_TRC_REG_001_BOUNDED_CORRECTION_AUTHORIZATION_IN_PRIMARY_CODEX_THREAD_2026-07-30
  - USER_DRAFT_R12_TASK_TRACE_CLOSURE_DESIGN_ACCEPTANCE_IN_PRIMARY_CODEX_THREAD_2026-07-31
  - USER_DRAFT_R12_BOUNDED_CORRECTION_AUTHORIZATION_IN_PRIMARY_CODEX_THREAD_2026-07-31
  - USER_DRAFT_R13_DERIVED_MATERIALIZED_TASK_PROJECTION_AUTHORIZATION_IN_PRIMARY_CODEX_THREAD_2026-07-31
  - USER_DRAFT_R14_ROUTE_A_DESIGN_ACCEPTANCE_IN_PRIMARY_CODEX_THREAD_2026-07-31
  - USER_DRAFT_R14_BOUNDED_CORRECTION_AUTHORIZATION_IN_RESPONSE_ANNOTATION_2026-07-31
  - ../00_Control_and_Source_Precedence.md
  - ../../AOS_Core_Roadmap.md
upstream_links:
  - ../00_Control_and_Source_Precedence.md
  - ../../AOS_Core_Roadmap.md
downstream_links:
  - C1_ACCEPTED_SUBJECT_MANIFEST.tsv
  - ../06_Traceability_and_Readiness.md
  - ../07_Implementation_Handoff.md
  - ../tasks/TASK-TEMPLATE.md
  - ../tasks/TASK-GRAPH.md
  - ../tasks/AOS3-DPKG-TASK-001_Core_Scaffold.md
  - ../tasks/AOS3-DPKG-TASK-002_Local_Bootstrap.md
limitations:
  - The Roadmap-owned TASK-### namespace and AOS-3/AOS_Core_Roadmap.md remain unchanged.
  - Materialized package-local Task candidates are documentation artifacts and are not accepted or executable Tasks.
  - AOS3-DPKG-TASK-003 remains a reserved graph-only identity after its DRAFT-R6 brief is dematerialized; corrected PSC-A-001, revised WFC-A-001, stale AC-WFC-A-001-01..07, and its schemas require a later exact contract decision.
  - This record does not assign an implementation repository.
  - Validation remains a separate read-only stage.
  - TRC-REG-001 is a DRAFT derived trace owner and cannot alter endpoint definitions, C1 acceptance, Task derivation, implementation authority, or Git authority.
  - DRAFT-R12 changed only three relation tuples, their two projections, the materialized-Task closure invariant, and package correction metadata.
  - DRAFT-R13 changes only the materialized Task projection authority/invariants, one omitted Task entry, its existing Evidence path, and package correction metadata; TRC-REG-001 and all endpoint definitions remain unchanged.
  - DRAFT-R14 removes one unsupported registry relation and its Task-002 derivation, removes one non-derived materialized Task note, regenerates both projections, and preserves REQ-ARCH-009 as a deferred DEC-ARCH-008 boundary without changing endpoint definitions.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# DEC-CORR-001 — Package-local Task Namespace

## 1. Decision

The human selected a distinct namespace for portable Task candidates owned by this package:

```yaml
namespace: AOS3-DPKG-TASK-###
owned_range:
  - AOS3-DPKG-TASK-001
  - AOS3-DPKG-TASK-002
  - AOS3-DPKG-TASK-003
  - AOS3-DPKG-TASK-004
  - AOS3-DPKG-TASK-005
  - AOS3-DPKG-TASK-006
  - AOS3-DPKG-TASK-007
owner_root: AOS-3/development-package/tasks/
roadmap_namespace: TASK-###
roadmap_owner: AOS-3/AOS_Core_Roadmap.md
namespace_collision_policy: FORBID
```

`TASK-###` in the Roadmap and `AOS3-DPKG-TASK-###` in this package are separate identities. No package artifact may claim to populate or update Roadmap `task_refs`.

## 2. Bounded correction authority

The DRAFT-R6 authorization permitted only the accepted DRAFT-R6 correction design. The DRAFT-R7 authorization permitted only recovery of the durable C1 manifest, correction of `VAL-R6-001` findings, and dematerialization of the current `AOS3-DPKG-TASK-003` brief inside `AOS-3/development-package/`. The DRAFT-R8 authorization permitted only correction of `VAL-R7-001` findings and the deterministic consequences of human-selected rules D1 and A2 within the declared Markdown paths. The DRAFT-R9 authorization permitted only the `VAL-R8-001` Y1 correction: remove the redundant scalar `authority` field from `PSC-A-001` and `WFC-A-001`, preserve each operational authority map, and project the resulting 126 current, 11 stale, and 12 new DRAFT subjects. The DRAFT-R10 authorization permitted only the `VAL-R9-001` T2 correction: add eight derived AC-PSC-to-existing-SCN mappings, restore three reverse trace links, record the exact correction receipt, and propagate package revision/status/next-action metadata without changing accepted subject definitions, Task derivation/materialization, or the C1 projection. The DRAFT-R11 authorization permitted only the `VAL-R10-001` route C correction: materialize exact `TRC-REG-001`, derive both requirement-contract projections from it, add deterministic equality invariants, record the exact receipt, and propagate package revision/status/validation-history/next-action metadata. The DRAFT-R12 authorization permitted only the `VAL-R11-001` route `R11-FIX-A`: add three exact semantic-completeness tuples, regenerate the two projections, add the materialized-Task relation-closure invariant, record the exact receipt, and propagate package revision/status/validation-history/next-action metadata. The DRAFT-R13 authorization permitted only the `VAL-R12-001` route `R12-FIX-B`: derive materialized Task projections from existing Task Brief `derived_from` fields, add the omitted `TASK-002` forward projection and its existing `AC-CTR-002-01`/`SCN-005` Evidence path, keep graph-only mappings separate, add deterministic invariants, and propagate correction metadata. The DRAFT-R14 authorization permits only route A for `VAL-R13-001` and `VAL-R13-002`: remove the unsupported `REQ-ARCH-009` Task/contract derivation and non-derived `REQ-WF-006` materialized Task note, regenerate the exact 83-row registry projections, retain compatibility as a deferred boundary, and propagate correction metadata. None of these authorizations permits:

- mutation of canonical `/docs`;
- mutation of `AOS-3/AOS_Core_Roadmap.md`;
- independent `VALIDATE`;
- Task execution or AOS implementation;
- Commit, Push, PR, Merge, or Release.

## 3. Staleness and reversal

This decision becomes stale if the package namespace, source candidate, Task identity mapping, or allowed root changes. Reusing Roadmap `TASK-###` identifiers inside this package requires a new exact human decision and reconciliation with the Roadmap owner.

```yaml
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
