```yaml
manifest_id: AOS-IMPLEMENTATION-PROFILE-PIPELINE-FREEZE
revision: R2
status: FROZEN

subject_class: PROFILE_PIPELINE_CANDIDATE_PAIR
freeze_state: FROZEN

supersedes_candidate_manifest:
  path: workspace/IMPLEMENTATION_PROFILE_PIPELINE_FREEZE_MANIFEST_R1.md
  relation: SUPERSEDES_FOR_FUTURE_HUMAN_REVIEW
  prior_human_acceptance: NOT_RUN

subjects:
  profile:
    path: workspace/IMPLEMENTATION_ARTIFACT_PROFILE.md
    document_id: AOS-IMPLEMENTATION-ARTIFACT-PROFILE
    revision: R4
    sha256: 774dbc8aeda3af931e18facf7a053c14b48a1d88c63c7da2c85d095ca8f67b4a

  pipeline:
    path: workspace/IMPLEMENTATION_PLANNING_PIPELINE_R9.md
    document_id: AOS-IMPLEMENTATION-PLANNING-PIPELINE
    revision: R9
    sha256: 437918c583d4fcf5f1f5a06b374f1dc0b5c4b6a744e31fceaf4c11f858b6887a

candidate_pair_activation: ACTIVATED

human_acceptance:
  state: ACCEPTED
  decision_scope: METHOD_FREEZE_BINDING_ONLY

implementation_authorization: NONE
git_authorization: NONE
```
