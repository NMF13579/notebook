---
artifact_id: AOS3-SUBJECT-STATE-REGISTRY-R15
artifact_type: SUBJECT_STATE_REGISTRY
package_revision: DRAFT-R15
revision: R1
status: DRAFT
authority: ROUTING_AND_CLASSIFICATION_ONLY
active_path_registry: ../ACTIVE_SUBJECTS_R15.txt
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# DRAFT-R15 subject-state registry

`ACTIVE_SUBJECTS_R15.txt` is the machine-readable active path owner. This
document classifies non-active files and subject-level dependencies. It does
not accept or reject a subject.

```yaml
normative_role:
  enum:
    - ACTIVE
    - SUPERSEDED
    - HISTORICAL_EVIDENCE
    - NON_NORMATIVE_EXAMPLE
    - DRAFT_TEMPLATE
```

## Active operational subjects

Every path in [`ACTIVE_SUBJECTS_R15.txt`](../ACTIVE_SUBJECTS_R15.txt) has:

```yaml
normative_role: ACTIVE
candidate_revision: DRAFT-R15
human_acceptance: NOT_RUN
acceptance_inheritance: FORBIDDEN_FOR_NEW_OR_MODIFIED_R15_BYTES
```

The manifest and author report are deliberately excluded from the active
digest. Tests and negative fixtures are not normative package content.

## Non-active file subjects

Each entry is explicit. `active_inbound_references` refers only to normative
operational references; an explicitly labelled historical-provenance link does
not activate a subject.

