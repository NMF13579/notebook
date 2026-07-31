---
artifact_id: DEC-PROD-005
artifact_type: HUMAN_PRODUCT_DECISION_RECORD
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R3
status: HUMAN_DECIDED
authority: HUMAN_DECISION
exact_subject: Ownership and relationship between Product Spec and Feature Passport
created: '2026-07-30'
gate_id: HUMAN_PRODUCT_GATE_G1
human_disposition: ACCEPT
human_decision_record:
  schema_version: aos.decision/v1
  decision_id: DEC-PROD-005
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
  - ../../../docs/01_Product.md
  - CURRENT_USER_CONFIRMATION_2026-07-30
upstream_links:
  - ../00_Control_and_Source_Precedence.md
  - ../../../docs/01_Product.md
downstream_links:
  - ../01_Product_and_Core_V1_Scope.md
  - ../02_User_Journeys_and_Workflows.md
limitations:
  - Exact storage format and physical file topology remain G2 or later decisions.
  - A Feature Passport cannot override Product Spec boundaries without a new human decision.
implementation_authorization: NONE
git_authorization: NONE
---

# DEC-PROD-005 — Product Spec and Feature Passport Relation

## Decision

```yaml
product_spec_owner:
  owns:
    - product problem and target users
    - product-level outcomes, scope, and non-goals
    - cross-feature journeys and constraints
    - product-level metrics, risks, and open decisions
feature_passport_owner:
  owns:
    - one feature identity and problem
    - actor, trigger, preconditions, inputs, outputs
    - behavior, states, failures, recovery, and authority
    - feature acceptance and negative scenarios
relationship:
  - Product Spec references Feature Passports
  - each Feature Passport references its governing Product Spec revision
  - duplicated claims defer to their declared owner
human_disposition: ACCEPT
```

## Boundary

The artifacts are logically separate even if a later physical-topology decision stores them together. A Feature Passport is not accepted merely because the Product Spec references it.

```yaml
decided_by: current human user in the primary Codex thread
decided_at: '2026-07-30'
authenticity_method: CURRENT_USER_MESSAGE_IN_PRIMARY_THREAD
historical_next_action_at_decision_time: APPLY_OWNER_BOUNDARY_IN_DOCUMENTS_01_AND_02
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
