---
artifact_id: AOS3-DPKG-G2-OPT-001
artifact_type: ARCHITECTURE_OPTION_PACKAGE
package_id: AOS3-DEVELOPMENT-PACKAGE
package_revision: DRAFT-R14
revision: R2
status: DRAFT
authority: PROPOSAL
exact_subject: Decision-ready G2 options for implementation repository, architecture, topology, toolchain, Project Memory, provider/privacy, Human Decision authenticity, Risk Profile vocabulary, and compatibility
created: '2026-07-30'
human_acceptance: NOT_RUN
provenance:
  - ../00_Control_and_Source_Precedence.md
  - ../01_Product_and_Core_V1_Scope.md
  - ../02_User_Journeys_and_Workflows.md
  - ../../../docs/00_Core.md
  - ../../../docs/02_Architecture.md
  - ../research/RSR-001_AgentOS_Interview_and_Product_Spec.md
  - ../research/RSR-002_AOS_FARM_Decision_and_Recovery_Boundaries.md
upstream_links:
  - ../00_Control_and_Source_Precedence.md
  - ../01_Product_and_Core_V1_Scope.md
  - ../02_User_Journeys_and_Workflows.md
  - ../research/RSR-001_AgentOS_Interview_and_Product_Spec.md
  - ../research/RSR-002_AOS_FARM_Decision_and_Recovery_Boundaries.md
downstream_links: []
limitations:
  - Options and recommendation are agent synthesis, not human architecture decisions.
  - No implementation repository existence, toolchain availability, dependency compatibility, or runtime behavior was verified.
  - Reference repositories have authority NONE and were not used as target topology.
  - Human-assigned weights are intentionally absent.
implementation_repository: UNASSIGNED
implementation_authorization: NONE
git_authorization: NONE
---

# G2 Architecture Option Package

## 1. Purpose and non-approval boundary

This packet prepares `HUMAN_ARCHITECTURE_GATE_G2`. It does not select architecture or authorize implementation.

```text
Option package ≠ ADR
Recommendation ≠ human decision
Reference evidence ≠ target requirement
Architecture decision ≠ implementation authorization
Implementation repository decision ≠ Commit/Push authority
```

## 2. Why G2 is material

The accepted `A → B → C` sequence requires:

- durable Product Spec/Feature Passport identity;
- later Task compilation against accepted contracts;
- exact repository/project-state binding for safe resume;
- a human-authentic decision boundary;
- provider/privacy handling for raw domain input;
- portable agent adapters;
- deterministic validation and recovery.

These choices affect data ownership, security, portability, recovery, and implementation Tasks. An ADR boundary is therefore required.

## 3. Fixed constraints

The following are already authoritative or human-decided:

1. knowledge repository remains documentation-only;
2. implementation repository remains `UNASSIGNED` until G2;
3. Core v1 sequence is `A → B → C`, with A first;
4. Product Spec and Feature Passport have separate logical ownership;
5. contract-first, small vertical slice, manual cycle before automation;
6. exact human authority, source provenance, read-only validation, and Git separation;
7. optional capabilities cannot become Core dependencies by convenience;
8. target design is not a copy of AOS-FARM or AgentOS.

## 4. Evaluation criteria

Weights are `UNASSIGNED`; only the human may assign them.

| Criterion ID | Criterion |
|---|---|
| `G2-CRIT-001` | Comprehensible to a non-programmer/domain expert |
| `G2-CRIT-002` | Smallest path to Slice A observable outcome |
| `G2-CRIT-003` | Portable across agent environments |
| `G2-CRIT-004` | Exact source/candidate/decision binding |
| `G2-CRIT-005` | Recoverable and inspectable local state |
| `G2-CRIT-006` | Minimal provider/privacy exposure |
| `G2-CRIT-007` | Deterministic contracts and validation |
| `G2-CRIT-008` | Clear evolution path to Slices B and C |
| `G2-CRIT-009` | Low dependency/operations burden |
| `G2-CRIT-010` | Reversal or migration is bounded |

## 5. Coherent architecture bundles

### `G2-OPT-A` — Local-first portable core

Status: `RECOMMENDED_CANDIDATE_ONLY`

