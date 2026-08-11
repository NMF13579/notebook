---
document_id: AOS3-IMPLEMENTATION-READY-DRAFT-R1
status: DRAFT
authority: NONE
review_status: READY_FOR_HUMAN_REVIEW
source_repository: NMF13579/notebook
target_repository: NMF13579/AOS-3
target_visibility: PRIVATE_DURING_DEVELOPMENT
git_history_strategy: CLEAN
license_status: DEFER_UNTIL_PUBLIC_DISTRIBUTION
runtime_implementation: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
---

# AOS-3 — Implementation-ready draft

## 1. Назначение и граница

Этот документ является единым reviewable blueprint для создания нового
репозитория `NMF13579/AOS-3`. Он определяет целевую структуру, начальный exact
состав переносимого продукта `aos/`, root payload, Project Memory templates,
runtime architecture, CLI boundary, data contracts, algorithms, проверки и
порядок реализации.

Документ не создаёт remote repository, не переносит файлы, не реализует
runtime и не разрешает Git operations. После human review он может стать
implementation input; само присутствие файла не является authorization.

```yaml
documentation_construction_authority: CURRENT_HUMAN_INSTRUCTION
runtime_implementation: NOT_RUN
target_repository_creation: NOT_RUN
commit: NOT_RUN
push: NOT_RUN
merge: NOT_RUN
release: NOT_RUN
```

## 2. Bound decisions and sources

### 2.1 Current human decisions

```yaml
migration_map:
  decision: ACCEPT
  sha256: 10b46fe19a6559e5a5ea53ecf414987fa1a97af18046a285ecfe9e86e221c86b
repository:
  identity: NMF13579/AOS-3
  visibility: PRIVATE_DURING_DEVELOPMENT
  git_history: CLEAN
  license: DEFER_UNTIL_PUBLIC_DISTRIBUTION
architecture:
  style: LOCAL_MODULAR_MONOLITH
  language: PYTHON_3_12_PLUS
  dependency_policy: MINIMAL_PINNED
  project_memory: REPOSITORY_RELATIVE_MARKDOWN_YAML_JSON
  privacy_default: LOCAL_ONLY
  compatibility: GREENFIELD
engineering_autonomy:
  exact_aos_inventory: AGENT_OWNED_REVERSIBLE_DESIGN
  root_payload: AGENT_OWNED_REVERSIBLE_DESIGN
  project_templates: AGENT_OWNED_REVERSIBLE_DESIGN
  internal_how: AGENT_OWNED_REVERSIBLE_DESIGN
```

### 2.2 Exact source bindings

| Source | Bytes | SHA-256 | Use |
|---|---:|---|---|
| `workspace/AOS3_NOTEBOOK_MIGRATION_MAP.md` | 150795 | `10b46fe19a6559e5a5ea53ecf414987fa1a97af18046a285ecfe9e86e221c86b` | accepted source-to-target classification and findings |
| `workspace/AOS3_REPOSITORY_ARCHITECTURE_AND_MIGRATION_SPEC.md` | 29895 | `44f495d70c9482192b3f374120198351d11d717c1e348d5c270c7a394ff74839` | product-in-place topology and portability contracts |
| `workspace/AOS3_ROOT_AGENTS_CANDIDATE.md` | 16074 | `e89351a85f191a964d6a33ab7311685c7bee28c57c04656ddcd3824fd3d259e7` | exact future root agent rules |
| `AOS/portable/MANIFEST.txt` | 1015 | `1e3746b4bb6a326d9e93f805cb4ebe8a233c367976189aae1c0d385cde261901` | accepted portable documentation seed |
| `workspace/AOS_DOCUMENTATION_X1/CANDIDATE_MANIFEST.txt` | 5535 | `1f0d12c3328348126a5882f05e52a512157075e852993018ffb023cd979bf42d` | accepted FTR-001/FTR-003 contracts |

The X1 human decision selects:

- `X1-DR-001: A`: Product Spec owns cross-feature facts; Feature Passports own
  feature-specific behavior and link to Product Spec.
- `X1-DR-002: A`: the first Product Runtime slice is FTR-001 from human request
  to a reviewable, human-confirmed Intent Record.

Current canonical `docs/00_Core.md` through `docs/06_Features.md` remain the
source owners for identity, product, architecture, development semantics,
lessons, references and feature dossiers until adapted target owners are
reviewed in AOS-3.

## 3. Delivery outcome

The first complete AOS-3 development candidate must provide:

1. a dedicated repository for developing AOS itself;
2. a directly maintained portable product under `aos/`;
3. an installable Python package and CLI with no network dependency;
4. the accepted AOS documentation and workflows inside the product;
5. an exact root payload supporting manual and preview-first automatic install;
6. a non-empty `project/` knowledge tree owned by the target project;
7. a working FTR-001 vertical slice;
8. deterministic manifest, schema, self-test and isolated-copy checks;
9. root developer documentation, research and tests that are not runtime
   dependencies of `aos/`.

