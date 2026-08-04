---
artifact_id: AOS3-SUBJECT-STATE-REGISTRY-R16
artifact_type: SUBJECT_STATE_REGISTRY
package_revision: DRAFT-R16
revision: R1
status: DRAFT
authority: ROUTING_AND_CLASSIFICATION_ONLY
active_path_registry: ../ACTIVE_SUBJECTS_R16.txt
working_baseline_revision: DRAFT-R15
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# DRAFT-R16 subject-state registry

[`ACTIVE_SUBJECTS_R16.txt`](../ACTIVE_SUBJECTS_R16.txt) является единственным
machine-readable owner current active path set. Этот registry классифицирует
новые R16 subjects и historical R15 candidate Evidence; он не принимает
feature, architecture, toolchain, implementation или Git decision.

```yaml
active_subjects:
  registry: ACTIVE_SUBJECTS_R16.txt
  candidate_revision: DRAFT-R16
  normative_role: ACTIVE
  human_acceptance: NOT_RUN
  acceptance_inheritance: FORBIDDEN_FOR_NEW_OR_MODIFIED_R16_BYTES

root_payload_subjects:
  - path: ROOT_FILES_MANIFEST.yaml
    normative_role: ACTIVE
    subject_role: ROOT_PAYLOAD_COPY_CONTRACT
  - path: root/AGENTS.md
    normative_role: ACTIVE
    subject_role: REPOSITORY_AGENT_ROUTER
  - path: root/README.md
    normative_role: ACTIVE
    subject_role: HUMAN_ENTRYPOINT
  - path: root/.gitignore
    normative_role: ACTIVE
    subject_role: MINIMAL_SHARED_IGNORE_BASE
  - path: root/.agents/rules/aos.md
    normative_role: ACTIVE
    subject_role: ANTIGRAVITY_WORKSPACE_RULE

r15_historical_candidate_evidence:
  - path: ACTIVE_SUBJECTS_R15.txt
    normative_role: HISTORICAL_EVIDENCE
  - path: development-package-state/R15_ACTIVE_CONTENT_MANIFEST.sha256
    normative_role: HISTORICAL_EVIDENCE
  - path: development-package-state/R15_AUTHOR_EXECUTION_REPORT.md
    normative_role: HISTORICAL_EVIDENCE
  - path: development-package-state/SUBJECT_STATE_REGISTRY_R15.md
    normative_role: HISTORICAL_EVIDENCE

r16_generated_evidence:
  - path: development-package-state/R16_ACTIVE_CONTENT_MANIFEST.sha256
    normative_role: HISTORICAL_EVIDENCE
  - path: development-package-state/R16_AUTHOR_EXECUTION_REPORT.md
    normative_role: HISTORICAL_EVIDENCE
  - path: development-package-state/R16_FULL_CANDIDATE_PATHS.txt
    normative_role: HISTORICAL_EVIDENCE
  - path: development-package-state/R16_FULL_CANDIDATE_MANIFEST.sha256
    normative_role: HISTORICAL_EVIDENCE

validation_support:
  - path: validation/test_validate_portable_package.py
    normative_role: NON_NORMATIVE_EXAMPLE
  - path: validation/fixtures/**
    normative_role: NON_NORMATIVE_EXAMPLE

carried_forward_non_active_classification:
  source_snapshot: development-package-state/SUBJECT_STATE_REGISTRY_R15.md
  scope: EXACT_UNCHANGED_NON_ACTIVE_PATHS_ONLY
  r16_owner: development-package-state/SUBJECT_STATE_REGISTRY_R16.md
  source_current_state_ownership: FORBIDDEN
  authority_effect: NONE

revision_partition:
  working_baseline_revision: DRAFT-R15
  working_baseline_disposition: USE_AS_EXACT_WORKING_BASELINE
  previous_independent_validation:
    revision: DRAFT-R15
    technical_result: PASS
  target_candidate_revision: DRAFT-R16
  DRAFT_R16_independent_validation: NOT_RUN
  DRAFT_R16_human_acceptance: NOT_RUN
  implementation_authorization: NONE
  git_authorization: NONE
```

R15-named registry, manifest и report остаются byte-preserved historical
Evidence. Они не являются competing current-state owners и не придают R16
acceptance. Root payload materialization требует отдельной authorization и не
заменяет full target repository preflight.
