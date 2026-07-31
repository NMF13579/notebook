---
artifact_id: DEC-PROD-006
artifact_type: HUMAN_PRODUCT_DECISION_RECORD
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R3
status: HUMAN_DECIDED
authority: HUMAN_DECISION
exact_subject: Whether RMP-004 and RMP-005 receive material sub-items at G1
created: '2026-07-30'
gate_id: HUMAN_PRODUCT_GATE_G1
human_disposition: ACCEPT
human_decision_record:
  schema_version: aos.decision/v1
  decision_id: DEC-PROD-006
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
  - ../../AOS_Core_Roadmap.md
  - CURRENT_USER_CONFIRMATION_2026-07-30
upstream_links:
  - ../00_Control_and_Source_Precedence.md
  - ../../AOS_Core_Roadmap.md
downstream_links:
  - ../01_Product_and_Core_V1_Scope.md
  - ../02_User_Journeys_and_Workflows.md
limitations:
  - This decision preserves current Roadmap IDs; it does not modify the Roadmap.
  - A later material boundary may require a new human decision and new RMP sub-items.
implementation_authorization: NONE
git_authorization: NONE
---

# DEC-PROD-006 — RMP-004 and RMP-005 Boundaries

## Decision

```yaml
rmp_004_split_decision: KEEP_UNSPLIT_UNTIL_MATERIAL_BOUNDARY
rmp_005_split_decision: KEEP_UNSPLIT_UNTIL_MATERIAL_BOUNDARY
human_disposition: ACCEPT
```

`RMP-004` continues to own the documentation path from discovery/intake to reviewed DRAFT specification. `RMP-005` continues to own minimal hierarchy, Task format, and derived Queue documentation.

No `RMP-004.N` or `RMP-005.N` is created in Stage B.

## Reopen conditions

- independent acceptance or authority boundaries emerge;
- the artifacts require distinct lifecycle or validation gates;
- one item cannot remain bounded without hiding material dependencies;
- a human explicitly requests the split.

```yaml
decided_by: current human user in the primary Codex thread
decided_at: '2026-07-30'
authenticity_method: CURRENT_USER_MESSAGE_IN_PRIMARY_THREAD
historical_next_action_at_decision_time: PRESERVE_UNSPLIT_RMP_BOUNDARIES_IN_STAGE_B
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