```yaml
non_active_subjects:
  - subject_id: AOS3-ROOT-ROADMAP-R14
    path: AOS_Core_Roadmap.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: PRE_R15_DRAFT_WORKSPACE_CONTEXT_NOT_REQUIRED_FOR_PORTABLE_BOOTSTRAP
  - subject_id: AOS3-ROOT-DESIGN-CHECKLIST-R14
    path: AOS_Design_Checklist.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: PRE_R15_NON_OWNER_CHECKLIST
  - subject_id: AOS3-ROOT-QUESTIONS-R14
    path: AOS_Questions_The_System_Should_Answer.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: PRE_R15_NON_OWNER_QUESTION_SET
  - subject_id: AOS3-DPKG-STATE-R14-001
    path: development-package-state/R14_ACCEPTANCE_AND_DELIVERY.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: true
    reason: IMMUTABLE_ACCEPTANCE_SIDECAR_FOR_EXACT_R14_AGGREGATE_ONLY
  - subject_id: AOS3-DPKG-R15-MANIFEST
    path: development-package-state/R15_ACTIVE_CONTENT_MANIFEST.sha256
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: NON_RECURSIVE_CANDIDATE_IDENTITY_OUTPUT_EXCLUDED_FROM_ITS_OWN_DIGEST
  - subject_id: AOS3-DPKG-R15-AUTHOR-REPORT
    path: development-package-state/R15_AUTHOR_EXECUTION_REPORT.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: AUTHOR_SELF_CHECK_EVIDENCE_WITH_NO_INDEPENDENCE_OR_ACCEPTANCE_EFFECT
  - subject_id: AOS3-DPKG-DOC-001-R14
    path: development-package/01_Product_and_Core_V1_Scope.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: R14_SCOPED_BASELINE_RETAINED_FOR_PROVENANCE_NOT_ACTIVE_BOOTSTRAP
  - subject_id: AOS3-DPKG-DOC-002-R14
    path: development-package/02_User_Journeys_and_Workflows.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: R14_SCOPED_BASELINE_RETAINED_FOR_PROVENANCE_NOT_ACTIVE_BOOTSTRAP
  - subject_id: AOS3-DPKG-DOC-003-R14
    path: development-package/03_Architecture_and_Decisions.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: R14_SCOPED_BASELINE_RETAINED_FOR_PROVENANCE_NOT_ACTIVE_BOOTSTRAP
  - subject_id: AOS3-DPKG-DOC-004-R14
    path: development-package/04_Runtime_and_Data_Contracts.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: R14_SCOPED_BASELINE_RETAINED_FOR_PROVENANCE_NOT_ACTIVE_BOOTSTRAP
  - subject_id: AOS3-DPKG-DOC-005-R14
    path: development-package/05_Quality_Recovery_and_Security.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: R14_SCOPED_BASELINE_RETAINED_FOR_PROVENANCE_NOT_ACTIVE_BOOTSTRAP
  - subject_id: AOS3-DPKG-DOC-006-R14
    path: development-package/06_Traceability_and_Readiness.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: development-package-state/SUBJECT_STATE_REGISTRY_R15.md
    active_inbound_references: false
    reason: R14_TRACEABILITY_SNAPSHOT_WITH_STALE_LIFECYCLE_AND_BLK_006_STATE
  - subject_id: AOS3-DPKG-ADAPTER-CODEX-R14
    path: development-package/adapters/CODEX.md
    normative_role: SUPERSEDED
    superseded_by: AGENTS.md
    active_inbound_references: false
    reason: SOURCE_BOUND_ADAPTER_NOT_REQUIRED_BY_PORTABLE_R15_ROUTE
  - subject_id: AOS3-C1-SUBJECT-MANIFEST-001
    path: development-package/decisions/C1_ACCEPTED_SUBJECT_MANIFEST.tsv
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: BYTE_BOUND_C1_ACCEPTANCE_WITNESS_RETAINED_UNCHANGED
  - subject_id: DEC-ARCH-001
    path: development-package/decisions/DEC-ARCH-001_Implementation_Repository.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-ARCH-002
    path: development-package/decisions/DEC-ARCH-002_Architecture_and_Topology.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-ARCH-003
    path: development-package/decisions/DEC-ARCH-003_Toolchain_and_Dependencies.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-ARCH-004
    path: development-package/decisions/DEC-ARCH-004_Project_Memory.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-ARCH-005
    path: development-package/decisions/DEC-ARCH-005_Provider_and_Privacy.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-ARCH-006
    path: development-package/decisions/DEC-ARCH-006_Human_Decision_Authenticity.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-ARCH-007
    path: development-package/decisions/DEC-ARCH-007_Risk_Profile_Vocabulary.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-ARCH-008
    path: development-package/decisions/DEC-ARCH-008_Compatibility.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-CONTRACT-001
    path: development-package/decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_C1_ACCEPTANCE_OWNER_FOR_BOUND_R4_SUBJECTS_ONLY
  - subject_id: DEC-CORR-001
    path: development-package/decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: HISTORICAL_R6_TO_R14_CORRECTION_RECEIPTS_WITH_CONSUMED_AUTHORIZATIONS
  - subject_id: DEC-PROD-001
    path: development-package/decisions/DEC-PROD-001_First_User_and_Job.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-PROD-002
    path: development-package/decisions/DEC-PROD-002_Observable_Outcome.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-PROD-003
    path: development-package/decisions/DEC-PROD-003_Core_V1_Slice_Sequence.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-PROD-004
    path: development-package/decisions/DEC-PROD-004_Core_V1_Scope_and_Non_Goals.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-PROD-005
    path: development-package/decisions/DEC-PROD-005_Product_Spec_and_Feature_Passport_Relation.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: DEC-PROD-006
    path: development-package/decisions/DEC-PROD-006_RMP_004_005_Boundaries.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: EXACT_HISTORICAL_DECISION_SCOPE_RETAINED_WITHOUT_R15_ACCEPTANCE_INHERITANCE
  - subject_id: AOS3-DPKG-TPL-DEC-R14
    path: development-package/decisions/DECISION-RECORD-TEMPLATE.md
    normative_role: SUPERSEDED
    superseded_by: templates/FIRST_VERTICAL_SLICE_SELECTION.template.md
    active_inbound_references: false
    reason: GENERIC_R14_TEMPLATE_REPLACED_BY_EXACT_R15_HUMAN_GATE_TEMPLATES
  - subject_id: AOS3-DPKG-G2-OPTION-R14
    path: development-package/decisions/G2_ARCHITECTURE_OPTION_PACKAGE.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: HISTORICAL_OPTION_PACKAGE_WITH_NO_CURRENT_BOOTSTRAP_ROLE
  - subject_id: AOS3-DPKG-TPL-RSR-R14
    path: development-package/research/RESEARCH-RECORD-TEMPLATE.md
    normative_role: SUPERSEDED
    superseded_by: NONE
    active_inbound_references: false
    reason: RESEARCH_TEMPLATE_NOT_REQUIRED_FOR_R15_PORTABLE_BOOTSTRAP
  - subject_id: RSR-001
    path: development-package/research/RSR-001_AgentOS_Interview_and_Product_Spec.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: PINNED_REFERENCE_EVIDENCE_AUTHORITY_NONE
  - subject_id: RSR-002
    path: development-package/research/RSR-002_AOS_FARM_Decision_and_Recovery_Boundaries.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: PINNED_REFERENCE_EVIDENCE_AUTHORITY_NONE
  - subject_id: RSR-003
    path: development-package/research/RSR-003_AgentOS_Task_Authorization_and_Handoff.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: PINNED_REFERENCE_EVIDENCE_AUTHORITY_NONE
  - subject_id: RSR-004
    path: development-package/research/RSR-004_AOS_FARM_Candidate_Validation_and_Recovery.md
    normative_role: HISTORICAL_EVIDENCE
    superseded_by: NONE
    active_inbound_references: false
    reason: PINNED_REFERENCE_EVIDENCE_AUTHORITY_NONE
  - subject_id: AOS3-DPKG-TASK-TEMPLATE-R14
    path: development-package/tasks/TASK-TEMPLATE.md
    normative_role: SUPERSEDED
    superseded_by: templates/PORTABLE_TASK_CANDIDATE.template.md
    active_inbound_references: false
    reason: R14_TEMPLATE_REPLACED_BY_SEPARATE_PORTABLE_AND_TARGET_BOUND_R15_TEMPLATES
  - subject_id: AOS3-DPKG-TASK-GRAPH-R14
    path: development-package/tasks/TASK-GRAPH.md
    normative_role: SUPERSEDED
    superseded_by: development-package/07_Implementation_Handoff.md
    active_inbound_references: false
    reason: EAGER_SEVEN_NODE_GRAPH_REPLACED_BY_LAZY_DECOMPOSITION
  - subject_id: AOS3-DPKG-TASK-001-R14
    path: development-package/tasks/AOS3-DPKG-TASK-001_Core_Scaffold.md
    normative_role: SUPERSEDED
    superseded_by: templates/PORTABLE_TASK_CANDIDATE.template.md
    active_inbound_references: false
    reason: UNACCEPTED_UNBOUND_R14_CANDIDATE_NOT_EXECUTABLE_IN_R15
  - subject_id: AOS3-DPKG-TASK-002-R14
    path: development-package/tasks/AOS3-DPKG-TASK-002_Local_Bootstrap.md
    normative_role: SUPERSEDED
    superseded_by: templates/PORTABLE_TASK_CANDIDATE.template.md
    active_inbound_references: false
    reason: UNACCEPTED_UNBOUND_R14_CANDIDATE_NOT_EXECUTABLE_IN_R15
  - subject_id: AOS3-R15-VALIDATOR-TESTS
    path: validation/test_validate_portable_package.py
    normative_role: NON_NORMATIVE_EXAMPLE
    superseded_by: NONE
    active_inbound_references: false
    reason: AUTHOR_TEST_HARNESS_EXCLUDED_FROM_ACTIVE_DIGEST
  - subject_id: R15-NEG-STATUS-AXIS-COLLISION
    path: validation/fixtures/status_axis_collision.md
    normative_role: NON_NORMATIVE_EXAMPLE
    superseded_by: NONE
    active_inbound_references: false
    reason: DELIBERATELY_INVALID_AUTHOR_FIXTURE
  - subject_id: R15-NEG-EXTERNAL-MANDATORY-LINK
    path: validation/fixtures/external_mandatory_link.md
    normative_role: NON_NORMATIVE_EXAMPLE
    superseded_by: NONE
    active_inbound_references: false
    reason: DELIBERATELY_INVALID_AUTHOR_FIXTURE
  - subject_id: R15-NEG-ACTIVE-ABSOLUTE-PATH
    path: validation/fixtures/active_absolute_path.md
    normative_role: NON_NORMATIVE_EXAMPLE
    superseded_by: NONE
    active_inbound_references: false
    reason: DELIBERATELY_INVALID_AUTHOR_FIXTURE
  - subject_id: R15-NEG-SELF-AUTHORIZED-TASK
    path: validation/fixtures/self_authorized_task.md
    normative_role: NON_NORMATIVE_EXAMPLE
    superseded_by: NONE
    active_inbound_references: false
    reason: DELIBERATELY_INVALID_AUTHOR_FIXTURE
  - subject_id: R15-NEG-UNBOUND-REPOSITORY-SPECIFIC-TASK
    path: validation/fixtures/unbound_repository_specific_task.md
    normative_role: NON_NORMATIVE_EXAMPLE
    superseded_by: NONE
    active_inbound_references: false
    reason: DELIBERATELY_INVALID_AUTHOR_FIXTURE
  - subject_id: R15-NEG-MODIFIED-ACCEPTED-SUBJECT
    path: validation/fixtures/modified_accepted_subject.md
    normative_role: NON_NORMATIVE_EXAMPLE
    superseded_by: NONE
    active_inbound_references: false
    reason: DELIBERATELY_INVALID_AUTHOR_FIXTURE
```

