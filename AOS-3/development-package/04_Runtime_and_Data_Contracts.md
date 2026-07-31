---
artifact_id: AOS3-DPKG-DOC-004
artifact_type: RUNTIME_AND_DATA_CONTRACTS
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R7
status: DRAFT_SOURCE_WITH_C1_ACCEPTED_SUBJECTS_AND_NEW_DRAFT_SCHEMAS
authority: PROPOSAL_WITH_HUMAN_ARCHITECTURE_INPUTS
exact_subject: Implementation-grade portable I/O, schemas, states, side effects, permissions, idempotency, and integration boundaries for RMP-002 through RMP-008
created: '2026-07-30'
human_acceptance: C1_ACCEPTED_126_CURRENT_11_STALE_10_NEW_AC_AND_2_NEW_SCHEMA_DRAFT
provenance:
  - path: ../../docs/00_Core.md
    use: authority, status, and safety invariants
  - path: ../../docs/02_Architecture.md
    use: C-001 through C-014 contract classes and ownership
  - path: ../../docs/03_Development.md
    use: task, execution, validation, report, recovery, and Git boundaries
  - path: ../../docs/06_Features.md
    use: relevant FTR-001 through FTR-019 behavior candidates
  - path: 01_Product_and_Core_V1_Scope.md
    use: product requirements and first-slice contract
  - path: 02_User_Journeys_and_Workflows.md
    use: journeys, transitions, failures, and recovery
  - path: 03_Architecture_and_Decisions.md
    use: accepted G2 architecture boundary
  - path: research/RSR-003_AgentOS_Task_Authorization_and_Handoff.md
    use: non-authoritative Task, authorization, result, and handoff evidence
  - path: research/RSR-004_AOS_FARM_Candidate_Validation_and_Recovery.md
    use: non-authoritative candidate, validation, and recovery evidence
upstream_links:
  - 01_Product_and_Core_V1_Scope.md
  - 02_User_Journeys_and_Workflows.md
  - 03_Architecture_and_Decisions.md
  - decisions/DEC-ARCH-002_Architecture_and_Topology.md
  - decisions/DEC-ARCH-004_Project_Memory.md
  - decisions/DEC-ARCH-005_Provider_and_Privacy.md
  - decisions/DEC-ARCH-006_Human_Decision_Authenticity.md
  - decisions/DEC-ARCH-007_Risk_Profile_Vocabulary.md
  - decisions/DEC-CORR-001_Package_Local_Task_Namespace.md
downstream_links:
  - 05_Quality_Recovery_and_Security.md
  - 06_Traceability_and_Readiness.md
  - 07_Implementation_Handoff.md
limitations:
  - Authored DRAFT labels inside the C1-frozen contract blocks remain historical source-state labels; effective acceptance is owned by DEC-CONTRACT-001.
  - Corrected PSC-A-001 is C1-stale in DRAFT-R9; its accepted CTR dependencies remain independently current.
  - SCH-PRODUCT-SPEC-001 and SCH-FEATURE-PASSPORT-001 are new DRAFT shared schemas outside the frozen CTR-003 subject and are not accepted by C1.
  - Changed WFC-A-001 plus both new shared schemas block AOS3-DPKG-TASK-003 materialization.
  - Task candidates derived from accepted contracts are not themselves human-accepted.
  - Exact repository paths, dependency versions, commands, and test entrypoints remain blocked by DEC-ARCH-001.
  - Runtime behavior and schema enforcement are NOT_RUN.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# 04 — Runtime and Data Contracts

## 1. Status boundary

This owner defines portable implementation-grade behavior. “Implementation-grade” means fields, states, effects, failure behavior, recovery, and executable acceptance are specified precisely enough for Task compilation. C1 acceptance does not mean implemented, executed, validated, or authorized.

```yaml
contract_source_status: C1_FROZEN_CTR_BLOCKS_WITH_NEW_DRAFT_SHARED_SCHEMAS
contract_acceptance: HUMAN_ACCEPTED_VIA_DEC-CONTRACT-001
current_package_acceptance_projection:
  current_accepted_subjects: 126
  stale_c1_subjects: [PSC-A-001, WFC-A-001, WFC-B-001, WFC-C-001, AC-WFC-A-001-01..07]
  new_draft_subjects: [AC-WFC-B-001-01..05, AC-WFC-C-001-01..05, SCH-PRODUCT-SPEC-001, SCH-FEATURE-PASSPORT-001]
accepted_subject_manifest_sha256: 2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
schema_implementation: NOT_RUN
runtime_verification: NOT_RUN
task_compilation: DRAFT_CANDIDATES_FROM_CURRENT_ACCEPTED_TASK_INPUTS
human_task_acceptance: NOT_RUN
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
```

## 2. Normative serialization boundary

Portable records use UTF-8 Markdown, YAML, or JSON. Machine-owned data structures must have one canonical YAML/JSON representation with:

- closed required fields and closed enums;
- explicit schema version;
- repository-relative POSIX-style paths;
- SHA-256 over raw bytes or a declared canonical manifest;
- timestamps as RFC 3339 UTC strings;
- no implicit conversion of missing, `UNKNOWN`, empty, or explicit `NONE`;
- deterministic ordering for manifest and digest inputs;
- rejection of duplicate keys, unsupported versions, and unexpected authority fields.

Markdown may explain a record but cannot override its machine-owned block.

## 3. Shared closed vocabularies