```yaml
implementation_repository:
  choice: NEW_DEDICATED_REPOSITORY
  exact_repository: HUMAN_INPUT_REQUIRED
architecture:
  style: MODULAR_MONOLITH_WITH_PORTS_AND_ADAPTERS
  runtime_shape: LOCAL_PROCESS
  primary_interface: CLI_AND_PORTABLE_TEXT_JSON_ARTIFACTS
toolchain:
  language: PYTHON_3_12_OR_NEWER
  dependency_policy: MINIMAL_PINNED_DEPENDENCIES
  distribution: LOCAL_PACKAGE_AND_CLI
project_memory:
  persistence: REPOSITORY_RELATIVE_MARKDOWN_YAML_JSON
  source_of_truth: VERSIONED_CONTRACT_FILES
  derived_indexes: REBUILDABLE
provider_privacy:
  default: LOCAL_ONLY_CORE
  external_provider: EXPLICIT_OPT_IN_ADAPTER
  sensitive_data: DENY_EXTERNAL_TRANSMISSION_UNTIL_EXPLICIT_POLICY
human_decision_authenticity:
  level: LOCAL_DECLARED_HASH_BOUND
  fields:
    - actor_reference
    - actor_role
    - decision_channel
    - exact_subject_hash
    - issued_at
    - grants
    - non_grants
  cryptographic_non_repudiation: false
risk_profile:
  vocabulary_option: G2-RISK-A_MINIMAL_ACTION_CLASSES
compatibility:
  target: GREENFIELD_CONTRACT_COMPATIBILITY_ONLY
  legacy_runtime_compatibility: false
```

Benefits:

- shortest path to first slice;
- state is human-readable and portable;
- easy exact hashing, diffing, review, and recovery;
- no database/service dependency;
- thin Codex/other-agent adapters.

Costs/risks:

- CLI/text UX may be less friendly for the first user;
- file concurrency and large-project query performance are limited;
- `LOCAL_DECLARED` decisions are honest but weakly authenticated;
- a later UI may require a new adapter and migration.

Reversal:

- keep schemas and ports stable;
- migrate file records into SQLite/service storage later;
- retain portable export as canonical interchange.

### `G2-OPT-B` — Local application with structured state

Status: `CANDIDATE`

```yaml
implementation_repository:
  choice: NEW_DEDICATED_REPOSITORY
  exact_repository: HUMAN_INPUT_REQUIRED
architecture:
  style: MODULAR_MONOLITH_WITH_PORTS_AND_ADAPTERS
  runtime_shape: LOCAL_APPLICATION
  primary_interface: LOCAL_WEB_OR_DESKTOP_UI_WITH_CLI_SUPPORT
toolchain:
  language: TYPESCRIPT_NODE_22
  dependency_policy: PINNED_UI_AND_SCHEMA_DEPENDENCIES
  distribution: LOCAL_APP_OR_PACKAGED_NODE_CLI
project_memory:
  persistence: LOCAL_SQLITE_WITH_PORTABLE_EXPORT
  source_of_truth: DATABASE_RECORDS_PLUS_IMMUTABLE_EXPORTS
  derived_indexes: REBUILDABLE
provider_privacy:
  default: LOCAL_STATE
  external_provider: EXPLICIT_PER_ACTION_OPT_IN
  sensitive_data: REDACTION_AND_USER_CONFIRMATION_REQUIRED
human_decision_authenticity:
  level: LOCAL_OS_OR_REPOSITORY_ACCOUNT_BOUND
  cryptographic_non_repudiation: OPTIONAL
risk_profile:
  vocabulary_option: G2-RISK-A_MINIMAL_ACTION_CLASSES
compatibility:
  target: GREENFIELD_WITH_PORTABLE_IMPORT_EXPORT
  legacy_runtime_compatibility: false
```

Benefits:

- stronger first-contact UX;
- structured queries and state transitions;
- better path to richer status/review surfaces;
- local operation preserves privacy.

Costs/risks:

- larger dependency and packaging surface;
- database/export ownership must be explicit;
- UI can create false authority if it becomes a competing Source of Truth;
- desktop/cross-platform packaging delays Slice A.

Reversal:

- retain portable export/import and domain ports;
- UI may be replaced without changing core contracts.

### `G2-OPT-C` — Collaborative service-first platform

Status: `CANDIDATE_NOT_RECOMMENDED_FOR_FIRST_SLICE`

```yaml
implementation_repository:
  choice: NEW_DEDICATED_REPOSITORY_OR_SERVICE_MONOREPO
  exact_repository: HUMAN_INPUT_REQUIRED
architecture:
  style: SERVICE_FIRST_MODULAR_PLATFORM
  runtime_shape: WEB_FRONTEND_API_AND_WORKER
  primary_interface: WEB_APPLICATION
toolchain:
  language: TYPESCRIPT_AND_OR_PYTHON
  dependency_policy: SERVICE_STACK
  distribution: HOSTED_DEPLOYMENT
project_memory:
  persistence: POSTGRES_OR_EQUIVALENT_SERVICE_DATABASE
  source_of_truth: AUTHENTICATED_SERVICE_RECORDS
  derived_indexes: REBUILDABLE
provider_privacy:
  default: HOSTED_POLICY_BOUND
  external_provider: MANAGED_CONNECTORS
  sensitive_data: ENCRYPTION_ACCESS_CONTROL_RETENTION_AND_AUDIT_REQUIRED
human_decision_authenticity:
  level: EXTERNAL_AUTHENTICATED
  cryptographic_non_repudiation: POLICY_DEPENDENT
risk_profile:
  vocabulary_option: G2-RISK-B_DIMENSIONAL_POLICY
compatibility:
  target: API_AND_ARTIFACT_MIGRATION
  legacy_runtime_compatibility: OPTIONAL_SEPARATE_DECISION
```