Not included in the first candidate:

- SaaS, hosted service, database or required external provider;
- automatic Commit, Push, Merge or Release;
- mandatory multi-agent orchestration;
- legacy-runtime compatibility or archive import;
- UI, marketplace, plugins or domain-specific Medical/Design behavior;
- automatic overwrite of user-owned root or `project/` files.

## 4. Target repository architecture

```text
AOS-3/
├── AGENTS.md
├── README.md
├── CHANGELOG.md
├── .gitignore
├── .editorconfig
├── .python-version
├── pyproject.toml
├── requirements-dev.lock
├── docs/
│   ├── README.md
│   ├── product/
│   ├── architecture/
│   ├── development/
│   └── decisions/
├── development/
│   ├── README.md
│   ├── drafts/
│   ├── research/
│   ├── audits/
│   └── fixtures/
├── tests/
│   ├── contracts/
│   ├── portability/
│   ├── installation/
│   └── integration/
├── tools/
│   ├── build_manifest.py
│   └── isolated_product_test.py
└── aos/
```

`LICENSE` is intentionally absent from the private-development candidate. It
becomes mandatory before public distribution. `.github/` is absent until a
working local test flow demonstrates which automation is useful.

### 4.1 Fact ownership

| Fact class | Owner |
|---|---|
| AOS product problem, users and observable behavior | `docs/product/` |
| AOS system and portable-product architecture | `docs/architecture/` and accepted ADRs |
| AOS development and release rules | `docs/development/` |
| Current shipped product behavior | exact `aos/` version and manifest |
| Working research and migration evidence | `development/` with authority `NONE` |
| Product test evidence | exact test result bound to an `aos/` identity |
| Installed project facts | target repository `project/` |
| Human decision | exact human-originated decision record |
| Git state | fresh repository observation |

## 5. Root repository file contracts

| Path | Purpose | Initial source or construction rule |
|---|---|---|
| `AGENTS.md` | cold-agent routing, anti-bureaucracy, autonomy and safety | byte-preserving placement from `workspace/AOS3_ROOT_AGENTS_CANDIDATE.md` |
| `README.md` | repository purpose, local setup, navigation and product isolation command | adapt from accepted repository specification |
| `CHANGELOG.md` | user-visible product changes by version | create with `Unreleased`; no false release history |
| `.gitignore` | Python caches, virtual environments, build/test output and local secrets | minimal explicit patterns |
| `.editorconfig` | UTF-8, LF, final newline and whitespace defaults | deterministic cross-editor baseline |
| `.python-version` | local runtime selection | `3.12` major/minor baseline |
| `pyproject.toml` | root development tools only | no runtime dependency for copied `aos/` |
| `requirements-dev.lock` | exact root test/lint dependencies | generated during implementation from the closed dev dependency set |
| `docs/README.md` | canonical owner map | link, do not duplicate facts |
| `development/README.md` | DRAFT/reference boundary | state authority `NONE` and promotion rule |
| `tools/build_manifest.py` | deterministic product manifest builder | root development tool; never required by installed product |
| `tools/isolated_product_test.py` | copy-only portability harness | executes against a temporary clean repository |

Root `pyproject.toml` may declare only developer dependencies needed for tests,
lint and packaging. Product runtime dependencies are declared independently by
`aos/pyproject.toml`.

### 5.1 Initial non-product path set

The first target candidate contains these additional tracked paths. Working
directories are created only when used; empty directory placeholders are not
required.

| Path | Construction source |
|---|---|
| `docs/README.md` | target owner and navigation map |
| `docs/product/00_CORE.md` | ADAPT from `docs/00_Core.md` |
| `docs/product/01_PRODUCT.md` | ADAPT from `docs/01_Product.md` |
| `docs/product/06_FEATURES.md` | ADAPT from `docs/06_Features.md` |
| `docs/architecture/02_SYSTEM_ARCHITECTURE.md` | ADAPT from `docs/02_Architecture.md` plus accepted current decisions |
| `docs/architecture/PORTABLE_PRODUCT_ARCHITECTURE.md` | derive from the accepted repository specification and this blueprint |
| `docs/architecture/REPOSITORY_ARCHITECTURE_AND_MIGRATION.md` | ADAPT accepted AOS-3 specification and close its stored status gap |
| `docs/development/03_DEVELOPMENT.md` | ADAPT from `docs/03_Development.md` and root anti-bureaucracy rules |
| `docs/development/TEST_STRATEGY.md` | target contract, portability, installation and integration matrix |
| `docs/decisions/README.md` | target decision owner and supersession rules |
| `docs/decisions/AOS3_FOUNDATION_DECISIONS.md` | repository, architecture, privacy, memory and compatibility decisions |
| `development/README.md` | DRAFT/reference boundary and on-demand directory rules |
| `development/migration/NOTEBOOK_MIGRATION_MAP.md` | exact accepted map copied as provenance, not runtime dependency |
| `tests/contracts/test_contracts.py` | schemas, enums, authority and result semantics |
| `tests/portability/test_isolated_product.py` | copy-only product operation |
| `tests/installation/test_installation.py` | preview, conflicts, apply, update and removal plan |
| `tests/integration/test_intent_flow.py` | FTR-001 end-to-end outcome |
| `tools/build_manifest.py` | deterministic product manifest builder |
| `tools/isolated_product_test.py` | disposable clean-repository harness |