```yaml
ClaimClass:
  - OBSERVED_AT_SNAPSHOT
  - REPORTED
  - SYNTHESIZED
  - CONFLICT
  - NOT_FOUND
  - UNKNOWN
  - NOT_RUN
  - BLOCKED

DocumentMaturity:
  - DRAFT
  - HUMAN_REVIEW_REQUIRED
  - HUMAN_ACCEPTED
  - STALE
  - SUPERSEDED

TechnicalResult:
  - CONTRACT_VIOLATION
  - FAIL
  - BLOCKED
  - UNKNOWN
  - NOT_RUN
  - PASS

HumanDisposition:
  - ACCEPT
  - NEEDS_CHANGES
  - REJECT
  - DEFER
  - NOT_RUN

PermissionState:
  - ALLOWED
  - HUMAN_AUTHORIZATION_REQUIRED
  - BLOCKED_POLICY
  - BLOCKED_UNKNOWN
  - NOT_APPLICABLE

RiskActionClass:
  - UNASSIGNED
  - READ_ONLY
  - REVERSIBLE_WRITE
  - PROTECTED_WRITE
  - DESTRUCTIVE_OR_PUBLISHING

Freshness:
  - CURRENT_FOR_BINDING
  - STALE
  - UNKNOWN
```

Unknown values are rejected. `NOT_RUN` is a result, not an omission. `PASS` never creates human or Git authority.

The `TechnicalResult` list above is a local DRAFT projection. Canonical [`docs/00_Core.md`](../../docs/00_Core.md) also lists `HUMAN_REVIEW_REQUIRED` on that axis, while [`docs/03_Development.md`](../../docs/03_Development.md) and this package use it as maturity/control state. `BLK-006_CANONICAL_STATUS_AXIS_CONFLICT` therefore blocks canonical TechnicalResult/ResultEnvelope conformance and readiness claims. This package neither imports a historical external blocker ID nor mutates canonical `/docs`; raw source values must be preserved until a separate human decision resolves the owner conflict.

## 4. Shared record schemas

### 4.1 `ArtifactEnvelope`

```yaml
schema_version: aos.core/v1
artifact_id: stable non-empty ID
artifact_type: closed type owned by its contract
revision: positive revision label
maturity: DocumentMaturity
exact_subject: non-empty statement
created_at: RFC3339 UTC
updated_at: RFC3339 UTC
source_bindings: [SourceBinding, ...]
upstream_ids: [stable ID, ...]
content_sha256: 64 lowercase hex characters
limitations: [non-empty string, ...]
implementation_authorization: NONE
git_authorization: NONE
```

Required rules:

- the digest excludes no bytes unless the exclusion is versioned and explicit;
- `content_sha256` cannot be used as a self-referential digest field without a detached manifest;
- an empty limitations list is allowed only after a check explicitly establishes none;
- maturity changes require a separate exact decision record.

### 4.2 `SourceBinding`

```yaml
source_id: stable ID
source_kind: HUMAN_DECISION | ACCEPTED_ARTIFACT | REPOSITORY_OBSERVATION | REFERENCE | USER_INPUT
locator: portable locator or repository/ref/commit/path
revision_or_commit: exact immutable identity
sha256: 64 lowercase hex or NOT_APPLICABLE
claim_class: ClaimClass
freshness: Freshness
authority_scope: [fact class, ...]
```

A floating branch, chat summary, or missing path cannot be represented as `CURRENT_FOR_BINDING`.

### 4.3 `CandidateManifest`

```yaml
manifest_version: 1
candidate_id: stable ID
subject_type: DOCUMENTATION | IMPLEMENTATION | VALIDATION_INPUT
baseline_binding: exact baseline or NOT_APPLICABLE
entries:
  - relative_path: normalized repository-relative path
    state: ADDED | MODIFIED | DELETED | RENAMED | UNCHANGED_INCLUDED
    content_sha256: 64 lowercase hex or NOT_APPLICABLE_FOR_DELETION
    size_bytes: non-negative integer
forbidden_paths: [normalized relative path, ...]
unexpected_paths_policy: BLOCK
manifest_sha256: detached SHA-256 of sorted entry lines
frozen_at: RFC3339 UTC
```

The manifest is invalid when paths are absolute, escape with `..`, resolve through an unsafe symlink, duplicate after normalization, or change after freeze.

### 4.4 `HumanDecisionRecord`

```yaml
schema_version: aos.decision/v1
decision_id: stable ID
decision_type: PRODUCT | CONTRACT | ARCHITECTURE | EXECUTION | RESULT | GIT
decision_value: ACCEPT | NEEDS_CHANGES | REJECT | DEFER | exact decision value
actor_reference: locally declared human reference
actor_role: non-empty role
authenticity_level: LOCAL_DECLARED_HASH_BOUND
decision_channel: non-empty local channel identifier
subject:
  discriminator: kind
  one_of:
    - kind: PACKAGE_CANDIDATE
      required_fields:
        - package_id
        - package_revision
        - candidate_scope
        - aggregate_sha256
        - manifest_basis
    - kind: ACCEPTED_SUBJECT_SET_WITH_PACKAGE_CANDIDATE
      required_fields:
        - package_revision
        - aggregate_sha256
        - accepted_subject_manifest_sha256
        - subject_ids
    - kind: HUMAN_MESSAGE_TEXT
      required_fields:
        - exact_text
        - normalization
        - sha256
    - kind: TASK_NAMESPACE_DECISION_WITH_SOURCE_CANDIDATE
      required_fields:
        - task_ids
        - source_package_revision
        - source_candidate_sha256
        - manifest_basis
  additional_fields_policy: FORBID_UNDECLARED_FOR_SELECTED_KIND
optional_record_fields:
  decision_revision: exact decision-record revision
  record_role: exact non-empty record role
issued_at: RFC3339 UTC
grants: [explicit fact class or operation, ...]
non_grants: [explicit excluded operation, ...]
expires_at: RFC3339 UTC or NOT_APPLICABLE
stale_when: [machine/human-readable condition, ...]
consumption: NOT_APPLICABLE | UNUSED | CONSUMED
record_additional_fields_policy: FORBID_UNDECLARED
```

