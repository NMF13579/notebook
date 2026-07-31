---
artifact_id: DEC-ARCH-003
adr_id: ADR-003
artifact_type: HUMAN_ARCHITECTURE_DECISION_RECORD_AND_ADR
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R3
status: HUMAN_DECIDED
authority: HUMAN_DECISION
exact_subject: Language, toolchain, dependency, and distribution boundary for AOS Core v1
created: '2026-07-30'
gate_id: HUMAN_ARCHITECTURE_GATE_G2
human_disposition: ACCEPT
human_decision_record:
  schema_version: aos.decision/v1
  decision_id: DEC-ARCH-003
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
  - Exact libraries, versions, package manager, supported operating systems, and CI matrix are not selected or verified.
implementation_authorization: NONE
git_authorization: NONE
---

# DEC-ARCH-003 / ADR-003 — Toolchain and Dependencies

```yaml
selected_option: G2-TOOL-A
language: PYTHON_3_12_OR_NEWER
dependency_policy: MINIMAL_PINNED_DEPENDENCIES
distribution: LOCAL_PACKAGE_AND_CLI
exact_dependencies: UNASSIGNED_UNTIL_REPOSITORY_PREFLIGHT
human_disposition: ACCEPT
```

The decision selects a toolchain class, not a requirements file or installation operation. Standard-library-first is preferred where it preserves contract strictness; any third-party dependency requires a named capability, pinned version, license/security review proportional to risk, and removal/migration boundary.

```yaml
historical_next_action_at_decision_time: DEFINE_REPOSITORY_BOUND_DEPENDENCY_SET_AFTER_DEC_ARCH_001
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
