---
artifact_id: DEC-ARCH-006
adr_id: ADR-006
artifact_type: HUMAN_ARCHITECTURE_DECISION_RECORD_AND_ADR
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R3
status: HUMAN_DECIDED
authority: HUMAN_DECISION
exact_subject: Human Decision authenticity, exact-subject binding, staleness, and non-grants for AOS Core v1
created: '2026-07-30'
gate_id: HUMAN_ARCHITECTURE_GATE_G2
human_disposition: ACCEPT
human_decision_record:
  schema_version: aos.decision/v1
  decision_id: DEC-ARCH-006
  decision_type: ARCHITECTURE
  decision_value: ACCEPT
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  decision_channel: PRIMARY_CODEX_THREAD
  subject:
    kind: PACKAGE_CANDIDATE
    package_id: AOS3-DEVELOPMENT-PACKAGE
    package_revision: DRAFT-R2
    candidate_scope: STAGE_B_G2_ARCHITECTURE_OPTION_PACKAGE
    aggregate_sha256: d8170b28019310126932fa80b6bae411a36215def03bb53011561364f604917d
    manifest_basis: package-relative sorted SHA-256 lines for 14 DRAFT-R2 files
  issued_at: '2026-07-30T10:28:46Z'
  grants: [ARCHITECTURE_DECISION_FOR_EXACT_SUBJECT]
  non_grants: [DOCUMENTATION_MUTATION, IMPLEMENTATION, EXECUTION, COMMIT, PUSH, MERGE, RELEASE]
  expires_at: NOT_APPLICABLE
  stale_when:
    - exact subject revision or hash changes
    - decision value changes or the human revokes it
  consumption: NOT_APPLICABLE
candidate_binding:
  package_revision: DRAFT-R2
  aggregate_sha256: d8170b28019310126932fa80b6bae411a36215def03bb53011561364f604917d
  manifest_basis: package-relative sorted SHA-256 lines for 14 DRAFT-R2 files
provenance:
  - G2_EXACT_USER_DECISION_IN_PRIMARY_CODEX_THREAD_2026-07-30
  - G2_ARCHITECTURE_OPTION_PACKAGE.md
  - ../research/RSR-002_AOS_FARM_Decision_and_Recovery_Boundaries.md
upstream_links:
  - G2_ARCHITECTURE_OPTION_PACKAGE.md
  - ../research/RSR-002_AOS_FARM_Decision_and_Recovery_Boundaries.md
downstream_links:
  - ../04_Runtime_and_Data_Contracts.md
  - ../05_Quality_Recovery_and_Security.md
limitations:
  - LOCAL_DECLARED does not prove cryptographic identity or non-repudiation.
implementation_authorization: NONE
git_authorization: NONE
---

# DEC-ARCH-006 / ADR-006 — Human Decision Authenticity

```yaml
selected_option: G2-AUTH-A
authenticity_level: LOCAL_DECLARED_HASH_BOUND
required_fields:
  - decision_id
  - decision_type
  - decision_value
  - actor_reference
  - actor_role
  - decision_channel
  - exact_subject_hash
  - issued_at
  - grants
  - non_grants
  - staleness_or_expiry
  - consumption_when_applicable
cryptographic_non_repudiation: false
human_disposition: ACCEPT
```

Generated, inferred, validator-created, or Evidence-derived decisions are invalid. A changed decision subject becomes stale. Every decision grants only its declared fact class and leaves unrelated implementation and Git permissions unchanged.

```yaml
historical_next_action_at_decision_time: DEFINE_DECISION_WITNESS_AND_STALENESS_CONTRACTS
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