No root audit/controller package is created. Additional `development/`
subdirectories appear only when a real draft, research item, audit or fixture
needs them.

## 6. Exact initial `aos/` inventory

The following is the closed initial product path set. Adding or removing a path
changes the product candidate identity and requires manifest regeneration.

### 6.1 Entry, package and accepted documentation

| Path | Role |
|---|---|
| `aos/AGENTS.md` | package-local agent routing and portability boundary |
| `aos/README.md` | product overview and installation choices |
| `aos/START_HERE.md` | primary human/agent entrypoint |
| `aos/ROOT_INSTALL_GUIDE.md` | manual and automatic root-payload contract |
| `aos/VERSION` | plain SemVer product version; initial candidate `0.1.0-dev` |
| `aos/MANIFEST.txt` | byte count and SHA-256 for every product file except itself |
| `aos/ROOT_PAYLOAD.yaml` | exact payload path, ownership and update policy records |
| `aos/pyproject.toml` | independently installable Python distribution and `aos` CLI |
| `aos/requirements.lock` | exact runtime dependency closure |
| `aos/docs/README.md` | portable documentation owner map |
| `aos/docs/00_PROJECT_CORE.md` | adapted portable core |
| `aos/docs/01_PRODUCT_MODEL.md` | adapted product model |
| `aos/docs/02_ARCHITECTURE_CONTRACTS.md` | adapted portable architecture contracts |
| `aos/docs/03_ENGINEERING_WORKFLOW.md` | adapted engineering workflow |
| `aos/docs/04_FEATURE_SPECIFICATIONS.md` | feature contracts and dispositions |
| `aos/docs/05_USER_JOURNEYS_AND_UX.md` | journeys and interaction expectations |
| `aos/docs/06_PROJECT_ROADMAP.md` | phased product scope without runtime readiness inflation |
| `aos/docs/07_DECISION_REGISTER.md` | product and architecture decisions |
| `aos/docs/08_TRACEABILITY.md` | intent-to-acceptance trace graph |

### 6.2 Stable workflows

| Path | Role |
|---|---|
| `aos/workflows/README.md` | workflow selection and common invariants |
| `aos/workflows/INTAKE.md` | FTR-001 request-to-reviewable-intent algorithm |
| `aos/workflows/PRODUCT_DEFINITION.md` | FTR-003 Product Spec and Feature Passport algorithm |
| `aos/workflows/TASK_EXECUTION.md` | bounded implementation and focused correction flow |
| `aos/workflows/REVIEW_AND_DECISION.md` | result, evidence and human-decision separation |
| `aos/workflows/CONTINUATION_AND_RECOVERY.md` | current state, interruption and bounded recovery |

### 6.3 Templates and schemas

| Path | Role |
|---|---|
| `aos/templates/README.md` | template usage and ownership rules |
| `aos/templates/intent_record.yaml` | new Intent Record candidate |
| `aos/templates/product_spec.md` | cross-feature Product Spec owner |
| `aos/templates/feature_passport.md` | feature-specific observable behavior |
| `aos/templates/architecture_decision.md` | decision-ready ADR without generated selection |
| `aos/templates/task_brief.md` | bounded implementation input |
| `aos/templates/evidence_record.yaml` | subject-bound technical evidence |
| `aos/templates/human_decision.yaml` | local exact-subject decision record |
| `aos/templates/current.md` | current state and one next action |
| `aos/templates/lesson.md` | failure, cause, correction and regression case |
| `aos/schemas/README.md` | schema ownership and versioning |
| `aos/schemas/intent-record.schema.json` | strict Intent Record structure |
| `aos/schemas/product-spec.schema.json` | machine-readable Product Spec frontmatter |
| `aos/schemas/feature-passport.schema.json` | Feature Passport identity and state fields |
| `aos/schemas/decision-record.schema.json` | human-decision binding and non-grants |
| `aos/schemas/task-brief.schema.json` | bounded task fields |
| `aos/schemas/evidence-record.schema.json` | evidence subject and check results |
| `aos/schemas/current-state.schema.json` | Project Memory continuity fields |

