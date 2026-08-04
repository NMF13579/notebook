---
artifact_id: DEC-ARCH-001
adr_id: ADR-001
artifact_type: HUMAN_ARCHITECTURE_DECISION_RECORD_AND_ADR
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R4
status: HUMAN_DECIDED_IMPLEMENTATION_REPOSITORY_DEFERRED
authority: HUMAN_DECISION
exact_subject: Implementation repository choice and exact repository identity for AOS Core v1
created: '2026-07-30'
gate_id: HUMAN_ARCHITECTURE_GATE_G2
human_disposition: ACCEPT
human_decision_record:
  schema_version: aos.decision/v1
  decision_id: DEC-ARCH-001
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
  manifest_basis: package-relative sorted SHA-256 lines for 14 Stage B files
latest_human_clarification:
  date: '2026-07-30'
  exact_subject: Repository creation and documentation location
  repository_creation: DO_NOT_CREATE
  documentation_repository: NMF13579/notebook
  implementation_repository: UNASSIGNED
  stage_c_contract_acceptance: NOT_GRANTED_BY_THIS_CLARIFICATION
repository_clarification_record:
  schema_version: aos.decision/v1
  decision_id: DEC-ARCH-001
  decision_revision: R2
  record_role: SUPERSEDING_REPOSITORY_CLARIFICATION
  decision_type: ARCHITECTURE
  decision_value: DEFER_IMPLEMENTATION_REPOSITORY_AND_USE_NOTEBOOK_FOR_DOCUMENTATION_ONLY
  actor_reference: PRIMARY_USER
  actor_role: PROJECT_OWNER
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  decision_channel: PRIMARY_CODEX_THREAD
  subject:
    kind: HUMAN_MESSAGE_TEXT
    exact_text: Репозиторий не создавать. Документация формируется только в notebook
    normalization: UTF-8 exact text plus LF
    sha256: d787a2aaed05912e00bb03bc3c77f8ab42d8f0fac8a7f9a21bde023797d8d2fa
  issued_at: '2026-07-30T08:30:49.653Z'
  grants:
    - DOCUMENTATION_LOCATION_BOUNDARY
    - IMPLEMENTATION_REPOSITORY_DEFERRED
  non_grants:
    - REPOSITORY_CREATION
    - DOCUMENTATION_MUTATION
    - CONTRACT_ACCEPTANCE
    - IMPLEMENTATION
    - EXECUTION
    - COMMIT
    - PUSH
    - MERGE
    - RELEASE
  expires_at: NOT_APPLICABLE
  stale_when:
    - the human assigns an implementation repository
    - the human authorizes repository creation
    - the role of NMF13579/notebook changes
    - the human revokes or replaces the clarification
  consumption: NOT_APPLICABLE
provenance:
  - G2_EXACT_USER_DECISION_IN_PRIMARY_CODEX_THREAD_2026-07-30
  - USER_REPOSITORY_AND_DOCUMENTATION_BOUNDARY_CLARIFICATION_2026-07-30
  - G2_ARCHITECTURE_OPTION_PACKAGE.md
  - ../00_Control_and_Source_Precedence.md
upstream_links:
  - G2_ARCHITECTURE_OPTION_PACKAGE.md
downstream_links:
  - ../03_Architecture_and_Decisions.md
  - ../06_Traceability_and_Readiness.md
  - ../07_Implementation_Handoff.md
limitations:
  - No AOS Core v1 implementation repository is assigned or authorized for creation.
  - NMF13579/notebook is the documentation repository only and is not an implementation repository.
  - Physical topology, dependencies, commands, runtime work, and repository-bound execution remain unresolved.
  - Primary-thread authenticity is locally declared; no independent cryptographic signature or non-repudiation is claimed.
implementation_authorization: NONE
git_authorization: NONE
---

# DEC-ARCH-001 / ADR-001 — Implementation Repository

## Human decisions and exact interpretation

```yaml
g2_historical_selection:
  selected_option: G2-REPO-A
  repository_choice: NEW_DEDICATED_REPOSITORY
  received_exact_repository: OWNER/REPOSITORY
  received_value_classification: UNRESOLVED_PLACEHOLDER
current_human_clarification:
  repository_creation: DO_NOT_CREATE
  documentation_repository: NMF13579/notebook
  documentation_root: AOS-3/development-package/
  notebook_repository_role: ACTIVE_PROJECT_KNOWLEDGE_REPOSITORY
  notebook_is_implementation_repository: false
effective_implementation_repository: UNASSIGNED
future_repository_binding: REQUIRES_SEPARATE_HUMAN_DECISION
implementation_authorization: NONE
git_authorization: NONE
```

The later human clarification supersedes only the G2 proposal to create a dedicated repository now. It does not change `DEC-ARCH-002..008`, accept the Stage C contracts, assign `notebook` as an implementation repository, or authorize implementation/Git work.

## Consequences

Unblocked:

- logical architecture, toolchain, persistence, privacy, authenticity, risk, compatibility, and portable contract authoring;
- implementation-independent acceptance and recovery contracts.
- completion and review of the portable documentation package in `NMF13579/notebook`;
- after exact contract acceptance, portable Task templates and Task Brief candidates whose repository binding remains explicitly `UNASSIGNED`.

Blocked:

- repository preflight and physical topology;
- dependency verification;
- repository-bound Task enrichment, physical paths, commands, and execution eligibility;
- implementation handoff into an actual repository.

## Reversal and staleness

This revision becomes stale when a human assigns an exact implementation repository, authorizes repository creation, changes the documentation repository, or changes the role of `NMF13579/notebook`.

```yaml
historical_next_action_at_decision_time: HUMAN_CONTRACT_GATE_C1
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