The selected `subject.kind` is the discriminator: exactly its declared fields are required, fields owned by another variant are forbidden, and every digest is 64 lowercase hex. The record is invalid if actor/channel/subject is absent, the subject changed, the decision was generated by an agent/validator, a consumer asks for an undeclared grant, or an undeclared record/subject field is present. These tagged variants preserve exact package-candidate, accepted-subject-set, human-message, and Task-namespace bindings without flattening them into a lossy generic tuple.

### 4.5 `ResultEnvelope`

```yaml
schema_version: aos.result/v1
result_id: stable ID
subject_binding: exact artifact/candidate/repository identity
result: TechnicalResult
technical_result_vocabulary_status: BLOCKED_BLK_006
checks:
  - check_id: stable ID
    required: true | false
    result: TechnicalResult
    method: command or deterministic method
    evidence_locator: portable locator
    limitations: [string, ...]
unknowns: [string, ...]
blockers: [string, ...]
human_disposition: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
next_required_action: exactly one action
```

Aggregate precedence is:

```text
CONTRACT_VIOLATION > FAIL > BLOCKED > UNKNOWN > NOT_RUN > PASS
```

A required `NOT_RUN` prevents aggregate `PASS`.

### 4.6 `ProjectMemoryRecord`

```yaml
schema_version: aos.memory/v1
memory_id: stable ID
project_identity:
  repository: exact repository or UNASSIGNED
  worktree: normalized absolute observation or NOT_APPLICABLE
  branch: observed value or NOT_APPLICABLE
  head: exact commit or NOT_APPLICABLE
  observed_at: RFC3339 UTC
active_stage: PLAN | EXECUTE | VALIDATE | REVIEW | NONE
candidate_binding: exact binding or NOT_APPLICABLE
accepted_decisions: [decision ID plus subject hash, ...]
findings: [finding ID, ...]
blockers: [blocker ID, ...]
checks_run: [check ID, ...]
checks_not_run: [check ID, ...]
permission_state: PermissionState
denied_actions: [action plus reason, ...]
changed_paths: [relative path, ...]
limitations: [string, ...]
next_required_action: exactly one action
source_sha256: detached digest
```

Project Memory is stale if any bound source changes. A derived summary cannot rewrite this record.

## 5. Permission and side-effect contract

### 5.1 Classification

```text
pure/read-only, exact scope known
→ propose READ_ONLY

bounded reversible local write
→ propose REVERSIBLE_WRITE

protected data/path/authority/network/provider change
→ propose PROTECTED_WRITE

deletion, irreversible mutation, publication, Commit, Push, Merge, Release
→ propose DESTRUCTIVE_OR_PUBLISHING
```

Only a human assigns `RiskActionClass`. The classifier returns a proposal and reasons, never permission.

### 5.2 Permission resolution

| Condition | Result |
|---|---|
| Read-only action, scope and data boundary known, allowed by current stage | `ALLOWED` |
| Write needs an exact human authorization | `HUMAN_AUTHORIZATION_REQUIRED` |
| Action is forbidden by policy/non-goal | `BLOCKED_POLICY` |
| Scope, identity, risk, provider, or authority is materially unknown | `BLOCKED_UNKNOWN` |
| Action does not apply to the subject | `NOT_APPLICABLE` |

Commit, Push, Merge, Release, provider transmission, and destructive actions require their own exact decisions regardless of other results.

### 5.3 Write request

Every write-capable application operation requires:

```yaml
operation_id: stable ID
idempotency_key: non-empty caller-supplied token
subject_binding: exact current subject
authorization_id: exact unconsumed authorization
preview_binding: exact preview hash
allowed_paths: [normalized relative path, ...]
forbidden_paths: [normalized relative path, ...]
expected_effects: [create | update | delete | rename, ...]
recovery_mode: ATOMIC_REPLACE | DURABLE_JOURNAL
```

Repeat with the same key and identical subject returns the original outcome. The same key with different input returns `CONTRACT_VIOLATION`. Unknown prior outcome returns `BLOCKED_UNKNOWN_OUTCOME` until reconciliation.

## 6. Integration boundaries

| Boundary | Default | Required behavior |
|---|---|---|
| Filesystem | Local | Normalize paths, reject escape/symlink ambiguity, atomic replace or journal |
| Git observation | Read-only | Record root/worktree/branch/HEAD/status without credential-bearing URLs |
| Git mutation | Disabled | Separate exact human decision per Commit/Push/Merge/Release |
| Network/provider | Disabled | No hidden call; optional adapter requires separate contract and consent |
| Clock | Local declared | Record source; do not claim trusted time |
| Agent adapter | Replaceable | Convert I/O only; no lifecycle/authority ownership |
| Derived index | Rebuildable | Carries source hash/freshness; no independent authority |

## 7. Contract registry