### 6.4 Runtime package

| Path | Responsibility |
|---|---|
| `aos/src/aos/__init__.py` | version and public package boundary |
| `aos/src/aos/__main__.py` | `python -m aos` entrypoint |
| `aos/src/aos/cli.py` | argparse command routing and stable exit envelopes |
| `aos/src/aos/domain/enums.py` | closed status, claim, authority and ownership vocabularies |
| `aos/src/aos/domain/records.py` | immutable internal record models |
| `aos/src/aos/domain/validation.py` | semantic invariants independent of I/O |
| `aos/src/aos/application/intake.py` | Intent Record scaffold, validation and review operations |
| `aos/src/aos/application/decisions.py` | exact-subject local decision recording and validation |
| `aos/src/aos/application/status.py` | repository-derived current state projection |
| `aos/src/aos/application/installation.py` | preview/apply root payload operations |
| `aos/src/aos/application/verification.py` | manifest, links, schemas and package checks |
| `aos/src/aos/ports/files.py` | confined read/write and atomic-publication interface |
| `aos/src/aos/ports/repository.py` | read-only repository observation interface |
| `aos/src/aos/adapters/filesystem.py` | pathlib-based local file adapter |
| `aos/src/aos/serializers/yaml_json.py` | safe YAML and deterministic JSON serialization |
| `aos/src/aos/py.typed` | typed-package marker |

### 6.5 Product tools, adapters, examples and self-test

| Path | Role |
|---|---|
| `aos/tools/README.md` | portable tool usage |
| `aos/tools/aos.py` | source-checkout CLI wrapper |
| `aos/tools/verify_package.py` | stdlib bootstrap verification before install |
| `aos/adapters/README.md` | adapter boundary and no-authority rule |
| `aos/adapters/codex/AGENTS.md` | Codex routing to workflows, templates and `project/` |
| `aos/adapters/generic/AGENT_GUIDE.md` | environment-neutral agent contract |
| `aos/examples/README.md` | examples are non-authoritative fixtures |
| `aos/examples/intent/example-request.txt` | minimal input example |
| `aos/examples/intent/expected-intent.yaml` | expected reviewable shape, never current project truth |
| `aos/selftest/README.md` | copied-product test instructions |
| `aos/selftest/test_manifest.py` | exact manifest and path-set checks |
| `aos/selftest/test_links.py` | internal-link and parent-dependency checks |
| `aos/selftest/test_schemas.py` | schema/template validity checks |
| `aos/selftest/test_portability.py` | isolated-copy and forbidden-path checks |

### 6.6 Root installation payload

| Path | Role |
|---|---|
| `aos/root/AGENTS.md` | installed repository routing to `aos/` and `project/` |
| `aos/root/START_HERE.md` | installed human-facing entrypoint |
| `aos/root/project/README.md` | Project Memory navigation |
| `aos/root/project/CURRENT.md` | current status, blockers and one next action |
| `aos/root/project/00_PROJECT.md` | project identity, outcome, scope and constraints |
| `aos/root/project/01_PRODUCT.md` | users, problems, journeys and requirements |
| `aos/root/project/02_ARCHITECTURE.md` | target project architecture and material decisions |
| `aos/root/project/03_DEVELOPMENT.md` | project-specific engineering and test rules |
| `aos/root/project/intents/README.md` | Intent Record location and naming |
| `aos/root/project/features/README.md` | Feature Passport location and ownership |
| `aos/root/project/decisions/README.md` | product and architecture decision records |
| `aos/root/project/tasks/README.md` | bounded current and historical task inputs |
| `aos/root/project/evidence/README.md` | durable subject-bound check results |
| `aos/root/project/research/README.md` | targeted findings with provenance |
| `aos/root/project/lessons/README.md` | failures, regressions and reusable lessons |

The closed initial product inventory contains 88 files. `MANIFEST.txt` records
the other 87 paths in ascending UTF-8 byte order as:

```text
<sha256><two spaces><byte_count><two spaces><relative_path><LF>
```

The manifest excludes itself and rejects symlinks, duplicate paths, absolute
paths, CRLF and unrecorded regular files.

## 7. Dependency contract

### Runtime

The allowed initial external runtime dependency set is closed to:

- `PyYAML` for safe YAML parsing and emission;
- `jsonschema` for executable JSON Schema validation.

The standard library owns CLI parsing, hashing, JSON, paths, temporary files,
subprocess control and immutable data structures. No HTTP, database, Git write,
LLM provider or telemetry dependency is allowed in the first candidate.

