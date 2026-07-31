---
artifact_id: DEC-PROD-003
artifact_type: HUMAN_PRODUCT_DECISION_RECORD
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R3
status: HUMAN_DECIDED
authority: HUMAN_DECISION
exact_subject: Ordered Core v1 slice sequence and identity of the first vertical slice
created: '2026-07-30'
gate_id: HUMAN_PRODUCT_GATE_G1
human_disposition: ACCEPT
human_decision_record:
  schema_version: aos.decision/v1
  decision_id: DEC-PROD-003
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
  - Acceptance of the sequence does not authorize automatic transition between slices.
  - Slices B and C require accepted upstream contracts and their own later authority.
implementation_authorization: NONE
git_authorization: NONE
---

# DEC-PROD-003 — Core v1 Slice Sequence

## Decision

```yaml
selected_directions:
  - G1-OPT-A
  - G1-OPT-B
  - G1-OPT-C
ordered_sequence:
  - G1-OPT-A_INTENT_TO_REVIEWED_PRODUCT_DRAFT
  - G1-OPT-B_ACCEPTED_CONTRACT_TO_BOUNDED_TASK
  - G1-OPT-C_EXISTING_PROJECT_TO_SAFE_NEXT_ACTION
first_core_v1_vertical_slice: G1-OPT-A_INTENT_TO_REVIEWED_PRODUCT_DRAFT
human_disposition: ACCEPT
```

## Boundary

The three options are accepted as ordered Core v1 directions, not as one combined first slice:

```text
A: intent → clarification → DRAFT Product Spec/Feature Passport → human review
→ B: accepted contract → bounded Task Brief → authorization-required stop
→ C: read-only state recovery → blockers → one safe next action → human review
```

Each arrow is a dependency and human gate, not automatic execution.

## Authenticity and staleness

```yaml
decided_by: current human user in the primary Codex thread
decided_at: '2026-07-30'
authenticity_method: CURRENT_USER_MESSAGE_IN_PRIMARY_THREAD
stale_when:
  - sequence order changes
  - a slice boundary changes materially
  - candidate binding changes without an explicit rebind
historical_next_action_at_decision_time: DOCUMENT_SLICE_A_AND_TRACE_FUTURE_SLICES_B_C
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