| Contract | Roadmap | Status | Primary reason |
|---|---|---|---|
| `CTR-001` | `RMP-002` | `DRAFT_BLOCKED_REPOSITORY_BINDING` | Development scaffold behavior |
| `CTR-002` | `RMP-003` | `DRAFT` | Bootstrap/install/first-start behavior |
| `CTR-003` | `RMP-004` | `DRAFT_FIRST_SLICE` | Intent to reviewed specification |
| `CTR-004` | `RMP-005` | `DRAFT_BLOCKED_UPSTREAM_ACCEPTANCE` | Hierarchy/Task/derived Queue |
| `CTR-005` | `RMP-006` | `DRAFT_FUTURE_BEHAVIOR` | Bounded execution |
| `CTR-006` | `RMP-007` | `DRAFT_FUTURE_BEHAVIOR` | Validation/Evidence/Human Decision |
| `CTR-007` | `RMP-008` | `DRAFT_FUTURE_BEHAVIOR` | Recovery/resume/Project Memory |

## 8. `CTR-001` — Development Scaffold

```yaml
contract_id: CTR-001
revision: R1
status: DRAFT_BLOCKED_REPOSITORY_BINDING
roadmap_id: RMP-002
actor:
  primary: developer or coding agent
  decision_owner: human repository owner
trigger: An accepted implementation Task requests a reproducible local foundation.
preconditions:
  - exact implementation repository is assigned and observed
  - DEC-ARCH-003 toolchain remains current
  - accepted scaffold contract and Task exist
  - documentation, implementation, and Git authorities are distinct
inputs:
  - repository identity and clean/isolated subject
  - Python version policy
  - proposed pinned dependency set
  - supported local environment matrix
  - allowed and forbidden paths
outputs:
  - scaffold manifest
  - one conceptual local entrypoint
  - strict contract loader boundary
  - doctor/self-test result envelope
  - dependency and environment provenance
states:
  - UNBOUND
  - PREFLIGHT_READY
  - SCAFFOLD_CANDIDATE
  - SELF_TEST_REQUIRED
  - HUMAN_REVIEW_REQUIRED
side_effects:
  read_only:
    - repository and environment observation
  write_capable:
    - create only authorized scaffold paths
  forbidden:
    - product runtime readiness claim
    - CI/CD, deployment, remote, or Git delivery
authority:
  agent_may:
    - propose manifest, paths, checks, and dependency rationale
  human_only:
    - assign repository, accept dependencies, authorize writes and Git actions
failures:
  - BLOCKED_UNASSIGNED_REPOSITORY
  - BLOCKED_UNSUPPORTED_PYTHON
  - BLOCKED_DIRTY_OR_WRONG_SUBJECT
  - FAIL_DEPENDENCY_PROVENANCE
  - FAIL_PARTIAL_SCAFFOLD_WRITE
recovery:
  - stop before write when identity/environment fails
  - preserve unrelated state
  - reconcile journal/manifest after interruption
  - repeat only with identical idempotency input or a new authorized revision
non_goals:
  - implement Slice A behavior
  - choose exact dependencies by default
  - create CI/CD or hosted deployment
  - perform Git operations
executable_acceptance:
  - AC-CTR-001-01 exact repository and Python provenance are reported
  - AC-CTR-001-02 clean bootstrap plus self-test is reproducible from declared inputs
  - AC-CTR-001-03 help and doctor read-only modes produce zero source writes
  - AC-CTR-001-04 a scaffold cannot claim Product Runtime or implementation readiness
```

## 9. `CTR-002` — Product Bootstrap and First-Start

```yaml
contract_id: CTR-002
revision: R1
status: DRAFT
roadmap_id: RMP-003
actor:
  primary: non-programmer or domain expert
  supporting: installer/bootstrap adapter
  decision_owner: human target owner
trigger: The user requests preview of installing, updating, disabling, or removing the local AOS package.
preconditions:
  - package and target identities are exact
  - operation mode is explicit
  - target paths are classified as MANAGED, USER, PROJECT, or UNKNOWN
  - apply/removal authorization is separate from preview
inputs:
  - signed-or-digest-bound package manifest with honest authenticity level
  - target root observation
  - operation mode PREVIEW | APPLY | UPDATE | DISABLE | REMOVE
  - ownership map and conflict policy
outputs:
  - exact side-effect-free preview
  - conflict list and required decisions
  - apply/recovery record when separately authorized
  - post-apply verification
  - one first-start action using the selected interaction surface
states:
  - TARGET_DISCOVERY
  - PREVIEW_READY
  - HUMAN_APPLY_AUTHORIZATION_REQUIRED
  - APPLYING
  - VERIFYING
  - FIRST_START_READY
  - RECOVERY_REQUIRED
side_effects:
  preview: none
  apply: only manifest-bound managed paths
  update: preserve user/project paths unless separately migrated
  remove: destructive and separately authorized
authority:
  agent_may:
    - inspect, classify, preview, and verify
  human_only:
    - resolve ownership conflict and authorize apply/update/remove
failures:
  - BLOCKED_WRONG_TARGET
  - BLOCKED_UNKNOWN_OWNERSHIP
  - BLOCKED_PREVIEW_STALE
  - FAIL_APPLY_DIFFERS_FROM_PREVIEW
  - FAIL_INTERRUPTED_APPLY
recovery:
  - use durable journal or atomic publication
  - preserve user/project state
  - classify actual versus intended changes
  - require human decision for destructive rollback or unknown outcome
non_goals:
  - silent overwrite
  - hosted installation
  - automatic update/removal
  - Git delivery
executable_acceptance:
  - AC-CTR-002-01 preview changes zero bytes
  - AC-CTR-002-02 apply is rejected when preview or target identity changes
  - AC-CTR-002-03 repeated identical apply is idempotent
  - AC-CTR-002-04 interrupted apply produces a recoverable journal without user-data loss
  - AC-CTR-002-05 first-start explains status, limitations, and one next action
```

