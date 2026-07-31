---
artifact_id: AOS3-DPKG-TPL-DEC-001
artifact_type: DECISION_RECORD_TEMPLATE
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R3
status: DRAFT
authority: PROPOSAL
exact_subject: Portable schema for human product, scope, architecture, authority decisions, and ADRs
created: '2026-07-30'
provenance:
  - ../00_Control_and_Source_Precedence.md
  - ../../../docs/00_Core.md
  - ../../../docs/03_Development.md
upstream_links:
  - ../00_Control_and_Source_Precedence.md
  - ../../../docs/00_Core.md
downstream_links: []
limitations:
  - This template does not contain or simulate a human decision.
  - A completed record is authoritative only for its exact subject, revision, hash, and declared fact class.
implementation_authorization: NONE
git_authorization: NONE
---

# Decision Record Template

Use one record for one material decision. Copy this template only inside an explicitly authorized documentation stage.

```yaml
record:
  record_id: DEC-###
  record_type: PRODUCT | CONTRACT | ARCHITECTURE | EXECUTION | RESULT | GIT
  revision: R1
  status: DRAFT
  authority: PROPOSAL
  exact_subject:
  created:
  supersedes: NONE

candidate_binding:
  package_id: AOS3-DEVELOPMENT-PACKAGE
  package_revision:
  subject_paths: []
  subject_sha256: []
  aggregate_sha256:

provenance:
  canonical_sources: []
  observed_repository:
  observed_ref:
  observed_commit:
  reference_records: []

context:
  confirmed_facts: []
  proposals: []
  conflicts: []
  unknowns: []
  limitations: []

options:
  - option_id:
    description:
    benefits: []
    costs: []
    risks: []
    affected_ids: []

human_decision:
  schema_version: aos.decision/v1
  decision_id: DEC-###
  decision_type: PRODUCT | CONTRACT | ARCHITECTURE | EXECUTION | RESULT | GIT
  decision_value: UNDECIDED
  actor_reference:
  actor_role:
  authenticity_level: LOCAL_DECLARED_HASH_BOUND
  decision_channel:
  subject:
    kind: PACKAGE_CANDIDATE | ACCEPTED_SUBJECT_SET_WITH_PACKAGE_CANDIDATE | HUMAN_MESSAGE_TEXT | TASK_NAMESPACE_DECISION_WITH_SOURCE_CANDIDATE
    # Copy exactly one payload from "Subject variants" below.
  issued_at:
  grants: []
  non_grants:
    - IMPLEMENTATION
    - EXECUTION
    - COMMIT
    - PUSH
    - MERGE
    - RELEASE
  expires_at: NOT_APPLICABLE
  stale_when:
    - exact subject revision or hash changes
    - decision value changes or the human revokes it
  consumption: NOT_APPLICABLE

effects:
  unblocks: []
  remains_blocked: []
  invalidates: []
  downstream_links: []

authorization:
  documentation_mutation: NONE
  implementation: NONE
  git:
    commit: NONE
    push: NONE
    merge: NONE
    release: NONE

checks:
  checks_run: []
  checks_not_run: []

next_required_action:
stop: true
```

## Subject variants

`subject.kind` is a required discriminator. Copy exactly one payload; do not combine fields from multiple variants.

```yaml
subject:
  kind: PACKAGE_CANDIDATE
  package_id: AOS3-DEVELOPMENT-PACKAGE
  package_revision: exact package revision
  candidate_scope: exact bounded scope
  aggregate_sha256: 64 lowercase hex
  manifest_basis: exact deterministic manifest rule
```

```yaml
subject:
  kind: ACCEPTED_SUBJECT_SET_WITH_PACKAGE_CANDIDATE
  package_revision: exact package revision
  aggregate_sha256: 64 lowercase hex
  accepted_subject_manifest_sha256: 64 lowercase hex
  subject_ids: [stable ID, ...]
```

```yaml
subject:
  kind: HUMAN_MESSAGE_TEXT
  exact_text: exact UTF-8 human message
  normalization: UTF-8 exact text plus LF
  sha256: 64 lowercase hex
```

```yaml
subject:
  kind: TASK_NAMESPACE_DECISION_WITH_SOURCE_CANDIDATE
  task_ids: [stable package-local Task ID, ...]
  source_package_revision: exact package revision
  source_candidate_sha256: 64 lowercase hex
  manifest_basis: exact deterministic manifest rule
```

Only `decision_revision` and `record_role` may be added as record-level metadata when the specific decision record requires them. Every other undeclared record or subject field is forbidden.

## Rules

1. `UNDECIDED` never becomes an implicit default.
2. A new subject revision makes a prior decision `STALE` until rebound or reconfirmed.
3. Decision authority never expands beyond `fact_class_scope`.
4. Product acceptance does not grant implementation or Git authority.
5. An ADR records a human architecture decision; an agent-authored option comparison remains `PROPOSAL`.
6. A record without actor, role, channel, RFC3339 receipt time, exact subject/hash binding, grants, non-grants, staleness, and consumption cannot unlock dependent work.
7. `LOCAL_DECLARED_HASH_BOUND` is local provenance, not cryptographic identity or non-repudiation.
8. One `subject.kind` selects one closed payload; mixed, missing, or undeclared variant fields invalidate the record.
