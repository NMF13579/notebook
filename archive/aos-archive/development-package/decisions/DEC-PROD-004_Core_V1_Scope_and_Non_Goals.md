---
artifact_id: DEC-PROD-004
artifact_type: HUMAN_PRODUCT_DECISION_RECORD
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R3
status: HUMAN_DECIDED
authority: HUMAN_DECISION
exact_subject: Core v1 product scope and non-goals for the accepted A to B to C sequence
created: '2026-07-30'
gate_id: HUMAN_PRODUCT_GATE_G1
human_disposition: ACCEPT
human_decision_record:
  schema_version: aos.decision/v1
  decision_id: DEC-PROD-004
  decision_type: PRODUCT
  decision_value: ACCEPT
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  decision_channel: PRIMARY_CODEX_THREAD
  subject:
    kind: PACKAGE_CANDIDATE
    package_id: AOS3-DEVELOPMENT-PACKAGE
    package_revision: DRAFT-R1
    candidate_scope: STAGE_A_G1_DECISION_PACKAGE
    aggregate_sha256: 4fe1a0fcc8493d00e60694f86ac734fac197f005246b6ae7cb2689ab6fd9ce80
    manifest_basis: package-relative sorted SHA-256 lines for 3 DRAFT-R1 files
  issued_at: '2026-07-30T10:28:46Z'
  grants: [PRODUCT_DECISION_FOR_EXACT_SUBJECT]
  non_grants: [DOCUMENTATION_MUTATION, IMPLEMENTATION, EXECUTION, COMMIT, PUSH, MERGE, RELEASE]
  expires_at: NOT_APPLICABLE
  stale_when:
    - exact subject revision or hash changes
    - decision value changes or the human revokes it
  consumption: NOT_APPLICABLE
candidate_binding:
  package_revision: DRAFT-R1
  aggregate_sha256: 4fe1a0fcc8493d00e60694f86ac734fac197f005246b6ae7cb2689ab6fd9ce80
  manifest_basis: package-relative sorted SHA-256 lines for 3 DRAFT-R1 files
provenance:
  - ../00_Control_and_Source_Precedence.md
  - ../../../docs/00_Core.md
  - ../../../docs/01_Product.md
  - CURRENT_USER_CONFIRMATION_2026-07-30
upstream_links:
  - ../00_Control_and_Source_Precedence.md
  - ../../../docs/00_Core.md
  - ../../../docs/01_Product.md
downstream_links:
  - ../01_Product_and_Core_V1_Scope.md
  - ../02_User_Journeys_and_Workflows.md
limitations:
  - This decision accepts a product boundary, not item-level FTR dispositions.
  - Advanced capabilities remain deferred even when they could support a selected slice.
implementation_authorization: NONE
git_authorization: NONE
---

# DEC-PROD-004 — Core v1 Scope and Non-goals

## In scope

```yaml
in_scope:
  - intent intake with original-input preservation
  - material clarification
  - DRAFT Product Spec and feature-specific Feature Passport
  - explicit human review stop
  - later compilation of accepted contracts into one bounded Task Brief
  - later read-only recovery of actual project state and one safe next action
  - visible assumptions, unknowns, scope, authority, Evidence state, and non-goals
```

## Non-goals

```yaml
non_goals:
  - implementation in the knowledge repository
  - automatic architecture, repository, dependency, Risk Profile, or provider selection
  - automatic Task activation or execution
  - autonomous recovery, remediation, retry, or self-heal
  - full backlog scheduling or Control Plane
  - automatic Commit, Push, Merge, or Release
  - implicit admission of optional or deferred capabilities
```

## Preserved boundaries

`human_disposition` for `FTR-001..030` remains unchanged. The selected product sequence constrains contract work; it does not accept every related feature dossier as implementation scope.

```yaml
decided_by: current human user in the primary Codex thread
decided_at: '2026-07-30'
authenticity_method: CURRENT_USER_MESSAGE_IN_PRIMARY_THREAD
historical_next_action_at_decision_time: APPLY_SCOPE_TO_STAGE_B_OWNERS
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