Ownership semantics:

| Class | Meaning | Default treatment |
|---|---|---|
| `MANAGED` | Created and owned by the installed package manifest | May update only through matching preview/authorization |
| `USER` | User-authored personal state | Preserve; conflict requires human decision |
| `PROJECT` | Project/repository-owned state | Preserve; migration requires accepted contract |
| `UNKNOWN` | Ownership cannot be proven | Block affected write |

## 10. `CTR-003` — Intake to Reviewed DRAFT Specification

```yaml
contract_id: CTR-003
revision: R1
status: DRAFT_FIRST_SLICE
roadmap_id: RMP-004
upstream_contracts:
  - PSC-A-001
  - WFC-A-001
actor:
  primary: non-programmer or domain expert
  supporting: conversational or CLI adapter and specification service
  decision_owner: human product owner
trigger: The user provides an idea, problem, brief, or solution-shaped request and asks for a reviewable product boundary.
preconditions:
  - original input boundary is known
  - local-only provider boundary is enforced
  - accepted project sources and current decisions are locatable
  - no implementation, Task, execution, validation, or Git permission is inferred
inputs:
  - original input bytes or explicit normalized bytes plus digest
  - user-declared context, constraints, non-goals, and sensitive flags
  - accepted decisions and source bindings
  - clarification answers linked to question IDs
outputs:
  - IntentRecord
  - DRAFT Product Spec
  - at least one DRAFT Feature Passport by human review when a feature boundary exists
  - classified gaps/conflicts/unknowns
  - CandidateManifest for the review subject
  - one Human Decision request
states:
  - INTAKE_DRAFT
  - NEEDS_CLARIFICATION
  - READY_FOR_SPEC_DRAFT
  - SPEC_DRAFT
  - HUMAN_REVIEW_REQUIRED
side_effects:
  - publish DRAFT local contract artifacts only in an authorized project-memory boundary
  - no external provider/network transmission
authority:
  agent_may:
    - preserve, classify, ask material questions, draft, bind, and report
  human_only:
    - answer material questions and accept/change/reject/defer exact contracts
failures:
  - EMPTY_OR_UNUSABLE_INPUT
  - MATERIAL_INFORMATION_MISSING
  - SOURCE_CONFLICT
  - SENSITIVE_BOUNDARY_UNKNOWN
  - STALE_UPSTREAM_DECISION
  - FAIL_PARTIAL_ARTIFACT_PUBLICATION
recovery:
  - preserve original input and answered questions
  - identify the exact affected field
  - keep unaffected claims usable
  - publish a new revision after correction; never rewrite frozen Evidence
non_goals:
  - architecture selection
  - Task Brief creation
  - implementation or runtime validation
  - provider-backed generation
  - Git operations
executable_acceptance:
  - AC-CTR-003-01 byte/digest comparison proves source preservation
  - AC-CTR-003-02 missing, unknown, conflict, assumption, and explicit NONE remain distinct
  - AC-CTR-003-03 every clarification declares its affected field and materiality
  - AC-CTR-003-04 all Product Spec and Feature Passport owner fields are present
  - AC-CTR-003-05 the review candidate has an exact detached manifest
  - AC-CTR-003-06 the terminal output contains one decision request and stops
```

Minimum `IntentRecord`:

```yaml
intent_id: stable ID
source_input:
  transport: RAW_BYTES | NORMALIZED_TEXT
  locator: local locator
  sha256: 64 lowercase hex
  normalization: description or NOT_APPLICABLE
actor:
problem:
desired_outcome:
context: []
constraints: []
non_goals: []
claims:
  confirmed: []
  assumptions: []
  unknowns: []
  conflicts: []
  explicit_none: []
sensitive_flags: []
questions:
  - question_id:
    affected_fields: []
    materiality_reason:
    answer_status: UNANSWERED | ANSWERED | DEFERRED
```

### 10.1 Shared `ProductSpecRecord` schema

This closed DRAFT schema makes the owner-field check in `AC-CTR-003-04` deterministic without changing the frozen `CTR-003` contract block.

```yaml
schema_id: SCH-PRODUCT-SPEC-001
schema_version: aos.product-spec/v1
status: DRAFT
authority: PROPOSAL
additional_fields_policy: FORBID_UNDECLARED
required_fields:
  - product_spec_id
  - revision
  - maturity
  - exact_subject
  - governing_decision_bindings
  - source_intent_bindings
  - target_users
  - problem_and_jobs
  - observable_outcomes
  - scope
  - non_goals
  - journeys
  - feature_passport_refs
  - constraints
  - assumptions
  - unknowns
  - conflicts
  - risks
  - acceptance_summary
  - provenance
  - candidate_binding
  - human_review
  - limitations
  - non_grants
field_contract:
  product_spec_id: stable non-empty ID
  revision: exact non-empty revision
  maturity: DRAFT | HUMAN_ACCEPTED | STALE | REJECTED | DEFERRED
  exact_subject: non-empty bounded product subject
  governing_decision_bindings: non-empty list of decision ID, revision, and SHA-256
  source_intent_bindings: non-empty list of IntentRecord ID and source SHA-256
  target_users: non-empty list
  problem_and_jobs: non-empty list
  observable_outcomes: non-empty measurable list
  scope: explicit list; empty is invalid
  non_goals: explicit list; empty is invalid
  journeys: list of stable journey IDs
  feature_passport_refs: list of Feature Passport ID and revision; may be empty only before a feature boundary exists
  constraints: explicit list, including explicit NONE when intentionally empty
  assumptions: explicit list
  unknowns: explicit list
  conflicts: explicit list
  risks: explicit list
  acceptance_summary: stable acceptance IDs or explicit NOT_DEFINED
  provenance: every product claim has owner, locator, and freshness
  candidate_binding: exact revision and detached SHA-256/manifest
  human_review: disposition plus one exact decision request or NOT_RUN
  limitations: explicit list
  non_grants: must include IMPLEMENTATION, EXECUTION, VALIDATION, COMMIT, PUSH, MERGE, RELEASE
```

