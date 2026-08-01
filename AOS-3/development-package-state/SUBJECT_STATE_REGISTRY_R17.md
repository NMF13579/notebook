---
artifact_id: AOS3-SUBJECT-STATE-REGISTRY-R17
artifact_type: SUBJECT_STATE_REGISTRY
package_revision: DRAFT-R17
revision: R1
status: DRAFT
authority: ROUTING_AND_CLASSIFICATION_ONLY
active_path_registry: ../ACTIVE_SUBJECTS_R17.txt
working_baseline_revision: DRAFT-R16
latest_human_accepted_revision: DRAFT-R16
human_acceptance: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# DRAFT-R17 subject-state registry

[`ACTIVE_SUBJECTS_R17.txt`](../ACTIVE_SUBJECTS_R17.txt) является единственным
machine-readable owner current active path set. Этот registry классифицирует
R17 candidate subjects, validation support и immutable R16 acceptance Evidence;
он не принимает feature, architecture, repository, toolchain, implementation
или Git decision.

```yaml
active_subjects:
  registry: ACTIVE_SUBJECTS_R17.txt
  candidate_revision: DRAFT-R17
  normative_role: ACTIVE_NORMATIVE
  path_count: 20
  human_acceptance: NOT_RUN
  acceptance_inheritance: FORBIDDEN_FOR_NEW_OR_MODIFIED_R17_BYTES

validation_support:
  normative_role: VALIDATION_SUPPORT
  paths:
    - validation/fixtures/active_absolute_path.md
    - validation/fixtures/external_mandatory_link.md
    - validation/fixtures/modified_accepted_subject.md
    - validation/fixtures/self_authorized_task.md
    - validation/fixtures/status_axis_collision.md
    - validation/fixtures/unbound_repository_specific_task.md
    - validation/test_validate_portable_package.py

immutable_r16_acceptance_evidence:
  normative_role: HISTORICAL_ACCEPTANCE_EVIDENCE
  paths:
    - ACTIVE_SUBJECTS_R16.txt
    - development-package-state/R16_ACCEPTANCE_AND_DELIVERY.md
    - development-package-state/R16_ACCEPTANCE_AND_DELIVERY.md.sha256
    - development-package-state/R16_ACTIVE_CONTENT_MANIFEST.sha256
    - development-package-state/R16_AUTHOR_EXECUTION_REPORT.md
    - development-package-state/R16_COMPOSITE_CONTENT_MANIFEST.sha256
    - development-package-state/R16_FULL_CANDIDATE_MANIFEST.sha256
    - development-package-state/R16_FULL_CANDIDATE_PATHS.txt
    - development-package-state/SUBJECT_STATE_REGISTRY_R16.md

r17_generated_evidence:
  normative_role_partition:
    AUTHOR_EVIDENCE:
      - development-package-state/R17_AUTHOR_EXECUTION_REPORT.md
    DETACHED_MANIFEST:
      - development-package-state/R17_ACTIVE_CONTENT_MANIFEST.sha256
      - development-package-state/R17_FULL_CANDIDATE_MANIFEST.sha256
      - development-package-state/R17_FULL_CANDIDATE_PATHS.txt

composite_subject:
  path_count: 40
  role_counts:
    ACTIVE_NORMATIVE: 20
    VALIDATION_SUPPORT: 7
    HISTORICAL_ACCEPTANCE_EVIDENCE: 9
    AUTHOR_EVIDENCE: 1
    DETACHED_MANIFEST: 3
  composite_manifest: development-package-state/R17_COMPOSITE_CONTENT_MANIFEST.sha256
  composite_manifest_membership: EXCLUDED_DETACHED_IDENTITY
  r17_acceptance_sidecar_membership: FORBIDDEN_BEFORE_HUMAN_DECISION

revision_partition:
  working_baseline_revision: DRAFT-R16
  working_baseline_disposition: USE_AS_EXACT_HUMAN_ACCEPTED_BASELINE
  previous_independent_validation:
    revision: DRAFT-R16
    technical_result: PASS
  previous_human_acceptance:
    revision: DRAFT-R16
    human_decision: ACCEPT
  target_candidate_revision: DRAFT-R17
  DRAFT_R17_independent_validation: NOT_RUN
  DRAFT_R17_human_acceptance: NOT_RUN
  implementation_authorization: NONE
  git_authorization: NONE

assessment:
  technical_result: NOT_RUN
  scope_disposition: OUT_OF_SCOPE
  artifact_state: NOT_FOUND
  failure_effect: NONE_FOR_R17
```

R16-named Evidence остаётся byte-preserved и не является competing current
owner. Root payload materialization требует отдельной human authorization.
Task Brief не создаёт Execution Authorization; Commit, Push, Merge и Release
остаются отдельными permissions.