Exact direct and transitive versions are pinned in `aos/requirements.lock`
during implementation. Updating a version is reversible HOW only when the
closed dependency names, Python support, local-only boundary and full product
tests remain unchanged.

### Development

Root development dependencies are limited initially to `pytest` and `ruff`,
with exact versions in `requirements-dev.lock`. Additional tools require a
demonstrated check that cannot be implemented clearly with the current set.

## 8. Runtime architecture

```text
CLI and agent adapters
        ↓
application operations
        ↓
domain records and invariants
        ↓
ports
        ↓
local filesystem and repository observers
```

Dependency direction is inward. Domain modules import no CLI, filesystem,
provider or repository implementation. Adapters may translate I/O but cannot
create product truth, human decisions or permissions.

### Component contracts

| Component | Owns | Must not own |
|---|---|---|
| `domain` | record shapes, enums and pure invariants | paths, user prompts, Git or file writes |
| `application.intake` | creation and validation of Intent candidates | human confirmation or product scope expansion |
| `application.decisions` | validation and storage of explicit local decision records | decision value inference |
| `application.status` | derived current view from owned records | independent product truth |
| `application.installation` | root-payload plan, conflict classification and bounded apply | unpreviewed writes or project overwrite |
| `application.verification` | deterministic checks and result envelope | correction or approval |
| `ports` | required I/O capabilities | concrete environment assumptions |
| `adapters` | confined environment access | domain policy or hidden state |

## 9. Project Memory and data layout

After installation, project-owned state is repository-relative:

```text
project/
├── CURRENT.md
├── 00_PROJECT.md
├── 01_PRODUCT.md
├── 02_ARCHITECTURE.md
├── 03_DEVELOPMENT.md
├── intents/INT-<UTC>-<suffix>.yaml
├── features/FTR-<number>.md
├── decisions/DEC-<UTC>-<suffix>.yaml
├── tasks/TASK-<UTC>-<suffix>.md
├── evidence/EVD-<UTC>-<suffix>.yaml
├── research/RSR-<UTC>-<suffix>.md
└── lessons/LES-<UTC>-<suffix>.md
```

IDs use UTC basic timestamps plus eight lowercase hexadecimal random
characters. IDs are locators, not authority. Exact subject identity is raw-byte
SHA-256 computed outside the subject to avoid self-reference.

### 9.1 Intent Record v1

```yaml
schema_version: aos.intent/v1
record_id: INT-YYYYMMDDTHHMMSSZ-8hex
revision: 1
state: RECEIVED
actor:
  reference: human supplied identifier or UNKNOWN
  role: PRODUCT_OWNER
original_request: exact preserved input
problem: null
desired_outcome: null
context: []
constraints: []
non_goals: []
assumptions: []
unknowns: []
sensitive_flags: []
source_bindings: []
limitations: []
next_route: CLARIFY
```

Allowed states are `RECEIVED`, `CLARIFYING`, `REVIEWABLE`, `CONFIRMED` and
`DEFERRED`. `CONFIRMED` is valid only when a separate decision record binds the
exact Intent Record bytes.

Every unknown contains `id`, `statement`, `affected_boundary` and
`resolution_route`. Every assumption includes `statement`, `source_class` and
`confirmation_status`.

### 9.2 Decision Record v1

```yaml
schema_version: aos.decision/v1
decision_id: DEC-YYYYMMDDTHHMMSSZ-8hex
decision_type: INTENT_CONFIRMATION
decision_value: CONFIRM
actor_reference: explicit local actor reference
actor_role: PRODUCT_OWNER
authenticity_level: LOCAL_DECLARED_EXACT_SUBJECT
decision_channel: declared channel
subject:
  path: project/intents/INT-....yaml
  bytes: positive integer
  sha256: 64 lowercase hex
issued_at: RFC3339 UTC
grants:
  - INTENT_CONFIRMATION_FOR_EXACT_SUBJECT
non_grants:
  - PRODUCT_SCOPE_EXPANSION
  - IMPLEMENTATION
  - COMMIT
  - PUSH
  - MERGE
  - RELEASE
```

The runtime validates this record but cannot generate a decision value from
Evidence, a PASS, agent text or file presence.

### 9.3 CURRENT.md

`CURRENT.md` is a rebuildable continuity view containing:

- exact repository observation timestamp;
- active project and accepted subject references;
- current bounded task, if any;
- blockers and affected boundaries;
- checks actually run and material `NOT_RUN`;
- permissions;
- exactly one next action when one is required.

It does not replace Product, Feature, Decision or Evidence owners.

### 9.4 Write and recovery rules

- Read before write and recheck the destination immediately before mutation.
- Confine all relative paths beneath the selected target root after symlink
  resolution.
