---
artifact_id: DEC-ARCH-002
adr_id: ADR-002
artifact_type: HUMAN_ARCHITECTURE_DECISION_RECORD_AND_ADR
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R3
status: HUMAN_DECIDED
authority: HUMAN_DECISION
exact_subject: Logical architecture, runtime shape, and interaction boundary for AOS Core v1
created: '2026-07-30'
gate_id: HUMAN_ARCHITECTURE_GATE_G2
human_disposition: ACCEPT
human_decision_record:
  schema_version: aos.decision/v1
  decision_id: DEC-ARCH-002
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
upstream_links:
  - G2_ARCHITECTURE_OPTION_PACKAGE.md
downstream_links:
  - ../03_Architecture_and_Decisions.md
  - ../04_Runtime_and_Data_Contracts.md
limitations:
  - Physical package paths remain unassigned until the implementation repository is bound.
implementation_authorization: NONE
git_authorization: NONE
---

# DEC-ARCH-002 / ADR-002 — Architecture and Topology

```yaml
selected_bundle: G2-OPT-A
selected_option: G2-ARCH-A
style: MODULAR_MONOLITH_WITH_PORTS_AND_ADAPTERS
runtime_shape: LOCAL_PROCESS
portable_interface:
  - TEXT
  - JSON
interaction_surface:
  - CONVERSATIONAL_AGENT_ADAPTER
  - CLI
source_of_truth_rule: ADAPTERS_AND_UI_ARE_DERIVED_OR_INPUT_OUTPUT_SURFACES
human_disposition: ACCEPT
```

Consequences:

- domain contracts and application services remain independent of Codex or another agent environment;
- adapters may render or collect data but cannot own lifecycle or authority state;
- no service, database, hosted control plane, or UI framework is a Core v1 dependency;
- physical module names are proposals until repository binding.

Reversal requires a new human architecture decision and migration plan preserving portable contracts and exports.

```yaml
historical_next_action_at_decision_time: APPLY_TO_STAGE_C_LOGICAL_ARCHITECTURE
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