### 10.2 Shared `FeaturePassportRecord` schema

```yaml
schema_id: SCH-FEATURE-PASSPORT-001
schema_version: aos.feature-passport/v1
status: DRAFT
authority: PROPOSAL
additional_fields_policy: FORBID_UNDECLARED
required_fields:
  - feature_passport_id
  - revision
  - maturity
  - exact_subject
  - governing_product_spec_binding
  - governing_decision_bindings
  - actor
  - trigger
  - preconditions
  - inputs
  - outputs
  - behavior
  - states
  - side_effects
  - authority
  - failures
  - recovery
  - non_goals
  - acceptance_ids
  - negative_scenario_ids
  - provenance
  - candidate_binding
  - human_review
  - limitations
  - non_grants
field_contract:
  feature_passport_id: stable non-empty ID
  revision: exact non-empty revision
  maturity: DRAFT | HUMAN_ACCEPTED | STALE | REJECTED | DEFERRED
  exact_subject: one bounded feature subject
  governing_product_spec_binding: exact Product Spec ID, revision, and SHA-256
  governing_decision_bindings: list of decision ID, revision, and SHA-256
  actor: primary actor plus human decision owner
  trigger: non-empty observable trigger
  preconditions: explicit list
  inputs: typed inputs with provenance requirements
  outputs: typed outputs with owner and maturity
  behavior: deterministic operation or transition description
  states: initial, intermediate, terminal success, blocked, and failure states
  side_effects: read-only, write-capable, and forbidden effects
  authority: agent-may and human-only operations
  failures: non-empty list with detection and required effect
  recovery: non-empty list with retry/authorization boundary
  non_goals: explicit list
  acceptance_ids: non-empty stable ID list
  negative_scenario_ids: non-empty stable ID list
  provenance: every claim has owner, locator, and freshness
  candidate_binding: exact revision and detached SHA-256/manifest
  human_review: disposition plus one exact decision request or NOT_RUN
  limitations: explicit list
  non_grants: must include IMPLEMENTATION, EXECUTION, VALIDATION, COMMIT, PUSH, MERGE, RELEASE
```

Both schemas require unknown, absent, and explicit `NONE` values to remain distinct. A conforming DRAFT record is not human-accepted merely because it is schema-complete.

## 11. `CTR-004` — Minimal Hierarchy, Task Candidate, and Derived Queue

```yaml
contract_id: CTR-004
revision: R2
status: DRAFT_BLOCKED_UPSTREAM_ACCEPTANCE
roadmap_id: RMP-005
actor:
  primary: product builder or coding agent
  decision_owner: human task owner
trigger: The user requests one bounded Task candidate from accepted product and feature contracts.
preconditions:
  - exact Product Spec and Feature Passport are HUMAN_ACCEPTED
  - requirement, contract, acceptance, and scenario IDs are accepted and current
  - documentation output is authorized inside AOS-3/development-package/tasks/ in NMF13579/notebook
  - implementation repository is either exact and observed or explicitly UNASSIGNED
  - no deferred/optional capability is required
inputs:
  - accepted upstream ID graph and digests
  - requested user outcome
  - repository binding state and optional observation
  - logical allowed/forbidden scope constraints
  - dependency and blocker records
outputs:
  - zero or one portable Task Brief candidate
  - eligibility result with reasons
  - repository_binding_state PORTABLE_UNBOUND or REPOSITORY_BOUND
  - minimal parent/contribution links
  - rebuildable Queue projection
  - zero or one recommended next Task ID
states:
  - UPSTREAM_CHECK
  - INELIGIBLE
  - PORTABLE_TASK_CANDIDATE
  - REPOSITORY_BINDING_REQUIRED
  - REPOSITORY_BOUND_TASK_CANDIDATE
  - HUMAN_TASK_REVIEW_REQUIRED
  - ELIGIBLE_NOT_AUTHORIZED
side_effects:
  - write a DRAFT Task candidate only after contract acceptance and documentation authorization
  - when repository binding is UNASSIGNED, keep physical paths, commands, dependency versions, and execution eligibility UNASSIGNED/BLOCKED
  - never activate or execute the Task
authority:
  agent_may:
    - validate upstream binding, compile a candidate, and recommend one next item
  human_only:
    - accept Task scope, assign Risk Profile, activate, or authorize execution
failures:
  - BLOCKED_DRAFT_UPSTREAM
  - BLOCKED_STALE_UPSTREAM
  - BLOCKED_REPOSITORY_BOUND_FIELDS_WITHOUT_BINDING
  - BLOCKED_SCOPE_EXPANSION
  - BLOCKED_OPTIONAL_CAPABILITY_ADMISSION
  - FAIL_ORPHAN_OR_CIRCULAR_DEPENDENCY
recovery:
  - preserve the eligibility result
  - obtain exact contract decision
  - obtain a separate exact repository decision only before repository-bound enrichment or execution
  - rebuild Queue from current owners
  - never reuse a stale Task digest
non_goals:
  - full backlog scheduling
  - automatic activation or Risk assignment
  - execution journal inside Task
  - execution or Git authorization
executable_acceptance:
  - AC-CTR-004-01 a DRAFT or stale upstream yields no TASK artifact
  - AC-CTR-004-02 every Task field traces to accepted IDs; an unbound Task declares implementation_repository UNASSIGNED and repository-bound fields UNASSIGNED
  - AC-CTR-004-03 Queue rebuild is deterministic and has no independent authority
  - AC-CTR-004-04 optional/deferred features cannot enter the Core queue
  - AC-CTR-004-05 Task candidate contains no execution_authorized or Git-authorized field
```