- Publish one file through a temporary sibling, flush and atomic replace.
- Existing project-owned files are never replaced by install/update.
- A multi-file apply records planned operations and completed operations in the
  returned result; interruption stops without automatic retry.
- A stale preview is rejected and must be recomputed.
- Validation is read-only.

## 10. Initial CLI contract

| Command | Default effect | Observable output |
|---|---|---|
| `aos --help` | read-only | command summary; no filesystem writes |
| `aos verify-package [PATH]` | read-only | manifest, inventory, links and schema result |
| `aos doctor --target PATH` | read-only | Python, dependency, path and conflict readiness |
| `aos install --target PATH` | read-only preview | ordered root-payload operation plan |
| `aos install --target PATH --apply` | bounded write | applied, skipped, conflicted and preserved paths |
| `aos update --source PATH --target PATH` | read-only preview | product-file changes, local modifications and rollback boundary |
| `aos update --source PATH --target PATH --apply` | bounded product replacement | verified new product or restored prior product on failure |
| `aos uninstall --target PATH` | read-only only | exact manual removal plan preserving root and `project/` |
| `aos status --target PATH` | read-only | concise current state and next action |
| `aos intent new --target PATH --input FILE_OR_DASH` | one create-only write | source-preserving Intent candidate path and identity |
| `aos intent validate PATH` | read-only | schema and semantic findings |
| `aos intent review PATH` | read-only | original, synthesis, assumptions, unknowns and route |
| `aos decision record --target PATH --subject PATH --value CONFIRM` | one create-only write | exact local decision record; no downstream authorization |
| `aos selftest` | read-only except temporary directory | focused product self-test results |

All commands support `--format text|json`. Text is concise and human-facing;
JSON uses one stable result envelope. Default writes are denied except for
commands whose name and arguments explicitly request a bounded create/apply.

Exit codes:

| Code | Meaning |
|---:|---|
| `0` | requested operation completed and all required checks passed |
| `2` | invalid input or schema |
| `3` | path, ownership or source conflict |
| `4` | authorization required or insufficient |
| `5` | unavailable environment or dependency |
| `6` | partial write requiring recovery |
| `7` | unexpected internal failure |

No command prints credentials, raw sensitive input beyond explicitly requested
review, or a traceback by default.

## 11. Product algorithms

### 11.1 Manifest verification

```text
read MANIFEST.txt as UTF-8 LF records
→ reject duplicate, absolute, escaping or unsorted paths
→ enumerate regular product files excluding MANIFEST.txt
→ reject symlinks and unexpected/missing paths
→ recompute bytes and SHA-256
→ compare every record
→ return one result without mutation
```

### 11.2 Root installation

```text
verify exact product manifest
→ load and validate ROOT_PAYLOAD.yaml
→ observe target paths and resolve symlinks
→ classify CREATE / SKIP_IDENTICAL / CONFLICT / MERGE_REQUIRED
→ emit byte-bound ordered preview
→ stop by default
→ on explicit --apply re-observe all target paths
→ reject stale preview or unknown ownership
→ create only non-conflicting paths
→ verify written bytes
→ report exact changed, preserved and conflicted paths
```

The first implementation does not merge text automatically. `MERGE_REQUIRED`
is reported for human/agent bounded handling.

### 11.3 Product update and removal

```text
verify new source candidate and installed product manifests
→ detect local modifications against the installed manifest
→ classify replace / add / remove / conflict / preserve
→ show exact preview and rollback boundary
→ stop by default
→ on explicit --apply recheck source and target identities
→ stage the complete new aos/ beside the installed directory
→ verify staged product and self-test
→ atomically exchange directories on the same filesystem
→ retain one recoverable prior directory until final verification
→ restore prior directory if verification fails
→ never mutate root project/ or user-owned root files
```

The initial uninstall command is intentionally read-only. It identifies the
installed `aos/` subject and tells the user how to remove it manually while
preserving `project/`, root `AGENTS.md`, `START_HERE.md` and all user files.
Automatic destructive removal requires a later explicit protected-operation
contract.

### 11.4 Intent intake

```text
preserve exact human input and provenance
→ create RECEIVED record
→ agent separates problem, outcome and proposed solution
→ classify assumptions, unknowns, constraints and sensitive flags
→ validate schema and semantic invariants
→ ask only material questions
→ publish a distinguishable revision
→ render REVIEWABLE view
→ require separate exact-subject confirmation record
```

The deterministic CLI scaffolds, validates, renders and binds records. The AI
agent performs language interpretation under the workflow and cannot create the
human confirmation.

### 11.5 Status and continuation

```text
observe repository and Project Memory owners
→ reject stale or malformed records
→ select current exact subjects by explicit references
→ derive blockers, permissions and checks
→ render status + one next action
→ never promote derived output to owner
```

## 12. Root payload contract