## Stale and new subject disposition

Every row has the required registry fields. `CONDITIONAL` means that a human
feature selection must first make the subject relevant.

| subject_id | path | previous_state | r15_state | authority_owner | required_for_portable_bootstrap | required_for_feature_contract | required_for_task_ids | human_decision_required | blocking_scope | normative_role |
|---|---|---|---|---|---|---|---|---|---|---|
| `PSC-A-001` | `development-package/01_Product_and_Core_V1_Scope.md` | `C1_ACCEPTED_EXACT_R4_THEN_STALE` | `HISTORICAL_ACCEPTED_REFERENCE_STALE` | `DEC-CONTRACT-001` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-003` | `true` | `DEPENDENT_FEATURE_CONTRACT_AND_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `WFC-A-001` | `development-package/02_User_Journeys_and_Workflows.md` | `C1_ACCEPTED_EXACT_R4_THEN_STALE` | `HISTORICAL_ACCEPTED_REFERENCE_STALE` | `DEC-CONTRACT-001` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-003` | `true` | `DEPENDENT_FEATURE_CONTRACT_AND_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `WFC-B-001` | `development-package/02_User_Journeys_and_Workflows.md` | `C1_ACCEPTED_EXACT_R4_THEN_STALE` | `HISTORICAL_ACCEPTED_REFERENCE_STALE` | `DEC-CONTRACT-001` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-004` | `true` | `DEPENDENT_FEATURE_CONTRACT_AND_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `WFC-C-001` | `development-package/02_User_Journeys_and_Workflows.md` | `C1_ACCEPTED_EXACT_R4_THEN_STALE` | `HISTORICAL_ACCEPTED_REFERENCE_STALE` | `DEC-CONTRACT-001` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-007` | `true` | `DEPENDENT_FEATURE_CONTRACT_AND_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-A-001-01` | `development-package/02_User_Journeys_and_Workflows.md` | `C1_ACCEPTED_EXACT_R4_THEN_STALE` | `HISTORICAL_ACCEPTED_REFERENCE_STALE` | `DEC-CONTRACT-001` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-003` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-A-001-02` | `development-package/02_User_Journeys_and_Workflows.md` | `C1_ACCEPTED_EXACT_R4_THEN_STALE` | `HISTORICAL_ACCEPTED_REFERENCE_STALE` | `DEC-CONTRACT-001` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-003` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-A-001-03` | `development-package/02_User_Journeys_and_Workflows.md` | `C1_ACCEPTED_EXACT_R4_THEN_STALE` | `HISTORICAL_ACCEPTED_REFERENCE_STALE` | `DEC-CONTRACT-001` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-003` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-A-001-04` | `development-package/02_User_Journeys_and_Workflows.md` | `C1_ACCEPTED_EXACT_R4_THEN_STALE` | `HISTORICAL_ACCEPTED_REFERENCE_STALE` | `DEC-CONTRACT-001` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-003` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-A-001-05` | `development-package/02_User_Journeys_and_Workflows.md` | `C1_ACCEPTED_EXACT_R4_THEN_STALE` | `HISTORICAL_ACCEPTED_REFERENCE_STALE` | `DEC-CONTRACT-001` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-003` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-A-001-06` | `development-package/02_User_Journeys_and_Workflows.md` | `C1_ACCEPTED_EXACT_R4_THEN_STALE` | `HISTORICAL_ACCEPTED_REFERENCE_STALE` | `DEC-CONTRACT-001` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-003` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-A-001-07` | `development-package/02_User_Journeys_and_Workflows.md` | `C1_ACCEPTED_EXACT_R4_THEN_STALE` | `HISTORICAL_ACCEPTED_REFERENCE_STALE` | `DEC-CONTRACT-001` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-003` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-B-001-01` | `development-package/02_User_Journeys_and_Workflows.md` | `NEW_DRAFT_R14` | `HISTORICAL_DRAFT_REFERENCE` | `DEC-CONTRACT-001_NON_ACCEPTANCE_BOUNDARY` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-004` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-B-001-02` | `development-package/02_User_Journeys_and_Workflows.md` | `NEW_DRAFT_R14` | `HISTORICAL_DRAFT_REFERENCE` | `DEC-CONTRACT-001_NON_ACCEPTANCE_BOUNDARY` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-004` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-B-001-03` | `development-package/02_User_Journeys_and_Workflows.md` | `NEW_DRAFT_R14` | `HISTORICAL_DRAFT_REFERENCE` | `DEC-CONTRACT-001_NON_ACCEPTANCE_BOUNDARY` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-004` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-B-001-04` | `development-package/02_User_Journeys_and_Workflows.md` | `NEW_DRAFT_R14` | `HISTORICAL_DRAFT_REFERENCE` | `DEC-CONTRACT-001_NON_ACCEPTANCE_BOUNDARY` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-004` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-B-001-05` | `development-package/02_User_Journeys_and_Workflows.md` | `NEW_DRAFT_R14` | `HISTORICAL_DRAFT_REFERENCE` | `DEC-CONTRACT-001_NON_ACCEPTANCE_BOUNDARY` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-004` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-C-001-01` | `development-package/02_User_Journeys_and_Workflows.md` | `NEW_DRAFT_R14` | `HISTORICAL_DRAFT_REFERENCE` | `DEC-CONTRACT-001_NON_ACCEPTANCE_BOUNDARY` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-007` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-C-001-02` | `development-package/02_User_Journeys_and_Workflows.md` | `NEW_DRAFT_R14` | `HISTORICAL_DRAFT_REFERENCE` | `DEC-CONTRACT-001_NON_ACCEPTANCE_BOUNDARY` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-007` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-C-001-03` | `development-package/02_User_Journeys_and_Workflows.md` | `NEW_DRAFT_R14` | `HISTORICAL_DRAFT_REFERENCE` | `DEC-CONTRACT-001_NON_ACCEPTANCE_BOUNDARY` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-007` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-C-001-04` | `development-package/02_User_Journeys_and_Workflows.md` | `NEW_DRAFT_R14` | `HISTORICAL_DRAFT_REFERENCE` | `DEC-CONTRACT-001_NON_ACCEPTANCE_BOUNDARY` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-007` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `AC-WFC-C-001-05` | `development-package/02_User_Journeys_and_Workflows.md` | `NEW_DRAFT_R14` | `HISTORICAL_DRAFT_REFERENCE` | `DEC-CONTRACT-001_NON_ACCEPTANCE_BOUNDARY` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-007` | `true` | `DEPENDENT_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `SCH-PRODUCT-SPEC-001` | `development-package/04_Runtime_and_Data_Contracts.md` | `NEW_DRAFT_R14` | `HISTORICAL_DRAFT_REFERENCE` | `DEC-CONTRACT-001_NON_ACCEPTANCE_BOUNDARY` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-003` | `true` | `DEPENDENT_FEATURE_CONTRACT_AND_TASK_ONLY` | `HISTORICAL_EVIDENCE` |
| `SCH-FEATURE-PASSPORT-001` | `development-package/04_Runtime_and_Data_Contracts.md` | `NEW_DRAFT_R14` | `HISTORICAL_DRAFT_REFERENCE` | `DEC-CONTRACT-001_NON_ACCEPTANCE_BOUNDARY` | `false` | `CONDITIONAL` | `AOS3-DPKG-TASK-003` | `true` | `DEPENDENT_FEATURE_CONTRACT_AND_TASK_ONLY` | `HISTORICAL_EVIDENCE` |

None of these subjects blocks package portability or target preflight.

## Existing Task disposition

| Task subject | task_candidate_role | dependency_state | executable | reason |
|---|---|---|---|---|
| `development-package/tasks/TASK-TEMPLATE.md` | `SUPERSEDED_REFERENCE` | `NOT_APPLICABLE` | `false` | Replaced by split R15 templates |
| `development-package/tasks/TASK-GRAPH.md` | `SUPERSEDED_REFERENCE` | `HUMAN_DECISION_REQUIRED` | `false` | Eager graph replaced by lazy decomposition |
| `AOS3-DPKG-TASK-001` | `SUPERSEDED_REFERENCE` | `CURRENT_ACCEPTED` | `false` | Unaccepted R14 portable candidate; no target binding |
| `AOS3-DPKG-TASK-002` | `SUPERSEDED_REFERENCE` | `CURRENT_ACCEPTED` | `false` | Unaccepted R14 portable candidate; no target binding |
| `AOS3-DPKG-TASK-003` | `SUPERSEDED_REFERENCE` | `HUMAN_DECISION_REQUIRED` | `false` | Stale/new upstream subjects |
| `AOS3-DPKG-TASK-004` | `SUPERSEDED_REFERENCE` | `HUMAN_DECISION_REQUIRED` | `false` | Stale/new upstream subjects |
| `AOS3-DPKG-TASK-005` | `SUPERSEDED_REFERENCE` | `TARGET_BINDING_REQUIRED` | `false` | Graph-only identity with no Task Brief |
| `AOS3-DPKG-TASK-006` | `SUPERSEDED_REFERENCE` | `TARGET_BINDING_REQUIRED` | `false` | Graph-only identity with no Task Brief |
| `AOS3-DPKG-TASK-007` | `SUPERSEDED_REFERENCE` | `HUMAN_DECISION_REQUIRED` | `false` | Stale/new upstream subjects |

## `BLK-006` disposition

Confirmed status owner for the active R15 package is the exact current human
prompt, consistent with the accepted `docs/00_Core.md` fact-class owner:

```yaml
technical_result:
  enum:
    - CONTRACT_VIOLATION
    - FAIL
    - BLOCKED
    - UNKNOWN
    - NOT_RUN
    - PASS
    - HUMAN_REVIEW_REQUIRED
human_decision:
  enum:
    - ACCEPT
    - NEEDS_CHANGES
    - REJECT
    - DEFER
feature_disposition:
  enum:
    - REQUIRED
    - OPTIONAL
    - DEFERRED
    - REFERENCE_ONLY
    - REJECTED
    - UNDECIDED
readiness_state:
  enum:
    - READY
    - NOT_READY
    - BLOCKED_BY_HUMAN_GATE
    - NOT_APPLICABLE
authorization_state:
  enum:
    - NONE
    - GRANTED
    - CONSUMED
    - EXPIRED
```

```yaml
blocker: BLK-006_CANONICAL_STATUS_AXIS_CONFLICT
disposition: RESOLVED_FOR_ACTIVE_DRAFT_R15_PACKAGE_SCOPE
canonical_docs_correction: NOT_RUN
historical_r14_definition_role: HISTORICAL_EVIDENCE
active_competing_enum: NONE
independent_validation_effect: NONE
human_acceptance_effect: NONE
```

This disposition does not rewrite canonical files outside `AOS-3/` and does
not claim that historical R14 subjects conform to the R15 active axes.
