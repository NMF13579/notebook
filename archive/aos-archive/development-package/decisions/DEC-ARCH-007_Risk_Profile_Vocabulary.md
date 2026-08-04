---
artifact_id: DEC-ARCH-007
adr_id: ADR-007
artifact_type: HUMAN_ARCHITECTURE_DECISION_RECORD_AND_ADR
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R3
status: HUMAN_DECIDED
authority: HUMAN_DECISION
exact_subject: Minimal human-owned Risk Profile vocabulary for AOS Core v1
created: '2026-07-30'
gate_id: HUMAN_ARCHITECTURE_GATE_G2
human_disposition: ACCEPT
human_decision_record:
  schema_version: aos.decision/v1
  decision_id: DEC-ARCH-007
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
downstream_links:
  - ../04_Runtime_and_Data_Contracts.md
  - ../05_Quality_Recovery_and_Security.md
limitations:
  - Thresholds mapping observed actions to a proposed minimum class remain DRAFT contract content.
implementation_authorization: NONE
git_authorization: NONE
---

# DEC-ARCH-007 / ADR-007 — Risk Profile Vocabulary

```yaml
selected_option: G2-RISK-A
vocabulary:
  - UNASSIGNED
  - READ_ONLY
  - REVERSIBLE_WRITE
  - PROTECTED_WRITE
  - DESTRUCTIVE_OR_PUBLISHING
assignment_authority: HUMAN_ONLY
agent_capability: PROPOSE_MINIMUM_WITH_REASONS
execution_authority_effect: NONE
human_disposition: ACCEPT
```

A Risk Profile classifies treatment; it never authorizes execution. Unknown or conflicting risk blocks only the affected write/action. Commit, Push, Merge, Release, external transmission, and destructive operations remain separate human decisions.

```yaml
historical_next_action_at_decision_time: DEFINE_PERMISSION_AND_EXECUTION_CONTRACTS
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
