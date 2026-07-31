---
artifact_id: AOS3-DPKG-TPL-RSR-001
artifact_type: TARGETED_REFERENCE_RESEARCH_TEMPLATE
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R1
status: DRAFT
authority: PROPOSAL
exact_subject: Portable schema for one narrow read-only reference research question with exact provenance
created: '2026-07-30'
provenance:
  - ../00_Control_and_Source_Precedence.md
  - ../../../docs/00_Core.md
  - ../../../docs/05_Reference.md
upstream_links:
  - ../00_Control_and_Source_Precedence.md
  - ../../../docs/05_Reference.md
downstream_links: []
limitations:
  - This template contains no reference finding.
  - Reference evidence has authority NONE and cannot select target architecture or product scope.
implementation_authorization: NONE
git_authorization: NONE
---

# Targeted Reference Research Record Template

Create a record only after a selected feature or contract exposes an exact knowledge gap.

```yaml
record:
  record_id: RSR-###
  revision: R1
  status: DRAFT
  authority: NONE
  exact_subject:
  research_question:
  created:

trigger:
  upstream_requirement_ids: []
  upstream_contract_ids: []
  gap_ids: []
  why_current_canonical_sources_are_insufficient:

source_boundary:
  repository_url:
  repository_role: READ_ONLY_REFERENCE
  ref:
  resolved_commit:
  paths: []
  allowed_evidence_types:
    - docs
    - contracts
    - tests
    - negative_fixtures
    - code
  excluded_paths: []

access:
  method:
  accessed_at:
  commit_resolution_result: NOT_RUN
  path_availability_result: NOT_RUN
  network_limitations: []

methods:
  searches: []
  files_inspected: []
  checks_run: []
  checks_not_run: []

findings:
  - finding_id: RSR-###-F###
    claim_class: OBSERVED_AT_SNAPSHOT | REPORTED | SYNTHESIZED | CONFLICT | NOT_FOUND | UNKNOWN | NOT_RUN | BLOCKED
    exact_claim:
    evidence_paths: []
    evidence_lines: []
    negative_evidence: false
    target_implication:
    authority: NONE

conflicts: []
unknowns: []
limitations: []
recommendations: []

reuse_boundary:
  copied_solution: false
  target_decision_made: false
  human_decision_required: true

authorization:
  reference_repository_mutation: NONE
  documentation_mutation: NONE
  implementation: NONE
  git:
    commit: NONE
    push: NONE
    merge: NONE
    release: NONE

result: NOT_RUN
next_required_action:
stop: true
```

## Rules

1. Resolve and record the exact commit before relying on mutable refs such as `dev`.
2. A missing or changed commit is `BLOCKED` or `NOT_FOUND`, never reconstructed from memory.
3. Classify discovered defects as negative evidence; do not copy the defective behavior.
4. Repository presence, tests, or historical PASS do not create target requirements.
5. Stop when the exact research question is answered or when scope expansion would be required.