Benefits:

- multi-user collaboration and stronger authenticated decisions;
- centralized state, audit, and provider policy;
- natural path to SaaS/workbench capabilities.

Costs/risks:

- contradicts the smallest local-first path unless human priorities change;
- substantially larger security, privacy, operations, and deployment surface;
- network and service availability become first-slice dependencies;
- optional SaaS capability would become premature Core complexity.

Reversal:

- expensive; requires service-to-portable export guarantees from the start.

## 6. Decision-by-decision options

The human may accept one bundle or compose compatible choices.

### `DEC-ARCH-001` — Implementation repository

| Option | Description | Boundary |
|---|---|---|
| `G2-REPO-A` | New dedicated implementation repository | Recommended; exact owner/name required |
| `G2-REPO-B` | Existing repository explicitly selected by human | Must verify role, branch, state, and compatibility |
| `G2-REPO-C` | Change this notebook repository to mixed documentation/implementation role | Conflicts with current role; requires separate explicit role decision |

No repository is inferred from directory presence.

### `DEC-ARCH-002` — Architecture and physical topology

| Option | Description | Fit |
|---|---|---|
| `G2-ARCH-A` | Local modular monolith, ports/adapters, CLI/text surface | Best fit for Slice A and portability |
| `G2-ARCH-B` | Local modular monolith with SQLite and local UI | Better UX/state queries; more dependencies |
| `G2-ARCH-C` | Service-first web/API platform | Strong collaboration/auth; excessive first-slice burden |

### `DEC-ARCH-003` — Language/toolchain/dependencies

| Option | Description | Trade-off |
|---|---|---|
| `G2-TOOL-A` | Python 3.12+, CLI, minimal pinned schema/serialization dependencies | Fast contract tooling; later UI adapter needed |
| `G2-TOOL-B` | TypeScript/Node 22, shared types, local UI/CLI | Strong UI path; packaging/dependency surface |
| `G2-TOOL-C` | Python core plus TypeScript UI | Flexible but premature dual-stack complexity |

Exact dependencies remain unselected until the toolchain option is accepted and verified in the implementation repository.

### `DEC-ARCH-004` — Project Memory persistence

| Option | Description | Trade-off |
|---|---|---|
| `G2-MEM-A` | Repository-relative Markdown/YAML/JSON with schemas and hashes | Human-readable, portable; limited concurrency/query |
| `G2-MEM-B` | Local SQLite plus canonical portable export | Structured state; dual-owner risk must be resolved |
| `G2-MEM-C` | Authenticated service database plus export | Collaboration/auth; operations and privacy burden |

Whichever option is selected must own repository identity, accepted decisions, stage/candidate, findings, blockers, checks, permission state, and one next action.

### `DEC-ARCH-005` — Provider/privacy boundary

| Option | Description | Trade-off |
|---|---|---|
| `G2-PRIV-A` | Local-only Core; no external provider call | Strong privacy and determinism; no built-in model capability |
| `G2-PRIV-B` | Explicit opt-in per provider action with redaction/preview | Useful AI integration; policy and consent required |
| `G2-PRIV-C` | Hosted managed provider layer | Central controls; largest security/compliance surface |

External content remains untrusted under every option.

### `DEC-ARCH-006` — Human Decision authenticity

| Option | Description | Honest claim |
|---|---|---|
| `G2-AUTH-A` | `LOCAL_DECLARED_HASH_BOUND` | Actor/channel declared; exact subject bound; no strong authentication |
| `G2-AUTH-B` | `REPOSITORY_ACCOUNT_BOUND` | Decision linked to authenticated repository account or signed record |
| `G2-AUTH-C` | `EXTERNAL_AUTHENTICATED` | Identity/session authenticated by dedicated service |

Minimum required fields under every option: decision ID/type/value, actor reference/role, authenticity level, channel, exact candidate/subject binding, time, grants, non-grants, expiry/staleness, and consumption when applicable.

### `DEC-ARCH-007` — Risk Profile vocabulary

#### `G2-RISK-A` — Minimal action classes

```text
UNASSIGNED
READ_ONLY
REVERSIBLE_WRITE
PROTECTED_WRITE
DESTRUCTIVE_OR_PUBLISHING
```

Human assigns the profile. Deterministic tooling may propose a minimum class and explain the dimensions.