Eligibility vocabulary:

```text
ELIGIBLE_FOR_PORTABLE_TASK_DRAFT
ELIGIBLE_FOR_REPOSITORY_BOUND_TASK_DRAFT
INELIGIBLE_DRAFT_UPSTREAM
INELIGIBLE_STALE_UPSTREAM
INELIGIBLE_REPOSITORY_BOUND_REQUEST_WITHOUT_BINDING
INELIGIBLE_BLOCKED_DEPENDENCY
INELIGIBLE_SCOPE_OR_OPTIONAL_ADMISSION
UNKNOWN_MATERIAL
```

## 12. `CTR-005` — Bounded Execution

```yaml
contract_id: CTR-005
revision: R1
status: DRAFT_FUTURE_BEHAVIOR
roadmap_id: RMP-006
actor:
  primary: coding agent or deterministic executor
  decision_owner: human execution owner
trigger: A human separately authorizes EXECUTE for one accepted Task, preview, subject, path set, and operation set.
preconditions:
  - exact Task is accepted and current
  - repository preflight and preview are current
  - human assigns RiskActionClass
  - execution authorization is valid, exact, unconsumed, and non-Git
  - recovery boundary exists
inputs:
  - Task Brief
  - repository/preflight binding
  - preview hash
  - HumanDecisionRecord for EXECUTE
  - idempotency key
outputs:
  - execution record
  - actual changed-path/effect inventory
  - journal or atomic-publication proof
  - focused checks and ResultEnvelope
  - one next action
states:
  - PREFLIGHT_REQUIRED
  - AUTHORIZATION_REQUIRED
  - READY_FOR_EXECUTE
  - EXECUTING
  - EXECUTION_STOPPED
  - EXECUTION_COMPLETED_UNVALIDATED
  - RECOVERY_REQUIRED
side_effects:
  - only exact authorized paths and operations
  - authorization consumption on first mutation boundary
  - no Commit, Push, Merge, Release, provider escalation, or next-stage transition
authority:
  agent_may:
    - verify, execute exact operations, stop, report, and preserve recovery state
  human_only:
    - assign Risk, authorize EXECUTE, expand scope, choose destructive recovery, authorize Git
failures:
  - BLOCKED_INVALID_OR_STALE_AUTHORIZATION
  - BLOCKED_PREVIEW_OR_SUBJECT_MISMATCH
  - BLOCKED_UNEXPECTED_PATH_OR_OPERATION
  - BLOCKED_CONCURRENT_MUTATION
  - FAIL_PARTIAL_WRITE
  - BLOCKED_UNKNOWN_OPERATION_OUTCOME
recovery:
  - stop mutation immediately
  - preserve journal, actual state, and authorization consumption
  - reconcile intended and observed effects
  - require human decision for unknown/destructive recovery
  - never retry by expanding scope or reusing stale authorization
non_goals:
  - automatic retry/correction
  - final validation or human acceptance
  - Git delivery or release
  - autonomous multi-task execution
executable_acceptance:
  - AC-CTR-005-01 no mutation occurs without exact human EXECUTE authorization
  - AC-CTR-005-02 only authorized paths and operations differ
  - AC-CTR-005-03 stale preview/HEAD/Task/auth is rejected before mutation
  - AC-CTR-005-04 interruption is detectable and recoverable
  - AC-CTR-005-05 terminal report stops before VALIDATE and Git
```

## 13. `CTR-006` — Validation, Evidence, and Human Decision