`aos/ROOT_PAYLOAD.yaml` is the owner of the following exact records:

| Payload path | Install policy | Owner after install | Update policy |
|---|---|---|---|
| `AGENTS.md` | `MERGE_REQUIRED` | `USER_OWNED` | never replace automatically |
| `START_HERE.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/README.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/CURRENT.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/00_PROJECT.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/01_PRODUCT.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/02_ARCHITECTURE.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/03_DEVELOPMENT.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/intents/README.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/features/README.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/decisions/README.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/tasks/README.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/evidence/README.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/research/README.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |
| `project/lessons/README.md` | `CREATE_ONLY` | `USER_OWNED` | never replace automatically |

An existing `project/` is always preserved. Missing starter files may be
offered as independent create-only additions, never as a bulk overwrite.

## 13. Project template contracts

| Template | Required content |
|---|---|
| `project/README.md` | ownership, navigation, source precedence and minimal update rules |
| `project/CURRENT.md` | current subject, status axes, blockers, checks, permissions and one next action |
| `project/00_PROJECT.md` | identity, problem, desired outcome, scope, non-goals, constraints and success signals |
| `project/01_PRODUCT.md` | users/JTBD, problems, journeys, requirements, acceptance and open product decisions |
| `project/02_ARCHITECTURE.md` | context, components, public contracts, data ownership, security, persistence and ADR links |
| `project/03_DEVELOPMENT.md` | local setup, implementation flow, tests, recovery and Git boundaries |
| `project/intents/README.md` | Intent states, naming, original-input preservation and confirmation rule |
| `project/features/README.md` | one Feature Passport per admitted feature; Product Spec remains cross-feature owner |
| `project/decisions/README.md` | decision format, exact-subject binding, non-grants and supersession |
| `project/tasks/README.md` | bounded tasks only when needed; no automatic backlog bureaucracy |
| `project/evidence/README.md` | current subject identity, checks, results, limitations and no approval inference |
| `project/research/README.md` | narrow question, source/ref/path, finding and target relevance |
| `project/lessons/README.md` | symptom, root cause, correction, regression check and applicability |

Templates contain prompts and examples but no facts from notebook or AOS-3.
Optional sections are omitted rather than filled with ceremonial placeholders.

## 14. Security and privacy baseline

- Core is local-only and contains no network client.
- External content is untrusted data and cannot modify authority or workflow.
- YAML uses safe loading; unknown fields and duplicate keys are rejected where
  the format parser exposes them.
- All target paths are repository-relative and confined after symlink
  resolution.
- Secrets, credential-bearing remotes and raw environment dumps are never
  written to Project Memory or reports.
- `--apply` cannot widen the previewed path set.
- Decision records use honest `LOCAL_DECLARED_EXACT_SUBJECT` authenticity; no
  cryptographic identity or non-repudiation is claimed.
- Git is read-only unless an exact later task authorizes an individual Git
  action. Product code contains no automatic Git mutation in the first release.

## 15. Test and acceptance matrix

### 15.1 Unit and schema

- every closed enum rejects unknown values;
- bool is not accepted where integer is required;
- missing and `null` remain distinct;
- all templates validate against their owning schema;
- path normalization rejects absolute paths, `..` escape and symlink escape;
- raw-byte identity is deterministic;
- Intent transition rules reject invalid promotion;
- Evidence and technical PASS cannot satisfy a decision field.

### 15.2 Contract

- manifest inventory is complete, sorted and self-excluding;
- `aos/AGENTS.md`, CLI and workflows use the same authority semantics;
- Product Spec and Feature Passport have non-overlapping fact ownership;
- root payload has one policy and one post-install owner per path;
- every write command has a read-only default or explicit write verb;
- JSON result envelope and exit code agree;
- `--help`, validation and preview produce no durable writes.

### 15.3 Integration

- request → Intent candidate → agent clarification → REVIEWABLE;
- REVIEWABLE exact bytes → explicit decision record → CONFIRMED;
- manifest verification → install preview → apply → byte verification;
- verified new candidate → update preview → staged replacement → rollback or
  verified completion;
- uninstall preview lists only the installed product and never lists
  `project/` or user-owned root paths;
- existing `AGENTS.md` produces `MERGE_REQUIRED` and no overwrite;
- existing `project/` is preserved while missing files are offered separately;
- interrupted apply reports exact partial state and performs no auto-retry;
- status is rebuilt from owners after a fresh process start.

### 15.4 Portability

```text
copy only aos/ to a clean temporary repository
→ remove access to AOS-3 parent directories
→ create Python 3.12 virtual environment
→ install from aos/ and its declared lock
→ verify MANIFEST.txt
→ run aos selftest
→ preview and apply root payload
→ create and validate an Intent Record
→ confirm there were no unexpected external writes or network calls
```

### 15.5 Required negative cases

- manifest mismatch or unexpected file;
- empty intent promoted to REVIEWABLE;
- generated human decision;
- stale subject digest;
- stale installation preview;
- user-owned path overwrite attempt;
- hidden dependency on `../docs`, `../development`, `../tests` or `../tools`;
- validation that mutates its subject;
- `NOT_RUN` reported as PASS;
- Git operation without separate permission;
- secret or absolute local path in output.

## 16. Implementation sequence

This is an engineering order, not a new lifecycle controller.

### Slice 0 — Repository and portable foundation

Create the root files, target owner documents, exact `aos/` tree, package
metadata, deterministic manifest builder and bootstrap verifier. Success means
`aos/` installs from its own directory and passes manifest/link/schema checks.

### Slice 1 — Accepted FTR-001 outcome

Implement Intent schemas, domain validation, create/validate/review commands,
Codex workflow and exact local confirmation record. Success means a human
request becomes a source-preserving REVIEWABLE Intent Record and explicit
confirmation can bind its exact bytes without granting implementation or Git
authority.

### Slice 2 — Installation and Project Memory

Implement `ROOT_PAYLOAD.yaml`, preview-first install, create-only apply,
conflict reporting, `CURRENT.md` projection and isolated-copy tests. Success
means manual and automatic routes produce the same target shape while
preserving an existing `project/`.

### Slice 3 — Accepted FTR-003 outcome

Implement Product Spec and Feature Passport templates/schemas, ownership
links, slice comparison and review output. No feature or slice is selected by
the agent.

### Slice 4 — Bounded engineering loop

Add Task Brief, Evidence, validation and recovery operations only after dogfood
shows the record shapes are necessary. Keep normal reversible work on the
lightweight flow defined by root `AGENTS.md`.

### Later optional slices

Repository discovery, UI, retrieval, routing, CI/release helpers, plugins and
domain profiles remain separately admitted features. They cannot become Core
dependencies by convenience.

## 17. Migration construction rules

| Source class | Target treatment |
|---|---|
| accepted current canonical owners | ADAPT into target `docs/`; preserve fact ownership |
| accepted `AOS/portable/**` | ADAPT into `aos/docs/` and product entrypoints; changed bytes receive a new identity |
| accepted X1 FTR-001/FTR-003 package | use as contract source for first slices and schemas |
| accepted R2/global packages | supporting provenance; do not create duplicate owners |
| root AGENTS candidate | MOVE byte-for-byte to target root `AGENTS.md` |
| selected archive ADRs, research and fixtures | REFERENCE under `development/` or root tests only when used |
| controllers, run state and correction history | EXCLUDE from target product and normal root navigation |
| audits and acceptance records | preserve only under migration provenance; never runtime dependency |

Every adapted target file is a new subject. No source acceptance is silently
transferred to changed bytes.

## 18. Review decisions and bounded unknowns

Only these items remain outside agent-owned reversible HOW:

| ID | Subject | Current state | Recommendation | Blocking scope |
|---|---|---|---|---|
| `AOS3-HR-001` | public license | `DEFER_UNTIL_PUBLIC_DISTRIBUTION` | choose before public visibility or release | public distribution only |
| `AOS3-HR-002` | official supported OS matrix | `NOT_SELECTED` | macOS and Linux first; Windows compatibility not claimed until tested | public compatibility claim only |
| `AOS3-HR-003` | target remote creation and initial Push | `NOT_RUN` | create private `NMF13579/AOS-3` with clean history after draft acceptance | repository delivery only |

These do not block review of this draft or local implementation design. They
do block dependent public compatibility, license and remote-delivery claims.

## 19. Draft acceptance criteria

This blueprint is ready for human review when:

1. all accepted current decisions are represented without authority expansion;
2. target root roles and one-owner boundaries are explicit;
3. the initial `aos/` path set is closed and counted;
4. root payload paths and ownership policies are complete;
5. Project Memory templates contain enough information for future agents;
6. FTR-001 first-slice behavior maps to schemas, CLI, algorithms and tests;
7. installation, update, conflict and recovery boundaries are testable;
8. `aos/` has no required dependency on the parent AOS-3 repository;
9. security, privacy and Git defaults fail closed;
10. remaining human decisions are material, bounded and non-blocking for draft
    review.

## 20. Construction status

```yaml
construction_result: PASS
semantic_self_review: PASS
markdown_checks: PASS
exact_identity: COMPUTED_EXTERNALLY_AT_HANDOFF
runtime_tests: NOT_RUN
human_review: NOT_RUN
implementation_authorization: NONE
git_authorization: NONE
next_action: HUMAN_REVIEW_OF_EXACT_DRAFT
```