#### `G2-RISK-B` — Dimensional policy

Record separate dimensions:

```text
filesystem | data | network | provider | authority | Git | destructive | external-content
```

Human selects the resulting treatment. More precise, but more complex for first use.

#### `G2-RISK-C` — Legacy-compatible labels

```text
LOW_RISK_FAST
MEDIUM_RISK_GUIDED
HIGH_RISK_PROTECTED
DESTRUCTIVE_OR_CANONICAL
```

Use only if a separately accepted compatibility requirement justifies importing the historical vocabulary.

### `DEC-ARCH-008` — Compatibility

| Option | Description | Trade-off |
|---|---|---|
| `G2-COMP-A` | Greenfield contracts; portable import/export only | Smallest target; recommended |
| `G2-COMP-B` | Compatibility with selected legacy artifact formats | Bounded migration value; mapping/fixtures required |
| `G2-COMP-C` | Broad CLI/runtime compatibility | High cost and legacy coupling; separate justification required |

## 7. Recommendation

```yaml
recommendation:
  bundle: G2-OPT-A
  repository: G2-REPO-A
  architecture: G2-ARCH-A
  toolchain: G2-TOOL-A
  project_memory: G2-MEM-A
  provider_privacy: G2-PRIV-A
  human_decision_authenticity: G2-AUTH-A
  risk_profile: G2-RISK-A
  compatibility: G2-COMP-A
recommendation_status: CANDIDATE_ONLY
human_decision: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
```

Reasoning:

- aligns with the accepted first slice and canonical “small vertical slice before platform” principle;
- minimizes operational and provider dependencies;
- keeps portable artifacts inspectable by humans and agents;
- supports exact hashing, read-only validation, and bounded recovery;
- leaves UI, database, stronger authentication, and hosted operation as reversible later decisions.

Primary limitation: the first user may need a thin conversational/agent adapter because CLI/text alone is not an ideal direct interaction surface.

## 8. Reference findings used and rejected

Used as non-authoritative constraints:

- preserve input and missing/unknown semantics from [`RSR-001`](../research/RSR-001_AgentOS_Interview_and_Product_Spec.md);
- separate product approval from operational readiness;
- bind Human Decisions to actor/channel/subject/grants/non-grants from [`RSR-002`](../research/RSR-002_AOS_FARM_Decision_and_Recovery_Boundaries.md);
- reject agent-assigned Risk Profile and candidate approval claims;
- require architecture options and human weights.

Rejected as target defaults:

- duplicate lifecycle owners;
- wholesale AgentOS Product Spec lifecycle;
- AOS-FARM Risk Profile labels without compatibility need;
- AOS-FARM topology and milestone system;
- minimal three-heading handoff template;
- any default stack selected by reference occurrence.

## 9. G2 acceptance payload

Every field is required. A custom combination must explain incompatibilities.

```yaml
gate_id: HUMAN_ARCHITECTURE_GATE_G2
candidate:
  package_revision: DRAFT-R2
  aggregate_sha256: TO_BE_COMPUTED_AFTER_STAGE_B_VALIDATION
decision:
  selected_bundle: G2-OPT-A | G2-OPT-B | G2-OPT-C | CUSTOM
  implementation_repository:
    option: G2-REPO-A | G2-REPO-B | G2-REPO-C
    exact_repository:
  architecture_option: G2-ARCH-A | G2-ARCH-B | G2-ARCH-C
  toolchain_option: G2-TOOL-A | G2-TOOL-B | G2-TOOL-C
  project_memory_option: G2-MEM-A | G2-MEM-B | G2-MEM-C
  provider_privacy_option: G2-PRIV-A | G2-PRIV-B | G2-PRIV-C
  human_decision_authenticity_option: G2-AUTH-A | G2-AUTH-B | G2-AUTH-C
  risk_profile_option: G2-RISK-A | G2-RISK-B | G2-RISK-C
  compatibility_option: G2-COMP-A | G2-COMP-B | G2-COMP-C
  interaction_surface:
  accepted_constraints: []
  accepted_tradeoffs: []
human_disposition: ACCEPT | NEEDS_CHANGES | REJECT | DEFER
implementation_authorization: NONE
git_authorization: NONE
```

## 10. Blockers

Until G2:

- implementation repository remains `UNASSIGNED`;
- documents `03..07` remain uncreated;
- implementation-grade runtime/data/security contracts remain blocked;
- no Task template or Task Brief may be created;
- no architecture option is promoted;
- no dependency may be installed;
- no implementation or Git action is authorized.

## 11. One next action

```yaml
historical_next_action_at_option_time: HUMAN_ARCHITECTURE_GATE_G2
current_package_next_required_action: AUTHORIZE_SEPARATE_VALIDATE_DRAFT_R14
stop: true
```