```yaml
contract_id: CTR-006
revision: R1
status: DRAFT_FUTURE_BEHAVIOR
roadmap_id: RMP-007
actor:
  primary: validator or reviewer
  decision_owner: human result owner
trigger: An exact candidate is frozen and a separate VALIDATE or REVIEW stage is authorized.
preconditions:
  - CandidateManifest is immutable and current
  - baseline, scope, environment, and check plan are bound
  - validation has no mutation authority
  - required and optional checks are distinguished
inputs:
  - frozen CandidateManifest
  - accepted acceptance/scenario IDs
  - validation matrix
  - environment/import provenance
outputs:
  - ResultEnvelope
  - Evidence records mapped to acceptance/scenarios
  - scope/diff reconciliation
  - compact review package
  - separate Human Decision request
states:
  - CANDIDATE_FROZEN
  - VALIDATING
  - VALIDATION_TERMINAL
  - HUMAN_REVIEW_REQUIRED
  - HUMAN_DECISION_RECORDED
side_effects:
  - Evidence/report publication outside the frozen subject only when authorized
  - zero candidate mutation
  - no correction, implementation, or Git action
authority:
  validator_may:
    - inspect, execute read-only checks, classify, and report
  human_only:
    - accept/reject/defer result and authorize any correction or Git action
failures:
  - FAIL_VALIDATION_MUTATED_SUBJECT
  - BLOCKED_STALE_OR_MOVING_CANDIDATE
  - BLOCKED_WRONG_ENVIRONMENT_OR_IMPORT
  - UNKNOWN_REQUIRED_CHECK_NOT_RUN
  - BLOCKED_EVIDENCE_APPROVAL_CONFLATION
recovery:
  - preserve failed Evidence and candidate identity
  - stop without correction
  - create a separate correction Task/revision
  - re-freeze and revalidate only after new authorization
non_goals:
  - generated acceptance
  - validation-time fixes
  - automatic retry or delivery
  - treating PASS as implementation/Git authority
executable_acceptance:
  - AC-CTR-006-01 every acceptance/scenario has Evidence or explicit NOT_RUN
  - AC-CTR-006-02 required NOT_RUN prevents PASS
  - AC-CTR-006-03 any candidate byte change invalidates validation
  - AC-CTR-006-04 review shows user impact, limitations, unknowns, and non-grants
  - AC-CTR-006-05 Human Decision actor/channel/subject/grants/non-grants are exact
```

## 14. `CTR-007` — Recovery, Resume, and Project Memory

```yaml
contract_id: CTR-007
revision: R1
status: DRAFT_FUTURE_BEHAVIOR
roadmap_id: RMP-008
actor:
  primary: user or new AI-agent session
  supporting: Project Memory/resume service
  decision_owner: human project owner
trigger: A session starts, work is interrupted, a failure occurs, or the user requests current status and one safe next action.
preconditions:
  - Project Memory owners are locatable
  - repository inspection is read-only
  - mutable facts will be refreshed
  - no hidden retry or mutation is permitted
inputs:
  - ProjectMemoryRecord and accepted decision bindings
  - actual repository/project observation
  - candidate, findings, checks, permissions, denied actions, and journals
outputs:
  - reconciled current-state record
  - stale/conflict/unknown classification
  - recovery options with side effects and authority
  - task-scoped Context Pack with inclusion reasons
  - exactly one safe next action
states:
  - MEMORY_LOAD
  - REPOSITORY_REFRESH
  - RECONCILING
  - CURRENT
  - STALE_OR_CONFLICT
  - RECOVERY_DECISION_REQUIRED
  - HUMAN_REVIEW_REQUIRED
side_effects:
  read_only_resume: none in source repository
  memory_update: separate authorized publication after reconciliation
  recovery: separate authorization based on exact actual state
authority:
  agent_may:
    - read, refresh, reconcile, classify, and propose one next action
  human_only:
    - resolve material conflicts, choose rollback/retry, authorize writes or Git
failures:
  - BLOCKED_MISSING_MEMORY_OWNER
  - BLOCKED_STALE_DECISION_OR_CANDIDATE
  - BLOCKED_INCOMPLETE_REPOSITORY_BINDING
  - BLOCKED_UNKNOWN_OPERATION_OUTCOME
  - BLOCKED_DERIVED_VIEW_AS_SOURCE
  - FAIL_RESUME_READ_ONLY_MUTATION
recovery:
  - preserve actual state and all journals
  - prefer repository observation for mutable facts
  - mark stale records rather than rewriting history
  - request one bounded human decision
  - retry only a newly authorized affected stage
non_goals:
  - autonomous self-heal or remediation
  - automatic lesson promotion
  - background indexing/provider calls
  - automatic Commit, Push, Merge, or Release
executable_acceptance:
  - AC-CTR-007-01 a new agent reconstructs stage, subject, blockers, permissions, and next action without chat
  - AC-CTR-007-02 changed HEAD/source hash makes affected memory stale
  - AC-CTR-007-03 read-only resume produces zero source-tree changes
  - AC-CTR-007-04 unknown operation outcome blocks retry pending reconciliation
  - AC-CTR-007-05 Context Pack lists every source and inclusion reason
```

## 15. Contract acceptance and Task boundary

This document does not self-accept any `CTR-*`. The human accepted every defined `CTR-001..007` and its exact acceptance/scenario subject through [`DEC-CONTRACT-001`](decisions/DEC-CONTRACT-001_Stage_C_Contract_Acceptance.md), bound to the frozen R4 candidate and accepted-subject digest.

```yaml
accepted_candidate_sha256: 00499af5d0f968481f0ed7e75c452bf74bf56eed380fd99d36a9a06dd8c54262
accepted_subject_manifest_sha256: 2e76304f5b53ce4b907eed060b67e4f1274f303cee05cdfb0eec559c21c6db3b
task_template: CREATED_DRAFT
task_graph: CREATED_DRAFT_SEVEN_NODES
task_briefs: [AOS3-DPKG-TASK-001, AOS3-DPKG-TASK-002]
graph_only_task_ids: [AOS3-DPKG-TASK-003, AOS3-DPKG-TASK-004, AOS3-DPKG-TASK-005, AOS3-DPKG-TASK-006, AOS3-DPKG-TASK-007]
new_draft_shared_schemas: [SCH-PRODUCT-SPEC-001, SCH-FEATURE-PASSPORT-001]
human_task_acceptance: NOT_RUN
future_execution_blocker: EXACT_IMPLEMENTATION_REPOSITORY_IS_UNASSIGNED
next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
